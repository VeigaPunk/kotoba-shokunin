Result: DONE — every round-56 routed item R1–R8 has a named round-57 answer (or an explicit carried/withdrawn reason), and the round-56 report's only unlabelled bare hashes are the three on line 14; three further non-resolving tokens are `sha256` digest prefixes, both verified against the bytes they name.

Read-only scout. Nothing was written except this report; no counter, verifier, wave context or lane file was touched. Work revision: base `47c05558`, freeze `ee50d8fa`, erratum `01312a77` (all read with `git --no-optional-locks`). Commands and exit states are given with each finding.

## 1. Disposition table — round-56 spot-check R1–R8

Plan anchors are `plans/round-57.md:81-88` (§ Routed defects). "Item" = the `build-spec.json` item that owns the answer (`.ufo/waves/round-57/build-spec.json`, `items[].name`).

| R | plan anchor | round-57 item | answer file / evidence | state at scan (2026-10-23 ~04:5xZ) |
|---|---|---|---|---|
| R1 | `plans/round-57.md:83` | `ExecR1HashCheck` (tool) + `ScribeQuality` Q41 + `ScribeMistakes` M58 | `.ufo/waves/round-57/build/check_report_hashes.sh` (2,747 B, landed 04:48Z; skips `sandbox` lines and digest-marked tokens at `:58,61` (rules described `:14-22`)); Q41 at `build/ScribeQuality.md:7`; M58 at `build/ScribeMistakes.md` (pending) | tool + Q row delivered; M58 report not yet on disk; report half independently verified below |
| R2 | `plans/round-57.md:83-84` | `ScribeR2Corrections` (+ Q42) | `build/ScribeR2Corrections.md` (not yet written); Q42 at `build/ScribeQuality.md:8` | item exists, deliverable pending; nothing landed. Targets confirmed at base `47c05558`: `SKILL.md:109` clause "singular `agent/` still loads per a 2026-01-17 docs commit"; `corpus/knowledge/agent-definition-files-round56.md:35-37`; `corpus/lessons/round-56.md` "Quote notes:" paragraph |
| R3 | `plans/round-57.md:84`, erratum at `:106` | no seat — answered by the freeze/erratum commits | `ee50d8fa` holds v1 C1 sha256 `2ac51d2a2f50d855…` and v1 C2 `b3dbe72fd9383b6d…`; `01312a77` holds v2 C1 `bf11a4efc1c7589a…` (C2 unchanged) and the w0 copies under `.ufo/waves/round-57/w0/` (v1 C1 `2ac51d2a…`, v2 C1 `bf11a4ef…`, v1 C2 `b3dbe72f…`, C2 v2 `8e388382…`). sha256 equality checked with `git show <rev>:<path> \| sha256sum` | satisfied by committed evidence; no scored version is uncommitted |
| R4 | `plans/round-57.md:84`, detail `:39` and `:116` | `ReviewC1Counter` (review) ; rule lives in C1 counter v2 | v2 at `01312a77:verifiers/check_plugin_manifests.py`: held test at path-segment boundaries with the memory-file exclusion — spec `:18-19,146-162`, code `:830` (`token_at_boundary`), `:960` (`held_in_text`), `:1040` (`new_ground`), self-test arms `:161-162` and `:1689-1690` (`.claude/AGENTS.md` does not hold `.claude/agents`); Q43 at `build/ScribeQuality.md:9` | rule + self-test arms present; independent review pending. **Plan-text conflict**: `:39` says "case-sensitively at path-segment boundaries", erratum `:116` says "case-insensitive at path-segment boundaries"; the code implements `:116` and excludes the round-56 symptom by the right-boundary rule (a `.` followed by a letter/digit is not a boundary), not by case |
| R5 | `plans/round-57.md:84`, detail `:40` | `ExecCounterC1` (w0) + `ReviewC1Counter` | `.ufo/waves/round-57/w0/ExecCounterC1.md:187` (v1: 54 killed, 0 survived), `:327` (v2 self-test 0 failures over 235 assertions), `:372` (v2: 72 killed, 1 survived of 73; survivor G06 documented equivalent at `:379`); w0 files committed at `01312a77` | evidence delivered; independent `--self-test` in `ReviewC1Counter` pending |
| R6 | `plans/round-57.md:84-85` | `ScribeR6StaleLine` | `build/ScribeR6StaleLine.md` (landed 04:48Z): target **`SKILL.md:520` at `01312a77`** (base `47c05558` = `:518`; freeze added 2 SKILL.md lines, `git diff --stat 47c05558 01312a77 -- SKILL.md` → `2 ++`); draft one-for-one line replacement, no net growth | draft delivered; not landed |
| R7 | `plans/round-57.md:85-86` | bounds + context + receipt (no single seat); Q44 in `ScribeQuality` | `.ufo/waves/round-57/bounds.md:6` (kill-by-PID + "at most 4 concurrent processes and 120 s"); build context `.ufo/waves/round-57/build-spec.json` `context` at char 3948 has the full form, and `build-dispatch.json.taskCall.context` is byte-identical (both 5,382 B); frozen grep `.ufo/waves/round-57/r7-bound-grep.txt` (04:37:44Z) prints round-56 build-spec/falsify/controls = 0 and round-57 bounds/build-spec/build-dispatch = 1, controls-call = 0; Q44 at `build/ScribeQuality.md:10` | met for the build wave and the receipt "fails on the round-56 build context" is shown. Gaps below |
| R8 | `plans/round-57.md:86-88` | not worked (carried) | plan `:86-88`: anti-loop moves off the agent-definition surface. Checked the whole spec: no item names `check_agentdef_boxes`, and no item edits `verifiers/verify_skill_checklist.py`. C2 seats are inputs only (`ExecC2CounterV3`, `ReviewC2Counter`, `CriticC2Rule`). `ScribeLogScorecard` prompt requires the LOG note "R8 carried" | carried as declared; no seat touches the box counter |

