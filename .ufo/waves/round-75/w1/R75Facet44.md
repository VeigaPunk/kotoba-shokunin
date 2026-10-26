# Facet 44 — evaluation threshold claim

## Observation (committed bytes)
At lane revision `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`round-74: hyaku run-8 orchestrator salvage…`), `corpus/knowledge/skill-eval-artefacts-round70.md:58-72` states that the Agent Skills guide says should-trigger passes above threshold (F7), while reference `run_eval.py` uses `>=` (F8); it derives the equality boundary, including the default three-run case, and recommends non-integral threshold×run counts, deduplicating query strings, or stating the applied rule. `:76-82` explicitly limits scope to the guides and one reference implementation, and says it makes no claim that clients natively run these artefacts. `SKILL.md:193` carries this guidance into author-facing rules, including the threshold disagreement. The supporting facts identify their source rows/snapshots at knowledge-entry lines 1-8; F7/F8 are tabulated at lines 33-34.

## Assessment / candidate claim
**Potential claim:** “The guide/reference implementation differ at the should-trigger threshold equality boundary; at threshold 0.5 with three runs, a single query has no equality outcome, but even run counts can produce one.” This is well bounded and falsifiable against the cited wording and implementation branch. The entry's stated scope and caveats are material; do not generalize this to every evaluator, client, or current implementation.

**Concrete control:** On the committed snapshots, verify the guide's located threshold wording and inspect the pinned implementation's should-trigger comparison; exercise synthetic per-query counts immediately below, equal to, and above threshold for odd/even run counts. Include duplicate query-string aggregation as a separate case because the entry says the reference groups by query string. A control should fail if the implementation comparison changes from `>=`, if the guide wording changes from “above,” or if equality becomes reachable under the stated single-query/default-run setup. Keep client-native execution claims explicitly out of scope unless separately sourced and observed.

## Risk / unknown
The cited evidence supports the disagreement as a fact about these particular pinned documents and script revision, not live/current upstream behavior. The r70 entry records snapshot hashes but this facet did not independently reopen/hash those snapshot bytes or execute the comparison; current status of those upstream sources is unresolved. Thus treat the proposed statement as a committed-source candidate, not a fresh-source finding. No files were edited; no tools installed or checks run.

## Evidence pointers
- `corpus/knowledge/skill-eval-artefacts-round70.md:1-8,33-34,56-72,74-82`
- `SKILL.md:193`
- Source revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD`)

Report path: `.ufo/waves/round-75/w1/R75Facet44.md`
