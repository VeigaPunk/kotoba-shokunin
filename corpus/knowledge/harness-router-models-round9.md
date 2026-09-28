# The two harness router models, side by side — round 9

Sourced 2026-09-28 (round 9). Supersedes the round-5 "model-compressed render"
framing for the **omp** half and the round-7 **omission of an opencode half**.
Both harnesses read the same frontmatter `description`, but they render and gate
it differently, so every craft rule below is harness-qualified. Basis tags:
**[r7]** `render-mechanism-round7.md`, **[r8]**
`opencode-offer-trace-round8.md`, **[r9]** round-9 measurement on this host
(commands inline), **[r9-up]** upstream `github.com/sst/opencode` dev source read
2026-09-28, **[INFERENCE]** = not measured.

## Why this file exists — the round-9 drift

The omp description cache went **5 → 17 rows** between rounds 7 and 9, and the
`SKILL.md` rule that depended on the old number ("the truncator is the default")
was both stale and harness-unscoped.

```bash
sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select count(*) from skill_descriptions;"   # 17
stat -c '%y %s' ~/.omp/agent/skill-descriptions.db                                               # 2026-09-28 17:57:58, 12288 B
```

**Row count is not coverage — the key is checked, not counted.** The cache key is
`sha256(prompt_template ‖ 0x00 ‖ name ‖ 0x00 ‖ description)` where the
description is hashed **exactly as the YAML loader yields it**: the scalar style
decides — plain/`>-` → ws-collapsed, no trailing newline (11 of 17 here); `>` →
ws-collapsed + `"\n"` (5); `|` → literal with newlines + `"\n"` (1) — i.e. 6 of
17 keys are newline-bearing (omarchy, wwkd, xbrd-ask, sekhmet-l3, kimi-webbridge,
ufo). A ws-strip check
without the style rule reports 11/17 — round-7's recipe half-wrong — and invents
a staleness finding. With the style-aware rule, **all 17 keys reproduce against
today's on-disk descriptions**, every live description is >100 ws chars, and the
newest captured catalogue (2026-09-28T21:06:34Z, one full `<skills>` block)
renders **17/17 from cache, 0 truncations**. That is a snapshot measurement:
adding a skill or editing a description changes the key and re-opens the
truncator path. [r9]

```bash
# template recovered from the omp ELF by anchoring, not by offset (round 10):
#   the keyed prompt is the whole NUL-terminated bunfs file
#   `/$bunfs/root/compress-description-<hash>.md`, 273 bytes, sha256
#   c1f03c8e248eb40ec7735baab67f686fc2f254e00d2a0241ff220628461bdb51:
#     Compress into one routing hint of at most 12 words: WHEN to use; WHEN NOT
#     only if it prevents confusion. Retain recognizable trigger words. Do not
#     restate the skill name or market it. Output one line without bullets or
#     quotes.\n\nSkill: {{name}}\nDescription: {{description}}\n
#   round 9 quoted only the first line — the placeholders are part of the hash
# key rule: sha256(template ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)
# authority: readable embedded JS (A8n/H7s/ldl), round 10, not disassembly
```

**Catalogue freeze (measured).** Scanning 230 captured `<skills>` blocks across
`~/.omp/agent/sessions/**` yields exactly four live signatures, monotone in
time: 3/17 cache rows (≤19:37Z) → 5/17 (19:51–20:38Z) → 11/17 (20:53–20:56Z) →
17/17 (21:00Z+); within a session the signature never changes, and the newest
block is 17/17 cache with 0 truncations. L1's own round-9 session froze earlier:
its catalogue carries **14 cache renders and 3 truncations** (omarchy, wwkd,
xbrd-ask), and for at least one key (sekhmet-l3) the text it froze on has since
been *replaced* in the db — a stale frozen string next to the live row. [r9]

**Consequence of the key including the description:** a byte-changing edit to a
`description` invalidates its row, so that skill can revert to the truncator
until recompression lands — a healthy edit can temporarily *lose* the render it
had. Same-key edits and an already-completed async write are exceptions. [r9]

## omp

