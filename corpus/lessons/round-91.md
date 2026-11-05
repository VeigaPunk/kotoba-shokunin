# Round 91 — kotoba (Linux host, omp 18.15.0): lesson

Author: **ScribeCorpus** (scribe seat). This file is the round-91 **scaffold**: the Gate record, the
Mistakes row and the Considerthese entry below are written; **the L1 completes the settlement** (the
seat record, the claim verdicts, the wave disposition and the final numbers).
Round: 91, plan `plans/round-91.md` (frozen at `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`), base
`9264baaa823cdae3d009a4004e014639551e016f`.
Pre-data controls: `plans/round-91-controls.md`, executed before any candidate score — receipt
`.ufo/waves/round-91/receipts/freeze-gate-r91.txt` (`freeze gate: 4 control(s) held — freeze may
proceed`, exit 0).

## Gate

Candidates considered, with the decision and the reason:

- **S262** — PIT (pitest) documentation, "Basic concepts"
  (`https://pitest.org/quickstart/basic_concepts`). **Admitted** as tier A, scoped to *the
  mutation-testing outcome vocabulary and the notion of an equivalent mutation as the
  mutation-testing tool PIT's own maintainer documentation states them* — not this lane's battery
  mechanics and not a mutation-score formula. Access date 2026-11-05; HTTP 200; 12155 B; page title
  "Basic concepts"; the page's own upstream source file
  `quickstart/basic_concepts.markdown` in `hcoles/pitest-site` (branch `gh-pages`) at revision
  `e8995cd59e3c` carries the same sentences, so the quotes are quote-equal in the file's own bytes
  (markdown lines 59-60, 107 and 109), not only in the rendered page. Located quote (§ Equivalent
  Mutations, HTML lines 122-123, 18 words): "not all mutations will behave differently than the
  unmutated class. These mutants are referred to as equivalent mutations." Second located quote
  (§ Running the tests, HTML line 175, 8 words): "Killed means a test caught the mutation
  successfully." Third (HTML line 177, 11 words): "Survived means the mutation was not detected by
  the covering test." Row written to `corpus/SOURCES.md`; cited by
  `corpus/knowledge/mutation-battery-arms-round91.md`.
  - **Why this row and not Stryker's page (S260) again** — S260 already carries the killed/survived
    vocabulary and the mutation-score formula at tier A. S262 is a *second tool's* maintainer
    documentation and adds two things S260 does not state in that form: the third outcome state
    (`No coverage`, distinct from `Survived`) and the *two named grounds of equivalence* (behaves
    exactly as the original; behaves differently only outside the scope of testing). The second
    ground is what makes the two-sided rule (Q47) well founded, so S262 is admitted and scoped so
    the two rows do not read as duplicates.
- **S263** — Python documentation, `subprocess`
  (`https://docs.python.org/3/library/subprocess.html`). **Admitted** as tier A, scoped to *what
  `subprocess` does when a child does not exit within `timeout` seconds — the `run()` contract
  (child killed and waited for, then `TimeoutExpired` re-raised) against the `Popen.communicate()`
  contract (child not killed)*. The lane's floors guard calls `subprocess.run(..., timeout=cap)`, so
  the `run()` contract is the one that binds it and the `communicate()` sentence is the contrast
  that keeps the row's scope honest. Access date 2026-11-05; HTTP 200; 208648 B; page footer
  "Last updated on Nov 05, 2026 (12:47 UTC)" (HTML line 2037); page title "subprocess — Subprocess
  management — Python 3.15.2 documentation". Located quote (§ `subprocess.run`, HTML lines 289-291,
  25 words): "If the timeout expires, the child process will be killed and waited for. The
  TimeoutExpired exception will be re-raised after the child process has terminated." Contrasting
  quote (§ `subprocess.Popen.communicate`, HTML line 1042, 10 words): "The child process is not
  killed if the timeout expires". Row written to `corpus/SOURCES.md`; cited by
  `corpus/knowledge/timeout-calibration-round91.md`.
