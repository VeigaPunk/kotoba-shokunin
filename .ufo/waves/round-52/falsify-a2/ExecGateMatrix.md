Result: HOLDS — no exit flipped 0→nonzero and no self-test tally dropped across all 17 lane gates run at both revisions; the only tally change was verify_surfaces.py self-test 119→129 (rose, floor bumped in step). One check-level staleness defect is flagged: `corpus.pointers.commit_total` was PASS at base and is DRIFT at head because the round-52 landing added corpus files and a commit citation without re-recording `verifiers/corpus-baseline.json`.

# ExecGateMatrix — all-gate no-harm matrix (round 52, attempt 2, FALSIFY)

Seat: `KotobaR52a2.ExecGateMatrix`. Target: every script in `verifiers/` (no `scripts/` or `tools/` dir exists in the lane repo), each in its default or documented run mode (`--self-test` included where argparse exposes it), run at base `c8579a4c5b48789e56fb9060ddd48f33569e1215` and head `c8407a453788df964df5a7b835dd0ce1360de882`.

Sandbox (bounds-compliant, read-only lane):
```
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin base && git -C base checkout -q c8579a4c5b48789e56fb9060ddd48f33569e1215
git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin head && git -C head checkout -q c8407a453788df964df5a7b835dd0ce1360de882
# mirror clones + fleet-root symlinks for gates that resolve --repo from the script's grandparent:
#   mirror/base/kotoba-shokunin  (real clone) + sibling-lane symlinks into /home/vgpnk/Projects/shokunin
#   mirror/head/kotoba-shokunin  (real clone) + sibling-lane symlinks
```
All runs used `python3 -B` (no bytecode writes). Counter scripts were run from the head checkout against `--rev <rev>` so the same instrument measures both revisions. Network (`--fetch`) rows used a 120 s timeout. Exact commands are the `argv` column: `<cmd>` run with `cwd` = the clone repo root.

## Matrix

