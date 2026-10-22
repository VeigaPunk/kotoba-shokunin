# Falsify: census row `tameshi` (round 49, C1 adjacency)

Verdict: HOLDS-BOUNDED. It applies to census row `tameshi` (classification `adjacent`, sibling pin 3b20f073c7305a582562cd323982991464c324f3) and to its PROVINCE.md § Adjacent row, at judged kotoba c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. The pin, branch, scope quote and both mechanical values hold. `adjacent` survives only as a judgment: the literal instrument clause of the contested rule points at `contested`, and the row cites a source the rule does not list. The PROVINCE boundary note overstates its one citation. The guard checks none of the branch, mechanical-column or boundary-note text.

## Findings (by severity)

### F1 (medium): the contested clause is not weighed; the "not contested" sweep was narrow
- Rule (census § Classification rule): contested = "writing or auditing other lanes' SKILL.md, prompts or AGENTS.md-class files, or the instruments over them".
- Tameshi PROVINCE.md:9 (Owns) names `kagi-shokunin/corpus/*check*.sh`. PROVINCE.md:28-32 (Core) keeps "every surface the lane has actually measured or now governs" and lists kagi `corpus/checklist-run.sh`.
- kagi `corpus/checklist-run.sh` at kagi fecee874 (the revision tameshi's runs used) reads kagi's SKILL.md: line 4 "`SKILL.md` §Credential-hygiene checklist holds 16 items"; lines 97-98 "Items live in one section of SKILL.md, one `- [ ] ` bullet each"; line 68 default `SKILL="$ROOT/SKILL.md"`.
- Literal reading: tameshi's committed scope names an executable instrument over another lane's SKILL.md checklist, so the row is `contested`. Counter-reading: that instrument runs operational credential checks, not SKILL craft, and kotoba's core instruments are craft-quality. The census must say which reading it uses. It does not.
- Build report Finding 6 swept only `SKILL.md PROVINCE.md README.md AGENTS.md MINT.md`. My sweep of `corpus/` and `tools/` (below) found no tameshi text that writes or audits another lane's SKILL.md, prompts or AGENTS.md. Other-lane SKILL.md mentions are provenance citations: corpus/knowledge/service-optin-protocol.md:47,158,199,253; closeout-r11.md:259,366; operator-runbook.md:238; incremental-pin-disposition.md:240.
- Not resolved: kumitate `scripts/kimi-census.mjs` (its header names `agents/secondary/` and `skills/`). `git -C kumitate-shokunin ls-tree --name-only fac39171ac28c606e90da75fc2ba2ed3df52f4ea agents/secondary/` returned no lines. I did not chase it further.

### F2 (medium): `adjacent` rests on a source the rule does not list; the matching source is not cited
- The rule's surfaces are "SKILL.md, PROVINCE.md, corpus files". The census row cites no evidence. The tameshi boundary note (kotoba PROVINCE.md:55) cites `.ufo/waves/round-16/w1/Overlap1.md:136`, a round-16 wave report. That file is not a listed surface.
- Tameshi's own classification of kotoba in that report is `complementary` (Overlap1.md:106, row O-08), not adjacent.
- Tameshi-side text that matches the rule's wording is in corpus: fleet-kill-rate-ledger.md:125-128 ("Boundary — sightings and adjacent machinery, not queued ... kotoba `verifiers/*` — file existence is O, their gate-ness is U") and :233-234 (U8); fleet-suite-census.md:625. Neither the row nor the note cites them.
- Kotoba's own PROVINCE row also states a split, but that is one side only, and it derives from the round-16 wave.
- Net: adjacency is supportable under the rule through corpus lines, but the record cites the wrong source.

### F3 (medium): the PROVINCE boundary note overstates its one citation
- Note (judged PROVINCE.md:55): "tameshi owns the fixture method, kotoba owns its own checklist instruments (tameshi `.ufo/waves/round-16/w1/Overlap1.md:136`)."
- Overlap1.md:136 at 3b20f07 reads "**F4 — kotoba owns the SKILL-checklist instrument; C2 must not conflate it.**" That is one instrument. The note widens it to plural "checklist instruments" and "its own". Overreach.
- "tameshi owns the fixture method": PROVINCE.md:7 "Owns: the method". Holds as a narrowed paraphrase.
- "verification-fixture craft and mutation testing": PROVINCE.md:3-5. Holds.
- The citation resolves (line 136 is F4). F4's other numbers (kotoba argparse `:2097-2119`, fixtures `:271,1528`, kotoba PROVINCE.md:30) are round-16 kotoba line numbers and are stale. The note does not repeat them.

### F4 (medium): the guard checks none of the fields named above
Mutant copies live in /fast/scratch/hyaku/kotoba-r49/falsify/RowTameshi/mut/. Each run was `python3 -B verifiers/check_sibling_census.py <census> --province <province>`.
- M1, branch `master` changed to `main` on the tameshi row: `rows 20 verified 20`, `province rows 20 matched 20`, exit=0.
- M2, names-kotoba `no` changed to `yes: kotoba` and arbitration `yes: kama` changed to `no`: exit=0.
- M3, PROVINCE note changed to "kotoba owns every verifier in the fleet" with cited line `Overlap1.md:999`: exit=0.
- Code: `check_census` checks the commit as hex (verifier:389), the classification enum (:393-398), the path:line split (:403-408) and the quote window (:415-435). For PROVINCE it checks only classification and commit (:532-542). It never reads the branch cell, the names-kotoba and arbitration cells, or the note's free text. The census calls the two mechanical columns "mechanical", so the guard does not do what the census says for them.

### F5 (low): guard docstring and code disagree
- Docstring verifier:40-41: "the path part of `path:line` is one of the skill file(s) the row names".
- Code :410-413 says the path cell is independent, and only path:line drives `git show`.
- Tameshi's row has path `SKILL.md` and path:line `PROVINCE.md:3`. The docstring rule fails this row. The guard passes it (judged run, exit=0). One of the two is wrong.

### F6 (info): the pin is no longer the tip
- `git -C tameshi-shokunin rev-parse master` gives 2b064cfbd3b4f3aed84deb1bf35c94e8a6c1b162, and HEAD is the same. The pin is an ancestor of it (`git merge-base --is-ancestor 3b20f07… master`, exit=0).
- `git diff --stat 3b20f07… master -- SKILL.md PROVINCE.md corpus tools README.md AGENTS.md MINT.md SHONEN.md`: 13 files, 741 insertions, 33 deletions. PROVINCE.md has 13 changed lines and SKILL.md 54.
- `git grep -niI kotoba 2b064cf -- ':!.ufo'` returns the same three lines as at the pin. Nothing new names kotoba.
- The build report's "HEAD detached at the master tip" held when it was checked. The census Limits section already records that tameshi advanced.

## Verified (holds)
- (1) Commit exists: `git -C tameshi-shokunin cat-file -t 3b20f07…` gives `commit`. Branch: `git branch -a --contains` lists `master`. Subject and date: 2026-10-22 06:36:44 -0300.
- (2) Scope quote: PROVINCE.md:3-5 at the pin, wrapped over three physical lines and verbatim once whitespace is collapsed. The verifier finds it in the ±2 window.
- (4) Mechanical columns, re-derived from `git show 3b20f07…:SKILL.md` line 3, the only description. It has no `kotoba` token, so "no". Whole lane-name tokens: `kama` only ("route those to the product lane or kama"), so "yes: kama". Both match the row.
- Pin facts: SKILL.md 2084 lines, 159719 bytes, sha256 7d3a9e2907fcb9fc1cb2ce6dee95f38e3c28cc07c974bfadc5feab022f07be4a. PROVINCE.md 105 lines, 5618 bytes, sha256 5d56df9bb86f1a27aeb095f2b169fe413770f9e0d7ad4d42fc7ef2abd1ecf939. Frontmatter is four lines (name :2, description :3). Owns 7-12, Refuses 14-18 (16-17 "Never edits a sibling's gate code"), Adjacent 44-47 with no `kotoba`. The build's 10 sweep hits (SKILL 9, README 1) match.
- Judged bytes: `git -C kotoba-shokunin show c48793db:PROVINCE.md | sha256sum` gives 9fe4ba1c…, identical to the lane working copy. The census gives 4ce0a306…, also identical.

## Commands and exit codes (verbatim)
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`, run in a private clone at c48793db: `rows 20 verified 20`, `province rows 20 matched 20`, exit=0.
- `python3 -B verifiers/check_sibling_census.py --self-test`: `self-test: 0 failure(s) over 39 assertions`, exit=0.
- M1, M2, M3: exit=0 each (see F4).
- `git -C tameshi-shokunin grep -niI kotoba 3b20f07… -- ':!.ufo'`: 3 lines (ledger:127, ledger:233, fleet-suite-census:625). Same at the tip.
- Build's base claim, `git -C kotoba-shokunin show a5adc146:PROVINCE.md | sed -n '32p'`: `- tameshi — verification-fixture craft and mutation testing.` True at base, historical now.

## Tools and writes
- No tools installed or upgraded. No lane writes. Scratch only: /fast/scratch/hyaku/kotoba-r49/falsify/RowTameshi/ (a clone of the lane at c48793db, and mutant copies).
- Sibling reads used `git show`, `grep`, `ls-tree`, `rev-parse` and `log`. Also used `cat-file`, `branch --contains`, `merge-base --is-ancestor` and `diff --stat`. These are read-only but outside the listed set, so I record them here.

## Residual risk and verification gaps
- The other 19 rows were not examined.
- F1 turns on how "the instruments over them" is read. I give both readings and do not decide it.
- kumitate `kimi-census.mjs` was not resolved (see F1).
- The F4 mutants show a coverage gap in the guard. They do not show the census values are wrong.

## Suggested fixes for the record owner (not applied)
1. Decide the instrument clause. Either record kagi `checklist-run.sh` as `contested`, or narrow the rule to craft-quality instruments.
2. Cite corpus ledger :125-128 and U8 :233-234 for the tameshi side of `adjacent`, alongside or instead of the wave report.
3. Rewrite the PROVINCE note to the F4 sentence: "kotoba owns the SKILL-checklist instrument".
4. Extend the guard to the branch (via `git branch --contains`), recompute the two mechanical columns from frontmatter, and check at least the cited line of the note.
5. Reconcile verifier docstring :40-41 with code :410-413.
