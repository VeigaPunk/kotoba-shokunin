# C2ClaudeDocs — Anthropic docs authority for SKILL.md `name`/`description` rules (round-48 build, attempt 2)

Scout seat `KotobaR48.C2ClaudeDocs`. Question: for `name` and `description`, which Anthropic
authority imposes which rule, at what exact wording, and how that differs from the agentskills.io
spec and from S003's recorded teach (`corpus/SOURCES.md:16`). Read-only on the lane; this file is
the only lane write. No tool installed or upgraded. No fetched code executed.

## Findings

**F1 — S003 carries the full pair, twice.** Primary: `best-practices.md` § Skill structure, the
"YAML Frontmatter" Note (`bp.md:148-165`). `name`: "Maximum 64 characters" / "Must contain only
lowercase letters, numbers, and hyphens" / "Cannot contain XML tags" / "Cannot contain reserved
words: \"anthropic\", \"claude\"". `description`: "Must be non-empty" / "Maximum 1,024 characters" /
"Cannot contain XML tags" / "Should describe what the Skill does and when to use it". Second
statement § Technical notes → "YAML frontmatter requirements" (`bp.md:1129-1134`) drops the
reserved-word examples ("no reserved words"). The overview page repeats the same six bullets under
§ Skill structure (`ov.md:208-223`). Third person lives in § Writing effective descriptions
(`bp.md:206`), the 500-line body in § Progressive disclosure patterns (`bp.md:257`); neither is in
the field list.

**F2 — S003's `.md` endpoint is not byte-stable, and it moved inside one day.** Round-47 pinned
`727f3fa1…` / 42,028 B (retained at `.ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md`);
today 2026-10-22T08:12:08Z the same URL is `f0a5d61b…` / 42,169 B. The diff is 32 hunks, 79
insertions / 79 deletions, every one a copy edit (link labels "Skills overview" → "Agent Skills",
backticks around `SKILL.md`, "like these" → "such as these", "at a glance" → "from its name").
**No rule line changed**: region diffs over `145-170` and `1100-1191` differ only in the "For
complete Skill structure details…" link line and backticks, so the six rule bullets, the
third-person warning and the 500-line sentence are byte-identical at both shas. Calibration that
this is drift, not method: same route (`x-middleware-rewrite:
/docs/as-markdown/en/agents-and-tools/agent-skills/best-practices`), `-L` and no-`-L` fetches
byte-identical, and round-47's own controls showed round-46 == round-47 for this URL. So the page
was edited between 2026-10-21 and 2026-10-22, and any "re-open by recorded sha256" recheck of S003
false-alarms by construction; the 90d cadence understates this page's churn.
`agentskills.io/specification.md` did **not** move: `9a67de89…` today = round-47's value.

