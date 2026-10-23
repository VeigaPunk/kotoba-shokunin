Result: DONE — drafted the requested source-aware C1 entry frame in this report only; no lane knowledge, skill, source-registry, or lesson file was written.

## Scope, evidence, and touched surfaces

- **Deliverable:** an unpopulated Markdown frame for `corpus/knowledge/plugin-manifests-round57.md` appears below. Bracketed slots remain for source-seat material and integration; no plugin manifest path, quotation, capability, or finding is supplied as fact.
- **Only file written:** `.ufo/waves/round-57/build/ScribeC1Entry.md` (this report). The target knowledge entry and `SKILL.md` were not changed. No counter, source page, or client was run; no tools were installed or updated.
- **Evidence read:** `plans/round-57.md:25-43,102-133` (C1 scope, predicate, v2 and C2 withdrawal); `verifiers/check_plugin_manifests.py:36-56,64-83,102-158,178-188` and `:628-707,710-774,1780-1858` (frozen checks); `corpus/QUALITY.md:15,23-25,41-42` (Q04, Q12-Q14, Q30-Q31); `corpus/knowledge/agent-definition-files-round56.md:1-20,40-86` (entry shape). The requested round-57 lesson path was read and returned “not found”; its `## Gate` material is therefore a source-seat/L1 integration slot, not evidence available to this report.
- **Gate status:** no command or verification was executed. The `recheck:` below is the requested future command, not a claimed pass. The required observed output, source URLs/anchors, and quotes remain unfilled.
- **Quality boundaries:** Q12 is scaffolded by the opening triple; source URL/anchor placeholders must be replaced by actual opened S079–S085 sources and corresponding rows before admission. No measured count or negative finding is asserted (Q13/Q14). A “documents nothing about Y” claim must remain “not checked” unless its sweep includes the vendor changelog/release notes, current docs source tree, and corpus grep (Q30). The `Limits` section identifies exactly what the counter reads and separates it from reviewer judgment (Q31).
- **Out of scope:** source research/fetching, completing `corpus/SOURCES.md` or the lesson Gate, drafting factual plugin-capability claims, changing the `SKILL.md` table, running C1, and all C2 rule/fix work. C2 remains withdrawn before data per `plans/round-57.md:124-133`.

## Draft text for L1 integration

```markdown
source: S079 ([Claude Code URL + anchor — source seat/L1 fills]), S080 ([Codex URL + anchor — source seat/L1 fills]), S081 ([VS Code URL + anchor — source seat/L1 fills]), S082 ([Copilot CLI URL + anchor — source seat/L1 fills]), S083 ([Gemini CLI URL + anchor — source seat/L1 fills]), S084 ([Cursor URL + anchor — source seat/L1 fills]), S085 ([opencode URL + anchor — source seat/L1 fills])
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch

# Plugin manifests by client (round 57)

This entry compares what each client's own documentation says about its plugin or extension manifest and the instruction-bearing contents a plugin can ship. These are documentation claims, not measurements of client loading behavior. Complete each client-specific statement from the cited source; do not infer a capability from a manifest filename alone.

## Per-client record

| Client | Manifest | Source | Quote |
|---|---|---|---|
| Claude Code | [`[manifest path from source]`] | S079 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| Codex | [`[manifest path from source]`] | S080 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| VS Code | [`[manifest path from source]`] | S081 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| Copilot CLI | [`[manifest path from source]`] | S082 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| Gemini CLI | [`[manifest path from source]`] | S083 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| Cursor | [`[manifest path from source]`] | S084 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |
| opencode | [`[manifest path from source]`] | S085 | [verbatim 6–25-word quote holding the manifest token and a plugin/extension word outside it] |

## What a plugin can ship

[Compare only components explicitly described by the cited client documentation. Cite source anchors in the cells or the evidence column. Do not treat an unmentioned category as absent: use “not checked” unless the complete Q30 sweep supports a bounded “not stated” finding.]

| Client | Skills | Agents | Commands | Context files | MCP servers | Source/anchor(s) and qualification |
|---|---|---|---|---|---|---|
| Claude Code | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S079 anchor(s); scope or caveat] |
| Codex | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S080 anchor(s); scope or caveat] |
| VS Code | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S081 anchor(s); scope or caveat] |
| Copilot CLI | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S082 anchor(s); scope or caveat] |
| Gemini CLI | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S083 anchor(s); scope or caveat] |
| Cursor | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S084 anchor(s); scope or caveat] |
| opencode | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [documented items / not checked] | [S085 anchor(s); scope or caveat] |

## Findings

- [Source-backed cross-client finding; cite the specific S### row and source anchor(s).]
- [Source-backed contrast or qualification; distinguish what documentation explicitly states from interpretation.]
- [Do not add a “documents nothing about Y” conclusion without the Q30 sweep; otherwise record the client/topic as “not checked.”]

## Limits

- **Frozen counter scope:** `python3 -B verifiers/check_plugin_manifests.py --rev <rev> --fetch` evaluates the first table under the exact `### Plugin manifests by client` heading (header, client rows, first backticked manifest token, token rules, and Action word minimum); the entry's matching record table (client, manifest, source ID, quote); the cited `SOURCES.md` row's ID/URL and checked kind, tier, status, opened date, pinned host, and URL exclusions; and whether the quote is recorded in the round-57 lesson's `## Gate`. With `--fetch`, it checks that the live page contains the quote and token at a token boundary. It computes new ground against the frozen base tree outside `.ufo/`.
- **Predicate, not a result:** the command passes only if its output is `plugin manifests found on the live page F of K; new ground G` with `F >= 5` and `G >= 3` (frozen rule: `plans/round-57.md:31-33`; `verifiers/check_plugin_manifests.py:178-183`). `[After an observed run, record each actual count in the lesson Gate as <number> — <command> <run date>; do not replace this slot with a target or an unrun result.]`
- **Reviewer judgment (Q31):** the counter does not read or validate the `What a plugin can ship` cells, the comparison matrix, or these Findings; it does not establish that a client actually loads the declared manifest, that the component comparison is complete or correctly interpreted, or what clients outside these seven support. Those are source-review judgments, not counter checks.
- **Negative claims (Q14/Q30):** no silence or absence is asserted by this frame. Any later claim that a client documents nothing about a component must carry the sweep: vendor changelog/release notes, current docs source tree, and a grep of the lane corpus. If any part is missing, say “not checked.”
```

## Artifact

- Report and embedded draft: `.ufo/waves/round-57/build/ScribeC1Entry.md`.
- Intended future target (not written): `corpus/knowledge/plugin-manifests-round57.md`.
