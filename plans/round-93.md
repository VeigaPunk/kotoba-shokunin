# Round 93 — kotoba (Linux host, omp) — plan

Author: KotobaR93 (L1, attempt 1). Round: 93. Base: lane tip at round start
`5549fa9ed3cd91aeb0349178b5ba75dfe41711e7` (branch `master`, local == remote, `jj-lane.sh state`).
Freeze commit: **this commit** — the plan, both frozen counting commands, both forgery-control
patches and the pre-data receipts under `.ufo/waves/round-93/receipts/` land together. Every builder
patch is `git diff --binary` from this freeze commit; every landing measurement is taken at a
committed lane revision and names it (round-92 closure defect 1: receipts must resolve).

Claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-93-addendum-*.md`
BEFORE any scored reading.

## Inherited state resolved at freeze

- Lane clean at base (`git status --porcelain` empty; `jj-lane.sh state` → `ahead=0 behind=0`).
- No earlier attempt of round 93 (`.ufo/watchdog.log`: one `launch kotoba round=93 … attempt=1`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-92-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  1 (revision identity) → record repair this round: every round-93 landing receipt names a
  committed lane revision, and the mined mistake below ships a check shown able to fail on the
  round-92 receipts; 2 (D2, committed-revision kill naming) → **C1**; 3 (F1, refused world's own exit
  code) → both round-93 counters pin the refused world's exit code (`rc == 2` in C1; the frozen
  tally line `guards 4 of 5` in C2); 4 (F-4, whole `INSTRUMENT_PINS` key removal silent) → **C2**;
  5 (Gate without a reject) → the round-93 lesson's Gate records a same-round reject or the sweep
  that found none; 6 (planner seat) → the report records that the validator rejects `planner` and the
  L1 holds the planner seat; 7 (lesson "pending") → the round-93 lesson cross-references
  `round-92-verifier-spotcheck.md` (the round-92 lesson is not rewritten); 8 carried reds → no-harm
  battery below.

## Claims (2 declared; causally separable; distinct axes)

### C1 — depth (lowest owned non-retired axis, score 9) — the battery names `kill-set-size` on a committed-revision dropped kill row

Routed defect 2 (round-92 addendum A3; CriticClaimsR92 D2). Round 92 pinned the kill-set size in
the battery's `--self-test` only (the working-tree manifest). A committed revision whose manifest
drops one kill row is refused by `evaluate()` only indirectly — the materialized clone's own
`bat-self-test` probe fails its declared baseline — with rc 2 and a line that does not name the arm.
C1 makes the `--rev` path read the committed manifest's kill-row count and refuse a count other than
`KILL_SET_PINNED` as could-not-evaluate (rc 2) **naming `kill-set-size`**, without labelling any other
baseline failure that way.

- **Counting command (frozen):** `bash verifiers/fixtures/round-93/c1-killpin-rev.sh [REV]`
- **Predicate (frozen, same sentence as the counter's header):** `C1-PREDICATE-MET` iff (drop) the
  committed world with the first `kill` row removed reads rc 2 AND names `kill-set-size`; (other) the
  committed world with the `fg-fixed-plan` fixture emptied and kill rows untouched reads rc 2 AND does
  NOT name `kill-set-size`; (honest) REV unmodified reads rc 0 AND does NOT name `kill-set-size`.
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision.
- **Do-nothing control (pre-data, receipt `receipts/redbefore-c1-base.txt`):** the counter at the base
  `5549fa9e` — expected `C1-PREDICATE-UNMET` (drop world rc 2, names no).
- **Forgery control (pre-data, `verifiers/fixtures/round-93/forgery-c1.patch`, receipt
  `receipts/forgery-c1-run.txt`):** a checker that prefixes every could-not-evaluate line with
  `arm kill-set-size:` — expected `C1-PREDICATE-UNMET` via the other world.
- **Kill rule:** the target is unmet if the landing reading is not `C1-PREDICATE-MET`, if the round-92
  controls (`bash verifiers/fixtures/round-92/controls-run.sh`) stop reading `shortcuts refused 2 of 2;
  honest held 2 of 2`, or if `--self-test` stops reading `0 failure(s)`. A miss is an honest stop,
  never a narrowed target.
- **Sourced:** the committed-revision read (`git show <rev>:<path>`) is grounded in a SOURCES row
  opened this round (gitrevisions `<rev>:<path>`), cited by the round-93 lesson and this claim's
  SCORECARD evidence.

### C2 — consistency (calibration sub-axis, score 10) — dropping a battery instrument's pin key is a named instrument-pin failure

Routed defect 4 (round-92 MutTesterBattery F-4). The tip battery's comment says "the pins, not the
size bound, carry the anti-laundering load", but `run_guards()` iterates `INSTRUMENT_PINS.items()`:
deleting one battery instrument's key silently removes that instrument from the pin guard — the
lane's self-assessment (the instrument is pinned) and the observed checker state disagree with no
signal. C2 makes every frozen `BATTERY` script path a required `INSTRUMENT_PINS` key, reported under
the existing `instrument-pin` guard id (the guard count stays 5).

- **Counting command (frozen):** `bash verifiers/fixtures/round-93/c2-pinkey.sh [REV]`
- **Predicate (frozen):** `C2-PREDICATE-MET` iff (honest) the unmodified checker prints
  `guard instrument-pin PASS` and `guards 5 of 5`; (keydrop) with the
  `verifiers/check_correction_sweep.py` key removed, a `FAIL guard instrument-pin:` line names
  `verifiers/check_correction_sweep.py` and the tally reads `guards 4 of 5`; (keyswap) the same key
  removed and a junk key added (key count unchanged) reads the same as keydrop.
- **Target:** `C2-PREDICATE-MET`, exit 0, at the landing revision.
- **Do-nothing control (pre-data, `receipts/redbefore-c2-base.txt`):** the counter at the base —
  expected `C2-PREDICATE-UNMET` (keydrop reads `guards 5 of 5`, no finding).
- **Forgery control (pre-data, `forgery-c2.patch`, `receipts/forgery-c2-run.txt`):** a count-based
  checker (`len(INSTRUMENT_PINS) < 7` → hardcoded finding) — expected `C2-PREDICATE-UNMET` via the
  keyswap world.
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET`, if `check_tip_battery.py
  --self-test` stops reading `0 failure(s)`, or if the round-92 `ctl-c2-honest.sh` world stops reading
  `C2-PREDICATE-MET`.
