Result: MIXED — S086's URL, byte count, sha256, anchors and every teaches-clause fact verify byte-exact against the live page, but the row's `mined`/`used-by` pair asserts a citation that no file in the candidate patch provides (verdict: admit with exact edits; two admissible variants below).

# Scope

Candidate row under test: `corpus/SOURCES.md` row `S086` in `.ufo/waves/round-57/a3/a2-candidate.patch:37` (the `+` line). The patch file is untrusted; every statement in the row was verified against live sources this seat. Source under test: https://developers.openai.com/plugins/build/plugins.md — the same URL S080 carries, so this is also a re-open of S080's source.

# Fetch evidence (this seat's opening, the admissibility opening)

```
$ date -u
Fri 23 Oct 2026 06:47:23 AM UTC
$ curl -sSL -o /tmp/s086-plugins.md -w 'HTTP %{http_code} %{size_download}B\n' 'https://developers.openai.com/plugins/build/plugins.md'
HTTP 200 38036B
$ wc -c /tmp/s086-plugins.md
38036 /tmp/s086-plugins.md
$ sha256sum /tmp/s086-plugins.md
c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1  /tmp/s086-plugins.md
```

Row claims `HTTP 200, 38,036 B, sha256 c37e330d…c4e1` — matches my fetch exactly (status, byte count, full sha256). The row's attributed timestamps (05:33:17Z RvS079S080; L1 re-open 05:44:34Z) are not independently verifiable by me; the byte identity is corroborated by my independent fetch. S080 (`/tmp` copy of `git show 07c33d73…:corpus/SOURCES.md`, line 93) carries the identical URL, byte count and sha256 — consistent.

# Fact-by-fact check against fetched bytes (/tmp/s086-plugins.md)

| Row claim | Fetched bytes | Verdict |
|---|---|---|
| § heading "Plugin creator output" at `plugins.md:59-89` | `:59` `### Plugin creator output`; section runs through `:89` (next content `:93`) | TRUE |
| "the contents at `:76-84`" | `:76-84` is the prose stating what is created vs empty; the scaffold tree itself is `:64-74`. The teaches facts are all stated at `:76-84` | TRUE (acceptable phrasing) |
| "the scaffold always creates only `.codex-plugin/plugin.json`" | `:76` `Only \`.codex-plugin/plugin.json\` is always created.` | TRUE, near-verbatim |
| "`.mcp.json` and `.app.json` start empty" | `:77-78` `.mcp.json starts with an empty \`mcpServers\` object, and .app.json starts with an empty \`apps\` object.` | TRUE |
| "a requested `hooks/` stays empty until `hooks/hooks.json` and its scripts are added" | `:82-84` `Requesting hooks creates an empty \`hooks/\` directory, not a hook configuration or executable script. Add \`hooks/hooks.json\` and its scripts…` | TRUE |
| teaches opens `supersedes S080 —` | required opener for a correction row, contract rule 2 (`CORPUS.md:117-118`) | TRUE |

## The S080-is-wrong claim

S086 quotes S080's teaches clause `"the compatibility scaffold also has optional app mappings, scripts, and hook files"` — byte-exact against S080 field 8 tail at `07c33d73…:corpus/SOURCES.md:93` (verified by splitting the row on `|`). Is S080 actually wrong? Page `:62` says the scaffold can create optional `.app.json`, `hooks/`, `scripts/` *when requested* — so "optional app mappings" and "scripts" are loose-but-defensible; "hook files" is contradicted by `:82-83` ("an empty `hooks/` directory, **not a hook configuration or executable script**"). The correction is justified and S086's teaches is the accurate statement.

# Column-shape check

Row as patched: `NF=13` on `|` split = 11 cells, matching header `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (`07c33d73…:corpus/SOURCES.md`, Registry header). `kind=docs`, `tier=A`, `status=mined`, `opened=2026-10-23`, `recheck=90d` — all enum-valid per contract v1 (`CORPUS.md:86-108`) and the census awk at `CORPUS.md:145`. `id` = S086, the next unused (tip max = S085), never reused. No `|` inside any cell. `source` cell follows the house `title — URL` pattern; the `(correction row: …)` parenthetical inside the title is novel but harmless.

# Findings

**F1 — `mined`/`used-by` dishonest under the candidate (the one real defect).** `used-by` = `corpus/knowledge/plugin-manifests-round57.md`, and `status` = `mined` requires "cited by ≥1 path in `used-by`" (`CORPUS.md:103-104`). Grep of the whole patch: `S086` occurs only at `:10` (SKILL.md basis text `(S079–S088; S086 and S087 correct S080 and S085)`) and `:37` (the row itself); the knowledge-file diff cites S028/S079–S085/S087/S088 but **never S086** (Codex "What a plugin can ship" row, patch `:98`, still cites only `S080 \`build-plugins.md:14-30,52-89\``). SKILL.md is neither a knowledge entry nor a lesson, so it is not a `used-by` path either. As patched, the row claims a citation that does not exist.

