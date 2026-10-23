Result: DONE — a redesigned agent-definition counter (seeded case shuffle, one isolated directory + HOME + TMPDIR + cwd per case, and 60 machine-checked hard negatives) scores **0 of 9** for both withdrawn round-56 controls on every seed I ran, while the reference delegate still scores 5 of 9; the counter file is delivered in this seat's scratch dir and nothing in the lane was edited.

# Scope

Seat `KotobaR56.C2RedesignCounter`. Assignment: a redesign of `verifiers/check_agentdef_boxes.py` that the two pre-data controls cannot meet — shuffled case order per seed, one fresh isolated directory (and HOME, TMPDIR, cwd) per case with no visible sibling state, and one hard-negative case per heuristic class per box. C2 is withdrawn this round (erratum 1, `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8`); this file is **redesign input for a later round only**. No claim, no admission, no measurement of round-56 content, no counter in the lane changed, no dispositions changed, no delegate shipped.

Deliverable (outside the lane, by assignment):

| Item | Value |
|---|---|
| Path | `/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter/verifiers/check_agentdef_boxes_v2.py` |
| sha256 | `5dbee46380651e98cfbc755962006f08f0e6990c82c4221ca94bdac59d531f4e` |
| Size / lines | 110 556 B / 2461 lines |
| Sandbox clone | `/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter` (clone of the lane, checked out at `e02f5f5d`) |
| Lane writes | this report only |

The frozen counter's bytes are unchanged and were the baseline in every run: `sha256sum verifiers/check_agentdef_boxes.py`
printed `8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe` in the lane working tree and in the sandbox clone (command output in §5), the same
digest both control reports record.

# 1. What the redesign changes (three changes, nothing else)

Everything else — the measured quantities (T, N, conditions a–d), the operational reading of `agentdef.01/.02/.05/.06/.07`, the instrument contract, the output format and the frozen predicate — is the frozen counter's, unchanged.

**1.1 Shuffled case order per seed.** `build_cases` now shuffles each box's case list with the run's seeded `random.Random` (`verifiers/check_agentdef_boxes_v2.py:1196-1204`, the shuffle at `:1202`). The order is a function of the seed alone and is printed nowhere; a fixed PASS/FAIL schedule keyed on the case index can no longer be right.

**1.2 One fresh isolated directory (and HOME, TMPDIR, cwd) per case.** `materialise_case` (`:1328`) builds, under a per-box run root, a fresh case root holding `tree/` (a private copy of the extracted revision tree, `:1339`), `target/`, `home/`, `tmp/` and `run/`. `delegate_env` (`:1357`) points HOME, TMPDIR and all four XDG directories at that case's `home/`/`tmp/`; the delegate runs with cwd `<case root>/run`. The case root is deleted immediately after the case (`evaluate`, `:1573-1590`), so the run root holds exactly one entry at every moment and no sibling case is visible. The private tree copy also means a delegate that writes state next to itself starts each case clean.

**1.3 Hard-negative families.** Every box carries, besides its twin pairs, 8–10 solo hard-negative cases (`hn-…`, 16 distinct shapes, `verifiers/check_agentdef_boxes_v2.py:355-388` for the building blocks). The twelve heuristic classes of the two withdrawn controls are transcribed verbatim as source text (`HEURISTIC_RULES_SOURCE`, `:1217`) and the self-test asserts, for **every one of the 12 classes × 5 boxes = 60 pairs**, that at least one generated case is answered wrongly by that class (§2.2). The self-test's shortcut fixtures run *that same source*, so the matrix and the fixtures cannot drift apart.

# 2. Self-test

Command (cwd = sandbox clone), exit 0, 24.2 s wall:

```text
timeout 900 python3 -B verifiers/check_agentdef_boxes_v2.py --self-test
self-test: 0 failure(s) over 184 assertions
exit 0
```

Full output: `redesign-receipts/self-test.txt` in the sandbox clone.

## 2.1 What the 184 assertions cover

