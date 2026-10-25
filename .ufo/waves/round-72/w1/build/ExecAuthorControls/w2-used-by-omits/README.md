# w2-used-by-omits — boxes citing rows whose `used-by` omits the entry

**Mutation:** row S262: `used-by` -> `—` (status stays `mined`)

**Prediction:** 3 of 4, exit 1

**Clause that should catch it:** (b) used-by conjunct — the row is mined, tiered and real; only the back-link is missing.

Replay: `bash replay.sh w2-used-by-omits` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
