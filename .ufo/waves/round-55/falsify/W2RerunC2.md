Result: BREAKS — C2 predicate fails at tip `f0e6b695`: 25 of 25 probes honoured but 12 of 13 controls; the only miss is `check_assertion_floors.py V` (got 2), caused by the `harness_independent` child self-test exceeding the gate's 120 s nested timeout under load.

## Measurement

Sandbox: `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/W2RerunC2 && git -C … checkout -q f0e6b695b746775823b65a8c45de7d50ea33e84f`. Lane untouched; all execution inside the clone.

Counter sha256 (required `0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d`):

```
0c1258e2c282996a9ea1e5e5da2fa269cdb4c10f88a3ddc17da1f76c8ad56c3d  /fast/scratch/hyaku/kotoba-r55/W2RerunC2/verifiers/check_could_not_evaluate.py
```

Run (`date -u` before clone: `Fri 23 Oct 2026 12:08:51 AM UTC`; counter launched ~00:09:03Z):

```
 21:09:03  up 16:13,  2 users,  load average: 61.72, 84.04, 86.81
measured f0e6b695b746775823b65a8c45de7d50ea33e84f
box_proof_case_deletion.py         R expect 2   got 2 ok
box_proof_case_deletion.py         G expect 2   got 2 ok
box_proof_case_deletion.py         S expect 0   got 0 ok
box_proof_case_deletion.py         V expect 0|1 got 0 ok
check_gate_finding_delta.py        R expect 2   got 2 ok
check_gate_finding_delta.py        R expect 2   got 2 ok
check_gate_finding_delta.py        G expect 2   got 2 ok
check_gate_finding_delta.py        S expect 0   got 0 ok
check_gate_finding_delta.py        V expect 0|1 got 0 ok
check_overlap_levers.py            R expect 2   got 2 ok
check_overlap_levers.py            G expect 2   got 2 ok
check_overlap_levers.py            S expect 0   got 0 ok
check_overlap_levers.py            V expect 0|1 got 0 ok
check_sources_append_only.py       R expect 2   got 2 ok
check_sources_append_only.py       G expect 2   got 2 ok
check_sources_append_only.py       S expect 0   got 0 ok
check_sources_append_only.py       V expect 0|1 got 1 ok
check_mcp_instructions.py          R expect 2   got 2 ok
check_mcp_instructions.py          G expect 2   got 2 ok
check_mcp_instructions.py          S expect 0   got 0 ok
check_mcp_instructions.py          V expect 0|1 got 0 ok
check_description_thresholds.py    R expect 2   got 2 ok
check_description_thresholds.py    G expect 2   got 2 ok
check_description_thresholds.py    S expect 0   got 0 ok
check_description_thresholds.py    V expect 0|1 got 0 ok
check_alwayson_boxes.py            R expect 2   got 2 ok
check_alwayson_boxes.py            G expect 2   got 2 ok
check_alwayson_boxes.py            S expect 0   got 0 ok
check_alwayson_boxes.py            V expect 0|1 got 0 ok
check_callee_rename.py             R expect 2   got 2 ok
check_callee_rename.py             G expect 2   got 2 ok
check_callee_rename.py             S expect 0   got 0 ok
check_callee_rename.py             V expect 0|1 got 0 ok
check_opencode_repin.py            R expect 2   got 2 ok
check_opencode_repin.py            G expect 2   got 2 ok
check_opencode_repin.py            S expect 0   got 0 ok
check_opencode_repin.py            V expect 0|1 got 0 ok
check_correction_sweep.py          R expect 2   got 2 ok
check_correction_sweep.py          G expect 2   got 2 ok
check_correction_sweep.py          S expect 0   got 0 ok
check_correction_sweep.py          V expect 0|1 got 0 ok
check_gate_registry.py             R expect 2   got 2 ok
check_gate_registry.py             G expect 2   got 2 ok
check_gate_registry.py             S expect 0   got 0 ok
check_gate_registry.py             V expect 0|1 got 0 ok
check_assertion_floors.py          G expect 2   got 2 ok
check_assertion_floors.py          S expect 0   got 0 ok
check_assertion_floors.py          V expect 0|1 got 2 MISS
verify_corpus_independent.py       G expect 2   got 2 ok
verify_corpus_independent.py       S expect 0   got 0 ok
verify_corpus_independent.py       V expect 0|1 got 1 ok
could-not-evaluate probes honoured 25 of 25; controls held 12 of 13
EXIT:1
 21:12:24  up 16:16,  2 users,  load average: 93.20, 83.96, 85.87
```

Every MISS line: the single line `check_assertion_floors.py          V expect 0|1 got 2 MISS`.

