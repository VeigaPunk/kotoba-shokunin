# ExecSrcZhipu — round 73, wave 1: source opening for C1 / Zhipu

**Verdict: OPENED AND BACKED — but the staged entry cannot pass C1(a) as written, and two of its three
synthesis sentences are refuted for Zhipu by this page.** The page is a real Markdown export (not a JS
shell), fetched today: HTTP 200, 0 redirects, 7 381 B, sha256
b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618, byte-identical on a second fetch.
All four backticked tokens the staged entry attributes to it are present word-bounded; but the entry
gives Zhipu **no placement token at all**, which C1(a) requires, and it attributes to Zhipu two surface
properties this page never states (a project/user scope split, and the `.agents/skills/` root).

Notation: paths under my build directory are untracked until the L1 lands them, so they are written
without code spans — the pointer gate resolves backticked lane tokens against a revision and must not see
them. Committed paths are in code spans.

---

## F1 — Fetch evidence (contract-format)

Commands (run from
/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecSrcZhipu):

```
curl -sL --max-time 60 -A 'Mozilla/5.0' -o raw.md -w 'final_url=%{url_effective}\nhttp_status=%{http_code}\nbytes=%{size_download}\ncontent_type=%{content_type}\nredirects=%{num_redirects}\n' 'https://docs.bigmodel.cn/cn/managed-agents/skills.md'
```

Observed, exactly:

```
final_url=https://docs.bigmodel.cn/cn/managed-agents/skills.md
http_status=200
bytes=7381
content_type=text/markdown; charset=utf-8
redirects=0
```

`date -I` → `2026-10-25`. `sha256sum raw.md` →

```
b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618  raw.md
```

- **Not a JS shell.** The `.md` route serves `text/markdown` with the whole page; no auth, no cookie.
  The docs index names the same URL: `llms.txt:69` → `- [Agent Skills](https://docs.bigmodel.cn/cn/managed-agents/skills.md)`
  (llms.txt: 200, 48 470 B, sha256 93ecea71…). No extraction step was needed.
- **Rendered route (not committed)**: `https://docs.bigmodel.cn/cn/managed-agents/skills` → 200,
  187 403 B, `text/html`, sha256 69056d8b…; `<title>Agent Skills - 智谱AI开放文档</title>`. Same document,
  Mintlify shell. Deleted after hash; the `.md` is the text source.
- **Stability**: refetch 74 s later → 200, 7 381 B, same sha256, `cmp raw.md refetch.md` → `IDENTICAL`.

## F2 — Snapshot and pin

- Snapshot: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-73/w1/build/ExecSrcZhipu/snapshot.md
  — the fetched bytes verbatim (132 lines, 7 381 B, UTF-8, whitespace preserved). Export chrome is inside
  the page bytes and is kept: lines 1-3 are the docs-index banner, the last line the Mintlify credit.
- Pin: snapshot.sha256 — one `sha256sum` line. `sha256sum -c snapshot.sha256` →
  `snapshot.md: OK`.
- Provenance: provenance.txt (same directory) carries the table of the four fetches.
- Suggested lane placement (C1(c); the round-73 snapshots directory does not exist yet — `ls` → absent):
  file `S<id>-zhipu-managed-agents-skills.md`, manifest line

  ```
  b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618  S<id>-zhipu-managed-agents-skills.md
  ```

## F3 — Token inventory: everything the staged entry attributes to this page

Staged entry: /home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md
(line 9 = source line S221, line 24 = the Zhipu table row, line 28 = the three-patterns paragraph).
Counts are against snapshot.md, run in the build directory.

