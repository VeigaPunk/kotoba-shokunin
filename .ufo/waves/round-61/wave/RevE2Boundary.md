# RevE2Boundary — C1/E2 boundary audit (round 61, attempt 1)

Seat: `kotoba-r61-wave-RevE2Boundary` (reviewer, judged on calibration).
Scope: verify the round-61 C1 claim is the provenance-authenticating counter
redesign (v3) measured on worlds + fixtures — **not** a re-measurement that
would retroactively convert round-60 C1's exploratory verdict (erratum E2,
`49f7ff22`). Read-only audit of committed bytes at tip `7827628a` (plan-freeze
commit; base `f3246d14`); no lane, fleet, sibling, `.ufo/state`, or index file
written; no git/jj mutation; no dispatch.

## Verdict

**BOUNDARY HOLDS — no blurring wording found in the frozen plan, the wave
spec, or the committed ground.** The round-61 C1 is a new claim about a new
artifact (counter v3, arms A1–A4, worlds W1–W7 + fixtures) under a new frozen
predicate sentence that the committed v2 counter cannot even print. The
exploratory status of round-60 C1 is recorded as irrevocable in the plan
document itself and in the closure ruling; nothing in round 61 proposes to
re-grade it. One LOW clarity-residue filed (§3) for integration wording.

## 1. The plan text that keeps the boundary (quoted, `plans/round-61.md` @ `7827628a`)

**New artifact, new claim — "redesigned (v3)", not a re-run of v2:**

> Line 21: `### C1 — depth (measured): provenance-authenticating counter v3`
>
> Lines 23–24: `The scoped-rules counter is redesigned (v3) with four frozen
> arms, and the seven r60-recorded attack worlds reject under it while the four
> eligible r60 rows still pass live.`

The r60 material enters only as *instrumentation*: "r60-recorded attack
worlds" are regression fixtures rebuilt from committed r60 receipts, and the
"four eligible r60 rows" are the regression pass-set — both feeding v3's
self-test, none re-adjudicating the r60 claim.

**The measured surface is worlds + fixtures, and the predicate is a new
sentence:**

