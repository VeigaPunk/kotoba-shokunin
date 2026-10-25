# honest — exit-0 arm: four boxes that really carry the rules

**Mutation:** none — the carrier verbatim

**Prediction:** 4 of 4, exit 0

**Clause that should catch it:** (a)-(d) all hold; this is the arm that must read 4.

Replay: `bash replay.sh honest` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
