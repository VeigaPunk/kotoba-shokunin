# ReviewerDivergence — Primary-Page Verification of Cross-Client Frontmatter-Spelling Claims (Round 73 Wave 1)

## Verdict Summary

**OVERALL VERDICT: DOCUMENTATION-ONLY (with 2 UNSUPPORTED sub-assertions in the staged entries and 1 localization/version gap in Qwen `zh`/`ja` and Kimi GitHub `skills.md`).**

Every statement below was verified today (`2026-10-25`) directly from the primary vendor pages using `curl -sL --max-time 60 -A 'Mozilla/5.0'`, `grep -n -F`, and `sed -n '<L>p'`. No client binary was executed in this review; therefore, all statements about parser/runtime handling (`reads`, `ignores`, `accepts`) are **DOCUMENTATION-ONLY** (vendor-documented behavior, not runtime-tested by the lane), and any unstated synthesis (such as *"does not fail loudly: it loads, and its tool allowlist is silently dropped"*) is **UNSUPPORTED** inference unless explicitly framed as an inference from the two vendors' docs.

| # | Staged Claim / Sub-Claim | Staged Location | Verdict | Why |
|---|---|---|---|---|
| **1a** | Qwen Code English docs state Qwen Code reads `allowedTools` and ignores `allowed-tools`. | `chinese-client-skill-surfaces.md:34-35`, `client-surface-census-extension.md:44-46` | **DOCUMENTATION-ONLY** (Supported as a doc statement on EN page; **UNSUPPORTED** on `zh` and `ja` twins) | `qwen_en` line 222 (`qwen_en.txt:1020`) states verbatim: *"Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored."* However, the `zh` and `ja` twins omit the entire *"Share Skills with other tools"* section (`grep -n -F "allowed-tools"` returns **0 hits** on `zh` and `ja`). Calling it runtime-verified is unsupported; calling it vendor-documented on the English page is exact. |
| **1b** | *"So a skill authored on CodeBuddy or Claude Code and installed into Qwen Code does not fail loudly: it loads, and its tool allowlist is silently dropped."* | `chinese-client-skill-surfaces.md:35-37`, `skill-body-authority-and-enforcement.md:32-34` | **UNSUPPORTED (as a primary-page fact) / DOCUMENTATION-ONLY INFERENCE** | The Qwen English page (`qwen_en.txt:1020`) says *"An `allowed-tools` field written for another agent is ignored"* under *"Share Skills with other tools"*, which implies the skill loads and the `allowed-tools` field is ignored. The phrase *"does not fail loudly: it loads, and its tool allowlist is silently dropped"* does not appear on any opened page (`grep -n -F "silently dropped"` = 0 hits across all pages). An entry must quote `"ignored"` and attribute the cross-client consequence as an implication of the two docs, not an observed runtime trace. |
| **2a** | CodeBuddy CLI page (`https://www.codebuddy.ai/docs/zh/cli/skills`) documents and uses hyphenated `allowed-tools` in its frontmatter table and SKILL.md examples. | `chinese-client-skill-surfaces.md:22,33-34`, `SOURCES.append.md:21` (S217) | **SUPPORTED (in documentation & examples)** | `codebuddy_zh` has **9 raw HTML lines / 15 extracted text lines** matching `allowed-tools` (`codebuddy_zh.txt:921,947,1251,1285,1324,1370,1420,1422,1425,1471,1474,1517,1521,1552`), including 6 YAML frontmatter code blocks and the `### Frontmatter 字段` table (`codebuddy_zh.txt:947`). `grep -n -F "allowedTools"` = **0 hits**. |
| **2b** | CodeBuddy CLI **examples** emit `disable-model-invocation` (and CodeBuddy table row in `chinese-client-skill-surfaces.md:22` claims `name`, `description` are required on CLI). | `chinese-client-skill-surfaces.md:22,33-34` | **UNSUPPORTED for "CLI examples" / SUPPORTED for Frontmatter Table** | On `https://www.codebuddy.ai/docs/zh/cli/skills`, `disable-model-invocation` appears **exactly once** (`codebuddy_zh.raw:55` / `codebuddy_zh.txt:949`), inside the `### Frontmatter 字段` specification table—**not** in any YAML example block! Conversely, `disable: false` appears only on the **IDE** page (`codebuddy_ide_zh.txt:159`), not on the CLI page (`grep -n -F "disable:" codebuddy_zh.txt` = 0 hits). Furthermore, the CLI table (`codebuddy_zh.txt:943,945`) marks `name` and `description` as `否` (not required, falling back to directory name), whereas only the IDE page (`codebuddy_ide_zh.txt:138-139`) marks them `(必需)`. |
| **3a** | Kimi Code accepts `whenToUse` / `when-to-use` / `when_to_use` and `disableModelInvocation` / `disable-model-invocation` / `disable_model_invocation`. | `chinese-client-skill-surfaces.md:23,30-33`, `SOURCES.append.md:23` (S219) | **DOCUMENTATION-ONLY (on `www.kimi.com/code/docs/...` only; UNSUPPORTED on GitHub `MoonshotAI/kimi-cli`)** | `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` (`kimi_web_en.txt:226,228`) and its English twin `/code/docs/en/...` (`kimi_web_en_2.txt:226,228`) explicitly document `whenToUse` (with `when-to-use`, `when_to_use`) and `disableModelInvocation` (with `disable-model-invocation`, `disable_model_invocation`). However, `https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md` (`kimi_gh_raw.txt`) and its `zh` twin (`kimi_gh_zh_raw.txt`) have **0 hits** for all six strings! |
| **3b** | Why the two Kimi URLs diverge (attributed to "translation drift" in `translation-drift-across-vendors.md` and `SOURCES.append.md:23`). | `SOURCES.append.md:22-23` (S218, S219), `translation-drift-across-vendors.md:10-41` | **REFUTED as "translation drift" — it is a product/version split** | Both `kimi-cli` on GitHub (`docs/en` and `docs/zh`) and `kimi.com/code/docs` (`zh` and `en`) have matching bilingual pairs! The migration page `https://www.kimi.com/code/docs/kimi-code-cli/guides/migration.html` (`kimi_mig_zh.txt:159,169`) states that Kimi Code CLI was rewritten from Python/`uv` (`kimi-cli`, using `~/.kimi/`) to Node.js (`kimi-code`, using `~/.kimi-code/`). The frontmatter difference (`name`/`description`/`license`/`compatibility`/`metadata` in `kimi-cli` vs `name`/`description`/`type`/`whenToUse`/`disableModelInvocation`/`arguments` in `kimi-code`) is a **Generation 1 (`kimi-cli`) vs Generation 2 (`kimi-code`) rewrite split**, not EN-vs-ZH translation drift. |

