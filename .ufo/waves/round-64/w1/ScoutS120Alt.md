# ScoutS120Alt — S120 alternate screen (round 64, wave 1)

Seat: `kotoba-r64.ScoutS120Alt`. Opened 2026-10-24 (response `Date` headers 2026-10-24T03:36Z). Lane tip named by the plan: `078eec4`. No tools installed. No snapshot file written (ScoutS120 owns that write). Scratch only: `/tmp/s120alt/`. This seat did not open the plan's primary candidate (Petrović, Ivanković & Ernst, "Practical Mutation Testing at Scale").

S120, as frozen in `plans/round-64.md` § Sources: a mutation-testing source at tier A or B for the claim that mutant kills are the coverage criterion behind load-bearing-branch pinning. Contract tiers (`SOURCES-CONTRACT-v1.md`): A = primary or authoritative for that scope; B = textbook or expert write-up; C = lead only.

## Ranked recommendation

1. **Use (b) if the paper does not open.** Cornell CS 5154 slides for Ammann & Offutt, *Introduction to Software Testing*, 2nd ed., Chapter 9. Verdict: **qualifies-as-S120**. Tier **B**. Kind `docs`. It is the only opened alternate that defines mutation coverage as a test requirement whose satisfaction is killing the mutant.
2. **Use (c) if a course-slide derivative is refused.** PIT's own docs. Verdict: **qualifies-as-S120**, tier **A scoped to what PIT states** (not A for the criterion's origin). Kind `docs`. States both halves the prompt asked for: equivalent mutants, and test-suite quality as the percentage of mutants killed.
3. **Do not mint S120 from (a).** The Google Engineering blog host is gone. The live Google Testing Blog post is real and was opened; it is **rejected** as the S120 row. Tier it would carry on a different claim: **B**.

Do not cite (b) or (c) as the Google industrial study. Both are fallbacks for the criterion, not substitutes for a measurement paper.

## Verdicts

| id | URL opened | HTTP | bytes | sha256 | verdict | tier | one-line reason |
|---|---|---|---|---|---|---|---|
| (a) | `https://testing.googleblog.com/2021/04/mutation-testing.html` (Engineering host separately 404; see below) | 200 | 238321 | `68ff282ff9490b704279de15fb68f9d2526144c970f30af6889c6438f8c9651a` | rejected | B (not minted) | Author defines the mutation score and says his group did not calculate it |
| (b) | `https://www.cs.cornell.edu/courses/cs5154/2021sp/resources/MutationTesting.pdf` | 200 | 742226 | `4f6b0885ded2d70aee8b3d9fe17b53d06660751985673b40c372a38bdfa393ba` | qualifies-as-S120 | B | Chapter slides define Mutation Coverage as one requirement: kill the mutant |
| (c) | `https://pitest.org/` and `https://pitest.org/quickstart/basic_concepts/` | 200 / 200 | 12023 / 12155 | `b0c7e050…2bf10cc` / `c51d8423…bfd92b3a` | qualifies-as-S120 | A for PIT's stated meanings | Maintainer docs: quality is percent killed; equivalent mutants do not change behavior |

Full hashes for (c) are in § (c).

## (a) Google Engineering blog — unfindable; Testing Blog opened and rejected

**Engineering host.** `GET https://engineering.googleblog.com/` → HTTP 404, `content-type: text/html; charset=UTF-8`, 2717 bytes, sha256 `947e9520a31d1ef116c75dde38cc05f4057c0f7237c8325c8d5128afdd20232e`. Body title is Blogger's missing-blog page: "Blog não encontrado" ("O blog que você está procurando não foi encontrado."). No post to quote. [INFERENCE] This is a dead Blogger blog, not a redirect to a successor Engineering blog. Not re-fetched.

**developers.googleblog.com search.** `GET https://developers.googleblog.com/search/?query=mutation%20testing` → HTTP 200, 77618 bytes, sha256 `e058bd29b6534dce671870b09a77453be52240f05f3915211464cfd6d0f05366`. Page says "3 results". None is a mutation-testing practice post. Titles and paths:

- 2026-09-15, "Build zero-trust AI agents that judge intent, not just syntax" — `/build-zero-trust-ai-agents-that-judge-intent-not-just-syntax/`
- 2026-08-17, "Build zero-trust AI agents with Google's Agent Development Kit" — `/build-zero-trust-ai-agents-with-googles-agent-development-kit/` (summary uses "mutate" for agents that change production state)
- 2026-07-16, "Building scalable AI agents with modular prompt transpilation" — `/building-scalable-ai-agents-with-modular-prompt-transpilation/`

