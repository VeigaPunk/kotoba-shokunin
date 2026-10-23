Result: MIXED — Depth naming and the different-Frontier-row anti-loop survive this attack; the frozen counter does misname that Frontier row.

# Scope and evidence boundary

Read-only review of axis fit and anti-loop at lane tip `07c33d73ddce769d9cea2846a6313164401b5478`, comparing base `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a`. This is a critic's scoped finding, not a canonical judgment, admission, or no-harm certification. No counter, test, client, or other runtime was invoked. No external source was fetched. No untrusted attempt-2 patch or excluded scratch record was used. No tools were installed or updated.

# 1. Axis fit: the coverage counterexample is strong, but does not establish misnaming

**Counterexample tested.** C1 starts with an unheld plugin frontier, adds new manifest paths, and counts distinct paths absent from the base. That resembles coverage much more directly than a numeric depth score. The lane's closest contrary precedent is round 52: `plans/round-52.md:39-58` declared **coverage** for a sourced knowledge entry plus a SKILL decision table on the other half of the very same *MCP/plugin instruction surfaces* row. `SCORECARD.md:30` still records that claim under coverage. Ownership of depth (`SCORECARD.md:3-15`) is not itself a reason to call new ground depth.

**Why that counterexample is not decisive.** Fleet `../AXES.md:11-12` defines depth by verifiable technical detail and actionable instructions, and coverage by the domain surfaces governed. These definitions can overlap; neither says every frontier-derived decision table must be called coverage. Fleet §9 (`../.ufo/prompts/kotoba-round-57.md:361-365`) prohibits choosing the axis from the number, not adding technical depth on previously unheld ground.

The committed change is not only seven extra rows or a manifest-token census. `SKILL.md:111-123` adds a packaging-aware audit step and technical distinctions: optional manifest versus required extension manifest, root versus compatibility formats, files at the plugin root rather than inside the manifest directory, and code modules rather than a JSON manifest. The action cells tell the reader where to look and which format to audit. These are the kinds of claimed technical distinctions depth governs. Their vendor correctness belongs to the source/ship-cell reviews; I have not independently established it here.

This is consistent with, rather than an invention beyond, rounds 54–56:

| Round | Declared depth surface | Why it is more than a count | Local evidence |
|---|---|---|---|
| 54 | Description thresholds by client | Authoring maximum versus render cut/budget, and what to do when descriptions are shortened | `plans/round-54.md:24-36`; `SKILL.md:189-201` |
| 55 | Explicit invocation by client | User-typed form versus model activation; how to exclude only the explicitly named activation from an implicit-trigger measure | `plans/round-55.md:18-41`; `SKILL.md:203-215` |
| 56 | Agent-definition files by client | Format/schema differences and avoiding use of an opencode checklist on other clients | `plans/round-56.md:19-45`; `SKILL.md:97-109` |
| 57 | Plugin manifests by client | Package origin, layout/format distinctions, and the resulting audit action | `plans/round-57.md:25-43`; `SKILL.md:111-123` |

The prior non-author records explicitly call C1 depth improved and coverage unchanged: `corpus/lessons/round-54-verifier-spotcheck.md:150-159`, `round-55-verifier-spotcheck.md:99-108`, and `round-56-verifier-spotcheck.md:168-178`. Those are comparison evidence, not authority to override this assignment. In particular, the round-54 record itself notes that the later surface-naming clause was not in its dispatched prompt (`round-54-verifier-spotcheck.md:120-122`).

**Review verdict:** depth is a defensible declared axis for the technical audit table. If the claimed result were merely new manifest locations, coverage would be the better description; a table's existence alone does not make it depth. The actual content and its stated reviewer guard prevent that reduction here. No compulsory depth→coverage relabel is established.

**Impacted axes and accounting boundary:** depth naming survives, but this does not verify the depth claim. Coverage receives no separate verified move. The frozen counter checks path/quote provenance and only a minimum action-cell length (`verifiers/check_plugin_manifests.py:64-69,108-132`); the plan expressly leaves component correctness to reviewers (`plans/round-57.md:42-43`). Do not convert a path count into a broad technical-correctness or coverage certificate.

# 2. Anti-loop: HOLDS for C1, without crediting withdrawn C2

The actual table rows, not their numerical counters or their file type, distinguish the surfaces:

| Round | Frontier row actually worked | Evidence |
|---|---|---|
| 53 | *Loader-rule freshness* and *Executed checklist coverage*, always-on half | `plans/round-53.md:22-54`; `corpus/README.md:117-124` |
| 54 | *Per-render consumption*, offer-render half | `plans/round-54.md:15-19`; `corpus/README.md:126-130` |
| 55 | *Implicit-intent fidelity*, explicit-invocation prerequisite | `plans/round-55.md:18-22`; `corpus/README.md:132-137` |
| 56 | *Executed checklist coverage*, agent-definition client map, not an executed box | `plans/round-56.md:10-22`; `corpus/README.md:139-145` |
| 57 C1 | *MCP/plugin instruction surfaces*, plugin-manifest half | `plans/round-57.md:15-29`; `corpus/README.md:102,147-153` |

