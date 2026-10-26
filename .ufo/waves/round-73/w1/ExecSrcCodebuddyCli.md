# ExecSrcCodebuddyCli — C1 source opening: CodeBuddy **CLI** Skills page (staged S217)

## Verdict

The page was opened today and it is **sourceable**: HTTP 200, VitePress server-rendered HTML (not a JS
shell), 217,520 bytes, byte-identical across two fetches, and its text extracts to a 25,241-byte snapshot. The
vendor's two discovery roots (`project` / `user`) and the two frontmatter keys the staged entry names are on
the page, and each was counted with a stated boundary recipe and pinned. **Four staged-entry defects are
confirmed against this page** (a fifth, the `name`/`description` "required" cell, is confirmed by fetching the
sibling IDE page myself), and one **plan-level defect** is proved: predicate C1(a)'s "word-bounded" clause,
read literally as `\b`, is wrong in **both** directions — too tight for every placement token (all of them
begin with `.` or `~` and end with `/`, so `N == 4` is unreachable) and too loose for keys (it would score the
staged, absent `disable` token as backed). That must be settled before any data (Q28), not after.

Snapshot: `.ufo/waves/round-73/w1/build/ExecSrcCodebuddyCli/snapshot.md` (25,241 B, 699 lines,
sha256 `88468f4f5f80055a86c5107eb87d530485bc8003313a742a214c55a4cfe4f784`). Raw response:
`raw-cli-skills.html` (217,520 B, sha256 `ee9e3b7187c5105bd1147dff41c1ecb793b695a28f3d1804344f543d6e34f2ee`).
Pins: `snapshot.sha256`. Fetch record: `fetch-log.md`. Shaping: `SNAPSHOT-SHAPING.md`. Row: `registry-row.md`.

---

## F1 — the fetch: 200, no redirect, stable bytes, and it is not a JS shell

```
$ cd .ufo/waves/round-73/w1/build/ExecSrcCodebuddyCli
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o raw-cli-skills.html -w 'http_status=%{http_code}\nfinal_url=%{url_effective}\nsize=%{size_download}\ncontent_type=%{content_type}\n' https://www.codebuddy.ai/docs/zh/cli/skills
http_status=200
final_url=https://www.codebuddy.ai/docs/zh/cli/skills
size=217520
content_type=text/html; charset=utf-8

$ sha256sum raw-cli-skills.html
ee9e3b7187c5105bd1147dff41c1ecb793b695a28f3d1804344f543d6e34f2ee  raw-cli-skills.html

$ date -I
2026-10-25
```

`num_redirects=0` (recorded in `fetch-log.md`); the local clock at fetch was `2026-10-25T21:00:49-03:00`.
A second fetch at `2026-10-25T21:02:01-03:00` returned the same 217,520 bytes and `cmp -s` printed
nothing → **byte-identical** across two fetches.

Not a shell: the article body is in the initial response —
`grep -c -F '项目级 Skills' raw-cli-skills.html` → `3`, `grep -c -F 'allowed-tools'` → `11`,
`grep -c -F 'disable-model-invocation'` → `1`. No raw-markdown export exists to prefer:
`.../cli/skills.md` returns **200 with 3,884 bytes** of the SPA's English not-found shell
(title `Tencent Cloud Code Assistant CodeBuddy – AI Code Editor`, empty body text), and
`/docs/llms.txt` (3,884 B) and `/llms.txt` (9,124 B) are the same shell served as `text/html`.

Extraction: `div.vp-doc` → markdown (`h*`, `pre` verbatim, `ul`/`ol`, pipe tables, inline `code` as backticks).
Two named transformations, no content moved or dropped: inline whitespace runs collapsed to one space, and
VitePress heading anchors kept as rendered (`[​](#anchor)`, U+200B). Details in `SNAPSHOT-SHAPING.md`.

## F2 — token census: what the staged entry attributes to this page, token by token

