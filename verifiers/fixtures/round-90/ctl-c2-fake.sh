#!/usr/bin/env bash
# ctl-c2-fake: a one-file scratch root measures 1, never 83 -> unmet (content-bound, Q25).
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin || exit 2
S=$(mktemp -d); trap 'rm -rf -- "$S"' EXIT
mkdir -p "$S/fake-skills-root/onelane"
cp SKILL.md "$S/fake-skills-root/onelane/SKILL.md"
OUT=$(python3 -B verifiers/check_host_skill_surfaces.py --skills-root "$S/fake-skills-root" --fleet-root /home/vgpnk/Projects/shokunin 2>&1); RC=$?
if [ "$RC" -eq 0 ] && printf '%s' "$OUT" | grep -q 'host skill surfaces measured 83:'; then
  echo "fake-root world meets predicate"; exit 0
fi
echo "C2-PREDICATE-UNMET fake root rc=$RC: $(printf '%s' "$OUT" | tail -1)"
exit 1
