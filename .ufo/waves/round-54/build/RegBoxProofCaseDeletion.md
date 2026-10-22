Result: DONE — added an isolated `--self-test`; its assertions pass, and valid normal-mode output is identical before and after.

| `verifiers/box_proof_case_deletion.py` | gate | `python3 -B verifiers/box_proof_case_deletion.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/checklist-baseline.json`, `verifiers/fixtures/dispatch-prompts/manifest.json`, in-file | temporary exports/fixture repos under `$TMPDIR`; no checkout writes | kotoba |

Evidence by cell:

- **Name / entry command:** In the sandbox clone at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, parser lines `215-227` define the flags; normal mode checks for the required revision at `381-390`. Before the fix, `python3 -B verifiers/box_proof_case_deletion.py --help` exited 0; its last help line was `                exported tree's manifest instead`.
- **Kind / verdict map:** Docstring lines `37-47` and classifier lines `193-208` define a kill as instrument exit 1 plus proof output and the deleted conjunct name. Main lines `391-428` return 2 for an unreadable checkout/export/tree or intact proof; lines `504-507` return 1 on errored/incomplete coverage, else 0. Missing `--rev` uses `argparse` error status 2 (line `390`). Uncaught exceptions also produce Python status 1; `read_manifest` raises at lines `150-162` and is called at `417` outside the export handler.
- **Self-test:** Literal `--self-test` is in parser lines `225-226`; the isolated repo/test assertions are lines `230-378`. Exact command from the clone: `TMPDIR="$PWD/.scratch-tmp" python3 -B verifiers/box_proof_case_deletion.py --self-test` → `self-test: 0 failure(s) over 10 assertions`, exit 0. It exercises exit 0 for six killed must-fail cases plus a surviving control; a second fixture revision asserts exit 1 when one must-fail deletion survives, and checks stable killed/survived findings.
- **Pinned values:** Lines `61-79` pin the manifest and map paths, six `CONJUNCTS`, and two accepted `PROVEN_LINES`. The baseline map is passed to the instrument at lines `182-190`; manifest cases are selected at lines `417-418`, `460-477`. The committed expected-value inputs are `verifiers/checklist-baseline.json` and `verifiers/fixtures/dispatch-prompts/manifest.json`.
- **Write scope:** Main mode's `TemporaryDirectory`, export, fixture copies, and manifest rewrites are at lines `396-399`, `449-456`; self-test writes only its temporary fixture repositories at lines `292-378`. Both normal-mode runs and the self-test used `TMPDIR="$PWD/.scratch-tmp"` inside the clone. No network or live-checkout writes were made.
- **Owner:** The frozen registry owner is `kotoba` (`verifiers/check_gate_registry.py:61-65`).

Patch delivered at `.ufo/waves/round-54/build/RegBoxProofCaseDeletion.patch`; the target source was changed only in the sandbox clone. No C2 registry counter was run; the parent owns that check.

Self-test output:

```text
self-test: 0 failure(s) over 10 assertions
EXIT=0
```

Normal-mode comparison, both run in the sandbox clone:

- Before the patch: `TMPDIR="$PWD/.scratch-tmp" python3 -B verifiers/box_proof_case_deletion.py --rev HEAD --repo "$PWD"` → exit 0.
- After the patch: same command → exit 0.

The stdout and exit line were identical in both observed runs; shared transcript:

```text
control: exit 0 boxes proven 2
fixtures: --fixtures
case d04-placeholder (report_path_literal): exit 1 killed
case d04-stem (report_stem_is_lane_id): exit 1 killed
case d04-unknown-lane (lane_identity_known): exit 1 killed
case d08-role-round (filename_role_round_equal): exit 1 killed
case d08-report-dir-round (filename_report_dir_round_equal): exit 1 killed
case d08-above-state (round_le_latest_dispatched): exit 1 killed
control d04-control: exit 1 killed
control d08-control: exit 1 killed
na d08-missing-state: exit 1 killed
controls killed 2 of 2
na killed 1 of 1
killed 6 of 6
EXIT=0
```


Mismatch note: the frozen counter requires a gate's self-test flag to be literal and pinned values non-`none` (`verifiers/check_gate_registry.py:29-36`); the patch now supplies the flag and the row supplies existing pinned paths. At the pre-integration tip, SKILL.md only cross-referenced the registry at `:532-533`, and `verifiers/README.md:3-6` says rows live in SKILL.md; neither had a target-specific entry. `verifiers/floors-registry.json:3-56` omits this script from its separate assertion-floor list. The script docstring still calls its old C2 “operability” (`:2`); round 54 names C2 “consistency” in `plans/round-54.md:38-41`.
