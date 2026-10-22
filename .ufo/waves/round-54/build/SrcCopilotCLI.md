Result: DONE — Copilot CLI's own command reference documents exactly one number on a skill's `description` ("Max 1024 characters"), with no documented truncation, shortening, listing budget or refusal past it; the drafted SOURCES row, entry row, Gate quote and SKILL.md row make the frozen C1 counter report `Copilot CLI BACKED found=True` in my sandbox clone.

# C1 source record — Copilot CLI (reserved row S056)

Seat: `SrcCopilotCLI`. Lane read-only; all execution in `/fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI` (clone of the lane at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, which is my pin; the lane tip I observed while reading was `d051ec40225a2cf330e45348eaf755a9877f5745`, not mine to judge). No lane file edited; no counter edited; no jj command run.

## 1. What the client documents

GitHub Copilot CLI's skills *how-to* page carries no limit at all (`grep -ciE 'charact|truncat|limit|budget|maximum'` over the fetched page → 0). Its command reference carries one, in the frontmatter table of `## Skills reference`:

- served markdown, `cli-command-reference.md:1274`:
  `| `description` | string | Yes | What the skill does and when to use it. Max 1024 characters. |`
- docs source, `content/copilot/reference/copilot-cli-reference/cli-command-reference.md:1285` in github/docs `main` (same sentence, unpadded cell widths).

Reading: an **authoring maximum** — it caps the value the client accepts in `SKILL.md`, not how much of the description reaches the model. It is *not* a per-entry cut and *not* a listing budget; the page states neither. The number coincides with the Agent Skills specification's own cap (already recorded in the lane at `corpus/knowledge/frontmatter-rule-authorities-round48.md:44`, and as the VS Code row S025's teach), so its value for C1 is that **this client's own docs host states it**; it is not evidence of a Copilot-CLI-specific render cut.

What the client does past the cap: **not documented**. See §10.

## 2. Deliverable 1 — `corpus/SOURCES.md` row (append after S052, before `## Paths`)

```
| S056 | GitHub Docs — GitHub Copilot CLI command reference — https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference | docs | A | The documented maximum length of a skill description in GitHub Copilot CLI's own frontmatter table | § Skills reference → § Skill frontmatter fields, the `description` row (`cli-command-reference.md:1274`); served .md fetched 2026-10-22T21:18:03Z (200, 461,944 B, sha256 `c61997ef…`), byte-identical to the S031 and S038 fetches; same row at `content/copilot/reference/copilot-cli-reference/cli-command-reference.md:1285` in github/docs main (200, 177,073 B, sha256 `48de33ea…`) | A skill description is required in frontmatter and its documented maximum is 1024 characters | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |
```

Eleven cells; first URL in the `source` cell is `docs.github.com`, one of the counter's pinned hosts for `Copilot CLI`. The `teaches` cell states no more than the quote. No `S056b` was needed.

## 3. Deliverable 2 — fetch record (all 2026-10-22, UTC)

