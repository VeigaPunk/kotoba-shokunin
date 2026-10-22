Result: HOLDS — the installed Claude Code 2.1.304 is well above the docs' 2.1.277 floor and exposes a model-free reader for the "Project instructions" setting (exit 0), but the list of files a session actually loads is only observable inside a model-backed session, which this seat was forbidden to start.

## 1. Identity and version

- `claude --version` → `2.1.304 (Claude Code)`, exit 0.
- `claude doctor` (run in `/tmp`, exit 0) → `Running: package-manager (2.1.304)`, `Commit: 17ab70404e5b`, `Platform: linux-x64`, `Package manager: pacman`, `Path: /opt/claude-code/bin/claude`, `No installation issues found.`
- `/usr/bin/claude` is a 110-byte POSIX shell wrapper owned by root: it exports `DISABLE_UPDATES=1` and `DISABLE_INSTALLATION_CHECKS=1`, then `exec /opt/claude-code/bin/claude "$@"`. sha256 `356673de39ab5e9e4d19314c33b2d0b01fa06519a44c3374aa947bfbd71a4049`.
- Real binary `/opt/claude-code/bin/claude`, 288,730,480 bytes, ELF 64-bit x86-64, not stripped, sha256 `ea0f135784631619a7a409d07322ecec964f9cc4fd377508ed1ba3f141f27912`, mtime 2026-10-19 19:39. `claude doctor` reports `Package manager: pacman` and `Auto-updates: Managed by package manager` (its own `Config install method` line reads `unknown`); the wrapper suppresses update checks in any case.
- Version floor: `2.1.304 >= 2.1.277` (27 patch levels above). Docs basis, `memory.md:364`: "Reading `AGENTS.md` directly requires Claude Code v2.1.277 or later." The negative case is stated at `memory.md:415`: "You're on a Claude Code version before v2.1.277". So this host is above the floor and AGENTS.md-as-project-instructions is available in principle.

## 2. Source basis fetch (re-opened this seat)

- URL `https://code.claude.com/docs/en/memory.md`, accessed 2026-10-22T20:04:37Z, HTTP 200, 51,971 bytes, 638 lines, sha256 `971d75bfce7a04c2e0d41e8752d01afe29ed500f2a7159f66d5f7156bea0c3ff`. Saved at `/fast/scratch/hyaku/kotoba-r53/ScoutClaudeBehaviour/memory.md`.
- Section line anchors in the fetched bytes: `## AGENTS.md` at 350; combination table 354-358; version note 364; "When Claude Code reads AGENTS.md" 366-377; "Choose which instruction files load" 384-395; plugin-ID note 407; "When AGENTS.md support is unavailable" 411-419; "Share one file with other coding tools" 442-461.
- Verbatim quotes (each at most 25 words, line numbers are in the fetched bytes):
  - `memory.md:356` row: an `AGENTS.md` with "no `CLAUDE.md` or `CLAUDE.local.md`" in the working directory "or above it" → "Your `AGENTS.md`".
  - `memory.md:357` row: both present → "Your `CLAUDE.md` files only".
  - `memory.md:391`: "Claude Code skips an `AGENTS.md` it has already loaded".
  - `memory.md:395`: "Add it to `pluginConfigs` under `cc-plugin-agents-md@builtin`, the ID of the built-in plugin that reads `AGENTS.md`."
  - `memory.md:395`: "ignores it in project and local settings files".
  - `memory.md:407`: "Claude Code v2.1.285 and later reads an entry under either ID."
  - `memory.md:442`: "you can still keep it as the one file every tool shares by putting an `@AGENTS.md` import in a `CLAUDE.md`".
  - `memory.md:445` code line: `@AGENTS.md`. `memory.md:452`: "If you don't need Claude-specific content, a symlink also works:". `memory.md:455` code line: `ln -s AGENTS.md CLAUDE.md`.
  - `memory.md:70`: "run `/context` in a session and check the list under **Memory files**".
  - `memory.md:375`: "In an interactive session you see a line such as `no CLAUDE.md found; AGENTS.md loaded: /home/you/repo/AGENTS.md`".
  - `memory.md:427` table row, `InstructionsLoaded` hooks: "Don't fire. They fire as usual for an `AGENTS.md` that a `CLAUDE.md` imports or symlinks to".
  - `memory.md:96`: "The audit runs through the bundled `/claude-api` skill." `memory.md:98`: "`/doctor prompt-audit` requires Claude Code v2.1.283 or later."