> Lines 50–54: `C1 predicate (same sentence in plan, counter label, receipt):`
> ``python3 -B verifiers/check_scoped_rules.py --self-test`` prints
> `worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
> ``python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch`` exits 0
> while the same command at base `f3246d14` exits 1.

Confirmed mechanically: the committed v2 counter
(`verifiers/check_scoped_rules.py` @ tip, sha256 `ca2585a4…` per
`controls-v2/SUMMARY.md:3`) has no `worlds reject` output path — its only
self-test print is `self-test: %d failure(s) over %d assertions`
(line 2487). The required output string exists nowhere in the frozen v2
source, so the predicate is unsatisfiable by re-measuring v2; it *requires*
the v3 redesign. The r60 predicate was the different sentence
`C1 predicate: --fetch exit 0 (F>=TARGET)` (`controls-v2/SUMMARY.md:4`,
fleet `.ufo/reports/round-60/kotoba.md:33`).

**The claim is gated as the redesign the closure pre-authorized:**

> Line 16 (routed defect g): `no measured C1 successor until the
> provenance-authenticating counter redesign (semantic key/action arms
> rejecting `sessions`-class keys).`

> Lines 57–59: `the L1 integrates, hardens against in-wave attack designs,
> freezes the counter sha at integration, runs the 7 committed fixtures
> (receipts committed before any `--fetch` data measurement, M90), then
> measures. Kill rule: any world exits 0 under `--self-test`, or any eligible
> row fails at tip, or base does not exit 1 → C1 fails.`

The kill rule binds only the round-61 claim; it names no consequence for the
r60 verdict, which is correct — that verdict is already ruled.

## 2. The r60 verdict is irrevocable on the record

- `plans/round-60.md:155-168` (erratum E2, committed `49f7ff22`, ancestor of
  tip — verified `git merge-base --is-ancestor`, exit 0): "So C1 is
  **exploratory** from this commit on, before any C1 data is integrated… It
  verifies only as `unprovable-but-better` with a named non-author reviewer;
  otherwise it lands `unprovable`. Counter v2 output is reported as
  supporting evidence, never as the claim's verdict; the counter, target and
  predicate stay unchanged."
- `corpus/lessons/round-60-verifier-spotcheck.md:60-83`: the named
  non-author reviewer ruled **`unprovable-but-better`**. §8 routes "a
  provenance-authenticating counter redesign … **before any measured
  successor to exploratory C1**" — i.e. the closure itself frames round-61
  C1 as a *successor*, explicitly conditional on the redesign, not a
  conversion.
- `SCORECARD.md:28` (depth row): "declared EXPLORATORY before data, erratum
  E2; score held 9; the row carries the verdict and reviewer pointer".
  `SCORECARD.md:156` records "C1 depth — scoped rule files by client —
  declared EXPLORATORY before data (erratum E2, `49f7ff22`; two v2 control
  worlds met the frozen predicate by forged provenance…)" and :158 names
  the same conditional: the redesign "if a measured successor to
  exploratory C1 is attempted".
- Fleet `.ufo/reports/round-60/kotoba.md:31,37`: "counter output is
  supporting evidence, never the verdict"; "Verdict: exploratory →
  `unprovable` as of this report (a named non-author reviewer … must still
  rule)". That report is append-only history; nothing in round 61 edits it.

Ancestry check (read-only): r60 tip `79cf2638` is an ancestor of base
`f3246d14` (exit 0), so the r60 data state is fully inside round-61's base;
the two forged-provenance worlds are historical fact, not re-tried here.

## 3. Findings

### LOW — L1 — residual wording risk at integration, not in the frozen plan

No wording in `plans/round-61.md`, `wave-spec.json`, or `wave-dispatch.json`
converts, re-grades, or re-measures the r60 verdict (grep for
`successor|convert|upgrade|re-grade|re-measur|retroactiv|verdict` over the
plan returns only the line-16 "no measured C1 successor until the redesign"
clause). Two phrasings a reader could over-parse, both already benign in
context, plus the receipt-name collision — file them so the integrated
report keeps them disambiguated:

1. Plan lines 23–24 "the seven r60-recorded attack worlds reject under it"
   and "the four eligible r60 rows still pass **live**" — "under it" =
   under v3; "live" modifies the v3 `--fetch` run at tip, not a fresh
   verdict on r60 rows. The r61 report/entry should carry the same
   qualifier ("under v3") so no reader maps "4 of 4 live" back onto the
   r60 exploratory claim.
2. Predicate conjunct "the same command at base `f3246d14` exits 1" — true
   only under the **v3** counter measured at base (v3's pinned artifacts —
   the A1 canonical key set grounded in S112–S115 "opened this round" —
   are absent at `f3246d14`, so rows fail → exit 1). Under committed v2,
   base `f3246d14` already contains the r60 data (`7b80ae80` is an
   ancestor) and `--fetch` would exit **0**. The receipt
   (`ExecReceiptsDesign` template) must echo the frozen sentence verbatim
   with the v3 counter sha256 on it — exactly as designed — otherwise a
   reader running v2 at base could "refute" the conjunct.
3. Receipt-name collision: `.ufo/waves/round-61/C1-measure.txt` (planned)
   vs `.ufo/waves/round-60/C1-measure.txt` (committed). Same basename,
   different artifact. The r61 file must lead with the v3 sha + the new
   predicate sentence so it cannot be misread as a re-measure of the r60
   claim (also feeds R-c disambiguation — `check_routed_repairs.py` R-c
   requires the LOG line to name both r60 files precisely).

### NONE — no HIGH or MED finding

Nothing in scope proposes editing the r60 SCORECARD row, the r60 report,
the E2 erratum, or the `unprovable-but-better` ruling; the SCORECARD
discipline assigned to `ScribeLogScore` is append-only ("score held,
verdict + reviewer pointer pending closure"), matching r60 convention.
`ScribeShonen.md` (uncommitted wave draft, wave/ScribeShonen.md:29) already
uses the correct successor framing: "count the round-61 C1 v3 result as a
measured successor to exploratory round 60 **only if the closure upholds
the frozen predicate**". `ScribeEntryV3`'s assigned shape (wave-spec)
carries the honest residue: a worlds table with the "v2 result" column
and the declared A4 limit ("committed-bytes provenance consistency, not
wall-clock authentication"), so the entry itself discloses what v3 does
and does not prove.

## 4. Residual risk

- **Successor-admission risk (owned by the r61 closure, not this wave):**
  whether a measured v3 pass can support a depth score move is the
  non-author closure's call. The boundary this seat certifies is narrower:
  the *claim* is a new measurement of a new counter, and the r60 verdict
  stands untouched whatever the outcome. `CriticC1Scope` independently
  argues the "stealth successor" reading; no contradiction between that
  framing and this audit — the redesign clause in routed defect (g) and
  closure §8 makes a measured successor *legitimate*, provided the report
  never re-labels the r60 claim "measured".
- **A4 declared limit:** the plan discloses v3 cannot authenticate
  wall-clock fetch time against author-forged commit dates (lines 37–39) —
  the exact gap that made W1 forgeable in spirit. The limit is declared
  before data; honest, but it means W1-class forgery at the *commit-date*
  level remains unmeasurable. The report must repeat the limit, not just
  the 7/7 count.
- **Fixture provenance:** the 7/7 claim rests on fixtures rebuilt from r60
  receipts by in-wave seats (`ExecWorldFixtures`, `MutWorldW1`,
  `MutWorldW24`, `ScoutFixtureBytes`). If a rebuilt world diverges from the
  recorded r60 bytes, the "reject" is about the fixture, not the forgery
  class — the divergence itself would be a finding against the
  instrumentation, covered by those seats' world-instrumentation receipts.

## 5. Verification gaps (named, honest)

- `ScribeEntryV3`/`ScribeLogScore`/`ScribeSkillReg` drafts were not yet on
  disk at audit time except `ScribeShonen.md`/`ScribeSkillReg.md`/`ScribeC3.md`
  (uncommitted `??` in `git status`); only the spec-mandated shapes and the
  committed plan could be audited. Any wording defect they introduce lands
  post-audit and belongs to the residual call.
- The v3 counter does not exist yet; the "new predicate sentence"
  argument is grounded in the v2 source's absence of the required output
  string (verified) plus the plan's freeze discipline, not in a v3 read.
- Fleet report read at
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-60/kotoba.md` — the
  lane's `.ufo/reports/` holds no round-60 file (reports live in the fleet
  repo); verified there, not in-lane.

