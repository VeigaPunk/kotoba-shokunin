# R75Attack11 — Falsification of R75Facet11

## Verdict

**Finding survives, narrowly: minor calibration risk, not a factual falsification.** The source itself explicitly dates the cache observation and labels the later live-set statement as 2026-10-14 errata. The report correctly refrains from asserting current cache state. Its proposed separation of historical observations from current measurements is materially actionable, though this passage already provides substantial temporal qualifiers and a historical receipt is not essential to a purely historical claim.

## Independent evidence

At the measured working-tree source `SKILL.md:32-45`, lines 32-34 state counts at round 7, round 9, and round 13 (explicit timestamp `2026-09-28T23:30Z`) and say all 17 keys reproduced against “today's” descriptions. Line 35 immediately labels the contrasting live-set count as “2026-10-14 errata” and points to LOG.md round 18. Lines 36-45 explain row identity, retention, source-path drift, and session timing. Thus “today's” is genuinely underspecified in the sentence, but neither the 17-key observation nor the later 7-key correction is presented without temporal context. Line 54 independently warns citations are point-in-time and must be re-read after drift.

I did not inspect mutable host cache/session state: the report's boundary is committed evidence, and a live query would not falsify the committed historical assertion. The proposed control is safe as a future evidence standard, but its “counter should fail” requirement is not demonstrated as an existing check, and the report does not offer a runnable command to test it. No current-state count claim is established here.

## Scope and residual risk

This is a wording/calibration observation, not a demonstrated defect in runtime behavior or a false historical count. Explicit dates and errata make gross misreading less likely; adding a date beside “today's” would improve precision but is low-severity. No duplicate evidence identified. LSP device/status was unavailable in this environment (`read xd://lsp` returned “No such tool”); source and report were inspected directly, so no semantic reference/caller claim is made. No code or lane source modified.