# ReviewD2Baseline — C2 / D2 baseline re-record attack (calibration)

Read-only seat. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`.
Round tip measured: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (lane HEAD, `master`).
Measured revision named by the receipts: `daedcdf992c17cbc0b8a6ece204e1c7ce2b45fce`; receipt revisions
`4119647` (baseline reconcile), `fc1b71e` (integrity-after / routed-after), `9e75e73`.
Environment: Python 3.14.8, git 2.56.0; `FLEET_ROOT = /home/vgpnk/Projects/shokunin` is hardcoded
(`verifiers/verify_corpus_integrity.py:125`). No tool installed or upgraded. No lane write, no lane
jj/Git-index mutation; sandboxes are `git clone --shared` copies under `/tmp/d2work`. `corpus/` was
clean (`git status --porcelain -- corpus/` empty), so the worktree run is committed bytes; the independent
enumeration below reads committed blobs directly (`git ls-tree` / `git show`), independent of the worktree.

Method: run the primary gate with and without `--no-baseline --json` at the measured revision and at the
tip; re-derive every count from committed blobs with an enumerator that uses only the module's own regexes
and predicates but records each site, its resolution source, and index coverage by literal FILE-column row
vs. glob; cross-check the second canonical instrument on the same bytes; then test each expectation for
concrete support.

## 1. Expected-vs-observed on committed bytes

| check (mode) | expect | @11385e0 (base instrument) | @daedcdf (measured rev) | @2a8eba5 (round tip) |
|---|---|---|---|---|
| `corpus.index.tracked_files` (equal) | 118 | 116 | **118 ✓** | **119 ✗** |
| `corpus.index.unindexed` (zero) | 0 | 4 | **0 ✓** | **1 ✗** |
| `corpus.index.stale_patterns` (zero) | 0 | 0 | 0 ✓ | 0 ✓ |
| `corpus.index.missing_paths` (zero) | 0 | 0 | 0 ✓ | 0 ✓ |
| `corpus.pointers.report_total` (equal) | 79 | 79 | **79 ✓** | **82 ✗** |
| `corpus.pointers.report_dead` (zero) | 0 | 0 | 0 ✓ | 0 ✓ |
| `corpus.pointers.commit_total` (equal) | 37 | 38 | **37 ✓** | **38 ✗** |
| `corpus.pointers.commit_unresolvable` (zero) | 0 | 3 | **0 ✓** | 0 ✓ |
| `corpus.pointers.commit_nonhash` (zero) | 0 | 0 | 0 ✓ | 0 ✓ |

Expectations are the nine values in `verifiers/corpus-baseline.json:13-47`; they agree with the counter
constants (`verifiers/check_r66_routed_repairs.py:41-49`) and the plan. **At the measured revision every
expectation matches committed bytes and every zero-mode class is genuinely zero. At the round tip three
equal-mode expectations are stale and one zero-mode class is violated.**

## 2. Findings, by severity

### F1 (high) — the frozen after-predicate is false at the final lane tree as written

`plans/round-66.md` freezes two clauses: the counter at `<round-66-tip>` reads `2 of 2`, and
"Independently, `python3 -B verifiers/verify_corpus_integrity.py` must exit **0 at the final lane tree**."
The first holds; the second does not at the tip.

```
$ python3 -B verifiers/verify_corpus_integrity.py            # @2a8eba5, committed corpus
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 ...
DRIFT   corpus.index.tracked_files: observed=119 expected=118
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=82 expected=79
DRIFT   corpus.pointers.commit_total: observed=38 expected=37
5/9 checks pass; DRIFT: ...; exit 1
```

`--no-baseline --json` at the same tip also exits 1: `unindexed` is a zero-mode violation and is
baseline-independent. The second instrument agrees exactly (`verify_corpus_independent.py --json`:
tracked 119, unindexed 1, report_total 82, commit_total 38, exit 1), so this is not an instrument split.

Cause is a single committed file: `2a8eba5` added `corpus/lessons/round-66-verifier-spotcheck.md`
(+83 lines) **after** the baseline re-record, with no coverage-map row (`grep -c round-66-verifier-spotcheck
corpus/README.md` → `0`). It carries the whole delta: +1 tracked file, +3 report pointers
(`.ufo/reports/round-66/kotoba.md` at lines 10, 22, 26 — all fleet-resolved), +1 commit citation
(`1154d57a…` at line 11 — fleet-resolved). Everything else is unchanged from the measured revision.

Reading the claim fairly: the fleet report scopes the gate line to `fc1b71e`
(`.ufo/reports/round-66/kotoba.md:28`), and the receipts reproduce exactly there (9/9, exit 0), so the
*measurements* are honest. The defect is that the plan's frozen wording promises exit 0 at the **final
lane tree**, which the round's own last commit falsifies, and no receipt re-measures the post-spot-check
bytes. This is the M21/M22 "unindexed closure landing" class (baseline notes `round47`, `round49`,
`round50`) recurring inside the round that closed it. It also leaves the admitted entry's own recheck red:
`corpus/knowledge/fleet-commit-resolution-round66.md` says the gate "must exit 0 after the round-66 corpus
baseline is re-recorded" — true at `4119647`/`fc1b71e`, false at the tip.

### F2 (medium-high) — the frozen C2 counter cannot observe the class it certifies

`check_d2` (`verifiers/check_r66_routed_repairs.py:78-99`) reads three committed blobs and asserts:
(a) `corpus/README.md` contains the four hardcoded r62–r65 path strings (`:34-37`, `:84`);
(b) `corpus-baseline.json` carries `EXPECTED_COUNTS` and the `round66_rerecord` note key (`:41-50`, `:88-94`);
(c) `verify_corpus_integrity.py` contains three source substrings (`:96-99`).
It never executes the observation at `--rev`.

Consequence, measured: `--rev` returns `2 of 2`, exit 0 at **4119647, fc1b71e, 9e75e73 and 2a8eba5** — the
same certification for the reconcile commit and for a tree whose gate is red with `unindexed=1`. The
counter therefore cannot distinguish "the baseline file was edited to the right numbers" from "the tree is
reconciled". `path in readme` is also satisfied by any prose mention or fenced example, not only a
FILE-column row; the only instrument that actually verifies the row is the gate, which the counter does not
run. The second clause of the predicate is what supplies the missing observation, and F1 shows it is
unreceipted at the tip. Structural note only — the code-span mutation verdicts belong to the
`MutC2CodeSpan` / `MutC2NoFleetHop` seats, which I did not pre-empt.

### F3 (medium-low) — the baseline note misattributes one of the three unresolvable reductions

`corpus-baseline.json:67` (`round66_rerecord`) says `commit_unresolvable 3 -> 0 (lane-first then fleet-root
resolution)`. The three base tokens are `451a02ff`, `def4b9ff…`, `7b370d54…`
(reproduced at `11385e0`: `commit_unresolvable_detail` = those three). The hop genuinely resolves two:
`def4b9f` = "round-62: kotoba report revision 7", `7b370d5` = "round-65: kotoba report" — present in the
fleet repo, absent in the lane. The third, `451a02ff`, is **absent from both** repositories
(`git cat-file -e '451a02ff^{commit}'` fails in lane and in `/home/vgpnk/Projects/shokunin`); it leaves the
counted set only through the new code-span exclusion. So the accurate statement is "2 resolved via the
fleet hop + 1 reclassified as code-span context", and the note's causal claim is wrong for one token. The
plan text authorizes both mechanisms (`plans/round-66.md` C2 move), so the change itself is legitimate —
the permanent record's attribution is not. The same note's `report_total 79 unchanged` compares
observed-at-base 79 with new-expectation 79 (the prior expectation was 51); `receipts/C2-reconcile-measure.txt`
states the expectation delta correctly (`81 -> 118`, `51 -> 79`, `32 -> 37`), so only the baseline artifact
is ambiguous.

### F4 (low) — the code-span exclusion is missing from the verifier's frozen EXCLUDED contract block

`verify_corpus_integrity.py` adds `inside_code_span` (`:321`) and applies it at `:522-523`, but the
"EXCLUDED — false-positive shapes" doctrine (`:50-90`) documents only the double-quote shape for commit
citations (`:60-62`). Both causes also emit the same detail label, `"(quoted meta-finding)"` (`:524`), so an
audit cannot tell quote-context from code-span-context without re-deriving it. The rule is pinned by
self-test (`:1040-1046`) and is documented in the lesson (M102 fix text) and in the independent verifier's
docstring (line 28), which is why this is low rather than medium. Current blast radius is checked: exactly
one site is code-span-excluded in the corpus (`corpus/lessons/round-54-verifier-spotcheck.md:147`,
`451a02ff`), and no live citation is hidden. Residual risk: the exclusion branches before `is_hex_object_id`,
so a live `commit \`hash\`` written inside a wider code span (e.g. a double-backtick table cell) would
disappear from `commit_total` without appearing in `commit_nonhash`.

