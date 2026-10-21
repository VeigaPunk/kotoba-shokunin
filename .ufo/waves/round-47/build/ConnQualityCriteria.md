verdict: Of this round's three mined classes, stale-premise is not captured by any QUALITY row (Q09 blesses "open debt" at close and Q10 only covers a source moving *during* a run), landing is captured by an instrument plus a fleet rule but fires a round late, and the r46 timestamp defect is captured by nothing; Q19 should make carried records and gate exemptions expire with their anchor, which is also the only wording that keeps C3's erratum registry from laundering dead citations.

## Axes (named)

- freshness (C1), operability (C2), calibration (C3) — declared at `.ufo/waves/round-47/build-spec.json` and `plans/round-47.md` (untracked working file; not at BASE).
- Frontier step = the SOURCES curation workflow (`plans/round-47.md:14-16`) and, in the corpus, the Frontier row `corpus/README.md:74` that C1+C2 consume.

## Evidence run (all read-only; no gate executed by me, no installs performed)

| # | command | exit | key output |
|---|---|---|---|
| 1 | `git -C <lane> rev-parse HEAD` | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; `git status --porcelain` → only `?? .ufo/waves/`, `?? plans/round-47.md` |
| 2 | `git show c61a973:SCORECARD.md \| sed -n '101p' \| grep -c 'omp 18.12.3'` | 0 | `1` — the pre-registered r47 C1 baseline names omp **18.12.3**, `Before: surfaces 5/7, pins 1/3` |
| 3 | `/fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 --version` | 0 | `omp/18.12.5` |
| 4 | `sha256sum /fast/scratch/kotoba-r47/shared/bin/omp-18.12.5 .../opencode-1.19.3` | 0 | `fdbc8136…` / `179ca421…` (matches `before/SUMMARY.md:11-12`) |
| 5 | `test -e /home/vgpnk/.opencode/bin/opencode` | 1 | the path hardcoded as both instruments' default is gone: `verifiers/verify_surfaces.py:130`, `verifiers/check_substrate_pins.py:63` (override flags exist at `verify_surfaces.py:1035`, `check_substrate_pins.py:306`) |
| 6 | `ls -l /home/vgpnk/.local/bin/opencode` | 0 | 1460-byte **bash script**, `package="opencode-ai"`; not executed (lane rule) |
| 7 | `git show c61a973:verifiers/baseline.json \| sed -n '1,12p'` | 0 | pins `9513ef9f…` (the r44 note: `omp/18.12.2`) + `d9123b9b…` — a third opencode sha, while r47 sees `179ca421…` |
| 8 | `git show c61a973:corpus/QUALITY.md \| grep -c 'Q19'` | 1 | `0` — Q19 does not exist at BASE |
| 9 | `git show c61a973:corpus/lessons/round-46.md \| sed -n '13,37p' \| grep -c 'Timestamp'` | 1 | `0` — the timestamp defect is in the Gate prose (`corpus/lessons/round-46.md:77`), not in any M1–M19 row |
| 10 | `git show c61a973:corpus/README.md \| sed -n '74p' \| grep -c '18.12.3'` | 0 | `1` — the Frontier row carries the same stale substrate |
| 11 | `git show --stat --oneline c61a973` | 0 | `1 file changed, 17 insertions(+)` — the spot-check file landed alone |
| 12 | `.ufo/waves/round-47/before/SUMMARY.md:3-12` | — | surfaces default exit 2; override 4 PASS / 3 FAIL; pins exit 2 DRIFT 3/3; checklist 9/10; corpus 2 DRIFT; harness 21/28 |

`plans/round-47.md` and everything under `.ufo/waves/round-47/` are untracked at BASE; line citations to them are working-tree only and are marked so.

## Which criteria govern each claim

### C1 — freshness (re-derive + re-pin omp 18.12.5 / opencode 1.19.3)

