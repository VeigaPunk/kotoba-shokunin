# Round 97 — kotoba (Linux host, omp) — plan

Author: KotobaR97 (L1, attempt 1). Round: 97. Base: lane tip at round start
`fa1bebae33e6b0ab4e36b9ba73ff7d4c5d610520` (branch `master`, local == remote, `jj-lane.sh state`:
`ahead=0 behind=0 tracked=0 untracked=0`).
Instrument commits: `7c01b10d54fbdcd97dd9ba06fe0954828e8a880f` (first cut) and
`94a1021762a888d8a360ba6efa759372cef392fb` (the measured bytes) — the v5 counter
`verifiers/fixtures/round-97/selftest-kills.py` and the C2 runner
`verifiers/fixtures/round-97/forgery-controls.py` (sha256 in every receipt header under
`.ufo/waves/round-97/receipts/`). Freeze commit: **this commit** — the plan and the pre-data receipts,
all taken with the committed instrument bytes of `94a10217`. Every landing measurement names a
committed lane revision.

**Pre-freeze instrument amendment (before any seat; receipts kept in `receipts/predraft/`).** At the
first cut, `forgery-controls.py v5-as-v4` read `forgeries refused 2 of 3`, not 0 of 3: g7 and g8 hold
the comment decoy by recognising the round-96 marker `# r96-decoy`, and the first cut used
`# r97-decoy` under `--rules v4` too, so the cause control was confounded by a marker rename (a
forger detail one line can adapt), not by rules 4–6. `94a10217` makes `--rules v4` use the v4 marker
so it reproduces v4 exactly; under the default v5 rules g7/g8 are refused with
`killed 0 of 11` (isolation: no marker ever survives to a later run), which does not depend on the
marker.

