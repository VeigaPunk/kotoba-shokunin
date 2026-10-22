Result: DONE — VS Code's Local harness reads `.github/copilot-instructions.md`, `AGENTS.md` (root, plus nested when enabled) and `CLAUDE.md` in four locations, treats all applicable sources as additive with no general precedence order, and documents neither a `GEMINI.md` file, an `@AGENTS.md` import, a symlink redirect, a size cap, nor a dating rule; six SOURCES rows drafted, four marker probes rejected.

Round 53, wave 1 (build), C2 source basis. Seat `KotobaR53.ScribeVSCode`. Target client: Visual Studio Code / GitHub Copilot Chat (`code.visualstudio.com` docs and `microsoft/vscode-docs`). Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` (verified in the sandbox clone). Nothing in the lane was written except this file; all fetched bytes live under `/fast/scratch/hyaku/kotoba-r53/ScribeVSCode/scratch/vscode/`. No tool was installed or upgraded (nothing was needed); no model call of any kind was made; no editor or client binary was executed.

## 0. Method and provenance

- Every source was opened with `curl -sS -L -A "Mozilla/5.0" -o <file> -w '<status> <bytes>'`, then `sha256sum`. UTC timestamps are from `date -u` immediately before and after each batch.
- The docs source tree was pinned at `microsoft/vscode-docs` `main` tip `fd64d64891a2e660bcc0d32ea402da905adfef7f` (`git ls-remote https://github.com/microsoft/vscode-docs refs/heads/main`, 2026-10-22T20:05:31Z, exit 0). The render of the custom-instructions page was re-fetched at that explicit commit (`pinned-custom-instructions.md`, 200, 25,213 B, sha256 `eb2be087…`) and `cmp -s` against the `main` fetch printed `IDENTICAL` (exit 0).
- The whole-tree control for the Q30 negatives is the codeload tarball of that commit: `https://codeload.github.com/microsoft/vscode-docs/tar.gz/fd64d64891a2e660bcc0d32ea402da905adfef7f`, 2026-10-22T20:07:20Z, HTTP 200, 35,508,770 B, sha256 `6732e10c18b868f293eba88fa1cb83c1c1d605b4e0eaa7686eef496b7ba63468`, extracted to `docs-tree/vscode-docs-fd64d64891a2e660bcc0d32ea402da905adfef7f` (8,886 files; 860 Markdown files; 156 release-note Markdown files).
- The rendered route and the docs source path diverge. The page is served at `/docs/copilot/customization/custom-instructions` (200, 162,008 B, sha256 `dc87f7c2…`), but its source file is `docs/agent-customization/custom-instructions.md`, and `docs/copilot/customization/custom-instructions.md` is a 404 in the repo. The site's Markdown view exists only at the source-directory route: `/docs/agent-customization/custom-instructions.md` (200, 23,423 B, sha256 `f7d67ca7…`, 365 lines); `/docs/agents/reference/ai-settings.md` (200, 65,274 B, sha256 `902fb594…`, 465 lines). The former rendered route `/docs/agent-customization/custom-instructions` still returns the byte-identical HTML page (200, 162,008 B, sha256 `dc87f7c2…`, re-fetched 2026-10-22T20:11:58Z), and its own `data-markdown-url` points at the `.md` route that works (`custom-instructions.html:1548`). This is the Q30 hazard: a row that anchors the rendered directory name (`copilot/customization`) would name a path neither the source tree nor the site's Markdown view has.
- Quoting convention: `custom-instructions.md:<line>` and `ai-settings.md:<line>` are lines in the pinned GitHub source files (fetched bytes); `v1_*.md:<line>` are lines in the pinned release-note source files; `custom-instructions.html:<line>` are lines in the rendered HTML; the Gate record also gives the site-Markdown line numbers where a `.md` view exists (they differ from the GitHub source because front matter and template lines differ). Every quote is a byte-exact substring, ≤25 words.

## 1. Answers for this client

### 1.1 Which always-on file names it reads

