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
- 2026-09-28 — round 7: mechanism-level correction + three new checklists,
  executed by 9 L2 lanes in one batch (MISSION.md minimum met: reviewer
  self-audit, critic drift recount, sentinel defect re-verify, executor ×2,
  scout ×2, connector routing map, planner AGENTS.md checklist).
  **Primary measurement** (scout lanes, L1 spot-verified): the `<skills>`
  description render is cache-or-truncate, not "model-compressed" as round 5
  claimed — `previewSkillDescription` does `slice(0,99)` + first-sentence
  (≥40 chars, no ellipsis) or last-space + `…`; an async LLM compressor fills
  `~/.omp/agent/skill-descriptions.db` (5/17 skills cached, key
  sha256(template+name+ws-description) reproduced 5/5). Compression activated
  2026-09-24→27 (earlier catalogues render verbatim 163–818 chars; current
  ≤98). Measured loss: 17.7% of description chars reach the router, 53/62
  quoted triggers lost, 13/13 `Triggers:`/反触发/`Excludes` clauses absent —
  all sit past the cliff. Also: 10681 compression-failure warns (99.92% Devin
  `invalid_argument`); two live catalogue variants coexist same-hour;
  godspeed offered 3911/3911 session_init records (round-6's 51.5% gap is
  opencode-side activation, not omp offer); `xbgst-surface` dead offer;
  `ufo` duplicate id (omp/agent copy wins); the six `*-shokunin` SKILL.md
  files are outside every discovery root — never routed at all.
  **Self-audit** (reviewer lane, verbatim 13-item checklist on own SKILL.md):
  7/13 clean, 4 fails + 1 ambiguous — all resolved same round (concrete
  sibling arbitration added to `description`; recipe-vs-prerequisite
  carve-out; bare-path citations grounded; "failure claim" defined).
  **New checklists landed**: dispatch-prompt (12 items, applied — 37/43
  prompt files fail ≥1; `<lane>` placeholders cost kake/kengaku canonical
  round-1 names; 38 files carry stale `m_composer`/`m_antigravity`/`m_grok`
  aliases; generator `shokunin-watchdog.sh` already fixed, artifacts stale)
  and AGENTS.md (8 items, applied — 6/6 repo files pass; host
  `~/.agents/AGENTS.md` fails: procedures at :18/:55, dated text :48/:51 —
  round-1 "zero procedures" claim corrected). SKILL.md rules 8→12 rewritten
  for the cliff (first-sentence exploit, reproduce-don't-assume, discovery-
  root gate); 4 new anti-patterns; Sources updated. **Drift recount**
  (critic): CLAUDE.md census 16→18 (+2 vendored); compression warns
  10191→10681; "byte-identical AGENTS.md" → shape-identical (6 distinct
  md5s, shared body hash equal). Artifacts:
  `corpus/knowledge/render-mechanism-round7.md`,
  `corpus/knowledge/dispatch-prompt-audit-round7.md`,
  `corpus/knowledge/alwayson-checklist-round7.md`, `lessons/round-7.md`.
  Cross-domain queue re-verified by sentinel lane: all sibling/agent-fleet
  defects still present (ufo.md cascade_note now 60d stale). `edit`
  boundary-echo recurred once (intro paragraph tail); caught by re-read.
- 2026-09-28 — round 9: axis move = **consistency** (lowest axis: harness-specific
  routing claims written as universal rules). 14 L2 lanes in two batched `task`
  calls (10 analysis/draft + 4 verification; MISSION.md floor 8): scouts
  (omp render census, opencode gate re-verify), 2 executors, scribe, planner,
  connector, critic ×2, reviewer ×2, sentinel ×2, distiller.
  **Drift measured first**: `sqlite3 -readonly ~/.omp/agent/skill-descriptions.db
  "select count(*) from skill_descriptions;"` → 17 rows (round 7: 5); the cache
  key's description salt is **style-aware** (`>-`/plain → ws-collapsed, `>` →
  +`"\n"` 5 keys, `|` → as-written+`"\n"` 1 key), so round-7's ws-normalised
  recipe reproduces only 11/17 and the correct one 17/17 → "the truncator is the
  default" is truncation-era. **Freeze was upgraded from [INFERENCE] to measured**:
  230 captured `<skills>` blocks show four signatures, monotone 3 ⊂ 5 ⊂ 11 ⊂ 17
  (19:37Z→21:00Z), one per session; kill-proof = L1's frozen catalogue holds a
  sekhmet-l3 render the live db has replaced, and the db's last write
  (20:57:58.180Z) landed 3.9 s after L1's session-start render (20:57:54.260Z).
  **Consistency landed**: `SKILL.md` gained `## Router model — which harness,
  which gate` (per-harness tag/render/offer gate/failure + check-before-predict
  recipe) and every cliff/render claim now names its harness (intro, frontmatter
  opener, rules 8/9, 3 anti-pattern rows). Measured before→after by an L2
  sentinel: 31 claim units, `UNSCOPED 9 → 0`, `UNSUPPORTED 7 → 6`, SCOPED 15 → 23,
  `<available_skills>` occurrences 0 → 3; the 6 residuals were re-worded in-round
  to cite the router model or be marked guidance/heuristic. A second L2 reviewer
  ran the 13-item trigger-fidelity checklist on SKILL.md itself: **13/13 pass**,
  0 ambiguous, with 2 citation fixes applied (split the `skill/index.ts`
  dedupe range to `:105-139`/`:235-246`; widen the session_init range).
  **Round-8's opencode mechanism sentences were re-verified and 3 corrected**:
  duplicates are last-parsed-wins under `concurrency:"unbounded"` (nondeterministic;
  154 vs 18 warn lines proof), name≠folder is not a gate (`NameMismatchError`
  dead code), the TUI never calls `fmt`. **Round-8 debt paid**: README rows for
  both round-8 artifacts + both lesson files, `lessons/round-8.md` written a
  round late, `SCORECARD.md` created (axes/planned/retired per AXES.md; consistency
  5→7), `SHONEN.md` regenerated to the canonical 4-box seed with one evidence
  line per box (all `[~]`). **Lane identity fixed**: repo-local
  `user.name=kotoba-shokunin`, `user.email=kotoba@shokunin.local` (round-7's
  `3b029b8` was a conformance defect under the operator identity). Counters
  re-run: warns 10681 → 10925, session_init 3911 → ~4032–4120 (live counter),
  opencode.db 415/216 and opencode.log 471 unchanged. Artifacts:
  `corpus/knowledge/harness-router-models-round9.md`,
  `corpus/knowledge/claim-scope-audit-round9.md`, `corpus/lessons/round-9.md`,
  report `../.ufo/reports/round-9/kotoba.md`.
