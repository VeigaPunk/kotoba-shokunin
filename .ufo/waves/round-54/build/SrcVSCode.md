Result: DONE — VS Code documents exactly one number that limits a skill's `description` (1024 characters, an authoring maximum); it documents no per-entry cut in the skill listing, no listing budget, and no consequence past the cap, recorded as S055 with entry, Gate and SKILL.md rows that the frozen counter marks backed in a sandbox clone.

## Behavior (what I opened this round)

Opened the client's own documentation at the markdown route, then swept the page, the
microsoft/vscode-docs source tree and the three most recent release notes for every
documented number that limits how much of a skill's `description` — or the skill list —
reaches the model or is accepted. Found exactly two numbers on the page that are limits:
`name` 64 characters (`agent-skills.md:147`) and `description` 1024 characters
(`:148`). Only the second is a description threshold. The page says what happens past the
name limit ("silently fail to load", line 147) and states nothing for the description.

## Fetch record

| what | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| served markdown (quoted source) | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T21:15:47Z | 200 | 22,871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| docs source file (pin check) | https://raw.githubusercontent.com/microsoft/vscode-docs/main/docs/agent-customization/agent-skills.md | 2026-10-22T21:15:55Z | 200 | 24,087 | `bae0c84d97f58b24a60611250db17d125fcccfe7217379494e055702167a8ccb` |
| release notes 1.143 (current) | https://code.visualstudio.com/updates/v1_143 | 2026-10-22T21:16:39Z | 200 | 109,512 | `ef373201ec4cdbec4b9c0c13b301eac711e1d39e6f6cb1a01934862e73483b1d` |
| release notes 1.142 | https://code.visualstudio.com/updates/v1_142 | 2026-10-22T21:16:39Z | 200 | 72,319 | `16ae927a4c8edb9443b7a7e90ba18b792bd0182125c57f579ae6fbcb44367840` |
| release notes 1.141 | https://code.visualstudio.com/updates/v1_141 | 2026-10-22T21:16:39Z | 200 | 115,526 | `4473da709b06c00839a971df628a9c0974568b41ebe9b89d63f84fe20dd0be3c` |

- Response headers on the quoted fetch: `content-type: text/markdown; charset=UTF-8`,
  `content-length: 22871`, `last-modified: Thu, 22 Oct 2026 18:02:44 GMT`,
  `HTTP/2 200`. Command:
  `curl -sS -D headers.txt -o page.md -w 'HTTP %{http_code}\nBYTES %{size_download}\n' https://code.visualstudio.com/docs/agent-customization/agent-skills.md`
  → `HTTP 200` / `BYTES 22871`, exit 0.
- The bytes are identical to the pin already recorded in row S025
  (`corpus/SOURCES.md:38`, fetched 2026-10-22T12:29:33Z, sha256 `de5ba34f…`), although
  Last-Modified moved from Wed 21 Oct 06:19:42 GMT to Thu 22 Oct 18:02:44 GMT. So the
  page body did not change today; only its stamp did.
- Served page vs docs source: the same 1024 sentence is present once in each
  (`grep -c -F 'Maximum 1024 characters.' src-page.md page.md` → 1 and 1). They differ in
  presentation only: the source has YAML frontmatter (`DateApproved: 10/21/2026`) and
  `{% data variables.… %}` placeholders, the served markdown has those substituted and an
  "AI agents: … see llms.txt" note prepended. Line numbers therefore shift: the
  `description` row is `agent-skills.md:148` served, `:159` in the source file. The docs
  tree I cloned is at `fd64d64891a2e660bcc0d32ea402da905adfef7f`; `git show HEAD:docs/agent-customization/agent-skills.md` hashes to `bae0c84d…` and 24,087 B, matching the
  raw fetch exactly.

## 1. SOURCES.md row (11 cells; paste as a new row of `## Registry`)

| S055 | Visual Studio Code — Use Agent Skills in VS Code (`description` maximum) — https://code.visualstudio.com/docs/agent-customization/agent-skills | docs | A | The documented number that limits a skill's frontmatter `description` in VS Code / GitHub Copilot, and whether the page documents a per-entry cut, listing budget or consequence past that number (vendor documentation for VS Code; not a measurement of the editor) | § SKILL.md file format → § Header (required), `description` row (`agent-skills.md:148`); § How Copilot uses skills, step 1 Discovery (`:302`) and the three-level note (`:308`); fetched as https://code.visualstudio.com/docs/agent-customization/agent-skills.md on 2026-10-22T21:15:47Z (200, 22,871 B, sha256 `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5`), byte-identical to the 12:29:33Z pin recorded in S025; upstream `docs/agent-customization/agent-skills.md:159` in microsoft/vscode-docs at `fd64d648` (24,087 B, sha256 `bae0c84d…`), same sentence | A skill's description helps Copilot decide when to load the skill, and its maximum is 1024 characters | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |

Notes for the integrator: the `teaches` cell deliberately says no more than the quote
(it does not claim truncation, a drop or a warning past the cap). The row keeps the
`source` cell's first URL on `code.visualstudio.com`, which is the pinned host for
VS Code in the counter (`HOSTS["VS Code"]`), and holds no `|` inside any cell so the
11-cell split is exact. S025 already covers this page for other claims; S055 is the
focused row C1 needs (opened today, `used-by` names the new knowledge file).

## 2. Entry row (`## Per-client record` of `corpus/knowledge/skill-listing-thresholds-round54.md`)

| VS Code | S055 | "help Copilot decide when to load the skill. Maximum 1024 characters." | `agent-skills.md:148` | An authoring maximum: the page states a `description` maximum of 1024 characters and no consequence, cut or budget past it. |

Quote is 11 words, verbatim inside line 148 of the fetched bytes
(`grep -c -F 'help Copilot decide when to load the skill. Maximum 1024 characters.' page.md` → 1,
exit 0), and the number appears exactly as the page writes it (`1024`, no comma).

## 3. Gate row (`corpus/lessons/round-54.md` § Gate)

| S055 | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 2026-10-22T21:15:47Z | 22,871 B, `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` | "help Copilot decide when to load the skill. Maximum 1024 characters." | `agent-skills.md:148` | SrcVSCode |

The quote string must stay byte-identical to the entry row's quote; the counter reads
double-quoted strings from `## Gate` rows whose first cell is an `S###` id
(`check_description_thresholds.py:204-221`).

## 4. Draft SKILL.md row (`### Description thresholds by client`)

| VS Code | `description` maximum 1024 characters (authoring maximum; `name` 64) | Not documented: the page states no truncation, drop, warning or refusal past 1024, and no listing budget | Keep the description under 1024 characters, leading with what the skill does and when to use it |

The threshold cell holds the tokens `1024` and `64`; the entry quote matches `1024`.

## Absence sweep for the two numbers VS Code does not document

The three-part Q30 sweep covers (a) release notes, (b) the current docs source tree,
(c) the lane corpus. The finding is only that these sources document no per-entry cut,
no listing budget and no past-the-cap behaviour for a `description`; it is not a claim
about the editor's compiled behaviour.

**(a) Release notes.** The markdown companion route does not exist for release notes:
`curl -sS -o rn-v1_143.md -w '%{http_code}' https://code.visualstudio.com/updates/v1_143.md`
→ `404` (also 404 for v1_142, v1_141), all three bodies byte-identical at 19,510 B
(sha256 `3c7efcaf106cf4615272e49727c964bc5d1888860dff2fff4cd33eb6c54c5e95`), so the HTML
was fetched instead. Counts over the fetched HTML:

```
v1_143 skill=1 1024=0 truncat=0
v1_142 skill=1 1024=0 truncat=1   # "even when the list truncates it" — background shell details
v1_141 skill=0 1024=0 truncat=0
```

The two skill mentions are a PR-list link ("agentHost: enable SDK skill installation",
v1_143) and a canvas-writing skill narrative (v1_142). No release note number limits a
description or the skill list.

**(b) Docs source tree.** `git clone --depth 1 --filter=blob:none --sparse
https://github.com/microsoft/vscode-docs.git` then `git sparse-checkout disable`, at
commit `fd64d64891a2e660bcc0d32ea402da905adfef7f`, 365 `.md` files under `docs/`:

```
grep -rn -i -E '1024|truncat|skill listing|skill list|list of skills' docs --include='*.md' | wc -l   -> 15
… same grep, filtered to skill/agent-customization paths                                                    -> 1 line: docs/agent-customization/agent-skills.md:159
grep -rn -i -E 'descriptions? (are |is )?(cut|shortened|trimmed)|cut off|shortened' docs/agent-customization docs/agents --include='*.md' -> 0
grep -rn -i -E 'up to [0-9]+ skills|[0-9]+ skills' docs --include='*.md'                                  -> 0
grep -rn -i -E 'exceed|longer than|too long|oversize|over the limit' docs/agent-customization docs/agents --include='*.md' -> 6
```

