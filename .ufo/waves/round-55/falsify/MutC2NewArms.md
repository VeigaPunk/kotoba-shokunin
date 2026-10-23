Result: MIXED — Six of eight one-line mutants were killed; the archive and git_show OSError-path mutants survived their gates’ self-tests, with exact bytes restored for all eight.

# MutC2NewArms — round-55 operability mutation probe

## Scope and method

- Target patch: `e966cd59748e4ca0ad7209ee2ac41eb22d64edac`, exactly its eight changed gates. Read `plans/round-55.md` first; C2’s frozen predicate and controls are at :43-62, and the counter’s rules are at `verifiers/check_could_not_evaluate.py:24-43`.
- Sandbox: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`, checked out at `f0e6b695b746775823b65a8c45de7d50ea33e84f`. The lane was read-only except this report. No counters, judging lines, self-test assertions, or lane source files were edited.
- Each mutant changed one behavior-bearing line in the sandbox. All eight pristine self-tests ran first. Then, for each gate separately: mutate one line, run its detector, invert the edit, and run the identical detector on restored bytes before proceeding. Thus no detector ran against a second gate’s mutant.
- Every detector was capped at 600 seconds with TERM and a five-second kill-after bound. `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` were removed from the environment; `PYTHONDONTWRITEBYTECODE=1`; `TMPDIR` was the sandbox’s `probe-tmp/`. No run timed out; all command subprocesses returned.
- Expected detector: the gate’s unchanged `--self-test` must exit 0 on pristine/restored bytes and nonzero on a covered defect. All baselines exited 0, so none of the mutant results is a baseline-failure false kill.
- The C2 aggregate counter was not run in this scoped probe. A survivor is a self-test coverage finding, not a verdict on C2’s frozen R/G predicate. No installation, source fetch, model call, or subagent dispatch was needed.

Sandbox setup commands (both exit 0, no output):

```sh
timeout 120 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/MutC2NewArms
timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r55/MutC2NewArms checkout -q f0e6b695b746775823b65a8c45de7d50ea33e84f
```

## Results

Source pointers in the table refer to pristine/restored bytes at the measured revision; all paths are under `verifiers/`.

| Gate and changed line | Mutant | Expected detector arm | Exit pristine / mutant / restored | Actual mutant output (summary; full output below) | Verdict |
| --- | --- | --- | --- | --- | --- |
| `box_proof_case_deletion.py:440` | git archive OSError handler returns 1 instead of 2 | new G assertions at :390-392; no archive-OSError-specific assertion | 0 / 0 / 0 | self-test: 0 failure(s) over 14 assertions | **SURVIVED** |
| `check_assertion_floors.py:468` | git preflight OSError handler returns 1 instead of 2 | F30 missing git at :1217-1219 | 0 / 1 / 0 | F30 missing git: exit 2: got 1 | **KILLED** |
| `check_correction_sweep.py:241` | remove OSError from the new could-not-evaluate catch | git unavailable check at :218-220 | 0 / 1 / 0 | 1 failure(s) over 13 assertions; git unavailable: exit 1 (FileNotFoundError) | **KILLED** |
| `check_description_thresholds.py:439` | drop the new revision-verification call | unknown revision assertion at :404-406 | 0 / 1 / 0 | unknown revision: got (1, False), expected (2, True) | **KILLED** |
| `check_gate_finding_delta.py:222` | new environment/revision catch returns 1 instead of 2 | unknown-base/head at :174-183 and git unavailable at :194-196 | 0 / 1 / 0 | 3 failure(s): unknown-base, unknown-head, git-unavailable each got (1, True) | **KILLED** |
| `check_mcp_instructions.py:314` | remove OSError from the new could-not-evaluate catch | G git unavailable at :281-283 | 0 / 1 / 0 | 2 failure(s): G exit-code and diagnostic assertions | **KILLED** |
| `check_overlap_levers.py:550` | git_show OSError uses RuntimeError instead of the caught EnvError | new G assertion at :1241-1244; no git_show-OSError-specific assertion | 0 / 0 / 0 | 0 failures; 53 assertions | **SURVIVED** |
| `verify_corpus_independent.py:71` | _git OSError uses RuntimeError instead of the caught EnvError | CLI unavailable-git assertions at :999-1001 | 0 / 1 / 0 | not ok 94: got 1 want 2; not ok 95: got False want True | **KILLED** |

## Survivors

1. **`box_proof_case_deletion.py:440`: archive OSError mapped to exit 1.** The new G self-test at :378-392 removes git before calling `main`. The revision subprocess at :417-425 precedes `export_tree` at :436 and its separate new OSError handler at :437-440. The mutant still printed `self-test: 0 failure(s) over 14 assertions`, exit 0. [INFERENCE] The G arm takes the earlier revision-check OSError handler and cannot distinguish the archive handler’s return code. This finding concerns an archive-launch OSError after a successful preflight, not a failure of the frozen “git absent from the outset” probe.

2. **`check_overlap_levers.py:550`: git_show OSError raised as RuntimeError.** `main` calls `verify_rev` at :599-600 before its `git_show` readers; `verify_rev` has its own OSError-to-EnvError conversion at :537-538. The new G arm removes git before entering `main` (:1228-1244). Changing only `git_show`’s separate new conversion at :549-550 left `0 failures` / `53 assertions`, exit 0. [INFERENCE] The G arm terminates at the earlier preflight and does not distinguish this later reader conversion; a git_show launch OSError after preflight would escape the `EnvError`/`OSError` catches at :605-610 as RuntimeError. That later-error behavior was not separately executed here.

These two results do not authorize changing the frozen contract or counter. No repair was made. The other six mutants were killed by the named new arms, as shown in the recorded output.

## Restoration evidence

Hashes were measured immediately before and after each detector with `timeout 10s sha256sum verifiers/<gate>` (all hash commands exited 0). Each detector left its input hash unchanged. The full pristine and restored hashes match in every row; only the one-line mutant has a different hash. No git reset, checkout, or other restoration operation was used after setup: each mutation was inverted surgically.

| Gate | Pristine SHA-256 | Mutant SHA-256 | Restored SHA-256 |
| --- | --- | --- | --- |
| `box_proof_case_deletion.py` | `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0` | `c423e527db824f6f750b2df541723bdb3e3b8e13cb42b86fde5092079d7a793a` | `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0` |
| `check_assertion_floors.py` | `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef` | `6c3799cde38ce1eae1416fda3e7842c8f48d03d3680def0687caeade875304e6` | `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef` |
| `check_correction_sweep.py` | `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1` | `a8518cf9996e36ae6a5f7b09b2ae3eea546b574275bc2119304d48048e82e993` | `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1` |
| `check_description_thresholds.py` | `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5` | `b51ab5a46a49b6b3f00c4d1e319b61ed46c181aef5e15cbd33f1e624e162961d` | `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5` |
| `check_gate_finding_delta.py` | `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48` | `d2c64838e7581f6374d5d65005d1c62cfc03274fbbf12a5d629c0b6aac039934` | `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48` |
| `check_mcp_instructions.py` | `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b` | `0e365d080283701d5965c91601b63f353a83654537cc639344b3f83ba4261997` | `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b` |
| `check_overlap_levers.py` | `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd` | `076545a29e2b904988dcee09e023132d77fe325d18b2f4797e8ccec876c67b44` | `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd` |
| `verify_corpus_independent.py` | `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8` | `2bf3cbdde1f0cb1575bd6e8190af00781a2dd20d7af6317019162e8be02938b7` | `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8` |

## Exact mutations and behavioral receipts

All stdout below is verbatim, without Markdown stripping. Every detector’s stderr was empty; child error diagnostics captured by a self-test appear in its stdout exactly as that self-test printed them. UTC lines below are the observed output of `timeout 10s date -u` (exit 0), not typed timestamps.

### box_proof_case_deletion.py

Changed only `verifiers/box_proof_case_deletion.py:440`:

Before:
```python
            return 2
