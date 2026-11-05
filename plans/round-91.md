# Round 91 — plan (frozen before any candidate score)

Author: KotobaR91 (L1). Base: `9264baaa823cdae3d009a4004e014639551e016f` (lane tip = pushed
`master` tip at round start; `jj-lane.sh state`: ahead 0 / behind 0). Linux host, omp.
Round-start census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kotoba` → exit 0, `kotoba  ok`, 33 pre-existing W04
duplicate-URL warnings (unchanged class), 187 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → 187). Receipt: `.ufo/waves/round-91/receipts/census-before.txt`.

Q19 re-measure of every carried before-value used below, run fresh at the base this round,
never copied: tip battery `guards 4 of 5; tip battery exit 0: 3 of 6`, rc 1
(`receipts/tipbattery-before.txt`) — including the NEW finding that the battery's
`instrument-pin` guard FAILs (`verifiers/check_assertion_floors.py` blob `c10c0f10…` is not a
pinned blob): the round-90 floors bump landed a new blob without the INSTRUMENT_PINS admission,
red since the r90 landing, unobserved until this re-measure; `verify_harness_independent.py
--self-test` measured standalone 160.2 s, exit 0, `0 failure(s) over 123 assertions`, 1-min
loadavg 2.73→3.16 (`receipts/harness-selftest-duration.txt`, against the base rev); freeze-gate
self-test `0 failure(s) over 30 assertions` (`receipts/base-freeze-selftest.txt`); battery
manifest 14 kill + 6 equivalent rows (`receipts/base-battery-manifest.txt`); registry 74 of 74
rc 0 (`base-registry.txt`); floors guard self-test rc 0 (`base-floors-selftest.txt`); checklist,
integrity, d5v3, sibling reds re-named in § No-harm battery. All five r90 routed defects
(`corpus/lessons/round-90-verifier-spotcheck.md` § Routed defects) are addressed this round:
1 → C1, 4 and 5 → C2, 2 and 3 as unclaimed work items in the scribe item.

## Claims (frozen)

### C1 — depth (owned reading: depth 9 < consistency 10, the lowest owned axis; type: capability deepening)

Surface: `verifiers/check_mutation_battery.py` (the r90 C1 instrument) and
`verifiers/fixtures/mutation-battery/manifest.tsv`. Closes r90 routed defect 1: the battery's
own G1 commit-check, G1 clean-tree and revision-copy restore guards have no self-test arm —
the three battery-guard mutants `mb-m2`, `mb-m15`, `mb-m16` (r90 `MutTesterBattery` recipes,
`.ufo/waves/round-90/w1/MutTesterBattery/harness.py`) survive at the base.

**Frozen predicate (one sentence, identical in receipts):** at the landing revision,
`python3 -B verifiers/check_mutation_battery.py --rev <rev> --work <scratch>` prints exactly
`mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors
0 of 0` and exits 0 with guards G1–G3 PASS, and `python3 -B verifiers/check_mutation_battery.py
--self-test` prints `0 failure(s) over N assertions` with N ≥ 22, exit 0.

- Counting command before: `grep -cP '\tkill\t'
  verifiers/fixtures/mutation-battery/manifest.tsv` → 14 at the base
  (`receipts/base-battery-manifest.txt`), and the three routed guard mutants replayed on the
  base bytes each leave the battery self-test green — the controls
  `ctl-c1-m2/mb-m15/mb-m16` print `SURVIVED` (plans/round-91-controls.md), so no-work cannot
  reach "killed 17 of 17".
- Counting command after: the predicate run and the self-test at the landing revision, plus the
  same three mutant replays at the landing bytes each printing `KILLED` (self-test exits
  nonzero under its mutant) — committed receipts.
- Design: (i) the manifest gains exactly three kill rows (targets
  `verifiers/check_mutation_battery.py`, recipes ported from the r90 harness with anchors
  re-verified against the final bytes: `mb-m2` G1 commit-check skip, `mb-m15` G1 clean-tree
  guard off, `mb-m16` restore `place(...)` re-read dropped); (ii) the battery's frozen probe
  set gains a third target entry for `verifiers/check_mutation_battery.py` (probe `--self-test`,
  declared baseline exit 0) so `manifest targets == PROBES keys` stays true; (iii) three new
  self-test arms exercise the three guards (non-commit full-hex `--rev` raises `CouldNotEvaluate`
  naming G1; a dirtied scratch clone raises G1 not-clean; a target file left mutated after a
  battery run is detected against the revision bytes), each arm red when its guard is disabled —
  the arms are the kill channel; (iv) the two-sided rule (Q47) is unchanged: the 6
  measurement-time equivalents survive, every kill-class row is killed; (v) if the battery
  self-test pins the real manifest's shape (targets or row counts), the same change updates that
  pin — sweep before editing (`grep -n 'PROBES\|manifest' verifiers/check_mutation_battery.py`).
- Guards: G1/G2/G3 as frozen; the instrument's SKILL.md registry row is NOT edited and stays
  conformant (`python3 -B verifiers/check_gate_registry.py --rev <landing>` → 74 of 74,
  phantom 0).
- Sourced: the knowledge entry `corpus/knowledge/mutation-battery-arms-round91.md` cites S262
  (external, opened this round) beside the own-work r90 battery bytes.
- Kill rule: no counter, manifest, PROBES or plan amendment after any scored reading; a defect
  found post-score is a routed finding, never repaired into the frozen bytes.

### C2 — freshness (advisory tied-lowest 8.0 under the all-axes reading; type: measured axis-move, two routed repairs)

Surface: (leg A) the floors guard's child-cap drift and the instrument-pin admission gap; (leg B)
the freeze-gate probe-world exit-ladder defect (r90 routed defects 4 and 5; the routed pointer is
`.ufo/reports/round-90/kotoba.md:113` on the fleet repo). The claim verifies only when BOTH
legs' after-states hold at the landing revision.

**Frozen predicate (legs conjoined):** at the landing revision —

- Leg A (floors child-cap, Q39 calibration + instrument-pin admission):
  - (a) `grep -n '^SELF_TEST_TIMEOUT_S = ' verifiers/check_assertion_floors.py` prints
    `SELF_TEST_TIMEOUT_S = 360` — the Q39 calibration: 2 × the round-91 measured standalone
    duration (160.2 s, `receipts/harness-selftest-duration.txt`, committed at the freeze, run
    against the base) rounded up to the 60 s grid; the receipt records host load and wall time.
  - (b) a new in-file constant pins the measured duration (`MEASURED_SELFTEST_S`, ceil to
    161) citing that receipt, and a new floors-guard self-test arm asserts
    `SELF_TEST_TIMEOUT_S >= 2 * MEASURED_SELFTEST_S` — the arm fails if either side is lowered
    (content guard, Q25); the floors-guard floor is bumped in-step in
    `verifiers/floors-registry.json` and the guard's two in-file tables (`instrument_total`
    stays 19), and `python3 -B verifiers/check_assertion_floors.py --self-test` exits 0 at the
    landing (`0 failure(s) over N assertions`).
  - (c) able-to-fail arms: a planted over-cap sleeper reads `self-test timed out` exit 2, and a
    planted sub-cap sleeper passes (Q18: no false red) — committed receipts.
  - (d) the instrument-pin gap heals: `git rev-parse <landing>:verifiers/check_assertion_floors.py`
    names a blob that IS an `INSTRUMENT_PINS` entry in `verifiers/check_tip_battery.py` (the
    admission lands in the same change, with a pointer comment naming this plan); the tip
    battery at the landing prints `guards 5 of 5; tip battery exit 0: 3 of 6` — the same three
    green gates as the base (gate registry, floors, correction sweep), no gate regressed (Q72
    post-state no-harm).
  - (e) a bare floors walk at the landing exits 0 on this host
    (`receipts/floors-live-landing.txt` naming the rev and the observed load).
- Leg B (freeze-gate probe-world exit ladder):
  - (a) the defect is re-derived from committed evidence BEFORE repair and recorded in
    `.ufo/waves/round-91/receipts/ladder-defect.md` (the probe world, the declared expectation,
    the observed exit at the base bytes, the command that showed it); if the routed pointer
    under-specifies and no inconsistency is re-derivable, the honest stop is recorded there and
    leg B narrows to `unprovable` in the report — decided before any scored reading, never
    after.
  - (b) the repair lands in `verifiers/check_freeze_gate.py` frozen bytes with a new self-test
    arm pinning the corrected leg; `python3 -B verifiers/check_freeze_gate.py --self-test` at
    the landing prints `0 failure(s) over N' assertions`, exit 0, with N' > 30 (the base count,
    `receipts/base-freeze-selftest.txt`).
  - (c) able-to-fail: in a scratch world reverting the touched lines to the base bytes, the new
    arm is red (committed receipt).
  - (d) no ladder regression: `fg-m3-ladder-refusal-to-2` and `fg-m3b-ladder-eval-to-1` stay
    killed inside C1's landing battery run (the same run covers both claims; named in both).

