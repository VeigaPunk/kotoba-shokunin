# Facet 42 — trigger-eval calibration boundary

**Axes:** factual support, falsifiability, scope, control operability.

## Finding

`corpus/knowledge/skill-eval-artefacts-round70.md:58-72` identifies a concrete threshold edge: the guide's “above” wording for should-trigger differs from the reference implementation's `>=` at exact equality. The discussion is unusually well bounded: it says the default three runs and threshold 0.5 avoid equality for a query string listed once, then names duplicate query strings and non-default thresholds as cases where equality can arise. The committed S210 snapshot supports the surrounding protocol advice: fixed train/validation split and no validation feedback during edits (`.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:136-163`). The knowledge entry attributes the behavior to S210/S211 and pins committed snapshots (`skill-eval-artefacts-round70.md:2-3,7-8`).

**Important limit:** the quoted entry's exact-threshold conclusion concerns a reference implementation, not a universal definition of “pass” or an observed kotoba description's quality. The same entry explicitly frames this as one guide/reference-implementation scope (`:74-77`). Its own “action” (`:71-72`) offers alternatives but does not show a description evaluation receipt or evidence that one choice was applied. Thus it is a sound candidate for a calibrated rule/control claim, not evidence of calibrated performance for a specific description.

## Concrete check/control

For a proposed description-performance claim, freeze the description bytes, query strings and labels, threshold, repetitions, and train/validation partition before measuring. Test both a unique query and a duplicate query at a setup that yields exact equality (e.g. threshold 0.5 with 2 runs, or duplicated query under 3 runs); assert and record separately the guide's strict `>` interpretation and the chosen implementation's `>=` result. Also include should-not-trigger equality as a control, since the entry says that side uses `<`. Report per-query numerator/denominator and identify which rule the verdict uses. Keep validation results out of edits and select/report the chosen revision using the predeclared validation rule, consistent with S210 lines 142-161. A character-limit check alone is not a semantic trigger-quality measure (`SKILL.md:23-46` describes distinct loader surfaces and does not claim that length validates quality).

## Evidence status

Observed in committed bytes: the attributed edge case and its qualifications (`corpus/knowledge/skill-eval-artefacts-round70.md:58-72`), S210's split/selection guidance (snapshot `:136-163`), and explicit scope refusal (`skill-eval-artefacts-round70.md:74-77`). Inference: those materials support designing a discriminating evaluation, but do not establish that any particular current description passes or generalizes. No live fetch, runtime evaluation, or source mutation performed. Remaining unknown: no target description's frozen query set, results, or committed receipt was examined here.

## Evidence commands

- `read corpus/knowledge/skill-eval-artefacts-round70.md:1-9,48-77`
- `read .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:136-163`
- `read SKILL.md:23-46`

Report trailer: `Facet 42; evidence from committed lane bytes at cited paths/lines; no live fetch or source edit performed.`