```
After:
```python
            return 1
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/box_proof_case_deletion.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0` / `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0`.

stdout:
```text
self-test: 0 failure(s) over 14 assertions
```

stderr: empty.

#### mutated — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/box_proof_case_deletion.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:50 AM UTC 2026
```

SHA-256 before / after detector: `c423e527db824f6f750b2df541723bdb3e3b8e13cb42b86fde5092079d7a793a` / `c423e527db824f6f750b2df541723bdb3e3b8e13cb42b86fde5092079d7a793a`.

stdout:
```text
self-test: 0 failure(s) over 14 assertions
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/box_proof_case_deletion.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:11:11 AM UTC 2026
```

SHA-256 before / after detector: `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0` / `fce3133a857c48d904e9a0e446588e090bda57ee0bb4ad35d1197611a04a83b0`.

stdout:
```text
self-test: 0 failure(s) over 14 assertions
```

stderr: empty.

### check_assertion_floors.py

Changed only `verifiers/check_assertion_floors.py:468`:

Before:
```python
        return 2
```
After:
```python
        return 1
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_assertion_floors.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef` / `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef`.

stdout:
```text
0 failure(s) over 152 assertions
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_assertion_floors.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:11:30 AM UTC 2026
```

SHA-256 before / after detector: `6c3799cde38ce1eae1416fda3e7842c8f48d03d3680def0687caeade875304e6` / `6c3799cde38ce1eae1416fda3e7842c8f48d03d3680def0687caeade875304e6`.

