Result: MIXED — All listed Gemini payloads and the candidate's preview/load-path additions are supported, but both versions omit the cited page's safety checkers.

## Scope and evidence

Reviewed only the Gemini CLI ship cells at `07c33d73ddce769d9cea2846a6313164401b5478` and their replacements in the untrusted candidate. No round/admission verdict is asserted.

- Frozen checkout: `/fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI`.
- Tip cells: `SKILL.md:121`; `corpus/knowledge/plugin-manifests-round57.md:46`.
- Candidate claims, not evidence: `.ufo/waves/round-57/a3/a2-candidate.patch:23,53,85-87,105`.
- Source: S083, https://geminicli.com/docs/extensions/reference.md .
- Independently fetched bytes: `/fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI/extensions-reference.md` (361 lines). All source line numbers below refer to these fetched bytes, not rendered HTML.

Commands executed, both exit 0:

```sh
timeout 120s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI && timeout 30s git -C /fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI checkout -q 07c33d73ddce769d9cea2846a6313164401b5478
```

Observed output: none.

```sh
timeout 10s date -u && timeout 60s curl --fail --location --silent --show-error --output /fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI/extensions-reference.md --write-out 'url=%{url_effective}\nhttp=%{http_code}\nbytes=%{size_download}\n' https://geminicli.com/docs/extensions/reference.md && timeout 10s sha256sum /fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI/extensions-reference.md
```

Observed output:

```text
Fri 23 Oct 2026 06:46:03 AM UTC
url=https://geminicli.com/docs/extensions/reference.md
http=200
bytes=12022
8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72  /fast/scratch/hyaku/kotoba-r57a3/A3ShipGeminiCLI/extensions-reference.md
```

The fetched byte count and SHA-256 match the existing S083 record at `corpus/SOURCES.md:96`. This agreement was checked against the actual row, not inherited from the candidate or an earlier seat report.

## Findings

### 1. Missing safety-checker surface in both versions

Counterexample: S083 explicitly documents a policy payload with `[[safety_checker]]` (`extensions-reference.md:291-298`), separately names safety checkers alongside policy rules (`:263`), and locates policy files under `policies/` (`:267-269`). Both tip cells end their payload inventory at “policy rules”; both candidate cells still do so. The existing S083 teaches clause already says “policy rules/safety checkers” (`corpus/SOURCES.md:96`), so this is lost detail between the source registry and the decision tables, not a newly discovered client capability.

[INFERENCE] An extension audit treating either ship list as its inventory can overlook a checker definition even after identifying ordinary policy rules. This is a fixable documentation omission, not a reason to delete an otherwise supported component or to alter the frozen counter.

Impacted axes: **depth** (the assigned axis: a named technical component disappears from the actionable table); **coverage** locally (one documented extension surface is missing). No numerical axis assessment or canonical judgment is claimed.

Smallest necessary correction in both tip/candidate cells: `policy rules` → `policy rules and safety checkers`. The existing source range already includes line 263, so this correction needs no fabricated citation and no source-range expansion.

### 2. Context fallback is documented but not made explicit

S083 `:158-161` says that `contextFileName` names the context file and that an extension-root `GEMINI.md` is loaded when that property is absent and the file is present. Neither version explains this fallback. This is an actionable path clarification, not proof that the current generic phrase “a context file” is false.

[INFERENCE] An auditor searching only manifest-named context could miss the default root file. The exact cells below therefore also spell out that existing source-supported fallback. Impact: depth and instruction-file discoverability; no client behavior was executed.

### 3. Candidate additions hold; no unsupported listed part or broken ship citation found

- `sub-agents (preview)` / `sub-agents (a preview feature)` is explicitly supported by S083 `:256`.
- `extensions load from <home>/.gemini/extensions` is explicitly supported by `:106`.
- All seven payload categories already listed at tip are supported inside the cited range `104-112,146-161,229-269`.
- That range also already holds both proposed additions to the payload description: context fallback at `160-161` and safety checkers at `263`.
- The candidate's Gemini quote note is accurate: the manifest quote starts mid-line 106 after the load-path sentence, continues through line 107, and folds exactly one LF to one ASCII space. No backticks are removed. This conclusion is independently derived here, not evidence adopted from the candidate's residual-seat provenance claim.

