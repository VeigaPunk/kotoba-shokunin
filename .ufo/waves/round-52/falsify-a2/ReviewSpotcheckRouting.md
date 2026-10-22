Result: HOLDS — every routed item in `corpus/lessons/round-51-verifier-spotcheck.md:158-172` has a disposition at `c8407a453788df964df5a7b835dd0ce1360de882` (fix, criterion, or a stated carry reason); one LOW evidence-pointer defect in the round-52 lesson's citation of the README fix.

Seat: `KotobaR52a2.ReviewSpotcheckRouting`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `c8407a4` (branch `master`; only `SCORECARD.md` dirty — attack target, reviewed below). All commands read-only; no lane writes.

## Defect 1 — `corpus/README.md` stale lever set + unqualified count — FIXED

- Core note: round-52 correction appended in the same bullet at `corpus/README.md:158-167`
  ("**Round 52 correction (append-only; routed defect 1 …):** … `overlap levers backed 4 of 7 clients`
  on the counter committed with the round-51 plan (`7c81a787`) … `7 of 7` holds only on the counter
  widened after the plan (lesson M35, Q28)"), naming the falsify-corrected lever set including
  `removed in a scope` for Copilot SDK and Gemini CLI.
- Index row `corpus/README.md:75` carries "**Round 52 correction (routed defect 1):** the effects in
  the landed table are `removed in a scope` (Copilot SDK, Gemini CLI) or `automatic choice off` … the
  declared round-51 count is 4 of 7 on the plan-commit counter `7c81a787`". The "removed in a scope"
  omission the spot-check named is corrected.
- Sweep check: `python3 -B verifiers/check_correction_sweep.py --rev c8579a4c…` → 3 FAILs
  (`r51-c2-readme` `corpus/README.md:119`, `r51-c2-scorecard-lead` `SCORECARD.md:28`,
  `r51-c2-province` `PROVINCE.md:17`), `correction sweep: 3 stale block(s)`, exit 1.
  `--rev c8407a45…` → `correction sweep: 0 stale block(s)`, exit 0. (M36 fix is real and able to fail.)
- Un-routed third stale place also corrected: `PROVINCE.md:18` carries "Round 52 correction (lesson
  M36; found by the round-52 sweep): the declared round-51 result is `overlap levers backed 4 of 7
  clients` …".

LOW finding — mis-cited line range in the lesson's own evidence: `corpus/lessons/round-52.md:70`
says the correction was "appended inside the same bullet (`:144-153`)", but at `c8407a4` the
correction block is `corpus/README.md:158-167`; `:144-153` straddles the end of the Round-50 note and
the start of the Round-51 note it corrects. The fix exists and the sweep passes; only the pointer is
wrong. Severity: LOW (record accuracy, no behavioral effect).

## Defect 2 — `SCORECARD.md:28` depth lead — FIXED

`SCORECARD.md:28` now opens "**round 51 (C2 — overlap levers by client, the learning claim; not
verified as declared; depth holds 9):** declared result, on the counter committed with the plan
(`7c81a787`): … `4 of 7`, exit 1 on the landed content". The widened `7 of 7`, exit 0 @ `34cfffbb`
is labelled "Second measurement, never the declared one (Q28)"; "four counted rows are new … (the
'six' first written here was the pre-falsify count)". Covered green by the sweep (above).

## Defect 3 — C2 not re-declared — DISPOSITIONED (stated reason, not a fix)

`plans/round-52.md:14-16`: "The round-51 C2 claim (overlap levers by client) is not re-declared: its
surface … has carried a claim in rounds 49, 50 and 51, and the drift sentinel asks for a different
frontier area." `corpus/lessons/round-52.md:74` repeats it. The spot-check's condition ("to claim
the per-client lever count, re-declare with frozen tables") was not invoked — no such claim is made.
The round-52 C2 counter `check_mcp_instructions.py` is frozen at the plan commit `4c003a4b` per
`plans/round-52.md:8` and `SCORECARD.md:30`. Consistent with the session rule.

