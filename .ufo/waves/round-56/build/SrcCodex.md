Result: PARTIAL — source evidence and all requested paste-ready cells are prepared, but the sandbox counter dry-run was not executed.

## Findings

### Selected source and quote

The client's official **Subagents** documentation describes local custom-agent files under both personal and project paths. The exact selected quote is 20 words, preserves the source's Markdown backticks, and appears in the fetched Markdown at `subagents.md:341-343`:

> To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents.

The quote includes both documented paths, and “agents” outside either path. The page is official OpenAI Codex documentation. The requested direct `.md` URL returned HTTP 200 after redirecting to OpenAI's Learn host, which the frozen C1 `HOSTS` map also permits (`verifiers/check_agent_definitions.py:135-140`). The canonical and `.md` routes were both absent from the base SOURCES registry (commands below). `.codex/agents/` is held at base per `plans/round-56.md:35-38`, so this row can back Codex but contributes no new-ground path.

### Ready-to-paste blocks

1. **SOURCES row**

```markdown
| S073 | OpenAI Developers — Subagents — https://developers.openai.com/codex/subagents.md | docs | A | Codex custom-agent definition locations and local TOML file schema (vendor documentation; not runtime behavior) | § Custom agents (`subagents.md:333-415`), § Custom agent file schema (`:387-415`); fetched `https://developers.openai.com/codex/subagents.md` → `https://learn.chatgpt.com/docs/agent-configuration/subagents.md`, HTTP 200, 22,907 B, sha256 `e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f`, 2026-10-23T02:47:05Z (seat SrcCodex) | Codex documents standalone TOML agents in personal/project directories, three required definition keys, model settings and supported feature switches | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

2. **Knowledge-entry row**

```markdown
| Codex | `.codex/agents/` | S073 | "To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents." |
```

3. **Detail paragraph**

```markdown
Codex agent definitions are standalone TOML files, not Markdown with YAML frontmatter or JSON: “To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents.” (`subagents.md:341-343`). Required keys are `name`, `description`, and `developer_instructions` (“Every standalone custom agent file must define:” — `subagents.md:350-354`). Capability reduction uses supported feature keys set to `false` (“To reduce a custom agent's capabilities, set supported feature keys to `false`:” — `subagents.md:400-405`), including `features.shell_tool`, `features.apps`, `features.plugins`, `features.memories`, and `features.request_permissions_tool`; this section does not document a generic `tools` allowlist. Model behavior keys include `model`, `model_reasoning_effort`, `model_reasoning_summary`, and `model_verbosity` (“Use `model`, `model_reasoning_effort`, `model_reasoning_summary`, and `model_verbosity` to customize model behavior.” — `subagents.md:395-398`). When set in a custom-agent file, `model` or `model_reasoning_effort` takes precedence (“If a custom agent file sets `model` or `model_reasoning_effort`, the value in the file takes precedence.” — `subagents.md:356-358`); otherwise Codex resolves each setting from explicit spawn value, then `[agents]` default, then the parent's value (“Before applying the file, Codex resolves each setting from an explicit spawn value, then the corresponding `[agents]` default, then the parent's value.” — `subagents.md:357-360`). The page distinguishes personal from project-scoped directories, but does not state which directory wins for a same-named custom agent. It does state that a custom agent matching a built-in name takes precedence over that built-in (“If a custom agent name matches a built-in agent such as `explorer`, your custom agent takes precedence.” — `subagents.md:385`); this is not a user-vs-project precedence rule.
```

4. **SKILL.md heading and table**

```markdown
### Agent-definition files by client

| Client | Definition location | What the file sets | Action |
|---|---|---|---|
| Codex | `.codex/agents/` (+ user path `~/.codex/agents/`) | Standalone TOML; required `name`, `description`, `developer_instructions`; supported `features.*` switches can disable capabilities; `model` and related keys set model behavior | Create a focused agent profile |
```

5. **Gate row**

```markdown
| S073 | https://developers.openai.com/codex/subagents.md | 2026-10-23T02:47:05Z | 22,907 B, sha256 `e7469d41`… | "To define your own custom agents, add standalone TOML files under `~/.codex/agents/` for personal agents or `.codex/agents/` for project-scoped agents." | `subagents.md:341-343` | SrcCodex |
```

