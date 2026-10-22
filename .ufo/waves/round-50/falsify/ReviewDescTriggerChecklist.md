# ReviewDescTriggerChecklist — round 50 falsify (kotoba)

Verdict: HOLDS-BOUNDED for the judged description at 956ee1676e4c18480bce8ac3993541462be76e11 (its SKILL.md blob is identical to the one at the claims commit 542f515672306e1baefcb69ba79f1d4c18b6450e). All 8 executed trigger boxes pass at base and at judged. One box changed state: box 5, sibling arbitration, which goes from 5 of 9 to 9 of 9 non-none census lanes. Bounded by F1 (one ownership phrase is kotoba's paraphrase, not PROVINCE's wording) and F2 (the base-revision counter has no `--skill` flag, so the base figure only reproduces with the judged counter).

## 1. Verifier run (requested)

Command: `python3 -B verifiers/verify_skill_checklist.py --json`, run in the lane with cwd = lane root.
Exit 0. Summary: pass 11, fail 0, na 0, exit_code 0.

| check | status | detail |
|---|---|---|
| checklist.box_map_complete | PASS | 41 boxes mapped (8 executed, 2 delegated, 31 unexecuted); delegated verify_dispatch_prompts.py --box-proof exit 0, boxes proven 2 |
| trigger.frontmatter_parses | PASS | description 1008 chars |
| trigger.name_directory | PASS | 'kotoba-shokunin' == directory 'kotoba-shokunin' |
| trigger.literal_trigger_string | PASS | carries literal 'Triggers:' |
| trigger.anti_trigger_clause | PASS | 'Anti-triggers' present |
| trigger.no_xml_tag | PASS | 2 fields scanned |
| trigger.line_budget | PASS | 539 lines within 600 |
| trigger.no_placeholder | PASS | 495 lines scanned |
| trigger.command_binary_resolves | PASS | 9 segments; 13 subjects resolve |
| trigger.citation_resolves | PASS | 46 resolve |
| governance.citation_resolves | PASS | 954 resolve, 2 files |

Cross-checks:
- The same command in a clone pinned to 956ee, in a directory named kotoba-shokunin, with fleet-root symlinks so `../` hops resolve as in the lane: exit 0, 11 PASS. Its sorted JSON has no diff against the lane run.
- Pinned base f30464660c675d1c1e2851a3bf0366a3aaffe5a8: exit 0, 11 PASS, description 814 chars.
- A first clone named `lane` failed `name_directory` and the `../` citations. That was my scratch layout, not a judged-bytes defect, and it is not counted.

## 2. Box by box (Trigger-fidelity checklist, judged SKILL.md)

| # | Box | How checked | Base (814 chars) | Judged (1008 chars) | State |
|---|---|---|---|---|---|
| 1 | Frontmatter parses | executed trigger.frontmatter_parses | PASS | PASS | unchanged |
| 2 | name matches directory | executed trigger.name_directory | PASS | PASS | unchanged |
| 3 | literal trigger string | executed trigger.literal_trigger_string | PASS | PASS | unchanged (same 8 quoted strings + `Triggers:`) |
| 4 | anti-trigger clause | executed trigger.anti_trigger_clause | PASS | PASS | unchanged (`Anti-triggers:` clause verbatim) |
| 5 | sibling overlap named concretely, with arbitration rule | read; census counter (no executed tag) | names 5 of 9 non-none lanes | names 9 of 9, exit 0 | CHANGED: partial → full |
| 6 | body opens with role line | read | body unchanged | body unchanged | unchanged |
| 7 | prerequisites fail-closed | read | body unchanged | body unchanged | unchanged |
| 8 | decision-table action cell | read | body unchanged | body unchanged | unchanged |
| 9 | commands runnable | executed trigger.command_binary_resolves | PASS, 13 subjects | PASS, 13 subjects | unchanged |
| 10 | failure claims carry signature | read | body unchanged | body unchanged | unchanged |
| 11 | citations resolve | executed trigger.citation_resolves | PASS, 46 | PASS, 46 | unchanged |
| 12 | derivation witness for own-instrument claims | read | body unchanged | body unchanged | unchanged |
| 13 | stale-risk facts pinned | read | body unchanged | body unchanged | unchanged |
| 14 | file ≤ 600 lines | executed trigger.line_budget | PASS, 537 | PASS, 539 | unchanged (+2 lines) |
| 15 | no TODO or placeholder | executed trigger.no_placeholder | PASS, 493 lines | PASS, 495 lines | unchanged |

Box 5 detail. Base names kagi, kake, kasegi, kengaku and kumitate, with a routing rule ("fixes route to the owning lane"). Against the five names alone it passes. The census classifies nine lanes as non-none, and the base omits chousa, kama, kotodama and tameshi. Judged names all nine, and each sits in a clause with an ownership word. Which set counts as "overlapping" is an interpretation: I used the census classification, because the box does not define the set itself.

SKILL.md diff f30464660c..956ee1676e: one hunk, `@@ -7,12 +7,14 @@`, inside the frontmatter. The body is byte-identical, so the body boxes cannot have changed state.

## 3. Other description checks (all run on the PyYAML value)

