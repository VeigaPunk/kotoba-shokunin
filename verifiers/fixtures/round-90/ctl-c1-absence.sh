#!/usr/bin/env bash
# ctl-c1-absence: at the base revision no battery instrument exists -> C1 predicate unmet.
B=0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5
if git cat-file -e "$B:verifiers/check_mutation_battery.py" 2>/dev/null; then
  echo "instrument exists at base"; exit 0
fi
echo "C1-PREDICATE-UNMET no verifiers/check_mutation_battery.py at $B"
exit 1
