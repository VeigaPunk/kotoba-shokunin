# w1-queued-rows — boxes citing `queued` rows

**Mutation:** the three appended A4 rows: `status` `mined` -> `queued` (used-by left intact)

**Prediction:** 3 of 4, exit 1

**Clause that should catch it:** (b) status conjunct — the rows resolve and name the entry, so only `status` catches it.

Replay: `bash replay.sh w1-queued-rows` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
