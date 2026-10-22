# SrcCopilotSkills — round-50 build seat (C1 source: GitHub Docs agent skills)

**Result (one line): HOLDS-BOUNDED — the requested URL opens (301 → the current "Agent skills" concept page) and that page documents no
tie-break between two overlapping skills (ten-term sweep = 0 each); the description *role* is documented one hop away on GitHub's
add-skills how-to, and GitHub's only stated precedence rules are by **name** (first-found-wins, provider-over-file), never by description.**

## Answer to the question, plainly

**Does the page document a tie-break between two overlapping skills? No.**
- The requested URL `https://docs.github.com/en/copilot/concepts/agents/about-agent-skills` returns **HTTP 301** →
  `location: /en/copilot/concepts/customizations/agent-skills` (final 200). The page it now lives at states **no** description role, **no**
  length cap, and **no** arbitration rule: the ten-term sweep over its served markdown is **0 for every term** (`description` → 0) —
  the negative evidence (Q14) with the exact sweep command and counts below.
- The description role is documented on GitHub's *how-to* pages reached by ordinary navigation from the concept page: `description` = "A
  description of what the skill does, and when Copilot should use it" (add-skills.md:33) and "Copilot will decide when to use your skills based
  on your prompt and the skill's description" (add-skills.md:233).
- The only *deterministic* precedence GitHub documents for skills is **name-keyed, not description-keyed**: CLI plugin reference — "**Agents
  and skills** use first-found-wins precedence" (:415) and "Skills are deduplicated by their name field inside the `SKILL.md` file" (:417);
  Copilot SDK — "A provider skill with the same name as a file-based skill replaces the file-based skill" (skills.md:685) and, for conflicting
  skills, the documented remedy is **manual**: "Use `disabledSkills` to exclude conflicting skills" (:809), "Reorganize skill directories to
  avoid overlaps" (:810).
- Consequence for C1: the new row can honestly say GitHub documents *no* description-overlap tie-break, so the round-50 precedence ruling
  (routed defect D3) is a kotoba-local rule, **not** a vendor-documented one — it must not be cited as such.

## Fetch log (all opened 2026-10-22 UTC; ordinary means only: curl, no browser, no bot challenge; every curl exited 0)

| file | URL | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| gh-skills.html | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills (→ 301 → /en/copilot/concepts/customizations/agent-skills) | 2026-10-22T12:29:15Z | 200 final | 566002 | `c7b30290a4e6a1f16587829c631b35ed6a492ad0ab967563be7b4a59c72a22f6` |
| gh-skills.md | https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md | 2026-10-22T12:29:21Z | 200 (`text/markdown`) | 2622 | `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7` |
| gh-skills-orig.md | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills.md | 2026-10-22T12:29:21Z | **404** | 502 | `979615bad4719ae23bf76385ee60de8b1b05c785ce74497dee80ecb54c69c522` (the `.md` variant does **not** follow the 301) |
| gh-docs-src.md | https://raw.githubusercontent.com/github/docs/main/content/copilot/concepts/customizations/agent-skills.md | 2026-10-22T12:31:22Z | 200 | 3617 | `64d4d9c49638cd2a34b153920cf04bc72986ed5669e16df93b77c4921f35feae` |
| gh-add-skills.md | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills.md | 2026-10-22T12:30:10Z | 200 | 11790 | `18c361b5b6536f50947545be92f667864f7c83f7c532c553a70a0c1dc40815b7` |
| gh-sdk-skills.md | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills | 2026-10-22T12:31:51Z | 200 | 35455 | `64856ff44e5481f3ccb16defbc80180874e463862ac12309ef23b18802d4b9f3` |
| gh-cli-plugin-ref.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 2026-10-22T12:31:51Z | 200 | 47200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` |

Also opened, not proposed as rows (they restate A/B): `gh-cli-add-skills.md` (200, 10,057 B, sha256 `989af498…`, 2026-10-22T12:30:35Z) and
`gh-cheatsheet.md` (200, 10,699 B, sha256 `25f43326…`, 2026-10-22T12:30:43Z). Local copies of all nine files:
`/fast/scratch/hyaku/kotoba-r50/build/src-copilot-skills/`; `sha256sum` over them → exit 0.

**Provenance of the move (not an inference):** the authored source in `github/docs` carries `redirect_from: -
/copilot/concepts/agents/about-agent-skills` in its frontmatter, and the page's "Edit this page" target is
`github/docs/blob/main/content/copilot/concepts/customizations/agent-skills.md`. The served `.md` (2,622 B, frontmatter and Liquid variables
resolved) differs from the authored file (3,617 B, frontmatter + `{% data variables... %}` placeholders); the body prose is the same. The
GitHub Docs search endpoint was also opened ordinarily:
`https://docs.github.com/api/search?query=skill%20description%201024&client_name=copilot-docs-seat` → 200, 5,347 B (it found the SDK page);
the same endpoint without `client_name` → 400 (`Missing required parameter 'client_name'`).

