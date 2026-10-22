# MutBoxProofBase — round-50 build, C2 independent before-measure (operability)

**HOLDS-BOUNDED — applies to C2 (operability): the declared before-value is confirmed at
`killed 0 of 6` (every one of the six must-fail deletions survives with exit 0 and
`boxes proven 2`), and the claim's target `6 of 6` is not yet implemented — `--box-proof`
enumerates only the cases the manifest still lists and never checks that a must-fail case
exists for each conjunct, nor that a PASS control exists.**

Base: `f30464660c675d1c1e2851a3bf0366a3aaffe5a8` (`master`), measured 2026-10-22.
Private clone: `/fast/scratch/hyaku/kotoba-r50/build/MutBoxProofBase/lane` (clean
`git status --porcelain` after every probe; no writes to the lane, the fleet root or any
sibling lane; this report is the only lane file written).

## Counter command

```
python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json
```

Pristine manifest sha256 `af3783949ba01e7a3d0c5701caae26d7d56bb99e7e166fcb25d442090d79ee51`
(identical in the clone and in the read-only lane checkout). Manifest inventory at base
(9 cases): 2 PASS controls (`d04-control`, `d08-control`), 6 must-fail mutants
(`d04-placeholder`, `d04-stem`, `d04-unknown-lane`, `d08-role-round`,
`d08-report-dir-round`, `d08-above-state`), 1 N/A case (`d08-missing-state`).

## The table — six must-fail deletions, one at a time, restored between

Each row: delete one manifest case, run the counter command, restore the exact pristine
manifest bytes, verify the restored sha256 equals the pristine one.

| # | deleted case | check | named conjunct | exit | stdout | verdict | restored sha256 == pristine |
|---|---|---|---|---|---|---|---|
| 0 | (none — pristine baseline) | — | — | 0 | `boxes proven 2` | — | yes (`af378394…`) |
| 1 | `d04-placeholder` | dispatch.04 | `report_path_literal` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |
| 2 | `d04-stem` | dispatch.04 | `report_stem_is_lane_id` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |
| 3 | `d04-unknown-lane` | dispatch.04 | `lane_identity_known` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |
| 4 | `d08-role-round` | dispatch.08 | `filename_role_round_equal` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |
| 5 | `d08-report-dir-round` | dispatch.08 | `filename_report_dir_round_equal` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |
| 6 | `d08-above-state` | dispatch.08 | `round_le_latest_dispatched` | **0** | `boxes proven 2` | **SURVIVED** | yes (`af378394…`) |

**`killed 0 of 6`** — identical to the plan's declared before-value, reproduced independently.
None of the six was inconclusive: the pristine baseline is green (exit 0), so exit 0 under
each deletion is a true survivor, not a red baseline.

## The additional probes

| # | probe | exit | stdout | verdict |
|---|---|---|---|---|
| A | delete **all 6** must-fail cases at once (2 PASS controls + 1 N/A remain) | **0** | `boxes proven 2` | SURVIVED — the corpus with no discriminating case at all still proves both boxes |
| B | delete both PASS controls `d04-control`, `d08-control` | **0** | `boxes proven 2` | SURVIVED — control coverage is not enforced either |
| C | delete the N/A case `d08-missing-state` | **0** | `boxes proven 2` | SURVIVED |
| D | delete all 9 cases | 1 | `boxes proven 0` | killed, but only by the `no fixture cases` guard, not by coverage |
| E | rename a fixture dir on disk (`d04-stem` → `d04-stem-RENAMED`), manifest unchanged | 1 | *(no stdout)* | uncaught `FileNotFoundError` traceback out of `box_proof` (`:799`); not a clean `boxes proven N` report |
| F | delete manifest case `d04-stem`, leave its fixture dir on disk (orphan) | **0** | `boxes proven 2` | SURVIVED — orphan fixture directories are invisible to the proof |
| G | relabel `d04-placeholder`: `report_path_literal` → `report_stem_is_lane_id` | **0** | `boxes proven 2` | **SURVIVED** |
| H–R | the other 11 relabels (each must-fail case relabelled to each of the two other conjuncts of its own check) | 1 | `boxes proven 1` | killed (11/11), stderr `box-proof: <check>/<id>: conjunct <name> is '<status>', expected 'FAIL'` |

