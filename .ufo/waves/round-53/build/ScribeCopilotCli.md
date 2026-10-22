Result: DONE — GitHub Copilot CLI documents all three always-on names (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`) plus `copilot-instructions.md` and `*.instructions.md`, combines any that co-exist without a general precedence order, honours a `@`-relative-path import (not in `GEMINI.md`), documents no size cap and no symlink behaviour for rule files; six SOURCES rows drafted, one changelog source rejected as a duplicate of S042.

Round 53, wave 1 (build), C2 source basis. Seat `KotobaR53.ScribeCopilotCli`. Target client: GitHub Copilot CLI and the Copilot coding agent. Lane base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`; plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. Nothing in the lane was written except this file; all fetched bytes live in `/fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/`. No tool was installed or upgraded (nothing was needed); no model call of any kind was made.

## 1. Method

All sources were opened with plain `curl -sS -o <file> -w 'status=%{http_code} bytes=%{size_download}'`, in the scratch directory above, and hashed with `sha256sum`. Every fetch printed `status=200` (or the failure status recorded in the Gate table); the shell reported no non-zero exit for the successful fetches. `docs.github.com` serves a `.md` variant of each page; quoting is against those bytes, with line numbers in the fetched file. The GitHub REST API returned 403 (rate limit) for the `github/docs` tree listing, so the source-tree inventory was read from the ordinary HTML tree page (`github.com/github/docs/tree/main/content/copilot/how-tos/copilot-cli/customize-copilot`, 200, 247,109 B, sha256 `8f907358…`) and by opening the individual source files.

The stale path in the brief (`/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions`) is a 404 as `.md` (502 B) and a 301 to `/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions` (200, 708,144 B HTML). That is the exact "old path" failure Q30 warns about, so every quote below is against the canonical path.

## 2. Answers

### 2.1 Which always-on file names it reads

GitHub Copilot CLI, rendered page `copilot-cli-custom-instructions.md` (8,730 B, sha256 `00e45ea5…`) § Types of custom instructions table `:15-22`:

- `:15` — "`$HOME/.copilot/copilot-instructions.md`" (user-level)
- `:16` — "`$HOME/.copilot/instructions/**/*.instructions.md`" (modular user-level)
- `:17` — "`.github/copilot-instructions.md`" (repository-wide)
- `:18` — "`.github/instructions/**/*.instructions.md`" (modular repository)
- `:19` — "`AGENTS.md`" — "Agent instructions, discovered in the standard locations." (verbatim)
- `:20` — "`CLAUDE.md`" — "Copilot CLI also uses `.claude/CLAUDE.md`." (verbatim)
- `:21` — "`GEMINI.md`" — "Agent instructions, discovered in the standard locations." (verbatim)
- `:22` — "Directories listed in `COPILOT_CUSTOM_INSTRUCTIONS_DIRS`" — "Additional `AGENTS.md` and `*.instructions.md` files."

`:11` defines "standard locations": "the repository root, the current working directory, intermediate directories between them, and any directories nested in the path of a file it is working on".

A fourth agent-instruction name exists on a different Copilot surface. `custom-instructions-support.md:44` (the code review row under § GitHub.com) reads, inside HTML markup: `<code>AGENTS.md</code>, <code>CLAUDE.md</code>, <code>GEMINI.md</code> or <code>REVIEW.md</code> files`. `REVIEW.md` appears nowhere in the CLI table, i.e. it is not a Copilot CLI name. The CLI's own support-matrix list repeats the three-name set at `:254` (`<code>AGENTS.md</code>, <code>CLAUDE.md</code> or <code>GEMINI.md</code> files`).

### 2.2 Two of them existing in one directory

Copilot CLI combines them. `copilot-cli-custom-instructions.md:30`:

> When multiple applicable user-level and repository instruction files exist, Copilot CLI combines their instructions.

Same line: "It removes duplicate copies of identical user-level `copilot-instructions.md`, repository-wide, and agent instructions, but does not define a general precedence order between these files." The concepts page repeats it for the whole product family, `custom-instructions.md:84`:

> Most surfaces and clients, including Copilot CLI, Visual Studio Code and Visual Studio, combine applicable instruction files without defining a general precedence order.

(verbatim.) The release notes record the change that produced this behaviour, `changelog.md:3086` under `## 0.0.385 - 2026-01-19`: "Combine all custom instruction files instead of using priority-based fallbacks" (verbatim). The same notes state the de-duplication rule at `:2050` (`## 1.0.26 - 2026-04-14`): "Avoid sending duplicate custom instruction files" (verbatim).

The **cloud-agent surface is the opposite**, and the divergence is documented in the same docs set — `repository-instructions.md:31`:

> When Copilot is working, the nearest `AGENTS.md` file in the directory tree will take precedence.

(verbatim.) `:33`: "Alternatively, you can use a single `CLAUDE.md` or `GEMINI.md` file stored in the root of the repository." (verbatim.) The docs-source reusable that renders `:31` is `data/reusables/copilot/custom-instructions-agents.md:1` (329 B, sha256 `ee14953c…`), same sentence modulo the `{% data variables.product.prodname_copilot_short %}` substitution.

So "nearest wins" is the cloud agent and code review; "combine, no general order" is the CLI. `custom-instructions.md:50` bounds the second: agent instructions "are similar to repository-wide custom instructions, but are currently not supported by all Copilot features" (verbatim).

### 2.3 Redirect honoured?

Yes, as an `@`-relative-path import, and only in three files. `copilot-cli-custom-instructions.md:48`:

> In `.github/copilot-instructions.md`, `AGENTS.md`, or `CLAUDE.md`, use `@` followed by a relative path to include another file.

(verbatim.) `:50` bounds it: "Absolute paths and paths beginning with `~/` are not loaded." and "File references are not expanded in `GEMINI.md` or `*.instructions.md` files." (second sentence, verbatim.) `:48` also says Copilot CLI "reads the referenced file immediately and supports references within referenced files". The changelog dates the capability: `changelog.md:1110` under `## 1.0.66 - 2026-06-30` — "Expand @-style imports in AGENTS.md, CLAUDE.md, and Copilot instruction files" (verbatim).

A config pointing at another name also exists, but only as a directory list, not a file alias: `:22` `COPILOT_CUSTOM_INSTRUCTIONS_DIRS` adds "`AGENTS.md` and `*.instructions.md`" files; the changelog fixes path handling at `:2388` (`1.0.6`).

**Symlink: not documented.** No page states whether a symlinked `AGENTS.md`/`CLAUDE.md` is followed (sweep in §3.2). I therefore record Copilot CLI as *not checked* on symlink redirection — never "silent", never "supported".

### 2.4 Documented size limit

**None for rule files.** The only numeric bound anywhere in the opened bytes is inside the prompt text that asks the cloud agent to *generate* a `copilot-instructions.md`, `repository-instructions.md:63`:

> Instructions must be no longer than 2 pages.

(verbatim.) It sits under `<Limitations>` inside a copyable prompt (`:44-121`), addressed to the generating agent, not to the loader; the same block says at `:64` "Instructions must not be task specific." (verbatim.) No loader cap, truncation rule or character budget for `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`copilot-instructions.md` appears on the CLI page, the concepts page, the support page or in the changelog (sweep in §3.1).

### 2.5 Dated or transient content

**Not documented as a rule for the file.** The nearest statements are load-time economics, not a dating rule — `custom-instructions.md:126`: "Because the instructions are sent with every chat message, they should be broadly applicable to most requests" (verbatim), and the generation-prompt line `repository-instructions.md:64` above. Copilot CLI does document *session* transience of edits: `copilot-cli-custom-instructions.md:105` — "Changes you make to custom instructions files are not immediately available for use in active CLI sessions." (verbatim.)

Consequence for C2: alwayson.04 ("no dated or transient text") is a lane craft rule. No Copilot document states it, so the box's rule may not be attributed to the vendor (Q20/Q23); the vendor supplies only the weaker "broadly applicable / not task specific" guidance.

### 2.6 Two reach facts the instrument's docstring does not yet carry

- **Subagents skip always-on files by default.** `create-custom-agents-for-cli.md:133`: "the subagent does not follow your repository's custom instructions by default" (verbatim); the opt-in is `include-custom-instructions: true` (`:135-142`), and `:149` confirms a directly selected agent "already follows your repository's custom instructions". The changelog records the same at `:364` (`## 1.0.86 - 2026-09-17`). An always-on file in a Copilot CLI repo is therefore not universally in front of the model.
- **Per-directory discovery is CLI-wide, not root-only.** `changelog.md:2292` (`## 1.0.11 - 2026-03-23`): "Custom instructions, MCP servers, skills, and agents are now discovered at every directory level from the working directory up to the git root" (verbatim). Claude Code rule files under `.claude/rules` were added at `:271` (`## 1.0.89 - 2026-09-28`): "Add support for Claude Code rule files in .claude/rules as custom instructions" (verbatim) — a third always-on location the CLI reads, not a redirect form.

## 3. Q30 sweeps for the three negatives

Each negative below names its three legs: the vendor changelog (`copilot-cli-changelog.md`, pinned `7ea98dfc…`, 289,859 B, sha256 `c4b793bd…`, 3,569 lines), the current docs source tree (`docs-src-add-repository-instructions.md` 13,608 B `04cf53d3…`; `src_content_copilot_how-tos_copilot-cli_customize-copilot_add-custom-instructions.md` 5,684 B `ed823a4f…`; `src_data_reusables_copilot_custom-instructions-agents.md` 329 B `ee14953c…`), and a grep of the lane corpus.

**3.1 No rule-file size limit.** (a) Changelog: `grep -n -i -E 'limit|truncat|characters|token budget|too large|maximum|max '` filtered to instruction lines gave context-window and compaction hits only; the full `grep -n -i 'instruction'` list (52 hits, reviewed) contains no cap. (b) Source tree: `grep -n -i -E 'symlink|symbolic|limit|truncat|characters|token|date|deprecat|stale|expire|page'` over the three files returned only the `<Limitations>` lines `docs-src-add-repository-instructions.md:73-76` and unrelated capability-list lines. (c) Lane corpus: `grep -rlE 'Copilot|copilot' corpus` (run 2026-10-22 from the lane root, exit 0) lists 15 files — `knowledge/{instruction-surface-census,instruction-surface-remeasure,mcp-server-instructions,sibling-overlap-census,skill-overlap-levers,skill-selection-rules}-round*.md`, `lessons/round-5{0,1,2}*.md`, `QUALITY.md`, `README.md`, `SOURCES.md`; no recorded size limit.

**3.2 No symlink behaviour for rule files.** (a) Changelog: `grep -n -i -E 'symlink|symbolic link'` → 11 hits, none about an instruction file: sandbox path policy (`:684`, `:1031`, `:1046`, `:1195`), skill discovery and duplicate-parse errors (`:1026`, `:1366`), `@`-file picker and `/cwd` completion (`:1269`, `:1411`, `:1514`), extensions (`:1478`), custom-agent definition discovery (`:3101`). (b) Source tree: `grep -n -i -E 'symlink|symbolic'` over the three files → 0 hits. (c) Corpus: no row about symlinked rule files for any Copilot surface. Verdict: *not checked*, per Q30. The counter's `symlink-redirect` PASS case must keep resting on Claude Code's memory page, as its docstring already says.

**3.3 No dating rule for rule files.** (a) Changelog: no instruction line mentions dates, staleness, expiry or freshness (the same 52-hit list). (b) Source tree: no `date|stale|expire|deprecat` hit in the instruction prose. (c) Corpus: `alwayson-checklist-round7.md:21` already records the lane rule as craft — "one canonical owner or explicit redirect" is stated as an AC item drafted by the lane, not a client quote. Verdict: the absence is real for this client, and the rule stays lane-authored.

## 4. Bearing on the C2 counter (operability)

Counter: `verifiers/check_alwayson_boxes.py` in the lane working tree at the plan commit `3bb0a7a3`, docstring `:1-44`, `RULES_A`/`RULES_B` `:61-62`, `CASES` `:65-88` (`alwayson.04` `:66-75`, `alwayson.07` `:76-87`).

| Counter case | Copilot CLI evidence | Effect |
|---|---|---|
| `alwayson.07` `import-redirect` (`CLAUDE.md` holds `@AGENTS.md`) | `copilot-cli-custom-instructions.md:48` documents `@` + relative path inside `CLAUDE.md`; `changelog.md:1110` | second client corroborates the form; the docs show no bare `@AGENTS.md` example, so "`@AGENTS.md` is an `@`-plus-relative-path reference" is `[INFERENCE]` (safe: the path is relative and inside the repo) |
| `alwayson.07` `symlink-redirect` | not documented (§3.2) | cannot be grounded on this client; keep Claude Code as the sole basis and do not claim Copilot honours it |
| `alwayson.07` `two-rule-files` → FAIL | CLI combines both (`:30`); cloud agent takes the nearest `AGENTS.md` (`repository-instructions.md:31`); Claude Code reads `CLAUDE.md` only (plan's basis) | the FAIL is a *cross-client portability* verdict, not a Copilot CLI error; the instrument's detail string should name the client that makes it one |
| `alwayson.07` `prose-mention` → FAIL | an import is `@` + path (`:48`); prose is not | consistent |
| `alwayson.04` all four FAIL cases | no vendor dating rule (§3.3); nearest text is `:126` and `repository-instructions.md:64` | keep the box rule lane-authored in the instrument's detail string (Q20/Q23) |

## 5. Drafted SOURCES.md rows

Column shape copied from `corpus/SOURCES.md:12` (11 columns, no `|` inside a cell). All `S0xx` are placeholders for the next unused numbers. `used-by` is the path the assignment names; see the caveat in §7 item 1.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | GitHub Docs — Adding custom instructions for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | docs | A | Which always-on rule-file names GitHub Copilot CLI reads, what it does when several exist in one directory, and which redirect form it expands (vendor documentation for Copilot CLI; not a measurement of the CLI binary) | § Types of custom instructions table (`copilot-cli-custom-instructions.md:11-22`), § How multiple instruction files interact (`:30-32`), § Referencing other files (`:48-50`), § Custom instructions in use (`:105`); fetched 2026-10-22T20:05:13Z (200, 8,730 B, sha256 `00e45ea5…`) | The CLI reads `AGENTS.md`, `CLAUDE.md` (also `.claude/CLAUDE.md`) and `GEMINI.md` as agent instructions plus `.github/copilot-instructions.md` and `*.instructions.md`; with several present it "combines their instructions" and states it "does not define a general precedence order between these files"; `@`-relative-path imports expand in `AGENTS.md` and `CLAUDE.md` but not in `GEMINI.md` | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | GitHub Docs — Custom instructions for GitHub Copilot (concepts) — https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions.md | docs | A | The cross-surface precedence GitHub documents for instruction files and why instruction text stays short and general (vendor documentation, not a measurement of any client) | § About repository custom instructions (`custom-instructions.md:50`), § Precedence of custom instructions (`:84`), § Writing effective custom instructions (`:126`); fetched 2026-10-22T20:04:59Z (200, 14,669 B, sha256 `6e7964dc…`) | "Most surfaces and clients, including Copilot CLI, Visual Studio Code and Visual Studio, combine applicable instruction files without defining a general precedence order"; agent instructions are "not supported by all Copilot features"; instructions ride every chat message, so they must be broadly applicable | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | GitHub Docs — Adding repository custom instructions for GitHub Copilot — https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | docs | A | Which rule file the Copilot cloud agent prefers in one directory, and the only numeric size and content wording found in the pages opened this round (vendor documentation for Copilot on GitHub; not a measurement of the CLI) | § Creating custom instructions, agent bullet (`repository-instructions.md:31`, `:33`); generation prompt `<Limitations>` (`:63-64`); fetched 2026-10-22T20:04:48Z (200, 22,858 B, sha256 `c29d67f0…`) | On the cloud-agent and code-review surface "the nearest `AGENTS.md` file in the directory tree will take precedence" and a single root `CLAUDE.md` or `GEMINI.md` is the alternative, which is the opposite of the CLI's combine rule; "no longer than 2 pages" and "must not be task specific" are prompt text to the generating agent, not a loader cap | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | GitHub Docs — Support for different types of custom instructions — https://docs.github.com/en/copilot/reference/custom-instructions-support.md | docs | A | Which custom-instruction classes each Copilot surface supports, including the agent-instruction name list the page gives for each surface (vendor documentation, not a measurement of any client) | § Copilot CLI (`custom-instructions-support.md:249-256`), § GitHub.com code review (`:44`); fetched 2026-10-22T20:04:59Z (200, 14,612 B, sha256 `90150f5a…`) | Copilot CLI supports repository-wide, path-specific, agent (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`) and personal instructions; Copilot code review on GitHub.com also reads a `REVIEW.md` agent-instruction file, a fourth name absent from the CLI's own table | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | GitHub Docs — `data/reusables/copilot/custom-instructions-agents.md` in github/docs (`main`) — https://raw.githubusercontent.com/github/docs/main/data/reusables/copilot/custom-instructions-agents.md | docs | A | The docs-source text that renders as the AGENTS.md paragraph of the repository-instructions page (the Q30 docs-source-tree leg) | whole file (`custom-instructions-agents.md:1`, one line, 329 B); fetched 2026-10-22T20:05:22Z (200, sha256 `ee14953c…`); rendered at `repository-instructions.md:31` | `AGENTS.md` may be created at several depths and the nearest one wins on the cloud-agent surface; the sentence lives in one reusable, so an edit there changes every surface that includes it and a recheck should watch the reusable, not only the rendered page | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | GitHub Docs — Applying your repository's custom instructions to a custom agent (Copilot CLI) — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | docs | A | Whether an always-on rule file reaches a Copilot CLI subagent (vendor documentation for Copilot CLI; not a measurement of the binary) | § Applying your repository's custom instructions to a custom agent (`create-custom-agents-for-cli.md:129-151`, opt-in block `:135-142`, exception `:149`); fetched 2026-10-22T20:06:37Z (200, 8,379 B, sha256 `506783b4…`) | A Copilot CLI subagent "does not follow your repository's custom instructions by default" and needs `include-custom-instructions: true` in its frontmatter, so an always-on file is not in every Copilot context in a repo that uses custom agents | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |

### 5.1 Rejected candidates

| candidate | reason |
|---|---|
| `content/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md` in github/docs (200, 13,608 B, sha256 `04cf53d3…`, 20:05:13Z) | Not written as a row: same prose as row 3 modulo `{% data variables %}`/`AUTOTITLE` and a `redirect_from` list, so a row would duplicate one source (Q11 sizing). Opened as the Q30 source-tree leg. Flip: if the rendered page and this file ever state different rules. |
| `content/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md` in github/docs (200, 5,684 B, sha256 `ed823a4f…`, 20:05:22Z) | Same reason against row 1; the source carries only `{% data variables.copilot.copilot_cli_short %}` substitutions and a category comment. Q30 source-tree leg. |
| `https://raw.githubusercontent.com/github/copilot-cli/main/changelog.md` (200, 289,859 B, sha256 `c4b793bd…`, 20:04:37Z) | Byte-identical to the pinned-commit fetch (`diff -q` empty, same sha256 at 20:05:42Z); the pinned URL in S042 is the citable one, so an unpinned row would be a moving target. |
| A **new row** for `https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md` | That artifact is already **S042** at the same commit with the identical bytes (`c4b793bd…`, 289,859 B). A second row would duplicate the source, and a `supersedes S042` marker would falsely retire S042's MCP-instruction teach, which `corpus/knowledge/mcp-server-instructions-round52.md` cites. Routed as §7 item 2 instead: the instruction-file anchors are `:271`, `:364`, `:1110`, `:2050`, `:2292`, `:3086` in S042's bytes. |
| `/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions.md` | 404 (502 B) at 20:04:37Z; the non-`.md` route 301s to the canonical page (20:04:42Z). A stale path, exactly the Q30 hazard. |
| `/en/copilot/how-tos/copilot-cli/customize-copilot/cli-best-practices.md` | 404 (502 B) at 20:06:37Z; the file exists in the directory inventory but not at that route. No claim needs it. |
| Copilot CLI overview page `.../customize-copilot/overview.md` (200, 4,304 B, sha256 `38f2e097…`, 20:06:37Z) | Redundant: it says only that "a copy of these instructions is added to your prompt" (`:9`), which row 2 grounds with a locatable sentence (`:126`). Opened as a sweep witness. |
| `https://agents.md/` | Not opened by me this round; already queued as S004 and no claim of mine rests on it. Not admitted, not rejected on content. |
| `https://code.claude.com/docs/en/memory.md` | Out of my target client. The plan names it as C2's basis and names a wave-1 seat as its row author; I did not open or cite it. |

## 6. Gate record

| source | URL | UTC | HTTP | bytes | sha256 | quote | line |
|---|---|---|---|---|---|---|---|
| CLI custom instructions | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 2026-10-22T20:05:13Z | 200 | 8,730 | `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980` | "When multiple applicable user-level and repository instruction files exist, Copilot CLI combines their instructions." | `copilot-cli-custom-instructions.md:30` |
| CLI custom instructions | same | 2026-10-22T20:05:13Z | 200 | 8,730 | same | "use `@` followed by a relative path to include another file" | `:48` |
| CLI custom instructions | same | 2026-10-22T20:05:13Z | 200 | 8,730 | same | "File references are not expanded in `GEMINI.md` or `*.instructions.md` files." | `:50` |
| Concepts | https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions.md | 2026-10-22T20:04:59Z | 200 | 14,669 | `6e7964dc1951c64c1b740b70e0353e56de6ae100805347b99440f050416de933` | "Most surfaces and clients, including Copilot CLI, Visual Studio Code and Visual Studio, combine applicable instruction files without defining a general precedence order." | `custom-instructions.md:84` |
| Repository instructions | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | 2026-10-22T20:04:48Z | 200 | 22,858 | `c29d67f0a342f2ae8de6bda04b8c7e7ce9a1341d61eaffdeee9a4fc8c9ced635` | "When Copilot is working, the nearest `AGENTS.md` file in the directory tree will take precedence." | `repository-instructions.md:31` |
| Repository instructions | same | 2026-10-22T20:04:48Z | 200 | 22,858 | same | "Instructions must be no longer than 2 pages." | `:63` |
| Support matrix | https://docs.github.com/en/copilot/reference/custom-instructions-support.md | 2026-10-22T20:04:59Z | 200 | 14,612 | `90150f5a25f493640b9a52da6ac0a363ece8ece13429bd2c6c4e5ebb0c44e814` | `<code>AGENTS.md</code>, <code>CLAUDE.md</code>, <code>GEMINI.md</code> or <code>REVIEW.md</code> files` | `custom-instructions-support.md:44` |
| Support matrix | same | 2026-10-22T20:04:59Z | 200 | 14,612 | same | `<code>AGENTS.md</code>, <code>CLAUDE.md</code> or <code>GEMINI.md</code> files` (Copilot CLI list) | `:254` |
| Docs reusable | https://raw.githubusercontent.com/github/docs/main/data/reusables/copilot/custom-instructions-agents.md | 2026-10-22T20:05:22Z | 200 | 329 | `ee14953c9296697b98614614c0dfb137655ed2c57371089a8dda53e632f349a7` | "the nearest `AGENTS.md` file in the directory tree will take precedence" | `:1` |
| Docs source (CLI page) | https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md | 2026-10-22T20:05:22Z | 200 | 5,684 | `ed823a4fd8e6d1fda61c8971262b2ad92360c1cf420284fad45ac91afa6dd1e8` | "Copilot CLI combines their instructions" (as `{% data variables.copilot.copilot_cli_short %}`) | `:43` |
| Docs source (repository page) | https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions.md | 2026-10-22T20:05:13Z | 200 | 13,608 | `04cf53d3969c4fe03988f0d25d7bc24e8590320f7e6c28041b1931105ba2c3a4` | "Instructions must be no longer than 2 pages." | `:74` |
| CLI changelog (pinned) | https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md | 2026-10-22T20:05:42Z | 200 | 289,859 | `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb` | "Expand @-style imports in AGENTS.md, CLAUDE.md, and Copilot instruction files" | `changelog.md:1110` |
| CLI changelog (pinned) | same | 2026-10-22T20:05:42Z | 200 | 289,859 | same | "Combine all custom instruction files instead of using priority-based fallbacks" | `:3086` |
| CLI changelog (pinned) | same | 2026-10-22T20:05:42Z | 200 | 289,859 | same | "Custom instructions, MCP servers, skills, and agents are now discovered at every directory level from the working directory up to the git root" | `:2292` |
| CLI custom agents | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | 2026-10-22T20:06:37Z | 200 | 8,379 | `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2` | "the subagent does not follow your repository's custom instructions by default" | `create-custom-agents-for-cli.md:133` |
| Directory inventory (Q30 aid) | https://github.com/github/docs/tree/main/content/copilot/how-tos/copilot-cli/customize-copilot | 2026-10-22T20:06:29Z | 200 | 247,109 | `8f90735849fef65c673ba91f4589e18dd6c26f66cd51bb8177438820a90bbebf` | — (file-name list only; API tree route was 403 rate-limited) | `cli-dir.html` |
| Stale path probe | https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions.md | 2026-10-22T20:04:37Z | 404 | 502 | not hashed | — | — |
| Redirect target | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions | 2026-10-22T20:04:45Z | 200 (via 301) | 708,144 | not hashed (HTML) | — | — |

Every quote above is ≤25 words and byte-exact in the named file; table-row quotes in the support page include the `<code>` markup because the prose is HTML, and are identified as such.

## 7. Findings, limits, out of scope

1. **Row status is contingent.** `status: mined` requires the `used-by` path to exist. `corpus/knowledge/alwayson-rule-files-round53.md` does **not** exist at base (`ls corpus/knowledge/` shows `alwayson-checklist-round7.md` only). If the entry is not landed, all six rows must be written `queued`, not `mined`.
2. **The changelog needs a scope decision, not a row.** S042 already holds this artifact at this commit and hash, with an MCP-instructions scope. The instruction-file facts I cite (`:271`, `:364`, `:1110`, `:2050`, `:2292`, `:3086`) fall outside that scope cell. Two clean options for the L1: append a dated scope clause to S042 (append-only correction, no new row), or write a new row whose `teaches` carries both the new facts and S042's MCP facts and whose `supersedes` cell names S042 — but then `mcp-server-instructions-round52.md` must be checked so its `source: … S042 …` line is not left pointing at a superseded row (Q29). I did not choose between them; a duplicate row would be the defect.
3. **Two clients disagree by design on co-existing files.** Copilot CLI combines `AGENTS.md` + `CLAUDE.md` + `GEMINI.md`; the Copilot cloud agent takes the nearest `AGENTS.md`; Claude Code (plan basis) reads `CLAUDE.md` only. So the `two-rule-files` FAIL is a portability verdict; the instrument's detail string should name the client whose behaviour makes it fail (Q20), and the knowledge entry should not present it as a Copilot CLI error.
4. **Symlink redirect remains single-sourced.** Only Claude Code documents it. Copilot CLI is *not checked* (§3.2). No instrument text should attribute symlink following to Copilot.
5. **`REVIEW.md` is a fourth name on a Copilot surface** (code review on GitHub.com, `custom-instructions-support.md:44`), not on the CLI. A canonical-name rule scoped to "Copilot" must say which surface.
6. **`@AGENTS.md` inside `CLAUDE.md` is documented behaviour, but the docs never show that exact literal** — only "`@` followed by a relative path". The counter's PASS case is sound; the knowledge entry should mark the literal as `[INFERENCE]` from the documented form.
7. **Always-on text does not reach Copilot CLI subagents** without `include-custom-instructions: true` (`create-custom-agents-for-cli.md:133-149`, `changelog.md:364`). Any claim that a single always-on file governs all Copilot work in a repo is false for subagents.
8. **Not measured, by construction.** I ran no instrument, no counter, no gate, and no build. This report records vendor documentation only; it is not a measurement of any Copilot binary, and no Copilot binary was executed (no `copilot` invocation of any kind).
9. **Evidence locations.** Fetched bytes and headers: `/fast/scratch/hyaku/kotoba-r53/ScribeCopilotCli/fetch/` (`repository-instructions.md`, `custom-instructions.md`, `custom-instructions-support.md`, `copilot-cli-custom-instructions.md`, `copilot-cli-changelog.md`, `copilot-cli-changelog-pinned.md`, `docs-src-add-repository-instructions.md`, `src_*`, `probe_*`, `cli-dir.html`, `h_*.txt`).