**F2 — integration gap, not a row defect: no lesson Gate line for S086.** Contract rule 1 (`CORPUS.md:112-115`) requires the round lesson's `## Gate` to record URL, access date and a ≤25-word quote per new row. Tip lesson `corpus/lessons/round-57.md` Gate has S079–S085 only; the candidate patch touches no lesson file. Same gap applies to S087/S088 — flagging for the S086 fix. Suggested quote for a Gate line, byte-exact at `plugins.md:76` (ends mid-line before " The other"): `"Only \`.codex-plugin/plugin.json\` is always created."` (7 words).

**F3 — counter safety: S086 is not a counted row.** `verifiers/check_plugin_manifests.py` counts only knowledge-entry rows; S086 is cited by none, so its extra-row presence does not change F or G, and its URL duplicating S080's cannot trip the base-URL rejection (S080 is new this round, not a base row). Its `mined` status is also unconstrained by the counter — the defect is purely contract honesty.

**F4 — residual inconsistency in the companion file (outside the row).** The candidate's knowledge file keeps the Codex ship-cell claim "(the scaffold writes `.mcp.json`)" while S086's correction says it is written only when requested (`plugins.md:77` "starts with an empty `mcpServers` object… The manifest references these files when requested"). If S086 is admitted, that cell should cite it.

# Verdict: admit with exact edits

Every factual claim in the row verifies byte-exact; the defect is the `mined`/`used-by` pair. Two admissible variants — the L1 picks one; both keep the row's verified cells unchanged.

## Variant A (recommended): keep `mined`, make `used-by` true outside the row

Row edits: append this seat's re-open evidence to the anchor cell. Exact old→new:

- anchor cell tail `(residual seat RvS079S080; re-opened by the L1 05:44:34Z, same sha256)` → `(residual seat RvS079S080; re-opened by the L1 05:44:34Z, same sha256; re-opened by falsify seat A3CandS086 2026-10-23T06:47:23Z, HTTP 200, same bytes)`

Required companion edits (outside the row, so `mined`/`used-by` becomes true):

- `corpus/knowledge/plugin-manifests-round57.md` Codex ship-row source-lines cell `S080 \`build-plugins.md:14-30,52-89\`` → `S080 \`build-plugins.md:14-30,52-89\`; S086 \`plugins.md:59-89\``, and tighten "(the scaffold writes `.mcp.json`)" → "(the scaffold writes `.mcp.json` only when requested)".
- `corpus/lessons/round-57.md` Gate: add the S086 line (URL above, `2026-10-23T05:33:17Z`, `38,036 B, sha256 c37e330d…`, quote per F2, location `plugins.md:76`).

## Variant B (row-only fix): demote the status pair

Corrected row in full (old `| mined | 2026-10-23 | 90d | corpus/knowledge/plugin-manifests-round57.md |` → `| queued | 2026-10-23 | 90d | — |`, plus the same evidence-note append):

```
| S086 | OpenAI Developers — Package your plugin (correction row: scaffold contents) — https://developers.openai.com/plugins/build/plugins.md | docs | A | Codex plugin-creator scaffold contents as the page states them (vendor documentation; not runtime behavior) | § Plugin creator output (`plugins.md:59-89`, the contents at `:76-84`); fetched 2026-10-23T05:33:17Z, HTTP 200, 38,036 B, sha256 `c37e330df8f040df8ee2f48035992b37c6a7decf6c3f5640822ca0907118c4e1` (residual seat RvS079S080; re-opened by the L1 05:44:34Z, same sha256; re-opened by falsify seat A3CandS086 2026-10-23T06:47:23Z, HTTP 200, same bytes) | supersedes S080 — its teaches clause "the compatibility scaffold also has optional app mappings, scripts, and hook files" is wrong: the scaffold always creates only `.codex-plugin/plugin.json`; `.mcp.json` and `.app.json` start empty and a requested `hooks/` stays empty until `hooks/hooks.json` and its scripts are added | queued | 2026-10-23 | 90d | — |
```

Variant B leaves the F4 inconsistency standing and weakens the corpus (a verified correction uncited); Variant A is preferred because the knowledge entry genuinely should cite the correction. If the L1 integrates Variant A without the evidence-note append, the row is admissible **as written**.

# Verification gaps / residual risk

- The attributed 05:33:17Z/05:44:34Z openings are claims of the untrusted patch; byte identity is corroborated by my fetch, the timestamps are not.
- S080's teaches being "wrong" is a judgment: the hooks part is flatly contradicted (`:82-83`); the "scripts"/"app mappings" parts are loose rather than false. The supersession stands on the hooks point.
- The page may drift: `opened`/`recheck 90d` handles that; my fetch is the third recorded identical-byte opening today.
- No tools installed; nothing outside this report file was written.

Report: .ufo/waves/round-57/a3/falsify/A3CandS086.md
