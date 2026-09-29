# Checklist execution, round 15 — pre-registration (written before landing)

**Lane:** kotoba-shokunin. **Round:** 15. **Axis move:** `operability` (7.5, the
lowest row in `SCORECARD.md`, tied with `calibration` and `adjacency` at 7.5).

**Move-selection record.** The mission prompt says *pick the lowest-scoring axis*.
Round 13's L0 question (may a lane work an advisory axis as its lowest-axis move,
and D-78's `AXES.md`↔`MISSION.md` naming) is still unanswered, and this round
again works the lowest row rather than an owned one — recorded, not
re-litigated. `operability` is chosen over the two other 7.5 rows because it
carries a **named, pre-falsified, unlanded deliverable**: round 13's plan
(`SCORECARD.md` § planned, item 2) already wrote the falsifier for exactly this
move, and the `operability` row already names the residual — "`SKILL.md`
checklist boxes remain the only un-automated procedures (40 boxes)".

**Scope fence (stated before landing).** This move executes *one* checklist's
boxes on *one* file class (`SKILL.md`). It does **not** claim the other 26 boxes
are executed, and it does **not** get relabelled as a `coverage` gain: the
coverage row moves this round only as the round-14 measurement debt (§ Round-14
closure), never as a consequence of this move.

**Pre-state (commands to re-run, at `29c17be`, working tree clean):**

| Fact | Command | Value |
|---|---|---|
| boxes in file | `grep -c '^- \[ \]' SKILL.md` | 40 (14/9/9/8 by section) |
| boxes executed by a committed instrument | (no command existed) | **0** |
| instruments in `verifiers/` | `ls verifiers/*.py verifiers/*.sh \| wc -l` | 5 (4 py + 1 sh) |
| operability row | `SCORECARD.md` | 7.5 — was 7 |

## Claim under test (falsifiable)

> As of round 15, **seven** of the 40 `SKILL.md` checklist boxes are executed by
> a committed instrument (`verifiers/verify_skill_checklist.py`) instead of read
> by a human, **one** is delegated to an existing instrument by name, and the
> remaining **32** are mapped to `unexecuted:<reason>` — and every box in the
> file is mapped to exactly one of those three dispositions by
> `verifiers/checklist-baseline.json`, pinned with the box's text sha256 so that
> a reworded, added, or removed box FAILs the run.

Falsified by any of: a check that passes with the defect present; a box absent
from the map; a map entry with no live box; a reworded box that still passes; a
check whose `evaluated` count is 0 yet reports PASS.

## Properties

| # | Property | How it is falsified |
|---|---|---|
| P1 | Every executed box's rule is stated with its failure mode and its limits (rule table in this file) | a reviewer finds a rule whose stated limit is contradicted by its own fixture |
| P2 | Each check fails closed on a fixture carrying exactly that defect | per-check broken fixture + `--self-test` asserting exit code **and** failing check id |
| P3 | No vacuous PASS: every check reports `evaluated N`; `N == 0` is a FAIL | empty/clean fixture with zero subjects → FAIL, not PASS |
| P4 | The box map is two-way and hash-pinned | reworded box → FAIL naming the box id; extra map entry → FAIL |
| P5 | The instrument is hermetic and read-only over foreign repos | sentinel audit; fleet run touches sibling `SKILL.md` files with no write |
| P6 | A non-author re-derives the executed/unexecuted split from the file's box text and agrees | reviewer lane, disagreeing entry named rather than averaged |

## Outcome bands (pre-registered)

| Band | Condition | operability |
|---|---|---|
| full | P2–P4 all hold, `--self-test` green with ≥1 assertion per check, mutation lane finds no escape inside the seven executed checks, reviewer re-derivation agrees, fleet application lands | **8.5** (8 = independently re-measured; +0.5 = one of the two band-9 criteria — machine-checked) |
| partial | instrument green and self-tested, but ≥1 escape or ≥1 unresolved lane disagreement | 8.0 |
| no move | any check cannot fail, or the map is decorative (a new box passes unmapped) | 7.5 |
| regression | the instrument reports a defect on the live file that a reviewer shows is not a defect (false positive) without an adjudicated rule fix | 7.0 |

## Round-14 closure (recording debt, not a second move)

Round 14 landed the opencode-side machine check and the census row-column parity
(`29c17be`) but the round terminated before the score was recorded: `SCORECARD.md`
still reads `coverage … 8.0 … Last change 13`, and
`../.ufo/reports/round-14/kotoba.md` is a DRAFT carrying `[PENDING]` markers.
Round 14's own pre-registration bands were full ⇒ 8.5 / partial ⇒ 8.25 /
no-move ⇒ 8.0. Round 15 re-measures the landed artifacts against those bands and
records the result **attributed to round 14** in `SCORECARD.md`, with the
attribution defect (unscored landing) named in `LOG.md`. Corrections to the
round-14 report land as an erratum appended after its filed bytes (PROTOCOL.md:
a filed report is a record, never rewritten).

## L2 plan (≥8 lanes, one batched call; floor is `../MISSION.md` § L2)

Batch 1 — `R15Plan` (planner), `R15Connector` (connector) @m_lunamax;
`R15Populate`, `R15Exec` (executors), `R15Surfaces` (scout) @m_flash;
`R15Rules` (critic), `R15Witness` (labrat), `R15R14` (reviewer), `R15Safety`
(sentinel) @m_zfl. Batch 2 (post-build) — `R15Mutate` (mutation-tester),
`R15Review` (reviewer), `R15Agree` (labrat), `R15Dead` (simplifier), `R15Distill`
(distiller), `R15Critic` (critic) @m_zfl.
