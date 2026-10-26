# R75 facet 51 — S211's `teaches` clause: "only at an even run count" is scoped to the default threshold, and nothing reads the cell

Read-only. Measured revision `65a5c7a663249e0522cc49e4a148424200d9ddfe` (lane `kotoba-shokunin`), tree clean
except siblings' untracked work (`git status --porcelain` → `?? .ufo/waves/round-75/`, `?? corpus/lessons/round-75.md`;
neither written by this seat). No source additions, no fetch, no model run, no install, no git/jj mutation.

## 1. The facet

`corpus/SOURCES.md:157` (row `S211`, 11 data cells, field 8 of the pipe split = `teaches`):

> … the reference runner passes a should-trigger query at a rate equal to the 0.5 threshold, defaults to 3 runs per
> query, **and disagrees with the specification only at an even run count** | mined | 2026-10-25 | 90d |
> corpus/knowledge/skill-eval-artefacts-round70.md |

The claim carries no condition on `--trigger-threshold`, which the same pinned code exposes as a free flag
(`.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:267`, `--trigger-threshold`, default `0.5`). The knowledge entry
this row's `used-by` names states the correct conditional in its own words
(`corpus/knowledge/skill-eval-artefacts-round70.md:69-70`):

> … with a non-default `--trigger-threshold` the rules disagree whenever threshold × runs is a whole number
> (1/3 and 2/3 at 3 runs).

Taken as a general rule the registry clause is falsified by four grid points, all at odd run counts (§3). Taken as
scoped to the defaults it is true but unstated — and the two readings lead a description audit to opposite
conclusions on the most natural strict rule it would pick. This is the surviving half of a defect the r70 wave
already found on the entry side: `corpus/lessons/round-70.md:259-261` records "Corrected in the entry after the
wave: … the odd-run action and its two limits (`ScoutEvenRunMath`, `S211Code`)" — the entry was reworded, the
registry cell was not, and the non-author r70 spot-check recorded the cell unchanged as `agree`
(`corpus/lessons/round-70-verifier-spotcheck.md:127`: it verified the quote at line 232 and the defaults at 266-267,
not the generalisation).

## 2. Observation — what the pinned bytes actually do

`.ufo/waves/round-70/snapshots/S211-run_eval.py.txt` (sha256 `43e3b8f8…`, pinned at
`verifiers/check_skill_evals.py:53`):

| line | byte | consequence |
|---|---|---|
| 232 | `did_pass = trigger_rate >= trigger_threshold` | equality **passes** |
| 234 | `did_pass = trigger_rate < trigger_threshold` | equality **fails** (should-not-trigger) |
| 230 | `trigger_rate = sum(triggers) / len(triggers)` | rate = k / effective runs |
| 213-229 | `query_triggers[query].append(...)`, keyed by query **string** | effective runs multiply when a query text is listed twice |
| 225 | `query_triggers[query].append(False)` on exception | an infrastructure error is scored as a non-trigger |
| 266 | `--runs-per-query` default `3` | odd ⇒ no equality at 0.5 |
| 267 | `--trigger-threshold` default `0.5` | free flag; the cell's `only` does not mention it |

The guide's side is `"A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable
default)."` (`.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:92`), i.e. strict `>`. So the two rules
divergence set = `{ (runs, thr) : ∃k, k/runs == thr }` — exactly the entry's "threshold × runs is a whole number".

Two byte-level facts the facet adds beyond the entry (observed, not inferred):
- **Duplicate query text overwrites the label** (`:218` writes `query_items[query] = item` inside the
  `as_completed` loop, `:228` reads it back): two entries with the same `query` and contradictory `should_trigger`
  are scored under whichever arrives last, i.e. nondeterministically. The entry's Action line ("de-duplicate query
  strings", `:71`) incidentally removes this, but neither surface states it.
