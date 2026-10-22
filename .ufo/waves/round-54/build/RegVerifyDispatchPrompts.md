Result: DONE — Audited the dispatch-prompts verifier and prepared its C2 registry row; no verifier code or existing documentation was changed.

## Registry row

| `verifiers/verify_dispatch_prompts.py` | gate | `python3 -B verifiers/verify_dispatch_prompts.py` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file; `verifiers/checklist-baseline.json`; `verifiers/fixtures/dispatch-prompts/manifest.json` | none in live/proof modes; `--self-test` temp tree under `$TMPDIR` | kotoba |

### Evidence by cell

- **Name:** `verifiers/verify_dispatch_prompts.py` is the module name and its docstring's declared subject (`verifiers/verify_dispatch_prompts.py:1-3`).
- **Kind:** The live mode returns 1 when a selected check is `FAIL` (`verifiers/verify_dispatch_prompts.py:1184`); box proof returns 1 when fewer than two boxes are proven and there was no substrate error (`:1145-1147`); the self-test returns 1 on failed assertions (`:975-978`). It is a gate, not a probe.
- **Entry command:** Defaults are the host's `.ufo/prompts`, `.ufo/state`, and fleet root (`:98-100`); the parser defaults to both checks (`:527-528`) and `main` dispatches to them (`:1150-1197`). In the sandbox clone, `python3 -B verifiers/verify_dispatch_prompts.py --help` exited 0; last line: `--json                machine-readable output`. The default entry command was also run read-only from the clone against those host paths; exact output and exit code are recorded below.
- **Verdict map / exit codes:** The docstring declares 0/1/2 (`:46-48`). Controlled code paths: **0** = no live check is `FAIL` (`:1184`), both boxes proven (`:1147`), all self-test assertions pass (`:978`), or argparse help; **1** = a live check is `FAIL` (`:1184`), a box proof is incomplete/incorrect (`:1147`), or self-test assertions fail (`:975-978`); **2** = argparse usage error (`:1151`; documented at `:46-47`), a required directory is absent/not a directory (`:1162-1173`), live input raises `EnvError` (`:1175-1183`), proof map/manifest cannot be read or parsed (`:1026-1051`), or a proof fixture hits an `OSError`/`EnvError` (`:1084-1092`, `:1145-1146`).
- **Self-test:** The exact flag is literal in the parser (`:529-531`). In the clone I ran `mkdir -p /fast/scratch/hyaku/kotoba-r54/RegVerifyDispatchPrompts/.tmp && TMPDIR=/fast/scratch/hyaku/kotoba-r54/RegVerifyDispatchPrompts/.tmp python3 -B verifiers/verify_dispatch_prompts.py --self-test`; exit 0, last line `0 failure(s) over 56 assertions`. The self-test uses `TemporaryDirectory` (`:689`) and builds/removes fixture trees there (`:590-603`, `:625-677`, `:857-960`).
- **Pinned values:** `PINNED_BOX_SHA`, `CONJUNCTS`, allowed co-failure and N/A conjunct are in-file (`:105-137`). Proof mode reads the default map `verifiers/checklist-baseline.json` (`:92-96`, `:1154-1158`), compares both delegation/hash values and the live `SKILL.md` hashes to those constants (`:1026-1070`), then reads `verifiers/fixtures/dispatch-prompts/manifest.json` for expected verdicts/conjunct statuses (`:1044-1051`, `:1071-1139`). The committed map has dispatch.04 and dispatch.08 delegated to this script (`verifiers/checklist-baseline.json:168-196`); the manifest contains the expected PASS/FAIL/N/A values (`verifiers/fixtures/dispatch-prompts/manifest.json:1-82`). The case directories under that fixture tree supply evaluated prompts/state/fleet inputs; the manifest and in-file pins are the expected values.
- **Write scope:** Live and `--box-proof` paths read inputs without writing (`:349-511`, `:985-1147`). Only `--self-test` writes temporary fixtures, under `tempfile.TemporaryDirectory` (`:590-603`, `:625-677`, `:689`, `:857-960`); my run set `TMPDIR` inside the clone. No network access or install was used.
- **Owner:** The frozen counter pins owner `kotoba` (`verifiers/check_gate_registry.py:60-65`). Its docstring requires gate rows to have 0=clean, 1=failed, a literal self-test flag, and non-`none` pinned values (`verifiers/check_gate_registry.py:20-36`).

### Retained command evidence

- Help: `python3 -B verifiers/verify_dispatch_prompts.py --help` (cwd: sandbox clone) — exit 0; last line `--json                machine-readable output`.
- Self-test: command above — exit 0; last line `0 failure(s) over 56 assertions`.
- Host-backed live run: `python3 -B verifiers/verify_dispatch_prompts.py` (cwd: sandbox clone; defaults from `:98-100`; read-only) — exit 1, exact output:
  ```
  FAIL dispatch.04: evaluated 320 — 320 file(s) evaluated: 292 PASS, 6 FAIL, 22 N/A; 28 out of scope; failing files: kake-L1.md (report_path_literal,report_stem_is_lane_id), kasegi-L1.md (report_path_literal,report_stem_is_lane_id), kengaku-L1.md (report_path_literal,report_stem_is_lane_id), kotoba-L1.md (report_path_literal,report_stem_is_lane_id), kumitate-L1.md (report_path_literal,report_stem_is_lane_id), protocol-L1.md (report_path_literal)
  PASS dispatch.08: evaluated 312 — 312 file(s) evaluated: 283 PASS, 0 FAIL, 29 N/A; 13 out of scope
  command_exit=1
  ```

### Mismatches and risks

- The script docstring says exit 0 means all selected checks PASS (`:46-47`), but the implementation returns 0 whenever no result is `FAIL` (`:1184`); `_finish` can produce `N/A` (`:492-501`). Thus a run with only N/A checks can exit 0. The row's `0=clean` follows the frozen registry vocabulary, but this is a code/docstring semantics gap.
- `SKILL.md:142-153` correctly names the delegation and six observed-conjunct must-fail cases, but its `--box-proof` summary omits additional implemented requirements: all-PASS controls and a dispatch.08 N/A case (`verifiers/verify_dispatch_prompts.py:989-1003`, `:1133-1138`). This is an under-description, not a contradiction. `verifiers/README.md` has no `verify_dispatch_prompts.py`, `dispatch.04`, `dispatch.08`, or `box-proof` match; `verifiers/floors-registry.json:45-48` only records its path and floor 56, with no conflicting behavior claim.
- [INFERENCE] `evaluate_dispatch_04/08` call `Path.iterdir()` (`:351`, `:428`) and `main` catches `EnvError`, not arbitrary `OSError` (`:1175-1183`). A directory-enumeration error could therefore escape as a Python traceback/status 1 rather than the documented could-not-evaluate status 2; this was not induced or tested.

Files changed: only this assigned report. No blocker.