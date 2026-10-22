# Falsify — C1 census row `chousa` (round 49, attempt 1)

Seat: KotobaR49.RowChousa (leaf, read-only). Judged on: adjacency.
Judged bytes: kotoba master c48793dbe5eb30cd661f42ecad7399ae94e3d7ad. Sibling pin: chousa-shokunin 6c5eb1466f2b8abbd3de576389037f435016d07b.

## Verdict

- Census row `chousa` (commit, branch, scope quote, both mechanical cells, classification `adjacent` under the rule as written): **HOLDS-BOUNDED**. The row is right on every field. Its classification is defensible, but its stated basis is weaker than the row says (F1, F2).
- PROVINCE.md § Adjacent chousa boundary note (judged line 38): **FAILS as written**. "kotoba cites it" has no citation in any committed kotoba scope surface (F2). "claim admission stays here" is presented as a kotoba-chousa split, but it is a fleet-wide rule that chousa also applies to its own corpus (F1).
- Build report `.ufo/waves/round-49/build/CensusChousa.md`: does not hold as written in four places (F1 "neither in dispute", F5 stale line, F6 MINT.md dismissal, F8 count).
- Guard: the mechanical cells and the boundary text are checked by no instrument (F4). The census recheck ("rows 20 verified 20") does not cover them.

## Checks

1. Commit and branch: HOLDS. `master`, `HEAD` and `pin^{commit}` all resolve to the pin. The pin is master's tip, committed 2026-10-22 05:02:45 -0300. The branch cell `master` is right.
2. Scope quote: HOLDS. `show pin:PROVINCE.md` line 3 equals the census quote cell exactly (Python equality True, one occurrence).
3. Classification `adjacent`: HOLDS under the rule as written. `contested`: no. Chousa's committed surfaces claim none of kotoba's core (E-b). `adjacent`: kotoba's committed `corpus/QUALITY.md:7-8` states the split, rooted in fleet `CORPUS.md:119-122` ("No second method … the research method stays chousa's").
4. Mechanical columns: HOLDS by re-derivation from `git show pin:SKILL.md`. The description (line 3) has no whole-token `kotoba` (case-insensitive; SKILL.md has zero `kotoba` anywhere). Its whole-token sibling names are `kasegi` and `kengaku`, which matches the census cell `yes: kasegi, kengaku`. No instrument checks either cell (F4).
5. PROVINCE.md boundary note, clause by clause:
   - "deep-research method": true (chousa PROVINCE.md:3).
   - "kotoba cites it": FALSE as a scope claim (F2).
   - "never re-derives it": true on my sweep (E-c, exit 1). The census and PROVINCE carry no sweep for it; the seat's only kotoba-side sweep was for the word `chousa` (F3).
   - "(`corpus/QUALITY.md`: claim admission stays here, the research method stays chousa's)": the quote is verbatim at QUALITY.md:7-8. The admission half is generic (F1).

## Findings (severity order)

F4 (medium-high, instrument). The guard checks quote, commit, classification and lane set only. It never checks `names kotoba`, `arbitration` or the boundary free text. Mutation runs (E-d): flipping chousa's mechanical cells to `yes`/`no` passes (exit 0); changing "kotoba cites it" to "kotoba quotes it" passes (exit 0). Controls fail as they should: a one-word quote change exits 1, and a classification or commit change exits 1. Static: the guard reads `names kotoba` and `arbitration` only in `CENSUS_CELL_NAMES` (`check_sibling_census.py:326`) and a non-empty test (`:383`). The PROVINCE check reads `cells[1]` and `cells[2]` only (`:532`, `:538`). The census labels these cells "mechanical" and its Limits say "the two mechanical columns are not [judgment]", but nothing computes them.

F1 (medium, basis). Admission is not a kotoba-chousa split. Fleet `CORPUS.md:119-121` gives every lane "Claim admission stays in corpus/QUALITY.md". Chousa applies that to its own corpus: `corpus/QUALITY.md:1` is titled "# Admission bar (probation draft)"; `:12-13` says "this file holds admission only"; `SKILL.md:35` says "admission stays in `corpus/QUALITY.md`". The build report (CensusChousa.md Finding 1, lines 11-17) says "kotoba owns admission … Two halves … neither in dispute". That is false for the admission half. Only "the research method stays chousa's" is pair-specific. Adjacency still holds, because the rule accepts either side's statement, but the rule admits a fleet-wide sentence as a pairwise split. The census should say so.

