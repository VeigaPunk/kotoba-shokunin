Result: DONE — Four routed cells have precise, source-grounded replacement text, and the sandbox counter still backs 7 of 7 clients.

## Finding and exact cell replacements

The source table was opened directly from base `f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c`. The base lines are unchanged between that commit and plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c0` (`git diff --exit-code f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c a10240c0940f770a5f2a5f32a7e3c363dd5d40c0 -- SKILL.md` → exit 0, no output). The same replacements below were applied only to the isolated sandbox copy of `SKILL.md` for the counter run; no lane product file was edited.

`SKILL.md:186` — Codex, “Past the threshold”

Old:
```text
Codex shortens skill descriptions first (its shipped parser also cuts each catalog description at 1,024 characters, `corpus/knowledge/frontmatter-rule-authorities-round48.md:51`), then for large skill sets may omit skills from the initial list and show a warning; selecting the skill still reads the full `SKILL.md`
```
New:
```text
At the initial-list budget, Codex shortens descriptions first; for large skill sets it may omit skills from the initial list with a warning; selecting a skill still reads the full `SKILL.md`.
```
Disposition: removed the unpinned shipped-parser cut claim. `frontmatter-rule-authorities-round48.md:51` explicitly says the CLI source was not pinned and “not tabled here because no source row pins that code.” The initial-list budget and documented behavior remain represented.

`SKILL.md:189` — Gemini CLI, “Documented threshold”

Old:
```text
~100 words of metadata (name + description) always in context per skill
```
New:
```text
No threshold: ~100 words is a size estimate for metadata (name + description), which is always in context.
```
Disposition: labels the estimate as no threshold while preserving the `100` token the frozen counter matches against the S057 quote.

`SKILL.md:189` — Gemini CLI, “Past the threshold”

Old:
```text
Nothing is cut: the full description is injected, so a longer one spends context tokens with no documented warning or truncation
```
New:
```text
The loader keeps `frontmatter.description` as-is (`skillLoader.ts:211`) and the prompt template inserts it directly (`snippets.ts:320`) at `google-gemini/gemini-cli@451a02ff`; no description cut appears in these steps, so longer descriptions spend context.
```
Disposition: the two source pointers were re-opened at the pinned commit; the revised statement is limited to what those load/render lines show.

`SKILL.md:190` — Cursor, “Action”

Old:
```text
Keep description at or under 1,024 characters; move detail into `references/` rather than the body
```
New:
```text
Keep `description` at or under 1,024 characters; an over-limit skill still loads and gets a yellow warning in `/skills`.
```
Disposition: removed the unsupported `references/` advice; the replacement follows the reopened S058 release-note warning behavior. `cursor.com/docs/skills.md` was not cited or opened.

Every changed base row remains a single physical line. The measured threshold numbers remain present: `~100` for Gemini, and unchanged threshold cells for Codex, Cursor, and the other clients.

## Reopened source evidence

All five URLs were fetched with ordinary `curl` (no browser), saved under `/fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/`, and hashed. Each exact `date -u` line below is copied from its fetch command.

- S057 Gemini docs: `https://geminicli.com/docs/cli/skills-best-practices.md`; date line `Thu Oct 22 11:13:02 PM UTC 2026`; HTTP 200; 3,257 bytes; SHA-256 `612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3`; fetched bytes `sources/gemini-best-practices.md`. Quote at line 24 (markdown retained): `**Metadata (name + description)**: Always in context (~100 words).`
  Command: `timeout 900s bash -lc 'date -u; curl -sSL --max-time 120 -o /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-best-practices.md -w "HTTP %{http_code}; bytes %{size_download}\n" https://geminicli.com/docs/cli/skills-best-practices.md; sha256sum /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-best-practices.md'`
- S054 Codex docs: `https://learn.chatgpt.com/docs/build-skills.md`; date line `Thu Oct 22 11:13:02 PM UTC 2026`; HTTP 200; 11,035 bytes; SHA-256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`; fetched bytes `sources/codex-build-skills.md`. Quotes: line 38, `this list uses at most 2% of the model's`; line 39, `context window, or 8,000 characters when the context window is unknown.`; line 40, `If many skills are installed, Codex shortens skill descriptions first.`; line 41, `For large skill sets, Codex may omit some skills from the initial list and show a warning.`; line 46, `When Codex selects a skill, it still reads the full SKILL.md instructions.`
  Command: `timeout 900s bash -lc 'date -u; curl -sSL --max-time 120 -o /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/codex-build-skills.md -w "HTTP %{http_code}; bytes %{size_download}\n" https://learn.chatgpt.com/docs/build-skills.md; sha256sum /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/codex-build-skills.md'`
