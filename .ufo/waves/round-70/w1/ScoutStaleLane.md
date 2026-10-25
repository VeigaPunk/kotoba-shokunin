# ScoutStaleLane — round 70 wave 1 (scout, read-only)

## Verdict (paste-ready)

Stale-lane: kotoba round=70 (hyaku-inline attempt=1, launched 2026-10-25T08:32:57-03:00, pgid=4135592) has been open 1436 s at 2026-10-25T08:56:53-03:00, which is more than 900 s (two 450 s driver ticks): **progressing**. Since launch there are 23 commits authored by kotoba-shokunin (tip 16b212a), and the protocol's `find -newermt` lists 206 files, 15 of them in committed lane scope. No other kotoba mission is open: watchdog.log has 4 earlier kotoba launches with no closing line (r16, r61, r63, r65), and each one is closed by a filed report at `.ufo/reports/round-<N>/kotoba.md` and by a later launch.

## Basis

- Rule: PROTOCOL.md lines 171-184 (§ Round-robin rounds). Mission age is measured from the launch timestamp, not the tick counter. "Progressing" means a commit authored by the lane, or files modified under the lane repo since launch. "Silent" means neither. If the only activity is commits by sibling lanes, the grade is `progressing-weak`.
- Tick: the driver comment `scripts/shokunin-watchdog.sh:6` says "tick 450s", and line 52 sets `TICK_SECONDS=${TICK_SECONDS:-450}`. Two ticks = 900 s.
- watchdog.log: 1334 lines, mtime 2026-10-25 08:50 -03:00. Its last line is `2026-10-25T08:50:16-03:00 launch mado round=37`.

## Findings

### F1 — kotoba round 70 is the only kotoba launch with no closing line through end of file
The script below walks every kotoba launch. A launch counts as closed when a later complete, lane-dead-no-report, or lane-round-failed line names the same round.
Command:
`awk '$3=="kotoba"{print NR": "$0}' .ufo/watchdog.log | awk '…launch opens; same-round close event clears…'`
Output:
```
UNCLOSED-BEFORE-NEXT-LAUNCH: 376: 2026-10-15T01:50:57-03:00 launch kotoba round=16 pid=2684804
UNCLOSED-BEFORE-NEXT-LAUNCH: 951: 2026-10-23T15:50:34-03:00 launch kotoba round=61 pgid=136767 driver=hyaku-inline attempt=1
UNCLOSED-BEFORE-NEXT-LAUNCH: 1078: 2026-10-23T20:33:30-03:00 launch kotoba round=63 pgid=2229890 driver=hyaku-inline attempt=2
UNCLOSED-BEFORE-NEXT-LAUNCH: 1127: 2026-10-24T01:56:02-03:00 launch kotoba round=65 pgid=2648025 driver=hyaku-inline attempt=1
OPEN-AT-EOF: 1332: 2026-10-25T08:32:57-03:00 launch kotoba round=70 pgid=4135592 driver=hyaku-inline attempt=1
```
Event types in the log (`awk '{print $2}' | sort | uniq -c`): launch, complete, lane-dead-no-report, lane-round-failed, launch-fail, steer, wrap, watchdog, and tick=N. A grep for wrap, watchdog, steer, tick, lane-round-failed, and launch-fail finds no line after line 402 (2026-10-15). So in the hyaku-inline era, only launch, complete, and lane-dead-no-report lines can open or close a mission.

### F2 — mission age
The round 70 launch was at 2026-10-25T08:32:57-03:00, which is 11:32:57Z. Measured at `date +%FT%T%z`, which returned 2026-10-25T08:56:53-0300, the age is 1436 s, or 3.19 ticks. That is over the 900 s threshold. This scout's run sits inside the round, so the age keeps growing until a complete line lands.

