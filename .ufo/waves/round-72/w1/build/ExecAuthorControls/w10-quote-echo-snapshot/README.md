# w10-quote-echo-snapshot — an A4 snapshot that is the quote echoed back

**Mutation:** snapshot S262 replaced by a one-line file holding exactly the located quote; pin recomputed

**Prediction:** 4 of 4, exit 0 — the second counter hole

**Clause that should catch it:** (d) as frozen cannot tell a page snapshot from a quote echo: the pin is honest, the file is not the page, and no conjunct reads the snapshot's provenance.

Replay: `bash replay.sh w10-quote-echo-snapshot` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
