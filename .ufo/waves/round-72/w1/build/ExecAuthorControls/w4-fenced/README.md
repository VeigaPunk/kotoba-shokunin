# w4-fenced — the boxes inside a fence

**Mutation:** the four boxes inside a ``` fence inside the checklist section

**Prediction:** 0 of 4, exit 1

**Clause that should catch it:** (a) rendered-bytes conjunct — fenced blocks are removed before box extraction.

Replay: `bash replay.sh w4-fenced` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
