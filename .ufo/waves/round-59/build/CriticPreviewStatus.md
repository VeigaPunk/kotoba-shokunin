Result: DONE — VS Code's Action must retain Preview; the other five clients do not have a general hook-maturity warning on the inspected pages, but trust, execution-surface, and startup-loading qualifications defeat an unconditional always-on interpretation.

## Scope and impacted axes

Read-only critic review of feature status and loading defaults, not a C1 score or an admission judgment. Axes at risk: **depth** (actionable, correctly scoped technical detail), with **operability** and **calibration** affected if a documented file is mistaken for an already-running enforcement mechanism. No counter, rule, target, census population, or product file is changed or proposed for change.

Evidence is freshly fetched vendor documentation, not a client-binary experiment. All primary hook-page hashes match the W0/control page hashes. Paths below are relative to `/fast/scratch/hyaku/kotoba-r59/CriticPreviewStatus/` unless explicitly lane-relative. Line numbers address the fetched bytes; quotes are contiguous verbatim slices of at most 25 whitespace-separated words, with no Markdown bytes stripped. Surrounding prose is paraphrase, not a quotation.

Reviewed proposal: lane `.ufo/waves/round-59/build/ScribeSkillSection.md:11-16`; also `.ufo/waves/round-59/build/SrcCursor.md:70-74`. These are drafts, not assumed integrated SKILL content.

## Per-client status and Action requirements

| Eligible client / frozen lead token | Status evidence on cited hooks page or settings docs | What the Action must preserve |
|---|---|---|
| Claude Code / `.claude/settings.json` | No general Preview/experimental/beta label for command hooks. `Claude-hooks.page:392` describes command handlers; `:396,3990` marks **agent handlers** experimental. `:1777-1783` marks the Bash changed-files payload list public beta, not the hook file or all `PostToolUse` hooks. `Claude-reference.page:3474-3482,3503-3511` documents defaults that allow hooks rather than an opt-in feature flag. | A command-script Action does **not** need a blanket experimental or beta label. If it recommends `type: "agent"`, say experimental; if it relies on `tool_response.bashEditDiff` as an enforcement inventory, preserve the beta/best-effort restriction. Settings-file hooks wait for workspace trust in interactive sessions (`Claude-hooks.page:4150-4153`); do not describe that as a universal approval gate, because `-p`/SDK sessions treat the folder as trusted. |
| Codex / `~/.codex/hooks.json` | `Codex-hooks.page:314-323`: hooks enabled by default; `[features].hooks = false` turns them off. `Codex-config.page:491-495` documents the feature key, without an experimental label. The deprecated item is the `codex_hooks` **alias**, not hooks. | No experimental/Preview badge or enable-flag instruction is justified by those blocks. **Review and trust non-managed definitions in `/hooks` first**: new/changed definitions are skipped until trusted (`Codex-hooks.page:64-71`). A default-enabled feature is not a default-trusted hook. |
| VS Code / `.github/hooks/*.json` | **Preview**, explicitly in `VSCode-hooks.page:4,11`. `:11` also says individual provider implementations may have a different lifecycle status. | **Must say Preview.** Also identify the **Copilot session target** for this page's repository source and lower-camel-case events (`:16-28,42-43,59,126-135`). Do not infer that all provider hooks share the editor feature's maturity or schema. |
| Copilot CLI / `~/.copilot/hooks/*.json` | `Copilot-hooks.page:22-28` describes CLI support and personal hooks. The public-preview label at `:24` belongs to **VS Code**, not CLI. `Copilot-config.page:459` has `disableAllHooks` default `false`; the separate generic `experimental` flag at `:467` is not described as a requirement for hooks. | No CLI Preview/beta/experimental label or `--experimental` instruction is supported here. Preserve **personal CLI** scope. `Copilot-reference.page:23` makes the location conditional on `COPILOT_HOME`; `:28-30,90` restricts cloud-agent discovery to repository files, not these personal files. |
| Gemini CLI / `.gemini/settings.json` | No Preview/experimental/beta/alpha occurrence in `Gemini-hooks.page` under the explicit search below. `Gemini-config.page:2300-2307` makes `hooksConfig.enabled` the canonical toggle with default `true`; it is not under `experimental`. | No hooks-experimental badge or mandatory opt-in flag. Preserve the project/workspace security condition. Do **not** turn the best-practices page's “Untrusted by default” label (`Gemini-hooks.page:409`) into “not executed until per-hook approval”: its steps say warn, then execute unless blocked, then mark trusted (`:413-426`). Untrusted-workspace safe mode is a different, stronger gate; see below. |
| Cursor / `.cursor/hooks.json` | No Preview/experimental/beta/alpha occurrence in `Cursor-hooks.page` under the explicit search below. Project hooks automatically load in **trusted workspaces** (`:647-651,769-781`). | No general maturity badge. Preserve trusted-project scope for desktop/CLI and the **writable-environment** condition for cloud execution (`:50-54`). Do not imply every event printed on the page works in cloud agents (`:82-108`). |