| Script | argv (mode) | rc@base | rc@head | last summary @ base | last summary @ head |
|---|---|---|---|---|---|
| verify_surfaces.py | (default, `--json` same) | 1 | 1 | surfaces.excluded_reason PASS (opencode_extract FAIL) | surfaces.excluded_reason PASS (opencode_extract FAIL) |
| verify_surfaces.py | `--self-test` | 0 | 0 | 0 failure(s) over **119** assertions | 0 failure(s) over **129** assertions |
| verify_corpus_integrity.py | (default) | 1 | 1 | 5/9 pass; DRIFT tracked_files, unindexed, report_total, report_dead | 5/9 pass; DRIFT tracked_files, report_total, report_dead, **commit_total** |
| verify_corpus_integrity.py | `--self-test` | 0 | 0 | 0 failure(s) over 150 assertions | 0 failure(s) over 150 assertions |
| verify_corpus_independent.py | (default) | 1 | 1 | exit 1 | exit 1 |
| verify_corpus_independent.py | `--self-test` | 0 | 0 | 91 assertions, 0 failures | 91 assertions, 0 failures |
| verify_dispatch_prompts.py | (default) | 1 | 1 | dispatch.08 PASS (dispatch.04 FAIL) | dispatch.08 PASS (dispatch.04 FAIL) |
| verify_dispatch_prompts.py | `--self-test` | 0 | 0 | 0 failure(s) over 56 assertions | 0 failure(s) over 56 assertions |
| verify_dispatch_prompts.py | `--box-proof --map verifiers/checklist-baseline.json` | 0 | 0 | boxes proven 2 | boxes proven 2 |
| verify_harness_claims.py | (default) | 1 | 1 | 21/28 pass; DRIFT omp.db.rows, offered.skills, cache.misses, catalogue.total, catalogue.missing_names, cache.verified_skills, oc.roots.names_plus_builtin | identical |
| verify_harness_claims.py | `--self-test` | 0 | 0 | 0 failure(s) over 10 assertions | 0 failure(s) over 10 assertions |
| verify_harness_independent.py | (default) | 0 | 0 | 24 derived, 4 scoped out, 0 unlanded | identical |
| verify_harness_independent.py | `--self-test` | 0 | 0 | 0 failure(s) over 123 assertions | 0 failure(s) over 123 assertions |
| verify_skill_checklist.py | (default) | 0 | 0 | governance.citation_resolves PASS | governance.citation_resolves PASS |
| verify_skill_checklist.py | `--self-test` | 0 | 0 | 0 failure(s) over 1851 assertions | 0 failure(s) over 1851 assertions |
| check_assertion_floors.py | (default, meta-guard runs all self-tests) | 0 | 0 | PASS overlap_levers observed=51 floor=51 | identical |
| check_assertion_floors.py | `--self-test` | 0 | 0 | 0 failure(s) over 150 assertions | 0 failure(s) over 150 assertions |
| check_overlap_levers.py | `--rev <rev>` | 0 | 0 | overlap levers backed 7 of 7 clients | identical |
| check_overlap_levers.py | `--rev <rev> --fetch` [NET] | 0 | 0 | quotes found on live pages 7 of 7 | identical |
| check_overlap_levers.py | `--self-test` | 0 | 0 | 51 assertions | 51 assertions |
| check_sibling_census.py | `corpus/knowledge/sibling-overlap-census-round49.md` | 0 | 0 | skill description length 1019 of 1024 | identical |
| check_sibling_census.py | `--self-test` | 0 | 0 | 0 failure(s) over 68 assertions | identical |
| check_substrate_pins.py | (default) | 1 | 1 | DRIFT 1/3 pins: opencode_binary_sha256 | identical |
| check_substrate_pins.py | `--self-test` | 0 | 0 | 0 failure(s) over 62 assertions | identical |
| compare_harness_independent.py | (default) | 1 | 1 | exit 1 — disagreements (catalogue/skill drift) | identical |
| compare_harness_independent.py | `--self-test` | 0 | 0 | 0 failure(s) over 330 assertions | identical |
| box_proof_case_deletion.py | `--rev <rev>` | 0 | 0 | killed 6 of 6 | killed 6 of 6 |
| fault_injection_corpus.sh | (default) | 1 | 1 | verdict: FAILURES PRESENT | verdict: FAILURES PRESENT |
| fault_injection_corpus.sh | `--self-test` | 1 | 1 | self-test: BROKEN (T2,T3 FAIL) | self-test: BROKEN (T2,T3 FAIL) |
| check_callee_rename.py [new@head] | `--rev <rev>` | 0 | 0 | robust 0 of 4 fixtures | robust 4 of 4 fixtures |
| check_callee_rename.py | `--rev <rev> --seed {7,1234,…}` | 0 | 0 | robust 0 of 4 @ all seeds | robust 4 of 4 @ all seeds |
| check_correction_sweep.py [new@head] | `--rev <rev>` | — | 0 | (not present at base) | correction sweep: 0 stale block(s) |
| check_correction_sweep.py | `--self-test` | — | 0 | (not present at base) | 0 failure(s) over 5 assertions |
| check_mcp_instructions.py [new@head] | `--rev <rev>` | 0 | 0 | backed 0 of 7 clients | backed 5 of 7 clients |
| check_mcp_instructions.py | `--rev <rev> --fetch` [NET] | 1 | 0 | found on live page 0 of 0 (no entry at base) | found on live page 5 of 5 |
| sources-census.sh (fleet script, plan's census cmd) | `validate --root <mirror> --file <clone>/corpus/SOURCES.md` | 0 | 0 | file ok | file ok |

New scripts at head (`check_callee_rename.py`, `check_correction_sweep.py`, `check_mcp_instructions.py`) have no base copy — "base" value is the head instrument run against `--rev c8579a4c…`, i.e. the measurement the plan specifies.

## Harm check (per the task's stated criterion)

- **Exit 0 → nonzero:** none. Every row that is 0 at base is 0 at head; every nonzero row was already nonzero at base.
- **Self-test tally drop:** none. All self-tests are byte-identical or rise. The only change is `verify_surfaces.py` 119→129 (the C1 callee-rename arms added assertions; `check_assertion_floors.py` floors bumped in step, floor 119→129, guard PASS at both).
- **New-at-head counters behave as designed:** callee-rename 0→4 of 4 (robust at all seeds 7/1234/0/999), correction-sweep red→green at base→head (0 stale blocks at head), mcp-instructions 0→5 of 7.

## Red-at-both rows — pre-existing, environmental, not a round-52 regression

All are red identically at base and head, and red in the live lane checkout (verified `python3 -B verifiers/<gate>` in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`), so the redness is the substrate, not the commit:

- `verify_surfaces.py` (exit 1): `opencode_extract` FAIL — the installed opencode binary moved to 1.19.4 after the 18.12.x pin; the fixture corpus only covers 1.19.3. The plan's no-harm guard "surfaces --json stays pass 7, exit 0 on omp 18.12.6" is currently FALSE on the live host — but the omp-side checks pass and the failure is identical at base, so C1 did not cause it.
- `check_substrate_pins.py` (exit 1): `opencode_binary_sha256` drift — same substrate move.
- `verify_dispatch_prompts.py` (exit 1): `dispatch.04` FAIL on fleet prompt files (`*-L1.md` report_path_literal / report_stem_is_lane_id) — live fleet state, unchanged.
- `verify_harness_claims.py` / `compare_harness_independent.py` (exit 1): live-omp catalogue/skill drift (`omp.db.rows`, `omp.offered.skills`, `oc.roots.names_plus_builtin`, …) — new skills installed on the host grew the offer catalogue; identical at base.
- `verify_corpus_integrity.py` / `verify_corpus_independent.py` (exit 1): corpus baseline staleness — `tracked_files` 72→73→75 and `report_dead=3` (dead `.ufo/reports/round-{48,51}/kotoba.md` pointers) carried in the lane. See flag below.
- `fault_injection_corpus.sh` default + `--self-test` (exit 1): the fault world's `corpus_integrity` run is dirty at both revisions because the corpus already carries `report_dead=3`; self-test T2/T3 assert a clean world exits 0, which is impossible while the base corpus is already red. Confirmed identical failure in the live lane — environmental, not a round-52 defect.

## Flag — check-level regression inside an already-red gate (not a strict "harm")

`verify_corpus_integrity.py` `corpus.pointers.commit_total`: **PASS at base (30/30) → DRIFT at head (31/30)**, and `corpus.index.tracked_files` drift widened 73→75. Root cause: the round-52 commit `c8407a4` added corpus files and a new commit citation (`4c003a4b` in `corpus/lessons/round-52.md`) but did **not** re-record `verifiers/corpus-baseline.json` (last re-recorded `59903b2`, round 51). This is the same defect class as round 14's "landing a corpus file without re-recording the baseline." It does not flip the gate's exit (still 1) so it is not a "harm" by the stated criterion, and `corpus.index.unindexed` was *fixed* (1→0: the round-51 spot-check file is now indexed). Severity: **low** — routine expectation refresh missed at landing.

Note on `check_overlap_levers.py` showing `7 of 7` at base: the script is identical at base and head (the post-widening falsify-hardened counter), and `--rev` measures corpus *files* at the revision, not script logic — base `c8579a4` already contains the round-51 widened corpus, so 7/7 at base is expected and not a discrepancy. The frozen declared counter (`4 of 7`) lives at plan-commit `7c81a787`/`4c003a4b`, a different revision than the judged base.

## Commands run

The exact invocations are the `argv` column above; every `verify_*`/`check_*`/`compare_*`/`box_proof` was run as `python3 -B verifiers/<script> <argv>` and `fault_injection_corpus.sh` as `TMPDIR=<scratch> bash verifiers/fault_injection_corpus.sh <argv>`, with `cwd` = the clone root (`mirror/base/kotoba-shokunin` or `mirror/head/kotoba-shokunin`). Representative:

```
cd mirror/base/kotoba-shokunin  && python3 -B verifiers/verify_surfaces.py        # rc=1
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/verify_surfaces.py        # rc=1
cd mirror/base/kotoba-shokunin  && python3 -B verifiers/verify_surfaces.py --self-test   # rc=0, 119 assertions
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/verify_surfaces.py --self-test   # rc=0, 129 assertions
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_callee_rename.py --rev c8579a4c…   # robust 0 of 4
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_callee_rename.py --rev c8407a4…   # robust 4 of 4
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_mcp_instructions.py --rev c8407a4… # 5 of 7
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_correction_sweep.py --rev c8407a4… # 0 stale blocks
# network (120s timeout):
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_mcp_instructions.py --rev c8407a4… --fetch   # 5 of 5
cd mirror/head/kotoba-shokunin  && python3 -B verifiers/check_overlap_levers.py   --rev c8407a4… --fetch   # 7 of 7
# fleet census gate (plan's census command), per-clone file:
cd /home/vgpnk/Projects/shokunin && bash scripts/sources-census.sh validate --root <mirror> --file <clone>/corpus/SOURCES.md  # exit 0 both
```

Full per-run stdout/stderr under `/fast/scratch/hyaku/kotoba-r52a2/ExecGateMatrix/logs/` (key: `<label>__<script>__<argv>.out|.err`); summary table `/fast/scratch/hyaku/kotoba-r52a2/ExecGateMatrix/matrix.tsv`.

## Verdict

**HOLDS.** The no-harm-across-gates claim survives: no gate that passed at base fails at head, and no instrument's self-test assertion count dropped. The round-52 instruments (callee-rename, correction-sweep, mcp-instructions) land correctly and the surfaces self-test grew 119→129 with the floor bumped in step. Two low-severity flags for the L1: (a) `corpus-baseline.json` was not re-recorded at landing, leaving a new `commit_total` DRIFT and a widened `tracked_files` DRIFT inside the already-red corpus gate; (b) the plan's recorded "surfaces pass 7 / pins OK 3/3, exit 0 on omp 18.12.6" no-harm guard is stale on the live host because the opencode binary moved to 1.19.4 after the pin — pre-existing substrate drift, identical at base, not a round-52 regression.
