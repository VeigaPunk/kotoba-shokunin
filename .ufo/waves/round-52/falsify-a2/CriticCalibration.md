Result: MIXED — 10 of 53 current-state statements do not match the repo or host at c8407a45; 6 are lane-text defects (one HIGH false-provenance line in the uncommitted SCORECARD diff) and 4 come from an opencode upgrade on the host at 2026-10-22T17:50:28Z.

# CriticCalibration — round 52 attempt 2, falsify wave

Seat: `KotobaR52a2.CriticCalibration` (critic; axis judged: calibration).
Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882` (lane `master`, committed 2026-10-22T17:10:42Z).
Second target: the uncommitted working-tree diff of `SCORECARD.md` against `master` (lane file mtime 2026-10-22T17:14:08Z, written after the head commit).
Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/CriticCalibration` (clone checked out at the judged revision). For gates that resolve `../.ufo` and sibling-lane pointers I used the fleet-shaped mirrors `fleet-base/` and `fleet-head/` (symlinks to the fleet-root entries, plus clones at `c8579a4c` and `c8407a45`). Detached worktrees `wt-43ca0bfb/` and `wt-e0320302/` hold the round-51 replays. Two gates (`verify_corpus_integrity.py`, `verify_skill_checklist.py`) were also run read-only in the lane; `git status --short` was identical before and after.
Tooling: no install or update.
Measured 2026-10-22T17:50Z–17:58Z.

## Scope and counting rule

Counted: every statement in `SCORECARD.md` or `SHONEN.md` that is written as current state or as a measured value and that this round touched or that names a round-51 or round-52 value. That covers the axes-row segments for round 51 and round 52, the `Round 51 completed`, `Next: round 52`, `Round 52 completed` and `Next: round 53` blocks, the round-51 and round-52 move-log rows, the round-51 calibration note, the capabilities rows that note corrects, and SHONEN box 1 (the box the note names). Each one was compared with what its command prints now. Two sets are kept apart: the committed file at `c8407a45` (29 statements) and the uncommitted working-tree diff (24 statements).
Not counted: SHONEN boxes 2–4. Round 52 did not touch them and they name no round-51 or round-52 value.

| Set | Checked | Mismatch | Caused by host drift | Lane-text mismatch |
|---|---:|---:|---:|---:|
| SCORECARD.md + SHONEN.md committed at `c8407a45` | 29 | 5 | 2 | 3 |
| SCORECARD.md uncommitted working-tree diff | 24 | 5 | 2 | 3 |
| **Total** | **53** | **10** | **4** | **6** |

## Mismatches

### W20 — HIGH — false provenance: "the falsify wave ran on live roles only" (working-tree diff, `SCORECARD.md:128`)
- Statement: `Round 52 completed` block: "The build wave never ran (…); the L1 did the build work; the falsify wave ran on live roles only."
- Observed: `.ufo/waves/round-52/falsify/` holds only `swarm-registry.json`. It lists 36 members, created and last updated at `2026-10-22T17:12:35.908Z`, and no seat report exists. `falsify-gate.txt` is 0 bytes. The SCORECARD line was written at 17:14:08Z, 1.5 minutes after dispatch and before any seat could report. The assignment records that the attempt-1 falsify wave was cut off by the omp restart and left no seat report. The round's own lesson says the opposite of the SCORECARD: `corpus/lessons/round-52.md:12` (M37): "the wave and its falsify seats are reported as not run, not replaced."
- Command: `python3 -c 'import json;d=json.load(open(".ufo/waves/round-52/falsify/swarm-registry.json"));print(d["createdAt"],d["updatedAt"],len(d["members"]))'` → `2026-10-22T17:12:35.908Z 2026-10-22T17:12:35.908Z 36`. `ls .ufo/waves/round-52/falsify/` → `swarm-registry.json` only.
- Axes: calibration (the owned consistency sub-axis) and adjacency to the closure, which would read it as falsify evidence.
- Smallest fix: "The attempt-1 falsify wave (36 seats registered 17:12:35Z) was cut off by an omp restart and left no seat report; attempt 2 re-runs it."

