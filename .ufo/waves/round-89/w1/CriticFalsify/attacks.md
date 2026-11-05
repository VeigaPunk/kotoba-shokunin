# CriticFalsify — attacks on the two frozen round-89 claims (pre-data)

Seat: CriticFalsify (critic, leaf). Lane `kotoba-shokunin`, lane HEAD read at `0f2b866` (wave dispatch commit).
Base `a5b3b15c00b1de5db321e4226a0a7db17340e605`; plan draft `43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3`.
`git diff 43fc784 HEAD -- plans/round-89.md` prints nothing: predicates, targets, controls and kill rules are unchanged.
Measurements: scratch clones under `/fast/scratch/hyaku/kotoba-r89/CriticFalsify/` (deleted at yield). Receipts
copied to `.ufo/waves/round-89/w1/CriticFalsify/receipts/`. No lane file was edited; `verifiers/check_freeze_gate.py`,
`check_r86_routed_repairs_v3.py` and their fixtures are in progress (untracked) and were only read and run.

Clause-to-arm map for the Q26 audit is in section 1. Verdicts are in section 2. Pre-data narrowing is in section 3.

---

## 1. Q26 headline audit (clause → turning arm)

### C1 — "freeze gate refuses an unsatisfiable freeze: exit 1 naming w_added_red; fixed plan exit 0"

| clause | turned on by | status |
|---|---|---|
| exit 1 | `check_freeze_gate.py` returns `EXIT_REFUSED` on the first control whose observed exit or stdout literal differs (lines 270–282) | has arm |
| names `w_added_red` | line 278 prints `REFUSED control <name> (line N)`; arms at self-test lines 462–488 (`arm unsat names w_added_red`, `text.count("REFUSED control") == 1`) | has arm |
| "unsatisfiable" | **no arm.** The gate never evaluates satisfiability. It compares a declared literal with the stdout of `sim-w-added-red.sh`, and that simulator only greps the recorded round-88 receipt for `PASS d5`. | **no arm — narrowing demand N6** |
| fixed plan exit 0 | `r88-controls-fixed.md` holds | has arm |
| shortcut (a), exit-only stub | no arm: the r88-controls arm declares a stdout literal, so it does not kill an exit-only plan | **no arm — narrowing demand N7** |

### C2 — "instance-level D5 instance drift K; exit 0 iff N==5 and K==0 and digests match"

| clause | turned on by | status |
|---|---|---|
| exit 0 iff N==5 | `compare`: `n != TARGET` → 1 (v3:699) | has arm (self-test `w_tip`, v3:946–948) |
| K==0 | `growth_names` (v3:495–500) feeds d5iii and `k = len(grew)` (v3:692) | has arm: `instance drift 0` (v3:948) |
| K>0 pinned | self-test arm at v3:998 requires `FAIL d5iii` and `instance drift 2` on the added-instance world | has arm |
| "instance" | K counts **names** whose value grew (`growth_names` returns names; print at v3:694), not instances. A name growing by 5 gives K=1. The v3 d5iii test is count-level, not instance-level. | **label/scope defect — narrowing demand N2** |
| digests match | `snap_ok` (v3:668–682) over `verify_corpus_integrity.py` and `corpus-baseline.json` | has arm (`snapshot_tampered`) |
| "same instance" | no leg compares detail identity (which citation, which path) | **no arm — narrowing demand N2** |

---

## 2. Verdict table

### C1 — freeze gate

