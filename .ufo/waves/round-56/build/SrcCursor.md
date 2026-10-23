Result: DONE — Cursor’s official subagent documentation supports S077, and the isolated one-client dry-run found its location and quote on the live page.

## Findings and source evidence

- Base URL reuse check, before drafting: `timeout 900s bash -lc 'grep -n "https://cursor.com/docs/subagents.md" /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md'` → exit 1, no output (no exact URL match).
- Fetch command: `timeout 900s bash -lc 'date -u; curl -sSL -w "effective_url=%{url_effective}\nHTTP %{http_code}\nsize_download=%{size_download}\n" https://cursor.com/docs/subagents.md -o /fast/scratch/hyaku/kotoba-r56/SrcCursor/subagents.md.fetched && wc -c /fast/scratch/hyaku/kotoba-r56/SrcCursor/subagents.md.fetched && sha256sum /fast/scratch/hyaku/kotoba-r56/SrcCursor/subagents.md.fetched'` → exit 0.
  - `date -u`: `Fri Oct 23 02:47:16 AM UTC 2026`
  - Requested/effective URL: `https://cursor.com/docs/subagents.md`; HTTP 200; 27,660 bytes; SHA-256 `264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668`.
- Downloaded bytes: `/fast/scratch/hyaku/kotoba-r56/SrcCursor/subagents.md.fetched` (491 lines). Markdown was not stripped. The selected quote is byte-exact at `subagents.md.fetched:427` (16 words).
- Word-count command (exit 0, output `16`):
  ```sh
  timeout 900s bash -lc 'printf "%s\n" "You can also create subagents manually by adding markdown files to \`.cursor/agents/\` (project) or \`~/.cursor/agents/\` (user)." | wc -w'
  ```
  - Quote: “You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user).”
- Detail from the fetched bytes: the page says “Each subagent is a markdown file with YAML frontmatter:” (`subagents.md:96`). The configuration table marks `name`, `description`, `model`, `readonly`, and `is_background` as Required `No` (`:122-128`); the `name` row says “Derived from filename” (`:124`), so no listed field is required. The documented write restriction is `readonly`: its row says “restricted write permissions (no file edits, no state-changing shell commands)” (`:127`); the configuration-fields table has no separate tools-allowlist field (`:122-128`). `model` is the model key: “The `model` field controls which model a subagent uses” (`:132`); `inherit` “Uses the same model as the parent agent. This is the default” (`:136`), while a specific ID “Uses the exact model you specify” (`:137`). The locations table gives project `.cursor/agents/` for “Current project only” (`:85`) and user `~/.cursor/agents/` for “All projects for current user” (`:88`). Precedence: “Project subagents take precedence when names conflict” and `.cursor/` takes precedence over `.claude/` or `.codex/` (`:92`).

## Ready-to-paste blocks

1. SOURCES row:

```text
| S077 | Cursor Docs — Subagents — https://cursor.com/docs/subagents.md | docs | A | Cursor's documented Markdown/YAML subagent file format, configuration fields, project and user locations, and name-conflict precedence | § File locations, `subagents.md:81-92`; § File format and Configuration fields, `:94-128`; § Model configuration, `:130-139`; § Creating subagents, `:421-427`; fetched 2026-10-23T02:47:16Z, HTTP 200, 27660 B, sha256 `264b4b00e713ec0dd73939306690ea4013168bead35411da3cc56fc1a71b2668` (seat SrcCursor) | Cursor documents Markdown files with YAML frontmatter, optional fields including `model` and `readonly`, project and user subagent paths, and project precedence for name conflicts | mined | 2026-10-23 | 90d | corpus/knowledge/agent-definition-files-round56.md, corpus/lessons/round-56.md |
```

2. Entry row:

```text
| Cursor | `.cursor/agents/` | S077 | "You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user)." |
```

3. Detail paragraph: “Each subagent is a markdown file with YAML frontmatter:” (`subagents.md:96`). The configuration table marks `name`, `description`, `model`, `readonly`, and `is_background` as Required “No” (`:122-128`); `name` is “Derived from filename” (`:124`). The documented write-restriction field is `readonly`, with “restricted write permissions (no file edits, no state-changing shell commands)” (`:127`); the configuration-fields table has no separate tools-allowlist field (`:122-128`). For model, “The `model` field controls which model a subagent uses” (`:132`); `inherit` “Uses the same model as the parent agent. This is the default” (`:136`), while a specific ID “Uses the exact model you specify” (`:137`). The project row pairs `.cursor/agents/` with “Current project only” (`:85`); the user row pairs `~/.cursor/agents/` with “All projects for current user” (`:88`). Precedence: “Project subagents take precedence when names conflict” and “`.cursor/` takes precedence over `.claude/` or `.codex/`” (`:92`).

4. SKILL.md row:

```text
| Cursor | `.cursor/agents/` (project); `~/.cursor/agents/` (user) | Markdown with YAML frontmatter; listed fields `name`, `description`, `model`, `readonly`, and `is_background` are optional; `readonly` restricts write permissions; `model` selects the model | Apply checklist to Cursor subagents |
```

5. Gate row:

```text
| S077 | https://cursor.com/docs/subagents.md | 2026-10-23T02:47:16Z | 27660 B, sha256 `264b4b00…` | "You can also create subagents manually by adding markdown files to `.cursor/agents/` (project) or `~/.cursor/agents/` (user)." | `subagents.md:427` | SrcCursor |
```

## Dry-run gate and provenance

The requested clone command found the sandbox path already present and exited 128 (`fatal: destination path '/fast/scratch/hyaku/kotoba-r56/SrcCursor' already exists and is not an empty directory`). Read-only inspection showed its HEAD was `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`; `git status --short --branch` showed only `## HEAD (no branch)` before this work. The fetched page was saved in this sandbox. The dry-run world changed only `SKILL.md`, `corpus/SOURCES.md`, the new `corpus/knowledge/agent-definition-files-round56.md`, and the new `corpus/lessons/round-56.md`; the fetched source file was not committed.

Sandbox commit: `e42713a27cb791cc3399e2effc8bd4fc145cc087` (`Add Cursor agent-definition dry-run world`), 4 files changed, 22 insertions. Counter command: `timeout 900s python3 -B verifiers/check_agent_definitions.py --rev e42713a27cb791cc3399e2effc8bd4fc145cc087 --fetch` from `/fast/scratch/hyaku/kotoba-r56/SrcCursor` → exit 1; output began `agent-definition locations found on the live page 1 of 1; new ground 1`. Cursor’s line was `Cursor       BACKED token=.cursor/agents/ norm=.cursor/agents found=yes base_count=0`: found yes; reason, the row was backed and the live page contained the quote and path, with zero base occurrences. The other six rows were absent from this deliberately one-client world. The full predicate was not met in this world (F=1, G=1; required F≥5, G≥2); this is not a full-round measurement.

## Rejections, touched surfaces, and limits

- Rejected pages opened: none; the candidate page was used.
- Lane surfaces changed: this report only, `.ufo/waves/round-56/build/SrcCursor.md`. No product files, counter, verifier, or C2 surface was edited in the lane. No tool was installed.
- Sandbox surfaces/commit and fetched artifact are listed above. No build, self-test, lint, or other gate was run; only the requested C1 `--fetch` dry-run was executed.
- Out of scope: other client rows, full-round C1 threshold, C2 (withdrawn), and any claim about runtime client behavior. The counter does not evaluate whether Cursor loads definitions as documented.
