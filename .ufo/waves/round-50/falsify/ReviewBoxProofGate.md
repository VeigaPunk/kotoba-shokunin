# ReviewBoxProofGate: round-50 D2 gate half (checklist.box_map_complete runs each delegated `--box-proof`)

Verdict: FAILS, applies to verifiers/verify_skill_checklist.py at 956ee1676e4c18480bce8ac3993541462be76e11 (+212/-12). Holds: no false red on the live tree; a failing delegated proof is red and names the instrument and exit code; a proof timeout is red; the self-test reads 1851 assertions with 0 failures. Fails: a delegate the gate cannot probe passes as "no --box-proof support" (the build calls this fail-closed); a relative `--map` from another directory gives a false red; non-UTF-8 `--help` output crashes the gate.

## Findings, by severity

### F1 High: fail-open on delegates the gate cannot probe
- `instrument_command` (line 945) and `supports_box_proof` (line 960) send three cases to "not run", which is PASS: the `--help` probe times out (120 s); the probe cannot exec (OSError); the file has no interpreter mapping and no execute bit.
- Probe I: `--help` sleeps. exit 0, PASS: "no --box-proof support (the --help probe timed out), not run". (Real 120 s timeout, hang-results.txt.)
- Probe F: `#!/nonexistent/interp`, mode 755. exit 0, PASS: "no --box-proof support (the --help probe failed ([Errno 2] No such file or directory ...)), not run".
- Probe E: shebang file, no suffix, mode 644. exit 0, PASS: "not runnable (no interpreter, not executable), not run". Probe L (`probe_x.js`, mode 644) gives the same.
- The same exec failure is red at proof time (OSError branch, line 1013). The gate is open at probe time and closed at proof time.
- Build evidence `.ufo/waves/round-50/build/BoxProofGate.md` line 33 says "A timeout or an unrunnable instrument is also a FAIL (fail-closed)". The code does not do that. Line 118 ("fail-closed on timeout") is true only for the proof run (probe J below).
- Q26: the detail "no --box-proof support" reports a fact the probe never measured.
- Current exposure: none on the live map, which has one delegate target (verify_dispatch_prompts.py) and that target runs.

### F2 Medium: a hidden flag passes
- Probe C: a stub accepts `--box-proof`, exits 1 under it, and hides the flag from `--help` (argparse `help=SUPPRESS`). exit 0, PASS: "no --box-proof support (the --help probe does not advertise --box-proof), not run".
- The probe only checks whether the help text contains the token. Build evidence lines 119-120 name this as a ceiling, but the check is still green, and "does not support" overstates what was measured.

### F3 Medium: relative `--map` gives a false red
- `main` keeps `map_path = Path(args.map)` unresolved (line 2534). `delegated_box_proof` runs the child with `cwd=base`, the map's repo root (line 1008). The child reads the relative path from the wrong directory.
- Probe G: gate run from the scratch dir with `--repo lane --skill lane/SKILL.md --map lane/verifiers/checklist-baseline.json`. exit 1, FAIL: "delegated instrument 'verifiers/verify_dispatch_prompts.py' failed its --box-proof (exit 2): boxes proven 0".
- Same instrument run directly from the lane root with that relative map: exit 2, stderr "box-proof: cannot read the box map lane/verifiers/checklist-baseline.json". Control M (absolute `--map`, same cwd): exit 0, PASS.
- Build evidence lines 45-46 say "main passes the resolved --map". The code does not resolve it.

### F4 Medium: the red detail drops the instrument's reason
- The detail carries only `first_line(proc.stdout)` (line 1018). Stderr is never shown.
- Probe H: scratch copy with manifest case `d04-stem` deleted. exit 1, FAIL: "...failed its --box-proof (exit 1): boxes proven 1". The instrument's stderr names the gap: "box-proof: dispatch.04: no isolated must-fail case for conjunct report_stem_is_lane_id". An operator must rerun the instrument to learn which conjunct is uncovered.
- Probe D (stub, reason on stderr) shows the same loss. Probe G's exit-2 failure reads "boxes proven 0", which also hides the cause.

### F5 Low-Medium: non-UTF-8 output crashes the gate
- Probe K: `--help` writes bytes `\xff\xfe` to stdout. `subprocess.run(..., text=True)` raises UnicodeDecodeError inside `supports_box_proof`. Only TimeoutExpired and OSError are caught. Result: a Python traceback, exit 1, no JSON, no check row.
- The proof run has the same `text=True` exposure (line 1007).

