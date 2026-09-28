# Lessons — round 5

Round: 5. Evidence: `LOG.md` round-5 entry, commit `4002b9f`,
report `/home/vgpnk/projects/shokunin/.ufo/reports/round-5/kotoba.md`,
audit artifact `corpus/knowledge/fleet-skill-audit-round5.md`.

## Worked

- **Independent L2 audit lane with the verbatim checklist in context.**
  Handing the reviewer the 13 items verbatim (not a summary) produced a
  strict-reading verdict table plus 5 checklist-ambiguity meta-findings —
  the checklist got tested as hard as the files did. Zero clarification
  requests; a blank-context agent executed the checklist end-to-end.
- **Re-running the audit's greps before editing.** The filed defect said
  "ark/火山方舟 anti-trigger lives in body not frontmatter" — re-grepping
  showed the quoted text *doesn't exist anywhere in the file*. Repairing the
  *filed* defect verbatim would have propagated a fabricated quote. The audit
  was right about the location error but wrong about the quoted text.
- **grep sweep before scoping a negative claim.** One `grep -n` over the
  16-file survey set turned "counterexample none found" into two named
  counterexamples (`bailian-docs-llm-wiki` body 何时使用/何时不要使用,
  `bailian-model-recommend` body 适用场景) — a falsified claim became a
  measured exception rate (2/16).
- **The gap queue ordered itself.** SHONEN box 2 + the aggregator audit's
  "cheapest end-to-end task" pointer + 3 filed corpus defects all converged
  on one move. A round whose scope is forced by three independent records is
  a well-scoped round.

## Failed / weak

- **`edit` boundary-echo failures, third round running.** Two PUT ranges
  (`frontmatter-trigger-surface.md` 12–14, `SKILL.md` 122–129) auto-repaired
  or left a duplicated sentence — the round-4 lesson's "re-read after
  multi-op edit" mitigation was applied and caught both, but the edit layer
  still emits literal op headers into file text on some inputs. The failure
  signature is now: *any `edit` where the body echoes existing file lines
  verbatim can duplicate them at the range boundary*. Mitigation that works:
  grep the edited region for the last/first body line afterward — duplicates
  show up immediately.
- **My own SKILL.md repeated a corpus defect I hadn't cross-checked.** The
  `requires.bins` over-generalization existed in both the corpus entry and
  SKILL.md rule 7 — filed once in the audit, fixed in two places. Lesson:
  when a claim lives in two files, the corpus and the skill, a defect fix
  must grep both.
- **Blind spots found before trusting the telemetry stores.** `stats.db`
  records `args_chars` not args (skill loads surface as plain `read` calls),
  `message` stores no system role (offered catalogue not in opencode.db —
  recover it from omp jsonl `session_init.systemPrompt`), and `agent.db`
  fails `pragma quick_check`. Every telemetry store needs a capability note
  before a metric is built on it.
- **L1 re-ran the scout's headline queries before writing corpus.** The
  415-call histogram and the ELF `<skills>` offset matched exactly — scout
  output became citeable evidence only after independent verification, per
  the no-fabrication rule.
## New evidence (opinion-flagged where not provable)

- The shonen mint template's `description` is capability+scope only — all 5
  sibling files share the shape and all 5 fail checklist items 2–3. This is a
  *mint-time* defect, not a per-lane one; fixing the template fixes the fleet.
  Prediction: a mint-template fix that adds quoted triggers + one
  anti-trigger clause moves fleet conformance from ~40% to ~80% of items.
- Strict-reading audits over-fail on ambiguous checklist wording (5
  meta-findings). A checklist doubles as a spec — underspecified terms
  ("every prerequisite", "ends in an action") produce reviewer-dependent
  verdicts. The fix is definitional, not pedagogical.
