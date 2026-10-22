Result: BREAKS — the entry's Copilot CLI negative is false: GitHub's own Copilot CLI command reference (`cli-command-reference.md:660`) and the official `github/copilot-cli` changelog (three entries) document what Copilot CLI does with MCP server `instructions`, and the frozen C2 counter admits a Copilot CLI row (scratch probe: `backed 6 of 7`, `found on the live page 6 of 6`, exit 0).

Seat: `KotobaR52a2.SweepCopilotCli`. Lane read at `c8407a453788df964df5a7b835dd0ce1360de882` (working tree; `SCORECARD.md` dirty, not touched). Sandbox: `/fast/scratch/hyaku/kotoba-r52a2/SweepCopilotCli/`. No tool was installed or updated; nothing was written outside this report and that sandbox.

## The target, verbatim

`corpus/knowledge/mcp-server-instructions-round52.md:29-37` (the Q14 sweep record):

```
32:**Copilot CLI** —
33:`https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md`
34:(14,240 B) contains `instructions` once, about installation instructions in the GitHub MCP
35:Registry, never about server instructions; `https://docs.github.com/en/copilot/concepts/context/mcp.md`
36:returned a 404 page. Both statements are bounded to the pages opened on 2026-10-22: the clients' source
37:code was not read, so "does not use server instructions" is not claimed.
```

and the client-level generalization at `:47-48`:

```
47:3. **Do not rely on it everywhere.** The specification makes the field optional and leaves placement
48:   to the client; two of the seven clients checked here document nothing about it.
```

The two per-page observations reproduce exactly (same byte counts and sha256 as the lesson Gate) — the fetch record is honest. What breaks is the sweep's scope and the conclusion drawn from it: the sweep never opened the CLI's own reference page, although the round already held it byte-for-byte (S031/S038, below).

## Statements found (primary sources, quoted verbatim)

### 1. docs.github.com — GitHub Copilot CLI command reference

`https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md`, § Command-line options (heading at `:650`), the option row at **`:660`** (table-column padding collapsed; cell text unaltered):

> `--allow-all-mcp-server-instructions` | Include initialization instructions from all MCP servers in the system prompt. By default, only allowlisted server instructions are included up front; other servers' instructions are retrieved on demand.

Two sentences, 11 and 17 whitespace-separated words, both containing `instructions`. The first sentence is exactly the shape the frozen counter admits: 3–25 words, contains the required word, and the page's host `docs.github.com` is pinned for Copilot CLI in `verifiers/check_mcp_instructions.py:87-88` (`"Copilot CLI": ("docs.github.com", "github.com/github/copilot-cli", "raw.githubusercontent.com/github/copilot-cli")`).

I checked the sentence is not an artefact of the `.md` route: the rendered HTML page `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference` (1,971,126 B, sha256 `cc871d0c…`) contains both sentences after the counter's own normalization (`<tags>` dropped, entities unescaped, whitespace collapsed); substring test printed `quote_found: True`, `q2_found: True`.

### 2. github.com/github/copilot-cli — changelog.md (clone HEAD `7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120`, last commit `2026-10-22T16:21:58Z`)

- `changelog.md:2893` heading `## 0.0.400 - 2026-01-30`; `:2895`:
  > - Add MCP server instructions support
- `changelog.md:1063` heading `## 1.0.66 - 2026-06-30`; `:1157`:
  > - Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts
- `changelog.md:195` heading `## 1.0.92 - 2026-10-05`; `:219`:
  > - MCP tools recover within the same turn when server instructions change

Release provenance: `https://api.github.com/repos/github/copilot-cli/releases/tags/v1.0.66-0` (200, 40,872 B, `published_at 2026-06-26T01:25:28Z`) carries the same line in its body:
> - Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts

### 3. github/copilot-cli issue #1579

`https://api.github.com/repos/github/copilot-cli/issues/1579` (200, 7,093 B), state `closed`, title:
> Copilot CLI ignores MCP server "instructions" (returned during MCP initialization)

Body (`### Describe the bug`): "MCP servers can (and often do) return instructions as part of their initialization lifecycle … Copilot CLI seems to ignore those instructions." Affected version `0.0.413-0`; 0 comments (`/comments` returned `[]`, 2 B). This is evidence the field is a tracked surface; it does not by itself establish present behaviour (the docs statement does). The version/dates sequence (support entry 0.0.400 on 2026-01-30, ignore report at 0.0.413-0, all-servers flag in 1.0.66 on 2026-06-30) is consistent with the flag being the fix, but the issue has no closing comment, so that remains [INFERENCE].

### 4. Pages checked that are silent on the field

