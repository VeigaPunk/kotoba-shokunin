# FalsifySeatCounts — round 62 wave 2

Attack: seat accounting for wave 1 `kotoba-r62-w1`. Lane tip `e6da78bbe420722dd18a13182a7c4b64ce02f005` (HEAD). Counter `verifiers/check_seat_counts.py` blob `26ac95a490750a8add515db38e1a4e644c2dda94`, sha256 `15311042ea31d9df63843af8cf865e35dc9065497bd43b59ab21cfc27c32a9b1` (worktree equals tip; introduced `9f03dcd`, unchanged since). Spec blob `9709ab66d742c59716adc3b3358ae18f81a4515d` is the same at `3e7aed9b` and at the tip. No installs.

Rerun date: `date -u` → `Fri 23 Oct 2026 09:33:24 PM UTC` (`2026-10-23T21:33:24Z`), exit 0.

## Commands (cwd = lane)

```
$ python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w1-spec.json --dir .ufo/waves/round-62/w1 --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
seat reports committed 35 of 39; missing 4: ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 3: ExecNoHarmRun.md, ScoutRegistry.md, ScribeLessonQ57.md
exit=1
```

```
$ python3 -B verifiers/check_seat_counts.py --spec .ufo/waves/round-62/w1-spec.json --dir .ufo/waves/round-62/w1 --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
seat reports committed 34 of 39; missing 5: ExecSuccessor31, ScribeLesson62, ScribeScorecard62, MutAbsorbMutants, ScribeReportSkeleton; unmatched 0: none
exit=1
```

Same line and exit 1 at the tip's parent `f9ab0812a574c369aa5cb94616e6ddffd1c5202b` (the receipt commit). `git merge-base --is-ancestor 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85 e6da78bbe420722dd18a13182a7c4b64ce02f005` exit 0.

`git ls-tree -r --name-only` under `.ufo/waves/round-62/w1`: 34 paths at `3e7aed9b`, 38 paths at the tip, all `*.md`, no `swarm-registry.json`. The four paths added by `e6da78b` (`git diff-tree --name-status -r e6da78b`) are `ExecNoHarmRun.md`, `ExecSuccessor31.md`, `ScoutRegistry.md`, `ScribeLessonQ57.md`. The same commit also `M` `ScribeEntry62.md`, `LOG.md`, and `SCORECARD.md`.

## 39 spec names — holds

`git show e6da78b:.ufo/waves/round-62/w1-spec.json`: `items` length 39, 39 unique `name`s, no duplicates. `w1-dispatch.json` agent-name set equals that set (both directions empty). Roles: executor 14, scribe 7, scout 5, reviewer 5, critic 4, connector 1, sentinel 1, simplifier 1, mutation-tester 1.

Spec order:

1. ExecAbsorbInstrument
2. ExecInstancesA3
3. ExecInstancesA4
4. ExecInstancesA1
5. ExecInstancesA2
6. ExecSuccessor31
7. ExecSuccessorC2
8. ExecDishonestTrees
9. ExecControls
10. ExecNoHarm62
11. ExecCensus62
12. SrcRulesFrontmatter
13. ExecRegistryRows
14. ScribeEntry62
15. ScribeQ57
16. ScribeLesson62
17. ScribeLog62
18. ScribeScorecard62
19. ScribeSourcesS118
20. ScoutPriorReceipts
21. ScoutCounterApi
22. ScoutRepairsApi
23. ConnSibling
24. ScoutSourcesShape
25. RevPlanScope
26. CriticC1Hollow
27. CriticC2Shortcut
28. CriticE1Class
29. SentPageInjection
30. RevS118
31. RevSentNovelty
32. SimplEntry62
33. MutAbsorbMutants
34. RevRegistryHonesty
35. RevClaimSeparation
36. RevBaseline
37. ScribeReportSkeleton
38. ScoutR62Candidates
39. ExecGateArms

`score()` (`verifiers/check_seat_counts.py:75-89`) counts `items[].name` against direct-child `<name>.md` only. Missing stays in spec order. Unmatched is sorted filenames. Denominator is `K + len(missing)`, which equals 39 here.

## Receipt at `3e7aed9b` — holds; tip ledger — fails

`.ufo/waves/round-62/controls/seat-counts-r62.txt` (blob `683ad682d8d88019452831a6e042ffa63668c495`, commit `f9ab081`) quotes the `3e7aed9b` line and `exit=1`. The rerun matches that line exactly.

`LOG.md:2555` quotes that same receipt and pins `measured at 3e7aed9b`. That quoted measurement is true. It is not the count at the commit that contains the sentence.

These sentences are in `e6da78b`, the commit that added `ExecSuccessor31.md`:

- `LOG.md:2547` — the five dead seats `ExecSuccessor31`, `ScribeLesson62`, `ScribeScorecard62`, `ScribeReportSkeleton`, `MutAbsorbMutants` "are named, not replaced." **Fails.** `ExecSuccessor31.md` is status `A` in that commit. The tool at that rev drops it from missing.
- `LOG.md:2563` — "39 spawn, 34 reports, 5 dead" and "Build-completion call: 5 seats (executor 2, scribe 2, scout 1)." **Fails on the report count.** Spawn 39 holds. At the same rev the tool prints 35 of 39, missing 4 (`ScribeLesson62`, `ScribeScorecard62`, `MutAbsorbMutants`, `ScribeReportSkeleton`), unmatched 3, exit 1. The four added basenames are 2 executor-named, 1 scribe, 1 scout. No fifth completion report is in `diff-tree` of `e6da78b`. The prose order at `:2547` also swaps `ScribeReportSkeleton` and `MutAbsorbMutants` versus the tool; the set of five is the `3e7aed9b` missing set, not the tip missing set.
- `SCORECARD.md:369` — "seat count 34 of 39 here" and "wave 1 39 (34 reports, 5 dead), build-completion call 5". **Fails** the same way. That line is committed at the tip, where the counter prints 35 of 39.

The five names match the tool only at `3e7aed9b` and `f9ab081`. They do not match the tool at the tip.

## Completion-call reports vs spec seats

| basename | in `w1-spec.json` `items[].name` | tip classification |
|---|---|---|
| ScoutRegistry | no | unmatched `ScoutRegistry.md` |
| ExecNoHarmRun | no | unmatched `ExecNoHarmRun.md` |
| ScribeLessonQ57 | no | unmatched `ScribeLessonQ57.md` |
| ExecSuccessor31 | yes (item 6, role executor) | counted in K (35). Not missing. |

`ScoutRegistry`, `ExecNoHarmRun`, and `ScribeLessonQ57` are not wave-1 spec seats. The counter does not ignore them: they are the unmatched set. There is no completion-call exclusion in `score()`.

`ExecSuccessor31` **is counted as a wave-1 spec seat** at the tip, because the completion report was committed at the spec seat's path `.ufo/waves/round-62/w1/ExecSuccessor31.md`. That is why K moved 34 → 35 inside `e6da78b`. The "not counted as wave-1 spec seats" check **fails** for this name.

Headers (tip bytes): `ExecSuccessor31.md` records creating `verifiers/check_scoped_rules_v31.py`; `ExecNoHarmRun.md` is the no-harm battery run at `3e7aed9b`; `ScoutRegistry.md` is the registry/census scout measured at `3e7aed9b`; `ScribeLessonQ57.md` records creating `corpus/lessons/round-62.md` and Q57. None of those three non-spec names fill `ScribeLesson62`, `ScribeScorecard62`, `MutAbsorbMutants`, or `ScribeReportSkeleton`.

## ScribeEntry62 at `3e7aed9b`

Historical object **is in git**:

- `git rev-parse 3e7aed9b:.ufo/waves/round-62/w1/ScribeEntry62.md` → `dfd80915fcce1a6de11c2d2a534a7cd7ecfa2ea9`, exit 0
- `git cat-file -t` → `blob`; `cat-file -s` → 12879 bytes, 149 lines
- first commit of the path: `3e7aed9b` ("wave-1 evidence (34 of 39 seat reports)")
- that commit is still an ancestor of the tip

Path bytes at the tip are **not** those bytes:

- `git rev-parse e6da78b:.ufo/waves/round-62/w1/ScribeEntry62.md` → `36be91ae558648c315f9e3a8d7601ae219df642a` (3286 bytes, 28 lines)
- `git diff --numstat 3e7aed9b e6da78b -- .ufo/waves/round-62/w1/ScribeEntry62.md` → `16 137`
- 49 of 149 old lines still occur in the tip file; 16 of 28 tip lines are new
- the `3e7aed9b` file is the wave-1 draft ("It did not write that product file"; fenced draft for `corpus/knowledge/erratum-absorption-round62.md`). The tip file says the seat wrote the knowledge entry and drops that draft. The rewrite is in `e6da78b`, the same commit as the four completion reports.

So the wave-1 report survives as the blob at `3e7aed9b`. It was not left intact at the path.

## Verdict

| check | result |
|---|---|
| 39 unique spec names; dispatch set equal | pass |
| receipt / tool at `3e7aed9b` and at `f9ab081`: 34 of 39, those five missing, unmatched 0, exit 1 | pass |
| LOG/SCORECARD five-dead and "34 reports" at the tip that contains them | **fail** (tool: 35 of 39, missing 4, unmatched 3, exit 1) |
| "named, not replaced" for `ExecSuccessor31` | **fail** (added in `e6da78b`) |
| completion call "5 seats (executor 2, scribe 2, scout 1)" | **fail** (4 added w1 files: executor 2, scribe 1, scout 1; no fifth report in that commit) |
| `ScoutRegistry`, `ExecNoHarmRun`, `ScribeLessonQ57` not spec seats | pass (they are unmatched, not in K) |
| `ExecSuccessor31` not counted as a wave-1 spec seat | **fail** (it is in K at the tip) |
| `ScribeEntry62` object at `3e7aed9b` still reachable | pass |
| that report's bytes still at the path | **fail** (rewritten in `e6da78b`) |

Confidence: high. All figures are from `check_seat_counts.py` and `git` on committed bytes.

Unknown: no completion-call spec or dispatch file is in the tip tree, so the asserted fifth completion seat cannot be named from a committed roster. Only the four basenames above were added under `w1/`.

Installs: none. Blockers: none.
