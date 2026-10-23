# ScoutAgentSpec — is there a shared, cross-client specification for agent-definition files?

Result: DONE — no vendor-neutral specification for agent-definition (subagent / custom-agent) files exists: agentskills.io
and agents.md cover other artifacts entirely, and the published Agent Plugins v1.0.0 standard names agents as out of
scope; the only documented cross-client interop is directory *reading* (Cursor reads `.claude/agents/` and
`.codex/agents/`; VS Code reads `.claude/agents` in the "Claude agent format"), and there is no shared field schema —
Codex's files are TOML, the other six clients' are Markdown + YAML frontmatter.

Seat: `KotobaR56.ScoutAgentSpec` (round-56 build wave, leaf; no dispatch, no lane writes except this report, no
counters touched, no lane code executed, no git writes anywhere, no model calls). Read-only git in the lane at
`e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`; scratch artifacts under
`/fast/scratch/hyaku/kotoba-r56/KotobaR56.ScoutAgentSpec/` (fetch bodies in `fetch/`, `fetch/s/`, `fetch/v/`,
`fetch/p/`, per-run manifest lines in `fetch/*/log.txt` and `fetch/log.txt`). No tool installs or upgrades; no pacman
transaction attempted.

Access window: `date -u` → `Fri 23 Oct 2026 02:46:37 AM UTC` (start) … `Fri 23 Oct 2026 02:51:31 AM UTC` (last fetch).
Method: ordinary `curl -sS -L --max-time 45` with a plain UA; every fetch line records URL, UTC timestamp, curl exit,
HTTP status, bytes and sha256 of the saved body. Quotes are byte-exact from the saved bytes; backticks/markdown are
preserved unless marked `[md stripped]`. Line numbers are 1-based in the fetched file; byte offsets are given for
single-line HTML. Nothing here was produced with a headless browser or any challenge-solving tool.

This is C1 depth material (entry prose / SKILL.md "Action" cells / lesson § Gate context), **not** a SOURCES row
proposal and not a claim receipt. The L1 decides. Sibling seats already cover the per-client Q30 changelog sweep
(`build/ScoutChangelogSweep.md`) and the base-held analysis (`build/ScoutHeldAgentDefs.md`); this report covers the
interoperability question only and does not duplicate them.

---

## 1. The direct answer: no shared agent-definition specification exists

| Candidate | What it standardises | Does it cover agent-definition files? | Evidence |
|---|---|---|---|
| Agent Skills (agentskills.io) | `SKILL.md` packages | **No** — 0 mentions of `subagent`/`sub-agent`/`agent definition`/`.agents` in the specification page or its markdown source; site index has no such page | §1.1 |
| Agent Plugins v1.0.0 (agent-plugins.org) | portable plugin packaging | **No, by explicit published statement**: "exactly two component types: skills and MCP servers"; agents are named as out of scope | §1.2 |
| AGENTS.md (agents.md) | project instructions ("a README for agents") | **No** — 0 mentions of `subagent` and 0 agent-definition directories on the site | §1.3 |
| Web (official sources only) | — | No adopted cross-client agent-definition spec found; the closest project is a community compiler, not a standard | §1.4 |

### 1.1 agentskills.io specifies skills only

- `https://agentskills.io/specification.md` — 2026-10-23T02:51:09Z, HTTP 200, 7,608 B, sha256
  `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` — **byte-identical to the S018 fetch**
  (`corpus/SOURCES.md:31` records `9a67de89…`, 7,608 B, 2026-10-22), so the page has not changed.
  Case-insensitive grep for `subagent`, `sub-agent`, `agent definition`, `.agents` → **0 matches**.
- `https://agentskills.io/sitemap.xml` — 2026-10-23T02:49:29Z, HTTP 200, 1,504 B, sha256 `a2638d69…` — 9 URLs:
  `client-implementation/adding-skills-support`, `clients`, `home`, `skill-creation/{best-practices,evaluating-skills,
  optimizing-descriptions,quickstart,using-scripts}`, `specification`. **No page about subagents or agent-definition
  files.**
