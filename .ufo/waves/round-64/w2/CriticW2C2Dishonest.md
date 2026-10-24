# CriticW2C2Dishonest — round 64, wave 2

Axes: **calibration / consistency**, with a self-test discrimination-depth consequence. C1 is not evaluated here. This is an adversarial report, not an admission or canonical judgment.

## Result

The landed counter correctly measures **4/4, exit 0** at `c019919c97ab5fe98e87a7754b4449ea4e699c99`, **0/4, exit 1** at the frozen base, rejects `--base` with **argparse exit 2**, and passes its **32-assertion** self-test. Its canned unconditional-label, broad-fingerprint, seat-worktree-read, and hardcoded-tally candidates are detected.

**Three additional dishonest variants survive the complete landed self-test, each with `0 failure(s) over 32 assertions`, exit 0:**

1. Replace the score-table derivation with the measured `depth=9, consistency=10` fingerprint.
2. Read `SCORECARD.md` from the dirty worktree rather than the requested committed revision.
3. Print the full 4/4 headline, exit 0 when the requested revision has no LOG blob (including a nonexistent 40-hex revision).

The first two certify an actually constructed, committed wrong-score world as **4/4, exit 0**, where the original returns **3/4, exit 1**. The third certifies the nonexistent `ffffffffffffffffffffffffffffffffffffffff` as **4/4, exit 0**. Exact missing arms below were exercised: original becomes **35 assertions, exit 0**; the three mutants become **2 / 1 / 1 failures, exit 1**, respectively.

These are **fixable self-test discrimination gaps**, not evidence that the original production counter miscounted the measured tip. A finite mutation suite is not proof against arbitrary fixture-aware replacement code; the demonstrated variants do not inspect fixture names or special-case the constructed commit hashes.

## Scope, provenance, and tools

- Read the frozen plan including E1–E3; relevant wave-1 `ExecR64Counter.md`, `MutR64Counter.md`, and `CriticC2Bound.md`; and round-63 `ExecW2E2Patch.md` E2/process analysis.
- Source for every mutant is `git show c019919c97ab5fe98e87a7754b4449ea4e699c99:verifiers/check_r64_routed_repairs.py`, SHA-256 **`8f5b9f915abe6ae42bf84c4c8842ed341c1e03afc184ca23351f33545e5294bf`**. The lane file's observed SHA-256 matched this value before exercising it.
- Only lane write: this report. All constructed repositories, commits, source variants and harnesses are under `/tmp`. No lane Git/jj/index writes, production edits, other-runtime orchestration, or subagent dispatch.
- No tools installed or upgraded. The specified `/home/vgpnk/Projects/shokunin/.omp/agent/RULES.md` was absent; no installation required it. The host-wide pacman pause was respected.
- Reproduction harnesses: `/tmp/kotoba-r64-CriticW2C2Dishonest-probe.py` and `/tmp/kotoba-r64-CriticW2C2Dishonest-base-aware.py`. Result artifacts: `/tmp/kotoba-r64-C2Dishonest-f9a8nm6t/`.
- An initial async self-test attempt was not launched because the tool reported its background-job cap; the subsequent synchronous run completed. A `pty=true` request fell back to non-terminal execution; reported to `xd://report_issue`. Neither affected the observed process exit codes below.

## 1. Real binary and frozen measurements

Actual commands/output, with exit codes captured from subprocess results:

```text
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
[stderr]
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
exit=1
```

The override test used the **real lane binary**, not only a substituted scratch source:

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r64_routed_repairs.py --base 078eec4a1f6a41c64ff8806f58b46a67cd413bfc --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
[stderr]
usage: check_r64_routed_repairs.py [-h] [--rev REV] [--root ROOT]
                                   [--self-test]
