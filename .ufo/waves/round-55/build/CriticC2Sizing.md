Result: BREAKS — two sandbox shortcuts meet the frozen C2 predicate (`25 of 25; 13 of 13`, exit 0): one turns real findings into 2, the other is only a preflight. A third, which changes none of the 13 gates, reaches exit 0 when the counter runs from a checkout of the measured revision. The counter is unchanged (sha256 `0c1258e2…` on every run); the fixes below are guards.

Seat: KotobaR55.CriticC2Sizing (critic, read-only). Sandbox: clone `/fast/scratch/hyaku/kotoba-r55/CriticC2Sizing` at `a10240c0`, scratch under `/fast/scratch/hyaku/kotoba-r55/CriticC2Sizing-scratch/` (script `mutate.py`, receipts `counter-*.txt`, `probes*.txt`, `saturation.txt`). The gate bytes at `a10240c0` are the same as at `f0e5de82`: `git diff --stat f0e5de82 a10240c0 -- verifiers/` shows only the two new counters.

## Counterexamples (frozen counter, sandbox commits on a10240c0)

| # | Shortcut | Commit | Counter line | Exit |
|---|---|---|---|---|
| D | 7 gates wrap `__main__`: exceptions become 2, and an exit of 1 becomes 2 unless `--self-test` is in argv. `verify_corpus_independent` gets only the exception wrapper (8 files, +40/−8). | `9c992b8d` | `honoured 25 of 25; controls held 13 of 13` (`counter-D-seq.txt`, run 23:42:54Z–23:46:19Z) | **0** |
| P | Naive preflight in `__main__` of the 8 failing gates: no `git` on PATH, or a `--rev/--base/--head` value that is not a commit, gives exit 2. Nothing else changes. | `65f5d237` | `honoured 25 of 25; controls held 13 of 13` (`counter-P-seq.txt`, run 23:46:19Z–23:49:04Z) | **0** |
| S | One new file `verifiers/argparse.py`, a shadow of the standard-library module. No gate changes. Counter run from a checkout of that revision. | `eb97c954` | `honoured 25 of 25; controls held 13 of 13`; stderr shows `SHADOW argparse loaded in check_could_not_evaluate.py` (`counter-S-incheckout.txt`) | **0** |
| S′ | Same commit, counter run from a clean `a10240c0` checkout. The measured gates still import the shadow, which installs an excepthook that exits 2. | `eb97c954` | `honoured 21 of 25; controls held 13 of 13` (`counter-S-clean.txt`) | 1 |
| A | The exception wrapper, plus deleting the `does not exist / exists on disk` branch that returns None (mcp, description thresholds) and raising in `git_show` (overlap). | `cc7300f0` | `24 of 25; 12 of 13` (the overlap self-test broke; assertion-floors G stayed 1) | 1 |
| C | The remap on all 13 gates | `a17e15bf` | `25 of 25; 8 of 13` | 1 |

The plan's §9 shortcut (always 2) is the bluntest form of the shortcut, and V catches it. D is the refined form: it remaps only 1 to 2, and V does not catch it.

## Q1. Does V (0 or 1 on the real revision) catch a gate that turns real findings into 2? No, for 11 of 13 gates.
- At base, V is 1 only for `check_sources_append_only` and `verify_corpus_independent` (`C2-base.txt`). For `check_gate_registry` it is 1 at `a10240c0` only because the two new counters were not registered yet. Every other V is 0, so remapping 1 to 2 cannot show there.
- `check_gate_finding_delta` V can never be 1. V passes `--base REV --head REV` (`check_could_not_evaluate.py:68`), and new findings are head minus base (`check_gate_finding_delta.py:37-39`). With identical trees that is empty, so the gate returns 0 (`:101,:106`).
- Red anchors, on the plans' own recorded before-revisions (`probes.txt` §A; floors in `probes3.txt` §E):

| Gate | Anchor | Base bytes | D bytes | P bytes |
|---|---|---|---|---|
| box_proof_case_deletion | `--rev f3046466` | 1 | 2 | 1 |
| gate_finding_delta | `--base e3371548 --head a10240c0` | 1 | 2 | 1 |
| overlap_levers | `--rev 43ca0bfb` | 1 | 2 | 1 |
| mcp_instructions | `--rev c8579a4c` | 1 | 2 | 1 |
| description_thresholds | `--rev 422ffd10` | 1 | 2 | 1 |
| correction_sweep | `--rev c8579a4c` | 1 | 2 | 1 |
| assertion_floors | red tree: one overlap self-test assertion removed, `--self-test-timeout 900` | 1 | 2 | 1 |

  For the five gates the attacks do not touch, base bytes give 1 at their anchors (`probes.txt` §B): `callee_rename` @ c8579a4c, `alwayson_boxes` and `opencode_repin` @ e78dff66, `gate_registry` @ 422ffd10, and `sources_append_only` @ tip.
