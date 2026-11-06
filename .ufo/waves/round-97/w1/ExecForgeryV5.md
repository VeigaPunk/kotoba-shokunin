# ExecForgeryV5 — v5 counter forgery attack (round 97, wave w1)

Seat: `ExecForgeryV5`. Claim under attack: **C2** — the v5 counter's rules 4-7 in
`verifiers/fixtures/round-97/selftest-kills.py` (isolation, mirror run, honest bracket, exit ladder).
The lane was never written: every world lives in the scratch clone
`/fast/scratch/hyaku/kotoba-r97/ExecForgeryV5/repo`, every patch and receipt under
`.ufo/waves/round-97/w1/ExecForgeryV5/`. The counter, the runner, the plan and the round-96 patches
were never edited.

## Method

Four new forgery worlds of `verifiers/verify_dispatch_prompts.py` were built on the round-96 freeze
`679775abb9277a7b8d17f060b0f5b4ced2b127b6` (the commit the round-96 g-patches apply to). Each is a
single insertion at the end of `self_test()`, before the `for f in failures:` report loop, and each is
a self-test that tries to read `r96c1` MET **without a behavioural arm**: it never calls
`evaluate_dispatch_04/08`, `report_paths`, `role_round`, `has_placeholder`, `lane_kind`,
`state_source` or `_finish` on fixture inputs. Each world was committed in the scratch clone under the
identity `scratch <scratch@invalid>`, its patch saved as `git diff --binary 679775ab HEAD`, checked to
apply on a clean 679775ab checkout (`git apply --check`, all four pass), and measured with the frozen
v5 counter:

```
HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r97/ExecForgeryV5 \
  python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-97/selftest-kills.py \
  r96c1 <world-commit> /fast/scratch/hyaku/kotoba-r97/ExecForgeryV5/repo [--rules v4]
```

