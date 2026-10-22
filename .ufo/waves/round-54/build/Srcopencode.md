Result: DONE — opencode documents exactly one number for a skill `description` (1-1024 characters, served v1 docs page), the rows below make opencode a backed client of the C1 counter in a sandbox run, and the source check shows neither shipped tree enforces or truncates it.

Seat: `KotobaR54.Srcopencode` (leaf, C1 client *opencode*, reserved SOURCES id S059). Lane read-only; the only lane file written is this report.

## 1. What opencode documents (the answer to item (1)–(5))

Numbers on the client's own docs, enumerated rather than sampled.

Served v1 page, `https://opencode.ai/docs/skills.md`, 200, 5,365 B, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f1bf8561`, fetched 2026-10-22T21:15:53Z. Every number-bearing line (`grep -nE "[0-9]" skills.md`):

- `skills.md:56` — `- Be 1–64 characters` (the `name` rule, not the description), with its regex at `:65` (`^[a-z0-9]+(-[a-z0-9]+)*$`)
- `skills.md:72` — `` `description` must be 1-1024 characters. ``
- `skills.md:227-231` — the five numbered troubleshooting steps (ordinals, not limits)

That is the whole set. The page documents **no listing budget, no per-entry cut in the skill listing, no truncation**. What it says the model sees is the full entry: `skills.md:110-111` "OpenCode lists available skills in the `skill` tool description. Each entry includes the skill name and description:", with the `<available_skills>` example at `:114-119`, and the only documented way to keep a skill out of the list is `metadata["opencode/autoinvoke"]` set to `"false"` (`:128-129`). A budget-word sweep over the fetched bytes returns nothing: `budget` 0, `truncat` 0, `shorten` 0, `limit` 0, `maximum` 0, `max ` 0.

Served V2 page (`https://opencode.ai/v2/docs/skills`, HTML only — the `.md` route answers 404) states the opposite for V2:

- `services/www/src/docs/content/skills.mdx:160` — "V2 currently does not enforce this pattern, the 1–64 character recommendation, a match between `name` and the directory, or a maximum description length."

So the number opencode documents (1024) is an **authoring maximum**, not a listing cut and not a budget, and the vendor itself says V2 does not enforce a maximum description length.

### Where the 1024 is enforced: nowhere in either shipped tree

- v1.19.4, tag `148842ef7cb1bc34192b3fff57d0f9721ab9c801`, `packages/opencode/src/skill/index.ts` (11,843 B, sha256 `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6`): `:39` `description: Schema.optional(Schema.String)`; `:53-57` `isSkillFrontmatter` tests `typeof data.description === "string"` and nothing else; `:332` renders `    <description>${skill.description}</description>` and `:344` renders `- **${skill.name}**: ${skill.description}` in the compact form. Grep for `1024` over `packages/opencode/src` at that tag returns 23 hits in 13 files (file-size conversions, compression threshold, `REASON_LIMIT` in an error middleware, tool-output truncation), and `git grep -n "1024" -- packages/opencode/src/skill` prints nothing and exits 1 — no 1024 in the skill path.
- v2.1.3, tag `bb25a2f4a3f3f04d7c344bec0c0574ea3510b3b1` — a published release (first entry in `releases.atom`, updated 2026-10-22T12:45:27Z, with its own tag page) that carries no Latest and no Pre-release badge; the releases page badges **v1.19.4** as Latest and lists it first, so which tag counts as "current" is not settled by those pages and I checked the skill source at both: `packages/schema/src/skill.ts:30` `description: Schema.String.pipe(optional)` — no `maxLength`; `packages/core/src/skill/instructions.ts:21` renders `    <description>${skill.description}</description>` inside `<available_skills>`; `:82-84` filters only on `description === undefined` and `autoinvoke === false`. `git grep -n "1024" -- packages/core/src packages/opencode/src` at that tag returns 30 hits, and over the skill paths (`packages/core/src/skill`, `packages/core/src/skill.ts`, `packages/schema/src/skill.ts`) it prints nothing and exits 1 — no 1024 in the skill path.

Reading for the entry: past 1024 characters opencode does nothing — no cut, no shortening, no drop, no warning, no refusal; the whole string goes into the listing. The documented number is a portability rule (the Agent Skills spec states the same 1-1024, `corpus/SOURCES.md` S001), not a load-time check.

### Served page versus docs source

