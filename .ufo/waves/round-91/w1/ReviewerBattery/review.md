# ReviewerBattery r91-w1 — attack C1: candidate battery arms, each guard disabled in turn

Candidate under attack: base `9af1a7af2adf0ab07cfd53f92affc1ed8d992262` + `ExecBatteryArms.patch`
only, committed in my scratch clone as `5edb26f83988bef98d4f41a60a465ec82078f881`
(`git rev-parse --show-toplevel` == the scratch clone). The patch was not changed. No network; no
writes outside my named paths; lane untouched.

## Verdicts

### (a) Patch applies on a fresh base clone; manifest rows parse — PASS
- `git clone -q --shared <lane> $D3 && git -C $D3 checkout -q 9af1a7af…` then
  `git -C $D3 apply --check …/ExecBatteryArms.patch` → `APPLY --CHECK OK rc=0`
  (toplevel assertion printed the clone itself first). Two further *actual* `git apply` runs on
  fresh base clones succeeded (candidate build; dirty-worktree rebuild).
- Parse path: `parse_manifest` (imported from the candidate instrument) on the real candidate
  manifest → `parse_manifest OK: 23 rows; kill 17, equivalent 6, survivor 0`;
  `mb rows: ['mb-m2-g1-commit-check-skipped', 'mb-m15-clean-tree-guard-off', 'mb-m16-restore-unverified']`;
  `targets==PROBES keys: True ['verifiers/check_freeze_gate.py', 'verifiers/check_mutation_battery.py', 'verifiers/check_r86_routed_repairs_v3.py']`.
  Every recipe is valid JSON (the builder's double-backslash escaping holds), every anchor matches
  exactly once on the candidate bytes (mb-m2 = 1, mb-m15 = 1, mb-m16 = 1), every mutant compiles.
- Manifest delta is exactly +3 kill rows (base 14 kill + 6 equivalent → 17 + 6), as frozen.

### (b) Candidate `--self-test` line and rc — PASS
- `TMPDIR=<scratch> python3 -B verifiers/check_mutation_battery.py --self-test` →
  `0 failure(s) over 25 assertions`, rc=0 (N=25 ≥ 22; base instrument measured 19 on the same
  host before the patch).
- Full frozen predicate at the candidate rev →
  `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`,
  G1/G2/G3 all `PASS`, rc=0; the three new rows killed via `[bat-self-test exit 0->1]`;
  `G2 copy integrity PASS: 23 mutant copies and 3 revision copies read back`.

### (c) Each guard disabled in turn — PASS (each mutant flips red for its own arm)
Replayed from the candidate manifest recipes with the instrument's own semantics
(json.loads → re.compile → findall==1 → sub), mutant compiled, then `--self-test`:

| mutant | self-test rc | observed |
|---|---|---|
| mb-m2-g1-commit-check-skipped | 1 | `1 failure(s) over 25 assertions` — FAIL `G1 commit check: the refusal says the revision is not a commit` (the disabled check lets the run reach `could-not-evaluate: G1: git show ffff… failed`) |
| mb-m15-clean-tree-guard-off | 1 | `2 failure(s) over 25 assertions` — both FAILs name `G1 clean-tree guard` |
| mb-m16-restore-unverified | 1 | `2 failure(s) over 25 assertions` — both FAILs name `G2 restore read-back` |

No mutant leaves the self-test green. The arms are the kill channel, as designed; consistent with
the builder's `mutant-mb-m2/15/16.txt` receipts and with the candidate battery run, where each mb
row is killed by `bat-self-test exit 0->1`.

### (d) G1 independence: new arms do not read the working tree — PASS
- Grep of the added arm code: no `open(`/`read_bytes`/`read_text` at all. The only such patterns
  in the file are pre-existing: `place()`'s G2 read-back of scratch copies (line 253) and the
  `FX_D5_LINECOUNT` fixture stub string (line 486, reads its own fixture `__file__`). The new
  arms intercept `git()` and `place()` in memory and run against fixture repos built in TMPDIR.
- Behavioral proof: with the working tree sabotaged (`manifest.tsv` ← `GARBAGE\tNOT\tTSV`;
  battery appended `# worktree-only contradiction line`), the run at the candidate rev still
  prints `killed 17 of 17 … survivors 0 of 0`, rc=0 — the garbage working tree is never read.
  Targets restored byte-identical (`cmp` vs `git show rev:path` for both files); a clean re-run
  reproduces rc=0 with the same line. No lane-path literals in the new code.

## Findings (non-blocking)
1. Review-method hazard for the mutation-tester seats: in a clone where a patch is applied but
   NOT staged, `git checkout -- <path>` restores the INDEX (base) bytes. My first mutant replay
   round therefore ran against the BASE instrument and showed the mutants "green over 19
   assertions" — an artifact of the harness, not a candidate defect. Exact-replay harnesses
   should keep a pristine copy of the bytes outside git (as my final round did).
2. The mb-m15/mb-m16 anchor texts also match the BASE bytes (1 each); the anchors are shared
   text, only the candidate carries the arms that observe the disabled guards. No anchor issue.
3. Calibration headroom, not a defect: the battery's frozen run went 26 s (base) → 39 s
   (candidate) with the third probe target; each probe stays far inside PROBE_TIMEOUT 120 s.

## Frozen-predicate conformance (attack view)
The candidate satisfies the C1 sentence exactly: predicate line verbatim, rc 0, guards PASS,
self-test `0 failure(s) over 25 assertions` (25 ≥ 22), manifest +3 kill rows, two-sided rule
untouched (6 equivalents survived, 0 disclosed survivors). No defect found in the patch.
