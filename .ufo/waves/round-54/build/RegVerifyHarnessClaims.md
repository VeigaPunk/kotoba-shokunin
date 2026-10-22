Result: PARTIAL — The registry row and source evidence are complete; I withheld the live host run because it reads session-log contents.

| `verifiers/verify_harness_claims.py` | gate | `python3 verifiers/verify_harness_claims.py` | 0=clean, 1=failed, 2=could-not-evaluate, 3=could-not-evaluate | `--self-test` | `verifiers/baseline.json` | none | kotoba |

Evidence for each cell:

- **Name:** The module is `verifiers/verify_harness_claims.py`; `verifiers/README.md:8-10` identifies this verifier and its baseline.
- **Kind:** It compares observations with baseline expectations (`verify_harness_claims.py:556-580, 649-670, 692-698`) and returns 1 on drift, 0 otherwise. That is a gate, not a probe.
- **Entry command:** The module usage at `verify_harness_claims.py:23-27` gives `python3 verifiers/verify_harness_claims.py` as the baseline-check command. I ran `python3 -B verifiers/verify_harness_claims.py --help` from `/fast/scratch/hyaku/kotoba-r54/RegVerifyHarnessClaims`: exit 0; last help line: `                        overrides for fixture testing`.
- **Verdict map:** Source returns 0 for baseline agreement (`:695-698`), 1 for drift (`:695-698`) or failed self-test (`:616-619`), 2 for unreadable environment/I/O (`:639-647`) and argparse usage errors (`:622-634`, argparse's exit 2), and 3 when no baseline is available in human-readable mode (`:692-694`). All are covered by the row; 2 and 3 mean it could not evaluate cleanly.
- **Self-test:** Exact flag `--self-test` is defined at `:625`; implementation at `:583-619`. In the sandbox clone at commit `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, `python3 -B verifiers/verify_harness_claims.py --self-test` exited 0; last line: `self-test: 0 failure(s) over 10 assertions`.
- **Pinned values:** `BASELINE` defaults to the adjacent `baseline.json` (`:52-58, 627`); evaluation reads expected values from `baseline["checks"][id]["expect"]` (`:568-575`). The committed file has those expected values under `checks` (`verifiers/baseline.json:16-39`).
- **Write scope:** No files or network writes found in source review. Inputs use read-only SQLite (`:286-288`), file reads (`:94, 297, 398-408, 460, 479, 653`); the source search found no write APIs. No host-backed run was made. Such a run scans and parses `~/.omp/agent/sessions/**/*.jsonl` (`:383-408`), which is session content I must not read; runtime of that scan is therefore unmeasured. Help and self-test were host-free.
- **Owner:** The frozen registry counter sets `OWNER = "kotoba"` (`check_gate_registry.py:59-65, 180-181`); its row rules require a gate to declare 0=clean, 1=failed, a literal self-test flag and existing pinned path (`:20-36`).

Mismatch / risk:

- `SKILL.md:129-131` and the verifier docstring (`verify_harness_claims.py:29-31`) describe exit 2 as an unreadable environment and exit 3 as no baseline. The source also lets argparse usage errors exit 2 (`:622-634`). More importantly, JSON mode returns 0 when `baseline is None` (`:659-670`), whereas human-readable mode returns 3 (`:692-694`). Thus `--json` combined with a missing baseline or `--no-baseline` is not a clean comparison despite exit 0; the registry row maps the normal gate invocation, but the mode-specific behavior should be considered when reading its 0 verdict.
- `verifiers/README.md:8-10` accurately says 28 checks, four exit codes and `--self-test`; source lists 28 checks (`:524-553`). `verifiers/floors-registry.json:25-27` points to this script with floor 10 and makes no claim about its verdicts or side effects. No mismatch found there.