The served bytes are line-identical to the docs source at tag v2.1.3: after dropping the mdx frontmatter and substituting `${name}` → `name`, the served text and `packages/web/src/content/docs/skills.mdx` have **131 non-blank lines each and 0 differing lines** (`difflib.unified_diff`, 0 output lines). [INFERENCE] the site is built from that file, since equality of bytes is what is observed; what is not in doubt is that the served page is the *v1* page, and the same tag also ships the V2 page that disowns the rule. The V2 HTML carries the same prose as `services/www/src/docs/content/skills.mdx`; code-element boundaries insert a space before terminal punctuation when rendered ("…to false ."), a markup artifact and not a wording difference.

## 2. Item (1) — SOURCES.md rows (single physical lines, 11 cells each)

```
| S059 | opencode — Agent skills (served docs) — https://opencode.ai/docs/skills.md | docs | A | What opencode's served v1 skills page states as the length rule for a skill's `description` (vendor documentation, not a measurement of enforcement) | § Follow length rules `skills.md:70-73`, the rule at `:72`; what the listing shows `skills.md:108-129`; fetched 2026-10-22T21:15:53Z (200, 5,365 B, sha256 `f10ced73…`), byte-identical to the S024 and S039 fetches; 0 differing lines from `packages/web/src/content/docs/skills.mdx:77` at tag v2.1.3 | The page's Follow length rules section states that `description` must be 1-1024 characters | mined | 2026-10-22 | 90d | corpus/knowledge/skill-listing-thresholds-round54.md |
```

```
| S059b | opencode — Agent skills, V2 docs page — https://opencode.ai/v2/docs/skills | docs | A | What opencode's V2 docs page states about enforcing a skill `description` length (vendor documentation for that page; not a measurement of the artifact) | § IDs, the enforcement sentence at `services/www/src/docs/content/skills.mdx:160`; § Frontmatter `:140`; § Loading `:184`; served as https://opencode.ai/v2/docs/skills (200, 32,694 B, sha256 `243e8890…`) on 2026-10-22T21:16:53Z; the `.md` route answers 404 | V2 does not enforce a maximum description length | mined | 2026-10-22 | on-release | corpus/knowledge/skill-listing-thresholds-round54.md |
```

Notes the L1 needs: (a) the highest id at the tip `7ad05d34` is S052 (`grep -oE '^\| S[0-9]{3,}' corpus/SOURCES.md | sort -u | tail -1` → `S052`), so S059 and S059b are ahead of the sequence and need the renumber the assignment anticipated; (b) the registry census still passes shape rules — `awk -F'|' '… NF!=13' corpus/SOURCES.md` → `0` malformed at the tip, and both rows above parse to 13 pipe fields / 11 cells (`len(line.split("|"))` on the lines in this report), the S059 one also having gone through the counter in the sandbox fixture; (c) `used-by` names the C1 entry, which did not exist at the tip when I finished (`ls corpus/knowledge/skill-listing-thresholds-round54.md` → absent) — the row goes live only with that entry.

## 3. Item (2) — fetch records

| what | URL | opened (UTC) | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| served v1 skills page | https://opencode.ai/docs/skills.md | 2026-10-22T21:15:53Z | 200 | 5,365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f1bf8561` |
| served V2 skills page (HTML) | https://opencode.ai/v2/docs/skills | 2026-10-22T21:16:53Z | 200 | 32,694 | `243e88907fcbf35a7ae7dfc99e7c772e1a50fe40632091e4c6b328f1619f1318` |
| v1 docs source | https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/web/src/content/docs/skills.mdx | 2026-10-22T21:17:50Z | 200 | 5,462 | `39548bda09fc936c42cabf232472a4d92b5ed7133ed7762db19cef970df7dd4a` |
| V2 docs source | https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/services/www/src/docs/content/skills.mdx | 2026-10-22T21:17:50Z | 200 | 9,187 | `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b` |
| v1.19.4 skill source | https://raw.githubusercontent.com/anomalyco/opencode/v1.19.4/packages/opencode/src/skill/index.ts | 2026-10-22T21:19:35Z | 200 | 11,843 | `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6` |
| v2.1.3 skill listing renderer | https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/core/src/skill/instructions.ts | 2026-10-22T21:19:35Z | 200 | 4,089 | `ee6b644ca849292f68fdfae7c6ab1d3f02b46e9050757ff4a7cb976199ccc60e` |
| v2.1.3 skill schema | https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/schema/src/skill.ts | 2026-10-22T21:19:36Z | 200 | 2,476 | `da003f8a6fd607569adb11e789c08eede92b044faa87648c422e69b47e281b4c` |
| release feed | https://github.com/anomalyco/opencode/releases.atom | 2026-10-22T21:22:44Z | 200 | 6,758 | `5d050363ba74e9b441a41de9c81ec34b39a9df91952e1e40d720052ff3a6fe1a` |
| release list (Latest badge) | https://github.com/anomalyco/opencode/releases | 2026-10-22T21:22:45Z | 200 | 503,395 | `9170d25f4b4969596ff2f9ac22c1f34cc366f0f4eadf09b539f49e004ccd7982` |
| release page v2.1.3 | https://github.com/anomalyco/opencode/releases/tag/v2.1.3 | 2026-10-22T21:22:46Z | 200 | 199,056 | `8f8f734facfec1a8ba14e19da533faf08162a45bd38d3a5070d5bc66652431ce` |
| release page v1.19.4 | https://github.com/anomalyco/opencode/releases/tag/v1.19.4 | 2026-10-22T21:22:46Z | 200 | 194,681 | `4ac6b1decfa5f15cec30d17a61438d1f66b724f6d868fe565b461873c0d81594` |
| tag list | `git ls-remote --tags https://github.com/anomalyco/opencode` | 2026-10-22T21:16Z (seconds not recorded) | — | — | — |

