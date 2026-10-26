# Round 75 — plan (hyaku run 10, lane kotoba, attempt 1)

Base lane branch `master`: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (remote matches at start). The previous r74 round is closed; its plan is historical and not continued. Wave 1 was a 64-seat v2 build/recon wave; it was read-only and produced no claim score. This plan freezes one claim before any landing or counter score. L1 is canonical planner; the bounded data-walk rode the scout/reviewer/connector seats. Seats write only their assigned report in `.ufo/waves/round-75/`; L1 owns integration and commits only through `jj-lane.sh`.

## Claim C1 — depth: the sourced trigger-eval guidance in SKILL is explicitly conditional at threshold equality

Surface: `SKILL.md:193` and `corpus/knowledge/skill-eval-artefacts-round70.md:56-72`, based on already-registered source rows S210/S213 and S211. Wave-1 evidence: `.ufo/waves/round-75/w1/R75Facet02.md:17-37,55-83` and `R75Facet03.md:5-8`; the guide says a should-trigger query passes “above” a threshold, but does not define whether equality passes. The paired reference code uses `>=` for should-trigger and `<` for should-not-trigger. The claim is not that either interpretation is universal: SKILL must instruct the reader to treat equality as unspecified by the guide and follow an explicitly named comparator for any implementation-specific report.

**Frozen predicate / counter:** `grep -Fxc 'The guide leaves equality unspecified; name the comparator used by the reference implementation (>=) rather than presenting the guide as a strict > rule.' SKILL.md` → `0` at base; expected `1` after. The outcome is one exact sentence in the source-derived rule; this does not assert general description quality or client behavior. Cheap no-op control: the base text scores 0. Kill control: a fixture copy retaining the old r70 wording (“the guide passes … only above”) also scores 0; a row mentioning S213 but not the equality distinction scores 0. This counter is intentionally a narrow content invariant, not a semantic source adjudicator; non-author attack/review remains required.

The sourced basis must be opened by L1 this round and S213 reused rather than duplicated. The round lesson records the located ≤25-word quote. No SOURCES row is added because the source is already registered and cited. Expansion is not claimed on this already-covered ground.

## Baseline and non-claim measures

At base, `python3 -B verifiers/check_spec_craft.py --rev master` prints `spec craft pages backed 3 of 3`, `held at base: 0`; `python3 -B verifiers/check_sibling_reread.py --rev master` prints `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`. These r74 counter surfaces are already at ceiling and are not r75 claims. `wc -lc SKILL.md` → `590 78569`; current description frontmatter lines 4–8 lengths are 76,78,73,79,72 (the stale 1,021-char assertion in `considerthese/2026-10-26.md` is not the current base). Tip battery at base reports 4 of 6, exit 1: corpus integrity and corpus independent exit 1; other inspected guards pass. This is a known base-red and must not be described as caused or fixed by C1.

## Frontier

Curation: opened https://agentskills.io/skill-creation/optimizing-descriptions.md on 2026-10-27; located quote “Use imperative phrasing.” (3 words), from “Writing effective descriptions.” Existing row S213 is reused. The round lesson records one candidate admit and one rejected stale proposal; non-author spot-check pending. Mistake mined: stale-premise in `corpus/lessons/round-75.md`; captured-by and fix stated there.

## Round shape

Two v2 waves, policy `/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy-v2.json`: w1 64 seats build/recon; w2 64 seats falsify wave-1 facet findings (only because w1 yielded at least 32 distinct candidate attacks). Total planned 128. W1 roles: 44 scout, 16 executor, 1 connector, 1 scribe, 1 critic, 1 reviewer; this wave is discovery, not a completed v2 claim build/attack mix. W2 roles: 32 reviewer, 16 critic, 16 mutation-tester. Seat totals, final role mix and dead seats are determined from results JSON after each WAVE-DONE. No residual task call planned.
