# ReviewerC2 — independent C2 attack

## Findings by severity

No blocking defect introduced by the C2 path/pin diff. Recommendation only: the wrong-binary and deleted-pin kill controls reject; this is not an admission or shipment decision.

**Residual, medium (pre-existing): coarse mtime pins can pass without nanosecond equality.** `verifiers/check_substrate_pins.py:145-168` computes a precision-dependent tolerance, and `:258-261` tests its absolute value. W10 uses `2026-11-01T17:11:08-03:00`, a later second than the actual stamp, yet exits 0:

```
PASS omp_binary_mtime: delta -718191196 ns (tolerance 999999999 ns)
OK 3/3 pins hold
```

W9 and W11 also pass second/millisecond precision. This is explicit existing behavior, not a newly introduced regression or a wrong-binary bypass: SHA256 remains exact. Thus a non-ns control does exit 0 if one expects all non-ns records to fail, but that expectation is NOT enforced by the existing guard. The actual candidate uses 9 digits, delta 0 and tolerance 0; W13 (1 ns error) exits 1. Do not describe the guard as enforcing nanosecond record *format* globally.

**Low, documentation:** historical round-72 wrapper comments remain directly above the round-85 corrections in three verifiers. They are dated, not active constants; no missing-path default remains. See search table below.

## Independent host derivation and candidate

Commands and complete output: `host-sha.txt`, `host-stat.txt`, `host-file.txt`, `host-version.txt`, and `candidate-comparison.json` beside this report.

- `sha256sum /home/vgpnk/.local/bin/omp`: `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`.
- `stat -c '%y' /home/vgpnk/.local/bin/omp`: `2026-11-01 17:11:07.281808804 -0300`.
- Normalizing its separator and offset gives `2026-11-01T17:11:07.281808804-03:00`; `st_mtime_ns=1793563867281808804`.
- `file`: x86-64 ELF, dynamically linked, 276785328 bytes (size also in surfaces receipt).
- `omp --version`: `omp/18.15.0`.
- ExecC2Pin's `baseline.json.candidate:5-6` matches independently derived SHA and ns ISO mtime exactly (`candidate_sha_exact=true`, `candidate_mtime_exact=true`). Candidate scoring with `python3 -B verifiers/check_substrate_pins.py --baseline <candidate>` exits 0, `OK 3/3 pins hold`, mtime delta/tolerance 0 ns.

Command caveat: `%Y-%m-%dT%H:%M:%S.%N%:z` is a strftime-style format, not GNU stat's format. The literal requested `stat -c` invocation exits 0 but prints `1793563867-/home-56T?:?:?./home/vgpnk/.local/bin/omp?z` (receipt `stat-format-caveat.txt`). `%Y` in stat is epoch seconds. I used `%y` plus exact textual normalization, not that malformed output, for the candidate comparison.

## Control table

All W rows below were scored with `python3 -B verifiers/check_substrate_pins.py --baseline <scratch-world>` and NO binary override after the constant move. `matrix.json` retains every exact stdout/stderr line; `matrix-output.txt` also retains the frozen HEAD/omp.real control column. The old unreadable defaults were observed before the writer moved the constants; they are not findings against the completed cutover.

| Control | exit | Exact summary |
|---|---:|---|
| W0 truthful baseline (host values re-derived by ReviewerC2) | 0 | `OK 3/3 pins hold` |
| W1 committed baseline as at HEAD (18.12.6 pins) | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` |
| W2 opencode sha under omp_binary_sha256 | 1 | `DRIFT 1/3 pins failed: omp_binary_sha256` |
| W3 both omp pins deleted | 1 | `PIN_ABSENT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` |
| W4 only omp_binary_mtime deleted | 1 | `PIN_ABSENT 1/3 pins failed: omp_binary_mtime` |
| W5 unregistered substrate pin (cursor) | 2 | `UNSUPPORTED 1/4 pins failed: cursor_binary_sha256` |
| W6 pin value not a string (epoch int) | 3 | `BAD_PIN 1/3 pins failed: omp_binary_mtime` |
| W7 mtime with 10 fractional digits | 3 | `BAD_PIN 1/3 pins failed: omp_binary_mtime` |
| W8 mtime naive (no UTC offset) | 3 | `BAD_PIN 1/3 pins failed: omp_binary_mtime` |
| W9 mtime coarse: seconds only, correct second | 0 | `OK 3/3 pins hold` |
| W10 mtime coarse: seconds only, WRONG second (+1s) | 0 | `OK 3/3 pins hold` |
| W11 mtime ms precision (3 digits) | 0 | `OK 3/3 pins hold` |
| W12 mtime space-separated (GNU stat %y form) | 0 | `OK 3/3 pins hold` |
| W13 mtime ns-exact, off by 1 ns | 1 | `DRIFT 1/3 pins failed: omp_binary_mtime` |
| W14 measured_against null (vacuity) | 1 | `VACUOUS 1/1 pins failed: -` |
| W15 measured_against empty object | 1 | `PIN_ABSENT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256` |
| W16 omp pin zeroed (a different ELF's sha) | 1 | `DRIFT 1/3 pins failed: omp_binary_sha256` |

Additional real-path controls using the actual candidate, not a zeroed SHA substitute:

| Control | exit | Exact summary |
|---|---:|---|
| `--omp-binary /home/vgpnk/.opencode/bin/opencode` | 1 | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` |
| `--omp-binary <scratch>/absent-omp` | 2 | `UNREADABLE 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` |

