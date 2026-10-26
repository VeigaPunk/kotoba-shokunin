#!/usr/bin/env python3
"""derive_rows.py -- mechanical C2 row cells for the round-74 sibling census.

Seat ExecSibRowsBR74 (round 74, wave 1).  Reads, for the five assigned lanes
(kaidoku, kake, kama, kasegi, kengaku), the frozen fleet heads
(`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`) and derives the
mechanical census cells from the sibling bytes with the BASE checker's own
derivation functions -- `description_of`, `token_in`, `fleet_lanes`,
`git_show`, `extract_adjacent_section`, `parse_blocks`,
`select_province_table` -- imported from a scratch copy of
`git show <base>:verifiers/check_sibling_census.py`.  Nothing is
re-implemented and nothing is taken from the measured revision (Q33: the
measured revision supplies bytes, not code).

Column names follow the ones the other round-74 row seats already wrote
(ExecSibRowsA/D: `skill_file`, `names_kotoba`, `arbitration`, `quote_at`,
`quote`; ExecSibRowsC: `r49_pin`, `delta`, `kotoba_hits_*`, `scope_*`), so the
merge seat joins one shape.

Emitted per lane:
  lane, branch, commit, r49_pin, skill_file, classification, names_kotoba,
  arbitration, quote_at, path_line, quote, delta, kotoba_hits_skill_md,
  kotoba_hits_province_md, scope_skill_md, scope_province_md,
  scope_skill_text, scope_province_text
`classification`, `quote_at`, `path_line` and `quote` stay EMPTY: the scouts
ScoutSib* own them and ExecSibMergeR74 joins.

Derivation rules (from the base checker, not restated here as a second
convention):
  * `skill_file` -- `SKILL.md` when the file exists at the frozen head,
    `none` when it does not;
  * `names_kotoba` -- `yes`/`no`: `token_in("kotoba", description)` on the
    frontmatter description (`description_of`);
  * `arbitration` -- `yes: <sorted lane names>` over the fleet lane set plus
    kotoba (the base's `all_lanes`), else `no`;
  * `delta` -- `+ins/-del` summed over `git diff --shortstat <r49 pin>
    <freeze head> -- SKILL.md PROVINCE.md`, `none` when the diff is empty;
  * `kotoba_hits_*` -- `path:line` for every line of SKILL.md / PROVINCE.md at
    the frozen head where `token_in("kotoba", line)` holds, `-` when none;
  * `scope_skill_md` / `scope_province_md` -- the frontmatter description's
    physical lines (same end rule as `description_of`) and PROVINCE.md's
    `Domain`/`Owns` label lines with their non-blank continuations; the
    `scope_*_text` columns carry the whitespace-collapsed line text.

`--verify-r49` re-derives branch, commit, skill file, names-kotoba and
arbitration at the round-49 pins (taken from the base-revision PROVINCE.md
`## Adjacent` table) and compares them cell-by-cell with the committed
round-49 entry.  A mismatch means the checker's derivation changed or the
round-49 row was wrong; the script exits 3 and names the cell.

Read-only: `git show` / `git diff --shortstat` / `git rev-parse
--verify` / `git merge-base --is-ancestor` only; the only writes are the two
output files named on the command line and its own scratch temp dir.
Stdlib only.
"""

import argparse
import hashlib
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANES = ("kaidoku", "kake", "kama", "kasegi", "kengaku")
FREEZE = ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
R49_CENSUS = "corpus/knowledge/sibling-overlap-census-round49.md"
R49_CELLS = ("lane", "branch", "commit", "skill file", "classification",
             "names kotoba", "arbitration", "scope quote at", "scope quote")
HEADER = ("lane", "branch", "commit", "r49_pin", "skill_file",
          "classification", "names_kotoba", "arbitration", "quote_at",
          "path_line", "quote", "delta", "kotoba_hits_skill_md",
          "kotoba_hits_province_md", "scope_skill_md", "scope_province_md",
          "scope_skill_text", "scope_province_text")
EMPTY = ("classification", "quote_at", "path_line", "quote")