| row (BASE line) | governs | concrete hook / hazard |
|---|---|---|
| Q09 `QUALITY.md:20` | primary: re-derive then re-pin; `"no rebaseline" is open debt, not a pass` | the 7 surfaces checks (`verifiers/verify_surfaces.py:175-181`) and 3 pins (`verifiers/check_substrate_pins.py:116-118`) must return to 7/7 and 3/3 at the **default** resolution, not via `--opencode-binary`; the default is the dead path at `verify_surfaces.py:130` / `check_substrate_pins.py:63`, so C1 must change the resolution rule or the default, not only the invocation — a plan that prints the override command as "after" is vacuous |
| Q10 `QUALITY.md:21` | measurement identity | the live binary moved between r44 and r47 (18.12.2 pinned → 18.12.3 measured → 18.12.5 live); every number in the after-state names the frozen snapshot sha, not the live path |
| Q14 `QUALITY.md:25` | negative claims | the 0/8 vacuity (`before/SUMMARY.md:4`) must be **retired with its sweep**, not fixed by deleting classes; re-verdicted classes carry the search |
| Q02 `QUALITY.md:13` | exhaustiveness | "8 loader classes" is a measurement from 18.12.3; if 18.12.5's class space is claimed complete, name its generator (`strings`/loader-rule derivation + seed), not the old list |
| Q18 `QUALITY.md:29` | tolerated input | the new `--opencode-binary` input class (npx-cache ELF) plus the extraction fixtures must keep control arms green; a false red on the frozen 1.19.3 ELF is harm |
| Q05 `QUALITY.md:16` | fix ships its arm | mutation seats `C1MutationSurfaces`/`C1MutationPins`; a re-pin with no mutation arm is unscored |
| Q03 `QUALITY.md:14` | record vs tree | `verifiers/baseline.json:5` pins 9513ef9f (18.12.2), while LOG.md:2270 records 18.12.3 installed in r46 — the pin block was already a record-vs-tree drift at BASE, before r47 touched it |
| Q13 `QUALITY.md:24` | counts | `7/7 — python3 -B verifiers/verify_surfaces.py --json <date>`; the plan prints the command without a date at `SCORECARD.md:101` |
| Q11 `QUALITY.md:22` | evidence sizing | strings dumps stay in `/fast/scratch/kotoba-r47/shared/` (lane Q11 rule) |

Not governing C1: Q01/Q06/Q07/Q12/Q15/Q16/Q17. Q16 is the **round** verdict's rule, not the per-claim measurement's; do not use it to excuse a self-measured claim.

Counterexample to the planned after-state: `SCORECARD.md:101`'s `After: 7/7, 3/3` fixes the target on the 18.12.3 check set. If 18.12.5 changes the class generator, a literal 7/7 can be met while Q02/Q14 fail. The plan's own `before/SUMMARY.md:4` already shows 4/7 at the override — so the after must be stated per-check-id, not as a fraction.

### C2 — operability (semantic `description` XML-tag check + remove `<skills>`)

| row | governs | hook / hazard |
|---|---|---|
| Q08 `QUALITY.md:19` | primary: "no XML tag inside `description:`; a structural parse is not a semantic pass" | the check lands beside the structural parse at `verifiers/verify_skill_checklist.py` (the round-16 limit text is at line 76); the lane's own `SKILL.md` `<skills>` is the same row |
| Q05 `QUALITY.md:16` | regression arm | `--self-test` must reject the planted tag and keep the assertion floor moving in step |
| Q18 `QUALITY.md:29` | control arms | folded/literal block scalars, quoted strings, a tag-free description, XML-looking **body** text, and tags in other frontmatter fields must stay green; the seats `C2FoldedParse`/`C2Battery`/`C2SimplifyFrontmatter` exist for this |
| Q13 `QUALITY.md:24` | counts | before `1 — grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md) <date>`; after `0 — same command <date>`; assertion count names the floor bump (`verifiers/floors-registry.json:5-7`, floor 1597) |
| Q04 `QUALITY.md:15` | commands | the same instrument carries `governance.citation_resolves` (`verifiers/verify_skill_checklist.py:1454-1494`); a C2 edit that breaks C3's gate is harm between claims |
| Q12 `QUALITY.md:23` | source discipline | S003 is **Anthropic-only** (`corpus/SOURCES.md:16`: "an Anthropic-only rule the open spec lacks"); if a knowledge entry lands, its scope must say so, and Q12's trio applies |

Counterexample: a check that reports "XML tags are invalid per the Agent Skills spec" would overstate S003 — S001's spec has 0 mentions (`corpus/SOURCES.md:16,24`). The failure text must attribute the rule to the vendor source, or the check exports a false universal.

### C3 — calibration (erratum registry + corpus index row)