stdout:
```text
1 failure(s) over 152 assertions
FAIL: F30 missing git: exit 2: got 1
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_assertion_floors.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:11:49 AM UTC 2026
```

SHA-256 before / after detector: `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef` / `7553f789960f2e24b6220801835ba63b66be48f2b6f3afebc558c3bc5414d3ef`.

stdout:
```text
0 failure(s) over 152 assertions
```

stderr: empty.

### check_correction_sweep.py

Changed only `verifiers/check_correction_sweep.py:241`:

Before:
```python
    except (OSError, RuntimeError) as e:
```
After:
```python
    except RuntimeError as e:
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_correction_sweep.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1` / `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1`.

stdout:
```text
0 failure(s) over 13 assertions
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_correction_sweep.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:12:08 AM UTC 2026
```

SHA-256 before / after detector: `a8518cf9996e36ae6a5f7b09b2ae3eea546b574275bc2119304d48048e82e993` / `a8518cf9996e36ae6a5f7b09b2ae3eea546b574275bc2119304d48048e82e993`.

stdout:
```text
1 failure(s) over 13 assertions
FAIL git unavailable: exit 1, stderr 'Traceback (most recent call last):\n  File "/fast/scratch/hyaku/kotoba-r55/MutC2NewArms/verifiers/check_correction_sweep.py", line 251, in <module>\n    sys.exit(main())\n             ~~~~^^\n  File "/fast/scratch/hyaku/kotoba-r55/MutC2NewArms/verifiers/check_correction_sweep.py", line 239, in main\n    verify_revision(a.rev)\n    ~~~~~~~~~~~~~~~^^^^^^^\n  File "/fast/scratch/hyaku/kotoba-r55/MutC2NewArms/verifiers/check_correction_sweep.py", line 138, in verify_revision\n    r = subprocess.run(["git", "-C", str(LANE), "rev-parse", "--verify", "--quiet",\n                        "%s^{commit}" % rev], capture_output=True)\n  File "/usr/lib/python3.14/subprocess.py", line 555, in run\n    with Popen(*popenargs, **kwargs) as process:\n         ~~~~~^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/lib/python3.14/subprocess.py", line 1039, in __init__\n    self._execute_child(args, executable, preexec_fn, close_fds,\n    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n                        pass_fds, cwd, env,\n                        ^^^^^^^^^^^^^^^^^^^\n    ...<5 lines>...\n                        gid, gids, uid, umask,\n                        ^^^^^^^^^^^^^^^^^^^^^^\n                        start_new_session, process_group)\n                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/lib/python3.14/subprocess.py", line 1990, in _execute_child\n    raise child_exception_type(errno_num, err_msg, err_filename)\nFileNotFoundError: [Errno 2] No such file or directory: \'git\'\n'
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_correction_sweep.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:12:23 AM UTC 2026
```

SHA-256 before / after detector: `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1` / `c22c986232c9c6ef14259f7b8fb49f2810bffdf59e4772e539c4fbb52b32f3b1`.

stdout:
```text
0 failure(s) over 13 assertions
```

stderr: empty.

### check_description_thresholds.py

Changed only `verifiers/check_description_thresholds.py:439`:

Before:
```python
            verify_rev(args.rev)
```
After:
```python
            pass
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_description_thresholds.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5` / `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5`.

