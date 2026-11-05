# Round 94 — kotoba (Linux host, omp) — plan

Author: KotobaR94 (L1, attempt 1). Round: 94. Base: lane tip at round start
`4d3e8e4d290d67ecf94a019059f434c71f399919` (branch `master`, local == remote, `jj-lane.sh state`:
`ahead=0 behind=0 tracked=0 untracked=0`).
Freeze commit: **this commit** — the plan, the frozen counting command, the forgery patch and the
pre-data receipts under `.ufo/waves/round-94/receipts/` land together. Every builder patch is
`git diff --binary` from this freeze commit; every landing measurement is taken at a committed lane
revision and names it.

Claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-94-addendum-*.md` BEFORE
any scored reading.

## Inherited state resolved at freeze

- Lane clean at base; no earlier attempt of round 94 (`.ufo/watchdog.log`: one
  `launch kotoba round=94 … attempt=1`, no `lane-dead-no-report kotoba round=94`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-93-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  1 (C2 measures one key; MutTesterPinCov m5) → **C2**; 2 (C1 counter gaps: dirty working tree
  F1/m3, added kill row F2, label-every-CNE F4/m6) → **C1**; R2 (cause attribution in the round-93
  `other` world) → carried, not claimed; 3 (receipt check fails open on a 41-hex header D2 and an
  indented header D3) → the round's **mined mistake** and its fix; 4 (a seat ended without writing
  its report file) → the wave context requires every seat to write its report file before its final
  answer, and the report records any seat that did not; 5 (prompt-commit attribution) →
  orchestrator-side, noted, not lane-fixable.

## Shared counting command (frozen)

`python3 -B verifiers/fixtures/round-94/selftest-kills.py {c1|c2} [REV] [REPO]` — the header of that
file is the specification. It clones REV, runs the claim's instrument `--self-test` unmodified
(honest), once per frozen mutant (a literal substitution of the instrument bytes at REV whose anchor
must match the declared number of times and whose result must compile, else could-not-evaluate),
and once per target **decoy** (the unmodified instrument with the mutant's replacement appended as
comments). A mutant is KILLED iff its self-test exits non-zero within 600 s (a timeout is
could-not-evaluate). The outcome classes follow S269 (PIT, "Killed means a test caught the mutation
successfully"); a mutant that does not compile is the non-viable class and is never scored as a kill.

**Predicate (frozen; the same sentence as the counter's header):** `<C>-PREDICATE-MET` iff (honest)
the unmodified self-test exits 0 and prints `0 failure(s)`; (targets) every target mutant applies and
is KILLED; (positive) the positive mutant applies and is KILLED; (guard) every target decoy's
self-test exits 0.

## Claims (2 declared; causally separable; distinct axes)

### C1 — depth (lowest owned non-retired axis, score 9) — the battery self-test kills the three round-93 kill-pin gaps

Instrument `verifiers/check_mutation_battery.py`. Round 93 recorded three mutants of the
committed-revision kill-set pin that its `--self-test` does not kill: a check that reads the
working-tree manifest (m3/F1), every could-not-evaluate line labelled `arm kill-set-size:` (m6/F4),
and a pin that accepts a count above the pin (F2). C1 adds behavioural self-test arms that kill them.

- **Counting command:** `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 <rev>`
- **Frozen mutants:** targets `k1-worktree-manifest`, `k2-label-every-cne`, `k3-accept-added-rows`;
  positive `k0-accept-any` (anchors and replacements in the counter's `CLAIMS["c1"]`).
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`.
- **Do-nothing control (pre-data, `receipts/redbefore-c1-base.txt`):** the counter at the base →
  `C1 targets killed 0 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`,
  `C1-PREDICATE-UNMET`, rc 1.
- **Forgery control (pre-data, `verifiers/fixtures/round-94/forgery-sniff.patch`, receipt
  `receipts/forgery-c1-run.txt`):** a self-test that "kills" each mutant by searching its own source
  for the mutant's text (tokens split across literals so the honest run passes) — expected
  `C1-PREDICATE-UNMET` via the decoy guard.
