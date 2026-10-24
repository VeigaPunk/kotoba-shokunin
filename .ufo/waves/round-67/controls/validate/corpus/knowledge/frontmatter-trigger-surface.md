# Frontmatter trigger surfaces

Falsifiable claims about `description:` fields, observed 2026-09-28.

## Fact 1 — Three trigger kinds coexist in mature descriptions

- **Literal invocation strings**, quoted: `"/wwkd", "plan this", "break this
  down"` — `~/.agents/skills/wwkd/SKILL.md` frontmatter.
- **Named domain triggers**, quoted: `Triggers: "sekhmet", "swarm", "L3", "fan
  out", "parallel probes", "spark"` — `~/.agents/skills/sekhmet-l3/SKILL.md`.
- **Implicit need phrases** (user describes the goal, never names the tool):
  the frontmatter carries the clipped forms `"做一个XX"`, `"实现XX功能"` in its
  `触发词` list; the fuller phrase `"我想做一个XX"` appears only in the body
  适用场景 list (L23) — `~/.agents/skills/bailian-model-recommend/SKILL.md`.
  Audit note: the quoted long form is body-sourced, not frontmatter.
## Fact 2 — Anti-triggers live in `description`, not only the body

- omarchy: `Excludes Omarchy source development in ~/.local/share/omarchy/` —
  `~/.agents/skills/omarchy/SKILL.md` frontmatter.
- bailian-gen: `反触发：普通问答、编程、写作、翻译不走本技能` — frontmatter.
- bailian-cli: `不要用于普通问答、编程、写作、翻译、摘要、泛搜索` — frontmatter.

Counterexamples (observed, weaken the rule):
- bailian-train-deploy: exclusion table `## 反触发表` lives at body L42+ —
  frontmatter carries no exclusion clause.
- bailian-docs-llm-wiki: frontmatter description is all-positive; the
  anti-trigger list `## 何时不要使用` sits at body L28–35.

Reason (opinion): the router surface is the description; body-level exclusions
cannot prevent activation, only correct it after the fact. The 2-of-10
exceptions suggest body restatement is used as a second-layer safety net for
router error — redundancy, not a substitute.

## Fact 3 — Sibling arbitration clauses name the neighbor and the rule

- bailian-model-recommend: `当用户同时涉及模型查询和模型选择时，优先使用本
  skill（本 skill 内部会读取模型数据完成推荐）` — names bailian-docs-llm-wiki
  as the overlapping sibling and states who wins.
- bailian-web-search frontmatter lists five sibling routes with `→` arrows.

## Fact 4 — Always-on skills override the trigger assumption explicitly

- godspeed: `Use on every prompt, including nested and delegated prompts,
  without waiting for a keyword` — `~/.agents/skills/godspeed/SKILL.md`.

## Fact 5 — Runtime deps go in metadata, not prose

- `metadata.requires.bins: ["bl"]` in 7 of 10 `bailian-*/SKILL.md` (the
  exceptions: docs-llm-wiki, model-recommend, train-deploy carry no
  `requires:` key); `compatibility: 需要已安装 bailian-docs-llm-wiki skill` on
  bailian-model-recommend; ufo uses `metadata:` keys for axis_family /
  language / substrate.

## Craft rules — moved from `SKILL.md` § Frontmatter craft (round 15)

The twelve rules and the render measurement behind them. `SKILL.md` keeps the
five that carry most of the weight plus the pointer; this is the authoritative
copy, and the line-budget box in `SKILL.md` § Trigger-fidelity checklist is what
forced the move (`file ≤ ~600 lines` — the file was 675 at round-15
pre-registration commit `63ceba7`).

**The render, measured.** On **omp** the router ingests `description` through a
**cache-or-truncate** render (mechanism proven from the omp binary,
`corpus/knowledge/render-mechanism-round7.md`): if a
`sha256(prompt ‖ 0x00 ‖ name ‖ 0x00 ‖ loader-held description)` row exists in
`~/.omp/agent/skill-descriptions.db`
the render is that LLM one-liner (≤160 chars, ≤12 words); otherwise a
deterministic truncator keeps at most 99 chars — first sentence wins if ≥40
chars, else last-space cut + `…`. Measured over the live 17-skill omp
catalogue: only 17.7% of source description chars reach the router, 53/62
quoted trigger spans are lost, and all 13 `Triggers:`/反触发/`Excludes`/不用于
clause markers sit past the cliff — none render (round-7 measurement; round 9
adds the drift: cache coverage 5/17 → 17/17 rows, so the truncator is now the
fallback, not the default — a session started before a row landed still shows
the truncation. Round 10 re-read the salt from the shipped JS: it is the
**loader-held** description (`>`/`|` keep their trailing newline, `>-`/plain do
not), so a uniform ws-collapse check reproduces 11/17 and invents staleness;
`verifiers/verify_harness_claims.py` checks all 17, and 17/17 lines of the newest
captured catalogue render from cache). On **opencode** the full `description`
reaches the model
untruncated, so front-loading there is style, not survival; trigger strings and
anti-triggers stay mandatory on both, because the offer gate and the model's own
matching both read the description. Field rules distilled from the survey and
this measurement:

