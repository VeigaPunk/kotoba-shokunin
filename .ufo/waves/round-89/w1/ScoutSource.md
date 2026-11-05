# ScoutSource — round 89 §2b source opening (S258, S259)

Seat: **ScoutSource**. Wave `r89-w1`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
All paths in this report are relative to that lane root.

## What I did

Opened the two source rows the plan's §2b names, so C1's knowledge entry can carry a provenance
trio. Both rows exist and both are grounded in bytes actually opened on 2026-11-05.

| row | kind | what it is | opened |
|---|---|---|---|
| **S258** | paper | Nosek, Ebersole, DeHaven, Mellor — "The preregistration revolution", *PNAS* 115(11):2600–2606, 2018-03 — https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/ | fetched HTTP 200, 196,972 B, sha256 `ee0d0560901a0e65c6b8079e2eaf1d79c049c74597ce3f374b4e19bce0ba51f9` |
| **S259** | own-work | `corpus/lessons/round-88-verifier-spotcheck.md` @ `a5b3b15c00b1de5db321e4226a0a7db17340e605` — routed defects 3 and 4 | `git show <rev>:<path>`, sha256 `236aa5172442fc7d5dbb860c59997f339883be82a9647b188f1bb84298215cfd` |

## Files written (mine only)

- `.ufo/waves/round-89/w1/ScoutSource/SOURCE_ROW.md` — the proposed rows in full: id, title-canonical
  URL, kind, tier proposal + scope sentence, anchor, quotes with locations, sha256, access date,
  `teaches` proposal.
- `.ufo/waves/round-89/w1/ScoutSource/s258.html` — the saved S258 bytes (196,972 B).
- `.ufo/waves/round-89/w1/ScoutSource/receipts.txt` — the full fetch transcript (all routes, statuses,
  digests) plus the S259 git verification transcript.
- `.ufo/waves/round-89/w1/SOURCE_READY` — content `S258 S259`.

Nothing under `corpus/`, `plans/`, `verifiers/`, `LOG.md`, `SCORECARD.md` or `MANIFEST.json` was
touched. No git/jj write was run in the lane; only read-only `git show` was used.

## S258 — located quotes (both ≤ 25 words)

- **Confirmatory vs exploratory** — §Preregistration in Practice → *Challenge 5: Many Experiments*,
  HTML line 1472 of the saved bytes:
  *"researchers can achieve confirmatory research via replication. All initial experiments are treated
  as exploratory research."* (15 words)
  Alternative in the same leg, §Challenge 7: Few a Priori Expectations, line 1478:
  *"Preregistration benefits both exploratory research and testing predictions during the iterative research process."* (13 words)
- **Timing of registration relative to outcomes** — §Preregistration Distinguishes Prediction and
  Postdiction, HTML line 1451:
  *"Preregistration of an analysis plan is committing to analytic steps without advance knowledge of the research outcomes."* (17 words)

`teaches` proposal: preregistration is a *pre-outcome commitment* — the plan is fixed before outcomes
are seen, so confirmatory tests stay separable from exploratory ones; a control whose expectation
cannot be observed under that commitment is not a confirmation.

## S259 — located quote (defect 3, the freeze-gate requirement)

`§ Routed defects`, **line 73** at revision `a5b3b15c00b1de5db321e4226a0a7db17340e605`:

> "a freeze must execute every frozen control and refuse the freeze on an expectation the predicate cannot satisfy"

(20 words; the line continues "and no counter byte may change after any scored reading (kill rule —
A3.1-style rulings are void)".)

Defect 4, **line 74**, the C2 successor requirement: *"instance-level D5 with controls executed
before the freeze"* (9 words).

## FINDING (route correction — needs an owner, not a counter change)

**The assignment's route (a) PMCID is wrong.** `https://pmc.ncbi.nlm.nih.gov/articles/PMC5813543/`
returns **HTTP 200** but serves a *different article* — "STOREKEEPER RELATED1/G-Element Binding
Protein (STKR1) Interacts with Protein Kinase SnRK1" (307,298 B, sha256
`20574435edee839a38369b17197395d194b68eedde578fda80de3e77ea2939b8`). Routes (b) `pnas.org/doi/…`
and (c) `doi.org/…` both return **HTTP 403** (publisher bot-block; 5,686 B and 5,697 B).

So all three prescribed routes as literally written fail to yield the paper — (a) on identity, (b)
and (c) on status. I resolved the assigned DOI through NCBI's own idconv API
(`pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=10.1073/pnas.1708274114&format=json` →
`"pmcid":"PMC5856500"`) and fetched `https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/` →
**HTTP 200**, title "The preregistration revolution", correct authors (Nosek, Ebersole, DeHaven,
Mellor), *PNAS* 115(11), 2018-03, PMID 29531091, pages 2600–2606. That is the route that produced
the saved bytes and the quotes. The row's canonical URL must therefore read **PMC5856500**, not
PMC5813543.

This is a plan/assignment text defect, not a counter defect: it changes no predicate sentence,
target, control or kill rule, and the round's C1 claim does not depend on the route list — the
source exists and is opened. It is recorded in `SOURCE_ROW.md`'s route ledger and in `receipts.txt`
so the L1/ScribeSources can write the row with the right URL. **I did not edit the plan.**

## Other notes / risks

- **Fetch-stability of the saved bytes.** Two independent fetches of PMC5856500 gave byte-identical
  *article text* but differing raw bytes: NCBI injects a per-session `ncbi_phid` meta tag (line 77)
  and a `csrfmiddlewaretoken` hidden input (line 1934) — exactly two differing lines, `diff` output
  in `receipts.txt`. The raw-byte sha256 in the row is therefore the digest of *this* saved copy;
  the fetch-stable digest of the article text (tags stripped, whitespace collapsed) is
  `dde98a5ebe159b7a4a4e07b52ce40e9d65e16d6c7b12f943d61c68ae1fcf3efc` (61,093 chars), identical
  across both fetches. Both digests are recorded in the row.
- **Access/licence.** Europe PMC's record for the DOI reports `isOpenAccess: N` for the publisher's
  version while the PMC author manuscript is served to this seat at HTTP 200. The S258 tier-A
  proposal is therefore scoped to *"the preregistration-before-data principle and the
  confirmatory/exploratory distinction as stated by the paper's own authors"* and explicitly not to
  the lane's freeze-gate mechanics (that is S259's scope). ScribeSources/ReviewerD5Gate may want to
  re-check the tier wording against the contract before the rows land.
- **Status proposal.** Both rows are proposed `mined` with `used-by` =
  `corpus/knowledge/freeze-gate-round89.md` (S258 + S259) and
  `corpus/knowledge/instance-d5-round89.md` (S259). Both knowledge entries are written by ScribeEntry,
  so if either entry is renamed before landing, `used-by` must follow.
- **No second row invented.** The registry's last committed row is S257; S258/S259 are the next two
  free ids. This seat wrote no table row — ScribeSources owns `corpus/SOURCES.md`.
