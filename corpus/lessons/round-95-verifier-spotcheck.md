author: hyaku closure (non-author integrator, @m_zfl)

# Round 95 verifier spot-check (non-author closure of kotoba round 95)

Lane round 95. Base `2d886a91e57efd3555ec9076a63209e2d8bfbb8d`, tip `7578906425d06e3124d8ea1c652883d4f4e89bef`
(freeze `673d1e2e`, landing `d1144fab`, record `f6a9f76a`, wave evidence `75789064`). Report
`.ufo/reports/round-95/kotoba.md` (fleet repo). Closure measured 2026-11-06T02:52Z.

Driver digest (copied from the mutable `.ufo/watchdog.log`):
`2026-11-05T21:59:23-03:00 launch kotoba round=95 pgid=2224233 driver=hyaku-inline attempt=1` ·
`2026-11-05T23:31:19-03:00 lane-dead-no-report kotoba round=95; retry same round (hyaku-inline attempt=1: L1 ended without a landed report: FAIL report_of (missing, unchanged, no SHONEN heading, or < 400B): .ufo/reports/round-95/kotoba.md)` ·
`2026-11-05T23:31:21-03:00 launch kotoba round=95 pgid=2174434 driver=hyaku-inline attempt=2` ·
`2026-11-05T23:50:40-03:00 complete kotoba round=95; hyaku-inline attempt=2`.

## Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git log --format='%an %ae %H %cI' -- .ufo/reports/round-95/kotoba.md` | `kotoba-shokunin kotoba@shokunin.local 494cb53d… 2026-11-05T23:50:05-03:00` (after the last lane commit 23:48:53, before the 23:50:40 complete line) | pass |
| SHONEN heading, one line per box | read report § SHONEN | 4 lines, all `[~]`, each with an evidence pointer | pass |
| cited commits exist and are ancestors of `master` | `git cat-file -t <h>; git merge-base --is-ancestor <h> master` for 2d886a91, 673d1e2e, d1144fab, f6a9f76a, 75789064 | all `commit`, all ancestors | pass |
| lane pushed, nothing left | `jj-lane.sh state …`; `git status --porcelain`; `git ls-remote origin refs/heads/master` | `ahead=0 behind=0 head=detached tracked=0 untracked=0`; empty; remote = `7578906425d0…` | pass |
| round commits by lane identity | `git log --format='%h %an %cI' 2d886a91..master` | 4 commits, all `kotoba-shokunin` | pass |
| prompt carries the template contract | `grep -n '^#' templates/round-prompt.md` vs `.ufo/prompts/kotoba-round-95.md`; every placeholder-free template line of §1–§5 present in the prompt (`diff` shows no template-only line) | §1 MISSION/AXES, §2 claims, §2b frontier, §3 L2 floor, §4 report contract, §5 commit, §6 hyaku addendum, §7 scratch; prompt commits `ba8c21b1` 21:59:20 (attempt 1) and `5c1b1798` 23:31:19 (attempt 2), each before its launch line | pass |
| wave dispatched | `git show 75789064:.ufo/waves/round-95/r95-w1-dispatch.json \| jq -c .counts` | `{"spawn":12,"resume":0,"total":12}` | pass |
| frozen bytes unchanged after freeze | `git diff --stat 673d1e2e 75789064 -- verifiers/fixtures/round-95 plans/round-95.md`; `sha256sum` of `selftest-kills.py` at both revs | empty diff; `d6ae74af…1d269001` at both | pass |
| scratch removed | `ls /fast/scratch/hyaku \| grep kotoba-r95` (excluding this closure's own dir, removed after use) | none | pass |
| marker? | — | real report, 4 resolvable lane commits | not a marker → status `ok` |

Defects (status-neutral):
- Attribution: both dispatch prompt commits (`ba8c21b1`, `5c1b1798`) are authored `kotoba-shokunin`, not the orchestrator/protocol identity (same pattern as rounds 93–94).
- Attempt 1 ended without a landed report (`lane-dead-no-report`, 23:31:19); attempt 2 reused the three committed attempt-1 commits after re-verifying them against receipts, and committed the uncommitted wave dir in `75789064`. Not a status defect: the report landed before the complete line.
- `r95-w1-results.json` carries `output=null` for all 12 seats (orchestrator kernel restart); seat results were read from committed `w1/*.md` files. MutTesterCounter95 has no verdicts (incomplete seat), disclosed, its salvaged raw matrix committed uncounted (62 files).
- Tip battery red-carry: `verify_skill_checklist.py`, `verify_corpus_integrity.py`, `verify_corpus_independent.py` exit 1 at the round-94 tip and at `d1144fab` alike (Gate standard, Closure consequence: conformance defect routed to the owner, status-neutral).

## Claim re-checks

**C1 — depth (battery self-test kills the round-94 survivors N1, N5, N11).**

Re-measured (plain, over committed bytes):
- `git diff 2d886a91 75789064 -- verifiers/check_mutation_battery.py | grep '^@@'` → one hunk `@@ -838,6 +838,73 @@ def self_test() -> int:` (+67 lines, all inside `self_test()`); `git diff d1144fab 75789064 -- verifiers/check_mutation_battery.py` → empty (landing code unchanged through the tip).
- assertion-call count inside `self_test()` (`awk` from `def self_test` to the next top-level `def`, `grep -cE '\bcheck\(|_check\(|expect\(|assert'`): **44 → 52** (+8). Read of the hunk: 4 `t.check` for N1 (both directions of `--rev` vs HEAD manifest), 1 for N5 (target-set refusal must not carry the `kill-set-size` label), 2 live + 1 rev-path for N11 (two and three rows above the pin refused, naming the observed count) = 8, matching the reported 38 → 46 assertions.
- every new arm is behavioural: N1/N5/N11 rev-path arms call `run_evaluate` on committed fixture repos, the N11 live arms call `kill_set_check`; no arm reads the instrument's source text.

Evidence-verified (lane-owned counter `verifiers/fixtures/round-95/selftest-kills.py`, not executed by the closure):
- before `receipts/redbefore-c1-base.txt`: `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-UNMET`, rc=1, decoy runs `0 failure(s) over 38 assertions`.
- after `receipts/landing/c1-counter.txt`: `C1 targets killed 3 of 3 (run errors 0); …` → `C1-PREDICATE-MET`, rc=0, `over 46 assertions`; `landing/bat-selftest.txt`: `0 failure(s) over 46 assertions`, rc=0; revision measured `landing/landing-rev.txt` = `d1144fab…`.
- positive control `r94c1` MET at base and landing; forgery `forgery-f6-crash-report.txt`: `C1 targets killed 0 of 3 (run errors 1)` → UNMET (the rule-1 fix shown able to fail; run-granular only, disclosed A2).
- independent hand-applied kills: `w1/ReviewerBatteryKills.md` §Kills names the failing arm per mutant (n1 2 failures, n5 1, n11 2; REPORTED-FAILURE, not run errors).
- open bound (not a C1 failure): salvaged MutTesterCounter95 raw matrix shows counter mutants M5/M6 reading false MET on demo worlds — a gap in the counter's committed control battery, routed.

Verdict: **C1 verifies** (re-measured structure + evidence-verified counter readings agree with the report).

No-harm (evidence-verified, `receipts/landing/`): round-93 `c1-killpin`/`c2-pinkey` MET/MET; round-94 counter c1/c2 MET/MET; round-92 `controls-run` `shortcuts refused 2 of 2; honest held 2 of 2`; gate registry `74 of 74 … phantom 0`; floors self-test `0 failure(s) over 176 assertions`; tip battery `guards 5 of 5; … 3 of 6` vs round-94 `2 of 6` (floors gate now exit 0 in 236.2 s instead of the 280 s timeout; the other three reds identical to the round-94 receipt). `git diff --stat 2d886a91 75789064 -- SKILL.md PROVINCE.md SHONEN.md` → empty. `git diff 2d886a91 75789064 -- SCORECARD.md` → append-only (round-95 annotations + round-96 intentions); no axis score changed, no capability row added.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | C1 verified (0 of 3 → 3 of 3 under the stricter v3 counter; 38 → 46 assertions) |
| consistency | unchanged | no claim; gate registry 74/74 held |
| coverage | unchanged | no claim; PROVINCE.md unchanged |
| operability | unchanged | no claim; tip battery reds identical to base, floors no longer times out (not claimed) |
| freshness | unchanged | no claim |
| calibration | unchanged | no claim; report discloses A1/A2/A3 bounds and the incomplete seat |
| adjacency | unchanged | no claim; no sibling file touched |

## Discernment spot-check (lesson `round-95.md` § Gate)

Re-opened 2026-11-06 by the closure (scratch, removed after use).

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S270 Python `unittest` docs | admit (tier A, docs, mined) | `curl -sS -L https://docs.python.org/3/library/unittest.html` → `200 336978`; sha256 `f9510cd7d7a67a32fb891016cbb42bf1dfcb80a370c689ed222058acbff3506d` (equals the lesson's digest) | agree | quote "Each tuple represents a test which raised an unexpected exception." found at lines 2413–2414 (fold after "an"), 10 words ≤25; the `failures` counterpart at 2421–2422; primary docs, and it grounds exactly rule 1's error-vs-failure split |
| Apache Ant `junit` task manual | reject | `curl -sS -L https://ant.apache.org/manual/Tasks/junit.html` → `200 33365`; sha256 `3f1ee369…c4a1` (equals the lesson's); `grep -ic 'unexpected exception'` → 0; line 104 "Stop the build process if a test fails (errors are considered failures as well)." | agree (reason partly overstated) | the page gives no definition of what an error is, so it cannot ground rule 1; but "conflates" is too strong: it keeps separate `haltonerror` (line 94 "Stop the build process if an error occurs during the test run.") and `errorproperty` (line 98) — the merge is scoped to `haltonfailure`. Decision stands; the reason should say "scoped merge under haltonfailure, no definition" |
| S260 re-open (no new row) | corroboration, no row | not re-fetched by the closure; lesson records a byte-identical scout re-fetch | not sampled | — |

SOURCES row re-open: `corpus/SOURCES.md` S270 row (the only new row; `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 195 at `2d886a91`, 196 at `75789064`) quotes the same 10-word sentence at HTML lines 2413–2414 — verified above.

Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → rc 0, 34 `W04`, 0 `E`-codes, last line `kotoba	ok	…/kotoba-shokunin/corpus/SOURCES.md` (same 34 W04 as `receipts/census-before.txt`; none new).

## Trend verdicts

- **expansion: unchanged** — no `knowledge/` entry admitted; S270 is a registry row cited by plan and lesson.
- **quality: improved** — the battery self-test kills three mutants it missed at base (`redbefore-c1-base.txt` 0 of 3 → `landing/c1-counter.txt` 3 of 3) under a counter that no longer scores a crash as a kill (`forgery-f6-crash-report.txt`); no admitted entry failed a re-check.
- **discernment: improved** — the outside spot-check agrees with the gate on the admit (S270) and the reject (Ant); Q84 (round-94 closure defect 1, applied: S260 re-opened, no duplicate row) and Q85 (mined mistake `run-error-scored-as-kill`, shown able to fail on f6) are each grounded in a lesson.

## Routed defects (lane fixes next round)

1. Ant reject reason: amend in the round-96 lesson (append, not rewrite) that the Ant page keeps `haltonerror`/`errorproperty` separate and merges errors into failures only under `haltonfailure`; the reject stands on "no definition of an error".
2. Counter control battery gaps: MutTesterCounter95 salvaged matrix M5 (f5) and M6 (f9) false MET; M2/M7/M8 unexposed — add committed controls and re-run the seat to verdicts.
3. m08 survivor (target-set `!=` → `<`; no extra-target world); N4 unobservable.
4. Recompile-compare / bytecode forgery worlds (g2, g3, f8) as committed controls; counter exit ladder (ReviewerCounterV3 F1/F3); predicate-flipping crash world (A2).
5. Tip battery flat 280 s outer cap on the floors gate (`check_tip_battery.py` `GATE_TIMEOUT_S`); three long-standing red gates (`verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`).
6. Attribution: dispatch prompt commits authored by the lane identity (orchestrator-side; noted for the operator).
