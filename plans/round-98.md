# Round 98 — kotoba (Linux host, omp) — plan

Author: KotobaR98 (L1, attempt 1). Round: 98. Base: lane tip at round start
`a33f262fc94e3cf27f3c935b5c53c1336bb94166` (branch `master`, local == remote, `jj-lane.sh state`:
`ahead=0 behind=0 tracked=0 untracked=0`).
Instrument commit: `a060b450a43673ebc54720a5192e99df188e80ce` — the v6 counter
`verifiers/fixtures/round-98/selftest-kills.py` and the C2 runner
`verifiers/fixtures/round-98/forgery-controls.py` (sha256 in every receipt header under
`.ufo/waves/round-98/receipts/`). Freeze commit: **this commit** — the plan and the pre-data receipts,
all taken with the committed instrument bytes of `a060b450`. Every landing measurement names a
committed lane revision.

Both claims are frozen here: predicate sentence, counting command, kill rule and target do not change
after any seat has scored (§9). An amendment is an L1 act via `plans/round-98-addendum-*.md` BEFORE any
scored reading.

## Inherited state resolved at freeze

- Lane clean at base; no earlier attempt of round 98 (`.ufo/watchdog.log`: one
  `launch kotoba round=98 … attempt=1`, no `lane-dead-no-report kotoba round=98`).
