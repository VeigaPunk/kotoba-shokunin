# ExecQuar03 — quarantine hand-check, register slice row 3 of 13 (S168)

## Verdict

**`absent` for the declared span; `present-after-fold(markdown-heading-strip + whitespace)` for the
row's real quote — the register row is a census parser artifact, NOT a fabrication. Retract/correct
the row; do not refuse it as fabrication.**

The quote cell holds the 1-token label fragment `` `section:` `` (8 chars, trailing colon, no
sentence). It is absent from every fetched artifact under seven named folds (0 hits each). But the
row's actual quote — the H2 heading of the cited page — **is** present, and the campaign's own census
records the same row id twice: once `folded` (fold `whitespace`) with the real quote, once `ABSENT`
with `section:`. The fragment is the text that sits *between* two quote pairs in the round-5 gate
note, so the register projected a delimiter label into a quote column. Refusing this row as
fabrication would be a false positive; keeping the quote cell as-is would be a fabricated quote.
Correct the quote cell to the located heading and the row is appendable.

## 1. Register row read (verbatim, slice line 3)

```
| `kotoba` | round5 | S168 | `payload-absent` | https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals | `section:` | cited source, companion URLs and local artifacts were all checked; the quote is in none of them |
```

Command: `sed -n '3p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt` → 233 bytes,
9 cells by `awk -F'|'`, quote cell = `section:` (untruncated, both backticks present, unlike rows 1
and 2). The same row is at `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:110`
(register header line 13: `payload-absent` = "every relevant source fetched cleanly and the quote is
in none of them | **the fabrication class**").

`S168` is not a lane registry row: `grep -c 'S168' corpus/SOURCES.md` → `0` (exit 1). The lane's only
S168 occurrence is `corpus/lessons/round-68.md:103`, which records the round-68 refusal.

## 2. Staged row by URL (host+path)

`grep -n 'vercel.com/blog/agents-md' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`
→ **one** hit: line 52, staged id **`S248`** (tier B, `docs`).

Staged id: **`S248`** (the register's campaign id `S168` is not itself staged; the URL is).

The staged row's own quote cell (line 52, columns 1–1200 read in two `cut` slices) reads:
`` "In 56% of eval cases, the skill was never invoked." `` and
`` "A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79%" ``
— both located in §4 below.

## 3. Fetch receipts (access date 2026-10-25, UTC)

| artifact | command target | HTTP | final URL | bytes | sha256 |
|---|---|---|---|---|---|
| cited HTML | `curl -fsSL -A 'Mozilla/5.0' https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` | **200** | same URL (no redirect) | **901,177** | `51d325f74f937056d97bca317f5eeab23b43596d2acc8997749cccf82f088b08` |
| `.md` export | same path + `.md` | **200** | same URL + `.md` | **11,843** (198 lines) | `d9c8dbd5cd080dab56554be7069eeecb8c7d357e2d7366a1ed9add10f91464dc` |
| archive | `https://web.archive.org/web/2026/https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` | **200** | `https://web.archive.org/web/20261022220721/https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` | **905,352** | `3c9edb88357593e23da83a3a0f7b0cda7b3d75b1bc314c7d940127147dc5b7b1` |

`-w 'status=%{http_code} final=%{url_effective} bytes=%{size_download}\n'` was the recorder;
`sha256sum` on the saved files. The cited URL is **not** a web.archive redirect (200 at the live
origin, final URL identical). Access timestamps: `2026-10-25T21:36:59Z` (HTML), same minute for the
two companions.

Two stability/freshness data points, unrequested but observed:
- the HTML byte count is **exactly** the round-5 gate note's `901 177 B` — the page is unchanged in
  size since 2026-10-23.
- the `.md` export is **now 200 / 11,843 B**, whereas the campaign's round-5 log recorded it as
  rejected: `lanes/kotoba/round5/SEARCH-LOG.md:55` → `` | F10 | ...agents-md-outperforms-skills-in-our-agent-evals.md | 404 | 270 234 B | **rejected** — guessed path; canonical form has no `.md` suffix | ``.
  That companion-URL half of the register's note is stale; it does not change this row's verdict.

## 4. Span location

Registered span: `section:`. Systematic fold matrix over all three artifacts (raw bytes and an
HTML-tag/script-stripped + entity-unescaped visible-text projection), computed by one `python3`
pass:

| fold (named) | cited HTML raw | HTML visible | `.md` export | archive raw | archive visible |
|---|---|---|---|---|---|
| literal `section:` | 0 | 0 | 0 | 0 | 0 |
| case-fold `(?i)section:` | 0 | 0 | 0 | 0 | 0 |
| case+whitespace `(?i)section\s*:` | 0 | 0 | 0 | 0 | 0 |
| markdown-escaped `section\:` | 0 | 0 | 0 | 0 | 0 |
| space-prefixed `:\s*section\b` | 0 | 0 | 0 | 0 | 0 |
| NFKC-normalized literal | 0 | 0 | 0 | 0 | 0 |
| bare word `\bsections?\b` (context only) | 15 | 1 | 1 | 16 | 4 |

The 15 HTML hits are CSS/JS tokens only — `grep -o 'section[^"<> ]\{0,25\}'` → `section`,
`section=content]]:border-0`, `section=`; no prose occurrence. **`section:` is absent.** The register's
note ("the quote is in none of them") is literally true.

Located anchor for the row's *real* quote (what the register's own census folded):

```
$ sed -n '36p' /tmp/k72w1-ExecQuar03.t7TA/s168.md
## **Skills weren't being triggered reliably**
```

Line **36** of the `.md` export. In the cited HTML the same heading is entity-escaped:
`grep -o 'Skills weren[^<]\{0,60\}' s168.html` → `Skills weren&#x27;t being triggered reliably`.
Folds named: (i) markdown heading markers `## **` … `**` stripped, (ii) whitespace fold — the
registry cell carries `triggered\nreliably`, the page carries one space, (iii) in the HTML form only,
the apostrophe is `&#x27;` (entity fold). **Anchor: section heading `Skills weren't being triggered reliably`.**

Corroborating located lines from the same export (each ≤25 words pasted; dropped bytes named):

```
$ sed -n '38p' /tmp/k72w1-ExecQuar03.t7TA/s168.md
In 56% of eval cases, the skill was never invoked. The agent had access to the documentation but didn't use it.
```
(line 38 continues ` Adding the skill produced no improvement over baseline:` — dropped, 8 words.)

```
$ sed -n '9p' /tmp/k72w1-ExecQuar03.t7TA/s168.md
A compressed 8KB docs index embedded directly in `AGENTS.md` achieved a 100% pass rate, while skills maxed out at 79% even with explicit instructions telling the agent to use them.
```
(dropped from the line: the trailing sentence `Without those instructions, skills performed no better
than having no documentation at all.` — 16 words.)

Results table, lines 41–43: `| Baseline (no docs) | 53% | — |`, `| Skill (default behavior) | 53% | +0pp |`.
Line 146: `The initial docs injection was around 40KB. We compressed it down to 8KB (an 80% reduction) while maintaining the 100% pass rate.` (dropped: the rest of that line after `pass rate.`, 20 words).

## 5. Origin of the fragment `section:` (why this is an artifact, not a fabrication)

The round-5 gate note that the census parses is
`/home/vgpnk/Projects/shokuknow/lanes/kotoba/round5/SOURCES-PROPOSED.md:36-37`:

```
— HTTP 200, 901 177 B. Anchor confirmed in the "Skills weren't being triggered
reliably" section: "In 56% of eval cases, the skill was never invoked." The four
```

`section:` is the **delimiter label between the closing `"` of the heading quote and the opening `"`
of the 56% quote** on a wrapped line — not a claim the round-5 seat made about the page.

The campaign census carries the same row twice, at adjacent indices
(`quote-lint-full-v5.json`, `findings[743]` and `findings[744]`):

- `findings[743]`: `"id": "S168"`, `"verdict": "folded"`, `"fold": "whitespace"`,
  `"quote": "Skills weren't being triggered\nreliably"`, `"line": "— HTTP 200, 901 177 B. Anchor confirmed in the \"Skills weren't being triggered\nreliably\" section: \"In 56% of eval cases,` — **the real quote, accepted**.
- `findings[744]`: `"id": "S168"`, `"verdict": "ABSENT"`, `"fold": null`, `"quote": "section:"`,
  `"binding": "id"`, `"line": "reliably\" section: \"In 56% of eval cases, the skill was never invoked.\" The four\nconfigurations were read from the resul` — **the fragment**.

The register generator copies the census quote verbatim and never synthesizes it:
`absent-defect-register.py:66` → `r["quotes"].append(f.get("quote") or "")`; its class table at
`:121-123` defines `payload-absent` as the fabrication class, which is why the fragment lands there.
Census-wide scale check (same file): `Counter(verdict)` over `findings` gives 324 `ABSENT`, **all 324
carrying `binding: "id"`**, and 27 of them have a quote of ≤12 chars (e.g. `kama S211 'still-live'`,
`revenger S062 'cell):'`) — the fragment class is systemic, not unique to this row.

## 6. What the L1 should land

- **Do not** append this row's quote cell and **do not** record S168 as a fabricated quote. Record
  the row as *retracted: census delimiter artifact; real quote present at anchor
  `Skills weren't being triggered reliably`* — the round-68 lesson line 103 (`refused — the quoted
  span was not located on the page this round fetched`) is true of the fragment and misleading about
  the row; a one-line correction there is the honest fix.
- The appendable content is already staged as **S248** with quotes I located verbatim in §4; nothing
  new needs to be mined from this URL for the register.

## Notes / calibration limits

- I did **not** adjudicate the four-configuration table's 79%/100% rows or the 40 KB→8 KB reduction
  as a claim (staged S248's business, and another wave-1 seat's target); I only located the bytes.
- The "local artifacts" half of the register note is vacuous here: the lane holds no S168 row
  (`grep -c` = 0), so no local artifact could have carried the fragment.
- The visible-text projection is my own (`script|style` strip, tag strip, `html.unescape`, whitespace
  collapse); counts on the raw bytes are the primary evidence and are what the fold matrix reports.
- No file was edited. No tool installed or upgraded (nothing was needed). Scratch
  `/tmp/k72w1-ExecQuar03.t7TA` deleted after the receipts above were taken; lane `git status` shows
  only the untracked `.ufo/waves/round-72/` wave tree that the L1 owns.
