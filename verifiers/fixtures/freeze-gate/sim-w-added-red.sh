#!/bin/sh
# sim-w-added-red.sh — freeze-gate simulator for the r88 control w_added_red (fail-closed).
#
# Prints the OBSERVED verdict that the committed round-88 receipts record for the
# w_added_red world (the round-88 tip plus a pointer to an unresolvable commit in a
# new lesson line): ExecMonotoneD5 measured the v2 gate's D5 on that world as PASS
# (finding F1 — the frozen control expected FAIL via (ii), which the name-level
# monotone predicate cannot produce; CriticFalsify C2-S1; plans/round-89.md routed
# defect 3). The r88 freeze declared `expect: exit 0; stdout contains D5=FAIL` for
# this control and never executed it — the disagreement this fixture reproduces.
#
# Grounding (grep targets, all committed):
#   .ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt   --- w_added block (PASS d5)
#   .ufo/waves/round-88/w1/ExecMonotoneD5.md             F1 + the control table row
#
# Fail-closed: a missing receipt, a missing control block, or a verdict line that no
# longer matches the recorded shape exits 2 (could-not-evaluate). It never guesses.
set -u

LANE=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
RECEIPTS="$LANE/.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt"
REPORT="$LANE/.ufo/waves/round-88/w1/ExecMonotoneD5.md"

die() { echo "sim-w-added-red: $*" >&2; exit 2; }

[ -f "$RECEIPTS" ] || die "receipt missing: $RECEIPTS"
[ -f "$REPORT" ] || die "receipt missing: $REPORT"

VERDICT=$(awk -v mark="--- w_added" '
    index($0, mark) == 1 {inbox = 1; next}
    /^--- / {inbox = 0}
    /^## / {inbox = 0}
    inbox && /^PASS d5/ {print "PASS"; exit}
    inbox && /^FAIL d5/ {print "FAIL"; exit}
' "$RECEIPTS")
[ -n "$VERDICT" ] || die "no d5 verdict line in the --- w_added block of $RECEIPTS"

grep -q 'F1 — the monotone test cannot see a new instance' "$REPORT" \
    || die "F1 marker absent from $REPORT"
grep -q 'w_added_red (tip + unresolvable citation line)' "$REPORT" \
    || die "w_added_red control row absent from $REPORT"

echo "w_added_red D5=$VERDICT"
exit 0