## 3. Primary finding — a model-free reader for the Project instructions setting

`claude plugin configure cc-plugin-agents-md@builtin --json` runs with no session and no model call. Exit 0, 1,220 bytes of JSON (`/fast/scratch/hyaku/kotoba-r53/ScoutClaudeBehaviour/configure.json`). On this host (default config):

- `schema.instructionFiles.title` = `"Project instructions"`, `default` = `"claude-md-or-agents-md"`, `options` = `["claude-md","claude-md-or-agents-md","claude-md-and-agents-md","managed-only"]`.
- `inputs.instructionFiles` = `"claude-md-or-agents-md"` — the effective value.
- `unconfigured` = `["instructionFiles"]` — nothing explicitly set; `configured` = `[]`.

So `inputs` reports the effective value with the default applied, and `unconfigured` reports whether it came from a settings file at all. A disk-only instrument can use exactly this command to decide which row of the docs table applies; it does not have to guess the default or parse the settings schema itself.

Non-JSON form, same exit 0: `claude plugin configure cc-plugin-agents-md@builtin` prints `Options for cc-plugin-agents-md (cc-plugin-agents-md@builtin):` / `❯ instructionFiles — Project instructions (optional, not set)`.

Read-only: running the command twice left `settings.json` byte-identical (sha256 `cb32b1fa585794cc074042e4451f8301e1ccfb765ac27e420b677e58f045cb36` before and after). It does create `$CLAUDE_CONFIG_DIR/.claude.json` and `$CLAUDE_CONFIG_DIR/backups/` in the redirected config directory it is given.

Related surfaces: `claude plugin details cc-plugin-agents-md@builtin` (exit 0) describes the built-in as "AGENTS.md as project instructions: by default loaded where the project has no CLAUDE.md; by its instructionFiles option, loaded beside CLAUDE.md, left out, or with the project instructions dropped". `claude plugin list` and `claude plugin list --json` do not list built-in plugins at all, so they cannot be used to detect this one.

## 4. Scope and precedence tests of that reader

All runs used a throwaway `CLAUDE_CONFIG_DIR` under `/fast/scratch/hyaku/kotoba-r53/ScoutClaudeBehaviour/`, so the real `~/.claude` config was never the input.

| Case | Config content | `inputs` | `unconfigured` | exit |
| :- | :- | :- | :- | :- |
| B | user `settings.json`: `pluginConfigs["cc-plugin-agents-md@builtin"].options.instructionFiles = "claude-md-and-agents-md"` | `claude-md-and-agents-md` | `[]` | 0 |
| C | user `settings.json`: top-level `"projectInstructions": "claude-md-and-agents-md"` | `claude-md-or-agents-md` (default) | `["instructionFiles"]` | 0 |
| D | both of the above | `claude-md-and-agents-md` | `[]` | 0 |
| E | user `settings.json` under the legacy id `agents-md@builtin`, value `claude-md` | `claude-md` | `[]` | 0 |
| P | project `./.claude/settings.json` sets `instructionFiles = "claude-md"` | `claude-md-or-agents-md` (default) | `["instructionFiles"]` | 0 |

Reading of the table, matched against the docs: user settings are read (`memory.md:395` names `~/.claude/settings.json`); the legacy plugin id is still honoured on 2.1.304 (`memory.md:407`); project settings are ignored (`memory.md:395`); a bare top-level `projectInstructions` key has no effect on 2.1.304. `--settings` is not accepted by this subcommand: `claude plugin configure ... --json --settings '{...}'` → `error: unknown option '--settings'`, exit 1, so the reader cannot exercise the `--settings`-file path even though the docs say the loader reads it.

The binary carries warning strings for the superseded key ("option projectInstructions in settings is not read: instructionFiles ... is set; remove projectInstructions") but neither `claude plugin configure` nor `claude doctor` printed any warning in cases C and D. Whatever emits them is in-session. Extract evidence: `/fast/scratch/hyaku/kotoba-r53/ScoutClaudeBehaviour/claude.strings` (produced with `strings -n 10 /opt/claude-code/bin/claude`), lines 396920-396922.

