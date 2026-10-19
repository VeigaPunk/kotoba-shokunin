# kotoba — round 30 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 30, loop 1 (loop-round 10), dispatched and admitted on critic-amended mechanisms.
Dispatch HEAD: `b761cd6`. Work commit: `8e0d53a` (this report lands in the follow-up publish commit).
Claims: **F** freshness (fault-harness tautology) · **D** operability (heredoc scanner) — `.ufo/round-30/claims.json` (items array 28; prose said 32 — corrected, the r23/r24 count class).
Swarm: 28/28 on `devin/deepseek-v4-1-flash-high`.
Status: **completed craft round, admitted.**

## Work performed

- **F — F3's control-world design landed** (the filed fix proven inert by C1/F5/R2): pristine control clone + delta==1 requirement; M7's no-op plant FAILs; 11 worlds verified (F5); exit codes intact; live ALL PASS byte-invariant; self-test 4->8. The (h) premise was false (no independent row exists) — recorded as the correction. Limit: alias re-exec still passes (F3, narrowed-not-closed).
- **D — D4's operator-level scanner landed** (D4 rejected both naive drafts over the `$(...)` regression): HEREDOC_RE `([A-Za-z0-9_]*~?)` + `heredoc_delimiter()` walk + call-site swap; 11/11 bash matrix; 71 fixtures unchanged; round-17 fixtures exact; self-test 0/1504; routing pin `15d0aa16`->`4d3d38c9`.
- **Deliberately not done:** the r17 ceiling doc direction (debt); no push (22 unpushed); SHONEN untouched.

## Landed changes

- `verifiers/fault_injection_corpus.sh` (F3), `verifiers/verify_skill_checklist.py` (D4), routing-16 JSON pin, SCORECARD rows + move log + planned, LOG § Round 30, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 30) |
|---|---|---|---|
| F | no-op plant probe | PASS (tautology) | FAIL (control-world delta) |
| F | fault self-test | 4 assertions | 8 |
| D | X11 quoted/comment `<<EOF` | phantom heredoc (checker 0, bash 1) | operator-level parse (11/11 matrix) |
| D | `<<EOF~` terminator | mis-captured | captured |
| D | self-test / fixtures | 0/1504, 71 dirs | unchanged |

Axis verdicts: **freshness — improved** (8.0 held); **operability — improved** (8.5 held); all others unchanged. No trade.
Drift handling: F's inert filed fix replaced by the verified design (recorded); the false (h) premise recorded; 28-not-32 corrected; debt carried.

## SHONEN

- [~] ×4 — unchanged.
