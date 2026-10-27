# R04RevHygiene — D2/D3 hygiene draft review

## Findings

**D2 commit description: verified truthful.** At lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`, `git cat-file -t d5aebcf` returned `commit` (exit 0). `git show --stat d5aebcf` reports `394 files changed, 67373 insertions(+)`. Commit author/date are `kotoba-shokunin` / `2026-10-25 23:16:44 -0300`; its complete subject is `hyaku run 7 interrupted: in-flight snapshot committed by the orchestrator (not a landing); lane L1 resumes from here`. Its parent is `d919179`; ancestry checks returned 0 for `d919179 → d5aebcf`, `d5aebcf → 2c81137`, and `d5aebcf → HEAD`. Neighbor subjects describe the counter/E1 freeze and C1/C2 data, respectively. `git grep -n d5aebcf HEAD -- LOG.md` returned no hits. Thus the facts in the D2 draft line are supported.

**D3 pointer answers the routed ask.** `corpus/lessons/round-74-verifier-spotcheck.md` routed item 3 asks for a forward pointer appended to the round-49 census so readers meet the corrected tsukuroi class. The draft names `corpus/knowledge/sibling-overlap-census-round74.md`, gives `none → adjacent (basis kotoba)` and the updated counts. The target re-pin says `10 adjacent, 10 none, 0 contested` and records the tsukuroi change at its lines 26 and 29. Its method cites the round-49 entry ranges `:43-64`, `:246-295`, `:416-458`; D3 appends after the old entry's tail, preserving these anchors. The round-49 census checker at freeze HEAD and after Form A returned the same 20 verified rows, `province rows 20 matched 4`, exit 1; the round-74 census guard remained `20/20`, exit 0. The 16 pre-existing round-49 FAIL lines are not increased by the append. `check_sibling_reread.py --rev` also remained 20/20, exit 0: its frozen round-49 pins/checker are read from its base revision.

**Form A violates recent-base LOG prefix preservation.** The r76 draft's measurements were made at `4de12b6`; between that tip and r77 base `2f675548`/freeze HEAD, LOG gained the r76 honest-stop section (8 lines). Form A's patch still applies at freeze HEAD, but a scratch clone applying and committing it reports `LOG@6523aced` is not a prefix of resulting LOG (`prefix_r77_base=False`, +740 bytes); `## Round 75` shifts from 2805 to 2807. It does pass historical `check_r63_routed_repairs.py` 5/5 with `append-only prefix=True`, because that counter compares against much earlier `35d44b4`, before the insertion point. That historical result does not make a mid-file insertion append-only relative to the current r77 base.

**Form B is the appropriate minimal compliant form, but its supplied patch is stale.** Routed item 2 explicitly says “LOG appended correction”; a tail correction section is the minimal form consistent with that request and the append-only convention. However, at freeze HEAD `git apply --check B10RepairD2D3.formB.patch` failed: `patch failed: LOG.md:2808`. Its EOF context is from the r76 wave tip, before the appended Round 76 section. Rebase the unchanged correction text to the current LOG tail; the D3 hunk remains a tail append. Do not apply Form A as a workaround.

## Counter/census impact

The frozen C1 and C2 hashes at lane HEAD match the r77 plan pins exactly: C1 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`; C2 `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`. C1 contains no `LOG` references. C2 extracts § Round 75 and checks its own R1/R4 lesson/log evidence; neither D2 form alters that section, and the D3 append is in another file. In the Form A scratch result C1 remained `description craft backed 0 of 6`, exit 1; C2 remained `r75 routed repairs closed 0 of 4`, exit 1, as expected before claim data. No counter bytes were changed. Form A's D3 append did not change the census guard outcomes; Form B's D3 hunk is the same append.

The checklist was attempted with an incomplete parent-layout shim and returned 8 PASS / 3 FAIL at base; this is not a valid checklist verdict and is not represented as one. The checklist should be rerun by the integrator in the real lane layout after integration.

## Verification evidence and gaps

Commands run in scratch clone `/fast/scratch/hyaku/kotoba-r77/R04RevHygiene/clone` at freeze HEAD, with `git rev-parse --show-toplevel` confirmed equal to the clone path:

- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`: base and Form A both exit 1, `rows 20 verified 20`, `province rows 20 matched 4`.
- Same command for `sibling-overlap-census-round74.md`: base and Form A both exit 0, `20/20` and `province rows 20 matched 20`.
- `python3 -B verifiers/check_sibling_reread.py --rev <full Form A revision>`: 20/20, exit 0.
- `python3 -B verifiers/check_r63_routed_repairs.py --rev <full Form A revision>`: 5/5, exit 0, append-only `prefix=True` against its historical base.
- C1/C2 commands at Form A revision: 0/6 and 0/4, respectively, exit 1.
- `git apply --check` at freeze HEAD: Form A exit 0; supplied Form B exit 1 (`LOG.md:2808`).
- Counter hashes checked at lane HEAD; both match plan.

Form B was not applied as supplied, so no Form B behavioral run is claimed. Recommendation is for the integrator to rebase Form B, verify current-HEAD prefix preservation and rerun the post-integration checklist/no-harm battery. No tools installed.

VERDICT: Reject Form A; rebase and use Form B plus the D3 tail append.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/R04RevHygiene.verdict.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/R04RevHygiene.md