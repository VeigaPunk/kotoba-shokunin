# MineMistake — round 50 build seat (frontier step: mined mistake + QUALITY row)

Seat: `KotobaR50.MineMistake` (scribe, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
branch `master` at `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. Ran 2026-10-22, 12:19Z–12:37Z.
No lane file was written except this report; all mutations ran in
`/fast/scratch/hyaku/kotoba-r50/build/MineMistake/lane` (private clone of the lane).

## Result

DRAFTED: the class "a claim headline wider than its counter" is **not** covered by any existing
criterion, so a **new row Q26** is drafted (not a superseding row); the round-50 lesson `## Mistakes`
row **M31** is drafted. Q26 **fails** both round-49 claim statements and **passes** both round-50
statements (round-50 C1 passes only once the cited `--skill` guard arm lands — at base that clause
is unmeasured, so the honest base verdict is FAIL-until-guard).

## The class, and whether it is already covered

Round-49 shipped two headlines that assert more than their counting commands print:

- adjacency row (`SCORECARD.md:34` @ `374ecf98`): "all 20 sibling lanes classified at pinned sibling
  commits **from their own bytes** (9 adjacent, 11 none, **0 contested** …)".
- operability row (`SCORECARD.md:31` @ `374ecf98`): "**round 49 (C2 — dispatch-prompt boxes
  executed**; score held 8.5)"; `plans/round-49.md`: "The full `dispatch.08` box is executed, state
  clause included"; commit `c48793d` subject: "C2 dispatch-prompt boxes dispatch.04/dispatch.08
  **executed** by verify_dispatch_prompts.py"; instrument docstring
  (`verifiers/verify_dispatch_prompts.py:738-742`, the `box_proof` docstring): "…the committed fixtures
  discriminate **every conjunct**".

Coverage check over `corpus/QUALITY.md` Q01–Q25: no row binds the **clauses of a statement** to what
the counter measures. Q13 (count carries its command), Q14 (negative claim carries its sweep),
Q19 (stale planned premise), Q01/Q02 (closure/exhaustive claims) are all met in form by the round-49
claims. Q25 is the closest and was **met in form**: each counter was shown able to fail ("remapping
one box to an unrelated instrument or turning one mutant fixture into a passing file prints `boxes
proven 1`, exit 1") and each claim cited a content guard. Q25 binds the *counter* side; it has no
clause about the statement. The overclaim survived Q25, so the class needs its own row: **Q26,
`supersedes` = `—`**.

## Draft row Q26 (`corpus/QUALITY.md`, table's exact column shape)

| Q26 | A claim's headline asserts nothing its counter does not measure: every clause of the statement (each quantity, provenance, coverage or universality claim) is turned on by the counter's output or by a cited guard whose exit code changes when that clause is falsified; a clause neither turns on is dropped from the statement or the statement is bounded to what the counter prints. The counter side stays with Q25, which this row does not supersede. | claim statements and headlines (plans, SCORECARD rows, LOG entries, commit subjects, lesson prose) | M31 A claim's headline asserted properties its counter never measured (`corpus/lessons/round-50.md` § Mistakes) | — |

## Q26 is able to fail — the four applications

Test procedure (per claim): list the statement's clauses; for each, ask whether the counter's output
or a cited guard's exit code turns on it; falsify the clause by mutation and watch counter and guard.

**1. round-49 C1 — FAILS.** Counter: the row-count awk (`SCORECARD.md:34`, `plans/round-49.md`).
Clauses "from their own bytes", "9 adjacent, 11 none" and "0 contested" are turned on by nothing:
the counter prints one integer (20); the census's own `names kotoba` column reads `no` for **7 of the
9** `adjacent` rows, so their class rests on kotoba's own description, not the sibling's bytes;
on a clone with kake reclassified `contested` (census + `PROVINCE.md`, consistently) the counter still
prints **20** and the cited guard still exits **0** while the split becomes 8 adjacent / 1 contested /
11 none. "0 contested" is unruled anyway (routed D3). → headline wider than its counter.

**2. round-49 C2 — FAILS.** Counter: `boxes proven 2`. The headline "boxes executed" / "the full
`dispatch.08` box is executed, state clause included" claims the whole box text; the proof covers six
named conjuncts with one fixture each; `LOG.md:2382` names **four** box clauses with no fixture
(unsubstituted variable before the report path, non-digit round folder, `≤` equality boundary,
legacy-state arm), `SKILL.md:131-133` names three of them and `SCORECARD.md:255` names two — the
count differs per surface, so the four-clause list is the one to cite. The proof does not enforce its own
coverage: deleting a must-fail case still prints `boxes proven 2`, exit 0 (round-49 falsify
`ReplayC2BoxProof` M1/M2/M3/M5/M6; reproduced here). The `every conjunct` docstring (D2) is false as
written (`ReplayC2BoxProof` F5). → headline wider than its counter.

**3. round-50 C1 — PASSES once the cited guard lands; FAIL at base on one clause.** Statement:
"kotoba's `SKILL.md` frontmatter names the census lanes classed `adjacent` or `contested` in
`corpus/knowledge/sibling-overlap-census-round49.md`: 5 of 9 → 9 of 9." The count clause is exactly the
counter's output (measured **5** at `f3046466`). The membership clause ("the census lanes classed
adjacent or contested") is **not** printed by the counter — its name list is hardcoded in the regex —
so it must be turned on by the cited guard. At base that guard command does not exist:
`check_sibling_census.py` has no `--skill` flag (exit 2, "unrecognized arguments: --skill SKILL.md").
PASS conditions: (a) the guard lands with a `--skill` arm whose exit code turns on a missing non-none
lane (exit 1), and (b) the D3 precedence ruling re-declares the 9-lane list before landing (the plan
already commits to this). Seat `KotobaR50.CensusGuard` reports that condition (a) is exactly what its
arm does — it reads the `SKILL.md` frontmatter description, takes the census lanes classified
non-none, and exits 1 naming each such lane that is not a whole-token case-insensitive match, printing
`names 5 of 9` on the base description (missing chousa, kama, kotodama, tameshi) (peer message,
2026-10-22; not measured by me).

**4. round-50 C2 — PASSES.** Statement: "deleting any one of the 6 must-fail cases from
`verifiers/fixtures/dispatch-prompts/manifest.json` makes `--box-proof` exit 1: 0 of 6 → 6 of 6." The
counter prints `killed K of 6` — the statement *is* the counter's output and exit rule; the
instrument's failure exit really is 1 (`box_proof` returns 1 when `proven != 2`; 2 only for an
unreadable map/manifest). One condition: the driver must read the case set and N from the manifest
(6 must-fail cases at base: d04-placeholder, d04-stem, d04-unknown-lane, d08-role-round,
d08-report-dir-round, d08-above-state) rather than hardcode 6, else a 7th case is unmeasured.

