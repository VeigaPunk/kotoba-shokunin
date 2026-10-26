# ExecSrcTrae — C1 source opening: TRAE (ByteDance), round 73 wave 1

**Verdict.** The TRAE page is genuinely openable today, is server-rendered (not a JS shell) and has a
first-party markdown twin (`/ide_skills.md`, 13,351 B) which I pinned as the snapshot. The page **does**
hold the project root `.trae/skills/`, the per-user root `~/.trae-cn/skills`, the `启用 .agents 技能目录`
toggle and the name-collision precedence; it **does not** hold `~/.trae/skills/` (the staged entry's
"international" root), never names ByteDance, and three of the staged entry's four section anchors name a
heading level that does not exist (one names a bold list item that is not a heading at all). One registry
row drafted, 11 cells / `NF=13` verified. Nothing in the lane was modified; scratch removed.

Snapshot: `.ufo/waves/round-73/w1/build/ExecSrcTrae/snapshot.md` (13,351 B, 233 lines) +
`snapshot.sha256` (`3126996917f9e14f81beec94c98f4fc19c6f52819a94776a1b3912ac314aa28b  snapshot.md`).
Raw command/output log: `.../ExecSrcTrae/fetch.log`.

---

## F1 — fetch record (step 1)

```
$ date -I
2026-10-25
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o trae.html \
    -w 'HTTP=%{http_code}\nFINAL_URL=%{url_effective}\nBYTES=%{size_download}\nCT=%{content_type}\n' \
    'https://docs.trae.cn/ide_skills'
HTTP=200
FINAL_URL=https://docs.trae.cn/ide_skills
BYTES=112444
CT=text/html; charset=UTF-8
$ sha256sum trae.html
62cacecddd30a8016ea693baebc4600c79955487174c377e47760ebd5813f3f3  trae.html
```

No redirect. Server-rendered: the body sits in `<div class="topic-markdown" data-topic-doc-content="true">`
at char offset 37397 and `<title …>技能（Skill）</title>` is in the served bytes.

## F2 — the real text source is the site's own markdown export (step 1)

The HTML is not a shell, but the site also publishes its own raw text, which is what I pinned:

```
$ curl -sL --max-time 40 -A 'Mozilla/5.0' -o /dev/null -w 'HTTP=%{http_code} BYTES=%{size_download} CT=%{content_type} FINAL=%{url_effective}\n' \
    'https://docs.trae.cn/ide_skills.md'
HTTP=200 BYTES=13351 CT=text/markdown; charset=utf-8 FINAL=https://docs.trae.cn/ide_skills.md
$ sha256sum trae.md
3126996917f9e14f81beec94c98f4fc19c6f52819a94776a1b3912ac314aa28b  trae.md
$ wc -lc trae.md
233 13351
```

How I found it, in the page's own words — line 1 of the export: `> Fetch the complete documentation index
at: https://docs.trae.cn/llms.txt`; and the probe `/ide_skills/index.md` returns the same 13,351 B
(HTTP 200), while `?format=md` returns the HTML route again (HTTP 200, 112,475 B, `text/html`).

Fidelity, so the pin is defensible: 118 of the 127 non-table markdown lines occur verbatim
(whitespace-collapsed) inside the tag-stripped HTML body; the 9 exceptions are markdown image syntax (4),
`:::tip` container markers (2) and inline links (3) — markup, not differing text.

## F3 — snapshot (step 2)

```
$ cp trae.md snapshot.md && sha256sum snapshot.md > snapshot.sha256
$ cmp trae.md snapshot.md   # identical — verbatim bytes, no header added
3126996917f9e14f81beec94c98f4fc19c6f52819a94776a1b3912ac314aa28b  snapshot.md
```

Verbatim on purpose: a header would break both `sha256 = fetched bytes` and the predicate-(d) "found after
whitespace collapse" check for any quote that starts at line 1.

## F4 — token audit of what the staged entry attributes to this page (step 3)