Honesty notes on the records: the two mdx files and the three code files were first read a minute or two before the stamps above, without a timestamp captured; I re-fetched them to record the access properly and the bytes are the same (the code hashes equal `git show <tag>:<path> | sha256sum` from the blobless clones, so the re-fetch and the tag content agree). The tag-list row is a `git ls-remote` output, not a page, so it carries no hash; every other row was fetched by plain HTTP and hashed from the bytes saved. Every quoted string below comes from the bytes listed here; the S059 quote was checked against the live page by the counter's `--fetch` run in §7, and the S059b quote by a normalized-substring probe on the fetched V2 HTML (found, `True`).

## 4. Item (3) — entry row for `corpus/knowledge/skill-listing-thresholds-round54.md` § Per-client record

```
| opencode | S059 | "`description` must be 1-1024 characters." | `skills.md:72` | An authoring maximum, not a listing cut and not a budget: the page states the number under Follow length rules and documents no consequence past it, neither shipped tree enforces it, and V2's own page says V2 enforces no maximum description length, so an over-long description is rendered whole rather than cut, shortened or refused. |
```

The quote is 5 words (`description` / must / be / 1-1024 / characters.) and holds the number exactly as the page writes it, `1-1024`.

## 5. Item (4) — Gate rows for `corpus/lessons/round-54.md` § Gate (round-53 header shape)

```
| S059 | https://opencode.ai/docs/skills.md | 2026-10-22T21:15:53Z | 5,365 B, `f10ced73971c…` | "`description` must be 1-1024 characters." | `skills.md:72` | Srcopencode |
| S059b | https://opencode.ai/v2/docs/skills | 2026-10-22T21:16:53Z | 32,694 B, `243e88907fcb…` | "V2 currently does not enforce this pattern, the 1–64 character recommendation, a match between `name` and the directory, or a maximum description length." | `services/www/src/docs/content/skills.mdx:160` | Srcopencode |
```

The S059b quote is 23 words and contains no number that a threshold cell could rest on, so S059b is evidence for the "past the threshold" cell, never the counted row: the entry's `row` cell must stay `S059` alone (the counter demands exactly one `S###` there).

## 6. Item (5) — draft SKILL.md row for `### Description thresholds by client`

```
| opencode | 1-1024 characters (v1 docs page; the v2 page says it enforces no maximum) | nothing: no cut, truncation, warning or refusal — both shipped trees print the whole string into `<available_skills>` (v1.19.4 `skill/index.ts:332`, v2.1.3 `skill/instructions.ts:21`) | keep the description inside 1-1024 characters, the rule the spec states too (S001), and front-load it, because opencode shows all of it |
```

## 7. Counter conformance and falsifier runs (sandbox only)

Sandbox: `unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r54/Srcopencode/lane; git -C lane checkout -q 7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` → HEAD `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`, clean. (Deviation to record: the clone sits in a `lane/` subdirectory of my seat scratch root because that root already held the fetched bytes; nothing on the host outside `/fast/scratch/hyaku/kotoba-r54/` was written.)

