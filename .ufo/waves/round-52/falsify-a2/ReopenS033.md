Result: MIXED — the Gate quote is verbatim, the row's fetch anchor is honest and its sha256 matches the attempt-1 fetched bytes, and the tier and budget statements hold; four precision defects remain, one Low–Medium (the citation no longer resolves on today's live bytes) and three Low (abbreviated section label; "always in context"; "both are always-loaded").

Seat: ReopenS033 (round-52 attempt 2, falsify). Lane read-only; probe run in
`/fast/scratch/hyaku/kotoba-r52a2/ReopenS033/clone` at `c8407a453788df964df5a7b835dd0ce1360de882`.
No installs or upgrades were needed or made.

## Re-open record (ordinary curl, no browser)

Command: `curl -sS -D headers.txt -o mcp.md -w 'http=%{http_code} bytes=%{size_download}' https://code.claude.com/docs/en/mcp.md`
(exit 0).

- URL: https://code.claude.com/docs/en/mcp.md
- UTC access: start 2026-10-22T17:50:09Z, end 2026-10-22T17:50:09Z
- HTTP/2 200; `content-type: text/markdown; charset=utf-8`; `last-modified: Thu, 22 Oct 2026 17:50:09 GMT`
  (server sets this equal to the fetch instant, so it is not a revision signal)
- Bytes: 128,298; sha256 `9ec4942d35fba402f5c246303748d53d88852736d825862c0a5e0efc22266428`
- Local scratch: `/fast/scratch/hyaku/kotoba-r52a2/ReopenS033/mcp.md`; headers in same directory.

Comparison with row `corpus/SOURCES.md:46`: anchor records 127,022 B, sha256 prefix
`9a42e98f…` at 2026-10-22T17:04:56Z. The live page **does not match** that anchor: +1,276 B,
different sha256. The anchor is nevertheless corroborated exactly by attempt 1's saved copy
`/fast/scratch/hyaku/kotoba-r52/src/cc-mcp.md` — 127,022 B, sha256
`9a42e98f81001adbefcf19d03fc40d591ffe55ba7c83b5a764ea725b403af766`, mtime `Oct 22 14:04`
local. The session timezone is UTC-03:00 (lesson/watchdog line `…-03:00`), so 14:04 local is
17:04Z [INFERENCE, corroboration only; mtime is not an authenticated fetch log]. So the recorded
anchor is honest for the attempted fetch; the bytes served at that URL changed between 17:04:56Z and
17:50:09Z.

What changed (diff of the two copies; 22 changed lines): a new section
`## Mark tools that are safe to call twice` inserted at live `:1408`, plus a rewritten OAuth
sentence at live `:768`. Line counts 1,647 (pinned) → 1,667 (live), +20. The quoted passage
itself is byte-identical except for its offset.

## Statement-by-statement verdicts

| # | statement under test | where | verdict | severity |
|---|---|---|---|---|
| S1 | Gate quote is verbatim, at the cited location, on the page as fetched | `corpus/lessons/round-52.md:20-21`; `corpus/SOURCES.md:46`; `corpus/knowledge/mcp-server-instructions-round52.md:24` | **HOLDS** | — |
| S2 | the recorded anchor / line citation resolves on a re-open | `corpus/SOURCES.md:46` anchor cell | **BREAKS** (page drifted; `:1468` no longer holds the quote live) | Low–Medium |
| S3 | row `teaches`: load at session start; purpose; cut at 4,096 by default | `corpus/SOURCES.md:46` | **HOLDS** | — |
| S4 | entry reading: "server instructions are always in context while tool definitions are deferred" | `corpus/knowledge/mcp-server-instructions-round52.md:24` | **BREAKS** narrowly — "always" is not the page's wording | Low |
| S5 | entry reading: page says instructions "help Claude understand when to search for your tools" (`:1476`) | same cell | **HOLDS** | — |
| S6 | entry reading: "cuts server instructions longer than 4,096 characters by default" (`:1484-1486`) | same cell | **HOLDS** | — |
| S7 | entry craft 2: "Claude Code cuts at 4,096 characters by default" | entry `:43-45` | **HOLDS** | — |
| S8 | entry craft 4: "the page compares server instructions to skills (`:1476`): both are always-loaded text" | entry `:49-52` | **BREAKS** narrowly — the skills half is not on this page | Low |
| S9 | SKILL: "Claude Code cuts it at 4,096 by default (S033)" | `SKILL.md:91` | **HOLDS** | — |
| S10 | SKILL: "with tool search, Claude Code loads only tool names and server instructions at session start (S033)" | `SKILL.md:92` | **HOLDS** | — |
| S11 | section label "§ Tool search" | `corpus/SOURCES.md:46`, entry `:1` and `:24` | **BREAKS** narrowly — actual heading is "Scale with MCP tool search" | Low |
| S12 | tier `docs` / `A` for this scope | `corpus/SOURCES.md:46` | **HOLDS** | — |
| S13 | Gate record completeness: URL, date, bytes, sha256, ≤25-word quote | `corpus/lessons/round-52.md:20-22` | **HOLDS** | — |