The one skill-related hit is the 1024 sentence itself (source line 159). The six
"exceed" hits are about model context windows, AI credits, hook compaction, session
cleanup, subagent cost tiers and the 128-tool cap — none about skill descriptions.

**(c) Lane corpus.** `grep -rn -i 'code\.visualstudio\.com' corpus/SOURCES.md` → three
rows (S025 skills page, S034 1.104 release notes, S047 custom instructions);
`grep -rn '1024' corpus/` → 19 lines in 7 files, and the only statements about this cap
are `corpus/knowledge/skill-selection-rules-round50.md` (records the cap at
`agent-skills.md:148` and "truncat 0" on the same text) and
`corpus/knowledge/sibling-overlap-census-round49.md:205` (same page, 22,871 B).
`grep -rn -i -E 'vs ?code|visualstudio' corpus/knowledge | grep -i -E 'truncat|listing budget|per-entry'`
→ 0 hits. No lane file claims a VS Code listing budget or a per-entry cut, so S055
contradicts nothing already admitted.

## Falsifier run (sandbox clone only)

Cloned the lane at `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` to
`/fast/scratch/hyaku/kotoba-r54/SrcVSCode/lane`, pasted the four rows above into the
sandbox copy (`corpus/SOURCES.md`, `corpus/knowledge/skill-listing-thresholds-round54.md`,
`corpus/lessons/round-54.md`, `SKILL.md`), and ran the frozen counter there:

```
python3 -B verifiers/check_description_thresholds.py --root . --json
  -> {"backed": 1, "of": 7, ...}   VS Code: row S055, backed true, tokens ["1024","64"], why []
  exit 1 (target 4 — expected with one client row present; no other client was attempted)

python3 -B verifiers/check_description_thresholds.py --root . --fetch
  -> "description thresholds backed 1 of 7 clients"
     "description thresholds found on the live page 1 of 1"
  exit 1

python3 -B verifiers/check_description_thresholds.py --self-test
  -> "self-test: 0 failure(s) over 22 assertions"   exit 0
```

So the row shapes satisfy every rule the counter applies to VS Code, including the
11-cell SOURCES row, tier/kind/status/opened/used-by, the pinned host, the 3-25-word
quote carrying the threshold token, and the quote's presence in the `## Gate` row and on
the live page. The counter was not run against the lane revision itself — the rows are
not integrated there, and I made no lane writes.

## Findings

1. VS Code's documented threshold is an **authoring maximum** on `description` (1024
   characters), not a listing cut and not a budget. The page's only model-facing
   statement is that Copilot reads `name` and `description` at discovery
   (`agent-skills.md:302`) and that "you can install many skills without consuming
   context" (`:308`) — no number for the list itself.
2. The page documents the consequence for the **name** field ("Names with invalid
   characters cause the skill to silently fail to load", `:147`) but attaches no
   consequence to the description maximum. Anyone who records "VS Code truncates at
   1024" would be recording an inference, not these bytes.
3. The description sentence is unchanged since the round-50 pin (same sha256), so S055
   adds no drift evidence; it adds a fresh open date and a description-scoped row.
4. `1,024` (comma form) does not appear on the page; the served bytes write `1024`, and
   the entry quote and SKILL.md threshold cell both use that form so the counter's token
   match holds.

## Out of scope / not done

- No lane file edited, no git or jj write in the lane, no push; no product code, judge,
  verifier or counter touched. The sandbox clone is the only place where writes happened.
- No client CLI invoked (no paid model call), no headless browser, no captcha solving;
  sources were opened with curl and plain HTTP reads (and one `git clone` of the public
  docs repository into scratch).
- No tool installed or upgraded; nothing in this task needed one.
- I did not test the editor's behaviour past 1024 characters; nothing here measures the
  binary, only what the vendor documents.

## Artifacts

- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/page.md` — served markdown, 22,871 B, sha256 `de5ba34f…`
- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/headers.txt` — response headers for that fetch
- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/src-page.md` — docs source file, 24,087 B, sha256 `bae0c84d…`
- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/rn-v1_141.html`, `rn-v1_142.html`, `rn-v1_143.html` — release notes used in sweep (a)
- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/docs-repo/` — microsoft/vscode-docs at `fd64d648`, full `docs/` checked out
- `/fast/scratch/hyaku/kotoba-r54/SrcVSCode/lane/` — sandbox clone at `7ad05d3` carrying the four rows and the counter runs above
