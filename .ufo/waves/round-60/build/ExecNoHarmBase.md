Result: DONE — all 33 registered gates exist at base `31092dc6` and every one exits 0 on its own `--self-test` (114.73 s wall, 2 concurrent, no timeout kill); the two prescribed commands are recorded (corpus integrity exit 1 with 5 pre-existing DRIFT, gate registry exit 0 / 33 of 33); receipt at `.ufo/waves/round-60/receipts/noharm-base-selftests.txt`.

# Round-60 BUILD — no-harm before-column (all gate self-tests at base)

Seat `KotobaR60.ExecNoHarmBase`. Item: run every registered gate's `--self-test` (rows in SKILL.md § Gate registry at `31092dc6f875370bddd6eb1e4da4ca0d210c56af`) under `timeout 600` each, at most 2 concurrent, record exit code + final line per gate; also run `python3 -B verifiers/verify_corpus_integrity.py` and `python3 -B verifiers/check_gate_registry.py --rev 31092dc6f875370bddd6eb1e4da4ca0d210c56af`.

## Deliverable

| file | what it is |
|---|---|
| `.ufo/waves/round-60/receipts/noharm-base-selftests.txt` | per-gate exit code, seconds, final line; the two prescribed commands' verbatim output; provenance; notes |
| `.ufo/waves/round-60/build/ExecNoHarmBase.md` | this report |

Nothing else was written in the lane. No lane file was edited; no git or jj write ran in the lane; no lane commit was made.

## Headline numbers

- **33 gate rows** in SKILL.md § Gate registry at the base rev, lines 458–490. The Self-test column is `--self-test` for every row (measured: `grep '^| \`verifiers/' SKILL.md | awk -F'|' '{print $6}' | sort | uniq -c` → `33  \`--self-test\``).
- **All 33 scripts exist at the base rev and all 33 exit 0** on `--self-test`: 0 nonzero, 0 exit-124 timeout kills.
- Longest gate `verify_harness_independent.py` 78 s; whole column 114.73 s wall. Nothing approached the 600 s cap.
- `verify_corpus_integrity.py` → **exit 1, 4/9 checks pass, 5 DRIFT** (before-value, not a round-60 regression).
- `check_gate_registry.py --rev 31092dc6…` → **exit 0, "gate registry rows conformant 33 of 33 lane verifiers; phantom 0"**.
- Assertion totals, verbatim from each script: 17, 99, 109, 1-case PASS, 165, 2, 244, 25, 21, 26, 44, 13, 28, 323, 105, 17, 2, 55, 239, 68, 21, 62, 20, 330, OK, 89, 99, 152, 56, 10, 123, 1852, 175.

## Method (why the sandbox is faithful to the lane)

