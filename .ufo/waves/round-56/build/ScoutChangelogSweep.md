# Q30 sweep — agent-definition location / file-format changes, 2025–2026 (seven C1 clients)

Result: DONE — all seven clients checked on both legs where the leg exists (Claude Code and Cursor publish no docs source tree; Codex's site docs source is unpublished — those legs are recorded `not checked`, never `silent`), and each client has at least one dated 2025–2026 record of an agent-definition location or file-format change (Claude Code 2025-07-24 introduction + 2026-07-01 `/agents` wizard removal; Codex TOML `.codex/agents/`; VS Code 1.106 chatmodes→agents rename; Copilot CLI 2026-03-02 user path change; Gemini CLI 2026-03-16/03-31 flag default-on; Cursor 2.4 2026-01-22 subagents release; opencode 2026-01-17 plural-forms rename).

Seat: KotobaR56.ScoutChangelogSweep (leaf, no dispatch). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin at e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8 (read-only; nothing in the lane written except this report). No tool installs or upgrades this seat; no pacman transaction attempted.

Access window (all fetches): `date -u` → `Fri Oct 23 02:46:59 AM UTC 2026` (start) and `Fri 23 Oct 2026 02:51:55 AM UTC` (end). Every URL below was opened with `curl -sSL --max-time 60 -A "Mozilla/5.0 (compatible; omp-scout)"`; status is curl's `%{http_code}`, bytes `%{size_download}`/file size, sha256 of the saved bytes. Artifacts: /fast/scratch/hyaku/kotoba-r56/ScoutChangelogSweep/ (96 files). Quotes are byte-exact except where marked `[md stripped]` (I removed markdown emphasis/backticks); line numbers are 1-based in the fetched bytes.

This is falsify-wave / entry-§Limits evidence, **not** a SOURCES row proposal. No row, quote or path here is offered as a C1 source; the L1 decides.

---

## 1. Claude Code

**Changelog (leg 1 — open).** `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md` — 200, 1,081,887 B, sha256 `adb803f8e1d19f3f678b8374de6db1223e9cb8afe2f8034f4b7cb618989997d9`.
- Location/format change: subagents introduced in `## 1.0.60` (heading at line 8985). Line 8987: `- You can now create custom subagents for specialized tasks! Run /agents to get started` (25 words). The changelog carries no dates; npm registry (`https://registry.npmjs.org/@anthropic-ai/claude-code`, 200, 1,556,915 B, sha256 `e220ac7cc9785b740b53e5c53c3473b61f72d0d1e5e7b93099cd685242ee8908`) gives `"1.0.60": 2025-07-24T20:52:22.104Z`.
- Line 4812, under `## 2.1.198` (npm `2026-07-01T16:50:16.245Z`): `- Removed the /agents wizard; ask Claude to create or manage subagents, or edit .claude/agents/ directly` [md stripped] — the file became the primary surface.
- Line 6115, `## 2.1.121` (npm 2026-04-27): `--dangerously-skip-permissions` no longer prompts for writes to `.claude/skills/`, `.claude/agents/`, `.claude/commands/`.
- Line 7691/7703, `## 2.1.47` (npm 2026-02-18): custom agent `model` field in `.claude/agents/*.md`; project-level `.claude/agents/` now discovered from a git worktree. Line 7753, `## 2.1.43`: "Fixed spurious warnings for non-agent markdown files in `.claude/agents/` directory".
- No change of the `.claude/agents/*.md` form itself appears in the changelog: the form is stable from 1.0.60 (2025-07) to 2.1.309 (head).

**Docs source tree (leg 2 — NOT CHECKED, not published).** anthropics org repo listing pages 1–2 (`https://api.github.com/orgs/anthropics/repos?per_page=100`, 200, 605,022 B, sha256 `1a49fd40ca6f7a5de8b831f65fec8d845df3cb3bdcdef9d5e7e322ecfdf02f37`; `…&page=2`, 200, 96,088 B, sha256 `355e2e4952dbf1705a962b5547ef19f4badf15963647f53fb515d1a5c23cfea3`) contain no docs/website repo. `https://api.github.com/repos/anthropics/claude-code/contents/` (200, 13,800 B, sha256 `412f4420deecb479a1d407320cf53bcbac815712f3040dd950d0a233b10eb193`) has no `docs/` entry. The live docs (code.claude.com/docs) were not opened by this seat.

**Lane corpus grep (leg 3).** No `.claude/agents` occurrence anywhere under `corpus/`.

## 2. Codex

**Changelog (leg 1 — open, pointer).** `https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md` — 200, 330 B, sha256 `c8458f99de91a4b4b9682ecb72c396f0d08c03c51a657759e1239c3a14c697d5`. Line 1: `The changelog can be found on the [releases page](https://github.com/openai/codex/releases).`
Release notes: `https://api.github.com/repos/openai/codex/releases?per_page=100` — 200, 36,264,273 B, sha256 `790b4cc61c6a0353558519967f2ce7a8954a89ec9c4ee2bd45ef6fc8252bbfe1`; window **rust-v0.158.0-alpha.14 (2026-09-25) → rust-v0.164.0-alpha.12 (2026-10-22)**. Subagent entries in the window, none of them a location or format change:
- rust-v0.163.0 (2026-10-15): `#52241 Preserve subagent capabilities independently of forked history`
- rust-v0.162.0 (2026-10-08): `#50082 Enable dynamic tool inheritance for fresh V2 subagents`
- rust-v0.161.0 (2026-10-07): `#49312 Notify parent agents when Guardian stops a subagent`
- rust-v0.160.0 (2026-10-01): `Subagents now retain environments that are still starting and receive their configuration or preparation failure.`
Older than the 100-release window: not reachable via this endpoint (unresolved, §Limits).

**Live docs page (evidence for the entry's Codex cell, and a format fact).** `https://developers.openai.com/codex/agent-configuration/subagents` — 200, 614,442 B, sha256 `bf21f1997d6de96ef1b5293d8bedb1961681f0d07e02133515e4e020a7d4bb43`. Verbatim (HTML tags stripped, byte text of the sentence): `To define your own custom agents, add standalone TOML files under ~/.codex/agents/ for personal agents or .codex/agents/ for project-scoped agents.` (22 words; backticks are `<code>` in the page). **Codex agent definitions are TOML, not markdown** — example files named on the page: `.codex/agents/pr-explorer.toml`, `reviewer.toml`, `docs-researcher.toml`, `code-mapper.toml`, `browser-debugger.toml`, `ui-fixer.toml`. A "What the file sets" cell that says "markdown with frontmatter" for Codex would be wrong.

**Docs source tree (leg 2 — partial).** `https://api.github.com/repos/openai/codex/contents/docs` — 200, 11,226 B, sha256 `d8932f581b54608340a69eeede8f97ec8aa71854300bd714515559ce8ea8da5b`; names: CLA.md, agents_md.md, authentication.md, config.md, contributing.md, example-config.md, exec.md, execpolicy.md, getting-started.md, install.md, license.md, open-source-fund.md, sandbox.md, skills.md, slash_commands.md — **no subagents or agent-definition file**. Repo root (`https://api.github.com/repos/openai/codex/contents/`, 200, 30,614 B, sha256 `110a249d1e0e891764668b8b00795b1892fd03a26f4f120fc16caf4ab5cb184e`) has no website/docs-source directory; openai org repo listing (`…/orgs/openai/repos?per_page=100`, 200, 538,341 B, sha256 `af50d72225d157d1b07f3a2c60f03247ffdf9ed57f203cdac36df492c4047012`) has no docs site repo. So the site page's own introduction date is not pinned by any changelog I could open: the dated changelog page (`https://developers.openai.com/codex/changelog`, 200, 1,714,171 B, sha256 `ff7fcbe9319a5eb49a7eb9eafc6bcad824c41061ea3fd1825435dabe8a51a772`) has exactly one date-anchored subagent mention — `2026-03-17 … GPT-5.4 mini … for lighter coding tasks and subagents` — which is a model note, not the doc's introduction.

**Lane corpus grep (leg 3).** No `.codex/agents` occurrence under `corpus/`.

## 3. VS Code

**Release notes = the changelog source (leg 1 — open).** Source tree `https://api.github.com/repos/microsoft/vscode-docs/contents/release-notes` (200, 132,281 B, sha256 `d1c990e2ca6d9c89a02125de21ace2fe5429a9579a25a26be9ef701597889df8`) runs to **v1_144.md**; I fetched and keyword-swept v1_106–v1_144 (37 files, listed below). `CHANGELOG.md` at microsoft/vscode root is 404 (14 B) — the release notes are the changelog.

The rename, `https://raw.githubusercontent.com/microsoft/vscode-docs/main/release-notes/v1_106.md` — 200, 72,864 B, sha256 `fb91838862affe99a6669abc52d37f73e596cc0932b11aff2e6b94a668ec2340`:
- line 162: `### Chat modes renamed to custom agents`
- line 164: `Chat modes have been renamed to custom agents throughout VS Code to better align with terminology used in other environments.`
- line 168: `When you create custom agents, the definition files are now located in .github/agents in your workspace.` [md stripped] — the sentence continues `These files can use the .agents.md suffix and can also be used as GitHub Copilot Cloud Agents and CLI Agents.` Note line 176 says `Custom agent .agent.md files now accept an additional target frontmatter property` — the same page uses both `.agents.md` (168) and `.agent.md` (176) for the suffix.
- line 172: `If you have existing custom chat modes (.chatmode.md files in .github/chatmodes), they continue to work and are automatically treated as custom agents.` [md stripped] — plus a quick fix that migrates them.
- line 174/176: custom agent metadata section; line 191 links `docs/agent-customization/custom-agents`.
- v1_107 (`…/release-notes/v1_107.md`, 200, 65,163 B, sha256 `cedd1d93438e1dd0504bbe9ce9fadb0b5062f41ed8d2e6c47b299d139b34b877`): line 208 custom agents in `.github/agents` now appear in Background Agents; line 242 `To prevent a custom agent from being used as a subagent, set the metadata property infer to false in the *.agent.md file.` [md stripped]
- Sweep v1_108–v1_144: **no further location change**. Hits only: v1_109 (organization-level custom agents, 91,591 B, sha256 `cf04c2ec0e16f791be568514b6d300a8497176cafa5af17e71586df21ed64b23`), v1_110 (`/agents` command), v1_111 (agent-scoped hooks in `.agent.md` frontmatter), v1_112/113 (discovery, Chat Customizations editor), v1_133 (portable customization packages), v1_136 ("Support reasoning effort in custom agent files", PR #329263). v1_108, v1_114, v1_116–117, v1_119–132, v1_134–135, v1_137–144: 0 hits.

**Current docs source tree (leg 2 — open).** `https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md` — 200, 16,522 B, sha256 `55c90b711eeffb0605b78c11c1cc09b057e28e70c6275a7e046a2c4334fff045`:
- line 117 `## Custom agent file locations`; line 123 `| Workspace | .github/agents folder | .agent.md or .md files |` [md stripped]
- line 125 `| User (…Copilot…) | ~/.copilot/agents folder | .agent.md or .md files |` [md stripped] — the current VS Code doc gives the **user-level** location as `~/.copilot/agents`, not a `.vscode` path; line 141 says to prefer "native harness folders, such as `.github/agents` and `~/.copilot/agents`", and line 143 notes Copilot CLI and the Copilot app do not inherit editor location settings.
- line 197 `If you have existing .chatmode.md files, rename them to .agent.md and place them in one of the supported custom agent locations.` [md stripped]
- Companion reference doc `docs/agents/reference/custom-agent-file-reference.md` — 200, 12,003 B, sha256 `1860f1ba79b085b542364a0457a642ba32d407deef588ef97e877164433186ca` (syntax, frontmatter, harness-specific fields).
- Full tree check `https://api.github.com/repos/microsoft/vscode-docs/git/trees/main?recursive=1` (200, 2,537,214 B, sha256 `3f562287b22732818f8559876fb77128eb663ccbca725f0895ae71e12588fbd2`): **zero paths containing `chatmode`** — the legacy form survives only as prose migration text, and `.chatmode.md`/`.github/chatmodes` are documented as still-loaded legacy.

**Lane corpus grep (leg 3).** No `.github/agents`, `.vscode/agents`, `.agent.md` or `chatmodes` occurrence under `corpus/`.

## 4. Copilot CLI

**Release notes (leg 1 — open).** `https://api.github.com/repos/github/copilot-cli/releases?per_page=100` — 200, 3,853,741 B, sha256 `6b02ce4c5e42d482dba4e03bbe3a1d81292d60d66bd7bfd77188ccae7706ce2d`; window **v1.0.83-2 (2026-09-02) → v1.0.103 (2026-10-22)**. No chatmode or location change in the window. Nearest: v1.0.97 (2026-10-13) `Add agent-scoped declarative hooks for custom agents` and `Discover all custom agents even when repositories define more than 100 or nest agent files deeply.`; v1.0.100 (2026-10-19) `Custom agents that declare the documented search, web or todo tool aliases…`. `https://raw.githubusercontent.com/github/copilot-cli/main/CHANGELOG.md` is 404 (14 B) — releases are the changelog.

**Docs source tree (leg 2 — open, public).** `https://api.github.com/repos/github/docs/git/trees/main?recursive=1` — 200, 3,889,749 B, sha256 `fd281e4fb36494739712d6dcbf88d78f07d02304fe0907816e3257c7eadff97e`: **zero paths containing `chatmode`** under the whole repo, so `.github/chatmodes` has no current documentation. Current CLI doc `https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md` — 200, 9,907 B, sha256 `f94dc9baf904179ef502908c1a61f0df288971ac1c3f75324d4002b44e1facfa`: line 29 `Each … is defined by a Markdown file with an .agent.md extension.` [md stripped]; line 35 `* **Project** (.github/agents/)`; line 36 `* **User** (~/.copilot/agents/)`; line 39 gives the id rule (file name without `.agent.md`/`.md`, personal beats repository).
- **Dated location change:** commit `ca31b28e5aac70bbe6be9f4458615b72af1b3ca7`, 2026-03-02, message `Hubwriter/update agents path (#59941)`; patch (`Accept: application/vnd.github.v3.patch`) 200, 2,851 B, sha256 `676166a44cff520a7d006ae6b60cefa0d4c672beea455e74a4748fe326656e00`, files `content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md` and `content/copilot/reference/custom-agents-configuration.md`, hunk lines 19–20: `-   * **User** (~/.config/copilot/agents/)` / `+   * **User** (~/.copilot/agents/)`. The user-level directory moved from `.config/copilot/agents` to `.copilot/agents`.
- Doc file history (commits API, 200, 60,289 B, sha256 `52fa79397ecdcf2d92fc0d4d2ed0e725172f5ffadc14fd2a5aeda47e4beb7a0f`, 13 commits): earliest 2026-02-16 `Copilot CLI: add Customization map topic and articles (#59601)`; 2026-09-30 `Correct Copilot CLI custom agent precedence (#63589)`; 2026-10-19 `Copilot CLI: Update modes, agents, and delegation articles (#64243)`.

**Lane corpus grep (leg 3).** No `.github/agents`, `.copilot/agents`, `.config/copilot/agents` or `chatmodes` occurrence under `corpus/`.

## 5. Gemini CLI

**Release notes (leg 1 — open).** `https://api.github.com/repos/google-gemini/gemini-cli/releases?per_page=100` — 200, 778,103 B, sha256 `05202dca3a406c42692f87a984702ca15d6378b7cd7051432be55c90fb41e57b`; window **v0.54.4 (2026-08-07) → v0.67.0-nightly.20261023 (2026-10-23)**. Only SSR-agent fixes: v0.57.0 (2026-08-25) `[SSR Agent] Issue Fix (22093): Prevent subagents from running when agents mode is disabled`; v0.56.0-nightly.20260818 `Format cli_help subagent output as markdown`. The introduction predates the window; the docs repo's own changelog files (`docs/changelogs/latest.md`, 200, 5,916 B, sha256 `bbbe4712fe5991cf5bebc741e1c2d963d1c22abe125baa27e7c2c72b59df7d11`; `docs/changelogs/preview.md`, 200, 5,802 B, sha256 `d8580ff5c9598a924c44e44934a50b0a4154c5aa6f8e896c5824116265231306`) contain no `subagent`/`enableAgents` line.

**Docs source tree (leg 2 — open).** `https://api.github.com/repos/google-gemini/gemini-cli/contents/docs` (200, 19,477 B, sha256 `63a5e5e680accb0b95d07577d610a502806051e833fe53c681155d14d5f6de8b`) contains `docs/core/subagents.md`. `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/core/subagents.md` — 200, 23,610 B, sha256 `1a1b38993a2f5c6e16afda1914974a86274e73fac90e3ab62334d45e34bf7849`:
- line 323 `1.  **Project-level:** .gemini/agents/*.md (Shared with your team)` [md stripped]
- line 324 `2.  **User-level:** ~/.gemini/agents/*.md (Personal agents)` [md stripped]
- line 591 `Subagents are enabled by default. To disable them, set enableAgents to false` [md stripped], with line 596 JSON `"experimental": { "enableAgents": false }`.
- Config reference `https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/reference/configuration.md` — 200, 102,685 B, sha256 `4b86e73ee6da5b18ec0515c3fbf12b9b72fb07fbb545fa93362507596cbc64f4`: line 2133 `` **`experimental.enableAgents`** (boolean) `` / line 2135 `- **Description:** Enable local and remote subagents.` (also line 2126 `experimental.adk.agentSessionSubagentEnabled`).
- **Dated flag history** (commits API for `docs/core/subagents.md`, 200, 108,343 B, sha256 `1b47d895842df52a68d37801ffdd11449255a9686226eb1101e4ce62f794de69`, 24 commits): 2026-01-27 `Sub-agents documentation. (#16639)` (doc created); 2026-01-29 `docs: mark A2A subagents as experimental in subagents.md (#17863)`; 2026-03-13 `docs: overhaul subagents documentation and add /agents command (#22345)`; **2026-03-16 `feat: enable subagents (#22386)`**; **2026-03-31 `docs: update subagents docs to not be experimental (#24343)`**; 2026-06-08 `chore: remove experimental text from browser agent docs (#27746)`. So the flag went from an experimental opt-in (Jan–Mar 2026) to default-on; the current reference still files `enableAgents` under `experimental`.

**Lane corpus grep (leg 3).** No `.gemini/agents` occurrence under `corpus/`.

## 6. Cursor

**Release notes (leg 1 — open).** `https://cursor.com/changelog` — 200, 204,106 B, sha256 `f1bb810497168fff3aa28afab07c4a0b3b1eeb9c069ca23ddaf782b18486d15a` (single-page HTML; latest entry is Projects, whose text says it "delegates tasks to thousands of subagents"). Feed `https://cursor.com/changelog/rss.xml` — 200, 128,193 B, sha256 `77de1812638d8be2d5aacdc3288e46073c7ddda117940a68b55f2a157939846f`. The subagents release: `https://cursor.com/changelog/2-4` — 200, 164,274 B, sha256 `fce9591e6eedc3531083236f53ea2799f8f6ebed5684f8433c6dd9af164773f7`, title `Subagents, Skills, and Image Generation · Cursor`, canonical `https://cursor.com/changelog/2-4`, page date text `Jan 22, 2026`. Verbatim: `Subagents, independent agents that handle discrete parts of a task in parallel…` (context) and `Optionally, you can define custom subagents. Learn more in our docs` (12 words) — the custom-definition capability arrives with 2.4.

**Live docs (substitute for leg 2; source tree NOT CHECKED).** `https://cursor.com/docs/agent/subagents` — 200, 676,361 B, sha256 `c9d06bc2e1cee8f39d64b115f51d13e21018549675c1958e533d23528b531264`, title `Subagents | Cursor Docs`. Verbatim (tags stripped): `You can also create subagents manually by adding markdown files to .cursor/agents/ (project) or ~/.cursor/agents/ (user).` (19 words) and `Add subagents to version control — Check .cursor/agents/ into your repository so the team benefits.` The page's location table also carries **compatibility** rows `.claude/agents/` and `~/.claude/agents/` (Cursor reading Claude Code's form) — a compatibility path is not Cursor's own form, which is exactly the distinction the C1 counter's `OWN_ROOTS` draws. No public Cursor docs source repo was found: `https://cursor.com/sitemap.xml` (200, 32,165 B, sha256 `e0965a53b6751009a53d59a1f4898efbb9ff89166de940722289816c34722366`) lists no docs agent URL and no docs source. So leg 2 for Cursor = **not checked** (docs site is the only published form).

**Lane corpus grep (leg 3).** No `.cursor/agents` occurrence under `corpus/`.

## 7. opencode

**Release notes (leg 1 — open).** `https://api.github.com/repos/sst/opencode/releases?per_page=100` (redirects to `api.github.com/repositories/975734319/…`) — 200, 6,180,413 B, sha256 `d06944100528e918662c064ff0a70df7d37e970b501c755a21f63448c05eff25`; window **v1.14.32 (2026-05-02) → v1.19.4 (2026-10-22)**. **No `agent/` vs `agents/` mention** in the window — the rename is recorded in the docs tree, not in release notes.

**Dated location change (docs tree, leg 2 — open).** Commit `58f7da6e9f8fb08a9f42a0d2cc34a18b2475ddea`, 2026-01-17, message `docs: document the plural forms`; patch 200, 17,894 B, sha256 `1cac434c4850aaf254deb7516c8bfb92ad26797e4dc3be371041695914ee387a`, 8 files. Hunk lines 25–28: `- Global: ~/.config/opencode/agent/` / `- Per-project: .opencode/agent/` / `+ Global: ~/.config/opencode/agents/` / `+ Per-project: .opencode/agents/` [md stripped]; line 158 added: `The .opencode and ~/.config/opencode directories use plural names for subdirectories: agents/, commands/, modes/, plugins/, skills/, tools/, and themes/. Singular names (e.g., agent/) are also supported for backwards compatibility.` [md stripped] (31 words — the 3–25-word C1 quote limit means this sentence cannot be a quote as-is; the shorter path line can).
Current docs, dev branch: `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/content/docs/agents.mdx` — 200, 21,066 B, sha256 `1f805f8a7cd1d877272d61ad6d59dae4d014c7b26009110d1c4b26c65a634dcc`, line 205 `- Global: ~/.config/opencode/agents/`, line 206 `- Per-project: .opencode/agents/`; docs dir listing (`https://api.github.com/repositories/975734319/contents/packages/web/src/content/docs`, 200, 43,690 B, sha256 `2d5a6545066d997d664a687997be8fbf9fb87defddd19de3dcc6923981beb286`) has `agents.mdx` (no `agent.mdx`). The file's own history (commits API, 200, 165,212 B, sha256 `8c75e419a832dfb74ff56a670165ebb8f73d3fd2a568c2557813d71126a2d564`, 40 commits) starts 2025-09-03, so `agents.mdx` as a filename predates the January 2026 content change; the January commit is where the **directory** form became plural in the docs.

**Format nuance (matters for "What the file sets").** `https://raw.githubusercontent.com/anomalyco/opencode/dev/packages/web/src/content/docs/config.mdx` — 200, 26,473 B, sha256 `61701752764534dec13663edf44945c60bb3b4672a6f24291f5c3c5d23d8647d`, line 507: `You can configure specialized agents for specific tasks through the agent option.` [md stripped] (JSON example at line 512 uses `"agent": { … }`). Directories are plural; the **config key stays singular `agent`**.

**Lane corpus grep (leg 3).** `~/.config/opencode/agents/` is present under `corpus/` (e.g. `corpus/knowledge/agent-def-audit-round6.md:5`, `corpus/knowledge/agent-defs-commands-and-round-prompts.md:9`, `corpus/knowledge/instruction-surface-census-round13.md:493`); `instruction-surface-census-round13.md:495-498` additionally records that opencode **also loads the singular `agent/` directory** (`~/.config/opencode/agent/ufo.md` live, loader doc table says `agent(s)/<name>.md`). Consistent with the 2026-01-17 backwards-compatibility sentence.

---

## Cross-client summary — change timeline (2025–2026)

| Client | Dated change | Date | Form after the change |
|---|---|---|---|
| Claude Code | subagents introduced (`/agents`); 2.1.198 removes the wizard, points at the directory | 2025-07-24 (npm 1.0.60); 2026-07-01 | `.claude/agents/*.md` (markdown + frontmatter) |
| Codex | custom agents documented as TOML under the agents dir (doc introduction date unresolved) | page live 2026-10-23; changelog window 2026-09-25+ | `~/.codex/agents/`, `.codex/agents/` — **TOML** |
| VS Code | chat modes → custom agents; `.chatmode.md` in `.github/chatmodes` → `.agent.md` in `.github/agents` | 1.106 (Oct 2025 release notes; 1.107 dated 2025-12-10) | `.github/agents/*.agent.md`; legacy `.chatmode.md` still loaded; user scope `~/.copilot/agents` |
| Copilot CLI | user-level agents dir moved `~/.config/copilot/agents/` → `~/.copilot/agents/` | 2026-03-02 | `.github/agents/` (project), `~/.copilot/agents/` (user), `.agent.md` |
| Gemini CLI | subagents documented; flag default-on, doc de-experimentalized | 2026-01-27; 2026-03-16; 2026-03-31 | `.gemini/agents/*.md`, `~/.gemini/agents/*.md`; `experimental.enableAgents` |
| Cursor | subagents released, including custom subagent definitions | 2026-01-22 (2.4) | `.cursor/agents/*.md`, `~/.cursor/agents/*.md`; compat `.claude/agents`, `.codex/agents` |
| opencode | directory form pluralised in the docs (singular kept for backwards compatibility) | 2026-01-17 | `.opencode/agents/`, `~/.config/opencode/agents/`; config key still `agent` |

## Limits / unresolved (falsify-wave material)

1. **Docs-source-tree legs that do not exist:** Claude Code and Cursor publish no docs source tree; Codex's site docs source is not in openai/codex and no docs site repo is in the openai org listing. For these three the sweep is changelog + live page only. Per the Q30 rule these legs are `not checked`, **not** `silent`.
2. **Windows, not full histories:** release-note endpoints give 100 releases. Copilot CLI covers 2026-09-02+, Gemini CLI 2026-08-07+, Codex 2026-09-25+, opencode 2026-05-02+. Anything before those windows is unreached here (Gemini's subagents introduction was recovered from the docs-file commit history instead).
3. **Codex page introduction date is unresolved** — the live `/codex/agent-configuration/subagents` page exists and says TOML, but no changelog I opened dates its publication.
4. **Cursor page dates** come from the changelog entry's own text (`Jan 22, 2026`), not from a machine-readable date field (the page HTML carries none); the RSS feed exists but was not parsed for that entry by this seat.
5. **A C1 quote cannot be taken from opencode's plural-names sentence** (31 words) or from the opencode release notes (no such line); the shortest verbatim path line is the one at patch line 27/28 or `agents.mdx:205-206`.
6. **Cross-check for the entry's Codex row:** the counter's `OWN_ROOTS` for Codex is `.codex`; the live page's own-scoped path is `.codex/agents/` and the personal one is `~/.codex/agents/` — both normalise to `.codex/agents`, which is **held at base** (`.codex/agents` appears in base text), so a Codex row can be in the table but cannot count as new ground.
7. Nothing in this sweep was written into the lane besides this report; no SOURCES row, no entry text, no counter change is proposed here.
