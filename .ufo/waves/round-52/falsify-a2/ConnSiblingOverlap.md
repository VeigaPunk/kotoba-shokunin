Result: MIXED — C2's entry absorbs no sibling's ground (0 contested, 0 new adjacent across 20 sibling lanes), but its protocol premise ("returns in its `initialize` result") is stale against the current MCP revision, which a sibling (kumitate) has recorded since 2026-10-19 and which removes `initialize` and moves `instructions` to `server/discover`.

Seat: ConnSiblingOverlap (connector, falsify wave attempt 2, round 52). Target: C2 scope (adjacency). Judged revision: kotoba `master` at `c8407a453788df964df5a7b835dd0ce1360de882`. Run 2026-10-22, 17:49Z to 17:55Z. Tooling installs: none.

## 1. Sweep method (sibling bytes read with read-only git at each lane's branch tip)

The scan used `git -C <lane> grep` at the `master` or `main` ref and read only committed bytes. Nothing in any sibling was written. The tip I read in each lane:

| lane | tip read | census pin (round 49) | moved |
|---|---|---|---|
| audio | 7a2fcd4f08831154686e4e323031f41fffdb077f | same | no |
| chousa | 6c5eb1466f2b8abbd3de576389037f435016d07b | same | no |
| game-dev-2d | 7753d49b16674e122ed134403e7a9b301f2cbf7e | same | no |
| game-dev-3d | 89dd182b70943a20ae9aa6c1ed0e3c9b6e79c080 | same | no |
| kagi | 899c50b42634a3a4ad0b28ab7509786315e2fc2b | same | no |
| kaidoku | a267311678309fd17772407e8afa122ec3219289 | 08c7a729… | yes |
| kake | 92235a0578b04458c5eb96c966f82fa03593130e | e73d48bb… | yes |
| kama | 1560e4d83f42b04f40336357de6f9637eafa0f4b | c808ba07… | yes |
| kasegi | 1fafde8f11454f3b0b98ab7f2b2e640aaf7f399a | same | no |
| kengaku | 1f3b0f1ec41ec297130e8944ff97968d32324632 | same | no |
| kotodama | 7fa37fbb6f0a0c39b3d6cfd3d371f5bb3a65050c | 35f0d49f… | yes |
| kumitate | fae386aa9e0542710b7a893d84c8e92e86fc079b | fac39171… | yes |
| lore | 380ef3abc7c7af11d7f23e9f9c82bb1937e1f695 | same | no |
| mado | 8e5d93691e2f7baa3d4a0a61c9428e5acb5d2122 | e33ea304… | yes |
| mori | df886be1cc75f1052002698bdb4a3d18a2eaf6c6 | 28b79d3d… | yes |
| revenger | 876630dbb4d630e016d7d8c32a19ea04c646cbae | same | no |
| souji | 4edb25dfe262515d0da63224bbba71e02e36cba5 | same | no |
| tabi | e3cf4e0d30bb835532ff44b118c5ad52e09eb76d | same | no |
| tameshi | 06b59b93697c9b0a8795ac2d0fe3d0bd7e18572c | 3b20f073… | yes |
| tsukuroi | 2e519d615135ba3b3d60dcd19a5642dc0d4391f9 | 22fd1642… | yes |

Sweeps, all exit 0:

- **Pattern 1 (broad MCP):** `\bmcp\b|InitializeResult|mcpServers|mcp\.json|server instructions|tool descriptions?`, case-insensitive, over `PROVINCE.md SKILL.md corpus/README.md corpus/knowledge/*`.
  - Lanes with hits: game-dev-3d, kaidoku, kumitate, tabi, kagi, kake, kasegi, kengaku and revenger.
  - Lanes with 0 hits: audio, chousa, game-dev-2d, kama, kotodama, lore, mado, mori, souji, tameshi and tsukuroi.
