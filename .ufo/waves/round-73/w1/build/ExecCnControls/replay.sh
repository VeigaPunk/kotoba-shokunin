#!/usr/bin/env bash
# replay.sh — replay every ExecCnControls shortcut world against a fresh
# fleet-shaped sandbox and record the readings. Writes only under mktemp dirs
# and stdout; never touches the lane, the fleet repo or any lane gate's tree.
#
#   bash replay.sh [world-dir ...]
#
# For each world:
#   1. P=$(mktemp -d /tmp/k73fleet-ExecCnControls.XXXX)
#      symlink every entry of the fleet root except kotoba-shokunin into $P
#   2. git clone --shared -q --no-checkout <lane> $P/kotoba-shokunin
#      git -C $P/kotoba-shokunin checkout -q -B world <BASE>
#      (every later git call names -C $P/kotoba-shokunin; git writes stay there)
#   3. copy _common/tree, then <world>/tree over it (world 1 skips _common),
#      `git rm` the frozen entry for world 6
#   4. commit with a throwaway identity inside the sandbox, then run
#      own-reading.py, sources-census.sh validate --file and, when it exists,
#      the wave-1 counter draft check_cn_vendor_surfaces.py
set -u
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
FLEET=/home/vgpnk/Projects/shokunin
BASE=072048fa8e8a52c707d25f7079772fa317244eb7
HERE=$(cd -- "$(dirname -- "$0")" && pwd)
DRAFT="$HERE/../ExecCnCounter/check_cn_vendor_surfaces.py"
# The counter draft (SELF_SHA filled at freeze 2). If a copy with a locally
# filled SELF_SHA is needed, set FROZEN=<copy>; the draft file itself is never
# edited here.
FROZEN=${FROZEN:-$HERE/../ExecCnCounter/check_cn_vendor_surfaces.py}
ENTRY=corpus/knowledge/chinese-vendor-skill-surfaces-round73.md
TODAY=$(date -I)

worlds=("$@")
if [ ${#worlds[@]} -eq 0 ]; then
  mapfile -t worlds < <(cd "$HERE" && printf '%s\n' [0-9]-* | sort)
  worlds=("base" "${worlds[@]}")
fi

for w in "${worlds[@]}"; do
  P=$(mktemp -d /tmp/k73fleet-ExecCnControls.XXXX) || exit 1
  for e in "$FLEET"/*; do
    b=$(basename -- "$e")
    [ "$b" = kotoba-shokunin ] && continue
    ln -s "$e" "$P/$b"
  done
  git clone --shared -q --no-checkout "$LANE" "$P/kotoba-shokunin" || exit 1
  R=$P/kotoba-shokunin
  git -C "$R" checkout -q -B world "$BASE" || exit 1
  [ "$(git -C "$R" rev-parse --show-toplevel)" = "$R" ] || { echo "BAD sandbox $R"; exit 1; }
  if [ "$w" != base ]; then
    if [ "$w" != 1-* ]; then cp -a "$HERE/_common/tree/." "$R/"; fi
    cp -a "$HERE/$w/tree/." "$R/"
    if [ "$w" = 6-* ]; then rm -f "$R/$ENTRY"; fi
    git -C "$R" add -A
    git -C "$R" -c user.name=ExecCnControls -c user.email=exec@localhost \
        commit -q -m "shortcut world $w" || exit 1
  fi
  REV=$(git -C "$R" rev-parse HEAD)
  echo "=== world: $w  sandbox: $P  rev: $REV"
  python3 -B "$HERE/own-reading.py" --repo "$R" --rev "$REV"
  echo "own-reading exit: $?"
  bash "$FLEET/scripts/sources-census.sh" validate --file "$R/corpus/SOURCES.md" \
       --today "$TODAY" > "$P/census.out" 2>&1
  echo "census exit: $?  findings: $(grep -cE $'\t(E|W)[0-9]{2}\t' "$P/census.out" || true)"
  sed -n '1,6p' "$P/census.out" | sed 's/^/  census | /'
  if [ -f "$FROZEN" ]; then
    python3 -B "$FROZEN" --repo "$R" --rev "$REV" > "$P/counter.out" 2>&1
    echo "counter(draft) exit: $?"
    sed -n '1,8p' "$P/counter.out" | sed 's/^/  counter | /'
  fi
  echo "sandbox kept: $P"
done
