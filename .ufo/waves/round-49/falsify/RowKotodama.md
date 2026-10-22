# Round 49 falsify: RowKotodama (C1 census row `kotodama`)

VERDICT: HOLDS-BOUNDED. Applies to the kotodama row of `corpus/knowledge/sibling-overlap-census-round49.md` and its row at `PROVINCE.md:47` (§ Adjacent). Pin: kotodama `35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a`. Judged kotoba bytes: `c48793dbe5eb30cd661f42ecad7399ae94e3d7ad`. The classification `adjacent`, the pinned commit, the branch cell, the scope quote and both mechanical cells hold. Bounded by F1 (judged-commit guard does not check the mechanical cells), F2 (stale citation in census Finding 7), and F3–F5.

Attacked, by item: (1) commit and branch cell; (2) scope quote at SKILL.md:8 (±2); (3) classification under the § Classification rule, including a contested sweep; (4) the two mechanical columns; (5) every factual statement in the PROVINCE.md kotodama row. Also census Finding 7 (reciprocity) and what the C1 guard covers for this row.

## Findings by severity

F1 MEDIUM. The judged commit's guard does not re-derive the mechanical cells for this row.
- `git show c48793d:verifiers/check_sibling_census.py` is 923 lines, sha256 `8889d219…`. It parses the names and arbitration cells (`CENSUS_CELL_NAMES`) but has no function that reads the pinned frontmatter to derive them (`token_in` and `mechanical_findings` absent).
- Mutant: kotodama arbitration cell changed to `yes: chousa, lore` (kotoba dropped). Committed guard run: exit 0, "rows 20 verified 20", "province rows 20 matched 20".
- The lane working copy's guard differs (1035 lines, sha256 `3500508a…`, not the committed file; its header says "round-49 falsify correction, seat CriticC1Landed", count 0 in the committed file). It has `mechanical_findings` (line 354), called with `expected | {SELF_LANE}` (lines 514–515). Same mutant: exit 1, "FAIL row 11 (census line 73) (lane kotodama): arbitration cell 'yes: chousa, lore' but the pinned description gives 'yes: chousa, kotoba, lore'".
- Effect: the mechanical cells are correct (F4), but the judged bytes do not prove them. The entry's recheck line ("exit 0 and rows 20 verified 20") is true at judged bytes and does not cover those columns. Fix: commit the mechanical check, or narrow the recheck claim.

F2 LOW-MEDIUM. Census Finding 7 cites a line that is blank at the judged commit.
- Census item 7 (judged bytes): "kotoba's `PROVINCE.md:34` already files kotodama as "no overlap observed" in a five-lane lump."
- `git show c48793d:PROVINCE.md`: line 34 is empty (repr `''`); the table starts at line 35; `b'no overlap observed' in` the file → False.
- `git show a5adc146:PROVINCE.md` line 34: "- kotodama (worldbuilding/naming), mado (desktop config), revenger (shipped-artifact RE), mori (fleet observability), kama (model serving) — no overlap observed." True at base.
- The census states a base-commit fact in the present tense, in a file committed at c48793d. The build seat report repeats it (`CensusKotodama.md` line 34). Fix: "at a5adc146, PROVINCE.md:34 (replaced by the round-49 Adjacent table)."

F3 LOW. The PROVINCE note's factual sentences have no guard.
- Mutant: "kotoba's description does not yet name kotodama" changed to "already names kotodama" in a copy of PROVINCE.md. Committed guard: exit 0, "province rows 20 matched 20".
- The guard does catch a classification mutant (kotodama `adjacent`→`none`): exit 1, "classified 'none' does not match the census 'adjacent'".
- So the note's sentences rest on my manual check in section 5, not on the guard.

F4 LOW. One gloss in the note is unsourced in the lane.
- PROVINCE.md:47 "(near-homonym names, 言葉 and 言霊)". 言霊 is sourced in kotodama (`SKILL.md:11`: "言霊 (kotodama, "word-spirit")").
- 言葉 appears in no kotoba file at c48793d except the new census (line 113), the new PROVINCE row, and the seat report (`git grep -n '言葉' c48793d` → 3 hits, all new). The gloss is correct Japanese for the lane name but has no lane source.
- Seat report line 30–31 calls both names "word/language" names; kotodama's own gloss is "word-spirit".

