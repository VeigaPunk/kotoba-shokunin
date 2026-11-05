#!/bin/sh
# sim-w-healed.sh — freeze-gate simulator for the r88 control w_healed (fail-closed).
#
# Prints the OBSERVED verdict recorded for the w_healed world (the round-87 base
# 223ae62424f8ab1eb365d733eb648d6228ddd7e8 with its report_dead red resolved): the
# v2 gate reads D5 PASS — a healed red passes; blanket refusal is not a gain. The
# verdict is recorded in the --- w_healed block of ExecMonotoneD5/receipts.txt
# ("PASS d5  identity: 9 names equal at base and rev; monotone: ...").
#
# Fail-closed: a missing receipt or a missing verdict line exits 2. Never guesses.
set -u

LANE=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
RECEIPTS="$LANE/.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt"

die() { echo "sim-w-healed: $*" >&2; exit 2; }

[ -f "$RECEIPTS" ] || die "receipt missing: $RECEIPTS"

VERDICT=$(awk -v mark="--- w_healed" '
    index($0, mark) == 1 {inbox = 1; next}
    /^--- / {inbox = 0}
    /^## / {inbox = 0}
    inbox && /^PASS d5/ {print "PASS"; exit}
    inbox && /^FAIL d5/ {print "FAIL"; exit}
' "$RECEIPTS")
[ -n "$VERDICT" ] || die "no d5 verdict line in the --- w_healed block of $RECEIPTS"

echo "w_healed D5=$VERDICT"
exit 0