## 3. Support test for the new expectations (no denominator fitting found)

At `daedcdf`, each nonzero expectation has concrete support, re-derived from committed blobs:

- `tracked_files = 118` — 116 base files + `corpus/lessons/round-66.md` + `corpus/knowledge/fleet-commit-resolution-round66.md`
  (`git diff --name-status 11385e0 daedcdf -- corpus/`: 3 M, 2 A, 0 D). 117 of the 118 are covered by a
  **literal** FILE-column row; the 118th is `README.md` (the index itself, excluded by design). No file is
  covered only by a glob (`glob_only_cover = 0`), so coverage is not laundered through a pattern. The four
  r62–r65 closure spot-check rows are real rows (`corpus/README.md`, added at `806b53b`).
- `report_total = 79` — all 79 counted pointers resolve to files; 21 do so only through the fleet root
  (`.ufo/reports/round-5x…/kotoba.md` in `corpus/lessons/round-56..65-verifier-spotcheck.md` and
  `round-57.md`); 0 dead. Excluded classes are the pre-existing 8 placeholder/glob shapes and 2 quoted
  pointers (`corpus/README.md:68`, `corpus/lessons/round-57.md:86`) — both unchanged from base.
- `commit_total = 37` — 35 lane-resolved + 2 fleet-only (`def4b9f`, `7b370d5`), 0 dead, 0 nonhash; no site
  resolves in both repositories. The one counted-set reduction (38 → 37) is the `451a02ff` reclassification
  of F3: its line reads "the `` commit `451a02ff` `` **grammar** in the new entry", and
  `corpus/lessons/round-54-verifier-spotcheck.md:147-148` records that the entry itself was rewritten to
  `google-gemini/gemini-cli@451a02ff`, so calling it token-shape context is supported by the text, not just
  by convenience. It is nevertheless the only exclusion that coincides exactly with a zero-mode defect, so
  it must not be described as a resolution (F3).
