Result: DONE — all 32 registered gates present at base `a975cbbf` exit 0 on their own `--self-test` (89 s wall, 2 concurrent, no timeout kill), and the freeze's 33rd row `check_hook_files.py` — absent at the base rev — exits 0 in a supplementary run at the freeze addendum; receipt written at `.ufo/waves/round-59/receipts/noharm-base-selftests.txt`.

# Round-59 BUILD — no-harm before-column (all gate self-tests at base)

Seat `KotobaR59.ExecNoHarmBase`. Item: run every registered gate's `--self-test` (rows in SKILL.md § Gate registry at `67b68e0f9a0c48e5aa5ced63e6117cfca69da491`) at base `a975cbbf00534443c49bf02e29c813a3db0bf0f8`, record exit code + final line per gate, at most 2 concurrent processes, `timeout 600` each.

## Deliverable

| file | what it is |
|---|---|
| `.ufo/waves/round-59/receipts/noharm-base-selftests.txt` | per-gate exit code, seconds, final line; provenance block; notes |
| `.ufo/waves/round-59/build/ExecNoHarmBase.md` | this report |

Nothing else was written in the lane. No lane file was edited, no git or jj write ran in the lane.

## Headline numbers

- 33 gate rows in SKILL.md § Gate registry at the freeze addendum (`SKILL.md:436-476` there).
- 32 of those scripts exist at base `a975cbbf`; **all 32 exit 0** on `--self-test` (0 nonzero, 0 exit-124 timeouts).
- 1 row (`verifiers/check_hook_files.py`, freeze line 457) does not exist at base: the base rev's SKILL.md registry has 32 rows, and the freeze addendum adds that one row and that one script (`git diff a975cbbf 67b68e0f -- SKILL.md` → exactly one added line, the hook-files row). Its self-test was therefore run supplementarily at the freeze addendum: **exit 0, `self-test: 0 failure(s) over 323 assertions`**, script sha256 `f695d59e…dbe71` (the target counter hash from the claim).
- Assertion totals (printed by each script, verbatim in the receipt): 17, 99, 109, 1-case PASS, 165, 2, 244, 25, 21, 26, 44, 13, 28, (hook counter 323), 105, 17, 2, 55, 239, 68, 21, 62, 20, 330, OK, 89, 99, 152, 56, 10, 123, 1852, 175.
- Longest gate `verify_harness_independent.py` 65 s; whole 32-gate column 89 s wall. Nothing approached the 600 s cap.

## Method (why the sandbox is faithful to the lane)

- `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q <lane> /fast/scratch/hyaku/kotoba-r59/ExecNoHarmBase/world/kotoba-shokunin; git -C … checkout -q a975cbbf…` → `git rev-parse HEAD` = `a975cbbf00534443c49bf02e29c813a3db0bf0f8`.
- The checkout dir is **named** `kotoba-shokunin`, and every fleet-root top-level entry except the lane, `.git` and `.jj` is symlinked read-only into `world/` (52 entries) — the precondition `ExecR2TipReceipts.md` § Method records (checklist name-directory trigger, `../` citation hops). Reproduced the same way; not a new discovery.
- A second checkout `world2/kotoba-shokunin` at `67b68e0f…` with the same linking was used only for the hook counter.
- Runner `/fast/scratch/hyaku/kotoba-r59/ExecNoHarmBase/run_selftests.sh` (sha256 `9a062c16…16701`): `( cd <checkout> && timeout 600 python3 -B <gate> --self-test )`, one `.log` (stdout+stderr) and one `.res` per gate; pairs only, so never more than 2 concurrent processes. `fault_injection_corpus.sh` ran as `bash verifiers/fault_injection_corpus.sh --self-test` (same flag, shell script).
- Exits were captured per gate; the shell's per-line abort on nonzero is why each capture uses `|| rc=$?` (the one intentional nonzero probe below needed it).
- Command string used per gate keeps the registry's script-relative form (no `--rev`/`--fetch`; the Self-test column is `--self-test` for every row, and gates that reject mixing confirm it: `check_hook_files.py:2358`).

## Evidence

Command + exit code + observed output (all run in the sandbox unless stated):