The page separates the **Copilot harness** (GitHub's own discovery) from the **Local harness** (VS Code settings). `custom-instructions.md:45`:

> Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`.

That sentence is scoped "For Local harness sessions" on the same line. The file-name set, with the mechanism that enables each:

| Name | Scope it is read at | Enabling mechanism (default) | Source |
|---|---|---|---|
| `.github/copilot-instructions.md` | repository root `.github/` | `github.copilot.chat.codeGeneration.useInstructionFiles` (`true`) for the Local harness; for Copilot sessions it is the project-wide guidance file, with no VS Code setting named | `custom-instructions.md:75-79`; `ai-settings.md:343` |
| `~/.copilot/copilot-instructions.md` | user-level, personal always-on | Copilot sessions, no VS Code setting named | `custom-instructions.md:89` |
| `AGENTS.md` | workspace root | `chat.useAgentsMdFile` (`true`) for the Local harness; Copilot harness discovery is separate | `custom-instructions.md:232`; `ai-settings.md:351` |
| nested `AGENTS.md` | subfolders | `chat.useNestedAgentsMdFiles` (`false`) plus `chat.useAgentsMdFile` | `custom-instructions.md:236-239`; `ai-settings.md:353` |
| `CLAUDE.md` | workspace root, `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md`, `CLAUDE.local.md` | `chat.useClaudeMdFile` (`true`) | `custom-instructions.md:248-257`; `ai-settings.md:352` |
| `.instructions.md` | `.github/instructions/**` and `.claude/rules` | **Targeted**, not always-on: `applyTo` / `paths` pattern, or `description` on demand | `custom-instructions.md:118`, `:127-136`, `:260`; `ai-settings.md:341-342` |

`:79` is explicit about the Local harness and `.github/copilot-instructions.md`:

> The Local harness also discovers this workspace file when `setting(github.copilot.chat.codeGeneration.useInstructionFiles)` is enabled.

The `CLAUDE.md` location table is at `:250-255`:
- `:252` — "`CLAUDE.md` in the root of your workspace"
- `:253` — "`.claude/CLAUDE.md` in your workspace"
- `:254` — "`~/.claude/CLAUDE.md` for personal instructions across all projects"
- `:255` — "`CLAUDE.local.md` for local-only instructions (not committed to version control)"

**`GEMINI.md`: not documented.** The string `GEMINI.md` (case-insensitive `gemini.md`) appears **zero** times in the rendered page, zero times in the 860 Markdown files of the pinned docs tree, and zero times in the 156 release-note files (§2.1). The page has a catch-all sentence at `:47` — "Some harnesses also recognize additional formats." — so the honest record is *VS Code's docs do not document `GEMINI.md`*, not *VS Code cannot read it*. Per Q30 the sweep is complete and the client can be recorded silent on the name; the weaker catch-all is noted so no entry claims an impossibility.

The Copilot harness's own discovery is delegated to GitHub's documentation (`:229` link). VS Code states only: "instructions are discovered at the repository root, the session's working directory, and intermediate directories between them" (`:229`).

### 1.2 What it does when two of them exist in one directory

It treats every applicable source as additive and does not define a winner. `custom-instructions.md:315`:

> Applicable instruction sources are additive. Do not depend on a file order or precedence rule to resolve conflicts because discovery and merge behavior can differ by harness.

For the Copilot harness, rendered HTML `custom-instructions.html:1938`:

> Copilot combines applicable instructions from `AGENTS.md` and other supported instruction files.

The same line continues: "Avoid conflicting guidance because there is no general precedence order between these files." `:317` says "Remove duplicate guidance and resolve contradictions at their source." and `:49` says "keep shared requirements consistent and avoid contradictory copies."

For the Local harness with both `AGENTS.md` and `CLAUDE.md` present, the page never states the joint outcome. Both settings default to `true` (`ai-settings.md:351`, `:352`), and the page says sources are additive (`:315`), so the reading is that both are discovered and attached. That composition is `[INFERENCE]`: no sentence names the `AGENTS.md` + `CLAUDE.md` pair. What *is* documented is that the client will not arbitrate between them.

### 1.3 Whether it honours a redirect

**No redirect form is documented for these files.**

- **`@AGENTS.md` import:** `grep -rn '@AGENTS'` over the whole pinned docs tree returns 0 hits (8,886 files). No VS Code page describes an `@` import inside `CLAUDE.md` or `AGENTS.md`.
- **Symlink:** `grep -rni 'symlink' --include=*.md` over the whole pinned tree returns 38 hits, all unrelated (worktree folder symlinks, C++ path caveats, Node debug flags); filtering for instruction/`AGENTS.md`/`CLAUDE.md`/`copilot` gives 0 (§2.2). No page states whether a symlinked `CLAUDE.md` is followed.
- **Config pointing at another name:** no name alias exists. The adjacent settings move or widen *locations*, not names:
  - `chat.instructionsFilesLocations` — "Configure custom instruction locations for the Local harness" (`ai-settings.md:340`, marked **deprecated**); default value lists `.github/instructions`, `.claude/rules`, `~/.copilot/instructions`, `~/.claude/rules`.
  - `chat.useCustomizationsInParentRepositories` (`ai-settings.md:347`, default `false`) — walks up to the repo root and collects "always-on instructions (`copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`)" (`docs/agent-customization/overview.md:189`), described in release notes 1.112 (`v1_112.md:168-172`).
  - `chat.includeReferencedInstructions` (`ai-settings.md:342`, default `false`) — "Automatically add instruction files referenced via Markdown links to chat requests." This is the only documented cross-file reference mechanism, it uses Markdown links rather than `@`, and it is off by default. `custom-instructions.md:73` says: "To reference files or URLs in instructions, use Markdown links."

So VS Code neither attests nor denies the two Claude Code redirect forms the C2 counter blesses; it documents a third, opt-in, link-based form instead. Under Q30 this client is *silent* on the `@AGENTS.md` import and symlink forms — the sweeps in §2.2 are complete.

### 1.4 Documented size limit

**None for any instruction file.** No character cap, token budget or truncation rule appears in the page, the settings reference, the 156 release-note files, or the docs tree. The only relevant text is authoring advice, `custom-instructions.md:332`:

> Keep your instructions short and self-contained.

That is guidance to the author, not a loader cap. Compare the neighbouring GitHub Copilot CLI/cloud docs, which at least state "Instructions must be no longer than 2 pages" inside a generation prompt (sibling report `ScribeCopilotCli.md` §2.4); VS Code states nothing numeric.

### 1.5 Anything about dated or transient content

**No rule.** Nothing forbids dates, expiring facts or live state in an always-on file. The nearest statements are maintenance advice:

- `docs/agents/guides/customize-copilot-guide.md:153` — "Update it when the architecture, commands, dependencies, or team practices change, and remove stale or duplicate rules."
- `docs/agents/guides/context-engineering-guide.md:250` — "Stale context leads to outdated or incorrect suggestions."

Both are generic review hygiene; neither says a dated sentence in `AGENTS.md` is a defect. Consequence for C2: alwayson.04 ("No dated or transient text; dates and live-state go to status files") is a lane craft rule with **no vendor attestation** from this client and must stay lane-authored in the instrument's detail string (Q20/Q23).

## 2. Q30 sweeps for the negatives

Three legs per negative: release notes, current docs source tree, lane corpus. The tree and release-note legs share the pinned tarball above (156 release-note files inside it). The corpus leg runs from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.

### 2.1 `GEMINI.md` not documented

- **Release notes:** `grep -rni 'gemini\.md' release-notes` → **0** hits (156 files). Case-insensitive `gemini` hits 16 lines, all model/provider names (e.g. `v1_97.md:139` "Gemini 2.0 Flash", `v1_117.md:126` "Gemini CLI" process detection); none is a rule file.
- **Docs source tree:** `grep -rni 'gemini\.md' .` → **0** hits (8,886 files). Rendered page: `grep -c GEMINI custom-instructions.html` → 0.
- **Lane corpus:** `grep -rni 'gemini\.md' corpus` → 7 hits, all round-13 harness-census rows about **omp/opencode** loaders (`corpus/knowledge/instruction-surface-census-round13.md:76,93,146,147,348,479`; `instruction-surface-remeasure-round13.md:38`); none mentions VS Code. No corpus entry records VS Code reading `GEMINI.md`.
- **Verdict:** VS Code's docs are silent on `GEMINI.md`; the sweep is complete. The catch-all at `custom-instructions.md:47` ("Some harnesses also recognize additional formats") is recorded so the entry does not overclaim.

### 2.2 `@AGENTS.md` import and symlink redirect not documented

- **Release notes:** `grep -rn '@AGENTS' release-notes` → **0**; `grep -rni 'symlink' release-notes` → 22 hits, **0** after the instruction/`AGENTS.md`/`CLAUDE.md`/`copilot` filter; none is about a rule file.
- **Docs tree:** `grep -rn '@AGENTS' .` → **0**; `grep -rni 'symlink' --include=*.md . | grep -ci 'instruction\|agents\.md\|claude\.md\|copilot'` → **0** (38 raw symlink hits tree-wide, all other topics).
- **Lane corpus:** `grep -rn '@AGENTS' corpus` → **0**; `grep -rni 'symlink' corpus` → 19 hits, 0 on instruction files (filtered count 0).
- **Verdict:** silent on both forms, sweep complete. The counter's docstring already bounds the forms to Claude Code's memory page; this client neither corroborates nor contradicts them, and no VS Code-sourced row may be cited for them.

### 2.3 No rule-file size limit

- **Release notes:** `grep -rniE 'truncat|character limit|size limit|max.*instruction|instruction.*limit' release-notes` → 33 hits; filtered to instruction/`AGENTS.md`/`CLAUDE.md`/`copilot` → 1 line (`v1_127.md:148`, session-title pill truncation), not a rule-file cap.
- **Docs tree:** `grep -rniE 'character|truncat|token limit|size limit|max.*size' docs/agent-customization docs/agents | grep -i 'instruction\|agents\.md\|claude\.md\|copilot-instructions'` → 6 lines, all unrelated (a `characteristics` heading at `docs/agents/concepts/agents.md:105` and OTel attribute truncation at `docs/agents/guides/monitoring-agents.md:125,144,145,262,281`); 0 about a rule-file cap. `grep -rn '8,000\|8000' docs/agent-customization docs/agents` → 3 hits, all unrelated (`maxInputTokens` example, an Excalidraw focus value, a Windows build number).
- **Lane corpus:** `grep -rni 'size limit\|character limit\|truncat' corpus | grep -i 'instruction\|agents\.md\|claude\.md'` → **0**.
- **Verdict:** silent, sweep complete.

### 2.4 No dating rule

- **Release notes:** `grep -rniE 'dated|transient|stale|expire|freshness' release-notes` → 476 hits; filtered to instruction/`AGENTS.md`/`CLAUDE.md`/`copilot-instructions` → 1 line (`v1_133.md:158`, a PR-list entry about stale relative doc paths), not a dating rule for rule files.
- **Docs tree:** `grep -rni 'transient\|dated text\|stale' docs/agent-customization docs/agents` → 4 hits: two are maintenance advice for instruction files (`customize-copilot-guide.md:153`, `context-engineering-guide.md:250`, quoted in §1.5); the other two are local-memory cleanup (`docs/agents/run/memory.md:47`) and terminal cleanup (`docs/agents/run/tools.md:211`). No rule, no prohibition.
- **Lane corpus:** `grep -rni 'dated or transient\|dated/transient\|transient text' corpus` → **1** hit, the checklist row itself (`corpus/knowledge/alwayson-checklist-round7.md:16`), which records the rule as lane-authored AC-4.
- **Verdict:** silent, sweep complete; the rule stays craft.

## 3. Bearing on the C2 counter (`verifiers/check_alwayson_boxes.py`, plan commit `3bb0a7a3`)

Counter contract read at `verifiers/check_alwayson_boxes.py:1-44` and cases `:65-88` in the sandbox clone. No case was run.

| Counter case | VS Code evidence | Effect on the claim |
|---|---|---|
| `alwayson.04` `plain-rules`, `version-number` → PASS; four dated/transient cases → FAIL | No vendor dating rule (§1.5/§2.4); nearest text is maintenance advice | The box's rule is lane-authored; the instrument's detail string must not cite VS Code as its authority |
| `alwayson.07` `agents-only` → PASS | Local harness attaches workspace-root `AGENTS.md` by default (`custom-instructions.md:232`, `ai-settings.md:351`) | Corroborated |
| `alwayson.07` `claude-only` → PASS | Local harness reads `CLAUDE.md` by default (`custom-instructions.md:248-257`, `ai-settings.md:352`) | Corroborated |
| `alwayson.07` `import-redirect` → PASS | No `@AGENTS.md` import documented anywhere in the tree (§2.2); only Markdown-link references, opt-in (`ai-settings.md:342`) | **Not corroborated by this client.** The PASS rests on Claude Code's page, as the docstring says. A repo using this form may have `AGENTS.md` ignored by VS Code; the knowledge entry should mark the form client-specific, not universal |
| `alwayson.07` `symlink-redirect` → PASS | No symlink behaviour documented (§2.2) | Not corroborated by this client; keep Claude Code as the sole basis |
| `alwayson.07` `two-rule-files` → FAIL | Sources are additive, no general precedence (`custom-instructions.md:315`); Copilot harness "combines" (`custom-instructions.html:1938`) | The FAIL is a *cross-client portability* verdict, not a VS Code error: VS Code reads both and will not arbitrate. The detail string should name the client whose behaviour makes the case a defect |
| `alwayson.07` `prose-mention` → FAIL | A prose mention is not a link or an import; the documented reference form is a Markdown link with `chat.includeReferencedInstructions` (`custom-instructions.md:73`, `ai-settings.md:342`) | Consistent |

Additional operability fact the docstring does not yet carry: the Copilot harness obeys GitHub's discovery, not `chat.useAgentsMdFile`. `custom-instructions.md:232`: the setting "does not control instruction discovery in other harnesses". So a repo's `AGENTS.md` reaches VS Code through two different mechanisms depending on the selected harness, and the Local-harness setting cannot switch the Copilot harness off.

## 4. Drafted SOURCES.md rows

Column shape copied from `corpus/SOURCES.md:12` (11 columns, no `|` inside a cell). All `S0xx` are placeholders for the next unused numbers. `used-by` is the path the assignment names. **Caveat:** that knowledge entry does not exist at base (`ls corpus/knowledge/ | grep -i alwayson` → `alwayson-checklist-round7.md` only), so if the entry is not landed, every row must be written `queued`, not `mined`.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | Visual Studio Code — Use custom instructions — https://code.visualstudio.com/docs/copilot/customization/custom-instructions | docs | A | Which always-on instruction files VS Code's Local harness reads, the settings that enable each, and how it treats several applicable sources (vendor documentation for VS Code; not a measurement of the editor) | § Types of instruction files (`custom-instructions.md:45`), § Use a `.github/copilot-instructions.md` file (`:79`, `:89`), § Use an `AGENTS.md` file (`:229`, `:232`, `:236`, `:239`), § Use a `CLAUDE.md` file (`:248-257`), § Resolve conflicting instructions (`:315-319`), § Tips for writing effective instructions (`:332`); source pinned at commit fd64d64891a2e660bcc0d32ea402da905adfef7f (25,213 B, sha256 `eb2be087…`); rendered page fetched 2026-10-22T20:04:53Z (200, 162,008 B, sha256 `dc87f7c2…`) | The Local harness reads `.github/copilot-instructions.md`, workspace-root `AGENTS.md` (nested files when `chat.useNestedAgentsMdFiles` is on) and `CLAUDE.md` in four locations; applicable sources are additive and the page tells authors not to depend on a file order or precedence rule | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Visual Studio Code — AI settings reference — https://code.visualstudio.com/docs/agents/reference/ai-settings | docs | A | Default values of the settings that enable each always-on instruction file in VS Code's Local harness (vendor documentation, not a measurement of the editor) | § Chat settings rows `chat.useClaudeMdFile` (`ai-settings.md:108`, `:352`), `chat.useNestedAgentsMdFiles` (`:109`, `:353`), `chat.instructionsFilesLocations` (`:340`), `chat.includeReferencedInstructions` (`:342`), `github.copilot.chat.codeGeneration.useInstructionFiles` (`:343`), `chat.useCustomizationsInParentRepositories` (`:347`), `chat.useAgentsMdFile` (`:351`); source pinned at commit fd64d648 (67,275 B, sha256 `6157cfd8…`); rendered page fetched 2026-10-22T20:09:43Z (200, 547,123 B, sha256 `36322715…`) | `chat.useAgentsMdFile` and `chat.useClaudeMdFile` both default to `true`, nested `AGENTS.md` defaults to `false`, `github.copilot.chat.codeGeneration.useInstructionFiles` defaults to `true`, `chat.includeReferencedInstructions` defaults to `false`, and `chat.instructionsFilesLocations` is deprecated | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Visual Studio Code — August 2025 release notes (version 1.104) — https://code.visualstudio.com/updates/v1_104 | docs | A | The release that introduced `AGENTS.md` as always-on chat context (vendor release notes, not a measurement of the editor) | § Support for AGENTS.md files (Experimental) (`v1_104.md:107-113`, setting `:109`, behaviour `:111`, default `:113`); source pinned at commit fd64d648 (63,277 B, sha256 `8c88ed30…`); rendered page fetched 2026-10-22T20:09:43Z (200, 179,457 B, sha256 `b352f4bd…`) | From 1.104 a workspace-root `AGENTS.md` is automatically picked up as chat context, enabled by default and controlled by `chat.useAgentsMdFile` | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Visual Studio Code — September 2025 release notes (version 1.105) — https://code.visualstudio.com/updates/v1_105 | docs | A | The release that made root `AGENTS.md` generally available and added nested-file discovery (vendor release notes) | § Support for nested AGENTS.md files (Experimental) (`v1_105.md:180-186`, setting `:182`, GA `:184`, nested `:186`); source pinned at commit fd64d648 (44,322 B, sha256 `ceefddfb…`); rendered page fetched 2026-10-22T20:09:43Z (200, 136,479 B, sha256 `4a200e8a…`) | Root `AGENTS.md` support became generally available and enabled by default; nested files arrived experimentally behind `chat.useNestedAgentsMdFiles` | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Visual Studio Code — January 2026 release notes (version 1.109) — https://code.visualstudio.com/updates/v1_109 | docs | A | The release that introduced reading Claude configuration files, including `CLAUDE.md` (vendor release notes) | § Agent Extensibility → § Claude compatibility (`v1_109.md:624-630`, opening `:626`, instruction locations `:630`); source pinned at commit fd64d648 (91,592 B, sha256 `cf04c2ec…`); rendered page fetched 2026-10-22T20:09:43Z (200, 277,876 B, sha256 `63099e9d…`) | VS Code began reading `CLAUDE.md` at the workspace root, `.claude/CLAUDE.md`, `~/.claude/CLAUDE.md` and `.claude/rules` as Claude compatibility | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Visual Studio Code — September 2024 release notes (version 1.94) — https://code.visualstudio.com/updates/v1_94 | docs | A | The release that introduced the shared `.github/copilot-instructions.md` file (vendor release notes) | § Custom instructions (Experimental) (`v1_94.md:170-176`, setting `:172`, behaviour `:176`); source pinned at commit fd64d648 (52,315 B, sha256 `f5d07cf6…`); rendered page fetched 2026-10-22T20:09:43Z (200, 139,739 B, sha256 `02397663…`) | `.github/copilot-instructions.md` was introduced as shared code-generation instructions, controlled by `github.copilot.chat.experimental.codeGeneration.useInstructionFiles` (renamed since) | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |

### 4.1 Rejected candidates

| candidate | reason |
|---|---|
| `https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md` | 404, 9 B (2026-10-22T20:04:53Z). The rendered route's directory has no Markdown variant; the site's Markdown view lives at the source-directory route (`/docs/agent-customization/custom-instructions.md`, 200, 23,423 B, sha256 `f7d67ca7…`, 20:14:26Z). A `.md` quote must use that route or the GitHub pin, never the rendered directory. Flip: if VS Code starts serving `.md` at the rendered route. |
| `docs/copilot/customization/custom-instructions.md` in `microsoft/vscode-docs` (`main` and `vnext`) | 404, 14 B each (20:04:58Z, 20:05:12Z). The rendered URL's directory name does not exist in the source tree; the file lives under `docs/agent-customization/`. This is the Q30 "old path" trap and the reason the rows anchor the source pin, not the rendered directory. |
| GitHub REST API `contents` listing for the docs repo | 403, 280 B (20:05:02Z), unauthenticated rate limit. Not evidence; the tarball replaced it. |
| jsDelivr package listing API | 503, 452 B (20:06:59Z). Not evidence. |
| `https://code.visualstudio.com/docs/agent-customization/custom-instructions` as a *source* | 200, 162,008 B, sha256 `dc87f7c2…` (20:11:58Z) — byte-identical to the current render, so it is the same page today, but the published route is now `/docs/copilot/customization/…`; a row pinned to the old route would decay silently. Opened as a probe only; the row uses the current rendered URL plus the source pin. |
| GitHub Copilot CLI / Copilot cloud-agent pages | Not this client. Already covered by the sibling seat `ScribeCopilotCli` and rows S027/S028/S031/S038/S042. |
| Claude Code memory page (`https://code.claude.com/docs/en/memory.md`) | Out of my target client. The plan names it as C2's redirect basis and assigns its row to another seat; I did not open or cite it. |
| The `microsoft/vscode-docs` release notes for 1.106/1.107/1.112 as rows | Opened and grepped; they add only parent-repository discovery (`v1_112.md:168-172`) and a PR-list mention (`v1_106.md:932`). That fact is carried in row 2's `chat.useCustomizationsInParentRepositories` anchor; separate rows would duplicate one source. |

## 5. Gate record

| source row | URL | UTC | HTTP | bytes | sha256 | quote | line |
|---|---|---|---|---|---|---|---|
| 1 rendered | https://code.visualstudio.com/docs/copilot/customization/custom-instructions | 2026-10-22T20:04:53Z | 200 | 162,008 | `dc87f7c2a0c19e731bb2902306f505740bef05dc78df1214a1fbc67a374b7ab0` | "Copilot combines applicable instructions from `AGENTS.md` and other supported instruction files." | `custom-instructions.html:1938` |
| 1 rendered | same | same | 200 | 162,008 | same | "Applicable instruction sources are additive. Do not depend on a file order or precedence rule to resolve conflicts" | `custom-instructions.html:2251` |
| 1 site md | https://code.visualstudio.com/docs/agent-customization/custom-instructions.md | 2026-10-22T20:14:26Z | 200 | 23,423 | `f7d67ca79edbb768ce875f74497428aa6fc9605dd9a0c6823328e781e0696b31` | "Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`." | `site-custom-instructions.md:32` |
| 1 site md | same | same | 200 | 23,423 | same | "Copilot combines applicable instructions from `AGENTS.md` and other supported instruction files." | `:216` |
| 1 site md | same | same | 200 | 23,423 | same | "Applicable instruction sources are additive. Do not depend on a file order or precedence rule to resolve conflicts" | `:302` |
| 1 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/docs/agent-customization/custom-instructions.md | 2026-10-22T20:10:54Z | 200 | 25,213 | `eb2be0877a6241a520bdd41cf26346ec2ba9c8a0576f855cb09f0d2b4ce34d6b` | "Project instructions can use `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`." | `custom-instructions.md:45` |
| 1 source | same | same | 200 | 25,213 | same | "The Local harness also discovers this workspace file when `setting(github.copilot.chat.codeGeneration.useInstructionFiles)` is enabled." | `:79` |
| 1 source | same | same | 200 | 25,213 | same | "The `setting(chat.useAgentsMdFile)` setting controls whether instructions from workspace-root `AGENTS.md` files are automatically attached to chat requests and is enabled by default." | `:232` |
| 1 source | same | same | 200 | 25,213 | same | "Set both `setting(chat.useAgentsMdFile)` and `setting(chat.useNestedAgentsMdFiles)` to `true` to discover nested `AGENTS.md` files." | `:239` |
| 1 source | same | same | 200 | 25,213 | same | "The Local harness searches for Claude instructions in these locations when `setting(chat.useClaudeMdFile)` is enabled" | `:248` |
| 1 source | same | same | 200 | 25,213 | same | "`CLAUDE.local.md` for local-only instructions (not committed to version control)" | `:255` |
| 1 source | same | same | 200 | 25,213 | same | "Do not depend on a file order or precedence rule to resolve conflicts" | `:315` |
| 1 source | same | same | 200 | 25,213 | same | "Keep your instructions short and self-contained." | `:332` |
| 2 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/docs/agents/reference/ai-settings.md | 2026-10-22T20:05:50Z | 200 | 67,275 | `6157cfd8b7d7439d88891c96454b6087f3d764588c57d85efa84139b2d270bb2` | "Automatically attach instructions from workspace-root `AGENTS.md` files to chat requests in Local harness sessions only." | `ai-settings.md:351` |
| 2 source | same | same | 200 | 67,275 | same | "Enable or disable using `CLAUDE.md` files as always-on custom instructions." (default `true`) | `:352` |
| 2 source | same | same | 200 | 67,275 | same | "List `AGENTS.md` files in workspace subfolders for on-demand loading in Local harness sessions." (default `false`) | `:353` |
| 2 source | same | same | 200 | 67,275 | same | "Automatically add custom instructions from `.github/copilot-instructions.md` to chat requests." (default `true`) | `:343` |
| 2 source | same | same | 200 | 67,275 | same | "Automatically add instruction files referenced via Markdown links to chat requests." (default `false`) | `:342` |
| 2 rendered | https://code.visualstudio.com/docs/agents/reference/ai-settings | 2026-10-22T20:09:43Z | 200 | 547,123 | `3632271596f8138f54658bf76a740e8fcdf306af1190c27342d3bd1bfd687058` | — (rendered route resolves; quotes above are the pinned source bytes) | — |
| 2 site md | https://code.visualstudio.com/docs/agents/reference/ai-settings.md | 2026-10-22T20:14:26Z | 200 | 65,274 | `902fb594b4bdc902d905275cb85cff4abffe1289ded093fa44e2a06933fa8e81` | "Automatically attach instructions from workspace-root `AGENTS.md` files to chat requests in Local harness sessions only." | `site-ai-settings.md:348` |
| 2 site md | same | same | 200 | 65,274 | same | "Enable or disable using `CLAUDE.md` files as always-on custom instructions." (default `true`) | `:349` |
| 3 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/release-notes/v1_104.md | 2026-10-22T20:05:50Z | 200 | 63,277 | `8c88ed30421e6446cd8787be24ae2461d7e6932f37115bf179b2a2301d817bd6` | "when you have an `AGENTS.md` file in your workspace root(s), it is automatically picked up as context for chat requests" | `v1_104.md:111` |
| 3 rendered | https://code.visualstudio.com/updates/v1_104 | 2026-10-22T20:09:43Z | 200 | 179,457 | `b352f4bd8c6a29b4975a135fdb66d03191871483253b645ca7736da217938eac` | "Support for `AGENTS.md` files is enabled by default" | source `v1_104.md:113` |
| 4 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/release-notes/v1_105.md | 2026-10-22T20:05:50Z | 200 | 44,322 | `ceefddfbb53481a7cc3c4b96d8c03911594f7d22e882568d2c79fa12a41e02af` | "This functionality is now generally available and enabled by default." | `v1_105.md:184` |
| 4 source | same | same | 200 | 44,322 | same | "We now also added support for nested `AGENTS.md` files in subfolders of your workspace." | `:186` |
| 4 rendered | https://code.visualstudio.com/updates/v1_105 | 2026-10-22T20:09:43Z | 200 | 136,479 | `4a200e8a2ce8fee847395b00dd51c48b8309c61bb457027924372b0c1198bf47` | — (rendered route resolves) | — |
| 5 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/release-notes/v1_109.md | 2026-10-22T20:06:31Z | 200 | 91,592 | `cf04c2ec0e16f791be568514b6d300a8497176cafa5af17e71586df21ed64b23` | "VS Code now reads Claude configuration files directly" | `v1_109.md:626` |
| 5 source | same | same | 200 | 91,592 | same | "**Instructions**: `CLAUDE.md` files in your workspace root, `.claude/CLAUDE.md`, and `~/.claude/CLAUDE.md`." | `:630` |
| 5 rendered | https://code.visualstudio.com/updates/v1_109 | 2026-10-22T20:09:43Z | 200 | 277,876 | `63099e9d6b6d405741db4cbb965ace46b0bc8e5e6cbacb8c7938734c783c0f55` | — (rendered route resolves) | — |
| 6 source | https://raw.githubusercontent.com/microsoft/vscode-docs/fd64d64891a2e660bcc0d32ea402da905adfef7f/release-notes/v1_94.md | 2026-10-22T20:06:31Z | 200 | 52,315 | `f5d07cf6109c042862b5a55e49b2f00100601bed3ef72d292490f9e191e216e0` | "define **shared instructions** for code generation in a `.github/copilot-instructions.md` file in your workspace" | `v1_94.md:176` |
| 6 rendered | https://code.visualstudio.com/updates/v1_94 | 2026-10-22T20:09:43Z | 200 | 139,739 | `023976632244e758ee2c7135f633c19654fe44ad98c620c1b27ece1044cb635c` | — (rendered route resolves) | — |
| Q30 tree control | https://codeload.github.com/microsoft/vscode-docs/tar.gz/fd64d64891a2e660bcc0d32ea402da905adfef7f | 2026-10-22T20:07:20Z | 200 | 35,508,770 | `6732e10c18b868f293eba88fa1cb83c1c1d605b4e0eaa7686eef496b7ba63468` | — (whole-tree grep control; 8,886 files, 860 Markdown) | — |
| docs advice (not a row) | tarball member `docs/agents/guides/customize-copilot-guide.md` | 2026-10-22T20:07:20Z | 200 (tarball) | 35,508,770 | `6732e10c…` | "remove stale or duplicate rules" | `customize-copilot-guide.md:153` |
| marker probe | https://code.visualstudio.com/docs/copilot/customization/custom-instructions.md | 2026-10-22T20:04:53Z | 404 | 9 | `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5` | — | — |
| marker probe | https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/copilot/customization/custom-instructions.md | 2026-10-22T20:04:58Z | 404 | 14 | not hashed | — | — |
| marker probe | https://api.github.com/repos/microsoft/vscode-docs/contents/docs/copilot/customization?ref=main | 2026-10-22T20:05:02Z | 403 | 280 | not hashed | — (rate limit) | — |
| marker probe | https://data.jsdelivr.com/v1/packages/gh/microsoft/vscode-docs@fd64d648…?structure=flat | 2026-10-22T20:06:59Z | 503 | 452 | not hashed | — | — |
| old-route probe | https://code.visualstudio.com/docs/agent-customization/custom-instructions | 2026-10-22T20:11:58Z | 200 | 162,008 | `dc87f7c2a0c19e731bb2902306f505740bef05dc78df1214a1fbc67a374b7ab0` | — (byte-identical to the current rendered page) | — |

Every quoted line is ≤25 words and byte-exact in the named fetched file. The rendered-release-note rows are provenance that the human URL resolves; their quotes are cited from the pinned source files, which the table names.

## 6. Findings, limits, out of scope

1. **Row status is contingent on the knowledge entry.** `status: mined` requires `corpus/knowledge/alwayson-rule-files-round53.md` to exist and cite the rows. It does not exist at base. If it is not landed, all six rows must be written `queued`; the L1 should check before appending.
2. **VS Code reads both `AGENTS.md` and `CLAUDE.md` by default and refuses to pick a winner** (the pair composition is `[INFERENCE]` from the two `true` defaults plus the additive rule, §1.2; the no-precedence rule is documented). Its docs say sources are additive and warn against assuming precedence (`custom-instructions.md:315`). The same combine-without-precedence behaviour is documented for Copilot CLI (sibling report `ScribeCopilotCli.md` §2.2), so the alwayson.07 `two-rule-files` FAIL is a portability hazard, not a VS Code error. The knowledge entry should attribute the FAIL to the clients that pick one name (Claude Code reads `CLAUDE.md` only; opencode folds `AGENTS.md` → `CLAUDE.md` → `CONTEXT.md` first-hit, already recorded at `corpus/knowledge/instruction-surface-census-round13.md:479`), not to VS Code. Unlike Copilot CLI, VS Code does not document `GEMINI.md` (finding 4).
3. **The two redirect forms remain Claude-Code-only.** VS Code documents no `@AGENTS.md` import and no symlink handling for rule files; its only documented cross-file reference is Markdown links behind `chat.includeReferencedInstructions`, default `false`. The counter's PASS cases can keep resting on Claude Code's memory page, but no VS Code row or knowledge sentence may say "clients honour redirects" without naming the client. This is a source-boundary issue for the C2 knowledge entry, not a defect in the frozen counter.
4. **GEMINI.md is undocumented for VS Code.** Zero hits across 8,886 files at the pinned tip plus all release notes, and no corpus row associates it with VS Code. Because `custom-instructions.md:47` allows that "Some harnesses also recognize additional formats", the record is "not documented", never "unsupported".
5. **No size cap and no dating rule exist in this client's docs.** alwayson.04's rule is lane-authored; the nearest vendor text is review hygiene (`customize-copilot-guide.md:153`). The instrument's detail strings must not attribute the rule to VS Code.
6. **Harness split is an operability fact the instrument does not carry.** `chat.useAgentsMdFile` is Local-only and "does not control instruction discovery in other harnesses" (`custom-instructions.md:232`); the Copilot harness follows GitHub's discovery, linked from `:229`. A repo's always-on file reaches VS Code through different mechanisms depending on the selected harness.
7. **What was not measured.** I ran no counter, gate, instrument, build or editor. This is vendor documentation reading, not a measurement of VS Code. No `code` CLI, no extension host and no Copilot backend was invoked. The C2 counter's exit code and the 6 pinned cases were not re-run; that is the executor's and the main agent's work.
8. **Evidence locations.** All fetched bytes: `/fast/scratch/hyaku/kotoba-r53/ScribeVSCode/scratch/vscode/` — `custom-instructions.html`, `custom-instructions.md` (404 body), `vscode-docs-custom-instructions-main.md`, `pinned-custom-instructions.md`, `ai-settings.md`, `rn/v1_*.md` (60–144), `rn-v1_104.md`…`rn-v1_107.md`, `rendered-*.html`, `vscode-docs-main.tar.gz`, `docs-tree/`, `jsdelivr-flat.json`, `api-customization-dir.json`, `tree-*.html`. The sandbox clone is `/fast/scratch/hyaku/kotoba-r53/ScribeVSCode` at `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`; no lane file was modified except this report.
