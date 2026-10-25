# ExecQuar06 — quarantine hand-check, register slice row 6 of 13

**Verdict: `absent` → refuse as fabrication class.** The register row's quoted span
`スキルのインストール` is not a heading, not a table cell and not contiguous text in the cited
archive snapshot, in any other 2026 snapshot of the same page, in the live Japanese page, in the
live `.md` export, or in the English archive. It is not a fold of any heading that does exist.
Staged id for the row's URL: **S260** (`SOURCES.append.md:64`, exact `?hl=ja` URL match).
Calibration: the staged record S260 is *not* itself fabricated — its own payload quote is present
verbatim in the cited snapshot at line 1533 under the heading 「API 開発スキルを追加する」. What is
fabricated is the register row's *quote*: it names a section that the page never had.

## 1. Register row, re-read (not taken from the assignment text)

```
$ sed -n '6p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt
| `kotoba` | round6 | S180 | `payload-absent` | https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | `スキルのインストール` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Quoted span: `スキルのインストール` (10 chars). Campaign id in the row: `S180`.

## 2. Staged row lookup by URL host+path

```
$ grep -n 'ai\.google\.dev/gemini-api/docs/coding-agents' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
53:| S249 | Google — Coding agent setup & developer resources … — https://ai.google.dev/gemini-api/docs/coding-agents — archived at https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents …
64:| S260 | Google — Gemini API：コーディング アシスタントの設定（日本語） — https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja — the live address `https://ai.google.dev/gemini-api/docs/coding-agents` redirects in a loop and is not reachable | docs | B | …
```

Row 6's URL carries `?hl=ja` → **staged id S260** (line 64). S249 (line 53) is the English page,
a different record. S260's payload cell reads: 「スキルのインストール」section of the archived
Japanese page; quote "MCP がインストールされていない場合でも、フォールバックとして ai.google.dev から
llms.txt を取得します。"; also "skills.sh : 推奨。…" and the command
`npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global`; artifact cell
`corpus/knowledge/japanese-first-party-skill-sources.md`.

## 3. Fetch of the cited URL

```
$ curl -sSL -A 'Mozilla/5.0' -o archive.html -w 'HTTP=%{http_code} FINAL=%{url_effective} SIZE=%{size_download}\n' \
    'https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja'
