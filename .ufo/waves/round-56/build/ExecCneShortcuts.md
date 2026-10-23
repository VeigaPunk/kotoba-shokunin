Result: DONE — `verifiers/check_could_not_evaluate.py` v2 closes the three round-55 shortcuts (D red anchors per gate, P class-N no-git `--root` probes, S PYTHONSAFEPATH=1 + stdlib-shadow scan), saves every run's stdout/stderr, and is delivered as a patch that applies clean at b0b7140b/e02f5f5d; receipts: S exits 2, D and P are NOT MET (exit 1) on their rebuilt worlds, and b0b7140b prints its line.

Seat: ExecCneShortcuts (executor, leaf). Sandbox clone `/fast/scratch/hyaku/kotoba-r56/ExecCneShortcuts` at `e02f5f5d` plus sandbox commit `436339c` (v2). The three worlds were rebuilt *in that clone* by fetching the round-55 sizing critic's commits from `/fast/scratch/hyaku/kotoba-r55/CriticC2Sizing`: `world-D = 9c992b8dd55f00e7c45de4471a600262e54a66a8`, `world-P = 65f5d237192d6dbb8c4e12d7f84fb12dbe22197f`, `world-S = eb97c954f7821760d09059f8125de2edc277dbca`. Those are sandbox-only commits and do not exist in the lane, so the world receipts below are this seat's, from the clone named above.

Tool installs or updates: none. No lane file was edited by this seat; lane writes are this report and the patch file named below. `verifiers/check_agentdef_boxes.py` and every other lane file are untouched (C2 is withdrawn; this is a routed repair, not a re-claim).

## Deliverable

- Patch: `.ufo/waves/round-56/build/ExecCneShortcuts-v2.patch` (19,705 bytes, sha256 `7df216c5e5c1b3ed157f7a7b4b9a7b2a36a06ba83b7caf211058340608faab88`), produced by `git format-patch -1 436339c` in the sandbox clone. One file: `verifiers/check_could_not_evaluate.py`, +196/−47.
- v2 file sha256: `a6844d7261b391af3f1659ee70913e3146a65cb420419aa7b4a936801546d72b`.
- The v1 file is one blob from `a10240c0` to `e02f5f5d` (`git --no-optional-locks diff --quiet a10240c0 e02f5f5d -- verifiers/check_could_not_evaluate.py` → YES; also YES for `b0b7140b..e02f5f5d`), so `git apply --check` of the patch against a pristine `b0b7140b` tree printed `APPLIES CLEAN`.
- Integrate with `git apply .ufo/waves/round-56/build/ExecCneShortcuts-v2.patch`; then the self-test and the base line below should reproduce.

## What v2 adds (each change only adds a way to fail)

