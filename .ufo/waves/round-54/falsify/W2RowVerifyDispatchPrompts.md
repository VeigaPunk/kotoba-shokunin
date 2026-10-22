Result: MIXED — row text is accurate and structurally conformant, but the verdict-map cell BREAKS in implementation: two substrate-error conditions (unreadable or undecodable prompt dir/file) exit 1 ("failed") with a traceback instead of the declared 2 ("could-not-evaluate").

# W2RowVerifyDispatchPrompts — attack on the C2 registry row for `verifiers/verify_dispatch_prompts.py`

Row under attack (SKILL.md:474, tip 58db81c):
`| verifiers/verify_dispatch_prompts.py | gate | python3 -B verifiers/verify_dispatch_prompts.py | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | verifiers/checklist-baseline.json, verifiers/fixtures/dispatch-prompts/manifest.json | self-test tree under $TMPDIR | kotoba |`

Method: sandbox clone at 58db81c (`/fast/scratch/hyaku/kotoba-r54/W2RowVerifyDispatchPrompts`), read-only lane git. Script byte-identical to the commit that added the row (git log --follow: last change 542f515, round 50; diff bf65974..58db81c for the script is empty). Self-tests and probes run against temp trees only. No installs performed.

## Cell-by-cell

### Verdict map (0=clean, 1=failed, 2=could-not-evaluate) — BREAKS (script implementation)
All three codes are produced:
- 0: clean temp tree → `PASS dispatch.04` / `PASS dispatch.08`, exit 0 (probe, 0.09s).
- 1: live fleet run → `FAIL dispatch.04: evaluated 321 … 6 FAIL`, exit 1; and every substrate-crash probe below also exits 1.
- 2: missing dir → `ERROR /nonexistent: not a directory`, exit 2; bad flag → argparse exit 2; `--box-proof` missing fixture dir → exit 2.

But the script maps substrate errors to exit 1, contradicting its own docstring ("Exit codes: … 2 usage or substrate error (missing/unreadable directory or map)", verify_dispatch_prompts.py:46-48) and the row's declared meaning:
- Unreadable-but-existing prompts dir: `chmod 000` dir → traceback `PermissionError` (pathlib iterdir) → **exit 1** (should be 2). `main()` catches only `EnvError` (lines 1175-1183); `evaluate_dispatch_04/08` call `prompts_dir.iterdir()` (lines 351, 428), which is not wrapped by `read_text` and not caught.
- Non-UTF-8 prompt file: `UnicodeDecodeError` (a `ValueError`) from `read_text` → traceback → **exit 1**. `read_text` catches only `OSError` (lines 159-163).

No produced code is missing (0/1/2 all reachable), but produced code 1 carries a non-failed meaning, so the cell does not hold "no produced code is missing" — a substrate error is misclassified as `failed`. For comparison, the `--box-proof` mode correctly handles the same class (`except (EnvError, OSError)` → exit 2, lines 1089-1093), so the live path's behavior is the outlier.

### Gate vs probe — HOLDS
The script is a gate: it returns live verdicts and exits 1 on real failures (observed on the live fleet run: `FAIL dispatch.04` exit 1). Not a probe.

### Entry command — HOLDS
`python3 -B verifiers/verify_dispatch_prompts.py` from repo root reads DEFAULT_PROMPTS/STATE_DIR/FLEET (read-only; the live run touched nothing in the lane). No network. Runtime 0.09s << 10 min. Exit codes as observed above.

### Self-test flag — HOLDS
`--self-test` calls `self_test()` directly (line 1152-1153): 56 in-process assertions over synthetic fixtures built under `tempfile.TemporaryDirectory(prefix="dispatch-selftest-")` (line 689). Result: `0 failure(s) over 56 assertions`, exit 0. It is the script's own test (not nested/usage text) and writes only under `$TMPDIR`; no leftover `dispatch-selftest-*` after exit.

### Pinned values — HOLDS (with note)
`verifiers/checklist-baseline.json` and `verifiers/fixtures/dispatch-prompts/manifest.json` both exist at the rev and are read as expected values by `--box-proof` (lines 1027, 1045; box map `disposition=delegated:verifiers/verify_dispatch_prompts.py`, `text_sha256` match; fixture cases `expect_verdict`/`expect_conjunct[_status]` match). `--box-proof` → `boxes proven 2`, exit 0. Note: neither file is read by the default entry command or by `--self-test` (which builds its own fixtures); the default mode's expected values are in-file constants (`PINNED_BOX_SHA`, `CONJUNCTS`). The row lists the real pinned-value locations, so the cell holds, but the read is conditional on the undocumented `--box-proof` mode.

### Write scope (self-test tree under `$TMPDIR`) — HOLDS
All writes in the script are under the TemporaryDirectory (lines 589-603, 656-675, 734-807, 819-822, 857-888, 959-960); it self-removes. The live run writes nothing.

## Regression risk / verification gaps
- The live gate is **red at this rev corner: `python3 -B verifiers/verify_dispatch_prompts.py` exits 1 with `FAIL dispatch.04: … kake-L1.md (report_path_literal,report_stem_is_lane_id), kasegi-L1.md … kengaku-L1.md … kotoba-L1.md … kumitate-L1.md … protocol-L1.md (report_path_literal)`. That is a live-fleet finding, not a row defect, but the row's "clean" state should not be assumed.
- An all-N/A run (empty prompts dir) exits 0 (`N/A dispatch.04/08 … evaluated 0` → exit 0). The docstring says 0 = "all selected checks PASS"; the outer standard reads 0 = clean, and N/A is not a failure — consistent with the row, but worth noting the docstring wording is narrower than the behavior.

## Proposed fix (text only — no lane edits made)
No row-text change needed; the defect is in the script. Proposed patch for `verifiers/verify_dispatch_prompts.py`, `main()` (around lines 1175-1183): catch `OSError` and `ValueError` alongside `EnvError` in the `try` around `run_checks`, printing `ERROR …` (and the `--json` payload in exit_code 2) and returning 2. That makes the script's exit 1 cover only real check failures, matching the declared map, and removes the tracebacks.

## Evidence pointers
- `git log --oneline --follow -- verifiers/verify_dispatch_prompts.py` → last change 542f515 (round 50); script unchanged in bf65974..58db81c.
- `python3 -B verifiers/verify_dispatch_prompts.py` → `FAIL dispatch.04: evaluated 321 …`, exit 1 (0.09s).
- `python3 -B verifiers/verify_dispatch_prompts.py --self-test` → `0 failure(s) over 56 assertions`, exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof` → `boxes proven 2`, exit 0.
- `python3 -B verifiers/verify_dispatch_prompts.py --prompts /tmp/r54-unreadable` (chmod 000) → `PermissionError` traceback, exit 1.
- `python3 -B verifiers/verify_dispatch_prompts.py --prompts /tmp/r54-badutf/prompts` (0xff bytes in prompt) → `UnicodeDecodeError` traceback, exit 1.
- `python3 -B verifiers/verify_dispatch_prompts.py --prompts /nonexistent` → `ERROR /nonexistent: not a directory`, exit 2.
- Clean temp tree → `PASS` both boxes, exit 0; empty temp tree → `N/A` both, exit 0.
- `python3 -B verifiers/check_gate_registry.py --rev 58db81c` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0.
