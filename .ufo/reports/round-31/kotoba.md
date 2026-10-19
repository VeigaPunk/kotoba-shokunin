# kotoba — round 31 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 31, loop 1 (loop-round 11), dispatched and admitted on critic-shaped designs.
Dispatch HEAD: `ec42466`. Work commit: `<pending — recorded at landing>`.
Claims: **B** freshness (extractor-blindness arm) · **G** operability (floors-guard hardening) — `.ufo/round-31/claims.json` (items array 27; prose said 32 — corrected, the count class).
Swarm: 27/27 on `zai-coding-plan/glm-5.3-flash-low` (max-effort pin).
Status: **completed craft round, admitted.**

## Work performed

- **B — B4's omp-scoped blindness arm landed** (C1's REVISE shaped it: the naive kind-keyed arm was rekind-defeatable): 0 extracted + declared loader literals present in the dump -> FAIL "extractor blind" (B4's combined probe: exit 1 naming 33 literals; plain dead-dump r21 semantics preserved; opencode's by-design 0-extraction unaffected — the omp scope is load-bearing). Self-test 82->87 with the `strings-omp-blind.txt` fixture; floors bumped 82->87 in-step (R3/R4's order: G first).
- **G — G2's hardening landed** (G3-approved): 120s subprocess timeout (M5's hang class) + two-way EXPECTED_INSTRUMENTS registry self-check (S6's shrink class); probes on /tmp copies exit 2 naming; live all-PASS byte-invariant.
- **Deliberately not done:** R1's three errata (drafted, verified, filed in LOG — declare-before-work); no push (24 unpushed); SHONEN untouched.

## Landed changes

- `verifiers/verify_surfaces.py` (B4 arm + fixture), `verifiers/check_assertion_floors.py` (G2 hardening + floors bump), SCORECARD rows + move log + planned, LOG § Round 31, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 31) |
|---|---|---|---|
| B | combined strip+rekind probe | exit 0 (0 extracted) | exit 1 "extractor blind: 33 literal(s)" |
| B | self-test / floors | 0/82, floor 82 | 0/87, floor 87 |
| G | hanging-instrument probe | hangs the guard | FAIL named, exit 2 |
| G | registry-shrink probe | exit 0 silent | exit 2 naming |
| gates | eight-gate sweep | — | all exit 0 |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held); all others unchanged. No trade.
Drift handling: C1's B-REVISE and G3's defects recorded; the 27-not-32 count corrected (third recording of the class); R1 errata filed ready-to-land.

## SHONEN

- [~] ×4 — unchanged; R1's SHONEN errata are drafted and filed, not yet landed.
