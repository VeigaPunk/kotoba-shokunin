# kotoba — round 37 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 37, loop A position 1 of the operator's fresh 3-loop regimen (operator goal 2026-10-19, token-plan amendment).
Dispatch HEAD: `041f6ba`. Work commit: `c8e233d` (this report lands in the follow-up publish commit).
Claims: **C1** depth (source-blind re-derivation of the harness claim set) · **C2** operability (floors-guard pair) · **C3** freshness (CommonMark fence-spec) — `.ufo/round-37/claims.json`.
Provider: `alibaba-token-plan/deepseek-v4.1-flash` key 1 (operator amendment 2026-10-19: token plan replaces opencode-go for the swarm waves). **Key-1 monthly quota exhausted mid-wave** (429 on seats V3/B1; resets 11-11 — rotation moves to key 2 next dispatch). Attempts: attempt-1 opencode-go-2 (earlier session, interrupted; fragments `scouts/{M7,X2}.md` at this HEAD used as evidence), attempt-2 opencode-go-1 (operator-interrupted at ~93 min, no output persisted), attempt-3 token-plan-1 (this wave).
Swarm: 22/24 seats (24 declared; V3+B1 lost to the 429 — the count class, recorded).
Status: **REJECTED — C1 fails as declared; C2 and C3 verify and land. Depth unchanged; operability/freshness improved (advisory scores held on a rejected round).**

## Work performed

- **C1 — FAILED AS DECLARED (unanimous across P3/P4/V1/V2/A1/I1/R1).** The source-blind instruments landed as unverified scaffold: `verifiers/verify_harness_independent.py` (24 derived, 4 declared-UNLANDED of 28 named checks; self-test 0/71; mutant-tree probe exit 1 naming the mutant) and `verifiers/compare_harness_independent.py` (self-test 0/59). But the claim's counting commands are red at the settled tree: comparator exit 1 — headline 23/28, strict 17/28 — with 5 open rows: three `omp.catalogue.*` rows the blind extractor cannot land (the catalogue carrier is selected by a rule inside the harness's own scope — a real blindness boundary, not a guess) and two live disagreements, `oc.dup.roots_both_sided` (3 vs 0) and `oc.log.skills_tag_hits` (13 vs 0), both with raw-substrate evidence favoring the harness (V1's independent literal-tag count derives 0; V2's raw log counts corroborate 0 `<skills>` literals and 0 duplicate lines). R1's structural defects stand and are queue material: the N/N headline is copy-satisfiable (its counter-instrument scores 28/28 without opening anything — the 11-row divergence is in fact the strongest evidence the table was not copied), the claim never specified the freeze-before-compare receipt, and the counting command cannot witness agreement. No adjudication doc landed; `corpus/knowledge/harness-independent-round37.md` was not written.
- **C2 — VERIFIED (composite: P5's external anchor + P6's override arm).** New `verifiers/floors-registry.json` + `registry_anchor_drift()` in `verifiers/check_assertion_floors.py` closes the two-table coordinated deletion (red-before reproduced at HEAD bytes by M7, then independently by V4/V5/I1/I2/S2: 5 PASS exit 0 with the row silently gone; red-after: exit 2 `FAIL registry row vanish: pins`) and path/floor/size drift (`path drift` / `path absent` / `floor drift` / `size drift`, every class named, 8 mutant shapes). P6's `override_drift()` closes the `--script` repoint (red-before: foreign repoint and decoy counts exit 0; red-after: exit 2 `override repoint` / `override path missing`). The guard's own self-test lands: 0/41 over F1–F11 with the anchor call shown load-bearing. Floors EXACT 6/6 (`evidence/v5-derive_floors.py`: 10/119/59/87/1584/62).
- **C3 — VERIFIED (P7+P8 pair), one named residual.** `extract_boxes` in `verifiers/verify_skill_checklist.py` is CommonMark-spec: closing fence = same character + length ≥ opener, info string belongs to the opener (backtick-fence info may not contain a backtick), P7's indented-code marker, and an unclosed fence surfaces as a named FAIL through `box_map_complete` (lane policy, spec-cited as policy by S2). The 15-shape `FENCE_SHAPES` battery plus the cmark 0.31.2 oracle give 0 misclassifications (the HEAD instrument misclassified 5/11–11/15 planted shapes); 71 fixture dirs byte-identical; live byte-invariant (stdout sha `b3275e1c…`); self-test 1504→1584 with floors bumped in-step in all four carriers; the routing-16 JSON pin re-pinned `f182cd56→9ea386da` (P8, replay-green measured). **Residual (V6): container-relative fences** — an opener at 4+ columns inside a list item misclassifies (4/36 lines on V6's extended matrix); the reference fix is banked at `evidence/v6-container-relative.patch` (oracle 0/36, self-test pins untouched) for a future round. Latency exposure measured: 0 corpus fences sit at ≥4 columns.
- **Deliberately not done:** C1's closure (r38's top item per R1's amendment); registering the two C1 instruments in `floors-registry.json` before they verify (P1's handoff — else their 71/59-assertion self-tests ride unguarded); the V6 patch landing (named residual, separate claim); the 3-artifact coordinated-edit boundary (declared trust boundary, documented by R2/V5 — not an unclosed class); the divergence merge (operator).

