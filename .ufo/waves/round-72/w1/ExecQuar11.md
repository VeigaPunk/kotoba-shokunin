# ExecQuar11 — quarantine hand-check, register slice row 11 of 13 (`S239`, https://skills.sh/agent)

**Verdict: `unverifiable-class` — the row carries no quoted span at all, so nothing can be
refused as fabrication; but the class cell's premise ("could not be fetched") is false as of
today, and the source it names is fetchable (HTTP 200), so the round-68 flip condition is now
open. The staged row for this URL is `S319`, not `S239` — staged `S239` is a different document,
so any id-keyed join would attach the wrong source.**

No committed lane file was modified. Nothing was installed. Scratch used and deleted:
`/tmp/k72w1-ExecQuar11.IC54`, `/tmp/k72w1-ExecQuar11b.*`.

## The row, verbatim

```
$ sed -n '11p' .ufo/waves/round-72/assimilation/quarantine-slice-full.txt
| `kotoba` | round10 | S239` | the cited source could not be fetched, so no quote was checked | https://skills.sh/agent |
```

- Line 11 of 13 (`wc -l` → 13). Field count: `awk -F'|' 'NF>1{print NR": cols="NF-2}'` → `11: cols=5`,
  the same 5-field shape as rows 1, 2, 8–13 (rows 3, 6, 7 read `cols=7` only because their backticked
  quotes contain `|`). So the row has **lane | round | id | class | url** and *no quote cell*: the
  instruction's "quoted span between backticks" resolves to the campaign id `S239` plus one stray
  trailing backtick (the id cell is `S239`` in bytes, `cat -A` shows `S239\` |`).
- The class cell is prose, not a quote: `the cited source could not be fetched, so no quote was checked`.

## Staged row for this URL (host+path match)

```
$ grep -n 'skills\.sh/agent' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
123:|| S319 | skills.sh — Agents index — https://skills.sh/agent | docs | B | ...
```

**Staged id: `S319`** (`SOURCES.append.md:123`; also cited at
`knowledge/corpus/knowledge/japanese-client-layer-round10.md:4`). Its locator cell reads
"the introduction above the per-agent list, at the sentence stating the install promise", and its
claim cell reads "skills install once and are available across every session". `S319` is not in
`.ufo/waves/round-72/assimilation/collisions` (S203–S213) and is above the lane registry's top id.

**Id-space hazard (calibration).** Staged `S239` is not this document:

```
$ grep -n 'S239' /home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md
43:| S239 | IHBench: Instruction-Hierarchy Robustness Benchmark — https://arxiv.org/abs/2607.25987 | paper | B | ...
```

The lane registry tops out at `S213` (`.ufo/waves/round-72/assimilation/reg-ids`, last line `S213`),
so register id `S239` is a register/campaign id, not a staged id. Join this row by URL only; joining
by id adopts arXiv 2607.25987 in place of the agents index.

## Fetch record (step 2)

Access date 2026-10-25 (UTC `21:37:45Z` for the saved body).

```
$ curl -sS -A 'Mozilla/5.0' -D hdr.txt -o body.html -L --max-redirs 5 https://skills.sh/agent
http_code=200 final=https://www.skills.sh/agent size=69574 ct=text/html; charset=utf-8 redirects=1
$ grep -Ei '^(HTTP/|location:)' hdr.txt
HTTP/2 308
location: https://www.skills.sh/agent
HTTP/2 200
$ sha256sum body.html
f6e88229f4af5875491687d0611f83edded72c35f9b0731e501cd633d58071c9  body.html
```

- The exact cited form also succeeds: `curl -fsSL -A 'Mozilla/5.0' https://skills.sh/agent` →
  `code=200 final=https://www.skills.sh/agent size=69574`, `exit=0`, same sha256. The bare-host 308
  body is 15 bytes, `Redirecting...` (sha256 `7c040f86…`) — a client that does not follow the
  redirect sees a 15-byte stub, which is the only fetch failure mode I can reproduce.
- Direct final host: `https://www.skills.sh/agent` → `code=200 size=69574`, same sha256.
- `.md` export: `https://skills.sh/agent.md` → `curl: (22) … 404` (`code=404`); `agent/index.md`
  likewise 308→404. No markdown export exists for this page.
- Archive form: the URL is not a web.archive redirect, so no archive form was needed for the fetch.
  CDX, for provenance: `http://web.archive.org/cdx/search/cdx?url=skills.sh/agent&output=json` →
  captures `20260507201019`, `20260513025356`, `20260530134727`, `20260607112319`, all `200`; the
  `from=20261001` query returns `[]` (no capture after 2026-06-07, so the archive cannot date the
  round-10 claim).
- The earliest-wayback-availability probe was rate-limited once: `archive.org/wayback/available` →
  `429 Too Many Requests`; the CDX endpoint above answered `200`, so this did not block anything.

## Located span (step 3)

The register row has no quote, so the span I checked is the one the staged locator names. Extraction
(scratch): strip `<script>`/`<style>`, turn `</p|li|h1..h3|header|div|ul|main|section>` into newlines,
strip remaining tags, `html.unescape`, drop empty lines → 88 lines (`page.txt`).