- **A raised run is a non-trigger** (`:225`), so a client timeout silently lowers a should-trigger rate and raises a
  should-not-trigger rate. No equality hazard at 0.5, but an audit that counts it as evidence of description
  behaviour is measuring its harness.

## 3. Falsification grid (executed derivation over the pinned branch)

Replicated only the two comparison lines above and enumerated `runs ∈ [2,6] × threshold ∈ {1/2, 1/3, 2/3, 1/4, 3/4, 1}`;
a point diverges when `code == True` and `guide == False` at `rate == threshold`:

```
(2, '1/2', '1/2', 'even')   (2, '1', '2/2', 'even')
(3, '1/3', '1/3', 'ODD')    (3, '2/3', '2/3', 'ODD')    (3, '1', '3/3', 'ODD')
(4, '1/2', '2/4', 'even')   (4, '1/4', '1/4', 'even')   (4, '3/4', '3/4', 'even')   (4, '1', '4/4', 'even')
(5, '1', '5/5', 'ODD')
(6, '1/2', '3/6', 'even')   (6, '1/3', '2/6', 'even')   (6, '2/3', '4/6', 'even')   (6, '1', '6/6', 'even')
total divergences: 14 | on odd run counts: 4
sanity: rate=2/3 thr=2/3 -> code True guide False
```

So the cell's `only at an even run count` is true exactly while `--trigger-threshold` stays `0.5`
(there `k/runs == 1/2 ⇔ runs` even). Four counterexample classes:

1. **`--trigger-threshold 2/3`, 3 runs** — the most natural audit rule, "at least two of three runs must trigger".
   Rate `2/3` ⇒ code passes, guide's "above" fails, at an **odd** run count. The cell tells the auditor this cannot
   happen.
2. **`--trigger-threshold 1/3`, 3 runs** — the mirror, "at least one of three".
3. **`--trigger-threshold 1`, any run count** — "must fire every time". Rate `1` equals the threshold at 2,3,4,5,6
   runs (4 odd points). Under the guide's wording *no* rate can be above `1`, so every should-trigger query fails;
   under the pinned code every query that fired in all runs passes. The strictest natural rule sits permanently
   inside the gap, and the cell's "even run count" clause says nothing about it.
4. **Duplicate query text at the default** — 6 effective runs, `3/6`, even; the only way the cell is true at the
   default (`:213-229`), and it is the reading the cell's neighbouring clause "defaults to 3 runs per query" invites.

Verdict on the facet: **scope defect, not a false statement about the default configuration.** A reader who trusts
the registry cell for calibration gets a rule that is wrong for every non-default threshold, including two of the
three rules an audit is likely to adopt.

## 4. Secondary, same family (lower confidence, labelled)

- **Authority name.** The cell says "disagrees with **the specification**", while the entry's authority note says
  the opposite (`corpus/knowledge/skill-eval-artefacts-round70.md:13-16`): "S209 and S210 are the skill-creation/
  **guides** on agentskills.io, **not the specification page** … Nothing below is a normative spec rule." The row's
  own `scope` cell (field 6) hedges "one implementation, **not the specification**", so the two cells in one row
  name opposite authorities for the same comparison. [OBSERVED: wording collision; INFERENCE: intent.] This is not
  only S211's problem — the r71 superseding rows call the same two guides "the open specification's own trigger-eval
  protocol" (`corpus/SOURCES.md:152` and `:153`, scope cells), so the lane holds two conventions and the entry
  contradicts both. One predicate set should cover all three cells.
- **Boundary of the r70 spot-check.** `corpus/lessons/round-70-verifier-spotcheck.md:127` admitted the row on the
  quote (line 232), the run default (266) and the threshold default (267). The generalisation in field 8 was not
  exercised, which is why it survived.

## 5. Control weakness — measured: nothing reads the cell

- `grep -rln 'S211' verifiers/` → `verifiers/check_skill_evals.py`, `verifiers/check_skill_evals_v2.py` (plus a
  `.pyc`). No other counter names this row.