## Sweep (Q14 negative evidence) — command and counts

```
for f in gh-skills.md gh-add-skills.md gh-cli-add-skills.md gh-cheatsheet.md gh-sdk-skills.md gh-cli-plugin-ref.md; do
  echo "=== $f ($(wc -c <$f) B) ==="
  for t in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do
    printf '  %-16s %s\n' "$t" "$(grep -ciE "$t" $f)"; done
  printf '  %-16s %s\n' '1,024' "$(grep -cE '1,024' $f)"; printf '  %-16s %s\n' 'description' "$(grep -ciE 'description' $f)"
done
```

| term | gh-skills.md (2622 B) | gh-add-skills.md (11790 B) | gh-cli-add-skills.md (10057 B) | gh-cheatsheet.md (10699 B) | gh-sdk-skills.md (35455 B) | gh-cli-plugin-ref.md (47200 B) |
|---|---|---|---|---|---|---|
| `overlap` | 0 | 0 | 0 | 0 | **1** | 0 |
| `ambigu` | 0 | 0 | 0 | 0 | 0 | 0 |
| `precedence` | 0 | 0 | 0 | 0 | 0 | **8** |
| `tie[- ]?break` | 0 | 0 | 0 | 0 | 0 | 0 |
| `conflict` | 0 | 0 | 0 | 0 | **3** | **1** |
| `multiple skills` | 0 | 0 | 0 | 0 | **1** | 0 |
| `same name` | 0 | 0 | 0 | 0 | **1** | **3** |
| `prioriti` | 0 | 0 | 0 | 0 | 0 | 0 |
| `1024` | 0 | 0 | 0 | 0 | 0 | **2** |
| `truncat` | 0 | 0 | 0 | 0 | 0 | 0 |
| `1,024` (added) | 0 | 0 | 0 | 0 | **1** | 0 |
| `description` (added) | **0** | 5 | 5 | 0 | 19 | 23 |

Two honesty notes on the sweep: (a) the requested `1024` pattern is blind to the comma-formatted `1,024`, which is why the extra `1,024` pattern
was added — the only description-length cap GitHub states (1,024 characters) is written with the comma; (b) the HTML route of the concept page
sweeps `conflict` → 2, but both hits are sidebar navigation links to "Policy conflicts"
(`/en/copilot/reference/enterprise-administrators/policy-conflicts`), not article prose — the `.md` route is the text of record.

## Located verbatim quotes (≤25 words each; location given)

- `gh-skills.md:7` (§ About agent skills): "Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant to improve its performance"
- `gh-skills.md:7`: "The Agent Skills specification is an [open standard](https://github.com/agentskills/agentskills), used by a range of different AI systems."
- `gh-skills.md:30-31` (§ Finding and storing skills): "Project skills, stored in your repository (`.github/skills`, `.claude/skills`, or `.agents/skills`)"
- `gh-add-skills.md:32` (frontmatter field list): "**name** (required): A unique identifier for the skill. This must be lowercase, using hyphens for spaces."
- `gh-add-skills.md:33` (frontmatter field list): "**description** (required): A description of what the skill does, and when Copilot should use it."
- `gh-add-skills.md:233` and `gh-cli-add-skills.md:121` (§ How Copilot uses agent skills): "When performing tasks, Copilot will decide when to use your skills based on your prompt and the skill's description."
- `gh-cheatsheet.md:31` (§ Usage comparison): "Automatic: chosen by Copilot when relevant to your prompt"
- `gh-sdk-skills.md:289` (§ SKILL.md format): "**`description`**: A short description of what the skill does."
- `gh-sdk-skills.md:662` (§ Provider limits and errors): "A catalog can contain at most 1,024 skills and 1 MiB of metadata. Each description and argument hint can be at most 1,024 characters."
- `gh-sdk-skills.md:685` (§ Provider lifecycle): "A provider skill with the same name as a file-based skill replaces the file-based skill, and `skills.reload` reports a warning."
- `gh-sdk-skills.md:807,809,810` (§ Troubleshooting → § Skill conflicts): "If multiple skills provide conflicting instructions:" / "Use `disabledSkills` to exclude conflicting skills" / "Reorganize skill directories to avoid overlaps"
- `gh-cli-plugin-ref.md:411,415,417` (§ Loading order and precedence): "**Agents and skills** use first-found-wins precedence." / "Skills are deduplicated by their name field inside the `SKILL.md` file."
- `gh-docs-src.md:11-12` (github/docs frontmatter): "redirect_from: - /copilot/concepts/agents/about-agent-skills"

