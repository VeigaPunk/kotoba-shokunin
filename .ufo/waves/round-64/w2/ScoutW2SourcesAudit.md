# ScoutW2SourcesAudit — S120 exclusion audit

Seat: `kotoba-r64.ScoutW2SourcesAudit-2`. Date: 2026-10-24. Measured data tip: `c019919c97ab5fe98e87a7754b4449ea4e699c99`.

Axes: literal quotation fidelity; exclusion-reason fidelity; scope-limited tier fidelity; coverage of every named exclusion. Read-only investigation, except this report; no subagents, git/jj writes, tests, builds, or installs. Scratch: `/tmp/r64-sources-w2-7uti6aa8/`.

## Findings

1. **F1 — Landed sweep falsely calls the alternates unscreened (high confidence).** `corpus/SOURCES.md:282-284` at the measured tip says ScoutS120Alt's Google/university/PIT fallbacks “stay unscreened because the title match succeeded.” The same commit's `.ufo/waves/round-64/w1/ScoutS120Alt.md:17-21,104` records HTTP/body/hash evidence, **11 URLs screened**, Cornell/PIT qualifying, and Google Testing Blog opened and rejected. `ScribeSOURCESRow.md:320-322,490-492` repeats the unscreened assertion. My refetch reproduced **9/11 complete body hashes**, including Google, Cornell, and both included PIT pages. [INFERENCE] The primary-only `8/8/1/7` tally need not include the separate alternate sweep, but “not counted here” cannot honestly mean “unscreened.” Narrow correction: describe the two sweeps separately.

2. **F2 — Google's 13-word quotation is exact; treating it as a disqualifying refusal changes the question (medium confidence on relevance; high on bytes/context).** `ScoutS120Alt.md:39` is literally correct, including capitalization. Its context is a historical observation about the **hackathon prototype**, not a declaration that mutant kills cannot guide tests. The report's `:49-51` moves from that observation to “does not teach” the pinning criterion, and makes Google using an aggregate mutation score the required flip. Yet the frozen plan `plans/round-64.md:165-169` asks for the mutant-kills-mean-coverage method, not proof Google computes an aggregate score. The page positively teaches “The more injected bugs the tests catch, the better they are” and describes developers adding a test and seeing the mutant killed. Moreover, the **accepted** S120 paper explicitly calls computing the full mutation score infeasible and non-actionable (`S120.page:424-434`). [INFERENCE] Agree with rejecting this blog as evidence that Google computes/uses an aggregate mutation-score criterion; disagree that the refusal sentence alone disqualifies it as an expert account of using individual mutant kills as test goals. This is contextual/relevance overreach, **not a fabricated quotation**. Selecting the stronger paper remains defensible.

3. **F3 — Exclusion (d) prints an incomplete title and understates the Bitcoin source (high confidence on title/content; medium on scope judgment).** `corpus/SOURCES.md:262-264` / `ScribeSOURCESRow.md:300-302` quote the title as “Mutation Testing in the Wild: Challenges and Lessons from Bitcoin”; the publisher record and PDF title end **“Bitcoin Core”**, without an ellipsis. The actual source is Bruno Ely Reis Garcia, SAST 2026, pp. 274–276, DOI `10.5753/sast.2026.30421`. Its abstract explicitly claims mutation testing is “tractable even on large, complex codebases”; its introduction says a surviving mutant signals a potential test-suite blind spot, and §2.3 defines equivalent mutants. [INFERENCE] Excluding an unopened, redundant, single-system report is reasonable. Calling it devoid of a scale claim for this method is not supported by those bytes; it lacks Google's multi-project deployment evidence, not a scale discussion or the pinning/equivalence concepts. This does not require admitting another row.

**No Cornell/PIT tier inflation found.** Cornell **B** and PIT **A for PIT's own statements only** fit the actual scope rule (`/home/vgpnk/Projects/shokunin/CORPUS.md:93-98`). Google **B** is also a defensible conservative expert-write-up tier.

## Google quotation: exact bytes and context

