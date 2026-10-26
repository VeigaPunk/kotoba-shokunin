source: S217 — TRAE Docs 技能（Skill） — https://docs.trae.cn/ide_skills — located quote "若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 `.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` 目录中的技能。" — retrieved 2026-10-25
source: S218 — CodeBuddy Docs Skills（IDE） — https://www.codebuddy.ai/docs/zh/ide/Features/Skills — located quote "元数据 (YAML Frontmatter):name 和 description 决定了 AI 何时会使用这个 Skill。描述需具体说明 Skill 的功能和使用场景。" — retrieved 2026-10-25
source: S219 — CodeBuddy Code Skills（CLI） — https://www.codebuddy.ai/docs/zh/cli/skills — located quote "1. **项目级 Skills**：`.codebuddy/skills/`（项目根目录下） 2. **用户级 Skills**：`~/.codebuddy/skills/`（用户主目录下）" — retrieved 2026-10-25
source: S220 — Kimi Code CLI Agent Skills (English) — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md — located quote "when a skill name is defined in more than one scope, the more specific scope wins" — file read from main 2026-10-25
source: S221 — Kimi Code 文档 Agent Skills — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — located quote "模型也可以根据 description 和 whenToUse 自动调用 Skill。disableModelInvocation 设为 true 或 type 设为 flow 时不自动调用。Skill 调用最多允许嵌套 3 层，超过后会被终止。" — retrieved 2026-10-25
source: S222 — 智谱 AI 开放文档 Agent Skills — https://docs.bigmodel.cn/cn/managed-agents/skills.md — located quote "Skill 将领域工作流程、模板和脚本打包给云端 Agent。Agent 先读名称与描述，再按任务读取正文和配套资料，不必每次把整套方法塞进 system prompt。" — retrieved 2026-10-25
verified-at: 2026-10-25
recheck: 60d — re-fetch all six pages and re-count each vendor's discovery roots and frontmatter keys, confirming none has silently changed (ran 2026-10-25)
ground: round-73 Q1 — which Chinese-vendor clients expose an Agent Skills surface

# Four Chinese-vendor skill surfaces: discovery roots, frontmatter vocabulary, placement

All six pages were re-opened this round. The vendor table carries one row per
vendor; the tokens in a row are the placement paths and frontmatter keys that
row's cited page states.

| vendor | source ids | placement tokens | frontmatter keys | note |
|---|---|---|---|---|
| TRAE | S217 | `.trae/skills/`, `~/.trae-cn/skills`, `.agents/skills/`, `~/.trae/skills/` | `name`, `description` | rules always load, skills on demand; `.trae/skills/` wins on names |
| CodeBuddy | S218, S219 | `.codebuddy/skills/`, `~/.codebuddy/skills/` | `name`, `description`, `allowed-tools` | IDE + CLI share the hyphenated spelling |
| Kimi Code | S220, S221 | `.kimi-code/skills/`, `.agents/skills/` | `name`, `description`, `whenToUse` | project over user over extra over built-in |
| Zhipu | S222 | `/workspace/skills/` | `name`, `description`, `type:zai` | uploaded package, read on demand, never injected |

**The practical hazard is the placement split, not the file format.** TRAE,
CodeBuddy and Kimi Code all read a skill body from a directory and name it from
`description`; Zhipu uploads a package and reads `/workspace/skills/` on demand
instead of injecting the body. A skill copied between them keeps its frontmatter
and loses the placement or the key spelling the target client reads.

**Two live divergences the six pages carry.** TRAE's international user root does
not appear in the page text fetched this round (only the domestic
`~/.trae-cn/skills`); Kimi's English page names `.kimi/skills/` while the Chinese
page names `.kimi-code/skills/`. Both are recorded as observations, not fixed
values: the census decides which vendors the live pages back.

## Gate

- all six pages re-fetched 2026-10-25; quotes above are copied from the
  committed snapshots under `.ufo/waves/round-73/snapshots/`
- one row per vendor; no vendor is backed by a token its cited page lacks
