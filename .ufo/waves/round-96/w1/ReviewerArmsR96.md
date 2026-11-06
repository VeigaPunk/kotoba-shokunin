# ReviewerArmsR96 — review of the C1 patch (ExecArmsR96)

Verdict: **NO BLOCKING FINDING.** The patch lands C1 at the candidate: `C1-PREDICATE-MET`,
`R95C1-PREDICATE-MET`, `--box-proof` `boxes proven 2`, production text byte-identical, every one of
t01..t11 killed by a behavioural assertion for the stated reason. Three minor (non-blocking)
labelling defects and one disclosed residual risk are recorded below.

Reviewed artifact: `.ufo/waves/round-96/w1/ExecArmsR96/ExecArmsR96.patch`,
sha256 `799bbaac9485587900baeaee0291db2bc5beca97978ab773e2a2d5b770b73088` (8378 B, 139 lines) —
identical before and after the `ExecArmsR96_READY` file appeared, and identical to the sha the READY
names. Base `679775abb9277a7b8d17f060b0f5b4ced2b127b6`; the patch's `index 6e239ae..c6ecbd5` matches
`git rev-parse 679775ab:verifiers/verify_dispatch_prompts.py` = `6e239ae45307fec3cbe89a4d91c839723e893855`.

My candidate: `/fast/scratch/hyaku/kotoba-r96/ReviewerArmsR96/cand` at
`1067e15e8bdc54e3e1edc6bcea08b0096a772e52` (freeze + patch, scratch identity). The builder's named
commit `443430a6` is gone with its clone; the file blob my clone produces is `c6ecbd5b…`, exactly the
blob the patch header names, so the bytes I measured are the bytes the builder measured.

## 1. Behaviour observation (ANTI-SNIFFING) — PASS

Every new arm calls `evaluate_dispatch_04` / `evaluate_dispatch_08` on a `_write_case` fixture tree and
reads the returned verdict / conjunct status. Audit of the 128 added lines: 0 occurrences of `assert`,
`raise`, `print(`, `subprocess`, `socket`, `urllib`, `requests`, `open(`, `__file__`, `inspect.`,
`getsource`; 18 `rec(` call sites (22 assertions after the two loops), 4 `evaluate_dispatch_04` and
5 `evaluate_dispatch_08` calls, 9 `_write_case` calls. No arm reads the instrument's source, its AST,
or its own code objects.

## 2. Kill attribution — PASS (each mutant applied by hand in my candidate clone)

Method: anchors read from the frozen counter (`CLAIMS["c1"]`) by import, applied as literal
single-anchor substitutions to the candidate's `verifiers/verify_dispatch_prompts.py`, then
`python3 -B verifiers/verify_dispatch_prompts.py --self-test` run on disk. Honest control:
`0 failure(s) over 78 assertions`, rc 0.

