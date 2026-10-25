# Round 52 — lesson (kotoba, hyaku campaign, attempts 1 and 2)

Round: 52 (steered; fleet `/home/vgpnk/Projects/shokunin/.ufo/watchdog.log` lines `launch kotoba round=52 … attempt=1`,
2026-10-22T12:48:39-03:00, and `lane-dead-no-report kotoba round=52` then `launch … attempt=2`, 14:30:02-03:00).
Plan: `plans/round-52.md` at `4c003a4b` (counters frozen there). LOG.md § Round 52 (attempt-2 landing).

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| M36 | `reference-drift` | Round 51's corrections sweep missed places that still stated the superseded C2 result without the declared one: `corpus/README.md:133-141` (pre-falsify lever set; unqualified `overlap levers backed 7 of 7 clients`) and the `SCORECARD.md:28` depth lead (`7 of 7`, exit 0 @ `34cfffbb`; "six rows are new"), found by the closure (`corpus/lessons/round-51-verifier-spotcheck.md:158-167`, routed defects 1-2); and a third, `PROVINCE.md:17` (`verifiers/check_overlap_levers.py` prints `overlap levers backed 7 of 7 clients`), which the closure did not route and this round's sweep found. | PROTOCOL § Evidence standard, "Corrections sweep every mention" — the rule existed, but the sweep was a manual grep with no committed list of what was superseded, so nothing failed when a place was missed. | `verifiers/check_correction_sweep.py` with a registry of superseded claims: each block holding a stale claim must also hold the declared result (and lead with it in a SCORECARD cell). Shown able to fail: `--rev c8579a4c` → exit 1, `FAIL r51-c2-readme corpus/README.md:119`, `FAIL r51-c2-scorecard-lead SCORECARD.md:28`, `FAIL r51-c2-province PROVINCE.md:17`; after the repairs in this round → exit 0; `--self-test` 0 failures over 5 assertions (red, green, wrong-block, declared-after-lead and clean arms). New criterion Q29. |
| M37 | `provider` | The build wave (34 seats, validated `.ufo/waves/round-52/build-dispatch.json`) waited on the seat gate from about 16:05Z: the first `wave-slot.sh acquire kotoba build 34` call timed out after 3,600 s with no grant (`live_estimate` 52 then 84 against cap 85); a second acquire was still waiting at 17:10Z. Main also reported at 17:02Z that the route serving executor, scribe and mutation-tester seats was fully down. | none | The L1 did the build work itself (C1 code, C2 sources and entry, repairs) so the claims could land; the wave and its falsify seats are reported as not run, not replaced. Not a criterion: a capacity event, not a judgment error. |
| M38 | `false-negative` | The C2 sweep recorded opencode and Copilot CLI as silent on server instructions (attempt-1 entry § sweep, this lesson § Rejected). opencode's current docs source `services/www/src/docs/content/mcp-servers.mdx:429` and Copilot CLI's changelog `:1157`, `:2895` both document it; the sweep opened a superseded docs path and a how-to page, never the vendor changelog or the current docs tree. The lane's own round-13 census (`instruction-surface-census-round13.md:283`) already listed opencode's `<mcp_instructions>`. Found by attempt-2 seats `CriticLearning` and `SweepOpencode`. | Q14 (a negative carries its sweep) — the sweep was recorded, so Q14 passed; it does not ask whether the sweep covered the places a vendor states support | Rows S041 and S042, entry and `SKILL.md` corrected; criterion Q30. Shown able to fail: at `c8407a45` the entry's sweep names neither a changelog nor the lane's own prior records, so Q30 rejects it. |
| M39 | `overclaim` | The C2 entry § Limits (`c8407a45`, lines 61-63) and the uncommitted SCORECARD coverage cell said the frozen counter checks that each quote "is located" and "in the round's Gate"; the counter never reads the `location` cell and accepts the quote anywhere in the lesson (seat `CriticCalibration`: five location cells set to `nowhere` still print `backed 5 of 7`). The instrument was described wider than its code. | Q26 (the statement claims only what the counter prints) — applied to the claim statement, not to prose describing the counter | Entry § Limits rewritten to list exactly the cells and checks the counter reads; SCORECARD cell corrected before commit. |
| M40 | `unsupported-claim` | The attempt-1 L1's uncommitted SCORECARD block said "the falsify wave ran on live roles only" and titled the round "completed"; the attempt-1 falsify directory holds only a 36-seat registry and no seat report (seats `CriticCalibration`, `CriticLearning`, `CriticFrozenTables`). It also recorded "live gate `pass 7`", which held at 17:45Z (attempt-2 L1 run, `pass 7`, exit 0) but not after the host's opencode moved to 1.19.4 at 17:50:30Z. | PROTOCOL § Evidence standard (an unrun check has not passed) | The block was rewritten by the attempt-2 L1 before commit; the host-drift result is stated with its time. |

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