- generator rules: ≥4 PASS and ≥4 FAIL cases per box; every grouped case paired with its twin (one PASS, one FAIL, same file names, size ratio ≤ 1.5); solo hard negatives ungrouped;
- the 60-pair hard-negative coverage matrix (§2.2);
- shuffle: two seeds give different orders for every box; the first case of every box varies over 12 seeds (≥3 distinct labels each);
- per-case isolation census (§2.3);
- the reference delegate scores 5 of 9 and every generated box counts;
- 11 shortcut fixtures each exit 1 and print 0 of 9;
- reworded box, absolute delegated path, `..` path, stdlib shadow under `verifiers/`, and a stdlib shadow beside the counter itself behave as the frozen counter's self-test requires.

## 2.2 Hard-negative coverage matrix (printed by `--self-test`)

Twelve classes × five boxes, witness case named per cell, zero missing (the witness choice depends on the seed because the list is shuffled):

```text
more_than_one_file: agentdef.01=hn-roster-substring-config-mentions-stem; agentdef.02=f5-roster-without-agent-map; agentdef.05=f1-description-with-date; agentdef.06=f4-task-word-plus-current-task; agentdef.07=f4-third-section-repeats-first
name_differs_from_any_stem: agentdef.01=f2-sibling-roster-consistent; agentdef.02=f5-roster-without-agent-map; agentdef.05=f1-description-with-date; agentdef.06=f4-task-word-plus-current-task; agentdef.07=f4-third-section-repeats-first
name_not_in_any_stem: agentdef.01=f2-absent-name-with-declaring-sibling; agentdef.02=f2-parent-names-no-subagent; agentdef.05=f1-description-with-date; agentdef.06=f4-task-word-plus-current-task; agentdef.07=f4-third-section-repeats-first
flat_name_count_and_membership: agentdef.01=hn-name-swapped-across-stems; agentdef.02=f2-parent-names-no-subagent; agentdef.05=f1-description-with-date; agentdef.06=f4-task-word-plus-current-task; agentdef.07=f4-third-section-repeats-first
stem_absent_from_config: agentdef.01=f1-name-matches-stem; agentdef.02=f2-child-reached-via-subagents; agentdef.05=hn-repeated-lines-short; agentdef.06=f2-handover-cadence; agentdef.07=hn-same-heading-equal-content
any_roster_bypasses_missing_stem: agentdef.01=f1-name-matches-stem; agentdef.02=hn-roster-substring-unrelated-roster; agentdef.05=hn-repeated-lines-short; agentdef.06=f2-handover-cadence; agentdef.07=hn-same-heading-equal-content
digits_anywhere: agentdef.01=hn-roster-substring-config-mentions-stem; agentdef.02=hn-digits-anywhere-body-date; agentdef.05=f4-date-in-body-only; agentdef.06=hn-first-five-lines-front-num; agentdef.07=f4-third-section-repeats-first
first_five_lines_digits: agentdef.01=hn-roster-substring-config-mentions-stem; agentdef.02=f2-parent-names-no-subagent; agentdef.05=hn-date-below-fifth-frontmatter-line; agentdef.06=hn-first-five-lines-front-num; agentdef.07=f4-third-section-repeats-first
repeated_lines: agentdef.01=f1-name-matches-stem; agentdef.02=hn-digits-anywhere-body-date; agentdef.05=hn-repeated-lines-short; agentdef.06=f2-handover-cadence; agentdef.07=hn-same-heading-equal-content
task_round_anywhere: agentdef.01=hn-task-round-words; agentdef.02=f2-parent-names-no-subagent; agentdef.05=f1-description-with-date; agentdef.06=hn-task-round-words; agentdef.07=f4-third-section-repeats-first
current_task_round_one_shot: agentdef.01=hn-task-round-words; agentdef.02=f2-parent-names-no-subagent; agentdef.05=f1-description-with-date; agentdef.06=hn-task-round-words; agentdef.07=f4-third-section-repeats-first
paragraph_leads: agentdef.01=hn-paragraph-leads-shared; agentdef.02=f2-parent-names-no-subagent; agentdef.05=f1-description-with-date; agentdef.06=f4-task-word-plus-current-task; agentdef.07=hn-same-heading-equal-content
```

