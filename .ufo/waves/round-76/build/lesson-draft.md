<!-- Round-76 lesson — BUILD DRAFT (seat B17LessonScribe). Landing target `corpus/lessons/round-76.md`.
     The integrator drops this comment and replaces `<freeze>` / `<tip>` with the committed revisions.
     No claim data is written here: every number below was printed from committed or fetched bytes named
     beside it. Dispositions in § Routed defects name the artifact and the counter conjunct that reads it;
     the landed state at the time this draft was written is recorded in `.ufo/waves/round-76/w1/B17LessonScribe.md`. -->

---
author: kotoba L1 (hyaku run 10, round 76, attempt 1)
date: 2026-10-27
round: 76
lane: kotoba
---

# Round 76 lessons — kotoba

Claims (frozen in `plans/round-76.md` at `abd8e5cfd45ea3863b344ac58a187b0c5de620d0`; counters
`verifiers/check_desc_craft.py` — `description craft backed K of 6` — and `verifiers/check_r75_routed_repairs.py`
— `r75 routed repairs closed 4 of 4` — frozen at `<freeze>` before data; two pre-data corrections in
`plans/round-76-addendum-1.md` at `7eed80e9`): **C1 depth** — the description-writing half of S213 admitted at
guide-advice level, acted on in `SKILL.md` § Body craft, and audited on kotoba's own `description`; **C2
consistency** (calibration sub-axis) — the r75-closure routed defects R1–R4 closed with committed corrections
and receipts. Base battery, wave shape and scores: `plans/round-76.md` § Base battery, `LOG.md` § Round 76,
`SCORECARD.md` round-76 annotation (one v2 wave, 64 seats; attack share and role set per
`plans/round-76-addendum-1.md` § Wave role correction, recounted in M76-6 below).

## Gate

