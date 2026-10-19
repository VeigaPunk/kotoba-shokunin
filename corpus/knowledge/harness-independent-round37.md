# Independent harness re-derivation — round 37 (C1)

Round 37's depth move is the harness counterpart of round 12: the **28 pinned
harness checks stop being author-only**. `AXES.md`'s band 10 asks for repeated
non-author verification in the opposite direction; rounds 10–23 built the
harness gate, its baseline and its pin guard, all author-side. So a
**source-blind instrument re-derives the expected values from the raw
substrates** (ELF bytes, sqlite, the opencode log, the skill roots), a third
driver joins the two check-for-check, and every disagreement is adjudicated
here rather than explained away.

Round 37 landed this **unverified**: the comparator exited 1 at 23/28 with 5
open rows, the corpus doc was absent, and the counting command is
copy-satisfiable (R1). Round 38 closed it — the two adjudicated rows were fixed
in the instrument, the three blindness-blocked rows are declared scoped out by
the instrument itself, and the driver now exits 0 over the landed scope. This
file records the closure: the adjudications and their probes, the scope-out and
its validation, the freeze-before-compare receipt, and the blindness-by-
construction scrub.

**What the exit 0 does not mean (round 40, seat W1 — the honest state).** The
24/24 is real over the landed scope, but it is **not** evidence that a copier
cannot reach it, and the class round 39 meant to close survives in channels the
three locks do not cover. Measured at the round-40 dispatch state (HEAD
`1c32b43`, driver `bb8dcecd`, IND `872993f8`; probe
`.ufo/round-40/drafts/w1/probe-channels.py`, transcript `probe-preland.txt`):
ten attack payloads built from the live instruments' own captures all read
**exit 0 / 24/24** while the same divergence placed in the channel the driver
actually reads reads exit 1. The named survivors:

- **F-2 (r39 R1, HIGH).** `IND_VALUE_KEYS` accepts `expected`/`expected_value`
  first, and the live IND never emits them, so a record carrying the harvested
  value in `expected` and `"NOT DERIVED"` in both derived fields is scored as
  derived agreement.
- **F-3 (r39 R1, MEDIUM).** `_record_list` returns the first of
  `results`/`rows`/`checks`; the other two are never cross-checked.
- **Round 40 additions, same class, measured by this seat on the same bytes:**
  the top-level `landed`/`unlanded` counts are unread; a **committed** scoped
  row may carry a divergent value beside its `SCOPED_OUT` flag (the flag, not
  the value, decides the row leaves the join); the probe `target` is
  payload-chosen (the committed scope file stores `kind`+`reason` only, no
  target — measured), so a payload-built census tree satisfies the recomputation;
  a `state` alias shadows `status`; a stringified value in a shadow channel is
  invisible; and a duplicate id divergent-first is dropped.
- **The scope-file CWD door (round 40, R1 filed, W1 reproduced).**
  `load_scope_file(args.scope_file)` resolves the path against the **process
  CWD** while the receipt records its digest against `--cwd`, so a driver run
  from a planted directory enforces a *different* scope file than the receipt
  attests: exit 0, 5 rows scoped out, while the receipt's own `sha256` names the
  honest 4-row repo file. Reproduction:
  `.ufo/round-40/drafts/w1/cwd-door.py` → `cwd-door-preland.txt` (arm A exit 0,
  arm B control exit 2, arm C digest mismatch).

So the reader should treat §1's exit 0 as **conditional on the payload being
honest**, which is the opposite of what a counter-instrument is for. The
pending C1' fix (round 40) is aimed at F-2/F-3; whether it closes the wider
class is a measurement, not an expectation — see §5.

