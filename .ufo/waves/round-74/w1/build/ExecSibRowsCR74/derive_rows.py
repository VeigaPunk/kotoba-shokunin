#!/usr/bin/env python3
"""derive_rows.py -- round-74 C2 mechanical row cells for five sibling lanes.

Seat: ExecSibRowsCR74 (round 74, wave 1).  Lanes: kotodama, kumitate, lore,
mado, mori.

Every classification-bearing cell is produced by the BASE checker's own
functions, imported from a scratch copy of

    git -C <lane> show 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908:verifiers/check_sibling_census.py

(spec 2 (a): the measured revision supplies bytes, not code -- Q33).  This
script re-implements none of them: `description_of`, `token_in`,
`fleet_lanes`, `git_show`, `normalize_lane`, `normalize_lane`, `collapse`,
`parse_blocks`, `select_census_table` and `mechanical_findings` are imported.
The arbitration cell is assembled here from `fleet_lanes` + `token_in` (+ the
checker's own `sorted` join shape) and then CROSS-CHECKED by feeding it back
into `mechanical_findings`, which re-derives the same cells from the pinned
bytes and names a mismatch.  A derived row therefore never rests on this
script's own reading of the description.

Columns (header + one row per lane, tab separated):

    lane  branch  commit40  skill_file  classification  names_kotoba
    arbitration  quote  r49_pin  delta  kotoba_hits_skill_md
    kotoba_hits_province_md  scope_skill_md  scope_province_md
    scope_skill_text  scope_province_text  selfcheck

  * `classification` and `quote` are EMPTY by contract: the scouts own them
    and the merge tool joins those cells (this seat does not classify).
  * `skill_file` / `names_kotoba` / `arbitration` are the census row cells
    (census column order 4, 6, 7).
  * `delta` is `+ins/-del` summed over
    `git diff --shortstat <r49 pin> <freeze head> -- SKILL.md PROVINCE.md`,
    `none` when that diff prints nothing.
  * `kotoba_hits_*` are the whole-word `kotoba` hits at the head
    (`token_in("kotoba", line)`), `path:line` comma-joined, `-` when none.
  * `scope_*` are the candidate scope-statement lines as `path:line` lists:
    every physical line of the frontmatter `description` value (SKILL.md) and
    the column-0 `Domain`/`Owns` lines (PROVINCE.md).  `scope_*_text` carries
    the same lines whitespace-COLLAPSED with ` || ` separators -- a preview
    for choosing, not a quotable form: a scout copies its quote from
    `sed -n '<L>p'` of the pinned bytes (Q: quotes are copied, not shaped).
  * `selfcheck` is `ok` when `mechanical_findings` accepted the assembled
    cells, else the checker's problem strings.

Also re-derives the round-49 cells at the round-49 pins (PROVINCE.md §
Adjacent) and compares them with the landed round-49 census row for the same
lane; mismatches are printed and exit code 1.

Usage:
    python3 derive_rows.py --scratch DIR --out rows.tsv [--lanes a,b,c]
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

LANE = "kotoba-shokunin"
BASE_REV = "1e03d1991bc02281b00a5b7a5e00c9d5d5d72908"
DEFAULT_LANES = ("kotodama", "kumitate", "lore", "mado", "mori")
SHORTSTAT_INS = re.compile(r"(\d+) insertion")
SHORTSTAT_DEL = re.compile(r"(\d+) deletion")

# The first nine columns are exactly the round-49 census cells, in census
# order (CENSUS_CELL_NAMES), so a merge tool can take 1..9 as one census row:
#   lane | branch | commit | path | classification | names kotoba |
#   arbitration | path:line | quote
# `classification`, `path_line` and `quote` are intentionally EMPTY here (the
# scouts own them).  Everything after them is this seat's derivation evidence.
COLUMNS = ("lane", "branch", "commit", "path", "classification",
           "names_kotoba", "arbitration", "path_line", "quote",
           "r49_pin", "delta", "r49_quote_at_head",
           "kotoba_hits_skill_md", "kotoba_hits_province_md",
           "scope_skill_md", "scope_province_md", "scope_skill_text",
           "scope_province_text", "selfcheck")


def load_checker(scratch, lane_repo):
    """Write the BASE revision's checker into scratch and import it."""
    src = subprocess.run(
        ["git", "-C", str(lane_repo), "show", BASE_REV + ":verifiers/check_sibling_census.py"],
        capture_output=True)
    if src.returncode != 0:
        sys.exit("cannot read the base checker: %s"
                 % src.stderr.decode("utf-8", "replace").strip())
    path = Path(scratch) / "base_check_sibling_census.py"
    path.write_bytes(src.stdout)
    spec = importlib.util.spec_from_file_location("base_census", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def git(repo, *args):
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), \
        proc.stderr.decode("utf-8", "replace")


