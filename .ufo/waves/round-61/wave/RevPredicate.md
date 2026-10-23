# RevPredicate — audit of the three frozen predicate sentences against claim-sizing rule 9

Seat: kotoba-r61-wave-RevPredicate · 2026-10-23 · read-only audit, no lane/fleet writes except this report.
Commits examined: freeze `7827628` → E1 `c630c4c` → E2 `3dbf007` (all on top of base `f3246d1`).
Inputs: `plans/round-61.md` (at freeze and at HEAD), rule 9 text (`.ufo/prompts/kotoba-round-61.md` §6 item 9, lines 350–372), `verifiers/check_routed_repairs.py` (full), `verifiers/check_scoped_rules.py` (docstring, rev-mode, predicate, self-test regions), `.ufo/waves/round-61/controls/C2-base.txt`, `wave-dispatch.json`/`wave-spec.json` (counter-writer + fixture + C2-audit task texts), r60 ground (`controls-v2/SUMMARY.md`, `corpus/lessons/round-60-verifier-spotcheck.md` §7–§8), `AXES.md`.

## Per-predicate verdicts

| predicate | verdict |
|---|---|
| C1 (depth) | **2 defects** (1 high, 1 medium) + 2 low notes — sentence is byte-stable and well-sized, but its base clause has no declared mechanism and its label/receipt slots are not pinned to the full sentence |
| C2 (calibration) | **predicates clean** — sized, enumerated, control-committed-and-reproduced; 3 declared-limit notes only |
| C3 (adjacency) | **withdrawn pre-data (E1, `c630c4c`) — the rule-9-correct outcome**; this seat independently confirms the hollow-control class (M92) |

Rule-change check: the plan diff `7827628→c630c4c→3dbf007` is append-only errata (+15, +24 lines); the C1 and C2 predicate sentences are byte-identical across all three commits (verified by `git show` extraction). Both errata are pre-data: no v3 measurement exists (the counter is still being drafted; `ExecCounterV3` is in flight), and no repair blob has landed (C2 at tip still 0 of 6, measured below). No rule was changed after any seat scored data. kumitate r42 is not implicated.

## Rule-9 checklist

- **Universal clause not enumerable by the counting command** — none found. C1's "seven worlds reject / four eligible rows pass" is fully enumerated (W1–W7 named in the plan, W0 do-nothing included with expected exit 1; the four eligible rows are the r60 eligible set). C2's "every routed repair (a)–(f)" enumerates six, each with its own blob test. C3's universals died with the claim.
- **Target a do-nothing control could reach** — C2: committed base control scores 0 of 6, exit 1 (`C2-base.txt`, in the freeze commit); 6 of 6 not reachable do-nothing. C1: with v2 unchanged, `--fetch` exits 0 at tip (r60 measured 4 of 4 live) and at base, so the conjunction (tip 0 ∧ base 1) fails do-nothing — **but see Defect 1: the base conjunct may be unreachable in the *other* direction (honest work fails it too)**. C3: the frozen 0→1 observables were all preserved by a hollow tree (row + index kept, entry swapped for scope-absorbing claims) — exactly the do-nothing-reachability rule 9 bars; E1 withdrew it before data. Correct.
- **Rule changed after data risk** — clean (see above). E2's A3 amendment (byte-identity → url_key identity) is pre-data with the limit disclosed and the predicate sentence explicitly unchanged; the r60 E1/E2 precedent and the r56–r58 withdrawal precedent are cited in the errata themselves.
- **Axis named by surface not number** — clean. All three claims name axes by surface (depth, calibration, adjacency per `AXES.md`); "depth 9 (consistency 10)" cites the held SCORECARD scores, not a produced number. (AXES.md axes carry no numerals.)

## C1 findings

### Defect 1 (high): the base clause "same command at base `f3246d14` exits 1" has no declared mechanism, and the dispatched design plausibly makes it exit 0

