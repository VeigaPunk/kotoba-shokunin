# kotoba-shokunin — Iteration Log

- 2026-09-28 — round 0: minted as shonen.
- 2026-09-28 — round 1: rewrote SKILL.md as skill-file craft domain knowledge
  (anatomy table, frontmatter trigger rules, decision-table criteria, compression
  rules, 13-item trigger-fidelity checklist, anti-patterns, ~600-line bound).
  Evidence: surveyed 16 production skill files — `~/.agents/skills/{wwkd,godspeed,
  sekhmet-l3,xbrd-ask,omarchy,bailian-*}/SKILL.md` and
  `~/.config/opencode/skills/ufo/SKILL.md` (line counts 18–392; anatomy patterns
  and citations recorded in the file's Sources section).
  Also created corpus/ per ../CORPUS.md: README index + 3 knowledge entries
  (frontmatter triggers, anatomy/compression, fail-closed/anti-patterns) +
  lessons/round-1.md. Independent reviewer lane returned SHIP with all 13
  checklist items passing; added explicit drift-fail-closed clause post-review.
- 2026-09-28 — round 3: closed the AGENTS.md/dispatch-prompt gap filed in round-1
  corpus. SKILL.md gained an "Instruction surfaces" taxonomy (SKILL.md opt-in vs
  AGENTS.md always-on vs dispatch prompts one-shot), 2 cross-surface
  anti-patterns, checklist scope note, and 5 new source entries (3 previously
  unread bailian files now read in-body + AGENTS.md/prompt surfaces). Corpus:
  knowledge/agents-md-and-dispatch-surfaces.md, lessons/round-3.md, README gap
  list updated. Evidence: `cat`/`md5sum` of 6 shokunin AGENTS.md (identical
  5-line template), `diff` of .ufo/prompts/{kagi,kotoba}-L1.md, full reads of
  bailian-{docs-llm-wiki,managed-agent,sandbox}/SKILL.md, PROTOCOL.md file
  contract. Note: operator directive skipped round 2; LOG records actual rounds.
