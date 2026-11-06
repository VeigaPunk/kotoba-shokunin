#!/usr/bin/env bash
# round-98 landing measurements (KotobaR98). Usage: landing-run.sh <landing-rev>
# Each receipt: header (cmd, instrument shas, date) + stdout/stderr + rc. Scratch under $HYAKU_SCRATCH.
set -u
L=${1:?landing rev}
BASE=a33f262fc94e3cf27f3c935b5c53c1336bb94166
INSTR=a060b450a43673ebc54720a5192e99df188e80ce
R=/home/vgpnk/Projects/shokunin/kotoba-shokunin
O=$R/.ufo/waves/round-98/receipts/landing
S=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotoba-r98/KotobaR98
mkdir -p "$O" "$S"
export TMPDIR=$S HYAKU_SCRATCH=$S
cd "$R" || exit 2
echo "$L" > "$O/landing-rev.txt"
K=verifiers/fixtures/round-98/selftest-kills.py
F=verifiers/fixtures/round-98/forgery-controls.py
CSHA=$(git show "$L:$K" | sha256sum | cut -c1-64)
FSHA=$(git show "$L:$F" | sha256sum | cut -c1-64)
run() { # name cmd...
  local n=$1; shift
  { echo "# cmd: $*"; echo "# landing $L; counter sha256 $CSHA; controls sha256 $FSHA; date $(date -Iseconds)"
    "$@" 2>&1; echo "rc=$?"; } > "$O/$n.txt"
}
run instr-identity bash -c "git diff --exit-code --stat $INSTR $L -- $K $F && echo 'v6 counter and C2 runner byte-identical to $INSTR'"
run c1-v6          python3 -B $K c1 "$L" &
run c1-rulesv5     python3 -B $K c1 "$L" "$R" --rules v5 &
run r97c1-v6       python3 -B $K r97c1 "$L" &
run r96c1-v6       python3 -B $K r96c1 "$L" &
run r95c1-v6       python3 -B $K r95c1 "$L" &
run c2-v6          python3 -B $F v6 "$L" &
wait
run r97-c1         python3 -B verifiers/fixtures/round-97/selftest-kills.py c1 "$L" &
run r97-r96c1      python3 -B verifiers/fixtures/round-97/selftest-kills.py r96c1 "$L" &
run r97-c2-v5      python3 -B verifiers/fixtures/round-97/forgery-controls.py v5 "$L" &
run r96-c1         python3 -B verifiers/fixtures/round-96/selftest-kills.py c1 "$L" &
run r95-c1         python3 -B verifiers/fixtures/round-95/selftest-kills.py c1 "$L" &
run r93-c1-killpin bash verifiers/fixtures/round-93/c1-killpin-rev.sh "$L" &
wait
run r92-controls   bash verifiers/fixtures/round-92/controls-run.sh &
run gate-registry  python3 -B verifiers/check_gate_registry.py --rev "$L" &
run floors-selftest python3 -B verifiers/check_assertion_floors.py --self-test &
run dp-selftest    python3 -B verifiers/verify_dispatch_prompts.py --self-test &
run dp-boxproof    python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json &
wait
git show "$BASE:verifiers/verify_dispatch_prompts.py" > "$S/dp-base.py"
git show "$L:verifiers/verify_dispatch_prompts.py" > "$S/dp-landing.py"
run dp-live-base    python3 -B "$S/dp-base.py"
run dp-live-landing python3 -B "$S/dp-landing.py"
{ echo "# cmd: diff <(grep -E '^(PASS|FAIL|N/A)' dp-live-base) <(... dp-live-landing)"
  diff <(grep -E '^(PASS|FAIL|N/A)' "$O/dp-live-base.txt") <(grep -E '^(PASS|FAIL|N/A)' "$O/dp-live-landing.txt"); echo "rc=$?"; } > "$O/dp-live-equal.txt"
run tip-battery    python3 -B verifiers/check_tip_battery.py --rev "$L"
run census         /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
run skill-identity git diff --exit-code --stat "$BASE" "$L" -- SKILL.md
run prod-identity  bash -c "diff <(git show $BASE:verifiers/verify_dispatch_prompts.py) <(git show $L:verifiers/verify_dispatch_prompts.py) | grep -E '^[0-9]' "
rm -rf -- "$S"
echo done
