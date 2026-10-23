# ScribeReportSkeleton
role: UFO-FSD scribe
item: Draft the round-63 report skeleton from the frozen plan; do not write the fleet report.

## Findings
1. The frozen plan names depth and calibration/consistency as the active axes, identifies calibration/consistency (8.5) as the lowest owned axis, and keeps the stagnation nudge dormant (`depth 9 < 10.0`). Evidence: `plans/round-63.md:5-10`.
2. The frozen gates are C1's `python3 -B verifiers/check_scoped_rules_v32.py --self-test`, with exact output at `plans/round-63.md:35-49`, and C2's `python3 -B verifiers/check_r63_routed_repairs.py --rev <rev>`, with five committed-byte checks at `plans/round-63.md:88-109`.
3. **Conflict for the canonical judge, verbatim:** `plans/round-63.md:111-117` says: “At the r62 tip `35d44b4b` (before this round's corrections) the counter prints `0 of 5`, exit 1: check 1 fails (the file is untracked), 2–3 fail (no correction line names the receipt revision or the sizes), 4 passes (an empty delta is a prefix — recorded honestly as a check that only bites when text is rewritten), 5 fails.” It then says: “The target is 5 of 5; the do-nothing control (the r62 tip) scores 0 of 5 on the four content checks, so it cannot meet the target.” The stated `0 of 5` conflicts with the same paragraph's explicit “4 passes”; this report does not reconcile it.
4. Live lane-state evidence (read-only command; no attribution to this seat):
   Command: `git status --porcelain && git rev-parse HEAD && git show -s --format='%H%n%s' HEAD`
   Output:
   ```text
   ?? .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
   ?? .ufo/waves/round-63/w1-dispatch.err
   ?? .ufo/waves/round-63/w1-dispatch.json
   ?? .ufo/waves/round-63/w1-spec.json
   ?? .ufo/waves/round-63/w1/
   ?? verifiers/check_scoped_rules_v32.py
   8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
   8c4cefa8e1b751d5f93dbcc65349b8e985b102d8
   round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
   ```
   These are observed lane files at scribe time; this seat changed none of them.
5. The requested r62 tone source was not present at the lane path `.ufo/reports/round-62/kotoba.md` (`read` returned `Path ... not found`). The hard bounds prohibit touching the fleet repo, so that report was not fetched elsewhere. No gates or tests were run, no tool was installed or updated, and no product code was changed. The only intended touched surface is this report file.

## Artifacts
Draft report body (fenced markdown as requested; not written to the fleet repo):

````markdown
## Work performed
Plan-declared scope (this skeleton is not execution evidence): C1 targets depth by closing the sixth frozen erratum survivor G9, `e2f-compound-purpose-outside-citation`; C2 targets calibration/consistency by closing and counting the five defects routed by the r62 non-author spot-check. The source-frontier step opens S119 and re-probes S049. Record execution only from the seats' receipts and committed bytes.

## Landed changes
Plan-declared targets, to be supported by path-level evidence at close:
- Add `verifiers/check_scoped_rules_v32.py` from `verifiers/check_scoped_rules_v31.py` for G9. Do not edit frozen `verifiers/check_scoped_rules.py`, `verifiers/check_scoped_rules_v31.py`, `verifiers/check_erratum_absorption.py`, or `verifiers/check_routed_repairs_v2.py`.
- Add `verifiers/check_r63_routed_repairs.py`; its five checks are `late-write-tracked`, `receipt-rev-named`, `entry-size-named`, `append-only`, and `noharm-arms-named`, computed from committed bytes at the supplied revision.
- Adopt the inherited r62 late-seat file as C2 item 1, and append the correction described by the plan; do not rewrite earlier `LOG.md` bytes.
- Add S119 with its URL, access date, located quote (at most 25 words) and snapshot; re-probe S049 under both `Accept` forms and append its correction/SOURCES note as described in the plan.

## Before -> after measurements
- Commit refs: before `<MEASURED>` -> measured report revision `<MEASURED>`.
- C1 before/control: `survivors closed <MEASURED> of <MEASURED>` (plan-declared v31 expectation: 5 of 6). After, report the observed counts: worlds reject `<MEASURED> of <MEASURED>`; eligible rows pass `<MEASURED> of <MEASURED>`; survivors closed `<MEASURED> of <MEASURED>`. Frozen target output:
  ```text
  worlds reject 7 of 7; eligible rows pass 4 of 4
  survivors closed 6 of 6
  must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
  ```
- C2 before at the r62 tip: `<MEASURED> of <MEASURED>` (plan states 0 of 5, but its explicit check-4 pass is a count conflict; see the finding above). After: `<MEASURED> of <MEASURED>` (frozen target: `r62 routed defects closed 5 of 5`).
- Sources census: before 16 W04 (`census-before.txt`); after `<MEASURED>` W04 (plan expects 17 if S119's URL is new; if it duplicates an existing URL, name the duplicate and record a re-open instead).

## Sources & frontier
Open one new source row, S119, on transparent, appended, linked correction/errata practice, cited by C2's repair method. Put the URL, access date and a located quote of at most 25 words in the round-63 lesson `## Gate`, with a snapshot under `.ufo/waves/round-63/snapshots/`. Re-probe S049's cursor `.md` rejection reason under both `Accept` forms; correct it in the round-62 lesson's Gate and append the SOURCES note, not rewrite it. Census command:
```text
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
```

## Trend verdicts
Plan axes: depth + consistency (calibration sub-axis). C1 works depth; C2 works the lowest owned axis, calibration/consistency (8.5), below depth (9). The five non-owned axes are advisory under `SCORECARD.md`; the all-axes reading of “lowest non-retired axis” remains the open round-47 L0 question. The stagnation nudge stays dormant (`depth 9 < 10.0`). No measured trend outcome is asserted by this plan-derived skeleton.

## SHONEN
The plan routes defect 5 as “SHONEN boxes (operator-owned; no change).”

## Round shape
Wave 1 build (32–64, policy v1); wave 2 falsify (32–64) only if wave 1 yields at least 32 distinct attack items; residual at most 8 if leftovers remain; total at most 128. The §3 planner seat is held by the L1; any bounded planning data-walk rides a scout/revenger item and is named in the report. The lane repo is the L1's only write target; seats write only their own report under `.ufo/waves/round-63/<wave>/`. Apply the tooling authorization and pacman pause, and keep every `Report:` trailer relative to the lane repo.

## Stale-lane
At base, `git status --porcelain` showed one untracked lane file: `.ufo/waves/round-62/w2/FalsifyC2HonestH1.md`, an r62 late seat write found by spot-check defect 1. C2 item 1 adopts it; it is never silently dropped.

## Tool installs
Follow `~/.omp/agent/RULES.md`: no pacman transactions during the pause; use `uv tool`, `npx`, or an official binary if a tool is needed. This scribe seat performed no tool install or update.
````

## Verdict
INFORMS — this is a plan-derived skeleton, not a claim that gates, repairs, sources, or measurements landed. To change my mind on execution, I would need the relevant committed bytes at the measured revision, exact gate/census outputs, and source/snapshot receipts. The C2 tally conflict above remains explicitly unresolved for the canonical judge.
