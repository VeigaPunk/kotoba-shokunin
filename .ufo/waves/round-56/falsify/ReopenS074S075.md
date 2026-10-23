Result: MIXED — S074 and S075 live fetches match the recorded bytes/hashes and support the Gate quotes, shared `.github/agents` project path, VS Code's `.claude/agents` compatibility, and Copilot CLI's personal-wins-on-same-ID rule, but Copilot CLI's "required `description`" and "YAML frontmatter" claims are wider than S075 (sourced from an uncited reference page), Finding 2's S074 line anchor is off by 13 lines (`123-126` vs `108-113`), Finding 1 and `SKILL.md:105` flatten VS Code's harness-dependent user locations, and `Quote notes` omit S075's markdown stripping.

## Live Fetch & Gate Quote Verification (S074, S075, and companion reference pages)

All fetches ran in `/fast/scratch/hyaku/kotoba-r56/ReopenS074S075` using ordinary `curl -L -sS` (no headless browser, no bot-challenge bypass, no paid model calls, no tools installed or updated).

### Command and observed output (Batch 1 — S074 and S075)

```text
$ unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
$ rm -rf /fast/scratch/hyaku/kotoba-r56/ReopenS074S075
$ mkdir -p /fast/scratch/hyaku/kotoba-r56/ReopenS074S075
$ git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/ReopenS074S075/repo
$ git -C /fast/scratch/hyaku/kotoba-r56/ReopenS074S075/repo checkout -q c22fdd390e10623209024c9bbc2fa86b0cdfc333
$ cd /fast/scratch/hyaku/kotoba-r56/ReopenS074S075
$ date -u
Fri 23 Oct 2026 03:07:27 AM UTC
$ timeout 60s curl -L -sS -D s074.headers -o s074-custom-agents.md -w 'S074 final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://code.visualstudio.com/docs/agent-customization/custom-agents.md'
S074 final=https://code.visualstudio.com/docs/agent-customization/custom-agents.md HTTP=200 bytes=15714
$ sha256sum s074-custom-agents.md
8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f  s074-custom-agents.md
$ wc -c s074-custom-agents.md
15714 s074-custom-agents.md
$ date -u
Fri 23 Oct 2026 03:07:27 AM UTC
$ timeout 60s curl -L -sS -D s075.headers -o s075-create-custom-agents-for-cli.md -w 'S075 final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md'
S075 final=https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md HTTP=200 bytes=8379
$ sha256sum s075-create-custom-agents-for-cli.md
506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2  s075-create-custom-agents-for-cli.md
$ wc -c s075-create-custom-agents-for-cli.md
8379 s075-create-custom-agents-for-cli.md
```
(Exit code: `0`.)

### Command and observed output (Batch 2 — companion reference pages and docs source trees)

```text
$ cd /fast/scratch/hyaku/kotoba-r56/ReopenS074S075
$ date -u
Fri 23 Oct 2026 03:07:42 AM UTC
$ timeout 60s curl -L -sS -D vscode-ref.headers -o vscode-custom-agent-file-reference.md -w 'VSCodeRef final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference.md'
VSCodeRef final=https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference.md HTTP=200 bytes=11205
$ sha256sum vscode-custom-agent-file-reference.md
71e4dbc2daea59ea575fbc1eb307f8b1f1324c1b586aa942abf957ac8b8f0288  vscode-custom-agent-file-reference.md
$ wc -c vscode-custom-agent-file-reference.md
11205 vscode-custom-agent-file-reference.md
$ date -u
Fri 23 Oct 2026 03:07:44 AM UTC
$ timeout 60s curl -L -sS -D copilot-cfg.headers -o copilot-custom-agents-configuration.md -w 'CopilotCfg final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://docs.github.com/en/copilot/reference/custom-agents-configuration.md'
CopilotCfg final=https://docs.github.com/en/copilot/reference/custom-agents-configuration.md HTTP=200 bytes=18901
$ sha256sum copilot-custom-agents-configuration.md
9ea3e683cfcb7950af70e577ef5453cfe95690c2ff34185acb5896b60bfb0a12  copilot-custom-agents-configuration.md
$ wc -c copilot-custom-agents-configuration.md
18901 copilot-custom-agents-configuration.md
$ date -u
Fri 23 Oct 2026 03:07:44 AM UTC
$ timeout 60s curl -L -sS -D vscode-src.headers -o vscode-src-custom-agents.md -w 'VSCodeSrc final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md'
VSCodeSrc final=https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md HTTP=200 bytes=16522
$ sha256sum vscode-src-custom-agents.md
55c90b711eeffb0605b78c11c1cc09b057e28e70c6275a7e046a2c4334fff045  vscode-src-custom-agents.md
$ wc -c vscode-src-custom-agents.md
16522 vscode-src-custom-agents.md
$ date -u
Fri 23 Oct 2026 03:07:45 AM UTC
$ timeout 60s curl -L -sS -D copilot-src.headers -o copilot-src-create-custom-agents-for-cli.md -w 'CopilotSrc final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md'
CopilotSrc final=https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md HTTP=200 bytes=9907
$ sha256sum copilot-src-create-custom-agents-for-cli.md
f94dc9baf904179ef502908c1a61f0df288971ac1c3f75324d4002b44e1facfa  copilot-src-create-custom-agents-for-cli.md
$ wc -c copilot-src-create-custom-agents-for-cli.md
9907 copilot-src-create-custom-agents-for-cli.md
```
(Exit code: `0`.)