F2 (medium, citation). "kotoba cites it" has no citation in any committed kotoba scope surface. `git grep` for `chousa-shokunin/` outside `.ufo` returns exit 1 (E-c). Every citation of chousa artifacts is work product: `.ufo/round-46/scouts/w2-connector.md:13, :30, :35`. Scope surfaces name chousa (PROVINCE.md:38, QUALITY.md:8) and cite none of its files.

F3 (medium, unswept negative). "never re-derives it" is supported by my sweep (E-c: eight method phrases, zero hits, exit 1). The seat never swept it (CensusChousa.md:124-125 is a `chousa`-word grep at base a5adc146). Kotoba's tier A/B/C and search log come from the fleet contract (`CORPUS.md:93-97`, `:126-128`). The census never cites `CORPUS.md:119-122`, the rule that actually makes the negative true.

F5 (medium, citation). CensusChousa.md:16 cites `PROVINCE.md:29` for "kotoba cites it, never re-derives it". At c48793db that row is line 38. Line 29 is the census path line. The cited line 29 is the base a5adc146 row (`git show a5adc146:PROVINCE.md`, line 29: "- chousa — deep-research method (source hierarchy, citation chaining); kotoba cites it, never re-derives it."). ConnectSiblingOverlap.md:112 repeats the stale cite.

F6 (medium, omission). `MINT.md:52-53`: "Rejected recipients for this material: lore, kotoba, kasegi, kama, kumitate, tameshi." CensusChousa.md Finding 4 cites this line and then says "None is a scope surface." MINT.md is a committed domain-boundary record (its "Domain boundary" paragraph; an integration guard appended 2026-10-15). It is outside the rule's listed surfaces (SKILL.md, PROVINCE.md, corpus files), so excluding it can be defended, but the stated reason is wrong. It is the one chousa-side statement that routes kotoba out of chousa's material, and the seat cites it and discards it. Adjacency is unaffected.

F7 (low, coverage; no defect). The seat did not read `considerthese/2026-10-19..21.md`, `SHONEN.md`, `AGENTS.md`, `README.md`. I read them: no cross-lane authoring; the considerthese files are own-lane reflections. `LOG.md`, `SCORECARD.md` and `tools/research-gate.sh` were keyword-swept, not read. The gate's zero-write claim is the SKILL's, not verified here.

F8 (low, count). CensusChousa.md:109-110 says `-i kotobank` gives "87 lines in 26 files". My count: 87 lines in 27 files (E-f). The "26 + 3 = 29" arithmetic is not the case-insensitive union. The case-sensitive substring count (29 files) is correct.

F9 (out of row, QUALITY owner). At the current fleet root, `CORPUS.md` lines are one early. Q12 cites `:17` (blank; rule at `:18`). Q13 cites `:33` (blank; rule at `:34`). Q14 cites `:38` (the count rule; the negative-claim rule is at `:39`). The fleet root is not pinned.

F10 (out of row, chousa's own claim). `corpus/knowledge/metadata-screen-r25.md:26-27` says the header is "the lane's own convention". Its "neither source" refers to S029 and S033, so that part is literally true. But fleet `CORPUS.md:18` and `:163-170` prescribe `source:`, `verified-at:` and `recheck:` for every knowledge entry. The build seat (Finding 6) accepted the line at face value.

F11 (out of row, definition). Census `arbitration` cells count `kotoba` as a sibling name for kengaku (`yes: chousa, kama, kotoba, kumitate, tameshi`) and kotodama (`yes: chousa, kotoba, lore`). The census rule says "sibling lane names"; the guard's `fleet_lanes` excludes kotoba (`SELF_LANE`). Build Finding 3 uses a third definition ("gives or refuses a domain"). No effect on chousa, where every definition gives `yes: kasegi, kengaku`.

## What would make the row and note hold

Cite `CORPUS.md:119-122` as the basis. State that both lanes keep admission in their own QUALITY.md and that the research method is chousa's (chousa `SKILL.md:17-20` matches the fleet's list). Replace "kotoba cites it" with the committed citation the work product holds, or drop it. Add the method-phrase sweep (E-c) to the row's evidence. Make the guard check the two mechanical cells against the pinned description, or mark them unchecked.

## Evidence (commands and exit codes, verbatim)