| | author's instrument (HAR) | independent derivation (IND) |
|---|---|---|
| file | `verifiers/verify_harness_claims.py` | `verifiers/verify_harness_independent.py` |
| sha256 | `6b8eb4b6e85b1640cbdbfedd10a6ee9055923caaad226736e7f672e8dff934f3` | `872993f875338f4f…` (round 39: the init_count predicate fix and seat P1's scoped-row probes landed here; `82ad9700a59cf7cf…` is the r38-closure sha this doc was written against) |
| author | r10/r23 lanes (author side) | round-37 builder seats, blinded to the harness source, `baseline.json`'s harness rows, and corpus docs quoting them |
| self-test | `--self-test` → `0 failure(s) over 10 assertions` | `--self-test` → `0 failure(s) over 104 assertions` (86 at the r38 closure; 93 after the round-39 init_count grammar fixtures; 104 after seat P1's scope-out probe battery) |
| exits | 0 pass · 1 drift · 2 inconclusive · 3 no baseline | 0 clean · 1 drift (`--freeze`/`--observed`) · 2 environment unreadable |
| join driver | `verifiers/compare_harness_independent.py`, sha256 `bb8dcecd65f160d3…`, `--self-test` → `0 failure(s) over 97 assertions` (83 at the r38 closure, 93 mid-round-39) | same driver, mode-aware headline + strict column, `--receipt` (freeze receipt) |

**Round 41 calibration erratum (append-only; join-driver row).** The table's
`bb8dcecd…` / 97-assertion stamp is an earlier snapshot, not the settled r40
or current comparator. At HEAD `b1be35f9522f21c0c5b39879358a011806ab9200`
(tree `8bb24450a9c500c427019c7147013b4946525b09`),
`sha256sum verifiers/compare_harness_independent.py` is
`1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76`;
`python3 verifiers/compare_harness_independent.py --self-test` returned
`0 failure(s) over 118 assertions`, exit 0, and the live comparator returned
24/24 (strict 20/24; 4 adjudicated, 4 scoped out), exit 0. The old 97 remains
as a historical reading; it is not the current self-test count. The round-39
93/floor=93 reading below is also historical to that measurement.

**Adjudication ledger.** The r38 witness seat's rulings for the rows this file
adjudicates are at `.ufo/round-38/evidence/a1-adjudication-ledger.md`
(rows `adj-r38-01` … `adj-r38-14`). §3 below and that ledger are the two records
of the same rows; where they differ, this file was the stale one — round 39
re-files `oc.log.init_count_monotone` under its true class per that ledger's
row 3 (see §3).

Agreement predicate (round-37 C1 adjudication protocol §2, frozen before the
first join): `equal` → value equality; `zero` → both readings empty; `positive`
→ inequality direction. Strict type-tagged equality is published beside it.
All numbers below were re-measured at write time (2026-10-19; the r38 closure
at HEAD `cb4e0f3`, IND `82ad9700…`, driver `c1538342…`; the round-39
init_count re-filing at IND `872993f8…` against driver `8cfdefdf…`) by the
commands in §6.

**Measurement stamp, not a pin.** Both C1 instruments were edited by sibling
seats while this file was written (IND moved `27ae80ae…` → `82ad9700…`, then
`872993f8…` at round 39; the driver `de2bd8ab…` → `0f7f59e8…` → `c1538342…` →
`8cfdefdf…`, with identical headline `24/24, exit 0` at the last three). Every
number here is stamped with the sha it was measured on; the shas are re-read
from `git status`-visible working bytes, so a reader re-running §6 after the
round lands should expect the assertion counts to have moved and must
re-measure before quoting them. The round-39 counts were re-read a second time
after the sibling edits settled, and the floors guard was re-run at that state
(`PASS harness_independent observed=104 floor=104`, `PASS
compare_harness_independent observed=93 floor=93`, exit 0).

## 1. The claim this round lands

*Live tree*: the driver prints
`agreement: 24/24 (mode-aware protocol headline; 28 live checks, 4 scoped out by
the independent instrument)`, `strict 20/24`, `adjudicated rows: 4`,
`disagree: 0`, `scoped-out: 4`, and **exits 0** — `all checks agree, both
instruments green`. The after-state the claim declares is met **over the landed
scope**, and the scope is declared by the instrument itself, not by the driver.
(Round 39 moved the strict column 19 → 20 and the adjudicated set 5 → 4: the
`oc.log.init_count_monotone` pair used to agree only because both sides were
empty; with the predicate fixed the row is a list-vs-list agreement, so it left
the adjudicated column rather than changing the headline.)

*The round-37 state* (the reason this file exists): the same driver at
`de2bd8ab…` against IND `27ae80ae…` printed `23/28`, `disagree: 5`, exit 1.
The 5 rows were the two adjudications below plus the three catalogue rows. The
closure is therefore traceable, not asserted: each row has a probe, a ruling,
and a landed change.

*Mutant tree* (a fabricated `init count` / duplicate-name log fed to both
instruments via their own `--oc-log` flags; round-39 re-measurement, log kept at
`.ufo/round-39/drafts/p2/fixtures-oc-log-mutant.log`): both instruments move;
the driver reports `24/24`, exit 3, naming the *live* side's own non-PASS rows
(`oc.dup.roots_both_sided`, `oc.log.init_count_max`) — the init_count rows are no
longer disagreements, because round 39 gave IND the same occurrence grammar and
the same violation rendering as HAR (before the fix the same leg read `21/24`,
exit 1, `init_count_max (2 vs 5)` and `init_count_monotone (1 vs [])`).
*Frozen-vs-mutant* (the frozen receipt against the mutated live side): `21/24`,
exit 1, naming the same class set from the frozen values
(`init_count_max 0 vs 5`, `skills_rescan_max 3 vs 2`) — the semantics the
claim's after-text requires, and the reason the freeze receipt is load-bearing.

## 2. Agreement, check for check

Live tree. `ind` = IND's re-derivation, `har` = HAR's live observation,
`pin` = the baseline expect. `OUT` = declared scoped out (§3). Full
four-number blocks (one line per row, with the pin column) are reproduced by
§6's `four-number-blocks` command.

| # | check | mode | ind | har | pin | agree |
|---:|---|---|---|---|---|---|
| 1 | `oc.dup.onesided_roots` | zero | `0` | `[]` | `[]` | yes |
| 2 | `oc.dup.roots_both_sided` | equal | `0` | `0` | `0` | yes |
| 3 | `oc.log.available_skills_hits` | zero | `0` | `0` | `0` | yes |
| 4 | `oc.log.init_count_max` | equal | `0` | `0` | `0` | yes |
| 5 | `oc.log.init_count_monotone` | zero | `[]` | `[]` | `[]` | yes |
| 6 | `oc.log.skills_rescan_max` | equal | `3` | `3` | `3` | yes |
| 7 | `oc.log.skills_tag_hits` | zero | `0` | `0` | `0` | yes |
| 8 | `oc.permission.skill_allow` | equal | `0` | `0` | `0` | yes |
| 9 | `oc.permission.skill_lines` | equal | `0` | `0` | `0` | yes |
| 10 | `oc.roots.names_plus_builtin` | equal | `7` | `7` | `7` | yes |
| 11 | `oc.roots.plugins_cache` | zero | `0` | `False` | `False` | yes |
| 12 | `omp.cache.keys_reproduced` | equal | `7` | `7` | `7` | yes |
| 13 | `omp.cache.misses` | zero | `0` | `0` | `0` | yes |
| 14 | `omp.cache.verified_skills` | equal | `7` | `7` | `7` | yes |
| 15 | `omp.catalogue.found` | equal | `None` | `True` | `True` | **OUT** |
| 16 | `omp.catalogue.matched` | equal | `None` | `7` | `7` | **OUT** |
| 17 | `omp.catalogue.missing_names` | zero | `None` | `[]` | `[]` | **OUT** |
| 18 | `omp.catalogue.total` | equal | `None` | `7` | `7` | **OUT** |
| 19 | `omp.db.rows` | equal | `14` | `14` | `14` | yes |
| 20 | `omp.db.rows_wellformed` | equal | `14` | `14` | `14` | yes |
| 21 | `omp.descriptions.missing` | zero | `0` | `[]` | `[]` | yes |
| 22 | `omp.descriptions.over_cliff` | positive | `7` | `7` | `7` | yes |
| 23 | `omp.descriptions.unmodelled` | zero | `0` | `0` | `0` | yes |
| 24 | `omp.elf.template_bytes` | equal | `273` | `273` | `273` | yes |
| 25 | `omp.elf.template_sha256` | equal | `c1f03c8e…db51` | `c1f03c8e…db51` | `c1f03c8e…db51` | yes |
| 26 | `omp.names.mismatches` | zero | `0` | `[]` | `[]` | yes |
| 27 | `omp.offered.dangling` | equal | `0` | `0` | `0` | yes |
| 28 | `omp.offered.skills` | equal | `7` | `7` | `7` | yes |

**24/24 over the landed scope** (4 scoped out); the strict type-tagged column
is 20/24 — 4 rows agree under the mode predicate while their encodings differ
(`0` vs `[]`, `0` vs `False`), and the driver names all 4. A naive `!=` check
scores 21/24 on the same data because Python's `0 == False` is true; that is
exactly the type laundering the driver's strict column exists to catch, so the
driver's number is the one quoted here. HAR's own live verdicts are `28/28 checks pass`, exit 0, in the same run — the
two are answers to different questions (drift-from-pin vs independent
re-derivation), and only the second is this round's claim.

Raw populations, measured with the writer's own extractors: the opencode log
(922 296 B) contains **0** literal `<skills>`, **13** `skills="` attributes,
**13** `skills rescanned` lines, **0** `duplicate skill name` lines, **0**
`init count` lines, **0** `<available_skills>`; the 13 rescan arrays repeat
exactly 3 names (`shokunin`, `swarm`, `tower`). The session tree holds **763**
`.jsonl` files; **620** carry at least one `<skills>` block; **678** candidate
blocks; **534** pass the harness's own gate, every one totalling 7 lines. The
cache holds 14 rows; an independent frontmatter read plus the binary's own key
formula reproduces **7/7** keys — but only with clip-chomped folded scalars
(a naive space-join yields 1/7, the defect class V2 found and the builder
repaired). The newest qualifying catalogue (`2026-10-15T05:02:56.169Z`) matches
**7/7** cached descriptions.

## 3. Adjudications

One row per disagreement or definitional difference. The r38 witness seat's
rulings for these rows are the **adjudication ledger** at
`.ufo/round-38/evidence/a1-adjudication-ledger.md` (rows `adj-r38-01` …
`adj-r38-14`, one class/readings/probe/ruling/action/`blind:` block per row);
this section is the corpus-side record of the same rows, and the round-39
re-filings below supersede the labels this file carried at the r38 closure.
The probe outputs quoted by the r38 rows lived under `.ufo/round-38/drafts/w1/`,
which the r38 integrator pruned (`.ufo/round-38/evidence/PRUNE.log`); every
number a reader wants to check is re-derivable by the commands in §6. A row
without a probe is not a ruling.

**adj-r37-01 — `oc.log.skills_tag_hits` (D2, definitional → fixed).**
At the round-37 state IND derived **13**, HAR observed **0**. Hand probe:
`grep -c -o '<skills>' <log>` → **0**; `grep -o 'skills="' <log> | wc -l` →
**13**. The id's name and its extractor sentence say `<skills>` (an XML
literal); IND was counting the attribute form and said so in its own evidence
text. Ruling: **definitional, harness side wins the id**. Landed action: IND
now derives `0` and carries the adjudication in its docstring; the row agrees.
Blind: `source-read(author)`.

**adj-r37-02 — `oc.dup.roots_both_sided` (D2, definitional → fixed).**
IND derived **3**, HAR observed **0**. Hand probe:
`grep -c 'duplicate skill name' <log>` → **0**; the 3 was names repeated across
rescan arrays — a different population from HAR's `existing=`/`duplicate=`
per-root split. Ruling: **definitional, harness side wins the id**. Landed
action: IND re-scoped to the duplicate-name grammar and now derives `0`. Blind:
`source-read(author)`.

**adj-r37-03/04/05 — `omp.catalogue.{found,total,matched,missing_names}`
(D4 presence asymmetry → formally scoped out).** IND published `None` with
`status=UNLANDED`. The catalogue carrier's selection rule (which session file's
block is *the* catalogue) lives inside the harness's own authored scope, so a
source-blind builder cannot derive it without reading the rule it must not
read. The substrate value is not in doubt — the writer's own gate + scan
reproduces `total=7, matched=7, missing=[]` at the newest qualifying catalogue,
and HAR reads the same. Ruling: **these four rows are OUT of the independent
instrument**, declared by the instrument itself with a non-empty reason per id
(its `scoped_out` map), and they **may not fold into any agreement count**.