Opened [Google Testing Blog — Mutation Testing](https://testing.googleblog.com/2021/04/mutation-testing.html). HTTP 200, 238321 B, SHA-256 `68ff282ff9490b704279de15fb68f9d2526144c970f30af6889c6438f8c9651a`: **identical to wave 1**. Byline Goran Petrovic; date April 12, 2021.

The native web-reader omitted the body because it lives in a `script type='text/template'`; I opened raw HTML and parsed that template, rather than treating the incomplete reader output as absence. Source line 1138, heading **From Prototype To Launch**, first paragraph (HTML tags removed; text otherwise unchanged):

> I quickly realized that the hackathon crew did not calculate the Mutation score, the ratio of mutants detected by tests, which is a prominent metric in the research literature and the holy grail of evaluating test quality, but just enumerated live mutants.

The designated substring is present exactly and has 13 whitespace-separated words:

> did not calculate the Mutation score, the ratio of mutants detected by tests

The preceding narrative calls the hackathon result a prototype and describes a year of inactivity before the author's research. The same article first teaches:

> The more injected bugs the tests catch, the better they are.

Later, in the service/code-review workflow:

> when they write a test to kill a mutant, they want to see the mutant killed.

The blog also explains unproductive mutants and equivalent cache-removal behavior. [INFERENCE] An aggregate score, an individual kill witness, and line coverage are different concepts; declining the first does not negate the second. Do not cite the literature-praise clause as proof Google calculates a score; do not erase the article's individual-kill workflow either.

## Seven primary-sweep exclusions: individual dispositions

These are the seven **works** in `ScribeSOURCESRow.md:290-310`, landed at `corpus/SOURCES.md:252-272`. They are not ScoutS120Alt's six excluded URLs plus one rejected blog. Agree/disagree judgments below are [INFERENCE] from the stated scope and observed evidence, not claims of independently observing wave-1 browsing.

| Exclusion | Disposition | Observed source bytes / qualification |
|---|---|---|
| **(a) Just et al., FSE 2014, real-fault validity** | **Agree** with different empirical target and no new row from an allegedly unopened work; no mis-tier stated. | [Author abstract](https://homes.cs.washington.edu/~mernst/pubs/mutation-effectiveness-fse2014-abstract.html), 200 / 4136 B / SHA `3fd406c3d19dbba6c6c164cb875f26bc1aab9a92130708a4f8209e4a76d286d5`, says the results show a statistically significant relationship between mutant and real-fault detection independently of code coverage. Crossref identifies the six named authors, FSE 2014, pp. 654–665, DOI `10.1145/2635868.2635929`. This is not evidence that the work lacks basic mutation-method framing; only that its principal empirical question differs. Contract rule 2 is append-only, not a blanket prohibition on adding a separately scoped source row. |
| **(b) Petrović/Ivanković, State of Mutation Testing at Google** | **Agree** with preferring the later report for the chosen Google-deployment scope; “superseded” is a curation choice, not proof the earlier study is invalid. | [Google Research record](https://research.google/pubs/state-of-mutation-testing-at-google/), 200 / 145543 B / SHA `b0eeeb8698fcf86376ad994d896107832ee11661f12091bf0b88120c90b05847`, explicitly says 6,000 engineers. Its linked PDF is 419943 B / SHA `c128ccd374906ade3e4e885dbfb685bc7268ee92ccf4c8d71f678b17e3cdbcca`. The accepted S120 snapshot `:300-302` says more than 24,000 developers and more than 1,000 projects. Crossref confirms ICSE-SEIP 2018, pp. 163–171, DOI `10.1145/3183519.3183521`. No numerical misquote found in the exclusion. |
| **(c) Jia/Harman survey** | **Agree** with **B for this secondary-survey scope** and redundancy rationale. | Crossref title/author record, 200 / 28953 B / SHA `7b7779ee631d8c52cb8a736f48ee955601e44d11dd7095d67a76a4d09f0b5a2a`, confirms title, Yue Jia/Mark Harman, TSE, 649–678, 2011, DOI `10.1109/TSE.2010.62`. Accepted snapshot `:1901-1902` cites `[28]` for the equivalent-mutant problem, and `:2186-2189` identifies exactly this survey. Contract `CORPUS.md:95-96` explicitly places surveys in B. Full survey body not opened by this seat; no claim to revalidate all its contents. |
| **(d) Bitcoin experience report** | **Disagree in part — F3.** Correct single-system/unopened exclusion can stand; exact title and scale characterization need correction. | [Publisher](https://sol.sbc.org.br/index.php/sast/article/view/45883), 200 / 22760 B / SHA `6b56b6d200e87503a23cc7a4a683e6c42ed13a10730421a43cfbc604da8a6c89`; [PDF](https://sol.sbc.org.br/index.php/sast/article/download/45883/45644), 200 / 478212 B / SHA `e598469578758cf223c3b59a50b3a764e5e91acd2df2ee361f579c0fe4b843a4`. PDF p.1 title ends “Bitcoin Core”; abstract discusses scalability; introduction explicitly calls survivors potential blind spots; p.2 §2.3 states equivalent mutants have the same behavior and cannot be killed. This is not an unrelated subject, although it is not a Google multi-project study. |
| **(e) Does Mutation Testing Improve Testing Practices?** | **Agree** that its main empirical question differs and an unopened alternate need not become a row; qualification: it also directly teaches the method. | [Author record](https://homes.cs.washington.edu/~rjust/publ/PetrovicIFJ2021b-abstract.html), 200 / 2363 B / SHA `e15a815a81efc326c2dd8ef8aba55ef349a91bb97482e5cf03055fdea3300e36`; [PDF](https://homes.cs.washington.edu/~rjust/publ/mutation_testing_practices_icse_2021.pdf), 200 / 762226 B / SHA `e8395421df15432e445f472fafe60b442812413fc9c694d4f351afb763bdf401`. Same four authors, ICSE 2021, 910–921; Crossref DOI `10.1109/ICSE43902.2021.00087`. Abstract investigates nearly 15 million mutants' effects on developer behavior and fault coupling. §II also makes surviving mutants concrete test goals. Thus “not selected” is honest; “cannot ground the method” would not be. |
| **(f) arXiv:2103.02722** | **Agree**, wrong work. | [arXiv record](https://arxiv.org/abs/2103.02722), 200 / 39320 B / SHA `b9074417b0916f55454fcb238218756660cfda5dd5f950d3d55a5d8174300bc1`, title “A Markov jump process associated with the matrix-exponential distribution”, Oscar Peralta, math.PR, March 3, 2021. Exact wave-1 body hash reproduced. |
| **(g) DOI 10.1109/ICSE43902.2021.00068** | **Agree**, wrong work. | [Crossref record](https://api.crossref.org/works/10.1109%2Ficse43902.2021.00068), 200 / 8977 B / SHA `950a2b5056cd9bbe3a2ddac519ed0c9ba68dece3bf603c5b8894feb3b5921532`, title “An Empirical Study on Deployment Faults of Deep Learning Based Mobile Applications”, Zhenpeng Chen and six coauthors, ICSE 2021, 674–685. [Its preprint](https://arxiv.org/abs/2101.04930), 200 / 45327 B / SHA `05c0c128a8f7fef7be6a9e778c451269ee363d7b7e52bd06105cb7e436ff29e3`, independently matches title/authors/domain. |

## Alternate sweep: every exclusion/rejection and both admitted fallbacks

All eleven URLs below were reopened independently. `exit` is curl's process exit, distinct from HTTP status; curl was not invoked with `--fail`. Body hashes are Python `hashlib.sha256` of saved response bytes.

| URL/candidate | HTTP / bytes / exit | SHA-256 | Audit |
|---|---|---|---|
| [Engineering Blogger host](https://engineering.googleblog.com/) | 404 / 2718 / 0 | `ec47bb53c8d293c8efb7d6fa79e4d00273123c6089e083937f55718653f64938` | **Agree** exclude this endpoint: body says “Blog não encontrado”; no redirect. W1 had 2717 B / a different hash. Current response alone does not establish the historical hash was wrong or that every Google engineering publication is gone. |
| [Developers Blog search](https://developers.googleblog.com/search/?query=mutation%20testing) | 200 / 77618 / 0 | `d9b47a46a321291fb9cae7e22dcf9e5ecf582ee064d2bd2acbe13e30cd9046ab` | **Agree** exclude those search results: body says 3 results; titles concern zero-trust agents (Sept.15/Aug.17) and modular prompt transpilation (July16), exactly the three W1 titles, not a mutation-testing practice post. Length matches W1; whole-body hash differs. No inference of global nonexistence. |
| [GMU book URL](https://cs.gmu.edu/~offutt/softwaretest/) | 200 / 55514 / 0 | `2230c7db575b479b320002ebb9b3f06ae771d6407af9263849c8e81e77249214` | **Agree**: one redirect to `https://cs.gmu.edu/`, a department home, not chapter prose. W1 hash identical. |
| [Albany contents](https://www.albany.edu/faculty/offutt/softwaretest/contents.html) | 200 / 15142 / 0 | `1a2b95fecd645eb50119b34e8866b5713a6d2eebe33db93b033589319565d0ce` | **Agree**: contents lines 180–186 name chapter 9, §9.1.2 and §9.2.2 but do not teach their prose. W1 hash identical. A contents listing is a lead, not a chapter quotation. |
| [Cornell directory listing](https://www.cs.cornell.edu/courses/cs5154/2021sp/resources/) | 403 / 289 / 0 | `c6671e8ec2a6ec510bfaf19035a021d9017384c863aa10bf9a70c40b0b7f61c9` | **Agree** exclude listing, **not** the PDF. W1 hash identical. |
| [PIT FAQ](https://pitest.org/faq/) | 200 / 20845 / 0 | `ccf6ac493d6935e2f0a90b716254c57024973d5e2bf1bf3c1e8e60b9772629c1` | **Agree** for the equivalent-mutant-definition scope: zero case-insensitive `equivalent` occurrences in parsed text; nearest survivor heading addresses duplicated `finally` blocks, not semantic equivalence. W1 hash identical. |
| [Google Testing Blog](https://testing.googleblog.com/2021/04/mutation-testing.html) | 200 / 238321 / 0 | `68ff282ff9490b704279de15fb68f9d2526144c970f30af6889c6438f8c9651a` | **Quote/context bytes agree; rejection rationale partly disagree — F2.** B is reasonable for an expert narrative; not evidence Google uses an aggregate score. |
| [Cornell course](https://www.cs.cornell.edu/courses/cs5154/2021sp/) | 200 / 24424 / 0 | `7e6cd89207a9366d7623b69c44c14ae7d601fb9ea88835dfe39d0ef65e112ba7` | Supporting identity: instructor Owolabi Legunsen, 4/5 and 4/7 both link the same slides. W1 hash identical. |
| [Cornell PDF](https://www.cs.cornell.edu/courses/cs5154/2021sp/resources/MutationTesting.pdf) | 200 / 742226 / 0 | `4f6b0885ded2d70aee8b3d9fe17b53d06660751985673b40c372a38bdfa393ba` | **Agree qualify, B.** Modified textbook-course material, not an original industrial study. W1 hash identical. |
| [PIT homepage](https://pitest.org/) | 200 / 12023 / 0 | `b0c7e0505c51c95b596060ef27babbce08e72d5aaf4557eb002c2637d2bf10cc` | **Agree qualify, A for PIT's own statements only.** W1 hash identical. |
| [PIT basic concepts](https://pitest.org/quickstart/basic_concepts/) | 200 / 12155 / 0 | `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a` | **Agree same limited A.** W1 hash identical. |

### Cornell B: located evidence

PDF slide 1 states the material is “modified versions of the publicly-available slides for Chapter 9” of Ammann/Offutt. Printed slide **12**, **Syntax-Based Coverage Criteria**, states mutation coverage has one requirement per mutant: kill it. The slide-10 equivalent-mutant statement is “No test can kill it (same behavior as original).”

`pdftotext -layout` output at `cornell.txt:177-179`:

```text
             Syntax-Based Coverage Criteria
      Mutation Coverage (MC) : For each m  M,TR contains
      exactly one requirement, to kill m.
```

The W1 designated quote has the same words; its conventional `∈` glyph and spacing are a presentation normalization of the PDF's symbol-font extraction, not a changed coverage criterion. [INFERENCE] B is honest under the contract's explicit textbook/strong-secondary clause. The equivalent-mutant caveat is retained; no claim that every survivor is automatically a missing assertion is warranted.

### PIT A: located evidence and bound

Homepage source line 114, **What is mutation testing?**:

> The quality of your tests can be gauged from the percentage of mutations killed.

Basic-concepts source `:120-123`, **Equivalent Mutations**, contains the exact W1 ten-word quote across a newline:

> not all mutations will behave differently than the unmutated class

Basic-concepts `:177`, **Running the tests**:

> Survived means the mutation was not detected by the covering test.

All three normalized-text substring checks returned `True`. [INFERENCE] The official tool's definitions support A **for what PIT documents**, not the criterion's origin, empirical superiority over every other coverage measure, or this lane's implementation. W1 correctly disclaims its promotional “gold standard” language. Additional caution: the docs also use “equivalent” for behavior outside a team's test scope (`:145-152`); do not silently promote that pragmatic usage into a universal mathematical-equivalence theorem. This is a bound on reuse, not a defect in the stated tier.

## Captured command evidence

Commands were executed with `subprocess.run(..., capture_output=True)`; the following output and process exit values were captured, not inferred. SHA values above were computed from saved bytes with `hashlib`, not claimed to be output from an unrun `sha256sum` command.

```text
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:corpus/SOURCES.md
exit 0 bytes 127553 sha256 975cbce9d2f23291b34389db1419c7b2698825c5dddc8921063e6202824fc847
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/w1/ScribeSOURCESRow.md
exit 0 bytes 40536 sha256 d7f6b8d176a8f5df5324d1d6659ad25493cc2c5202c4122e176c52a342e78a9e
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/w1/ScoutS120Alt.md
exit 0 bytes 13770 sha256 ae7235995548e145e033ccbe1dc054967e157fdf5c6992607b0f5a3e334f0742
$ git show c019919c97ab5fe98e87a7754b4449ea4e699c99:.ufo/waves/round-64/snapshots/S120.page
exit 0 bytes 571600 sha256 15963c3e67b577182fb40318960ca654d70951ddc8827529de82d7f563cc79e8

$ curl -sS -L --max-time 35 -D /tmp/r64-sources-w2-7uti6aa8/google.hdr -o /tmp/r64-sources-w2-7uti6aa8/google.body -w 'HTTP=%{http_code} bytes=%{size_download} type=%{content_type} redirects=%{num_redirects} effective=%{url_effective}' https://testing.googleblog.com/2021/04/mutation-testing.html
HTTP=200 bytes=238321 type=text/html; charset=UTF-8 redirects=0 effective=https://testing.googleblog.com/2021/04/mutation-testing.html
exit=0
hashlib.sha256(body)=68ff282ff9490b704279de15fb68f9d2526144c970f30af6889c6438f8c9651a

$ pdftotext -layout cornell_pdf.body cornell.txt
exit 0
$ pdftotext -layout bitcoin_pdf.body bitcoin_pdf.txt
exit 0
$ pdftotext -layout state_pdf.body state_pdf.txt
exit 0
$ pdftotext -layout practices_pdf.body practices_pdf.txt
exit 0

refusal_quote_equal True words 13
PIT home exact True
PIT equivalent exact True
PIT Survived exact True
PIT FAQ equivalent occurrences 0
W1 body hashes reproduced: 9 of 11
```

The abbreviated `pdftotext` lines above use the actual scratch basenames; executions supplied their absolute `/tmp/r64-sources-w2-7uti6aa8/` paths. Download receipts with full commands/HTTP/exit/hash are also in scratch `downloads.json`, `paper-downloads.json`, `more-downloads.json`, `final-downloads.json`, `practices-download.json`; durable key outputs are preserved here.

## Limits / remaining unknowns

- Wave-1 access history is observed through committed reports, not retrospectively reconstructed from today's fetches. “Not opened this round” in the seven-work log cannot be independently proven just by reopening it now.
- Crossref's first requests for the State/incorrect-ICSE DOI endpoints returned HTTP 429, empty bodies, curl exit 0. Encoded-DOI requests then returned the 200 records cited above. The guessed Google Research practices URL returned 404; the linked author PDF and Crossref record resolved the work. No missing source blocked a disposition.
- Cornell/PIT/Google bodies and all seven primary exclusions received an individual disposition; the survey was checked via metadata plus its actual citation in S120, not via its full text.
- `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was absent when read. No installation/update was needed or performed; pacman guard untouched.
- No exported code contract or symbols are at issue; this is a Markdown/HTML/PDF source audit, not an LSP definition/reference investigation. Literal searches locate evidence only. No C1/C2 behavioral result is asserted.

Report: `.ufo/waves/round-64/w2/ScoutW2SourcesAudit.md`