- Counting command before: `tipbattery-before.txt` (`guards 4 of 5`),
  `base-freeze-selftest.txt` (30 assertions), `harness-selftest-duration.txt` (160.2 s against
  cap 120 — the stale-premise arithmetic in the guard docstring names round-56 figures).
- Counting command after: the greps and self-tests above at the landing + the tip battery line.
- Sourced: the knowledge entry `corpus/knowledge/timeout-calibration-round91.md` cites S263
  (external, opened this round) beside Q39's grounded lesson.
- Controls (pre-data, through the r89 freeze gate): ctl-c2-cap, ctl-c2-ladder, ctl-c2-pin,
  ctl-c2-fakecap (plans/round-91-controls.md).
- Kill rule: as C1.

### Lowest-axis obligation

Owned reading: depth 9 < consistency 10 → C1 works the lowest owned axis. All-axes reading:
freshness 8.0 and adjacency 8.0 tied lowest → C2 works freshness. Both readings stated and both
worked; the L0 question (`kotoba | round-50`) stays open.

## No-harm battery (Q65 at base — receipts committed at the freeze; Q72 post-state at landing)

| command | base reading |
|---|---|
| `python3 -B verifiers/check_gate_registry.py --rev 9264baaa…` | `74 of 74; phantom 0`, rc 0 (`base-registry.txt`) |
| `python3 -B verifiers/check_assertion_floors.py --self-test` | rc 0 (`base-floors-selftest.txt`) |
| `python3 -B verifiers/check_tip_battery.py --rev 9264baaa…` | `guards 4 of 5; tip battery exit 0: 3 of 6`, rc 1 — named red: guard `instrument-pin` FAIL (blob `c10c0f10…` unpinned; r90 bump left the admission out), gates checklist/integrity/corpus_independent red, carried (`tipbattery-before.txt`) |
| `python3 -B verifiers/verify_skill_checklist.py --json` | rc 1, `governance.citation_resolves` carried (`base-checklist.txt`) |
| `python3 -B verifiers/verify_corpus_integrity.py --json` | rc 1, carried DRIFT set (`base-integrity.txt`) |
| `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt …` | carried reading (`base-d5v3.txt`) |
| `python3 -B verifiers/check_sibling_census.py … --province PROVINCE.md` | carried red, province rows mismatch (`base-sibling.txt`) |
| sources census | exit 0, 187 rows (`census-before.txt`) |
| `SKILL.md` size (Q78) | 600 lines / 92,672 B / 165 lines > 120 chars / longest 1491 at line 518 (`base-skill-size.txt`) — NO SKILL.md edit this round: no registry row is added (both claims close on existing instruments), the 600-line ceiling cannot absorb a row add |