### F6 Low: the new self-test arms cover only the red and green paths
- Base f304646: `--self-test` exit 0, "0 failure(s) over 1845 assertions". 956ee: exit 0, "0 failure(s) over 1851 assertions".
- Unpatched code (base plus the six new arms, gate call removed; scratch splice): exit 1, "4 failure(s) over 1851 assertions". Failing arms: stub exiting 1 turns the check red; failing instrument and exit named; proof run stated in detail; skipped instrument stated in detail. Arms 3 and 5 (green controls) pass on unpatched code by design. Build evidence line 77 reports the same arms (1, 2, 4, 6).
- So "the arms fail on the unpatched code" holds for 4 of 6, not all six.
- No arm covers F1, F2, F3, F4 or F5.

## Verified holds (commands and exit codes)
- `git -C <lane> diff f304646 956ee -- verifiers/verify_skill_checklist.py` exit 0: 212 insertions, 12 deletions.
- sha256 (first 16 hex) of SKILL.md, checklist-baseline.json, verify_skill_checklist.py, verify_dispatch_prompts.py, manifest.json: lane and 956ee clone identical (checked before 13:38 UTC).
- In lane, read-only: `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete --json` exit 0, PASS "41 boxes mapped (8 executed, 2 delegated, 31 unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2". Wall time 0.106 s. Repeated at 13:41:47 UTC: exit 0, same PASS.
- In lane, read-only: `python3 -B verifiers/verify_skill_checklist.py --json` exit 0; pass 11, fail 0, na 0 (13:37:49 UTC).
- Clone 956ee `--json`: exit 1 with trigger.name_directory, trigger.citation_resolves, governance.citation_resolves. Base clone f304646: exit 1 with the same three IDs. These come from my clone layout (directory named `lane`/`base`; `../` citations resolve outside the clone), not from the round-50 change.
- `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` exit 0, "boxes proven 2". `--help` exit 0 and lists `--box-proof`.
- `python3 -B verifiers/check_assertion_floors.py` in the 956ee clone: exit 0, "PASS checklist observed=1851 floor=1851". floors-registry.json pins 1851.
- Probe B (red stub): exit 1, FAIL "delegated instrument 'verifiers/probe_red.py' failed its --box-proof (exit 1): boxes proven 0".
- Probe A (green stub): exit 0, PASS.
- Probe J (proof run sleeps, real 120 s): exit 1, FAIL "delegated instrument 'verifiers/probe_hangproof.py' timed out after 120s running --box-proof". Fail-closed, as claimed.

## Residual risk and gaps
- `--json` is no longer side-effect-free by construction: each run executes each delegate with `--help` and `--box-proof`. For the one live delegate, the only write calls are in self-test helpers (`_write_case`, lines 588-605, and `_proof_fixture_corpus`, lines 625-678; both called only from `self_test`, lines 679-984); `box_proof` (lines 985-1149) has none. Other delegates are unchecked.
- Subprocesses inherit the gate's stdin (no `stdin=subprocess.DEVNULL`). Read from the code, not tested.
- Worst case is 240 s per delegate (probe plus proof).
- Lane state: lane SKILL.md changed at 13:41:36 UTC (sha256 05457302, against 9fe2ca74 at 956ee). This seat did not write it; the writer is unknown. The verdict is on 956ee; the working copy still passes the box-map check.
- Not covered by this seat: C1 census, C2 deletion counts, D1-D6 except the D2 gate half, S024-S029, Q26 wording.

## Writes and tools
- Apart from this report, this seat wrote no lane file. In-lane runs used `python3 -B`. Lane files modified after 13:34:05 UTC were written by other processes. `verifiers/__pycache__/verify_skill_checklist.cpython-314.pyc` (mtime 12:33:36 UTC) predates this seat.
- No tool installed or updated. Present: python3 3.14.8, bash, strace, timeout.
- Scratch evidence: probe_driver.py (fast and hang modes), probe_more.py, splice_unpatched.py, *.txt and *.json logs, clones lane (956ee), base (f304646), red, unpatched, stubs/.

## Fix list for the author (not applied)
1. Fail closed: probe timeout, probe OSError and not-runnable become FAIL naming the instrument. Use "not run" only for a clean `--help` that lacks the flag.
2. `map_path = Path(args.map).resolve()` in `main`.
3. Put the instrument's stderr reason line into the FAIL detail.
4. Decode with `errors="replace"` and treat decode errors as FAIL.
5. Add self-test arms for timeout, unrunnable delegate, relative `--map`, stderr reason and non-UTF-8 output.
