Result: MIXED — causal separability HOLDS (each counter reads none of the other claim's files; C1 verifies at c2107ec before C2; C2 verifies on a C2-without-C1 tree) and the committed work harms no gate's exit status, but the uncommitted SCORECARD.md BREAKS calibration with an unsupported provenance sentence and a premature "completed" headline, and two low consistency defects landed (a dangling LOG.md pointer, a corpus-integrity check flipped from PASS to FAIL).

Seat: KotobaR52a2.CriticSeparability (critic). Judged revision c8407a453788df964df5a7b835dd0ce1360de882; lane working tree = that commit + the uncommitted SCORECARD.md diff. Sandbox: /fast/scratch/hyaku/kotoba-r52a2/CriticSeparability (clone at c8407a4; sandbox-only worktrees under `_scratch/` at c8579a4 = base, c2107ec = C1-only, c8407a4 = head, and head + the lane's uncommitted SCORECARD.md = "wt"). Runs 2026-10-22T17:50Z–17:58Z. No installs or updates. Lane: read-only git only; this file is the only lane write.

## A. Separability

### A1 HOLDS — the C1 counter reads no C2 file
Static: `verifiers/check_callee_rename.py:61-63,159-161` reads fixtures with `git show c8579a4c…:verifiers/fixtures/surfaces/<n>` and only `<rev>:verifiers/verify_surfaces.py` from the measured revision. C2 (c2107ec..c8407a4) does not touch that file:
`git diff --stat c2107ec c8407a4 -- verifiers/verify_surfaces.py` → empty.
Dynamic (traced with strace, full strings): `strace -f -qq -s 512 -e trace=execve -o c1.strace python3 -B verifiers/check_callee_rename.py --rev c8407a4` → exit 0. The only `git show` targets are `c8407a4:verifiers/verify_surfaces.py` plus 8 fixture paths at `c8579a4c5b48789e56fb9060ddd48f33569e1215:verifiers/fixtures/surfaces/…`. The gate subprocess runs from a temporary directory with explicit `--repo/--omp-strings/--opencode-strings/--baseline/--inventory` paths inside that directory, so it does not read the lane's SKILL.md, corpus or census.

### A2 HOLDS — the C2 counter reads no C1 file
Static: `verifiers/check_mcp_instructions.py:62-64,183-186` reads only ENTRY, `corpus/SOURCES.md` and `corpus/lessons/round-52.md`. C1 touches none of them:
`git diff --stat 4c003a4 c2107ec -- corpus/knowledge/mcp-server-instructions-round52.md corpus/SOURCES.md corpus/lessons/round-52.md` → empty.
Dynamic: the strace of `--rev c8407a4` (exit 0) shows exactly three `git show` targets: `c8407a4:corpus/knowledge/mcp-server-instructions-round52.md`, `c8407a4:corpus/lessons/round-52.md`, `c8407a4:corpus/SOURCES.md`.

### A3 HOLDS — the two-by-two matrix (each claim moves only its own counter)
Commands: `python3 -B verifiers/check_callee_rename.py --rev <r>` and `python3 -B verifiers/check_mcp_instructions.py --rev <r>`.

| tree | C1 counter | C2 counter |
|---|---|---|
| c8579a4 (base) | `robust 0 of 4`, exit 1 | `backed 0 of 7`, exit 1 |
| 4c003a4 (plan) | `0 of 4`, exit 1 | `0 of 7`, exit 1 |
| c2107ec (C1 only) | `4 of 4`, exit 0 (also `--seed 7`, `--seed 1234`: `4 of 4`, exit 0) | `0 of 7`, exit 1 |
| C2 without C1 (`--root`, built as `git archive 4c003a4` + `patch -p1` of `git diff c2107ec c8407a4`; `diff -rq` against the c8407a4 tree differs in exactly `verifiers/check_assertion_floors.py`, `verifiers/floors-registry.json`, `verifiers/verify_surfaces.py`) | `0 of 4`, exit 1 | `5 of 7`, exit 0 |
| c8407a4 (both) | `4 of 4`, exit 0 | `5 of 7`, exit 0 |

The counters are frozen: `git diff --stat 4c003a4 c8407a4 -- verifiers/check_callee_rename.py verifiers/check_mcp_instructions.py` → empty. Lane and sandbox copies have the same sha256 (`b16d6064…6d03`, `d4b1464f…63c9`), and `git diff --stat -- verifiers/` in the lane working tree → empty.
(My first C2-only tree used `git apply` from a subdirectory of the sandbox repository. That silently skipped every path and printed a false `0 of 7`. I discarded it and rebuilt the tree with `patch`; the table uses only the rebuilt tree.)

### A4 HOLDS — C1 verifies before C2 landed, including its no-harm guards
At a sandbox worktree of c2107ec:
- `python3 -B verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 129 assertions`, exit 0
- `python3 -B verifiers/check_assertion_floors.py` → exit 0, 12 `PASS` lines
- `python3 -B verifiers/verify_surfaces.py --json` → identical JSON to the head run (`diff` exit 0); its exit 1 is the host opencode drift in B1 and shows at base too.

### A5 HOLDS (wording, nit) — C1 touched one more file than the plan's separability paragraph lists
`plans/round-52.md:60` says C1 changes only `verify_surfaces.py` "(and its fixtures, self-test, floor)". C1 also edits `verifiers/check_assertion_floors.py` (floor 119→129 in three places and its self-test anchors). That is floor bookkeeping, and neither counter reads the file, so separability holds. Severity: nit.

### A6 HOLDS — C1 causes no identity change on the live substrate
`diff <(jq -S . base-live.json) <(jq -S . head-live.json)` → exit 0. The live gate output on the installed omp (sha256 `85d9daf3…`) is byte-identical at c8579a4 and c8407a4: `surfaces.literal_present: 42 loader-kind entries verified`, `surfaces.no_uncovered_class: all 8 extracted loader class(es) declared`.

## B. No-harm matrix (one command per harm check; base c8579a4 / head c8407a4 / wt = head + uncommitted SCORECARD.md)

Runner: `_scratch/matrix.sh` in the sandbox (each line is one command run at the tree root). Exit codes:

| axis | check (command) | base | head | wt | round harm? |
|---|---|---|---|---|---|
| operability | `python3 -B verifiers/verify_surfaces.py --json` | 1 (pass 6) | 1 (pass 6) | 1 | none: same failure at base (B1) |
| operability | `python3 -B verifiers/verify_surfaces.py --self-test` | 0 (119) | 0 (129) | 0 (129) | none |
| operability | `python3 -B verifiers/check_assertion_floors.py` | 0 (12 PASS) | 0 (12 PASS) | 0 | none |
| operability | `python3 -B verifiers/check_substrate_pins.py` | 1 (opencode sha) | 1 | 1 | none: host drift (B1) |
| operability | `python3 -B verifiers/verify_skill_checklist.py` | 1 | 1 | 1 | none: same failure set; the differences are line numbers (SKILL.md +10 lines) and the sandbox directory name; `trigger.line_budget` PASS 577→587 of 600 |
| operability | `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 (boxes proven 2) | 0 | 0 | none |
| operability | `python3 -B verifiers/verify_harness_claims.py` | 1 (21/28) | 1 (21/28) | 1 | none: identical DRIFT list |
| operability | `python3 -B verifiers/verify_harness_independent.py` | 0 | 0 | 0 | none |
| operability | `python3 -B verifiers/compare_harness_independent.py --self-test` | 0 (330) | 0 | 0 | none |
| consistency | `python3 -B verifiers/verify_corpus_integrity.py` | 1 (5/9) | 1 (5/9) | 1 | **check-level flip (B3)** |
| consistency | `python3 -B verifiers/verify_corpus_independent.py` | 1 | 1 | 1 | improved: `corpus.index.unindexed` DRIFT gone |
| consistency | `bash verifiers/fault_injection_corpus.sh` | 1 | 1 | 1 | improved: `corpus.index.unindexed` gone from the control row |
| consistency | `bash …/scripts/sources-census.sh validate --root <fake fleet root symlinked to the tree> kotoba` | 0 `kotoba ok` | 0 | 0 | none |
| adjacency | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | 0 | 0 | 0 | none (description 1019 of 1024, unchanged) |
| adjacency/depth | `python3 -B verifiers/check_overlap_levers.py --root .` | 0 (7 of 7) | 0 (7 of 7) | 0 | none |
| calibration | `python3 -B verifiers/check_correction_sweep.py --rev <r>` (head script) | 1 (3 stale: README:119, SCORECARD:28, PROVINCE:17) | 0 | 0 (`--root` lane) | improved (M36 fix red→green; `--self-test` `0 failure(s) over 5 assertions`) |

The base-side failures in checklist, corpus-integrity and corpus-independent come partly from my sandbox location: `../.ufo/reports/…` pointers resolve against the sandbox, not the fleet root. Base and head sit in the same location, so the base-versus-head comparison stays fair.

### B1 HOLDS (no round harm) / BREAKS reproducibility of a working-tree claim — host opencode replaced mid-session. Severity: low.
`stat` shows `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` with mtime 2026-10-22T17:50:30Z (package `opencode-ai` 1.19.4). `check_substrate_pins.py` in the lane → `FAIL opencode_binary_sha256: expect=179ca421… got=538fcb1b…`, `DRIFT 1/3`, exit 1. The live gate in the lane → `{"pass":6,"fail":1}`, exit 1, failing `surfaces.opencode_extract` ("rule(s) matched nothing: OC-4 …"). Base fails identically, so the round did not cause this. But the uncommitted `SCORECARD.md:32` freshness lead says "No harm: live gate `pass 7`, exit 0 on omp 18.12.6; … pins `OK 3/3`". That no longer reproduces, and the sentence carries no measurement time. [INFERENCE] Something on the host ran `npx opencode-ai` at about 17:50Z, after the L1 ran its guards.
Smallest correction: give the no-harm guard results a UTC timestamp and record the opencode drift (sha `538fcb1b…`, 1.19.4, 17:50:30Z) as host substrate drift outside the round. Do not re-pin the opencode sha inside this round's claims.

### B2 BREAKS — calibration: the uncommitted SCORECARD makes a provenance claim with no artifact behind it. Severity: medium.
`SCORECARD.md:128` (working tree only) says: "the falsify wave ran on live roles only. Verdicts belong to the non-author closure."
Evidence that the attempt-1 falsify wave ran no seats:
- `jq '{members:(.members|length), with_agent:([.members[]|select(.agentId!=null)]|length)}' .ufo/waves/round-52/falsify/swarm-registry.json` → `{"members":36,"with_agent":0}`
- `.ufo/waves/round-52/falsify/` holds only `swarm-registry.json`, with no seat reports.
- `wc -c .ufo/waves/round-52/falsify-gate.txt` → `0` (no slot grant recorded).
- The assignment states that attempt 1's falsify wave "was cut off by the restart and left no seat report".

The same line's headline "**Round 52 completed (hyaku campaign, attempt 1)**" declares completion while attempt 2's falsify wave is still running and no closure exists (premature saturation). Its "Next: round 53" line (`SCORECARD.md:130`) carries "the S024 superseding row; fixture labels for lines 9, 15 and 33". This attempt's milestone lands both, so the line goes stale when attempt 2 lands.
Smallest correction: replace "the falsify wave ran on live roles only" with what the artifacts show (36 registered falsify members, 0 spawned, no reports, cut off by the 17:26Z restart; attempt 2 re-ran the wave). Drop "completed" from the headline until the closure rules. Rewrite the round-53 carry list after attempt 2 lands.

### B3 BREAKS (check level) — consistency: one corpus-integrity check flips from PASS to FAIL. Severity: low.
`python3 -B verifiers/verify_corpus_integrity.py`:
- base: `DRIFT corpus.index.tracked_files 73≠72`, `corpus.index.unindexed 1`, `corpus.pointers.report_total 47≠46`, `corpus.pointers.report_dead 3`, which is `5/9`
- head: `tracked_files 75≠72`, `report_total 47≠46`, `report_dead 3`, **`corpus.pointers.commit_total observed=31 expected=30`**, also `5/9`

The new commit citation is `corpus/knowledge/mcp-server-instructions-round52.md:61` ("frozen at the round-52 plan commit `4c003a4b`"), matched by `COMMIT_RE` (`verify_corpus_integrity.py:146`). The gate exit is 1 at base too, because `verifiers/corpus-baseline.json` has been stale since round 51. So operability is unchanged, but a check that passed at base now fails, and `tracked_files` drifts further.
Smallest correction: re-record `commit_total` (31) and `tracked_files` (75) in `verifiers/corpus-baseline.json`, with the reason stated. Or avoid the ``commit `…` `` citation shape in the entry.

### B4 BREAKS — consistency: dangling pointer in a committed index row. Severity: low.
`corpus/README.md:79` (committed in c8407a4): "| Round-52 lessons | `lessons/round-52.md` | LOG.md round-52 entry; …". `LOG.md` has no round-52 entry at c8407a4 or in the working tree. Its last headings are `:2412` "Round 51 landing …" and `:2423` "Round 51 landing pin and falsify wave", and `git diff --stat c8579a4 c8407a4 -- LOG.md` is empty. Rows 73 and 76 (rounds 50 and 51) point to LOG entries that exist.
Smallest correction: add the round-52 LOG.md entry at landing, or say in the row that it is still to be written.

### B5 HOLDS — calibration: the depth-lead rewrite (`SCORECARD.md:28`, committed) reproduces
The round-51 plan-commit counter, extracted with `git show 7c81a787:verifiers/check_overlap_levers.py` into the sandbox and run with `--rev <r>`:
- `43ca0bfb`: `0 of 7`, exit 1
- `34cfffbb`: **`4 of 7`, exit 1**
- `c8579a4`: `4 of 7`, exit 1
- `c8407a4`: `4 of 7`, exit 1

This matches the rewritten lead ("`0 of 7` … @ `43ca0bfb` → `4 of 7`, exit 1 on the landed content"), and the C2 edit to SKILL.md does not change the round-51 result. The axis score cells are unchanged by both the committed and the uncommitted diff; freshness "held 8" and coverage "held 8.5" are not raised.

### B6 HOLDS — the working-tree coverage cell's tier statement
`git show c8407a4:corpus/SOURCES.md`: S032–S036 and S038 are tier A, S037 is tier B, all `mined` and opened 2026-10-22. `check_mcp_instructions.py --rev c8407a4 --json` backs the MCP specification (S032), Claude Code (S033), VS Code (S034), Codex (S035) and Gemini CLI (S036); opencode and Copilot CLI are not backed. I did not run `--fetch`, so I have not checked the "`--fetch` 5 of 5" statement.

### B7 Observation (tradeoff, not a defect of this round)
The new `verifiers/check_correction_sweep.py --self-test` (`0 failure(s) over 5 assertions`) is not registered in `verifiers/floors-registry.json` or `check_assertion_floors.py` (`grep -c correction_sweep` → 0 in both). It could silently lose assertions, which is exactly the class the floors guard exists for. Separately, SKILL.md line-budget headroom fell from 23 to 13 lines (`trigger.line_budget` 587 of 600).

## Impacted axes
- calibration: B2 (medium) and the timestamp in B1 (low)
- consistency: B3 and B4 (low)
- operability: no gate exit changed between base and head; B7 is advisory
- adjacency: no harm (sibling census and overlap levers both exit 0, unchanged)
- freshness (C1) and coverage (C2): separability holds