- `https://agentskills.io/llms.txt` — 2026-10-23T02:51:23Z, HTTP 200, 1,374 B, sha256 `d9b01a3a…` — the same 9 docs.
- `https://api.github.com/repos/agentskills/agentskills/git/trees/main?recursive=1` — 2026-10-23T02:51:24Z, HTTP 200,
  60,279 B, sha256 `01ca5002…` — the spec's own docs source tree holds exactly 10 markdown/mdx docs
  (`docs/specification.mdx`, `docs/home.mdx`, `docs/clients.mdx`, `docs/client-implementation/adding-skills-support.mdx`,
  five `docs/skill-creation/*.mdx`, plus READMEs). **No subagent / agent-definition page.**
- `https://agentskills.io/clients.md` — 2026-10-23T02:51:09Z, HTTP 200, 282 B, sha256 `6dabf4e3…` — a stub whose only
  content is a "Client Showcase" heading; it names no agent-definition directory.

### 1.2 Agent Plugins v1.0.0 excludes agents by published statement (the strongest single piece of evidence)

- `https://agent-plugins.org/specification.md` — 2026-10-23T02:50:43Z, HTTP 200, 44,846 B, sha256
  `34710a33979953fd884e9b7d69af12a39e3e1e93f465fea2afaa886a5ca82ba0`; fetched as the site's own `.md` variant, so
  the bytes below are the published text.

  Line 279 (§7 Component types):
  > Agent Plugins v1 defines exactly two component types: **skills** and **MCP servers**. Other component types are
  > outside the v1 format and do not affect conformance.

  Line 616 (rationale):
  > Other proposed component types — such as commands, hooks, agents, rules, and LSP servers — remain too
  > client-specific for a stable portable contract and are outside the v1 format until their formats converge.

  Line 285 states the skills component's format source is the Agent Skills specification — i.e. the one cross-client
  artifact format that does exist is `SKILL.md`, and its sibling standard deliberately leaves agent definitions out.
  `[INFERENCE]` The phrase "until their formats converge" is the closest thing to a statement that no convergence
  exists today.

### 1.3 AGENTS.md is about project instructions, not agent definitions

- `https://agents.md/` — 2026-10-23T02:50:44Z, HTTP 200, 81,690 B, sha256
  `06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979` — case-insensitive counts on the whole page:
  `subagent` 0, `sub-agent` 0, `.claude/agents` / `.codex/agents` / `.github/agents` / `.cursor/agents` /
  `.gemini/agents` / `.opencode/agents` / `.copilot/agents` all 0.

### 1.4 Open-web sweep (official sources only) found no adopted standard

A `web_search` for an adopted cross-client agent-definition format returned vendor subagent docs, AGENTS.md
(instructions), Agent Plugins (excludes agents) and community tooling. The one project that states the gap explicitly
— a third-party "supagents" compiler that generates per-client files from one source — is community work, not a
standard, and was not opened by this seat (not a lane source). `[INFERENCE]` Absence of an adopted standard is
supported by the three published artifacts above; the search itself is discovery, not proof.

Lane-corpus leg of the sweep: `grep -rn -i -E "shared (agent|subagent) spec|cross-client (agent|subagent)|agentskills.*(subagent|agent-definition)" corpus/ SKILL.md`
in the lane → 0 matches (exit 1, no output).

---

## 2. Cross-client directory reading — what is actually documented

### 2.1 Cursor reads Claude Code's and Codex's agent directories (strongest interop statement)

`https://cursor.com/docs/subagents.md` — 2026-10-23T02:49:27Z, HTTP 200, 27,660 B, sha256
`264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668` (the rendered page
`https://cursor.com/docs/subagents` was also fetched: 2026-10-23T02:47:31Z, HTTP 200, 676,361 B, sha256
`c9d06bc2…`; the same table is present there).

Lines 83–92 of the `.md` (line 83 is the `### File locations` heading):

```
| Type                  | Location            | Scope                                                |
| :-------------------- | :------------------ | :--------------------------------------------------- |
| **Project subagents** | `.cursor/agents/`   | Current project only                                 |
|                       | `.claude/agents/`   | Current project only (Claude compatibility)          |
|                       | `.codex/agents/`    | Current project only (Codex compatibility)           |
| **User subagents**    | `~/.cursor/agents/` | All projects for current user                        |
|                       | `~/.claude/agents/` | All projects for current user (Claude compatibility) |
|                       | `~/.codex/agents/`  | All projects for current user (Codex compatibility)  |
```