stdout:
```text
self-test: 0 failure(s) over 24 assertions
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_description_thresholds.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:12:39 AM UTC 2026
```

SHA-256 before / after detector: `b51ab5a46a49b6b3f00c4d1e319b61ed46c181aef5e15cbd33f1e624e162961d` / `b51ab5a46a49b6b3f00c4d1e319b61ed46c181aef5e15cbd33f1e624e162961d`.

stdout:
```text
FAIL unknown revision exits 2 with could-not-evaluate: got (1, False), expected (2, True)
self-test: 1 failure(s) over 24 assertions
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_description_thresholds.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:12:58 AM UTC 2026
```

SHA-256 before / after detector: `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5` / `328ccc254fdb311e693056015b6bb438f52ba6da1b3e025ccb03ccc13d9da2a5`.

stdout:
```text
self-test: 0 failure(s) over 24 assertions
```

stderr: empty.

### check_gate_finding_delta.py

Changed only `verifiers/check_gate_finding_delta.py:222`:

Before:
```python
        return 2
```
After:
```python
        return 1
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_gate_finding_delta.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48` / `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48`.

stdout:
```text
self-test: 0 failure(s) over 12 assertions
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_gate_finding_delta.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:13:19 AM UTC 2026
```

SHA-256 before / after detector: `d2c64838e7581f6374d5d65005d1c62cfc03274fbbf12a5d629c0b6aac039934` / `d2c64838e7581f6374d5d65005d1c62cfc03274fbbf12a5d629c0b6aac039934`.

stdout:
```text
self-test: 3 failure(s) over 12 assertions
FAIL arm/unknown-base-revision: got (1, True), want (2, True)
FAIL arm/unknown-head-revision: got (1, True), want (2, True)
FAIL arm/git-unavailable: got (1, True), want (2, True)
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_gate_finding_delta.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:13:34 AM UTC 2026
```

SHA-256 before / after detector: `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48` / `c2d5d80b599db71ddfbcd18b184f27e5505df812b36cd5b92f034dcc0d958b48`.

stdout:
```text
self-test: 0 failure(s) over 12 assertions
```

stderr: empty.

### check_mcp_instructions.py

Changed only `verifiers/check_mcp_instructions.py:314`:

Before:
```python
    except (RuntimeError, OSError) as e:
```
After:
```python
    except RuntimeError as e:
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_mcp_instructions.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b` / `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b`.

stdout:
```text
self-test: 0 failure(s) over 14 assertions
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_mcp_instructions.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:13:52 AM UTC 2026
```

SHA-256 before / after detector: `0e365d080283701d5965c91601b63f353a83654537cc639344b3f83ba4261997` / `0e365d080283701d5965c91601b63f353a83654537cc639344b3f83ba4261997`.

stdout:
```text
FAIL G git unavailable exits 2: got False, expected True
FAIL G git unavailable reports could-not-evaluate: got False, expected True
self-test: 2 failure(s) over 14 assertions
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_mcp_instructions.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:14:08 AM UTC 2026
```

SHA-256 before / after detector: `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b` / `85cf4075f40be2cdf0eed7d0b82e12c0d46036b2090ddaabb6dd4f7c7b34719b`.

stdout:
```text
self-test: 0 failure(s) over 14 assertions
```

stderr: empty.

### check_overlap_levers.py

Changed only `verifiers/check_overlap_levers.py:550`:

Before:
```python
        raise EnvError("git not runnable: %s" % exc) from exc
```
After:
```python
        raise RuntimeError("git not runnable: %s" % exc) from exc
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_overlap_levers.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd` / `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd`.

stdout:
```text
0 failures
53 assertions
```

stderr: empty.

#### mutated — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_overlap_levers.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:14:32 AM UTC 2026
```

SHA-256 before / after detector: `076545a29e2b904988dcee09e023132d77fe325d18b2f4797e8ccec876c67b44` / `076545a29e2b904988dcee09e023132d77fe325d18b2f4797e8ccec876c67b44`.

stdout:
```text
0 failures
53 assertions
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/check_overlap_levers.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:14:47 AM UTC 2026
```

SHA-256 before / after detector: `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd` / `660a6d3f6be49b7d67bdc91166489cac33e6963a3e355b1d0b2ca58a2dc3e7dd`.

stdout:
```text
0 failures
53 assertions
```

stderr: empty.

### verify_corpus_independent.py

Changed only `verifiers/verify_corpus_independent.py:71`:

Before:
```python
        raise EnvError("git not runnable: %s" % exc) from exc
