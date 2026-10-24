# kotoba-shokunin — Promotion checklist

Promotion to shokunin requires all of:

- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  evidence: `.ufo/round-46/scouts/B2.md` (SKILL.md inventory: 7 anatomy rows, 5 decision rows, 41 checklist boxes 15/9/9/8, 38 Sources entries; lane-run). Recount at round 57 (`A3CriticScorecardCalib`): the 5 decision-shape rows moved to `corpus/knowledge/anatomy-and-compression.md:102-108` (pointer `SKILL.md:241`, repointed round 60 for the round-59 carried R4 drift); § Sources holds 18 top-level entries at `cbbee56e` (`git show cbbee56e:SKILL.md | awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' | wc -l` prints 18; the same awk printed 33 at `07c33d73` — true at the round-57 recount — and 20 at `c63ccc68`, drift corrected here in round 63 per `ScoutW2SHONEN`)
- [~] At least one end-to-end domain task executed and logged in LOG.md
  evidence: `corpus/knowledge/cold-run-round11.md` (corpus-integrity verifier red-before → green-after, cold run by a lane-dispatched reviewer — lane evidence per PROTOCOL Promotion gates)
- [~] Instructions executable by an agent without oral context
  evidence: `corpus/lessons/round-8-aggregator-box3-coldrun.md` (only non-author run on record: `[~]` with defects B1/B2, both fixed in round 13; no fresh non-author re-run since)
- [~] No cross-domain bleed (PROVINCE.md still accurate)
  evidence: `PROVINCE.md` § Adjacent (round 46, sibling-overlap scan `.ufo/round-46/scouts/w2-connector.md`; the section was rewritten in round 49 from `corpus/knowledge/sibling-overlap-census-round49.md` — the round-60 close moved `## Adjacent` off line 33; at the round-63 tip the heading is `PROVINCE.md:35` and the round-49 rewrite sentence is `:37`, drift corrected here per `ScoutW2SHONEN`; the sibling-census guard `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` prints `rows 20 verified 20` / `province rows 20 matched 20`, exit 0)