### Admitted in attempt 2 (after the falsify wave; L1 re-fetched every page and copied each quote from the bytes)

- **S039** (supersedes S024; carried item 4 of the round-51 spot-check; drafted by seat `ScribeS024`) —
  https://opencode.ai/docs/skills.md, opened 2026-10-22T17:50:09Z by the seat and re-opened by the L1 at 17:55:41Z,
  5,365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` (both opens). Quote (`skills.md:230`):
  "Check permissions—skills with `deny` are hidden from agents".
- **S040** — https://modelcontextprotocol.io/specification/2026-07-28/schema.md, opened 2026-10-22T17:56:44Z, 214,138 B,
  sha256 `6daa817b8e9fec97ff86197dca32dbca8fdf4ec13df01aa9d1251630e2360c11`. Quote (`schema.md:1304`, § DiscoverResult,
  field `instructions`): "should not duplicate information already in tool descriptions". With it:
  https://modelcontextprotocol.io/specification/2026-07-28/changelog.md (17:56:45Z, 11,855 B, `b4c48776…`), item 2 at `:14`:
  "remove the `initialize`/`notifications/initialized` handshake"; versioning page (3,219 B, `06e45272…`) `:25` names
  2026-07-28 the current version. Found by seat `ConnSiblingOverlap` (kumitate holds the revision as its row S010, `queued`).
- **S041** — https://raw.githubusercontent.com/anomalyco/opencode/cdf1c200a671378458b50f9e3167405f1f326b24/services/www/src/docs/content/mcp-servers.mdx,
  opened 2026-10-22T17:57:36Z, 15,476 B, sha256 `fd3b05ead1ecfde68181f90507cbb616f5cd3d5fa360494b4e261e4b9f3627a2`. Quote
  (`mcp-servers.mdx:429`, § Server instructions): "When a server returns instructions during initialization, OpenCode adds them to the system prompt:"
  Found by seats `CriticLearning` and `SweepOpencode` (the same text is live at https://opencode.ai/v2/docs/mcp-servers/).
- **S042** — https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md,
  opened 2026-10-22T17:57:36Z, 289,859 B, sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`. Quote
  (`changelog.md:1157`, § 1.0.66 - 2026-06-30): "Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts"
  and (`:2895`, § 0.0.400 - 2026-01-30) "Add MCP server instructions support". Found by seat `CriticLearning`.

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
**Correction (attempt 2):** both rejections were false negatives. The opencode docs path opened above had been superseded by
`services/www/src/docs/content/mcp-servers.mdx`, which documents server instructions (S041), and Copilot CLI states its
support in its changelog (S042), a page the sweep never opened (M38). The two pages above still say nothing, as recorded.

### Rows touched (old → new)

None of S001–S031 changed in place. S031's `teaches` is superseded by the new row S038, and S024's by the new row S039
(append-only, contract rule 2): S024 `status` mined → mined, `recheck` 90d → 90d, `used-by` unchanged. S039's anchor records
that S024's HTML-route hash `4d96fa56…` is stale. Round 51's reason for not writing S024's superseding row ("would add a W04
duplicate-URL warning", `corpus/lessons/round-51.md:65-66`) was wrong as stated: W04 compares scopes, and with S024's scope
kept byte-identical the census adds no warning (seat `ScribeS024`, measured; census exit 0 after S039 landed).

### Spot-check

Owed to the non-author closure (at least one admit and one reject).

## Routed defects from the round-51 spot-check

1. `corpus/README.md:133-141` — correction appended inside the same bullet (`:158-167`; attempt 1 wrote `:144-153`, corrected
   by seat `ReviewSpotcheckRouting`), and the index row (`:75`) carries a
   correction naming `removed in a scope`. Fixed. The sweep (M36) catches the Core note, not the index row: the base index row
   states the old claim in other words ("seven client pages", "removed everywhere") and matches no registry phrase (attempt-2
   seat `MutSweepCheck`, revert M2 survived). The sweep's scope is its registry rows, phrase-bound per file; it does not find a
   reworded or new stale claim, and nothing runs it automatically (seats `MutSweepCheck`, `CriticQ29`).
