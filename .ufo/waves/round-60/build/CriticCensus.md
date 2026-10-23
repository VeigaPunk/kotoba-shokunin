Result: HOLDS — every frozen census eligibility verdict survives this review; VS Code needs a harness qualifier, not a different token or target.

# CriticCensus — round-60 BUILD

Reviewed by `KotobaR60.CriticCensus`. Scope: `plans/round-60.md` § Census (freeze record) at `b1cd64bb45eee744c4ec93be8631f1eddb28fddd`, including its E1 context. Axes examined: **depth** and **calibration**. These are source-review findings, not C1 measurements, admission decisions, or a Rust-judge verdict.

## Per-row verdicts

Source labels below resolve to the exact URL, UTC access line, HTTP result, byte count and full sha256 in the fetch ledger. Line numbers address the original fetched bytes, not a reader-mode rendering.

| Frozen row | Verdict | Evidence and strongest attempted counterexample | Smallest safe correction |
|---|---|---|---|
| Claude Code — `.claude/rules/`, `paths` | **HOLDS** | `claude:166,168,176` names the actual rules directory and recursive Markdown discovery; it is not the example filename `testing.md` or the example matching path. `:194,198-199,209,218` establish path-conditional rules and the YAML key/value. | None to eligibility. Preserve the distinction that rules without `paths` load unconditionally (`:188,209`); the folder itself does not make a rule conditional. |
| Codex — NOT ELIGIBLE | **HOLDS** | `codex_agents:9-15,83,151-159` documents the directory/cwd instruction chain and fallback filenames. The strongest rival, `.codex/rules`, is explicitly command execution policy: `codex_rules:5,15,22,46,61-71`. `pattern` is a command-prefix list of literals or unions; `match`/`not_match` are command examples, not work-file selectors. The current source tree, full documentation export and release notes were searched below. | Keep the negative specific to instruction attachment. Do not turn it into a claim that Codex has no path patterns anywhere: deny-read policies and security-scan settings do have them. |
| VS Code — `.github/instructions/**/*.instructions.md`, `applyTo` | **HOLDS**, bounded to supported harnesses | `vscode:25-32` prints this exact discovery glob in the Copilot targeted-instructions column and separately supports it for Local sessions. `:120,128,132` names the actual `.github/instructions` folder and recursive discovery. `:54,105,156,164` supplies behavior and the key. This is a documented file selector, not a literal directory name and not an example file. Native Codex is the strongest counterexample to a universal VS Code reading (`:29`). | Qualify the VS Code entry/action as **Copilot/Local harnesses**. Do not imply that choosing a Claude-family model switches harnesses, or that native Claude/Codex harnesses read this format. |
| Copilot CLI — `.github/instructions/**/*.instructions.md`, `applyTo` | **HOLDS** | `copilot:1,9,18` explicitly identifies the CLI and this exact modular-repository discovery glob. `:54-60` directs the author to create the actual folder and instruction files; `:32,66,74` documents file matching and the key. Neither the selected token nor the directory is an example-specific filename. | None to eligibility. Retain the CLI's discovery qualification: the modular row excludes intermediate directories (`:18`), and disabled instructions are not included (`:32`). |
| Gemini CLI — NOT ELIGIBLE | **HOLDS** | `gemini_context:25-35` documents directory/ancestor JIT discovery, and `:94-105` makes `fileName` a context-filename setting. The current source tree does contain a `match` object, but it selects model/agent request context, not file paths (`gemini:docs/cli/generation-settings.md:67-88,172-208`; `gemini:docs/core/subagents.md:509-520`). A genuinely path-related `argsPattern` selects tool authorization, not instruction loading (`gemini:docs/reference/tools.md:190-198`; policy-engine `:88-94,107-115`). | Say that no eligible **instruction-file attachment key** was found in this bounded sweep, not that the client has no conditional rules or path patterns of any kind. |
| Cursor — `.cursor/rules`, `globs` | **HOLDS** | `cursor:32,42` names the actual project-rule folder and required `.mdc` extension; this is not a sample `react-patterns.mdc`. `:65-70,83-86,131` establishes the path-attached variant and `globs` assignment. | Preserve `alwaysApply: false` for the path-attached case. `alwaysApply: true` ignores globs (`:67`), and plain `.md` files are ignored (`:42`). The folder alone is not an activation rule. |
| opencode — NOT ELIGIBLE | **HOLDS** | Both V1 and current V2 were examined. `opencode_rules:64,68,111,126` documents directory/global guidance and instruction-source globs. V2 `opencode_v2:17,45,101-126`, backed by `opencode:services/www/src/docs/content/instructions.mdx:19,47,103-126`, distinguishes directory discovery from configured instruction-source enumeration. The changelog explicitly advertises local instruction globs (`opencode_changelog:371`), so dismissing them as absent would be wrong. They choose **which instruction files to load**, not **which work files activate an instruction file**. | Retain the source-selection versus target-file-selection distinction. Do not describe opencode as lacking instruction globs. The `paths` key found in migration docs is under `skills`, not instruction frontmatter. |

The eligible VS Code/CLI tokens are file-discovery globs rooted in a documented directory, which the frozen spec explicitly allows (`verifiers/check_scoped_rules.py:87-102`). Calling those globs “folders” literally would be imprecise; it does not falsify their eligibility. No census token, rule, target, routing, or axes change is proposed.

## Strongest counterexample: the same folder does not identify one universal VS Code loader

**Counterexample available directly from the vendor table:** select the native OpenAI Codex harness inside VS Code. The VS Code page's targeted-instructions cell is then nested `AGENTS.md` files (`vscode:29`), not `.github/instructions/**/*.instructions.md`. Native Anthropic Claude has `.claude/rules` (`:28`). The page says support depends on the selected harness (`:9,23`) and names the Copilot and Local cases separately (`:27,32,120,128`). This breaks an unqualified instruction such as “put this in `.github/instructions` for every VS Code agent,” not the frozen existential eligibility row. No runtime behavior was simulated or asserted.

**Do both products document the SAME folder? Yes.** VS Code's Copilot workspace row is `.github/instructions` (`vscode:120`); the CLI creation step names exactly `.github/instructions` (`copilot:54`). Both independently print `.github/instructions/**/*.instructions.md` (`vscode:27`; `copilot:18`). The `**` is a discovery selector for nested instruction files, not a second folder and not the frontmatter's matching-work-file pattern. `applyTo` is the latter.

**Do they name the reader? Yes.** The VS Code page identifies Copilot and Local harness support; the CLI page identifies Copilot CLI in its title and discovery statements (`copilot:1,9,32`). The linked harness definition is even more explicit: `vscode_harnesses:8` documents a shared Copilot runtime across VS Code, CLI and app; `:50` places the Copilot harness in Agent Host and Local in the extension host. Therefore these are two documented client surfaces, not evidence of independent underlying implementations. The frozen E5 exception counts clients and permits their shared token; there is no basis here to change that rule or claim implementation independence.

Discovery is not fully interchangeable either. The CLI table excludes intermediate directories for modular instructions (`copilot:18`). VS Code searches its supported locations recursively (`vscode:132`) and expressly warns that CLI/app do not inherit editor custom-search settings (`:130`). Sharing a repository folder does not make editor profiles or custom discovery settings portable.

**Impacted axes:** depth (the instructions must identify the reader and activation conditions) and calibration (do not infer universal support or independent implementations from two client labels). **Smallest safe correction:** add a short Copilot/Local harness qualifier beside the VS Code row/action, and retain native-format guidance for other harnesses in the entry. This is a fixable presentation defect if omitted, not an inherent tradeoff requiring a counter or target change. Only the canonical judge may decide the round.

## Negative-case sweep: three required legs, plus near misses

### Documentation source trees and searched content

Current branches were resolved through read-only GitHub metadata and all selected Markdown source bytes were opened on the permitted raw mirrors, pinned to these upstream commits:

- Codex: `openai/codex@d8acdf151577132d4ee1de47a4d1822ae5acb762`, `docs/**/*.md`/`.mdx` path entries from the current tree. These repository docs are mostly migration/link stubs, so the served `codex_export` was also searched; examining the stubs alone would be insufficient.
- Gemini CLI: `google-gemini/gemini-cli@a713410aba5d594594e20d5c822e3aab8f822089`, all Markdown docs path entries. The `docs/CONTRIBUTING.md` symlink target (`../CONTRIBUTING.md`) was opened separately as `gemini_contributing`.
- opencode: `anomalyco/opencode@4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f`, English V1 root docs and the entire V2 `services/www/src/docs/content/` Markdown subtree, including nested plugin/SDK/CLI/console docs. This includes nested V2 pages beyond W0's root-only selection. Locale translations were not separately read; no locale/version alias was used to manufacture another source.

GitHub API responses are enumeration/ref metadata only, not pinned-host claim-backing pages. Every substantive documentation quotation is from a pinned vendor host or the allowed raw mirror of its repository.

The count expression actually evaluated was `len(doc_sets[client])`. Every listed source fetch exited 0 and returned HTTP 200. Counts and exact keyword-sweep results follow; the fetch ledger records each URL and its bytes rather than silently treating a failed request as absence.


| Tree | Selected path entries | Successful HTTP 200 |
|---|---:|---:|
| codex | 15 | 15 |
| gemini | 97 | 97 |
| opencode | 100 | 100 |

`gemini_contributing` is an additional successful fetch, not another docs-tree path entry. The symlink path bytes and target bytes are both in the ledger. The source scan used `re.search(pattern, line, re.I)` for every line of every selected response. Observed matching-line counts:

| Source tree | applyTo/apply_to | globs | paths key | match key | frontmatter | native rules folder |
|---|---:|---:|---:|---:|---:|---:|
| codex | 0 | 0 | 0 | 0 | 0 | 0 |
| gemini | 0 | 0 | 0 | 4 | 11 | 0 |
| opencode | 0 | 2 | 1 | 0 | 28 | 0 |

