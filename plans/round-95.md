# Round 95 — kotoba (Linux host, omp) — plan

Author: KotobaR95 (L1, attempt 1). Round: 95. Base: lane tip at round start
`2d886a91e57efd3555ec9076a63209e2d8bfbb8d` (branch `master`, local == remote, `jj-lane.sh state`:
`ahead=0 behind=0 tracked=0 untracked=0`).
Freeze commit: **this commit** — the plan, the frozen counting command, the control-world builder,
the six control patches and the pre-data receipts under `.ufo/waves/round-95/receipts/` land
together. Every builder patch is `git diff --binary` from this freeze commit; every landing
measurement is taken at a committed lane revision and names it.

The claim is frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-95-addendum-*.md` BEFORE
any scored reading.

## Inherited state resolved at freeze

- Lane clean at base; no earlier attempt of round 95 (`.ufo/watchdog.log`: one
  `launch kotoba round=95 … attempt=1`, no `lane-dead-no-report kotoba round=95`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-94-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  - 2 (counter scores a run error as a kill; CriticClaimsR94 D8) → fixed in this round's frozen
    counter (rule 1: a kill is a REPORTED-FAILURE; RUN-ERROR is its own class), shown able to fail
    on control world f6 (below); the round's **mined mistake**.
  - 3 (the decoy guard misses comment-skipping sniffers; A2/D4) → fixed in the frozen counter
    (rule 2: a code decoy; rule 3: source-blind mutant runs), shown able to fail on control worlds
    f2, f3, f4, f5.
  - 4 (battery survivors N1, N5, N11) → **C1**. D3 (receipt declarations that do not start a line)
    → carried with reason: a mid-line rule makes honest `lane rev <hash>` lines in committed
    receipts change class, which needs its own no-harm census; not claimed this round.
  - 1 (S269/S262 same-URL duplicate forced by a frozen plan) → a lesson-backed `QUALITY.md`
    criterion at record time; this round adds no row on a URL the registry already holds (S260
    already holds the Stryker page — re-opened as corroboration, no new row; the new row is a
    different document).
  - 5 (tip-battery floors gate 280 s timeout under fleet load) → carried, measured at landing and
    reported; no claim.
  - 6 (prompt-commit attribution) → orchestrator-side, not lane-fixable.

## Counting command (frozen)

`python3 -B verifiers/fixtures/round-95/selftest-kills.py {c1|r94c1} [REV] [REPO]` (sha256
`d6ae74af40135f9b30b0101d5a195a3d950b6a72073020ac59ba58da1d269001` at freeze) — the header of that
file is the specification. Successor of the round-94 counter (left unchanged). For each run the
instrument `verifiers/check_mutation_battery.py --self-test` is executed in a `--shared` clone at
REV; three rules differ from round 94:

1. **Outcome classes.** REPORTED-FAILURE = exit 1 and the summary `<N> failure(s) over <M>
   assertions` with N ≥ 1 and at least one `FAIL ` line; CLEAN = exit 0 and N = 0; anything else is
   RUN-ERROR. A mutant is KILLED iff REPORTED-FAILURE; a RUN-ERROR is never a kill. Grounds: S270
   (Python `unittest.TestResult`: `errors` are tests that "raised an unexpected exception",
   `failures` are tests where "a failure was explicitly signalled") and S260 re-opened (Stryker:
   "Runtime error — The running of the tests resulted in an error (rather than a failed test)").
   A timeout (600 s) or a mutant that does not compile is could-not-evaluate (exit 2).
2. **Two decoys per target.** The comment decoy (round 94) and a code decoy: each changed statement
   inserted, mutated, under `if __name__ == "__decoy__":` immediately before the original statement.
   A decoy HOLDS iff CLEAN.
3. **Source-blind mutant runs.** A mutant's code is compiled with the instrument's path as filename
   and executed as `__main__` while the file on disk holds the unmodified bytes; a self-test that
   reads its own source cannot tell a mutant run from the honest run.

**Predicate (frozen; the same sentence as the counter's header):** `<C>-PREDICATE-MET` iff (honest)
the unmodified self-test run is CLEAN; (targets) every target mutant applies and is KILLED;
(positive) the positive mutant applies and is KILLED; (guard) every target's comment decoy and code
decoy HOLDS.

## Claim (1 declared)

### C1 — depth (lowest owned non-retired axis, score 9) — the battery self-test kills the round-94 survivors N1, N5, N11

Instrument `verifiers/check_mutation_battery.py`. Round-94 MutTesterBattery94 recorded three
mutants that the landed `--self-test` does not kill (`.ufo/waves/round-94/w1/MutTesterBattery94.md`):
N1 the `--rev` kill-set check reads the manifest at `HEAD` instead of `--rev` (every rev-path
fixture has `rev == HEAD`); N5 the target-set refusal is labelled `arm kill-set-size:` (no arm
exercises that refusal's label); N11 the pin accepts exactly two rows above it (the added-row arms
add one row only). C1 adds behavioural self-test arms that kill them.

- **Counting command:** `python3 -B verifiers/fixtures/round-95/selftest-kills.py c1 <rev>`
- **Frozen mutants:** targets `n1-manifest-at-head`, `n5-label-targets-cne`, `n11-accept-plus-two`;
  positive `n10-accept-plus-one` (anchors and replacements in the counter's `CLAIMS["c1"]`).
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`.
- **Do-nothing control (pre-data, `receipts/redbefore-c1-base.txt`):** the counter at the base →
  `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`,
  `C1-PREDICATE-UNMET`, rc 1.