| token (as the entry attributes it) | entry line | `grep -c -F` | `grep -n -F` lines | edge-bounded hits | verdict |
|---|---|---|---|---|---|
| `选择内置或自定义 Skill` (heading anchor) | :9 | 1 | 25 | 1 | PRESENT — literal heading is `## 选择内置或自定义 Skill` (level 2, the entry writes `#` for all six sources) |
| `name` | :24 | 7 | 37,46,57,65,71,104,112 | 3 (37,71,104) | PRESENT — 37 = frontmatter sentence; 71/104 = code/JSON `name`; the other 4 are `display_name` |
| `description` | :24 | 1 | 37 | 1 | PRESENT |
| `type:zai` | :24 | 1 | 27 | 1 | PRESENT |
| `type:custom` | :24 | 1 | 28 | 1 | PRESENT |
| `SKILL.md` | (not in the Zhipu cell) | 4 | 28,32,37,47 | 5 occurrences | PRESENT — available if the L1 wants a sixth token |
| `/workspace/skills/<目录名>/` | **not attributed** | 1 | 83 | 1 | PRESENT — the page's only placement path; the entry omits it |
| `uploaded package` (prose, both root cells) | :24 ×2 | 0 | — | 0 | **ABSENT** as a literal; the page says 上传 (upload) but never this phrase, and gives no project/user root |
| `.agents/skills/` (synthesis, attributed to all four) | :28 | 0 (`.agents` = 0) | — | 0 | **ABSENT** |
| `~/` root form | (implied by "user roots") | 0 | — | 0 | **ABSENT** |
| `项目级` / `用户级` | (implied by "project scope / user scope") | 0 / 0 | — | 0 | **ABSENT** |
| `allowed-tools`, `allowedTools`, `whenToUse`, `disable-model-invocation`, `disableModelInvocation`, `priority` | (contrast keys, not claimed for Zhipu) | 0 each | — | 0 | ABSENT — Zhipu's frontmatter is the minimal pair |

Package row for the same page (/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:25) claims two
quotes; both are literal in the snapshot:

```
$ sed -n '7p' snapshot.md
Skill 将领域工作流程、模板和脚本打包给云端 Agent。Agent 先读名称与描述，再按任务读取正文和配套资料，不必每次把整套方法塞进 system prompt。
$ sed -n '37p' snapshot.md
SKILL.md frontmatter 写 name 和非空 description；正文说清任务流程、何时读参考文件、输出要求。一个 Skill 解决一类任务，避免宽泛触发。
```

Both claimed strings occur (line 7 and line 37 respectively). The census extension
(`client-surface-census-extension.md`) names Zhipu nowhere — `grep -c -i 'zhipu\|bigmodel'` → `0` — so it
attributes nothing to this page; there is no Qwen-side token to check here.

## F4 — What the page does NOT say that the staged entry claims (defects of the staged entry)

**D1 — no placement token → C1(a) fails as written.** C1(a) needs "at least three [tokens], at least one
root or placement token and at least two keys". The Zhipu cell has four keys (`name`, `description`,
`type:zai`, `type:custom`) and **zero** placement tokens: both root columns say `uploaded package`, which
is ABSENT from the page. The page's only placement statement is line 83:

`运行目录为 /workspace/skills/<目录名>/，按需读取`

(the path token is literally ``/workspace/skills/<目录名>/``). The renumbered entry row must carry it, or
Zhipu caps C1 at 3 of 4 no matter what else lands.

**D2 — the scope split is refuted for Zhipu.** Entry :28: "Second, all four separate a project scope from a
user scope". This page has no scope axis: `grep -c -F '项目级'` → `0`, `'用户级'` → `0`, `'~/'` → `0`. What it
has instead is a skill library (marketplace install or upload) plus a per-Agent mount — a different
structure, not a two-scope structure. The census must not carry the "all four" sentence into the lane.

**D3 — the `.agents/skills/` root is refuted for Zhipu.** Entry :28: "Third, all four now read the
cross-vendor `.agents/skills/` root". `grep -c -F '.agents'` → `0` on the whole page. Zhipu reads skills
from its own library, mounted at line 83. Three of four may read `.agents/`; the fourth does not.

**D4 — "platform from user skills" is the entry's gloss, not the page's words.** The page's terms are
内置 (`type:zai`, enumerated by `GET /v1/skills?source=zai`, line 27) and 自定义 (`type:custom`, upload your
SKILL.md plus templates/scripts, line 28); the mount table (line 79) reads `| type | zai 或 custom |`.
Substance backed; vocabulary overstated.

