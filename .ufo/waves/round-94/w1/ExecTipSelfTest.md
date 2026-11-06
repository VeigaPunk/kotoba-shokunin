# ExecTipSelfTest — C2 build (round 94, r94-w1)

Seat: ExecTipSelfTest. Claim: C2 (plans/round-94.md § C2). Owned file: `verifiers/check_tip_battery.py`, `self_test()` only.
Freeze base: `edc731a91a956f6df20c27a74fb981b286f6ba58`. Candidate (scratch commit, identity `scratch <scratch@invalid>`, removed clone):
`d8088c1e847712eb3f80a0992c2de06a069db5a3`. Patch: `.ufo/waves/round-94/w1/ExecTipSelfTest/ExecTipSelfTest.patch`
(sha256 `726e15b9c617a6e690a46e6b2748428c283186223dd51568232346928e7983d7`). READY: `.ufo/waves/round-94/w1/ExecTipSelfTest_READY`.

## Change

One hunk, `@@ -721,28 +721,34 @@ def self_test()` (13 insertions, 7 deletions); no other region touched.
- Old block: two worlds (`keydrop`, `keyswap`), both dropping only `BATTERY[5]`.
- New block: six keydrop worlds (`keydrop-0`..`keydrop-5`), one per BATTERY script. Each drops ONLY its own key; the other five pins still admit their fixture blobs, so the only pin failure is the dropped path. The keyswap arm is kept unchanged in intent (drops `BATTERY[5]`, adds junk key `verifiers/r93-junk-key.py`).
- Per world, four assertions: exit 1; the line `FAIL guard instrument-pin: <that path> has no INSTRUMENT_PINS key` present; exactly one `has no INSTRUMENT_PINS key` line in the output and it starts with that path; tally reads `guards 4 of 5`. Total self-test assertions 80 → 102.
- Behavioural: each arm runs `main()` on a fixture world and reads exit code and output. No reading of instrument source text.
- Production `run_guards()` unchanged. FROZEN ANCHOR `        for path in scripts:` / `            if path not in INSTRUMENT_PINS:` matches exactly 1 time in the candidate (checked by count).

## Evidence (commands and observed lines)

- Baseline at freeze: `python3 -B verifiers/check_tip_battery.py --self-test` → `self-test: 0 failure(s) over 80 assertions`, rc 0, wall 2.9 s (`selftest-baseline.out`).
- Candidate: `self-test: 0 failure(s) over 102 assertions`, rc 0, wall 3.5 s (`selftest-after.out`). Self-test time is well under `SELF_TEST_TIMEOUT_S` (360); `check_assertion_floors.py` was NOT run by this seat (see Risks).
- Patch apply proof: fresh clone at `edc731a…`, `git apply --check` → `APPLY-CHECK-OK`; applied in that clone, self-test → `self-test: 0 failure(s) over 102 assertions`; that clone removed.
- Frozen counter `python3 -B verifiers/fixtures/round-94/selftest-kills.py c2 d8088c1e… <scratch repo>` (`counter-c2.txt`):
  - honest rc 0: `self-test: 0 failure(s) over 102 assertions`
  - `p1-one-key-hardcode` rc 1 KILLED: `FAIL pin keydrop-4 world tally reads guards 4 of 5 …; guards 5 of 5; tip battery exit 0: 6 of 6`
  - `p2-skip-first-key` rc 1 KILLED: `FAIL pin keydrop-0 world tally reads guards 4 of 5 …; guards 5 of 5`
  - `p0-skip-last-key` rc 1 KILLED: `FAIL pin keyswap world names only that key: []`
  - decoys `p1` rc 0 HELD, `p2` rc 0 HELD
  - `C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2`
  - `C2-PREDICATE-MET`, rc 0.
- Round-93 counter `bash verifiers/fixtures/round-93/c2-pinkey.sh d8088c1e… <scratch repo>` (`c2-pinkey.txt`, rc 0):
  - `honest world: instrument-pin PASS and guards 5 of 5: yes`
  - `keydrop world: check_correction_sweep.py named and guards 4 of 5: yes`
  - `keyswap world: check_correction_sweep.py named and guards 4 of 5: yes`
  - `C2-PREDICATE-MET`
- Hand world m5 (the round-93 MutTesterPinCov m5 shape): candidate with ONLY the `verifiers/check_gate_registry.py` key removed from `INSTRUMENT_PINS` (one line deleted, scratch commit `940d478a…`), run as `python3 -B verifiers/check_tip_battery.py --rev 940d478a… --repo <clone> --fleet /home/vgpnk/Projects/shokunin` (`m5-hand-world.txt`):
  - `FAIL guard instrument-pin: verifiers/check_gate_registry.py has no INSTRUMENT_PINS key (battery instrument unpinned)`
  - `fleet root /home/vgpnk/Projects/shokunin; guards 4 of 5; tip battery exit 0: 2 of 6`, rc 1.
  - The rc 1 is the carried tip-battery reds (the same carried reds read `tip battery exit 0: 3 of 6` on the unmodified candidate in c2-pinkey's honest world). The dropped key is now named by the tip battery; the m5 survivor is killed.

## Findings

1. Round-93 m5 (coverage pinned to one key) is closed: the self-test now measures all six BATTERY keys, and the counter's p1/p2/p0 mutants are each killed.
2. Pre-existing, NOT changed (out of scope): `self_test()` starts by setting the module global `INSTRUMENT_PINS = {}` and does not restore the real pin dict at the end. Harmless in a one-shot self-test process, noted for the L1.

## Risks and verification gaps

- `check_assertion_floors.py` was not run (the tip-battery self-test wall time moved 2.9 s → 3.5 s; the budget it checks is `SELF_TEST_TIMEOUT_S` 360, not changed). The reviewer seat or L1 should run it at the landing revision.
- The landing no-harm battery (`check_gate_registry.py --rev`, `check_tip_battery.py --rev`, round-92 controls, round-93 counters at the landing revision) was not run by this seat; that belongs to the main agent after integration.
- The decoy guard catches comment-appending sniffers only; the new arms are behavioural, but an AST-aware sniffer is outside the counter's reach (disclosed in the plan).
- The m5 hand world was a single run on a scratch commit, not a landing reading.

## Tools installed

None. No host setting changed. No write to the lane, fleet root, sibling lanes, or any git write in the lane. The scratch clone and all scratch dirs under `/fast/scratch/hyaku/kotoba-r94/ExecTipSelfTest` were removed before yield.
