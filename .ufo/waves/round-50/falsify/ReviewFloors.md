HOLDS-BOUNDED — applies to the floors change f30464660c..956ee1676e (verifiers/floors-registry.json, verifiers/check_assertion_floors.py: EXPECTED_INSTRUMENTS, INSTRUMENTS, docstring, F6 anchor). All bumps are in step and the live guard is green. Two limits: the docstring side of the bump rule is not checked by anything, and F6 pins only the downward size direction.

Scope: judged bytes 956ee1676e4c18480bce8ac3993541462be76e11. Lane read-only; all writes under /fast/scratch/hyaku/kotoba-r50/falsify/ReviewFloors/. Leaf seat, no delegation. Only the floors change was reviewed; C1, C2, D1-D6, S024-S029, Q26 belong to other seats.

## Answers

1. Are all three places bumped in step (checklist 1851, dispatch_prompts 56, sibling_census 68, total 11)? Yes, at 956ee16:
   - floors-registry.json: checklist 1851, dispatch_prompts 56, sibling_census 68, instrument_total 11; 11 entries.
   - EXPECTED_INSTRUMENTS: 11 rows; checklist 1851, dispatch_prompts 56, sibling_census 68.
   - INSTRUMENTS: 11 rows; same three floors. The sibling_census row uses `self-test:\s*(\d+) failure\(s\) over (\d+) assertions`.
   - Guard docstring: same three floors, as prose. No check reads it (see F1).
   - F6 anchor (self_test, line 706): `"instrument_total": 11`. Matches.
2. Does the F6 arm still test what it claims (a size drift is caught)? Partly. It catches a total one below the entry count, and it catches deletion of the size check, but only through its class-name assertion (see F2, F3). It has no arm for a total above the entry count.

## Findings (severity order)

F1 MEDIUM — The docstring side of the bump rule is not enforced, and the rule text overclaims. Q26 instance.
- Registry $comment says: "a half-bump now fails loudly on the side that was missed". The guard docstring (lines 44-55) gives the same rule.
- Planted V8: docstring `checklist 1851` changed to `1845`, nothing else. Live run exit 0, all 11 PASS (checklist observed=1851).
- No code path reads the docstring (registry_drift, registry_anchor_drift, self_test).
- Owner options: add a docstring token check, or narrow the $comment and docstring rule to the registry and the two tables.

F2 LOW — F6 pins only the downward size direction.
- Planted V6: size check changed to `elif total < len(entries):`. `--self-test` exit 0, `0 failure(s) over 150 assertions`. The F6 downward case (10 vs 11 entries) still reds under `<`, so no arm catches the change.
- Planted V9: V6 guard plus registry total 12 (11 entries). Live run exit 1: `FAIL floors_guard observed=150 floor=150 self_test_failures=2`. The live size check printed nothing. The red comes from the stale F6 literal and the class-name assertion, not from a size arm.
- F6 assumes total equals entries. Any mismatch reds the self-test, which is why the upward case still goes red, but by accident.

F3 LOW — The F6 exit-code assertion measures exit 2, not size drift. Q26 instance.
- The F6 fixture tree holds only the guard and the registry. Every declared path therefore reports `path absent`, which also exits 2.
- Planted V7: size check deleted (`elif False:`). Self-test exit 1, `1 failure(s) over 150 assertions`. The only failing assertion is `F6 size drift: names the class`. `F6 size drift: exit 2` still passes.
- Only the class-name line measures size drift. The label "exit 2" overstates what is measured.

F4 LOW (operability) — A total change has a sixth touch point the rule does not name.
- A floor move touches: registry floor, EXPECTED_INSTRUMENTS, INSTRUMENTS, docstring. Adding or removing an instrument also touches the registry total and the F6 literal. The $comment and docstring name neither the total nor the F6 literal.
- Planted V4: registry total 12 with 11 entries. Live exit 2: `FAIL registry size drift: instrument_total=12 but 11 entries`. Self-test exit 1: `FAIL: mutation anchor lands exactly once (F6/total): got 0`. The self-test names the stale literal; the rule does not.

F5 LOW (operability, not a defect) — A failing self-test reaches the live run as a count only: `FAIL floors_guard observed=150 floor=150 self_test_failures=2` (V9). The failing arm names appear only when the guard's own `--self-test` is run in that tree. Same format for every instrument.

