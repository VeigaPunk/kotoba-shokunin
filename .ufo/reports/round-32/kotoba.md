# kotoba — round 32 report (2026-10-19)

Lane: `kotoba-shokunin`. Round 32, loop 1 (loop-of-round 12), dispatched and admitted on the critic-corrected set.
Dispatch HEAD: `419a13b`. Work commit: `<pending — recorded at landing>`.
Claims: **E** calibration (three filed errata) · **W** freshness (pins whitespace keys) — `.ufo/round-32/claims.json` (items array 29; prose said 32 — corrected).
Provider: antigravity/gemini-3.8-flash **failed on all lanes** (`502 token/shim error` — the auth shim itself is broken; a retry probe confirmed); identical items reran on `devin/deepseek-v4-1-flash-high` per the exhaustion clause. **Round 13's gemini-4-argon will likely hit the same shim.**
Swarm: 29/29 on the substitute lane.
Status: **completed craft round, admitted.**

## Work performed

- **E — landed amended.** Scout C1/E1 falsified the filed erratum (a) at dispatch: round 30's `~?` fix already repaired `<<EOF~`, so the filed row would have written a new falsehood. E1's corrected row landed (quoted forms still over-catch; single `~` fixed; the true `~~`-plus under-catch named). E(b): SHONEN:20 27->28. E(c): dated recount note appended (round-16 values were exact at the note's own commit). No mark touched; E5's interlock proof + positive control.
- **W — W3's unicodedata variant landed** (W4's pick): 13 whitespace-edged key shapes rejected (exit 2, both forms named); trim disqualified as laundering; live byte-invariant; self-test 51->62; floors bumped in-step.
- **Deliberately not done:** the `~~`-plus scanner fix (named, not claimed); no push; SHONEN marks untouched.

## Landed changes

- `corpus/knowledge/checklist-execution-round17.md` (:317 row), `SHONEN.md` (two corrections + recount note), `verifiers/check_substrate_pins.py` (W3), `verifiers/check_assertion_floors.py` (floors 62), SCORECARD, LOG § Round 32, this report + fragments.

## Before → after measurements

| Claim | Measurement | Before | After (round 32) |
|---|---|---|---|
| E(a) | r17:317 row | false in both directions | names the true residual (~~-plus) |
| E(b)/(c) | SHONEN counts | 27; 9/67/1283 | 28; dated recount note |
| W | padded-key shapes (13) | exit 0 silent | exit 2 naming both forms |
| W | self-test / floors | 0/51, floor 51 | 0/62, floor 62 |
| gates | sweep (TMPDIR=/dev/shm) | — | all green |

Axis verdicts: **calibration — improved** (8.5 held); **freshness — improved** (8.0 held); all others unchanged. No trade.
Drift handling: the filed erratum falsified and corrected pre-landing (C1/E1); antigravity shim failure recorded with the round-13 flag; 29-not-32 corrected; debt carried (M1 HIGH: box-map parity floor — filed).

## SHONEN

- [~] ×4 — unchanged; E(b)/(c) corrected evidence prose only.