### Exact short status quotes

- VS Code, `VSCode-hooks.page:11`: `The VS Code hooks experience is in Preview.` (8 words; the preceding blockquote marker is outside the slice.)
- Claude subtype only, `Claude-hooks.page:3990`: `Agent hooks are experimental.` (4 words; contiguous sentence from the warning.)
- Codex, `Codex-hooks.page:314`: `Hooks are enabled by default.` (5 words; first sentence only.)
- Codex trust, `Codex-hooks.page:67`: `changed hooks are marked for review and skipped until trusted.` (10 words; contiguous slice of line 67.)
- Gemini toggle, `Gemini-config.page:2302-2306`: the `hooksConfig.enabled` block names the canonical toggle and prints `- **Default:** `true`` on line 2306. This is an ordinary on-by-default toggle, not evidence of experimental status.

## Strongest counterexamples and smallest safe corrections

### 1. The proposed VS Code Action drops a status the source explicitly supplies

Proposal: lane `build/ScribeSkillSection.md:13` says only `Configure command hooks for agent events.` The actual source title and note both say Preview (`VSCode-hooks.page:4,11`). This is a **fixable depth/calibration omission**, not grounds to remove VS Code from the frozen eligible census. Preview is not an ineligibility conjunct.

Smallest correction to the Action: **`Preview: select Copilot and verify command hooks in a fresh session.`** Selecting the harness is documented at `:42-43`; the fresh-session diagnostic is at `:110`. Keep the frozen census token as assigned by the integrator; this review does not resolve the draft's separate audit-file versus glob mismatch.

### 2. A new Codex personal hook is discovered but does not run merely because hooks are enabled

A user creates a valid new `~/.codex/hooks.json` and follows only the draft Action `Run commands or MCP tools at lifecycle events.` (lane `build/ScribeSkillSection.md:12`). The source lists that file at `Codex-hooks.page:44`, yet `:64-67` explicitly skips new/changed non-managed definitions until review/trust. This is the strongest direct counterexample to equating an enabled feature and a documented file with active enforcement.

Smallest correction: **`Review and trust non-managed hooks in /hooks before using lifecycle checks.`** No dangerous bypass flag is needed or recommended. User-file discovery and trust-to-execute are separate facts. The project alternative also loads only with a trusted `.codex/` layer (`:58-60`; `Codex-config.page:1825-1828`), but that alternative is not the frozen user-level lead token.

### 3. Cursor's cloud-scoped source draft lists real events that its cloud scope cannot deliver

Lane `build/SrcCursor.md:73` pairs a project-cloud description and an always-on Action with `sessionStart` and `sessionEnd`. Both are real hook events, so a printed-identifier check cannot establish cloud availability. `Cursor-hooks.page:88-89` explicitly lists both as unavailable in cloud agents. `:54` says hooks do not run during initial read-only cloud turns and start once the environment is writable. `:98` does confirm the project file is a loaded cloud source.

Smallest correction: for a cloud-scoped row, use **`preToolUse`, `postToolUse`** (`:66-67`, with full event definitions at `:860-862,897-899`) and say **`Run project command hooks once the cloud environment is writable.`** Alternatively scope lifecycle events to the desktop/CLI instead of cloud. Do not delete the eligible token or claim the file is globally disabled.

