# ScoutIndexRows — index observation at tip, r62–r65 spot-check rows (round 66, w1)

Seat: scout (leaf; no dispatch). Read-only observation; no production edits.
Observed tip: `2a8eba56b3f9321b70c569fa2816d42237ca49a2` ("round-66 verifier spot-check (integrator, hyaku): non-author admit/reject"). Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`. Scope: the four closure-owned r62–r65 spot-check paths and their `corpus/README.md` coverage-map rows; whether any new corpus file is unindexed.

## Index observation at tip (live run, both gate implementations)

`python3 -B verifiers/verify_corpus_integrity.py` → **exit 1** (recorded receipt `receipts/C2-integrity-after.txt` shows exit 0 at the earlier measured revision `fc1b71e`; the drift below postdates it):

- `corpus.index tracked=119 unindexed=1 stale=0 missing=0` (136 FILE-column patterns over 118 md files)
- `corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0`
- `--json` DRIFT rows: `tracked_files` 119 vs baseline 118; `unindexed` 1 vs 0, `unindexed_detail = ["corpus/lessons/round-66-verifier-spotcheck.md"]`; `report_total` 82 vs 79; `commit_total` 38 vs 37. PASS: `stale_patterns`, `missing_paths`, `report_dead`, `commit_unresolvable`, `commit_nonhash`.
- `python3 -B verifiers/verify_corpus_independent.py --json` corroborates: index `unindexed=1` naming the same file, `tracked_files=119`, `md_files=118`, DRIFT verdict on `corpus.index.unindexed`; commit/report classes agree (38/82) with all zero-checks PASS.

## Four r62–r65 spot-check paths: indexed exactly once each

`git ls-files corpus/` tracks all four under `corpus/lessons/`; `corpus/README.md` § Coverage map (lines 5–124) carries one dedicated row per file in the round-66-indexed block:

| README line | Row | FILE-column token | Occurrences in README |
|---|---|---|---|
| 118 | Round-62 non-author spot-check (closure) | `lessons/round-62-verifier-spotcheck.md` | 1 |
| 119 | Round-63 non-author spot-check (closure) | `lessons/round-63-verifier-spotcheck.md` | 1 |
| 120 | Round-64 non-author spot-check (closure) | `lessons/round-64-verifier-spotcheck.md` | 1 |
| 121 | Round-65 non-author spot-check (closure) | `lessons/round-65-verifier-spotcheck.md` | 1 |

- `grep -c` gives exactly 1 literal occurrence per path; each sits in the coverage-map section (between `## Coverage map` line 5 and `## Frontier` line 126), so each is a live index row, not prose.
- The only FILE-column glob in the map is `lessons/round-{1,4,5}-aggregator-audit.md` (line 30) — brace expansion over aggregator audits; it cannot match `*-verifier-spotcheck.md`, so no glob double-covers the four paths. Each is indexed exactly once.
- Gate cross-check: `unindexed_detail` names only the r66 file; the four r62–r65 files are absent from it (denoted by their rows).

## New corpus file missing from the map: YES, one

`corpus/lessons/round-66-verifier-spotcheck.md` — tracked at tip (added by `2a8eba5`, the tip commit itself; `git log` shows it as the only path in that commit, +83 lines) but **zero occurrences** in `corpus/README.md`. It is the gate's sole `unindexed` file and accounts for all four DRIFT deltas:

- `tracked_files` 119 vs baseline 118 (the file landed after the `round66_rerecord` baseline pin measured at `daedcdf`/tip-ward `fc1b71e`),
- `unindexed` 1 vs 0,
- `report_total` 82 vs 79 — the file adds 3 `.ufo/reports/...` pointer tokens (lines 10, 22, 26, all `.ufo/reports/round-66/kotoba.md`),
- `commit_total` 38 vs 37 — the file adds 1 `commit ``<hex>`` idiom (fleet report commit `1154d57a…`, line 11; resolves via the r66 lane→fleet hop, so `commit_unresolvable` stays 0). Its bare-sha and short-sha mentions are not `commit`-idiom tokens.

This matches the established round pattern (every prior closure spot-check landed unindexed and was indexed next round — README rows for r46–r61 all say so), and matches sibling `ScoutCorpusCount`'s reconciliation (base 116 + 2 lane-authored = 118 pinned; +1 closure spot-check = 119 at tip).

## Counter vs gate at the same tip

`python3 -B verifiers/check_r66_routed_repairs.py --rev HEAD` → `control at 11385e04: 0 of 2`, `D1 PASS`, `D2 PASS`, `r66 routed defects closed 2 of 2`, **exit 0** — while the integrity gate exits 1 on the same tree. Mechanism (observed in `check_r66_routed_repairs.py` `check_d2`): the counter's committed-byte predicate is `all(path in readme for path in SPOTCHECKS)` over exactly the four r62–r65 names (line ~35: `tuple("lessons/round-%d-verifier-spotcheck.md" % n for n in (62,63,64,65))`) plus `EXPECTED_COUNTS` read from the committed baseline blob, not a re-measurement of the tree. The r66 file is outside its four-name enumeration and its expected-count pins read the (now stale-by-one-file) baseline JSON, so a post-pin unindexed corpus file cannot trip it. Frozen predicate intact; coverage gap at the live tip.

## Findings

1. All four r62–r65 closure spot-check paths are indexed exactly once in `corpus/README.md` (lines 118–121); no glob or prose row duplicates them. CONFIRMED.
2. NOT confirmed for the second clause: one new corpus file, `corpus/lessons/round-66-verifier-spotcheck.md`, is missing from the map — sole `unindexed` entry at tip, both gate implementations agree.
3. Gate at tip: exit 1, 4 DRIFT rows, all attributable to that one file; zero-class checks (stale, missing, report_dead, unresolvable, nonhash) all PASS.
4. The r66 routed counter still certifies 2 of 2 at the same tip because its D2 check enumerates the four named paths against committed blobs and reads expected counts from the committed baseline, not the live tree — consistent with the frozen predicate, blind to post-pin index drift.

## Gaps / notes

- No claim scored here; observations only. The r66 file's missing row is an index-observation fact, not a judgment on C2's frozen predicate.
- Worktree noise noted, not counted: ` M .ufo/waves/round-66/w1/swarm-registry.json` (outside `corpus/`).
- Base state not re-measured live; `controls/C2-before.txt` already pins it.
- No tools installed this run (host pacman pause observed; nothing needed).