Line 92 (precedence rule, contiguous prose):

> Project subagents take precedence when names conflict. When multiple locations contain subagents with the same name,
> `.cursor/` takes precedence over `.claude/` or `.codex/`.

Cursor's own format (lines 96–124): markdown + YAML frontmatter, fields `name`, `description`, `model`, `readonly`,
`is_background` — **all optional** ("Required: No" for each row).

Hazard / open question: Cursor documents *Codex compatibility* for `.codex/agents/`, but Codex's own documented files
there are TOML (§3). The page does not say whether Cursor parses TOML; `[INFERENCE]` the row is a discovery claim and
format equivalence is unverified.

### 2.2 VS Code reads `.claude/agents` in the "Claude agent format"

The rendered page `https://code.visualstudio.com/docs/copilot/customization/custom-agents` (2026-10-23T02:47:31Z, HTTP
200, 132,660 B, sha256 `288d3754c9f6df8b05b016f6832d072d2aedf14639e1b0a27ffc9002985e99c7`) is Liquid-templated; its
**source** is `https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md`
— 2026-10-23T02:50:21Z, HTTP 200, 16,522 B, sha256
`55c90b711eeffb0605b78c11c1cc09b057e28e70c6275a7e046a2c4334fff045` (path found in the repo tree listing
`https://api.github.com/repos/microsoft/vscode-docs/git/trees/main?recursive=1`, 2026-10-23T02:49:29Z, HTTP 200,
2,537,214 B, sha256 `3f562287…`).

Lines 121–126:

```
| Scope | Default file location | File format |
|-------|-----------------------|-------------|
| Workspace | `.github/agents` folder | `.agent.md` or `.md` files |
| Workspace (Claude format) | `.claude/agents` folder | `.md` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |
| User ({% data variables.product.prodname_copilot_short %}) | `~/.copilot/agents` folder | `.agent.md` or `.md` files |
| User ({% data variables.product.prodname_anthropic_claude %}) | `~/.claude/agents` folder | `.md` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |
```

Line 132: "For Claude-specific fields and compatibility with Local, see the [Claude agent format
reference](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format)."
Line 141: "Prefer native harness folders, such as `.github/agents` and `~/.copilot/agents`, over custom search
locations."
Line 139 (the Local harness keeps its own storage): "The **Local** harness stores user-level custom agents in
{% data variables.product.prodname_vscode_shortname %} profile storage, separate from harness user folders such as
`~/.copilot/agents` and `~/.claude/agents`."

Hazard: lines 125–126 contain Liquid `{% data variables … %}` in the raw source, and the rendered HTML substitutes
product names ("GitHub Copilot", "Anthropic Claude", "VS Code"). A quote must therefore be taken from the URL the row
cites — raw md and rendered page are **not** interchangeable for those two rows. Rows 123–124 have no Liquid and are
identical in both.

### 2.3 What each client documents for its own directory (cross-checked, no other client's dir named)

Counts are case-insensitive substring counts over the fetched bytes listed in §5; "other-client dirs" = the six other
`.<vendor>/agent(s)` forms searched.

| Client | Own location documented | Format | Other-client dirs named? | Source (fetched bytes) |
|---|---|---|---|---|
| Claude Code | `.claude/agents/`, `~/.claude/agents/` (table lines 162–163; line 127 scope prose) | markdown + YAML frontmatter | **no** — `.codex/agents`, `.cursor/agents`, `.gemini/agents`, `.agents/` all 0 | `code.claude.com/docs/en/sub-agents.md`, 111,624 B, sha256 `84b2646c…` |
| Codex | `.codex/agents/`, `~/.codex/agents/` (byte 503,880) | **TOML**, required `name`, `description`, `developer_instructions` | **no** — `.claude/agents` 0 | `developers.openai.com/codex/subagents`, 614,442 B, sha256 `bf21f199…` |
| VS Code | `.github/agents` (native), `.claude/agents` (Claude format) | `.agent.md`/`.md` + YAML frontmatter | **yes — `.claude/agents`** | see §2.2 |
| Copilot CLI | `.github/agents/`, `~/.copilot/agents/` (md lines 25, 27) | markdown, `.agent.md` (line 17) | **no** — `.claude/agents` 0 | `docs.github.com/.../create-custom-agents-for-cli.md`, 8,379 B, sha256 `506783b4…` |
| Gemini CLI | `.gemini/agents/*.md`, `~/.gemini/agents/*.md` (lines 323–324) | markdown + YAML frontmatter | **no** — `.claude/agents` 0 | `raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/core/subagents.md`, 23,610 B, sha256 `1a1b3899…` |
| Cursor | `.cursor/agents/`, `~/.cursor/agents/` | markdown + YAML frontmatter | **yes — `.claude/agents`, `.codex/agents`** | see §2.1 |
| opencode | `.opencode/agents/`, `~/.config/opencode/agents/` (lines 209–210, 718) | markdown + YAML frontmatter (`mode: subagent`, `permission`) | **no** — `.claude/agents` 0 | `opencode.ai/docs/agents.md`, 20,997 B, sha256 `5d070a8b…` |

