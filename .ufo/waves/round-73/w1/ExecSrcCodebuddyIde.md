# ExecSrcCodebuddyIde — C1 source opening: CodeBuddy IDE Skills (S216 slot)

## Verdict

The page opens clean at `https://www.codebuddy.ai/docs/zh/ide/Features/Skills`, HTTP 200, no redirect,
36633 B, server-rendered (not a JS shell), and it carries three of the four backticked tokens the staged
entry attributes to it — `.codebuddy/skills/` (placement), `name`, `description` — plus `allowed-tools`
and `disable` as optional keys and the heading `渐进式披露设计原则`. It therefore **can** back a CodeBuddy
row under C1(a)'s token rule.

Two tokens the staged entry rests on are **ABSENT** from this page: `~/.codebuddy/skills/` (the user root
the entry's Tencent cell puts beside the project root, present on the CLI page S217 per the peer who owns
that page — not re-opened by me) and `.agents/skills/` (the entry's "all four now read the cross-vendor
`.agents/skills/` root", which has no Tencent page behind it on either S216 or, per the peer, S217). The
first is a citation-precision defect — one cell must name S217 for the user root; the second is a missing
source for a four-vendor claim.

One plan defect, independent of this page's content: C1 predicate **(a)** as frozen cannot be satisfied by
any placement token of the form `.dir/` or `~/…/`, because a both-sides `\b` regex never matches a token
that begins with `.` or `~` and ends with `/`. Measured below (`word-bounded=0`, `literal=2`). The same
clause is also too loose on keys — it counts `name` inside `skill-name/` on this page and would count
`disable` inside `disable-model-invocation`. Both readings must be fixed before any claim data (Q28) or C1
is unsatisfiable for honest rows and forgeable for stuffed ones.

## 1. Fetch record

```
$ date -I
2026-10-25
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -w '\n---HTTP:%{http_code}---\nFINALURL:%{url_effective}\nBYTES:%{size_download}\n' -o page.html 'https://www.codebuddy.ai/docs/zh/ide/Features/Skills'
---HTTP:200---
FINALURL:https://www.codebuddy.ai/docs/zh/ide/Features/Skills
BYTES:36633
$ sha256sum page.html
35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6  page.html
$ file page.html
HTML document, Unicode text, UTF-8 text, with very long lines (23642)
```

Final URL after redirects is identical to the requested URL; the served bytes carry
`<link rel="canonical" href="https://www.codebuddy.ai/docs/zh/ide/Features/Skills">`.

Not a JS shell — the body is in the served bytes (VitePress SSR, single `<main>` at byte offset 25848):

```
probe 'Skill 应建立在工作区的'      -> 1 occurrence in raw HTML
probe '.codebuddy/skills/'          -> 2 occurrences in raw HTML
probe '渐进式披露设计原则'          -> 4 occurrences in raw HTML (heading text + self-anchor id/href + content)
probe 'allowed-tools'               -> 1 occurrence in raw HTML
```

No raw/markdown export was needed, and none is advertised: the whole document is in `<main>` in the fetched
bytes, so no sitemap, API or GitHub source had to be found.

Record: `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/fetch-record.txt`.

## 2. Snapshot

| file | size | sha256 |
|---|---|---|
| `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/snapshot.md` | 3887 B, 101 lines | `a8aa1e094eb638f3437c12aab9f9d7608739836132ad0a9a7c8e427562213453` |
| `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/snapshot.sha256` | 78 B | line `a8aa1e09…  snapshot.md` |

```
$ sha256sum snapshot.md > snapshot.sha256 && cat snapshot.sha256
a8aa1e094eb638f3437c12aab9f9d7608739836132ad0a9a7c8e427562213453  snapshot.md
```

Extraction: `<main>` only, block tags → newlines, inline tags stripped, entities unescaped, `\u200b`
removed, empty runs collapsed, internal whitespace preserved. Headings keep their level (`#`…`####`),
list items keep a `- ` prefix, fenced blocks keep their inner text. Under the 300 KB cap.

Document skeleton (line numbers are snapshot lines, used by every pointer below):

```
12:## Skill 的结构
29:### SKILL.md (必需)
48:### 打包资源 (可选)
70:## 渐进式披露设计原则
78:## 创建 Skill 的流程
88:## 最佳实践
95:## Skill 管理
```

The staged entry's S216 source line names the headings `# Skill 的结构` and `# 渐进式披露设计原则`;
both exist, at snapshot lines 12 and 70 (rendered as `##`, the page's H2 level under the H1 `# Skills`).

## 3. Token audit — every backticked token the staged entry attributes to this page

Staged entry: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md`.
Its Tencent table cell reads, verbatim: `` `.codebuddy/skills/` `` | `` `~/.codebuddy/skills/` `` |
"`name`, `description` required; `allowed-tools`, `disable` optional; CLI examples also use
`disable-model-invocation`", cited `(S216, S217)`. The entry's third shared pattern adds the
`.agents/skills/` root for all four vendors including Tencent.

```
$ for t in '.codebuddy/skills/' '~/.codebuddy/skills/' 'name' 'description' 'allowed-tools' \
           'disable' 'disable-model-invocation' '渐进式披露设计原则' 'frontmatter'; do
    printf '%-32s %s  lines: %s\n' "$t" "$(grep -c -F -- "$t" snapshot.md)" \
      "$(grep -n -F -- "$t" snapshot.md | cut -d: -f1 | tr '\n' ',')"; done
```

| token | `grep -c -F` | snapshot lines | verdict | what the line says |
|---|---|---|---|---|
| `.codebuddy/skills/` | 2 | 14, 82 | **PRESENT** | line 14 `Skill 应建立在工作区的 .codebuddy/skills/ 目录下。`; line 82 `- 创建目录：在 .codebuddy/skills/ 下创建新的 Skill 目录。` — both project/workspace scope |
| `~/.codebuddy/skills/` | 0 | — | **ABSENT** | the page states no user-scope path at all (see §3.1) |
| `name` | 4 | 17, 20, 32, 37 | **PRESENT** (3 real, 1 false) | line 20 `│   │   ├── name: (必需)`; line 32 the routing sentence; line 37 the YAML example. Line 17 is `skill-name/` in the tree block — the key, not a substring of the directory placeholder (see §5: a `\b` match counts it, a proper boundary does not) |
| `description` | 4 | 21, 32, 38, 90 | **PRESENT** | line 21 `│   │   └── description: (必需)`; line 90 最佳实践 `在 description 中清楚地说明 Skill 何时应该被使用。` |
| `allowed-tools` | 1 | 39 | **PRESENT** | `allowed-tools: # 可选，指定允许使用的工具` |
| `disable` | 1 | 40 | **PRESENT** | `disable: false # 可选，是否禁用` |
| `disable-model-invocation` | 0 | — | **ABSENT** | not on this page; the entry scopes it to "CLI examples" (S217), so absence here is not a misattribution |
| `渐进式披露设计原则` | 1 | 70 | **PRESENT** | `## 渐进式披露设计原则` |

So the entry's "required" reading is genuinely S216's, and S216-only: the tree block marks both keys 必需
(lines 20-21), while the optional pair is marked `# 可选` on the same code sample (lines 39-40). This
corroborates the peer reading of the CLI page (S217 marks fields optional and defaults `name` to the
directory name) — reported by `ExecSrcCodebuddyCli`, not taken on trust: I re-measured my own page.

The hyphenated `allowed-tools` spelling the entry credits to "CLI examples" is already on **this** page
(line 39), so the entry under-credits S216 for it.

### 3.1 The user root and the `.agents` root are absent from *this* page, definitively

```
$ python3 - page.html   # regex over the raw served bytes
tilde-codebuddy  occurrences=0 []
Users-form       occurrences=0 []
home-form        occurrences=0 []
agents-root      occurrences=0 []
user-skills-zh   occurrences=1 ['用户级别']
project-skills   occurrences=1 ['Project Skills']
global-root      occurrences=0 []
```

The page mentions user scope **only as a settings-UI category**, with no path:

```
100:- 集中管理：查看和管理当前项目（Project Skills）和用户级别（User Skills）的所有 Skills。
```

and `grep -c -F '.agents' snapshot.md` → `0`.

Consequences for the staged entry, with the correction the peer's answer forced:

1. **`~/.codebuddy/skills/` is absent from S216 but not unsourced — it is S217-only.** The entry writes the
   two roots in one Tencent cell cited `(S216, S217)`, so a reader who opens the page named first cannot
   find the user root. This is a citation-precision defect, not a fabricated token: `ExecSrcCodebuddyCli`
   reports the token on their own S217 snapshot at two lines, and I have **not** opened S217 myself, so the
   correction is recorded as peer evidence and should be re-opened by a wave-2 seat before the entry lands.
   The fix is one cell edit: split the cell's citation so the project root names S216 and the user root
   names S217.

2. **"all four now read the cross-vendor `.agents/skills/` root" has no Tencent page behind it at all.**
   The entry states it as one of three patterns shared by all four vendors. It is absent from S216 (my
   measurement above) and `ExecSrcCodebuddyCli` reports 0 occurrences on S217 as well, so this is not the
   citation-precision problem of item 1: on the two pages the entry cites for Tencent, the pattern has no
   support. Either a third Tencent source is named or the sentence becomes a three-vendor claim. Flagged
   for wave 2 to re-open S217 independently before the entry lands.

3. **No precedence statement.** The entry says "both TRAE and Kimi make the scope a *precedence* rule rather
   than just a label", implying CodeBuddy does not. On this page that implication holds — precedent-free:

```
$ grep -n -E '优先级|优先|覆盖|冲突|precedence' snapshot.md ; echo "exit=$?"
exit=1          (zero lines)
```

## 4. Located quote and the row it grounds

**Quote** — heading `### SKILL.md (必需)` (snapshot line 29), sentence at snapshot line 32:

```
元数据 (YAML Frontmatter):name 和 description 决定了 AI 何时会使用这个 Skill。
```

20 words by the count stated in the anchor cell (14 CJK characters + 6 latin tokens; 14 under a CJK-run
reading). Dropped from the same snapshot line, named: the following sentence
`描述需具体说明 Skill 的功能和使用场景。` — nothing else on the line was dropped.

Whitespace-collapse check (C1 predicate (d) style):

```
$ python3 -c "... norm=lambda x: re.sub(r'\s+',' ',x).strip() ..."
collapsed found: True | raw found: True
```

**Row** — `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/registry-row.md`, fleet 11-column schema,
`S<<id>>` placeholder (the lane's `S216` is already a Hermes row, `corpus/SOURCES.md:156`):

```
| S<<id>> | CodeBuddy IDE Docs — Skills (腾讯云代码助手 CodeBuddy) — https://www.codebuddy.ai/docs/zh/ide/Features/Skills | docs | A | CodeBuddy IDE's own normative statement of its skill frontmatter (name and description required, allowed-tools and disable optional) and of where a project skill sits (the workspace's .codebuddy/skills/); one client's own documentation of its own schema, no claim about any other client | the "SKILL.md (必需)" subsection (heading snapshot line 29, sentence line 32); quote "元数据 (YAML Frontmatter):name 和 description 决定了 AI 何时会使用这个 Skill。" (20 words counting 14 CJK characters and 6 latin tokens; dropped from the same snapshot line: the following sentence 描述需具体说明 Skill 的功能和使用场景。); access 2026-10-25 HTTP 200, final URL unchanged after redirects, 36633 B, sha256 35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6, snapshot a8aa1e094eb638f3437c12aab9f9d7608739836132ad0a9a7c8e427562213453 | in CodeBuddy IDE the frontmatter name and description alone decide when the agent uses a skill, so the description is the routing surface and a body is loaded only after it matches | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |
```

Parse check:

```
$ awk -F'|' '{printf "line %d NF=%d %s\n", NR, NF, (NF==13?"OK":"BAD")}' registry-row.md
line 1 NF=13 OK
$ awk -F'|' 'NF!=13{print "BAD"}' registry-row.md | wc -l
0
```

No `|` appears inside any cell (NF=13 exactly, single line). Header row + separator must be supplied by the
L1 at landing; this file holds the data row alone.

**Tier A, and why.** The seat brief says tier B unless the page is the maintainer's own statement. This is
Tencent's own documentation of its own product, and it states the schema normatively (`name: (必需)`,
`description: (必需)` at snapshot lines 20-21), which is the same class the lane already ranks A for a
client's own normative rule (`corpus/SOURCES.md:144` Roo Code docs, `:145` Amp docs) while ranking
descriptive vendor overviews B (`:154` Factory, `:156` Hermes). If the L1 prefers Tencent internally
consistent with the CLI page's tier, B is also admitted by C1(b); the counter accepts both.

**C1(a) token sufficiency.** The row's vendor cell must carry ≥3 backticked tokens, ≥1 root/placement and
≥2 keys. This page backs `.codebuddy/skills/` (placement) + `name` + `description` (keys), with
`allowed-tools` and `disable` spare — so the cell is satisfiable from committed bytes alone.

## 5. Plan attack — C1(a)'s "word-bounded" clause is unsatisfiable for placement tokens

Frozen text, `plans/round-73.md` § C1(a): the row's backticked tokens "each occur **word-bounded** in the
committed page snapshot of a source that row cites".

Measured on the snapshot this row would pin:

```
$ python3 - <<'EOF'
import re; s=open('snapshot.md').read()
for t in [...]: print(t, len(re.findall(r'\b'+re.escape(t)+r'\b', s)), s.count(t))
EOF
.codebuddy/skills/           word-bounded=0  literal=2
~/.codebuddy/skills/         word-bounded=0  literal=0
allowed-tools                word-bounded=1  literal=1
disable                      word-bounded=1  literal=1
name                         word-bounded=4  literal=4
description                  word-bounded=4  literal=4
渐进式披露设计原则                    word-bounded=1  literal=1
```

`\b` needs a word/non-word transition on each side. A token that *starts* with `.` or `~` (non-word, after a
space which is also non-word) and *ends* with `/` (non-word, before a space or `。`) has no such transition:
`.codebuddy/skills/` is present twice and matches zero times word-bounded. Since C1(a) requires at least one
root or placement token per vendor and every one of the four vendors' roots has this shape
(`.trae/skills/`, `~/.trae-cn/skills/`, `.codebuddy/skills/`, `~/.codebuddy/skills/`, `.kimi-code/skills/`,
`.agents/skills/`, `docs.bigmodel.cn` aside), **C1 can never reach `N == 4`** under the literal clause.

The fix that keeps the intent and can still fail: define the boundary as "not preceded and not followed by
`[A-Za-z0-9_-]`" — `(?<![A-Za-z0-9_-])` … `(?![A-Za-z0-9_-])`. Measured, the substitution is not a
weakening but a strict improvement in both directions, because `\b` today is wrong on keys too:

```
$ python3 -c "... re.search(r'\bdisable\b','disable-model-invocation') ..."
\bdisable\b in "disable-model-invocation": True
lookaround disable in "disable-model-invocation": False
```

`\b` treats the hyphen as a boundary, so the frozen clause lets a row's `disable` token be satisfied by
`disable-model-invocation` — the exact confusable pair this round's staged entry turns on (the entry credits
`disable` to the IDE page and `disable-model-invocation` to the CLI page). The lookaround form refuses it.

And the loose direction is live on this very page, not hypothetical:

```
$ python3 -c "for m in re.finditer(r'\bname\b', snap): print(line(m))"
\bname\b at snapshot line 17 -> skill-name/
\bname\b at snapshot line 20 -> │   │   ├── name: (必需)
\bname\b at snapshot line 32 -> 元数据 (YAML Frontmatter):name 和 description 决定了 AI 何时会使用这个 Ski
\bname\b at snapshot line 37 -> name: pdf-editor
```

`\bname\b` counts the `name` inside `skill-name/` at line 17 — a `grep -c -F` hit that is not the key. So the
frozen clause under-counts paths and over-counts keys on the same page, and both readings are wrong in the
direction that matters.

The peer seat proposed a stricter variant, `(?<![A-Za-z0-9_/.-])<tok>(?![A-Za-z0-9_/-])`. Measured against
mine on this snapshot, the two agree on every token in the audit table and on every adversarial case I could
construct; they differ only for a token that ends in a word character and is followed by `/` (`skills` in
`skills/foo`: mine matches, the peer's does not). Every vendor root in C1 is a full path ending in `/`, so
either variant closes the defect; mine is the smaller edit, the peer's additionally refuses a bare directory
name. The counter owner picks one and states it in the plan, the docstring and the receipt.

So the one change makes C1(a) satisfiable for placement tokens **and** able to fail on key confusion; the
witnesses on this snapshot:

| world | `\b` clause (frozen) | lookaround clause |
|---|---|---|
| `.codebuddy/skills/` present twice (this page) | 0 — false negative | 2 — correct |
| `name` claimed, `skill-name/` present (this page, line 17) | 1 — false positive on a non-key line | 0 — correct |
| `disable` claimed, only `disable-model-invocation` present (a token-stuffed row) | 1 — false positive | 0 — correct |

The counter owner makes the edit; this is a read-only seat and I have not touched `verifiers/`. The point for
the L1 is only that the clause must be restated in the plan, the counter docstring and the receipt before
any seat scores data (Q28) — as frozen, C1(a) cannot be met by any honest vendor row.

## 6. Files, cleanup, tooling

Written (all under the lane's wave-1 build dir, nothing committed, no lane file touched):

- `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/snapshot.md`
- `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/snapshot.sha256`
- `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/fetch-record.txt`
- `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyIde/registry-row.md`

Scratch `/tmp/k73w1-ExecSrcCodebuddyIde.fetch.*` deleted before return. No git write, no jj command, no
gate run, no sandbox built (no gate needed for a source opening). No tool installed or upgraded.

## 7. Risks

1. **The `\b` clause (§5) is the one thing that can make C1 a structural miss** rather than a sourcing miss;
   it must be decided before any seat scores data (Q28).
2. **The entry's Tencent cell needs splitting, and its third-pattern sentence needs a vendor removed.**
   Project root is S216; the user root is S217 (peer-read); `.agents/skills/` is on neither page, so the
   "all four" sentence is currently a four-vendor claim with three vendors behind it. Both fixes are one-cell
   edits inside the staged entry, and neither touches the lane's frozen C1 predicate.
3. **Snapshot line numbers are stable only for this fetch** (sha256-pinned). The freeze should pin
   `snapshot.md`'s hash, not the HTML's, since the extraction recipe is what the row's line pointers index.
4. `corpus/SOURCES.md:5` says the contract is fleet `SOURCES-CONTRACT-v1.md`; that file does not exist at the
   fleet root (`ls SOURCES-CONTRACT-v1.md` → No such file), and `corpus/QUALITY.md:6-7` ("Tier definitions
   live in `corpus/SOURCES.md`") plus `corpus/README.md:60` ("tier definitions defer to `SOURCES.md`") both
   defer to a file whose sections are only `## Registry`, `## Paths`, `## Search log` and four
   `## Leads (unopened)` headings — `grep -c -E '^\| tier|Tier A|Tier B' corpus/SOURCES.md` → `0`. The tier A/B distinction
   is therefore convention-only in this lane; my A-vs-B note in §4 carries the precedent lines so the L1 can
   overrule it without re-deriving anything.

## 8. Corrections after the peer cross-check (audit trail)

`ExecSrcCodebuddyCli` — the seat that owns the CLI page — answered two open questions with their own snapshot
of S217. I did **not** open S217, so everything below sourced to them is peer evidence, not my measurement,
and every S216 number in this report remains mine.

What changed in this report as a result:

1. `~/.codebuddy/skills/` moved from "unsourced defect" to "**citation-precision defect**": the peer reports
   the token on S217 at two lines (`2. **用户级 Skills**：`~/.codebuddy/skills/`（用户主目录下）` and the
   `/skills` panel list). My S216 measurement is unchanged — 0 occurrences, page states no user-scope path.
   The entry's error is writing both roots in one cell cited `(S216, S217)`, which makes the page named first
   look like it carries a root it does not.
2. `.agents/skills/` was **upgraded**, not downgraded: the peer reports 0 occurrences on S217 as well, so the
   staged "all four vendors read `.agents/skills/`" has no Tencent page behind it on either cited page. My
   S216 probe stands (`agents-root occurrences=0`).
3. §5 gained a third witness (the `\bname\b` hit on `skill-name/`, snapshot line 17) and a comparison of my
   boundary variant with the peer's stricter one. Both variants agree on every token in this audit; they
   differ only for a bare directory name followed by `/`.

Their independent reproductions that agree with my S216 side: required markers are the IDE page's (their CLI
field table marks all nine rows 否); the IDE page documents `disable` only and has 0 `disable-model-invocation`;
the IDE page states no precedence while S217 states it twice. None of that is folded into my row — the row
stays scoped to the IDE page's own normative frontmatter statement.
4. Pointer conflict, opened and then **closed as a shaping split**. The peer first cited the IDE page's
   `name: (必需)` at "IDE text line 30"; my retained snapshot has it at line 20 with `description: (必需)` at
   line 21 (both `grep -n`-verified), and snapshot line 30 is blank. The peer then re-fetched the page
   (byte-identical, sha256 `35114e39…` both times) and withdrew the extraction-dependent pointers, moving to
   pinned-byte facts instead — `grep -o -F` on the raw HTML counts `name: (必需)` 1, `description: (必需)` 1,
   `必需` 10, `allowed-tools` 1, `disable` 1, `disable-model-invocation` 0, `~/.codebuddy/skills/` 0,
   `.codebuddy/skills/` 2, `.agents` 0 — every count of which I then re-measured myself on a third
   independent fetch from the same URL, sha256 `35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6`
   (byte-identical to my 21:00 fetch), obtaining the identical nine numbers. So the two
   readings index different artifacts (217 KB raw HTML vs a 101-line extracted snapshot), not different facts.
   **At landing, quote the byte-level counts and re-derive any line pointer from a sha256-pinned extraction**;
   the row in §4 cites my snapshot lines, whose artifact is the only IDE copy retained.
