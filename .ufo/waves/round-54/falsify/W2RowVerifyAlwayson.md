Result: HOLDS — every cell of the `verifiers/verify_alwayson.py` registry row at bf65974c7845a06d7ef621ad998c6378ff735cd5 matches the script's real behavior; no cell breaks.

Scope: SKILL.md § Gate registry row at line 457 (`git show bf65974c:SKILL.md`):
`| verifiers/verify_alwayson.py | gate | python3 -B verifiers/verify_alwayson.py --check <box> --target <dir> | 0=clean, 1=failed, 2=could-not-evaluate | --self-test | in-file | none | kotoba |`
Attacked in a sandbox clone at bf65974c (`/fast/scratch/hyaku/kotoba-r54/W2RowVerifyAlwayson`, clean `git status` after all runs). Script unchanged between bf65974c and tip 58db81c (`git diff` empty; last touched round 53, commit 55973a2); row byte-identical at tip (SKILL.md:471 there).

## Per-cell findings

**Name — `verifiers/verify_alwayson.py`: HOLDS.**
Blob exists at the revision and is in the counter's universe. The C2 counter itself prints `verifiers/verify_alwayson.py  OK` and `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0, run at bf65974c in the sandbox.

**Kind — `gate`: HOLDS.**
PROTOCOL.md § Gate standard (line 390-392): a gate reads surfaces, compares against expected values persisted in the repo, returns a verdict; "a tool that cannot fail is a probe". This script can and does fail: `--check alwayson.04 --target verifiers/fixtures/alwayson/a04-iso-date` printed `FAIL ... dated/transient text found: AGENTS.md:5 ISO date/timestamp '2026-11-01'`, exit 1 (check_dated_text, lines 284-296; dispatch at 389-394). It is the delegated verifier for checklist boxes alwayson.04/.07 (SECTION/DELEGATION_TARGET, lines 57-59; confirmed by `--box-proof` printing `boxes proven 2`, exit 0).

**Entry command — `python3 -B verifiers/verify_alwayson.py --check <box> --target <dir>`: HOLDS.**
Both flags are required (parser.error line 652-653): `--check alwayson.04` alone → `error: --check and --target are required`, exit 2. `<box>` is a real metavar over choices `alwayson.04|alwayson.07` (line 624); invalid choice → exit 2. Ran clean on a fixture: `PASS alwayson.04: ... a04-plain-rules: no recognized date or transient cue in 1 selected files`, exit 0. Optional `--json` (line 632) only changes output format; omitting it from the entry cell is consistent with sibling rows.

**Verdict map — `0=clean, 1=failed, 2=could-not-evaluate`: HOLDS.**
Every declared code is produced with the declared meaning; no produced code is missing.
- 0: PASS → `code = 0` (line 656), observed exit 0.
- 1: FAIL → `else 1` (line 656), observed exit 1.
- 2: InputError → `code = 2` (lines 657-659), observed twice: missing target `ERROR alwayson.04: cannot read target directory /nonexistent-dir-xyz`, exit 2; escaping-symlink fixture `ERROR alwayson.04: symlink for AGENTS.md escapes target directory`, exit 2. Usage errors → `parser.error` → argparse exit 2 (observed). Docstring contract (lines 6-7) matches: "Exit 0 means PASS, 1 means FAIL, and 2 means usage or unreadable input."
- `main()` returns only 0/1/2 across all three modes (self_test line 555: 0/1; box_proof lines 565, 583, 614: 0/1/2; check line 664: 0/1/2). `-h` exits 0 (clean help, argparse standard). Gate pair `0=clean`/`1=failed` present as required by counter rule (check_gate_registry.py:154).

**Self-test — `--self-test`: HOLDS.**
Literal flag at lines 620-621; `--self-test` dispatches to `self_test()` (line 640-643) → `_fixture_suite(FIXTURES_DIR)` (line 551) over the committed `verifiers/fixtures/alwayson/` corpus (line 62) — the script's own self-test, not a nested call to another verifier's mode and not usage text. Ran: `0 failure(s) over 89 assertions`, exit 0. The in-process `main(argv)` invocations inside the suite (lines 512-528) are the script's own CLI under contract check (exit code + payload `exit_code` + status, line 520-522) — that satisfies the Gate-standard self-test clause (asserts exit code and expected finding status; expected values committed in-file as CASE_EXPECTATIONS, lines 409-438). Extra-arg guard verified: `--self-test --target .` → `error: --self-test does not accept --check, --target, --map, or --fixtures`, exit 2.

