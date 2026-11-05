# ExecPinCoverage (r93-w1 C2 build)

## Change
`verifiers/check_tip_battery.py` only:
1. `run_guards()`: when `INSTRUMENT_PINS` is non-empty, every frozen `BATTERY` script path
   not a key of `INSTRUMENT_PINS` now appends an `instrument-pin` failure naming the path:
   `verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key (battery instrument unpinned)`
   (exact detail format asserted by the new self-test). Guard count unchanged (5 guards).
2. `--self-test`: two new arms, `pin keydrop` and `pin keyswap`, each pinning every BATTERY
   script blob from the fixture except the missing key (`BATTERY[5]`, `check_correction_sweep.py`),
   swap arm adding a junk key; both assert exit 1, `FAIL guard instrument-pin: <missing> has no
   INSTRUMENT_PINS key`, and `guards 4 of 5`. Two earlier single-pin arms (already relying on an
   empty-dict "no pin" escape, pinned OK, prefix) were updated to full-pin all six scripts so
   they stay green under the new coverage; the silly `base_blob` var in the pinned-OK arm is now
   unused upstream of the rebind but harmless (left untouched to minimize diff).

## Evidence
- Base self-test (clone at 6d7eee05, before change): `python3 -B verifiers/check_tip_battery.py --self-test` → `self-test: 0 failure(s) over 74 assertions`.
- After change (candidate 72ed8d684ad3ba4a012a5e7b642234f90f239a33): `python3 -B verifiers/check_tip_battery.py --self-test` → `self-test: 0 failure(s) over 80 assertions`.
- Frozen counter (candidate, REPO=$D): `HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r93/ExecPinCoverage bash <lane>/verifiers/fixtures/round-93/c2-pinkey.sh 72ed8d68... "$D"` → `C2-PREDICATE-MET` (however the background run output was not yet retrieved at write time; see note).
- Honest control (initial background run): cap and admission conjuncts True, `guard instrument-pin PASS` (see next line for final).
- Patch: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ExecPinCoverage/ExecPinCoverage.patch` applies on fresh 6d7eee05 clone (`git apply --check` → APPLY-OK), sha256 `b14049dd7878ef28448c23e17f1b93cb47c0664adba137dbdbac8755c849cfa7`.
- Frozen counter (candidate, REPO=$D): `HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r93/ExecPinCoverage bash <lane>/verifiers/fixtures/round-93/c2-pinkey.sh 72ed8d68... "$D"` → `C2-PREDICATE-MET`, exit 0: honest `guard instrument-pin PASS`, `guards 5 of 5`, `tip battery exit 0: 3 of 6`; keydrop `FAIL guard instrument-pin: verifiers/check_correction_sweep.py has no INSTRUMENT_PINS key (battery instrument unpinned)`, `guards 4 of 5`; keyswap same missing-key FAIL plus the junk-blob FAIL, `guards 4 of 5`.
- Honest control (candidate): `HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r93/ExecPinCoverage bash verifiers/fixtures/round-92/ctl-c2-honest.sh 72ed8d68...` → `C2-PREDICATE-MET` (cap and admission conjuncts True, `guard instrument-pin PASS`).
