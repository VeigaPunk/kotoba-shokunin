#!/bin/sh
# MutTesterAnchorR100 receipt runner: one counter reading per world.
# usage: run_counter.sh <name> <rev>
set -u
NAME=$1
REV=$2
R=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-100/w1/MutTesterAnchorR100
D=/fast/scratch/hyaku/kotoba-r100/MutTesterAnchorR100/repo
export HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r100/MutTesterAnchorR100
export TMPDIR=/fast/scratch/hyaku/kotoba-r100/MutTesterAnchorR100
OUT=$R/counter-$NAME.txt
{
  echo "# cmd: python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-100/anchor-lists.py $REV $D"
  echo "# date: $(date -Iseconds)"
  echo "# instrument sha256: $(sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-100/anchor-lists.py | cut -d' ' -f1) anchor-lists"
  python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-100/anchor-lists.py "$REV" "$D" 2>&1
  echo "rc=$?"
} > "$OUT" 2>&1
