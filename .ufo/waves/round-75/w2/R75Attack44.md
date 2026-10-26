# R75Attack44 — attack on facet 44

## Verdict
**Survives attack, with a material qualification to the proposed control.** The central factual claim is correct for the explicitly pinned guide wording and reference-script snapshot, and its scope is bounded to those artefacts. The report’s proposed “fail if equality becomes reachable under the stated single-query/default-run setup” is not a reliable regression condition by itself: equality is mathematically unreachable in that setup whether comparator is `>` or `>=`, so it cannot distinguish the disputed rule. Require an equality-reachable control (or inspect the comparator directly).

## Independently reopened evidence
Measured checkout HEAD and the cited revision both resolve to `65a5c7a663249e0522cc49e4a148424200d9ddfe`.

- `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` says the guide describes should-trigger success as “above” threshold, whereas the reference passes at `>=`; its default is 3 runs, so rate 0.5 is unavailable for a query string listed once; even run counts permit equality; duplicate query strings aggregate their runs; and non-default thresholds can also make threshold×runs integral.
- At lines 76-82 the entry expressly confines scope to the guides and one reference implementation and refuses a claim that clients natively run the artefacts.
- `SKILL.md:193` repeats the advice and threshold distinction, including keeping runs×threshold non-integral and query strings unique.
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234` independently confirms grouping by query string, rate calculation as `sum(triggers)/len(triggers)`, and `should_trigger` branch `trigger_rate >= trigger_threshold`; lines 266-267 give defaults 3 and 0.5. This is the pinned committed snapshot, not a fresh claim about upstream/live behavior.
- Knowledge entry lines 1-8 identify S213’s located guide quote (“passes if its trigger rate is above a threshold”) and S211’s pinned script and source lines. F7/F8 are tabulated at lines 33-34.

## Cheap control exercised
Ran exact rational arithmetic for run counts 2, 3, and 4 at threshold 1/2, plus the default-three-run duplicate-query case and threshold 1/3 over three runs. Results: at 3 unique runs there is no equality rate; at 2 and 4 runs, half the trials makes guide `>` false and reference `>=` true; duplicate default-three-run entries aggregate 3/6 and likewise diverge; threshold 1/3 over three runs gives equality at 1/3 and diverges. This validates the report’s mathematical examples, not execution of `run_eval.py` itself (which depends on Claude CLI and external model runs and was not invoked).

## Counterexample to the proposed check
A mutant implementation changing the comparison from `>=` to `>` produces exactly the same below/equal-unreachable/above outcomes for a once-listed query with three runs at threshold 0.5. Thus the suggestion to fail when equality “becomes reachable” under that setup is vacuous as a comparator-change detector. Conversely, the instruction to inspect the pinned branch and add an even-run equality case is discriminating and safe. Duplicate-query aggregation is separately evidenced by the source and entry, and the cited scope refusal prevents an overbroad client-runtime inference.

## Axes and smallest safe correction
- **Consistency:** factual claim and committed evidence agree; scope and provenance are stated accurately.
- **Operability:** revise the proposed control so it asserts an equality-reachable case (e.g. 2 runs, 1 trigger at 0.5) changes outcome under `>=` versus `>`; retain the 3-run case only as a check that equality is unreachable. Test duplicate grouping separately if that behavior is in control scope.

No lane source changes, live fetches, or production edits made.

Report path: `.ufo/waves/round-75/w2/R75Attack44.md`