Result: MIXED — the C2 entry's provenance trio, five located quotes, sweep bounds and Limits all verify against re-fetched live bytes, but two sentences in `## What follows for the craft` are wider than their cited rows (line :50 "always-loaded" attributed to skills, line :55 "five clients" count).

Target: `corpus/knowledge/mcp-server-instructions-round52.md` @ `c8407a45` (working tree). All re-fetches by plain `curl` (UA `kotoba-shokunin-review/52` or `Mozilla/5.0`), 2026-10-22T17:54–17:55Z, saved under `/fast/scratch/hyaku/kotoba-r52a2/ReviewEntry/pages/` (scratch only, nothing written to the lane besides this report).

## Provenance trio (Q12) — HOLDS

- `source:` (:1) names S032–S037, each with URL and anchor; anchors match the SOURCES.md anchor cells verbatim (`SOURCES.md:45-50`, e.g. S033 `§ Tool search (mcp.md:1468); § Tool search for MCP server authors (:1476-1493)`).
- `verified-at: 2026-10-22` (:2) matches every row's `opened` cell and the Gate times (lesson :17-33, opened 17:04–17:07Z).
- `recheck:` (:3) runs: `python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882` → `mcp instructions backed 5 of 7 clients`, exit 0; `--fetch` → `found on the live page 5 of 5`, exit 0; `--rev c8579a4c…` (base) → `backed 0 of 7`, exit 1. Counter identical at the frozen plan commit: `git diff 4c003a4b c8407a45 -- verifiers/check_mcp_instructions.py` → empty (no post-plan widening, Q28 holds).
- One nuance in Limits (:62): "checks that each row's quote is located" is true only under `--fetch` (script :243-252); without it the quote is checked only for shape, word count, host and Gate presence. The stated recheck command does include `--fetch`, so the line is accurate for the documented recheck.

## Per-client record — every quote verified on live bytes

