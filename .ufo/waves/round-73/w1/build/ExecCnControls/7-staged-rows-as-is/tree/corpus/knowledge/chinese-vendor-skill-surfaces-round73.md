
# Four Chinese-vendor skill surfaces: discovery roots, frontmatter, and trigger surfaces

source: S214 — https://docs.trae.cn/ide_skills — `# 了解 TRAE 中的技能` → `# 动态按需加载`, `# 技能 vs 规则`, `# 使用 .agents 技能目录` — retrieved 2026-10-23
source: S216 — https://www.codebuddy.ai/docs/zh/ide/Features/Skills — `# Skill 的结构`, `# 渐进式披露设计原则` — retrieved 2026-10-23
source: S217 — https://www.codebuddy.ai/docs/zh/cli/skills — `# 项目级 Skills`, `# 用户级 Skills` — retrieved 2026-10-23
source: S218 — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md — `# Skill discovery`, `# Description resolution` — file read from `main` on 2026-10-23
source: S219 — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — `# Frontmatter 字段`, `# Skill 存放位置` — retrieved 2026-10-23
source: S221 — https://docs.bigmodel.cn/cn/managed-agents/skills.md — `# 选择内置或自定义 Skill` — retrieved 2026-10-23
verified-at: 2026-10-23
recheck: 60d — re-fetch all six pages and re-count the discovery roots and the frontmatter field names per vendor, confirming none has silently changed (ran 2026-10-23)
ground: round-1 question Q1 — whether other Chinese or Japanese clients expose an Agent Skills surface. Closed for the Chinese-vendor channel; the Japanese-client channel yielded nothing.

**The answer to Q1.** Four Chinese vendors ship an Agent Skills surface, each with its
own discovery roots and its own frontmatter vocabulary. None of them is the Qwen Code
surface already held from wave 1, and each is a distinct product family, not a re-run of
a held client.

| vendor | product | project roots | user roots | distinctive frontmatter |
|---|---|---|---|---|
| ByteDance | TRAE IDE (S214) | `.trae/skills/` | `~/.trae-cn/skills/` (domestic build), `~/.trae/skills/` (international) | `name`, `description` only; the canonical body shape is 描述 / 使用场景 / 指令 / 示例 |
| Tencent | CodeBuddy IDE + CLI (S216, S217) | `.codebuddy/skills/` | `~/.codebuddy/skills/` | `name`, `description` required; `allowed-tools`, `disable` optional; CLI examples also use `disable-model-invocation` |
| Moonshot | Kimi Code CLI (S218, S219) | `.kimi-code/skills/`, `.agents/skills/` | `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` | `name`, `description`, `type` (`prompt`/`inline`/`flow`), `whenToUse`, `disableModelInvocation`, `arguments` |
| Zhipu AI | managed agents (S221) | uploaded package | uploaded package | `name`, `description` required; `type:zai` / `type:custom` distinguishes platform from user skills |

**Three patterns the four vendors share.** First, all four treat the `description` as the
routing surface, and all four describe the trigger as the model scanning brief
descriptions before loading anything. TRAE says it outright: "智能体不会在任务开始时一次性读取所有技能的完整内容" — the agent scans the brief descriptions first and loads a body only when the task is judged highly relevant. Second, all four separate a project scope from a user scope, and both TRAE and Kimi make the scope a *precedence* rule rather than just a label. Third, all four now read the cross-vendor `.agents/skills/` root — TRAE behind an explicit "启用 .agents 技能目录" toggle and with `.trae/skills/` winning any name collision, Kimi as a first-class group alongside its own vendor root.

**The frontmatter-vocabulary divergence is the practical hazard.** Kimi accepts three
spellings of the same field — `whenToUse`, `when-to-use`, `when_to_use` — and the same
tolerance for `disableModelInvocation` / `disable-model-invocation` /
`disable_model_invocation` (S219). CodeBuddy's CLI examples emit the hyphenated
`disable-model-invocation` and `allowed-tools` spellings (S217). Against this, wave 1
established that Qwen Code reads `allowedTools` and **ignores** `allowed-tools`. So a
skill authored on CodeBuddy or Claude Code and installed into Qwen Code does not fail
loudly: it loads, and its tool allowlist is silently dropped. This is the clearest
cross-client compatibility trap the lane now holds, and it is only visible when the
Chinese-vendor surfaces are read side by side.

**What is still missing.** No Japanese-*client* skill surface was found in this round.
The Japanese side of the corpus is a documentation and practice tier (see
`japanese-prompt-craft-tiers.md`), not a client tier. That is a finding, not an omission.

---
