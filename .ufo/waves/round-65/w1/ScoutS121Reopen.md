# ScoutS121Reopen — S121 live re-open (freshness axis)

Seat: scout, wave kotoba-r65-w1, 2026-10-24. Lane bounds respected: read-only on
the fleet/lane tree; all scratch under `/tmp`; no subagent dispatch.

## Live re-open of S121

Command (run 2026-10-24, this session):

```
$ curl -sSL -o /tmp/S121-live.pdf https://madeyski.e-informatyka.pl/download/Madeyski13TSE.pdf \
    -w 'HTTP %{http_code} | %{size_download} B | %{time_total}s'
HTTP 200 | 1126684 B | 3.687916s
$ sha256sum /tmp/S121-live.pdf
bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3  /tmp/S121-live.pdf
$ stat -c %s /tmp/S121-live.pdf
1126684
$ file /tmp/S121-live.pdf
PDF document, version 1.5
$ cmp /tmp/S121-live.pdf .ufo/waves/round-65/snapshots/S121.pdf && echo 'BYTES IDENTICAL'
BYTES IDENTICAL
```

Freshly extracted text is byte-identical to the committed text artifact:

```
$ pdftotext /tmp/S121-live.pdf /tmp/S121-live.txt
$ cmp /tmp/S121-live.txt .ufo/waves/round-65/snapshots/S121.txt → no output
$ sha256sum S121-live.txt snapshots/S121.txt
475818a52ede04c3ca1c3a25eb5f1f813c931ef0ba07d5f9d2f23228ab60d27c  (both files)
$ pdfinfo S121-live.pdf → Pages: 22, CreationDate: Mon Aug 25 09:21:17 2014 -03
```

## Quote verification (whitespace-normalized, fresh bytes)

Both quotes found verbatim after whitespace normalization (`re.sub(r'\s+',' ')`):

- Q1 (16 words): "The experiment indicated that SOM in general and JudyDiffOp
  strategy in particular provide the best results" — found=True. Spans
  extracted-text lines 62–66; the row anchors it to line 64 — **agree**.
- Q2 (24 words): "Empirical results suggest that applying SOMs reduced the
  number of mutants by approximately 50%, without much decrease in the quality
  of the test suite." — found=True. Sits at extracted-text lines 1174–1176
  exactly as the row anchors — **agree**.
- DOI `10.1109/TSE.2013.44` present in the live bytes at extracted-text line 90
  — **agree** with the row's publisher-record cell ("from the PDF header
  line 90").

## Re-open of the REJECTED first candidate arXiv:1309.4818

```
$ curl -sSL https://arxiv.org/abs/1309.4818 → HTTP 200
<title>[1309.4818] Carlson's <_1-relation on the class of epsilon numbers</title>
Authors: Parménides García Cornejo
Subjects: Logic (math.LO); submitted 18 Sep 2013
Abstract: "Based on the class of epsilon numbers, another binary relational
  <^1 in the ordinals is introduced..."
```

- `mutation` / `Madeyski` do not occur anywhere on the live page.
- Confirmed NOT the mutation paper — a mathematical-logic paper on Carlson's
  ε-numbers. **Agree** with the recorded rejection (M101) and the report's
  "Rejected with reasons" line.

## Agree/disagree with the row's anchor cells

| Row cell (corpus/SOURCES.md:132) | Live observation | Verdict |
|---|---|---|
| URL madeyski.e-informatyka.pl/…Madeyski13TSE.pdf | HTTP 200, application/pdf | agree |
| 1,126,684 B | 1,126,684 B | agree |
| sha256 `bad1b681…a07418a3` | identical digest | agree |
| opened 2026-10-24 | re-opened 2026-10-24 live | agree |
| quote cell Q1, abstract, 16 words | verbatim, whitespace-normalized | agree |
| support quote Q2, lines 1174–1176, 24 words | verbatim at lines 1174–1176 | agree |
| DOI 10.1109/TSE.2013.44 (header line 90) | present at extracted-text line 90 | agree |
| snapshot `.ufo/waves/round-65/snapshots/S121.pdf` | byte-identical (cmp clean) | agree |
| extracted text `S121.txt` | byte-identical (sha `475818a5…`) | agree |
| arXiv:1309.4818 rejected | live page: math.LO ε-numbers paper | agree |

**Verdict: AGREE on every anchor cell.** Nothing drifted since the opening
(same digest — the artifact is static). Freshness holds: source is live,
reachable, and the committed snapshot is faithful.

## Claims supported / falsified

- Supports: S121 admit decision (spot-check target); the report's "S121
  opening" evidence (HTTP 200, size, sha); the row's quote/locator cells;
  M101's recorded rejection of arXiv:1309.4818.
- Falsifies: nothing.

## Gaps / residual unknowns

- [INFERENCE] IEEE TSE 40(1):23-42 publication metadata comes from the PDF
  header/preprint itself; I did not re-open the IEEE Xplore record (row cites
  the DOI from the artifact, which is what it documents).
- Tier-A framing (author-hosted preprint vs IEEE record) is CriticFrontier's
  seat — not attacked here.

## Tooling

No installs this seat (curl, sha256sum, cmp, pdftotext, pdfinfo, python3 all
pre-installed; pacman pause respected).
