#!/usr/bin/env bash
# MutTesterKillPin scratch driver (round 93). Serial: one counter run at a time.
set -u
S=/fast/scratch/hyaku/kotoba-r93/MutTesterKillPin
D=$S/repo
CAND=75213bd92a8e7c9fc8e433a4915f5f70f1e1ac16
LANE=/home/vgpnk/Projects/shokunin/kotoba-shokunin
C1=$LANE/verifiers/fixtures/round-93/c1-killpin-rev.sh
OUT=$S/out
MAN=verifiers/fixtures/mutation-battery/manifest.tsv
export TMPDIR=$S HYAKU_SCRATCH=$S
mkdir -p "$OUT"

commit_mutant() {  # name -> prints rev
  local name=$1
  git -C "$D" checkout -q -f "$CAND" || return 1
  python3 -B "$S/mut.py" "$D" "$name" >&2 || return 1
  git -C "$D" add -A -- verifiers/check_mutation_battery.py || return 1
  git -C "$D" -c user.name=scratch -c user.email=scratch@invalid commit -q -m "r93 mutant $name (scratch, not a lane commit)" || return 1
  git -C "$D" rev-parse HEAD
}

run_mut() {  # name
  local name=$1 rev
  rev="$(commit_mutant "$name")" || { echo "BUILD-FAILED $name" | tee "$OUT/$name-summary.txt"; return; }
  git -C "$D" diff "$CAND" "$rev" -- verifiers > "$OUT/$name.diff"
  {
    echo "mutant $name rev $rev"
    bash "$C1" "$rev" "$D" 2>&1
    echo "counter_rc=$?"
  } > "$OUT/$name-counter.txt"
  ( cd "$D" && TMPDIR="$S" python3 -B verifiers/check_mutation_battery.py --self-test ) > "$OUT/$name-selftest.txt" 2>&1
  echo "selftest_rc=$?" >> "$OUT/$name-selftest.txt"
  git -C "$D" checkout -q -f "$CAND"
}

# 1. candidate: dirty working-tree probe (committed bytes must govern; expect rc 0)
dirty_probe() {  # name label
  local name=$1 label=$2
  python3 -B - "$D/$MAN" <<'PY' || return
import pathlib, sys
p = pathlib.Path(sys.argv[1]); lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
for i, ln in enumerate(lines[1:], 1):
    f = ln.rstrip("\n").split("\t")
    if len(f) >= 3 and f[2] == "kill":
        del lines[i]; break
p.write_text("".join(lines), encoding="utf-8")
PY
  ( cd "$D" && python3 -B verifiers/check_mutation_battery.py --rev "$(git -C "$D" rev-parse HEAD)" --work "$S/wdirty-$label" ) > "$OUT/dirty-$label.txt" 2>&1
  echo "dirty_rc=$?" >> "$OUT/dirty-$label.txt"
  git -C "$D" checkout -q -- "$MAN"
}

git -C "$D" checkout -q -f "$CAND"
( cd "$D" && python3 -B verifiers/check_mutation_battery.py --rev "$CAND" --work "$S/wdirty-cand-noop" ) > "$OUT/honest-cand.txt" 2>&1; echo "honest_rc=$?" >> "$OUT/honest-cand.txt"
dirty_probe cand cand

for m in m1 m2 m3 m4 m5 m6; do
  run_mut "$m"
done

# m3 dirty probe: the mutant reads the working tree, so a dirty kill-row drop must refuse under m3.
rev="$(commit_mutant m3)" && dirty_probe m3 m3
git -C "$D" checkout -q -f "$CAND"

# 2. added-kill-row world: 18 kill rows, every target has a probe set (expect rc 2 naming kill-set-size)
git -C "$D" checkout -q -f "$CAND"
python3 -B - "$D/$MAN" <<'PY' || { echo "ADD-ROW-BUILD-FAILED"; exit 0; }
import pathlib, sys
p = pathlib.Path(sys.argv[1]); text = p.read_text(encoding="utf-8")
src = [ln for ln in text.splitlines() if ln.startswith("fg-m1-expect-exit-sign-flip\t")][0]
f = src.split("\t")
f[0] = "fg-r93-extra-kill"
f[4] = "r93 added-kill-row world (scratch, not a lane commit)"
if not text.endswith("\n"):
    text += "\n"
p.write_text(text + "\t".join(f) + "\n", encoding="utf-8")
PY
git -C "$D" add -A -- "$MAN" && git -C "$D" -c user.name=scratch -c user.email=scratch@invalid commit -q -m "r93 added-kill-row world (scratch)"
R18="$(git -C "$D" rev-parse HEAD)"
( cd "$D" && python3 -B verifiers/check_mutation_battery.py --rev "$R18" --work "$S/w18" ) > "$OUT/added18.txt" 2>&1; echo "added18_rc=$?" >> "$OUT/added18.txt"
git -C "$D" checkout -q -f "$CAND"

echo DRIVER-A-DONE > "$OUT/driver-a.done"

# 3. round-92 controls-run: candidate (baseline) and m5 (kill check before the target-set check)
rm -rf "$S/ctl-cand" "$S/ctl-m5"
git clone -q --shared "$D" "$S/ctl-cand" && git -C "$S/ctl-cand" checkout -q "$CAND"
( cd "$S/ctl-cand" && bash verifiers/fixtures/round-92/controls-run.sh ) > "$OUT/controls-cand.out" 2> "$OUT/controls-cand.err"; echo "controls_rc=$?" >> "$OUT/controls-cand.out"

git clone -q --shared "$D" "$S/ctl-m5" && git -C "$S/ctl-m5" checkout -q "$CAND"
python3 -B "$S/mut.py" "$S/ctl-m5" m5 && git -C "$S/ctl-m5" add -A -- verifiers/check_mutation_battery.py \
  && git -C "$S/ctl-m5" -c user.name=scratch -c user.email=scratch@invalid commit -q -m "r93 mutant m5 (scratch)"
( cd "$S/ctl-m5" && bash verifiers/fixtures/round-92/controls-run.sh ) > "$OUT/controls-m5.out" 2> "$OUT/controls-m5.err"; echo "controls_rc=$?" >> "$OUT/controls-m5.out"

echo DRIVER-B-DONE > "$OUT/driver-b.done"
