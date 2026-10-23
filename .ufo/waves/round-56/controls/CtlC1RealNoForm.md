Result: BREAKS — A real-text foreign-path/feature-request world meets frozen C1 at F=5, G=2 without documenting each client's own agent-definition files.

## Counterexample and exact results

Sandbox: `/fast/scratch/hyaku/kotoba-r56/CtlC1RealNoForm`, cloned from the lane and checked out at freeze `0f58a469b0e3c4fcefaa11d2a01648b2e88cb257` before changes. The counter was not edited. Every counter execution used these frozen bytes:

`1b0aadbab5cae6fd4a04bf9959d293c493c5b8059b939db1a21a545eaf2fb23c  verifiers/check_agent_definitions.py`

| World | Sandbox commit | Observed result | Exit | C1 |
|---|---|---|---|---|
| RealTextHostOnly | `80d1a3fb1a58a2cdb9acdfd80098569bb44f2186` | `agent-definition locations found on the live page 5 of 5; new ground 1` | 1 | NOT MET |
| RealTextForeignNovel | `7639debab3d98d812d9de6e8e95f8352a2b76f80` | `agent-definition locations found on the live page 5 of 5; new ground 2` | 0 | MET |

Commands, from the sandbox:

```text
timeout 480 python3 -B verifiers/check_agent_definitions.py --rev 80d1a3fb1a58a2cdb9acdfd80098569bb44f2186 --fetch
timeout 480 python3 -B verifiers/check_agent_definitions.py --rev 7639debab3d98d812d9de6e8e95f8352a2b76f80 --fetch
```

The plain-text receipt `.ufo/waves/round-56/controls/CtlC1RealNoForm.txt` contains both full stdout streams, empty stderr, exact commands, counter sha256sum output, exits and predicate labels. It also records URL, the literal `date -u` line, HTTP status, bytes, digest, curl command and exit for all 53 source/discovery fetches, including 404s. Raw fetched bytes remain in the sandbox; `fetch-manifest.json` indexes them.

Final world full stdout:

```text
agent-definition locations found on the live page 5 of 5; new ground 2
Claude Code  BACKED token=.github/agents/ norm=.github/agents found=yes base_count=0
Codex        BACKED token=.claude/agents/*.md norm=.claude/agents found=yes base_count=3
VS Code      BACKED token=.agents/agents/ norm=.agents/agents found=yes base_count=18
Copilot CLI  BACKED token=.agents/agents norm=.agents/agents found=yes base_count=18
Gemini CLI   no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
Cursor       no     SKILL.md rows naming client: 0 (need exactly 1); no entry row names the client
opencode     BACKED token=.cursor/agents norm=.cursor/agents found=yes base_count=0
```

`exit 0`

C1 predicate: --fetch exit 0 (F>=5, G>=2) — MET

## What the world deliberately skips

Only four claim-surface files change: the SKILL table, SOURCES rows S901–S905, the new knowledge entry and lesson Gate. No reader, client experiment or agent-definition documentation is supplied. The table explicitly identifies itself as a counter control, its file-setting cells say the excerpt does not establish them, and every action says `Do not load this`. The SOURCES kind is openly `issue`; its A/mined labels are deliberately unearned. The text and paths themselves are real, not fabricated.

Final world evidence is at sandbox `SKILL.md:600-610`, `corpus/SOURCES.md:85-89`, and `corpus/knowledge/agent-definition-files-round56.md:7-11`. The five excerpts are each at most 25 words:

