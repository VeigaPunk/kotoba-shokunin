Result: DONE — Copilot CLI’s dedicated custom-agent guide is verified, and the one-client dry-run recognizes `.github/agents/`; this single-row world does not meet the global C1 thresholds.

## Findings

The correct page is GitHub Docs’ Copilot CLI-specific “Creating and using custom agents for GitHub Copilot CLI,” not the cloud-agent custom-agents page. The served `.md` route is live at the required pinned host. Its definition, project/user directories, authoring inputs, tool restriction, and duplicate-ID behavior are at `served.md:17,23-30,65-82`; the corresponding current `github/docs` source is at `source.md:29-39,83-90`.

The separate custom-agent configuration reference is used only for schema detail: it says its YAML-frontmatter properties apply to GitHub.com, Copilot CLI, and supported IDEs (`config.md:10-12`); `description` is required while `name` is optional (`:18-19`); the profile body is Markdown below YAML frontmatter (`:31`); `tools` selects available tools (`:40-51`); and `model` is a string selecting the execution model, inheriting the default if absent (`:22`). The direct Copilot CLI guide also says a restriction adds a `tools` specification (`served.md:78-80`).

**Quote formatting disclosure:** The quote below retains the page’s words and the backticked path, but removes the Markdown list/bold markers and collapses the line break/indentation between fetched lines 23 and 25. It is within the 3–25-word limit; the counter accepted it.

## Ready-to-paste blocks

### 1. SOURCES row

