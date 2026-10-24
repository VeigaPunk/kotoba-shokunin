# ExecGovProbe — `GOVERNANCE_CORRECTIONS` fail-closed probe (round-65 W1)

Seat: executor, wave kotoba-r65-w1, 2026-10-24. Lane bounds respected: the
lane tree was read-only (no git/jj writes, no edits outside this report); all
fixture worlds and harnesses live under `/tmp/govprobe/`; no subagent dispatch
(this seat holds no dispatch tool).

Assignment: probe the fail-closed shapes of the round-65 C2 recorded-correction
mechanism in `/tmp` fixture worlds by importing
`verifiers/verify_skill_checklist.py`; every named shape must FAIL with its
named class, the honest world must PASS; then demonstrate the do-nothing
control (`corrections=()`) on the live repo, pasting the FAIL lines.

## Attack surface pin

```
$ python3 -c "import sys; sys.path.insert(0,'verifiers'); import verify_skill_checklist as v; ..."
import ok /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py
corrections rows: 3
horizon 2621 2315
Python 3.14.8
```

```
$ sha256sum verifiers/verify_skill_checklist.py
86d8b1584242ccaa096ac9a17e83be28c49e88a21c90bfb7b7ffddfa94bb25f1
$ git show 80bb8921:verifiers/verify_skill_checklist.py | sha256sum
86d8b1584242ccaa096ac9a17e83be28c49e88a21c90bfb7b7ffddfa94bb25f1   # identical
$ git log --oneline 80bb8921..HEAD -- verifiers/verify_skill_checklist.py
(empty — instrument unchanged since the C2 measure commit)
```

**The tree has moved past the round-65 tip.** `git rev-parse HEAD` =
`2a8eba56b3f9321b70c569fa2816d42237ca49a2` (round-66 commits landed:
`0e104f4` frontier, then `4119647…9e75e73`, `2a8eba5`). The probed instrument
bytes are nevertheless **byte-identical to the C2 measure rev `80bb8921`**, so
the attack surface is exactly the landed C2 implementation; only the governance
data advanced (see §Rev sweep). Governance-file lengths at probe time:
`LOG.md` 2633 lines, `SCORECARD.md` 387 lines.

Mechanism under probe: `correction_problems()` (verifier lines 1699–1734) and
`check_governance_citations(..., corrections=…, corrections_horizon=…)`
(1737–1806). Row shape `(log line, line sha256, subject file, subject line,
stale token, corrected token)`; validation order is horizon → byte pin →
wording (both tokens on the line) → subject liveness → stale-still-red →
corrected-resolves. Errata rows are applied and their subjects removed **before**
corrections validate.

## Method

Harness `/tmp/govprobe/probe_corrections.py` (scratch, not committed) imports
the verifier and builds a fresh `tempfile.TemporaryDirectory` per case:

```
repo/LOG.md        line 1 `corpus/live.md`; line 2 = the appended notice
repo/SCORECARD.md  8 padding lines; line 9 `corpus/gone.md` (the stale cell)
repo/corpus/live.md exists; corpus/gone.md absent
```

Each case is run three ways where applicable: (a) unregistered
(`corrections=()`), proving the world is red before the mechanism; (b) the
mutated row; (c) the honest row. Every assertion checks status, the exact
class string, the residual-red reporting, and (for honest worlds) that the
`N recorded correction(s) excused` counter moves. Case count 23, mismatches 0,
exit 0. A second harness (`at_rev.py`, `horizon_forward.py`) re-runs the live
rows over governance bytes checked out from a given rev into a `/tmp` mirror
world (lane-root and parent tops symlinked read-only).

## Named fail-closed shapes — all FAIL with their class

```
shape past-horizon: FAILs closed                           ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md' is past horizon 1 or absent; SCORECARD.md:9: 'corpus/gone.md' does not resolve from /tmp/govprobe-shape-jk0tnqaa; ... 0 recorded correction(s) excused
shape absent-notice-line: FAILs closed                     ok
    FAIL evaluated=2 :: correction LOG.md:5 SCORECARD.md:9 'corpus/gone.md' is past horizon 2 or absent; ...
shape line-drift: FAILs closed                             ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md': line text drifted; ...
shape wording: FAILs closed                                ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md': correction wording not on the line; ...
shape no-live-subject: FAILs closed                        ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:8 'corpus/gone.md': names no live red subject; ...
shape no-live-subject(quoted token): FAILs closed          ok
    FAIL evaluated=2 :: correction LOG.md:2 LOG.md:3 'corpus/gone.md': names no live red subject; ...
shape corrected-dead (dead token on the notice line): FAILs closed ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md': corrected token 'corpus/absent-xyz.md' does not resolve; ...
shape stale-restored: FAILs closed                         ok
    FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md': stale, the old token now resolves; ...
shape never-masks (second dead subject exposed)            ok
    FAIL evaluated=2 :: LOG.md:3: 'corpus/other-dead.md' does not resolve from /tmp/govprobe-mask-t405l4qs; ... 1 recorded correction(s) excused
```

