# R75Attack58 — independent falsification of R75Facet58

## Target and measured bytes

Target: `.ufo/waves/round-75/w1/R75Facet58.md`. Central factual claim attacked: the paragraph at `SKILL.md:166` asserts four clients state 1,024 and none of those clients documents a cut there, while attributing the entire paragraph to `verifiers/check_description_thresholds.py`.

Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe`. Committed `SKILL.md` SHA-256: `1b2804fbab784b2c523681259f37d783238f65b2ca21c69b01a5a041bd13155f`. Current working-tree `SKILL.md` SHA-256 is `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`; it differs, so I did not use it as evidence. All probe inputs were loaded from `git show <revision>:<path>`.

## Attack / result

I independently executed the committed counter module's public `judge()` against committed input bytes, mutating only the in-memory header string. Actual outputs (`backed count`, `unbacked clients`):

- Pristine: `7, []`
- Header count changed from “four clients state 1,024” to “three clients state 1,024”: `7, []`
- Same count changed to “six”: `7, []`
- Negative flipped from “none documents a cut there” to “a cut is documented there”: `7, []`

The behavior-bearing observation is that the counter does not evaluate the header sentence: all three contradictory mutations preserve the exact pristine result. This corroborates the control weakness, not a defect in the factual sentence itself. The report's underlying table evidence is independently visible in committed `SKILL.md:172-176`: VS Code, Copilot CLI, Cursor, and opencode each contain a 1,024 threshold; their respective past-threshold cells say “Not documented”, “Not documented”, “No cut documented”, and “nothing: no cut…”. The four-row factual claim therefore survives this attack at the measured revision. Scope caution also survives: the prose says “four clients” without expressly saying “of seven”; the report identifies the separate 11-client census and unswept four clients, but I did not re-run an external-client sweep.

## Verdict

**Survived attack on the report's central control finding; underlying factual claim not falsified.** A counter cited as checking the paragraph gives identical results for altered counts and a reversed negative, so its attribution does not gate these clauses. The proposed extension's exact functioning is untested; this probe supports only the need for a detector that reads the paragraph, not that the proposed design is sufficient. No claim is made here about live vendor behavior or the render inference.

## Restoration evidence

No file was edited: mutations were transient strings in memory, with no scratch fixture or live fetch. Thus committed and working-tree `SKILL.md` bytes remain unmodified by this probe; the hashes above are the before/after evidence available (current worktree already differed from the measured commit before probing). No lane source or sibling file was written. Report path: `.ufo/waves/round-75/w2/R75Attack58.md`.
