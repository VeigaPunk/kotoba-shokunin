# ExecQuar12 — quarantine hand-check, register slice row 12 of 13

**Verdict: `unverifiable-class` — NOT fabrication. Not adopted. Retire the row as superseded by
staged `S323`.**

The row carries **no quoted span**. Its class cell is the prose form "the cited source could not be
fetched, so no quote was checked", which the register's own legend defines as `unreachable` — a class
whose reader action is "re-fetch, or mark the row unverifiable — do NOT call it a fabrication"
(`absent-defect-register.md:14`). Per addendum §10 the row is therefore `unverifiable`, not a
fabrication, and nothing from it is appended.

Second measured fact, which changes the *disposition* but not the verdict: the cited URL answers
today (308 → 200, 138,514 bytes) and the staged package already holds two `mined` rows on the same
host+path (`S323`, exact URL; `S367`, `www` form). The `unreachable` premise is stale, so the row is
re-derivable rather than merely unverifiable: it is superseded, not pending.

All commands below were run by this seat on 2026-10-25; scratch `/tmp/k72w1-ExecQuar12.s7kA`
(created with `mktemp -d /tmp/k72w1-ExecQuar12.XXXX`, deleted at the end). No lane file was touched.

## 1. The row, as read

```
$ cd .../.ufo/waves/round-72/assimilation && wc -l quarantine-slice-full.txt && sed -n '12p' quarantine-slice-full.txt
13 quarantine-slice-full.txt
| `kotoba` | round10 | S243` | the cited source could not be fetched, so no quote was checked | https://skills.sh/docs/api |
```

`od -c` on the same line confirms the id cell is ``S243` `` (an **unmatched** backtick after the id),
and that the 4th cell is plain prose, not a backtick-delimited quote:

```
0000000   |       `   k   o   t   o   b   a   `       |       r   o   u
...
0000020   n   d   1   0       |       S   2   4   3   `       |       t
```

The slice is a verbatim copy of the canonical register row
`/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:331`
(identical bytes, same stray backtick), so the defect is in the register, not in the slice derivation:

```
$ sed -n '331p' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md
| `kotoba` | round10 | S243` | the cited source could not be fetched, so no quote was checked | https://skills.sh/docs/api |
```