2. `SCORECARD.md:28` — the depth lead now opens with the declared result (`4 of 7` on the plan-commit counter `7c81a787`); the
   widened `7 of 7` is labelled a second measurement; "six rows are new" corrected to four. Fixed.
3. Round-51 C2 not re-declared this round (plan § Claims); the round-52 claims work other surfaces.
4. Carried items: S031 superseded by S038 (fixed, attempt 1). In attempt 2: S024 superseded by S039 (fixed; drafted by seat
   `ScribeS024`, quote re-checked by the L1); fixture lines 9, 15 and 33 of `verifiers/fixtures/surfaces/strings-omp-18.12.6.txt`
   labelled as not-dump bytes (fixed; seat `ExecFixtureLabels` diff applied byte-identical to its sandbox copy; they are now
   lines 11, 19 and 40, and the round-51 lesson's numbering is the old file's). D2 F1–F5, the D7 items, R1 and R5 stay carried:
   attempt 1 had no build seats (M37) and attempt 2 spent its one wave on falsifying the landed claims.

## Falsify-wave corrections (attempt 2)

One validated 34-seat v1 wave (`.ufo/waves/round-52/falsify-a2-spec.json`), judged at `c8407a45`. Every finding below that
changed landed text, by seat (reports under `.ufo/waves/round-52/falsify-a2/`):

- `CriticLearning`, `SweepOpencode`, `SweepCopilotCli` (BREAKS): the C2 negatives for opencode and Copilot CLI were false (M38).
  Rows S041, S042; entry table, sweep record, craft items 1, 3 and 5, `SKILL.md` table, `PROVINCE.md:19`, `corpus/README.md:78`
  corrected; `check_correction_sweep.py` rows `r52-c2-*` registered (red at `c8407a45`, green after; self-test 5 → 7).
- `CriticC2Sizing`, `ReopenS032`, `ReopenS034`, `CriticFrozenTables` (BREAKS, low-medium): the entry and SCORECARD described the
  counter as checking location and Gate placement (M39, Q31); "five clients" counted the spec as a client. Corrected.
  `CriticC2Sizing` also notes the C2 target is a floor ("at least 3"), not one value; the declared value stays `5 of 7` @ `c8407a45`.
- `ConnSiblingOverlap` (F1): the current MCP revision 2026-07-28 removes `initialize` and puts `instructions` on
  `server/discover`; row S040, entry Limits and `SKILL.md:87` corrected. No sibling ground absorbed (0 adjacent, 0 contested).
- `ReopenS033`: the page drifted (quote `:1468` → `:1488`), the heading is "Scale with MCP tool search", "always in context" and
  "both are always-loaded text" were the lane's inference. Corrected. `ReopenS035` (308 alias), `ReopenS036` (Antigravity banner),
  `ReopenS037` (tier B arguable) recorded in the entry Limits or here; S037's tier is left as written (no count depends on it).
- `CriticC1Escape` P4 (medium): a callee whose groups stay unresolved was never admitted, so its calls vanished. Fix in
  `extract_classes`: also admit a callee when an unresolved call's file is a declared file. `ReviewC1Diff` (medium): an empty omp
  baseline passed `surfaces.no_uncovered_class` on 0 == 0; fix: an empty declared set falls back to the callee allowlist (repro now
  `FAIL … 8 loader class(es) undeclared`, exit 1). Self-test stays 0 failures over 129 (no arm added for either fix: carried).
- Not fixed, recorded as limits: member-call loaders (`CriticC1Escape` P2, `MutCalleeCounter` M4 survives the counter), admission
  keyed on the group only survives every gate (`MutCalleeCounter` M5), decoy stand-in for a vanished loader (P1b), the C2 counter's
  loose host-path pins and substring Gate rule (`MutMcpCounter` M12, M16).
- `ScoutLiveShape`, `CriticCalibration`, `ReviewScorecardLeftover`: the attempt-1 SCORECARD leftover's "falsify wave ran" and
  "completed" were unsupported, and "live gate pass 7" no longer reproduced after opencode 1.19.4 replaced 1.19.3 on the host at
  17:50:30Z (M40). The leftover was rewritten before commit.
- `ReviewSpotcheckRouting`, `ReviewLesson`, `ReviewCorrections`, `ReviewMoreStale`: pointer `:144-153` → `:158-167`; LOG.md had
  no round-52 entry; `PROVINCE.md:26` restated `7 of 7` without the declared result. Corrected.
- `CriticQ29`, `MutSweepCheck`: Q29's "must exit 0 before the report" has no runner; the attempt-2 L1 ran it before the report
  (LOG.md). The registry is phrase-bound (above, item 1).
