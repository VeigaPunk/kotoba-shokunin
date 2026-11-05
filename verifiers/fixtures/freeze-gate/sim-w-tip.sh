#!/bin/sh
# sim-w-tip.sh — freeze-gate simulator for the r88 control w_tip (fail-closed).
#
# Prints the OBSERVED verdict recorded for the w_tip world (the honest landing tip
# 4df1e8005016c75390a5e06b209462df58c95918). Three committed receipts ground it:
#   - receipts/before-C2-tip.txt — the frozen r87 gate (the do-nothing control)
#     reads "FAIL d5" / "r86 routed defects closed 4 of 5" at the tip;
#   - receipts/l1-c2-tip.txt — the v2 gate re-measured by the L1 at the same tip
#     reads "PASS d5" / "r86 routed defects closed 5 of 5" / exit=0;
#   - w1/ReviewerC2/review.md (item 4) — the reviewer's independent re-derivation
#     confirms the v2 reading ("r86 routed defects closed 5 of 5", exit=0).
# w_tip is a v2-gate control (plans/round-88.md § C2), so the printed verdict is the
# v2 gate's observed verdict: w_tip D5=PASS.
#
# Fail-closed: any missing receipt or missing recorded line exits 2. Never guesses.
set -u

LANE=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
BEFORE="$LANE/.ufo/waves/round-88/receipts/before-C2-tip.txt"
AFTER="$LANE/.ufo/waves/round-88/receipts/l1-c2-tip.txt"
REVIEW="$LANE/.ufo/waves/round-88/w1/ReviewerC2/review.md"

die() { echo "sim-w-tip: $*" >&2; exit 2; }

[ -f "$BEFORE" ] || die "receipt missing: $BEFORE"
[ -f "$AFTER" ] || die "receipt missing: $AFTER"
[ -f "$REVIEW" ] || die "receipt missing: $REVIEW"

grep -q '^FAIL d5' "$BEFORE" || die "do-nothing FAIL d5 line absent from $BEFORE"
grep -q '^r86 routed defects closed 4 of 5$' "$BEFORE" \
    || die "4-of-5 line absent from $BEFORE"
grep -q '^PASS d5' "$AFTER" || die "PASS d5 line absent from $AFTER"
grep -q '^r86 routed defects closed 5 of 5$' "$AFTER" || die "5-of-5 line absent from $AFTER"
grep -q '4df1e8005016c75390a5e06b209462df58c95918' "$AFTER" \
    || die "tip revision absent from $AFTER"
grep -q '^r86 routed defects closed 5 of 5$' "$REVIEW" \
    || die "reviewer 5-of-5 line absent from $REVIEW"

echo "w_tip D5=PASS"
exit 0
