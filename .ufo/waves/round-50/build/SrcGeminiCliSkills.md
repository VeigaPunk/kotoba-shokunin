# Round 50 seat report — SrcGeminiCliSkills (C1 source: Gemini CLI skills docs)

Result: **the Gemini CLI docs state a tie-break only for skills that share a NAME (by discovery-tier precedence); they state NO tie-break for two skills with different names and overlapping scope** — and they state **no description length cap at all** (the 1024-character cap exists only in Gemini CLI's own authoring validator script, not in the docs prose and not in the loader).

Scope: open `https://geminicli.com/docs/cli/skills/` by ordinary means (curl; the site serves a `.md` variant), record URL / UTC access time / HTTP status / bytes / sha256, locate verbatim quotes for description-in-discovery, description-in-activation, the cap, and same-name/overlapping-scope precedence, run the required `grep -ciE` sweep, and draft the `corpus/SOURCES.md` row plus the round-50 lesson `## Gate` line. Read-only on the lane; the only file written there is this report. Scratch `/fast/scratch/hyaku/kotoba-r50/build/SrcGeminiCliSkills/`. No package installed or upgraded (curl, sha256sum, grep, git ls-remote only).

## Fetch record

| route | accessed (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://geminicli.com/docs/cli/skills/ | 2026-10-22T12:28:34Z | 200 | 114,148 | `b17895012da7cbefb20291d6210a3b016d0680a53d6fbc4eaed703d9b0f98640` |
| https://geminicli.com/docs/cli/skills.md | 2026-10-22T12:28:45Z, re-fetch 12:34:04Z | 200 | 5,763 | `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` |
| https://geminicli.com/docs/cli/skills (no trailing slash) | 2026-10-22T12:29Z | 200, no redirect | — | — |

Both routes carry the same prose; the `.md` variant is byte-identical across two fetches (`cmp` exit 0). Header on the `.md` route: `last-modified: Fri, 16 Oct 2026 02:36:07 GMT`, `etag: "0957231f9c46588b9bdf8e23f4ec7fb73d8ac709348b0d3735b6f5214e24058e"`, `content-type: text/markdown`.

**The page did move and the old official host is dead.** `https://google-gemini.github.io/gemini-cli-docs/docs/cli/skills/` → HTTP 404 (also without trailing slash). The upstream README now points at `https://geminicli.com/docs/` (`README.md:28`, fetched 200, 12,107 B) and `https://geminicli.com/llms.txt` (200, 968,590 B) lists `**[Agent Skills](/docs/cli/skills)**` at line 263 — so `geminicli.com/docs/cli/skills/` is the current official Gemini CLI page on skills. Freshness: page `Last-Modified` 2026-10-16, six days before the fetch.

## Findings and located quotes (each ≤ 25 words)

**F1 — The `description` is the discovery and activation input.**
- § How it works (`skills.md:20-22`): "Gemini CLI scans the discovery tiers and injects the name and description of all enabled skills into the system prompt."
- § How it works, step 2 (`skills.md:23-24`): "When Gemini identifies a task matching a skill's description, it calls the `activate_skill` tool."
- § Design for discovery (`skills-best-practices.md:8-9`): "The most important part of a skill is its `description`. This is the only information the model has before activation."
- § Metadata and triggers (`creating-skills.md:155-156`): "**`description`**: **CRITICAL.** This is how Gemini decides when to use the skill."

**F2 — Precedence is stated, and it is by name.**
- § Discovery tiers (`skills.md:37-38`): "Gemini CLI discovers skills from several locations, following a specific order of precedence (lowest to highest)"
- § Precedence and aliases (`skills.md:51-52`), the only tie-break rule in the docs: "If multiple skills share the same name, the version from the higher-precedence location is used."
- § Precedence and aliases (`skills.md:52-53`): "the `.agents/skills/` alias takes precedence over the `.gemini/skills/` directory."
- Tier list (`skills.md:40-47`): built-in → extension → user (`~/.gemini/skills/` or `~/.agents/skills/`) → workspace (`.gemini/skills/` or `.agents/skills/`), lowest to highest. Same rule repeated on § Using Agent Skills (`using-agent-skills.md:19-20`).

**F3 — No rule for overlapping scope under distinct names.** The only "overlap" word in the five fetched Gemini CLI pages is authoring advice, not a runtime rule — § Design for discovery (`skills-best-practices.md:16-17`): "Avoid overlap: Ensure your skill descriptions are distinct from one another and from the general capabilities of the model." No arbitration, tie-break, ambiguity or conflict vocabulary appears in `skills.md` (sweep below).

**F4 — No description cap in the docs; the cap is in the vendor's own script.** `1024` → 0 hits on every fetched Gemini CLI doc page, and no page states a character budget for the description. The only budget is soft and stated in words — § Progressive disclosure (`skills-best-practices.md:24`): "**Metadata (name + description)**: Always in context (~100 words)." The hard cap is in the built-in skill-creator's validator, `packages/core/src/skills/builtin/skill-creator/scripts/validate_skill.cjs:71-72` (upstream commit `09d81bf116b6f0ef084731dc996aa9d56438bb70`, `main` tip by `git ls-remote` 2026-10-22T12:38:52Z): `if (description.length > 1024) { return { valid: false, message: 'Description is too long (max 1024)' }; }` The same file requires a single-line description (`:60-65`) and a hyphen-case name (`:67-69`). The **loader Gemini CLI actually reads at discovery** (`packages/core/src/skills/skillLoader.ts:40-134`) has no length check (`1024` → 0 hits) and silently skips a `SKILL.md` whose frontmatter lacks `name:` or `description:` (documented at `tutorial.md:111-113`). The cap is therefore an authoring-time rule of Gemini CLI's own packaging tooling, not a documented or load-time rule — do not credit it to the docs page.

**F5 — The vendor's own code confirms the name-only tie-break.** `packages/core/src/skills/skillManager.ts` (commit `09d81bf`): the merge map is keyed by name only (`:125-127`) and the last-discovered same-name skill wins (`:143`), with a warning, not a resolution rule (`:139`): `Skill conflict detected: "${newSkill.name}" from "${newSkill.location}" is overriding the same skill from "${existingSkill.location}".` Two skills with **different** names never collide: no description is compared anywhere (`grep -niE 'description.*(===|==|compare|similar|match)|similar'` over `skillManager.ts`, `skillLoader.ts`, `snippets.ts` → no match). The system prompt carries every enabled skill's name, description and location with no truncation — `packages/core/src/prompts/snippets.ts:318-322` renders `<skill><name>…</name><description>${skill.description}</description><location>${skill.location}</location></skill>`, called from `packages/core/src/prompts/promptProvider.ts:120-126,166-174`. Minor inconsistency worth recording: the source's doc comment says "Precedence: Extensions (lowest) -> User -> Workspace (highest)." (`skillManager.ts:52`) while the code comment says "Built-in skills (lowest precedence)" (`:61`); the docs page puts built-in lowest, which agrees with the code.

## Required sweep (Q14 negative evidence)

One `grep -ciE` per pattern over the fetched page text `skills.md` (5,763 B):

```
$ cd /fast/scratch/hyaku/kotoba-r50/build/SrcGeminiCliSkills
$ for p in 'overlap' 'ambigu' 'precedence' 'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do printf '%-16s %s\n' "$p" "$(grep -ciE "$p" skills.md)"; done
overlap 0 | ambig 0 | precedence 4 | tie[- ]?break 0 | conflict 0
multiple skills 1 | same name 1 | prioriti 1 | 1024 0 | truncat 0
```

Counts: `overlap` 0, `ambigu` 0, `precedence` 4, `tie[- ]?break` 0, `conflict` 0, `multiple skills` 1, `same name` 1, `prioriti` 1, `1024` 0, `truncat` 0. (`prioriti` 1 is `skills.md:33`, "prioritize the skill's procedural guidance", not a selection rule.) The same ten patterns over the HTML-text extraction of the HTML route give the same numbers except `precedence` 5 (the nav table of contents). Companion pages fetched at the same time: `skills-best-practices.md` overlap 1, precedence 0, rest 0; `creating-skills.md` precedence 1, rest 0; `using-agent-skills.md` precedence 2, `multiple skills` 1, `same name` 1, rest 0; `tutorial.md` all 0.

**Plain answer:** the page documents a tie-break between two skills **that share a name** (higher-precedence discovery location wins; `.agents/skills/` beats `.gemini/skills/` inside a tier) and **nothing** between two skills with different names whose descriptions overlap — the only "overlap" sentence in the whole Gemini CLI skills documentation tells the author to keep descriptions distinct, and the vendor's loader confirms it: the merge key is the name and no description is ever compared. Same shape of finding as the round-49 rows S022/S023 for Claude, now with a third client (Google's Gemini CLI) and a vendor implementation to back the negative claim.

## Drafted registry rows for `corpus/SOURCES.md` (11-column shape, ids for the L1)

The registry ends at S023 today (`grep -c '^| S0' corpus/SOURCES.md` → 23; `grep -ci gemini corpus/SOURCES.md` → 0, so this is a new row, not a re-open). Two rows are drafted: the docs page the claim needs, and the pinned vendor source carrying the cap and the name-only merge. Columns are id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by.

Row 1 (docs) — id placeholder `S0NN`:

| S0NN | Gemini CLI — Agent Skills — https://geminicli.com/docs/cli/skills/ | docs | A | How Gemini CLI discovers and activates skills (the `description`'s role) and what its documentation says about skills that collide (vendor documentation, not a measurement of omp or opencode) | § How it works (`skills.md:20-24`); § Discovery tiers (`skills.md:37-47`); § Precedence and aliases (`skills.md:49-53`); § Design for discovery (`skills-best-practices.md:8-17`); fetched as https://geminicli.com/docs/cli/skills.md (200, 5763 B, sha256 `8e1b4cbe…`) on 2026-10-22T12:28:45Z, byte-identical on re-fetch at 12:34:04Z, page Last-Modified 2026-10-16; the HTML route (200, 114148 B, sha256 `b1789501…`) carries the same prose; the former official host `google-gemini.github.io/gemini-cli-docs/docs/cli/skills/` is 404 and the upstream README now points at geminicli.com | The `description` is the only skill text in context before a trigger and the field the request is matched against, so it decides whether a skill applies; the only collision rule the page states is by name — two skills sharing a name resolve by discovery-tier precedence (built-in < extension < user < workspace), with `.agents/skills/` beating `.gemini/skills/` inside a tier; the page states no tie-break between two skills with different names and overlapping scope (sweeps over `skills.md`: `overlap`, `ambigu`, `tie[- ]?break`, `conflict` → 0 each; `multiple skills`, `same name` → 1 each; the single "Avoid overlap" line is author advice, `skills-best-practices.md:16`); no description length cap appears in the prose (`1024` → 0; the soft budget is "~100 words" of metadata, `skills-best-practices.md:24`) | mined | 2026-10-22 | 90d | SKILL.md, corpus/knowledge/sibling-overlap-census-round49.md |

Row 2 (vendor code) — id placeholder `S0NN+1`:

| S0NN+1 | google-gemini/gemini-cli — skill discovery, skill-creator validator — https://github.com/google-gemini/gemini-cli/tree/09d81bf116b6f0ef084731dc996aa9d56438bb70/packages/core/src/skills | code | A | Gemini CLI's own skill merge, prompt rendering and description validation (vendor source at a pinned commit, not a measurement of omp or opencode) | `packages/core/src/skills/skillManager.ts:52,61,124-146`; `packages/core/src/skills/skillLoader.ts:40-134`; `packages/core/src/prompts/snippets.ts:314-324`; `packages/core/src/prompts/promptProvider.ts:120-126,166-174`; `packages/core/src/skills/builtin/skill-creator/scripts/validate_skill.cjs:38-72`; upstream commit `09d81bf116b6f0ef084731dc996aa9d56438bb70` (`main` tip by `git ls-remote`, 2026-10-22T12:38:52Z); opened 2026-10-22, re-fetched 12:44:22Z byte-identical | The merge key is the name alone — `skillMap.set(newSkill.name, newSkill)` makes the last-discovered same-name skill win and logs "Skill conflict detected"; distinct names never collide and no description is ever compared, so two overlapping skills both reach the prompt, each rendered as name/description/location with no truncation; the 1024-character description cap and the single-line rule live only in the skill-creator's `validate_skill.cjs` (authoring-time), not in the loader Gemini CLI reads at discovery, and the loader silently skips a SKILL.md missing `name:` or `description:` | mined | 2026-10-22 | on-release | SKILL.md, corpus/knowledge/sibling-overlap-census-round49.md |

No cell of any existing row changes; no re-open, so no old→new table.

## Drafted lesson `## Gate` lines (for `corpus/lessons/round-50.md`, table shape of round 49)

| row | URL | accessed (UTC) | quote, at most 25 words (location) |
|---|---|---|---|
| S0NN | https://geminicli.com/docs/cli/skills/ | 2026-10-22T12:28:45Z | "If multiple skills share the same name, the version from the higher-precedence location is used." (§ Precedence and aliases, `skills.md:51-52`) — seat `.ufo/waves/round-50/build/SrcGeminiCliSkills.md` |
| S0NN+1 | https://raw.githubusercontent.com/google-gemini/gemini-cli/09d81bf116b6f0ef084731dc996aa9d56438bb70/packages/core/src/skills/builtin/skill-creator/scripts/validate_skill.cjs | 2026-10-22T12:44:22Z | "return { valid: false, message: 'Description is too long (max 1024)' }" (`validate_skill.cjs:72`) — seat `.ufo/waves/round-50/build/SrcGeminiCliSkills.md` |

Gate sentence for the L1, in the Q14 form (negative claim carries its sweep): the Gemini CLI skills documentation states a name-based precedence tie-break and no overlap tie-break; sweep over the fetched 5,763 B `skills.md` — `overlap` 0, `ambigu` 0, `tie[- ]?break` 0, `conflict` 0, `1024` 0, `truncat` 0, `precedence` 4, `multiple skills` 1, `same name` 1, `prioriti` 1 (command above).

## Axis note for the L1

**Adjacency (C1 source).** The new row is a third client-side authority on how a `description` drives skill selection, and its negative finding lines up with the round-49 Claude rows (S022/S023) and with the census entry's "What decides between overlapping skills" section, which may append this row and its sweep. Craft consequence: with three client docs and no vendor tie-break for differently-named overlapping skills, a description that names its neighbour and says who owns what is the whole author-side mechanism — the conclusion the census already reached from S022/S023.

**Freshness.** Page `Last-Modified` 2026-10-16, opened and re-fetched 2026-10-22 with byte-identical bytes; the pre-move official host 404s and the upstream README now points at geminicli.com, so the row is fresh as of today: recheck `90d` for the docs row, `on-release` for the code row (S021–S023 precedent).

## Out of scope / not done

No product code, `SKILL.md`, `PROVINCE.md`, `corpus/SOURCES.md` or lesson file was edited by this seat — the row and Gate lines above are drafts for the L1 to integrate. The Gemini CLI *runtime* was not exercised (no Gemini CLI on this host); the sweep and quotes are documentation-and-source evidence, not an observed router trace. The description cap was not traced past the skill-creator validator: no other length check exists in the loader and the prompt renderer does not truncate, but truncation elsewhere in the CLI's request pipeline was not searched exhaustively. The census entry `corpus/knowledge/sibling-overlap-census-round49.md` was read only for its "What decides between overlapping skills" section; this seat owns neither the census append nor the C1 counter.
