#!/usr/bin/env python3
"""roundtrip_test.py -- prove merge_census.py reproduces known-good shapes and
refuses every case its seat contract names.

Round-trip (the falsifier): the round-49 census entry's 20 table rows and the
`## Adjacent` rows of `PROVINCE.md` at the frozen base are parsed, split into
four rows TSVs and ten scout JSONs (the round-74 input schemas), and fed back
through the tool.  The regenerated census table must equal the r49 table row for
row, and the regenerated PROVINCE rows must equal the base PROVINCE rows.

Then nine refusal cases, each expecting exit 2 and a message naming the lane or
path.  Fixtures live under --work (a scratch directory the caller deletes).

Usage:
  python3 roundtrip_test.py --tool merge_census.py --lane <lane root> \
      --base 1e03d1991bc02281b00a5b7a5e00c9d5d5d72908 --work /tmp/k74...
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

WS_RUN = re.compile(r"\s+")
CELL_SPLIT = re.compile(r"(?<!\\)\|")
SEPARATOR_CELL = re.compile(r"\A:?-{2,}:?\Z")
ROWS_DIRS = ("ExecSibRowsAR74", "ExecSibRowsBR74", "ExecSibRowsCR74",
             "ExecSibRowsDR74")


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [p.replace("\\|", "|").strip() for p in CELL_SPLIT.split(s)]


def is_separator(cells):
    return bool(cells) and all(SEPARATOR_CELL.match(c) for c in cells)


def table_blocks(text):
    blocks, current = [], []
    for line in text.splitlines():
        if line.strip().startswith("|"):
            current.append(line)
        elif current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def pick_table(text, columns, first_header):
    for block in table_blocks(text):
        header = split_row(block[0])
        if len(header) != columns or header[0].strip().lower() != first_header:
            continue
        body = block[1:]
        if body and is_separator(split_row(body[0])):
            body = body[1:]
        return header, [split_row(line) for line in body], block
    raise SystemExit("no %d-column table starting with %r" % (columns, first_header))


def git_show(repo, rev, path):
    proc = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (rev, path)],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit("git show %s:%s failed: %s" % (rev, path, proc.stderr))
    return proc.stdout


def run(tool, args):
    return subprocess.run([sys.executable, str(tool)] + args,
                          capture_output=True, text=True)


def diff(expected, actual, label):
    if expected == actual:
        print("PASS %s: %d line(s), diff empty" % (label, len(expected)))
        return True
    print("FAIL %s" % label)
    for line in difflib.unified_diff(expected, actual, "expected", "regenerated",
                                     lineterm="", n=1):
        print("  " + line)
    return False


def write_fixtures(rows, province, root):
    """rows: r49 table cells (9); province: {lane: boundary cell}."""
    root.mkdir(parents=True, exist_ok=True)
    lanes = [cells[0] for cells in rows]
    ordered = sorted(rows, key=lambda cells: cells[0])
    assert lanes == sorted(lanes), "the r49 table is not sorted by lane"

    # four rows TSVs, five lanes each, header + the six required cells + the
    # two optional quote cells (the r49 cells, wrapping quotes included).
    for index, directory in enumerate(ROWS_DIRS):
        chunk = ordered[index * 5:(index + 1) * 5]
        lines = ["lane\tbranch\tcommit\tskill_file\tnames_kotoba\tarbitration"
                 "\tquote_at\tquote"]
        for lane, branch, commit, skill_file, _cls, names, arb, quote_at, quote in chunk:
            lines.append("\t".join([lane, branch, commit, skill_file, names, arb,
                                    quote_at, quote]))
        target = root / directory / "rows.tsv"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ten scout JSONs, two lanes each
    for index in range(10):
        directory = root / ("ScoutSibFix%02dR74" % (index + 1))
        directory.mkdir(parents=True, exist_ok=True)
        for lane, branch, commit, _skill, cls, _names, _arb, quote_at, quote in \
                ordered[index * 2:(index + 1) * 2]:
            record = {"lane": lane, "head40": commit,
                      "proposed_classification": cls, "quote": quote,
                      "quote_path_line": quote_at,
                      "boundary": province[lane], "r49_classification": cls,
                      "changed": False}
            (directory / (lane + ".json")).write_text(
                json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8")

    # the freeze fixture: the r49 pins are both the pin and the head here, so
    # every delta is `none` (the git path is still exercised).
    lines = ["# fixture freeze built from the round-49 table rows"]
    for lane, branch, commit, _skill, _cls, _names, _arb, _qa, _q in ordered:
        lines.append("\t".join([lane, branch, commit, "-", "-"]))
    freeze = root / "freeze.tsv"
    freeze.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return freeze


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--tool", default=str(Path(__file__).with_name("merge_census.py")))
    parser.add_argument("--lane", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--work", required=True)
    parser.add_argument("--fleet-root", default="/home/vgpnk/Projects/shokunin")
    args = parser.parse_args(argv)

    lane_root = Path(args.lane)
    work = Path(args.work)
    tool = Path(args.tool)
    census_path = lane_root / "corpus/knowledge/sibling-overlap-census-round49.md"

    header, rows, block = pick_table(census_path.read_text(encoding="utf-8"), 9, "lane")
    print("r49 census table: %d rows, header %d cells" % (len(rows), len(header)))
    assert len(rows) == 20, "expected the 20 r49 rows, found %d" % len(rows)

    province_text = git_show(lane_root, args.base, "PROVINCE.md")
    p_header, p_rows, p_block = pick_table(province_text, 4, "lane")
    province = {cells[0]: cells[3] for cells in p_rows}
    print("base PROVINCE section-Adjacent rows: %d" % len(p_rows))
    assert set(province) == {cells[0] for cells in rows}, "lane sets differ"

    fixtures = work / "fixtures"
    freeze = write_fixtures(rows, province, fixtures)

    expected_r49 = ["| " + " | ".join(cells) + " |" for cells in rows]
    expected_r49 = [header_line(header)] + [block[1]] + expected_r49
    expected_province = ["| " + " | ".join(cells) + " |" for cells in p_rows]
    expected_province = ["| lane | classification | commit | boundary |",
                         "|---|---|---|---|"] + expected_province

    ok = True
    regen_r49 = run(tool, ["--inputs-root", str(fixtures), "--freeze", str(freeze),
                           "--shape", "census-r49"])
    if regen_r49.returncode != 0:
        print("FAIL census-r49 exit %d\n%s" % (regen_r49.returncode, regen_r49.stderr))
        ok = False
    else:
        (work / "regen-r49.md").write_text(regen_r49.stdout, encoding="utf-8")
        ok &= diff(expected_r49, regen_r49.stdout.rstrip("\n").splitlines(),
                   "census-r49 round-trip against the r49 table")

    regen_province = run(tool, ["--inputs-root", str(fixtures), "--freeze", str(freeze),
                                "--shape", "province"])
    if regen_province.returncode != 0:
        print("FAIL province exit %d\n%s" % (regen_province.returncode,
                                             regen_province.stderr))
        ok = False
    else:
        (work / "regen-province.md").write_text(regen_province.stdout, encoding="utf-8")
        ok &= diff(expected_province,
                   regen_province.stdout.rstrip("\n").splitlines(),
                   "province round-trip against base PROVINCE.md")

    regen_census = run(tool, ["--inputs-root", str(fixtures), "--freeze", str(freeze),
                              "--shape", "census", "--base-rev", args.base,
                              "--lane-root", str(lane_root)])
    if regen_census.returncode != 0:
        print("FAIL census exit %d\n%s" % (regen_census.returncode,
                                           regen_census.stderr))
        ok = False
    else:
        (work / "regen-census.md").write_text(regen_census.stdout, encoding="utf-8")
        lines = regen_census.stdout.rstrip("\n").splitlines()
        body = lines[2:]
        deltas = [split_row(line)[-1] for line in body]
        good = (len(body) == 20 and len(split_row(lines[0])) == 10
                and deltas == ["none"] * 20)
        print("%s census shape: %d rows, %d columns, deltas %s"
              % ("PASS" if good else "FAIL", len(body),
                 len(split_row(lines[0])), sorted(set(deltas))))
        ok &= good

    # ------------------------------------------------------------------
    # refusals
    # ------------------------------------------------------------------
    cases = []

    def prepare(name):
        target = work / "cases" / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(fixtures, target)
        return target

    def case(name, expect, shape="census-r49", mutate=None, extra=()):
        root = prepare(name)
        if mutate:
            mutate(root)
        result = run(tool, ["--inputs-root", str(root), "--freeze",
                            str(root / "freeze.tsv"), "--shape", shape,
                            "--base-rev", args.base, "--lane-root",
                            str(lane_root)] + list(extra))
        hit = expect in result.stderr
        print("%s refusal %-22s exit %d, expects %r"
              % ("PASS" if result.returncode == 2 and hit else "FAIL",
                 name, result.returncode, expect))
        for line in result.stderr.splitlines()[:2]:
            print("    " + line)
        return result.returncode == 2 and hit

    def edit_json(root, lane, **changes):
        for path in root.glob("ScoutSib*R74/%s.json" % lane):
            record = json.loads(path.read_text(encoding="utf-8"))
            record.update(changes)
            path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")

    def edit_tsv(root, lane, column, value):
        index = {"commit": 2, "skill_file": 3, "names_kotoba": 4,
                 "arbitration": 5, "quote_at": 6, "quote": 7}[column]
        for path in root.glob("ExecSibRows*R74/rows.tsv"):
            lines = path.read_text(encoding="utf-8").splitlines()
            changed = False
            for number, line in enumerate(lines[1:], 1):
                cells = line.split("\t")
                if cells[0] == lane:
                    cells[index] = value
                    lines[number] = "\t".join(cells)
                    changed = True
            if changed:
                path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    ok &= case("missing-rows-file", "missing rows file",
               mutate=lambda root: (root / "ExecSibRowsBR74/rows.tsv").unlink())
    ok &= case("duplicate-lane", "lane is in two rows files",
               mutate=lambda root: (root / "ExecSibRowsBR74/rows.tsv").write_text(
                   (root / "ExecSibRowsBR74/rows.tsv").read_text(encoding="utf-8")
                   + (root / "ExecSibRowsAR74/rows.tsv").read_text(
                       encoding="utf-8").splitlines()[1] + "\n", encoding="utf-8"))
    ok &= case("head40-vs-rows", "differs from scout head40",
               mutate=lambda root: edit_json(root, "kagi", head40="0" * 40))
    ok &= case("head40-vs-freeze", "differs from the freeze head",
               mutate=lambda root: (edit_json(root, "kagi", head40="1" * 40),
                                    edit_tsv(root, "kagi", "commit", "1" * 40)))
    ok &= case("empty-quote", "empty quote",
               mutate=lambda root: edit_json(root, "lore", quote=""))
    ok &= case("bad-classification", "not one of contested/adjacent/none",
               mutate=lambda root: edit_json(root, "mado",
                                             proposed_classification="shared"))
    ok &= case("pipe-in-cell", "contains a `|`",
               mutate=lambda root: edit_json(root, "tabi",
                                             boundary="browser craft | not ours"))
    ok &= case("lane-set-short", "but no scout record",
               mutate=lambda root: [p.unlink() for p in
                                    root.glob("ScoutSib*R74/tsukuroi.json")])
    ok &= case("lane-set-extra", "is not in the freeze file",
               mutate=lambda root: (
                   (root / "ScoutSibFix01R74/zzz.json").write_text(
                       json.dumps({"lane": "zzz", "head40": "0" * 40,
                                   "proposed_classification": "none",
                                   "quote": "a quote of six words at least here",
                                   "quote_path_line": "SKILL.md:3",
                                   "boundary": "not a fleet lane",
                                   "r49_classification": "none",
                                   "changed": False}) + "\n", encoding="utf-8"),
                   (root / "ExecSibRowsAR74/rows.tsv").write_text(
                       (root / "ExecSibRowsAR74/rows.tsv").read_text(encoding="utf-8")
                       + "\t".join(["zzz", "master", "0" * 40, "NONE", "no SKILL.md",
                                    "no SKILL.md", "", ""]) + "\n", encoding="utf-8")))
    ok &= case("changed-contradicts-delta", "changed=true but git diff",
               shape="census",
               mutate=lambda root: edit_json(root, "audio", changed=True))
    ok &= case("rows-quote-disagrees", "rows quote differs from the scout quote",
               mutate=lambda root: edit_tsv(root, "souji", "quote",
                                            '"a different sentence entirely"'))

    # ------------------------------------------------------------------
    # a positive delta: a freeze head that has moved past the r49 pin must
    # produce the plan's shortstat, not `none`
    # ------------------------------------------------------------------
    lane = "kake"
    head = subprocess.run(["git", "-C", str(Path(args.fleet_root) / "kake-shokunin"),
                           "rev-parse", "master"], capture_output=True,
                          text=True).stdout.strip()
    root = prepare("delta-nonzero")
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        print("SKIP delta-nonzero: no kake head")
    else:
        lines = (root / "freeze.tsv").read_text(encoding="utf-8").splitlines()
        lines = ["\t".join([lane, "master", head, "-", "-"])
                 if line.startswith(lane + "\t") else line for line in lines]
        (root / "freeze.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
        edit_tsv(root, lane, "commit", head)
        edit_json(root, lane, head40=head, changed=True)
        result = run(tool, ["--inputs-root", str(root), "--freeze",
                            str(root / "freeze.tsv"), "--shape", "census",
                            "--base-rev", args.base, "--lane-root", str(lane_root),
                            "--fleet-root", args.fleet_root])
        pin = None
        for cells in p_rows:
            if cells[0] == lane:
                pin = cells[2]
        direct = subprocess.run(["git", "-C", str(Path(args.fleet_root) / "kake-shokunin"),
                                 "diff", "--shortstat", pin, head, "--", "SKILL.md",
                                 "PROVINCE.md"], capture_output=True, text=True).stdout
        direct = WS_RUN.sub(" ", direct).strip()
        cell = None
        for line in result.stdout.splitlines():
            if line.startswith("| " + lane + " |"):
                cell = split_row(line)[-1]
        good = (result.returncode == 0 and cell == direct and direct
                and re.search(r"\d+ files? changed", direct) is not None)
        print("%s delta-nonzero: exit %d, cell %r, direct shortstat %r"
              % ("PASS" if good else "FAIL", result.returncode, cell, direct))
        if result.returncode != 0:
            print("    " + result.stderr.splitlines()[0] if result.stderr else "")
        ok &= bool(good)

    print("RESULT %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def header_line(header):
    return "| " + " | ".join(header) + " |"


if __name__ == "__main__":
    sys.exit(main())