F5 LOW. The arbitration column's sibling set is undefined.
- The entry's intro defines "20 sibling lane repos", which excludes kotoba. The guard's `fleet_lanes` docstring says "minus kotoba". The row lists "chousa, kotoba, lore". The working-copy guard counts kotoba via `expected | {SELF_LANE}`.
- The § Classification rule does not say which set applies. No count changes: kotoba is never the only name in any arbitration list. Fix: state "any lane other than the row's own, kotoba included" in the rule.

F6 INFO. The pin is not the tip. `git -C kotodama rev-list --count 35f0d49..main` → 8 (tip d9f73c8). `git diff --quiet 35f0d49 main -- SKILL.md PROVINCE.md MINT.md README.md AGENTS.md` → exit 0 for each of the five. The only change in scope is `corpus/README.md` (`--numstat` 16 insertions, 4 deletions), with 0 kotoba lines in its diff. The split still holds at tip. The census discloses that pins move.

## Check results

(1) Commit and branch cell: HOLDS.
- `git -C kotodama cat-file -e 35f0d49…^{commit}` → exit 0.
- `git -C kotodama merge-base --is-ancestor 35f0d49 main` → exit 0. `git branch -a --contains 35f0d49` → `main`, `remotes/origin/main`.
- Subject: "round-51: claim D - pastoralism section-2 boundary table 11 -> 15 rows…", 2026-10-22 06:33:02 -0300.
- Cell `main` is right. Per-row loop over all 20 census rows: pin exists and branch contains pin on 20 of 20.

(2) Scope quote: HOLDS.
- Pinned SKILL.md: 88426 bytes, 734 newline-terminated lines, sha256 `1b4efe0f83fafe57c208076a23c9a42b111e2c1de4688c342215938c9fe8fd53` (matches seat).
- Quote (21 words, verbatim): "Domain: the generative craft that connects languages, cultures, myths, symbolisms, and eras to their linguistics and costumes for a fictional world". It is a substring of whitespace-normalized lines 8–10. "Domain: the generative craft that connects" occurs on line 8 only. Within ±2 of 8.

(3) Classification `adjacent`: HOLDS under the rule as written. Contested excluded.
- Rule text: `adjacent` = "either side's committed scope surfaces … state a split of one artifact, function or trigger area between the sibling and kotoba."
- Split: SKILL.md:3 contains "NOT prompt/skill craft (kotoba-shokunin)" (checked: True). This is an anti-trigger on kotoba's trigger area. The rule's letter has no further test (no "governance half" requirement). `none` is therefore not available, and the census override is correct.
- Supporting: MINT.md:20–21 "kotoba owns prompt/skill craft despite its name" (verbatim, checked True); PROVINCE.md:20 "prompt/skill craft (kotoba)."; MINT.md:30; README.md:6 (copy of SKILL description).
- Seat's `none` rests on "kotodama holds an instance of SKILL.md, not a half of its governance". That is not a rule test. Seat report also contradicts itself: Finding 1 says `none`, Finding 4 says "keep the lane in § Adjacent".
- Contested sweep (pinned tree): no kotodama scope surface writes or audits another lane's SKILL.md, prompts or AGENTS.md-class files.
  - Pattern search for sibling-lane names next to SKILL/AGENTS/prompt in SKILL.md, PROVINCE.md, README.md, MINT.md, AGENTS.md, REGIMEN.md, SCORECARD.md, SHONEN.md, corpus/, tools/, templates/: only the kotoba split lines above. Other hits are lore ownership lines (`tools/gates/myth-consistency-gate.py:30`, `corpus/knowledge/culture-material/material-culture-inference-method.md:41`, `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:171`, `corpus/lessons/round-2-triage/V01.md:78`), not kotoba.
  - `git -C kotodama grep -c -E 'git -C [^ ]*-shokunin|\.\./[a-z-]*-shokunin/[A-Za-z]' <pin> -- corpus tools templates SKILL.md PROVINCE.md README.md MINT.md REGIMEN.md SCORECARD.md` → 0 lines.
  - tools: only `tools/gates/argot-derivation-gate.py:4` names SKILL.md (docstring). `git grep -lci frontmatter <pin> -- tools/` → no paths, exit 1.
  - AGENTS.md: 40 lines (`wc -l`), 0 kotoba. SKILL.md lines 509–521, `grep -c -i kotoba` → 0.
  - Whole-token `kotoba` in kotodama scope surfaces: SKILL.md:3, README.md:6, PROVINCE.md:20, MINT.md:20, MINT.md:30. Corpus whole-token hits are Japanese compounds (makura-kotoba, Onna-kotoba) and are false positives.