### F3 — round 70 is progressing, backed by commits the lane authored
- `git log --since='2026-10-25T08:32:57-03:00' --all --format='%an <%ae>' | sort | uniq -c` returns `23 kotoba-shokunin <kotoba@shokunin.local>` and `2 protocol-shokunin <protocol@shokunin.local>`. The round-70 commits include 53de0ac (frozen plan, 08:42:21), a647fa7 (pre-data controls), 8edeb49 (C2 and C1 work), aa9c9ad, ac3c0f1, and 16b212a (08:52:59). `git rev-parse HEAD master` returns 16b212a390c7ce68b6bce49b2c3766b154fbcbae for both, which matches the measured tip.
- `find /home/vgpnk/Projects/shokunin/kotoba-shokunin -newermt 2026-10-25T08:32:57-03:00 -type f -not -path '*/.git/*' | head` returns a non-empty list. The first entries are `corpus/knowledge/skill-eval-artefacts-round70.md`, `corpus/lessons/round-69.md`, `corpus/lessons/round-70.md`, `corpus/SOURCES.md`, `corpus/README.md`, `verifiers/corpus-baseline.json`, `verifiers/verify_skill_checklist.py`, a `__pycache__` .pyc file, `verifiers/check_r69_routed_repairs.py`, and `verifiers/check_skill_evals.py`. The full count is 206.
- Calibration caveat: the protocol's `find` excludes only `.git`. By top-level directory, the 206 files split into 161 `.jj` internals, 32 `.ufo` (wave or seat scratch and reports), 5 `corpus`, 5 `verifiers`, and 1 each in `LOG.md`, `SCORECARD.md`, `SKILL.md`, `plans`, and `considerthese`. Committed lane scope is therefore 15 files, not 206. The grade does not depend on this, because the lane-authored commits are enough on their own.
- This is not `progressing-weak`: the lane has its own commits, so the sibling (protocol-shokunin) commits are not the only activity.

### F4 — no other kotoba mission is open
Each of the 4 earlier launches with no closing line has a report and a later launch. Reports were checked with `ls -la --time-style=full-iso .ufo/reports/round-<N>/kotoba.md`.

| Launch | Report at the report path | What closes it |
|---|---|---|
| r16, 2026-10-15T01:50:57 | yes, mtime 2026-10-13 16:44:48 | many later kotoba launches. The log lines for this period are lane-round-failed and marker lines, from before hyaku-inline. |
| r61, 2026-10-23T15:50:34 | yes, 2026-10-23 17:38:54 | filed before the r62 launch at 17:40:02. The log has no complete line for r61. |
| r63 attempt=2, 2026-10-23T20:33:30 | yes, 2026-10-24 00:06:42 | relaunched at 22:40:29, completed 00:08:49 |
| r65, 2026-10-24T01:56:02 | yes, 2026-10-24 03:16:40 | relaunched at 02:24:03, completed 03:17:11 |

There is no report yet for round 70: `ls .ufo/reports/round-70/kotoba.md` returns "No such file or directory". That fits a mission that is still running.

### F5 — process check doesn't settle it either way
`ps -o pid=,etime=,cmd= -g <pgid>` returns nothing for pgids 136767, 2229890, 2648025, or 4135592. So the round 70 pgid recorded in the log is not a live process group.
[INFERENCE] Under the hyaku-inline driver, the L1 runs as a subagent inside the orchestrator session, so the logged pgid doesn't track it. The peer roster shows `L1Kotoba70` as "running", which I did not observe through `ps`. Liveness is graded only from file and commit activity, as the protocol requires.

### Side observation (outside the scoped question)
kotoba round=68 has two complete lines, at watchdog.log:1242 (2026-10-24T23:17:49) and :1249 (2026-10-25T03:23:10). This does not affect whether anything is open.

## Remaining unknowns
- Whether the driver daemon or the hyaku-inline orchestrator will write a complete line for round 70. That has not happened yet.
- The 2 protocol-shokunin commits since launch are not examined here. They don't affect the grade.

## Tooling
No installs or updates.
