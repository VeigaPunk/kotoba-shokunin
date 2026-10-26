# ExecBatteryFix — C3 / M127: cause, red-before, repair draft (round 73, wave 1)

**Verdict.** The L1's cause is **confirmed** at base `072048f` — the counter derives the *lane itself* as the fleet
root from `--repo .` — with one refinement that sharpens the mechanism: because the derived entries are relative
paths, the sandbox links are *self-referential* (`../.ufo -> '.ufo'`, ELOOP), not lane-pointing. The repair is a
two-site patch in `verifiers/check_tip_battery.py` (+14/−2, deliverable `fix.patch`, sha256 `49c53626…`): anchor
`--repo`/`--fleet` before deriving the fleet root, and send "fleet root == the lane" down the counter's existing
could-not-evaluate channel (exit 2). Same command string before and after, only delta = the patch: base reads
`2 of 6` with floors+checklist exit 1; patched reads `4 of 6` with floors+checklist exit 0 in two fresh fleet
sandboxes, matching the hand runs gate-for-gate. Exit stays 1 at base for two causes outside this repair: the
corpus-integrity/independent red on the unindexed `round-72-verifier-spotcheck.md` (ExecIndexBaseline) and the
`instrument-size` guard (plan addendum before C3 data).

All seat work stayed inside `build/ExecBatteryFix/` and throwaway sandboxes; no lane file was modified.

## 1. Cause — confirmed, mechanism refined

Base blob identity: `git show 072048f…:verifiers/check_tip_battery.py` sha256 `7e42ab55…` equals the live
`verifiers/check_tip_battery.py` sha256 `7e42ab55…` — the counter did not change between base and `HEAD` (`ac8fc59`).

Probe (cwd = a fleet-shaped base sandbox of `072048f`, built as the contract's `build_sandbox` construction):

```
$ python3 -B probe_fleet_root.py 072048fa8e8a52c707d25f7079772fa317244eb7
== form A (documented r72 invocation): --repo '.'
   repo='.' fleet='.'  fleet==repo:True
   ../.ufo is a symlink -> '.ufo' (exists=False)
   ../.ufo/reports/round-7/kotoba.md exists=False
   symlinked entries (14): .git .gitignore .ufo AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md
== form B (absolute lane path): --repo '/tmp/k73fleet-ExecBatteryFix.gNP4/kotoba-shokunin'
   repo='/tmp/k73fleet-ExecBatteryFix.gNP4/kotoba-shokunin' fleet='/tmp/k73fleet-ExecBatteryFix.gNP4'
   fleet==repo:False
   ../.ufo is a symlink -> '/tmp/k73fleet-ExecBatteryFix.gNP4/.ufo' (exists=True)
   ../.ufo/reports/round-7/kotoba.md exists=True
   symlinked entries (47): .devin .gitignore .jj .omp .scratch .tower .ufo .ufo-scratch
```

Line pointers: `verifiers/check_tip_battery.py:609-610` (`repo = Path(args.repo)` / `fleet = Path(args.fleet) if
args.fleet else repo.parent`; the L1 cites `:610`, `:609` is the other half of the same derivation).
`Path(".").parent` is `Path(".")` (observed above), so `fleet == repo`; then `:181-183`
(`(parent / entry.name).symlink_to(entry)`) stores the *relative* entry name as the link target, which resolves
relative to the link's own directory — a self-loop, so `../.ufo` is not even the lane's `.ufo`.

First failing line, from the instrumented RED run's saved gate stdout
(`red-gates-repo-dot/verify_skill_checklist.out:10`):

```
FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k72-tip-0ja5fp44/kotoba-shokunin
```

(13 words, whole line.) The second FAIL is the same class on the governance citations — `evaluated 1283 —
correction LOG.md:2619 …` with 32 more `../.ufo/...` tokens (line >25 words: tail dropped after the first
clause). The citation is the one at `SKILL.md:558`; the fleet copy
`/home/vgpnk/Projects/shokunin/.ufo/reports/round-7/kotoba.md` exists, the lane copy does not.

`check_assertion_floors.py` is downstream, not an independent red: `:622-623` runs each instrument with
`--self-test`, `cwd=repo` (the sandbox lane), and the checklist's self-test reads the live tree's `../.ufo`
citations. Observed at one rev in three sandbox shapes (base counter, same `072048f`):

```
form A: --repo '.' -> fleet='.'; verify_skill_checklist.py exit 1
   first failing line: FAIL trigger.citation_resolves: evaluated 187 — line 558: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/k73gate-oa4y0vtd/kotoba-shokunin
   verify_skill_checklist.py --self-test exit 1
form B: --repo '<P>/kotoba-shokunin' -> fleet='<P>'; verify_skill_checklist.py exit 0
   verify_skill_checklist.py --self-test exit 0
form C (absolute lane as its own fleet root): exit 1; --self-test exit 1
```

and floors printed `FAIL checklist observed=1863 floor=1863 self_test_failures=2`. So the *gate* is right (form B
green at the same rev) and the *counter's derivation* is wrong: the repair belongs in the counter.

Frozen-predicate invocation is not the broken one — observed from the sandbox:
`check_tip_battery._default_lane()` → `repo=<sandbox lane> fleet=<sandbox>`. The r72 receipt's `4 of 6` (same two
gates red, the other four green) is [INFERENCE] the same cause at r72, whose corpus index was still consistent;
not re-run here.

