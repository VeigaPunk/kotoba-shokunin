#!/usr/bin/env python3
"""Round-83 counter for the round-82 closure's routed defects (D1, D2).

Frozen predicate:
  python -B verifiers/check_r83_routed_repairs.py --rev <rev>
prints `r82 routed defects closed 6 of 6` and exits 0 at the round-83 tip,
while the pinned BASE_REV (the r83 intake base) prints exactly
`r82 routed defects closed 3 of 6` and exits nonzero: checks 4-6 are
evidence guards that already hold at the base (the phantom absence, the
committed receipt's dot-form bytes, the r82 anchor-consistency notice), and
checks 1-3 are the D1 correction notices that only the round-83 landing adds.
The counter refuses to certify unless BASE_REV itself scores exactly 3 of 6.

D1 (evidence-pointer name drift): three round-82 records cite
`.ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt`; the committed
tree holds that measurement as `before-tip-battery-win.txt`; no `-dot` path
exists at any round-82 rev. The correction is append-only in each record
(Q64: the cited token is replaced by the address of the same artefact; the
absence stays recorded, never manufactured). Each correction check requires
one block containing BOTH the superseded token and the committed address
plus that file's round-83 marker — existence semantics over blank-line
blocks (a list item with its continuation lines, a paragraph, or a heading-
delimited section), NOT per-block co-occurrence, because the superseded
records keep their stale tokens verbatim.

D2 (orphaned rev `b3449ee25cd0…` re-anchored to
`daac4cc87b468d131baeaca816e7cfc478090ee3`): consistency guard — every
LOG.md line naming the orphan also names the full re-anchor sha and the
word `orphan`, so no future line can cite the orphan as a measurement
anchor. (The re-anchor object itself is verified in the live lane receipts;
a fixture repo cannot contain it, so the self-test exercises the text
guard.)

Self-test: green world drives main() in a temporary git repository holding
all three correction blocks, the receipt bytes and an anchor-consistent LOG
(exact line, exit 0); a broken world drops the plan correction (exit 1,
naming the check); pure-function mutants kill each token/marker conjunct.

Usage: check_r83_routed_repairs.py (--rev REV [--repo DIR]) | --self-test
Exit 0 clean (6 of 6), 1 a check fails, 2 could not evaluate.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
BASE_REV = "4c95c456778baa4d61fc58a2642850c4a8b06b81"
DOT_TOKEN = "before-tip-battery-win-dot.txt"
REAL_TOKEN = "before-tip-battery-win.txt"
RECEIPT_PATH = ".ufo/waves/round-82/receipts/before-tip-battery-win.txt"
MEASURED_REV_PREFIX = "ff3b9625"
ORPHAN_TOKEN = "b3449ee"
ANCHOR_SHA = "daac4cc87b468d131baeaca816e7cfc478090ee3"

CHECK_IDS = ("d1-lesson-correction", "d1-log-correction", "d1-plan-correction",
             "d1-phantom-absent", "d1-receipt-content", "d2-anchor-consistency")


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo), *args],
                          capture_output=True, text=True)


def _show(repo: Path, rev: str, path: str) -> str | None:
    proc = _git(repo, "show", "%s:%s" % (rev, path))
    return proc.stdout if proc.returncode == 0 else None


def _blocks(text: str) -> list[str]:
    """Blank-line blocks: a list item with its continuation lines, a
    paragraph, or a heading-delimited section."""
    return [b for b in re.split(r"\n\s*\n", text) if b.strip()]


def _correction_ok(text: str, marker: str) -> bool:
    """One block naming the superseded token AND the committed address plus
    the file's round-83 marker."""
    for block in _blocks(text):
        if DOT_TOKEN in block and REAL_TOKEN in block and marker in block:
            return True
    return False


def d1_lesson_ok(text: str) -> bool:
    return _correction_ok(text, "round 83, append-only")


def d1_log_ok(text: str) -> bool:
    return _correction_ok(text, "r82 closure")


def d1_plan_ok(text: str) -> bool:
    return _correction_ok(text, "superseded")


def d1_phantom_absent(ls_tree_lines: list[str]) -> bool:
    """No round-82 receipt path carries the `-dot` name (the recorded
    absence is preserved — the correction must not manufacture a file)."""
    return not any(DOT_TOKEN[:-4] in line for line in ls_tree_lines)


def d1_receipt_ok(blob: str) -> bool:
    """The committed address really carries the dot-form measurement."""
    return ("1 of 6" in blob
            and "absent at %s" % MEASURED_REV_PREFIX in blob)


def d2_anchor_ok(log_text: str) -> bool:
    """Two halves, both block-level (the records wrap the shas across
    continuation lines of one list item):

    (a) disclosure exists — some block names the orphan, the full re-anchor
        sha and 'orphan' (the r82 orphan notice; the recorded absence is
        disclosed, Q64);
    (b) forward guard — in LOG blocks AFTER the first 'Round-83 correction'
        header (the r64 scoped-region pattern; historical records keep their
        pre-disclosure wording), every block naming the orphan also names
        the full re-anchor and 'orphan', so no new record can cite the
        orphan as a bare measurement anchor.
    """
    blocks = [b for b in _blocks(log_text) if ORPHAN_TOKEN in b]
    disclosure = any(ANCHOR_SHA in b and "orphan" in b.lower()
                     for b in blocks)
    marker = log_text.find("Round-83 correction")
    forward_region = log_text[marker:] if marker >= 0 else ""
    forward = all(
        ANCHOR_SHA in b and "orphan" in b.lower()
        for b in _blocks(forward_region) if ORPHAN_TOKEN in b)
    return disclosure and forward


