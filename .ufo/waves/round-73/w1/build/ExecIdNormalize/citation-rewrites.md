# Citation rewrites — chosen by document, never by arithmetic

Source file: package entry `knowledge/corpus/knowledge/chinese-client-skill-surfaces.md` (45 lines).
Each staged id the entry cites resolves to exactly one lane id: the `source:` lines carry the URL,
the vendor-table rows carry the vendor name, and the two anchors agree for every id (checked below:
no cited staged id had two candidate lane ids). Prose citations with neither URL nor vendor on their
own line are resolved by that id's unique map and marked `context`.

The four Qwen rows (staged S205-S208) are cited **zero times** by this entry — its opening paragraph
explicitly excludes the Qwen surface ("None of them is the Qwen Code surface ...") — so their
`used-by` cannot name this entry; see `gate-notes.md`.

## Map applied

| staged id | lane id | document (URL) | anchor evidence |
|---|---|---|---|
| S205 | S217 | https://qwenlm.github.io/qwen-code-docs/en/users/features/skills | not cited by the entry |
| S206 | S218 | https://qwenlm.github.io/qwen-code-docs/zh/users/features/skills | not cited by the entry |
| S207 | S219 | https://qwenlm.github.io/qwen-code-docs/ja/users/features/skills | not cited by the entry |
| S208 | S220 | https://qwenlm.github.io/qwen-code-docs/zh/blog/updates/weekly-update-2026-02-09 | not cited by the entry |
| S214 | S221 | https://docs.trae.cn/ide_skills | line 4: url+vendor; line 21: vendor |
| S216 | S222 | https://www.codebuddy.ai/docs/zh/ide/Features/Skills | line 5: url; line 22: vendor |
| S217 | S223 | https://www.codebuddy.ai/docs/zh/cli/skills | line 6: url; line 22: vendor; line 34: context |
| S218 | S224 | https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md | line 7: url; line 23: vendor |
| S219 | S225 | https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html | line 8: url; line 23: vendor; line 33: context |
| S221 | S226 | https://docs.bigmodel.cn/cn/managed-agents/skills.md | line 9: url; line 24: vendor |

## Citation sites

| entry line | staged ids | lane ids | anchor | rewritten line |
|---|---|---|---|---|
| 4 | S214 | S221 | url+vendor | source: S221 — https://docs.trae.cn/ide_skills — `# 了解 TRAE 中的技能` → `# 动态按需加载`, `# 技能 vs 规则`, `# 使用 .agents 技能目录` — retrieved 2026-10-23 |
| 5 | S216 | S222 | url | source: S222 — https://www.codebuddy.ai/docs/zh/ide/Features/Skills — `# Skill 的结构`, `# 渐进式披露设计原则` — retrieved 2026-10-23 |
| 6 | S217 | S223 | url | source: S223 — https://www.codebuddy.ai/docs/zh/cli/skills — `# 项目级 Skills`, `# 用户级 Skills` — retrieved 2026-10-23 |
| 7 | S218 | S224 | url | source: S224 — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md — `# Skill discovery`, `# Description resolution` — file read from `main` on 2026-10-23 |
| 8 | S219 | S225 | url | source: S225 — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — `# Frontmatter 字段`, `# Skill 存放位置` — retrieved 2026-10-23 |
| 9 | S221 | S226 | url | source: S226 — https://docs.bigmodel.cn/cn/managed-agents/skills.md — `# 选择内置或自定义 Skill` — retrieved 2026-10-23 |
| 21 | S214 | S221 | vendor | \| ByteDance \| TRAE IDE (S221) \| `.trae/skills/` \| `~/.trae-cn/skills/` (domestic build), `~/.trae/skills/` (international) \| `name`, `description` only; the canonical body shape is 描述 / 使用场景 / 指令 / 示例 \| |
| 22 | S216, S217 | S222, S223 | vendor | \| Tencent \| CodeBuddy IDE + CLI (S222, S223) \| `.codebuddy/skills/` \| `~/.codebuddy/skills/` \| `name`, `description` required; `allowed-tools`, `disable` optional; CLI examples also use `disable-model-invocation` \| |
| 23 | S218, S219 | S224, S225 | vendor | \| Moonshot \| Kimi Code CLI (S224, S225) \| `.kimi-code/skills/`, `.agents/skills/` \| `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` \| `name`, `description`, `type` (`prompt`/`inline`/`flow`), `whenToUse`, `disableModelInvocation`, `arguments` \| |
| 24 | S221 | S226 | vendor | \| Zhipu AI \| managed agents (S226) \| uploaded package \| uploaded package \| `name`, `description` required; `type:zai` / `type:custom` distinguishes platform from user skills \| |
| 33 | S219 | S225 | context (per-id unique map) | `disable_model_invocation` (S225). CodeBuddy's CLI examples emit the hyphenated |
| 34 | S217 | S223 | context (per-id unique map) | `disable-model-invocation` and `allowed-tools` spellings (S223). Against this, wave 1 |

