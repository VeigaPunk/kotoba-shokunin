# ScoutHostClients — C1 documentation tied to what is installed on this host

Result: DONE — six of the seven C1 clients are installed on this host with recorded versions, four of their
installed bundles carry the agent-definition directory the C1 table would name, and the host state corroborates
the counter's own-config-root rule while showing one plan line (the C2 trust boundary) pointing at a directory
that does not exist here.

Seat: `KotobaR56.ScoutHostClients` (leaf, read-only). Lane repo `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
at `3d8efd7c5c4709d5acfd61d11d066591d7d2d5ae` (post `e02f5f5`). All commands read-only; no lane file touched;
no git/jj write anywhere; no sandbox clone needed; nothing installed or upgraded. The only file this seat wrote
is this report.

UTC window: `Fri 23 Oct 2026 02:46:36 AM UTC` (start) through `~03:16 UTC`.

## 1. Installed clients — versions and resolved payloads

`for c in claude codex opencode gemini copilot cursor-agent code; do command -v "$c"; done` (exit 0), then
`"$c" --version` (each exit 0), then `readlink -f` + `file` on each resolved path.

| Client (C1 row name) | CLI | `--version` output | Path | Resolved payload |
|---|---|---|---|---|
| Claude Code | `claude` | `2.1.304 (Claude Code)` | `/usr/bin/claude` | 110-byte sh wrapper → `/opt/claude-code/bin/claude` (Bun bundle) |
| Codex | `codex` | `codex-cli 0.163.0` | fnm multishell shim | `…/fnm/node-versions/v24.21.0/…/node_modules/@openai/codex/bin/codex.js` → native `…/@openai/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex` |
| opencode | `opencode` | `1.19.4` | `~/.local/bin/opencode` | 1460-byte bash wrapper (mise node + `npx opencode-ai`) → `~/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, 214,522,032 bytes |
| Gemini CLI | `gemini` | `0.65.0` | `~/.local/bin/gemini` | wrapper → `~/.npm/_npx/d07ada7b4a99c96e/node_modules/@google/gemini-cli` |
| Copilot CLI | `copilot` | `GitHub Copilot CLI 1.0.103.` (+`Run 'copilot update' to check for updates.`) | `~/.local/bin/copilot` | wrapper → `~/.npm/_npx/965e8981e34edf7c/node_modules/@github/copilot` → native `@github/copilot-linux-x64/copilot`, 198,445,888 bytes |
| Cursor | `cursor-agent` | `2026.10.22-27dcf5f` | `~/.local/bin/cursor-agent` | `~/.local/share/cursor-agent/versions/2026.10.22-27dcf5f/cursor-agent` (bash) → `index.js` + `cursor-agent-sea`, `cursor-agent-worker-sea` |
| VS Code | `code` | **MISSING** | — | also missing: `code-oss`, `codium`, `vscodium`, `code-insiders`; and `~/.config/Code`, `~/.config/Code - OSS`, `~/.config/VSCodium`, `~/.vscode`, `~/.vscode-oss` all absent |

Consequence for C1: the VS Code row is the one row this host cannot corroborate by introspection; the other six
can. (Observed, exit codes above.)

## 2. Agent-definition directories that exist on this host

`ls -d ~/.claude/agents ~/.codex/agents ~/.config/opencode/agents ~/.gemini/agents ~/.cursor/agents ~/.copilot/agents`:

| Path | State | File counts (`find -maxdepth 3`) |
|---|---|---|
| `~/.claude/agents` | EXISTS | regular files 0, symlinks 1, entries 2 — single entry `the-kimiraikkoner.md -> /home/vgpnk/Projects/the-kimiraikkoner/the-kimiraikkoner.md` |
| `~/.codex/agents` | ABSENT | — (`~/.codex` holds `config.toml`, `auth.json`, `goals_1.sqlite`, `app-server-*`, …) |
| `~/.config/opencode/agents` | ABSENT | — (`~/.config/opencode` holds only `cli.json`, `opencode.json`, `service.json`) |
| `~/.config/opencode/agent` (singular) | ABSENT | — |
| `~/.gemini/agents` | ABSENT | — (`~/.gemini` is empty, `total 0`) |
| `~/.cursor/agents` | ABSENT | — (`~/.cursor` holds `agent-cli-state.json`, `ai-tracking`, `plugins`, `projects`, `sandbox-policies`, `skills-cursor`) |
| `~/.copilot/agents` | ABSENT | — (`~/.copilot` holds `config.json`, `installed-plugins`, `logs`, `session-state`) |