The dedicated `hn-` families also kill their intended class on their own (checked separately, exit 0, no failures): `hn-digits-anywhere-body-date`, `hn-first-five-lines-front-num`, `hn-date-below-fifth-frontmatter-line`, `hn-repeated-lines-short`, `hn-repeated-lines-long-body`, `hn-paragraph-leads-shared`, `hn-same-heading-equal-content`, `hn-task-round-words`, `hn-front-round-word`, `hn-current-task-in-frontmatter`, `hn-one-shot-in-frontmatter`, `hn-roster-substring-theme-only`, `hn-roster-substring-unrelated-roster`, `hn-roster-substring-config-mentions-stem`, `hn-name-swapped-across-stems`, `hn-name-differs-from-any-stem-two-files`.

## 2.3 Isolation census (printed by `--self-test`)

The census fixture reports the shape it sees, once for the first case of `agentdef.01` and once for the last:

```text
isolation census: [{"cwd_entries": 0, "cwd_parent_entries": 5, "home_entries": 0, "root_name": "7a5918f243339d83", "run_root_entries": 1, "target_name": "g2", "target_parent_entries": 5, "tmp_entries": 0}, {"cwd_entries": 0, "cwd_parent_entries": 5, "home_entries": 0, "root_name": "5583e22ab0612029", "run_root_entries": 1, "target_name": "g1", "target_parent_entries": 5, "tmp_entries": 0}]
```

`run_root_entries == 1` in both probes is the "no visible sibling case" measurement; `target_parent_entries == 5` is constant (tree, home, tmp, run, target); cwd, HOME and TMPDIR are empty; the case root name is random per case.

## 2.4 Red arm — the matrix has teeth

A mutated copy (`redarm/check_agentdef_boxes_v2.py`, scratch only) drops every `hn-` case of `agentdef.07`. Self-test output, exit 1:

```text
  paragraph_leads: ... ; agentdef.07=MISSING
self-test: 2 failure(s) over 184 assertions
FAILED paragraph_leads: agentdef.07 has a witness case: no generated case of agentdef.07 is answered wrongly by paragraph_leads
FAILED heuristic-tuned: 0 of 9: agent-definition boxes executed and discriminating 1 of 9
```

The second failure is the substantive one: with `agentdef.07`'s hard negatives gone, the tuned heuristic control counts that box (1 of 9). Receiver: `redesign-receipts/redarm.txt`.

## 2.5 Satisfiability and cost

- reference delegate, worst case (every case of every box runs): `agent-definition boxes executed and discriminating 5 of 9`, exit 0, **10.9 s** for 90 cases on this host. Case tallies: `agentdef.01 17/17, .02 18/18, .05 20/20, .06 18/18, .07 17/17`.
- the same reference delegate on three fixed seeds: 5 of 9, exit 0 each time, with three different case orders (`redesign-receipts/reference-seeds.txt`).
- `TOTAL_BUDGET` stays 240 s and the per-case timeout stays 20 s, unchanged from the frozen counter; the per-case tree copy costs 17 ms on the extracted tree of this revision (407 entries, 1 623 390 B of blobs at `e02f5f5`).

# 3. The two control delegates, rebuilt and scored under the redesign

Method: each control world was reconstructed **inside the sandbox clone only** by extracting the delegate file (`verifiers/control_heuristic.py` + `verifiers/control_mode.json`, or `verifiers/control_generator_keyed.py`) and the world's `verifiers/checklist-baseline.json` from the control sandbox commit named in the control report, committing it in the clone, and running both counters against that commit with `--repo <clone>`. The frozen counter run is the baseline check that the world is a faithful reconstruction.

## 3.1 World table (all 11 worlds, exact exit codes)

`Frozen` = `python3 -B verifiers/check_agentdef_boxes.py --rev <rev>` (the frozen predicate, unchanged bytes); `Redesign` = `python3 -B verifiers/check_agentdef_boxes_v2.py --rev <rev>`. Receipt: `redesign-receipts/scores.tsv`.

