#!/usr/bin/env python3
r"""check_r63_routed_repairs.py -- round-63 C2 counter (calibration sub-axis).

Round 63, claim C2: the five defects the round-62 non-author spot-check routed
(corpus/lessons/round-62-verifier-spotcheck.md §6) are closed in the round-62
close record, and the closure is COUNTED from committed bytes rather than
asserted.  Frozen at the round-63 plan commit (erratum E1 pre-data): the five
checks below are the declared predicate; a later change is a second
measurement, never the declared one (corpus/QUALITY.md Q28).

Frozen predicate:
  python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>
prints `r62 routed defects closed 5 of 5` and exits 0.

The five checks, each COMPUTED from `git show <rev>:<path>`:

  1 late-write-tracked   `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md` is a
                         tracked blob at <rev> (the spot-check's defect 1).
  2 receipt-rev-named    the `receipt_rev=` token is read out of
                         `.ufo/waves/round-62/C2-successor-measure.txt` at
                         <rev>; LOG.md at <rev> must carry an appended line
                         naming that exact token (defect 2a).
  3 entry-size-named     `wc -l` and `wc -w` of
                         `corpus/knowledge/erratum-absorption-round62.md` at
                         <rev> are computed; one LOG.md line must carry both
                         numbers and the entry path (defect 2b).
  4 append-only          the r62-tip `LOG.md` bytes are a byte-prefix of
                         `LOG.md` at <rev>, AND <rev>'s LOG adds at least one
                         line beyond that prefix (erratum E1: without the
                         second conjunct the check is vacuous at the tip).
  5 noharm-arms-named    the `reg_gate` and `corpus-idx` verdict lines are
                         read from `.ufo/waves/round-62/noharm-tip.txt` at
                         <rev>; LOG.md at <rev> must name both classes and the
                         measured `reg_gate` count (defect 4).

Bounds (declared before data): the counter binds these five named defects and
the two receipts it reads.  A new class of self-assessment mismatch, a claim
that is wrong in a way no receipt records, and a correction that names the
right tokens with wrong prose are outside it.  Checks 2, 3 and 5 are token
linkage: they prove the correction names the measured value, not that every
sentence around it is true.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LANE = Path(__file__).resolve().parent.parent
R62_TIP = "35d44b4b4dcdda234b5dbff7af37e432fec55f05"
LATE = ".ufo/waves/round-62/w2/FalsifyC2HonestH1.md"
C2_RECEIPT = ".ufo/waves/round-62/C2-successor-measure.txt"
ENTRY = "corpus/knowledge/erratum-absorption-round62.md"
LOG = "LOG.md"
NOHARM = ".ufo/waves/round-62/noharm-tip.txt"
REV_RE = re.compile(r"^[0-9a-fA-F]{40}$")
RECEIPT_REV_RE = re.compile(r"receipt_rev=([0-9a-f]{40})")
REG_GATE_RE = re.compile(r"^\s*(?:FAIL|PASS)\s+reg_gate\b.*$", re.MULTILINE)
CORPUS_IDX_RE = re.compile(r"^\s*(?:FAIL|PASS)\s+corpus-idx\b.*$", re.MULTILINE)
REG_COUNT_RE = re.compile(r"(\d+) of (\d+)")


class EnvError(Exception):
    pass


def git(root: Path, args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root)] + list(args),
                          capture_output=True, text=True, timeout=20)


def show(root: Path, rev: str, path: str) -> str | None:
    p = git(root, ["show", "%s:%s" % (rev, path)])
    return p.stdout if p.returncode == 0 else None


def check_late_write(root: Path, rev: str) -> tuple[bool, str]:
    p = git(root, ["ls-tree", "-r", rev, "--", LATE])
    if p.returncode != 0:
        return False, "git ls-tree failed: %s" % (p.stderr.strip()[:120] or "?")
    tracked = bool(p.stdout.strip())
    if tracked:
        size = git(root, ["cat-file", "-s", "%s:%s" % (rev, LATE)])
        if size.returncode != 0 or not size.stdout.strip().isdigit():
            return False, "tracked blob size unreadable at %s" % rev
        if int(size.stdout.strip()) == 0:
            return False, "tracked blob is empty at %s (no evidence)" % rev
    return tracked, ("tracked at %s" % rev if tracked
                     else "not a tracked blob at %s" % rev)


def check_receipt_rev(root: Path, rev: str) -> tuple[bool, str]:
    receipt = show(root, rev, C2_RECEIPT)
    if receipt is None:
        return False, "%s absent at %s" % (C2_RECEIPT, rev)
    found = RECEIPT_REV_RE.findall(receipt)
    if not found:
        return False, "no receipt_rev= token in %s at %s" % (C2_RECEIPT, rev)
    token = found[-1]
    log = show(root, rev, LOG) or ""
    named = [line for line in log.splitlines()
             if token in line and "receipt" in line.lower()]
    return bool(named), ("LOG names %s on %d line(s)" % (token, len(named))
                         if named else "LOG never names %s" % token)


def check_entry_size(root: Path, rev: str) -> tuple[bool, str]:
    entry = show(root, rev, ENTRY)
    if entry is None:
        return False, "%s absent at %s" % (ENTRY, rev)
    lines = len(entry.splitlines())
    words = len(entry.split())
    log = show(root, rev, LOG) or ""
    hits = [line for line in log.splitlines()
            if ENTRY in line and str(lines) in line and str(words) in line]
    return bool(hits), ("LOG states %d lines / %d words on %d line(s)"
                        % (lines, words, len(hits)) if hits
                        else "LOG never states %d lines / %d words for %s"
                        % (lines, words, ENTRY))


def check_append_only(root: Path, rev: str) -> tuple[bool, str]:
    base_log = show(root, R62_TIP, LOG)
    rev_log = show(root, rev, LOG)
    if base_log is None or rev_log is None:
        return False, "LOG.md unreadable at one of the two revisions"
    prefix = rev_log.startswith(base_log)
    grew = len(rev_log.splitlines()) > len(base_log.splitlines())
    return prefix and grew, ("prefix=%s grew_by=%d line(s)"
                             % (prefix, len(rev_log.splitlines())
                                - len(base_log.splitlines())))


def check_noharm(root: Path, rev: str) -> tuple[bool, str]:
    receipt = show(root, rev, NOHARM)
    if receipt is None:
        return False, "%s absent at %s" % (NOHARM, rev)
    reg = REG_GATE_RE.search(receipt)
    idx = CORPUS_IDX_RE.search(receipt)
    if reg is None or idx is None:
        return False, "receipt lacks a reg_gate or corpus-idx verdict line"
    # the `N of M` count sits on the indented detail line that follows the
    # verdict line, so search the block between reg_gate and corpus-idx.
    block = receipt[reg.end():idx.start()] if reg.end() <= idx.start() else receipt[reg.end():]
    counts = REG_COUNT_RE.search(block) or REG_COUNT_RE.search(reg.group(0))
    if counts is None:
        return False, "the reg_gate line carries no `N of M` count"
    count_token = "%s of %s" % (counts.group(1), counts.group(2))
    log = show(root, rev, LOG) or ""
    named = [line for line in log.splitlines()
             if "reg_gate" in line and "corpus-idx" in line
             and count_token in line]
    return bool(named), ("LOG names reg_gate %s + corpus-idx on %d line(s)"
                         % (count_token, len(named)) if named
                         else "LOG does not name reg_gate %s + corpus-idx"
                         % count_token)


CHECKS = (
    ("late-write-tracked", check_late_write),
    ("receipt-rev-named", check_receipt_rev),
    ("entry-size-named", check_entry_size),
    ("append-only", check_append_only),
    ("noharm-arms-named", check_noharm),
)


def run(root: Path, rev: str) -> int:
    closed = 0
    for name, fn in CHECKS:
        ok, detail = fn(root, rev)
        closed += 1 if ok else 0
        print("%-4s %-20s %s" % ("PASS" if ok else "FAIL", name, detail))
    print("r62 routed defects closed %d of %d" % (closed, len(CHECKS)))
    return 0 if closed == len(CHECKS) else 1


# --------------------------------------------------------------------------
# self-test: two constructed trees, both directions
# --------------------------------------------------------------------------

def _write(root: Path, path: str, text: str) -> None:
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def _commit(root: Path, message: str) -> str:
    env = {"GIT_AUTHOR_NAME": "selftest", "GIT_AUTHOR_EMAIL": "s@t",
           "GIT_COMMITTER_NAME": "selftest", "GIT_COMMITTER_EMAIL": "s@t",
           "GIT_AUTHOR_DATE": "2026-10-23T12:00:00+00:00",
           "GIT_COMMITTER_DATE": "2026-10-23T12:00:00+00:00"}
    subprocess.run(["git", "-C", str(root), "add", "-A"], check=True,
                   capture_output=True)
    subprocess.run(["git", "-C", str(root), "commit", "-m", message],
                   check=True, capture_output=True, env={**env})
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                         check=True, capture_output=True, text=True)
    return out.stdout.strip()


def _base_tree(root: Path) -> None:
    _write(root, LOG, "# log\n\n## Round 62\n- original line\n")
    _write(root, C2_RECEIPT, "measured\nreceipt_rev=%s\n" % ("3f911504" + "ce76d9ca"
                                                             + "186f297d6d4a9cd8ed77508a"))
    _write(root, ENTRY, "line one\nline two three four\n")
    _write(root, NOHARM, "--- arms ---\nFAIL  reg_gate    x\n"
                         "        tip: gate registry rows conformant 36 of 38 "
                         "lane verifiers; phantom 0\n"
                         "FAIL  corpus-idx  tip leaves new corpus file(s) "
                         "unindexed: corpus/lessons/x.md\n")


def _repaired(root: Path, log_extra: str) -> None:
    _write(root, LATE, "seat finding\n")
    _write(root, LOG, (root / LOG).read_text() + log_extra)


def self_test() -> int:
    import shutil
    import tempfile

    failures = 0
    assertions = 0

    def check(name: str, actual: object, expected: object) -> None:
        nonlocal assertions, failures
        assertions += 1
        if actual != expected:
            failures += 1
            print("FAIL %s: got %r, expected %r" % (name, actual, expected))

    tmp = Path(tempfile.mkdtemp(prefix="r63-c2-"))
    try:
        base = tmp / "base"
        base.mkdir()
        subprocess.run(["git", "-C", str(base), "init", "-q"], check=True)
        _base_tree(base)
        base_rev = _commit(base, "base")

        # M1 substitution arm: a dirty worktree must not satisfy check 1.
        _write(base, LATE, "untracked worktree copy\n")
        check("worktree: an untracked copy on disk leaves check 1 red",
              check_late_write(base, base_rev)[0], False)
        (base / LATE).unlink()

        # the do-nothing control: the r62 tip itself
        ok, detail = check_late_write(base, base_rev)
        check("base: late write is not tracked", ok, False)
        ok, detail = check_receipt_rev(base, base_rev)
        check("base: the receipt revision is not named", ok, False)
        ok, detail = check_entry_size(base, base_rev)
        check("base: the entry size is not stated", ok, False)
        ok, detail = check_append_only(base, base_rev)
        check("base: append-only fails on the growth conjunct", ok, False)
        ok, detail = check_noharm(base, base_rev)
        check("base: the interim reds are not named", ok, False)
        base_ok = sum(1 for _, fn in CHECKS if fn(base, base_rev)[0])
        check("base: the do-nothing control scores 0 of 5", base_ok, 0)

        # the repaired tree: one appended LOG block naming every measured value
        sizes = "%d lines / %d words" % (
            len((base / ENTRY).read_text().splitlines()),
            len((base / ENTRY).read_text().split()))
        extra = ("\n## Corrections\n"
                 "- C2 receipt revision named: receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a.\n"
                 "- %s, %s.\n" % (ENTRY, sizes) +
                 "- No post-report child commit exists.\n"
                 "- The r62 no-harm receipt's two interim reds: reg_gate 36 of 38 "
                 "and corpus-idx round-61 spot-check; both fixed at tip.\n")
        # the base tree is the r62 tip, so the prefix comparison needs the same
        # base commit; use the base rev as R62_TIP for the repaired tree.
        global R62_TIP
        saved_tip = R62_TIP
        R62_TIP = base_rev
        try:
            _repaired(base, extra)
            repaired_rev = _commit(base, "repaired")
            results = {name: fn(base, repaired_rev)[0] for name, fn in CHECKS}
            check("repaired: all five checks pass", results,
                  {name: True for name, _ in CHECKS})
            check("repaired: the counter scores 5 of 5",
                  sum(1 for v in results.values() if v), 5)

            # label-only shortcut: every token in the LOG, no receipt bytes
            (base / C2_RECEIPT).unlink()
            shortcut_rev = _commit(base, "shortcut")
            ok, detail = check_receipt_rev(base, shortcut_rev)
            check("shortcut: a LOG naming a constant fails without the receipt",
                  ok, False)

            # a rewritten (non-append-only) LOG fails the prefix conjunct
            _write(base, C2_RECEIPT, "measured\nreceipt_rev=%s\n"
                   % ("3f911504" + "ce76d9ca" + "186f297d6d4a9cd8ed77508a"))
            _write(base, LOG, "rewritten\n## Corrections\n"
                   "- receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a\n"
                   "- %s, %s.\n" % (ENTRY, sizes) +
                   "- reg_gate 36 of 38 and corpus-idx named\n")
            rewrite_rev = _commit(base, "rewrite")
            ok, detail = check_append_only(base, rewrite_rev)
            check("rewrite: a rewritten LOG fails the prefix conjunct", ok, False)

            # Each substitution arm below restores a proper append (the base
            # LOG plus one corrections block) and swaps exactly one measured
            # value, so the named check must reject it.  Without these arms a
            # counter that never reads the receipt/entry/receipt-count bytes
            # (MutCalibInstrument M2/M3/M5) would print the same headline.
            base_log = show(base, base_rev, LOG) or ""

            # M3: the entry grows after the correction names its size.
            _write(base, LOG, base_log + extra)
            _write(base, ENTRY, (base / ENTRY).read_text() + "line five\n")
            size_rev = _commit(base, "entry-size-shift")
            check("entry-size: a shifted entry size fails check 3",
                  check_entry_size(base, size_rev)[0], False)

            # M2: a short token is not the receipt's exact token.
            _write(base, LOG, base_log + extra.replace(
                "3f911504ce76d9ca186f297d6d4a9cd8ed77508a", "3f911504"))
            token_rev = _commit(base, "short-token")
            check("receipt-rev: a short token does not satisfy check 2",
                  check_receipt_rev(base, token_rev)[0], False)

            # M5: a substituted count is not the receipt's count.
            _write(base, LOG, base_log + extra.replace("36 of 38", "37 of 38"))
            count_rev = _commit(base, "count-swap")
            check("noharm: a substituted reg_gate count fails check 5",
                  check_noharm(base, count_rev)[0], False)

            # check 1 substance: a zero-byte tracked blob is not evidence.
            _write(base, LOG, base_log + extra)
            _write(base, LATE, "")
            empty_rev = _commit(base, "empty-late-write")
            check("late-write: a zero-byte tracked blob fails check 1",
                  check_late_write(base, empty_rev)[0], False)
        finally:
            R62_TIP = saved_tip

        print("self-test: %d failure(s) over %d assertions"
              % (failures, assertions))
        return 1 if failures else 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="round-63 C2 counter: the r62 spot-check's routed defects")
    ap.add_argument("--rev", help="full 40-hex revision to measure")
    ap.add_argument("--root", default=str(LANE), help="repository root")
    ap.add_argument("--self-test", action="store_true",
                    help="run the constructed-tree controls")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.rev is None or not REV_RE.match(args.rev):
        ap.error("--rev must be a full 40-hex revision (or use --self-test)")
    root = Path(args.root).resolve()
    if not (root / ".git").exists():
        print("error: %s is not a git checkout" % root, file=sys.stderr)
        return 2
    try:
        return run(root, args.rev.lower())
    except (subprocess.SubprocessError, OSError) as exc:
        print("error: could not evaluate: %s" % exc, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
