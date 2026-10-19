# kotoba — round 36 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 36, loop 2 (round-of-loop 2), dispatched and admitted.
Dispatch HEAD: `754197e`. Work commit: `<pending — recorded at landing>`.
Claims: **Z** freshness (the r29 dead-code fix, real) · **P3** freshness (index fence blindness) — `.ufo/round-36/claims.json` (items array 29; prose said 32 — the count class, corrected).
Provider: hyper dry (`remaining_credits: 0`) → `devin/deepseek-v4-1-flash-high` per the goal's stated fallback.
Swarm: 29/29.
Status: **completed craft round, admitted.**

## Work performed

- **Z — landed (Z4's 2-token guard):** the zero/positive intrinsic arms now fire only when no baseline exists; the baseline arm serves those pins. Integrator proofs: a first spot-probe forgot to write the mutated JSON and read green — rerun with the write: **all four mode classes flip** (equal/zero/positive, exit 1 DRIFT-naming each); the swarm's Z5 ran the full 28/28 on the same design; live 28/28 byte-invariant; self-test 10 (floor holds). The round-29 'verified' record is **closed**.
- **P3 — landed on P3b's pair** (P4: primary-only breaks the two witnesses): the coverage census is fence-aware in BOTH corpus instruments; the fenced-row swap flips 0->1; live 53/52/0, 9/9 byte-invariant; self-tests 119/59; floors bumped in-step.
- **Deliberately not done:** Z4's residuals (positive vacuity, bool alias); the glob-only-maps class; the divergence merge (operator).

## Landed changes

- `verifiers/verify_harness_claims.py` (Z), `verifiers/verify_corpus_integrity.py` + `verifiers/verify_corpus_independent.py` (P3b pair), `verifiers/check_assertion_floors.py` (floors 119/59), SCORECARD, LOG § Round 36, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 36) |
|---|---|---|---|
| Z | zero/positive corruption | exit 0 (dead code) | exit 1 DRIFT (4/4 classes; Z5's 28/28) |
| Z | live | 28/28 | 28/28 byte-invariant |
| P3 | fenced-row swap | exit 0 | exit 1, unindexed names it |
| P3 | self-tests / floors | 108/52 | 119/59 (bumped in-step) |
| gates | sweep | — | all green; replay green; fault@/dev/shm green |

Axis verdicts: **freshness — improved** (8.0 held; the falsified class is truly closed); all others unchanged. No trade.
Drift handling: the 29-not-32 count corrected; my own probe bug (unwritten JSON) recorded with the rerun; Z4/P4 named residuals filed; the stale-ref ack recurrence noted (4th time — fresh mirrors used).

## SHONEN

- [~] ×4 — unchanged.