check_r64_routed_repairs.py: error: unrecognized arguments: --base 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
exit=2
```

## 2. Arm-to-shortcut mapping (r63 E2 discipline)

Here, **detected** means the process-world auditor rejects the dishonest candidate. The suite itself then stays green because rejection is its expected outcome. **Survived** below means changed counter logic itself passes the entire original suite; these are different observations.

| Shortcut | Landed arm / discriminating world | Observed result |
|---|---|---|
| Unconditionally print `r63 routed defects closed 4 of 4`, exit 0, for every rev | `counter arm: label-only rejected by constructed worlds`; uncorrected **base**, also look-alike | Candidate `base rc=0 count=4`, versus required nonzero/count<4: detected. This does not satisfy the complete two-conjunct predicate at the frozen base. |
| Base-aware label: print 0/nonzero only at BASE_REV and 4/zero everywhere else | Same process-world auditor's **look-alike** world; base/target alone cannot distinguish it | Executed this variant through the original label arm: base `rc=1 count=0`, look-alike `rc=0 count=4`, target `rc=0 count=4`: detected at look-alike. The original source does not separately name a base-aware candidate. |
| Broad fingerprint: marker + old control-base token + lowest/consistency text + 23-assertion text implies all four closed | `counter arm: fingerprint rejected by constructed worlds`; **look-alike** has those tokens but wrong control-commit citation | Candidate base `0`, look-alike `4`, target `4`; honest look-alike `3`: detected. |
| Read seat marker from disk, not `<rev>` | `counter arm: worktree-read rejected by constructed worlds`; committed **target** seat copy removed from disk | Candidate target `rc=1 count=3`, honest target `rc=0 count=4`: detected. This is a seat-file provenance test, not coverage of every evidence file's provenance. |
| Hardcode assertion tally `23`, do not materialize the r63 source | `counter arm: hardcoded assertion tally is rejected`; **substituted-source** world | Candidate `rc=0 count=4` where source substitution must reject: detected. The direct arm is `assertion source substitution rejects stale tally`. |
| Green, partially repaired, or repointed-green pinned control | `base arm: green pinned control refuses certification`; `base arm: partial pinned control refuses certification`; `base arm: repointed green BASE_REV refuses certification` | Original 32-assertion run exercised all three without failure. These are refusal tests, not proof that a source literal can never be edited to a different red baseline. |
| Hardcode the measured axis scores instead of parsing the score table | **No discriminating landed arm**: the axes arm only reorders the same 9/10 values and adds an unrelated later table | **Survived 32 assertions**; wrong committed depth 8 still scores 4/4. |
| Read the scorecard from dirty disk instead of `<rev>` | **No discriminating landed arm**: the process suite deletes only the seat file; all scorecards visible there still mean 9/10 | **Survived 32 assertions**; dirty depth 9 hides committed depth 8, scores 4/4. |
| Label-only success fallback for nonexistent revisions | **No missing-object process world** in the landed suite | **Survived 32 assertions**; nonexistent 40-hex input scores 4/4. |

Full observed original self-test output (revision-pinned copy, identical source SHA above):

```text
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/original.py --self-test
      label-only: base rc=0 count=4 want rc!=0 count<4; look-alike rc=0 count=4 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
      honest/label-only: base rc=1 count=0 want rc!=0 count<4; look-alike rc=1 count=3 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
      fingerprint: base rc=1 count=0 want rc!=0 count<4; look-alike rc=0 count=4 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
      honest/fingerprint: base rc=1 count=0 want rc!=0 count<4; look-alike rc=1 count=3 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
      worktree-read: base rc=1 count=0 want rc!=0 count<4; look-alike rc=1 count=2 want rc!=0 count<4; target rc=1 count=3 want rc=0 count=4
      honest/worktree-read: base rc=1 count=0 want rc!=0 count<4; look-alike rc=1 count=3 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
      hardcoded-count: substituted-source rc=0 count=4 want rc!=0 count<4
self-test: 0 failure(s) over 32 assertions
exit=0
```

The unconditional source was the landed `LABEL_ONLY_SOURCE`, written to scratch and actually run against base, measured tip and nonexistent revision; each printed the full headline and exited 0. The base-aware extension was also actually run:

```text
landed _audit_counter(base-aware-label): base rc=1 count=0 want rc!=0 count<4; look-alike rc=0 count=4 want rc!=0 count<4; target rc=0 count=4 want rc=0 count=4
auditor_accepts=False
```

Replacing just the canned `LABEL_ONLY_SOURCE` with that extension and executing the entire suite retained `self-test: 0 failure(s) over 32 assertions`, exit 0, because the existing look-alike process arm successfully rejects it.

## 3. Surviving fingerprints / worktree provenance: exact mutations and counterexample

### M-A — measured-axis fingerprint

In `check_lowest_axis`, replace exactly:

```python
    scores, detail = _axis_scores(scorecard)
```

with:

```python
    scores, detail = {"depth": Decimal("9"), "consistency": Decimal("10")}, "hardcoded score fingerprint"
```

The blob-existence check remains, but its score/ownership content is no longer interpreted. All other logic, guards, canned candidates, and self-tests remain unchanged.

### M-W — dirty-worktree scorecard

In `check_lowest_axis`, replace exactly:

```python
    scorecard = show(root, rev, SCORECARD)
```

with:

```python
    scorecard = (root / SCORECARD).read_text(encoding="utf-8")
