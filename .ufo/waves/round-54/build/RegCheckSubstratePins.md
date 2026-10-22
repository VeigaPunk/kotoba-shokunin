Result: DONE — the source and isolated runs support a gate row with exit codes 0–3 and `verifiers/baseline.json` as its pinned-value file.

Axes: consistency (row semantics), safety (bounded writes), evidence (source and observed runs).

Files changed: only this assigned report. The requested sandbox clone is at `/fast/scratch/hyaku/kotoba-r54/RegCheckSubstratePins`; no implementation files were edited.

## Registry row

| `verifiers/check_substrate_pins.py` | gate | `python3 -B verifiers/check_substrate_pins.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | self-test temp files under `$TMPDIR`; otherwise none | kotoba |

## Evidence by cell

- **Name:** the sandbox file is `verifiers/check_substrate_pins.py`; shebang and docstring: `verifiers/check_substrate_pins.py:1-2`.
- **Kind:** the docstring says code 0 means every expected pin holds, while code 1 means drift, a missing expected pin, or vacuity (`:9-32`). `VERDICT_CODE` maps only `PASS` to 0 and maps `DRIFT`, `PIN_ABSENT`, and `VACUOUS` to 1 (`:115-130`). Thus 1 is a gate failure, not a probe result. The frozen registry rules require a gate to declare `0=clean` and `1=failed` (`verifiers/check_gate_registry.py:20-36`).
- **Entry command:** the script defaults its repository to its own grandparent (`:63`) and defaults the baseline to `<repo>/verifiers/baseline.json`; it has no required argument (`:302-320`). The shortest root-relative Python invocation is in the row. Help command `python3 -B /fast/scratch/hyaku/kotoba-r54/RegCheckSubstratePins/verifiers/check_substrate_pins.py --help` exited **0**. Its final output line was `                        only` (the wrapped end of the `--self-test` help text).
- **Verdict map:** `VERDICT_CODE` defines 0–3 (`:115-125`); `check_pins` and `main` give their conditions (`:167-259`, `:322-339`). Specifically: **0** all expected pins pass; **1** drift, expected pin absent, or `measured_against` absent/null/non-mapping; **2** binary read/stat failure (`UNREADABLE`) or unsupported substrate/kind/key (`UNSUPPORTED`); **3** unreadable/unparseable/non-object baseline (`NO_BASELINE`) or invalid pin value (`BAD_PIN`). Codes 2 and 3 mean the comparison could not be evaluated, rather than a measured pin drift. An unknown CLI option also exits 2: `python3 -B /fast/scratch/hyaku/kotoba-r54/RegCheckSubstratePins/verifiers/check_substrate_pins.py --bad-option` → **2**, `argparse` usage error.
- **Self-test:** literal flag declaration and dispatch are at `:311-316`; temporary fixture setup and the return rule are at `:349-380`, `:564-567`. Command `TMPDIR=/fast/scratch/hyaku/kotoba-r54/RegCheckSubstratePins python3 -B /fast/scratch/hyaku/kotoba-r54/RegCheckSubstratePins/verifiers/check_substrate_pins.py --self-test` exited **0**; final output line: `0 failure(s) over 62 assertions`. Setting `TMPDIR` to the clone kept the temporary fixture writes inside it.
- **Pinned values:** `EXPECTED_PINS` names `omp_binary_sha256`, `omp_binary_mtime`, and `opencode_binary_sha256` (`:75-79`); default loading reads `verifiers/baseline.json` (`:318-324`). That committed file has the `measured_against` block and values at `verifiers/baseline.json:4-10`. The README explicitly says `verifiers/fixtures/pins/` is evidence-only (`verifiers/README.md:11-15`); the verifier source uses temporary fixtures for self-test, not that directory (source `:361-395`; source search finds `fixtures` only in the `--self-test` help text at `:311-312`).
- **Write scope:** normal mode opens baseline and binaries read-only and never executes a pinned binary (`:34-46`); self-test uses `TemporaryDirectory` and writes its fixtures there (`:361-391`), including fixture-only `utime`/permission changes (`:418-422`, `:508-514`). The default gate run in the sandbox exited **0** and ended `OK 3/3 pins hold`; output was three `PASS` lines and that summary. It read the host-anchored binaries at paths in `:64-67`, so this is a read-only result for this host, not a portable clone-only result.
- **Owner:** `OWNER = "kotoba"` in `verifiers/check_gate_registry.py:59-65`.

## Documentation comparison

- `verifiers/README.md:11-15` agrees: baseline `measured_against` pins, three named pins, exit codes 0/1/2/3, `--self-test` temporary fixtures, fixture directory evidence-only, and no pinned-binary execution. No behavior mismatch found.
- At this revision, `SKILL.md:532-533` points to `verifiers/README.md` and says registry rows belong in § Gate registry, but the actual `## Gate registry` heading/table and this row are absent. That is the C2 row to add, not a discrepancy in the script description.
- `verifiers/floors-registry.json:33-36` records floor 62 for this verifier. The self-test returned 62 assertions; `verifiers/check_assertion_floors.py:164-165` also pins this file at 62. No floor mismatch found.

## Risks and blockers

Risk: default execution depends on host-installed binary paths (`:40-46`, `:64-67`); the observed green is host-specific. The script itself states it does not execute those binaries. No blockers. No tools were installed.