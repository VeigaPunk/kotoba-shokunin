#!/usr/bin/env bash
# ctl-c2-base (round 91, C2 no-work control): the tip battery at the round base. Leg A(d) requires
# "guards 5 of 5" with the floors blob pinned; at base the line reads "guards 4 of 5", so unmet.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r91/ctl-c2-base"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/w.XXXX")" || { echo "C2-PREDICATE-UNMET: scratch unavailable"; exit 1; }
trap 'rm -rf -- "$W"' EXIT
out="$(cd "$LANE" && TMPDIR="$W" python3 -B verifiers/check_tip_battery.py --rev 9264baaa823cdae3d009a4004e014639551e016f 2>&1)"
echo "$out" | tail -1
if echo "$out" | grep -q 'guards 5 of 5'; then echo "C2-PREDICATE-MET"; exit 0; fi
echo "C2-PREDICATE-UNMET"; exit 1
