# ExecQuar13 — quarantine hand-check, register slice row 13 of 13 (S169 / ai.google.dev)

**Verdict: `unverifiable-class`** — row 13's quote cell is a prose class cell ("the cited source could
not be fetched, so no quote was checked"), not a quote, so there is nothing to locate and the row is
**not** fabrication. Calibration finding on top of the verdict: the class cell's stated reason is
**false as of 2026-10-25** — the cited URL now returns HTTP 200 with no redirects, and the page carries
the exact sentence the staged sibling row S249 quotes. The row's verdict stays `unverifiable` (no
quote in the cell), but its `unreachable` premise no longer holds.

## F1 — the row, byte-exact, and its shape

```
$ cd .../round-72/assimilation && wc -l quarantine-slice-full.txt
13 quarantine-slice-full.txt
$ sed -n '13p' quarantine-slice-full.txt
| `kotoba` | round5 | S169` | the cited source could not be fetched, so no quote was checked | https://ai.google.dev/gemini-api/docs/coding-agents |
$ sed -n '13p' quarantine-slice-full.txt | wc -c
149
$ sed -n '13p' quarantine-slice-full.txt | sha256sum
6bdaeff291ff4e94256b1ee7e31be90129c1eea357bdff942e8a01fe9e264004  -
```

- `cat -A` shows no trailing whitespace; the line ends `|$`.
- Shape defect, unchanged from the other five prose rows: the campaign id carries a stray closing
  backtick (`S169\``) while the quote cell has **no** opening backtick — the same artefact
  `CritMistakeSweep` recorded for rows S236–S243 in round 69
  (`.ufo/waves/round-69/w1/CritMistakeSweep.md:134,142`). This is a formatting artefact, not evidence
  of a lost quote: the cell text is a complete sentence with its own full stop.

## F2 — `S169` is a campaign id, not a staged id; the staged row by URL is **S249**

```
$ grep -c -w 'S169' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
0
$ sha256sum /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
e2bdff3fe7b1a44bc764f180c6bda2ba73e9c625bbe9dd28eec3d9cef7090aaf  SOURCES.append.md   (175885 B, mtime Oct 24 23:33)
$ grep -n -i "ai.google.dev/gemini-api/docs/coding-agents" SOURCES.append.md
53:| S249 | Google — Coding agent setup & developer resources (live URL redirects in a loop; content read from the Internet Archive snapshot) — https://ai.google.dev/gemini-api/docs/coding-agents — archived at https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents | docs | B | ...
64:| S260 | Google — Gemini API：コーディング アシスタントの設定（日本語） — https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents?hl=ja — the live address `https://ai.google.dev/gemini-api/docs/coding-agents` redirects in a loop and is not reachable | docs | B | ...
```

- **Staged id for row 13's URL (host+path `ai.google.dev/gemini-api/docs/coding-agents`): `S249`**
  (line 53) — exact URL match, English page. Sibling `S260` (line 64) is the `?hl=ja` archive variant,
  same path with a query, and is the staged counterpart of register row S180, not of row 13.
- S249's own quote, read at line 53: "Skills come pre-installed in Google AI Studio Build and are
  bundled in the Gemini API plugin for Antigravity." (19 words, copied from the staged bytes; nothing
  dropped). S249 cites the archive as its retrieval surface and states the live URL "serves a redirect
  loop".
- Consequence for the lane: row 13's URL is already carried by a staged row, so re-sourcing row 13
  would append no new document — it would duplicate S249 (the same relation round 70 found for S151→S210,
  `.ufo/waves/round-70/w1/ScoutQuarantine.md:57`).

## F3 — fetch of the cited URL: HTTP 200, no redirect loop, content present

Commands run in `D=$(mktemp -d /tmp/k72w1-ExecQuar13.XXXX)` (`/tmp/k72w1-ExecQuar13.Q9JF`), all with
`-A 'Mozilla/5.0' --max-time 60`, access date **2026-10-25** (UTC clock `2026-10-25T21:37:26Z`).

| target | HTTP | final URL | bytes | sha256 |
|---|---|---|---|---|
| live `https://ai.google.dev/gemini-api/docs/coding-agents` | 200 | same URL, `num_redirects=0` | 115366 | `219ba9d1fccce7fa6343a7156bcd9905903b1fe528cda97f28be971ca3d2ccc9` |
| `.md` export `.../coding-agents.md` | 200 | same URL, `num_redirects=0` | 115362 | `fc99923c0ef2130dd7c2e20215b0259d67e8871a09a72d9d7575c179ecafd724` |
| archive `https://web.archive.org/web/2026/https://ai.google.dev/gemini-api/docs/coding-agents` | 200 | `https://web.archive.org/web/20261023092329/https://ai.google.dev/gemini-api/docs/coding-agents` (`num_redirects=1`) | 121174 | `5591770cd485a13875044acda1d98001da14138869f34943a43dc8740f761d85` |

```
$ curl -sSL -A 'Mozilla/5.0' --max-time 60 -o live.html \
    -w 'http_code=%{http_code}\nfinal_url=%{url_effective}\nsize=%{size_download}\nredirects=%{num_redirects}\n' \
    'https://ai.google.dev/gemini-api/docs/coding-agents'
http_code=200
final_url=https://ai.google.dev/gemini-api/docs/coding-agents
size=115366
redirects=0
exit=0
$ curl -sSI -A 'Mozilla/5.0' ... | grep -i -E '^(HTTP/|content-type|content-length|server)'
HTTP/2 200
content-type: text/html; charset=utf-8
content-length: 115366
server: Google Frontend
$ head -c 300 live.html   # first bytes after 8 blank lines
<!doctype html>
<html 
      lang="en"
      dir="ltr">
```

