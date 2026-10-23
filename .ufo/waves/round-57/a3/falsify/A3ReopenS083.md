Result: MIXED — the live page matches S083's recorded sha256 and the Gate quote is the second sentence of lines 106–107 with one folded line break; the committed quote note does not say the quote starts mid-line, and the candidate's S083 clause is the text to land.

## Fetch (matches the row)

Command (exit 0), scratch `/fast/scratch/hyaku/kotoba-r57a3/A3ReopenS083/`:

```sh
date -u
curl -sS -D headers.txt -o extensions-reference.md -w 'http_code=%{http_code}\nsize_download=%{size_download}\nurl_effective=%{url_effective}\ncontent_type=%{content_type}\n' --max-time 60 'https://geminicli.com/docs/extensions/reference.md'
wc -c extensions-reference.md
sha256sum extensions-reference.md
```

- `date -u`: `Fri 23 Oct 2026 06:45:35 AM UTC`
- HTTP/2 200; header `date: Fri, 23 Oct 2026 06:45:35 GMT`; `content-type: text/markdown; charset=utf-8`; `content-length: 12022`; `last-modified: Fri, 16 Oct 2026 02:36:07 GMT`; `x-cache: HIT`
- final URL `https://geminicli.com/docs/extensions/reference.md` (no redirect)
- `wc -c`: 12022; `sha256sum`: `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72`

Row at `07c33d73` `corpus/SOURCES.md:96` records HTTP 200, 12,022 B, sha256 `8b9eecb254df04220b23d56da6d63018abe7c5364122af7dee16b05d63b1fe72` (opened 2026-10-23T04:46:46Z). Equal, not merely the lesson's prefix `8b9eecb2…` (`corpus/lessons/round-57.md:18`). No tool installed.

## Gate quote: shaped, one fold, mid-line start

Lesson `## Gate` (`corpus/lessons/round-57.md:18`) and the entry quote cell (`corpus/knowledge/plugin-manifests-round57.md:28`) are the same 11-word string (backticks kept; the counter's split leaves the period on `directory.`):

"Each extension must have a `gemini-extension.json` file in its root directory."

Fetched bytes, verbatim, no markup stripped (the file has no `\r`):

- line 106 (8 words): `Gemini CLI loads extensions from `<home>/.gemini/extensions`. Each extension`
- line 107 (9 words): `must have a `gemini-extension.json` file in its root directory.`

`Each` is byte 2981, column 63 of line 106. The only change from the raw bytes to the quote is one line break folded to a space: the single `\n` between `extension` and `must` (line 106 has no trailing space). Not a fence (the next fence is ` ```json ` at line 113). No list marker. Backticks around `gemini-extension.json` are in both the quote and the page.

The quote is not the whole of `:106-107`. Folding both lines yields 17 words. The unquoted prefix is the 6-word load-path sentence plus the space after it (62 bytes): `Gemini CLI loads extensions from `<home>/.gemini/extensions`. ` The quote then runs to the end of line 107, including the period. Nothing follows it.

## No unshaped quote states that same location

Q42 shaping checked on this page: an unshaped quote is a contiguous single-line span (no folded break, no stripped markup, no omitted fence info string, no omitted list marker).

No single line holds `gemini-extension.json`, an `extension`/`plugin` word outside that token, and `root`. The only sentence that puts the file in the extension root is the shaped one above.

- Line 107 alone is unshaped and 9 words and does say `in its root directory`, but the only `extension` on that line is inside the token, so it does not name the extension.
- The only unshaped 6–25-word span on the page that has the token and an outside `extension` word is line 69 (10 words): `Update an extension to the version specified in its `gemini-extension.json``. That is the quote the source seat proposed (`build/SrcGeminiCLI.md:15-19`). It does not say the file is in the root. The sentence's last word `file.` is on line 70, so the full sentence would also be folded.

Q42's "replace with an unshaped quote when one exists" does not fire. Keep the shaped quote and name what was left out.

## Which note is accurate

Committed entry clause (`plugin-manifests-round57.md:34-35`), true but not enough:

`S083 `extensions-reference.md:106-107` (one line break folded)`

The lesson's parallel clause (`round-57.md:24-25`) is the same gap: `S083 folds one line break (`:106-107`).` Neither says the quote begins at column 63, after the load-path sentence. Reading `:106-107` with one fold as the whole span produces the 17-word string, which is not the quote.

Candidate S083 clause in `.ufo/waves/round-57/a3/a2-candidate.patch` (the `plugin-manifests-round57.md` quote-locations hunk), checked against these bytes: accurate. It does not patch the lesson. This seat did not re-check the other clients' clauses in that hunk, or the hunk's closing sentence about attempt-2 residual seats.

## Exact text to land

Entry, old → new (S083 clause only):

- old: `S083 `extensions-reference.md:106-107` (one line break folded)`
- new: `S083 `extensions-reference.md:106-107` (one line break folded; the quote begins mid-line 106, after the load-path sentence, which is not quoted)`

Lesson `## Gate` quote notes, old → new (not in the candidate patch):

- old: `S083 folds one line break (`:106-107`).`
- new: `S083 folds one line break (`:106-107`; the quote begins mid-line 106, after the load-path sentence, which is not quoted).`