### S1 — quote is verbatim at `:1468` on the fetched bytes (HOLDS)

Pinned copy `/fast/scratch/hyaku/kotoba-r52/src/cc-mcp.md` (127,022 B, sha256 `9a42e98f…`):

```
1466:## Scale with MCP tool search
1468:Tool search keeps MCP context usage low by deferring tool definitions until Claude needs them. Only tool names and server instructions load at session start, so adding more MCP servers has minimal impact on your context window. Claude Code doesn't impose a fixed per-server tool cap; the practical limit is your context window budget.
```

The quoted sentence is sentence two of `:1468`, byte-identical to the Gate quote, one
occurrence on the page (`python3` check: words 22, `quote_present=True occurrences=1`). Word
count 22 ≤ the 25-word contract limit (`CORPUS.md` rule 1). It contains `instructions`, as
the C2 counter requires.

Live bytes (128,298 B, sha256 `9ec4942d…`): same sentence, one occurrence, now at `:1488`
under `## Scale with MCP tool search` at `:1486`. So the quote survives live; only its line
moved.

### S2 — the anchor/citation no longer resolves live (BREAKS, Low–Medium)

On live bytes, `:1468` is a blank line inside the "Multiple resource references" example
(`:1464-1472`), ~20 lines before the quote; the section moved from `:1466` to `:1486`. The
row's byte count and sha256 also no longer match. This is honest snapshot drift, not a false
record, and it does not break C2's stated `--fetch` result: I re-ran the counter on the live
URLs —

```
$ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882 --fetch
MCP specification  BACKED found=True
Claude Code        BACKED found=True
...
mcp instructions backed 5 of 7 clients
mcp instructions found on the live page 5 of 5
exit 0
```

(the non-`--fetch` run also prints `backed 5 of 7`, exit 0). The counter's `--fetch` checks
substring presence, not the anchor, so the drift is invisible to it.

Why Low–Medium rather than low: the page is under active edit on the very day it was mined
(+1,276 B within 46 minutes), so the `90d` recheck will re-open a page whose cited lines and
anchor are already stale, and a reviewer following `mcp.md:1468` on the live page lands in
unrelated text. Fix candidate: cite the heading and quote, and keep the byte/sha anchor
explicitly labelled as the 17:04:56Z snapshot (or refresh the row's anchor and line numbers);
consider recording the drift in the lesson's "Rows touched" log if the anchor is rewritten.

### S3/S5/S6/S7/S9/S10 — the page does say these (HOLDS)

Pinned copy, exact lines:

```
1474:### Tool search for MCP server authors
1476:If you're building an MCP server, the server instructions field becomes more useful with tool search enabled. Server instructions help Claude understand when to search for your tools, similar to how [skills](/docs/en/skills) work.
1484:Claude Code cuts a tool description or server instructions that run past these default limits, and Claude sees only the text before the cut:
1486:* **Server instructions, and the description of a tool that loads upfront**: 4,096 characters
1493:Descriptions and instructions from some of the MCP servers that Anthropic hosts at `api.anthropic.com` reach Claude in full. To change the limits for the other MCP servers in your session, set [`CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`](/docs/en/env-vars#variables) ...
```

- `:1476` supplies the purpose and the skills comparison verbatim.
- `:1484-1486` supplies the cut and the 4,096 default; "by default" is correct because
  `:1493` documents an env-var override and `:1491` documents the old 2,048 limit.
- `SKILL.md:91` "cuts it at 4,096 by default" and `SKILL.md:92` "with tool search, Claude Code
  loads only tool names and server instructions at session start" are both on the page
  (`:1468`, `:1486`); tool search being the default is also on the page (`:304-305`: "With
  tool search, the default"; `:399`; `:1526`), so SKILL's unqualified "with tool search" is
  consistent.
- Row `teaches` ("help Claude decide when to search") is a fair paraphrase of "help Claude
  understand when to search" (`:1476`).

### S4 — "always in context" is stronger than the page (BREAKS, Low)

The page says "Only tool names and server instructions load at session start"
(`:1468`) and that tool definitions are deferred until needed. It never says the
instructions remain in context for the session (no "always"/"persist"/"remain" statement near
server `instructions`; the only lines about server `instructions` are `:1468, :1476, :1478,
:1484, :1486, :1489, :1493` — the other `instructions` hits, `:165-187`, are about setup
instructions). The entry's "always in context" is an inference from "load at session start
and are not deferred", and it is the same reading this lane uses for skill descriptions
(`SKILL.md:66`, sourced elsewhere). It is not contradicted by the page, but it is not the
page's word. A second qualification in context: `:1582` and `:1600` document `alwaysLoad`,
under which a server's tools "load into context regardless of the search" and startup waits
for them — so "only tool names and server instructions load at session start" is the default,
not a universal, and the entry's flat "tool definitions are deferred" inherits that
simplification. Recommended wording: "load at session start and are not deferred (tool
definitions are deferred until needed by default)". Severity Low: the quote does not say
"always", and a reader can fairly infer persistence, so the craft rule is not wrong — the
sourcing is slightly over-tightened.

### S8 — "both are always-loaded text" adds a skills claim not on S033 (BREAKS narrowly, Low)

Entry `:49-52`: "In Claude Code the page compares server instructions to skills (`:1476`):
both are always-loaded text that decides when the model reaches for a capability…". The
comparison is exactly on the page ("similar to how skills work", `:1476`). "Skills are
always-loaded" is not on this page — its four `skill` hits are `:53, :529, :1476, :1610`,
none about skills' load policy — that fact comes from S022/S023 (both cited elsewhere in the
lane). The sentence attributes it as part of what "the page" says. Fix: either cite S022/S023
for the skills half or write "both are loaded at session start". Severity Low: it does not
change the craft rule, and the lane already holds the skills claim from stronger rows.