**The practice post that does exist** is the Google Testing Blog, not the Engineering blog. `GET https://testing.googleblog.com/2021/04/mutation-testing.html` → HTTP 200, no redirect, `text/html; charset=UTF-8`, 238321 bytes, sha256 `68ff282ff9490b704279de15fb68f9d2526144c970f30af6889c6438f8c9651a`. Header `last-modified: Wed, 21 Oct 2026 16:23:15 GMT` (Blogger shell; not treated as a content revision). In-page byline: "By Goran Petrovic". In-page date: "Monday, April 12, 2021".

Designated quote (13 words), section "From Prototype To Launch", first paragraph, contiguous:

> did not calculate the Mutation score, the ratio of mutants detected by tests

The clause immediately before those words is "the hackathon crew". The same sentence goes on to call that ratio "a prominent metric in the research literature and the holy grail of evaluating test quality" and says the crew "just enumerated live mutants" instead. A 24-word slice of the literature-praise half, without the negation, would mis-cite the page.

Second located sentence, same post, after the first `checkout` mutant table (22 words):

> If a test fails, we say it kills the mutant, and if no tests fail, we say that the mutant is alive.

Later, same post: unproductive mutants are ones for which "writing tests for those mutants would make the test suite worse, not better." "Coverage" on this page is line coverage used to pick which tests to run against a mutant, not the kill ratio.

**Verdict: rejected** as S120. Kind would be `docs`. Tier B is what an expert-narrative row would carry, and it is not minted here. The page does not teach "kills are the coverage you pin." It defines that score and declines it, then teaches suppression of unproductive mutants. Citing the score clause as Google's criterion would be the wrong-authority failure (QUALITY Q23 / M24).

Flip that would change this: a sentence on this URL that states Google uses the mutation score as the coverage criterion. None found in the extracted article (3427 words). A different, non-S120 row could still teach "at most one mutant per line; arid nodes are not test targets" from this page at tier B.

## (b) University chapter material — qualifies, tier B (recommended)

**Opened chapter artifact.** Cornell CS 5154, Spring 2021, instructor Owolabi Legunsen. Course page `GET https://www.cs.cornell.edu/courses/cs5154/2021sp/` → HTTP 200, 24424 bytes, sha256 `7e6cd89207a9366d7623b69c44c14ae7d601fb9ea88835dfe39d0ef65e112ba7`. Title "CS 5154: Software Testing". Schedule rows 4/5 and 4/7 are both "Mutation Testing" and both link `resources/MutationTesting.pdf` (4/7 also links `resources/mutation.zip`, not fetched).

**PDF.** `GET https://www.cs.cornell.edu/courses/cs5154/2021sp/resources/MutationTesting.pdf` → HTTP 200, `application/pdf`, 742226 bytes, sha256 `4f6b0885ded2d70aee8b3d9fe17b53d06660751985673b40c372a38bdfa393ba`, `Last-Modified: Wed, 07 Apr 2021 05:07:45 GMT`. Directory listing `…/resources/` is HTTP 403, 289 bytes, sha256 `c6671e8ec2a6ec510bfaf19035a021d9017384c863aa10bf9a70c40b0b7f61c9` ("You don't have permission to access this resource."); the PDF URL itself is 200.

Slide 1 text: "CS 5154 / Mutation Testing / Owolabi Legunsen" and "The following are modified versions of the publicly-available slides for Chapter 9 in the Ammann and Offutt Book, 'Introduction to Software Testing'". Footer on the coverage slide: "Introduction to Software Testing, edition 2 (Ch 9) © Ammann & Offutt" printed page 12. Slide title: "Syntax-Based Coverage Criteria".

Designated quote (15 words, punctuation and the element-of glyph not counted), printed slide 12. `pdftotext` joined "M,TR" across the line break; the quote restores that one layout space and no words:

> Mutation Coverage (MC): For each m ∈ M, TR contains exactly one requirement, to kill m.

That is the mutant-kills-mean-coverage claim, as a coverage criterion: one requirement per mutant, and the requirement is to kill it. Same deck, slide "Some types of Mutants" (not the designated quote): "Equivalent mutant : No test can kill it (same behavior as original)" (11 words).

**Verdict: qualifies-as-S120. Tier B. Kind `docs`.** Textbook chapter material via a named university course, which is tier B (textbook), not A: these are modified course slides, not the book and not an original paper. Bound the entry must keep: the slides also say an equivalent mutant is one no test can kill, so a survivor is not automatically a missing pin.

**Screened and not used as (b):**