## 5. What `claude doctor` does and does not report

- `claude doctor` prints install health only. Run in a directory containing both `AGENTS.md` and a `CLAUDE.md` with `@AGENTS.md`, the output was byte-identical to the empty-directory run apart from wall time (`diff` exit 0). It reports no instruction files, no memory list, and no Project instructions value.
- `claude doctor --help` (exit 0) offers only `-h`. There is no `--json` and no memory subcommand.
- `claude doctor prompt-audit` ignores the argument and prints the ordinary doctor report (exit 0) — there is no CLI form of prompt-audit.

## 6. prompt-audit is model-backed, so out of bounds

`memory.md:96-98` places the audit behind the bundled `/claude-api` skill and sets a 2.1.283 floor, which 2.1.304 meets. The binary confirms the mechanism: the slash-command body is a prompt handed to the model, beginning "Run the `prompt-audit` subcommand from the Subcommands table above: read `shared/prompt-audit.md` first and follow it in order." (claude.strings lines 282988-282989, duplicated at 438340). Running it therefore requires a model call, which the assignment forbids. Consequence for C2: prompt-audit cannot be the instrument, and no alwayson.04/07 box may lean on it.

## 7. Only observable inside a session (not determinable under this bound)

- The loaded-file list: `/context` → **Memory files** row (`memory.md:70`; `/context all to expand` and the `Memory files` row are in the binary at claude.strings 389892 and 322452).
- The startup notice `no CLAUDE.md found; AGENTS.md loaded: ` (`memory.md:375`; literal at claude.strings 396922). It is emitted in the conversation, and a conversation needs a model call to start.
- `InstructionsLoaded` hooks, which fire for `CLAUDE.md` but not for an `AGENTS.md` read through the setting (`memory.md:427`; hook literals at claude.strings 226522, 226557, 258753). A hook-based probe still needs a session.

None of these was executed: no `claude -p`, no interactive session, no background session (`--bg`), no `--resume`/`attach`.

## 8. Built-in plugin enable state is not readable from the non-model surfaces tried

Disabling the built-in plugin also removes AGENTS.md support (`memory.md:415-417`), so an instrument would ideally check it. `claude plugin list`, `claude plugin list --json` and `claude plugin list --available --json` (exit 0; `installed` holds only `cowork-plugin-management@synced`, `available` is the marketplace catalogue) never show built-ins, and `claude plugin details cc-plugin-agents-md@builtin` prints no enabled field. `claude plugin list --all --json` is rejected: `error: unknown option '--all'`, exit 1. This remains an unknown for the instrument.

## 9. Implication for alwayson.04 and alwayson.07 [INFERENCE]

From the observed behaviour only, a disk-only instrument can decide: (a) the effective Project instructions value, hence which of the four docs rows applies (section 3, section 4); (b) which candidate files exist up the ancestor chain and whether a `CLAUDE.md` shadows `AGENTS.md` (`memory.md:356-357`); (c) whether a redirect exists, by matching an `@AGENTS.md` import line versus a prose mention (`memory.md:442-445`) and by resolving a `CLAUDE.md` symlink to `AGENTS.md` with `readlink` (`memory.md:452-455`, plus the write-through-symlink caveat at 460). It cannot confirm that the client actually loaded them; that needs a session. This matches the plan's split, where the counter scores the instrument's behaviour on pinned cases, not the live client.

## 10. Environment-switch string evidence (not behaviour)

The binary contains 31 `CLAUDE_CODE_*` names matching MD/MEMORY/INSTRUCT/CONTEXT, including `CLAUDE_CODE_DISABLE_CLAUDE_MDS`, `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD`, `CLAUDE_CODE_DISABLE_ORG_MEMORY`. Presence is string evidence only; none of these switches was exercised, so their semantics are unverified and should not be asserted in the corpus without a run.

## 11. Boundary compliance and side effects

