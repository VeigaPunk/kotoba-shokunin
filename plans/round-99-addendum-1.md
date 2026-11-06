# Round 99 — addendum 1 (before any landing reading)

Author: KotobaR99 (L1). Written after ScoutSourcesR99's report and before the landing reading of either
claim. No predicate, counter, target or kill rule changes.

## A1 — S281 cites the version-pinned page

ScoutSourcesR99 F1 (`.ufo/waves/round-99/w1/ScoutSourcesR99.md`): the L1's access record of
`https://docs.python.org/3/library/argparse.html` (`receipts/sources-opened.txt`, sha256 `bcd717f2…`,
334994 B) does not re-fetch byte-identically: `/3/` is a rolling build whose Sphinx footer
`Last updated on …` changes, so the digest is stale within the hour (the scout reproduced the L1's
digest exactly by changing only the footer timestamp). S281 therefore cites
`https://docs.python.org/release/3.15.2/library/argparse.html` (HTTP 200, 327874 B, sha256
`36e8d5361b591376bbf9255c08147ece82f5f1fe52a5abd3d149656e902bb8ae`, five identical fetches; the same
22-word quote at HTML lines 989–990). The claim's grounding is unchanged: C1's t08 arm rests on the
`'append'` action semantics. The `/3/` access is kept in the lesson's Gate as superseded-by-pin.

## A2 — rolling-digest drift of three existing rows is routed, not repaired

The same mechanism makes the recorded digests of S253 (tempfile), S270 (unittest) and S276 (pathlib)
non-reproducible (ScoutSourcesR99 F1). Registry cells are append-only; a superseding row per page is
round-100 work and is not claimed here.