| # | URL | HTTP | bytes | sha256 | window |
|---|---|---|---|---|---|
| 1 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` | 21:18:03Z → 21:18:04Z |
| 2 | https://raw.githubusercontent.com/github/docs/main/content/copilot/reference/copilot-cli-reference/cli-command-reference.md | 200 | 177,073 | `48de33ea09a3e532f2355c45886d6e17aa37090fe9599cd4240a1d04f035c7f2` | 21:18:04Z |
| 3 | https://raw.githubusercontent.com/github/copilot-cli/7ea98dfc33c68aaf6443ea8fc054e20ff7fcd120/changelog.md | 200 | 289,859 | `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb` | 21:18:04Z |
| 4 | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md | 200 | 10,057 | `989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0` | 21:18:04Z |
| 5 | https://docs.github.com/en/copilot/concepts/customizations/agent-skills.md | 200 | 2,622 | `ed1e29440ec3aeadef2f461d1dc29910eb4014f0a1b451d8f04e73763605d4a7` | 21:24:08Z |
| 6 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference.md | 200 | 47,200 | `d0d362cc5aa2ef84775145e499596c7e6529531c7b29972ae29f547b5da220d0` | 21:16:34Z |
| 7 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference.md | 200 | 166,811 | `8be36090c19a7e284d4137f03db150927f3f215fb3b21ddfc9d87c614bec21b0` | 21:16:41Z |
| 8 | https://docs.github.com/en/copilot/reference/customization-cheat-sheet.md | 200 | 10,699 | `25f43326fb38833208df14cc9d9f6a72bf182f0785bf5b2a86748953a0fc3b25` | 21:16:41Z |

Rows 6-8 times are the download files' modification stamps (`ls --time-style=full-iso`, host clock UTC-03:00, converted), not a start/end window.

Fetch route notes: `…/copilot-cli/customize-copilot/create-skills` and `…/concepts/agents/about-agent-skills` both 302-redirect to the pages in rows 4 and 5. The `.md` route for the concept page exists only at the canonical path (`concepts/customizations/agent-skills.md`); the pre-redirect path returns 404. The served page and the docs source carry the identical sentence at the cited lines (rows 1 and 2). Measured size difference, not attributed: served 1,944 lines / 461,944 B against source 1,955 lines / 177,073 B — the served file's lines are longer on average, and I did not establish why.

Row 1's sha256 equals the S031 and S038 fetches (`c61997ef…`) and row 3's equals the S042 fetch (`c4b793bd…`): neither page moved since those rounds, so my row records no change, only a new anchor and teach.

## 4. Deliverable 3 — entry row for `corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record

```
| Copilot CLI | S056 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | Authoring maximum: the frontmatter table caps a skill description at 1024 characters, and the page states no behaviour past the cap. |
```

Quote: 12 words, verbatim, carries the number as a whole token.

## 5. Deliverable 4 — Gate row for `corpus/lessons/round-54.md` § Gate

```
| S056 | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 2026-10-22T21:18:03Z | 461,944 B, sha256 c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | SrcCopilotCLI |
```

## 6. Deliverable 5 — SKILL.md row for `### Description thresholds by client`

```
| Copilot CLI | `description` max 1024 characters | not documented; the page states the cap and no truncation, shortening or refusal | keep the description at 1024 characters or fewer, front-loaded on what the skill does and when to use it |
```

## 7. Counter self-check (sandbox clone, not the lane)

I built the four artifacts in my clone (final state `ec24056`, on base `7ad05d34`) and ran the frozen counter on that working tree, which `ec24056` records unchanged:

```
$ cd /fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI
$ python3 -B verifiers/check_description_thresholds.py --root .
Copilot CLI  BACKED
description thresholds backed 1 of 7 clients            # exit 1 (only 1 < target 4; the other six clients have no row yet)
$ python3 -B verifiers/check_description_thresholds.py --root . --fetch
Copilot CLI  BACKED found=True
description thresholds backed 1 of 7 clients
description thresholds found on the live page 1 of 1    # exit 1 (same reason)
```

(The per-client JSON for Copilot CLI: `row S056`, `url …/cli-command-reference`, `tokens ["1024"]`, `backed true`, `why []`.) Re-run against the committed revision, so the artifacts alone carry the verdict:

```
$ python3 -B verifiers/check_description_thresholds.py --rev ec24056
Copilot CLI  BACKED
description thresholds backed 1 of 7 clients            # exit 1
```

So the drafted rows satisfy C1's per-client rule exactly as frozen; whether the round clears `backed 4 of 7` depends on the other six seats, and on nothing in this report.

## 8. Negative sweep — no other documented number (Q30 three parts)

**Part 1, changelog / release notes.** `github/copilot-cli` at pinned commit `7ea98dfc…` (`changelog.md`, 289,859 B, 3,569 lines). Skill-related numeric statements, each checked and none a description or listing limit:

- `changelog.md:1315` (1.0.64): picker **name** column widened from 25 to 35 characters so fewer long skill *names* are truncated — a terminal picker column, not the model-facing listing.
- `changelog.md:1965` (1.0.33): the skill picker truncates CJK/Japanese descriptions and long names — a display cut, no number.
- `changelog.md:1993` (1.0.32): "Skills that exceed the token limit are still discoverable and invocable by name" — implies a token budget exists, states no number.
- `changelog.md:1006` (1.0.69) and `:773` (1.0.72): skill loading warnings surfaced in `skill list`; control characters stripped from names/descriptions in listing output — no length rule.
- `changelog.md:2754` (0.0.410): name validation widened; name and description made optional with fallbacks — no cap.
- `grep -nE '1024|2048|4096' changelog.md` → no output, exit 1.

**Part 2, docs source tree.** All 63 markdown files under `content/copilot/how-tos/copilot-cli/`, `content/copilot/concepts/customizations/` and `content/copilot/reference/copilot-cli-reference/` in github/docs `main` (list: `_scratch/srctree/list.txt`, 63 paths; fetched with `raw.githubusercontent.com`, all HTTP 200). Result:

- `grep -l '1024' *.md` → exactly two files: `cli-command-reference.md` (one line, the skill `description` row) and `cli-plugin-reference.md` (the plugin-manifest and marketplace description caps).
- `grep -nEi 'skill.{0,80}(limit|truncat|characters|budget|maximum|max )'` across all 63 → exactly one line: `cli-command-reference.md:1285`, the row this report records.