- **Tag:** `<skills>` (ELF template `- {{name}}: {{description}}`). [r7]
- **Render:** `cache.get(key) ?? previewSkillDescription(description)`.
  `previewSkillDescription` = ws-collapse (`replace(/\s+/g," ").trim()`);
  `len <= _8n` (`_8n=100`) → verbatim; else `s = t.slice(0, _8n-1)` (offset 99);
  first `[.!?]`-sentence kept **only if ≥40 chars, no ellipsis**; else cut at the
  last ASCII space + U+2026 `…`. Constants `_8n=100, idl=160, adl=12` (anchors on
  the shipped binary — ELF offsets drift across builds). The cache write is
  fire-and-forget: a miss emits the truncation and the compressor's row lands
  later. [r7; literals re-verified round 9]
- **Offer gate:** a `SKILL.md` under a discovery root (project walk-up
  `.agent/skills`/`.agents/skills` + user home, `.claude/skills`,
  `~/.claude/plugins/cache`); `description` undefined ⇒ not offered; duplicate
  names resolve by root order (`~/.omp/agent/skills/ufo` wins over
  `~/.config/opencode/skills/ufo`). A file outside every root (e.g. this repo's
  `*-shokunin/SKILL.md` set) is never offered — its description craft is
  audit-hygiene, not routing. [r7]
  **Round-10 correction:** `~/.agents/skills` is the root that carries 15 of the
  17 offered names (round 9 named only `.agents/skills` in passing) and
  `~/.omp/agent/skills` carries the other two; the 17-row cache is exactly this
  union. Two entries there (`sekhmet`, `xbrd`) are dangling symlinks and are
  therefore not offered — `verifiers/` records that count instead of ignoring it.
- **Failure modes (cache-miss path):** hard cliff at offset 99 (chars ≥99
  contribute 0; effective keep 55–96, mean 83.9); 53/62 quoted trigger spans
  lost, 0/13 `Triggers:`/反触发/`Excludes`/`不用于` markers survive; CJK worse
  (`[.!?]` excludes `。；：` → mid-clause cut at an incidental ASCII space). [r7]
- **Verify:**
  ```bash
  sqlite3 -readonly ~/.omp/agent/skill-descriptions.db "select length(description), description from skill_descriptions;"
  grep -ho '<skills>' ~/.omp/agent/sessions/**/*.jsonl | wc -l    # catalogue blocks in captured sessions
  grep -rh '"type":"session_init"' ~/.omp/agent/sessions/ | wc -l   # counter drifts inside a round: re-run
  python3 verifiers/verify_harness_claims.py   # round 10: the three probes above as pass/fail checks
  ```

## opencode

- **Tag:** `<available_skills>` for the verbose system-prompt catalogue
  (`skill/index.ts:326/336`). The literal `<skills>` occurs 0 times in the
  opencode tree — sweep: `git clone --depth 1
  https://github.com/sst/opencode && grep -rn '<skills>' --include=*.ts
  --include=*.tsx --include=*.txt opencode/packages | wc -l` → 0 (dev, read
  2026-09-28) — so a `<skills>` grep on opencode can never hit. The non-verbose
  branch renders `## Available Skills` + `- **name**: description` and has **no
  production caller** (tests only). [r9-up]
- **Render:** `description` passed through **untruncated** — full frontmatter
  bytes + escaped absolute `<location>` (`skill/index.ts:332-333`). No 99-char
  cliff, no cache. Repo-wide, every `Truncate` use targets tool output or
  compaction; the system prompt is a plain `join("\n")` (`session/llm.ts:126`).
  The TUI skill list reads `app.skills({})` and does
  `description?.replace(/\s+/g," ").trim()` (`tui/.../dialog-skill.tsx:41`) —
  whitespace collapse only, never truncation. [r9-up]
