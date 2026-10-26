# CriticEntryRisk — pre-attack of the staged C1 entry (round 73, wave 1)

**Verdict: the staged entry does not clear the bar as written, and it cannot reach C1's frozen target.**
Copied into the lane unchanged, its vendor table scores **2 of 4** under the plan's own predicate (a), not 4:
the TRAE row carries two root tokens no cited page contains (`~/.trae/skills/`; `~/.trae-cn/skills/` written
with a trailing slash the page does not print) and the Zhipu row carries **no path or placement token at all**
(`uploaded package` is not a token). Beyond that, five universality claims ("all four …") are falsified by the
pages the entry itself cites, one provenance claim ("wave 1 established") points at a package file the plan
does not assimilate and at no lane entry, one runtime claim ("silently dropped") exceeds documentary evidence,
one negative claim has no sweep, one cross-reference points at the wrong package entry, the entry opens with a
blank line and an H1 instead of `source:` lines, and four of six source lines carry no located quote.

Axes impacted: **coverage (C1) only.** C2 (own description) and C3 (tip battery) are untouched by anything
here. Nothing I ran mutated the lane; the trace is under
`.ufo/waves/round-73/w1/build/CriticEntryRisk/` (`sources-fetched.tsv` lists URL, HTTP status, bytes, sha256,
access date for every fetch; two oversized raw fetches were deleted after their hashes were recorded).
No tool was installed. No `/tmp` scratch was needed; every command ran from the lane root or the build dir.

Entry under attack: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md`
(read-only; line numbers below are `nl -ba` of that file). Bar: `corpus/QUALITY.md` (Q12–Q14, Q23, Q26, Q32,
Q42, Q51, Q56, Q65) and `/home/vgpnk/Projects/shokunin/CORPUS.md` (provenance trio, count, sweep, quote
location, append-only).

---

## 1. What I opened (nothing accepted from the entry or the plan)

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o S214.raw -w '%{http_code}' https://docs.trae.cn/ide_skills
200   bytes=112442  sha256=7332587cd47670dcc659e71b4584378d817ae6224c96a0aa0a2bbd73e91a40c6
$ … S216 https://www.codebuddy.ai/docs/zh/ide/Features/Skills
200   bytes=36633   sha256=35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6
$ … S217 https://www.codebuddy.ai/docs/zh/cli/skills
200   bytes=217520  sha256=ee9e3b7187c5105bd1147dff41c1ecb793b695a28f3d1804344f543d6e34f2ee
$ … S218 https://raw.githubusercontent.com/moonshotai/kimi-cli/main/docs/en/customization/skills.md
200   bytes=13528   sha256=5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52
$ … S219 https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html
200   bytes=79788   sha256=e3b314dcff628fc2f88fe6b679e7d6096a209725451957b8ca35360fb5f20989
$ … S221 https://docs.bigmodel.cn/cn/managed-agents/skills.md
200   bytes=7381    sha256=b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618
```

HTML pages were reduced to text by an inline extractor (`<script>/<style>/<noscript>` blocks and all tags
removed, block tags → newline, whitespace collapsed; the extractor is in the transcript, snapshots are
`S214.txt`, `S216.txt`, `S217.txt`, `S219.txt`). Every quote below is pasted from the named snapshot line, with
the bytes I dropped named; `byte-exact` is not claimed for any HTML-derived quote (Q56).

---

## 2. Findings (each with its command and its observed output)

### F1 — TRAE user roots: one invented, one mis-transcribed; both sink predicate (a)

```
$ grep -o '~/\.trae/skills' S214.raw | wc -l
0
$ grep -o '~/\.trae-cn/skills' S214.raw | wc -l
1
$ sed -n '107p' S214.txt
macOS/Linux：本地根目录 ~/.trae-cn/skills 。
$ grep -c '国际\|国内' S214.raw
0
```

The page prints `~/.trae-cn/skills` — **no trailing slash** — once, and never mentions a domestic/international
build split, nor `~/.trae/skills/`. Entry line 21 asserts `~/.trae-cn/skills/` (domestic build),
`~/.trae/skills/` (international). The international docs host returns a 1,903,042-byte JS shell
(`https://docs.trae.ai/ide_skills`, 200, sha256 `aabe5c78…`, text extraction 94 bytes) and contains neither
string, so there is no page under the entry's own citation that backs the international root, and the token as
written fails an exact/word-bounded match on the domestic page too.

