# R75Facet29 — sourced-depth/control finding

## Axes
- **Evidence depth:** High for documentary guidance and a concrete implementation discrepancy; not evidence that description performance improves.
- **Falsifiability:** Strongly testable if exact threshold boundary is included.
- **Scope:** Limited to the documented Agent Skills description-evaluation guidance and its cited implementation.
- **Control weakness:** Existing round-70 recommendation leaves boundary semantics under-specified.

## Finding (observed)
`corpus/knowledge/skill-eval-artefacts-round70.md:33-34` records the guide's trigger rule as “above the threshold” (0.5 suggested) and the cited `run_eval.py` behavior as `>=`; the implementation therefore accepts equality while the prose describes strictly-above. This is a specific, independently falsifiable description-audit candidate—not a claim about quality or real-world trigger accuracy. The entry pins S213 to an upstream revision at line 6 and S211 to a tree and source lines 230–234 at line 3. The facts table explicitly separates them at lines 33–34.

The same entry recommends labelled should/should-not-trigger queries and repeated runs at lines 48–51, with a validation split not used to guide edits. Line 54 explicitly warns that the skill-creator loop is “twice, not independent corroboration.” This is well-calibrated: it avoids presenting repeated runs as an independent source of truth.

## Concrete control
For a description-audit counter, include a deterministic boundary fixture with trigger rate exactly equal to threshold, plus immediately below and above; run the guide-derived strict comparison and the pinned implementation comparison as separate expected outcomes. Record threshold, numerator/denominator, and comparison operator. Keep validation queries held out from iterative description changes, and report only observed trigger rates—not a causal claim of improved description absent a paired baseline. This control makes the prose/code mismatch observable and prevents ambiguous “passes threshold” wording from concealing it.

## Risks / limits
- The cited source text is a committed documentary snapshot; this read did not independently open the snapshot bytes or execute `run_eval.py`. Treat the mismatch as the committed entry's sourced claim, not a newly executed result.
- A single boundary case validates operator semantics, not calibration quality, query representativeness, repeatability, or generalization.
- Do not infer native client support for `evals/evals.json`: the entry's lines 76–80 explicitly limits scope and says no client-native execution claim is made.

## Evidence
- `corpus/knowledge/skill-eval-artefacts-round70.md:3,6-8,33-34,48-54,76-80`
- `corpus/lessons/round-74-verifier-spotcheck.md:102-104` records depth and calibration sub-axis unchanged because no claim was declared; this facet is a candidate, not a retroactive r74 claim.
- `plans/round-74.md:47-51` defines r74 C1 as a depth claim on different body-craft guide sources, reinforcing that the r74 plan is not evidence of a frozen r75 description-audit claim.

Commands/evidence used: targeted `grep` over the five assigned files for calibration/source/claim/control terms, then `read` of the committed knowledge entry lines above. No edits, installs, live fetches, or execution performed.
