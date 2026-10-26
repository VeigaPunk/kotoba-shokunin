# R75Attack60 — Facet 60

Axes: factual calibration (whether the stated evidence defect is real) and actionability (whether proposed controls are relevant and falsifiable).

## Verdict

**Partly survives; scope/actionability is overstated.** The central provenance observation is correct: the Gemini row points at source S057, whose kind is `docs` and whose scope expressly disclaims measurement of an installed binary, while the table's cell 2 makes claims about implementation files. The existing detector accepts this combination. That is a real gap in the stated evidence chain, not proof that the code claim is false. Facet 60 does not establish a present round-75 false claim or an in-scope production defect; it proposes a new governance/evidence control. Its proposed G1 is plausibly non-vacuous for code claims, but its specialized matching requirements need care, and G3/G4 are not established as necessary controls by the evidence presented.

## Independent evidence

At measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, reopened `corpus/SOURCES.md:70`: S057 is `docs`, and its scope says it is vendor documentation, “not a measurement of any installed binary.” The row's cited anchor concerns `skills-best-practices.md`, not `skillLoader.ts` or `snippets.ts`. Reopened `SKILL.md:174`: the past-threshold cell nevertheless asserts what those two implementation steps do and cites a pinned Gemini CLI commit. Thus the distinction between the docs evidence and the code assertion is real. This does not by itself show the assertion is inaccurate: the row also cites a commit, and the report says separate pinned-code readings reproduced the pointers; the limitation is that those bytes are not committed in the lane.

Reopened `verifiers/check_description_thresholds.py:302-316`: the detector allows kinds `spec`, `docs`, and `code` interchangeably and checks tier, status, opened date, used-by, and host, but does not associate source kind/scope with the claim in cell 2. Lines 317-325 check quote length, presence of a numeric token from the threshold cell, and membership in the round-54 gate quotes. Lines 280-285 check that threshold cell has a number and action is present. It does not read the past-threshold cell. I ran the specified bounded command, `python verifiers/check_description_thresholds.py --rev 65a5c7a6`; actual output reports all seven clients BACKED, including Gemini, and exits successfully. Therefore the detector does not test the disputed implementation assertion. The run confirms the weakness, not whether the underlying code assertion is true.

## Attack on proposed controls / scope

G1 directly addresses the observed mismatch and can be falsifiable: a code pointer without code evidence should fail, while a valid pinned snapshot and matching source anchor should pass. The report's proposed “manufactured code row and snapshot” positive control is important: without it, a red-only guard could be vacuous. But requiring a snapshot only under `.ufo/waves/<round>/snapshots/` and a particular new manifest/printed-count scheme is a suggested implementation, not a demonstrated unique solution. A committed, pinned code source with precise path/line evidence could satisfy the provenance need without necessarily adopting that exact scheme. More importantly, this provenance gap should not be promoted into a finding that the implementation claim is false or that the whole threshold table is invalid.

G3 does not establish that `promptProvider.ts` is part of the claim's actual subject: the current cell names loader and prompt-template steps, and the cited four-file sweep is described in prose, not independently reopened here. Nor does adding the separate validator's 1024 limit necessarily belong in this cell: that validator is a distinct validation surface, and Facet 60 itself marks its presence at the 451a02ff pin unverified. Treat the validator point as an explicitly unverified adjacent risk, not counterevidence to the bounded loader/template statement. G4's proposal for a `no-cap` annotation is likewise a proposed schema change, not an implication of the observed provenance mismatch.

## Residual limits

No live fetch was performed, consistent with the cited no-fetch boundary. I did not reproduce the external implementation bytes or test G1/G3/G4 mutants; only the existing detector was run. No lane source was changed. The claim that the present implementation has no description truncation remains unverified by this attack; the detector's BACKED result cannot establish it.

Report trailer: Facet 60; measured tip `65a5c7a663249e0522cc49e4a148424200d9ddfe`; evidence reopened from committed bytes cited above; bounded detector run as recorded; no live fetch or lane source edit.
