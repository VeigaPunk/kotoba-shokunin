Result: HOLDS — the Claude Code row and its entry note use actual lifecycle events, and their configuration, action and line-reference claims are supported by S096.

## Scope and axes

Seat: `KotobaR59.CellsClaudeCode`. Attacked revision: `c63ccc6823e1f6a8577acbb43d19551eadbbee9a`.

Attacked material: `SKILL.md:127`; `corpus/knowledge/hook-files-round59.md:23,32-35`. This is the pre-registered semantic review in `plans/round-59.md:93-98`, not a judgment of C1 or of the round. The frozen counter and targets are unchanged: `verifiers/check_hook_files.py:253-254` reads `TARGET = 4`, `NEW_TARGET = 5`.

Impacted axis: **depth**, specifically whether the routing table contains actionable, correctly sourced technical detail. **Calibration** bounds the conclusion: these are documentation claims, not observed hook execution or an unconditional enforcement guarantee. No axis trade or required correction was established within this seat's scope.

## Opened evidence and provenance

Opened the committed S096 snapshot through the read tool, including lines 17-65, 237-245, 900-939, 1223-1229, 1718-1732 and 4140-4153. Page: https://code.claude.com/docs/en/hooks.md . All page line numbers below refer to `.ufo/waves/round-59/snapshots/S096.page`.

The existing snapshot, rather than a new network response, is the evidence reviewed. Original fetch metadata is attributed to `corpus/SOURCES.md:108` and `.ufo/waves/round-59/build/SrcClaudeCode.md:7-12`: HTTP 200, 274129 bytes, SHA-256 `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8`. The producer's recorded `date -u` line is `Fri 23 Oct 2026 09:34:52 AM UTC`; that is not a fetch performed by this seat.

My local access/hash command, run from the lane repo:

```sh
timeout 30s date -u && timeout 30s sha256sum .ufo/waves/round-59/snapshots/S096.page && timeout 30s wc -c .ufo/waves/round-59/snapshots/S096.page
```

Exit 0; observed output:

```text
Fri 23 Oct 2026 09:53:29 AM UTC
c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  .ufo/waves/round-59/snapshots/S096.page
274129 .ufo/waves/round-59/snapshots/S096.page
```

Pinned-object check:

```sh
timeout 30s git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:.ufo/waves/round-59/snapshots/S096.page | sha256sum
```

Exit 0; observed `c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8  -`. Thus the opened local snapshot matches the attacked revision's snapshot and the SOURCES digest.

Also read the attacked committed table and entry using these read-only commands (each exit 0):

```sh
timeout 30s git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:SKILL.md
timeout 30s git --no-optional-locks show c63ccc6823e1f6a8577acbb43d19551eadbbee9a:corpus/knowledge/hook-files-round59.md
```

Their Claude Code row and note match the file lines cited in this report. The first command's displayed output elided unrelated material; the attacked section was displayed.

All vendor quotations below retain the source Markdown bytes and are at most 25 words apiece. Short quotations are contiguous source substrings; no source Markdown was stripped.

## Every backticked span in the Events cell

`SKILL.md:127` contains exactly the following two Events spans; neither is merely an incidental identifier elsewhere on the page.

| Span | Ruling | Exact page text and location |
|---|---|---|
| `PreToolUse` | **event** | S096:37, in the table headed `Event`: “Before a tool call executes. Can block it” |
| `SessionStart` | **event** | S096:33, in that same table: “When a session begins or resumes” |

These are also event-section headings, `### PreToolUse` at S096:1718 and `### SessionStart` at S096:1223. S096:1720 explicitly says “Runs after Claude creates tool parameters and before processing the tool call.” S096:1225 says “Runs when Claude Code starts a new session or resumes an existing session.” Their use in the row is lifecycle-event use, not substring presence alone.

No span is ruled `not an event`; the addendum's mandatory correction trigger is not reached for this row.

## Hook config cell: every claim and reference

`SKILL.md:127` claims project `.claude/settings.json`, with user and local settings files also available, citing S096:243-245. **Supported**, with no line drift:

S096:243:

```text
| `~/.claude/settings.json` | All your projects | No, local to your machine |
```

S096:244:

```text
| `.claude/settings.json` | Single project | Yes, can be committed to the repo |
```

S096:245:

```text
| `.claude/settings.local.json` | Single project | No, gitignored when Claude Code saves a setting to it |
```

These rows occur under `### Hook locations` (S096:237), introduced at S096:239 by “Where you define a hook determines its scope:”. They therefore support hook configuration locations, not merely unrelated settings paths. The row does not claim these are the only locations, that the user file travels to cloud sessions, or a scope-precedence rule.