### W21 — MED — premature completion: heading "Round 52 completed (hyaku campaign, attempt 1)" (working-tree diff, `SCORECARD.md:128`)
- Observed: the round is open. Attempt 2's falsify wave (this wave, `.ufo/waves/round-52/falsify-a2/`, dispatched 17:49Z) is running, the carried build items (fixture labels, the S024 superseding row) are this attempt's milestone, and the lesson's `### Spot-check` says "Owed to the non-author closure". Every earlier `Round N completed` block in the file was written after that round's falsify wave.
- Smallest fix: write the heading as "Round 52 landed (attempt 1; falsify and closure pending)", or hold the block until attempt 2 closes.

### W7 — MED — the counter does not check `location` (working-tree diff, `SCORECARD.md:30`)
- Statement: coverage row, round-52 segment: "The counter checks location, length, the word `instructions`, host and Gate record".
- Observed: `verifiers/check_mcp_instructions.py` only uses `location` as a header name (`:22`, `:90`). It never reads the location cell. A sandbox mutant that set the location cell of all 5 counted rows to `nowhere` still prints:
  `python3 -B verifiers/check_mcp_instructions.py --root .` → exit 0, `mcp instructions backed 5 of 7 clients` (`notes/mut-location.txt`; file restored with `git checkout` in the sandbox).
- The same overclaim appears in `corpus/knowledge/mcp-server-instructions-round52.md:60-62` § Limits ("checks that each row's quote is located") and matches the plan's statement wording ("a located quote", `plans/round-52.md:42`). The counter is frozen, so the text has to change, not the code.
- Smallest fix: "The counter checks the source row (tier A, `mined`, opened 2026-10-22, `used-by`), host, quote length, the word `instructions` and the Gate record; the location cell is not checked." Apply the same wording to entry § Limits.

### C18 — LOW — round-51 calibration note: "moves `surfaces` 99 → 115" (committed, `SCORECARD.md:278`)
- Observed: the surfaces floor was 115 at `59903b26`, 119 at the round-51 head `c8579a4c` and 129 at `c8407a45`. Command: `git show <rev>:verifiers/floors-registry.json` → `surfaces.floor`. Self-test: `0 failure(s) over 119 assertions` at `c8579a4c`, `129` at `c8407a45`. The note was committed in `533ff20`, one commit before `c363de7` added the parameter-shadow arm (115 → 119). The note claims "current values at round 51" but was stale by the round-51 head. Its "passes 12 rows" still holds (12 PASS at head).
- Smallest fix: an append-only line: surfaces 119 at the round-51 head, 129 at round 52.

### C21 — LOW/MED — round-51 calibration note: "`verify_corpus_integrity.py` is 8 of 9 at round 51 (the carried `report_dead 2`)" (committed, `SCORECARD.md:278`)
- Observed (fleet-shaped mirror, and the lane read-only at head):
  - `c8579a4c`: exit 1, `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.report_dead` (tracked 73 vs 72, unindexed `corpus/lessons/round-51-verifier-spotcheck.md`, report_dead 3).
  - `c8407a45`: exit 1, `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_total` (tracked 75 vs 72, report_total 47 vs 46, report_dead 3, commit_total 31 vs 30).
  - The third dead pointer is `corpus/lessons/round-51-verifier-spotcheck.md:25: .ufo/reports/round-51/kotoba.md`.
- No-harm note (not counted): round 52 cleared `unindexed` and added a `commit_total` drift without re-recording the corpus baseline. The score stays 5 of 9 at both ends, but the failing set changed.
- Smallest fix: an append-only line with the current 5 of 9 and its four drifts, or a baseline re-record (the L1 decides).

### C29 — LOW (carried) — SHONEN box 1: "38 Sources entries" (committed, `SHONEN.md:6`)
- Observed: `git show <rev>:SKILL.md | awk '/^## Sources/{f=1;next} /^## /{f=0} f && /^- /' | wc -l` → 39 at both `c8579a4c` and `c8407a45`. Round 51 reported this mismatch and left SHONEN unchanged, and round 52 also left it unchanged.
- Smallest fix: 38 → 39, citing the awk command.