```
$ sed -n '4,7p' page.txt
PacksTopicsOfficialAuditsDocs
skills/agentsAgents
Every AI coding agent that supports the open skills CLI. Install once, use across every session.
Claude Code
```

```
$ grep -n 'Install once' page.txt
6:Every AI coding agent that supports the open skills CLI. Install once, use across every session.
```

**Line 6** of the text extraction. Located literal, 6 words, copied from the fetched bytes:
`Install once, use across every session.` — literal equality in the raw HTML, not a fold: the raw
document is one line (`raw_newlines 0`, 69,574 bytes) and the literal occurs twice, at char offsets
`7707` and `46469`; the offset-7707 site is the rendered header paragraph, the 46469 site is the RSC
flight payload. No case/whitespace/markdown fold was used, so no fold is named.

**Anchor:** the `Agents` index page header (`<header class="mb-10">`, raw chars 7287–7750) — H1
`Agents — All AI agents that support the skills CLI`, breadcrumb `skills/agentsAgents`, then the
paragraph whose last sentence is the located literal, immediately followed by
`<ul class="grid …">` (the per-agent list). This is exactly the staged locator's "introduction above
the per-agent list". The list holds 20 entries (`grep -o '<li><a class="flex' body.html | wc -l` →
`20`), which matches the staged knowledge file's "names 20 agents".

Pre-round-10 provenance, for the class cell's premise: the 2026-06-07 archive capture returns
`code=200 size=76587 sha256 5a085c0e5fa827bfc1225e73ae24eb5495ac1f09416445677c1799bb6366ad0b`, holds
the same literal twice (offsets 7287, 53550) and the same 20-entry list. So the page was fetchable,
with this sentence and this list, four months before the register wrote "could not be fetched".

## Why `unverifiable-class` and not `present`

Addendum §10 (`plans/round-72.md:187-198`) hand-checks the slice row by row; the seat's rule for a
prose class cell is that the row is `unverifiable`, which is not fabrication. This row has no quoted
span, so there is nothing to compare against the bytes; I did not invent one to promote the row. What
I can report is that the row's stated reason is false today.

The register's own flip rule (`corpus/lessons/round-68.md`, the paragraph under the 13-row table):
"Flip condition for an `unreachable` row: the source becomes fetchable and the quote is then checked —
an unreachable row is never a fabrication claim." Fetchable: yes (200, above). Quote to check: the
row supplies none, so the only checkable sentence is staged `S319`'s locator sentence, and it is
present verbatim with the anchor located. That makes an **adopt of `S319`** available to the L1; it
does not resurrect a row quote that never existed. Adopt form if the L1 takes it:

- staged id `S319`; URL as served `https://www.skills.sh/agent` (cited `https://skills.sh/agent`
  308-redirects to it); accessed 2026-10-25; sha256 `f6e88229…`; 69,574 bytes; quote
  `Install once, use across every session.`; anchor "the header introduction above the per-agent
  grid on the Agents index page".

If the L1 instead keeps the register row, the correct recorded class is still `unverifiable` — but
the reason must change from "could not be fetched" to "the register row carries no quoted span", and
that difference belongs in the round-72 lesson as a `stale-premise` row, because the class was
inherited, not measured: the same 13 rows with the same verdicts sit in `corpus/lessons/round-68.md`
lines 101–113 (`| S239 | unreachable | skills.sh/agent | unverifiable — same class |`, line 112),
four lane rounds before this register slice.

## Side evidence, not verdicts (other seats own these rows)

Same `curl -fsSL -A 'Mozilla/5.0'` form, status only, to test whether the prose class is a property
of the URLs or of the round that wrote it:

```
https://skills.sh/docs                    -> code=200 final=https://www.skills.sh/docs size=44245
https://skills.sh/audits                  -> code=200 final=https://www.skills.sh/audits size=484518
https://skills.sh/docs/api                -> code=200 final=https://www.skills.sh/docs/api size=138514
https://code.claude.com/docs/en/security.md -> code=200 final=https://code.claude.com/docs/en/security.md size=15462
https://ai.google.dev/gemini-api/docs/coding-agents -> code=200 final=https://ai.google.dev/gemini-api/docs/coding-agents size=115362
```

All six prose-class URLs (S236, S237, S238, S239, S243, S169) answer 200 today. I make no claim about
whether each contains the quote its own row would need — I did not open them for content.

## Risks and blockers

- **Not a blocker.** The only failure mode I can reproduce for this URL is a non-following client
  seeing the 15-byte `Redirecting...` stub. If round 10's fetch was done with a redirect-less client,
  that explains the class cell without any site outage — unverified, since no capture exists between
  2026-06-07 and today.
- **Id join.** Register `S239` ≠ staged `S239`. Any renumber map for this row must key on
  `skills.sh/agent`, as the round-70 scout's map does for `S231 → S210`.
- **Coverage limit.** I checked one page's content; the sibling five rows above are status-only.
- Nothing in this hand-check is `byte-exact` beyond the literal string and the sha256s pasted above;
  all other quotations are word-copied with the dropped bytes being the surrounding HTML markup.
