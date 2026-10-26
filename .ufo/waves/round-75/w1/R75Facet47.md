# R75Facet47 — description audit candidate

## Axis: sourced depth and calibration

**Observation (committed bytes).** At lane HEAD `65a5c7a663249e0522cc49e4a148424200d9ddfe`, `SKILL.md:3-18` describes the frontmatter `description` as trigger/anti-trigger and sibling-boundary prose, ending with “shokunin files sit outside the omp discovery roots, so omp never reads this text.” The audit-relevant rule at `SKILL.md:23-47` is broader: it calls the description “the only part any router ingests” (`:23-25`), then supports that with omp/opencode surfaces and a documentation-mapped set of 11 clients. These are distinct claims: a narrow claim about observed routing surfaces versus a universal statement about “any router.”

**Control and falsifiability.** A good audit candidate is the universal quantifier at `SKILL.md:23-25`. Check the committed documentation/source rows for the claimed 11 clients, and require the audit to enumerate the actual router/client population and the exact evidence each client ingests. Counterexample criterion: one in-scope router that ingests body text or other skill fields falsifies “only part any router ingests”; absent an exhaustive declared population, restrict the wording to the observed omp/opencode implementations plus the documented 11-client set. This is a source-coverage control, not evidence that the statement is false.

**Risk / calibration.** The paragraph itself says only two harnesses are observable and the other 11 are mapped “by documentation” (`SKILL.md:23-25`), while its lead clause says “any router.” That phrasing risks silently converting bounded evidence into universal scope. A separate, checkable safeguard is already stated at `SKILL.md:54-56`: line citations are points-in-time and must be re-read if drifted. The description body explicitly says omp never reads it (`SKILL.md:16-18`), which also makes a live omp-trigger claim outside the warranted scope unless tested against the actual discovery path.

## Evidence and commands

- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` → `65a5c7a663249e0522cc49e4a148424200d9ddfe`.
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show HEAD:SKILL.md | wc -c` → `78569` bytes.
- Read committed worktree lines: `SKILL.md:3-18`, `SKILL.md:23-47`, `SKILL.md:54-56`.
- Source-backed conclusion is limited to the text and its stated evidence boundary; I did not verify the external 11-client documentation or router implementations.

## Unresolved

Whether any of the 11 documented clients actually ingest only `description`, and whether another router exists beyond that documented set, remain unverified here. This is a candidate audit/control, not a finding of factual error.