| mutant | rc | summary | failing assertion(s) — `self-test FAIL:` line |
|---|---|---|---|
| t01-var-dropped | 1 | 2 failures / 78 | `t01/t02 brace form: report path '${LANE}' is not literal, conjunct report_path_literal FAIL: got {'status': 'PASS', 'detail': '1 report path(s), all literal'}` and the same for `t01/t03 bare form` `'$LANE'` |
| t02-var-brace-only | 1 | 1 / 78 | `t01/t03 bare form: report path '$LANE' is not literal, … got {'status': 'PASS', …}` |
| t03-var-bare-only | 1 | 1 / 78 | `t01/t02 brace form: report path '${LANE}' is not literal, … got {'status': 'PASS', …}` |
| t04-le-to-lt | 1 | 2 / 78 | `t04-le-to-lt: round equal to the latest dispatched is PASS on conjunct round_le_latest_dispatched: got {'status': 'FAIL', 'detail': 'round 7 > latest dispatched 7 (kote.report-baseline = 7)'}` (+ the file-verdict arm) |
| t05-finish-allna-pass | 1 | 3 / 78 | `t05-finish-allna-pass: an all-N/A dispatch.08 reads N/A, not PASS: got ('PASS', '1 file(s) evaluated: 0 PASS, 0 FAIL, 1 N/A; 0 out of scope')` (+ two `_finish`-observing arms labelled t11/t10, see §6) |
| t06-role-whole-text | 1 | 2 / 78 | `t06-role-whole-text: a round token only on a later line leaves conjunct filename_role_round_equal FAIL: got {'status': 'PASS', 'detail': 'role line round 7'}` (+ the file-verdict arm) |
| t07-dirs-subset | 1 | 1 / 78 | `t07-dirs-subset: a round-6 path beside the round-7 path leaves conjunct filename_report_dir_round_equal FAIL: got {'status': 'PASS', 'detail': 'report dir round 7'}` |
| t08-bad-first-only | 1 | 1 / 78 | `t08-bad-first-only: a placeholder in the second report path leaves conjunct report_path_literal FAIL: got {'status': 'PASS', 'detail': '2 report path(s), all literal'}` |
| t09-wrong-first-only | 1 | 1 / 78 | `t09-wrong-first-only: a second stem that sorts after the lane id leaves conjunct report_stem_is_lane_id FAIL: got {'status': 'PASS', 'detail': "report stem 'kote' == lane id"}` |
| t10-nonint-baseline | 1 | 3 / 78 | `t10-nonint-baseline: a non-integer baseline leaves conjunct round_le_latest_dispatched N/A: got {'status': 'PASS', 'detail': "round 7 <= latest dispatched 1000000000 (non-integer round in …/nonint/state/kote.report-baseline: 'abc')"}` (+ file and check arms) |
| t11-noreport-04-pass | 1 | 5 / 78 | `t11-noreport-04-pass: a file with no report path has the dispatch.04 file verdict N/A: got {… 'verdict': 'PASS', 'conjuncts': {… all 'PASS' …}}` (+ three conjunct arms + check arm) |
| p00-md-not-stripped (positive) | 1 | 5 / 78 | `control: dispatch.04 verdict PASS: … 'report stem(s) kote.md != lane id'` + 4 box-proof arms |

Every kill is a REPORTED failure: exit 1, a `self-test FAIL: ` line, and a final
`<N> failure(s) over <M> assertions` with N ≥ 1. No kill is a crash / RUN-ERROR.

## 3. Production byte-identity — PASS

`git diff --stat 679775ab..HEAD` → `1 file changed, 128 insertions(+)`, zero deletions.
`git diff -U0` → one hunk, `@@ -799,0 +800,128 @@ def self_test() -> int:`; `self_test` spans
679..1108, `box_proof` starts 1113 — the hunk is wholly inside `self_test()`.
Independent split at `def self_test() -> int:` and the `# box proof` rule:
`head (docstring..run_checks) IDENTICAL (30547 vs 30547 bytes)`, `tail (box_proof..main) IDENTICAL
(9825 vs 9825 bytes)` → `PRODUCTION-BYTE-IDENTICAL`. File mode `100755` preserved. No new top-level
constant or helper was added; the insertion is in-function only.

## 4. Frozen anchors — PASS

All twelve frozen anchor texts (11 targets + positive) still match **exactly once** in the candidate
(`base=1 cand=1 expect=1` for every row); zero occurrences inside the 128 added lines. Every mutated
statement is 1 line → 1 line, so the counter's `code_decoy` line-count guard is satisfied (observed:
all 11 code decoys ran and held). No frozen file was touched: the patch names only
`verifiers/verify_dispatch_prompts.py`.

## 5. Fixture hygiene — PASS

Fixtures are built by `_write_case(root, …)` with `root = Path(tmp)` from
`tempfile.TemporaryDirectory(prefix="dispatch-selftest-")`, which honours `TMPDIR`. Observed: with
`TMPDIR=/fast/scratch/hyaku/kotoba-r96/ReviewerArmsR96`, the t10 failure detail prints
`/fast/scratch/hyaku/kotoba-r96/ReviewerArmsR96/dispatch-selftest-hhv_vjmw/nonint/state/kote.report-baseline`.
After the runs, `find $TMPDIR -maxdepth 1 -name 'dispatch-selftest-*'` returns nothing — cleaned by
the context manager. No added line mentions `/tmp`, `mkdtemp`, or any absolute path.

## 6. Gate readings on the candidate (`1067e15e…`, repo = my scratch clone)

