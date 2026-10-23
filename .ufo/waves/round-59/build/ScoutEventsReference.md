Result: DONE — Six eligible clients; each census page prints at least two real hook events, and the before-tool / session-start pair is on that same page except Gemini's quote page, which has no session-start name.

Seat ScoutEventsReference. No tools installed. No lane file edited except this report. No new fetch: line numbers are from the census scratch bytes, and each sha256 below equals the census report for that file. Identifier check: case-sensitive, neighbours outside `[A-Za-z0-9_]` (the counter's `event_on_page` / `EVENT_WORD` rule), run on those bytes after `Fri 23 Oct 2026 09:34:20 AM UTC`.

Opencode is not in the tables. Censusopencode: not eligible.

How to read the marks. **Before tool = yes** only when that page's own sentence says the event fires before a tool executes. **Session start = yes** only when that page says the event fires because a session begins, resumes, or is created. A name can be a real hook event and still be **no** on both marks. The counter only checks that the backticked spelling occurs as its own identifier on the snapshot page; it does not check these marks (plan round-59, falsify route: a printed identifier can be `GitHub` or `JavaScript`).

Events-cell constraint: both names have to be on the snapshot of the row's URL. A name that exists only on a second page fails that row.

## Safe pair on the census page

| Client | Census page (snapshot this if it is the row URL) | Before a tool runs | At session start | Do not put in that snapshot |
|---|---|---|---|---|
| Claude Code | `code.claude.com/docs/en/hooks.md` | `PreToolUse` line 37 | `SessionStart` line 33 | camelCase `preToolUse` / `sessionStart` (not on this page) |
| Codex | `learn.chatgpt.com/docs/hooks.md` | `PreToolUse` lines 449, 949 | `SessionStart` line 27 | `SubagentStart` is not session start (same table cell, different event) |
| VS Code | `code.visualstudio.com/docs/agent-customization/hooks.md` | `preToolUse` line 130 is the tool-call event; this page does not say "before" | `sessionStart` line 128 | `SessionStart` is absent. `Read` / `Write` / `Edit` on line 139 are tool names, not events |
| Copilot CLI | `docs.github.com/.../concepts/customizations/hooks.md` | `preToolUse` line 37 | `sessionStart` line 34 | `preCompact`, `subagentStart`, `permissionRequest`, `notification`, `postToolUseFailure`, `userPromptTransformed`, and every PascalCase alias: on the reference, not on this page |
| Gemini CLI | quote page `geminicli.com/docs/hooks/best-practices.md` | `BeforeTool` is on the page; the "before a tool executes" sentence is **not** | none. `SessionStart` is absent | `SessionStart` is on `docs/hooks.md` line 40 and the reference, not on the quote page |
| Cursor | markdown body of `cursor.com/docs/hooks` (the `.md` URL 404'd for the counter) | `preToolUse` line 862 | `sessionStart` line 1340 (desktop). Line 88: cloud agents do not fire it at true session start | `stop` is a real event and also an ordinary English word |

## Claude Code

Page: https://code.claude.com/docs/en/hooks.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusClaudeCode/hooks.md`

sha256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`, 274129 bytes, 4219 lines. CensusClaudeCode fetch `Fri 23 Oct 2026 09:02:19 AM UTC`, HTTP 200. Same bytes as control S096.

The summary table is lines 31-65. Each name is backticked in the Event cell. The same 33 names are `###` headings under `## Hook events` (line 1219). "When" below is the table cell, shortened only where the cell runs long; the line is the table row.

| Event | Line | When the page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `SessionStart` | 33 | When a session begins or resumes | no | yes |
| `Setup` | 34 | `--init-only`, or `--init` / `--maintenance` in `-p`. Line 1385: does not fire on normal startup | no | no |
| `UserPromptSubmit` | 35 | When a prompt is submitted, before Claude processes it | no | no |
| `UserPromptExpansion` | 36 | When a user-typed command expands into a prompt, before it reaches Claude | no | no |
| `PreToolUse` | 37 | Before a tool call executes. Can block it | yes | no |
| `PermissionRequest` | 38 | When a tool call needs a permission decision | no | no |
| `PermissionDenied` | 39 | When auto mode denies a tool call | no | no |
| `PostToolUse` | 40 | After a tool call succeeds | no | no |
| `PostToolUseFailure` | 41 | After a tool call fails | no | no |
| `PostToolBatch` | 42 | After a batch of parallel tool calls resolves, before the next model call | no | no |
| `Notification` | 43 | When Claude Code sends a notification | no | no |
| `MessageDisplay` | 44 | While assistant message text is displayed | no | no |
| `SubagentStart` | 45 | When a subagent is spawned | no | no |
| `SubagentStop` | 46 | When a subagent finishes | no | no |
| `TaskCreated` | 47 | When a task is being created via `TaskCreate` | no | no |
| `TaskCompleted` | 48 | When a task is being marked as completed | no | no |
| `Stop` | 49 | When Claude finishes responding | no | no |
| `StopFailure` | 50 | When the turn ends due to an API error | no | no |
| `TeammateIdle` | 51 | When an agent-team teammate is about to go idle | no | no |
| `InstructionsLoaded` | 52 | When a CLAUDE.md or rules file is loaded. The cell also says it fires at session start and on later lazy loads. Line 1424: session start for eager files, again later for lazy files | no | also, not the session-start event |
| `ConfigChange` | 53 | When a configuration file changes during a session | no | no |
| `CwdChanged` | 54 | When the working directory changes | no | no |
| `DirectoryAdded` | 55 | When a working directory is added mid-session | no | no |
| `FileChanged` | 56 | When a watched file changes on disk | no | no |
| `WorktreeCreate` | 57 | When a worktree is being created | no | no |
| `WorktreeRemove` | 58 | When a worktree a `WorktreeCreate` hook created is being removed | no | no |
| `PreCompact` | 59 | Before context compaction | no | no |
| `PostCompact` | 60 | After context compaction completes | no | no |
| `PreModelSwitch` | 61 | Before Claude Code applies a model switch | no | no |
| `PostModelSwitch` | 62 | After the session's model changes | no | no |
| `Elicitation` | 63 | When an MCP server requests user input during a tool call | no | no |
| `ElicitationResult` | 64 | After a user responds to an MCP elicitation | no | no |
| `SessionEnd` | 65 | When a session terminates | no | no |

Cadence, lines 23-25: per session `SessionStart` and `SessionEnd`; per turn `UserPromptSubmit`, `Stop`, `StopFailure`; on every tool call `PreToolUse` and `PostToolUse` (except `EndConversation`). `PermissionRequest` is a permission decision, not the before-execution event. `Stop` is its own identifier; `StopFailure` does not count as `Stop` (the next character is a word character).

## Codex

Page: https://learn.chatgpt.com/docs/hooks.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusCodex/learn.chatgpt.com_docs_hooks.md.body`

sha256 `57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92`, 47133 bytes, 1131 lines. CensusCodex fetch `Fri 23 Oct 2026 09:03:06 AM UTC`, HTTP 200. Same bytes via the `developers.openai.com/codex/hooks.md` redirect. Same bytes as control S097.

Twelve names. The summary table is lines 23-28. Each name is also a `###` heading under `## Hooks` (line 646).

| Event | Summary line | Section line | When the page says it fires | Before tool | Session start |
|---|---|---|---|---|---|
| `PreToolUse` | 25 | 751 | Summary cell is only "During a turn". Line 449: block or rewrite the call. Lines 949 and 955 (code mode): stop the tool before it runs; the promise rejects before the tool runs | yes | no |
| `PermissionRequest` | 25 | 833 | Line 835: when Codex is about to ask for approval. Line 838: does not run for commands that do not need approval | no | no |
| `PostToolUse` | 25 | 893 | Line 895: after supported tools produce output | no | no |
| `PreCompact` | 25 | 960 | Line 962: before Codex compacts the chat | no | no |
| `PostCompact` | 25 | 978 | Line 980: after Codex compacts the chat | no | no |
| `UserPromptSubmit` | 25 | 996 | Summary: during a turn. Line 1005: field `prompt` is the user prompt about to be sent. No before-tool sentence | no | no |
| `SubagentStop` | 25 | 1034 | Summary: during a turn. Section gives matcher and fields, not a before-tool or session-start sentence | no | no |
| `Stop` | 25 | 1068 | Summary: during a turn. Section gives fields (`stop_hook_active`), not a before-tool sentence | no | no |
| `Interrupt` | 26 | 1102 | Line 26 and line 1104: when you interrupt an active turn. Not for subagents | no | no |
| `SessionStart` | 27 | 648 | Line 27: when a session or subagent starts (this name is the session one). Line 656: `source` is how the session started (`startup`, `resume`, `clear`, `compact`, `fork`) | no | yes |
| `SubagentStart` | 27 | 721 | Same summary cell as `SessionStart`, but it is the subagent start. Section only says the matcher is `agent_type` | no | no |
| `SessionEnd` | 28 | 684 | Line 28: when the main thread ends. Line 686: when a session ends. Does not run for subagents | no | no |

## VS Code

Census page: https://code.visualstudio.com/docs/agent-customization/hooks.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusVSCode/hooks.md`

sha256 `98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08`, 15152 bytes, 214 lines. CensusVSCode fetch `Fri 23 Oct 2026 09:02:50 AM UTC`, HTTP 200. Same bytes as control S098.

This page's own event table is lines 126-135, column heading "Copilot event". It says the full list and timing are on the GitHub Copilot reference (line 137). That reference is not this page.

| Event | Line | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `sessionStart` | 128 | Add context when a session starts or resumes | no | yes |
| `userPromptSubmitted` | 129 | Observe a submitted prompt. Line 137: command-hook output is ignored for this event | no | no |
| `preToolUse` | 130 | Inspect or make a decision about a tool call. Also a JSON key on line 83. This page does not say "before" | no on this page | no |
| `postToolUse` | 131 | Validate a successful result or add context. Line 152: cannot undo an action that already completed | no | no |
| `preCompact` | 132 | Save information before compaction | no | no |
| `subagentStart` | 133 | Observe a subagent starting (same cell as the next name) | no | no |
| `subagentStop` | 133 | Observe a subagent finishing | no | no |
| `agentStop` | 134 | Check whether the agent should finish its turn | no | no |
| `sessionEnd` | 135 | Clean up when the session terminates | no | no |
| `PreToolUse` | 139 | Compatible alias of `preToolUse`. Receives snake_case fields. Real alias, different spelling | no on this page | no |

Also on this page, Local harness only (line 183): a scoped `Stop` hook is treated as `SubagentStop` when the agent runs as a subagent. `Stop` and `SubagentStop` are real Local event names here. They are not in the Copilot table above.

Not events, same line 139: `Read`, `Write`, `Edit` are Claude-style tool names.

Absent from this page (scan returned no identifier hit): `SessionStart`, `UserPromptSubmit`, `PostToolUse`, `SessionEnd`, `PreCompact`, `SubagentStart`, `errorOccurred`, `notification`, `permissionRequest`, `postToolUseFailure`, `userPromptTransformed`. An Events cell that uses those spellings fails a snapshot of this page.

The "before a tool" sentence for the Copilot spelling is on the page this one links, GitHub hooks-reference.md line 277: `preToolUse` fires before each tool executes. That file is the Copilot reference below (sha256 `7ad7c168…`), not a VS Code snapshot.

### VS Code Local reference (second page, not the census quote page)

https://code.visualstudio.com/docs/agents/reference/hooks-reference.md — title "Legacy Local hooks reference".

File: `/fast/scratch/hyaku/kotoba-r59/CensusVSCode/hooks-reference.md`

sha256 `5024a8e5f991a08b341079ee97c538cb15eddf7247e845a1478734ac5e115e7c`, 14412 bytes, 415 lines. Fetched by CensusVSCode; not the lead quote page. camelCase `sessionStart` and `preToolUse` are absent here.

| Event | Line | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `PreToolUse` | 117 | Fires before the agent invokes a tool | yes | no |
| `PostToolUse` | 172 | Fires after a tool completes successfully | no | no |
| `UserPromptSubmit` | 218 | Fires when the user submits a prompt | no | no |
| `SessionStart` | 238 | Fires when the first prompt starts the session | no | yes |
| `Stop` | 274 | Fires when the current agent execution is about to stop. Line 274: does not mean the session ended | no | no |
| `SubagentStart` | 317 | Fires when the agent starts a subagent | no | no |
| `SubagentStop` | 355 | Fires when a subagent is about to stop | no | no |
| `PreCompact` | 393 | Fires before the harness compacts conversation context | no | no |

## Copilot CLI

Census page (the concepts page, control S099): https://docs.github.com/en/copilot/concepts/customizations/hooks.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusCopilotCLI/concepts-hooks.md`

sha256 `23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4`, 8428 bytes, 166 lines. CensusCopilotCLI fetch `Fri 23 Oct 2026 09:02:56 AM UTC`, HTTP 200.

Line 32: these are examples of Copilot CLI hook events. Eight names. Line 43 points at the reference for the full set. PascalCase aliases are not on this page.

| Event | Line | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `sessionStart` | 34 | When a new agent session begins or when resuming an existing session | no | yes |
| `sessionEnd` | 35 | When the agent session completes or is terminated | no | no |
| `userPromptSubmitted` | 36 | When the user submits a prompt | no | no |
| `preToolUse` | 37 | Before the agent uses any tool (`bash`, `edit`, `view`). Can approve or deny | yes | no |
| `postToolUse` | 38 | After a tool completes (success or failure) | no | no |
| `agentStop` | 39 | When the main agent has finished responding | no | no |
| `subagentStop` | 40 | When a subagent completes, before returning results to the parent | no | no |
| `errorOccurred` | 41 | When an error occurs during agent execution | no | no |

### Copilot reference (full list; not the census quote page)

https://docs.github.com/en/copilot/reference/hooks-reference.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusCopilotCLI/hooks-reference.md`

sha256 `7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97`, 72175 bytes, 927 lines. Same fetch batch, HTTP 200. Line 266: the table lists every supported event.

| Event | Line | When this page says it fires | Before tool | Session start | Also printed as |
|---|---|---|---|---|---|
| `agentStop` | 270 | The main agent finishes a turn | no | no | heading `agentStop` / `Stop` line 553 |
| `errorOccurred` | 271 | An error occurs during execution | no | no | `ErrorOccurred` line 654 |
| `notification` | 272 | When the CLI emits a system notification. Not on the concepts page | no | no | — |
| `permissionRequest` | 273 | Before the permission service runs. Not on the concepts page | no (permission service, not tool execution) | no | — |
| `postToolUse` | 274 | After each tool completes successfully | no | no | `PostToolUse` line 489 |
| `postToolUseFailure` | 275 | After a tool completes with a failure. Not on the concepts page | no | no | `PostToolUseFailure` line 524 |
| `preCompact` | 276 | Context compaction is about to begin. Not on the concepts page | no | no | `PreCompact` line 691 |
| `preToolUse` | 277 | Before each tool executes | yes | no | `PreToolUse` line 433 |
| `sessionEnd` | 278 | The session terminates | no | no | `SessionEnd` line 339 |
| `sessionStart` | 279 | A new or resumed session begins | no | yes | `SessionStart` line 300 |
| `subagentStart` | 280 | A subagent is spawned (before it runs). Not on the concepts page | no (before a subagent, not before a tool) | no | — |
| `subagentStop` | 281 | A subagent completes | no | no | `SubagentStop` line 615 |
| `userPromptSubmitted` | 282 | The user submits a prompt | no | no | `UserPromptSubmit` line 367 |
| `userPromptTransformed` | 283 | After the runtime transforms a submitted prompt. Not on the concepts page | no | no | — |

`permissionRequest` line 273 says "before the permission service runs", not before the tool executes. The concepts page's before-tool event remains `preToolUse`.

## Gemini CLI

Two pages. The census quote, and the page control S100 snapshotted, is best-practices. The event catalog is `docs/hooks.md`. A snapshot of best-practices cannot carry `SessionStart`.

### Quote page (best-practices) — only three event names

https://geminicli.com/docs/hooks/best-practices.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks_best-practices.md.body`

sha256 `fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc`, 17650 bytes, 710 lines. CensusGeminiCLI fetch `Fri 23 Oct 2026 09:03:23 AM UTC`, HTTP 200. Same bytes as control S100.

Scan of the eleven catalog names: only `BeforeTool`, `AfterModel`, `AfterAgent` occur. `SessionStart`, `SessionEnd`, `BeforeAgent`, `BeforeModel`, `BeforeToolSelection`, `AfterTool`, `PreCompress`, `Notification` do not.

| Event | Lines | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `BeforeTool` | 31, 178, 202, 307, 615, 655 | Line 31: hooks that run frequently (like `BeforeTool` or `AfterModel`). Line 655: use `BeforeTool` hooks to prevent committing sensitive data. Line 178: sample field `hook_event_name` `BeforeTool`. This page never says "before a tool executes" | no on this page | no |
| `AfterModel` | 31, 76, 103 | Line 76: fires after every chunk of LLM output | no | no |
| `AfterAgent` | 74, 79, 228 | Line 74: fires once per turn after the model finishes its final response | no | no |

### Hooks page — the catalog (census cites it; not the quote page)

https://geminicli.com/docs/hooks.md

File: `/fast/scratch/hyaku/kotoba-r59/CensusGeminiCLI/geminicli.com_docs_hooks.md.body`

sha256 `a06a92438d3110690e875d61feef49a850d82eda618bb837146a1a7ff7a4c8d9`, 8341 bytes, 168 lines. Fetch `Fri 23 Oct 2026 09:02:48 AM UTC`, HTTP 200. Table lines 38-50. Each name once, backticked, except `BeforeTool` also at lines 86 and 107 and `AfterTool` also at line 86.

| Event | Line | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `SessionStart` | 40 | When a session begins (startup, resume, clear) | no | yes |
| `SessionEnd` | 41 | When a session ends (exit, clear) | no | no |
| `BeforeAgent` | 42 | After the user submits a prompt, before planning | no | no |
| `AfterAgent` | 43 | When the agent loop ends | no | no |
| `BeforeModel` | 44 | Before sending the request to the LLM | no | no |
| `AfterModel` | 45 | After receiving the LLM response | no | no |
| `BeforeToolSelection` | 46 | Before the LLM selects tools | no | no |
| `BeforeTool` | 47 | Before a tool executes | yes | no |
| `AfterTool` | 48 | After a tool executes | no | no |
| `PreCompress` | 49 | Before context compression | no | no |
| `Notification` | 50 | When a system notification occurs | no | no |

The reference repeats the same eleven names and the same two marks. https://geminicli.com/docs/hooks/reference.md — file `geminicli.com_docs_hooks_reference.md.body`, sha256 `06d37f2f66812ee78bb46c37a112203376f0bae4d3b8b44ac79d0bda4b86a118`, 13321 bytes, 330 lines.

| Event | Line | When this page says it fires | Before tool | Session start |
|---|---|---|---|---|
| `BeforeTool` | 94 | Fires before a tool is invoked | yes | no |
| `AfterTool` | 116 | Fires after a tool executes | no | no |
| `BeforeAgent` | 147 | After a user submits a prompt, before the agent begins planning | no | no |
| `AfterAgent` | 165 | Once per turn after the model generates its final response | no | no |
| `BeforeModel` | 189 | Before sending a request to the LLM | no | no |
| `BeforeToolSelection` | 206 | Before the LLM decides which tools to call | no | no |
| `AfterModel` | 223 | Immediately after an LLM response chunk is received | no | no |
| `SessionStart` | 247 | On application startup, resuming a session, or after `/clear` | no | yes |
| `SessionEnd` | 262 | When the CLI exits or a session is cleared | no | no |
| `Notification` | 274 | When the CLI emits a system alert | no | no |
| `PreCompress` | 289 | Before the CLI summarizes history | no | no |

If the Gemini row snapshots best-practices, the Events cell can be `BeforeTool` and `AfterAgent` (or `AfterModel`). Both are real hook events, and neither is a session-start event. Putting `SessionStart` in that cell fails the snapshot check. The before-tool sentence and the session-start sentence live on `hooks.md` lines 47 and 40.

## Cursor

Page the census saved: https://cursor.com/docs/hooks.md — sha256 `8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d`, 69145 bytes, 1507 lines.

File: `/fast/scratch/hyaku/kotoba-r59/CensusCursor/hooks.md`

CensusCursor fetch `Fri 23 Oct 2026 09:03:03 AM UTC`, HTTP 200. Control CtlFabEvents, `Fri 23 Oct 2026 09:21:27 AM UTC`: that `.md` URL returned HTTP 404 to the counter's curl header set (389 bytes). `https://cursor.com/docs/hooks` returned HTTP 200 and the same 69145 bytes, same sha256. Line numbers below are that markdown body. A row the counter will fetch should cite `https://cursor.com/docs/hooks`, not the `.md` URL.

Twenty-one names. Category list lines 24-44. Per-event headings start at line 860. `stop` is lowercase. It is a documented event at line 1316 and it also occurs as an ordinary English word, so a semantic seat has to use the heading, not a random "stop".

| Event | Heading line | Also listed | When the page says it fires | Before tool | Session start |
|---|---|---|---|---|---|
| `sessionStart` | 1338 | 26 | Line 1340: when a new composer conversation is created. Line 26: session lifecycle. Line 88: not run in cloud agents; a cloud firing would be after the first write, not at true session start | no | yes (desktop). Cloud: no |
| `sessionEnd` | 1372 | 26 | Line 1374: when a composer conversation ends. Line 89: cloud agents have no such boundary | no | no |
| `preToolUse` | 860 | 27, 66 | Line 862: before any tool execution, all tool types | yes | no |
| `postToolUse` | 897 | 27, 67 | Line 899: after successful tool execution | no | no |
| `postToolUseFailure` | 936 | 27, 68 | Line 938: when a tool fails, times out, or is denied | no | no |
| `subagentStart` | 970 | 28, 69 | Line 972: before spawning a subagent (Task tool) | no (before a subagent spawn) | no |
| `subagentStop` | 1010 | 28, 70 | Line 1012: when a subagent completes, errors, or is aborted | no | no |
| `beforeShellExecution` | 1058 | 29, 62 | Line 1060: before any shell command or MCP tool is executed (shared heading with the next name) | yes (shell or MCP) | no |
| `beforeMCPExecution` | 1058 | 30, 90 | Same sentence as `beforeShellExecution`. Line 90: not available in cloud agents | yes (shell or MCP) | no |
| `afterShellExecution` | 1102 | 29, 63 | Line 1104: after a shell command executes | no | no |
| `afterMCPExecution` | 1123 | 30, 90 | Line 1125: after an MCP tool executes. Not in cloud agents (line 90) | no | no |
| `beforeReadFile` | 1159 | 31, 64 | Line 1161: before the Agent reads a file | yes (file read) | no |
| `afterFileEdit` | 1147 | 31, 65 | Line 1149: after the Agent edits a file | no | no |
| `beforeSubmitPrompt` | 1255 | 32, 71 | Line 1257: right after the user hits send, before the backend request | no | no |
| `preCompact` | 1404 | 33, 72 | Line 1406: before context-window compaction | no | no |
| `stop` | 1316 | 34, 75 | Line 1318: when the agent loop ends | no | no |
| `afterAgentResponse` | 1283 | 35, 73 | Line 1285: after the agent has completed an assistant message | no | no |
| `afterAgentThought` | 1294 | 35, 74 | Line 1296: after the agent completes a thinking block | no | no |
| `beforeTabFileRead` | 1196 | 39, 91 | Line 1198: before Tab (inline completions) reads a file. Tab, not the agent tool hook. Not in cloud agents (line 91) | yes (Tab file read, not agent tool) | no |
| `afterTabFileEdit` | 1219 | 40, 91 | Line 1221: after Tab edits a file | no | no |
| `workspaceOpen` | 1442 | 44, 92 | Line 42: app lifecycle, outside any agent session. Line 1444: when Cursor opens a workspace and on every workspace-folder change | no | no |

The generic before-any-tool event is `preToolUse` (line 862). `beforeShellExecution`, `beforeMCPExecution`, and `beforeReadFile` are before one tool kind. `beforeTabFileRead` is Tab, not the agent. `workspaceOpen` is not session start.

## Case traps for the Events cell

Same words, different spellings, and the counter is case-sensitive.

| Spelling | On Claude / Codex hooks page | On VS Code census page | On Copilot concepts page | On Copilot reference | On Gemini hooks.md | On Gemini best-practices | On Cursor markdown |
|---|---|---|---|---|---|---|---|
| `PreToolUse` | yes | yes, alias, line 139 only | no | yes | no (`BeforeTool`) | no | no |
| `preToolUse` | no | yes | yes | yes | no | no | yes |
| `SessionStart` | yes | no | no | yes | yes | no | no |
| `sessionStart` | no | yes | yes | yes | no | no | yes |
| `BeforeTool` | no | no | no | no | yes | yes | no |

No tool was installed or upgraded.
