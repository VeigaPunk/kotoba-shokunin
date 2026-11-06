#!/usr/bin/env bash
# Round-99 pre-data receipts (L1 KotobaR99). Instruments at c0489d14; receipts under receipts/.
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
R=$L/.ufo/waves/round-99/receipts
B=52e8e95ac4faf4ded84d7b82cbc204792590d0f7
W=/fast/scratch/hyaku/kotoba-r99/L1/worlds
export HYAKU_SCRATCH=/fast/scratch/hyaku
K=$L/verifiers/fixtures/round-99/selftest-kills.py
C=$L/verifiers/fixtures/round-99/carried-reds.py
rec() { # name, then command
  local name=$1; shift
  { echo "# cmd: $*"; echo "# date: $(date -Is)"; echo "# instrument sha256: $(sha256sum "$K" | cut -c1-64) selftest-kills; $(sha256sum "$C" | cut -c1-64) carried-reds"
    cd "$L" && "$@"; echo "rc=$?"; } > "$R/$name.txt" 2>&1
}
rec redbefore-c1-base python3 -B "$K" c1 $B &
rec redbefore-c1-base-rulesv5 python3 -B "$K" c1 $B "$L" --rules v5 &
rec poscontrol-r98c1-base python3 -B "$K" r98c1 $B &
rec poscontrol-r97c1-base python3 -B "$K" r97c1 $B &
rec c2-base python3 -B "$C" $B &
for w in w1-stub-gates:a70a060c1af2c8ee08cacddef0bc0085312b8983 w2-baseline-only:5c03d99193e76d1fd2d100a0d4f6eb8f346fb926 \
  w3-checklist-gov-na-pinned:cdc2436d40eb16e119eab563d16140edb8beb9b2 w4-checklist-gov-forced-pass-pinned:6deb505562dc4bcf3901c1efafe247ef5b39590b \
  w5-battery-edited-outside-pins:93f2110ab257ad9f13a3e5429cfd1372b7bdbbeb; do
  rec "c2-ctl-${w%%:*}" python3 -B "$C" "${w##*:}" "$W" &
done
wait
grep -H -E "PREDICATE|carried reds green|targets killed|^rc=" "$R"/*.txt