- **Pattern 2 (the C2 field itself):** `InitializeResult|"instructions"|instructions\?|server[- ]instructions|serverInfo|initialize(d)? result|instructions field|instructions string`, same file set. The only hits are revenger `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md:527,579-585`, which are EVM opcode `"instructions"` arrays and unrelated. So **no sibling scope surface mentions MCP server `instructions` or `InitializeResult`.**
- **Frontmatter description:** extracted from each `SKILL.md` and grepped for `\bmcp\b|instructions|tool description`. The count is 0 in all 17 lanes that have a skill file (audio, game-dev-2d and revenger have none).
- **Co-occurrence:** `kotoba.*\bmcp\b|\bmcp\b.*kotoba` over `PROVINCE.md SKILL.md corpus/*` in all 20 lanes gives 0 lines. No sibling scope surface routes MCP text to kotoba, or away from it.
- **Corpus outside `knowledge/`:** the same broad pattern over `corpus/*` excluding `knowledge/` and `README.md`. Hits are kaidoku lessons (REA session and registration facts), game-dev-3d lessons (paths under `unreal-mcp`), kumitate `corpus/SOURCES.md:18-24,32,35,37,39`, kengaku evidence (`--no-webui-mcp-proxy` flags, MCP-Atlas) and audio `corpus/live/*` ("MCP servers: rea only"). None of these makes a wording claim.
- **Whole trees, including wave reports (not scope surfaces):** run for completeness. The only real server `instructions` values are kaidoku `.ufo/waves/luna-round-{2,6,8}/receipts/*`, which hold REA's live `initialize` result (section 4, finding F3).

## 2. Per-hit classification under kotoba's census rule

The rule is in `corpus/knowledge/sibling-overlap-census-round49.md:43-58`, with the round-50 precedence at `:252-260` and `:319-324`. The element classified is C2's ground: the wording and placement of MCP server `instructions`, and the per-tool `description` placement in `SKILL.md:86-94`.

