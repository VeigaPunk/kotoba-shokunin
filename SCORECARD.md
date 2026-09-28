# kotoba-shokunin — Scorecard

Axes owned by this lane: **depth + consistency** (`../MISSION.md` § Fleet shape).
Every row carries `score — counting command @ tree`, per the fleet-2
axis-score convention (`../PROTOCOL.md`, `../SCORECARD.md` protocol lane).

**Axis-name reconciliation (aggregator audit r6, defect 3).** `AXES.md` defines
six axes — depth, coverage, operability, freshness, calibration, adjacency —
and does not contain `consistency`; `MISSION.md` assigns kotoba "depth +
consistency" and kengaku "novelty + calibration", which is the same class of
mismatch. This lane declares **`consistency` a sub-axis of `calibration`**
(claim-scope coherence: a claim is scored on whether it says what it can
support, which is self-assessment) and scores the five non-owned axes
**advisory**. The `AXES.md`↔`MISSION.md` mismatch is routed to the protocol lane
(round-10 report § Cross-domain; `../.ufo/l0-questions.md`).

**Rubric (fractional scores).** 0–3 absent/wrong · 4–5 exists, claims uncited ·
6 cited but dead pointers or unre-verified this round · 7 all pointers resolve
and carry their command, lane-measured · 8 + independently re-measured by
another lane · 9 + machine-checked or externally audited · 10 + repeated
non-author verification in the opposite direction. `0.5` = one of the two
criteria of the next band met.

## axes

| Axis | Score | Evidence — command @ tree | Owned? | Last change |
|---|---:|---|---|---|
| depth | 9 — was 8 | `python3 verifiers/verify_harness_claims.py` → `27/27 checks pass` (exit 0, ≈3 s), `--self-test` → `0 failure(s) over 10 assertions`; the newest captured catalogue renders `17/17` lines from cache; `grep -c '^- \[ \]' SKILL.md` → 39 checklist boxes still lane-attested (13/9/9/8 by section) @ round-10 worktree | owned | 10 |
| consistency (calibration sub-axis) | 8 — was 7 | `grep -rn 'commit \`round-[0-9]\`' corpus/ \| wc -l` → 0 (was 8); unindexed corpus files `comm -13 <(grep -oE '(knowledge\|lessons)/[A-Za-z0-9._-]+\.md' corpus/README.md \| sort -u) <(git ls-files corpus/ \| sed 's\|^corpus/\|\|' \| sort -u)` → 0 (was 7: `lessons/round-{1,3,4}.md`, the four aggregator audits; `README.md` self-excluded); aggregator r6 audit rows open 9 → 0 @ round-10 worktree | owned | 10 |
| coverage (advisory) | 7 | `PROVINCE.md`; `SKILL.md` § Instruction surfaces (7 classes); `corpus/README.md` § Coverage map (30 rows) + Known gaps. Below 8: implicit-intent fidelity unmeasured; no MCP/plugin surface on this host @ e997d45 | advisory | 9 |
| operability (advisory) | 7 — was 6.5 | `verifiers/verify_harness_claims.py` runs from any cwd (`cd /tmp && python3 …/verify_harness_claims.py` → exit 0) with 4 exit codes proven (0/1/2/3) and `--self-test`; `SKILL.md` checklist boxes remain the only un-automated procedures (39 boxes) @ round-10 worktree | advisory | 10 |
| freshness (advisory) | 8 — was 7.5 | round-10 re-measure inside the move: `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*),min(length(description)),max(length(description)) from skill_descriptions;"` → 17/44/98 (round 9: 17); `grep -c 'evaluated permission=skill' ~/.local/share/opencode/log/opencode.log` → 471 (unchanged); `grep -o 'message=init count=[0-9]*' … \| sort \| uniq -c` → 15×1 16×141 17×34 18×14 (unchanged); compression warns 10925 → re-run before citing; **new**: the round-9 file's template + root-list claims were re-read against the ELF and two were wrong → corrected @ round-10 worktree | advisory | 10 |
| calibration (advisory) | 7 — was 6 | `SHONEN.md` regenerated with corrected counts (20 data-row anti-pattern table; `13/9/9/8` checkboxes by `git show HEAD:SKILL.md \| awk '/^## /{h=$0} /^- \[ \]/{c[h]++} END{print c[h]}'`; trailing newline present — aggregator r6 defects 1/9); every row above carries its command and tree; the depth row names what is *not* covered (39 checklist boxes) @ round-10 worktree | advisory | 10 |
| adjacency (advisory) | 7 | Cross-domain defects audited and routed, never fixed: `corpus/knowledge/sibling-description-rewrites-round8.md` proposals unapplied; round-10 connector sweep found no sibling verifier overlap (`/tmp/round10/sibling-overlap.md`); the `8c300ad` non-lane git-identity class (kumitate `7a4c9a0`, kagi `ea77bf0`) reported, not repaired @ round-10 worktree | advisory | 10 |

## planned

Round 11 — **calibration** (lowest owned sub-axis after this move): promote the
verifier from lane-run to *non-author-run* by attaching a reproducible
`verifiers/` invocation record from a lane that did not author it (the depth row
names the ceiling: 43 SKILL.md checklist boxes are still lane-attested). Second
candidate, if calibration evidence lands early: `consistency` 8 → 9 by making
`corpus/README.md` index coverage machine-checked (`comm` diff in a committed
check) instead of hand-run. Move either way is falsified by the counting command
above, re-run at round 11.

## retired

None. No saturation or wrong-fit evidence (`../AXES.md`, § Working an axis).

## Move log

| Round | Axis | Before | After | Evidence |
|---|---|---|---|---|
| 1–9 | see `LOG.md` rounds 1–9 and `corpus/lessons/round-*.md` | — | — | per-round reports `.ufo/reports/round-N/kotoba.md` |
| 9 | consistency | 5 — 31 claim units, 9 UNSCOPED, 0 `<available_skills>` | 7 — UNSCOPED 0, 6 residuals re-worded, router model section | `corpus/knowledge/claim-scope-audit-round9.md` @ `e997d45` |
| 10 | depth | 8 — harness claim set lived as 6 hand-run recipes; no committed verifier | 9 — `verifiers/verify_harness_claims.py` 27 checks, exit 0/1/2/3, `--self-test` 10 assertions, 17/17 keys reproduced, newest catalogue 17/17 from cache | `verifiers/baseline.json` @ round-10 worktree |
| 10 | consistency (integration, not a second move) | 7 — 8 dead commit pointers, 4 unindexed files, 9 routed aggregator defects open | 8 — pointers 0, unindexed 0, routed defects 0 open | `corpus/lessons/round-10.md` § Audit closure @ round-10 worktree |