Note the counting nuance: `find ~/.claude/agents -type f | wc -l` prints `0` because the only entry is a
symlink; the directory is not empty in the sense of a listing. A future instrument that counts regular files
only would read this directory as empty.

Repo-level, `/home/vgpnk/Projects` to depth 2 (and a depth-3 pass for the dot-directory forms):

| Path | Files |
|---|---|
| `/home/vgpnk/Projects/ufo-fsd-alpha/agents` | 13 regular `.md` (`connector, critic, distiller, executor, labrat, mutation-tester, planner, revenger, reviewer, scout, scribe, sentinel, simplifier`) |
| `/home/vgpnk/Projects/opencodeufo/.opencode/agents` | 8 regular `.md` (`architect, executor, fallback, porter, reader, reviewer, scout-go, scout`) |

No other `agents`/`agent` directory exists at depth 2 under `/home/vgpnk/Projects`, and no
`.github/agents`, `.vscode/agents`, `.codex/agents`, `.cursor/agents`, `.gemini/agents`, `.copilot/agents`
exists at depth 3. The lane repo itself carries none of these forms.

## 3. What the installed code itself says (the C1 tie)

Method: bounded `grep -aoE` over the resolved payload named in §1, regex requiring the client's own config
directory segment. This is evidence that the installed build *references* a path, not proof of load semantics
(no client was driven; no paid calls; no config mutated).

- **Claude Code** (`/opt/claude-code/bin/claude`, raw grep exit 0): `.claude/agents/` ×12, `.claude/agents/*.md`
  ×7, `.claude/agents` ×6, `~/.claude/agents/*.md`, `~/.claude/agents/`, `~/.claude/agents`; also
  `.claude/agent-memory/`, `.claude/agent-memory-local/`, `.claude/agent-registry.json`. Runtime strings read
  `… comes from its definition (`.claude/agents/*.md` frontmatter or SDK `agents`)` and
  `n:"(removed) Ask Claude to create/manage subagents, or edit .claude/agents/"`. The bundle also carries the
  literal `code.claude.com/docs/en/sub-agents` (the same page base row S026 already cites).
- **opencode** (`…/opencode-ai/bin/opencode.exe`, exit 0): exactly one hit, `.opencode/agents/`, in a UI string:
  `Add {highlight}.md{/highlight} files to {highlight}.opencode/agents/{/highlight} for specialized AI personas`.
  No `.config/opencode/agent(s)` literal exists in this payload; the only `.config/opencode/…` strings are
  `.config/opencode/.` ×2 and `.config/opencode/tui.json` ×1.
- **Gemini CLI** (installed package ships its own docs, exit 0): `bundle/docs/core/subagents.md:323-324`
  `1.  **Project-level:** `.gemini/agents/*.md` (Shared with your team)` /
  `2.  **User-level:** `~/.gemini/agents/*.md` (Personal agents)`, and `:331`
  `**Example: `.gemini/agents/security-auditor.md`**`; `bundle/docs/reference/commands.md:26-27`
  ``Rescans agent directories (`~/.gemini/agents` and `.gemini/agents`) and reloads the registry.``;
  `bundle/docs/core/remote-agents.md:32-33` repeat the two levels.
- **Copilot CLI**: runtime `copilot --help` (exit 0) lines 115-116:
  `Allow file access to a directory and load its .github/skills` / `and .github/agents as trusted configuration (can be used`
  (continues `multiple times). A relative path resolves against the …`); `--agent <agent>` at line 62
  (`Specify a custom agent to use`). Raw grep of the 198 MB native binary for `.github/agents` returned **no
  matches** — the binary's strings are packed/compressed, so a raw-binary grep is not decisive for Copilot.
  The runtime help output is decisive and is the host evidence for this client.
- **Cursor** (`…/2026.10.22-27dcf5f/`, exit 0): `index.js` and both SEA binaries each hold one `.cursor/agents`
  literal; the globs are `"**/.cursor/agents/**/*.md"`, `.cursor/agents/**/*.mdc`,
  `.cursor/agents/**/*.markdown`, `.cursor/agents/**`, and a config table with
  `configDir:".cursor",subdir:"agents"` (×3). The same table also carries
  **`configDir:".claude",subdir:"agents"` (×3)**, alongside `.claude/skills`, `.codex/skills`,
  `.cursor/rules`, `.cursor/skills`, `.cursor/skills-cursor`, `.agents/skills`, `.grok/skills`.
