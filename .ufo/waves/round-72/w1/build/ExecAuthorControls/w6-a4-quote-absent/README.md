# w6-a4-quote-absent — an A4 box whose quote is absent from its snapshot

**Mutation:** snapshot S262 truncated to its first five lines; pins recomputed over the truncated bytes

**Prediction:** 3 of 4, exit 1

**Clause that should catch it:** (d) quote-in-snapshot conjunct — the pin is honest (it pins the truncated bytes), the quote is gone.

Replay: `bash replay.sh w6-a4-quote-absent` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
