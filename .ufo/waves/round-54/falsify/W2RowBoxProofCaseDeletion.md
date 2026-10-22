Result: MIXED — the C2 registry row for `verifiers/box_proof_case_deletion.py` holds on 7 of 8 cells, but the verdict-map cell BREAKS: could-not-evaluate inputs (bad `--rev`, corrupt manifest at `<rev>`) exit 1 with a traceback instead of the declared `2=could-not-evaluate`.

Scope: row `| verifiers/box_proof_case_deletion.py | gate | python3 -B verifiers/box_proof_case_deletion.py --rev <rev> | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | verifiers/checklist-baseline.json, verifiers/fixtures/dispatch-prompts/manifest.json | temp exports under $TMPDIR | kotoba |`, `SKILL.md:455` at tip `58db81c4465b0e9b07ef2485b87d8970683afac6` (same row at `bf65974c:SKILL.md:441`; script blob `9328108d…` identical at `bf65974c` and tip, verified by `git rev-parse <rev>:verifiers/box_proof_case_deletion.py`).

All work in sandbox clone `/fast/scratch/hyaku/kotoba-r54/W2RowBoxProofCaseDeletion` at `58db81c4`. Line numbers are `verifiers/box_proof_case_deletion.py` there.

## Cell-by-cell

**Name — HOLDS.** `verifiers/box_proof_case_deletion.py` is a blob directly under `verifiers/` at `bf65974c` and at tip; row name matches exactly.

**Kind `gate` — HOLDS.** Re-runnable verdict script: reads the exported tree at `<rev>`, compares deletions-killed against the in-file pinned denominator `CONJUNCTS` (six conjuncts, lines 70-77) and returns a verdict that can fail (`return 0 if killed == 6 else 1`, line 507; errors → `return 1`, line 506). It can fail → gate per PROTOCOL.md § Gate standard ("a tool that cannot fail is a probe").

**Entry command — HOLDS.** `python3 -B verifiers/box_proof_case_deletion.py --rev 58db81c4465b0e9b07ef2485b87d8970683afac6` run in the sandbox: exit 0, 1.35 s wall, no network (subprocesses are local `git` and `sys.executable` only, lines 130, 173-176, 184-189). Last lines: `controls killed 2 of 2` / `na killed 1 of 1` / `killed 6 of 6`. `--rev` is enforced at lines 389-390.

