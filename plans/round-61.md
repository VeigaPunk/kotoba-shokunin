# kotoba round 61 — plan (attempt 1, hyaku run 5)

Date: 2026-10-23. L1: agent KotobaR61 (the canonical §3 planner seat; no swarm planner role).
Base: `f3246d1493b60ea1c0d947a19c39f9e08e92f326` (lane branch tip; `jj-lane.sh state` clean, ahead 0).
Round driver: `.ufo/prompts/kotoba-round-61.md` (attempt 1; no inherited dead-attempt state — watchdog shows a single launch line).

## Why this round (motivation, one line each)

The r60 closure (`corpus/lessons/round-60-verifier-spotcheck.md` §7–§8) routed seven defects:
(a) report claimed "32 reports, 0 dead"; 29 committed — correct the count;
(b) `plans/round-60.md` (+189) and `considerthese/2026-10-23.md` (+39) omitted from the r60 report landed scope — name them;
(c) the r60 base measurement lives in `receipts/freeze2-selftest.txt`, not `C1-measure.txt` as the joint citation implied — name pointers precisely;
(d) no standalone committed census-after file — commit one this round;
(e) the report word "byte-exact" overstates the documented S106 `&#124;` escape / S107 whitespace shaping — reserve the word;
(f) M90 control gap — receipts before probing, controls complete before data seats;
(g) no measured C1 successor until the provenance-authenticating counter redesign (semantic key/action arms rejecting `sessions`-class keys).
Lowest owned non-retired axis: **depth 9** (consistency 10). r59 R1–R4 all landed (r60 closure §5) — build on that base.

## Claims (3, distinct axes, causally separable)

### C1 — depth (measured): provenance-authenticating counter v3

The scoped-rules counter is redesigned (v3) with four frozen arms, and the seven r60-recorded
attack worlds reject under it while the four eligible r60 rows still pass live.

Frozen arm spec (classes fixed here; implementation rides the wave):
- **A1 semantic scope-key** — a row's Scope key must be in the canonical per-client key set
  grounded in S112–S115 (opened this round), and must bind a path-like value on the cited line.
  Rejects W5 (`sessions`-class / ExecKeyForms extra keys: `patterns`, `claudeMdExcludes`).
- **A2 semantic action** — every load/event claim in the Action cell must be supported by text
  on the committed snapshot page (not vocabulary matching alone). Rejects W6 (invented action).
- **A3 URL canonical** — a re-open row's URL must be byte-identical to its base row's URL.
  Rejects W2 (locale/enterprise alias renderings with real content).
- **A4 snapshot provenance** — the row's recorded sha256 must equal the committed snapshot
  bytes, the located quote must occur verbatim in them, and the earliest commit introducing
  those bytes must be no older than the row's recorded open date (rejects recycled bytes:
  W1, round-53 scratch under a fresh-fetch claim). Limit, declared before data: the arm
  authenticates internal provenance consistency of committed bytes; it cannot authenticate
  wall-clock fetch time against author-forged commit dates.

