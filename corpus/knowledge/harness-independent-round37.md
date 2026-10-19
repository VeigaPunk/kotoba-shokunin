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

| | author's instrument (HAR) | independent derivation (IND) |
|---|---|---|
| file | `verifiers/verify_harness_claims.py` | `verifiers/verify_harness_independent.py` |
| sha256 | `6b8eb4b6e85b1640cbdbfedd10a6ee9055923caaad226736e7f672e8dff934f3` | `82ad9700a59cf7cff63e75cda2272a9450ca9407358b884a35166c1f8e044f03` |
| author | r10/r23 lanes (author side) | round-37 builder seats, blinded to the harness source, `baseline.json`'s harness rows, and corpus docs quoting them |
| self-test | `--self-test` → `0 failure(s) over 10 assertions` | `--self-test` → `0 failure(s) over 86 assertions` |
| exits | 0 pass · 1 drift · 2 inconclusive · 3 no baseline | 0 clean · 1 drift (`--freeze`/`--observed`) · 2 environment unreadable |
| join driver | `verifiers/compare_harness_independent.py`, sha256 `9a8c4cb4fdacdc58…`, `--self-test` → `0 failure(s) over 83 assertions` | same driver, mode-aware headline + strict column, `--receipt` (freeze receipt) |

Agreement predicate (round-37 C1 adjudication protocol §2, frozen before the
first join): `equal` → value equality; `zero` → both readings empty; `positive`
→ inequality direction. Strict type-tagged equality is published beside it.
All numbers below were re-measured at write time (2026-10-19, HEAD `cb4e0f3`,
IND `82ad9700…`, driver `c1538342…`) by the commands in §6.

**Measurement stamp, not a pin.** Both C1 instruments were edited by sibling
seats while this file was written (IND moved `27ae80ae…` → `82ad9700…`, the
driver `de2bd8ab…` → `0f7f59e8…` → `c1538342…`, with identical headline
`24/24, exit 0` at the last two). Every number here is stamped with the sha it
was measured on; the shas are re-read from `git status`-visible working bytes,
so a reader re-running §6 after the round lands should expect the assertion
counts to have moved and must re-measure before quoting them.

## 1. The claim this round lands

*Live tree*: the driver prints
`agreement: 24/24 (mode-aware protocol headline; 28 live checks, 4 scoped out by
the independent instrument)`, `strict 19/24`, `adjudicated rows: 5`,
`disagree: 0`, `scoped-out: 4`, and **exits 0** — `all checks agree, both
instruments green`. The after-state the claim declares is met **over the landed
scope**, and the scope is declared by the instrument itself, not by the driver.

*The round-37 state* (the reason this file exists): the same driver at
`de2bd8ab…` against IND `27ae80ae…` printed `23/28`, `disagree: 5`, exit 1.
The 5 rows were the two adjudications below plus the three catalogue rows. The
closure is therefore traceable, not asserted: each row has a probe, a ruling,
and a landed change.

*Mutant tree* (a fabricated `init count` / duplicate-name log fed to both
instruments via their own `--oc-log` flags): both move; the driver reports
`21/24`, exit 1, naming `oc.log.init_count_max (2 vs 5)`,
`oc.log.init_count_monotone (1 vs [])` and `oc.dup.onesided_roots (2 vs the
root list)`. *Frozen-vs-mutant* (the frozen receipt against the mutated live
side): `21/24`, exit 1, naming the same class set from the frozen values
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
| 5 | `oc.log.init_count_monotone` | zero | `0` | `[]` | `[]` | yes |
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
is 19/24 — 5 rows agree under the mode predicate while their encodings differ
(`0` vs `[]`, `0` vs `False`), and the driver names all 5. A naive `!=` check
scores 20/24 on the same data because Python's `0 == False` is true; that is
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

One row per disagreement or definitional difference. Probe outputs saved under
`.ufo/round-38/drafts/w1/`. A row without a probe is not a ruling.

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

