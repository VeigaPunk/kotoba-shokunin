Result: MIXED — S032's anchor, Gate quote, reading-cell facts, budget attributions and tier all hold on a byte-identical re-open, but the entry's § Limits (and SCORECARD:30, which repeats it) misdescribes the C2 counter: the counter never checks the location cell and its lesson check is whole-file, not § Gate.

Seat: ReopenS032 (scout, leaf). Target: SOURCES row S032, its use in `corpus/knowledge/mcp-server-instructions-round52.md`, `corpus/lessons/round-52.md` § Gate, and `SKILL.md`. Judged revision `c8407a453788df964df5a7b835dd0ce1360de882`. No lane file edited; no tool installed or upgraded; all writes under `/fast/scratch/hyaku/kotoba-r52a2/ReopenS032/`.

## Fetch record (ordinary curl GET, no browser, no challenge bypass)

| URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://modelcontextprotocol.io/specification/2025-11-25/schema.md | 2026-10-22T17:50:12Z | 200 | 130,800 | `5ab7cfcd5ea05c7491637e76122362cc4416201ea0c81482f6747f59343f1691` |
| https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle.md | 2026-10-22T17:52:09Z | 200 | 9,177 | `f1e1c10b6a89b42c92b22262e588d61476d03d65e123399220f513d6018f8987` |
| https://modelcontextprotocol.io/specification/2025-11-25/basic/index.md | 2026-10-22T17:52:09Z | 200 | 11,157 | `04b3c620d15e436a8aa59517aaae935021323cf133324a3b6ac4a6eb4f822261` |

The schema body is byte-identical to the row's recorded fetch (130,800 B; 8-hex prefix `5ab7cfcd` matches; the Gate's full hash matches exactly), 45 minutes after the recorded 17:04:55Z fetch. Response headers at 17:54:29Z: `HTTP/2 200`, `content-type: text/markdown; charset=utf-8`; in that response `last-modified` was stamped one second after `date`, so content identity rests on sha256, never on that stamp. Fetched copies are scratch, not evidence.

The page is 1,304 lines. Only two lines mention `instructions` at all, case-insensitively — lines 461 and 463, both inside `InitializeResult` (the token appears four times across them, in the field declaration, its description, and their permalink anchors). No `draft` marker anywhere; all 46 internal `/specification/` links point at `2025-11-25`, so the revision in the row's anchor is corroborated by the page, not only by the URL.

## The page's own text at the cited location, verbatim

- line 454 heading: `### InitializeResult`
- lines 456-463 the interface; line 461 field declaration: `[instructions](#initializeresult-instructions)?: string;`
- line 463 (single long line, field description):
  `instructions?: string[Permalink](#initializeresult-instructions) Instructions describing how to use the server and its features. This can be used by clients to improve the LLM's understanding of available tools, resources, etc. It can be thought of like a "hint" to the model. For example, this information MAY be added to the system prompt.`
- line 463 also carries, for the type: `}After receiving an initialize request from the client, the server sends this response.`
- lifecycle page, line 142: `    "instructions": "Optional instructions for the client"` (inside the initialize example); neither page places the text anywhere by requirement.

The entry's S032 reading cell (entry:23, verbatim): `The field is optional and server-sent. The same schema text goes on: clients can use it "to improve the LLM's understanding of available tools, resources, etc." and it is "like a "hint" to the model". The 2025-11-25 schema text does not say where a client must place it.`

## Verdicts per statement

