- **2026-10-25 — search-log correction (r72 closure defect D3; appended in round 73).**
  Question: where did the round-72 assimilation note land? At `c69711e` the round-64
  placement-correction note sits at `corpus/SOURCES.md:206-208` and its title reads
  "2026-10-24 — placement correction (appended by the L1 in wave 2)"; its second line reads
  "originally landed at EOF under" its quoted heading string. Commit `a0f7f17` (round-72 claim
  data) inserted the round-72 note between that note's first and second lines and cut the
  heading code span at its opening backtick. Reader-visible at the tip: `corpus/SOURCES.md:214`
  starts with a level-2 heading marker followed by `Leads (unopened)` and the note's tail, and
  `:217` keeps the older stray of the same family (already at `c69711e:210`). No bytes before
  this note are rewritten — the split sentence stays where `a0f7f17` left it and this note is
  the correction of record (CORPUS rule 2, append-only); it adds no registry row.
