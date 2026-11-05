# ScribeSources — round 88 w1 findings

Full detail: `.ufo/waves/round-88/w1/ScribeSources/summary.md` and `.ufo/waves/round-88/w1/ScribeSources/receipts.txt`.

- S257 registry row at `corpus/SOURCES.md:198` (11 cells, NF 13). Upstream sha256 re-verified `976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e`; quote at line 149 present.
- Index row for `corpus/knowledge/omp-root-semantics-round88.md` at `corpus/README.md:177`; round-88 § Frontier note appended at `corpus/README.md:342`.
- Census `sources-census.sh validate ... kotoba` exit 0 (`kotoba ok`; 33 pre-existing W04 warnings).
- Integrity: 4/9 → 3/9 PASS. `stale_patterns` 0 → 1 is transient: the knowledge file is on disk but not yet tracked; clears on commit. `tracked_files` 173 → 174 and `unindexed` 1 → 2 come from other seats' files (`corpus/lessons/round-88-addendum-1.md`; pre-existing `round-87-verifier-spotcheck.md` still unindexed).
- C1 handoffs `C1_READY` and `FORGERY_READY` did not appear inside the wait window; C2 (`C2_READY`) did, with a disclosed self-test failure (1 of 16).
