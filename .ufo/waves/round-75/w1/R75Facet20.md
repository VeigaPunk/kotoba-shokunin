# Round 75 — facet 20: description-audit calibration

## Observations (committed source)

- `SKILL.md:3-18` defines a narrowly scoped description: skill-file craft, trigger fidelity, named triggers and anti-triggers, and ownership boundaries. This is a reviewable scope, but does not itself report measured routing precision/recall.
- `SKILL.md:23-46` calls the description a loader contract and contrasts omp's potentially cached/truncated render with opencode's full-description render. The passage explicitly calls cache coverage time-varying and marks the old project-scoped `ufo` path as historical/unpinned (`:32-46`). Thus the text itself distinguishes observed historical mechanism from current live behavior; it should not be read as a current fleet census.
- `corpus/knowledge/skill-eval-artefacts-round70.md:19-21,32-34,47-72` supplies useful controls: output assertions versus trigger queries, repeated-run trigger rates, held-out validation split, and an explicit discrepancy between guide “above threshold” and implementation `>=`. At `:74-80` it expressly refuses the unsupported claim that clients natively run the eval file. These are concrete, falsifiable calibration ingredients, but the entry describes the sources and a suggested author process, not a measured audit outcome for this skill's own description.
- `corpus/lessons/round-74-verifier-spotcheck.md:76-78` records an observed folded-description parse at revision `ec2c1d3`, 1,021 characters against 1,024, and names ten non-`none` lanes. This is a pinned structural/length check; it does not establish that the ten names are correct trigger coverage or that excluded/anti-trigger queries route correctly.

## Candidate claim and check

A defensible candidate is bounded to *structural description scope*: “At `ec2c1d3`, the parsed folded frontmatter description is 1,021 characters (under its 1,024 cap) and names the ten lanes classified non-`none` in the corresponding adjacency census.” The spotcheck row supports the first observation and states the second; for a fresh claim, a concrete check should parse frontmatter from the stated commit and compare extracted lane names exactly against the committed census classifications at that same revision. Preserve the revision and command output in a committed receipt. This does not warrant a claim of routing effectiveness.

For effectiveness, use a separate held-out query set with explicit should-trigger/should-not-trigger labels, repeated runs, and a preregistered threshold; report counts/rates and threshold boundary semantics. The round-70 entry documents why equality at threshold is consequential (`:58-72`). Include near-miss queries for the explicit anti-triggers and sibling ownership clauses, and report false positives/negatives separately. Do not infer a live client router result from frontmatter character count or a source-guide recommendation.

## Risks / unresolved

- The spotcheck is historical at `ec2c1d3`, not evidence of the current r75 tip; no r75 frozen claim or current receipt was examined here.
- No live fetch or model/client experiment was performed. Consequently no present-day cache coverage, router behavior, or empirical trigger score is established.
- The round-70 evaluation recommendations do not establish that its proposed query set is representative; query construction and held-out adequacy require independent review.

Evidence commands: `read SKILL.md:1-48`, `read corpus/knowledge/skill-eval-artefacts-round70.md:1-84`, and `read corpus/lessons/round-74-verifier-spotcheck.md:75-78` (repository source reads; no execution of evaluation or live fetch).