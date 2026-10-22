# Round 49 falsify: RowKasegi (C1 census row `kasegi`)

**Verdict: FAILS** for the classification column. The `kasegi` row of `corpus/knowledge/sibling-overlap-census-round49.md` and the `kasegi` row of `PROVINCE.md` § Adjacent both say `none`. Under the entry's own § Classification rule ("either side's committed scope surfaces"), kotoba's committed SKILL.md and corpus name kasegi in a split, so the class must be `adjacent`. The commit and branch cell, the scope quote, the two mechanical columns and the facts in the boundary note HOLD.

Judged bytes: kotoba master `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad` (census, PROVINCE.md and SKILL.md sha256 equal the lane files). Sibling pin: `1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a`.

Method: leaf seat, no delegation. Private clones in `/fast/scratch/hyaku/kotoba-r49/falsify/RowKasegi/{kasegi,kotoba}`. Sibling repo read only through `cat-file`, `rev-parse`, `log`, `show`, `ls-tree`, `grep`. Nothing written in the lane except this file. No tool installed or upgraded.

## Findings

**F1 (high). `none` contradicts the rule the entry states.**
- Rule (census § Classification rule): "`adjacent`: either side's committed scope surfaces (SKILL.md, PROVINCE.md, corpus files) state a split of one artifact, function or trigger area between the sibling and kotoba."
- Kotoba `SKILL.md:10-12` (description, c48793d): "Sibling boundary: the five `*-shokunin` domain skills (kagi, kake, kasegi, kengaku, kumitate) own their own SKILL.md content — this skill audits and reports; fixes route to the owning lane." It names kasegi and splits the SKILL.md artifact (kasegi owns content, kotoba audits). That meets the adjacency test.
- Kotoba `corpus/SOURCES.md:65-66`: "out-of-scope security/injection items (adjacent to kasegi)".
- Kotoba `corpus/SOURCES.md:123`: "Skill-injection evidence (arXiv 2510.26328, 2601.10338, 2510.09023), Meta Rule of Two — adjacent to kasegi; report, do not absorb."
- The census knows of the conflict (Finding 3: the description names 5 siblings, and "the gap is recorded, not closed"). It classes kasegi from the sibling side only. The kotodama override applies the same logic one way (sibling description refuses kotoba, so adjacent). The reverse direction was never applied.

**F2 (high, outside this row). The same defect hits `kake`.** Kotoba `SKILL.md:11` names kake in the same ownership sentence, and the census row is `kake | none`. Under the same rule kake is adjacent. With kasegi and kake both moved, the counts are 9 adjacent and 11 none. Flagged for the kake falsifier; not analysed here.

**F3 (medium). The boundary note reaches the wrong conclusion from true facts.** Its facts hold (section 5). Withdrawing the unsourced prompt-injection clause does not remove the kotoba-side splits in F1, and the note does not mention them.

**F4 (low).** Census Finding 3 names the disagreement and leaves it open. For kasegi the open item is the classification.

