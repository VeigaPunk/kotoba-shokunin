#!/bin/bash
# Extra rung probes (non-UTF-8 plan; --work under a regular file). Usage: extra_probe.sh <repo-dir> <results-tsv>
set -u
S=/fast/scratch/hyaku/kotoba-r91/RevengerLadder
REPO="$1"; RES="$2"
W="$S/work-extra"; P="$S/plans"
mkdir -p "$W" "$P"
: > "$RES"
cd "$REPO" || exit 9
GATE="python3 -B verifiers/check_freeze_gate.py"
printf '## Controls\n- control a: true\n  expect: exit 0; stdout contains x\n\xff\n' > "$P/nonutf8.md"
printf 'x' > "$W/afile"
probe() {
  local label="$1"; shift
  local out err rc first stream
  out=$(mktemp "$W/out.XXXXXX"); err=$(mktemp "$W/err.XXXXXX")
  "$@" >"$out" 2>"$err"; rc=$?
  if [ -s "$out" ]; then first=$(head -n 1 "$out"); stream=stdout
  else first=$(head -n 1 "$err"); stream=stderr; fi
  printf '%s\t%s\t%s\t%s\t%s\n' "$label" "$rc" "$stream" "$first" "$*" >> "$RES"
  rm -f "$out" "$err"
}
probe "X1-nonutf8-plan" bash -c "$GATE --plan $P/nonutf8.md --work $W"
probe "X2-work-under-file" bash -c "$GATE --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md --work $W/afile/sub"
probe "X3-selftest-rc" bash -c "$GATE --self-test"
echo "EXTRA-DONE"
