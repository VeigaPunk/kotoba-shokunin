Result: DONE — `verifiers/check_correction_sweep.py` was unregistered at the round-58 freeze; `ExecFloorsSweep.patch` registers it in `verifiers/floors-registry.json` and both in-file guard tables at floor 18 (the observed count at `3de87aad`), each frozen dropped-case mutant M08–M11 now reddens the guard (exit 1, `FAIL correction_sweep observed=17 floor=18`) while the sweep's own self-test stays green, and the companion `ExecFloorsSweep.integrated.patch` pins the floor at the lane's integrated count 25, measured green at HEAD `46b4a70`.

# R3, second guard — floored assertion count for the correction sweep

Read-only lane work; every run is in `/fast/scratch/hyaku/kotoba-r58/ExecFloorsSweep`. The clone
`…/ExecFloorsSweep` is at the freeze commit `3de87aad29e960c95ed35840442f424c48c29729` (worktree-only
edits; **no commits**, no sandbox commit hash to cite); `…/ExecFloorsSweep/apply-world` and
`…/ExecFloorsSweep/integrated-world` are throwaway clones at `3de87aa` and at the integrated lane HEAD
`46b4a70` (same discipline, no commits), and `…/ExecFloorsSweep/check-world` is a pristine `46b4a70`
clone used only for `git apply --check`.

## 1. Registration status at the freeze commit: NOT registered

- `verifiers/floors-registry.json:3` — `"instrument_total": 13,` with entries checklist,
  compare_harness_independent, corpus_independent, corpus_integrity, floors_guard, harness,
  harness_independent, pins, overlap_levers, surfaces, dispatch_prompts, sibling_census, alwayson.
  No `correction_sweep` entry.
- `verifiers/check_assertion_floors.py:151-166` (`EXPECTED_INSTRUMENTS`) — 13 names, no
  `correction_sweep`; `:191-220` (`INSTRUMENTS`) — the same 13 rows.
- The instrument exists and already prints a parseable summary:
  `verifiers/check_correction_sweep.py:278` — `print("%d failure(s) over %d assertions" ...)`.
- `grep -rn "correction_sweep" verifiers/check_assertion_floors.py verifiers/floors-registry.json`
  → `GREP_EXIT=1` (no match) on those bytes; the guard and registry files are byte-identical at
  `3de87aa` and at the integrated `46b4a70`, so the reading holds for both. The only
  `check_correction_sweep.py` mentions in `verifiers/` are `check_sweep_mutants.py` and
  `check_could_not_evaluate.py`, which do not floor it.

Observed count at the freeze bytes, measured before drafting (UTC window 08:09:36):

    $ cd /fast/scratch/hyaku/kotoba-r58/ExecFloorsSweep && python3 -B verifiers/check_correction_sweep.py --self-test
    0 failure(s) over 18 assertions
    EXIT=0

18 assertions = 15 `case(...)` arms + 3 CLI arms (unknown revision, git unavailable, refusing git).

## 2. Delivered patch

`.ufo/waves/round-58/build/ExecFloorsSweep.patch` — sha256
`61830536883ac672b958d09c248358dddc94f98c0edaad8ba329e566e5b2e13e`, 70 lines, two files,
`git diff --stat` = `15 insertions(+), 4 deletions(-)` (the four deleted lines are the docstring
floor-list line, the F6 comment line, the F6 fixture literal and the registry `instrument_total`
line; no removed logic).

