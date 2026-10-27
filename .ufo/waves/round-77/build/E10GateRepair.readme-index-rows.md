# R76-D4 index rows — the two unindexed closure spot-checks (kotoba, round 77 w1)

Owner: seat `E10GateRepair`. Deliverable 1 of 3. This is the **minimum** patch that
closes `corpus.index.unindexed` at the round-77 base; it does not touch any data file.

## The gate's row pattern (from `verifiers/verify_corpus_integrity.py`)

`file_column_tokens()` harvests the **backticked tokens in column 2 (File) of a
`## Coverage map` table row**, outside fenced regions. A token is a corpus-relative
path (`lessons/x.md`, `knowledge/y.md`) or a glob/brace pattern over such paths; it
covers a tracked file when `expand_pattern()` (exact match or `fnmatch` over
`git ls-files corpus/`) hits it. A tracked corpus file that no column-2 token covers,
and that is not `corpus/README.md` itself, is `corpus.index.unindexed`. Column 3 (the
description cell) is prose: it is scanned for report pointers and `commit `<hex>``
citations like any other tracked corpus markdown, but never as an index path.

`verify_corpus_independent.py` implements the same class by its own tokenizer, so a
row that satisfies one satisfies the other (measured below).

## The rows (copy verbatim; append at the end of the coverage map, before `## Frontier`)

```markdown
| Round-75 non-author spot-check (closure) | `lessons/round-75-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): the round-75 C1 re-check on committed bytes (`0`→`1`, verdict improved-bounded), the independent S213/S211 re-opens, the per-axis and trend verdicts, the frontier census and wave-shape reconciliation, and four routed defects R1-R4 (the stale 1,021-character premise, the absent tip no-harm receipt, the phantom `R75Attack28` seat report, the round-75 `LOG.md` closing line); landed without an index row, so both corpus gates were red at the round-77 base (`unindexed 2`, `tracked_files` 146 against 144); indexed round 77 |
| Round-76 non-author spot-check (closure) | `lessons/round-76-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 76's honest-stop disposition (neither C1 nor C2 landed, no axis moved), the per-claim re-checks from committed bytes, the round-end census, four conformance defects CD1-CD4 (the stray `kotoba-shokukin/` duplicate path, the missing `lessons/round-76.md`, the unrun census, the 52-vs-64 report-file gap) and five routed defects R76-D1-R76-D5; indexed round 77 |
```

The description cells name no `.ufo/reports/…` pointer and no `commit `<hex>`` token,
so both rows leave `report_total` and `commit_total` exactly where the two files
already put them (measured: 102 / 44 before and after).

## Patch form

`E10GateRepair.readme-index-rows.patch` (same directory) is that insertion as a
`git apply`-able diff, generated in a scratch clone with
`git -c diff.mnemonicPrefix=false diff -- corpus/README.md` (the lane config sets
`diff.mnemonicPrefix=true`, so an unprefixed run produces `i/…`/`w/…` headers).

```
git -C <clone> apply E10GateRepair.readme-index-rows.patch
```

Anchor: the coverage-map table ends at `| Round-74 verifier spot-check (closure) | …`;
the patch inserts the two rows after it, before the blank line and `## Frontier`.

## Measured effect (scratch clone of lane HEAD `6523aced`, receipts in
`.ufo/waves/round-77/receipts/E10GateRepair.*`)

| state | `unindexed` | `tracked_files` | `report_total` | `commit_total` | integrity exit | independent exit |
|---|---|---|---|---|---|---|
| base (no rows, old baseline) | 2 | 146 | 102 | 44 | 1 | 1 |
| + these two rows, old baseline | 0 | 146 | 102 | 44 | 1 (3 `equal` DRIFTs: 146/102/44 vs 144/99/43) | **0** |
| + rows + `E10GateRepair.refresh_baseline.sh` | 0 | 146 | 102 | 44 | **0** (9 PASS) | **0** |

The middle row is the load-bearing one: indexing alone fixes the zero-mode class and
the independent gate; only the baseline refresh can fix the three `equal` ids.

## Conflict with `build/SC06ReadmeCorpus.patch` (sibling seat)

`SC06ReadmeCorpus.patch` (in this same build directory) contains the two rows above
**plus** rows for `knowledge/description-craft-round76.md`, `lessons/round-76.md`,
`lessons/round-77.md` and a Round 77 append-only Core/known-gap note. The two patches
are mutually exclusive in both orders — `git apply --check` exits 1 each way (measured
in `/fast/scratch/hyaku/kotoba-r77/E10GateRepair/both` and `both2`), because both
insert at the same `## Frontier` anchor.

Apply **exactly one**:

- SC06's patch is the superset and is the right one **if and only if** it lands in the
  same commit as the three data files it indexes. Applied alone at base it makes both
  gates *worse* in zero mode: `stale_patterns` 0 → 3 and `missing_paths` 0 → 3
  (measured; receipt `E10GateRepair.sibling-rows-ordering.txt`), because a column-2
  token for a file that is neither tracked nor on disk is STALE **and** MISSING.
- This patch is the fallback: it is green on the base tree immediately and depends on
  no unlanded file.