- `check_skill_evals.py` reads the row at `:164` (`len(row) != 11`) and `:167` (`row[7] != "mined" or ENTRY not in
  row[10]`) — status and `used-by` only. The `teaches` cell is field index 6, never touched.
- `check_skill_evals_v2.py` parses `teaches` only for a `supersedes S0NN` marker (docstring `:37`) and requires an
  upstream-commit token in `anchor`; it does not evaluate the clause.
- Both are green on this cell today, and they disagree on everything else:

```
$ python3 -B verifiers/check_skill_evals.py --rev HEAD        # entry's own `recheck:` command (entry:8)
measured-rev: 65a5c7a663249e0522cc49e4a148424200d9ddfe
skill eval facts backed 1 of 8
  F1..F6: S212 has no pinned snapshot
  F7: S213 has no pinned snapshot
exit=1

$ python3 -B verifiers/check_skill_evals_v2.py --rev HEAD     # r71 successor, registered SKILL.md:505
measured-rev: HEAD
skill eval artefacts verified 10 of 10
exit=0
```

Two consequences worth recording beside the facet:
1. The entry's `recheck:` line (`:8`) names the v1 counter, which is **red at HEAD** — the entry's rows were
   re-pointed to `S212`/`S213` at `bf98d28` while v1 pins snapshots for `S209`–`S211` only
   (`verifiers/check_skill_evals.py:47-57`). Q04 ("every `recheck:`/source command resolves and runs today")
   is violated on this entry, and both `SKILL.md:503` (v1) and `:505` (v2) are still registered as gates.
2. Any new cell-reading arm belongs in a **new** counter or in a post-freeze successor, not in v1/v2: their
   judgment tables are frozen (Q28), and v1 is already red for an unrelated reason, so a red v1 cannot
   discriminate a teaches-cell defect.

## 6. Proposed check and its controls (design only — no file written)

`verifiers/check_s211_threshold_scope.py --rev <rev>`, exit 0 clean / 1 content verdict / 2 could-not-evaluate, all
inputs from committed bytes at `--rev` (snapshot sha256 verified first, as v1 does: tamper ⇒ exit 2). Frozen at the
plan commit; the grid and the two comparison lines are transcribed from the pinned snapshot, never read from the
measured tree.