## Proposed `corpus/SOURCES.md` rows (11-column shape; id placeholder `S0NN` — the L1 assigns the number)

Registry table shape: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`. Row A is the row the
assignment asks for; Rows B–D are the pages reached from it by ordinary navigation, each carrying distinct teaching. **All four are GitHub
Copilot vendor documentation, not a measurement of kotoba's substrate (omp / opencode)** — the `scope` cell says so, as rows S022/S023 do.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0NN (A — primary: the requested URL's current target) | GitHub Docs — Agent skills — https://docs.github.com/en/copilot/concepts/customizations/agent-skills | docs | A | GitHub Copilot's own concept page for agent skills: what a skill is, where it is stored, and which surfaces load it (vendor documentation for GitHub Copilot, not a measurement of omp or opencode) | § About agent skills (`agent-skills.md:7`); § Where you can use agent skills (`:13`); § Finding and storing skills (`:24`, `:30-31`); the requested route .../concepts/agents/about-agent-skills 301-redirects here (github/docs frontmatter `redirect_from:`), fetched as .../customizations/agent-skills.md (200, 2,622 B, sha256 `ed1e2944…`) on 2026-10-22T12:29:21Z; the HTML route (200, 566,002 B, sha256 `c7b30290…`) carries the same prose inside a client app shell | The page defines a skill as a folder Copilot loads when relevant, points at the open Agent Skills standard, and lists the storage locations; it says nothing about the `description` field, states no length cap, and documents no rule for choosing between skills whose descriptions both apply (sweep on the fetched markdown: `overlap`, `ambigu`, `precedence`, `tie[- ]?break`, `conflict`, `multiple skills`, `same name`, `prioriti`, `1024`, `truncat` → 0 each; `description` → 0) | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
| S0NN (B — the description role, one hop from A) | GitHub Docs — Adding agent skills for GitHub Copilot — https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills | docs | A | How GitHub Copilot decides that a skill applies, and what the page states about the `name` and `description` frontmatter fields (vendor documentation for GitHub Copilot, not a measurement of omp or opencode) | § Creating and adding a skill, frontmatter field list (`add-skills.md:32-33`); § How Copilot uses agent skills (`:233`); § Managing skills with GitHub CLI (`:213`, validation deferred to the Agent Skills specification); fetched as .../customize-cloud-agent/add-skills.md (200, 11,790 B, sha256 `18c361b5…`) on 2026-10-22T12:30:10Z | The `description` is the field Copilot matches the request against ("what the skill does, and when Copilot should use it") and `name` must be "A unique identifier for the skill"; the page states no character cap for the description and no arbitration rule for skills whose descriptions both apply (sweeps: the ten terms → 0 each; `description` → 5) | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
| S0NN (C — conflict handling and the one description cap GitHub states) | GitHub Docs — Custom skills (Copilot SDK) — https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills | docs | A | The Copilot SDK's documented skill contract: SKILL.md frontmatter fields, provider-served skill catalogs, and what the page says about skills that conflict (vendor documentation for GitHub Copilot, not a measurement of omp or opencode) | § SKILL.md format (`skills.md:289`); § Serving existing SKILL.md files (`:647`); § Provider limits and errors (`:662`); § Provider lifecycle (`:685`); § Troubleshooting → § Skill conflicts (`:805-810`); fetched as .../copilot-sdk/features/skills.md (200, 35,455 B, sha256 `64856ff4…`) on 2026-10-22T12:31:51Z | GitHub states a description cap only for provider-served catalogs (at most 1,024 characters per description and argument hint, at most 1,024 skills and 1 MiB of metadata per catalog); when skills conflict the documented remedy is manual — exclude one with `disabledSkills` or reorganize the directories — so no automatic tie-break between overlapping skills is documented (sweeps: `overlap` 1, `conflict` 3, `multiple skills` 1, `same name` 1, `1,024` 1, `1024` 0) | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |
| S0NN (D — the only stated precedence rule, name-keyed) | GitHub Docs — GitHub Copilot CLI plugin reference — https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference | docs | A | The precedence rules GitHub Copilot CLI states for duplicate component names, including skills, and the length caps it states for manifest descriptions (vendor documentation for GitHub Copilot CLI, not a measurement of omp or opencode) | § Loading order and precedence (`cli-plugin-reference.md:411-421`); § Optional metadata fields (`:195`); § Plugin entry fields (`:349`); fetched as .../copilot-cli-reference/cli-plugin-reference.md (200, 47,200 B, sha256 `d0d362cc…`) on 2026-10-22T12:31:51Z | Copilot CLI is the one GitHub surface that documents a deterministic tie-break, and it is keyed on the **name**, not the description: agents and skills use first-found-wins precedence, skills are deduplicated by the `name` field inside `SKILL.md`, and a plugin cannot override project-level or personal configurations; the page's 1,024-character cap is on plugin-manifest descriptions, not on the SKILL.md `description` | mined | 2026-10-22 | 90d | corpus/knowledge/sibling-overlap-census-round49.md |

## Lesson Gate lines (round-50 `corpus/lessons/round-50.md` § Gate — same 4-column shape as round-49)

| row | URL | accessed (UTC) | quote, at most 25 words (location) |
|---|---|---|---|
| S0NN (A) | https://docs.github.com/en/copilot/concepts/customizations/agent-skills | 2026-10-22T12:29:21Z | "Agent skills are folders of instructions, scripts, and resources that Copilot can load when relevant to improve its performance" (§ About agent skills, `agent-skills.md:7`) — no description role, no cap, no tie-break (ten-term sweep 0 each) |
| S0NN (B) | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills | 2026-10-22T12:30:10Z | "**description** (required): A description of what the skill does, and when Copilot should use it." (frontmatter field list, `add-skills.md:33`) |
| S0NN (C) | https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills | 2026-10-22T12:31:51Z | "A catalog can contain at most 1,024 skills and 1 MiB of metadata. Each description and argument hint can be at most 1,024 characters." (§ Provider limits and errors, `skills.md:662`) |
| S0NN (D) | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference | 2026-10-22T12:31:51Z | "**Agents and skills** use first-found-wins precedence." (§ Loading order and precedence, `cli-plugin-reference.md:415`) |

## Findings for the L1

1. **Adjacency (judged axis): high but bounded.** GitHub Copilot is a real client of the same open Agent Skills standard kotoba targets, and its
   pages are the closest vendor statement of "how a client presents skill descriptions": the description is the trigger field
   (`add-skills.md:33,233`). It does **not** license wording that a description "wins" a contest between siblings — every precedence GitHub
   states is name-keyed. Write the row as a *negative* source for the tie-break; the D3 ruling stays a kotoba-local rule and the census entry
   must not cite GitHub for a tie-break.
2. **Freshness (judged axis): high.** All four pages were fetched live on 2026-10-22T12:29Z–12:31Z; the concept page's repo source shows the
   redirect is intentional and current (`redirect_from:` in `github/docs` frontmatter).
3. **The concept page is thin for the claim**: it names no `description` field at all (`description` → 0 on the whole page). Row B carries C1's
   source requirement; Row A supports it with the canonical location and the negative sweep.
4. **Layering:** GitHub's pages defer the normative frontmatter rules to the open spec (add-skills.md:213 points at
   `agentskills.io/specification` for `gh skill publish --dry-run` validation), consistent with rows S018/S019/S022/S023. The 1,024-character
   cap in Row C is a *provider-catalog* limit, not a SKILL.md frontmatter rule; do not cite it as the spec's cap.
5. **Cap inventory from this round's fetch:** `1024` in Row D is the plugin-manifest `description`; `1,024` in Row C is the provider catalog.
   **No GitHub Docs page states a cap for the SKILL.md `description`** — the spec's own 1,024 cap (S018/S017) remains the only source for it.
6. **Opened but not proposed as rows** (restate A/B; hashes in the fetch log): the CLI add-skills how-to (`gh-cli-add-skills.md`) and the
   customization cheat sheet (`gh-cheatsheet.md`; its Agent-skills row gives trigger = "Automatic: chosen by Copilot when relevant to your
   prompt"). GitHub Docs search was used only to find the SDK page; the endpoint without `client_name` returns 400, recorded above.

## Gates run (this seat), bounds, out of scope

- All nine `curl -sS -L` fetches → exit 0 (status, bytes, sha256 in the fetch-log table); `sha256sum` over the nine files → exit 0; the
  ten-term `grep -ciE` sweep → exit 0 with the counts pasted above.
- Tooling: **no install or upgrade was needed** — `curl`, `grep`, `sha256sum`, `wc` are already on this host, so no pacman/uv/npm channel was
  used; nothing to record beyond "none".
- Lane mutation: none. Nothing under `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was edited except this report file; no git/jj write command
  ran in the lane, the fleet repo or any sibling lane. All fetches landed in `/fast/scratch/hyaku/kotoba-r50/build/src-copilot-skills/`.
- Out of scope (not this seat): editing `corpus/SOURCES.md`, `corpus/lessons/round-50.md`, `SKILL.md` or the census entry — the drafts above are
  for the L1 to integrate; the D3 precedence wording and the C1 description edit belong to other seats' files.
