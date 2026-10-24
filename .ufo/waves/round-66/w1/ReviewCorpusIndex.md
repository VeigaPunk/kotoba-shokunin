# Review — corpus index / coverage map (round 66, kotoba)

Read-only seat. No production edit, no claim/counter/threshold/baseline change, no lane jj or Git
index write. All mutation confined to `/tmp/r66-review/` (throwaway archive sandbox). No tool
installs were needed.

## Revisions (keep these distinct)

| label | revision | role |
|---|---|---|
| pinned base | `11385e04e368c1e94ab1a5a89d7439033eb1f855` | plan base; C2 "before" (0 of 2) |
| C2 measured rev | `fc1b71e56fda86fefe672f2cae90a62318d34449` | revision both C2 receipts were taken at (green) |
| observed lane tip | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` | HEAD, integrator spot-check commit, one commit *after* the C2 measurement |

Worktree was dirty only in `.ufo/waves/round-66/w1/swarm-registry.json` (peer artifact) plus peer
reports; `corpus/` worktree bytes are clean against HEAD.

## Method — independent, not the shipped instruments

Own parser (`/tmp/r66-review/coverage_check.py`, written from the README/coverage-map contract, no
import of `verify_corpus_integrity.py` or `verify_corpus_independent.py`):

1. isolate the `## Coverage map` section (heading to next `## `);
2. take **only column-2** backticked tokens of table rows;
3. brace-expand `{a,b}` and `fnmatch` each variant against `git ls-files corpus/`;
4. for every non-glob variant, also test on-disk existence relative to `corpus/`.

Cross-checked the same parse against the committed `README.md` at the pinned base
(`git show <base>:corpus/README.md`) and against `git ls-tree -r --name-only <rev> corpus/`.

## Coverage result — exact counts

| tree | tracked corpus files | `.md` | coverage rows | col-2 tokens | distinct tokens | unindexed | stale | missing |
|---|---|---|---|---|---|---|---|---|
| base `11385e04` | 116 | 115 | 108 | 130 | 125 | **4** | 0 | 0 |
| tip `2a8eba5` | **119** | **118** | **114** | **136** | **131** | **1** | 0 | 0 |

- Tip set = 118 `.md` + 1 `.json` (`knowledge/sibling-citation-routing-round16.json`). 118 files are
  addressable; `README.md` is the index itself. Covered = **117 of 118**; unindexed = **1**.
- 136 tokens = 115 distinct corpus-internal + 16 distinct `../verifiers/...` + 0 rooted/tilde.
  0 glob tokens; two brace tokens expand (`lessons/round-{1,4,5}-aggregator-audit.md`,
  `../verifiers/fixtures/checklist/command-heredoc-tilde{,-dead,-misterm}/`).
- 114 data rows; every one carries ≥1 column-2 token (only the header row has none).
- **Stale = 0 and missing = 0 at both trees**: every corpus-internal token matches a tracked file,
  and every non-glob variant resolves on disk.
- base→tip delta is exactly **+6 rows / +6 tokens, zero tokens dropped**, and the six are exactly
  the round's promised rows (below). Base unindexed 4 = the four closure spot-check lessons; those
  are now indexed — D2's index half is genuinely closed on committed bytes.

## Confirmed rows

| README line | row | token | state |
|---|---|---|---|
| 118–121 | Round-62/63/64/65 non-author spot-check (closure) | `lessons/round-{62,63,64,65}-verifier-spotcheck.md` | tracked, indexed, all four files declare `author: hyaku closure (non-author integrator, @m_kfc)` (r64 on line 3, not line 2) |
| 122 | Repository-context commit resolution (round 66) | `knowledge/fleet-commit-resolution-round66.md` | tracked, indexed; `corpus/SOURCES.md:133` (S122) lists it and `corpus/lessons/round-66.md` in `used-by` |
| 123 | Round-66 lessons | `lessons/round-66.md` | tracked, indexed; file carries `## Gate`, `## Mistakes` M102/M103, `## Status changes`, and the S122 §6.7 quote; snapshot `.ufo/waves/round-66/snapshots/S122-excerpt.txt` exists |

## Findings

### High — the observed lane tip fails the plan's own C2 after-predicate; both corpus gates are red

Plan C2 freezes: "Independently, `python3 -B verifiers/verify_corpus_integrity.py` must exit 0 at the
final lane tree." At HEAD `2a8eba5` it does not:

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 ...
           unindexed: corpus/lessons/round-66-verifier-spotcheck.md