```
After:
```python
        raise RuntimeError("git not runnable: %s" % exc) from exc
```

#### pristine — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/verify_corpus_independent.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:10:02 AM UTC 2026
```

SHA-256 before / after detector: `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8` / `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8`.

stdout:
```text
ok 1 - index: only orphan.md unindexed
ok 2 - index: unindexed detail names orphan.md
ok 3 - index: ghost.md + nomatch/*.md stale
ok 4 - index: stale detail (glob token counts as stale pattern)
ok 5 - index: ghost + 3 rooted tokens (external, rooted dead, rooted dead dir)
ok 6 - index: missing detail (brace expansions path-checked; rooted tokens checked)
ok 7 - index: eight tokens in the coverage map
ok 8 - index: one token outside the coverage map section, not counted
ok 9 - index: brace expansion
ok 10 - index: nested brace expansion
ok 11 - index: token without braces is its own expansion
ok 12 - index: ../ token is not corpus-internal
ok 13 - index: rooted token is not corpus-internal
ok 14 - fence: only the live row's token is harvested
ok 15 - fence: the fenced row's file stays unindexed
ok 16 - fence: unindexed detail names the fenced row's file
ok 17 - fence control: without the fence both rows count
ok 18 - fence control: both files are covered
ok 19 - fence pseudo-closer: only the live row's token is harvested
ok 20 - fence pseudo-closer: the quoted row's file stays unindexed
ok 21 - fence: a mismatched fence char does not close
ok 22 - fence: an unclosed tilde fence runs to EOF
ok 23 - fence: a mixed backtick pseudo-closer does not close tilde
ok 24 - fence: blockquote container is outside the line scanner
ok 25 - blockquote fence: only the live row is harvested
ok 26 - blockquote fence: quoted row file remains unindexed
ok 27 - blockquote fence: fail-safe impact names the unindexed file
ok 28 - fence: a shorter closer is content, not a closer
ok 29 - fence: a closer with an info string is content
ok 30 - fence: a closer with trailing text is content
ok 31 - fence: a longer closer closes
ok 32 - fence: a same-length closer closes
ok 33 - fence: an empty-info closer with trailing blanks closes
ok 34 - fence: a legal info opener still needs a >= opener-length closer
ok 35 - fence indent: a 0-space closer closes
ok 36 - fence indent: a 2-space closer closes
ok 37 - fence indent: a 3-space closer closes
ok 38 - fence indent: a 4-space closer is content
ok 39 - fence indent: a tab closer is content
ok 40 - fence indent: a mixed space+tab closer is content
ok 41 - fence indent: a 4-space opener is content
ok 42 - fence indent: a tab opener is content
ok 43 - fence indent: a 4-space tilde closer is content
ok 44 - fence indent: a tab tilde closer is content
ok 45 - fence indent 4space: only the live row's token is harvested
ok 46 - fence indent 4space: the quoted row's file stays unindexed
ok 47 - fence indent 4space: unindexed detail names the quoted file
ok 48 - fence indent tab: only the live row's token is harvested
ok 49 - fence indent tab: the quoted row's file stays unindexed
ok 50 - fence indent tab: unindexed detail names the quoted file
ok 51 - fence indent control: a 3-space closer closes, both rows count
ok 52 - fence indent control: a 3-space closer covers the second file
ok 53 - pointers: seven checked promises
ok 54 - pointers: all four shapes counted
ok 55 - pointers: four excluded tokens
ok 56 - pointers: every exclusion reason fires
ok 57 - pointers: one quoted token is context
ok 58 - pointers: dead relative, dead bare and dead prose token
ok 59 - pointers: dead detail
ok 60 - pointers: candidate population
ok 61 - pointers: shape absolute
ok 62 - pointers: shape tilde
ok 63 - pointers: shape relative
ok 64 - pointers: shape bare
ok 65 - pointers: rooted token resolves as-is
ok 66 - pointers: tilde resolves against HOME
ok 67 - pointers: relative hops resolve from the citing directory
ok 68 - pointers: bare token joins the citing directory
ok 69 - pointers: dotdot after leading hops detected
ok 70 - pointers: pure leading hops are not dotdot-after-hops
ok 71 - pointers: fleet-root report remains checked
ok 72 - pointers: existing fleet-root report resolves
ok 73 - commits: five citations in scope
ok 74 - commits: 6-hex, 41-hex and word are nonhash
ok 75 - commits: deadbeef unresolvable, the real sha resolvable
ok 76 - commits: exactly one hex citation resolves
ok 77 - commits: quoted citation is context
ok 78 - commits: candidate population
ok 79 - commits: two hex-shaped citations
ok 80 - commits: nonhash detail sorted
ok 81 - commits: unresolvable detail
ok 82 - commits: 7 hex accepted
ok 83 - commits: uppercase hex accepted
ok 84 - commits: 6 hex rejected by length
ok 85 - clean: no violations
ok 86 - clean: exit 0
ok 87 - clean: six violation classes all PASS
ok 88 - env: non-git directory rejected
ok 89 - env: missing corpus/ rejected
ok 90 - cli: clean fixture exits 0
ok 91 - cli: json names the repo
ok 92 - cli: drifting fixture exits 1
ok 93 - cli: drifting fixture reports unindexed=1
ok 94 - cli: unavailable git exits 2
ok 95 - cli: unavailable git reports could-not-evaluate
self-test: 95 assertions, 0 failures
```