- S058 Cursor release notes: `https://cursor.com/docs/release-notes.md`; date line `Thu Oct 22 11:13:02 PM UTC 2026`; HTTP 200; 301,193 bytes; SHA-256 `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd`; fetched bytes `sources/cursor-release-notes.md`. Quotes at line 122: `Skills that load but exceed the spec's limits now show a yellow warning count in `/skills`` and `a description over 1,024 characters`.
  Command: `timeout 900s bash -lc 'date -u; curl -sSL --max-time 120 -o /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/cursor-release-notes.md -w "HTTP %{http_code}; bytes %{size_download}\n" https://cursor.com/docs/release-notes.md; sha256sum /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/cursor-release-notes.md'`
- Gemini loader: `https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/packages/core/src/skills/skillLoader.ts`; date line `Thu Oct 22 11:13:02 PM UTC 2026`; HTTP 200; 6,560 bytes; SHA-256 `8bce3215263e9ec06f32a865715c04af6deb4b6299db1490665f53972d4326f9`; fetched bytes `sources/gemini-skillLoader.ts`. Quote at line 211: `description: frontmatter.description,`
  Command: `timeout 900s bash -lc 'date -u; curl -sSL --max-time 120 -o /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-skillLoader.ts -w "HTTP %{http_code}; bytes %{size_download}\n" https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/packages/core/src/skills/skillLoader.ts; sha256sum /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-skillLoader.ts'`
- Gemini prompt renderer: `https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/packages/core/src/prompts/snippets.ts`; date line `Thu Oct 22 11:13:02 PM UTC 2026`; HTTP 200; 70,505 bytes; SHA-256 `b2cccbd0cf68e33d057f33938e457fe3c781cc7e65c593f7a3974d70c5c68fe7`; fetched bytes `sources/gemini-snippets.ts`. Quote at line 320: `<description>${skill.description}</description>`
  Command: `timeout 900s bash -lc 'date -u; curl -sSL --max-time 120 -o /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-snippets.ts -w "HTTP %{http_code}; bytes %{size_download}\n" https://raw.githubusercontent.com/google-gemini/gemini-cli/451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1/packages/core/src/prompts/snippets.ts; sha256sum /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/gemini-snippets.ts'`

## Gate and limits

Command run after applying the four cell replacements in the isolated clone at `/fast/scratch/hyaku/kotoba-r55/ScribeC1Cells`:

```text
timeout 900s bash -lc 'date -u; python3 -B verifiers/check_description_thresholds.py --root /fast/scratch/hyaku/kotoba-r55/ScribeC1Cells'
```

Date line: `Thu Oct 22 11:13:57 PM UTC 2026`. Exit 0. Output:

```text
Claude Code  BACKED 
Codex        BACKED 
VS Code      BACKED 
Copilot CLI  BACKED 
Gemini CLI   BACKED 
Cursor       BACKED 
opencode     BACKED 
description thresholds backed 7 of 7 clients
```

This was the requested `--root` run, not `--fetch`. The counter docstring (`verifiers/check_description_thresholds.py:46-57`) says it does not judge whether a number is a render cut, budget, or authoring maximum; 7/7 is mechanical counter evidence, not a semantic verdict or live-page check. The separate source fetches above are the source reopen evidence. No client CLI, browser, install, or source-tree mutation was used.

## Surfaces and artifacts

- Lane file written: `.ufo/waves/round-55/build/ScribeC1Cells.md` (this report only).
- Sandbox-only modified file: `/fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/SKILL.md`; the frozen counter and other lane files were not changed.
- Base excerpt: `/fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/SKILL-f0e5de82.md`.
- Reopened source artifacts: the five `sources/*` files listed above in the sandbox clone.
- Out of scope: no edits to lane `SKILL.md`, the round-54 entry or lesson, `SOURCES.md`, either counter, or any verifier. No `cursor.com/docs/skills.md` citation was needed because the unsupported `references/` instruction was dropped.