| World (control) | Sandbox commit in the clone | Frozen N / exit | Redesign N / exit |
|---|---|---|---|
| naive-multifile @`9d714be` | `ee5e391c5ff9` | 0/9, 1 | **0/9, 1** |
| naive-any-stem-difference @`f5781a4` | `fdc66200bed9` | 0/9, 1 | **0/9, 1** |
| naive-stem-membership @`7b3fdd0` | `86c68c18fc31` | 0/9, 1 | **0/9, 1** |
| tuned-identity-only @`2df8ab3` | `91f4c0bfbf4e` | 1/9, 1 | **0/9, 1** |
| tuned-identity-and-roster @`ef55fd0` | `70f9efe467c5` | 2/9, 1 | **0/9, 1** |
| tuned-three-boxes @`5a29592` | `e984e01a9ab8` | 3/9, 0 | **0/9, 1** |
| tuned-all-five @`6df3156` | `2d32d968b566` | 4/9, 0 | **0/9, 1** |
| **tuned-all-five-refined @`40c2b5e`** | `f730349ef30c` | **5/9, 0** | **0/9, 1** |
| generator-keyed-pristine @`5cf91c7` | `4abd449f1faf` | 0/9, 1 | **0/9, 1** |
| **generator-keyed-mutant @`41c2f48`** | `8d919f03f332` | **5/9, 0** | **0/9, 1** |
| generator-keyed-restored @`7ea209c` | `411a54045731` | 0/9, 1 | **0/9, 1** |

Every frozen baseline reproduces the N recorded in the two control reports (`CtlC2Heuristics.md` table and `CtlC2GeneratorKeyed.md` world list) exactly, including the 0/9 do-nothing and restored worlds. Under the redesign every world is 0 of 9 → exit 1 → `C2 predicate: exit 0 (N>=3)` **NOT MET**.

Delegate bytes prove the rebuild is the control, not a look-alike:

| World | sha256 of the delegate in the measured commit | Matches |
|---|---|---|
| refined `f730349` | `5fd223d4921e03efa57b96396b44b17237622dc085a5692db385271d2473d9d5` | `CtlC2Heuristics` @`40c2b5e` (same hash) |
| mutant `8d919f0` | `23f6b6b464b1d168b1067e4cde745399ecf2ab756beccb17e0c85cf4d5fca7ef` | `CtlC2GeneratorKeyed.md` "mutant (W2)" |
| pristine `4abd449` | `0c8c6727ca8ca242129f4152ec4b591c2af65df97f7a7792789a0f93ae9eed84` | `CtlC2GeneratorKeyed.md` "before (W1) / after (W3)" |

The refined world's mode file is the control's own profile (`{"agentdef.01":"flat_name_count_and_membership","agentdef.02":"any_roster_bypasses_missing_stem","agentdef.05":"five_line_numeric_or_propose","agentdef.06":"current_task_or_round_or_one_shot_anywhere","agentdef.07":"paragraph_lead_or_heading_repeated"}`).

## 3.2 Seed stability (each control run three times with a fresh seed)

`timeout 300 env TMPDIR=<scratch>/.probe-tmp python3 -B verifiers/check_agentdef_boxes_v2.py --rev <rev> --repo <clone>`

| Control | Seeds | Result per run | Exit |
|---|---|---|---|
| tuned-all-five-refined | `436167672befbc389d70760fd5c9e561`, `146c389c2484fc55c531167319acae87`, `facb9745fdd6f003658e7d447f55f843` | 0 of 9, 0 of 9, 0 of 9 | 1, 1, 1 |
| generator-keyed-mutant | `f6625ab20ae67f3a95c886e3c9453ee6`, `b59b4f4ec58f2c6953b2d6439aa940b7`, `3e443b2e63b83126ffb0808335f08978` | 0 of 9, 0 of 9, 0 of 9 | 1, 1, 1 |

The generator-keyed control was seed-stable at 5 of 9 on 10 independent seeds (`CtlC2GeneratorKeyed.md`) and the heuristics control at 5 of 9 on 3 seeds (`CtlC2Heuristics.md`); the redesign is 0 of 9 on the six seeds above and on the single seed drawn by each of the 11 world-capture runs.

## 3.3 Which hard negative killed which control

tuned-all-five-refined (`redesign-receipts/tuned-all-five-refined.redesign.txt`), seed `791ac258ca7c5368f3925134de5c2681`:

```text
agent-definition boxes executed and discriminating 0 of 9
  agentdef.01: not counted (1 of 17 cases wrong: hn-name-swapped-across-stems expected FAIL, saw exit 0, status PASS)
  agentdef.02: not counted (2 of 18 cases wrong: hn-roster-substring-theme-only expected FAIL, saw exit 0, status PASS; hn-roster-substring-unrelated-roster expected FAIL, saw exit 0, status PASS)
  agentdef.05: not counted (2 of 20 cases wrong: hn-date-below-fifth-frontmatter-line expected FAIL, saw exit 0, status PASS; hn-first-five-lines-front-num expected PASS, saw exit 1, status FAIL)
  agentdef.06: not counted (4 of 7 cases wrong: hn-one-shot-in-frontmatter expected PASS, saw exit 1, status FAIL; hn-front-round-word expected PASS, saw exit 1, status FAIL; hn-current-task-in-frontmatter expected PASS, saw exit 1, status FAIL; hn-task-round-words expected PASS, saw exit 1, status FAIL)
  agentdef.07: not counted (2 of 17 cases wrong: hn-same-heading-equal-content expected PASS, saw exit 1, status FAIL; hn-paragraph-leads-shared expected PASS, saw exit 1, status FAIL)
```

These include the semantic witnesses the heuristics control report listed as its smallest safe correction (`CtlC2Heuristics.md` "Smallest safe correction": swapped names for .01, stem-outside-the-agent-map for .02, ISO date beyond the fifth frontmatter line for .05) plus the .06 frontmatter-only and .07 same-lead witnesses it asked to add "if the revised counter continues to claim fidelity".

generator-keyed-mutant (`redesign-receipts/generator-keyed-mutant.redesign.txt`), seed `f18e8e5c2516ce2852f2a7580bf3d12f`:

```text
agent-definition boxes executed and discriminating 0 of 9
  agentdef.01: not counted (4 of 8 cases wrong: f3-no-name-anywhere expected PASS, saw exit 1, status FAIL; hn-digits-anywhere-body-date expected PASS, saw exit 1, status FAIL; ...)
  agentdef.02: not counted (4 of 7 cases wrong: f1-orphan-not-enrolled expected FAIL, saw exit 0, status PASS; f5-roster-without-agent-map expected FAIL, saw exit 0, status PASS; ...)
  agentdef.05: not counted (4 of 5 cases wrong: hn-name-differs-from-any-stem-two-files expected PASS, saw exit 1, status FAIL; ...)
  agentdef.06: not counted (4 of 4 cases wrong: f4-bare-word-task expected PASS, saw exit 1, status FAIL; ...)
  agentdef.07: not counted (4 of 6 cases wrong: hn-repeated-lines-short expected PASS, saw exit 1, status FAIL; ...)
```

The mutant's schedule (`"PFPFFPPFFP"` for .02, `"PF"*5` for the rest) indexes a directory count that is now constant (5 in the case root, 1 in the run root), so its answers are a fixed string of FAILs; the shuffled order breaks the remaining positional guess even if it were not.

# 4. Files, and what was not touched

Written outside the lane:

```text
/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter/verifiers/check_agentdef_boxes_v2.py   (the deliverable)
/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter/redesign-probe.sh                       (world rebuild script)
/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter/redesign-receipts/                      (scores.tsv, self-test.txt, redarm.txt, reference-seeds.txt, *.frozen.txt, *.redesign.txt)
/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignCounter/redarm/check_agentdef_boxes_v2.py       (mutated copy for the red arm)
```

Not touched, per the C2 withdrawal and the lane bounds: `verifiers/check_agentdef_boxes.py` (bytes unchanged: the frozen predicate is the baseline in §3), `verifiers/checklist-baseline.json`, `SKILL.md` (the nine agentdef box texts are untouched), `verifiers/verify_surfaces.py`, `verifiers/check_agent_definitions.py`, `.ufo/state`, `.ufo/watchdog.log`, `MANIFEST.json`, any jj state or the lane Git index. No lane file was edited by this seat other than this report.

# 5. Commands and clocks

All in the sandbox clone unless stated; every command was `timeout`-capped; no `pacman`, no installs, no paid model call, no browser.