| id | predicate | kills |
|---|---|---|
| A | row `S211` is 11 cells, status `mined`, `used-by` names the entry (reuse, not re-implement, v1 `:164-167`) | row removal/renumber |
| B | every clause of `teaches` that mentions a run count also names the threshold condition, **inside the same clause** (split on `;`/`,`): `--trigger-threshold`, `threshold × runs`, or `at the default 0.5`; prints `s211 teaches: threshold condition named` | current bytes; a qualifier appended as a dangling token elsewhere in the cell |
| C | the cell's asserted scope covers every point of the frozen grid G (`runs ∈ [2,6] × thr ∈ {1/2,1/3,2/3,1}`) computed from snapshot `:232`/`:234`; on failure prints the first uncovered point, e.g. `runs=3 threshold=2/3 rate=2/3: code pass, guide fail` | "only at an even run count" as a general claim |
| D | the authority named in the cell resolves to `S213`'s page; a cell saying `the specification` fails while entry `:13-16` says guides-not-specification (or the cell must say `the guide's wording` as entry `:58-60` does) | the authority collision in §4, on S211 `teaches` and on `S212`/`S213` scope cells |

Self-test contract (Q48, both directions) — every arm drives `main()`:

| arm | fixture | required |
|---|---|---|
| T1 | appended superseder row with the corrected clause ("at the default 0.5 threshold, exactly the even run counts; otherwise whenever threshold × runs is a whole number") | exit 0 + the exact line `s211 teaches: threshold condition named` |
| T2 | bytes at HEAD | exit 1 + prints `runs=3 threshold=2/3 rate=2/3` |
| T3 | current cell with ` threshold × runs` appended after a semicolon | exit 1 (B must be structural, not token-presence: Q25/Q37 real-text shortcut) |
| T4 | cell with `only at an even run count` **deleted** and no condition added | exit 1 (deletion is not a repair; C requires positive entailment) |
| T5 | row absent | exit 1 (content verdict), snapshot sha mismatch | exit 2 |

Kill rule: T1 green while any of T2/T3/T4 is green ⇒ the check is a lexeme probe; fix before any data is scored.
Equivalent world that must stay green (two-sided, Q47): the corrected clause reworded without the `only` family of
tokens.

**Bound (Q51).** The check reads the cell's words and the pinned branch only. It cannot decide whether the guide's
"above" was meant as a strict inequality at the threshold (the page never discusses equality,
`S210-optimizing-descriptions.md:92`) nor which rule an audit *should* adopt; those are named non-author
judgements. It also cannot see the harness behaviours of §2 beyond the transcribed lines.

## 7. Repair channel and risks

- **`teaches` is a protected cell.** `verifiers/check_sources_append_only.py:11-14` makes a protected-cell change
  "every column except status, recheck, used-by" a breach (exit 1). The repair must therefore be an **appended
  superseder row** whose scope cell begins `supersedes S211 — …` (18 such rows exist: `grep -c 'supersedes S'
  corpus/SOURCES.md` → `18`; `S212`/`S213` are the exact same-URL precedent, `corpus/SOURCES.md:152-153`).
- **Census risk, unmeasured.** A second row for the same URL may add a duplicate-URL warning; the census lives at the
  fleet root (`scripts/sources-census.sh` under `/home/vgpnk/Projects/shokunin`, absent from this lane), outside
  this seat's write and measurement scope. Measure before promising a clean census.
- **Q28 risk.** Adding arm D to a frozen counter is a second measurement, never the declared one; the clean channel
  is a new counter file plus its own plan-time freeze.
- **The red v1.** If the entry's `recheck:` is left naming v1, no round can cite this entry as re-checked; the fix is
  a one-line re-point to v2 plus the Q04 evidence, but that line is *not* protected (recheck is exempt), so it can be
  edited in place — the cheapest repair in this report.
- **No live evidence.** No fetch and no `run_eval.py` execution (no model experiments permitted this wave): the 14
  divergence points are a static derivation from the pinned branch, and the audit consequence in §3 is that
  derivation applied to three threshold choices, not an observed client run.

## 8. Retained evidence

```
sed -n '157p' corpus/SOURCES.md | fold -w 200          # cell 8 = the teaches clause above
awk -F'|' 'NR==157{print NF}' corpus/SOURCES.md        # 13 → 11 data cells
grep -n 'did_pass\|runs-per-query\|trigger-threshold\|append(False)\|query_items' \
  .ufo/waves/round-70/snapshots/S211-run_eval.py.txt   # 213,214,218,225,232,234,266,267
sed -n '92p' .ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md   # guide wording "above a threshold"
python3 -B verifiers/check_skill_evals.py --rev HEAD          # "1 of 8", exit 1
python3 -B verifiers/check_skill_evals_v2.py --rev HEAD       # "10 of 10", exit 0
grep -rln 'S211' verifiers/                                   # the two counters only
grep -c 'supersedes S' corpus/SOURCES.md                      # 18
grep -n 'even run count' corpus/SOURCES.md corpus/knowledge/skill-eval-artefacts-round70.md  # 157 (cell), :66 (entry)
```

Grid and branch-enumeration code: two comparison lines transcribed from snapshot `:232`/`:234`, `Fraction`-exact
enumeration, output as printed in §3.

## 9. Refusals

No claim is made that the guide is wrong or that the code is right, that any client runs `evals/evals.json`, that
the audit should adopt a particular threshold, or that the census counts a superseder as distinct — none of these
was measured. The facet is the scope of one committed cell against one committed entry paragraph, plus the measured
fact that no counter evaluates either.