- Cross-row (outside this row, noted only): `none` rows with kotoba mentions are roster lists, LOG or evidence logs, or corpus anchors. None is a scope-surface split. Not ruled on.

(4) Mechanical columns: HOLD at pin. Not guarded at judged bytes (F1).
- Frontmatter description (SKILL.md:3, 613 characters). Whole token, case-insensitive: `kotoba` present → "names kotoba" = yes (census: yes).
- Whole-token hits against the 20 sibling names: chousa, lore. With kotoba added: chousa, lore, kotoba. Census: "yes: chousa, kotoba, lore" (see F5 on the set).
- Substring hits equal whole-token hits (no near-miss tokens).

(5) PROVINCE.md:47 row, judged bytes:
"| kotodama | adjacent | 35f0d49f96f1d51f8b006136a8e1d0e8d0919a7a | worldbuilding and naming; its description refuses prompt and skill craft by naming kotoba (near-homonym names, 言葉 and 言霊); kotoba's description does not yet name kotodama |"
- Classification `adjacent`: matches census. Commit: matches pin.
- "worldbuilding and naming": pinned PROVINCE.md lines 3–7 ("linguistic-cultural worldbuilding … naming systems"). True.
- "its description refuses prompt and skill craft by naming kotoba": SKILL.md:3. True.
- "言霊": SKILL.md:6, 10–11; README.md:6. True. "言葉": F4.
- "kotoba's description does not yet name kotodama": judged SKILL.md (frontmatter and body) contains 0 `kotodama`. `git grep -c -w -i kotodama c48793d -- PROVINCE.md SKILL.md README.md AGENTS.md` → PROVINCE.md:1 (the row itself). True.
- The note cites no line numbers. Census cites checked: SKILL.md:3 (True), MINT.md:20 (True), PROVINCE.md:20 (True).

Census Finding 2 (base SKILL.md lines 1–16 contain 0 `kotodama`) is true. Finding 7 is F2.

Seat report (`.ufo/waves/round-49/build/CensusKotodama.md`): sha256 values and byte counts match (SKILL `1b4efe0f…`, 88426; PROVINCE `05b34a57…`, 1636). It says the MINT quote is "9 words"; it is 7. It says 言霊 is a "word/language" name (F4).

## Commands and exit codes

- `git -C <kotodama> cat-file -e 35f0d49…^{commit}` → 0
- `git -C <kotodama> merge-base --is-ancestor 35f0d49 main` → 0; `rev-list --count 35f0d49..main` → 8
- `git -C <kotodama> diff --quiet 35f0d49 main -- SKILL.md` (and PROVINCE.md, MINT.md, README.md, AGENTS.md) → 0 each
- Lane judged commit: `git -C kotoba-shokunin rev-parse master HEAD` → both c48793d; census and PROVINCE blobs equal lane files (True, True)
- Guard, committed file, scratch clone at c48793d: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --fleet <scratch>/shokunin` → "rows 20 verified 20", "province rows 20 matched 20", exit 0
- Mutants (scratch copies), committed guard / working-copy guard:
  - kotodama arbitration cell drops kotoba → 0 / 1 (F1)
  - quote "fictional world" → "fictional worlds" → 1 / 1 ("quote not found at SKILL.md:8 (+/-2 lines)")
  - PROVINCE kotodama `adjacent`→`none` → 1 (committed)
  - PROVINCE note "does not yet name" → "already names" → 0 (committed; F3)
- Working-copy guard, unmutated (scratch copy): exit 0.

Scratch only: `/fast/scratch/hyaku/kotoba-r49/falsify/RowKotodama/` (pinned SKILL/PROVINCE/MINT copies, a clone of the lane at c48793d, symlinks to the sibling repos, mutants). No lane writes. No jj. No git writes in the lane. No subagents.

## Tooling

No installs or upgrades. Tools used: git, python3 standard library, sha256sum, grep, sed, wc, cut, cp, ln.

## Residual risk and verification gaps

- The `adjacent` call depends on reading a refusal in SKILL.md:3 as a split. The rule text supports that reading. A stricter reader could say a disclaimer is not a split. I found no text in the rule that says so.
- Contested sweep is pattern-based over committed scope paths. The 1,857 report files were not read in full. Reports are outside the rule's scope list. The one report that quotes the split (round-33 A01 line 75) was checked and is verbatim.
- The guard's mechanical checks were run only in the working copy. Judged bytes have none (F1).
- Pin-to-tip drift was checked only on the five scope files and the corpus/README.md numstat.
