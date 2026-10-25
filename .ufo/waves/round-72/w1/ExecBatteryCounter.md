# ExecBatteryCounter — C3 tip battery counter (wave 1 build)

Seat: ExecBatteryCounter (executor, C3). Deliverable:
`.ufo/waves/round-72/w1/build/ExecBatteryCounter/check_tip_battery.py` (556 lines,
executable). Verdict: **counter built, self-tested, and run on three honest and
three shortcut worlds; all receipts below are observed, never asserted.**

Frozen predicate (the same sentence as in `plans/round-72.md` § C3, in the
counter's docstring, and in this receipt):

```
python3 -B verifiers/check_tip_battery.py --rev <rev>  ->  prints "tip battery exit 0: N of 6", exit 0 when N == 6
```

## Q63 receipt — honest real world at the base (before any freeze)

Command (exactly the frozen form; `--repo` left at its default — the counter
resolves the lane as the nearest ancestor carrying `verifiers/` and
`SKILL.md`, so the draft path and an installed `verifiers/` copy both default to
the lane):

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
time python3 -B .ufo/waves/round-72/w1/build/ExecBatteryCounter/check_tip_battery.py --rev c69711ee08279609374d895bb0f3c8c18ccf15c9
```

Observed (final bytes; wall 41.5 s of output, 41.6 s process):

```
measured rev c69711ee08279609374d895bb0f3c8c18ccf15c9 in a fleet-shaped sandbox; base c69711ee08279609374d895bb0f3c8c18ccf15c9
guarded paths 568, deleted 0; floors 15 rows; instruments added 0 / deleted 0 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
guard instrument-size PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 1 wall 0.3s
gate verifiers/check_assertion_floors.py exit 1 wall 38.7s
gate verifiers/verify_skill_checklist.py exit 0 wall 1.4s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.2s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.5s
gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
wall 41.5s
tip battery exit 0: 2 of 6
counter exit=1
```

`tip battery exit 0: 2 of 6`, exit 1 — exactly the plan's do-nothing control
(measured by hand in the plan's table: registry 1, floors 1, checklist 0,
integrity 1, independent 1, sweep 0 → 2). The receipt precedes the freeze (Q63).

Second honest world, the lane tip `e61fd29` (plan freeze + wave-1 spec commits):
guards PASS, `tip battery exit 0: 2 of 6`, exit 1, wall 45.6 s. The wave-1
`.ufo` additions alter no gate and trip no guard.

## The counter and its guards

`BASE = c69711ee08279609374d895bb0f3c8c18ccf15c9`, `GATE_TIMEOUT_S = 280`,
`LINE_CAP = 40`, and `BATTERY` are pinned module constants, never read from
`--rev`. Sandbox construction is the r71 K69-11 pattern
(`verifiers/check_r69_routed_repairs_v2.py` lines 170–230): `git clone --shared
--no-checkout` into `<parent>/kotoba-shokunin`, every other fleet-root entry
symlinked into `<parent>`, then `git checkout -q <rev>`. Guards run on the
clone's committed bytes; the six commands run from the clone root with 280 s
each; a timeout/absent script is counted as not-exit-0 (never as exit 2). Exit
2 only when the sandbox cannot be built (clone/checkout failure, fleet root
unreadable, pinned base absent from the clone) — covered by self-test arms.

Guard readings (documented choices, none changing a frozen sentence):

- **no-deletions**: no path under `corpus/` or `verifiers/`, and no
  `SKILL.md`, tracked at the base is absent at `<rev>` (568 guarded paths at
  base).
- **floors**: no row of `verifiers/floors-registry.json` is lower than at the
  base, and no base row is dropped (15 rows at base).
- **instrument-size**: the six instruments gain at most 40 lines total over the
  base **and lose at most 40**. The plan bounds additions; the same cap on
  deletions is what makes the plan's own control — "replace
  `check_gate_registry.py` by a stub `sys.exit(0)` (must fail the size cap)" —
  actually fail: a two-line stub *adds* two lines and deletes ~380, so an
  additions-only cap cannot see it (demonstrated below).
- **spotcheck-identity**: every `corpus/lessons/*-verifier-spotcheck.md`
  present at the base is byte-identical (same blob SHA) at `<rev>` (26 base
  files). A file *added* at `<rev>` is reported as INFO, never a failure: the
  round's own spot-check lesson may land at the tip, and any deletion of a base
  file is already caught by no-deletions.

## Self-test

`python3 -B check_tip_battery.py --self-test` drives `main()` on tiny isolated
local git worlds (stub gates, never the lane): 1 satisfying world (exit 0,
last line exactly `tip battery exit 0: 6 of 6`), 1 broken world per guard
(deletion, floor lowered, +41 added lines, −60 via stub replacement, spot-check
edit), 1 broken world per gate (each stub exits 1 → `5 of 6`), and 2
could-not-evaluate worlds (unknown rev, missing fleet root → exit 2).

Observed: `self-test: 0 failure(s) over 37 assertions`, exit 0 (0.8 s).

Mutation calibration — each of the five mutants of the counter makes the
self-test fail, proving the arms bind:

| mutant | self-test result |
|---|---|
| `LINE_CAP = 1000` | 4 failures (size + stub worlds read exit 0) |
| deletion guard disabled | 2 failures (deletion world reads exit 0) |
| floors comparison disabled | 2 failures (floor world reads exit 0) |
| spot-check identity disabled | 2 failures (spot-check world reads exit 0) |
| exit-1 counted as green | 12 failures (gate worlds read 6 of 6) |

## Real shortcut worlds (built in `--shared` clones of the lane; commits only
inside the clones)

1. **Delete the r71 spot-check lesson** (`b4c2766`). `git rm
   corpus/lessons/round-71-verifier-spotcheck.md` only. Observed: `FAIL guard
   no-deletions: corpus/lessons/round-71-verifier-spotcheck.md tracked at the
   base is absent at b4c2766…`, `FAIL guard spotcheck-identity: … absent at
   b4c2766…`; the deletion alone turns both corpus gates green → `tip battery
   exit 0: 4 of 6`, exit 1 (the guards bind; N alone would be 4).
2. **Lower a floor + stub the gate registry** (`912151d`). Checklist floor
   1862→1861 and `check_gate_registry.py` → `sys.exit(0)` (378 lines removed).
   Observed: `FAIL guard floors: row checklist floor 1861 < base 1862`,
   `FAIL guard instrument-size: instruments lose 377 lines > 40`; the stub
   gate exits 0 → `tip battery exit 0: 3 of 6`, exit 1.
3. **Bless the five DRIFT baseline values without indexing the file**
   (`dbb4c0b`). Set `corpus-baseline.json` expects to the observed values
   (tracked_files 133, unindexed 1, report_total 93, commit_total 41,
   commit_nonhash 2). Observed: gates all PASS, `tip battery exit 0: 2 of 6`,
   exit 1 — `verify_corpus_integrity.py` stays red because the two zero-mode
   checks ignore the baseline's `mode` cell: `DRIFT corpus.index.unindexed:
   observed=1 expected=0 / empty`, `DRIFT corpus.pointers.commit_nonhash:
   observed=2 expected=0 / empty` (7/9 checks pass). The plan's control holds.

No shortcut world reads 6 or exit 0 (kill-rule condition not triggered).

## Notes

- Dead code removed during build; `python3 -m py_compile` clean; the build dir
  holds only `check_tip_battery.py`.
- No tool installed or upgraded (generic-rules log: none). No pacman
  transaction attempted. No lane/committed file touched (`git status
  --porcelain` of the lane shows only other seats' untracked wave-1 files).
- Scratch (`/tmp/k72w1-ExecBatteryCounter.bpcN`, timing logs) deleted.
- Risks: the counter's 280 s per-gate timeout exceeds the 120 s contention cap
  by design; it runs alone (observed 41–47 s). The `--base` override exists
  solely for `--self-test`; any receipt using it prints `note: base override`
  and is distinguishable from a frozen run.
- Blockers: none.
