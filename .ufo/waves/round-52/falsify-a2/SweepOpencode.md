Result: MIXED — the two page counts the entry records reproduce byte-exact (`instructions` 0 times on `opencode.ai/docs/mcp-servers.md` and on its `packages/web` source), but opencode's live official v2 docs page, its docs source tree, its source code and its v2.1.3 changelog all handle MCP server `instructions`, so the entry's bounded negative is incomplete and the frozen counter backs 6 of 7 clients with admitted evidence, not 5.

Seat: KotobaR52a2.SweepOpencode. Target: the entry's opencode negative,
`corpus/knowledge/mcp-server-instructions-round52.md:29-37` ("Not counted, with the sweep (Q14): **opencode** …"),
its consequence `:48` ("two of the seven clients checked here document nothing about it") and the derived
`SKILL.md:94` row. Judged revision `c8407a453788df964df5a7b835dd0ce1360de882`. Read-only in the lane; all
writing work in `/fast/scratch/hyaku/kotoba-r52a2/SweepOpencode/`.

## Attack A — the page-level counts as written (HOLDS)

Both counts reproduce, and the recorded digest matches, so nothing in the literal sentence is false.

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-22T17:50:15Z
$ curl -sS -o opencode-mcp-servers.md -w 'http=%{http_code} bytes=%{size_download}\n' https://opencode.ai/docs/mcp-servers.md
http=200 bytes=13941
$ sha256sum opencode-mcp-servers.md
12ed2af6c5f48701160ab6e1abe79fedbe293e55c5889c447be57ff79cd14de0
$ grep -c -i instructions opencode-mcp-servers.md ; echo exit=$?
0
exit=1
```

The entry records 13,941 B and sha256 `12ed2af6c5f4…` (`round52.md:29-30`); both match. The docs source on the
old `sst` raw path and on the current `anomalyco` raw path are byte-identical, 14,015 B, sha256
`ad6e6687ab4c8b535471ff176957fc7623b5f06230efc848b854c5c96acd70f5`, `grep -c -i instructions` → 0 on both
(fetched 17:50:43Z). The deployed HTML page also has 0 occurrences
(https://opencode.ai/docs/mcp-servers/, 17:52:28Z, 127,218 B, sha256 `f46a70ba8e11b79bba067de8bb23e8d26535a269c496f15a143198a7b274a5e5`).

So the sweep's page selection is honest. What it is not is complete.

## Attack B — opencode's live official docs document it (BREAKS, major)

`opencode.ai/v2/docs/mcp-servers/` (same official host, the v2 docs tree) has a dedicated section:

```
$ curl -sS -o opencode-v2-mcp-servers.html -w 'http=%{http_code} bytes=%{size_download}\n' https://opencode.ai/v2/docs/mcp-servers/
http=200 bytes=74655          # 2026-10-22T17:56:30Z
$ sha256sum opencode-v2-mcp-servers.html
6b21fef207156e5eddc160e5f2697f598e7f53cc83153d48fca8303f0efcef86
$ grep -o -i instructions opencode-v2-mcp-servers.html | wc -l
13
```

Fetched bytes, verbatim (HTML lines 517-521):

```
517: <h2 id="server-instructions">Server instructions</h2>
518: <p>When a server returns instructions during initialization, OpenCode adds them to the system prompt:</p>
519: <pre ... data-language="text"><code><span class="line"><span>&lt;mcp_instructions&gt;</span></span>
520: <span class="line"><span>  &lt;server name=&quot;sentry&quot;&gt;</span></span>
521: <span class="line"><span>    Search for an existing issue before creating a new one.</span></span>
```

Quote for the record (14 whitespace words, contains `instructions`):
"When a server returns instructions during initialization, OpenCode adds them to the system prompt:"

Source of that page, in the same repository (`docs` kind, pinned host `github.com/anomalyco/opencode` /
`raw.githubusercontent.com/anomalyco/opencode` in `verifiers/check_mcp_instructions.py:84-86`):

- `services/www/src/docs/content/mcp-servers.mdx:427-441` — full section, fetched 17:55Z, 15,476 B, sha256
  `fd3b05ead1ecfde68181f90507cbb616f5cd3d5fa360494b4e261e4b9f3627a2`. It states the placement
  (`:429`), shows the `<mcp_instructions>` shape (`:431-437`) and the omission rule (`:441`).
- `services/www/astro.config.ts:8,11` — `base = "/v2/"`, `site: … "https://opencode.ai"` in production:
  this tree is the deployed v2 docs, not a stray draft.
- The section is not new: the same file at the 2026-10-15 revision `d0732eadf8` is byte-identical
  (15,476 B, `## Server instructions` at `:427`). It predates the sweep by a week.
