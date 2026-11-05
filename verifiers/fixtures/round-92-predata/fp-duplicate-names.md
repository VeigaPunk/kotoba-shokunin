# fp-duplicate-names.md — two `control dup` entries, both passing (fixture for the rp-duplicate-names
# probe). Round-91 ExecLadder F1 re-derived: the gate accepts duplicate control names as valid spec
# and reads `freeze gate: 2 control(s) held` — no parse-time rejection exists.

## Controls

- control dup: bash verifiers/fixtures/round-92-predata/sim-pass.sh
  expect: exit 0; stdout contains OK
- control dup: bash verifiers/fixtures/round-92-predata/sim-pass.sh
  expect: exit 0; stdout contains OK
