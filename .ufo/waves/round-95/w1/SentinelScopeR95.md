# SentinelScopeR95 — scope, safety, no-harm on the round-95 wave-1 candidate (kotoba)

Seat: SentinelScopeR95 (sentinel, attack seat 5 of 12). Lane: kotoba-shokunin.
Base/freeze: `673d1e2e6f850bb54dda9698cf825cf6788c7d0d`. Round base: `2d886a91e57efd3555ec9076a63209e2d8bfbb8d`.
Candidate = freeze + `ExecBatteryKills` patch (verifiers/check_mutation_battery.py) + `ScribeCorpusR95` patch (corpus/SOURCES.md, corpus/lessons/round-95.md, corpus/README.md).
Scratch: `/fast/scratch/hyaku/kotoba-r95/SentinelScopeR95` (TMPDIR=HYAKU_SCRATCH; removed before yield). Candidate clone: `<scratch>/repo` (scratch identity, candidate rev named below).
Waiting on: `ExecBatteryKills_READY`, `ScribeCorpusR95_READY` (poll 120 s, cap 75 min).

## Axes

- A scope-integrity — candidate diff touches ONLY owned files; frozen files byte-identical.
- B no-harm — every landing gate green on the candidate.
- C safety — no /tmp, no network, no credential shapes, fixture git hygiene.
- D evidence-fidelity — every check cites command + observed line + PASS/FAIL.

## Status