## Touch list (Q73 sweep receipt `receipts/q73-sweep.txt`)

- `verifiers/check_mutation_battery.py` — self-test arms, PROBES third target, self-test pin
  updates; NOT in the tip battery's `BATTERY` list (no instrument-pin), not pinned by any
  counter (sweep committed).
- `verifiers/fixtures/mutation-battery/manifest.tsv` — exactly +3 kill rows.
- `verifiers/check_assertion_floors.py` — cap 120→360, `MEASURED_SELFTEST_S`, the Q39
  arithmetic arm, the over-cap/sub-cap regression arms, docstring stale round-56 arithmetic
  updated to the round-91 measurement, `floors_guard` floor value in both tables. This file IS
  battery-listed: the same change appends its new blob to `INSTRUMENT_PINS` in
  `verifiers/check_tip_battery.py` (pointer comment names this plan).
- `verifiers/check_tip_battery.py` — `INSTRUMENT_PINS` append only.
- `verifiers/check_freeze_gate.py` — ladder repair + one self-test arm; not battery-listed.
- `verifiers/floors-registry.json` — `floors_guard` floor value only.
- `verifiers/fixtures/round-91/` — the controls' fail-closed sims.
- `plans/round-91.md`, `plans/round-91-controls.md`, `LOG.md`, `corpus/SOURCES.md` (S262, S263,
  ≥1 rejection row), `corpus/knowledge/*round91*`, `corpus/lessons/round-91.md`,
  `corpus/README.md` (index rows for the new corpus files; append-only Frontier notes),
  `SCORECARD.md` (r90 routed defect 2: append-only annotation naming
  `.ufo/waves/round-90/w1/ExecBattery/battery-selftest.txt` as the real self-test path; the
  round-91 section), `PROVINCE.md` § Core (r90 routed defect 3: the mutation battery joins the
  executable-instruments bullet), wave evidence under `.ufo/waves/round-91/`.
