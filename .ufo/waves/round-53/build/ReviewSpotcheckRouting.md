Result: MIXED — all six round-52 spot-check routed defects have a disposition in `plans/round-53.md`, but six items of the SCORECARD `Next: round 53` block have no disposition there, and the round-52 lesson's carried items are named as carried only in `corpus/lessons/round-52.md:114` and `SCORECARD.md:130`, never in the round-53 plan itself.

Seat: `KotobaSpelling`-independent reviewer `KotobaR53.ReviewSpotcheckRouting`; read-only, no sandbox clone needed (nothing written but this report; no git/jj writes anywhere; no lsp server consulted — this is a routing check over markdown planning documents, so all evidence below is text-level with path:line pointers; no code definitions or callers were at issue). Method: full read of `plans/round-53.md`, targeted reads/greps of the three routing sources, glob sweeps for operator lesson files. All paths below are relative to the lane root.

## 1. Round-52 spot-check §6 routed defects → `plans/round-53.md` (6 of 6 dispositioned)

Source: `corpus/lessons/round-52-verifier-spotcheck.md` § 6 (items 1–6). Plan section: `plans/round-53.md` § "Routed defects from the round-52 spot-check (repairs, not claims)" (items 1–6). The lists are one-to-one; nothing widened.

| §6 item | plan disposition | verdict |
|---|---|---|
| 1. Re-derive and re-pin opencode 1.19.4 | plan item 1: "this is C1" (claim, `surfaces pass 7 of 7 … pins OK 3/3 … kept 9 of 9 … self-test 0 failure(s)`, exit 0) | routed |
| 2. Re-record `verify_corpus_integrity` baseline | plan item 2: index the spot-check file; resolve or classify the 5 fleet-report pointers in the instrument with a self-test arm; re-record the baseline last (repair, detailed) | routed |
| 3. Self-test arms for the two attempt-2 C1 fixes in `verify_surfaces.py` | plan item 3: arms for unresolved-group admission and the empty-baseline fallback, "each shown able to fail by reverting its fix" (repair) | routed |
| 4. Tighten the C2 counter class (`MutMcpCounter` M12 host-prefix pin, M16 quote-substring) | plan item 4: QUALITY criterion grounded in a round-53 lesson row; `verifiers/check_mcp_instructions.py` tightened so both mutants are killed, with self-test arms; round-52 declared results re-measured on the plan-commit counter (repair) | routed |
| 5. Drift sentinel — work a different frontier area | plan item 5: "handled by C2's choice of frontier (above) and by Q26 statements" (handled with a reason) | routed |
| 6. Q30 sweep before any client absence is recorded | plan item 6: "Q30 already landed in round 52 (`corpus/QUALITY.md:41`); this round applies it to every client negative" (landed with a reason + application). Citation verified: the Q30 row is exactly at `corpus/QUALITY.md:41`. Plan C2 also binds it per client: "any client recorded as silent carries the Q30 three-part sweep or is recorded `not checked`" | routed |

No defect in §6 is unaddressed; none of the six is silently dropped.

## 2. `SCORECARD.md:130` `Next: round 53` block → plan dispositions (5 of 11; 6 gaps)

Full block text (read raw, one line): the Q19 re-measure instruction, the drift-sentinel sentence, then nine candidate clauses. Disposition as stated in `plans/round-53.md`:

1. "re-measure every before-value first (Q19)" — plan header: before-values measured by the L1 2026-10-22T19:50–19:54Z at `e78dff66` (Q19), quoted per claim. **Dispositioned.**
2. "Drift sentinel (seat `CriticLearning`) … round 53 works a different frontier area" — plan item 5 (§1 above). **Dispositioned.**
3. "opencode 1.19.4 re-derivation and re-pin" — C1. **Dispositioned.**
4. "whether omp reads MCP server `instructions` and where (Frontier; kotoba's own host)" — **missing.** The plan never mentions MCP server `instructions` for omp. (Its C2 client list "Codex, opencode, Gemini CLI, Copilot, Cursor, agents.md, omp" is AGENTS.md/CLAUDE.md resolution, a different surface.) C2's "different frontier area" rationale implicitly passes over this candidate but does not name it as carried.
5. "plugin instruction surfaces" — **missing.** The word "plugin" does not occur in the plan.
6. "the C1 limits found by the falsify wave (member-call loaders, a new callee with only an undeclared pair, decoy stand-ins) and a self-test arm for the attempt-2 unresolved-group admission fix" — split. The self-test arm is dispositioned (plan item 3 covers both attempt-2 fixes). The three named limits are **missing**: the plan's nearest text ("What the counter does not measure … OC-4/OC-6 rules match the loader code they name … reviewer and mutation-tester work in wave 2") is about opencode rule anchoring, not the omp extraction limits, and names none of the three.
7. "the C2 counter's loose host pins and substring Gate rule for the next counter (`MutMcpCounter` M12, M16)" — plan item 4. **Dispositioned.**
8. "the R5 v2 configured-root oracle" — **missing** in the plan; carried with a reason in `corpus/lessons/round-52.md:114` only.
9. "R1's no-name fallback" — **missing** in the plan; carried in `round-52.md:114` only.
10. "the D7 items" — **missing** in the plan; carried in `round-52.md:114` only.
11. "D2 F1–F5 (carried with reasons in `corpus/lessons/round-52.md`)" — carried with a reason, but in the block's own text, not in the plan.