## Action cell: every claim and reference

1. **Move a before-tool check into a hook here — supported as routing advice.** S096:37 supplies the before-execution timing, S096:244 supplies the project location, and S096:910 gives the concrete combination:

   ```text
   This `PreToolUse` hook in `.claude/settings.json` runs a project script before each Bash command, and blocks the command if the script fails:
   ```

   The adjacent configuration at S096:914-923 uses `PreToolUse`, matcher `Bash`, a command handler and `"onFailure": "block"`. The row supplies routing advice, not a fabricated hook implementation or a claim to have run one. Its final S096:4146 citation supports the security clauses below; before-tool timing is supported by the Events cell's S096:37 citation, not by 4146 alone.

2. **Review and test each command before adding it — supported.** Exact substring at S096:4146:

   ```text
   Review and test all hook commands before adding them to your configuration.
   ```

3. **The command runs with the user's permissions — supported.** Exact substring at S096:4146:

   ```text
   Command hooks execute shell commands with your full user permissions.
   ```

The Action cell speaks about commands; it does not falsely attribute shell permissions to every possible handler type. The parenthetical S096:4146 points to the actual warning, not to an unrelated security section.

## Entry row and per-client note

- `corpus/knowledge/hook-files-round59.md:23`: the source is S096 and the quoted project/Bash-hook sentence is the unchanged complete sentence at S096:910, reproduced above. **Supported.** Its fail-blocking wording is about that example, whose configuration explicitly sets `onFailure` to `block`; it is not a claim that every hook failure blocks.
- Entry lines 32-33: project `.claude/settings.json`, user `~/.claude/settings.json`, local `.claude/settings.local.json`; parenthetical `hooks.md:243-245`. **Supported**, by the three exact rows above.
- Entry lines 33-34: `SessionStart` (`:33`) and `PreToolUse` (`:37`). **Supported**, both ruled **event** above, with the cited line numbers correct.
- Entry line 34: `PostToolUse` (`:40`). **Supported; event.** Exact description at S096:40: “After a tool call succeeds”.
- Entry line 34: `SessionEnd` (`:65`). **Supported; event.** Exact description at S096:65: “When a session terminates”. S096:23 independently groups `SessionStart` and `SessionEnd` as per-session events.
- Entry lines 34-35: command hooks have the user's full permissions; review and test every hook command before adding it; parenthetical `:4146`. **Supported**, by the two exact security substrings above.

Every parenthetical source-line reference in the attacked Claude Code row and note resolves to the asserted material. No unsupported or overstated field claim was found on the routing-advice reading the text actually states.

## Strongest local counterexample tested

Candidate attack: read “a check that must run before a tool call” as a guarantee that a project `PreToolUse` hook runs before **every** tool call, irrespective of event support, matching or policy. That stronger proposition is false on this same page.

- S096:25 explicitly includes this exception:

  ```text
  `PreToolUse` and `PostToolUse`, except [`EndConversation`](/docs/en/tools-reference#endconversation-tool-behavior) calls, which skip both
  ```

- S096:1720 also says “Matches on any tool name except `EndConversation`:”.
- S096:19 conditions dispatch: “When an event fires and a matcher matches,”.
- S096:257 introduces managed `allowManagedHooksOnly`; S096:259 then states:

  ```text
  Your user, project, local, and plugin hooks are blocked.
  ```

- S096:904 says “On most events, when a hook fails or times out, Claude Code still carries out the action.” The source example's explicit fail-closed configuration matters.

**Disposition:** this defeats an unconditional enforcement claim, not the scoped row's location/event/security facts or its recommendation to route a before-tool check here. The Action cell says “a tool call”, not “every tool call”; the entry explicitly disclaims runtime behaviour at lines 66-69. Omitting an exhaustive hook implementation is consistent with the stated province boundary. Do not promote this review into evidence for universal execution or blocking.

## Smallest safe correction and handoff

**Required correction: none for the attacked row and note.** Optional precision, if the L1 wants to preclude the stronger reading: replace the first Action clause with “Route a check before a matched tool call to a `PreToolUse` hook here”, and cite S096:19,37,1720. That changes no event name, source token, counter, rule or target. It remains routing guidance, not an implementation.

This seat wrote only this report. No lane Git/jj writes, sandbox commits, lane-code execution, counter rerun/mutation, hook execution, live fetch, paid model calls, additional runtime invocation, or tool installation/update occurred. The milestone's other seats own counter and whole-round checks; none are claimed here. No lane-wide no-harm result is inferred from this narrow semantic review.

Report: `.ufo/waves/round-59/falsify/CellsClaudeCode.md`
