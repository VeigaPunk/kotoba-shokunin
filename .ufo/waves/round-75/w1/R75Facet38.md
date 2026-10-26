# R75Facet38 — description-audit calibration

## Finding (committed evidence)
At `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `corpus/lessons/round-74-verifier-spotcheck.md:76` reports the candidate skill description as 1,021 characters against a 1,024 cap and says it names all 10 lanes classified non-`none`. The next line (`:77`) identifies the counter evidence as 0/20 failure, 20/20 pass, carry-forward 20/20, and 47 self-test assertions. The plan had made that description coverage a C2 predicate (`plans/round-74.md:121-129`); the spotcheck records C2 remeasurement and later says freshness improved (`:101`).

The report's counter result supports literal structural coverage under its defined predicate, not whether the description is a good, calibrated description of kotoba's actual remit. The distinction is explicit nearby in the same spotcheck: C1 page fidelity required reviewer judgement and was separately reviewed (`:58-64`), while C2's description row reports parse/count facts only (`:76-77`). The existing report therefore provides no evidence that the ten lane names are semantically appropriate, that the description avoids false-positive routing, or that it excludes genuinely relevant prompts. Those are candidate gaps, not proof of a defect.

## Concrete control proposal
Keep the existing count as a structural guard; add a separate held-out semantic audit before making any sourced-depth/calibration claim about the description. Freeze a small, provenance-pinned set of prompts: positives covering each asserted lane boundary and negatives near each anti-trigger/sibling boundary. Have independent reviewers classify expected route and justify each classification from committed `SKILL.md`/sibling source bytes. Record per-case expected-vs-observed routing, false positives and false negatives, and adjudicate disagreements; do not collapse this into a keyword-count score. Include a must-fail control by mutating/removing a boundary phrase and confirming the audit detects the changed route or failed criterion. Bound conclusion to that prompt set; this does not establish population-wide routing quality.

## Evidence and confidence
- Observed: `SKILL.md:3-18` gives the description's scope, triggers, anti-triggers, and sibling ownership boundaries; `corpus/lessons/round-74-verifier-spotcheck.md:76-77` reports the structural description count and counter results.
- Observed: `plans/round-74.md:121-129` frames the adjacent-lane census/re-pin as C2 freshness work; it is historical context, not an r75 frozen claim.
- Inference: a literal lane-name count cannot by itself demonstrate semantic calibration or routing performance; these outcomes are not reported in the cited C2 row.
- Confidence: high for the narrow evidence boundary; no independent route-quality result found in the examined committed records.
- Unresolved: whether an existing prompt fixture/receipt elsewhere measures actual description-trigger precision/recall; this facet did not sweep the full repository or inspect runtime behavior.

## Commands / source locations
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- Read committed working-tree source at `SKILL.md:3-18`, `corpus/lessons/round-74-verifier-spotcheck.md:58-64,76-77,101-105`, `plans/round-74.md:121-129`.
- LSP device unavailable in this environment (`read xd://lsp` reported no such tool); findings rely on cited literal source locations, not semantic LSP evidence.

Report path: `.ufo/waves/round-75/w1/R75Facet38.md`