def read_freeze(path):
    rows = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        cells = line.split("\t")
        if len(cells) != 5:
            continue
        rows[cells[0]] = {"branch": cells[1], "head": cells[2],
                          "skill_blob": cells[3], "province_blob": cells[4]}
    return rows


def read_province_pins(province_path, chk):
    """lane -> commit from PROVINCE.md's own `## Adjacent` table."""
    text = Path(province_path).read_text(encoding="utf-8")
    blocks = chk.parse_blocks(text.splitlines())
    table = chk.select_province_table(blocks)
    pins = {}
    if table is None:
        return pins
    for _line_no, cells in table["rows"]:
        if len(cells) != chk.PROVINCE_COLUMNS:
            continue
        lane = chk.normalize_lane(cells[0])
        if lane:
            pins[lane] = cells[2].strip().lower()
    return pins


def read_census_rows(census_path, chk):
    """lane -> dict of the landed round-49 census row cells."""
    text = Path(census_path).read_text(encoding="utf-8")
    blocks = chk.parse_blocks(text.splitlines())
    table = chk.select_census_table(blocks)
    rows = {}
    if table is None:
        return rows
    for line_no, cells in table["rows"]:
        if len(cells) != chk.CENSUS_COLUMNS:
            continue
        lane = chk.normalize_lane(cells[0])
        if lane:
            rows[lane] = dict(zip(chk.CENSUS_CELL_NAMES, cells), line=line_no)
    return rows


def scope_description_lines(text):
    """Physical line numbers of the frontmatter `description` value.

    Extents mirror `description_of`'s own regex: the value starts at the
    `description:` line and ends before the next column-0 line (or the end of
    the frontmatter); blank lines inside the block are skipped.
    """
    if not text or not text.startswith("---"):
        return []
    front = text.split("\n---", 1)[0]
    match = re.search(r"^description:(.*?)(?=^\S|\Z)", front, re.S | re.M)
    if not match:
        return []
    lines = front.splitlines()
    start = front.count("\n", 0, match.start())
    end = front.count("\n", 0, match.end())
    out = []
    for index in range(start, min(end + 1, len(lines))):
        if lines[index].strip():
            out.append(index + 1)
    return out


def scope_province_lines(text):
    out = []
    for index, line in enumerate(text.splitlines(), 1):
        if re.match(r"^(?:\*\*)?(Domain|Owns)\b", line):
            out.append(index)
    return out


def kotoba_hits(chk, text):
    if text is None:
        return "-"
    return [i for i, line in enumerate(text.splitlines(), 1)
            if chk.token_in("kotoba", line)]


def shortstat_delta(repo, pin, head):
    code, out, _err = git(repo, "diff", "--shortstat", pin, head,
                          "--", "SKILL.md", "PROVINCE.md")
    if code != 0:
        return "error"
    out = out.strip()
    if not out:
        return "none"
    ins = SHORTSTAT_INS.search(out)
    dele = SHORTSTAT_DEL.search(out)
    return "+%s/-%s" % (ins.group(1) if ins else "0",
                        dele.group(1) if dele else "0")