**Source re-opened this round (existing row, not a new row).** S213 —
`https://agentskills.io/skill-creation/optimizing-descriptions.md` — row written 2026-10-25, reused in
round 75 for its eval protocol, re-opened 2026-10-27 for its description-writing half. Snapshot:
`.ufo/waves/round-76/snapshots/optimizing-descriptions.md`, 13,403 bytes, 196 lines, sha256
`7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, HTTP 200 at
`snapshots/fetch-record.json` (`fetched_at` 2026-10-27T16:57:56Z); the same digest is in
`snapshots/MANIFEST.sha256`. Freshness: byte-identical to the round-70 snapshot and the round-74 staged
snapshot (`cmp` exit 0, `w1/A24ScoutFresh.md`) and to an independent stdlib re-fetch (`urllib` vs `curl`,
3 of 3 agree, `w1/B26FetchRecheck.md`, receipt `receipts/fetch-recheck.txt`).

**Located quote** (≤25 words, verbatim from those bytes, after the page's first heading at line 5):
"`A few sentences to a short paragraph is usually right`" — 10 words, § Writing effective descriptions
(heading line 21), line 28 of the snapshot; it occurs in neither `evaluating-skills.md` nor
`best-practices.md`, so it is page-unique rather than site chrome (`build/quotes-s213.md`, quote #9).
The entry `corpus/knowledge/description-craft-round76.md` carries five such located quotes in its opening
rule table — five rule rows derived from the four principles at `:25`–`:28` (pushiness split into breadth
and unnamed-domain contexts) — and its worked-example reading at `:184`–`:188`; the self-audit under
§ This lane's own `description`, measured records `description`
render 1022 characters (clip newline kept; 1021 stripped) and first sentence 151 characters, receipt
`receipts/description-audit-4de12b61f75c73e3675ef0e422cc2be0f7da8960.txt`, and § What this entry does not
claim (Q62) bounds the rest. The snapshot digest has the four pinned homes the addendum names (§ Correction):
`snapshots/MANIFEST.sha256`, `snapshots/fetch-record.json`, the digest table inside
`verifiers/check_desc_craft.py`, and this Gate.

**Admit.** The page's description-writing rules — imperative phrasing, user intent over mechanics,
deliberate breadth including contexts the user never names, and length under the specification's 1024
character ceiling — are admitted at the level round 74 used for the same guide set (`S223`–`S225`,
`corpus/knowledge/spec-skill-creation-craft-round74.md`): guide advice from the format's own maintainers,
documentary evidence, no agent client run. They are acted on in `SKILL.md` § Body craft (one rule row
citing the entry and S213, three quote fragments verbatim in the snapshot) and turned on the lane's own
`description`: imperative phrasing **not met**, user intent **partial**, pushiness **met**, unnamed-domain
contexts **partial**, short **not met** (1022 characters, 7 sentences), hard limit **met with 2 characters of
headroom**, so the next edit to that field must trim before it extends.

**Reject (held).** Any claim that this page's trigger-rate protocol is evidence that kotoba's description
triggers reliably. The page's 20-query × 3-run loop, its 0.5 threshold and its train/validation split are
instructions to run, not a run; no held-out query experiment exists in this lane. The round-75 Gate hold
therefore stands, and the entry carries it as § Limits.

**Reject (refused).** The staged package entry `spec-description-trigger-discipline.md` (package
`/home/vgpnk/Projects/shokuknow/merge/kotoba/`, staged row `S231`) as a citable artifact. It rests on this
same page and carries the package's 2026-10-23 opening; fleet `CORPUS.md` rule 1 requires the source to be
opened in the round that writes the row. The page was opened directly this round with its own snapshot and
two independent fetches, so the entry is written from this round's bytes and nothing is adopted from the
package.

**Reversed this round.** The round-75 Gate reject candidate — "any claim that the 1021-character description
size … remains current; current frontmatter is materially shorter" — is false: the folded render is 1022
characters clip-preserving (1021 stripped) over block lines 4–18, identical at `65a5c7a`, `ac9f295`,
`b7f13f4b` and `4de12b61` (`w1/B21RevMethod.md` §2–§4). The convention is frozen in
`plans/round-76-addendum-1.md` § Render-length convention (`7eed80e9`): clip 1022 / stripped 1021, both
printed beside every receipt that carries the number. Corrected under R1; the superseded text is named
there, not rewritten.

**`considerthese/2026-10-26.md` proposal 3 is mined as C1.** Its text: "The description is still 1,021 of
1,024 chars, and its first sentence is still about 150 chars against the skill's own 99-char omp render
cliff. … A round that admits that page and then audits kotoba's own frontmatter against it would close
both." Measured: 1022 clip / 1021 stripped, first sentence 151 — the proposal's numbers are current inside
the 1021/1022 convention. Admission (done above) and the self-audit (done above) are the two halves it
asks for; the "omp 99-char render cliff" is **not** on this page and is not claimed from it.

**Proposals 1, 2, 4, 5 declined.**

- **1 (byte ceiling + 200-char line check).** The 600-line box is a checklist-executed budget whose box
  text is sha256-pinned per box in `verifiers/checklist-baseline.json` (schema `kotoba-checklist-v1`,
  `text_sha256`) and executed by `verify_skill_checklist.py`; replacing the box with a byte/line rule is a
  baseline-map change and needs its own claim, and it is not in this round's touch list. Declined for this
  round, not judged wrong.
- **2 (move `## Gate registry` to `verifiers/REGISTRY.md`).** Q67: "a move that takes a protocol-named home
  (the gate registry in `SKILL.md`) elsewhere is an L0 question, not a claim" (`plans/round-76.md` § Trigger
  records the same); such a move also re-points `check_gate_registry.py`'s target.
- **4 (close a round "provisional" until its falsify wave runs).** Closure procedure, owned by the
  protocol/scorecard closure, not a corpus or craft datum; and this round's v2 band puts 22 of 64 seats on
  attack (34.4%, the validated mix — M76-6) inside the one wave, so a "wave 2 pending" state does not arise.
- **5 (per-round evidence cap / `.ufo` compression).** Operator-level fleet policy over the working tree;
  a lane cannot cap fleet evidence from inside a round's claim surface.

**Assimilation: none.** Recorded above: the only staged artifact on this theme is refused as a staged
artifact and re-grounded in-round, so no `SOURCES.append.md` row, no entry and no renumber map is imported
this round.

