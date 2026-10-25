# ExecQuar08 — quarantine hand-check, register slice row 8 of 13

**Verdict: `unverifiable-class`** (addendum §10 vocabulary; NOT fabrication). Register row 8 carries a
**prose class cell**, not a quote: `the cited source could not be fetched, so no quote was checked`.
There is no source span in the row to locate, so the row itself can be neither adopted nor refused as
a fabrication. **Do not adopt the row as written; do not refuse it as fabrication.**

**Staged id for the cited URL (host+path `skills.sh/docs`): `S316`** —
`/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:120`, corroborated by
`/home/vgpnk/Projects/shokuknow/lanes/kotoba/ID-REMAP.md:25` (`round10 | S243 | S316`). The
campaign id `S236` is **not** the staged id and not even the current pre-renumber id (three id epochs,
§3).

**Calibration, and the one thing that matters for the L1:** the row's premise is **false**. The
census that produced it had the page on disk — its own cache holds a body **byte-identical** to the
one I fetched today (sha256 `54828058…` both, §6) — and the census's own matcher, re-run today
against that cache and the census-time source file, scores the recovered campaign quote **`exact`**,
twice (§6). The underlying campaign row (round10 `S236`, staged `S316`) is therefore
**present**, anchored at **"How are you securing skills?"**, quote *"We encourage you to review
skills before installing and use your own judgment."* — 13 words (`printf … | wc -w` → `13`),
located at byte **12352** of the served body (§5). Adoption still needs an entry the lane does not have (§7).

## 1. The register row, as read (byte-exact)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-72/assimilation
$ sed -n '8p' quarantine-slice-full.txt
| `kotoba` | round10 | S236` | the cited source could not be fetched, so no quote was checked | https://skills.sh/docs |
```

Slice row 8 is byte-identical to register line 327 of the campaign register (nothing dropped, no
fold applied):

```
$ sed -n '8p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt > slice8.txt
$ sed -n '327p' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md > reg327.txt
$ cmp slice8.txt reg327.txt && echo CMP=identical
CMP=identical
$ sha256sum slice8.txt reg327.txt
1259ab9581a30dda17bbd7db4740e5ad03ef056b6efabd2b0277da63442cdc1b  slice8.txt
1259ab9581a30dda17bbd7db4740e5ad03ef056b6efabd2b0277da63442cdc1b  reg327.txt
```

Cell structure — **five** cells under a **seven**-column header, a stray backtick after the id, and a
prose why-note where the class token would be:

