# CriticFalsify — round 89 wave r89-w1 (attack seat)

Full verdicts, commands and observed lines: `.ufo/waves/round-89/w1/CriticFalsify/attacks.md`.
Receipts: `.ufo/waves/round-89/w1/CriticFalsify/receipts/`. Lane read at `0f2b866`; predicates unchanged since the draft
(`git diff 43fc784 HEAD -- plans/round-89.md` empty).

## Verdicts

| claim | attack | verdict |
|---|---|---|
| C1 | refuses an unsatisfiable freeze (the gate only compares declared text with a receipt-grep simulator) | ATTACK STANDS |
| C1 | exit 1 naming `w_added_red`; fixed plan exit 0 | REPELLED (arms exist; observed) |
| C1 | do-nothing: an existing verifier already refuses the r88 world | REPELLED (none parses a plan Controls block) |
| C1 | shortcut (a) killed by the r88-controls arm | ATTACK STANDS (exit-only stub holds, exit 0) |
| C2 | "instance-level": D5(iii) is count-level | ATTACK STANDS (same-count swap passes) |
| C2 | `instance drift K` pinned at 0 vs >0 | REPELLED (arms at v3:948/998); K counts names, label wrong |
| C2 | do-nothing: frozen v2 reads the added-instance world PASS | REPELLED (v2 `5 of 5`, exit 0, observed) |
| C2 | vacuity at the landing tip | REPELLED for corpus growth (exit 1 on one appended line); STANDS for out-of-corpus and swaps |
| C2 | Q79 location: receipt in lane, controls in clones | ATTACK STANDS, blocking (`report_dead 1>0`, `4 of 5`, exit 1 at the same revision) |
| C2 | M87-1 launder guard survived into v2/v3 | ATTACK STANDS (v2 has zero launder/blob guard hits; probe E green) |
| kill rule | freeze diff path covers all inputs | ATTACK STANDS (C2 base receipt, round-88 receipts read by the sims, SKILL.md rows, uncommitted state) |
| Q80 | attack seats present | REPELLED (4 planned; MutTesterGates output still open) |
| sourced | S258 quotes; S259 quotes | REPELLED for quotes (verbatim, located, ≤25 words); STANDS for the `teaches` inference and two S259 word counts |
| sourced | S258 failed route not paraphrased | REPELLED (route (a) is a different article; not used) |

## Pre-data narrowing for the L1 (must land before the first candidate score)

1. **N1 (C2, blocking, Q79).** Materialize `.ufo/reports/round-76/kotoba.md` as a world-local commit in every clone world and in `w_equivalence`. Probe B (materialized) → `5 of 5`, exit 0; probe A (symlink) → `4 of 5`, exit 1.
2. **N2 (C2, blocking, Q26).** Choose: bound the headline to count-level and rename K, or add a detail-identity leg with probe E as a control expecting exit 1.
3. **N3 (C2, Q26/Q37).** Bound D5 to corpus `*.md` citations, or add a named `w_relocated` control (probe F currently exit 0).
4. **N4 (C2, regression).** Reinstate the M87-1 blob-immutability conjunct for `corpus/lessons/round-81.md` and `round-86-verifier-spotcheck.md`; probe E is its control. Otherwise disclose the dropped guard.
5. **N5 (C2, Q79).** `write_base_receipt` asserts a clean tree and writes from the freeze commit.
6. **N6 (C1, Q26/Q37).** Either the sims run the instrument, or the C1 headline is bounded to "refuses a declaration that contradicts the recorded verdict".
7. **N7 (C1, Q37).** Refuse exit-only or literal-less control declarations (exit 3) or require a stdout literal per control; `stub-exit-only.md` currently holds.
8. **N8 (kill rule).** Extend the freeze diff path to `.ufo/waves/round-89/{receipts,w1}`, `.ufo/waves/round-88/{w1/ExecMonotoneD5,w1/ExecMonotoneD5.md,w1/ReviewerC2,w1/CriticFalsify,receipts}`, `SKILL.md`, `scripts`, `LOG.md`, `SCORECARD.md`; add clean-tree and ignored-file checks and the `-`-line check on the freeze diff of the plan.
9. **N9 (sourced).** Label the `teaches` line as the lane's inference; use `PMC5856500`; correct S259 word counts (18 and 8).
10. **N10 (Q80).** MutTesterGates output must land or the round closes provisional.

## Risks

- The C2 gate's do-nothing control is real: v2 is blind on the added-instance world. The v3 gate catches it (`FAIL d5iii`, exit 1), so the discrimination control is non-vacuous, but only for corpus-scope growth and only at count level.
- The lane HEAD moved from the plan base `a5b3b15` to `0f2b866` (wave dispatch commit). Predicates are unchanged; the freeze receipts must name the freeze commit.
- `verifiers/check_freeze_gate.py` and `check_r86_routed_repairs_v3.py` were read and run in their current untracked state; both may change before freeze, and these verdicts apply to the state read here.
- No instrument was edited; no git write was run; no tool was installed or updated.