- `verifiers/floors-registry.json`
  - `"instrument_total": 13` -> `14` (`:3`);
  - appended entry (after `alwayson`, matching the file's appended-new-row style):
    `"correction_sweep": {"floor": 18, "path": "verifiers/check_correction_sweep.py"}`.
- `verifiers/check_assertion_floors.py`
  - docstring floor list gains `correction_sweep 18` plus a round-58 sentence naming routed defect
    R3 and the M08–M11 class (`:10-13`);
  - `EXPECTED_INSTRUMENTS` gains `"correction_sweep": 18` (`:165`);
  - `INSTRUMENTS` gains
    `"correction_sweep": ("verifiers/check_correction_sweep.py", 18, r"(?m)^(\d+) failure\(s\) over (\d+) assertions$", 2, 1)`
    (`:218-219`) — the sweep's summary is the standard `(<failures>) failure(s) over (<assertions>) assertions`
    shape, so assertion group 2, failure group 1;
  - the guard self-test's F6 fixture anchor `'"instrument_total": 13'` -> `'"instrument_total": 14'`
    (`:802`) and its comment (`:798-799`). This literal is load-bearing: a stale value makes the F6
    swap land zero times and the guard's own self-test reddens.

Applied bytes (sandbox final state): `verifiers/check_assertion_floors.py`
`d2809db66a3024f8bca5f731b8b62bcd7ae01b7e2514b89a472bf20fd59403b5`;
`verifiers/floors-registry.json` `1226a9b2c1ecbe965a1042c41c07880a436c96b6104d48f8122e3a2f7aeac64d`.

Applicability at the freeze commit: a pristine clone of `3de87aa` (`apply-world`) ran
`git apply --check -v ../ExecFloorsSweep.patch` -> `Checking patch verifiers/check_assertion_floors.py...`
`Checking patch verifiers/floors-registry.json...`, `APPLY_CHECK_EXIT=0`.

Companion artifact: `.ufo/waves/round-58/build/ExecFloorsSweep.integrated.patch` (sha256
`46e78c30543993efcb20c1bfc932d82a34bcf4fddc535e43308b63963ab5b4ba`) — the same change with the floor at
the lane's integrated count 25, verified at HEAD `46b4a70`. §5 states which one to apply.

At `46b4a70` the L1's integration snapshot already tracks `.ufo/waves/round-58/build/ExecFloorsSweep.patch`
(blob `05daa22c…`, bytes equal to sha256 `6183053…`), while `verifiers/check_assertion_floors.py`
(`a17c3103…`) and `verifiers/floors-registry.json` (`c29a9238…`) are unchanged in the tree: the artifact is
committed, the change is not applied. This report and the integrated companion are new untracked files.

## 3. Runs, in order

**Before** (pristine `3de87aa`, UTC 08:09:40 -> 08:10:50, 70.05 s):

    $ timeout 900 python3 -B verifiers/check_assertion_floors.py
    PASS harness observed=10 floor=10
    ... 13 PASS lines, no correction_sweep row ...
    PASS alwayson observed=89 floor=89
    EXIT=0

**Patch, then guard's own self-test** (UTC 08:11:51):

    $ timeout 600 python3 -B verifiers/check_assertion_floors.py --self-test
    0 failure(s) over 165 assertions
    SELFTEST_EXIT=0

**After** (patched tree, UTC 08:11:51 -> 08:13:06, 74.42 s):

    $ timeout 900 python3 -B verifiers/check_assertion_floors.py
    PASS harness observed=10 floor=10
    ...
    PASS alwayson observed=89 floor=89
    PASS correction_sweep observed=18 floor=18
    WALK_EXIT=0

**Half-bump caught by the guard itself (transient, before the delivered bytes).** My first attempt
added the registry row but not `instrument_total`. The guard named it on both channels, unprompted:

    $ python3 -B verifiers/check_assertion_floors.py --self-test
    1 failure(s) over 165 assertions
    FAIL: mutation anchor lands exactly once (F6/total): got 0
    SELFTEST_EXIT=1
    $ python3 -B verifiers/check_assertion_floors.py
    FAIL registry size drift: instrument_total=13 but 14 entries in verifiers/floors-registry.json
    WALK_EXIT=2

The delivered patch is the corrected bytes; this is recorded because it is a live discriminator
for the bump-in-step rule, not because it survived into the deliverable.

## 4. The dropped-case mutants M08–M11 now fail — measured per mutant

Each frozen row from `verifiers/check_sweep_mutants.py:TABLE` was applied **in place** to the sandbox
`verifiers/check_correction_sweep.py` (its canonical path, exactly the counter's shape: a single
`case(...)` call removed, nothing else), then both instruments were run, then the file was restored
with `git checkout -- verifiers/check_correction_sweep.py` and its sha256 re-checked.

| Mutant (frozen desc) | sweep `--self-test` | floors walk | window (UTC) |
|---|---|---|---|
| M08 drop `r57 quote notes red` | `0 failure(s) over 17 assertions`, EXIT=0 | EXIT=1, `FAIL correction_sweep observed=17 floor=18` | 08:13:21–08:14:30 |
| M09 drop `r57 quote notes green` | same, EXIT=0 | EXIT=1, same FAIL line | 08:15:03–08:16:10 |
| M10 drop `r57 singular agent clause red` | same, EXIT=0 | EXIT=1, same FAIL line | 08:16:23–08:17:30 |
| M11 drop `r57 singular agent clause green` | same, EXIT=0 | EXIT=1, same FAIL line | 08:17:41–08:18:50 |

That is the discrimination the R3 defect lacked: the mutant's own self-test reads green
(`0 failure(s) over 17 assertions`, exit 0 — the surviving-mutant shape) and only the floor reddens
it. After M11 the sweep was restored and its sha256 equals the pristine baseline
`799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` (also
`git show HEAD:verifiers/check_correction_sweep.py`, byte-identical).

## 5. Floor value is integration-dependent — measured on the integrated tree

`ExecC2Arms`'s deliverable is already in this directory (sha256 `3fe7fc6e…`), and the lane has already
integrated the arms: at UTC 08:23:58 the lane HEAD is `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`, whose
`verifiers/check_correction_sweep.py` is `df66b485cc00a5058643b387882abe648d6e83b66d68a5865596e88515309c2f`
and whose self-test prints `0 failure(s) over 25 assertions`, exit 0. The lane's guard and registry are
still the freeze bytes (`a17c3103…`, `c29a9238…`), so the base patch applies there unchanged — a clone at
`46b4a70` passes `git apply --check -v ../ExecFloorsSweep.patch`, exit 0.

Measured counts and verdicts:

| tree | sweep count | floor | guard walk |
|---|---|---|---|
| freeze `3de87aa` + `ExecFloorsSweep.patch` | 18 | 18 | exit 0, `PASS correction_sweep observed=18 floor=18` (08:11:51–08:13:06) |
| `3de87aa` + `ExecC2Arms.patch` only | 23 | — | count only, no walk |
| integrated `46b4a70` + `ExecFloorsSweep.integrated.patch` | 25 | 25 | exit 0, `PASS correction_sweep observed=25 floor=25` (08:24:33–08:25:51); guard self-test `0 failure(s) over 165 assertions`, exit 0 |

- `ExecC2Arms.patch` on pristine `3de87aa` gives 23 (`git apply` exit 0; applied sweep sha
  `f54cff1791b67b87384e8479e7b6481ad706b41a29374f777d503d02f8d2d3c6`, matching the arms seat's own
  reported sha; UTC 08:20:11). The lane's `46b4a70` sweep carries two assertions more than that
  patch alone, so the value that matters for integration is 25, not 23.
- `ExecFloorsSweep.integrated.patch` (sha256 `46e78c30543993efcb20c1bfc932d82a34bcf4fddc535e43308b63963ab5b4ba`,
  70 lines) is the same registration with the floor at 25 at the same five sites. A pristine clone at
  `46b4a70` passes `git apply --check -v` (exit 0) and the applied clone walks green over all 14 rows
  (78.40 s), with `instrument_total` at 14 and the F6 anchor at `"instrument_total": 14`.

**What the L1 should do:** apply `ExecFloorsSweep.integrated.patch` if the lane's
`verifiers/check_correction_sweep.py` stays at `df66b485…` (25 assertions); apply the base
`ExecFloorsSweep.patch` only if that file is reverted to the freeze bytes (`799ea95…`, 18 assertions).
If neither holds, re-read `python3 -B verifiers/check_correction_sweep.py --self-test` and set the
value at all five sites in the same change — the registry floor, `EXPECTED_INSTRUMENTS`, the
`INSTRUMENTS` row, the docstring floor list and the docstring sentence. A floor below the observed
count stays green but is blind to exactly that many dropped assertions, which is the defect this
entry closes.

## 6. Evidence inventory (sandbox, `/fast/scratch/hyaku/kotoba-r58/ExecFloorsSweep/`)

| file | sha256 |
|---|---|
| `before.txt` (pristine walk, exit 0) | `23fe8f4b2f5f3c23c181758b115ef36c996a3e37c7121293262d699388fd8149` |
| `after-selftest.txt` (guard self-test, 0/165) | `00bcb4a4efa1196ab5dbb9f52183938040245c6335d77a937dde247e1e4185d5` |
| `after.txt` (patched walk, 14 PASS, exit 0) | `764809573ace3d03176ade6c02c290ea7c3b32c5f01c446183fc85f432bd9532` |
| `m08-sweep-selftest.txt` = `m09-…` = `m10-…` = `m11-…` | `a6e91c2d35ddf676cbee21d4363313582165327d81e94eddf83859ab41897455` |
| `m08-floors.txt` = `m09-…` = `m10-…` = `m11-…` | `c64765b362a549f8cbcdfb4d7d18ea2b3c8c0dc9922d551214ff7e2b5a6ae41b` |
| `combined-23.txt` (both patches, floor 23, exit 0) | `528e542a9affb99618f941813fd47b76a6ccb6c396cefe9bb56bc3ea7a361ae6` |
| `integrated-selftest.txt` (guard self-test at `46b4a70`, 0/165) | `00bcb4a4efa1196ab5dbb9f52183938040245c6335d77a937dde247e1e4185d5` |
| `integrated-walk.txt` (integrated tree, floor 25, exit 0) | `031572c9188b393493bc4eab7f32d324cb29c74d084c6e718a79cb0d2b03e5bf` |
| `probe/check_correction_sweep.pristine.py` | `799ea9502acc78521e3c7b4183945b52bfb1c8964e2c91bec2a64b134447bd18` |
| `ExecFloorsSweep.patch` (delivered, floor 18) | `61830536883ac672b958d09c248358dddc94f98c0edaad8ba329e566e5b2e13e` |
| `ExecFloorsSweep.integrated.patch` (delivered, floor 25) | `46e78c30543993efcb20c1bfc932d82a34bcf4fddc535e43308b63963ab5b4ba` |

The four mutant fixtures share hashes by construction: each run's only differing output line is the
same `FAIL correction_sweep observed=17 floor=18`, and each sweep summary is the same 17-assertion
line; the four runs are separated by the windows in §4 and by the mutation applied before each.

## 7. Risks and non-claims

- **Under-floor integration** (§5) is the one real risk: the base patch at floor 18 is green on the
  integrated tree (25 observed) but blind to the 7 assertions above the freeze count (2 above the
  arms-only 23), and blind to any future drop down to 18. The integrated companion patch sets 25;
  either way, bump-in-step is the rule the registry's own `$comment` states.
- **Not run by this seat:** `verifiers/check_sweep_mutants.py` at the patched tree (the counter runs
  the sweep's own self-test only; my per-mutant measurements above already show it still reports
  M08–M11 surviving, so the counter's verdict is unchanged by this patch — it is a second guard, not
  a counter change); `verifiers/check_could_not_evaluate.py` (its `check_assertion_floors.py` anchor
  is a `--script overlap_levers=…` red-child run in a temp clone, unaffected by a 14th row, but not
  executed here); the lane's post-integration gate set.
- **Cost:** the guard walk gains one child (the sweep self-test, which itself spawns three git
  calls); measured walk times on this host were 70.05 s before, 74.42 s after and 78.40 s on the
  integrated tree (host load was not recorded, so the delta is not attributed to the new child alone).
- **Patch format:** both patches were generated with explicit `--src-prefix=a/ --dst-prefix=b/`
  because the sandbox inherits the lane's `diff.noprefix=true` (jj-colocated); they apply with
  `git apply -p1` or `patch -p1`. `ExecFloorsSweep.patch` is against the freeze bytes of the guard
  and registry (unchanged at `46b4a70`); `ExecFloorsSweep.integrated.patch` is against `46b4a70`
  itself and differs only in the floor value (25 vs 18) at the same sites.
- **Writes:** sandbox only, plus this report and the two patch files in
  `.ufo/waves/round-58/build/`; no lane file was edited, no git/jj state in the lane was touched,
  nothing was committed or pushed. No tool installs or upgrades were needed.
