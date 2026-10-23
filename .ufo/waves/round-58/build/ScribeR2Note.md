Result: DONE — Drafted an append-only correction sentence and a Q29 registry row that detects the stale README claim in its own block.

## Drafts to deliver verbatim

Append this one sentence immediately after the existing round-57 Frontier note, before the blank line that starts `## Known gaps`; do not edit the old note:

> Round 58 correction: the plugin-manifest entry and `SKILL.md` § Plugin manifests by client draw on S079 (Claude Code manifest path and standard component inventory), S080 (Codex plugin manifest locations and package contents), S081 (VS Code manifest formats and capabilities), S082 (Copilot CLI manifest location, formats, and component types), S083 (Gemini CLI extension manifest and contents), S084 (Cursor plugin manifest paths and components), S085 (opencode plugin-manifest label, discovery locations, and registerable surfaces), and correction rows S086 (Codex plugin-creator scaffold contents, correcting S080), S087 (opencode plugin-discovery anchor and global location, correcting S085), and S088 (Cursor manifest schema, per-format component table, and component discovery locations) — the full source set is S079–S088.

Proposed Q29 registry row (same style as `verifiers/check_correction_sweep.py:31-80`):

```python
{"id": "r58-r2-readme-plugin-sources", "file": "corpus/README.md",
 "stale": r"the plugin half is recorded, not held as a verified claim",
 "declared": r"Round 58 correction:.*S079–S088", "lead": False},
```

## Findings and evidence

- The old note is `corpus/README.md:150-159`; it names only `S079–S085` at `:152` while describing the plugin entry and `SKILL.md` section. The correction sentence above adds, without changing that note, the correction rows S086–S088.
- The source roles are grounded in `corpus/SOURCES.md:92-101` and the gate ledger `corpus/lessons/round-57.md:16-25`: S079 Claude Code, S080 Codex, S081 VS Code, S082 Copilot CLI, S083 Gemini CLI, S084 Cursor, S085 opencode; S086 corrects S080's scaffold contents, S087 corrects S085's discovery-page anchor and records the global folder, and S088 documents Cursor manifest schema, component table and discovery locations. The entry's basis/roles are visible at `corpus/knowledge/plugin-manifests-round57.md:30-60`; the corresponding SKILL section is `SKILL.md:111-123`.
- The stale regex is the exact phrase at README line 151. `functions.grep` for `the plugin half is recorded, not held as a verified claim` returned a match at line 151 only; it is in the round-57 note's paragraph/block (lines 150-159). The declared regex is in the proposed sentence as written. Keep the sentence on one physical line and append it without an intervening blank line so both patterns remain in the same checker block.
- Checker behavior: `verifiers/check_correction_sweep.py:93-113` forms blocks at blank lines, list/table items and headings; `:116-130` searches the stale and declared regexes in each same block. The proposed stale text uniquely selects the old note's block in the current README, and the placement above puts the declaration in that same block. The row uses `lead: False`, matching the non-leading correction rows.

## Gates, surfaces, and limits

- No shell command, counter, verifier, self-test, or test was run; no execution pass is claimed. The only targeted search was the read-only `functions.grep` for the stale phrase, with the line-151 result described above; a second `functions.grep` for `S079–S088` found its existing uses at README lines 93-94. The checker behavior was read from source, not executed.
- Proposed touched surfaces for the integrator: append one sentence to `corpus/README.md` and add one row to `verifiers/check_correction_sweep.py`; the old note remains verbatim. No lane product files were changed by this seat.
- Out of scope: source re-fetch, counter or C1 claim judgment, checker execution, and editing either proposed product surface. The evidence here establishes citation roles and regex/block placement only; it does not establish runtime plugin behavior.
- Artifact: `.ufo/waves/round-58/build/ScribeR2Note.md`.