- **Kill rule:** the target is unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen
  anchor no longer matches (could-not-evaluate); if `bash verifiers/fixtures/round-92/controls-run.sh`
  stops reading `shortcuts refused 2 of 2; honest held 2 of 2`; or if
  `bash verifiers/fixtures/round-93/c1-killpin-rev.sh <rev>` stops reading `C1-PREDICATE-MET`. A miss
  is an honest stop, never a narrowed target.
- **Sourced:** S269 (PIT basic concepts, outcome classes), opened this round, cited here and in the
  round-94 lesson.

### C2 — consistency (calibration sub-axis, score 10) — the tip-battery self-test measures every BATTERY pin key

Instrument `verifiers/check_tip_battery.py`. Round 93 made a missing `INSTRUMENT_PINS` key a named
`instrument-pin` failure, but the self-test drops only `BATTERY[5]`: a coverage loop hardcoded to that
one key, or one that skips the first script, passes it (MutTesterPinCov m5; closure defect 1). C2
makes the self-test measure the six-key coverage behaviourally.

- **Counting command:** `python3 -B verifiers/fixtures/round-94/selftest-kills.py c2 <rev>`
- **Frozen mutants:** targets `p1-one-key-hardcode`, `p2-skip-first-key`; positive
  `p0-skip-last-key`.
- **Target:** `C2-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2`.
- **Do-nothing control (pre-data, `receipts/redbefore-c2-base.txt`):** expected
  `C2 targets killed 0 of 2`, `C2-PREDICATE-UNMET`, rc 1.
- **Forgery control (pre-data, same patch, `receipts/forgery-c2-run.txt`):** expected
  `C2-PREDICATE-UNMET` via the decoy guard.
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET`, if a frozen anchor no
  longer matches, or if `bash verifiers/fixtures/round-93/c2-pinkey.sh <rev>` stops reading
  `C2-PREDICATE-MET`.

Causal separability: C1 touches only `verifiers/check_mutation_battery.py`; C2 touches only
`verifiers/check_tip_battery.py`. The counter's `c1` and `c2` runs read only their own instrument.

**Disclosed bounds (stated, not claimed):** the decoy guard catches text sniffers that read comment
lines; an AST-aware sniffer is out of its reach (the reviewer seats read the new arms for behaviour).
Killing a frozen mutant set shows those mutants are killed, not that every mutant is.

## No-harm battery (landing, at the committed landing revision)

Gate registry `python3 -B verifiers/check_gate_registry.py --rev <rev>` (base 74 of 74); tip battery
`python3 -B verifiers/check_tip_battery.py --rev <rev>` (base guards 5 of 5; 3 of 6, the carried
reds); round-92 `controls-run.sh` (2 of 2 / 2 of 2); round-93 counters `c1-killpin-rev.sh`,
`c2-pinkey.sh` (MET); `check_assertion_floors.py --self-test`; census
`sources-census.sh validate --root … kotoba` rc 0; SKILL.md byte-identical (600 lines).

## Frontier step

S269 (PIT basic concepts) opened this round grounds the counter's outcome classes and C1. One
same-round reject recorded in the lesson Gate. Mined mistake: the round-93 receipt check
`verifiers/fixtures/round-93/check-receipt-revs.sh` fails open on a header-shaped line it cannot
parse (a 41-hex `REV=` header is silently dropped; an indented header is ignored; CriticClaimsR93
D2/D3) — captured-by `none`; fix: such lines are reported `MALFORMED` and exit 1, shown able to fail
on committed fixtures under `verifiers/fixtures/round-94/receipt-headers/`, while the round-93
landing receipts still read `9 resolved, 0 unresolved`, rc 0.

## Wave

One v1 wave `r94-w1`, 12 seats: executor 3, scout 1, scribe 1, connector 1, reviewer 2,
mutation-tester 2, critic 1, sentinel 1 (attack 5 of 12). The validator rejects `planner`; the L1
holds the §3 planner seat; the connector's overlap scan carries the planning data-walk.
