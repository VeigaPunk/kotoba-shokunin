#!/usr/bin/env python3
"""merge_census.py -- join the round-74 sibling rows TSVs and scout JSONs into
(a) the body table of `corpus/knowledge/sibling-overlap-census-round74.md` and
(b) the rows of `PROVINCE.md` section `## Adjacent`.

Seat contract (ExecSibMergeR74; schemas also sent to the sibling seats):

  rows TSV -- four files, `.ufo/waves/round-74/w1/build/ExecSibRows{A,B,C,D}R74/rows.tsv`,
  tab-separated, one row per lane, optional header line whose first cell is
  `lane`.  Positional order when headerless:

      lane  branch  commit  skill_file  names_kotoba  arbitration  [quote_at]  [quote]  [delta]

  The first six are required; `quote_at`, `quote` and `delta` are optional and,
  when non-empty, are cross-checked against the scout JSON / the recomputation.

  scout JSON -- ten files, `.ufo/waves/round-74/w1/build/ScoutSib*R74/<lane>.json`:

      lane, head40, proposed_classification, quote, quote_path_line, boundary,
      r49_classification, changed

Output shapes (`--shape`):

  census      9 r49 columns + a trailing `delta` cell (the assigned r74 shape).
  census-r49  the round-49 shape exactly, 9 columns, byte-identical row form.
              Needed because the base copy of `verifiers/check_sibling_census.py`
              selects a table only when its header has exactly CENSUS_COLUMNS = 9
              cells (`_select_table`, verifiers/check_sibling_census.py:143,233);
              a 10-column table is refused there as "census table not found".
  province    `| lane | classification | commit | boundary |` rows.

Refusals: every one exits 2 and names the lane (or the path) it refuses:

  * a missing input file (explicit path, or one of the four declared rows files
    under `--inputs-root`), and an input set with no scout JSON at all;
  * a lane in two input files (two TSVs, two JSONs, or both);
  * a lane present in the TSVs but not the JSONs, or the reverse;
  * a head40/commit that is not 40 hex, or differs from the lane's head in the
    freeze file, or a branch that differs from the freeze file's branch;
  * an empty quote, an empty required field, a classification (proposed or r49)
    outside contested/adjacent/none, a `quote_path_line` that is not PATH:LINE;
  * a lane set that is not exactly the freeze file's lanes (missing or extra);
  * a `|` in any output cell.  Escaping is the author's job; this tool refuses
    rather than rewriting a cell (the checker splits on unescaped pipes);
  * a TSV quote/quote_at that disagrees with the scout JSON's, and a TSV `delta`
    that disagrees with the recomputation;
  * `changed` contradicting the recomputed delta (`--shape census` only).

`delta` is the plan's C2 (c) recomputation, verbatim:
`git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`, whitespace
collapsed, or `none` when the output is empty.  The r49 pin is the commit in the
`## Adjacent` table of `PROVINCE.md` at `--base-rev` (the frozen base), read with
`git show`, so the pins survive the landing of the round-74 rows; `--r49-pins`
overrides it with a `lane<TAB>commit` file.

Read-only except for `--out`.  Stdlib only (Python >= 3.9).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

LANE_SUFFIX = "-shokunin"
CLASSIFICATIONS = ("contested", "adjacent", "none")
HEX40 = re.compile(r"\A[0-9a-fA-F]{40}\Z")
WS_RUN = re.compile(r"\s+")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
SEPARATOR_CELL = re.compile(r"\A:?-{2,}:?\Z")
PATH_LINE = re.compile(r"\A[^:\s][^:\n]*:[0-9]+\Z")
SHORTSTAT = re.compile(r"(\d+) files? changed"
                       r"(?:, (\d+) insertions?\(\+\))?"
                       r"(?:, (\d+) deletions?\(-\))?")
BASE_REV = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
DEFAULT_FLEET = "/home/vgpnk/Projects/shokunin"
ROWS_DIRS = ("ExecSibRowsAR74", "ExecSibRowsBR74", "ExecSibRowsCR74",
             "ExecSibRowsDR74")

ROW_FIELDS = ("lane", "branch", "commit", "skill_file", "names_kotoba",
              "arbitration", "quote_at", "quote", "delta")
ROW_REQUIRED = 6                      # the six cells a rows seat must supply
SCOUT_FIELDS = ("lane", "head40", "proposed_classification", "quote",
                "quote_path_line", "boundary", "r49_classification", "changed")

HEADER_ALIASES = {
    "lane": "lane", "branch": "branch", "commit": "commit", "head": "commit",
    "head40": "commit", "skill file": "skill_file", "skill_file": "skill_file",
    "path": "skill_file",
    "names kotoba": "names_kotoba", "names_kotoba": "names_kotoba",
    "arbitration": "arbitration", "quote at": "quote_at",
    "quote_at": "quote_at", "path:line": "quote_at", "path_line": "quote_at",
    "scope quote at": "quote_at", "quote": "quote",
    "scope quote": "quote", "delta": "delta",
}
# A rows seat may pack extra evidence columns beside the join columns (r49_pin,
# kotoba_hits_*, scope_*, selfcheck, its own delta).  Those are ignored: this
# tool owns the delta cell and the scout JSON owns the classification, so a
# second copy in the TSV is evidence, not input.

CENSUS_HEADER = ("| lane | branch | commit | skill file | classification | "
                 "names kotoba | arbitration | scope quote at | scope quote |")
CENSUS_SEPARATOR = "|---|---|---|---|---|---|---|---|---|"
CENSUS_HEADER_DELTA = ("| lane | branch | commit | skill file | classification | "
                       "names kotoba | arbitration | scope quote at | scope quote | delta |")
CENSUS_SEPARATOR_DELTA = "|---|---|---|---|---|---|---|---|---|---|"
PROVINCE_HEADER = "| lane | classification | commit | boundary |"
PROVINCE_SEPARATOR = "|---|---|---|---|"


class Refusals:
    """Collects every refusal so one run reports all of them."""

    def __init__(self):
        self.messages = []

    def add(self, subject, message):
        self.messages.append("REFUSE %s: %s" % (subject, message))

    def __bool__(self):
        return bool(self.messages)


# --------------------------------------------------------------------------
# small helpers (the same cell rules as verifiers/check_sibling_census.py)
# --------------------------------------------------------------------------

def collapse(text):
    return WS_RUN.sub(" ", text).strip()


def strip_wrapping(cell):
    """Remove a wrapping pair of double quotes or backticks, then whitespace."""
    s = cell.strip()
    changed = True
    while changed and len(s) >= 2:
        changed = False
        if (s[0] == '"' and s[-1] == '"') or (s[0] == "`" and s[-1] == "`"):
            s = s[1:-1].strip()
            changed = True
    return s


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [p.replace("\\|", "|").strip() for p in CELL_SPLIT.split(s)]


def is_separator_row(cells):
    return bool(cells) and all(SEPARATOR_CELL.match(c) for c in cells)


def markdown_tables(text):
    """[(header_cells, [row_cells, ...]), ...] for every pipe-table block."""
    blocks, current = [], []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    tables = []
    for block in blocks:
        header = split_row(block[0])
        body = block[1:]
        if body and is_separator_row(split_row(body[0])):
            body = body[1:]
        tables.append((header, [split_row(line) for line in body]))
    return tables


def normalize_lane(cell):
    s = strip_wrapping(cell)
    low = s.lower()
    if low.endswith(LANE_SUFFIX):
        s = s[: -len(LANE_SUFFIX)]
    return s.strip().lower()


def one_line(subject, field, value, refusals):
    """A markdown cell is one line: refuse tabs/newlines, collapse if present."""
    if "\n" in value or "\t" in value:
        value = collapse(value)
    if not value:
        refusals.add(subject, "empty %s" % field)
    return value


def check_cell(subject, field, value, refusals):
    if "|" in value:
        refusals.add(subject, "%s cell contains a `|` (%r); escaping is the "
                              "author's job, this tool refuses" % (field, value))
    if "\n" in value or "\t" in value:
        refusals.add(subject, "%s cell spans more than one line" % field)


# --------------------------------------------------------------------------
# inputs
# --------------------------------------------------------------------------

def read_freeze(path, refusals):
    """{lane: (branch, head40)} from the frozen heads receipt."""
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        refusals.add(str(path), "missing freeze file (%s)" % exc)
        return {}
    lanes = {}
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            refusals.add(str(path), "line %d is not lane<TAB>branch<TAB>head" % number)
            continue
        lane = normalize_lane(parts[0])
        branch, head = parts[1].strip(), parts[2].strip().lower()
        if lane in lanes:
            refusals.add(lane, "lane appears twice in the freeze file %s" % path)
            continue
        lanes[lane] = (branch, head)
    if not lanes:
        refusals.add(str(path), "freeze file names no lane")
    return lanes


def read_rows(path, refusals):
    """[(lane, record, path), ...] from one rows TSV."""
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        refusals.add(str(path), "missing rows file (%s)" % exc)
        return []
    lines = [line for line in text.splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines:
        refusals.add(str(path), "rows file is empty")
        return []
    header = None
    first = [cell.strip() for cell in lines[0].split("\t")]
    if first and first[0].lower() in ("lane", "lane name"):
        header = [HEADER_ALIASES.get(cell.lower().replace("-", "_"), None)
                  for cell in first]
        missing = [f for f in ROW_FIELDS[:ROW_REQUIRED] if f not in header]
        if missing:
            refusals.add(str(path), "header lacks required column(s): %s "
                                    "(found %r)" % (", ".join(missing), first))
            return []
        lines = lines[1:]
    out = []
    for number, line in enumerate(lines, 1):
        cells = line.split("\t")
        if header is None:
            if len(cells) < ROW_REQUIRED:
                refusals.add(str(path), "data row %d has %d cells, needs at least "
                                        "%d (lane branch commit skill_file "
                                        "names_kotoba arbitration)"
                                        % (number, len(cells), ROW_REQUIRED))
                continue
            values = dict(zip(ROW_FIELDS, cells))
        else:
            values = {field: "" for field in ROW_FIELDS}
            for name, cell in zip(header, cells):
                if name is not None:
                    values[name] = cell
        lane = normalize_lane(values["lane"])
        if not lane:
            refusals.add(str(path), "data row %d has an empty lane cell" % number)
            continue
        values = {k: v.strip() for k, v in values.items()}
        out.append((lane, values, str(path)))
    return out


def changed_flag(value, lane, refusals):
    """The scout's `changed` as a boolean when it carries one, else None.

    The seats write this cell as a boolean, an object (`{"differs": false,
    "why": "..."}`) or a prose note ("No. Classification unchanged; delta ...").
    Only a boolean, or an object's boolean `differs`/`changed` key, can drive
    the delta cross-check; prose is evidence and is not parsed for a verdict.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, dict):
        for key in ("differs", "changed", "is_changed"):
            if isinstance(value.get(key), bool):
                return value[key]
        return None
    if isinstance(value, str) and value.strip():
        return None
    refusals.add(lane, "`changed` is empty or of no usable type (%r)" % (value,))
    return None