## Landed changes

Commit `c8e233d`: `verifiers/check_assertion_floors.py` (registry anchor + override_drift + self-test), `verifiers/floors-registry.json` (new anchor), `verifiers/verify_skill_checklist.py` (fence-spec + indented-code marker), `verifiers/verify_harness_independent.py` + `verifiers/compare_harness_independent.py` (C1 scaffold, unverified), `verifiers/fixtures/harness-independent/` (4 fixture cases), `corpus/knowledge/sibling-citation-routing-round16.json` (pin re-issue), SCORECARD, LOG § Round 37, `.ufo/round-37/` (claims, 24 scout fragments incl. the two 429 losses, curated `evidence/` + PRUNE.log), this report.

## Before → after measurements

| Claim | Measurement | Before | After (round 37) |
|---|---|---|---|
| C1 | comparator headline | n/a (no instruments) | **exit 1 — 23/28 (strict 17/28), 5 open rows** → FAILS AS DECLARED |
| C1 | instrument self-tests | n/a | IND 0/71, CMP 0/59 (scaffold only) |
| C2 | two-table coordinated deletion | 5 PASS exit 0 (M7/V4/V5/I1/I2/S2 at HEAD bytes) | exit 2 `row vanish: pins` |
| C2 | `--script` repoint | exit 0 (foreign + decoy counts) | exit 2 `override repoint` named |
| C2 | floors guard self-test | none (M7 defect) | 0/41, anchor load-bearing |
| C3 | planted fence shapes vs cmark | 5/11–11/15 misclassified at HEAD | 0 misclassifications (15/15 battery + oracle) |
| C3 | self-test / floors | 1504 | 1584, bumped in-step 4 carriers + routing pin |
| gates | 8-gate battery + replays | green at HEAD | green at `c8e233d`; floors EXACT 6/6 |

Axis verdicts: **operability — improved** (C2 verified); **freshness — improved** (C3 verified); **depth — unchanged** (C1 fails as declared; scaffold + full evidence banked for r38); consistency/coverage/calibration/adjacency — unchanged. No trade; no axis harmed. Advisory scores held on a rejected round (lane idiom: scalar movement waits for admission).
Drift handling: 24-not-26/22 seats (429 losses) recorded; the stale floor list in the dispatch brief (82/51 vs live 87/62) quoted by six seats — recorded, SCORECARD S5 debt remains; the r36-queue "18/35 reports missing SHONEN" claim does not reproduce (B2: 9/17 fleet-path, 0/17 lane-repo); ~79M of working-tree probe copies pruned (PRUNE.log), curated evidence committed.

## SHONEN

- [~] SKILL.md decision tables/error patterns/checklists with cited sources — 41 boxes live (`15/9/9/8`), 38/38 citation tokens resolve; the round's own additions are instruments, not SKILL prose. Pointer: `verify_skill_checklist.py` box_map + B2's live re-run.
- [~] End-to-end domain task executed and logged — the round IS an e2e craft task (three claims, two verified); pointer: this report + `c8e233d`.
- [~] Instructions executable without oral context — gates run cold from the repo (V2/I2 clean-tree replays); pointer: `evidence/v5-derive_floors.py` EXACT 6/6.
- [~] No cross-domain bleed — PROVINCE.md untouched, zero sibling writes (R2 conformance sweep); the divergence merge stays operator-owned.
No `[x]`: no named non-author verifier exists (PROTOCOL: a lane-dispatched subagent is still the lane).
