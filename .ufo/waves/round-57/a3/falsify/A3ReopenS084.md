Result: MIXED — the live page matches S084's recorded sha256 and the Gate quote is a verbatim contiguous substring of `plugins.md:28`; the committed quote note is true but incomplete, and the candidate's S084 clause is the accurate one to land, tightened to the exact omitted bytes.

## Fetch (matches the row)

Command (exit 0), scratch `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS084/`:

```sh
date -u
curl -sS -D plugins.headers -o plugins.md -w 'http_code=%{http_code}\nsize_download=%{size_download}\nurl_effective=%{url_effective}\ncontent_type=%{content_type}\nredirect_url=%{redirect_url}\nnum_redirects=%{num_redirects}\n' --max-time 60 'https://cursor.com/docs/plugins.md'
wc -c plugins.md
sha256sum plugins.md
```

- `date -u`: `Fri 23 Oct 2026 06:45:41 AM UTC`
- HTTP/2 200; header `date: Fri, 23 Oct 2026 06:45:41 GMT`; `content-type: text/markdown; charset=utf-8`; `x-vercel-cache: MISS`; no `content-length` header
- final URL `https://cursor.com/docs/plugins.md` (`num_redirects=0`, empty `redirect_url`)
- `wc -c`: 20323; `sha256sum`: `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62`
- file is LF only (384 newlines, 0 CR, 384 lines)

Row at `07c33d73` `corpus/SOURCES.md` S084 records HTTP 200, 20,323 B, sha256 `74387ff95205965ca3060fac4d12966fea7b1525cc0e972e6f265bbee591cb62`, opened 2026-10-23T04:46:52Z. Equal, not merely the lesson's prefix `74387ff9…` (`corpus/lessons/round-57.md:19`). No tool installed.

## Gate quote: one line, contiguous, list marker left out

Lesson `## Gate` (`corpus/lessons/round-57.md:19`) and the entry quote cell (`corpus/knowledge/plugin-manifests-round57.md:29`) are the same 12-word string (backticks kept; splitting on whitespace after removing backticks still yields 12):

"plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and"

Fetched line 28, the only occurrence (byte offset 1967), verbatim:

`- **Cursor Plugins**: plugins with a `.cursor-plugin/plugin.json` manifest, which add rules, agents, commands, hooks, and [variables](https://cursor.com/docs/reference/plugins.md#variables)`

- Prefix not quoted, 20 bytes: `- **Cursor Plugins**: `
- Suffix not quoted, 71 bytes, one leading space: ` [variables](https://cursor.com/docs/reference/plugins.md#variables)`
- The quote's last word is `and`. The link's visible word `variables` is not in the quote.

Q42 kinds, against these bytes:

- Folded line breaks: no. The span is one line.
- Stripped markup: no character inside the span was deleted. The backticks around `.cursor-plugin/plugin.json` are in both the quote and the page. The bold markers and the link are outside the span, not stripped out of included text.
- Fence info string: no. The quote is not in a fence (the `text` fence for the Cursor Plugin tree is at the `### Cursor Plugin` sample, lines 284–295).
- List marker: yes, omitted. The line starts with `- `; that marker is not in the quote.

The lesson (`round-57.md:22-24`) calls S084 unshaped and discloses the omission in the same parenthesis. That matches landed Q42 (`corpus/QUALITY.md:53`), whose shaping list is folded lines, stripped markup, and a fence info string — not a list marker. It does not match the same paragraph's treatment of S082, which is not called unshaped for omitting the list number `2. `. The omission here is real and disclosed; the label "unshaped" is the part that is inconsistent with S082, not a mis-location of the bytes.

## Unshaped quote of the same manifest location

The manifest location this row counts is `.cursor-plugin/plugin.json` for a Cursor Plugin.

