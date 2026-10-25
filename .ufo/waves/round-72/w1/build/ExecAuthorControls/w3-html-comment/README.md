# w3-html-comment — the boxes inside an HTML comment

**Mutation:** the four boxes wrapped in `<!--` … `-->` inside the checklist section

**Prediction:** 0 of 4, exit 1

**Clause that should catch it:** (a) rendered-bytes conjunct — the predicate removes HTML comments before it looks for boxes.

Replay: `bash replay.sh w3-html-comment` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