```
$ sed -n '327p' absent-defect-register.md | awk -F'|' '{print "cells="NF-2; for(i=2;i<NF;i++) printf "  $%d=[%s]\n", i-1, $i}'
cells=5
  $1=[ `kotoba` ]
  $2=[ round10 ]
  $3=[ S236` ]
  $4=[ the cited source could not be fetched, so no quote was checked ]
  $5=[ https://skills.sh/docs ]
```

The quoted span under test is therefore the register's own why-note, present verbatim at register
line 327 (that is the only place it exists to be found — it is not a source quotation).

## 2. Why the cell is prose: the generator, not the row

These six kotoba rows are emitted by a different branch than the classed rows, and the branch has a
template defect:

```
$ grep -n 'r\[.id.\]}` | {r\[.note.\]}' absent-defect-register.py
160:        out.append(f"| `{r['lane']}` | {r['round']} | {r['id']}` | {r['note']} | "
```

The `}` after `{r['id']}` is a literal backtick — that is the `S236\`` artifact. The column header
for that branch is `why it was not checked`, not `class`:

```
$ sed -n '256,263p' absent-defect-register.md
## Rows whose quotes were NEVER CHECKED
…
rows: **109**

| lane | round | id | why it was not checked | cited source |
```

The class the generator would have assigned is `unreachable`, and the register's own legend defines
it as *not* a fabrication:

```
$ sed -n '14p' absent-defect-register.md
| `unreachable` | the source could not be fetched, so the quote was never checked | re-fetch, or mark the row unverifiable — do NOT call it a fabrication |
$ sed -n '18p' absent-defect-register.md
- rows with at least one ABSENT quote: **194**
```

The Totals table counts only `payload-absent` rows (194); the 109 never-checked rows sit outside its
taxonomy. Six of the 109 are kotoba (`awk 'NR>262 && /^\| `/' … | grep -c kotoba` → `6`).

## 3. Staged row by URL, and three id epochs

```
$ grep -n 'skills\.sh/docs' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md | cut -c1-150
120:| S316 | skills.sh — Documentation, the answer on securing skills — https://skills.sh/docs | docs | B | …
$ sed -n '25p' /home/vgpnk/Projects/shokuknow/lanes/kotoba/ID-REMAP.md
| round10 | `S243` | `S316` |
```

The staged row's anchor cell is `the "How are you securing skills?" section, at the sentence advising
installers` — an anchor, not a literal quote; its `used-by` is
`corpus/knowledge/installer-security-guidance-round10.md`.

Ids, three epochs, each verified against its own artifact:

| epoch | artifact | round-10 block | docs row |
|---|---|---|---|
| census snapshot | `git show 1d7d66b3:lanes/kotoba/round10/SOURCES-PROPOSED.md` (12 rows) | `S235`…`S246` | **`S236`** (line 17) |
| renumber input | `ID-REMAP.md:24-35` "was" column | `S242`…`S253` | `S243` |
| current / staged | `lanes/kotoba/round10/SOURCES-PROPOSED.md` (12 rows) + `SOURCES.append.md` | `S315`…`S326` | **`S316`** (line 17) |

```
$ grep -o '^| S[0-9]\{3\}' r10-at-census.md | head -2 ; … | tail -2
| S235
| S236
| S245
| S246
$ grep -o '^| S[0-9]\{3\}' lanes/kotoba/round10/SOURCES-PROPOSED.md | head -2 ; … | tail -2
| S315
| S316
| S325
| S326
```

The register's `S236` is the **census-snapshot** id, which is neither the remap's `was` nor the staged
id. The URL is the only sound join — an id join silently lands on a different row (staged `S236` is
`agentskills.io/skill-creation/using-scripts.md`, `SOURCES.append.md:40`). Round 70's scout reached
the same conclusion for one pair (`w1/ScoutQuarantine.md` §F5); this is the full arithmetic for the
block: snapshot `S235`→current `S315` is a constant +80.

## 4. Fetch record — the cited URL

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-25T21:37:02Z
$ curl -fsSL -A 'Mozilla/5.0' -o skills-sh-docs.html -w 'HTTP=%{http_code}\nFINAL=%{url_effective}\nSIZE=%{size_download}\nCT=%{content_type}\n' 'https://skills.sh/docs'
HTTP=200
FINAL=https://www.skills.sh/docs
SIZE=44245
CT=text/html; charset=utf-8
$ sha256sum skills-sh-docs.html
5482805850e94ed3187449118c8f7c4b61f3b2614b745b42ff4373238228754b  skills-sh-docs.html
```

Access date **2026-10-25** (server `date: Sun, 25 Oct 2026 21:38:43 GMT`), HTTP **200**,
final URL `https://www.skills.sh/docs`, **44,245 bytes**, sha256 `54828058…`, `text/html`.

Redirect chain is one Vercel hop, and a fetcher that does not follow it sees no page at all:

```
$ curl -sSI -A 'Mozilla/5.0' 'https://skills.sh/docs'
HTTP/2 308
content-type: text/plain
location: https://www.skills.sh/docs
refresh: 0;url=https://www.skills.sh/docs
server: Vercel
$ curl -sS -A 'Mozilla/5.0' -o nofollow.bin -w 'code=%{http_code} size=%{size_download}\n' 'https://skills.sh/docs'
code=308 size=15
$ xxd nofollow.bin | head -1
00000000: 5265 6469 7265 6374 696e 672e 2e2e 0a    Redirecting....
```

`.md` export (the assignment's alternate form) does not exist here; the URL is not a
`web.archive.org` redirect, so no archive form applies:

```
$ curl -sS -A 'Mozilla/5.0' -L -o docs-md.out -w 'code=%{http_code} final=%{url_effective} size=%{size_download}\n' 'https://skills.sh/docs.md'
code=404 final=https://www.skills.sh/docs.md size=21076
```

## 5. Span location — the recovered campaign quote is present

The row has no quote, but the campaign row behind it does, and I recovered it from the census-time
source file the census actually read:

```
$ git show 1d7d66b3:lanes/kotoba/round10/SOURCES-PROPOSED.md > r10-at-census.md
$ grep -n -A6 'Gate — S236' r10-at-census.md
38:## Gate — S236
39-
40-- URL: https://skills.sh/docs
41-- Opened: 2026-10-24
42-
43-> "We encourage you to review skills before installing and use your own judgment."
```

**Served bytes, 2026-10-25.** The document is a single line (`sed -n '1p' … | wc -c` → `44245`), so
offsets, not line numbers, are the locator; the pasted spans are substrings of line 1 and everything
outside them is dropped:

```
$ sed -n '1p' skills-sh-docs.html | grep -o '<h2[^>]*>How are you securing skills?</h2>'
<h2 class="text-2xl font-semibold tracking-tight mb-2">How are you securing skills?</h2>
$ sed -n '1p' skills-sh-docs.html | grep -o 'We encourage you to review skills before installing and use your own judgment\.</p>'
We encourage you to review skills before installing and use your own judgment.</p>
```

Offsets (each string occurs twice — once in the rendered section, once in the Next.js RSC payload;
both are served bytes, no fold applied):

```
heading  offsets [11758, 40850]
sentence offsets [12352, 41630]
```

Anchor: `<h2>` **How are you securing skills?**, sentence in the muted box beneath it.
**Verdict on the recovered quote: `present`** (exact, no fold). The register row itself remains
`unverifiable-class` because it carries no quote to check.

## 6. Calibration — the `fetch-failed` verdict is false, reproducibly

The census's own negative/positive cache holds the page, fetched **11 s before** the census JSON was
written, and it is byte-identical to today's fetch:

```
$ stat -c '%y %s %n' .qcache/14e9af26cf6b7a8c0d38f9c9.raw .qcache/14e9af26cf6b7a8c0d38f9c9.txt quote-lint-full-v5.json
2026-10-24 08:05:13.488300012 -0300 44245 .qcache/14e9af26cf6b7a8c0d38f9c9.raw
2026-10-24 08:05:13.490065692 -0300 2593 .qcache/14e9af26cf6b7a8c0d38f9c9.txt
2026-10-24 08:05:24.867276155 -0300 quote-lint-full-v5.json
$ sha256sum skills-sh-docs.html .qcache/14e9af26cf6b7a8c0d38f9c9.raw
5482805850e94ed3187449118c8f7c4b61f3b2614b745b42ff4373238228754b  skills-sh-docs.html
5482805850e94ed3187449118c8f7c4b61f3b2614b745b42ff4373238228754b  .qcache/…raw
$ cmp skills-sh-docs.html .qcache/14e9af26cf6b7a8c0d38f9c9.raw && echo CMP=identical
CMP=identical
```

The cached text carries both spans (line numbers from the cache file, `sed -n` pastes):

```
$ grep -n 'securing skills\|We encourage' .qcache/14e9af26cf6b7a8c0d38f9c9.txt
26: [![skills.sh](https://skills.sh/b/anthropics/skills)](https://skills.sh/anthropics/skills) How are you securing skills?
28: We do our best to maintain a safe ecosystem, … We encourage you to review skills before installing and use your own judgment.
```

And the census's own functions, run today against the census-time file and the census's cache (no
network, no write), return `exact` — not `fetch-failed`:

```
$ PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY'   # imports quote-lint.py, uses its own parse_rows/
                                               # parse_gate_blocks/bind_blocks/block_url/cached_text/match
row id S236 explicit_binding True
block_url -> 'https://skills.sh/docs'
cache_path exists -> True
cached_text -> 2593 chars
block_quotes -> [('> "We encourage you to review skills before installing and use your own judgment."', [('We encourage you to review skills before installing and use your own judgment.', 'literal')]), ('Anchor: the "How are you securing skills?" section, at the sentence advising installers.', [('How are you securing skills?', 'literal')])]
quote 'We encourage you to review skills before installing and use your own judgment.' kind literal match -> exact
quote 'How are you securing skills?' kind literal match -> exact
```

(`block_quotes` pasted whole, not elided.)

The recorded finding, for contrast (`quote-lint-full-v5.json`, finding index 700) — no `quote` field,
verdict `fetch-failed`, detail = the URL whose body was on disk:

```
700 {"lane": "kotoba", "round": "round10", "id": "S236", "verdict": "fetch-failed", "detail": "https://skills.sh/docs"}
```

`fetch-failed` is emitted only when `cached_text(url)` returns `None` (`quote-lint.py:799-802`), and
`cached_text` never touches the network (`quote-lint.py:441-451`). **Mechanism: [INFERENCE]** — the
verdict is a stale/negative-cache artifact of an earlier pass, not a statement about the source: I
cannot reproduce it from the artifacts, and a concurrent second census run could also explain the
mtimes. What is observed, not inferred: the census held the exact bytes and the exact quotes at
08:05 on 2026-10-24, and 11 s later wrote a JSON calling that URL unfetchable.

## 7. Consequences for the lane (blockers, not verdicts)

- **The staged row's `used-by` entry does not exist in the lane.** `S316` points at
  `corpus/knowledge/installer-security-guidance-round10.md`;
  `ls -l corpus/knowledge/installer-security-guidance-round10.md` → `No such file or directory`
  (the only round-10 entry present is `harness-verifier-round10.md`). Under C1's predicate (b)/(c)
  the row cannot be appended as-is.
- **The lane holds no skills.sh row at all:** `grep -c 'skills\.sh' corpus/SOURCES.md` → `0`; the
  lane's highest id is `S213`. Any adoption is a new row plus a new entry, not a re-point.
- **Round 68 already reached the same class for the same reason:**
  `corpus/lessons/round-68.md:109` → `| S236 | unreachable | skills.sh/docs | unverifiable — same
  class |`. The class was right; the reason is now demonstrably wrong.
- **Register-level defect worth a lesson row:** a never-checked row is printed with its why-note in
  the class column and a stray backtick in the id cell (`absent-defect-register.py:160`), so a
  reader — or an automated slice consumer — can read "could not be fetched" as a finding about the
  source when it is a finding about the checker's cache.

## Risks / limits of this check

- Verdict is a statement about bytes I fetched on 2026-10-25 and about the census's cache on
  2026-10-24, not about the page as of round 10.
- The row has no quote; the `present` result above belongs to the recovered campaign quote, which I
  took from the census-time source file, not from the register row.
- I did not re-check the other five kotoba never-checked rows (S237, S238, S239, S243, S169) — other
  seats own them; the same cache mechanism may affect them.
- Tooling: nothing installed, no pacman transaction, no host service touched. Scratch
  `/tmp/k72w1-ExecQuar08.b2BX` used for fetches and deleted before return; no lane file modified.