Boundary recipe used: left `(?<![A-Za-z0-9_/.-])`, right `(?![A-Za-z0-9_/-])` (see F7 for why `\b` cannot be
used). The counts in this section are **lookaround-bounded counts, not `\b` counts** — a counter or receipt
that prints them must name this recipe, because `\b` would have counted `~/.codebuddy/skills/` as absent (too
tight) *and* `disable` as present (too loose). Command:

```
$ python3 - <<'PY'
import re
lines=open('snapshot.md',encoding='utf-8').read().split('\n')
for tok in ['name','description','allowed-tools','disable','disable-model-invocation',
            '.codebuddy/skills/','~/.codebuddy/skills/','项目级 Skills','用户级 Skills']:
    pat=re.compile(r'(?<![A-Za-z0-9_/.-])'+re.escape(tok)+r'(?![A-Za-z0-9_/-])')
    ls=[i+1 for i,l in enumerate(lines) if pat.search(l)]
    print(f'{tok:<26} lines={len(ls)} {ls[:12]}')
PY
```

| staged token | attributed to this page by | lookaround-bounded count | snapshot lines | status |
|---|---|---|---|---|
| `.codebuddy/skills/` | staged entry vendor row (project roots) | 5 | 35, 41, 326, 615, 640 | **PRESENT** |
| `~/.codebuddy/skills/` | staged entry vendor row (user roots) | 2 | 36, 639 | **PRESENT** |
| `name` | staged entry vendor row | 12 | 58, 83, 167, 181, 213, 245, 290, 373, 410, 452, 535, 662 | **PRESENT** (as a key: 58, 213, 245, 290, 373, 410, 452) |
| `description` | staged entry vendor row | 15 | 59, 84, 115, 132, 183, 214, 246, 291, 374, 411, 453, 499, … | **PRESENT** |
| `allowed-tools` | staged entry vendor row + prose | 14 | 60, 85, 375, 412, 454, 500, 547, 549, 554, 604, 607, 651, 655, 689 | **PRESENT** |
| `disable-model-invocation` | staged entry vendor row + prose | 1 | 86 | **PRESENT** (field-table row, not an example) |
| `disable` (bare key) | staged entry vendor row | **0** | — | **ABSENT** |
| `# 项目级 Skills` (as heading) | staged entry `source:` line | string 5×, heading **0** | 12, 35, 502, 640, 661 | tokens **present**, **not a heading** |
| `# 用户级 Skills` (as heading) | staged entry `source:` line | string 3×, heading **0** | 12, 36, 502 | tokens **present**, **not a heading** |
| `.agents/skills/`, `allowedTools` | (staged entry, other vendors / Qwen) | 0 | — | **ABSENT** on this page |

`grep`-level confirmation of the two `disable` readings:

```
$ grep -n -F 'disable' snapshot.md
86:| `disable-model-invocation` | 否 | 设置为 `true` 时，Skill 不会出现在 Skill 工具中，只能通过 `/skill-name` 手动触发 | `true` |
535:Skill "<name>" is disabled via skillOverrides. Re-enable it in /skills or remove the override from your settings to run it.
```

Both literal hits are non-keys: the prefix inside `disable-model-invocation` (line 86) and the word `disabled`
inside an error string (line 535). The page's own field table (lines 83–91) has **nine rows and no `disable`
row**.

## F3 — what the page does NOT say that the staged entry claims (each an entry defect)

1. **`disable` as an optional frontmatter key — ABSENT.** Zero lookaround-bounded occurrences (F2). The
   staged vendor row's "`allowed-tools`, `disable` optional" cannot be sourced here. The token belongs to the
   IDE page alone: my own fetch of it shows `disable` exactly once, on the line carrying `是否禁用` (raw
   response line 43, sha256 `35114e39…`), and `disable-model-invocation` 0 (F8). A joint S216+S217 citation
   hides that split.
