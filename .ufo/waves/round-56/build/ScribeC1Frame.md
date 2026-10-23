Result: PARTIAL — the requested entry and SKILL.md frames are drafted, but the entry’s source field cannot be finalized without the new client-source rows.

## Paste-ready draft: `corpus/knowledge/agent-definition-files-round56.md`

The frontmatter `source:` value below is an explicit citation slot, not a claim or a real citation. The current `corpus/SOURCES.md` ends its registry at S071; this seat has no new C1 source-row URLs or anchors to cite. Replace the slot with the actual per-client S### citations before treating the entry as admitted.

```markdown
source: S### (client documentation URL, page anchor) for each client row below
verified-at: 2026-10-23
recheck: python3 -B verifiers/check_agent_definitions.py --rev <rev> --fetch

# Agent-definition files by client (round 56)

This entry records where each client's own documentation says its agent-definition files live and what those files set. These are documentation statements, not measurements of whether a client discovers, loads, or applies any such file.

## Per-client record

| Client | Location | Source | Quote |
|---|---|---|---|

## Findings

## Limits

- `verifiers/check_agent_definitions.py --rev <rev> --fetch` checks the first table under the named SKILL.md heading: its fixed header, one unique row per pinned client, the first backticked location token (including its path form, `agent`/`agents` segment, and ownership under that client's frozen configuration roots), and at least three words in the Action cell. In the entry table it checks client, Source ID, and Quote cells: a 3–25-word quote with the location token and a separate `agent`/`subagent` word; a cited SOURCES row with an eligible new ID and URL, `docs` kind, tier A, `mined` status, an allowed opened date, pinned host, and no base URL or tracker-page URL; and the quote recorded in `corpus/lessons/round-56.md` § Gate. With `--fetch`, it additionally checks the live page for the quote and a boundary-delimited location token, then counts distinct normalized paths absent from the base tree outside `.ufo/`. The predicate exits 0 only at F ≥ 5 and G ≥ 2.
- The counter does not assess the `What the file sets` cell's substantive accuracy or completeness, the source's meaning beyond its coded checks, or whether a client actually discovers, loads, or applies a file. Those are reviewer readings of the cited documentation, not measured client behaviour; clients outside the seven pinned clients are out of scope. The counter also does not validate this entry's `source:`, `verified-at:`, or `recheck:` frontmatter.
```

## Paste-ready SKILL.md intro

> The agent-definition fidelity checklist below is opencode-only, so select the right client-specific file from this table before applying it; do not assume `opencode/agents/*.md` is a universal location. Basis: `corpus/knowledge/agent-definition-files-round56.md`; checked by `verifiers/check_agent_definitions.py`.

Place `### Agent-definition files by client` inside `## Agent-definition fidelity checklist`, after that section's current opening paragraph (SKILL.md lines 310–314) and before its first checklist box (line 316). The table then provides the client-specific target before the existing checklist; leave all nine agent-definition box texts unchanged. SKILL.md currently ends at line 598 while its line-budget box sets a 600-line ceiling (lines 300–303), so integration must make room without changing those boxes.

## Findings and evidence

- **Frame and predicate:** `plans/round-56.md:19-45` defines C1 as the client decision table plus sourced entry and gives the F ≥ 5, G ≥ 2 `--fetch` predicate. `verifiers/check_agent_definitions.py:26-68,70-98` specifies the table cells, quote/source conditions, live-page check, and output predicate. The implementation read at `verifiers/check_agent_definitions.py:548-606,1085-1159` confirms the row checks and exit condition.
- **Q31 boundary:** `corpus/QUALITY.md:42` says counter prose must name only tests the code reads and label unrun checks reviewer judgment. The `What the file sets` cell is not semantically inspected by the counter; runtime discovery/loading is not measured by this counter either. `corpus/knowledge/explicit-invocation-round55.md:1-12,18-21,30,64-77` supplied the frontmatter, scope, table, Findings, and Limits style.
- **Placement and unchanged boxes:** `SKILL.md:308-354` contains the parent heading, its current opening paragraph, and the nine existing agent-definition checklist boxes; `SKILL.md:300-303` states the 600-line limit. No product file or box text was edited.
- **Source slot:** `corpus/SOURCES.md:77-86` shows the current last registry row S071 followed by `## Paths`; no new C1 source-row citation was available to this seat.
- **Frozen-counter version conflict, verbatim:** the assignment context says, “the C1 counter v1.1 at e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8 and its rules, target and predicate are frozen”. The plan instead says, “**C1 counter v1.3 (erratum 3, same commit, before any C1 content).**” and “This is the C1 counter the claim is judged on”. See `plans/round-56.md:124-155`; this conflict is reported, not resolved here.

## Gates, touched surfaces, and limits of this seat

- Shell commands, tests, counter runs, and source fetches: none. No check is claimed as run or passed; no tool was installed.
- Touched surface: only `.ufo/waves/round-56/build/ScribeC1Frame.md` (this report). `SKILL.md`, the entry, `corpus/SOURCES.md`, lessons, counters, and C2 surfaces were not edited.
- Out of scope: authoring client source rows/quotes, filling the real frontmatter citations, inserting the table into SKILL.md, resolving the counter-version conflict, and all C2 redesign or execution work.
- Provenance: repository text read from the paths and line ranges cited above; the requested `verified-at: 2026-10-23` is reproduced as the specified draft field, not presented as a source fetch performed by this seat.
