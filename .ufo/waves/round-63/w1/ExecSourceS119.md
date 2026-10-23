# ExecSourceS119
role: S119 source-freshness scout
item: C2 repair-method primary-source probe

## Findings

1. All three requested URLs failed via static fetch, so none was a usable hit: `https://publicationethics.org/guidance/correction` returned HTTP 403; `https://publicationethics.org/retraction-guidelines` returned HTTP 403; `https://www.niso.org/publications/rp-8-2008-jav` returned HTTP 404. No body bytes were available to hash or quote for these failures.

2. Fallback primary source: International Committee of Medical Journal Editors (ICMJE), “Corrections and Version Control,” accessed 2026-10-23. `curl` followed redirects; the effective URL is unchanged. Command and actual output:

```text
curl -L -sS -o /tmp/kotoba-s119-icmje.html -w 'final_url=%{url_effective}\nhttp_status=%{http_code}\nbytes=%{size_download}\n' 'https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html' && sha256sum /tmp/kotoba-s119-icmje.html
final_url=https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
http_status=200
bytes=22722
e2c3db0563cf06fe9cd048b1c0a9766ccb420c1c2396336b6f845d4c0e5e830d  /tmp/kotoba-s119-icmje.html
```

3. Three candidate quotes from the fetched HTML body (all <=25 words; line numbers are from that exact downloaded body). The exact-pattern `functions.grep` probes and matching output:

```text
functions.grep(path="/tmp/kotoba-s119-icmje.html", pattern="publish a correction notice  as soon as possible detailing changes from and citing the original publication")
170: <li><i class="icon-li icon-ok"></i>The journal should publish a correction notice  as soon as possible detailing changes from and citing the original publication; the correction should be on an electronic or numbered print page that is included in an electronic or a print Table of Contents to ensure proper indexing. </li>

functions.grep(path="/tmp/kotoba-s119-icmje.html", pattern="archive all prior versions of the article")
172: <li><i class="icon-li icon-ok"></i>The journal should archive all prior versions of the article. This archive can be either directly accessible to readers or can be made available to the reader on request.</li>

functions.grep(path="/tmp/kotoba-s119-icmje.html", pattern="The citation should be to the most recent version.")
174: <li><i class="icon-li icon-ok"></i>The citation should be to the most recent version.</li>
```

4. Interpretation: Quote 1 supports publishing a distinct, transparent correction notice that cites the original; quote 2 supports preserving prior versions. Together they support transparent correction/version history rather than silent in-place rewriting. Quote 3 (latest-version citation) does **not** support append-only correction by itself. ICMJE does not literally prescribe an “append-only” log, so cite it for the correction-notice, citation, and prior-version preservation practice—not as an exact rule for append-only file edits.

## Artifacts

```text
ICMJE | Recommendations | Corrections and Version Control
https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html
HTTP 200 | 22,722 bytes | SHA-256 e2c3db0563cf06fe9cd048b1c0a9766ccb420c1c2396336b6f845d4c0e5e830d

Line 170 (16 words): “publish a correction notice  as soon as possible detailing changes from and citing the original publication”
Line 172 (7 words): “archive all prior versions of the article”
Line 174 (9 words): “The citation should be to the most recent version.”
```

## Verdict

INFORMS — the requested three URLs were unavailable, but the ICMJE primary guidance is a byte-verified alternative that supports transparent corrections and preserved versions. I would change this assessment if the downloaded body/hash or exact line-matched substrings proved incorrect, or if the C2 claim requires an explicit literal append-only mandate.
