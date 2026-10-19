# kotoba — round 44 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 44, loop A position 8 of the operator's 3-loop regimen.
Dispatch HEAD: `6881ce3` (r43's publish commit). Work commit: this commit's parent (the report lands in the follow-up publish commit).
Claims: **C1** depth (close the record+map composition door) · **C2** operability (R2's three residuals) · **C3** calibration (reconcile the substrate red) — `.ufo/round-44/claims.json`.
Provider: `openai-codex/gpt-6-luna-max` (pos-8 plan was `zai-coding-plan/glm-5.3-flash` — zai quota-exhausted; operator directive: all zai positions run on codex luna-max for the rest of the session).
Swarm: 24/24 seats.
Status: **ADMITTED — all three claims verified and landed.** The record+map composition door — the last named channel in the r37-r44 laundering class — is closed. Depth 9 held (the 9.5 shape now needs the held-out hunt to find no unlisted door); operability 8.5 held; calibration 8.5 held.

## Work performed

- **C1 depth — the record+map composition door is CLOSED; the laundering class's last named channel.** `check_independent_scope_maps` (`verifiers/compare_harness_independent.py:684`) now cross-checks the **RECORD** channel against the committed scope file + the derived set, the same way the r43 key-set check constrains the MAP channel: a record supplying a non-null value for a committed scope-out row → `scope-out value laundering` exit 2; a record-list+map whose combined id-set exceeds the honest derived set → `derived-set overflow` exit 2. The real 24-row V10 fixture (`record-map-24-composition` — F1 rebuilt it to reproduce the *real* case, not the earlier 28-value stand-in) now fails closed naming `oc.dup.onesided_roots`. F1/I1/B2 verified the closure on the settled comparator sha `13b6d791`; R1/X1's "still open" readings were measured on earlier shas (`d8b8c7f`/`a2bf6a2a`/`354e1b3`) — temporal, not substantive; on the landed bytes the arm fails closed. **This closes the r37-r44 laundering arc** (R1-D1 scope-out → F-2 value channel → F-3 channel reconciliation → map forms → record+map composition). The residual question for depth's 9.5 shape: does a fresh held-out hunt still find an unlisted door?
- **C2 operability — VERIFIED (P2; V2 + R2 verify).** Three residuals closed class-named: a dotted-id top-level map shadow beside the row channels → exit 2; a record whose `check`/`id` fields disagree → exit 2; a record with conflicting `re_derived`/`observed` → exit 2. V2's matrix confirms each frozen-vs-landed; comparator self-test **213→245** with floors in-step. X2's 4th-shape hunt named new residuals for the queue: `expected`/`expected_value` conflict and a lone non-string `status` silently discarded (both still exit 0).
- **C3 calibration — VERIFIED (P3; V3 + H1 + G1 + R2 verify).** The carried substrate red is reconciled: the live OMP is a real version change **18.11.1 → 18.12.2** (sha `bf1e86a9` → `9513ef9f`, mtime 2026-10-19 — a legitimate rebuild, not instrument-stale). The 0/8 loader-class extraction was stale because the new bundle uses `I5`/`Gl`/`Mo` callees; P3 extended the OMP-only extractor, added the call shapes to the fixture, and re-pinned the binary. The live census resolves **11 call sites to the exact 8 declared loader classes**. Surfaces gate back to **7/7**, pins back to **3/3** (was 5/7 + 1/3). Named bound: no upstream OMP source/build commit provenance could be established (the installed binary doesn't expose it) — recorded, not smoothed.
- **Wave conformance.** 24/24 seats, no commits; writes inside `.ufo/round-44/` + `verifiers/` + fixtures + `corpus/` + LOG/SCORECARD + `baseline.json`; no `.git` symlinks (Z1); floors-registry churn settled in-step; drafts pruned to evidence (the 47MB OMP strings dump + cited probe results preserved).
- **Deliberately not done:** the held-out hunt on the settled closure (r45's depth target); X2's residuals; OMP provenance (no upstream commit); digest-append; IND hang; resolver-vs-brace; SHONEN form; the divergence merge (operator).

## Landed changes

Lane-identity work commit: `verifiers/compare_harness_independent.py` (record+map scope cross-check + R2's three residual fixes + F1's fixture wiring; self-test 245), `verifiers/fixtures/compare-harness-independent/` (record-map-24-composition/control real-case fixtures + the R2 residual fixtures), `verifiers/verify_surfaces.py` + `verifiers/fixtures/surfaces/strings-omp-newcallees.txt` (the extended callee allowlist I5/Gl/Mo), `verifiers/baseline.json` (OMP 18.12.2 re-pin), `verifiers/floors-registry.json` + `verifiers/check_assertion_floors.py` (floors `10/150/91/87/1597/62/104/245/150`), SCORECARD, LOG § Round 44, `.ufo/round-44/` (claims, 24 scouts, curated evidence), this report.

## Before → after measurements

| Claim | Measurement | Before | After (round 44) |
|---|---|---|---|
| C1 | record+map composition | exit 0 — 24/24 (adjudications 4→0) or 28/28 laundering | **exit 2 `derived-set overflow`** — record channel cross-checked for scoped-out values + combined id-set; real 24-row fixture fails closed |
| C2 | R2's three residuals | all exit 0 | **all exit 2 class-named**; self-test 213→245 |
| C3 | substrate red | surfaces 5/7 (0/8 loader-class), pins 1/3 | **surfaces 7/7, pins 3/3** — real OMP 18.11.1→18.12.2 rebuild, extractor + re-pin |
| gates | battery | green at `6881ce3` | **green at landing** — floors 9/9 EXACT `10/150/91/87/1597/62/104/245/150`; comparator 0/245; join 24/24; corpus 9/9 + exit 0; surfaces 7/7; pins 3/3; checklist 10×PASS |

Axis verdicts: **depth — improved** (the record+map composition door closed; the r37-r44 laundering arc is closed — the residual question for 9.5 is the held-out hunt, not a named door); **operability — improved** (C2 verified; score held); **calibration — improved** (C3 verified; score held); consistency/coverage/freshness/adjacency — unchanged.
Drift handling: floors moved in-step (comparator 213→245, EXACT 9/9 at close); the comparator self-test ran red mid-round while the R2 fixtures landed before the floor bump (the r37 anchor catching a half-state) — settled green; the substrate pins drifted legitimately (real rebuild) and were re-pinned with evidence, not smoothed.

## SHONEN

- [~] box 1 (decision tables / error patterns / checklists / cited sources, `SHONEN.md:5`) — four checklists `15/9/9/8` = 41 boxes; § Sources 38 bullets resolve; anti-pattern home 20 data rows. Pointer: B2's re-run (`.ufo/round-44/scouts/B2.md`). Stale-count defect carried (`corpus/README.md:11` "18-row").
- [~] box 2 (end-to-end task executed and logged, `SHONEN.md:16`) — `verify_harness_claims.py` → `28/28 checks pass` exit 0; LOG round-arcs; artifacts `corpus/knowledge/harness-verifier-round10.md`, `cold-run-round11.md`. Pointer: this report + the work commit.
- [~] box 3 (instructions executable without oral context, `SHONEN.md:22`) — all gates run cold; the comparator + scope-file + reconciler + fixtures committed and re-runnable; `verify_skill_checklist.py` exit 0 10×PASS, `--self-test` 0/1597; floors 9/9 EXACT. Pointer: `verifiers/fixtures/compare-harness-independent/record-map-24-*`.
- [~] box 4 (no cross-domain bleed; `PROVINCE.md` accurate, `SHONEN.md:41`) — PROVINCE.md unchanged since seed (`43e0c02`); writes confined to the lane repo (Z1 conformance); the divergence merge stays operator-owned.
No `[x]`: no named non-author verifier exists (PROTOCOL: a lane-dispatched subagent is still the lane).
