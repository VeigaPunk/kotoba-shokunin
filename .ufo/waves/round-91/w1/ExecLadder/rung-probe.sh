#!/bin/bash
# rung-probe.sh <clone-root> <probe-dir>  — run every return path of check_freeze_gate.py once.
# Prints: label | rc | first stdout line | last stderr line. Read-only against the clone.
set -u
R="$1"; P="$2"; cd "$R" || exit 2
F=verifiers/check_freeze_gate.py
mkdir -p "$P"
printf '## Controls\n- control ok: echo x\n  expect: exit 0; stdout contains x\n' > "$P/ok.md"
printf '## Controls\n- control ok: true\n  expect: exit 0; stdout contains x\n' > "$P/ok-noout.md"
printf '## Controls\n- control ok: echo x\n  expect: exit 0; stdout contains x\n\xff\xfe junk\n' > "$P/nonutf8.md"
printf '## Controls\n- control same: echo a\n  expect: exit 0; stdout contains a\n- control same: echo b\n  expect: exit 0; stdout contains b\n' > "$P/dupe.md"
printf '## Controls\n- control sig: kill -9 $$\n  expect: exit 0; stdout contains x\n' > "$P/sig.md"
printf '## Controls\n- control nx: /nonexistent-cmd-xyz\n  expect: exit 127; stdout contains x\n' > "$P/nx127.md"
printf '## Controls\n- control slow: sleep 5\n  expect: exit 0; stdout contains x\n' > "$P/slow.md"
printf '## Controls\n- control two: echo x; exit 2\n  expect: exit 2; stdout contains x\n' > "$P/exit2declared.md"
printf '## Controls\n- control two: echo x; exit 2\n  expect: exit 0; stdout contains x\n' > "$P/exit2undeclared.md"
printf '## Controls\n- control np: /etc/hostname\n  expect: exit 0; stdout contains x\n' > "$P/notexec.md"
printf 'no controls here\n' > "$P/noblock.md"
printf '## Controls\n' > "$P/emptyblock.md"
printf '## Controls\n- control nocmd:\n  expect: exit 0; stdout contains x\n' > "$P/nocmd.md"
printf '## Controls\n- control a: echo x\n  expect: exit 0; stdout contains x; bogus\n' > "$P/bogusclause.md"
mkdir -p "$P/adir.md"
printf 'blocker\n' > "$P/afile"
run() {
  local label="$1"; shift
  local out rc err
  out=$("$@" 2>"$P/err.txt"); rc=$?
  err=$(tail -1 "$P/err.txt" | cut -c1-120)
  echo "[$label] rc=$rc | out1=$(printf '%s' "$out" | head -1 | cut -c1-140) | err=$err"
}
run self-test python3 -B $F --self-test
run fixture-unsat-REFUSED python3 -B $F --plan verifiers/fixtures/freeze-gate/r88-controls.md
run fixture-fixed-HELD python3 -B $F --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md
run plan-missing python3 -B $F --plan "$P/none.md"
run plan-is-directory python3 -B $F --plan "$P/adir.md"
run plan-nonutf8 python3 -B $F --plan "$P/nonutf8.md"
run no-block python3 -B $F --plan "$P/noblock.md"
run empty-block python3 -B $F --plan "$P/emptyblock.md"
run control-no-command python3 -B $F --plan "$P/nocmd.md"
run unrecognized-clause python3 -B $F --plan "$P/bogusclause.md"
run duplicate-names python3 -B $F --plan "$P/dupe.md"
run control-killed-by-signal python3 -B $F --plan "$P/sig.md"
run declared-127-missing-cmd python3 -B $F --plan "$P/nx127.md"
run timeout python3 -B $F --plan "$P/slow.md" --timeout 1
run exit2-declared-held python3 -B $F --plan "$P/exit2declared.md"
run exit2-undeclared-REFUSED python3 -B $F --plan "$P/exit2undeclared.md"
run exit126-not-executable python3 -B $F --plan "$P/notexec.md"
run work-root-under-file python3 -B $F --plan verifiers/fixtures/freeze-gate/r88-controls-fixed.md --work "$P/afile/sub"
run both-modes python3 -B $F --self-test --plan x
run no-mode python3 -B $F
run bad-timeout python3 -B $F --plan x --timeout abc
run ok-plain python3 -B $F --plan "$P/ok.md"
run ok-stdout-literal-absent-REFUSED python3 -B $F --plan "$P/ok-noout.md"
