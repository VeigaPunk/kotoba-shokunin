# ExecForgeryV6 — v6 counter forgery attack (round 98, wave w1)

Seat: `ExecForgeryV6`. Claim under attack: **C2** — the v6 counter's rules 1–10 in
`verifiers/fixtures/round-98/selftest-kills.py` (git-less world, minimal child env,
honest bracket, mirror). Built on the round-96 freeze
`679775abb9277a7b8d17f060b0f5b4ced2b127b6` in scratch clone
`/fast/scratch/hyaku/kotoba-r98/ExecForgeryV6/repo`; lane never written, no counter
or plan edited, no git/jj mutation in the lane.

## Method

Four new forgery worlds of `verifiers/verify_dispatch_prompts.py` were built on the
round-96 freeze. Each is a single insertion at the end of `self_test()`, before the
`for f in failures:` report loop, and each is a self-test that tries to read `r96c1`
MET **without a behavioural arm**: none of them calls `evaluate_dispatch_04/08`,
`report_paths`, `role_round`, `has_placeholder`, `lane_kind`, `state_source`,
`box_proof` or `_finish` on fixture inputs. Each world was committed in the scratch
clone under the identity `scratch <scratch@invalid>`, its patch saved as
`git diff --binary 679775ab <world-commit>`, checked to apply on a clean `679775ab`
checkout (`git apply --check`, all four pass), and measured with the frozen v6 counter
plus `--rules v5`:

```
HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r98/ExecForgeryV6 \
  python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-98/selftest-kills.py \
  r96c1 <world-commit> /fast/scratch/hyaku/kotoba-r98/ExecForgeryV6/repo [--rules v5]
```

