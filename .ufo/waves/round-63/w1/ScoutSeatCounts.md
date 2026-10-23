# ScoutSeatCounts

role: scout
item: ScoutSeatCounts
axes: calibration (does the r62 report's wave-2 "39" equal `check_seat_counts.py`'s denominator N)
rev measured: report tip `e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02`, plan base `35d44b4b4dcdda234b5dbff7af37e432fec55f05` (w2 tree identical), freeze `306381da`, lane HEAD at probe `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`
installs: none

Method is `verifiers/check_seat_counts.py` `score()`: N = non-empty `items[].name` in the spec; K = those names whose `<name>.md` is a direct child of the report dir in `git ls-tree -r --name-only <rev>`; missing = spec names without that file; unmatched = `*.md` children the spec does not name. `swarm-registry.json` is not an `.md`, so it is neither a seat report nor unmatched.

## Findings

1. Declared seats (spec N) = **39**, unique, no duplicate names.
   Command: `python3` over `.ufo/waves/round-62/w2-spec.json` counting `items[].name`.
   Output: `items 39` / `named 39` / `unique 39` / `dups []`.

2. Committed reports at the report tip, the plan base, and current HEAD = **35 of 39**. Unmatched **0**. Exit 1.
   Command (same line at all three revs):
   `python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w2-spec.json --dir .ufo/waves/round-62/w2 --rev <rev>`
   Output:
   `seat reports committed 35 of 39; missing 4: FalsifyControls, FalsifyV31Harm, FalsifyC2HonestH1, FalsifyStatementSemantics; unmatched 0: none`
   `git ls-tree` at those revs: `files=36 md=35` (the 36th path is `swarm-registry.json`).
   `git diff --stat 35d44b4b… e53b6e5c… -- .ufo/waves/round-62/w2 .ufo/waves/round-62/w2-spec.json` is empty; a set compare of the two `ls-tree` listings is `identical`.

3. Missing names (committed, at tip/base/HEAD): `FalsifyControls`, `FalsifyV31Harm`, `FalsifyC2HonestH1`, `FalsifyStatementSemantics`.
   Unmatched names: none.
   Working tree adds one untracked file the counter does not count:
   `git status --porcelain -- .ufo/waves/round-62/w2` → `?? .ufo/waves/round-62/w2/FalsifyC2HonestH1.md`.
   Disk `*.md` count is 36; committed `*.md` count stays 35. `FalsifyC2HonestH1` remains missing.

4. Registry `.ufo/waves/round-62/w2/swarm-registry.json` (`schema` `ufo-swarm-registry-v1`, `wave` `kotoba-r62-w2`, `reportDir` `.ufo/waves/round-62/w2`) has **39** member keys. `spec-not-reg []`, `reg-not-spec []`. Roles: reviewer 17, critic 10, scout 5, mutation-tester 3, sentinel 2, revenger 1, connector 1 (sum 39). No status field (`statuses {'None': 39}`). The four missing names are registry members (`kind: spawn`); the registry does not record a report.

5. The r62 report's wave-2 figure **39 is the spec's count**. Fleet report `.ufo/reports/round-62/kotoba.md:84` (commit `def4b9f`, porcelain clean):
   `**Wave 2** kotoba-r62-w2, policy v1: **39 spawn** … (core attack roles 30 of 39, 77%).`
   Same "39 spawn" at line 24. N from `items[].name` is 39, and the registry key set is that same 39. The figure is not a file count and not K.

6. The same paragraph's numerator is not the counter at the tip the report cites. Line 84 says `**32 reports committed** (29 at the first freeze, three more landed and were swept into 306381da); at close seven seats had still not settled`.
   Command at `306381da`:
   `seat reports committed 32 of 39; missing 7: FalsifyControls, FalsifyV31Harm, FalsifyC2HonestH1, FalsifyClaimC2, FalsifyScorecard, FalsifyStatementSemantics, FalsifyGateRegress; unmatched 0: none`
   Exit 1. `md=32`. That matches "32 committed" and "seven … not settled".
   Between `306381da` and `e53b6e5c` exactly three paths appear (set difference, empty reverse):
   `FalsifyClaimC2.md`, `FalsifyGateRegress.md`, `FalsifyScorecard.md`.
   At the cited tip `e53b6e5c` the counter is **35 of 39**, missing 4, not 32 of 39 missing 7. Lane `LOG.md` § Round 62 repeats "39 spawn" and "Round total 83 seats" and does not restate the wave-2 committed numerator (the wave-2 sentence is truncated in the log at "Dead seat…").

7. Contrast, not the assigned denominator: wave 1 at base is a different 39.
   `python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w1-spec.json --dir .ufo/waves/round-62/w1 --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05`
   → `seat reports committed 35 of 39; missing 4: ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 3: ExecNoHarmRun.md, ScoutRegistry.md, ScribeLessonQ57.md`
   `w1-spec.json` `items` length 39. Receipt `.ufo/waves/round-62/controls/seat-counts-r62.txt:5` is this wave-1 line at `e6da78bb`, not wave 2.

## Artifacts

No lane product. The counting command and its outputs are the artifact:

```
$ python3 -B verifiers/check_seat_counts.py \
    --spec .ufo/waves/round-62/w2-spec.json \
    --dir .ufo/waves/round-62/w2 \
    --rev e53b6e5c0aaa1ef2b0861b9399fef44f8b907f02
seat reports committed 35 of 39; missing 4: FalsifyControls, FalsifyV31Harm, FalsifyC2HonestH1, FalsifyStatementSemantics; unmatched 0: none
exit=1

$ python3 -B verifiers/check_seat_counts.py \
    --spec .ufo/waves/round-62/w2-spec.json \
    --dir .ufo/waves/round-62/w2 \
    --rev 306381da
seat reports committed 32 of 39; missing 7: FalsifyControls, FalsifyV31Harm, FalsifyC2HonestH1, FalsifyClaimC2, FalsifyScorecard, FalsifyStatementSemantics, FalsifyGateRegress; unmatched 0: none
exit=1
```

## Verdict

INFORMS. The stated wave-2 figure 39 **is** the spec's count: `w2-spec.json` has 39 `items[].name`, the registry has those same 39 keys, and the counter's N is 39. Committed reports at the cited tip are 35, not 39; missing are the four names above; unmatched is none.

The report's "32 reports committed" equals the counter at `306381da` only. At `e53b6e5c` / `35d44b4b` it is 35 of 39. I would change the "39 is the spec count" half if N were taken from something other than `items[].name` (it is not: that is what `score()` counts). I would drop the numerator mismatch if `e53b6e5c:.ufo/waves/round-62/w2` listed 32 `*.md` files; it lists 35.