| # | attack | verdict | evidence |
|---|---|---|---|
| C1-a | The gate refuses an *unsatisfiable* freeze. It only refuses a declaration that disagrees with a simulator, and the simulator is a receipt grep. | **ATTACK STANDS** | `sh verifiers/fixtures/freeze-gate/sim-w-added-red.sh` → `w_added_red D5=PASS`, exit 0. The sim reads `.ufo/waves/round-88/w1/ExecMonotoneD5/receipts.txt` (`--- w_added` block) and `ExecMonotoneD5.md`. Nothing executes `check_r86_routed_repairs_v2.py`. This is the Q37 "gate that remaps real findings" shape. Accuracy today: the v2 gate on the added-instance world reads `PASS d5`, `5 of 5`, exit 0 (see C2-c), so the sim's text is right. The gate still does not check it. |
| C1-b | Exit 1 naming `w_added_red`. | **REPELLED** | `python3 -B verifiers/check_freeze_gate.py --plan verifiers/fixtures/freeze-gate/r88-controls.md` → `REFUSED control w_added_red (line 36): declared "exit 0; stdout contains D5=FAIL"; observed exit=0 stdout=w_added_red D5=PASS\n (stdout literal 'D5=FAIL' absent from observed stdout)`, exit=1. Fixed plan → `freeze gate: 4 control(s) held — freeze may proceed`, exit 0. Arms at self-test 462–488. |
| C1-c | Do-nothing: an existing instrument already refuses the r88 world. | **REPELLED** | No pre-existing verifier parses a plan `## Controls` block. `grep -ln '## Controls\|expect:' verifiers/*.py` hits only `check_agentdef_boxes.py:343`, `check_alwayson_boxes.py:184`, `check_could_not_evaluate.py:181`, which use `expect` as their own function parameters. `before-c1-absence.txt` (grep-exit=1) corroborates. The round-88 v2 gate does not refuse the unexecuted control either: its self-test fails `1 failure(s) over 16 assertions` (`before-v2-selftest.txt`), and that failure is recorded but not refused. |
| C1-d | Shortcut (a): "a stub whose controls declare exit 0 against the refusing simulator, killed by the r88-controls arm." | **ATTACK STANDS (mis-cited arm)** | `stub-exit-only.md` (two controls, `expect: exit 0` only) → `freeze gate: 2 control(s) held — freeze may proceed`, exit 0 (`receipts/stub-exit-only-result.txt`). The r88-controls arm declares `stdout contains D5=FAIL`, so it cannot kill an exit-only stub. Shortcut (a) has no arm. |
| C1-e | Sourced-claim (Q80): S258 quotes. | **REPELLED** for the quotes, **STANDS** for the `teaches` line (section 4). | |

### C2 — instance-level D5

| # | attack | verdict | evidence |
|---|---|---|---|
| C2-a | "Instance-level": D5(iii) detects instance growth. It compares one integer per check name. | **ATTACK STANDS** (headline overstates) | Probe E: a same-count instance swap. In `corpus/lessons/round-81.md:8` the dead hex `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` is replaced by another dead hex `fedcba9876543210…`, count unchanged. `python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt r-lane.json --root <clone@B>` → `PASS d5iii no name grew past its receipt value`, `r86 routed defects closed 5 of 5`, `instance drift 0`, exit 0 (`receipts/E.txt`). |
| C2-b | The `instance drift K` print is pinned at 0 vs >0 by an arm. | **REPELLED** (arms exist); **STANDS** on what K counts | Arms at v3:948 (`instance drift 0`) and v3:998 (`code == 1 and "FAIL d5iii" in out and "instance drift 2"`). Probe C reads `FAIL d5iii instance growth under: ['corpus.pointers.commit_total 62>61', 'corpus.pointers.commit_unresolvable 2>1']`, `instance drift 2`, exit 1 (`receipts/C.txt`). K is a name count (v3:495–500, v3:694), so the label is wrong, not the arm. |
| C2-c | Do-nothing: the frozen v2 gate reads the added-instance world as PASS. | **REPELLED** (v2 is blind on the world, as claimed) | Scratch clone at base `a5b3b15` plus one appended lesson line citing unresolvable `0123456789abcdef…`. `python3 -B verifiers/verify_corpus_integrity.py --json` → `commit_unresolvable DRIFT observed=2` (base 1), `commit_total DRIFT 62`. The name-set of DRIFT is identical. `check_r86_routed_repairs_v2.py --rev <world> --repo <clone> --work <dir>` → `PASS d5 identity: 9 names equal …; monotone: DRIFT at rev [...] is a subset of base [...]`, `r86 routed defects closed 5 of 5`, exit 0. Frozen v2 self-test: `1 failure(s) over 16 assertions`, `FAIL arm w_added_red`. |
| C2-d | Vacuity: the landing adds no corpus bytes, so exit 0 at the landing tip is trivial. | **REPELLED** for corpus growth; **STANDS** for growth outside corpus and for swaps | Probe C (corpus growth): one appended line under already-red names → v3 `FAIL d5iii`, exit 1. Non-vacuous on that world. Probe F (outside corpus): `[0123…]` added to `LOG.md` → `PASS d5iii`, `r86 routed defects closed 5 of 5`, `instance drift 0`, exit 0 (`receipts/F.txt`). Probe E (swap) also passes, see C2-a. |
| C2-e | Q79 location: the receipt is written in the lane and the controls are measured in clones. | **ATTACK STANDS (blocking)** | Lane receipt: `r-lane.json` at `0f2b866`, `corpus.pointers.report_dead PASS observed 0`. Clone at the same revision with the symlink intact (`.ufo/reports/round-76/kotoba.md` → `../../../../.ufo/reports/round-76/kotoba.md`, dangling outside the fleet root): `FAIL d5ii new DRIFT names absent from the receipt: ['corpus.pointers.report_dead']`, `FAIL d5iii instance growth under: ['corpus.pointers.report_dead 1>0']`, `r86 routed defects closed 4 of 5`, exit 1 (`receipts/A.txt`). Probe B materializes the 8,128-byte report as a world-local commit in the clone: `PASS d5iii`, `5 of 5`, exit 0 (`receipts/B.txt`). Every clone-measured control and `w_equivalence` as written would fail for the wrong reason. |
| C2-f | Regression: the round-87 M87-1 launder guard survived into v2/v3. | **ATTACK STANDS** | `grep -c -i 'launder\|rewritten\|blob'`: `check_r86_routed_repairs.py` 38, `_v2.py` 0, `_v3.py` 5. The 5 in v3 are instrument-identity blob checks (v3:20, 156, 323, 344, 347). The r87 gate's conjuncts at `check_r86_routed_repairs.py:64–68, 425–432` (`… rewritten at … (blob … != base …)`) compare non-author and historical records to base blobs. v2 replaced r87's D5 and dropped them. Probe E is the consequence: `corpus/lessons/round-81.md:8` rewritten to a different dead hex is green. Q64 forbids that move, and the plan does not disclose the drop. |
| C2-g | The base receipt is taken from the working tree but records `HEAD`. | **ATTACK STANDS** | `write_base_receipt` (v3:505–542) runs the integrity gate in the working tree (cwd = root) and stores `rev-parse HEAD` with no clean-tree assertion. The lane is currently dirty at `verifiers/floors-registry.json` and in untracked new instruments (`git status --porcelain`). A receipt written then would pin a state no commit names. |
| C2-h | Snapshot digest pins (`verify_corpus_integrity.py`, `corpus-baseline.json`). | **REPELLED** (in code) | `snap_ok` and `snapshot_tampered` at v3:668–682; `LEG_ORDER` includes `snapshot_tampered` (v3:588). The `w_rerecorded` world was not run by this seat (ExecCtlWorlds owns it). |