- NO edit to `SKILL.md`, to any `corpus/lessons/round-*-verifier-spotcheck.md` (the tip
  battery's spotcheck-identity guard pins them), to `.ufo/state/`, `MANIFEST.json`,
  `scripts/`, `templates/`, sibling repos, or `/home/vgpnk/Projects/shokuknow`.

## Frontier step (§2b)

- SOURCES: S262 and S263 opened this round by the scout seat; at least one rejection row
  (reason + flip). Census before→after: 187 → 189 expected; both commands pasted in the report.
- Mistake mined into `corpus/lessons/round-91.md` `## Mistakes`: the instrument-pin admission
  gap (class `landing`: a battery-listed instrument changed without the pinned-blob admission;
  evidence `receipts/tipbattery-before.txt` guard line; captured-by: Q73's pre-freeze sweep —
  the r90 touch list named the floors bump but not its `INSTRUMENT_PINS` consequence; fix:
  the admission lands with C2 leg A(d), and this plan's Q73 sweep names `INSTRUMENT_PINS`
  explicitly).
- Sourced claims: C1 cites S262; C2 cites S263.
- Assimilation: none — L0 `kotoba | round-88` (renumber-or-retire; 55 measured collisions)
  stays open; the package stays unadopted.
- Considerthese: no proposal implemented this round — both claims are instrument-deepening with
  frozen predicates; proposal 3 (description self-audit round shape) stays carried because it
  needs a SKILL.md-description rewrite the 600-line budget cannot absorb (`base-skill-size.txt`).
- The kotoba slice of the absent-defect register stays NOT adopted and NOT verdict-landed
  (L0-blocked), carried, not silently dropped.

## Wave shape

ONE v1 wave `r91-w1` of 13 seats under policy v1 (band 8–16). Build seats (write patches, never the lane): ExecBatteryArms, ExecFloorsCap, ExecLadder (executors), ScoutSources (scout), ScribeCorpus (scribe). Connector: ConnectorOverlap (1, ≤ 2). Attack seats (policy attack roles reviewer, critic, mutation-tester, labrat): ReviewerBattery, ReviewerRepairs, CriticClaims, MutTesterBattery, MutTesterRepairs, LabratLadder = 6/13 ≈ 46 % (≥ 25 %). Sentinel: SentinelScope (scope and safety, non-attack). L2 floor roles met (executor ×3, scribe, scout, reviewer ×2, critic, connector). The L1 holds the §3 planner seat — the validator excludes `planner`, disclosed standing deviation. Writers never touch the lane: each writes `<Seat>.patch` in its wave dir; the L1 integrates the three code patches and the scribe patch after the build handoffs. Attack seats build the candidate in their own scratch clone from base plus those patches. Residual calls: none planned.
