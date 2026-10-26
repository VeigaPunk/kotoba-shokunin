# ExecSrcKimiZh — Kimi Code (Chinese) skills page: opened, snapshotted, tokens audited, one registry row

Seat: ExecSrcKimiZh (leaf, read-only executor for source opening; writes only under
`.ufo/waves/round-73/w1/build/ExecSrcKimiZh/` and this report). Round 73, wave 1, C1 coverage, vendor
**Kimi Code**. Date of work: 2026-10-25.

## Verdict

The live page `https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html` supports **every
backticked token** the staged entry attributes to it (18 tokens checked, 0 ABSENT), and it is a
pre-rendered VitePress document, not a JS shell, so no alternate text extraction was needed. **But the
staged entry's joint `(S218, S219)` citation is not safe**: the current `MoonshotAI/kimi-cli`
`docs/*/customization/skills.md` document that S218 names carries a *different* frontmatter table
(`name`, `description`, `license`, `compatibility`, `metadata`) and different user roots
(`~/.config/agents/skills/` recommended) — none of `whenToUse`, `disableModelInvocation`, `arguments`,
`type`, `.kimi-code`, `KIMI_CODE_HOME` occurs in it (0 hits each). The page's own source of truth is
`MoonshotAI/kimi-code` `docs/zh/customization/skills.md`, verified below. One registry row is drafted and
parses to 11 cells; the located quote (14 words) is grounded at `snapshot.md:86`.

## 1. Fetch record

```
$ curl -sL --max-time 60 -A 'Mozilla/5.0' -o /tmp/kimi-skills.raw \
    -w 'status=%{http_code} url=%{url_effective} bytes=%{size_download}\n' \
    'https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html'
status=200 url=https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html bytes=79788
$ date -I
2026-10-25
$ sha256sum /tmp/kimi-skills.raw
e3b314dcff628fc2f88fe6b679e7d6096a209725451957b8ca35360fb5f20989  /tmp/kimi-skills.raw
$ file /tmp/kimi-skills.raw
HTML document, Unicode text, UTF-8 text, with very long lines (31615)
```

Headers (`curl -sL -o /dev/null -D -` on the same URL): one `HTTP/2 200`, **no `location:` header**
(no redirect chain), `content-type: text/html`, `last-modified: Sat, 24 Oct 2026 08:25:19 GMT`,
`date: Mon, 26 Oct 2026 00:02:08 GMT` (local access date `date -I` = 2026-10-25).

Not a JS shell: the markup holds the page text (`<h1>`…`<h3>`, `<table><thead><tr><th>`, `<pre>` code
blocks); the only window global of interest is `window.__VP_HASH_MAP__` (asset bookkeeping). Independent
byte agreement: the sibling artifact `.ufo/waves/round-73/w1/build/CriticEntryRisk/S219.raw`
(`sha256sum` run by me) is the same 79,788 bytes, same `e3b314dc…` — a second same-day fetch of the same
bytes, used only as corroboration of the byte identity, not as content evidence.

Saved: `raw-skills-zh.html` (79,788 B, `e3b314dc…`) in the build dir.

## 2. Snapshot

- `snapshot.md` — 142 lines, 6,928 B, sha256
  `e34a1f1cfdbfcaa7997c755cb90d6d4fceed396cfcec81cffce8b16598039d1d`; pin line in `snapshot.sha256`:
  `e34a1f1cfdbfcaa7997c755cb90d6d4fceed396cfcec81cffce8b16598039d1d  snapshot.md`.
- Produced by `extract.py` in the same dir (`python3 extract.py raw-skills-zh.html > snapshot.md`);
  shaping is documented in its docstring: site chrome (`script/style/nav/header/footer/aside/button` and
  the VitePress `<span class="lang">` fence label) dropped, headings `#`-prefixed, `<pre>` content copied
  verbatim, table cells `|`-separated, the U+200B heading anchor removed, >2 blank lines collapsed.
  No translation, no re-wrap, no token normalisation.