The plan and the `ExecCounterV3` dispatch declare *what* must happen at base but never *why* it would. Grounded in the committed v2 rev-mode (`check_scoped_rules.py:2510–2563`: exit 0 iff `--fetch` ∧ found ≥ TARGET; exit 2 if SKILL.md/rev unreadable; exit 1 otherwise), the four r60 eligible rows at base have: committed snapshots introduced 2026-10-23 (`7b80ae8`) = recorded open date (A4 "no older than" passes on equality), actions supported by those snapshots (A2 passes), url_key-equal re-opens (amended A3 passes), and scope keys that are exactly the keys the canonical set will contain. The dispatch pins the A1 set **inside the counter** ("populated from S112-S115 row texts the scribes draft this wave") — not read from the measured revision — so the set is identical at base and at tip. Under that design, `v3 --rev f3246d14 --fetch` computes found = 4 ≥ TARGET and **exits 0 at base: the frozen predicate is unsatisfiable and the kill rule fires on good work.** The plausible fix (require S112–S115 rows, or the seven committed fixture worlds, to exist in the measured revision, so base genuinely lacks them and exits 1) is nowhere stated in plan, dispatch, or arm spec.

Required before the `--fetch` data measurement (this is M90 applied to C1's own control): (a) declare in the plan (erratum) exactly which condition makes base exit 1 and confirm it exits 1 not 2; (b) commit a C1 base control receipt (e.g. `.ufo/waves/round-61/controls/C1-base.txt`, the v2 counter's run at base plus the declared mechanism) alongside the seven fixture receipts. `round-61/controls/` currently holds only `C2-base.txt`.

### Defect 2 (medium): only the self-test line of the C1 predicate is pinned in the counter/receipt slots — the full sentence is not

Rule 9: "Freeze one predicate that is the same sentence in the plan, the same condition in the counter's code and the same label in the receipt." The plan sentence has two clauses; the dispatch pins only clause 1 verbatim ("Print the predicate line exactly: `worlds reject 7 of 7; eligible rows pass 4 of 4`"). The v2 precedent label is a *different, shorter* sentence (`RECEIPT = "C1 predicate: --fetch exit 0 (F>=TARGET)"`, `check_scoped_rules.py:259`). Nothing commits v3's docstring label or the integration receipt to carry the **full** two-clause sentence including the base-exit-1 clause and an instantiated `<tip>` sha. L1 action at integration: pin the full sentence verbatim in the v3 counter label and in the measurement receipt, with `<tip>` replaced by the integration sha and the base sha spelled out.

### Note 3 (low): dispatch text superseded by E2

The committed `ExecCounterV3` task text still reads "add A3 URL byte-i[dentity]" — superseded 40 minutes later by E2 (url_key identity). The dispatch's own pointer ("per the frozen arm spec in plans/round-61.md") makes the plan canonical, so a seat re-reading the plan gets the amended arm; drafts built from the dispatch string alone will carry the dead arm. The L1 must reconcile at integration and keep E2's fixture rule (every world receipt pins the rejecting arm and printed line).

### Note 4 (low): dispatch key-set enumeration is internally inconsistent

`ExecCounterV3` task text: "allow the four documented keys paths/applyTo/applyTo/globs" — four items, three distinct (`applyTo` twice). The canonical per-client key set must be enumerated exactly once, from the S112–S115 row texts; correct the enumeration when integrating.

## C2 detail (predicates clean)

Same-sentence check passes on all three slots: plan line 64 (`routed repairs verified 6 of 6` exit 0; base 0 of 6, exit 1) = counter code (`check_routed_repairs.py`: prints `routed repairs verified {k} of 6`, `return 0 if k == 6 else 1`, exit 2 = could-not-evaluate) = committed receipt label (`C2-base.txt` ends `routed repairs verified 0 of 6` + `base-exit=1`). The self-test enumerates every repair's absence arm (base world 0 of 6, no-log 3, no-quality 5, each damaged file 5, R-a-without-command 5, R-b-missing 5) — all arms pass (measured below). The control receipt was committed in the freeze commit, before any repair content existed (repairs still absent at tip — measured). Calibration-axis conformance: the six counted items are precisely claimed-vs-committed mismatch repairs (32-vs-29, omitted files, wrong pointer), not assertions.

