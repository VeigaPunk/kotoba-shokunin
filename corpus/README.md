# kotoba-shokunin corpus

Domain: prompt & skill craft — SKILL.md/AGENTS.md quality, trigger fidelity.

## Coverage map

| Area | File | Basis |
|------|------|-------|
| Frontmatter trigger surfaces | `knowledge/frontmatter-trigger-surface.md` | 16 production skill files surveyed 2026-09-28 |
| Skill anatomy & compression | `knowledge/anatomy-and-compression.md` | same survey; line counts 18–392 |
| Failure/anti-pattern patterns | `knowledge/fail-closed-and-anti-patterns.md` | bailian family, ufo, sekhmet-l3 |
| AGENTS.md & dispatch prompts | `knowledge/agents-md-and-dispatch-surfaces.md` | 6 child AGENTS.md + `~/.agents/AGENTS.md` + 8 `.ufo/prompts/*-L1.md` |
| Agent defs, commands & round-N prompts | `knowledge/agent-defs-commands-and-round-prompts.md` | 18 `opencode/agents/*.md` + 3 `opencode/command/*.md` + 6 `*-round-N.md` |
| Fleet SKILL.md audit (round-5) | `knowledge/fleet-skill-audit-round5.md` | 13-item checklist applied to 5 sibling `*-shokunin/SKILL.md`, strict + refined readings |
| Harness system prompt (6th class) | `knowledge/harness-system-prompt.md` | observed-not-owned; notes from this session's injected preamble |
| Activation telemetry & compressed router surface | `knowledge/skill-activation-telemetry.md` | opencode.db `part` (415 calls / 216 sessions, re-verified round 9), opencode.log permission lines (471), omp session jsonl; the row's `~95–103 chars` render-size claim is round-5 truncation-era — round 9 measures 17 cache rows of 44–98 chars against 163–818-char sources |
| Trigger-miss proxy (round-6) | `knowledge/trigger-miss-proxy-round6.md` | opencode.db 398 sessions: literal-trigger coverage + godspeed always-on hole (51.5%) |
| CLAUDE.md surface (7th class) | `knowledge/claude-md-surface.md` | 16-file census; loader strings in binaries, 0 captured injections |
| Agent-def audit (round-6) | `knowledge/agent-def-audit-round6.md` | 9-item checklist applied to 18 `opencode/agents/*.md` |
| Render mechanism & trigger survival | `knowledge/render-mechanism-round7.md` | omp binary reverse-engineered (ELF strings): cache-or-truncate render, `slice(0,99)` cliff, 14 catalogues / 3911 session_init census; round-7 loss figures (17.7% of chars, 53/62 quoted spans, 13/13 `Triggers:` clauses) are truncation-era; cache tier re-measured round 9: 17 rows and all 17 keys reproduce against on-disk descriptions (style-aware YAML salt), newest captured catalogue (2026-09-28T21:06Z) renders 17/17 from cache with 0 truncations |
| Dispatch-prompt audit + checklist | `knowledge/dispatch-prompt-audit-round7.md` | 12-item checklist applied to 43 `.ufo/prompts/*.md` (37 fail) + resolvability sweep incl. generator bugs |
| Always-on checklist + self-audit | `knowledge/alwayson-checklist-round7.md` | 8-item AGENTS.md checklist (host file FAIL); 13-item self-audit of SKILL.md (4 fails cured); drift recount table |
| Round-7 lessons | `lessons/round-7.md` | LOG.md round-7, commit `round-7`, report `../.ufo/reports/round-7/kotoba.md` |
| Round-5 lessons | `lessons/round-5.md` | LOG.md round-5, commit `round-5`, report `../.ufo/reports/round-5/kotoba.md` |
| Round-6 lessons | `lessons/round-6.md` | LOG.md round-6, commit `round-6`, report `../.ufo/reports/round-6/kotoba.md` |
| opencode offer trace (round-8) | `knowledge/opencode-offer-trace-round8.md` | opencode ELF + global skill roots + `message=init count=N` log line; godspeed offered 387/387 attested sessions, activated 205/399 = 51.4%; round-6's empty `<skills>` search explained (opencode's tag is `<available_skills>`) |
| Sibling description rewrites (round-8) | `knowledge/sibling-description-rewrites-round8.md` | 5 drop-in `description:` blocks (one per sibling `*-shokunin/SKILL.md`) with reproduced H7s renders and pinned md5s; producer-ready, not applied (cross-domain) |
| Harness router models (round-9) | `knowledge/harness-router-models-round9.md` | per-harness tag/render/gate/failure tables + verify recipes: omp `<skills>` = `cache.get(key) ?? previewSkillDescription` (99-char cliff, keep 55–96) vs opencode `<available_skills>` = untruncated `description` + `<location>`; offer gates differ (omp: dir in a discovery root; opencode: `description` defined + `skill` permission enabled, dedupe by name is nondeterministic); supersedes the round-5 omp framing and the round-7 opencode omission; carries the round-9 key-reproduction nuance and the WAL caveat on the db mtime |
| Harness-claim scope audit (round-9) | `knowledge/claim-scope-audit-round9.md` | consistency measurement, before → after: 31 claim units swept by marker (`router`, `cliff`, `<skills>`, `slice(0,99)`, `render`, `truncat`, `catalogue`, `compressed`, `99`, `sees`) and classified SCOPED / UNSCOPED / UNSUPPORTED; before-state on `SKILL.md` @ `143fe473…` (487 lines) = 15 SCOPED / 9 UNSCOPED / 7 UNSUPPORTED with 0 `<available_skills>` occurrences; after-state grep counts + the landed `## Router model` table |
| Round-8 lessons | `lessons/round-8.md` | LOG.md round-8 entry (never written — see the lesson), commit `8c300ad`, report `../.ufo/reports/round-8/kotoba.md` |
| Round-9 lessons | `lessons/round-9.md` | LOG.md round-9 entry, commit `ROUND9_COMMIT`, report `../.ufo/reports/round-9/kotoba.md` |

## Known gaps

- Implicit-intent fidelity is still unmeasured — the literal-trigger proxy
  (round-6) covers only prompts that name a skill. Needs an intent-labeling
  pass; the join recipe is proven.
- MCP tool descriptions: no `mcp` config exists on this host (opencode.json
  key set verified 2026-09-28) — the surface class is absent, not just
  unsurveyed. Plugin manifests: `~/.config/opencode/plugin/` holds one
  unrelated nudge script, no manifest conventions to survey.
- Sibling arbitration gap is *measured and persisted*: named overlaps exist
  (kagi↔kake CDP, kengaku↔bailian-docs-llm-wiki); 0/5 descriptions carry an
  arbitration clause, still true at round-7 sentinel re-check. Fixes are
  cross-domain — routing map in `knowledge/alwayson-checklist-round7.md` +
  the round-7 report. The mint-template producer itself has no identified
  owner (integrator assignment needed).
- opencode-side offer is now measured (round 8): godspeed offered 387/387
  attested sessions (100%) against activation 205/399 = 51.4%, so the round-6
  "51.5% coverage" gap is model choice on the consume side, not an offer hole.
  What remains open is per-render consumption attribution — no per-session
  offer→activation join exists on either harness.
- The render cliff is measured for the 17 offered skills; round 9 finds all 17
  cache keys reproduce against on-disk descriptions, so there is no live
  truncation tier to compare against — whether the cached one-liners route
  better than the descriptions would is unmeasured (no per-render activation
  attribution exists).
