#!/usr/bin/env bash
# Round-99 landing readings (L1 KotobaR99). Usage: landing-run.sh <landing rev>
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
R=$L/.ufo/waves/round-99/receipts/landing
mkdir -p "$R"
V=$1
B=52e8e95ac4faf4ded84d7b82cbc204792590d0f7
export HYAKU_SCRATCH=/fast/scratch/hyaku
K=$L/verifiers/fixtures/round-99/selftest-kills.py
K98=$L/verifiers/fixtures/round-98/selftest-kills.py
C=$L/verifiers/fixtures/round-99/carried-reds.py
rec() {
  local name=$1; shift
  { echo "# cmd: $*"; echo "# date: $(date -Is)"; echo "# rev: $V"
    echo "# instrument sha256: $(sha256sum "$K" | cut -c1-64) selftest-kills v6.1; $(sha256sum "$C" | cut -c1-64) carried-reds"
    cd "$L" && "$@"; echo "rc=$?"; } > "$R/$name.txt" 2>&1
}
rec c1-v61 python3 -B "$K" c1 "$V" &
rec c1-rulesv5 python3 -B "$K" c1 "$V" "$L" --rules v5 &
rec r98c1-v61 python3 -B "$K" r98c1 "$V" &
rec r97c1-v61 python3 -B "$K" r97c1 "$V" &
rec c2 python3 -B "$C" "$V" &
wait
rec r96c1-v61 python3 -B "$K" r96c1 "$V" &
rec r95c1-v61 python3 -B "$K" r95c1 "$V" &
rec r98-counter-c1 python3 -B "$K98" c1 "$V" &
rec gate-registry python3 -B verifiers/check_gate_registry.py --rev "$V" &
wait
D=/fast/scratch/hyaku/kotoba-r99/L1/landing-wt
rm -rf "$D"; mkdir -p "$D"; git -C "$L" archive "$V" | tar -x -C "$D"
{ echo "# git archive $V; python3 -B verifiers/verify_dispatch_prompts.py --box-proof"; cd "$D" && python3 -B verifiers/verify_dispatch_prompts.py --box-proof; echo "rc=$?"; } > "$R/dp-boxproof.txt" 2>&1
{ echo "# git archive $V; python3 -B verifiers/verify_dispatch_prompts.py --self-test | tail -1"; cd "$D" && python3 -B verifiers/verify_dispatch_prompts.py --self-test | tail -1; echo "rc=${PIPESTATUS[0]}"; } > "$R/dp-selftest.txt" 2>&1
{ echo "# git diff -U0 $B $V -- verifiers/verify_dispatch_prompts.py | grep '^@@'"; git -C "$L" diff -U0 $B "$V" -- verifiers/verify_dispatch_prompts.py | grep '^@@'; } > "$R/prod-identity.txt" 2>&1
{ echo "# instrument bytes at $V equal to instrument commit c0489d14"; for f in verifiers/fixtures/round-99/selftest-kills.py verifiers/fixtures/round-99/carried-reds.py; do git -C "$L" diff --quiet c0489d14156a7687d10ae5389d72eaa923b2bc29 "$V" -- $f && echo "$f identical" || echo "$f DIFFERS"; done; } > "$R/instr-identity.txt" 2>&1
rm -rf "$D"
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba > "$R/census-end.txt" 2>&1; echo "rc=$?" >> "$R/census-end.txt"
grep -H -E "PREDICATE|targets killed|carried reds green|boxes proven|failure\(s\)|identical|DIFFERS|^@@|registry rows|^rc=" "$R"/*.txt
