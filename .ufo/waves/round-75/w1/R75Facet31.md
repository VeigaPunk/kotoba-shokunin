# R75Facet31 — trigger-threshold calibration

## Finding

**Candidate: `corpus/knowledge/skill-eval-artefacts-round70.md` § “The one disagreement, and the action it implies” (lines 56–72).** This is a concrete, falsifiable description-audit candidate, but its calibration should not be generalized beyond the named guide and one pinned implementation. Confidence: high for what the committed entry asserts; no fresh validation of its cited snapshots or verifier was done in this read-only scout pass.

The entry distinguishes S213's guide wording (“above” the threshold) from S211 `run_eval.py`'s inclusive `>=` branch, and bounds disagreement to should-trigger queries at equality (lines 58–70). It states a testable condition: at threshold 0.5 with an odd number of runs on a single query, equality is impossible; even run counts can reach equality. It further identifies duplicate query strings and thresholds whose product with run count is integral as routes to equality (lines 62–70). This is stronger than a vague claim that a counter is “stricter” or “looser”: it names the predicate and the boundary case.

The actionable advice at line 71 (“keep threshold × runs non-integral … de-duplicate query strings, or state which rule the report applies”) is directionally clear but the paragraph does not itself establish that these choices are sufficient for every implementation/configuration, or that query deduplication is semantically safe. Treat this as a scoped risk, not a demonstrated defect. Also, “every disagreement runs one way” at line 70 is scoped by surrounding text to the described two sources; it is not evidence about other clients or versions. The entry's explicit refusal to claim native client support at lines 76–82 is good scope control.

## Committed evidence / reproducible checks

Paths and line references are to the current committed-tree working copy inspected here; for immutable reruns, resolve the same paths at an explicit commit with `git show <rev>:<path>`.

- `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` — guide-vs-implementation comparison, arithmetic edge cases, bounded conclusion and advice.
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8` — provenance identifies S209–S213, the upstream revision, snapshot hashes (abbreviated in prose), verification date, and a recheck command.
- `corpus/SOURCES.md:151-153` — S210/S212/S213 rows; S213 identifies the description trigger-eval subsection and upstream revision (long rows are wrapped/truncated in ordinary reads, so inspect exact bytes with `git show <rev>:corpus/SOURCES.md` when reviewing).
- `corpus/QUALITY.md:31,34,36-37` — Q20/Q23 require naming the approximated rule and counterexamples in both directions; Q25/Q26 require mutant sensitivity and headline clauses to be measured.

Concrete, cheap falsification controls for a future audit (not run here):

1. Recompute `trigger_rate` with runs `3`, `4`, duplicate query entries, and thresholds `0.5`, `1/3`, `2/3`; compare the guide's strict boundary with the exact committed S211 branch. Record whether each case reaches equality and which verdict each rule yields. This tests the paragraph's math and directionality.
2. Mutate the pinned implementation comparison (`>=` to `>`) and require the boundary-case check to change its output; separately mutate threshold/run inputs to prove the test reads the actual comparator and not just source labels. This satisfies the spirit of Q25/Q26 rather than merely counting citations or rows.
3. Audit any proposed “fix” (deduplicate, alter run count, or choose an explicit rule) against duplicated-query and non-default-threshold cases. Preserve an explicit scope statement: guide S213 versus the one S211 revision, not clients generally.

## Limits

This report read the local entry and registry rows only. It did not open the snapshot files, run `verifiers/check_skill_evals.py`, fetch live pages, or verify the S211 branch at its stated commit. Therefore the assessment is of the sourced claim's framing and proposed controls, not an independent reproduction of its factual inputs. No files other than this report were written.