Result: DONE — S072 is live-page-backed and the isolated dry-run finds Claude Code; the held path adds no new ground and this one-client world does not meet round-wide C1.

## Finding and source evidence

Selected official page: **Claude Code Docs — Subagents in the SDK**, https://code.claude.com/docs/en/agent-sdk/subagents.md. At `sdk-subagents.md:17`, the fetched Markdown states: `* **Filesystem-based**: define agents as markdown files in `.claude/agents/` directories.` The quote below preserves the page's Markdown markers; no Markdown was stripped. The dot-directory occurs as page text, not inside a URL, and `agents` also occurs outside that path.

Base URL check, before drafting:

```text
timeout 30s grep -n 'https://code.claude.com/docs/en/agent-sdk/subagents.md' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
exit 1; no output
```

Selected-page fetch command and observed metadata:

```text
timeout 60s mkdir -p /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode && date -u && timeout 60s curl -sS -L -D /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sdk-subagents.headers -o /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sdk-subagents.md -w 'HTTP %{http_code}\nURL %{url_effective}\n' 'https://code.claude.com/docs/en/agent-sdk/subagents.md' && timeout 20s wc -c /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sdk-subagents.md && timeout 20s sha256sum /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sdk-subagents.md
```

Observed: `Fri 23 Oct 2026 02:48:46 AM UTC`; HTTP 200; effective URL `https://code.claude.com/docs/en/agent-sdk/subagents.md`; `wc -c` = 41461; SHA-256 `5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315`. The quote is at fetched bytes' line 17. `read` showed `sdk-subagents.md:14-18`: the page distinguishes programmatic agents, filesystem-based Markdown definitions in `.claude/agents/`, and built-in agents.

Supporting and rejected-page fetch commands (each `curl` returned HTTP 200; byte counts and full hashes are recorded below with the related page):

```text
date -u && timeout 60s curl -sS -L -D /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sub-agents.headers -o /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sub-agents.md -w 'HTTP %{http_code}\nURL %{url_effective}\n' 'https://code.claude.com/docs/en/sub-agents.md' && timeout 20s wc -c /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sub-agents.md && timeout 20s sha256sum /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/sub-agents.md
timeout 60s mkdir -p /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode && date -u && timeout 60s curl -sS -L -D /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/best-practices.headers -o /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/best-practices.md -w 'HTTP %{http_code}\nURL %{url_effective}\n' 'https://code.claude.com/docs/en/best-practices.md' && timeout 20s wc -c /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/best-practices.md && timeout 20s sha256sum /fast/scratch/hyaku/kotoba-r56/SrcClaudeCode/best-practices.md
```

## Ready-to-paste blocks

**1. SOURCES.md row (11 cells)**

```markdown
| S072 | Claude Code Docs — Subagents in the SDK — https://code.claude.com/docs/en/agent-sdk/subagents.md | docs | A | Claude Agent SDK documentation of filesystem-based subagent definition files | § Overview, `sdk-subagents.md:14-18`; fetched 2026-10-23T02:48:46Z, HTTP 200, 41,461 B, sha256 `5b7aa6c66705f223744ac58acd69b7629d4ccd23c56655678c975b22f9711315` (seat SrcClaudeCode) | Filesystem-based subagent definitions are Markdown files in `.claude/agents/` directories, distinguished from programmatic and built-in subagents | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

**2. Entry row (the first table header is exact)**

```markdown
| Client | Location | Source | Quote |
|---|---|---|---|
| Claude Code | `.claude/agents/` | S072 | "**Filesystem-based**: define agents as markdown files in `.claude/agents/` directories." |
```

**3. Detail paragraph with line-cited source quotes**

S072 itself states the filesystem form and path. For file-format details, the already-existing S026 Claude Code subagents page (supporting detail only, not the entry's counted source) says “Subagents are Markdown files with YAML frontmatter” (`sub-agents.md:94`) and “Subagent files use YAML frontmatter for configuration, followed by the system prompt in Markdown” (`:242`). It says “Only `name` and `description` are required” (`:289`); “To restrict tools, use the `tools` field as an allowlist or the `disallowedTools` field as a denylist” (`:446`); and “The `model` field controls which model the subagent uses” (`:349`). The scope table lists “`.claude/agents/` | Current project | 3” (`:162`) and “`~/.claude/agents/` | All your projects | 4” (`:163`); the page says that same-name definitions use “the one from the higher-priority location” (`:156`). The full table orders managed settings 1, `--agents` CLI 2, project 3, user 4, plugin 5 (`:158-164`): project definitions outrank user definitions, while managed and CLI definitions outrank both. S026 was re-fetched as `https://code.claude.com/docs/en/sub-agents.md` at `Fri 23 Oct 2026 02:49:03 AM UTC`, HTTP 200, 111,624 B, sha256 `84b2646c513754ef5f33c6f5a0d7f59960021a65b5a09c35b9158fa116a73d5a`; it remains background evidence, not S072.