| command | observed |
|---|---|
| `selftest-kills.py c1 <rev> <repo>` | `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11` → `C1-PREDICATE-MET`, rc 0 (11.9 s) |
| `selftest-kills.py r95c1 <rev> <repo>` | `R95C1 targets killed 3 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `R95C1-PREDICATE-MET`, rc 0 (86.9 s) |
| `verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 |
| `verify_dispatch_prompts.py --self-test` | `0 failure(s) over 78 assertions`, rc 0 |
| `check_assertion_floors.py --repo <cand>` | rc 0 (exit 0 = all floors hold); tail shows `PASS dispatch_prompts observed=78 floor=56` among 12 `PASS … observed=N floor=N` rows |
| `selftest-kills.py c1` at base `679775ab` (do-nothing control) | `0 of 11 … C1-PREDICATE-UNMET`, rc 1 — reproduces `receipts/redbefore-c1-base.txt` |

## Findings

### Blocking
None.

### Minor (non-blocking, cosmetic; do not change a reading)

- **M1 — mislabelled assertion (instrument convention).** In the t11 block:
  `rec("t05-finish-allna-pass: the no-report-path dispatch.04 evaluates 1", r["evaluated"] == 1, …)`
  names t05 but observes the t11 fixture's `evaluated` count; `evaluated` comes from `len(files)` and
  is untouched by the t05 mutant, so the assertion cannot guard t05. It should be labelled
  `t11-noreport-04-pass`. Convention: "Every new self-test assertion names the arm it guards."
  No effect on any kill (verified: it holds under t05).
- **M2 — under-describing labels on the two parameter-expansion arms.** The arms are labelled
  `t01/t02 brace form` and `t01/t03 bare form`, but t02 is killed by the *bare* arm and t03 by the
  *brace* arm too (each mutant makes exactly one form pass). A fully accurate label is
  `t01/t02/t03 brace form` / `t01/t02/t03 bare form`. Behaviour and kills are correct; only the
  label under-names.
- **M3 — attribution is many-to-one for t05.** `_finish` is shared, so t05 is killed by three
  assertions (its own all-N/A arm first, then the check-status arms labelled t11 and t10). This is
  honest and stronger than one-arm-per-mutant, but a reader of the counter's per-mutant line should
  not expect a single named arm. Recorded as an observation, not a defect.

### Residual risk (disclosed by the plan, not a defect)

- **R1 — the new arms are not floored.** `floors-registry.json` keeps `dispatch_prompts` at 56
  (observed 78). Deleting exactly the 22 new assertions returns the count to 56 and the anti-shrink
  guard would still read PASS. The plan states this explicitly ("a floor, not an exact count; raising
  it is not claimed"), so it is a disclosed bound of C1, not a patch defect.
- **R2 — frozen-set bound.** Killing t01..t11 shows those eleven mutants are killed, not that every
  mutant is; the sweep's other survivors (sentence-final `.`, empty baseline, fleet-root stem) stay
  out of the set. Disclosed in the plan.
- **R3 — v3 code-object-sniffer bound unchanged.** A mutant that inspects its own compiled code
  objects and proves the decoy guard dead is still not caught. Disclosed.

## Verification gaps

- I did not re-run the five forgery worlds f1..f5 (other seats own that); the counter's decoy
  readings at the candidate are consistent with the pre-data forgery receipts.
- The builder's named commit `443430a6` no longer exists (its clone was removed); identity of the
  measured bytes is established through the patch header blob `c6ecbd5` = my applied blob, not
  through that commit.
- `--box-proof`'s own docstring still lists the clauses it does not prove (unsubstituted variable,
  `<=` at equality, legacy-state arm, non-digit round folder). Those clauses are now covered by the
  self-test, not by the box proof; the docstring is production text and correctly left byte-identical.

## Receipts (this seat)

`.ufo/waves/round-96/w1/ReviewerArmsR96/` — `attribution.txt` (every mutant applied by hand, its
failing `self-test FAIL:` lines), `c1-counter.txt`, `r95c1-counter.txt`, `boxproof.txt`,
`production-identity.txt`. All produced from my own candidate clone, not copied from the builder.

## Tool installs

None. No pacman, no uv, no npm.

## Scratch

`/fast/scratch/hyaku/kotoba-r96/ReviewerArmsR96/` (repo at base, cand at candidate, `attribution.py`,
`bytecheck.py`) — removed before yielding. No lane write beyond this report.