- [x] plan round-95.md read in full; counter header read.
- [x] scratch dir + clone at freeze; receipts copied (redbefore-c1-base, poscontrol-r94c1-base, census-before).
- [x] base census-before receipt: 34 W04 rows, `rc=0` (copied under receipts/).
- [x] READY files present (poll cycle 5/6, ~10 min): ExecBatteryKills (patch sha256 `f9506fe3…bc41d96` verified), ScribeCorpusR95 (sha256 `6007a3a4…f68ac0e7` verified)
- [x] candidate built: **`cbadcf02589184980c43059c656f08f59b104208`** (my clone; builder's own candidate rev `3d13eb93…` is the same two patches at a different commit time — sha256s match the READY declarations)
- [x] scope checks — all PASS
- [x] no-harm checks — all PASS (c2 candidate: see below)
- [x] safety checks — all PASS

## Candidate scope (base `673d1e2e` → candidate `cbadcf02`)

| check | command | observed | verdict |
|---|---|---|---|
| changed paths | `git diff --name-status 673d1e2e cbadcf02` | only `M corpus/README.md`, `M corpus/SOURCES.md`, `A corpus/lessons/round-95.md`, `M verifiers/check_mutation_battery.py`; 243 insertions, 0 deletions | PASS |
| nothing else touched | `git diff --name-only … \| grep -vE owned` | no output (grep exit 1) | PASS |
| SKILL.md byte-identical | `git rev-parse cbadcf02:SKILL.md` | `e3b2524131a192172f357af3ca0e013511cbeea4` = base blob | PASS |
| manifest.tsv untouched | `git rev-parse cbadcf02:verifiers/fixtures/mutation-battery/manifest.tsv` | `ebdc4570f6526e3d7b089147ae7bf1b470eeaeab` = base blob | PASS |
| instrument production code | `git diff` hunk headers | single hunk `@@ -838,6 +838,73 @@ def self_test() -> int:` — all 67 lines inside `self_test()` (nested `_commit`/`_extra_kill_rows` helpers), mode `100755` unchanged | PASS |
| frozen anchors intact | `grep -cF` per anchor on candidate file | `committed = git_show(lane, rev, MANIFEST)…` 1; `raise CouldNotEvaluate("manifest must name exactly the targets %s"` 1; `return n == want, "observed` 1; `ok_pin, pin_detail = kill_set_check(committed, pinned)` 1; `print("could-not-evaluate: %s" % exc)` 3 — exactly as declared | PASS |
| corpus rows | `git diff … -- corpus/` | exactly ONE README index row (line 197, Round-95 lesson) + ONE SOURCES row (S270) + new lesson file | PASS |

## Candidate no-harm

| check | command | observed | verdict |
|---|---|---|---|
| gate registry | `cd $D && python3 -B verifiers/check_gate_registry.py --rev cbadcf02` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 | PASS |
| r93 killpin | `bash verifiers/fixtures/round-93/c1-killpin-rev.sh cbadcf02 $D` | `C1-PREDICATE-MET`, rc 0 | PASS |
| r93 pinkey | `bash verifiers/fixtures/round-93/c2-pinkey.sh cbadcf02 $D` | `C2-PREDICATE-MET`, exit 0 (honest instrument-pin PASS, guards 5 of 5; keydrop/keyswap 4 of 5 naming check_correction_sweep.py) | PASS |
| r94 counter c1 | `python3 -B verifiers/fixtures/round-94/selftest-kills.py c1 cbadcf02 $D` | `C1 targets killed 3 of 3; positive killed 1 of 1; honest rc 0; decoys held 3 of 3`, `C1-PREDICATE-MET`, rc 0 | PASS |
| r94 counter c2 | `…round-94/selftest-kills.py c2 cbadcf02 $D` | `C2 targets killed 2 of 2; positive killed 1 of 1; honest rc 0; decoys held 2 of 2`, `C2-PREDICATE-MET`, rc 0 | PASS |
| assertion floors | `python3 -B verifiers/check_assertion_floors.py --self-test` (lane tree = base; no `--rev` exists) | `0 failure(s) over 176 assertions`, rc 0; note: `floors-registry.json` pins NO floor for check_mutation_battery.py (no "mutation" key), so the +8 arms need no floors bump — C1's frozen counter is their guard | PASS |
| census | `bash scripts/sources-census.sh validate --file $D/corpus/SOURCES.md` | rc 0, W04 count **34** (unchanged), `file ok …` | PASS |
| v3 counter c1 (claim instrument) | `HYAKU_SCRATCH=$S python3 -B verifiers/fixtures/round-95/selftest-kills.py c1 cbadcf02 $D` | `C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`, `C1-PREDICATE-MET`, rc 0 | PASS |
| v3 positive control | `…selftest-kills.py r94c1 cbadcf02 $D` | `R94C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3`, `R94C1-PREDICATE-MET`, rc 0 | PASS |

Assertion arithmetic: honest self-test 38 (base, redbefore receipt) → **46** on candidate = exactly the 8 new `t.check` arms.

## Candidate safety

| check | command | observed | verdict |
|---|---|---|---|
| no hardcoded /tmp | `git diff \| grep '^\+' \| grep -iE '/tmp'` (added lines, all files) and `grep -c '/tmp'` candidate instrument | no matches (exit 1); instrument full-file count 0 (base also 0) | PASS |
| no network | added-line scan for `socket\|urllib\|httplib\|http.client\|requests` + new-import scan | no matches; diff adds zero imports | PASS |
| no credential shapes | added-line scan for `password\|secret\|api_key\|credential\|token` | no matches; the only identity-like string is the fixture commit identity `battery-selftest <battery-selftest@example.invalid>` | PASS |
| fixture git hygiene | read of added block (lines 839-911) | every git call is `_git_fixture(repo, …)`/`head(repo)` on fixture repos created by `build_fixture` under the self-test scratch root; commit identity is the fixture identity above; no call names the lane or fleet | PASS |
| kills are reported failures | v3 c1 run lines | every target kill is `rc 1 KILLED: N failure(s) over 46 assertions` (N = 1 or 2); run errors 0 | PASS |
| every new assertion names its arm | read of added block | all 8 `t.check` labels begin `n1 manifest-at-rev`, `n5 label-targets-cne`, `arm kill-set-size (n11)`, `n11 accept-plus-two (rev path)` | PASS |

## Findings

1. (non-defect, invocation note) `check_gate_registry.py --rev` resolves the revision in the **current working tree's repo**; run from the candidate clone, not the lane, or it reports `could-not-evaluate: git ls-tree failed: fatal: not a tree object` for a rev that exists only in the clone. Not a counter defect — documented usage; my first candidate attempt hit it and was rerun correctly.
2. Corpus-README grep hits for `/tmp`/`http` are pre-existing base rows (round-13/23/70 history), not candidate additions; the added-lines scan across the whole candidate diff is clean.

## Risks

- None observed on the audited surface. The candidate rev this seat scored is `cbadcf02589184980c43059c656f08f59b104208`; the L1's landing commit will have a different hash — the landing readings must be re-taken there (this seat's role ends at the candidate).

## Baseline readings at freeze `673d1e2e` (for candidate comparison)

| check | command | observed | verdict |
|---|---|---|---|
| assertion floors (base) | `python3 -B verifiers/check_assertion_floors.py --self-test` (lane cwd) | `0 failure(s) over 176 assertions`, rc 0 | PASS |
| gate registry (base) | `python3 -B verifiers/check_gate_registry.py --rev 673d1e2e` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, rc 0 | PASS |
| round-93 c1-killpin-rev (base) | `bash verifiers/fixtures/round-93/c1-killpin-rev.sh 673d1e2e $D` (REPO = my clone) | `C1-PREDICATE-MET`, rc 0 (drop/other/honest conjuncts yes) | PASS |
| census (base) | `bash scripts/sources-census.sh validate --file $D/corpus/SOURCES.md` | rc 0, `grep -c W04` = 34, final `ok` line | PASS |
| round-93 c2-pinkey (base) | `bash verifiers/fixtures/round-93/c2-pinkey.sh 673d1e2e $D` | `C2-PREDICATE-MET`, rc 0 (honest 5 of 5; keydrop/keyswap 4 of 5 naming check_correction_sweep.py) | PASS |

## Findings

(none yet)

## Risks

(none yet)
