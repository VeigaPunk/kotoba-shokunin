source: S249 — Claude Code — Agent SDK: Agent Skills — https://code.claude.com/docs/en/agent-sdk/skills.md — § Set up skills in a session (heading line 44; sentence at line 46) and § Pre-approve tools for skills (heading line 344; note at line 348) — located quote "frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration" (13 words, one occurrence in the snapshot text view at view line 234 / raw line 348) — snapshot `.ufo/waves/round-81/snapshots/S249.md` (28 395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`), fetch record `.ufo/waves/round-81/snapshots/S249.fetch.json`
source: S248 — Claude Code — Agent SDK: Agent Skills — https://code.claude.com/docs/en/agent-sdk/skills.md — § Pre-approve tools for skills (line 348) — the same page and the row of record for this surface since round 80, cited here because this entry is what its `used-by` cell moves to
verified-at: 2026-10-27
recheck: 30d — `u=https://code.claude.com/docs/en/agent-sdk/skills.md; f=$(mktemp); curl -fsSL -A Mozilla/5.0 --max-time 60 "$u" -o "$f" && sha256sum "$f" && tr -d '\140' < "$f" | grep -c -F "frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration"` — prints the digest line `ac62c2df…` and then `1` on 2026-10-27 (command exit 0). A different digest means the page moved, and every span below has to be re-located in the new bytes before this entry is cited again; the pin is the committed snapshot, never the URL
ground: no knowledge entry documents the Agent SDK's query-config grant channel at base `b284223105f4d106f7e8f56ed4fd296c643cda0e`: `git grep -c 'allowedTools' b2842231 -- corpus/knowledge` (run 2026-10-27) prints two files — `agent-definition-files-round56.md` (2: Claude Code's subagent keys `tools` and `disallowedTools`) and `chinese-vendor-skill-surfaces-round73.md` (1: Qwen Code's `allowedTools`, recorded there as not carried) — and `git grep -c 'allowed_tools' b2842231 -- corpus/knowledge` (same run) prints one file, `allowed-tools-surfaces-round80.md` (1: its own `ground:` line's grep pattern, not a claim); none names an SDK session, a query-config option or an auto-allow relation

Text view: a `.html` snapshot has its `script` and `style` blocks removed, its tags replaced by one space and its entities decoded; a Markdown snapshot has every backtick byte deleted and an unordered-list marker removed at a line start; every snapshot then has its whitespace collapsed to single spaces.
S249 is a Markdown snapshot, so only the Markdown arm shapes it.
Every located quote below is stated in that view, without the backticks the served Markdown carries, and was re-located in the committed snapshot's own bytes before this entry was written (receipts `.ufo/waves/round-81/build/Kb81E08C2Entry-quoteprobe.txt` and `Kb81E08C2Entry-entrycheck.txt`).

# The Agent SDK is a seventh `allowed-tools` surface, and the first with a second grant channel

Round 80 recorded what six pages say a skill's `allowed-tools` frontmatter field means, one row per client, form-level only (`corpus/knowledge/allowed-tools-surfaces-round80.md`).
Its Claude Code row is the CLI page, whose grant is a per-turn permission pre-approval.
The page this entry pins is the Claude Agent SDK's skills page: the same field in an SDK session, documented beside a second channel that lives in the query configuration rather than in the skill file, with an automatic gate that adds the Skill tool when skills are enabled, and a managed-settings override that voids both channels.
It also states the negative in the SDK's own words — the list pre-approves the named tools rather than restricting the others — and names the option that does restrict, which is `skills`, not `allowedTools`.

This entry deepens the held matrix rather than opening an area: it adds one surface, and five mechanisms the six-surface table has no column for (channel, auto-allow relation, explicit-`tools` interaction, managed override, restriction lever).
Everything below is documentary: one page fetched twice and pinned, no SDK installed, imported, configured or run.

## The channels the page documents