**Part 3, lane corpus.** `grep -rn '1024' corpus/ SKILL.md | grep -i copilot` → one line, S025 (the VS Code row, whose page states "capped at 1024 characters" for VS Code's skills). No lane file records a Copilot-CLI-authored number: `corpus/knowledge/` files naming Copilot CLI are the round-49/50/51/52/53 entries, none of which carries a Copilot CLI description cap.

Conclusion: Copilot CLI documents **one** number in this area, the 1024-character authoring maximum; it documents **no** per-entry cut in the listing and **no** listing budget, and it does not say what happens past the cap. That is a "documents nothing" statement for those three sub-questions, made after the three-part sweep above.

## 9. Adjacent numbers found and why they do not qualify

- `cli-command-reference.md:1273`: skill `name` "Max 64 characters" — a name cap, not the description.
- `cli-command-reference.md:1186`: combined MCP tool name (`serverName-toolName`) capped at 64 characters — MCP tool names.
- `cli-plugin-reference.md:195` and `:349`: plugin manifest and marketplace `description` "Max 1024 chars" — a *plugin's* description, not a skill's. (`:189`, `:338`, `:347`: 64-char name caps, same family.) A separate SOURCES row (S056b) was therefore not needed.
- `cli-config-dir-reference.md:461-462`, `:473`, `:509`: `disabledSkills`, `dynamicRetrieval {skills?}`, `ignoredSkillsLocations`, `skillDirectories` — levers/no numbers, no cap.

## 10. What happens past the cap — not documented; the one local probe is inconclusive

- The `## Skills reference` section has no validation, warning or troubleshooting statement; `grep -niE 'skill.{0,40}(valid|invalid|too long|exceed)|(valid|invalid|too long|exceed).{0,40}skill'` over the whole served command reference returns no matching lines (grep exit 1). `copilot skill list --json` is documented to return a `description` field per row (`cli-command-reference.md:1330`) with no truncation note.
- Attempted probe on the installed CLI, recorded so nobody repeats it as if it settled anything: the wrapper `~/.local/bin/copilot` resolves `@github/copilot` through npx; the payload is `~/.npm/_npx/965e8981e34edf7c/node_modules/@github/copilot-linux-x64/copilot` (198,445,888 B). `grep -a -c '1024 characters'` → 0, but the **control** `grep -a -c 'SKILL.md'` → 0 and `grep -a -c 'disable-model-invocation'` → 0, so the binary is not plain-text greppable and the negative proves nothing. **No claim rests on this probe.**
- Only doc-introspection CLI runs were made: `copilot --version` (GitHub Copilot CLI 1.0.103) and `copilot skill --help`. No model call, no `claude -p` / `codex exec` / `opencode run` / `gemini -p`.

## 11. Integration notes for the L1

1. **Index the new entry.** `verifiers/verify_corpus_integrity.py` counts indexed corpus files. At the pinned tip `7ad05d34` it already reports DRIFT before any round-54 content: `corpus.index.tracked_files 79 | 78 | DRIFT`, `corpus.index.unindexed 1 | 0 | DRIFT` (`corpus/lessons/round-53-verifier-spotcheck.md`), `corpus.pointers.report_total 51 | 49 | DRIFT`, exit 1. My harness copy raised it to `tracked_files 81` / `unindexed 3` (adding `corpus/knowledge/skill-listing-thresholds-round54.md` and `corpus/lessons/round-54.md`). Landing the entry therefore needs a `corpus/README.md` index row for the entry and for `lessons/round-54.md` (`README.md:83` already says the spot-check lesson is "indexed round 54"), plus whatever baseline re-record the wave-2 corpus-integrity seat owns. Not a defect of this row, but it is the row's landing cost.
2. **Same URL, two earlier rows.** S028 is the plugin reference (different page). S031 and S038 are this command reference; their anchors span the same table (S031 `:1269-1279`, S038 `:1278`), but neither teaches the description cap — S031's teach is the `disable-model-invocation` lever and the name-keyed arbitration rules, S038's a supersede of S031. S056 anchors the `description` row itself (`:1274`) and teaches only the cap, so it duplicates no teach; it also duplicates no anchor line. If the L1 would rather fold the cap into S038 as a supersede, the entry's `row` cell would then cite S038 and the Gate row would need S038's bytes (identical sha256, so `--fetch` is unaffected).
3. **Line budget.** The drafted SKILL.md row is one line; `SKILL.md` at `7ad05d34` is 552 lines, and the counter's `trigger.line_budget` is not in this seat's scope.

## 12. Limits of this record

- I did not verify that Copilot CLI truncates, refuses or accepts a description over 1024 characters — the docs state no behaviour, and my binary probe was inconclusive by its own control. Any sentence claiming truncation at 1024 would be unsourced.
- The number is the shared Agent Skills cap restated by this client; it is not evidence that Copilot CLI behaves differently from other clients at the boundary.
- The three pages in fetch rows 6-8 are timed by download file stamp, not by a start/end window.
- The docs source is `github/docs` `main` (unversioned): the served sha256 is the record, the source is corroboration for the sentence's wording at a second location, not a pin.

## 13. Tooling

No installs, no upgrades, no pacman transaction. Local commands used: `curl`, `sha256sum`, `gh api` (read-only tree listings), `git` (clone/checkout/commit inside my sandbox only), `copilot --version`, `copilot skill --help`.

## 14. Artifacts

- Harness clone with the four drafted artifacts committed: `/fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI` at `ec24056` (base `7ad05d34`; earlier fixture commit `a78d827` carries provisional wording).
- Counter runs: `/tmp/final-fetch.txt` (text), `/tmp/final.json` (JSON + summary line).
- Fetched bytes: `/fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI/_scratch/fetch2/` (command reference served and source, changelog, skills how-to, concept page, config-dir and cheat-sheet pages, `cmdref.html`), `/fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI/_scratch/fetch/` (plugin reference), docs source sweep `_scratch/srctree/` (63 files + `list.txt`).
- Corpus-integrity comparison captures: `/tmp/ci-tip.json` (tip), `/tmp/ci.json` (fixture).