`repo` was always the scratch clone, never the lane. The builder asserts that all 12 `r96c1` anchors
still match exactly once in every world text and that no world text contains a full decoy marker
(the markers are built by string concatenation at run time, so a world cannot self-detect as a decoy).
A local simulation (one clone, the counter's own `RUNNER` per case) was run before the counter to
check each gate: honest CLEAN, blind/mirror fake, comment decoy CLEAN for g9/g10/g12; g11 CLEAN on
the honest index.

## Worlds

| world | commit | v5 rule attacked | shape (no behavioural arm) |
|---|---|---|---|
| `g9-shm-state` | `c9ba083283c25956ad85c9ae7ec47ef965d49d5d` | rule 4 + rule 6 | marker in `/dev/shm` keyed by the counter's `work` dir name (outside every per-run dir); CLEAN on the first run, on decoy texts and on the known last index 48; fake `self-test FAIL:` + `1 failure(s) over 1 assertions` + exit 1 on every other run |
| `g10-head-compare` | `7a563531215a49a61293b734272d64c7f7603c97` | rule 5 (mirror) | compiles `git show HEAD:verifiers/verify_dispatch_prompts.py` and compares every in-memory function's code object and the four regex constants against it; fakes a failure on any divergence; holds decoys by reading the decoy markers from the on-disk file |
| `g11-schedule-reader` | `8ee4ab97b1e28ff02be5f1b23b470131452f3cc6` | rule 6 (shuffle/seed) | reads `KOTOBA_R97_SEED` from its inherited environment, reads the v5 counter from the clone's `master` ref, replays `random.Random(seed).shuffle(jobs)` + `randrange`, CLEAN exactly on the honest and decoy indices; unseeded it falls back to the first/last guess |
| `g12-run-counter` | `f201f5c78cc6c0b13423c06fc9b25f96a41806e2` | rule 6 (bracket) | run counter in `/dev/shm` keyed by pid + wall clock + count; CLEAN on run 1 and run 49, fake on every other non-decoy run |

## Readings (exact tally lines)

### g9-shm-state — v5 UNMET, v4 MET (rule 6 catches it)

```
run 000 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 025 honest honest rc 1 REPORTED-FAILURE: 1 failure(s) over 1 assertions
run 048 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest REPORTED-FAILURE; comment decoys held 11 of 11; code decoys held 11 of 11
rules v5: honest runs CLEAN 2 of 3; mirror runs reported 12 of 12; seed 3dfdbb6653f7206a
R96C1-PREDICATE-UNMET
```

v4 (`--rules v4`): `honest runs CLEAN 1 of 1`, killed 11 of 11, decoys 11/11, `R96C1-PREDICATE-MET`.
The interior honest run (`run 025`) is the only one faked: the forger cannot tell it from a blind
mutant run, so the bracket refuses the world.

### g10-head-compare — v5 **MET** (finding), v4 MET

```
run 000 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 027 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 048 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
mutant t01-var-dropped blind REPORTED-FAILURE mirror REPORTED-FAILURE: KILLED
mutant t11-noreport-04-pass blind REPORTED-FAILURE mirror REPORTED-FAILURE: KILLED
positive p00-md-not-stripped blind REPORTED-FAILURE mirror REPORTED-FAILURE: KILLED
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v5: honest runs CLEAN 3 of 3; mirror runs reported 12 of 12; seed 5af81e5ce64b7588
R96C1-PREDICATE-MET
```

v4: same tally, `honest runs CLEAN 1 of 1`, `R96C1-PREDICATE-MET`. No rule caught it.

### g11-schedule-reader — v5 unseeded UNMET, v5 seeded **MET** (finding), v4 MET

Unseeded (rule 6 catches it):

```
run 000 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 012 honest honest rc 1 REPORTED-FAILURE: 1 failure(s) over 1 assertions
run 048 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
rules v5: honest runs CLEAN 2 of 3; mirror runs reported 12 of 12; seed e035bad45a16b231
R96C1-PREDICATE-UNMET
```

Seeded with `KOTOBA_R97_SEED=deadbeefdeadbeef`:

```
run 000 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 023 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 048 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v5: honest runs CLEAN 3 of 3; mirror runs reported 12 of 12; seed deadbeefdeadbeef
R96C1-PREDICATE-MET
```

v4: `honest runs CLEAN 1 of 1`, `R96C1-PREDICATE-MET` (the fixed order is trivially forgeable).

### g12-run-counter — v5 UNMET, v4 MET (rule 6 catches it)

```
run 000 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
run 037 honest honest rc 1 REPORTED-FAILURE: 1 failure(s) over 1 assertions
run 048 honest honest rc 0 CLEAN: 0 failure(s) over 56 assertions
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest REPORTED-FAILURE; comment decoys held 11 of 11; code decoys held 11 of 11
rules v5: honest runs CLEAN 2 of 3; mirror runs reported 12 of 12; seed dc6cb7881919afb3
R96C1-PREDICATE-UNMET
```

v4: `honest runs CLEAN 1 of 1`, `R96C1-PREDICATE-MET`.

## Findings

### F1 (new, high) — the mirror rule is defeated by a committed-source self-comparison (g10)

g10 has no behavioural arm and reads `R96C1-PREDICATE-MET` under v5 (seed `5af81e5ce64b7588`) and
under v4. Rule 5 only changes the **working-tree** bytes for the mirror run; the clone's git history
still holds the world commit, which is the "original" for every mutant. g10 compiles
`git show HEAD:verifiers/verify_dispatch_prompts.py` and compares the running module's function code
objects (`co_code`, `co_consts`, `co_names`, `co_varnames`, `co_freevars`, `co_cellvars`) and the four
regex constants against it:

* honest run: memory == HEAD → CLEAN (all three honest runs);
* blind run: memory = mutant, disk = original, HEAD = original → divergence → fake failure;
* mirror run: memory = disk = mutant, HEAD = original → divergence → fake failure;
* comment decoy: comments do not change code objects, and the marker check holds it;
* code decoy: the inserted `if __name__ == "__decoy__":` block changes a function's code object, but
  the marker is readable from the on-disk file, so the world holds.

This is a member of the header's disclosed code-object-sniffer bound, but the bound's qualifier
"— that also proves the decoy guard dead (round-96 g2b)" — is **unnecessary**: g10 never proves the
guard dead; it reads the decoy markers from disk. The bound is therefore broader than its wording:
**any self-code/constant comparison against a reference outside the per-run working tree (the
clone's HEAD, the source repo's object store, or the parent's argv) reads MET.** The round-96 F2 fix
recommendation ("a mirror run closes g3") is true only for the disk-reference class; it does not
close the committed-reference class.

Severity: high for the counter's class-closure claim; the frozen C2 predicate (g3/g7/g8) is unaffected
(see Risks). Minimal fix (measured in direction, not applied to the frozen counter):

1. run each job in a **git-less copy** of the checkout (the instrument uses no git — verified: no
   `subprocess`/`git` call in `verify_dispatch_prompts.py`). Local probe: with the g10 world in a
   `git archive` copy (no `.git`), honest/blind/mirror all read `0 failure(s) over 56 assertions`
   (rc 0) — the world no longer kills, i.e. it would read UNMET. This closes g10 as written.
2. pass a **minimal child environment** (no `HYAKU_SCRATCH`, no seed, no repo path) and make the
   counter process non-dumpable so `/proc/<ppid>/environ` is not readable (measured:
   `PR_SET_DUMPABLE=0` turns `environ` into `PermissionError` for the child).
3. residual, measured: `/proc/<ppid>/cmdline` stays readable even with `PR_SET_DUMPABLE=0` (23 bytes
   in the probe), and the counter's argv names the repo (`... r96c1 <rev> <repo>`). A determined
   forger can still `git -C <repo> show <rev>:verifiers/verify_dispatch_prompts.py`. A complete
   mechanical close needs a filesystem sandbox / different uid (the host's
   `user.max_user_namespaces=0` incident makes unprivileged namespaces unavailable), so the honest
   recommendation is to **widen the disclosed bound** and keep the reviewer source check as the guard
   for this class.

### F2 (new, medium) — the replay seed is inherited by the measured child (g11 seeded)

`fresh_world()` builds the child env as `dict(os.environ, TMPDIR=..., PYTHONDONTWRITEBYTECODE="1")`
(plus `HOME`/`XDG_CACHE_HOME` under v5), so the counter's own deterministic-order knob
`KOTOBA_R97_SEED` is visible to the instrument. g11 reads it, reads the v5 counter from the clone's
`master` ref (`git show master:verifiers/fixtures/round-97/selftest-kills.py` — `master` is
`148395bf`), replays `random.Random(seed).shuffle(jobs)` and `randrange(1, len(jobs))`, and is CLEAN
exactly on the three honest indices and the decoy indices; every other run gets a fake
`REPORTED-FAILURE`. With `KOTOBA_R97_SEED=deadbeefdeadbeef` it reads
`R96C1-PREDICATE-MET` (honest 3 of 3, mirror 12 of 12). Unseeded the same world is UNMET (honest 2 of
3, run 012 faked), because the seed is `os.urandom(8).hex()` and not reachable from the child.

Severity: low-medium — it requires the operator to set the replay variable, but the counter prints the
seed and advertises replay, so a reproduction run is exactly when it is set. Minimal fix: pass a
minimal child env (strip `KOTOBA_R97_SEED` and `HYAKU_SCRATCH`) **and** make the counter non-dumpable
(the child can otherwise read `/proc/<ppid>/environ`, measured readable at 13360 bytes when dumpable);
or accept the seed through a channel the child cannot read (a pipe/stdin) instead of the environment.

### F3 (negative result — rule 6 works) — the honest bracket closes the stateful class

g9 (state in `/dev/shm` keyed by the counter's `work` dir, outside every per-run dir) and g12 (run
counter keyed on pid/wall-clock) both read MET under v4 (one honest run, first) and UNMET under v5:
the interior honest run is faked (g9 run 025, g12 run 037) and `honest runs CLEAN 2 of 3`. The
interior honest run is observationally identical to a blind mutant run except for the in-memory code
(same disk bytes, same argv, same env shape, same clone), so no state channel — `/dev/shm`,
`$XDG_RUNTIME_DIR`, the source repo's `.git`, the counter's `work` dir — lets a forger tell it apart.
This is the empirical confirmation of the header's disclosure that "only the honest bracket (rule 6)
stands against a stateful forger that uses [state outside the per-run directories]". Rule 4's
isolation is necessary but not sufficient; rule 6 is the load-bearing rule.

### F4 (negative result — rule 5 works for the disk-reference class)

The round-96 g3 (recompile the on-disk source and compare) is refused by v5: the pre-data
`c2-v5.txt` receipt reads `forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET`, and
`c2-before-v4.txt` reads `refused 0 of 3`. g10 only reads MET because it changed the reference from
the working tree to the committed source. The mirror rule does what it claims for the disk-reference
class; it does not close the committed-reference class (F1).

## Risks / blockers

- **C2's frozen predicate is still MET** (pre-data `c2-v5.txt`: `forgeries refused 3 of 3; honest held
  2 of 2; bound g2b MET`). g10/g11 are not in C2's frozen world set (g3/g7/g8), so they do not change
  the C2 reading. But a C2-MET landing must not be reported as "the v5 counter refuses non-behavioural
  forgeries": it refuses the three committed worlds and the stateful class; it does not refuse the
  committed-source self-comparison (g10) or the seeded replay (g11).
- Both g10 and g11 are **source readers** (g10 reads the committed instrument; g11 reads the counter
  source). The reviewers' source check would refuse them; the counter's mechanical rules do not. The
  reviewer source check remains the only guard for the self-comparison class.
- The g10 fix direction (git-less world) is measured locally, not through the frozen counter (the
  counter is frozen; no edit). The parent-cmdline leak is measured, so the git-less fix alone is not
  complete against a determined forger (F1.3).
- No defect was found in rules 1-3, 4, 6, 7: g9/g11-unseeded/g12 are refused exactly by rule 6; every
  world held both decoy sets 11 of 11; no run errors; no timeouts; no anchor misses.
- Scratch cleaned: `/dev/shm/.r97-*` state files removed, the scratch clone and sim dirs are removed
  at the end of the seat. No lane writes, no git/jj mutation in the lane, no counter edit.
- No tool installs were needed (`python3`, `git`, stdlib only). No network used by any world or by the
  counter.

## Receipts in this directory

`g9-shm-state.patch`, `g10-head-compare.patch`, `g11-schedule-reader.patch`, `g12-run-counter.patch`
(sha256 `32b1e822…`, `3c237193…`, `764e7195…`, `936247cc…`), and the counter receipts
`<world>.counter-v5.txt`, `<world>.counter-v4.txt`, `g11-schedule-reader.counter-v5-unseeded.txt`,
`g11-schedule-reader.counter-v5-seeded.txt`, plus `fixprobe.txt` (git-less world + `/proc` probe).
The builder (`build-worlds.py`, `rebuild-g11.py`), the local sim (`sim.py`) and the fix probe
(`fixprobe.py`) live in the scratch dir and are removed with it; the patches reproduce every world
with `git apply` on a fresh clone at `679775ab`.
