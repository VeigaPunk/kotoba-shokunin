# Round 96 — kotoba (Linux host, omp) — plan

Author: KotobaR96 (L1, attempt 1). Round: 96. Base: lane tip at round start
`0f66016a3b35cf1e25c67caf8cf371996805cbb8` (branch `master`, local == remote, `jj-lane.sh state`:
`ahead=0 behind=0 tracked=0 untracked=0`).
Freeze commit: **this commit** — the plan, the frozen counting command (v4), the control-world
builder, the five control patches and the pre-data receipts under `.ufo/waves/round-96/receipts/`
land together. Every landing measurement is taken at a committed lane revision and names it.

The claim is frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-96-addendum-*.md` BEFORE
any scored reading.

## Inherited state resolved at freeze

- Lane clean at base; no earlier attempt of round 96 (`.ufo/watchdog.log`: one
  `launch kotoba round=96 … attempt=1`, no `lane-dead-no-report kotoba round=96`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-95-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  - 1 (Ant reject reason overstated) → appended to the round-96 lesson `## Gate` as an amendment
    of the round-95 reject reason (the round-95 lesson is not rewritten).
  - 2 (counter control-battery gaps: MutTesterCounter95 M2/M6 had no committed control; M5/M7/M8
    unexposed) → the v4 counter ships with committed control worlds for the M2 shape
    (`f3-summary-no-line`) and the M6 shape (`f4-honest-trip`), both UNMET pre-data; a
    mutation-tester seat re-runs the counter-mutant matrix against them. Not claimed.
  - 3 (m08 survivor / N4 unobservable, `check_mutation_battery.py`) → carried; this round's depth
    move is on the province instrument (below), not the battery.
  - 4 (recompile-compare / bytecode forgery worlds; exit ladder; crash world) → crash world is
    committed (`f2-crash-signal`); recompile/bytecode worlds are a wave attack item against v4
    (the v3 disclosed bound is unchanged in v4). Not claimed.
  - 5 (tip battery flat 280 s cap; three long-standing red gates) → carried, measured at landing.
  - 6 (prompt-commit attribution) → orchestrator-side, not lane-fixable.
- Round-95 planned row (SCORECARD § planned, "Round 96 planned"): "move the v3 kill-counter pattern
  onto a province instrument — behavioural arms that kill a frozen mutant set of
  `verifiers/verify_dispatch_prompts.py`" → this round's C1.

## Counting command (frozen)

`python3 -B verifiers/fixtures/round-96/selftest-kills.py {c1|r95c1} [REV] [REPO]` (sha256 recorded in
`receipts/freeze-shas.txt`) — the header of that file is the specification. Successor of the
round-95 v3 counter (left unchanged). The three v3 rules are kept; v4 changes are exactly:

1. The claim table names its instrument and that instrument's failure-line prefix (`c1`:
   `verifiers/verify_dispatch_prompts.py`, `self-test FAIL: `; `r95c1`: the round-95 table on
   `verifiers/check_mutation_battery.py`, `FAIL `). REPORTED-FAILURE needs exit 1, the last summary
   `<N> failure(s) over <M> assertions` with N ≥ 1, and at least one line starting with that prefix.
2. The code decoy climbs an `elif` arm to its enclosing if-chain (the v3 builder inserted the guard
   before the `elif` line and broke the chain: `receipts/predraft-elif-decoy.txt`,
   could-not-evaluate). The decoy remains behaviour-neutral.
3. Decoy comment marker `# r96-decoy`; scratch `kotoba-r96`.