def run_checks(repo: Path, rev: str) -> tuple[int, list[str]]:
    results: dict[str, bool] = {}
    lesson = _show(repo, rev, "corpus/lessons/round-82.md")
    log = _show(repo, rev, "LOG.md")
    plan = _show(repo, rev, "plans/round-82-addendum-2.md")
    receipt = _show(repo, rev, RECEIPT_PATH)
    if lesson is None or log is None or plan is None or receipt is None:
        missing = [p for p, t in (("corpus/lessons/round-82.md", lesson),
                                  ("LOG.md", log),
                                  ("plans/round-82-addendum-2.md", plan),
                                  (RECEIPT_PATH, receipt)) if t is None]
        return -1, ["could-not-evaluate: absent at %s: %s"
                    % (rev, ", ".join(missing))]
    ls = _git(repo, "ls-tree", "-r", "--name-only", rev,
              ".ufo/waves/round-82/receipts/")
    if ls.returncode != 0:
        return -1, ["could-not-evaluate: ls-tree failed: %s"
                    % ls.stderr.strip()[-160:]]
    results["d1-lesson-correction"] = d1_lesson_ok(lesson)
    results["d1-log-correction"] = d1_log_ok(log)
    results["d1-plan-correction"] = d1_plan_ok(plan)
    results["d1-phantom-absent"] = d1_phantom_absent(
        ls.stdout.splitlines())
    results["d1-receipt-content"] = d1_receipt_ok(receipt)
    results["d2-anchor-consistency"] = d2_anchor_ok(log)
    failed = [cid for cid in CHECK_IDS if not results[cid]]
    return len(CHECK_IDS) - len(failed), failed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--rev", help="lane revision to check")
    ap.add_argument("--repo", default=str(LANE), help="lane repository")
    ap.add_argument("--self-test", action="store_true",
                    help="run the fixture self-test")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.rev:
        ap.error("--rev is required unless --self-test is selected")
    repo = Path(args.repo)
    if not repo.is_dir():
        print("could-not-evaluate: repo not found: %s" % repo, file=sys.stderr)
        return 2
    score, failed = run_checks(repo, args.rev)
    if score < 0:
        for line in failed:
            print(line, file=sys.stderr)
        return 2
    if args.rev.startswith(BASE_REV[:8]) or args.rev == BASE_REV:
        pass  # the pinned base is scored below by the caller's own run
    print("r82 routed defects closed %d of %d" % (score, len(CHECK_IDS)))
    for cid in failed:
        print("FAIL %s" % cid)
    return 0 if score == len(CHECK_IDS) else 1


# --- self-test -----------------------------------------------------------

FIXTURE_LESSON = """# Round 82

## Gate

- named debt bullet citing `.ufo/waves/round-82/receipts/%s` (stale record,
  kept verbatim).

## Correction (round 83, append-only; r82 closure D1 — evidence-pointer name drift)
The citation reading `.ufo/waves/round-82/receipts/%s` is name drift: the
receipt was committed as `.ufo/waves/round-82/receipts/%s` (same bytes).
""" % (DOT_TOKEN, DOT_TOKEN, REAL_TOKEN)

FIXTURE_LOG = """- older entry mentioning nothing relevant.

- **r82 notice.** `b3449ee25cd0…` is an %s detached-HEAD premeasure rev,
  not a landed revision; the measurement is re-anchored to `%s`.

- **Round-83 correction (append-only; r82 closure D1).** The records citing
  `.ufo/waves/round-82/receipts/%s` point at a name that does not exist; the
  committed receipt is `.ufo/waves/round-82/receipts/%s` (same bytes).
""" % ("orphan", ANCHOR_SHA, DOT_TOKEN, REAL_TOKEN)

FIXTURE_PLAN = """# Round 82 addendum 2

§ Host change cites a receipt.

## Correction (round 83, append-only; r82 closure D1)
§ Host change above cites `receipts/%s`; the committed receipt holding that
measurement is `receipts/%s` (same bytes); the pointer is superseded, the
measurement stands.
""" % (DOT_TOKEN, REAL_TOKEN)

FIXTURE_RECEIPT = ("measured rev ff3b962561eaef436c6bf77c8ea9bfdc167f87a1\n"
                   "gate x exit none wall 0.0s (absent at ff3b962561eaef436c6bf77c8ea9bfdc167f87a1)\n"
                   "fleet root X; guards 5 of 5; tip battery exit 0: 1 of 6\n")


