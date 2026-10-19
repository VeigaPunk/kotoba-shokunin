# kotoba — round 35 report (2026-10-19) — LOOP 2 OPENS

Lane: `kotoba-shokunin`. Round 35, loop 2 (round-of-loop 1), dispatched and admitted.
Dispatch HEAD: `48a0720`. Work commit: `<pending — recorded at landing>`.
Claims: **H** freshness (multi-tilde heredocs) · **D** operability (fenced-decoy boxes) — `.ufo/round-35/claims.json` (items array 59; prose said 64 — the count class, corrected).
Swarm: 59/59 on `opencode-go-7` (key 7 probed alive; rotation per the plan).
Status: **completed craft round, admitted.**

## Work performed

- **H — landed on H5's WIDE pattern** (three drafts, two critics converged; C1's 36-form battery = the same pattern): `HEREDOC_RE` captures the full tilde run — `<<EOF~~`/`<<EOF~~~` close like bash (20/20 matrix). An intermediate edit dropped the quotes' optionality → 9 self-test failures caught it before commit. Live byte-invariant; self-test 0/1504; r17:317 third correction (the `~~`-plus clause became false — H6); pin `2b3daa2f`.
- **D — landed on D3's patch with D4's review**: `extract_boxes` skips fenced regions (and terminates continuations at fences) — the fenced `- [ ]` decoy flips 0->1 naming the missing box; live 41/41; 71/71 fixtures unchanged. D4's named residuals (indented-code decoys, short-closer guard, unclosed-fence loud-fail) filed.
- **The N-lane sweep (loop-2 calibration):** 14 per-round re-measurement lanes over rounds 21-34. Headline: **round 29's H claim is FALSIFIED** — M8/N09 prove the zero/positive pin fix is dead code (`:560/563` dispatch before the baseline arm reads `expect`); all 11 corruptions still exit 0. The r29 record stands corrected in LOG § Round 35; the real fix is queued for round 36. Plus 40+ bookkeeping defects filed across the r21-34 reports.
- **Deliberately not done:** the r29-H real fix (queued); the divergence merge (operator's gate); a scout's mid-round merge attempt was aborted and the tree verified clean before landing.

## Landed changes

- `verifiers/verify_skill_checklist.py` (H regex + D fence-skip), `corpus/knowledge/checklist-execution-round17.md` (:317 third correction), routing-16 JSON pin (`2b3daa2f`), SCORECARD, LOG § Round 35, this report + 59 fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 35) |
|---|---|---|---|
| H | `<<EOF~~` probe | exit 0 (body+tail swallowed) | closes like bash (20/20 matrix) |
| H | self-test | 0/1504 | 0/1504 (a bad intermediate caught by it) |
| D | fenced decoy | exit 0, 41/41 parity | exit 1 naming the missing box; 41/41 live |
| calibration | r29 H | claimed closed | FALSIFIED: dead code — fix queued |
| gates | sweep (TMPDIR=/dev/shm) | — | all green; floors 6/6; replay green |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held); **calibration — improved** (the r29 falsification is a calibration gain: a false 'verified' is now a named defect); adjacency / coverage / depth / consistency — unchanged. No trade.
Drift handling: 59-not-64 corrected; the dead-code falsification and the 6/3 window correction recorded; D4/C1 named residuals filed.

## SHONEN

- [~] ×4 — unchanged; S3's recount confirms the box map and marks.