---

## 1. Fetched Primary Sources & Snapshots

All fetches were executed on `2026-10-25` (`date -I`) with `curl -sL --max-time 60 -A 'Mozilla/5.0'`. Text-extracted snapshots (all `< 42 KB`, well under the 300 KB cap) are saved under `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/`.

Command used:
```bash
curl -sL --max-time 60 -A 'Mozilla/5.0' -o "$SCRATCH/$name.raw" -w '%{http_code}' "$url"
wc -c < "$SCRATCH/$name.raw" && sha256sum "$SCRATCH/$name.raw"
```

| Snapshot file (`.ufo/waves/round-73/w1/build/ReviewerDivergence/`) | Primary URL | HTTP Status | Access Date | Raw Bytes | Raw SHA-256 | Extracted Text Bytes | Extracted Text SHA-256 |
|---|---|---:|---|---:|---|---:|---|
| `qwen_en.txt` | `https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/` | 200 | `2026-10-25` | 607,888 | `6c15b3d819202e6e08f2d7441b05c915e8e45873fd9d32a48fb2810afb2c9ebf` | 32,769 | `71db00db79fa0232a6cb334cec3ba646b1b75416021ea72dc0ba701316088cd1` |
| `qwen_zh.txt` | `https://qwenlm.github.io/qwen-code-docs/zh/users/features/skills/` | 200 | `2026-10-25` | 592,311 | `3c7ff8cd3e66c05f949525ed5861287b03cc4dea2f267c742e9fbaa130b51b90` | 30,025 | `0c499dd581b1ff96bd8ff4cc7a356cb58e2a82dc4e73d3d05e8f6fe61a600c34` |
| `qwen_ja.txt` | `https://qwenlm.github.io/qwen-code-docs/ja/users/features/skills/` | 200 | `2026-10-25` | 623,622 | `b507d57f0f4f259beeaa2ceb065630bd0308699623536920d98dcb231e41cdd2` | 41,654 | `365ef345a32178f55725be39369c7a1475425212b7cf09f3420329da4e70d216` |
| `codebuddy_zh.txt` | `https://www.codebuddy.ai/docs/zh/cli/skills` | 200 | `2026-10-25` | 217,520 | `ee9e3b7187c5105bd1147dff41c1ecb793b695a28f3d1804344f543d6e34f2ee` | 28,640 | `4ba57f11932203e2cb5d946c2f1f7d63db3c9080ff50aa1f871348dc90c0ef4a` |
| `codebuddy_ide_zh.txt` | `https://www.codebuddy.ai/docs/zh/ide/Features/Skills` | 200 | `2026-10-25` | 36,633 | `35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6` | 4,710 | `796b4137da011f0d299788ece73d99cd82e390bd047b499f8819f143db99283f` |
| `kimi_gh_raw.txt` | `https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md` | 200 | `2026-10-25` | 13,528 | `5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52` | 13,528 | `5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52` |
| `kimi_gh_zh_raw.txt` | `https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/zh/customization/skills.md` | 200 | `2026-10-25` | 12,366 | `491db492cc1e9090dd930177e838d3e2669573afafcecc42d9fb57cbfdd146cf` | 12,366 | `491db492cc1e9090dd930177e838d3e2669573afafcecc42d9fb57cbfdd146cf` |
| `kimi_web_en.txt` | `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` | 200 | `2026-10-25` | 79,788 | `e3b314dcff628fc2f88fe6b679e7d6096a209725451957b8ca35360fb5f20989` | 8,254 | `19cc0175de8bf5ef5807540a07ecd4b16445a437b42f55fa115f8c4a9678bbe7` |
| `kimi_web_en_2.txt` | `https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html` | 200 | `2026-10-25` | 79,962 | `a6769b0c44d89eaa1e4ce59eed6dbfc20aa7b246a557229f316048a8f165bea4` | 9,215 | `b54fe5b0a635431a2a017ef40fe72e97fac77d36d8002a8af263c6b52059bbe1` |
| `kimi_mig_zh.txt` | `https://www.kimi.com/code/docs/kimi-code-cli/guides/migration.html` | 200 | `2026-10-25` | 64,552 | `b995a993870c3043ef7345a6163622a61c005b829c17e97ab78dacadbb9dfd23` | 3,191 | `9a9faf6fd202d53fb85560307836c9cbc841865b2013b2ace6f4aa02f5d2a96a` |

