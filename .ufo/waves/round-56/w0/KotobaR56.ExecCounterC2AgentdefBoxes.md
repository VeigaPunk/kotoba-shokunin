# KotobaR56.ExecCounterC2AgentdefBoxes — round-56 C2 counter (agent-definition boxes)

Counter (scratch, NOT in the lane; the L1 integrates it): `/fast/scratch/hyaku/kotoba-r56/KotobaR56.ExecCounterC2AgentdefBoxes/check_agentdef_boxes.py`
sha256 `8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe` · 1652 lines · intended lane path `verifiers/check_agentdef_boxes.py`.
Frozen predicate (docstring): `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>` exits 0 iff it prints
`agent-definition boxes executed and discriminating N of T` with N ≥ 3. Receipt label `C2 predicate: exit 0 (N>=3)`.

## Receipts (raw output in `<seat>/receipts/`)
`--self-test`: **exit 0** · `self-test: 0 failure(s) over 109 assertions`
`--rev b0b7140b` (cwd = lane clone at base): **exit 1**
```
agent-definition boxes executed and discriminating 0 of 9
  agentdef.01/02/05/06/07: not counted (disposition is unexecuted, not delegated)
  agentdef.03/04/08/09: not counted (no case generator for this box ...)
seed: 3d9637f65404752212bdefadf1aaa66b
```
`--rev deadbeef`: **exit 2** · `cannot evaluate: ... 'show' ... exit status 128`

## Discrimination evidence
- Independent instrument written from the docstring alone (`indep/verify_agentdef.py`): first run **3 of 9** — it hid the
  absent-`name:` clause and never parsed `subagents:`; fixing only those two bugs gives **5 of 9, exit 0**, stable over
  20 seeds. The reading is implementable exactly as stated.
- Partial instrument (.05/.06 only): **2 of 9, exit 1** — the N≥3 threshold is not free.
- size-keyed and word-keyed delegates: **0 of 9, exit 1**. `--self-test` controls, each **0 of 9, exit 1**: constant-PASS,
  constant-FAIL, no-reader, junk (non-JSON), id-keyed, exit-remap (prints FAIL but exits 2), name-keyed.
- Round-55 classes closed: remap (exit must be 0/1 *and* match), entry-preflight (the delegate never sees git; any other
  exit ⇒ not counted), argparse shadow (condition (c) plus the counter scrubbing its own dir from sys.path — planted
  both under `verifiers/` and beside the counter).

## Rules the spec left open (my choice)
1. BASE_REV shas pinned as constants from `git show b0b7140b:...checklist-baseline.json`, so `--self-test` is hermetic;
   a box_id with no pin cannot count.
2. The delegated path must be a **blob at exactly that path** (`git ls-tree`); a directory or absent path ⇒ not counted.
3. One reason per box, in spec order: (a) disposition/path → (b) reworded sha → (c) stdlib shadow → (d) cases;
   no-generator boxes say so first, since they can never count.
4. Shadow scan is recursive `verifiers/**/*.py` with stem in `sys.stdlib_module_names`; the archive is `verifiers/` plus
   the delegated path when outside it, because the rev tree's absolute `.ufo/` symlinks defeat safe extraction.
5. `.01`: absent `name:` is a defect only when ≥1 sibling exists and **every** sibling declares `name:`. No lone
   absent-name case is generated, so the stricter "absent always fails" reading gives the same verdict on every case.
6. `.02`: identity = declared `name:` else stem; enrolled = keys of the top-level `agent` object; `subagents:` entries
   are identifiers; reachability = least fixed point. Cases set `name == stem`, so both readings coincide.
7. `.05`: markers = ISO `YYYY-MM-DD` (covers timestamps), month-name date, round index (`round 12`/`round-12`/`round
   #12`) or `PROPOSE round`; **frontmatter only**; `3.12` is not a date; live seat assignments are a stated non-goal.
8. `.06`: markers = `your current task`, round index, one-shot phrases (`one-shot`, `once only`, `only this once`,
   `for this task only`, `this time only`, `just this once`); **body only**; bare `task` is not a defect.
9. `.07`: paragraph = maximal run of non-blank lines, whitespace-collapsed; duplication counts only at ≥40 normalised
   characters (so `- yes`/`---` are not blocks); same-named ATX sections with different content conflict.
10. Twins: 4–5 pairs per box; twins share the case-dir base name **and** the file names (only the random parent differs)
    with sizes within 1.5×, so a name-keyed delegate is wrong by construction, not by luck.
11. Seed = `secrets.token_hex(16)`, printed last; stems/names/words/dates/timestamps/versions/rounds derive from
    `random.Random(seed)`; no `--seed` flag and the seed never enters the delegate's argv/env.
12. Delegate run = `sys.executable -B -P`, fresh empty cwd, env minus PYTHONPATH/PYTHONHOME/PYTHONSTARTUP plus
    PYTHONSAFEPATH=1, 20 s per case, 240 s total budget (inside the 300 s cap).
13. The delegate's JSON `exit_code` field is not required, only the exit code and the `{id, status}` entry; `--repo`
    defaults to the parent of the script's `verifiers/` dir; exit 2 on git failure/unknown rev/unreadable map.

## State
No lane writes except this report; no tool installs (python3 3.14 stdlib + git 2.56). All git calls read-only with
`GIT_OPTIONAL_LOCKS=0`; sandbox work, clone and receipts under the seat directory. Residual limit: a delegate keyed on
the *full* target path (random-hex parent included) is chance per case, ≤2⁻²⁴ to reach N≥3; names/sizes/ids/labels cannot.