### Gate quotes check
- **S074 (`corpus/lessons/round-56.md:16`, `corpus/knowledge/agent-definition-files-round56.md:23`, `corpus/SOURCES.md:87`):**
  - Byte count (`15,714 B`) and SHA-256 (`8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f`) match live `s074-custom-agents.md` exactly.
  - Gate quote (20 words, byte-exact at `s074-custom-agents.md:63`, no markdown stripped):
    `For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:`
- **S075 (`corpus/lessons/round-56.md:17`, `corpus/knowledge/agent-definition-files-round56.md:24`, `corpus/SOURCES.md:88`):**
  - Byte count (`8,379 B`) and SHA-256 (`506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2`) match live `s075-create-custom-agents-for-cli.md` exactly.
  - Gate quote (20 words): `"Choose between the options to create the custom agent in the repository or in your home directory: Project (\`.github/agents/\`)"`.
  - In `s075-create-custom-agents-for-cli.md:23-25`, the raw bytes are:
    - Line 23 (17 words, byte-exact): `3. Choose between the options to create the custom agent in the repository or in your home directory:`
    - Line 24: empty line
    - Line 25 (3 words, byte-exact): `   * **Project** (\`.github/agents/\`)`
  - This passes `verifiers/check_agent_definitions.py` (which strips markdown emphasis/list tokens and collapses whitespace), but see **Finding F4** below on the missing markdown-stripping disclosure in `Quote notes`.

---

## Attacks & Findings on Landed C1 Content (`c22fdd390e10623209024c9bbc2fa86b0cdfc333`)

### F1 (Defect — False Provenance / Wider Than Cited Page): Copilot CLI's `required description` and `YAML frontmatter` claims cite S075, which contains neither

- **Target rows/lines attacked:**
  - `SKILL.md:99`: `Formats differ (Codex is TOML; the rest are Markdown with YAML frontmatter), so § Agent-definition fidelity checklist applies to opencode files only. Basis: corpus/knowledge/agent-definition-files-round56.md (S072–S078, S026)`
  - `SKILL.md:106` (Copilot CLI row, `What the file sets` cell): `Markdown profiles (\`.agent.md\`; \`.md\` also recognized); YAML frontmatter with required \`description\`, optional \`name\`; \`tools\` limits tools; the personal profile wins on the same ID`
  - `corpus/knowledge/agent-definition-files-round56.md:47` (Finding 3): `Copilot CLI requires \`description\` and makes \`name\` optional (S075);`
