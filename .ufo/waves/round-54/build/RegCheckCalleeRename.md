Result: DONE — Added the requested self-test in a sandbox-only patch; the prescribed normal verdict output stayed identical.

## Files and behavior
- Sandbox source changed: `verifiers/check_callee_rename.py`. The lane source remains unchanged; its unified diff is delivered at `.ufo/waves/round-54/build/RegCheckCalleeRename.patch` (5,730 bytes, captured from the clone’s `git diff`).
- The new `--self-test` makes isolated temp roots from the pinned gate at `SELF_TEST_REV`, checks a robust case including the expected `omp:rnplant/RNPLANT.md` finding, then injects a check-suppression mutant in a temporary copy and asserts the counter reports it non-robust. No verdict logic or normal counting line was changed. Source: sandbox `verifiers/check_callee_rename.py:145-219,222-234`; temp copy and cleanup: `:169-197`; pinned source: `:64-67`.
- All commands ran in `/fast/scratch/hyaku/kotoba-r54/KotobaR54.RegCheckCalleeRename`; `TMPDIR` was set to that clone’s `.tmp` for executions that create temporary files. No network or host dependency was used. The self-test and normal mode use temporary directories and remove them on exit (`:169-197,237-261`). No tools were installed. No LSP interface was available in the supplied tools.

## Registry rows
Post-patch row (paste after the patch lands):

```text
| `verifiers/check_callee_rename.py` | gate | `python3 -B verifiers/check_callee_rename.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | temp directories under `$TMPDIR` (removed) | kotoba |
```

Truthful row for the unpatched lane file at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`:

```text
| `verifiers/check_callee_rename.py` | gate | `python3 -B verifiers/check_callee_rename.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | none | in-file | temp directory (removed) | kotoba |
```

The second row is not C2-conformant: the frozen registry counter forbids `none` for a gate’s self-test (`verifiers/check_gate_registry.py:29-34,156-166`). The patch supplies the real self-test flag rather than misclassifying a verdict-producing gate as a probe. `in-file` is accurate for expected outcomes/IDs; the committed fixture inputs used by the measurement are listed below.

## Evidence
- `python3 -B verifiers/check_callee_rename.py --help` → exit 0; last help line: `--json`. Patched help lists `--self-test` between `--root` and `--seed`.
- Final self-test command: `TMPDIR=/fast/scratch/hyaku/kotoba-r54/KotobaR54.RegCheckCalleeRename/.tmp python3 -B verifiers/check_callee_rename.py --self-test` → exit 0. Exact output:

```text
PASS self-test robust case: strings-omp-clean.txt exit=0 finding=omp:rnplant/RNPLANT.md
PASS self-test non-robust case: strings-omp-clean.txt exit=1 finding=self-test injected suppression
self-test: 0 failure(s) over 2 assertions
```

  The final line is `self-test: 0 failure(s) over 2 assertions`.
- First self-test attempt in the intermediate sandbox patch exited 1 and printed `FAIL self-test robust case`, `FAIL self-test non-robust case`, and `self-test: 2 failure(s) over 2 assertions`. That version used `FIXTURE_REV` as the known-good gate. The final patch pins the self-test gate to `SELF_TEST_REV=422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4`; the successful final output above is from that version.
- Normal counter before the patch: `TMPDIR=/fast/scratch/hyaku/kotoba-r54/KotobaR54.RegCheckCalleeRename/.tmp python3 -B verifiers/check_callee_rename.py --rev 422ffd10` → exit 0. After the final patch, the same command → exit 0. Both runs printed exactly these same lines:

```text
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 4 of 4 fixtures
```

- Explicit result codes: `0` iff all four fixture cases are robust; `1` otherwise (`verifiers/check_callee_rename.py:37-39,279-289`). `2` is the handled evaluation failure (`:276-278`; the self-test also returns 2 if its pinned setup cannot be evaluated, `:212-215`). Argparse usage errors return 2, including missing/conflicting source options and `--self-test --json` (`:224-234`). The row maps each to `clean`, `failed`, or `could-not-evaluate`, respectively.
- Shortest normal entry command is the `--rev` usage form (`:41-44`). The self-test flag is present in usage and parser (`:44,227`). The counter’s rules require gates to declare 0/1 meanings, a literal self-test flag, non-`none` pins, nonempty write scope, and owner `kotoba` (`verifiers/check_gate_registry.py:20-36,154-181`). Protocol defines a gate as a verdict script that can fail and requires a fixture-based self-test (`PROTOCOL.md:390-402`).
- The pinned measurement inputs read from `FIXTURE_REV` are `verifiers/fixtures/surfaces/strings-omp-clean.txt`, `strings-omp-newcallees.txt`, `strings-omp-18.12.5.txt`, `strings-omp-18.12.6.txt`, `baseline-clean.json`, `baseline-18.12.5.json`, `inventory-clean.md`, and `strings-opencode-clean.txt` (`verifiers/check_callee_rename.py:64-76,241-244,253-268`). Expected check IDs, planted ID, expected outcomes, and self-test expectations are in-file (`:84-86,137-142,178-208`). The script-under-test is taken from `--rev`/`--root` (`:245-252`); self-test uses the separately pinned `SELF_TEST_REV` source (`:64-67,169-174`).

## Documentation match, risks, blockers
- At the unpatched lane tip, `SKILL.md` has no `## Gate registry` section or callee row; its Sources text points registry rows to that section (`SKILL.md:532-533`). `verifiers/README.md:3-6` says rows live in `SKILL.md` and does not describe this verifier. These are absence-before-integration, not contradictory behavior claims.
- `verifiers/floors-registry.json:41-45` records the assertion floor for `verify_surfaces.py`, not this counter; it makes no claim about `check_callee_rename.py`.
- Residual risk: self-test depends on the pinned historical commit remaining readable in the local Git object database and on the pinned gate’s module guard remaining uniquely identifiable (`:64-65,169,186-193`); it fails closed if those assumptions break. No blockers remain for this scoped patch. I did not run the C2 registry verifier, builds, linters, formatters, or other tests.