Relabel summary: 11 of 12 relabels killed; the one survivor is G, whose case relabels
`report_path_literal` → `report_stem_is_lane_id`. G survives because the `d04-placeholder`
fixture makes **two** conjuncts FAIL at once (`report_path_literal` FAIL and
`report_stem_is_lane_id` FAIL, `lane_identity_known` PASS), so the case's conjunct label is
not what distinguishes it. Per-fixture conjunct statuses measured at base:

| fixture | verdict | report_path_literal | report_stem_is_lane_id | lane_identity_known | filename_role_round_equal | filename_report_dir_round_equal | round_le_latest_dispatched |
|---|---|---|---|---|---|---|---|
| d04-control | PASS | PASS | PASS | PASS | — | — | — |
| d04-placeholder | FAIL | **FAIL** | **FAIL** | PASS | — | — | — |
| d04-stem | FAIL | PASS | **FAIL** | PASS | — | — | — |
| d04-unknown-lane | FAIL | PASS | N/A | **FAIL** | — | — | — |
| d08-control | PASS | — | — | — | PASS | PASS | PASS |
| d08-role-round | FAIL | — | — | — | **FAIL** | PASS | PASS |
| d08-report-dir-round | FAIL | — | — | — | PASS | **FAIL** | PASS |
| d08-above-state | FAIL | — | — | — | PASS | PASS | **FAIL** |
| d08-missing-state | N/A | — | — | — | PASS | PASS | N/A |

## Findings

