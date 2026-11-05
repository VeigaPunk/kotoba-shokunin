#!/usr/bin/env bash
# ctl-c1-r89harness: the r89 wave battery exists but is not a registered lane verifier -> unmet.
B=0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5
if ! git cat-file -e "$B:.ufo/waves/round-89/w1/MutTesterGates/harness.py" 2>/dev/null; then
  echo "harness missing (unexpected)"; exit 1
fi
N=$(git show "$B:SKILL.md" | grep -c 'check_mutation_battery.py' || true)
if [ "$N" -ge 1 ]; then echo "registry row present"; exit 0; fi
echo "C1-PREDICATE-UNMET r89 harness present but no registered instrument (registry rows naming it: $N)"
exit 1
