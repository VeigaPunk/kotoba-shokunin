#!/bin/bash
# SentinelScopeR99 final no-harm runner. Usage: final_checks.sh <CAND_REV> <D>
set -uo pipefail
SEAT=SentinelScopeR99
S=/fast/scratch/hyaku/kotoba-r99/$SEAT
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
BASE=b53e209603e7c480cd975ea543e415b66f695438
REV="$1"; D="$2"
export TMPDIR=$S/tmp HYAKU_SCRATCH=$S
mkdir -p "$TMPDIR"
LOG=$S/final-checks.log
: > "$LOG"
run() { # label, command...
  local label="$1"; shift
  echo "=== $label" >> "$LOG"
  echo "\$ $*" >> "$LOG"
  "$@" >> "$LOG" 2>&1
  echo "rc=$?" >> "$LOG"
  echo >> "$LOG"
}
run "gate-registry" python3 -B "$D/verifiers/check_gate_registry.py" --rev "$REV"
run "r98-c1" python3 -B "$LANE/verifiers/fixtures/round-98/selftest-kills.py" c1 "$REV" "$D"
run "r98-r97c1" python3 -B "$LANE/verifiers/fixtures/round-98/selftest-kills.py" r97c1 "$REV" "$D"
run "floors-selftest" python3 -B "$D/verifiers/check_assertion_floors.py" --self-test
run "box-proof" python3 -B "$D/verifiers/verify_dispatch_prompts.py" --box-proof
run "live" python3 -B "$D/verifiers/verify_dispatch_prompts.py" \
  --prompts /home/vgpnk/Projects/shokunin/.ufo/prompts \
  --state-dir /home/vgpnk/Projects/shokunin/.ufo/state \
  --fleet /home/vgpnk/Projects/shokunin
echo "=== census" >> "$LOG"
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md" >> "$LOG" 2>&1
echo "rc=$?" >> "$LOG"
echo "W04=$(bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file "$D/corpus/SOURCES.md" 2>&1 | grep -c W04)" >> "$LOG"
echo >> "$LOG"
run "tip-battery" python3 -B "$D/verifiers/check_tip_battery.py" --repo "$D" --rev "$REV" \
  --fleet /home/vgpnk/Projects/shokunin
echo DONE >> "$LOG"