Both claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-97-addendum-*.md` BEFORE any
scored reading.

## Inherited state resolved at freeze

- Lane clean at base; no earlier attempt of round 97 (`.ufo/watchdog.log`: one
  `launch kotoba round=97 … attempt=1`, no `lane-dead-no-report kotoba round=97`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-96-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  - 1 (frozen receipt `round-96/receipts/sources-opened.txt` line 12: S272 quote "19 words", measures 22)
    → a named correction entry in `corpus/lessons/round-97.md` § Corrections pointing at the receipt
    (append-only; the round-96 receipt stays frozen).
  - 2 (v4 counter reads MET on g3/g7/g8, addendum A3) → **this round's C2**.
  - 3 (dispatch-checker survivors: MutTesterDispatchR96's 15, the sweep's 7 non-target) → **this
    round's C1** (13 non-equivalent survivors frozen as `CLAIMS["c1"]`; the three named equivalents
    m09/m15/m16 are excluded with their reasons, see § C1).
  - 4 (counter exit ladder A4; round-95 m08/N4) → A4 is v5 rule 7 (not claimed; a reviewer item
    probes it); m08/N4 carried.
  - 5 (three long-standing red gates; tip battery flat 280 s floors cap) → carried, measured at landing.
  - 6 (wave-evidence growth from saved HTML, 1.94 MB in round 96) → wave context forbids committing
    full source HTML; sources are stored as digest + line excerpt (`receipts/sources-opened.txt`).
  - 7 (prompt-commit attribution) → orchestrator-side, not lane-fixable.
- Round-96 planned row (SCORECARD § planned, "Round 97 planned"): v5 counter on committed g3/g7/g8
  worlds → C2; next survivor set → C1; exit ladder → v5 rule 7.

## Counting commands (frozen at the instrument commit)

- **C1:** `python3 -B verifiers/fixtures/round-97/selftest-kills.py c1 <rev>` (v5; the header is the
  specification). Rules 1–3 are the v4 rules; v5 adds 4 isolation (fresh clone, TMPDIR, HOME,
  XDG_CACHE_HOME per run), 5 mirror run (mutant text on disk; KILLED iff blind AND mirror are
  REPORTED-FAILURE), 6 honest bracket (three honest runs: first, last, random interior; other runs
  shuffled, seed printed), 7 exit ladder. `--rules v4` reproduces the round-96 rules for separability.
- **C2:** `python3 -B verifiers/fixtures/round-97/forgery-controls.py {v4|v5|v5-as-v4} <rev>` — reads
  the counter bytes at `<rev>` with `git show`, rebuilds the committed round-96 forgery worlds
  (`.ufo/waves/round-96/w1/ExecCounterForgeryR96/<world>.patch` on the round-96 freeze `679775ab`,
  identity `forgery`, scratch only) and runs the counter on them.

## Claim C1 — depth (lowest owned non-retired axis, score 9) — the dispatch-prompt checker's self-test kills thirteen more frozen survivors

Surface moved: `verifiers/verify_dispatch_prompts.py --self-test`, the executable proof of SKILL.md
§ Dispatch-prompt fidelity checklist boxes `dispatch.04` / `dispatch.08`. The round-96 arms closed
t01..t11 and nothing else (MutTesterDispatchR96 F1: 15 of 19 new mutants survive, 12 with
differential witnesses). C1 adds behavioural arms for the lane-identity scope (fleet-root lanes known
by `.report-baseline` or legacy `.round`, a FILE named `<lane>-shokunin`), the "missing state source is
never a pass" invariant (empty / unreadable baseline), the check-level FAIL headline (no arm asserted
`status == "FAIL"`), and the extraction edges (sentence-final `.`, `<>`, `round-` prefix, `round7`,
the per-file note, no-report dispatch.08).

- **Predicate (frozen; the same sentence as the counter header):** `<C>-PREDICATE-MET` iff (honest)
  every honest run is CLEAN; (targets) every target mutant applies and is KILLED; (positive) the
  positive mutant applies and is KILLED; (guard) every target's comment decoy and code decoy HOLDS.
- **Frozen mutants** (`CLAIMS["c1"]` of the v5 counter): t01-rstrip-dot, t02-empty-baseline,
  t03-fleetroot-stem-pass, t04-fleetroot-no-baseline, t05-placeholder-empty-angle,
  t06-sibling-file-as-lane, t07-report-regex-noprefix, t08-role-regex-nospace, t09-file-note-dropped,
  t10-unreadable-as-baseline, t11-lane-kind-legacy-dropped, t12-finish-single-fail-na,
  t13-noreport-08-pass; positive p00-md-not-stripped. Excluded as equivalent (MutTesterDispatchR96
  § Equivalent mutants): m09 (reason text unobserved by any verdict), m15 (dead second
  `has_placeholder` conjunct), m16 (unreachable `.`/`..` skip). m17 is a RUN-ERROR class (F6), not a
  survivor.
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13`.
- **Do-nothing control (pre-data, `receipts/redbefore-c1-base.txt`):** the counter at the base →
  `C1 targets killed 0 of 13`, `C1-PREDICATE-UNMET`, rc 1 (every target CLEAN in both blind and
  mirror runs). Same under `--rules v4` (`receipts/redbefore-c1-base-rulesv4.txt`).
- **Positive controls (pre-data):** `r96c1` at the base → MET (`receipts/poscontrol-r96c1-base.txt`);
  `r95c1` at the base → MET (`receipts/poscontrol-r95c1-base.txt`) — v5 does not refuse honest arms.
- **Separability:** C1 is also readable under `--rules v4` (the round-96 rules), so it does not depend
  on C2's hardening; the landing records both readings.
- **Kill rule:** unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen anchor no longer
  matches (could-not-evaluate); if `selftest-kills.py r96c1 <rev>` or `r95c1 <rev>` stops reading MET;
  if `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` stops reading `boxes proven 2` rc 0;
  or if production code of `verify_dispatch_prompts.py` outside `self_test()` and its self-test
  helpers changes. A miss is an honest stop, never a narrowed target.

## Claim C2 — consistency (calibration sub-axis, score 10) — the kill counter refuses the three round-96 forgery classes that read MET with no behavioural arm

Surface moved: the lane's kill-counter instrument (v4 → v5). The round-96 counter reads
`C1-PREDICATE-MET` on three committed forgery worlds that carry no behavioural arm (round-96
addendum A3): g3 recompile-compare, g7 stateful fake (TMPDIR marker), g8 clone marker.

