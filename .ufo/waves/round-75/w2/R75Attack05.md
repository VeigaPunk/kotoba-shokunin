# R75Attack05 — trigger-threshold boundary

**Axes:** calibration; depth. **Verdict: central historical claim survives attack; proposed control is accurate for the stated pinned artifacts, with an applicability limit rather than a factual defect.** At measured master `65a5c7a`, independently reopened `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,56-72` and the pinned sources. S210 snapshot lines 90-92 explicitly says three runs are a reasonable starting point, should-trigger passes above threshold, and should-not-trigger below. S211 snapshot lines 213-229 aggregates outcomes keyed by exact query string and computes rate over that list; lines 231-234 use `>=` for should-trigger and `<` for should-not-trigger; lines 266-267 set defaults to 3 runs and .5. Therefore a unique query with three outcomes cannot equal .5, but duplicate identical query entries can aggregate to 3/6 and hit the implementation's inclusive boundary. The entry accurately preserves the guide/spec distinction and refuses claims about native client execution (lines 74-82).

**Attack / limitation:** No factual counterevidence or in-scope duplicate found. The proposed minimal truth table is sound. Its prescription to “de-duplicate query strings” is not itself a universal cure: different labels for duplicate query strings are collapsed into one `query_triggers` group and `query_items[query]` is overwritten by the latest item (S211 lines 217-229), so de-duplication must preserve/resolve `should_trigger` label conflicts, not merely discard exact duplicate rows. The facet does not assert otherwise; this is a practical qualification to the control. It also does not establish that the evaluator is a current round-75 runtime, and explicitly limits itself to historical pinned evidence.

**Check:** Read-only source check performed; no model run or live fetch. No command execution needed: the proposed boundary follows directly from the committed comparator, grouping, and defaults. Historical snapshots establish their own recorded source contents, not current upstream behavior.

**Evidence paths** (relative to `kotoba-shokunin`):
- `corpus/knowledge/skill-eval-artefacts-round70.md:13-16,33-34,56-82`
- `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:90-92`
- `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:213-234,266-267`
