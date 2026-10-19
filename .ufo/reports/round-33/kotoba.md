# kotoba — round 33 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 33, loop 1 (round-of-loop 13), dispatched and admitted.
Dispatch HEAD: `35e4f62`. Work commit: `68918b4` (this report lands in the follow-up publish commit).
Claims: **X** freshness (corpus-index exclusion class) · **F** operability (box-map absolute floor) — `.ufo/round-33/claims.json`.
Provider: `antigravity/gemini-4-argon` failed on a 2-lane probe with the same `502 token/shim error` as round 12 — the lane's auth shim is broken for a second consecutive round (operator-level; loop-2 rounds 44/45 and loop-3 rounds 58/59 will hit it unless repaired). Identical items on `devin/deepseek-v4-1-flash-high` per the exhaustion clause.
Swarm: 8/8 on the substitute lane.
Status: **completed craft round, admitted.**

## Work performed

- **X — X2's pair landed** (checker + independent companion; X4's review could not read the drafts and was outweighed by X2's direct evidence): FILE tokens that are /-ending, absolute/~ -rooted, or whitespace-bearing are classified and checked instead of silently dropped. Proofs: all 8 planted dead shapes flip exit 0->1 and **both instruments agree** (they diverged before — independent caught dir tokens, integrity did not); the 2 live dropped tokens (README :44/:57) re-enter the census (index_patterns 67->69, observed-only); live 9/9 byte-invariant; self-test 88->108; floors bumped 88->108 in-step.
- **F — F1's pinned-field design landed** (F3's circularity catch rejected the map-length floor — it shrinks with the shrink): `checklist-baseline.json` gains `"box_total": 41`, validated in `load_map`; `check_box_map` fails when live boxes < floor or entries != floor. Proofs: the r32 two-sided shrink (1/5/33/40) fails naming the floor; M1's one-sided classes still flip; live 10 × PASS; self-test 0/1504; routing pin updated (`e26f1939`). Residual (F1, documented): removing the key AND the shrink passes — the map-custody trust boundary. (`.ufo/round-33/SKILL.md` is F1's probe fixture copy — evidence, not a stray.)
- **Deliberately not done:** no push (28 unpushed); SHONEN untouched.

## Landed changes

- `verifiers/verify_corpus_integrity.py` + `verifiers/verify_corpus_independent.py` (X2 pair), `verifiers/verify_skill_checklist.py` + `verifiers/checklist-baseline.json` (F1), `verifiers/check_assertion_floors.py` (floors 108), routing-16 JSON pin, SCORECARD, LOG § Round 33, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 33) |
|---|---|---|---|
| X | planted exclusion shapes (8) | silent drop / divergence | all flip; instruments agree |
| X | census | 67 patterns (2 dropped) | 69 (all checked) |
| X | self-test / floors | 0/88, floor 88 | 0/108, floor 108 |
| F | two-sided shrink | exit 0 (evaluated 8) | exit 1 naming the floor |
| gates | sweep | — | all green (replay, corpus, floors, fault@/dev/shm) |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held; the r32 HIGH closed); all others unchanged. No trade.
Drift handling: the antigravity outage recorded with loop-2/3 flags; F3's circularity catch and F1's residual documented; the publish-time citation FAIL (this report not yet existing) is the check working — resolved by this file.

## SHONEN

- [~] ×4 — unchanged.
