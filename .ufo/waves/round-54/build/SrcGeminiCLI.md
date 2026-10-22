# SrcGeminiCLI — Gemini CLI description-volume source (round 54, C1)

Result: DONE — Gemini CLI's own documentation gives exactly one number for how much of a skill's metadata reaches the model before activation (`~100 words`, always in context, a soft per-skill listing budget); no authoring maximum and no per-entry cut are documented, and code reading at 451a02ff shows the loader and prompt renderer pass the description through whole.

Scope of this report: the C1 source seat for client `Gemini CLI`, reserved SOURCES id `S057`. I opened the client's documentation this round, recorded one tier-A `mined` row, one entry row, one Gate row and one draft SKILL.md decision-table row. Nothing in the lane was written; lane reads were plain file reads and greps, and no git or jj command ran in the lane. All assembly and execution happened in my own sandbox clone.

## 1. What the client documents

The client's docs make three statements that matter for this frontier row, at `geminicli.com/docs/cli/skills-best-practices.md`:

- `:8-9` — "The most important part of a skill is its `description`. This is the only information the model has before activation."
- `:24` — the only numeric statement about description volume: `1.  **Metadata (name + description)**: Always in context (~100 words).`
- `:25` — the body figure, which is not a description limit: ``2.  **`SKILL.md` body**: Loaded only after the skill triggers (<5k words).``

The companion page `skills.md:20-22` says the name and description of **all** enabled skills are injected into the system prompt at session start, and `skills.md:90-91` documents `/skills list [all] [nodesc]` where `nodesc` hides descriptions — from the human-facing list, not from the prompt (see § 5).

Reading: `~100 words` is a **listing budget** for one skill's metadata (name plus description, always in context). It is not an authoring maximum and not a per-entry cut in a rendered listing. Past it the documentation is silent; the code has no cut (see § 5), so the consequence is spent context tokens, with no documented warning, truncation or refusal.

## 2. Fetch record (all 2026-10-22 UTC; `curl`, no headless browser, no captcha route)

| URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|
| https://geminicli.com/docs/cli/skills-best-practices.md | 21:16:27Z | 200 | 3,257 | `612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3` |
| https://geminicli.com/docs/cli/skills.md | 21:16:05Z | 200 | 5,763 | `8e1b4cbe2cd31effa3375aa5d480269ab28bf82c02a42d9b52cbb61e5b248590` |
| https://geminicli.com/docs/cli/creating-skills.md | 21:16:27Z | 200 | 6,705 | `b7061545075525a3fda156cb8350a6e8079367c3a3cf454fe470c62bf5246c3c` |
| https://geminicli.com/docs/cli/using-agent-skills.md | 21:16:27Z | 200 | 3,052 | `9e61fb7cb289263a102e937849f7019efc860e961da1dbcdf3ce36056e9df708` |
| https://geminicli.com/docs/cli/cli-reference.md | 21:16:27Z | 200 | 16,561 | `2d445008576bc09564f6a204482d8f980272f159781b2a79e07de6abc8a87840` |
| https://geminicli.com/docs/changelogs/latest.md | 21:18:27Z | 200 | 4,140 | `f38215087f7adabbd9d52831ceeb1def13bc98eb4b62181c518f295e399dd68f` |
| https://geminicli.com/docs/changelogs/preview.md | 21:18:27Z | 200 | 6,038 | `c186463197c0cb2d65eece11cc0b69a567d7a2b4967443447cf8488b40d06593` |
| https://geminicli.com/docs/cli/skills-best-practices/ (HTML; 301 from the no-slash route) | 21:19:55Z | 200 | 104,469 | `40bb440debc96489a6ce663571dcfaab87290fb630a80b6f86d64856f66230f0` |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/cli/skills.md | 21:16:05Z | 200 | 5,740 | `51e8573ef4c068dbdef5f73bd665c47ab16718aefe4edba365fe333b2d85f96d` |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/skills/skillLoader.ts | 21:17:02Z | 200 | 6,560 | `8bce3215263e9ec06f32a865715c04af6deb4b6299db1490665f53972d4326f9` |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/packages/core/src/skills/skillManager.ts | 21:17:02Z | 200 | 5,755 | `0e13ed68e7d76725d95342428c12e4a823c06e75a89654cbb4ee079b4297d613` |
| https://raw.githubusercontent.com/google-gemini/gemini-cli/main/CHANGELOG.md | 21:16:05Z | 404 | 14 | `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed` |
| https://github.com/google-gemini/gemini-cli/tree/main/packages/core/src/skills (HTML directory listing) | 21:16:44Z | 200 | 222,821 | `770d685b2f105fa6b8979fd0c177c4e0a5608b66f048ff6fcee8fe8f1d8eb3b8` |
| https://api.github.com/repos/google-gemini/gemini-cli/git/trees/main?recursive=1 | 21:16:31Z | 403 | 280 | unauthenticated rate limit (`"API rate limit exceeded"`); replaced by the shallow clone below |

