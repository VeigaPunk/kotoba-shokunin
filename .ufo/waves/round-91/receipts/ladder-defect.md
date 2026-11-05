# ExecLadder — C2 leg B: re-derivation of the freeze-gate exit-ladder defect

Seat: ExecLadder (executor). Scope: `verifiers/check_freeze_gate.py` at the freeze base
`9af1a7af2adf0ab07cfd53f92affc1ed8d992262`. Observed in a scratch clone only; the lane was not written.

## 1. The routed text

`.ufo/reports/round-90/kotoba.md` (fleet root, line 113): "an exit-ladder inconsistency in the
freeze-gate probe world (ReviewerRepairs, counter defect routed, not repaired into frozen bytes)".
Same text, carried: `corpus/lessons/round-90-verifier-spotcheck.md` routed defect 5, and
`corpus/lessons/round-90.md` (routed items list).

Search for the rung (committed evidence, all `grep -rn -i ladder` / `exit-ladder` / `probe world`):

- `.ufo/waves/round-90/w1/ReviewerRepairs/review.md` and `.ufo/waves/round-90/w1/ReviewerRepairs.md`
  do NOT name a ladder rung. The routed pointer under-specifies the defect.
- `.ufo/waves/round-90/w1/ReviewerBattery/review.md` item 5 (fg-m3, fg-m4) and
  `.ufo/waves/round-89/w1/MutTesterGates.md` F2 name mutant-coverage gaps (eval rung reached only by
  the self-test), not a counter defect.
- `plans/round-89-addendum-1.md` A2.4 names a duplicate-control-name doc drift (not an exit rung).

So the link between the routed phrase and the defect below is **[INFERENCE]**: it is the only
exit-code contradiction between the gate's docstring and its observed behaviour that I could
re-derive from committed evidence (Step 1a). It is re-derived from the bytes, not from the pointer.

## 2. Rung enumeration (Step 1a)

Docstring ladder (`check_freeze_gate.py` lines 20–25): 0 held; 1 refused; 2 could-not-evaluate
("a declared command missing/not executable/timeout, or the plan file unreadable"); 3 invalid spec.

Each row: command run from the scratch clone at base bytes (`receipts` copy:
`.ufo/waves/round-91/w1/ExecLadder/rung-probe-base.txt`; patched bytes: `rung-probe-patched.txt`).
Probe script: `.ufo/waves/round-91/w1/ExecLadder/rung-probe.sh`.