| row | governs | hook / hazard |
|---|---|---|
| Q04 `QUALITY.md:15` | primary: "pruning a runner turns the gate red, not the citation silent" | Q04's own evidence pointer is `LOG.md:2111` (`corpus/lessons/round-46.md:22`); the registry is the *narrow* exception that keeps Q04 honest |
| Q03 `QUALITY.md:14` | record names the commit | the SCORECARD row and the registry file must name the commit that holds them; `c61a973` is the closure commit, not a candidate |
| Q05 + Q18 | arms, both directions | errata-keyed absent path PASS and named; errata key whose token/line moved FAIL; an errata key for a **live** path FAIL (a pre-excused live citation is a false green); the three existing governance arms (`verify_skill_checklist.py:2026-2062`) stay green |
| Q14 `QUALITY.md:25` | the absent runner is a negative claim | the LOG line already carries its sweep (command + exit 2 + "absent"), which is why an erratum is legitimate here and a bare dead path at another line is not |
| Q13 `QUALITY.md:24` | counts | `10/10 — python3 -B verifiers/verify_skill_checklist.py --json <date>`; `0 DRIFT — python3 -B verifiers/verify_corpus_integrity.py --json <date>` |
| Q16 `QUALITY.md:27` | non-author verdict | the spot-check file is integrator-authored (`c61a973`, `git show --stat` above); the closure still needs a non-author re-read |
| Q12 | knowledge | not claimed this round; if the erratum design lands a knowledge entry, the trio applies |
| Q19 (proposed) | the erratum itself | see below — the registry is an exemption and must expire with its anchor |

Counterexample / landing-order trap: `verifiers/corpus-baseline.json:57` records `tracked_files 55 -> 58` for the r46 landing; adding the index row for `corpus/lessons/round-46-verifier-spotcheck.md` makes 59, so the baseline's `corpus.index.tracked_files` (`verifiers/corpus-baseline.json:13`) must move 58 → 59 **in the same landing**. Index row alone leaves the gate red for a new reason; baseline alone is a fitted denominator with no file. Both, or neither.

### Frontier step (SOURCES workflow; `plans/round-47.md:14-16`)

- Q12 `QUALITY.md:23` — each admitted knowledge entry opens with `source: S###` + anchor, `verified-at:`, `recheck:` that runs.
- Q13 `QUALITY.md:24` and Q14 `QUALITY.md:25` — the search log's identified/screened/included/excluded counts and any "no row exists" claim carry command + date and the sweep (`corpus/SOURCES.md` contract rule 5).
- Q10 `QUALITY.md:21` — fetched sha256 before/after; a live page that changes mid-round invalidates the quote (the r46 fetch log records shas; the `18:40Z` vs `21:40Z` defect at `corpus/lessons/round-46.md:77` is the same family applied to time).
- Q04 `QUALITY.md:15` — `recheck:` cadence must be a date or a real trigger (`on-release`, `90d`); the substrate rows' 90d is meaningless when the substrate moved twice between rounds (evidence #2-#7).
- Q11 `QUALITY.md:22` — the fetch log is cited, not multiplied.
- Q19 (proposed) — the Frontier row `corpus/README.md:74` is a carried record and would have to name its round/substrate; at BASE it still says "omp 18.12.3 … 5/7 … 1/3", and `PROVINCE.md:21` repeats it.

## Does this round's mined mistake already have a captured-by row?

| mined class (seat) | nearest existing rows | verdict |
|---|---|---|
| **stale-premise** (`MistakeStalePremise`): plan baseline measured on 18.12.3, spent on 18.12.5; pinned opencode path gone | Q09 — but Q09 *explicitly permits* a debt close ("`no rebaseline` is open debt, not a pass"), and r46 closed on exactly that debt (`LOG.md:2314`); Q10 — source moving **during** a run, not between observation and use; Q03 — the stale record does name a commit, just not a substrate sha/version; Q13 — the plan names the command, not the observation | **not captured** → Q19 |
| **landing** (`MistakeUnindexedLanding`): `corpus/lessons/round-46-verifier-spotcheck.md` landed alone (`git show --stat c61a973`), gates red at HEAD (`before/SUMMARY.md:7`) | instrument `corpus.index.unindexed` + `corpus.index.tracked_files` (`verifiers/verify_corpus_integrity.py:629-631`, baseline `:13`); fleet rule `/home/vgpnk/Projects/shokunin/CORPUS.md` § Rules "An index row is a claim" | **captured, but a round late** — no QUALITY row; the capture is mechanical, not a criterion |
| **sweep-others** (`MistakeSweepOthers`): S001–S008 `accessed_utc` labelled `Z` at 18:40 while local time was 21:40 (`corpus/lessons/round-46.md:77`) | Q12 — field presence, not correctness; Q13 — a date, not a zone; Q10 — a sha, not a clock | **not captured** → Q19's observation-time clause |