| # | statement (owner) | verdict | evidence |
|---|---|---|---|
| 1 | Gate quote `"Instructions describing how to use the server and its features."` is verbatim at `schema.md:463` (lesson:18-19, entry:23) | **HOLDS** | Appears exactly once in the fetched file, on line 463, under § InitializeResult (line 454), in the `instructions?: string` description. `grep -c` → 1; Python `page.count(q)` → 1; 10 whitespace words; contains `instructions`. |
| 2 | Row anchor `130,800 B, sha256 5ab7cfcd…` (SOURCES:45) | **HOLDS** | Re-fetch identical: 130,800 B, sha256 `5ab7cfcd…1691`; full hash equals the Gate cell. |
| 3 | "The `instructions` field is optional" (row teaches, entry:23, SKILL.md:87) | **HOLDS** | Line 461 `instructions…?: string;`; lifecycle:142 says "Optional instructions for the client". |
| 4 | "server-sent" / "a server returns in its `initialize` result" (row teaches, entry:11-12, SKILL.md:87) | **HOLDS** | Line 463: `After receiving an initialize request from the client, the server sends this response.` |
| 5 | "describing how to use the server and its features" (row teaches, SKILL.md:87) | **HOLDS** | Verbatim first sentence of line 463. |
| 6 | "which clients can use to improve the model's understanding" (row teaches, entry:23) | **HOLDS** | Line 463: `This can be used by clients to improve the LLM's understanding of available tools, resources, etc.` The entry's quoted fragment `to improve the LLM's understanding of available tools, resources, etc.` is an exact substring. |
| 7 | "the schema leaves its placement to the client" (row teaches, SKILL.md:87); entry:23 "does not say where a client must place it" | **HOLDS, narrow** | The field text contains 0 `MUST`; the only placement sentence is a permission: `For example, this information MAY be added to the system prompt.` A permission leaves the choice to the client, so the claim is not false. But it is not silence: the schema names the system prompt as a permitted placement, and both the row and SKILL.md drop that datum. See the coverage-gap note (statement 7) under Inferences. |
| 8 | Entry reading cell's other quoted fragments: `like a "hint" to the model` and the `improve the LLM's understanding…` clause (entry:23) | **HOLDS** | Both are exact substrings of line 463 (checked raw). Typographic nit: the entry nests double quotes inside double quotes; the words are the page's. |
| 9 | Budgets: 4,096 chars (Claude Code) and first 512 chars (Codex) | **HOLDS as attribution** | No budget is attributed to S032 anywhere. Entry:44-45 and SKILL.md:91 credit S033 and S035. The schema sets no length limit on the field (plain `string`, no `maxLength`, no cap sentence), and the row/entry/SKILL.md claim none. |
| 10 | Tier `A`, kind `spec`, scope "protocol text, not a measurement of any client" | **HOLDS** | Fleet contract `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:26-30`: A is "primary or authoritative for that scope (spec, official docs…)". This is the official specification's schema reference at its versioned route; the row's scope is correctly bounded to protocol text. No tier inflation (`spec` is allowed at A; `community` would not be). `recheck: on-release` is a permitted cadence (`:38-39`). Row shape is 11 cells; status `mined` is consistent with its `used-by` naming the entry and lesson. |
| 11 | Entry § Limits: "The counter … checks that each row's quote is **located**, short, contains `instructions`, sits on the client's own host and **is in the round's Gate**" (entry:61-63; repeated as "checks location, length, the word `instructions`, host and Gate record" at `SCORECARD.md:30`) | **BREAKS — LOW** | Read of the frozen counter: `verifiers/check_mcp_instructions.py:205-235` uses only `r[1]` (row id) and `r[2]` (quote cell). The location cell (table cell 4) is never read; a wrong line number would still count as backed. The lesson condition at `:234` is `sid not in lesson or quote not in lesson` over the whole file, not a test that the quote sits under `## Gate`; a quote placed in § Mistakes would pass. For S032 both underlying facts are true by hand check — the quote is on the cited line 463 and appears in the Gate at lesson:18-19 — so the C2 count itself is unaffected; the description of the instrument is what is wrong. Fix: reword both sentences (e.g. "checks the quote cell's length and required word, the source row's tier/kind/status/opened/used-by and pinned host, and that the quote appears verbatim somewhere in the round lesson; the location cell is checked by hand, not by the counter"). |
| 12 | Entry intro "sits beside the tool descriptions" (entry:11-13) | **INFO, not a break** | Not on the S032 page. It is a client-doc synthesis (S035's "alongside the server's tools"); no row cell or location attributes it to S032. Fine as framing, but a reader could take it as spec text. |
| 13 | README:78 "five client pages (S032 spec, …) each with a located quote on what the client does" | **INFO, adjacent** | S032 is the specification row, not a client page; the entry's own table labels it "MCP specification". One-word category slip outside my target, reported for the L1's judgment. |

## Machine checks reproduced (read-only)

```
$ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882
MCP specification  BACKED
Claude Code        BACKED
VS Code            BACKED
Codex              BACKED
Gemini CLI         BACKED
opencode           no rows naming client: 0 (need 1)
Copilot CLI        no rows naming client: 0 (need 1)
mcp instructions backed 5 of 7 clients
exit=0
```

The S032 row passes every counter condition (tier A, kind spec, status mined, opened 2026-10-22, used-by names the entry, URL host `modelcontextprotocol.io` allowed). Counter freeze holds:

```
$ git diff 4c003a4b9c7dae8ebb8ad34bbc14cd1706febeeb c8407a453788df964df5a7b835dd0ce1360de882 -- verifiers/check_mcp_instructions.py
(no output) exit=0
```

`--fetch` for S032 is established directly: the quote is a substring of the raw page and of the counter's normalized form (lowercase, tags/backticks/emphasis stripped, whitespace collapsed), so the counter would score S032 `found=True`. I did not fetch the other four backed pages; those rows are other seats' targets.

## Inferences and remaining unknowns

- [INFERENCE] "leaves its placement to the client" is a correct reading of `MAY be added to the system prompt`; calling the dropped example a defect is a judgment call, so I record it as a coverage gap, not a break. Recommended one-clause fix in the row teaches and SKILL.md:87: "the schema leaves placement to the client and names the system prompt as one permitted placement (`MAY`)".
- The page's `last-modified` header at 17:54:29Z was stamped one second after the response `date`, so it does not track content edits; sha256 is the only usable identity, and it is stable between the recorded 17:04:55Z fetch and my 17:50:12Z fetch.
- Severity summary: one LOW defect (statement 11, two documents: entry § Limits and SCORECARD:30), two INFO notes (statements 12, 13). Everything else HOLDS; no anchor drift, no quote drift, no tier inflation, no unsupported S032 statement found.
