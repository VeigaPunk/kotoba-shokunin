#!/usr/bin/env python3
r"""check_routed_repairs.py -- frozen counter for the round-61 C2 (calibration) claim.

Round 61, claim C2 (axis: calibration): the round-60 non-author closure
(`corpus/lessons/round-60-verifier-spotcheck.md` §7-§8) routed six
record-keeping defects — (a) a report count overstated against committed
bytes, (b) two lane files missing from the report's landed scope, (c) a base
measurement cited under the wrong filename, (d) no standalone census-after
file, (e) the word "byte-exact" overstating documented quote shaping, (f) the
M90 control gap (controls must complete before data seats).  This counter
counts how many of the six routed repairs are landed at the measured revision.

This counter is frozen at the round-61 plan commit.  The six repair patterns
below are pinned here and never read from the revision measured.  A later
change is a second measurement, never the declared one (corpus/QUALITY.md Q28).

Universe: six repairs, R-a .. R-f, one counting command each over blobs of the
measured revision (`git show <rev>:<path>`):

  R-a  LOG.md holds the corrected round-60 build-report count on one line:
       the substrings `build reports`, `claimed 32`, `committed 29`, and the
       counting path `.ufo/waves/round-60/build`.
  R-b  LOG.md names both routed files: `plans/round-60.md` and
       `considerthese/2026-10-23.md`.
  R-c  LOG.md holds one line containing both `receipts/freeze2-selftest.txt`
       and `C1-measure.txt` (the r60 base-measurement pointer disambiguation).
  R-d  `.ufo/waves/round-61/census-after.txt` exists and its last non-empty
       line is `exit=0`.
  R-e  `corpus/QUALITY.md` contains `Q56` and `byte-exact`, and
       `corpus/lessons/round-61.md` exists and contains `M91`.
  R-f  `.ufo/waves/round-61/receipts/controls-ancestry.txt` exists and
       contains `merge-base --is-ancestor` and `exit 0`.

Output: `routed repairs verified K of 6`.  Exit 0 iff K == 6, 1 otherwise,
2 = could not evaluate.  The counter reads committed blobs only; it does not
judge whether a repair text is substantively honest — reviewers remain
responsible for that (Q31).

Usage:
  python3 -B verifiers/check_routed_repairs.py [--rev <rev>]
  python3 -B verifiers/check_routed_repairs.py --self-test
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent


def git_show(rev: str, path: str) -> str | None:
    p = subprocess.run(
        ["git", "-C", str(LANE), "show", f"{rev}:{path}"],
        capture_output=True,
    )
    if p.returncode != 0:
        return None
    return p.stdout.decode("utf-8", "replace")


def check_repairs(blobs: dict[str, str | None]) -> tuple[int, list[str]]:
    """Score the six repairs over a path->blob map (None = absent)."""
    why: list[str] = []
    log = blobs.get("LOG.md") or ""
    quality = blobs.get("corpus/QUALITY.md") or ""

    ra = (
        "build reports" in log
        and "claimed 32" in log
        and "committed 29" in log
        and ".ufo/waves/round-60/build" in log
    )
    why.append(f"R-a count correction: {'ok' if ra else 'missing'}")

    rb = "plans/round-60.md" in log and "considerthese/2026-10-23.md" in log
    why.append(f"R-b landed-scope names: {'ok' if rb else 'missing'}")

    rc = any(
        "receipts/freeze2-selftest.txt" in line and "C1-measure.txt" in line
        for line in log.splitlines()
    )
    why.append(f"R-c base-measure pointer: {'ok' if rc else 'missing'}")

    census = blobs.get(".ufo/waves/round-61/census-after.txt")
    rd = (
        census is not None
        and [ln for ln in census.splitlines() if ln.strip()][-1].strip() == "exit=0"
        if census is not None
        else False
    )
    why.append(f"R-d census-after file: {'ok' if rd else 'missing'}")

    lesson = blobs.get("corpus/lessons/round-61.md")
    re_ = (
        "Q56" in quality
        and "byte-exact" in quality
        and lesson is not None
        and "M91" in lesson
    )
    why.append(f"R-e byte-exact criterion + M91: {'ok' if re_ else 'missing'}")

    ancestry = blobs.get(".ufo/waves/round-61/receipts/controls-ancestry.txt")
    rf = (
        ancestry is not None
        and "merge-base --is-ancestor" in ancestry
        and "exit 0" in ancestry
    )
    why.append(f"R-f controls-ancestry receipt: {'ok' if rf else 'missing'}")

    return sum([ra, rb, rc, rd, re_, rf]), why


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rev", default=None, help="revision to measure (default: lane branch tip)")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    rev = args.rev
    if rev is None:
        p = subprocess.run(
            ["git", "-C", str(LANE), "rev-parse", "--verify", "master"],
            capture_output=True,
        )
        if p.returncode != 0:
            print("routed repairs verified could-not-evaluate: no rev", file=sys.stderr)
            return 2
        rev = p.stdout.decode().strip()

    paths = [
        "LOG.md",
        "corpus/QUALITY.md",
        "corpus/lessons/round-61.md",
        ".ufo/waves/round-61/census-after.txt",
        ".ufo/waves/round-61/receipts/controls-ancestry.txt",
    ]
    blobs = {p: git_show(rev, p) for p in paths}
    if blobs["LOG.md"] is None or blobs["corpus/QUALITY.md"] is None:
        print("routed repairs verified could-not-evaluate: unreadable rev", file=sys.stderr)
        return 2

    k, why = check_repairs(blobs)
    for w in why:
        print(w)
    print(f"routed repairs verified {k} of 6")
    return 0 if k == 6 else 1


def self_test() -> int:
    """Fixture arms: each repair absent -> count drops; base world -> 0 of 6."""
    failures = 0

    def expect(name: str, blobs: dict[str, str | None], want: int) -> None:
        nonlocal failures
        got, _ = check_repairs(blobs)
        status = "ok" if got == want else "FAIL"
        if got != want:
            failures += 1
        print(f"self-test {name}: {got} of 6 (want {want}) {status}")

    full_log = (
        "round-60 build reports claimed 32 committed 29 "
        "(`ls .ufo/waves/round-60/build | wc -l`)\n"
        "landed scope names plans/round-60.md and considerthese/2026-10-23.md\n"
        "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
    )
    quality = "Q56: byte-exact reserved for literal equality"
    lesson = "## Mistakes\nM91: overstatement class\n"
    census_after = "kotoba ok\nexit=0\n"
    ancestry = "$ git merge-base --is-ancestor $CTL $DATA\nexit 0\n"

    world: dict[str, str | None] = {
        "LOG.md": full_log,
        "corpus/QUALITY.md": quality,
        "corpus/lessons/round-61.md": lesson,
        ".ufo/waves/round-61/census-after.txt": census_after,
        ".ufo/waves/round-61/receipts/controls-ancestry.txt": ancestry,
    }
    expect("all-repairs", world, 6)
    expect("base-world", {k: None for k in world}, 0)
    expect("no-log", {**world, "LOG.md": None}, 3)
    expect("no-quality", {**world, "corpus/QUALITY.md": None}, 5)

    for key, damaged in [
        ("corpus/lessons/round-61.md", "empty\n"),
        (".ufo/waves/round-61/census-after.txt", "exit=1\n"),
        (".ufo/waves/round-61/receipts/controls-ancestry.txt", "no proof\n"),
    ]:
        expect(f"without-{Path(key).name}", {**world, key: damaged}, 5)

    log_without_ra_cmd = (
        "round-60 build reports claimed 32 committed 29\n"
        "landed scope names plans/round-60.md and considerthese/2026-10-23.md\n"
        "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
    )
    expect("ra-without-command", {**world, "LOG.md": log_without_ra_cmd}, 5)

    log_without_rb = (
        "round-60 build reports claimed 32 committed 29 "
        "(`ls .ufo/waves/round-60/build | wc -l`)\n"
        "erratum: base measurement is receipts/freeze2-selftest.txt not C1-measure.txt\n"
    )
    expect("rb-missing", {**world, "LOG.md": log_without_rb}, 5)

    print(f"self-test: {failures} failure(s)")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
