# Round-51 seat report — SrcClaudeCode (C2 frontier source, client: Claude Code)

**HOLDS — the Claude Code skills page documents levers other than the description that remove one
of two overlapping skills from the model's choice, best `disable-model-invocation: true`
(frontmatter), which "removes the skill from Claude's context entirely" (`skills.md:886`) — a
removal lever, not a documented tie-break (the page states no rule choosing between two matching
descriptions).**

C2's Claude Code row is backed by S022's page (https://code.claude.com/docs/en/skills), opened by
ordinary means (curl), `.md` variant. The fetched bytes are byte-identical to the round-48/50 fetch
recorded in S022 (sha256 `cdfcb0df…` matches; 111,557 B). Lane base
`43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`; lane checkout was read-only — only this report was
written there. Artifacts in `/fast/scratch/hyaku/kotoba-r51/build/SrcClaudeCode/`.

## Fetch record

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://code.claude.com/docs/en/skills.md | 2026-10-22T14:19:03Z | 200 | 111,557 | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |
| same route, second fetch with UA | 2026-10-22T14:32:16Z | 200 | 111,557 | `cdfcb0df…` (`cmp` exit 0, byte-identical) |
| https://code.claude.com/docs/en/skills (HTML) | 2026-10-22T14:32:17Z | 200 | 1,233,129 | `102195341251387cee65e8d8f47809878c3c118a12f53fff64bea966a6c42ee2` |

The **`.md` variant** was used (content-type `text/markdown; charset=utf-8`, 1,234 lines). The bytes
are byte-identical to the round-48/50 fetch in S022 — **the page has not changed since round 48**;
the `last-modified` header equals the fetch time (dynamic) so content hash is the freshness signal.

## Findings

**F1 — The best lever: `disable-model-invocation: true` (frontmatter field).** Set in the skill's
own `SKILL.md` YAML frontmatter; the page says it "removes the skill from Claude's context entirely"
(`skills.md:886`) and the model-side effect is "Description not in context" (`:577`), so the model
never sees the description and cannot choose the skill; the user can still invoke it manually with
`/name` (`:393`, `:577`). The page's own troubleshooting remedy for a skill firing too often pairs
description specificity with this lever (`:1194-1195`).

**F2 — Other documented levers (each with key term, what it does, where set, located quote).**
- `user-invocable: false` (frontmatter) — hides the skill from the `/` menu while Claude may still
  load it; the opposite direction from F1, so it does not stop model choice (`:394`, `:551`,
  `:578`, NOTE `:890`).
- `skillOverrides` setting, values `"off"` / `"user-invocable-only"` / `"name-only"` (settings
  file: `settings.json`, `settings.local.json`, managed settings) — `"off"` hides the skill from
  Claude's listing and the `/` menu; `"user-invocable-only"` hides it from Claude's listing but
  keeps it in `/` (`:894`, `:898-903`, `:907`, `:323`).
- Permission deny rules `Skill(name)` / `Skill(name *)` — deny the Skill tool for a named skill, or
  all skills (`:848-866`).
- `disableBundledSkills` (settings) — turns off the bundled skills set entirely (`:29`, `:321`).
- `paths` globs (frontmatter) — scope automatic activation to matching files (`:403`); a gating
  lever, not a removal from the listing.
- Remove a skill — delete its directory, or disable/remove the providing plugin (`:313-323`).

**F3 — No tie-break between two matching skills.** Sweeps over the fetched bytes: `overlap` 0,
`ambigu` 0, `arbitrat` 0, `tie[- ]?break` 0, `both match` 0, `multiple skills` 0, `prioriti` 0;
`conflict` 1 (`:49`, `/doctor prompt-audit`), `precedence` 1 (`:920`, a `skillOverrides` alias
rule), `hidden` 3 (`:902`, `:903`, `:907` — `skillOverrides` states), `same name` 2 (`:200`,
`:278`). The page's only "which one wins" rules are same-name collisions settled by origin
(`:196-208`) and explicitly stacked skills (`:682`); neither arbitrates two matching descriptions.
Per the round's bound: a disable/deny lever removes a skill from choice; it is not a documented
tie-break.

**F4 — D3 input.** `SKILL.md:375-377` currently says the documented remedy for overlap is "a more
specific description"; for Claude Code the page itself documents `disable-model-invocation: true`
as a second remedy on the same troubleshooting list (`skills.md:1195`), so the D3 rewrite should
name the lever alongside specificity.

**F5 — Counter-shape change flagged.** The lever counter `verifiers/check_overlap_levers.py` was
rebuilt mid-round by the LeverGuard seat to a 6-column SKILL.md header (`client | lever | held by |
effect | row | key term`) and additional checks (source URL vendor prefix, kind/tier, `reviewed`
lever list, code-span-in-quote, quote ≤25 words, row id in the round-51 lesson `## Gate`, duplicate
source-row). Deliverables below use that current shape; the 4-column shape in the task prompt no
longer parses.

## Deliverable (a) — `SKILL.md` § Anti-patterns, "Overlap levers by client" table row

```markdown
| Claude Code | frontmatter flag that removes the skill from Claude's context entirely, so the model can no longer choose it and only a manual slash command reaches it | skill author | automatic choice off | S022 | `disable-model-invocation` |
```

## Deliverable (b) — `corpus/knowledge/skill-overlap-levers-round51.md`, entry table row

```markdown
| Claude Code | S022 | frontmatter `disable-model-invocation: true` removes the skill from Claude's context entirely, so the model can no longer choose it | "`disable-model-invocation` \| No \| Set to `true` to prevent Claude from automatically loading this skill." (skills.md:393) |
```

Quote = 15 words, verbatim prefix of `skills.md:393`, contains the key term `disable-model-invocation`
verbatim and as an exact backticked code span; pipe-escaped (`\|`) so the entry table cell parses.
Verified `BACKED Claude Code` and `FETCH Claude Code: quote found` against the live page (the `.md`
sibling of the source URL).

## Deliverable (c) — `corpus/SOURCES.md` row S022 (no new id; the row exists, is `mined`, and
covers this page). Exact old -> new cell text (the applied row is in `patch.diff`):