- **Predicate (frozen; the same sentence as the runner header):** `C2-PREDICATE-MET` iff forgeries
  refused 3 of 3 AND honest held 2 of 2 (h1: the round-96 table at the round-96 landing `801dd9bc`;
  h2: the round-95 table at `<rev>`). g2b (guard-aware code-object sniffer) is reported as a disclosed
  bound and is not scored.
- **Target:** `forgery-controls.py v5 <landing rev>` → `C2 v5: forgeries refused 3 of 3; honest held 2 of 2`,
  `C2-PREDICATE-MET`, rc 0.
- **Do-nothing control (pre-data, `receipts/c2-before-v4.txt`):** the lane's counter before this round
  (v4, unchanged) → `forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`, UNMET rc 1.
  **Cause control (`receipts/c2-v5-as-v4.txt`):** the v5 file with `--rules v4` → refused 0 of 3: the
  refusal comes from rules 4–6, not from a table or path change.
- **Pre-data reading of the target command (`receipts/c2-v5.txt`):** recorded at the instrument commit;
  the landing re-reads it at the landing revision.
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET` rc 0; if either honest world
  stops being held; or if the v5 counter at the landing revision differs from the instrument commit
  bytes (an in-round counter change after scoring is not this claim). A new forgery world a seat builds
  that reads MET under v5 is a disclosed finding, not a rescue and not a narrowing.
- **Sourced:** S273 (opened this round, `receipts/sources-opened.txt`): Bazel Test Encyclopedia,
  https://bazel.build/reference/test-encyclopedia, HTTP 200, 223640 B, sha256 `6b07e08f…5346`, § Test
  interaction with the filesystem (HTML line 656): "Tests should create files only within the
  directories specified by $TEST_TMPDIR and $TEST_UNDECLARED_OUTPUTS_DIR (if set). These directories
  will be initially empty." (21 words, HTML lines 659–661) — grounds rule 4 (every run gets a fresh,
  initially empty TMPDIR and HOME; HOME = TEST_TMPDIR is the encyclopedia's recommended value, line 559)
  and the disclosed bound (state outside the per-run dirs, line 622: no constant path is exclusive).

**Disclosed bounds (stated, not claimed):** g2b remains MET under v5 (no cheap counter-side rule;
reviewer source check stands); state outside the per-run directories survives isolation and only the
honest bracket stands against it; the counter's mutant set is frozen, so killing it is not killing
every mutant.

## No-harm battery (landing, at the committed landing revision)

v5 `r96c1` and `r95c1` (MET); round-96 `selftest-kills.py c1|r95c1 <rev>` (MET); round-95
`selftest-kills.py c1|r94c1`; round-93 `c1-killpin-rev.sh`; round-92 `controls-run.sh`; gate registry
`check_gate_registry.py --rev <rev>` (base 74 of 74); `check_assertion_floors.py --self-test`;
`verify_dispatch_prompts.py --box-proof` (boxes proven 2) and its live run over the fleet prompts
(verdict lines equal at base and landing); tip battery; census rc 0 (base 34 W04); SKILL.md byte-identical.

## Frontier step

Row S273 (above) is opened this round and grounds C2. Same-round rejects recorded in the lesson Gate.
Mined mistake: `shared-state-between-scored-runs` — evidence round-96 addendum A3 and
`.ufo/waves/round-96/w1/ExecCounterForgeryR96.md` F1 (g7/g8 MET with zero arms); captured-by: none
(no committed stateful control world existed); fix: v5 rules 4–6 with committed g7/g8 controls,
shown able to fail — `forgery-controls.py v5-as-v4` (the fix switched off) reads refused 0 of 3
(`receipts/c2-v5-as-v4.txt`).

## Wave

One v1 wave `r97-w1`, 11 seats: executor 2 (C1 arms; v5 forgery attack), scout 1, scribe 1,
connector 1, reviewer 2, mutation-tester 2, critic 1, sentinel 1 (attack 5 of 11). The validator
rejects `planner`; the L1 holds the §3 planner seat; the connector's overlap scan carries the planning
data-walk.
