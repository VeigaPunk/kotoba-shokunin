# ExecC1HalfControls — round 67 C1 half-repair controls

Axes: calibration discrimination, verbatim evidence, scope isolation. This seat reports observations only; it does not judge C1 or admit a repair.

## Revision and worlds

The pinned base and measured source revision are both `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. In each scratch copy, `git rev-parse HEAD master` printed that hash twice. The lane tree was copied to `/tmp/k67-k2` and `/tmp/k67-k3`; all mutations and verifier runs stayed in scratch. No Git or jj write command was run.

- **K2** added exactly one coverage-map row at `corpus/README.md:124` for `lessons/round-66-verifier-spotcheck.md`. Its `verifiers/corpus-baseline.json` remained byte-identical to the lane copy (`cmp` exit 0).
- **K3** left `corpus/README.md` byte-identical to the lane copy (`cmp` exit 0; no match for the spot-check path). It re-recorded the three equal-mode baseline expectations from `python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json`: tracked files `118→119`, report total `79→82`, commit total `37→38`. The observation exited 1 because unindexed remained 1. Zero-mode expectations remain 0, as required by the gate's baseline-independent zero mode.
- Before the K2 mutation, the copied base printed `5/9 checks pass` and exited 1 with the four declared DRIFT rows, confirming the control starting point.

## Verdicts and failed conjuncts

| World | Observed primary-gate verdict | Repair conjunct still failing | Frozen C1 conjunct affected |
|---|---|---|---|
| K2: index row only | **6/9 checks pass, exit 1**; `unindexed=0` | Baseline re-record: the three equal-mode census checks still DRIFT — `tracked_files observed=119 expected=118`, `report_total observed=82 expected=79`, `commit_total observed=38 expected=37` | First conjunct (`verify_corpus_integrity.py` must print `9/9 checks pass` and exit 0) fails |
| K3: baseline only | **8/9 checks pass, exit 1**; all three equal-mode census checks now pass | Coverage-map index row: `corpus.index.unindexed observed=1 expected=0 / empty`, detail `corpus/lessons/round-66-verifier-spotcheck.md` | First conjunct fails |

Thus each half-repair remains red for its distinct missing half. The independent-verifier command, C1's second frozen conjunct, was not part of this assigned run; this report makes no observation about it.

## Exact evidence

The verbatim combined stdout/stderr and exit codes are in `controls/C1-half-controls.txt` (absolute: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-67/w1/controls/C1-half-controls.txt`). Raw scratch receipts are `/tmp/k67-k2-output.txt`, `/tmp/k67-k2-exit.txt`, `/tmp/k67-k3-output.txt`, `/tmp/k67-k3-exit.txt`; mutation diffs are `/tmp/k67-k2-mutation.diff` and `/tmp/k67-k3-mutation.diff`.

## Files changed

- Scratch only: `/tmp/k67-k2/corpus/README.md` (one row); `/tmp/k67-k3/verifiers/corpus-baseline.json` (three measured equal-mode expectations).
- Allowed seat outputs: this report and `controls/C1-half-controls.txt`.
- No production corpus, verifier, plan, source, lane Git index, or jj state was changed. No tool was installed or upgraded.

## Remaining risks and blockers

- The verifier's report/commit resolution can consult the host fleet root, so these are copied-tree controls, not fully hermetic fixtures.
- The scratch copies preserve the source revision and the two relevant starting files; unrelated in-flight wave output under copied `.ufo/` is not evidence for these verdicts.
- Blockers: none.