HTTP=200 FINAL=https://web.archive.org/web/20260908032619/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja SIZE=113449
$ sha256sum archive.html
1b9ea838f3740569344d679603d7e935023471bbb59d753b9b3e548e191d951f  archive.html
```

Access date 2026-10-25 (`date -u` → `2026-10-25T21:40:31Z`). HTTP 200, no error page, 113 449 B,
snapshot **20260908032619**. Page title (line 42): `Gemini MCP とスキルを使用してコーディング アシスタントを設定する`.
The fetch succeeded, so the row is **not** `unverifiable-class` and **not** `unreachable`.

## 4. Span location — absent

Line-based search, then cross-line/tag-folded search over the whole byte stream:

```
$ grep -c -- 'スキルのインストール' archive.html
0
$ tr '\n' ' ' < archive.html | grep -o -- 'スキルの.\{0,12\}インストール' | sort | uniq -c      # (no output)
$ tr '\n' ' ' < archive.html | grep -oE -- 'スキルの(<[^>]*>|[[:space:]])*インストール' | sort | uniq -c   # (no output)
$ grep -o -- 'スキルの.\{0,20\}' archive.html | sort -u
スキルのインデックスを作成します。</p>
スキルの検証</th>
```

The only `スキルの…` continuations on the page are the troubleshooting sentence and a table cell
(`<th style="text-align: left">スキルの検証</th>`, line 1619). Full heading enumeration of the
snapshot (`grep -o '<h[1-4][^>]*>[^<]*</h[1-4]>'`), in page order:

```
[h2] Gemini Docs MCP を接続する
[h2] API 開発スキルを追加する
[h3] gemini-api-dev
[h4] skills.sh でインストールする
[h4] Context7 でインストールする
[h3] gemini-live-api-dev
[h3] gemini-interactions-api
[h2] インストールを確認する
[h3] 1. エージェントの動作を確認する
[h3] 2. マニフェストとツールを確認する
[h2] トラブルシューティング
[h3] エージェントがスキルを検出できなかった
[h3] グローバルとローカルの競合
[h2] リソース
```

Nearest real heading to the staged quote's subject, and its `sed` output:

```
$ sed -n '1531p' archive.html
<h2 data-text="API 開発スキルを追加する" id="available-skills" tabindex="-1">API 開発スキルを追加する</h2>
$ sed -n '1535p' archive.html
<p>これらのスキルをインストールするには、次のいずれかのサポートされているツールを使用します。両方のインストール手順は、各スキル モジュールの下に記載されています。</p>
```

Folds tested and **rejected**: (a) whitespace fold — `スキルの インストール`, `スキルの\nインストール`
both 0 hits; (b) markdown/HTML-tag fold — `スキルの<tag>インストール` 0 hits; (c) paraphrase of the
existing h4s 「skills.sh でインストールする」/「Context7 でインストールする」 — particle and form
differ (`スキルをインストールする` vs `スキルのインストール`), so it is not a fold of those headings;
(d) table-header fold — the verify table's cell is `スキルの検証`, not `スキルのインストール`.

## 5. Variants of the same page, all span-free

| variant | command target | status / final | size | sha256 (first 12) | span |
|---|---|---|---|---|---|
| cited archive `web/2026/…?hl=ja` | as above | 200 / `20260908032619` | 113 449 | `1b9ea838f374` | 0 |
| June snapshot `20260608145637…?authuser=0&hl=ja` | `curl -sSL -A 'Mozilla/5.0' 'https://web.archive.org/web/20260608145637/https://ai.google.dev/gemini-api/docs/coding-agents?authuser=0&hl=ja'` | 200 / same | 108 746 | `8d691986cb5b` | 0 |
| live `?hl=ja` HTML | `curl -sSL -A 'Mozilla/5.0' 'https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja'` | 200 / same | 122 506 | `61cd2819da49` | 0 |
| live `.md?hl=ja` export | `curl -sSL -A 'Mozilla/5.0' 'https://ai.google.dev/gemini-api/docs/coding-agents.md?hl=ja'` | 200 / same | 122 510 | `11037c3f1807` | 0 |
| archived English page | `curl -sSL -A 'Mozilla/5.0' 'https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents'` | 200 / `20261023092329` | 121 174 | `5591770cd485` | n/a (EN) |

- June snapshot headings are `[h4] skills.sh を使用してインストールする` / `[h4] Context7 を使用してインストールする`
  — same structure, still no `スキルのインストール`.
- Live Japanese page heading for the same section (line 2175):
  `<h2 data-text="Gemini エージェント スキルをインストールする" id="available-skills" …>` — again not the quoted span.
- The `.md` export is **not** a markdown rendering: `grep -n '^#' live-ja.md` returns nothing and its
  size is within 4 B of the live HTML, i.e. `.md` serves the same HTML. Recording this so no later
  seat treats `.md` as an independent text source.
- Archived `.md` form (`https://web.archive.org/web/2026/…/coding-agents.md?hl=ja`) → HTTP 404, 4 651 B
  (`5c2cd7bd2be6…`), so the archive has no `.md` capture at all.
- English archive headings: `Install Gemini agent skills`, `Available skills`, `Mount skills in Managed
  Agents`, … — the English page has no heading equivalent to `スキルのインストール` either.

## 6. What *is* present: S260's own payload quote