**4. SKILL.md table section and Claude Code row**

```markdown
### Agent-definition files by client

| Client | Definition location | What the file sets | Action |
|---|---|---|---|
| Claude Code | `.claude/agents/` (user path: `~/.claude/agents/`) | Markdown files with YAML frontmatter and a Markdown system prompt; required `name` and `description`; `tools` allowlist restricts available tools; optional `model` controls model choice | Create project subagents and scope tool access |
```

The format/field statements in this cell are the S026 supporting details cited above; S072 remains the entry's new source. The first backticked span in the location cell is the project directory. The action is seven words.

**5. Round-56 Gate row**

```markdown
| S072 | https://code.claude.com/docs/en/agent-sdk/subagents.md | 2026-10-23T02:48:46Z | 41,461 B, sha256 `5b7aa6c6…` | "**Filesystem-based**: define agents as markdown files in `.claude/agents/` directories." | `sdk-subagents.md:17` | SrcClaudeCode |
```

## Dry-run and gate outcome

Sandbox clone was created at `/fast/scratch/hyaku/kotoba-r56/SrcClaudeCode`, checked out at frozen erratum base `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`. The first commit was `71170241d2d5b66daaad90ac98c7e310dc3a82d4` (four requested surfaces). That first draft had omitted the source's `**` around `Filesystem-based`; its initial counter run found Claude Code, but the quote was corrected to preserve source bytes. Correction commit `773bc67d56eaa934cd4fd31b702b7fa92737a182` changed only the entry and Gate quote cells. This final commit is the measured world and still contains only `SKILL.md`, `corpus/SOURCES.md`, `corpus/knowledge/agent-definition-files-round56.md`, and `corpus/lessons/round-56.md` relative to e02.

Final command:

```text
timeout 900s python3 -B verifiers/check_agent_definitions.py --rev 773bc67d56eaa934cd4fd31b702b7fa92737a182 --fetch
```

Observed output (exit 1):

```text
agent-definition locations found on the live page 1 of 1; new ground 0
Claude Code  BACKED token=.claude/agents/ norm=.claude/agents found=yes base_count=3
```

Claude Code: **found=yes**. The frozen path is held (`base_count=3`), so this row contributes F but not new ground G. The single-client world has F=1/1 and G=0; it cannot establish the full predicate (F≥5 and G≥2). Exit 1 is the expected overall result for this intentionally one-client world, not a Claude Code page miss. The initial quote-correction run used `timeout 900s python3 -B verifiers/check_agent_definitions.py --rev 71170241d2d5b66daaad90ac98c7e310dc3a82d4 --fetch`; it printed the same 1-of-1/G=0 and Claude `found=yes`, exit 1, but is superseded because the entry quote was not byte-exact.

The sandbox table append takes SKILL.md from its base 598 lines to 604 lines. This dry-run is therefore not a line-budget-compliant product patch; integration must preserve the 600-line gate. No lane product file or counter was edited. No tool was installed or updated.

## Rejected page opened

- **Claude Code — Best practices for Claude Code**, `https://code.claude.com/docs/en/best-practices.md`: fetched at `Fri 23 Oct 2026 02:47:45 AM UTC`, HTTP 200, 36,360 B, sha256 `b225977e2892002cc91ff4dfe2d6a7e2324fd455aa6325c889cecb009ca76052`. Its line 279 says “Define specialized assistants in `.claude/agents/` that Claude can delegate to for isolated tasks.” I did not select it: that path sentence has no `agent`/`subagent` word outside the path; the next paragraph has “Subagents” but is separate. The selected SDK page puts the location and outside-path `agents` in one direct line. No claim is made that the Best practices page is inaccurate.

## Scope, limits, and artifacts

- **Touched surfaces:** only the four requested files in the sandbox clone; sandbox commits listed above. In the lane, only this report was written: `.ufo/waves/round-56/build/SrcClaudeCode.md`.
- **Out of scope:** C2 remains withdrawn; no agentdef delegate, map disposition, verifier, or counter changes; no full seven-client C1 score; no freshness claim.
- **Evidence limit:** the three temporary fetched Markdown files were removed before cloning because the required clone destination was the same seat path. Their sizes, hashes, timestamps, quotes, and line references are recorded here; the raw fetch files are not retained. The final sandbox revision is available at `/fast/scratch/hyaku/kotoba-r56/SrcClaudeCode`.
- **Report artifact:** `.ufo/waves/round-56/build/SrcClaudeCode.md`.
