source: S259 (own-work: corpus/lessons/round-88-verifier-spotcheck.md @ a5b3b15c00b1de5db321e4226a0a7db17340e605, lines 73-74 — routed defect 4 "instance-level D5 with controls executed before the freeze"; the v2 blindness receipt is .ufo/waves/round-89/controls/v2-before-addinst.txt)
verified-at: 2026-11-05 @ freeze revision 12f4b6b93f1eef3b20c0ec6249c2c065215909f5 (receipt .ufo/waves/round-89/receipts/d5v3-base-receipt.json; amendments plans/round-89-addendum-1.md A1.1-A1.7)
recheck: python3 -B verifiers/check_r86_routed_repairs_v3.py --self-test (expect `0 failure(s) over 37 assertions`, exit 0); python3 -B verifiers/check_r86_routed_repairs_v3.py --base-receipt .ufo/waves/round-89/receipts/d5v3-base-receipt.json (expect `closed 5 of 5`, `instance drift 0`, exit 0 at the freeze tree); python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test (expect `1 failure(s) over 16 assertions`: the frozen w_added_red arm — the v2 blindness is the recorded control, not a regression)

# D5 at instance level: per-name value and detail non-growth against a base receipt

## Why the name-level test was blind

The round-88 gate v2 (`verifiers/check_r86_routed_repairs_v2.py`) read integrity-gate state at two
granularities: the set of check names (identity) and the set of names in DRIFT (monotone). An added
citation under an already-red name changes neither set. Measured at the freeze state, the frozen v2 gate reads
`closed 5 of 5`, exit 0 on the added-instance world (`.ufo/waves/round-89/controls/v2-before-addinst.txt`), the same
reading it gives the honest tip (`v2-before-tip.txt`). The v3 gate reads exit 1 on that world, naming `d5iii`
with `instance drift 2` (`final-w_added_instance.txt`).

## What v3 pins

A base receipt written at a clean freeze commit pins: the revision, the sha256 of the integrity instrument and of
`corpus-baseline.json`, the full observation (nine check rows with live values), the per-name detail entries (the
sorted `*_detail` lists), the blobs of two lessons that may not be rewritten (`corpus/lessons/round-86-verifier-spotcheck.md`,
`corpus/lessons/round-81.md`), and a receipt self-digest (`receipt_sha256`, addendum A1.5).

- d5i: the same nine names and the integrity `--self-test` green at the root.
- d5ii: the DRIFT names are a subset of the receipt's (a healed red leaves the set).
- d5iii: no name's value grew past its receipt value, and no detail entry is absent from the receipt.
- snapshot: the pinned digests and record blobs match (an absent record pins as null and a change either way fails).
- Location (Q79): a receipt and a measured root of different location classes return exit 2 (could-not-evaluate),
  because the tracked symlink `.ufo/reports/round-76/kotoba.md` resolves only in the lane's parent shape.

## Measured controls at the freeze revision (final gate; `.ufo/waves/round-89/controls/`)

| world | expected | observed | closed / drift | file |
|---|---|---|---|---|
| w_tip (freeze tree, lane-shaped clone) | 0 | 0 | 5 of 5 / 0 | `final-w_tip.txt` |
| w_healed (base = freeze tree minus two index rows; freeze tree heals `corpus.index.unindexed` 2 → 0) | 0 | 0 | 5 of 5 / 0 | `final-w_healed.txt`, `w_healed_base-write.txt` |
| w_added_instance (one lesson line citing an unresolvable hash) | 1 | 1 | 4 of 5 / 2 | `final-w_added_instance.txt` |
| w_silenced (one integrity check removed from the script) | 1 | 1 | 4 of 5 / 0 (`FAIL d5i`, `FAIL snapshot_tampered`) | `final-w_silenced.txt` |
| w_rerecorded (one baseline expectation re-recorded) | 1 | 1 | 4 of 5 / 0 (`FAIL snapshot_tampered`) | `final-w_rerecorded.txt` |
| equivalence: lane vs lane-shaped tip clone, observation dict | identical | identical | — | `equivalence.txt` |

## The base-versus-freeze reading (disclosed, not a healed-red control)

Judged against the round's base receipt (`a5b3b15c`, `base-a5b3b15c-receipt.json`), the freeze tip reads exit 1,
`instance drift 2`: `corpus.index.tracked_files 180>177` and `corpus.pointers.report_total 144>141` (measured,
`final-info_round_base_vs_tip.txt`). The round's three new corpus files (its lesson, its knowledge entries) are that
growth under names that were already red at the base; registry rows and index rows add no corpus `*.md` citation. That growth is real and is the reason the healed-red control was
built on a base that differs from the freeze tree only by the heal (`final-info_round_base_vs_tip.txt`). D5 cannot
separate "this round healed a red" from "this round added to a red" when both happen between the receipt and the
world; the receipt must be taken at the freeze, which is what the claim's protocol requires.

## Bounds

- D5 reads the integrity gate's output. It does not judge what a new citation means.
- The population is the corpus `*.md` citations the integrity instrument reads (`corpus/`). A dead citation in
  `LOG.md` or `SCORECARD.md` is outside it (addendum N3); this is a named residual.
- A name whose value is unchanged but whose detail text is rewritten to a different citation is caught by the detail
  leg (probe E shape, unit arm `arm d5iii detail`); a rewrite that keeps value and detail text identical is not a change.
- `w_healed`'s base is a scratch-only commit (`2043fde2`, deleted with the scratch clone); its tree differs from the
  freeze tree only by the two removed index rows. The receipt records the tree, not the scratch commit, as the
  evidence.
- `pointers.commit_unresolvable` stays red at 1 (`corpus/lessons/round-81.md:8`). This gate does not claim it repaired.
- The `report_dead` detail depends on the lane-shaped location; a clone-shaped measurement is refused, not compared.
