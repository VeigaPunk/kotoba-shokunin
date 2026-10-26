# R75Attack32 — attack on R75Facet32

## Verdict
**Finding survives narrowly as a traceability/control gap, but its candidate claim is substantiated.** The facet accurately says it had not inspected S210's body, so the criticism is not a false factual assertion. Independent inspection shows the proposed sentence is in fact supported by the pinned source. No lane-source defect established.

## Axes
Evidence calibration; consistency; operability.

## Independent evidence
At measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe`, the knowledge entry `corpus/knowledge/skill-eval-artefacts-round70.md:2` identifies S210 and its pinned snapshot prefix. The snapshot `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md` hashes to `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`.

The candidate “The Agent Skills guide recommends evaluating description trigger queries with a held-out split to reduce overfitting” is directly supported: S210 `:136-145` explains overfitting and prescribes a train/validation split; `:147` describes running against separate files; `:151-161` says to evaluate both sets, keep validation out of change-guidance, and select by validation pass rate. Thus the candidate is no longer merely plausible or unsupported once the body is consulted. The knowledge entry's `:48-52` likewise summarizes the split and validation-based selection, but does not provide a located quotation for this multi-part claim.

## Attack assessment / control
The facet's scoped statement (“not established by the excerpts/lines inspected here”) is true: it explicitly records not inspecting the snapshot body. It is not evidence that S210 fails to support the claim. The control proposal to reopen S210 and record a located quotation plus digest is useful and non-vacuous; this attack performed that reopening and recorded both exact section lines and full digest.

A test rejecting an absent/off-snapshot quote would not establish that a quote is from the *right section*: the existing `verifiers/check_skill_evals.py:145-161` checks quote length/key terms and membership anywhere in the pinned snapshot, not section provenance. This is a limitation of that counter's behavior, not a demonstrated failure of the proposed quote-and-digest control, which requires a located section quotation. No command/control was run; source bytes and verifier logic were read only.

## Evidence boundary
Read-only inspection of target `w1/R75Facet32.md`, the measured revision's knowledge entry and S210 snapshot, and verifier logic. No live fetch, runtime check, or lane edit. LSP device was unavailable (`xd://lsp` returned “No such tool”).

Report: `.ufo/waves/round-75/w2/R75Attack32.md`