Additional startup caveat only if claiming **every prompt**: `Cursor-hooks.page:814` says the desktop app waits only briefly for hooks by default and documents the Enterprise dashboard's **Block until hooks are ready** setting. Its contiguous clause `so they run on every prompt, including the first one after a restart.` is 13 words. An unqualified first-prompt guarantee is not supported by the default. This is not a Preview flag.

### 4. Gemini does name a census-token location that is not loaded in untrusted safe mode; its docs disagree on the trust feature's default

`Gemini-trust.page:74-79` says untrusted workspace safe mode ignores project settings, expressly naming `.gemini/settings.json`. Short exact quote, lines 77-78 (11 words; the list prefix is outside the slice, with the physical newline and indentation retained):

```text
The CLI will **not** load the
    `.gemini/settings.json` file from the project.
```

Do not flatten this into “hooks are off by default.” The current configuration reference says `security.folderTrust.enabled` defaults **true** (`Gemini-config.page:1983-1987`), while the dedicated trust guide says the **Trusted Folders feature** is disabled by default (`Gemini-trust.page:10-11`). This is a vendor-documentation contradiction about folder trust, not a measured runtime default or proof that hooks require an experimental flag. Separately, `hooksConfig.enabled` defaults true (`Gemini-config.page:2302-2307`). The best-practices page's untrusted **hook identity** sequence warns then executes unless blocked (`Gemini-hooks.page:413-426`); that is not the safe-mode file-loading rule.

Smallest safe correction: **`Define project hooks; untrusted-workspace safe mode ignores this file.`** In the knowledge note, cite both trust-default statements and leave their conflict explicit if discussing defaults. Do not silently choose one as runtime truth and do not recommend bypassing trust.

## Does a census token name a location not loaded by default?

**Not as an unconditional, all-surfaces statement about any of the six local lead locations.** The evidence instead establishes these important conditional exclusions; several match a census token literally:

1. **Gemini `.gemini/settings.json`: not loaded in untrusted-workspace safe mode**, explicitly `Gemini-trust.page:77-79`. Default folder-trust documentation conflicts as above; a universal default claim would overstate it.
2. **Claude `.claude/settings.json`: its hooks do not apply to cloud threads inside a project**, `Claude-settings.page:324`; Anthropic-hosted sessions spanning several repositories read only two plugin/marketplace keys from each repository file, not hooks (`:326`). A one-repository cloud session outside project threads reads the file (`:325`). Interactive sessions also hold all settings hooks pending workspace trust (`Claude-hooks.page:4152`), whereas `-p`/SDK sessions do not (`:4153`). No blanket local opt-in flag follows.
3. **Codex `~/.codex/hooks.json`: the file is a discovery source, but new/changed non-managed definitions are skipped until trusted**, `Codex-hooks.page:44,64-71`. Do not misreport this as “the file isn't loaded.” The untrusted-project file exclusion concerns `<repo>/.codex/hooks.json`, not the selected user lead (`:58-60`).
4. **Copilot CLI `~/.copilot/hooks/*.json`: normal user directory on macOS/Linux, redirected to `$COPILOT_HOME/hooks/` when that variable is set**, `Copilot-reference.page:23`. Personal files are not the cloud agent's discovery source (`:28-30,90`). This is a surface/environment distinction, not experimental CLI hooks.
5. **Cursor `.cursor/hooks.json`: auto-loaded in trusted workspaces, not an unconditional untrusted-workspace runner**, `Cursor-hooks.page:771,779-781`. Cloud read-only turns have no running hooks (`:54`), and desktop startup can outrun default loading (`:814`). The separate **user** `~/.cursor/hooks.json` is unavailable in cloud agents (`:102`). The frozen counter normalizes away `~/`, so that counted identity must not erase the user's versus project's different execution scopes.
6. **VS Code `.github/hooks/*.json`: this page names it for Copilot sessions**, `VSCode-hooks.page:18,42-43,59`. The legacy Local harness's `chat.useHooks`, `chat.useClaudeHooks`, and `chat.hookFilesLocations` must not be presented as the controls for the shared Copilot harness (`:69-71,180-185`). In particular, the documented opt-in condition `chat.useClaudeHooks` concerns importing Claude settings into **Local**, not a new flag required for the frozen VS Code repository token.