1. **Red anchor per gate (closes world D).** Frozen `ANCHORS` table, one entry per gate, expected exit exactly 1: the sizing critic's anchor table (`.ufo/waves/round-55/build/CriticC2Sizing.md` § counterexamples, `probes.txt` §A/§B) plus the floors gate's red tree as a `--script overlap_levers=verifiers/zz_stub_nosummary.py` child (v2 writes that stub into its temporary clone). A gate that launders a real 1 into 2 misses its anchor; the D world misses seven.
2. **PYTHONSAFEPATH=1 for every gate run plus a stdlib-shadow scan (closes world S).** Every gate environment gets `PYTHONSAFEPATH=1` (the gates cannot import a `verifiers/<stdlib-name>.py`), and a scan refuses with exit 2 when `verifiers/*.py` in the counter's own checkout *or* in the measured revision has a stem in `sys.stdlib_module_names`.
3. **Class N, a probe class an entry-only preflight cannot meet (closes world P).** The four gates that accept `--root` (`check_correction_sweep`, `check_mcp_instructions`, `check_description_thresholds`, `check_overlap_levers`) are run with `--root .` and **git absent**, expecting 0 or 1: reading a directory needs no git, so a missing git must not be could-not-evaluate. The P preflight exits 2 on the missing git alone; the honest gates return 0 (measured at b0b7140b).
4. **Saved run streams.** Every run's stdout/stderr is written under `--out DIR` (default: a fresh `kotoba-r56-cne-runs-*` directory under the system temp dir, printed as `run outputs saved under …`), file names `<seq>-<gate>-<kind>.stdout|.stderr`; the text output also prints the last stderr line of every MISS. A receipt can now show *why* a run exited as it did (e.g. whether the floors G stderr names git or a nested timeout).
5. The tally line becomes `could-not-evaluate probes honoured <K> of 29; controls held <C> of 13; red anchors held <A> of 13`; exit 0 iff all three are full, 1 otherwise, 2 = the counter itself could not evaluate. The tally line is frozen text (`25` was 12 class-R + 13 class-G; v2 adds 4 class-N). The temporary clone directory and the no-git PATH directory names are randomised, which also defeats a label-keyed preflight (the critic's world L, never counter-run).

## Receipts

Environment: 32 cores. Load at each measurement is pasted below; the L1's message notes a host-wide load spike (up to 96 at 02:57–03:04Z) and a cleanup `pkill -f 'fast/scratch/hyaku/kotoba-r56'` at ~03:06Z that killed my first parallel attempt; those runs were discarded and re-run (see "Incidents").

Self-test (sandbox clone, `PYTHONSAFEPATH=1 python3 -B verifiers/check_could_not_evaluate.py --self-test`):

```
self-test: 0 failure(s) over 21 assertions
self-test exit 0
```

### world-S (measured revision `eb97c954`, the `verifiers/argparse.py` shadow)

```
$ PYTHONSAFEPATH=1 python3 -B verifiers/check_could_not_evaluate.py --rev world-S --out …/runs/world-S
could-not-evaluate: shadow module(s) under verifiers/ at eb97c954f782: argparse.py
world-S exit 2
```

The critic's exact S run (counter run *from* a checkout of the measured revision) also refuses, both with and without `PYTHONSAFEPATH=1`:

```
$ cd scratch/probe-S-shadow   # clone at world-S with v2's counter copied in
$ python3 -B verifiers/check_could_not_evaluate.py --rev world-S …
SHADOW argparse loaded in check_could_not_evaluate.py
could-not-evaluate: shadow module(s) under verifiers/ in this checkout: argparse.py
exit 2
$ PYTHONSAFEPATH=1 python3 -B verifiers/check_could_not_evaluate.py --rev world-S …
could-not-evaluate: shadow module(s) under verifiers/ in this checkout: argparse.py
exit 2
```

In the first run the shadow *did* load (its stderr line is on screen) and the file-based checkout scan still refused.

### world-D (measured revision `9c992b8d`; remap 1→2 on seven gates) and world-P (measured revision `65f5d237`; entry-only preflight)

Both worlds are NOT MET. Observed tally lines (each measurement saved 136 run files; load 70.70 at the start and 31.72 at the end, 03:05:20Z–03:13:56Z):

```
--- world-D (measured 9c992b8dd55f00e7c45de4471a600262e54a66a8)
box_proof_case_deletion.py         A expect 1   got 2 MISS
check_gate_finding_delta.py        A expect 1   got 2 MISS
check_overlap_levers.py            A expect 1   got 2 MISS
check_mcp_instructions.py          A expect 1   got 2 MISS
check_description_thresholds.py    A expect 1   got 2 MISS
check_correction_sweep.py          A expect 1   got 2 MISS
check_assertion_floors.py          A expect 1   got 2 MISS
could-not-evaluate probes honoured 29 of 29; controls held 13 of 13; red anchors held 6 of 13

--- world-P (measured 65f5d237192d6dbb8c4e12d7f84fb12dbe22197f)
check_correction_sweep.py          N expect 0|1 got 2 MISS
check_mcp_instructions.py          N expect 0|1 got 2 MISS
check_description_thresholds.py    N expect 0|1 got 2 MISS
check_overlap_levers.py            N expect 0|1 got 2 MISS
could-not-evaluate probes honoured 25 of 29; controls held 13 of 13; red anchors held 13 of 13
```

The D misses are exactly the seven gates that world remaps (a real 1 laundered to 2); the D world's `verify_corpus_independent` anchor still gives 1 because its blanket wrapper only converts exceptions, so 6 anchors hold rather than 0. The P misses are exactly the four class-N probes: its preflight exits 2 on the missing git even for `--root`, where the honest gates return 0.

Exit values: the frozen rule is `return 0 if honoured == 29 and held == 13 and anchors == 13 else 1`, so both are 1 (6 ≠ 13; 25 ≠ 29). Honesty note: the subshell `echo "… exit $?" > …/world-D.exit` files are absent — the harness ended that job right after the runs — so for these two runs the exit values are read off the same frozen condition that produced the tally ([derived, not separately echoed]); the S and b0b7140b exits were echoed and are observed above. v1 met both worlds with exit 0 (the critic's `counter-D-seq.txt` and `counter-P-seq.txt`); v2 does not.

### b0b7140b (the round-55 spot-check revision; printed, no target)

```
$ PYTHONSAFEPATH=1 python3 -B verifiers/check_could_not_evaluate.py --rev b0b7140b --out …/runs/b0b7140b
Fri 23 Oct 2026 03:06:33 AM UTC   load average: 64.78, 65.29, 41.03
measured b0b7140b5a7cf8a50f13989ee6285fc8ee245c41
…
check_overlap_levers.py            N expect 0|1 got 0 ok
run outputs saved under /fast/scratch/hyaku/kotoba-r56/ExecCneShortcuts/scratch/runs/b0b7140b
could-not-evaluate probes honoured 29 of 29; controls held 13 of 13; red anchors held 13 of 13
b0b7140b exit 0
Fri 23 Oct 2026 03:13:37 AM UTC   load average: 40.60, 70.30, 53.88
```

No target (C2 is withdrawn); the line is recorded, and on this revision it is full — every probe, control and anchor held, with 0 `MISS` lines and 68 gate runs saved as 136 stdout/stderr files under `scratch/runs/b0b7140b/`. The assertion-floors G run exits 2 for the right reason: its saved stderr ends `could-not-evaluate: git not runnable: [Errno 2] No such file or directory: 'git'` (not a nested timeout).

### Hand-probes at b0b7140b (sandbox `scratch/probe-base`, the anchors and new classes measured directly, never in the lane)

The 13 frozen anchors, each expected 1 (`rc=1` on all; `t` = wall seconds):

```
box_proof_case_deletion --rev f3046466            rc=1 t=1s
check_gate_finding_delta --base e3371548 --head a10240c0  rc=1 t=1s
check_overlap_levers --rev 43ca0bfb               rc=1 t=1s
check_sources_append_only --rev a10240c0          rc=1 t=0s
check_mcp_instructions --rev c8579a4c             rc=1 t=0s
check_description_thresholds --rev 422ffd10       rc=1 t=0s
check_alwayson_boxes --rev e78dff66               rc=1 t=0s
check_callee_rename --rev c8579a4c                rc=1 t=0s
check_opencode_repin --rev e78dff66               rc=1 t=7s
check_correction_sweep --rev c8579a4c             rc=1 t=0s
check_gate_registry --rev 422ffd10                rc=1 t=0s
verify_corpus_independent (no args)               rc=1 t=0s
check_assertion_floors stub child 900             rc=1 t=57s
```

Class N at b0b7140b (`--root .`, `PATH` holding only a `python3` symlink), expected 0|1:

```
check_correction_sweep --root .      rc=0
check_mcp_instructions --root .      rc=0
check_description_thresholds --root . rc=0
check_overlap_levers --root .        rc=0
```

Why the separator is class N and not "git present but refusing": with a `git` shim that is present and refuses every command (exit 128, "dubious ownership"), the honest b0b7140b gates give `rc=2` for all twelve rev-taking gates, `rc=1` for assertion floors and `rc=2` for `verify_corpus_independent` — exactly what the P preflight gives — so that class cannot separate P from an honest gate. Measured: `box_proof 2, finding_delta 2, overlap 2, sources_append_only 2, mcp 2, description_thresholds 2, alwayson 2, callee_rename 2, opencode_repin 2, correction_sweep 2, gate_registry 2, assertion_floors 1, verify_corpus_independent 2`.

Why `verify_corpus_independent`'s anchor (no args) is legitimately red at b0b7140b: it reports the corpus's own POINTERS/COMMITS class findings, e.g. `corpus/README.md:68: .ufo/reports/round-48/kotoba.md` (pointer to a file that does not exist) and unresolved commit tokens such as `451a02ff`, `4dd7753`, `cfb894a5`; exit 1. The same probe gave 1 at a10240c0 (the critic's `probes.txt` §A), so it is red at both measured revisions.

## What v2 does not measure, and risks

- It is **not a claim**. Round-56 erratum 1 withdrew C2 before data; this is round-55 routed defect 3's repair. No predicate, target or map disposition changes; `verifiers/check_agentdef_boxes.py` and `verifiers/checklist-baseline.json` are untouched.
- Red anchors are frozen inputs. If a gate's judging lines later change so an anchor legitimately returns 0, the anchor will MISS (a way to fail — but also a false alarm the L1 must adjudicate). The `verify_corpus_independent` row is the most exposed: it depends on the corpus's current pointer/commit findings staying unresolved; if they are repaired, re-freeze that one row.
- The floors anchor depends on `check_assertion_floors.py --script NAME=PATH` accepting a stub *inside* the clone. If a revision removes or confines that vector, the anchor MISSes; the stub is written by v2 into the temporary clone only and never into the lane.
- The shadow scan is a file-name rule for direct children of `verifiers/`; a shadow under a different name, a package directory, or a shadow that forges the scan itself is outside its reach. `PYTHONSAFEPATH=1` for the counter's own process is in the documented command; the checkout scan is file-based and still refused the loaded S shadow (receipt above).
- Class N depends on the four `--root` modes staying git-free (measured at b0b7140b). The two gates with no `--root` (floors, corpus-independent) have no class-N probe.
- Unchanged from v1: under heavy host load the assertion-floors nested self-test timeout can turn its G/V runs into 2 (the critic saw this at load 88–107); v2 makes the cause visible in the saved stderr but does not mask it.

## Incidents

- A first parallel attempt at the four measurements (started 03:04Z) was killed at ~03:06Z by another seat's cleanup `pkill -f 'fast/scratch/hyaku/kotoba-r56'` (the L1's message names PIDs 1197368/70/72). Those partial receipts were discarded; the receipts above were re-run afterwards. Any future cleanup with that pattern will kill these counters (their command lines contain the scratch path).
- The world commits live only in the round-55 and this seat's sandbox clones. The L1 cannot resolve `world-D/P/S` in the lane; re-running those receipts requires fetching them from `/fast/scratch/hyaku/kotoba-r55/CriticC2Sizing` (still present at this writing) or this clone.
- One `git checkout --detach` in a fresh clone of my clone failed with `fatal: '--detach' cannot be used with '-b/-B/--orphan'` (the clone maps branches to `origin/*`); `git checkout --detach origin/world-S` then worked. [INFERENCE] the clone's detached HEAD confuses the short-name resolution; recorded here only as a scratch-tooling note.