def derive(chk, repo, commit, lane, all_lanes):
    """The three mechanical cells + the sibling-side `none` condition."""
    skill_text, _err = chk.git_show(repo, commit, "SKILL.md")
    province_text, _err2 = chk.git_show(repo, commit, "PROVINCE.md")
    if skill_text is None:
        return {"skill_file": "NONE", "names_kotoba": chk.NO_SKILL,
                "arbitration": chk.NO_SKILL, "description": "",
                "skill_text": None, "province_text": province_text,
                "selfcheck": "ok"}
    description = chk.description_of(skill_text)
    names = "yes" if chk.token_in(chk.SELF_LANE, description) else "no"
    named = sorted(n for n in all_lanes if n != lane and chk.token_in(n, description))
    arb = ("yes: " + ", ".join(named)) if named else "no"
    values = {"path": "SKILL.md", "names kotoba": names, "arbitration": arb}
    problems = chk.mechanical_findings(repo, commit, values, lane, all_lanes, "")
    return {"skill_file": "SKILL.md", "names_kotoba": names, "arbitration": arb,
            "description": description, "skill_text": skill_text,
            "province_text": province_text,
            "selfcheck": "ok" if not problems else "; ".join(problems)}


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--scratch", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--fleet", default="/home/vgpnk/Projects/shokunin")
    parser.add_argument("--lane-repo",
                        default="/home/vgpnk/Projects/shokunin/kotoba-shokunin")
    parser.add_argument("--freeze", default=None)
    parser.add_argument("--lanes", default=",".join(DEFAULT_LANES))
    parser.add_argument("--fixture", default=None,
                        help="also write a scratch census fragment whose "
                             "classification/path:line/quote cells are CARRIED "
                             "from the round-49 rows, so the base checker can "
                             "re-verify the derived cells of these lanes")
    args = parser.parse_args(argv)

    lane_repo = Path(args.lane_repo)
    fleet = Path(args.fleet)
    freeze_path = Path(args.freeze or lane_repo /
                       ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv")
    chk, base_copy = load_checker(args.scratch, lane_repo)

    freeze = read_freeze(freeze_path)
    # The checker calls mechanical_findings with `expected | {SELF_LANE}`
    # (check_sibling_census.py:746-747), so kotoba itself is part of the
    # arbitration vocabulary: a sibling description that names kotoba yields a
    # `kotoba` entry in the arbitration cell.  Deriving with the bare
    # fleet_lanes set silently drops it (kotodama's r49 row is the case).
    all_lanes = sorted(chk.fleet_lanes(fleet) | {chk.SELF_LANE})
    pins = read_province_pins(lane_repo / "PROVINCE.md", chk)
    r49 = read_census_rows(lane_repo / "corpus/knowledge/sibling-overlap-census-round49.md", chk)

    print("# base checker copy: %s" % base_copy)
    print("# base checker sha256: %s"
          % subprocess.run(["sha256sum", str(base_copy)], capture_output=True,
                           text=True).stdout.split()[0])
    print("# fleet lanes (%d): %s" % (len(all_lanes), ", ".join(all_lanes)))

    rows = []
    mismatches = []
    for lane in args.lanes.split(","):
        lane = lane.strip()
        if not lane:
            continue
        if lane not in freeze:
            sys.exit("lane %s is not in the freeze file %s" % (lane, freeze_path))
        head = freeze[lane]["head"]
        repo = chk.repo_dir_for(lane, fleet)
        pin = pins.get(lane, "")
        # (b) the freeze head must be an ancestor of the lane's branch head.
        code, _out, _err = git(repo, "merge-base", "--is-ancestor", head,
                               freeze[lane]["branch"])
        ancestor = "yes" if code == 0 else "NO(exit %d)" % code
        _c, tip, _e2 = git(repo, "rev-parse", freeze[lane]["branch"])
        tip = tip.strip()
        _c3, raw_short, _e3 = (git(repo, "diff", "--shortstat", pins.get(lane, head),
                                   head, "--", "SKILL.md", "PROVINCE.md")
                               if pins.get(lane) else (0, "", ""))
        print("# %s: tip %s = %s (%s freeze head %s); shortstat %r"
              % (lane, freeze[lane]["branch"], tip[:8],
                 "at freeze head" if tip == head else "MOVED past freeze head",
                 head[:8], raw_short.strip()))
        got = derive(chk, repo, head, lane, all_lanes)
        hits_skill = kotoba_hits(chk, got["skill_text"])
        hits_prov = kotoba_hits(chk, got["province_text"])
        skill_lines = scope_description_lines(got["skill_text"] or "")
        prov_lines = scope_province_lines(got["province_text"] or "")
        skill_text_lines = (got["skill_text"] or "").splitlines()
        prov_text_lines = (got["province_text"] or "").splitlines()
        scope_skill = ",".join("SKILL.md:%d" % n for n in skill_lines) or "-"
        scope_prov = ",".join("PROVINCE.md:%d" % n for n in prov_lines) or "-"
        preview_skill = " || ".join(
            "SKILL.md:%d %s" % (n, chk.collapse(skill_text_lines[n - 1]))
            for n in skill_lines) or "-"
        preview_prov = " || ".join(
            "PROVINCE.md:%d %s" % (n, chk.collapse(prov_text_lines[n - 1]))
            for n in prov_lines) or "-"
        cell_hits_skill = ",".join("SKILL.md:%d" % n for n in hits_skill) if isinstance(hits_skill, list) else "-"
        cell_hits_prov = ",".join("PROVINCE.md:%d" % n for n in hits_prov) if isinstance(hits_prov, list) else "-"
        old = r49.get(lane)
        # Does the round-49 quote still locate at the freeze head?  Mechanical
        # only (the checker's own locate_quote, same +/-2 window); the QUOTE
        # cell itself stays empty -- the scouts own it.
        quote_at_head = "-"
        if old and old["quote"].strip():
            try:
                q_path, q_line = chk.split_path_line(old["path:line"])
            except ValueError:
                q_path = None
            if q_path:
                q_text, _e = chk.git_show(repo, head, q_path)
                if q_text is not None:
                    found, index, heading = chk.locate_quote(
                        q_text.splitlines(), q_line,
                        chk.collapse(chk.strip_wrapping(old["quote"])))
                    quote_at_head = ("%s:%d%s" % (q_path, index + 1,
                                                  " (heading!)" if heading else "")
                                     if found else "no")

        row = {
            "lane": lane, "branch": freeze[lane]["branch"], "commit": head,
            "path": got["skill_file"], "classification": "",
            "names_kotoba": got["names_kotoba"], "arbitration": got["arbitration"],
            "path_line": "", "quote": "", "r49_pin": pin or "-",
            "delta": shortstat_delta(repo, pin, head) if pin else "no-pin",
            "r49_quote_at_head": quote_at_head,
            "kotoba_hits_skill_md": cell_hits_skill or "-",
            "kotoba_hits_province_md": cell_hits_prov or "-",
            "scope_skill_md": scope_skill, "scope_province_md": scope_prov,
            "scope_skill_text": preview_skill,
            "scope_province_text": preview_prov,
            "selfcheck": got["selfcheck"] + ("; ancestor " + ancestor
                                             if ancestor != "yes" else "; ok"),
        }

        # round-49 re-derivation: same script, the r49 pin, compare the cells.
        old = r49.get(lane)
        if old and pin:
            again = derive(chk, repo, pin, lane, all_lanes)
            pairs = (("skill_file", again["skill_file"], old["path"]),
                     ("names_kotoba", again["names_kotoba"], old["names kotoba"]),
                     ("arbitration", again["arbitration"], old["arbitration"]),
                     ("commit", pin, old["commit"].strip().lower()))
            for name, mine, landed in pairs:
                if mine.strip().lower() != landed.strip().lower():
                    mismatches.append(
                        "%s %s: re-derived %r != r49 row %r (census line %d)"
                        % (lane, name, mine, landed, old["line"]))
            print("# r49 re-derivation %s@%s: skill_file=%r names=%r arb=%r "
                  "| r49 row%r/%r/%r (line %d)"
                  % (lane, pin[:8], again["skill_file"], again["names_kotoba"],
                     again["arbitration"], old["path"], old["names kotoba"],
                     old["arbitration"], old["line"]))
        rows.append(row)

    out = Path(args.out)
    with out.open("w", encoding="utf-8") as handle:
        handle.write("\t".join(COLUMNS) + "\n")
        for row in rows:
            handle.write("\t".join(row[c] for c in COLUMNS) + "\n")
    print("# wrote %s (%d rows)" % (out, len(rows)))
    for row in rows:
        print("# %-9s %s %s %-4s names=%-3s arb=%-28s delta=%-10s self=%s"
              % (row["lane"], row["branch"], row["commit"][:8],
                 row["path"], row["names_kotoba"], row["arbitration"],
                 row["delta"], row["selfcheck"]))
    if args.fixture:
        out_lines = ["# fixture only: derived cells with classification, path:line and",
                     "# quote CARRIED from the round-49 rows (no classification is made",
                     "# by this seat); used to prove the derived cells pass the base",
                     "# checker's own row checks.", "",
                     "| lane | branch | commit | path | classification | names kotoba "
                     "| arbitration | path:line | quote |",
                     "|---|---|---|---|---|---|---|---|---|"]
        for row in rows:
            old = r49.get(row["lane"])
            if not old:
                continue
            out_lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |"
                             % (row["lane"], row["branch"], row["commit"], row["path"],
                                old["classification"], row["names_kotoba"],
                                row["arbitration"], old["path:line"], old["quote"]))
        Path(args.fixture).write_text("\n".join(out_lines) + "\n", encoding="utf-8")
        print("# wrote fixture %s" % args.fixture)

    if mismatches:
        print("\n## r49 MISMATCHES")
        for message in mismatches:
            print("- " + message)
        return 1
    print("\n## r49 re-derivation: all cells match the landed round-49 rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
