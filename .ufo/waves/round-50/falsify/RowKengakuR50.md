VERDICT: HOLDS-BOUNDED. Applies to the kengaku row `adjacent`, basis both (PROVINCE.md:46 and census row at corpus/knowledge/sibling-overlap-census-round49.md:78; kotoba 956ee1676e4c18480bce8ac3993541462be76e11; kengaku pin 1f3b0f1ec41ec297130e8944ff97968d32324632). The class holds on the census rule as written. The ruling's stated reasons do not hold as worded, and the ruling does not decide the one committed kengaku material on which the precedence choice would change the row.

Scope: the kengaku row and its ruling only (census entry lines 246-295; PROVINCE.md:46). C1, C2, D1-D6, S024-S029 and Q26 are not assessed here.
Lane writes: none, except this report; `.ufo/waves/round-50/falsify/` was created for it. Scratch: /fast/scratch/hyaku/kotoba-r50/falsify/RowKengakuR50/ (extracted trees, strace logs).
Tools: none installed. Used /usr/bin/strace (preinstalled). No web fetches. Disclosure: both repos were read with `git archive <rev> | tar -x`, a read-only object read that is not on the listed allow-list.

## Answers

1. Does plans/round25_census.sh read only its own lane's SKILL.md? Not on a literal reading. It reads the lane root it is run from. Its only root check is `[ -f SKILL.md ] && [ -d corpus ]` (script lines 37-38). Traced from the kengaku pin root: 87 distinct lane-root paths opened, files and directories (E6). These include SKILL.md, corpus/SOURCES.md, corpus/lessons/round-25.md, SHONEN.md, corpus/knowledge/, PROVINCE.md, SCORECARD.md, corpus/README.md, grader.py, plans/state_check.py, and corpus/evidence receipts. Opened outside the lane: none, except two environment paths (E7). Only the frontmatter count reads SKILL.md alone (awk, script line 172). If "reads only the SKILL.md" is meant to describe only that count, it is true.
2. Are the quotes verbatim? SKILL.md:3: "kotoba owns prompt and skill craft (kengaku keeps only measured capability effects)" is verbatim. README:192 contains "frontmatter triggers" verbatim, but "says only" is false: the line lists six outputs (SOURCES census, new rows, mistakes rows, SHONEN form, frontmatter triggers, both instruments' summaries) and says nothing about which files are read (E13). The kotoba-side quote, SKILL.md:13 "kengaku owns measured effects of prompt format", is verbatim.
3. Does the reasoning hold? The class holds. The first premise does not (F1). "No claim" follows from the scope-surface rule (census:47-54, wave reports excluded at :54). The ruling states that rule only in its last clause (F2).
4. Would claim-always-wins change the row? Not through the census script. Its cross-root runs are recorded only in .ufo wave reports, which census:54 excludes under either precedence. Claim-always-wins changes the row only if the corpus connector reads of kotoba's Core instruments count as audits (F5). Then the current precedence is the only thing that keeps the row adjacent, through kengaku's own SKILL.md:3 split.

## Findings (severity order)

F1 MODERATE. The ruling's premise misdescribes the script. census:271-272 and PROVINCE.md:46 both say it "reads only the SKILL.md of the lane it runs in". Measured: 87 lane-root paths (E6). Fix: "reads the lane root it runs from; its frontmatter count reads that root's SKILL.md".

F2 MODERATE. "No claim" rests on the scope-surface rule, not on the read scope. Run in a directory holding only kotoba's SKILL.md and an empty corpus/, the same script prints skill_frontmatter_triggers=8 (E5). So it does count another lane's trigger strings when pointed there. What keeps this out is census:54 ("Wave reports and run logs (`.ufo/`, `reports/`) are not scope surfaces"). The only records of cross-root runs I found are .ufo/waves/round-25/build/CensusScriptExec.md:44 and :48 (predicted kotoba 8) and .ufo/waves/round-25/falsify/RevCensusScript.md:24 (18 fleet copies). The round-49 note (census:162-165) rests on those reports and on the script's cwd reading (round-49 .ufo/waves/round-49/falsify/RowKengaku.md findings 2, lines 19-24). So the ruling's "rested on excluded wave reports" is correct. RuleKengaku.md's headline ("the premise ... is not supported by the pinned script") overstates it: the script does count another lane's triggers when run there (E5).

F3 MINOR. Citation errors. (a) README:192 "says only" (see answer 2). (b) RuleKengaku.md §2 places README:192 in the "What's here" table. It is in the plans/ table, whose header is "| File | Covers |" at README:178. The ruling cites that seat, so the error carries into its basis.

F4 MINOR. Row attribution. PROVINCE.md:46 gives "kengaku keeps measured capability effects of prompt format" as "(kengaku description, SKILL.md:3)". SKILL.md:3 says "kengaku keeps only measured capability effects". "of prompt format" comes from kengaku PROVINCE.md:30-32 and :138, and the row drops "only". "kotoba owns the craft rules" paraphrases "kotoba owns prompt and skill craft". Neither phrase is in quotation marks, so there is no verbatim failure. The citation points to the wrong line for one phrase.

F5 MODERATE. Unruled committed material, and the one place the precedence decides. Kengaku's corpus files are scope surfaces (census:47). Three connector reports read kotoba instruments that kotoba's own Core lists (judged PROVINCE.md:14: verify_harness_claims.py, verify_corpus_integrity.py):
  - corpus/evidence/round10-fleet/r10-connector.md:29 (E5: reads verifiers/verify_harness_claims.py:1-93, :502-644, :645-671), :32 (E8), and :48 (advice: do not inherit kotoba's "3 = no baseline").
  - corpus/evidence/round11-fleet/r11-connector.md:22 (describes verify_harness_claims.py:2-8 and verify_corpus_integrity.py:2-40).
The round-50 ruling never mentions them (E11). Under claim-always-wins these reads would make the row contested if they count as "auditing ... the instruments over them" (census:45-46). Under the current precedence the row stays adjacent, because kengaku's SKILL.md:3 split assigns prompt and skill craft to kotoba (census:256-260). My reading: the connectors use kotoba's instruments as design evidence for kengaku's own grader, and they audit no SKILL.md, prompt or AGENTS.md file. So they are not a claim. The ruling should say that, because it is the only route by which the precedence choice changes this row.

F6 MODERATE. A round-49 item is still open. corpus/evidence/round9-fleet/sibling-overlap.md:12 labels the kotoba relationship "**Contested** — prompt format is a treatment in kengaku experiments, while prompt construction is kotoba's province" (E10). Its last cell states the split: "Kotoba owns the craft rule and production render/trigger behavior. Kengaku owns experimental design, scoring, and claims about resulting capability." Round-49 RowKengaku.md finding 5 asked for the label to be recorded and explained. The round-50 census entry, lesson, PROVINCE.md and LOG never mention round9-fleet (E9). The rule classifies by content, so the label does not change the class. The ruling should say so.

F7 MINOR. census:47 lists "SKILL.md ..., PROVINCE.md, corpus files" as the adjacency scope surfaces. plans/, where the script lives, is not listed. The ruling could use that point; it does not. I do not rely on it here.

## What holds (verified)
- The kengaku pin commit exists (E1). The kengaku row commit matches in PROVINCE.md:46 and in the census row at census:78, and both say adjacent (E2).
- Kengaku's side of the split: SKILL.md:3, and PROVINCE.md:30-32 ("this lane keeps the *measured* effect of prompt format on capability and hands the reusable craft implication out").
- Kotoba's side of the split: SKILL.md:10-13 (judged).
- Every quote the ruling gives (census:271-276) matches the pin, except the "says only" wording in F3.

## Evidence (commands and exit codes; <S> = /fast/scratch/hyaku/kotoba-r50/falsify/RowKengakuR50)
E1 git -C /home/vgpnk/Projects/shokunin/kengaku-shokunin cat-file -t 1f3b0f1ec41ec297130e8944ff97968d32324632 → commit, exit 0.
E2 git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 956ee1676e4c18480bce8ac3993541462be76e11:PROVINCE.md | grep -n -i kengaku → line 46, exit 0.
E3 git archive <pin> | tar -x -C <S>/kengaku-pin, and the same for 956ee167 into <S>/kotoba-judged → extracted; tree listings checked.
E4 cd <S>/kengaku-pin && strace -f -qq -e trace=openat,open,access,stat,newfstatat,statx,execve,readlink -o traceA.txt sh plans/round25_census.sh → prints skill_frontmatter_triggers=6, calib_exit=0, state_check_exit=0; exit=0.
E5 cwd <S>/runB-kotoba-cwd (kotoba SKILL.md copy, empty corpus/); strace as E4 with sh <S>/kengaku-pin/plans/round25_census.sh → skill_frontmatter_triggers=8, other lane keys absent; exit=0.
E6 grep -E "^[0-9]+ +openat\(" traceA.txt | grep -v ENOENT | grep -o -E 'kengaku-pin/[^"]+' | sort -u | wc -l → 87.
E7 grep -E "^[0-9]+ +openat\(" traceA.txt | grep -v ENOENT | grep -v -E '"/(usr|lib|lib64|etc|proc|dev|sys|bin|sbin|var|run|opt)' | grep -v '"<S>/kengaku-pin' | grep -v -E 'AT_FDCWD, "[^/]' | grep -o -E '"[^"]+"' | sort -u → two paths: /home/vgpnk/.config/git/config and /home/vgpnk/.local/lib/python3.14/site-packages; exit 0.
E8 grep -rn -i kotoba corpus/evidence/round25-calibration corpus/evidence/round25-sources (kengaku pin) → no match, exit 1.
E9 grep -n -i -E "round9-fleet|sibling-overlap\.md" corpus/knowledge/sibling-overlap-census-round49.md corpus/lessons/round-50.md PROVINCE.md LOG.md (judged) → no match, exit 1.
E10 grep -n "Contested" corpus/evidence/round9-fleet/sibling-overlap.md (kengaku pin) → line 12, exit 0.
E11 grep -rn "verify_harness_claims\|verify_corpus_integrity" corpus/evidence/round10-fleet corpus/evidence/round11-fleet (kengaku pin) → r10-connector.md:21,26,29,30,32,42,57; r11-connector.md:22,57; exit 0.
E12 grep -n "verify_harness_claims\|verify_corpus_integrity" PROVINCE.md (judged) → line 14, exit 0.
E13 grep -n "frontmatter triggers" corpus/README.md (kengaku pin) → line 192, exit 0.
E14 Read (no edits): kengaku SKILL.md:3 raw and SKILL.md 1-15; kengaku PROVINCE.md:19-43 and :138; kengaku corpus/README.md:183-200; kotoba SKILL.md:1-19; kotoba PROVINCE.md:1-53; census entry 1-70, 150-190, 240-300; round-49 RowKengaku.md; round-50 RuleKengaku.md; round-25 CensusScriptExec.md:36-50 and RevCensusScript.md:15-30.
E15 Not run: verifiers/check_sibling_census.py, the mutation scripts, and the C1/C2 counters (outside this row).

## Recommended edits to the ruling (owner decides; the class stays adjacent under all six)
1. census:271-272 and PROVINCE.md:46: replace "reads only the SKILL.md of the lane it runs in" with "reads the lane root it runs from; its frontmatter count reads that root's SKILL.md".
2. census:273: replace "says only 'frontmatter triggers'" with "lists frontmatter triggers among six outputs".
3. Lead the kengaku ruling with the scope-surface rule (census:54) and say that the .ufo/waves/round-25 cross-root runs are not scope.
4. Rule the connector reads (round10-fleet/r10-connector.md:29-32 and :48; round11-fleet/r11-connector.md:22) as design evidence, not audits of kotoba surfaces.
5. Record the "Contested" label at round9-fleet/sibling-overlap.md:12, and say that the content rule gives adjacent.
6. PROVINCE.md:46: cite PROVINCE.md:30-32 for "of prompt format", not SKILL.md:3.

## Residual risk
- The class depends on the scope-surface reading (census:54). A reading that counts cwd-parameterised counters over a SKILL.md as claims makes the row contested. RuleKengaku.md §5(b) says the same.
- The census guard was not run here. Its pass would confirm only the consistency I checked by grep (E2, E12, census:78).