- Provenance: the snapshot is the render of the maintainer's markdown
  `MoonshotAI/kimi-code` `docs/zh/customization/skills.md` —
  `https://raw.githubusercontent.com/MoonshotAI/kimi-code/main/docs/zh/customization/skills.md`
  (HTTP 200, 7,332 B, sha256 `2fa8c4e99d03d4fce8e9bd5b367698801ab4e9eca564d357054dec9a5c9710ff`; saved as
  `source-docs-zh-skills.md`). A formatting-insensitive containment check
  (`**`/backtick/link stripping on the markdown, prefix-preserving comparison) matched **94 of 107**
  non-empty snapshot lines; the 13 misses are 10 ``` fence markers and 3 fenced-code lines whose literal
  backticks survive in the snapshot but were stripped from the markdown by the comparison, i.e. markup
  rendering only, not content difference. The English twin `docs/en/customization/skills.md` has the same heading set
  (`## Skill Locations` :85, `### Frontmatter Fields` :59) and the same key vocabulary.

## 3. Token audit — every backticked token the staged entry attributes to this page

Source of the token list: `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/chinese-client-skill-surfaces.md`
— the Moonshot row (paths `…(S218, S219)`) and the "frontmatter-vocabulary divergence" paragraph (cited
`(S219)`). Counts are `grep -c -F` on `snapshot.md` plus the matching line numbers; the last column is a
word-bounded count (`(?<![\w-])token(?![\w-])`, the predicate's matching rule).

| token | grep -c -F | snapshot lines | word-bounded | verdict |
|---|---|---|---|---|
| `.kimi-code/skills/` | 3 | 83, 89, 137 | 2 | PRESENT (line 137 is `…/skills/review-pr/…`, so not word-bounded there) |
| `.agents/skills/` | 3 | 84, 86, 90 | 3 | PRESENT |
| `$KIMI_CODE_HOME/skills/` | 2 | 83, 137 | 1 | PRESENT |
| `~/.kimi-code/skills/` | 2 | 83, 137 | 1 | PRESENT |
| `~/.agents/skills/` | 2 | 84, 86 | 2 | PRESENT |
| `name` | 9 | 23,24,25,36,57,62,66,73,113 | 12 | PRESENT |
| `description` | 5 | 37,58,66,107,114 | 5 | PRESENT |
| `type` | 4 | 38,59,107,115 | 4 | PRESENT |
| `prompt` | 3 | 38,59,115 | 4 | PRESENT |
| `inline` | 1 | 59 | 1 | PRESENT |
| `flow` | 2 | 59,107 | 2 | PRESENT |
| `whenToUse` | 4 | 39,60,107,116 | 4 | PRESENT |
| `when-to-use` | 1 | 60 | 1 | PRESENT |
| `when_to_use` | 1 | 60 | 1 | PRESENT |
| `disableModelInvocation` | 3 | 40,61,107 | 3 | PRESENT |
| `disable-model-invocation` | 1 | 61 | 1 | PRESENT |
| `disable_model_invocation` | 1 | 61 | 1 | PRESENT |
| `arguments` | 4 | 41,62,73,117 | 5 | PRESENT |
| `extra_skill_dirs` (page-only, not in the staged entry) | 2 | 92,94 | 2 | page fact the entry omits |

`ABSENT` tokens: none. The two anchor headings the staged S219 source line names also exist:
`### Frontmatter 字段` at `snapshot.md:54`, `## Skill 存放位置` at `snapshot.md:78` (the staged line
writes both with a `#` prefix; the rendered levels are h3/h2, so the level is imprecise, the text exact).
The Qwen extension entry names this page nowhere: `grep -c -i 'kimi'
…/client-surface-census-extension.md` prints `0` (exit 1), so it attributes no token to S219.

## 4. Located quote and the registry row

Located quote, copied from the snapshot (`sed -n '86p'` output, pasted; the only dropped bytes are the
line terminator, no shaping):

```
Kimi 专属用户级 Skill 目录会随 KIMI_CODE_HOME 移动，隔离数据根时也会隔离 Kimi 专属 Skills。通用 ~/.agents/skills/ 目录仍放在真实 OS home 下，以便跨工具共享。
```

Location: § `## Skill 存放位置` (`snapshot.md:78`), paragraph at `snapshot.md:86`. Counts:
`sed -n '86p' snapshot.md | wc -w` → `14`; `wc -m` → `114`. The quote is `quote-equal` to that snapshot
line (not `byte-exact` to the HTML: the snapshot is itself the documented text extraction of the bytes).

Drafted row (`registry-row.md`; id is the `S<<id>>` placeholder because the package's staged numbers
collide with the lane's live S203–S216 per `plans/round-73.md`; host `www.kimi.com` is in the frozen
C1 host set):

```
| S<<id>> | Kimi Code Docs — Agent Skills (中文站点) — https://www.kimi.com/code/docs/kimi-code-cli/customization/skills.html | docs | A | Kimi Code CLI's own skill discovery roots, scope precedence and frontmatter vocabulary, as its maintainer documents them (vendor documentation for its own CLI; not a measurement of the running CLI) | § Skill 存放位置 (`snapshot.md:86`); live page opened 2026-10-25, HTTP 200, 79,788 B, sha256 `e3b314dc…`, `last-modified: Sat, 24 Oct 2026 08:25:19 GMT`, rendered from `MoonshotAI/kimi-code` `docs/zh/customization/skills.md` (7,332 B, sha256 `2fa8c4e9…`); headings `## Skill 存放位置` (`snapshot.md:78`), `### Frontmatter 字段` (`snapshot.md:54`) | Kimi Code CLI moves its own user-level skills directory with `KIMI_CODE_HOME` while the shared `~/.agents/skills/` root stays in the real OS home for cross-tool sharing, so isolating the data root isolates vendor skills only | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |
```

Validation:

```
$ awk -F'|' '{printf "NF=%d\n", NF}' registry-row.md
NF=13
$ awk -F'|' 'NF!=13{print "BAD NF="NF}' registry-row.md      # no output, exit 0
cells: 11  id=[S<<id>>] kind=[docs] tier=[A] status=[mined] opened=[2026-10-25] recheck=[90d] usedby=[corpus/knowledge/chinese-vendor-skill-surfaces-round73.md]
```

Tier rationale: `CORPUS.md:93` — tier **A** is "primary or authoritative for that scope (spec, official
docs, source code, original paper, maintainer statement…)"; this is the vendor's own documentation of its
own CLI, and the scope cell restricts it to what the vendor documents, explicitly not a measurement of
the running binary. `kind docs`, `status mined`, no `|` inside any cell.

## 5. What the page does NOT say that the staged entry claims

1. **No intra-root ordering, and no "first-class group".** The entry says, of the `.agents/skills/` root,
   "Kimi as a first-class group alongside its own vendor root". The page lists the project roots
   `.kimi-code/skills/` (`:89`) and `.agents/skills/` (`:90`) with no ordering, and its only precedence
   rule is across the four scopes — "Kimi Code CLI 按作用域分四档扫描，越具体的作用域优先级越高：Project >
   User > Extra > Built-in。" (`:80`). Which root wins on a project-level name collision is **not stated on
   this page**; "first-class group" is the entry's inference, not the page's words.
2. **No "scan brief descriptions before loading" mechanism for Kimi.** The entry's shared-pattern sentence
   says all four "describe the trigger as the model scanning brief descriptions before loading anything".
   This page says only: "模型也可以根据 description 和 whenToUse 自动调用 Skill。disableModelInvocation 设为
   true 或 type 设为 flow 时不自动调用。" (`:107`, pasted from the snapshot without the page's inline-code
   styling) — auto-invocation from `description` + `whenToUse`,
   nothing about pre-scanning brief descriptions. (That mechanism is in the English kimi-cli doc, S218's
   ground, not here.)
3. **`name`/`description` "required" is conditional.** The page states the requirement for the *directory*
   form only — "目录型 SKILL.md 中 name 和 description 必须显式填写，省略任意一项均会导致解析失败。"
   (`:66`) — while the flat form may omit them (`:57`, `:58`: `name` from the file name, `description`
   from the first non-empty body line, truncated at 240 characters). The staged row lists the keys without
   that condition.
4. **Fields this page does not carry at all.** `license`, `compatibility`, `metadata` — the fields the
   current kimi-cli document (S218) puts in its frontmatter table — are absent from this snapshot; and the
   fields this page carries (`type`, `whenToUse`, `disableModelInvocation`, `arguments`) are absent from
   that document (§ 6). A row citing both pages jointly therefore cites no single page for its field list.
5. **Coverage the entry omits** (gaps, not false claims): the page also documents `extra_skill_dirs`
   declared in `config.toml` (`:92`, `:94`), `builtin_product_skills` to switch off the built-in product
   skills (`:97`), the project-root definition ("工作目录向上最近的含 .git 的目录", `:88`), and the
   § 调用 Skill rule that skill invocation nests at most 3 levels (`:107`).

## 6. Cross-check of the `(S218, S219)` joint citation (evidence only; S218 is not my claim)

Against the sibling English snapshot `.ufo/waves/round-73/w1/build/ExecSrcKimiEn/snapshot.md`
(sha256 `5a18c338…`, the current `MoonshotAI/kimi-cli` `docs/en/customization/skills.md`):

```
$ for t in '.kimi-code' 'KIMI_CODE_HOME' 'whenToUse' 'when-to-use' 'disableModelInvocation' 'disable-model-invocation' 'arguments'; do printf '%s\t%s\n' "$t" "$(grep -c -F -- "$t" $S)"; done
.kimi-code	0
KIMI_CODE_HOME	0
whenToUse	0
when-to-use	0
disableModelInvocation	0
disable-model-invocation	0
arguments	0
$ grep -n '~/.config/agents/skills/' $S
39:  1. `~/.config/agents/skills/` (recommended)
```

and its § Frontmatter fields table (`$S:166-174`, rows at `:170-174`) lists `name`, `description`, `license`,
`compatibility`, `metadata` — a different generation of the format. Consequences for the entry, stated
without judging S218: the entry's Kimi row cannot be grounded by S218 for its keys, and the entry drops
S218's recommended root `~/.config/agents/skills/`. The live zh page (S219) is the newer, product-site
document and is the one this seat can back.

## 7. Handoff for the L1 integration

- Snapshot for C1 conjunct (c): copy
  `.ufo/waves/round-73/w1/build/ExecSrcKimiZh/snapshot.md`
  (sha256 `e34a1f1cfdbfcaa7997c755cb90d6d4fceed396cfcec81cffce8b16598039d1d`, 6,928 B) to
  `.ufo/waves/round-73/snapshots/` and pin it in `snapshots/MANIFEST.sha256`, e.g.
  `e34a1f1cfdbfcaa7997c755cb90d6d4fceed396cfcec81cffce8b16598039d1d  snapshots/<chosen-name>.md`
  (the manifest's second field must match the path as the counter resolves it).
- Two paths this report names do not exist at the base and are integration targets, not filed bytes:
  `.ufo/waves/round-73/snapshots/` (and its manifest) and `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md`.
  A report-pointer check run before the L1 lands them will name exactly these two; that is expected.
- Row: `registry-row.md`; replace `S<<id>>` with the renumbered id at integration. The row's URL host
  `www.kimi.com` is in the frozen C1 host list for Kimi Code; the row's quote is `snapshot.md:86`.
- Entry-side tokens that the row may carry, all verified here: `.kimi-code/skills/`, `.agents/skills/`,
  `$KIMI_CODE_HOME/skills/`, `~/.kimi-code/skills/`, `~/.agents/skills/`, `whenToUse`,
  `disableModelInvocation`, `type`, `arguments` (≥3 tokens, ≥1 root/placement token, ≥2 keys satisfied).
  Prefer the word-bounded group; note `.kimi-code/skills/` is word-bounded only at `:83`/`:89`.
- If the entry keeps the "first-class group" or "scans brief descriptions" wording, it must cite S218 for
  those clauses or drop them (§ 5 items 1–2).

## 8. Bounds and tooling

- Read-only on the lane: no committed lane file touched, no `jj`, no lane Git index write, no gate run.
  The only git-adjacent commands were `curl`/`sha256sum`; no fixture repo was created.
- Scratch: all temporary files were left in `/tmp` by name (`/tmp/kimi-*`, `/tmp/kc-*.json`,
  `/tmp/q86.txt`, `/tmp/snap.sha`) and deleted (`ls /tmp | grep -c '^kimi-'` → `0`); deliverables live
  only in `.ufo/waves/round-73/w1/build/ExecSrcKimiZh/` (`raw-skills-zh.html`, `snapshot.md`,
  `snapshot.sha256`, `extract.py`, `source-docs-zh-skills.md`, `token-counts.txt`, `registry-row.md`).
- Tools installed: none. No pacman/npm/uv transaction was run.
