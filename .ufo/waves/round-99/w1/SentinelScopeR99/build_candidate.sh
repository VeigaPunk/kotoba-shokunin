#!/bin/bash
# SentinelScopeR99 candidate builder.
# Usage: build_candidate.sh <seat>   (seat = SentinelScopeR99)
set -euo pipefail
SEAT="${1:-SentinelScopeR99}"
BASE=b53e209603e7c480cd975ea543e415b66f695438
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
W1="$LANE/.ufo/waves/round-99/w1"
D=/fast/scratch/hyaku/kotoba-r99/$SEAT/repo
rm -rf -- "$D"
git clone -q --shared "$LANE" "$D"
git -C "$D" checkout -q "$BASE"
top=$(git -C "$D" rev-parse --show-toplevel)
[ "$top" = "$D" ] || { echo "FATAL toplevel $top != $D"; exit 2; }
git -C "$D" config user.name scratch
git -C "$D" config user.email scratch@invalid
for seat in ExecRedsR99 ScribeCorpusR99 ExecArmsR99; do
  p="$W1/$seat/$seat.patch"
  if [ ! -s "$p" ]; then echo "FATAL missing or empty patch: $p"; exit 2; fi
  echo "== applying $seat ($(sha256sum "$p" | cut -d' ' -f1))"
  git -C "$D" apply --binary "$p"
  git -C "$D" add -A
  git -C "$D" commit -q -m "round-99 candidate: $seat"
done
echo "CANDIDATE $(git -C "$D" rev-parse HEAD)"