Into that clone only, I pasted the four pieces above (SKILL.md table row, entry file with the one row, a `## Gate` table with the S059 row, and the S059 SOURCES row) and ran the declared counter:

```
python3 -B verifiers/check_description_thresholds.py --root .
  opencode: "row": "S059", "url": "https://opencode.ai/docs/skills.md", "quote": "`description` must be 1-1024 characters.", "tokens": ["1","1024","1","2"], "backed": true, "why": []
  description thresholds backed 1 of 7 clients
  exit=1        (target is 4; the other six clients are other seats' rows)
```

Live-page measurement:

```
python3 -B verifiers/check_description_thresholds.py --root . --fetch
  opencode     BACKED found=True
  description thresholds found on the live page 1 of 1
  exit=1
```

Two negative runs, each a copy of that sandbox clone:

```
neg/  entry quote 1-1024 → 1-9999 and the SOURCES row opened 2026-10-22 → 2026-10-21
  opencode     no S059 opened '2026-10-21'; round-54 Gate does not record this quote for S059
  description thresholds backed 0 of 7 clients
  exit=1
```

```
neg2/ SKILL.md cell, entry quote and Gate quote all moved 1-1024 → 1-9999, consistently
  opencode     BACKED found=False
  description thresholds found on the live page 0 of 1
  exit=1
```

Finally the blocks exactly as written in sections 2, 4, 5 and 6 were re-extracted from this report and pasted into a fresh clone (`exact/`, HEAD `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39`) with no retyping:

```
python3 -B verifiers/check_description_thresholds.py --root . --fetch
  opencode     BACKED found=True
  description thresholds backed 1 of 7 clients
  description thresholds found on the live page 1 of 1
  exit=1
```

and the registry census on the same tree keeps the shape: 53 rows, malformed 0, duplicate ids 0, one `S059` row and one `S059b` row. So the delivered text, not a paraphrase of it, is what the counter accepted.

## 8. Findings

F1. **The declared C1 run cannot catch a fabricated number; `--fetch` can.** In `neg2` the SKILL.md cell, entry quote and Gate quote agreed on `1-9999`, and the counter printed `opencode     BACKED found=False` — the row passed every file-level rule (that is what `BACKED` reports) and only the live-page check rejected it (`found on the live page 0 of 1`, exit 1). The reason the file-level rules pass: token containment is satisfied by any token of the threshold cell, and a cell `1-9999 characters` yields the token `1` as well as `9999` (`NUM_RE` splits the range), so a wrong number on the left of the hyphen still carries a matching token. `corpus/knowledge/skill-listing-thresholds-round54.md` should therefore carry the `--fetch` reading beside the declared one, as the plan already intends.

F2. **The number opencode documents is not the number opencode enforces.** Served page says `must be 1-1024 characters`; v1.19.4 has no such check at `skill/index.ts:39,53-57`; v2.1.3 has none at `packages/schema/src/skill.ts:30`; and the V2 page says so in words (`skills.mdx:160`). This is consistent with the round-53 spot-check's reason for rejecting this same page as a standalone row (`corpus/lessons/round-53-verifier-spotcheck.md:133`: "documents rules 1.19.3 does not enforce"). The S059 `scope` cell above therefore says "vendor documentation, not a measurement of enforcement", and the entry's reading cell says the limit is unenforced — a reviewer who wants a stricter reading has the two source anchors.

F3. **The served page is not stale; the rule is version-scoped.** The served `.md` is line-identical to `packages/web/src/content/docs/skills.mdx` at tag v2.1.3 (0 differing lines after frontmatter and `${name}` substitution) [INFERENCE that the site is built from that file], i.e. opencode still ships the v1 page, while the same tag ships the V2 page that drops the rule. Anyone reading `opencode.ai/docs/skills` today is reading v1 documentation. That matters for every "pass the threshold" statement about this client: on v2 nothing happens at all, and on v1 the docs state the rule but the artifact does not apply it.