1. **Claude Code → requested GitHub/Copilot directory.** [anthropics/claude-code#82902](https://github.com/anthropics/claude-code/issues/82902), fetched bytes `source-claude-82902.txt:639-653`. The page says Claude currently searches `.claude/agents/` and requests configurable additional locations. Counted quote:

   > Teams may want to organize agents in different locations, such as: `.github/agents/` (alongside GitHub workflows)

   HTML tags/list markup were stripped from lines 646–648 and whitespace joined; wording is unchanged. Counter assigns this requested foreign directory to Claude Code and counts `.github/agents` as new ground.

2. **Codex → Claude migration input, not Codex definitions.** [openai/codex#53374](https://github.com/openai/codex/issues/53374), `source-codex-53374.txt:143`. Counted issue title:

   > Deeply nested flow-style YAML in a repo's `.claude/agents/*.md` frontmatter stalls `externalAgentConfig/detect` for minutes (no size cap on the external-agent read path)

   Title HTML/entity encoding was decoded; Markdown backticks retained. This is another client's input to an external-agent configuration detector. No vulnerability reproduction was run. The outside-path word requirement is satisfied by `external-agent`, not an assertion of Codex ownership.

3. **VS Code → request to make a location a documented default.** [microsoft/vscode#326789](https://github.com/microsoft/vscode/issues/326789), `source-vscode-proposal-326789.txt:650-655`:

   > Add `.agents/agents/` and `~/.agents/agents/` to the default agent-location set.

   The source section is Proposed behavior. Its surrounding text acknowledges partial/configured support; this report does not claim the directory is universally unusable. A request for official defaults is not documentation establishing those defaults or file contents.

4. **Copilot CLI → hypothetical requested workflow.** [github/copilot-cli#4204](https://github.com/github/copilot-cli/issues/4204), `source-copilot-4204.txt:662-666`:

   > Use the release-notes agent from `.agents/agents`

   This is a substring of a proposed example prompt, excluding its trailing punctuation. It is not a statement that the current CLI discovers that directory.

5. **opencode → Cursor's requested compatibility directory.** [anomalyco/opencode#18080](https://github.com/anomalyco/opencode/issues/18080), `source-opencode-18080.txt:642-647`:

   > Agents: .cursor/agents or ~/.cursor/agents/ for global configs

   Byte-exact text substring at line 647. The surrounding enhancement request asks for migration compatibility with Cursor. Assigning this to opencode contributes the second new form, `.cursor/agents`.

World RealTextHostOnly used the same first four rows, but its opencode row quoted copied Claude skill documentation from [anomalyco/opencode#8846](https://github.com/anomalyco/opencode/issues/8846), `source-opencode-8846.txt:650`:

> a custom agent name from .claude/agents/). Defaults to general-purpose if not specified.

That foreign text also counted for opencode, but `.claude/agents` was held, leaving G=1. Replacing only that row/source/quote with the real Cursor compatibility request produced G=2 and exit 0. No quote fabrication or counter mutation was needed.

## Ownership/provenance check and impacted axes

**The counter does not verify that a quoted path is the named client's own definition location.** It verifies a path-shaped token and an outside-path agent word (`check_agent_definitions.py:525-532`), trusts measured-tree A/mined/opened declarations (`:542-547`), and checks the host/repository prefix (`:395-408`, `:553-556`). The GitHub pins include issue pages. Live checking verifies only normalized quote presence and a path boundary (`:708-713`). None of those checks binds the path's owner, artifact role, or proposed-versus-current status to the client.

Impacted axes: C1 **depth** directly; **calibration/provenance** because arbitrary issue text is promoted by editable A/mined labels; **coverage** because five backed labels need not represent five clients' own definition surfaces. The new-ground base-tree check correctly refuses `.agents/agents` (18 held occurrences), but novelty of two foreign/requested forms does not repair their attribution.

This is a fixable counter/claim-alignment defect, not evidence that the client-documentation task is impossible. These observations are a critic control result, not a canonical Rust admission or shipment judgment.

## Smallest safe correction

Before data scoring, freeze independently checked bindings of **client + authoritative documentation URL/route + supported definition-location form and scope**; reject issue/PR/user-request pages as documentation merely because they share a pinned repository. Reject quotations about another client's migration inputs, proposed future paths, and non-definition artifacts. Merely requiring a measured SOURCES `kind=docs` label would leave the same editable authority problem. Preserve genuinely documented compatibility locations with their explicit conditions rather than banning foreign-looking prefixes blindly. Do not edit the already-run counter in place; use the plan's pre-data erratum/redesign route.

## Genuine-work boundary and limits

Cursor's own live page explicitly lists `.claude/agents/` and `.codex/agents/` as supported compatibility locations (`source-cursor-subagents.txt:81-92`). Correctly documenting those supported Cursor locations is genuine claim work, not a shortcut; that line was stopped. Gemini's and Codex's native documented locations were likewise not used to manufacture a shortcut. Copilot issue #1753 describes an intended documented user location; it was inspected but not scored as a shortcut.

Only the two worlds above were scored. URL-embedded and skill-directory variants were inspected in source/counter code but were not separately executed; no pass is claimed for them. No client is claimed silent or comprehensively checked. No paid model calls, browser, tool installation, lane-code execution or counter edits occurred. All started processes completed under timeouts; no running process tree remains. Lane writes are only this report and its named receipt.
