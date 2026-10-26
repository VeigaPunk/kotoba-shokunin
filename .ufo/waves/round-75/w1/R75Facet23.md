# R75Facet23 — calibration/sourcing control

## Finding (one facet)
**Observed:** `corpus/knowledge/skill-eval-artefacts-round70.md:48-54` presents the trigger-set protocol (about 20 queries, 8–10 positive and negative, about 3 runs; ~40% validation) and explicitly qualifies it as guidance, not independent corroboration: the same protocol is already held in S124. Its source block `:1-8` identifies S210/S213 as the optimizing-descriptions guide, pins upstream revision/snapshot, records verified-at and a recheck command. `:13-16` explicitly distinguishes the guide from the specification and says its numbers are recommendations, not normative rules. This is strong source calibration and avoids promoting advice to a requirement.

**Control weakness / inference:** `corpus/QUALITY.md:34` (Q23) requires located authority quotations plus a sweep for whether *other authorities* state an attributed rule. The knowledge entry carefully labels the material as guide advice, but the specific trigger protocol at `skill-eval-artefacts-round70.md:48-54` does not itself show that authority sweep or a located quote range for S210; source metadata names sections, and line 9 describes provenance/grounding. Thus Q23’s cross-authority control is not visibly demonstrated in this paragraph. This is a documentation/control gap, not evidence that the advice is false or overclaimed. The lesson is especially relevant to description audits: quantify recommendation status and avoid treating borrowed protocol as an independent result.

## Concrete check/control
For the r75 audit, check the committed source snapshot at the exact S213 revision, capture the located quote range supporting each numeric recommendation, and search the other relevant authorities for the same rule. Record positive/negative sweep results; retain “guide recommendation” wording unless a separate normative authority supports stronger language. A content-removal mutant of the quoted rule should make the audit guard fail (QUALITY.md:36-37, Q25-Q26), rather than relying on row/count presence.

## Evidence basis and limits
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-9,13-16,48-54` — source/version/provenance, scope calibration, and trigger recommendation.
- `corpus/QUALITY.md:34,36-37` — applicable attribution, mutant, and headline calibration controls.
- Commands used: `grep -n` over the five assigned files for source/calibration/control terms; `read` of the cited committed-file line ranges. No live fetch or edits performed; no install.
- No claim here that S213’s source text was independently reopened in this inspection; the committed entry records its pinned snapshot and recheck procedure. The r74 plan is historical and was not treated as an r75 frozen claim.

## Report trailer
Paths are relative to `kotoba-shokunin`:
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-16,48-54`
- `corpus/QUALITY.md:34,36-37`