1. **Capability first, triggers second.** One clause naming what the skill does
   ("xbreed ask — optional cross-model advisory protocol"), then trigger
   material.
2. **Quote literal trigger strings.** `Triggers: "sekhmet", "swarm", "L3", "fan
   out"` (sekhmet-l3); `"/wwkd", "plan this", "break this down"` (wwkd). Quoted
   strings match how routers and humans actually phrase intent (design
   guidance — no matcher-level measurement exists for either harness).
3. **Include implicit-intent triggers.** bailian-model-recommend activates on
   `"做一个XX"` in its frontmatter 触发词 (the fuller `"我想做一个XX"` sits in
   its body 适用场景). If users arrive without naming the skill, the
   description must catch the *need*, not the name.
4. **Co-locate anti-triggers.** Most surveyed files carry exclusions in the
   description itself: omarchy "Excludes Omarchy source development",
   bailian-gen "反触发：普通问答、编程、写作、翻译不走本技能". Observed
   exceptions (2 of 10 bailian files): bailian-train-deploy and
   bailian-docs-llm-wiki keep exclusion lists only in the body (反触发表 /
   何时不要使用) — a second-layer net for router error, not a substitute:
   an anti-trigger in the body but not the frontmatter still causes false
   activation — the catalogue is built from frontmatter only (see `SKILL.md`
   § Router model).
5. **State sibling boundaries when overlap exists.** bailian-model-recommend:
   "当用户同时涉及模型查询和模型选择时，优先使用本 skill". Naming the neighbor
   and the arbitration rule prevents double-activation.
6. **Always-on skills say so explicitly.** godspeed: "Use on every prompt …
   without waiting for a keyword." If activation is unconditional, the
   description must override the trigger assumption, not rely on it.
7. **Declare runtime needs in metadata, not prose.** `metadata.requires.bins:
   ["bl"]` on 7 of 10 bailian skills (docs-llm-wiki, model-recommend and
   train-deploy omit `requires:`), `compatibility:` on model-recommend.
   Machines read metadata; prose warnings get skipped.
8. **On omp the 99-char cliff is absolute — write for the truncator, not the
   compressor.** Anything past ws-collapsed offset 99 is invisible whenever the
   cache misses: 0 chars survive in all 14 measured truncations; effective keep
   is 55–96 (last-space back-off). Put the capability clause + the most
   match-critical WHEN material in the first ≤99 chars; everything later is
   only reachable if the async LLM cache has landed *for this session's
   catalogue* — coverage is time-varying (5/17 rows at round 7; 17 rows at round
   9, all 17 keys reproduced against today's on-disk descriptions) and the cache
   key includes the description, so **editing a `description` invalidates its row
   and reverts that skill to the truncator** until the compressor writes a new
   one. The cache path also rewrites, so late text may return paraphrased, not
   verbatim. opencode has no cliff: its system-prompt catalogue renders the full
   description. CJK
   edge (omp only): the sentence regex knows only `[.!?]`, so 。；： don't count
   and CJK text cuts mid-clause at an incidental ASCII space (549→44 observed).
9. **Exploit the omp first-sentence branch.** If the first `.`/`!`/`?` sentence
   is ≥40 chars it renders whole with NO ellipsis — a clean complete hint
   (godspeed does this: keeps "Use on every prompt…" verbatim). But the same
   branch *discards* sentence 2+: godspeed's own trigger list sits in its
   second sentence and is gone. Put trigger material inside sentence 1 or
   accept the loss.
10. **Verify the render by reproduction, not assumption.** H7s is ~10 lines —
    re-run it (recipe in `corpus/knowledge/render-mechanism-round7.md`) or
    read the newest *catalogue-bearing* `<skills>` block under
    `~/.omp/agent/sessions/**/*.jsonl` — newest-mtime is not the rule; the
    newest file often carries none (`python3 verifiers/verify_harness_claims.py
    --json` → `omp.catalogue_path` names the one it resolved).
    The catalogue is frozen per session at render time and two variants can
    coexist same-hour, so today's render is evidence, not a spec.
11. **Invocation-shaped triggers for domain-term names.** When the skill's
    name is also a domain term (ufo, omarchy), a bare noun trigger cannot
    separate invocation from reference — measured 2026-09-28: all 5 literal
    `ufo` misses in opencode.db were domain mentions, not calls. Pair the
    noun with slash-form or imperative-context triggers.
12. **Skill files outside a discovery root never route.** omp loads
    `.agent/skills` + `.agents/skills` (project walk-up + user home),
    `.claude/skills`, marketplace cache. A SKILL.md at a bare repo root (the
    six `*-shokunin` files) is never offered — for those, `description` craft
    is audit-hygiene, not routing surface; check the discovery root before
    predicting router behavior.