Shape-by-shape attribution (all measured, exit code of the case = 0 when the
classification matched):

| Required class | Trigger used | Class string observed |
|---|---|---|
| past-horizon | row line 2, horizon 1 (and row line 5 over a 4-line LOG) | `is past horizon 1 or absent` |
| line-drift | pin `"0"*64` | `: line text drifted` |
| wording | corrected token `corpus/x.md` absent from the notice | `: correction wording not on the line` |
| no-live-subject | row names SCORECARD line 8 (padding) | `: names no live red subject` |
| corrected-dead | `corpus/absent-xyz.md` **on the notice line** | `corrected token 'corpus/absent-xyz.md' does not resolve` |
| stale-restored | `corpus/gone.md` created in the world | `stale, the old token now resolves` |
| never-masks | an extra unquoted `corpus/other-dead.md` on LOG line 3 | `LOG.md:3: 'corpus/other-dead.md' does not resolve` **+** `1 recorded correction(s) excused` |

Two extra fail-closed interactions, measured:

```
double-excusal: FAIL evaluated=2 :: correction LOG.md:3 LOG.md:2 'corpus/gone.md': names no live red subject; ... 1 recorded absence(s) excused, 0 recorded correction(s) excused
shape double-excusal(status first): correction fails closed ok
cross-mask: FAIL evaluated=3 :: erratum LOG.md:2 'corpus/gone.md': line text drifted; LOG.md:2: 'corpus/gone.md' does not resolve from /tmp/govprobe-crossmask-vo9zxl4m; ... 1 recorded correction(s) excused
shape cross-mask: broken errata still fails beside a valid correction ok
```

- Double registration (a correction for a subject the errata already excused) is
  **rejected**, because errata filtering precedes correction liveness: the
  subject is no longer live. One cell cannot be excused twice.
- A drifted errata row keeps its own failure while an unrelated valid correction
  is still excused (`1 recorded correction(s) excused`); neither mechanism
  papers over the other's broken row.

## Honest worlds PASS

Fresh worlds, SCORECARD-owned and LOG-owned stale cells, each red when
unregistered and green when the row is registered:

```
control SCORECARD.md: unregistered world is RED            ok
    FAIL evaluated=2 :: SCORECARD.md:9: 'corpus/gone.md' does not resolve from /tmp/govprobe-honest-xr_8h4ol; ... 0 recorded correction(s) excused
honest SCORECARD.md: pinned correction PASSes              ok
    PASS evaluated=1 :: 1 governance citation token(s) resolve across 2 files; ... 1 recorded correction(s) excused
control LOG.md: unregistered world is RED                  ok
    FAIL evaluated=3 :: LOG.md:10: 'corpus/gone.md' does not resolve from /tmp/govprobe-honest-lns186ue; ... 0 recorded correction(s) excused
honest LOG.md: pinned correction PASSes                    ok
    PASS evaluated=2 :: 2 governance citation token(s) resolve across 2 files; ... 1 recorded correction(s) excused
```

The `0 recorded correction(s) excused` → `1 recorded correction(s) excused`
counter movement is what makes the PASS attributable to the row, not to a
permissive fixture.

## Do-nothing control — live repo, `corrections=()`

```
=== do-nothing control: live repo, corrections=() ===
status=FAIL evaluated=1209
detail: LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin;
        LOG.md:2580: '.ufo/watchdog.log' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin;
        SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin;
        10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 0 recorded correction(s) excused
control live: corrections=() is RED on exactly the three cells ok
    status=FAIL evaluated=1209 red_cells=3
```

Exactly three red cells — the count is sound because the detail truncates only
above four reds (`bad[:4]` plus `(+N more)`), so a fourth red would have been
printed as a fourth cell and a fifth as `(+1 more)`; either would have broken my
`red_cells == 3` assertion. The pre-existing errata absence-excusal still holds
in the same run (`1 recorded absence(s) excused`), matching the regression
requirement.

With the landed rows:

```
status=PASS evaluated=1206
detail: 1206 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s),
        3 schematic token(s) excluded, 1 recorded absence(s) excused, 3 recorded correction(s) excused
live: landed corrections PASS with 3 excused               ok
    status=PASS evaluated=1206 (do-nothing 1209 minus 3)
```

