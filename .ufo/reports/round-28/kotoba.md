# kotoba — round 28 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 28, loop 1 (loop-round 8), dispatched and admitted.
Dispatch HEAD: `44b1733`. Work commit: `e8a81ac` (this report lands in the follow-up publish commit).
Claims: **K** freshness (rekind escape) · **P** operability (pins exact-case + overclaims) — `.ufo/round-28/claims.json`.
Swarm: 16/16 on `zai-coding-plan/glm-5.3-flash` (the summary showed 15; the 16th deliverable is C2's report skeleton — corrected here, the r23-A4 class).
Status: **completed craft round, admitted.**

## Work performed

- **K — K3's kind-consistency arm landed** (K4's pick over K2's zero-declared arm, which stays silent on a partial rekind): full rekind -> exit 1 naming all 8 `id->doc`; partial -> exit 1 naming the 7; live byte-invariant; self-test 75->82 with true-discriminator fixtures.
- **P — P2's exact-case patch landed** (P3-approved): six mis-case variants all exit 2 naming the canonical pin; self-test 46->51; three overclaim sites corrected (SKILL.md:465, capabilities row, corpus doc — the pins fixtures dir is evidence-only).
- **Deliberately not done:** no push (18 unpushed, divergence unchanged); SHONEN untouched; no capability (window stays complete, nudge dormant).

## Landed changes

- `verifiers/verify_surfaces.py` (K3 arm + 2 fixtures), `verifiers/check_substrate_pins.py` (P2 patch), `SKILL.md`/`SCORECARD.md`/corpus doc (overclaim corrections), SCORECARD rows + move log + planned, LOG § Round 28, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 28) |
|---|---|---|---|
| K | full rekind probe | exit 0 (escape) | exit 1 naming 8 `id->doc` |
| K | partial rekind probe | exit 0 (K2's hole) | exit 1 naming 7 |
| K | self-test | 0/75 | 0/82 |
| P | mis-cased key probe | exit 0 silent | exit 2 naming the canonical pin |
| P | self-test | 0/46 | 0/51 |
| gates | seven-gate sweep | — | all exit 0 |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held); all others unchanged. No trade.
Drift handling: one scout fragment lost (recorded); K4's K2-rejection and P3's approval recorded; X10/S4 debt carried.

## SHONEN

- [~] ×4 — unchanged.
