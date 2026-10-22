source: S032 (https://modelcontextprotocol.io/specification/2025-11-25/schema.md, `schema.md:461-463` § InitializeResult), S033 (https://code.claude.com/docs/en/mcp.md, `mcp.md:1468, 1476-1493` § Scale with MCP tool search), S034 (https://code.visualstudio.com/updates/v1_104, § Support for server instructions, `v1_104:1113-1114`), S035 (https://developers.openai.com/codex/mcp.md, `mcp.md:197-199`), S036 (https://geminicli.com/docs/tools/mcp-server.md, § Instructions `mcp-server.md:1311-1315`), S037 (https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/, § A Note for Client Implementers), S040 (https://modelcontextprotocol.io/specification/2026-07-28/schema.md, § DiscoverResult `schema.md:1293, 1301-1304`), S041 (https://raw.githubusercontent.com/anomalyco/opencode/cdf1c200a671378458b50f9e3167405f1f326b24/services/www/src/docs/content/mcp-servers.mdx, § Server instructions `:427-441`), S042 (https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md, `:2895`, `:1157`)
verified-at: 2026-10-22
recheck: python3 -B verifiers/check_mcp_instructions.py --rev <rev> --fetch

# MCP server `instructions`: what each client does with them (round 52)

Frontier area: MCP and plugin instruction surfaces (`corpus/README.md` § Frontier;
`PROVINCE.md` § Frontier). Round 13 (`instruction-surface-census-round13.md` § C) found the MCP
configuration keys absent from this host's two harness configs and named the class live anyway; its
line 283 already recorded opencode's MCP server instructions (`<mcp_instructions>`) as a non-file
prompt surface, without a per-client record or an authoring rule. This entry holds one such surface:
the optional `instructions` string a server returns in its `initialize` result (spec revision
2025-11-25, S032; in the current revision 2026-07-28 the `initialize` handshake is removed and the
field sits on the `server/discover` result, S040). It is server-wide text, written by the server
author, that clients document placing beside the tool descriptions or in the system prompt, where it
competes for the same context as skills and always-on files.

Every page below was opened on 2026-10-22 (fetch times, byte counts and sha256 in
`corpus/lessons/round-52.md` § Gate). These are documentation statements, not measured client
behaviour.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|
| MCP specification | S032 | "Instructions describing how to use the server and its features." | `schema.md:463`, § InitializeResult, field `instructions?: string` (spec 2025-11-25) | The field is optional and server-sent. The same schema text goes on: clients can use it "to improve the LLM's understanding of available tools, resources, etc." and it is "like a "hint" to the model". The 2025-11-25 schema text does not say where a client must place it. |
| Claude Code | S033 | "Only tool names and server instructions load at session start, so adding more MCP servers has minimal impact on your context window." | `mcp.md:1468` (pinned bytes; `:1488` on the 17:50Z re-open), § Scale with MCP tool search | With tool search, server instructions load at session start while tool definitions are deferred; the page says instructions "help Claude understand when to search for your tools" (`:1476`) and cuts server instructions longer than 4,096 characters by default (`:1484-1486`). |
| VS Code | S034 | "VS Code now reads MCP server instructions and will include them in its base prompt." | release notes 1.104 (August 2025), § Support for server instructions | As of 1.104, server instructions go into VS Code's base prompt. No length limit is stated in that section. |
| Codex | S035 | "Codex reads the MCP `instructions` field returned during initialization and uses it as server-wide guidance alongside the server's tools." | `mcp.md:197` | Codex uses the text as server-wide guidance and advises keeping "the first 512 characters self-contained" (`:199`). |
| Gemini CLI | S036 | "which will be appended to the system instructions." | `mcp-server.md:1315`, § Instructions | Gemini CLI supports MCP server instructions and appends them to its system instructions (`:1313-1315`). |
| opencode | S041 | "When a server returns instructions during initialization, OpenCode adds them to the system prompt:" | `mcp-servers.mdx:429`, § Server instructions (docs source, commit pinned in the S041 URL) | opencode puts the text in the system prompt inside an `<mcp_instructions>` block (`:431-437`) and omits a server's instructions when the agent's permissions deny every one of its tools (`:441`). |
| Copilot CLI | S042 | "Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts" | `changelog.md:1157`, § 1.0.66 - 2026-06-30 (changelog, commit pinned in the S042 URL) | Copilot CLI added "MCP server instructions support" in 0.0.400 (`:2895`, 2026-01-30). Its command reference (S038's page, `cli-command-reference.md:660`, sha256 `c61997ef…`) states the default the flag changes: "By default, only allowlisted server instructions are included up front; other servers' instructions are retrieved on demand." How a server becomes allowlisted is not stated there (seat `SweepCopilotCli`). |

Sweep record (Q14), kept as found and corrected: at `c8407a45` the opencode and Copilot CLI rows were
recorded as not counted, because `https://opencode.ai/docs/mcp-servers.md` (13,941 B, sha256
`12ed2af6c5f4…`), the docs source path `packages/web/src/content/docs/mcp-servers.mdx` (14,015 B) and
`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md`
(14,240 B) contain no statement about server instructions. That negative was wrong: the opened
opencode path had been superseded by `services/www/src/docs/content/mcp-servers.mdx`, and Copilot
CLI states its support in its changelog, not on the how-to page (falsify seat `CriticLearning`,
attempt 2; rows S041 and S042 opened and quotes re-checked by the L1 at 17:57Z).

## What follows for the craft

1. **Server-wide guidance belongs in `instructions`, not repeated in every tool description.**
   The current specification says so directly: the text "should not duplicate information already in
   tool descriptions" (S040, `schema.md:1304`). Six clients (Claude Code, VS Code, Codex, Gemini CLI,
   opencode, Copilot CLI) document that they put the text in front of the model; Codex names its use
   for "cross-tool workflows, constraints, and rate limits" (`:199`).
2. **Front-load it.** The documented budgets differ: Claude Code cuts at 4,096 characters by default;
   Codex asks for the first 512 characters to stand alone. A text written to the smaller budget is
   safe in both.
3. **Do not rely on it everywhere.** The specification makes the field optional and leaves placement
   to the client (2025-11-25; the 2026-07-28 text gives a system prompt only as an example, S040).
   Clients also drop it: opencode omits a server's instructions when the agent's permissions deny
   all of its tools (S041), and Copilot CLI needs a flag to include instructions from all servers
   (S042). Guidance every session must see belongs in a skill or always-on file as well.
4. **It is an instruction surface that a skill author does not control.** Claude Code's page says
   server instructions "help Claude understand when to search for your tools, similar to how skills
   work" (S033, `:1476`): both are text that decides when the model reaches for a capability, so an
   MCP server's `instructions` can overlap a skill's description the same way two skill descriptions
   can (`skill-overlap-levers-round51.md`).
5. **Client implementers are asked to show it.** The MCP blog (S037) recommends that a client
   "expose instructions to users and provide transparency about what servers are injecting into
   context". Whether any of the six clients does so was not checked.

## Limits

- Documentation statements only; no client was run against a server that sends `instructions`.
- omp, kotoba's own host harness, was not checked this round.
- Spec revision: S032 is the 2025-11-25 text, where the field sits on `InitializeResult`. The current
  revision 2026-07-28 removes the `initialize` handshake and moves the field to the `server/discover`
  result (S040, `changelog.md:14, 16`). Codex and opencode still describe the field as returned
  "during initialization"; which revision each client speaks was not checked.
- The counter (`verifiers/check_mcp_instructions.py`, frozen at the round-52 plan commit `4c003a4b`)
  reads the `client`, `row` and `quote` cells only. It checks that the quote is 3 to 25 words and
  contains `instructions`, that the cited row is tier A, `mined`, opened 2026-10-22, on the client's
  pinned host and names this entry in `used-by`, and that the lesson file contains the row id and the
  quote anywhere. It does not read the `location` cell, does not require the quote to sit in the
  lesson's `## Gate` section, and does not judge the `reading` cell or whether the quote is about
  server instructions (attempt-2 falsify seats `CriticC2Sizing`, `ReopenS032`, `ReopenS034`). Each
  location and reading above was re-checked by a falsify seat re-opening the page.
- Page drift seen on re-open (17:50Z): S033's page gained a section, so the quote moved from `:1468`
  to `:1488` (still verbatim, once); S034's HTML changes one per-fetch meta line, so its byte count
  and sha256 do not reproduce while the quote and line do; S035's URL now answers 308 to
  `learn.chatgpt.com/docs/extend/mcp.md?surface=cli` with byte-identical content.
- Gemini CLI: the rendered site carries a banner saying Gemini CLI "was replaced by Antigravity CLI"
  for some account types (seat `ReopenS036`; not on the `.md` route S036 cites). The row records
  documentation, not which users still run the client.