---

## 2. Claim-by-Claim Verification, `grep -n -F` Hits, and Located Quotes

### Claim 1: Qwen Code reads `allowedTools` and ignores `allowed-tools` (plus `disable-model-invocation`)

#### 1.1 `grep -n -F` across Qwen Code English, Chinese (`zh`), and Japanese (`ja`) pages

Command:
```bash
BUILD="/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence"
grep -n -F "allowedTools" "$BUILD"/qwen_*.txt
grep -n -F "allowed-tools" "$BUILD"/qwen_*.txt
grep -n -F "disable-model-invocation" "$BUILD"/qwen_*.txt
grep -n -F "disableModelInvocation" "$BUILD"/qwen_*.txt
```

Observed output on extracted text snapshots (`$BUILD/qwen_*.txt`) and raw HTML (`qwen_*.raw`):

- **`allowedTools` in `qwen_en` (6 hits in `qwen_en.txt` / 6 hits in `qwen_en.raw`):**
  - `qwen_en.txt:955` (`qwen_en.raw:178`): `Resuming a session with `--continue` / `--resume` re-applies both halves — the `allowedTools` allow rules and the `hooks:` — of every Skill the model loaded through the Skill tool, because those invocations are recorded in the conversation as tool calls.`
  - `qwen_en.txt:957` (`qwen_en.raw:179`): `In these cases a Skill that declares `hooks:` or `allowedTools` leaves a debug log line saying why. ... The match covers the body only, so an edit to just the frontmatter is re-applied with the new `allowedTools` and `hooks:`.`
  - `qwen_en.txt:965` (`qwen_en.raw:183`): `The Skill’s body and its `allowedTools` still apply in those sessions, but its gate does not, so a rule you rely on a hook to enforce is not enforced there. Bare mode goes further: no Skills are discovered at all, so there is no body and no `allowedTools` either.`
  - `qwen_en.txt:967` (`qwen_en.raw:184`): `With an IDE companion connected that value is live: revoking trust silences an already-registered gate — and suspends the Skill’s `allowedTools` — at the next tool call, without a restart.`
  - `qwen_en.txt:1016` (`qwen_en.raw:219`): `These Skills load as personal Skills, so their `allowedTools` and hooks are not gated by folder trust, even when a trusted project’s settings add the directory: only point this at folders you control.`
  - `qwen_en.txt:1020` (`qwen_en.raw:222`): `Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored.`

- **`allowedTools` in `qwen_zh` (4 hits in `qwen_zh.txt` / 4 hits in `qwen_zh.raw`):**
  - `qwen_zh.txt:942` (`qwen_zh.raw:169`): `使用 `--continue` / `--resume` 恢复会话时，会重新应用模型通过 Skill 工具加载的每个 Skill 的两部分 —— `allowedTools` 允许规则和 `hooks:` —— 因为这些调用在对话中被记录为工具调用。`
  - `qwen_zh.txt:944` (`qwen_zh.raw:170`): `在这些情况下，声明了 `hooks:` 或 `allowedTools` 的 Skill 会留下一行调试日志说明原因。 ... 匹配仅覆盖主体，因此仅编辑 frontmatter 会使用新的 `allowedTools` 和 `hooks:` 重新应用。`
  - `qwen_zh.txt:952` (`qwen_zh.raw:174`): `Skill 的主体及其 `allowedTools` 在这些会话中仍然有效，但其 gate 不会生效，因此你依赖 hook 强制执行的规则在那里不会被强制执行。Bare 模式更进一步：根本不会发现任何 Skills，因此既没有主体也没有 `allowedTools`。`
  - `qwen_zh.txt:954` (`qwen_zh.raw:175`): `当有 IDE companion 连接时，该值是实时的：撤销信任会在下一次工具调用时静默已注册的 gate —— 并暂停 Skill 的 `allowedTools` —— 无需重启。`
  - *(Note: lines 1016 and 1020 of `qwen_en.txt` are inside the `Share Skills with other tools` section, which is completely absent from `qwen_zh.txt`!)*

- **`allowedTools` in `qwen_ja` (2 hits in `qwen_ja.txt` / 2 hits in `qwen_ja.raw`):**
  - `qwen_ja.txt:956` (`qwen_ja.raw:173`): `これらのセッションでも Skill の本体とその `allowedTools` は引き続き適用されますが、ゲートは適用されないため、フックに適用を依存しているルールはそこで適用されません。ベアモードはさらに進みます。Skill はまったく検出されないため、本体も `allowedTools` もありません。`
  - `qwen_ja.txt:958` (`qwen_ja.raw:174`): `信頼を取り消すと、次にツール呼び出しがあったときに、すでに登録されたゲートがサイレントになり、Skill の `allowedTools` も一時停止されます。`
  - *(Note: `qwen_ja` has an older version of the `--continue` / `--resume` bullet at `qwen_ja.txt:948` that says session hooks are in-memory only and not restored, and like `qwen_zh`, `qwen_ja` omits the entire `Share Skills with other tools` section!)*