Gemini CLI's sentence, byte-exact (lines 322–324 of the raw md):

> Custom agents are defined as Markdown files (`.md`) with YAML frontmatter. You can place them in:
> 1. **Project-level:** `.gemini/agents/*.md` (Shared with your team)
> 2. **User-level:** `~/.gemini/agents/*.md` (Personal agents)

Codex's sentence, byte-exact (byte 503,880 of the fetched HTML; `<code>` tags wrap only the two paths, so it survives
the counter's tag→space normalisation):

> To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or
> `.codex/agents/` for project-scoped agents.

Copilot CLI, byte-exact (md lines 17, 25, 27):

> Each custom agent is defined by a Markdown file with an `.agent.md` extension. … **Project** (`.github/agents/`) …
> **User** (`~/.copilot/agents/`)

opencode, byte-exact (md lines 209–210):

> - Global: `~/.config/opencode/agents/`
> - Per-project: `.opencode/agents/`

### 2.4 Format divergence (why "shared spec" is not merely undocumented)

- Codex is the outlier: **TOML** files with required keys `name`, `description`, `developer_instructions`
  (developers.openai.com/codex/subagents; required-fields table, all three "Required: Yes").
- The other six document markdown + YAML frontmatter, but with different field vocabularies: Claude Code
  (`tools`, `disallowedTools`, `permissionMode`, `maxTurns`, `skills`, `memory`, …), Gemini CLI
  (`kind`, `tools`, `temperature`, `max_turns`, `timeout_mins`), opencode (`mode`, `permission`), Cursor
  (`model`, `readonly`, `is_background`, all optional), Copilot CLI/VS Code (`user-invocable`,
  `disable-model-invocation` — VS Code page, fetched HTML around byte 106,226).
- `[INFERENCE]` A common directory or filename convention is therefore not a common file schema; the C1 table's
  "What the file sets" column should state per-client fields, not a shared field list.

---

## 3. Consequences for C1's new-ground target (verified against BASE_REV, not the working tree)

`git --no-optional-locks grep -i -F -l <path> b0b7140b -- ':!.ufo'` in the lane (read-only), one call per path:

| Path | Present at base `b0b7140b`? | Files |
|---|---|---|
| `.claude/agents` | **held** | `corpus/knowledge/alwayson-rule-files-round53.md`, `verifiers/verify_alwayson.py` |
| `.codex/agents` | **held** | `LOG.md`, `corpus/knowledge/alwayson-rule-files-round53.md`, `corpus/knowledge/instruction-surface-census-round13.md`, `corpus/knowledge/instruction-surface-remeasure-round13.md` |
| `.opencode/agent` | **held** | `corpus/knowledge/instruction-surface-remeasure-round13.md`, `verifiers/checklist-baseline.json` |
| `.github/agents` | **zero** | — |
| `.cursor/agents` | **zero** | — |
| `.gemini/agents` | **zero** | — |
| `.copilot/agents` | **zero** | — |

The counter counts occurrences in the **base tree** (`verifiers/check_agent_definitions.py:1124-1136`, via
`git_grep_count(lane, BASE, n)`, `:222-233`, paths under `.ufo/` excluded), so post-base files that mention these
strings (e.g. `plans/round-56.md`, `verifiers/check_agent_definitions.py` — the only two working-tree hits for
`.github/agents` and `.cursor/agents`) do not consume new ground. Confirmed read of the code, not inferred.

