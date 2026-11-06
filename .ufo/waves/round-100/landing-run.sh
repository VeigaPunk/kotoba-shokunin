#!/usr/bin/env bash
# Round-100 landing readings (L1 KotobaR100). Usage: landing-run.sh <landing rev>
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
R=$L/.ufo/waves/round-100/receipts/landing
REV=$1
B=7b449a637c03d9b4c43a81b4df37cb38c2ea89ee
F=03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687
export HYAKU_SCRATCH=/fast/scratch/hyaku
K=$L/verifiers/fixtures/round-100/selftest-kills.py
C=$L/verifiers/fixtures/round-100/anchor-lists.py
mkdir -p "$R"
rec() { local name=$1; shift
  { echo "# cmd: $*"; echo "# date: $(date -Is)"; echo "# rev: $REV"; cd "$L" && "$@"; echo "rc=$?"; } > "$R/$name.txt" 2>&1; }
rec c1-v62 python3 -B "$K" c1 "$REV" &
rec c1-rulesv5 python3 -B "$K" c1 "$REV" "$L" --rules v5 &
for t in r99c1 r98c1 r97c1 r96c1 r95c1; do rec "$t-v62" python3 -B "$K" $t "$REV" & done
rec c2 python3 -B "$C" "$REV" &
wait
W=/fast/scratch/hyaku/kotoba-r100/L1/landing-world; rm -rf "$W"; mkdir -p "$W"
git -C "$L" archive "$REV" | tar -x -C "$W"
rec dp-selftest python3 -B "$W/verifiers/verify_dispatch_prompts.py" --self-test
rec dp-boxproof bash -c "cd '$W' && python3 -B verifiers/verify_dispatch_prompts.py --box-proof"
rec battery python3 -B "$L/verifiers/check_tip_battery.py" --repo "$L" --rev "$REV" --fleet /home/vgpnk/Projects/shokunin
rec gate-registry python3 -B "$L/verifiers/check_gate_registry.py" --rev "$REV"
rec census-end /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
{ echo "# production identity: diffs from the freeze $F to $REV"
  git -C "$L" diff -U0 "$F" "$REV" -- verifiers/verify_dispatch_prompts.py | grep '^@@'
  echo "deleted lines dispatch_prompts: $(git -C "$L" diff "$F" "$REV" -- verifiers/verify_dispatch_prompts.py | grep -c '^-[^-]')"
  git -C "$L" diff -U0 "$F" "$REV" -- verifiers/verify_skill_checklist.py | grep '^@@'
  echo "counter blobs at REV vs instrument d1e1170d:"
  for f in selftest-kills.py anchor-lists.py; do echo "$f $(git -C "$L" rev-parse $REV:verifiers/fixtures/round-100/$f) $(git -C "$L" rev-parse d1e1170d:verifiers/fixtures/round-100/$f)"; done
} > "$R/identity.txt" 2>&1
rm -rf "$W"
grep -H -E "PREDICATE|^C[12] |targets killed|failure\(s\) over|boxes proven|guards|^rc=" "$R"/*.txt
