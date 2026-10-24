# ScoutS120 — open S120 (mutation-testing primary)

Seat: `kotoba-r64.ScoutS120`. Access date: 2026-10-24. No tools installed. No production files written. One wave-evidence file written: `.ufo/waves/round-64/snapshots/S120.page`.

## Verdict

The plan's bibliographic triple does **not** open this paper. The title does. Opened primary is Petrović, Ivanković, Fraser, and Just, *Practical Mutation Testing at Scale* (subtitle on the PDF: *A view from Google*), arXiv:2102.11378v2 [cs.SE] 26 Feb 2021. Michael Ernst is not an author. The work is not ICSE 2021.

**Gate quote (22 words), the one quote for the teaches cell:**

> Mutation analysis assesses a test suite’s adequacy by measuring its ability to detect small artificial faults, systematically seeded into the tested program.

Anchor: Abstract, first paragraph, HTML id `abstract1.1`, first sentence. The apostrophe in `suite’s` is U+2019. Present in the snapshot.

**Tier proposal: A**, scoped only to this paper's own statement that mutation analysis measures test-suite adequacy by whether the suite detects seeded faults (the mutant-kill / detection witness), inside a paper whose subject is that measurement deployed at Google scale. Not A for Ernst as author, for ICSE 2021, for arXiv:2103.02722, for DOI 10.1109/ICSE43902.2021.00068, or for reading any kill rate as traditional mutation score or as proof a kill is a real fault.

## Opened source (the snapshot)

| field | value |
|---|---|
| URL | https://arxiv.org/html/2102.11378 |
| request profile | default curl (no custom UA, no Accept override), `-L` |
| access date | 2026-10-24 (response `date: Sat, 24 Oct 2026 03:37:19 GMT`; `last-modified: Mon, 24 Aug 2026 19:56:57 GMT`) |
| HTTP | 200 |
| content-type | text/html; charset=utf-8 |
| bytes | 571600 |
| sha256 | `15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8` |
| snapshot | `.ufo/waves/round-64/snapshots/S120.page` (byte-identical; `sha256sum` after copy matches) |

Alternate request profile, same work, different body (not the snapshot):

| field | value |
|---|---|
| URL | https://arxiv.org/pdf/2102.11378.pdf (301 to `/pdf/2102.11378`, then 200) |
| profile | Chrome-like UA + `Accept: application/pdf,*/*` |
| HTTP | 200, `application/pdf`, `last-modified: Mon, 23 Jan 2023 08:47:39 GMT` |
| bytes | 728951 |
| sha256 | `a9bdf44159a7b8a6f4b77d7e347650e52d9915bf68f765ff5333f7feee56a081` |
| pages | 22 (`pdfinfo`) |
| scratch | `/tmp/scout-s120/2102.11378.pdf` |

Confirmatory HTML fetch `https://export.arxiv.org/html/2102.11378v2` was HTTP 200, 571600 bytes, **sha256-identical** to the snapshot. ar5iv `https://ar5iv.labs.arxiv.org/html/2102.11378` timed out: curl exit 28, HTTP 000, 0 bytes (not an opened body).

Abs page (identity only, not the snapshot): `https://arxiv.org/abs/2102.11378` HTTP 200, 45029 bytes, sha256 `aaf66df07f514232c0eb1cdf010c9db99a1a9e886c9a6a3f933c54fb32eceeed`. Citation metadata: title `Practical Mutation Testing at Scale`; authors Goran Petrović, Marko Ivanković, Gordon Fraser, René Just; `citation_arxiv_id` 2102.11378; submitted 2021-02-22, announced 2021-02-26; comment "This work has been submitted to the IEEE for possible publication". No journal-ref and no DOI on the abs page.

Authors on the HTML (`ltx_personname`): Goran Petrović, Marko Ivanković, Gordon Fraser, René Just. Version line in the HTML: `arXiv:2102.11378v2 [cs.SE] 26 Feb 2021`.

## What the quote grounds, and what it does not

The 22-word sentence is the paper's own definition of the witness: adequacy is measured by detection of seeded faults. In this literature a detected mutant is a killed mutant. That is the teaches-cell benefit (mutant-kill as the coverage witness). "Deployed at scale" is the paper's subject (title; § II *Mutation Testing at Google*; abstract scale sentences) and is **not inside** these 22 words. No single ≤25-word sentence in the opened HTML contains both the adequacy definition and the Google-scale deployment.

Located empirical companion, **not** the gate quote (13 words), § V-C *RQ2 Mutant Survivability*, paragraph `S5.SS3.p2.1`, first sentence:

> Overall, 87.5% of all generated mutants are killed by the initial test suite.

The next sentence in that paragraph says this is not the traditional mutation score, because mutagenesis is probabilistic and generates only a subset. Do not teach 87.5% as the coverage witness.

