HOLDS-BOUNDED — C1 census finding 4 and finding 2, plus the C2 live-run note on six `*-L1.md` prompts: the owners named are right for two of four items. One item names kotoba itself as a party (so it is not sibling-to-sibling). One item has no record that carries it to the next round. One item fails only on files that no dispatcher reads.

Seat: KotobaR49.ConnectAdjacencyRoutes (connector, leaf). Judged bytes: master at c48793dbe5eb30cd661f42ecad7399ae94e3d7ad.
Attacked: census `corpus/knowledge/sibling-overlap-census-round49.md` findings 2 and 4 (lines 110-122), `PROVINCE.md:41,44,47`, and LOG.md:2372 ("dispatch.04 FAIL on six `*-L1.md` prompts").
L0 queue read: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`, 99 lines, 75492 bytes, sha256 24f02a67…e2bb, read 2026-10-22 about 11:30Z.

## Findings, one per item

**1. kaidoku and revenger: same-domain wording.** The integrator (protocol) owns the fix. An open line already exists, so report it only.
- Both lanes claim "reverse engineering of shipped artifacts": kaidoku `PROVINCE.md:3` at 08c7a729, and revenger `PROVINCE.md:3-5` at 876630db.
- kaidoku `SKILL.md:677` at 08c7a729 says "The kaidoku/revenger dynamic-analysis boundary remains an open L0 question."
- The open line is L0 line 42, filed by `tsukuroi | round-1` (added in 79752af on 2026-10-15). It asks the integrator to "arbitrate the kaidoku/revenger shipped-artifact overlap". It has no `L0 ANSWER`: the queue holds 2 answers, at lines 52 and 53. L0 line 65 (`tabi | round-17`) is a related open line about revenger's browser and Electron runtime evidence.
- kotoba is not a party: both rows are `none`. Rule: no new line, because filing would re-flag line 42.
- Defect: census finding 4 says the item "belongs to the integrator" but does not cite L0 line 42, so a reader cannot see the question is already queued. Fix inside the lane: cite `l0-questions.md` line 42 and line 65.

**2. kagi: the unresolved owner of the opencode config.** The integrator owns the ruling. No open line exists. kotoba is a named party, so a new line is warranted (draft A).
- kagi `corpus/adjacency.tsv:81` at 899c50b4 reads `$HOME/.config/opencode integrator unresolved`. It continues: "kotoba owns the instruction/agent surface … kama owns the endpoint identity … Ruling still owed to the integrator; no fleet-ledger row currently governs this ownership question."
- kama `corpus/knowledge/cross-lane-scope.md:29` at c808ba07 says: "**Kotoba** owns the instruction/agent surface and its model/fallback wording". kotoba's own `PROVINCE.md:44` (kama row) claims the same.
- Contradiction (stated, not smoothed): census finding 4 calls this item "Sibling-to-sibling … not ruled on". `PROVINCE.md:41` says the owner "is unresolved and stays with the integrator". But kotoba's own kama row and both siblings' records name kotoba as a partial owner.
- Routing gap: the round routes the item to the integrator, but the integrator has no question to answer. Grepping the queue for `config/opencode|opencode config|instruction/agent surface` finds only L0 line 13 (`kama | round-1`, about endpoint drift, not ownership). kagi's three lines (4, 36, 90) are about other topics.

**3. kotodama → kotoba: routing is not reciprocal.** kotoba owns the fix (its own `SKILL.md` description). This is not an L0 matter; report it only.
- kotodama `SKILL.md:3` at 35f0d49f refuses prompt and skill craft by naming kotoba, and `MINT.md:20` records "kotoba owns prompt/skill craft". kotoba's description (lines 1-16) does not name kotodama: grep exit 1.
- The deferral reason is the session drift guard in `plans/round-49.md:7-9`. That is a session note, not an operator ruling, so no L0 line is needed. The queue has no line on the homonym or reciprocity (grep exit 1 on `homonym|collision|kotoba.*kotodama|kotodama.*kotoba`).
- Defect: census line 114 says the fix is "carried to the next round's plan", but no record carries it. No round-50 plan exists (`ls plans`). `corpus/lessons/round-49.md` mentions kotodama only for the classification override (line 24). In `plans/round-49.md`, kotodama appears only inside the counting commands (lines 30 and 43). The only standing hook is the phrase "does not yet name kotodama" in `PROVINCE.md:47`. Fix inside the lane: add an explicit carry line to the round-49 lesson or the closing LOG entry.

**4. The six `*-L1.md` prompts with a `<lane>` report path.** The fleet (operator or integrator) owns these files. No open line exists. A new line is warranted only to retire the files (draft B).
- The files are dead round-1 artifacts. Both live dispatchers write and read `<lane>-round-<N>.md` only: `scripts/shokunin-watchdog.sh:166,173,198,295` and `scripts/hyaku/inline.sh:99-105`. A `git grep` for `-L1.md` outside the prompts, reports and waves directories finds only `ROADMAP.md:108`, which is a historical count. All eight `*-L1.md` files were last committed in ccc7217 (2026-09-28, author `shokunin`).
- Six of them (kake, kasegi, kengaku, kotoba, kumitate, protocol) contain `.ufo/reports/round-1/<lane>.md`, one occurrence each. kagi and aggregator have none. All eight also contain the obsolete lowercase root `/home/vgpnk/projects/shokunin` (2 to 5 occurrences each).
- Second-order effect on C2: the live dispatch.04 FAIL is real in the bytes but sits on files that no dispatcher reads, so the live run will stay red until the fleet retires them. kotoba first recorded the same defect 24 days ago (`LOG.md:121`, commit 3b029b8, 2026-09-28: "`<lane>` placeholders … generator … already fixed, artifacts stale"). No L0 line was ever filed for it (grep for `<lane>|L1\.md|placeholder|dispatch\.04` matches only the queue header at line 24).
- I did not narrow the instrument's scope to turn the run green; that would hide the symptom instead of fixing it.

## Proposed move (one, bounded)

Route each item to a channel that will act on it, and touch nothing in sibling or fleet files:
1. In the lane, cite L0 lines 42 and 65 in census finding 4 for kaidoku and revenger.
2. Move the opencode item out of the "sibling-to-sibling" list. Record kotoba as a party (wording owner, per kama cross-lane-scope.md:29), and file draft A.
3. Write the kotodama carry into a lane record.
4. File draft B, so that the dispatch.04 live failure has an owner who can clear it.

Axes improved: adjacency (two items reach a queue where someone can answer them; one routing claim corrected) and operability (the C2 live failure gets a route to closure). Axes harmed: none. Both drafts are append-only lines, neither repeats an existing line, and no instrument or classification changes. The `none`/`adjacent` counts stay at 7 adjacent and 13 none.

Draft L0 lines (at most two; neither repeats an existing line):

A. `kotoba | round-49 | Who owns $HOME/.config/opencode as a group? kagi records owner=integrator, status=unresolved (kagi-shokunin corpus/adjacency.tsv:81 at 899c50b4) and no line in this queue names it. A per-surface split already exists in kama-shokunin corpus/knowledge/cross-lane-scope.md:12-13,29 (c808ba07): kotoba owns agent and instruction wording including model and fallback claims, kama the endpoint truth, kagi credential and request hygiene, the operator the provider declaration. Ratify that split as the answer, or name one owner for edits to opencode.json provider blocks? Until ruled, kotoba claims only the wording and edits nothing under that path.`

B. `kotoba | round-49 | Retire the eight round-1 .ufo/prompts/*-L1.md files (last commit ccc7217, 2026-09-28)? No dispatcher reads them: scripts/shokunin-watchdog.sh:173 and scripts/hyaku/inline.sh:99 write and read <lane>-round-<N>.md only. Six (kake, kasegi, kengaku, kotoba, kumitate, protocol) still carry the report path .ufo/reports/round-1/<lane>.md and all eight the old lowercase root /home/vgpnk/projects/shokunin, so kotoba verifiers/verify_dispatch_prompts.py fails dispatch.04 on them on every live run. Fleet-owned files; kotoba records the failure and edits nothing there.`

## Risks

- Draft B is cleanup-grade. The integrator may rule that kotoba should exclude unreferenced files from the instrument instead. If so, that is a scoping change the round must declare, not a silent filter.
- Draft A asks the integrator to rule on a partition that three lanes already practise. If the answer is "the split stands", the line still closes kagi's `unresolved` row.
- Appending to the fleet L0 file is a write outside the lane. The round-22 append is the recorded precedent (LOG.md:1335). This seat did not append.

## Evidence (all read-only on the lane and fleet; the one write was to the scratch directory)

- `wc -lc .ufo/l0-questions.md; sha256sum …` → 99 lines, 75492 bytes, 24f02a6792bf…e2bb, exit 0.
- `grep -n -iE 'kaidoku|revenger|reverse engineering|opencode|kotodama|<lane>|L1\.md|placeholder|dispatch\.04' .ufo/l0-questions.md` → lines 10,12,13,15,24,42,44-48,51-53,56,57,65,71,94,96,98, exit 0. None is an ownership line for opencode, `<lane>` or kotodama↔kotoba.
- `grep -c 'L0 ANSWER' .ufo/l0-questions.md` → 2. `sed -n 42p … | grep -c ANSWER` → 0.
- `git log -S'arbitrate the kaidoku/revenger' -- .ufo/l0-questions.md` → 79752af 2026-10-15 09:00:09 -0300.
- `grep -l -F '<lane>' .ufo/prompts/*-L1.md` → 6 files, exit 0. Per-file `grep -c -F '.ufo/reports/round-1/<lane>.md'` → 1,1,1,1,1,1,0,0. Lowercase root counts → 3,5,3,3,3,5,2,2.
- `grep -n -E 'prompts/|L1\.md' scripts/shokunin-watchdog.sh scripts/hyaku/inline.sh scripts/hyaku/closure-prompt.md` → only `<lane>-round-<n>.md` patterns, exit 0.
- `git grep -n -F -- '-L1.md' -- ':!.ufo/prompts' ':!.ufo/reports' ':!.ufo/waves'` → ROADMAP.md:108 only, exit 0.
- `git -C kagi-shokunin show 899c50b4…:corpus/adjacency.tsv | sed -n 81p`, `git -C kama-shokunin show c808ba07…:corpus/knowledge/cross-lane-scope.md | sed -n '12,13p;29p'`, `git -C kaidoku-shokunin show 08c7a729…:SKILL.md | sed -n 677p`, `git -C revenger-shokunin show 876630db…:PROVINCE.md | sed -n 1,8p` → quoted above, all exit 0.
- `git show c48793db:SKILL.md | sed -n 1,16p | grep -iE 'opencode|kotodama'` → exit 1 (no match).
- Scratch clone at /fast/scratch/hyaku/kotoba-r49/falsify/ConnectAdjacencyRoutes/clone, checked out at c48793db, ran `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20`, `province rows 20 matched 20`, exit 0. The guard passes, so none of the findings above is caught by it: they concern routing prose, not quotes or pins.

Tools installed or updated: none.
