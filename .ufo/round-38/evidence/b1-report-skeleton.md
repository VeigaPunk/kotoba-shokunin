# kotoba — round 38 report (2026-10-19) — SKELETON v1

> Scribe seat B1. Cells filled from late-arriving seat reports in `.ufo/round-38/scouts/`.
> Shape mirrors `.ufo/reports/round-37/kotoba.md`. Every filled cell carries a seat citation;
> unfilled cells stay `[PENDING]` — never smoothed. Re-measure at the landing commit.

Lane: `kotoba-shokunin`. Round 38, loop A position 2 of 12 (operator's fresh 3-loop regimen).
Dispatch HEAD: `cb4e0f3`. Work commit: `[PENDING]`.
Claims: **C1** depth (close the r37 source-blind re-derivation) · **C2** operability (V4's two floors-guard residuals) · **C3** freshness (V6 container-relative fence + battery + routing pin) — `.ufo/round-38/claims.json`.
Provider: `devin/deepseek-v4-1-flash-max` (operator amendment 2, 2026-10-19: token-plan family exhausted — attempts 1/2 both 429; resets 11-11/10-23/10-28).
Swarm: `[PENDING]`/24 seats.
Status: `[PENDING]`.

## C0 — dispatch-HEAD state (scribe-measured before any r38 work)

- **The checklist gate is RED at the dispatch HEAD `cb4e0f3`, and r37's own work commit `c8e233d` introduced it** — B1 attribution probe: 0 non-resolving governance tokens at `041f6ba` (r37 dispatch), **3 at `c8e233d`**, same 3 at `cb4e0f3`; r36 had `273` subjects / `0` bad, HEAD has `293` / `3` bad. Seat B2's independent `gov-provenance.py` reproduces the same three, identical line numbers.
  - `python3 verifiers/verify_skill_checklist.py` → `FAIL governance.citation_resolves: evaluated 293 — SCORECARD.md:131: '.ufo/round-37/scouts/{P5,P6,V4,V5,I1,I2,S2}.md' does not resolve …; SCORECARD.md:132: …; SCORECARD.md:133: …`, exit 1. Transcript: `drafts/b1/gate-battery-baseline-r38.txt`; attribution: `drafts/b1/citation-probe.txt` + `drafts/b1/b2-gov-provenance-crosscheck.txt`.
  - Cause (B1 mechanism probe, `drafts/b1/c0-mechanism.txt`): `citation_subjects` filters tokens containing `<>*?$` but **not braces**. SCORECARD's older brace tokens all carry a trailing `*` (`.ufo/round-21/scouts/{F,R,S,M}*.md`) and are dropped; r37's three brace-sets carry **no `*`**, so they enter the subject list as literal paths and fail `citation_resolve` — 041f6ba: 137 subjects / 0 brace-bearing; c8e233d: 151 subjects / 3 brace-bearing, all failing. **This falsifies two r37 record lines, both added by `c8e233d`** — `.ufo/reports/round-37/kotoba.md:32` ("gates green at `c8e233d`") and `LOG.md:1364` ("Whole-tree battery green at close … checklist 10×PASS"; measured 9 PASS / 1 FAIL at that commit). A carried red, `[PENDING: whether r38 fixes it or records it as carried]`.
  - Other 7 gates green at `cb4e0f3`: harness `28/28`, floors `6 × PASS (10/119/59/87/1584/62)`, corpus_integrity `9/9`, corpus_independent exit 0, surfaces 7 × PASS, pins `OK 3/3 (delta 0 ns)`, fault self-test `T1..T4 PASS / OK`.
- C1 before-state re-measured at `cb4e0f3`: `python3 verifiers/compare_harness_independent.py` → **exit 1 — headline 23/28, strict 17/28, 5 disagreements** (`oc.dup.roots_both_sided` 3 vs 0; `oc.log.skills_tag_hits` 13 vs 0; `omp.catalogue.{found,matched,total}` None vs live). Instrument self-tests already green: IND `0 failure(s) over 71`, CMP `0 failure(s) over 59`.
- **C1(a) adjudications independently confirmed by B1 on raw substrate** (`drafts/b1/c1-substrate-probe.txt`, log `~/.local/share/opencode/log/opencode.log`, 922,296 bytes): `grep -c -o '<skills>'` → **0** while `grep -o 'skills="' | wc -l` → **13** (IND counts the attribute, HAR the XML literal — definitional, harness side wins the id); `grep -c 'duplicate skill name'` → **0** (HAR's population). The three `omp.catalogue.*` rows are scoped out by name with the blindness blocker. Doc: `corpus/knowledge/harness-independent-round37.md` (W1's slice, §1–§6 shape, 303 lines, untracked at write time).
- Floors registry at `cb4e0f3` carries **6** instruments (harness/corpus_integrity/corpus_independent/surfaces/checklist/pins) — the C1 registration leg (IND 71 / CMP 59) is open.

## Work performed

- **C1 — landed on the measured legs, with two recorded dissents.** Adjudicated the 5 open rows with substrate probes (the two live disagreements resolve to the harness: `oc.log.skills_tag_hits` counts `skills="` — 13 on raw substrate — while IND counts the `<skills>` XML literal, 0 live; `oc.dup.roots_both_sided` 0 duplicate-name lines) and formally scoped the 3 `omp.catalogue.*` families OUT by name with the blindness blocker; the comparator gained a `SCOPED_OUT` mechanism (absent at dispatch — S1 F2) and now exits 0. Freeze receipt committed (A1: both captures sha'd before the join); corpus doc landed (`corpus/knowledge/harness-independent-round37.md`, §1–§6); both instruments registered (8 rows, floors 71/59). Seat citations: A1, W1, P1, R1, V2, S1, S2.
  - **Dissent (A1, reproduced by B1):** the doc's §3 files `oc.log.init_count_monotone` and `oc.roots.plugins_cache` as "D5 cosmetic / zero-delta representation". B1 planted a strictly *increasing* init-count log (no violation exists) → HAR `[]`, IND `1` — **different predicates, not two encodings** (code cites IND `:451-454` vs HAR `:489-493`); and the two `plugins_cache` arms read **different paths** (HAR `~/.claude/plugins/cache` absent; IND `~/.cache/opencode` exists, 0 entries), agreeing by coincidence of populations. Evidence: `drafts/b1/c1-substrate-probe.txt`, `drafts/b1/plant/`.
  - **Dissent (R1):** the exit 0 is "not earned as declared" — a self-consistent scope-out declaration can launder a real disagreement (R1-D1); plus R1-D2 (the above mis-filing), D3 (doc §1/§5 staleness — since refreshed to `24/24`), D5 (floors SLACK not EXACT), D6 (gates red at the frozen instant).
  - **Dissent (V1, reproduced by B1):** the claim's "every disagreement adjudicated and recorded" clause **FAILS AS DECLARED** — `oc.log.init_count_max` has **no adjudication ruling in any r38 artifact** (B1: 3 occurrences in the doc, all table/prose; 0 in A1's report), and the `init_count_monotone` ruling was dropped and re-classified cosmetic against its own fixture (V1 DEFECTS 1/2/6). The `24/24` is green over a surface where those rows agree *via the `zero` predicate*, not by matching predicates. V1 also measures floors `71/86` and `59/83` (stale, not EXACT); V3 corrects the claim text ("4 rows scoped out, not 3").
- **C2 — landed; the claim's two declared shapes close.** Non-str key: exit 1 raw `TypeError` → exit 2 class-named. Malformed 5→4-field tuple: 3 lines incl. the self-contradictory `floor drift … row=None` → a single `malformed row` line. Guard `--self-test` 41 → 68; live 8/8 PASS byte-invariant (sha `aff5a4a6…`). Seat citations: P4 (builder), B2, I2, R1, V4, S1.
  - **Dispute (V4, reproduced by B1):** the patch **introduces** a crash one site over — a `None` row *path* now exits 1 `TypeError` where HEAD named it exit 2 (`drafts/b1/c2b/independent-c2-findings.txt`).
- **C3 — landed.** Container-relative fence fix live; oracle **0/30** (was 4); `FENCE_SHAPES` 15 → 18; `--self-test` 1584 → 1597 with the floor bumped in-step; 145/145 checklist fixture files byte-identical; routing-16 pin re-issued `MATCH True`. Seat citations: P5, V5, V6b, S2, R2, I2.
  - **Dissent (I2):** withholds `improved` because the claim's "live byte-invariant" clause cannot hold over the C0 red gate. **Evidence gap (R1-D7, S2 F2/F4):** the committed `evidence/` scripts are not runnable as banked (`parents[]` depth, missing `shapes.json`); the oracle matrix used by the counting command is a **reconstruction**, not V6's byte-identical original.
- **Deliberately not done:** fixing the C0 carried red (SCORECARD notation is a governance file; the parent owns the publish commit); the IND floor bump 71 → 86; the blind-tree scrub-list repair; re-recording the corpus baselines; the divergence merge (operator).

## Landed changes

`[PENDING: work commit sha from the integrator]` — the working tree at this draft's write carries:
`verifiers/verify_harness_independent.py` + `verifiers/compare_harness_independent.py` (C1: SCOPED_OUT scope mechanism, predicate repairs), `verifiers/check_assertion_floors.py` + `verifiers/floors-registry.json` (C2 residuals + C1's 2 new rows, floors 1584→1597 in-step), `verifiers/verify_skill_checklist.py` (C3 container-relative fences + 3 battery shapes), `verifiers/fixtures/harness-independent/oc-log/case.json`, `verifiers/corpus-baseline.json` (re-record in flight), `corpus/knowledge/sibling-citation-routing-round16.json` (pin re-issue `214ae44d…`), `corpus/README.md`, `corpus/knowledge/harness-independent-round37.md` (new, untracked), `.ufo/round-38/`. **Not yet landed: the SCORECARD notation fix for the C0 red.**

## Before → after measurements

| Claim | Measurement | Before (dispatch HEAD `cb4e0f3`) | After (round 38) |
|---|---|---|---|
| C1 | comparator headline | **exit 1 — 23/28 (strict 17/28), 5 open rows** (scribe-measured) | **exit 0 — `24/24` (28 live checks, 4 scoped out), strict 19/24, 0 disagreements, 0 uncovered** — B1 re-run; `--expect-n 28` also exit 0. The scoping mechanism S1 F2 flagged as missing has landed |
| C1 | instrument self-tests | IND 0/71, CMP 0/59 green (scribe-measured) | IND **86**, CMP **83**, and the registry floors were **bumped in-step to match** — final sweep 13:51Z: `PASS harness_independent observed=86 floor=86`, `PASS compare_harness_independent observed=83 floor=83`, **8/8 EXACT, zero headroom** (the earlier 15-assertion slack is closed) |
| C1 | floors registry | 6 instruments, IND/CMP unregistered | **8 instruments, 8/8 EXACT — `harness_independent 86` + `compare_harness_independent 83`** (bumped in-step; B1 final sweep 13:51Z, guard `eaf5bf46…`) |
| C1 | blind-tree residual | n/a (no scrub this round) | **3 — NOT 0** (S2 F3: the banked scrub list predates the C1 instruments; `verify_harness_independent.py` + 2 fixtures leak). `[PENDING: fix or record]` |
| C2 | non-str key mutant | **exit 1 — raw `TypeError: can only concatenate str (not "NoneType") to str`** (B1 matched-mutant re-run at HEAD bytes) | **exit 2 — `FAIL registry non-string key: EXPECTED_INSTRUMENTS has None (instrument names must be str)`** (B1 re-run on working-tree patch) |
| C2 | malformed-tuple mutant | **exit 2 — 3 lines incl. `FAIL registry floor drift: surfaces registry=87 expected=87 row=None`** (self-contradictory) | **exit 2 — single `FAIL registry malformed row: surfaces (expected 5-field tuple)`, no extras** (B1 re-run) |
| C2 | guard self-test | 0/41 (scribe-measured) | **0/68 — grew 41→68** (B1 live re-run; I2 F6 independently reads 41→57 at an earlier mid-flight point) |
| C2 | NEW crash introduced by the patch | **exit 2 — `FAIL registry path drift: pins registry=verifiers/check_substrate_pins.py row=None`** (named) | **exit 1 raw `TypeError: unsupported operand type(s) for /: 'PosixPath' and 'NoneType'` at the guard's `main()` (`paths = {name: repo / spec[0] …}`)** — B1 matched mutation (`pins` row path → `None`) on head vs live bytes in an isolated 8-row world at guard sha `9500a9666dd4`. **A regression the before-state did not have**; V4 disputes closure on this, P4 says its scope is closed. Distinct shape from the claim's S (non-str *key*): this is a non-str row *value*. `[PENDING: fix or record]` |
| C2 | malformed-field arm (V4-H2) | **exit 2 — `FAIL registry malformed row: pins (non-integer floor)` AND the contradictory `FAIL registry floor drift: pins registry=62 expected=62 row=(62,)`** (B1 re-run on HEAD bytes) | **UNCHANGED — the same contradictory pair persists on the live patched guard** (B1 re-run, exact 8-row world, 13:54Z): `malformed row: pins (non-integer floor)` **plus** `floor drift: pins registry=62 expected=62 row=(62,)`. So the patch fixed the short-*tuple* arm but **not the malformed-*field* arm** — V4's H2 residual stands |
| C2 | live stdout byte-invariance | — | **byte-identical, sha `aff5a4a6…`** head vs patched (B1 `diff` → no output; measured at the frozen `6`-row state) |
| C3 | V6 matrix misclassifications | **4 mismatches / 30 probe lines** at `9ea386da…` (V6b/R2/V5 re-measured; container shapes S07 L6, S08 L7, S07b L7, S07b L10) | **0 mismatches / 30 lines, 18 shapes, spec-vs-cmark disagreements 0** — B1 independent re-run via `drafts/s2/oracle-fixed.py` at live sha `214ae44dcba4` |
| C3 | container battery shapes | `FENCE_SHAPES` 15 (no container shape) | **18** — the 3 container shapes landed; `checklist --self-test` **1584 → 1597** (B1 live re-run) |
| C3 | 71 checklist fixture dirs | 145 files (v6b pre-state manifest) | **145/145 `sha256sum -c` OK, 0 FAILED** — B1 independent check (byte-identical) |
| C3 | routing-16 pin | `9ea386da…` (r37 re-issue) | **RE-ISSUED: pin `214ae44d…` == live `214ae44d…` → `MATCH True`** (B1 re-run at 13:44Z) |
| gates | 8-gate battery | 7/8 green — **checklist RED** (scribe-measured) | **5/8 green at the final pre-landing sweep (13:51:23Z)**: harness / floors / surfaces / pins / fault exit 0; **checklist exit 1** (`governance.citation_resolves`, SCORECARD:131-133 — the C0 carried red, NOT fixed by C1/C2/C3); **corpus_integrity + corpus_independent exit 1** — 3 DRIFTs, **diagnosed by B1 as an ordering artifact, not a defect**: `verifiers/corpus-baseline.json` already expects `tracked_files=54` / `report_total=38`, while live reads 53/37 because `corpus/knowledge/harness-independent-round37.md` is still **untracked** (`git ls-files --error-unmatch` → "Did you forget to git add?"). Both corpus gates go green the moment the parent stages the doc. `[PENDING: landing-commit re-run]` |

Axis verdicts (scribe's evidence-backed recommendation; **the landing commit's re-run is the authority** — finding 8 of `scouts/B1.md` carries the recipe):

- **depth (C1) — contested; do NOT declare closed without settling D5.** Favorable, all re-measured by B1: comparator exit 1 → **exit 0 / 24/24** (strict 19/24, 4 scoped out by name); registry 8 rows **8/8 EXACT** after the in-step bump; corpus doc landed §1–§6; freeze receipt committed and ordering-verified (A1); the two open-row winners confirmed on raw substrate by B1's own probes; blindness-by-construction executable and green (V2); adjudication + scope-out + registration verify (A1, P1, P2, V3). **Against:** the "every disagreement adjudicated and recorded" clause **fails as declared** — `oc.log.init_count_max` has no ruling anywhere (V1; B1 grep), `init_count_monotone` is mis-filed cosmetic against its own fixture (A1 D-A; B1 plant proves different predicates), `plugins_cache`'s arms read different paths (A1 D-B; B1 confirmed) — and those are exactly the `zero`-predicate rows the green headline rests on; R1 adds that a self-consistent scope-out can launder a real disagreement. **Recommended: `improved` only after the two rows are re-adjudicated or explicitly re-opened; otherwise `failed-as-declared` on that clause with the mechanism credited.** V3's text correction: 4 rows scoped out, not 3.
- **operability (C2) — the claim's two declared shapes verify as declared.** Non-str key: raw `TypeError` exit 1 → named exit 2; malformed tuple: contradictory trio → single named line; self-test 41 → 68; live byte-invariant. **Caveat:** the patch introduces a crash on a `None` row *path* one site over (V4; B1 matched measurement) — recorded, unrefuted.
- **freshness (C3) — verifies on the measured legs, two reservations.** Oracle 4 → **0** mismatches/30 lines; `FENCE_SHAPES` 15 → 18; self-test 1584 → 1597 in-step; 145/145 checklist fixture files byte-identical; pin re-issued `MATCH True`; replays green (P6). **Reservations:** I2 withholds `improved` because the claim's byte-invariance clause cannot hold over the red checklist gate; the counting matrix is a **reconstruction** (the banked evidence scripts are not runnable as shipped — S2/R2/R1-D7).
- **consistency / coverage / calibration / adjacency — held**, except calibration carries the falsified r37 record lines below.
- **SHONEN — 4 × `[~]`, no `[x]`** (no named non-author verifier; PROTOCOL.md:63-68).

Drift handling (must be written into the published report):
- **Independent agreement at the settled tree:** the integrator's FINAL battery (I1, `drafts/i1/logs/final/summary.txt`, 13:55:45Z) matches B1's measurements at every point — same instrument shas (`check_assertion_floors eaf5bf46…`, `checklist 214ae44d…`, `IND 82ad9700…`), same 5/8 live gate exits, all 10 self-tests rc=0, registry `instrument_total 8` with floors `10/119/59/87/1597/62/86/83`, `derive_floors rc=0`, `replay_frozen rc=0` / `replay_live rc=1` (by-design r26 `source_drift`). Two independent measurements, no disagreement.
- **The carried red (C0/D1):** r37's `c8e233d` turned the checklist gate red and shipped two false green-battery lines (`.ufo/reports/round-37/kotoba.md:32`, `LOG.md:1364`). Fix the SCORECARD:131-133 notation in the publish commit, or record it as carried — either way the r37 record needs correcting. Reproduced independently by B1, B2, S2, R2, I2.
- **Corrections:** the dispatch claim text says "3 catalogue rows"; V3 measures **4** scoped out. r37's recorded live checklist stdout sha `b3275e1c…` is stale vs live `02de0b97…` (I2 F3).
- **Residuals:** blind-tree id-string residual 3 (pin-values 0); the `NonePath` crash; the corpus-baseline DRIFTs (in-flight); the evidence-script runnability gap; the two mis-filed rows + the unadjudicated `init_count_max`.
- **Closed during the round:** the floor-headroom class (86/71 → 86/86, 76/59 → 83/83) — P4 and V1 measured it live; it is superseded at guard `eaf5bf46…`.

## SHONEN

> Source: seat B2's paste-ready block (`.ufo/round-38/drafts/b2/shonen-section.md`), measured at `cb4e0f3`.
> `[PENDING: re-run box counts + floors at the landing commit before pasting into the published report]`.

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) —
  pointers re-measured: `git show HEAD:SKILL.md | awk '/^## /…'` → `15; 9; 9; 8; total: 41` boxes over four
  checklists (`SKILL.md:177/252/298/329`); § Decision tables :151; § Sources :367 = 38 bullets,
  `PASS trigger.citation_resolves: evaluated 38 — 38 repo-rooted citation token(s) resolve`; anti-pattern home
  `corpus/knowledge/fail-closed-and-anti-patterns.md` = 22 pipe rows / 20 data rows (`SKILL.md:349` "Twenty rows").
  Still true; stale-count defect carried (`corpus/README.md:11` "18-row").
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) —
  `python3 verifiers/verify_harness_claims.py` → `28/28 checks pass`, exit 0 (re-run this wave); LOG.md round-5/7/10/11 arcs;
  artifacts present: `corpus/knowledge/harness-verifier-round10.md`, `corpus/knowledge/cold-run-round11.md`.
  The newest non-author cold run remains round 11 — nothing this round restores `[x]`.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) —
  `python3 verifiers/verify_skill_checklist.py` → **exit 1: 9 × PASS, 1 × FAIL** (`governance.citation_resolves evaluated 293`,
  the r37 brace-glob scout lists — the carried red, § C0); `--self-test` → `0 failure(s) over 1584` exit 0;
  `check_assertion_floors.py` → 6 × PASS `floor == observed` (`10/119/59/87/1584/62`) exit 0; 71 fixture dirs.
  Box pointers hold; the live gate carrying them is red at this HEAD — not smoothed.
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) —
  `git log -1 --format="%h %ad %s" --date=short -- PROVINCE.md` → `43e0c02 2026-09-28 seed: kotoba shonen` (unchanged);
  LOG.md:96 and :481 record the round-7 cross-domain audit as routed-not-fixed; this wave wrote only inside the lane repo.

No `[x]` this round: no external verifier is named (PROTOCOL.md:63-68); the fleet `checkShonen` rule refuses `[x]` without a verifier-id token and the file carries none.

Note line: all four boxes were last actually checked by the aggregator lane's round-8 cold run (`corpus/lessons/round-8-aggregator-box3-coldrun.md`); the [x]-readiness pack is scout C2's round-25 dossier (`.ufo/round-25/scouts/C2.md`).
