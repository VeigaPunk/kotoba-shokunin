Result: HOLDS — the S034 Gate quote is verbatim at the cited location (HTML line 1114 under the § Support for server instructions heading at 1113), the row is a valid tier-A `docs`/`mined` row whose every field reproduces, and every S034-derived statement in the entry and SKILL.md is supported by the page; the only record defects are low-severity: the recorded sha256/byte count is not reproducible because the page carries a per-fetch A/B `awa-expId` meta tag, and the entry's reading cell generalizes an August-2025 release note into present tense.

Seat: KotobaR52a2.ReopenS034. Lane read at c8407a453788df964df5a7b835dd0ce1360de882 (working tree; only SCORECARD.md dirty, not touched). Sandbox: /fast/scratch/hyaku/kotoba-r52a2/ReopenS034/. No tool was installed or updated; nothing was written outside this report and that sandbox.

## Re-open evidence (ordinary curl, no browser)

| fetch | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | https://code.visualstudio.com/updates/v1_104 | 2026-10-22T17:50:08Z | 200 | 179,457 | `ee92f6454fb1e19ad9c85e605ee490a4128c8aeb3c672ec400f6c3c18b256e59` |
| 2 | https://code.visualstudio.com/updates/v1_104.md | 2026-10-22T17:52:22Z | 404 | 19,510 | `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95` |
| 3 (context) | https://code.visualstudio.com/docs/agent-customization/mcp-servers.md | 2026-10-22T17:52:01Z | 200 | 12,557 | `957e49242f60d335ee65e5ef40cb9098a41982f8d0c1b4a13a4bb20780fbcc5d` |
| 4 (context) | https://code.visualstudio.com/docs/agents/reference/mcp-configuration.md | 2026-10-22T17:52:37Z | 200 | 22,286 | `3849bb50504e62901c469133e7a7dbfb80c955af934356a1675c6cb9e5001abc` |

The round's own fetch copy survives at `/fast/scratch/hyaku/kotoba-r52/src/vscode-1104.html`: `sha256sum` = `19d9259e93ab3109cb243f33631494c9d2cc49546a5e90f5df6ea2765bd6e859`, 179,440 B — exactly the row (`corpus/SOURCES.md:47`) and the lesson Gate (`corpus/lessons/round-52.md:23-25`) values. So the anchor was a true record of the 17:05:11Z fetch.

Comparison with today's live bytes: `diff -u old.html v1_104.html` returns exactly one changed line, HTML line 6:
`<meta name="awa-expId" content="tv-downloadv2:1447446;" />` → `<meta name="awa-expId" content="tv-downloadv2:1447446;9ec16314:1468469;" />`.
The added experiment id is 17 bytes; 179,457 − 179,440 = 17. No line was added or removed, so line numbering is unchanged and the quote is still at the same line.

Quote, verbatim on today's bytes:
```
1112: ...<h2 id="_mcp" data-needslink="_mcp">MCP</h2>
1113: <h3 id="_support-for-server-instructions" ...>Support for server instructions</h3>
1114: <p>VS Code now reads MCP server instructions and will include them in its base prompt.</p>
1115: <h3 id="_mcp-auto-discovery-disabled-by-default" ...>MCP auto discovery disabled by default</h3>
```
Section structure: the § Support for server instructions subsection is heading (1113) plus one paragraph (1114); it is one sentence long. The next heading starts at 1115.

The `.md` variant: HTTP 404, 19,510 B, contains "Page not found", byte-identical to the round's scratch copy (`/fast/scratch/hyaku/kotoba-r52/src/vscode-1104.md`, same sha256). The row's claim that it "returned a 404 page" is exact.

## Statement verdicts (S034 and its uses)