### Kill rules and freeze protocol (both claims)

| # | attack | verdict | evidence |
|---|---|---|---|
| K-a | `git diff <freeze> <landing> -- verifiers verifiers/fixtures plans corpus` misses the C1 controls' inputs. | **ATTACK STANDS** | The four C1 sims read round-88 receipts outside those prefixes: `sim-w-added-red` → `.ufo/waves/round-88/w1/ExecMonotoneD5.md`, `…/ExecMonotoneD5/receipts.txt`; `sim-w-silenced` → `…/CriticFalsify/attacks.md`, `…/ExecMonotoneD5/receipts.txt`; `sim-w-healed` → `…/ExecMonotoneD5/receipts.txt`; `sim-w-tip` → `.ufo/waves/round-88/receipts/before-C2-tip.txt`, `…/l1-c2-tip.txt`, `…/w1/ReviewerC2/review.md`. A post-score edit to those files changes a declared control's observed verdict with an empty diff. |
| K-b | The same command misses the C2 base receipt and its snapshot pins. | **ATTACK STANDS** | The pins live in the base receipt at `.ufo/waves/round-89/receipts/d5v3-base-receipt.json` (planned), which is outside the prefixes. The kill rule names "the base receipt or the snapshot digest pins." |
| K-c | SKILL.md registry rows change semantics after a score. | **ATTACK STANDS** | `check_gate_registry.py` reads SKILL.md's `## Gate registry` (line 354). A row's `kind` (gate ↔ probe) or command, changed after the score, changes what the lane claims is a gate, and SKILL.md is outside the prefixes. Q46 governs this. |
| K-d | Uncommitted state and gitignored inputs are invisible to a commit-to-commit diff. | **ATTACK STANDS** | The integrity gate reads the working tree. `git diff <freeze> <landing>` reads commits only. Currently `M verifiers/floors-registry.json` plus untracked instruments. Requires `git status --porcelain` empty and `git ls-files -o -i --exclude-standard` empty at both revisions. |
| K-e | The freeze-receipt command `git diff <draft> <freeze> -- plans/round-89.md` proves that no predicate changed. | **ATTACK STANDS** | The command prints lines but the plan does not require that no `-` line appears inside a predicate block. An empty `-`-line check is needed. |
| K-f | Scope of the kill rule for C1 includes "its floors row": the floors row (`verifiers/floors-registry.json`) is inside `verifiers/`. | **REPELLED** | Covered by the diff path. |
| K-g | `scripts/` (sources census) and `LOG.md`/`SCORECARD.md`. | **NOTE** (not a predicate) | Not on either claim's predicate path. Listed for completeness. |