| rung / path | command (abridged) | base exit | patched exit | first output line (base) | docstring line | verdict |
|---|---|---|---|---|---|---|
| 0 self-test | `--self-test` | 0 | 0 | `0 failure(s) over 30 assertions` | 13–14 | consistent |
| 0 held | `--plan r88-controls-fixed.md` | 0 | 0 | `freeze gate: 4 control(s) held — freeze may proceed` | 17–18 | consistent |
| 1 refused | `--plan r88-controls.md` | 1 | 1 | `REFUSED control w_added_red (line 36): …` | 16, 20 | consistent |
| 2 plan missing | `--plan probes/none.md` | 2 | 2 | `COULD-NOT-EVALUATE: cannot read plan …` | 22 | consistent |
| 2 plan is a directory | `--plan probes/adir.md` | 2 | 2 | `COULD-NOT-EVALUATE: cannot read plan … Is a directory` | 22 | consistent |
| **2 plan not UTF-8** | `--plan probes/nonutf8.md` (byte `\xff` in body) | **1** | **2** | base: stdout empty; stderr `UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff` (Python traceback) | 22 ("the plan file unreadable") | **INCONSISTENT at base → repaired** |
| 2 control timeout | `--plan slow.md --timeout 1` | 2 | 2 | `COULD-NOT-EVALUATE control slow (line 2): timeout after 1s` | 22, 47 | consistent |
| 2 control rc 126 | `--plan notexec.md` | 2 | 2 | `COULD-NOT-EVALUATE control np (line 2): command not executable (rc=126)` | 22, 47 | consistent |
| 2 control rc 127 | `--plan nx127.md` (declares `exit 127`) | 2 | 2 | `COULD-NOT-EVALUATE control nx (line 2): command not found (rc=127)` | 22, 47 | consistent (a declaration cannot pin 127; see finding F2) |
| 3 no Controls block | `--plan noblock.md` | 3 | 3 | `INVALID SPEC: no ## Controls block found` | 23–25 | consistent |
| 3 empty block | `--plan emptyblock.md` | 3 | 3 | `INVALID SPEC: empty ## Controls block` | 23–25 | consistent |
| 3 control without command | `--plan nocmd.md` | 3 | 3 | `INVALID SPEC: control nocmd (line 2): no command` | 23–25 | consistent |
| 3 unrecognized clause | `--plan bogusclause.md` | 3 | 3 | `INVALID SPEC: control a (line 3): unrecognized expect clause 'bogus'` | 23–25 | consistent |
| 3 argparse usage (both modes) | `--self-test --plan x` | 3 | 3 | `INVALID SPEC: --self-test and --plan are mutually exclusive` (stderr) | none (`_Parser` comment, line 298–299) | consistent |
| 3 argparse usage (no mode) | `(no args)` | 3 | 3 | `INVALID SPEC: one of --self-test or --plan is required` | none (`_Parser` comment) | consistent |
| 3 argparse usage (bad float) | `--plan x --timeout abc` | 3 | 3 | `INVALID SPEC: argument --timeout: invalid float value: 'abc'` | none (`_Parser` comment) | consistent |
| 1 control rc != declared | `exit 2` observed, `expect: exit 0` | 1 | 1 | `REFUSED control two (line 2): … observed exit=2` | 47–50 (`exits nonzero is OBSERVED`) | consistent with the docstring text |
| 0 control rc == declared 2 | `exit 2` observed, `expect: exit 2` | 0 | 0 | `freeze gate: 1 control(s) held` | 47–50 | consistent with the docstring text |
| 1 control killed by signal | `kill -9 $$`, `expect: exit 0` | 1 | 1 | `REFUSED control sig … observed exit=-9` | 47–50 | not contradicted by text; see finding F3 |
| 0 duplicate control names | two `control same` entries, both pass | 0 | 0 | `freeze gate: 2 control(s) held` | none | see finding F1 |
| 1 work root under a file | `--work probes/afile/sub` | **1** | **1** | base: stderr `NotADirectoryError` (traceback) | not named in the ladder | second uncaught path; see finding F4 (not repaired) |

Counts: 25 rung probes; 1 contradicts the docstring ladder (the not-UTF-8 plan), 1 further uncaught
path outside the ladder text (work root, F4).

## 3. Verdict (Step 1a) — **REPAIRABLE**

**Exact defect.** `verifiers/check_freeze_gate.py`, base line 258–263, `run_gate`:

```
258    try:
259        text = plan_path.read_text(encoding="utf-8")
260    except OSError as exc:          # <- UnicodeDecodeError (a ValueError / UnicodeError) is not OSError
        print("COULD-NOT-EVALUATE: cannot read plan %s: %s" % (plan_path, exc),
              file=out)
263        return EXIT_EVAL
```

The read fails on an undecodable plan with `UnicodeDecodeError`, which is not an `OSError`; it escapes
`run_gate`, `main`, and the module, and CPython exits 1. Rung 1 is "refused", so the gate reports a
refusal of the plan's content when the docstring (line 22) assigns an unreadable plan file to rung 2.
A caller that branches on the exit code (the freeze routine) reads a refusal where the ladder says
could-not-evaluate. Declared expectation (docstring line 22): 2. Observed at base: 1 (traceback).

**Repair (Step 2, applied in the scratch clone; patch `.ufo/waves/round-91/w1/ExecLadder/ExecLadder.patch`).**
- line 260: `except OSError as exc:` → `except (OSError, UnicodeError) as exc:` (the one touched line).
- one new self-test arm `arm plan-not-utf8 could-not-evaluate` (`arm_plan_not_utf8`, inserted after
  `arm_plan_missing`, lines 365–369), listed in `ARMS` after `arm plan-missing could-not-evaluate`.
  The arm writes a non-UTF-8 plan and asserts `rc == EXIT_EVAL` and `cannot read plan`.
- Self-test count: 30 → 31 (`N' > 30`).