The scope-out is validated loudly, not trusted (probes re-run at write time):

```
$ python3 verifiers/compare_harness_independent.py --independent-json ind-bad-scope.json
ERROR: independent: scoped_out names omp.db.rows but its status is 'DERIVED', not 'SCOPED_OUT'   exit 2
$ python3 verifiers/compare_harness_independent.py --independent-json ind-empty-scope.json
ERROR: independent: scoped_out is present but empty (declare the set or omit the key; an empty
declaration is ambiguous)                                                                        exit 2
```

So a scope-out cannot hide a derived row, cannot be an empty gesture, and
cannot be a way to make a check disappear quietly. Deleting the rows from the
payload instead is exit 2 (`uncovered checks`), never agreement.

**adj-r39-01 — `oc.log.init_count_monotone` / `oc.log.init_count_max` (D1, defect(independent) → fixed).**
The r38 witness ledger's row 3 (`adj-r38-03`) ruled IND's predicate a
`defect(independent)`: IND counted *runs carrying more than one `init count`
line* while the id names *decreases between consecutive counts* — the opposite
predicate over a different population, invisible live because the opencode log
carries **0** `init count` lines. R1's counter-probe and V1's mutant leg
(`.ufo/round-38/scouts/R1.md` F-3, `V1.md` DEFECTS 2) both named the sibling
divergence on `init_count_max` as unadjudicated; A1's erratum `adj-r38-14`
already flagged the comparator's own `adjudicated_rows` label as the smoothing
trap. Round 39 re-files both rows under **D1** here and lands the fix:

```
# before (predicate), on a log whose counts only grow (1,2) -- no violation exists
HAR init_count_monotone_violations = []            IND oc.log.init_count_monotone = 1
# after, same log
HAR init_count_monotone_violations = []            IND oc.log.init_count_monotone = []
# a real decrease, both sides, same rendering
HAR ['3->2', '2->1']                               IND ['3->2', '2->1']
# the non-grammar form the old fixture used (message="init count" value=N)
HAR 0                                             IND 0   (was: IND 2)
```

Landed action: both rows derive from one `message=init count=(\d+)` occurrence
sequence in file order (`verifiers/verify_harness_independent.py:517-552`), the
violation is rendered `a->b` as HAR renders it, and the self-test's
bug-restating arm (`1` where the predicate requires `0`) is replaced by five
true discriminators (increasing ⇒ `[]`; decrease ⇒ `['3->2']`; cross-run
decrease ⇒ `['2->1']`; quoted form ⇒ `0`/`[]`; max = largest, not last).
Self-test 86 → 93 assertions; floor bumped in-step (86 → 93). Fixture-backed
logs: `.ufo/round-39/drafts/p2/{mut-hargrammar-inc,mut-hargrammar-dec,mut-quoted,mut-hargrammar-crossrun}.log`.
Blind: `source-read(author)` (adjudicating seat).

**Zero-delta representation rows (D5, cosmetic).** `[]` vs `0`
(`oc.dup.onesided_roots`, `omp.descriptions.missing`, `omp.names.mismatches`),
`False` vs `0` (`oc.roots.plugins_cache`). Same population, different emptiness
encoding; the driver's `zero` predicate handles them and publishes the strict
column beside it. No action. (`oc.log.init_count_monotone` stood in this list
until round 39; it was removed because its two readings were *different
predicates*, not two encodings — see adj-r39-01.)

**Mode source (D5, named).** `verify_harness_claims.py`'s `CHECKS` table and
`baseline.json` disagree on exactly 2 ids: `oc.permission.skill_lines` and
`oc.permission.skill_allow` are `at_least` in the baseline, `equal` in the
code, and `evaluate()` honours the code and ignores the baseline's mode. The
independent instrument and this file read modes from the **code table**; the
divergence is named so a future reconciler against the baseline's advertised
modes is not read as a defect.

## 3b. Shared properties and the controls