**F1 (HIGH, structural — the reason the claim's target is not met).** `box_proof`
(`verifiers/verify_dispatch_prompts.py:737-828`) selects cases with
`cases = [c for c in manifest.get("cases", []) if c.get("check") == cid]` (`:791`) and then
iterates only those (`:796`). The only population check is `if not cases:` → `"no fixture
cases"` (`:792-794`). There is no check that each entry of `CONJUNCTS` (`:84-90`) has a
must-fail case, none that a PASS control exists, and none that every fixture directory on
disk is referenced by a manifest case. `CONJUNCTS` is consulted only by the evaluator at
`:317-321`; `box_proof` never reads it. Hence probe A: a manifest holding only the two PASS
controls and the N/A case still prints `boxes proven 2` and exits 0.

**F2 (MEDIUM — the coverage gap is invisible to the always-on detector too).**
`--self-test` also survives the deletions: with `d08-above-state` deleted from the manifest,
`python3 -B verifiers/verify_dispatch_prompts.py --self-test` → exit 0, `0 failure(s) over
32 assertions`. The floors registry row `dispatch_prompts` (floor 32) reruns only
`--self-test`, and no committed gate runs `--box-proof` (`grep -rn "box-proof"` over
`verifiers/` finds only the instrument's own argument and docstring). So the gap F1
describes is not caught by any always-on check.

**F3 (MEDIUM — the plan's counter is not committed).** `plans/round-50.md` defines the C2
counter as "a committed driver that … deletes each must-fail case in turn … prints
`killed K of 6`". No such driver is committed at base (`grep -rn "killed"` over `verifiers/`,
`scripts/` and the wave specs returns none). My probe driver
(`/fast/scratch/hyaku/kotoba-r50/build/MutBoxProofBase/probe_final.py`) is scratch only and is
not a substitute: the build seat must commit the driver for the after-value to be
reproducible from the tree.

**F4 (LOW — one fixture does not isolate its conjunct).** G above: `d04-placeholder` fails
both `report_path_literal` and `report_stem_is_lane_id`, so its `expect_conjunct` label can
be swapped to the stem conjunct with no observable change. The other five must-fail cases
each fail exactly one conjunct, and their relabels are all killed.

**F5 (LOW — the proof's failure mode on a missing fixture directory is a traceback).**
Probe E: renaming a fixture directory on disk while the manifest still names it produces an
uncaught `FileNotFoundError` from `box_proof` (`:799`) with **no** `boxes proven N` on
stdout. Exit is 1, so a gate would still read red, but the stdout contract ("prints exactly
`boxes proven N`") is broken on this path.

**F6 (LOW — D2 wording still overclaims).** The `box_proof` docstring (`:738-739`) still
says the fixtures "discriminate every conjunct", and the `--box-proof` help text (`:487-488`)
still says "the committed fixtures discriminate every conjunct". Measured here: each of the
six named conjuncts does have a must-fail case (paper coverage is complete), but one case
(`d04-placeholder`) is not conjunct-isolated (F4), so its `expect_conjunct` label is not
load-bearing; and the manifest's own note (`:81`) claims "one must-pass control and one
must-fail mutant per conjunct" where only **two** controls exist for six conjuncts. D2's
rewording is still owed.

## Limits

- Measured only the manifest data plane; no instrument source was mutated. The counter ran
  in the clone at base; the pristine command was also run read-only in the lane checkout
  (`-B`, no writes) → `boxes proven 2`, exit 0, identical manifest sha256.
- The live-fleet run (`--json` over `/home/vgpnk/Projects/shokunin/.ufo/prompts`) is outside
  this seat's assignment and was not measured.
- Tools installed or upgraded: none. No pacman/uv/npm transaction; stock `python3` 3.14.8 only.
- Web sources: none opened.

## Evidence (commands, exit codes)

- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin …/lane && git -C …/lane checkout -q f30464660c675d1c1e2851a3bf0366a3aaffe5a8` → exit 0; `git rev-parse HEAD` → `f30464660c675d1c1e2851a3bf0366a3aaffe5a8`.
- Pristine: `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` → exit 0, stdout `boxes proven 2`, stderr empty.
- Same command in the lane checkout (`/home/vgpnk/Projects/shokunin/kotoba-shokunin`, read-only) → exit 0, `boxes proven 2`.
- Rows 1–6 (six single must-fail deletions): exit 0 each, stdout `boxes proven 2`, stderr empty, restored sha256 `af3783949ba01e7a3d0c5701caae26d7d56bb99e7e166fcb25d442090d79ee51` == pristine for 6/6.
- Row A (all 6 must-fail deleted): exit 0, `boxes proven 2`. Row B (both controls deleted): exit 0, `boxes proven 2`. Row C (N/A deleted): exit 0, `boxes proven 2`. Row D (all 9 deleted): exit 1, `boxes proven 0`, stderr `dispatch.04: no fixture cases` / `dispatch.08: no fixture cases`.
- Row E (fixture dir renamed): exit 1, stdout empty, stderr `Traceback … FileNotFoundError` at `verify_dispatch_prompts.py:799`; directory name restored.
- Row F (manifest case deleted, dir orphaned): exit 0, `boxes proven 2`.
- Rows G–R (12 relabels): exit 0 for G (`boxes proven 2`), exit 1 and `boxes proven 1` for H–R, each with stderr `box-proof: <check>/<id>: conjunct <name> is '<status>', expected 'FAIL'`.
- `sha256sum verifiers/fixtures/dispatch-prompts/manifest.json` → `af378394…` before and after every probe (23 rows in `final.json`, all `restored_exact: true`; plus the 2 extra probes in `extra.json`, of which probe E restored the directory name and probe F restored the manifest bytes exactly).
- `sha256sum verifiers/verify_dispatch_prompts.py` → `512cff275e0d4e68ea3bb6b6df5ec877054309ee96b38e70f880167dbba90452` (unchanged); `sha256sum verifiers/checklist-baseline.json` → `049429aaefd85009f55871de0afc593a4e570f757885399cb0963c85e57063e6` (unchanged).
- `git -C …/lane status --porcelain` → empty, exit 0, after every probe.
- `python3 -B verifiers/verify_dispatch_prompts.py --self-test` with `d08-above-state` deleted → exit 0, `0 failure(s) over 32 assertions`.
- Driver and raw results: `/fast/scratch/hyaku/kotoba-r50/build/MutBoxProofBase/probe_final.py`,
  `…/final.json`, `…/relabel.json`, `…/aggregate.json`, `…/extra.json`.