One cross-tool check to avoid a false flag claim: the linked Cursor third-party guide says loading Claude settings requires **Include Third-Party Plugins, Skills, and Other Configs**, but immediately says the setting is **on by default** (`Cursor-thirdparty-canonical.page:11`); it names `.claude/settings.json` at `:20`. That is not evidence that the Claude client itself requires a flag, nor a disabled-by-default Cursor import.

## Integration correction, not a counter redesign

The frozen counter intentionally checks only the Action word floor (`verifiers/check_hook_files.py:912-914`; docstring `:54-58`). It cannot certify Preview disclosure, trust admission, workspace mode, cloud event availability, or startup readiness. These findings belong in the Action cells and the sourced explanatory note; do not modify the frozen counter, rule, targets, or census to paper over them. I did not execute the counter or create a mutant, and claim no observed predicate result.

Minimal status action is mandatory only for **VS Code: Preview**. Claude's experimental/beta qualifications are conditional on the selected subtype/payload; broad badges for Codex, Copilot CLI, Gemini CLI, or Cursor would have false scope on this evidence. Preserve the execution qualifications above wherever the Action promises automatic or always-on behavior. The changes are fixable content precision, not an unavoidable tradeoff requiring a new census. No judge, runtime, admission, integration, or shipping action was performed.

S102 is **not used or assigned** by this review. Supporting settings/trust pages are opened evidence in this report; no new SOURCES row is drafted or claimed committed.

## Bounded search receipts

Used the specialized grep tool (not a client runtime) with pattern `(?i)preview|experimental|\bbeta\b|\balpha\b` over the six freshly fetched hook pages. Observed maturity-label hits: Claude agent hooks at lines 396 and 3990, Claude changed-files list at 1783, VS Code at 4 and 11, and the VS-Code-specific Copilot sentence at 24. Codex hits on `preview` at 188 and 532-535 concern shortened output text, not feature maturity. Repeated the same bounded search over just `Gemini-hooks.page` and `Cursor-hooks.page`; tool output: `No matches found`. This is absence of those strings on these pages, **not** a claim that either client documents nothing about hook maturity everywhere, and not a stability guarantee.

Read the hooks-related settings blocks named in the per-client table, rather than attributing unrelated generic experimental settings to hooks. All reads were static. No headless browser, challenge bypass, client model call, package install, tool upgrade, build, test, linter, counter invocation, or other runtime was used.

## Fetch and process receipts

