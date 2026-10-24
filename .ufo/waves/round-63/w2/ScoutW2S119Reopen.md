# ScoutW2S119Reopen

role: scout (non-author re-open; CORPUS.md SOURCES rule 1 — "Non-author verification re-opens a sample")
item: S119 quote-present re-open of https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html against committed snapshot `.ufo/waves/round-63/snapshots/S119.page` at `cbbee56e9a3589b0b46736ad36f1b77701def80e`
axes: freshness (judged). No other axis moved. Tools installed: none.

## Verdict

**quote-present PASS.** Both located sentences are still on the live page, on the same lines as the committed snapshot, and both are literal substrings of this re-open and of the snapshot. The teaches cell's two quoted spans are literal substrings of both. Byte-identity is not claimed by the row and is not held: two fetches minutes apart, same size, different sha256, and the only body delta versus the snapshot is the Cloudflare `__CF$cv$params` tail on line 310.

Committed bytes checked, not a dirty tree: `git rev-parse HEAD` = `cbbee56e9a3589b0b46736ad36f1b77701def80e`; `git status --short` on `corpus/SOURCES.md`, the knowledge entry, the lesson, and `S119.page` was empty; `git hash-object` of the snapshot equals `HEAD:.ufo/waves/round-63/snapshots/S119.page` (`664e7e16df33b7ac5693a5ba48b34afdf3994929`). Snapshot sha256 `d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2` matches the S119 anchor cell.

## Attack

```text
date -u +'%Y-%m-%dT%H:%M:%SZ' && curl -sS -L -D /tmp/kotoba-r63-w2-s119.headers -o /tmp/kotoba-r63-w2-s119.html -w 'final_url=%{url_effective}\nhttp_status=%{http_code}\nbytes=%{size_download}\ncontent_type=%{content_type}\nredirects=%{num_redirects}\n' --max-time 45 'https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html' && wc -c /tmp/kotoba-r63-w2-s119.html && sha256sum /tmp/kotoba-r63-w2-s119.html && sha256sum .ufo/waves/round-63/snapshots/S119.page && wc -c .ufo/waves/round-63/snapshots/S119.page
```

```text
2026-10-24T01:57:12Z
final_url=https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
http_status=200
bytes=22722
content_type=text/html
redirects=0
22722 /tmp/kotoba-r63-w2-s119.html
f6362c09dddaca8631c502864a6b595b190c5ed285317a4e2988f7a49f718b44  /tmp/kotoba-r63-w2-s119.html
d76af0c067c1f09a21113857f66eb6725ee75d1731f5339da464e5555d3bc9d2  .ufo/waves/round-63/snapshots/S119.page
22722 .ufo/waves/round-63/snapshots/S119.page
```

Response headers recorded, cookie and NEL endpoint omitted: HTTP/2 200, content-type text/html, cf-cache-status DYNAMIC, date Sat, 24 Oct 2026 01:57:13 GMT.

Second fetch, 70 seconds later, same URL:

```text
2026-10-24T01:58:22Z
http_status=200
bytes=22722
content_type=text/html
110de2fd787752122a1f0d06264d93d748ce46c42ea2b88f8a5c4092e256c782  /tmp/kotoba-r63-w2-s119-b.html
```

Fetch A equals fetch B: false. Fetch B equals snapshot: false. Quote-region lines 165-180 identical to the snapshot on both fetches. Diff of fetch A vs snapshot: 19 bytes, line 310 only (`r:'a4f4625d0c646d39'` to `r:'a4f55e948d012b18'`, `t:'MTc5Mjc5NjcwMg=='` to `t:'MTc5MjgwNzAzMw=='`). Diff of fetch A vs fetch B: 15 bytes, same line, same two parameters.

### grep (verbatim)

Fixed-string probes. `grep -nF` exit 0 on snapshot and on fetch A for both sentences.

```text
=== SNAPSHOT greps ===
170:						<li><i class="icon-li icon-ok"></i>The journal should publish a correction notice  as soon as possible detailing changes from and citing the original publication; the correction should be on an electronic or numbered print page that is included in an electronic or a print Table of Contents to ensure proper indexing. </li>
exit_q1_snap=0
172:						<li><i class="icon-li icon-ok"></i>The journal should archive all prior versions of the article. This archive can be either directly accessible to readers or can be made available to the reader on request.</li>
exit_q2_snap=0
=== FRESH greps ===
170:						<li><i class="icon-li icon-ok"></i>The journal should publish a correction notice  as soon as possible detailing changes from and citing the original publication; the correction should be on an electronic or numbered print page that is included in an electronic or a print Table of Contents to ensure proper indexing. </li>
exit_q1_new=0
172:						<li><i class="icon-li icon-ok"></i>The journal should archive all prior versions of the article. This archive can be either directly accessible to readers or can be made available to the reader on request.</li>
exit_q2_new=0
=== quote-region diff (lines 165-180) ===
quote-region identical
```

`wc -w` on the lesson's two extracted quotes: 16 and 7. Python `in` on both snapshot and fetch A:

| span | snap | fresh | words |
|---|---|---|---|
| lesson `:170` `publish a correction notice  as soon as possible detailing changes from and citing the original publication` (two spaces after `notice`) | yes | yes | 16 |
| lesson `:172` `archive all prior versions of the article` | yes | yes | 7 |
| teaches `"as soon as possible detailing changes from and citing the original publication"` | yes | yes | 12 |
| teaches `"archive all prior versions of the article"` | yes | yes | 7 |

The teaches cell (`corpus/SOURCES.md:131`, committed) is grounded by those two spans: a correction notice that cites the original, and preservation of prior versions. The cell already bounds the rest ("not a silent rewrite of the record; the page does not mandate literal append-only files"). The anchor's dynamic-element disclaimer is what this re-open observed: same 22,722 B, sha256 not `d76af0c0…` and not the cited seat probe `e2c3db05…`.

## Bound (no row change)

Do not rewrite the S119 row or the snapshot. The row's disclaimer is the correct claim. Exact bound text, if a later note needs one sentence:

> Re-opened 2026-10-24T01:57:12Z and 2026-10-24T01:58:22Z: HTTP 200, 22,722 B, sha256 `f6362c09dddaca8631c502864a6b595b190c5ed285317a4e2988f7a49f718b44` then `110de2fd787752122a1f0d06264d93d748ce46c42ea2b88f8a5c4092e256c782`. Lines 165-180 match snapshot `d76af0c0…`; the only body delta is `window.__CF$cv$params` on line 310. Located quotes at `:170` and `:172` are unchanged.

## Smallest safe correction (not required for PASS)

`corpus/knowledge/compound-clause-citation-round63.md:19-20` joins a quotation that drops the page's second space, so the joined string is not a substring (`grep -nF` exit 1; Python `in` False on snapshot and on both fetches). The double-space form is a substring. This does not touch the teaches cell or the lesson Gate, which keep the literal spans.

Proposed line 19 (one added space after `notice`):

```text
   the practice for a published article: publish "a correction notice  as soon as
```

Joined quote that then matches `:170`: `a correction notice  as soon as possible detailing changes from and citing the original publication`.

## Unresolved

None for quote-presence. The page still does not say "append" or forbid an in-place edit of article text; that bound is already in the teaches cell and the knowledge entry, and this re-open does not widen it.
