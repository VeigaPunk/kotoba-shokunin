verdict: S003 still-holds — the `.md` source is byte-identical to the round-46 fetch (sha256 `727f3fa1…`) and the description field still reads "Cannot contain XML tags" at `best-practices.md:162`; no status/recheck change is warranted, one conditional `used-by` update and two evidence-record defects are reported.

# S003 — frontier re-open, round 47

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (verified `git rev-parse HEAD`, rc 0).
Row under test: `corpus/SOURCES.md:16`. Contract: fleet `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (rules at :32–:40, :49–:51).
Fetch record: `.ufo/waves/round-47/build/SrcS003.json` (6,440 B, metadata + ≤25-word quotes only; no page bytes copied into the lane).

## Fetch (all times true UTC from `date -u`)

| surface | HTTP | content-type | bytes | sha256 | accessed_utc |
|---|---|---|---|---|---|
| `…/agent-skills/best-practices` (rendered) | 200 | `text/html; charset=utf-8` | 1,178,651 | `f7637bb4acb408bd7816c9e5c231ad685e1bfd5ff20549dce639f2d4ef6d7b6c` | 2026-10-21T15:54:10Z |
| `…/best-practices.md` (source) | 200 | `text/markdown; charset=utf-8` | 42,028 | `727f3fa1168eb1c33ce6a3cbfc94a02ef1dfd647388f6ca9daf7cb6294762f42` | 2026-10-21T15:54:11Z |
| `…/best-practices.txt` (negative control) | 200 | — (header not captured; body HTML) | 142,540 | `8e4856731a53c3532f50f23ef61cc8a3d0ddf7a50898b41895309e44b4430b49` | 2026-10-21T15:54:11Z |

**Freshness, strongest available signal:** the `.md` sha256 equals the round-46 fetch record's sha256 verbatim
(`.ufo/round-46/evidence/w2/sources/fetch-log.json` `/rows/2`: `727f3fa1…`, accessed 2026-10-19T18:40:54Z).
Zero byte drift across two days, so no diff-vs-2026-10-19 is needed or possible to improve on. An independent
peer fetch in this same wave (`.ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md`) hashes
identically — two seats, same bytes.

**Counterexample worth keeping:** `.txt` returns **HTTP 200 with a Next.js error body**
(`id="__next_error__"`, 142,540 B). A status-only fetch check would have accepted an error page as content;
only `.md` and the rendered HTML carry the rules. (Recorded in the JSON `negative-control-txt`.)

## Still holds — evidence at the fetched bytes

Quote (21 words), location `best-practices.md:159–163` — the `description` bullet list inside the
"YAML Frontmatter" note under `## Skill structure` (md:146, rendered anchor `#skill-structure`; HTML
byte offset ~149479):

> "Must be non-empty … Maximum 1,024 characters … **Cannot contain XML tags** … Should describe what the Skill does and when to use it"

- XML ban, name field (control): md:155 "Cannot contain XML tags"; reserved words md:156.
- Third person: md:206 "**Always write in third person**. The description is injected into the system prompt…" (heading `### Writing effective descriptions`, md:201). Quote 5 words.
- What + when: md:203 and md:163.
- 500-line rule: md:257 "Keep SKILL.md body under 500 lines for optimal performance"; restated md:1140; checklist md:1150.
- Restatement in Technical notes: md:1134 "`description`: Maximum 1,024 characters, non-empty, no XML tags".
- Anchor: row's "§ Skill structure field list" resolves — h2 `Skill structure` (md:146), rendered id `skill-structure`; sibling ids `naming-conventions`, `writing-effective-descriptions` also present.

Every clause this page must supply is present at BASE: the XML-tag ban, the third-person rule, what+when,
and the 500-line guidance. The cross-source tail of the cell ("the open spec lacks") is treated in D2.
No old→new content change is required.

## Recommended row changes (contract rule 2 admits only these three fields)

| field | old | new | recommendation |
|---|---|---|---|
| `status` | `mined` | `mined` | **no change** — cited by `SKILL.md`; stays `mined` |
| `recheck` | `90d` | `90d` | **no change** — next due 2027-01-19 from this re-open (2027-01-17 from `opened` 2026-10-19) |
| `used-by` | `SKILL.md` | `SKILL.md, verifiers/verify_skill_checklist.py` | **conditional** — apply only when C2's description XML-tag check actually lands in that file; log old→new in `corpus/lessons/round-47.md` per rule 2 |

Census-safety of the `used-by` addition: contract requires every `used-by` path to exist
(`SOURCES-CONTRACT-v1.md` census tail); `verifiers/verify_skill_checklist.py` exists at BASE.
Literal-contract caveat: :40 says `used-by` holds "knowledge entries or lessons", and both the current
`SKILL.md` and the proposed verifier path are neither — the registry already uses the broader reading.
If the L1 wants to stay literal, use `corpus/lessons/round-47.md` instead once that lesson exists.

`opened`, `anchor`, `teaches`, `tier`, `kind`, `scope` are **not** mutable in place (rule 2, :49–:51);
no recommendation touches them.

## Defects found (calibration; neither falsifies the row)

**D1 — the round-46 evidence pair is field-inverted.** `fetch-log.json` `/rows/2` `quote_location` says
"description rules (claude-bp.md line 155; name field repeats it line 162)"; `corpus/lessons/round-46.md:65`
repeats it. At the byte-identical source, md:155 is the **name** bullet and md:162 is the **description**
bullet (`:158` `description:`, `:161` Maximum 1,024, `:162` XML ban). The row's `teaches` is right; the
citation attribution is backwards. Lessons are append-only, so the correction belongs in the round-47
lesson's `## Gate`, not as an edit.
`corpus/lessons/round-46.md:77`'s re-open ("lines 155 and 162") is unordered and therefore still true.