**Non-author admit/reject spot-check: pending.** Dispatched wave seats are lane seats and do not qualify;
the closure owns the sampled re-open.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| M76-1 · `layout-window-counted-as-value` | `corpus/lessons/round-75.md:11` measured the description with `awk 'NR>=3&&NR<=8'` — 6 of the block's 16 source lines (3–18), whose raw `length($0)` values 14, 76, 78, 73, 79, 72 sum to 392 of 1022 rendered characters — and `:5` rejected the imported 1,021 on that basis. Committed bytes render 1022 (clip) / 1021 (stripped) at `65a5c7a`, `ac9f295`, `b7f13f4b` and `4de12b61`, content block lines 4–18; a reflow moves the raw line sum with an identical rendered value (`w1/B21RevMethod.md` §2–§4, whose "372" mis-sums its own five printed lengths). | none at the time — Q67/Q54/Q60 pin a reproducible count at a revision but not the measurement unit against the artefact's parse unit; Q74 (added this round in `corpus/QUALITY.md`) is that criterion: a block scalar is measured on the whole rendered value at a named revision, naming the parser (`yaml.safe_load`), the slice (the frontmatter keeping the block's trailing newline) and whether the clip newline is counted (clip 1,022 / stripped 1,021, the convention named beside the number), because `length($0)` counts the indent and the `description: >` marker line as content. | R1: appended correction in `corpus/lessons/round-75.md` plus `receipts/r1-folded-render.txt`, which recomputes 1022 from the measured revision's `SKILL.md`; the entry states the same convention once (§ measure). |
| `number-drift` (slice off-by-one) | Measured by this seat at `b7f13f4`: `fm = "\n".join(git show b7f13f4:SKILL.md .split("\n")[:18]) + "\n"; len(yaml.safe_load(fm)["description"])` → **1022**; `s[:s.index("\n---",4)]` → **1021**. The frozen R1 label is 1022, so a counter or receipt that slices at the fence prints one below the label and fails for a formatting reason, not a content reason. | none at base — Q74 names the convention but no gate enforced the slice, and the existing `check_skill_evals_v2.py` G4 arm measures sibling descriptions, not kotoba's own | `plans/round-76-addendum-1.md` § Render-length convention (`7eed80e9`) fixes clip-preserving 1022 as the target and requires every receipt to print both variants; the R1 receipt carries the slice and the method, and the counter's must-fail arm reads 1021. |
| `vacuous` | `w1/A11MutRedBefore.md`: the red-before probe ran the two frozen counters from a base checkout and got `can't open file .../check_desc_craft.py`, exit 2, four times, verdict INCONCLUSIVE. It tested for the counter's presence at base instead of running the frozen counter from its freeze commit against `--rev <base>` data — the invocation every script counter since r69 uses (r74's `check_spec_craft.py` `0 of 3` at base `1e03d19` is the precedent). | none — the plan's "counters freeze before data" fixes *when* the counter bytes exist, not how the red-before invocation is formed | State the invocation in the same sentence as the frozen predicate ("run the counter from its freeze commit, pass `--rev <base>`"), and have the red-before receipt print both revisions' lines. Re-run belongs to the mutation seats. |
| `reference-drift` | `verifiers/check_skill_evals_v2.py` F7 requires S213's `used-by` to equal `corpus/knowledge/skill-eval-artefacts-round70.md` **exactly** (`row[10].strip() != ENTRY`, line 288); C1 (e) appends a second entry to that cell. Measured by this seat in a scratch clone of the base with the append applied (`w1/B17LessonScribe.md` § 3): `python3 -B verifiers/check_skill_evals_v2.py --repo <fixture> --rev <fixture tip>` → `skill eval artefacts verified 1 of 10`, exit 1, with `F7: S213 used-by != corpus/knowledge/skill-eval-artefacts-round70.md (exact match required)`; at base the same counter reads `2 of 10`, exit 1. A further step down from a red counter, not a green→red regression. | none — the registry's append-only `used-by` duty and that counter's exact pin contradict, and no gate compares two counters' demands on one cell | Route to round 77: relax F7 to membership (`ENTRY in [p.strip() for p in row[10].split(",")]`) with its `--self-test` arm re-pinned, or ledger the cell inside F7; until then the no-harm line names the 2 of 10 → 1 of 10 move. |
| M76-5 · `scope` | `plans/round-76.md` § Wave shape budgets `labrat` 4 and `sonic` 1 as top-level seats; the dispatch validator refuses both (`unknown_role`) and the committed `w1-spec.json` holds 64 seats with 0 labrat and 0 sonic — their probe/read tasks were re-roled to scout, scribe and simplifier. | none in `QUALITY.md`; the pre-dispatch role validator caught it (`unknown_role`), which is the guard working, and the plan's role list was not drawn from that table | `plans/round-76-addendum-1.md` § Wave role correction records the validated topology; the lesson's claim line states the dispatched mix, not the plan's estimate. |
| M76-6 · `number-drift` | The same plan sentence reads "30 build + 34 attack (attack share 53%)". The validated dispatch has attack roles defined as reviewer + critic + mutation-tester + sentinel (10 + 6 + 4 + 2) = **22 of 64 = 34.4%** (`plans/round-76-addendum-1.md` § Wave role correction prints the same 22/64). No taxonomy yields the plan's 34: its own attack list adds the `attack-simplifier` seats and omits revengers (22 + 3 = 25/64 = 39.1%), and the dispatch's A/B seat-name prefixes split 36/28. The plan's §3 floor list also sums to 56, not 64. | none — no gate recounts a plan's seat arithmetic against the dispatch it produces, and the taxonomy was undefined | The addendum's taxonomy is the one this round's claim uses and the lesson names it in the same sentence as the number; future wave-shape sentences take their counts from the dispatch file and name the role set. |