- `services/www/src/docs/content/instructions.mdx:70` — the initial-instruction order lists
  "3. MCP server, reference, and skill guidance" before AGENTS.md files.

Why the sweep missed it, structurally: the v2 tree is not enumerated by `https://opencode.ai/sitemap.xml`
(17:53:50Z, 94,104 B, sha256 `30a734434019c646588b5206a3433c8e776871e33ef240fae75796290ea0ef7c`; 706 locs,
561 under `/docs`, 0 under `/v2/`), and `https://opencode.ai/v2/docs/mcp-servers.md` returns 404 (9 B), so
the `.md` endpoint that produced the entry's page does not exist for this tree. A sweep that opened only
`/docs/…mcp-servers` therefore cannot see it. `dev.opencode.ai/v2/docs/mcp-servers/` serves the same page
(200, 74,655 B).

## Attack C — opencode's source implements it (BREAKS, major, independent ground)

Fetched 17:50:43Z from `raw.githubusercontent.com/anomalyco/opencode/dev/` (branch `dev`; repo default branch
is `dev`, pushed 2026-10-22T17:49:44Z):

- `packages/core/src/mcp/client.ts:117` — `readonly instructions: string | undefined` on the `Connection`
  handle; `:338` — `instructions: client.getInstructions()?.trim() || undefined,` (20,244 B, sha256
  `d90742250e6152fee90cafb9069290aeaef9f1ecf8211aa572cb6bd0d7a5f4e5`).
- `packages/core/src/mcp/index.ts:30-33` (`ServerInstructions`), `:126`
  `readonly instructions: () => Effect.Effect<ServerInstructions[]>`; implementation `:691-698` collects
  `entry.client?.instructions` per server (37,981 B, sha256
  `3bbdfe064ff9c32c6a2627c3597315b2d64919e41996885db4269ee88b7ea776`).
- `packages/core/src/mcp/instructions.ts` — renders the prompt block:
  `:19-29` builds `<server name="…">` entries and `<mcp_instructions>`;
  `:41` "The available MCP server instructions have changed. This list supersedes the previous one.";
  `:63` "Lists server instructions reachable under the given ruleset; callers pass the merged agent and
  Session permissions." (4,803 B, sha256 `13a166ca02c13aa6b14e6545676400efe542804ce76b81f26ec4d4e6788c7070`).
  `:87-111` gates visibility on the session reaching at least one tool of that server.
- `packages/core/src/session/context.ts:14,83,216` — the session context composes the
  `McpInstructions.Service` and its node, i.e. this text reaches the model request path (9,404 B).
- `packages/core/test/mcp-instructions.test.ts` — asserts the exact `<mcp_instructions>` block for
  permitted servers and an empty string when `execute` is denied (6,871 B, sha256
  `cca8c4e4b5115bf483429dcef1c78cedcf11485b371b88326b986132883919e5`). File history: 10 commits, oldest
  2026-07-16T14:40:38Z.
- SDK provenance, `@modelcontextprotocol/client@2.0.0` (tarball sha256
  `cb470b0249b4a06e262145ab2281ea25344e77608f312a5a52ab4dcc26bfa732`): `dist/index.mjs:3245`
  `this._instructions = result.instructions;` inside the initialize path (the next line sends
  `notifications/initialized`), and `dist/index.d.mts:2109-2111`:
  "After initialization has completed, this may be populated with information about the server's
  instructions." So the field opencode reads is the `initialize` result's `instructions`, exactly the
  surface the entry tracks.
- Public release note, `CHANGELOG.md:59` under `## v2.1.3 — 2026-10-22` (`:5`, 50,001 B, sha256
  `7c4cb74025c345d5a5df08195da5005674478055c6c804f25221f3bb931c519b`):
  "Updates to MCP instructions, skills, and project references now send only changed entries instead of
  repeating the full list."