- `add-mcp-servers.md:22` — the page's single `instructions` hit is "For installation instructions, available tools, and URLs for specific MCP servers, see the GitHub MCP Registry" (the entry's sentence is exact).
- `/en/copilot/concepts/context/mcp.md` — still HTTP 404, 502 B, byte-identical to the entry's record (sha256 `979615ba…`). The current concept page is `/en/copilot/concepts/customizations/mcp` (12,989 B); it has 2 `instructions` hits, both about prompts/custom guidance and setup instructions, none about the field.
- `use-copilot-cli/overview.md` (14 hits), `cli-config-dir-reference.md` (19), `cli-programmatic-reference.md` (1), `cli-plugin-reference.md` (1), `configure-copilot-cli.md` (0) — all hits are custom instruction files (`copilot-instructions.md`, `*.instructions.md`, `--no-custom-instructions`, `/instructions`), not server instructions.
- `acp-server.md` (0), enterprise `mcp-management.md` (0), `copilot-sdk/features/mcp.md` (0), reference landing page (0; it links exactly five subpages: acp-server, cli-command-reference, cli-config-dir-reference, cli-plugin-reference, cli-programmatic-reference).
- `github/copilot-cli` `README.md:19` names MCP extensibility but says nothing about `instructions` (1 hit, the `/login` sentence); `install.sh` has 0 MCP/instruction hits.

## Sweep record (queries, pages, counts)

Search queries issued (results used only as pointers; every quote above is from bytes I fetched):

1. `site:docs.github.com copilot-cli MCP server "instructions"`
2. `site:docs.github.com/en/copilot copilot-cli configuration command reference`
3. `"--allow-all-mcp-server-instructions"`
4. `site:docs.github.com/en/copilot "MCP" "Copilot CLI" server instructions allowlist`
5. `site:github.blog OR site:docs.github.com "server instructions" "Copilot CLI"`
6. docs search API: `/api/search/v1?query=allow-all-mcp-server-instructions&language=en&version=free-pro-team%40latest&size=20` (17:55:55Z, 200, 11,586 B, sha256 `7b2ea2e095d5dd51927e91aa65c1f19197db7f1c0cbe9a0ced3ccf08a23e36ab`) → 20 hits; this API is not phrase-exact: it returned `/en/copilot/concepts/customizations/mcp`, whose bytes contain the flag 0 times. So I opened every candidate CLI page by hand.
7. docs search API: same endpoint, `query=MCP+server+instructions` (17:55:56Z, 200, 11,817 B, sha256 `6291d05c8cef1abc86fd94337b7d6e470847e336e02f451eae08d5b0413140a1`) → 20 hits, general MCP pages; no new CLI page beyond the five above.

Fetches (ordinary curl, no browser; all 2026-10-22 UTC):

| # | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| 1 | `.../copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers.md` | 17:50:13Z | 200 | 14,240 | `640035aa0936ffb83ee8dd7034370019224c43cf03ee9560103a3a9cd190433b` |
| 2 | `.../copilot/concepts/context/mcp.md` | 17:50:13Z | 404 | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` |
| 3 | `.../copilot/reference/copilot-cli-reference/cli-command-reference.md` | 17:50:48Z | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| 4 | `.../copilot/how-tos/copilot-cli/use-copilot-cli/overview.md` | 17:50:48Z | 200 | 20,619 | `3d7922046390c5277e88a09c1f392f79e01f452bdf579193378472d466a9f7aa` |
| 5 | `.../copilot/reference/copilot-cli-reference/cli-config-dir-reference.md` | 17:50:48Z | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` |
| 6 | `.../copilot/reference/copilot-cli-reference/cli-programmatic-reference.md` | 17:50:49Z | 200 | 28,794 | `10f321e9f1b5aa2aa54f7e6de255287fe285be0f02195a508b3a63c50f82a0fa` |
| 7 | `.../copilot/reference/copilot-cli-reference/cli-plugin-reference.md` | 17:50:49Z | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |
| 8 | `.../copilot/reference/copilot-cli-reference.md` (landing) | 17:52:43Z | 200 | 1,021 | `d9c707cc59fe9a145646d0dbc8a63a5d9ecb9419f434781e3f0a45b433ff6b90` |
| 9 | `.../copilot/concepts/enterprise/mcp-management.md` | 17:52:43Z | 200 | 4,447 | `5bb274f487e39b496dfc28a98e7d0f29aed9aac998cc3ef7fbe08ce93ce5bd50` |
| 10 | `.../copilot/reference/copilot-cli-reference/acp-server.md` | 17:53:12Z | 200 | 14,117 | `e4bf270233e8ff33b37d64c93a5e594ae59ae9d2fc7e4bce0b620c613b45dcd3` |
| 11 | `.../copilot/reference/copilot-cli-reference/cli-command-reference` (HTML) | 17:53:12Z | 200 | 1,971,126 | `cc871d0c59c1b2ce337ca38d12851a0bf998afd5efb9324675f6d7caef7e4f0f` |
| 12 | `.../copilot/release-notes.md` | 17:53:53Z | 404 | 502 | `979615ba…` (same generic 404 page) |
| 13 | `.../copilot/changelog.md` | 17:53:53Z | 404 | 502 | `979615ba…` (same generic 404 page) |
| 14 | `.../copilot/concepts/customizations/mcp.md` | 17:56:06Z | 200 | 12,989 | `1fd3f72695b36fc1143e39fa280d31092e37f7ce1055551ee81607a8737702f8` |
| 15 | `.../copilot/how-tos/copilot-cli/set-up-copilot-cli/configure-copilot-cli.md` | 17:56:07Z | 200 | 12,460 | `7668cebe8597170449ae58f928f86378cabd9fbf1639a770b8512be435e0a177` |
| 16 | `.../copilot/how-tos/copilot-sdk/features/mcp.md` | 17:56:07Z | 200 | 33,713 | `ea9d5247ffcb236f9a96a22f052899afdbc1a93e3b53dd68d07f6b03040c3e8f` |
| 17 | `https://api.github.com/repos/github/copilot-cli/issues/1579` | 17:53:12Z | 200 | 7,093 | `3931077f1af1d948cdd04b1ef40413c1275c89007d1bd39ce7d91236ec85db41` |
| 18 | `.../issues/1579/comments` | 17:53:54Z | 200 | 2 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` (`[]`) |
| 19 | `.../releases/tags/v1.0.66-0` | 17:53:53Z | 200 | 40,872 | `b2638f1eea88ef5d50b97185f51490345629bb8684b8d14af020c8212a057844` |
| 20 | `git clone --depth 1 https://github.com/github/copilot-cli` (17:50:25Z) | HEAD `7ea98dfc…` |  | README 7,740; changelog 289,859; install.sh 7,018 | README `33657f2e…`; changelog `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`; install.sh `00efcc2e…` |