The strongest overlap objection is that plugins ship skills and agents already covered in rounds 53–56. That does not make the package-origin/manifest-format audit surface identical to skill listing, explicit invocation, agent schema, or box execution. The exact row at `corpus/README.md:102` is different from rows `:99,101,103,104` used by those rounds. The row was worked in round 52, but its note explicitly left plugin surfaces unheld (`corpus/README.md:106-111`); this is not a claim that the whole row was never touched.

Round 53's work is more varied than the shorthand “skill-listing” suggests, but accounting for its loader-freshness claim still does not produce a round-53–56 move on the MCP/plugin row.

C2's proposed *Command extraction* row (`corpus/README.md:100`) is not needed to establish the anti-loop. C2 was withdrawn before data (`plans/round-57.md:124-133`), so it cannot be presented as a second completed frontier move.

No frontier→Core success follows from passing this anti-loop check. `PROVINCE.md:19,28` still leaves plugin surfaces Frontier; `corpus/README.md:147-156` explicitly records the C1 miss and withdrawn C2. The pinned base→tip diff changes neither `PROVINCE.md` nor the existing Frontier table rows; it appends the round-57 note.

# 3. Fixable documentary defect: the frozen counter names a nonexistent row

`verifiers/check_plugin_manifests.py:39-40` calls its target Frontier row *Plugin manifests*. There is no such row in `corpus/README.md:97-104`; the existing row is *MCP/plugin instruction surfaces*. The plan and README already map C1 correctly, so this is a reference defect, not an anti-loop failure or a reason to change the axis.

**Smallest safe correction:** append a documentary erratum to the lesson/final report. Do not edit the frozen counter or rewrite the frozen declaration. Record this exact old→new reference correction:

Old (`verifiers/check_plugin_manifests.py:39-40`):

```text
and what to do with it when reading a skill -- the `corpus/README.md` Frontier
row *Plugin manifests*.
```

New (erratum reading only):

```text
and what to do with it when reading a skill -- the plugin-manifest half of the
`corpus/README.md` Frontier row *MCP/plugin instruction surfaces*.
```

Impacted axes: depth/coverage provenance and surface identification only. This does not change the predicate, clients, target, axis declaration, scores, or route.

# 4. The miss remains the miss

Read, not rerun: `.ufo/waves/round-57/C1-measure.txt:1-13` records the committed content revision, frozen v2 sha256, `plugin manifests found on the live page 4 of 4; new ground 4`, and exit 1. The predicate remains F ≥ 5 and G ≥ 3 (`plans/round-57.md:31-33,119-120`). `SCORECARD.md:28,148` already records MISS and holds depth at 9. Neither preferring coverage nor accepting depth naming repairs that frozen miss. There is no successful coverage fallback or saturation conclusion in this review.

# Read-only command evidence

Commands below ran with cwd `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; no lane code was executed.

1. `timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --unified=5 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a 07c33d73ddce769d9cea2846a6313164401b5478 -- SKILL.md corpus/README.md PROVINCE.md` — exit 0. Output adds the plugin table, moves the older decision-table craft block to its corpus pointer, adds two gate-registry rows and the round-57 Frontier note, and makes two routed historical opencode corrections. No `PROVINCE.md` diff.
2. `timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -n -i -E 'plugin|extension' 47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a -- SKILL.md PROVINCE.md corpus/README.md corpus/knowledge/instruction-surface-census-round13.md corpus/lessons/round-54.md corpus/SOURCES.md` — exit 0. Output includes base `PROVINCE.md:19,28`, Frontier row `corpus/README.md:102`, round-52 remainder `:110`, base source S028 at `corpus/SOURCES.md:41`, and existing generic plugin-loader census entries. Thus generic plugins were not unknown to the lane; the new manifest/audit detail must carry the depth rationale, not the bare word “plugin”.
3. `timeout 30s git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin diff --name-only 07c33d73ddce769d9cea2846a6313164401b5478 -- SCORECARD.md PROVINCE.md SKILL.md plans/round-52.md plans/round-53.md plans/round-54.md plans/round-55.md plans/round-56.md plans/round-57.md corpus/README.md corpus/knowledge/plugin-manifests-round57.md corpus/lessons/round-54-verifier-spotcheck.md corpus/lessons/round-55-verifier-spotcheck.md corpus/lessons/round-56-verifier-spotcheck.md corpus/lessons/round-57.md verifiers/check_plugin_manifests.py .ufo/waves/round-57/C1-measure.txt` — exit 0, no output. The lane document line pointers used above therefore match the named tip at inspection.
