# A33RecordsMatch: round 48 records against committed bytes (Q03, Q13)

Seat: KotobaR48.A33RecordsMatch (leaf). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin.
Target: LOG.md round-48 entry (LOG.md:2345-2354 at 84b9c9b); SCORECARD.md round-48 clauses at 84b9c9b (depth row :28, freshness row :32, move-log rows :201-202, planned "Round 48 completed" :110, "Next: round 49" :112).
Named commits: base 75f671b, attempt-1 c0185da, C2 d1ae458, C1 887b6af, records 84b9c9b. Lane tip at check time: eb5a80f (06:04:05 -0300), four commits after the records commit (see X2).

## Verdict: DEFECT (MEDIUM, Q03)

1. Every number and hash I re-derived in the scoped records matches committed bytes at the named commits, except one pointer: the planned clause names `.ufo/reports/round-48/kotoba.md`, which exists at no ref (X1).
2. Q13 is not met in the scoped records. No count carries a date; 13 of 17 LOG counts carry no command (X4, LOW, scope caveat).
3. The records describe 84b9c9b correctly, but master moved. Four same-identity commits after 84b9c9b changed the C2 consumer (self-test 115 to 116), rewrote the planned clauses, and edited five SOURCES rows (three old, two new). No record names those bytes (X2, MEDIUM).
4. Custody (HIGH, process; not this seat's action): fourteen tracked files were edited uncommitted in the lane between 05:54 and 06:02 -0300, and four same-identity commits landed them between 05:56 and 06:04 -0300. Falsify readings of the lane tree read a moving target (X9).

## Re-derivation at committed bytes (reproduced unless marked)

Hashes
- H1 ruler 01af33a6... = sha256 of 84b9c9b:.ufo/round-48/tools/config-root-ruler.py (full sha256 01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45). Same at 75f671b and c0185da.
- H2 oracle 1d09a38c... = sha256 of 84b9c9b:.ufo/round-48/oracle/config-root-cases.json. 13 cases.
- H3 before receipt 8bec447a... = sha256 of 84b9c9b:.ufo/round-48/verification/before-configured-root.json (first committed at 75f671b; absent at c0185da, as expected).
- H4 commit names resolve and form the claimed chain 75f671b, d1ae458, 887b6af, 84b9c9b. c0185da and 75f671b are ancestors of origin/master (checked at 2788704 and eb5a80f).
- H5 receipt revisions: before 197b5a4087bad..., after d1ae45830235c... (match SCORECARD).
- H6 consumer verifiers/verify_harness_independent.py: 872993f8... at 197b5a4 and 75f671b; d67b1b6e... at d1ae458, 887b6af, 84b9c9b. Before receipt consumer_sha256_before = 872993f8 (ok). After receipt consumer_sha256_after = d67b1b6e (ok). After receipt consumer_sha256_before = d67b1b6e (wrong, X5).
- H7 omp 18.12.6, binary sha256 85d9daf3a05fc76e... (live host binary, not a committed artifact): ok as observation.

Counts
- N1 knowledge *.md: 34 @75f671b to 35 @887b6af (exact SCORECARD command). ok.
- N2 SOURCES rows 15 to 21 (grep '^| S0'); census validate reports 21 rows. ok.
- N3 "old rows unchanged": ok @887b6af (numstat 6 insertions, 0 deletions). False @eb5a80f (X2).
- N4 corpus-baseline corpus.index.tracked_files expect 61 to 63. ok.
- N5 LOG 2343 lines @75f671b; 2354 @84b9c9b (+11, matches diff hunk +2341,14). Horizon GOVERNANCE_ERRATA_HORIZON = 2315 (verify_skill_checklist.py:377 @887b6af). ok.
- N6 lesson M24-M27 and QUALITY Q20-Q21 present @887b6af. ok.
- N7 33 seats = connector 2 + critic 2 + executor 9 + mutation-tester 2 + revenger 1 + reviewer 4 + scout 8 + scribe 5 (build-dispatch.json; 33 keys in build-assignments.json). ok.
- N8 harness self-test: 104 @75f671b; 115 @d1ae458. Both exit 0 (re-run).
- N9 registry harness_independent 104 to 115 (git diff 75f671b d1ae458). check_assertion_floors.py @d1ae458: exit 0, "PASS harness_independent observed=115 floor=115". ok.
- N10 ruler exit 1 to 0. Re-run: before at 197b5a4 exit 1, verdict failed; after at d1ae458 exit 0, verdict clean. Exit map is ruler line 327 (2 if errors, 1 if failed or mismatches, else 0). ok.
- N11 target failures 5 to 0. Same five ids fail before (re-run and committed); none after. ok.
- N12 behavioral mismatches 0 and evaluation errors 0 in both receipts. ok.
- N13 "0 non-target value or status changes": per case, committed before vs after, 0 non-target differences; the 5 target checks move 2-3 to 3-4 (oc.roots.names_plus_builtin). Re-run receipts show 0 differing cases vs committed. ok.
- N14 13-case oracle: 13 cases, 13 settled. ok.
- N15 check_substrate_pins.py exit 1, "DRIFT 2/3" @75f671b and @887b6af (re-run). ok.
- N16 verify_surfaces.py --json exit 1, pass 5 fail 2 @75f671b and @887b6af (re-run). ok.
- N17 compare_harness_independent.py --json exit 2, "false blocker" @75f671b (re-run). ok.
- N18 adjacency replay (count block of sibling-citation-routing-round16.md, HEAD frozen) exit 1 "instrument_drift" @75f671b (re-run). ok.
- N19 census validate exit 0 @75f671b (fleet-shaped copy); exit 0 @887b6af with three W04 warnings (S018, S019, S021). ok.
- N20 six authorities (S018, S017, S019, S012, S021, S020) match knowledge `source:`; verified-at 2026-10-22. ok.
- N21 SKILL.md:151 says "stricter" @75f671b and not @887b6af. ok.
- N22 "two pushed commits" (c0185da, 75f671b): ancestors of origin/master. ok.
- N23 attempt-1 "ruler, oracle and receipt hashes match committed bytes": ok @75f671b.
- N24 host: ~/.config/opencode/skill and skills both absent (live). ok.
- N25 planned line "verify_skill_checklist.py:1307-1308" holds the "stricter" string @84b9c9b. ok.
- N26 move-log before-values (34 entries; 5 @197b5a4; SKILL.md:151 "stricter"). ok.
- Result: 0 value mismatches across N1-N26 and H1-H7, except X5 (receipt label).

## Mismatches

X1 MEDIUM (Q03). SCORECARD:110 @84b9c9b reads "Report `.ufo/reports/round-48/kotoba.md`." The path is absent at 84b9c9b, at tip eb5a80f, and at every ref (`git cat-file -e` exit 128; `git log --all -- .ufo/reports/round-48` lists 0 commits). The fleet root `.ufo/reports/round-48/` holds only `kotodama.md`. The tip rewrote the sentence to "Report: the round-48 kotoba report in the fleet repository's reports tree." It still names no path or commit, and no such file exists there. Round 48 is recorded as completed with a report nobody can open.

X2 MEDIUM (Q03/M3, tip drift). Four commits after 84b9c9b, all by kotoba-shokunin <kotoba@shokunin.local>: d28b16b (05:56:07 -0300), 2788704 (05:58:57), 48819b9 (06:01:38; "C2 follow-up: an unreadable configured root contributes nothing (falsify A24; Q05), self-test arm 115->116, floor 115->116"), eb5a80f (06:04:05). At tip: consumer sha256 0f33f600...; self-test "0 failure(s) over 116 assertions", exit 0 (re-run in a private clone); registry floor 116; SCORECARD :110 and :112 rewritten; SOURCES rows S001, S003, S012, S018, S019 edited (LOG "old rows unchanged" is false at tip); QUALITY Q22-Q23 and lesson M28 added. LOG.md is byte-identical at tip, and the depth, freshness, and move-log rows are unchanged. The records are correct for d1ae458 and stale for master. No ruler receipt covers the tip consumer.

X3 LOW (Q03, evidence completeness at 84b9c9b). The commit subject says "wave-1 evidence", but 29 of 33 seat reports were committed at 84b9c9b. Four were untracked and written 05:52-05:53 -0300, ten minutes after the 05:42:44 commit: C1LiveJoinEffect.md, C1RulerNoHarmMutants.md, FrQualityCriteria.md, FrCorpusIndexNeeds.md. All four are committed at tip. Four committed reports (C1NoHarmBattery, C2SkillsRefRun, FrMistakeScribe, FrSourcesRowsScribe) were rewritten at tip (C2SkillsRefRun 134 changed lines; FrMistakeScribe 188). The 84b9c9b bytes remain retrievable via `git show 84b9c9b:<path>`.

X4 LOW (Q13; scope caveat). QUALITY.md row 24 scopes Q13 to "knowledge/lesson prose"; the rule text in CORPUS.md says "Any number in a corpus entry". LOG.md and SCORECARD.md are outside that literal scope; applied here because the assignment names it. LOG round-48 entry: 17 numeric counts; 0 in `<number> — <command> <date>` form; 0 dated; 13 with no command; 4 with a script name but no full command. SCORECARD round-48 clauses: about 20 numeric items; none dated; one (the freshness "Count:" line) names its command and separates with "@ <commit>".

X5 LOW (receipt label). `.ufo/round-48/verification/after-configured-root.json` records consumer_sha256_before = d67b1b6e (the landed consumer). Ruler line 309 sets that field from source_bytes, which is `git show <--revision>:<consumer>`. The base consumer 872993f8 is absent from the after receipt, so a reader sees before equal to after and no consumer change. The before receipt is correct. No record cites the field.

X6 LOW nit (Q03). Freshness row :32 says "at base and tip" and names no tip commit. Verified at 887b6af (exit 1, 5/7). 84b9c9b has identical verifier bytes to 887b6af. Not re-run at eb5a80f.

X7 INFO (plan, not a record claim). plans/round-48.md "L1 pre-run: exit 0, verdict clean" ran on scratch candidate 26035dc (consumer sha256 2d824c0b..., checked in /fast/scratch/hyaku/kotoba-r48-a2/cand). The landed consumer is d67b1b6e, so that pre-run describes different bytes. The plan does not claim equality.

X8 INFO (pre-existing). SCORECARD has no round-47 move-log rows (`| 47 |` count 0 @84b9c9b). Not a round-48 clause.

X9 HIGH (custody; not this seat's action). Between 08:54:12Z and 09:02:31Z (05:54-06:02 -0300), fourteen tracked files were edited in the lane working tree without a commit: SCORECARD.md, verifiers/verify_harness_independent.py, verifiers/verify_skill_checklist.py, verifiers/check_assertion_floors.py, verifiers/floors-registry.json, corpus/QUALITY.md, corpus/SOURCES.md, corpus/lessons/round-48.md, corpus/knowledge/frontmatter-rule-authorities-round48.md, PROVINCE.md, and four build reports. Between 05:56 and 06:04 -0300, four same-identity commits landed those edits plus falsify reports A14-A34. The lane master moved during the falsify wave. Each falsify verdict must name the commit it read. I could not establish who made the edits; this seat wrote nothing to the lane.

## Commands and exit codes (private clones and scratch unless noted)
- `git show <rev>:<path> | sha256sum` for H1-H3, H6 (read-only).
- Ruler, after: `--revision d1ae458... --consumer-sha256 d67b1b6e...` gave exit 0, verdict clean, 13 settled, 0 target failures. Ruler, before: `--revision 197b5a4...` gave exit 1, verdict failed, five target ids. Scratch receipts under seats2/A33RecordsMatch/ruler-*-scratch/receipt.json.
- `verify_harness_independent.py --self-test`: @75f671b exit 0 (104); @d1ae458 exit 0 (115); @eb5a80f exit 0 (116).
- `verify_harness_independent.py --json` @d1ae458 exit 0.
- `check_assertion_floors.py`: @75f671b PASS 104; @d1ae458 exit 0 PASS 115; @887b6af exit 0, 9 PASS.
- `check_substrate_pins.py` @75f671b and @887b6af: exit 1, DRIFT 2/3.
- `verify_surfaces.py --json` @75f671b and @887b6af: exit 1, pass 5 fail 2.
- `compare_harness_independent.py --json` @75f671b: exit 2, "false blocker".
- Adjacency replay @75f671b: exit 1 "instrument_drift".
- `scripts/sources-census.sh` (fleet root, read-only) on fleet-shaped copies: validate @75f671b exit 0 "ok"; validate @887b6af exit 0 with three W04; census @887b6af rows 21.
- Live host: omp/18.12.6 sha256 85d9daf3...; ~/.config/opencode/skill and skills absent; `git ls-remote origin refs/heads/master` exit 0.

## Gaps and residual risk
- Not re-derived: prose with no number (for example "kills the recursive mutant", "Verdicts belong to the non-author closure"); knowledge and lesson content beyond counts and supersedes markers; seat-report contents (A19 and A26 cover mutants).
- At tip eb5a80f I did not re-run census, pins, surfaces, or make a fresh ruler receipt. X2 is described from diffs and one self-test run.
- Host observations (omp sha, configured-root absence, live pin and surface results) can drift; they are not committed evidence.
- Lane git use was read-only: `git log`, `show`, `ls-tree`, `cat-file`, `merge-base`, `branch --contains`, `grep`, `remote -v`, `ls-remote`, and several `git status --porcelain` queries. git may refresh the .git/index stat cache during status. No lane file, ref, or index entry was written by this seat.
- Tools: none installed. Used git, python3, sha256sum, grep, awk, diff, stat, and the packaged fleet census script (read-only, run on copies). Scratch: /fast/scratch/hyaku/kotoba-r48-a2/seats2/A33RecordsMatch/.