`instructions` counts: command reference 60 (1 about server instructions, `:660`; the rest custom instruction files/API paths); config-dir 19; overview 14; programmatic 1; plugin 1; add-mcp 1; concept `customizations/mcp` 2; configure-copilot-cli 0; SDK MCP 0; enterprise MCP management 0; acp-server 0; landing 0; repo README 1; repo changelog 52 of which 3 are the MCP-server-instructions lines above; install.sh 0.

## The entry's own already-fetched page refutes it

`corpus/SOURCES.md:44` (S031) records the command reference fetched at 14:19:21Z, 461,944 B, sha256 `c61997ef…`; `corpus/lessons/round-52.md:35-40` (S038) re-opened the same page at 17:07:03Z with the full sha256 `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` — identical to my 17:50:48Z fetch. So the bytes containing `:660` were in the round's hands almost three hours before the entry's 17:05:54Z Copilot sweep and were re-opened about a minute after it, for the skills row. The negative was refutable from the round's own scratch without any new fetch; the sweep simply never grepped that page for `instructions`.

## Frozen-counter admission probe (scratch copy only, lane untouched)

In `/fast/scratch/hyaku/kotoba-r52a2/SweepCopilotCli/probe` I copied the lane's entry, `corpus/SOURCES.md`, `corpus/lessons/round-52.md` and `verifiers/check_mcp_instructions.py`, then added:

- one entry row `| Copilot CLI | S039 | "Include initialization instructions from all MCP servers in the system prompt." | cli-command-reference.md:660 | … |`;
- one 11-cell SOURCES row `S039` citing `https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference`, kind `docs`, tier `A`, status `mined`, opened `2026-10-22`, `used-by` naming the entry;
- one Gate bullet in the lesson containing `S039` and the quote verbatim.

```
$ python3 -B probe/verifiers/check_mcp_instructions.py --root probe --fetch
MCP specification  BACKED found=True
Claude Code        BACKED found=True
VS Code            BACKED found=True
Codex              BACKED found=True
Gemini CLI         BACKED found=True
opencode           no rows naming client: 0 (need 1)
Copilot CLI        BACKED found=True
mcp instructions backed 6 of 7 clients
mcp instructions found on the live page 6 of 6
probe-exit=0
```

Lane baseline at the judged revision, for comparison:

```
$ python3 -B verifiers/check_mcp_instructions.py --rev c8407a453788df964df5a7b835dd0ce1360de882 --fetch
… Copilot CLI        no rows naming client: 0 (need 1)
mcp instructions backed 5 of 7 clients
mcp instructions found on the live page 5 of 5
exit=0
```

So C2's printed number is true as printed (`5 of 7`, target ≥3), but the client list is not: the seventh client is admissible and would print `6 of 7` with no judgment-table change (data row only). Id note: `S039` is proposed for the carried S024 superseding row (`.ufo/waves/round-52/falsify-a2/ScribeS024.md:66,94`); if that lands first, the Copilot CLI row takes `S040`. My probe used S039 for convenience only; it is scratch, not a lane id.

