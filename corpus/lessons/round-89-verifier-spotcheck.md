# Round 89 — verifier spot-check (kotoba)

author: hyaku closure (non-author integrator, @m_zfl)

Fresh non-author closure of kotoba round 89. Round base `a5b3b15c00b1de5db321e4226a0a7db17340e605`; lane tip / post-round HEAD `07d87d89fd2512022c6b2b3bf28e3b8aa80bb03f` (= pushed `refs/heads/master` at closure). Report `.ufo/reports/round-89/kotoba.md` (fleet commit `4221c8d2`, author `kotoba-shokunin <kotoba@shokunin.local>`, 2026-11-05 09:43:32 -03 — before the watchdog complete line 09:48:04). Dispatch digest copied from `.ufo/watchdog.log`: launch `2026-11-05T07:38:15-03:00 launch kotoba round=89 pgid=146869 driver=hyaku-inline attempt=1`; complete `2026-11-05T09:48:04-03:00 complete kotoba round=89; hyaku-inline attempt=1`.

## Conformance (step 1)

- Report committed in the fleet repo by the lane identity: `git -C /home/vgpnk/Projects/shokunin log --format='%an <%ae> %H %ad' -- .ufo/reports/round-89/kotoba.md` → `kotoba-shokunin <kotoba@shokunin.local> 4221c8d2f6acdf5f2b9bf2f02f653f525c38d3ad 2026-11-05 09:43:32 -03`. PASS.
- `## SHONEN` heading present, one line per box (4 boxes, all `[~]` with resolvable pointers; no `[x]`). PASS.
- Cited lane commits exist and are ancestors of the branch ref `master` (jj-colocated; ancestry tested against `master`, not `@{u}`): `43fc7840`, `0f2b8668`, `39704adc`, `12f4b6b9`, `f062a563`, `99ddd746`, `07d87d89`, plus base `a5b3b15c` — all `merge-base --is-ancestor` true, `master = 07d87d89fd25…`. PASS.
- Lane repo clean and pushed: `scripts/hyaku/jj-lane.sh state …kotoba-shokunin` → `branch=master local=07d87d89… remote=07d87d89… ahead=0 behind=0 tracked=0 untracked=0`; `git status --porcelain` → empty. PASS.
- Prompt fidelity: `templates/round-prompt.md` rendered with LANE=kotoba, ROUND=89, FLEET_ROOT, AXES diffs byte-identical against dispatched prompt lines 1–140; only the hyaku addendum §6 is appended. All round-level items and the five child-lane items embedded. PASS.
- Report is a real report, not a marker: named claims, landed-changes table with LOG entries and commit hashes, before→after measurements with counting commands, Sources & frontier with counting commands, trend verdicts, SHONEN assessment. PASS.
- Wave shape: `r89-w1` 12 seats (band 8–16), attack seats 4/12 = 33 % (≥25 %), connector 1 (≤2), WAVE-DONE + `r89-w1-results.json` before report. PASS. Defect note (status-neutral): no planner seat; the wave validator excludes `planner` (r88 precedent, disclosed in the report).

## Per-claim re-check

Method: claims resting on lane-owned gates are **evidence-verified** (PROTOCOL §Gate standard, Closure consequence — committed self-test tallies, frozen-run verdicts, revision measured; no sibling gate executed). Plain measurements (grep/wc/git/census) were **re-measured** by this closure.

**C1 — depth (capability: pre-freeze control executor `verifiers/check_freeze_gate.py`).** Verdict: **improved**.
- Re-measured before-absence: `git grep -n 'freeze_gate\|freeze-gate' a5b3b15c -- verifiers plans` → no matches, exit 1 (matches reported receipt `before-c1-absence.txt`). Instruments and fixtures present at `99ddd746` (`git ls-tree -r 99ddd746 -- verifiers/check_freeze_gate.py verifiers/fixtures/freeze-gate/ …` → 9 files).
- Evidence-verified after (committed `.ufo/waves/round-89/receipts/landing-measure.txt`, measured rev `99ddd746`): `c1-selftest` → `0 failure(s) over 30 assertions`, exit 0; `c1-unsat` → `REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL"; observed exit=0 stdout=w_added_red D5=PASS`, exit 1; `c1-fixed` → `freeze gate: 4 control(s) held — freeze may proceed`, exit 0. All three frozen-predicate arms met. Capability row in `SCORECARD.md` capabilities table, first working round 89.

