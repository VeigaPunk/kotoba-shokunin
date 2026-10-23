Result: DONE — Re-opened the S089 source, confirmed the heading mismatch, and identified the only SOURCES-contract-compliant correction form.

# Round 59 routed R4 — S089 anchor

## Re-open evidence

Re-opened `https://code.claude.com/docs/en/slash-commands.md` using ordinary `curl` (no browser or access-control bypass).

Command:

```sh
timeout 30s bash -c 'set -eu; date -u; mkdir -p /fast/scratch/hyaku/kotoba-r59/ScribeR4Note; curl -sS -L --max-time 20 -D /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.headers -o /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md -w "HTTP_STATUS=%{http_code}\nBYTES=%{size_download}\nURL=%{url_effective}\n" https://code.claude.com/docs/en/slash-commands.md; sha256sum /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md; wc -c /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md'
```

Exit: 0 (command completed and emitted all post-fetch measurements).

Observed output:

```text
Fri Oct 23 09:34:33 AM UTC 2026
HTTP_STATUS=200
BYTES=114542
URL=https://code.claude.com/docs/en/slash-commands.md
6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd  /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md
114542 /fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md
```

`grep` over the fetched bytes found `152:## Choose where skills load`; the `read` view confirms the heading at line 152. Line 172 is the `Command files` bullet under that section, not a heading. Thus the current S089 anchor at `corpus/SOURCES.md:102`, `§ Where skills live (slash-commands.md:172)`, has both a mismatched heading label and a locator that points at the bullet rather than the heading. The direct command-file evidence at line 172 remains useful and can be named separately. The fetched bytes' SHA-256 is identical to the value currently recorded in S089.

## Contract and correction draft

`/home/vgpnk/Projects/shokunin/CORPUS.md:112-118` says a row is written after opening the source; only `status`, `recheck`, and `used-by` may change in place, with each such change logged old→new; a correction is a new row whose `teaches` opens `supersedes S0NN —`. Therefore the allowed form is an appended correction row. Editing S089's `anchor` cell in place is not allowed by this contract.

After the round-59 assigned IDs S096–S101 and reserved S102, append the following as S103 at the end of the SOURCES Registry. This draft assumes the existing knowledge caller is migrated from S089 to S103; that caller currently names S089 at `corpus/knowledge/command-files-round58.md:2`.

```markdown
| S103 | Claude Code Docs — Extend Claude with skills (custom command files; S089 anchor correction) — https://code.claude.com/docs/en/slash-commands.md | docs | A | Claude Code `.claude/commands/` Markdown files, supported frontmatter and arguments, and file-name-to-command mapping (vendor documentation; not a runtime test) | § Choose where skills load (`slash-commands.md:152`); Command files bullet (`:172`); § Frontmatter reference (`:378,402-403`); § How a skill gets its command name (`:450-451`); fetched 2026-10-23T09:34:33Z, HTTP 200, 114,542 B, sha256 `6b070e872dea28905a7ea7f45c4d5960f5bdf28cc73ac808799af6d50435ffbd` (R4 re-open) | supersedes S089 — Claude Code documents `.claude/commands/` Markdown command files as still-working older-format files; they accept skill frontmatter except `name` and `paths`, map file names to slash commands, and document argument hints and named positional arguments | mined | 2026-10-23 | 90d | corpus/knowledge/command-files-round58.md, corpus/lessons/round-59.md |
```

The paired knowledge-frontmatter migration makes the proposed S103 `used-by` accurate. In the round-59 lesson `## Gate`, record the S103 URL, access date/time, and the byte-exact quote `Choose where skills load` (5 words; `slash-commands.md:152`), as required by the contract's Rule 1.

For `## Rows touched (old → new)`: do **not** add an S089 anchor-cell old→new line for this allowed correction-row form; S089 stays unchanged and S103 is appended. The hypothetical in-place line would be `S089 anchor: § Where skills live (slash-commands.md:172) → § Choose where skills load (slash-commands.md:152)`, but that describes a contract-forbidden edit and must not be recorded as the fix. Round-58's existing lesson demonstrates the heading style at `corpus/lessons/round-58.md:36-41`.

## Surfaces, gates, and scope

- Behavior: no product or corpus behavior was changed; this is a source re-open and correction draft.
- Gates: no verifier, counter, test, or build was run. No tool was installed or updated.
- Lane writes: only this report. Fetched page bytes and response headers are in the seat scratch directory listed below.
- Out of scope: no edit to `SOURCES.md`, `command-files-round58.md`, or any lesson; no counter or other route work; no subagents.

## Artifacts

- Report: `.ufo/waves/round-59/build/ScribeR4Note.md`
- Fetched source: `/fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.md`
- Response headers: `/fast/scratch/hyaku/kotoba-r59/ScribeR4Note/slash-commands.headers`
