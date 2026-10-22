**FAILS** (C2 as declared, before landing). `killed 6 of 6` can come from a manifest hash pin. It can also come
from a label-based coverage rule that can be laundered. The obvious "any observed FAIL" rule scores 5 of 6. A
traceback also exits 1. The 6-case deletion counter alone cannot tell these apart. The base is falsifiable:
0 of 6 holds at `f3046466`.

Seat: CriticC2Sizing (critic, operability). Base: `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Scratch:
`/fast/scratch/hyaku/kotoba-r50/build/CriticC2Sizing/` (`probe.py`, `arms.py`, `make_mutants.py`,
`make_mutants2.py`, `mutants/`). None of the mutants is a proposed patch. Measured 2026-10-22T12:28Z–12:33Z.
No tools were installed or updated.

## Findings

**F1. A hash pin produces `killed 6 of 6` (question 1). Yes, that is a problem.** I made a scratch mutant,
`mut_hash.py`, that adds one `sha256(manifest.json) == pin` test to `box_proof`. It kills all 6 deletions
(exit 1, `boxes proven 0`). It also kills edits that remove no coverage: a note edit, reordering the cases,
and deleting a case after adding its twin. The plan's statement ("deleting any one of the 6 must-fail cases
makes `--box-proof` exit 1") is literally satisfied by this pin. The milestone says the proof "enforces its
case coverage", and a pin does not do that. It enforces byte identity and blocks legitimate fixture growth.
The CaseDeletionDriver spec even suggests "a mutant that makes box_proof exit 1 on any deletion" to show the
driver can kill. That shows the driver is sensitive, not that C2 holds. Impacted axis: operability (false
provenance if 6 of 6 is cited from a non-coverage mechanism).

**F2. The obvious coverage rule scores 5 of 6, not 6 of 6 (questions 1 and 3).** `d04-placeholder` fails two
conjuncts: `report_path_literal` FAIL and `report_stem_is_lane_id` FAIL (probe output below). This is
structural. `report_paths()` (lines 131-145) returns the path segment after `round-N/` as the stem. Line 324
runs the placeholder test on that same segment, and line 362 compares it to the lane id. So a placeholder in
the report path also breaks the stem, unless the lane id itself contains `<` or `$`. I tried
`round-7/<seat>/kote.md` in a scratch copy and the stem still FAILs. Under the BoxProofCoverage wording ("a
must-fail case whose observed failing conjunct is that conjunct"), the "any observed FAIL" reading
(`mut_any.py`) leaves `delete d04-stem` alive (exit 0, `boxes proven 2`): the placeholder case covers the
stem too.

**F3. Coverage can be laundered with a relabelled copy (question 3).** Label-based coverage checked against
the observation (`mut_label.py`) scores 6 of 6 and kills a plain relabel (placeholder relabelled to stem
exits 1). But "delete `d04-stem`, then add a copy of the placeholder entry labelled `report_stem_is_lane_id`"
survives (exit 0, `boxes proven 2`). The stem conjunct is then "covered" only as a side effect of the
placeholder. A plain relabel without deletion also survives at the base (exit 0). Exact isolation, meaning
exactly one FAIL conjunct per case (`mut_isolated.py`), is unsatisfiable for `report_path_literal` (F2): the
intact proof exits 1. Isolation with one pinned co-failure exception (`mut_pinned.py`: literal may co-fail
stem only) kills all 6 deletions and both laundering arms. Twin-then-delete, note edit and reorder survive,
as they should.

**F4. 6 is the right number for the headline, but the controls and the N/A case carry weight too
(question 2).** At the base, deleting `d04-control`, `d08-control` or `d08-missing-state` each exits 0
(`boxes proven 2`). MutBoxProofBase measured the same (its `aggregate.json` uses the same manifest sha256
`af378394…`). I ran two evaluator mutants to show these cases matter:
- With the stem conjunct always FAIL (`ev_stem_always_fail.py`), the intact proof exits 1 (the control
  catches it). Delete `d04-control` and it exits 0, `boxes proven 2`: a broken evaluator is "proven".
- With missing state read as PASS (`ev_missing_state_pass.py`), the intact proof exits 1. Delete
  `d08-missing-state` and it exits 0, `boxes proven 2`. That breaks the "missing state source is never a
  pass" clause (docstring line 36).

None of the rules in F2-F3 catches this. `mut_full.py`, which adds "at least one all-PASS control per box"
and "the N/A case for `round_le_latest_dispatched`", kills all 3 (`no all-PASS control case`, `no N/A case
for conjunct round_le_latest_dispatched`). The 6 equals the existing `CONJUNCTS` constant (lines 84-90): 3
conjuncts for each box. Keep 6 as the declared C2 target, but enforce and report the 3 other cases
separately.

**F5. Exit 1 is not specific enough (question 4).** Deleting a must-fail fixture directory while keeping
its manifest entry exits **1** at the base. That exit comes from an uncaught `EnvError` traceback raised
inside `box_proof` (line 799), not from a FAIL. A driver that deletes directories, or counts any exit 1 as a
kill, prints 6 of 6 against the unmodified r49 instrument. Also, `box_proof` does not catch `EnvError`, which
contradicts the "exit 2 on substrate error" contract in the docstring (lines 45-47).

**F6. The denominator is derived from the measured revision (question 4).** The CaseDeletionDriver spec
counts "each case whose `expect_verdict` is FAIL" in the revision's own manifest, and prints `of N`. Take a
revision with 5 must-fail cases and a re-pinned or permissive instrument: it prints `killed 5 of 5` and exits
0, while the claim text says "of 6". The thing being measured should not set its own denominator.

**F7. Question 4 at the base: the claim is falsifiable, and 0 of 6 is confirmed.** All 6 deletions with the
r49 instrument exit 0 with `boxes proven 2` (table below). The statement matches the counter's arithmetic.
It is narrower than the milestone headline "box proof enforces its case coverage". Deletion alone does not
test relabelling, copies, controls or the N/A arm. This is the round-49 "headline wider than its counter"
mistake again.

**F8. Duplicate authority risk.** The BoxProofCoverage spec asks for "a constant next to the box text hashes"
listing the named conjuncts. `CONJUNCTS` (lines 84-90) already pins exactly those six names. A second list
would be a second authority that can drift. Reuse `CONJUNCTS`.

## Required changes (smallest safe set)

1. **Coverage rule (BoxProofCoverage, `verify_dispatch_prompts.py`).** For each conjunct `n` in
   `CONJUNCTS[cid]`, the box counts only if some case satisfies all of these: `expect_verdict == "FAIL"`; the
   observed verdict is FAIL; the observed `n` is FAIL; and the other observed FAIL conjuncts are a subset of
   `ALLOWED_CO_FAIL.get(n, set())`. Pin `ALLOWED_CO_FAIL = {"report_path_literal": {"report_stem_is_lane_id"}}`
   in the instrument, with a one-line reason (the placeholder is inside the stem). Check the observation, not
   the `expect_conjunct` label. Print one stderr line per uncovered conjunct, for example `box-proof:
   dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id`. Do not add a second
   conjunct list (F8).
2. **Controls and N/A (same file).** Require at least one case per box with `expect_verdict == "PASS"` whose
   observed conjuncts are all PASS. Require one `expect_verdict == "N/A"` case whose observed
   `round_le_latest_dispatched` is N/A. Each missing case gets its own stderr line.
3. **Substrate errors (same file).** Catch `EnvError` per case inside `box_proof`. Report it as a problem
   line and exit 2, never as a traceback.
4. **Driver (CaseDeletionDriver).**
   - (a) Pin the denominator to the six conjunct names, not to the manifest's FAIL count. A conjunct with no
     case at `<rev>` prints `survived (absent)`. The final line is always `killed K of 6`.
   - (b) "Delete" means removing a manifest entry, never a directory.
   - (c) A kill requires all three: exit code exactly 1, stdout `boxes proven 1` or `boxes proven 0`, and a
     stderr line that names the deleted case's conjunct. Anything else (exit 2, a traceback, or a line that
     names something else) prints `survived` or `error`.
   - (d) Print the separate lines `controls killed C of 2` and `na killed A of 1`, outside the 6.
5. **Discriminating arms, so a hash pin cannot pass.** In the driver, or as `--self-test` arms shown failing
   on the base first, require:
   - adding a twin of one must-fail case and then deleting the original exits 0;
   - a note-only edit exits 0;
   - "delete `d04-stem` plus add a placeholder copy labelled stem" exits 1.
   `mut_hash.py` fails the first two; `mut_label.py` fails the third.
6. **Claim text.** The statement may stay "deleting any one of the 6 must-fail cases … 0 of 6 → 6 of 6". The
   SCORECARD operability row and the commit subject must not say "enforces its case coverage" unless items
   1, 2 and 5 land. Otherwise say "deletion-enforced for six named conjuncts". Do not cite the driver's
   planted-mutant 6 of 6 as C2 evidence.

## Evidence (all in the scratch clone at `f3046466`; `git -C lane status --porcelain` stayed empty, exit 0)

`python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` gives
`boxes proven 2`, exit 0. `--self-test` gives `0 failure(s) over 32 assertions`, exit 0.

`python3 -B probe.py lane` (exit 0) shows these observed conjunct statuses:
- `d04-placeholder`: FAIL. `report_path_literal` FAIL, `report_stem_is_lane_id` FAIL, `lane_identity_known`
  PASS.
- `d04-stem`: FAIL on the stem only.
- `d04-unknown-lane`: `lane_identity_known` FAIL, stem N/A.
- Each of the three d08 must-fail cases fails exactly one conjunct.
- `d08-missing-state`: `round_le_latest_dispatched` N/A.

`probe.py`, deleting only the fixture directory for each of the 6 must-fail cases: exit 1 every time, with a
`Traceback` through line 799.

`python3 -B arms.py lane <instrument>` (exit 0 for every run). Each cell is the instrument's exit code and
`boxes proven` value:

| arm | base | mut_hash | mut_any | mut_label | mut_pinned | mut_full |
|---|---|---|---|---|---|---|
| intact | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 |
| delete d04-placeholder | 0 / 2 | 1 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d04-stem | 0 / 2 | 1 / 0 | **0 / 2** | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d04-unknown-lane | 0 / 2 | 1 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d08-role-round | 0 / 2 | 1 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d08-report-dir-round | 0 / 2 | 1 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d08-above-state | 0 / 2 | 1 / 0 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete d04-control | 0 / 2 | 1 / 0 | 0 / 2 | 0 / 2 | 0 / 2 | 1 / 1 |
| delete d08-control | 0 / 2 | 1 / 0 | 0 / 2 | 0 / 2 | 0 / 2 | 1 / 1 |
| delete d08-missing-state | 0 / 2 | 1 / 0 | 0 / 2 | 0 / 2 | 0 / 2 | 1 / 1 |
| relabel placeholder to stem | 0 / 2 | 1 / 0 | 0 / 2 | 1 / 1 | 1 / 1 | 1 / 1 |
| delete stem + relabelled copy | 0 / 2 | 1 / 0 | 0 / 2 | **0 / 2** | 1 / 1 | 1 / 1 |
| add twin, delete original | 0 / 2 | **1 / 0** | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 |
| edit note only | 0 / 2 | **1 / 0** | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 |
| reorder cases only | 0 / 2 | **1 / 0** | 0 / 2 | 0 / 2 | 0 / 2 | 0 / 2 |

Killed counts on the 6 must-fail deletions: base 0 of 6, `mut_hash` 6 of 6, `mut_any` 5 of 6, `mut_label`
6 of 6, `mut_pinned` 6 of 6, `mut_full` 6 of 6. The killed lines name the conjunct, for example `box-proof:
dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id`.

`mut_isolated.py` (exactly one FAIL conjunct per case): intact exits 1 with `boxes proven 1`, `no must-fail
case covers conjunct report_path_literal`. It stays that way with the placeholder rewritten to
`round-7/<seat>/kote.md`, where the stem is still FAIL.

Evaluator mutants:

| mutant | intact | delete d04-control | delete d08-missing-state |
|---|---|---|---|
| `ev_stem_always_fail` | 1 / 1 (control caught it) | **0 / 2** | 1 / 1 |
| `ev_missing_state_pass` | 1 / 1 (N/A case caught it) | 1 / 1 | **0 / 2** |

Script sha256 prefixes: `probe.py` 136399426b4bf676, `arms.py` 20787571c45c52e5, `make_mutants.py`
08ee9404d0280ce2, `make_mutants2.py` 11eae7ee1820b3c6. Mutant build commands: `python3 -B make_mutants.py lane
mutants` (exit 0) and `python3 -B make_mutants2.py lane mutants` (exit 0).
