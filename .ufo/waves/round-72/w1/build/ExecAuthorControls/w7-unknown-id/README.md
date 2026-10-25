# w7-unknown-id — a box naming an id that resolves in no registry row

**Mutation:** A1 tail cites `S999` beside the real `S203`

**Prediction:** 3 of 4, exit 1

**Clause that should catch it:** (b) registry-row conjunct — every cited id must be an 11-cell row; S999 is in none.

Replay: `bash replay.sh w7-unknown-id` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