## Routed defects

R1–R4 are the round-75 non-author closure's items (`corpus/lessons/round-75-verifier-spotcheck.md` § 6).
D1–D5 are the round-74 closure's items carried two rounds; their state is recorded here rather than
re-routed.

**R1 (quality/calibration) — closed.** `corpus/lessons/round-75.md` carries an appended correction naming
the superseded M75-1 row text ("stale-premise … `awk 'NR>=3&&NR<=8'` … 14,76,78,73,79,72") and the `## Gate`
reject candidate, asserting the folded-render measurement (1022 characters, clip newline kept; 1021
stripped; block lines 4–18) and citing this spot-check's § 6 R1. Receipt
`.ufo/waves/round-76/receipts/r1-folded-render.txt` recomputes 1022 from the measured revision's `SKILL.md`.
Counter arm: `check_r75_routed_repairs.py` R1; the counter recomputes the number from bytes, so a reflowed
`SKILL.md` cannot be passed by reformatting a receipt.

**R2 (evidence standard) — closed.** `receipts/noharm-at-tip.txt` names the r75 tip
`b7f13f4b39cbd43076a85568adca763a6f674e7a` on its first line and carries stdout plus exit codes of
`python3 -B verifiers/verify_corpus_integrity.py --json` and `.../verify_corpus_independent.py --json`; the
`LOG.md` § Round 75 append cites the receipt path. The revision is the r75 tip, not the r76 judged tip: the
defect was a missing post-landing receipt for round 75, and the render the spot-check disputed is identical
at both (`w1/B21RevMethod.md` §2).

**R3 (wave hygiene) — closed.** `.ufo/waves/round-76/w2-registry-note.md` (draft
`build/w2-registry-note.md`) reconciles `R75Attack28`: the results entry carries no top-level `report`
field, the report path appears only inside the verdict prose, the path never entered any commit
(`git log --all --diff-filter=A` empty), the wave dir holds 63 `.md` files plus `swarm-registry.json`, and
the results file holds 64 entries with 0 empty outputs. Machine-checkable `jq` excerpts and both `test -e`
forms are in the note. `LOG.md` § Round 75 cites the note.

**R4 (lesson completeness) — closed.** `LOG.md` § Round 75 carries an appended closing line **after** the
filed "w2 falsify results pending" text (that text is not rewritten): wave `kotoba-r75-w2` settled 64 of 64
results with 0 dead seats and 63 of 64 report files, the one absent report being `R75Attack28`, recorded as a
phantom per R3.

**D1 (dispatch the falsify wave) — landed in round 75** (w2 exists, 64 seats, 64 settled entries).

**D2 (unlisted orchestrator snapshot) — landed.** `LOG.md` § Round 74 carries an appended line naming
`d5aebcf` as the orchestrator's in-flight snapshot committed during the run-7 interruption, not a lane
landing (commit message bytes verified before writing).

**D3 (missing forward pointer) — landed.** `corpus/knowledge/sibling-overlap-census-round49.md` carries an
appended forward pointer to `corpus/knowledge/sibling-overlap-census-round74.md` and to the one class that
changed (tsukuroi `none` → `adjacent`), so a reader of the old entry meets the re-pin.