### R1 residual (calibration)
- R1 asked for labels "in every wave context **and** in the report". The report half is now checkable by a tool. The context half is satisfied only indirectly: the wave contexts call `bounds.md` binding and `bounds.md:4` carries "every sandbox commit hash you cite is labelled `sandbox <hash> (…)`, never cited bare", but no context restates it — `grep -c 'never cited bare'` = 0 in `build-spec.json`, `build-dispatch.json` and `controls-call.json`.
- Q41 (`build/ScribeQuality.md:7`) requires the clone path "on the same line"; `check_report_hashes.sh:58-61` skips **any** line containing `sandbox` and does not require a path. The tool is weaker than the criterion it grounds.

### R7 residual (calibration)
- The pre-freeze control call's context carries only the shortened form: `.ufo/waves/round-57/controls-call.json` context at char 1773 says "kill only by the PIDs you started; contention tests capped" — no "4 processes/120 s". The frozen grep therefore prints 0 for that context, and Q44's own criterion ("cap … at 4 concurrent processes and 120 seconds; a context check must fail when either bound is absent") would fail the round-57 controls call. [INFERENCE] The controls call predates the full wording (bounds.md existed, 48 min vs the call's 32 min), so the omission is a dispatch-text bug, not a missing bound: the call points at `bounds.md` as binding.
- The falsify-wave call does not exist yet (`.ufo/waves/round-57/falsify/` is empty), so "every wave context" is unproven for that wave.

## 2. Round-56 report audit (`.ufo/reports/round-56/kotoba.md`, 132 lines)

Method: every hex run of 7–40 chars was checked with `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse --verify -q <tok>^{commit}` (exit 0 = resolves). 35 token occurrences; 29 resolve; 6 do not.

**Bare, unlabelled, non-resolving — line 14 only (the three R1 cites).** All three resolve in the round-56 sandbox clones named by their own receipts, so the correct labels are available:

| token in report | full hash (from receipt) | clone path (receipt line) |
|---|---|---|
| `40c2b5eb` | `40c2b5eb530fac42f26abc7d391651ef9caf92bd` | `/fast/scratch/hyaku/kotoba-r56/CtlC2Heuristics` (`.ufo/waves/round-56/controls/CtlC2Heuristics.md:5`) |
| `41c2f484` | `41c2f4847665b8b6f8f42935b420721bd2c32c39` | `/fast/scratch/hyaku/kotoba-r56/CtlC2GeneratorKeyed` (`CtlC2GeneratorKeyed.md:140`) |
| `7639deba` | `7639debab3d98d812d9de6e8e95f8352a2b76f80` | `/fast/scratch/hyaku/kotoba-r56/CtlC1RealNoForm` (`CtlC1RealNoForm.txt:27`; also present in `/fast/scratch/hyaku/kotoba-r56/L1-recontrol`) |

**Non-resolving but correct digest prefixes (not defects).** `2f672bd1` (lines 14 and 55) and `73497d2a` (line 15) are each preceded by `sha256` on the same line. Both verified against the bytes they name:
- `git show e02f5f5d:verifiers/check_agent_definitions.py | sha256sum` → `2f672bd155a4c125caa7e1758e06137b72ede4caec75d4e67baeee227bbe6c47`.
- The 19-line block `SKILL.md:157-175` at `b0b7140b` has sha256 `73497d2a0440ba83…` and is byte-identical to `corpus/knowledge/render-mechanism-round7.md:100-118` at `f897d18a` (searched all 19-line windows; one match).
- All other 12 distinct tokens (naming 10 commits: `f897d18a`, `b0b7140b`, `0f58a469`, `e02f5f5d`, `c22fdd39`, `96189083`, `3d8efd7c`, `250e3026`, `a5314640`, `15257a27`) resolve, exit 0.

**Path citations.** All 12 shorthand paths resolve once their contextual root is applied — `render-mechanism-round7.md` → `corpus/knowledge/`; `build/ConnSiblingOverlap.md`, `build/ScribeS065.md`, `controls/*`, `census-start.txt`, `census-end.txt` → `.ufo/waves/round-56/`; `check_agentdef_boxes.py`, `check_could_not_evaluate.py`, `check_explicit_invocation.py` → `verifiers/`. No dangling path was found at `f897d18a`.

**Cross-lane citations resolve, but the report gives no repo root.** Line 94 `corpus/knowledge/omp-task-contract.md:168` is `kumitate-shokunin/corpus/knowledge/omp-task-contract.md:168` (exact line holds "Direct `.claude/agents`, `.codex/agents`, and `.gemini/agents` roots are excluded"). Line 95 `cross-lane-scope.md:29` is `kama-shokunin/corpus/knowledge/cross-lane-scope.md:29` (exact line holds "**Kotoba** owns the instruction/agent surface"). Both are accurate, but neither is resolvable from inside `kotoba-shokunin` alone — a reader needs out-of-band knowledge of which sibling lane owns the file.

**One un-receipted observation (not a citation).** The misroot sweep sentence ("`git -C /home/vgpnk/Projects/shokunin status --porcelain` lists 7 untracked fleet-root files") has no committed output under `.ufo/waves/round-56/` (`git ls-tree -r f897d18a -- .ufo/waves/round-56 | grep -i 'misroot\|porcelain'` → only `build/swarm-registry.json` matched a related name). It cannot be re-checked after the fleet root changes. [INFERENCE] Low value to route; it is an observation, not a claim.

Minor: the landed-changes table's "LOG § Round 56" anchor is the heading `LOG.md:2478` ("## 2026-10-23 — Round 56 (…)"); the section exists, only the label is abbreviated.

## 3. Confidence and remaining unknowns
- **Observed (high confidence):** the table above, the token scan, the digest verifications, the counter sha256s per revision, the SKILL.md line shift 518→520, the context texts and their grep counts, the cross-lane line matches.
- **[INFERENCE]:** the R7 controls-call omission is a wording regression (bounds existed before the call); the plan `:39`/`:116` conflict is a stale pre-erratum sentence that the erratum superseded, because every scored control ran on the code that matches `:116`.
- **Unknown / not checked:** whether `ScribeR2Corrections`, `ExecR1HashCheck`'s report and `ScribeMistakes` had landed after this scan (they were absent at 04:5xZ); whether the falsify wave will carry the full bound; whether Q44 as drafted will be applied to the existing controls-call context.
- **Out of scope, one line only:** `CriticC2Rule`'s prompt points at "the ExecC2Fix item", which is not in `build-spec.json` (`items[].name`), so that seat's rule text has no in-wave referent.