Module history for `packages/core/src/mcp/instructions.ts` runs from 2026-07-16 (`a5b28c2af2`) through
2026-10-21 (`15adc3d91e`, 11 commits), so this is not a feature that landed after the sweep.

## Attack D — the frozen counter admits the evidence the sweep left out (BREAKS the "not counted" disposition)

Lane, judged revision: `5 of 7`, exit 0 (opencode: "no rows naming client: 0 (need 1)").

Sandbox clone of the lane at `c8407a4`, one opencode row added citing the live v2 page, one `S099`
`corpus/SOURCES.md` row (`docs`, tier `A`, `mined`, opened `2026-10-22`, url on `opencode.ai`) and one
`corpus/lessons/round-52.md` Gate bullet carrying the quote verbatim:

```
$ python3 -B …/verifiers/check_mcp_instructions.py --root .
…
opencode           BACKED
mcp instructions backed 6 of 7 clients
exit=0
$ python3 -B …/verifiers/check_mcp_instructions.py --root . --fetch
opencode           BACKED found=True
mcp instructions backed 6 of 7 clients
mcp instructions found on the live page 6 of 6
exit=0
```

The demo row is a probe, not a proposed final wording; the point is that the counter as frozen — including
its opencode host pins — accepts this evidence and prints one client more than the entry does. The C2
statement ("at least 3 of 7") is therefore not falsified; it is under-filled by exactly the client the
entry set aside. The sandbox tree lives at `/fast/scratch/hyaku/kotoba-r52a2/SweepOpencode/lane`; no lane
file was written.

## Attack E — the negative's craft consequences (BREAKS, minor)

- `corpus/knowledge/mcp-server-instructions-round52.md:48`: "two of the seven clients checked here document
  nothing about it." False for opencode as of today: the vendor's live v2 docs page and its docs source
  document the placement, the block shape and the permission rule.