```text
| S075 | GitHub Docs — Creating and using custom agents for GitHub Copilot CLI — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | docs | A | Copilot CLI custom-agent profile locations, Markdown file extension, authoring inputs, tool restriction, and personal-versus-repository duplicate handling | § Creating a custom agent (`create-custom-agents-for-cli.md:17,23-30,65-82`); fetched 2026-10-23T02:47:19Z, HTTP 200, 8,379 B, sha256 `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2` (seat SrcCopilotCLI) | Copilot CLI custom agents are Markdown `.agent.md` profiles in project `.github/agents/` or user `~/.copilot/agents/`; for the same ID, the personal agent is used, and restricting tools adds a `tools` specification | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

### 2. Entry row

```text
| Copilot CLI | `.github/agents/` | S075 | "Choose between the options to create the custom agent in the repository or in your home directory: Project (`.github/agents/`)" |
```

### 3. Detail paragraph

> Each Copilot CLI custom agent is a Markdown `.agent.md` file (“Each custom agent is defined by a Markdown file with an `.agent.md` extension,” `create-custom-agents-for-cli.md:17`). The profile configuration reference labels the schema “YAML frontmatter properties” and explicitly includes Copilot CLI (`custom-agents-configuration.md:10-12`); it marks `description` as **Required** and `name` as optional (`:18-19`), and says the behavior/instructions are Markdown below that frontmatter (`:31`). The `tools` property controls which tools are available (`:40`); an omitted property enables all tools, a selected list enables only those tools, and an empty list disables all (`:46-51`); the CLI creation page likewise says restricting tools adds a `tools` specification (`create-custom-agents-for-cli.md:78-80`). The `model` key is a string naming the execution model and inherits the default if unset (`custom-agents-configuration.md:22`). The CLI guide names the repository path “Project (`.github/agents/`)” (`create-custom-agents-for-cli.md:23-25`) and the user path “User (`~/.copilot/agents/`)” (`:23-27`); when personal and repository agents share an ID, “the personal agent is used” (`:30`).

### 4. SKILL.md row

```text
| Copilot CLI | `.github/agents/` (+ user `~/.copilot/agents/`) | Markdown `.agent.md`; YAML frontmatter with required `description`, optional `name`; `tools` controls available tools | Create and scope specialist agent profiles |
```

### 5. Gate row

```text
| S075 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md | 2026-10-23T02:47:19Z | 8,379 B, sha256 `506783b4…` | "Choose between the options to create the custom agent in the repository or in your home directory: Project (`.github/agents/`)" | create-custom-agents-for-cli.md:23-25 | SrcCopilotCLI |
```

## Fetch and provenance evidence

**Served Copilot CLI page.** `date -u` output: `Fri 23 Oct 2026 02:47:19 AM UTC`. Exact fetch command (run from the sandbox clone):

```sh
timeout 900s curl -L -sS -D served.headers -o served.md -w 'served URL final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md'
```

Exit 0; final URL was the requested URL, HTTP 200, curl reported 8,379 bytes; `wc -c` reported 8,379; `sha256sum served.md` returned `506783b43d77536f2771dd5670225a47cefa70365fb54f64316b2fed96ae34f2`. Fetched-byte line anchors: `served.md:17,23-30,65-82,135-149`.

**Docs source-tree cross-check.** `date -u` output: `Fri 23 Oct 2026 02:47:19 AM UTC`. Exact command: `timeout 900s curl -L -sS -D source.headers -o source.md -w 'source URL final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://raw.githubusercontent.com/github/docs/main/content/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md'`. Exit 0, HTTP 200, 9,907 bytes; SHA-256 `f94dc9baf904179ef502908c1a61f0df288971ac1c3f75324d4002b44e1facfa`; source lines `source.md:29-39,83-90` carry the same extension, locations, precedence, and tools material. This is the `github/docs` `main` source copy, not a commit-pinned source snapshot.

**Schema reference.** `date -u` output: `Fri 23 Oct 2026 02:47:40 AM UTC`. Exact command: `timeout 900s curl -L -sS -D config.headers -o config.md -w 'final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://docs.github.com/en/copilot/reference/custom-agents-configuration.md'`; exit 0, HTTP 200, 18,904 bytes; SHA-256 `914d2b3aca98f2bc096e477a4acaa19ce26adc7c76542a70e3cea48eb1ba26cc`; relevant lines `config.md:10-12,18-22,31,40-51`.

**Base-row check, performed before drafting.** `timeout 900s grep -n 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` produced no output, exit 1. Revision-specific confirmation: `timeout 900s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -F 'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli.md' b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- corpus/SOURCES.md` produced no output, exit 1.

## Dry-run and gates

Sandbox clone command completed with `sandbox checkout complete`:

```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; mkdir -p /fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI && timeout 900s git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI && timeout 900s git -C /fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI checkout -q e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
```

The sandbox world commit is `69be8614f3c76d4e15e0c3ae493e6f6e10ef3d5b` (parent checkout `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`). The exact command staged only `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/agent-definition-files-round56.md`, and `corpus/lessons/round-56.md`:

```sh
set -eu; repo=/fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI; timeout 900s git -C "$repo" add -- SKILL.md corpus/SOURCES.md corpus/knowledge/agent-definition-files-round56.md corpus/lessons/round-56.md; timeout 900s git -C "$repo" -c user.name=SrcCopilotCLI -c user.email=src-copilot-cli@local.invalid commit -m 'dry-run C1 Copilot CLI source row'; timeout 900s git -C "$repo" rev-parse HEAD
```

Observed commit output: `4 files changed, 18 insertions(+)`, followed by `create mode 100644` for each of the two new entry and lesson files; the final printed hash was `69be8614f3c76d4e15e0c3ae493e6f6e10ef3d5b`.

Counter command: `timeout 900s python3 -B verifiers/check_agent_definitions.py --rev 69be8614f3c76d4e15e0c3ae493e6f6e10ef3d5b --fetch` (run from the sandbox clone). Observed output:

```text
agent-definition locations found on the live page 1 of 1; new ground 1
Copilot CLI  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
```

Exit 1. Copilot CLI is found: the live page contains the quote and `.github/agents/` path, and the path has zero case-insensitive hits in the frozen base text. The global result is not a C1 pass: this deliberately one-client world has F=1 and G=1, below frozen F≥5 and G≥2. No other client rows were added to this world.

The dry-run SKILL insertion adds eight lines to the 598-line base `SKILL.md` (ending at line 598 in the read snapshot), so this literal block is not independently line-budget-compliant; integrate it with the round’s planned line-budget move. No lane product file or Git/JJ state was changed by this seat; only this report is written in the lane.

## Rejections and boundaries

- **Opened, not used as the S075 source:** GitHub Docs’ broad Copilot CLI command reference. Exact command: `timeout 900s curl -L -sS -D cli-reference.headers -o cli-reference.md -w 'final=%{url_effective} HTTP=%{http_code} bytes=%{size_download}\n' 'https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md'`; fetched at `Fri 23 Oct 2026 02:47:40 AM UTC` (HTTP 200, 461,944 B, SHA-256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9`). The direct custom-agent CLI guide is the more focused S075 evidence for project/user locations and precedence.
- **Search lead only, not fetched or cited:** “About custom agents” for Copilot cloud agent (`https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents`); excluded because the assignment is specifically Copilot CLI, not only the cloud coding agent.
- No tools were installed or updated. No counter, verifier, C2 delegate, or map disposition was edited; no C2 work was attempted. No other client rows were included.

## Artifacts

- Lane report: `.ufo/waves/round-56/build/SrcCopilotCLI.md` (only lane file written by this seat).
- Sandbox commit: `69be8614f3c76d4e15e0c3ae493e6f6e10ef3d5b` in `/fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI`.
- Fetched files: `/fast/scratch/hyaku/kotoba-r56/SrcCopilotCLI/served.md`, `source.md`, `config.md`, and `cli-reference.md` (plus their response headers), all outside the lane.
