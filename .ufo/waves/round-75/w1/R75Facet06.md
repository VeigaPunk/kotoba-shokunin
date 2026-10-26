# R75 facet 6 — Q71, script-only control

## Axes
Sourced depth: whether Q71's rationale is tied to an observed failure. Calibration/operability: whether the prescribed control distinguishes script-reproducible evidence from the claim's non-script content.

## Observations (committed-file evidence)
- `corpus/QUALITY.md:87` (Q71) requires the plan to disclose the measured script-only-world score on the same frozen counter; headline scope is limited to what that world cannot attain, and a target-reaching world requires an explicit disclosure and named non-author judgment.
- Its cited rationale is `corpus/lessons/round-74.md` M135: a carry-forward world scores `20 of 20` in `check_sibling_reread.py`, despite the plan's “quotes die at moved lines” statement being false for all 20 rows. This is a concrete counterexample to treating the counter's nominal target as evidence of the claimed semantic property.
- The same round's verifier spotcheck reports this limitation and distinguishes the re-derived freshness work from the counter's discrimination: `corpus/lessons/round-74-verifier-spotcheck.md:80-86` says the carry-forward world also scores 20/20, while the freshness move (15 stale pins re-read/re-pinned and sampled quotes re-located) was independently re-derived; the judged change is separately assessed by a reviewer.
- `corpus/knowledge/skill-eval-artefacts-round70.md:18-21,27-34` makes a useful neighboring distinction: output correctness and trigger firing are separate questions with separate artefacts; its authority note (`:13-16`) explicitly limits the guide's advice and disclaims normative-spec status. This supports keeping any audit claim scoped to the measured construct, not generalizing a proxy score into overall quality.

## Assessment / inference
Q71 is well calibrated for the specific failure it names: it forces disclosure of the strongest script-only baseline and prevents claiming that a fully script-reachable target demonstrates additional human-judgment value. It is falsifiable by running that control through the frozen predicate and comparing its score to the target. It does not itself establish that the remaining judgment is sound or independent; named seats and their evidence are still required, and Q71 cannot make their conclusions true by requiring disclosure. Confidence: high for the rule and its r74 motivating counterexample; moderate for proposed use in an r75 description audit, because this is a general claim-control principle, not direct evidence about any specific current description.

## Concrete control for an r75 audit
For each proposed description-audit claim, freeze the predicate and target first. Construct a script-only control using the same committed description/source rows, with no human semantic assessment, and record its score and command beside the target. If that control reaches the target, do not claim that the counter demonstrates substantive description quality; bound the claim to the mechanically observed fields and assign semantic/factual support judgments to named non-author reviewers. For a claim about sourced depth, require reviewers to map each description clause to a committed source row and located source text, and record unsupported/overbroad clauses as counterexamples. This is a recommended control design, not an observed r75 result.

## Risk / unknown
The selected r74 spotcheck gives the carry-forward score and reviewer conclusion, but does not by itself provide the frozen counter's full control input and invocation in the excerpted lines; use the cited committed receipt/control artifact and pinned revision before treating the result as a reproducible r75 baseline. This facet makes no claim that current r75 descriptions have passed or failed an audit.

## Evidence commands
- `nl -ba corpus/QUALITY.md | awk 'NR==87'` — Q71 exact rule/rationale.
- `nl -ba corpus/lessons/round-74-verifier-spotcheck.md | awk 'NR>=80 && NR<=86'` — carry-forward limitation and separate re-derived evidence.
- `nl -ba corpus/knowledge/skill-eval-artefacts-round70.md | awk 'NR>=13 && NR<=34'` — scope disclaimer and distinction of evaluation constructs.