The whole of line 28 is 16 words with backticks removed and nothing else changed (`-`, `**Cursor`, `Plugins**:`, then the prose, then the link as one whitespace-delimited word). It is verbatim, so it folds nothing, strips nothing, and omits no list marker. It states the same location, and it names **Cursor Plugins**, which the landed substring does not. [INFERENCE] the counter would still find it: its page normalisation deletes `*` `_` and backticks on both sides, and this line has no `_`. This seat did not run the counter.

Two other single-line spans are not that statement:

- Line 208 whole line (7 words) starts at the path and has no `plugin`/`extension` word outside the token. The subject is the end of line 207. Joining them is the 7-word sentence "A Cursor Plugin has a `.cursor-plugin/plugin.json` manifest." The raw bytes are `A Cursor Plugin has a\n`.cursor-plugin/plugin.json` manifest.` — one folded line break, so it is shaped. The 17-word pair of sentences across `:207-208` ("An Agent Plugin has a `plugin.json` manifest at its root. A Cursor Plugin has a `.cursor-plugin/plugin.json` manifest.") is the same fold.
- Line 320, indent stripped (10 words): "for an Agent Plugin or `.cursor-plugin/plugin.json` for a Cursor Plugin." Unshaped, and it has `Plugin` outside the token, but the word `manifest` is not on the line (the list number `2. ` is on line 319). It names the path for a Cursor Plugin; it does not say the path is a manifest. Line 358 (8 words) starts at the path, so the only `plugin` is inside the token, and "For a Cursor Plugin, add a" is line 357.

Q42's replace-with-unshaped rule therefore has one real candidate, the entire line 28, and only if the omitted list marker counts as shaping that must be replaced. Landed Q42 does not list that omission, the lesson already calls the substring unshaped, and the candidate does not change the quote. This seat would keep the 12-word substring and name the bytes it leaves out. Do not switch the quote to the folded 7-word sentence.

## Which note is accurate

Committed entry clause (`plugin-manifests-round57.md:35-36`), true but not enough:

`S084 `plugins.md:28`, a contiguous substring (the list marker and bold label before it and the link after it are not quoted)`

It does not say the cut is on `and`, before the link word `variables`. A reader can think `variables` is inside the quote and only the URL was dropped. The lesson's parenthesis (`round-57.md:23-24`) has the same gap.

Candidate S084 clause in `.ufo/waves/round-57/a3/a2-candidate.patch` (the `plugin-manifests-round57.md` quote-locations hunk), checked against these bytes: accurate. The quote does end on `and`, and `variables` is not quoted. This seat did not re-check the other clients' clauses in that hunk, or the hunk's closing sentence about attempt-2 residual seats. The patch does not touch the lesson.

Same fetch, not the quote note: line 211 is `You can also develop either format from `~/.cursor/plugins/local`. See`, so the candidate's opening-paragraph citation of S084 `plugins.md:211` matches this page. The anchor cell's ranges also match the headings this fetch shows (`## What plugins contain` at line 7, body `:9-18`; `## The Agent Plugins standard` at line 20, body `:22-30` including the quote; `## Creating plugins` at line 253 through line 298).

## Exact text to land

Entry, old → new (S084 clause only):

- old: `S084 `plugins.md:28`, a contiguous substring (the list marker and bold label before it and the link after it are not quoted)`
- new: `S084 `plugins.md:28`, a contiguous substring from `plugins with` through `and` (12 words; no line break folded, no markup inside the span stripped, no fence info string); the bytes before it are `- **Cursor Plugins**: ` and the bytes after it are ` [variables](https://cursor.com/docs/reference/plugins.md#variables)` (the quote ends on `and`; the link's word `variables` is not quoted)`

Lesson `## Gate` quote notes, old → new (not in the candidate patch):

- old: `S084 is a contiguous substring: the list marker and bold label before it and the link after it are not quoted`
- new: `S084 is a contiguous substring of `plugins.md:28` from `plugins with` through `and`: the bytes before it are `- **Cursor Plugins**: ` and the bytes after it are ` [variables](https://cursor.com/docs/reference/plugins.md#variables)` (ends on `and`; `variables` is not quoted)`
