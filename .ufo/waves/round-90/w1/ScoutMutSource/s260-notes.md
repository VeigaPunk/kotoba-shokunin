# S260 — mutation-testing practice primary source (round-90 §2b)

Seat: **ScoutMutSource** (lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`).
Access date: **2026-11-05** (all fetches this date). Fetch tool: `curl 8.23.0` (system `/usr/bin/curl`).

Purpose: open ONE mutation-testing practice primary source that grounds C1's vocabulary —
the **mutant / killed / survived** terms and the **equivalent-mutant (or mutation-score)**
notion — so `corpus/SOURCES.md` can carry row **S260** (external, tier per contract), and so
the round lesson's `## Gate` can record the route ledger (≥1 rejection with reason + flip).

Per r89 spot-check note 1, the sha256 below is **fetch-time metadata only**. Every quote is
grounded by **line anchor + byte size + page title**, never by the digest.

---

## 1. Route ledger (honest record, in the order prescribed)

| # | route | command | HTTP | bytes | verdict |
|---|---|---|---|---|---|
| (a) | mutmut docs index | `curl -sL --max-time 60 -o s260-routea-mutmut-index.html -w 'HTTP=%{http_code} URL=%{url_effective} SIZE=%{size_download}' https://mutmut.readthedocs.io/en/latest/` | **200** | 51074 | **HTTP 200, but PARTIAL SUPPORT ONLY** — grounds leg (i) killed/survived vocabulary; does **not** ground leg (ii): zero occurrences of "equivalent", and the only "mutation score" mention is a badge command, not a definition |
| (a′) | mutmut "How it works" / glossary subpages | `curl -sL --max-time 60 -o /tmp/mp_* -w '%{http_code}' https://mutmut.readthedocs.io/en/{latest,2.4.0,3.0.0}/{howitworks,glossary,how-it-works,usage,mutations}.html` | **404** (all 15 probes) | ~2.5 KB each | **REJECTED (route absent).** The Sphinx build has exactly one document — `en/latest/searchindex.js` → `docnames: ['index']` — so no "How it works" or glossary page exists to fetch. **Flip:** if mutmut publishes a glossary/how-it-works page naming equivalent mutants and the score formula, re-open and re-judge |
| (a″) | mutmut repo README (source of the same docs text) | `curl -sL --max-time 60 -o s260-routea-mutmut-readme.rst -w 'HTTP=%{http_code} SIZE=%{size_download}' https://raw.githubusercontent.com/boxed/mutmut/master/README.rst` | **200** | 22381 | **corroboration of (a)** — `docs/index.rst` is `.. include:: ../README.rst`, so the readthedocs page and the repo RST carry the same sentences at the same line numbers (workflow lines 617–618 ≡ index lines 537–538) |
| (b) | Stryker Mutator docs entry | `curl -sL --max-time 60 -o s260-routeb-stryker-general.html -w 'HTTP=%{http_code} URL=%{url_effective} SIZE=%{size_download}' https://stryker-mutator.io/docs/` | **200** | 30253 | grounds leg (i) at line 5; links (same site) to the two sub-pages below that carry leg (ii) |
| (b′) | Stryker — Mutant states and metrics | `curl -sL --max-time 60 -o s260-snapshot.html -w 'HTTP=%{http_code} URL=%{url_effective} SIZE=%{size_download}' https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/` | **200** | 27068 | **ADOPTED — the S260 primary.** One page carries **both** required legs with located lines: Killed (12), Survived (14), Mutation score formula (51) + definition (52) |
| (b″) | Stryker — Equivalent mutants | `curl -sL --max-time 60 -o s260-snapshot-equivalents.html -w 'HTTP=%{http_code} URL=%{url_effective} SIZE=%{size_download}' https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants/` | **200** | 38687 | **ADOPTED as the sibling anchor** — the explicit "equivalent mutant" definition (line 16), reached by following `href="/docs/mutation-testing-elements/equivalent-mutants/"` out of the route-(b) page |

Response headers are saved beside each snapshot: `s260-headers-*.txt` (status line, `content-type`,
`last-modified`, `date`, `x-proxy-cache`).

### REJECTED routes (for the lesson `## Gate`)

1. **REJECTED — ACM DL DOI landing, HTTP 403 (bot/paywall gate).**
   `curl -sL --max-time 60 -o rejected-dl.acm.org_doi_10.1145_2382577.2382594.html -w 'HTTP=%{http_code} SIZE=%{size_download}' https://dl.acm.org/doi/10.1145/2382577.2382594`
   → `HTTP=403 SIZE=5471`; body title `Just a moment...` (Cloudflare JS/cookie challenge), 5471 B,
   sha256 `d91bbff16ba212064051e25b28a06e4d5982cb9603136e022beb53812087fa47`.
   **Reason:** the peer-reviewed route is not readable without a JS challenge; no quote may be taken
   from bytes that are not the article. **Flip:** re-open the same DOI through an institutional/
   open-access mirror (or the publisher's PDF endpoint) and re-judge the row if the article's own
   wording is needed for the equivalent-mutant definition.
2. **REJECTED — Wikipedia "Mutation testing", HTTP 200 but tier C, lead only.**
   `curl -sL --max-time 60 -o rejected-en.wikipedia.org_wiki_Mutation_testing.html -w 'HTTP=%{http_code} SIZE=%{size_download}' https://en.wikipedia.org/wiki/Mutation_testing`
   → `HTTP=200 SIZE=170845`; title `Mutation testing - Wikipedia`; sha256
   `52cedf2bd7438ac219a480eaad661dc156eb92fc37eb5d97fc86dc27ed6cfdb8`.
   **Reason:** `community`/encyclopedia text is C-tier — usable as a *lead* to the underlying
   papers, never as sole support for a tier-A-scoped claim; the S260 claim is tier-A-scoped, so
   Wikipedia may not back it. **Flip:** it stays a lead; if a claim ever lands at tier C, or if a
   named paper is cited from its reference list, re-open that paper directly.
3. **REJECTED as the S260 support — route (a) mutmut docs (HTTP 200, 51074 B).** Not refused for
   access; refused as **sole support**, because it cannot ground leg (ii): `grep -niE 'equiv'`
   → no matches, and "Mutation score badges" (line 545) is a `mutmut badge` / `export-cicd-stats`
   command pair, not a definition of the score. **Flip:** if mutmut's docs gain a glossary that
   names equivalent mutants and the score formula, mutmut becomes a valid second tier-A source
   and this rejection flips to "admitted".

---

## 2. The adopted source (S260 primary)

| field | value |
|---|---|
| canonical URL | `https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/` |
| sibling URL (same doc set) | `https://stryker-mutator.io/docs/mutation-testing-elements/equivalent-mutants/` |
| page title (primary) | `Mutant states and metrics \| Stryker Mutator` |
| page title (sibling) | `Equivalent mutants \| Stryker Mutator` |
| HTTP status | 200 (both), `content-type: text/html; charset=utf-8`, `server: cloudflare` |
| byte size | primary **27068 B**; sibling **38687 B** |
| sha256 (fetch-time metadata only) | primary `8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da`; sibling `b71ae15708a1da890d4fedc56a80453fc6619c7ea81ef77e1bc755c471276c42` |
| access date | 2026-11-05 |
| saved bytes | `.ufo/waves/round-90/w1/ScoutMutSource/s260-snapshot.html` (primary), `…/s260-snapshot-equivalents.html` (sibling) |
| kind | `docs` |
| tier | **A**, scoped to *the mutation-testing vocabulary and metric definitions as the mutation-testing tool's own documentation states them* — official vendor documentation is primary for its own terminology. **Not** authoritative for this lane's battery mechanics (those are lane-local, S261) |

---

## 3. Located quotes (each ≤ 25 words; `wc -w` on the quoted segment)

Full `sed -n '<L>p'` outputs and the byte-shaping statement for every quote are in
`s260-quote-receipts.txt` (same directory).

### Leg (i) — the killed / survived vocabulary

**Q1a — killed** — `s260-snapshot.html` **line 12** — `wc -w` = **15**

> "When at least one test failed while this mutant was active, the mutant is killed."

`sed -n 12p s260-snapshot.html` →
```
When at least one test failed while this mutant was active, the mutant is killed. This is what you want, good job!</li>
```
Byte shaping: **none** — the quoted segment is a contiguous raw-byte substring of line 12.

**Q1b — survived** — `s260-snapshot.html` **line 14** — `wc -w` = **12**

> "When all tests passed while this mutant was active, the mutant survived."

`sed -n 14p s260-snapshot.html` →
```
When all tests passed while this mutant was active, the mutant survived. You're missing a test for it.</li>
```
Byte shaping: **none** — contiguous raw-byte substring of line 14.

Corroboration from the route-(b) entry page, `s260-routeb-stryker-general.html` line 5 (30253 B,
title `What is mutation testing? | Stryker Mutator`): the same two terms in one sentence —
`If your tests fail then the mutant is killed. If your tests passed, the mutant survived.`
— and at line 20 `If at least one of your tests fail, we say the mutant is killed. … If no test fails, it survived.`
Byte shaping: the `<em>` tags are the only markup removed for reading; no words altered.

### Leg (ii) — the equivalent-mutant / mutation-score notion

**Q2a — mutation score definition** — `s260-snapshot.html` **line 52** — `wc -w` = **12**

> "The total percentage of mutants that were detected. The higher, the better!"

`sed -n 52p s260-snapshot.html` →
```
<!-- -->The total percentage of mutants that were detected. The higher, the better!</li>
```
Byte shaping: **none** — contiguous raw-byte substring of line 52.

**Q2b — the score formula** — `s260-snapshot.html` **line 51** — `wc -w` = **5**

> "detected / valid * 100"

`sed -n 51p s260-snapshot.html` →
```
<li class=""><strong>Mutation score</strong> <code>detected / valid * 100</code><br/>
```
Byte shaping: **none** — contiguous raw-byte substring of line 51 (the `<strong>`/`<code>` markup
around it is not part of the quoted segment).

**Q3 — the equivalent-mutant notion (explicit)** — `s260-snapshot-equivalents.html` **line 16** — `wc -w` = **17**

> "It is called equivalent mutant. There is no definitive way for Stryker to find and ignore them."

`sed -n 16p s260-snapshot-equivalents.html` →
```
<p>It is called <em>equivalent mutant</em>. There is no definitive way for Stryker to find and ignore them. There is currently also no way yet to mark them to be ignored.</p>
```
Byte shaping: the quoted segment crosses the `<em>…</em>` markup boundary; **the only bytes
removed are those two literal tag sequences** (`<em>` and `</em>`) — no word, spacing or
punctuation was altered. The raw line above is the verbatim snapshot byte sequence.

**Q4 (corroboration, mutmut — route (a) partial support)** — `s260-routea-mutmut-index.html`
(51074 B, title `mutmut - python mutation tester — mutmut documentation`), line 157:
> "there could only ever show up as survivors." (`wc -w` = 7)

and lines 537–538 (identical sentences in the repo RST at lines 617–618):
> "Find a mutant you want to work on and write a test to try to kill it." (`wc -w` = 15)

Byte shaping: **none** on either — contiguous raw-byte substrings of the named lines.

---

## 4. What the opened source teaches (for the scribe's `teaches` cell)

A mutant is **killed** when at least one test fails with the mutant active, and **survived** when
all tests pass with it active; the **mutation score** is the percentage of *detected* (killed +
timeout) among *valid* mutants. A **mutant** is the mutated program; a mutant that no test can
distinguish from the original is an **equivalent mutant** — it survives by construction, and
nobody has a definitive way to find and ignore it automatically. Therefore a battery that reports
"equivalents survived E of E" is reporting a *property of the mutants it generated*, not a
failure of the suite: the score ceiling for such a battery is below 100 % by exactly the
equivalent-class count.

This is the vocabulary C1's frozen predicate speaks (`killed K of M`, `equivalents survived E of E`,
`disclosed survivors S of S`): the score formula `detected / valid * 100` says why an equivalent
mutant cannot be counted as detected, and the equivalent-mutant definition says why it must not
be counted as a gap in the suite.

---

## 5. Row proposal for ScribeCorpus (`corpus/SOURCES.md`, owner: ScribeCorpus)

The scribe writes the row; this is the content the seat measured. Field values are proposals only.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S260 | Stryker Mutator documentation — "Mutant states and metrics" and "Equivalent mutants" — https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ (and …/equivalent-mutants/); HTTP 200, 27068 B and 38687 B, fetched 2026-11-05 | docs | A | the mutation-testing vocabulary and metric definitions as the tool's own documentation states them (killed / survived / mutation score / equivalent mutant) — not this lane's battery mechanics | "Mutant states and metrics" § Mutant states: Killed (HTML line 12), Survived (line 14), § Metrics: Mutation score `detected / valid * 100` (line 51) + definition (line 52); "Equivalent mutants" § Equivalent mutants (HTML line 16); both pages' own <title> and byte size as the fetch anchor | a mutant is killed iff ≥1 test fails and survived iff all tests pass; mutation score = detected/valid*100; an equivalent mutant is indistinguishable from the original, survives by construction and cannot be auto-ignored, so it caps the attainable score rather than exposing a test gap | mined | 2026-11-05 | 180d | corpus/knowledge/mutation-battery-round90.md |

Gate evidence to copy into the round lesson `## Gate` (≤25 words, with location):
URL + access date + byte size + line anchor + the quote.

---

## 6. Files this seat wrote (all under `.ufo/waves/round-90/w1/ScoutMutSource/`)

- `s260-notes.md` — this file.
- `s260-snapshot.html` — primary snapshot, 27068 B, sha256 `8641c389…` (HTTP 200).
- `s260-snapshot-equivalents.html` — sibling snapshot, 38687 B, sha256 `b71ae157…` (HTTP 200).
- `s260-routeb-stryker-general.html` — route-(b) entry page, 30253 B, sha256 `cd83338b…` (HTTP 200).
- `s260-routea-mutmut-index.html` — route-(a) partial-support page, 51074 B, sha256 `07453b3f…` (HTTP 200).
- `s260-routea-mutmut-readme.rst` — route-(a″) corroboration, 22381 B, sha256 `412dd489…` (HTTP 200).
- `s260-headers-*.txt` — response headers per fetch (5 files).
- `s260-quote-receipts.txt` — `sed -n '<L>p'` outputs, `wc -w` counts, byte-shaping statements.
- `receipts-rejected-routes.txt` — the two rejected fetches with HTTP status and digests.
- `rejected-*.html` — the two rejected bodies as fetched (403 ACM body; 200 Wikipedia body).

Nothing outside `.ufo/waves/round-90/w1/ScoutMutSource/` was written by this seat; no git or jj
command was run against the lane.
