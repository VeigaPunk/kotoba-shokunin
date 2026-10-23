Result: MIXED — the live page matches S082's recorded hash and the Gate quote is line 27 with only the list marker `2. ` removed, but that quote is shaped even though the same 17-word line is an unshaped quote of the same location. The candidate's S082 clause is the accurate note; the committed clause omits `:27`.

## Fetch vs row

Row at `07c33d73ddce769d9cea2846a6313164401b5478` (`corpus/SOURCES.md` S082; working tree clean for this file; `git --no-optional-locks rev-parse HEAD` printed that hash):

- URL: `https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md`
- Recorded: 2026-10-23T04:47:14Z, HTTP 200, 7,711 B, sha256 `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64`

Re-fetch (scratch `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS082/plugins-creating.md`; no lane git write; no tool installed):

```sh
date -u
# Fri Oct 23 06:45:37 AM UTC 2026
timeout 120 curl -sS -L --max-time 60 -D headers.txt -o plugins-creating.md \
  -w 'http_code=%{http_code}\nsize_download=%{size_download}\nurl_effective=%{url_effective}\nnum_redirects=%{num_redirects}\ncontent_type=%{content_type}\n' \
  'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating.md'
date -u
# Fri Oct 23 06:45:38 AM UTC 2026
wc -c plugins-creating.md
sha256sum plugins-creating.md
```

Observed: `http_code=200`, `size_download=7711`, `num_redirects=0`, `content_type=text/markdown; charset=utf-8`, effective URL unchanged. Response header `date: Fri, 23 Oct 2026 06:45:38 GMT`, `content-length: 7711`. `wc -c` printed `7711`. sha256 `c0642867c28a816b5a1210a3f51d66efd2f37cd09ae950228a3c517cf5cb7d64`. Byte-identical to the row. 187 lines.

## Gate quote in the fetched bytes

Lesson Gate (`corpus/lessons/round-57.md:17`) quote, 16 whitespace-separated words:

`Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.`

Location column on that row: `plugins-creating.md:27`. Lesson quote-note (`round-57.md:24`): "S082 omits the list number `2. ` before it".

Fetched line 27, verbatim (`repr` of the line):

`2. Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.`

Python check on the fetched bytes: the quote occurs once; `line[3:]` equals the Gate quote; the three omitted bytes are `2. ` (`0x32 0x2e 0x20`). The backticks around `plugin.json` and the final period are kept. Not a folded line break. Not a fence info string. Shaped only by dropping the ordered-list marker. 17 words with the marker, 16 without. The lesson location `:27` and the lesson's "omits the list number" sentence are both true of these bytes.

## Unshaped quote of the same location

Yes. The whole of line 27 is one line, 17 words (≤25), and states the same manifest location (`plugin.json` at the root of the directory) with no bytes removed. Q42 (`corpus/QUALITY.md:53`) says a quote that needs shaping (folded lines, stripped markup, a fence info string) is replaced by an unshaped quote from the same page when one exists. This one does not need shaping: dropping the list marker is optional. The assignment's shaping list includes a list marker, so the landed quote is shaped.

A second unshaped sentence on line 14 (10 words) is not the same statement: "Agent Plugins 1.0 requires the manifest at the plugin root." It names the plugin root and not `plugin.json` (that token is in the previous sentence on the line), and the next sentence says legacy plugins support additional locations. No other line pairs `plugin.json` with the directory root inside 25 words.

## Which note is accurate

Committed note (`corpus/knowledge/plugin-manifests-round57.md:33-34`), the quote as it stands:

`S082` / `` `plugins-creating.md` step 2 (the list number `2. ` is not quoted) ``

True about the omitted bytes and about step 2. Incomplete: it is the only clause in that paragraph with no line number, and the bytes plus the lesson location column both fix the quote on line 27. Step 2's body continues through the examples (lines 29–65); without `:27` "step 2" is wider than the quote.

Candidate replacement (claim in `.ufo/waves/round-57/a3/a2-candidate.patch`, verified here, not taken as evidence), S082 clause only:

`` S082 `plugins-creating.md:27`, step 2 (the list number `2. ` is not quoted) ``

Accurate against the fetched bytes. The rest of that hunk (other rows, and "Re-derived against live bytes by the round-57 attempt-2 residual seats") was not checked.

Text to land for the quote as committed, S082 clause only (old → new):

```
S082
`plugins-creating.md` step 2 (the list number `2. ` is not quoted);
```

```
S082 `plugins-creating.md:27`, step 2 (the list number `2. ` is not quoted);
```

If the L1 applies Q42 and replaces the shaped quote, that note becomes false and the quote text changes instead. Old → new, in both `corpus/lessons/round-57.md:17` and `corpus/knowledge/plugin-manifests-round57.md:27`:

```
Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.
```

```
2. Choose a plugin format, then add a `plugin.json` manifest file to the root of the directory.
```

Then the location note to land is `` S082 `plugins-creating.md:27` (one line, unshaped) ``, and `corpus/lessons/round-57.md:22-24` drops "S082 omits the list number `2. ` before it" and lists S082 with the unshaped one-line rows. This seat does not edit those files.

## Confidence

High on the hash match, on line 27, and on the three omitted bytes. High that the candidate's S082 clause is the accurate description of the quote as committed. The Q42 replacement is a rule application, not a second reading of the bytes. No tool installed.