**D5 — the placement cell loses the page's actual mechanics.** Line 83 also fixes: at most 20 skills per
Agent, no duplicate directories, skills frozen for a Session's life (overridable only at creation via
`agent_with_overrides`), and 非空 (`SKILL.md` non-empty) is required whenever a skill is declared. The
version rules (lines 87-95) resolve `latest` at Session creation / Deployment trigger / sandbox start, and
a pinned version is what makes a run reproducible. "uploaded package / uploaded package" collapses all of
this into one word.

**D6 — "required" is an inference.** Line 37 says `SKILL.md frontmatter 写 name 和非空 description` — write
`name` and a **non-empty** `description`. Presence of `name` is stated; "required" as a validation rule is
not, and the distinguishing constraint (non-empty) is dropped by the entry.

**D7 — "explicit refusal" overstates.** The package row (SOURCES.append.md:25) says "an explicit refusal to
place skill content in the system prompt". The page says `不必每次把整套方法塞进 system prompt` — "no need to
stuff the whole method into the system prompt each time" (line 7). Policy statement yes; refusal, no.

**D8 — heading level.** The source line cites `# 选择内置或自定义 Skill`; the page has `## 选择内置或自定义 Skill`
(line 25). Uniform convention across the six sources in the entry, so not a claim defect — recorded so the
laned Gate quote does not call it byte-exact.

## F5 — Located quote for the registry row's `teaches`

Primary quote — heading `# Agent Skills`, snapshot.md line 7, literal (copied from `sed -n '7p'`):

> 先读名称与描述，再按任务读取正文和配套资料