| # | lane | file:line | quote (verbatim) | MCP ground | class |
|---|---|---|---|---|---|
| 1 | kaidoku | `PROVINCE.md:15-17` | "configured REA MCP pins are Devin `rea-agents@6.7.0` (`/home/vgpnk/.config/devin/mcp_config.json:7`), OMP `rea-agents@6.7.0` (`/home/vgpnk/.omp/agent/mcp.json:8`)" | MCP client configuration for the REA server, across three client config files | none |
| 2 | kaidoku | `corpus/knowledge/2026-10-13-mcp-registrations.md:3,5` | "# kaidoku-r1 — REA MCP registration surface (this host)" / "Scope: which MCP clients on this host have the `rea` server registered" | REA registration ownership (also `corpus/README.md:15,84`) | none |
| 3 | kumitate | `PROVINCE.md:14` | "Kimi Code substrate `~/.kimi-code/` — rows K1–K5, gated by `scripts/kimi-census.mjs`" | the Kimi MCP client plane, a Core element | none |
| 4 | kumitate | `corpus/knowledge/kimi-mcp-plane.md:5,9` | "# K1 — MCP plane: `~/.kimi-code/mcp.json`" / "The Kimi Code CLI reads its MCP servers from mcp.json files, not from `config.toml`." | MCP client configuration (Kimi) | none |
| 5 | kumitate | `corpus/knowledge/kimi-mcp-plane.md:67-68` | "the `rea` MCP server registration itself is kaidoku's surface (report, never absorb — QUALITY Q9)" | sibling-to-sibling split (kumitate and kaidoku) | none for kotoba |
| 6 | kumitate | `PROVINCE.md:20` | "MCP protocol revisions as they bear on orchestration — `corpus/SOURCES.md` rows, queued." | MCP spec revisions (Frontier) | none (no split; a dependency, see F1) |
| 7 | kumitate | `corpus/SOURCES.md:23` | "MCP goes stateless: sessions and Mcp-Session-Id removed; server/discover; MRTR; tasks as extension" (row S010, status `queued`, 2026-10-19) | the 2026-07-28 revision that moves `instructions` | none (dependency, see F1) |
| 8 | kumitate | `corpus/SOURCES.md:37` | "OMP-native MCP config: project .omp/mcp.json and user ~/.omp/agent/mcp.json are the primary server-definition files" (row S024) | omp MCP client configuration | none |
| 9 | kumitate | `PROVINCE.md:26` | "MCP/OAuth security practice (token passthrough, confused deputy) → kasegi / kagi." | MCP security routing | none |
| 10 | tabi | `corpus/knowledge/webmcp-chromium-loopback-round-16.md:136-138` | "The REA `discover_webmcp_tools` verb and MCP server registration are kaidoku's; the agent-side MCP plane is kumitate's; authoring WebMCP tools for the operator's own published properties is kake's" | MCP ownership map; does not name kotoba | none |
| 11 | tabi | `corpus/knowledge/webmcp-chromium-loopback-round-16.md:101` | "**no**: shared vocabulary only (`name`, `description`, `inputSchema`; S037); result shapes and lifecycles differ" | WebMCP page tools are not MCP tools | none |
| 12 | tabi | `corpus/knowledge/webmcp-invocation-round-17.md:117` | "Agent-side MCP plane: kumitate. Authoring tools for the operator's own properties: kake." | same map | none |
| 13 | kake | `SKILL.md:28` | "\| app.ds4cc.com \| `https://app.ds4cc.com/mcp` \| `ds4cc-marketplace/apps-sdk` + `render.yaml` \|" | an operator-owned MCP endpoint (property, not wording) | none |
| 14 | game-dev-3d | `corpus/knowledge/unreal-mcp/upstream/skills/create-toolset/SKILL.md:276` | "All AI-callable tools use `@toolset_registry.tool_call` followed by `@staticmethod`. The docstring becomes the AI-visible tool description." (same at `:89` for C++) | MCP tool-description authoring guidance in **vendored upstream** bytes | none (no fleet lane owns these files; precedent at census `:319-324`) |
| 15 | game-dev-3d | `corpus/knowledge/unreal-mcp/upstream/skills/unreal-skill/SKILL.md:56` | "`instructions` is a class attribute string containing the guidance loaded when the skill activates." | an Unreal Agent Skill payload, not `InitializeResult.instructions` (same word, different surface) | none |
| 16 | kagi | `corpus/knowledge/config-layering.md:46` | "- **`mcp`**: empty — global defines none for janitor." | opencode config layering | none |
| 17 | revenger | `corpus/knowledge/seed.md:62` | "\| F07 \| no MCP server registered (`:10-11`) \| server keys in `~/.omp/agent/mcp.json` (no values read) \|" | REA readiness, read-only registration check (also `2026-10-12-rea-readiness-checklist.md:15,38`) | none |
| 18 | kengaku | `SKILL.md:40` | "\| MCP tool orchestration \| MCP-Atlas \| 36 real MCP servers / 220 tools / 1,000 tasks — tool discovery & orchestration \|" | measuring MCP tool use; C2 measures nothing (entry `:59`) | none |
| 19 | kasegi | `corpus/knowledge/ufo-archive-2026.md:51` | "Archive paths `claim-packages/<slug>` (coinbase, metamask mm01, mongodb-mcp)" | a claim-package name | none |

**Counts on this element:** 19 hits in 9 lanes, all `none`; 0 `adjacent`; 0 `contested`. No hit claims the wording or placement of MCP server `instructions` or of tool descriptions, and no hit states a split of that text with kotoba. The census counts (9 adjacent, 11 none, 0 contested) are not affected.

Two corroborations sit outside scope surfaces and do not count under the rule (`:54-56`):

- tabi `.ufo/waves/round-16/drafts/DraftAdjacency.md:39` (at `e3cf4e0d`): "**C-C — tool names, descriptions and schemas as agent-facing text.** These are prompt-like strings read by a model. kotoba owns the craft of such text". This is a wave draft that never reached tabi's scope surfaces; census `:171-176` already records it.
- kama `corpus/knowledge/cross-lane-scope.md:29` (re-read at `1560e4d8`, unchanged from the census pin): "**Kotoba** owns the instruction/agent surface and its model/fallback wording". Its scope is agent files and model/fallback wording, so stretching it to MCP server text would be my inference. [INFERENCE]