All scratch writes are inside the assigned sandbox clone. Clone command, exit **0**, empty stdout/stderr:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE && timeout 60 git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r59/CriticPreviewStatus && timeout 30 git -C /fast/scratch/hyaku/kotoba-r59/CriticPreviewStatus checkout -q 67b68e0f9a0c48e5aa5ced63e6117cfca69da491
```

No sandbox commits were made. No lane Git/jj writes were made.

For each row below, the exact shell command was this form with `FILE` and `URL` replaced verbatim by its cells, run in `/fast/scratch/hyaku/kotoba-r59/CriticPreviewStatus` with a 60-second tool deadline:

```sh
timeout 5 date -u && timeout 40 curl -sSL --max-time 30 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -o FILE -w 'HTTP %{http_code}; bytes %{size_download}; effective %{url_effective}\n' URL && timeout 5 sha256sum FILE
```

These are ordinary fetches, not executions of lane code or the counter fetcher. The header values equal the committed counter's `CURL_UA`/`CURL_ACCEPT` at lines 316-318. Every command exited **0**, stderr empty. The 404 also has curl exit 0 because `--fail` was not passed; it is recorded as a failed HTTP source, not evidence. The final effective URL equals the requested URL in every row.

Exact `date -u` stdout groups:

```text
A: Fri 23 Oct 2026 09:36:29 AM UTC
B: Fri 23 Oct 2026 09:36:44 AM UTC
C: Fri 23 Oct 2026 09:37:03 AM UTC
D: Fri 23 Oct 2026 09:37:48 AM UTC
E: Fri 23 Oct 2026 09:38:16 AM UTC
F: Fri 23 Oct 2026 09:38:28 AM UTC
```

The group letters are this report's labels, not part of the `date` command's output. Each invocation printed the date line shown for its group immediately before curl, followed by the HTTP/bytes/effective line and `sha256sum` output reconstructed in this table without truncating the digest:

| UTC group | FILE | URL (also effective URL) | HTTP | bytes | sha256 |
|---|---|---|---:|---:|---|
| A | Claude-hooks.page | https://code.claude.com/docs/en/hooks.md | 200 | 274129 | c6ef9d211e8c4dc870add6302c47971f5fec316888993143011716f78b9862d8 |
| A | Codex-hooks.page | https://learn.chatgpt.com/docs/hooks.md | 200 | 47133 | 57166ef03e7059732dd90925d5c42dd4d187eb2625d66cc154d0fbd2edb65f92 |
| A | VSCode-hooks.page | https://code.visualstudio.com/docs/agent-customization/hooks.md | 200 | 15152 | 98c5be6b693a19ccd10c79b933d56e010101cef5a0eed699bd25e80289461e08 |
| A | Copilot-hooks.page | https://docs.github.com/en/copilot/concepts/customizations/hooks.md | 200 | 8428 | 23370e092d2e2e81587b84038d0be116d99243a83c810b8e8cd41cf8734a10f4 |
| B | Gemini-hooks.page | https://geminicli.com/docs/hooks/best-practices.md | 200 | 17650 | fb44fbcfaccc3cdb7895d989f3808bed66cfa6516411535c4c4d9077d242e7bc |
| B | Cursor-hooks.page | https://cursor.com/docs/hooks | 200 | 69145 | 8436af768468590299c1beab9ea34bff8c5f1e5649ae244a989c28960dd2c88d |
| B | Codex-config.page | https://learn.chatgpt.com/docs/config-file/config-reference.md | 200 | 136297 | fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21 |
| B | Claude-settings.page | https://code.claude.com/docs/en/settings.md | 200 | 42013 | df255caa05a7c40c1806810cb587233a3a4f83dc2ea997b0f3d89a5c49071f04 |
| C | Gemini-config.page | https://geminicli.com/docs/reference/configuration.md | 200 | 102704 | 4fb90004ef3e4aeb3705ceeea4ab8a0d8e0e3aa4553293a1df035990740cc9ca |
| C | VSCode-local.page | https://code.visualstudio.com/docs/agents/reference/hooks-reference.md | 200 | 14412 | 5024a8e5f991a08b341079ee97c538cb15eddf7247e845a1478734ac5e115e7c |
| C | Copilot-reference.page | https://docs.github.com/en/copilot/reference/hooks-reference.md | 200 | 72175 | 7ad7c168f319ce390802289ededf8dead2742959b18b5ccf6f41c2342cbf1c97 |
| C | Copilot-config.page | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md | 200 | 166811 | 8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0 |
| D | Claude-reference.page | https://code.claude.com/docs/en/settings-reference.md | 200 | 414094 | 111f95f7d1b75102fe61f73eb824a5955bf0bfa458e12f4d00e601a041e34a32 |
| E | Gemini-trust.page | https://geminicli.com/docs/cli/trusted-folders.md | 200 | 6188 | f994664cdbb7f206bca5ea61cea0004d9e8f039454c0204d068d8f42e1cb0c48 |
| E | Cursor-thirdparty.page | https://cursor.com/docs/reference/third-party-hooks.md | 404 | 389 | 4f98eb063d1914a3100f2c7e6bab3a449877d33da375eb3c05edc3a61e78afb1 |
| F | Cursor-thirdparty-canonical.page | https://cursor.com/docs/reference/third-party-hooks | 200 | 8851 | c2d2e67fd529f5d14feaaab22b3662f9eac2d21a4c54846f3e28fca6d63292c6 |

Tool installations/updates: **none**. The sole lane write is this report. Its required `ls -l` receipt is pasted in the final handoff after the write.

Report: .ufo/waves/round-59/build/CriticPreviewStatus.md
