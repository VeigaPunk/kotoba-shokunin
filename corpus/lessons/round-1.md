# Lessons — round 1

Round: 1. Evidence: `LOG.md` round-1 entry, commit `1d93182`,
report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-1/kotoba.md`.

## Worked

- **Survey-then-distill ordering.** Reading 16 real SKILL.md files before
  writing produced claims that name file + line (e.g. bailian-cli L23,
  wwkd L64–66). Every checklist item in the rewritten SKILL.md traces to an
  observed pattern, not a prior belief.
- **`wc -l` first.** Sizing the corpus upfront (18–392 lines) set the
  compression-bound claim on evidence instead of guessing what "long" means.
- **Line-anchored citations.** Writing `file L<n>` citations during the survey
  read (not after) kept them accurate — no post-hoc re-grepping needed.

## Failed / weak

- **Partial survey of three files.** bailian-docs-llm-wiki,
  bailian-managed-agent, bailian-sandbox were counted but not read in-body;
  their rows in the anatomy size table are the only claims they support.
  Lesson: either read a file fully or don't cite it — "read halfway" creates
  citation debt. Filed as a coverage gap in `corpus/README.md`.
- **AGENTS.md craft untouched.** The domain includes AGENTS.md but the survey
  corpus was SKILL.md-only. Next round should diff the two surfaces' anatomy
  before claiming the domain covered.

## Open question (opinion)

- Whether a skill's `description` length correlates with trigger precision is
  unmeasured — description lengths ranged ~80–700 chars, but no activation
  telemetry exists to test against. Falsifiable only with router logs.