Source audited: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md`,
TRAE row + the three pattern paragraphs. `grep -c -F` against `snapshot.md`:

| staged token | `grep -c -F` | snapshot lines |
|---|---|---|
| `.trae/skills/` | 3 | 76, 158, 214 |
| `~/.trae-cn/skills/` (with trailing slash) | **0 → ABSENT** | page has it without the slash at 78 |
| `~/.trae-cn/skills` | 1 | 78 |
| `~/.trae/skills/` (international) | **0 → ABSENT** | — |
| `~/.trae/skills` | **0 → ABSENT** | — |
| `%userprofile%/.trae-cn/skills` (page has it; entry omits it) | 1 | 79 |
| `.agents/skills/` | 7 | 210, 214, 216, 218, 222, 224, 228 |
| `启用 .agents 技能目录` | 1 | 226 |
| `动态按需加载` | 1 | 15 (a bold list item, not a heading) |
| `智能体不会在任务开始时一次性读取所有技能的完整内容` | 1 | 16 |
| `SKILL.md` | 9 | 5, 14, 58, 62, 81, 83, 123, 154, 158 |
| `` `name` `` (backticked, as the entry writes it) | **0 → ABSENT** | page writes the YAML key `name:` at 87 |
| `` `description` `` (backticked) | **0 → ABSENT** | page writes `description:` at 88 |
| `ByteDance` | **0 → ABSENT** | — |
| `字节跳动` | **0 → ABSENT** | — |
| `allowed-tools`, `whenToUse` | 0 → ABSENT | correctly attributed to CodeBuddy/Kimi, not to TRAE |

Exact bytes for the two root lines:

```
$ sed -n '76p' snapshot.md
* **项目技能**：项目所在路径下的 `.trae/skills/` 目录。
$ sed -n '78p' snapshot.md
   * macOS/Linux：本地根目录 `~/.trae-cn/skills`。
$ sed -n '79p' snapshot.md
   * Windows：本地根目录 `%userprofile%/.trae-cn/skills`。
```

## F5 — the stage entry's anchors name heading levels that do not exist

```
$ grep -n '^#' snapshot.md
7:## 了解 TRAE 中的技能 {#d9db28cb}
208:## 使用 .agents 技能目录 {#f734fc43}
212:### **注意事项** {#ac147835}
$ sed -n '15p;33p' snapshot.md
* **动态按需加载**
* **技能 vs 规则**
```

- `# 动态按需加载` — **not a heading**; line 15 is a bold list item. The entry's anchor names a
  heading that does not exist.
- `# 技能 vs 规则` — **not a heading**; line 33 is a bold list item under `### 技能 vs 其他功能`
  (line 30). Second anchor naming a non-heading.
- `# 了解 TRAE 中的技能` — exists at **`##`**, not `#` (line 7).
- `# 使用 .agents 技能目录` — exists at **`##`**, not `#` (line 208).