## Defect 4 — carried items

| sub-item | disposition at c8407a4 | evidence |
|---|---|---|
| S031 superseding row | FIXED | `corpus/SOURCES.md:51` S038 row, `teaches` cell reads "supersedes S031 — the page documents the frontmatter field `disable-model-invocation`, the `ignoredSkillsLocations` setting and the `copilot skill disable` command; it does not contain `disabledSkills` (0 occurrences), which S031 named"; Gate record `corpus/lessons/round-52.md:35-40` (quote `:1300`, grep sweep counts); append-only, S031 unchanged in place (`round-52.md:62`). |
| S024 superseding row | CARRIED with reason | No `supersedes S024` row in SOURCES.md (grep: none); `round-52.md:75-77` "carried, not worked: the build wave that held them never received a seat grant and the route for their executor and scribe seats was down (M37)"; also uncommitted `SCORECARD.md` "Next: round 53" lists it. |
| fixture labels lines 9/15/33 | CARRIED with reason | `git diff c8579a4c c8407a45 -- verifiers/fixtures/surfaces/strings-omp-18.12.6.txt` → empty; lines 9 and 15 remain bare `}`, line 33 an unlabelled non-dump marker; same `round-52.md:75-77` carry reason. |
| D2 F1–F5 | CARRIED with reason | `SKILL.md:150` still reads "(`.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1–F5, carried)"; `round-52.md:75-77` carry reason; SCORECARD round-53 list. |
| D7 items | CARRIED with reason | `verifiers/box_proof_case_deletion.py` still has no `--self-test` (grep: no matches) — the D7 blocker stands; `round-52.md:75-77` carry reason. |
| R1, R5 | CARRIED with reason | `round-52.md:75-77`; SCORECARD "Next: round 53" names "the R5 v2 configured-root oracle; R1's no-name fallback". |

Carry reason is grounded in M37 (`round-52.md:11`): seat-gate starvation (acquire timed out after
3,600 s; second acquire pending at 17:10Z) plus the executor/scribe/mutation route outage — a
documented capacity event, consistent with this wave being the a2 re-attack. No sub-item is silently
dropped; none of the three dispositions is missing, so no BREAK.

## Session-rule question — "a target missed on frozen tables is an honest stop, never a widened table"

Substantively captured, by two rows split across the two halves of the rule:

- `corpus/QUALITY.md:39` Q28 (grounded in M35, `corpus/lessons/round-51.md:146`): "A counter's
  judgment tables … are frozen at the plan commit; a later change to them is reported as a second
  measurement beside the declared one, never in its place, and the claim's verdict is read on the
  declared counter." This is the "never a widened table" half; reading the verdict on the declared
  counter forces the honest-stop verdict when the target is missed.
- `corpus/QUALITY.md:26` Q15 (M11): "An honest stop names its blocker and leaves axes unchanged; it
  is a valid round outcome, recorded as such." — the "honest stop" half, as a standing preserve rule.
- `corpus/QUALITY.md:40` Q29 (new, M36) is a different rule — corrections must be registered in
  `verifiers/check_correction_sweep.py` in the same commit — not the frozen-tables rule.

No single criterion states the session rule verbatim; Q28 + Q15 together cover both clauses. If the
operator wants the sentence itself in a row, that is a wording addition, not a gap.

## Uncommitted `SCORECARD.md` (attempt-1 leftover, attack target)

`git diff -- SCORECARD.md`: prepends the round-52 C2 paragraph to the coverage lead and round-52 C1
to the freshness lead, adds a "Round 52 completed … / Next: round 53" block listing the carried items
(S024 row, fixture labels 9/15/33, R5, R1, D7, D2 F1–F5), and appends two round-52 move-log rows.
Depth lead (defect 2's fix) is untouched. No regression of any routed disposition; it records the
carries to round 53 consistently with the lesson.

Installs: none. No network access performed.