Exact scan patterns (counts are search observations, not a semantic verifier):
```text
applyTo = \bapply_?to\b
globs = \bglobs\b
paths_key = (?m)^\s*(?:["\x27`]?paths["\x27`]?)\s*[:=]
match_key = (?m)^\s*(?:["\x27`]?match["\x27`]?)\s*[:=]
frontmatter = front\s*matter|frontmatter
path_scoped = path[- ](?:scop|specif)|file[- ]scop|scoped?\s+(?:rules?|instructions?)
rules_folder = \.(?:codex|gemini|opencode)/rules
```

The nonzero near misses were read, not counted as evidence of attachment semantics:

- Gemini's `match` sites are request/model overrides (`generation-settings.md:84,181,203`; `core/subagents.md:520`). Skill/subagent frontmatter is a different surface. `.gemini/system.md` is a full system-prompt replacement selected by `GEMINI_SYSTEM_MD`, not a path-scoped attachment (`gemini:docs/cli/system-prompt.md:1-12,29-40`). `.geminiignore` is an ignore file; policy `argsPattern` can constrain paths in tool calls but does not inject Markdown instructions.
- opencode's only line-start `paths` key in this scan is the V1 `skills.paths` migration example (`opencode:services/www/src/docs/content/migrate-v1.mdx:294-313`). Its plural `globs` hits describe configured instruction-source enumeration and available read tools (`config.mdx:444-449`; `permissions.mdx:233`). Permissions in agent frontmatter can have path resources, but they authorize tools, not rule-file activation. V1's `.cursor/rules/*.md` example is a foreign instruction-source glob, not evidence that opencode implements Cursor's `globs` frontmatter.
- The Codex full export's key-form `match` is execpolicy's command-example list (`codex_export:749`). `paths` examples are scan/artifact configuration (`:45850,46621,46981`), not instruction metadata; the scan page even says those paths do not expand globs (`:46626`). Actual glob documentation covers filesystem-denial and network scopes (`:14530-14533,38053-38099,53439,53452`), not instruction attachment. `applyTo`/`apply_to`, `frontmatter` and `path-scoped` have no hits in this export under the reported searches.

To avoid assuming only familiar key names exist, a second, deliberately broad static search collected any line-start key-like name followed by `:`/`=` when `*` occurred on that line or the following lines. The exact expression was `^\s*["\x27`]?([A-Za-z][A-Za-z0-9_-]*)["\x27`]?\s*[:=]`, and the window was `'\n'.join(lines[i-1:min(i+3,len(lines))])`. This is read-only text inspection, not a C1 run. Its candidates were reviewed as prose, examples, policy/tool keys, source-list keys, or unrelated API/UI data; it did not reveal an instruction-attachment key. In particular, opencode `system` neighbors wildcard permissions but is not a pattern-taking field, and Gemini `argsPattern` is a path-related authorization near miss, not ignored evidence.

### Changelogs / releases opened

- Codex `codex_changelog:1` points to the releases page. Both that releases page and the current stable `rust-v0.164.0` release were opened (`codex_releases`, `codex_release_tag`). The stable release's raw HTML had no `applyTo`/`apply_to`, whole-word `globs`, `frontmatter`, or `path-scoped` hit. This is bounded release evidence, not a claim to have read every historical release.
- Gemini's announcement index, stable notes and preview notes were opened (`gemini_changelog`, `gemini_stable`, `gemini_preview`), as well as their current docs-source counterparts. The announcement index explicitly records JIT context discovery (`gemini_changelog:385-389`). The preview source has a skill-frontmatter parsing fix (`gemini:docs/changelogs/preview.md:71-72`); that is not a rule attachment key.
- opencode's current changelog was opened (`opencode_changelog`). Its instruction-glob announcement at `:371` was treated as positive evidence and then followed into V2 instruction/config documentation, where the globs enumerate instruction sources. This avoids the earlier round-52 failure mode of calling a client silent after looking only at an old page.

### Lane corpus searched

The specialized grep tool was used over the lane's complete `corpus/` with `gitignore: false`, case-insensitive:

```json
{"pattern":"(?i)(apply_?to|\\bglobs\\b|path[- ]scop|\\.codex/rules|\\.gemini/rules|\\.opencode/rules)","path":"/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus","case":false,"gitignore":false,"skip":0}
```

Tool result: success (there is no subprocess exit code for this tool). Relevant returned evidence: `corpus/SOURCES.md:57-59` (S044-S046); `corpus/knowledge/instruction-surface-remeasure-round13.md:25,47-49`; `corpus/knowledge/instruction-surface-census-round13.md:254-257,480`; and the skill-selection/overlap entries' references to **Claude** `paths`. The round-13 `applyTo` hit describes the github/instructions class, not native Codex, Gemini CLI or opencode attachment. The opencode `instructions` source globs were already held in the corpus. No returned corpus evidence establishes the missing native attachment mechanism; near-miss text was not reassigned across clients.

This supplies all Q30 legs for the bounded negative verdicts: current docs source, changelog/release notes, and the lane corpus. It does **not** prove there is no undocumented implementation, private feature, translation-only fact, future change, or historical release with other behavior. The verdict is that the frozen NOT ELIGIBLE classification survives the documented C1 search at the recorded access times.

## Commands, bounds, and provenance

Frozen plan read (read-only; exit 0):
```sh
timeout 30 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show b1cd64bb45eee744c4ec93be8631f1eddb28fddd:plans/round-60.md
```
Observed census is at `plans/round-60.md:99-110`, with A1 at `:54-65` and E1 at `:125-153`. The counter docstring was read before this report was drafted (`verifiers/check_scoped_rules.py:1-225`); no counter was invoked, and no measured revision was scored.

Fetch command template actually used for every ledger entry:
```sh
timeout 5 date -u
timeout 50 curl -sSL --max-time 45 \
  -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36' \
  -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' \
  -w '\n__CENSUS_META__%{http_code} %{url_effective}' '<URL>'
```
`date -u` lines were captured immediately before each fetch. The final curl write-out delimiter and metadata were separated from the response body; `len(body)` and `hashlib.sha256(body).hexdigest()` produced the ledger byte counts and hashes. No body normalization or Markdown shaping was used for those hashes. Four bounded curl processes ran concurrently at most. Bodies stayed in memory; no source or receipt files were written outside this report.

No lane code executed; no sandbox commits, lane Git writes, jj mutations, model calls, tests, builds, linters, formatters, or C1 measurement runs. No tools installed or updated. One tooling issue was reported through the required QA device: the read tool treats an inline line selector on `xd://eval/helpers` as part of the topic; rereading its bare topic supplied the docs. That tooling issue had no source-evidence consequence.

## Verbatim quote and count receipts

Every quoted block below is an exact whole-line selection from the original fetched body. The shown `timeout 5 sed -n` selection was actually run against the in-memory fetched bytes (stdin), before the displayed `printf ... | wc -w` command. Every selection and counting subprocess exited 0; every selected quote is a byte substring of its body. No Markdown bytes were stripped and no line wraps were changed. Key/header excerpts need not meet the C1 entry-quote minimum; these are review receipts, not proposed C1 cells.


### ClaudeFolder — `claude:166`

Selection: `timeout 5 sed -n '166p'` (stdin = fetched body), exit 0.

```text
### Organize rules with `.claude/rules/`
```

Counting command actually run:
```sh
printf '%s\n' '### Organize rules with `.claude/rules/`' | wc -w
```
Exit 0; `wc -w` output: `5`.


### ClaudeKey — `claude:198-199`

Selection: `timeout 5 sed -n '198,199p'` (stdin = fetched body), exit 0.

```text
paths:
  - "src/api/**/*.ts"
```

Counting command actually run:
```sh
printf '%s\n' 'paths:
  - "src/api/**/*.ts"' | wc -w
```
Exit 0; `wc -w` output: `3`.


### VSCodeGlob — `vscode:27`

Selection: `timeout 5 sed -n '27p'` (stdin = fetched body), exit 0.

```text
| Copilot | [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) or [`AGENTS.md`](#use-an-agentsmd-file) | [`.github/instructions/**/*.instructions.md`](#use-instructionsmd-files) |
```

Counting command actually run:
```sh
printf '%s\n' '| Copilot | [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) or [`AGENTS.md`](#use-an-agentsmd-file) | [`.github/instructions/**/*.instructions.md`](#use-instructionsmd-files) |' | wc -w
```
Exit 0; `wc -w` output: `9`.


### VSCodeFolder — `vscode:120`

Selection: `timeout 5 sed -n '120p'` (stdin = fetched body), exit 0.

```text
| Copilot workspace | `.github/instructions` |
```

Counting command actually run:
```sh
printf '%s\n' '| Copilot workspace | `.github/instructions` |' | wc -w
```
Exit 0; `wc -w` output: `6`.


### VSCodeNativeCodex — `vscode:29`

Selection: `timeout 5 sed -n '29p'` (stdin = fetched body), exit 0.

```text
| OpenAI Codex | [`AGENTS.md`](#use-an-agentsmd-file) | `AGENTS.md` files in subfolders |
```

Counting command actually run:
```sh
printf '%s\n' '| OpenAI Codex | [`AGENTS.md`](#use-an-agentsmd-file) | `AGENTS.md` files in subfolders |' | wc -w
```
Exit 0; `wc -w` output: `11`.


### CopilotFolder — `copilot:54`

Selection: `timeout 5 sed -n '54p'` (stdin = fetched body), exit 0.

```text
1. Create the `.github/instructions` directory if it does not already exist.
```

Counting command actually run:
```sh
printf '%s\n' '1. Create the `.github/instructions` directory if it does not already exist.' | wc -w
```
Exit 0; `wc -w` output: `11`.


### CopilotKey — `copilot:66`

Selection: `timeout 5 sed -n '66p'` (stdin = fetched body), exit 0.

```text
   applyTo: "app/models/**/*.rb"
```

Counting command actually run:
```sh
printf '%s\n' '   applyTo: "app/models/**/*.rb"' | wc -w
```
Exit 0; `wc -w` output: `2`.


### CursorFolder — `cursor:32`

Selection: `timeout 5 sed -n '32p'` (stdin = fetched body), exit 0.

```text
Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.
```

Counting command actually run:
```sh
printf '%s\n' 'Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled. They are scoped using path patterns, invoked manually, or included based on relevance.' | wc -w
```
Exit 0; `wc -w` output: `24`.


### CursorKey — `cursor:85-86`

Selection: `timeout 5 sed -n '85,86p'` (stdin = fetched body), exit 0.

```text
globs: src/components/**/*.tsx
alwaysApply: false
```

Counting command actually run:
```sh
printf '%s\n' 'globs: src/components/**/*.tsx
alwaysApply: false' | wc -w
```
Exit 0; `wc -w` output: `4`.


### CodexCommands — `codex_rules:5`

Selection: `timeout 5 sed -n '5p'` (stdin = fetched body), exit 0.

```text
Use rules to control which commands Codex can run outside the sandbox.
```

Counting command actually run:
```sh
printf '%s\n' 'Use rules to control which commands Codex can run outside the sandbox.' | wc -w
```
Exit 0; `wc -w` output: `12`.


### CodexPattern — `codex_rules:61`

Selection: `timeout 5 sed -n '61p'` (stdin = fetched body), exit 0.

```text
- `pattern` **(required)**: A non-empty list that defines the command prefix to match. Each element is either:
```

Counting command actually run:
```sh
printf '%s\n' '- `pattern` **(required)**: A non-empty list that defines the command prefix to match. Each element is either:' | wc -w
```
Exit 0; `wc -w` output: `17`.


### CodexDiscovery — `codex_agents:83`

Selection: `timeout 5 sed -n '83p'` (stdin = fetched body), exit 0.

```text
Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible.
```

Counting command actually run:
```sh
printf '%s\n' 'Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible.' | wc -w
```
Exit 0; `wc -w` output: `19`.


### GeminiDiscovery — `gemini_context:32-33`

Selection: `timeout 5 sed -n '32,33p'` (stdin = fetched body), exit 0.

```text
      automatically scans for `GEMINI.md` files in that directory and its
      ancestors up to a trusted root.
```

Counting command actually run:
```sh
printf '%s\n' '      automatically scans for `GEMINI.md` files in that directory and its
      ancestors up to a trusted root.' | wc -w
```
Exit 0; `wc -w` output: `16`.


### GeminiFilename — `gemini_context:105`

Selection: `timeout 5 sed -n '105p'` (stdin = fetched body), exit 0.

```text
    "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]
```

Counting command actually run:
```sh
printf '%s\n' '    "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]' | wc -w
```
Exit 0; `wc -w` output: `4`.


### OpenCodeSourceGlobs — `opencode_v2:101`

Selection: `timeout 5 sed -n '101p'` (stdin = fetched body), exit 0.

```text
Use the `instructions` array to add files, glob patterns, or HTTP(S) URLs alongside discovered `AGENTS.md` files:
```

Counting command actually run:
```sh
printf '%s\n' 'Use the `instructions` array to add files, glob patterns, or HTTP(S) URLs alongside discovered `AGENTS.md` files:' | wc -w
```
Exit 0; `wc -w` output: `16`.


### OpenCodeMerge — `opencode_v2:115`

Selection: `timeout 5 sed -n '115p'` (stdin = fetched body), exit 0.

```text
Configured instructions load after `AGENTS.md` files, in the order they are listed. Entries from every config document are combined.
```

Counting command actually run:
```sh
printf '%s\n' 'Configured instructions load after `AGENTS.md` files, in the order they are listed. Entries from every config document are combined.' | wc -w
```
Exit 0; `wc -w` output: `19`.


### OpenCodeChangelog — `opencode_changelog:371`

Selection: `timeout 5 sed -n '371p'` (stdin = fetched body), exit 0.

```text
- Load local glob patterns and remote URLs configured through `instructions`, and refresh them when configuration changes. ([#55539](https://github.com/anomalyco/opencode/pull/55539))
```

Counting command actually run:
```sh
printf '%s\n' '- Load local glob patterns and remote URLs configured through `instructions`, and refresh them when configuration changes. ([#55539](https://github.com/anomalyco/opencode/pull/55539))' | wc -w
```
Exit 0; `wc -w` output: `18`.


## Fetch ledger

Each row records one completed ordinary curl fetch. `date -u` is pasted verbatim. Every final HTTP result and subprocess exit code is explicit. API rows are enumeration metadata only. Raw source names carry their repository-relative path, and their URL includes the pinned upstream commit.

| Label | Requested URL | date -u | HTTP / final URL | curl exit | Body bytes | sha256 |
|---|---|---|---|---:|---:|---|
| `claude` | https://code.claude.com/docs/en/memory.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://code.claude.com/docs/en/memory.md | 0 | 54043 | `82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7` |
| `vscode` | https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | 0 | 23715 | `a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f` |
| `copilot` | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 0 | 8730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` |
| `cursor` | https://cursor.com/docs/rules | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://cursor.com/docs/rules | 0 | 17403 | `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8` |
| `codex_agents` | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | 0 | 9149 | `9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e` |
| `codex_rules` | https://learn.chatgpt.com/docs/agent-configuration/rules.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://learn.chatgpt.com/docs/agent-configuration/rules.md | 0 | 6783 | `4ecdfe26ece03895220808a7aa4f05c91d837492300262baf5a5df35c3f44ce7` |
| `codex_export` | https://learn.chatgpt.com/docs/llms-full.txt | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://learn.chatgpt.com/docs/llms-full.txt | 0 | 2550095 | `efc3a0f74d5e2b8d86308716b45bb2fd52abb2f1b816d0a1c88031b87f839bff` |
| `codex_changelog` | https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md | 0 | 330 | `c8458f99de91a4b4b9682ecb72c396f0d08c03c51a657759e1239c3a14c697d5` |
| `gemini_context` | https://geminicli.com/docs/cli/gemini-md.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://geminicli.com/docs/cli/gemini-md.md | 0 | 3816 | `e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2` |
| `gemini_changelog` | https://geminicli.com/docs/changelogs.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://geminicli.com/docs/changelogs.md | 0 | 69617 | `e8fb2a25f450de8ed4cc1db23c0c48d269853cd05b375399e7a4e47d834f423a` |
| `gemini_stable` | https://geminicli.com/docs/changelogs/latest.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://geminicli.com/docs/changelogs/latest.md | 0 | 4140 | `f38215087f7adabbd9d52831ceeb1def13bc98eb4b62181c518f295e399dd68f` |
| `gemini_preview` | https://geminicli.com/docs/changelogs/preview.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://geminicli.com/docs/changelogs/preview.md | 0 | 6038 | `c186463197c0cb2d65eece11cc0b69a567d7a2b4967443447cf8488b40d06593` |
| `opencode_rules` | https://opencode.ai/docs/rules.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://opencode.ai/docs/rules.md | 0 | 6684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |
| `opencode_v2` | https://opencode.ai/v2/docs/instructions/ | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://opencode.ai/v2/docs/instructions/ | 0 | 5618 | `56162c66b6124de0591d8b902f5e0c9dee3ca03a468985aabb64808630f5c957` |
| `opencode_index` | https://opencode.ai/llms.txt | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://opencode.ai/v2/llms.txt | 0 | 4061 | `79fe81b6d690646e875dbbbc696738286f677a47bd2ea39c4318437ed0dfacd0` |
| `opencode_changelog` | https://raw.githubusercontent.com/anomalyco/opencode/dev/CHANGELOG.md | `Fri Oct 23 12:09:07 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/dev/CHANGELOG.md | 0 | 55190 | `1d7914fd62cb1f12806a2397700a7beebab4575b88d80b41478da3f22dd0ba2a` |
| `codex_tree` | https://api.github.com/repos/openai/codex/git/trees/main?recursive=1 | `Fri Oct 23 12:09:31 PM UTC 2026` | 200 https://api.github.com/repos/openai/codex/git/trees/main?recursive=1 | 0 | 3353348 | `65970477555c5546746c5a6aef3e4a9bb1847c1d23b69b08c53f637a25452541` |
| `gemini_tree` | https://api.github.com/repos/google-gemini/gemini-cli/git/trees/main?recursive=1 | `Fri Oct 23 12:09:31 PM UTC 2026` | 200 https://api.github.com/repos/google-gemini/gemini-cli/git/trees/main?recursive=1 | 0 | 1068132 | `37fb83b47f9633f4356971245342583c7961116f8bf58b2c98571a677b181185` |
| `opencode_tree` | https://api.github.com/repos/anomalyco/opencode/git/trees/dev?recursive=1 | `Fri Oct 23 12:09:31 PM UTC 2026` | 200 https://api.github.com/repos/anomalyco/opencode/git/trees/dev?recursive=1 | 0 | 2971864 | `c0938eacb6273290965803e38e81c9bbf4064b5f863f2920ab786cd52de8d788` |
| `codex_commit` | https://api.github.com/repos/openai/codex/commits/main | `Fri Oct 23 12:09:57 PM UTC 2026` | 200 https://api.github.com/repos/openai/codex/commits/main | 0 | 9758 | `3785a5b93b5e5689963ba64207b1cac56ff682432f0a5581625b705cc0524526` |
| `gemini_commit` | https://api.github.com/repos/google-gemini/gemini-cli/commits/main | `Fri Oct 23 12:09:57 PM UTC 2026` | 200 https://api.github.com/repos/google-gemini/gemini-cli/commits/main | 0 | 45171 | `cdc2607600827543433ab19c66b59e7904f5ac2a45b260953624567a97eba6e8` |
| `opencode_commit` | https://api.github.com/repos/anomalyco/opencode/commits/dev | `Fri Oct 23 12:09:57 PM UTC 2026` | 200 https://api.github.com/repos/anomalyco/opencode/commits/dev | 0 | 14195 | `b15662a69cffd656d9176a1fdcf1c3dcaec6b56363ff085bc3d494bee463e934` |
| `codex_releases` | https://github.com/openai/codex/releases | `Fri Oct 23 12:09:57 PM UTC 2026` | 200 https://github.com/openai/codex/releases | 0 | 554907 | `c4e75a1f97a87344468f86a744826ccdf5a708c6bd52227a3989611ab6bb5e6f` |
| `codex:docs/CLA.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/CLA.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/CLA.md | 0 | 2059 | `3c3fc352c13db113d079a637f338e696e2dc47af53bae3394cf8fb8de6daa562` |
| `codex:docs/agents_md.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/agents_md.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/agents_md.md | 0 | 126 | `56f5b6026b15fad40fe8b1f6f8910b9fccdf66da3b39dd943c91877e2299619e` |
| `codex:docs/authentication.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/authentication.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/authentication.md | 0 | 134 | `3fe4a065894ac5c1c212432a2c35b9e16a39a79377ea4c9521122a28ae0f7aef` |
| `codex:docs/config.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/config.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/config.md | 0 | 726 | `745768b4da6cd73e414fc49c5c6ef3d6bf8a0c08289fab23a7dd79776ab31d9d` |
| `codex:docs/contributing.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/contributing.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/contributing.md | 0 | 2622 | `205b46a2a743aaec47ea46ef7787dfae72eaa9dee4529fba4c635109c8cada9a` |
| `codex:docs/example-config.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/example-config.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/example-config.md | 0 | 134 | `8c360f977c2f5971b36bbda5721ec51b2604e7013eca46b3d4f51433461909c3` |
| `codex:docs/exec.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/exec.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/exec.md | 0 | 146 | `49eac6fd452d21763683c9f224075d6c5c74ffa28217fbe50c279fa6a543200b` |
| `codex:docs/execpolicy.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/execpolicy.md | `Fri Oct 23 12:10:39 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/execpolicy.md | 0 | 138 | `76b29e8cffcfab00c706e9bbd443e4f4b8c53288968b434e5990af1766132450` |
| `codex:docs/getting-started.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/getting-started.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/getting-started.md | 0 | 177 | `210187b0199e42d71beabab773f6b8f3c01fe897037df1b16f88dd4efe007e90` |
| `codex:docs/install.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/install.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/install.md | 0 | 2732 | `1126ec733921878a40720e139ba7be88e325ecf9fa5b113de2cc636bc71a1f5a` |
| `codex:docs/license.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/license.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/license.md | 0 | 84 | `dca51cd27a681f46b17d7867d1e8311c024ec1478a6e12b6463a71a4e2f869ba` |
| `codex:docs/open-source-fund.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/open-source-fund.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/open-source-fund.md | 0 | 340 | `7dd10179cc0275c1cef77f5ab63e5e0b149aca2868318e7d958dea0d1e42707c` |
| `codex:docs/sandbox.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/sandbox.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/sandbox.md | 0 | 150 | `61d4dd0ccda2a0cbbde78832e752cdf56b1eb8cf7a54f1d46b52a2824c911249` |
| `codex:docs/skills.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/skills.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/skills.md | 0 | 115 | `e59789d09692310bbf94e2ef8db0aaf00d97f2226982c8c5330d2d260583a97d` |
| `codex:docs/slash_commands.md` | https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/slash_commands.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/openai/codex/d8acdf151577132d4ee1de47a4d1822ae5acb762/docs/slash_commands.md | 0 | 145 | `0c063e80ca817a88bc7cd81c11669f73dad1941296142153bdac4dc08a733e69` |
| `gemini:docs/CONTRIBUTING.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/CONTRIBUTING.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/CONTRIBUTING.md | 0 | 18 | `3b4a07b9c92d73f838166d1bc5907f6d4305d0661b13e4617d9820f4d21e7207` |
| `gemini:docs/admin/enterprise-controls.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/admin/enterprise-controls.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/admin/enterprise-controls.md | 0 | 6462 | `ee86880b717cca667e55b25f7e955f02517f3740667949ae0137f14c0f4744f6` |
| `gemini:docs/behavioral-evals.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/behavioral-evals.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/behavioral-evals.md | 0 | 7119 | `158f67da4fd2a5ba5ec4f8165040f0bf16f89959af67545783bef1fbcdfae836` |
| `gemini:docs/changelogs/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/index.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/index.md | 0 | 70570 | `cdc7744aec682e441d8ffb55e71eb49067060d7d9fc799370f3d79f123ec6b32` |
| `gemini:docs/changelogs/latest.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/latest.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/latest.md | 0 | 5916 | `bbbe4712fe5991cf5bebc741e1c2d963d1c22abe125baa27e7c2c72b59df7d11` |
| `gemini:docs/changelogs/preview.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/preview.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/changelogs/preview.md | 0 | 5802 | `d8580ff5c9598a924c44e44934a50b0a4154c5aa6f8e896c5824116265231306` |
| `gemini:docs/cli/acp-mode.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/acp-mode.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/acp-mode.md | 0 | 4684 | `812af1001c110f474a624c3026c31e66519ca95c251d1f79679d8ebd56edd779` |
| `gemini:docs/cli/auto-memory.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/auto-memory.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/auto-memory.md | 0 | 6976 | `232133c2568ca86323415901f2648147f65ac85751c8aa1ea07cb9d7b6d1a588` |
| `gemini:docs/cli/checkpointing.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/checkpointing.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/checkpointing.md | 0 | 3115 | `cb4261f5390134e586459de23a1fef62d2741d9e0c0b3ca1c1372c629e8a89af` |
| `gemini:docs/cli/cli-reference.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/cli-reference.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/cli-reference.md | 0 | 16563 | `ec376db5857fe8dda715ce38575370c33aa03390925b2d7024f0642021525545` |
| `gemini:docs/cli/creating-skills.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/creating-skills.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/creating-skills.md | 0 | 6689 | `244e992d0a504bf54e92679291d30fdbe6a2e98f960a19bcb75ee928e3960385` |
| `gemini:docs/cli/custom-commands.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/custom-commands.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/custom-commands.md | 0 | 12130 | `d0a7dacc329cfb6055195b066e70e6c75cfce280e626101bad14f4d1907a7e83` |
| `gemini:docs/cli/enterprise.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/enterprise.md | `Fri Oct 23 12:10:40 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/enterprise.md | 0 | 19166 | `2632ef8a3a7017d12aad83581437404c095e38080c844e45d0bdc82ed4ce57ca` |
| `gemini:docs/cli/gemini-ignore.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/gemini-ignore.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/gemini-ignore.md | 0 | 2065 | `21cf247e9066355a3ec1130097e3aaa6ec7065a95d1b52c623e7e46d975253cc` |
| `gemini:docs/cli/gemini-md.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/gemini-md.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/gemini-md.md | 0 | 3807 | `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf` |
| `gemini:docs/cli/generation-settings.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/generation-settings.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/generation-settings.md | 0 | 6516 | `06d1a138349ec1c97202936557042c87de992e729268cda82c7f83d6b3356a3f` |
| `gemini:docs/cli/git-worktrees.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/git-worktrees.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/git-worktrees.md | 0 | 3577 | `3c2cec491f0134509b431eaebd8e7d036efd49edea900f546c917a7479a13150` |
| `gemini:docs/cli/headless.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/headless.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/headless.md | 0 | 1578 | `42718e00f5acac2ab039091fab282ed9b3d992ae9f49afc64ec7636fbf6fa6ec` |
| `gemini:docs/cli/model-routing.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model-routing.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model-routing.md | 0 | 2735 | `7e7cc3785ea30a59481d155c6f3c09299b1fa13d57fb982b555852c5bd960141` |
| `gemini:docs/cli/model-steering.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model-steering.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model-steering.md | 0 | 2878 | `81817458cdae634a539ada9539b95fce258289502aa226422eab7bbd8f9df545` |
| `gemini:docs/cli/model.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/model.md | 0 | 2730 | `11ab3a82c4e8212c693ef5f20c43ff82def58703563150ba127163fb10b9ac51` |
| `gemini:docs/cli/notifications.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/notifications.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/notifications.md | 0 | 1952 | `cc07054bf15d52359f1d7785d09d7b13accb50b6d84416e56ff28f467667e4b3` |
| `gemini:docs/cli/plan-mode.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/plan-mode.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/plan-mode.md | 0 | 19595 | `373ead37591eff0fc5b6280cd9ec96244ea48acc1307ba3673c03d9e808d41cc` |
| `gemini:docs/cli/rewind.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/rewind.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/rewind.md | 0 | 2330 | `ed3e2ea2d3f021b1acf38acab2ed06cdc3f27d2649b794076551498a13071165` |
| `gemini:docs/cli/sandbox.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/sandbox.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/sandbox.md | 0 | 15484 | `2c97b1fbc92c33fa9f045669a5fe93f5690ee8a8c2ae839418d350ae78d6d0e5` |
| `gemini:docs/cli/session-management.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/session-management.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/session-management.md | 0 | 6352 | `849204da2c2151de46a39764f0cc92bb7eaac43262051467388d254f671a92fe` |
| `gemini:docs/cli/settings.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/settings.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/settings.md | 0 | 37345 | `f20e3dfa2c27974be9d2200a5d0f6804e45b09b90810b432ca9bebec9fc355e2` |
| `gemini:docs/cli/skills-best-practices.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills-best-practices.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills-best-practices.md | 0 | 3258 | `a064fd7fb55eab56d44e74b7367ad122f93a2f48fdfa5442e658ff3ba07d34f0` |
| `gemini:docs/cli/skills.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/skills.md | 0 | 5740 | `51e8573ef4c068dbdef5f73bd665c47ab16718aefe4edba365fe333b2d85f96d` |
| `gemini:docs/cli/system-prompt.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/system-prompt.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/system-prompt.md | 0 | 4634 | `46d42b94733e625d548b3022d99a3a01211ae6f73e7554413e9da45444528241` |
| `gemini:docs/cli/telemetry.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/telemetry.md | `Fri Oct 23 12:10:41 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/telemetry.md | 0 | 29634 | `c731cf1f5403c2164f1164dc1c9581782e324c16cc6c4fedb51716978d45c133` |
| `gemini:docs/cli/themes.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/themes.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/themes.md | 0 | 8097 | `a9e0ea7b69f472039ac22f969f9bf646f8c3152b966fed40e902a15326066c0d` |
| `gemini:docs/cli/token-caching.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/token-caching.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/token-caching.md | 0 | 754 | `0cd2b222377c8874b7cb4e52fc8f61e198643e716aea987855d0d4780ad54f12` |
| `gemini:docs/cli/trusted-folders.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/trusted-folders.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/trusted-folders.md | 0 | 6195 | `a9d986314ad4806d356eeca678a9ea0f838851372c84979471d1ba6e0250e44d` |
| `gemini:docs/cli/tutorials/automation.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/automation.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/automation.md | 0 | 7141 | `a5e815ce9cafc808f92a05dc92672b2c553edd1aae395ea873c1abfd41268ebd` |
| `gemini:docs/cli/tutorials/file-management.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/file-management.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/file-management.md | 0 | 4472 | `bc2d4b7e25b4ad34f78061a7ffb43f149f6e3afa5f3281c46882e6eb0f753342` |
| `gemini:docs/cli/tutorials/mcp-setup.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/mcp-setup.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/mcp-setup.md | 0 | 3254 | `9a4633c905689c79d06e1e3fe59236ccc76010bce5ef6da38b0ff41e5f14a4b0` |
| `gemini:docs/cli/tutorials/memory-management.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/memory-management.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/memory-management.md | 0 | 4541 | `3d745a89d9f455a458af2561002612270628ce6acb4af8364b4d1f614d32ff9c` |
| `gemini:docs/cli/tutorials/plan-mode-steering.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/plan-mode-steering.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/plan-mode-steering.md | 0 | 3509 | `b0f94afa0966740c08a346cac5660882fcc30ad60361d75e64faab4b0cf0c2a5` |
| `gemini:docs/cli/tutorials/session-management.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/session-management.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/session-management.md | 0 | 3668 | `a14b362df736246a99019504996507dcca7d0af5715cb5321a5891bf79fbb0b5` |
| `gemini:docs/cli/tutorials/shell-commands.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/shell-commands.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/shell-commands.md | 0 | 3624 | `66a496e97d82605e11475ac0379ede83ec49f2fe5c0c22301cde61a87284a2df` |
| `gemini:docs/cli/tutorials/skills-getting-started.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/skills-getting-started.md | 0 | 5855 | `111e8bfa1b99c2d2e2728864d092728334f73eb4fc9ce2998f6cf6ba3ca1c167` |
| `gemini:docs/cli/tutorials/task-planning.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/task-planning.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/task-planning.md | 0 | 3048 | `c04a41a1ee7c3e2de39fbb671abc9925c9403615a3de8606e9d3815f0ae3b794` |
| `gemini:docs/cli/tutorials/web-tools.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/web-tools.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/tutorials/web-tools.md | 0 | 2524 | `72b60e4b4a2b99e3b33230c4e496e5fec0ff9424d0145bc447dc6c257197d8c2` |
| `gemini:docs/cli/using-agent-skills.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/using-agent-skills.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/cli/using-agent-skills.md | 0 | 3044 | `17ba498a64dd181f9cb74e1039b06c4e8940cc17bb0970e275c318acaad5bc41` |
| `gemini:docs/core/gemma-setup.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/gemma-setup.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/gemma-setup.md | 0 | 3141 | `39a8e3db8f99a0f72a9e926d92254ad16c10f3d1e57a3007ba135f67493dc6ed` |
| `gemini:docs/core/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/index.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/index.md | 0 | 5043 | `38fc5c42dcd681285c59e4915333d6db84a66ce6b322fd71806f53fcb6e93fb3` |
| `gemini:docs/core/local-model-routing.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/local-model-routing.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/local-model-routing.md | 0 | 7149 | `a0746424a484dbcb0952db3c775d6e0b30399a3f3837b7f36a306ea4c8ee62ed` |
| `gemini:docs/core/remote-agents.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/remote-agents.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/remote-agents.md | 0 | 17049 | `8dd736d4ad31ffdb3ef8736746da31935b00fffaa37de07408827bf36d6fc2aa` |
| `gemini:docs/core/subagents.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/subagents.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/core/subagents.md | 0 | 23610 | `1a1b38993a2f5c6e16afda1914974a86274e73fac90e3ab62334d45e34bf7849` |
| `gemini:docs/examples/proxy-script.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/examples/proxy-script.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/examples/proxy-script.md | 0 | 2823 | `365fdeb71a8baf51b4793df6ab9a71e5fe6e6a99a5f2372c8660d0525352e8ba` |
| `gemini:docs/extensions/best-practices.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/best-practices.md | `Fri Oct 23 12:10:42 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/best-practices.md | 0 | 5801 | `ea5d066016310aa7cc20b00f8d717feb0f815649d0f40b7cd0b9550dfe273bab` |
| `gemini:docs/extensions/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/index.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/index.md | 0 | 1781 | `ba0bfc2f0dde9d780e29ad2b37446eeeff7c760052682c0f25e592a02bbffecf` |
| `gemini:docs/extensions/reference.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/reference.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/reference.md | 0 | 12029 | `cf42a742ae7476faaf96a79fbcf462d86c1845fa6a2c0f39930d96559e284d34` |
| `gemini:docs/extensions/releasing.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/releasing.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/releasing.md | 0 | 7622 | `94b07a2ac657790e8b8094452f19bbfcc156e1e595fccc5ee15f9b5852742dfe` |
| `gemini:docs/extensions/writing-extensions.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/writing-extensions.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/extensions/writing-extensions.md | 0 | 12332 | `f298c787f9ba4173fd288fab86d1686c2982e7dda5e1651ca93435fea91d986f` |
| `gemini:docs/get-started/authentication.mdx` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/authentication.mdx | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/authentication.mdx | 0 | 15046 | `8a2eb3910788d931b0892f2cc5d188f6f0dd4602349767db307df2b242bbfd5f` |
| `gemini:docs/get-started/gemini-3.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/gemini-3.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/gemini-3.md | 0 | 4616 | `c8912d310b801f86e8b59f00e35dfbb439e49f66538aad39605f12ef1bebc0f0` |
| `gemini:docs/get-started/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/index.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/index.md | 0 | 6337 | `c74c971c45e16021738e66ac89766e7c4ea43dee69996780df6238616c0beb51` |
| `gemini:docs/get-started/installation.mdx` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/installation.mdx | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/get-started/installation.mdx | 0 | 5630 | `ec1cc36ade6cc1590fecc6029fbf190922ad42b5d93ebbec04d0466304359901` |
| `gemini:docs/hooks/best-practices.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/best-practices.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/best-practices.md | 0 | 17651 | `7d9ba054f3b227ced18db33f184da0eec9117966093a30dadbce15b75a6d79e2` |
| `gemini:docs/hooks/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/index.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/index.md | 0 | 8342 | `3d3eed03c5394c59e91d714f94015735a9697bef4d7c84796d8d6302b16a640c` |
| `gemini:docs/hooks/reference.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/reference.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/reference.md | 0 | 13319 | `103bab9f0f8fd7251b97d06c6b7c4e52752427bf23cbacd1379f2aecaaf26e4c` |
| `gemini:docs/hooks/writing-hooks.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/writing-hooks.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/hooks/writing-hooks.md | 0 | 11539 | `de4d2d8920ddf40354562b335921933287faaa8b6db10ba053b727081039afee` |
| `gemini:docs/ide-integration/ide-companion-spec.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/ide-integration/ide-companion-spec.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/ide-integration/ide-companion-spec.md | 0 | 10821 | `143b49bbf7817cc5d6c8c3c6e3e1b255cb2a0f4c710a039d756cf8028c68cd91` |
| `gemini:docs/ide-integration/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/ide-integration/index.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/ide-integration/index.md | 0 | 13249 | `f64abac0a339b47599272ccf0d0eb4a42d72ecf1b77af433b1f45cb763d3f661` |
| `gemini:docs/index.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/index.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/index.md | 0 | 5910 | `a99fc6bf1c1ba19c6de5fdfd6470982bd8746ad6d0153e8d07d96d3957921e5d` |
| `gemini:docs/integration-tests.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/integration-tests.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/integration-tests.md | 0 | 8530 | `1939abc1f2b7aedbc7184132a1467cbc929cf3b674856a478357a5b051b4ed06` |
| `gemini:docs/issue-and-pr-automation.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/issue-and-pr-automation.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/issue-and-pr-automation.md | 0 | 10043 | `faf0360d6e7e8c6d48cbe1b80f712e22e02e8961daf36f517b3a85e79b4a35a9` |
| `gemini:docs/local-development.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/local-development.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/local-development.md | 0 | 4889 | `80cf294a2a9d4e33ae6178c80b8d667134050ab81c9744f5097c3433db672b0b` |
| `gemini:docs/npm.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/npm.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/npm.md | 0 | 2544 | `2ee05cabd896a5e3bc9e37b57e3d5fd61e8cdf30a10baa746ca7e69ea41c86c3` |
| `gemini:docs/reference/commands.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/commands.md | `Fri Oct 23 12:10:43 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/commands.md | 0 | 24289 | `8e3c5433d6c96bcf53c8bc4504138c19e941cba7d5363fd9dac947c5647c4abf` |
| `gemini:docs/reference/configuration.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/configuration.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/configuration.md | 0 | 102685 | `4b86e73ee6da5b18ec0515c3fbf12b9b72fb07fbb545fa93362507596cbc64f4` |
| `gemini:docs/reference/keyboard-shortcuts.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/keyboard-shortcuts.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/keyboard-shortcuts.md | 0 | 23917 | `ebce6750916d66c587fa9370d2d98ee6948de936463bb2db02cc121ef8411648` |
| `gemini:docs/reference/memport.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/memport.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/memport.md | 0 | 6382 | `eb2737b49776e97e5b967114c50150d42d7c45606c0fbccc24b9bc8d8ab6da11` |
| `gemini:docs/reference/policy-engine.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/policy-engine.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/policy-engine.md | 0 | 19414 | `4895bc05bccef1a16ab1442c7a9b12ebe61945f0f079e9fca3261cf8b9e2d0f5` |
| `gemini:docs/reference/tools.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/tools.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/reference/tools.md | 0 | 18029 | `24f63ba1a361baca3e3141cf059751b8b6218d06c0145516db41967bcbac0b31` |
| `gemini:docs/release-confidence.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/release-confidence.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/release-confidence.md | 0 | 5455 | `f514bbe0a116a40410983647f57ee2e7dae527791d756a8e62c37f4efd0d1999` |
| `gemini:docs/releases.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/releases.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/releases.md | 0 | 23251 | `c50335efe3dce02254275e113e5c380848b5d62e2ca0058e89e58548584e7059` |
| `gemini:docs/resources/faq.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/faq.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/faq.md | 0 | 8089 | `74928afb51ad73cf1170edebf68f5782ed829e1ef2e69f36dd679a594ac51070` |
| `gemini:docs/resources/quota-and-pricing.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/quota-and-pricing.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/quota-and-pricing.md | 0 | 9148 | `b843e3c26e76f53e3a667d86c9b0bde92dcfb7ebadc0a7924f75979eaf3428e4` |
| `gemini:docs/resources/tos-privacy.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/tos-privacy.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/tos-privacy.md | 0 | 6658 | `522e2c6fc73f4d736c13118e4ef1bd4e9ce48b2562ec385bac4c53d145b2c073` |
| `gemini:docs/resources/troubleshooting.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/troubleshooting.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/troubleshooting.md | 0 | 10459 | `2d11eec3cf098af919a97c87cc3ecd313bd9e6ac9b7df2b706b21e052413f784` |
| `gemini:docs/resources/uninstall.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/uninstall.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/resources/uninstall.md | 0 | 1540 | `839d715ea05f2cd14c2b008bff070c60a39627bdc4faf59f5bde29d4c9169117` |
| `gemini:docs/tools/activate-skill.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/activate-skill.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/activate-skill.md | 0 | 1515 | `90abfd1b806a09c086c46eb17115636d81167850e1e5e1556062aa380d7fb30c` |
| `gemini:docs/tools/ask-user.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/ask-user.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/ask-user.md | 0 | 2821 | `0783a882a536c095a0d1600515192b79b89c15a1f5635bfeaaba8cc591fc0084` |
| `gemini:docs/tools/file-system.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/file-system.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/file-system.md | 0 | 5151 | `bcdf392eddc135811976d045f19f8a2d782003fa528add7c98f3a6e59a97ef3b` |
| `gemini:docs/tools/internal-docs.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/internal-docs.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/internal-docs.md | 0 | 1683 | `ff2712ba8a9af421fa36d0095ad7ff8b59b6564a4a47875a4727939474501283` |
| `gemini:docs/tools/mcp-resources.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/mcp-resources.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/mcp-resources.md | 0 | 1781 | `afd0283a49c6f585a6f43885f39fdd833aa543b8b0e12356facc3ead49c9d237` |
| `gemini:docs/tools/mcp-server.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/mcp-server.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/mcp-server.md | 0 | 44112 | `9e4608980e3adf50d39c6b336536829257f45f48a83f5e7e677a622929693b46` |
| `gemini:docs/tools/memory.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/memory.md | `Fri Oct 23 12:10:44 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/memory.md | 0 | 1185 | `f441a575c49c629875423e76476454f24e5bee8e9aa71a8453f0993e310f54e1` |
| `gemini:docs/tools/planning.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/planning.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/planning.md | 0 | 2639 | `cf7e5c9d383c2912858cd8ae61edd818ed8a7634c1cbaf465dc0b0ce08fda119` |
| `gemini:docs/tools/shell.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/shell.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/shell.md | 0 | 7944 | `7e9649ff91274b23cc05c0af8e4aec31f2d832439d448e61e5b47f964c2de5dd` |
| `gemini:docs/tools/todos.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/todos.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/todos.md | 0 | 1246 | `ac1f3d58ea3bad6bc78ac958d39fa3345a6268fb6343a58a7b330db573ee5e67` |
| `gemini:docs/tools/tracker.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/tracker.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/tracker.md | 0 | 2610 | `c06f28126df09d9dfefed8b40534bc48f2cba293babe5ce3f7fc5d4db1e9bb89` |
| `gemini:docs/tools/web-fetch.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/web-fetch.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/web-fetch.md | 0 | 1682 | `1881535b18fc9786f5e3afd74c066161296fc9b1086dfcef4e6087891cf17b9e` |
| `gemini:docs/tools/web-search.md` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/web-search.md | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/docs/tools/web-search.md | 0 | 1149 | `3f528d5410cba40e0816e28497c3d13e7b5443c5c6002808c054fbce4f5b6908` |
| `opencode:packages/web/src/content/docs/acp.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/acp.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/acp.mdx | 0 | 3782 | `dd4db9108c5c239c1df4454e3392a7a1d061e3d2c465c6640332f890b28ee414` |
| `opencode:packages/web/src/content/docs/agents.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/agents.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/agents.mdx | 0 | 21066 | `1f805f8a7cd1d877272d61ad6d59dae4d014c7b26009110d1c4b26c65a634dcc` |
| `opencode:packages/web/src/content/docs/cli.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/cli.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/cli.mdx | 0 | 32048 | `cbadf869da555205cd9419ae75a421de9ef4bca5a89117be602c7038d02ac9dc` |
| `opencode:packages/web/src/content/docs/commands.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/commands.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/commands.mdx | 0 | 6712 | `853516ad84f3cf9c2c09b9ddb72a1b44c98eac072db4c2712434259bbd8bd93c` |
| `opencode:packages/web/src/content/docs/config.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/config.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/config.mdx | 0 | 26473 | `61701752764534dec13663edf44945c60bb3b4672a6f24291f5c3c5d23d8647d` |
| `opencode:packages/web/src/content/docs/custom-tools.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/custom-tools.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/custom-tools.mdx | 0 | 4930 | `0a5df35e96df711324244d91fc3d16001bca81cea5b91f86207a8fc55f1209fc` |
| `opencode:packages/web/src/content/docs/ecosystem.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/ecosystem.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/ecosystem.mdx | 0 | 10676 | `ef3b0b22c9973698ed182dc4ee09979049eacb6d9436f106715b74b6372c0ea9` |
| `opencode:packages/web/src/content/docs/enterprise.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/enterprise.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/enterprise.mdx | 0 | 4930 | `83c66a699996c05bfb67d374b094bf30b3002700d74feb6e6ac9f020bd5b9bd8` |
| `opencode:packages/web/src/content/docs/formatters.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/formatters.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/formatters.mdx | 0 | 9814 | `ccac419e2ecd738048f52d6a268a82ce408c98328c690fcdc6114602a14c9de7` |
| `opencode:packages/web/src/content/docs/github.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/github.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/github.mdx | 0 | 12065 | `f80b6a3bfe9411dab2340106d8d74945c51e5e8f42459d055544e85d18d4bd26` |
| `opencode:packages/web/src/content/docs/gitlab.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/gitlab.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/gitlab.mdx | 0 | 6629 | `e03edeed17566d997a5b89d7771a472b8486da959dd33a071a17c375e0cb6311` |
| `opencode:packages/web/src/content/docs/ide.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/ide.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/ide.mdx | 0 | 1583 | `adda70c2cff634a861d6f927d4868c2c8ae5f5ccb87034bcb158ac1035473ecd` |
| `opencode:packages/web/src/content/docs/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/index.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/index.mdx | 0 | 8440 | `d0e47562392876b0d7482156685c781dc9ce79404cf4d559cf485025618eb0e1` |
| `opencode:packages/web/src/content/docs/keybinds.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/keybinds.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/keybinds.mdx | 0 | 9747 | `bd0a018a9da07e524adf40705c16fa32c54f7018c89eaa5d0b7a00e26ab2ade2` |
| `opencode:packages/web/src/content/docs/lsp.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/lsp.mdx | `Fri Oct 23 12:10:45 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/lsp.mdx | 0 | 10612 | `740c3558dd93047ce7d832111362e61ddcffebb4c7580a2e0f7db41c73798399` |
| `opencode:packages/web/src/content/docs/mcp-servers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/mcp-servers.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/mcp-servers.mdx | 0 | 14802 | `cd7651cdcd7f485926a6756869bfb34bbc415fcd75398b36481a943594236cfc` |
| `opencode:packages/web/src/content/docs/models.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/models.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/models.mdx | 0 | 5554 | `f3be1c5e087107c68fcc88277c2e5f81295bcb7180a28102a7285b728281c81a` |
| `opencode:packages/web/src/content/docs/network.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/network.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/network.mdx | 0 | 1413 | `3fe58939d928838b9944a215e090f093dd12032ca3d58583cd4c00197174f2d6` |
| `opencode:packages/web/src/content/docs/permissions.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/permissions.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/permissions.mdx | 0 | 7627 | `df4e3560a1c7cb928dd798874004f68c61573ac586447d040742261181b70162` |
| `opencode:packages/web/src/content/docs/plugins.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/plugins.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/plugins.mdx | 0 | 9473 | `4cc0d8db8645a036d1398a9e3be65c386ab75d003a2699c14bc06c267ea1354f` |
| `opencode:packages/web/src/content/docs/policies.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/policies.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/policies.mdx | 0 | 4150 | `05dc12f06ba4f663287600f2d06327dd38741da3a7337bf8be4a52460af77e0f` |
| `opencode:packages/web/src/content/docs/providers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/providers.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/providers.mdx | 0 | 66903 | `8c72ab58b340f0158836f97c3b86b7db31a3f4362b57e0faade740a9105b727c` |
| `opencode:packages/web/src/content/docs/references.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/references.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/references.mdx | 0 | 4551 | `e2ba34b82bfef747618792dbd83dc6bafab3f13e5e8676f3cbfa883a99a7929e` |
| `opencode:packages/web/src/content/docs/rules.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/rules.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/rules.mdx | 0 | 6758 | `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9` |
| `opencode:packages/web/src/content/docs/sdk.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/sdk.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/sdk.mdx | 0 | 20421 | `a19667903d2dce2154983aada75382aac07f1dbd73600e7f8b6d7e5b4b05cca9` |
| `opencode:packages/web/src/content/docs/server.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/server.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/server.mdx | 0 | 17881 | `dbd4f6bd27df5c249f3d63d9500be08f9f330c57ec3facf9ba84c12702327dbc` |
| `opencode:packages/web/src/content/docs/skills.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/skills.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/skills.mdx | 0 | 4727 | `95f88d31438a5c046335310d07aa36733a257502798cab1fe26298c1a27b46e4` |
| `opencode:packages/web/src/content/docs/themes.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/themes.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/themes.mdx | 0 | 9853 | `5ccead60e73e32388c91769d629245162af2f6eb34c98007c8c87b9385487819` |
| `opencode:packages/web/src/content/docs/tools.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/tools.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/tools.mdx | 0 | 8543 | `75a27986eb21ec76fb3514f2b553d2a291f3a71a4b3ec69a1426ad8978d46d98` |
| `opencode:packages/web/src/content/docs/troubleshooting.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/troubleshooting.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/troubleshooting.mdx | 0 | 9560 | `3616ffc3d43f9fc14504e784c1f8ed390bbd8d25ff5c49fdd34cdb11e49bb493` |
| `opencode:packages/web/src/content/docs/tui.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/tui.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/tui.mdx | 0 | 9835 | `b5f12cd811558323c314bbb811461927b68a72f8bff514a345817e417ff6be6b` |
| `opencode:packages/web/src/content/docs/web.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/web.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/web.mdx | 0 | 3280 | `6a7501225b5ed7118dd756540e9e7430b54480522a2a3193ca4a55bc4ad0a30e` |
| `opencode:packages/web/src/content/docs/windows-wsl.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/windows-wsl.mdx | `Fri Oct 23 12:10:46 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/packages/web/src/content/docs/windows-wsl.mdx | 0 | 3052 | `e236a7225fa7cd391737d207d4e299117db6c5efcfb2c6165d9dadc81dd1a510` |
| `opencode:services/www/src/docs/content/agents.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/agents.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/agents.mdx | 0 | 8779 | `6cca5b0a5a88387e94177d9c13d2e539fb710d69b2298ca6d44b9bc465c8b57a` |
| `opencode:services/www/src/docs/content/attachments.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/attachments.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/attachments.mdx | 0 | 6556 | `7243b6aa6914d3a56919131831c91ace4b486f490d0b26e44af796e36f11f4fc` |
| `opencode:services/www/src/docs/content/build/client/effect.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/client/effect.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/client/effect.mdx | 0 | 5103 | `afa74f67ce6528983ef282673fcadaf6a9d67e6b1e5a699c730d54e0e17b3f45` |
| `opencode:services/www/src/docs/content/build/client/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/client/index.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/client/index.mdx | 0 | 6177 | `270736528ef5f966340cbf95152654719ff5f900b7a223d62a9514bfc3d0eaff` |
| `opencode:services/www/src/docs/content/build/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/index.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/index.mdx | 0 | 958 | `afd045b82ef46975e422f4abfb7ebc6bb9f800b2cbbd76e007d9d5b1e0a7ce8a` |
| `opencode:services/www/src/docs/content/build/plugins/cli.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/cli.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/cli.mdx | 0 | 21958 | `5c4b178762e33563a96df0b710e8171e4dc7dab7e257e8c2e753040cb44feb22` |
| `opencode:services/www/src/docs/content/build/plugins/effect.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/effect.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/effect.mdx | 0 | 50709 | `69785b10e371cbc9acb91110bdc538db8950b7b2c508fe1e2bc819819f797b19` |
| `opencode:services/www/src/docs/content/build/plugins/effect/rpc.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/effect/rpc.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/effect/rpc.mdx | 0 | 3876 | `a5e08204f13bcd69e80223000f0f32ac2de5b96e62f9611a70dfee3b55004c87` |
| `opencode:services/www/src/docs/content/build/plugins/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/index.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/index.mdx | 0 | 60780 | `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5` |
| `opencode:services/www/src/docs/content/build/plugins/migrate-v1.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/migrate-v1.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/migrate-v1.mdx | 0 | 15100 | `9ac058db236908db691e9b5337d27b3178c5b44eca478ab84c59c8cafc65d510` |
| `opencode:services/www/src/docs/content/build/plugins/rpc.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/rpc.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/plugins/rpc.mdx | 0 | 5582 | `a3f4cab20e9aa542cd278296c4a7dd47123a262f0e91813f65991a12f77a3770` |
| `opencode:services/www/src/docs/content/build/sdk/cloudflare.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/cloudflare.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/cloudflare.mdx | 0 | 2462 | `50913a2d7adc54fba68fea97129aac4620c7df599c1e73d1e75cfb1634ddd88e` |
| `opencode:services/www/src/docs/content/build/sdk/effect.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/effect.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/effect.mdx | 0 | 2674 | `0c60c483dac3233776cb2dcf438aabe7ab5f705c2f64fc9bb63f83f0bb731a63` |
| `opencode:services/www/src/docs/content/build/sdk/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/index.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/build/sdk/index.mdx | 0 | 3053 | `2238d5757307d20033bfced4ba331c59771aa76329600ea7ec59d396e225ade3` |
| `opencode:services/www/src/docs/content/cli/acp.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/acp.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/acp.mdx | 0 | 18213 | `8fbbebf1fb509e802280b8a9e6502069d80f897568b0b76eaac9f9993019dc99` |
| `opencode:services/www/src/docs/content/cli/commands.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/commands.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/commands.mdx | 0 | 9882 | `9e980f9cc2559ec3e88769f30525bda451c0c2b92b1d9f49f33cafb0105a6d5f` |
| `opencode:services/www/src/docs/content/cli/config.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/config.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/config.mdx | 0 | 18967 | `1dd9d6db3541194f16c02ffce3cefe7513f5d08112177e2c1d0f87abb5a26fae` |
| `opencode:services/www/src/docs/content/cli/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/index.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/index.mdx | 0 | 3232 | `d935f6c8ef6f215b15823c94184fab52947796b8dedd442a4410ffbde9110532` |
| `opencode:services/www/src/docs/content/cli/keybinds.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/keybinds.mdx | `Fri Oct 23 12:10:47 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/keybinds.mdx | 0 | 30654 | `20ed9b99d41f48d4bdca32ade5782ae44ca6e82e5e10787c0d8fb07d71619a0d` |
| `opencode:services/www/src/docs/content/cli/plugins.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/plugins.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/plugins.mdx | 0 | 1779 | `3bdd07b84485f03fd53a8f2e60a4a62fcf64e2de877aa18907262de017827388` |
| `opencode:services/www/src/docs/content/cli/providers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/providers.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/providers.mdx | 0 | 5013 | `42dc135d88952baef3653f2ae368593e3796b3cacba528d878b75047f600e8ca` |
| `opencode:services/www/src/docs/content/cli/theme.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/theme.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/theme.mdx | 0 | 7731 | `7412ec5b5ff22af5c7fe6a09a326145d915171b60139464ac725cd1378afbecb` |
| `opencode:services/www/src/docs/content/cli/tui.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/tui.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/tui.mdx | 0 | 3363 | `3ac27d5867b8bdcf550216259b53dd9ecac97a9b8993f464d483110b4d65ffcd` |
| `opencode:services/www/src/docs/content/cli/web.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/web.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/cli/web.mdx | 0 | 3545 | `54cd56b0166aa80683921cbc32beb074a41969177691e10c5c867df621f3e2fa` |
| `opencode:services/www/src/docs/content/commands.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/commands.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/commands.mdx | 0 | 7242 | `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` |
| `opencode:services/www/src/docs/content/compaction.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/compaction.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/compaction.mdx | 0 | 7925 | `d10e5bb06a3d6857a52e7ebe16f183ca342481feb6e75264fe314e570decc662` |
| `opencode:services/www/src/docs/content/config.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/config.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/config.mdx | 0 | 16687 | `15e0fc4dc6ff1d5b305b6bebfd34d8a00e175ce60911f80277dea7e50f311d98` |
| `opencode:services/www/src/docs/content/console/api/budgets.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/budgets.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/budgets.mdx | 0 | 4278 | `f892b12162555ea0c851c6a4e96426f3755a418acb9fa4602b91a487e2816af2` |
| `opencode:services/www/src/docs/content/console/api/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/index.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/index.mdx | 0 | 8310 | `8537ce2c6bdf8e10d3fec560907e94192347ea1b319aecf7b40285501732972f` |
| `opencode:services/www/src/docs/content/console/api/inference.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/inference.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/inference.mdx | 0 | 3276 | `e455d6447af0d75e477f6f780d54dc5ebf4b65a3182aa184f2666bec9a292b4f` |
| `opencode:services/www/src/docs/content/console/api/providers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/providers.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/api/providers.mdx | 0 | 3462 | `3be18b4ecd072e1b220b48f0d5ff4e7b18184cae0f60b3dfe9809835ef0157c4` |
| `opencode:services/www/src/docs/content/console/billing.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/billing.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/billing.mdx | 0 | 2844 | `ccc28ec810ba9146731fe0ae41116e59f621019094f6ce6b72ac2760f9189614` |
| `opencode:services/www/src/docs/content/console/budgets.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/budgets.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/budgets.mdx | 0 | 4470 | `938c3ef2297d3915a58d3cca3df45e9ee0e8bff99253573a03a54fcf2de229b1` |
| `opencode:services/www/src/docs/content/console/go.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/go.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/go.mdx | 0 | 44363 | `2da01588d03f9a95ae90fbe030c7bbec8ff4c5e56b7475a096701e843539ecfb` |
| `opencode:services/www/src/docs/content/console/harnesses/claude-code.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/claude-code.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/claude-code.mdx | 0 | 2991 | `e973cbea9fb9077adee299406ac1e9f76141cf6ff4dd8982a6041d26fbd22d63` |
| `opencode:services/www/src/docs/content/console/harnesses/codex.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/codex.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/codex.mdx | 0 | 2636 | `60cba77096da2040c437fb57cf2bbf86ee25407581b592b5b48acac5f8ee82e1` |
| `opencode:services/www/src/docs/content/console/harnesses/hermes.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/hermes.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/hermes.mdx | 0 | 1800 | `8edb329aebba0884b054acfbc6032aa5c52f898051009b88b93176941466884a` |
| `opencode:services/www/src/docs/content/console/harnesses/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/index.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/index.mdx | 0 | 4592 | `d167a97a06458584fac8c8af4fa1b5f346c226df5b7751585bac1b5128008afd` |
| `opencode:services/www/src/docs/content/console/harnesses/pi.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/pi.mdx | `Fri Oct 23 12:10:48 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/pi.mdx | 0 | 1694 | `eb310b4ac6768d9271cb56c93928cd35d0ad38a5bcb092c74942bf4d97cca4e7` |
| `opencode:services/www/src/docs/content/console/harnesses/raycast.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/raycast.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/harnesses/raycast.mdx | 0 | 1426 | `8b44a752863dab541c07230d4cc71008afaf2ef3f1c36fe0af94b57b5c9cf824` |
| `opencode:services/www/src/docs/content/console/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/index.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/index.mdx | 0 | 1556 | `43b82abe0427fdd6f7fdc1bb2fe21e1b16517406e536b8731dc66adc160b2c06` |
| `opencode:services/www/src/docs/content/console/members.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/members.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/members.mdx | 0 | 3009 | `abf8b104cf300885d9c56498492bdfe101513c4f47b1d8e89e486257ffd3120b` |
| `opencode:services/www/src/docs/content/console/models.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/models.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/models.mdx | 0 | 38343 | `ead0e300895f0ac2c698bb084985216d53a982e37325c81a766de71d2999af0a` |
| `opencode:services/www/src/docs/content/console/providers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/providers.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/providers.mdx | 0 | 5561 | `21be2082180799df4a952efa8bd71e4c2e98f2626cdc91d046cae8675fb5df18` |
| `opencode:services/www/src/docs/content/console/scim.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/scim.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/scim.mdx | 0 | 3837 | `0668eda2d83d3e759a996e92cf1f04d3a5ce26d885ce846dfac13cbbe209edd7` |
| `opencode:services/www/src/docs/content/console/sso.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/sso.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/sso.mdx | 0 | 4207 | `b58f82bb878f960dced1afdc57dad552f91de1421da649fa68694b99469e4006` |
| `opencode:services/www/src/docs/content/console/websearch.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/websearch.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/websearch.mdx | 0 | 1785 | `8c03d3d4e9a567250c438be0a0a7134d1b05752e2791aa39973cf436889ac700` |
| `opencode:services/www/src/docs/content/console/workspaces.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/workspaces.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/console/workspaces.mdx | 0 | 3933 | `fcc5235f3bcf3f2a70deb4394f65417bc5c7c35df3fc492d8402524daca17658` |
| `opencode:services/www/src/docs/content/formatters.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/formatters.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/formatters.mdx | 0 | 6131 | `a754fd93ab60b3068070886a9d242cdaf12c78d883400264089165ba04368d5a` |
| `opencode:services/www/src/docs/content/index.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/index.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/index.mdx | 0 | 4926 | `ec1bd2c1aedf1faf300c8343ab7ef314ee1328a94dae52085de278682711720b` |
| `opencode:services/www/src/docs/content/instructions.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/instructions.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/instructions.mdx | 0 | 5634 | `7c767eb7433054c47549b8e28e1d934aee40e1b36fdf09d777a04062c2958895` |
| `opencode:services/www/src/docs/content/mcp-servers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/mcp-servers.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/mcp-servers.mdx | 0 | 15476 | `fd3b05ead1ecfde68181f90507cbb616f5cd3d5fa360494b4e261e4b9f3627a2` |
| `opencode:services/www/src/docs/content/migrate-v1.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/migrate-v1.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/migrate-v1.mdx | 0 | 20805 | `f3d42b36cec1b498d19543b32e72a069e006ee2a4a6884e548ce3a9408fd78a0` |
| `opencode:services/www/src/docs/content/models.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/models.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/models.mdx | 0 | 15539 | `3224817dd3153bf39ce35cb1e5174d49d16ade9effbb5feb6406f1f478888b23` |
| `opencode:services/www/src/docs/content/network.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/network.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/network.mdx | 0 | 3370 | `e70878768a50d5aefe5e9b18c78ae53296e40c8b7c679c66ccf0675589ab2b2c` |
| `opencode:services/www/src/docs/content/permissions.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/permissions.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/permissions.mdx | 0 | 12068 | `264c0f179b8cd29194d0e1552c65e42f74699f42fdc02d6990c9016769254957` |
| `opencode:services/www/src/docs/content/plugins.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/plugins.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/plugins.mdx | 0 | 4371 | `39afa29948069c9e8d95ba812ee1701535912a7e5ce3ed7fef5d4ba6d7521fd3` |
| `opencode:services/www/src/docs/content/policies.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/policies.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/policies.mdx | 0 | 9539 | `6e533bea017bb5c945aba6decb4b4655eb663bd5f2db4fa0fe7f9a19c9220557` |
| `opencode:services/www/src/docs/content/providers.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/providers.mdx | `Fri Oct 23 12:10:49 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/providers.mdx | 0 | 23164 | `4f19df27aba970a602150f16cb569dfabbc0b9b7973897b026664a5e9b40c236` |
| `opencode:services/www/src/docs/content/references.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/references.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/references.mdx | 0 | 7012 | `cd24a7bf489a87abc3172fff654b8e471e95f478bc12ff079164bb003931eb36` |
| `opencode:services/www/src/docs/content/skills.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/skills.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/skills.mdx | 0 | 9187 | `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b` |
| `opencode:services/www/src/docs/content/snapshots.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/snapshots.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/snapshots.mdx | 0 | 4876 | `e1925ab71776c2e79b420f7bb72f8331c9902fc390acc4aacf52956d86c7df8a` |
| `opencode:services/www/src/docs/content/themes.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/themes.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/themes.mdx | 0 | 7657 | `352d2bf3700aa0a9956c770c80a487d25368f9fa39e5a94dbcc426fcd98248ce` |
| `opencode:services/www/src/docs/content/tools.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/tools.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/tools.mdx | 0 | 10268 | `85eea8ebbc447e4a71259ad6ca2db96c0ef6b41236ed600e3e599f787c3bc91a` |
| `opencode:services/www/src/docs/content/troubleshooting.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/troubleshooting.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/troubleshooting.mdx | 0 | 7714 | `f77ae5067c021a41513497e630dc32003f7ceaa481a82bdc30e94c40a8d54ddd` |
| `opencode:services/www/src/docs/content/warming.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/warming.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/warming.mdx | 0 | 3857 | `68ea79bb5b59fecc75367160607f30be7050337269966813680f9607fc96a274` |
| `opencode:services/www/src/docs/content/websearch.mdx` | https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/websearch.mdx | `Fri Oct 23 12:10:50 PM UTC 2026` | 200 https://raw.githubusercontent.com/anomalyco/opencode/4232b8bcd624965b2c35fa39c50e7fe9ae8b6f1f/services/www/src/docs/content/websearch.mdx | 0 | 2518 | `991c6df05933357444753307a6225ba6d67f760956ba4aeb9a4b0f83bcd00653` |
| `gemini_contributing` | https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/CONTRIBUTING.md | `Fri Oct 23 12:11:19 PM UTC 2026` | 200 https://raw.githubusercontent.com/google-gemini/gemini-cli/a713410aba5d594594e20d5c822e3aab8f822089/CONTRIBUTING.md | 0 | 20400 | `b9cd98e07df3d36ba7267e5a5edeae1166d85e78b41ff1d960648f5d3bed60c0` |
| `vscode_harnesses` | https://code.visualstudio.com/docs/agents/concepts/agent-harnesses.md | `Fri Oct 23 12:11:19 PM UTC 2026` | 200 https://code.visualstudio.com/docs/agents/concepts/agent-harnesses.md | 0 | 12091 | `4b6511928c80d3b34d2c98a6dfaf167eacee16a974363a2878bd32428cecdf2c` |
| `codex_release_tag` | https://github.com/openai/codex/releases/tag/rust-v0.164.0 | `Fri Oct 23 12:11:19 PM UTC 2026` | 200 https://github.com/openai/codex/releases/tag/rust-v0.164.0 | 0 | 463639 | `4ea2a41d7202e03720cefdb4f05fb74d95aa86453444fa42bd5378cfae5f3312` |

Report: .ufo/waves/round-60/build/CriticCensus.md
