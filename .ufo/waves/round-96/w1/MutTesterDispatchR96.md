# MutTesterDispatchR96 — mutation probe beyond the frozen C1 set (round 96, wave r96-w1)

Seat: MutTesterDispatchR96 (leaf; no subagent dispatch). Instrument under test:
`verifiers/verify_dispatch_prompts.py --self-test` (SKILL.md § Dispatch-prompt fidelity
checklist, boxes `dispatch.04` / `dispatch.08`).

- BASE: freeze commit `679775abb9277a7b8d17f060b0f5b4ced2b127b6`, instrument sha256
  `de9602710a67a3a54ca7ede0e64fcc8047410071b5df8f853e5cb401cc4adc2b`, honest self-test
  `0 failure(s) over 56 assertions`.
- CANDIDATE: freeze commit + `ExecArmsR96.patch` (sha256
  `799bbaac9485587900baeaee0291db2bc5beca97978ab773e2a2d5b770b73088`, named by
  `ExecArmsR96_READY`), built in this seat's scratch clone as commit
  `580290e9234d1f2d7672b5f3a37550efe269e9cb`, tree `198c2c8c6c9db5d4f58906f08c9b638dec04edef`,
  instrument sha256 `b5176411edb9b8b8552933e980e028e035640b8ff746af2acf005813c27eed7d`,
  honest self-test `0 failure(s) over 78 assertions`. The READY names the executor's own scratch
  rev `443430a6…`; the commit revs differ by metadata only — `git diff --binary <freeze> HEAD`
  in my clone reproduces the patch's `index 6e239ae..c6ecbd5` line and every hunk byte for byte
  (only the `a/ b/` vs `c/ i/` diff-format prefixes differ), and the patch is a single +128-line
  insertion inside `self_test()`.

## Method

The frozen counter's own machinery, imported read-only from
`verifiers/fixtures/round-96/selftest-kills.py` (`RUNNER`, `classify`, `code_decoy`,
`run_selftest`, `last_line`): every mutant is one literal single-anchor substitution (the anchor
must match exactly once), compiled with the instrument's path as filename and executed as
`__main__` with argv `[path, --self-test]` **while the file on disk holds the honest bytes**
(source-blind), 600 s timeout. Each mutant also gets the counter's comment decoy (`# r96-decoy`)
and code decoy (`if __name__ == "__decoy__":`) so no classification rests on the decoy
scaffolding. Classification is the counter's: KILLED = REPORTED-FAILURE (exit 1, last summary
`N failure(s) over M assertions` with N >= 1, at least one `self-test FAIL: ` line); RUN-ERROR =
anything else; SURVIVED = CLEAN. The instrument was restored byte-identical after every run
(`restored OK instrument sha256 …` in both receipts).

A second driver, `differ.py`, loads the honest and each mutated instrument as modules (no
subprocess), builds fixture trees under TMPDIR and calls the mutated function directly, so every
non-equivalent mutant has an exhibited input where honest and mutant disagree — a SURVIVED mutant
is a real behavioural difference the self-test does not observe, not a semantic no-op.