**D4 (unfloored self-tests) — landed.** `check_spec_craft.py --self-test` (250) and
`check_sibling_reread.py --self-test` (47) are floored in `verifiers/floors-registry.json` and in the in-file
tables of `verifiers/check_assertion_floors.py`, bumped in step; receipt `receipts/d4-selftests.txt` names
tip `4de12b61f75c73e3675ef0e422cc2be0f7da8960`.

**D5 (falsify arm for carried cells) — conditional, not landed.** The condition is "if a later freshness
claim depends on the judged cells"; no later claim does — round 76's C1 is depth over the `description`
field and C2 is r75 repairs, neither reads the carry-forward cells. Recorded, not built.

**Routed forward to round 77 (new).** F1: F7's exact-match `used-by` pin against the append-only registry
(M76-4). F2 is closed this round by `plans/round-76-addendum-1.md` (§ Correction, `7eed80e9`): C1 (a)'s
anchor-digest clause is withdrawn and the digest is pinned in four places instead, so no in-place rule-2
breach is needed and none was made.

## Round honesty

- **C1 (a) was unsatisfiable as filed and is withdrawn before data.** S213's anchor cell carries no sha256
  (it names the upstream commit `69ef37e` and the "Running multiple times" quote), so "the
  optimizing-descriptions digest equals the digest recorded in the S213 row's anchor update" needed a third
  in-place cell change, which fleet `CORPUS.md` rule 2 does not permit. `plans/round-76-addendum-1.md`
  (`7eed80e9`) withdraws the clause and pins the digest in four places instead: `snapshots/MANIFEST.sha256`,
  `snapshots/fetch-record.json`, the digest table inside `verifiers/check_desc_craft.py`, and this `## Gate`
  access record. No rule-2 breach was made; the registry change this round is the S213 `used-by` append only.
- **C2's headline is "four repair artifacts present and content-checked at the named revision", not an
  independent adjudication.** The counter reads committed content (receipts, note, LOG lines, correction) and
  recomputes R1's 1022; it does not re-run the two corpus gates for R2, and R1's "re-derive any downstream
  claim" clause is satisfied by the state of the tree (no live claim consumes the "materially shorter"
  assertion), not by a counter arm. The critique that would have made this a headline defect is
  `w1/A16CritHeadlineC2.md`; its demands are answered above where they are checkable and named here where
  they are not.
- **Several attack seats inspected a build that did not exist yet.** `A01RevQuoteLocate`, `A02RevHashChain`,
  `A17CritAudit` and `A34ScoutReceipts` returned blocked/incomplete verdicts at a clock before the drafts
  and receipts landed, and `A11MutRedBefore` returned exit 2 (M76-3). Their tests are presence checks at
  one moment, not falsifications; the re-runs and the closure's spot-check carry the verdicts.
- **The 1022/1021 pair is one convention, named once** (entry § measure, Q74, the R1 receipt). No sentence in
  this round compares one form against the other; the entry prints 1022 and names 1021 as the stripped form.
- **Wave timing:** the base battery (`base-battery/base-battery.txt`) is green at `b7f13f4` and the census
  reads 151 rows with 20 W04 duplicate-URL warnings, the same set as round 75; `SKILL.md` is 590 lines at
  base against the 600-line box, and the round's patch (`build/skill-patch.md`, after the simplifier's cut)
  lands at **593** — 7 lines of margin, with the budget box's text unchanged.

## Status changes

**S213 `used-by`** — old: `corpus/knowledge/skill-eval-artefacts-round70.md`; new:
`corpus/knowledge/skill-eval-artefacts-round70.md, corpus/knowledge/description-craft-round76.md`
(comma+space, the separator the census parser splits on). `status` stays `mined`, `opened` stays
2026-10-25, `recheck` stays `90d`; the row keeps 11 cells (13 fields with the table's own pipes).

**Landing constraint** measured this round: the `used-by` append and the entry file land in the **same**
commit. With the append in the registry and the entry absent, `scripts/sources-census.sh validate --file
corpus/SOURCES.md` exits 1 with `E11 S213 missing used-by corpus/knowledge/description-craft-round76.md`
(reproduced in a scratch clone this wave, `w1/B17LessonScribe.md` § 1.4), and `check_skill_evals_v2.py`'s A10
arm reports the same.

**No other cell changes.** No row is added (S213 is re-used, not re-opened as a new id); no other `status`,
`recheck` or `used-by` cell moves; `corpus/knowledge/description-craft-round76.md` is a new entry, not a row.
