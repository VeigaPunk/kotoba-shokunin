#!/usr/bin/env bash
# ctl-c2-capline-only (round 91): the shortcut "raise the child cap and say nothing else". Meets the
# predicate only if the cap is >= 2x the measured duration AND the floors blob is pinned at the rev;
# at base the cap is 120, so the cap test alone already refuses.
set -u
LANE="$(cd "$(dirname "$0")/../../.." && pwd)"
cap="$(grep -E '^SELF_TEST_TIMEOUT_S = ' "$LANE/verifiers/check_assertion_floors.py" | awk '{print $3}')"
echo "SELF_TEST_TIMEOUT_S=${cap:-absent}"
if [ -n "${cap:-}" ] && [ "$cap" -ge 320 ] 2>/dev/null; then echo "C2-PREDICATE-MET"; exit 0; fi
echo "C2-PREDICATE-UNMET"; exit 1
