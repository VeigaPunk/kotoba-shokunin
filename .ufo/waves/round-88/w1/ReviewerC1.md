# ReviewerC1 — scoped findings (round-88 w1 attack seat)

Full per-claim review with evidence: `.ufo/waves/round-88/w1/ReviewerC1/review.md`. Scratch
`/fast/scratch/hyaku/kotoba-r88/ReviewerC1/` deleted at yield. No frozen file edited; no lane write
outside my seat dir; no ELF execution (read-only mmap only); no git writes anywhere.

## Verdicts (frozen C1 predicate, per assignment item)

- **Item 1 (independent bound re-implementation) — AGREE.** My checker reads the honest ledger
  `12 of 12, exit 0` at the tip (`receipts/indep_C1_honest.txt`, `indep_C1_honest_A14.txt`), using
  binding-call-line + join anchoring (A1.4 tokens aligned) and its per-row `// packages/` nearest-header
  (A1.2 alignment).
- **Item 2 (sets frozen in time) — UNPROVABLE from git** (file uncommitted; kill rule is the mechanism).
  My pre-commitment (`independent_c1.py` before v2 landed) corroborates it; the counter's own freeze
  hypothesis rests on the L1's addendum sha-disclosure (A1.4/A1.5/A1.8), not on anything this seat can
  measure after the fact.
- **Item 3 (tip re-run + 4 forged rejections) — AGREE.** My revs `efa495922e…`, `2d42bb6ead…`,
  `40f898da22…`, `8f779f6ca6…` read `10,10,9,9` of `12` (`exit=1`) on my checker
  (`receipts/indep_C1_worlds.txt`); the frozen r87 control on the same revs reproduces its record
  `12 of 12 exit 0` each (`r87control_on_myworlds.txt`). Rejections are per-failed-conjunct, not blanket.
- **Item 4 (positive control against blanket refusal) — AGREE.** Honest-tip `12 of 12` on the
  independent checker stands alongside the r87 counter's committed record.

## Findings (scoped)

1. `pattern_problem(v1) + bound(v1)` accepts `/etc/skills`, `/tmp/x/skills`, `~root/skills` (r87 counter
   conjuncts 1+4). My checker refuses all three. Re-measured independently:
   `receipts/indep_escape_check.txt`. Matches CriticFalsify C1-S4.
2. v1 binding tokens `cwd`/`skills` accept forged r87 worlds. My checker's A1.4-aligned sets refuse them.
   (`indep_C1_worlds_A14.txt`.)
3. mmap-position pitfall for any future counter that hashes an mmap and then searches it — document or
   refactor. Caught by my seat's own instrument before it caught anything else.
4. v2 landed (`sha256 506a2ba936e7af4492c3a79dd077a68d9ce190a802236d102cb51cbd6b4b9beb`) but
   `C1_READY` and `FORGERY_READY` never appeared within my 45-min poll window (assignment's poll
   budget). The v2 direct scoring (and CriticFalsify's S1/S2/S4 blocks against v2 as landed) therefore
   stayed within the L1's and the executor's own runs — not re-verified by this seat. The kill rule and
   the addendum's controls remain the operative enforcement in that window.

## Residual risks

- v2 as landed was not executed by this seat; my corroboration runs against the honest and forged
  *ledgers* and against the *r87 frozen counter* (whose exists-method I re-derived). If v2's actual
  reading differs from the addendum's intent, that divergence is not visible from this seat's output.
- The four rebuild revs differ in SHA from the r87 receipt revs; their TSVs are byte-identical to the r87
  receipts, and the r87 counter reproduces its r87 record on them — my fixture-fidelity anchor.
