Result: DONE — drafted the requested conditional Round-57 Frontier notes and Core line; only this report was written.

# Draft text for integration

Append these two paragraphs after the Round-56 append-only note in `corpus/README.md` § Frontier:

> **Round 57 (append-only note on the MCP/plugin instruction surfaces row above):** *MCP/plugin instruction surfaces* — if C1 lands, one documented slice moves to Core: where each of the seven pinned clients documents its plugin/extension manifest and what instruction-bearing material a plugin can ship, including MCP servers, held in `knowledge/plugin-manifests-round57.md` and acted on in `../SKILL.md` § Plugin manifests by client (`../verifiers/check_plugin_manifests.py --rev <rev> --fetch` → `plugin manifests found on the live page F of K; new ground G`, with F ≥ 5 and G ≥ 3). Still not held: whether clients load or run plugins as documented, and whether/how plugin-shipped MCP instructions are loaded or used at runtime.
>
> **Round 57 (append-only note on the Command extraction row above):** *Command extraction* — C2 was withdrawn before data (erratum 1): the frozen predicate was met by a generator-keyed control, a path-keyed control, character skips with an echo fallback, and a stub replacing the gate (`CtlC2GeneratorKeyed`, `CtlC2DoNothingJunk`, `CtlC2CharShortcuts`, `MutC2Counter`). No C2 fix or data claim is made; the info-less fence false FAILs remain Frontier. A later redesign needs to reject those four hollow worlds, include a gate-deletion check so it proves it exercises the actual command-extraction gate, and preserve FAILs for real missing commands. Erratum 1's v2 counter was not re-controlled and lacks that gate-deletion conjunct, so it is not frozen.

Conditional Core bullet for `PROVINCE.md` § Core (include only if C1 lands):

> - Plugin manifests by client (round 57, if C1 lands): the documented plugin/extension manifest locations and declared plugin payload surfaces for seven pinned clients, including instruction-bearing components — `corpus/knowledge/plugin-manifests-round57.md`, acted on in `SKILL.md` § Plugin manifests by client; C1's frozen gate is `verifiers/check_plugin_manifests.py --rev <rev> --fetch` (F ≥ 5, G ≥ 3). This documents what manifests and plugin packages declare, not whether clients load or run plugins or use plugin-shipped MCP instructions; those remain Frontier.

# Findings and evidence

- `plans/round-57.md:15-21,25-43` defines C1 as the sourced seven-client plugin-manifest table/entry and pins its `--fetch` predicate at F ≥ 5 and G ≥ 3. This is the frozen contract, not evidence that the predicate passed.
- `plans/round-57.md:45-65,102-133` establishes C2's scope and erratum 1 withdrawal: the four listed controls met the v1 predicate before data; C2 is not a claim this round; no seat writes the fence-handling fix; v2 was not re-controlled and lacks the gate-deletion conjunct.
- `corpus/README.md:93-115,139-145` supplies the existing Frontier rows and Round-56 note form. `PROVINCE.md:8-29` supplies the current Core/Frontier split, including MCP server `instructions` already in Core and plugin surfaces/behavior in Frontier.
- Read-only attempt to inspect `corpus/knowledge/plugin-manifests-round57.md` returned “not found” at inspection time. Consequently this draft makes no claim about its contents, completed sources, or C1 results; the Core addition is explicitly conditional.

# Touched surfaces, gates, and limits

- Written surface: `.ufo/waves/round-57/build/ScribeFrontier.md` only. `corpus/README.md` and `PROVINCE.md` are proposed targets, not edited by this seat; lane bounds reserve lane writes to the seat's own report.
- Gates: no commands, counters, tests, source fetches, or builds were run. The C1 threshold and C2 withdrawal above are read from the plan; they are not execution evidence from this seat.
- Out of scope: product/code changes, verifier edits, source-registry or lesson updates, C2 redesign implementation, judgment, and integration.
- No tools were installed or updated. No external sources were opened.