- Direction check: no equal-mode expectation was lowered. `81 → 118`, `51 → 79`, `32 → 37` are all
  increases over the prior baseline; the zero-modes stayed 0. There is no downward fit.

Reconciliation at the receipt revisions also reproduces: gate 9/9 exit 0 at `4119647` and at `fc1b71e`;
independent instrument 37/0 exit 0 at `fc1b71e`; counter `0 of 2` at `11385e0` and `2 of 2` at `fc1b71e`.
Source pins hold at the tip: `verify_corpus_integrity.py` sha256 `febfa57e…6534`, counter `3129c0d7…3141`,
independent `de51f457…71c9` — matching the three receipts; self-tests 161 and 14 assertions, 0 failures.

## 4. Residual risk

- The gate reads the working tree by design, so the tip verdict is only committed-bytes-stable while
  `corpus/` is clean (it was; the only worktree deltas are wave artifacts under `.ufo/waves/`).
- `FLEET_ROOT` is a hardcoded host path: on any other host the 2 fleet-only commits read unresolvable and
  the 21 fleet-reachable pointers read dead. The baseline records `host: vgpnk`, consistent with prior
  rounds, but the reconciliation is not hermetic off this host.
- `as_of`/`measured_against` in the baseline still describe the round-16 measurement (2026-09-29); only the
  appended note describes round 66. This follows the file's existing convention but makes the new record
  discoverable only by reading the note key.
- The second instrument was aligned to the hop/code-span semantics inside this same round (M103), so
  agreement at `fc1b71e`/tip is implementation-independent but round-coupled evidence, weaker than a
  derivation by a lane that never saw the change.

## 5. Verification gaps

- I did not run mutant baselines or fabricated-baseline counters; the code-span and no-fleet-hop mutation
  verdicts are the `MutC2*` seats' scope.
- I verified the three cited fleet objects exist and their subjects match the citing sentences; I did not
  audit the fleet report bodies (round-62/65/66 `kotoba.md`), which is the spot-check's scope.
- Fleet-root absence/other-host behaviour was read from code and the self-test fixtures, not exercised live.
- C1 was not inspected (other seats).

## 6. Disposition

Calibration holds at the measured revision: `118 / 0 / 0 / 0 / 79 / 0 / 37 / 0 / 0`, every expectation
supported by a real file or resolved object, both instruments green, pins matching. It does not hold at the
round tip: the frozen "exit 0 at the final lane tree" clause is false (`5/9`, `unindexed=1`, exit 1), the
baseline is stale by one commit (+1 file, +3 pointers, +1 commit), and the counter still certifies
`2 of 2` because it never observes. Recommendation for the L1/orchestrator, not applied here: either pin
the gate clause to the measured revision (`fc1b71e`, which the fleet report already does) or index
`corpus/lessons/round-66-verifier-spotcheck.md` and re-record at the tip next round; and make counter D2
evaluate the index/citation observations at `--rev` so it can fail on `unindexed > 0`.
