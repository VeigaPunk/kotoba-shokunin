#!/usr/bin/env bash
# ctl-c1-stub: a scratch stub printing the success line without a manifest fails the manifest guard -> unmet.
B=0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5
S=$(mktemp -d)
trap 'rm -rf -- "$S"' EXIT
cat > "$S/check_mutation_battery.py" <<'PY'
import sys
print("mutation battery killed 3 of 3 kill-set; equivalents survived 2 of 2; disclosed survivors 1 of 1")
sys.exit(0)
PY
OUT=$(python3 -B "$S/check_mutation_battery.py"); RC=$?
N=$(git show "$B:SKILL.md" | grep -c 'check_mutation_battery.py' || true)
if [ "$RC" -eq 0 ] && [ "$N" -ge 1 ]; then echo "stub world meets predicate"; exit 0; fi
echo "C1-PREDICATE-UNMET stub prints the line (rc=$RC) but manifest/registry guard fails (registry rows: $N)"
exit 1
