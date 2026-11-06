#!/usr/bin/env bash
# Round-100 pre-data receipts (L1 KotobaR100). Instruments at d1e1170d; receipts under receipts/.
# Control worlds: .ufo/waves/round-100/build-ctl-worlds.py <scratch repo> (patches in receipts/ctl-worlds/).
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
R=$L/.ufo/waves/round-100/receipts
B=7b449a637c03d9b4c43a81b4df37cb38c2ea89ee
W=/fast/scratch/hyaku/kotoba-r100/L1/worlds
export HYAKU_SCRATCH=/fast/scratch/hyaku
K=$L/verifiers/fixtures/round-100/selftest-kills.py
C=$L/verifiers/fixtures/round-100/anchor-lists.py
rec() { # name, then command
  local name=$1; shift
  { echo "# cmd: $*"; echo "# date: $(date -Is)"; echo "# instrument sha256: $(sha256sum "$K" | cut -c1-64) selftest-kills; $(sha256sum "$C" | cut -c1-64) anchor-lists"
    cd "$L" && "$@"; echo "rc=$?"; } > "$R/$name.txt" 2>&1
}
rec redbefore-c1-base python3 -B "$K" c1 $B &
rec redbefore-c1-base-rulesv5 python3 -B "$K" c1 $B "$L" --rules v5 &
rec poscontrol-r99c1-base python3 -B "$K" r99c1 $B &
rec poscontrol-r98c1-base python3 -B "$K" r98c1 $B &
rec c2-base python3 -B "$C" $B &
while IFS=: read -r name rev; do
  rec "c2-ctl-$name" python3 -B "$C" "$rev" "$W" &
done < /fast/scratch/hyaku/kotoba-r100/L1/ctl-revs.txt
wait
grep -H -E "PREDICATE|^C2 |targets killed|^rc=" "$R"/*.txt