## Evidence index (all committed bytes, read-only)

| item | pointer | observation |
|---|---|---|
| r61 plan | `plans/round-61.md` @ `7827628a` | lines 16, 21–24, 26–48, 50–59 quoted above |
| E2 erratum | `plans/round-60.md:155–168` @ `49f7ff22` | exploratory before data; counter output never the verdict |
| v2 controls | `.ufo/waves/round-60/controls-v2/SUMMARY.md` | W1/W2 MET v2 predicate by forged provenance (:12,:14); E2 named (:17–19) |
| closure ruling | `corpus/lessons/round-60-verifier-spotcheck.md` | §3 `unprovable-but-better`; §8 successor-conditional clause |
| v2 counter | `verifiers/check_scoped_rules.py` | no `worlds reject` path; self-test prints only `self-test: %d failure(s)` (:2487) |
| C2 checker | `verifiers/check_routed_repairs.py` | six r60 record-keeping repairs; none re-grades E2 |
| base control | `.ufo/waves/round-61/controls/C2-base.txt` | `routed repairs verified 0 of 6`, `base-exit=1` (matches committed run) |
| SCORECARD | `SCORECARD.md:28,156,158` | E2 verdict + reviewer pointer on depth row; successor phrasing |
| fleet report | `fleet .ufo/reports/round-60/kotoba.md:7,31,37` | supporting-evidence-only wording; `unprovable` pending judge |
| ancestry | `git merge-base --is-ancestor` | `79cf2638`→`f3246d14` exit 0; `49f7ff22`→tip exit 0 |
| wave spec | `.ufo/waves/round-61/wave-spec.json` | seat shapes keep boundary; no conversion wording |

Installs: none (no installs; pacman paused per ruling — none needed).
Blockers: none.
Attacked: the C1/E2 boundary — audited whether round-61's C1 is the v3
redesign measured on worlds+fixtures (it is) or a re-measurement that would
retroactively convert E2's exploratory verdict (no wording does that; one
LOW clarity-residue filed for integration receipts).