**C2 — consistency (calibration sub-axis; instance-level D5 v3).** Verdict: **improved** (score held 10 at ceiling; the move is the discrimination).
- Evidence-verified after (same receipt): `c2-selftest` → `0 failure(s) over 37 assertions`, exit 0; `c2-tip` → `r86 routed defects closed 5 of 5`, `instance drift 0`, exit 0.
- Controls evidence-verified (committed `.ufo/waves/round-89/controls/final-*.txt`): `w_tip` expected 0 / observed 0; `w_healed` 0/0; `w_added_instance` 1/1 with `FAIL d5iii instance growth … commit_total 62>61, commit_unresolvable 2>1`, `instance drift 2`; `w_silenced` 1/1 (`FAIL d5i` + `snapshot_tampered`); `w_rerecorded` 1/1 (`snapshot_tampered`); `equivalence.txt` → `IDENTICAL observation`.
- Blindness before-state evidence-verified: `before-v2-selftest.txt` → `1 failure(s) over 16 assertions` (frozen `w_added_red` arm); `controls/v2-before-addinst.txt` records the v2 gate reading exit 0 on the added-instance world (recorded control, kept red by design — disclosed, not a regression).

**Plain re-measurements (this closure's own runs).**
- SOURCES rows: `git show a5b3b15c:corpus/SOURCES.md | grep -cE '^\|\s*S[0-9]{3,}\s*\|'` → **183**; same at `99ddd746` and `07d87d89` → **185**. Matches reported 183 → 185 (+2, both tier A: S258 external, S259 own-work).
- Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → exit **0**, verdict `ok` (33 pre-existing W04 duplicate-URL warnings, unchanged before/after).
- Kill rule: `git diff --stat 12f4b6b9 07d87d89 -- verifiers verifiers/fixtures plans` → empty. PASS.
- `SKILL.md` 600 lines at base and tip (within the 600-line budget). Registry receipt: `73 of 73 lane verifiers; phantom 0` at `99ddd746` (committed output).
- Axis harm: `git diff a5b3b15c 07d87d89 -- SCORECARD.md` → additions only (capability row, round-89 annotations, sources note); no axis value lowered; the `consistency` row carries its `calibration` mapping in-row (Fleet-2 rule); C1 works the lowest owned non-retired axis (depth 9 < consistency 10).

## Spot-check table (LEARNING.md discernment)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S258 Nosek et al., "The preregistration revolution", PNAS 2018 (tier A, scoped) | admit (lesson § Gate) | `https://pmc.ncbi.nlm.nih.gov/articles/PMC5856500/` re-fetched 2026-11-05 by closure | **agree** | `citation_title` = "The preregistration revolution"; byte size identical (196,972 B); both located quotes verbatim at the recorded HTML lines 1451 and 1472: "Preregistration of an analysis plan is committing to analytic steps without advance knowledge of the research outcomes." (17 words) and "researchers can achieve confirmatory research via replication. All initial experiments are treated as exploratory research." (15 words) — both ≤25 words, correctly located, and they ground the row's `teaches`. Caveat: the sha256 does not reproduce on re-fetch (`ee0d0560…` recorded vs `ca841f46…` observed at equal length) — dynamic PMC bytes; the located quotes, not the digest, carry the grounding. Routed below as an informational note. |
| S258 route (a) `PMC5813543` | reject (different article) | same URL re-fetched by closure | **agree** | 307,298 B (byte-identical to the lane's record); `citation_title` = "STOREKEEPER RELATED1/G-Element Binding Protein (STKR1) Interacts with Protein Kinase SnRK1" — a different article; rejecting it was correct, and the superseding route (PMC5856500) serves the cited paper. |
| S259 own-work (round-88 spot-check @ `a5b3b15c`, lines 73–74) | admit | `git show a5b3b15c:corpus/lessons/round-88-verifier-spotcheck.md` lines 73–74 | **agree** | routed defects 3 and 4 are on those lines; the recorded quotes are located (line-level) and ≤25 words (18 and 8 by `wc -w` on the quoted segments). |
| Assimilation of `/home/vgpnk/Projects/shokuknow/merge/kotoba/` | reject (55 id collisions; append-only rule) | committed `.ufo/waves/round-89/assimilation/collisions` receipt + CORPUS.md rule 2 | **agree** | adoption before the operator's renumber-or-retire ruling (open L0 `kotoba | round-88`) would violate the append-only SOURCES contract; honest stop. |

Sample: ≥1 admit (S258, S259) and ≥1 reject (route (a), assimilation) — duty met. Both knowledge entries open with the `source:` / `verified-at:` / `recheck:` provenance trio and cite their rows (`freeze-gate-round89.md` → S258+S259; `instance-d5-round89.md` → S259).

## Trend verdicts (closure)

- **expansion — improved.** Two admitted knowledge entries on uncovered ground (freeze-gate execution of declared controls; instance-level D5 against a base receipt), each `source:` citing a `mined` row (S258, S259) — provenance trios verified; coverage map +5 rows (`corpus/README.md` diff: two previously unindexed round-87/88 spot-checks + three round-89 rows; integrity receipt `unindexed=0`).
- **quality — unchanged.** No admitted entry failed a re-check; none superseded. Round-88 routed defects 1 and 5 answered (criterion Q81 landed at `corpus/QUALITY.md:100` citing the round-89 lesson; MERGE-REPORT count corrected with both commands in the lesson, append-only). Committed integrity receipt shows the disclosed honest reds only (`pointers.commit_unresolvable` = 1, pinned historical record).
- **discernment — improved.** The lane left the verdict to closure; this non-author spot-check agrees with the sampled admits (S258, S259) and rejects (route (a), assimilation). Per LEARNING.md, spot-check agreement on admits *and* rejects grades `improved`. The lane's gate decisions further caught an unsatisfiable control and an exit-only declaration before any score (addendum A1/A2, disclosed).

## Routed defects / notes for round 90 (status-neutral)

1. **S258 digest non-reproducibility (informational, this spot-check):** PMC HTML re-fetches differ in dynamic bytes at equal length; future rows should ground external quotes in line anchors + size + title, treating the raw sha256 as fetch-time metadata only.
2. **Carried by the lane's own routing (confirm, do not re-open):** mutation battery re-run on final (post-A2) bytes; duplicate control names in the freeze gate (documented invalid, A2.4); `report_dead` symlink class (Q79 location flip).
3. **Seat deaths:** 3 of 12 scribe seats landed nothing; the L1 performed and disclosed the work (lesson § Seat record). Honest accounting, no defect; watch for recurrence.
4. **No planner seat** in the wave (validator excludes `planner`; disclosed r88 precedent) — protocol minimum role split still lists 1× planner; keep the deviation disclosed each round it holds.
5. **Open L0 questions, routed around correctly:** `kotoba | round-88` (assimilation renumber-or-retire; C1 kill ruling), `kotoba | round-73` (gate-registry home). Not answered by this closure.
6. **Promotion note for the operator:** all four SHONEN boxes now cite resolvable, non-author-checkable evidence (this round adds two gate-registry rows to SKILL.md, an end-to-end run of both instruments, root-runnable commands, and an unchanged-PROVINCE overlap scan). Promotion review is operator-owned; nothing here bars it. No `[x]` was written by this closure (promotion is not a closure act).

Verdict: **kotoba round 89 admitted** — every claim verifies (C1 evidence-verified + re-measured; C2 evidence-verified), no axis harmed, census exit 0, prompt and report conformant.
