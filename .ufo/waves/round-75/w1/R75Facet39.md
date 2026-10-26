# Facet 39 — trigger-rate threshold boundary

**Assessment (observation):** `corpus/knowledge/skill-eval-artefacts-round70.md:33-34` records a genuine boundary difference: guide S213 says a should-trigger query passes when its rate is *above* threshold (and suggests 0.5); the pinned reference implementation S211 uses `>=`, so equality passes there. The same entry identifies both source rows and snapshots at lines 2-6, and limits its scope to those guides plus one implementation at lines 76-77. This is useful sourced depth: it distinguishes normative wording from one observed implementation rather than presenting them as equivalent.

**Calibration/control risk (inference):** A description audit that adopts “above” while implementing inclusive comparison, or vice versa, can change classifications exactly at the threshold without any change in observed trigger rate. That risks a misleading headline when aggregate pass counts omit the comparator and boundary cases. The current fact is carefully qualified; do not generalize S211's comparator to other clients or implementations.

**Concrete control:** Freeze the comparator in the audit protocol and report it with the threshold. Add two deterministic fixture cases for a should-trigger query: rate exactly equal to threshold (must pass under the explicitly chosen `>=` rule; must fail under `>`), and just below threshold (must fail under either). Record expected and actual classification. Keep the same threshold and query set for baseline/candidate runs; report per-query trigger rates and aggregate separately. This makes the equality choice falsifiable and prevents aggregate scores from hiding it.

**Evidence basis:** committed knowledge entry lines 27-34 give the described eval protocol, threshold guidance, and implementation discrepancy; lines 76-77 explicitly refuse the unsupported claim that clients natively run the artefact. `corpus/QUALITY.md:36-37` supplies the relevant general control: a claim counter must be shown to fail on falsified claimed content, and every headline clause must be measured or bounded to what its counter prints. The suggested equality fixtures operationalize that criterion for this narrowly scoped threshold claim; they are recommendations, not evidence of an existing audit implementation.

**Unresolved:** This facet did not inspect a round-75 frozen plan/counter or run fixtures; therefore it establishes a candidate control and source-backed discrepancy, not that a current description-audit counter is defective or that any audited skill was misclassified.

## Report trailer

- `corpus/knowledge/skill-eval-artefacts-round70.md:2-6,27-34,76-77`
- `corpus/QUALITY.md:36-37`