`repo` was always the scratch clone, never the lane. All four share a compile-based
`_fisis` (code-object signatures of the running module's functions vs a reference
blob's top-level functions, plus `*RE` pattern constants) and the g9/g10 decoy-marker
guard (markers built by string concatenation at run time, so a world cannot
self-detect as a decoy). No world text contains a full decoy marker.

## Worlds

| world | final commit | v6 rule attacked | shape (no behavioural arm) |
|---|---|---|---|
| `g13-ppid-cmdline-ref` | `b3bf2f1eccf72fa1cdef34e32880551be98cb258` | rule 8 (disclosed bound?) | reads `/proc/<ppid>/cmdline`, parses REV+REPO from argv[4]/argv[5], `git -C <repo> show <rev>:<instrument>`, compares code objects |
| `g14-ppid-environ-seed` | `2906f994da6ce1db36a70325be550da9cad3d515` | rule 9 (non-dumpable claim) | reads `/proc/<ppid>/environ` for `KOTOBA_R97_SEED`, replays the counter schedule, fakes exactly the non-honest runs |
| `g15-fs-scan-ref` | `8e1be6637810323096977bfcafc18daf31486637` | rule 8 (no parent argv) | scans the filesystem for repos carrying the instrument, walks `git log --all` (60 newest) plus `git reflog HEAD` (60 newest), fakes iff memory matches no committed blob |
| `g16-work-pristine-ref` | `c34dc6cb7205a675994b67a8f9b4ba57b5d6abb4` | rule 8 (shared `work/` tree) | reads the shared `work/pristine` honest reference via `Path(__file__).resolve().parents[4]`, fakes iff memory diverges from it |

## Readings (exact tally lines; receipts beside this report)

### g13-ppid-cmdline-ref — v6 **MET**, v5 MET (finding)

v6:

```
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v6: honest runs CLEAN 3 of 3; mirror runs reported 12 of 12; seed <hex>
R96C1-PREDICATE-MET
```

v5 (`--rules v5`, same tally line): `R96C1-PREDICATE-MET`, rc 0. The world's first
attempt used counter-argv indices 2/3 (off by one — argv is
`[python, -B, script, claim, REV, REPO]`; fixed to 4/5). g13 fakes every
blind/mirror mutant run, holds honest and both decoy sets, never crashes.

### g14-ppid-environ-seed — v6 UNMET, v5 unseeded UNMET, v5 seeded MET (cause control)

v6:

```
R96C1 targets killed 0 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v6: honest runs CLEAN 3 of 3; mirror runs reported 1 of 12; seed <hex>
R96C1-PREDICATE-UNMET
```

v5 unseeded: `R96C1-PREDICATE-UNMET` (0 of 11 killed — no seed available). v5 seeded
(`KOTOBA_R97_SEED=deadbeefdeadbeef`): `R96C1-PREDICATE-MET` (rc 0) — the replay
engine works when the seed is inherited, exactly the round-97 g11 gap. Under v6
the seed is unreachable (F3): the child gets `PermissionError` on
`/proc/<ppid>/environ` (measured directly, `environ-probe.txt`) and the minimal
child env carries no replay seed.

### g15-fs-scan-ref — v6 **MET**, v5 MET (finding)

v6:

```
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v6: honest runs CLEAN 3 of 3; mirror runs reported 12 of 12; seed <hex>
R96C1-PREDICATE-MET
```

v5 (`--rules v5`, same tally line): `R96C1-PREDICATE-MET`, rc 0 (612 s). Finds the
world's own commit by scanning `**/.git` under the scratch bases first,
then `git log --all` + `git reflog HEAD` (60 newest each, deduped). `log --all`
alone misses dangling detached-HEAD builds (measured: the g15 commit was absent
from `log --all` but present in `reflog`); with the reflog walk the honest run is
CLEAN and every mutant run is faked. Slow (~9 s/run — up to 120 compile/blob
checks per run) but within the counter's per-run timeout.

### g16-work-pristine-ref — v6 **MET** (finding), v5 UNMET

v6:

```
R96C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11
rules v6: honest runs CLEAN 3 of 3; mirror runs reported 12 of 12; seed <hex>
R96C1-PREDICATE-MET
```

v5: `R96C1-PREDICATE-UNMET` (no `pristine/` dir in the v5 clone world, so the
world fakes every run including honest: `honest REPORTED-FAILURE`, `CLEAN 0 of 3`).
g16 is v6-specific — it attacks rule 8's own export (F2).

## Findings

### F1 (new, high) — the disclosed parent-cmdline bound is live (g13 MET under v6)

Rule 9 leaves `/proc/<ppid>/cmdline` readable; it names `REV` and `REPO`
(counter argv[4]/argv[5]). g13 parses them, `git -C <repo> show
<rev>:verifiers/verify_dispatch_prompts.py` recovers the committed world blob,
and `_fisis` (compile-based code-object signatures plus `*RE` constants) fakes
exactly the mutant runs. g13 reads `R96C1-PREDICATE-MET` under both v6 and v5
with no behavioural arm, no state channel, and no seed. This is the plan's
disclosed bound ("a forger that reads REPO's object store through it ... is not
refused by rule 8") realized as a working forgery — the bound's wording is
exactly right; the world confirms it is reachable on this host. Severity: high
for the counter's mechanical-closure claim (the committed-reference class remains
open in v6), zero effect on C2's frozen predicate (g13 is not in its world set).
Minimal fix (measured in direction, never applied to the frozen counter): hide
the parent's argv from the child — run the measured child through a tiny launcher
whose argv carries no REV/REPO (chdir + exec the runner with argv
`[path, --self-test]`), or scrub the counter's own argv before spawning children
(a re-exec with a sanitized argv). No sandbox needed for this channel: the leak
is the argv itself.

### F2 (new, high) — rule 8's pristine export is itself the honest reference (g16 MET under v6)

The `work/pristine` tree that every run reflink-copies from is the honest source
bytes sitting in the counter's work dir, one `parents[4]` hop above the
instrument (`.../rNNN.xxx/world/kotoba-shokunin/verifiers/...`). g16 reads it
with no git, no argv, no env — pure filesystem reachability — and fakes every
divergence. So the git-less world does not remove the honest reference; it
relocates it to a predictable shared path inside the run's own ancestor tree,
preserved untouched for all 49 runs (the counter overwrites only
`clone/<instrument>`). Severity: high — same class as F1 but reachable without
any proc trick. Minimal fix: do not leave the shared pristine tree reachable
from the run's ancestor chain — copy it into the per-run dir only and remove the
shared copy before spawning the child (the run's own copy is overwritten with the
mutant on mirror runs, so it cannot serve as a reference once the shared source
is gone). The per-run dir is deleted after each run, so a private per-run source
leaves nothing shared behind.

### F3 (negative result — rule 9 works) — the non-dumpable claim holds for environ (g14 UNMET under v6)

A child of a `PR_SET_DUMPABLE=0` parent gets `PermissionError: [Errno 13]`
reading `/proc/<ppid>/environ` (measured directly; `environ-probe.txt`), and the
minimal child env carries no replay seed. g14 kills 0 of 11 under v6, but reads
MET under `--rules v5` seeded (`KOTOBA_R97_SEED=deadbeefdeadbeef`), reproducing
the round-97 g11 gap under the old rules — the cause control proving the v6
refusal comes from rule 9, not from a schedule change.

### F4 (negative result — the honest bracket still stops pure state) — no new signal

None of the four worlds uses state outside the per-run directories except g15's
read-only scan; all four are refused-or-MET exactly by whether their reference
channel exists, not by counting. The bracket continues to stand against stateful
forgers; reference recovery (F1/F2/g15), not state, is the open class.

### F5 (new, medium) — g15's reachability bound (landed worlds are findable without the parent)

A landed world's commit is findable by scanning the filesystem for any repo
carrying the instrument and walking `log --all` + reflog (newest 60 each) —
reflog is load-bearing for dangling detached-HEAD builds (`log --all` alone
missed the g15 commit; `reflog` had it). Cost: ~9 s/run on this host. This
class needs no proc leak at all — only that the world commit exists somewhere
reachable on the host filesystem, which it always does (the counter reads it via
`git show rev:` from the same object store). Minimal fix: none mechanical short
of a filesystem sandbox/different uid (the plan's stated bound); the reviewer
source check remains the guard for this class, and the bound should stay
disclosed with this measurement attached.

## Risks / blockers

- **C2's frozen predicate is still MET** (pre-data `c2-v6.txt`: `forgeries refused
  5 of 5; honest held 2 of 2`). g13/g15/g16 are not in C2's frozen world set
  (g3/g7/g8/g10/g11), so they do not change the C2 reading. But a C2-MET landing
  must not be reported as "the v6 counter refuses non-behavioural forgeries": it
  refuses the five committed worlds and the stateful class; it does not refuse
  the proc-cmdline reference (g13), the filesystem-scan reference (g15), or its
  own pristine export (g16).
- All three MET worlds are **source readers** (they read a committed/pristine
  reference of the instrument). The reviewers' source check would refuse them;
  the counter's mechanical rules do not. The reviewer source check remains the
  only guard for the reference-recovery class.
- The F1/F2 fixes are measured in direction (g13/g16 in-world behavior under
  v6), not through the frozen counter (the counter is frozen; no edit).
- Two findings classes are new relative to round 97: F2 (the pristine export
  as reference — v6-specific, since v5 has no pristine dir; g16 reads UNMET
  under v5) and the reflog detail of F5.
- No defect was found in rules 1–7, 9, 10: g14 is refused exactly by rule 9; the
  g14 v5-seeded MET reproduces the v5 gap (cause control); every world held both
  decoy sets 11 of 11 in its final reading; no run errors in final readings
  (earlier builds' `RUN-ERROR`s were builder bugs by this seat — an
  `extend(...)[:400]` precedence slip and an argv off-by-one — all fixed and
  re-measured; the counter never misclassified them).
- No tool installs were needed (`python3`, `git`, stdlib only). No network used by
  any world or by the counter. Scratch cleaned on yield; `/dev/shm/.r97-*` state
  removed; no lane writes, no git/jj mutation in the lane, no counter edit.

## Receipts in this directory

- `g13-ppid-cmdline-ref.patch` (sha256 `ee4c0c16d434…`), `g14-ppid-environ-seed.patch`
  (`0e880b2d70be…`), `g15-fs-scan-ref.patch` (`57e70a63c8ed…`),
  `g16-work-pristine-ref.patch` (`5600035cd2a6…`) — final builds, each
  `git apply --check` clean on a fresh `679775ab` checkout.
- Counter receipts: `<world>.counter-v6.txt` (all four), `<world>.counter-v5.txt`
  (g13/g16; g15-v5 pending `_counter-v5.txt` — see below), `g14-ppid-environ-seed.counter-v5-unseeded.txt`,
  `g14-ppid-environ-seed.counter-v5-seeded.txt`, plus `environ-probe.txt` (direct
  `/proc/<ppid>/environ` PermissionError probe). The builder (`build.py`) and
  sims live in the scratch dir and are removed with it; the patches reproduce
  every world with `git apply` on a fresh `679775ab` clone.