## Follow-up: which child timed out

Direct rerun (`date -u` `Fri 23 Oct 2026 12:13:30 AM UTC`), `timeout 900 python3 -B verifiers/check_assertion_floors.py`, wall 139.77 s:

```
PASS harness observed=10 floor=10
PASS corpus_integrity observed=152 floor=152
PASS corpus_independent observed=95 floor=93
PASS surfaces observed=175 floor=175
PASS checklist observed=1852 floor=1852
PASS pins observed=62 floor=62
FAIL harness_independent self-test timed out after 120s (hung?)
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=152 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=53 floor=51
PASS alwayson observed=89 floor=89
EXIT:2
```

The timed-out child is `harness_independent` (`verifiers/verify_harness_independent.py --self-test`; nested limit `SELF_TEST_TIMEOUT_S = 120`, `verifiers/check_assertion_floors.py:147`, hit at `:535-537` → exit 2 per docstring `:44-48`).

Second measurement, `PYTHONSAFEPATH=1` (reported beside, never in place; ran concurrently with the plain rerun, so both reflect the same load window, `date -u` `Fri 23 Oct 2026 12:13:30 AM UTC`, wall 140.64 s): identical output line-for-line — `FAIL harness_independent self-test timed out after 120s (hung?)`, `EXIT:2`. PYTHONSAFEPATH makes no observable difference.

Isolation: `timeout 300 python3 -B verifiers/verify_harness_independent.py --self-test` alone (`date -u` `Fri 23 Oct 2026 12:16:02 AM UTC`) printed `0 failure(s) over 123 assertions`, exit 0, wall 221.96 s — the child is not hung; it needs ~222 s under this load, 1.85× the gate's 120 s limit. The child's own floor still holds (123 observed ≥ 123 floor when it does finish; inside the gate it is killed before producing a summary).

## Comparison with `.ufo/waves/round-55/C2-measure-e966cd59.txt`

Identical outcome at the earlier revision: same 25/25 probes, same 12/13 controls, same single MISS (`check_assertion_floors.py V got 2`), exit 1, at load average ~65–104. Between `e966cd59` and `f0e6b695` only commits `f2cc409` (QUALITY/lesson text) and `f0e6b69` (wave evidence) landed; `git diff --stat e966cd59..f0e6b695 -- verifiers/` is empty, so the gate-under-test bytes did not change and the repeat miss is the same load-dependent mechanism, not a regression introduced after e966cd59.

## Findings

1. **C2 predicate: BREAKS at `f0e6b695`.** `could-not-evaluate probes honoured 25 of 25; controls held 12 of 13`, counter exit 1. The frozen summary requires 13/13.
2. **Defect (operability, in `check_assertion_floors.py`):** the gate's real-verdict path returns 2 — `could-not-evaluate` — whenever any child self-test exceeds a fixed 120 s, conflating *cannot evaluate* with *slow under load*. Three of three observations (counter V probe, direct run, PYTHONSAFEPATH run) failed on `harness_independent` specifically; the child completes correctly given 300 s. The gate's judging lines are not wrong; its timeout is load-sensitive at ~60–95 load average. Repair routing: the frozen counter invokes this gate with no arguments (`GATES` real-args `[]`, `verifiers/check_could_not_evaluate.py:80`), so `--self-test-timeout` cannot be supplied by the caller and the counter itself is frozen — the only in-scope repair is inside the gate (raise the `SELF_TEST_TIMEOUT_S = 120` default at `verifiers/check_assertion_floors.py:147`, or retry a timed-out child once before declaring could-not-evaluate). Judging lines (what it reads, compares, counts) stay untouched either way.
3. **No new defect in wave-1 G/S patches:** all 25 could-not-evaluate probes honoured at tip, including the two no-R gates (`check_assertion_floors.py`, `verify_corpus_independent.py`); `corpus_independent` observed=95 ≥ floor=93 reflects the two G-fix assertions (`build/FixCorpusIndependent.md:6`) landing above the unchanged floor — consistent, not drift.

## Verification gaps / residual risk

- All runs were under high fleet load (avg 60–95). Whether the V control holds on an idle host was not measured; the mechanism (fixed 120 s vs. measured ~222 s child) makes a pass at this load implausible.
- The counter's per-probe TIMEOUT (600 s) was not approached; no `None`/timeout misses observed.
- No tools installed; `git`, `python3`, `timeout`, `sha256sum` only. No lane files modified; the clone at `/fast/scratch/hyaku/kotoba-r55/W2RerunC2` remains for reuse.

Report: .ufo/waves/round-55/falsify/W2RerunC2.md
