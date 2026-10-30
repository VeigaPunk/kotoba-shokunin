# Kb82M03Controls — mutation probe of the E19 frozen C1 guard and the unchanged C1 counter

Axes: freshness; operability. Fixture-only probe: no production after-value scored, no axis score, no 6/6 tip-battery claim. Base `47dbe8781657de563ff867caca6244d28e3db504`. All candidates were commits in my scratch clone (toplevel asserted before every git call); no lane, index, jj, production, verifier, plan, corpus or fleet-root write. No tool installed or upgraded. Pacman untouched. Background job cap was saturated host-wide on first launch; the harness was re-run in the foreground.

## Frozen identities re-checked before any run

- `/home/vgpnk/.local/bin/omp`: 276244656 bytes, mtime ns 1793326786168359786 (`2026-10-29T23:19:46.168359786-03:00`), sha256 `e7dd2b606c4ebe9d1a7bcfad1b8820db968cd6b05409fed1c6bc8db0b6a95a8f`. Matches the E19 frozen guard.
- `/home/vgpnk/.opencode/bin/opencode`: sha256 `ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7`. Matches.
- Frozen counter `verifiers/check_substrate_repin_v2.py` at base: sha256 `629487a116bdf287f2bcd43652ead051b052efd0a32632b38a45fece6ed4b348` (equals `git show 47dbe87:verifiers/check_substrate_repin_v2.py`).
- E19 guard `build/Kb82E19PinGuard_guard.py`: sha256 `61ace2b9e586f34f9344e0147a5f586b94c9680e17f900494f76b36ecbfd77e3` (the frozen value).
- Guard self-test (`--self-test`): exit 0, `0 failure(s) over 9 assertions`.

## Mutation results

G = minimal live re-pin on top of base: `check_substrate_pins.py` and `verify_surfaces.py` omp default to `omp` (ELF); `baseline.json` pins omp sha and mtime to live. Every mutant is G plus one change, rebuilt from base. Counter: exit codes and stdout are verbatim; wall times are in the JSON.

| Run | Mutation | Guard exit (red checks) | Counter exit, verbatim | Class |
|---|---|---|---|---|
| B0 | unchanged base | 1 | 2: `verify_surfaces.py reported 0 row(s) (exit_code 2: omp binary not found: .../omp.real)` | red as expected |
| C0 | G (path + pin only) | 0 (15/15 checks) | 0: `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | accepted (see S5) |
| A1 | pin sha = stale 18.12.2 digest `9513ef9f…` | 1 [omp.sha-pin] | 1: `pins OK 2/3`; FAIL pins | killed by both |
| A2 | pin mtime one ns off (`…168359785`) | 1 [omp.ns-mtime-pin] | 1: `pins OK 2/3` | killed by both |
| A3 | defaults + pins → same-mtime stub omp, stub sha self-pinned | 1 [omp.sha-pin, both omp defaults] | 1: `pins OK 3/3; surfaces pass 5 of 7` | guard-killed; counter pins HOLLOW (S2) |
| A4 | `check_substrate_pins.py` replaced by canned PASS printer | 1 [check_substrate_pins.py.AST-defaults] | **0**: `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | guard-only kill (S3) |
| A5 | `verify_surfaces.py` replaced by canned 7-PASS printer | 1 [verify_surfaces.py.AST-defaults] | **0**: `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | guard-only kill (S3) |
| A6b | `verifiers/json.py` shadows stdlib json; both instruments byte-identical to G; shadow returns canned PASS payloads | **0** (15/15; scope list shows `verifiers/json.py`) | **0**: `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | **SURVIVED guard and counter (S1)** |
| A7 | `omp:agents-md/AGENTS.md` deleted from `surfaces-baseline.json`; inventory untouched | 1 [census.exact-base-identities] | 1: `surfaces pass 5 of 7` | killed by both |
| A8 | same deletion plus its inventory row removed | 1 [census.exact-base-identities] | 1: `surfaces pass 6 of 7` | killed by both |
| A9 | extra `measured_against` key `omp_binary_path` → stub; pins/defaults live | **0** | 1: `FAIL pins: 3 of 4 row(s) hold, 4 row(s) reported` | guard survived; counter killed by row count (S4) |
| A10 | defaults + pins → stub whose bytes are the live `strings -n 4` dump (same mtime ns) | 1 [omp.sha-pin, both omp defaults] | **0**: `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified` | guard-only kill; counter fully hollow for omp (S2) |
| C10 | defaults via symlink to live omp | 0 | 0: unchanged C0 line | accepted (legit: identity is bytes) |
| C11 | comment-only edit to `check_substrate_pins.py` | 0 | 0: unchanged C0 line | accepted (AST insensitive to comments) |

