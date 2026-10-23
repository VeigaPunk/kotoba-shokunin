# RevSourceQuote

role: reviewer — S119 quote discipline, independent fetch
item: Verify S119 correction-practice source: substring, ≤25-word quote, located line, sha256-vs-snapshot, and whether "appended correction rather than in-place rewrite" is what the page says.

## Findings

1. **All three plan-suggested URLs are dead today** (independent fetch 2026-10-23, `curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'`): `publicationethics.org/guidance/correction` → HTTP 403 Cloudflare challenge (5,586 B); `publicationethics.org/retraction-guidelines` → HTTP 403 challenge (5,592 B); `www.niso.org/publications/rp-8-2008-jav` → HTTP 404 (21,189 B Drupal 404 page). Same failures as `ExecSourceS119`. Any S119 row must cite a fallback source.

2. **Acta Orthopaedica (`ExecSourcesRow` draft source) is byte-verified and fetch-stable.** My fetch `curl -sSL 'https://actaorthop.org/actao/correctionsandappeals'` → HTTP 200, 21,024 B, sha256 `39e51269ad0eef9888e011a7bc5e9cd253dbbfb1cd1e3edcf5b76761ad1b9494` — **byte-identical** to the sibling's independent fetch one minute earlier (same size + hash). A snapshot committed today of these bytes reproduces exactly.
   - (a) Substring: `grep -o 'Any necessary changes[^<]*' body-acta.html` returns the full sentence; the proposed 19-word quote `Any necessary changes will be accompanied with a post-publication notice which will be permanently linked to the original article` is a literal substring (sentence continues "…so that readers will be fully informed…").
   - (b) Word count: 19 ≤ 25. (c) Located line: 252 (raw HTML).
   - (d) sha256 `39e51269…` — **will** match a snapshot committed today (stable page).

3. **COUNTER-EVIDENCE — Acta is not an "appended rather than in-place rewrite" source.** Same line 252 states, verbatim: `Articles that have been published should remain extant, exact, and unaltered to the maximum extent possible. Necessary corrections will be made to published articles however as authorized by the Editor.` The page's policy is **in-place correction of the published article plus a permanently linked notice** — the exact model the plan's wording excludes. The sibling's own finding 2 concedes it "does not prohibit authorized changes to article text," yet the draft row's teaches cell claims "published articles should remain unaltered to the maximum extent possible" — that phrase is the *aspiration* half of a sentence whose "however" clause authorizes edits. If the row teaches append-not-rewrite, the quote alone does not carry it.

4. **ICMJE (`ExecSourceS119` source) is semantically the best match for "appended correction rather than in-place rewrite"** — its model is post-a-new-dated-version + archive-all-prior-versions + linked correction notices (versions stack; nothing silently rewritten). Verified on my own fetch `curl -sSL 'https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/corrections-and-version-control.html'` → HTTP 200, 22,722 B (same count as sibling), sha256 `d2c41fb8bd98ad5d9ea018f393385b5b01e6fdf2db192dc5b9b649fd67d23ab7`.
   - Best candidate quote (a–c): `post a new article version with details of the changes from the original version and the date(s) on which the changes were made` — Python `in` and `grep -F` both confirm literal substring; 23 words ≤ 25; located at raw line 171. Support quotes: `The journal should archive all prior versions of the article` (10 words, line 172) and `Previous electronic versions should prominently note that there are more recent versions of the article` (15 words, line 173). All verified substrings in all three of my independent fetches.
   - (d) sha256 **will NOT reproduce on refetch**: three of my fetches (22722 B each) gave `d2c41fb8…`, `85640fd1…`, `6d3fd492…` and the sibling's `e2c3db05…` differs again. The only diff is a per-request Cloudflare-injected script at the tail (my diff: line 971 `window.__CF$cv$params={r:'a4f4610b6e26c802',t:…}` → `r:'a4f461d78da6ece8'`); the quote region (lines 170–174) is identical. A committed snapshot is honest as a fetch receipt, but a later refetcher's sha256 will differ — the row should not claim reproducible page bytes, or the snapshot should record the hash with a "per-request CF script tail" note.

