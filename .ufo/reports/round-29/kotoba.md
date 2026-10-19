# kotoba — round 29 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 29, loop 1 (loop-round 9), dispatched and admitted on scout C1's resolutions.
Dispatch HEAD: `daf701d`. Work commit: `<pending — recorded at landing>`.
Claims: **H** freshness (harness zero/positive pins) · **T** capability acquisition (assertion-floor guard) — `.ufo/round-29/claims.json` (the items array carried 27 lanes; prose said 32 — corrected, the r23/r24 count class).
Swarm: 27/27 on `openai-codex/gpt-6-luna-max`.
Status: **completed craft round, admitted.**

## Work performed

- **H — H2's four-line mode fix landed** (C1's semantics: zero==expect exact, positive>=expect): `omp.db.rows` / `oc.log.skills_rescan_max` corruption probes -> DRIFT exit 1; the swarm's all-28 matrix flipped every pin; live byte-invariant 28/28; harness self-test 0/10.
- **T — T3's guard landed as `verifiers/check_assertion_floors.py`** with T4's documented trust boundary: floors 10/88/52/82/1504/51; live all-PASS; deletion probes (79/82, 1482/1504, 50/51) and an unparseable-output probe flip it to exit 1.
- **Deliberately not done:** H3's extra self-test cases not merged (22 vs 14 assertions — follow-up); no push (ahead 20); SHONEN untouched.

## Landed changes

- `verifiers/verify_harness_claims.py` (H mode fix), `verifiers/check_assertion_floors.py` (new guard), SCORECARD (freshness/operability rows, move log, **capabilities row 2**, planned), LOG § Round 29, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 29) |
|---|---|---|---|
| H | zero/positive corrupt | exit 0 silent (11 pins) | exit 1 DRIFT naming each |
| H | live gate | 28/28 | 28/28 byte-invariant |
| T | floors guard | absent | live all-PASS; deletion/unparseable probes exit 1 |
| T | capabilities table | 1 row | 2 rows |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held; capability row 2 entered, stagnation window resets); all others unchanged. No trade.
Drift handling: C1's holds resolved by named choices (H semantics, T trust boundary); the 27-not-32 count corrected; debt carried.

## SHONEN

- [~] ×4 — unchanged.