Themes appear at `:301-344`, settings at `:178-227`, `excludeTools` at `:162-167`, plan storage at `:168-172`, and variable substitution at `:352-361`. These are additional documented UI/configuration/control features; I do not inflate this instruction-bearing inventory by presenting each as another instruction file. In particular, the source calls themes CLI UI customization (`:303-304`), not another instruction-bearing component. This finding makes no claim that the client is silent on any topic.

## Evidence for every part of the proposed cells

Each quotation below is a contiguous byte-exact substring of the fetched source, at most 25 words. No Markdown bytes are stripped and no line breaks are folded in these quotations.

- **MCP servers** — `extensions-reference.md:146-157`; line 146: ``- `mcpServers`: A map of MCP servers to settings.``
- **Context file via `contextFileName`** — `:158-159`; line 158: ``- `contextFileName`: The name of the file that contains the context for the``.
- **Default root `GEMINI.md` when the property is absent and the file exists** — `:160-161`; line 160: ``If this property is not used but a `GEMINI.md` file is present in your``; line 161: `extension directory, then that file will be loaded.` These substrings begin after the lines' two-space indentation; the quoted bytes themselves are unchanged.
- **TOML commands** — `:229-238`; line 231: `by placing TOML files in a`; placement under the commands subdirectory is at `232`, and command-name examples are at `237-238`.
- **Hooks in `hooks/hooks.json`** — `:240-244`; line 243: ``hooks in a `hooks/hooks.json` file within your extension directory.``
- **Hooks not in the manifest** — line 244: ``hooks are not defined in the `gemini-extension.json` manifest.``
- **Skills** — `:246-250`; line 249: ``skill definitions in a `skills/` directory.``
- **Sub-agents** — `:252-259`; line 258: `that users can delegate tasks to.`; line 259: ``agent definition files (`.md`) to an `agents/` directory in your extension root.``
- **Preview qualification** — line 256: `> Sub-agents are a preview feature currently under active development.`
- **Policy rules and safety checkers** — `:261-269`; line 263: `Extensions can contribute policy rules and safety checkers to Gemini CLI`; the checker example is `:291-298`.
- **Extension load directory** — line 106: ``Gemini CLI loads extensions from `<home>/.gemini/extensions`.``

For completeness, the unchanged manifest claim is supported by `:106-107`: “Each extension” at the end of line 106, followed by “must have a `gemini-extension.json` file in its root directory.” on line 107. The complete manifest quotation is recovered by the explicitly described single LF-to-space fold.

## Exact cells I would land

Own minimal correction of the candidate, preserving its verified preview and load-path details. These are proposals only; no lane file was edited.

### `SKILL.md`, What a plugin can ship

Tip old:

```text
MCP servers, a context file (`contextFileName`), TOML commands, hooks in `hooks/hooks.json`, skills, sub-agents, policy rules
```

Candidate old:

```text
MCP servers, a context file (`contextFileName`), TOML commands, hooks in `hooks/hooks.json`, skills, sub-agents (preview), policy rules; extensions load from `<home>/.gemini/extensions`
```

Either old → exact new:

```text
MCP servers, a context file (`contextFileName`; otherwise root `GEMINI.md` if present), TOML commands, hooks in `hooks/hooks.json`, skills, sub-agents (preview), policy rules and safety checkers; extensions load from `<home>/.gemini/extensions`
```

### `corpus/knowledge/plugin-manifests-round57.md`, Instruction-bearing parts a plugin can ship

Tip old:

```text
MCP servers, a context file (`contextFileName`), TOML commands, hooks (in `hooks/hooks.json`, not in the manifest), skills, sub-agents, policy rules
```

Candidate old:

```text
MCP servers, a context file (`contextFileName`), TOML commands, hooks (in `hooks/hooks.json`, not in the manifest), skills, sub-agents (a preview feature), policy rules
```

Either old → exact new:

```text
MCP servers, a context file (`contextFileName`; otherwise root `GEMINI.md` if present), TOML commands, hooks (in `hooks/hooks.json`, not in the manifest), skills, sub-agents (a preview feature), policy rules and safety checkers
```

Retain the source cell exactly:

```text
S083 `extensions-reference.md:104-112,146-161,229-269`
```

## Bounds

No client runtime, lane code, tests, counter, or judge was executed. No C1 remeasurement or round-wide no-harm conclusion is claimed. No sandbox commit was created. No tools were installed or updated. Only this report was written in the lane; the checkout and fetched source are inside this seat's sandbox.
