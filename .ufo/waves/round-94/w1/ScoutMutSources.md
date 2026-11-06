# ScoutMutSources — mutation-outcome source scout (round 94, r94-w1)

Seat: ScoutMutSources (scout, leaf, no subagent dispatch). Repo writes: none. Receipts: this directory only.
Access date for all rows: 2026-11-05 (UTC). Raw bytes kept under `.ufo/waves/round-94/w1/ScoutMutSources/`.
Quote rule: ≤25 words, located by raw HTML line of the fetched bytes (`grep -n` on the saved file).

## 1. Re-open of the L1 source — PIT "Basic concepts"

| field | observed |
|---|---|
| URL | https://pitest.org/quickstart/basic_concepts/ |
| HTTP | 200 (`curl -sS -o … -w '%{http_code}'`, re-run 2026-11-05) |
| bytes | 12155 (matches the L1 record) |
| sha256 | c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a (matches the L1 record) |
| saved as | `ScoutMutSources/pitest-basic_concepts.html` |
| version / date pin | none. Page has `<title>Basic concepts</title>` only; no "last updated", no version string (grep for `updated`, `version`, `20xx`: no hits). **The page is unpinned**; the registry row (S262) pins it by upstream commit instead. |

Located sentences (raw HTML lines of the saved file):

- L175: `<p><strong>Killed</strong> means a test caught the mutation successfully.</p>` — matches the plan's sentence exactly.
- L177: `<p><strong>Survived</strong> means the mutation was not detected by the covering test.</p>` — matches exactly.
- L166–172: outcome list `Killed / Survived / No coverage / Non viable / Timed Out / Memory error / Run error`.
- L179: `No coverage` is the same as Survived except no test exercised the line.
- Timed-out definition: L181–182, `A mutation may <strong>time out</strong> if it causes an infinite loop …`.
- Non-viable definition: L184–185, `A <strong>non viable</strong> mutation is one that could not be loaded by the JVM as the bytecode was in some way invalid.`
- Run error: L192–194.
- Equivalent mutations: L120–123 (section heading L120, `equivalent mutations` L123).

Verdict on the plan's claim: the plan's two quoted sentences reproduce byte-equal (modulo the `<strong>` markup) at L175 and L177. The timed-out class is "Timed Out" in the PIT list (L170) and "time out" in prose (L181); PIT does not define a non-viable class in terms of *timeouts*.

## 2. Registry check (`grep -n` in `corpus/SOURCES.md`, 2026-11-05)

| URL | registry row | status |
|---|---|---|
| https://pitest.org/quickstart/basic_concepts | **S262** (line 203) — kind docs, tier A, status (see row), quotes L175/L177 | **already registered** |
| https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ | **S260** (line 201) | already registered |
| https://en.wikipedia.org/wiki/Mutation_testing | **S264** (line 205), tier C, `REJECTED` | already registered (rejected) |
| https://mutmut.readthedocs.io/en/latest/ | no row; **rejected in round 90** (`corpus/lessons/round-90.md:31`, `round-90-verifier-spotcheck.md:65`) | not a row |
| https://cosmic-ray.readthedocs.io/en/latest/ (+ `concepts.html`, `theory.html`) | no row; `grep -rln cosmic corpus/` → 0 hits | **new candidate** |

Finding (registry, for the plan owner): the plan's frontier step and milestone name the PIT source "S269" and ask for a "PIT row". **S262 already holds that URL** and quotes the same two sentences; S269 is not present in the registry (the last row is S268). A second PIT row would duplicate S262 under a new id. Recommendation: no new PIT row; re-use S262 (its `used-by`/`recheck` may change in place per SOURCES rule 2) and correct the plan's "S269 / PIT row" wording by an L1 addendum before scoring. If a new row is nonetheless admitted, its `teaches` must open `supersedes S262 —` (rule 2), which is not the case here.