**Verdict map `0=clean, 1=failed, 2=could-not-evaluate` — BREAKS.**
Declared codes are all genuinely produced with the right meaning on the scripted paths: `2` at lines 394 (not a git checkout), 404 (`git archive` DriverError), 410 (missing instrument), 415 (missing manifest), 428 (intact control nonzero); `1` at 506-507 (runs errored / killed < 6); `0` at 507 (killed 6 of 6). Usage errors exit 2 via `ap.error` (lines 386, 390) — consistent with the declared 2.
But two could-not-evaluate inputs escape the map as exit 1 tracebacks:
- `--rev deadbeef…` (nonexistent rev): `git archive` fails with empty stdout; `tarfile.ReadError: empty file` raises inside the extraction loop (line 133-137) before the `DriverError` re-raise at lines 143-147 is reached, so `export_tree` propagates an uncaught exception. Observed: traceback ending `tarfile.ReadError: empty file`, `BADREV_EXIT=1`. Docstring line 83 names "bad revision" as the canonical `DriverError` (could-not-evaluate) case — the intended 2 is unreachable for the common failure shape.
- Corrupt `verifiers/fixtures/dispatch-prompts/manifest.json` at `<rev>`: `read_manifest` raises `DriverError("cannot parse …")` at lines 156-159, but the call at line 417 sits outside the try covering `export_tree` (lines 400-404), so it propagates. Observed on a scratch commit (`009a1dbc…` in the sandbox): traceback `DriverError: cannot parse …/manifest.json`, `MALFORMED_EXIT=1`.
Also uncaught-by-construction (read, not reproduced): `subprocess.TimeoutExpired` from `run_box_proof` (timeout 600, lines 188-189; the `--help` probe's timeout is caught at 177), `tarfile`/`shutil.copytree`/`OSError` crashes — all exit 1.
Severity: minor-moderate honesty defect. No produced code is undeclared (all crashes land on declared code 1), but `1=failed` is produced for revisions that were never evaluated — a bad `--rev` reports as a measured box-proof failure. The row states the intended map; the script violates it on crash paths.

**Self-test `--self-test` — HOLDS.** Flag defined at lines 225-226 and dispatched to `self_test()` at 384-388. It is the script's own self-invocation: builds an isolated temp git repo (`TemporaryDirectory`, line 292), a stub instrument and fixture manifest (lines 250-317), then calls `main(["--rev", rev, "--repo", str(repo)])` (line 344) and asserts both exit codes (0 and 1, lines 348, 362) and stable finding strings (`case d04-placeholder (report_path_literal): exit 1 killed`, `killed 6 of 6`, `killed 5 of 6` — lines 349-370). Observed: `self-test: 0 failure(s) over 10 assertions`, `EXIT=0`. Not a nested call or usage text; satisfies the Erratum-2 guard (gate row + declared flag exits 0 at the measured revision).

**Pinned values `verifiers/checklist-baseline.json`, `verifiers/fixtures/dispatch-prompts/manifest.json` — HOLDS.** Both exist at `bf65974c` and tip. `manifest.json` is read by the script itself from the exported tree (`read_manifest(manifest_path)`, line 417; `MANIFEST_REL` lines 62-63) and supplies the per-case expected values it scores against (`expect_conjunct`/`expect_verdict`/`check` at 467-470, 483-484). `checklist-baseline.json` (`MAP_REL`, line 65) is passed as `--map verifiers/checklist-baseline.json` to the instrument at line 185 — the pinned expected-verdict source for the box proof the script runs; the kill verdict depends on it. The script relays rather than `open()`s it, which matches how the instrument's own row (SKILL.md:474) lists the same two files. Note the pinned denominator itself is in-file (`CONJUNCTS`, 70-77); the two paths are the repo-persisted expected values.

**Write scope `temp exports under $TMPDIR` — HOLDS.** All writes land under `tempfile.TemporaryDirectory(prefix="box-proof-case-deletion-")` (line 396): the `git archive` export (lines 401, 122-147), per-case `fixtures-<cid>` copies and rewritten manifests (lines 449-455), the stderr `TemporaryFile` (line 128). Self-test writes only inside its own `TemporaryDirectory` repo (lines 292-338). `git archive`/`git -C root` calls on `--repo` are read-only; no lane-tree write exists. Observed temp dirs: `/tmp/box-proof-case-deletion-*`.

**Owner `kotoba` — HOLDS.** Matches the counter's pinned `OWNER` (`check_gate_registry.py:65`).

## Proposed fix (script, not the row — text only)

The row is the honest statement of intent; the script should be brought to it. In `main`, wrap the manifest read and scoring setup in the `DriverError` net, and harden `export_tree`:

```python
        try:
            export_tree(root, args.rev, export)
            manifest = read_manifest(export / MANIFEST_REL)
        except DriverError as exc:
            print("ERROR %s" % exc, file=sys.stderr)
            return 2
```

and in `export_tree`, catch `tarfile.TarError` around the open/iteration (lines 133-138) and re-raise `DriverError("git archive %s failed …")` so a dead `<rev>` yields exit 2; optionally wrap `run_box_proof`'s `subprocess.run` (line 188) in `except subprocess.SubprocessError` → per-run `error` or `DriverError`. No row text change is then needed.

If the row must describe current as-is behavior instead, no cell rewrite is honest — `1=failed` is what the crashes produce; the defect is in the script.

## Evidence log

- `git clone` → `checkout 58db81c4` in `/fast/scratch/hyaku/kotoba-r54/W2RowBoxProofCaseDeletion`; `git rev-parse HEAD` = `58db81c4465b0e9b07ef2485b87d8970683afac6`.
- `python3 -B verifiers/box_proof_case_deletion.py --self-test` → exit 0, `self-test: 0 failure(s) over 10 assertions`.
- `python3 -B verifiers/box_proof_case_deletion.py --rev 58db81c4…` → exit 0, last line `killed 6 of 6`, 1.35 s.
- `--self-test --rev abc` → usage error, exit 2; bare invocation → usage error, exit 2; `--rev 009a1dbc… --repo /nonexistent-dir` → `ERROR … is not a git checkout`, exit 2.
- `--rev deadbeef…` → `tarfile.ReadError` traceback, exit 1. `--rev 009a1dbc…` (scratch commit with `not json at all{` manifest) → `DriverError: cannot parse` traceback, exit 1.
- Row text identical at `bf65974c:SKILL.md:441` and tip `SKILL.md:455`; script blob `9328108df63cd242a8a9226ddb0bb17fbc21fed3` at both revs.

No installs performed. No lane files touched except this report.