The served page's own response headers (re-fetched headers-only at 21:23:19Z): `content-type: text/markdown; charset=utf-8`, `content-length: 3257`, `etag: "94f3a2f9e95d8ddf438c28edc827b90bb7c3e3eff129c05694b444b017bb8eb6"`, `last-modified: Fri, 16 Oct 2026 02:36:07 GMT`. A body re-fetch at 21:23:19Z returned the same 3,257 bytes and the same sha256.

Fetched file: `/fast/scratch/hyaku/kotoba-r54/SrcGeminiCLI/fetch/geminicli.com_docs_cli_skills-best-practices.md`; quote is on **line 24** of those bytes (`grep -n "Metadata"` → `24:1.  **Metadata (name + description)**: Always in context (~100 words).`).

Never fetched with any paid model call; no client binary or CLI was run.

## 3. Served page vs the docs source tree

- `docs/cli/skills-best-practices.md` in google-gemini/gemini-cli at `451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1` is identical to the served markdown except a missing final newline on the served copy (`diff` → one `\ No newline at end of file` hunk). Same line 24, same words.
- `docs/cli/skills.md` at the same commit differs from the served markdown only in link targets (7 hunks: `/docs/...` vs `./....md`). Prose, including `:20-22` (all enabled skills injected) and `:90-91` (`nodesc`), is identical.
- The served changelog lags the repo: `geminicli.com/docs/changelogs/latest.md` says `# Latest stable release: v0.64.0`, `Released: October 13, 2026` (4,140 B), while `docs/changelogs/latest.md` at `451a02ff` says `v0.65.0`, `Released: October 20, 2026` (5,916 B). Recorded as a provenance limit, not a freshness claim.
- The clone: `git clone -q --filter=blob:none --no-checkout --depth 1 https://github.com/google-gemini/gemini-cli repo`, sparse `packages/core/src docs` (later `packages/cli/src`), `git log -1` → `451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1 2026-10-22T19:07:09Z` — the same commit round 53's S046 row pinned.

## 4. Delivered rows

### (1) `corpus/SOURCES.md` row — append at the end of the registry table, before `## Leads (unopened)` (11 cells; verified 11 by splitting on `|`)

```
| S057 | Gemini CLI docs — Agent Skill best practices (served page, checked against the docs source tree at 451a02ff) — https://geminicli.com/docs/cli/skills-best-practices.md | docs | A | What Gemini CLI's own documentation states about how much of a skill's name and description stays in the model's context and what it says about that volume (vendor documentation of a soft budget, not a measurement of any installed binary) | § Progressive disclosure (`skills-best-practices.md:24`); § Design for discovery (`:8-16`); fetched 2026-10-22T21:16:27Z (200, 3,257 B, sha256 `612c3b83…`), byte-identical to `docs/cli/skills-best-practices.md` at google-gemini/gemini-cli@`451a02ff` except a missing trailing newline on the served copy; the slash route (200, 104,469 B, sha256 `40bb440d…`) carries the same sentence; S029 already cites this page at `:24` in its teaches cell | A skill's name and description are always in context as metadata budgeted at about 100 words | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |
```

The `teaches` cell says no more than the quote (`~100 words`, always in context, name plus description). The anchor carries the page's other locations and the provenance; it also records that S029 already cites `:24`, so the entry is not presented as a new discovery.

### (2) Entry row — `corpus/knowledge/skill-listing-thresholds-round54.md`, under `## Per-client record` with header `client | row | quote | location | reading`

```
| Gemini CLI | S057 | "Metadata (name + description): Always in context (~100 words)." | `skills-best-practices.md:24` | A soft per-skill listing budget, not an authoring maximum or a per-entry cut: the metadata is always in context at about 100 words, and past it the client documents nothing — the description reaches the prompt whole (no truncation at `skillLoader.ts:211` or `snippets.ts:320`, commit `451a02ff`), so the cost is context tokens. |
```

