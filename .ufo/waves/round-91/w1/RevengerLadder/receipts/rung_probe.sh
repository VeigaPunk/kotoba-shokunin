#!/bin/bash
# RevengerLadder r91-w1 — freeze-gate exit-rung probe battery (base bytes 9af1a7a).
# Read-only w.r.t. the lane; all writes under $S. Public CLI only: python3 -B
# verifiers/check_freeze_gate.py ... run from the scratch clone root (cwd=$D).
set -u
S=/fast/scratch/hyaku/kotoba-r91/RevengerLadder
D="$S/repo"
W="$S/work"
P="$S/plans"
mkdir -p "$W" "$P"
RES="$S/probe-results.tsv"
: > "$RES"

cd "$D" || exit 9
GATE="python3 -B verifiers/check_freeze_gate.py"

# scratch plans reaching each rung
cat > "$P/gone.md" <<'EOF'
## Controls
- control gone: verifiers/fixtures/freeze-gate/no-such-sim-xyz.sh
  expect: exit 0; stdout contains x
EOF
cat > "$P/slow.md" <<'EOF'
## Controls
- control slow: sleep 200
  expect: exit 0; stdout contains x
EOF
printf '# not executable on purpose\n' > "$P/noexec-sim.sh"
chmod 644 "$P/noexec-sim.sh"
cat > "$P/noexec.md" <<EOF
## Controls
- control noexec: $P/noexec-sim.sh
  expect: exit 0; stdout contains x
EOF
printf '# a plan\nwith no controls section\n' > "$P/no-block.md"
printf '## Controls\n' > "$P/empty.md"
printf '## Controls\n- control broken:\n  expect: exit 0\n' > "$P/nocmd.md"
printf '## Controls\n- control a: true\n- control b: true\n  expect: exit 0\n' > "$P/noexpect.md"
printf '## Controls\n  expect: exit 0\n' > "$P/orphan.md"
printf '## Controls\n- control c: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh\n  expect: stderr contains x\n' > "$P/badclause.md"
printf '## Controls\n- control d: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh\n  expect: exit 0; stdout contains D5=PASS\nthis is prose\n' > "$P/prose.md"
printf '## Controls\n- control healed: bash verifiers/fixtures/freeze-gate/sim-w-healed.sh\n  expect: exit 0\n' > "$P/exitonly.md"

probe() {
  local label="$1"; shift
  local out err rc first
  out=$(mktemp "$W/out.XXXXXX"); err=$(mktemp "$W/err.XXXXXX")
  "$@" >"$out" 2>"$err"
  rc=$?
  if [ -s "$out" ]; then first=$(head -n 1 "$out"); stream=stdout
  else first=$(head -n 1 "$err"); stream=stderr; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$label" "$rc" "$stream" "$first" "$*" >> "$RES"
  rm -f "$out" "$err"
}

probe "A-pass-fixture"    bash -c "$GATE --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md --work $W"
probe "B-refused-fixture" bash -c "$GATE --plan verifiers/fixtures/freeze-gate/r88-controls.md --work $W"
probe "C2a-plan-missing"  bash -c "$GATE --plan verifiers/fixtures/freeze-gate/no-such-plan.md --work $W"
probe "C2b-cmd-missing"   bash -c "$GATE --plan $P/gone.md --work $W"
probe "C2c-timeout"       bash -c "$GATE --plan $P/slow.md --timeout 1 --work $W"
probe "C2d-not-exec"      bash -c "$GATE --plan $P/noexec.md --work $W"
probe "C2e-plan-is-dir"   bash -c "$GATE --plan verifiers/fixtures/freeze-gate --work $W"
probe "C3a-no-block"      bash -c "$GATE --plan $P/no-block.md --work $W"
probe "C3b-empty-block"   bash -c "$GATE --plan $P/empty.md --work $W"
probe "C3c-no-command"    bash -c "$GATE --plan $P/nocmd.md --work $W"
probe "C3d-orphan-expect" bash -c "$GATE --plan $P/orphan.md --work $W"
probe "C3e-bad-clause"    bash -c "$GATE --plan $P/badclause.md --work $W"
probe "C3f-prose-line"    bash -c "$GATE --plan $P/prose.md --work $W"
probe "C3g-exit-only"     bash -c "$GATE --plan $P/exitonly.md --work $W"
probe "C3h-no-args"       bash -c "$GATE"
probe "C3i-both-flags"    bash -c "$GATE --self-test --plan $P/empty.md"
probe "O-self-test"       bash -c "$GATE --self-test"
echo "BATTERY-DONE rc=$?"
