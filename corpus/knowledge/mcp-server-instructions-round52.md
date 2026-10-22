source: S032 (https://modelcontextprotocol.io/specification/2025-11-25/schema.md, `schema.md:461-463` § InitializeResult), S033 (https://code.claude.com/docs/en/mcp.md, `mcp.md:1468, 1476-1493` § Tool search), S034 (https://code.visualstudio.com/updates/v1_104, § Support for server instructions, `v1_104:1113-1114`), S035 (https://developers.openai.com/codex/mcp.md, `mcp.md:197-199`), S036 (https://geminicli.com/docs/tools/mcp-server.md, § Instructions `mcp-server.md:1311-1315`), S037 (https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/, § A Note for Client Implementers)
verified-at: 2026-10-22
recheck: python3 -B verifiers/check_mcp_instructions.py --rev <rev> --fetch

# MCP server `instructions`: what each client does with them (round 52)

Frontier area: MCP and plugin instruction surfaces (`corpus/README.md` § Frontier;
`PROVINCE.md` § Frontier). Round 13 (`instruction-surface-census-round13.md` § C) found the MCP
configuration keys absent from this host's two harness configs and named the class live anyway; it
did not record what text an MCP server puts in front of the model. This entry holds one such
surface: the optional `instructions` string a server returns in its `initialize` result. It is
server-wide text, written by the server author, that sits beside the tool descriptions and competes
for the same context as skills and always-on files.

Every page below was opened on 2026-10-22 by the L1 (fetch times, byte counts and sha256 in
`corpus/lessons/round-52.md` § Gate). These are documentation statements, not measured client
behaviour.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|
| MCP specification | S032 | "Instructions describing how to use the server and its features." | `schema.md:463`, § InitializeResult, field `instructions?: string` (spec 2025-11-25) | The field is optional and server-sent. The same schema text goes on: clients can use it "to improve the LLM's understanding of available tools, resources, etc." and it is "like a "hint" to the model". The 2025-11-25 schema text does not say where a client must place it. |
| Claude Code | S033 | "Only tool names and server instructions load at session start, so adding more MCP servers has minimal impact on your context window." | `mcp.md:1468`, § Tool search | With tool search, server instructions are always in context while tool definitions are deferred; the page says instructions "help Claude understand when to search for your tools" (`:1476`) and cuts server instructions longer than 4,096 characters by default (`:1484-1486`). |
| VS Code | S034 | "VS Code now reads MCP server instructions and will include them in its base prompt." | release notes 1.104 (August 2025), § Support for server instructions | Server instructions go into VS Code's base prompt. No length limit is stated in that section. |
| Codex | S035 | "Codex reads the MCP `instructions` field returned during initialization and uses it as server-wide guidance alongside the server's tools." | `mcp.md:197` | Codex uses the text as server-wide guidance and advises keeping "the first 512 characters self-contained" (`:199`). |
| Gemini CLI | S036 | "which will be appended to the system instructions." | `mcp-server.md:1315`, § Instructions | Gemini CLI supports MCP server instructions and appends them to its system instructions (`:1313-1315`). |

Not counted, with the sweep (Q14): **opencode** — `https://opencode.ai/docs/mcp-servers.md`
(13,941 B, sha256 `12ed2af6c5f4…`) and the docs source
`raw.githubusercontent.com/sst/opencode/dev/packages/web/src/content/docs/mcp-servers.mdx`
(14,015 B) contain `instructions` 0 times. **Copilot CLI** —
`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md`
(14,240 B) contains `instructions` once, about installation instructions in the GitHub MCP
Registry, never about server instructions; `https://docs.github.com/en/copilot/concepts/context/mcp.md`
returned a 404 page. Both statements are bounded to the pages opened on 2026-10-22: the clients' source
code was not read, so "does not use server instructions" is not claimed.

## What follows for the craft

1. **Server-wide guidance belongs in `instructions`, not repeated in every tool description.**
   Four clients (Claude Code, VS Code, Codex, Gemini CLI) document that they put the text in front of
   the model; Codex names its use for "cross-tool workflows, constraints, and rate limits" (`:199`).
2. **Front-load it.** The documented budgets differ: Claude Code cuts at 4,096 characters by default;
   Codex asks for the first 512 characters to stand alone. A text written to the smaller budget is
   safe in both.
3. **Do not rely on it everywhere.** The specification makes the field optional and leaves placement
   to the client; two of the seven clients checked here document nothing about it.
4. **It is an instruction surface that a skill author does not control.** In Claude Code the page
   compares server instructions to skills (`:1476`): both are always-loaded text that decides when the
   model reaches for a capability, so an MCP server's `instructions` can overlap a skill's description
   the same way two skill descriptions can (`skill-overlap-levers-round51.md`).
5. **Client implementers are asked to show it.** The MCP blog (S037) recommends that a client
   "expose instructions to users and provide transparency about what servers are injecting into
   context". Whether any of the five clients does so was not checked.

## Limits

- Documentation statements only; no client was run against a server that sends `instructions`.
- omp, kotoba's own host harness, was not checked this round.
- The counter (`verifiers/check_mcp_instructions.py`, frozen at the round-52 plan commit `4c003a4b`)
  checks that each row's quote is located, short, contains `instructions`, sits on the client's own
  host and is in the round's Gate; whether the `reading` cell is right is reviewer judgment.