| row | re-fetch | verdict |
|---|---|---|
| S032 spec | 130,800 B, sha256 `5ab7cfcd5ea05c74` — byte-identical to Gate | quote verbatim at `spec.md:463`; the continuation "to improve the LLM's understanding … like a \"hint\" to the model … MAY be added to the system prompt" also verbatim in the same line. Row reading accurate. |
| S033 Claude Code | 128,298 B, `9ec4942d` — **drifted** (Gate: 127,022 B, `9a42e98f`) | quote verbatim, now `:1488` (recorded `:1468`); skills comparison now `:1496` (recorded `:1476`); 4,096 limit now `:1506` (recorded `:1484-1486`). See F3. |
| S034 VS Code | 179,457 B, `ee92f645` — +17 B vs Gate 179,440 B | quote verbatim at HTML `:1114`, under `### Support for server instructions` at `:1113`. Reading accurate. |
| S035 Codex | 26,995 B, `c78df8c7` — byte-identical (needed `curl -L`; the bare URL 308-redirects, counter's urllib follows it) | quote verbatim `:197`; "cross-tool workflows, constraints, and rate limits" and "first 512 characters self-contained" verbatim `:199`. |
| S036 Gemini CLI | 43,656 B, `4aefc4dc` — byte-identical | quote verbatim `:1315`, inside `## Instructions` at `:1311`. |
| S037 blog | 49,781 B, `96794ff9` — byte-identical | quote verbatim in § A Note for Client Implementers: "we recommend that you expose instructions to users and provide transparency about what servers are injecting into context". § Currently Supported Host Applications defers to the Clients page — the blog itself lists no clients. |

## `## What follows for the craft` — sentence-by-sentence

- :42-43 item 1 — HOLDS. Checked each of the four: Claude Code "server instructions load at session start" (:1488, correctly scoped to tool search in the row), VS Code "include them in its base prompt", Codex "server-wide guidance alongside the server's tools" (weakest — implies, rather than states, model-facing, but :199's "when Codex is deciding how to use the server" supports it), Gemini "appended to the system instructions". The `(:199)` cite for "cross-tool workflows…" is verbatim.
- :44-46 item 2 — HOLDS. 4,096 is the documented default (page: "cuts a tool description or server instructions that run past these default limits", configurable via `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` — "by default" is precise); the 512 cell is verbatim. "A text written to the smaller budget is safe in both" is the stated craft inference, bounded to the two documented budgets.
- :47-48 item 3 — HOLDS. Spec field is `instructions?` optional and placement is client-chosen ("MAY be added to the system prompt"). "two of the seven clients" counts opencode and Copilot CLI correctly; "clients" inherits the counter's own wording (`backed 5 of 7 clients`, spec counted as a client) — convention, not a defect.
- :49-52 item 4 — **F1 (low).** :50 "both are always-loaded text" is wider than the cited row. The page (:1496) compares only function — "Server instructions help Claude understand when to search for your tools, **similar to how skills work**" — and never says skills are always-loaded text (always-loaded is documented on the page for server instructions only, :1488). The functional comparison and the overlap point hold; the "always-loaded" premise for skills rests on outside knowledge. The `skill-overlap-levers-round51.md` cross-reference is a valid internal row.
- :53-55 item 5 — quote and recommendation verified verbatim (S037), and "was not checked" is honest. **F2 (low):** :55 "any of the five clients" is ambiguous/inconsistent — item 1 documents *four* clients; the fifth backed row is the specification, which is not a client. If the intended set is the seven checked, the sweep already covers the two silent ones; as written the count has no clean referent (the blog lists no client names, deferring to the Clients page).

## Negatives bounded (Q14) — HOLDS

- opencode (:29-32): re-fetched `opencode.ai/docs/mcp-servers.md` → 200, 13,941 B, `12ed2af6c5f4` (byte-identical to Gate), `grep -ci instructions` → 0; raw `.mdx` → 200, 14,015 B, `ad6e6687ab4c`, grep → 0.
- Copilot CLI (:33-36): `add-mcp-servers.md` → 200, 14,240 B, `640035aa0936` (byte-identical); single `instructions` hit at line 22 — "For installation instructions, available tools, and URLs for specific MCP servers, see the GitHub MCP Registry" — matches "about installation instructions in the GitHub MCP Registry". `concepts/context/mcp.md` → 404, 502 B "Page not found".
- The bound itself (:36-37) is honest: "the clients' source code was not read, so 'does not use server instructions' is not claimed." Consistent with the corpus: the round-13 census already recorded opencode's `<mcp_instructions>` prompt surface (`instruction-surface-census-round13.md:283`, commit `5cc1340`), so the entry correctly claims only documentation silence, not absence.

## Limits — HOLDS

- :59 "Documentation statements only" matches :16 and every row's teaches/scope cell ("vendor documentation, not a measurement").
- :60 omp unchecked — consistent with PROVINCE:19 keeping measured client behaviour on Frontier.
- :61-63 counter description accurate per script review (located/short/`instructions`/host/Gate checks at :196-235; `reading` cell verified by no check — :62 says so itself).

## Findings (severity)

- **F1 — low** — `mcp-server-instructions-round52.md:50`: "both are always-loaded text" attributes always-loaded status to skills; the cited page (`claude.md:1496`, recorded :1476) supports only the functional comparison. One-word fix direction: drop "always-loaded" for the skill side or re-ground it.
- **F2 — low** — `mcp-server-instructions-round52.md:55`: "the five clients" has no clean referent (four documented clients + spec). Fix direction: "any client" or "the four clients above".
- **F3 — verification gap (no defect in the entry)** — `code.claude.com/docs/en/mcp.md` drifted within ~50 minutes of the Gate fetch (17:04Z): 127,022 → 128,298 B, new sha, all three cited line anchors now sit ~20 lines low (quote `:1468`→`:1488`, skills `:1476`→`:1496`, limit `:1484-1486`→`:1506`). `v1_104` gained 17 B. Quotes remain verbatim on live bytes and `--fetch` still passes 5 of 5, but the entry's line-level anchors age fast on that page; the Gate's byte-pinned record (:20-22) is the durable evidence.

## Tooling

No installs or upgrades were needed; `curl`, `python3`, `git` already present. Pacman untouched.

Report: .ufo/waves/round-52/falsify-a2/ReviewEntry.md