- First 99 characters: identical at base and judged. First differing character is at index 474.
- Length: 1008 characters, 1014 UTF-8 bytes, cap 1024. Headroom is 16 characters.
- Literal triggers: the 8 quoted strings and the `Triggers:` label are unchanged. None lost, none added.
- Anti-trigger: `Anti-triggers:` and its clause ("general prompt engineering … reference/ tree.") are verbatim at both revisions. Judged adds `NOT kotodama-shokunin`.
- XML: no `<`, `>`, `&lt;`, `\x3c` or `\u003c` in either description.
- Third person: no I, me, my, we, us, our, you, your or yours in either description.
- No TODO, FIXME, TBD or "coming soon" in the judged description.

## 4. C1 counter (description names the non-none census lanes)

- Judged census + judged SKILL.md: exit 0. Output: "rows 20 verified 20", "province rows 20 matched 20", "skill description names 9 of 9 non-none lanes", "skill description length 1008 of 1024".
- Judged census + base SKILL.md: exit 1. Output: "names 5 of 9", "length 814 of 1024", FAIL for chousa, kama, kotodama and tameshi.
- The census classes 9 rows `adjacent` (chousa, kagi, kake, kama, kasegi, kengaku, kotodama, kumitate, tameshi) and 11 rows `none`. Those nine names match the judged description exactly.
- Q26 for the sentence "each in a clause with an ownership or routing word": the counter measures it. Rule G1 (check_sibling_census.py lines 409-462) counts a lane only when the clause that names it carries a whole-word marker (owns, own, owned, route, routes, routing, upper-case NOT, see above, as above, see also). Each of the nine judged clauses has one. The counter does not measure whether an ownership claim is true of the sibling's own bytes (see F1).

## 5. Findings

F1 — low — The kama clause is kotoba's paraphrase, not PROVINCE's or kama's wording. Judged description: "kama owns endpoint verification". PROVINCE.md § Adjacent, kama row (present at base and at judged; the judged row adds a round-50 ruling), quotes kama's split as "kama owns independent verification", and its scope is "local model serving and endpoint health". The phrase "endpoint verification" appears in no PROVINCE.md row. The router reads only the description, so this wording is what routes. No instrument checks it. The other ownership clauses match PROVINCE: chousa "research method"; tameshi "fixture and mutation method" (PROVINCE: "tameshi owns the fixture method"); kengaku "measured effects of prompt format" (PROVINCE: "kengaku keeps measured capability effects of prompt format"); kotodama "naming and language" (PROVINCE: "worldbuilding and naming"). Fix routes to kotoba and is not made here: quote PROVINCE's wording, or check kama's SKILL.md.

F2 — low — The base C1 figure cannot be reproduced with base-revision tooling. At f304646 `verifiers/check_sibling_census.py` has no `--skill` option. Running `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` there gives "unrecognized arguments: --skill SKILL.md", exit 2. The claimed "5 of 9 (exit 1)" reproduces only when the judged counter reads the base SKILL.md. The numbers hold; the claim should name the counter revision.

F3 — info — Headroom is 16 characters under the 1024 cap. One further clause of 17 or more characters fails the counter's length cap (SKILL_DESCRIPTION_MAX = 1024).

F4 — info — "fixes route to the owning lane" is generic. The concrete owner names in the same description carry the routing, so I do not count it as a defect.

F5 — info — The first-99-characters rule: the prefix is unchanged, but I did not trace where the 99-character figure is stated in the lane.

F6 — observed, outside this seat's scope — At judged, `box_map_complete` runs the delegated box proof (`verify_dispatch_prompts.py --box-proof`, exit 0, "boxes proven 2"). At base the same check reports "41 boxes mapped (8 executed, 2 delegated, 31 unexecuted)" with no proof run. It still passes. This belongs to the C2 seat and I did not analyse it.

## 6. Scope and gaps

Not covered by this seat: C2 deletion counts, D1–D6 repairs, S024–S029 and the re-opened S019/S022 rows, the census's appended round-50 sections, M31, and Q26 beyond the C1 sentence. No build, test or formatter was run.

## 7. Evidence (commands and exit codes)

- `python3 -B verifiers/verify_skill_checklist.py --json` (lane cwd): exit 0.
- Same command, pinned judged clone: exit 0. Pinned base clone: exit 0.
- `python3 -B verifiers/check_sibling_census.py … --province PROVINCE.md --skill <path>`: judged corpus + judged SKILL exit 0; judged corpus + base SKILL exit 1; base-revision script exit 2 (no `--skill`).
- My first base census attempt returned exit 2 because my persistent shell still had `set -e` from an earlier call. The rerun used `set +e`; the results above are from the rerun.
- Blob IDs: SKILL.md 3347ba41 at both 542f515 and 956ee; verifiers/checklist-baseline.json 3fa38ec6 at both.
- PyYAML 6.0.3 `safe_load` on system python3 (3.14.8): base 814 characters, 820 bytes; judged 1008 characters, 1014 bytes.

## 8. Lane and tool hygiene

- Lane writes: none from me. Runs used `-B`, and the delegated box-proof run also uses `-B` (verifier line 952). `find -newer` shows only other seats' round-50 files. Lane git status when checked: `M corpus/lessons/round-50.md`, plus untracked round-50 files from other seats.
- Scratch: /fast/scratch/hyaku/kotoba-r50/falsify/ReviewDescTriggerChecklist/ (clone at 956ee, base export at f304646, pinned trees with fleet-root symlinks).
- Tools installed or updated: none. PyYAML 6.0.3 was already present on system python3.
