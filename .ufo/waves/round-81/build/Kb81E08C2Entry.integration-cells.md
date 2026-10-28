# Kb81E08C2Entry — integration cells for the L1 (proposal text, nothing here is applied)

Seat: leaf, round 81, C2 entry build. The seat's write scope excludes `corpus/`, `SKILL.md`, `PROVINCE.md` and `verifiers/`, so every cell below is TEXT FOR THE L1 to land, not an edit. The entry itself is published verbatim at `.ufo/waves/round-81/build/allowed-tools-sdk-round81.md`; the L1 copies it to `corpus/knowledge/allowed-tools-sdk-round81.md`.

Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`.

## 1. `corpus/SOURCES.md` — new row S249 (11 cells, no `|` inside any cell)

Append to the same registry block that holds S248 (the block whose header is at base line 137):

```
| S249 | Claude Code — Agent SDK: Agent Skills — https://code.claude.com/docs/en/agent-sdk/skills.md | docs | B | What the Claude Agent SDK page documents about pre-approving tools for a skill in an SDK session: the frontmatter field, the query-config option in both language spellings, the skills-to-Skill-tool relation, the managed override and the option that restricts | § Set up skills in a session (line 44 heading, sentence at 46) and § Pre-approve tools for skills (line 344 heading, note at 348); fetched 2026-10-27, HTTP 200, 28395 B, sha256 ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2; snapshot `.ufo/waves/round-81/snapshots/S249.md`, fetch record `.ufo/waves/round-81/snapshots/S249.fetch.json`; located quote "frontmatter or with the allowedTools option (allowed_tools in Python) in your query configuration" | In SDK sessions a skill's frontmatter field pre-approves tools and so does the query-config option; setting skills adds the Skill tool to that option automatically; managed permission rules void both; the option that removes tools from view is the skills list, not the tool list | mined | 2026-10-27 | 90d | corpus/knowledge/allowed-tools-sdk-round81.md |
```

## 2. `corpus/SOURCES.md` — S248, one cell only

- Base (line 189) last cell: `—`
- New last cell: `corpus/knowledge/allowed-tools-sdk-round81.md`
- Every other S248 cell stays byte-identical, including `status` = `queued` (the plan says "no other cell changes"; the census's E11 only resolves `used-by` targets that exist on disk, and it does not forbid a `queued` row from carrying a real one — verified by running the census on a scratch clone, receipt `.ufo/waves/round-81/build/Kb81E08C2Entry-census-scratch.txt`).

## 3. `SKILL.md` — author-facing rule area (base line 164, one sentence appended to that same paragraph)

```
In an SDK session the same field sits beside a query-config channel: the Agent SDK page documents `allowedTools` (TypeScript) / `allowed_tools` (Python) as the second grant, adds the Skill tool to it automatically when `skills` is set, lets managed permission rules void both, and names `skills` — not the tool list — as the option that removes tools from view (entry `corpus/knowledge/allowed-tools-sdk-round81.md`, S249).
```

## 4. `SKILL.md` — counter registry row (8 cells; put it beside the `check_allowed_tools.py` row at base line 518)

```
| `verifiers/check_sdk_allowed_tools.py` | gate | `python3 -B verifiers/check_sdk_allowed_tools.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate — round-81 C2 counter (depth): committed bytes only; prints `sdk allowed-tools surface documented N of 1`; the surface is documented when the entry `corpus/knowledge/allowed-tools-sdk-round81.md` carries `source:` naming S249 and the snapshot, `verified-at: 2026-10-27` and `recheck:`, the S249 row is an 11-cell mined row naming this entry and the canonical URL, the row's snapshot `S249.md` hashes to the pin in both the counter and the fetch record, the entry's located quote occurs in that snapshot's text view, S248's `used-by` names the entry, and `SKILL.md`, `corpus/README.md` and `PROVINCE.md` name the channel | `--self-test` | in-file | none when measuring (reads committed bytes); `--self-test` uses isolated fixture repos under `$TMPDIR` (removed) | kotoba |
```

## 5. `corpus/README.md` — coverage map row (3 cells; beside the round-80 entry row at base line 159)

```
| Agent SDK allowed-tools channel (round 81) | `knowledge/allowed-tools-sdk-round81.md` | entry `corpus/knowledge/allowed-tools-sdk-round81.md` — what the Claude Agent SDK skills page documents about pre-approving tools for a skill in an SDK session — the frontmatter field beside the query-config `allowedTools`/`allowed_tools` option, the `skills`→Skill-tool auto-allow, the `allowManagedPermissionRulesOnly` override that voids both channels, the explicit-`tools` `"Skill"` requirement, and the SDK's own restriction lever (`skills`, whose unlisted entries the model never sees while their files stay reachable through Read and Bash) (S249, snapshot-pinned 28395 B sha256 ac62c2df…; documentary only, no SDK run) |
```

## 6. `PROVINCE.md` — `## Core` bullet (beside the round-80 bullet at base line 34)

```
- Agent SDK allowed-tools channel (round 81, depth): the Claude Agent SDK skills page documents a second grant channel beside the skill's `allowed-tools` frontmatter — query-config `allowedTools` (TypeScript) / `allowed_tools` (Python) — with the `skills`→Skill-tool auto-allow, a managed `allowManagedPermissionRulesOnly` override that voids both channels, and the page's own statement that the list pre-approves rather than restricts while `skills` is the option that removes tools from view (S249; documentary evidence, no SDK run) — `corpus/knowledge/allowed-tools-sdk-round81.md`, counted by `verifiers/check_sdk_allowed_tools.py --rev <rev>`.
```

## Landing order

1. Copy the entry to `corpus/knowledge/allowed-tools-sdk-round81.md` (conjunct (a)/(d) read it).
2. Land row S249 and the S248 `used-by` cell (census E11 resolves the entry; the entry must exist first — the r80 seat measured the ordering failure: 12 E11 lines with the targets absent).
3. Land the SKILL.md sentence + registry row, the README coverage row and the PROVINCE bullet (conjuncts (f)/(g)).
4. Land `verifiers/check_sdk_allowed_tools.py` with its registry row in the same commit (plan repair 6), pinned in `.ufo/waves/round-81/receipts/freeze-shas.txt` before any after-value is measured.
5. The snapshot `.ufo/waves/round-81/snapshots/S249.md`, `S249.fetch.json` and `S249.manifest` are already published by this seat; no copy step is needed for them.

## What the L1 must not do

Do not rewrite S248's other cells, including its `status` (`queued`), to make the entry look better; the plan freezes "no other cell changes" and the r81 counter's conjunct (e) reads only `used-by`. Do not add a `MANIFEST.sha256` to the r81 snapshots directory on this seat's account: this seat published a per-snapshot `S249.manifest` only, and a whole-directory manifest written now would go stale as sibling seats add snapshots.
