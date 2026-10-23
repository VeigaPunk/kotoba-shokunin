Result: HOLDS — live S085 bytes match the recorded sha256, and the Gate quote is a verbatim 11-word prefix of `index.mdx:21`; the candidate does not correct that clause.

## Fetch

- URL (SOURCES S085 at `07c33d73ddce769d9cea2846a6313164401b5478`): `https://raw.githubusercontent.com/anomalyco/opencode/bdf757209ff742b8551a4874347edb845241e5bb/services/www/src/docs/content/build/plugins/index.mdx`
- `date -u` (before and after the same curl): `Fri 23 Oct 2026 06:45:40 AM UTC`
- HTTP status: 200 (`content-length: 60780`; `content-type: text/plain; charset=utf-8`)
- Byte count: 60780 (`wc -c` and curl `size_download`)
- sha256: `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5`
- Row records the same hash and size: fetched 2026-10-23T04:51:25Z (HTTP 200, 60,780 B, sha256 `e505931a59faa9a6685be195ccf42fcd8e3ddb9bb1d9e52f95d3b6c862cb83a5`). Match. Bytes saved at `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS085/index.mdx`.
- No tools installed.

## Gate quote in the fetched bytes

Lesson `corpus/lessons/round-57.md:20` (commit `07c33d73`, working tree clean against that commit for this file):

"Plugins under `.opencode/plugins/` are loaded automatically, like the local example above."

at `index.mdx:21`.

Fetched line 21, byte-exact (`repr` confirms ASCII, offset 0):

`Plugins under `.opencode/plugins/` are loaded automatically, like the local example above. To load published packages`

The recorded quote is that line's first sentence, including the period. The next bytes are a space and `To load published packages` (the second sentence continues on line 22). 11 words. Not shaped under Q42: no folded line break, no stripped markup (the backticks around `.opencode/plugins/` stay in the quote), no fence info string, no list marker. The fence opener is a different line (`index.mdx:10`, `` ```ts title=".opencode/plugins/example/index.ts" ``) and is not part of the quote.

The same page has no other prose sentence that states `.opencode/plugins/`. The only other hit is that fence title, which names an example file, not the load folder. The recorded quote is already the unshaped ≤25-word statement of the manifest location. Q42 does not require a replacement quote.

Lesson quote note (`round-57.md:22-23`) calls S085 "one line" and "unshaped". Unshaped holds. "One line" holds only as "does not cross a line break": the quote is not the whole of line 21. The parenthetical substring carve-out on that note is only for S084.

Timestamp side mismatch, not a byte mismatch: the Gate opened column for this URL is `2026-10-23T04:47:59Z` (`round-57.md:20`), which is the SOURCES sibling-page time, not the index fetch time `2026-10-23T04:51:25Z`. Size and sha on the Gate row still match this page.

## Quote-location notes

Tip entry, `corpus/knowledge/plugin-manifests-round57.md:36` (same commit): `S085 `index.mdx:21`.`

Candidate replacement (`.ufo/waves/round-57/a3/a2-candidate.patch:88-90`, untrusted): the S085 clause is the same `S085 `index.mdx:21`.` The patch then appends, to the whole paragraph, `Re-derived against live bytes by the round-57 attempt-2 residual seats (`.ufo/waves/round-57/attempt2/residual/`).` That sentence is not a fact about these bytes. I did not open those residual reports and do not treat them as evidence.

Both notes are accurate as a line pointer. Neither is more accurate for S085. The candidate names a sentence cut for other rows (S079 "first of two sentences") and does not do so for S085, which has the same shape. I would not land the residual trailer.

## Text to land

Old (`plugin-manifests-round57.md:36`, S085 clause only):

`S085 `index.mdx:21`.`

New:

`S085 `index.mdx:21`, the first sentence of the line (verbatim; the remainder "To load published packages" is not quoted).`

Leave the lesson quote text unchanged. Do not append the candidate's residual-seats sentence.