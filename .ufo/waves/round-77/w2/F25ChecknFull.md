# F25ChecknFull — round 77 w2 full battery

Measured revision: `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (`round-77: freeze plan, base receipts (counters unchanged from r76 freeze)`). `git status --short` showed staged 0, unstaged 0, and 35 untracked w1/w2/build/receipt items. At the measured commit, `git cat-file -e HEAD:corpus/knowledge/description-craft-round76.md` and `git cat-file -e HEAD:corpus/lessons/round-76.md` both failed (exit 128, path absent). Thus the round-77 claims are not committed at the assigned HEAD. Draft/receipt presence in the worktree is not proof of a landed claim; no assertion below treats it as landed.

Counter integrity: `sha256sum verifiers/check_desc_craft.py verifiers/check_r75_routed_repairs.py` returned respectively `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` and `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63`, exactly the plan pins.

## Frozen claims at HEAD

Commands ran from the isolated `git clone --shared` scratch clone, with `--repo /fast/scratch/hyaku/kotoba-r77/F25RunFull/clone` and the measured revision above; its top-level assertion succeeded. Scratch clone was removed before reporting.

- `python3 -B verifiers/check_desc_craft.py --repo "$S/clone" --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `description craft backed 0 of 6`, exit 1. The counter reports a–f fail; entry and lesson absent at revision. This matches the frozen red-at-base contract, and does not verify C1.
- `python3 -B verifiers/check_r75_routed_repairs.py --repo "$S/clone" --work "$S/work" --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` → `r75 routed repairs closed 0 of 4`, exit 1; R1–R4 open. This matches the frozen red-at-base contract, and does not verify C2.
- `python3 -B verifiers/check_desc_craft.py --self-test` → 0 failures / 53 assertions, exit 0.
- `python3 -B verifiers/check_r75_routed_repairs.py --self-test` → 0 failures / 27 assertions, exit 0.

## No-harm battery at the assigned HEAD

All commands executed in the same scratch clone unless noted. Each exit below is the invoked gate's own status, not a pipeline status.

| Command | Observed result | Exit |
|---|---|---:|
| `python3 -B verifiers/verify_corpus_integrity.py --json` | DRIFT: tracked files 146 vs 144; 2 unindexed spot-check lessons; report pointers 102 vs 99; commits 44 vs 43 | 1 |
| `python3 -B verifiers/verify_corpus_independent.py --json` | unindexed count 2; reports the same unindexed round-75/76 spot-check lessons | 1 |
| `python3 -B verifiers/check_gate_registry.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` | 60/62 lane verifiers conformant, phantom 0; C1 and C2 have no registry rows | 1 |
| `python3 -B verifiers/check_assertion_floors.py` | checklist self-test failures 2; remaining listed floors pass | 1 |
| `python3 -B verifiers/check_tip_battery.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` | guards 5/5, tip battery 1/6; nested registry/floors/checklist/corpus checks exit 1; correction sweep exit 0 | 1 |
| `python3 -B verifiers/verify_skill_checklist.py --json` | 8 pass, 3 fail: name-vs-directory (`clone`), plus two citation resolution failures (clone-path context) | 1 |
| `python3 -B verifiers/check_skill_evals_v2.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e` | `skill eval artefacts verified 2 of 10`; missing the expected SKILL.md row | 1 |
| `wc -l < SKILL.md` | 590 lines (within plan's ≤600 limit) | 0 |
| `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | `kotoba ok`; W04 duplicate-URL warnings, including S213, reported | 0 |

These are HEAD/base results, not final-tip results. The red corpus checks, missing registry rows, and absent claim data prevent claiming the planned final no-harm battery passed. The checklist result also has clone-name/path dependent failures and is not evidence of a lane-content regression by itself.

## Verdict / axes

C1 depth and C2 consistency/calibration remain unverified because the data is absent from the measured commit. Freshness and operability are not established: the required final green corpus and full battery do not exist at this revision. The frozen counter bytes are unchanged and their self-tests passed, but that does not replace a successful counter run on landed claim data. No minimal content repair is responsibly specified from this base-only measurement; the required next evidence is a committed data tip followed by this exact battery on that tip. No tools installed.

VERDICT: BLOCKED — assigned HEAD is the pre-data freeze; C1/C2 are red as specified and final no-harm is not green.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F25ChecknFull.md