**The headline is copy-satisfiable (R1's counter-instrument, re-run here).**
`R1-counter_blind.py` opens no forbidden artifact: it harvests
id/mode/expected from the harness's own `--json` stdout, re-observes with
`--no-baseline`, and scores **28/28 mode-semantics agreement, 28/28 exact-value
matches, exit 0**. So N/N discriminates *drift*, not *independence*; what
certifies independence is the blindness evidence (§4) plus the fact that the
derivation produced a 5-row divergence at a state where a copier would have
produced 28/28 — the divergence was the evidence, and closing it removed the
only such signal this round can point at.

**Vacuity is quantified.** A null instrument (`null_echo.py`, every id → 0,
reads nothing) collects **15/28** under the mode-aware predicate (13
disagreements, exit 1) — 54% of the headline is available for zero content via
the `zero`-mode predicate. The headline must therefore always be read with the
strict column and the adjudication table beside it.

**Mutant behaviour.** On the fabricated log both instruments move and the
driver exits 1 naming them (§1). The frozen arm is what flips *and* names, which
is R1's structural point made executable.

**Pre-existing red, found at write time and since closed (re-measured round 39).**
At the r38 write time `python3 verifiers/verify_skill_checklist.py` **exited 1
at HEAD bytes**: `FAIL governance.citation_resolves … SCORECARD.md:131,132,133`
— the round-37 rows' brace-glob citations
(`.ufo/round-37/scouts/{P5,P6,V4,V5,I1,I2,S2}.md`) were not expanded by the
gate's brace-unaware citation predicate (`SCHEMATIC_CITATION_RE` covers `round-N`
only). Round 38 reworded those SCORECARD rows and the gate now **exits 0**
(`grep -c 'scouts/{P5,P6' SCORECARD.md` → `0`; `python3
verifiers/verify_skill_checklist.py; echo $?` → `0`), with `--self-test`
green at `0 failure(s) over 1597 assertions`. The red was a live-gate defect in
the then-committed bytes, recorded here rather than smoothed; this paragraph is
the record of it, not a live claim.

## 4. Blindness — method and scrub residual

Blindness is **by construction, with a countable residual**, not an
attestation. `R1-make_blind_tree.sh` builds a worktree from `git archive HEAD`
(no `.git/` → the history channel is closed), removes the harness source and
`__pycache__`, reduces `baseline.json` to pin-shaped keys only (its prose notes
leaked `keys_reproduced=7`, `17→7`), deletes the docs that quote the pin set,
and drops `.ufo/` (prior-round fragments quote the pins). Re-run at write time:

- **pin-value residual = 5 (round 40; was 4 at the r39 write time, 0 at r38)** —
  the five files the scrub now reports are `verifiers/verify_harness_independent.py`,
  `verifiers/harness-independent-scope.json` (its blocker prose names
  `omp.catalogue.matched`), its two fixtures
  (`verifiers/fixtures/harness-independent/{oc-log,omp-cache}/case.json`) and
  **this document**, which quotes the pinned stdout forms in its own §1–§2.
  The doc is new to the surface (the script's delete list is a measured
  inventory taken before this file existed, so the doc survives the scrub) and
  is the honest case: a file that publishes the pins belongs in the surface, so
  it is counted, not waved away. The others are the builder's own artifacts
  naming their own rows; none is harness source. (The script prints
  `harness_pin_residual_count=5`; at the r38 write time its token list predated
  these landed artifacts and printed 3.)
- The scrubbed tree still **runs green**: with the current instrument and
  fixtures copied in, `24 derived, 4 scoped out, 0 unlanded`, exit 0,
  `--self-test 0 failure(s) over 104 assertions`; the pins guard runs inside it
  (`exit 0`); the substrate stays reachable (the db is outside the repo);
  `tree_files=340`, `dot_git_present=no`. The driver inside the scrub tree
  fails closed on the (correctly) absent harness — `ERROR: live instrument
  failed with no stdout … exit 2` — which is the scrub working as designed.

**Round 41 calibration erratum (append-only; §4 scrub rerun).** The `340`
`tree_files` and nested pins-guard `exit 0` above are a round-40 snapshot, not
current. Re-running the committed script
`bash .ufo/round-37/evidence/R1-make_blind_tree.sh <fresh-temp-dir>` at
`2026-10-19T13:37:10-03:00`, using `HEAD b1be35f9522f21c0c5b39879358a011806ab9200`
(tree `8bb24450a9c500c427019c7147013b4946525b09`), produced
`harness_pin_residual_count=5`, `tree_files=358`, `dot_git_present=no`, and
`pins_guard_in_scrub_tree=NONZERO`; the scrub-builder itself exited 0. The
script's SHA-256 is `077211322ba8bd2c7d14f0272dd20b1cd21761135369343049b0b34cc22fc298`
(committed blob `225fcd31e8f46cd40a94c9fa803e53e0c869db88`). Direct
`python3 verifiers/check_substrate_pins.py` at the same HEAD/worktree returned
exit 1 (`DRIFT 2/3`): omp SHA expected `bf1e86a9…`, observed `9513ef9f…`, and
mtime delta `285644401942067 ns`; the opencode SHA pin passed. This is live
host-substrate drift, not a repository edit. The 104 IND assertions and 24/24
join remain green; the old nested pins-guard result is retained as its earlier
snapshot, not a current green.

**Freeze-before-compare receipt.** The driver's `--json` output channel
republishes each id's pinned `expected`, so "source-blind" must cover the
output channel: a builder that reads the per-check table before freezing has
contaminated its own derivation. Receipt: IND captured with `--write-freeze` to
`ind-freeze.json`, sha256 `09fb71ca5e79d7f1…`, mtime `10:43:17.517`; the harness
capture (`har-live.json`, sha256 `f25e960303d30277…`) landed at `10:43:14.042`
— in this round the freeze is a *re-freeze* at the settled instrument sha, and
the joined run consumed the frozen file with the same `24/24, exit 0`. At the
round-37 state the ordering was measured forward: IND freeze `01fd40ef…` at
`10:34:00.883` preceded the harness capture at `10:34:01.637`. This is a
*narrowing*, not a proof; the residue is stated in §5.