Frozen worlds (each rebuilt as a committed fixture from the r60 receipts; W0 do-nothing extra):
W1 `CtlReopenForged d` · W2 `CtlReopenHeldKey b` · W3 `CtlReopenHeldKey a` ·
W4 `CtlReopenHeldKey c` · W5 wrong scope-key (ExecKeyForms) · W6 invented action ·
W7 v1-hollow rescore world (regression). Ground: `.ufo/waves/round-60/controls-v2/SUMMARY.md`,
`.ufo/waves/round-60/build/ExecKeyForms.md`, `.ufo/waves/round-60/controls/SUMMARY.md`.
Before (committed, r60): W1 and W2 **met** the v2 predicate (`--fetch` exit 0); W5/W6 pass
as real rows (ExecKeyForms: "the frozen counter backs a row end-to-end (exit 0, 4 of 4 live)
with one of them as the Scope key").

**C1 predicate (same sentence in plan, counter label, receipt):**
`python3 -B verifiers/check_scoped_rules.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
`python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0 while the same
command at base `f3246d14` exits 1.
Counter-writing: 2 wave executor seats draft v3 source + fixtures + self-test arms from this
spec against the committed v2 source; the L1 integrates, hardens against in-wave attack
designs, freezes the counter sha at integration, runs the 7 committed fixtures (receipts
committed before any `--fetch` data measurement, M90), then measures. Kill rule: any world
exits 0 under `--self-test`, or any eligible row fails at tip, or base does not exit 1 → C1 fails.

### C2 — calibration (measured): the six routed record-keeping repairs, guarded

Every r60-closure routed repair (a)–(f) lands with a committed receipt, counted by
`python3 -B verifiers/check_routed_repairs.py --rev <rev>` → `routed repairs verified 6 of 6`
exit 0 (at base `f3246d14`: `0 of 6`, exit 1 — control receipt committed before any repair).
The six repairs as frozen in the checker: R-a LOG.md carries the corrected build-report count
(claimed 32 vs committed 29) with its counting command; R-b LOG.md round-61 landed-scope
names `plans/round-60.md` and `considerthese/2026-10-23.md`; R-c LOG.md erratum names the r60
base-measurement pointer precisely (`receipts/freeze2-selftest.txt` vs `C1-measure.txt`);
R-d `.ufo/waves/round-61/census-after.txt` exists ending exit=0; R-e `corpus/QUALITY.md` gains
criterion Q56 reserving "byte-exact" for literal equality and `corpus/lessons/round-61.md`
mines it as a mistake; R-f `.ufo/waves/round-61/receipts/controls-ancestry.txt` records
`git merge-base --is-ancestor` showing the control-receipts commit precedes the C1 data
commit. Do-nothing control: a world with no repairs (base) scores 0 of 6.

### C3 — adjacency (measured): kama writing-revision calibration imported

Sibling admission offered by the orchestrator (session note 6): kama's
`corpus/knowledge/self-assessment-at-writing.md` is opened this round and admitted as
SOURCES row S117; a knowledge entry `corpus/knowledge/writing-revision-calibration-round61.md`
cites it; the corpus README index gains a row. Counting command:
`grep -c 'self-assessment-at-writing' corpus/SOURCES.md` 0 → 1, plus `test -f` on the entry
and its `README.md` row. Tier honesty: sibling-lane artifact, tier B for the scope
"writing-revision calibration for prompt-craft self-assessment", kind `own-work` (sibling
repo path), never sole support for a claim outside that scope.

## Frontier step (inside the claim cap)

- Census before: `.ufo/waves/round-61/census-before.txt` (exit 0, 13 W04) — committed with this plan.
- Census after: `.ufo/waves/round-61/census-after.txt` — committed at integration.
- Mined mistake: M91 (the "32 reports, 0 dead" overstatement and the pointer sloppiness it rode
  with) → `corpus/lessons/round-61.md` `## Mistakes`; the fix (R-a/R-c receipts + Q56) is shown
  able to fail: the checker exits 1 at base.
- Sourced claim: C1 rests on S112–S115 opened this round; C3 rests on S117.

## Wave shape (one v2 wave, 64–96 seats, ≥25% attack; session note 5)

`kotoba-r61-wave` under policy v2. Build seats draft/verify against committed bytes and return
reports + full draft texts (the L1 is the only integrator; seats never write the lane).
Attack seats attack the frozen predicate, the r60 evidentiary ground, the routed-repair
wording, and the C3 bleed boundary; control seats rebuild the seven worlds and re-score the
committed v2 counter (world-instrumentation receipts). After integration a residual call
(≤8 reviewer/critic seats) attacks the landed bytes; counted in the round total.

Tooling authorization (operator 2026-10-19) stands for every seat; pacman is PAUSED
host-wide — install via `uv tool`/`npx`/official binaries only, record any install.

## Erratum E1 — C3 withdrawn as a counted claim before data (2026-10-23, pre-data)

`CriticC3Axis` exhibited a static counterexample to the frozen C3 counter: a tree that keeps
the S117 row and its index row while replacing the entry with scope-absorbing unsupported
claims preserves every named counting observable (`grep -c` 0→1, `test -f`, README row).
The counter therefore cannot measure the axis property (AXES.md adjacency = reported, not
absorbed), and rule 9 bars a target a hollow control can reach. Per the r56–r58 pre-data
withdrawal precedent, **C3 is withdrawn as a counted claim before any C3 data entered the
lane**; the frozen predicate is retired unmeasured. The curation itself continues as
frontier-step work (SOURCES row S117, the knowledge entry, the README row, the lesson Gate)
and is reported under Sources & frontier, not as a claim. The class is mined as M92
(a presence counter cannot back an adjacency claim) into `corpus/lessons/round-61.md`.
Round claims are now C1 (depth) and C2 (calibration). The sourced-claim rule is still met
by C1's S112–S115.

## Commit order

This plan + checker + C2 base control + census-before (freeze commit) → wave evidence →
integration commits (counter v3, fixtures, receipts, entry, rows, lesson, LOG, SCORECARD,
registry/index) → report → fleet report. Lane commits only via `scripts/hyaku/jj-lane.sh`.