**Attack A1, "Does C2's entry absorb a sibling's ground?": HOLDS.**

The fleet's MCP ground divides as follows: REA server registration and client config is kaidoku's; the Kimi MCP plane and MCP protocol revisions are kumitate's; WebMCP page tools are tabi's, with WebMCP authoring kake's; MCP security goes to kasegi and kagi; MCP-Atlas measurement is kengaku's; vendored Unreal toolset guidance sits with game-dev-3d.

C2 takes none of these:

- It touches no client config file. Its sources are client docs and spec text.
- It measures nothing ("Documentation statements only", entry `:59`).
- Its omp gap ("omp, kotoba's own host harness, was not checked", `:60`) leaves the omp config side unclaimed.

## 3. Findings

### F1 — the protocol premise is stale against the current MCP revision. Severity: medium (freshness and correctness of held craft; the count does not change)

**What kotoba says:**

- Entry `corpus/knowledge/mcp-server-instructions-round52.md:11`: "the optional `instructions` string a server returns in its `initialize` result".
- `SKILL.md:87`: "server-wide text the server returns at `initialize`; the spec makes it optional and leaves placement to the client."
- `PROVINCE.md:19` moves this to Core.
- `git grep -nE '2026-07-28|server/discover|DiscoverResult|stateless' c8407a4` matches only unrelated omp binary strings under `.ufo/round-44/evidence/` ("stateless reset" and similar). Kotoba never mentions the 2026-07-28 revision.

**What the spec says.** Fetched with `curl -sSL`, HTTP 200 for each:

| UTC | bytes | sha256 | URL |
|---|---|---|---|
| 2026-10-22T17:51:49Z | 11,855 | `b4c487760d46daf05ae30aea467516794af2dabe806b5fda43f9db9c7edc7c29` | https://modelcontextprotocol.io/specification/2026-07-28/changelog.md |
| 2026-10-22T17:51:49Z | 214,138 | `6daa817b8e9fec97ff86197dca32dbca8fdf4ec13df01aa9d1251630e2360c11` | https://modelcontextprotocol.io/specification/2026-07-28/schema.md |
| 2026-10-22T17:51:52Z | 130,800 | `5ab7cfcd5ea05c7491637e76122362cc4416201ea0c81482f6747f59343f1691` | https://modelcontextprotocol.io/specification/2025-11-25/schema.md (byte-identical to the S032 row's `5ab7cfcd…`) |
| 2026-10-22T17:51:53Z | 3,219 | `06e45272cc902fc0a8b7376ec60086793c96e10102860ece9650ebb97200bb5f` | https://modelcontextprotocol.io/specification/versioning.md |

Verbatim quotes:

- `versioning.md:25`: "The **current** protocol version is [**2026-07-28**](/specification/2026-07-28/)."
- `versioning.md:64-66`: "handshake-based protocol revisions (`2025-11-25` and earlier), see [Backward Compatibility](…)"
- `changelog.md:14`: "2. Make MCP stateless: remove the `initialize`/`notifications/initialized` handshake."
- `schema.md` (2026-07-28):
  - `:1293`, in `interface DiscoverResult`: "[instructions](#discoverresult-instructions)?: string;"
  - `:1301-1304`: "Natural-language guidance describing the server and its features. This can be used by clients to improve an LLM's understanding of available tools (e.g., by including it in a system prompt). It should focus on information that helps the model use the server effectively and should not duplicate information already in tool descriptions."
- `schema.md:463` (2025-11-25, the S032 bytes): "…It can be thought of like a "hint" to the model. For example, this information MAY be added to the system prompt."

**What follows:**

