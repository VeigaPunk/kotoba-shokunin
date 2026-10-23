Result: DONE — The frozen live-page check returns `True` for the unshaped Cursor quote at `https://cursor.com/docs/reference/deeplinks.md`.

## Behavior
- Confirmed the W0 quote unchanged: 13 whitespace-separated words; the `.cursor/commands` token and `commands` outside it are both present. No bytes were stripped from the primary Markdown page.
- A direct call to the frozen counter’s `fetch(url)` and `found_on_page(page, quote, token)` returned `True` for the exact URL, quote, and token below.
- The SKILL row’s filename-to-slash-name wording is marked `[INFERENCE]`: Cursor’s changelog gives the `[command].md` filename pattern and `/` invocation, but does not expressly state that the basename becomes the slash name. The cited command summaries do not specify custom-command frontmatter or argument-placeholder syntax.

## Gates and provenance
- Read the frozen `verifiers/check_command_files.py` specification at `:1-223`. It requires a verbatim 6–25-word quote, the token and `command(s)`/`prompt(s)` outside the token, a new tier-A `docs`/`mined` source opened 2026-10-23, and a non-change-note URL. The quote below is 13 words and the direct deeplinks URL is on pinned host `cursor.com`; the Changelog is supplemental only, not the scored source URL.
- Sandbox clone command: `timeout 900 bash -lc 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r58/SrcCursor && git -C /fast/scratch/hyaku/kotoba-r58/SrcCursor checkout -q 3de87aad29e960c95ed35840442f424c48c29729'` — returned no output. The tool transcript did not expose an exit-code field.
- Counter proof, run with working directory `/fast/scratch/hyaku/kotoba-r58/SrcCursor`: `timeout 900s python3 -B -c 'from verifiers import check_command_files as c; url="https://cursor.com/docs/reference/deeplinks.md"; quote="Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory."; page=c.fetch(url); print(c.found_on_page(page, quote, ".cursor/commands"))'` — output: `True`; the tool returned normally (no explicit exit-code field).
- Primary-page fetch command: `timeout 900 bash -lc 'set -o pipefail; date -u; curl -sSL -o /fast/scratch/hyaku/kotoba-r58/SrcCursor/cursor-deeplinks.html -w "HTTP %{http_code}\\nURL %{url_effective}\\n" https://cursor.com/docs/reference/deeplinks.md; wc -c /fast/scratch/hyaku/kotoba-r58/SrcCursor/cursor-deeplinks.html; sha256sum /fast/scratch/hyaku/kotoba-r58/SrcCursor/cursor-deeplinks.html'`.
  - `date -u`: `Fri Oct 23 08:08:47 AM UTC 2026`.
  - HTTP 200; final URL `https://cursor.com/docs/reference/deeplinks.md`; 5,972 bytes; SHA-256 `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4`.
  - The fetched Markdown body has the quote at line 54; no bytes were stripped.
- Better-page check: fetching `https://cursor.com/docs/agent/chat/commands` redirected to `https://cursor.com/help/customization/skills#how-do-i-migrate-commands-to-skills` (HTTP 200, 181,908 bytes, SHA-256 `1fa1a626e791bb05f6b2a98e1d655d852913a8bb5b59de1f1dd170ade3001082`; `date -u` was `Fri Oct 23 08:08:47 AM UTC 2026`). This is a skills migration page, not a current command-file reference. `https://cursor.com/docs/customize-cursor.md` (HTTP 200, 5,200 bytes, SHA-256 `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e`; `date -u`: `Fri Oct 23 08:11:01 AM UTC 2026`) calls commands reusable Markdown prompts at line 31, but does not give the `.cursor/commands` path.
- Supplemental filename/invocation page: `https://cursor.com/changelog/1-6` (HTTP 200, 145,839 bytes, SHA-256 `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152`; `date -u`: `Fri Oct 23 08:10:18 AM UTC 2026`), line 2. Its rendered sentence was quoted after stripping HTML tags; this URL contains `changelog`, so it is not proposed as the counter’s source URL.
- `functions.grep` searched the fetched deeplinks page for `deprecated|deprecat|legacy|migrate|skills`: `No matches found`. The page itself does not mark `.cursor/commands` deprecated/legacy or point to a replacement. The newer command URL instead lands on the help page’s “How do I migrate commands to skills?” section: HTML line 35 says `/migrate-to-skills` converts eligible rules and commands; line 39 says it converts both user-level and workspace-level slash commands while preserving explicit invocation. The help page provides migration guidance, not an explicit deprecation/legacy label. It does not identify a user-level command-file path.