```
$ grep -n -- 'llms\.txt</code> を取得します' archive.html
1533:<p>このスキルは、アシスタントのコンテキストに<strong>組み込みのルールとベスト プラクティス</strong> … 両方がインストールされている場合、このスキルはドキュメントに MCP サービスを使用しますが、MCP がインストールされていない場合でも、フォールバックとして <code dir="ltr" translate="no">ai.google.dev</code> から <code dir="ltr" translate="no">llms.txt</code> を取得します。</p>
```

Line 1533, anchor heading 「API 開発スキルを追加する」 (`h2`, `id="available-skills"`, line 1531).
Pasted span (dropped bytes: the two `dir="ltr" translate="no"` attribute sets and the clause before
`MCP がインストールされていない場合でも`):

> `MCP がインストールされていない場合でも、フォールバックとして <code …>ai.google.dev</code> から <code …>llms.txt</code> を取得します。`

That is the staged quote with tags flattened — so the staged row's *payload* verifies; only its
section label 「スキルのインストール」 does not.

## 7. Local-artifact leg of the register row

```
$ ls -l corpus/knowledge/japanese-first-party-skill-sources.md
ls: cannot access 'corpus/knowledge/japanese-first-party-skill-sources.md': No such file or directory
$ grep -rln 'ai\.google\.dev' corpus/
corpus/lessons/round-68.md
$ grep -rn -- 'スキルのインストール' corpus/
(no output)
```

S260's artifact cell points at a path the lane does not hold, and no lane corpus file contains the
quoted span. The only lane text carrying S180 is the prior lesson:

```
$ sed -n '106p' corpus/lessons/round-68.md
| S180 | payload-absent | web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja | refused — the quoted span was not located on the page this round fetched |
```

Independent round-68 verdict agrees with mine; my check adds the June snapshot, live HTML, live
`.md`, English archive and the fold tests, which round 68 did not record.

## 8. Side finding — the staged row's live-address note is stale

```
$ curl -sS -A 'Mozilla/5.0' -o /dev/null -L --max-redirs 12 -w 'HTTP=%{http_code} FINAL=%{url_effective} REDIRECTS=%{num_redirects}\n' 'https://ai.google.dev/gemini-api/docs/coding-agents'
HTTP=200 FINAL=https://ai.google.dev/gemini-api/docs/coding-agents REDIRECTS=0
```

S260 (and S249, whose title cell my grep shows as "live URL redirects in a loop; content read from the
Internet Archive snapshot") state the live address "redirects in a loop and is not reachable".
On 2026-10-25 it answers 200 with zero redirects. This does not change row 6's verdict (the span is
still absent), but it does mean the "unreachable" scoping in S249/S260 needs re-derivation before
any append. CDX check (`cdx/search/cdx?url=ai.google.dev/gemini-api/docs/coding-agents&matchType=prefix&from=2026&to=2026&collapse=digest&limit=60`,
6,353 B, sha256 `a2896d43d560…`): the returned 60-row slice contains exactly one `hl=ja` capture,
`20260608145637 … ?authuser=0&hl=ja`. The cited `web/2026/` form resolves to `20260908032619`
(per the fetch's final URL), which is **not** in that 60-row slice — the slice was capped at
`limit=60`, so I do not claim the capture list is complete.

## Verdict line for the lesson

`S180 | absent (fabrication class) | web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja`
→ refuse the row; the quoted span `スキルのインストール` is a section label that no capture of the page
carries (nearest real heading: 「API 開発スキルを追加する」, snapshot 20260908032619 line 1531). Do **not**
drop staged S260: its payload quote verifies at line 1533, and its artifact cell needs repointing
(`corpus/knowledge/japanese-first-party-skill-sources.md` is absent).

## Bounds / hygiene

- Read-only on the lane: no committed lane file touched; this report is the only write.
- Scratch `/tmp/k72w1-ExecQuar06.h2x8` (fetched bytes only), deleted before return.
- No git/jj mutation, no fixture repo, no gate run, no subagent dispatch. No tool installed.
- Concurrency: single curl per call, longest 6.2 s (CDX), all under the 120 s cap.
