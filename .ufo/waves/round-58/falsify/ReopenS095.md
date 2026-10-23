Result: HOLDS — S095 re-opened byte-identical (200, 7,242 B, same sha256); the entry quote is verbatim at commands.mdx:21, the shaping note is accurate, and every fact in the SKILL.md cells and entry bullet verifies against the page.

Seat: KotobaR58.ReopenS095. Target: SOURCES row S095 (opencode V2 commands docs, pinned `4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3`), SKILL.md:119 opencode row, entry `corpus/knowledge/command-files-round58.md` opencode row+bullet, at `46b4a706`. `git --no-optional-locks diff 46b4a706..HEAD -- SKILL.md corpus/SOURCES.md corpus/knowledge/command-files-round58.md` is empty (exit 0): working copy == content commit for all three files.

## Re-open

- `date -u`: Fri 23 Oct 2026 08:26:49 AM UTC
- `curl -sS https://raw.githubusercontent.com/anomalyco/opencode/4e0bc52216d91c3a8d10035837b1b6f9b82fd1d3/services/www/src/docs/content/commands.mdx` → HTTP_STATUS=200, BYTES=7242, sha256 `dda6bba03043afff71a0bec4f0cfa40aaac12d53c1b20358df15e557c1a7ec11` — matches SOURCES.md:107 (7,242 B, same sha) exactly; the page is unchanged since the row's 2026-10-23T08:08:26Z fetch.
- Row anchor check: § Markdown is at `commands.mdx:19`; cited lines `:21` (locations sentence), `:28` (`.md`-only + nested `/` names), `:34-37` (nested invocation, legacy `command/`, frontmatter/trimmed-body sentence) — all real. § Fields `:68-77` is the field table. § Arguments `:99-105` is the `$ARGUMENTS` sentence + example. "V2" attribution holds: the file is under `services/www/`, and `https://opencode.ai/v2/docs/commands` serves this content (below).

## Q42 — entry quote and shaping note

Entry quote (`command-files-round58.md:40`): "Put global commands in `~/.config/opencode/commands/` and project commands in `.opencode/commands/`." — byte-exact copy of `commands.mdx:21`, verified against the fetched bytes. No shaping was applied or needed. HOLD.

Note at `:30-31`: "the opencode quote is from the pinned docs source because the served page is HTML without `Accept: text/markdown`." Verified 2026-10-23T08:27:04Z/08:27:11Z:
- `curl https://opencode.ai/v2/docs/commands` → 200, 32,304 B, `content-type=text/html` — page is HTML by default, as stated.
- `curl https://opencode.ai/v2/docs/commands.md` → 404, 9 B (contrast: v1 `https://opencode.ai/docs/commands.md` → 200, 6,664 B, text/plain — so the v2 site has no `.md` route).
- `curl -H 'Accept: text/markdown' https://opencode.ai/v2/docs/commands` → 200, 7,220 B, `content-type=text/markdown`, sha256 `c3dc75fc…`; the quote sentence is line 19 of that body, byte-identical to the pinned source.
The note is literally accurate — the served page *is* HTML without the header — and it does not falsely claim markdown is unobtainable. HOLD. [INFERENCE] The seat quotes fetched bytes only, so a raw GitHub source was the clean fetch.

## SKILL.md:119 — every fact, one line each

Row: `| opencode | `.opencode/commands/` (project; user `~/.config/opencode/commands/`) | `.md` only; nested path → `/`-separated name; optional YAML frontmatter; trimmed body is the template; `$ARGUMENTS` (S095 `:21,28,37,99`) | Keep the body a complete prompt template |`

- Command files cell, `.opencode/commands/` (project) — HOLDS, `commands.mdx:21` names it the project folder.
- Command files cell, user `~/.config/opencode/commands/` — HOLDS, `:21` calls it "global"; user↔global is the same home-folder convention used by sibling rows.
- What a file sets, `.md` only — HOLDS, `:28` "Only `.md` files are discovered."
- What a file sets, nested path → `/`-separated name — HOLDS, `:28` "Nested paths become command names with `/` separators" (example `:30-34`, `/team/review`).
- What a file sets, optional YAML frontmatter — HOLDS, `:37` "Add YAML frontmatter when the command needs metadata."
- What a file sets, trimmed body is the template — HOLDS, `:37` "The trimmed Markdown body is always the prompt template" (reinforced by `:95`, body supplies `template`).
- What a file sets, `$ARGUMENTS` — HOLDS, `:99` "Use `$ARGUMENTS` for the complete argument string exactly as entered."
- Cited anchors `:21,28,37,99` — all four are the right lines. HOLD.
- Action cell, "Keep the body a complete prompt template" — actionable guidance consistent with `:37`/`:95` (the body is the template verbatim); reviewer judgment, nothing on the page contradicts it. HOLD as advice.

## Entry `What a file sets` bullet (`command-files-round58.md:57-59`)

- "only `.md` files are discovered and nested paths become `/`-separated names (`:28`)" — HOLDS, `:28`.
- "optional YAML frontmatter, and the trimmed body is the prompt template (`:37`)" — HOLDS, `:37`.
- "`$ARGUMENTS` is the whole argument string (`:99`)" — HOLDS, `:99` ("complete argument string exactly as entered"; example `:105`).
- "the user folder is `~/.config/opencode/commands/` (`:21`)" — HOLDS, `:21`.
- Entry table row `:40` folder cell `.opencode/commands/` — HOLDS, `:21`; quote verified above.

## Residual risk / observations (not defects)

- Completeness, not correctness: the page also documents frontmatter fields `description`/`agent`/`model`/`subagent`/`subtask` (`:72-77`), positional `$1`–`$n` placeholders (`:109-117`), `!` shell blocks (`:143-160`), no-placeholder argument fallback (`:127`), global-vs-project precedence (`:243-252`), and legacy `command/` dirs (`:34`). Neither the cell nor the bullet claims exhaustiveness, but note the asymmetry: the Codex row/bullet names both its positional (`$1`–`$9`) and `$ARGUMENTS` placeholders, while the opencode row/bullet names `$ARGUMENTS` only and omits `$1`–`$n` (`:109`). Counter does not read these cells (entry `:65-67`, Q31).
- Served-page drift: the live V2 markdown body differs from the pinned commit only in three example model strings (served `claude-sonnet-4-5`, `gpt-5`; pinned `claude-sonnet-5-5`, `gpt-6.1-sol`) plus the `# Commands` H1 — the served build is older than the pin. No cited line, fact, or the quote is touched.
- Terminology: page says "global", rows say "user" — same path `:21`; consistent with sibling-row convention.

## Verification gaps

None for the named scope: URL re-fetched byte-identical, every cited line read in the fetched bytes, both cells and the bullet checked fact-by-fact, shaping note probed on all three routes (`/v2/docs/commands`, `.md`, `Accept: text/markdown`). No client was run (entry's own Limit, `:63` — vendor documentation only).

Tooling: none installed or updated.