Guard self-test run: 9 assertions, 0 failures, exit 0.

## Surviving classes (exact)

**S1 — survives both guard and counter (A6b).** A non-instrument file under `verifiers/` (`json.py`) shadows the stdlib `json` module. The instruments' bytes are identical to G, but the shadow returns canned PASS payloads for `check_substrate_pins.py` and `verify_surfaces.py`. Result: guard exit 0 with 15/15 green, and counter exit 0 with the full target line. Causes: (a) the guard's `extracted_scope_changed_paths` list names `verifiers/json.py` but the value is informational only; no path outside the defaults is rejected; (b) the guard AST-freezes only the two instrument files, not their imports; (c) the counter runs tree code with `sys.path[0]` = tree `verifiers/`, so a shadow there is executed. Consequence: the numeric C1 certification is invalid for any revision that carries such a file, and nothing in the guard rejects it.

**S2 — survives the counter; only the guard catches it (A3, A10). The counter's omp conjunct is hollow.** The counter's `holds()` returns True for every PASS non-opencode pin row (`if row.get("pin") != OPENCODE_PIN: return True`). The omp pin verdict is therefore the instrument's own verdict against the tree's default path bytes, not the live host bytes. A3 shows `pins OK 3/3` for a self-pinned stub omp; A10 shows `pins OK 3/3; surfaces pass 7 of 7` when the stub's bytes are the live omp `strings` dump, so the surfaces conjunct is also satisfied by path bytes alone. Only the outside guard binds omp identity. Repair (not applied; the counter is frozen, so a deliberate planner decision is needed): bind omp rows to live bytes as opencode rows already are.

**S3 — counter accepts stub instrument stdout (A4, A5).** The counter trusts the JSON payload; a canned printer scores `3/3, 7/7, 3/3`, exit 0. Only the guard's executable-AST freeze rejects it.

**S4 — guard gap, caught by counter only (A9).** The guard checks only the three pin fields of `measured_against`. An extra `*_binary_*` key pointing at a stub passes the guard. The counter rejects it only through the row count (4 rows reported, PINS_TOTAL 3). Repair: the guard should require the exact key set of `measured_against` and reject unknown binary keys.

**S5 — C0 meets the target with the guard green. Planner call required.** The path-plus-pin-only candidate yields `pins OK 3/3; surfaces pass 7 of 7; removal ledger 3 of 3 verified`, exit 0, and guard exit 0. The plan names path-only and pin-only worlds as shortcuts that must be rejected unless the guard rejects them. Here the surfaces 7/7 is derived by the base extractor from the live omp dump (A10 shows it is derived from whichever bytes the default path names), and the guard rejects every omp-identity lie I tested (A1, A2, A3, A10). So C0 is not hollow for the surfaces conjunct, but the omp pins conjunct rests on the guard (S2). I did not declare C0 a shortcut and did not claim the target met by an independent measurement.

**Untested (declared, not measured).** Corpus inventory edits that keep the class set; census fields outside `harness/literal/context_kind/verdict` (guard compares only those four); relative default paths. These are outside the guard's compared set by code reading [INFERENCE: unverified by run].