**Coupling (must be landed with it — not in my patch).** `arm_floor_row` asserts
`floors-registry.json` `freeze_gate.floor == len(ARMS)`. With the new arm the self-test reads
`FAIL arm floors-row freeze_gate … freeze_gate floor 30 != self-test assertion count 31` and exits 1.
The row is owned by ExecFloorsCap (floors_guard row only); I did not edit it in the patch. The L1
must bump `freeze_gate` 30 → 31 in the same landing, in `verifiers/floors-registry.json` (line 26) and
in the guard's two in-file tables `verifiers/check_assertion_floors.py` (line 200 `"freeze_gate": 30`
and line 280 `"freeze_gate": ("verifiers/check_freeze_gate.py", 30, …`) under the BUMP-IN-STEP rule.
Verified in scratch only: with `floors-registry.json` line 26 set to 31 the self-test reads
`0 failure(s) over 31 assertions`, exit 0 (see §4).

## 4. Able-to-fail and anchors (Step 2 c and battery)

- Revert world (`repo-revert`): patched file with line 260 restored to `except OSError as exc:`, all
  else unchanged, floor 31 in the scratch registry:
  `FAIL arm plan-not-utf8 could-not-evaluate: unexpected UnicodeDecodeError('utf-8', b'## Controls\n…\xff\xfe\n', 68, 69, 'invalid start byte')`,
  `1 failure(s) over 31 assertions`, exit 1. Receipt: `.ufo/waves/round-91/w1/ExecLadder/able-to-fail.txt`.
- Patched file, floor 31: `0 failure(s) over 31 assertions`, exit 0. Receipt: `selftest-patched-scratch-floor31.txt`.
- Battery anchors (the eight `fg-*` rows that target this file, read from `verifiers/fixtures/mutation-battery/manifest.tsv`),
  each checked with `re.findall(anchor, final_bytes)` on the patched file:
  `fg-m1 1`, `fg-m1b 1`, `fg-m2 1`, `fg-m2b 1`, `fg-m3 1`, `fg-m3b 1`, `fg-m4 1`, `fg-x1 1` — every
  anchor matches exactly once. None of the touched lines (line 260; the inserted arm; the `ARMS` row)
  is inside any anchor. The manifest was not edited.

## 5. Findings (not repaired; routed to L1)

- **F1 (duplicate control names).** Two controls with the same name both run; the plan reads
  `freeze gate: 2 control(s) held`, exit 0 (rung 0). Addendum A2.4 says "the docstring is corrected at the
  freeze commit"; the file carries no duplicate-name sentence at all (`grep -in dup check_freeze_gate.py` is
  empty). The doc-truth claim in A2.4 is not realised in the frozen bytes. No arm pins it. Not a rung
  contradiction on the docstring as written; not repaired (frozen predicate; addendum deferred it).
- **F2 (declared 127 unpinnable).** A control that declares `expect: exit 127` is never compared: rc 126/127
  is read as could-not-evaluate (rung 2) before the declaration is checked. Consistent with the docstring
  text (line 47), recorded as a bound.
- **F3 (signal-killed control).** `kill -9 $$` reads `observed exit=-9` and refuses (rung 1). The docstring
  (lines 47–50) says a control that "runs and exits nonzero" is observed; a signal kill is arguably
  could-not-evaluate. A judgement, not a contradiction of the printed text; not repaired.
- **F4 (uncaught work-root failure).** `--work` under a regular file (`os.makedirs` in `run_control`,
  line 219) raises `NotADirectoryError` uncaught: exit 1, traceback. The docstring ladder does not list
  it; by the rung-2 spirit ("could-not-evaluate") it would be 2. Left for the L1: a second repair would
  widen the change beyond the routed pointer. Recorded for round 92.
- **F5 (BOM).** A plan with a UTF-8 BOM before `## Controls` reads `INVALID SPEC: no ## Controls block`
  (rung 3). Consistent with the grammar; noted for the record.

## 6. Honest status

- Verdict REPAIRABLE rests on a re-derived contradiction (docstring line 22 vs base bytes), not on the
  routed pointer's wording. If the L1 reads "probe world" as the battery's `fg-*` probes only, the routed
  defect is not the one repaired here, and the leg should narrow to `unprovable` per plan leg B(a).
- The self-test count moves 30 → 31 only together with the `freeze_gate` floor bump (§3 Coupling). Without
  that bump the patched gate's own self-test is red (exit 1). The patch alone is therefore not landable
  under the current registry; the L1 must land the floor bump with it.