F4. **No listing budget or per-entry cut exists to find, and the sweep proves it on three fronts.** (a) Release notes: `git show HEAD:CHANGELOG.md` at v2.1.3 is 554 lines with three `skill` mentions (`:168,253,434`, none about description length) and one hit for `1024|description length|truncat` (`:310`, an output-token/tool-call sentence), exit 0 for the grep; `releases.atom` (6,758 B) has zero `skill|description` hits, grep exit 1. (b) Docs source trees: `git grep -niE "available_skills|skill.{0,20}budget|skill.{0,20}truncat"` over `services/www/src/docs/content` and `packages/web/src/content/docs` returns only the `<available_skills>` examples (v1 page and its translations), no budget wording; `grep -niE "budget|truncat|shorten|1-1024"` on the V2 mdx is empty, exit 1. (c) Lane corpus: 8 prior lines touch opencode plus truncation/budget/1024, all saying the same thing in different rounds (`corpus/knowledge/claim-scope-audit-round9.md:23,24,37`, `opencode-offer-trace-round8.md:180`, `harness-router-models-round9.md:171,175`, `sibling-overlap-census-round49.md:202` "`1024` 1 (the description cap…"), plus the Codex-only `frontmatter-rule-authorities-round48.md:51`). So "no listing budget documented" is a checked negative, not a silence.

F5. **What does limit the listing is a flag, not a number.** Both pages document `metadata["opencode/autoinvoke"]: "false"` (v1 `skills.md:128-129`; V2 `skills.mdx:137,142`) and V2 adds `disable-model-invocation: true` (`:138`) plus "skills without [a description] are not advertised" (`:140`). An author who needs to keep a skill out of the model's view has a documented switch; there is no length lever besides the advisory 1024.

F6. **Id bookkeeping.** The tip holds 52 SOURCES rows (S001–S052, 0 malformed by the contract census), so S059/S059b are not the next free ids; the L1 renumbers as the assignment states, and the two rows above must keep their internal pairing (entry row `S059`, Gate row `S059`) through that renumber.

## 9. Bounds compliance

- Lane files: none edited by me. When I first checked the lane, `git status --porcelain` showed only the untracked `.ufo/waves/round-54/` directory that holds this report; at the end of my run the same command also showed `M SKILL.md`, `M corpus/README.md` and `?? verifiers/check_sources_append_only.py` — concurrent seats' work, not mine (`git diff --stat SKILL.md corpus/README.md` → 34 insertions; no `### Description thresholds by client` heading was present yet). No `add`, `commit`, `checkout`, `stash`, `reset`, `pull`, `push` or `worktree` ran in the lane, and no jj command ran anywhere.
- Writes: this report at `.ufo/waves/round-54/build/Srcopencode.md`, plus fetched bytes and the fixture clone under `/fast/scratch/hyaku/kotoba-r54/Srcopencode/`.
- No subagents, no `task`, no swarm, no model parameter, no `ask`, no client CLI invoked (nothing ran `opencode` at all), no headless browser, no captcha or access-control bypass (plain `urllib` GETs with a curl user agent).
- No installs or upgrades this round, so nothing to record under the tooling directive.
- Negative-claim rule (Q30) satisfied for every "documents nothing" statement above: changelog/release notes, docs source tree, and lane corpus grep, each with its command and result.

## 10. Out of scope, not done here

- The C1 entry body, the SKILL.md table and its placement, the lesson § Gate insertion, the SOURCES renumber: L1 integration.
- C2 (gate registry) rows and any verifier change: other seats; I ran no lane verifier against the lane tree.
- No statement about whether any model actually consumes the full description at request time — the render is shown, the model's attention is not measured; `corpus/knowledge/harness-router-models-round9.md:175` already carries that caveat.
- No freshness work, nothing on `verifiers/verify_surfaces.py`, nothing on the executed-checklist or always-on-box frontier.

## 11. Artifacts

- Report: `.ufo/waves/round-54/build/Srcopencode.md` (this file)
- Fetched bytes: `/fast/scratch/hyaku/kotoba-r54/Srcopencode/skills.md`, `v2-skills.html`, `v2-skills.txt`, `a.mdx` (v1 docs source), `b.mdx` (V2 docs source), `skill-v1.19.4.ts`, `rel.atom` / `rel2.atom` (byte-identical), `rel2.html`, `r2-v2.1.3.html`, `r2-v1.19.4.html`, `CH.md`
- Sandbox clone and fixtures: `/fast/scratch/hyaku/kotoba-r54/Srcopencode/lane` (conformant), `neg` (stale date + wrong number), `neg2` (consistent fabricated number)
- Blobless source clones: `/fast/scratch/hyaku/kotoba-r54/Srcopencode/oc-v2.1.3` (HEAD `bb25a2f4a3f3f04d7c344bec0c0574ea3510b3b1`), `oc-v1.19.4` (HEAD `148842ef7cb1bc34192b3fff57d0f9721ab9c801`)
