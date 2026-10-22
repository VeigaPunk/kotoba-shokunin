# ReviewLesson — round-50 falsify (corpus/lessons/round-50.md at 956ee1676e4c18480bce8ac3993541462be76e11)

**VERDICT: HOLDS-BOUNDED** — applies to the lesson file as assigned: M31's evidence pointer reproduces
end to end; Q26 is shown able to fail as claimed (one citation-precision note); the erratum's 16 rows all
resolve and 12 content-verify; the Gate matches the landed diff (one under-recorded knowledge section);
D1-D6 match the bytes (one dangling heading pointer in the lesson's D3 bullet).

Workspace: private clone at `/fast/scratch/hyaku/kotoba-r50/falsify/ReviewLesson/lane` (956ee167), plus
`lane-base` (f3046466) and `lane-mut` (374ecf98). No lane file written except this report. No tools
installed or upgraded; no pacman transaction. All runs 2026-10-22 UTC.

## 1. M31 evidence pointer — HOLDS

Every command in the M31 row reproduces (the `audio|chousa|…|tsukuroi` elision expanded with the 20
census lane names read off `374ecf98`'s census table):

- Counter: `git show 374ecf98:PROVINCE.md | awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' | grep -cE '^\| (audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi) \| (contested|adjacent|none) \| [0-9a-f]{40} \|'` → `20`, exit 0.
- Split: `9 adjacent` / `11 none`; census `names kotoba` cell `no` for **7 of 9** adjacent rows (awk over the census table at 374ecf98).
- Mutant at 374ecf98 (kake `adjacent`→`contested` in census `:75` and `PROVINCE.md:43`): same counter → `20`, exit 0; split `8 adjacent / 1 contested / 11 none`; guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` → `rows 20 verified 20` / `province rows 20 matched 20`, exit 0. Exactly as the row states.
- C2 half at f3046466: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0.
- Guard without `--skill` at base: exit 2, `unrecognized arguments: --skill SKILL.md` (the pointer's premise that the base guard cannot see the description).
- Plan C1 counter at base → `5`, exit 0.
- Committed driver at head over base: `python3 -B verifiers/box_proof_case_deletion.py --rev f3046466` → all six must-fail cases `exit 0 survived` with `boxes proven 2`, `killed 0 of 6`, exit 1 — the row's "deleting a must-fail case leaves `boxes proven 2`, exit 0".

## 2. Q26 shown able to fail — HOLDS (one citation-precision note)

- Q26 landed in `corpus/QUALITY.md` byte-equivalent to the MineMistake draft (headline/nothing-unmeasured rule, applies to claim statements and headlines, grounded in M31, supersedes `—`).
- `MineMistake.md` § "the four applications": round-49 C1 FAILS (counter prints one integer; reclassification invisible), round-49 C2 FAILS (`boxes proven 2` survives case deletion), round-50 C2 PASSES. The FAIL arms rest on E1-E10, which I reproduced independently (section 1).
- **Finding Q26a (minor, citation precision):** the lesson says "applied to the two round-50 statements as re-sized before landing it passes both (seat MineMistake.md)", but MineMistake (12:19-12:37Z) tested the statements as *first planned* — its application 3 quotes the pre-re-size wording and gives a conditional pass. The re-sized-wording pass is nonetheless true on the landed bytes, verified directly: at 956ee167 the guard prints exactly the statement's counter line (`skill description names 9 of 9 non-none lanes`, `skill description length 1008 of 1024`, exit 0), and a bare-name description (9 lane names, no ownership/routing clauses) → nine `FAIL ... no clause that names it carries an ownership or routing marker` lines, `skill description names 0 of 9 non-none lanes`, exit 1. Every clause of the re-sized statement turns on the cited guard.

## 3. Erratum: 16 rejected items — HOLDS

All 16 rows' pointers resolve at 956ee167: every cited file exists and every cited line range is inside
the file (checked with line counts over the clone; longest cited range 171-176 in the 295-line census).
Content spot-checks, 12 of 16 rows, each supported by the cited bytes:

- 1: census `:111-115` (kasegi clause unsourced; `git grep` exit 1, `git log -S` empty) + `CensusKasegi.md:26-31` region.
- 2: `RowKengaku.md:11-15` — route telemetry "historical, absent since 2026-10-15"; note copied the stale half.
- 3: `RowMado.md:17` — F1 "no claim on kotoba ground is false as written"; omarchy skill frontmatter claimed as mado surface.
- 4: `RowKama.md:29` — F3 "Dropped: 'agent' and 'fallback'".
- 5: `RowChousa.md:37` — F6 MINT.md "Rejected recipients" cited then discarded as "None is a scope surface"; reason wrong.
- 6: `CensusKotodama.md:19,30` — anti-triggers name kotoba; MINT.md:20 name-collision row.
- 7: `CriticC1Landed.md:19,32` — kotoba's own description names kake/kasegi; either-side reading → 9 adjacent.
- 8: `CriticC1Landed.md:26` + `RowTameshi.md:16` region — basis is a wave report, excluded surface.
- 9: `RowTabi.md:23-26` — split only in wave drafts; row outcome stays `none`.
- 12: `round-49.md:98-101` — M30 correction ("that line does carry the clause", kasegi PROVINCE.md:3-4 mis-cite).
- 13: `round-49.md:102-104` — removing d04-stem still prints `boxes proven 2`.
- 14: `ReopenS022.md:11-12` — "description alone" not what the page says.

Rows 10, 11, 15, 16 (`plans/round-49.md:27-30,35-43/58-61,63-72/76`, `CriticC1Sizing.md:12,21-27`,
`MineMistake.md:88-91`, `CriticC2Sizing.md:9-21`, `CriticBoxReword.md:36`, `DispatchIndependent.md:25`,
`R4CountProvenance.md:14-21`): files exist, ranges in bounds — resolvable, not content-re-verified.

## 4. Gate admit/reject vs landed — HOLDS-BOUNDED

`git diff --stat f30464660c675d1c1e2851a3bf0366a3aaffe5a8 956ee1676e4c18480bce8ac3993541462be76e11`:
50 files, +6950/−71. Admitted list matches: census +107 (round-50 sections at `:190` and `:246`);
QUALITY.md +1 (Q26 only); `corpus/lessons/round-50.md` created (134 lines); plans/round-50.md created;
SOURCES diff touches only S019, S022 (modified) and S024-S029 (added); `grep -c '^| S0' corpus/SOURCES.md`
→ `29` (rows 23 → 29 as claimed). Reject list respected: no row beyond S029 landed; the Copilot
concept/SDK and Gemini source-code rows are absent; no `DescDraft` artifact in the wave evidence or diff.

- **Finding G1 (moderate, gate record):** the Gate's knowledge line reads "Candidates 1, admitted 1" and
  describes only the six-pages section, but the census entry gained a *second* appended round-50 section —
  `## Round 50: precedence between contested and a stated split (routed defect D3)` (census `:246`),
  kotoba's own precedence rule plus rulings. It landed without an admit line in the Gate. (Same point is
  raised by falsify seat `CriticLearningBar.md` F7.)
- Minor: `corpus/README.md` +6 (index row, round-50 note) appears in the diff unmentioned by the Gate;
  records housekeeping, consistent with the round, not a contradiction.

## 5. Routed-defect dispositions D1-D6 — HOLDS-BOUNDED

- D1 ✓ `ReviewD1D5Facts.md` confirms the round-49 pattern (four addenda rewrote only line 4, appended at EOF); the decision is recorded.
- D2 ✓ bytes: `verify_dispatch_prompts.py` docstring names "every one of the six *named* conjuncts" (`:55`) and observed-status coverage (`:59-61`); the four no-fixture clauses (unsubstituted variable, `<=` at equality, legacy-state arm, non-digit round folder) at `:75-77`, `:547-548`, `:1018`; `verify_skill_checklist.py` `box_map_complete` + `BOX_PROOF_FLAG`/`supports_box_proof`, "--box-proof --map <map> ... must exit 0" (`:67`, `:311`, `:960`); SCORECARD operability row carries the six-conjunct bound, kill rule, controls 0 of 3 → 3 of 3 (`:31`).
- D3 ✓ substance: duplicate-row rejection present (`check_sibling_census.py`, 27 `duplicate` hits; marker/clause arm `:82-86`, `:432-434`, `:513-517`, `:555-559`); floors-registry `"sibling_census": {"floor": 68, "path": "verifiers/check_sibling_census.py"}` — the "68 assertions" claim matches; precedence ruling landed at census `:246`.
  - **Finding D3a (minor, dangling pointer):** the lesson's D3 bullet says "see `## D3 precedence ruling` below", but no such heading exists in the lesson (`git show 956ee167:corpus/lessons/round-50.md | grep -c '^## D3 precedence ruling'` → `0`, exit 1) or anywhere in the tree; the ruling's actual heading is the census entry's `## Round 50: precedence between contested and a stated split (routed defect D3)`. The cross-reference is unresolvable as written.
- D4 ✓ SCORECARD adjacency row (`:34`) bounded ("the clause test is lexical"); "kotoba's own description", "their own bytes" (2), "no precedence rule" present in SCORECARD.
- D5 ✓ erratum table (16 rows, section 3) plus separate admit/reject lists in the lesson Gate.
- D6 ✓ `CarryD6.md`: "ALL THREE STILL OPEN at `f3046466`" (R4 2 of 23 unprovenanced; R5 v1 only frozen; R1 fallback byte-identical to the falsified head).

## Residual risk and verification gaps

- Erratum rows 10, 11, 15, 16: pointers resolve; cited round-49 seat-report contents not re-read against claims (time box).
- S019/S022 "byte-identical re-open": sha256/byte claims taken from seat reports and SOURCES cells; no re-fetch performed (fetch-freshness belongs to the Reopen seats; a fresh fetch may legitimately differ).
- The C1/C2 headline after-values at `542f515` (9 of 9 exit 0 verified at 956ee167; `killed 6 of 6` at 542f515 not re-run here — replay seats own it; I verified the base side `killed 0 of 6` exit 1).
- CriticPrecedenceLanded (sibling) independently flags the same D3a dangling pointer (its F10); CriticLearningBar flags G1 (its F7) — convergent, not contradictory.

## Evidence index (exit codes verbatim)

1. Counter @374ecf98 → `20`, exit 0. 2. Split 9/11; names-kotoba `no` = 7 of 9. 3. Mutant counter → `20`, exit 0; guard exit 0 (`rows 20 verified 20`, `province rows 20 matched 20`). 4. Base `--box-proof` → `boxes proven 2`, exit 0. 5. Base guard `--skill` → exit 2. 6. Base C1 counter → `5`. 7. Driver `--rev f3046466` → `killed 0 of 6`, exit 1. 8. Head guard → `skill description names 9 of 9 non-none lanes`, exit 0. 9. Bare-name description → `names 0 of 9`, nine FAIL marker lines, exit 1. 10. `grep -c '^| S0' corpus/SOURCES.md` → `29`. 11. `git show 956ee167:corpus/lessons/round-50.md | grep -c '^## D3 precedence ruling'` → `0`, exit 1. 12. `git diff --stat f3046466 956ee167` → 50 files, +6950/−71.