21 characters, 1 whitespace token — inside the 5-25 bound under either the character reading or the lane's
whitespace-word reading. Dropped bytes, named: the preceding `Agent ` (the sentence's subject) and the
trailing `，不必每次把整套方法塞进 system prompt。` (the system-prompt consequence). Within one line, so it
survives C1(d)'s whitespace-collapse comparison unchanged.

Supporting file:line pointers (citations, not the quote): line 25 heading; line 27 `type:zai` + `GET
/v1/skills?source=zai`; line 28 `type:custom` + "上传你的 SKILL.md 和所需模板/脚本"; line 37 the frontmatter
sentence; line 79 the mount `type` table; line 83 the runtime path.

One-sentence `teaches` this grounds: *a cloud skill is an uploaded, versioned package of SKILL.md plus
templates and scripts whose name and non-empty description are read first while the body loads per task
from `/workspace/skills/<目录名>/`; `type:zai` is a built-in skill and `type:custom` an uploaded one; the page
names no project or user filesystem root.*

## F6 — Draft registry row (11 columns) and its check

Written byte-identically to row.draft.md in the build directory:

| S<<id>> | 智谱 AI 开放文档 — Managed Agents — Agent Skills — https://docs.bigmodel.cn/cn/managed-agents/skills.md | docs | B | Zhipu's managed-agents skill surface: how a cloud Skill is packaged, uploaded, versioned and mounted per Agent, and how built-in and custom skills are selected (one vendor's product documentation; no local harness is measured) | `# Agent Skills` (snapshot.md:7), `## 选择内置或自定义 Skill` (snapshot.md:25-28, mount `type` table :79), `## 挂载到 Agent` (runtime dir snapshot.md:83); fetched as https://docs.bigmodel.cn/cn/managed-agents/skills.md (200, 7381 B, sha256 `b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618`, text/markdown, 0 redirects, refetch byte-identical) on 2026-10-25; quote "先读名称与描述，再按任务读取正文和配套资料" (21 chars; dropped: the preceding "Agent " and the trailing "，不必每次把整套方法塞进 system prompt。") | a cloud skill is an uploaded, versioned package of SKILL.md plus templates and scripts whose name and non-empty description are read first while the body loads per task from `/workspace/skills/<目录名>/`; `type:zai` is a built-in skill listed by `GET /v1/skills?source=zai` and `type:custom` an uploaded one; the page names no project or user filesystem root | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |

Check, observed:

```
$ gawk -F'|' '/^\| S<<id>> \|/{printf "NF=%d cells=%d pipes=%d\n", NF, NF-2, NF-1}' row.draft.md
NF=13 cells=11 pipes=12
```

Cell-by-cell (gawk substr, first 70 chars each) confirms cells 1-11 as id / source / docs / B / scope /
anchor / teaches / mined / 2026-10-25 / 90d / corpus/knowledge/chinese-vendor-skill-surfaces-round73.md.
No `|` inside any cell — 12 pipes total.

Census expectations when the L1 lands it: `S<<id>>` is a placeholder, so `scripts/sources-census.sh
validate` will report **E02** (id not `S[0-9]{3,}`) until renumbering; E01 must not fire (NF=13). No W04:
`grep -c 'docs.bigmodel.cn' corpus/SOURCES.md` → `0`, so the URL is unique in the lane. Tier B follows the
lane's own precedent — S214 (Factory), S215 (pi-mono), S216 (Hermes) are all vendor docs at B; A is
reserved for the open format's maintainers.

## F7 — Attacks on the frozen plan / counter, from this page

**A1 — a naive word-boundary test reports the page's only placement path ABSENT.** C1(a) says tokens must
"occur word-bounded". For a token that begins with a non-word character (`/workspace/...`), Python's `\b`
requires a word character on the inside edge, so `\b/workspace/skills/<目录名>/\b` never matches text where
the token is preceded by a space. Demonstrated on the snapshot:

```
$ python3 - <<'PY'   (abridged)
tok='/workspace/skills/<目录名>/'
print('naive \\b:', bool(re.search(r'\b'+re.escape(tok)+r'\b',t)))
print('edge-class:', bool(re.search(r'(?<![A-Za-z0-9_])'+re.escape(tok)+r'(?![A-Za-z0-9_])',t)))
PY
naive \b: False
edge-class: True
```

Observed counts under the edge-class rule: `name 3, description 1, type:zai 1, type:custom 1, SKILL.md 5`.
If the C1 counter implements `\b<token>\b`, every path token becomes unfindable and Zhipu (and every vendor
whose only placement token is a path) reads as unbacked — the counter would be measuring its regex, not the
page. Fix before data (Q28): use the edge-class form, or word-bound only tokens whose first and last
characters are word characters.

**A2 — the C1 margin for this vendor is zero, and it is reachable.** C1 lowers the target only if the
pre-data census cannot reach 4. For Zhipu the live page backs six tokens including one placement path and
four keys, so N = 4 is achievable *for this vendor provided D1 is repaired in the entry*. The census must
therefore record Zhipu as reachable **with a correction**, not as-is: as staged, this vendor scores 0
placement tokens.

**A3 — C1(c) has no directory to point at yet.** A listing of the round-73 snapshots directory → absent. Until the L1
creates the directory and `MANIFEST.sha256`, the counter's own rule returns exit 2 for every cited row —
that is by design, but the base "0 of 4" receipt must be re-taken after the directory exists, not before,
or the do-nothing figure will be indistinguishable from a missing-manifest error.

**A4 — C1(d) is safe for this page.** The quote is inside one physical line and contains no whitespace run,
so whitespace collapse is a no-op; no shaping was applied to produce it.

## F8 — Cleanup, bounds, risks

- No `mktemp` scratch directory was created; no lane gate was run; no git or jj write; no process started
  beyond short-lived `curl`/`grep`/`python3` (each well under the 120 s cap). No tool was installed.
- Deleted after hashing: raw.md, refetch.md (identical refetches), page.html (187 KB shell render),
  llms.txt (48 KB index; only its line 69 is evidence and it is quoted above).
- Kept in the build directory: snapshot.md (7 381 B), snapshot.sha256 (78 B), provenance.txt (2 486 B),
  row.draft.md (1 897 B).
- **Risk 1:** the entry's staged `retrieved 2026-10-23` proves nothing for this lane (addendum §10); this
  report's own fetch is the only access evidence, and the date in the row is today's.
- **Risk 2:** the row's snapshot pin will not match until the L1 copies snapshot.md under
  the round-73 snapshots directory with the exact filename recorded in the manifest; copying and renaming
  is hash-neutral, editing is not.
- **Risk 3:** if the L1 lands the entry with the staged Zhipu row unchanged (D1), C1 cannot reach 4 of 4;
  the counter would then be correct and the claim would be false — the fix belongs in the entry, not the
  predicate.
