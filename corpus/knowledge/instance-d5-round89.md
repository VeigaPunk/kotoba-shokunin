source: S259 (own-work: corpus/lessons/round-88-verifier-spotcheck.md @ a5b3b15c00b1de5db321e4226a0a7db17340e605, lines 73-74 — routed defect 4 "instance-level D5 with controls executed before the freeze"; the v2 blindness receipt is .ufo/waves/round-89/receipts/ctl-v2-blindness.txt)
verified-at: 2026-11-05 @ plan draft 43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3 (addendum 1: plans/round-89-addendum-1.md, A1.1-A1.6)
recheck: python3 -B verifiers/check_r86_routed_repairs_v3.py --self-test (expect `0 failure(s) over 37 assertions`, exit 0); python3 -B verifiers/check_r86_routed_repairs_v2.py --self-test (expect `1 failure(s) over 16 assertions`, the frozen w_added_red arm — the v2 blindness is the control, not a regression)

# D5 at instance level: per-name value and detail non-growth against a base receipt

## Why the name-level test was blind

The round-88 gate v2 (`verifiers/check_r86_routed_repairs_v2.py`) read integrity-gate state at two
granularities: the set of check names (identity) and the set of names in DRIFT (monotone). An added
citation under an already-red name changes neither set, so the frozen control `w_added_red` reads PASS
under v2 (`ExecMonotoneD5.md` F1; `ctl-v2-blindness.txt`). The same world reads exit 1 naming `d5iii` under
v3 (`ctl-w_added_instance.txt`: `FAIL d5iii instance growth under: [commit_total 62>61, commit_unresolvable 2>1]`).

## What v3 pins

A base receipt written at a clean freeze commit pins: the revision, the sha256 of the integrity instrument
and of `corpus-baseline.json`, the full observation (nine check rows with live values), the per-name detail
entries (the sorted `*_detail` lists of the observation), the record blobs of two non-author or historical
lessons, and a receipt self-digest (addendum A1.5).

- d5i: the same nine names and the integrity `--self-test` green at the root.
- d5ii: the DRIFT names are a subset of the receipt's (a healed red passes).
- d5iii: no name's value grew past its receipt value, and no detail entry is absent from the receipt.
- snapshot: the pinned digests and record blobs match; a receipt whose self-digest is pinned by the caller
  must match it before any leg runs.
- Location (Q79): a receipt and a measured root of different location classes return exit 2
  (could-not-evaluate), because the tracked symlink `.ufo/reports/round-76/kotoba.md` resolves only in the
  lane's parent shape.

## Measured controls (committed before the freeze)

| world | v3 result | receipt |
|---|---|---|
| w_added_instance (one lesson line citing an unresolvable hash) | exit 1, `FAIL d5iii`, `instance drift 2` | `ctl-w_added_instance.txt` |
| w_silenced (one integrity check removed) | exit 1, `FAIL snapshot_tampered` (digest pin) | `ctl-w_silenced.txt` |
| w_rerecorded (baseline expectations re-recorded) | exit 1, `FAIL snapshot_tampered` | `ctl-w_rerecorded.txt` |
| w_healed (one red citation resolved) | exit 0, `closed 5 of 5`, `instance drift 0` | `ctl-w_healed.txt` |
| w_tip (honest tip) | exit 0, `closed 5 of 5`, `instance drift 0` | `ctl-w_tip.txt` |

Note the w_silenced and w_rerecorded worlds were built before A1.5 and A1.2 existed; their polarity is
reproduced by the digest leg, which both amendments keep. Their pre-amendment receipts are the committed
`ctl-*.txt` files and are not rewritten.

## Bounds

- D5 reads the integrity gate's output. It does not judge what a new citation means.
- The population is the corpus `*.md` citations the integrity instrument reads. A dead citation in `LOG.md`
  is outside it (ExecCtlWorlds probe F shape; addendum N3) and is a named residual.
- A name whose value is unchanged but whose detail text is rewritten to a different citation is caught by the
  detail leg (probe E shape); a rewrite that keeps both value and detail text identical is not a change.
- `pointers.commit_unresolvable` stays red at 1 (`corpus/lessons/round-81.md:8`). This gate does not claim
  it repaired; a healed red passes d5ii and d5iii by construction.
