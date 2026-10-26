# R75Facet11 — cache-history paragraph calibration

## Finding

**Candidate:** `SKILL.md:32-46` (especially `:32-45`), the paragraph reporting cache-row counts and live-key reproduction, followed by the session-staleness behavior.

**Observed in committed bytes:** `SKILL.md:32-45` calls 5/17, 17/17, and 18 rows dated round 13/2026-09-28; says all 17 live keys still reproduce against “today's” descriptions; then records an erratum that the live set is now 7 (`:34-41`). It also explains rows are keyed by `(name, description-as-loaded)` and never pruned (`:36-42`), and that rows land after session start (`:43-45`). `SKILL.md:54-56` explicitly warns citations are point-in-time and must be re-read after drift.

The dated rows and explicit erratum make the historical nature partly recoverable, but the nearby phrase “today's on-disk descriptions” at `:34` has no date attached to “today” in that sentence and sits beside a present-tense mechanism. The paragraph therefore risks being read as a current-state measurement despite its historical dates. This is a calibration/falsifiability weakness, not evidence that the historical count itself is false.

## Evidence and limits

- `corpus/lessons/round-74-verifier-spotcheck.md:102-105` records depth and calibration as unchanged, with no declared claim; it does not independently validate this paragraph.
- A committed historical scout explicitly contrasts the old paragraph with later observations: `.ufo/waves/round-47/falsify/W2SkillSubstrateProse.md:159-160` quotes the same claims, and `:246-248` lists verification limits (including no runtime opencode execution and no session-body reads). Its findings are a dated historical audit, not a current remeasurement.
- The broad grep result found additional dated artifacts with varying cache counts, but those historical rows do not establish the current host state. I did not inspect live host state or fetch sources, consistent with the read-only committed-evidence boundary.

## Concrete check/control

For any r75 description-audit claim using this paragraph, separate **historical observation** from **current measurement**. Pin the commit/revision and date for each historical cache count; remove or explicitly date “today's” in the 2026-09-28 sentence. To assert a present cache population, require a committed receipt that prints the measurement timestamp and exact read-only query over the pinned cache database, plus a deterministic reproduction check for the specifically enumerated keys against the correspondingly dated on-disk descriptions. Keep those outcomes separate: database row count is not live-skill coverage (the paragraph itself says so at `SKILL.md:36-42`). A counter should fail when the asserted date/count/key set is changed or when a cited key no longer reproduces; it must not treat a historic receipt as current evidence.

## Confidence / unresolved

High confidence that the prose contains dated historical measurements and an erratum, based on the committed lines above. The exact live cache population and which keys currently reproduce remain unverified and are not asserted here.