# CaseDeletionDriver — round-50 build, C2 operability counter

**Result: the C2 counter is delivered and behaves as specified — at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` it prints `killed 0 of 6` (exit 1); on a scratch instrument with observed-conjunct coverage it prints `killed 6 of 6` (exit 0), so the driver can report a kill; the lane checkout was not modified by this seat.**

## Files changed

- `verifiers/box_proof_case_deletion.py` (new, 348 lines) — the driver.
- Patch: `/fast/scratch/hyaku/kotoba-r50/build/CaseDeletionDriver/patch.diff` (unified diff against `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; `git diff --stat` → `1 file changed, 348 insertions(+)`).
- Scratch clone `/fast/scratch/hyaku/kotoba-r50/build/CaseDeletionDriver/lane` (branch `r50/c2-driver`, driver commit `5dc547e`). The mutant branches `r50/c2-mutant-coverage` / `r50/c2-mutant-broken` live only in that clone and are **not** in the patch.

## Behaviour

Usage: `python3 -B verifiers/box_proof_case_deletion.py --rev <commit>` from the lane root (`--repo DIR` overrides the source checkout; `--in-place` forces the manifest-rewrite fallback).

1. Exports the tree at `<rev>` read-only with `git archive <rev> | tar -x -C <tmpdir>` (a `tarfile` stream; stdlib only). Nothing is written in the lane. One absolute-target symlink fixture (`.ufo/round-46/drafts/r1/run-02/cases/symlinked-scope-directory-cwd/verifiers`) is skipped, because materialising it would point outside the export.
2. Reads `verifiers/fixtures/dispatch-prompts/manifest.json` from the export; runs the **intact** box proof as a control and aborts with **exit 2** unless it exits 0 (a revision whose own intact proof fails cannot be scored for case coverage).
3. Scores the **six pinned conjunct names** (denominator fixed at 6, not the manifest's FAIL count): `dispatch.04` — `report_path_literal`, `report_stem_is_lane_id`, `lane_identity_known`; `dispatch.08` — `filename_role_round_equal`, `filename_report_dir_round_equal`, `round_le_latest_dispatched`. For each conjunct the manifest entry carrying it is deleted — **the entry only, never a fixture directory** — and the revision's own instrument is re-run. A conjunct with no case at `<rev>` prints `survived (absent)`.
4. Deletes the must-pass controls (`d04-control`, `d08-control`) and the N/A case (`d08-missing-state`) in turn, scored the same way, **outside the six**.
5. **Kill criterion**: exit code exactly 1 **and** stdout carries `boxes proven 1` or `boxes proven 0` **and** stderr carries a line naming the deleted case's conjunct (for a case that declares no conjunct: its id or its box). Anything else is `survived` (the proof did not break for that case) or `error` (the instrument failed for an unrelated reason — usage/substrate error). Errors never count as kills and force a non-zero exit.
6. Output: one line per case, then `controls killed C of N`, `na killed A of M` and, as the **last line**, `killed K of 6`. Exit 0 only when K == 6 and no run errored, else 1.
7. The instrument is pointed at the temporary manifest with `--fixtures` when that revision's instrument accepts the option (it does at `f3046466`); otherwise the exported tree's own manifest is rewritten in place.

Imports: `argparse`, `json`, `shutil`, `subprocess`, `sys`, `tarfile`, `tempfile`, `pathlib` — standard library only, no new dependency.

## Evidence (commands and exit codes)

Base revision, from the scratch clone:

```
$ python3 -B verifiers/box_proof_case_deletion.py --rev f30464660c675d1c1e2851a3bf0366a3aaffe5a8
control: exit 0 boxes proven 2
fixtures: --fixtures
case d04-placeholder (report_path_literal): exit 0 survived
case d04-stem (report_stem_is_lane_id): exit 0 survived
case d04-unknown-lane (lane_identity_known): exit 0 survived
case d08-role-round (filename_role_round_equal): exit 0 survived
case d08-report-dir-round (filename_report_dir_round_equal): exit 0 survived
case d08-above-state (round_le_latest_dispatched): exit 0 survived
control d04-control: exit 0 survived
control d08-control: exit 0 survived
na d08-missing-state: exit 0 survived
controls killed 0 of 2
na killed 0 of 1
killed 0 of 6
EXIT=1
```

The same run with the real lane as the source (`--repo /home/vgpnk/Projects/shokunin/kotoba-shokunin`) gives identical output, `EXIT=1`. The control line (`boxes proven 2`) shows the base revision's own box proof passes — the 0 of 6 is C2's "before" number, not a driver failure.

**The driver can report a kill.** Scratch mutant (clone only, branch `r50/c2-mutant-coverage`, commit `55610d8`): the instrument's `box_proof` enforces *observed* coverage — it records, per box, the status each fixture case actually observed for each conjunct, and fails the proof when the case that made the observation is gone (`verifiers/fixtures/dispatch-prompts/coverage.json` anchors the observation; no manifest byte hash is compared, so an unrelated manifest edit leaves the proof passing):

```
$ python3 -B verifiers/box_proof_case_deletion.py --rev 55610d818a62a33caaa647ed5a9c898c0e542b99
control: exit 0 boxes proven 2
fixtures: --fixtures
case d04-placeholder (report_path_literal): exit 1 killed
case d04-stem (report_stem_is_lane_id): exit 1 killed
case d04-unknown-lane (lane_identity_known): exit 1 killed
case d08-role-round (filename_role_round_equal): exit 1 killed
case d08-report-dir-round (filename_report_dir_round_equal): exit 1 killed
case d08-above-state (round_le_latest_dispatched): exit 1 killed
control d04-control: exit 1 killed
control d08-control: exit 1 killed
na d08-missing-state: exit 1 killed
controls killed 2 of 2
na killed 1 of 1
killed 6 of 6
EXIT=0
```

The same mutant with `--in-place` (manifest rewritten in the exported tree instead of `--fixtures`): identical, `killed 6 of 6`, `EXIT=0`. The kill is proof-shaped, not a bare non-zero exit — stdout is `boxes proven 1` and stderr names the deleted case's conjunct:

```
$ python3 -B verifiers/verify_dispatch_prompts.py --box-proof \
    --map verifiers/checklist-baseline.json --fixtures <copy minus d04-stem>
boxes proven 1
box-proof: dispatch.04: conjunct report_stem_is_lane_id is observed by no case any more (the case 'd04-stem' is gone)
EXIT=1
```

Abort path (intact proof already failing — scratch branch `r50/c2-mutant-broken`, broken box pin):

```
$ python3 -B verifiers/box_proof_case_deletion.py --rev r50/c2-mutant-broken
control: exit 1 boxes proven 1
ERROR the intact box proof at r50/c2-mutant-broken does not exit 0; case coverage is not measurable
EXIT=2
```

Patch applies to a clean clone of the base and runs there:

```
$ git -C applytest apply --check patch.diff   →  APPLY_CHECK_OK
$ python3 -B applytest/verifiers/box_proof_case_deletion.py --repo applytest --rev f3046466...
killed 0 of 6 ; EXIT=1
$ python3 -m py_compile verifiers/box_proof_case_deletion.py   →  COMPILE_OK
```

The lane was never written to by this seat (the edits visible in `verifiers/verify_dispatch_prompts.py`, `verifiers/verify_skill_checklist.py` and `corpus/QUALITY.md` are other seats'; this seat's only lane write is this report).

## Findings for the L1

1. **The base is 0 of 6.** Deleting any of the six must-fail entries leaves the box proof at `boxes proven 2` (exit 0): the proof checks the cases the manifest still lists and never notices that a conjunct lost its case. C2's "after" state needs the instrument to enforce coverage — that is the BoxProofGate seat's file, not mine.
2. **Fixture redundancy (look before the fix is written).** The committed cases observe `report_stem_is_lane_id` as **FAIL** twice — `d04-stem` (its own case) and `d04-placeholder` (a placeholder path also breaks the stem check). A coverage rule at conjunct level ("each conjunct must be observed FAIL by some case") therefore cannot detect the deletion of `d04-stem`: with that rule alone the scratch mutant reached only `killed 5 of 6`. Coverage stated per observing case (`coverage.json`) detects all six. A real fix must pin coverage per case, make the fixtures pure (one failing conjunct per case), or both.
3. **The N/A case is load-bearing.** `d08-missing-state` is the only case observing `round_le_latest_dispatched` as `N/A`; a coverage rule demanding only FAIL observations would not notice its deletion.
4. **Not registered in `verifiers/floors-registry.json`.** Those rows carry a self-test assertion floor and a self-test output regex; the driver has no `--self-test`, so there is no floor to pin. A row would mean three coordinated edits (registry, `EXPECTED_INSTRUMENTS`, `INSTRUMENTS`) that belong to the floors seat's discipline — flagged, not done. No verifier enumerates `verifiers/*.py`, so the new file breaks no existing gate.
5. **No `corpus/SOURCES.md` row** (the driver cites no external source) and no SCORECARD edit (other seats own those files).

## Risks / blockers

- The driver requires the revision to keep `verifiers/verify_dispatch_prompts.py` and `verifiers/fixtures/dispatch-prompts/manifest.json`; a revision that renames them makes the driver exit 2 (not a score) rather than mis-score it.
- The export skips one absolute-target symlink fixture; no verifier reads it, but a future instrument that did would see a tree one link short of the checkout. The skip is stated in the driver's docstring.
- The driver reports `survived` (not `error`) when the instrument exits 1 without the proof-shaped stdout/stderr — a failure it cannot attribute to the deleted case's conjunct. That is the conservative reading of criterion (c); a future counter may prefer `error`.

## Tooling

No tool was installed or upgraded: Python 3.14.8 (stdlib only), `git`, tar via `tarfile`. No network source was opened for this item.
