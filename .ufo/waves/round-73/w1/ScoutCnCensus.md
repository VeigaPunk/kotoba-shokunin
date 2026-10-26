# ScoutCnCensus — Q45 census for C1 (round 73, wave 1)

**Verdict: the live pages can back 4 of 4 vendors to the plan's rule (≥3 tokens: ≥1 root/placement + ≥2 keys). The target `N == 4` stands; no lowering.** But the margin is thin for two vendors and the staged entry carries tokens/claims the live bytes do not hold (see "Entry defects"). Access date 2026-10-25 (`date -I`); all seven fetches HTTP 200, `curl -sL --max-time 60 -A 'Mozilla/5.0'`.

## Per-page table

| page (label) | URL | HTTP | bytes (raw) | server-rendered? | own heading present (`grep -c -F`) |
|---|---|---|---|---|---|
| TRAE `trae` | https://docs.trae.cn/ide_skills | 200 | 112,442 | yes, text 13,370 B after tag-strip | `了解 TRAE 中的技能` 2, `动态按需加载` 1, `技能 vs 规则` 1, `使用 .agents 技能目录` 2 |
| CodeBuddy IDE `cbide` | https://www.codebuddy.ai/docs/zh/ide/Features/Skills | 200 | 36,633 | yes, text 4,926 B | `Skill 的结构` 1, `渐进式披露设计原则` 1 |
| CodeBuddy CLI `cbcli` | https://www.codebuddy.ai/docs/zh/cli/skills | 200 | 217,520 | yes, text 28,983 B | `项目级 Skills` 3 (html)/5 (txt), `用户级 Skills` 3 |
| Kimi GH raw `kimiraw` | https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md | 200 | 13,528 | plain markdown | `Skill discovery` 1, `Description resolution` 1 |
| Kimi GH blob `kimiblob` | https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md | 200 | 318,606 (318,615 on rerun: page not byte-stable) | yes (body in html, text 17,530 B) | same two headings 1 each |
| Kimi Code `kimicom` | https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html | 200 | 79,788 | yes, text 8,370 B | `Frontmatter 字段` 1, `Skill 存放位置` 1 |
| Zhipu `zhipu` | https://docs.bigmodel.cn/cn/managed-agents/skills.md | 200 | 7,381 | plain markdown | `选择内置或自定义 Skill` 1 |

No page is a JS shell (every heading found in the fetched bytes with no browser). Raw-html sha256: trae 7332587c…, cbide 35114e39…, cbcli ee9e3b71…, kimiraw 5a18c338…, kimiblob 4fdb8fe0…, kimicom e3b314dc…, zhipu b20e45c7…. Text-extracted snapshots (stripped scripts/styles; `ext.py`) are in `build/ScoutCnCensus/snap/*.txt` (94,088 B total) with sha256 `cbcli 6f688e84…, cbide 131415d3…, kimiblob 331f1749…, kimicom fb4a3c44…, kimiraw 5a18c338…, trae 879f09c9…, zhipu b20e45c7…`.

## Token counts (`grep -c -F -- TOKEN page.txt`, lines containing the token)

| vendor | token (kind) | counts |
|---|---|---|
| TRAE | `.trae/skills/` (root) | trae 3 |
| TRAE | `~/.trae-cn/skills/` (root) | **0** with trailing slash; `~/.trae-cn/skills` (no slash) 1 (`:249` "macOS/Linux：本地根目录 ~/.trae-cn/skills。") |
| TRAE | `~/.trae/skills/` (root, "international") | **0** (also 0 without slash) |
| TRAE | `.agents/skills/` | 9 |
| TRAE | `name` / `description` (keys) | 4 / 1 (`:264-265` frontmatter example `name: 技能名称`, `description: 简要描述…`) |
| CodeBuddy | `.codebuddy/skills/` | cbide 2, cbcli 10 |
| CodeBuddy | `~/.codebuddy/skills/` | cbide 0, cbcli 3 |
| CodeBuddy | `allowed-tools` | cbide 1, cbcli 14 |
| CodeBuddy | `disable` | cbide 1 (`:295 disable: false # 可选，是否禁用`), cbcli 2 |
| CodeBuddy | `disable-model-invocation` | cbide 0, cbcli 1 (`:1839`, a field table row, "设置为 true 时，Skill 不会出现在 Skill 工具中") |
| CodeBuddy | `name` / `description` | cbide 4/4, cbcli 17/15 |
| Kimi Code | `.kimi-code/skills/` | kimiraw 0, kimiblob 0, **kimicom 3** |
| Kimi Code | `$KIMI_CODE_HOME/skills/` / `~/.kimi-code/skills/` | 0 / 0 on both GitHub forms; **kimicom 2 / 2** |
| Kimi Code | `.agents/skills/` / `~/.agents/skills/` | kimiraw 2 / 1, kimiblob 2 / 1, kimicom 3 / 2 |
| Kimi Code | `whenToUse`, `disableModelInvocation`, `arguments` | 0 / 0 / 0 on GitHub forms; **kimicom 4 / 3 / 5** |
| Kimi Code | `when-to-use`, `when_to_use`, `disable-model-invocation`, `disable_model_invocation` | kimicom 1 each; GitHub 0 |
| Kimi Code | `type` / `name` / `description` | kimiraw 8/22/12, kimicom 4/9/5 |
| Zhipu | `type:zai` / `type:custom` | zhipu 1 / 1 (`:27-28`, unbackticked in the page, unspaced; `type: zai` 0) |
| Zhipu | `name` / `description` | zhipu 7 / 1 (`:37` "SKILL.md frontmatter 写 name 和非空 description"; word-bounded `name` 3) |
| Zhipu | placement `/v1/skills` (not in the staged table) | zhipu 8 word-bounded; `GET /v1/skills?source=zai` `:27`; `POST /v1/skills` upload |