Four cited anchors, four wrong levels, two of them not headings at all. The counter's rule "at least one
root or placement token" would pass anyway, but the entry's Gate block would be citing anchors a reader
cannot land on — exactly the defect class S018 records for S001 ("the page has no 'Skill metadata table'
heading").

## F6 — the frontmatter and body shape: supported, with a shaping caveat

```
$ sed -n '83,89p' snapshot.md
`SKILL.md` 文件的格式如下：

```Markdown
---
name: 技能名称
description: 简要描述这个技能的功能和使用场景
$ grep -n -E '^## (描述|使用场景|指令|示例)' snapshot.md
94:## 描述
97:## 使用场景
100:## 指令
103:## 示例（可选）
```

The entry's "the canonical body shape is 描述 / 使用场景 / 指令 / 示例" is real, but two shaping notes:
the four are `##` headings **inside a fenced `Markdown` example block** (lines 92-104), not the page's own
sections; and the fourth is `示例（可选）` — optional in the page, unmarked in the entry. The entry's
"`name`, `description` only" is an inference from a two-key example: the page says `格式如下` and never
states exclusivity, and it writes the keys as bare YAML keys, never backticked.

## F7 — the vendor attribution is the entry's own

`ByteDance` 0, `字节跳动` 0, `ICP备` 0, no `og:site_name`, no `<link rel=canonical>`. What the page does
carry is its own title `技能（Skill）` and its own product framing (`TRAE 提供以下内置技能`). So the page is
TRAE's own documentation of TRAE — a maintainer statement about the product — but the vendor name is not
on the page and must not be presented as page-sourced.

## F8 — `~/.trae/skills/` is not on this page, and the sibling domain cannot supply it

```
$ curl ... 'https://docs.trae.ai/ide_skills'     -> HTTP=200 BYTES=1913042 FINAL=https://docs.trae.ai/ide/traework-to-traecode-data-migration?_lang=en
$ curl ... 'https://docs.trae.ai/ide_skills.md'  -> HTTP=200 BYTES=1913042 FINAL=(same)
$ curl ... 'https://docs.trae.ai/llms.txt'       -> HTTP=200 BYTES=1913042 FINAL=(same)
$ md5sum the three fetched files
816c16198a0c473726ef509e8d725036  (all three identical)
```

All three are one 1,913,042 B document: `<title>Important update: TraeCode and TraeWork is merged into the
all-new TRAE - Documentation - TRAE</title>` — a soft redirect to a migration notice, not the skills page.
`~/.trae/skills` and `~/.trae-cn` occur 0 times in it. Conclusion: the entry's "`~/.trae/skills/`
(international)" root is **unsupported by every page I could reach**; it is either stale (the international
docs are mid-migration to a merged product) or was inferred from the domestic root. It must be dropped from
the vendor row, not carried as fact.

## F9 — what the page holds that the staged entry drops

- The **Windows** global root: `%userprofile%/.trae-cn/skills` (line 79). The entry lists two user roots,
  one of them nonexistent, and omits the one real second form.
- `find-skills` / the `skills` CLI as the install path into `.agents/skills/` (lines 216-220), and the
  `agentskills.io` specification as the `.agents` root's authority (line 210) — i.e. TRAE is reading the open
  cross-vendor convention, which is the interesting cross-client fact and is not in the entry.
- `应用到全局` — a project skill can be promoted to a global one from the skill panel (line 194), i.e. the
  scope is not fixed at creation.
- The four built-in skills (lines 107-115) and the plugin-market install route (lines 161-173).

---

## Step 4 — the located quote (≤25 words)

`sed -n '214p' snapshot.md` (verbatim, nothing dropped):

> 若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 `.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` 目录中的技能。

Location: § 使用 .agents 技能目录 → ### 注意事项, `snapshot.md:214`.
Measured: **9 whitespace tokens, 33 CJK characters**, 0 bytes dropped. Found verbatim after whitespace
collapse only (`quote in re.sub(r'\s+',' ',snapshot)` → `True`).

## Step 5 — the registry row (11 cells, `NF=13` verified)

```
| S<<id>> | TRAE docs — 技能（Skill） — https://docs.trae.cn/ide_skills | docs | A | TRAE IDE's skill discovery roots, the `.agents/skills/` cross-vendor toggle and the name-collision precedence between them (client skill surface; the product's own documentation, and the page never names its vendor) | § 使用 .agents 技能目录 → § 注意事项, `snapshot.md:214` (roots at `:76`, `:78`, `:79`); quote "若你在 TRAE 内创建的技能（位于 `.trae/skills/` 目录）与 `.agents/skills/` 中的技能重名，系统将优先调用 `.trae/skills/` 目录中的技能。" (9 whitespace tokens, 33 CJK chars); fetched as https://docs.trae.cn/ide_skills.md (200, 13,351 B, sha256 `3126996917f9…`) on 2026-10-25 | A same-name skill created in `.trae/skills/` wins over the `.agents/skills/` copy, so the cross-vendor root is read but never overrides the vendor root, and the per-user global root is `~/.trae-cn/skills` (Windows `%userprofile%/.trae-cn/skills`) | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |
```

```
$ awk -F'|' '{print "line " NR ": NF=" NF}' row.md
line 1: NF=13
$ awk -F'|' 'NF!=13{print "FAIL NF="NF; bad=1} END{if(!bad) print "PASS: NF=13 -> 11 cells"}' row.md
PASS: NF=13 -> 11 cells
```