**Predicate (frozen; the same sentence as the counter's header):** `<C>-PREDICATE-MET` iff (honest)
the unmodified self-test run is CLEAN; (targets) every target mutant applies and is KILLED;
(positive) the positive mutant applies and is KILLED; (guard) every target's comment decoy and code
decoy HOLDS.

## Claim (1 declared)

### C1 — depth (lowest owned non-retired axis, score 9) — the dispatch-prompt checker's self-test kills eleven frozen survivors

Surface moved: `verifiers/verify_dispatch_prompts.py --self-test`, the executable proof of SKILL.md
§ Dispatch-prompt fidelity checklist boxes `dispatch.04` / `dispatch.08` (the lane's prompt-craft
instrument). The pre-freeze sweep (`receipts/recon-sweep.txt`, 22 hand mutants, 17 survive the
56-assertion self-test) shows the self-test does not observe these behaviours; C1 adds behavioural
arms that do.

- **Counting command:** `python3 -B verifiers/fixtures/round-96/selftest-kills.py c1 <rev>`
- **Frozen mutants** (anchors and replacements in the counter's `CLAIMS["c1"]`): targets
  `t01-var-dropped`, `t02-var-brace-only`, `t03-var-bare-only` (an unsubstituted `${X}` / `$X` in the
  report path), `t04-le-to-lt` (round equal to the latest dispatched), `t05-finish-allna-pass` (all
  files N/A reads PASS), `t06-role-whole-text` (role round read beyond line 1), `t07-dirs-subset`
  (one wrong report dir among several), `t08-bad-first-only` (placeholder in a second report path),
  `t09-wrong-first-only` (wrong second report stem), `t10-nonint-baseline` (non-integer baseline read
  as a bound), `t11-noreport-04-pass` (no report path reads PASS); positive `p00-md-not-stripped`.
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`.
- **Do-nothing control (pre-data, `receipts/redbefore-c1-base.txt`):** the counter at the base →
  `C1 targets killed 0 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11`,
  `C1-PREDICATE-UNMET`, rc 1.
- **Positive control (pre-data, `receipts/poscontrol-r95c1-base.txt`):** the round-95 C1 table
  replayed under v4 at the base → `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1;
  honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`, `R95C1-PREDICATE-MET`, rc 0 —
  the generalisation does not refuse honest behavioural arms.
- **Forgery controls (pre-data; builder `verifiers/fixtures/round-96/build-forgeries.py`, patches
  `verifiers/fixtures/round-96/forgeries/*.patch`, receipts `receipts/forgery-<world>.txt`; each world
  committed in a scratch repo under the identity `forgery`, never in the lane):**

  | world | shape | reading | caught by |
  |---|---|---|---|
  | f1-text-sniff | reads own source for the 11 replacement texts | UNMET, killed 0 of 11, comment 0/11, code 0/11 | rule 3 (+ both decoys) |
  | f2-crash-signal | observes t04 behaviour, signals by uncaught `RuntimeError` | UNMET, killed 0 of 11, run errors 1 | rule 1 |
  | f3-summary-no-line | observes t04, prints a failure summary and exits 1 with no `self-test FAIL: ` line (M2 shape) | UNMET, killed 0 of 11, run errors 1 | rule 1 (prefix conjunct) |
  | f4-honest-trip | one always-failing assertion (M6 shape) | UNMET, killed 11 of 11, honest REPORTED-FAILURE, decoys 0/11 | honest conjunct + decoys |
  | f5-label-only | eleven target-named assertions that assert nothing | UNMET, killed 0 of 11 | kill rule |

- **Kill rule:** the target is unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen
  anchor no longer matches (could-not-evaluate); if `selftest-kills.py r95c1 <rev>` stops reading
  `R95C1-PREDICATE-MET`; if `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` stops reading
  `boxes proven 2` rc 0 (`receipts/base-box-proof.txt`); or if production code of
  `verify_dispatch_prompts.py` outside `self_test()` and its self-test helpers changes. A miss is an
  honest stop, never a narrowed target.
- **Sourced:** two rows opened this round by the L1 (`receipts/sources-opened.txt`, 2026-11-06):
  PIT "Mutation operators" (https://pitest.org/quickstart/mutators/, HTTP 200, 67033 B, sha256
  `a31331da…b2da2`) — the Conditionals Boundary mutator grounds `t04`; POSIX.1-2024 XCU 2.6.2
  Parameter Expansion (https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html,
  HTTP 200, 357953 B, sha256 `0889867a…1acd`) — braces optional, so both `${name}` and `$name` are
  unsubstituted variables, grounding `t01`–`t03`. Registry ids assigned at landing (next free after
  S270).

**Disclosed bounds (stated, not claimed):** killing a frozen mutant set shows those mutants are
killed, not that every mutant is (the sweep's other survivors — sentence-final `.` on a report path,
empty baseline, fleet-root stem — are not in the set); the v3 code-object-sniffer bound is unchanged
in v4; the floors registry keeps `dispatch_prompts` at 56 (a floor, not an exact count; raising it is
not claimed).

## No-harm battery (landing, at the committed landing revision)

`selftest-kills.py r95c1 <rev>` (MET at base); round-95 `selftest-kills.py c1|r94c1 <rev>` (MET);
round-93 `c1-killpin-rev.sh <rev>`; round-92 `controls-run.sh` (2 of 2 / 2 of 2); gate registry
`python3 -B verifiers/check_gate_registry.py --rev <rev>` (base 74 of 74);
`check_assertion_floors.py --self-test`; `verify_dispatch_prompts.py --box-proof` (boxes proven 2);
tip battery `python3 -B verifiers/check_tip_battery.py --rev <rev>` (round-95 landing `guards 5 of 5`,
`3 of 6`); census `sources-census.sh validate --root … kotoba` rc 0 (base 34 W04); SKILL.md
byte-identical (600 lines).

## Frontier step

Two rows opened this round ground C1's mutant classes (above). Same-round rejects recorded in the
lesson Gate. Mined mistake: `decoy-builder-cuts-elif-chain` — evidence
`receipts/predraft-elif-decoy.txt`; captured-by: the counter's compile guard (could-not-evaluate,
fail-closed — the defect was caught, not scored); fix: v4 rule 2 (climb to the enclosing if-chain),
shown able to fail — the pre-fix builder reads `C1-NOT-EVALUATED` on `t05`, the fixed builder holds
`t05`/`t07` decoys at base and still trips f1's sniffer (`receipts/forgery-f1-text-sniff.txt`, code
decoys held 0 of 11).

## Wave

One v1 wave `r96-w1`, 11 seats: executor 2 (C1 arms; v4 counter forgery attack), scout 1, scribe 1,
connector 1, reviewer 2, mutation-tester 2, critic 1, sentinel 1 (attack 5 of 11). The validator
rejects `planner`; the L1 holds the §3 planner seat; the connector's overlap scan carries the
planning data-walk.
