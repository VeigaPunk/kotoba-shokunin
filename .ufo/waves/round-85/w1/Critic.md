# Critic — round 85 wave 1

Full six-world table, exact command templates, oracle limitations and required answers: `.ufo/waves/round-85/w1/Critic/worlds.md`. Per-world argv/output/exits: `.ufo/waves/round-85/w1/Critic/W0-c1.json` through `W7-surfaces.json`; aggregate `results.json`; independent oracle, builder and exact small fixtures retained beside them.

- C1 depth: W0..W5 score **4,6,6,6,4,4 of 8**, each exit 1. None of the required shortcut worlds reaches target. Additional W7 (description + conforming eval + entry) scores **8/8**, exit 0. Counter was unavailable at construction; these are independent frozen-plan oracle observations, not production `--rev` measurements.
- C2 freshness: W4 path-only gives **DRIFT 2/3**, exit 1; surfaces **pass 7 / fail 0**, exit 0. W5 values-only gives **UNREADABLE 2/3**, exit 2; surfaces missing omp.real, exit 2. Neither reaches the conjunction.
- Strongest counterexample: additional W6 changes just two predicate-read path constants plus the omp sha/mtime pins; **OK 3/3 pins hold**, exit 0, and surfaces **pass 7 / fail 0**, exit 0, despite the two other caller constants remaining stale. Smallest safe correction: finish all four owned constants and inspect the two unmeasured callers; do not claim the conjunction covers them.
- C1 limitation: W7 contains the claimed artifact types but a source/date field is not proof of a live source reopening, and lexical eval shape is not measured trigger behavior. Smallest correction: bind the real entry to the live source receipt and keep claim language structural. Do not add/rename frozen rules.

No production files changed, no git writes, no tools installed. Scratch worlds were removed after copying receipts. No admission or judgment decision made.
