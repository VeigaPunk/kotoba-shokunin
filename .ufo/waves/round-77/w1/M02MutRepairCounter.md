# M02MutRepairCounter — C2 mutation probe

Axes: consistency (C2 counter behavior), calibration, coverage, operability; depth, freshness and adjacency were not changed or assessed by this mutation probe.

The frozen verifier hash matched the round-77 plan before mutation. Lane source and git state were left unchanged; all mutations were applied only to a scratch-clone copy. The clone was based at `6523aced1ee0ebe07dca996213bdc645a6acbd1e` and its top-level path was verified as `/fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone`.

Pristine baseline:

`python3 -B /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone/verifiers/check_r75_routed_repairs.py --repo /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/clone --work /fast/scratch/hyaku/kotoba-r77/M02MutRepairCounter/work --self-test`

Observed exit 0; output ended `self-test: 0 failure(s) over 27 assertions` (honest fixture closed 4/4; token-dump rejected).

I exercised 36 distinct single-point mutants, running the same `--self-test` for each. Two initial harness anchors matched more than once; I narrowed those anchors and re-ran those individual mutants, so every listed mutant has a completed self-test result. Outcomes: 14 killed (counter self-test exit 1), 22 survived (self-test exit 0), 0 inconclusive. The exact survivor line numbers, reasons and outcome details are in the build deliverable. High-impact survivors include missing exact-tip-ancestor coverage for R2, untested isolated R1 render/line-range/quote checks, under-isolated R2 transcript and live-gate failure arms, absent R3 excerpt/path/absence controls, and missing R4 settlement mutations. Disclosure only; frozen verifier not changed.

Restoration: restored-clone `--self-test` again exited 0 with `self-test: 0 failure(s) over 27 assertions`. Post-run `sha256sum` for the lane verifier, pristine backup and restored scratch verifier was identical: `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`; `cmp` of pristine backup and restored scratch verifier succeeded. No tools installed. Scratch work was removed before reporting.

VERDICT: 36 single-point mutants tested; 14 killed, 22 survived; restored bytes match frozen counter hash.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/M02MutRepairCounter.survivors.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/M02MutRepairCounter.md