Field dump against the register's 7-column header (`lane | round | id | class | cited source |
quote(s) | note`, line 30) shows only five populated cells — **there is no quote cell and no note
cell** on this row:

```
$ awk -F'|' 'NR==331{for(i=1;i<=NF;i++){v=$i; gsub(/^ +| +$/,"",v); printf "f%d=[%s]\n", i-1, v}}' <register>
f1=[`kotoba`]
f2=[round10]
f3=[S243`]
f4=[the cited source could not be fetched, so no quote was checked]
f5=[https://skills.sh/docs/api]
f6=[]
```

So `f4` is the **class** cell (prose spelling of `unreachable`), `f5` is the **cited source**. Nothing
in this row claims any text was ever in the page — the row asserts only that a fetch failed.

## 2. Staged lookup by URL (host+path)

The staged package `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md` holds **two**
`mined` rows on this host+path, and **no row under the register's id `S243`**:

```
$ grep -n 'skills\.sh/docs/api' SOURCES.append.md
127:| S323 | skills.sh — API Reference — https://skills.sh/docs/api | docs | B | ...
171:| S367 | skills.sh — API Reference — https://www.skills.sh/docs/api | docs | B | ...
$ grep -c 'skills\.sh/docs/api' SOURCES.append.md
2
```

| staged id | URL | status | retrieved | used-by |
|---|---|---|---|---|
| `S323` | `https://skills.sh/docs/api` (exact) | `mined` | 2026-10-24 | `corpus/knowledge/registry-total-round10.md` |
| `S367` | `https://www.skills.sh/docs/api` (www form, same path) | `mined` | 2026-10-24 | `corpus/knowledge/leaderboard-count-round15.md` |

Staged id for this row: **`S323`** (with `S367` on the `www` form). Not `not staged`.

**Id collision (F4 below):** the staged `S243` is a different source entirely —
`SOURCES.append.md:47` `| S243 | Rethinking Self-Evolving Agent Skills: Feedback Dynamics over
Multiple Rounds — https://arxiv.org/abs/2608.02636 | paper | ...` — and `S243` is in the kotoba
`staged-ids` list (`.../assimilation/staged-ids`). Adopting the register row "as S243" would collide
with a mined row; the register id and the lane registry id are different id spaces.

## 3. Fetch record (cited URL)

```
$ curl -sSL -A 'Mozilla/5.0' -o api.html -w 'HTTP=%{http_code} FINAL=%{url_effective} BYTES=%{size_download} CT=%{content_type}\n' 'https://skills.sh/docs/api'
HTTP=200 FINAL=https://www.skills.sh/docs/api BYTES=138514 CT=text/html; charset=utf-8
$ sha256sum api.html ; date -u +%Y-%m-%dT%H:%M:%SZ
fe7da4732661eb068ee22708cd1e814a1aa67ba85e936498c63585b225c23d13  api.html
2026-10-25T21:37:32Z
```

| field | value |
|---|---|
| access date | 2026-10-25 (21:37Z and 21:41Z) |
| first hop | `HTTP/2 308`, `location: https://www.skills.sh/docs/api`, `server: Vercel` |
| final URL | `https://www.skills.sh/docs/api` |
| status | `200` |
| bytes | 138,514 |
| sha256 | `fe7da4732661eb068ee22708cd1e814a1aa67ba85e936498c63585b225c23d13` |
| stability | second fetch byte-identical (`cmp -s api.html api2.html` → `IDENTICAL=yes`, same sha) |

Alternate forms tried (the URL is **not** a `web.archive.org` redirect; both were attempted anyway):

| form | result |
|---|---|
| `https://skills.sh/docs/api.md` | `HTTP=404 FINAL=https://www.skills.sh/docs/api.md BYTES=22822` |
| `https://www.skills.sh/docs/api.md` | `HTTP=404 ... BYTES=22822` (identical body, sha256 `3a3f9f61…`) |
| `https://www.skills.sh/llms.txt` | `HTTP=404 ... BYTES=21086` |
| `https://web.archive.org/web/2026/https://skills.sh/docs/api` | `HTTP=200 FINAL=https://web.archive.org/web/20260917175802/https://www.skills.sh/docs/api BYTES=141125`, sha256 `3f4139fb05105a50286d56cedbffafb577edf3f9e67921fcb1a445792247727c` |
| `https://archive.org/wayback/available?url=skills.sh/docs/api` | `429 Too Many Requests` (API throttled; the direct snapshot above answered) |

The archived snapshot is dated **2026-09-17 17:58:02**, i.e. the page was publicly archived before the
staged rows were mined — the class premise is not reproducible (F3).

## 4. Quoted span and anchor

There is **no quoted span to locate** — the cell is prose (§1). What can be located is the **anchor
named by the staged row on this same URL**, `S323`: "the introductory paragraph above the
authentication section". Both readings of that anchor exist in the fetched bytes.

Fold named: the page is server-rendered HTML; the doc markup sits on **line 1** of the 134-line body,
so a `sed -n '<L>p'` locator is useless here and I give byte offsets as well. The extraction below is
`sed -n '1p' | grep -o` (contiguous text copied from the fetched bytes; the only bytes dropped are the
HTML tags between the quoted words, named inline).

```
$ sed -n '1p' api.html | grep -o -E 'Programmatic access to the skills\.sh skill catalog, leaderboard, and search\.'
Programmatic access to the skills.sh skill catalog, leaderboard, and search.
```
→ line 1, byte offset **8422** (second render at 72315). This is the page's own introductory
paragraph (under the `API Reference` h1).

```
$ sed -n '1p' api.html | grep -o -E 'All endpoints are under.{0,150}Responses are JSON\.'
All endpoints are under <code class="px-1.5 py-0.5 bg-muted rounded text-sm font-mono">/api/v1/</code> and served over HTTPS. Responses are JSON.
```
→ line 1, byte offset **8751**; this paragraph sits **directly above** the Authentication heading.
Dropped bytes: the single `<code …>` tag pair around `/api/v1/`.

```
$ sed -n '1p' api.html | grep -o -E 'tracking-tight mb-2">Authentication</h2>'
tracking-tight mb-2">Authentication</h2>
```
→ line 1, byte offset **9014** (second render at 37759). The same two paragraphs are present in the
2026-09-17 archive snapshot (`grep -o -E 'All endpoints are under.{0,120}' wb.html` matched), so the
anchor is not a fresh-page artifact.

Anchor for this row: **n/a — no quote**; anchor for the superseding staged row `S323`: the intro
paragraph(s) above the `Authentication` section, located as above.

## 5. Verdict and disposition

| question | answer |
|---|---|
| quoted span present? | none exists in the row (prose class cell) |
| present / after-fold / absent | not applicable |
| unreachable | **not today** — HTTP 200, twice, byte-identical |
| class verdict | **`unverifiable-class`** (register class `unreachable`; not fabrication) |
| adopt with anchor? | **no** — nothing to adopt, no quote |
| disposition | retire as **superseded by staged `S323`** (same host+path, `mined`, used-by `corpus/knowledge/registry-total-round10.md`); do not append the register row, do not re-use its id |

Prior lane records agree and were **not** relied on — re-verified from the register and the live URL
myself: `corpus/lessons/round-68.md:113` `| S243 | unreachable | skills.sh/docs/api | unverifiable —
same class |` and `corpus/lessons/round-70.md:112` (six "could not be fetched" rows including S243).
The lane corpus holds **no** `S243` entry row: `grep -rn 'S243' corpus/` returns only those two lesson
tables.

## 6. Findings

**F1 — the register's prose-class rows carry a malformed id cell (systematic, 78 rows).** Every
`unreachable`-class row's id cell ends in an unmatched backtick; no `payload-absent` row does:

```
$ awk -F'|' '/could not be fetched, so no quote was checked/ && /^\| `/{id=$4; gsub(/^ +| +$/,"",id); if (id ~ /`$/) n++} END{print n+0}' <register>
78
$ awk -F'|' '/`payload-absent`/ && /^\| `/{id=$4; gsub(/^ +| +$/,"",id); if (id ~ /`$/) n++} END{print n+0}' <register>
0
```
Consequence: a hand-check that keys on a backtick-delimited id (`grep -F '`S243`'`) silently skips
**all 78** unreachable rows — this seat's row among them. The class cell is likewise plain prose
instead of a backticked class token, so no tool can classify these rows without a prose match.

**F2 — the register's Totals block does not account for the prose-class rows.** The header claims
"rows with at least one ABSENT quote: **194**" and its class table lists only `payload-absent | 194`;
the Rows table actually holds 330 data rows, 78 of them the unreachable prose class and 31 the
"gate block named no locator" class:

```
$ awk -F'|' '/^\| .[a-z0-9-]+. \|/{n++; c=$5; gsub(/^ +| +$/,"",c); if(c=="\x60payload-absent\x60") pa++; else if(c ~ /could not be fetched/) ur++; else if(c ~ /gate block named no locator/) gn++; else other++} END{printf "rows=%d payload-absent=%d unreachable-prose=%d gate-no-locator=%d other=%d\n", n, pa, ur, gn, other}' <register>
rows=330 payload-absent=194 unreachable-prose=78 gate-no-locator=31 other=27
```
The 194 figure is honest for quoted rows; the point is that the register cannot be used to size the
quarantine load, and a slice reader gets no class table for the 109 unquoted rows.

**F3 — the row's class premise is stale and was already false at archive time.** The URL answers
`200` today (§3) and the Wayback snapshot of **2026-09-17** carries the same `Authentication` section
and the same intro paragraph. So `unreachable` is a record-vs-tree defect in the register: a
"could not be fetched" verdict that a re-fetch does not reproduce. Reader action per the register's
own legend is "re-fetch, or mark the row unverifiable" — both were done here; the re-fetch succeeded,
so the row is re-derivable and should be retired in favour of `S323`/`S367` rather than left as debt.

**F4 — id-space collision risk if the row is adopted by id.** Staged `S243`
(`SOURCES.append.md:47`, arXiv 2608.02636, `mined`) and register `S243` are unrelated, and `S243` is
already in the kotoba `staged-ids` list. Any lesson line that says "adopted S243" would be ambiguous
between the two. Nothing was appended from this row.

**Not a finding / recorded as unobserved:** the page's `.md` export and `llms.txt` both 404, so the
only machine-readable copy is the HTML (plus the archive snapshot). The archive availability API
returned 429 on one call; the direct snapshot URL succeeded, so no conclusion rests on the 429.

## 7. Scope

- Files written: this report only. No committed lane file, register, staged package or fleet file was
  modified; no git/jj command was run.
- Scratch `/tmp/k72w1-ExecQuar12.s7kA` (6 fetched bodies + headers) deleted before return; every
  command and its observed output is pasted above.
- Tooling: none installed or upgraded.
