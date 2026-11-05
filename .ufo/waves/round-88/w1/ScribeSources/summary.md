# ScribeSources — round 88 w1 summary

Seat: ScribeSources (leaf). Lane: /home/vgpnk/Projects/shokunin/kotoba-shokunin.

## What changed

1. `corpus/SOURCES.md` line 198 — registry row **S257** (after S256 at line 197). Source: omp 18.15.0
   agent-dirs walk-up module, upstream `packages/coding-agent/src/discovery/agents.ts` at tag v18.15.0
   (12313 B, sha256 976360027cee582030f2ec4871544821d8b66c25e8687ea461f4bee56aacb92e, re-fetched and matched).
   kind `code`, tier `A`, status `mined`, opened 2026-11-05, recheck `on-release`,
   used-by `corpus/knowledge/omp-root-semantics-round88.md`. 11 cells, 13 pipe-fields, no `|` in a cell.
   Located quote `if (current === (ctx.repoRoot ?? ctx.home)) break;` at upstream line 149 (verified).
2. `corpus/README.md` line 177 — index row for `corpus/knowledge/omp-root-semantics-round88.md`
   (after the round-87 knowledge row at line 176; before the round-87 lessons row at line 178). Written
   once the file existed on disk. The row describes the entry's own measured state: C1 not admitted.
3. `corpus/README.md` line 342 — append-only § Frontier note (round 88) after the end of the file's
   last section (line 340). It records C2 at 5 of 5 with a disclosed self-test failure (1 of 16,
   arm `w_added_red`), C1 not landed at note time, and the held items.

## Census and integrity

- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → `kotoba ok`, exit 0
  (33 W04 duplicate-url warnings, pre-existing). It was exit 1 with E11 until the knowledge file existed.
- `verify_corpus_integrity.py --json`: before 4/9 PASS → after 3/9 PASS.
  - `corpus.index.tracked_files` 173 → 174 (expected 172): DRIFT, one tracked addition by another seat
    (`corpus/lessons/round-88-addendum-1.md`).
  - `corpus.index.unindexed` 1 → 2 (expected 0): `corpus/lessons/round-87-verifier-spotcheck.md`
    (pre-existing) and `corpus/lessons/round-88-addendum-1.md` (not this item). Not indexed here.
  - `corpus.index.stale_patterns` 0 → 1 (expected 0): `corpus/README.md:177` names the knowledge file,
    which exists on disk but is not yet tracked; the check reads tracked paths. Expected to clear when
    ScribeEntry's file is committed. The row was not removed.
  - Other DRIFT names unchanged (`pointers.report_total`, `pointers.commit_total`,
    `pointers.commit_unresolvable`). Full lines in `receipts.txt`.
- `verifiers/corpus-baseline.json`: not edited.

## Not done / blocked

- C1 handoffs `C1_READY` and `FORGERY_READY` never appeared inside the window. `ExecLiveBound` was still
  running at the last check; `ExecForgeryWorlds` withheld FORGERY_READY. The knowledge entry states this.
- The round-88 § Frontier note is append-only and dated by its own text; the knowledge entry and the
  index row now exist, so the note's "knowledge file absent" remark is true as of its write time only.

## Files written by this seat

- corpus/SOURCES.md (line 198)
- corpus/README.md (line 177; line 342)
- .ufo/waves/round-88/w1/ScribeSources/receipts.txt
- .ufo/waves/round-88/w1/ScribeSources/summary.md
- .ufo/waves/round-88/w1/ScribeSources.md
