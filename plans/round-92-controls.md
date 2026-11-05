# Round 92 — pre-data controls (frozen declarations)

Executed through the round-89 capability before any candidate exists:

    python3 -B verifiers/check_freeze_gate.py --plan plans/round-92-controls.md --timeout 1200

Round 92's controls are **defect-demonstration** declarations: each expects the routed round-91
defect to be OBSERVABLE at the freeze base (`5031a78215778525a7c777116ad6f6b89acac817`), so the
freeze may proceed only when every defect this round claims to fix is real at these bytes. The
probe scripts exit 0 iff the defect is observed; the declarations below expect that observation.

Basis (all read this round): round-91 verifier spot-check routed defects 1–3;
`corpus/lessons/round-91.md` § Mistakes (`vacuous` row) and § Settlement;
`plans/round-91-addendum-1.md` A5; `.ufo/waves/round-91/w1/ExecLadder/ladder-defect.md`
F1/F2/F4 (re-derived worlds); re-observed at the round-92 base in
`.ufo/waves/round-92/receipts/redbefore-*.txt`.

## Controls

- control oldcapline-met-on-shortcut: bash verifiers/fixtures/round-91/ctl-c2-capline-only.sh
  expect: exit 0; stdout contains C2-PREDICATE-MET
- control oldmanifest-unmet-noread: bash verifiers/fixtures/round-91/ctl-c1-manifest-only.sh
  expect: exit 1; stdout contains C1-PREDICATE-UNMET
- control m6-dropped-row-green: bash verifiers/fixtures/round-92-predata/rp-m6-dropped-row.sh
  expect: exit 0; stdout contains 0 failure(s) over 25 assertions
- control workfile-uncaught-crash: bash verifiers/fixtures/round-92-predata/rp-work-regular-file.sh
  expect: exit 0; stdout contains rp-work crash observed
- control dupnames-accepted: bash verifiers/fixtures/round-92-predata/rp-duplicate-names.sh
  expect: exit 0; stdout contains rp-dup duplicate control names accepted
- control declared127-uncompared: bash verifiers/fixtures/round-92-predata/rp-exit127.sh
  expect: exit 0; stdout contains rp-127 declared exit 127 never compared
