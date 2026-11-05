#!/usr/bin/env bash
# ctl-c2-windows: the r84 Windows-root form cannot reach this host's surface -> unmet.
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin || exit 2
OUT=$(python3 -B verifiers/check_host_skill_surfaces.py --skills-root "C:/Users/jpvei/.agents/skills" --fleet-root /home/vgpnk/Projects/shokunin 2>&1); RC=$?
if [ "$RC" -eq 0 ] && printf '%s' "$OUT" | grep -q 'host skill surfaces measured 83:'; then
  echo "windows-root world meets predicate"; exit 0
fi
echo "C2-PREDICATE-UNMET r84 Windows-root form rc=$RC: $(printf '%s' "$OUT" | tail -1)"
exit 1