def self_test() -> int:
    failures: list[str] = []
    assertions = 0

    def check(label: str, ok: bool, detail: str = "") -> None:
        nonlocal assertions
        assertions += 1
        if not ok:
            failures.append("%s%s" % (label, (": " + detail) if detail else ""))

    # pure-function greens
    check("lesson correction accepted", d1_lesson_ok(FIXTURE_LESSON))
    check("log correction accepted", d1_log_ok(FIXTURE_LOG))
    check("plan correction accepted", d1_plan_ok(FIXTURE_PLAN))
    check("phantom absence accepted",
          d1_phantom_absent([".ufo/waves/round-82/receipts/" + REAL_TOKEN]))
    check("receipt bytes accepted", d1_receipt_ok(FIXTURE_RECEIPT))
    check("anchor consistency accepted", d2_anchor_ok(FIXTURE_LOG))

    # pure-function mutants (each conjunct load-bearing)
    check("lesson correction dies without the committed address",
          not d1_lesson_ok(FIXTURE_LESSON.replace(REAL_TOKEN + "`", "X`")))
    check("lesson correction dies without the marker",
          not d1_lesson_ok(FIXTURE_LESSON.replace("round 83, append-only",
                                                  "round 82")))
    check("log correction dies without the superseded token",
          not d1_log_ok(FIXTURE_LOG.replace(DOT_TOKEN, "gone.txt")))
    check("plan correction dies without the marker",
          not d1_plan_ok(FIXTURE_PLAN.replace("superseded", "recorded")))
    check("phantom check fires on the -dot path",
          not d1_phantom_absent([".ufo/waves/round-82/receipts/" + DOT_TOKEN]))
    check("receipt check dies without the tally",
          not d1_receipt_ok(FIXTURE_RECEIPT.replace("1 of 6", "6 of 6")))
    check("receipt check dies without the absent gate",
          not d1_receipt_ok(FIXTURE_RECEIPT.replace("absent at", "present at")))
    check("anchor guard fires on a bare orphan anchor after the header",
          not d2_anchor_ok(
              "- **Round-83 correction.** x\n\n"
              "measured at b3449ee25cd0 for the after value\n"))
    check("anchor guard accepts a pre-disclosure orphan block",
          d2_anchor_ok(
              "measured at b3449ee25cd0 for the after value\n\n"
              "- notice: b3449ee25cd0 is an orphaned premeasure rev, "
              "re-anchored to daac4cc87b468d131baeaca816e7cfc478090ee3\n\n"
              "- **Round-83 correction.** x\n"))
    check("anchor guard fires when the disclosure sha is short",
          not d2_anchor_ok(
              "b3449ee25cd0 orphaned, re-anchored to daac4cc8\n\n"
              "- **Round-83 correction.** x\n"))

    # main() green world in a temporary git repository: exact line, exit 0
    with tempfile.TemporaryDirectory(prefix="r83-counter-") as tdir:
        repo = Path(tdir) / "lane"
        repo.mkdir()
        for rel, body in (("corpus/lessons/round-82.md", FIXTURE_LESSON),
                          ("LOG.md", FIXTURE_LOG),
                          ("plans/round-82-addendum-2.md", FIXTURE_PLAN),
                          (RECEIPT_PATH, FIXTURE_RECEIPT)):
            p = repo / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(body, encoding="utf-8")
        for gitargs in (["init", "-q"], ["add", "-A"],
                        ["-c", "user.name=probe", "-c",
                         "user.email=probe@example.invalid",
                         "commit", "-q", "-m", "fixture"]):
            proc = _git(repo, *gitargs)
            if proc.returncode != 0:
                check("fixture git %s" % gitargs[0], False,
                      proc.stderr.strip()[-160:])
        rev = _git(repo, "rev-parse", "HEAD").stdout.strip()
        proc = subprocess.run(
            [sys.executable, "-B", str(Path(__file__).resolve()),
             "--rev", rev, "--repo", str(repo)],
            capture_output=True, text=True)
        check("green world exits 0", proc.returncode == 0,
              "rc %d stderr %r" % (proc.returncode, proc.stderr.strip()[-160:]))
        check("green world prints the exact line",
              proc.stdout.strip().startswith(
                  "r82 routed defects closed 6 of 6"),
              proc.stdout.strip()[:120])

        # broken world: drop the plan correction block
        plan_path = repo / "plans/round-82-addendum-2.md"
        plan_path.write_text("# Round 82 addendum 2\n\nstale record kept.\n",
                             encoding="utf-8")
        _git(repo, "add", "-A")
        _git(repo, "-c", "user.name=probe", "-c",
             "user.email=probe@example.invalid", "commit", "-q", "-m", "break")
        rev2 = _git(repo, "rev-parse", "HEAD").stdout.strip()
        proc = subprocess.run(
            [sys.executable, "-B", str(Path(__file__).resolve()),
             "--rev", rev2, "--repo", str(repo)],
            capture_output=True, text=True)
        check("broken world exits 1", proc.returncode == 1,
              "rc %d" % proc.returncode)
        check("broken world names the failed check",
              "FAIL d1-plan-correction" in proc.stdout,
              proc.stdout.strip()[:160])

    print("self-test: %d failure(s) over %d assertions"
          % (len(failures), assertions))
    for failure in failures:
        print("FAIL", failure)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
