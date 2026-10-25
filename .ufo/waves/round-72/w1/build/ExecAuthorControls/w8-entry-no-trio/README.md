# w8-entry-no-trio — the entry without the provenance trio

**Mutation:** the A4 entry keeps its `source:` lines and loses `verified-at:` and `recheck:`

**Prediction:** 3 of 4, exit 1

**Clause that should catch it:** (c) provenance conjunct — the entry exists and names its ids, but carries no verification date.

Replay: `bash replay.sh w8-entry-no-trio` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