**Zero-delta representation rows (D5, cosmetic).** `[]` vs `0`
(`oc.dup.onesided_roots`, `oc.log.init_count_monotone`,
`omp.descriptions.missing`, `omp.names.mismatches`), `False` vs `0`
(`oc.roots.plugins_cache`). Same population, different emptiness encoding; the
driver's `zero` predicate handles them and publishes the strict column beside
it. No action.

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

**Pre-existing red, found and recorded at write time.**
`python3 verifiers/verify_skill_checklist.py` **exits 1 at HEAD bytes** (the
worktree is unmodified vs `cb4e0f3` for `SCORECARD.md`):
`FAIL governance.citation_resolves … SCORECARD.md:131,132,133` — the round-37
rows' brace-glob citations (`.ufo/round-37/scouts/{P5,P6,V4,V5,I1,I2,S2}.md`)
are not expanded by the gate's brace-unaware citation predicate
(`SCHEMATIC_CITATION_RE` covers `round-N` only). The gate's `--self-test` is
green (`0 failure(s) over 1597 assertions`) and every other gate passes; the
red is a live-gate defect in committed bytes, recorded here, not smoothed.

## 4. Blindness — method and scrub residual

Blindness is **by construction, with a countable residual**, not an
attestation. `R1-make_blind_tree.sh` builds a worktree from `git archive HEAD`
(no `.git/` → the history channel is closed), removes the harness source and
`__pycache__`, reduces `baseline.json` to pin-shaped keys only (its prose notes
leaked `keys_reproduced=7`, `17→7`), deletes the docs that quote the pin set,
and drops `.ufo/` (prior-round fragments quote the pins). Re-run at write time:

- **pin-value residual = 0** — no file in the scrub tree carries the 64-hex
  template value, the pinned stdout forms (`keys_reproduced=7`, `db_rows=14`,
  `offered=7`, `28/28 checks pass`) or the pins-guard substrate shas outside
  the guard's own baseline block.
- **id-string residual = 3** — `verifiers/verify_harness_independent.py` and
  its two fixtures (`verifiers/fixtures/harness-independent/{oc-log,omp-cache}/case.json`)
  carry check-id strings. These are the builder's own artifacts naming their
  own rows; they are not harness source and carry no pinned value. Named so the
  residual is counted, never waved away. (R1's script prints
  `harness_pin_residual_count=3` because its token list predates these landed
  artifacts.)
- The scrubbed tree still **runs green**: with the current instrument and
  fixtures copied in, `24 derived, 4 scoped out, 0 unlanded`, exit 0,
  `--self-test 0 failure(s) over 86 assertions`; the pins guard runs inside it
  (`exit 0`); the substrate stays reachable (the db is outside the repo);
  `tree_files=337`, `dot_git_present=no`. The driver inside the scrub tree
  fails closed on the (correctly) absent harness — `ERROR: live instrument
  failed with no stdout … exit 2` — which is the scrub working as designed.

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
- **Agreement falsifies implementations, never specs.** A second same-spec
  instrument inherits the class spec's scope choices; the 24/24 is evidence
  about two implementations, not about the substrate model. The two
  adjudications moved *IND* to HAR's reading — the harness side won both rows,
  so this comparison has never falsified the author instrument on a value.
- **Blindness is attested plus structural.** The scrub bounds the *file*
  channel; the `--json` output channel is bounded by the freeze receipt; a
  negative (nobody read the source) is still not provable from inside the repo.
- **The instruments are host-anchored** (absolute default paths for the omp
  binary, db, log, roots), so a clone's run needs the flags — the same
  hermeticity caveat r12 recorded for the corpus pointers.
- **`oc.roots.names_plus_builtin`'s built-in term is declared 0** in both
  instruments (the string `customize-opencode` is absent from the binary); a
  future binary carrying it would move both readings together, un-adjudicated.
