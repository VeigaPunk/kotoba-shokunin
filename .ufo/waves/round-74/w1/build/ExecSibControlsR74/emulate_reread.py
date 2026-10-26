#!/usr/bin/env python3
"""emulate_reread.py -- expected-score emulator for the round-74 C2 controls.

This is NOT the round-74 counter.  It applies the frozen C2 conjuncts (a)-(e)
of `plans/round-74.md` to one world's overlay, using the *base* revision's
`check_sibling_census.py` (sha256 2f9d8a88b1d3dd8562455006d5ea89ec02546a1ecb9d023f327d88e5502eedc7,
`git show 1e03d199:verifiers/check_sibling_census.py`) for conjunct (a) and the
province cross-check, exactly as the plan says the measured revision must not
supply the code.  Conjuncts (b), (c) and (e) are re-implemented here from the
plan's wording; where the plan is ambiguous the ambiguity is named in the
output (`note:`), never silently resolved.

Usage:
    python3 -B emulate_reread.py <world-dir> [--fleet /home/vgpnk/Projects/shokunin]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_sibling_census_base as base  # noqa: E402

ENTRY_REL = "corpus/knowledge/sibling-overlap-census-round74.md"
FREEZE_REL = ".ufo/waves/round-74/receipts/sibling-heads-freeze.tsv"
HEADER9 = ("| lane | branch | commit | path | classification | names kotoba "
           "| arbitration | path:line | quote |")
SEP9 = "|---|---|---|---|---|---|---|---|---|"
LANE_SUFFIX = "-shokunin"


def git(repo, *args):
    p = subprocess.run(["git", "-C", str(repo)] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def read_freeze(path):
    rows = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        lane, branch, head = line.split("\t")[:3]
        rows[lane] = {"branch": branch, "head40": head}
    return rows


def split_cells(line):
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)]
    if cells and cells[0] == "":
        cells = cells[1:]
    if cells and cells[-1] == "":
        cells = cells[:-1]
    return cells


def read_entry_table(text):
    """Return (header_cells, rows) for the census table of the entry."""
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith("| lane | branch | commit |"):
            start = i
            break
    if start is None:
        return None, []
    header = split_cells(lines[start])
    rows = []
    i = start + 2
    while i < len(lines) and lines[i].startswith("|"):
        rows.append(split_cells(lines[i]))
        i += 1
    return header, rows


def nine_column_table(header, rows):
    """The census table as the base checker reads it: nine cells per row."""
    out = [HEADER9, SEP9]
    for cells in rows:
        out.append("| " + " | ".join(cells[:9]) + " |")
    return "\n".join(out) + "\n"


def province_adjacent_rows(text):
    body = base.extract_adjacent_section(text)
    if body is None:
        return {}
    table = base.select_province_table(base.parse_blocks(body))
    if table is None:
        return {}
    out = {}
    for _line_no, cells in table["rows"]:
        if len(cells) != 4:
            continue
        out[base.normalize_lane(cells[0])] = {
            "classification": cells[1].strip().lower(),
            "commit": cells[2].strip().lower()}
    return out


SHORTSTAT = re.compile(r"(\d+) files? changed"
                       r"(?:, (\d+) insertions?\(\+\))?"
                       r"(?:, (\d+) deletions?\(-\))?")
# The round-74 counter renders the delta as `+<ins>/-<del>`; the emulator uses
# the same rendering so a world's (c) status means the same thing under both.


def render_delta(shortstat_text):
    text = " ".join(shortstat_text.split())
    if not text:
        return "none"
    match = SHORTSTAT.search(text)
    if not match:
        return "ERR"
    return "+%d/-%d" % (int(match.group(2) or 0), int(match.group(3) or 0))


def delta_for(lane, pin, head, fleet):
    rc, out, err = git(fleet / (lane + LANE_SUFFIX), "diff", "--shortstat",
                       pin, head, "--", "SKILL.md", "PROVINCE.md")
    if rc != 0:
        return "ERR"
    return render_delta(out)


def names_kotoba(repo, commit, path):
    rc, out, err = git(repo, "show", "%s:%s" % (commit, path))
    if rc != 0:
        return False
    return base.token_in("kotoba", out)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("world", help="world directory (holds overlay/)")
    ap.add_argument("--fleet", default="/home/vgpnk/Projects/shokunin")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)
    world = Path(args.world).resolve()
    fleet = Path(args.fleet)
    entry_path = world / "overlay" / ENTRY_REL
    province_path = world / "overlay" / "PROVINCE.md"
    freeze_path = world / "overlay" / FREEZE_REL
    if not entry_path.exists():
        print("no entry overlay at %s" % entry_path, file=sys.stderr)
        return 2
    freeze = read_freeze(freeze_path)
    text = entry_path.read_text(encoding="utf-8")
    header, rows = read_entry_table(text)
    entry_province = province_adjacent_rows(province_path.read_text(encoding="utf-8"))
    notes = []

    # --- conjunct (a): the base copy of check_sibling_census.py, verbatim ----
    with tempfile.TemporaryDirectory() as tmp:
        census_tmp = Path(tmp) / "census9.md"
        census_tmp.write_text(nine_column_table(header, rows), encoding="utf-8")
        result = base.check_census(census_tmp, fleet, province_path)
    failures_a = {}
    failures_d = {}
    per_lane_rows = {}
    for message in result["failures"]:
        m = re.search(r"\(lane ([a-z0-9-]+)\)", message)
        if message.startswith("province row"):
            m2 = re.search(r"lane ([a-z0-9-]+)", message)
            if m2:
                failures_d.setdefault(m2.group(1), []).append(message)
            else:
                notes.append("province failure without a lane: " + message[:120])
            continue
        if m:
            failures_a.setdefault(m.group(1), []).append(message)
        elif message.startswith("lane set"):
            for lane in re.findall(r"[a-z0-9-]+", message.split(":", 1)[1]):
                failures_a.setdefault(lane, []).append(message)
        elif " appears in more than one row" in message:
            m3 = re.search(r"lane ([a-z0-9-]+) appears", message)
            if m3:
                failures_a.setdefault(m3.group(1), []).append(message)

    # rows per lane, for the duplicate and single-row rules
    for cells in rows:
        if cells:
            per_lane_rows.setdefault(base.normalize_lane(cells[0]), []).append(cells)

    ok = {}
    detail = {}
    for lane, fz in sorted(freeze.items()):
        status = {}
        why = []
        cells_list = per_lane_rows.get(lane, [])
        # a
        a_ok = (len(cells_list) == 1 and lane not in failures_a
                and len(cells_list[0]) >= 9)
        if len(cells_list) != 1:
            why.append("a: %d rows" % len(cells_list))
        elif lane in failures_a:
            why.append("a: " + failures_a[lane][0][:110])
        status["a"] = a_ok
        row = cells_list[0] if cells_list else None
        commit = (row[2].strip().lower() if row and len(row) > 2 else "")
        classification = (row[4].strip().lower() if row and len(row) > 4 else "")
        # b
        b_ok = commit == fz["head40"]
        if not b_ok:
            why.append("b: commit %s != freeze head %s" % (commit[:12], fz["head40"][:12]))
        rc, _out, _err = git(fleet / (lane + LANE_SUFFIX), "merge-base",
                             "--is-ancestor", commit, "refs/heads/" + fz["branch"])
        if b_ok and rc != 0:
            b_ok = False
            why.append("b: commit is not an ancestor of refs/heads/%s" % fz["branch"])
        status["b"] = b_ok
        # c
        pin = json.loads((HERE / "lanes.json").read_text(encoding="utf-8"))[lane]["pin"]
        want = delta_for(lane, pin, fz["head40"], fleet)
        have = row[9].strip() if row and len(row) >= 10 else None
        c_ok = have is not None and " ".join(have.split()) == want
        if not c_ok:
            why.append("c: delta cell %r != recomputed %r" % (have, want))
        status["c"] = c_ok
        # d
        prow = entry_province.get(lane)
        d_ok = (prow is not None and prow["classification"] == classification
                and prow["commit"] == commit)
        if not d_ok:
            why.append("d: PROVINCE row %r vs entry %s/%s"
                       % (prow, classification, commit[:12]))
        status["d"] = d_ok
        # e -- the plan's literal wording: the whole word `kotoba` anywhere in
        # the pinned SKILL.md or PROVINCE.md of a `none` row.
        repo = fleet / (lane + LANE_SUFFIX)
        e_ok = True
        if classification == "none":
            hits = [p for p in ("SKILL.md", "PROVINCE.md")
                    if names_kotoba(repo, commit, p)]
            if hits:
                e_ok = False
                why.append("e: none row but %s names kotoba" % ",".join(hits))
        status["e"] = e_ok
        ok[lane] = all(status.values())
        detail[lane] = {"status": status, "why": why}

    total = sum(1 for v in ok.values() if v)
    if args.json:
        print(json.dumps({"world": world.name, "of": len(freeze), "pass": total,
                          "lanes": detail, "notes": notes}, indent=1))
    else:
        print("# world:", world.name)
        for lane in sorted(detail):
            s = detail[lane]["status"]
            flags = " ".join("%s:%d" % (k, s[k]) for k in "abcde")
            print("%-13s %s %s" % (lane, flags,
                                   "" if ok[lane] else "| " + "; ".join(detail[lane]["why"])[:150]))
        for note in notes:
            print("# note:", note)
        print("sibling rows re-pinned and re-read %d of %d" % (total, len(freeze)))
    return 0 if total == len(freeze) else 1


if __name__ == "__main__":
    sys.exit(main())