### Q80 — attack seats

| # | attack | verdict | evidence |
|---|---|---|---|
| Q80-a | Wave has no attack seat. | **REPELLED** | Attack seats present or planned: `ReviewerFreezeGate`, `ReviewerD5Gate` (both have seat directories), `CriticFalsify` (this seat), `MutTesterGates`. |
| Q80-b | Mutation-tester output exists. | **STANDS (open)** | `.ufo/waves/round-89/w1/MutTesterGates` does not exist at this read. The round closes provisional under Q80 unless the seat's output lands. |

---

## 3. PRE-DATA narrowing list (findings the L1 must fix before the first candidate score)

Each item names the arm or receipt that proves it. Predicate changes before the first candidate score go through a
pre-score addendum with its own re-run controls (the C1 rule). Anything after the first score kills the claim.

**N1 — C2, blocking, Q79.** `report_dead` depends on the symlink `.ufo/reports/round-76/kotoba.md`, which resolves only in
the lane. A clone measuring the same revision reads `report_dead 1>0` and D5 refuses (`receipts/A.txt`). Every
clone-measured control world (`w_added_instance`, `w_silenced`, `w_rerecorded`, `w_healed`, `w_tip` in clones) and `w_equivalence`
as written would fail for that reason. **Fix:** every world builder materializes the symlink target as a world-local
commit (as probe B does: `receipts/B.txt` → `5 of 5`), and `w_equivalence` compares the lane with the materialized clone.
Name this in the plan's Q79 (a) item.

