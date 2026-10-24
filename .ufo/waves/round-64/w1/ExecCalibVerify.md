# ExecCalibVerify — round 64 wave 1

## Result

Read-only calibration evidence for the LOG corrections block; no production files changed and no tools installed or updated. The repository tip observed via `git rev-parse HEAD` was `c04fffbeafcaf810897258d56f99cca736ed3a91` (round-64 plan freeze).

## Measured values

| Routed defect / requested check | Measured value | Evidence |
|---|---|---|
| 1 — inherited seat edit | SHA-256 of `git diff 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md`: `4fcd654b601f9bf8744eee9c57b0c12d6cf0509ff028bd657ed575cad01d4579`; exact-case specialized grep found 1 `temporal mismatch` occurrence at line 728. | The diff is measured against the working tree; this measurement alone does not establish that the inherited edit is committed. C2 check 1 requires the marker in the measured committed revision. |
| 2 — control citations | C1 control add commit: `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` (`8c4cefa`); C2 control add commit: `cbbee56e9a3589b0b46736ad36f1b77701def80e` (`cbbee56`). Both controls pin base `35d44b4b` internally. The C1 path is absent from that pinned base: `cat-file -e` failed, exit 128. | Exact log outputs and fatal line below. |
| 3 — owned-axis minimum | depth = 9; consistency (calibration sub-axis) = 10; therefore depth 9 < consistency 10 and depth is the lowest owned axis. | `SCORECARD.md` axes table at the observed tip: depth row's Evidence — command @ tree includes `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` (round 60); consistency row includes `python3 -B verifiers/check_gate_registry.py --rev <rev>` (round 54). |
| 4 — stale assertion count | Existing `check_r63_routed_repairs.py --self-test` prints `self-test: 0 failure(s) over 23 assertions`, exit 0. Correct count is 23, not the intermediate 21 in `ExecW2E2Patch`. | The round-63 spot-check independently records 17 fixed `check()` calls plus 3 arms × 2 checks = 23. |

## Exact retained command evidence

### 1. Added-control revisions

Commands run:

```text
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --diff-filter=A --format='%H %h %s' -1 -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin log --diff-filter=A --format='%H %h %s' -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
```

Exact output and per-command exit codes:

```text
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8 8c4cefa round-63: plan freeze and C1 do-nothing control (v31 5 of 6), census-before
exit=0
cbbee56e9a3589b0b46736ad36f1b77701def80e cbbee56 round-63: wave-1 build — G9 guard closes sixth frozen survivor (v32), r62 routed-repairs counter, S119 + entry, LOG corrections (defects 1-4), w1 evidence
exit=0
```

### 2. Pinned-base absence

Command run:

```text
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -e 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt
```

Exact stderr and exit code:

```text
fatal: path '.ufo/waves/round-63/controls/C1-do-nothing-v31.txt' exists on disk, but not in '35d44b4b4dcdda234b5dbff7af37e432fec55f05'
exit=128
```

### 3. SCORECARD axes table

Read `SCORECARD.md` rows 26–29 at the observed tip. Header: `| Axis | Score | Evidence — command @ tree | Owned? | Last change |`. The owned rows read:

```text
| depth | 9 | … `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` … | … |
| consistency (calibration sub-axis) | 10 | … `python3 -B verifiers/check_gate_registry.py --rev <rev>` … | … |
```

The rows explicitly identify depth as owned in the SCORECARD header (owned axes: depth + consistency) and consistency as the calibration sub-axis; the minimum is depth 9 < consistency 10. The table's evidence-command column is included above so the score comparison is tied to the recorded counting evidence, not a guessed score.

### 4. Routed-counter self-test

Command run:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r63_routed_repairs.py --self-test
```

Exact output and exit code:

```text
      label-only: base: rc=0 count=5 (want rc!=0 count<5)
      honest/base: base: rc=1 count=0 (want rc!=0 count<5)
      fingerprint: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=0 count=5 (want rc!=0 count<5)
      honest/partial: base: rc=1 count=0 (want rc!=0 count<5); partial: rc=1 count=2 (want rc!=0 count<5)
      worktree-read: base: rc=1 count=0 (want rc!=0 count<5); target: rc=1 count=4 (want rc=0 count=5)
      honest/target: base: rc=1 count=0 (want rc!=0 count<5); target: rc=0 count=5 (want rc=0 count=5)
self-test: 0 failure(s) over 23 assertions
exit=0
```

### 5. Seat-edit diff and marker count

Command run:

```text
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff 38defdc -- .ufo/waves/round-63/w2/MutW2SplitClauses.md | sha256sum
```

Exact output and exit code:

```text
4fcd654b601f9bf8744eee9c57b0c12d6cf0509ff028bd657ed575cad01d4579  -
exit=0
```

The exact-case specialized `functions.grep` search returned the sole match at `.ufo/waves/round-63/w2/MutW2SplitClauses.md:728`:

```text
728:   was a **temporal mismatch** on my part.
```

Measured occurrence count: **1**. Per the repository tool policy, I used the specialized grep tool rather than invoking shell `grep -c`; the count above is the exact-case search result.

## LOG.md corrections-block text for L1

Append after the existing round-63 section. Each routed defect is one physical bullet line; line 1 includes the diff digest and marker count, line 2 the control revisions and pinned-base failure, line 3 the owned-axis scores and command-column evidence, and line 4 the corrected assertion count.

```markdown
### Round-63 corrections (appended in round 64; the r63 verifier spot-check's routed defects 1–4)

- **Defect 1 — inherited seat edit.** The working-tree correction to `.ufo/waves/round-63/w2/MutW2SplitClauses.md` has diff SHA-256 `4fcd654b601f9bf8744eee9c57b0c12d6cf0509ff028bd657ed575cad01d4579` against `38defdc`; the exact marker `temporal mismatch` occurs once (line 728). C2 check 1 closes only when this edit is committed at the measured revision.
- **Defect 2 — control citation.** `.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` was added at `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`; `.ufo/waves/round-63/controls/C2-before-r62tip.txt` at `cbbee56e9a3589b0b46736ad36f1b77701def80e`. Both pin `35d44b4b` internally, but `git cat-file -e 35d44b4b4dcdda234b5dbff7af37e432fec55f05:.ufo/waves/round-63/controls/C1-do-nothing-v31.txt` fails (exit 128: path exists on disk, but not in that commit); cite each adding revision plus the pinned base, not the base as the controls' creator.
- **Defect 3 — lowest owned axis.** `SCORECARD.md` owns depth and consistency (calibration sub-axis): depth is 9 with evidence command `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` (round 60), while consistency is 10 with `python3 -B verifiers/check_gate_registry.py --rev <rev>` (round 54); therefore depth 9 < consistency 10 and depth is the lowest owned axis.
- **Defect 4 — stale seat assertion count.** `python3 -B verifiers/check_r63_routed_repairs.py --self-test` prints `self-test: 0 failure(s) over 23 assertions`, exit 0; the spot-check independently counts 17 fixed checks plus 3 arms × 2 checks = 23, correcting `ExecW2E2Patch`'s intermediate `21 assertions`.
```

## Risks / blockers

No blocker to reporting these measurements. The seat-edit hash/count describes the inherited working-tree diff; the edit's inclusion in a future committed revision remains for the L1's integration and C2 measurement to establish. No r64 counter predicate run was requested or claimed here.
