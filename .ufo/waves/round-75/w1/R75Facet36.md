# R75Facet36 — calibration/control facet

## Finding

**Observed:** `corpus/knowledge/skill-eval-artefacts-round70.md:33-35` records a concrete boundary discrepancy: guide S213 says a should-trigger query passes when its trigger rate is *above* a threshold (default 0.5 is advice), while S211 implementation uses `>=`. Lines 13-16 explicitly bound the guides as advice, not normative specification. This is well-calibrated source scope and a falsifiable claim (quoted guide wording versus pinned implementation expression).

**Control weakness / risk:** the current claim establishes one reference implementation's equality behavior, not that the Agent Skills format or clients generally use inclusive thresholding. The section's explicit boundary is strong, but later prose at `:48-54` characterizes the general query/run/split protocol as the skill-creator loop and notes same-protocol statements are not independent corroboration. Avoid turning those observations into a universal client-behavior claim.

## Concrete check/control

At the pinned S211 bytes, test a trigger rate exactly equal to the configured threshold and assert `did_pass` is true; separately compare that result with S213's strict “above” wording. Keep the result labelled as implementation-vs-guide discrepancy, not specification rule or client behavior. The artifact already locates the implementation fact at `:34`; retaining an equality-boundary fixture in any future description-audit counter makes the distinction falsifiable.

## Evidence and limits

- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8`: source identities, pinned snapshots/hashes and recheck command.
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-35`: normative-scope hedge and threshold discrepancy.
- `corpus/knowledge/skill-eval-artefacts-round70.md:48-54`: repeated protocol is explicitly not independent corroboration.
- `corpus/lessons/round-74-verifier-spotcheck.md:76-77`: a separate description claim was parsed at 1,021 characters against 1,024 cap; this is length/name coverage, not evidence that its description triggers appropriately.

**Inference:** this is a useful calibration-control candidate for r75 description audit: static length and token checks cannot establish trigger effectiveness. No evidence in these inspected lines establishes actual trigger performance or a cross-client runtime result.

**Commands:** `read corpus/knowledge/skill-eval-artefacts-round70.md:1-53`; `read corpus/lessons/round-74-verifier-spotcheck.md:72-78`.

## Report

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-75/w1/R75Facet36.md`