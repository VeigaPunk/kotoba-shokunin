# SOURCE_ROW — round 89 §2b — seat ScoutSource

Opened 2026-11-05. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Two rows proposed for `corpus/SOURCES.md` (owned by ScribeSources): **S258** (external, paper) and
**S259** (own-work). Both rows are grounded in bytes this seat actually opened; no row is proposed
from memory.

---

## S258 — external, paper

| field | value |
|---|---|
| id | S258 |
| title-canonical URL | https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/ (Nosek BA, Ebersole CR, DeHaven AC, Mellor DT, "The preregistration revolution", *PNAS* 115(11):2600–2606, 2018-03; DOI https://doi.org/10.1073/pnas.1708274114; PMID 29531091; PMCID PMC5856500) |
| kind | `paper` |
| tier | **A** — scoped to *the preregistration-before-data principle and the confirmatory/exploratory distinction as stated by the paper's own authors*. Tier A is confined to that scope: the paper is the primary source for what preregistration is claimed to do; it is **not** authoritative for this lane's freeze-gate mechanics, which are lane-local (S259). Europe PMC metadata records `isOpenAccess: N` for the publisher's version, so the tier rests on the PMC author-manuscript text actually read here, not on an open-access licence claim. |
| scope | The preregistration-methods grounding for "the design/analysis plan is committed before outcomes are observed, so a prediction is separated from a postdiction", and for the confirmatory-vs-exploratory label the C1 freeze gate mechanizes |
| anchor | §Preregistration Distinguishes Prediction and Postdiction (HTML line 1451) and §Preregistration in Practice → Challenge 5: Many Experiments (HTML line 1472) of the saved bytes; revision = PMC5856500, PNAS 115(11), 2018-03-01 |
| access date | 2026-11-05 (fetch 2026-11-05T11:08:22Z) |
| sha256 of saved bytes | `ee0d0560901a0e65c6b8079e2eaf1d79c049c74597ce3f374b4e19bce0ba51f9` (196,972 B, `text/html; charset=utf-8`) |
| saved bytes | `.ufo/waves/round-89/w1/ScoutSource/s258.html` |
| text-projection sha256 | `dde98a5ebe159b7a4a4e07b52ce40e9d65e16d6c7b12f943d61c68ae1fcf3efc` (tags stripped, whitespace collapsed, 61,093 chars) — the fetch-stable digest; the raw-byte digest varies between fetches only because NCBI injects a per-session `ncbi_phid` meta tag and a `csrfmiddlewaretoken` hidden input (two differing lines, article text identical; see `receipts.txt`) |
| status | proposed `mined` (cited by `corpus/knowledge/freeze-gate-round89.md`) |
| recheck | 365d |

### Candidate located quotes (≤ 25 words each)

**(a) confirmatory vs exploratory — §Preregistration in Practice → Challenge 5: Many Experiments, HTML line 1472 of the saved bytes**

> "researchers can achieve confirmatory research via replication. All initial experiments are treated as exploratory research."

(15 words; the surrounding sentence continues "When something of interest is observed, then the
initial design and analysis script become the preregistration for testing a prediction by running
the experiment again.")

Alternative candidate for the same leg, §Preregistration in Practice → Challenge 7: Few a Priori
Expectations, HTML line 1478:

> "Preregistration benefits both exploratory research and testing predictions during the iterative research process."

(13 words)

**(b) timing of registration relative to outcomes — §Preregistration Distinguishes Prediction and Postdiction, HTML line 1451 of the saved bytes**

> "Preregistration of an analysis plan is committing to analytic steps without advance knowledge of the research outcomes."

(17 words)

### `teaches` proposal (one line)

Preregistration is a *pre-outcome commitment* — the plan is fixed before outcomes are seen, so
confirmatory tests stay separable from exploratory ones; a control whose expectation cannot be
observed under that commitment is not a confirmation.

### Route ledger (honest record of the three prescribed routes)

| route | URL | result |
|---|---|---|
| (a) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5813543/ | **HTTP 200 but the wrong article** — the served page is "STOREKEEPER RELATED1/G-Element Binding Protein (STKR1) Interacts with Protein Kinase SnRK1", 307,298 B, sha256 `20574435edee839a38369b17197395d194b68eedde578fda80de3e77ea2939b8`. The PMC id in the assignment does **not** carry the preregistration paper. Route (a) therefore does not yield S258. |
| (b) | https://www.pnas.org/doi/10.1073/pnas.1708274114 | **HTTP 403** (publisher bot-block), 5,686 B, sha256 `8c0313664a3409474dea8c3abe00f0bcad7e564927585aeb06f716331f2a8079` |
| (c) | https://doi.org/10.1073/pnas.1708274114 | **HTTP 403** (redirects to `https://pnas.org/doi/full/10.1073/pnas.1708274114`), 5,697 B, sha256 `4d0e6ca489153b6f1094a827593baac19d1f0e6886cf03ecc4958492f86bb36b` |
| (a′) | https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/ | **HTTP 200** — the paper, resolved from the DOI via the NCBI idconv API (`pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=10.1073/pnas.1708274114&format=json` → `"pmcid":"PMC5856500"`). This is the route that produced the saved bytes. |

No route was fabricated and no quote was taken from a source this seat did not open. The correct
PMCID for the assigned DOI is **PMC5856500**, not PMC5813543 — recorded here so the row's URL is
correct and so the plan's route list can be amended by the owner if it is ever reused.

---

## S259 — own-work

| field | value |
|---|---|
| id | S259 |
| own-work locator | repo path `corpus/lessons/round-88-verifier-spotcheck.md` at commit `a5b3b15c00b1de5db321e4226a0a7db17340e605` (lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; command `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show a5b3b15c00b1de5db321e4226a0a7db17340e605:corpus/lessons/round-88-verifier-spotcheck.md`) |
| title-canonical URL | `git show a5b3b15c00b1de5db321e4226a0a7db17340e605:corpus/lessons/round-88-verifier-spotcheck.md` (repo-relative path + commit — the own-work locator form the registry uses) |
| kind | `own-work` |
| tier | **A** — scoped to *what the round-88 spot-check recorded as the lane's requirement for a freeze gate and for the C2 successor, at that revision*. Tier A rests on the lane's own re-runnable gate output (the byte-verified commit contents), not on any external claim. |
| scope | The round-88 spot-check's routed defects 3 and 4 — the freeze-gate requirement (execute every frozen control; refuse an expectation the predicate cannot satisfy; no counter byte changes after a scored reading) and the C2 successor requirement (instance-level D5; controls executed before the freeze) |
| anchor | `§ Routed defects (the lane must fix by its next round)`, item 3 at **line 73** and item 4 at **line 74** of the file at revision `a5b3b15c00b1de5db321e4226a0a7db17340e605` (verified with `grep -n 'freeze-gate\|Freeze gate\|instance-level'` over the same bytes) |
| access date | 2026-11-05 |
| sha256 of the opened bytes | `236aa5172442fc7d5dbb860c59997f339883be82a9647b188f1bb84298215cfd` (from `git show <rev>:<path> \| sha256sum`) |
| status | proposed `mined` (cited by `corpus/knowledge/freeze-gate-round89.md` and `corpus/knowledge/instance-d5-round89.md`) |
| recheck | on-release (the file is append-only in the lane; a re-open means re-reading the same revision) |

### Located quote for the freeze-gate requirement (defect 3) — line 73

> "a freeze must execute every frozen control and refuse the freeze on an expectation the predicate cannot satisfy"

(20 words; the same line continues "and no counter byte may change after any scored reading (kill
rule — A3.1-style rulings are void)".)

### Defect 4 (line 74) — the C2 successor requirement, quoted for the same locator

> "instance-level D5 with controls executed before the freeze"

(9 words)

### `teaches` proposal (one line)

The lane's own round-88 spot-check already ruled that a freeze must execute every control and
refuse an unsatisfiable expectation, and that the D5 successor must be instance-level — so the
requirement record for C1 and C2 already exists in the corpus and need only be mechanized.

---

## Both rows — open questions for the owners

- **Row count / numbering:** the two ids are free (last committed row is S257). ScribeSources owns
  the actual table rows; this seat proposes content only and wrote nothing under `corpus/`.
- **`used-by`:** proposed `corpus/knowledge/freeze-gate-round89.md` (S258 + S259) and
  `corpus/knowledge/instance-d5-round89.md` (S259) — the entries the plan names as citing them.
- **Route correction:** the plan/assignment's route (a) PMCID is wrong; the row's canonical URL must
  read `PMC5856500`.
