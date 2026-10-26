#!/usr/bin/env python3
r"""check_sibling_reread.py -- frozen counter for the round-74 C2 (freshness) claim.

Landing path (intended): `verifiers/check_sibling_reread.py` in
/home/vgpnk/Projects/shokunin/kotoba-shokunin.

Frozen predicate (round-74 plan § C2, the same sentence in the plan, in this
docstring and in the receipt):

    python3 -B verifiers/check_sibling_reread.py --rev <rev>
        -> prints "sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads N of 20", exit 0 when N == 20

AMENDED BEFORE ANY DATA by plans/round-74-addendum-1.md E1.2: the headline's
"re-read" became "re-pinned, re-located and re-diffed" (no counter reads for
meaning); conjunct (e) (a whole-file `kotoba` clause that contradicted (a) and
made tabi's honest `none` row unreachable) is withdrawn -- the base checker's
none rule (description and PROVINCE.md) inside (a) is the rule, and the lanes
whose SKILL.md body names kotoba under a `none` row are PRINTED, not counted;
conjunct (f) is added: an eleventh `evidence` cell
`<path>:<line> <changed|unchanged> "<6-25-word quote>"` whose line is
re-located (+-2 lines) at the frozen head of the sibling file (or, behind the
`kotoba/` prefix, in this lane's file at --rev), is not a heading, and whose
changed/unchanged flag the counter recomputes against the round-49 pin (or the
base revision for a `kotoba/` file).  The pure carry-forward world is measured
by the seats and reported as the upper bound a mechanical re-pin reaches.

Why this file exists
--------------------
`PROVINCE.md` § Adjacent and `corpus/knowledge/sibling-overlap-census-round49.md`
state each sibling lane's boundary at a commit pinned at round 49-50.  At the
round-74 base 15 of those 20 siblings' `SKILL.md` or `PROVINCE.md` have changed
since the pin (`receipts/sibling-staleness-base.tsv`): the Adjacent table is a
claim about today's siblings read from yesterday's bytes.  The round-74 entry
`corpus/knowledge/sibling-overlap-census-round74.md` re-pins every sibling lane
at the heads frozen in `receipts/sibling-heads-freeze.tsv`; this counter counts
how many lanes are re-pinned AND re-read, from committed bytes only.

What it measures
----------------
Frozen pins (never read from the revision measured, Q28/Q33):

  * `BASE_REV` -- the round-74 base commit.  The round-49 pins and the base
    copy of the census checker are read from it, so a measured revision cannot
    supply its own checker or its own idea of "the old pin".
  * `BASE_CHECKER_SHA256` -- the sha256 of `verifiers/check_sibling_census.py`
    at BASE_REV.  The bytes are fetched with `git show BASE_REV:<path>` from
    the measured repository, hashed, and refused when they differ.  The
    round-49 row checks are therefore the base's code, not this file's.
  * `FREEZE_SHA256` -- the sha256 of `receipts/sibling-heads-freeze.tsv`, the
    L1's freeze written before any wave-1 seat ran.  `--freeze PATH` overrides
    the file (a seat may point at a copy); the default path is sha-pinned.
  * `FREEZE_LANES` -- the frozen lane count.  A freeze file that does not hold
    exactly 20 lanes is a could-not-evaluate, never a lower denominator.

Lane `L` (one of the 20 frozen lanes) is RE-PINNED AND RE-READ at `--rev` iff
all of:

  (a) entry row -- `corpus/knowledge/sibling-overlap-census-round74.md` at
      `--rev` holds exactly one row for `L` in the round-49 nine-cell row shape
      plus a tenth `delta` cell, and that row passes the BASE checker's row
      checks.  The tenth cell is stripped here and the nine remaining cells are
      handed to the base copy's `check_census()`; the base's parser and its
      row checks are used unchanged (its bytes are never edited).  The base's
      census-wide lane-set and duplicate-row checks are the base's too and must
      come back clean.
  (b) commit cell -- equals `L`'s head in the freeze file, exact 40-hex
      equality, no prefix; and that commit is an ancestor of the lane's branch
      head at measurement (`refs/heads/<branch>` from the freeze row).  The
      freeze's two blob cells are re-derived from the same commit: a freeze
      file whose blob columns do not describe its own head is refused.
  (c) delta cell -- equals this counter's recomputation of
      `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`,
      rendered `+<insertions>/-<deletions>` summed over both files, `none`
      when the diff is empty.  The r49 pin is the commit cell of the lane's
      row in `PROVINCE.md` at BASE_REV.
  (d) PROVINCE row -- `## Adjacent` at `--rev` carries `L`'s row with the same
      commit and the same classification as the entry row.
  (e) no false `none` -- a row classified `none` is refused when the lane's
      pinned `SKILL.md` OR `PROVINCE.md` contains the whole word `kotoba`
      (recomputed from the frozen head; the base checker only looks at the
      description and at PROVINCE.md).

Bound (Q26/Q51): this counter measures pins, one shortstat delta, the cells,
quote location and the mechanical `none` rule.  It does NOT measure whether
`adjacent`/`contested`/`none` is the right classification or whether a
boundary sentence reads correctly; that is a reviewer judgement, assigned to
named non-author wave-2 seats.  Siblings keep moving after the freeze: a row
is valid at its frozen head, not at the round end.

Exit ladder (family contract):
  0  N == 20, the base census-wide checks are clean and no guard fired
  1  N < 20, or the base census-wide checks failed -- every failing lane is
     named on stdout
  2  usage error / could not evaluate: bad arguments, not a git work tree, the
     base checker absent or its sha256 not the pin, the freeze file absent,
     sha-mismatched or not 20 lanes

Usage:
    check_sibling_reread.py --rev <rev> [--repo DIR] [--fleet DIR] [--freeze PATH]
    check_sibling_reread.py --emit-cells [--repo DIR] [--fleet DIR]
    check_sibling_reread.py --self-test

`--emit-cells` prints the mechanical cells an entry author must copy
(lane, frozen commit, skill file, names-kotoba, arbitration, delta), recomputed
from the frozen heads with the base copy's helpers.  It is a convenience for
the seats; the counter never accepts its output as a verdict.

Read-only: it reads the lane repository through `git show` at the named
revisions and the sibling lanes through `git -C <fleet>/<lane>-shokunin`; it
writes nothing outside its own temporary directory.

Stdlib only (Python >= 3.9).
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

LANE_SUFFIX = "-shokunin"
SELF_LANE = "kotoba"
DEFAULT_FLEET = "/home/vgpnk/Projects/shokunin"

# Round-74 base commit: the measured revision supplies bytes, never code.
BASE_REV = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
BASE_CHECKER_PATH = "verifiers/check_sibling_census.py"
BASE_CHECKER_SHA256 = "2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7"

ENTRY_PATH = "corpus/knowledge/sibling-overlap-census-round74.md"
PROVINCE_PATH = "PROVINCE.md"
SKILL_PATH = "SKILL.md"
FREEZE_PATH = ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
FREEZE_SHA256 = "6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d"
FREEZE_LANES = 20

CENSUS_COLUMNS = 11          # round-49 nine + `delta` + `evidence`
EVIDENCE_COLUMN = "evidence"
DELTA_COLUMN = "delta"
NO_SKILL = "-"               # the freeze's "no such blob" cell
CLASSIFICATIONS = ("contested", "adjacent", "none")

HEX40 = re.compile(r"\A[0-9a-fA-F]{40}\Z")
SHORTSTAT = re.compile(r"(\d+) files? changed"
                       r"(?:, (\d+) insertions?\(\+\))?"
                       r"(?:, (\d+) deletions?\(-\))?")


class UsageError(Exception):
    """Raised for anything that makes the measurement impossible (exit 2)."""


@dataclass(frozen=True)
class Pins:
    """The frozen inputs.  `PINS` below is the declared measurement; the
    self-test builds its own for a throwaway fixture fleet.  No CLI flag sets
    any field of it."""

    base_rev: str = BASE_REV
    base_checker_path: str = BASE_CHECKER_PATH
    checker_sha256: str = BASE_CHECKER_SHA256
    entry_path: str = ENTRY_PATH
    freeze_path: str = FREEZE_PATH
    freeze_sha256: str = FREEZE_SHA256
    lanes: int = FREEZE_LANES


PINS = Pins()


# --------------------------------------------------------------------------
# git plumbing
# --------------------------------------------------------------------------

def _run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=None if cwd is None else str(cwd),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def git_ok(repo, *args):
    """(ok, stdout, stderr-first-line) for `git -C repo ...`."""
    proc = _run(["git", "-C", str(repo)] + list(args))
    err = proc.stderr.decode("utf-8", "replace").strip().splitlines()
    return proc.returncode == 0, proc.stdout.decode("utf-8", "replace"), \
        (err[0] if err else "")


def git_show_bytes(repo, rev, path):
    """Raw bytes of `rev:path`, or (None, error)."""
    proc = _run(["git", "-C", str(repo), "show", "%s:%s" % (rev, path)])
    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        return None, (err[0] if err else "git show failed")
    return proc.stdout, None


def git_show_text(repo, rev, path):
    raw, error = git_show_bytes(repo, rev, path)
    if raw is None:
        return None, error
    return raw.decode("utf-8", "replace"), None


def short(rev):
    return rev[:12]


def resolve_commit(repo, rev):
    ok, out, err = git_ok(repo, "rev-parse", "--verify", "--quiet",
                          "%s^{commit}" % rev)
    if not ok or not out.strip():
        raise UsageError("revision %r is not a commit in %s (%s)"
                         % (rev, repo, err or "no output"))
    return out.strip()


def lane_repo(fleet, lane):
    return Path(fleet) / (lane + LANE_SUFFIX)


def render_delta(shortstat):
    """`+<ins>/-<del>` from `git diff --shortstat`, `none` when empty."""
    text = " ".join(shortstat.split())
    if not text:
        return "none"
    match = SHORTSTAT.search(text)
    if not match:
        raise UsageError("cannot read a git diff --shortstat line: %r" % shortstat)
    insertions = int(match.group(2) or 0)
    deletions = int(match.group(3) or 0)
    return "+%d/-%d" % (insertions, deletions)


# --------------------------------------------------------------------------
# the freeze file
# --------------------------------------------------------------------------

FREEZE_FIELDS = ("lane", "branch", "head40", "skill_md_blob", "province_md_blob")


def parse_freeze(text):
    """lane -> {branch, head, skill_blob, province_blob}.  Raises UsageError."""
    lanes = {}
    problems = []
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cells = [c.strip() for c in line.split("\t")]
        if len(cells) != len(FREEZE_FIELDS):
            problems.append("line %d: %d tab-separated fields, expected %d"
                            % (number, len(cells), len(FREEZE_FIELDS)))
            continue
        row = dict(zip(FREEZE_FIELDS, cells))
        if not row["lane"]:
            problems.append("line %d: empty lane" % number)
            continue
        if not row["branch"]:
            problems.append("line %d (lane %s): empty branch"
                            % (number, row["lane"]))
            continue
        if not HEX40.match(row["head40"]):
            problems.append("line %d (lane %s): head40 %r is not a 40-hex object id"
                            % (number, row["lane"], row["head40"]))
            continue
        lane = row["lane"].lower()
        if lane in lanes:
            problems.append("line %d: lane %s appears twice" % (number, lane))
            continue
        lanes[lane] = {"branch": row["branch"],
                       "head": row["head40"].lower(),
                       "skill_blob": row["skill_md_blob"],
                       "province_blob": row["province_md_blob"]}
    if problems:
        raise UsageError("freeze file: " + "; ".join(problems))
    return lanes


def read_freeze(repo, override, pins):
    """(lanes, description).  `override` is a path or None for the pinned file.

    The default freeze file is read from the worktree when it is there, else
    from the newest commit that carries it: the plan commit holds the receipt
    in the object store even when a fleet-shaped sandbox is checked out at an
    earlier revision, so the do-nothing control at the base revision still
    reaches a verdict instead of a could-not-evaluate.  Both routes are
    sha256-pinned, so a tampered copy is refused wherever it is found.
    """
    if override:
        path = Path(override).expanduser()
        if not path.is_file():
            raise UsageError("freeze file %s does not exist" % path)
        raw = path.read_bytes()
        text = raw.decode("utf-8", "replace")
        lanes = parse_freeze(text)
        if len(lanes) != pins.lanes:
            raise UsageError("freeze file %s holds %d lane(s), the frozen "
                             "denominator is %d" % (path, len(lanes), pins.lanes))
        return lanes, "%s (override, %d lanes)" % (path, len(lanes))
    path = Path(repo) / pins.freeze_path
    if path.is_file():
        raw = path.read_bytes()
        source = "%s (pinned, worktree)" % path
    else:
        ok, out, _ = git_ok(repo, "rev-list", "--all", "--max-count=1", "--",
                            pins.freeze_path)
        rev = out.strip() if ok else ""
        raw = None
        if rev:
            raw, _ = git_show_bytes(repo, rev, pins.freeze_path)
        if raw is None:
            raise UsageError("freeze file %s is absent from the worktree and no "
                             "commit in this repository carries it (the default "
                             "path is pinned to sha256 %s)"
                             % (path, pins.freeze_sha256))
        source = "%s (pinned, object store at %s)" % (path, short(rev))
    digest = hashlib.sha256(raw).hexdigest()
    if digest != pins.freeze_sha256:
        raise UsageError("freeze file %s has sha256 %s, pinned %s: the frozen "
                         "heads changed" % (path, digest, pins.freeze_sha256))
    lanes = parse_freeze(raw.decode("utf-8", "replace"))
    if len(lanes) != pins.lanes:
        raise UsageError("freeze file %s holds %d lane(s), the frozen "
                         "denominator is %d" % (path, len(lanes), pins.lanes))
    return lanes, "%s, %d lanes, sha256 %s" % (source, len(lanes), digest)


# --------------------------------------------------------------------------
# the base copy of check_sibling_census.py (Q33: bytes, never the measured code)
# --------------------------------------------------------------------------

BASE_API = ("check_census", "token_in", "description_of", "fleet_lanes",
            "parse_blocks", "split_row", "extract_adjacent_section",
            "normalize_lane", "UsageError")


def load_base_checker(repo, pins, workdir):
    raw, error = git_show_bytes(repo, pins.base_rev, pins.base_checker_path)
    if raw is None:
        raise UsageError("the base census checker %s is absent at %s in %s (%s)"
                         % (pins.base_checker_path, short(pins.base_rev), repo, error))
    digest = hashlib.sha256(raw).hexdigest()
    if digest != pins.checker_sha256:
        raise UsageError("%s at %s has sha256 %s, pinned %s: the measured "
                         "repository does not carry the base copy"
                         % (pins.base_checker_path, short(pins.base_rev),
                            digest, pins.checker_sha256))
    target = Path(workdir) / "kotoba_base_check_sibling_census.py"
    target.write_bytes(raw)
    spec = importlib.util.spec_from_file_location(
        "kotoba_base_check_sibling_census", str(target))
    if spec is None or spec.loader is None:
        raise UsageError("cannot import the base census checker")
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001 -- any import failure is exit 2
        raise UsageError("the base census checker at %s does not import: %s"
                         % (short(pins.base_rev), exc))
    missing = [name for name in BASE_API if not hasattr(module, name)]
    if missing:
        raise UsageError("the base census checker at %s lacks %s: not the copy "
                         "this counter pins" % (short(pins.base_rev),
                                                ", ".join(missing)))
    return module


# --------------------------------------------------------------------------
# PROVINCE.md `## Adjacent`, by header name (tolerates added columns)
# --------------------------------------------------------------------------

def province_rows(base, text):
    """lane -> [row] from the `## Adjacent` table, keyed by header name.

    Returns None when PROVINCE.md holds no `## Adjacent` table with lane,
    classification and commit columns.  Column ORDER is read from the header,
    so a later column added to the table does not silently shift the cells.
    """
    body = base.extract_adjacent_section(text)
    if body is None:
        return None
    for block in base.parse_blocks(body):
        if block["sep_line"] is None:
            continue
        header = [c.strip().strip("`").lower() for c in block["header"]]

        def column(*names):
            for index, cell in enumerate(header):
                if cell in names:
                    return index
            return None

        index = {"lane": column("lane"),
                 "classification": column("classification", "class"),
                 "commit": column("commit")}
        if any(value is None for value in index.values()):
            continue
        rows = {}
        for line_no, cells in block["rows"]:
            if len(cells) <= max(index.values()):
                continue
            lane = base.normalize_lane(cells[index["lane"]])
            if not lane:
                continue
            rows.setdefault(lane, []).append(
                {"line": line_no,
                 "classification": cells[index["classification"]].strip().lower(),
                 "commit": cells[index["commit"]].strip()})
        return rows
    return None


# --------------------------------------------------------------------------
# the entry: round-49 nine-cell rows plus a tenth `delta` cell
# --------------------------------------------------------------------------

@dataclass
class EntryRow:
    line: int
    cells: list = field(default_factory=list)

    @property
    def lane(self):
        return self.cells[0] if self.cells else ""

    @property
    def delta(self):
        return self.cells[9].strip() if len(self.cells) == CENSUS_COLUMNS else ""

    @property
    def evidence(self):
        return self.cells[10].strip() if len(self.cells) == CENSUS_COLUMNS else ""


def parse_entry(base, text):
    """(rows, problem).  The table is the first block whose header has ten cells
    and whose last header cell is `delta`.  The base's own split_row/parse_blocks
    do the parsing: the extra cell is tolerated by stripping it, never by
    editing the base checker."""
    if text is None:
        return None, "entry absent at the measured revision"
    blocks = base.parse_blocks(text.splitlines())
    for block in blocks:
        if block["sep_line"] is None:
            continue
        header = block["header"]
        if len(header) != CENSUS_COLUMNS:
            continue
        if header[-1].strip().strip("`").lower() != EVIDENCE_COLUMN:
            continue
        if header[-2].strip().strip("`").lower() != DELTA_COLUMN:
            continue
        rows = [EntryRow(line=line_no, cells=cells)
                for line_no, cells in block["rows"]]
        return rows, None
    return None, ("entry has no census table with %d cells and trailing `%s`, "
                  "`%s` cells (round-49 nine-cell row shape plus both)"
                  % (CENSUS_COLUMNS, DELTA_COLUMN, EVIDENCE_COLUMN))


def _escape(cell):
    return cell.replace("|", "\\|")


def build_base_census(entry_rows):
    """(text, kept rows in table order) for the base checker.

    The rows are re-emitted with `|` escaped because the base's split_row
    unescapes it; each kept row's 1-based position in this projection is its
    row index in the base's own failure labels, which is how a base row refusal
    is mapped back to a lane.
    """
    kept = [row for row in entry_rows if len(row.cells) == CENSUS_COLUMNS]
    if not kept:
        return None, []
    header = ["lane", "branch", "commit", "skill file", "classification",
              "names kotoba", "arbitration", "scope quote at", "scope quote"]
    out = ["# round-74 sibling census, nine-cell projection", "",
           "| " + " | ".join(header) + " |",
           "|" + "|".join("---" for _ in header) + "|"]
    for row in kept:
        out.append("| " + " | ".join(_escape(c) for c in row.cells[:9]) + " |")
    return "\n".join(out) + "\n", kept


# --------------------------------------------------------------------------
# the measurement
# --------------------------------------------------------------------------

def measure(repo, rev, fleet, freeze_override, pins):
    """Run every check.  Returns a report dict; raises UsageError for exit 2."""
    commit = resolve_commit(repo, rev)
    fleet = Path(fleet).expanduser().resolve()
    if not fleet.is_dir():
        raise UsageError("fleet root %s is not a directory" % fleet)
    # M127: a fleet root that is the lane itself cannot hold the siblings; the
    # lane's own tree has no `*-shokunin` directory, so this would read as a
    # lane-set refusal rather than the caller's mistake.
    if fleet == repo.resolve():
        raise UsageError("the fleet root is the lane itself (%s); pass the "
                         "directory that holds the lane" % fleet)

    report = {"rev": commit, "base": pins.base_rev, "fleet": str(fleet),
              "lanes": [], "census_failures": [], "notes": [], "n": 0,
              "census_rows": 0, "census_verified": 0, "freeze": ""}

    with tempfile.TemporaryDirectory(prefix="sibling-reread-") as workdir:
        base = load_base_checker(repo, pins, workdir)
        frozen, freeze_note = read_freeze(repo, freeze_override, pins)
        report["freeze"] = freeze_note

        base_province, _ = git_show_text(repo, pins.base_rev, PROVINCE_PATH)
        if base_province is None:
            raise UsageError("%s is absent at the base revision %s"
                             % (PROVINCE_PATH, short(pins.base_rev)))
        base_pins = province_rows(base, base_province)
        if base_pins is None:
            raise UsageError("%s at %s holds no `## Adjacent` table with lane/"
                             "classification/commit columns"
                             % (PROVINCE_PATH, short(pins.base_rev)))

        province_at_rev, _ = git_show_text(repo, commit, PROVINCE_PATH)
        province_at_rev_rows = (None if province_at_rev is None
                                else province_rows(base, province_at_rev))

        entry_text, entry_error = git_show_text(repo, commit, pins.entry_path)
        entry_rows, entry_problem = parse_entry(base, entry_text)
        if entry_problem:
            report["notes"].append(entry_problem)
            entry_rows = []

        # (a), the base's part: one run over the nine-cell projection.
        census_text, kept = build_base_census(entry_rows)
        base_index = {}
        base_failures = []
        if census_text is None:
            report["census_failures"].append(
                "census table not found in %s at %s (no ten-cell row)"
                % (pins.entry_path, short(commit)))
        else:
            census_path = Path(workdir) / "census9.md"
            census_path.write_text(census_text, encoding="utf-8")
            try:
                result = base.check_census(census_path, fleet, None)
            except base.UsageError as exc:
                raise UsageError("the base census checker refused the projection: %s"
                                 % exc)
            report["census_rows"] = result["rows"]
            report["census_verified"] = result["verified"]
            base_failures = result["failures"]
            for number, row in enumerate(kept, 1):
                base_index[id(row)] = number
            for failure in base_failures:
                if not re.match(r"\Arow \d+ \(", failure):
                    report["census_failures"].append(failure)

        for lane in sorted(frozen):
            frozen_row = frozen[lane]
            reasons = []
            srepo = lane_repo(fleet, lane)
            row = _single_row(base, entry_rows, lane, reasons)
            delta_cell = ""

            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                delta_cell = row.delta
                number = base_index.get(id(row))
                if number is None:
                    reasons.append("row is not in the nine-cell projection")
                else:
                    prefix = "row %d (" % number
                    for failure in base_failures:
                        if failure.startswith(prefix):
                            reasons.append("base row check: " + failure)

            # freeze self-check: the blob columns must describe the head they name
            _check_freeze_blobs(srepo, lane, frozen_row, reasons)

            # (b): exact commit cell, and the frozen head is an ancestor of the branch
            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                cell = row.cells[2].strip()
                if cell.lower() != frozen_row["head"]:
                    reasons.append("commit cell %s is not the frozen head %s"
                                   % (short(cell) if cell else "<empty>",
                                      short(frozen_row["head"])))
            _check_ancestry(srepo, lane, frozen_row, reasons)

            # (c): the delta cell against the recomputation from the r49 pin
            pin_row = (base_pins.get(lane) or [])
            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                want, why = _recompute_delta(srepo, lane, pin_row,
                                             frozen_row["head"], pins)
                if why:
                    reasons.append(why)
                elif delta_cell != want:
                    reasons.append("delta cell %r but the recomputation gives %r "
                                   "(git diff --shortstat %s %s -- SKILL.md "
                                   "PROVINCE.md)"
                                   % (delta_cell, want,
                                      short(pin_row[0]["commit"]),
                                      short(frozen_row["head"])))

            # (d): the lane's row in PROVINCE.md § Adjacent at --rev
            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                _check_province_row(lane, row, province_at_rev_rows,
                                    province_at_rev, reasons)

            # (e) withdrawn (E1.2): the base none rule inside (a) is the rule.  A
            # `none` row whose SKILL.md body names kotoba is printed, not counted.
            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                _note_none_body_mention(base, srepo, lane, row,
                                        frozen_row["head"], report)

            # (f): the evidence cell, re-located and re-diffed
            if row is not None and len(row.cells) == CENSUS_COLUMNS:
                _check_evidence(base, repo, commit, srepo, lane, row,
                                frozen_row["head"], pin_row, pins, reasons)

            if not srepo.is_dir():
                reasons.insert(0, "no sibling repo at %s" % srepo)

            report["lanes"].append((lane, reasons))
            if not reasons:
                report["n"] += 1

    return report


def _single_row(base, entry_rows, lane, reasons):
    candidates = [row for row in entry_rows
                  if row.cells and base.normalize_lane(row.cells[0]) == lane]
    if not candidates:
        reasons.append("entry has no row for %s" % lane)
        return None
    if len(candidates) > 1:
        reasons.append("entry has %d rows for %s (lines %s); exactly one is "
                       "required" % (len(candidates), lane,
                                     ", ".join(str(r.line) for r in candidates)))
        return None
    row = candidates[0]
    if len(row.cells) != CENSUS_COLUMNS:
        reasons.append("row at entry line %d has %d cells, expected %d"
                       % (row.line, len(row.cells), CENSUS_COLUMNS))
        return None
    return row


def _check_freeze_blobs(srepo, lane, frozen_row, reasons):
    if not srepo.is_dir():
        return
    for path, key in ((SKILL_PATH, "skill_blob"), (PROVINCE_PATH, "province_blob")):
        ok, out, _ = git_ok(srepo, "rev-parse", "--verify", "--quiet",
                            "%s:%s" % (frozen_row["head"], path))
        have = out.strip() if ok and out.strip() else NO_SKILL
        if have != frozen_row[key]:
            reasons.append("freeze: %s blob cell %s but %s at the frozen head "
                           "is %s" % (path, short(frozen_row[key]), path, short(have)))


def _check_ancestry(srepo, lane, frozen_row, reasons):
    if not srepo.is_dir():
        return
    branch = "refs/heads/%s" % frozen_row["branch"]
    ok, out, _ = git_ok(srepo, "rev-parse", "--verify", "--quiet", branch)
    if not ok or not out.strip():
        reasons.append("frozen branch %s is absent in %s" % (branch, srepo))
        return
    ok, _, err = git_ok(srepo, "merge-base", "--is-ancestor",
                        frozen_row["head"], branch)
    if not ok:
        proc = _run(["git", "-C", str(srepo), "merge-base", "--is-ancestor",
                     frozen_row["head"], branch])
        if proc.returncode == 1:
            reasons.append("frozen head %s is not an ancestor of %s"
                           % (short(frozen_row["head"]), branch))
        else:
            reasons.append("git merge-base --is-ancestor %s %s failed (%s)"
                           % (short(frozen_row["head"]), branch, err))


def _recompute_delta(srepo, lane, pin_row, head, pins):
    if not pin_row:
        return None, ("no round-49 pin for %s in %s at %s"
                      % (lane, PROVINCE_PATH, short(pins.base_rev)))
    pin = pin_row[0]["commit"].strip()
    if not HEX40.match(pin):
        return None, ("the round-49 pin for %s in %s at %s is %r, not a commit"
                      % (lane, PROVINCE_PATH, short(pins.base_rev), pin))
    if not srepo.is_dir():
        return None, None
    ok, out, err = git_ok(srepo, "diff", "--shortstat", pin, head,
                          "--", SKILL_PATH, PROVINCE_PATH)
    if not ok:
        return None, ("git diff --shortstat %s %s failed in %s (%s)"
                      % (short(pin), short(head), srepo, err))
    try:
        return render_delta(out), None
    except UsageError as exc:
        return None, str(exc)


def _check_province_row(lane, row, province_at_rev_rows, province_at_rev, reasons):
    if province_at_rev is None:
        reasons.append("%s absent at the measured revision" % PROVINCE_PATH)
        return
    if province_at_rev_rows is None:
        reasons.append("%s holds no `## Adjacent` lane table at the measured "
                       "revision" % PROVINCE_PATH)
        return
    rows = province_at_rev_rows.get(lane) or []
    if not rows:
        reasons.append("%s § Adjacent has no row for %s at the measured "
                       "revision" % (PROVINCE_PATH, lane))
        return
    if len(rows) > 1:
        reasons.append("%s § Adjacent has %d rows for %s; exactly one is "
                       "required" % (PROVINCE_PATH, len(rows), lane))
        return
    entry_commit = row.cells[2].strip().lower()
    entry_class = row.cells[4].strip().lower()
    if rows[0]["commit"].lower() != entry_commit:
        reasons.append("%s § Adjacent commit %s does not match the entry's %s"
                       % (PROVINCE_PATH, short(rows[0]["commit"]),
                          short(entry_commit) if entry_commit else "<empty>"))
    if rows[0]["classification"] != entry_class:
        reasons.append("%s § Adjacent classification %r does not match the "
                       "entry's %r" % (PROVINCE_PATH, rows[0]["classification"],
                                       entry_class))


def _note_none_body_mention(base, srepo, lane, row, head, report):
    if row.cells[4].strip().lower() != "none" or not srepo.is_dir():
        return
    hits = []
    for path in (SKILL_PATH, PROVINCE_PATH):
        text, _ = git_show_text(srepo, head, path)
        if text is not None and base.token_in(SELF_LANE, text):
            hits.append(path)
    if hits:
        report.setdefault("none_body_mentions", []).append(
            "%s (%s at %s)" % (lane, ", ".join(hits), short(head)))


EVIDENCE_RE = re.compile(
    r'\A(?P<where>[^\s:"\u201c]+):(?P<line>[0-9]+)\s+'
    r'(?P<flag>changed|unchanged)\s+["\u201c](?P<quote>[^"\u201d]+)["\u201d]\s*\Z')


def _ws(text):
    return re.sub(r"\s+", " ", text).strip()


def _check_evidence(base, repo, commit, srepo, lane, row, head, pin_row, pins,
                    reasons):
    """(f): the evidence cell is re-located and its flag recomputed."""
    cell = row.evidence
    m = EVIDENCE_RE.match(cell)
    if not m:
        reasons.append("evidence cell %r is not `<path>:<line> <changed|"
                       "unchanged> \"<quote>\"`" % cell[:80])
        return
    where, line_no, flag, quote = (m.group("where"), int(m.group("line")),
                                   m.group("flag"), _ws(m.group("quote")))
    own = where.startswith("kotoba/")
    path = where[len("kotoba/"):] if own else where
    parts = Path(path).parts
    if (not path or path.startswith("/") or ".." in parts or "\\" in path
            or len(path) > 200):
        reasons.append("evidence path %r is not a relative path inside the "
                       "repository" % where)
        return
    words = len(quote.split())
    if not 6 <= words <= 25:
        reasons.append("evidence quote is %d words (want 6-25)" % words)
    if own:
        text, _ = git_show_text(repo, commit, path)
        old, _ = git_show_text(repo, pins.base_rev, path)
        place = "lane file %s at %s" % (path, short(commit))
    else:
        if not srepo.is_dir():
            return
        text, _ = git_show_text(srepo, head, path)
        pin = (pin_row[0]["commit"].strip() if pin_row else "")
        old, _ = git_show_text(srepo, pin, path) if pin else (None, None)
        place = "%s at the frozen head %s" % (path, short(head))
    if text is None:
        reasons.append("evidence file is absent: %s" % place)
        return
    lines = text.splitlines()
    if not 1 <= line_no <= len(lines):
        reasons.append("evidence line %d is outside %s (%d lines)"
                       % (line_no, place, len(lines)))
        return
    window = _ws(" ".join(lines[i] for i in range(max(0, line_no - 3),
                                                  min(len(lines), line_no + 2))))
    if quote not in window:
        reasons.append("evidence quote not found within 2 lines of %s:%d (%s)"
                       % (path, line_no, place))
    elif lines[line_no - 1].lstrip().startswith("#"):
        reasons.append("evidence line %s:%d is a heading, not a sentence"
                       % (path, line_no))
    recomputed = "unchanged" if (old is not None and old == text) else "changed"
    if flag != recomputed:
        reasons.append("evidence flag %r but the recomputation gives %r (%s "
                       "against %s)" % (flag, recomputed, place,
                                        "the base revision" if own
                                        else "the round-49 pin"))


# --------------------------------------------------------------------------
# stdout
# --------------------------------------------------------------------------

def render(report):
    print("repo %s rev %s base %s" % (report["repo"], short(report["rev"]),
                                      short(report["base"])))
    print("freeze %s" % report["freeze"])
    print("fleet %s" % report["fleet"])
    print("base census: rows %d verified %d (delta cell stripped, base-row checks)"
          % (report["census_rows"], report["census_verified"]))
    for note in report["notes"]:
        print("note %s" % note)
    for failure in report["census_failures"]:
        print("FAIL census-wide %s" % failure)
    for item in report.get("none_body_mentions", []):
        print("info none-row SKILL.md/PROVINCE.md body names kotoba (reported, "
              "not counted): %s" % item)
    for lane, reasons in report["lanes"]:
        if reasons:
            print("lane %s: FAIL %s" % (lane, "; ".join(reasons)))
        else:
            print("lane %s: ok" % lane)
    print("sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads %d of %d"
          % (report["n"], report["lanes_total"]))


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def resolve_repo(argument):
    """The lane repository root.  No argument: the git toplevel of this file's
    directory (it lands at `verifiers/`, so that is the lane root; run from the
    draft path under `.ufo/` it still resolves to the lane)."""
    if argument:
        start = Path(argument).expanduser()
        if not start.is_dir():
            raise UsageError("--repo %s is not a directory" % start)
        start = start.resolve()
    else:
        start = Path(__file__).resolve().parent
    ok, out, err = git_ok(start, "rev-parse", "--show-toplevel")
    if not ok or not out.strip():
        raise UsageError("%s is not inside a git work tree (%s)" % (start, err))
    root = Path(out.strip())
    if not (root / PROVINCE_PATH).is_file():
        raise UsageError("%s holds no %s: not the lane repository"
                         % (root, PROVINCE_PATH))
    return root


def build_parser():
    parser = argparse.ArgumentParser(
        description="Re-pin and re-read the round-74 sibling census at the "
                    "frozen fleet heads.")
    parser.add_argument("--rev", help="the revision to measure")
    parser.add_argument("--repo", metavar="DIR",
                        help="the lane repository (default: the git toplevel "
                             "of this file's directory)")
    parser.add_argument("--fleet", default=DEFAULT_FLEET, metavar="DIR",
                        help="fleet root holding the `*-shokunin` sibling repos "
                             "(default: %s)" % DEFAULT_FLEET)
    parser.add_argument("--freeze", metavar="PATH",
                        help="freeze file override (default: the pinned "
                             "receipt %s)" % FREEZE_PATH)
    parser.add_argument("--emit-cells", action="store_true",
                        help="print the mechanical cells an entry author must "
                             "copy, recomputed from the frozen heads")
    parser.add_argument("--self-test", action="store_true",
                        help="assert the arms of the counter on a throwaway "
                             "fixture fleet and exit")
    return parser


def emit_cells(repo, fleet, pins):
    fleet = Path(fleet).expanduser().resolve()
    with tempfile.TemporaryDirectory(prefix="sibling-cells-") as workdir:
        base = load_base_checker(repo, pins, workdir)
        frozen, note = read_freeze(repo, None, pins)
        base_province, _ = git_show_text(repo, pins.base_rev, PROVINCE_PATH)
        if base_province is None:
            raise UsageError("%s is absent at %s" % (PROVINCE_PATH,
                                                     short(pins.base_rev)))
        base_pins = province_rows(base, base_province) or {}
        all_lanes = base.fleet_lanes(fleet) | {SELF_LANE}
        print("# %s" % note)
        print("lane\tcommit\tskill file\tnames kotoba\tarbitration\tdelta")
        for lane in sorted(frozen):
            head = frozen[lane]["head"]
            srepo = lane_repo(fleet, lane)
            skill_text, _ = git_show_text(srepo, head, SKILL_PATH)
            if skill_text is None:
                skill_cell, names_cell, arb_cell = "NONE", "no SKILL.md", "no SKILL.md"
            else:
                description = base.description_of(skill_text)
                skill_cell = SKILL_PATH
                names_cell = "yes" if base.token_in(SELF_LANE, description) else "no"
                named = sorted(n for n in all_lanes
                               if n != lane and base.token_in(n, description))
                arb_cell = ("yes: " + ", ".join(named)) if named else "no"
            want, why = _recompute_delta(srepo, lane, base_pins.get(lane), head, pins)
            print("%s\t%s\t%s\t%s\t%s\t%s"
                  % (lane, head, skill_cell, names_cell, arb_cell,
                     want if why is None else "could-not-evaluate: %s" % why))
    return 0


def main(argv=None, pins=PINS):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.self_test:
        if args.rev or args.emit_cells or args.freeze or args.repo:
            parser.error("--self-test cannot be combined with the other options")
        return self_test()

    try:
        repo = resolve_repo(args.repo)
        if args.emit_cells:
            if args.rev:
                parser.error("--emit-cells cannot be combined with --rev")
            return emit_cells(repo, args.fleet, pins)
        if not args.rev:
            parser.error("--rev is required")
        report = measure(repo, args.rev, args.fleet, args.freeze, pins)
    except UsageError as exc:
        print("could-not-evaluate: %s" % exc, file=sys.stderr)
        return 2

    report["repo"] = str(repo)
    report["lanes_total"] = pins.lanes
    render(report)
    ok = (report["n"] == pins.lanes and not report["census_failures"])
    return 0 if ok else 1


# --------------------------------------------------------------------------
# self-test
# --------------------------------------------------------------------------
#
# The fixture is a throwaway fleet: 20 tiny sibling repositories plus a lane
# repository (`kotoba-shokunin`) whose base commit carries the census checker
# this counter loads.  The self-test's stand-in checker (STUB_CHECKER below)
# mirrors the base's row-check contract so the strip-and-delegate path is
# exercised end to end; at measurement the real base bytes are sha256-pinned
# and loaded from the measured repository, and the seat report measures the
# same fixture against those real bytes via `Pins(base_rev=...)`.

STUB_CHECKER = r'''#!/usr/bin/env python3
# Stand-in for verifiers/check_sibling_census.py, used ONLY by the self-test of
# check_sibling_reread.py: it mirrors the base's nine-cell row-check contract so
# the strip-and-delegate path can be exercised without shipping the base bytes.
import re
import subprocess
from pathlib import Path

CENSUS_COLUMNS = 9
CLASSIFICATIONS = ("contested", "adjacent", "none")
LANE_SUFFIX = "-shokunin"
SELF_LANE = "kotoba"
LINE_TOLERANCE = 2
HEX40 = re.compile(r"\A[0-9a-fA-F]{40}\Z")
SEP = re.compile(r"\A:?-{2,}:?\Z")
WS = re.compile(r"\s+")
CELL = re.compile(r"(?<!\\)\|")
MIN_QUOTE_WORDS = 6


class UsageError(Exception):
    pass


def collapse(text):
    return WS.sub(" ", text).strip()


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [p.replace("\\|", "|").strip() for p in CELL.split(s)]


def is_separator(cells):
    return bool(cells) and all(SEP.match(c) for c in cells)


def parse_blocks(lines):
    blocks, current = [], []
    for number, line in enumerate(lines, 1):
        if line.strip().startswith("|"):
            current.append((number, line))
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    out = []
    for raw in blocks:
        sep, body = None, raw
        if len(raw) >= 2 and is_separator(split_row(raw[1][1])):
            sep = raw[1][0]
            body = raw[2:]
        out.append({"header": split_row(raw[0][1]), "sep_line": sep,
                    "rows": [(n, split_row(t)) for n, t in body]})
    return out


def strip_wrapping(cell):
    s = cell.strip()
    while len(s) >= 2 and ((s[0] == '"' and s[-1] == '"')
                           or (s[0] == "`" and s[-1] == "`")):
        s = s[1:-1].strip()
    return s


def normalize_lane(cell):
    s = strip_wrapping(cell)
    if s.lower().endswith(LANE_SUFFIX):
        s = s[: -len(LANE_SUFFIX)]
    return s.strip().lower()


def token_in(name, text):
    return re.search(r"(?<![a-z0-9-])" + re.escape(name) + r"(?![a-z0-9])",
                     text, re.I) is not None


def description_of(skill_text):
    if skill_text is None or not skill_text.startswith("---"):
        return ""
    front = skill_text.split("\n---", 1)[0]
    m = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
    if not m:
        return ""
    return re.sub(r"\A[>|][+-]?\s*", "", collapse(m.group(1))).strip()


def fleet_lanes(root):
    lanes = set()
    for entry in Path(root).iterdir():
        if entry.is_dir() and entry.name.lower().endswith(LANE_SUFFIX):
            lane = entry.name[: -len(LANE_SUFFIX)].lower()
            if lane != SELF_LANE:
                lanes.add(lane)
    return lanes


def git_show(repo, commit, path):
    p = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (commit, path)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", "replace")


def locate(lines, line_no, quote):
    exact = line_no - 1
    for offset in (0, 1, -1, 2, -2):
        index = exact + offset
        if 0 <= index < len(lines) and quote in collapse(lines[index]):
            return index, lines[index].strip().startswith("#")
    low = max(0, exact - LINE_TOLERANCE)
    high = min(len(lines), exact + LINE_TOLERANCE + 1)
    window = list(range(low, high))
    if quote in collapse(" ".join(lines[i] for i in window)):
        return window[0], lines[window[0]].strip().startswith("#")
    return None, False


def extract_adjacent_section(text):
    lines = text.splitlines()
    start = None
    for number, line in enumerate(lines, 1):
        if re.match(r"\A##\s+Adjacent\s*\Z", line):
            start = number
            break
    if start is None:
        return None
    body = []
    for line in lines[start:]:
        if re.match(r"\A##\s+\S", line):
            break
        body.append(line)
    return body


def check_census(census_path, fleet_root, province_path=None):
    result = {"failures": [], "rows": 0, "verified": 0}
    failures = result["failures"]
    text = Path(census_path).read_text(encoding="utf-8")
    blocks = [b for b in parse_blocks(text.splitlines())
              if b["sep_line"] is not None and len(b["header"]) == CENSUS_COLUMNS]
    if not blocks:
        failures.append("census table not found")
        return result
    rows = blocks[0]["rows"]
    result["rows"] = len(rows)
    expected = fleet_lanes(fleet_root)
    seen = set()
    counts = {}
    for _n, cells in rows:
        if len(cells) == CENSUS_COLUMNS and cells[0].strip():
            lane = normalize_lane(cells[0])
            counts[lane] = counts.get(lane, 0) + 1
    for lane in sorted(counts):
        if counts[lane] > 1:
            failures.append("census table: lane %s appears in more than one row"
                            % lane)
    for index, (line_no, cells) in enumerate(rows, 1):
        label = "row %d (census line %d)" % (index, line_no)
        if len(cells) != CENSUS_COLUMNS:
            failures.append(label + ": expected %d cells, found %d"
                            % (CENSUS_COLUMNS, len(cells)))
            continue
        lane = normalize_lane(cells[0])
        if not lane:
            failures.append(label + ": empty lane cell")
            continue
        label = "%s (lane %s)" % (label, lane)
        seen.add(lane)
        names = ("lane", "branch", "commit", "path", "classification",
                 "names kotoba", "arbitration", "path:line", "quote")
        values = dict(zip(names, cells))
        empty = [k for k in names if not values[k].strip()]
        if empty:
            failures.append(label + ": empty cell(s): " + ", ".join(empty))
            continue
        commit = values["commit"].strip()
        if not HEX40.match(commit):
            failures.append(label + ": commit %r is not a 40-hex object id" % commit)
            continue
        classification = values["classification"].strip().lower()
        if classification not in CLASSIFICATIONS:
            failures.append(label + ": classification %r is not one of %s"
                            % (values["classification"], "/".join(CLASSIFICATIONS)))
            continue
        cell = strip_wrapping(values["path:line"])
        if ":" not in cell:
            failures.append(label + ": malformed path:line %r" % values["path:line"])
            continue
        path, _, number = cell.rpartition(":")
        if not path.strip() or not number.strip().isdigit():
            failures.append(label + ": malformed path:line %r" % values["path:line"])
            continue
        quote = collapse(strip_wrapping(values["quote"]))
        if not quote:
            failures.append(label + ": empty quote cell")
            continue
        repo = Path(fleet_root) / (lane + LANE_SUFFIX)
        content = git_show(repo, commit, path.strip())
        if content is None:
            failures.append(label + ": git show %s:%s failed"
                            % (commit[:12], path.strip()))
            continue
        lines = content.splitlines()
        found, heading = locate(lines, int(number), quote)
        if found is None:
            failures.append(label + ": quote not found at %s:%s (+/-%d lines)"
                            % (path.strip(), number, LINE_TOLERANCE))
            continue
        if heading:
            failures.append(label + ": quote sits on a markdown heading")
            continue
        if len(quote.split()) < MIN_QUOTE_WORDS:
            failures.append(label + ": quote has fewer than %d words"
                            % MIN_QUOTE_WORDS)
            continue
        skill_text = git_show(repo, commit, "SKILL.md")
        if skill_text is None:
            if (values["path"].strip().lower() != "none"
                    or values["names kotoba"].strip().lower() != "no skill.md"
                    or values["arbitration"].strip().lower() != "no skill.md"):
                failures.append(label + ": no SKILL.md at the pin, but the "
                                "skill/names/arbitration cells do not say so")
                continue
            description = ""
        else:
            if values["path"].strip().lower() == "none":
                failures.append(label + ": SKILL.md exists but the skill cell "
                                "says NONE")
                continue
            description = description_of(skill_text)
            want_names = "yes" if token_in(SELF_LANE, description) else "no"
            if values["names kotoba"].strip().lower() != want_names:
                failures.append(label + ": names-kotoba cell %r but the pinned "
                                "description gives %r"
                                % (values["names kotoba"], want_names))
                continue
            named = sorted(n for n in (expected | {SELF_LANE})
                           if n != lane and token_in(n, description))
            want_arb = ("yes: " + ", ".join(named)) if named else "no"
            if values["arbitration"].strip().lower() != want_arb:
                failures.append(label + ": arbitration cell %r but the pinned "
                                "description gives %r"
                                % (values["arbitration"], want_arb))
                continue
        if classification == "none":
            province = git_show(repo, commit, "PROVINCE.md")
            if token_in(SELF_LANE, description) or (
                    province is not None and token_in(SELF_LANE, province)):
                failures.append(label + ": classified none, but the sibling's "
                                "description or PROVINCE.md at the pin names kotoba")
                continue
        result["verified"] += 1
    missing = sorted(expected - seen)
    extra = sorted(seen - expected)
    if missing:
        failures.append("lane set: %d sibling lane(s) never surveyed: %s"
                        % (len(missing), ", ".join(missing)))
    if extra:
        failures.append("lane set: %d lane(s) not in the fleet: %s"
                        % (len(extra), ", ".join(extra)))
    return result
'''

FIXTURE_LANES = ["lane%02d" % i for i in range(1, FREEZE_LANES + 1)]


def _git(repo, *args):
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "kotoba self-test",
                "GIT_AUTHOR_EMAIL": "self-test@example.invalid",
                "GIT_COMMITTER_NAME": "kotoba self-test",
                "GIT_COMMITTER_EMAIL": "self-test@example.invalid"})
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    if proc.returncode != 0:
        raise RuntimeError("git %s failed in %s: %s"
                           % (" ".join(args), repo,
                              proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode("utf-8", "replace")


def _init(repo, branch):
    repo.mkdir(parents=True)
    _git(repo, "init", "-q", "-b", branch)
    top = _git(repo, "rev-parse", "--show-toplevel").strip()
    if Path(top).resolve() != repo.resolve():
        raise RuntimeError("fixture repo %s is not its own toplevel (%s)"
                           % (repo, top))
    _git(repo, "config", "user.name", "kotoba self-test")
    _git(repo, "config", "user.email", "self-test@example.invalid")
    _git(repo, "config", "commit.gpgsign", "false")


def _commit(repo, message):
    _git(repo, "add", "-A")
    proc = subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", message],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        # A world that changes nothing is a valid world: report the same revision.
        if b"nothing to commit" in proc.stderr or b"no changes added" in proc.stderr:
            return _git(repo, "rev-parse", "HEAD").strip()
        raise RuntimeError("git commit failed in %s: %s"
                           % (repo, proc.stderr.decode("utf-8", "replace").strip()))
    return _git(repo, "rev-parse", "HEAD").strip()


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sibling_skill(lane, body_note=""):
    body = ("---\n"
            "name: %s-shokunin\n"
            "description: >\n"
            "  %s scope: fixture checks and nothing else.\n"
            "---\n"
            "\n"
            "# %s\n"
            "\n"
            "Fixture body line for %s.\n" % (lane, lane.replace("lane", "Lane "),
                                             lane, lane))
    if body_note:
        body += body_note + "\n"
    return body


def sibling_province(lane, pin):
    return ("# PROVINCE (%s)\n"
            "\n"
            "## Domain\n"
            "\n"
            "%s owns the %s surface only.\n"
            "\n"
            "| lane | classification | commit | boundary |\n"
            "|---|---|---|---|\n"
            "| %s | none | %s | fixture boundary |\n"
            % (lane, lane, lane, lane, pin))


def entry_text(frozen, classes, deltas):
    header = ("| lane | branch | commit | skill file | classification | "
              "names kotoba | arbitration | scope quote at | scope quote | "
              "delta | evidence |")
    out = ["# sibling-overlap census (round 74, fixture)", "",
           "source: S999 (fixture); sibling bytes: the 20 sibling lanes at "
           "their frozen heads", "verified-at: 2026-10-25", "",
           header, "|" + "|".join("---" for _ in range(CENSUS_COLUMNS)) + "|"]
    for lane in sorted(frozen):
        flag = "changed" if lane == "lane01" else "unchanged"
        out.append("| %s | %s | %s | SKILL.md | %s | no | no | PROVINCE.md:5 | "
                   "\"%s owns the %s surface only.\" | %s | PROVINCE.md:5 %s "
                   "\"%s owns the %s surface only.\" |"
                   % (lane, frozen[lane]["branch"], frozen[lane]["head"],
                      classes[lane], lane, lane, deltas[lane], flag, lane, lane))
    return "\n".join(out) + "\n"


def lane_province(frozen, classes):
    out = ["# PROVINCE (fixture lane)", "", "## Core", "", "fixture.", "",
           "## Adjacent", "",
           "| lane | classification | commit | boundary |",
           "|---|---|---|---|"]
    for lane in sorted(frozen):
        out.append("| %s | %s | %s | fixture boundary |"
                   % (lane, classes[lane], frozen[lane]["head"]))
    out += ["", "## After", "", "text.", ""]
    return "\n".join(out)


class Fixture:
    """A throwaway fleet: 20 sibling repos and a lane repo.

    `checker_bytes` are the census-checker bytes the lane repo's base commit
    carries; the self-test passes a stand-in, the seat report passes the real
    base bytes fetched with `git show BASE_REV:verifiers/check_sibling_census.py`.
    """

    def __init__(self, root, checker_bytes):
        self.root = Path(root)
        self.fleet = self.root / "fleet"
        self.fleet.mkdir(parents=True)
        self.lane = self.fleet / (SELF_LANE + LANE_SUFFIX)
        self.frozen = {}
        self.pins = {}
        self.branch = {}
        self._make_siblings()
        self._make_lane(checker_bytes)

    def _make_siblings(self):
        for index, lane in enumerate(FIXTURE_LANES, 1):
            branch = "main" if lane == "lane20" else "master"
            repo = self.fleet / (lane + LANE_SUFFIX)
            _init(repo, branch)
            # lane19 carries `kotoba` in its SKILL.md BODY only (outside the
            # frontmatter description): the base checker's none rule reads the
            # description and PROVINCE.md, so only conjunct (e) can catch a
            # `none` classification over these bytes.
            note = "Hand-offs route to kotoba." if lane == "lane19" else ""
            _write(repo / SKILL_PATH, sibling_skill(lane, note))
            _write(repo / PROVINCE_PATH, sibling_province(lane, "0" * 40))
            pin = _commit(repo, "pin")
            _write(repo / PROVINCE_PATH, sibling_province(lane, pin))
            pin = _commit(repo, "pin with its own id")
            if lane == "lane01":
                # a head that moved: one appended line, so the delta is +1/-0
                with (repo / PROVINCE_PATH).open("a", encoding="utf-8") as handle:
                    handle.write("\nAppended after the pin.\n")
                head = _commit(repo, "head")
            else:
                head = pin
            self.pins[lane] = pin
            self.frozen[lane] = {"branch": branch, "head": head,
                                 "skill_blob": _git(repo, "rev-parse",
                                                    "%s:SKILL.md" % head).strip(),
                                 "province_blob": _git(repo, "rev-parse",
                                                       "%s:PROVINCE.md" % head).strip()}
            self.branch[lane] = branch

    def _make_lane(self, checker_bytes):
        _init(self.lane, "master")
        _write(self.lane / "verifiers" / "check_sibling_census.py",
               checker_bytes.decode("utf-8") if isinstance(checker_bytes, bytes)
               else checker_bytes)
        _write(self.lane / PROVINCE_PATH, self._base_province())
        self.base = _commit(self.lane, "base: pins, base checker")
        self.classes = {lane: ("adjacent" if lane in ("lane19", "lane20") else "none")
                        for lane in FIXTURE_LANES}
        self.deltas = {lane: self._delta(lane) for lane in FIXTURE_LANES}
        self.entry = entry_text(self.frozen, self.classes, self.deltas)
        self.province = lane_province(self.frozen, self.classes)
        _write(self.lane / ENTRY_PATH, self.entry)
        _write(self.lane / PROVINCE_PATH, self.province)
        self.rev = _commit(self.lane, "rev: entry, re-pinned adjacent table")
        self.freeze_text = self._freeze_text()
        _write(self.lane / FREEZE_PATH, self.freeze_text)
        self.pins_obj = Pins(base_rev=self.base,
                             checker_sha256=hashlib.sha256(
                                 checker_bytes if isinstance(checker_bytes, bytes)
                                 else checker_bytes.encode("utf-8")).hexdigest(),
                             freeze_sha256=hashlib.sha256(
                                 self.freeze_text.encode("utf-8")).hexdigest(),
                             lanes=FREEZE_LANES)

    def _base_province(self):
        out = ["# PROVINCE (fixture lane, round-49 pins)", "", "## Adjacent", "",
               "| lane | classification | commit | boundary |",
               "|---|---|---|---|"]
        for lane in FIXTURE_LANES:
            out.append("| %s | none | %s | fixture boundary |"
                       % (lane, self.pins[lane]))
        return "\n".join(out) + "\n"

    def _delta(self, lane):
        repo = self.fleet / (lane + LANE_SUFFIX)
        out = _git(repo, "diff", "--shortstat", self.pins[lane],
                   self.frozen[lane]["head"], "--", SKILL_PATH, PROVINCE_PATH)
        return render_delta(out)

    def _freeze_text(self):
        lines = ["# sibling heads frozen for the self-test fixture",
                 "# lane\tbranch\thead40\tskill_md_blob\tprovince_md_blob"]
        for lane in sorted(self.frozen):
            row = self.frozen[lane]
            lines.append("%s\t%s\t%s\t%s\t%s"
                         % (lane, row["branch"], row["head"],
                            row["skill_blob"], row["province_blob"]))
        return "\n".join(lines) + "\n"

    def state(self, entry=None, province=None):
        """Commit a world: rewrite the entry and/or PROVINCE.md and commit.

        The new commit becomes the measured revision, so the next `run()` reads
        the world that was just committed.
        """
        _write(self.lane / ENTRY_PATH, self.entry if entry is None else entry)
        _write(self.lane / PROVINCE_PATH,
               self.province if province is None else province)
        self.rev = _commit(self.lane, "world")
        return self.rev

    def run(self, rev=None, argv_extra=(), pins=None):
        """Call main() with captured stdout.  Returns (exit, stdout)."""
        argv = ["--rev", rev or self.rev, "--repo", str(self.lane),
                "--fleet", str(self.fleet)] + list(argv_extra)
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(io.StringIO()):
            code = main(argv, pins=pins or self.pins_obj)
        return code, buffer.getvalue()


def self_test():
    total = 0
    failures = []

    def rec(what, ok, got=None):
        nonlocal total
        total += 1
        if not ok:
            failures.append("%s: got %r" % (what, got))

    with tempfile.TemporaryDirectory(prefix="reread-selftest-") as tmp:
        fixture = Fixture(Path(tmp), STUB_CHECKER.encode("utf-8"))
        pins = fixture.pins_obj
        green_line = "sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads %d of %d" % (FREEZE_LANES,
                                                                     FREEZE_LANES)

        code, out = fixture.run()
        rec("green world exit 0", code == 0, (code, out[-400:]))
        rec("green world exact line", out.strip().splitlines()[-1:] == [green_line],
            out.strip().splitlines()[-1:])
        rec("green world names all 20 lanes ok",
            out.count(": ok") == FREEZE_LANES, out.count(": ok"))

        # Q66: the relative `--repo .` arm, run from the lane directory
        here = Path.cwd()
        try:
            os.chdir(fixture.lane)
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(io.StringIO()):
                code = main(["--rev", fixture.rev, "--repo", ".", "--fleet",
                             str(fixture.fleet)], pins=pins)
            rec("relative --repo . exit 0", code == 0, code)
            rec("relative --repo . exact line",
                buffer.getvalue().strip().splitlines()[-1:] == [green_line],
                buffer.getvalue().strip().splitlines()[-1:])
        finally:
            os.chdir(here)

        broken = "sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads %d of %d" % (FREEZE_LANES - 1,
                                                                  FREEZE_LANES)

        # (a) the quote is not at the pinned commit: base row check refuses it
        entry = fixture.entry.replace(
            '"lane04 owns the lane04 surface only."',
            '"this sentence is nowhere in the pinned file at all"')
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("(a) quote absent: exit 1", code == 1, code)
        rec("(a) quote absent: 19 of 20", out.strip().splitlines()[-1:] == [broken],
            out.strip().splitlines()[-1:])

        # (b) the commit cell is the r49 pin, not the frozen head
        entry = fixture.entry.replace(
            "| lane01 | master | %s |" % fixture.frozen["lane01"]["head"],
            "| lane01 | master | %s |" % fixture.pins["lane01"])
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("(b) pin as commit: exit 1", code == 1, code)
        rec("(b) pin as commit: 19 of 20", out.strip().splitlines()[-1:] == [broken],
            out.strip().splitlines()[-1:])
        rec("(b) pin as commit: named reason",
            "is not the frozen head" in out, out[-400:])

        # (b), Q32: a 12-hex prefix of the frozen head is not the frozen head
        entry = fixture.entry.replace(
            fixture.frozen["lane01"]["head"],
            fixture.frozen["lane01"]["head"][:12])
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("(b) commit prefix: exit 1", code == 1, code)
        rec("(b) commit prefix: 19 of 20",
            out.strip().splitlines()[-1:] == [broken], out.strip().splitlines()[-1:])

        # (c) the delta cell disagrees with the recomputation
        entry = fixture.entry.replace("| %s |" % fixture.deltas["lane01"],
                                      "| +9/-9 |", 1)
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("(c) wrong delta: exit 1", code == 1, code)
        rec("(c) wrong delta: 19 of 20", out.strip().splitlines()[-1:] == [broken],
            out.strip().splitlines()[-1:])
        rec("(c) wrong delta: named reason", "recomputation gives" in out, out[-400:])

        # (d) PROVINCE.md § Adjacent still carries the r49 pin for one lane
        province = fixture.province.replace(
            "| lane01 | none | %s |" % fixture.frozen["lane01"]["head"],
            "| lane01 | none | %s |" % fixture.pins["lane01"])
        fixture.state(province=province)
        code, out = fixture.run()
        rec("(d) province commit stale: exit 1", code == 1, code)
        rec("(d) province commit stale: 19 of 20",
            out.strip().splitlines()[-1:] == [broken], out.strip().splitlines()[-1:])
        rec("(d) province commit stale: named reason",
            "does not match the entry" in out, out[-400:])

        # (e) a `none` row over bytes whose SKILL.md body names kotoba
        entry = fixture.entry.replace("| lane19 | master | %s | SKILL.md | adjacent |"
                                      % fixture.frozen["lane19"]["head"],
                                      "| lane19 | master | %s | SKILL.md | none |"
                                      % fixture.frozen["lane19"]["head"])
        province = fixture.province.replace(
            "| lane19 | adjacent | %s |" % fixture.frozen["lane19"]["head"],
            "| lane19 | none | %s |" % fixture.frozen["lane19"]["head"])
        fixture.state(entry=entry, province=province)
        code, out = fixture.run()
        rec("(e withdrawn) none over a SKILL.md body mention: exit 0", code == 0,
            (code, out[-300:]))
        rec("(e withdrawn) none over a body mention: counted 20 of 20",
            out.strip().splitlines()[-1:] == [green_line],
            out.strip().splitlines()[-1:])
        rec("(e withdrawn) body mention is printed, not counted",
            "info none-row SKILL.md/PROVINCE.md body names kotoba" in out
            and "lane19" in out, out[-500:])

        # (f) evidence arms
        base_entry = fixture.entry
        cell = ('PROVINCE.md:5 unchanged "lane04 owns the lane04 surface only."')
        for label, repl in (
                ("quote absent near the line",
                 'PROVINCE.md:5 unchanged "this sentence is nowhere near that line"'),
                ("flag says changed over an unchanged file",
                 'PROVINCE.md:5 changed "lane04 owns the lane04 surface only."'),
                ("heading line is not a sentence",
                 'PROVINCE.md:3 unchanged "Domain lane04 owns the lane04 surface only"'),
                ("path escapes the repository",
                 '../lane05-shokunin/PROVINCE.md:5 unchanged "lane04 owns the '
                 'lane04 surface only."'),
                ("line outside the file",
                 'PROVINCE.md:999 unchanged "lane04 owns the lane04 surface only."'),
                ("malformed cell", "pointer")):
            fixture.state(entry=base_entry.replace(cell, repl, 1))
            code, out = fixture.run()
            rec("(f) %s: exit 1" % label, code == 1, (code, out[-300:]))
            rec("(f) %s: 19 of 20" % label,
                out.strip().splitlines()[-1:] == [broken],
                out.strip().splitlines()[-1:])
        fixture.state(entry=base_entry.replace(
            "| PROVINCE.md:5 unchanged \"lane04", "| unchanged \"lane04", 1))
        code, out = fixture.run()
        rec("(f) evidence cell without a pointer: exit 1", code == 1, code)
        fixture.state()

        # extra: a missing row
        lines = fixture.entry.splitlines(True)
        entry = "".join(line for line in lines
                        if not line.startswith("| lane20 |"))
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("missing row: exit 1", code == 1, code)
        rec("missing row: 19 of 20", out.strip().splitlines()[-1:] == [broken],
            out.strip().splitlines()[-1:])
        rec("missing row: census-wide lane set failure",
            "FAIL census-wide lane set" in out, out[-400:])

        # extra: a duplicated row
        entry = fixture.entry
        dup = [line for line in entry.splitlines(True) if line.startswith("| lane03 |")]
        entry = entry.replace(dup[0], dup[0] + dup[0], 1)
        fixture.state(entry=entry)
        code, out = fixture.run()
        rec("duplicated row: exit 1", code == 1, code)
        rec("duplicated row: 19 of 20", out.strip().splitlines()[-1:] == [broken],
            out.strip().splitlines()[-1:])
        rec("duplicated row: names the lane",
            "has 2 rows for lane03" in out, out[-500:])

        # guards: freeze sha, freeze lane count, base checker sha, CLI forms
        fixture.state()
        (fixture.lane / FREEZE_PATH).write_text(
            fixture.freeze_text.replace("lane01\t", "lane01X\t"), encoding="utf-8")
        code, out = fixture.run()
        rec("freeze sha mismatch: exit 2", code == 2, code)

        short_freeze = fixture.lane / "short-freeze.tsv"
        short_freeze.write_text("\n".join(fixture.freeze_text.splitlines()[:20]) + "\n",
                                encoding="utf-8")
        code, out = fixture.run(argv_extra=("--freeze", str(short_freeze)))
        rec("freeze lane count: exit 2", code == 2, code)

        _write(fixture.lane / FREEZE_PATH, fixture.freeze_text)
        _write(fixture.lane / "verifiers" / "check_sibling_census.py",
               STUB_CHECKER + "\n# tampered base copy\n")
        bad_base = _commit(fixture.lane, "a revision whose checker is not the base")
        code, out = fixture.run(pins=pins.__class__(
            base_rev=bad_base, checker_sha256=pins.checker_sha256,
            freeze_sha256=pins.freeze_sha256, lanes=pins.lanes))
        rec("base checker sha mismatch: exit 2", code == 2, code)

        buffer = io.StringIO()
        try:
            with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
                main([], pins=pins)
            rec("no --rev: exit 2", False, "no SystemExit")
        except SystemExit as exc:
            rec("no --rev: exit 2", exc.code == 2, exc.code)

        try:
            with contextlib.redirect_stdout(io.StringIO()), \
                    contextlib.redirect_stderr(io.StringIO()):
                main(["--self-test", "--rev", "x"], pins=pins)
            rec("--self-test with --rev: exit 2", False, "no SystemExit")
        except SystemExit as exc:
            rec("--self-test with --rev: exit 2", exc.code == 2, exc.code)

        # Q33: the pins are not settable from argv
        names = set()
        for action in build_parser()._actions:
            names.update(action.option_strings)
        rec("no CLI flag sets the pins",
            not any("sha" in name or "base" in name or "pin" in name
                    for name in names), sorted(names))

        # a satisfying world after every mutation
        code, out = fixture.run()
        rec("restored world exit 0", code == 0, (code, out[-400:]))

    print("self-test: %d failure(s) over %d assertions" % (len(failures), total))
    for failure in failures:
        print("FAIL %s" % failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