- No paid or model call of any kind: no `claude -p`, no `claude run`, no interactive or background session, no `--resume`. Commands used were `--version`, `--help`, `doctor` (with and without arguments), `plugin list`, `plugin details`, `plugin configure` (read mode, no `--values-stdin`), and read-only reads of `~/.claude/settings.json` and `~/.claude.json`.
- Nothing was written in the lane except this report file. All scratch, config dirs and extracted strings live under `/fast/scratch/hyaku/kotoba-r53/ScoutClaudeBehaviour/`.
- Side effect disclosure: these client invocations refreshed the client's own state files in the home directory. `~/.claude.json` mtime moved to 2026-10-22 17:06:56 (backups created at 17:04 and 17:06 under `~/.claude/backups/`), `~/.claude/.credentials.json` and `~/.claude/plugins/.last_inuse_sweep` were touched at 17:04-17:05. `~/.claude/settings.json` was not modified (mtime still 2026-10-19 12:36, content still only `{"theme":"dark"}`, so the live Project instructions value is the default `claude-md-or-agents-md`).
- No package was installed or upgraded; no pacman transaction was attempted.

## 12. Command log (command → exit; observed output)

1. `/usr/bin/claude --version` → 0; `2.1.304 (Claude Code)`.
2. `timeout 120 /usr/bin/claude doctor` → 0; health block quoted in section 1, `No installation issues found.`
3. `claude doctor --help` → 0; only `-h, --help`.
4. `claude doctor prompt-audit` → 0; ordinary doctor output, argument ignored.
5. `claude --help` → 0; command list has `agents, attach, auth, auto-mode, doctor, gateway, import, install, logs, mcp, plugin, purge, respawn, rm, setup-token, stop, ultrareview, update`. No `config` and no `memory` command.
6. `claude config --help` → 0 but only the top-level help is shown; `config` is not a subcommand in 2.1.304.
7. `claude plugin --help` → 0; subcommands include `configure`, `details`, `list`, `enable`, `disable`, `eval`, `install`.
8. `claude plugin configure cc-plugin-agents-md@builtin --json` → 0; `inputs.instructionFiles = claude-md-or-agents-md`, `unconfigured = ["instructionFiles"]`.
9. `claude plugin configure agents-md@builtin --json` → 1; `No installed plugin has the id "agents-md@builtin". Use its full id (name@marketplace), as `claude plugin list` shows it.` Bare names `agents-md` and `cc-plugin-agents-md` behave the same; only the full id resolves.
10. `claude plugin details cc-plugin-agents-md@builtin` → 0; description plus zero skills/agents/hooks/MCP/LSP and `Always-on: ~0 tok`.
11. `claude plugin details cc-plugin-agents-md@builtin --json` → 1; `error: unknown option '--json'`.
12. `claude plugin list` → 0; only `cowork-plugin-management@synced`.
13. `claude plugin list --json` → 0; one entry, no built-ins.
14. `claude plugin list --available --json` → 0; `{"installed":[...],"available":[...]}`, still no built-ins.
15. `claude plugin list --all --json` → 1; `error: unknown option '--all'`.
16. Cases B/C/D/E/P from section 4: each `claude plugin configure cc-plugin-agents-md@builtin --json` under `CLAUDE_CONFIG_DIR=<case>` → exit 0, values as tabled. `doctor` under cases C and D → exit 0 with no instruction-key diagnostics.
17. `claude plugin configure ... --json --settings '{...}'` → 1; `error: unknown option '--settings'`.
18. Re-ran case B after hashing: settings file sha256 unchanged, exit 0.
19. `diff` of doctor output in `/tmp` versus a directory holding `AGENTS.md` + `CLAUDE.md` → 0 (identical).
20. `sha256sum /usr/bin/claude /opt/claude-code/bin/claude` → hashes in section 1.

## 13. Remaining unknowns

- Whether the built-in agents-md plugin is enabled on this host; no non-model surface tried exposes it (section 8).
- The concrete file list a session loads here, and the exact wording the client emits at launch on 2.1.304; both need a session.
- Semantics of `CLAUDE_CODE_DISABLE_CLAUDE_MDS` and the other instruction-related environment switches (section 10).
- The `--settings`-file path of the loader could not be exercised through `plugin configure`, which rejects the flag; a session-only path was out of bounds.
- No check was made of the marketplace network response beyond the fact that `plugin list --available` returned catalogue data with exit 0.
