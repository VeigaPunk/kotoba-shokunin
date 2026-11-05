# ReviewerRepairs — scoped findings (round 91, wave w1)

1. **HIGH (attribution, resolved before reading):** the `ExecFloorsCap_READY` and `blob.txt` I
   first observed (≈12:0x) named blob `0b29bcd0…`; at 12:15 the READY read
   `blob=6f2c52fb… selftest_N=176 rc=0`. The mid-run refresh is the builder's own correction hard
   (their item-text deviation #3). My verdicts are against the final receipt and the patch-pinned
   blob `6f2c52fb…`; apply-proof (`git apply --check` at 9af1a7a) and blob equality both re-verified.
   No rescue was made by me; the corrected receipts are what the L1 lands.

2. **HIGH (plan predicate vs landable candidate):** the plan's leg-A(predicate text)
   `SELF_TEST_TIMEOUT_S = 360` cannot pass a *bare* floors walk in isolation: the same patch bumps
   the in-file `freeze_gate` floor to 31, so without ExecLadder's patch the walk reads
   `FAIL freeze_gate observed=30 floor=31`, rc 1 (my (e) run). Conversely ExecLadder's
   `0 failure(s) over 31` alone reds the in-file floor table at 30. **The two patches are
   conjoined by construction; anyone scoring "patch A" alone will record a false red.** Landed
   candidate must be base + A + B; the two self-tests (floors 176, freeze 31) and the tip battery
   `5 of 5` must be read at that revision.

3. **MEDIUM (pin-probe attribution):** my (d) probe named `--rev 9af1a7a…` (the freeze base), so
   the `FAIL guard instrument-pin` there names `c10c0f10…` — the pre-patch blob already unpinned
   (the r90 gap). The clean-run control printed the identical FAIL before any mutation, so the
   FAIL is the pre-existing red, not my one-byte flip's effect. The mutated-blob edge was NOT
   isolated. What IS established: the guard fail-closes on a rev whose blob is unpinned, other
   guards unaffected, and the patch admits `6f2c52fb…`. The mutated-blob→FAIL and
   admitted-blob→PASS edges must be re-run at the landing rev.

4. **MEDIUM (arm count accounting):** READY text adds 9 rec-arms + 2 swap anchors (+11) to a
   claimed base 165; 165 + 11 = 176 ✓. The frozen predicate/before-receipt trail (plan § C2
   counting-before) cites `base-floors-selftest.txt` (rc 0, no count) and tipbattery-before only
   mentions `harness-selftest-duration.txt 123 assertions`. `base-floors-selftest.txt` does not
   record 165; the 165 comes from the builder's scratch at the freeze settle, which my own base
   probe (30-formula freeze gate aside) could not confirm because the base walk's per-child caps
   freeze-gate floors at 30 vs in-file 30 was not countable pre-patch without the builder's run.
   Low risk (the frozen route lands the 176 row), recorded for the LEDGER not the repair.

5. **LOW (GATE_TIMEOUT_S):** my bare floors walk at wall 223.55 s is inside the tip battery's
   `GATE_TIMEOUT_S = 280` by ~56 s at load ≈ 3.0. The builder measured 219.4 s in their probe
   (`tip-selftest.txt` shows only the self-test, their gate wall in the
   `bg_6504` transcript: 219.4 s). Under a heavier load burst the margin thins; carry risk
   noted by the L2, not repaired.

6. **LOW (review task shape):** no LSP server answered in this repo seat; all checks were
   literal reads + git plumbing, which matches the lane's documented probe affordances.
   Never presented as semantic proof.

No counter was rescued; no frozen predicate was edited; no instrument bytes changed outside my
scratch clones; no git/jj write touched the lane; scratch deleted (`/fast/scratch/hyaku/kotoba-r91/ReviewerRepairs/`).
Tool installs: none needed (stdlib-only probes; /usr/bin/time preinstalled).