- `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r60/ExecNoHarmBase/world/kotoba-shokunin && git -C … checkout -q 31092dc6f875370bddd6eb1e4da4ca0d210c56af` → `git rev-parse HEAD` = `31092dc6f875370bddd6eb1e4da4ca0d210c56af`.
- The checkout dir is **named** `kotoba-shokunin`, and every fleet-root top-level entry except the lane, `.git` and `.jj` is symlinked read-only into `world/` (62 entries) — the precondition recorded in `.ufo/waves/round-59/build/ExecNoHarmBase.md` § Method (checklist name-directory trigger, `../` citation hops). Reproduced the same way; not a new discovery.
- Runner `/fast/scratch/hyaku/kotoba-r60/ExecNoHarmBase/run_selftests.sh` (sha256 `9a062c16…a16701`, byte-identical to round-59's): `( cd <checkout> && timeout 600 python3 -B <gate> --self-test )` per gate, one `.log` (stdout+stderr) and one `.res` per gate, **pairs only**, so never more than 2 concurrent processes. `fault_injection_corpus.sh` ran as `bash verifiers/fault_injection_corpus.sh --self-test` (shell script, same flag).
- The registry's own entry-command forms were used verbatim except for the `--rev <rev>`/`--fetch` arguments, which the Self-test column does not name; `check_gate_registry.py` and `check_hook_files.py` refuse `--self-test` mixed with `--rev`/`--fetch`/`--json` (the latter at `check_hook_files.py:2358`), so the self-test form is the only coherent one.
- A second checkout `world2/kotoba-shokunin` at the freeze rev `b1cd64bb45eee744c4ec93be8631f1eddb28fddd` and at the lane tip `49f7ff22a3c93a80d649611e9f6e4b8a4b43af35` (same symlink linking) was used only for the supplementary observations below.

## Evidence

Command + exit code + observed output (all run in the sandbox unless stated):

1. **Base column** — `timeout 1800 bash run_selftests.sh world/kotoba-shokunin logs-base <33 gates>` → runner exit 0; 33 `.res` files, every field 2 = `0`. Representative rows (full table is in the receipt):
   - `verifiers/box_proof_case_deletion.py  0  1  self-test: 0 failure(s) over 17 assertions`
   - `verifiers/verify_harness_independent.py  0  78  0 failure(s) over 123 assertions`
   - `verifiers/fault_injection_corpus.sh  0  7  self-test: OK`
2. **Registry read** — in the base checkout `grep -c '^| \`verifiers/' SKILL.md` → `33`; `wc -l SKILL.md` → `587`; `git diff 31092dc6 b1cd64bb -- SKILL.md` → empty (identical SKILL.md at both revs).
3. **`verify_corpus_integrity.py`** — `cd world/kotoba-shokunin && timeout 600 python3 -B verifiers/verify_corpus_integrity.py` → exit **1**; `DRIFT corpus.index.tracked_files: observed=97 expected=81`, `DRIFT corpus.index.unindexed: observed=1` (`corpus/lessons/round-59-verifier-spotcheck.md`), `DRIFT corpus.pointers.report_total: observed=66 expected=51`, `DRIFT corpus.pointers.commit_total: observed=33 expected=32`, `DRIFT corpus.pointers.commit_unresolvable: observed=1` (`corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff`); `4/9 checks pass`.
4. **`check_gate_registry.py --rev 31092dc6…`** — exit **0**; `gate registry rows conformant 33 of 33 lane verifiers; phantom 0` (33 `OK` lines).
5. **Residue** — `git status --porcelain` empty in the base checkout after all 35 runs (0 lines); every self-test's temp tree went to `$TMPDIR`.

## Findings for the L1 (before-column consistency)

- **No gate is self-test-broken at base.** The before-column is 0 nonzero for every registered gate at `31092dc6`; any nonzero seen after integration is attributable to the round's changes, not to base state. That is the property this receipt supplies.
- **`verify_corpus_integrity.py`'s before-value is RED, not green.** Base = exit 1, 5 DRIFT. The identical five names and counts hold at the freeze rev `b1cd64bb` and at the lane tip `49f7ff2` (measured in `world2`). So the round-60 baseline for this gate is "exit 1 / 5 DRIFT"; an after-column that still reads exit 1 with the same five names is not a regression, and a green run would be an improvement. The one actionable item in the base column: `corpus/lessons/round-59-verifier-spotcheck.md` (landed at `31092dc`) has **no row in `corpus/README.md`** (`grep -c round-59-verifier-spotcheck corpus/README.md` → 0), which is the `unindexed 1` finding — the same defect class round 58 landed and round 59 indexed.
- **The gate-registry gate is RED at every rev that carries the new counter, and green at the base.** Measured: base `31092dc6` → exit 0, 33 of 33; freeze `b1cd64bb` → exit **1**, "33 of 34 lane verifiers; phantom 0", with `verifiers/check_scoped_rules.py    no registry rows naming it: 0 (need 1)`; lane tip `49f7ff2` → exit **1**, same. The cause is structural, not a typo: `check_gate_registry.py`'s universe is every `.py`/`.sh` blob under `verifiers/` at the rev (`Tree.universe()`, `check_gate_registry.py:118-129`) and each needs exactly one registry row (`judge()`, `:225-235`). The round-60 counter file therefore makes the registry gate red until its SKILL.md § Gate registry row lands (build-spec item `ExecGateRegistry` owns the row). This is a **known red at the freeze**, not something the round introduced silently — the L1 should record it as an owed row, not as a passing before-column.
- **The base rev has no `verifiers/check_scoped_rules.py` at all** (`git ls-tree --name-only 31092dc6 verifiers/ | grep -i scoped` → no match, exit 1). The counter first exists at `49c3e87d` (sha256 `6aea3be0…`, the v1 freeze) and is v2 from `b1cd64bb` (sha256 `ca2585a4…`, unchanged at the tip `49f7ff2`). So the round-60 counter has **no before-value in this column** — it cannot be compared across revs the way `check_hook_files.py` was in round 59; its own self-test is covered by the freeze receipts (`.ufo/waves/round-60/receipts/freeze-selftest.txt`, `freeze2-selftest.txt`), not by this one.
- **The assertion-floors guard is green at base and unchanged at the tip.** `check_assertion_floors.py` (live, not self-test) exits 0 at the base with all 14 floors holding (harness 10, corpus_integrity 152, corpus_independent 99/93, surfaces 175, checklist 1852, pins 62, harness_independent 123, compare_harness_independent 330, floors_guard 165/150, dispatch_prompts 56, sibling_census 68, overlap_levers 55/51, alwayson 89, correction_sweep 25) and the same 14 PASS lines at the tip (135.63 s). The new counter is not yet an instrument of that registry; adding it (if the round wants a floor on it) is `ExecGateRegistry`'s item.
- **Line budget headroom at the base is 13 lines** (587 lines, bound "File ≤ 600 lines" at `SKILL.md:306`, box `trigger.line_budget`). The claim's C1 shape (a ~14-line `### Scoped rule files by client` section) therefore needs an equal or larger verbatim move out, exactly as the claim states; the registry row for the new counter adds one more line to the spend. Measurement only — budgeting is the integrator's item.

## Risks / notes

- The receipt's per-gate "final line" is the last non-blank line as printed; three gates end on their own success marker rather than a "`0 failure(s) over N assertions`" line (`check_alwayson_boxes.py`, `check_overlap_levers.py`, `fault_injection_corpus.sh`) — quoted verbatim, exit code carries the verdict. Marked `[INFERENCE]` for `check_overlap_levers.py`'s bare `55 assertions` line.
- Self-tests exercise `--self-test` only; they do not run the gates' `--rev`/`--fetch` predicates. This receipt is a harness-health column, not a claim about the C1 counter's predicate — that is the integration wave's job.
- Full per-gate logs (33 files, 30418 bytes) live only under `/fast/scratch/hyaku/kotoba-r60/ExecNoHarmBase/logs-base/`; they are scratch, not committed. The receipt carries everything the column needs.
- No network access was used by this seat (no `--fetch` in any command), no paid model call, no tool installed or upgraded.
- No blocker.