1. Base column — `timeout 3300 bash run_selftests.sh world/kotoba-shokunin logs-base <32 gates>` → `runner exit=0`; 32 `.res` files, all field 2 = `0`. Verbatim rows are in the receipt's table; representative:
   `verify_skill_checklist.py	0	0	2026-10-23T09:37:07Z	0 failure(s) over 1852 assertions`
   `verify_harness_independent.py	0	65	2026-10-23T09:36:02Z	0 failure(s) over 123 assertions`
   `fault_injection_corpus.sh	0	5	2026-10-23T09:35:57Z	self-test: OK`
2. Registry-size measurement — in the base checkout `grep -c '^| \`verifiers/' SKILL.md` → `32`; on the freeze copy → `33`; `git diff a975cbbf 67b68e0f -- SKILL.md` prints the single added line `+| \`verifiers/check_hook_files.py\` | gate | python3 -B verifiers/check_hook_files.py --rev <rev> --fetch …`.
3. Absent-at-base probe — `cd world/kotoba-shokunin && timeout 600 python3 -B verifiers/check_hook_files.py --self-test` → exit **2**, `python3: can't open file '…/world/kotoba-shokunin/verifiers/check_hook_files.py': [Errno 2] No such file or directory` (log `logs-base/check_hook_files.py.absent.log`). This is the honest base-rev result for row 457, not a gate failure.
4. Supplementary run — `cd world2/kotoba-shokunin && timeout 600 python3 -B verifiers/check_hook_files.py --self-test`, started `2026-10-23T09:37:28Z` → exit **0**; output `counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` / `self-test: 0 failure(s) over 323 assertions`.
5. Residue — `git status --porcelain` empty in both checkouts after the runs (all self-test worlds are `$TMPDIR` temp trees: registry column "temp … under `$TMPDIR`").
6. Receipt written, then listed: `ls -l .ufo/waves/round-59/receipts/noharm-base-selftests.txt` → `-rw-r--r-- 1 vgpnk vgpnk 9551 … noharm-base-selftests.txt`.

## Findings for the L1 (before-column consistency)

- **No gate is self-test-broken at base.** The before-column reads 0 nonzero for every gate that exists at `a975cbbf`; any nonzero seen after integration is attributable to the round's changes, not to base state. That is the property this receipt supplies.
- **Row 457 cannot be compared across revs as a normal row.** `check_hook_files.py` is new at the freeze addendum; its before-value is "absent", its supplementary column is exit 0 / 323 assertions. If the plan's counter table wants a literal before/after pair for the hook counter, the before cell is *not present at base*, not "unrun" and not "fails".
- **Gate count discrepancy is explained by the registry diff, not by a dropped gate**: base 32 rows ↔ freeze 33 rows, the delta being exactly the hook-files row. `check_gate_registry.py --self-test` at base (28 assertions) also exits 0, and the round-58 W0 receipt records `check_gate_registry.py --rev` as `0 (32 of 32)` at base — consistent with 32 rows there.
- The base rev's SKILL.md is 596 lines (`wc -l SKILL.md` in the base checkout), matching the claim's "base `a975cbbf` 596"; the freeze addendum's is 597 (one hook-files row). This is a measurement only; budgeting (600-line cap) is the integrator's item.

## Risks / notes

- The receipt's per-gate "final line" is the last non-blank line as printed; three gates end on their own success marker rather than a "`0 failure(s) over N assertions`" line (`check_alwayson_boxes.py`, `check_overlap_levers.py`, `fault_injection_corpus.sh`) — quoted verbatim, exit code carries the verdict. Marked `[INFERENCE]` for `check_overlap_levers.py`'s bare `55 assertions` line in the receipt.
- Full per-gate logs (27513 bytes, 32 logs) live only under `/fast/scratch/hyaku/kotoba-r59/ExecNoHarmBase/logs-base/`; they are scratch, not committed. The receipt carries everything the column needs.
- Self-tests exercise `--self-test` only; they do not run the gates' `--rev`/`--fetch` predicates. This receipt is a harness-health column, not a claim about hook-file evidence — the C1 counter's real predicate is the integration wave's job.
- No tool was installed or upgraded; no network access was used by this seat; no paid model call.
- No blocker.