### F2 — Zhipu row has no discovery root or placement token; its "distinctive frontmatter" mistranslates the page

```
$ sed -n '27,28p' S221.raw
* **内置**：type:zai，以 `GET /v1/skills?source=zai` 查询当前目录，不固定承诺某个名字或版本永远存在。
* **自定义**：type:custom，上传你的 SKILL.md 和所需模板/脚本。
$ sed -n '83p' S221.raw | cut -c1-140
Skill 非空时必须同时声明 agent\_toolset\_20260601；Agent 使用的 Skill 最多 20 个，目录不得重复。运行目录为 `/workspace/skills/<目录名>/`，按需读取。…
$ grep -c '项目级\|用户级\|project\|user' S221.raw
1
```

(the single hit is `用户协议` — the user agreement link, not a user scope.) The page states no project root and
no user root; it states an upload API and a runtime mount, and its `type` distinction is **built-in vs
uploaded**, not "platform from user skills". Entry line 24 writes `uploaded package` in both root columns and
`distinguishes platform from user skills`. Under the frozen predicate the row has four backticked tokens, all
keys, zero path/placement tokens → not backed regardless of how well the keys match.

### F3 — "all four now read the cross-vendor `.agents/skills/` root" is false for two of four

```
$ grep -c '\.agents' S216.raw ; grep -c '\.agents' S217.raw ; grep -c '\.agents' S221.raw
0
0
0
$ grep -c '\.agents/skills' S214.txt
3
```

TRAE documents the root (§ 使用 .agents 技能目录); Kimi documents it (S219:141, :145). CodeBuddy's IDE and CLI
pages never mention `.agents`, and the Zhipu page has no local root at all. "all four … now" is a universality
claim plus a temporal claim with no prior state cited; both fail.

### F4 — "all four separate a project scope from a user scope" is false for Zhipu

Same command as F2. TRAE documents 项目技能/全局技能 (S214.txt:75, :84, :105-108), CodeBuddy documents
`项目级 Skills` / `用户级 Skills` (S217.txt:453-454), Kimi documents Project > User > Extra > Built-in
(S219.txt:138-145). Zhipu documents none: skills are uploaded to a console library and mounted to an agent.

### F5 — TRAE's documented precedence is not a scope-precedence rule

```
$ grep -n '优先' S214.txt
203:若你在 TRAE 内创建的技能（位于 .trae/skills/ 目录）与 .agents/skills/ 中的技能重名，系统将优先调用 .trae/skills/ 目录中的技能。
```