Distinct normalised zero-count values available: `.github/agents`, `.cursor/agents`, `.gemini/agents`,
`.copilot/agents` → up to 4, target 2. Two integration notes:

1. If both the VS Code row and the Copilot CLI row use `.github/agents`, they collapse to **one** distinct value
   (G counts DISTINCT normalised paths). Using `~/.copilot/agents/` for Copilot CLI (its own documented user
   location, under the counter's `OWN_ROOTS["Copilot CLI"]` = `.github`, `.copilot`) keeps three distinct values.
2. VS Code's only own-root location in its documentation table is `.github/agents` (its `.claude/agents` row is the
   *Claude compatibility* path, which erratum 2's `OWN_ROOTS` rule rejects for VS Code — correctly, per the plan's
   reasoning). So VS Code must take `.github/agents`.

---

## 4. Candidate quotes for the C1 entry (hand-over, byte-exact; the L1/scribes decide)

The counter's normalisation (`_plain`, `:684-688`) strips `` ` ``, `*`, `_`, unescapes HTML entities, lowercases and
collapses whitespace; `norm_page` (`:696-700`) replaces tags with a space and drops comments/scripts. Consequence:
quotes may span markdown table pipes and code spans freely, and HTML-page quotes survive as long as no *content* sits
between two tags.

| Client | Path token | Candidate quote (source, location) | Words | Notes |
|---|---|---|---|---|
| Cursor | `.cursor/agents/` | `**Project subagents** \| \`.cursor/agents/\` \| Current project only` — cursor md line 85 | 6 | path + `subagents` outside it; also usable: line 92 precedence sentence (contains `subagents` twice but no `.cursor/agents/` token) |
| Cursor (compat fact, for the Action cell) | `.claude/agents/` | line 86 cell: "`.claude/agents/` \| Current project only (Claude compatibility)" | 5 | the cell has no `agent` word outside the path → **cannot** satisfy the counter's `AGENT_WORD_RE`; use as prose, not as the row quote |
| VS Code | `.github/agents` | `Workspace \| \`.github/agents\` folder \| \`.agent.md\` or \`.md\` files` — raw md line 123 | 7 | no Liquid on this line; identical in rendered page |
| VS Code (Claude-format fact) | `.claude/agents` | `Workspace (Claude format) \| \`.claude/agents\` folder \| \`.md\` files in the [Claude agent format]` — raw md line 124 | 12 | ends inside a markdown link; safe (brackets are literal) but ugly — trim to end at "format" |
| Codex | `.codex/agents/` | "To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents." — HTML byte 503,880 | 20 | quote holds **both** forms; counter accepts the token with or without `~/` |
| Gemini CLI | `.gemini/agents` | "**Project-level:** `.gemini/agents/*.md` (Shared with your team)" — raw md line 323 | 6 | `*.md` inside the token is fine (`TOKEN_RE` allows `*`) |
| Copilot CLI | `~/.copilot/agents/` | "**User** (`~/.copilot/agents/`)" — md line 27 | 3 | exactly 3 words; add context ("create the custom agent … **User** …") if the word floor is a concern |
| opencode | `.opencode/agents/` | "Per-project: `.opencode/agents/`" — md line 210 | 3 | exactly 3 words; the fuller line 715 sentence is safer |
| Claude Code | `.claude/agents/` | table row line 162: "\| `.claude/agents/` \| Current project \| 3 \| Ask Claude, or create the file manually \|" | 9 | row can exist in the table but cannot count: `.claude/agents` is held at base and S026 already cites this page |

Host check for these URLs against the counter's `HOSTS` (`:135-152`): `cursor.com` ✓ Cursor; `code.visualstudio.com`
and `raw.githubusercontent.com/microsoft/vscode-docs` ✓ VS Code; `developers.openai.com` ✓ Codex; `geminicli.com` and
`raw.githubusercontent.com/google-gemini/gemini-cli` ✓ Gemini CLI; `docs.github.com` ✓ Copilot CLI;
`opencode.ai` ✓ opencode; `code.claude.com` ✓ Claude Code. **`agentskills.io`, `agent-plugins.org` and `agents.md` are
not pinned for any client**, so §1's evidence cannot back a C1 row — it belongs in entry prose/lesson context only.

