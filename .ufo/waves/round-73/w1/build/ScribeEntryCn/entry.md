source: S<<TRAE>> — TRAE 文档（字节跳动）— 技能（Skill） — https://docs.trae.cn/ide_skills — § 技能所在目录 — located quote "项目技能：项目所在路径下的 `.trae/skills/` 目录。 全局技能： macOS/Linux：本地根目录 `~/.trae-cn/skills`。" (snapshot `cn-trae-skills.md:193-195`)
source: S<<CB-IDE>> — 腾讯云代码助手 CodeBuddy — Skills（IDE 页） — https://www.codebuddy.ai/docs/zh/ide/Features/Skills — § Skill 的结构 — located quote "每个 Skill 由一个必需的 `SKILL.md` 文件和可选的打包资源组成。Skill 应建立在工作区的 `.codebuddy/skills/` 目录下。" (snapshot `cn-codebuddy-ide-skills.md:157`)
source: S<<CB-CLI>> — CodeBuddy CLI — Skills（CLI 页） — https://www.codebuddy.ai/docs/zh/cli/skills — § 目录结构 — located quote "Skills 通过在特定目录中创建 `SKILL.md` 文件来定义： 项目级 Skills：`.codebuddy/skills/`（项目根目录下） 用户级 Skills：`~/.codebuddy/skills/`（用户主目录下）" (snapshot `cn-codebuddy-cli-skills.md:921-925`)
source: S<<KIMI-ZH>> — Kimi Code CLI — 技能（Skill） — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html — § Skill 存放位置 — located quote "按作用域分四档扫描，越具体的作用域优先级越高：Project > User > Extra > Built-in。 用户级（对所有项目生效）： `$KIMI_CODE_HOME/skills/`（默认：`~/.kimi-code/skills/`） `~/.agents/skills/`" (snapshot `cn-kimi-zh-skills.md:273-281`)
source: S<<KIMI-EN>> — moonshotai/kimi-cli — docs/en/customization/skills.md — https://github.com/moonshotai/kimi-cli/blob/main/docs/en/customization/skills.md (the raw path `raw.githubusercontent.com/moonshotai/kimi-cli/main/docs/en/customization/skills.md` serves the same bytes) — `## Skill discovery`, user-level roots — located quote "**Brand group** (mutually exclusive): 1. `~/.kimi/skills/` 2. `~/.claude/skills/` 3. `~/.codex/skills/`" (snapshot `cn-kimi-en-skills.md:34-37`)
source: S<<ZHIPU>> — 智谱 BigModel — Agent Skills（managed agents） — https://docs.bigmodel.cn/cn/managed-agents/skills.md — § 挂载到 Agent — located quote "Skill 非空时必须同时声明 agent\_toolset\_20260601；Agent 使用的 Skill 最多 20 个，目录不得重复。运行目录为 `/workspace/skills/<目录名>/`，按需读取。" (snapshot `cn-zhipu-skills.md:83`)
verified-at: 2026-10-25
recheck: 30d — `for p in 'https://docs.trae.cn/ide_skills|.trae/skills/' 'https://www.codebuddy.ai/docs/zh/ide/Features/Skills|.codebuddy/skills/' 'https://www.codebuddy.ai/docs/zh/cli/skills|~/.codebuddy/skills/' 'https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html|.kimi-code/skills/' 'https://raw.githubusercontent.com/moonshotai/kimi-cli/main/docs/en/customization/skills.md|.kimi/skills/' 'https://docs.bigmodel.cn/cn/managed-agents/skills.md|/workspace/skills/'; do u=${p%%|*}; q=${p#*|}; printf '%s ' $(curl -fsSL -A Mozilla/5.0 --max-time 60 $u | grep -c -F -- $q); done` — prints `3 2 3 2 2 1` on 2026-10-25 (the TRAE URL answers 400 without a browser user agent); any 0 means the page moved or the fetch failed, which is a re-open, never a silent edit
ground: the lane's surface maps hold where a client reads a skill, an agent definition, a command file, a hook file or a scoped rule, plus the collision and trust rules for the pinned clients — but no Chinese-vendor skill surface at base `072048f`: `grep -rniE 'trae|codebuddy|kimi code|kimi-code|zhipu|bigmodel|moonshot' corpus SKILL.md PROVINCE.md` printed one line, `corpus/knowledge/opencode-offer-trace-round8.md:84`, a local config path rather than a surface row. Round-73 claim C1 (coverage, 8.5) supplies this entry; none of the four vendors is one of the lane's pinned seven.

# Four Chinese-vendor skill surfaces — where the body goes and what the frontmatter is called

