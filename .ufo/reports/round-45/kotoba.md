# kotoba — round 45 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 45, loop A position 9 of the operator's 3-loop regimen — **the held-out hunt on the settled closure**.
Dispatch HEAD: `032f47b` (r44's publish commit). Work commit: this commit's parent (the report lands in the follow-up publish commit).
Claims: **C1** depth (held-out hunt — is the laundering class closed?) · **C2** operability (X2's two residuals) · **C3** calibration (reconcile records to post-r44 tree) — `.ufo/round-45/claims.json`.
Provider: `openai-codex/gpt-6-luna-max`.
Swarm: 42 seats reported (~42 min).
Status: **C1 improved-bounded — depth holds 9, 9.5 not supported; C2 and C3 verified and land.** Depth 9 held; operability 8.5 held; calibration 8.5 held.

## Work performed

- **C1 depth — improved, bounded; 9.5 NOT supported.** The full r41 census replay (46/46 subprocess arms, input hashes unchanged) on the landed `13b6d791` comparator: **14 of the 25 r41-open doors now reject exit 2, 11 still exit 0** (H01/H02/C1/C2/S1/Y1/R2 independently reproduce the same replay — `11 open, 29 closed, 4 controls, 1 diagnostic, 1 caller-trust`). The record+map composition is confirmed closed on the requested before/after bytes: frozen `d8b8c7f` exit 0 → landed `13b6d791` exit 2 `derived-set overflow`; the real 24-row `record-map-24-composition` fixture fails closed, and the `record-map-24-control` stays green on both — a true discriminator, not a false-green. **But the surviving doors are not demonstrably bounded** — the held-out hunts (C1/C2/S1) found doors OUTSIDE the 46-arm census: raw duplicate-JSON-members (decoder last-wins), the scope-file cwd door with a *stronger null-value bypass*, live-JSON mode/verdict/summary shadow channels. C1's "exhaustive residual list" branch is therefore not verified — **depth holds 9**, and the landed comparator must not be described as closing all doors.
  - **The 11 still-open doors (the durable residual):** 4 caller-supplied live-JSON arms — `live-mode-positive-masks-independent-drift` (the strongest false-green: live 7 vs ind 999 still exit 0 because the supplied live mode makes the row green), `live-mode-split-across-row-channels`, `live-verdict-shadow-in-row-channel`, `live-top-level-observed-summary-divergence` — all conditional on a caller tampering with the live JSON, not the ordinary producer path; the **scope-file cwd door** (the F3 seam, still open — a relative `--scope-file` from a planted cwd reads exit 0 23/23 while the receipt attests the honest file, now with a stronger null-value bypass); `unmatched-extra-scoped-out-probe` + scoped-out reason/evidence drift (accepted metadata/probe irregularities); and the raw duplicate-JSON-member doors.
- **C2 operability — VERIFIED on the newer `1101213a` comparator.** X2's two residuals closed on the landed bytes: a conflicting `expected`/`expected_value` pair → exit 2 `record value alias conflict` (the within-record cross-check now reconciles foreign-key disagreement); a lone non-string `status` → exit 2 `non-string status` (was silently discarded). S1's "still open" readings were on `13b6d791` (the r44 landing) — temporal; on `1101213a` they fail closed. Comparator self-test **245→255**, floors in-step. Score held: advisory.
- **C3 calibration — VERIFIED.** `corpus/knowledge/harness-independent-round41-census.md` updated to the post-r44 state (append-only annotation — the r41 measurement preserved verbatim, each r43/r44-closed door marked closed-at-sha); the doc's `recheck` line still runs; records reconciled to the settled tree (N3 errata).
- **Wave conformance.** 42 seats, no commits; writes inside `.ufo/round-45/` + `verifiers/` + fixtures + corpus doc + LOG/SCORECARD; no `.git` symlinks; floors churn settled in-step; drafts pruned to evidence.
- **Deliberately not done:** the surviving doors in reachability order — the scope-file cwd seam (resolve `--scope-file` once vs `--cwd`, record the resolved path+digest in the receipt); the live-JSON shadow channels (the producer-vs-payload trust question); raw duplicate-JSON-member handling; scoped-out probe/reason/evidence drift; the exhaustive-census problem (a provably-complete open-door list). Standing debt: digest-append; IND hang; resolver-vs-brace; SHONEN form; OMP provenance; the divergence merge (operator).

## Landed changes

Lane-identity work commit: `verifiers/compare_harness_independent.py` (X2's two residual fixes — record value alias conflict + non-string status; self-test 255), `verifiers/fixtures/compare-harness-independent/` (expected-alias-conflict + status-lone-nonstring + shared live.json), `verifiers/floors-registry.json` + `verifiers/check_assertion_floors.py` (floors `…/255/150`), `corpus/knowledge/harness-independent-round41-census.md` (post-r44 append-only annotation), SCORECARD, LOG § Round 45, `.ufo/round-45/` (claims, 42 scouts, curated evidence), this report.

## Before → after measurements

| Claim | Measurement | Before | After (round 45) |
|---|---|---|---|
| C1 | r41 census replay on `13b6d791` | 25 open (r41 baseline) | **14 closed / 11 open** — record+map verified closed (frozen `d8b8c7f` exit 0 → landed exit 2 `derived-set overflow`); the residual list is durable but not bounded |
| C2 | X2's residuals | expected/expected_value + lone non-string status exit 0 | **both exit 2 class-named** (`record value alias conflict`, `non-string status`) on `1101213a`; self-test 255 |
| C3 | census doc currency | r41-state (25 open, stale) | **reconciled to post-r44** (append-only closed-at-sha marks; recheck runs) |
| gates | battery | green at `032f47b` | **green at landing** — floors 9/9 EXACT `10/150/91/87/1597/62/104/255/150`; comparator 0/255; join 24/24; corpus 9/9 + exit 0; surfaces 7/7; pins 3/3; checklist 10×PASS |

Axis verdicts: **depth — improved, bounded** (14/25 doors closed + record+map verified; the surviving doors are not bounded — 9.5 not supported; 9 held); **operability — improved** (C2 verified; score held); **calibration — improved** (C3 verified; score held); consistency/coverage/freshness/adjacency — unchanged.
Drift handling: floors moved in-step (comparator 245→255, EXACT 9/9 at close); the comparator self-test ran red mid-round while X2 fixtures landed before the floor bump — settled green; the "still open" vs "closed" readings across seats were temporal (different comparator shas `13b6d791` vs `1101213a`) — recorded against the landed sha.

## SHONEN

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) — four checklists `15/9/9/8` = 41 boxes; § Sources 38 bullets resolve; anti-pattern home 20 data rows. Pointer: B2's re-run (`.ufo/round-45/scouts/B2.md`). Stale-count defect carried (`corpus/README.md:11` "18-row").
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) — `verify_harness_claims.py` → `28/28 checks pass` exit 0; LOG round-arcs; artifacts `corpus/knowledge/harness-verifier-round10.md`, `cold-run-round11.md`. Pointer: this report + the work commit.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) — all gates run cold; the comparator + scope-file + reconciler + fixtures + census replay committed and re-runnable; `verify_skill_checklist.py` exit 0 10×PASS, `--self-test` 0/1597; floors 9/9 EXACT. Pointer: `.ufo/round-45/evidence/` (the census replay + hunts).
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) — PROVINCE.md unchanged since seed (`43e0c02`); writes confined to the lane repo (Z1 conformance); the divergence merge stays operator-owned.
No `[x]`: no named non-author verifier exists (PROTOCOL: a lane-dispatched subagent is still the lane).
