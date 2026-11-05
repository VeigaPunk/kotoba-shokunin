#!/bin/sh
# R87-D7 sweep: LOG.md round-87 C2 "verified, `5 of 5`" lines that no later LOG entry supersedes.
# Prints the unannotated stale lines and exits 1 if any remain (red), 0 if none (green).
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin || exit 2
stale=$(grep -n 'C2 — consistency (calibration sub-axis, score 10): verified, `5 of 5`' LOG.md | cut -d: -f1)
unannotated=0
for n in $stale; do
  if ! tail -n +$((n+1)) LOG.md | grep -q "supersedes LOG.md:$n"; then
    echo "UNANNOTATED stale line $n"
    unannotated=$((unannotated+1))
  fi
done
echo "stale=$(echo $stale | wc -w) unannotated=$unannotated"
[ "$unannotated" -eq 0 ]