## 5. What is still not verified

- **The green is scope-conditional.** `24/24` is over the landed scope; 4 of
  28 live checks are excluded by the instrument's own declaration. A reader who
  quotes the headline without the scope is quoting a different claim, which is
  why §1 quotes the driver's full line.
- **The green is also payload-conditional (round 40, seat W1).** Ten attack
  payloads reach exit 0 / 24/24 against the driver at the round-40 dispatch
  state (the F-2 and F-3 channels plus the seven round-40 additions named in
  the header note), while the same divergence in the read channel is named.
  A green from this driver therefore bounds *drift between two honest
  instruments*, not a copier's ability to satisfy the join. Measured:
  `.ufo/round-40/drafts/w1/probe-channels.py` at driver `bb8dcecd` (transcript
  `probe-channels-preland.txt`); the round-40 C1' landing is aimed at the first
  two of these, and the rest stand until measured closed.
- **The probe target is payload-supplied.** The committed
  `verifiers/harness-independent-scope.json` stores `kind` and `reason` per
  scoped row but no `target` (measured: `sorted(entry)` → `['kind', 'reason']`
  for all four rows), so the census the driver recomputes is computed over the
  tree the *payload* names. A payload that builds a tree with a spread of
  totals satisfies `distinct_totals >= 2` and keeps its scope-out. The
  `false blocker` classes catch a vacuous or single-total surface, not a
  fabricated one.
- **The scope-file path is resolved against the process CWD.** `--scope-file`
  is opened relative to the process CWD while the receipt's `scope_file.sha256`
  is computed relative to `--cwd`, so the enforced set and the attested digest
  can describe different files (round 40: exit 0 with a 5-row planted set,
  receipt digest = honest 4-row file). Repro `.ufo/round-40/drafts/w1/cwd-door.py`.
