# CriticBoxReword — kotoba round 49 falsify: the `dispatch.08` box re-wording

**Verdict: HOLDS-BOUNDED** — applies to the `dispatch.08` re-wording in `SKILL.md` (a5adc146 → c48793d)
and to C2's `dispatch.08` half. The premise is true. Choosing N/A over FAIL is right. The re-word
fixes a false factual clause; it does not hide a prompt defect. It is bounded on four counts:
(a) the plan never declared it; (b) the live result under the declared box is missing from LOG and
SCORECARD; (c) under the new authority the conjunct cannot fail on any driver-rendered prompt, so
every live case that could fail is routed to N/A; (d) the authority is uncommitted, moving state.

Attacked: the box text diff (`SKILL.md` lines 329-334), `state_source` and `evaluate_dispatch_08` in
`verifiers/verify_dispatch_prompts.py`, the `.ufo/state/` premise, and the C2 records (LOG line 2372,
SCORECARD row 31 and capability row 255, lesson lines 79-83, `plans/round-49.md` line 75).

## Findings

F1. The premise holds (calibration). The only writer of `<id>.round` is `launch_lane`
(`scripts/shokunin-watchdog.sh:220`). The watchdog log has 0 `launch_lane`-format lines (no
`driver=` tag) after 2026-10-15T01:51-03:00. The removed slot driver (`cadb3e3`) and `inline.sh:100`
call `record_report_baseline` but never write `.round`. All 21 `.round` files have an mtime between
2026-10-15 01:45:42 and 01:50:57 -0300. `kotoba.round` (value 16) was last committed in `17c1fad`
on 2026-09-29. The first field of `report-baseline` equals the hyaku claim round on 13 of 13
claimed pool lanes. On the 2 unclaimed pool lanes it is the next round minus 1 (kama 25/26,
chousa 28/29). That makes 15 of 15 pool lanes. `inline.sh:97-100` renders the prompt and then calls
`record_report_baseline "$lane" "$n"` with the same `$n`.

F2. N/A is correct and FAIL would be wrong (calibration). I wrote `.round` into a baseline for the 6
legacy lanes, in scratch only. The result was `FAIL dispatch.08 … 272 PASS, 7 FAIL, 0 N/A`, exit 1.
The 7 failing files are aggregator-round-11 and -12, audio-round-101, game-dev-2d-round-105,
game-dev-3d-round-108, lore-round-103 and protocol-round-15. Each of those rounds has a committed
report, for example `.ufo/reports/round-101/audio.md` at `930677e` and `round-108/game-dev-3d.md`
at `98c854e`. So all 7 rounds were dispatched, and all 7 FAILs would be false reds. The `.round`
values match each lane's last `launch_lane` log line (audio, lore and game-dev at 1, aggregator 10,
protocol 14). These lanes were later dispatched by routes that never write `.round`: the kaika W2
prompts (`5b471e4`, 2026-10-19) and the 2026-09-29 commits.

F3. The plan did not declare the re-word, and the declared commitment was dropped (operability,
calibration). `plans/round-49.md:75` says "The full `dispatch.08` box is executed, state clause
included; its live failures are findings." The plan was committed in `f054b8e` at 2026-10-22T11:03Z.
That is after PlanDataWalk's 09:45Z walk had already recommended the new authority. PlanDataWalk
lines 114-116 give the motive: "a red count the round cannot defend". The plan has dated re-sizing
notes for C1 and C2, but none for this re-word. The declared box failed 166 of 289 prompts (blind
instrument) and 21 of 21 target lanes (PlanDataWalk). That result appears only in the lesson
(lines 80-81). LOG line 2372 and both SCORECARD rows report only `PASS 250, N/A 29`.
Verify: `rg -n "166" LOG.md SCORECARD.md` returns no match on this round.

F4. The new conjunct cannot fail on live, driver-rendered prompts (operability). The prompt and the
baseline are written by one `dispatch` call with the same round number (`inline.sh:98-100`).
PlanDataWalk records "hi > baseline: no" on 17 of 17 lanes, which holds by construction. The only
live files where the comparison could fail are the 7 out-of-band prompts (F2), and all 7 sit on
state-stale lanes, which are not compared. So the live discriminating count is 0. The fixtures
(`d08-above-state`) prove the code can fail. They do not show that the fleet can produce a failure.
The capability row 255 does not state this limit.

F5. The authority is uncommitted, moving state (calibration; Q10). Fleet `git status` shows
`report-baseline` modified or added for at least 10 lanes. `kotoba.report-baseline` has 0 commits.
- On committed bytes at fleet HEAD `ff3aff278b896d6b65aaa02b9fa7cc9f235e266f` (prompts plus state
  extracted with `git archive`), the result is `FAIL dispatch.08 … 202 PASS, 23 FAIL, 54 N/A`,
  exit 1. All 23 FAILs are on `round_le_latest_dispatched`. The cause: `inline.sh` commits only the
  prompt, never the baseline.
