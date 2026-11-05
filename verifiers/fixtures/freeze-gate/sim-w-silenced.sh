#!/bin/sh
# sim-w-silenced.sh — freeze-gate simulator for the r88 control w_silenced (fail-closed).
#
# Prints the OBSERVED verdict recorded for the w_silenced world (the round-88 tip with
# the corpus.pointers.commit_unresolvable CHECKS entry removed from the integrity
# script): the v2 gate's identity leg (i) FAILs — 8 check names measured vs the
# reference base's 9 — so the silenced check's world is unreachable in the measured
# name set. The verdict is recorded in the --- w_silenced block of
# ExecMonotoneD5/receipts.txt ("FAIL d5  identity FAIL: rev has 8 names, base has 9").
# The silencing-class disclosure is CriticFalsify/attacks.md C2-S2 (in-place silencing
# of a red check passes D5 v2 — the round-88 freeze's blind spot, routed defect 4).
#
# Fail-closed: missing receipts or an unexpected recorded shape exit 2. Never guesses.
set -u

LANE=$(CDPATH= cd -- "$(dirname -- "$0")/../../.." && pwd)
RECEIPTS="$LANE/.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt"
ATTACKS="$LANE/.ufo/waves/round-88/w1/CriticFalsify/attacks.md"

die() { echo "sim-w-silenced: $*" >&2; exit 2; }

[ -f "$RECEIPTS" ] || die "receipt missing: $RECEIPTS"
[ -f "$ATTACKS" ] || die "receipt missing: $ATTACKS"

LINE=$(awk -v mark="--- w_silenced" '
    index($0, mark) == 1 {inbox = 1; next}
    /^--- / {inbox = 0}
    /^## / {inbox = 0}
    inbox && /^PASS d5/ {print; exit}
    inbox && /^FAIL d5/ {print; exit}
' "$RECEIPTS")
[ -n "$LINE" ] || die "no d5 verdict line in the --- w_silenced block of $RECEIPTS"

grep -q 'C2-S2' "$ATTACKS" || die "C2-S2 row absent from $ATTACKS"
grep -q 'in-place silencing of a red check passes D5 v2' "$ATTACKS" \
    || die "C2-S2 silencing row absent from $ATTACKS"

case "$LINE" in
    FAIL*)
        if printf '%s\n' "$LINE" | grep -q 'identity FAIL: rev has 8 names, base has 9'; then
            echo "w_silenced D5=FAIL-world-unreachable"
            exit 0
        fi
        ;;
esac
die "unexpected recorded verdict shape in --- w_silenced: $LINE"