## Rewritten entry (whole file, review copy — this seat does not land it)

```markdown

# Four Chinese-vendor skill surfaces: discovery roots, frontmatter, and trigger surfaces

source: S221 — https://docs.trae.cn/ide_skills — `# 了解 TRAE 中的技能` → `# 动态按需加载`, `# 技能 vs 规则`, `# 使用 .agents 技能目录` — retrieved 2026-10-23
source: S222 — https://www.codebuddy.ai/docs/zh/ide/Features/Skills — `# Skill 的结构`, `# 渐进式披露设计原则` — retrieved 2026-10-23
source: S223 — https://www.codebuddy.ai/docs/zh/cli/skills — `# 项目级 Skills`, `# 用户级 Skills` — retrieved 2026-10-23
source: S224 — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md — `# Skill discovery`, `# Description resolution` — file read from `main` on 2026-10-23
source: S225 — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — `# Frontmatter 字段`, `# Skill 存放位置` — retrieved 2026-10-23
source: S226 — https://docs.bigmodel.cn/cn/managed-agents/skills.md — `# 选择内置或自定义 Skill` — retrieved 2026-10-23
verified-at: 2026-10-23
recheck: 60d — re-fetch all six pages and re-count the discovery roots and the frontmatter field names per vendor, confirming none has silently changed (ran 2026-10-23)
ground: round-1 question Q1 — whether other Chinese or Japanese clients expose an Agent Skills surface. Closed for the Chinese-vendor channel; the Japanese-client channel yielded nothing.

**The answer to Q1.** Four Chinese vendors ship an Agent Skills surface, each with its
own discovery roots and its own frontmatter vocabulary. None of them is the Qwen Code
surface already held from wave 1, and each is a distinct product family, not a re-run of
a held client.

| vendor | product | project roots | user roots | distinctive frontmatter |
|---|---|---|---|---|
| ByteDance | TRAE IDE (S221) | `.trae/skills/` | `~/.trae-cn/skills/` (domestic build), `~/.trae/skills/` (international) | `name`, `description` only; the canonical body shape is 描述 / 使用场景 / 指令 / 示例 |
| Tencent | CodeBuddy IDE + CLI (S222, S223) | `.codebuddy/skills/` | `~/.codebuddy/skills/` | `name`, `description` required; `allowed-tools`, `disable` optional; CLI examples also use `disable-model-invocation` |
| Moonshot | Kimi Code CLI (S224, S225) | `.kimi-code/skills/`, `.agents/skills/` | `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` | `name`, `description`, `type` (`prompt`/`inline`/`flow`), `whenToUse`, `disableModelInvocation`, `arguments` |
| Zhipu AI | managed agents (S226) | uploaded package | uploaded package | `name`, `description` required; `type:zai` / `type:custom` distinguishes platform from user skills |

**Three patterns the four vendors share.** First, all four treat the `description` as the
routing surface, and all four describe the trigger as the model scanning brief
descriptions before loading anything. TRAE says it outright: "智能体不会在任务开始时一次性读取所有技能的完整内容" — the agent scans the brief descriptions first and loads a body only when the task is judged highly relevant. Second, all four separate a project scope from a user scope, and both TRAE and Kimi make the scope a *precedence* rule rather than just a label. Third, all four now read the cross-vendor `.agents/skills/` root — TRAE behind an explicit "启用 .agents 技能目录" toggle and with `.trae/skills/` winning any name collision, Kimi as a first-class group alongside its own vendor root.

**The frontmatter-vocabulary divergence is the practical hazard.** Kimi accepts three
spellings of the same field — `whenToUse`, `when-to-use`, `when_to_use` — and the same
tolerance for `disableModelInvocation` / `disable-model-invocation` /
`disable_model_invocation` (S225). CodeBuddy's CLI examples emit the hyphenated
`disable-model-invocation` and `allowed-tools` spellings (S223). Against this, wave 1
established that Qwen Code reads `allowedTools` and **ignores** `allowed-tools`. So a
skill authored on CodeBuddy or Claude Code and installed into Qwen Code does not fail
loudly: it loads, and its tool allowlist is silently dropped. This is the clearest
cross-client compatibility trap the lane now holds, and it is only visible when the
Chinese-vendor surfaces are read side by side.

**What is still missing.** No Japanese-*client* skill surface was found in this round.
The Japanese side of the corpus is a documentation and practice tier (see
`japanese-prompt-craft-tiers.md`), not a client tier. That is a finding, not an omission.

---
```

