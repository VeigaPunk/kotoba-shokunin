#!/usr/bin/env python3
"""check-filled.py — re-check every filled line of the assembled round-80 freeze receipt.

Each line is checked against primary bytes, never against a report:

  part 0   sha256 of `git show <BASE>:<path>`   (the pre-state at the round-80 base)
  part 1   sha256 of the measured bytes          (`--rev` reads `<rev>:<path>`, else the worktree)
  part 1b  git blob id                            (`git rev-parse <rev>:<path>`; 40 hex, not sha256)
  part 2   sha256 of the measured bytes          (same rule as part 1)
  part 3   sha256 of the published patch file    (worktree: .ufo/waves/round-80/build/...)
  part 4   sha256 of the r79 draft named         (worktree)

`{{MARKER}}` lines are skipped: they are pending seat outputs. A file that does not exist yet is
reported, not guessed. Tip-side parts (1, 1b, 2) describe bytes that are not in the tree until the
freeze commit: with `--rev` they are read from that revision, without it they are reported as
*deferred* (never silently skipped, never counted as a pass). Exit 0 iff every line that could be
checked verifies.

Usage:
  python3 -B .ufo/waves/round-80/build/Kb80S15FreezeShas-checkfilled.py [--rev <rev>]

Run it with no --rev at the base (parts 1-3 are pending there and skip), then again with
`--rev <F2>` at the freeze commit, where every line must verify: that second run is the freeze
self-check the L1 commits before any after-value is measured.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
BASE = "398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93"
# The counter's own pinned base: the instrument-size guard diffs from THIS, never from BASE (C-b).
PINNED_BASE = "072048fa8e8a52c707d25f7079772fa317244eb7"
RECEIPT = f"{LANE}/.ufo/waves/round-80/build/Kb80S15FreezeShas.md"


REPO = LANE  # overridable with --repo (git reads only; part-3/4 paths stay workspace-relative)


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, check=True).stdout


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rev", default=None, help="read parts 1/1b/2 from <rev> instead of the worktree")
    ap.add_argument("--repo", default=LANE,
                    help="repository the git reads use (default the lane); part-3/4 paths stay in the lane")
    ap.add_argument("--expect-numstat", default=None,
                    help="comma list <basename>=<added>/<deleted>, e.g. "
                         "check_assertion_floors.py=22/3,verify_corpus_independent.py=10/3,"
                         "verify_corpus_integrity.py=28/2 ; needs --rev ; asserts no instrument took a "
                         "line past the published hunks")
    args = ap.parse_args()
    global REPO
    REPO = args.repo

    text = open(RECEIPT, encoding="utf-8").read()
    block = re.search(r"## 1\..*?```\n(.*?)```", text, re.S).group(1)

    part = None
    checked = skipped = deferred = failed = 0
    for line in block.splitlines():
        if line.startswith("# part 1b"):
            part = "1b"
            continue
        if line.startswith("# part "):
            part = line.split()[2]
            continue
        if line.startswith("#"):
            continue  # note/annotation lines do not close a part; only a new "# part N" header does
        if not line.strip():
            continue
        if line.startswith("base="):
            if line != f"base={BASE}":
                print(f"MISMATCH base= line: {line}")
                failed += 1
            continue
        if "{{" in line:
            skipped += 1
            continue

        want, path = line.split("  ", 1)
        try:
            if part == "0":
                got = sha256(git("show", f"{BASE}:{path}"))
            elif part in ("1", "1b", "2") and not args.rev:
                deferred += 1
                print(f"DEFERRED {path}: tip-side line, needs --rev <F2> or the landed tree")
                continue
            elif part == "1b":
                rev = args.rev or "HEAD"
                got = git("rev-parse", f"{rev}:{path}").decode().strip()
            elif part in ("1", "2") and args.rev:
                got = sha256(git("show", f"{args.rev}:{path}"))
            else:
                got = sha256(open(f"{LANE}/{path}", "rb").read())
        except (subprocess.CalledProcessError, FileNotFoundError) as exc:
            print(f"MISSING {path}: {exc}")
            failed += 1
            continue

        checked += 1
        if got != want:
            failed += 1
            print(f"MISMATCH {path}: receipt {want} observed {got}")

    if args.expect_numstat:
        if not args.rev:
            print("NUMSTAT skipped: --expect-numstat needs --rev")
        else:
            six = ["verifiers/check_gate_registry.py", "verifiers/check_assertion_floors.py",
                   "verifiers/verify_skill_checklist.py", "verifiers/verify_corpus_integrity.py",
                   "verifiers/verify_corpus_independent.py", "verifiers/check_correction_sweep.py"]
            raw = git("diff", "--numstat", PINNED_BASE, args.rev, "--", *six).decode()
            got = {}
            for row in raw.splitlines():
                added, deleted, path = row.split("\t")
                got[path.split("/")[-1]] = (int(added), int(deleted))
            want = {}
            for item in args.expect_numstat.split(","):
                name, pair = item.split("=")
                a, d = pair.split("/")
                want[name] = (int(a), int(d))
            for name in sorted(want):
                if got.get(name) != want[name]:
                    failed += 1
                    print(f"NUMSTAT MISMATCH {name}: expected {want[name][0]}/{want[name][1]}, "
                          f"measured {got.get(name)}")
            total = (sum(a for a, _ in got.values()), sum(d for _, d in got.values()))
            print(f"six-instrument numstat {total[0]} added / {total[1]} deleted (cap 60)")
            if total[0] > 60 or total[1] > 60:
                failed += 1
                print("NUMSTAT FAIL: an instrument gained or lost more than LINE_CAP lines")

    print(f"checked {checked} line(s), deferred {deferred} tip-side, skipped {skipped} pending, "
          f"{failed} failure(s)")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
