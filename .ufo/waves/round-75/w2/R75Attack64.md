# R75Attack64 — independent attack on R75Facet64

## Verdict
**Survived attack on central counter-calibration finding; qualifications: one proposed headline control is textually non-vacuous but semantically incomplete.** At measured HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the credited counter demonstrably counts backed rows, not the sentence's asserted four 1,024 clients or its negative about render cuts. It accepts at least four backed clients (TARGET=4), and currently reports 7 of 7 / rc 0. This is a material mismatch in what “checked by” appears to credit. No evidence establishes that the sentence's underlying factual description is false; the report's calibration distinction is the stronger, supported finding.

## Independently reopened evidence
`SKILL.md:166` says “four clients state 1,024 and none documents a cut there” and ends “checked by `verifiers/check_description_thresholds.py`.” The table immediately below has four 1024 rows among seven: VS Code (`:172`), Copilot CLI (`:173`), Cursor (`:175`), and opencode (`:176`). The opencode cell itself qualifies the documented range as v1 and says the v2 page enforces no maximum, a qualifier the aggregate sentence omits. The 1,024 population therefore holds table-scoped, with that wording qualification.

The counter source confirms its own specified invariant: docstring `verifiers/check_description_thresholds.py:13-17,19-44` defines BACKED structure/provenance/quote requirements, not a count of 1,024 entries; `:46-48` explicitly disclaims judging render-cut vs budget vs authoring maximum. `:55-57` specifies output as backed K of seven and rc 0 iff K≥TARGET (4); `:83` sets TARGET=4. `:281` extracts numbers from each threshold cell, `:323-326` uses them to validate the entry quote and gate-recorded quote, and `:509-514` counts BACKED rows and applies the floor. It does not read the 1,024 aggregate sentence or decide whether any client documents a cut.

Safe bounded detector run on current lane bytes: `python3 -B .../verifiers/check_description_thresholds.py --root .../kotoba-shokunin` printed all seven clients BACKED and `description thresholds backed 7 of 7 clients`, rc 0. This confirms the counter's current output, not current upstream pages. No live fetch was performed.

## Attack on proposed controls
The proposed exact-count guard addresses a real gap, but its headline arm (`grep -c 'four clients state 1,024' = 1 and N=4`) does not by itself prove the sentence says that count in the asserted context: unrelated duplicate text, or a sentence retaining “four” while changing the negative/qualifier, could satisfy those two predicates. It must inspect a uniquely anchored exact sentence/field, or parse the claim, rather than merely substring-match. Similarly, `a6` sensibly recognizes that a negative claim needs reviewer judgment; an assigned sweep command and reviewer name are process evidence, not an automated proof of the negative.

The byte-pin proposal is useful for reproducibility, but snapshots/full hashes alone establish identity of the captured bytes, not that the page was complete or still current. The report properly treats this as supporting control rather than proof of live truth. Scope is also appropriately bounded to seven table rows; the broader portability-floor sentence at `SKILL.md:162` mentions the spec as another 1,024 authority, so “four clients” should be explicitly table-scoped to avoid a reader counting five authorities in this file.

## Result
Central factual claim—that the credited counter does not test the aggregate count or render-cut negative—is supported by independent source inspection and a successful baseline run. Underlying table count is supported at the measured bytes; current vendor-page truth remains unmeasured. Proposed exact-count assertion is directionally relevant but needs uniqueness/context protection to be a robust claim-surface control.

## Report trailer
- Facet: description-threshold aggregate sentence and counter credit.
- Verdict: survived attack, with proposed headline guard qualified as incomplete.
- Evidence revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- Paths: `SKILL.md:162,166,168-176`; `verifiers/check_description_thresholds.py:13-57,83,266-330,509-514`; `corpus/knowledge/skill-listing-thresholds-round54.md:15-19,38-46`; `.ufo/waves/round-75/w1/R75Facet64.md`.
