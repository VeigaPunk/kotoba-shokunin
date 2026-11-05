# fp-exit127.md — a control that actually exits 127 and declares `exit 127` (fixture for the
# rp-exit127 probe: the declared 127 is never compared; the harness intercepts 126/127).

## Controls

- control one27: bash verifiers/fixtures/round-92-predata/sim-127.sh
  expect: exit 127; stdout contains OK