| channel | form the page prints | where | what the page says it does | located span |
|---|---|---|---|---|
| frontmatter `allowed-tools` | the skill's own frontmatter key, hyphenated | raw 348 | in SDK sessions it pre-approves tools for a project or personal skill | "pre-approve tools for a project or personal skill with the skill's" |
| query config `allowedTools` (TypeScript) | `allowedTools: ["Read", "Grep", "Glob"]` (raw 380), `["Read", "Write", "Bash"]` (raw 85) | raw 348, 380 | the second grant channel, camelCase spelling | "frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration" |
| query config `allowed_tools` (Python) | `allowed_tools=["Read", "Grep", "Glob"]` (raw 360), `["Read", "Write", "Bash"]` (raw 64) | raw 348, 360 | the same channel under its snake_case spelling | the same span, which names both spellings in one sentence |
| managed settings `allowManagedPermissionRulesOnly` | a managed-settings key, linked to the settings reference | raw 348 | when the organization sets it, Claude Code ignores both grant channels | "in managed settings, Claude Code ignores both" |
| the `skills` option feeding `allowedTools` | `skills="all"`, a list of names, or `[]` (raw 32, 37, 41) | raw 46 | setting `skills` adds the Skill tool to `allowedTools` automatically | "When you set skills, the SDK adds the Skill tool to allowedTools automatically" |
| an explicit `tools` list | `tools` | raw 46 | an explicit tool list has to carry `"Skill"` or skills cannot be invoked | "in that list so Claude can invoke skills." |
| the grant's scope | not a form; a statement | raw 389 | the list pre-approves the named tools rather than restricting the others; the full permission flow is permission modes plus the `canUseTool` callback | "The list pre-approves the named tools rather than restricting the others." |
| skills synced from claude.ai | not a form; an exception | raw 348 | those skills follow their own frontmatter rules | "follow their own frontmatter rules." |
| the option that does restrict: `skills` | exact skill names, `plugin:skill` for plugin skills, prefixed names for clashes in `additionalDirectories`/`add_dirs` (raw 100-104) | raw 98-110 | the model does not see unlisted skills and the Skill tool rejects them, while their files stay reachable through Read and Bash | "The model doesn't see unlisted skills and the Skill tool rejects them" |
| the `skills` list's naming rule | exact names only (raw 106); a wildcard suffix raises an invalid-name error (raw 478, 490) | raw 106 | a non-exact entry fails the session before it starts | "The list takes exact skill names only." |

## The page's own words, span by span

- **Two grant channels in one sentence, and the frontmatter one is the CLI page's.** Raw 348 begins "In SDK sessions, you can pre-approve tools for a project or personal skill with the skill's" and then, after a link to the CLI skills page's pre-approve section, continues "frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration."
  So the SDK page adopts the frontmatter field's semantics by reference rather than restating them, and what it adds is the config channel beside it.
- **The managed override voids both channels at once.** The same paragraph continues "in managed settings, Claude Code ignores both", where the condition is the linked key `allowManagedPermissionRulesOnly`.
  "Both" covers exactly the two channels the sentence just named, so the override is not a per-channel rule.
- **An exception is carved out for synced skills.** The paragraph closes by naming who follows other rules: skills synced from claude.ai "follow their own frontmatter rules."
- **Enabling skills writes into the `allowedTools` channel.** Raw 46: "When you set skills, the SDK adds the Skill tool to allowedTools automatically."
  The same sentence adds that an explicit `tools` list has to carry `"Skill"` — "in that list so Claude can invoke skills." — so the auto-add is a default, not a write that survives an explicit `tools` value.
- **The grant is a pre-approval, said in the SDK's own voice.** Raw 389: "The list pre-approves the named tools rather than restricting the others."
- **The restriction lever on this page is `skills`.** Raw 108: "The model doesn't see unlisted skills and the Skill tool rejects them", and the same sentence continues "while their files remain on disk and stay reachable through Read and Bash."
  It also says that restricting the list does not restrict dispatch by name (raw 108), which is the SDK's own version of the six-surface matrix's finding: the field named like an allow-list does not sandbox, and the option absent from the skill file is the one that removes tools from view.
- **The `skills` list is exact-name only and fails early.** Raw 106: "The list takes exact skill names only." and "If an entry can't work as an exact name" then "query() rejects the list before the session starts."
  Raw 104 adds the prefixed-name form for collision cases and the floor "Requires Claude Code v2.1.309 or later" for it.

## Two spellings, one option, and a third namespace

The page prints every SDK option twice: `allowedTools` in TypeScript and `allowed_tools` in Python (raw 348), matching `settingSources`/`setting_sources` (raw 18, 62, 83) and `additionalDirectories`/`add_dirs` (raw 104).
The skill file's frontmatter key is `allowed-tools`, hyphenated, and the same sentence at raw 348 carries both the hyphenated key and the camelCase option, which is the page's own evidence that they are different namespaces: one is written in the skill, the other in the query configuration.
A skill author and a session developer therefore grant the same thing through different strings, and neither string appears in the other's file.

## Defaults the page states for the surrounding options

- `skills` omitted: "When omitted, discovered skills are enabled and the Skill tool is available, matching CLI behavior" (raw 32), and the discovery default is "the SDK loads user and project sources" (raw 28), so skills in `~/.claude/skills/`, `<cwd>/.claude/skills/` and `.claude/skills/` are found.
- `skills` values: beside the `"all"` and `[]` forms, the page accepts "a list of skill names to allow only those, or [] to let Claude invoke none" (raw 32); it also says to pass `skills: "all"` rather than a wildcard (raw 110).
- Confirmation channel: the init message's `skills` array lists user-invocable skills; a `user-invocable: false` skill "loads and remains available to Claude, but doesn't appear in the array", and "The array lists the same skills whether or not they're in your skills list" (raw 96).
- Who may invoke: "By default, both you and Claude can invoke any skill" (raw 121), and that path is restricted through the skill's frontmatter rather than through `allowedTools`.