| # | statement | where | verdict |
|---|---|---|---|
| S1 | row exists with the contract's 11 columns | `corpus/SOURCES.md:47`; field-split on the S034 row → `NF=13` | HOLDS |
| S2 | anchor: `§ MCP → § Support for server instructions`, HTML 1113-1114, revision 1.104 / August 2025 | page: h2 `_mcp` 1112, h3 1113, quote 1114; `<title>August 2025 (version 1.104)</title>` | HOLDS |
| S3 | `teaches` = "VS Code 1.104 reads MCP server instructions and includes them in its base prompt" | page line 1114; "1.104" from the page title | HOLDS |
| S4 | tier `A`, kind `docs`, for the scope "whether VS Code puts MCP server instructions in front of the model" | contract v1 (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`): A = primary or authoritative for the scope, official docs; release notes are the vendor's own statement of what the feature does | HOLDS |
| S5 | status `mined`, `used-by` = entry + lesson | both paths exist and cite S034 (`corpus/knowledge/mcp-server-instructions-round52.md:1,25`, `corpus/lessons/round-52.md:23`) | HOLDS |
| S6 | `opened` 2026-10-22 | fetch timestamp 17:05:11Z that date | HOLDS |
| S7 | recheck `on-release` | the claim is bound to a release; a later VS Code release is exactly when it can move (same cadence as S005/S008/S016) | HOLDS |
| S8 | the Gate quote (15 words, URL, access time) | `corpus/lessons/round-52.md:23-25`; 15 ≤ 25 words; quote matches page bytes exactly; location "HTML line 1114, § Support for server instructions" correct | HOLDS |
| S9 | `.md` variant was a 404 | fetch 2 above, 404, "Page not found" | HOLDS |
| S10 | entry source line `v1_104:1113-1114` | `corpus/knowledge/mcp-server-instructions-round52.md:1`; heading 1113, quote 1114 | HOLDS |
| S11 | entry quote cell | `:25` equals page line 1114 verbatim | HOLDS |
| S12 | entry location cell "release notes 1.104 (August 2025), § Support for server instructions" | page title and h3 | HOLDS |
| S13 | reading cell sentence 1: "Server instructions go into VS Code's base prompt." | page: "will include them in its base prompt" — same claim; the page's "now/will" marks the change introduced in 1.104, which the location cell pins | HOLDS (see D2) |
| S14 | reading cell sentence 2: "No length limit is stated in that section." | the subsection is heading 1113 + one sentence 1114 + next h3 1115; no limit text; the page's 9 `instructions` occurrences are the quote at 1114, the section id/heading at 1113 (3), an Arm-download link label at 371 (2), an `AGENTS.md` sentence at 506, "custom instructions" for prompt files at 551, and an ESLint release-note link at 1901 — none of them a limit on MCP server instructions; no `characters` limit near MCP; fetches 3 and 4 contain no server-instructions text at all | HOLDS |
| S15 | entry § What follows 1: "Four clients (Claude Code, VS Code, Codex, Gemini CLI) document that they put the text in front of the model" | `:42`; "base prompt" is the text put in front of the model — [INFERENCE], the vendor's own wording for the prompt | HOLDS |
| S16 | SKILL.md `:93`: "…Claude Code, VS Code (S034), Codex and Gemini CLI (S036) put `instructions` in front of the model already" | same inference as S15; no VS Code budget is claimed from S034 anywhere in SKILL.md or the entry | HOLDS |
| S17 | the statement S034 is used to back — the counter finds the quote on the live page | `python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882 --fetch` → exit 0; per-client line `VS Code BACKED found=True`; `mcp instructions backed 5 of 7 clients`; `mcp instructions found on the live page 5 of 5` | HOLDS |

Answer to "does the quote say what the reading cell says, in context": yes. The page's sentence is the vendor stating, in the MCP section of the 1.104 release notes, that the editor reads the server's `instructions` and places them in its base prompt; the reading cell says exactly that. Nothing in the surrounding section qualifies or narrows it (nothing about ordering, precedence, truncation or opt-out). The one thing the reading cell adds by dropping is the version, covered under D2.

## Defects, with severity

- **D1 — LOW (record reproducibility).** The row's and Gate's `179,440 B` / sha256 `19d9259e…` do not reproduce on a fresh open: the page injects a per-fetch A/B experiment id into `<meta name="awa-expId">` at HTML line 6 (today `tv-downloadv2:1447446;9ec16314:1468469;`, +17 B, sha256 `ee92f645…`). Every content line, the quote and the cited line numbers are identical, so the anchor still grounds the quote; the contract's rule 1 requires URL, access date and a located ≤25-word quote, all of which reproduce. Consequence: any future freshness check that treats the recorded hash as a re-verifiable anchor will emit a false BREAK on this page. Fix: append to the anchor "(hash varies with a per-fetch A/B `awa-expId` meta at HTML line 6; quote and line numbers are stable)" or drop the hash from the recheck basis. Not a BREAK of C2: the counter compares the quote, not the hash.
- **D2 — LOW (currency wording).** The entry's reading cell speaks in the present about behavior introduced by the August 2025 (1.104) release notes, in a document verified 2026-10-22. The version is pinned in the same row's location cell and the entry's Limits section bounds everything to documentation statements, so no reader is misled about the evidence class; but "as of 1.104" would remove the ambiguity. Whether later VS Code releases changed, limited or removed this is **not checked** (see unknowns). Not a BREAK of any S034 statement.
- **D3 — LOW, adjacent to S034 but not a statement from it.** `corpus/knowledge/mcp-server-instructions-round52.md:62` says the counter "checks that each row's quote is located". The frozen counter never reads the location cell (column 3): its per-row reads are `r[1]` (row id) and `r[2]` (quote), at `verifiers/check_mcp_instructions.py:200,226`; the quote checks are word count, the word `instructions`, and verbatim presence in the round lesson (`:227-235`). A row with an empty or wrong location cell would still be `BACKED`. Severity low (the sentence overstates the counter, not the row); I did verify S034's location by hand above. No lane edit made.

## Remaining unknowns

- VS Code releases after 1.104 (1.105 onward) were not opened; whether the base-prompt inclusion still holds, or gained a length limit, is unverified. The entry does not claim it, so this does not falsify S034 but bounds its currency.
- The page's byte size and hash are not stable anchors (D1); any re-verification must compare the quote and its line, not the digest.