**F5 (info). Sibling side: no contested or split claim found.**
- No pinned kasegi scope surface claims skill, prompt, frontmatter, AGENTS.md or CLAUDE.md craft. Case-insensitive pinned-tree grep for `sibling|neighbo|adjacen|arbitrat|contest|ownership|owner|george|kotoba|skill craft|prompt craft|frontmatter|AGENTS\.md|CLAUDE\.md`, excluding `.ufo/` and `LOG.md`, returns only self-scoped lines (PROVINCE.md:19,40,42,47; SKILL.md:267,449,729,747) and citation rows.
- Tools (`corpus/instruments/{density,resolve,anchorcheck,source-recheck,test_resolve}.py`) work on their own root: argv SKILL.md or repo root. `anchorcheck.py:51,112` discovers roots by SKILL.md or `.git`. No path into another `*-shokunin` lane in any `.py`; the only `../` hits are fixture strings (`test_resolve.py:257,268,269`).
- Records, not split statements: `LOG.md:400` (kotoba inventories a CLAUDE.md inside `george/`; "kasegi park stands, qualified as unexplored-by-kasegi"); `LOG.md:501` (kotoba's `sibling-description-rewrites-round8.md` "repeats kasegi policy-intake facts"). LOG.md is not a listed surface. If it counted, these would add weak adjacency, not contest.
- `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4,6,18` records kotoba's round-5 audit ("kasegi L86") and cites kotoba's checklist item 10 as an analogy. Not a split.
- Frontier F01–F08 (`corpus/README.md:195-202`): CVSS v4, coordinated-disclosure timelines, safe harbor, AI-assisted finding validation, CWE Top 25, FIRST, CNA rules, EU CRA. No skill or prompt craft.
- Vulnerability text (`SKILL.md:739-747, 783-788`, CWE-78 in a third-party plugin-dev hook script): a third-party bug, no split with kotoba stated; not counted.
- `considerthese/2026-10-19.md`, `10-20.md`, `10-21.md`: self-scoped reflections; no kotoba or craft split.
- `AGENTS.md` read in full (5 lines, self-scoped). `SCORECARD.md:4-5` and `README.md:6` say adjacency is reported, not absorbed. `SHONEN.md`: grep only, no kotoba.

## 1. Commit and branch cell: HOLDS
- `git cat-file -t 1fafde8f…` → `commit`.
- `rev-parse master` → `1fafde8f…`; `rev-parse HEAD` → same (HEAD detached at the pin).
- `git log --oneline 1fafde8f..master | wc -l` → 0; `git log --oneline master..1fafde8f | wc -l` → 0. Master tip is the pin.

## 2. Scope quote at PROVINCE.md:3 (±2 lines): HOLDS
- Pin PROVINCE.md line 3: "**Domain:** bounty & security research — scopes ~/Projects/bounties, program rules, claim packages". The census quote is an exact substring.
- `grep -c -F` of the quote: pin PROVINCE.md → 1; census file at c48793d → 1.
- Lines 1–5: 1 title, 2 and 4 blank, 5 starts the Round-15 annotation. The quote sits at line 3 only.
- `cmp` of `c8b719d:PROVINCE.md` line 3 against pin line 3 → `cmp-exit=0`.
- Relevant but not an error: PROVINCE.md:5-22 say the `~/Projects/bounties` root and both surviving roots are removed or ABSENT. The census quote omits this. It does not change the class.

## 3. Classification: FAILS (F1, F2)
Sibling side clean (F5). Kotoba side adjacent (F1). Under the stated rule, `none` is wrong.

## 4. Mechanical columns: HOLDS
- `SKILL.md` lines 1-4 at the pin: single-line `description: Domain specialist — bounty & security research — scopes ~/Projects/bounties, program rules, claim packages. Rank: shonen.`
- Line 3 through `grep -o -i -w -E` with the 20 sibling names plus `kotoba` → no output, `sibling-token-exit=1`. Substring `kotoba|kotodama|shokunin` → `kotoba-substring-exit=1`.
- names kotoba = no; arbitration = no. Both correct as written.

## 5. PROVINCE.md boundary note (kasegi row, line 45): facts hold, conclusion does not
Note: "bounty and security research; the earlier "prompt-injection exploits" clause had no source in kasegi's tree and is withdrawn".
- "bounty and security research": kasegi PROVINCE.md:3, SKILL.md:3, README.md:6. HOLDS.
- "the earlier 'prompt-injection exploits' clause": kotoba `a5adc146` PROVINCE.md:33, "- kasegi — security research incl. prompt-injection exploits." (`git show a5adc146…:PROVINCE.md | grep -n -i kasegi` → `33:`, exit 0). HOLDS.
- "had no source in kasegi's tree": pinned tree `git grep -n -i -E 'prompt.{0,3}inject'` → `tree-exit=1`. All refs and all history: `git log --all -E -G 'prompt.{0,3}inject'` → empty, exit 0. Positive control `git log --all -E -G 'command.{0,3}inject' | wc -l` → 6, exit 0, so the pickaxe works. PROVINCE.md history (4 commits) with `-S prompt` and `-S injection` → empty, exit 0 each. HOLDS.
- "is withdrawn": the judged PROVINCE.md kasegi row carries no such clause. HOLDS.
- Round-46 source: `git show c48793d:.ufo/round-46/scouts/w2-connector.md` line 22 cites `../kasegi-shokunin/PROVINCE.md:3-4`; kasegi PROVINCE.md line 4 is blank. HOLDS.
- § Adjacent (kasegi): line 40 `## Adjacent`; lines 44-47 name chousa, kagi, kake, kengaku and not kotoba. HOLDS.
- Missing from the note: the kotoba-side splits (F1).

## 6. Other checks
- Kotoba mentions of kasegi, case-insensitive, pinned kasegi tree: 7 lines in 4 files (`LOG.md:400, 501`; `corpus/instruments/citation-survival.tsv:1025`; `.ufo/rounds/round-21/frozen-head-citation-survival.tsv:1041`; `corpus/lessons/round-5-aggregator-mirror-ambiguous-citation-base.md:4,6,18`). The seat's case-sensitive count of 6 misses `LOG.md:501` ("Kotoba's"). No effect on the class.
- Kotoba judged commit, `git grep -n -i kasegi c48793d` → exit 0: PROVINCE.md:45; SKILL.md:10-11; SOURCES.md:65-66, 123; `corpus/knowledge/sibling-description-rewrites-round8.md:259-310` (a proposed kasegi description whose arbitration names kengaku and kumitate, not kotoba; not counted).

## Commands run (exit codes as printed)
- `git grep -n -i -E 'prompt.{0,3}inject' 1fafde8…` → `tree-exit=1`.
- `git log --all --oneline -E -G 'prompt.{0,3}inject'` → empty, `hist-exit=0`.
- `git log --all --oneline -E -G 'command.{0,3}inject' | wc -l` → 6, `positive-control-exit=0`.
- `git log --all --oneline -S kotoba` → 4 commits, `S-kotoba-exit=0`.
- `git log -- PROVINCE.md` → 4 commits; `-S prompt`, `-S injection` → empty, exit 0 each.
- `awk NR==3` on SKILL.md piped to sibling-name grep → `sibling-token-exit=1`.
- `cmp` of `c8b719d` and pin PROVINCE.md line 3 → `cmp-exit=0`.
- `sha256sum` lane versus clone for census, PROVINCE.md, SKILL.md → identical pairs.
- `git grep -n -i kotoba` (pin) → exit 0; `git grep -n -i kasegi c48793d` → exit 0.
- Tools path sweep (`git grep -E 'Projects/shokunin|-shokunin/|\.\./'` over `*.py`) → only fixture strings.
- Not run: `verifiers/check_sibling_census.py` (the guard). Its recheck text says it checks quote, commit, classification and PROVINCE match. Whether it reads kotoba's own surfaces is [INFERENCE from the recheck text; unverified].

## Residual risk and gaps
- Kasegi `SKILL.md` (1,023 lines) swept by grep, not read end to end. Lines 167, 313, 321 and 368 that the seat cites for "owns" are not re-read by me.
- kake row not analysed beyond F2.
- No kasegi commits past the pin at check time (2026-10-22).
- `PROVINCE.md:25` (Refuses) is from display count, not grep.

## Recommendation (not an edit)
Reclassify kasegi to `adjacent`, and kake under the same rule, citing kotoba `SKILL.md:10-12` and `corpus/SOURCES.md:65-66, 123`, in the census rows and the PROVINCE.md § Adjacent rows. Keep the commit, quote and mechanical columns. Recount the census summary (9 adjacent and 11 none if both move). Make the guard check each classification against both sides' surfaces, not only sibling bytes.