- `GET https://cs.gmu.edu/~offutt/softwaretest/` (the URL printed on slide 1) → HTTP 200 after 1 redirect, final URL `https://cs.gmu.edu/`, 55514 bytes, sha256 `2230c7db575b479b320002ebb9b3f06ae771d6407af9263849c8e81e77249214`. That is the department front page, not the book. Rejected as a chapter source.
- `GET https://www.albany.edu/faculty/offutt/softwaretest/contents.html` → HTTP 200, 15142 bytes, sha256 `1a2b95fecd645eb50119b34e8866b5713a6d2eebe33db93b033589319565d0ce`, `Last-Modified: Fri, 06 Dec 2019 21:16:53 GMT`. Table of contents only. It names §9.1.2 "Mutation Testing" and §9.2.2 "Program-based Mutation" under Chapter 9 "Syntax-based Testing". No chapter prose, so no quote and no row.

## (c) PIT docs — qualifies, tier A for PIT's own statements (second)

Two pages, same docs set, both `Last-Modified: Wed, 03 Jun 2026 08:45:37 GMT`.

| page | HTTP | bytes | sha256 |
|---|---|---|---|
| `https://pitest.org/` | 200 | 12023 | `b0c7e0505c51c95b596060ef27babbce08e72d5aaf4557eb002c2637d2bf10cc` |
| `https://pitest.org/quickstart/basic_concepts/` | 200 | 12155 | `c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a` |
| `https://pitest.org/faq/` (screened, not the row) | 200 | 20845 | `ccf6ac493d6935e2f0a90b716254c57024973d5e2bf1bf3c1e8e60b9772629c1` |

Designated quote (14 words), homepage section "What is mutation testing?":

> The quality of your tests can be gauged from the percentage of mutations killed.

Located equivalent-mutant quote (10 words), `basic_concepts` heading "Equivalent Mutations" (the paragraph says mutations that do not behave differently "are referred to as equivalent mutations"):

> not all mutations will behave differently than the unmutated class

Same page, "Running the tests" (11 words), the operational line for a covered-but-unpinned branch:

> Survived means the mutation was not detected by the covering test.

The FAQ was fetched and searched for "equivalent"; no match. Its nearest heading is "I have mutations that are not killed but should be", about `finally`-block copies. Not a source for equivalent mutants.

**Verdict: qualifies-as-S120. Tier A, scope-limited. Kind `docs`.** A is right for "what the PIT maintainer says a kill and an equivalent mutant are" (official docs / maintainer statement). It is not A for the origin of the criterion, and the homepage's "gold standard" sentence is promotional — do not put that sentence in `teaches`. Ranked under (b) because S120's scope is the coverage criterion, which the chapter defines and PIT only restates as a product metric.

## Sweep (this seat)

Question: which alternate can be S120 if the named paper fails? Where: the three named classes (Google engineering/practice blog, a university mutation-testing chapter, PIT's equivalent-mutant and quality docs). Date: 2026-10-24.

Identified 11 URLs. Screened 11 (all fetched). Included 2 as qualifying ((b) PDF, (c) homepage + basic concepts, counted as one candidate). Excluded 6 from a row: Engineering host 404, developers-blog search (3 false hits, one URL), GMU book URL (redirects to the department home), Albany contents (TOC only), Cornell `resources/` listing (403, PDF still 200), PIT FAQ (no equivalent-mutant text). Rejected after opening: the Testing Blog post, as the S120 claim. Stop: each of (a), (b), and (c) has a located quote and a verdict; no further university or PIT page was required.

## Draft row (not applied; L1 copies only if the paper fails)

```
| S120 | Cornell CS 5154 Spring 2021 — Mutation Testing slides (modified from Ammann and Offutt, Introduction to Software Testing, 2nd ed., ch. 9) — https://www.cs.cornell.edu/courses/cs5154/2021sp/resources/MutationTesting.pdf | docs | B | mutation coverage as the requirement to kill each mutant | slide Syntax-Based Coverage Criteria, printed p.12; PDF last-modified 2021-04-07; linked from the course page 4/5 and 4/7 rows | Mutation coverage is one requirement per mutant, and that requirement is to kill it; an equivalent mutant is one no test can kill | queued | 2026-10-24 | 365d | — |
```

If (b) is refused and (c) is used instead, replace that row's source/anchor/teaches with the homepage quality quote plus the basic_concepts equivalent-mutant anchor, tier A, and keep the scope words "what PIT states", not "the criterion's origin".

## Unresolved

- The plan's paper (authors, venue, whether it says "kills mean coverage") was not opened here.
- Testing Blog `last-modified` is 2026-10-21 while the byline date is 2021-04-12. Single fetch; byte-stability not re-checked.
- Slide glyph for "element of" is whatever `pdftotext` emitted (``), not re-derived from the font.
- `resources/mutation.zip` (course code, 4/7 row) was not fetched.

## Claims

Supports: plan § Sources needs an opened A/B source for mutant-kills-mean-coverage; (b) and (c) can be that source; (a) as an Engineering-blog post cannot. Does not support: treating the Testing Blog as an endorsement of mutation score; treating PIT's "gold standard" line as the criterion's definition; treating these slides as the Google study.