---

## 5. Fetch manifest (URL, `date -u`, status, bytes, sha256)

All fetches: `curl -sS -L --max-time 45 -A 'Mozilla/5.0 (X11; Linux x86_64) curl-research'`, HTTP status from
`%{http_code}`, sha256 of saved bytes. Full per-run logs: `fetch/log.txt`, `fetch/s/log.txt`, `fetch/v/log.txt`,
`fetch/p/log.txt`.

| UTC | URL | HTTP | Bytes | sha256 |
|---|---|---|---|---|
| 02:47:31Z | https://cursor.com/docs/subagents | 200 | 676,361 | `c9d06bc2e1cee8f39d64b115f51d13e21018549675c1958e533d23528b531264` |
| 02:47:31Z | https://code.claude.com/docs/en/sub-agents | 200 | 1,336,521 | `3a7ce2e991513a9df8f866b707e58d587d69e3629f25c680565d4b63f9e62d7d` |
| 02:47:31Z | https://code.visualstudio.com/docs/copilot/customization/custom-agents | 200 | 132,660 | `288d3754c9f6df8b05b016f6832d072d2aedf14639e1b0a27ffc9002985e99c7` |
| 02:47:32Z | https://opencode.ai/docs/agents/ | 200 | 183,509 | `1bddca5ba3df59505ae4ec4bb082887764ad5fe255b78100408158e5d1e70b27` |
| 02:47:32Z | https://agentskills.io/specification | 200 | 454,121 | `2383f899fe9f661cc34257867bf7d00fec0024f104bf4e6dbe5f922c4efd3597` |
| 02:47:57Z | https://geminicli.com/docs/core/subagents/ | 200 | 195,250 | `be339fc2e18e8ff9a18940e18aa8661fa6dac1a51e753753e3d1b359abb4cab3` |
| 02:47:57Z | https://opencode.ai/docs/agents.md | 200 | 20,997 | `5d070a8ba9c2db70db759aa019e2e48e5c3cd834d4892f17ffb99ba3fc852b1b` |
| 02:47:57Z | https://cursor.com/docs/subagents.md | 200 | 27,660 | `264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668` |
| 02:48:25Z | https://developers.openai.com/codex/subagents | 200 | 614,442 | `bf21f1997d6de96ef1b5293d8bedb1961681f0d07e02133515e4e020a7d4bb43` |
| 02:48:25Z | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents | 200 | 625,666 | `27ef0f9a2e67a301fe74b655997c91f204be9d38d60d8790a48486e837e0fc3a` |
| 02:48:26Z | https://code.visualstudio.com/docs/copilot/customization/custom-agents.md | **404** | 9 | `0019dfc4b32d63c1392aa264aed2253c1e0c2fb09216f8e2cc269bbfb8bb49b5` |
| 02:48:45Z | https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/copilot/customization/custom-agents.md | **404** | 14 | `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed` |
| 02:48:45Z | https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/core/subagents.md | 200 | 23,610 | `1a1b38993a2f5c6e16afda1914974a86274e73fac90e3ab62334d45e34bf7849` |
| 02:48:46Z | https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents.md | **404** | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| 02:49:27Z | https://code.claude.com/docs/en/sub-agents.md | 200 | 111,624 | `84b2646c513754ef5f33c6f5a0d7f59960021a65b5a09c35b9158fa116a73d5a` |
| 02:49:28Z | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli | 200 | 606,102 | `87c1fa3fb3bf753e13b79d4cca443acdd512dca6aad928d577a7dd5c34986ac1` |
| 02:49:29Z | https://agentskills.io/sitemap.xml | 200 | 1,504 | `a2638d695083d91fd36a87da6177410d5e45e7ba6ad9c6cee16e28c1e0c17c8b` |
| 02:49:29Z | https://api.github.com/repos/microsoft/vscode-docs/git/trees/main?recursive=1 | 200 | 2,537,214 | `3f562287b22732818f8559876fb77128eb663ccbca725f0895ae71e12588fbd2` |
| 02:50:21Z | https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md | 200 | 16,522 | `55c90b711eeffb0605b78c11c1cc09b057e28e70c6275a7e046a2c4334fff045` |
| 02:50:21Z | https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/agent-plugins.md | 200 | 17,914 | `367b3b776e038c3410cfe666efa96871b6a782395e3334be3ccdab384eb28022` |
| 02:50:43Z | https://agent-plugins.org/specification.md | 200 | 44,846 | `34710a33979953fd884e9b7d69af12a39e3e1e93f465fea2afaa886a5ca82ba0` |
| 02:50:44Z | https://agents.md/ | 200 | 81,690 | `06b65de9018141350fe45cdd9fccafa59787badc46f30d92a06c07e612713979` |
| 02:51:09Z | https://agentskills.io/clients.md | 200 | 282 | `6dabf4e3f4b39b29c6df9dcc6cff893a59a5cce3740a3a905df2a8b19e183e32` |
| 02:51:09Z | https://agentskills.io/specification.md | 200 | 7,608 | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |
| 02:51:10Z | https://raw.githubusercontent.com/sst/opencode/dev/packages/web/src/content/docs/agents.mdx | 200 | 21,066 | `1f805f8a7cd1d877272d61ad6d59dae4d014c7b26009110d1c4b26c65a634dcc` |
| 02:51:23Z | https://agentskills.io/llms.txt | 200 | 1,374 | `d9b01a3a13b79bb04ee0bc25125087d92e393f0c7e8f028c4c5fa4c217f1fbfb` |
| 02:51:24Z | https://api.github.com/repos/agentskills/agentskills/git/trees/main?recursive=1 | 200 | 60,279 | `01ca5002410a0518d4776e7e667fed9b42d7f687f126dd3676ef4123b89e517f` |
| 02:51:31Z | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | 200 | 8,379 | `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2` |