- **`allowed-tools` across all three Qwen pages:**
  - `qwen_en.txt:1020` (`qwen_en.raw:222`): **1 hit**: `Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored.`
  - `qwen_zh.txt` / `qwen_zh.raw`: **0 hits**
  - `qwen_ja.txt` / `qwen_ja.raw`: **0 hits**

- **`disable-model-invocation` vs `disableModelInvocation` across all three Qwen pages:**
  - `disable-model-invocation`: **4 hits** in `qwen_en.txt` (`903, 917, 922, 957`), **4 hits** in `qwen_zh.txt` (`890, 904, 909, 944`), **3 hits** in `qwen_ja.txt` (`896, 910, 915`).
  - `disableModelInvocation`: **0 hits** across all three Qwen pages (`en`, `zh`, `ja`).
  - *(Observation: Qwen Code uses camelCase for `allowedTools`, but hyphenated `disable-model-invocation` and `user-invocable`!)*

#### 1.2 Exact `sed -n '<L>p'` Verification & Located Quote for Qwen Code

Command:
```bash
sed -n '222p' "$SCRATCH/qwen_en.raw"
sed -n '1020p' "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/qwen_en.txt"
```

Observed `sed -n '222p'` on raw HTML (`qwen_en.raw`):
```html
<p class="x:not-first:mt-[1.25em] x:leading-7">Qwen Code reads the <code class="nextra-code" dir="ltr">allowedTools</code> frontmatter field. An <code class="nextra-code" dir="ltr">allowed-tools</code> field written for another agent is ignored.</p>
```

Observed `sed -n '1020p'` on extracted text (`qwen_en.txt`):
```text
Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored.
```

- **Located quote (16 words, quote-equal after stripping HTML tags `<p ...>`, `<code ...>`, `</code>`, `</p>`; byte-exact to `qwen_en.txt:1020` when `<code ...>` is rendered as backticks):**
  > "Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored."
  — `https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/`, § `View available Skills` → `Share Skills with other tools` (`qwen_en.raw:222` / `qwen_en.txt:1020`).

#### 1.3 Verdict on Qwen Code Claim
- **Verdict:** **DOCUMENTATION-ONLY** (for Qwen reading `allowedTools` and ignoring `allowed-tools` on the English page); **UNSUPPORTED** on the `zh` and `ja` twins (where `allowed-tools` does not appear); **UNSUPPORTED as a direct quote** for `"silently dropped"` / `"does not fail loudly"`.
- **Is there a sentence that says `"ignores"`, or is it inferred?**
  There **is** an explicit sentence on the English page (`qwen_en.raw:222`) that uses the exact passive verb **"is ignored"**: *"Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored."* Because this sentence appears inside the subsection *"Share Skills with other tools"* (immediately after explaining how to point `skills.directories` at `["~/.claude/skills"]` or use `~/.agents/skills/`), the documentation explicitly addresses cross-agent skill sharing and states that `allowed-tools` is ignored. However, `"does not fail loudly: it loads, and its tool allowlist is silently dropped"` (`chinese-client-skill-surfaces.md:36-37`) is authorial paraphrase/inference and is not verified at runtime.

---

### Claim 2: CodeBuddy CLI examples use hyphenated `allowed-tools` and `disable-model-invocation`

#### 2.1 `grep -n -F` on CodeBuddy CLI (`https://www.codebuddy.ai/docs/zh/cli/skills`) and IDE (`https://www.codebuddy.ai/docs/zh/ide/Features/Skills`)

Command:
```bash
BUILD="/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence"
grep -n -F "allowed-tools" "$BUILD/codebuddy_zh.txt" "$BUILD/codebuddy_ide_zh.txt"
grep -n -F "allowedTools" "$BUILD/codebuddy_zh.txt" "$BUILD/codebuddy_ide_zh.txt"
grep -n -F "disable-model-invocation" "$BUILD/codebuddy_zh.txt" "$BUILD/codebuddy_ide_zh.txt"
grep -n -F "disable" "$BUILD/codebuddy_zh.txt" "$BUILD/codebuddy_ide_zh.txt"
```