- **Counterexample & local evidence:**
  - S075 (`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md`, `s075-create-custom-agents-for-cli.md`, 8,379 B) **does** support `optional name` at line 30 (byte-exact, 8 words):
    `The optional \`name\` field does not affect deduplication.`
  - However, S075 **never** states that `description` is a required frontmatter key and **never** mentions `YAML`:
    - `yaml` (case-insensitive) has **0 matches** in `s075-create-custom-agents-for-cli.md`.
    - `frontmatter` appears once, at `s075-create-custom-agents-for-cli.md:135` (byte-exact, 10 words): `add \`include-custom-instructions: true\` to the agent file's frontmatter:` followed by an example block (`:138-143`).
    - `required` appears once, at `s075-create-custom-agents-for-cli.md:61` (byte-exact, 16 words): `You can review and make changes, if required, before continuing the agent creation process in the CLI.`
    - At `s075-create-custom-agents-for-cli.md:69-76` (`Option 2: Create the agent profile manually`), the interactive `/agent` CLI wizard prompts the user for `1. Enter a name for the agent.`, `2. Enter a description...`, `3. Enter instructions...` — it does not state which frontmatter keys are required in a file.
  - Instead, `YAML frontmatter` and `description` = `**Required** string` come from a **different page** linked at `s075-create-custom-agents-for-cli.md:156`: `https://docs.github.com/en/copilot/reference/custom-agents-configuration.md` (`copilot-custom-agents-configuration.md`, 18,901 B, sha256 `9ea3e683cfcb7950af70e577ef5453cfe95690c2ff34185acb5896b60bfb0a12`), lines 10, 18, and 19:
    - Line 10 (byte-exact, 4 words): `## YAML frontmatter properties`
    - Line 18 (byte-exact, 12 words): `| \`name\`                     | string                                                   | Display name for the custom agent. Optional.                                                                                                                                                                                                                                                                            |`
    - Line 19 (byte-exact, 12 words): `| \`description\`              | **Required** string                                      | Description of the custom agent's purpose and capabilities                                                                                                                                                                                                                                                              |`
  - `SrcCopilotCLI.md:7,16,27,53` explicitly noted that `required description` came from `custom-agents-configuration.md` (`config.md:10-12,18-19`), and therefore omitted `required description` from the `S075` row in `corpus/SOURCES.md:88`. Neither `custom-agents-configuration.md` nor `custom-agent-file-reference.md` appears anywhere in `corpus/SOURCES.md` (`grep` across `corpus/` and `SKILL.md` returned 0 matches).
  - By contrast, when S072 (`sdk-subagents.md`) lacked Claude Code's file-schema keys, `SKILL.md:103` and `agent-definition-files-round56.md:1,29-30,46` explicitly cited base row `S026`. Crediting `(S075)` for `requires description` in `agent-definition-files-round56.md:47` and `SKILL.md:106` attributes a rule to a source row that does not state it (Q23).
- **Impacted axes:** calibration, depth, consistency (fixable defect, not a counter break or required tradeoff).
- **Smallest safe correction:** Either (a) bound `SKILL.md:106` and `corpus/knowledge/agent-definition-files-round56.md:47` to what `S075` itself states (`frontmatter` with `name` optional (`:30`), `description` for inference (`:105`), `tools` (`:80`), `include-custom-instructions` (`:135`), noting that `S075` links `custom-agents-configuration` for full schema), OR (b) admit `https://docs.github.com/en/copilot/reference/custom-agents-configuration.md` as a `SOURCES.md` row (or add its URL/sha256 to `S075` if allowed by append-only rules — since `S075` is new in round 56, `check_sources_append_only.py --base b0b7140b` allows editing `S075` or adding `S079`) and cite that row for `YAML frontmatter` and `required description`.

---

### F2 (Defect — Wrong Line Anchor): Finding 2 cites `S074 custom-agents.md:123-126` for VS Code's `.claude/agents` workspace table row, which is actually at `:108-113` (`:111`)

- **Target line attacked:** `corpus/knowledge/agent-definition-files-round56.md:43-44`:
  `and VS Code lists \`.claude/agents\` as a workspace location in Claude format (S074 \`custom-agents.md:123-126\`).`