Quote, fragment: `与 .agents/skills/ 中的技能重名，系统将优先调用 .trae/skills/ 目录中的技能` — dropped
prefix `若你在 TRAE 内创建的技能（位于 .trae/skills/ 目录）` (23 CJK chars + one space). The precedence rule
on the page is `.trae/skills/` **over `.agents/skills/`**, at the same scope; the page states no rule for a
project skill colliding with a global skill. Entry line 28 attributes the scope-precedence rule to "both TRAE
and Kimi"; Kimi's page does state it (S219.txt:138 `Kimi Code CLI 按作用域分四档扫描，越具体的作用域优先级越高：
Project > User > Extra > Built-in 。`), TRAE's does not. Also "winning **any** name collision" (line 28)
overstates a rule the page limits to `.agents/skills/`.

### F6 — the Kimi row is cited to a page that never carried it, and the two Kimi pages contradict each other

```
$ grep -c 'kimi-code' S218.raw ; grep -c 'whenToUse' S218.raw ; grep -c 'KIMI_CODE_HOME' S218.raw
0
0
0
$ curl -sL "https://api.github.com/repos/moonshotai/kimi-cli/commits?path=docs/en/customization/skills.md&per_page=10"
4335ee52f237 2026-04-24T05:22:33Z fix(skill): scope-group the skills system prompt and honor project ove…
$ curl -sL https://raw.githubusercontent.com/moonshotai/kimi-cli/4335ee52f237/docs/en/customization/skills.md -o S218-at-4335ee52.md
$ sha256sum S218-at-4335ee52.md S218.raw
5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52  S218-at-4335ee52.md
5a18c3384e8e91be4cb99570a83b62a046aeddb434d6bed403bab72592b43c52  S218.raw
$ sed -n '166,173p' S218.raw | tail -4
| `name` | … | No |
| `description` | … | No |
| `license` | License name or file reference | No |
| `compatibility` | Environment requirements, up to 500 characters | No |
```

The file has not changed since 2026-04-24 (its last commit, months before the entry's `verified-at:
2026-10-23`; today's bytes are identical to that commit's bytes), so the entry's S218 citation for the Kimi
roots and keys was wrong **at the moment it was written**, not eroded since. S218's own user roots are
`~/.kimi/skills/` → `~/.claude/skills/` → `~/.codex/skills/` (brand group) and `~/.config/agents/skills/`
(recommended) → `~/.agents/skills/` (generic group) (S218.raw:35-40, :62-65), and its frontmatter table holds
`name`, `description`, `license`, `compatibility`, `metadata` — none of `type`, `whenToUse`,
`disableModelInvocation`, `arguments`. S219 backs every token of the row. So the row's two citations disagree
in substance and the entry records neither the disagreement nor which page governs; `blob/main` also names no
revision (CORPUS.md `anchor`: "plus revision … Never a bare homepage"; Q10).

### F7 — "wave 1 established that Qwen Code reads `allowedTools`" has no lane ground and no staged source

```
$ grep -rni 'qwen' corpus | wc -l
4
$ grep -rni 'qwen' corpus
corpus/knowledge/sibling-description-rewrites-round8.md:365:… (a benchmark CSV path)
corpus/lessons/round-1-aggregator-audit.md:3:… (the aggregator's model id)
corpus/lessons/round-4-aggregator-audit.md:4:… (same)
corpus/lessons/round-67.md:103:… (`ScoutQwen` seat name)
```

No lane entry holds a Qwen Code surface. The supporting text lives in the package, in an entry the plan does
**not** stage:

```
$ grep -n -A4 'allowedTools' client-surface-census-extension.md
44: extension, then bundled. One interoperability trap is explicit: Qwen Code reads the
45: `allowedTools` frontmatter field, and an `allowed-tools` field written for another agent is
46: ignored. A skill authored for a different client can therefore be silently accepted and
47: silently mis-configured.
```

Even that source says "ignored" — a documentary statement about key names. The entry upgrades it to observed
runtime behaviour: "does not fail loudly: it loads, and its tool allowlist is silently dropped" (lines 35-37).
That is a runtime claim inferred from docs; the lane's own rule for this class is stated in `PROVINCE.md:30`
(hook files: "This is documentary evidence, not observed runtime behaviour") and Q51/Q26 require the claim to
be bounded to what is measured. "**the** clearest cross-client compatibility trap the lane now holds … only
visible when the Chinese-vendor surfaces are read side by side" (lines 37-39) is also falsified inside the
package: `client-frontmatter-and-discovery-divergence.md` already holds a three-client frontmatter-divergence
entry (S250 Deep Code, S252 Junie, S255/S256 the spec) whose own headline is that a skill "can be valid under
the specification, rejected by one client, and silently renamed by another" — the trap is visible without a
single Chinese-vendor page.

### F8 — the Japanese negative has no sweep, points at the wrong entry, and points outside the lane

```
$ sed -n '41,43p' chinese-client-skill-surfaces.md
**What is still missing.** No Japanese-*client* skill surface was found in this round.
The Japanese side of the corpus is a documentation and practice tier (see
`japanese-prompt-craft-tiers.md`), not a client tier. That is a finding, not an omission.
$ ls corpus/knowledge | grep -i japanese          # in the lane
(no output)
$ head -3 /home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/japanese-prompt-craft-tiers.md
# The Japanese tier: a prefectural government prompt collection, and an industrial maintenance loop
```

Three defects in three sentences: (i) the negative carries no sweep command (CORPUS.md: "A negative claim
carries its sweep"; Q14; Q30 for per-client negatives); (ii) the pointer names the *prompt-craft* tier entry,
which is about a Chiba prefectural prompt guideline and a METI deck — the entry that actually covers the
Japanese *client* question is `japanese-language-skill-surface-layer.md` ("The Japanese layer is documentation
and market, not client … Closed as a **negative**"); (iii) neither file exists in the lane, so the pointer is
dangling for a lane reader — the same reference-drift class the round's own frontier step names.

### F9 — the provenance trio and the located quotes do not meet the lane's admission shape

```
$ nl -ba chinese-client-skill-surfaces.md | sed -n '1,3p'
     1	
     2	# Four Chinese-vendor skill surfaces: discovery roots, frontmatter, and trigger surfaces
     3	
$ head -3 corpus/knowledge/resident-index-and-rungs-round72.md
source: S214 — Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills …
source: S215 — pi-mono — coding agent — Skills — …
source: S216 — Hermes Agent Docs — Skills — …
```

The lane's own latest entries open at `source:` and carry a `located quote "…"` per source (round-72 entry,
round-68 entry). The staged entry opens with a blank line and an H1, has **no** `located quote` for S216, S217,
S218, S219, S221, and its only two quotes (the TRAE sentence and the `启用 .agents 技能目录` label) name no
location. C1 predicate (a) says the entry "opens with `source:` lines"; (d) says "each cited row's located
quote … is found in its snapshot" — with no located quotes there is nothing for (d) to check.

```
$ nl -ba chinese-client-skill-surfaces.md | sed -n '11p'
    11	recheck: 60d — re-fetch all six pages and re-count the discovery roots and the frontmatter field names per vendor, confirming none has silently changed (ran 2026-10-23)
```

`recheck:` is prose, not a command (Q04: "every `recheck:`/source command resolves and runs today"). Contrast
the round-72 entry, whose `recheck:` is a shell loop printing `1 1 1`. And the recheck's own assertion is
already false in the sense that matters: re-running it today produces a **contradiction** between S218 and S219
(F6), which the sentence "confirming none has silently changed" cannot surface or turn red.

### F10 — counts and evaluative claims without the corpus forms

`Four Chinese vendors` (line 14), `Three patterns` (line 26), `all four` (×5, lines 26-28) are counts with no
`<number> — <command> <date>` (CORPUS.md; Q13), and the universality clauses are what F3/F4 falsify. "each is a
distinct product family, not a re-run of a held client" (lines 16-17) is market commentary with no source
(the plan's own assimilation gate excludes market commentary; `PROVINCE.md` § Core names client surface maps,
trust gates, hook files, scoped rules, command files, agent definitions — not product families). "the clearest
cross-client compatibility trap" (line 37) is an opinion that is not marked as one (CORPUS.md: "A corpus entry
is falsifiable or marked opinion").

### F11 — two source anchors name bold labels, not headings

```
$ grep -o '<h[23][^>]*id="[^"]*"' S217.raw | head -6
<h2 id="什么是-skills" …>   <h2 id="skills-vs-slash-commands" …>   <h2 id="创建-skills" …>
<h3 id="目录结构" …>        <h3 id="skill-md-格式" …>             <h3 id="frontmatter-字段" …>
$ sed -n '453,454p' S217.txt
项目级 Skills ： .codebuddy/skills/ （项目根目录下）
用户级 Skills ： ~/.codebuddy/skills/ （用户主目录下）
```

No heading with `项目级 Skills` / `用户级 Skills` exists; those are bold labels inside `# 创建 Skills → 目录结构`.
Same class on S214: `动态按需加载` and `技能 vs 规则` are bold labels (the page's h2/h3 ids are `主要特点`,
`使用场景`, `技能 vs 其他功能`, …), while `使用 .agents 技能目录` **is** an h2 (`f734fc43`). The registry
`anchor` cell must name "exact section / heading / page / line" (CORPUS.md), so two of S214's three anchors and
both of S217's need to be restated as section + line.

### F12 — the staged ids collide with live lane rows; copying the source lines unchanged cites the wrong documents

```
$ grep -nE '^\|[[:space:]]*S(214|216|217|218|219|221)[[:space:]]*\|' corpus/SOURCES.md
154:| S214 | Factory Documentation — Skills — https://docs.factory.ai/cli/configuration/skills | …
156:| S216 | Hermes Agent Docs — Skills — https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | …
```

S214 and S216 already mean Factory and Hermes in this lane; S217, S218, S219 and S221 are free. Renumber by
document (the plan's own requirement); the `source:` lines must not be carried across. This is exactly the
plan's shortcut world 1; it must score `0 of 4`, and it will — but so will the unaltered entry (F1/F2), which
means that control will not distinguish "no rows" from "unsupported tokens".

### F13 — the CJK quote and the 5–25-word rule

```
$ sed -n '55p' S214.txt | cut -c1-50
智能体不会在任务开始时一次性读取所有技能的完整内容。在执行任务前，智能体会先扫描
$ python3 -c "print(len('智能体不会在任务开始时一次性读取所有技能的完整内容'))"
25
```

The quoted sentence is 25 characters and zero space-delimited words. C1 predicate (d) requires a "located quote
(5–25 words)"; for CJK there is no stated tokenisation, so either the counter must state one (characters? a
segmenter?) or the entry must use a quote the counter can count. As written, the entry also does not say the
quote sits in the body under `主要特点 → 动态按需加载` (S214.txt:54-55) rather than in a heading or a table —
"a quote names its location" (CORPUS.md), and Q23 wants a *located* quote per attribution.

---

## 3. Rewrite list — every failing sentence and the weaker sentence the pages do support

| entry line | sentence (abridged) | defect | supported replacement | page |
|---|---|---|---|---|
| 2 | H1 "Four Chinese-vendor skill surfaces: discovery roots, frontmatter, and trigger surfaces" | "discovery roots" false for Zhipu (no local root); title precedes the provenance trio | move below the trio; retitle "Chinese-vendor skill surfaces round 73: roots, frontmatter, trigger" — no count in the title | — |
| 11 | `recheck: 60d — re-fetch all six pages and re-count … (ran 2026-10-23)` | prose, not a command (Q04); asserted run cannot fail | `recheck: 60d — \`for p in "https://docs.trae.cn/ide_skills\|.trae/skills/" … ; do printf '%s ' "$(curl -fsSL "$u" \| grep -c "$q")"; done\` — prints 1 per page` (the round-72 entry's shape) | round-72 entry |
| 12 | ground: "…the Japanese-client channel yielded nothing." | no sweep (Q14/Q30); pointer below is wrong | drop the Japanese clause from `ground:` | — |
| 14-17 | "Four Chinese vendors ship an Agent Skills surface … None of them is the Qwen Code surface already held from wave 1, and each is a distinct product family, not a re-run of a held client." | count without command; Qwen provenance absent in-lane (F7); market commentary unmarked | "Each of the four pages below (`S###`×4) documents a skill surface; the host and frontmatter they document are the table's cells." Delete the Qwen and product-family clauses, or move them to the lesson as open questions. | — |
| 21 | TRAE row: `~/.trae-cn/skills/` (domestic build), `~/.trae/skills/` (international); "ByteDance" | one token absent from every cited page; the second written with a slash the page omits; vendor attribution absent from the page (`grep -c '字节\|ByteDance' S214.raw` → 0) | `\| TRAE (S214) \| TRAE IDE \| \`.trae/skills/\` \| \`~/.trae-cn/skills\` (macOS/Linux), \`%userprofile%/.trae-cn/skills\` (Windows) \| \`name\`, \`description\`; body sections 描述/使用场景/指令/示例 \|` | S214.txt:105, :107, :108 |
| 22 | CodeBuddy row | tokens all present; anchor wrong (F11) | keep the row; restate the S217 anchor as `# 创建 Skills → 目录结构` with S217.txt:453-454 | S216.txt:68, :87-88; S217.txt:453-454, :469, :490 |
| 23 | Kimi row cited `(S218, S219)` | S218 never carried these tokens and its own table contradicts them (F6); `blob/main` unpinned | cite S219 for the row; add one sentence recording the divergence: "S218 (`@4335ee52f237`) lists `~/.kimi/skills/`, `~/.claude/skills/`, `~/.codex/skills/` and a `name`/`description`/`license`/`compatibility`/`metadata` table, and does not state the roots or keys S219 states." | S219.txt:123-127, :140-145; S218.raw:35-40, :166-173 |
| 24 | Zhipu row: "uploaded package / uploaded package"; "`type:zai` / `type:custom` distinguishes platform from user skills" | no path token → row unbacked; mistranslation | `\| Zhipu (bigmodel.cn) \| managed agents (S221) \| no local root: upload via \`POST /v1/skills\`, runtime mount \`/workspace/skills/<目录名>/\` \| — (no project/user scopes documented) \| \`name\`, \`description\` required; \`type:zai\` built-in vs \`type:custom\` uploaded \|` | S221.raw:27-28, :83 |
| 26-28 | "First, all four treat the `description` as the routing surface …" | supported — keep, but cite each vendor's line | keep; add `(S214.txt:55, S216.txt:104, S219.txt:154, S221.raw:7)` | as listed |
| 28 | "Second, all four separate a project scope from a user scope" | false for Zhipu (F4) | "Three of the four (TRAE, CodeBuddy, Kimi) separate a project scope from a user scope; Zhipu mounts an uploaded package to the agent and documents no scopes." | S214.txt:105-108; S217.txt:453-454; S219.txt:138-145; S221.raw:83 |
| 28 | "both TRAE and Kimi make the scope a *precedence* rule" | TRAE's precedence is `.trae/skills/` over `.agents/skills/` (F5) | "Kimi makes the scope a precedence rule (`Project > User > Extra > Built-in`); TRAE's documented precedence is `.trae/skills/` over a colliding `.agents/skills/` entry, at the same scope." | S219.txt:138; S214.txt:203 |
| 28 | "Third, all four now read the cross-vendor `.agents/skills/` root … with `.trae/skills/` winning any name collision" | false for CodeBuddy and Zhipu (F3); "any" overstates | "Two of the four (TRAE, Kimi) read the cross-vendor `.agents/skills/` root — TRAE behind an explicit `启用 .agents 技能目录` toggle and giving `.trae/skills/` priority over a colliding `.agents/skills/` entry, Kimi as one of two user-scope groups." | S214.txt:203, :210; S219.txt:141, :145 |
| 30-33 | Kimi's three spellings and the `disableModelInvocation` variants | supported — keep | keep; add the located quote `| whenToUse | | 触发场景描述，也接受 when-to-use 、 when_to_use 写法 |` | S219.txt:125-126 |
| 33-34 | "CodeBuddy's CLI examples emit the hyphenated `disable-model-invocation` and `allowed-tools` spellings (S217)" | supported — keep | keep | S217.txt:469, :490 |
| 34-37 | "Against this, wave 1 established that Qwen Code reads `allowedTools` and **ignores** `allowed-tools`. So a skill … does not fail loudly: it loads, and its tool allowlist is silently dropped." | no lane provenance; runtime claim from docs (F7) | Either cut, or: "Qwen Code's own page records `allowedTools` and states that an `allowed-tools` field written for another agent is ignored (package `client-surface-census-extension.md:44-47`; *not* admitted this round). What happens at load is not measured here." | package entry, lines 44-47 |
| 37-39 | "This is the clearest cross-client compatibility trap the lane now holds, and it is only visible when the Chinese-vendor surfaces are read side by side." | opinion unmarked; contradicted by the package's own divergence entry | cut | `client-frontmatter-and-discovery-divergence.md` |
| 41-43 | "No Japanese-*client* skill surface was found in this round … (see `japanese-prompt-craft-tiers.md`) … That is a finding, not an omission." | no sweep; wrong pointer; dangling in-lane (F8) | cut the paragraph. If the negative must survive, it belongs in the lesson's Gate with the round-16 sweep cited: "no Japanese-origin client was found across eight inventories (`japanese-language-skill-surface-layer.md`; sweep `japanese-client-census-round16.txt`)" — and only if that entry is co-staged | package `japanese-language-skill-surface-layer.md` |
| 4-9 | six `source:` lines | no `located quote` per source; two ids collide with live rows; S218 unpinned (F6, F9, F12) | one `source:` line per renumbered id, each ending `— located quote "…" (snapshot `S###-*.txt:<line>`)` in the round-72 shape; S218 pinned `@4335ee52f237` | round-72 entry |

---

## 4. Plan and counter attacks (C1 is the wave's claim; these are for the L1 and the counter seats)

1. **Predicate (a) vs the lane's own admission shape.** (a) requires the entry to "open with `source:` lines".
   The lane carries at least one admitted entry that opens with an H1 and no trio
   (`corpus/knowledge/frontmatter-trigger-surface.md:1-3`), and the staged entry opens with a blank line and an
   H1. Either the counter reads the trio *anywhere before the first body paragraph* (state it), or (a) is
   red on a shape the lane has historically admitted. The staged entry fails either way (F9), but the counter
   must say which file it reads.
2. **"a source that row cites" is ambiguous for multi-source rows, and the Kimi row is exactly the ambiguous
   case.** Union semantics: Kimi passes (S219). Single-snapshot semantics: Kimi fails (S218 lacks every token).
   The two cited pages genuinely disagree (F6), so no token match can decide which page governs. Smallest fix
   that keeps C1 frozen: require **one** `source:` per table row (the governing page) and move secondary pages
   to prose; then (a) is decidable and the divergence is recorded rather than hidden.
3. **Predicate (b)'s host freeze excludes the only international TRAE host.** `docs.trae.ai` is not in the
   frozen host list; since that page serves a JS shell (94 bytes of text) it could not supply a quotable
   snapshot anyway. Dropping the international-root claim (F1) is therefore the minimal path — it needs **no**
   plan erratum. Adding it would need one, before data.
4. **Predicate (a) is a conjunction a shortcut can neither meet nor miss informatively.** Because *every*
   backticked token must match, one stray token in a row silently converts a backed vendor into an unbacked
   one — the failure is invisible unless the counter prints the missing token. Recommend the counter print
   `V unbacked: missing token '<tok>'` per vendor; without it the `2 of 4` reading is indistinguishable from
   `no row` and from `host mismatch`.
5. **Control 1 will not disambiguate.** The plan's first shortcut world (staged entry copied unchanged, no
   registry rows) reads `0 of 4`; the staged entry's own content also reads `2 of 4`. Keep both readings but
   print the row count separately (`rows 4, backed 2`) so the control's expected `0` means "no rows", not
   "tokens missing".

---

## 5. Smallest safe correction (what I would land)

1. Renumber the six ids by document (F12); keep S217-S219, S221 free ids, move TRAE/CodeBuddy off S214/S216.
2. TRAE row: drop the international root entirely; transcribe `~/.trae-cn/skills` exactly (no trailing slash);
   attribute by product, not by vendor corporate name (F1).
3. Zhipu row: replace both root cells with the upload API and the `/workspace/skills/<目录名>/` mount, and
   translate `type:zai`/`type:custom` as built-in/uploaded (F2). This alone turns the row from unbacked to
   backed under (a).
4. Rewrite the three "all four" clauses as "three of four" / "two of four" with the per-vendor line citations,
   and split TRAE's collision precedence from Kimi's scope precedence (F3-F5).
5. Cite S219 as the governing Kimi page, pin S218 at `4335ee52f237`, and record the S218/S219 divergence in one
   sentence (F6).
6. Cut the Qwen runtime sentence and the "clearest trap" opinion, or bound the Qwen sentence to the
   documentary wording of the package entry it came from, marked as not admitted (F7).
7. Cut the Japanese paragraph from this entry and keep the negative in the lesson's Gate with its sweep (F8).
8. Move the provenance trio above the H1, add one `located quote` per source with its snapshot line, and make
   `recheck:` a shell loop that prints a count per page (F9, F13).

After 1-8 the entry's table should read `vendor skill surfaces backed 4 of 4` under predicate (a) as frozen,
without any plan erratum. I have not landed any of it: this seat is read-only, and the entry lives in the
package (`/home/vgpnk/Projects/shokuknow/merge/kotoba/…`), which this seat must not modify either.