Observed output:
- **`allowed-tools` on `codebuddy_zh.txt` (CLI page — 15 lines in `codebuddy_zh.txt`, 9 lines in `codebuddy_zh.raw`):**
  - `codebuddy_zh.txt:921` (`codebuddy_zh.raw:39`, YAML example under `## SKILL.md 格式`): `allowed-tools: Read, Write, Bash, WebFetch`
  - `codebuddy_zh.txt:947` (`codebuddy_zh.raw:55`, table row under `### Frontmatter 字段`): `| `allowed-tools` | 否 | 允许使用的工具白名单，逗号分隔 | `Read, Write, Bash``
  - `codebuddy_zh.txt:1251` (`codebuddy_zh.raw:127`, YAML example 1 `pdf`): `allowed-tools: Read, Write, Bash, WebFetch`
  - `codebuddy_zh.txt:1285` (`codebuddy_zh.raw:152`, YAML example 2 `data-analysis`): `allowed-tools: Read, Write, Bash, WebFetch, NotebookEdit`
  - `codebuddy_zh.txt:1324` (`codebuddy_zh.raw:184`, YAML example 3 `code-review`): `allowed-tools: Read, Grep, Bash, Edit`
  - `codebuddy_zh.txt:1370` (`codebuddy_zh.raw:222`, list item under `## AI 如何选择 Skills`): `工具需求：任务所需工具是否在 allowed-tools 范围内`
  - `codebuddy_zh.txt:1420` (`codebuddy_zh.raw:227`, heading `### allowed-tools 白名单`): `allowed-tools 白名单 ​`
  - `codebuddy_zh.txt:1422` (`codebuddy_zh.raw:227`): `通过 `allowed-tools` 字段限制 Skill 可以使用的工具：`
  - `codebuddy_zh.txt:1425` (`codebuddy_zh.raw:227`, YAML snippet): ``allowed-tools: Read, Write, Bash(git:*), Grep``
  - `codebuddy_zh.txt:1471` (`codebuddy_zh.raw:232`, YAML best-practice example): `allowed-tools: Bash`
  - `codebuddy_zh.txt:1474` (`codebuddy_zh.raw:235`, YAML best-practice example): `allowed-tools: Read, Write, Bash(git:status,git:diff), Grep``
  - `codebuddy_zh.txt:1517` (`codebuddy_zh.raw:244`, FAQ): `验证 allowed-tools 是否包含所需工具`
  - `codebuddy_zh.txt:1521` (`codebuddy_zh.raw:244`, FAQ): `检查 allowed-tools 配置`
  - `codebuddy_zh.txt:1552` (`codebuddy_zh.raw:245`, `### Skills + MCP`): `Skills 可以调用 MCP 提供的外部工具（如果在 allowed-tools 中）。`

- **`allowed-tools` on `codebuddy_ide_zh.txt` (IDE page — 1 hit):**
  - `codebuddy_ide_zh.txt:158` (YAML example under `### SKILL.md (必需)`): `allowed-tools: # 可选，指定允许使用的工具`

- **`allowedTools` on both CodeBuddy pages:** **0 hits**.

- **`disable-model-invocation` on `codebuddy_zh.txt` (CLI page — 1 hit ONLY):**
  - `codebuddy_zh.txt:949` (`codebuddy_zh.raw:55`, table row under `### Frontmatter 字段`):
    `| `disable-model-invocation` | 否 | 设置为 `true` 时，Skill 不会出现在 Skill 工具中，只能通过 `/skill-name` 手动触发 | `true``
  - **0 hits in any YAML example block on `codebuddy_zh.txt`!**
  - **0 hits on `codebuddy_ide_zh.txt`!**

- **`disable` (bare key) on both CodeBuddy pages:**
  - `codebuddy_ide_zh.txt:159` (YAML example under `### SKILL.md (必需)`): `disable: false # 可选，是否禁用`
  - `codebuddy_zh.txt` (CLI page): **0 hits** for frontmatter key `disable` (only line 1406 English error string `"Skill \"<name>\" is disabled via skillOverrides..."` and line 949 `disable-model-invocation`).

#### 2.2 Exact `sed -n '<L>p'` Verification & Located Quotes for CodeBuddy CLI

Command:
```bash
sed -n '39p' "$SCRATCH/codebuddy_zh.raw"
sed -n '921p;947p;949p' "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/codebuddy_zh.txt"
```

Observed `sed -n '39p'` on `codebuddy_zh.raw`:
```html
<span class="line"><span style="--shiki-light:#11782a;--shiki-dark:#85E89D;">allowed-tools</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">: </span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">Read, Write, Bash, WebFetch</span></span>
```

Observed `sed -n '921p;947p;949p'` on `codebuddy_zh.txt`:
```text
allowed-tools: Read, Write, Bash, WebFetch
| `allowed-tools` | 否 | 允许使用的工具白名单，逗号分隔 | `Read, Write, Bash`
| `disable-model-invocation` | 否 | 设置为 `true` 时，Skill 不会出现在 Skill 工具中，只能通过 `/skill-name` 手动触发 | `true`
```

- **Located quote 2A (5 words, quote-equal after stripping Shiki `<span ...>` tags from `codebuddy_zh.raw:39`; byte-exact to `codebuddy_zh.txt:921`):**
  > "`allowed-tools: Read, Write, Bash, WebFetch`"
  — `https://www.codebuddy.ai/docs/zh/cli/skills`, § `SKILL.md 格式` (`codebuddy_zh.raw:39` / `codebuddy_zh.txt:921`).

- **Located quote 2B (12 tokens, quote-equal after stripping HTML `<tr><td><code>` tags from `codebuddy_zh.raw:55`; byte-exact to `codebuddy_zh.txt:949`):**
  > "`| disable-model-invocation | 否 | 设置为 true 时，Skill 不会出现在 Skill 工具中，只能通过 /skill-name 手动触发 | true |`"
  — `https://www.codebuddy.ai/docs/zh/cli/skills`, § `SKILL.md 格式` → `### Frontmatter 字段` (`codebuddy_zh.raw:55` / `codebuddy_zh.txt:949`).

