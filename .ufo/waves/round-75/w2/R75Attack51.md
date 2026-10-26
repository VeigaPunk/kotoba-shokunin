# R75Attack51 — attack on R75Facet51

## Verdict

**Core scope defect survives; medium-high confidence.** At measured `HEAD` `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `corpus/SOURCES.md:157` says the reference runner disagrees with “the specification only at an even run count,” while its own scope says “not the specification.” The pinned runner permits non-default `--trigger-threshold`; its should-trigger predicate is `>=` (`.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:232`), whereas the cited guide says “above” (`corpus/knowledge/skill-eval-artefacts-round70.md:58-60`). At threshold 2/3 and 3 runs, rate 2/3 therefore passes the runner and fails the guide wording: a direct odd-run counterexample to the unqualified registry claim.

The wording is not wholly unrepaired: the knowledge entry at `:67-70` explicitly states both duplicate-query and non-default-threshold limits, including 1/3 and 2/3 at three runs. This narrows impact to the protected registry cell, not the entry's explanation. The facet's “specification” authority concern is directly supported by the row's scope (“not the specification”) and entry `:76-77` (guides/reference implementation); still, the evidence establishes inconsistent labels, not downstream confusion.

## Independent evidence and check

- Re-read the registry row, entry, pinned runner lines, v1 parsing logic, and append-only rule. Snapshot SHA-256 is `43e3b8f80dbf69c343967ba77e268fae991d9fa3ed68b32a0ff02532cd48657f`.
- v1 reads the S211 row's 11-cell shape, status and `used-by` (`verifiers/check_skill_evals.py:163-168`); no predicate checks the `teaches` claim. v2's documented registry-specific handling concerns superseder markers and upstream anchors (`verifiers/check_skill_evals_v2.py:35-40`), not evaluation of this clause.
- Ran the available relevant current counter: `python3 -B verifiers/check_skill_evals_v2.py --rev HEAD` → `measured-rev: HEAD`, `skill eval artefacts verified 10 of 10`, exit 0. This is consistent with the facet's claim that the identified defect is not caught; it does not validate the proposed new check.
- The proposed `check_s211_threshold_scope.py` is not present in the worktree, so its predicates/self-test arms T1–T5 cannot be exercised. No equivalent executable detector is specified in the repository. Its proposed phrase/splitting rules (notably B and D) remain design claims, not demonstrated controls; no mutant kill/survival conclusion is warranted for them.
- `check_sources_append_only.py:5-15` confirms the stated repair-channel constraint: protected cells cannot be changed in place; correction requires an appended superseder row.

## Calibration / limits

The comparison is conditional on interpreting the guide's “above” as strict `>` and the runner's threshold flag as operative; this is precisely the wording/code comparison the row itself purports to record. No live fetch or model run was made. The worktree has a modified knowledge-entry file (`git status` reports `M corpus/knowledge/skill-eval-artefacts-round70.md`); I did not write or alter it. No source, counter, or scratch mutation was made. The facet's separate claims about duplicate-label nondeterminism and exception scoring are consistent with pinned lines 218 and 225, but are secondary to the demonstrated scope counterexample.