### Host drift: opencode upgraded during this wave (W12, W14, C20, C23)
- Observed: `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` now reports version 1.19.4 (`package.json` `"version": "1.19.4"`), sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, mtime 2026-10-22T17:50:30Z (`package.json` 17:50:28Z). That is after both the head commit and the working-tree SCORECARD write. The pin is `179ca421…` (`verifiers/baseline.json:10`).
  - `python3 -B verifiers/check_substrate_pins.py` → exit 1, `DRIFT 1/3 pins failed: opencode_binary_sha256`. The omp sha256 and mtime pins both PASS.
  - `python3 -B verifiers/verify_surfaces.py --json` → exit 1, pass 6 fail 1. `surfaces.opencode_extract` FAIL: "declared opencode class(es) produced by no rule: opencode:instruction-context/AGENTS.md, opencode:read-hook/instructions …". `surfaces.literal_present` and `surfaces.no_uncovered_class` (the omp checks) PASS.
- Statements this falsifies now:
  - W12: freshness round-52 "live gate `pass 7`, exit 0".
  - W14: freshness round-52 "pins `OK 3/3`".
  - C20: the round-51 note's "(pins `OK 3/3`, surfaces 7 of 7)".
  - C23: the substrate-pin capability row's "`exit 0`, `OK 3/3 pins hold`".
- Each was true when written, as far as the record shows [INFERENCE: I did not observe the pre-17:50Z state]. None is caused by round 52, and the omp half of every claim still holds. Fixing them belongs to opencode re-pin freshness debt, not to a rewrite of these statements.
- Smallest fix: one append-only observed-state line naming opencode 1.19.4, its sha256 and its install time. Do not edit the round-52 measurements.

## Statements that hold (43)

Committed at `c8407a45`:
- **C1–C8, depth row round-51 segment.** Commands: the plan-commit counter `git show 7c81a787:verifiers/check_overlap_levers.py` and the current counter, run from the sandbox.
  - plan counter `--rev 43ca0bfb` → exit 1, `0 of 7`
  - plan counter `--rev 34cfffbb` → exit 1, `4 of 7`
  - plan counter `--rev c8579a4c` and `--rev c8407a45` → exit 1, `4 of 7`, with exactly the three failures named: `effect not allowed ('removed in a scope') (GitHub Copilot SDK)`, the same for Gemini CLI, and `entry quote malformed (opencode)`
  - `34cfffbb`'s own counter `--rev 34cfffbb` → exit 0, `7 of 7`
  - current counter `--rev c8579a4c` and `--rev c8407a45` → exit 0, `7 of 7`
  - `--self-test` → `51 assertions` (floor 51)
  - `--fetch` (17:56:06Z–17:56:16Z) → exit 0, `quotes found on live pages 7 of 7`
  - "four counted rows are new" matches `corpus/lessons/round-51.md:163`; the "Lead rewritten round 52" text is in the `c8579a4c..c8407a45` diff.
- **C9, C12, C14, round-51 freshness record.** Replayed in worktrees:
  - `43ca0bfb`: `surfaces.literal_present` and `surfaces.no_uncovered_class` FAIL.
  - `e0320302`: both PASS.
  - So the omp checks go 0 of 2 → 2 of 2. The full 5 → 7 of 7 cannot be replayed on today's host because the opencode check fails at both revisions.