r46 open residuals (`corpus/lessons/round-46-verifier-spotcheck.md:17`), mapped for completeness (state reproduction is `C3Residuals`' seat, not mine):

| residual | captured-by |
|---|---|
| printed C1 counting command exits 2 as written | **Q04** (`QUALITY.md:15`) |
| `SKILL.md` description carries `<skills>` | **Q08** (`QUALITY.md:19`), closed by C2 |
| payload can mark committed rows out of scope | **none today** → Q19's exemption clause (a payload-declared exemption is an exemption) |
| mirror-map-removed input passes | none; same exemption shape if the payload declares it — `[INFERENCE]`, not reproduced here |
| row with no verdict / `NaN` / case-variant keys pass | none — a false green in instrument tolerance (see deferred Q20 note) |
| mismatched row-level `kind` passes | none — same false-green class |

## Proposed move — Q19 (candidate row, advice only)

| id | criterion | applies to | grounded in | supersedes |
|---|---|---|---|---|
| Q19 | A carried record — before-value, pin, gate count, frontier row — and any exemption that suppresses a gate (erratum, scope-out, payload opt-out) name the anchor they were true against (commit/sha, `file:line`, token, observation time with zone) and are re-derived by the round that spends them; a moved anchor retires the value with its failing command and voids the exemption. | round plans/carried measurements; gate exemptions | M9 Gate regressions found a round late (substrate rebuild); M14 Unstable source during a measured run; M4 Dead recheck/source command | — |

Why this row and not a narrower one:

1. **Q09's carve-out is the hole.** Q09 says a missing rebaseline is "open debt, not a pass" (`corpus/QUALITY.md:20`). r46 took that debt legitimately (pins 1/3, surfaces 5/7 at `LOG.md:2314`), and the r47 plan then spent the debt-state numbers as its baseline (`SCORECARD.md:101`). No existing row forbids spending a debt-state measurement as the next claim's before-value. Q19 does, without retracting Q09's permission to close on debt.
2. **The interval is uncovered.** Q10 covers inside a run (before/after sha); Q09 covers the gate after a rebuild. Q19 covers *between the observation and its use* — the two-round gap in evidence #2-#7 (18.12.2 pinned → 18.12.3 seen → 18.12.5 live).
3. **The exemption clause is the C3 synthesis.** C3 adds an erratum registry keyed on `LOG.md:2111` (`plans/round-47.md:34-36`). Without Q19, a line-keyed registry makes the governance gate satisfiable by declaration: any dead citation can be excused by adding a row, which turns the calibration axis self-attested. With Q19, the erratum is a record that must carry `(file, line, token, observation)` and void when the line's token moves.
4. **It captures a carried r46 residual for free** — "payload can mark committed rows out of scope" is the same exception class (self-declared exemption without a committed anchor). This is a capture, not a closure claim; `C3Residuals` owns the state.
5. **It is mechanically enforceable in two places**: the landing half by the existing battery practice (r46's `.ufo/round-46/evidence/w2/gates/` ran a before/after battery; the unindexed file would have failed at landing), and the use half by a plan-vs-before check (extract each `Before:` cell, re-run its command, FAIL on mismatch).

Lesson it would cite: `corpus/lessons/round-47.md` § Mistakes, the `MistakeStalePremise` row — with evidence #2 (stale `SCORECARD.md:101`), #3 (omp/18.12.5), #5 (pinned path absent), #7 (pin block already 18.12.2/d9123b9b), #12 (before summary contradicts 5/7 and 1/3). Secondary: the same numbers at `corpus/README.md:74` and `PROVINCE.md:21` (evidence #10) — the class is in the *records*, not only the plan.

Fix that can fail (required by the fleet rule "a fix is shown able to fail before it counts"):

- Planted red: keep `SCORECARD.md:101` at `Before: surfaces 5/7, pins 1/3` while `before/SUMMARY.md:3-5` shows default exit 2 and pins 3/3 failed → a plan-vs-before check must FAIL naming the cell and the re-derivation command. Green control: the same plan with the cells replaced by `observed — command — date` passes.
- Erratum arms for `verify_skill_checklist.py` (Q05/Q18): (a) errata-keyed absent path PASSES and the detail names the erratum; (b) the same erratum with a token that no longer matches the line FAILS; (c) an erratum keyed to a path that **exists** FAILS (false-green control); (d) the three existing governance arms (`verifiers/verify_skill_checklist.py:2026-2062`) stay green.
- Floor bump in step: `verifiers/floors-registry.json:5-7` (checklist floor 1597) moves once. C2 and C3 both edit this instrument, so a serial landing needs an intermediate floor and a joint landing needs the final count; otherwise one claim's after-value is unmeasurable in isolation (separability harm — flag to `ConnClaimSeparability`/L1).

Affected axes: calibration improves (C3's registry becomes governed and the stale records get an expiry rule); freshness improves-or-neutral (C1's before-value is re-derived; no extra substrate work); operability neutral (no accepted-input change in `compare_*`/`verify_surfaces`). No row retires.

## Contradictions and risks (stated, not smoothed)

1. **Grounding header blocks a round-47-authored row.** `corpus/QUALITY.md:8-9` says `grounded in` names the class row in `corpus/lessons/round-46.md` § Mistakes. An r47-mined class cannot ground Q19 under that sentence. Resolution proposed: ground Q19 in M9+M14+M4 (all present at `corpus/lessons/round-46.md:27,32,22`) and cite the r47 row only as the lesson's evidence. Widening the header to "the round lesson that mined it" would let a same-round mistake self-certify its own criterion; do not widen it. If the integrator prefers the r47 row as the grounding, that is a header edit first, then the row — and the header edit is prose, not an append, so it needs to be recorded in the round lesson.
2. **Q19 vs Q09 overlap.** Q19 must not supersede Q09. Q09 is the gate-side rule that made r44/r46 land; Q19 is the record-side rule. If forced to one, superseding Q09 (`supersedes: Q09`) would retire the sharpest freshness rule the lane has, on weaker evidence. Recommend no supersession.
3. **C3 creates the false-green surface.** A registry that can excuse any `file:line` is a widening; Q18 covers false *red* only. Q19's exemption clause plus arm (c) above are the minimum guard. This is the second-order effect where C3's fix could harm the very axis it improves.
4. **Deferred candidate, not proposed this round:** a Q20 for instrument tolerance ("a row missing its verdict, a non-finite number, a case-variant key, or a self-declared opt-out is not accepted input; widening tolerance ships a near-miss arm that stays RED"). It would be grounded in M17/Q18's sibling direction and cover three open r46 residuals, but it is a different class from stale-premise and C3Residuals owns their current state; adding it now would double the round's criteria surface.
5. **Stale records are plural.** The stale numbers live at `SCORECARD.md:101`, `corpus/README.md:74`, and `PROVINCE.md:21`. Fixing only the plan's before-cell leaves two Frontier/Province records claiming 18.12.3 after C1 lands. Q19's "frontier row" clause is what makes those edits required, not optional.
6. **C1's 21/28 harness debt is Q09-scoped, not closed by C1.** The plan names it (`plans/round-47.md:41-45`); Q09's "open debt, not a pass" is the right disposition, but under Q19 the debt cannot become an r48 baseline either.

## What I did NOT check

- I ran no gate: no `verify_surfaces.py`, `check_substrate_pins.py`, `verify_skill_checklist.py`, corpus instrument, or batteries. All gate results cited are the recorded before-measurements (`before/SUMMARY.md` and the five `.out` files, 12:10-12:11 host time) or printed in the report above.
- I did not reproduce the six r46 residuals; `C3Residuals` owns that. My "no captured-by" verdicts for the three false-green residuals and the mirror opt-out are row-text analysis, not measurement (the mirror one is marked `[INFERENCE]`).
- I did not open S003's live page (network); the Anthropic-only scope is taken from `corpus/SOURCES.md:16` and the round-46 record.
- I did not read `verifiers/compare_harness_independent.py` beyond the records' descriptions, so the exact `kind`/`NaN` tolerance sites are unverified here.
- `plans/round-47.md`, `.ufo/waves/round-47/**`, and the r47 lesson (which does not exist yet; `.ufo/round-47/claims.json` is also absent) are not at BASE — those citations are working-tree only.
- No tools installed or upgraded; no pacman/npx/uv invocation (`~/.local/bin/opencode` was read, never executed).