**Pinned values — `in-file`: HOLDS.**
Every expected value the script compares against lives in-file: `PINNED_BOX_SHA` per-box sha256 pins (lines 67-70), `CASE_EXPECTATIONS` (id, box, expected status, pinned fixture dir — lines 409-438), `SECTION`/`DELEGATION_TARGET` (58-59), `CANDIDATE_PATHS` (73-79), `MAX_FILE_BYTES` (64). The files it does read are inputs verified against those pins, not trusted expectations: the fixture manifest's ids and dirs are checked to equal CASE_EXPECTATIONS (lines 478-495) and `checklist-baseline.json` box-map `text_sha256` must equal PINNED_BOX_SHA (lines 594-597). Cell is consistent with the table's own convention: `verify_dispatch_prompts.py` names `fixtures/dispatch-prompts/manifest.json` because that manifest carries `expect_verdict`/`expect_conjunct` per case; the alwayson manifest carries only id→dir pairs, all pinned in-file.

**Write scope — `none`: HOLDS.**
No write syscalls in the source (no `open(...,"w")`, `write_text`, `tempfile`, `mkdir`, `os.remove` — full read of lines 1-668). Empirical: after running `--self-test`, four `--check` modes, and `--box-proof` in the sandbox, `git status --porcelain` prints 0 lines. Self-test reads committed fixtures rather than building temp trees, so `none` is accurate where sibling rows say "under `$TMPDIR`". Residual note, not a break: `--box-proof` does `import verify_skill_checklist` (line 577); invoked without `-B` a bytecode cache could be written under `verifiers/__pycache__/`, but the declared entry command carries `-B` and no cache appeared in any run.

**Owner — `kotoba`: HOLDS.**
Lane-owned script (created in this lane at round-53 commit 55973a2); `kotoba` is the counter-pinned owner (check_gate_registry.py:65,180).

## Residual risks / verification gaps (not defects in the row)

1. Unhandled-exception path: an unexpected crash exits 1 via the interpreter, which the row maps to `failed` rather than `could-not-evaluate`. All declared codes are produced, so the row stays honest; this is shared by every Python gate in the table and is a standard-level, not row-level, question.
2. `self_test()` mutates the module global `MAX_FILE_BYTES` (lines 533-545, restored in `finally`) — in-process only, no write-scope impact.
3. `--box-proof` (lines 622-623) is a second mode not in the entry-command cell; its verdict codes (0/1/2, lines 565/583/614) are already covered by the declared map, and sibling rows likewise declare one entry command. No defect.
4. The erratum-2 guard list (four gates lacking `--self-test` at 7ad05d34) does not name this script; its pre-existing `--self-test` exits 0 as shown above.

No corrected row text proposed: all eight cells hold.

Commands run (all in sandbox clone at bf65974c, exit codes observed):
- `python3 -B verifiers/verify_alwayson.py --self-test` → `0 failure(s) over 89 assertions`, exit 0
- `python3 -B verifiers/verify_alwayson.py --check alwayson.04 --target verifiers/fixtures/alwayson/a04-plain-rules` → `PASS ...`, exit 0
- `... --target verifiers/fixtures/alwayson/a04-iso-date` → `FAIL ... ISO date/timestamp '2026-11-01'`, exit 1
- `... --target /nonexistent-dir-xyz` → `ERROR ... cannot read target directory`, exit 2
- `... --target verifiers/fixtures/alwayson/a04-outside-link/target` → `ERROR ... symlink escapes`, exit 2
- `python3 -B verifiers/verify_alwayson.py --box-proof` → `boxes proven 2`, exit 0
- `python3 -B verifiers/check_gate_registry.py --rev bf65974c...` → `gate registry rows conformant 24 of 24 lane verifiers; phantom 0`, exit 0; row judged `OK`
- `git status --porcelain` after all runs → 0 lines
- `git diff bf65974c 58db81c -- verifiers/verify_alwayson.py` → empty (no drift)

No installs needed (system python3, git). No network use. No lane files modified; only this report.
