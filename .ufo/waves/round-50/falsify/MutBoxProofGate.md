# MutBoxProofGate — round-50 falsify seat: mutation of the delegated `--box-proof` gate code

**Verdict: HOLDS-BOUNDED** — applies to the round-50 D2 gate half (the checklist gate that runs a
delegated instrument's `--box-proof` against the map under check) at the judged bytes
`956ee1676e4c18480bce8ac3993541462be76e11`. The shipped gate code behaves as its own statement says
under every mutant I applied to the five named points (exit-code test, help detection, timeout, map
path, detail text): no defect was found in the code as written. The bound is on the *detector*: the
gate's own `--self-test` survives 4 of 12 single-point mutants, each of which silently weakens the
delegated proof (M3, M7, M11, M12). The gate's self-assertion is therefore weaker than the Q25
demand that a counter be *shown able to fail*.

## Setup

- Private clone: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin <scratch>/lane`,
  `git -C <scratch>/lane checkout -q 956ee1676e4c18480bce8ac3993541462be76e11`.
- Scratch: `/fast/scratch/hyaku/kotoba-r50/falsify/mut-box-proof-gate/` (harness, probes, results.json).
- Mutated file: `verifiers/verify_skill_checklist.py` (the gate), functions `supports_box_proof`
  (help detection, timeout) and `delegated_box_proof` (exit-code test, map path, detail text).
- Detector (the same command for every mutant): `python3 -B verifiers/verify_skill_checklist.py --self-test`.
- Pristine sha256 of the mutated file: `325d22efdf26d8a99bf5f2f395bd10ae1bc6322737859b539c80af9689d51eae`
  (identical before the sweep and after it; `git status --porcelain` in the scratch clone: empty).
- Baseline: `--self-test` → exit 0, `0 failure(s) over 1851 assertions`. A baseline failure would
  have made every result inconclusive; the baseline is green, so KILLED/SURVIVED are meaningful.
- Every mutant is a single-point text substitution; the file was restored byte-exact after each run
  (`restored_ok=True` for all 12, re-checked by sha256).

## Results

| mutant | point | change (one point) | detector exit | self-test failures | verdict |
|---|---|---|---|---|---|
| M1 | exit-code test | `if proc.returncode != 0:` → `== 0:` | 1 | 4 | KILLED |
| M2 | exit-code test | `if proc.returncode != 0:` → `> 1:` (only exit > 1 fails) | 1 | 2 | KILLED |
| M3 | help detection | `BOX_PROOF_FLAG in (proc.stdout + proc.stderr)` → `in proc.stdout` | 0 | 0 | **SURVIVED** |
| M4 | help detection | same line → `in proc.stderr` | 1 | 3 | KILLED |
| M5 | timeout | `BOX_PROOF_TIMEOUT = 120` → `= 0` | 1 | 3 | KILLED |
| M6 | timeout | proof run `timeout=BOX_PROOF_TIMEOUT` → `timeout=0` | 1 | 3 | KILLED |
| M7 | map path | `if map_path is not None:` → `if map_path is None:` (map never passed) | 0 | 0 | **SURVIVED** |
| M8 | map path | `argv += ["--map", str(map_path)]` → `argv += ["--map"]` | 1 | 3 | KILLED |
| M9 | detail text | failure detail `(exit %d)` → `(rc %d)` | 1 | 1 | KILLED |
| M10 | detail text | skip note `no %s support` → `no %s capability` | 1 | 1 | KILLED |
| M11 | detail text | `summary = first_line(proc.stdout)` → `first_line(proc.stderr)` | 0 | 0 | **SURVIVED** |
| M12 | delegated run | proof run loses `cwd=str(base)` | 0 | 0 | **SURVIVED** |

All 8 kills are the delegated-box-proof arms failing (`self-test FAIL: delegated box proof: …`), not
unrelated assertions. Killed: M1, M2, M4, M5, M6, M8, M9, M10. Survived: M3, M7, M11, M12.

## Findings on the four survivors (coverage findings, not code defects)

The shipped bytes are correct; each survivor is a *weakening the self-test cannot see*, confirmed by a
second probe. A surviving mutant is a coverage finding and does not license a change of the contract.

- **M7 (map path) — the strongest.** The delegated instrument is run without `--map`, so the proof
  runs against the instrument's own default map instead of *the map under check*. Probe with an
  argv-echoing stub: pristine note `… --box-proof exit 0: ARGV --box-proof --map
  /tmp/m7probe/verifiers/checklist-baseline.json`; under M7 `… ARGV --box-proof` (no map). The gate
  still prints `exit 0` and stays green. The gate's own comment calls this run "a red-before run
  points the live map at a snapshot" — under M7 the snapshot map is silently ignored. No self-test arm
  pins that `--map` reaches the instrument.
- **M3 (help detection).** An instrument that advertises `--box-proof` on stderr is not run at all.
  Probe: pristine → `delegated verifiers/probe_err.py: --box-proof exit 1` with problem
  `failed its --box-proof (exit 1)` (gate red); under M3 → `no --box-proof support (…), not run`,
  problem `None` (gate green). The delegation is unproven and the gate says nothing.
- **M11 (detail text).** The instrument's own proof line is dropped from the detail. Live gate run at
  the judged bytes, pristine: `… delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0:
  boxes proven 2`; under M11 the same run prints `… --box-proof exit 0` — the operator loses the
  `boxes proven 2` count, and the self-test asserts only `exit 0`, so it passes.
- **M12 (delegated run).** The instrument is run from the gate's cwd instead of the map's repo.
  Probe (stub prints its cwd): pristine `CWD /tmp/m12probe`; under M12 `CWD
  /fast/scratch/hyaku/kotoba-r50/falsify/mut-box-proof-gate`. A relative-path instrument would break;
  no self-test arm pins the cwd.

## Scope and evidence

- Read-only on the lane checkout `/home/vgpnk/Projects/shokunin/kotoba-shokunin`: no file there was
  edited, created or deleted except this report; no git write command and no `jj` command was run in
  the lane, the fleet root, or any sibling lane. All mutations and runs happened in the scratch clone.
- Commands and exit codes (scratch clone):
  - `python3 -B verifiers/verify_skill_checklist.py --self-test` → exit 0, `0 failure(s) over 1851
    assertions` (baseline, and again after the sweep).
  - `python3 -B harness.py` → per-mutant runs; every mutant run exited 0 or 1 as tabulated; final
    `sha256sum verifiers/verify_skill_checklist.py` = `325d22ef…d51eae` (pristine).
  - `python3 -B verifiers/verify_skill_checklist.py --skill SKILL.md --map
    verifiers/checklist-baseline.json --check checklist.box_map_complete` → exit 0,
    `PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 2 delegated, 31
    unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`
    (live gate at the judged bytes; the delegated proof does run and does pass).
  - `python3 -B survivor_probe.py` and `python3 -B extra_probe.py` → the M3/M7/M11/M12 probe output
    quoted above; both scripts restore the pristine bytes (`restored_ok=True`).
- Tooling: no install was needed — the gate, the harness and the probes are Python 3.14.8 standard
  library only (no third-party package, no network fetch).
- Not measured here (other seats' scope): the C2 counter itself (`verifiers/box_proof_case_deletion.py`,
  the 6 must-fail deletions), the C1 census guard, and the D1–D6 wording repairs.
