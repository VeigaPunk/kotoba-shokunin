#!/usr/bin/env python3
r"""check_correction_sweep.py -- the round-52 fix for lesson M36 (shown able to fail).

Round 51's corrections sweep missed two places that still stated a superseded
claim without the declared result (round-51 spot-check, routed defects 1-2):
`corpus/README.md` (the round-51 Core note: `overlap levers backed 7 of 7
clients`) and the `SCORECARD.md` depth cell (lead `7 of 7`, exit 0 @
`34cfffbb`).  This check sweeps the registry below.

Rule per registry entry: every Markdown block of FILE that contains the STALE
pattern must also contain the DECLARED pattern; with `lead: true` the DECLARED
pattern must occur BEFORE the first STALE match in that block (a headline leads
with the declared result).  A block is a list item with its indented
continuation lines, a paragraph, or one table row.

Usage: check_correction_sweep.py (--rev REV | --root DIR) | --self-test
Exit 0 clean, 1 a block violates an entry, 2 could not evaluate.
A new superseded claim is added as a new registry row; rows are not edited.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
REGISTRY = (
    {"id": "r51-c2-readme", "file": "corpus/README.md",
     "stale": r"overlap levers backed 7 of 7 clients", "declared": r"4 of 7", "lead": False},
    {"id": "r51-c2-scorecard-lead", "file": "SCORECARD.md",
     "stale": r"`7 of 7`, exit 0 @ `34cfffbb`", "declared": r"4 of 7", "lead": True},
    {"id": "r51-c2-province", "file": "PROVINCE.md",
     "stale": r"overlap levers backed 7 of 7 clients", "declared": r"4 of 7", "lead": False},
    # round 52 attempt 2 (M38, Q29/Q30): opencode and Copilot CLI were recorded
    # as silent on MCP server instructions; S041 and S042 document both.
    {"id": "r52-c2-skill-silent", "file": "SKILL.md",
     "stale": r"say nothing about server instructions", "declared": r"S041", "lead": False},
    {"id": "r52-c2-province-five", "file": "PROVINCE.md",
     "stale": r"specification and five pinned clients", "declared": r"S041", "lead": False},
    {"id": "r52-c2-readme-five", "file": "corpus/README.md",
     "stale": r"five client pages \(S032 spec", "declared": r"S041", "lead": False},
)


def blocks(text: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    cur: list[str] = []
    start = 0
    for i, ln in enumerate(text.splitlines(), 1):
        new_item = bool(re.match(r"^(?:[-*] |\d+\. |\|)", ln)) or ln.startswith("#")
        if not ln.strip() or new_item:
            if cur:
                out.append((start, "\n".join(cur)))
            cur = [] if not ln.strip() else [ln]
            start = i
            if ln.startswith("|") or ln.startswith("#"):
                out.append((i, ln))
                cur = []
            continue
        if not cur:
            start = i
        cur.append(ln)
    if cur:
        out.append((start, "\n".join(cur)))
    return out


def sweep(read) -> list[str]:
    bad = []
    for e in REGISTRY:
        text = read(e["file"])
        if text is None:
            raise RuntimeError("missing %s" % e["file"])
        for line, b in blocks(text):
            m = re.search(e["stale"], b)
            if not m:
                continue
            d = re.search(e["declared"], b)
            if not d or (e["lead"] and d.start() > m.start()):
                bad.append("%s %s:%d stale claim without the declared result%s" % (
                    e["id"], e["file"], line, " leading" if e["lead"] else ""))
    return bad


def reader(rev: str | None, root: str | None):
    def read(path: str):
        if rev:
            r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (rev, path)],
                               capture_output=True)
            return r.stdout.decode("utf-8") if r.returncode == 0 else None
        p = Path(root) / path
        return p.read_text(encoding="utf-8") if p.is_file() else None
    return read


def self_test() -> int:
    fails, n = [], 0

    def case(name, readme, score, want, province="- nothing stale\n",
             skill="- nothing stale\n"):
        nonlocal n
        n += 1
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "corpus").mkdir()
            (Path(t) / "corpus/README.md").write_text(readme)
            (Path(t) / "SCORECARD.md").write_text(score)
            (Path(t) / "PROVINCE.md").write_text(province)
            (Path(t) / "SKILL.md").write_text(skill)
            got = sweep(reader(None, t))
        ids = sorted(x.split()[0] for x in got)
        if ids != sorted(want):
            fails.append("%s: got %r" % (name, got))

    stale_r = "- note: `overlap levers backed 7 of 7 clients`.\n  more text\n"
    fixed_r = stale_r + "  Correction: declared result 4 of 7.\n"
    later_r = stale_r + "\n- next item: 4 of 7 elsewhere\n"
    stale_s = "| depth | 9 | `0 of 7` -> `7 of 7`, exit 0 @ `34cfffbb`; correction 4 of 7 |\n"
    fixed_s = "| depth | 9 | declared 4 of 7; widened `7 of 7`, exit 0 @ `34cfffbb` |\n"
    case("red both", stale_r, stale_s, ["r51-c2-readme", "r51-c2-scorecard-lead"])
    case("green both", fixed_r, fixed_s, [])
    case("correction in another block is not a correction", later_r, fixed_s, ["r51-c2-readme"])
    case("declared after the stale lead fails", fixed_r, stale_s, ["r51-c2-scorecard-lead"])
    case("no stale claim: clean", "- nothing here\n", "| depth | 9 | x |\n", [])
    silent = "| every client | a skill too | the opencode pages say nothing about server instructions |\n"
    case("r52 silent negative without S041 fails", "- x\n", "| d | 9 | x |\n",
         ["r52-c2-skill-silent"], skill=silent)
    case("r52 silent negative with S041 passes", "- x\n", "| d | 9 | x |\n", [],
         skill=silent.replace("|\n", "; corrected by S041 |\n"))
    print("%d failure(s) over %d assertions" % (len(fails), n))
    for f in fails:
        print("FAIL", f)
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--rev")
    g.add_argument("--root")
    g.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    try:
        bad = sweep(reader(a.rev, a.root))
    except RuntimeError as e:
        print("could-not-evaluate: %s" % e, file=sys.stderr)
        return 2
    for b in bad:
        print("FAIL", b)
    print("correction sweep: %d stale block(s)" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