The wired CLI path (not only the imported function) prints the same numbers:

```
$ python3 -B verifiers/verify_skill_checklist.py --json --check governance.citation_resolves
{
  "checks": [
    {
      "detail": "1206 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused, 3 recorded correction(s) excused",
      "evaluated": 1206,
      "id": "governance.citation_resolves",
      "status": "PASS"
    }
  ],
  "exit_code": 0, "fail": 0, "na": 0, "pass": 1
}
exit=0
```

A corrupted row on the **real** governance bytes fails closed:

```
status=FAIL evaluated=1207
detail: correction LOG.md:2621 SCORECARD.md:158 '.ufo/reports/round-60/kotoba.md': line text drifted;
        SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve from /home/vgpnk/Projects/shokunin/kotoba-shokunin; ...
live: drifted row fails closed on real governance bytes    ok
```

The three pinned notice lines themselves re-hash clean at HEAD:

```
line 2619 pinned=b11e4e8be95834db actual=b11e4e8be95834db match=True
line 2620 pinned=1dcb9d9e62066089 actual=1dcb9d9e62066089 match=True
line 2621 pinned=6836c34a99a4db12 actual=6836c34a99a4db12 match=True
subject lines at HEAD: LOG.md:2533 / LOG.md:2580 / SCORECARD.md:158 still carry the stale tokens
```

## Mirror-world tamper arms on the live governance bytes

`/tmp` world whose `LOG.md`/`SCORECARD.md` are **copies** of HEAD's files, all
other trees symlinked read-only, parent-level `../` targets shadowed:

```
copy/base: status=FAIL evaluated=1209          # reproduces the live do-nothing red
copy:      status=PASS evaluated=1206          # 3 excused; base minus 3
copy/token-moved: FAIL -> correction LOG.md:2621 SCORECARD.md:158 ...: names no live red subject
copy/restored:    FAIL -> correction LOG.md:2620 LOG.md:2580 '.ufo/watchdog.log': stale, the old token now resolves
```

Tampering the *subject* cell (token renamed on SCORECARD:158) or restoring the
stale path makes the corresponding row fail with the same class as its synthetic
twin — the live rows are not weaker than the fixture rows.

## Rev sweep — the receipt's number reproduces at its own rev

`python3 -B /tmp/govprobe/at_rev.py <rev>` checks out the two governance files
from `<rev>` into a mirror world and runs the check twice:

| rev | LOG.md lines | SCORECARD.md lines | base eval `corrections=()` | with rows | state |
|---|---|---|---|---|---|
| `80bb8921` (C2 measure) | 2622 | 379 | **1196** | **1193**, 3 excused | FAIL → PASS |
| `0e104f49` (round-65 tip) | 2622 | 381 | 1200 | 1197, 3 excused | FAIL → PASS |
| `2a8eba56` (HEAD) | 2633 | 387 | 1209 | 1206, 3 excused | FAIL → PASS |

`80bb8921` reproduces the receipt exactly: 1193 evaluated + 3 excused = the
1196 base, with the same three red cells named. The 1193 → 1197 → 1206 drift is
entirely governance-data growth after the measure (round-65 frontier SCORECARD
annotations, round-66 appends: `git diff 80bb8921 HEAD -- LOG.md SCORECARD.md`
= 11 inserted LOG lines, 10 inserted / 1 replaced SCORECARD lines) — [INFERENCE]
each added subject comes from those appended lines; the aggregate delta of +13
subjects is measured directly. The three pinned rows bite at every rev and are
never re-pinned.

## Forward falsifier — the horizon is a frozen ceiling

The mechanism's bound is the constant `GOVERNANCE_CORRECTIONS_HORIZON = 2621`,
which equals the last landed notice line. HEAD's `LOG.md` is already 2633 lines,
so a **new** correction appended today is rejected until the constant is bumped:

```
HEAD LOG.md lines: 2633 corrections horizon: 2621
new row @ line 2634, frozen horizon: status=FAIL evaluated=1207
   detail: correction LOG.md:2634 SCORECARD.md:388 'corpus/round66-absent-report.md' is past horizon 2621 or absent;
           SCORECARD.md:388: 'corpus/round66-absent-report.md' does not resolve ...; 3 recorded correction(s) excused
new row @ line 2634, horizon bumped: status=PASS evaluated=1206
   detail: ... 4 recorded correction(s) excused
```

Direction is fail-closed (the new cell stays red, the three old rows still work),
so no false green; but the "append-only recorded correction" workflow is a
one-shot until round 66+ bumps the constant in step with the new notice line.