- **`R1-make_blind_tree.sh` at `.ufo/round-37/evidence/` resolves its repo root
  one level too high** (`$HERE/../../../..` from `.ufo/round-37/evidence` lands
  on the parent directory, not this repo), so the committed script archives the
  wrong tree; the copy this round ran from `.ufo/round-38/drafts/w1/` resolves
  correctly. The finding is recorded, not silently patched in a prior round's
  file.

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
# both instruments, both directions
python3 verifiers/verify_harness_claims.py            ; echo "HAR exit=$?"   # 28/28, exit 0
python3 verifiers/verify_harness_independent.py       ; echo "IND exit=$?"   # 24 derived, 4 scoped out, exit 0
python3 verifiers/verify_harness_claims.py --self-test       # 0 failure(s) over 10 assertions
python3 verifiers/verify_harness_independent.py --self-test  # 0 failure(s) over 86 assertions

# the join, with the freeze receipt
python3 verifiers/verify_harness_independent.py --write-freeze /tmp/ind-freeze.json
sha256sum /tmp/ind-freeze.json          # 09fb71ca5e79d7f1… (at this tree)
python3 verifiers/compare_harness_independent.py --independent-json /tmp/ind-freeze.json
echo "CMP exit=$?"                      # agreement 24/24 (4 scoped out), exit 0
# the executable receipt (round-38 seat P2, A1-D1): both sides' input digests +
# invocation record; `frozen-inputs` when both sides are consumed from files
python3 verifiers/verify_harness_claims.py --json > /tmp/har-freeze.json
python3 verifiers/compare_harness_independent.py --live-json /tmp/har-freeze.json \
  --independent-json /tmp/ind-freeze.json --receipt /tmp/receipt.json
echo "CMP exit=$?"                      # agreement 24/24, exit 0; receipt mode=frozen-inputs
python3 verifiers/compare_harness_independent.py --self-test  # 0 failure(s) over 83 assertions

# the mutant leg (both instruments move; the frozen arm flips and names)
python3 verifiers/compare_harness_independent.py \
  --live-cmd "python3 verifiers/verify_harness_claims.py --json --oc-log .ufo/round-38/drafts/w1/fixtures/oc-log-mutant.log" \
  --independent-cmd "python3 verifiers/verify_harness_independent.py --json --oc-log .ufo/round-38/drafts/w1/fixtures/oc-log-mutant.log"
                                                                 # 21/24, exit 1, names the mutated rows

# blindness by construction + the controls + the scope-out validation
bash .ufo/round-38/drafts/w1/R1-make_blind_tree.sh /tmp/blind-tree  # pin-value residual 0; id-string residual 3
python3 .ufo/round-37/evidence/R1-counter_blind.py                  # 28/28 with zero derivation, exit 0
python3 verifiers/compare_harness_independent.py --independent-cmd "python3 .ufo/round-38/drafts/w1/null_echo.py"  # 15/28, exit 1
python3 verifiers/compare_harness_independent.py --independent-json .ufo/round-38/drafts/w1/ind-bad-scope.json     # exit 2, class named

# the four-number blocks used by §2 (writer's script, prints ind/har/pin per row)
python3 - <<'PY'
import json
ind = json.load(open(".ufo/round-38/drafts/w1/ind-final.json"))["checks"]
har = json.load(open(".ufo/round-38/drafts/w1/har-final.json"))["results"]
pin = json.load(open("verifiers/baseline.json"))["checks"]
for r in sorted(har, key=lambda x: x["check"]):
    print(f'{r["check"]:32s} {r["mode"]:8s} ind={ind.get(r["check"])!r:10} '
          f'har={r["observed"]!r:10} pin={pin.get(r["check"],{}).get("expect")!r}')
PY
```

Round-37 evidence kept: `.ufo/round-37/evidence/` (the adjudication protocol,
R1's blindness scripts and counter-instrument, V6's oracle, V5's floors
derivation, P4's live report) and the 22 seat fragments at
`.ufo/round-37/scouts/`. The round-37 report is at
`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/reports/round-37/kotoba.md`;
the work landed as `commit c8e233d` with the report at `commit cb4e0f3`. The
round-38 closure probes are at `.ufo/round-38/drafts/w1/`.

This file is the harness counterpart of
`corpus/knowledge/independent-verification-round12.md`; the direction is the
same — a non-author derived the verdicts and the author's instrument is the
thing that had to agree — and the standing residue is the same: agreement
falsifies implementations, never specs.
