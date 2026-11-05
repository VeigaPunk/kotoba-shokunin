#!/usr/bin/env bash
# ctl-c1-base (round 91, C1 no-work control): runs the battery instrument exactly as it stood at the
# round base and exits 0 iff the frozen C1 predicate line is printed. At base the battery prints
# "killed 14 of 14", so the predicate is unmet and the control must exit 1.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r91/ctl-c1-base"
mkdir -p "$ROOT" && W="$(mktemp -d "$ROOT/w.XXXX")" || { echo "C1-PREDICATE-UNMET: scratch unavailable"; exit 1; }
trap 'rm -rf -- "$W"' EXIT
out="$(cd "$LANE" && TMPDIR="$W" python3 -B verifiers/check_mutation_battery.py --rev 9264baaa823cdae3d009a4004e014639551e016f --work "$W" 2>&1)"
echo "$out" | tail -3
if echo "$out" | grep -q 'mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0'; then
  echo "C1-PREDICATE-MET"; exit 0
fi
echo "C1-PREDICATE-UNMET"; exit 1