## Verdicts and severity

Line numbers below are the `c8407a4` working-tree content as read at 17:50Z; the L1's 17:57Z uncommitted fix moved them (see Concurrent lane state).

| # | attack | verdict | severity |
|---|---|---|---|
| 1 | Entry `:32-37` Copilot CLI reject ("never about server instructions"; client-level silence) | **BREAKS** — two pinned-host primary sources document the field: command reference `:660` (default allowlist, on-demand retrieval, all-servers flag) and repo changelog `:2895` / `:1157` / `:219` | **High** for the entry (a false Q14 negative, refutable from bytes the round already held) |
| 2 | Entry `:47-48` "two of the seven clients … document nothing about it" | **BREAKS** — Copilot CLI documents it; only opencode remains silent by the entry's own record (I did not re-run opencode's sweep; outside this seat) | **High** (same sentence) |
| 3 | Entry `:41-42` "Four clients … put the text in front of the model" | **BREAKS by consequence** — the docs sentence is "Include initialization instructions from all MCP servers in the system prompt", so Copilot CLI is a fifth such client, gated by an allowlist | **Medium** (count understated once the row is added) |
| 4 | `SKILL.md:94` "the opencode and Copilot CLI pages opened on 2026-10-22 say nothing about server instructions (entry § sweep)" | **Knock-on** — literally true of the two pages the entry opened, but the clause defers to the broken sweep; the parenthetical must change when the entry is fixed. `SKILL.md:86`'s `S032–S037` range also stops matching if the new row is cited | **Medium** |
| 5 | C2's printed claim (`backed 0 of 7` → ≥3 of 7; `--fetch` 5 of 5) | **HOLDS** — 5 of 7 and 5 of 5 reproduce at the judged rev, exit 0; the target is met with or without Copilot CLI | none (the defect is the entry's prose, not the counter number) |
| 6 | The entry's two Copilot fetch records (`14,240 B`; `404`, `502 B`) | **HOLDS** — byte-identical to my re-fetches, same sha256; they are simply too narrow to support the sweep's conclusion | none |

What the L1 needed to change at the judged revision (defect report, not an edit; the working tree has since been fixed — see below): replace the Copilot CLI reject with an admitted row (`S040` if S039 is spent), quote the 11-word first sentence at `cli-command-reference.md:660`, record the reading as "included in the system prompt for allowlisted servers by default; other servers' instructions are retrieved on demand; `--allow-all-mcp-server-instructions` includes all", then rewrite entry `:32-48` (five clients, one silent client), extend the entry's `source:` line at `:1` (it names S032–S037 only), update `SKILL.md:86,94`, and keep the `add-mcp-servers.md` and 404 observations as bounded page facts.

## Concurrent lane state (read-only, 18:00Z)

When I finished the sweep, `git status --short -- .` showed `SKILL.md`, `corpus/SOURCES.md` and `corpus/knowledge/mcp-server-instructions-round52.md` modified on top of `c8407a4` (plus the pre-existing `SCORECARD.md`). Those are the L1's uncommitted fixes, written at 17:57Z while this seat ran; I did not write them, and this report is my only lane write.

- The entry now carries `| Copilot CLI | S042 | "Add --allow-all-mcp-server-instructions to optionally include instructions from all MCP servers in system prompts" | changelog.md:1157 … |` (`:32`), the sweep paragraph records the old negative as wrong (`:34-41`), and `SKILL.md:86,94` now cite S040–S042 and drop the silent-client clause.
- `python3 -B verifiers/check_mcp_instructions.py --root . --fetch` at 18:00Z prints `backed 7 of 7`, `found on the live page 7 of 7`, exit 0 (opencode was also fixed, via S041).
- Remaining gap this seat closes: S042's reading still ends "[INFERENCE: the changelog does not say which servers are included without the flag]". The docs command reference at `:660` says it — only allowlisted server instructions are included up front, other servers' instructions are retrieved on demand. Adding that page to S042's anchor/source (or a new row, S043) removes the inference; the docs quote passes the frozen counter unchanged (probe above), and the current 7 of 7 does not depend on changing the counter.

## Remaining unknowns

- How a server becomes "allowlisted" for instructions is not stated on the command reference; the page's enterprise-allowlist section is about which servers may load, not which instructions load up front. Do not merge the two controls in the reading cell without a source.
- The docs page states no version gate; the changelog places the flag at 1.0.66 (2026-06-30) and "support" at 0.0.400 (2026-01-30). Whether the current default behaviour is exactly the flag's behaviour at every version is [INFERENCE].
- No client was run; no source code was read (the public repo contains only `README.md`, `changelog.md`, `install.sh`, `LICENSE.md` and `.github/`). Claims rest on vendor documentation, as the entry's Limits already say.
