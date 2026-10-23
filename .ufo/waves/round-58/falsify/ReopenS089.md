Result: DONE — S089 re-opened byte-identical (HTTP 200, 114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`); every fact in the Claude Code cells holds against the page at the stated lines except one wrong section name in the SOURCES anchor cell, and one entry Limits sentence that omits S089's own precedence statement.

Scope: SOURCES row S089 (`corpus/SOURCES.md:102`), SKILL.md `§ Custom command files by client` Claude Code row (`SKILL.md:113`), and the entry `corpus/knowledge/command-files-round58.md` (`:15-16,:31-34,:35,:44-45,:63-64`) — checked at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe` via `git --no-optional-locks show` and against the working copy (identical rows at both; see note below). Page line numbers (`:NNN`) are lines of the bytes fetched below.

## Re-open

- `date -u` → `Fri 23 Oct 2026 08:29:22 AM UTC`
- `curl -sSL -w 'HTTP %{http_code} bytes %{size_download}\n' -o slash-commands.md https://code.claude.com/docs/en/slash-commands.md` → `HTTP 200 bytes 114542`, curl exit 0
- `wc -c` → `114542`; `sha256sum` → `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd`
- Row claims (`corpus/SOURCES.md:102`): fetched 2026-10-23T08:08:35Z, HTTP 200, 114,542 B, same sha256 — **holds**, byte-identical re-open ~21 min later. Lesson Gate (`corpus/lessons/round-58.md` § Gate) carries the same record and quote.
- Scratch copy: `/fast/scratch/hyaku/kotoba-r58/ReopenS089/slash-commands.md`.

## Entry quote verbatim at the stated line (Q42)

- `grep -F -c '"**Command files**: a Markdown file in `.claude/commands/` is the older format and still works."'` on the fetched bytes → match at line 172, count 1. The line begins `* **Command files**: a Markdown file in \`.claude/commands/\` is the older format and still works. It supports the same [frontmatter](#frontmatter-reference) except \`name\` and \`paths\`...`. The quoted span is byte-exact; only the leading `* ` list marker and the line's continuation fall outside the span. **Holds.**
- Q42 verdict: at `46b4a706` the note (entry `:28`) said only "every quote is copied from the fetched bytes" and named shaping for VS Code only — it did not name Claude Code's dropped `* ` marker. That was an incomplete note under Q42 (bytes adjacent to the span are dropped and were unnamed). The falsify wave has already corrected it: the working copy (entry `:31-32`, seats `ReviewEntry`, `CriticVSCodeQuote`, `ReopenS091`) now reads "Claude Code drops the line's leading `* ` list marker." — accurate per my byte check. Nothing further to change for S089.

## Per-fact verification against the page

`corpus/SOURCES.md:102`:

1. URL opens, HTTP 200, 114,542 B, sha256 `6b070e87…` — **holds** (row matches my re-open; `:102` anchor cell).
2. Title "Extend Claude with skills" — **holds**: H1 `# Extend Claude with skills` at `:5`; "(custom command files)" is the lane's scope annotation.
3. Anchor "§ Where skills live (`slash-commands.md:172`)" — **wrong** (heading name): no heading `Where skills live` exists in the fetched bytes (`grep -c 'Where skills live'` → 0 headings; the only matches are lowercase link anchors `#where-skills-live` at `:73,:283,:378`). The heading of the section containing `:172` is `## Choose where skills load` at `:152`. The line number `:172` itself is correct. Smallest correction: rename the anchor to "§ Choose where skills load (`slash-commands.md:172`)".
4. Anchor "§ Frontmatter reference (`:378,402-403`)" — **holds**: heading `### Frontmatter reference` at `:376`; cited facts at `:378,:402,:403`.
5. Anchor "§ How a skill gets its command name (`:450-451`)" — **holds**: heading `#### How a skill gets its command name` at `:439`; cited facts at `:450-451`.
6. Scope cell ".claude/commands/ Markdown files, supported frontmatter and arguments, file-name-to-command mapping" — **holds** (:172, `:378,:402-403`, `:450-451` respectively).
7. Teaches cell "still-working older-format files; accept skill frontmatter except `name` and `paths`; map file names to slash commands; argument hints and named positional arguments" — **holds** (:172, :378, :450, :402-403).
8. `status` mined / `opened` 2026-10-23 / `recheck` 90d / `used-by` `corpus/knowledge/command-files-round58.md` — **holds** (consistent with the wave; today's bytes re-opened this round).

`SKILL.md:113` (Client = Claude Code):

9. Command files cell `.claude/commands/` — **holds**: named at `:172,:378,:450`.
10. `(project)` qualifier — **holds as annotation**: the page names only the relative folder; `~/\.claude/commands` has zero matches in the fetched bytes, so the page documents no user-level commands folder. The "(project)" label is consistent with the page's own Personal `~/.claude/skills/` vs Project `.claude/skills/` split (`:157-158`), not page-stated verbatim for commands.
11. `Markdown` — **holds**: `:172` "a Markdown file in `.claude/commands/`".
12. `deploy.md` → `/deploy` — **holds**: `:450` "`.claude/commands/deploy.md` → `/deploy`".
13. `skill frontmatter except `name` and `paths`` — **holds**: `:378` "A command file … accepts the same fields except `name` and `paths`" (also `:172` "supports the same frontmatter except `name` and `paths`").
14. `argument-hint` — **holds**: `:402` field row "Hint shown during autocomplete to indicate expected arguments."
15. `named `arguments` for `$name`` — **holds**: `:403` "Named positional arguments for `$name` substitution … Accepts a space-separated string or a YAML list. Names map to argument positions in order."
16. Cited line refs `:172,378,402-403,450` — **holds**: every ref lands on the fact it supports.
17. Action "Audit it like a skill" — **holds**: `:378` same-fields sentence + `:17` "both create `/deploy` and work the same way".
18. Action "the page calls it the older format" — **holds**: `:172` "is the older format" verbatim.
19. Action "author new work as a skill" — **holds**: `:172` "Prefer a skill for new work".

`corpus/knowledge/command-files-round58.md`:

20. Lead `:15-16` "Claude Code calls `.claude/commands/` files "the older format" that "still works" (S089 `:172`)" — **holds**: both phrases verbatim at `:172`.
21. Quote row `:35` — **holds**: byte-exact span at `:172` (grep -F, above).
22. What-a-file-sets bullet `:44-45` "a Markdown file" — **holds**: `:172`.
23. "`deploy.md` becomes `/deploy` (`:450`)" — **holds**: `:450`.
24. "the same frontmatter as a skill except `name` and `paths` (`:378`)" — **holds**: `:378` (and `:172`).
25. "`argument-hint` and named positional `arguments` for `$name` substitution (`:402-403`)" — **holds**: `:402-403`.

## Findings

- **F1 (minor — locator accuracy):** `corpus/SOURCES.md:102` anchor "§ Where skills live" names no heading in the fetched bytes; the containing section is `## Choose where skills load` (`slash-commands.md:152`). The wrong name was imported from the page's own stale `#where-skills-live` link anchors (`:73,:283,:378`). Line `:172` is right; only the section label is wrong.
- **F2 (minor — entry completeness):** `corpus/knowledge/command-files-round58.md:63-64` says command/skill precedence "is recorded only where a page states it (Copilot CLI, S028 `:456`)". S089's own page states the same precedence at `slash-commands.md:214` — `| A skill and a file in `.claude/commands/` | The skill |` under `### Resolve skills that share a name` (`:205`). No Claude Code cell asserts otherwise, so nothing is false; but the parenthetical reads as if S028 were the only stating page, and the entry records no Claude Code precedence though its own source gives one (which independently corroborates the Copilot CLI row's "skills override commands"). Smallest correction: extend the parenthetical, e.g. "(Copilot CLI, S028 `:456`; Claude Code, S089 `slash-commands.md:214` — a skill wins over a same-named command file)".

## Residual risk / adjacent observations (outside the named cells; routed, not my per-fact list)

- `SKILL.md:109` preamble absolute "the model never picks it from a description" is not supported by S089 for Claude Code: `:17` says command files and skills "work the same way"; `:378` grants command files every skill field except `name`/`paths` — including `description` and `when_to_use`, which `:400` says Claude uses "to decide when to apply the skill"; `:73-74` (`### Run your checks before each commit`) let a `.claude/commands/` file count as a project skill that "Claude can invoke"; `:404` lists `disable-model-invocation` as accepted frontmatter for such files. The page is self-tensioned (the same `:17` calls invocation control a skill add-on), so the absolute should not rest on S089 [INFERENCE about the preamble only — the Claude Code cells themselves are consistent].
- S065 (`corpus/SOURCES.md:78`) cites `https://code.claude.com/docs/en/skills.md` (fetched 2026-10-22T23:12:23Z, 112,748 B, sha `909dd50a…`) and its own cell notes "the `slash-commands.md` route served the same bytes" then. My 114,542 B / `6b070e87…` fetch differs from S065's recorded bytes — the document moved upstream between fetches. Whether S089's admission stands as same-authority re-open vs new source is `CriticS089Alias`'s item; this is the byte evidence.
- Revision note: the working copy is under live integration. I confirmed `SKILL.md:113`, `corpus/SOURCES.md:102`, entry `:35,:44,:63` identical at `46b4a706` and working copy; entry `:31-34` (Quote notes) already differs — the corrected text is itself accurate per my byte check.
- No user-level commands folder exists on the page (`~/\.claude/commands` zero matches); if a reader needs runtime scope, "(project)" only documents what this page documents — the SOURCES scope cell already limits the row to "vendor documentation; not a runtime test".

## Verification gaps

- I did not re-run the counter; `--fetch` verdict and `held-at-base` belong to `RerunC1Counter`.
- I did not check S065's cited lines on today's bytes (the page is now 114,542 B vs S065's 112,748 B); not my row.
- Tools: none installed or updated.

Report: `.ufo/waves/round-58/falsify/ReopenS089.md`
