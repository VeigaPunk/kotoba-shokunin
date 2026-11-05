#!/usr/bin/env bash
# ctl-c2-empty: an empty skills root measures 0, never 83 -> unmet (content-bound, Q25).
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin || exit 2
S=$(mktemp -d); trap 'rm -rf -- "$S"' EXIT
mkdir -p "$S/empty-skills-root"
OUT=$(python3 -B verifiers/check_host_skill_surfaces.py --skills-root "$S/empty-skills-root" --fleet-root /home/vgpnk/Projects/shokunin 2>&1); RC=$?
if [ "$RC" -eq 0 ] && printf '%s' "$OUT" | grep -q 'host skill surfaces measured 83:'; then
  echo "empty-root world meets predicate"; exit 0
fi
echo "C2-PREDICATE-UNMET empty root rc=$RC: $(printf '%s' "$OUT" | tail -1)"
exit 1