- E-a Pin and tree. `git -C chousa-shokunin rev-parse --verify 6c5eb14…^{commit}` → exit 0. `rev-parse master` → exit 0, `6c5eb14…`. `rev-parse HEAD` → exit 0, `6c5eb14…`. `log -3 --format=%H%x20%ad%x20%s master` → exit 0. `ls-tree -r --name-only 6c5eb14…` → exit 0, 800 paths; `verifiers/` entries 0; `tools/` entries `tools/research-gate.sh` only; no `skills/` or `.agents/`. Blob pins from the build seat match (`rev-parse pin:PROVINCE.md` → `0f94a0c4…`; SKILL.md `877b324d…`; MINT.md `74a66872…`; QUALITY.md `a4a60131…`). sha256 of PROVINCE.md `cf7826a4…`; SKILL.md `42937571…`, 569 lines.
- E-b Cross-lane sweeps (pin, `-- . ':!.ufo'`). Authoring words (`frontmatter|system prompt|dispatch prompt|prompt (craft|wording|text)|AGENTS\.md|skill craft|other lanes?|another lane|cross-lane`) → exit 0, 5 lines; none is cross-lane authoring. Other-lane `*-shokunin/` paths (`[a-z]+-shokun(in|ki)/`, which does not match names with digits such as game-dev-*) → exit 0, 103 lines; 5 name another lane (mori 2, kasegi 1, souji 1, tameshi 1), all citations or lineage. Gates table (SKILL.md 66-76 read in full): owner `chousa` on every row; verify modes "zero writes".
- E-c Kotoba judged. `git -C kotoba-shokunin grep -I -n -i -E 'question framing|source hierarch|hop resolution|claim-vs-source|citation chain|primary > secondary|primary / secondary|aggregator > unsourced|search-strategy' c48793db… -- SKILL.md PROVINCE.md AGENTS.md README.md corpus verifiers tools plans ':!.ufo'` → exit 1, 0 lines. `git grep -I -n -i 'chousa-shokunin/' c48793db… -- . ':!.ufo'` → exit 1. `… -- . ':!.ufo'` with `chousa` → exit 0, 10 lines (PROVINCE.md:38; corpus/QUALITY.md:8; census lines 64, 72, 73, 75, 94, 123; plans/round-49.md:30, 43; census and plans only name it). `… -- .ufo` with `chousa-shokunin/` → exit 0, 10 lines (w2-connector.md:10, 13, 30, 31, 35 among them).
- E-d Guard mutations. Scratch clone `/fast/scratch/hyaku/kotoba-r49/falsify/RowChousa/kotoba` at c48793db (`git clone -q` exit 0; `checkout -q` exit 0). Command: `python3 -B verifiers/check_sibling_census.py <census> --fleet /home/vgpnk/Projects/shokunin --province <PROVINCE>`. BASE exit 0 (`rows 20 verified 20`, `province rows 20 matched 20`). census_names (chousa `names kotoba` yes, arbitration no) exit 0. census_quote (`craft` → `craftsmanship`) exit 1 (`quote not found at PROVINCE.md:3`). census_class (none) exit 1. prov_text ("kotoba cites it" → "kotoba quotes it") exit 0. prov_class (none) exit 1. prov_commit (`1`×40) exit 1.
- E-e Quote and lines. `git show c48793db:corpus/QUALITY.md` lines 7-8 (exit 0). `git show c48793db:PROVINCE.md` chousa row at line 38 (exit 0); `git show a5adc146:PROVINCE.md` chousa row at line 29 (exit 0). Fleet `CORPUS.md` read at lines 17-18, 33-34, 38-39, 64-68, 93-97, 119-122, 163-170 (read tool, no git).
- E-f Counts. `git -C chousa-shokunin grep -I -c -i kotobank 6c5eb14… -- .` → exit 0, 87 lines in 27 files. `grep -I -l -i -w kotoba` → exit 0, 3 files (CriticAxisHarm.md:29, MINT.md:52, SCORECARD.md:479); overlap with kotobank files: none. `grep -I -l kotoba` (case-sensitive) → exit 0, 29 files.

## Residual risk and gaps

- Fleet `CORPUS.md` is not pinned; its line numbers are as read on 2026-10-22. The contract's source file `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` was not located (a `**` glob timed out, which is not proof of absence).
- I ran the guard on one scratch copy only. The base run covers all 20 rows, but I did not audit the other 19 rows.
- `tools/research-gate.sh` (about 170 KB), `LOG.md` and `SCORECARD.md` were searched, not read in full.

## Tooling

No installs or updates. Used existing `git` and `python3`. No pacman, no jj, no git write in the lane. Lane access was read-only (`git show`, `grep`, `ls-tree`, `rev-parse`, `log`) plus a scratch clone. The only file written in the lane is this report.
