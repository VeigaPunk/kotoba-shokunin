# CalibrationRecords — round 50 falsify (calibration count)

**Verdict: HOLDS-BOUNDED** for round-50 calibration at `956ee1676e4c18480bce8ac3993541462be76e11`. Every count the round-50 records state reproduces. **mismatches 5 of 51.** None of the five is a wrong counter value. Two are SCORECARD qualifiers spliced into the middle of an older cited shell command, which breaks that command and makes the label "Round 49 (as recorded)" untrue. The other three are wording errors: one summary line, one incomplete LOG account of the seats, and a lesson bullet that contradicts the census entry.

Seat: `KotobaR50.CalibrationRecords`, 2026-10-22T13:30Z–13:40Z. All runs were made in a private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/CalibrationRecords/` (`lane` = judged revision, `base` = `f3046466`, `t-*` = `git archive` exports). Tools installed: none.

## Findings

1. **SCORECARD:31 and :34. Each qualifier sits inside a cited command.** The D2 qualifier starts at character 2884 of line 31, between `` `sed -n '/^---$/,/^---$/p' SKILL.md `` and `` | grep -c '<skills>'` ``, inside the round-47 command. The D4 qualifier starts at character 1709 of line 34, between `` `awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' PROVINCE.md `` and `` | grep -cE '^\| (<20 lane names>) …` ``, inside the round-49 counter. If the qualifier text is cut out, the rest of each row is byte-identical to the base row, so the edit was an insertion at the first ` | ` inside a code span. Both rows' cells already contain unescaped pipes inside code spans; that is the likely cause. As a result, "**Round 49 (as recorded):**" is not as recorded, and anyone who copies either command gets prose inside a shell pipeline.
2. **SCORECARD:120** says "D4 qualifiers appended to the two rows above". One of the two is labelled D2, and neither is appended (see finding 1).
3. **LOG.md:2391** says "`FloorsRegister` and `DescDraft` were overtaken". The build spec has 33 seats, but only 29 seat reports exist in `.ufo/waves/round-50/build/`. `D2D4Wording` (scribe) and `PrecedenceDraft` (scribe) also have no report and `agentId: null` in `swarm-registry.json`, and the LOG does not mention them.
4. **corpus/lessons/round-50.md:127-129 (D4)** says the SCORECARD row "now says that kake and kasegi are `adjacent` because of kotoba's own description, not their own bytes". The census entry at the same commit (`sibling-overlap-census-round49.md:284-289`) says "Their `adjacent` class does not rest on kotoba's description alone … Basis both", and the SCORECARD qualifier itself cites the aggregator-mirrored lesson. Counterexample on the substance: at their pins, both sibling lessons read "Filed by: kotoba round-5 report … Aggregator-owned file" (kake `e73d48bb` and kasegi `1fafde8f`, lines 4-5). So the census's "both" rests on bytes that kotoba filed and the aggregator owns. Either the lesson or the census basis column is wrong. They cannot both stand, and that disagreement is for the judge to settle (impacted axes: adjacency, calibration).
5. **Bounds confirmed (they are correct, not mismatches):**
   - A false-ownership description shaped like mutant m9 (chousa, kama and tameshi each given a wrong owner phrase) still prints `9 of 9`, exit 0.
   - Relabelling `d04-placeholder` to `report_stem_is_lane_id` without deleting anything prints `boxes proven 2`, exit 0.
   - A duplicated kama row is rejected in both tables (exit 1, "appears in more than one row").
6. SHONEN.md has no round-50 statement: `git diff --quiet f3046466 956ee16 -- SHONEN.md` exits 0, and it was last touched at `f2f9ee1` (round 46). It is not counted.

**Smallest safe corrections** (to be appended in a later round, not made here):
- Move each qualifier to the end of its round's prose: on line 31 just before `**round 47 (C2`, and on line 34 just before `**round 26 —`. This restores both code spans.
- SCORECARD:120 should read "D2 and D4 qualifiers".
- LOG should name all four seats with no report.
- The lesson's D4 bullet should match the census basis, or the census should re-rule the kake and kasegi basis as `kotoba`.

## Calibration table

| # | statement (path:line) | observed at the judged revision | result |
|---|---|---|---|
| 1 | SCORECARD.md:31 `killed 0 of 6` @f3046466 → `6 of 6` @542f515 | driver: `killed 0 of 6` exit 1; `killed 6 of 6` exit 0 (also at 956ee16) | match |
| 2 | :31 kill rule (exit 1, `boxes proven` below 2, stderr names the conjunct) | `box_proof_case_deletion.py:195-206` | match |
| 3 | :31 control and N/A deletions 0 of 3 → 3 of 3 | `controls killed 0 of 2`/`na killed 0 of 1` → `2 of 2`/`1 of 1` | match |
| 4 | :31 coverage from observed statuses, one pinned co-failure | `verify_dispatch_prompts.py:130-134` `ALLOWED_CO_FAIL` | match |
| 5 | :31 checklist gate runs `--box-proof` (`checklist.box_map_complete`) | live: `delegated … --box-proof exit 0: boxes proven 2` | match |
| 6 | :31 four clauses have no fixture | manifest has 9 cases; none covers those clauses | match |
| 7 | :31 a relabel without deletion still passes | `boxes proven 2`, exit 0 | match |
| 8 | :31 D2 qualifier: round-49 proof did not enforce coverage | base driver `killed 0 of 6` | match |
| 9 | :31 "Round 49 (as recorded)" text | D2 qualifier spliced inside a cited command (finding 1) | **mismatch** |
| 10 | :34 names the 9 lanes, each in an ownership/routing clause, 1,008 of 1,024, guard 5 of 9 exit 1 → 9 of 9 exit 0 | guard output identical; clauses read | match |
| 11 | :34 lexical bound (m9 passes) | my m9-shaped mutant prints 9 of 9, exit 0 | match |
| 12 | :34 D3 rule; kama, kengaku and tameshi ruled `adjacent`; no row moves | census :246-281; PROVINCE classes identical (20 rows, 9 adjacent) | match |
| 13 | :34 duplicates rejected in either table; floored 68 | dup probes exit 1 (both tables); floors `sibling_census observed=68 floor=68` | match |
| 14 | :34 D4 qualifier content | census :284-289; sibling files at their pins | match |
| 15 | :34 "Round 49 (as recorded)" text | D4 qualifier spliced inside the round-49 counter (finding 1) | **mismatch** |
| 16 | :120 C1/C2 values; D1-D3, D5 and D6 dispositions | as in rows 1, 10 and 44-48 | match |
| 17 | :120 "D4 qualifiers appended to the two rows above" | one is D2; neither is appended | **mismatch** |
| 18 | :122 Next round 51 citations (`Kl`, `Ho`, `bq`, `S$`; G3) | `BaselineGatesB.md:34-44`; `CriticC1Sizing.md:31` | match |
| 19 | :252 move-log row, adjacency | rows 10 and 12 | match |
| 20 | :253 move-log row, operability | row 1 | match |
| 21 | LOG.md:2390 base f3046466; no earlier round-50 attempt | only 542f515 and 956ee16 carry `round-50` | match |
| 22 | :2391 33 seats: scribe 12, scout 7, executor 5, critic 3, reviewer 3, mutation-tester 2, connector 1 | `build-spec.json` Counter is identical | match |
| 23 | :2391 two seats overtaken | 4 seats with no report (finding 3) | **mismatch** |
| 24 | :2392 both counters re-sized before landing | `plans/round-50.md:66-87` | match |
| 25 | :2393 C1: 9 lanes, 1,008/1,024, first 99 characters unchanged, self-test 44 → 68 floored | parsed description common prefix 474 characters; self-tests 44 / 68 | match |
| 26 | :2393 S024-S029 written; S019/S022 byte-identical; no tie-break; rules keyed on name | 23 → 29 rows; sizes and shas agree with the rows; census :190-229 | match (records only; pages not refetched) |
| 27 | :2394 C2 driver 0→6, controls 0/2→2/2, N/A 0/1→1/1, self-test 32 → 56 | as observed | match |
| 28 | :2394 checklist self-test 1845 → 1851; floors 10 → 11, all PASS | as observed; floors exit 0 at both revisions | match |
| 29 | :2395 routed defects D1-D6 | rows 44-48 | match |
| 30 | :2396 base red (`unindexed 1`); tracked 66 → 68, report_total 43 → 44, `report_dead 2` stays | base: 4 DRIFT, `unindexed=1`; baseline diff 66→68, 43→44; judged: only `report_dead observed=2` | match |
| 31 | :2397 census exit 0, 23 → 29 rows, W04 on S018, S019 and S021 | exit 0 at base (scratch root) and at landing; same three W04 | match |
| 32 | lesson:3-7 claims and plan | plan :9-39 | match |
| 33 | lesson:17 M31 counter at 374ecf98 → 20 | 20 | match |
| 34 | lesson:17 `names kotoba` = `no` for 7 of 9 adjacent | census :70-88: 7 `no` | match |
| 35 | lesson:17 base: six removals, `killed 0 of 6` | reproduced | match |
| 36 | lesson:17 docstring stops saying "every conjunct" | base :488 and :739 say it; judged says "every one of the six named conjuncts" | match |
| 37 | lesson:19-25 Q26 exists; first plan re-sized | `QUALITY.md:37`; plan :66-87 | match |
| 38 | lesson:30-33 knowledge admitted 1; Q26 admitted | census :190; QUALITY :37 | match |
| 39 | lesson:34 and :77 S024-S029 `mined`; rows 23 → 29 | `grep -c '^| S0'` 23 → 29; status `mined` | match |
| 40 | lesson:57-62 row URLs and access times | URLs agree (S024 lists the `.md` fetch route of `/docs/skills`) | match |
| 41 | lesson:64-72 S019 42,169 B `f0a5d61b…`; S022 111,557 B `cdfcb0df…` | the same values are in the SOURCES rows | match |
| 42 | lesson:81-84 round-49.md:21-24 reads "candidates 1, admitted 1 … rejected 0" | as quoted | match |
| 43 | lesson:106-108 S011 is the only `rejected` row | 1 row, S011 | match |
| 44 | lesson:115-117 D1 line-4 pattern (seat) | `ReviewD1D5Facts.md:4,25-35` | match (the round-50 report itself is not yet filed) |
| 45 | lesson:118-122 D2 docstring, help text and gate | help names the six conjuncts; gate live | match |
| 46 | lesson:123-126 D3 mutants M1, M2, M7, M8 (before); floored 68 | `MutCensusGuardBase.md:29-38` SURVIVED; registry 68 | match |
| 47 | lesson:127-129 D4 "because of kotoba's own description, not their own bytes" | census :284-289 says "Basis both" (finding 4) | **mismatch** |
| 48 | lesson:131-134 D6: all three open at f3046466 | `CarryD6.md:8` | match |
| 49 | corpus/README.md:71 spot-check landed at f3046466 unindexed; admitted; D1-D6 | added in f304646; base `unindexed=1`; spot-check :16 and D1-D6 | match |
| 50 | README:72 lesson index entry | sections present | match |
| 51 | README:125-128 9 lanes including kotodama; guard path; six more pages | `../verifiers/check_sibling_census.py` resolves from `corpus/`; S024-S029 | match |

Excluded (forward-looking, not checkable at this revision): LOG.md:2398 "follow in the next entry".

**mismatches 5 of 51**

## Evidence (commands run in the scratch clone; exit codes as printed)

- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill ../skill-<rev>.md`: f304646 `names 5 of 9`, `length 814 of 1024`, exit 1; 542f515 and 956ee16 `9 of 9`, `1008 of 1024`, exit 0.
- `python3 -B verifiers/box_proof_case_deletion.py --rev <rev>`: f3046466 `killed 0 of 6` exit 1; 542f515 and 956ee16 `killed 6 of 6` exit 0.
- `--self-test` (base → judged): census 44 → 68, dispatch prompts 32 → 56, checklist 1845 → 1851; all exit 0 with 0 failures.
- `python3 -B verifiers/check_assertion_floors.py`: base 10 PASS exit 0; judged 11 PASS exit 0.
- `python3 -B verifiers/verify_corpus_integrity.py`: base `5/9 checks pass` (tracked 67, unindexed 1, report_total 44, report_dead 2), exit 1; judged `8/9`, DRIFT `report_dead observed=2` only, exit 1.
- `bash scripts/sources-census.sh validate --root <root> kotoba`: fleet root (lane HEAD = 956ee16) exit 0; scratch root linked to base exit 0; three W04 both times.
- Probes on copies of the judged tree:
  - m9-shaped description → `9 of 9`, exit 0.
  - Placeholder relabel → `boxes proven 2`, exit 0.
  - Duplicated kama row → exit 1 in the PROVINCE table and exit 1 in the census table.
- Splice check: a Python script cut the `**Round-50 qualifier (routed defect D2|D4):**` text out of the judged lines 31 and 34 and compared the rest with the base rows. Round-49 tail identical: True for both lines; the qualifiers sit at characters 2884-3089 (line 31) and 1709-2072 (line 34).
- `git -C <kake|kasegi> show <pin>:corpus/lessons/round-5-aggregator-mirror-*.md` lines 4-5: "Filed by: kotoba round-5 report … Aggregator-owned file".
