Result: HOLDS — S090 (Codex) re-fetched live and every checked fact holds; the row receipt, the entry quote, the SKILL.md cells and the entry bullet are all accurate, with only two cosmetic line-anchor imprecisions in the row's section list.

Seat: KotobaR58.ReopenS090 (reviewer, leaf; no subagents dispatched).
State under attack: `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` (C1 content commit). All `git show` reads below are at that rev; lane untouched (read-only git only).

## Re-open (receipt check)

- `date -u`: `Fri 23 Oct 2026 08:26:43 AM UTC`
- `curl -sS -o … -L --max-time 60 'https://learn.chatgpt.com/docs/custom-prompts.md'` → `HTTP 200 | 3357 bytes | url https://learn.chatgpt.com/docs/custom-prompts.md`
- `sha256sum` → `d6f7cf8dd9f31d2faf5604ef3a6f8322132a7b66fa50823109cb681e372a0fa9` (3,357 bytes)
- Row records (SOURCES.md:103, cell 7): `fetched 2026-10-23T08:07:59Z, HTTP 200, 3,357 B, sha256 d6f7cf8d…a0fa9` → **holds**: status, byte count and sha256 all match the live fetch byte-for-byte. Page is live and unchanged since the row's recorded fetch.
- Lesson Gate (corpus/lessons/round-58.md:11) repeats the same URL, HTTP 200, 3,357 B, sha256 `d6f7cf8d…` and quote at `custom-prompts.md:62` → consistent with the fetched bytes.
- Fetched bytes saved at `/fast/scratch/hyaku/kotoba-r58/ReopenS090/custom-prompts.md` (own scratch dir; nothing executed from the lane).

## Q42 — quote verbatim and the shaping note

Entry (corpus/knowledge/command-files-round58.md, Codex row): `"Manage prompts by editing or deleting files under `~/.codex/prompts/`."`
- Byte check against the fetch: that exact string is the leading substring of fetched line 62 (`python3` membership test: `quote at line 62 byte-exact: True`). 9 words, byte-exact → **holds, verbatim at the stated location** (the entry row does not print a line number, but the SOURCES row's manage-commands anchor `:48-62` and the Gate's `custom-prompts.md:62` both resolve to the right line).
- Shaping note accuracy: the note says "every quote is copied from the fetched bytes" and names only the VS Code (`&#124;`), Gemini CLI (list/bold markers kept) and opencode (pinned docs source) exceptions — none applies to Codex, and no shaping was applied to this quote. **The note is accurate for this row**: the table cell contains the raw sentence with no escapes or edits.
- Verifier cross-check [INFERENCE from source read, not a counter run]: `check_command_files.py` requires the quote to hold the row's command token `~/.codex/prompts/` and a command/prompt word outside it; "Manage **prompts** by editing … under `~/.codex/prompts/`" satisfies both, and the Gate line repeats the quote verbatim.

## SKILL.md Codex row (line 114, "Custom command files by client")

`Command files` cell — `~/.codex/prompts/` (user only; not shared through the repo):
- `~/.codex/prompts/` → **holds** (`:15` `mkdir -p ~/.codex/prompts`, `:18` `Create ~/.codex/prompts/draftpr.md`, `:62` `files under ~/.codex/prompts/`).
- "user only" → **holds** (`:10` "live in your local Codex home directory … `~/.codex`").
- "not shared through the repo" → **holds** (`:10` "so they're not shared through your repository").

`What a file sets` cell — `Markdown; draftpr.md → /prompts:draftpr; frontmatter description, argument-hint; $1–$9, $ARGUMENTS (S090 :10,18,34,40-42)`:
- "Markdown" → **holds** (`:8` "turn Markdown files into reusable prompts"; `:46` "Codex ignores non-Markdown files in the prompts directory").
- `draftpr.md → /prompts:draftpr` → **holds** (`:18` creates `~/.codex/prompts/draftpr.md`; `:34` "Typing `/prompts:draftpr` … shows your custom command"; `:51`,`:55` confirm).
- frontmatter `description` → **holds** (`:40` "Set it in YAML front matter as `description:`"; example `:22`).
- frontmatter `argument-hint` → **holds** (`:41` "Document expected parameters with `argument-hint: KEY=<value>`"; example `:23`).
- `$1`–`$9`, `$ARGUMENTS` → **holds, verbatim wording** (`:42` "`$1` through `$9` expand from space-separated arguments … `$ARGUMENTS` includes them all").
- Cited lines (`:10,18,34,40-42`) each back the fact they are attached to → **holds**.

`Action` cell — `Deprecated for skills: never ship one in a repo, migrate it to a skill`:
- "Deprecated for skills" → **holds** (`:5` "Custom prompts are deprecated. Use [skills] for reusable instructions"; `:8` "Custom prompts (deprecated)").
- "never ship one in a repo" → **holds** (`:10` "they're not shared through your repository"; an explicit-invocation file also cannot take repo-shared form per the same line).
- "migrate it to a skill" → **holds** (`:10` "If you want to share a prompt (or want Codex to implicitly invoke it), use skills" — the page's own migration direction).

## Entry "What a file sets" bullet (Codex, S090)

- "a Markdown file in the user folder only, not shared through the repository (`:10`)" → **holds** (`:10`, one line carries both halves).
- "`draftpr.md` is invoked as `/prompts:draftpr` (`:18,34`)" → **holds** (`:18` creates the file; `:34` shows the invocation; `:51` corroborates).
- "frontmatter `description` and `argument-hint` (`:40-41`)" → **holds** (`:40`,`:41`).
- "`$1`–`$9` and `$ARGUMENTS` placeholders (`:42`)" → **holds** (`:42`).

## Row-level cells

- Kind `docs`, tier `A`, status `mined`, opened `2026-10-23`, host `learn.chatgpt.com` (a pinned Codex host per the counter's HOSTS map) → consistent; no tracker/changelog URL pattern.
- Summary cell 8 → **holds**: user-local Markdown prompt files (`:10`), example slash-command invocation (`:34`,`:51`), YAML metadata + argument placeholders (`:40-44`), deprecated in favour of skills (`:5-8` — the page links the word "skills" to `build-skills`; "Agent Skills" is the summary's paraphrase, accurate in substance).

## Findings / defects

1. **Cosmetic anchor imprecision (not a fact defect):** SOURCES cell 7 anchors the create block as `:12-23`; the create-prompt block's fenced example actually runs to `:30`, so the range omits the prompt body (`:26-29`). Everything the cited lines must support is inside `:12-23`, so this is imprecise annotation, not a wrong claim.
2. **Cosmetic anchor imprecision:** "expected invocation (`:32-34`)" — the expected-invocation sentence is `:34` alone; `:32` is the restart step. Harmless, but the tighter anchor is `:34`.
3. No factual errors found. Byte count, sha256, HTTP status, quote bytes, line citations, and every fact in both SKILL.md cells and the entry bullet verify against the live page as fetched 2026-10-23T08:26:43Z.

## Not in scope / not verified here

- The `~/.codex/prompts/` rows at SKILL.md:86 (agent files) and :100 (plugin manifest) are other sections' Codex rows citing other sources; not attacked by this item.
- Verifier behaviour was read, not run (frozen counter; falsify seats do not re-run C1 — that is the integrator's seat).
- No tools installed or upgraded this session (curl, git, python3 already present); pacman untouched per bounds.

Report: .ufo/waves/round-58/falsify/ReopenS090.md