SHORTSTAT_INS = re.compile(r"(\d+) insertions?\(\+\)")
SHORTSTAT_DEL = re.compile(r"(\d+) deletions?\(-\)")
DESCRIPTION_LINE = re.compile(r"\Adescription:")
COLUMN0 = re.compile(r"\A\S")
PROVINCE_LABEL = re.compile(r"\A(?:\*\*)?(Domain|Owns)(?:\*\*)?\s*:")
PROVINCE_ANY_LABEL = re.compile(
    r"\A(?:\*\*[^*]{1,40}:\*\*|[A-Z][A-Za-z /()-]{0,30}:)")


def git(repo, *args):
    proc = subprocess.run(["git", "-C", str(repo)] + list(args),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return (proc.returncode, proc.stdout.decode("utf-8", "replace"),
            proc.stderr.decode("utf-8", "replace"))


def load_checker(lane_repo, base_rev, scratch):
    code, out, err = git(lane_repo, "show",
                         "%s:verifiers/check_sibling_census.py" % base_rev)
    if code != 0:
        raise SystemExit("cannot read the base checker at %s: %s"
                         % (base_rev, err.strip().splitlines()[:1]))
    path = Path(scratch) / "check_sibling_census_base.py"
    path.write_bytes(out.encode("utf-8"))
    spec = importlib.util.spec_from_file_location("base_census", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, hashlib.sha256(out.encode("utf-8")).hexdigest()


def read_freeze(path):
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        cells = line.split("\t")
        if cells[0] == "lane":
            continue
        rows[cells[0]] = {"branch": cells[1], "head": cells[2],
                          "skill_blob": cells[3], "province_blob": cells[4]}
    return rows


def r49_pins(checker, province_text):
    """lane -> commit from the base PROVINCE.md `## Adjacent` table."""
    body = checker.extract_adjacent_section(province_text)
    if body is None:
        raise SystemExit("no `## Adjacent` section in the base PROVINCE.md")
    table = checker.select_province_table(checker.parse_blocks(body))
    if table is None:
        raise SystemExit("no province table in the base PROVINCE.md")
    pins = {}
    for _line, cells in table["rows"]:
        if len(cells) != checker.PROVINCE_COLUMNS:
            continue
        lane = checker.normalize_lane(cells[0])
        if lane:
            pins[lane] = cells[2].strip().lower()
    return pins


def shortstat_delta(repo, pin, head):
    """`+ins/-del` summed over SKILL.md and PROVINCE.md, or `none`."""
    code, out, err = git(repo, "diff", "--shortstat", pin, head, "--",
                         "SKILL.md", "PROVINCE.md")
    if code != 0:
        raise SystemExit("git diff --shortstat %s %s failed in %s: %s"
                         % (pin, head, repo, err.strip().splitlines()[:1]))
    text = out.strip()
    if not text:
        return "none"
    ins = SHORTSTAT_INS.search(text)
    dele = SHORTSTAT_DEL.search(text)
    return "+%s/-%s" % (ins.group(1) if ins else "0",
                        dele.group(1) if dele else "0")


def kotoba_hits(checker, repo, commit, name):
    hits = []
    text, _err = checker.git_show(repo, commit, name)
    if text is None:
        return hits
    for number, line in enumerate(text.splitlines(), 1):
        if checker.token_in(checker.SELF_LANE, line):
            hits.append("%s:%d" % (name, number))
    return hits


def description_lines(skill_text):
    """`path:line`+`text` for the frontmatter `description`'s physical lines.

    Same end rule as `description_of`: the value runs to the next column-0
    line, inside the frontmatter only.
    """
    if skill_text is None or not skill_text.startswith("---"):
        return []
    lines = skill_text.splitlines()
    front_end = None
    for index, line in enumerate(lines[1:], 2):
        if line.startswith("---"):
            front_end = index
            break
    if front_end is None:
        return []
    start = None
    for index in range(2, front_end + 1):
        if DESCRIPTION_LINE.match(lines[index - 1]):
            start = index
            break
    if start is None:
        return []
    out = [("SKILL.md:%d" % start, lines[start - 1])]
    for index in range(start + 1, front_end + 1):
        if COLUMN0.match(lines[index - 1]):
            break
        out.append(("SKILL.md:%d" % index, lines[index - 1]))
    return out


def province_surface_lines(province_text):
    """`path:line`+`text` for `Domain` / `Owns` labels and continuations."""
    if province_text is None:
        return []
    lines = province_text.splitlines()
    out = []
    index = 1
    while index <= len(lines):
        line = lines[index - 1]
        if PROVINCE_LABEL.match(line):
            out.append(("PROVINCE.md:%d" % index, line))
            index += 1
            while index <= len(lines) and lines[index - 1].strip():
                nxt = lines[index - 1]
                if PROVINCE_ANY_LABEL.match(nxt) or nxt.startswith("#") \
                        or nxt.strip().startswith("|"):
                    break
                out.append(("PROVINCE.md:%d" % index, nxt))
                index += 1
            continue
        index += 1
    return out


def derive_cells(checker, fleet_root, lane, commit):
    """(cells, description, skill_text, province_text) for one lane."""
    repo = fleet_root / (lane + "-shokunin")
    skill_text, _err = checker.git_show(repo, commit, "SKILL.md")
    province_text, _province_err = checker.git_show(repo, commit, "PROVINCE.md")
    all_lanes = checker.fleet_lanes(fleet_root) | {checker.SELF_LANE}
    cells = {}
    if skill_text is None:
        cells["skill_file"] = "none"
        cells["names_kotoba"] = checker.NO_SKILL.lower()
        cells["arbitration"] = checker.NO_SKILL.lower()
        description = ""
    else:
        description = checker.description_of(skill_text)
        cells["skill_file"] = "SKILL.md"
        cells["names_kotoba"] = "yes" if checker.token_in(
            checker.SELF_LANE, description) else "no"
        named = sorted(n for n in all_lanes
                       if n != lane and checker.token_in(n, description))
        cells["arbitration"] = ("yes: " + ", ".join(named)) if named else "no"
    skill_hits = kotoba_hits(checker, repo, commit, "SKILL.md")
    province_hits = kotoba_hits(checker, repo, commit, "PROVINCE.md")
    cells["kotoba_hits_skill_md"] = ",".join(skill_hits) or "-"
    cells["kotoba_hits_province_md"] = ",".join(province_hits) or "-"
    skill_scope = description_lines(skill_text)
    province_scope = province_surface_lines(province_text)
    cells["scope_skill_md"] = ",".join(at for at, _text in skill_scope) or "-"
    cells["scope_province_md"] = ",".join(
        at for at, _text in province_scope) or "-"
    cells["scope_skill_text"] = " || ".join(
        "%s %s" % (at, checker.collapse(text)) for at, text in skill_scope)
    cells["scope_province_text"] = " || ".join(
        "%s %s" % (at, checker.collapse(text)) for at, text in province_scope)
    return cells, description, skill_text, province_text


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--lane-repo",
                        default="/home/vgpnk/Projects/shokunin/kotoba-shokunin")
    parser.add_argument("--fleet", default="/home/vgpnk/Projects/shokunin")
    parser.add_argument("--base",
                        default="1e03d1991bc02281b00a5b7a5e00c9d5d5d72908")
    parser.add_argument("--freeze", default=FREEZE)
    parser.add_argument("--r49-census", default=R49_CENSUS)
    parser.add_argument("--out", default="rows.tsv")
    parser.add_argument("--candidates", default="scope-candidates.tsv")
    parser.add_argument("--verify-r49", action="store_true")
    args = parser.parse_args(argv)
    lane_repo = Path(args.lane_repo).resolve()
    fleet_root = Path(args.fleet).resolve()
    scratch = tempfile.mkdtemp(prefix="derive_rows_")
    try:
        checker, checker_sha = load_checker(lane_repo, args.base, scratch)
        print("checker: %s:verifiers/check_sibling_census.py sha256=%s"
              % (args.base[:12], checker_sha))
        freeze = read_freeze(lane_repo / args.freeze)
        base_province, _err = checker.git_show(lane_repo, args.base,
                                               "PROVINCE.md")
        pins = r49_pins(checker, base_province)
        expected = checker.fleet_lanes(fleet_root)
        if set(freeze) != expected:
            raise SystemExit("freeze lanes differ from the fleet lane set: "
                             "only-in-freeze=%s only-in-fleet=%s"
                             % (sorted(set(freeze) - expected),
                                sorted(expected - set(freeze))))
        print("fleet lanes: %d; freeze lanes: %d" % (len(expected), len(freeze)))

        r49_rows = {}
        if args.verify_r49:
            census = (lane_repo / args.r49_census).read_text(encoding="utf-8")
            table = checker.select_census_table(checker.parse_blocks(
                census.splitlines()))
            if table is None:
                raise SystemExit("r49 census table not found")
            for _line, cells in table["rows"]:
                if len(cells) == checker.CENSUS_COLUMNS:
                    r49_rows[checker.normalize_lane(cells[0])] = dict(
                        zip(R49_CELLS, cells))

        out_rows = []
        candidate_rows = []
        verify_failures = []
        for lane in LANES:
            entry = freeze[lane]
            pin = pins[lane]
            repo = fleet_root / (lane + "-shokunin")
            cells, _description, skill_text, province_text = derive_cells(
                checker, fleet_root, lane, entry["head"])
            row = {name: "" for name in HEADER}
            row["lane"] = lane
            row["branch"] = entry["branch"]
            row["commit"] = entry["head"]
            row["r49_pin"] = pin
            row["delta"] = shortstat_delta(repo, pin, entry["head"])
            for name, value in cells.items():
                row[name] = value
            out_rows.append(row)
            for at, text in description_lines(skill_text):
                candidate_rows.append((lane, "SKILL.md", at, text))
            for at, text in province_surface_lines(province_text):
                candidate_rows.append((lane, "PROVINCE.md", at, text))

            # The freeze file's blob pins must be the bytes this run reads.
            for name, want in (("SKILL.md", entry["skill_blob"]),
                               ("PROVINCE.md", entry["province_blob"])):
                code, out, _err = git(repo, "rev-parse",
                                      "%s:%s" % (entry["head"], name))
                if code == 0 and want != "-" and out.strip() != want:
                    raise SystemExit("%s: %s blob at %s is %s, freeze says %s"
                                     % (lane, name, entry["head"][:12],
                                        out.strip()[:12], want[:12]))

            # The freeze head must be the branch head or its ancestor.
            code, out, _err = git(repo, "rev-parse", "--verify",
                                  "refs/heads/%s" % entry["branch"])
            branch_head = out.strip()
            code, _out, err = git(repo, "merge-base", "--is-ancestor",
                                  entry["head"], branch_head)
            if code != 0:
                raise SystemExit("%s: freeze head %s is not an ancestor of "
                                 "refs/heads/%s=%s (%s)"
                                 % (lane, entry["head"], entry["branch"],
                                    branch_head, err.strip()))
            print("%s: branch head %s; freeze head %s %s"
                  % (lane, branch_head[:12], entry["head"][:12],
                     "equal" if branch_head == entry["head"] else "ancestor"))

            if args.verify_r49:
                old = r49_rows.get(lane)
                if old is None:
                    verify_failures.append("%s: no r49 row" % lane)
                    continue
                derived = derive_cells(checker, fleet_root, lane, pin)[0]
                derived["branch"] = old["branch"].strip()
                derived["commit"] = pin
                mapping = (("branch", "branch"), ("commit", "commit"),
                           ("skill file", "skill_file"),
                           ("names kotoba", "names_kotoba"),
                           ("arbitration", "arbitration"))
                for old_name, new_name in mapping:
                    want = old[old_name].strip()
                    if new_name in ("names_kotoba", "arbitration"):
                        want = want.lower()
                    if derived[new_name] != want:
                        verify_failures.append(
                            "%s: %s at the r49 pin: derived %r, r49 row %r"
                            % (lane, old_name, derived[new_name], want))

        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write("\t".join(HEADER) + "\n")
            for row in out_rows:
                handle.write("\t".join(row[name] for name in HEADER) + "\n")
        with open(args.candidates, "w", encoding="utf-8") as handle:
            handle.write("lane\tfile\tline\ttext\n")
            for lane, name, at, text in candidate_rows:
                number = at.rsplit(":", 1)[1]
                flat = re.sub(r"\s+", " ", text).strip()
                handle.write("%s\t%s\t%s\t%s\n" % (lane, name, number, flat))
        print("wrote %s (%d rows) and %s (%d candidate lines)"
              % (args.out, len(out_rows), args.candidates, len(candidate_rows)))

        if args.verify_r49:
            if verify_failures:
                print("r49 re-derivation: %d DISCREPANCY(IES)"
                      % len(verify_failures))
                for message in verify_failures:
                    print("  " + message)
                return 3
            print("r49 re-derivation: %d of %d lanes match on branch, commit, "
                  "skill file, names kotoba, arbitration"
                  % (len(LANES), len(LANES)))
        return 0
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