- **C10.** `verify_harness_claims.py` → exit 1, `21/28`.
- **C11.** `e0320302` self-test `0 failure(s) over 115 assertions`, floor 115.
- **C13, `Next: round 52`.** Each candidate was worked or carried into `Next: round 53`.
- **C15, round-51 depth move-log row.** Holds as C1–C8.
- **C16.** `check_substrate_pins.py --self-test` → `0 failure(s) over 62 assertions`.
- **C17.** `check_assertion_floors.py` → exit 0, 12 PASS.
- **C19.** `verify_skill_checklist.py` (lane, read-only) → exit 0, `checklist.box_map_complete … delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2`.
- **C22.** The note's "counts 39" is still 39.
- **C24.** `verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → exit 0, `boxes proven 2`.
- **C25.** `check_sibling_census.py … --skill SKILL.md` → exit 0, `9 of 9`, length 1019 of 1024; floor 68 PASS.
- **C26–C28, SHONEN counts.** 7 anatomy rows (`SKILL.md:66-72`), 5 rows in § Decision tables (`:182-186`), 41 boxes split 15/9/9/8. Round 52 added a second, 4-row decision table in § Instruction surfaces (`:89-94`). The round-46 method does not count it; recorded here but not counted as a mismatch.

Working-tree diff:
- **W1–W4.** `check_mcp_instructions.py` → exit 1, `0 of 7` at `c8579a4c` and at `4c003a4b`; exit 0, `5 of 7` at `c8407a45`; `--fetch` (17:51:46Z–17:51:49Z) → exit 0, `found on the live page 5 of 5`. The script is byte-identical at `4c003a4b` and `c8407a45` (`git diff --quiet`).
- **W5.** S032–S036 are tier A and S037 is tier B (`corpus/SOURCES.md:45-50`).
- **W6.** opencode and Copilot CLI are recorded as silent (entry `:29`, lesson § Rejected). I did not re-fetch those pages.
- **W8–W11.** `check_callee_rename.py` with seeds 52, 7 and 1234 → exit 1, `0 of 4` at `c8579a4c` and `4c003a4b`; exit 0, `4 of 4` at `c2107ecf` and `c8407a45`. The script is identical at `4c003a4b` and the head, `FIXTURE_REV = "c8579a4c…"` (`:61`), and the default seed is 52 (`:146`).
- **W13.** `verify_surfaces.py --self-test` → 119 at `c8579a4c`, 129 at head; floor 129.
- **W15.** 12 PASS.
- **W16.** The two counters hold as above.
- **W17.** `check_correction_sweep.py`:
  - `--rev c8579a4c` → exit 1, `FAIL r51-c2-readme corpus/README.md:119`, `FAIL r51-c2-scorecard-lead SCORECARD.md:28`, `FAIL r51-c2-province PROVINCE.md:17`, `3 stale block(s)`
  - `--rev c8407a45` → exit 0, `0 stale block(s)`
  - `--self-test` → `0 failure(s) over 5 assertions`
  - Q29 is at `corpus/QUALITY.md:40`.
- **W18.** S038 says it supersedes S031 (`corpus/SOURCES.md:51`).
- **W19.** The build registry has 34 members, all created at 16:00:24Z, with no report (lesson M37).
- **W22.** `Next: round 53` candidates are carried with M37 as the reason (`corpus/lessons/round-52.md:75-77`).
- **W23–W24.** The round-52 move-log rows hold as W1–W11.

## Not counted (structural)

- **MED.** At the judged revision the committed `SCORECARD.md` has no round-52 C1 or C2 record. The only round-52 edit is the depth-lead repair. The coverage and freshness segments, `Round 52 completed`, `Next: round 53` and both round-52 move-log rows exist only in the uncommitted working-tree diff. Round 51's calibration seat reported the same gap.
- **LOW.** `corpus/lessons/round-52.md:4` cites "LOG.md § Round 52", but `LOG.md` at `c8407a45` has no round-52 heading (the last is `Round 51 landing pin and falsify wave`, `:2423`). This is outside the two files assigned.

## For the L1

Before committing the working-tree `SCORECARD.md`:
1. Rewrite the falsify sentence (W20).
2. Retitle or hold the completion block (W21).
3. Drop "location" from the counter description in the coverage row and in entry § Limits (W7).
4. Append the current values for C18, C21 and C29, and one host-drift line for opencode 1.19.4 (W12, W14, C20, C23).

Checks to re-run after the fix:
- `python3 -B verifiers/check_correction_sweep.py --rev <new>` (exit 0)
- `python3 -B verifiers/verify_skill_checklist.py` in the lane (its `governance.citation_resolves` check reads `SCORECARD.md`)
- `python3 -B verifiers/check_substrate_pins.py` (expect `DRIFT 1/3` until opencode is re-pinned)