- Variant A (sandbox `wt-A`) moves the frozen before-receipts of rounds 51, 52 and 54 from 1 to 2: mcp @ `4c003a4b`, description thresholds @ `e3371548`, overlap @ `7c81a787`. That is an identity change V cannot see.

## Q2. Cheaper shortcuts, and keying on labels
- A blanket `except Exception: 2` alone is not enough. It turns crashes into 2, but leaves the four non-crash misses at 1: R on overlap, mcp and description thresholds (a file absent at an unknown revision reads as a real `0 of 7`), and G on assertion floors (`FAIL … summary=missing`). Variants A and S′ stop at 21–24 of 25.
- The remap (D) or the preflight (P) is enough.
- Keying on labels buys nothing over P. The honest checks cost the same: `rev-parse --verify REV^{commit}` and git on PATH. I built a label-keyed variant L (`95be8b9c`): it acts only when `kotoba-r55-cne-` is in `__file__`, PATH ends in `nogit-bin`, or a revision differs from the clone's HEAD. Outside the counter it still exits 1 on R and G (box proof R=1, mcp R=1, correction sweep G=1; shell output). **Its counter run was not done** (deadline).
- Trust hole: Python puts the script directory first on `sys.path`. So any `verifiers/<stdlib-name>.py` replaces that module in the counter and in every gate. A diff review of each changed gate sees nothing.
- Fix verified: with `PYTHONSAFEPATH=1`, S run from its own checkout drops to `14 of 25; 12 of 13`, the same as the base run under the same flag (`counter-S-incheckout-safe.txt`, `counter-base-safe.txt`). The one control miss in both runs is assertion floors V=2 from load (see Q5).

## Q3. Axis
Operability, by `AXES.md:13`: "A checklist item can be run and produces the stated outcome." The surface is the scripts' exit paths. The counter does not read the registry text, so the cheaper consistency shortcut (rewording `2=could-not-evaluate`) cannot move it. Good.

The two probe classes saturate early, though. P meets the predicate, yet these classes still exit 1:
- corrupt manifest in box proof: base 1, P 1 (DriverError traceback)
- non-JSON output from a child gate in finding delta: base 1, P 1
- misshapen baseline in always-on boxes, a gate already counted honoured: base 1 (AttributeError)
- git present but refusing (simulated "dubious ownership", git exits 128) in assertion floors: base 1, P 1 (`probes2.txt` §C)

The record must say "exits 2 on an unknown revision and with git absent from PATH". It must not say "honours could-not-evaluate".

## Q4. Is a do-nothing reachable?
The base is not: `13 of 25`. A run with no change to the claimed surface is reachable (S, exit 0). A hidden regression is also reachable through P. The `--root` forms of correction sweep, mcp, description thresholds and overlap need no git: with git absent they exit 0 at base and 2 under P (`probes2.txt` §D). The counter never runs `--root`. Note that the registry entry command for correction sweep is `--root .`.

## Q5. Measurement stability (new)
Load average was 88–107. Under that load, `check_assertion_floors` hit its nested 120 s timeout (`harness_independent self-test timed out after 120s`) and exited 2 in V and G. That happened in all four concurrent counter runs, the untouched base included: `controls held 12 of 13`, and G honoured for the wrong reason (`base-safe`: 14 of 25). The counter saves no gate output, so a receipt cannot show why a run exited 2.

## Smallest safe corrections (guards; counter unchanged)
1. Run the predicate from a checkout of the plan commit `a10240c0`, with `PYTHONSAFEPATH=1` exported (the gates inherit it, `check_could_not_evaluate.py:132`). Record both in the receipt. Reject any change under `verifiers/` that adds a module whose stem is in `sys.stdlib_module_names`. By grep, only `verify_alwayson.py:576` puts `verifiers/` on `sys.path`, and it does so explicitly.
2. Red-anchor control in wave 2: re-run the table above on the integrated commit and require 1 at every anchor. This separates D and A (2) from P (1).
3. Hand-run R and G outside the counter's temp path and PATH name. This catches L.
4. Run the four `--root` forms with git absent, and require the base codes.
5. Run the counter on an idle host and paste `uptime`. For assertion floors, check that the G stderr names git, not a timeout.
6. Narrow the wording of the C2 record (Q3).

Lane working copy (read-only `git --no-optional-locks diff`, 23:42:43Z, tip `9615579`): the in-flight gate patches use the P shape, with `rev-parse --verify` and `except OSError`. My regex scan found no remap, catch-all, label key or shadow module. Corrections 2–6 apply to them.

## Incident (disclosed to the L1 at about 23:29Z)
I typed `PATH=<shim> git status` and the real git ran (the bash hash table), with the fleet root as cwd. `/home/vgpnk/Projects/shokunin/.git/index` then showed mtime 23:29:20Z. That fits git's optional stat refresh; no staged content changed. A later lane `git status --porcelain` left the lane index mtime at 23:24:04Z (unchanged). No installs. No lane edits except this file.