## Calibration finding — the suite's `corrected-dead` arm is not isolating

The only self-test arm for the corrected-token-dead class is at verifier line
2475: `("corrected token dead", (crow[:5] + ("corpus/absent-xyz.md",),), 2,
"does not resolve")`, where `crow`'s notice text contains `corpus/live.md`, not
the dead token. The wording branch therefore fires first, and the arm's
`"does not resolve"` needle is satisfied by the residual subject red, not by the
resolve branch. Replicated byte-for-byte:

```
self-test-arm replica: FAIL evaluated=2 :: correction LOG.md:2 SCORECARD.md:9 'corpus/gone.md':
    correction wording not on the line; SCORECARD.md:9: 'corpus/gone.md' does not resolve ...; 0 recorded correction(s) excused
self-test arm replica: off-line dead token hits the wording branch ok
    branch hit = wording; resolve branch silent
```

`grep -n "absent-xyz"` confirms this is the only such arm. So
`correction_problems` line 1729 (`elif not citation_resolve(corrected, repo)`)
has **no isolating assertion** in the 1862-assertion suite: a regression that
deleted only that branch would keep the suite green. The isolated arm in §Named
shapes (dead token *on* the notice line, `forbid=["wording"]`) is what actually
pins the class. Advisory fix for the C2 owner: move the dead token onto the
notice line in the existing arm (or add the isolated row), keeping the same
needle. This is a calibration gap in the *witness*, not a live false green —
the live rows' corrected tokens resolve and the row set is otherwise exercised.

## Claims supported / falsified

- **Supports C2** (plan §Claim C2): every listed fail-closed shape —
  corrected-token-does-not-resolve, correction-names-no-subject,
  named-cell-not-red, drifted notice text, never-red subject, and the
  `GOVERNANCE_ERRATA` regression — fails with its named class; the honest world
  passes; and the wired check prints PASS at 1206 evaluated / 3 excused, exit 0
  (the 11/11 full-checklist number is the C2 receipt's; this seat ran the one
  check).
- **Supports the C2 do-nothing control** (plan §Claim C2, §9): with
  `corrections=()` the live check FAILs on exactly the three original cells
  (`LOG.md:2533`, `LOG.md:2580`, `SCORECARD.md:158`), evaluated 1209, while the
  three appended notices — which exist in the same files — change nothing on
  their own.
- **Supports the C2 receipt's counted predicate at its rev**: 1193 reproduced at
  `80bb8921` (base 1196, 3 excused).
- **Falsifies** the implicit reading that the 1193 count is a property of the
  mechanism at HEAD: the same mechanism reports 1206 at `2a8eba5` because
  governance data grew +13 subjects after the receipt. The rev-pinned number is
  correct; a HEAD re-measure must state the rev.
- **Narrows** the suite's `corrected-dead` arm: it does not exercise the
  corrected-resolve branch (calibration finding above).

## Risks / gaps

1. **Horizon is a frozen ceiling** (measured, §Forward): reuse needs a
   bump-in-step; the round-66 appends already sit 12 lines above it. Fail-closed.
2. **`corrected-dead` branch unisolated in the suite** (measured): a
   branch-deletion regression is not caught by the 1862 assertions.
3. **Truncated reporting**: `check_governance_citations` prints at most four
   red cells (`(+N more)`); my "exactly three" claims are safe only because a
   fourth would have been shown. A future run with ≥5 reds cannot be counted
   from the detail string alone — an assertion-count gap, not a mechanism bug.
4. **Quoted-token subjects cannot be corrected** (measured): a correction naming
   a token that only appears inside same-line double quotes fails
   `names no live red subject`. That is the intended exclusion (meta-findings
   are not live promises), but it means a mistakenly-quoted live cell must be
   fixed by appending an unquoted restatement, not by a correction row.
5. Not probed here (out of seat scope): the full `--self-test` re-run, the
   checklist floor 1852→1862 registration, and whether any other round-66
   governance appends need corrections — the do-nothing run shows none
   (exactly 3 reds at HEAD).
6. [INFERENCE] The `..`-hop convention (`citation_resolve` ≤3 hops, no interior
   `..`) is what makes the live corrected tokens resolve against the *fleet*
   root rather than the lane; I verified the resolution outcome, not the fleet
   root's contents.

## Tooling

No installs or upgrades this seat (python3 3.14.8, git, sha256sum, coreutils
were sufficient; pacman pause not needed). Scratch artifacts under
`/tmp/govprobe/` (`probe_corrections.py`, `probe.out`, `at_rev.py`,
`horizon_forward.py`) are uncommitted by design; the lane tree was not modified.