Receipts: `wrong-elf-candidate.txt`, `missing-path-candidate.txt`. Malformed values use the guard's existing exit-3 BAD_PIN tier, not the new-instrument 0/1/2 convention; no exit-code logic changed in this diff.

## Remaining omp.real search table

Literal fallback search over `verifiers/` and `SKILL.md`, captured in `omp-real-search.txt`. No SKILL.md matches. Each surviving line is classified, including executable test data that is not a host path:

| Location | Classification | Meaning |
|---|---|---|
| `verifiers/baseline.json:15` | Documentation/data | Historical round-72 path and wrapper note |
| `verifiers/baseline.json:17` | Documentation/data | Round-85 note explicitly says omp.real is absent |
| `verifiers/check_report_pointers.py:80` | Documentation | Dotted non-pointer example |
| `verifiers/check_report_pointers.py:658` | Test fixture data | Dotted non-pointer example, not binary resolution |
| `verifiers/check_report_pointers.py:772` | Live test assertion | Checks non-pointer token is absent from output; not a filesystem path |
| `verifiers/check_substrate_pins.py:64` | Comment | Dated round-72 historical substrate |
| `verifiers/check_substrate_pins.py:67` | Comment | Round-85 absence correction |
| `verifiers/check_substrate_repin_v2.py:13` | Documentation | Historical round-72 claim description |
| `verifiers/verify_harness_claims.py:53` | Comment on live assignment | Assignment now uses `.local/bin/omp`; only comment mentions omp.real |
| `verifiers/verify_harness_independent.py:124` | Comment | Round-85 absence correction |
| `verifiers/verify_surfaces.py:165` | Comment | Dated round-72 historical substrate |
| `verifiers/verify_surfaces.py:168` | Comment | Round-85 absence correction |

Four changed defaults resolve the same installed ELF: pins `:69`, surfaces `:170`, claims `:53`, independent harness `:125`. Their argparse default callsites are respectively pins `:312`, surfaces `:2433`, claims `:629`, independent `:1718`. This is textual tracing plus exercised pins/surfaces, not semantic LSP proof.

## Surfaces, inventory and diff

`python3 -B verifiers/verify_surfaces.py --json`, with no override, exits 0: pass 7, fail 0. `surfaces-tree.json` identifies `/home/vgpnk/.local/bin/omp` with SHA `6737ee24…`, identical to the independently hashed ELF and candidate. Exact inventory detail: `inventory id set == baseline id set (42 ids)`; `all 8 extracted loader class(es) declared`. Literal and kind parity each report 42 rows.

`committed-scoped-diff.txt` records the actual base-to-reviewed-HEAD diff: four path constants, explanatory comments, two omp pin values, and a round-85 historical note. No `surfaces-baseline.json` change; extraction and pin comparison logic unchanged. Working-tree edits were committed by the integrator during review; `review-revision.txt` records the later observed HEAD. I performed no git writes or production edits.

## Vacuity verdict and gaps

Non-vacuous for the frozen C2 kill rule: opencode SHA under the omp pin fails 1, deleted omp pins fail 1, and the actual candidate against opencode's different ELF fails 1. No wrong-binary/deleted-pin control exited 0. Missing paths fail 2. Coarse-mtime controls do exit 0 as documented above; their SHA still names the correct binary.

LSP device unavailable (`read xd://lsp` returned `No such tool`), therefore references/definitions/diagnostics could not be queried; searches are literal fallback only. Harness claims/independent default callers were inspected, not executed. No resume paths, alternate runtimes, routing identities or saturation claim were changed by this scoped diff. Final integrated-tip reruns belong to the main agent. Tools installed/updated: none.

Self-evaluation: accuracy 4 (mutable tree snapshot, receipts label it); completeness 4 (LSP unavailable); clarity 4 (full matrix retained separately); actionability 4 (coarse-format limitation explicitly separated from the kill rule); conciseness 4 (required tables make this longer than a verdict). Improvements applied: distinguish pre-fix evidence from completed cutover, and retest actual candidate against the different ELF rather than relying on a zeroed SHA. Overall 4.0; confidence scoped to retained observations.
