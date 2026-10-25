# w5-outside-section — the boxes placed outside the checklist section (in § Sources)

**Mutation:** the four boxes moved to the end of `## Sources`, section otherwise unchanged

**Prediction:** 0 of 4, exit 1

**Clause that should catch it:** (a) section conjunct — the boxes are rendered but not inside `## Trigger-fidelity checklist`.

Replay: `bash replay.sh w5-outside-section` from this directory (clones the lane `--shared`, checks out the base, applies `carrier/` then `delta.patch`, commits inside the throwaway clone, runs the literal oracle).