- **Positive control (pre-data, `receipts/poscontrol-r94c1-base.txt`):** the round-94 C1 table
  replayed under the v3 rules at the base → `R94C1 targets killed 3 of 3 (run errors 0); positive
  killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`,
  `R94C1-PREDICATE-MET`, rc 0 — the v3 rules do not refuse honest behavioural arms (blanket refusal
  is not a gain).
- **Forgery controls (pre-data; builder `verifiers/fixtures/round-95/build-forgeries.py`, patches
  `verifiers/fixtures/round-95/forgeries/*.patch`, receipts `receipts/forgery-<world>.txt`; each
  world committed in a scratch repo under the identity `forgery`, never in the lane):**

  | world | shape | reading | caught by |
  |---|---|---|---|
  | f1-text-sniff | every line, substring (round-94 forgery) | UNMET, killed 0 of 3, comment 0/3, code 0/3 | rule 3 (+ both decoys) |
  | f2-line-filter | non-`#` lines (CriticClaimsR94 D4) | UNMET, killed 0 of 3, code 0/3 | rule 3 (+ code decoy) |
  | f3-token-sniff | tokenize, comments dropped (MutTesterBattery94) | UNMET, killed 0 of 3, code 0/3 | rule 3 (+ code decoy) |
  | f4-guard-aware-raise | skips comments and the decoy guard; raises | UNMET, killed 0 of 3 | rule 3 |
  | f5-guard-aware-report | skips comments and the decoy guard; reports | UNMET, killed 0 of 3 | rule 3 |
  | f6-crash-report | drives N11 behaviour, signals by uncaught `RuntimeError` (D8 shape) | UNMET, killed 0 of 3, run errors 1 | rule 1 |

- **Kill rule:** the target is unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen
  anchor no longer matches (could-not-evaluate); if `python3 -B verifiers/fixtures/round-95/selftest-kills.py r94c1 <rev>`
  stops reading `R94C1-PREDICATE-MET`; if `bash verifiers/fixtures/round-92/controls-run.sh` stops
  reading `shortcuts refused 2 of 2; honest held 2 of 2`; or if
  `bash verifiers/fixtures/round-93/c1-killpin-rev.sh <rev>` stops reading `C1-PREDICATE-MET`. A miss
  is an honest stop, never a narrowed target.
- **Sourced:** S270 (Python `unittest` — `TestResult.errors` / `TestResult.failures`), opened this
  round (2026-11-05, HTTP 200, 336978 B, sha256
  `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d`), grounds rule 1, which decides
  what C1's "killed" means. S260 (Stryker "Mutant states and metrics") re-opened the same day
  (HTTP 200, 27068 B, sha256 `8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da`)
  as corroboration; no new row on its URL.

**Disclosed bounds (stated, not claimed):** a self-test that sniffs its own compiled code objects
(not its source file) and proves the decoy guard dead is not caught; killing a frozen mutant set
shows those mutants are killed, not that every mutant is. Stryker counts a timeout as detected; this
counter keeps a timeout could-not-evaluate (stricter, as in round 94).

## No-harm battery (landing, at the committed landing revision)

`selftest-kills.py r94c1 <rev>` (MET at base); round-93 `c1-killpin-rev.sh <rev>` and
`c2-pinkey.sh <rev>` (MET); round-94 `selftest-kills.py c1|c2 <rev>` (MET at base); round-92
`controls-run.sh` (2 of 2 / 2 of 2); gate registry `python3 -B verifiers/check_gate_registry.py --rev <rev>`
(base 74 of 74); `check_assertion_floors.py --self-test`; tip battery
`python3 -B verifiers/check_tip_battery.py --rev <rev>` (round-94 landing `guards 5 of 5`, `2 of 6`
with the floors timeout routed as defect 5); census `sources-census.sh validate --root … kotoba`
rc 0; SKILL.md byte-identical (600 lines).

## Frontier step

S270 opened this round grounds C1's kill rule. Same-round rejects recorded in the lesson Gate.
Mined mistake: `run-error-scored-as-kill` — evidence `.ufo/waves/round-94/w1/CriticClaimsR94.md`
D8; captured-by `none`; fix: rule 1, shown able to fail on f6 (`receipts/forgery-f6-crash-report.txt`:
`run errors 1`, UNMET, where the round-94 rule `rc != 0` would have scored the same run KILLED).

## Wave

One v1 wave `r95-w1`, 12 seats: executor 3 (C1 arms; base no-harm readings; further forgery
worlds against the v3 counter), scout 1, scribe 1, connector 1, reviewer 2, mutation-tester 2,
critic 1, sentinel 1 (attack 5 of 12). The validator rejects `planner`; the L1
holds the §3 planner seat; the connector's overlap scan carries the planning data-walk.