- No `corpus/lessons/operator-*.md`.
- `corpus/lessons/round-97-verifier-spotcheck.md` read in full. Routed defects dispositioned:
  - 1 (tip battery 3 of 6; `verify_skill_checklist`, `verify_corpus_integrity`,
    `verify_corpus_independent` red since round 96) → not claimed; a scout item re-measures each red and
    names its cause so the next round can dispose of it; the landing tip battery is a no-harm reading
    (red set must not grow).
  - 2 (g10 committed reference, g11 seeded replay read MET under v5) → **this round's C2** (v6 rules 8–9).
  - 3 (counter-rule mutants V4–V9 survive C2's worlds) → a mutation-tester item re-runs counter-rule
    mutants against the v6 counter and C2's five worlds; reported, not claimed.
  - 4 (MutTesterDispatchR97's 11 survivors) → **this round's C1** (the nine verdict-bearing ones).
  - 5 (counter exits with a traceback; floor 56 vs 105; t10 root dependence) → traceback: v6 rule 10
    (not claimed; a reviewer item probes it); floor and t10 carried.
  - 6 (t09 cosmetic mutant counted as a kill) → C1's frozen table excludes the two no-verdict survivors
    (m32 verdict-equivalent, m34 reporting-only) by rule, with the reason in the counter header.
  - 7 (S273 whole-page digest not reproducible) → this round's access records carry the HTTP code, size,
    sha256 AND a line excerpt (`receipts/sources-opened.txt`), so a re-open can verify by excerpt.
  - 8 (orchestrator-side) → not lane-fixable.
- Round-97 planned row (SCORECARD § planned, "Round 98 planned"): v6 counter with git-less per-run copy
  and minimal child env → C2; exception ladder → v6 rule 10; MutTesterDispatchR97's survivors → C1;
  assertion-floor raise → carried.

## Counting commands (frozen at the instrument commit)

- **C1:** `python3 -B verifiers/fixtures/round-98/selftest-kills.py c1 <rev>` (v6; the header is the
  specification). Rules 1–7 are the v5 rules; v6 adds 8 git-less world (`git archive` export, a
  reflink copy per run), 9 minimal child environment and non-dumpable counter, 10 total exit ladder.
  `--rules v5` reproduces the round-97 rules for separability.
- **C2:** `python3 -B verifiers/fixtures/round-98/forgery-controls.py {v5|v6|v6-as-v5} <rev>` — reads
  the counter bytes and the committed world patches at `<rev>` with `git show`, rebuilds each world on
  the round-96 freeze `679775ab` in a scratch clone (identity `forgery`, scratch only) and runs the
  counter's `r96c1` table on it.

## Claim C1 — depth (lowest owned non-retired axis, score 9) — the dispatch-prompt checker's self-test kills nine more frozen survivors

Surface moved: `verifiers/verify_dispatch_prompts.py --self-test`, the executable proof of SKILL.md
§ Dispatch-prompt fidelity boxes `dispatch.04` / `dispatch.08` and of its `--box-proof`. The round-97
arms closed t01..t13 and none of MutTesterDispatchR97's 15 new mutants beyond three (F1: 11 survive).
C1 adds behavioural arms for: the prompt-name regex end anchor, the dispatch.08 report-dir SET (two dirs),
the verdict lookup over a multi-file result, the box proof's two map-side checks (disposition, live
SKILL.md box hash), the box-hash fence close rule, the KIND of a state entry (a directory named
`<lane>.round`) and of a prompts-dir entry (a directory named like a prompt), and the `.MD` suffix.

- **Predicate (frozen; the same sentence as the counter header):** `<C>-PREDICATE-MET` iff (honest)
  every honest run is CLEAN; (targets) every target mutant applies and is KILLED; (positive) the
  positive mutant applies and is KILLED; (guard) every target's comment decoy and code decoy HOLDS.
- **Frozen mutants** (`CLAIMS["c1"]` of the v6 counter): t01-lane-suffix-unanchored (m20),
  t02-dirs-first-only (m22), t03-verdict-first-file (m23), t04-proof-disposition-unenf (m24),
  t05-proof-live-hash-unenf (m25), t06-fence-any-close (m26), t07-legacy-exists (m27),
  t08-prompts-include-dirs (m28), t09-md-uppercase (m31); positive p00-md-not-stripped.
  Excluded by rule (round-97 closure defect 6: no-verdict mutants are not kill targets): m32
  (verdict-equivalent) and m34 (reporting-only). Also excluded: m21 (RUN-ERROR class), m29/m30/m33
  (already killed at the base).
- **Target:** `C1-PREDICATE-MET`, exit 0, at the landing revision — tally
  `C1 targets killed 9 of 9 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 9 of 9; code decoys held 9 of 9`.
- **Do-nothing control (pre-data, `receipts/redbefore-c1-base.txt`):** the counter at the instrument
  commit (production and self-test bytes equal to the round base) → `C1 targets killed 0 of 9`,
  `C1-PREDICATE-UNMET`, rc 1. Same under `--rules v5` (`receipts/redbefore-c1-base-rulesv5.txt`).
- **Positive controls (pre-data):** `r97c1`, `r96c1`, `r95c1` at the base → MET
  (`receipts/poscontrol-*-base.txt`) — v6 does not refuse honest arms (git-less, minimal env).
- **Separability:** C1 is also read under `--rules v5`, so it does not depend on C2's rules 8–10; the
  landing records both readings.
- **Kill rule:** unmet if the landing reading is not `C1-PREDICATE-MET`; if a frozen anchor no longer
  matches (could-not-evaluate); if `selftest-kills.py r97c1 <rev>`, `r96c1 <rev>` or `r95c1 <rev>`
  stops reading MET; if `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` stops reading
  `boxes proven 2` rc 0; or if production code of `verify_dispatch_prompts.py` outside `self_test()`
  and its self-test helpers changes. A miss is an honest stop, never a narrowed target.

## Claim C2 — consistency (calibration sub-axis, score 10) — the kill counter refuses the two round-97 forgery classes v5 reads MET

Surface moved: the lane's kill-counter instrument (v5 → v6). The round-97 counter reads
`R96C1-PREDICATE-MET` on two committed worlds that carry no behavioural arm (round-97 addendum A1/A2,
`.ufo/waves/round-97/w1/ExecForgeryV5.md` F1/F2): g10 (compares its code objects with
`git show HEAD:<instrument>`) and g11 (replays the counter's schedule from `KOTOBA_R97_SEED`, measured
seeded).

- **Predicate (frozen; the same sentence as the runner header):** `C2-PREDICATE-MET` iff forgeries
  refused 5 of 5 (g3, g7, g8, g10, g11-seeded) AND honest held 2 of 2 (h1: the round-96 table at the
  round-96 landing `801dd9bc`; h2: the round-95 table at `<rev>`). g2b is reported as a disclosed bound
  and is not scored.
- **Target:** `forgery-controls.py v6 <landing rev>` →
  `C2 v6: forgeries refused 5 of 5; honest held 2 of 2`, `C2-PREDICATE-MET`, rc 0.
- **Do-nothing control (pre-data, `receipts/c2-before-v5.txt`):** the lane's counter before this round
  (v5, unchanged) → `forgeries refused 3 of 5` (g10, g11 MET), `C2-PREDICATE-UNMET`, rc 1.
  **Cause control (`receipts/c2-v6-as-v5.txt`):** the v6 file with `--rules v5` → refused 3 of 5: the
  refusal comes from rules 8–9, not from a table, marker or schedule change (v6 keeps v5's marker,
  replay variable and schedule).
- **Pre-data reading of the target command (`receipts/c2-v6.txt`):** recorded at the instrument commit;
  the landing re-reads it at the landing revision.
- **Kill rule:** unmet if the landing reading is not `C2-PREDICATE-MET` rc 0; if either honest world
  stops being held; or if the v6 counter or the runner at the landing revision differs from the
  instrument commit bytes. A new forgery world a seat builds that reads MET under v6 is a disclosed
  finding, not a rescue and not a narrowing.
- **Sourced** (opened this round, `receipts/sources-opened.txt`, access record with excerpt):
  - Python `subprocess` docs, Popen `env` (HTML lines 881–883): "these are used instead of the default
    behavior of inheriting the current process’ environment." (14 words) — grounds rule 9.
  - git-archive(1) DESCRIPTION (lines 1708–1710): "Creates an archive of the specified format
    containing the tree structure for the named tree, and writes it out to the standard output."
    (22 words) — grounds rule 8 (a tree, not a repository).
  - proc_pid_environ(5) (lines 90–91): "Permission to access this file is governed by a ptrace access
    mode PTRACE_MODE_READ_FSCREDS check" (15 words) — grounds the non-dumpable counter.

**Disclosed bounds (stated, not claimed):** g2b remains unrefused; state outside the per-run directories
survives isolation and only the honest bracket stands against it; `/proc/<ppid>/cmdline` names the
counter path, REV and REPO, so a forger that reads REPO's object store through it, or scans the
filesystem for the lane, is not refused by rule 8 (ExecForgeryV5 F1.3); the counter's mutant set is
frozen, so killing it is not killing every mutant.

## No-harm battery (landing, at the committed landing revision)

v6 `r97c1`, `r96c1`, `r95c1` (MET); round-97 `selftest-kills.py c1|r96c1 <rev>` (MET); round-97
`forgery-controls.py v5 <rev>` still reads its frozen 3-of-3 world set refused; round-96, round-95,
round-93 and round-92 pins as in round 97; gate registry `check_gate_registry.py --rev <rev>` (base 74 of
74); `check_assertion_floors.py --self-test`; `verify_dispatch_prompts.py --box-proof` (boxes proven 2)
and its live run over the fleet prompts (verdict lines equal at base and landing); tip battery (red set
not larger than base); census rc 0 (base 34 W04); SKILL.md byte-identical.

## Frontier step

Rows from `receipts/sources-opened.txt` (S277–S279 admitted, S280 rejected as redundant) ground C2.
Mined mistake: `measured-child-reads-counter-state` — evidence round-97 addendum A1/A2 and
`.ufo/waves/round-97/w1/ExecForgeryV5.md` F1/F2 (the counter handed the measured child its own
history and replay seed); captured-by: Q87 (isolation named clone/TMPDIR/HOME but not the history or
the environment); fix: v6 rules 8–9 plus a Q87 amendment row, shown able to fail —
`forgery-controls.py v6-as-v5` (the fix switched off) reads refused 3 of 5 (`receipts/c2-v6-as-v5.txt`).

## Wave

One v1 wave `r98-w1`, sized to the claims (see `.ufo/waves/round-98/r98-w1-spec.json`). The validator
rejects `planner`; the L1 holds the §3 planner seat; the connector's overlap scan carries the planning
data-walk.
