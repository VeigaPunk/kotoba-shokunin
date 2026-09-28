# The omp description-render mechanism — reverse-engineered, round 7

Sourced 2026-09-28 (round 7), L2 scout lanes `ScoutRenderSurvival` +
`ScoutCatalogueCensus`; key claims L1 re-verified. Supersedes the round-5
"model-compressed render" framing in `skill-activation-telemetry.md` —
compression is real but is the *minority* path on this host. Full lane
artifacts: `/tmp/kotoba-r7/scout-renders.md`, `/tmp/kotoba-r7/scout-catalogue-census.md`.

## Mechanism — two render paths in `skill-descriptions.ts`

Embedded unminified source recovered via `strings -n 6 ~/.local/bin/omp`
(omp 18.4.2, 285672928 B, mtime 2026-09-28 15:14, BuildID
`5afca2666bfab8605a934f1b6231dacae0518a5f`):

1. **Deterministic truncator** `previewSkillDescription` (H7s), strings line
   684191-684199, ELF region @177145052:
   `t = ws-collapse(description); if len<=100 return t; s=t.slice(0,99);`
   then `o = s.match(/^.*?[.!?](?=\s|$)/)` — **first sentence wins if ≥40 chars,
   NO ellipsis** — else cut `s` at last ASCII space and append U+2026 `…`.
   Constants @177147479: `_8n=100, idl=160, adl=12`.
   L1 reproduced byte-exact on kotoba's own 756-char description →
   `Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
   dispatch prompts /…` (104 incl. `…`): every quoted trigger string lost.
2. **LLM compressor** (j7s, `smol`-role model, maxTokens 1024, temp 0, 30 s
   abort; validator: single line ≤160 chars, ≤12 words). Cache:
   `~/.omp/agent/skill-descriptions.db`, key =
   `sha256(prompt_template \0 name \0 ws-normalised description)` — all 5
   present rows key-reproduced by the scout lane. Compression is
   fire-and-forget: the render that misses the cache emits H7s and a
   background write lands later.
3. **Catalogue template** @283082932: `- {{name}}: {{description}}` inside
   `<skills>`; description field = `cache.get(key) ?? H7s(description)`.

## Measured (compressed era, 17-skill catalogues)

- **Hard cliff, not a gradient:** source chars ≥ offset 99 contribute 0 to
  all 14 H7s renders; effective keep 55–96 chars (mean 83.9) after last-space
  back-off. A first `.`/`!`/`?` sentence ≥40 chars keeps *only* that sentence
  (godspeed: keeps sentence 1, drops the trigger list in sentence 2).
- **Trigger loss:** 53/62 quoted trigger spans absent from renders (85.5%);
  the 9 survivors are incidental substrings. 13/13 `Triggers:`/反触发/
  `Excludes`/`不用于` clause markers — **0 survive**. Worst: wwkd 0/7
  (`plan this`, `/wwkd`, …), ufo 0/6, omarchy loses a 20-item trigger list +
  `Excludes` clause (`Use when` fell 1 char past the keep at 87).
- **Compression telemetry:** 10681 `Skill description compression failed`
  warns (99.92% `Devin stream error invalid_argument`), 304 pids,
  2026-09-24→09-28 (`grep -rh 'Skill description compression failed'
  ~/.omp/logs/ | wc -l`). Only 5/17 skills have a cached LLM render.
- **Regime change:** catalogues dated ≤2026-09-24 render descriptions
  verbatim (163–818 chars, 17/17 byte-identical to sources); catalogues dated
  ≥2026-09-27 render ≤98 chars. Compression activated between 09-24 and
  09-27 on this host.
- **Non-determinism:** two live 17-skill catalogues coexist same-hour
  (`48ff8c9eeaef` 42 files vs `aea95a70f738` 83 files), differing only in the
  2 skills whose cache rows landed between them. Session prompt prefixes
  freeze the render at session start [INFERENCE from file granularity].
- **Offer coverage (omp):** godspeed offered in **3911/3911** session_init
  records, 14/14 catalogues — the round-6 51.5% godspeed coverage gap is
  opencode-side activation, NOT an omp offer hole. 3911 session_init records,
  14 distinct catalogues, 4 membership signatures (15/16/17-skill sets as
  skills installed over time).
- **Dead offers:** `xbgst-surface` was offered in 2264 records through
  2026-09-08 with no SKILL.md under any global root (project-scoped source).
- **`ufo` duplicate id:** `~/.omp/agent/skills/ufo/SKILL.md` (605-char desc)
  wins over `~/.config/opencode/skills/ufo/` (434) — the render proves which
  copy omp loads. `~/.agents/skills/{sekhmet,xbrd}` are dangling symlinks
  (verified L1: targets under ufo-fsd-alpha absent) — dir name ≠ skill name;
  they contribute 0 catalogue entries.
- **Shokunin skills never render:** the six `*-shokunin` SKILL.md files sit at
  repo roots, not in any omp discovery root (`.agent/skills`,
  `.agents/skills` project walk-up + user home, `.claude/skills`,
  `~/.claude/plugins/cache`). Their `description` trigger craft is invisible
  to the omp router entirely — activation is by steer/dispatch, not routing.

## Craft consequences (revised rules)

- **The 99-char cliff is the real constraint.** Put a complete routing hint
  in the first ≤99 ws-collapsed chars — the truncator keeps nothing later.
  First-sentence semantics: one sentence ≥40 chars ending before 99 keeps
  verbatim WITHOUT ellipsis; otherwise last-space cut + `…`.
- **Quoted triggers still pay** — but only inside the first ~99 chars, or via
  the LLM cache when it lands (sibling-home cache row kept
  `"plan this", "break this down", "/wwkd"` for wwkd). Below 99 chars they are
  verbatim; past it they are gone.
- **Anti-triggers past the cliff are dead weight for routing** — but the LLM
  prompt says "WHEN NOT only if it prevents confusion", so a cached render
  may keep a short exclusion. Budget: WHEN-hint first, WHEN-NOT second only
  if it fits the window.
- **CJK descriptions hit a worse edge**: `[.!?]` sentence detection excludes
  `。；：`, so CJK text cuts at an incidental ASCII space mid-clause (observed:
  549→44 chars).
- **Verify by reproduction, not logs**: re-run H7s (recipe above) on a new
  description to see the actual router view; the sqlite cache table lists
  which skills escaped truncation.