stderr: empty.

#### mutated — exit 1

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/verify_corpus_independent.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:15:07 AM UTC 2026
```

SHA-256 before / after detector: `2bf3cbdde1f0cb1575bd6e8190af00781a2dd20d7af6317019162e8be02938b7` / `2bf3cbdde1f0cb1575bd6e8190af00781a2dd20d7af6317019162e8be02938b7`.

stdout:
```text
ok 1 - index: only orphan.md unindexed
ok 2 - index: unindexed detail names orphan.md
ok 3 - index: ghost.md + nomatch/*.md stale
ok 4 - index: stale detail (glob token counts as stale pattern)
ok 5 - index: ghost + 3 rooted tokens (external, rooted dead, rooted dead dir)
ok 6 - index: missing detail (brace expansions path-checked; rooted tokens checked)
ok 7 - index: eight tokens in the coverage map
ok 8 - index: one token outside the coverage map section, not counted
ok 9 - index: brace expansion
ok 10 - index: nested brace expansion
ok 11 - index: token without braces is its own expansion
ok 12 - index: ../ token is not corpus-internal
ok 13 - index: rooted token is not corpus-internal
ok 14 - fence: only the live row's token is harvested
ok 15 - fence: the fenced row's file stays unindexed
ok 16 - fence: unindexed detail names the fenced row's file
ok 17 - fence control: without the fence both rows count
ok 18 - fence control: both files are covered
ok 19 - fence pseudo-closer: only the live row's token is harvested
ok 20 - fence pseudo-closer: the quoted row's file stays unindexed
ok 21 - fence: a mismatched fence char does not close
ok 22 - fence: an unclosed tilde fence runs to EOF
ok 23 - fence: a mixed backtick pseudo-closer does not close tilde
ok 24 - fence: blockquote container is outside the line scanner
ok 25 - blockquote fence: only the live row is harvested
ok 26 - blockquote fence: quoted row file remains unindexed
ok 27 - blockquote fence: fail-safe impact names the unindexed file
ok 28 - fence: a shorter closer is content, not a closer
ok 29 - fence: a closer with an info string is content
ok 30 - fence: a closer with trailing text is content
ok 31 - fence: a longer closer closes
ok 32 - fence: a same-length closer closes
ok 33 - fence: an empty-info closer with trailing blanks closes
ok 34 - fence: a legal info opener still needs a >= opener-length closer
ok 35 - fence indent: a 0-space closer closes
ok 36 - fence indent: a 2-space closer closes
ok 37 - fence indent: a 3-space closer closes
ok 38 - fence indent: a 4-space closer is content
ok 39 - fence indent: a tab closer is content
ok 40 - fence indent: a mixed space+tab closer is content
ok 41 - fence indent: a 4-space opener is content
ok 42 - fence indent: a tab opener is content
ok 43 - fence indent: a 4-space tilde closer is content
ok 44 - fence indent: a tab tilde closer is content
ok 45 - fence indent 4space: only the live row's token is harvested
ok 46 - fence indent 4space: the quoted row's file stays unindexed
ok 47 - fence indent 4space: unindexed detail names the quoted file
ok 48 - fence indent tab: only the live row's token is harvested
ok 49 - fence indent tab: the quoted row's file stays unindexed
ok 50 - fence indent tab: unindexed detail names the quoted file
ok 51 - fence indent control: a 3-space closer closes, both rows count
ok 52 - fence indent control: a 3-space closer covers the second file
ok 53 - pointers: seven checked promises
ok 54 - pointers: all four shapes counted
ok 55 - pointers: four excluded tokens
ok 56 - pointers: every exclusion reason fires
ok 57 - pointers: one quoted token is context
ok 58 - pointers: dead relative, dead bare and dead prose token
ok 59 - pointers: dead detail
ok 60 - pointers: candidate population
ok 61 - pointers: shape absolute
ok 62 - pointers: shape tilde
ok 63 - pointers: shape relative
ok 64 - pointers: shape bare
ok 65 - pointers: rooted token resolves as-is
ok 66 - pointers: tilde resolves against HOME
ok 67 - pointers: relative hops resolve from the citing directory
ok 68 - pointers: bare token joins the citing directory
ok 69 - pointers: dotdot after leading hops detected
ok 70 - pointers: pure leading hops are not dotdot-after-hops
ok 71 - pointers: fleet-root report remains checked
ok 72 - pointers: existing fleet-root report resolves
ok 73 - commits: five citations in scope
ok 74 - commits: 6-hex, 41-hex and word are nonhash
ok 75 - commits: deadbeef unresolvable, the real sha resolvable
ok 76 - commits: exactly one hex citation resolves
ok 77 - commits: quoted citation is context
ok 78 - commits: candidate population
ok 79 - commits: two hex-shaped citations
ok 80 - commits: nonhash detail sorted
ok 81 - commits: unresolvable detail
ok 82 - commits: 7 hex accepted
ok 83 - commits: uppercase hex accepted
ok 84 - commits: 6 hex rejected by length
ok 85 - clean: no violations
ok 86 - clean: exit 0
ok 87 - clean: six violation classes all PASS
ok 88 - env: non-git directory rejected
ok 89 - env: missing corpus/ rejected
ok 90 - cli: clean fixture exits 0
ok 91 - cli: json names the repo
ok 92 - cli: drifting fixture exits 1
ok 93 - cli: drifting fixture reports unindexed=1
not ok 94 - cli: unavailable git exits 2: got 1 want 2
not ok 95 - cli: unavailable git reports could-not-evaluate: got False want True
self-test: 95 assertions, 2 failures
```

stderr: empty.

#### restored — exit 0

Working directory: `/fast/scratch/hyaku/kotoba-r55/MutC2NewArms`.

```sh
timeout --signal=TERM --kill-after=5s 600s python3 -B verifiers/verify_corpus_independent.py --self-test
```

UTC access/run line:
```text
Fri Oct 23 12:15:24 AM UTC 2026
```

SHA-256 before / after detector: `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8` / `8b66d62bd859e415ffc195821f6f375367f8ae7aac326cbfb8b6e97fb1fef7c8`.

stdout:
```text
ok 1 - index: only orphan.md unindexed
ok 2 - index: unindexed detail names orphan.md
ok 3 - index: ghost.md + nomatch/*.md stale
ok 4 - index: stale detail (glob token counts as stale pattern)
ok 5 - index: ghost + 3 rooted tokens (external, rooted dead, rooted dead dir)
ok 6 - index: missing detail (brace expansions path-checked; rooted tokens checked)
ok 7 - index: eight tokens in the coverage map
ok 8 - index: one token outside the coverage map section, not counted
ok 9 - index: brace expansion
ok 10 - index: nested brace expansion
ok 11 - index: token without braces is its own expansion
ok 12 - index: ../ token is not corpus-internal
ok 13 - index: rooted token is not corpus-internal
ok 14 - fence: only the live row's token is harvested
ok 15 - fence: the fenced row's file stays unindexed
ok 16 - fence: unindexed detail names the fenced row's file
ok 17 - fence control: without the fence both rows count
ok 18 - fence control: both files are covered
ok 19 - fence pseudo-closer: only the live row's token is harvested
ok 20 - fence pseudo-closer: the quoted row's file stays unindexed
ok 21 - fence: a mismatched fence char does not close
ok 22 - fence: an unclosed tilde fence runs to EOF
ok 23 - fence: a mixed backtick pseudo-closer does not close tilde
ok 24 - fence: blockquote container is outside the line scanner
ok 25 - blockquote fence: only the live row is harvested
ok 26 - blockquote fence: quoted row file remains unindexed
ok 27 - blockquote fence: fail-safe impact names the unindexed file
ok 28 - fence: a shorter closer is content, not a closer
ok 29 - fence: a closer with an info string is content
ok 30 - fence: a closer with trailing text is content
ok 31 - fence: a longer closer closes
ok 32 - fence: a same-length closer closes
ok 33 - fence: an empty-info closer with trailing blanks closes
ok 34 - fence: a legal info opener still needs a >= opener-length closer
ok 35 - fence indent: a 0-space closer closes
ok 36 - fence indent: a 2-space closer closes
ok 37 - fence indent: a 3-space closer closes
ok 38 - fence indent: a 4-space closer is content
ok 39 - fence indent: a tab closer is content
ok 40 - fence indent: a mixed space+tab closer is content
ok 41 - fence indent: a 4-space opener is content
ok 42 - fence indent: a tab opener is content
ok 43 - fence indent: a 4-space tilde closer is content
ok 44 - fence indent: a tab tilde closer is content
ok 45 - fence indent 4space: only the live row's token is harvested
ok 46 - fence indent 4space: the quoted row's file stays unindexed
ok 47 - fence indent 4space: unindexed detail names the quoted file
ok 48 - fence indent tab: only the live row's token is harvested
ok 49 - fence indent tab: the quoted row's file stays unindexed
ok 50 - fence indent tab: unindexed detail names the quoted file
ok 51 - fence indent control: a 3-space closer closes, both rows count
ok 52 - fence indent control: a 3-space closer covers the second file
ok 53 - pointers: seven checked promises
ok 54 - pointers: all four shapes counted
ok 55 - pointers: four excluded tokens
ok 56 - pointers: every exclusion reason fires
ok 57 - pointers: one quoted token is context
ok 58 - pointers: dead relative, dead bare and dead prose token
ok 59 - pointers: dead detail
ok 60 - pointers: candidate population
ok 61 - pointers: shape absolute
ok 62 - pointers: shape tilde
ok 63 - pointers: shape relative
ok 64 - pointers: shape bare
ok 65 - pointers: rooted token resolves as-is
ok 66 - pointers: tilde resolves against HOME
ok 67 - pointers: relative hops resolve from the citing directory
ok 68 - pointers: bare token joins the citing directory
ok 69 - pointers: dotdot after leading hops detected
ok 70 - pointers: pure leading hops are not dotdot-after-hops
ok 71 - pointers: fleet-root report remains checked
ok 72 - pointers: existing fleet-root report resolves
ok 73 - commits: five citations in scope
ok 74 - commits: 6-hex, 41-hex and word are nonhash
ok 75 - commits: deadbeef unresolvable, the real sha resolvable
ok 76 - commits: exactly one hex citation resolves
ok 77 - commits: quoted citation is context
ok 78 - commits: candidate population
ok 79 - commits: two hex-shaped citations
ok 80 - commits: nonhash detail sorted
ok 81 - commits: unresolvable detail
ok 82 - commits: 7 hex accepted
ok 83 - commits: uppercase hex accepted
ok 84 - commits: 6 hex rejected by length
ok 85 - clean: no violations
ok 86 - clean: exit 0
ok 87 - clean: six violation classes all PASS
ok 88 - env: non-git directory rejected
ok 89 - env: missing corpus/ rejected
ok 90 - cli: clean fixture exits 0
ok 91 - cli: json names the repo
ok 92 - cli: drifting fixture exits 1
ok 93 - cli: drifting fixture reports unindexed=1
ok 94 - cli: unavailable git exits 2
ok 95 - cli: unavailable git reports could-not-evaluate
self-test: 95 assertions, 0 failures
```

stderr: empty.

