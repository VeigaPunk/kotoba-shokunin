# Round 73 — plan addendum 3 (freeze 2: counters, controls, base readings — before C1 claim data)

Order of events this addendum records (each commit named; nothing below is a claim result):

1. **C3 landed first** (`11b05d9f43c94d9423395bd8e9edba731d8a4c8c`: `verifiers/check_tip_battery.py` anchored, guard base rebased
   to `072048f`, 69-assertion self-test, the r72 spot-check indexed in `corpus/README.md`, `verifiers/corpus-baseline.json`
   re-recorded). The E2 predicate was measured at that revision in both invocation forms with receipts committed before this
   freeze: `receipts/c3-formA-11b05d9.txt` (`--repo .`) and `receipts/c3-formB-11b05d9.txt` (absolute): both
   `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0. Shortcut worlds replayed against it:
   `receipts/c3-controls-11b05d9.txt` (none reads exit 0; w1 now fails `no-deletions` and `spotcheck-identity`). Survivors:
   `receipts/c3-mutation-rerun.txt` — 22 of 23 mutants killed; M10 survives as an equivalent mutant (unreachable: `_resolve()` raises first).
   `ExecBatteryControls` w5/w6 (a *replaced* counter) are outside the predicate and recorded as a bound (Q26): the counter is run
   from the checkout that measures, not from the revision measured.
2. **C1 counter frozen here** (`verifiers/check_cn_vendor_surfaces.py`, file sha256 `7177a7f6923789f5b180534c5cba71b08a4f04f052e358d7d750379eda5e22f9`,
   blanked sha in `SELF_SHA`; 161-assertion self-test, 0 failures), carrying E2's conjuncts (e) opened-this-round, (f) PROVINCE bullet,
   (g) registry row. Do-nothing: `receipts/c1-base-freeze.txt` (`backed 0 of 4`, exit 1). Shortcut worlds:
   `receipts/c1-controls-freeze.txt` (the seven ExecCnControls worlds, every one below 4, the tampered snapshot exit 2) plus the
   self-test's 161 assertions. The six page snapshots and `snapshots/MANIFEST.sha256` are committed with this freeze: they are the
   fetched inputs the claim cites (raw bytes re-fetched by the L1 at 2026-10-26T00:34:39Z, identical to the seat fetch), not claim content.
   The wave-1 seats whose names collided with kake r57's (`CriticC1Counter`, `CriticC3Counter`) never spawned (dispatcher keys by name);
   their attacks are re-asked in wave 2 under lane-unique names.
3. **The mined-mistake gate** `verifiers/check_report_pointers.py` (sha256 `6c382b95d0f0c2d6c90aeb7949732085b25dd8ba4502e2a7934d945bd8306f27`) is frozen
   with the tail `ExecPointersControls` D1/D3 found: it exits 0 iff `U == 0` **and** the report holds at least one blob pointer
   (`B > 0`); `M == 0` or `B == 0` is exit 2 (cannot evaluate). Red-before: `receipts/pointers-red-before.txt` — the r72 report at the r72 tip
   reads `34 of 37; unresolved 3`, exit 1, naming `tip-check_tip_battery.txt` (line 70) and `receipts/tip-check_substrate_repin_v2.txt` (line 103)
   and the r72 redaction mask `S2xx.sha256` (line 45). It is not a claim; `CriticMistakeClass` F3–F5 are met in the draft (round map for
   `receipts/`, `--round`, a fixed bare-basename ladder). Why it is a fourth resolver and not a rerun of Q36/Q50/Q60: those criteria are
   prose and `check_report_hashes.sh`/`check_r67_routed_repairs.py` scan commit hashes and one report's one arm; none resolves a
   report's path tokens against the tree at a named revision, which is the r72 miss.
4. The registry rows for the two new scripts, the entry, its six registry rows (S217–S222), the `PROVINCE.md` bullet and the other record
   text land in the C1 data commit that follows. Measured values for C1 are taken only on that commit.