- **Disclosed scope:** the required key set is the frozen `BATTERY` list; `check_freeze_gate.py`'s key
  (not a battery script) is not covered, and an edit that removes both a key and the coverage check is
  out of scope for an in-file guard. Both are stated, not claimed.

Causal separability: C1 touches only `verifiers/check_mutation_battery.py`; C2 touches only
`verifiers/check_tip_battery.py`. Neither counter runs the other instrument.

## No-harm battery (landing, at the committed landing revision)

Gate registry `python3 -B verifiers/check_gate_registry.py --rev <rev>` (base 74 of 74); tip battery
`python3 -B verifiers/check_tip_battery.py --rev <rev>` (base guards 5 of 5; 3 of 6, the carried
reds); round-92 controls `controls-run.sh` (2 of 2 / 2 of 2); `check_mutation_battery.py
--self-test`, `check_tip_battery.py --self-test`, `check_assertion_floors.py --self-test`; census
`sources-census.sh validate --root … kotoba` rc 0; SKILL.md byte-identical (600/600 lines).

## Frontier step

One SOURCES row opened this round grounds C1 (gitrevisions `<rev>:<path>`); one same-round reject
recorded in the lesson Gate; mined mistake: round-92 receipts named a scratch revision that never
resolved in the lane (closure defect 1) — fix: `verifiers/fixtures/round-93/check-receipt-revs.sh`,
shown failing on `.ufo/waves/round-92/receipts/landing/` and passing on the round-93 landing receipts.

## Wave

One v1 wave `r93-w1`, 12 seats: executor 3, scout 1, scribe 1, connector 1, reviewer 2,
mutation-tester 2, critic 1, sentinel 1 (attack 5 of 12). The validator rejects `planner`; the L1
holds the §3 planner seat.
