# Skill activation telemetry & the compressed router surface

Sourced 2026-09-28 (round 5) by read-only scout lane + L1 verification.
Two load-bearing facts for this domain: (1) activation telemetry exists on
this host and per-prompt attribution works; (2) the router never sees raw
`description` bytes — it sees a model-compressed render.

## Fact — the `<skills>` catalogue is a compressed render, not source text

**ROUND-7 SUPERSESSION:** the "model-compressed" framing below is only half
the mechanism. Round 7 (`render-mechanism-round7.md`) proved the render is
cache-or-truncate: 5/17 skills carry LLM cache rows; 12–14 render by
deterministic `slice(0,99)`+`…` — and the compression did not exist before
2026-09-27 (earlier catalogues render descriptions verbatim). Treat the
measured sizes below as that era's snapshot.

- The template is embedded plaintext in the omp ELF
  (`~/.local/bin/omp`, byte offset 283082932, found via `grep -abo '<skills>'`):
  `{{#each skills}}- {{name}}: {{description}}{{/each}}` with the directive
  "you MUST read `skill://<name>` before proceeding". Not found in
  `~/.opencode/bin/opencode` or `pi_natives` — the prompt is omp's.
- Rendered catalogues live in `session_init.systemPrompt` records
  (`~/.omp/agent/sessions/**/*.jsonl`, 3837 records) and in 32 raw
  request captures (`~/.omp/logs/http-400-requests/*.json`,
  `.body.messages[role=system].content`).
- Measured render sizes (newest capture vs source `description`):
  wwkd 820→96, bailian-cli 681→79, omarchy 660→87, bailian-gen 578→56,
  godspeed 163→91, ufo 436→93 chars. Rendered lines cap ~95–103 bytes;
  compression is a *model call* (rewrites, not truncates — godspeed's render
  is a paraphrase), and it has a logged failure mode: 10191
  `"Skill description compression failed"` warns across `~/.omp/logs/`.

**Craft consequence (opinion):** `description` bytes are *input to a
compressor*, not router-visible text. Front-load the match-critical clause in
the first ~95 chars; a trigger string or anti-trigger placed late in a long
description may be paraphrased away. Verbatim trigger strings still earn
their place (they give the compressor salient tokens to keep), but nothing
past the render window is guaranteed.

## Fact — a real activation trace exists; fidelity is measurable

Primary store: `~/.local/share/opencode/opencode.db` (sqlite, WAL).
Per-call activation = `part` rows where `json_extract(data,'$.tool')='skill'`;
skill name at `$.state.input.name`, resolved dir at `$.state.metadata.dir`.
Join `part.message_id → message.id` for the user prompt text,
`message.data.agent`/`model` for the lane. Verified example session
`ses_fb0f5491…`: one user prompt → godspeed, ufo, bailian-cli,
bailian-protocol, wwkd loads within 22s.

Observed histograms (2026-08-28 → 2026-09-28 window):

| Store | Signal | Totals |
|-------|--------|--------|
| opencode.db `part` | tool='skill' calls | 415 calls, 216 sessions, 11 skills: godspeed 239, wwkd 52, ufo 51, customize-opencode 27, bailian-protocol 15, bailian-cli 13, xbrd-ask 8, sekhmet-l3 4, omarchy 4, xbgst-surface 1, bailian-docs-llm-wiki 1 |
| opencode.log | `message=evaluated permission=skill pattern=<name>` | 471 lines; same ranking |
| omp session jsonl | `tool_execution_start`/`toolCall` args `skill://X` | 5609 files, 5137 with ≥1 ref |
| agent.db `command_usage` | `skill:<name>` slash counts | ufo 99, godspeed 4 |

Query recipe (read-only):
`sqlite3 -readonly opencode.db "select json_extract(data,'$.state.input.name') from part where json_extract(data,'$.tool')='skill'"`

## Fact — secondary signals worth knowing

- **Loader collisions**: 1898 `duplicate skill name` WARNs in opencode.log —
  same skill name under `.claude/skills/` vs `.agents/skills/` vs
  `.config/opencode/skills/`. Description arbitration cannot fix a
  loader-level resolution order.
- **Phantom activation**: `customize-opencode` fired 27–28× across stores but
  has no SKILL.md in surveyed roots — an activation source outside the file
  survey set.
- **Blind spots**: `stats.db tool_calls` records `args_chars` but not args
  (skill loads surface only as `read`); `message` table stores no system
  role, so the *offered* catalogue must be recovered from omp jsonl
  `session_init.systemPrompt`, not opencode.db. `agent.db` has detected
  page/index corruption (`pragma quick_check` fails) — gate integrity before
  trusting it.

## What this does NOT yet answer

False-negative rate (prompts that needed a skill but got none) is measurable
in principle — join user prompts to per-session skill loads — but requires
classifying prompt intent at scale. Deferred: the join recipe is proven; the
labeling pass is a future round's work.