- **No redirect loop today.** The register row and staged S249/S260 both assert the live URL "redirects in
  a loop"/"is not reachable"; that was true on 2026-10-23 when S249 was mined, and it is not true on
  2026-10-25. This is the substantive calibration datum of this hand-check.
- **No markdown export exists.** The `.md` path returns `content-type: text/html` with
  `content-length: 115366` — the same HTML document (body bytes 115362 vs 115366, a transfer-level
  difference only; `size_download` vs `content-length`). So the assignment's ".md export" branch resolves
  to the same page, not to a markdown source.
- **Archive content is byte-different but text-identical to live.** Text extraction (scripts/styles
  stripped, tags → newlines, entities unescaped) yields 707 text lines from each; `difflib.unified_diff`
  over them returns 0 lines. The 121174 vs 115366 byte delta is explained by 49 occurrences of
  `web.archive.org` inside the snapshot (wayback URL rewriting), not by content change. The staged S249
  row records the snapshot as "121 172 B"; my fetch measured 121174 B — a 2-byte difference, recorded,
  not reconciled.

## F4 — the quoted span: no quote in the cell, but the page's own sentence is present

Step 3 of the assignment (locate the quoted span) has no input from row 13: its cell is prose. For the
L1's benefit I located the sentence that the staged sibling S249 quotes, on the **live** page, so a
future row can be re-pointed at the live URL without re-mining:

```
$ python3 <strip tags → live.txt>          # 707 text lines
$ grep -n -E '^(Summary of agent resources|Install Gemini agent skills)$' live.txt
207:Summary of agent resources
241:Install Gemini agent skills
$ sed -n '255p;256p;257p;258p;259p' live.txt
Skills come pre-installed in
Google AI Studio
Build
and are bundled in the
Gemini API
$ grep -o '.\{0,160\}Skills come pre-installed in.\{0,240\}' live.html | head -1
<aside class="note"><strong>Note:</strong><span> Skills come pre-installed in <a href="https://ai.studio/build">Google AI Studio
```

- Anchor for the sentence: section **"Install Gemini agent skills"** (live text line 241), inside a
  `Note:` aside; the resource table anchor **"Summary of agent resources"** is at live text line 207.
  Both anchors that S249 names exist on the live page.
- Fold required to match: **present-after-fold(inline-link markup)** — the sentence is split by anchors
  (`<a href="https://ai.studio/build">Google AI Studio` / `Build`, then `Gemini API` / `plugin` /
  `for Antigravity`), so the single-string form only exists after link text is joined with spaces.
  Word count of the joined sentence: 19; bytes dropped: none, markup replaced by the fold.
- The same sentence sits at archive text line 255 (`grep -n "pre-installed" arch.txt` → `255:`), i.e.
  the snapshot and the live page agree.

## F5 — prior-round state, re-run by me (not taken on trust)

```
$ grep -rn "S169" --include=*.md --include=*.txt --include=*.py --include=*.json .   # in kotoba-shokunin
./corpus/lessons/round-68.md:108:| S169 | unreachable | ai.google.dev/gemini-api/docs/coding-agents | unverifiable — the register never checked the quote; unreachable is not fabrication |
./.ufo/waves/round-70/w1/ScoutQuarantine.md:59:| S169 | ai.google.dev/gemini-api/docs/coding-agents | 0 | 0 | 0→0 |
./.ufo/waves/round-72/assimilation/quarantine-slice-full.txt:13:| `kotoba` | round5 | S169` | ...
```

Round 68 already fixed the class correctly (`unverifiable`, "unreachable is not fabrication"), and round
70's per-URL check found no registry row for the URL. What neither round recorded is that the URL is
reachable again; F3 supplies that measurement.

## What the L1 should land

1. **Keep row 13 classified `unverifiable`.** Its cell carries no quote; refusing it as fabrication
   would be wrong under addendum §10.
2. **Do not append a source for row 13.** Its URL is staged S249 (English) with S260 as the `?hl=ja`
   sibling; an append would duplicate S249, exactly the S151→S210 pattern round 70 caught.
3. **Record the freshness datum** (C2 axis): the "redirects in a loop" premise in register rows 13,
   S180, S249 and S260 is false as of 2026-10-25 — live HTTP 200, 115366 B, `num_redirects=0`, content
   text-identical to the 20261023092329 snapshot. If the lane re-pins any Google row this round, the
   live URL is now a valid retrieval surface.
4. **Normalise the stray backtick** after `S169` if the register text is ever rewritten; it is cosmetic
   and consistent across all six prose rows.

## Risks / limits

- Only one access date (2026-10-25, single GET per target); no repeat fetch, so no stability claim
  beyond "200 once, no redirects".
- The live page is HTML with client-side chrome; my text extraction is a lossy projection (tags →
  newlines). The anchor and sentence matches above are from the raw HTML (`grep -o` on `live.html`) and
  from that projection, both quoted.
- `sed -n '13p'` output above is pasted from the tool result; the line is 149 bytes including the
  trailing newline.
- No files outside the report and the scratch dir were written; scratch `/tmp/k72w1-ExecQuar13.Q9JF`
  removed before return. No tools installed or upgraded. No lane gate run (out of scope for this seat).