**F3 — Claude Code's skills doc is a separate authority with rules no other authority states.** It
follows the open standard but documents its own enforcement: all fields optional, only
`description` "Recommended" (`cc.md:381`); a name is refused for hidden, direction-changing or
blank-like characters, `<` or `>`, or "over 256 characters" (`errors.md:5388`) — a 256 cap, not 64;
no lowercase/hyphen charset rule for the name value at all; the frontmatter `name` **overrides**
the directory name while the directory name also invokes the skill (`cc.md:431`), the opposite
direction from the spec's "Must match the parent directory name"; angle brackets in the description
are escaped, not refused ("Claude Code sanitizes the display text the skill supplies, such as its
description", `cc.md:295`); the listing truncates "the combined `description` and `when_to_use`
text … at 1,536 characters" (`cc.md:389`); and packaging / claude.ai / Skills API paths hard-fail
on keys outside the spec's six fields — "Allowed properties are: allowed-tools, compatibility,
description, license, metadata, name" (`cc.md:423`) — while Claude Code itself ignores unknown
fields without error (`cc.md:381`). `SOURCES.md` has **no row** for `code.claude.com/docs/en/skills`;
round-47 cited it only as a cross-check in SrcNewAnthropicPlatformSkills.

**F4 — the Skills API guide is a fourth Anthropic authority, and the API error path a fifth.**
`skills-guide.md` § Managing custom Skills → Creating a Skill → **Requirements** (`:2258-2261`) and
§ Limits and constraints → Request limits (`:3549-3550`) state "`name`: Maximum 64 characters,
lowercase letters/numbers/hyphens only, no XML tags, no reserved words (\"anthropic\", \"claude\")"
and "`description`: Maximum 1,024 characters, non-empty, no XML tags". § Error handling adds the
failure mode: "A request that fails because of a Skill problem returns HTTP 400. The `error.message`
field in the JSON response body describes the problem." The directory-match rule there is
**beta-only**: the migration table's beta column reads "Files must sit inside a top-level directory
whose name matches the Skill `name`", the current column reads "`SKILL.md` may sit at the root of the
upload". Round-47 rejected this page as "no upload rejection" and its drafted row never landed; the
Requirements list is an upload precondition, so that rejection rationale is at least half wrong. The
guide also drifted since round-47 (recorded `76a440b2…` / 144,610 B → today `15b7cf01…` / 145,336 B),
and round-47's literal quote of the description bullet read "Maximum 1024 characters" where today's
bytes read "1,024"; the old bytes were not retained (`/fast/scratch/kotoba-r47` is gone), so that is
**[INFERENCE]** a numbering copyedit, not a rule change.

**F5 — per-authority rule matrix (C2 entry content; the lane-checker column is the
`trigger.no_xml_tag` seat's measurement, not asserted here).**

| rule | S001 spec | S003 + overview (Anthropic docs) | Claude Code skills doc | Skills API guide (upload) |
|---|---|---|---|---|
| `name` required | Yes | Yes ("Required fields: `name` and `description`") | No ("All fields are optional") | implied by bundle |
| `name` length | Max 64 chars | Maximum 64 characters | no cap stated; refused over 256 chars | Maximum 64 characters |
| `name` charset | a-z 0-9 hyphen; no leading/trailing; no `--` | lowercase letters, numbers, hyphens | none stated; hidden / direction-changing / blank-like and `<`/`>` refused | lowercase letters/numbers/hyphens only |
| `name` = parent dir | "Must match the parent directory name" | not stated | no — `name` overrides the directory name | beta upload layout only; current: root OK |
| `name` reserved words | none | "anthropic", "claude" | only the `anthropic-skills` namespace and folder name `synced` | "anthropic", "claude" |
| `name` XML tags | none | Cannot contain XML tags | `<`/`>` refused in a name | no XML tags |
| `description` required | Yes | Yes, non-empty | Recommended; falls back to the body's first non-empty line | non-empty |
| `description` length | Max 1024 chars | Maximum 1,024 characters | no cap; listing truncates description+`when_to_use` at 1,536 | Maximum 1,024 characters |
| `description` XML tags | none (0 occurrences of xml/tag on the page) | Cannot contain XML tags | angle brackets escaped, not refused | no XML tags |
| `description` voice | none | "Always write in third person" | none | none |
| body length | "Keep your main `SKILL.md` under 500 lines." | "Keep the `SKILL.md` body under 500 lines for optimal performance." | none | none |
| unknown keys | not addressed | not addressed | ignored locally; hard error on packaging/upload | six fields only |

**F6 — against S003's recorded teach (`corpus/SOURCES.md:16`).** Holds: description XML tags, third
person, "states what the skill does and when", 500-line body. Wrong: the cell's "an Anthropic-only
rule the open spec lacks" cannot cover the 500-line body (`spec.md:237` states it too — round-47 D2)
or the 64/1024 caps (the spec has both). Incomplete: the same page's `name` rules (64 chars, charset,
XML tags, reserved words) and the description 1,024 cap are absent from the cell, and the anchor
"§ Skill structure field list" is loose — the field list is a Note inside § Skill structure, and the
page states the pair a second time under § Technical notes. S001's recorded anchor defect
(§ "Skill metadata table" names no heading; real headings are `### Frontmatter`, `#### name field`,
`#### description field`) reconfirmed on today's bytes.

## Evidence

Fetches, `curl -sS`, 2026-10-22, all HTTP 200, `content-type: text/markdown; charset=utf-8`, origin
`date:` header 08:12:08-08:12:10 GMT; scratch `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2ClaudeDocs/src/`:

| url (`.md` reader route) | bytes | sha256 |
|---|---|---|
| platform.claude.com/…/agent-skills/best-practices.md | 42,169 | `f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` |
| platform.claude.com/…/agent-skills/overview.md | 21,840 | `7913d4556c014c6bf7f23e186efded1b36da63d7b29d73898267ebe8d2f6258f` |
| code.claude.com/docs/en/skills.md | — | `cdfcb0df93072710866de536ba823c06a0804038d488cd27a2ba48ad114cd456` |
| agentskills.io/specification.md | — | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` |
| platform.claude.com/…/build-with-claude/skills-guide.md | 145,336 | `15b7cf010a1ec5ac532c27e7d0ab14f14e500992c4d5346ed4de25db87260400` |
| code.claude.com/docs/en/errors.md | — | `37e9799a44678ea216d5c5cc4c6a39fb4029cf9323875de3464a2088bd32d990` |
| platform.claude.com/…/api/skills/create.md | — | `c066aba981965b98c461c245f43a0d47347bbc59160b05030ec229565da536a2` (no frontmatter validation, no error codes) |
| platform.claude.com/…/agent-skills/quickstart.md | — | `27f907732940f1299415b305021a9c2767043c356d8f1fc4e20f39f8f9f9f9b3` (API tutorial: states **no** frontmatter requirements) |

Located quotes (≤25 words), section named because `.md` line numbers move: `best-practices.md`
§ Skill structure "Cannot contain XML tags" (4 words), "Cannot contain reserved words:
\"anthropic\", \"claude\"" (6); § Writing effective descriptions "Always write in third person" (5);
§ Progressive disclosure patterns "Keep the `SKILL.md` body under 500 lines for optimal
performance." (11). `overview.md` § Skill structure "Required fields: `name` and `description`" (6).
`code.claude.com/docs/en/skills` § Frontmatter reference "All fields are optional. Only
`description` is recommended" (9), "truncated at 1,536 characters in the skill listing" (8);
§ Using skill frontmatter outside Claude Code "Allowed properties are: allowed-tools, compatibility,
description, license, metadata, name" (10). `code.claude.com/docs/en/errors` § Skill or command name
refused "a name may not hold hidden, direction-changing or blank-like characters, < or >, or be over
256 characters" (19). `agentskills.io/specification` § `name` field "Must match the parent directory
name" (6), "Must not contain consecutive hyphens (`--`)" (7); § Progressive disclosure "Keep your
main `SKILL.md` under 500 lines." (7). `skills-guide.md` § Creating a Skill → Requirements
"`description`: Maximum 1,024 characters, non-empty, no XML tags" (8); § Error handling "A request
that fails because of a Skill problem returns HTTP 400." (12).

Commands (scratch dir): `sha256sum bp.md ov.md cc.md spec.md guide.md errors.md` → exit 0, table
above. `curl -sSL -o bp2.md …/best-practices.md && sha256sum bp2.md && cmp bp.md bp2.md` → exit 0,
`f0a5d61b…`, `METHOD-AGNOSTIC-IDENTICAL`. `diff -u
.ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md bp.md` → exit 1, 32 hunks
(`grep -c '^@@' s003.diff`), 79/79 lines. `diff <(sed -n '145,170p' old) <(sed -n '145,170p' bp.md)`
→ exit 1, exactly one changed line (the "For complete Skill structure details…" link); six rule
bullets identical. Same for `1100,1191` → exit 1, 5 changed lines, all backticks/link labels; the two
rule bullets identical. `grep -n '^[-+].*(XML|reserved word|Maximum|…)' s003.diff` → only 500-line
backtick/punctuation lines, no rule text.

## Unresolved / boundaries

- Whether `skills-ref` enforces the spec's leading/trailing-hyphen, consecutive-hyphen and
  directory-match rules is the skills-ref seat's slice; the spec page only says the validator
  "checks that your `SKILL.md` frontmatter is valid and follows all naming conventions".
- No authority found states that a description over 1,024 characters or a name over 64 characters is
  *refused* on the Anthropic side; the caps are documented requirements, and the only numeric refusal
  text found is Claude Code's 256-character name notice.
- The `skills-guide.md` byte drift cannot be diffed (round-47's bytes not retained); the
  "1024" → "1,024" observation rests on round-47's literal quote versus today's bytes.
