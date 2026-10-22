# Round 52 — lesson (kotoba, hyaku campaign, attempt 1)

Round: 52 (steered; `.ufo/watchdog.log` line `launch kotoba round=52 … attempt=1`, 2026-10-22T12:48:39-03:00).
Plan: `plans/round-52.md` at `4c003a4b` (counters frozen there). LOG.md § Round 52.

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M36 | `reference-drift` | Round 51's corrections sweep missed places that still stated the superseded C2 result without the declared one: `corpus/README.md:133-141` (pre-falsify lever set; unqualified `overlap levers backed 7 of 7 clients`) and the `SCORECARD.md:28` depth lead (`7 of 7`, exit 0 @ `34cfffbb`; "six rows are new"), found by the closure (`corpus/lessons/round-51-verifier-spotcheck.md:158-167`, routed defects 1-2); and a third, `PROVINCE.md:17` (`verifiers/check_overlap_levers.py` prints `overlap levers backed 7 of 7 clients`), which the closure did not route and this round's sweep found. | PROTOCOL § Evidence standard, "Corrections sweep every mention" — the rule existed, but the sweep was a manual grep with no committed list of what was superseded, so nothing failed when a place was missed. | `verifiers/check_correction_sweep.py` with a registry of superseded claims: each block holding a stale claim must also hold the declared result (and lead with it in a SCORECARD cell). Shown able to fail: `--rev c8579a4c` → exit 1, `FAIL r51-c2-readme corpus/README.md:119`, `FAIL r51-c2-scorecard-lead SCORECARD.md:28`, `FAIL r51-c2-province PROVINCE.md:17`; after the repairs in this round → exit 0; `--self-test` 0 failures over 5 assertions (red, green, wrong-block, declared-after-lead and clean arms). New criterion Q29. |
| M37 | `provider` | The build wave (34 seats, validated `.ufo/waves/round-52/build-dispatch.json`) waited on the seat gate from about 16:05Z: the first `wave-slot.sh acquire kotoba build 34` call timed out after 3,600 s with no grant (`live_estimate` 52 then 84 against cap 85); a second acquire was still waiting at 17:10Z. Main also reported at 17:02Z that the route serving executor, scribe and mutation-tester seats was fully down. | none | The L1 did the build work itself (C1 code, C2 sources and entry, repairs) so the claims could land; the wave and its falsify seats are reported as not run, not replaced. Not a criterion: a capacity event, not a judgment error. |

## Gate

### Admitted (rows opened this round; every quote copied from the fetched bytes)

- **S032** — https://modelcontextprotocol.io/specification/2025-11-25/schema.md, opened 2026-10-22T17:04:55Z,
  130,800 B, sha256 `5ab7cfcd5ea05c7491637e76122362cc4416201ea0c81482f6747f59343f1691`. Quote (`schema.md:463`):
  "Instructions describing how to use the server and its features."
- **S033** — https://code.claude.com/docs/en/mcp.md, opened 2026-10-22T17:04:56Z, 127,022 B, sha256
  `9a42e98f81001adbefcf19d03fc40d591ffe55ba7c83b5a764ea725b403af766`. Quote (`mcp.md:1468`):
  "Only tool names and server instructions load at session start, so adding more MCP servers has minimal impact on your context window."
- **S034** — https://code.visualstudio.com/updates/v1_104, opened 2026-10-22T17:05:11Z, 179,440 B, sha256
  `19d9259e93ab3109cb243f33631494c9d2cc49546a5e90f5df6ea2765bd6e859`. Quote (HTML line 1114, § Support for server
  instructions): "VS Code now reads MCP server instructions and will include them in its base prompt."
- **S035** — https://developers.openai.com/codex/mcp.md, opened 2026-10-22T17:04:58Z, 26,995 B, sha256
  `c78df8c70b7f31f73557f77ad4208ff97656808fb423e6f4eb81151f8b009284`. Quote (`mcp.md:197`):
  "Codex reads the MCP `instructions` field returned during initialization and uses it as server-wide guidance alongside the server's tools."