- **Counterexample & local evidence:**
  - In the file fetched from S074 (`https://code.visualstudio.com/docs/agent-customization/custom-agents.md`, `s074-custom-agents.md`, 15,714 B, sha256 `8643b098…`), lines `123-126` are:
    - Line 123: empty line
    - Line 124 (byte-exact, 6 words): `### Local harness locations and migration`
    - Line 125: empty line
    - Line 126 (first 22 words, byte-exact): `The **Local** harness stores user-level custom agents in VS Code profile storage, separate from harness user folders such as \`~/.copilot/agents\` and \`~/.claude/agents\`.`
  - The `## Custom agent file locations` table that lists `.claude/agents` as `Workspace (Claude format)` is instead at **`s074-custom-agents.md:108-113`** (matching `corpus/SOURCES.md:87`, which anchors `§ Custom agent file locations (:104-115); Local harness locations (:124-128)`):
    - Line 110 (byte-exact, 11 words): `| Workspace | \`.github/agents\` folder | \`.agent.md\` or \`.md\` files |`
    - Line 111 (byte-exact, 16 words): `| Workspace (Claude format) | \`.claude/agents\` folder | \`.md\` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |`
    - Line 112 (byte-exact, 12 words): `| User (Copilot) | \`~/.copilot/agents\` folder | \`.agent.md\` or \`.md\` files |`
    - Line 113 (byte-exact, 17 words): `| User (Anthropic Claude) | \`~/.claude/agents\` folder | \`.md\` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |`
  - **Root cause:** `ScoutChangelogSweep.md:56-57` cited lines `123-126` from `https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/custom-agents.md` (`vscode-src-custom-agents.md`, 16,522 B, sha256 `55c90b71…`), which starts with a 15-line YAML frontmatter block (`vscode-src-custom-agents.md:1-15`) absent from the served `S074` `.md` file (`15,714 B`). Also note that `s074-custom-agents.md:113` and `:126` list user-level `~/.claude/agents` alongside workspace `.claude/agents`.
- **Impacted axes:** calibration, consistency (fixable defect).
- **Smallest safe correction:** Change `(S074 \`custom-agents.md:123-126\`)` at `corpus/knowledge/agent-definition-files-round56.md:44` to `(S074 \`custom-agents.md:108-113\`)` (or `:111,113`).

---

### F3 (Defect — Over-flattening of Source Scope): `SKILL.md:105` and Finding 1 flatten VS Code's harness-dependent user locations into unqualified `~/.copilot/agents`

- **Target rows/lines attacked:**
  - `SKILL.md:105` (VS Code row, `Definition location` cell): `` `.github/agents` (user `~/.copilot/agents`; also reads `.claude/agents` in Claude format) ``
  - `corpus/knowledge/agent-definition-files-round56.md:38-39` (Finding 1): `1. **Two shared folders, one format split.** VS Code and Copilot CLI both use \`.github/agents/\` in the repository and \`~/.copilot/agents/\` for the user (S074, S075);`
- **Counterexample & local evidence:**
  - While `s074-custom-agents.md:110` lists `.github/agents` as the single default workspace folder (and `:128` says `Prefer native harness folders, such as \`.github/agents\` and \`~/.copilot/agents\`, over custom search locations.`), `s074-custom-agents.md:108-113` and `:126` explicitly split VS Code user-level agent locations by harness:
    - **Copilot harness:** `~/.copilot/agents` (`s074-custom-agents.md:112`: `| User (Copilot) | \`~/.copilot/agents\` folder | \`.agent.md\` or \`.md\` files |`).
    - **Local harness:** VS Code profile storage (`s074-custom-agents.md:126`: `The **Local** harness stores user-level custom agents in VS Code profile storage, separate from harness user folders such as \`~/.copilot/agents\` and \`~/.claude/agents\`.`).
    - **Anthropic Claude harness:** `~/.claude/agents` (`s074-custom-agents.md:113`: `| User (Anthropic Claude) | \`~/.claude/agents\` folder | ... |`).
  - `corpus/SOURCES.md:87` (`teaches` cell for S074) accurately records `user locations vary by harness`, and notes `.agent.md` or `.md` files (`s074-custom-agents.md:110,112`), whereas `SKILL.md:105` and `agent-definition-files-round56.md:38-39` drop the harness qualification (and `SKILL.md:105` mentions only `.agent.md`, omitting `.md`).