5. **Honest-scope caveat for ICMJE too:** the word "append" never appears on the page (only "appendix," once, re: showing retraction-diff extent in supplementary material/appendix for "complete transparency"), and ICMJE's model is *new version + archive*, not literal text-append; it also permits retraction-with-republication of a changed paper. The strongest defensible teaching is "transparent, dated, linked corrections with preserved prior versions" — LOG.md's append-only discipline is a stricter instance of that, so the citation holds if the row teaches transparency/preservation rather than asserting the source mandates append-only.

6. **Sibling cross-check:** `ExecSourceS119.md` line numbers 170/172/174 all match my raw HTML exactly; their 16/7/9-word counts recount correctly. `ExecSourcesRow.md`'s line-252 quote and hash reproduce byte-exact. No committed snapshot exists yet (`.ufo/waves/round-63/snapshots/` empty at 23:0XZ); whichever fetch's bytes the L1 snapshots will be authentic, but only Acta's hash refetches identically.

## Artifacts

```text
$ curl -sSL -D hdr -o body-acta.html 'https://actaorthop.org/actao/correctionsandappeals'
final_url=https://actaorthop.org/actao/correctionsandappeals  http_status=200  bytes=21024
39e51269ad0eef9888e011a7bc5e9cd253dbbfb1cd1e3edcf5b76761ad1b9494  body-acta.html
$ grep -n -o 'Any necessary changes[^<]*' body-acta.html
252:Any necessary changes will be accompanied with a post-publication notice which will be permanently linked to the original article so that readers will be fully informed of any necessary changes. The Editor will decide…
$ grep -n -i -o '[^<]*unaltered[^<]*' body-acta.html
252:p>We follow the STM Association guidelines that "Articles that have been published should remain extant, exact, and unaltered to the maximum extent possible". Necessary corrections will be made to published articles however as authorized by the Editor.
```

```text
$ python3 substring check on my ICMJE fetch (22,722 B, sha256 d2c41fb8…)
substring=True line=171 words=23 :: b'post a new article version with details of the changes from the original version and the date(s) on which the changes were made'
substring=True line=172 words=10 :: b'The journal should archive all prior versions of the article'
substring=True line=173 words=15 :: b'Previous electronic versions should prominently note that there are more recent versions of the article'
substring=True line=170 words=16 :: b'publish a correction notice  as soon as possible detailing changes from and citing the original publication'   # note raw double space after "notice"
```

```text
$ sha256sum across three ICMJE fetches ~1 min apart (all 22,722 B; only the injected CF script differs)
d2c41fb8bd98ad5d9ea018f393385b5b01e6fdf2db192dc5b9b649fd67d23ab7  fetch1
85640fd17b5888a15cc465c73dc14bb8b9e0a7886ebf9d5d9ca9f5f2223647d8  fetch2
6d3fd49229572628cd41d03bf99bafc84e44e6b852fdc13f088c7d5e16c65ad5  fetch3
sibling ExecSourceS119: e2c3db0563cf06fe9cd048b1c0a9766ccb420c1c2396336b6f845d4c0e5e830d
```

Recommendation for the L1: prefer **ICMJE** (semantics match the plan's "appended rather than in-place rewrite") with the 23-word line-171 quote and a snapshot note that the tail hash is per-request; if **Acta** is used, keep the linked-notice teaching but drop any claim that the source requires leaving the article unaltered — the page says the opposite.

## Verdict

INFORMS — both candidate sources' quotes verify as literal substrings on my own bytes (Acta 19w@252, stable sha `39e51269…`; ICMJE 23w@171 + 10w@172 + 15w@173, volatile sha), but Acta's page explicitly authorizes in-place corrections ("Necessary corrections will be made to published articles however as authorized by the Editor") — counter-evidence against the "rather than in-place rewrite" claim if asserted as the source's rule. I would change my recommendation if a fetch-stable primary source mandating version-preserving corrections (e.g., an accessible COPE errata page or RFC-Editor immutability text) were produced, or if the S119 row's teaches cell is narrowed to linked transparent notices + preserved prior versions.