- **S264** — Wikipedia, "Mutation testing"
  (`https://en.wikipedia.org/wiki/Mutation_testing`). **Rejected.** Access date 2026-11-05; HTTP
  200; 170845 B; page revision `wgCurRevisionId` 1373580212 ("This page was last edited on 6
  September 2026, at 19:05"). Two independent reasons: it is crowd-editable tertiary text — a lead,
  never support for a tier-A-scoped claim — and its own stated score formula counts equivalent
  mutants in the denominator (located, text line 96, 14 words: "the mutation score is the number of
  mutants killed / total number of mutants"), which is the opposite convention from the two-sided
  rule (Q47) this round's C1 rests on: an equivalent mutant that survives by construction is charged
  as a score defect. Its equivalent-mutant sentence (text line 125, "Such mutants are called
  equivalent mutants") is a usable lead but is uncited at that point and carries no authority over
  the denominator question. **Flip:** re-open as a lead-only row if a future claim needs
  plain-language orientation to the equivalent-mutant notion and no primary source states it
  directly, or if the article is revised so its score formula excludes equivalent mutants from the
  denominator *and* cites a primary source for that exclusion, in which case the score sentence
  becomes quotable as a tertiary summary — never as the authority for the denominator.
- **Jia & Harman survey (the plan's third-choice route for S262)** — opened, reachable
  (`https://mutationtesting.uni.lu/TR-09-06.pdf`, HTTP 200, 434884 B; the publisher routes answer
  403 and 202), **not proposed as a row**: the corpus already screened this exact work out (round-64
  search log, `corpus/SOURCES.md` lines 414-417 — "secondary survey, tier B at best, and it
  duplicates S120's scope"), so re-proposing it would reopen a rejection the corpus has already
  ruled on, and S260 plus S120 already carry the killed/survived/equivalent vocabulary. Left as a
  lead in the scout's receipt only.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **187** before this round (receipt
`.ufo/waves/round-91/receipts/census-before.txt`) and **190** after (three rows appended: S262,
S263, S264 — the plan's Frontier arithmetic of "187 → 189" counted the rejection candidate as prose
outside the registry table, while the seat item places it in the registry as a `rejected` row, so
the measured after-count is one higher; the plan is frozen and is corrected by the L1 at
integration, not here). Validation: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh
validate --file corpus/SOURCES.md --today 2026-11-05` → exit 0, with the same 33 pre-existing W04
duplicate-URL warnings and no E-code once the three new files exist on disk (E11 resolves the
`used-by` paths of S262/S263 and S264 to the corpus files this round creates).

Spot-check result: **pending** — the non-author closure samples one admit and one reject from this
gate.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `landing`: a battery-listed instrument changed without the pinned-blob admission — the round-90 floors bump landed a new blob for `verifiers/check_assertion_floors.py` without the matching `INSTRUMENT_PINS` entry in `verifiers/check_tip_battery.py`, so the tip battery's `instrument-pin` guard has read FAIL since the r90 landing, unobserved until this round's re-measure | `.ufo/waves/round-91/receipts/tipbattery-before.txt` — `FAIL guard instrument-pin: verifiers/check_assertion_floors.py blob c10c0f108f484221d0a7600ac227f10f019f5d4d at 9264baaa823cdae3d009a4004e014639551e016f is not a pinned blob` (the receipt's `guards 4 of 5; tip battery exit 0: 3 of 6`, rc=1) | the Q73 sweep of the r90 plan, which named the floors bump but not its `INSTRUMENT_PINS` consequence — `plans/round-90.md` § Touch list names `verifiers/floors-registry.json` and the `instrument_total` bump, and never the tip battery's pin list | the pin admission lands with ExecFloorsCap (the same change appends the new blob to `INSTRUMENT_PINS` in `verifiers/check_tip_battery.py`, with a pointer comment naming `plans/round-91.md` § C2 leg A(d)), and `plans/round-91.md`'s Q73 sweep names `INSTRUMENT_PINS` explicitly — so the next round's sweep sees the pin list as a swept surface, not an implied one |
| `number-drift`: the frozen plan's § Frontier census expectation (187 → 189) disagreed with its own counting command once the rejection candidate was appended as a registry row (measured 190) | `plans/round-91.md` § Frontier step; `.ufo/waves/round-91/w1/ScribeCorpus/census-after.txt` (rows 190); `.ufo/waves/round-91/w1/SentinelScope/sentinel.md` finding F2 | none — Q19 re-measures before-values; no criterion re-derives a plan's expected after-count from its own counting command before the freeze | `plans/round-91-addendum-1.md` A2 records the measured 190 and the arithmetic; the counting command is unchanged and no row was dropped to match the old expectation |
| `vacuous`: a frozen pre-data control reads MET on the shortcut it names — `ctl-c2-capline-only` (cap raised to 360, no `INSTRUMENT_PINS` admission) prints `C2-PREDICATE-MET`, exit 0; it held at the freeze base only because the base cap (120) sits below its threshold | `.ufo/waves/round-91/w1/CriticClaims.md` § Controls and § Shortcut check; `verifiers/fixtures/round-91/ctl-c2-capline-only.sh` | Q37 exists (real-input shortcut controls must be run before data) and was satisfied in form; it does not require the control to refuse the failing conjunct of its own shortcut | routed to round 92: a committed cap-only shortcut world that asserts the pin, run through the frozen gate; `plans/round-91-addendum-1.md` A5. Not claimed as fixed this round |
| `landing`: attempt 1 dispatched wave `r91-w1` (`r91-w1.ready.dispatched`, 12:06:18) and ended without a landed report; the wave registry was never settled (all 13 rows `agentId: null`, no `r91-w1-results.json`, no WAVE-DONE to the attempt-2 L1) | `.ufo/waves/round-91/w1/swarm-registry.json`; `.ufo/watchdog.log` line `lane-dead-no-report kotoba round=91` (13:34:09) | none — no criterion requires an L1 to record a wave's seat ids before it can end | attempt 2 read the seat outputs from disk and disclosed the missing result record in the report; no second wave was dispatched, because the ready file was taken and a re-dispatch would double-spawn writers |

## Considerthese

`considerthese/2026-10-26.md` was read (proposals only; nothing implemented).

- **No proposal implemented this round.** Both claims are instrument-deepening with frozen
  predicates, so no proposal of this file is inside either claim's scope, and no proposal is
  implemented outside them.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried: it needs a SKILL.md description rewrite, and the 600-line budget cannot absorb one —
  `SKILL.md` is already 600 lines (receipt `.ufo/waves/round-91/receipts/base-skill-size.txt`:
  600 lines / 92,672 B / 165 lines over 120 chars), so a rewrite of the frontmatter description has
  to be paid for by lines saved elsewhere, which is a claim-adjacent edit this round's frozen
  predicates do not admit.
- **Proposals 1, 4 and 5** (a byte/line ceiling; "do not close a round before its falsify wave
  runs"; a per-round evidence budget) are carried unchanged from the previous rounds; proposal 5
  was already mined in round 90 as criterion Q82 and is not re-mined here.

## Sources

- **S262** — PIT (pitest) documentation, "Basic concepts"; URL
  `https://pitest.org/quickstart/basic_concepts`; access 2026-11-05; HTTP 200; 12155 B; located
  quotes at HTML lines 122-123 (18 words), 175 (8 words) and 177 (11 words), all quote-equal in
  the upstream markdown at revision `e8995cd59e3c` (lines 59-60, 107, 109). Tier A scoped. Status
  `mined`; used-by `corpus/knowledge/mutation-battery-arms-round91.md`.
- **S263** — Python documentation, `subprocess`; URL
  `https://docs.python.org/3/library/subprocess.html`; access 2026-11-05; HTTP 200; 208648 B;
  located quote at HTML lines 289-291 (25 words) and the contrast at HTML line 1042 (10 words);
  page footer "Last updated on Nov 05, 2026 (12:47 UTC)". Tier A scoped. Status `mined`; used-by
  `corpus/knowledge/timeout-calibration-round91.md`.
- **S264** — Wikipedia, "Mutation testing"; URL `https://en.wikipedia.org/wiki/Mutation_testing`;
  access 2026-11-05; HTTP 200; 170845 B; page revision 1373580212; located quote at text line 96
  (14 words). Tier C, community, lead only. Status `rejected`; used-by
  `corpus/lessons/round-91.md`.
