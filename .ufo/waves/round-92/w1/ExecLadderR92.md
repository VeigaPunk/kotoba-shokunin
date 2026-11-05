# ExecLadderR92 — C2(b) build report (round 92, wave r92-w1)

Candidate: `e073723ae667b64e534f8621bddb83ad12ad0e71` (freeze base) + `ExecLadderR92.patch`
= scratch commit `9e267a6e4caaed1bb89060cbe2bfe027226cf717` (scratch identity, inside the scratch clone only).

## Files changed (patch: `.ufo/waves/round-92/w1/ExecLadderR92/ExecLadderR92.patch`)

- `verifiers/check_freeze_gate.py` — three fail-closed rungs + three named self-test arms.
- `verifiers/floors-registry.json` — `freeze_gate` floor 31 → 34 (only that cell).
- `verifiers/check_assertion_floors.py` — the two `freeze_gate` cells (`EXPECTED_INSTRUMENTS` line 206, `INSTRUMENTS` line 292) 31 → 34 (only those).
- `verifiers/check_tip_battery.py` — `INSTRUMENT_PINS` appends only: a new `verifiers/check_freeze_gate.py` key (freeze-base blob `a6f18c27…`, kept; candidate blob `856f543b…`), and candidate blob `4ed35c4e…` appended to the `check_assertion_floors.py` tuple (earlier blobs kept).

## Behaviour

1. **Rung 1, `--work` unusable** (`_work_root_problem`, called in `run_gate` after parse, before any control runs): `os.makedirs` + a probe `mkdtemp`/`rmdir` under the root. `NotADirectoryError`/`FileExistsError` → `COULD-NOT-EVALUATE --work <path>: not a directory`, exit 2. Other `OSError` → `COULD-NOT-EVALUATE --work <path>: <exc>`, exit 2. Both regular-file readings verified, zero stderr bytes.
2. **Rung 2, duplicate control name**: `parse_plan` refuses any second `control <name>` at parse time → `INVALID SPEC: duplicate control dup (line 9): already declared at line 7`, exit 3. Nothing runs.
3. **Rung 3, declared `exit 126|127`**: `parse_expect` → `INVALID SPEC: control one27 (line 7): exit 127 is unobservable (126/127 are the harness's own could-not-evaluate codes; a declared 127 can never be compared)`, exit 3. A control that *runs* and exits 127 still reads could-not-evaluate (existing `missing-command` arm, unchanged).

Self-test: `0 failure(s) over 34 assertions`, rc 0 (31 → 34; new arms `arm work-root under-a-regular-file and named-regular-file could-not-evaluate (no traceback)`, `arm parse-duplicate control name is invalid spec, refused before any run`, `arm unobservable-rung declared exit 126/127 is invalid spec`).

## Readings (candidate, run in the scratch clone)

| probe / world | observed | expected |
|---|---|---|
| `rp-work-regular-file.sh` (fixture `fp-minimal`, `--work <file>/sub`) | `COULD-NOT-EVALUATE --work …/notadir/sub: not a directory`, rc 2; script exit 1 (its pass condition is the old crash) | rc 2 named |
| `--work <file>` (named regular file, FileExistsError twin) | `COULD-NOT-EVALUATE --work …/tmp/plainfile: not a directory`, rc 2, 0 stderr bytes | rc 2 named |
| `--work <file>/sub` direct | `COULD-NOT-EVALUATE --work …/plainfile/sub: not a directory`, rc 2, 0 stderr bytes | rc 2 named |
| `rp-duplicate-names.sh` | `INVALID SPEC: duplicate control dup (line 9): already declared at line 7`, rc 3 | rc 3 named |
| `rp-exit127.sh` | `INVALID SPEC: control one27 (line 7): exit 127 is unobservable …`, rc 3 | rc 3 named |
| honest `fp-minimal.md` | `freeze gate: 1 control(s) held`, rc 0 | held |
| honest `r88-controls-fixed.md` | `freeze gate: 4 control(s) held`, rc 0 | held |
| `r88-controls.md` | `REFUSED control w_added_red (line 36)…`, rc 1 | rc 1 (see finding F1) |
| `--self-test` | `0 failure(s) over 34 assertions`, rc 0 | N' = 34 |
| `check_tip_battery.py --rev 9e267a6e… --fleet /home/vgpnk/Projects/shokunin` | `guards 5 of 5; tip battery exit 0: 3 of 6`; `check_assertion_floors.py exit 0` (re-runs freeze-gate self-test at floor 34); reds = `verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent` (same three as base) | guards 5 of 5; rc 1 only from the three carried reds |