- **Codex** (native `…/codex-linux-x64/vendor/x86_64-unknown-linux-musl/bin/codex`, exit 0): the only hit is a
  raw string-table fragment `…urlref.codex.codex/config.toml.codex/agents.codex/hooks.agents.agents/skills, plugins/cache…`.
  Rust binaries concatenate length-prefixed literals, so `.codex/agents` is a plausible member of that table —
  **[INFERENCE]**, not established by this grep. `codex --help` (exit 0) offers `agents` only as
  `Browse all agent sessions on the shared local app-server daemon`, and the host `~/.codex/config.toml` has no
  agent-definition key (its only `agent` line is `args = [ "-y", "rea-agents@6.7.0", "mcp" ]`, an MCP server).
  **Codex is the one client whose agent-definition directory this host does not corroborate.**

## 4. What this means for C1 (report only; no counter, entry or SKILL.md text was touched)

1. **Corroborated by installed code on this host**: Claude Code `.claude/agents`; Cursor `.cursor/agents`;
   opencode `.opencode/agents`; Gemini CLI `.gemini/agents`; Copilot CLI `.github/agents` (runtime help only).
2. **Not corroborated here**: Codex (string-table fragment only), VS Code (client not installed at all).
3. **The counter's own-root rule matches installed reality.** `verifiers/check_agent_definitions.py` (v1.3 at
   `3d8efd7`) restricts each client to its own configuration root and treats a compatibility path as the other
   client's form. Cursor's own installed table loads `configDir:".claude",subdir:"agents"` in addition to
   `.cursor/agents`, so a `.claude/agents` quote could legitimately appear on a Cursor-owned page — the
   erratum's refusal of that as Cursor's row is host-corroborated, not merely a convention.
4. **A plan line to re-check.** The plan's C2 trust boundary (withdrawn claim, kept as redesign input) names
   "an independent run of the delegate on the live `~/.config/opencode/agents/` files". That directory does not
   exist on this host (`~/.config/opencode` holds three JSON files only), and the installed opencode 1.19.4
   binary's own literal is `.opencode/agents/` (plural, project scope). The live plural example here is
   `/home/vgpnk/Projects/opencodeufo/.opencode/agents` with 8 `.md` files. A later round reusing that trust
   boundary line should name an existing directory or accept `~/.config/opencode/agent` singular too.
5. **Counting caveat for any host-side instrument**: `~/.claude/agents` holds one symlink and zero regular
   files; a regular-file-only count reports it empty.

## 5. Gaps and limits of this seat

- The literal-presence method shows a client's build mentions a path; it does not show the client loads it, nor
  whether the documented directory is the user-level or project-level one in each case. C1's "What the file
  sets" column is not checkable this way.
- No client was driven beyond `--version`, `--help` and package-file reads; `opencode agent list` was attempted
  once and returned `Error: Unexpected error` / `Database is not empty and has no session table` (unrelated to
  agents; no state in the agent directories was touched).
- Raw grep is non-decisive for the two packed native binaries (Copilot: no hits for a string that provably
  exists at runtime; Codex: one ambiguous fragment).
- This seat did not open any network source, did not read the C1 entry or the counter's own rules in full, and
  scored nothing.
