# Kb80S08ReadmeRows — index-coverage test for the three new coverage rows

Seat Kb80S08ReadmeRows, round 80 wave 1, 2026-10-27.
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80S08ReadmeRows` (`clone3` = base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`, no patch; `clone2` = same base with `Kb80S08ReadmeRows.patch` applied plus two stub files `corpus/lessons/round-80.md` and `corpus/knowledge/allowed-tools-surfaces-round80.md`, so the rows' targets exist). The stubs are disposable fixtures, not landed content.

## base run (clone3, no patch), direct exit capture
command: `cd clone3 && python3 -B verifiers/verify_corpus_integrity.py > f 2>&1; rc=$?; echo "exit=$rc"`
```
corpus.index    tracked=152 unindexed=1 stale=0 missing=0  (169 FILE-column patterns over 151 md files)
DRIFT   corpus.index.tracked_files: observed=152 expected=144
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
3/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
exit=1
```

## patch applied + indexed files present (clone2, committed), direct exit capture
command: `cd clone2 && git apply …/Kb80S08ReadmeRows.patch && (stub files created) && git add -A && git commit -qm … && python3 -B verifiers/verify_corpus_integrity.py > f 2>&1; rc=$?; echo "exit=$rc"`
```
corpus.index    tracked=154 unindexed=0 stale=0 missing=0  (172 FILE-column patterns over 153 md files)
DRIFT   corpus.index.tracked_files: observed=154 expected=144
4/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.pointers.report_total, corpus.pointers.report_dead, corpus.pointers.commit_total, corpus.pointers.commit_unresolvable
exit=1
```

## readings
- The index class the rows exist to fix: `unindexed` 1 → 0. No `stale` and no `missing` is introduced; the column-2 pattern count rises by exactly 3 (169 → 172), one per new row.
- `corpus.index.tracked_files` (154 vs the stale baseline 144) stays red by design: the baseline refresh is repair 3's second step (`.ufo/waves/round-79/build/refresh-corpus-baseline.py` / E03), which the plan runs at the final pre-report commit after every corpus file lands. The four `corpus.pointers.*` DRIFTs are repairs 4–5's target and are untouched by a README-only patch.
- The gate's overall exit is 1 in both runs; no finding appears that is attributable to the new rows.

## row shape
- Every coverage-map row is 3 cells after the patch except lines 12 and 18, which are 4 cells **at base as well** (measured with the same splitter on the unpatched base README) — pre-existing, not introduced here.
- Column-2 tokens for the three new rows, harvested with `verify_corpus_integrity.file_column_tokens` on the patched README: `lessons/round-79-verifier-spotcheck.md`, `lessons/round-80.md`, `knowledge/allowed-tools-surfaces-round80.md` — exactly the three intended paths, no extra token.

## patch result
- `git apply --check` on a fresh base clone: exit 0.
- `corpus/README.md` sha256 after applying the patch: `9db6cc91a6942679c45d118896ee4780563da859b43defcac65b6935355d75a1` (identical in the generating clone and in a second fresh base clone).
- Patch: 5 insertions, 0 deletions, one file; sha256 `10117e66ea3c3fb0a15d0a2657565da9b719a1edcd601a771e94a17494613f5c` (23 lines, 7,941 bytes).