2. **"`name`, `description` required" — false for this page.** Both are marked 否 (optional) in the field
   table, and `name` explicitly defaults:
   `83: | `name` | 否 | Skill 名称，未指定时使用目录名 | `pdf` |`
   (8 words; the child row's trailing example cell and the leading `| ` are dropped). Same for `description`
   at line 84. "Required" is the IDE page's claim — `name: (必需)` occurs exactly once there, raw response
   line 33 — see F8 for the divergence this creates inside one vendor.
3. **`# 项目级 Skills` / `# 用户级 Skills` are not headings.** They are bold list items under
   `### 目录结构` (line 31):
   `35: 1. **项目级 Skills**：`.codebuddy/skills/`（项目根目录下）`
   `36: 2. **用户级 Skills**：`~/.codebuddy/skills/`（用户主目录下）`
   (two lines quoted; the bold markers are the snapshot's own). A `source:` line citing `# 项目级 Skills` as a
   section points at something that does not exist as a section on this page.
4. **"CLI examples also use `disable-model-invocation`" understates it.** It is a documented field-table row
   (line 86), not an example artifact: `| `disable-model-invocation` | 否 | 设置为 `true` 时，Skill 不会出现在 Skill 工具中`
   (13 words; the tail of the row after `工具中` is dropped).
5. **The staged "three patterns" second claim is wrong for this vendor.** The entry says "both TRAE and Kimi
   make the scope a *precedence* rule rather than just a label", implying CodeBuddy does not. This page states
   precedence twice — `## AI 如何选择 Skills` factor 4 (line 502) and the FAQ (lines 659–662). The sibling
   confirms S216 states none (`grep -n -E '优先级|优先|覆盖|冲突|precedence'` → exit 1). So the correct sentence
   is "CodeBuddy's CLI states it, its IDE page does not".
6. **`.agents/skills/` — ABSENT** (0 hits). Tencent therefore stays out of the entry's third shared pattern
   (cross-vendor root) for **both** CodeBuddy pages; the entry must not silently extend it.

## F4 — what the page says that the staged entry omits (the C1 depth available here)


The staged Tencent row carries 2 keys; the page's field table carries 9 rows (lines 83–91) plus a settings-side
four-state override. Present and verified (line pointers, no quote needed):

| surface | lines |
|---|---|
| `user-invocable: false` — hides from `/` menu, keeps model invocation | 87, section `### 隐藏 Skill（user-invocable）` 234–248 (example 245) |
| `context: fork`, `agent`, `model` — subagent-context execution | 88–90, 205–233 (example 290) |
| `hooks` inside `SKILL.md`, `context: fork` only, with an `admin-trusted` safety gate | 91, 270–362 (gate heading 324) |
| `skillOverrides` four-state visibility (`on` / `name-only` / `user-invocable-only` / `off`), precedence `PROJECT_LOCAL > PROJECT > USER`, illegal values filtered before merge, plugin skills immune (`locked by plugin`) | 504–543 (540) |
| variable placeholders `${…}`, `${VAR:-default}`, applied to skills, slash commands and subagent definitions | 93–121 |
| declaring output files in `SKILL.md` | 158–204 |
| `/skills` panel shows name + estimated token count, split user / project / plugin | 629–643 |
| `allowed-tools` pattern matching, `Bash(git:*)`, `Edit(src/**/*.ts)` | 547–560, 604–607 |
| the agent picks by description-vs-task relevance and by tool need | 495–502 |

Recommended token set for the entry's CodeBuddy row (all present word-bounded, so predicate C1(a) is
satisfiable as soon as F7's boundary wording is fixed): `.codebuddy/skills/`, `~/.codebuddy/skills/`, `name`,
`description`, `allowed-tools`, `disable-model-invocation` — 1 root + 5 keys, comfortably over the 3-token /
1-root / 2-key floor; add `user-invocable`, `context`, `hooks`, `skillOverrides` if the row should carry the
page's actual depth. **Do not carry `disable`.**

## F5 — located quote and the drafted registry row

Quote, `sed -n '661,662p' snapshot.md` (the newline between the two adjacent bullets is the only dropped byte
sequence; the two markers `- ` are the snapshot's own bytes):

```
661: - 项目级 Skills 优先级更高
662: - 使用不同的 name 避免冲突
```

> `- 项目级 Skills 优先级更高 - 使用不同的 name 避免冲突` — 8 whitespace tokens, located under
> `### 常见问题` (line 645), whose question is `**Q：项目级和用户级 Skill 冲突？**` (line 659).
> Found in the snapshot after whitespace collapse only: `re.sub(r'\s+',' ',text)` → `True`.

It grounds the one-sentence `teaches`: a project skill outranks a user skill of the same name, and distinct
names avoid the collision — the fact the staged entry's "three patterns" paragraph denies this vendor.

Row (also in `registry-row.md`, id placeholder pending the L1's renumber; lane max id today is `S216`):

| S<<id>> | CodeBuddy Code Skills （技能系统） — Tencent CodeBuddy CLI docs — https://www.codebuddy.ai/docs/zh/cli/skills | docs | B | the CLI skill surface: its two discovery roots, the frontmatter keys the CLI documents, and the project-over-user precedence on a name collision, as one vendor's own page states them | `### 常见问题` at snapshot line 645, its scope-collision answer at lines 659-662, the root list at lines 35-36 and the field table at lines 83-91; quote "- 项目级 Skills 优先级更高 - 使用不同的 name 避免冲突" (8 tokens; the newline between the two adjacent bullets collapsed to one space) | the CLI discovers project skills in `.codebuddy/skills/` and user skills in `~/.codebuddy/skills/`, routes on `description`, and gives a project skill precedence over a user skill of the same name while documenting `disable-model-invocation`, not a bare disable key | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |

Parse check:

```
$ awk -F'|' '/^\| S<<id>> \|/ {print "NF="NF}' registry-row.md
NF=13
```

13 fields = 2 empty edges + 11 cells; no `|` inside any cell. Tier B (one vendor's documentation, not the
maintainer's own statement about the lane). Host `www.codebuddy.ai` matches the frozen host set for
CodeBuddy.

Hygiene check on the `teaches` cell: `grep -n 'required' registry-row.md` → exit 1. The cell deliberately never
says which keys are *required*: the two CodeBuddy pages disagree on exactly that (F8), so a row asserting
either contract would be contradicted by the other page at landing. Same discipline the IDE-page row needs —
the divergence belongs in the entry's divergence paragraph, where both citations can stand side by side.

## F6 — for the L1: snapshot placement for predicate C1(c)

My write scope is `w1/build/ExecSrcCodebuddyCli/`; the predicate wants the snapshot under
`.ufo/waves/round-73/snapshots/` with its sha256 in `snapshots/MANIFEST.sha256`. Copy
`snapshot.md` → `.ufo/waves/round-73/snapshots/<assigned-id>-codebuddy-cli.md` and pin
`88468f4f5f80055a86c5107eb87d530485bc8003313a742a214c55a4cfe4f784`. Predicate (c) is satisfiable as written:
`.ufo` is tracked, not ignored —

```
$ git ls-files .ufo/waves/round-73 | wc -l
14
$ git check-ignore -v .ufo/waves/round-73/w1/build/ExecSrcCodebuddyCli/snapshot.md ; echo exit=$?
exit=1
```

## F7 — plan attack (wave-1 duty): C1(a)'s "word-bounded" clause is wrong in **both** directions

Predicate (a) requires each backticked token to "occur word-bounded in the committed page snapshot". Read as
`re.search(r'\b'+tok+r'\b')`, no dot-prefixed root can ever match, because `\b` needs a word character on both
sides and `.`/`~` are non-word while a trailing `/` needs a word character after it:

```
$ python3 - <<'PY'
import re
t=open('snapshot.md',encoding='utf-8').read()
for tok in ['.codebuddy/skills/','~/.codebuddy/skills/','allowed-tools','disable-model-invocation']:
    m=re.search(r'\b'+re.escape(tok)+r'\b', t)
    print(f'{tok:<26} in_snapshot={tok in t} \\b-match={bool(m)}')
PY
.codebuddy/skills/         in_snapshot=True \b-match=False
~/.codebuddy/skills/       in_snapshot=True \b-match=False
allowed-tools              in_snapshot=True \b-match=True
disable-model-invocation   in_snapshot=True \b-match=True
```

Consequence: a counter implementing the sentence literally can only ever match key tokens, never a "root or
placement token" — so **N == 4 is unreachable at the frozen target** for all four vendors, whose roots are all
dot-prefixed (`.trae/skills/`, `.kimi-code/skills/`, `.agents/skills/`, `.codebuddy/skills/`). This is a
counter/sentence mismatch, not a page problem, and it is not one of the frozen shortcut worlds. Fix before any
data: define "word-bounded" as the boundary I used (`(?<![A-Za-z0-9_/.-])…(?![A-Za-z0-9_/-])`) in the plan
addendum, the counter docstring and the receipt — or state the clause as "literal occurrence with a
non-token-character boundary". Q28: nothing may change after a seat scores data.

### The loose half: `\b` also backs tokens that are not the key

`\b` treats `-` and `/` as non-word, so a key token matches inside a longer hyphenated or slashed string. On
my snapshot:

```
$ python3 - <<'PY'
import re
lines=open('snapshot.md',encoding='utf-8').read().split('\n')
for tok in ['disable','name']:
    hits=[(i+1,l.strip()[:110]) for i,l in enumerate(lines) if re.search(r'\b'+tok+r'\b', l)]
    print(f'\\b{tok}\\b: {len(hits)} lines; first 4: {hits[:4]}')
PY
\bdisable\b: 1 lines; first 4: [(86, '| `disable-model-invocation` | 否 | 设置为 `true` 时，Skill 不会出现在 Skill 工具中，只能通过 `/skill-name` 手动触发 | `true` |')]
\bname\b: 17 lines; …  (83 is the field-table row, 86 the disable-model-invocation row via `/skill-name`)
```

So a `\b`-based counter would score the **staged `disable` token as backed**, which is precisely the defect
F2/F3 measure — the matcher would manufacture the false positive the round exists to catch. Under the
lookaround recipe `disable` is 0 lines and `~/.codebuddy/skills/` is 2 lines: both directions flip to correct.
(An independent peer reached the same two-direction conclusion on the IDE page; the numbers above are mine and
were run on my snapshot.)

Two further checks the L1 can bank as **satisfiable, no defect**:

- do-nothing figure reproduced independently at the base —
  `git show 072048fa8e8a52c707d25f7079772fa317244eb7:corpus/SOURCES.md | grep -ciE 'docs\.trae\.cn|codebuddy\.ai|kimi\.com/code|moonshotai/kimi-cli|docs\.bigmodel\.cn'` → `0`;
  base rows → `142`. So "held at base: 0" is true and the base cannot accidentally score.
- the frozen CodeBuddy host `www.codebuddy.ai` is exactly the URL that answers; no redirect leaves the host.
  (The page's *assets* are served from `download.codebuddy.ai` — an asset host, never a source-cell candidate.)

## F8 — intra-vendor divergence on the same two keys (my own cross-check, not the sibling's number)

The two CodeBuddy products disagree about whether `name` and `description` are required, and the staged entry's
joint `(S216, S217)` citation hides it. I fetched the IDE page myself to confirm the other side:

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o ide.html -w 'status=%{http_code} bytes=%{size_download} final=%{url_effective}\n' https://www.codebuddy.ai/docs/zh/ide/Features/Skills
status=200 bytes=36633 final=https://www.codebuddy.ai/docs/zh/ide/Features/Skills
$ sha256sum ide.html
35114e395730127380bd599904b7175edd7e5939216a31d10ab5a420f02a3fc6  ide.html
```

The re-fetch is byte-identical to the first (`sha256 35114e39…` both times), and on those pinned bytes the
evidence is occurrence counts, not extraction line numbers:

```
$ for t in 'name: (必需)' 'description: (必需)' '是否禁用' '必需' 'disable' 'allowed-tools' 'disable-model-invocation' '~/.codebuddy/skills/' '.codebuddy/skills/' '.agents'; do printf '%-30s %s\n' "$t" "$(grep -o -F "$t" ide.html | wc -l)"; done
name: (必需)                   1
description: (必需)            1
是否禁用                       1
必需                           10
disable                        1
allowed-tools                  1
disable-model-invocation       0
~/.codebuddy/skills/           0
.codebuddy/skills/             2
.agents                        0
```

Raw-response line numbers on the same bytes: `name: (必需)` at raw line 33, `description: (必需)` at raw line 34
(the tree block), `allowed-tools` at raw line 42, `是否禁用` at raw line 43 (the `disable` line), and the project
root at raw line 30 — `Skill 应建立在工作区的 `.codebuddy/skills/` 目录下` (13 words; surrounding HTML spans
dropped).

**Line-pointer portability, stated because two seats measured this page differently:** an earlier draft of this
report cited "IDE text line 30 / 80" from a whitespace-collapsed `div.vp-doc` text dump. Those numbers are
withdrawn — they are an artefact of one extraction recipe, and a peer using `<main>` with different block
splitting legitimately gets different ones. The counts, the sha256 and the raw-response line numbers above are
the artifact-independent form; a reviewer should re-derive from a sha256-pinned copy rather than quote any
seat's extraction line.

| key | CodeBuddy **IDE** (S216) | CodeBuddy **CLI** (S217, mine) |
|---|---|---|
| `name` | 必需 (required) | 否 (optional), defaults to the directory name — snapshot line 83 |
| `description` | 必需 (required) | 否 (optional) — snapshot line 84 |
| `disable` | present as an optional key (IDE line 80) | **absent** (field table 83–91, 9 rows) |
| `disable-model-invocation` | **absent** | present (line 86) |
| `~/.codebuddy/skills/` | **absent** (project scope only) | present (lines 36, 639) |

This is a divergence **inside one vendor**, not a vendor-vs-spec divergence, and it belongs in the entry's
divergence paragraph next to the Qwen `allowed-tools` / `allowedTools` trap — not in either row's `teaches`,
because a row states what its own page says. It is also the reason the staged entry's single Tencent row cannot
be repaired by fixing tokens alone: the row fuses two products whose field contracts differ.

## F9 — not observed (stated, not inferred)

- `verifiers/check_cn_vendor_surfaces.py` and `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` did
  not exist as of 21:02 (`ls` → `No such file or directory` for both), so the counter could not be run against
  this row. My row is unexecuted evidence: it parses to 11 cells and every token in it is present, but no
  counter agreed or disagreed yet.
- I did not re-open the TRAE, Kimi or Zhipu pages; the `.trae/`/`.kimi-code/` strings in F7 are the staged
  entry's spellings, used only to show the regex arithmetic, not as page evidence.
- No tool was installed (no upgrade needed); no host service touched; no pacman call made.

## Scratch

Two scratch dirs, both deleted before this report was finalized: `/tmp/k73w1-ExecSrcCodebuddyCli.Kr0m` (the
HTML parse, the alternate-URL probes and the byte-stability re-fetch) and `/tmp/k73w1-ExecSrcCodebuddyCli.Okv4`
(the IDE-page cross-check in F8). Nothing outside `w1/build/ExecSrcCodebuddyCli/` and this report was written,
and no tracked lane file was touched.
