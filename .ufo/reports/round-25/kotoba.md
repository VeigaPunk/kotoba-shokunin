# kotoba — round 25 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 25, loop 1 (loop-round 5) — the loop's verification/correctness sweep over rounds 21-24.
Dispatch HEAD: `123ea62`. Work commit: `a46321c` (+ record fix `1e899a1`; this report lands in the follow-up publish commit).
Claims: **V1** freshness (re-verify every artifact landed in rounds 21-24) · **V2** calibration (re-measure every number in rounds 21-24's records) — `.ufo/round-25/claims.json`. Scout C1 put both on HOLD as filed (shape only: no command manifest; L0 uncommitted; count discrepancies) — corrected in the round record; substance verified.
Swarm: 64/64 on `openai-codex/gpt-6-luna-max`.
Non-author rule: a lane-dispatched swarm is the lane — **no SHONEN [x] claimed**; scout C2 delivered the [x]-readiness pack (per-box procedures + aggregator repair request) for a non-kotoba verifier.
Status: **completed craft round, admitted.**

## Work performed

- **V1 — artifact re-verification (scouts W01-W16):** r21 surfaces fix re-extracts 8/8 loader classes from the live binary + vacuity fires on stripped dumps; probe-dir fixture green in clone AND export, rmdir → exactly 2 failures; omp pins hold (round-18 replay still exits 1 naming the pin); routing counts 14 delta-0 with frozen replay 226/14/14/0; corpus-baseline 53/36 matches. r22: byte-gate `e046a025…` reproduces, contiguity + no-dup hold, surfaces 7/7; L0 append still prefix-pure (50 lines, uncommitted — integrator-owned). r23: pins guard live 3/3 (delta 0 ns) + all six probes on /tmp copies + fixtures green in clone/export/foreign-cwd + capabilities row evidence green. r24: every errata value re-measures; Fix A re-proven (export 0/1504 exact; live byte-identical; probe-dir → 2; tamper → box_map FAIL); checklist sha == routing JSON pin.
- **V2 — record re-measurement (scouts N01-N12):** every number in the four rounds' reports/LOG/SCORECARD re-measured. Corrections filed in LOG § Round 25: r23 "64 items" → 63; r23 "518/+2" → 521/+5; r24 "48 items" → 45; the round-12 erratum's "43 = 43 at either" → 43/37 per tree (fixed in the file in-round); r22's figures are commit-context differences (named).
- **Red probes (M/X lanes):** 20/20 flip — box tamper, surfaces vacuity, corpus dead pointer + stale-pattern, independent hash, harness catalogue, checklist heredoc, pins (sha/mtime/missing/VACUOUS/PIN_ABSENT), OC-1 anchor, new-callee corruption, fault class (d) both instruments.
- **In-round repairs:** baseline.json:7 stale note; census erratum self-drifted citation; round-12 erratum tree-pairing; 4 ignored .pyc removed.
- **Deliberately not done:** no [x] claims; no sibling/fleet writes; no push (ahead 11).

## Landed changes

- Four repairs (above) + SCORECARD (freshness row, move-log rows, planned) + LOG § Round 25 + this report + 64 fragments.
- Intentionally unchanged: the filed rounds 21-24 reports (records — corrections live in this round's entry).

## Before → after measurements

| Claim | Measurement | Before | After (round 25) |
|---|---|---|---|
| V1 | artifacts re-verified | lane-authored single-session checks only | 64-lane re-verification, all green; 4 repairs; debt filed |
| V1 | red probes | — | 20/20 flip |
| V2 | records re-measured | spot-checked only | 12 lanes; 5 corrections filed + 2 fixed in-round |
| gates | seven-gate sweep | — | all exit 0 (pins guard incl.; 3/3 hold) |

Axis verdicts: **freshness — improved** (8.0 held: the loop's landed work is now cross-verified); **calibration — improved** (8.5 held: records re-measured, corrections filed); all others unchanged. No trade.
Drift handling: C1's holds corrected the claim shape (recorded); W05/G05/X03/L0/credits filed as debt; count corrections filed against rounds 23-24's own records.

## SHONEN

- [~] ×4 — unchanged; the [x]-readiness pack (scout C2) is staged for a non-kotoba verifier; nothing here is non-author evidence.