- **Agreement falsifies implementations, never specs.** A second same-spec
  instrument inherits the class spec's scope choices; the 24/24 is evidence
  about two implementations, not about the substrate model. The adjudications
  moved *IND* to HAR's reading in every row decided so far — the harness side
  has won each one — so this comparison has never falsified the author
  instrument on a value. Round 39's init_count ruling is the fourth such move
  (the r38 ledger's rows 1-3 plus this pair) and the first where the two
  readings had been *predicates* rather than populations.
- **The r38 ledger's own §6 is a dispatch-state transcript, not a live command
  set (round-39 reconciliation).** Its `compare_harness_independent.py` line is
  annotated `exit 1, 23/28, 5 disagreements`, which is the state at IND
  `27ae80ae…`; at the settled state it prints `24/24`, `disagree: 0`, `exit 0`.
  The ledger says so in its own footnote and pins both ends in
  `final-state.txt`/`freeze-receipt.txt`, so the two records agree — but a
  reader who runs the ledger's block expecting exit 1 at the current tree will
  see exit 0, and that is the ledger's stale end, not a regression. This file
  is the live record; the ledger is the r38 witness's ruling set.
- **The r38 ledger's `blind:` and probe pointers name pruned drafts.** Every
  `drafts/a1/*` and `drafts/w1/*` path in `.ufo/round-38/evidence/`'s ledger is
  gone (`.ufo/round-38/evidence/PRUNE.log`); the rulings survive, the probe
  transcripts do not. Where this file quotes a r38 probe number it is quoting
  the ledger, and §6's commands re-derive the live ones.
- **Two rows are known-defective on the harness side and still pass.**
  `oc.roots.plugins_cache` reads two different paths (HAR `~/.claude/plugins/cache`,
  IND `~/.config/../.cache/opencode`) and agrees only because both are empty —
  the r38 ledger's unclosed erratum `adj-r38-14`, and not this seat's to fix.
  A one-sided plant moves HAR alone; the agreement is coincidental, not measured.
- **The driver's disagreement line can print identical values.** On a `zero`-mode
  row whose readings are non-empty *and equal*, the line reads
  `expected ['3->2','2->1'], observed ['3->2','2->1']` — the verdict is correct
  (a `zero`-mode row with a non-empty reading is a failure) but the rendering is
  self-contradictory to a reader. Measured round 39 on the decreasing mutant log
  (`.ufo/round-39/drafts/p2/`); not introduced by the predicate fix, which merely
  made such a reading reachable for the first time.
- **Blindness is attested plus structural.** The scrub bounds the *file*
  channel; the `--json` output channel is bounded by the freeze receipt; a
  negative (nobody read the source) is still not provable from inside the repo.
- **The instruments are host-anchored** (absolute default paths for the omp
  binary, db, log, roots), so a clone's run needs the flags — the same
  hermeticity caveat r12 recorded for the corpus pointers.
- **`oc.roots.names_plus_builtin`'s built-in term is declared 0** in both
  instruments (the string `customize-opencode` is absent from the binary); a
  future binary carrying it would move both readings together, un-adjudicated.
- **`R1-make_blind_tree.sh`'s r37 depth bug is repaired in the committed copy
  (re-measured round 39).** The r37 evidence copy resolved its repo root one
  level too high (`$HERE/../../../..` from `.ufo/round-37/evidence` landed on
  the parent directory), so it archived the wrong tree; round 38 rewrote it to
  walk up until `verifiers/verify_harness_claims.py` is found. The committed
  script now runs from its own path — round-39 re-run:
  `bash .ufo/round-37/evidence/R1-make_blind_tree.sh /tmp/blind-tree` →
  `repo=/home/vgpnk/Projects/shokunin/kotoba-shokunin`,
  `tree_files=338`, `harness_pin_residual_count=4` (see §4). The r38 note that
  the fix lived only in a pruned draft copy is superseded by the repair.

**Round 41 calibration erratum (append-only; §5 historical scrub count).**
The `338` / residual `4` above remain the explicitly dated r39 reading; they
are not the later §4 or current count. The r40 §4 snapshot is `340` / `5`, and
the frozen committed-HEAD rerun at `b1be35f9522f21c0c5b39879358a011806ab9200`
(tree `8bb24450a9c500c427019c7147013b4946525b09`) is `tree_files=358` /
`harness_pin_residual_count=5` (`bash
.ufo/round-37/evidence/R1-make_blind_tree.sh <fresh-temp-dir>`, exit 0;
script SHA-256 `077211322ba8bd2c7d14f0272dd20b1cd21761135369343049b0b34cc22fc298`).
The r39 values are retained as history; this note supplies the current value
for readers following the `see §4` pointer.

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
# both instruments, both directions
python3 verifiers/verify_harness_claims.py            ; echo "HAR exit=$?"   # 28/28, exit 0
python3 verifiers/verify_harness_independent.py       ; echo "IND exit=$?"   # 24 derived, 4 scoped out, exit 0
python3 verifiers/verify_harness_claims.py --self-test       # 0 failure(s) over 10 assertions
python3 verifiers/verify_harness_independent.py --self-test  # 0 failure(s) over 104 assertions
                                                             # (86 at the r38 closure, 93 after the
                                                             # round-39 init_count grammar fixtures)

# the join, with the freeze receipt
python3 verifiers/verify_harness_independent.py --write-freeze /tmp/ind-freeze.json
sha256sum /tmp/ind-freeze.json          # 09fb71ca5e79d7f1… at the r38 closure tree;
                                        # re-measured round 39 the capture is a function of
                                        # the instrument's payload, not of this doc, so a
                                        # re-run prints the sha of whatever instrument bytes
                                        # are live at that moment (ae4baa55… at IND 872993f8…)
python3 verifiers/compare_harness_independent.py --independent-json /tmp/ind-freeze.json
echo "CMP exit=$?"                      # agreement 24/24 (4 scoped out), exit 0
# the executable receipt (round-38 seat P2, A1-D1): both sides' input digests +
# invocation record; `frozen-inputs` when both sides are consumed from files
python3 verifiers/verify_harness_claims.py --json > /tmp/har-freeze.json
python3 verifiers/compare_harness_independent.py --live-json /tmp/har-freeze.json \
  --independent-json /tmp/ind-freeze.json --receipt /tmp/receipt.json
echo "CMP exit=$?"                      # agreement 24/24, exit 0; receipt mode=frozen-inputs
python3 verifiers/compare_harness_independent.py --self-test  # 0 failure(s) over 97 assertions
                                                             # (was 83 at the r38 closure, 93 mid-r39;
                                                             # round 40 adds the fixture battery)
# Round 41 current re-measure (the 97 above is historical): at HEAD
# b1be35f9522f21c0c5b39879358a011806ab9200 / tree
# 8bb24450a9c500c427019c7147013b4946525b09, driver SHA-256
# 1742dcccad1118399f0aa959f7ea6884d5992834d8c4c8b94e108277ae87df76;
# --self-test -> 0 failures / 118 assertions, exit 0; live join -> 24/24,
# strict 20/24, 4 adjudicated / 4 scoped out, exit 0 (2026-10-19 13:36:30-41 -03).

# the mutant leg (both instruments move; the frozen arm flips and names).
# round 39: this fixture is durable at verifiers/fixtures/harness-independent/
# (the round-38 drafts it used to live in were pruned after measurement).
python3 verifiers/compare_harness_independent.py \
  --live-cmd "python3 verifiers/verify_harness_claims.py --json --oc-log verifiers/fixtures/harness-independent/oc-log/mutant-init-count.log" \
  --independent-cmd "python3 verifiers/verify_harness_independent.py --json --oc-log verifiers/fixtures/harness-independent/oc-log/mutant-init-count.log"
                                                                 # 24/24, exit 3: both instruments move
                                                                 # together on the init_count rows (round 39),
                                                                 # and the driver names the live side's own
                                                                 # non-PASS rows instead of a disagreement

# the round-39 predicate arms, each re-runnable against both instruments.
# round 40: the four logs this loop used to read from .ufo/round-39/drafts/p2/
# were pruned by the r39 integrator (only b2/ and PRUNE.log survive), so the
# block rebuilds them from the grammar the r39 adjudication landed. Each log
# carries one occurrence sequence; the r39 ruling is that both init_count rows
# derive from it in file order.
mkdir -p /tmp/w1-pred
printf 'run=aaa message=init count=1\nrun=aaa message=init count=2\n' > /tmp/w1-pred/mut-hargrammar-inc.log
printf 'run=aaa message=init count=3\nrun=aaa message=init count=2\nrun=aaa message=init count=1\n' > /tmp/w1-pred/mut-hargrammar-dec.log
printf 'run=aaa message="init count" value=2\n' > /tmp/w1-pred/mut-quoted.log
printf 'run=aaa message=init count=2\nrun=bbb message=init count=1\n' > /tmp/w1-pred/mut-hargrammar-crossrun.log
for LOG in mut-hargrammar-inc mut-hargrammar-dec mut-quoted mut-hargrammar-crossrun; do
  python3 verifiers/verify_harness_claims.py --no-baseline --json \
    --oc-log /tmp/w1-pred/$LOG.log > /dev/null   # live column
  python3 verifiers/verify_harness_independent.py --json \
    --oc-log /tmp/w1-pred/$LOG.log > /dev/null   # independent column
done
# both columns move together: inc -> []/0, dec -> ['3->2','2->1'], quoted -> 0/[]

# blindness by construction + the controls + the scope-out validation.
# round 39: every input these lines used to read from .ufo/round-38/drafts/w1/
# was pruned by the r38 integrator (PRUNE.log: drafts 95M -> 548K). The script
# below rebuilds each input it needs, so the block is self-contained.
bash .ufo/round-37/evidence/R1-make_blind_tree.sh /tmp/blind-tree
                                                    # round-40 re-run: pin-value residual 5
                                                    # (see §4), tree_files=340
python3 .ufo/round-37/evidence/R1-counter_blind.py  # 28/28 with zero derivation, exit 0
cat > /tmp/null_echo.py <<'PY'
import json, subprocess, sys
ids = [r["check"] for r in json.loads(subprocess.run(
    [sys.executable, "verifiers/verify_harness_claims.py", "--json"],
    capture_output=True, text=True, check=True).stdout)["results"]]
print(json.dumps({"checks": {i: 0 for i in ids}}))
PY
python3 verifiers/compare_harness_independent.py --independent-cmd "python3 /tmp/null_echo.py"
echo "CMP exit=$?"                      # 15/28, exit 1 (vacuity control)
python3 - <<'PY'
import json, subprocess, sys, pathlib
out = subprocess.run([sys.executable, "verifiers/verify_harness_independent.py", "--json"],
                     capture_output=True, text=True, check=True).stdout
bad = json.loads(out); bad["scoped_out"]["omp.db.rows"] = "names a derived row"
pathlib.Path("/tmp/ind-bad-scope.json").write_text(json.dumps(bad))
emp = json.loads(out); emp["scoped_out"] = {}
pathlib.Path("/tmp/ind-empty-scope.json").write_text(json.dumps(emp))
PY
python3 verifiers/compare_harness_independent.py --independent-json /tmp/ind-bad-scope.json
echo "CMP exit=$?"                      # exit 2, class named
python3 verifiers/compare_harness_independent.py --independent-json /tmp/ind-empty-scope.json
echo "CMP exit=$?"                      # exit 2, empty declaration named

# the four-number blocks used by §2 (runs both instruments live, prints ind/har/pin per row)
python3 - <<'PY'
import json, subprocess, sys
ind = json.loads(subprocess.run([sys.executable, "verifiers/verify_harness_independent.py", "--json"],
                                capture_output=True, text=True, check=True).stdout)["checks"]
har = {r["check"]: r for r in json.loads(subprocess.run(
    [sys.executable, "verifiers/verify_harness_claims.py", "--json"],
    capture_output=True, text=True, check=True).stdout)["results"]}
pin = json.load(open("verifiers/baseline.json"))["checks"]
for cid in sorted(har):
    r = har[cid]
    print(f'{cid:32s} {r["mode"]:8s} ind={ind.get(cid)!r:12} '
          f'har={r["observed"]!r:12} pin={pin.get(cid,{}).get("expect")!r}')
PY
```

Round-37 evidence kept: `.ufo/round-37/evidence/` (the adjudication protocol,
R1's blindness scripts and counter-instrument, V6's oracle, V5's floors
derivation, P4's live report) and the 22 seat fragments at
`.ufo/round-37/scouts/`. The round-37 report is at
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-37/kotoba.md`;
the work landed as `commit c8e233d` with the report at `commit cb4e0f3`. The
round-38 closure probes were at `.ufo/round-38/drafts/w1/` and were **pruned by
the r38 integrator** (`.ufo/round-38/evidence/PRUNE.log`); what survives is the
curated `.ufo/round-38/evidence/` set — the adjudication ledger, the r38 scouts'
quoted numbers, the C2 residuals patch and the V6b fence-divergence probe — plus
the durable fixtures the r39 seats landed under
`verifiers/fixtures/harness-independent/` and `verifiers/harness-independent-scope.json`.
Every number this file quotes is re-derivable by §6.

This file is the harness counterpart of
`corpus/knowledge/independent-verification-round12.md`; the direction is the
same — a non-author derived the verdicts and the author's instrument is the
thing that had to agree — and the standing residue is the same: agreement
falsifies implementations, never specs.
