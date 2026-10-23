Result: MIXED — the frozen C2 counter's `--self-test` kills 3 of 7 mutants, but 4 survive it and 2 of those survive the base run unchanged, so the counter's self-test is not a sufficient guard on its own probe logic.

# Mutation test of the frozen C2 counter (round 55, seat MutC2Counter)

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_could_not_evaluate.py`
(frozen at plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`, sha256
`0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d`).

The lane counter was never edited. Every mutation was applied to a **sandbox clone** at
`/fast/scratch/hyaku/kotoba-r55/MutC2Counter/` (one clone per mutant, `.mutprobe/m*/`), and
every mutant clone was restored to the pristine sha256 afterwards (evidence below).

## Method

1. Pristine baseline: run the unmodified counter at base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`
   in the sandbox, to confirm the sandbox reproduces the committed receipt
   `.ufo/waves/round-55/controls/C2-base.txt` before judging any mutant.
2. Mutate one behaviour-bearing point at a time (`tally` / `ok` / `plan_runs` / `run_one` /
   `measure`), run `--self-test`, and for every mutant the self-test does **not** kill, run the
   mutated counter at base and compare the printed summary line with the pristine one.
3. Restoration: copy the pristine bytes back over every mutant clone; re-hash all.

Commands run in the sandbox (all capped by `timeout`, all read-only w.r.t. the lane):

```
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/MutC2Counter
git -C /fast/scratch/hyaku/kotoba-r55/MutC2Counter checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c0
python3 -B verifiers/check_could_not_evaluate.py --self-test
python3 -B verifiers/check_could_not_evaluate.py --rev f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c
```

## Baseline (pristine, sandbox) — reproduces the committed receipt

`2026-10-22T23:13:35Z` → `2026-10-22T23:17:07Z`, exit 1, 211 s:

```
could-not-evaluate probes honoured 13 of 25; controls held 13 of 13
```

Identical to `.ufo/waves/round-55/controls/C2-base.txt` (`13 of 25; 13 of 13`, exit 1). The
sandbox is therefore a valid place to judge mutants.

**But the pristine baseline does not hold still.** A *second* pristine run of the same frozen
bytes later in the session (same sandbox, same revision, but on a host busy with the wave's
sibling seats) printed:

```
could-not-evaluate probes honoured 14 of 25; controls held 12 of 13
```

— a different line for identical bytes. The first run (idle host, 23:13) matched the committed
receipt exactly; the later one (busy host, 00:05) did not. Both runs are in the evidence files
`.mutprobe/pristine-base.txt` and `.mutprobe/pristine-serial2.txt`. This is the single most
important limit of this probe and is detailed in "Limit of this probe itself" below: **the C2
receipt line carries ±1 of load-dependent noise, so it can only be compared against another
line measured under the same load conditions.** The m2b/m3 verdicts below rest on the *shape* of
the per-gate rows, not on the last digit of the summary.

## Results

| id | mutation | file:line | `--self-test` | base run @ f0e5de82 | verdict |
|----|----------|-----------|---------------|-----------------------|---------|
| m1 | `ok()` also accepts exit 1 where "2" is expected | `verifiers/check_could_not_evaluate.py:103` | **killed** (1 failure: `probe exiting 1 is not honoured`) | — | killed |
| m2 | `plan_runs()` no longer emits the V (real-revision) control | `:99` | **killed** (2 failures: `every gate has S and V`, `always-2 gate fails its V control`) | — | killed |
| m2b | V control runs `--self-test` instead of the real revision | `:99` | survives (0 failures) | `13 of 25; 13 of 13`, exit 1 — **line unchanged** | **survivor** |
| m3 | random-revision existence check dropped (`rand` no longer verified absent from the clone) | `:151-153` | survives (0 failures) | `13 of 25; 13 of 13`, exit 1 — **line unchanged** | **survivor** |
| m3b | `rand` = the measured revision, so every class-R probe runs the real revision | `:153` | survives (0 failures) | `7 of 25; 12 of 13`, exit 1 — line changed | killed at base |
| m4 | class-G probe leaves `git` on `PATH` | `:128-129` | survives (0 failures) | `7 of 25; 12 of 13`, exit 1 — line changed | killed at base |
| m5 | control check uses `any(...)` instead of `all(...)` | `:112` | **killed** (3 failures: `always-2 gate fails its V control`, `red self-test fails the S control`, `self-test exiting 2 fails the S control`) | — | killed |
| m6 | a probe that times out is reported as exit 2 (honoured) instead of `None` | `:134-135` | survives (0 failures) | not finished (deadline) | **survivor (self-test only)** |

### Self-test output, verbatim

```
[m1] FAIL probe exiting 1 is not honoured: got (3, 2), expected (2, 2)
[m1] self-test: 1 failure(s) over 12 assertions          exit 1
[m2] FAIL every gate has S and V: got False, expected True
[m2] FAIL always-2 gate fails its V control: got (3, 2), expected (3, 1)
[m2] self-test: 2 failure(s) over 12 assertions          exit 1
[m2b] self-test: 0 failure(s) over 12 assertions          exit 0
[m3] self-test: 0 failure(s) over 12 assertions          exit 0
[m3b] self-test: 0 failure(s) over 12 assertions          exit 0
[m4] self-test: 0 failure(s) over 12 assertions          exit 0
[m5] FAIL always-2 gate fails its V control: got (3, 2), expected (3, 1)
[m5] FAIL red self-test fails the S control: got (3, 2), expected (3, 1)
[m5] FAIL self-test exiting 2 fails the S control: got (3, 2), expected (3, 1)
[m5] self-test: 3 failure(s) over 12 assertions          exit 1
[m6] self-test: 0 failure(s) over 12 assertions          exit 0
```

### Base runs of the self-test survivors (serial, one at a time)

```
m2b  could-not-evaluate probes honoured 13 of 25; controls held 13 of 13   exit 1
m3   could-not-evaluate probes honoured 13 of 25; controls held 13 of 13   exit 1
m3b  could-not-evaluate probes honoured  7 of 25; controls held 12 of 13   exit 1
m4   could-not-evaluate probes honoured  7 of 25; controls held 12 of 13   exit 1
```

pristine under the same serial conditions: `13 of 25; 13 of 13`, exit 1.
(pristine on the later busy host: `14 of 25; 12 of 13` — see the baseline note above.)

Row-level detail, which is what the verdicts rest on:

- **m2b** (V control runs `--self-test`): every V row still reads `expect 0|1` and every gate
  returns 0, so the summary line is byte-identical to the pristine baseline. The only visible
  trace is that `check_sources_append_only.py V` and `verify_corpus_independent.py V` return
  0 instead of 1 — invisible in the summary, and only detectable on the shortcut commit (below).
- **m3** (random-revision existence check dropped): summary line byte-identical to the
  baseline; no per-gate row moves at all. The mutation is behaviourally inert here because a
  random 40-hex string is never an existing object.
- **m3b** (R probe runs the real revision): every R row flips from `got 2 ok`/`got 1 MISS` to
  `got 0 MISS` — the R probes no longer exercise an unknown revision, so they stop being
  could-not-evaluate probes at all. Honoured falls 13 → 7.
- **m4** (git left on PATH for class G): every G row flips to `got 0 MISS` / `got 1 MISS` —
  the class-G probe no longer tests the git-absent path. Honoured falls 13 → 7.

### Independent shortcut probe (a second, sharper check on m2b)

I rebuilt the §9 shortcut control from scratch in a separate sandbox clone
(`.mutprobe/shortcut`, commit `a09346dda0f72b69392705def8ecc72efd702ee5` on `a10240c`): the
thirteen gates replaced by stubs that `exit 0 if '--self-test' in sys.argv else 2`. With the
**pristine** counter this reproduces the committed shortcut receipt exactly:

```
could-not-evaluate probes honoured 25 of 25; controls held 0 of 13    exit 1
```

which matches `.ufo/waves/round-55/controls/C2-shortcut.txt` (`25 of 25; 0 of 13`, exit 1). The
same stub commit measured with the **m2b** counter gives:

```
could-not-evaluate probes honoured 25 of 25; controls held 13 of 13   exit 0
```

So m2b — replacing the real-revision V control with `--self-test` — makes the counter pass the
exact shortcut the §9 control exists to reject. m2b is the dangerous survivor.

## Findings reported (limits of the frozen counter, not of the lane gates)

1. **m2b — the real-revision control is not self-testable.** `plan_runs()` builds the V row with
   `args = real` (`:99`). Swapping it for `["--self-test"]` keeps the self-test green (the
   self-test's `world()` helper synthesises codes by kind and never checks *which arguments* a
   V run carries), keeps the base summary line identical (`13 of 25; 13 of 13`), and turns the
   §9 shortcut control from exit 1 into exit 0. The self-test asserts that a gate always
   exiting 2 breaks its V control, but never asserts that the V control runs the real revision.
   A cheap fix would be a self-test assertion that the V row's args are the gate's real-revision
   argument list and differ from the S row's `--self-test`. *Reported only; the counter is
   frozen and was not edited.*
2. **m3 — the random-revision existence check is untested.** `measure()` draws `rand` and loops
   until `git cat-file -e rand` fails (`:151-153`), so the class-R probe is guaranteed to name
   an object the clone does not have. Dropping that loop keeps the self-test green and keeps the
   base line unchanged (a random 40-hex string is almost never an existing object, so the
   behaviour is identical in practice) — the guard is real but unverified by any check the
   counter runs. *Reported only.*
3. **m6 — a timed-out probe is indistinguishable from an honest exit 2.** `run_one()` returns
   `None` on `TimeoutExpired` (`:134-135`), and `ok()` treats `None` as "not honoured"; the
   self-test covers the synthetic case (`probe timing out is not honoured`) but the mutation
   that changes the *real* timeout path to return 2 keeps the self-test green. The base run was
   still in flight when the wave deadline passed, so m6 is reported as a **self-test survivor
   only** — its base-run effect is not claimed here.
4. **m3b and m4 are caught, but only by the base receipt, not by the self-test.** Both leave
   `--self-test` green (exit 0) while corrupting the measurement (honoured 13 → 7). A counter
   whose self-test passes can still be measuring nothing real; the base receipt is the only
   check that caught these two.

## Limit of this probe itself: the base measurement is not deterministic

The first pristine re-run (run concurrently with three other base runs) printed
`14 of 25; 12 of 13`, not `13 of 25; 13 of 13`. The cause is isolated to
`verifiers/check_assertion_floors.py`: it runs ~16 child `--self-test` subprocesses with a
120 s per-child timeout (`SELF_TEST_TIMEOUT_S = 120`, `check_assertion_floors.py:147`, `:532-536`),
and a child that times out makes the parent exit 2 (`run_error` → `return 2`, `:543-544`). Under
CPU contention a child hits its 120 s limit and the gate's class-G/V code changes between 1 and
2 — which is exactly the row that moved (`check_assertion_floors.py G expect 2 got 1 MISS` →
`got 2 ok`, and `V expect 0|1 got 0 ok` → `got 2 MISS`).

Consequences for how these numbers must be read:

- All comparisons above were re-run **serially** (one base run at a time) to remove the load
  effect; the serial numbers are the ones reported.
- The committed receipt `.ufo/waves/round-55/controls/C2-base.txt` was taken on an idle host, so
  it records the unloaded value `13 of 25; 13 of 13`. A re-run of the same frozen bytes on a
  busy host can print `14 of 25; 12 of 13` — a different line for identical bytes. **The C2
  receipt line is therefore not reproducible under load**, which is a property of the measured
  gates, not of the counter. Worth knowing before anyone treats a receipt-line difference as
  evidence of a counter change.
- The two gates most affected are `check_assertion_floors.py` and `verify_corpus_independent.py`
  — the same two that carry the round-55 repair work (`FixAssertionFloors`,
  `FixCorpusIndependent` are running in this wave). Their class-G exit codes are the least
  stable numbers in the C2 measurement.

### Direct confirmation of the flip (identical bytes, standalone)

Running the *unmodified* gate at base `f0e5de82` twice in a row, outside the counter:

```
run1 exit 2 elapsed 144s
run2 exit 1 elapsed 123s
```

Same bytes, same revision, different exit code. The gate's own wall time (~120-145 s) sits right
at its 120 s per-child timeout, so whether a child self-test is judged "timed out" (→ exit 2)
or "ran and failed its floor" (→ exit 1) is a coin flip decided by machine load. This is a
property of the **measured gate**, not of the counter; the counter merely reports whatever the
gate returned. It means the C2 base receipt's `13 of 25; 13 of 13` line is a load-dependent
number, and that any comparison of receipt lines must be made on an idle host.

## Restoration evidence

Every mutant clone was restored to the pristine bytes after its run; the lane counter was never
touched. Final hashes (all identical to the frozen counter):

```
$ sha256sum /fast/scratch/hyaku/kotoba-r55/MutC2Counter/verifiers/check_could_not_evaluate.py
0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_could_not_evaluate.py
0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d
$ sha256sum .mutprobe/{m1,m2,m2b,m3,m3b,m4,m5,m6,shortcut}/verifiers/check_could_not_evaluate.py
0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d   (x9)
```

The lane's `git status --porcelain verifiers/` does list eight modified gate files
(`box_proof_case_deletion.py`, `check_assertion_floors.py`, `check_correction_sweep.py`,
`check_description_thresholds.py`, `check_gate_finding_delta.py`, `check_mcp_instructions.py`,
`check_overlap_levers.py`, `verify_corpus_independent.py`). Those are sibling executor seats'
in-flight edits, **not mine**: `verifiers/check_could_not_evaluate.py` is not among them and its
sha256 is unchanged. My base runs are unaffected by that working-tree state in any case —
`measure()` clones the lane and checks out the named revision, so the gates measured are the
**committed** bytes of `f0e5de82`, never the siblings' uncommitted edits. The shortcut sandbox
(`a09346d`) and the mutant clones live only under
`/fast/scratch/hyaku/kotoba-r55/MutC2Counter/`; nothing was pushed and no lane Git or jj state
was mutated.

## Not done

- m6's base run at `f0e5de82` was cut off by the wave-settle deadline; m6 is reported as a
  self-test survivor with its base-run effect explicitly unclaimed.
- The C1 counter was not examined (different seat).
- No mutation was run against the round-55 tip, since the tip's gates do not yet exist in this
  lane checkout at the time of the run.
