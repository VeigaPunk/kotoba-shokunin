#!/usr/bin/env bash
# X01-counterbuild-receipts.sh — regenerate the C2 counter receipts (kotoba r79 w1).
# Read-only over the lane; writes only into .ufo/waves/round-79/build/.
set -u
L=/home/vgpnk/Projects/shokunin/kotoba-shokunin
R=$L/.ufo/waves/round-79/build
C=$R/check_allowed_tools.py
BASE=b10bcbc6b00f8f56b202ccbadca311007b5b463c
S=${S:-/fast/scratch/hyaku/kotoba-r79/Kb79X01CounterBuild}
export TMPDIR=$S/tmp
mkdir -p "$TMPDIR" "$S/home"
OUT=$R/X01CounterBuild-receipts.txt
{
echo "# X01 counter receipts — kotoba round 79 w1 — $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "# scratch: $S (removed at yield); TMPDIR=$TMPDIR"
echo
echo '## counter bytes'
echo "\$ sha256sum \$C"; sha256sum "$C"
echo "\$ wc -l \$C"; wc -l < "$C"
echo "\$ python3 -B \$C --print-self-sha"; python3 -B "$C" --print-self-sha
echo
echo '## --self-test (stdlib only, no network, isolated local git repos)'
python3 -B "$C" --self-test --work "$TMPDIR" > "$R/selftest.txt" 2>&1; rc=$?
echo "\$ python3 -B check_allowed_tools.py --self-test --work \$TMPDIR   # rc=$rc   (full output: selftest.txt, $(wc -l < "$R/selftest.txt") lines)"
tail -3 "$R/selftest.txt"
echo
echo '## base measurement, absolute --repo form'
python3 -B "$C" --repo "$L" --rev "$BASE" --work "$TMPDIR" > "$R/base-c2-abs.txt" 2>&1; rc=$?
echo "\$ python3 -B \$C --repo $L --rev $BASE   # rc=$rc"
cat "$R/base-c2-abs.txt"
echo
echo '## base measurement, relative --repo . form (cwd = lane root)'
(cd "$L" && python3 -B "$C" --repo . --rev "$BASE" --work "$TMPDIR" > "$R/base-c2-dot.txt" 2>&1); rc=$?
echo "\$ cd $L && python3 -B \$C --repo . --rev $BASE   # rc=$rc"
cat "$R/base-c2-dot.txt"
echo
echo '## counter in its eventual home (scratch clone at lane HEAD, verifiers/check_allowed_tools.py)'
if [ ! -d "$S/home/clone" ]; then
  git clone -q --shared "$L" "$S/home/clone"
  git -C "$S/home/clone" checkout -q "$(git -C "$L" rev-parse HEAD)"
fi
test "$(git -C "$S/home/clone" rev-parse --show-toplevel)" = "$S/home/clone" || { echo "TOPLEVEL MISMATCH"; exit 9; }
cp "$C" "$S/home/clone/verifiers/check_allowed_tools.py"
(cd "$S/home/clone" && python3 -B verifiers/check_allowed_tools.py --rev HEAD --work "$TMPDIR" > "$R/home-from-verifiers.txt" 2>&1); rc=$?
echo "\$ (scratch clone) python3 -B verifiers/check_allowed_tools.py --rev HEAD   # rc=$rc"
cat "$R/home-from-verifiers.txt"
(cd "$S/home/clone" && python3 -B verifiers/check_allowed_tools.py --repo . --rev "$BASE" --work "$TMPDIR" > "$R/home-from-verifiers-base.txt" 2>&1); rc=$?
echo "\$ (scratch clone) python3 -B verifiers/check_allowed_tools.py --repo . --rev $BASE   # rc=$rc"
head -3 "$R/home-from-verifiers-base.txt"
echo
echo '## held-at-base probe: which frozen hosts already appear in corpus/SOURCES.md at base'
echo '$ git show '"$BASE"':corpus/SOURCES.md | grep -c -- <host>'
for h in "agentskills.io" "code.claude.com" "docs.factory.com/harness/skills" "learn.microsoft.com" "raw.githubusercontent.com/badlogic/pi-mono" "raw.githubusercontent.com/mistralai/mistral-vibe"; do
  printf "%-52s %s\n" "$h" "$(git -C "$L" show "$BASE":corpus/SOURCES.md | grep -c -- "$h")"
done
echo
echo '## temp-dir discipline (no hardcoded /tmp; mktemp honours TMPDIR and --work)'
TMPDIR="$TMPDIR" python3 -B - "$C" <<'PY'
import importlib.util, os, sys, shutil
spec = importlib.util.spec_from_file_location("k", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
d = m.mktemp("probe-")
print(d, "under TMPDIR" if d.startswith(os.environ["TMPDIR"]) else "NOT UNDER TMPDIR")
shutil.rmtree(d)
PY
} > "$OUT" 2>&1
rc=$?
echo "receipts rc=$rc -> $OUT"
