**HOLDS-BOUNDED** (C2 as landed): `killed 0 of 6` at `f3046466` and `killed 6 of 6` at `542f515` and `956ee16` reproduce. The landed instrument rejects every byte-level laundering arm I tried. Four things fall outside that result, and each is a fixable defect, not a reason to reject the measurement:
(a) the counter can be laundered through manifest ids and labels, and two scratch revisions print a false `killed 6 of 6`;
(b) a hash pin placed in `main()` passes the counter, the self-test and the gate;
(c) four surfaces still say more than the counter measures (Q26);
(d) the run mode silently reports N/A for a non-digit round folder.

Seat: CriticC2Landed (critic, operability). Judged bytes: `956ee1676e4c18480bce8ac3993541462be76e11`. The verifiers are unchanged from `542f515` (`git diff --stat 542f515 956ee16 -- verifiers/` is empty). Work was done in a private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/CriticC2Landed/lane`. Scratch revisions were committed only there, and its `git status --porcelain | wc -l` printed 0 after every run. Measured from 2026-10-22T13:31Z to 13:37Z. No tools were installed or updated. The godspeed skill was read from `/fast/scratch/hyaku/kumitate-r39/src/.cursor/skills/godspeed/` because none exists under `~/.omp`.

## Findings

**F1. Q26: wording wider than the counter (impacts operability and calibration).** The counter measures six single-entry deletions. The following surfaces claim more:
- `corpus/lessons/round-50.md:120` (committed bytes) says "`--box-proof` now enforces its own case coverage (C2)". Instrument docstring `verify_dispatch_prompts.py:1005` says "what makes the proof enforce its own coverage", and the self-test comment at `:854` says the same. Neither the counter nor a cited guard turns that clause on: a relabel still passes (SCORECARD states this bound), and F3's `main()` pin also passes. The commit subject, the SCORECARD row, `SCORECARD.md:120` and `:253`, and the LOG heading all say "deletion-enforced for six named conjuncts". That wording is accurate.
- `box_proof_case_deletion.py:11` says "This driver measures that at an arbitrary revision." F2 falsifies this.
- `SKILL.md:131` and the docstring's first sentence (`:8`) still say the boxes are "*executed*". This is the M31 word. F4 shows one box clause is not executed as a failure.
- `SKILL.md:133-134` lists three clauses without a fixture. The docstring, the help text and the SCORECARD list four; SKILL.md omits the non-digit round folder.
- The manifest note says "one must-fail mutant per conjunct of dispatch.04 and dispatch.08". The boxes have clauses without fixtures, so this means only the six named conjuncts. The note is from round 49 and D2 did not touch it.

**F2. The counter can be laundered by manifest ids and labels (question 2; impacts operability through false provenance).** The landed instrument holds against every byte-level arm (table below). The counter does not. It picks the case to delete by the `expect_conjunct` label, falls back to non-FAIL holders when no labelled must-fail case exists (`pool = must_fail or holders`, line 308), and deletes every entry that shares the `id` (lines 282-285).
- **Duplicate-id twin.** Scratch revision `2fd9cad9` appends a second entry with id `d04-stem` and nothing else. The counter prints `killed 6 of 6`, exit 0. But deleting one of the two entries just restores the landed manifest, which exits 0. So the statement "deleting any one … makes `--box-proof` exit 1" is false for that manifest. The instrument accepts duplicate ids (arm "duplicate-id twin": exit 0, `boxes proven 2`).
- **Stripped label plus an unlabelled twin.** Scratch revision `715e541a` removes the label from `d08-above-state` and adds an unlabelled twin `d08-above-twin`. With `--in-place`, the counter prints `case d08-missing-state (round_le_latest_dispatched): exit 1 killed` and `killed 6 of 6`, exit 0. That sixth "kill" is the deletion of the N/A case, which is not a must-fail case. Deleting `d08-above-state` itself exits 0 (arm below).
- The same revision in the default `--fixtures` mode crashes the counter with a `FileExistsError` traceback, exit 1, and prints no `killed` line. The N/A case is attempted twice under the same work directory name (line 287). The driver's docstring promises `error` for unrelated failures, not a traceback.
- Control: scratch revision `94d877d4` adds a labelled twin first. The counter correctly prints `killed 5 of 6`.
- The landed manifest has 9 cases, 9 unique ids, 6 FAIL cases and exactly one label per conjunct. So the landed 6 of 6 is genuine.

**F3. A hash pin in `main()` is indistinguishable from coverage enforcement (question 2; this is the sizing critique's F1 again, one level up).** Scratch mutant `dc265ef0` adds a manifest sha256 check in `main()` before calling `box_proof`. On any change it prints `boxes proven 0`, names all six conjuncts and exits 1. `box_proof()` itself is untouched. Results:
- counter: `killed 6 of 6`, exit 0;
- `--self-test`: `0 failure(s) over 56 assertions`, exit 0;
- intact `--box-proof`: `boxes proven 2`, exit 0;
- gate `checklist.box_map_complete`: PASS.

Only a twin-then-delete run through the CLI exposes it: exit 1, `boxes proven 0`. A coverage rule exits 0 there. The cause: the discriminating arms (twin, note edit, relabelled copy) landed as self-test arms that call `box_proof()` directly, so they never reach the CLI path that the counter and the gate run.

**F4. The run mode does not execute the non-digit round folder clause.** A prompt with report path `/fleet/.ufo/reports/round-x/kote.md` comes back N/A on every dispatch.04 conjunct. On dispatch.08, `filename_report_dir_round_equal` is N/A and the file verdict is N/A, not FAIL, even though box `dispatch.08` (`SKILL.md:333`) requires the round token to be identical across file name, role line and report directory. The other three clauses do execute: `${LANE}` FAILs `report_path_literal`; round 7 with state 7 PASSes; round 8 with state 7 FAILs `round_le_latest_dispatched`. The new docstring bound ("not proven") is accurate. "Executed" (F1) is not.

**F5. The denominator of 6 is honestly pinned (question 3).** The counter uses its own `CONJUNCTS` tuple (lines 68-75), not the measured revision's manifest. A conjunct with no case prints `survived (absent)`. The instrument's `CONJUNCTS` is guarded by `SELF_TEST_CONJUNCTS`. That is a deliberate second copy, used as a tripwire against shrinking the list, not a second authority. Not pinned: the numerator's case selection (F2).

**F6. The D2 docstring and help text are accurate, except for the scope words in F1 (question 4).** The help text (`:532-549`), the module section (`:50-77`) and the `box_proof` docstring (`:986-1022`) name the six conjuncts, say coverage is read from observed statuses rather than labels, name the pinned co-failure, the control and the N/A requirement, and the exit 2 for substrate errors, and list four clauses without a fixture. "Every one of the six named conjuncts" is bounded and true. The gate half is wired: a revision with `--box-proof` renamed and `d04-stem` deleted turns `checklist.box_map_complete` to FAIL (exit 2, because the help text still mentions `--box-proof`).

## Smallest safe corrections
1. Counter (`box_proof_case_deletion.py`):
   - exit 2 when the manifest has duplicate ids, or when a deletion removes anything other than exactly one entry;
   - drop the `or holders` fallback, so a conjunct whose label is not on a must-fail case prints `survived (absent)`;
   - give each attempt its own work directory, using a counter index.
2. Counter: before scoring, run twin-then-delete and a note-only edit through the CLI. If either exits non-zero, print an error and do not score. This closes F3.
3. Instrument: report duplicate case ids as a problem line.
4. Wording:
   - `corpus/lessons/round-50.md:120` and `verify_dispatch_prompts.py:854` and `:1005`: replace "enforces its own (case) coverage" with "deletion-enforced for six named conjuncts";
   - counter line 11: bound "arbitrary revision" to manifests with unique ids and one labelled must-fail case per conjunct;
   - `SKILL.md:131` and docstring `:8`: bound "executed" to the six named conjuncts, and add the non-digit round folder to the `SKILL.md:133-134` list.

## Evidence (scratch clone; exit codes verbatim)
- `python3 -B verifiers/box_proof_case_deletion.py --rev <rev>`:
  - `f3046466` → `controls killed 0 of 2`, `na killed 0 of 1`, `killed 0 of 6`, exit 1;
  - `542f515` → `2 of 2`, `1 of 1`, `killed 6 of 6`, exit 0;
  - `956ee16` → the same as `542f515`, exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0. `--self-test` → `0 failure(s) over 56 assertions`, exit 0.
- `python3 -B arms.py lane` (exit 0): each arm copies the fixtures, mutates the copy and runs `--box-proof --fixtures <copy>`. Results:

| arm | exit | boxes proven | stderr (first problem) |
|---|---|---|---|
| intact | 0 | 2 | — |
| relabel placeholder to stem (no deletion) | 0 | 2 | — (the bounded residual) |
| twin with different bytes, then delete `d04-stem` | 0 | 2 | — (correct: coverage kept) |
| manifest `dir` swap, role ↔ report-dir | 1 | 1 | `conjunct filename_role_round_equal is 'PASS', expected 'FAIL'` |
| `dir` swap plus label swap | 0 | 2 | — (equivalent manifest) |
| physical directory swap | 1 | 1 | same as the manifest swap |
| edit `d04-stem` so it also fails literal | 1 | 1 | `no isolated must-fail case for conjunct report_stem_is_lane_id` |
| edit `d08-role-round` so it fails report-dir | 1 | 1 | `conjunct filename_role_round_equal is 'PASS'…` |
| duplicate-id twin of `d04-stem` | 0 | 2 | — (accepted; feeds F2) |
| strip the label from `d08-above-state` | 0 | 2 | — |
| strip the label, add an unlabelled twin, delete the original | 0 | 2 | — |
| control `dir` pointed at `d08-missing-state` | 1 | 1 | `verdict 'N/A', expected 'PASS'` |
| `d04-unknown-lane` check retagged to `dispatch.4` | 1 | 1 | `no isolated must-fail case for conjunct lane_identity_known` |

- `python3 -B mkrevs.py lane` (exit 0) built scratch revisions `2fd9cad9` (duplicate id), `715e541a` (stripped label plus twin) and `94d877d4` (labelled twin). Counter results with `--repo lane --rev <sha>`:
  - `2fd9cad9` → `killed 6 of 6`, exit 0;
  - `715e541a` → traceback, exit 1; with `--in-place` → `killed 6 of 6`, exit 0;
  - `94d877d4` → `killed 5 of 6`, exit 1.
- `python3 -B mkmutants.py lane` (exit 0) built `dc265ef0` (the `main()` pin) and `9646eaef` (`--box-proof` renamed, `d04-stem` deleted). Results:
  - `dc265ef0`: counter `killed 6 of 6`, exit 0; self-test 56 assertions, exit 0; intact proof exit 0; `verify_skill_checklist.py --json` exit 1, with `checklist.box_map_complete` PASS (its three FAILs are clone-location artefacts: `trigger.name_directory`, and two citation checks on `../.ufo/reports`); twin-then-delete exit 1, `boxes proven 0`.
  - `9646eaef`: `checklist.box_map_complete` FAIL, "failed its --box-proof (exit 2)".
- Run-mode probe, `verify_dispatch_prompts.py --prompts … --state-dir … --fleet … --json`:
  - `probe/` → exit 1; `round-x` file N/A on both boxes; the `${LANE}` file FAILs dispatch.04;
  - `probe2/` → exit 1; round 7 with state 7 PASS; round 8 FAIL.
- sha256 prefixes: `box_proof_case_deletion.py` `e09a402fd16c9311`; `verify_dispatch_prompts.py` `de9602710a67a3a5`; `arms.py` `a81847240c333c41`; `mkrevs.py` `3f8952edff3f6d9c`; `mkmutants.py` `eca93ab2a1941b41`.
