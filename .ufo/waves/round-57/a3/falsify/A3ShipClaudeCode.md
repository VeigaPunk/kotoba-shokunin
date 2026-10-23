Result: MIXED — The tip omits five documented component types; every named addition and cited range in the candidate holds, but the row can more precisely expose settings limits, inline command bodies, root-skill discovery, and MCP-bound message channels.

# Scope and axes

Read-only review of the Claude Code ship cells at lane tip `07c33d73ddce769d9cea2846a6313164401b5478`, plus the proposed replacements at `.ufo/waves/round-57/a3/a2-candidate.patch:15,97`. The patch is a claim under review, not evidence. No earlier-attempt scratch was used.

Primary impacted axis: depth (which plugin surfaces to inspect and where their instructions can reside). Evidence/provenance precision is also affected. This is advisory criticism, not a canonical judgment, admission, or measurement of C1. No counter, runtime, client, or lane code was executed; no lane content was changed except this report.

# Independently opened source

S079 URL: https://code.claude.com/docs/en/plugins-reference.md

Fetched bytes: `/fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md`. All external line references below address these unmodified fetched bytes. No Markdown bytes were stripped or line breaks folded in the short quotations below; quotes are contiguous substrings of the indicated line.

Sandbox creation, exit 0, no output:

```sh
timeout 90 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode && timeout 30 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Fetch/receipt command, exit 0:

```sh
timeout 5 date -u && timeout 90 curl --location --silent --show-error --max-time 75 --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md --write-out 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nsize_download=%{size_download}\n' https://code.claude.com/docs/en/plugins-reference.md && timeout 5 sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md && timeout 5 wc -c /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md
```

Observed output:

```text
Fri 23 Oct 2026 06:46:00 AM UTC
url_effective=https://code.claude.com/docs/en/plugins-reference.md
http_code=200
size_download=42124
f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e  /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md
42124 /fast/scratch/hyaku/kotoba-r57a3/A3ShipClaudeCode/plugins-reference.md
```

The byte count and full digest match the committed S079 receipt at `corpus/SOURCES.md:92`. This is a fresh fetch, not reliance on that receipt.

# Findings and strongest counterexamples

## 1. Tip inventory is incomplete; the candidate's additions are real

Affected tip locations: `SKILL.md:117`; `corpus/knowledge/plugin-manifests-round57.md:42`.

The source's standard-layout table lists workflows at line 625, themes at 626, monitors at 627, executables at 628, and settings at 629. Neither tip cell lists these five component types. This is fixable depth loss, not a reason to alter a frozen counter or change the client census.

Every component named by either the tip or candidate is actually named in S079. The candidate does not fabricate any of its five additions. Its root-`CLAUDE.md` warning is also supported at line 665. The candidate's cited range `30,34,611-629,665` holds its actual text; the tip's `34-36,611-629` also holds its narrower claims. There is no wrong-line citation in these Claude ship rows.

## 2. Bound “settings” to the only settings the page says take effect

Source line 216 says: “Only `agent` and `subagentStatusLine` take effect; other keys are dropped at load.” Line 629 names the same two defaults. The candidate's bare word `settings` is a true component label, but should not be read as arbitrary plugin-supplied settings being applied. The proposed cell below names the two defaults instead. This is a scope clarification, not evidence that the candidate invented a settings component.

## 3. The source exposes instruction-discovery paths beyond named directories

- Source line 243 describes inline command `content` as “Inline Markdown for the command body, instead of `source`”. Lines 236-255 establish that a plugin can declare that body in the manifest instead of shipping a command file. An auditor who searches only `commands/` can miss those instructions. Both existing inventories say commands, so this is a missing discovery detail, not a wholly missing component category.
- Source line 618 says: “A plugin with `SKILL.md` at its root, no `skills/`, and no `skills` key loads as a single skill”. This useful instruction-bearing location is absent from both ship cells. The replacement records that sufficient discovery condition without claiming it is the only way to load a root skill: line 148 also permits `skills` to name the plugin root.
- Source lines 147 and 514-520 document `channels`, bound to a plugin MCP server. Line 514 says: “`channels` declares the message channels a plugin provides, such as a bridge to a chat app.” That same line links to how the server injects messages. Neither cell mentions channel declarations, and neither existing ship-row citation covers them. [INFERENCE] This is a useful additional message-entry surface for an instruction-surface audit. It must remain described as MCP-bound, not invented as an independent always-on instruction-file authority.

## 4. Do not turn component inventory into an always-on-context guarantee

Themes, executables, server configuration, and settings are documented ship components; their inclusion does not establish that their file contents are all loaded as instructions. In particular, line 665 explicitly says a root `CLAUDE.md` is not loaded as context. The candidate correctly adds that distinction.

The page also names `userConfig`, mod type declarations, and eval cases at lines 145-146 and 159. I have not silently treated those as absent from the page. Those lines alone do not establish a separate always-on instruction-file loading surface, so the replacement below does not recast them as one. Monitors' interactive/provider restrictions are at line 158; a “can ship” inventory should not be interpreted as a promise that every component runs in every host or session.

# Part-by-part line evidence for the proposed cells

All references are S079 `plugins-reference.md` from the fresh fetch above.

| Proposed part | Lines | What the fetched page establishes |
|---|---|---|
| skills; root single-skill discovery condition | 148, 618 | Skill directories/root path support; automatic single-root-skill layout when both the directory and manifest key are absent |
| Markdown commands, file or inline bodies | 149, 236-243, 619 | Command files/directories or a manifest object map; `content` is inline Markdown |
| agents | 150, 620 | Agent Markdown files and their default directory |
| hooks | 151, 621 | Hook files/inline config and default hook configuration path |
| MCP server configurations | 152, 622 | MCP configuration/bundles/inline entries and default `.mcp.json` |
| LSP server configurations | 153, 623 | LSP configuration files/inline maps and default `.lsp.json` |
| MCP-bound message channels | 147, 514-520 | Plugin channels bind to one of its MCP servers; not a distinct always-on instruction file |
| output styles | 154, 624 | Output-style files/directories; standard layout specifies Markdown files |
| workflow `.js` files / JavaScript workflows | 155, 625 | Workflow `.js` files or directories |
| themes | 156-157, 626 | Theme files/directories; standard layout specifies JSON; manifest field is under `experimental` |
| monitors | 156, 158, 363, 627 | Monitor file/inline array and default path; availability restrictions are documented at 158 |
| `bin/` executables | 628 | Files placed on the Bash tool's PATH while the plugin is enabled; host-install limitations are on the same line |
| `agent` / `subagentStatusLine` defaults | 144, 216, 629 | Only these plugin settings take effect; root `settings.json` takes precedence over the manifest key |
| optional manifest; files under root, not inside `.claude-plugin/` | 30, 34, 617 | Optional manifest and separation of the metadata directory from component files/subdirectories |
| root `CLAUDE.md` not loaded; validator warning; instructions in a skill | 665 | All three statements are explicitly on this line; this is documentation evidence, not an executed validator test |

# Exact old → new text to land

My recommendation is an own replacement, retaining the candidate's supported additions while narrowing settings and making the additional discovery paths explicit. These are proposed edits only; the L1 integrates.

## `SKILL.md` — “What a plugin can ship” cell only

Old tip cell (`SKILL.md:117`):

```text
skills, commands, agents, hooks, MCP and LSP server configs, output styles
```

Old candidate cell (`a2-candidate.patch:15`):

```text
skills, commands, agents, hooks, MCP and LSP server configs, output styles, workflows, themes, monitors, executables, settings; a plugin-root `CLAUDE.md` is not loaded as context (ship instructions as a skill)
```

Replace either old cell →

```text
skills (a root `SKILL.md` loads as a single skill when `skills/` and the `skills` key are both absent), commands (files or inline Markdown), agents, hooks, MCP and LSP server configs, MCP-bound message channels, output styles, JavaScript workflows, themes, monitors, `bin/` executables, and `agent`/`subagentStatusLine` defaults; a plugin-root `CLAUDE.md` is not loaded as context (put context instructions in a skill)
```

No change is proposed to the manifest token, client identity, or Action cell.

## `corpus/knowledge/plugin-manifests-round57.md` — ship cell

Old tip cell (`:42`):

```text
skills, Markdown commands and agents, hooks, MCP and LSP server configurations, output styles; the manifest is optional and every other file sits at the plugin root, not inside `.claude-plugin/`
```

Old candidate cell (`a2-candidate.patch:97`):

```text
skills, Markdown commands and agents, hooks, MCP and LSP server configurations, output styles, workflows, themes, monitors, executables, settings; the manifest is optional and every other file sits under the plugin root, not inside `.claude-plugin/`; a `CLAUDE.md` at the plugin root is not loaded as context (`claude plugin validate` warns on it), so instructions that must load go in a skill
```

Replace either old cell →

```text
skills (a root `SKILL.md` loads as a single skill when `skills/` and the `skills` key are both absent), Markdown commands (files or inline bodies) and agents, hooks, MCP and LSP server configurations, MCP-bound message channels, output styles, workflow `.js` files, themes, monitors, `bin/` executables, and `agent`/`subagentStatusLine` defaults; the manifest is optional and other plugin files sit under the plugin root, not inside `.claude-plugin/`; a plugin-root `CLAUDE.md` is not loaded as context (`claude plugin validate` warns), so context instructions go in a skill
```

Matching Source lines cell, exact old → new:

Old tip:

```text
S079 `plugins-reference.md:34-36,611-629`
```

Old candidate:

```text
S079 `plugins-reference.md:30,34,611-629,665`
```

Replace either old citation →

```text
S079 `plugins-reference.md:30,34,147-150,216,236-243,514-520,617-629,665`
```

# Bounds and verification record

The exercised verification was the ordinary curl fetch plus byte count/digest and read-only comparison of the specified cells against fetched source lines. No C1 rerun, client invocation, validator run, build, test, or canonical judgment was performed or claimed. No installs or upgrades were needed. The frozen counter and all lane files other than this report remain untouched by this seat.
