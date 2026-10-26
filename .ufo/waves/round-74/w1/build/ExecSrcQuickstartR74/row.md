# Registry row draft — quickstart page (C1, round 74 wave 1)

Lane schema: 11 columns (`id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by`),
no `|` inside any cell. `id` is the placeholder `S<next>`: the lane's highest id at base is `S222`
(`grep -oE '^\| S[0-9]{3,} ' corpus/SOURCES.md | tr -d '| ' | sort -u | tail -3` → S220, S221, S222), so the
next free lane id is `S223`; the staged package also uses `S223` (Chiba Prefecture) and every id up to `S390`,
so the package side must be renumbered at import and the lane id never follows the package's numbering.

Row (copy verbatim into `corpus/SOURCES.md` after the last data row, once the L1 fixes the id):

| S<next> | Agent Skills — Quickstart: Create your first Agent Skill — https://agentskills.io/skill-creation/quickstart.md | docs | A | the page's own first-skill tutorial, scoped to the guidance its own lines state — where a VS Code project keeps a skill, what the minimal folder holds, and how the tutorial verifies discovery; it is not the format rules (those stay S001) and it states no client-neutral discovery root | "## Create the skill" and "## How it works"; upstream `agentskills/agentskills@69ef37e9424c0a7ea9dd2293b559e43ec8176379` `docs/skill-creation/quickstart.mdx` (repo head on 2026-10-25 by `git ls-remote`, path unchanged since `8aeff47` 2026-04-19); fetched as `.md` HTTP 200, 4 080 B, sha256 `7c480b447edac58fd8ff8f250c471dfc7d4621155b91fabed46379075c32bffb`, on 2026-10-25; quote "VS Code looks for skills in `.agents/skills/` by default." | a first skill is one folder holding one `SKILL.md` at the project's `.agents/skills/` root, its `name` equal to the folder, its `description` naming the when, confirmed by `/skills` and one natural prompt | queued | 2026-10-25 | 90d — re-fetch the `.md` and confirm the `.agents/skills/` default, the portability sentence and the worked description are unchanged (ran 2026-10-25) | corpus/knowledge/spec-skill-creation-craft-round74.md |

## Landing notes for the L1 (not part of the row)

1. **`status` conflict, must be decided before data.** This draft carries `queued` as the seat instruction
   directs, but plan § C1 predicate (b) requires `status `mined`` for the page's `S###` to count. If the row
   lands as `queued`, `check_spec_craft.py` rejects `quickstart` by construction. Either the row lands
   `mined` (the r73 precedent: S213, opened 2026-10-25, is `mined` with an entry) or the predicate's (b) is
   amended in a committed addendum before any seat scores data (Q28). This report does not choose.
2. **Snapshot location.** The C1 predicate (c) reads `.ufo/waves/round-74/snapshots/<P>.<ext>` against
   `snapshots/MANIFEST.sha256`; this seat wrote `snapshot.md` / `snapshot.sha256` under
   `.ufo/waves/round-74/w1/build/ExecSrcQuickstartR74/` as its instructions direct. Copy the same bytes to
   the snapshots path and add the manifest pin (sha256 `7c480b44…c32bffb`, 4 080 B) — do not re-fetch and
   do not reshape the text, or predicate (d)'s whitespace-collapsed quote location changes.
3. **Row cell checks.** 11 cells; no `|` in any cell; the anchor quote is 9 words (predicate (d) window
   5–25); the tier-A scope is deliberately narrower than the staged S237's ("where a compliant client looks
   for skills"), which this page does not state.
