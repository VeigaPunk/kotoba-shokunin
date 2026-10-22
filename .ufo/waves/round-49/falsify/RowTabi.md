VERDICT: FAILS for the `tabi` classification `none` (census row, and the matching PROVINCE § Adjacent row at kotoba c48793db). Commit, branch, scope quote and both mechanical columns HOLD. The PROVINCE tabi note HOLDS-BOUNDED.

Under the literal rule (SKILL.md, PROVINCE.md, corpus files only), `none` would stand. It fails because the sweep that certifies `none` is false as written, and the split it misses sits in tabi's committed round-16 wave drafts: the blind spot that census Limits name (census :131-133).

Scope: leaf seat, read-only, no subagents. Pin: tabi-shokunin e3cf4e0d30bb835532ff44b118c5ad52e09eb76d. Judged bytes: kotoba master c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. Private clone for the guard: /fast/scratch/hyaku/kotoba-r49/falsify/RowTabi/kotoba. No tools installed or upgraded.

## Findings

1. HIGH. Tabi's committed record states a split with kotoba, and `none` misses it.
   - `.ufo/waves/round-16/drafts/DraftAdjacency.md:39` (at pin, authored by a tabi seat, line 3): "C-C — tool names, descriptions and schemas as agent-facing text. These are prompt-like strings read by a model. kotoba owns the craft of such text … tabi records the observed text verbatim and its shape; it does not grade wording. Route craft findings to kotoba."
   - Same file line 13 labels the row "kotoba (prompt/skill craft) — contested (C-C)". `.ufo/waves/round-16/w1/DraftAdjacency.md:11,30` repeats the split ("kotoba craft … tabi records shape only").
   - This is a split of one function between tabi and kotoba, which is what census :47-48 calls `adjacent`. The right label is `adjacent`, not `contested`: section 3 of the same draft gives tabi no craft claim.
   - Never landed or ruled. `corpus/lessons/round-16-verifier-spotcheck.md:138-150` rules C-A only; `kotoba` has no hit in corpus/lessons; tabi PROVINCE.md, SKILL.md and corpus/adjacency.tsv carry no kotoba split (0 kotoba rows).
   - Counter-reading: a wave draft is not a "scope surface" under the parenthesis. Against that, census :131-133 says `none` rests on a sweep, and "a claim stated only in an unread wave report would be missed." This claim sits in a wave report. The round must either rule drafts out and say so, or reclassify.
   - Build report CensusTabi.md:94 says "Zero of those [`.ufo` wave specs/receipts, corpus, scripts, LOG.md] state a rule over skill/prompt authoring for another lane." That is false for DraftAdjacency.md:39. The build report never mentions the round-16 drafts.
   - Kotoba side is corroborating, not a split: kotoba PROVINCE.md:23 (Frontier) lists "MCP/plugin instruction surfaces", the surface where WebMCP tool text sits.

2. MEDIUM. A second kotoba leg sits in the same substrate, and tabi's adjacency map quotes the clause without it.
   - kumitate SCORECARD, tabi-cited pin 1770305f :1553-1559, and census pin fac39171 :1612-1618: "`plugins/managed/kimi-webbridge` internals route to tabi … `skills/*` craft and trigger discipline to kotoba."
   - `.ufo/waves/round-17/w2/AdjRow9.md:55` quotes the kotoba leg. `corpus/adjacency.tsv` row 10 (kumitate, `split-declared`) quotes only the tabi and kaidoku legs.
   - The glob means user skills: kumitate fac39171 SCORECARD.md:706 reads `~/.kimi-code/skills/` (godspeed, reverse-engineer-anything, shokunin, ufo, wwkd). So the kotoba leg does not cover tabi's plugin SKILL.md (`plugins/managed/kimi-webbridge/skills/kimi-webbridge/SKILL.md`, cited at tabi SKILL.md:211,417,580,677,1414). The overlap is in kind (trigger discipline), not in artifact. This supports `adjacent`; it does not decide it alone, and neither lane's scope surface states it.

3. MEDIUM. The build seat's reason for rejecting `adjacent` on the plugin-loader touchpoint uses a test the rule does not contain.
   - CensusTabi.md:52-53: "being a disjoint split … not a shared boundary either — hence `none`, not `adjacent`." Census :47-48 asks whether a split is stated. It does not ask for a shared boundary. The touchpoint `corpus/knowledge/webbridge-plugin-anatomy.md:50-55` states no kotoba split, so this row's outcome is not changed by it; the reasoning is wrong.

4. LOW. Build report count is wrong. CensusTabi.md:41-42 says the adjacency map has "9 rows … 11 lines incl. header+comment." Actual: 11 lines, 10 data rows (kagi 2, kaidoku 2, kake 2, revenger 2, kama 1, kumitate 1), no comment line.

5. The guard passes and cannot test the claim. In the private clone at c48793db it exits 0 with "rows 20 verified 20" and "province rows 20 matched 20". It checks a 40-hex commit, the enum {contested, adjacent, none}, quotes within ±2 lines (LINE_TOLERANCE = 2), and census/PROVINCE agreement. A wrong `none` passes. A reclassification must change four places together: census row :80; census counts :93 (7 adjacent / 13 none, to 8 / 12); PROVINCE kotoba :54; and the count commands at plans/round-49.md:30,43.

