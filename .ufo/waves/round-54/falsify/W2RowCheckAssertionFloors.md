Result: BREAKS — The verdict map conflates an unparseable child result with `failed`, and the write-scope cell omits a nested test’s temporary writes under the repo fixture tree.

## Findings (by severity)

### Medium — Verdict map: BREAKS

The landed row (`SKILL.md` at bf65974, line 443; identical text at tip line 457) declares `0=clean, 1=failed, 2=could-not-evaluate`. The source explicitly puts “summary could not be parsed” and “instrument could not be run” under exit 1 (`verifiers/check_assertion_floors.py:44-48`). In `main`, only `TimeoutExpired` is routed to `run_error`/exit 2 (`:525-533`); a missing summary makes `ok` false (`:534-542`) and the final result is exit 1 (`:543-545`). A child that cannot provide a verdict is not a `failed` measurement under the protocol’s outer classes (`PROTOCOL.md:390-397`).

Direct sandbox discriminator: I pointed all 13 `--script` overrides at a unique stub that exits 0 without a summary. The gate printed `FAIL … summary=missing` for all 13 and exited 1 (`UNPARSEABLE_CHILD_EXIT=1`). The stub was created and removed inside the sandbox clone. Thus code 1 is produced, but this path means “could not evaluate,” not `failed`. The source also leaves non-timeout `subprocess.run` launch errors uncaught (`:526-533`), which likewise does not give a deliberate `could-not-evaluate` result.

There is no truthful row-only map for this mixed code. Correct the verifier to route missing/unparseable child summaries and child-launch errors to code 2, retaining code 1 for a validly measured failed self-test; then keep `1=failed, 2=could-not-evaluate` in the row. The declared row text alone cannot repair the current behavior.

### Low — Write scope: BREAKS

The gate’s own fixture battery writes under `tempfile.TemporaryDirectory` and cleans it (`verifiers/check_assertion_floors.py:548-550, 648-664`). But the entry loop runs every registered child’s `--self-test` (`:168-169, 525-529`). The nested `compare_harness_independent.py --self-test` calls `fixture_battery()` (`verifiers/compare_harness_independent.py:2387`); its committed `scope-file-cwd` case selects the process-CWD arm (`verifiers/fixtures/compare-harness-independent/scope-file-cwd/case.json:17-19`), which creates temporary directories under `FIXTURE_DIR`, not `$TMPDIR` (`compare_harness_independent.py:1433, 1498-1505, 1576-1585`). Both are cleaned in `finally` (`:1615-1619`), but this is still part of the entry command’s observable write scope.

Proposed corrected write-scope cell: `temp fixtures under $TMPDIR; removable temporary directories under verifiers/fixtures/compare-harness-independent`.
Proposed full row after correcting the verifier’s return-code classification above:

| `verifiers/check_assertion_floors.py` | gate | `python3 -B verifiers/check_assertion_floors.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/floors-registry.json` | temp fixtures under `$TMPDIR`; removable temporary directories under `verifiers/fixtures/compare-harness-independent` | kotoba |

The verdict-map text is valid only after the source uses code 2 for child results that cannot be evaluated; without that code change, no row-only wording is accurate.

## Cell-by-cell result

- **Name — HOLDS.** The row names the existing script (`SKILL.md@bf65974:443`; its self-registration as `floors_guard` is at `check_assertion_floors.py:170-171`).
- **Kind — HOLDS.** It compares instrument self-test outputs and assertion floors against persisted expected values, then returns a verdict (`check_assertion_floors.py:312-388, 523-545`), matching the protocol definition of a gate (`PROTOCOL.md:390-397`).
- **Entry command — HOLDS.** Ran from the sandbox clone at `58db81c4465b0e9b07ef2485b87d8970683afac6`; all 13 instruments printed `PASS`, ending `PASS alwayson observed=89 floor=89`, exit 0. The required bare invocation also completed in 46.275 s. A constrained rerun with `TMPDIR` inside the clone completed in 1:34.75, exit 0, ending on the same PASS line; it stayed below 10 minutes and required no network.
- **Verdict map — BREAKS.** See the finding above. The clean path and failed/unparseable path returned 0 and 1 respectively; code 2 is produced for registry drift/escape and timeout (`check_assertion_floors.py:469-478, 491-496, 517-521, 530-545`). Normal explicit control flow produces only 0, 1, and 2 (`:453-545, 1206-1207`), with argparse usage errors also using 2.
- **Self-test — HOLDS.** `--self-test` dispatches to this script’s own `self_test()` (`check_assertion_floors.py:459-463, 548-593`), which runs its own fixture battery under a temporary directory (`:648-664`) and checks fixture subprocess exit codes. It is not usage text or merely a nested verifier call. Ran the flag in the sandbox: `0 failure(s) over 150 assertions`, exit 0 (1.35 s with sandbox-local `TMPDIR`).
- **Pinned values — HOLDS.** `REGISTRY_REL` is `verifiers/floors-registry.json` (`check_assertion_floors.py:151`); the script reads and parses it (`:320-328`) and checks each entry’s path/floor against both in-file tables (`:343-380`).
- **Write scope — BREAKS.** See the finding above. The guard’s direct fixtures are under `$TMPDIR`, but the nested comparator test also creates and removes temporary directories under the committed fixture directory.
- **Owner — HOLDS.** `kotoba` is the row owner (`SKILL.md@bf65974:443`) and the frozen counter’s owner value (`check_gate_registry.py:65, 180-181`).

## Residual risk and verification gaps

The source file is unchanged between bf65974 and the reviewed tip; the row text is likewise unchanged apart from line number. The exact bare entry and self-test commands were run in the sandbox using the ambient `TMPDIR` (its value was not recorded). After source review showed nested tests create temporary fixtures, both commands were rerun with `TMPDIR` directed inside the clone. Final sandbox `git status --porcelain` was empty, and no `.fixture-*`/`.scope-cwd-*` directories remained under the comparator fixture root. The local temporary directory was removed.

No `lsp` device or LSP status interface is exposed in the available tools, so no LSP semantic checks were possible; no grep result is used as semantic proof. No installs were made.