### S11 — section label is abbreviated (BREAKS narrowly, Low)

Both the row and the entry call the first location "§ Tool search (`mcp.md:1468`)"; the
heading that contains `:1468` is `## Scale with MCP tool search` (`:1466` pinned, `:1486`
live). The second label, `§ Tool search for MCP server authors` (`:1474`), is exact. The
corpus contract requires an exact heading/section in the anchor (`CORPUS.md` "anchor" bullet),
and the lane has treated a non-existent heading name as a defect before (S018 superseding
S001 for a named heading that does not exist). Here the line is exact and the section is
unambiguous, so severity Low, but the label should read "Scale with MCP tool search" (or
"§ Scale with MCP tool search … § Tool search for MCP server authors").

### S12 — tier is right (HOLDS)

`CORPUS.md` tier rule: "A: primary or authoritative for that scope (spec, official docs,
source code, original paper, maintainer statement…)". `code.claude.com/docs` is Anthropic's
official Claude Code documentation; the row's scope limits it to "what Claude Code documents
… (vendor documentation, not a measurement of omp or opencode)". Kind `docs`, tier `A` is
correct, and the row does not inflate the tier into a measurement of Claude Code's actual
behavior.

### S13 — Gate record is complete and the sha256 is corroborated (HOLDS)

`corpus/lessons/round-52.md:20-22` records URL, `opened 2026-10-22T17:04:56Z`, `127,022 B`,
full sha256 `9a42e98f81001adbefcf19d03fc40d591ffe55ba7c83b5a764ea725b403af766`, quote location
`mcp.md:1468`, and the 22-word quote. That full hash equals the hash of attempt 1's saved
`cc-mcp.md`, and the quote is present exactly once in it. The C2 counter's Gate requirement
(id + quote verbatim in the lesson) passes: the counter prints `Claude Code BACKED`. The
Gate does not record the byte-level check itself, but the bytes and hash are recorded and
reproducible only from the scratch copy, which the lesson correctly labels scratch, not
evidence — so the fetch time itself is not independently authenticated beyond the matching
hash and mtime.

## Counter evidence

In the sandbox clone at `c8407a453788df964df5a7b835dd0ce1360de882`:

- `python3 -B verifiers/check_mcp_instructions.py --rev c8407a4…` → `mcp instructions backed 5 of 7 clients`, exit 0.
- `python3 -B verifiers/check_mcp_instructions.py --rev c8407a4… --fetch` → `backed 5 of 7`, `found on the live page 5 of 5`, exit 0.

Both were run after my fresh fetch, so the `--fetch` figure is live right now, not a
replayed value.

## What this does to the attack targets

- Gate quote verbatim and at the cited location **on the pinned fetch**: it holds.
- Every S033 statement in the row's `teaches`, the entry's limits/budgets, and `SKILL.md`
  **is on the page**: it holds.
- The quote does say what the reading cell says **in mechanism**; the reading adds the word
  "always" and, in craft item 4, a skills property the page does not state — both Low, both
  fixable by one-word/sourcing edits, neither changing the entry's rule.
- Tier: correct.
- The one operational risk is citation rot: the live page has already moved the quote from
  `:1468` to `:1488` and changed bytes/sha within 46 minutes of the recorded fetch.

## Remaining unknowns

- Whether 17:04:56Z was the origin build or a cached edge copy cannot be authenticated; only
  the matching saved bytes corroborate it.
- The page is under active edit (one change observed mid-hour), so the live line and byte
  anchor may move again before closure; C2's `--fetch` claim only requires substring
  presence, which currently holds.

## Exact fixes for the L1

1. `corpus/SOURCES.md:46` anchor and `corpus/knowledge/mcp-server-instructions-round52.md:1,24`:
   name the section "Scale with MCP tool search" (`:1466` pinned / `:1486` live), or cite
   both headings; keep `:1468` as the pinned-copy line and note the line refers to the
   2026-10-22T17:04:56Z fetch (127,022 B, sha256 `9a42e98f…`).
2. Entry `:24`: replace "always in context" with "load at session start and are not
   deferred".
3. Entry `:49-52`: cite S022/S023 for skills' always-loaded property, or say "both load at
   session start".
4. Optional: refresh the row's anchor bytes/sha to the current page (128,298 B, sha256
   `9ec4942d…`) only if re-opening this round, and log the old→new anchor change; otherwise
   leave the snapshot honest and add the snapshot caveat.
