# Facet 41 — sourced description-eval advice

**Axes:** factual support; falsifiability; scope; operational control.

## Finding

`corpus/knowledge/skill-eval-artefacts-round70.md:48-54` gives a concrete protocol for skill-description trigger evaluation: labelled positive/negative queries, repeated runs, a held-out validation split, and iteration selection by validation rate. Its source pointer at `:2` identifies S210 and relevant sections on trigger-query design, testing, overfitting, and optimization. This is plausibly falsifiable as process advice, but the quoted knowledge excerpt does not itself show the underlying snapshot text or a measured result from applying the protocol to a description; the passage is an attributed recommendation, not evidence that a particular description is calibrated.

Scope caveat is explicit at `:76-79`: it makes no claim clients natively run the eval artefact. The `SKILL.md:23-46` loader-contract discussion is a separate claim set, with detailed mutable host/cache observations and historical errata (`:32-45`); do not treat the presence of a cap/character count as semantic or factual validation of description quality.

## Concrete check/control

For any proposed description-quality claim, freeze a committed query fixture with `should_trigger` labels, keep a declared validation partition untouched during edits, and report per-query repeated-run rates plus the selection rule. Re-open the pinned S210 snapshot and verify the recommendation at the cited sections; separately inspect the exact description bytes at the claimed revision. Avoid claiming a measured improvement unless a committed receipt records before/after results on the same queries and distinguishes validation from tuning data.

## Evidence status

Observed: cited lines above in committed files; no live fetch or experiment performed. Inference: a protocol-only entry supports proposing a control, not asserting that a target description passes it. Remaining unknown: this facet's excerpt alone does not expose the full S210 quote/snapshot content or any target description's held-out performance.