- `c2-live-run-1115Z.json` has the keys checks, exit_code, fail, na and pass. It has no sha256 of
  the state directory.
- So the 11:15Z PASS cannot be reproduced from any commit, and the box text does not say that it
  reads working-tree state.

F6. The "(hyaku driver)" attribution has no located quote (Q23).
- `record_report_baseline` is defined in `scripts/shokunin-watchdog.sh:120` and called at `:203`
  (launch), at `:364` (source-gate retry of the same round) and at `inline.sh:100`.
- The authority's own documentation (`:31`) says the file "holds "round SHA256" for the report bytes
  captured immediately before launch or after a blocked source-gate check". It does not say "latest
  dispatched round".
- `:27` still says "`.ufo/state/<lane>.round` holds the current round number". This contradicts the
  new box, and the contradiction is not routed as a fleet-root defect (Q17). PlanDataWalk line 146
  only cites `:27-31` as evidence.

F7. The `state-stale` report is invisible (operability). The box says these lanes are "reported
`state-stale`", and `none` and `stale` lanes both map to N/A. The text output prints only
`29 N/A`; `state-stale` appears only in the per-file JSON details. JSON breakdown: aggregator 9,
protocol 12, and 2 each for audio, game-dev-2d, game-dev-3d and lore, all state-stale.
The "neither file" branch fires for 0 live lanes: kotodama and souji have a baseline.
Side note (outside scope): at base, the `dispatch.08` disposition was a copy of dispatch.03's
"| godspeed" reason.

## Impacted axes
operability (F3, F4, F7), calibration (F1 holds; F3, F5, F6 bound it). Fixable defects; no
tradeoff that the judge must reject.

## Smallest safe correction
1. Append a dated re-sizing note to the plan, or an append-only line to the LOG C2 entry. It should
   record the declared-box result (166 of 289, 21 of 21 lanes) and the re-word as a target change.
2. Add a limit to the capability row: live discrimination is 0 by construction, and the 7 decidable
   out-of-band files are N/A. A reports-based fallback (a committed `.ufo/reports/round-N/<lane>.md`
   counts as dispatched) would make the 29 N/A files decidable. By F2, all 7 high rounds would pass.
3. Print a `state-stale` count in the text output. Record a sha256 manifest of the state directory
   with every live run, and say "working tree" in the box.
4. Route `watchdog.sh:27` as a fleet-root defect report, and cite `:120`/`:31` in the box.

## Evidence (UTC 2026-10-22; scratch `/fast/scratch/hyaku/kotoba-r49/falsify/CriticBoxReword/`)
- `git diff a5adc146… c48793d… -- SKILL.md`: exit 0 (re-word at 329-334).
- `rg -n '\.round"|\.round\b' scripts/` returns one writer, `shokunin-watchdog.sh:220`.
  `git show cadb3e3 | rg '^-.*(\.round|record_report_baseline)'` shows the baseline call only.
- Watchdog log: 0 non-driver launches after 2026-10-15T01:51
  (`rg ' launch ' .ufo/watchdog.log | rg -v driver= | awk '$1>"2026-10-15T01:51"' | wc -l`).
- `ls -la --time-style=full-iso .ufo/state/`: 21 `.round` files with mtimes from
  2026-10-15 01:45:42 to 01:50:57 -0300. The lane-by-lane table of round, baseline, next and claim
  comes from the shell loop over `$HOME/.local/state/shokunin-hyaku/{next,claims}`.
- `verify_dispatch_prompts.py --check dispatch.08` on a live snapshot (11:29:39Z):
  `PASS … 250 PASS, 0 FAIL, 29 N/A`, exit 0.
- The same check with `.round` used as the baseline for the 6 legacy lanes: `272 PASS, 7 FAIL`,
  exit 1.
- The same check on fleet HEAD `ff3aff2` committed prompts and state: `202 PASS, 23 FAIL, 54 N/A`,
  exit 1.
- `--box-proof --map verifiers/checklist-baseline.json`: `boxes proven 2`, exit 0. `--self-test`:
  `0 failure(s) over 32 assertions`, exit 0.
- `git log -1 -- .ufo/reports/round-{101/audio,103/lore,105/game-dev-2d,108/game-dev-3d,11/aggregator,12/aggregator,15/protocol}.md`:
  every report is present and committed (930677e, 6556f12, efd37ce, 98c854e, e5efe29, d941b7c, bdff08b).
- `git log -- plans/round-49.md`: f054b8e 2026-10-22T08:03:29-03:00 (the only commit).
- No tools were installed or upgraded. No web sources were opened. Nothing in the lane was written
  except this report.