## What the page does not state

Each negative below carries its sweep over the committed snapshot: `grep -ci -- '<token>' .ufo/waves/round-81/snapshots/S249.md`, run 2026-10-27.

- **No precedence between the two grant channels.** The sentence joins them with "or" and never says which one wins when both name tools, or whether they union. Sweep: `precedence` 0, `priority` 0, `wins` 0, `override` 0 occurrences.
- **No expiry rule for the option.** The CLI page's per-turn clearing rule is not restated here for the SDK channel: `clears` 0, `cleared` 0, `next message` 0.
- **No statement about an unknown tool name in `allowedTools`.** `unknown tool` 0; the only name-validation rules on the page are for `skills` names (raw 106, 478, 490).
- **No default tool list.** `default` occurs three times and none of them is a tool default: the skills-enablement default (raw 22), the `query()` setting-source default (raw 28) and who may invoke a skill (raw 121).
- **Nothing about subagents and this option.** `subagent` occurs twice (raw 24, 516), both contrasting skills with the `agents` option or linking the subagents page; neither says whether `allowedTools` reaches a subagent.

## Limits

- **Documentary evidence only.** One page fetched twice and pinned on 2026-10-27 (local; `2026-10-28T02:27:26Z` UTC); no SDK package was installed, imported, configured or run, and no claim here is about observed permission behaviour, prompting, tool admission or refusal.
- **The route read is the `.md` export.** The page opens with a `## Documentation Index` pointer to `https://code.claude.com/docs/llms.txt`, which identifies it as the site's `llms.txt`-style Markdown export; the HTML rendering of the same route was not read here and no claim is made that the two carry the same prose.
- **The page states no revision for itself.** No commit, last-modified or build id appears in the bytes: `grep -ci 'last-modified\|revision\|build id'` prints 0. It names two version floors for other behaviours (raw 104 `v2.1.309`, raw 166 `v2.1.274`), which are not floors for the grant channels.
- **The pin is the snapshot and its digest, not the address.** Two fetches 1 s apart were byte-identical (`cmp` rc=0), and the same 28 395-byte body with sha256 `ac62c2df…` is the file round 80's scout seat saved at `.ufo/waves/round-80/build/Kb80S05-agent-sdk-skills.md`, so the page was byte-identical across two rounds and two fetchers. A re-fetch that returns a different digest invalidates every span above until they are re-located; the recheck in the header measures exactly that.
- **Markdown link shaping decides which spans are quotable.** The page wraps the frontmatter key and the managed-settings key in Markdown links, and the text view deletes backticks but keeps link targets, so the view holds `[allowed-tools](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill)` and `[allowManagedPermissionRulesOnly](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)`. Every span above is written around a link, which is why the primary located quote begins mid-sentence at "frontmatter".
- **An inherited quote is unbackable in this view.** The round-80 row's first located quote for this page ends `with the skill's allowed-tools frontmatter or with the allowedTools option`, and that string occurs **0** times in the text view, for the link reason above. This entry does not repeat it, and the row is not rewritten here — its `used-by` cell is the only cell this round changes, so the defect is recorded rather than repaired.
- **Span word counts.** The primary located quote is 13 words; no span quoted above exceeds 25, and each is a single occurrence in the view (receipt `.ufo/waves/round-81/build/Kb81E08C2Entry-entrycheck.txt`, which prints words, occurrences and the view line for every quoted span in this entry).
- **Raw line numbers drift.** Every number above is a line of the committed 2026-10-27 snapshot, never of a live URL.

## Scope

What one page documents about two ways to pre-approve tools in an SDK session for a skill: the skill's frontmatter field, the query-config option in both language spellings, the `skills`-to-Skill-tool relation, the managed override, and the SDK's own restriction lever.
Not claimed: any client's runtime behaviour (none observed), a precedence rule the page never states, the SDK's permission modes or `canUseTool` mechanics (the page links the permissions page and stops), other Agent SDK pages, and the platform API's own skills surface.

## Related

- `corpus/knowledge/allowed-tools-surfaces-round80.md` — the six-surface matrix this entry extends with a seventh surface and five columns it does not carry.
- `corpus/knowledge/agent-definition-files-round56.md` — Claude Code's subagent definition keys, where `disallowedTools` is an agent-file key; this entry's `allowedTools` is a query option, and the page says nothing about how the two meet.
- `corpus/knowledge/chinese-vendor-skill-surfaces-round73.md` — records Qwen Code's `allowedTools` spelling as not carried; that is a different product's key and does not support or contradict anything here.
