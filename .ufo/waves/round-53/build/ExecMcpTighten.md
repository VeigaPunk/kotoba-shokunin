Result: DONE — Tightened both MCP counter matchers, killed M12 and M16, and retained the three requested revision counts.

## Changes and behavior

- Patch changes only `verifiers/check_mcp_instructions.py`. Host/path pins now require the exact host and either the exact pinned path or a slash-delimited descendant; a path such as `/modelcontextprotocol-evil/...` is rejected. Host-only pins retain their existing host/subdomain behavior.
- The Gate parser reads recorded quotes within each `S###` bullet in `corpus/lessons/round-52.md` § Gate. A row now backs only when its quote cell equals a recorded quote for that same ID. The rule is exact string equality; committed rows satisfy it (the tightened run at `e78dff66` remains 7/7). S042's two explicitly recorded quotes are both retained.
- Added `--self-test`: 8 assertions (5 M12 boundary/host cases, 3 M16 exactness/row cases). Base had no self-test option or assertion tally. New count for the parent to account for: 8 assertions. No floor files were edited.
- LSP was unavailable in the supplied tool inventory; no LSP endpoint was exposed. No installs or upgrades.

## Mutant evidence

The round-52 mutation report identifies M12 and M16 at `.ufo/waves/round-52/falsify-a2/MutMcpCounter.md:89-100,128-135`. Before tightening, the M12 mutant used S032's URL `https://github.com/modelcontextprotocol-evil/specification/2025-11-25/schema.md`; M16 changed only the entry quote to `"appended to the system instructions."` while the Gate kept the full quote.

- Before, M12 (`e32840a8a39873b358bbb5bf1173a3efc3f08e88`): `python3 -B verifiers/check_mcp_instructions.py --rev e32840a8a39873b358bbb5bf1173a3efc3f08e88` → `mcp instructions backed 7 of 7 clients`, exit 0.
- Before, M16 (`a7ed84dba7b21abd2c5bc6a40154ff16cd0afc05`): `python3 -B verifiers/check_mcp_instructions.py --rev a7ed84dba7b21abd2c5bc6a40154ff16cd0afc05` → `mcp instructions backed 7 of 7 clients`, exit 0.
- After, M12 (`--root .` on the one-fault working tree): `MCP specification  no S032 source URL 'https://github.com/modelcontextprotocol-evil/specification/2025-11-25/schema.md' not on a pinned host`; `mcp instructions backed 6 of 7 clients`, exit 0.
- After, M16 (`--root .` on the one-fault working tree): `Gemini CLI         no round-52 Gate does not record this quote for S036`; `mcp instructions backed 6 of 7 clients`, exit 0.

Both after-mutant data edits were restored before packaging. The M12 arm rejects the former prefix matcher; the M16 fragment arm rejects the former substring matcher.

## Required revision measurements

All three used the tightened script in the sandbox clone.

- `python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882` (exit 0):
  ```text
  MCP specification  BACKED
  Claude Code        BACKED
  VS Code            BACKED
  Codex              BACKED
  Gemini CLI         BACKED
  opencode           no rows naming client: 0 (need 1)
  Copilot CLI        no rows naming client: 0 (need 1)
  mcp instructions backed 5 of 7 clients
  exit=0
  ```
- `python3 -B verifiers/check_mcp_instructions.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302` (exit 0):
  ```text
  MCP specification  BACKED
  Claude Code        BACKED
  VS Code            BACKED
  Codex              BACKED
  Gemini CLI         BACKED
  opencode           BACKED
  Copilot CLI        BACKED
  mcp instructions backed 7 of 7 clients
  exit=0
  ```
- `python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c5b48789e56fb9060ddd48f33569e1215` (exit 1):
  ```text
  MCP specification  no rows naming client: 0 (need 1)
  Claude Code        no rows naming client: 0 (need 1)
  VS Code            no rows naming client: 0 (need 1)
  Codex              no rows naming client: 0 (need 1)
  Gemini CLI         no rows naming client: 0 (need 1)
  opencode           no rows naming client: 0 (need 1)
  Copilot CLI        no rows naming client: 0 (need 1)
  mcp instructions backed 0 of 7 clients
  exit=1
  ```

Self-test evidence: `python3 -B verifiers/check_mcp_instructions.py --self-test` → `self-test: 0 failure(s) over 8 assertions`, exit 0.

## Commands and exit codes

Commands below ran in the assigned sandbox clone unless a destination is shown. Successful calls that did not print an explicit `exit=` returned 0.

1. `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten checkout -q 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` — exit 0.
2. `git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten add corpus/SOURCES.md && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten -c user.name='Kotoba R53 Executor' -c user.email='kotoba-r53-exec@example.invalid' commit -qm 'mutant M12 evil sibling path' && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten rev-parse HEAD` — exit 0; `e32840a8a39873b358bbb5bf1173a3efc3f08e88`.
3. `python3 -B verifiers/check_mcp_instructions.py --rev e32840a8a39873b358bbb5bf1173a3efc3f08e88` — 7/7; exit 0.
4. `git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten -c user.name='Kotoba R53 Executor' -c user.email='kotoba-r53-exec@example.invalid' revert --no-edit HEAD && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten rev-parse HEAD` — exit 0; `fdfd683471fc7fe1a24389874920381f542b910d`.
5. `git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten add corpus/knowledge/mcp-server-instructions-round52.md && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten -c user.name='Kotoba R53 Executor' -c user.email='kotoba-r53-exec@example.invalid' commit -qm 'mutant M16 quote fragment' && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten rev-parse HEAD` — exit 0; `a7ed84dba7b21abd2c5bc6a40154ff16cd0afc05`.
6. `python3 -B verifiers/check_mcp_instructions.py --rev a7ed84dba7b21abd2c5bc6a40154ff16cd0afc05` — 7/7; exit 0.
7. `git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten -c user.name='Kotoba R53 Executor' -c user.email='kotoba-r53-exec@example.invalid' revert --no-edit HEAD && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten rev-parse HEAD` — exit 0; `d93dd74f4f3d95fa0c5b57b6f97d12b771b47a01`.
8. `python3 -B verifiers/check_mcp_instructions.py --self-test; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — 0 failures over 8 assertions; exit 0.
9. `python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — 5/7; exit 0.
10. `python3 -B verifiers/check_mcp_instructions.py --rev e78dff667237fba2e3cf9eccb802eff5bc9ea302; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — 7/7; exit 0.
11. `python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c5b48789e56fb9060ddd48f33569e1215; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — 0/7; exit 1.
12. `python3 -B verifiers/check_mcp_instructions.py --root .; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — M12 after: 6/7; exit 0.
13. `python3 -B verifiers/check_mcp_instructions.py --root .; rc=$?; printf 'exit=%s\\n' "$rc"; exit "$rc"` — M16 after: 6/7; exit 0.
14. `git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten add -A && git -C /fast/scratch/hyaku/kotoba-r53/ExecMcpTighten diff --cached --binary 3bb0a7a33e6eb585a83a1a55dee30b26079b1e36 > /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-53/build/ExecMcpTighten.patch` — exit 0.

## Delivered files, risks, and blockers

- Patch source changed: `verifiers/check_mcp_instructions.py` only.
- Delivered artifacts: `.ufo/waves/round-53/build/ExecMcpTighten.patch` and this report, `.ufo/waves/round-53/build/ExecMcpTighten.md`.
- No blocker. The parent must account for the 8 new self-test assertions in the assertion-floor registry at integration; those floor files were intentionally left untouched.