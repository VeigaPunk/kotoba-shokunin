#!/bin/bash
S=/fast/scratch/hyaku/kotoba-r98/MutTesterCounterV6
cd "$S"
run_one() { n="$1"; python3 -B "$S/harness.py" "$S/counters/$n.py" "$n" --c2 --tables > "$S/logs/matrix/$n.txt" 2>&1; }
export -f run_one 2>/dev/null || true
for n in W1-rule8-off W2-rule9-env-inherited W3-nondumpable-removed W4-rule10-removed W5-seed-in-child-env W6-hardlink-pristine V4-home-xdg-not-reset V5-no-shuffle V6-honest-any V7-unicode-uncaught V8-mirror-original V9-decoy-runerror-held; do echo "$n"; done | xargs -P 2 -I{} bash -c 'n={}; python3 -B "$0/harness.py" "$0/counters/$n.py" "$n" --c2 --tables > "$0/logs/matrix/$n.txt" 2>&1' "$S"
echo MATRIX-DONE
