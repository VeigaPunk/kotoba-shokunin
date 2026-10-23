Result: DONE — `box_proof_case_deletion.py` now exits 2 with a `could-not-evaluate:` stderr line for both C2 probe classes.

## Change

- Delivered unified diff: `.ufo/waves/round-55/build/FixBoxProof.patch`.
- Sandbox commit: `cf927705c98eb83bd26e5283d5f29852f06744fa` (based on plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`).
- Diff stat: `verifiers/box_proof_case_deletion.py | 39 ++++++++++++++++++++++++++++++++++++`; `1 file changed, 39 insertions(+)`.
- `verifiers/box_proof_case_deletion.py:417-429` verifies `--rev` with `git rev-parse --verify --quiet <rev>^{commit}` before archive/read; a failed check or `OSError` returns 2 and prints `could-not-evaluate:`. Lines 435-443 map an `OSError` from `git archive` to the same exit/message.
- Regression assertions at `verifiers/box_proof_case_deletion.py:373-392` check exit 2 and the stderr marker for an unknown revision and for a PATH containing only a `python3` link. The classification and counting logic is unchanged.

## Probe root causes

- **R (unknown revision):** At the plan commit, `verifiers/box_proof_case_deletion.py:128-147` passed the revision directly to `git archive`, consumed its empty output with `tarfile.open` before checking the archive process result, and `main` only caught `DriverError` around the export (`:401-404`). The uncaught `tarfile.ReadError` produced exit 1. Evidence: running the plan-commit script from the sandbox with `--rev 0000000000000000000000000000000000000000` yielded `tarfile.ReadError: empty file`, exit 1; the frozen base receipt also records R got 1 (`.ufo/waves/round-55/controls/C2-base.txt:4`).
- **G (git absent from PATH):** At the plan commit, `export_tree` started `git` with `subprocess.Popen` at `verifiers/box_proof_case_deletion.py:129-131`, with no `OSError` handling; `main` caught only `DriverError` at `:401-404`. `FileNotFoundError` therefore escaped as exit 1. Evidence: running the plan-commit script with PATH containing only `python3` yielded `FileNotFoundError: ... 'git'`, exit 1; the frozen base receipt records G got 1 (`.ufo/waves/round-55/controls/C2-base.txt:5`).

## Verification evidence

- Gate self-test before: `timeout 900s python3 -B verifiers/box_proof_case_deletion.py --self-test` → `self-test: 0 failure(s) over 10 assertions`, exit 0.
- Gate self-test after, at the final sandbox commit: same command → `self-test: 0 failure(s) over 14 assertions`, exit 0.
- Real verdict before, at plan commit: `timeout 900s python3 -B verifiers/box_proof_case_deletion.py --rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` → summary `killed 6 of 6`, exit 0.
- Real verdict after, at plan commit: same command → summary `killed 6 of 6`, exit 0.
- Real verdict after, at sandbox commit `cf927705c98eb83bd26e5283d5f29852f06744fa` → summary `killed 6 of 6`, exit 0. The before/after real-verdict exit code and summary are unchanged.
- Final frozen C2 command: `timeout 900s python3 -B verifiers/check_could_not_evaluate.py --rev HEAD` (measured `cf927705c98eb83bd26e5283d5f29852f06744fa`) → exit 1 overall. Its lines for this gate were:

  ```text
  box_proof_case_deletion.py         R expect 2   got 2 ok
  box_proof_case_deletion.py         G expect 2   got 2 ok
  box_proof_case_deletion.py         S expect 0   got 0 ok
  box_proof_case_deletion.py         V expect 0|1 got 0 ok
  could-not-evaluate probes honoured 15 of 25; controls held 13 of 13
  ```

  The scoped gate honors both probes and holds both controls. The full frozen counter remains unmet because other gates still miss probes; those are outside this assignment.

No tools were installed or updated. No blockers for this gate.