Declared-limit notes (no predicate defect; the counter's docstring already assigns them to reviewers per Q31): (1) plan's R-a wording "with its counting command" says slightly more than the code checks, which tests the path substring `.ufo/waves/round-60/build` but not the command shape; (2) R-d is satisfiable by any file ending `exit=0`, including a stale or hand-typed one; (3) R-f accepts any text containing `merge-base --is-ancestor` and `exit 0` without verifying the ancestry itself. These are byte-counter limits, disclosed in the docstring; the honesty layer is the reviewers'.

## C3 detail (withdrawn — correct)

This seat had independently flagged the same class before seeing E1: (a) the README-row conjunct had **no counting command at all** in the plan ("plus `test -f` on the entry and its `README.md` row" — `test -f` cannot check a row, and no grep/pattern for the README row is named), so "the corpus README index gains a row" was not re-derivable by the named commands; (b) `test -f` passes on an empty file; (c) all three observables measure *presence*, not the adjacency property (reported, not absorbed). CriticC3Axis's static counterexample (row + index kept, entry replaced by scope-absorbing unsupported claims) reaches every observable, so the target was do-nothing-equivalent-reachable — rule 9 bars it, and E1 withdrew the claim **before any C3 data entered the lane**, retiring the predicate unmeasured, keeping curation as frontier work, and mining M92. This is the discipline working; no defect in the withdrawal. For M92's lesson text: the absence of a counting command for the README row (point (a)) is an additional, distinct sizing defect worth naming beside the presence-counter class.

## Measurements (run by this seat, read-only; `python3 -B` = no bytecode writes)

```
Fri 23 Oct 2026 07:15:07 PM UTC   (date -u)
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
base-exit=$? → 1
(matches .ufo/waves/round-61/controls/C2-base.txt line-for-line)

$ python3 -B verifiers/check_routed_repairs.py --rev c630c4cbc01ff5e5438ab0033cfadd6e19382ab1
… same six lines … routed repairs verified 0 of 6
tip-exit=$? → 1   (no repair content has landed as of c630c4c)

$ python3 -B verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok … (9 arms) …
self-test: 0 failure(s)
selftest-exit=$? → 0

$ grep -c 'self-assessment-at-writing' corpus/SOURCES.md → 0, exit 1
$ test -f corpus/knowledge/writing-revision-calibration-round61.md → exit 1
(C3 base value 0, at the pre-data tree; observables since withdrawn by E1)

$ git show 7827628:plans/round-61.md | sed -n '50,55p'  vs  git show 3dbf007:plans/round-61.md | sed -n '50,56p'
→ C1 predicate sentence byte-identical across freeze → E1 → E2
```

## Residual risk and verification gaps

- I did not and could not run v3 (it does not exist); Defect 1's base-exit-0 outcome is an inference from the committed v2 mechanics + the dispatched pinned-set design, not a measurement. It is actionable now precisely because it is checkable the moment v3 exists — before any `--fetch`.
- The counter-label and receipt slots for C1 are unlanded; my slot check there is a contract-gap check, not a drift observation.
- C2's R-a/R-d/R-f honesty limits are unexercised by me (ExecC2Audit's assignment covers dishonest-pass probing); I verified the control direction only.
- Lane tip moved during the audit (c630c4c → 3dbf007); findings are stated against 3dbf007 except where a measurement names its rev.

Installs: none. Blockers: none.

Attacked the three frozen predicate sentences (C1/C2/C3) against claim-sizing rule 9 across plan/counter/receipt slots and committed controls: C2 clean, C3 correctly withdrawn pre-data (E1), C1 carries one high defect (undeclared, plausibly unsatisfiable base-exit-1 clause) and one medium (unpinned full-sentence label/receipt slots), both fixable pre-data.