## Answers to the seat's questions

- Is the unchanged C1 counter hollow for omp? Yes for the pins conjunct (A3, A10) and for the surfaces conjunct whenever the omp bytes at the tree's default path are the only input (A10). The counter's opencode handling is bound to live bytes and was not broken by any mutant.
- Does the outside E19 guard reject the shortcut worlds? It rejects: wrong omp digest (A1), ns off-by-one (A2), self-pinned stub omp (A3), stub instrument output (A4, A5), class deletion (A7, A8), stub omp with live strings (A10). It does NOT reject: shadowing module under `verifiers/` (S1) and extra baseline keys (S4).
- Does the guard's frozen predicate hold? Its own self-test passes (9/9). The guard is necessary but not sufficient for the C1 numeric certification: S1 must be closed before any scored C1 after-value is trusted.

## Recommended repairs (not applied; no production write)

1. Guard: hard-fail any changed path under `verifiers/` or `corpus/` outside an allowlist (the two default dicts and `baseline.json` `measured_against` only); reject any new `.py` whose stem is in `sys.stdlib_module_names`; require the exact `measured_against` key set.
2. Counter (planner decision; frozen predicate): remove the `if row.get("pin") != OPENCODE_PIN: return True` shortcut so omp rows are bound to live omp bytes.
3. Add S1 and S2 fixtures to the guard self-test so each is red.

## Mistakes

| Attempt | Defect | Effect | Repair |
|---|---|---|---|
| Harness v1 | each mutant re-applied `apply_G()` on top of an already-applied G | `0 match(es)`; G commit existed; harness aborted | reset each mutant to base, then apply G once |
| A6 v1 | shadow loaded stdlib json via `from json import scanner` | counter exit 2 (`ImportError`), not a kill | loader with verifiers dir removed from `sys.path` → A6b |
| First launch | background job cap (100) host-wide | harness not started | re-ran in foreground |

## Receipts and environment

- Harness: `build/Kb82M03Controls_mutate.py` sha256 `1eab14fe53d8989e0d211cfea3a4277989dd0180da7e27a9f0f6c5a06656ecf6`; results `build/Kb82M03Controls_mutants.json` sha256 `265736ebf55b33638ac8198158325c211d1b86021ea8fe9bf2d9e648e7a1998e` (harness wall 178 s; counter ~15–17 s per run).
- Probe 2: `build/Kb82M03Controls_probe2.py` sha256 `7c81c3d945e3a8928845a8ead319468cbedca7cfbb03dbfdeda5b604d306e104`; results `build/Kb82M03Controls_probe2.json` sha256 `45dff9d0bae88c27ace16bd571a3e1d62cae13890137c45623939d80fe0b7584` (wall 35 s).
- Revisions and per-run outputs are in the JSON files; the commit hashes are scratch-only and not integration candidates.
- Tools observed, none installed: Python 3.14.8, GNU binutils `strings` 2.47, git 2.56.0.
- Disk guard: scratch 431.6G free before and after.
- Scratch `/fast/scratch/hyaku/kotoba-r82/Kb82M03Controls/` deleted on exit after receipts were copied to `build/`.
- No production after-value scored; no axis score; no 6/6 battery claim; no seat commit or push.

VERDICT: E19 guard rejects wrong omp digest, ns-mtime drift, self-pinned stub omp, stub instrument output and class deletion (guard self-test 9/9 green). It does NOT reject a verifiers/ module that shadows stdlib json (S1: guard 0, counter 0 — both green). The C1 counter's omp pins conjunct is hollow (S2: stub omp with live strings → 3/3, 7/7, 3/3). Numeric C1 certification is not trustworthy until S1 and S2 are closed; C0 meets the target with guard green (S5, planner call).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82M03Controls.md ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M03Controls_mutate.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M03Controls_probe2.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M03Controls_mutants.json ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82M03Controls_probe2.json