- Under the current revision the field is still optional and server-sent, so craft rules 2 and 3 stand.
- It now arrives on `server/discover`, not on `initialize`. The 2025-11-25 statement holds for handshake-based peers only.
- The current text states C2's craft rule 1 in the spec's own words: "should not duplicate information already in tool descriptions". It is lowercase "should", not RFC 2119 SHOULD. Entry `:41` and the `SKILL.md:93` row derive that rule from client docs alone. The rule is right; the spec support is missing.

**Sibling side.** kumitate registered the revision on 2026-10-19 (`corpus/SOURCES.md:23`, row S010, status `queued`) and named spec revisions as its Frontier (`PROVINCE.md:20`). This is a dependency, not an overlap: kotoba reads one field's wording purpose, and kumitate reads revisions as they bear on orchestration.

**Not broken:** S032's quote still locates, because the URL is versioned and the bytes are identical. So `check_mcp_instructions.py` still prints `5 of 7`. F1 attacks the reading and the craft premise, not the counter.

### F2 — kotoba's own corpus contradicts "opencode is silent". Severity: low to medium (internal consistency; not sibling ground)

- `corpus/knowledge/instruction-surface-census-round13.md:283` at `c8407a4`: "| opencode non-file prompt surfaces: MCP server instructions (`<mcp_instructions>`), references (`<available_references>`), … | doc | they reach the prompt but are **not file classes**…".
- C2 entry `:29-37` records opencode as not counted (`instructions` 0 times on the two pages opened), and `SKILL.md:94` says those pages "say nothing about server instructions".
- The entry does bound itself ("the clients' source code was not read"), but it does not reconcile the lane's own round-13 record of an opencode `<mcp_instructions>` prompt surface.
- I did not re-derive which record is right. [INFERENCE] The round-13 row may rest on opencode source or binary rather than the docs page. That belongs to the opencode sweep seat's lane, not to adjacency.

### F3 — a host-observed server `instructions` string exists in a sibling's receipts (data only). Severity: info

- kaidoku `.ufo/waves/luna-round-6/receipts/leg-2.md:9` (at `a2673116`) holds REA 6.5.0's live `initialize` result with an `instructions` value. Extracted with `git show … | grep -o '"instructions":"[^"]*"'` and a JSON decode, it is **812 characters**. It opens: "REA provides reverse-engineering tools for local artifacts, native binaries, managed code, browser pages, and runtimes. Use the tool that directly answers the question; …".
- `.ufo/waves/luna-round-8/ZB3.md:17` holds a 304-character value labelled 6.4.0.
- These are wave receipts, which are not scope surfaces, and the string is untrusted target data.
- They bear on C2's limit "no client was run against a server that sends `instructions`" (entry `:59`). The server omp is configured with (`~/.omp/agent/mcp.json`, kaidoku `PROVINCE.md:16`) does send the field, and at 812 characters it exceeds Codex's 512-character self-contained budget (S035). Running a client remains unrun.

## 4. Proposed move (one, bounded): a revision note outside the counted table

**Move.** Add three things, in the round-52 fix commit:

1. One prose bullet to the entry's `## Limits` (or a new short `## Spec revision` section). Never a second row in `## Per-client record`.
2. One `corpus/SOURCES.md` row (next free id) for `https://modelcontextprotocol.io/specification/2026-07-28/schema.md`, § DiscoverResult `:1293, 1301-1304`, with `used-by` naming the entry and the fetch record (UTC, bytes, sha256 above) in `corpus/lessons/round-52.md` § Gate.
3. A rewording of `SKILL.md:87`: "server-wide text the server returns at `initialize` (revisions to 2025-11-25) or on `server/discover` (2026-07-28, current); optional, placement left to the client". The `SKILL.md:93` "why" cell gains the 2026-07-28 sentence "should not duplicate information already in tool descriptions".

The note cites kumitate `corpus/SOURCES.md:23` (S010) as the lane that tracks MCP revisions: report, do not absorb.

**Axes:**

