# kotoba — round 26 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 26, loop 1 (loop-round 6), dispatched and admitted.
Dispatch HEAD: `10bf6d3`. Work commit: `6fa44f3` (this report lands in the follow-up publish commit).
Claims: **R** adjacency (routing-replay guard repair) · **I** operability (independent-verifier crash class) — `.ufo/round-26/claims.json`.
Provider: grok-4.7-fast 403-exhausted on all 46 reported lanes → recorded substitution to `devin/deepseek-v4-1-flash-high` (no stated fallback for loop-round 6; general exhaustion clause). 48 items, all fragments landed.
Status: **completed craft round, admitted** — both claims verify; no axis harmed.

## Work performed

- **R — guard repair (R4's pick of three drafts, R3a):** the replay code in `sibling-citation-routing-round16.md` now reads `fixture["instrument"]["sha256"]` + fails closed (`instrument_pin_absent`). Integrator proofs: `HEAD frozen` → exit 0 (`226/14/14/0/4/3`); before-revision `581e293` → exit 0 (the documented Before command runs again); tamper/re-pin discriminating probes flip per R3.
- **I — crash class (F4's pick, F2's diff applied verbatim):** `_open_text` at every read site; a deleted/dangling/dir/no-perm tracked file → EnvError exit 2 naming the file (primary parity), no traceback. Integrator proofs on a `cp -a` copy: crash exit 2 (primary exit 2), self-test 0/52, live agreement + primary 9/9, red probes flip.
- **Sweep (S/M/X lanes):** ack 0/5 sixth measure; L0 line pure-append, uncommitted (integrator-owned); all red probes flip; fixtures/gates baselines green. Named debt filed in LOG § Round 26 (X14 shallow-clone divergence — high; S7 pins-fixtures orphan; M4 harness expect-not-read; X8 six stale README counts; X10/X11/X12/M2 escape classes; S3 SHONEN command drift; X16 quota precheck signal).
- **Deliberately not done:** no git-state changes (divergence/shallow filed for loop-14); no sibling/fleet writes; no push (ahead 14).

## Landed changes

- `corpus/knowledge/sibling-citation-routing-round16.md` — guard repair [LOG § Round 26].
- `verifiers/verify_corpus_independent.py` — F2's diff [LOG § Round 26].
- SCORECARD (adjacency/operability rows, move log, planned), LOG § Round 26, this report + 48 fragments (X3 as `X03.md`).

## Before → after measurements

| Claim | Measurement | Before | After (round 26) |
|---|---|---|---|
| R | published replay | exit 1 `instrument_drift` (all three modes) | exit 0 at HEAD + before-revision; tamper flips |
| I | crash probe | exit 1 `:313` traceback | exit 2 classified, naming the file (primary parity) |
| I | self-test | 0/52 | 0/52 exact; agreement re-proven |
| gates | seven-gate sweep | — | all exit 0 |

Axis verdicts: **adjacency — improved** (8.0 held: the replay tooling is truthful again); **operability — improved** (8.5 held: the instrument classifies instead of crashing); all others unchanged. No trade.
Drift handling: grok→devin substitution recorded; C2's stagnation correction (window 2/3, no reset from I) recorded; sweep debt filed.

## SHONEN

- [~] ×4 — unchanged; no non-author evidence this round.
