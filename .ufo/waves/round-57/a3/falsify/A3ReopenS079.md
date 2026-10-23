Result: MIXED — the S079 hash and Gate quote hold as an unshaped 9-word prefix of line 34; the tip note omits that cut, and the candidate's "two sentences" is false (the line has three).

Seat: A3ReopenS079. Revision read: `07c33d73ddce769d9cea2846a6313164401b5478` (`git --no-optional-locks rev-parse HEAD` printed that hash; `git --no-optional-locks diff --stat 07c33d73 -- corpus/SOURCES.md corpus/lessons/round-57.md corpus/knowledge/plugin-manifests-round57.md` printed nothing). No tools installed. No sandbox clone (read and one curl only).

## Fetch

Command (scratch `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS079/`, exit 0):

```
date -u
timeout 120 curl -fsSL -D headers.txt -o plugins-reference.md -w 'http_code=%{http_code} size_download=%{size_download} url_effective=%{url_effective}\n' 'https://code.claude.com/docs/en/plugins-reference.md'
wc -c plugins-reference.md
sha256sum plugins-reference.md
```

Observed:

```
Fri 23 Oct 2026 06:45:43 AM UTC
http_code=200 size_download=42124 url_effective=https://code.claude.com/docs/en/plugins-reference.md
42124 plugins-reference.md
f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e
```

Response header `date: Fri, 23 Oct 2026 06:45:43 GMT`, `content-type: text/markdown; charset=utf-8`, `HTTP/2 200`. Body has no CR bytes; 698 lines plus a trailing newline.

Row at `corpus/SOURCES.md` (S079, committed): HTTP 200, 42,124 B, sha256 `f2910dd6020f5448e5d8c9a8c3b5af7b31b7222d247c20b25f44a712b805916e`, opened 2026-10-23T04:46:45Z. Byte count and sha256 match this fetch. The URL is `https://code.claude.com/docs/en/plugins-reference.md`.

## Gate quote

Lesson `corpus/lessons/round-57.md:14` (§ Gate):

"Save the manifest at `.claude-plugin/plugin.json` under the plugin root."

Location claimed: `plugins-reference.md:34`.

Fetched line 34 (byte offset 2233, length 202, 27 words) is exactly:

Save the manifest at `.claude-plugin/plugin.json` under the plugin root. Put every other plugin file at the plugin root, not inside `.claude-plugin/`. That includes `skills/`, `commands/`, and `hooks/`.

The Gate quote is bytes 2233–2304 (72 bytes), a prefix of that line, including the backticks and the period. The next bytes are ` Put every other plu`. It occurs once (`text.count` = 1). Backtick-aware split on `.` outside backticks gives three sentences:

1. (9 words) Save the manifest at `.claude-plugin/plugin.json` under the plugin root.
2. (12 words) Put every other plugin file at the plugin root, not inside `.claude-plugin/`.
3. (6 words) That includes `skills/`, `commands/`, and `hooks/`.

Shaping (Q42, `corpus/QUALITY.md:53`, plus the list-marker case the lesson already names for S082): none inside the quoted span. No folded line break, no stripped markup (the backticks stay), no fence info string, no list marker. The span is unshaped. It is not the whole line.

An unshaped quote of ≤25 words on this page does state the same manifest location: the Gate quote itself (9 words). Q42 does not require replacing it. The whole line is 27 words, so it cannot be the ≤25-word quote.

Two other statements of the same place, neither a better replacement:

- Line 9, first sentence, 12 words, also a cut from a longer line (43 words, three sentences): "A plugin manifest is the `plugin.json` file in a plugin's `.claude-plugin/` directory." It does not contain the joined token `.claude-plugin/plugin.json`.
- Line 617 is a table row, not prose: `| Manifest | `.claude-plugin/plugin.json` | Plugin metadata and configuration. Optional |`. Dropping the pipes would be stripped markup. The joined path appears only on lines 34 and 617.

## Which note is accurate

Tip, `corpus/knowledge/plugin-manifests-round57.md:32` (§ Quote locations):

`S079 `plugins-reference.md:34`;`

Accurate on the line and on the unshaped class. Incomplete: it does not say the quote is only the first sentence. The lesson at `corpus/lessons/round-57.md:22-23` says S079 is "one line" and "unshaped", which is true of the span, and discloses the substring cut for S084 but not for S079.

Candidate (untrusted `.ufo/waves/round-57/a3/a2-candidate.patch` lines 82–83), S079 clause only:

`S079 `plugins-reference.md:34`, the first of two sentences on the line;`

Not accurate. Line 34 has three sentences, not two. Do not land that clause.

Text to land, S079 clause only (leave S080–S085 to their seats):

old: `S079 `plugins-reference.md:34`;`

new: `S079 `plugins-reference.md:34`, the first sentence of a three-sentence line (the bytes after the first period are not quoted);`

Lesson insertion, same fact, inside the existing parenthesis at `corpus/lessons/round-57.md:23` (do not otherwise rewrite that sentence):

old: `unshaped (S084 is a contiguous substring:`

new: `unshaped (S079 is the first of three sentences on `plugins-reference.md:34`, and the bytes after the first period are not quoted; S084 is a contiguous substring:`