def read_scout(path, refusals):
    """[(lane, record, path), ...] from one scout JSON file."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        refusals.add(str(path), "missing scout file (%s)" % exc)
        return []
    except ValueError as exc:
        refusals.add(str(path), "not JSON (%s)" % exc)
        return []
    if not isinstance(data, dict):
        refusals.add(str(path), "top-level JSON value is not an object")
        return []
    lane = normalize_lane(str(data.get("lane", "")))
    if not lane:
        refusals.add(str(path), "empty or missing `lane`")
        return []
    record = {}
    for field in SCOUT_FIELDS:
        value = data.get(field)
        if field == "changed":
            if value is None:
                refusals.add(lane, "missing `changed` in %s" % path)
            record[field] = changed_flag(value, lane, refusals)
            continue
        if value is None:
            refusals.add(lane, "missing `%s` in %s" % (field, path))
            value = ""
        elif not isinstance(value, str):
            refusals.add(lane, "`%s` is %r, not a string" % (field, value))
            value = str(value)
        record[field] = value.strip()
    return [(lane, record, str(path))]


def expand_rows(paths, inputs_root, refusals):
    if inputs_root:
        root = Path(inputs_root)
        for name in ROWS_DIRS:
            paths = list(paths) + [str(root / name / "rows.tsv")]
    return list(paths)


def expand_scouts(paths, inputs_root, refusals):
    if inputs_root:
        root = Path(inputs_root)
        found = sorted(str(p) for p in root.glob("ScoutSib*R74/*.json"))
        if not found:
            refusals.add(str(root), "no ScoutSib*R74/*.json under the inputs root")
        paths = list(paths) + found
    expanded = []
    for path in paths:
        p = Path(path)
        if p.is_dir():
            files = sorted(str(f) for f in p.glob("*.json"))
            if not files:
                refusals.add(str(p), "directory holds no *.json")
            expanded.extend(files)
        else:
            expanded.append(str(p))
    return expanded


# --------------------------------------------------------------------------
# delta (plan C2 (c))
# --------------------------------------------------------------------------

def git_show(repo, rev, path):
    proc = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (rev, path)],
                          capture_output=True, text=True)
    return proc.stdout if proc.returncode == 0 else None


def load_r49_pins(args, refusals):
    if args.r49_pins:
        pins = {}
        try:
            text = Path(args.r49_pins).read_text(encoding="utf-8")
        except OSError as exc:
            refusals.add(args.r49_pins, "missing r49 pins file (%s)" % exc)
            return {}
        for line in text.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                refusals.add(args.r49_pins, "line %r is not lane<TAB>commit" % line)
                continue
            pins[normalize_lane(parts[0])] = parts[1].strip().lower()
        return pins
    text = git_show(args.lane_root, args.base_rev, "PROVINCE.md")
    if text is None:
        refusals.add(str(args.lane_root), "git show %s:PROVINCE.md failed"
                                          % args.base_rev)
        return {}
    for header, rows in markdown_tables(text):
        lowered = [cell.lower() for cell in header]
        if len(header) != 4 or lowered[0] != "lane" or "commit" not in lowered[2]:
            continue
        index = lowered.index("commit")
        pins = {}
        for cells in rows:
            if len(cells) != 4:
                continue
            lane = normalize_lane(cells[0])
            if lane:
                pins[lane] = cells[index].strip().lower()
        if pins:
            return pins
    refusals.add(str(args.lane_root), "no 4-column `| lane | classification | "
                                      "commit | boundary |` table in PROVINCE.md "
                                      "at %s" % args.base_rev)
    return {}


def shortstat_delta(args, lane, pin, head, refusals):
    repo = Path(args.fleet_root) / (lane + LANE_SUFFIX)
    proc = subprocess.run(["git", "-C", str(repo), "diff", "--shortstat",
                           pin, head, "--", "SKILL.md", "PROVINCE.md"],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        refusals.add(lane, "git diff --shortstat %s %s in %s failed: %s"
                           % (pin[:12], head[:12], repo,
                              collapse(proc.stderr) or "exit %d" % proc.returncode))
        return None
    text = collapse(proc.stdout)
    if not text:
        return "none"
    if args.delta_format == "plusminus":
        match = SHORTSTAT.search(text)
        if not match:
            refusals.add(lane, "cannot read a git diff --shortstat line: %r" % text)
            return None
        return "+%d/-%d" % (int(match.group(2) or 0), int(match.group(3) or 0))
    return text


# --------------------------------------------------------------------------
# merge
# --------------------------------------------------------------------------

def merge(args, refusals):
    freeze = read_freeze(args.freeze, refusals)
    rows = []
    for path in expand_rows(args.rows, args.inputs_root, refusals):
        rows.extend(read_rows(path, refusals))
    scouts = []
    for path in expand_scouts(args.scouts, args.inputs_root, refusals):
        scouts.extend(read_scout(path, refusals))

    merged = {}
    for lane, values, path in rows:
        if lane in merged:
            refusals.add(lane, "lane is in two rows files: %s and %s"
                               % (merged[lane]["_rows_path"], path))
            continue
        merged[lane] = {"_rows": values, "_rows_path": path}
    for lane, values, path in scouts:
        if lane not in merged:
            refusals.add(lane, "lane has a scout record (%s) but no rows row"
                               % path)
            continue
        if "_scout" in merged[lane]:
            refusals.add(lane, "lane is in two scout files: %s and %s"
                               % (merged[lane]["_scout_path"], path))
            continue
        merged[lane]["_scout"] = values
        merged[lane]["_scout_path"] = path

    for lane in sorted(merged):
        if "_scout" not in merged[lane]:
            refusals.add(lane, "lane has a rows row (%s) but no scout record"
                               % merged[lane]["_rows_path"])

    expected = set(freeze)
    seen = set(merged)
    for lane in sorted(expected - seen):
        refusals.add(lane, "lane in the freeze file %s has no row (missing file "
                           "or missing lane)" % args.freeze)
    for lane in sorted(seen - expected):
        refusals.add(lane, "lane is not in the freeze file %s" % args.freeze)

    pins = load_r49_pins(args, refusals) if args.shape == "census" else {}

    records = []
    for lane in sorted(seen):
        rec = merged[lane]
        values = rec.get("_rows")
        scout = rec.get("_scout")
        if values is None or scout is None:
            continue
        branch = one_line(lane, "branch", values["branch"], refusals)
        commit = values["commit"].strip()
        skill_file = one_line(lane, "skill_file", values["skill_file"], refusals)
        names = one_line(lane, "names_kotoba", values["names_kotoba"], refusals)
        arbitration = one_line(lane, "arbitration", values["arbitration"], refusals)
        classification = scout["proposed_classification"].strip().lower()
        r49_classification = scout["r49_classification"].strip().lower()
        quote = one_line(lane, "quote", strip_wrapping(scout["quote"]), refusals)
        quote_at = one_line(lane, "quote_path_line", scout["quote_path_line"], refusals)
        boundary = one_line(lane, "boundary", scout["boundary"], refusals)

        if not HEX40.match(commit):
            refusals.add(lane, "commit %r is not a 40-hex object id" % commit)
        if not HEX40.match(scout["head40"]):
            refusals.add(lane, "head40 %r is not a 40-hex object id" % scout["head40"])
        elif commit and commit.lower() != scout["head40"].strip().lower():
            refusals.add(lane, "rows commit %s differs from scout head40 %s"
                               % (commit, scout["head40"]))
        if classification not in CLASSIFICATIONS:
            refusals.add(lane, "proposed classification %r is not one of %s"
                               % (scout["proposed_classification"],
                                  "/".join(CLASSIFICATIONS)))
        if r49_classification not in CLASSIFICATIONS:
            refusals.add(lane, "r49 classification %r is not one of %s"
                               % (scout["r49_classification"],
                                  "/".join(CLASSIFICATIONS)))
        if quote_at and not PATH_LINE.match(quote_at):
            refusals.add(lane, "quote_path_line %r is not PATH:LINE" % quote_at)

        if lane in freeze:
            freeze_branch, freeze_head = freeze[lane]
            if freeze_head and commit and commit.lower() != freeze_head:
                refusals.add(lane, "head40 %s differs from the freeze head %s in %s"
                                   % (commit, freeze_head, args.freeze))
            if freeze_branch and branch and branch != freeze_branch:
                refusals.add(lane, "branch %r differs from the freeze branch %r"
                                   % (branch, freeze_branch))

        # a rows seat may leave the quote cells empty (the scout owns them);
        # when it fills them they must agree with the scout record.
        rows_quote = strip_wrapping(values["quote"])
        if rows_quote and collapse(rows_quote) != collapse(quote):
            refusals.add(lane, "rows quote differs from the scout quote: %r vs %r"
                               % (rows_quote, quote))
        rows_quote_at = values["quote_at"].strip()
        if rows_quote_at and rows_quote_at != quote_at:
            refusals.add(lane, "rows quote_at %r differs from the scout "
                               "quote_path_line %r" % (rows_quote_at, quote_at))

        delta = ""
        if args.shape == "census":
            pin = pins.get(lane)
            if not pin:
                refusals.add(lane, "no r49 pin for the lane (base PROVINCE.md "
                                   "section `## Adjacent`)")
            else:
                delta = shortstat_delta(args, lane, pin, commit.lower(), refusals) or ""
                # The rows seats also carry a delta column (ExecSibRowsDR74's
                # mechanics.tsv uses `+ins/-del`); it is evidence.  This tool
                # owns the cell and emits the plan's C2 (c) shortstat string.
                changed = scout["changed"]
                if changed is not None and delta:
                    if changed is False and delta != "none":
                        refusals.add(lane, "changed=false but git diff --shortstat "
                                           "reports %r" % delta)
                    if changed is True and delta == "none":
                        refusals.add(lane, "changed=true but git diff --shortstat "
                                           "is empty for SKILL.md and PROVINCE.md")

        census_cells = [lane, branch, commit, skill_file, classification, names,
                        arbitration, quote_at, '"%s"' % quote]
        province_cells = [lane, classification, commit, boundary]
        for field, cell in zip(ROW_FIELDS[:9], census_cells):
            check_cell(lane, field, cell, refusals)
        for field, cell in zip(("lane", "classification", "commit", "boundary"),
                               province_cells):
            check_cell(lane, field, cell, refusals)
        if delta:
            check_cell(lane, "delta", delta, refusals)
        records.append({"census": census_cells, "province": province_cells,
                        "delta": delta})

    return records


# --------------------------------------------------------------------------
# output
# --------------------------------------------------------------------------

def render(records, shape):
    lines = []
    if shape == "census":
        lines.append(CENSUS_HEADER_DELTA)
        lines.append(CENSUS_SEPARATOR_DELTA)
        for record in records:
            lines.append("| " + " | ".join(record["census"] + [record["delta"]]) + " |")
    elif shape == "census-r49":
        lines.append(CENSUS_HEADER)
        lines.append(CENSUS_SEPARATOR)
        for record in records:
            lines.append("| " + " | ".join(record["census"]) + " |")
    elif shape == "province":
        lines.append(PROVINCE_HEADER)
        lines.append(PROVINCE_SEPARATOR)
        for record in records:
            lines.append("| " + " | ".join(record["province"]) + " |")
    else:  # pragma: no cover - argparse restricts the value
        raise SystemExit("unknown shape %r" % shape)
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="join the round-74 sibling rows TSVs and scout JSONs into "
                    "the census table and the PROVINCE section-Adjacent rows")
    parser.add_argument("--rows", action="append", default=[], metavar="PATH",
                        help="rows.tsv (repeatable; a directory expands to its "
                             "*.tsv siblings by explicit file only)")
    parser.add_argument("--scouts", action="append", default=[], metavar="PATH",
                        help="scout .json file or directory (repeatable)")
    parser.add_argument("--inputs-root", metavar="DIR",
                        help="expand the declared inputs: the four "
                             "ExecSibRows{A,B,C,D}R74/rows.tsv and "
                             "ScoutSib*R74/*.json under DIR")
    parser.add_argument("--freeze", required=True, metavar="PATH",
                        help="the frozen sibling heads TSV")
    parser.add_argument("--shape", default="census",
                        choices=("census", "census-r49", "province"))
    parser.add_argument("--fleet-root", default=DEFAULT_FLEET)
    parser.add_argument("--lane-root", default=str(Path(__file__).resolve().parents[5]))
    parser.add_argument("--base-rev", default=BASE_REV,
                        help="revision whose PROVINCE.md section-Adjacent rows "
                             "carry the r49 pins")
    parser.add_argument("--r49-pins", metavar="PATH",
                        help="lane<TAB>commit file overriding the base-rev read")
    parser.add_argument("--delta-format", default="shortstat",
                        choices=("shortstat", "plusminus"),
                        help="the delta cell: the collapsed `git diff --shortstat` "
                             "text (plan C2 (c), default) or `+<ins>/-<del>`, the "
                             "form check_sibling_reread.py:render_delta compares")
    parser.add_argument("--out", metavar="PATH", help="write here instead of stdout")
    args = parser.parse_args(argv)

    refusals = Refusals()
    records = merge(args, refusals)
    if refusals:
        for message in refusals.messages:
            print(message, file=sys.stderr)
        print("REFUSE %d problem(s); nothing written" % len(refusals.messages),
              file=sys.stderr)
        return 2
    text = render(records, args.shape)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
