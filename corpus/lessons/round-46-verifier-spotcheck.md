# round-46 — non-author verification and spot-check (orchestrator, kaika)

Written by the integrator, not the lane (CORPUS.md: corrections and outside reviews are new
files; the lane owns `round-46.md`). Verifiers were fresh agents dispatched by the orchestrator
after the round landed at `04192c252`; full reports are committed in the fleet repo at
`.ufo/waves/kaika-w3/kotoba-review.md` and `kotoba-critic.md`.

## Spot-check (LEARNING.md — at least one admit and one reject)

| decision | sample | verifier | result |
|---|---|---|---|
| admit | S003 (Anthropic skill structure) and S006 admitted as sources — reviewer and critic re-opened S002/S003/S004/S011 and the open Agent Skills spec; agree (the 'cannot contain XML tags' rule is vendor-specific, recorded as such) | W3ReviewKotoba | agree |
| reject | S011 (community claim that a mismatched skill 'will not load') kept at tier C / rejected as support — S002's 'Lenient validation: warn, load anyway' contradicts it; agree | W3ReviewKotoba | agree |

## Adjudication

ADMITTED: the r46 WIP (`36ab0d3`) closed on re-measurement — f2f9ee1 + 04192c2. Per-axis: depth improved (planted-cwd scope-file case exit 0→2; honest run 24/24; score held 9), operability improved-bounded (7 named bad-input cases 0→2 reject; the false failure introduced by the fix was caught and fixed pre-landing; score held 8.5), calibration improved-bounded (faked reason/evidence/probe-target 0→2; SCORECARD/census now cite `36ab0d3`; score held 8.5), consistency/coverage/freshness/adjacency unchanged. Corpus conformance landed without credit: QUALITY.md (18 criteria), round-46 lesson (19 mistake classes), SOURCES.md (11 rows, census ok), SHONEN canonical, PROVINCE Core/Frontier/Adjacent. Trends: expansion unchanged (no knowledge entry — the three claims filled the cap), quality unchanged, discernment improved (narrow, 3/3 spot-check agree). Open residuals (carried): mirror-map-removed input passes; row with no verdict, NaN and case-variant keys pass; mismatched row-level `kind` passes; payload can mark committed rows out of scope; the printed C1 counting command exits 2 as written; SKILL.md's own description carries `<skills>` (its new Q08 forbids it).