- **Offer gate (four conditions, all file- or permission-side):**
  1. `description` defined — `list.filter(s => s.description !== undefined)`
     (`skill/index.ts:322`);
  2. frontmatter parses with a string `name:` (`isSkillFrontmatter`,
     `:53-60/:123`) — **folder-name equality is not checked**:
     `NameMismatchError` (`:67`) is declared and never thrown, so
     `…/foo/SKILL.md` declaring `name: bar` is offered as `bar`;
  3. the `skill` permission is not disabled for the agent (`session/system.ts:108`;
     per-skill deny filtered at `skill/index.ts:314`);
  4. it wins the by-name dedupe — which is **nondeterministic**: the duplicate
     assignment is unguarded (`:125-139`, last parsed wins) and discovery runs
     `Effect.forEach(…, {concurrency:"unbounded"})` (`:240-242`). Round-8's
     "first-scanned wins" is wrong; live proof (same file set, same log):
     `.claude/skills/<name>` is the early copy in 154 warn lines (13 runs) and
     the late copy in 18 (5 runs) — `grep 'duplicate skill name'
     ~/.local/share/opencode/log/opencode.log | grep -c 'existing=/home/vgpnk/.claude'`
     → 154; `… | grep -c 'duplicate=/home/vgpnk/.claude'` → 18. [r9-up]
- **Failure modes:** no verbatim offer record persists (the catalogue is
  assembled in `prompt.ts` and discarded; the `session_context_epoch` table
  exists but this build's migrations wipe it, 0 rows), so offer is measured
  indirectly — `message=init count=N` per instance plus reconstruction of the
  root union (17 on disk + builtin `customize-opencode` = 18). [r8]
- **Verify:**
  ```bash
  grep -o 'message=init count=[0-9]*' ~/.local/share/opencode/log/opencode.log | sort | uniq -c  # 15×1 16×141 17×34 18×14
  grep -c '<available_skills>' ~/.local/share/opencode/log/opencode.log   # 0 — never logged
  python3 verifiers/verify_harness_claims.py   # round 10: init count vs root union + builtin, dup split
  ```

## Cross-harness craft rules

1. **A description safe under the omp cliff is safe on opencode — not the
   reverse.** An opencode-perfect long description can lose its whole trigger
   list on omp whenever the cache misses. [r7+r8]
2. **Front-load the capability + the match-critical WHEN into the first ~99
   ws-collapsed chars** (≤95 after last-space back-off). Later bytes are
   invisible on the omp cache-miss path and simply redundant on opencode. [r7]
3. **Editing a description re-rolls the omp render.** The cache key includes the
   description; expect a truncator render until a new row lands, so a
   front-loaded draft must survive the cliff *before* the compressor catches up. [r9]
4. **Frontmatter anti-triggers help opencode; on omp they are dead weight past
   the cliff.** WHEN-hint first, WHEN-NOT only if it fits. [r7]
5. **Never rely on the body to fix routing.** Both routers read only the
   frontmatter `description`; a body-only trigger or anti-trigger changes
   neither offer nor render. [r7+r8]
6. **`description` is the offer gate on both, but the failure is silent on
   opencode** (a skill without one vanishes from the catalogue with no warn);
   duplicate names resolve by loader order — silent on omp, warned-but-
   nondeterministic on opencode. One copy per name, one owner per root. [r7+r8]
7. **A CJK description pays an extra tax on omp** (`[.!?]` excludes `。；：`, so
   the cut lands mid-clause); opencode is unaffected. Keep the CJK routing clause
   inside the first ~40 chars. [r7]
8. **State the harness before predicting a render.** "The router sees …" is not
   a fact about this host: omp truncates/caches, opencode does not. [r9]

## Unknowns

- Whether the model *attends* to the untruncated opencode description (rendering
  is measured; routing benefit is not).
- Per-render activation attribution: no per-session offer→activation join exists
  on either harness, so "does a cached render route better than a truncation?"
  has no test.
- The exact content of the opencode `init count` 16/17-name sets (only the
  15/18 endpoints were enumerated). [r8]
- Whether the Aug-2026 binary rendered the omp catalogue identically (code path
  and log formats match → [INFERENCE]).
- The `skill-descriptions.db` main-file mtime is **not** last-write: the file is
  WAL-mode (a `-shm` touch, 0 B `-wal`), so `17:57:58` is a lower bound for row
  landings. [r9 **[INFERENCE]**]
- Systematic CJK survival rate on omp (observed per render, never counted). [r9]