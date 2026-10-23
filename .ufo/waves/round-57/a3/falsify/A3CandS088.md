Result: MIXED — S088's fetch metadata is byte-exact, its column shape and every teaches clause are grounded in the live page except one ambiguous connective: admit with the exact edit below (`or` → `and no`), not as written.

# Scope
Verify the untrusted candidate SOURCES row S088 (Cursor plugins reference) in
`.ufo/waves/round-57/a3/a2-candidate.patch:39`. The row text (verbatim, from the patch):

```
| S088 | Cursor Docs — Plugins reference — https://cursor.com/docs/reference/plugins.md | docs | A | Cursor's plugin manifest schema, per-format component table and component discovery locations (vendor documentation; not runtime behavior) | § Formats (`reference-plugins.md:9-15`); § Cursor Plugin component discovery (`:152-165`); § Rule frontmatter fields (`:184-193`); fetched 2026-10-23T05:33:49Z, HTTP 200, 30,324 B, sha256 `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204` (residual seat RvS083S084; re-opened by the L1 05:47:52Z, same sha256) | When the manifest names no path, Cursor discovers components by folder: `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json` and `mcp.json`, and a root `SKILL.md` is read as a single-skill plugin when there is no `skills/` folder or manifest `skills` field | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

# Fetch evidence (this seat's opening — the admissibility opening for the row)

- Command: `curl -sS -o s088-plugins-ref.md -w 'HTTP %{http_code} | %{size_download} bytes\n' 'https://cursor.com/docs/reference/plugins.md'`
- `date -u` at fetch: `Fri 23 Oct 2026 06:46:23 AM UTC` (second sample `Fri 23 Oct 2026 06:48:36 AM UTC`)
- Observed: `HTTP 200 | 30324 bytes`; `sha256 3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204`; 529 lines.
- Bytes retained at `/fast/scratch/hyaku/kotoba-r57a3/A3CandS088/reference-plugins.md` (sha256 re-verified after move).
- **Byte-identical to the candidate's recorded evidence** (200, 30,324 B, same sha256). The row's fetch metadata is verified.

# Claim-by-claim check (line numbers in my fetched bytes)

| # | Row claim | Evidence | Result |
|---|---|---|---|
| 1 | Anchor `§ Formats (reference-plugins.md:9-15)` | `:7` heading is `## Supported plugin formats`; `:9` "Cursor loads plugins in two formats, identified by their manifest location:"; `:11-15` the two-row format table: Agent Plugins → "`plugin.json` at the plugin root" / "Skills, MCP servers"; Cursor Plugins → "`.cursor-plugin/plugin.json`" / "Skills, MCP servers, rules, agents, commands, hooks, variables" | TRUE — cite lands on the right block; note the heading is `Supported plugin formats`, not `Formats` (approximate heading label; anchor filename `reference-plugins.md` is the lane's basename-disambiguation convention, matching siblings `build-plugins.md`, `agent-plugin-reference.md`, `plugins-creating.md` — S084's `plugins.md` would otherwise collide). |
| 2 | Anchor `§ Cursor Plugin component discovery (:152-165)` | `:152` exact heading `## Cursor Plugin component discovery`; `:154` "When the manifest does not specify explicit paths for a component type, the parser uses **automatic folder-based discovery**:"; `:156-164` the component table | TRUE, heading and range exact. |
| 3 | Anchor `§ Rule frontmatter fields (:184-193)` | `:184` exact heading `### Rule frontmatter fields`; `:186-190` fields `description`, `alwaysApply`, `globs`; `:192` link to Rules page | TRUE, exact. |
| 4 | teaches: "When the manifest names no path, Cursor discovers components by folder" | `:154` (above) + `:166` "If a manifest field **is** specified (e.g., `"skills": "./my-skills/"`), it **replaces** folder discovery for that component. The default folder is not also scanned." | TRUE — including the implicit converse: a specified path replaces, never supplements, folder discovery. |
| 5 | teaches: folder list `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json`, `mcp.json` | `:158` Skills→`skills/`; `:159` Rules→`rules/`; `:160` Agents→`agents/`; `:161` Commands→`commands/`; `:162` Hooks→`hooks/hooks.json`; `:163` MCP Servers→`mcp.json` | TRUE — six defaults, order and spelling exact. (Nit: the row calls the set "folder" discovery while two entries are files; the source itself names the mechanism "automatic folder-based discovery" (:154), so the wording tracks the vendor's own term.) |
| 6 | teaches: "a root `SKILL.md` is read as a single-skill plugin" | `:164` "| Root Skill  | `SKILL.md` at plugin root | Treated as a single-skill plugin ... |" | TRUE. |
| 7 | teaches: condition "when there is no `skills/` folder **or** manifest `skills` field" | `:164` (cont.): "(only if no `skills/` dir **and** no manifest `skills` field)" | **DEFECT — ambiguous connective.** The source states a conjunction: BOTH absent. The row's "no `skills/` folder **or** manifest `skills` field" parses two ways: the charitable "neither folder nor field" (correct), and the literal "no folder, OR a `skills` field [exists]" — under which a plugin whose manifest names `skills` would still have its root `SKILL.md` read, directly contradicting `:166` (a specified `skills` field replaces discovery). One-word fix removes the false parse. |

Additional checks:

- Manifest schema exists on the page as the row's scope claims: `## Cursor Plugin manifest` `:63-95` (required `name` `:70-74`; optional fields incl. `rules`/`agents`/`skills`/`commands`/`hooks`/`mcpServers`/`variables` `:76-94`; example `:96-110`). The scope phrase "manifest schema" is accurate, though the anchor does not cite this block — optional anchor addition below.
- No conflict elsewhere: `:467` repeats "Component discovery runs within the `my-plugin/` directory, using manifest paths if specified or folder-based discovery as fallback"; `:512`/`:520` consistent.
- `~/.cursor/plugins/local` does **not** appear on this page (`grep -n 'plugins/local'`: no match) — the local-development claim in the candidate's SKILL.md Cursor cell and knowledge paragraph is S084's (`plugins.md:211`) evidence, not S088's; no bearing on this row, flagged only so nobody grounds that phrase on S088.
- The candidate's SKILL.md Cursor cell also says "a root `SKILL.md` alone is a single-skill plugin" (patch :24), eliding the `:164` conditions. The knowledge-entry row (patch :106) keeps the conditions. Out of my row's scope; noted for whoever reviews the SKILL.md cell.

# Column shape vs 11-column header at 07c33d73

Header (tip `corpus/SOURCES.md`): `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` — 11 columns.
`awk -F'|'` on the candidate's S088 line: **NF=13 = conformant** (the same grep also matched two prose mentions of "S088" at patch lines 10 and 106 with NF 1 and 5 — those are not table rows). No `|` inside any cell: the sha256, timestamps and backtick spans contain none. Cell order matches the header positionally: id `S088` (unused at tip — highest committed id is `S085`, via `git show <tip>:corpus/SOURCES.md | grep -oE 'S[0-9]{3}' | sort -u | tail`); kind `docs` ∈ enum; tier `A` appropriate (vendor reference doc for its own product); status `mined` — internally consistent since the same patch rewrites `corpus/knowledge/plugin-manifests-round57.md` to cite `S088` at patch line 106; opened `2026-10-23` ISO; recheck `90d` ∈ cadence form; used-by `corpus/knowledge/plugin-manifests-round57.md` — path exists at tip (`git cat-file -e` → 0).

# Contract v1 check (fleet CORPUS.md §SOURCES.md)

- Rule 1 (row is a claim, opened this round): **satisfied by my opening** — this fetch is the required opening; bytes and sha256 recorded above.
- Rule 2 (append-only): S088 is a new row, not a rewrite; teaches does not need the `supersedes S0NN` opener.
- Shape table: all enum fields conform; no `|` inside cells; `id` not reused.
- Rule 6: no credential material.
- Anchor carries revision per contract ("exact section … plus revision"): the fetch tuple (timestamp, status, bytes, sha256) is the revision pin; the provenance clause "(residual seat RvS083S084; re-opened by the L1 05:47:52Z, same sha256)" names unverifiable-to-me attempt-2 history — [INFERENCE] their identities, but the sha256 they claim is now proven correct by my fetch.
- Gate requirement (round lesson records URL, access date, ≤25-word quote for `teaches`): a quote for the lesson's `## Gate` — from `:164`, 13 words, contiguous substring: "Treated as a single-skill plugin (only if no skills/ dir and" — alternatively `:154`, 14 words: "the parser uses automatic folder-based discovery" would need shaping; prefer the `:164` fragment or this contiguous one from `:154`: "When the manifest does not specify explicit paths for a" (13 words). The lesson-gate bookkeeping itself is the lesson seat's item.

# Findings

**F1 (must-fix, one word):** teaches condition `or` → `and no`. As written the row admits a false reading (`SKILL.md` read when the manifest DOES name `skills`, contradicted by `:166`). Old→new inside the teaches cell:

- old: `a root \`SKILL.md\` is read as a single-skill plugin when there is no \`skills/\` folder or manifest \`skills\` field`
- new: `a root \`SKILL.md\` is read as a single-skill plugin when there is no \`skills/\` folder and no manifest \`skills\` field`

**F2 (optional, scope↔anchor gap):** scope claims "plugin manifest schema" but no anchor cites it. Optional addition: `§ Cursor Plugin manifest (\`:63-95\`)` after the `§ Formats` anchor.

**F3 (optional provenance):** my re-open can be recorded in the anchor parenthetical: `falsify re-open 2026-10-23T06:46Z, same sha256, seat A3CandS088`.

**Nits (no edit required):** approximate heading label `§ Formats` for `## Supported plugin formats`; "folder" discovery wording follows the vendor's own term for a list containing two file paths.

# Verdict

**Admit with exact edits** — required: F1. Recommended (admissible without): F2, F3. Corrected row in full:

```
| S088 | Cursor Docs — Plugins reference — https://cursor.com/docs/reference/plugins.md | docs | A | Cursor's plugin manifest schema, per-format component table and component discovery locations (vendor documentation; not runtime behavior) | § Formats (`reference-plugins.md:9-15`); § Cursor Plugin manifest (`:63-95`); § Cursor Plugin component discovery (`:152-165`); § Rule frontmatter fields (`:184-193`); fetched 2026-10-23T05:33:49Z, HTTP 200, 30,324 B, sha256 `3bbf36f3320382adb68509aa758e2e764fd31c5de5f5c70c6af1683497b11204` (residual seat RvS083S084; re-opened by the L1 05:47:52Z, same sha256; falsify re-open 2026-10-23T06:46Z, same sha256, seat A3CandS088) | When the manifest names no path, Cursor discovers components by folder: `skills/`, `rules/`, `agents/`, `commands/`, `hooks/hooks.json` and `mcp.json`, and a root `SKILL.md` is read as a single-skill plugin when there is no `skills/` folder and no manifest `skills` field | mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |
```

If the L1 takes only the required fix and drops F2/F3, the row is still fully admissible — the teaches cell alone must carry `and no`.