**D2 — `teaches` closing clause can be read as false.** `corpus/SOURCES.md:16` ends
"…body under 500 lines; an Anthropic-only rule the open spec lacks". The open spec **does** carry the
500-line rule: `agentskills.io/specification.md:237` "Keep your main `SKILL.md` under 500 lines. Move
detailed reference material to separate files." (fetched 200, 7,608 B, sha256 `9a67de89…`).
What the spec lacks is the XML ban and the third-person rule — `grep -c -i xml` → 0 (rc 1);
`grep -c -i "third person\|third-person"` → 0 (rc 1); its `description` bullets are md:99–103
(1–1024 chars, what+when, keywords). So "an Anthropic-only rule" is true only for the XML/third-person
clause, but its position after "body under 500 lines" lets it deny a rule the spec has.
Rule 2 forbids in-place `teaches` edits: either accept the reading and record the clarification in the
round-47 lesson, or open a `supersedes S003 —` row whose text separates the two (recommended wording:
"…; the XML-tag ban and the third-person rule are Anthropic-only — the open spec's description rules at
`specification.md:99–103` carry neither, while its 500-line guidance at `:237` matches").
`corpus/lessons/round-46-verifier-spotcheck.md:12` already adjudicates the XML rule as vendor-specific — consistent.

## Operability notes for C2 (measured at BASE)

- `SKILL.md:3` opens `description: >` (folded block scalar) and the frontmatter closes at `SKILL.md:16`;
  `<skills>` sits inside the description at **`SKILL.md:14`** ("never reach the `<skills>` router").
- Whole-file `grep -c '<skills>' SKILL.md` → **8**; frontmatter-only → **1**. A check that greps the file
  instead of the parsed `description` will not distinguish the C2 target from body prose (lines 22, 91…).
  `verifiers/verify_skill_checklist.py:1176` (`check_frontmatter`) already holds the parsed field dict at
  `:1177`, so the rule can key off the unquoted value with no new parser.
- Tag shape: the source rule bans XML tags, not the bare `<` character. `[INFERENCE]` match
  `<[A-Za-z/!?][^>]*>` on the parsed value so `a < b` prose and the angle-bracket-free rest of the
  description stay green; the planted failing control is precisely `<skills>`.
- The description is folded (`>`), so line-splitting mid-sentence (`skill's\n  reference/`) must not be
  treated as tag boundaries — evaluate on the folded string.
- Cross-check against the in-wave draft (peer artifact `.ufo/waves/round-47/build/C2SkillRewrite.patch`,
  537 B, **not** production): it replaces "never reach the `<skills>` router" with "never reach the omp
  skill catalogue router". `SKILL.md:3–15` contains exactly one `<` (line 14), so the parsed-description
  check flips 1 → 0 on that patch alone, and the rewritten text still satisfies S003's third-person
  (md:206) and what+when (md:163) clauses — C2 introduces no new S003 violation.

## Commands run (exit codes, key output)

| command | rc | key output |
|---|---|---|
| `git rev-parse HEAD` | 0 | `c61a973b2e02e1ded169703ddcb06466f4edd8bd` |
| `curl -sS -L … best-practices` (html) | 0 | `http_status=200 size=1178651 content_type=text/html; charset=utf-8` |
| `curl -sS -L … best-practices.md` | 0 | `md_http=200 md_size=42028 md_type=text/markdown; charset=utf-8` |
| `curl -sS -L … best-practices.txt` | 0 | 200, 142540 B, body `id="__next_error__"` |
| `sha256sum page.html best-practices.md best-practices.txt` | 0 | `f7637bb4… / 727f3fa1… / 8e485673…` |
| `grep -n -i "xml tags\|third person\|500 lines\|1,024" best-practices.md` | 0 | 155, 161, 162, 206, 257, 1133, 1134, 1140, 1150 |
| `curl -sS -L … agentskills.io/specification.md` | 0 | 200, 7608 B, `9a67de89…` |
| `grep -c -i xml spec_specification.md` | 1 | `0` |
| `grep -c -i "third person\|third-person" spec_specification.md` | 1 | `0` |
| `grep -n "500" spec_specification.md` | 0 | `:237 Keep your main SKILL.md under 500 lines` |
| `grep -c '<skills>' SKILL.md` / frontmatter-only | 0 / 0 | `8` / `1` |
| `sha256sum .ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md` | 0 | `727f3fa1…` (peer copy identical) |
| `python3 -c 'json.load(SrcS003.json)'` | 0 | `json ok`, 16 keys, 6,440 B |

No tools installed or upgraded this round (nothing was needed). No pacman transaction attempted.

## What I did NOT check

- No Wayback/archive diff: byte identity with the round-46 record already bounds drift to zero.
- Did not run `verifiers/verify_skill_checklist.py` or any lane gate — not named in this item, and the
  production tree is read-only to me.
- Did not open the linked `agent-skills/overview#skill-structure` page; only this page's own restatements
  (md:165, md:1136) point at it.
- Did not test whether any client actually enforces the XML ban or third-person rule at load time — the
  source states the rule; enforcement is out of scope here.
- Did not inspect the rendered HTML beyond the queried rule regions (byte offsets 149479, 473159, 799519),
  so a change elsewhere on the page would not have been noticed — but the identical `.md` digest rules
  that out for the whole document.