## Tier A scope (proposal for the S120 row)

- kind: `paper`
- tier: **A**
- scope to write: mutant-kill (detection of a seeded fault) as the test-suite adequacy witness, as stated by this paper; the Google deployment is the setting, not a license to treat every kill as a real fault or as line coverage
- anchor to write: Abstract, `abstract1.1`, first sentence; arXiv:2102.11378v2 (26 Feb 2021). Journal version, Crossref only, not opened: *IEEE Transactions on Software Engineering*, DOI 10.1109/TSE.2021.3107634, issued 2022-10-01, pages 3900–3912, title *Practical Mutation Testing at Scale: A view from Google*, same four authors
- recheck: 180d
- status: the row is the scribe's; this seat does not write `corpus/SOURCES.md`

## Plan identifiers — opened, rejected

These were fetched. They are not the titled paper. Do not snapshot them as S120 and do not cite them as this source.

1. **arXiv:2103.02722** (plan's id). Default abs `https://arxiv.org/abs/2103.02722` HTTP 200, 39320 bytes, sha256 `b9074417b0916f55454fcb238218756660cfda5dd5f950d3d55a5d8174300bc1`. Title: *A Markov jump process associated with the matrix-exponential distribution*, author Oscar Peralta. ar5iv HTML `https://ar5iv.labs.arxiv.org/html/2103.02722` HTTP 200, 305407 bytes, sha256 `c9a8764be7ba2e056c45f8b6bfd430800e427e2cc7e8eef025d396baccc8f83d`, same title. PDF `https://arxiv.org/pdf/2103.02722.pdf` HTTP 200, 198298 bytes, sha256 `2f7d8c52497e4774c9cd1b0346adc748ff924f0c1da62f458fa80a16f119d43b`, 12 pages. **Rejected:** wrong work.

2. **DOI 10.1109/ICSE43902.2021.00068** (plan's DOI). `https://doi.org/10.1109/ICSE43902.2021.00068` with a browser UA and `Accept: text/html` returned 302 to `https://ieeexplore.ieee.org/document/9401981/`, then **HTTP 202**, 2055 bytes, sha256 `2e829b01d4d98cbeb4eb53f2da5b59c40259e48506b8c6f71b0fd6bc18ab2e7a`. Body is an AWS WAF interstitial, not the article. Crossref `https://api.crossref.org/works/10.1109/ICSE43902.2021.00068` HTTP 200, 8977 bytes, sha256 `950a2b5056cd9bbe3a2ddac519ed0c9ba68dece3bf603c5b8894feb3b5921532`: title *An Empirical Study on Deployment Faults of Deep Learning Based Mobile Applications*, Chen et al., ICSE 2021, pages 674–685. **Rejected:** wrong work; IEEE HTML not opened.

Crossref for the journal version of the **title-matched** paper: `https://api.crossref.org/works/10.1109/TSE.2021.3107634` HTTP 200, 6804 bytes, sha256 `67bc39e21a883f6775398b09eba7a446df77dee356b2ef09ddbf78c3411adb69`. That DOI was not fetched as publisher HTML. [INFERENCE] the TSE article is the published version of arXiv:2102.11378; the abs page itself only says "submitted to the IEEE".

## ScoutS120Alt

Not blocked on. The title-matched primary opened, so this seat did not screen Alt's three fallbacks: (a) Google Engineering blog on mutation testing, (b) a university "Mutation Testing" chapter, (c) PIT docs on equivalent mutants. Those remain Alt's assignment. If the L1 refuses the identity correction and insists on the plan's arXiv id or DOI, the primary is the wrong paper and Alt's screen is the fallback. Dependency recorded, not waited on.

## Claims

| claim | result |
|---|---|
| Plan candidate "Petrovic, Ivankovic, Ernst", ICSE 2021, arXiv:2103.02722, DOI 10.1109/ICSE43902.2021.00068 is one openable mutation-testing paper | **falsified** (two different opened/resolved works; neither is this title; Ernst absent) |
| A primary titled *Practical Mutation Testing at Scale* opens and yields one ≤25-word located quote for the mutant-detection adequacy witness | **supported** (arXiv:2102.11378v2 HTML, quote above) |
| Tier A for that scoped witness claim | **proposed**, with the limits in the tier section |
| 87.5% kill rate is the coverage witness | **not supported** as a teach; the paper denies it is the mutation score |

## Copy check (exercised)

```
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  /tmp/scout-s120/2102.html
15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8  .../.ufo/waves/round-64/snapshots/S120.page
571600 .../.ufo/waves/round-64/snapshots/S120.page
```

Quote re-extracted from the snapshot after the copy: 22 words, id `abstract1.1` present. Exit 0.