## Draft row M31 (`corpus/lessons/round-50.md` § Mistakes — the file does not exist at base; paste into
the § Mistakes table with the round-49 header `|class|evidence pointer (command → output)|captured-by|fix|`)

| M31 A claim's headline asserted properties its counter never measured (twice in round 49: the adjacency row's "from their own bytes … 0 contested" and the operability headline's "executed") | `git show 374ecf98:PROVINCE.md \| awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' \| grep -cE '^\| (audio\|chousa\|…\|tsukuroi) \| (contested\|adjacent\|none) \| [0-9a-f]{40} \|'` → 20, exit 0 — one integer, no classification; the census's own `names kotoba` column reads `no` for 7 of the 9 `adjacent` rows, so "from their own bytes" is false on the census's own table; on a clone at `374ecf98` with kake reclassified `contested` in both the census and `PROVINCE.md` the same counter still prints 20 and the cited guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` still exits 0 (`rows 20 verified 20`, `province rows 20 matched 20`) while the split reads 8 adjacent / 1 contested / 11 none (seat `.ufo/waves/round-50/build/MineMistake.md`, 2026-10-22). C2: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → `boxes proven 2`, exit 0, while the headline says "dispatch-prompt boxes executed" and `plans/round-49.md` says "The full `dispatch.08` box is executed, state clause included"; the proof covers six named conjuncts with one fixture each and `LOG.md:2382` names four box clauses with no fixture (unsubstituted variable before the report path, non-digit round folder, `≤` equality boundary, legacy-state arm; `SKILL.md:131-133` names three, `SCORECARD.md:255` two), and deleting a must-fail case leaves `boxes proven 2`, exit 0 (`.ufo/waves/round-49/falsify/ReplayC2BoxProof.md` M1/M2/M3/M5/M6; reproduced 2026-10-22: six of six removals → exit 0, `boxes proven 2`, `killed 0 of 6`) | none → Q26 (Q25 was met in form: each counter was shown able to fail and a content guard was cited; Q13, Q14 and Q19 were met too — they bind form, not the statement) | Q26. The round-49 headlines are re-stated with their bounds (SCORECARD append; the `box_proof` docstring stops saying "every conjunct" — routed D2/D4), and both round-50 statements are written as exactly what their counters print (`plans/round-50.md` C1/C2: the frontmatter name count, and `killed K of 6` over the manifest's must-fail cases). |

## Evidence (commands, exit codes verbatim; all 2026-10-22)

| # | command (cwd) | output | exit |
|---|---|---|---|
| E1 | `git show 374ecf98:PROVINCE.md \| awk '/^## Adjacent/{f=1;next} /^## /{f=0} f' \| grep -cE '^\| (audio\|…\|tsukuroi) \| (contested\|adjacent\|none) \| [0-9a-f]{40} \|'` (lane) | `20` | 0 |
| E2 | same awk piped to `awk '{print $4}' \| sort \| uniq -c` (lane) | `9 adjacent`, `11 none` | 0 |
| E3 | census table scan: `names kotoba` cell of the 9 `adjacent` rows (lane) | 9 adjacent rows, 7 of them `no` | 0 |
| E4 | clone at `374ecf98`, kake `adjacent`→`contested` in census **and** `PROVINCE.md`: declared C1 counter | `20` (split 8 adjacent / 1 contested / 11 none) | 0 |
| E5 | same clone: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | `rows 20 verified 20` / `province rows 20 matched 20` | 0 |
| E6 | lane at `f3046466`: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | `error: unrecognized arguments: --skill SKILL.md` | 2 |
| E7 | lane at `f3046466`: C1 counter `git show f3046466:SKILL.md \| awk 'NR==1&&/^---$/{f=1;next} f&&/^---$/{exit} f' \| grep -oiwE 'chousa\|kagi\|kake\|kama\|kasegi\|kengaku\|kotodama\|kumitate\|tameshi' \| sort -u \| wc -l` | `5` | 0 |
| E8 | scratch driver `driver.py` over the `f3046466` tree: remove one must-fail case at a time, run `--box-proof` | 6 × `boxes proven 2`, exit 0; `killed 0 of 6` | 0 |
| E9 | `verifiers/verify_dispatch_prompts.py` manifest at `f3046466` | 9 cases: 2 PASS controls, 6 must-fail, 1 N/A | 0 |
| E10 | `verifiers/verify_dispatch_prompts.py:737-826` (read) | `return 0 if proven == 2 else 1`; `2` only for unreadable map/manifest | — |

## Surfaces that carry the round-49 overstatement (for the fix cell)

Measured by seat `KotobaR50.D2D4Wording` (2026-10-22) and consistent with my own reads: "0 contested"
survives on `SCORECARD.md:34`, `corpus/README.md:69` and `corpus/knowledge/sibling-overlap-census-round49.md:99`;
"from their own bytes" survives on `SCORECARD.md:34` and on the census entry's own opening
(`corpus/knowledge/sibling-overlap-census-round49.md:10`, "from each sibling's own committed bytes at a
pinned commit"); `LOG.md:2371` carries "0 contested" in the round-49 landing record (append-only, so
the correction is appended, not rewritten). The fix therefore has to reach the census entry itself, not
only `SCORECARD.md`.

## Touched surfaces, artifacts, limits

- Lane files written: **this report only** (`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-50/build/MineMistake.md`).
- Artifacts (all under `/fast/scratch/hyaku/kotoba-r50/build/MineMistake/`): `patch.diff` (appends the
  Q26 row to `corpus/QUALITY.md`; `git apply -p0 --check` → exit 0 against `f3046466`),
  `driver.py` (the case-deletion driver used for E8), `lane/` (private clone, mutations reverted).
- L1 note: apply `patch.diff` only if `grep -c '^| Q26' corpus/QUALITY.md` is 0; `corpus/lessons/round-50.md`
  does not exist at `f3046466`, so M31 must be pasted into the § Mistakes table of the lesson file the
  round creates (the row text above is paste-ready; M31 is the next free number after M29/M30).
- No web source was opened; no tool was installed or upgraded (nothing to record).
- Out of scope for this seat: the SCORECARD/D2 wording fixes (seat `KotobaR50.D2D4Wording`), the
  `--skill` guard arm (seat `KotobaR50.CensusGuard`), the box-proof coverage driver (seat
  `KotobaR50.CaseDeletionDriver`); I did not edit the plan, SCORECARD, LOG or the census entry.
- Conflicts: none observed; the only coordination was with `KotobaR50.SrcOpencodeDocs` (I claim no
  `corpus/SOURCES.md` row, so no S-id is taken by this seat).
- Lane state observed during my run (not mine, left untouched): at 12:38:43Z the lane working tree
  carried an in-place modification of `verifiers/verify_skill_checklist.py` (+212/−12, the round-50 D2
  gate half). `git status --porcelain` in the lane showed ` M verifiers/verify_skill_checklist.py`
  alongside the untracked `.ufo/waves/round-50/` and `plans/round-50.md`. My own writes are this report
  and the scratch clone only.

Report: `.ufo/waves/round-50/build/MineMistake.md`
