Result: DONE — VS Code S074 evidence and the isolated one-client C1 dry-run are complete; this intentionally partial world does not meet the global C1 predicate.

## Findings and provenance

The official VS Code custom-agents page documents `.github/agents` as the workspace default and separates workspace, user, and harness-specific locations. The entry quote below is copied byte-for-byte from the downloaded Markdown route at `custom-agents.md:63`; no Markdown was stripped. The phrase is 20 words, contains `.github/agents` in the file path, and contains “agent” outside that path.

The supplied candidate URL, `https://code.visualstudio.com/docs/copilot/customization/custom-agents`, was fetched with `curl --location`; the effective URL was `https://code.visualstudio.com/docs/agent-customization/custom-agents` (HTTP 200). The official Markdown route used for S074 was `https://code.visualstudio.com/docs/agent-customization/custom-agents.md` (HTTP 200). The fetched Markdown file's lines cited below are the raw response lines.

### Requested ready-to-paste blocks

1. **SOURCES row**

```markdown
| S074 | VS Code — Custom agents in VS Code — https://code.visualstudio.com/docs/agent-customization/custom-agents.md | docs | A | VS Code custom-agent workspace and user-level locations, file format, and configuration fields | § Custom agent file structure (`custom-agents.md:59-69`); § Custom agent file locations (`:104-115`); Local harness locations (`:124-128`); fetched 2026-10-23T02:47:52Z, HTTP 200, 15,714 B, sha256 `8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f` (seat SrcVSCode) | The workspace default is `.github/agents`; agent files use `.agent.md` or `.md` and Markdown instructions with optional YAML frontmatter; user locations vary by harness | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

2. **Knowledge entry row**

```markdown
| VS Code | `.github/agents` | S074 | "For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:" |
```

3. **Detail paragraph**

VS Code custom-agent files use an optional YAML header and Markdown body: “A custom agent file contains an optional YAML header, enclosed by `---` delimiters, followed by a Markdown body with the agent's instructions” (`custom-agent-file-reference.md:10`). For the VS Code format, no header fields are required: “All fields in this table are optional” (`custom-agent-file-reference.md:35`); the separate Claude format marks `name` and `description` required (`:148-149`). The `tools` field restricts the available tools: “If the agent specifies a `tools` list, only those tools are available” (`custom-agents.md:23`). The `model` field is “The model to use in the Copilot harness”; an array is tried in preference order, and “If omitted, the currently selected model is used” (`custom-agent-file-reference.md:44`). The workspace row is “| Workspace | `.github/agents` folder | `.agent.md` or `.md` files |” (`custom-agents.md:110`); the workspace Claude-format row instead names `.claude/agents` (`:111`). User Copilot files are listed as “| User (Copilot) | `~/.copilot/agents` folder | `.agent.md` or `.md` files |” (`:112`), and user Anthropic Claude files as “| User (Anthropic Claude) | `~/.claude/agents` folder | `.md` files in the Claude agent format |” (`:113`). For Local, “The Local harness stores user-level custom agents in VS Code profile storage” (`:126`). The page says workspace agents are for a specific workspace and user-level agents are available across workspaces (`:106`), but these opened VS Code pages state no precedence rule between workspace and user-level definitions. The only explicit relevant precedence found is tool-list precedence: “In Local, a prompt file's `tools` list takes precedence over the custom agent's `tools` list” (`custom-agent-file-reference.md:140`); that is not a workspace/user discovery rule.

4. **SKILL.md row** (first backticked location is the workspace default; Action has five words)

```markdown
| VS Code | `.github/agents` (+ user: `~/.copilot/agents`; Local: VS Code profile storage) | Markdown instructions with optional YAML frontmatter for name, description, and tools | Create a workspace custom agent |
```

5. **Gate row**

```markdown
| S074 | https://code.visualstudio.com/docs/agent-customization/custom-agents.md | 2026-10-23T02:47:52Z | 15,714 B, sha256 `8643b098`… | "For example, save this planning agent as `.github/agents/planner.agent.md`. It uses read-only tools to research a task and return a plan:" | `custom-agents.md:63` | SrcVSCode |
```

### Fetches and raw-byte evidence

First fetch batch: `date -u` printed exactly `Fri Oct 23 02:46:49 AM UTC 2026`.

Command used:

```sh
timeout 900 bash -lc 'date -u; curl --location --silent --show-error --output vscode-custom-agents.html --write-out "Page URL: %{url_effective}\nPage HTTP: %{http_code}\n" https://code.visualstudio.com/docs/copilot/customization/custom-agents; printf "Page bytes: "; wc -c < vscode-custom-agents.html; printf "Page sha256: "; sha256sum vscode-custom-agents.html; curl --location --silent --show-error --output vscode-custom-agents.md --write-out "Source URL: %{url_effective}\nSource HTTP: %{http_code}\n" https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/copilot/customization/custom-agents.md; printf "Source bytes: "; wc -c < vscode-custom-agents.md; printf "Source sha256: "; sha256sum vscode-custom-agents.md'
```

Observed output: page effective URL `https://code.visualstudio.com/docs/agent-customization/custom-agents`, HTTP 200, 132,660 B, SHA-256 `288d3754c9f6df8b05b016f6832d072d2aedf14639e1b0a27ffc9002985e99c7`; the attempted old GitHub raw source URL returned HTTP 404, 14 B, SHA-256 `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed`.

Second fetch batch: `date -u` printed exactly `Fri Oct 23 02:47:52 AM UTC 2026`.

Command used:

```sh
timeout 900 bash -lc 'date -u; curl --location --silent --show-error --output custom-agent-reference.html --write-out "Reference URL: %{url_effective}\nReference HTTP: %{http_code}\n" https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference; printf "Reference bytes: "; wc -c < custom-agent-reference.html; printf "Reference sha256: "; sha256sum custom-agent-reference.html; curl --location --silent --show-error --output custom-agent-reference.md --write-out "Reference markdown URL: %{url_effective}\nReference markdown HTTP: %{http_code}\n" https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference.md; printf "Reference markdown bytes: "; wc -c < custom-agent-reference.md; printf "Reference markdown sha256: "; sha256sum custom-agent-reference.md; curl --location --silent --show-error --output custom-agents-current.md --write-out "Current markdown URL: %{url_effective}\nCurrent markdown HTTP: %{http_code}\n" https://code.visualstudio.com/docs/agent-customization/custom-agents.md; printf "Current markdown bytes: "; wc -c < custom-agents-current.md; printf "Current markdown sha256: "; sha256sum custom-agents-current.md'
```

Observed output: reference HTML `https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference`, HTTP 200, 125,109 B, SHA-256 `913eb1dcee3504c995337edaf4ab05e8a98033f25e6edc0a0b0912da9bdf39cb`; reference Markdown `https://code.visualstudio.com/docs/agents/reference/custom-agent-file-reference.md`, HTTP 200, 11,205 B, SHA-256 `71e4dbc2daea59ea575fbc1eb307f8b1f1324c1b586aa942abf957ac8b8f0288`; custom-agents Markdown `https://code.visualstudio.com/docs/agent-customization/custom-agents.md`, HTTP 200, 15,714 B, SHA-256 `8643b0986edea38447e9c759052284439a39e332d9f3dea2c4a6934c3361b07f`.

### Base citation check

The base SOURCES blob was extracted with `timeout 900 git -C /fast/scratch/hyaku/kotoba-r56/SrcVSCode show e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8:corpus/SOURCES.md > base-SOURCES.md`. `functions.grep` searched that frozen base file for the exact S074 URL `https://code.visualstudio.com/docs/agent-customization/custom-agents.md` and for `^\| S074 \|`; both returned `No matches found`. Thus the URL and ID were absent at the specified base before drafting the row.

## C1 sandbox dry-run

The sandbox clone was created at `/fast/scratch/hyaku/kotoba-r56/SrcVSCode` from the lane and checked out at `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`. Only the following four files were committed in the dry-run world: `SKILL.md` (the exact heading/header and VS Code row), `corpus/knowledge/agent-definition-files-round56.md` (the VS Code entry row), `corpus/SOURCES.md` (S074), and `corpus/lessons/round-56.md` (the Gate row). No verifier or counter was edited.

Commit command:

```sh
timeout 900 git -C /fast/scratch/hyaku/kotoba-r56/SrcVSCode add -- SKILL.md corpus/SOURCES.md corpus/knowledge/agent-definition-files-round56.md corpus/lessons/round-56.md && timeout 900 git -C /fast/scratch/hyaku/kotoba-r56/SrcVSCode commit -m 'Round 56 VS Code C1 dry-run' && git -C /fast/scratch/hyaku/kotoba-r56/SrcVSCode rev-parse HEAD && git -C /fast/scratch/hyaku/kotoba-r56/SrcVSCode show --stat --oneline --summary HEAD
```

Observed: commit `fe5badd809f47482878ad55ac06eeea27f4894ae`; `4 files changed, 19 insertions`; the two new files are the requested knowledge entry and lesson. The commit is sandbox-only.

Counter command:

```sh
timeout 900 bash -lc 'python3 -B verifiers/check_agent_definitions.py --rev fe5badd809f47482878ad55ac06eeea27f4894ae --fetch; rc=$?; printf "COUNTER_EXIT=%s\\n" "$rc"; exit 0'
```

Observed output:

```text
agent-definition locations found on the live page 1 of 1; new ground 1
Claude Code  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Codex        no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
VS Code      BACKED token=.github/agents norm=.github/agents found=yes base_count=0
Copilot CLI  no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
COUNTER_EXIT=1
```

VS Code is `BACKED`: the live page contains the recorded quote and path, and `.github/agents` has `base_count=0`. This one-client fixture reports `F=1`, `G=1`, exit 1; it does not satisfy the frozen global thresholds `F>=5`, `G>=2` and is not evidence that the full round claim passed.

## Rejections, surfaces, and limits

- Rejected as a source: `https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/copilot/customization/custom-agents.md` returned HTTP 404 (14 B; digest above), so it supplied no quote or content. The current official `.md` route on `code.visualstudio.com` was used instead.
- The candidate HTML route was not retained as the S074 URL because `curl -L` reported the current canonical path; its fetched page was used as an HTML cross-check. No status for the pre-redirect response was recorded.
- The opened custom-agent reference page was used for field semantics, not as a second S074 source row; it does not establish workspace-versus-user location precedence.
- This seat did not edit lane product files, the frozen counter, `verifiers/verify_surfaces.py`, C2 map dispositions, or any agent-definition delegate. C2 remains withdrawn per the plan. No tool was installed or updated.
- The counter only establishes documentation quote/path presence and the frozen source/table conditions. It does not establish that VS Code loads a given file at runtime. The sandbox table contains only this client's row; other clients' coverage and the complete C1 predicate remain outside this seat's dry-run.

**Touched surfaces:** in the lane, only this report file was written. In the sandbox commit above: `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/agent-definition-files-round56.md`, `corpus/lessons/round-56.md`.

**Artifacts:** report `.ufo/waves/round-56/build/SrcVSCode.md`; fetched bytes and sandbox clone/commit under `/fast/scratch/hyaku/kotoba-r56/SrcVSCode/` (commit `fe5badd809f47482878ad55ac06eeea27f4894ae`).
