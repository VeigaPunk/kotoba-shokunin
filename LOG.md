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
- 2026-09-28 — round 4: extended the instruction-surfaces taxonomy 3→5 classes.
  New surfaces surveyed: `~/.config/opencode/agents/*.md` (18 files, 14–197
  lines; roster frontmatter with `subagents`/`cascade`/`permission_mode`;
  `NOT general-purpose. NOT explore.` negative routing in 7/18; identical
  9-line godspeed preamble in 13/18 — doubled in mutation-tester.md; stale
  dated `cascade_note` in ufo.md), `~/.config/opencode/command/*.md` (3 files;
  pointer-then-rules idiom + `agent:` key + `$ARGUMENTS`), and the round-N
  dispatch mode (`.ufo/prompts/*-round-*.md`, 3–4 lines vs 9–12-line spawn
  mode; `diff kake-round-4.md kasegi-round-4.md` shows name+path-only
  variance). SKILL.md gained 3 table rows, 2 evidence paragraphs, spawn-vs-round
  completeness rule, 6 anti-patterns, 3 source entries. Corpus: knowledge/
  agent-defs-commands-and-round-prompts.md, lessons/round-4.md, README gap
  list updated (5-class coverage; system-prompt/CLAUDE.md/MCP remain open).

- 2026-09-28 — round 5: first end-to-end domain task + round-1 defect repairs.
  Audit: an independent L2 reviewer lane applied the 13-item trigger-fidelity
  checklist verbatim to the 5 sibling `*-shokunin/SKILL.md` files (strict
  reading); L1 verified frontmatter items and every cited defect line.
  Result: all 5 fail — systemic template defect, all descriptions are
  `Domain specialist — scopes X` with zero quoted triggers/anti-triggers
  (items 2–3: 0/5), zero sibling arbitration (item 4: 0/5) despite named
  overlaps found (kagi↔kake CDP, kengaku↔bailian-docs-llm-wiki). 5
  checklist-ambiguity meta-findings filed and resolved in SKILL.md
  (prerequisite defined, action-cell rule replaces last-column rule, command
  scope widened, citation-base rule added, item 4 surface pinned to
  `description`). Defect repairs (aggregator audit queue): dropped the
  fabricated `bailian-train-deploy` 火山方舟/ark frontmatter quote (verified:
  the text exists nowhere in that file); scoped `requires.bins` claim to
  7-of-10 with named exceptions; replaced the unswept "counterexample none
  found" claim with a grep sweep + 2/16 counterexample rate
  (bailian-docs-llm-wiki body 何时使用/何时不要使用, bailian-model-recommend
  body 适用场景). Corpus: knowledge/fleet-skill-audit-round5.md,
  knowledge/harness-system-prompt.md (6th surface class — observed,
  not owned), lessons/round-5.md, README coverage+gaps updated. SHONEN.md:
  all 4 boxes ticked with evidence lines.
  Telemetry (scout lane + L1 re-verified): a real activation trace exists —
  `~/.local/share/opencode/opencode.db` `part` table, `$.tool='skill'` (415
  calls / 216 sessions / 11 skills; histogram re-run by hand matches:
  godspeed 239, wwkd 52, ufo 51, …); per-prompt attribution via
  `part.message_id → message`. Bigger find: the `<skills>` catalogue the
  router sees is a model-compressed render of `description` (~95–103 chars,
  template embedded at ~/.local/bin/omp ELF offset 283082932 — re-verified by
  `grep -abo`; 10191 compression-failure warns in ~/.omp/logs). SKILL.md
  gained the compressed-render caveat + front-load rule 8. Corpus:
  knowledge/skill-activation-telemetry.md.
- 2026-09-28 — round 6: three convergent moves. (a) Second end-to-end domain
  task: added a 9-item agent-definition fidelity checklist to SKILL.md and an
  independent L2 reviewer lane applied it verbatim to all 18
  `~/.config/opencode/agents/*.md` — 15/18 clean, 4 fail cells (ufo.md missing
  `name:` + stale `cascade_note` "until 2026-08-29", mutation-tester.md
  preamble doubled at lines 8-14+34-40, scout.md `aaron` bin absent from PATH),
  all L1 re-verified (`command -v aaron` empty; frontmatter greps). 10
  meta-findings resolved into the checklist (schema-not-list key rule,
  description-dated-text scope, same-name-differing-content blocks, file-path
  resolution, harness-literal carve-out). Audit corrected round-4 counts:
  godspeed preamble 13→14/18 (orch.md missed), negative routing 7→11/18.
  Artifact: `corpus/knowledge/agent-def-audit-round6.md`. (b) Seventh surface
  class: CLAUDE.md census — 16 files (5 operator-authored incl. a 4339-line
  outlier, 1 dispatch template, 10 vendored/cache); loader strings exist in
  both harness binaries (9/17 refs) but 0 captured injections — a cold
  always-on channel; SKILL.md gained a surfaces-table row. MCP/plugin
  surfaces verified absent (`opencode.json` key set; plugin/ = one nudge
  script). Artifact: `corpus/knowledge/claude-md-surface.md`. (c) First
  fidelity measurement: literal-trigger miss proxy over opencode.db (398
  sessions / 415 skill calls, command/directive text scrubbed) — unique-token
  triggers miss 0%; godspeed always-on coverage only 51.5%; domain-term
  names ambiguous (all 5 `ufo` misses are references, not calls). SKILL.md
  gained frontmatter rule 9 (invocation-shaped triggers for domain-term
  names). Artifact: `corpus/knowledge/trigger-miss-proxy-round6.md`.
  SHONEN.md re-attributed `[~]` self-asserted per PROTOCOL.md round-6 rule.
  Sibling defect re-check: all 5 sibling descriptions still unchanged
  post-audit (fleet still fails trigger items — fix remains cross-domain).