## 2. RED-BEFORE

Verbatim base counter, the receipt's command and the command GREEN re-runs (cwd = a fresh fleet sandbox of `072048f`):

```
$ python3 -B verifiers/check_tip_battery.py --rev 072048fa8e8a52c707d25f7079772fa317244eb7 --repo .
gate verifiers/check_gate_registry.py exit 0 wall 0.7s
gate verifiers/check_assertion_floors.py exit 1 wall 80.4s
gate verifiers/verify_skill_checklist.py exit 1 wall 2.5s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.7s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.9s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
wall 86.6s
tip battery exit 0: 2 of 6
exit=1
```

This reproduces the committed `receipts/c3-base-battery-counter.txt` gate-for-gate (that receipt's floors wall,
128.1 s, is load; the verdicts are identical). Saved: `red-verbatim-base.txt`.

Instrumented RED (base blob imported unchanged; wrapper only captures each gate's stdout/stderr):

```
$ K73_GATE_OUT=…/red-gates-repo-dot python3 -B instrumented_counter.py --rev 072048f… --repo .
instrument: repo='.' fleet='.' fleet==repo=True
… tip battery exit 0: 2 of 6        exit=1  wall 50 s
```

## 3. Fix delta

`build/ExecBatteryFix/fix.patch` — 32 lines, 1770 B, sha256 `49c53626…`, one file, +14/−2. Applied with
`git apply -p1` to a scratch copy of the base blob it reproduces `fixed_counter.py` byte-for-byte
(sha256 `1d479d2d…`, `cmp` clean).

1. `main()` `:609-610` → `repo = Path(args.repo).resolve()` and
   `fleet = Path(args.fleet).resolve() if args.fleet else repo.parent`. Anchoring both arguments fixes the
   derived root *and* removes the relative-link-target class for `--fleet` as well.
2. `build_sandbox()`, after the two `is_dir` checks → `raise EnvError("the fleet root is the lane itself …")`
   when `repo.resolve() == fleet.resolve()`. A fleet root equal to the lane cannot be fleet-shaped (its `../`
   would reach the lane's own tree), so it takes the counter's existing could-not-evaluate channel: exit 2, never
   a battery reading.

Untouched: the six gate commands, `BATTERY`, `BASE`, the guards, the pins, the argument names, the printed
frozen line. The patch adds one comment block per site naming M127 and the mechanism.

## 4. GREEN ×2 — the fixed counter, twice, fresh sandboxes

Each run: fresh `mktemp -d` fleet sandbox at `072048f`, `git apply -p1 fix.patch`,
`git diff --numstat` = `14  2  verifiers/check_tip_battery.py`, then the identical RED command string.

* run 1: `exit=1 wall=88.6s`, `gate verifiers/check_assertion_floors.py exit 0 wall 83.0s`,
  `gate verifiers/verify_skill_checklist.py exit 0 wall 2.4s`, integrity 1, independent 1, registry 0, sweep 0,
  `tip battery exit 0: 4 of 6` (`green-1.txt`).
* run 2 (fresh sandbox): `exit=1 wall=87.9s`, floors exit 0 wall 77.8 s, checklist exit 0 wall 3.1 s,
  integrity 1, independent 1, `tip battery exit 0: 4 of 6` (`green-2.txt`).

Agreement reached: the counter's per-gate verdicts now equal the hand runs at the same rev — checklist and floors
green in a fleet-shaped sandbox, integrity/independent red for the index defect. Before the patch the counter
disagreed with those hand runs on exactly the two fleet-root gates.

Counter self-test (its own guard, not a lane gate): patched `python3 -B verifiers/check_tip_battery.py --self-test`
→ exit 0, `self-test: 0 failure(s) over 42 assertions`, wall 2 s (`self-test-fixed.txt`).

Guard case: patched counter, `--repo . --fleet .` → `exit=2`,
`could-not-evaluate: the fleet root is the lane itself (<lane>); pass the directory that holds the lane`. Before
the patch that shape was the silent `2 of 6` (instrumented line `fleet==repo=True`); form C above is the resolved
but unguarded equivalent at gate level, observed red. The guard removes a wrong *reading*, not a red gate.

## 5. Still red, and its owner

`verify_corpus_integrity.py` and `verify_corpus_independent.py` remain exit 1 at base: DRIFT keys
`corpus.index.unindexed` (observed=1: `corpus/lessons/round-72-verifier-spotcheck.md`),
`corpus.pointers.report_total` (observed=95 vs 93) and `corpus.pointers.commit_unresolvable` (3); the independent
gate independently derives the same three. That needs an index row for the non-author r72 spot-check and a
baseline re-record — **not touched here**, left to `ExecIndexBaseline` as assigned.

`FAIL guard instrument-size: instruments gain 76 lines > 40` is orthogonal to this cause (it measures the six
battery instruments against r72 base `c69711e`); the plan re-sets it by addendum before C3 data. Until both land,
the counter's exit stays 1 at base even though the M127 disagreement is gone — the C3 predicate (`6 of 6`) is the
tip measurement after both, not a base measurement.

## 6. Operability / risk

* Blind spot that let this ship: the counter's self-test always passes an absolute `--repo` and an explicit
  `--fleet` (`_drive`, `:433`), so no fixture exercises a relative `--repo`; my fix is not anchored by a
  self-test case. A true discriminator needs a fleet root carrying `../.ufo` content the lane lacks (a stub gate
  reading `../.ufo/<marker>`); adding it would raise the counter's assertion count (floors requires a minimum, so
  safe). Left out to keep the delta one-cause — say the word for a second patch.
* Walls are load-dependent, verdicts are not: floors measured 47 s / 78 s / 80 s / 83 s in my runs and 128.1 s in
  the committed receipt, with identical exit codes.
* The frozen predicate's command omits `--repo`, while the base and r72 receipts pass `--repo .`; both forms are
  equivalent after the patch. The predicate sentence needs no change.
* Both `resolve()` calls also make the sandbox construction independent of the caller's cwd, which is what makes
  the patch safe to run from `.ufo/waves/.../build/<seat>/` too.

## 7. Evidence (all under `build/ExecBatteryFix/`)

| file | what it is |
|---|---|
| `fix.patch` | deliverable, against base `072048f` (`a/verifiers/check_tip_battery.py`) |
| `base_counter.py` | byte copy of `git show 072048f…:verifiers/check_tip_battery.py` (sha `7e42ab55…`) |
| `fixed_counter.py` | base + `fix.patch`, byte-identical to a `git apply` of the patch (sha `1d479d2d…`) |
| `instrumented_counter.py` | unmodified base counter imported, gate stdout/stderr captured |
| `probe_fleet_root.py` | prints the derived repo/fleet and the sandbox's `../.ufo` link for both forms |
| `probe_checklist_gate.py` | gate-level A/B/C discrimination plus `--self-test` exits |
| `red-verbatim-base.txt` | verbatim RED run, `2 of 6`, exit 1, wall 86.6 s |
| `red-base-repo-dot.txt` | instrumented RED run, `2 of 6`, exit 1, wall 50 s |
| `red-gates-repo-dot/` | the six gates' stdout/stderr for that run (failing lines quoted above) |
| `green-1.txt`, `green-2.txt` | the two patched runs, `4 of 6`, floors/checklist exit 0 |
| `self-test-fixed.txt` | patched counter self-test, 42 assertions, 0 failures |
| `gate-probe-forms.txt`, `gate-probe.txt` | earlier/final gate probes (form A/B/C) |

Scratch fleet sandboxes (`/tmp/k73fleet-ExecBatteryFix.*`, `/tmp/k73patch.*`) were deleted; every git write was a
working-tree `git apply` inside those sandboxes, no commit anywhere.

## 8. Tooling

None installed, upgraded or downgraded for this seat.