Quote mechanics: 9 words; contains `100` as a whole token; it is the served line 24 with the list ordinal and the two emphasis markers dropped (markup, not words; the counter's own `--fetch` normalization strips `*`, backticks and underscores from both sides). The words, punctuation and the `~` are verbatim from the fetched bytes.

### (3) Gate row — `corpus/lessons/round-54.md` § Gate

```
| S057 | https://geminicli.com/docs/cli/skills-best-practices.md | 2026-10-22T21:16:27Z | 3,257 B, sha256 612c3b83… | "Metadata (name + description): Always in context (~100 words)." | `skills-best-practices.md:24` | SrcGeminiCLI |
```

### (4) Draft SKILL.md row — `### Description thresholds by client`, header `Client | Documented threshold | Past the threshold | Action`

```
| Gemini CLI | ~100 words of metadata (name + description) always in context per skill | Nothing is cut: the full description is injected, so a longer one spends context tokens with no documented warning or truncation | Keep name + description near 100 words and move detail into the `SKILL.md` body, which loads only after activation (`skills-best-practices.md:24-25`) |
```

The threshold cell holds exactly one number token (`100`), matching the quote. The location reference sits in the action cell so the threshold cell cannot be misread as threshold 24.

## 5. Why "nothing is cut" — code reading, not execution [INFERENCE about runtime behaviour]

Evidence at google-gemini/gemini-cli `451a02ff` (shallow clone; files also fetched raw, hashes above):

- `packages/core/src/skills/skillLoader.ts:211` — `description: frontmatter.description,`: the frontmatter string is kept as-is; the loader's only `length` use is quote stripping (`:66`, `value.length >= 2`). No cap, no validation of description length.
- `packages/core/src/prompts/snippets.ts:314-325` — `renderAgentSkills` builds `<description>${skill.description}</description>` (`:320`) with no slice or escape.
- `packages/core/src/prompts/promptProvider.ts:120-126` (the `system.md` override branch) and `:166-173` (standard composition) — both pass `description: s.description` straight through.
- `packages/cli/src/ui/commands/skillsCommand.ts:37-43,72` — `nodesc`/`--nodesc` only sets `useShowDescriptions`, passed as `showDescriptions: useShowDescriptions` for the `/skills list` UI. It is not wired to the prompt path, so it cannot keep a description out of the model's context.
- `grep -rn -E "description\.(slice|substring|substr)|\.slice\(0, *[0-9]+\)" packages/core/src/skills packages/core/src/prompts/snippets.ts packages/core/src/prompts/promptProvider.ts packages/cli/src/ui/commands/skillsCommand.ts` → rc=1, no match.
- Warning sites in the skill path are about discovery errors (`skillLoader.ts:179`) and name collisions (`skillManager.ts:133,138`); none concerns description length.

## 6. Sweep record (the three Q30 legs, run although the client does document a number)

Run in `/fast/scratch/hyaku/kotoba-r54/SrcGeminiCLI/repo` (clone at `451a02ff`) and the lane checkout.

Leg A — changelog / release notes:
```
$ grep -n -i "skill" geminicli.com_docs_changelogs_latest.md geminicli.com_docs_changelogs_preview.md
(no output; rc=1)
$ ls docs/changelogs
index.md  latest.md  preview.md
$ grep -n -i "skill" docs/changelogs/preview.md
71:- fix(core): harden SKILL.md frontmatter parsing for single-line descriptions by
$ grep -n -i "skill" docs/releases.md
(no output; rc=1)
```
`docs/changelogs/index.md` has 22 lines mentioning skills; read through those 22 matches, none states a description or listing limit with a number (e.g. `:233`, `:256`, `:303-304`, `:560-562`, `:611`, `:664-670`).

Leg B — current docs source tree:
```
$ grep -rnE "[0-9]+ ?(words|characters|chars|tokens)" docs/ | grep -iE "skill|description"
docs/cli/skills-best-practices.md:24:1.  **Metadata (name + description)**: Always in context (~100 words).
$ grep -n -iE "budget|limit|max(imum)?\b|cap\b|truncat|characters|chars" docs/cli/skills.md docs/cli/skills-best-practices.md docs/cli/creating-skills.md docs/cli/using-agent-skills.md
docs/cli/skills-best-practices.md:77:- **Limit scope**: Design skills to be as focused as possible to minimize the
```
Line 77 is prose with no number. `docs/reference/configuration.md` lists only `skills.enabled` (boolean), `skills.disabled` (array) and `admin.skills.enabled`; no size key.

```
$ grep -rnE "(up to|at most|maximum of|limit of|no more than) [0-9]+|[0-9]+ (skills|skill)" docs/ | grep -i skill
(no output; rc=1)
$ grep -nE "(up to|at most|maximum of|limit of|no more than) [0-9]+|[0-9]+ (skills|skill)" geminicli.com_docs_cli_skills.md geminicli.com_docs_cli_skills-best-practices.md geminicli.com_docs_cli_creating-skills.md geminicli.com_docs_cli_using-agent-skills.md
(no output; rc=1)
```
So there is no documented cap on the number of skills either, in the served pages or the source tree.

Leg C — lane corpus:
```
$ grep -rn "100 words" corpus/
corpus/SOURCES.md:42  (one hit, inside S029's teaches cell: "... → 0; the soft budget is \"~100 words\" of metadata, `skills-best-practices.md:24`)")
$ grep -rn -iE "gemini" corpus/ | grep -iE "threshold|truncat|character limit|word limit|1024|8000"
corpus/SOURCES.md:42  (the S029 row, same cell)
$ grep -rn "skill-listing-thresholds" corpus/ SKILL.md verifiers/
verifiers/check_description_thresholds.py:9, :78, :329, :356
```
So the number is already in the corpus through S029 (round 50's row: "no description length cap appears in the prose (`1024` → 0; the soft budget is "~100 words" of metadata, `skills-best-practices.md:24`)"). It is not new knowledge; S057 is a dedicated row for the page that the C1 counter can use, and the entry must be worded as confirmation of S029, not as discovery.

## 7. Counter verification in my sandbox

Sandbox clone (lane untouched): `/fast/scratch/hyaku/kotoba-r54/SrcGeminiCLI/lane`, checked out at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`. I assembled the four pieces above there plus a minimal `corpus/lessons/round-54.md` Gate table.

```
$ python3 -B verifiers/check_description_thresholds.py --rev 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39
description thresholds backed 0 of 7 clients        (exit 1)
$ python3 -B verifiers/check_description_thresholds.py --root . --json
...
"client": "Gemini CLI", "row": "S057", "url": "https://geminicli.com/docs/cli/skills-best-practices.md",
"quote": "Metadata (name + description): Always in context (~100 words).",
"tokens": ["100"], "backed": true, "why": []
...
description thresholds backed 1 of 7 clients        (exit 1; target is 4, other seats' rows absent)
$ python3 -B verifiers/check_description_thresholds.py --root . --fetch --json
description thresholds backed 1 of 7 clients
description thresholds found on the live page 1 of 1
```
So the Gemini CLI cells satisfy every rule in the counter's docstring, and the quote is found on the live page. `SKILL.md` in the sandbox was 558 lines with the section appended (552 at tip plus 6 appended lines; a placed section of heading + blank + 3 table lines is 5, plus one separating blank → 557), under the 600-line `trigger.line_budget` the plan cites.

## 8. Findings

1. **One number, and it is a budget.** Gemini CLI's own docs state no authoring maximum and no per-entry cut for a skill's `description`; the only number is `~100 words` for metadata (name plus description) that is always in context (`skills-best-practices.md:24`). Past it: no documented behaviour; the code injects the full description (`snippets.ts:320`), so the cost is context tokens. A reviewer may read `~100 words` as a description of the loading layer rather than a limit; the counter does not judge that (Q31), and the entry says which reading it takes.
2. **The number already exists in the corpus.** S029's teaches cell (`corpus/SOURCES.md:42`) records "the soft budget is "~100 words" of metadata, `skills-best-practices.md:24`" and notes `1024` → 0 (no cap in the prose). My row must not be sold as new knowledge; the entry's value is the dedicated row, the Gate quote and the decision-table row the C1 counter requires.
3. **`nodesc` is not a description control.** It hides descriptions in the `/skills list` UI only (`skillsCommand.ts:37-43,72`); prompt injection of every enabled skill's name and description is unconditional (`skills.md:20-22`, `snippets.ts:314-325`).
4. **Served vs source.** Page identical except a trailing newline; `skills.md` identical in prose, different in link targets only; the served changelog is one release behind the repo (v0.64.0 vs v0.65.0) and mentions no skill limits. A reader who used only the served changelog would see nothing on this topic — which is why the repo `preview.md:71` line is reported here.
5. **No other numeric limit found in the four skill pages**: only step numbers and the `<5k words` body figure (`:25`), which is not a description limit. Commands and outputs in § 6.

## 9. Limits and out-of-scope

- The client binary was never run. "The full description reaches the prompt" is code reading at `451a02ff`; runtime behaviour (e.g. a downstream model-side truncation) is not measured. Marked [INFERENCE].
- The `~100 words` figure covers name plus description together, not the description alone; the entry says so.
- The Gate quote drops the markdown list ordinal `1.` and the `**` emphasis markers; the words, punctuation and `~` are verbatim from line 24 of the fetched bytes. If the L1 prefers the exact line bytes, quote `**Metadata (name + description)**: Always in context (~100 words).` — it still passes `--fetch` and is 9 words, but it renders with literal asterisks in the table.
- No freshness claim, no change to `verifiers/verify_surfaces.py`, nothing on the executed-checklist / always-on-box frontier. No C2 work. No lane writes, no git writes in the lane, no jj commands.
- Tooling: no installs or upgrades (system `curl`, `git`, `python3` 3.14 only). Scratch paths: `/fast/scratch/hyaku/kotoba-r54/SrcGeminiCLI/{fetch,repo,lane}`.
- The GitHub REST tree route was rate-limited (403, § 2); the shallow sparse clone replaced it. The raw `CHANGELOG.md` route is 404 — the repo keeps release notes in `docs/changelogs/`.