- **S036** — https://geminicli.com/docs/tools/mcp-server.md, opened 2026-10-22T17:04:58Z, 43,656 B, sha256
  `4aefc4dc30c329cbbd16ca24fe294fb0d91ec87e8f61baca7116c19b6a1a14fd`. Quote (`mcp-server.md:1315`, § Instructions):
  "which will be appended to the system instructions."
- **S037** (tier B: maintainers' blog, explanatory) — https://blog.modelcontextprotocol.io/posts/2025-11-03-using-server-instructions/,
  opened 2026-10-22T17:04:57Z, 49,781 B, sha256 `96794ff9735768eacfe54e3cf6d2de5493f5fab4b2deed54feae99aaaa72e050`. Quote
  (§ A Note for Client Implementers): "we recommend that you expose instructions to users and provide transparency about what servers are injecting into context"
- **S038** (supersedes S031; carried item 4 of the round-51 spot-check) —
  https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md, re-opened
  2026-10-22T17:07:03Z, 461,944 B, sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` (byte-identical
  to the round-51 fetch). Quote (`:1300`): "Use the `ignoredSkillsLocations` setting to exclude specific directories (and their
  descendants) from discovery". Sweep: `grep -c disabledSkills` → 0; `ignoredSkillsLocations` 1; `disable-model-invocation` 2;
  `copilot skill disable` 1.

Fetch log: the fetched copies under `/fast/scratch/hyaku/kotoba-r52/src/` are scratch, not evidence; the values above are
the record.

### Rejected (opened, not admitted as a client row)

- **opencode** — https://opencode.ai/docs/mcp-servers.md (17:05:56Z, 13,941 B, sha256 prefix `12ed2af6c5f4`) and
  https://raw.githubusercontent.com/sst/opencode/dev/packages/web/src/content/docs/mcp-servers.mdx (17:05:56Z, 14,015 B,
  `ad6e6687ab4c`): `grep -ci instructions` → 0 on both. Reason: the pages say nothing about server instructions. Flip: a
  docs statement, or a read of opencode's MCP client source showing where the text goes.
- **Copilot CLI** — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md (17:05:54Z,
  14,240 B, `640035aa0936`): one `instructions` hit (line 22, installation instructions in the GitHub MCP Registry), none about
  server instructions; https://docs.github.com/en/copilot/concepts/context/mcp.md returned a 404 page (502 B). Reason and flip as
  for opencode.
- **VS Code `.md` variant** — https://code.visualstudio.com/updates/v1_104.md returned a "Page not found" HTML page (19,510 B);
  the HTML page was used instead (S034).

No row was written for either rejection: no `S###` id is spent on a page that teaches nothing for this scope.

### Rows touched (old → new)

None of S001–S031 changed in place. S031's `teaches` is superseded by the new row S038 (append-only, contract rule 2).

### Spot-check

Owed to the non-author closure (at least one admit and one reject).

## Routed defects from the round-51 spot-check

1. `corpus/README.md:133-141` — correction appended inside the same bullet (`:144-153`), and the index row (`:75`) carries a
   correction naming `removed in a scope`. Fixed; caught by `check_correction_sweep.py` (M36).
2. `SCORECARD.md:28` — the depth lead now opens with the declared result (`4 of 7` on the plan-commit counter `7c81a787`); the
   widened `7 of 7` is labelled a second measurement; "six rows are new" corrected to four. Fixed.
3. Round-51 C2 not re-declared this round (plan § Claims); the round-52 claims work other surfaces.
4. Carried items: S031 superseded by S038 (fixed). S024 superseding row, fixture labels for lines 9, 15 and 33, D2 F1–F5, the D7
   items, R1 and R5 — carried, not worked: the build wave that held them never received a seat grant and the route for their
   executor and scribe seats was down (M37).