Tier `A`: the page is the product's own statement about where its own client looks (lane precedent —
S022 Claude Code docs, S024 opencode docs, S025 VS Code docs are all `A`). If the L1 prefers to read
"maintainer's own statement" narrowly as a spec, drop to `B`; nothing else in the row changes.
`kind` `docs`. Draft also saved at `.../ExecSrcTrae/row.md`.

---

## Plan / counter attacks (before data)

**A1 — predicate (d)'s "5–25 words" is undefined for Chinese.** The natural quote for the 动态按需加载
passage (line 16) measures **3 whitespace tokens / 112 CJK chars**: a counter counting whitespace tokens
scores the correct quote *too short*, a counter counting CJK characters scores most whole sentences *too
long*. The unit must be frozen in the counter docstring before data, like Q65. My row's quote was chosen to
survive a whitespace-token count (9) *and* a 5-word floor; the counter should print both figures per quote.

**A2 — predicate (a)'s "word-bounded" is undefined against backticks and ASCII `\b`.** In the snapshot every
path token is delimited by backticks (`` `.trae/skills/` ``), and `name:` is delimited by line start and a
colon. Python's `\b` requires a word character on one side, so `\b\.trae\b`-style matching reports ABSENT for
every path token — the counter would be red for the wrong reason and a shortcut world (invented root) would
be indistinguishable from an honest one. Freeze the rule as `(?<![0-9A-Za-z_])<token>(?![0-9A-Za-z_])` (what
the lane's own counters use) or normalize backticks away before matching, and show one red case.

**A3 — predicate (a)'s "at least two keys" collides with how the page writes keys.** The page presents `name`
and `description` as YAML keys inside a fenced example (lines 87-88). `` `name` ``/`` `description` `` backticked
occur **0** times. Unless the frozen rule says "the key with or without backticks and with or without its
trailing colon", the honest TRAE row fails (a) on a page that plainly has both keys. This must be written
into the counter before any seat scores data.

**A4 — do not extend the token check to registry cells.** Lane rows backtick pointers and hash fragments
(`snapshot.md:214`, `:76`, `3126996917f9…`); a row-level literal token check reports 0 for those and would
fail honest rows. Predicate (a) as frozen applies the token check to the entry's vendor-table row only —
keep it there explicitly, since the registry row is what a later wave will hand the counter.

**A5 — the snapshot pin must name the route.** `docs.trae.cn` serves two non-identical bodies for this page
(HTML 112,444 B / sha256 `62cacecd…`; markdown 13,351 B / sha256 `3126996917…`). Pin the `.md` route in
`snapshots/MANIFEST.sha256` (as S018/S021/S024 do) or the same page yields two hashes and predicate (c)
fails on a re-fetch. My snapshot has no added header, so `sha256(snapshot.md) == sha256(fetched .md)` and
re-fetch equality is checkable byte-for-byte.

**A6 — shortcut control to add for C1 (currently missing from the plan's list).** "a root path invented and
absent from the snapshot" is listed, but nothing exercises the *vendor-attribution* case that this page
actually has: a row whose backticked tokens all occur while its `source`/`scope` asserts a vendor name the
page never states (`ByteDance` = 0). That world should still score bounded — a counter that passes it is
not checking the citation, only the token bag. Suggested added world: the honest TRAE row with `~/.trae/skills/`
substituted for `~/.trae-cn/skills` (one ABSENT root) must score below 4.

## Constraints observed

- Lane tree untouched: only `.ufo/waves/round-73/w1/build/ExecSrcTrae/` (snapshot.md, snapshot.sha256,
  fetch.log, row.md) and this report were written. No git/jj write, no pacman, no installs.
- Scratch `/tmp/k73w1-ExecSrcTrae.IsGj` deleted before return.
- No lane gate run (wave 1 is in flight; the L1 owns the post-integration gate).

## Blockers

None. One open decision for the L1 only: tier `A` vs `B` for F7's reason, and A1-A3 must be written into
`check_cn_vendor_surfaces.py` before freeze 2.