Process note: my helper script numbered bodies per run and later runs overwrote earlier `01.body…` files in the same
directory; the manifest lines above are the durable record (URL + timestamp + bytes + sha256 for every fetch), and the
canonical copies used for quotes are the ones in `fetch/s/`, `fetch/v/`, `fetch/p/` fetched at 02:49–02:51Z.

---

## 6. Q30 status (what is checked, what is not)

- **Ecosystem negative ("no shared agent-definition specification")** — three legs done: (i) site index + spec page +
  docs source tree for agentskills.io; (ii) published specification text + rationale for Agent Plugins v1.0.0;
  (iii) official-site text for agents.md; plus the lane-corpus grep (0 matches) and a discovery search. Scope limit:
  no *client* changelog was swept for a hypothetical "shared spec" proposal — per-client "documents no shared spec"
  claims are **not checked**, not silent.
- **Cross-client reads** — the two positives (Cursor, VS Code) are read from the vendors' own docs. For the five
  clients whose fetched page names no other client's directory (Claude Code, Codex, Copilot CLI, Gemini CLI,
  opencode) the sweep is **page-level only** (one page per client, plus Gemini CLI's and opencode's docs-source page);
  no changelog leg and no repo-wide docs search were run for this question → **not checked**, not silent. Sibling
  `build/ScoutChangelogSweep.md` holds the changelog leg for location/format changes; its scope is per-client
  location/format history, not the shared-spec question.

## 7. Remaining unknowns

1. Does Cursor actually parse Codex TOML agent files, or only discover files in `.codex/agents/`? Its page documents
   a Markdown+YAML format and lists `.codex/agents/` as a compatibility location; it does not state the parse.
   Verifiable only by running Cursor on a TOML file (out of scope for this seat).
2. Does VS Code's `.claude/agents` row load under the default Local harness, or only when the Claude-format harness is
   selected? Line 139 suggests the Local harness keeps user agents in profile storage; the page does not state the
   load path per row.
3. Is any *shared* agent-definition directory (e.g. `.agents/agents`) documented anywhere official? None of the seven
   client pages names one; the round-56 v1.2/v1.3 controls found such paths only in issue-tracker text, which the
   counter rejects by design. Unresolved, and not a docs claim.
4. Whether a vendor-neutral agent-definition format is under construction: Agent Plugins v1.0.0 line 616 says "until
   their formats converge", but no draft or working group page was found on the official sites checked.
