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
