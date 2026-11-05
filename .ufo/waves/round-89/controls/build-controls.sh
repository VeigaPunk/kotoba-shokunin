#!/bin/bash
# Round-89 control builder (KotobaR89, L1). Run once at the freeze commit (A) before any landing measurement.
# Worlds are lane-shaped (Q79 location class): each clone sits directly under a scaffold dir that holds the
# fleet-root copy of the tracked round-76 symlink target, so the receipt and every measured root share the
# "lane" location class. Scratch lives under $HYAKU_SCRATCH/kotoba-r89 and is deleted on exit.
set -eu
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
GATE=$LANE/verifiers/check_r86_routed_repairs_v3.py
FREEZE=${FREEZE:?set FREEZE to the freeze commit hash}
BASE=a5b3b15c00b1de5db321e4226a0a7db17340e605
RC=$LANE/.ufo/waves/round-89/receipts
OUT=$LANE/.ufo/waves/round-89/controls
SCR=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r89
S=$SCR/scaffold
trap 'rm -rf -- "$SCR"' EXIT
rm -rf "$S"; mkdir -p "$S/shokunin/.ufo/reports/round-76" "$OUT"
cp /home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md "$S/shokunin/.ufo/reports/round-76/kotoba.md"
mk() { git clone -q --shared "$LANE" "$S/shokunin/$1"; git -C "$S/shokunin/$1" checkout -q --detach "$2"
       test "$(git -C "$S/shokunin/$1" rev-parse --show-toplevel)" = "$S/shokunin/$1"; }
mk base "$BASE"; mk tip "$FREEZE"
for w in w_added_instance w_silenced w_rerecorded; do mk "$w" "$FREEZE"; done

# 1) base receipt at the round base, written by a copy of the gate inside the base clone (LANE = that clone)
cp "$GATE" "$S/shokunin/base/verifiers/check_r86_routed_repairs_v3.py"
echo "verifiers/check_r86_routed_repairs_v3.py" >> "$S/shokunin/base/.git/info/exclude"
python3 -B "$S/shokunin/base/verifiers/check_r86_routed_repairs_v3.py" --write-base-receipt "$OUT/base-a5b3b15c-receipt.json" \
  > "$OUT/base-a5b3b15c-write.txt" 2>&1; echo "write-base-exit=$?" >> "$OUT/base-a5b3b15c-write.txt"

# 2) worlds (scratch deltas on the freeze clone; none touches a pinned record)
echo 'Control citation for round 89: commit `0123456789abcdef0123456789abcdef01234567`.' >> "$S/shokunin/w_added_instance/corpus/lessons/round-89.md"
sed -i '/"corpus.pointers.commit_nonhash": ("zero"/d' "$S/shokunin/w_silenced/verifiers/verify_corpus_integrity.py"
sed -i '15s/"expect": 172/"expect": 177/' "$S/shokunin/w_rerecorded/verifiers/corpus-baseline.json"
test "$(sed -n 15p "$S/shokunin/w_rerecorded/verifiers/corpus-baseline.json" | grep -c 177)" = 1

# 3) runs: the lane-written freeze receipt, judged on each world; the base receipt judged on the freeze tip
run() { # name receipt root expected-exit
  set +e; TMPDIR="$SCR" python3 -B "$GATE" --base-receipt "$2" --root "$3" > "$OUT/final-$1.txt" 2>&1; rc=$?; set -e
  echo "expected-exit=$4 observed-exit=$rc" >> "$OUT/final-$1.txt"; }
run w_tip        "$RC/d5v3-base-receipt.json" "$S/shokunin/tip" 0
run w_added_instance "$RC/d5v3-base-receipt.json" "$S/shokunin/w_added_instance" 1
run w_silenced   "$RC/d5v3-base-receipt.json" "$S/shokunin/w_silenced" 1
run w_rerecorded "$RC/d5v3-base-receipt.json" "$S/shokunin/w_rerecorded" 1
run w_healed     "$OUT/base-a5b3b15c-receipt.json" "$S/shokunin/tip" 0

# 4) equivalence: the lane and the lane-shaped tip clone print the same observation (Q79)
TMPDIR="$SCR" python3 -B "$GATE" --base-receipt "$RC/d5v3-base-receipt.json" --print-observation > "$OUT/equiv-lane.txt" 2>&1 || true
TMPDIR="$SCR" python3 -B "$GATE" --base-receipt "$RC/d5v3-base-receipt.json" --root "$S/shokunin/tip" --print-observation > "$OUT/equiv-tip.txt" 2>&1 || true
awk '/^(PASS|FAIL|SKIP|r86|instance)/ {exit} {print}' "$OUT/equiv-lane.txt" | sha256sum > "$OUT/equiv-lane.sha"
awk '/^(PASS|FAIL|SKIP|r86|instance)/ {exit} {print}' "$OUT/equiv-tip.txt" | sha256sum > "$OUT/equiv-tip.sha"
cmp "$OUT/equiv-lane.sha" "$OUT/equiv-tip.sha" && echo "equivalence: IDENTICAL observation" | tee "$OUT/equivalence.txt"
echo "done"