Drivers (this seat's receipts, not lane files): `probe.py`, `differ.py`.
Commands (`$S=/fast/scratch/hyaku/kotoba-r96/MutTesterDispatchR96`):

```
TMPDIR=$S/tmp HYAKU_SCRATCH=$S python3 -B …/probe.py base 679775abb9… "$S/repo"
TMPDIR=$S/tmp HYAKU_SCRATCH=$S python3 -B …/probe.py cand 580290e923… "$S/cand"
TMPDIR=$S/tmp HYAKU_SCRATCH=$S python3 -B …/differ.py     679775abb9… "$S/repo"
TMPDIR=$S/tmp HYAKU_SCRATCH=$S python3 -B …/differ.py     580290e923… "$S/cand"
```

## Mutant matrix — base vs candidate (19 mutants, all new; none of t01..t11/p00)

honest: base CLEAN 56 assertions, candidate CLEAN 78 assertions.
**Totals identical at both revisions: KILLED 3, RUN-ERROR 1, SURVIVED 15.** Every comment decoy
and every code decoy held at both revisions (19 of 19 each).

| id | class | base | cand | evidence (failing assertions at the candidate) |
|---|---|---|---|---|
| m01-rstrip-dot | sentence-final `.` kept in a report stem | SURVIVED | SURVIVED | — |
| m02-empty-baseline | empty baseline read as an unbounded bound | SURVIVED | SURVIVED | — |
| m03-fleetroot-stem-pass | fleet-root `report_stem_is_lane_id` reads PASS | SURVIVED | SURVIVED | — |
| m04-fleetroot-no-baseline | `.report-baseline` dropped from `lane_kind` | SURVIVED | SURVIVED | — |
| m05-placeholder-empty-angle | `<>` no longer a placeholder (`*`→`+`) | SURVIVED | SURVIVED | — |
| m06-sibling-file-as-lane | a *file* `<lane>-shokunin` counts as a lane repo (`is_dir`→`exists`) | SURVIVED | SURVIVED | — |
| m07-report-regex-noprefix | report dir without `round-` accepted | SURVIVED | SURVIVED | — |
| m08-role-regex-nospace | `round7` read as the role round (`\s+`→`\s*`) | SURVIVED | SURVIVED | — |
| m09-outofscope-reason | fleet-root out-of-scope reason text changed | SURVIVED | SURVIVED | equivalent (below) |
| m10-file-note-dropped | per-file `note` never attached | SURVIVED | SURVIVED | — |
| m11-evaluated-pass-only | `evaluated` counts PASS files only | **KILLED** (1) | **KILLED** (3) | `t05-finish-allna-pass: the all-N/A dispatch.08 still evaluates 1`, `t05…: the no-report-path dispatch.04 evaluates 1`, `an L1 file is in scope for dispatch.04` |
| m12-unreadable-as-baseline | unreadable baseline reads as an unbounded bound | SURVIVED | SURVIVED | — |
| m13-lane-kind-legacy-dropped | legacy `.round` no longer a lane identity | SURVIVED | SURVIVED | — |
| m14-finish-single-fail-na | one failing file reads N/A, not FAIL | SURVIVED | SURVIVED | — |
| m15-has-placeholder-redundant | second `has_placeholder` conjunct dropped | SURVIVED | SURVIVED | equivalent (below) |
| m16-dotdot-skip | `.`/`..` stem skip removed | SURVIVED | SURVIVED | equivalent (below) |
| m17-l1-in-08-scope | L1 files in scope for dispatch.08 | RUN-ERROR | RUN-ERROR | `TypeError: %d format: a real number is required, not NoneType` |
| m18-state-last-field | baseline read from the last field | **KILLED** (4) | **KILLED** (9) | e.g. `control: dispatch.08 verdict PASS`, `t04-le-to-lt: round equal … PASS`, `t10-nonint-baseline: … N/A` |
| m19-file-first-conjunct-only | only the first conjunct decides the file verdict | **KILLED** (8) | **KILLED** (11) | e.g. `wrong lane stem: dispatch.04 FAIL`, `unknown lane: dispatch.04 FAIL`, `missing state: dispatch.08 file verdict is not PASS` |

The candidate's new arms kill **none** of the 19 new mutants; the only verdict change from base to
candidate is the *strength* of three existing kills (m11 1→3, m18 4→9, m19 8→11 failing
assertions), i.e. the new arms add independent observation of `evaluated`, of the inclusive bound
and of the file-verdict precedence, but no new behaviour class.

## Equivalent mutants (named, with the reason)

- **m09-outofscope-reason** — no self-test assertion reads an out-of-scope `reason` string; the
  only assertion on `out_of_scope` is its length (`len(r08["out_of_scope"]) == 2`). Differential
  check: `out_of_scope[0]["reason"]` differs, **all verdicts and statuses identical**.
- **m15-has-placeholder-redundant** — the second `has_placeholder` sees
  `.ufo/reports/round-<digits>/<stem>`; the fixed prefix contains no `<`, `>` or `$`, so any
  placeholder/variable match in the full path lies entirely in the stem, which the first conjunct
  already tests. The conjunct is dead code. `report_paths` and `evaluate_dispatch_04` are
  **identical over a 16-text corpus** (sentence-final punctuation, `<>`, `$X`, `${X}`, `.`, `..`,
  `...`, multiple paths, absolute paths).
- **m16-dotdot-skip** — `stem` has already been `rstrip(".,;:")`-ed, so `"."` and `".."` both
  become `""` and are caught by `if not stem`; the tuple test is unreachable. Identical over the
  same corpus.

## Differential witnesses (every non-equivalent mutant is behaviourally distinct)

Receipts `differ-base.txt`, `differ-cand.txt`. Selected rows (honest → mutant):

| id | witness | honest | mutant |
|---|---|---|---|
| m01 | `report_paths("Write it at .ufo/reports/round-7/kote.md. Then stop.")` | `[(7,'kote')]` | `[(7,'kote.md.')]` |
| m02 | `state_source` on an empty `kote.report-baseline` | `('none', None, 'empty …')` | `('baseline', 10**9, 'empty …')` |
| m03 | fleet-root role, stem != lane: `report_stem_is_lane_id` | `N/A` | `PASS` |
| m04 | `lane_kind` with only `agg.report-baseline` | `fleet-root-role` | `unknown` |
| m05 | `has_placeholder("kote<>")` | `True` | `False` |
| m06 | `lane_kind` where `kote-shokunin` is a plain file | `fleet-root-role` | `sibling-lane` |
| m07 | `report_paths(".ufo/reports/7/kote.md")` | `[]` | `[(7,'kote')]` |
| m08 | `role_round("… round7 of up to 1024.")` | `None` | `7` |
| m10 | `file['note']` on a file with no report path | `'no report path found'` | absent |
| m11 | `evaluated` with one FAILing file | `1` | `0` |
| m12 | `state_source` on a mode-000 baseline | `('none', None, 'unreadable …')` | `('baseline', 10**9, 'unreadable …')` |
| m13 | `lane_kind` with only `agg.round` | `fleet-root-role` | `unknown` |
| m14 | check status with exactly one failing file | `FAIL` | `N/A` |
| m18 | `state_source("9 <64 zeros>")` | `('baseline', 9, …)` | `('baseline', 0, …)` |
| m19 | file verdict with a wrong report stem | `FAIL` | `PASS` |

## Findings

**F1 (coverage, main result).** The candidate's 22 new arms close the frozen eleven and nothing
else: 15 of 19 new mutants survive at the candidate exactly as at the base, 12 of them
behaviourally distinct (witnesses above). The new arms are per-survivor, not per-behaviour-class:
every arm is anchored on one frozen mutant's input shape, so the neighbouring edge of the same
function stays unobserved. This is a coverage finding about the *claim's scope*, not a defect in
the patch: the plan's C1 target is the eleven, and it is met.

**F2 (most serious survivors — the "never a pass" invariant).** `m02` and `m12` make a *missing*
state source read as a PASS bound (`10**9`), which contradicts the instrument's own docstring
("A missing state source is never a pass"). Both survive: no arm writes an empty or unreadable
`<lane>.report-baseline`. Minimal arm: write `state/kote.report-baseline` as `""` (and once as a
mode-000 file) and assert `round_le_latest_dispatched` is `N/A` and the file verdict is not PASS.

**F3 (headline verdict never asserted FAIL).** `m14` makes `_finish` report `N/A` for a check with
exactly one failing file and survives at both revisions: **no arm anywhere in the self-test
asserts a check-level `status == "FAIL"`** — arms assert file verdicts, conjunct statuses, and
check-level `N/A` (the new `t05`/`t10` arms) and `!= "PASS"`, never `== "FAIL"`. Minimal arm: a
prompts dir with one wrong-stem file, assert `evaluate_dispatch_04(...)["status"] == "FAIL"`.

**F4 (lane-identity scope).** `m03`, `m04`, `m06`, `m13` all survive: no arm builds a fleet-root
lane (state file only, no `<lane>-shokunin` repository), so the `N/A`-not-`PASS` rule for the
fleet-root stem, the `.report-baseline` identity arm, the legacy `.round` identity arm and the
`is_dir` (not `exists`) test on `<lane>-shokunin` are unobserved. `m06` is the sharpest: a plain
*file* named `<lane>-shokunin` would silently promote a lane to `sibling-lane`.

**F5 (extraction edges).** `m01`, `m05`, `m07`, `m08`, `m10` survive: sentence-final punctuation
on a report path, an empty `<>` placeholder, a report dir without the `round-` prefix, `round7`
with no space, and the per-file `note` are all unobserved. Each has a one-line witness above.

**F6 (RUN-ERROR, not a kill).** `m17` (L1 files in scope for dispatch.08) does not produce a
reported failure — it raises `TypeError: %d format: a real number is required, not NoneType` in
the `report dir round(s) %s != file name round %d` detail. Under the counter's rule such a mutant
is a RUN-ERROR and can never be a kill; any future arm aimed at that defect must first make the
`%d` path total, or it will read as a run error.

**F7 (dead code).** Three of the survivors are equivalent mutants (`m09`, `m15`, `m16`): the
second `has_placeholder` conjunct in `evaluate_dispatch_04` and the `.`/`..` stem skip in
`report_paths` are unreachable, and the out-of-scope `reason` text is unobserved. Not a defect,
but they are not worth arms.

## Context reading (not this seat's claim)

`python3 -B verifiers/fixtures/round-96/selftest-kills.py c1 580290e923… "$S/cand"` on exactly this
candidate tree reads `C1 targets killed 11 of 11 (run errors 0); positive killed 1 of 1; honest
CLEAN; comment decoys held 11 of 11; code decoys held 11 of 11` / `C1-PREDICATE-MET`
(receipt `counter-c1-cand.txt`). The eleven are killed; the fifteen above are outside the claim.

## Bounds and risks

- Every mutant is a single-line literal substitution; multi-line restructuring defects are out of
  scope, as are `box_proof()` internals (my item scopes the evaluation path:
  `evaluate_dispatch_04/08`, `report_paths`, `role_round`, `has_placeholder`, `lane_kind`,
  `state_source`, `_file_result`, `_finish`).
- Equivalence for `m09`/`m15`/`m16` is a static argument plus a 16-text differential corpus, not a
  proof over all inputs.
- The probe reuses the counter's `RUNNER`, so the counter's disclosed bound applies unchanged: a
  self-sniffer of its own compiled code objects that also proves the decoy guard dead is not
  caught. No mutant here is such a sniffer.
- Base and candidate readings use the same driver, same anchors and the same scratch layout, so
  the base→candidate delta is attributable to the patch alone.

## Files written

- `.ufo/waves/round-96/w1/MutTesterDispatchR96.md` (this report)
- `.ufo/waves/round-96/w1/MutTesterDispatchR96/probe.py`, `differ.py` (drivers)
- `.ufo/waves/round-96/w1/MutTesterDispatchR96/probe-base.txt`, `probe-cand.txt`,
  `differ-base.txt`, `differ-cand.txt`, `counter-c1-cand.txt`
- No lane file, no SKILL.md, no corpus file, no frozen instrument; no git/jj write in the lane.
- Tool installs: none needed.