## Confirmed (no finding)
- Live guard in the lane exits 0. Each observed count equals its floor exactly, so one deleted assertion reds that row.
- Four single-table or registry half-bumps are caught live with exit 2 and a named class line: registry-only checklist (V1), in-file-tables-only checklist (V2), EXPECTED-only checklist (V3, two lines), registry-only sibling_census (V5).
- Total drift is caught live (V4, exit 2).
- registry_anchor_drift on judged bytes returns an empty list.

## Evidence (command, exit code)

E1 Scratch clone at judged rev: `git clone -q <lane> .../lane`; `git -C .../lane checkout -q 956ee1676e4c18480bce8ac3993541462be76e11`; rev-parse HEAD = 956ee16. Exit 0.
E2 Diff of the two files, `git --no-pager diff --no-ext-diff f30464660c 956ee16 -- <2 files>`: 2 files, +23/-13 (from --stat).
E3 Lane working copy against judged rev: `diff -rq lane/verifiers scratch/verifiers` exit 0. sha256 of lane check_assertion_floors.py a962ab8b98b5…, of floors-registry.json 2b057afcc5b5…; both equal the judged-rev blobs.
E4 Lane guard, read-only: `cd <lane> && python3 -B verifiers/check_assertion_floors.py` exit 0, wall 35.44 s, stderr empty. 11 PASS lines: harness 10/10, corpus_integrity 150/150, corpus_independent 91/91, surfaces 99/99, checklist 1851/1851, pins 62/62, harness_independent 123/123, compare_harness_independent 330/330, floors_guard 150/150, dispatch_prompts 56/56, sibling_census 68/68.
E5 Lane tree before and after E4, excluding .git .jj .ufo (`find -printf` snapshot, then `diff`): exit 0. The run wrote nothing in the lane.
E6 Scratch `python3 -B verifiers/check_assertion_floors.py --self-test` at 956ee16: exit 0, `0 failure(s) over 150 assertions`.
E7 Scratch `python3 -B -c` table count: EXPECTED rows 11, INSTRUMENTS rows 11, registry entries 11, instrument_total 11; registry_anchor_drift → []; exit 0.
E8 Stale-literal grep over verifiers/, corpus/, SCORECARD.md, SKILL.md for `checklist 1845`, `dispatch_prompts 32`, `instrument_total`, `sibling_census 6x`: hits were docstring history (lines 10-14), the EXPECTED/INSTRUMENTS rows, and the F6 literal. No stale live floor.

E9 Planted half-bumps, each in its own scratch clone of 956ee16, live guard unless noted:

| Variant | Planted change | Exit | Key output |
|---|---|---|---|
| V1 | registry checklist floor 1852 | 2 | FAIL registry floor drift: checklist registry=1852 expected=1851 row=1851 |
| V2 | EXPECTED + INSTRUMENTS checklist 1852, registry 1851 | 2 | FAIL registry floor drift: checklist registry=1851 expected=1852 row=1852 |
| V3 | EXPECTED checklist 1852 only | 2 | floor drift checklist floor=1851 expected=1852; registry floor drift ... row=1851 |
| V4 | registry total 12 | 2 (self-test 1) | size drift: instrument_total=12 but 11 entries; self-test: mutation anchor lands exactly once (F6/total): got 0 |
| V5 | registry sibling_census floor 69 | 2 | FAIL registry floor drift: sibling_census registry=69 expected=68 row=68 |
| V6 | guard `elif total < len(entries):` (self-test) | 0 | 0 failure(s) over 150 assertions |
| V7 | guard `elif False:` (self-test) | 1 | 1 failure(s); only failure: F6 size drift: names the class |
| V8 | docstring checklist 1845 only | 0 | all 11 PASS |
| V9 | V6 guard + registry total 12 | 1 | FAIL floors_guard observed=150 floor=150 self_test_failures=2 |

Planting used the `edit` tool on the scratch copies. Full runs took 35 s each.

## Tooling
Installed or upgraded: nothing. Tools used were already present: git, python3, sha256sum, diff, find, timeout.

## Residual risk and verification gaps
- The sibling_census self-test output format was checked only through the observed match (68). The regex is unanchored, like the harness row.
- I did not run an upward size drift with a fully consistent state. The self-test cannot express total above entries without going red (F2).
- Peers wrote into the lane's .ufo during my run. The lane snapshot excluded .ufo, so it does not cover those writes.
- Not checked: whether any runner or CI invokes the guard.