## Vendors the live pages back (rule: ≥1 root/placement + ≥2 keys, word-bounded)

| vendor | pages that carry it | root/placement tokens present | keys present | backed? |
|---|---|---|---|---|
| TRAE | trae | `.trae/skills/`, `~/.trae-cn/skills` (slash-less), `.agents/skills/` | `name`, `description` | **yes** (exactly 2 keys) |
| CodeBuddy | cbide + cbcli | `.codebuddy/skills/`, `~/.codebuddy/skills/` (cbcli only) | `name`, `description`, `allowed-tools`, `disable` (cbide), `disable-model-invocation` (cbcli) | **yes** |
| Kimi Code | **kimicom only** | `.kimi-code/skills/`, `$KIMI_CODE_HOME/skills/`, `~/.kimi-code/skills/`, `.agents/skills/`, `~/.agents/skills/` | `whenToUse`, `disableModelInvocation`, `arguments`, `type`, `name`, `description` | **yes, via S219 only** |
| Zhipu | zhipu | **none in the staged table** ("uploaded package" is not a token); present on page: `/v1/skills`, `GET /v1/skills?source=zai`, `SKILL.md` | `type:zai`, `type:custom`, `name`, `description` | **yes only if the entry adds a placement token** such as `/v1/skills` |

**Count: 4 of 4 reachable.** Margin: Zhipu needs the entry row to carry a backticked placement token the staged row lacks; TRAE has exactly two keys and the slash-less user root. Counter note: a word-bounded matcher that requires the trailing `/` of `~/.trae-cn/skills/` scores 0 on that token.

## Entry defects against the live bytes (fix in the lane's entry, before the counter reads it)

1. `~/.trae/skills/` "(international)" — **absent** from the live TRAE page (0 hits, any form). The only user root is `~/.trae-cn/skills` (`:249`, Windows `%userprofile%/.trae-cn/skills` `:251`). Drop it or cite another source.
2. `~/.trae-cn/skills/` with trailing slash is 0; page writes it without.
3. Kimi attribution is split: S218 (GitHub `docs/en/customization/skills.md`) documents a **different layout** — `~/.kimi/skills/`, `~/.claude/skills/`, `~/.config/agents/skills/`, `.kimi/skills/`, `.claude/skills/` (`kimiraw:35-40,62-65`) — with no `.kimi-code`, `whenToUse`, `disableModelInvocation`, `arguments`. Every Kimi Code token backs only from S219 (`kimi.com`). A row citing S218 for those tokens would fail (d)/(a) per-source; the table's "(S218, S219)" cell must not claim S218 holds them. S218 and S219 also describe two different roots sets (old `.kimi/skills/` vs `.kimi-code/skills/`): worth one line in the entry.
4. Prose "all four now read the cross-vendor `.agents/skills/` root": `grep -c -F '.agents'` is **0** on cbide, cbcli and zhipu. Only TRAE (9) and Kimi (kimicom 3) hold it. Unbacked for CodeBuddy and Zhipu.
5. "all four separate a project scope from a user scope": Zhipu page has no scope split (upload/mount by API); the staged table itself says "uploaded package". Unbacked for Zhipu.
6. CodeBuddy `disable-model-invocation`: lives only on cbcli (1), not cbide (0); `disable` only on cbide frontmatter example, plus cbcli 2 hits (not checked for frontmatter context).
7. kimi blob bytes differ between two fetches (318,606 vs 318,615): snapshot kimiraw (13.5 KB, stable sha 5a18c338… both times) rather than the blob html; registry URL for (b) must still be the `github.com/moonshotai/kimi-cli` blob form.
8. Zhipu `type:zai`/`type:custom` exist as plain text on the page (`:27-28`), not backticked; they are API values `source.type`, not SKILL.md frontmatter (the page says frontmatter is `name` + non-empty `description`, `:37`). The entry's "distinctive frontmatter" label for them is loose.

Freshness: entry's retrieval date 2026-10-23; the headings and the TRAE quote at `trae.txt:123` (`智能体不会在任务开始时一次性读取所有技能的完整内容`) are still present 2026-10-25.

## Census command
`build/ScoutCnCensus/census-cn.sh [workdir]` (needs `ext.py` beside it; fetches the 7 URLs in parallel, tag-strips, prints sha256 and per-token `grep -c -F` counts). Ran in ~2 s; output matches the table. Core of it:
`curl -sL --max-time 60 -A 'Mozilla/5.0' -o P.html URL; python3 ext.py P.html > P.txt; grep -c -F -- 'TOKEN' P.txt`.

## Unobserved
Not run: any lane gate, the counter (not yet built), the S### id renumbering. CodeBuddy `disable-model-invocation` as frontmatter vs a settings field (cbcli:1839 is a field-table row, observed). Did not test whether kimi.com serves the same bytes to a different user agent. Installed tools: none.