Four vendors ship an Agent Skills surface that this lane's maps did not hold: TRAE (ByteDance), CodeBuddy
(Tencent), Kimi Code (Moonshot), Zhipu managed agents (智谱). Six pages were opened on 2026-10-25 — two of
them are one vendor's own two surfaces and do not agree with each other, which is this entry's sharpest
finding. Documentary evidence only (tier B, vendor documentation): no client was installed, loaded, routed or
refused here, and the word precedence below always means that a page states an order, never that a client was
observed to apply one.

## The per-vendor map

| vendor | project roots | user roots or placement | frontmatter keys | the page the row rests on |
|---|---|---|---|---|
| TRAE IDE (ByteDance) | `.trae/skills/` | `~/.trae-cn/skills` (macOS/Linux), `%userprofile%/.trae-cn/skills` (Windows) — the page prints no trailing slash | `name`, `description` only; the page's own body shape is 描述 / 使用场景 / 指令 / 示例 | S<<TRAE>> § 技能所在目录, § SKILL.md 文件格式 |
| CodeBuddy IDE + CLI (Tencent) | `.codebuddy/skills/` | `~/.codebuddy/skills/` — CLI page only; the IDE page documents no user root | `name`, `description`, `allowed-tools`, `disable-model-invocation`, `user-invocable` (CLI frontmatter table; the IDE page's example adds `disable`) | S<<CB-IDE>> § Skill 的结构; S<<CB-CLI>> § 目录结构, § Frontmatter 字段 |
| Kimi Code CLI (Moonshot) | `.kimi-code/skills/`, `.agents/skills/` | `$KIMI_CODE_HOME/skills/` (default `~/.kimi-code/skills/`), `~/.agents/skills/` | `name`, `description`, `type`, `whenToUse`, `disableModelInvocation`, `arguments` — `whenToUse` and `disableModelInvocation` take three spellings each | S<<KIMI-ZH>> § Skill 存放位置, § Frontmatter 字段 |
| Zhipu managed agents (智谱) | none documented — the page never names a project scope | uploaded package, mounted per agent; the runtime directory is `/workspace/skills/<目录名>/` | `name`, `description` (non-empty), and the page names no third key | S<<ZHIPU>> § 选择内置或自定义 Skill, § 挂载到 Agent |

Two rows carry a shape the other two do not. **Kimi** also accepts a flat `.md` file as a skill —
"扁平形式的 `name` 可省略，省略时取文件名去掉 `.md` 扩展名" (`cn-kimi-zh-skills.md:204`) — and its directory form is strict: "目录型 `SKILL.md` 中 `name` 和 `description` 必须显式填写，省略任意一项均会导致解析失败。" (`:255`). **Zhipu** has no directory at all: a skill is an uploaded package of one top-level directory, mounted to an agent by `type` and pinned by version, so its roots column is a placement on the platform, not a path in a repository.

## The three patterns the pages share — and two the staged draft overstated

1. **The name-and-description pair is the whole routing surface; the body waits for a decision.** All four pages state it in their own words. TRAE: "智能体不会在任务开始时一次性读取所有技能的完整内容。" (`cn-trae-skills.md:108`). CodeBuddy gives it as a three-level table: "元数据 (Metadata)：始终在上下文中 (~100 词)。 Skill 主体 (SKILL.md body)：当 Skill 被触发时加载 (<5k 词)。 打包资源 (Bundled resources)：按需由 AI 加载 (无限制)。" (`cn-codebuddy-ide-skills.md:218-220`). Kimi injects at startup — "it discovers all skills and injects their names, paths, and descriptions into the system prompt" (`cn-kimi-en-skills.md:7`) — and its zh page says the model picks on the same two fields: "模型也可以根据 `description` 和 `whenToUse` 自动调用 Skill。" (`cn-kimi-zh-skills.md:303`). Zhipu: "Agent 先读名称与描述，再按任务读取正文和配套资料" (`cn-zhipu-skills.md:7`). Four of four.
2. **A project scope outranks a user scope — but only two of the four publish that order.** CodeBuddy publishes it plainly: "Skill 来源：项目级 Skills 优先于用户级 Skills" (`cn-codebuddy-cli-skills.md:1398`), repeated in its FAQ at `:1553`. Kimi publishes a four-rung ladder: "按作用域分四档扫描，越具体的作用域优先级越高：Project > User > Extra > Built-in。" (`cn-kimi-zh-skills.md:273`). TRAE names both scopes (项目技能 / 全局技能) and publishes only a root collision rule instead: "若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 `.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` 目录中的技能。" (`cn-trae-skills.md:375`). Zhipu publishes neither scope. The staged draft's sentence — that all four separate a project scope from a user scope — is therefore not what these pages say: two scope orders, one root order, one no scope.
3. **The cross-vendor `.agents/skills/` root is read by two of the four, not all four.** TRAE reads it behind an explicit switch — "在 导入设置 部分，打开 启用 .agents 技能目录 开关。" (`cn-trae-skills.md:389`) — and lets its own root win a collision (quote above). Kimi reads it at both scopes: `~/.agents/skills/` and `.agents/skills/` (`cn-kimi-zh-skills.md:277-285`). CodeBuddy's two pages never name it and Zhipu's page never does — 0 hits on each, counts in Limits. A skill distributed only through `.agents/skills/` is therefore not portable across these four on their own evidence.

The other half of pattern 3 is the part that changes authoring practice: TRAE treats `.agents/skills/` as an imported namespace that its own directory outranks, while Kimi treats it as a first-class root alongside its own — so the same shared body has different standing in the two clients that read it.

## The frontmatter-spelling hazard

**Same vendor, two pages, two vocabularies (Kimi).** The zh page documents `type`, `whenToUse`, `disableModelInvocation` and `arguments`, and says outright that the last two take three spellings each: "`disableModelInvocation` | 设为 true 禁止模型自动调用，也接受 `disable-model-invocation`、`disable_model_invocation` 写法" (`cn-kimi-zh-skills.md:249`). The GitHub page's frontmatter table lists `name`, `description`, `license`, `compatibility`, `metadata` — `whenToUse` and `disableModelInvocation` do not occur on it at all (0 hits). The pages also disagree on the roots: `.kimi-code/skills/` occurs twice on the zh page and zero times on the GitHub page, `.kimi/skills/` twice on the GitHub page and zero times on the zh page. A body written to one page is placed or keyed wrong on the other reading, and no page of the vendor reconciles them. On this host on 2026-10-25 the zh page's roots are the ones that exist: `ls -d ~/.kimi-code/skills ~/.agents/skills ~/.kimi/skills ~/.config/agents/skills` prints the first two and errors on the last two. That is evidence about one host on one day, not a discovery rule, and no client's discovery was observed.

**Same vendor, two surfaces, a contradiction about required fields (CodeBuddy).** The IDE page presents the two keys as required matter — "每个 Skill 由一个必需的 `SKILL.md` 文件和可选的打包资源组成" and "`name` 和 `description` 决定了 AI 何时会使用这个 Skill。" (`cn-codebuddy-ide-skills.md:157,174`). The CLI page's table marks both as optional: "| `name` | 否 | Skill 名称，未指定时使用目录名" (`cn-codebuddy-cli-skills.md:969`). The CLI page's table is the lenient reading — a missing `name` falls back to the directory name — while Kimi's zh page makes omission of either key a parse failure, so required-ness is not a property of the format but of the page: an author moving a body between these vendors cannot carry it along.

**Across vendors, one intent and three spellings, with one documented tolerance.** CodeBuddy writes the allowlist and the invocation switch hyphenated (`allowed-tools`, `disable-model-invocation`); Kimi writes the switch camelCase and documents the hyphenated form as accepted; TRAE documents no allowlist key at all (0 hits) and Zhipu documents none. So among these four the tool allowlist is a CodeBuddy-only key: a body carrying one loses it on the other three as far as their pages say, and the only spelling tolerance any page grants is Kimi's own alias list. Two rules follow: keep the allowlist in the vendor whose page you load the body into, and never assume a camelCase and a hyphenated pair are interchangeable — no page here says it reads the other's spelling.

**Zhipu's `type` is not a SKILL.md key.** The page separates the two levels: the frontmatter is "SKILL.md frontmatter 写 name 和非空 description" (`cn-zhipu-skills.md:37`), while `type:zai` and `type:custom` are the catalog kinds ("**自定义**：type:custom，上传你的 SKILL.md 和所需模板/脚本。", `:28`) and the mount table's field ("| type | zai 或 custom |", `:79`). Putting `type:` into a Zhipu body's frontmatter is reading an API field as a document key.

## What a skill author does with this

- **Write the description for the scanning step, not the body.** Four pages agree the model sees names and descriptions first; the description is the only text competing for the load (pattern 1).
- **Keep the body portable by keeping it keyless.** Only `name` and `description` are documented by all four; every other key in the table is vendor-specific, and the two vendors that document a strictness disagree with their own sibling pages.
- **Pick the placement from the page you target, then open the vendor's other page.** Kimi's two pages disagree on both the root and the vocabulary; assuming the newer-sounding root is the live one is inference, not a quote.
- **Do not rely on `.agents/skills/` for these four.** Two read it; one of the two outranks it with its own root.

## Limits

- Documentary evidence only: six pages read 2026-10-25, four vendors, not a census — a Chinese vendor silent here is not a vendor without a skill surface. No client was installed or run; no load, route, refusal, precedence decision or parse failure was observed.
- **No page states a version of the skill format.** The bytes this entry rests on are pinned by the snapshot sha256s (`snapshots/MANIFEST.sha256`), and the Kimi GitHub page is a `main`-branch file: it can change without the URL changing, which is why the recheck line compares counts instead of trusting the URL.
- **Two CodeBuddy surfaces were read (IDE, CLI).** WorkBuddy and the enterprise surface appear only as navigation links on the pages fetched; nothing about them is claimed.
- **Sibling boundary:** kumitate (kumitate `corpus/knowledge/kimi-skills-plugins.md`) owns the host's Kimi skills-and-plugins plane — its read of `~/.kimi-code/skills/` on disk, 2026-10-13. This entry records vendor pages, plus the one host existence check in the hazard section; it adopts none of kumitate's observations, and that check is not a claim about discovery.
- **TRAE's international root is dropped, not refuted.** The staged draft carried `~/.trae/skills/`; the page fetched has 0 occurrences of that string and one of `~/.trae-cn/skills`, so the row states only the root the bytes carry. A separate international build may exist; no page read here says so.
- **The Kimi contradiction is recorded, not resolved.** The zh page's `$KIMI_CODE_HOME/skills/`, the GitHub page's `~/.config/agents/skills/` (recommended there) and `merge_all_available_skills` (GitHub page only) hint at two discovery generations; that reading is inference, and no page says which is current.
- **Zhipu's runtime directory is the server's**, stated by the page for a mounted skill; nothing about a local client's behaviour follows from it.
- **The Qwen Code tool-allowlist trap is not carried here.** The staged parent entry pairs CodeBuddy's `allowed-tools` with Qwen Code's `allowedTools`; this entry cites only the four vendors whose hosts the claim froze, so adopting a fifth id would move that set. Flagged to the L1; the CodeBuddy-vs-Kimi half above is the part backed by the cited pages.
- **Code spans inside quotes are the snapshots' own text**: the HTML pages were text-extracted with `<code>` rendered as backticks and whitespace runs collapsed, so every quote above is quote-equal to the snapshot under that documented shaping, not byte-equal to the served HTML.
- Counts and sweeps: `grep -c -F '<token>' <snapshot>` in `.ufo/waves/round-73/snapshots/`, files in the order TRAE, CodeBuddy IDE, CodeBuddy CLI, Kimi zh, Kimi EN, Zhipu:

```
$ for t in '.agents/skills/' 'allowed-tools' 'whenToUse' 'disableModelInvocation' 'license' '项目'; do \
    printf '%-24s' $t; for f in cn-trae-skills.md cn-codebuddy-ide-skills.md cn-codebuddy-cli-skills.md \
    cn-kimi-zh-skills.md cn-kimi-en-skills.md cn-zhipu-skills.md; do printf ' %3s' $(grep -c -F -- $t $f); done; echo; done
.agents/skills/            9   0   0   3   2   0
allowed-tools              0   1  14   0   0   0
whenToUse                  0   0   0   4   0   0
disableModelInvocation     0   0   0   3   0   0
license                    0   0   0   0   1   0
项目                       16   1  19   7   0   0
```

  The roots that decide the contradiction: `grep -c -F '.kimi-code/skills/' cn-kimi-zh-skills.md cn-kimi-en-skills.md` → `2 0`; the same with `.kimi/skills/` → `0 2`; `grep -c -F '~/.trae/skills' cn-trae-skills.md` → `0`.

## Scope

Prompt-and-skill craft: where a skill body must sit for one of four Chinese-vendor clients to read it, and what that client's page calls the frontmatter. Not: a client's runtime behaviour (none observed), a trust gate for an untrusted body (`corpus/knowledge/client-trust-gates-round68.md`), a name-collision rule for the held clients (`corpus/knowledge/skill-name-precedence-round69.md`), or any market or translation commentary — PROVINCE's Core admits the surfaces and the frontmatter vocabulary, not the vendor comparison itself. The CodeBuddy CLI page also states that frontmatter hooks from non-built-in sources are not registered by default (`cn-codebuddy-cli-skills.md:1229`); that is round 68's ground and is not claimed here.

## Related

- `corpus/knowledge/skill-name-precedence-round69.md` — the same-name rules for five clients; TRAE's `.trae/skills/` over `.agents/skills/` is a sixth, root-level instance of the same question.
- `corpus/knowledge/client-trust-gates-round68.md` — what a client does with a body it did not place; this entry stops at placement.
- `corpus/knowledge/instruction-surface-census-round13.md` — the client surface census these four are absent from.
