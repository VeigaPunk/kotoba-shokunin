Result: DONE — Re-opened the Claude Code docs, confirmed the frozen counter matches the project command-folder token, and drafted the S089 source, entry, skill, and Gate rows.

## Findings

Fetched `https://code.claude.com/docs/en/slash-commands.md` with `curl -sSL` at the following `date -u` output:

```text
Fri Oct 23 08:08:35 AM UTC 2026
HTTP_STATUS=200
BYTES=114542
6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd  /fast/scratch/hyaku/kotoba-r58/SrcClaudeCode/claude-slash-commands.md
```

The quote below is 14 words and is a contiguous raw-Markdown substring of fetched `slash-commands.md:172`. No bytes inside the selected quote were changed; the line's leading list-marker bytes `* ` are omitted, and the emphasis markers and inline-code backticks are retained:

> **Command files**: a Markdown file in `.claude/commands/` is the older format and still works.

The passage does not label command files deprecated or legacy: it calls the form “the older format” and says it still works (`slash-commands.md:172`). The page says custom commands have been merged into skills and prefers a skill for new work because skills can have supporting files (`:17,172`). It does not state a `~/.claude/commands/` user path; therefore the proposed row scopes the token to project `.claude/commands/`. It also says an added directory loads its `.claude/commands/` (`:190`).

## Frozen-counter probe

Sandbox clone revision observed:

```text
3de87aad29e960c95ed35840442f424c48c29729
```

Command run (the Python import is from the sandbox clone; the exact URL, quote, and token passed to the requested functions are shown):

```sh
timeout 900 sh -c 'git -C /fast/scratch/hyaku/kotoba-r58/SrcClaudeCode rev-parse HEAD && timeout 900 python3 -B -c '\''import sys; sys.path.insert(0, "/fast/scratch/hyaku/kotoba-r58/SrcClaudeCode"); from verifiers import check_command_files as c; url = "https://code.claude.com/docs/en/slash-commands.md"; quote = "**Command files**: a Markdown file in `.claude/commands/` is the older format and still works."; page = c.fetch(url); print(c.found_on_page(page, quote, ".claude/commands/"))'\'''
```

Outcome: exit 0; output was the revision above followed by `True`.

## Drafts (verbatim)

### SOURCES.md row

```markdown
| S089 | Claude Code Docs — Extend Claude with skills (custom command files) — https://code.claude.com/docs/en/slash-commands.md | docs | A | Claude Code `.claude/commands/` Markdown files, supported frontmatter and arguments, and file-name-to-command mapping (vendor documentation; not a runtime test) | § Where skills live (`slash-commands.md:172`); § Frontmatter reference (`:378,402-403`); § How a skill gets its command name (`:450-451`); fetched 2026-10-23T08:08:35Z, HTTP 200, 114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` (seat SrcClaudeCode) | Claude Code documents `.claude/commands/` Markdown command files as still-working older-format files; they accept skill frontmatter except `name` and `paths`, map file names to slash commands, and document argument hints and named positional arguments | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |
```

### Entry row

```markdown
| Claude Code | `.claude/commands/` | S089 | "**Command files**: a Markdown file in `.claude/commands/` is the older format and still works." |
```

### SKILL.md row

```markdown
| Claude Code | `.claude/commands/` (project; an added directory also loads this folder) | Markdown file (`"a Markdown file in `.claude/commands/`"`, `slash-commands.md:172`); file name without extension maps to the slash-command name (`".claude/commands/deploy.md" → "/deploy"`, `:450`; nested path mapping at `:451`); same frontmatter fields as skills except `name` and `paths` (`"accepts the same fields except `name` and `paths`"`, `:378`); optional `argument-hint` and named positional `arguments` for `$name` substitution (`"Hint shown during autocomplete"`, `:402`; `"Names map to argument positions in order"`, `:403`) | Prefer skills for new work; keep existing command files where useful |
```

### `## Gate` line

```markdown
| S089 | https://code.claude.com/docs/en/slash-commands.md | 2026-10-23T08:08:35Z | 114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` | "**Command files**: a Markdown file in `.claude/commands/` is the older format and still works." | `slash-commands.md:172` | SrcClaudeCode |
```

## Surfaces and limits

- Written lane surface: `.ufo/waves/round-58/build/SrcClaudeCode.md` (this report only). No product, counter, corpus, or Git index files were changed.
- Sandbox artifacts: `/fast/scratch/hyaku/kotoba-r58/SrcClaudeCode/` (frozen clone and fetched Markdown page).
- The requested direct `fetch`/`found_on_page` counter probe returned `True`. The complete C1 counter and merged table were not run or verified; this seat's deliverable is drafts only.
- Initial reads found `corpus/knowledge/command-files-round58.md` and `corpus/lessons/round-58.md` absent from the lane tree at report time. No tool was installed.