#### 2.3 Verdict on CodeBuddy CLI Claim
- **Verdict:**
  - **`allowed-tools` in CodeBuddy CLI examples and frontmatter table:** **SUPPORTED** (appears in 6 YAML examples and the `Frontmatter 字段` table).
  - **`disable-model-invocation` in CodeBuddy CLI "examples":** **UNSUPPORTED** for *examples*, **SUPPORTED** for the *`Frontmatter 字段` table* (`codebuddy_zh.txt:949`). The staged entry `chinese-client-skill-surfaces.md:22` (*"CLI examples also use `disable-model-invocation`"* and `:33-34` *"CodeBuddy's CLI examples emit the hyphenated `disable-model-invocation` and `allowed-tools` spellings (S217)"*) is factually inaccurate about where `disable-model-invocation` appears: it is a row in the CLI `Frontmatter 字段` table (`| disable-model-invocation | 否 | ... | true |`), not in a YAML example block.
  - **Bonus accuracy trap in `chinese-client-skill-surfaces.md:22`:** The staged table says for CodeBuddy (`S216, S217`): *"`name`, `description` required; `allowed-tools`, `disable` optional; CLI examples also use `disable-model-invocation`"*. In reality:
    1. On the IDE page (`S216`, `codebuddy_ide_zh.txt:138-139,158-159`), `name` and `description` are marked `(必需)` and the example shows `allowed-tools:` and `disable: false` as `# 可选`.
    2. On the CLI page (`S217`, `codebuddy_zh.txt:943-959`), the `Frontmatter 字段` table lists 9 fields (`name`, `description`, `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `model`, `hooks`), **all 9 marked `必填: 否`** (`name` defaults to directory name; two CLI examples at `codebuddy_zh.txt:984,998` omit `name` entirely!).

---

### Claim 3: Kimi Code accepts `whenToUse`/`when-to-use`/`when_to_use` and `disableModelInvocation`/`disable-model-invocation`/`disable_model_invocation`

#### 3.1 `grep -n -F` across both Kimi Code documentation surfaces

Command:
```bash
BUILD="/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence"
for k in "whenToUse" "when-to-use" "when_to_use" "disableModelInvocation" "disable-model-invocation" "disable_model_invocation"; do
  echo "=== $k ==="
  grep -n -F "$k" "$BUILD"/kimi_*.txt || true
done
```

Observed output:
- **On `https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md` (`kimi_gh_raw.txt`) and `.../docs/zh/customization/skills.md` (`kimi_gh_zh_raw.txt`):**
  - `whenToUse`: **0 hits**
  - `when-to-use`: **0 hits**
  - `when_to_use`: **0 hits**
  - `disableModelInvocation`: **0 hits**
  - `disable-model-invocation`: **0 hits**
  - `disable_model_invocation`: **0 hits**
  - Instead, `kimi_gh_raw.txt:168-174` (and `kimi_gh_zh_raw.txt:168-174`) documents only the 5 standard Agent Skills fields (`name`, `description`, `license`, `compatibility`, `metadata`, all `Required: No`) plus `type: flow` in § `Flow skills` (`kimi_gh_raw.txt:276,282`).

- **On `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` (`kimi_web_en.txt`, Chinese) and `https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html` (`kimi_web_en_2.txt`, English):**
  - **`whenToUse` (4 hits in `kimi_web_en.txt` / 4 hits in `kimi_web_en.raw`; 4 hits in `kimi_web_en_2.txt`):**
    - `kimi_web_en.txt:202` (`kimi_web_en.raw:376`, YAML example): `whenToUse: 当用户让我编写、修改或审查项目源代码时`
    - `kimi_web_en.txt:226` (`kimi_web_en.raw:388`, `### Frontmatter 字段` table): `| `whenToUse` | 触发场景描述，也接受 `when-to-use`、`when_to_use` 写法`
    - `kimi_web_en.txt:282` (`kimi_web_en.raw:389`, `## 调用 Skill` prose): `模型也可以根据 `description` 和 `whenToUse` 自动调用 Skill。`disableModelInvocation` 设为 true 或 `type` 设为 flow 时不自动调用。Skill 调用最多允许嵌套 3 层，超过后会被终止。`
    - `kimi_web_en.txt:291` (`kimi_web_en.raw:393`, `## 完整示例` YAML): `whenToUse: 当用户让我审查 PR、检查代码变更或评估提交质量时`
  - **`when-to-use` and `when_to_use` (1 hit each in `kimi_web_en.txt` and `kimi_web_en_2.txt`):**
    - `kimi_web_en.txt:226` (`kimi_web_en.raw:388`): `| `whenToUse` | 触发场景描述，也接受 `when-to-use`、`when_to_use` 写法`
    - `kimi_web_en_2.txt:226` (`kimi_web_en_2.raw:388`): `| `whenToUse` | Description of when the Skill should be triggered. Also accepts `when-to-use` and `when_to_use``
  - **`disableModelInvocation` (3 hits in `kimi_web_en.txt` / 3 hits in `kimi_web_en.raw`; 3 hits in `kimi_web_en_2.txt`):**
    - `kimi_web_en.txt:203` (`kimi_web_en.raw:377`, YAML example): `disableModelInvocation: false`
    - `kimi_web_en.txt:228` (`kimi_web_en.raw:388`, `### Frontmatter 字段` table): `| `disableModelInvocation` | 设为 true 禁止模型自动调用，也接受 `disable-model-invocation`、`disable_model_invocation` 写法`
    - `kimi_web_en.txt:282` (`kimi_web_en.raw:389`, `## 调用 Skill` prose): `模型也可以根据 `description` 和 `whenToUse` 自动调用 Skill。`disableModelInvocation` 设为 true 或 `type` 设为 flow 时不自动调用。Skill 调用最多允许嵌套 3 层，超过后会被终止。`
  - **`disable-model-invocation` and `disable_model_invocation` (1 hit each in `kimi_web_en.txt` and `kimi_web_en_2.txt`):**
    - `kimi_web_en.txt:228` (`kimi_web_en.raw:388`): `| `disableModelInvocation` | 设为 true 禁止模型自动调用，也接受 `disable-model-invocation`、`disable_model_invocation` 写法`
    - `kimi_web_en_2.txt:228` (`kimi_web_en_2.raw:388`): `| `disableModelInvocation` | If `true`, blocks automatic model invocation. Also accepts `disable-model-invocation`, `disable_model_invocation``

#### 3.2 Exact `sed -n '<L>p'` Verification & Located Quotes for Kimi Code

Command:
```bash
sed -n '226p;228p;282p' "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/kimi_web_en.txt"
sed -n '226p;228p' "/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/kimi_web_en_2.txt"
```

Observed output (`kimi_web_en.txt` — Chinese page at `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html`):
```text
| `whenToUse` | 触发场景描述，也接受 `when-to-use`、`when_to_use` 写法
| `disableModelInvocation` | 设为 true 禁止模型自动调用，也接受 `disable-model-invocation`、`disable_model_invocation` 写法
模型也可以根据 `description` 和 `whenToUse` 自动调用 Skill。`disableModelInvocation` 设为 true 或 `type` 设为 flow 时不自动调用。Skill 调用最多允许嵌套 3 层，超过后会被终止。
```

Observed output (`kimi_web_en_2.txt` — English page at `https://www.kimi.com/code/docs/en/kimi-code-cli/customization/skills.html`):
```text
| `whenToUse` | Description of when the Skill should be triggered. Also accepts `when-to-use` and `when_to_use`
| `disableModelInvocation` | If `true`, blocks automatic model invocation. Also accepts `disable-model-invocation`, `disable_model_invocation`
```

- **Located quote 3A (Chinese page, 7 tokens, quote-equal after stripping `<tr><td><code>` tags from `kimi_web_en.raw:388`; byte-exact to `kimi_web_en.txt:226`):**
  > "`| whenToUse | 触发场景描述，也接受 when-to-use、when_to_use 写法`"
  — `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html`, § `文件格式` → `### Frontmatter 字段` (`kimi_web_en.raw:388` / `kimi_web_en.txt:226`).
  *(English twin quote, 14 words, `kimi_web_en_2.txt:226`: "`| whenToUse | Description of when the Skill should be triggered. Also accepts when-to-use and when_to_use`")*

- **Located quote 3B (Chinese page, 9 tokens, quote-equal after stripping `<tr><td><code>` tags from `kimi_web_en.raw:388`; byte-exact to `kimi_web_en.txt:228`):**
  > "`| disableModelInvocation | 设为 true 禁止模型自动调用，也接受 disable-model-invocation、disable_model_invocation 写法`"
  — `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html`, § `文件格式` → `### Frontmatter 字段` (`kimi_web_en.raw:388` / `kimi_web_en.txt:228`).
  *(English twin quote, 11 words, `kimi_web_en_2.txt:228`: "`| disableModelInvocation | If true, blocks automatic model invocation. Also accepts disable-model-invocation, disable_model_invocation`")*

#### 3.3 Verdict on Kimi Code Claim
- **Verdict:** **DOCUMENTATION-ONLY** on `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` (and its English twin `/code/docs/en/...`); **UNSUPPORTED** on `https://raw.githubusercontent.com/MoonshotAI/kimi-cli/main/docs/en/customization/skills.md` (which documents the older Python `kimi-cli` surface where none of `whenToUse`, `when-to-use`, `when_to_use`, `disableModelInvocation`, `disable-model-invocation`, `disable_model_invocation` appear).
- **Critical C1 Counter Implication (`check_cn_vendor_surfaces.py`):**
  In `plans/round-73.md:68-70`, conjunct **(a)** requires that every backticked token in a vendor's table row *"occur word-bounded in the committed page snapshot of a source that row cites"*. As long as the Kimi Code row cites **both** the GitHub `kimi-cli` source and the `www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` source (and both snapshots are committed), tokens like `.kimi-code/skills/`, `$KIMI_CODE_HOME/skills/`, `whenToUse`, and `disableModelInvocation` will resolve against the `www.kimi.com` snapshot (`kimi_web_en.txt`), while `.kimi/skills/` or `merge_all_available_skills` will resolve against the GitHub `kimi-cli` snapshot (`kimi_gh_raw.txt`). If only the GitHub snapshot were cited, `whenToUse` and `disableModelInvocation` would fail conjunct (a)!

---

## 3. Exact Safe Wording for the Round-73 Knowledge Entry (`chinese-vendor-skill-surfaces-round73.md`)

To pass every lane quality gate (`QUALITY.md` quote/location/shaping rules, `CORPUS.md` command/sweep rules, and `check_cn_vendor_surfaces.py` word-bounded snapshot token matching) without asserting unmeasured runtime behavior or misattributing table rows as YAML examples, the entry may safely use the following exact wording:

### 3.1 Safe Wording for the Vendor Table Rows (CodeBuddy and Kimi Code)
- **CodeBuddy row (`S216`, `S217`):**
  - Do **not** say *"CLI examples also use `disable-model-invocation`"*.
  - Safe wording:
    > "`name`, `description` (marked required on the IDE page, optional in the CLI table); `allowed-tools`, `disable` on the IDE page; the CLI `Frontmatter 字段` table lists `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`, `agent`, `model`, `hooks`"
  - Backticked tokens guaranteed to occur word-bounded in `codebuddy_zh.txt` (`https://www.codebuddy.ai/docs/zh/cli/skills`):
    - Roots: `` `.codebuddy/skills/` ``, `` `~/.codebuddy/skills/` ``
    - Frontmatter keys: `` `name` ``, `` `description` ``, `` `allowed-tools` ``, `` `disable-model-invocation` ``, `` `user-invocable` ``, `` `context` ``, `` `agent` ``, `` `model` ``, `` `hooks` ``
  - Backticked token occurring only in `codebuddy_ide_zh.txt` (`https://www.codebuddy.ai/docs/zh/ide/Features/Skills`):
    - `` `disable` `` (at line 159: `disable: false # 可选，是否禁用`).

- **Kimi Code row (`S218`, `S219`):**
  - Safe wording:
    > "On `www.kimi.com/code/docs` (Node.js `kimi-code`): `name`, `description`, `type` (`prompt`/`inline`/`flow`), `whenToUse` (also `when-to-use`, `when_to_use`), `disableModelInvocation` (also `disable-model-invocation`, `disable_model_invocation`), `arguments`; on GitHub `MoonshotAI/kimi-cli` (Python `kimi-cli`): `name`, `description`, `license`, `compatibility`, `metadata`, and `type: flow`"
  - Backticked tokens guaranteed to occur word-bounded in `kimi_web_en.txt` (`https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html`):
    - Roots: `` `.kimi-code/skills/` ``, `` `$KIMI_CODE_HOME/skills/` ``, `` `~/.kimi-code/skills/` ``, `` `.agents/skills/` ``, `` `~/.agents/skills/` ``
    - Frontmatter keys: `` `name` ``, `` `description` ``, `` `type` ``, `` `whenToUse` ``, `` `when-to-use` ``, `` `when_to_use` ``, `` `disableModelInvocation` ``, `` `disable-model-invocation` ``, `` `disable_model_invocation` ``, `` `arguments` ``

### 3.2 Safe Wording for the Cross-Client Frontmatter-Spelling Hazard Paragraph

Replace `chinese-client-skill-surfaces.md:30-39` with:

> **Documented frontmatter-spelling divergence across clients.** On `www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` (`# Frontmatter 字段`), Kimi Code CLI documents three spellings for its trigger-scenario field — "`| whenToUse | 触发场景描述，也接受 when-to-use、when_to_use 写法`" — and the same three-spelling tolerance for model-invocation blocking: "`| disableModelInvocation | 设为 true 禁止模型自动调用，也接受 disable-model-invocation、disable_model_invocation 写法`" (the older `MoonshotAI/kimi-cli` GitHub markdown `docs/en/customization/skills.md` lists neither field). CodeBuddy CLI (`https://www.codebuddy.ai/docs/zh/cli/skills`, `# SKILL.md 格式` and `# Frontmatter 字段`) documents the hyphenated `disable-model-invocation` in its frontmatter table and uses `allowed-tools` in six YAML examples (e.g., "`allowed-tools: Read, Write, Bash, WebFetch`"). By contrast, Qwen Code's English documentation (`https://qwenlm.github.io/qwen-code-docs/en/users/features/skills/`, `# Share Skills with other tools`; omitted from the `/zh/` and `/ja/` translations) states: *"Qwen Code reads the `allowedTools` frontmatter field. An `allowed-tools` field written for another agent is ignored."* (Note: Qwen Code's own invocation-blocking key on the same page is the hyphenated `disable-model-invocation: true`.) By these vendor documents (documentation-only; not runtime-tested in this round), a skill using `allowed-tools` from CodeBuddy CLI or Claude Code has that field ignored when loaded by Qwen Code.

---

## Tooling & Hygiene Record
- **Tooling installed/updated:** None needed (`curl`, `python3`, `grep`, `sed`, `sha256sum` were sufficient).
- **Scratch directory:** `/tmp/k73w1-ReviewerDivergence.a4jQ` created via `mktemp -d` and removed via `rm -rf` before returning (`ls -ld /tmp/k73w1-ReviewerDivergence.*` verified clean).
- **Saved text snapshots:** 10 `.txt` files saved in `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ReviewerDivergence/` (total 208 KB; largest file 41,654 B).
- **Lane & fleet repo mutation:** Zero tracked or untracked edits outside `.ufo/waves/round-73/w1/`.