- **freshness:** up. The Core premise matches the current revision.
- **coverage:** up. Craft rule 1 gains direct spec support.
- **adjacency:** up. Kotoba cites the sibling's ground rather than re-deriving it.
- **No harm to the counted claim, shown in the sandbox:**
  - Clone `/fast/scratch/hyaku/kotoba-r52a2/ConnSiblingOverlap/clone` at `c8407a4`, then `python3 -B verifiers/check_mcp_instructions.py --root <clone>` → `mcp instructions backed 5 of 7 clients`, exit 0.
  - **Mutant A** (the prose bullet above added under `## Limits`) → `backed 5 of 7`, exit 0.
  - **Mutant B** (the same fact added as a second `| MCP specification | S039 |` row in the table) → `MCP specification  no rows naming client: 2 (need 1)`, `backed 4 of 7`, exit 0. The table must stay one row per client (`check_mcp_instructions.py:195-197`).
  - The clone was restored with `git checkout -- <entry>`; `git status --short | wc -l` → 0.

**Risks:**

1. Adding a table row, or swapping S032 for the new row, changes the counted data after the plan. Mutant B shows the count falls 5 → 4, so the move is prose only.
2. Another seat may judge rewording `SKILL.md` mid-falsify as scope creep. Mitigation: the edit is one clause in the preamble and the table header is unchanged.
3. Not run by me: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` with the new row, and `verifiers/verify_skill_checklist.py` and `verifiers/check_correction_sweep.py` on the edited `SKILL.md`. None of these has passed for this move until they are run.
4. The 2026-07-28 page is spec text, tier A. The spec site serves both revisions, so the S032 `--fetch` arm is unaffected; its bytes were identical at 17:51:52Z.

**Checks for the L1 after landing:**

- `python3 -B verifiers/check_mcp_instructions.py --rev <fix-rev>` → `5 of 7`, and the same with `--fetch`.
- `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` → unchanged.
- `scripts/sources-census.sh validate …` → exit 0.
- `git grep -n 'returns at `initialize`\|returns in its `initialize`' <fix-rev> -- SKILL.md corpus/knowledge/mcp-server-instructions-round52.md` → only qualified occurrences.

## 5. Contradictions stated, not scored

- The census rule classifies whole lanes; this attack classified one element. Every hit is `none` for that element. The lane rows (kumitate, kake and kama `adjacent`) rest on other elements and do not move.
- kumitate holds the MCP revision as `queued`, a SOURCES row and not admitted knowledge. Kotoba citing it as "kumitate's ground" should say "registered, not mined".
- game-dev-3d's vendored `create-toolset` text is tool-description craft, but in files no fleet lane owns. Under the round-50 precedence it is `none`. If game-dev-3d ever adopts it as its own rule, the classification needs a re-read.

## 6. Commands run (all read-only in the lane and in siblings; the sandbox was used only for the mutants)

- The per-lane `git -C <lane> grep -ciE <pattern 1> <tip> -- PROVINCE.md SKILL.md corpus/README.md 'corpus/knowledge/*'` loop → exit 0 (hit counts in section 1).
- `git -C <lane> grep -nIiE <pattern 2> …` over the 9 hit lanes → exit 0; only the revenger EVM lines.
- The tree-wide `git grep` for `InitializeResult|server[- ]instructions|…` → exit 0; kaidoku receipts, plus unrelated kama and souji JSON `"instructions"` keys.
- The frontmatter description loop → exit 0; 0 of 17.
- The kotoba+MCP co-occurrence loop → exit 0; 0 lines.
- `curl -sSL` × 4 → HTTP 200 each (table in F1).
- `git grep -nE '2026-07-28|server/discover|DiscoverResult|stateless' c8407a4` in the kotoba lane → exit 0; only `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` unrelated strings.
- Sandbox counter runs: baseline, mutant A and mutant B, with outputs as quoted in section 4.

Hygiene: one stray copy of mutant A was written to `/tmp/connsib-A.md` (outside the scratch bound) and removed at once; `ls` confirmed it was gone. No lane file other than this report was written.