**N2 — C2, blocking, Q26.** "Instance-level" is false: D5(iii) is one integer per check name, and K counts names. Probe E
(same-count swap, `receipts/E.txt`) passes. **Fix (choose one before scoring):** (a) bound the headline to "count non-growth
per check name", rename K to "grown names", and keep the arms at v3:948/998 consistent; or (b) add a detail-identity leg
(the set of citation/path details per check must not grow beyond the receipt's), with probe E as a control expecting exit 1.

**N3 — C2, Q26/Q37.** D5 is corpus-scoped: a dead citation in `LOG.md` passes (probe F, `receipts/F.txt`, exit 0). Either bound
the claim to corpus `*.md` citations, or add `w_relocated` as a named control with its honest expected verdict. Extending
the integrity scope edits a frozen instrument, so it is not an option this round.

**N4 — C2, regression (M87-1).** The launder conjuncts of the round-87 gate (`check_r86_routed_repairs.py:64–68, 425–432`) are
absent from v2 and v3. Probe E shows a historical record rewritten and green. **Fix:** reinstate blob-immutability for
`corpus/lessons/round-81.md` and `round-86-verifier-spotcheck.md` (the non-author and historical records named in the honest
bound), with probe E as the control expecting exit 1. Otherwise the plan must disclose the dropped guard as a residual.

**N5 — C2, vacuity/Q79.** `write_base_receipt` must refuse a dirty tree (`git status --porcelain` empty), record a `HEAD`
that equals the measured tree, and be written from the freeze commit itself. The integrity gate reads the working tree, so a
receipt written before the freeze commit can pin an observation no commit names (C2-g).

**N6 — C1, Q26/Q37 (headline).** The sims grep recorded receipt text; the gate compares declaration to text. The
headline "refuses an unsatisfiable freeze" is not what is measured. **Fix:** either the sims run the instrument on the world
and print the observed verdict, or the headline is bounded to "refuses a declared expectation that contradicts the control's
recorded verdict". The current reproduction is accurate today (v2 on the world reads `PASS d5`, matching `sim-w-added-red`),
so only the wording or the oracle must change.

**N7 — C1, Q37.** Shortcut (a) is mis-cited and not killed. `stub-exit-only.md` holds (exit 0, `receipts/stub-exit-only-result.txt`).
**Fix:** add an arm where an exit-only or literal-less control declaration is refused (exit 3, invalid spec), or require a stdout literal per control in the grammar.

**N8 — kill rule, all claims.** Extend the freeze diff path to cover the inputs found in K-a…K-d:
`.ufo/waves/round-89/receipts`, `.ufo/waves/round-89/w1`, `.ufo/waves/round-88/w1/ExecMonotoneD5`,
`.ufo/waves/round-88/w1/ExecMonotoneD5.md`, `.ufo/waves/round-88/w1/ReviewerC2`, `.ufo/waves/round-88/w1/CriticFalsify`,
`.ufo/waves/round-88/receipts`, `SKILL.md`, `scripts`, `LOG.md`, `SCORECARD.md`. Add `git status --porcelain` empty and
`git ls-files -o -i --exclude-standard` empty at both revisions, and the `-`-line empty check on the freeze diff of `plans/round-89.md` (K-e).

**N9 — sourced (Q62/Q80).** The knowledge entry must quote S258 only for the two located sentences (1451 and 1472). The `teaches`
line ("a control whose expectation cannot be observed under that commitment is not a confirmation") is the scout's inference,
not the paper's, and must be labelled as the lane's inference. Fix the S259 word counts in the row or lesson (see section 4).
Use URL `PMC5856500`, not the assignment's `PMC5813543`.

**N10 — Q80 closure.** `MutTesterGates` has no output at this read. Closure must show its output, or the round closes provisional.

---

## 4. Sourced-claim audit (Q80, C1 cites S258 + S259)

Checked against bytes I opened (`.ufo/waves/round-89/w1/ScoutSource/s258.html`, sha256 `ee0d0560901a0e65c6b8079e2eaf1d79c049c74597ce3f374b4e19bce0ba51f9`,
matching the seat's record; `git show a5b3b15c…:corpus/lessons/round-88-verifier-spotcheck.md`, sha256
`236aa5172442fc7d5dbb860c59997f339883be82a9647b188f1bb84298215cfd`, matching).

| source | claim | verification | verdict |
|---|---|---|---|
| S258, HTML line 1451, under §Preregistration Distinguishes Prediction and Postdiction (h2) | "Preregistration of an analysis plan is committing to analytic steps without advance knowledge of the research outcomes." | verbatim; 17 words (≤25) | **quote holds** |
| S258, HTML line 1472, under §Preregistration in Practice → "Challenge 5: Many Experiments." (h3 precedes line 1472) | "researchers can achieve confirmatory research via replication. All initial experiments are treated as exploratory research." | verbatim; 15 words (≤25) | **quote holds** |
| S258, line 1478 (alternative) | "Preregistration benefits both exploratory research and testing predictions during the iterative research process." | verbatim; 13 words | holds (not used) |
| S258 `teaches` line | "a control whose expectation cannot be observed under that commitment is not a confirmation" | this is the scout's inference; the paper says nothing of controls | **STANDS** — label as the lane's inference (N9) |
| S259, line 73 (defect 3) | "a freeze must execute every frozen control and refuse the freeze on an expectation the predicate cannot satisfy" | verbatim; **18 words** by count (`grep -o … \| wc -w`). The scout wrote 20. | quote holds; **word count miscounted** (still ≤25) |
| S259, line 74 (defect 4) | "instance-level D5 with controls executed before the freeze" | verbatim; **8 words** (the scout wrote 9) | quote holds; **word count miscounted** |
| S258 route (a) `PMC5813543` | assignment's route | HTTP 200 but a different article (STKR1/SnRK1, 307,298 B). The seat rejected it and did **not** paraphrase it into evidence. Routes (b)/(c) returned HTTP 403. The DOI resolves to `PMC5856500` via the NCBI idconv API. | **honest reject of the route**; no fabricated evidence |

Q80 "failed fetch must be reported as an honest reject, never paraphrased into evidence": **REPELLED** (the scout's receipt
shows the wrong article and the 403s, and no quote was taken from them).

---

## 5. Scope of this seat

- Written: `.ufo/waves/round-89/w1/CriticFalsify/attacks.md` (this file), `.ufo/waves/round-89/w1/CriticFalsify/receipts/*`, and the report `.ufo/waves/round-89/w1/CriticFalsify.md`.
- No lane file, instrument, plan, corpus file or fleet file was edited. No git write was run. No tool was installed.
- Scratch clones were used for probes and are deleted at yield. Probe commits (`675d67e`, `80cf9d7`, `ba34aca`) exist only in the scratch clone; the C world commit was dangling after detach and is recorded as its command, not a sha.