## Drafts (verbatim)

SOURCES row:

| S094 | Cursor Docs — Deeplinks — https://cursor.com/docs/reference/deeplinks.md | docs | A | Cursor's custom command directory and command-deeplink name/content model (vendor documentation; not runtime behavior) | § Commands (`deeplinks.md:52-54`); command-name/content parameters (`:67-74`); fetched 2026-10-23T08:08:47Z, HTTP 200, 5,972 B, sha256 `7ceb657892bdfa5d7a32f1168411fcaeb63c2f6ab41a5f0c45116a0a3f3a6bf4` (direct Markdown, no bytes stripped). Supporting page: https://cursor.com/docs/customize-cursor.md:31, fetched 2026-10-23T08:11:01Z (HTTP 200, 5,200 B, sha256 `9ae0878d97465512ad29459f5406538ec7b427dfbaa39e1cc95d3deb447f363e`); supplemental filename/invocation page: https://cursor.com/changelog/1-6:2, fetched 2026-10-23T08:10:18Z (HTTP 200, 145,839 B, sha256 `8d2a8bcfbbd6f0d6a7e76cc4535106d5384a471564ba98e6cbe166be6a8f5152`; HTML tags stripped for rendered quote; not the scored source URL) | Cursor documents custom commands defined in `.cursor/commands` and deeplink-created command names/content; supporting docs describe Markdown prompt files and a `[command].md` form; the cited command summaries specify no frontmatter or argument-placeholder schema | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md |

Entry row:

| Cursor | `.cursor/commands` | S094 | "Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory." |

SKILL.md row:

| Cursor | `.cursor/commands` (project/workspace; no user path documented) | Markdown prompt (“Commands are markdown files that define a focused workflow or action.” — `customize-cursor.md:31`). `[command].md` is used as `/command` [INFERENCE] from “Commands are stored in `.cursor/commands/[command].md`.” and Agent `/` dropdown (`changelog/1-6` HTML:2, tags stripped). No custom-command frontmatter or argument-placeholder schema documented in these pages (`deeplinks.md:52-54`; `customize-cursor.md:31`). | Prefer skills for new workflows; migrate commands with `/migrate-to-skills` |

Gate line:

- Cursor — https://cursor.com/docs/reference/deeplinks.md — accessed 2026-10-23 (`Fri Oct 23 08:08:47 AM UTC 2026`); line 54: “Command deeplinks allow you to share custom commands defined in your `.cursor/commands` directory.”

## Touched surfaces
- Wrote only `.ufo/waves/round-58/build/SrcCursor.md` in the lane. No product source, corpus, counter, lesson, or SKILL.md files were edited.
- Read-only source inputs: `verifiers/check_command_files.py:1-223`, `corpus/SOURCES.md:87-101`, and `.ufo/waves/round-58/w0/CensusCursor.md`.

## Out of scope
- No lane integration; the rows above are drafts for the L1.
- No full C1 counter run, other tests, tool installation/update, or subagent dispatch.

## Artifact paths
- Report: `.ufo/waves/round-58/build/SrcCursor.md`.
- Sandbox clone and fetched source bodies: `/fast/scratch/hyaku/kotoba-r58/SrcCursor/` (including `cursor-deeplinks.html`, `cursor-commands.html`, `cursor-customize.md`, and `cursor-changelog-1-6.html`).