DRIFT   corpus.index.tracked_files: observed=119 expected=118
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=82 expected=79
DRIFT   corpus.pointers.commit_total: observed=38 expected=37
5/9 checks pass; DRIFT: ... ; exit=1
```

The second instrument agrees at the same revision: `verify_corpus_independent.py` → `HEAD 2a8eba5`,
`tracked_files=119 index_tokens=136 unindexed=1 stale=0 missing=0`, `corpus.index.unindexed
observed=1 DRIFT`, exit 1.

Sole cause: `git show --stat 2a8eba5` = only `corpus/lessons/round-66-verifier-spotcheck.md`
(+83 lines) — no coverage-map row, no `corpus-baseline.json` re-record. Every drift is that one
file: tracked 119 vs pin 118; unindexed 1; `report_total` 82 vs 79 (the file carries 3
`.ufo/reports/round-66/kotoba.md` pointers); `commit_total` 38 vs 37.

This is the lane's recurring "landed without an index row" class the map itself records for
rounds 48–61 and which D2 exists to close. 20 of the 21 tracked `*-verifier-spotcheck.md` lessons
sit in column 2 (rounds 46–65); round 66 is the missing 21st. The C2 receipts are honest about
their revision (`fc1b71e`, where I reproduce the index/pointer totals: 118 / 0 / 136 / 117 / 79 /
37), but the claimed final-tree condition is not true of the tree that now exists.

### Medium — the frozen C2 counter cannot see the regression

`python3 -B verifiers/check_r66_routed_repairs.py --rev HEAD` → `r66 routed defects closed 2 of 2`,
exit 0, while the live gate exits 1 on the same revision. `check_d2` reads committed blobs
(`corpus/README.md`, `verifiers/corpus-baseline.json`, `verifiers/verify_corpus_integrity.py`) and
compares the baseline's frozen `EXPECTED_COUNTS` (`corpus.index.tracked_files: 118`) plus the
hop/`inside_code_span` markers; it never compares that pin with the revision's actual tracked count
and never runs the gate. Consequence: "2 of 2" and a red gate coexist at the tip, and the pinned
118 is already stale at HEAD (119). The counter is a pin-conformance check, not a liveness check.

### Low — re-freeze bookkeeping if the spot-check is indexed

If a follow-up indexes the r66 spot-check, the equal-mode values become tracked_files **119**,
report_total **82**, commit_total **38**. The round-66 frozen predicate values (118 / 79 / 37) must
stay bound to `fc1b71e` as a revision-scoped measurement, not be silently re-pinned; a new control
receipt should carry the new numbers.

## Residual risk and verification gaps

- Ownership question not judged: the missing row is introduced by the integrator commit `2a8eba5`,
  after the lane's measurement. Whether the integrator was expected to index is a plan question,
  outside this seat; the tree-level observation stands regardless.
- My fc1b71e reproduction used `git archive | tar -x` into `/tmp` + a fresh `git init` (no lane Git
  writes). It reproduces index and pointer *totals* exactly, but not history-dependent
  `commit_unresolvable` (35 in the sandbox without lane history vs 0 in place), so commit-resolution
  semantics were left to the seats that own that axis.
- I verified path/tracked/authorship facts for the four closure rows and the two new rows, plus the
  S122 `used-by` wiring; I did not re-score their prose claims (other seats own that).
- Textual comparison only over committed README bytes; no evaluation of whether a coverage row's
  *Basis* prose is accurate, only that column-2 tokens resolve.

## Verification commands used (all read-only)

```
git ls-files corpus/ | wc -l                          # 119
git ls-tree -r --name-only <rev> corpus/ | wc -l      # base 116 / tip 119
git show --stat 2a8eba5                               # only the spot-check lesson
python3 -B verifiers/verify_corpus_integrity.py       # tip 5/9 exit 1; fc1b71e sandbox index-side green
python3 -B verifiers/verify_corpus_integrity.py --self-test   # 0 failures over 161 assertions
python3 -B verifiers/verify_corpus_independent.py     # tip unindexed=1, exit 1
python3 -B verifiers/check_r66_routed_repairs.py --rev HEAD   # 2 of 2, exit 0
python3 /tmp/r66-review/coverage_check.py             # 114 rows / 136 tokens / 1 unindexed / 0 stale / 0 missing
python3 /tmp/r66-review/base_check.py                 # base 108 rows / 130 tokens / 4 unindexed
```