Red-before (base) for the same worlds: `redbefore-ladder-{work,dup,127}.txt` (uncaught `NotADirectoryError`; `2 control(s) held`; `COULD-NOT-EVALUATE … rc=127`).

Receipts: `ExecLadderR92/candidate-probes-and-honest-worlds.txt`, `candidate-work-root.txt`, `tipbattery-candidate.txt`, `base/`, `NOTE-probes.txt`.
READY: `ExecLadderR92_READY` → `LADDER-READY N'=34`.

## Findings

- **F1 (plan text, not edited).** `plans/round-92.md` § C2(b) says `verifiers/fixtures/freeze-gate/r88-controls.md` "still exits 0". At base and at the candidate it exits **1** (`REFUSED control w_added_red`). That is the designed unsatisfiable world, and the frozen self-test arm `arm predicate r88-controls world exits 1` asserts 1. The intended honest world is `r88-controls-fixed.md`, which exits 0 on the candidate. The L1 should amend the wording via an addendum if the text is to stand.
- **F2 (rung-3 line convention).** The rung-3 message names the expect line (`line 7`), matching the existing `no stdout literal` convention in `parse_expect`. The duplicate message names the control's own line plus the first declaration's line.
- **F3 (beyond the three named rungs, same class).** `_work_root_problem` also probes writability (a `mkdtemp` in the root) so a non-writable existing `--work` root reads could-not-evaluate instead of a traceback from `run_control`. It is one probe and is the same environment-exception class as rung 1.
- **F4 (docstring prose not edited).** The `check_assertion_floors.py` module docstring still says `freeze_gate 31` in its history prose. The item restricted edits to the two cells, so I left it; the bump-in-step rule may want it updated at landing.
- **F5 (pins keep the base blob).** `check_freeze_gate.py` had no `INSTRUMENT_PINS` key before. The freeze-base blob (identical at 5031a78 and e073723) is pinned alongside the new blob so the pre-patch reading stays green. Pinning the new blob alone would have turned the base reading red.
- **F6 (controls document, inference).** `plans/round-92-controls.md` is a defect-demonstration document. At the candidate its controls expect the defects to still be observable, so re-running it at landing would refuse by design. It is a base-only freeze check, not a landing check. [INFERENCE from the control expectations; not run.]

## Risks

- The `rp-*.sh` probes exit 1 on the candidate by construction (their pass condition is the defect). Any landing check that treats the probe exit code as the gate must read the printed line instead.
- The tip battery's process exit is 1 by carried reds, so a `guards 5 of 5` reading still needs the summary line, not the rc alone.
- Probes were run with `HYAKU_SCRATCH` redirected to my scratch so the L1's `l1-predata` directory was not written.

## Installs / host changes

None. No tools installed or upgraded; no sysctl or kernel setting touched; no pacman.

## Checks for the main agent to run

- `python3 -B verifiers/check_freeze_gate.py --self-test` → `0 failure(s) over 34 assertions`, rc 0.
- `python3 -B verifiers/check_assertion_floors.py --self-test` (≈3 min; the tip battery already exited 0 on it).
- `python3 -B verifiers/check_tip_battery.py --rev <landing>` → `guards 5 of 5`, red only in the three carried corpus gates.
- `python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/round-92-predata/fp-minimal.md` → held.