- `SKILL.md:94`: "the opencode and Copilot CLI pages opened on 2026-10-22 say nothing about server
  instructions (entry § sweep)". Literally true of the pages named, so the row is not a false statement;
  but its evidence base is now known to be one docs tree short, and its guidance ("needed on every client →
  a skill or always-on file too") treats opencode like a client with no known surface. opencode in fact puts
  the text in the system prompt, which is a stronger placement than three of the five backed clients
  document.

## Attack F — stale host in the citation (note, minor)

`github.com/sst/opencode` now answers 301 to repository id 975734319, which is
`anomalyco/opencode` (`full_name` anomalyco/opencode, homepage https://opencode.ai, default branch `dev`,
pushed 2026-10-22T17:49:44Z, not archived). The entry cites the old `raw.githubusercontent.com/sst/opencode/dev/…`
path (`:31`); it still serves the identical 14,015 B file, and the frozen counter pins both hosts
(`:84-86`), so nothing in the count moves. The repair should cite the current canonical host and note the
alias.

## Severity

| finding | verdict | severity | why |
|---|---|---|---|
| A page counts | HOLDS | — | reproduced byte-exact, digest matches |
| B live v2 docs page + docs source | BREAKS | major | official docs on the same host document the surface and its block shape; the sweep opened one docs tree of two |
| C source implementation | BREAKS | major | `getInstructions()` → `MCP.instructions()` → `<mcp_instructions>` → session context; tests and v2.1.3 changelog |
| D counter under-count | BREAKS | major | 6 of 7 reproducible with a single admitted row; printed claim remains true (under-filled) |
| E entry:48 / SKILL.md:94 | BREAKS | minor | page-scoped wording survives; the derived guidance and "document nothing" do not |
| F sst → anomalyco | note | minor | identical bytes; canonical host changed |

No printed number in the entry is false. The defect is that the negative was written as a sweep finding
when the client's live docs and source both answer the question, and the frozen counter was built to accept
exactly that answer.

## Sweep record

Queries and pages opened for this seat (all times UTC, 2026-10-22):

| # | what | url | http | bytes | sha256 (full) | `instructions` hits |
|---|---|---|---|---|---|---|
| 1 | v1 docs page, markdown | https://opencode.ai/docs/mcp-servers.md | 200 | 13,941 | `12ed2af6c5f48701160ab6e1abe79fedbe293e55c5889c447be57ff79cd14de0` | 0 |
| 2 | v1 docs page, deployed HTML | https://opencode.ai/docs/mcp-servers/ | 200 | 127,218 | `f46a70ba8e11b79bba067de8bb23e8d26535a269c496f15a143198a7b274a5e5` | 0 |
| 3 | v1 docs source (old host) | raw…/sst/opencode/dev/packages/web/src/content/docs/mcp-servers.mdx | 200 | 14,015 | `ad6e6687ab4c8b535471ff176957fc7623b5f06230efc848b854c5c96acd70f5` | 0 |
| 4 | v1 docs source (current host) | raw…/anomalyco/opencode/dev/packages/web/src/content/docs/mcp-servers.mdx | 200 | 14,015 | same | 0 |
| 5 | **v2 docs page (live)** | https://opencode.ai/v2/docs/mcp-servers/ | 200 | 74,655 | `6b21fef207156e5eddc160e5f2697f598e7f53cc83153d48fca8303f0efcef86` | 13 |
| 6 | **v2 docs source** | raw…/anomalyco/opencode/dev/services/www/src/docs/content/mcp-servers.mdx | 200 | 15,476 | `fd3b05ead1ecfde68181f90507cbb616f5cd3d5fa360494b4e261e4b9f3627a2` | 6 (section at `:427`) |
| 7 | sitemap | https://opencode.ai/sitemap.xml | 200 | 94,104 | `30a734434019c646588b5206a3433c8e776871e33ef240fae75796290ea0ef7c` | 706 locs, 0 `/v2/` |
| 8 | v2 `.md` variant (absent) | https://opencode.ai/v2/docs/mcp-servers.md | 404 | 9 | — | — |
| 9 | v2 docs on dev host | https://dev.opencode.ai/v2/docs/mcp-servers/ | 200 | 74,655 | not hashed; same byte count as #5 | 2 "Server instructions" |

Other searches:

- English docs sources: 33 pages under `packages/web/src/content/docs/` fetched and grepped; 8 contain
  `instructions` (`agents`, `config`, `ecosystem`, `github`, `gitlab`, `rules`, `skills`, `tools`), every hit
  read, all are the file-based `instructions` config or unrelated prose — none is the MCP initialize field.
  126 docs files were fetched in total (33 English + 93 localized); no page contains `server instructions`,
  `mcp_instructions` or `getInstructions`.
- Repository tree (`GET /repos/anomalyco/opencode/git/trees/dev?recursive=1`): 9,512 entries, 8,575 blobs,
  63 paths matching `mcp`; read in full the four core MCP files named above, the test, the session context
  and the v2 docs page.
- `gh search code` (authenticated, gh 2.102.0) in `anomalyco/opencode` for `McpInstructions`,
  `mcp_instructions`, `getInstructions`: hits only in the files above plus four test files that mock the
  service.
- The sources never contained the word in the two pages the entry opened; they do contain it elsewhere on
  the same host. Query list: "opencode MCP server instructions", `site:opencode.ai` MCP instructions (no
  opencode.ai result, relaxed), direct URL probes `/docs` vs `/v2/docs`, `.md` endpoint probes, sitemap
  enumeration.

## Not checked / open

- No opencode build was run against a server that sends `instructions`; every statement here is
  documentation or source reading, same as the entry's own limit.
- I did not clone or grep the whole repository. The tree listing, the authenticated code search over three
  terms, and the targeted raw fetches bound what I saw; a surface that never uses those tokens would be
  missed.
- I cannot prove the v2 docs page's exact state at 17:04Z (the entry's open time). The section is present in
  the 2026-10-15 revision of the file (byte-identical to today's) and the page is served live now; the repo
  has been pushed continuously.
- Localized docs (527 pages) were not read individually beyond the 93 fetched copies; the English source is
  the origin of those translations.
- The Copilot CLI half of the sweep is outside this ticket and was not attacked.

## Tooling

Nothing installed or upgraded. Used preinstalled `gh 2.102.0` (authenticated) for GitHub code search,
`curl 8.23.0`, `python3 3.14.8`. Pacman untouched (host transactions paused).

Lane working-tree note at report time: `git status --porcelain` shows ` M SCORECARD.md` (the attempt-1 carry
named in the wave brief) and ` M corpus/SOURCES.md` whose only hunk is an `S039` opencode-skills row; neither
is mine — this seat wrote only this report file. All probe writes were under
`/fast/scratch/hyaku/kotoba-r52a2/SweepOpencode/`.