- **Impacted axes:** depth, calibration, operability (fixable defect).
- **Smallest safe correction:**
  - In `SKILL.md:105`, qualify user storage and `.md` recognition: e.g., `` `.github/agents` (user `~/.copilot/agents` for Copilot, profile storage for Local; also `.claude/agents` in Claude format) `` and `` `.agent.md` (or `.md`) Markdown with optional YAML frontmatter: `name`, `description`, `tools` ``.
  - In `corpus/knowledge/agent-definition-files-round56.md:38-39`, qualify `~/.copilot/agents/` as VS Code's Copilot-harness user folder (with Local user agents in VS Code profile storage and Claude-harness user agents in `~/.claude/agents`, `custom-agents.md:112-113,126`).

---

### F4 (Minor Defect — Quote Hygiene): `Quote notes` omit that S075's quote strips markdown list/emphasis tokens and folds lines 23–25

- **Target lines attacked:**
  - `corpus/knowledge/agent-definition-files-round56.md:24,29-34`
  - `corpus/lessons/round-56.md:17,22-24`
- **Counterexample & local evidence:**
  - In `s075-create-custom-agents-for-cli.md:23-25`, line 23 ends with `home directory:`, line 24 is blank, and line 25 is `   * **Project** (\`.github/agents/\`)`.
  - The recorded quote `"Choose between the options to create the custom agent in the repository or in your home directory: Project (\`.github/agents/\`)"` strips `* ` and `**...**` and folds lines 23–25 into one line.
  - `SrcCopilotCLI.md:9` disclosed this normalization, and both `Quote notes` blocks (`agent-definition-files-round56.md:33-34`, `round-56.md:23-24`) disclose fence stripping for S078 (`Srcopencode`), but neither `Quote notes` block mentions that S075's quote strips `* **Project**` and folds lines 23–25.
- **Impacted axes:** calibration (fixable quote-hygiene defect).
- **Smallest safe correction:** Add one clause to `Quote notes` in `corpus/knowledge/agent-definition-files-round56.md:29-34` and `corpus/lessons/round-56.md:22-24`: `S075's quote folds lines 23–25 and strips the list/bold markers on * **Project** (SrcCopilotCLI).`

---

## Claims Verified as Holding Against S074 and S075

1. **Shared `.github/agents` workspace/project path (`SKILL.md:105-106`, `agent-definition-files-round56.md:23-24,38-39`, `SOURCES.md:87-88`):**
   - **Holds.** `s074-custom-agents.md:63,110,128,170` documents `.github/agents` as VS Code's workspace default folder; `s075-create-custom-agents-for-cli.md:25` documents `.github/agents/` as Copilot CLI's **Project** folder.
2. **VS Code `.claude/agents` compatibility claim (`SKILL.md:105`, `agent-definition-files-round56.md:43-45`):**
   - **Holds in substance** (modulo the line anchor `:123-126` → `:108-113` in F2 and the additional user-level `~/.claude/agents` row at `:113`). `s074-custom-agents.md:111` lists `| Workspace (Claude format) | \`.claude/agents\` folder | \`.md\` files in the [Claude agent format](/docs/agents/reference/custom-agent-file-reference.md#claude-agent-format) |`. Companion `vscode-custom-agent-file-reference.md:144-159` confirms `.claude/agents` uses plain `.md` files with Claude's schema (`name` and `description` required) and that Local maps supported Claude tool/model names to VS Code equivalents.
3. **Copilot CLI personal-wins-on-same-ID precedence claim (`SKILL.md:106`, `agent-definition-files-round56.md:39-40`, `SOURCES.md:88`):**
   - **Holds.** `s075-create-custom-agents-for-cli.md:30` states verbatim (25 words, byte-exact):
     `If personal and repository custom agents have the same ID, the personal agent is used. For an agent at the root of an \`agents\` directory,`
     and continues at `:30` (21 words, byte-exact):
     `the ID is the file name without the \`.agent.md\` or \`.md\` extension. The optional \`name\` field does not affect deduplication.`
     (Note: specifying in `agent-definition-files-round56.md:39-40` that the ID is the filename stem rather than the optional `name` key would sharpen the entry, since two files with the same `name` but different filenames both load.)

## Tooling and Process Hygiene

- Tools installed or updated: none.
- Sandbox/scratch directory: `/fast/scratch/hyaku/kotoba-r56/ReopenS074S075`. No commits were made in the lane; no background processes remain running.