Calibration note: the block's clauses are labelled "Candidates", so the plan was free not to claim them; but this review's question is whether each has a claim, repair, or carried-with-a-reason disposition, and for items 4, 5, the limits trio, 8, 9 and 10 the plan gives none — it neither claims nor names them as carried. Items 4 and 5 in particular are frontier alternatives with no carried-with-reason naming anywhere current (the `corpus/README.md` § Frontier rows predate this round and list "Executed checklist coverage" and "MCP/plugin instruction surfaces" as areas, not as round-53 dispositions).

## 3. `corpus/lessons/operator-*.md` files — none, confirmed

- `glob corpus/lessons/operator-*.md` → "No files found matching pattern".
- Broader sweep `glob corpus/lessons/*operator*` → "No files found matching pattern".

Zero operator lesson files exist, matching the expectation; no dispositions are owed for them.

## 4. Round-52 lesson carried items (D2 F1–F5, D7, R1, R5) named as carried somewhere current

Carried, identified at origin:

- **D2** = round-50 spot-check calibration defect: `SCORECARD.md:31`/`SKILL.md:135` claim the checklist gate runs `--box-proof` with no fail-open bound (`corpus/lessons/round-50-verifier-spotcheck.md:252-254`); findings F1–F5 at `:143-148` (PASS "not run" on an unprobeable delegate; F3–F5 false-red/crash arms; 4 `MutBoxProofGate` survivors).
- **D7** = `round-50-verifier-spotcheck.md:270-274`: C2-driver laundering, stderr-substring kill test, two crash paths, `box_proof_case_deletion.py` unfloored, arms F30–F33 unapplied.
- **R1** = `round-48-verifier-spotcheck.md:154-157`: configured/log-named roots keyed by directory name vs the agents root keyed by frontmatter name — the no-name double-count.
- **R5** = `round-48-verifier-spotcheck.md:167-168`: built-in marker join still open; the 13-case oracle lacks a nested-skill/frontmatter-name case (the v2 configured-root oracle).

Naming as carried, in current text:

- `corpus/lessons/round-52.md:114-115`: "D2 F1–F5, the D7 items, R1 and R5 stay carried: attempt 1 had no build seats (M37) and attempt 2 spent its one wave on falsifying the landed claims." — all four groups named as carried, each with the round's reason. This is the latest lesson, so the carried set plus reasons is on record in current corpus text.
- `SCORECARD.md:130` (`Next: round 53`, the current forward block): "the R5 v2 configured-root oracle; R1's no-name fallback; the D7 items; D2 F1–F5 (carried with reasons in `corpus/lessons/round-52.md`)." — all four named; the explicit "carried" label and reason pointer sit only on D2 F1–F5, while R5, R1 and D7 appear there as candidates without a carried label.
- `plans/round-53.md`: **none of the four is mentioned anywhere in the plan** (full-file read; grep for `carried`, `D7`, `R5`, `R1`, `F1` over the plan returns no relevant hit). The plan therefore gives no disposition to any carried item, even as carried-with-reason.

Net: the carried set is named as carried somewhere current (the round-52 lesson, with the SCORECARD forward block pointing at it for D2 F1–F5), but the round-53 plan itself carries nothing forward by name — which is the same gap as in §2.

## Findings (severity order)

1. **Routing gap (medium, plan-level):** six `Next: round 53` items lack any disposition in `plans/round-53.md` — omp MCP `instructions` (block item 4), plugin instruction surfaces (item 5), the three C1 falsify-wave limits (item 6, first half), R5 (item 8), R1 (item 9), D7 items (item 10). Evidence: full read of `plans/round-53.md` (85 lines; no occurrence of any of these terms) against `SCORECARD.md:130`. Two of them (omp MCP `instructions`, plugin surfaces) have no carried-with-reason naming anywhere current either — C2's different-frontier rationale supersedes them implicitly, without naming them.
2. **Carried set not restated in the plan (low):** D2 F1–F5, D7, R1, R5 are named as carried in `corpus/lessons/round-52.md:114` (with reasons) and named in `SCORECARD.md:130` (explicitly carried only for D2 F1–F5), but `plans/round-53.md` — the document this round is judged against — never names them. If the round closes with the plan as the sole routing record, a reader of the plan alone sees no trace of the carried debt.
3. **Non-finding, verified clean:** all six §6 routed defects are dispositioned in the plan one-to-one, with no widening (plan routed-defect list has exactly six items); the plan's Q30 citation `corpus/QUALITY.md:41` is exact; operator-*.md count is zero as expected.

## Residual risk and verification gaps

- Whether SCORECARD "Candidates" impose a disposition duty at all is a campaign-convention question, not decidable from the bytes; this report applies the assignment's framing (each item needs claim/repair/carried-with-reason). Under a looser reading (candidates are options; only §6 defects and explicit carried items are obligations), the plan's only defect would be finding 2.
- I checked carried-naming in the plan, the current SCORECARD forward block, and the latest lesson only, per the assignment's "somewhere current"; I did not sweep LOG.md or wave-1 seats' in-flight reports for additional carried-item naming, and none is needed to satisfy the check as assigned.
- No commands were executed against counters or gates (this seat reviews routing only); every claim above is grounded in the file reads and globs cited, with no inference beyond the two places marked as reading rationale ("implicitly supersedes", "nearest text") which are labelled as interpretation of named adjacent text.
