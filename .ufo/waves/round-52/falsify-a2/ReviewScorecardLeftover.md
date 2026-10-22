Result: MIXED — every measured value, hash, exit code and command in the SCORECARD.md leftover verifies against observed repo state, and the insertion is append-in-sequence per convention; two wording defects remain — a no-harm sentence now stale because the opencode binary moved at 17:50Z, and "the falsify wave ran" overstating a wave that produced zero seat reports before the 17:26Z restart.

Scope: the uncommitted working-tree diff of `SCORECARD.md` (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff -- SCORECARD.md`, 8 insertions / 2 deletions): coverage row lead, freshness row lead, "Round 52 completed" block, "Next: round 53" block, move-log rows 52. All runs in sandbox clone `/fast/scratch/hyaku/kotoba-r52a2/ReviewScorecardLeftover/repo` @ `c8407a453788df964df5a7b835dd0ce1360de882` (counters read their `--rev` via `git show` from `LANE`; files identical across clones).

# Verified — claims that HOLD

## Coverage row (axes table)
- `python3 -B verifiers/check_mcp_instructions.py --rev c8579a4c…` → `mcp instructions backed 0 of 7 clients`, exit 1. Observed exactly, exit 1.
- Same at `c8407a45…` → `mcp instructions backed 5 of 7 clients`, exit 0 (BACKED: MCP spec, Claude Code, VS Code, Codex, Gemini CLI; unbacked: opencode, Copilot CLI "no rows naming client"). Matches.
- `--fetch` → `mcp instructions found on the live page 5 of 5`, exit 0 (observed now, 2.3 s). Matches "found 5 of 5 quotes on the live pages".
- Frozen claim verified: `git diff 4c003a4b c8407a45 -- verifiers/check_mcp_instructions.py` is empty; file committed at `4c003a4b` (blob `0023d8f5`), unchanged to tip.
- "S032–S036 tier A, S037 tier B": SOURCES.md rows :45-49 are `spec|A`/`docs|A`, row :50 S037 is `docs|B`. The counter requires tier A; the entry's client table cites only S032–S036 (:23-27). Consistent.
- "opencode and Copilot CLI pages opened and silent (sweep)": entry :29-32 records the sweep (`instructions` 0 occurrences on `opencode.ai/docs/mcp-servers.md` etc.).
- Row leads with the declared round-52 result and names the frozen counter. Score cell stays `8.5 — was 8.0`, "score held 8.5" — no move claimed.

## Freshness row (axes table)
- `python3 -B verifiers/check_callee_rename.py --rev c8579a4c…` → `callee-rename robust 0 of 4 fixtures`, exit 1 (each fixture control=True, renamed=False, planted=False). Matches.
- Same at `4c003a4b…` → `0 of 4`, exit 1. Matches "… @ `c8579a4c` and @ `4c003a4b`".
- At `c2107ecf…` → `4 of 4`, exit 0; `--seed 7` → `4 of 4`; `--seed 1234` → `4 of 4`. The move log's "(seeds 52, 7, 1234)" matches the script's `default=52` (`check_callee_rename.py:146`).
- Frozen claim verified: `git diff 4c003a4b c8407a45 -- verifiers/check_callee_rename.py` empty; committed at `4c003a4b` (blob `f50297fb`).
- "fixtures read from `c8579a4c`": `FIXTURE_REV = "c8579a4c…"` at `check_callee_rename.py:61`. Accurate.
- Mechanism sentence matches code: `verify_surfaces.py:216-239` — `OMP_GENERIC_CALL_RE` matches any identifier; a callee is admitted when a call site registers a baseline-declared pair; the `q(u, "evil", "EVIL.md")` decoy is never admitted; a renamed callee's planted pair still FAILs `no_uncovered_class`. "Not covered: a change of call shape" matches the docstring's own limit (:228-230).
- "self-test 119 → 129 (floor 129 in step)": `floors-registry.json` surfaces floor 119 @ `c8579a4c` and `4c003a4b`, 129 @ `c2107ecf` and `c8407a45`; live `--self-test` → `0 failure(s) over 129 assertions`, exit 0. Matches.
- `python3 -B verifiers/check_assertion_floors.py` → 12 PASS lines, exit 0 (includes `surfaces observed=129 floor=129`). Matches "12 PASS".
- Score cell stays `8`, "score held 8" — no move claimed.

## Round-52-completed block (appended at :128)
- Counter values 0→4 of 4 and 0→5 of 7: verified above.
- "Round-51 routed defects 1-2 corrected": `corpus/README.md` index row :75 now names `removed in a scope` (diff `c8579a4c→c8407a45` shows the append), Core note gains the appended "Round 52 correction" paragraph (:155-164); `SCORECARD.md:28` depth cell at `c8407a45` now leads with "declared result, on the counter committed with the plan (`7c81a787`) … `0 of 7` → `4 of 7`, exit 1" — the declared result leads.
- "a third stale place, `PROVINCE.md:17`": confirmed — line 17 still contains "prints `overlap levers backed 7 of 7 clients`"; the correction was appended as line 18 (append-only, not laundered). The commit message's "PROVINCE:17" is consistent.
- The committed sweep check proves it: `python3 -B verifiers/check_correction_sweep.py --rev c8579a4c` → 3 FAILs (`r51-c2-readme`, `r51-c2-scorecard-lead`, `r51-c2-province` naming `PROVINCE.md:17`), exit 1; `--rev c8407a45` → `correction sweep: 0 stale block(s)`, exit 0.
- "S038 supersedes S031": `corpus/SOURCES.md:51` S038 last cell reads `supersedes S031 — the page documents the frontmatter field disable-model-invoca…` (re-opened 2026-10-22T17:07:03Z, byte-identical sha to the S031 fetch).

## Next-round-53 block (appended at :130)
- Candidates match the lesson's carried list: `corpus/lessons/round-52.md:75-77` — "S024 superseding row, fixture labels for lines 9, 15 and 33, D2 F1–F5, the D7 items, R1 and R5 — carried, not worked …" with the M37 reason. The Frontier candidates (omp reading MCP `instructions`, plugin surfaces) match `PROVINCE.md:19` ("Plugin surfaces and measured client behaviour stay Frontier").

## Move-log rows 52 (:264-265)
- Both rows' before/after values, commits, counter filenames, freeze attribution `(frozen 4c003a4b)` and entry paths all verified as above.

## Edit-in-place vs append check
- The two new blocks insert after "Next: round 52" and before the older "Next: round 44" leftover — continuing the chronological sequence 48→53 that the section already uses (:110-130). Not an in-place overwrite.
- Within the two edited axis-row cells, the round-52 text is PREPENDED and the round-51/round-15 history is retained verbatim — the file's own convention ("lead with the declared result" is even codified by `check_correction_sweep.py`'s `lead: true` rule). No prior claim was edited out.

# Findings

## F1 — MEDIUM-LOW (staleness): the no-harm sentence is now false on the live substrate
Freshness row: "No harm: live gate `pass 7`, exit 0 on omp 18.12.6; self-test 119 → 129 (floor 129 in step); pins `OK 3/3`; `check_assertion_floors.py` 12 PASS."

Observed now in the clone @ `c8407a45`:
- `python3 -B verifiers/verify_surfaces.py --json` → exit 1, `pass 6, fail 1`. Failing check: `surfaces.opencode_extract` — "declared opencode class(es) produced by no rule … rule(s) matched nothing: OC-4 … OC-6 …" (omp checks PASS; omp sha256 `85d9daf3…` still matches).
- `python3 -B verifiers/check_substrate_pins.py` → `FAIL opencode_binary_sha256: sha256 drift: expect=179ca421… got=538fcb1b…` / `DRIFT 1/3 pins failed`, exit 1.

Cause, not author error: the live opencode binary `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe` has mtime `2026-10-22T17:50:30Z` — after the 17:26Z restart that killed attempt 1. The claims were true when written (the C1 commit message records "live gate pass 7"); the substrate moved afterward. This is the Q09 drift class the pins gate exists to catch — the gate is working as designed.

Exact fix (append-style qualification, since the block is a completed-round record): qualify the no-harm sentence with its measurement time, e.g. "No harm at write time (~17:2xZ, before the 17:26Z restart): live gate `pass 7` … pins `OK 3/3` …" and record the post-restart drift as carried debt — the "Next: round 53" block already re-measures before-values (Q19), so adding "opencode binary moved 17:50Z; pins now `DRIFT 1/3`, `surfaces.opencode_extract` red" to the carried list keeps the record honest without rewriting the measured claim. Alternatively drop the sentence — it is a no-harm guard, "not part of the statement" per `plans/round-52.md:34`.

## F2 — LOW-MEDIUM (calibration): "the falsify wave ran on live roles only" overstates what happened
Completed block: "the falsify wave ran on live roles only."

Observed: `.ufo/waves/round-52/falsify/swarm-registry.json` registered 36 members, every one `agentId: null`; `falsify-dispatch.json` `resumeSends: 0`; `reportDir` holds only `swarm-registry.json` — zero seat reports. Spec roles: 16 reviewer, 12 scout, 7 critic, 1 connector — indeed all live roles (executor/scribe/mutation were the dead build-wave roles, consistent with `corpus/lessons/round-52.md` M37's route-outage note). The wave was dispatched (`falsify-taskcall-sent.json`, 17:12Z) and killed by the 17:26Z restart before producing any output. Lesson M37 itself says "the wave and its falsify seats are reported as not run."

"Ran" reads as if falsify work exists; none does. Exact fix: "the falsify wave was dispatched on live roles only and killed by the 17:26Z process restart with zero seat reports (attempt 2 re-attacks)". This also future-proofs the block, which otherwise reads as the round's final state.

## F3 — LOW (staleness at integration time): two round-53 candidates are being landed by attempt 2
"Next: round 53" lists "the S024 superseding row; fixture labels for lines 9, 15 and 33 of `strings-omp-18.12.6.txt`" — but this attempt-2 wave's milestone lands exactly those two items. If the wave completes them, the candidate text is stale the moment the file commits. The file's own convention handles this in place: cf. `SCORECARD.md:114` ("Round 49 correction to the `Next: round 49` block above … The candidate is struck; it is not a round-49 item"). Fix: at integration, append a one-line correction striking the two candidates as worked-in-round-52-attempt-2, or amend the list before commit. Low severity: candidates are explicitly candidates, and the lesson records them as carried — a planner would catch it, but the record should not need the catch.

## F4 — nit (over-attribution): "caught by the new check_correction_sweep.py"
"Round-51 routed defects 1-2 corrected (and a third stale place, `PROVINCE.md:17`), caught by the new `verifiers/check_correction_sweep.py`" — per lesson M36 (`corpus/lessons/round-52.md:10`), defects 1-2 were found by the round-51 closure's manual sweep; the new committed check found the third place and now pins all three (verified red→green above). The grammar attaches "caught" to all three. Fix: "…(and a third stale place, `PROVINCE.md:17`, found by the new `verifiers/check_correction_sweep.py`, which now pins all three; M36, Q29)". Cosmetic; the lesson states it correctly.

# Not findings
- No score move is claimed anywhere in the diff: coverage holds `8.5 — was 8.0`, freshness holds `8`, both say "score held" explicitly. Compliant.
- All four commit hashes named (`c8579a4c`, `4c003a4b`, `c2107ecf`, `c8407a45`, plus `7c81a787`/`34cfffbb` in retained history) are the real objects; command strings reproduce verbatim.
- `--fetch` ran live for this review: all five quotes present on the live pages.

# Verification gaps
- The coverage row's "whether each reading is right is reviewer judgment" caveat is satisfied by other seats in this wave; this report verified only the counter-visible properties (location, word count, `instructions`, host, Gate record) plus `--fetch` liveness.
- F1's measured-at time for the stale sentence is inferred from the commit message "live gate pass 7" and the 17:26Z restart; the leftover file itself carries no timestamp. [INFERENCE]

# Environment / tooling
- No installs performed. Sandbox clone: `git clone -q <lane> /fast/scratch/hyaku/kotoba-r52a2/ReviewScorecardLeftover/repo`, checked out `c8407a45`; read-only git in the lane. Network: one HTTP GET set via `check_mcp_instructions.py --fetch` (5 client doc URLs; output above).
