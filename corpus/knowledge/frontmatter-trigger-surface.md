# Frontmatter trigger surfaces

Falsifiable claims about `description:` fields, observed 2026-09-28.

## Fact 1 — Three trigger kinds coexist in mature descriptions

- **Literal invocation strings**, quoted: `"/wwkd", "plan this", "break this
  down"` — `~/.agents/skills/wwkd/SKILL.md` frontmatter.
- **Named domain triggers**, quoted: `Triggers: "sekhmet", "swarm", "L3", "fan
  out", "parallel probes", "spark"` — `~/.agents/skills/sekhmet-l3/SKILL.md`.
- **Implicit need phrases** (user describes the goal, never names the tool):
  `"我想做一个XX"`, `"帮我实现XX功能"` — `~/.agents/skills/bailian-model-recommend/SKILL.md`
  frontmatter + 适用场景 section.

## Fact 2 — Anti-triggers live in `description`, not only the body

- omarchy: `Excludes Omarchy source development in ~/.local/share/omarchy/` —
  `~/.agents/skills/omarchy/SKILL.md` frontmatter.
- bailian-gen: `反触发：普通问答、编程、写作、翻译不走本技能` — frontmatter.
- bailian-cli: `不要用于普通问答、编程、写作、翻译、摘要、泛搜索` — frontmatter.
- bailian-train-deploy: `反触发：用户点名火山方舟/ark 的精调不走本 skill` — frontmatter.

Reason (opinion): the router surface is the description; body-level exclusions
cannot prevent activation, only correct it after the fact.

## Fact 3 — Sibling arbitration clauses name the neighbor and the rule

- bailian-model-recommend: `当用户同时涉及模型查询和模型选择时，优先使用本
  skill（本 skill 内部会读取模型数据完成推荐）` — names bailian-docs-llm-wiki
  as the overlapping sibling and states who wins.
- bailian-web-search frontmatter lists five sibling routes with `→` arrows.

## Fact 4 — Always-on skills override the trigger assumption explicitly

- godspeed: `Use on every prompt, including nested and delegated prompts,
  without waiting for a keyword` — `~/.agents/skills/godspeed/SKILL.md`.

## Fact 5 — Runtime deps go in metadata, not prose

- `metadata.requires.bins: ["bl"]` across the bailian family;
  `compatibility: 需要已安装 bailian-docs-llm-wiki skill` on
  bailian-model-recommend; ufo uses `metadata:` keys for axis_family /
  language / substrate.