6. PROVINCE tabi note, kotoba PROVINCE.md:54: `| tabi | none | e3cf4e0d… | browser and web-interaction craft; no claim on kotoba ground |`
   - Commit: matches the pin. HOLDS.
   - "browser and web-interaction craft": tabi PROVINCE.md:3-4 says "browser & web-interaction craft". HOLDS (paraphrase).
   - "none": matches the census; disputed by finding 1.
   - "no claim on kotoba ground": tabi's own scope (PROVINCE.md:6-19) makes no craft claim. But the note cites no line, and it omits the C-C split and the kumitate leg. HOLDS-BOUNDED.

## What holds (attacked, not broken)
- Pin and branch. `git -C tabi-shokunin rev-parse master` → e3cf4e0d…76d, rc 0. `cat-file -t` → commit, rc 0. `merge-base --is-ancestor e3cf4e0 master` → rc 0. `for-each-ref refs/heads refs/remotes` → master, origin/master, origin and hyaku/s3-tabi22-fresh-review, all at e3cf4e0. `symbolic-ref -q HEAD` → rc 1 (detached). Branch cell `master`: right.
- Quote. `git show e3cf4e0:PROVINCE.md | tr '\n' ' ' | grep -c -F "browser & web-interaction craft (旅, journey) — driving real browsers against real sites with evidence discipline."` → 1, rc 0. Source lines 3 and 4 (break after "real"). Census :3 is inside the ±2 tolerance.
- Mechanical columns. SKILL.md:3 description: "Domain specialist — browser & web-interaction craft. Rank: shonen (probation)." Case-insensitive whole-token grep for the 20 sibling names plus `kotoba` → no match, rc 1. "names kotoba: no" and "arbitration: no" are right.
- Governing docs (SKILL, PROVINCE, AGENTS, README, MINT, SHONEN, SCORECARD), `git grep -c -i`: `prompt` 0, `AGENTS\.md` 0, `frontmatter` 0, `kotoba` 2 (SKILL.md:1313 and :1450, watchdog roster).
- Tree-wide `git grep -n -i kotoba e3cf4e0`, rc 0: every hit read. Roster strings; `.ufo` round 16–22 wave files; no other split statement.
- scripts: `git grep -n -E 'SKILL\.md|AGENTS\.md|frontmatter' e3cf4e0 -- scripts`, rc 0. Append-only checks, round templates, and check-freshness.mjs:15,18 pinning plugin SKILL.md bytes (freshness, not craft). No script in that grep grades a skill file, in tabi or any sibling. check-adjacency.mjs reads sibling bytes for tabi's own map only.
- kotoba side: `git -C kotoba-shokunin grep -n -w -i tabi c48793db -- ':!.ufo'` → PROVINCE.md:54, census :80, plans/round-49.md:30,43 only. The substring hit at SKILL.md:155 is "Portability". kotoba states no split naming tabi.

## Evidence (commands, exit codes)
- `git -C tabi-shokunin grep -n -E 'C-C' e3cf4e0 -- .ufo/waves/round-16` → 3 hits (drafts :13, :39; w1 :30), rc 0.
- `git -C tabi-shokunin grep -n -E '\bC-C\b' e3cf4e0 -- ':!.ufo'` → no output.
- `git show e3cf4e0:corpus/adjacency.tsv | wc -l` → 11; `… | tail -n +2 | wc -l` → 10 (sibling column: kagi 2, kaidoku 2, kake 2, kama 1, kumitate 1, revenger 2).
- `git grep -n 'skills/\*' e3cf4e0 -- .ufo corpus SKILL.md PROVINCE.md` → .ufo/waves/round-17/w2/AdjRow9.md:55 only.
- kumitate: `git -C kumitate-shokunin show 1770305f…:SCORECARD.md | sed -n 1553,1559p`; `show fac39171…:SCORECARD.md | sed -n 1612,1618p`; `grep -n '~/.kimi-code/skills' fac39171…` → SCORECARD.md:706. Each rc 0.
- Guard, in the private clone: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → "rows 20 verified 20", "province rows 20 matched 20", rc 0.
- Kotoba frontier: `git show c48793db:PROVINCE.md | sed -n 23p` names "MCP/plugin instruction surfaces".

## Gaps and residual risk
- Did not re-run the build seat's 61-match sweep or its 11092 tree-wide count.
- Did not read all 2441 lines of tabi SKILL.md; searched for the terms above and read the hits.
- No web source opened; none was needed for this row.

## Asks for the integrator
1. Decide whether `.ufo` wave drafts are scope surfaces. If yes, reclassify tabi to `adjacent`, with the split stated as "agent-facing tool text: kotoba owns the craft; tabi records verbatim, does not grade" (tabi `.ufo/waves/round-16/drafts/DraftAdjacency.md:39`). If no, say so in the census Limits and correct CensusTabi.md:94.
2. Correct CensusTabi.md:41-42 (9 rows, should be 10) and the reasoning at :52-53.
3. Change the census row, the counts, PROVINCE kotoba :54 and the plans/round-49.md count commands together. The guard will not catch a wrong `none`.
