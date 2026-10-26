# R75Facet10 — description-audit evidence calibration

## Finding (confidence: high for the internal inconsistency; medium for the control implication)

**Observed.** `corpus/knowledge/skill-eval-artefacts-round70.md:1-8` records S209/S210 as fetched 2026-10-25, then supersedes them with revision-anchored S212/S213 at lines 5-6. Its `ground:` statement at line 9 is a historical baseline claim explicitly pinned to `7d51253f`; it describes absence in the old SOURCES/corpus sweep, not current coverage. The entry scope at lines 76-80 explicitly limits itself to evaluation guides and a reference implementation, disclaims that clients natively run eval files, and separates an opt-in Claude plugin as a near-miss.

`corpus/lessons/round-74-verifier-spotcheck.md:46-64` rechecks the separate round-74 C1: sources S223–S225, pinned snapshot hashes, fetched-byte equality, provenance and page-fidelity judgments, and a counter result. It reports the C1 coverage verdict as **improved** (line 64), not closed. The report says some counter/self-test values are evidence-verified rather than rerun (lines 60, 63). This is a closure record about r74's declared claim, not evidence that the r70 entry is itself a current r75 claim.

**Inference / candidate weakness.** A description audit that treats the r70 `ground:` absence or its evaluation-guide scope as evidence about current r75 sourced depth would be stale or category-confused: the entry's own header records a superseding source revision and the lesson's independent C1 is about different pages and a different claim. The strongest control is therefore claim identity + committed-byte provenance, not a generic citation-presence test. This is a bounded audit candidate; these excerpts alone do not establish that any current description actually makes the mistaken claim.

## Concrete falsifiable check/control

At the selected committed tip, check the exact description sentence against its named evidence entry and the relevant committed source rows/snapshot: (1) resolve each cited `S###` in that revision's `corpus/SOURCES.md`; (2) verify source identity/anchor and `used-by`/entry provenance; (3) locate the quoted rule in the pinned snapshot; (4) compare the description's proposition and scope to that passage, rejecting a historical `ground:` baseline as a current-source assertion. Separately record whether the claim is sourced coverage, assimilation, or only a historical discovery; do not promote r74's `improved` to closure. A concrete failure condition is a description asserting current absence based only on r70's baseline sweep at `7d51253f`, despite the later S212/S213 rows and distinct S223–S225 C1 evidence.

This control is falsifiable by a committed revision where the description points to the correct current row and source passage supporting the same scope; conversely a counterexample is a description whose cited row resolves but whose located passage does not entail its wording. A mechanical row/hash check can establish provenance and byte identity, but entailment/scope still requires a reviewer; do not describe the mechanical check as a semantic proof.

## Evidence limits

- `corpus/knowledge/skill-eval-artefacts-round70.md:1-9, 76-80` gives source dates/revisions, historical ground scope, and the explicit client-runtime limitation.
- `corpus/lessons/round-74-verifier-spotcheck.md:46-64` gives r74 claim identity, commands/outcomes and the improved verdict; it distinguishes remeasured from evidence-verified assertions.
- These are inspected working-tree file lines. I did not establish a specific commit object for these files in this scout pass; no claim here that these exact bytes are committed at a named revision. No commands were run to execute counters or fetch live sources.
- No edits, installs, live fetches, or model experiments performed.