```text
date -u                                              -> Fri 23 Oct 2026 02:46:41 AM UTC (start)
sha256sum verifiers/check_agentdef_boxes.py          -> 8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  verifiers/check_agentdef_boxes.py
sha256sum verifiers/check_agentdef_boxes_v2.py       -> 5dbee46380651e98cfbc755962006f08f0e6990c82c4221ca94bdac59d531f4e  verifiers/check_agentdef_boxes_v2.py
python3 -B verifiers/check_agentdef_boxes_v2.py --self-test     -> exit 0, "self-test: 0 failure(s) over 184 assertions", 24.2 s
bash redesign-probe.sh (11 worlds, both counters)    -> completed, 47.4 s; output ends with the clone HEAD listing
loop over 11 world revs, both counters               -> completed, 203 s; redesign-receipts/scores.tsv holds all 11 rows
reference delegate over 3 fixed seeds                -> completed, 5 of 9 on each seed, 33.6 s
red-arm self-test                                    -> exit 1, 2 failures
date -u                                              -> Fri 23 Oct 2026 02:56:17 AM UTC (first probe finished)
```

The lane was inspected read-only: `git --no-optional-locks status --porcelain --untracked-files=all` at `250e302` shows other seats' files (`SKILL.md` modified, sibling build reports untracked) and none of mine except this report; `sha256sum verifiers/check_agentdef_boxes.py` in the lane is unchanged.

Sandbox commits (clone only, none pushed): `ee5e391` naive-multifile, `fdc6620` naive-any-stem-difference, `86c68c1` naive-stem-membership, `91f4c0b` tuned-identity-only, `70f9efe` tuned-identity-and-roster, `e984e01` tuned-three-boxes, `2d32d96` tuned-all-five, `f730349` tuned-all-five-refined, `4abd449` generator-keyed-pristine, `8d919f0` generator-keyed-mutant, `411a540` generator-keyed-restored.

Tooling: no tool installed or upgraded this seat. Processes: all runs returned; the only children were `timeout`-wrapped `python3` invocations, no long-lived service.

# 6. Limits and risks (what this evidence does not say)

1. **Not a claim and not integrated.** C2 stays withdrawn; the redesign is a later round's input. The file is in scratch, not in the lane, and the L1 decides whether to adopt it.
2. **0 of 9 is evidence about these two controls, not a proof of general discrimination.** The coverage matrix checks the twelve *transcribed* rules of the withdrawn controls (plus the two profile fixtures). A future control with a different rule is not covered; the matrix would have to grow.
3. **Cross-case persistence cannot be fully prevented in-process.** Per-case HOME, TMPDIR, cwd and the private tree copy close the channels the state-keyed fixture exercises, but a delegate can still write to a fixed absolute path it chooses. The defense there is the shuffle — an invocation count without a stable order carries no information — not confinement. The redesign says so in its docstring rather than claiming a sandbox.
4. **`repeated_lines` is a weak class.** The frozen case shape always repeats the two `---` frontmatter delimiters, so that class answers FAIL on every agent file and is wrong on every PASS case for a trivial reason. I keep it because it is the withdrawn control's rule; a later round that wants a meaningful repeated-line hard negative must first decide whether the delimiter repetition is in scope.
5. **`MAX_REPORTED = 4` changes the diagnostic tallies.** A box stops after four mismatches, so its line reads `4 of 7 cases wrong` rather than `4 of 18`; the counted/not-counted decision is identical, and the saving is what keeps a bad delegate cheap. A later round should decide whether to keep fail-fast.
6. **Runtime headroom is host-dependent.** 10.9 s for a correct delegate and 90 cases here; the budget check (240 s) marks the remaining cases wrong rather than passing them, so a much slower host degrades toward 0 of 9, not toward a false pass.
7. **The twin-pair device is partly vestigial** now that cases are isolated: the shared group directory name can no longer be compared across cases, but it still forces a name-keyed delegate to answer both twins alike. Cheap to keep; harmless if dropped.
8. **The nine box texts and every map disposition are untouched**, so nothing here pre-scores a later claim or changes any `unexecuted:` disposition.

# 7. Decisions the later round must make

- Adopt, shrink or replace the twelve-class coverage list, and freeze it before data.
- Keep or drop fail-fast (`MAX_REPORTED`).
- Keep or drop the per-case tree copy (17 ms/case here on 407 entries / 1.6 MB; it closes the write-next-to-itself channel).
- Decide whether the hard-negative families belong to the frozen counter or to a separate case corpus the counter loads (both are defensible; the counter currently generates them, so they are seeded and unpinned).
