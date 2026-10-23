Result: DONE — The assigned MCP gate now returns 2 for unknown revisions and when Git cannot run; its self-test and real verdict remain valid.

## Change
- Updated only `verifiers/check_mcp_instructions.py` in the sandbox clone and committed as `1ee2dc10056fe2d20c690a238bd68dc57ffb1d5a`.
- The gate verifies `--rev` with `git rev-parse --verify --quiet <rev>^{commit}` before reading files (`verifiers/check_mcp_instructions.py:305-310`) and maps `OSError` to its existing `could-not-evaluate:` stderr path (`:314-316`). Its read/judge/count/output logic is unchanged.
- Added self-test arms for an unknown 40-hex revision and a subprocess whose PATH contains only a `python3` link (`:264-283`).
- Unified diff: `.ufo/waves/round-55/build/FixMcpInstructions.patch`.
- Diff stat: `verifiers/check_mcp_instructions.py | 31 ++++++++++++++++++++++++++++++-`; 1 file changed, 30 insertions(+), 1 deletion(-).

## Probe causes and evidence
- **R (unknown revision):** At the plan commit, `read_file` ran `git show <rev>:<path>` (`verifiers/check_mcp_instructions.py:102`). Its error handling treated the phrase `exists on disk, but not in` as a missing file and returned `None` (`:104-108`), so the gate produced an ordinary failed verdict instead of an evaluation error. Confirmed with `git show 0000000000000000000000000000000000000000:corpus/knowledge/mcp-server-instructions-round52.md`: exit 128, `fatal: path 'corpus/knowledge/mcp-server-instructions-round52.md' exists on disk, but not in '0000000000000000000000000000000000000000'`. The baseline gate run with that revision returned exit 1 and `mcp instructions backed 0 of 7 clients`.
- **G (Git absent):** At the plan commit, `subprocess.run` in `read_file` (`:102`) could raise `FileNotFoundError`, while `main` caught only `RuntimeError` (`:285-287`). A baseline run with PATH limited to the `python3`-only directory raised `FileNotFoundError: [Errno 2] No such file or directory: 'git'` and exited 1. The plan receipt also records both MCP probes as misses (`.ufo/waves/round-55/controls/C2-base.txt:21-24`).

## Checks explicitly requested
- Before change, `python3 -B verifiers/check_mcp_instructions.py --self-test`: `self-test: 0 failure(s) over 10 assertions`; exit 0.
- After change, the same command: `self-test: 0 failure(s) over 14 assertions`; exit 0. Assertion count: 10 → 14.
- After change, frozen counter command `python3 -B verifiers/check_could_not_evaluate.py --rev HEAD` measured commit `1ee2dc10056fe2d20c690a238bd68dc57ffb1d5a` and reported:
  ```
  check_mcp_instructions.py          R expect 2   got 2 ok
  check_mcp_instructions.py          G expect 2   got 2 ok
  check_mcp_instructions.py          S expect 0   got 0 ok
  check_mcp_instructions.py          V expect 0|1 got 0 ok
  could-not-evaluate probes honoured 15 of 25; controls held 13 of 13
  ```
  Counter exit 1. The assigned gate passes R/G/S/V; the frozen overall C2 predicate remains unmet because other gates still miss probes.
- Real verdict before the change, at the plan commit: `python3 -B verifiers/check_mcp_instructions.py --rev a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` → exit 0; summary `mcp instructions backed 7 of 7 clients`.
- Real verdict after the change, at the plan commit: same command, exit 0; summary `mcp instructions backed 7 of 7 clients`.
- Real verdict after the change, at the sandbox commit: `python3 -B verifiers/check_mcp_instructions.py --rev HEAD` → exit 0; summary `mcp instructions backed 7 of 7 clients`.

Risk/blocker: none for this scoped gate repair. The C2 counter as a whole remains red at 15/25; this seat changed no other gate.