```

### Observed survival

Each full command produced the normal process diagnostics shown in §2 followed by the exact terminal lines below (diagnostics omitted here, not rerouted or suppressed during execution):

```text
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/hardcoded-axis.py --self-test
self-test: 0 failure(s) over 32 assertions
exit=0
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/worktree-scorecard.py --self-test
self-test: 0 failure(s) over 32 assertions
exit=0
```

### Strong counterexample, using the landed world's constructor

Constructed `/tmp/.../dishonest-world` with the original `_new_world`; committed an honest 4/4 target; then committed **only** a depth score change **9→8**, leaving the LOG statement `depth 9 < consistency 10` unchanged. Finally restored depth 9 **on disk without committing**. The original and both variants were invoked as fresh processes on the same bad committed revision. The base pin was substituted identically into all three sources, as in the landed process tests.

```text
world_base=999289ca16a522b62640a48b379182ade4b34b5a
world_target=e630e2d5529f87d4aee1f40ecc64fbadd466cb18
world_bad_axis=7308d1f2d709d54a19b90c5cad2c66d537a6482c

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/world-honest.py --root /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/dishonest-world --rev 7308d1f2d709d54a19b90c5cad2c66d537a6482c
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 975efae4 + 999289ca and base 35d44b4b
FAIL lowest-axis-corrected  computed owned minimum is depth at 8; expected depth 9 < consistency 10
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 3 of 4
exit=1

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/world-hardcoded-axis.py --root /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/dishonest-world --rev 7308d1f2d709d54a19b90c5cad2c66d537a6482c
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 975efae4 + 999289ca and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/world-worktree-scorecard.py --root /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/dishonest-world --rev 7308d1f2d709d54a19b90c5cad2c66d537a6482c
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 975efae4 + 999289ca and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0
```

**Impacted axes:** calibration/consistency (false provenance, measured-value fingerprint masquerading as computed score); discrimination depth. **Smallest safe correction:** the two source/provenance arms in §5, not another hardcoded score pin or a production exception.

## 4. Surviving nonexistent-revision label fallback

Insert immediately inside `run` before its original base-control code:

```python
    if show(root, rev, LOG) is None:
        print("r63 routed defects closed 4 of 4")
        return 0
```

This is a deliberately dishonest replacement, **not present in production**. It does not inspect fixture strings; the suite simply never calls a counter process on this input class.

Observed full-suite terminal lines, normal diagnostics omitted as in §3:

```text
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/missing-rev-label.py --self-test
self-test: 0 failure(s) over 32 assertions
exit=0
```

Observed fresh-process false certification:

```text
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/world-missing-rev-label.py --root /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev ffffffffffffffffffffffffffffffffffffffff
r63 routed defects closed 4 of 4
exit=0
```

The `world-` source uses the scratch control pin, but this branch returns before consulting that pin. The armed regression below demonstrates discrimination against the same fallback with the normal self-test's control substitutions.

**Impacted axis:** calibration. **Smallest safe correction:** one missing-object process-world assertion, §5. The existing argparse format check is not an object-existence self-test.

## 5. Exact missing arm text — exercised, not merely proposed

### A. Insert after the existing reordered-scorecard check, before `_write(root, LOG, _log_with_entry(base_log, short_line))` (landed lines 823–825)

```python
            honest_scorecard = _scorecard_text(reordered=True, move_table=True)
            _write(root, SCORECARD, honest_scorecard.replace(
                "| depth | 9 |", "| depth | 8 |", 1))
            stale_axis_rev = _commit(root, "changed score source, unchanged LOG")
            check("axes: committed score substitution rejects stale LOG",
                  check_lowest_axis(root, stale_axis_rev)[0], False)
            _write(root, SCORECARD, honest_scorecard)
            check("axes: dirty scorecard cannot repair committed score",
                  check_lowest_axis(root, stale_axis_rev)[0], False)
            _commit(root, "restore scorecard after provenance arms")

```

The first assertion kills the measured-axis fingerprint; the second kills the worktree reader even when its runtime values happen to equal the desired 9/10. Restoration is within the temporary constructed repository, preserving downstream world construction.

### B. Insert after the process-candidate loop, before the partial/green base-control arms (landed line 880)

```python
            missing_rev = "f" * 40
            check("revision: nonexistent object cannot certify",
                  _audit_counter(honest, root,
                                 [("missing-revision", missing_rev, False)])[0],
                  True)

```

`honest` here is the existing subprocess command for the counter under test, not a direct function call or a separately imported unmutated implementation.

### Exercised green/red evidence

Each command ran the complete suite with all existing process arms retained. Original process diagnostics were printed normally; below are its added FAIL lines and final tally/exit, not invented expected outputs:

```text
$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/armed-honest.py --self-test
self-test: 0 failure(s) over 35 assertions
exit=0

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/armed-hardcoded-axis.py --self-test
FAIL axes: committed score substitution rejects stale LOG: got True, expected False
FAIL axes: dirty scorecard cannot repair committed score: got True, expected False
self-test: 2 failure(s) over 35 assertions
exit=1

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/armed-worktree-scorecard.py --self-test
FAIL axes: dirty scorecard cannot repair committed score: got True, expected False
self-test: 1 failure(s) over 35 assertions
exit=1

$ /usr/bin/python3 -B /tmp/kotoba-r64-C2Dishonest-f9a8nm6t/armed-missing-rev-label.py --self-test
FAIL revision: nonexistent object cannot certify: got False, expected True
self-test: 1 failure(s) over 35 assertions
exit=1
```

This is a narrow correction to the evidence instrument, with no requested production counting-behavior change. [INFERENCE] If adopted after the measured tip, preserve the original 32-assertion receipts at their named revision and record the new source hash/count as a separate measurement; do not relabel historical receipts as 35. Canonical disposition remains with the judge/L1.