The sentence occupies three Markdown source lines; table-ready quotes join those line wraps with spaces, retain all words and punctuation, and do not strip the inline-code backticks.

## Evidence and gates

- Fetch command: `mkdir -p /fast/scratch/hyaku/kotoba-r56/SrcCodex && date -u && curl -sSL --max-time 90 -w '\nHTTP %{http_code} effective %{url_effective}\n' -o /fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.md https://developers.openai.com/codex/subagents.md; rc=$?; printf 'curl_exit=%s\n' "$rc"; wc -c -l /fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.md; sha256sum /fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.md`
  - `date -u`: `Fri 23 Oct 2026 02:47:05 AM UTC`
  - Observed: `HTTP 200 effective https://learn.chatgpt.com/docs/agent-configuration/subagents.md`; `curl_exit=0`; `563` lines, `22907` bytes; SHA-256 `e7469d41c5a18a4ee66ee40ca4a9a2617a697e42554a0198ac4481e1e597357f`.
- Base URL check, canonical URL: `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -nF 'https://developers.openai.com/codex/subagents' b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- corpus/SOURCES.md` → exit 1, no output.
- Base URL check, `.md` URL: `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -nF 'https://developers.openai.com/codex/subagents.md' b0b7140b5a7cf8a50f13989ee6285fc8ee245c41 -- corpus/SOURCES.md` → exit 1, no output.
- Live HTML route was also fetched at the same `date -u` time: `curl -sSL --max-time 90 -w '\nHTTP %{http_code} effective %{url_effective}\n' -o /fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.html https://developers.openai.com/codex/subagents`; observed HTTP 200, effective URL `https://learn.chatgpt.com/docs/agent-configuration/subagents`, `614442` bytes / `6796` lines, SHA-256 `bf21f1997d6de96ef1b5293d8bedb1961681f0d07e02133515e4e0202d7a4bb43`. The HTML body contains the same selected sentence at `subagents.html:5119-5120`.
- Frozen-counter code was read, not run. Its host map includes `developers.openai.com`, `learn.chatgpt.com`, and `github.com/openai/codex` (`verifiers/check_agent_definitions.py:135-140`); the fetched redirect therefore remains within the actual frozen host map.
- **Dry-run status:** no sandbox clone or commit was made and `python3 -B .../verifiers/check_agent_definitions.py --rev <rev> --fetch` was not invoked. The assigned scribe role prohibits invoking another runtime or judge and prohibits commits. Accordingly, no observed `Codex` found yes/no line or exit code exists; I do not fabricate one. Codex's held path means it contributes no new-ground count even if the quote is found.

## Rejections / opened but not used

- `https://developers.openai.com/codex/subagents` — HTTP 200 redirect to `https://learn.chatgpt.com/docs/agent-configuration/subagents`; opened, but the `.md` route was selected for direct prose and stable Markdown line citations. The HTML route independently contains the quote.
- `https://api.github.com/repos/openai/codex/git/trees/main?recursive=1` — HTTP 200, fetched as a repository-tree index only; not used as source evidence because the index is not the client's documentation page establishing the definition-file contract.

## Surfaces, scope, limits, artifacts

- Lane file written: `.ufo/waves/round-56/build/SrcCodex.md` only. No product file, counter, knowledge entry, SOURCES row, lesson, or SKILL.md table was edited; this report supplies paste-ready content for integration. No sandbox clone/commit, test, or package installation was performed.
- C2 remains out of scope and withdrawn before data. No delegate or map disposition was changed.
- Scratch fetch artifacts: `/fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.md`, `/fast/scratch/hyaku/kotoba-r56/SrcCodex/subagents.html`, and `/fast/scratch/hyaku/kotoba-r56/SrcCodex/codex-tree.json` (the API tree fetch was HTTP 200, `3352083` bytes, SHA-256 `7adcfe6675a872ef69562e1b9b81d624cfdeca00255a1a30343bdd2634a6093d`).
- No tools were installed or updated.
- Main known limits: the frozen `--fetch` predicate remains unmeasured for this proposed world; the source does not specify precedence between the personal and project agent directories. SKILL.md is at its stated 598/600-line budget, so integration must preserve the nine byte-identical checklist texts and account for the required table placement/space without editing those boxes.