Second finding: S262's `anchor` says "HTML lines 175 and 177", which matches this fetch. The plan's "Non-viable and timed-out definitions" are at L181–185 (not cited by S262's anchor). The C1/C2 counter does not depend on the timed-out wording, so this is a registry completeness note only.

## 3. Candidate sources judged for corpus/QUALITY.md and CORPUS.md tiers

Tier rules read: `corpus/SOURCES.md` contract (tier A = primary/authoritative for scope, incl. maintainer docs; tier C = lead only, crowd-editable is never A). QUALITY.md criteria applied: Q12 (`source:` names S### + URL + anchor, `verified-at`, runnable `recheck`), Q03/Q53 (located quote from fetched bytes), Q42 (quote from unshaped bytes), Q56 (no "byte-exact" for shaped quotes), Q32 (exact host + path-segment match), Q70 (quote must lie outside banner/nav/subtitle), Q74 (independent generator).

### Candidate A — Cosmic Ray "Theory" and "Concepts" (new, not in registry)

- URLs: https://cosmic-ray.readthedocs.io/en/latest/theory.html and https://cosmic-ray.readthedocs.io/en/latest/concepts.html (landing `…/en/latest/` also HTTP 200, 6130 B).
- Access: 2026-11-05. HTTP 200 for `en/latest/` (6130 B), `concepts.html` (18482 B), `theory.html` (5939 B).
- sha256:
  - `en/latest/`: 6151dc53f586dc4c7b5aad76d7afaaadc773c856dbfb5a2ab403396141cbbf93
  - `concepts.html`: d4da7008e4b3bc094608dc6ece72f18d751f562c53a874d9238ee10254adae7f
  - `theory.html`: a72ab7cf9c4acdeba9cfa5138150592ac5ce4544889ac819ce3dd60bcc0db6e3
- Version/date pin: none on the page (no version string; `grep -n -i 'version|updated|copyright'` hits only a Read the Docs "last updated" database sentence, not a release pin). Stability rests on the unpinned `latest` URL: **weak**.
- Located quotes:
  - theory.html L40–41: "your tests “killed” (i.e. detected) the mutant. If the changes cause your code to simply crash, then we say the mutant is “incompetent”. If your test suite passes, however, we say that the mutant has “survived”." (≈34 words; the shorter span `we say the mutant is “incompetent”` at L41 is ≤25 words).
  - concepts.html L172–176 (heading L172 "Timeouts"): "… if a test of a mutant takes longer than the timeout, the test is killed, and the mutant is marked incompetent."
- Verdict: **admit as a tier-A row only for the cross-tool contrast; reject as support for the C1/C2 outcome vocabulary.** Reason: it is maintainer documentation (primary for Cosmic Ray), so tier A is legitimate, but its outcome model differs from PIT and from the round's counter: a timeout is folded into `incompetent` (concepts L175–176), and crash is `incompetent` (theory L40–41), so the class set is not the PIT/S269 class set the plan's §Shared counting command cites. A row would be useful as a *counter-example to the 'timeout = could-not-evaluate' rule*: this lane treats a timeout as could-not-evaluate and an incompetent (non-viable) mutant as never scored as a kill; cosmic-ray treats timeout as a kill-like incompetence. Flip to admit as a primary citation: a versioned release page (the docs pin a release) or a source file (the `cosmic_ray` repo's outcome enum) that the row can quote at a tagged revision.
- Recommended teaches (if admitted): "Cosmic Ray marks a mutant whose test times out as incompetent, not killed or survived (concepts, L172–176)" — tier A scope = the Cosmic Ray tool only.

### Candidate B — mutmut documentation index (re-probed; already rejected round 90)

- URL: https://mutmut.readthedocs.io/en/latest/ — HTTP 200, 51074 B (matches the round-90 record), sha256 07453b3fdb3b962a4cc5aff66d7614a11016c9ce0ea482654c99e17688ec9cad.
- Probes on the saved bytes (tags stripped; line numbers are from the stripped text, not raw HTML): `grep -i -c equiv` → **0** (the round-90 finding reproduces); `grep -i 'killed\|survived'` → **0 hits**; `mutation score` appears only as the "Mutation score badges" heading (stripped L545, L612); `timeout` appears only as configuration keys (stripped L504–514: `timeout_constant`, `timeout_multiplier`, with the formula `(duration_of_original_tests + timeout_constant) * timeout_multiplier`). The index does not define an outcome vocabulary.
- Verdict: **reject (unchanged from round 90).** Reason: the index names no outcome classes and no equivalent-mutant definition; the only quotable outcome-adjacent text is a config formula. Flip: a glossary or 'how it works' page under the same host that defines killed/survived (the round-90 subpage probe `howitworks/glossary` remains the route; not re-probed here beyond the index).
- Note: the plan's `mutmut` route was already rejected at round 90, so this is a re-probe, not a new candidate.

### Candidate C (checked, already in registry) — Stryker "Mutant states and metrics"

- URL: https://stryker-mutator.io/docs/mutation-testing-elements/mutant-states-and-metrics/ — HTTP 200, 27068 B (matches S260), sha256 8641c38959222238f34aba0e20d3c51919cf183bf19a53f436257614cab656da (the same fetch metadata S260 records: 27068 B).
- Located quotes (raw HTML): L12 "When at least one test failed while this mutant was active, the mutant is killed." (15 words); L14 "When all tests passed while this mutant was active, the mutant survived." (S260 cites L14 for Survived).
- Verdict: **admit (already admitted as S260).** Reason: maintainer docs (tier A for vocabulary/metrics), unpinned to a version but stable path. Flip: a page that stops defining 'killed' would change the verdict.
- Note: S260's sha256 is not recorded in the row; this seat's sha256 is for the fetch today and is not identical to the page bytes the row was opened on (the row records the byte count only), so no sha256-level claim is made against S260.

### Candidate D (checked, already in registry and rejected) — Wikipedia "Mutation testing"

- Registry S264 (line 205): REJECTED (tier C; crowd-editable tertiary page is a lead, never support). Not re-fetched in this seat. Verdict unchanged: **reject**, flip: a reviewed secondary source (survey, textbook) replacing the article.

## 4. Summary of verdicts (per URL: access date, HTTP, bytes, sha256, located quote, verdict)

| URL | access | HTTP | bytes | sha256 | located quote (raw HTML line) | verdict | reason | flip |
|---|---|---|---|---|---|---|---|---|
| pitest.org/quickstart/basic_concepts/ | 2026-11-05 | 200 | 12155 | c51d8423…bfd92b3a | L175 "Killed means a test caught the mutation successfully." | admit (already S262) | maintainer docs, tier A | page dated/versioned |
| cosmic-ray.readthedocs.io/en/latest/theory.html | 2026-11-05 | 200 | 5939 | a72ab7cf…0db6e3 | L40–41 "…we say the mutant is “incompetent”." | admit as contrast row only (tier A, Cosmic Ray scope) | timeout folded into incompetent; unpinned | versioned release page or tagged outcome enum |
| cosmic-ray…/concepts.html | 2026-11-05 | 200 | 18482 | d4da7008…adae7f | L172–176 "…the mutant is marked incompetent." | same | same | same |
| mutmut.readthedocs.io/en/latest/ | 2026-11-05 | 200 | 51074 | 07453b3f…8ec9cad | none (0 `equiv` hits) | reject (round 90 stands) | no outcome definitions | glossary/how-it-works subpage |
| stryker-mutator.io …/mutant-states-and-metrics/ | 2026-11-05 | 200 | 27068 | 8641c389…56da | L12 "When at least one test failed while this mutant was active, the mutant is killed." | admit (S260) | maintainer docs | page stops defining killed |
| en.wikipedia.org/wiki/Mutation_testing | (registry S264) | — | — | — | — | reject (S264) | tier C, crowd-editable | reviewed secondary replaces it |

Bounded claims: the Cosmic Ray row would not change any counter; it is a contrast for the timeout class. Nothing here changes the frozen C1/C2 predicates.

## 5. Risks / open items for the L1

1. The plan's "S269" PIT row duplicates **S262** (same URL, same two quotes). Correct the plan wording by addendum before scoring; do not add a second PIT row.
2. Cosmic Ray classifies timeouts as incompetent (concepts L175–176) while PIT classifies Timed Out separately (PIT L170, L181). The plan's counting command treats timeout as could-not-evaluate; that is a lane convention, not a PIT or Cosmic Ray rule. Flag it in the round-94 lesson's Gate if a row is admitted.
3. PIT's basic-concepts page carries no version/date pin; S262 pins the upstream commit `e8995cd59e3c` — a reader cannot re-fetch that commit from the page alone.
4. No seat edited any repo; the only writes are the five files in this directory (pitest, mutmut, cosmic-ray ×3, stryker HTML) and this report.

## 6. Receipts (this directory)

- `pitest-basic_concepts.html` (12155 B, sha256 c51d8423f5a75e00c7039463f8a5992ef8f1f92b994d69f67d212ff7bfd92b3a)
- `mutmut_readthedocs_io_en_latest_.html` (51074 B)
- `cosmic-ray_readthedocs_io_en_latest_.html` (6130 B), `cosmic-ray_concepts.html` (18482 B), `cosmic-ray_theory.html` (5939 B)
- `stryker-mutator_io_docs_mutation-testing-elements_mutant-states-and-metrics_.html` (27068 B)

Install record: none (only `curl` and `sha256sum`, already on the host).