- **scope** old: `How Claude Code decides which of several available skills to use (the \`description\`'s role), how its skill listing is truncated and budgeted, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode)` → new: `How Claude Code decides which of several available skills to use (the \`description\`'s role), how its skill listing is truncated and budgeted, which documented levers remove one of two overlapping skills from the model's choice, and what the page says about skills that collide (vendor documentation, not a measurement of omp or opencode)`
- **anchor** old: `§ Frontmatter reference, \`description\` row (\`skills.md:389\`) and \`when_to_use\` row (\`:390\`); § Create your first skill (\`skills.md:114\`); § Resolve skills that share a name (\`skills.md:196-208\`); § Stack several skills in one message (\`skills.md:682\`); § Troubleshooting → § Skill triggers too often (\`skills.md:1190-1195\`) and § Skill descriptions are cut short (\`skills.md:1205-1213\`); fetched as https://code.claude.com/docs/en/skills.md (200, 111557 B, sha256 \`cdfcb0df…\`) on 2026-10-22T09:41:02Z and re-opened 2026-10-22T12:28:45Z byte-identical to those bytes and to the round-48 fetch of the same route; the HTML route (200, 1233129 B, sha256 \`10219534…\`) serves the same prose, did not redirect, and re-fetched byte-identical` → new: same text plus `; the lever sections — § Control who invokes a skill (\`skills.md:545-583\`, \`disable-model-invocation\` at \`:549\`, \`user-invocable\` at \`:551\`, the invocation table at \`:572-578\`); § Restrict Claude's skill access (\`skills.md:842-890\`, deny syntax at \`:848-866\`, hide-one-skill rule at \`:886\`); § Override skill visibility from settings (\`skills.md:892-925\`, the \`skillOverrides\` states table at \`:898-903\`); § Remove a skill (\`skills.md:313-323\`); § Bundled skills (\`skills.md:21-35\`, \`disableBundledSkills\` at \`:29\`); § Frontmatter reference \`paths\` row (\`skills.md:403\`); re-opened 2026-10-22T14:19:03Z and 14:32:16Z byte-identical`
- **teaches** old → new: retained in full, with this sentence appended: `; and the page's own documented levers that take one of two overlapping skills out of the model's choice are frontmatter \`disable-model-invocation: true\` ("This removes the skill from Claude's context entirely", \`skills.md:886\`, frontmatter row \`:393\`), frontmatter \`user-invocable: false\` (the opposite direction — hides from the `/` menu while Claude may still load it, \`:394\`, \`:551\`, \`:578\`), the \`skillOverrides\` setting's \`"off"\` and \`"user-invocable-only"\` states (hidden from Claude's listing, \`:898-903\`), permission deny rules \`Skill(name)\` / \`Skill(name *)\` (\`:866\`), the \`disableBundledSkills\` setting (\`:29\`), and the \`paths\` glob row (\`:403\`) — each removes or gates a skill from the choice; none is a documented tie-break between two matching descriptions`
- **used-by** old: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md` → new: `corpus/knowledge/sibling-overlap-census-round49.md, corpus/lessons/round-50.md, corpus/knowledge/skill-selection-rules-round50.md, corpus/knowledge/skill-overlap-levers-round51.md`

Status stays `mined`; opened `2026-10-22`; recheck `90d`. The row must land together with the
entry file (E11 otherwise). CORPUS.md rule 2 permits `use-by` in place; the scope/anchor/teaches
head is the round's requested form and matches round-50's in-place S022 precedent (logged in the
round-50 lesson § Gate).

## Evidence (commands, exit codes, paths)

- Fetch: `curl -sSL -w 'status=%{http_code} size=%{size_download}' -o skills.md https://code.claude.com/docs/en/skills.md` → `status=200 size=111557`; `sha256sum skills.md` → `cdfcb0df930…`; second fetch `cmp skills.md skills-2.md` → exit 0; `sha256sum skills-2.md` → identical. HTML: `curl -sSL -o skills.html https://code.claude.com/docs/en/skills` → `status=200 size=1233129`, sha256 `10219534…`; third/fourth HTML fetches `cmp` → exit 0.
- Quote verification: every quote located with `grep -nF` against the fetched bytes; word counts 8-18 (all ≤ 25). Key quote `skills.md:393` prefix and `skills.md:886` sentence found verbatim.
- Counter (current shape, from the lane working tree): `python3 -B verifiers/check_overlap_levers.py --root /fast/scratch/hyaku/kotoba-r51/build/SrcClaudeCode/world` → `BACKED Claude Code`, `overlap levers backed 1 of 7 clients`, `EXIT=1` (the other six clients are other seats' rows); with `--fetch` → `FETCH Claude Code: quote found (https://code.claude.com/docs/en/skills)`, `quotes found on live pages 1 of 1`.
- Census on the edited clone: `bash scripts/sources-census.sh validate /fast/scratch/.../SrcClaudeCode/censustree/kotoba-shokunin` → `ok`, same three pre-existing W04, `EXIT=0`; malformed-row awk → `0`. Without the entry file → `E11 S022 missing used-by corpus/knowledge/skill-overlap-levers-round51.md`, exit 1. Superseding-row mutant (same URL+scope, `supersedes S022 —`) → `ok` exit 0, no new W04.
- Self-test of the counter: `python3 -B verifiers/check_overlap_levers.py --self-test` (LeverGuard seat's build) — not rerun here; the counter's own report records 22/22.

## Out of scope

- Editing `corpus/SOURCES.md`, `SKILL.md`, `corpus/knowledge/skill-overlap-levers-round51.md`, or
  `corpus/lessons/round-51.md` in the lane: drafts only (read-only lane bound; the L1 integrates).
- The other six clients' rows in the SKILL.md/entry tables, `SKILL.md:375-377` (D3), the lesson §
  Gate record (the counter requires S022 there; I provide the exact Gate line text), and the
  S030 id collision between the SrcOpencode and SrcCopilotSdk drafts (both claim S030; registry max
  is S029; the L1 must de-duplicate).

## Artifacts

- `/fast/scratch/hyaku/kotoba-r51/build/SrcClaudeCode/skills.md` (+ `skills-2.md`, `skills.html`,
  `h1-3.html`, `md-ua.txt`, `headers-md.txt`, `headers-html.txt`) — fetched bytes; `old_*.txt` —
  exact pre-edit S022 cells; `skill_row.md`, `entry_row.md`, `lesson_gate_line.md` — drafted rows
  and Gate line; `lane/`, `final/`, `world/`, `mut/`, `censustree/` — private clones/worlds at
  `43ca0bfb` with the edits applied (world = validated `BACKED` fixture).
- `/fast/scratch/hyaku/kotoba-r51/build/SrcClaudeCode/patch.diff` — unified diff of the S022 row
  edit against `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10` (13 lines). `patch_full.diff` — same
  plus the shared draft files (SKILL.md row, entry stub, lesson stub) for reference; the L1 merges
  the seven clients' rows into the shared files, so only `patch.diff` is the scoped change.

## Tooling

None installed or upgraded this session; `curl`, `git`, `grep`, `awk`, `cmp`, `sha256sum`, `wc`,
`date`, `python3` and the fleet's `scripts/sources-census.sh` were present. No `pacman`, `uv
tool`, `cargo`, or `npm -g` transaction was run; no host service was restarted.
