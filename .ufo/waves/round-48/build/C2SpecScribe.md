# C2SpecScribe — spec half of `corpus/knowledge/frontmatter-rule-authorities-round48.md`

Seat: `KotobaR48.C2EntryScribe` → `KotobaR48.C2SpecScribe`, read-only scribe. Lane base `75f671b109d8eddd0d64c1429bd6379fe577175a`.
Scope: draft the **spec half** only (S001 open spec + S002 client guide) of the C2 knowledge entry.
Tools installed or upgraded: none. `pacman` untouched; no service restarted; no fetched code executed.

## Findings (read this first)

1. **The spec states no RFC-2119 keywords.** `grep -c -e 'MUST' -e 'SHOULD'` on the fetched
   `specification.md` → `0` (exit 1, no match). Strength is carried only by prose verbs:
   `Must` (5 lines), `Should` (2), `Can indicate` (1), `We recommend` (2), `May only contain` (1),
   plus three modal-free bullets (`metadata` ×2, `allowed-tools` ×2, `license`).
   **Consequence for the entry:** a "MUST vs SHOULD" column must label the *normative strength of the
   prose verb*, and say that the RFC-2119 mapping is the entry's normalization, not the source's.
2. **The frontmatter table is a lossy summary; the per-field sections carry the rules.** The table
   (`spec.md:28-35`) states `Max 64` / `Max 1024` / `Max 500` (no lower bounds) and omits the
   consecutive-hyphen rule, the directory-match rule, both `description` SHOULD clauses and the
   `compatibility` "if provided" condition. Every quoted rule below therefore comes from the
   `#### <field> field` section, not the table.
3. **Internal tension A — `name` character set (the one the prompt names).** `spec.md:64` reads
   "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)".
   The word *unicode* admits non-ASCII lowercase; the parenthetical enumerates ASCII only.
   `spec.md:30` rewords it without *unicode* ("Lowercase letters, numbers, and hyphens only").
   The spec gives no example either way, so `résumé` is undetermined by the text. **The entry must
   record the ambiguity, not pick a reading.**
4. **Internal tension B — table vs field, per field.** `name`: "Max 64 characters" (no minimum) vs
   "Must be 1-64 characters". `description`: "Max 1024 characters. Non-empty." vs "Must be 1-1024".
   `compatibility`: "Max 500 characters" vs "Must be 1-500 characters if provided" (the *if provided*
   conditional exists only in the field section). `metadata`: table says "Arbitrary key-value
   mapping" then parenthetically constrains to "(a map from string keys to string values)" —
   *arbitrary* and *typed* in one cell.
5. **Internal tension C — body length is two numbers and neither is a format rule.** `spec.md:187`
   says the body has "no format restrictions"; the 500-line figure lives in `## Progressive
   disclosure` (`spec.md:237`), and the token figure in the tier list (`spec.md:234`).
   500 lines and <5000 tokens are not stated to be equivalent. No frontmatter field is affected.
6. **Internal tension D — the client guide's own summary overstates its leniency.** `client.md:143`
   says the spec "defines strict constraints on the `name` field (matching the parent directory,
   character set, max length)" and that the lenient approach "deliberately relaxes these" — but the
   lenient bullets (`client.md:134-137`) relax only **two** of those three. The character set is
   named as strict and has no leniency bullet. Sweep: `grep -c -e 'unicode' -e 'consecutive'` on
   `client.md` → `0` (exit 1).
7. **The client imposes no rule on four of the six fields.** `client.md:114` says only
   "Extract `name` and `description` (required), plus any optional fields." Sweep on `client.md`:
   `license` → 0, `allowed-tools` → 0, `1024` → 0, `500 lines` → 0 (each exit 1); `compatibility`
   → 4 hits, **none of them a validation rule** (all are prose about compatibility of formats or
   the field's informational use at activation time); `metadata` → 2 hits, both the generic sense.
8. **The client guide's `description` rule is a skip, not a warn.** `client.md:136`:
   "Description is missing or empty → skip the skill (a description is essential for disclosure), log the error".
   S002's registry `teaches` cell says "lenient clients warn and load anyway on name mismatch" and
   omits the two hard skips — the round-47 lesson (`lessons/round-47.md` § Gate) already flagged this
   as a cell gap. The entry must not repeat it.
9. **S001's registry anchor is broken and this round is the round that cites it.** SOURCES S001
   anchors on "§ Skill metadata table"; the live page has no such heading (headings enumerated
   below). SOURCES contract rule 2 forbids an in-place anchor edit, and `lessons/round-47.md:46-49`
   says a superseding row "waits for the next round that cites S001" — that round is now.
   **The entry's `source:` line must use live anchors, and the frontier step must add the
   superseding S-row.** (S001's own `teaches` cell — "Name is 1-64 lowercase-hyphen chars matching
   its directory" — is accurate but drops the consecutive-hyphen and character-set rules.)
10. **Freshness: the spec bytes have not moved since round 47.** Live fetch sha256
    `9a67de89…de16` == the committed snapshot `.ufo/waves/round-47/build/KnowDescriptionRule.s001-specification.md`
    (same sha, `diff` exit 0). Client guide sha256 `79489bd2…e172` == the committed
    `KnowDescriptionRule.s002-adding-skills-support.md`. The renderer caveat from
    `.ufo/waves/round-47/build/SrcS002.md` still applies (the `.md` exporter changed twice in five
    weeks with zero prose change), so **the entry's recheck should be rule-string counts, not a
    sha256 equality.**

## Draft — the spec half of the entry (for the entry author; not landed by me)

### Q12 header lines (spec-half contribution; other rows belong to the other half)

```
source: S001 Agent Skills — Specification — https://agentskills.io/specification#frontmatter (field sections #name-field, #description-field, #compatibility-field, #metadata-field, #allowed-tools-field; #body-content, #progressive-disclosure, #validation); S002 Agent Skills — How to add skills support to your agent — https://agentskills.io/client-implementation/adding-skills-support#lenient-validation (also #handling-malformed-yaml, #frontmatter-extraction). S001's registry anchor label "§ Skill metadata table" names no live heading; the anchors above are the live ones and a superseding S-row is required (SOURCES contract rule 2).
verified-at: 2026-10-22T08:17:00Z
recheck: curl -fsSL https://agentskills.io/specification.md | grep -c -e 'unicode lowercase alphanumeric characters' -e 'Must be 1-64 characters' -e 'Must be 1-1024 characters' -e 'Must be 1-500 characters if provided' -e 'A map from string keys to string values' -e 'A space-separated string of tools that are pre-approved to run' -e 'Keep your main `SKILL.md` under 500 lines' | grep -qx 7 && curl -fsSL https://agentskills.io/client-implementation/adding-skills-support.md | grep -c -e 'Name exceeds 64 characters' -e "Name doesn't match the parent directory name" -e 'deliberately relaxes these' -e 'unquoted values containing colons' | grep -qx 4 && echo "S001+S002 rule text unchanged"
```

### Spec rules, with strength and client leniency

Strength key: **MUST** = spec verb `Must`; **MUST NOT** = `Must not`; **MUST-not-other** =
`May only contain` (only the listed set is permitted); **SHOULD** = `Should`; **RECOMMEND** =
`We recommend`; **CAN** = `Can indicate`; **descriptive** = no modal. The spec never uses RFC-2119
uppercase; the mapping above is the entry's normalization.

| Field | Rule, located quote (≤25 words) | Strength | Client (S002) leniency |
|---|---|---|---|
| `name` | `spec.md:63` "Must be 1-64 characters" | MUST | `client.md:135` "Name exceeds 64 characters → warn, load anyway" |
| `name` | `spec.md:64` "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)" | MUST-not-other (charset ambiguous — tension A) | none (`unicode` sweep → 0) |
| `name` | `spec.md:65` "Must not start or end with a hyphen (`-`)" | MUST NOT | none |
| `name` | `spec.md:66` "Must not contain consecutive hyphens (`--`)" | MUST NOT | none (`consecutive` sweep → 0) |
| `name` | `spec.md:67` "Must match the parent directory name" | MUST | `client.md:134` "Name doesn't match the parent directory name → warn, load anyway" |
| `description` | `spec.md:101` "Must be 1-1024 characters" | MUST | none (`1024` sweep → 0) |
| `description` | `spec.md:102` "Should describe both what the skill does and when to use it" | SHOULD | none |
| `description` | `spec.md:103` "Should include specific keywords that help agents identify relevant tasks" | SHOULD | none |
| `description` | — | — | `client.md:136` "Description is missing or empty → skip the skill (a description is essential for disclosure), log the error" (**skip**, not warn) |
| `compatibility` | `spec.md:134` "Must be 1-500 characters if provided" | MUST, conditional | none (no rule) |
| `compatibility` | `spec.md:135` "Should only be included if your skill has specific environment requirements" | SHOULD | none |
| `compatibility` | `spec.md:136` "Can indicate intended product, required system packages, network access needs, etc." | CAN | none |
| `metadata` | `spec.md:160` "A map from string keys to string values" | MUST (descriptive form, no modal) | none (no rule) |
| `metadata` | `spec.md:161` "Clients can use this to store additional properties not defined by the Agent Skills spec" | CAN | none |
| `metadata` | `spec.md:162` "We recommend making your key names reasonably unique to avoid accidental conflicts" | RECOMMEND | none |
| `allowed-tools` | `spec.md:176` "A space-separated string of tools that are pre-approved to run" | MUST (descriptive form) | none (`allowed-tools` sweep → 0) |
| `allowed-tools` | `spec.md:177` "Experimental. Support for this field may vary between agent implementations" | descriptive — spec does **not** require clients to honour it | none |
| body length | `spec.md:237` "Keep your main `SKILL.md` under 500 lines. Move detailed reference material to separate files." | RECOMMEND, under `## Progressive disclosure` — **not** a format rule | none (`500 lines` sweep → 0); client repeats `client.md:27` "\<5000 tokens (recommended)" |
| body length | `spec.md:187` "The Markdown body after the frontmatter contains the skill instructions. There are no format restrictions." | descriptive — the body is unconstrained by the format section | none |
| body length | `spec.md:234` "Instructions (\< 5000 tokens recommended): The full `SKILL.md` body is loaded when the skill is activated" | RECOMMEND (token budget, not equivalent to 500 lines) | `client.md:27` same figure, tier table |

### Spec-half absences (Q14: each carries its sweep)

- No markup/XML rule on `description`: `grep -c -i -e 'angle bracket' -e 'XML tag' spec.md` → `0`, exit 1.
- No reserved-word rule on `name`: `grep -c -i reserved spec.md` → `0`, exit 1.
- No closed field set: `grep -n -i -e 'unknown field' -e 'other fields' -e 'only these fields' -e 'must not contain any other' spec.md` → no match, exit 1.
- No `allowed-tools`/`license`/`metadata`/`compatibility` rule on the client side (counts in finding 7).
- S001's registry anchor names no heading: live headings are `Directory structure`, `SKILL.md format`,
  `Frontmatter` (`#frontmatter`), `name field` (`#name-field`), `description field`, `license field`,
  `compatibility field`, `metadata field`, `allowed-tools field`, `Body content` (`#body-content`),
  `Optional directories`, `Progressive disclosure`, `File references`, `Validation`.

### What the spec half does NOT claim

- It does not decide whether a non-ASCII lowercase `name` passes (tension A is recorded, not resolved).
- It does not claim any client's loader enforces the spec's `name` charset (tension D: the client
  guide has no such bullet).
- It does not claim the 500-line and 5000-token figures are the same limit.
- It says nothing about the skills-ref validator, Anthropic docs/packager, Codex, or the lane's own
  checker — those columns belong to the other half of the entry.

## Evidence (commands, exit codes as observed — 2026-10-22)

- `curl -fsSL -w 'SPEC HTTP:%{http_code} SIZE:%{size_download} URL:%{url_effective}' https://agentskills.io/specification.md -o f_spec.md` → exit 0, `HTTP:200 SIZE:7608 URL:https://agentskills.io/specification.md`; `date -u` → `spec_at=2026-10-22T08:17:00Z`.
- `curl -fsSL -w 'CLIENT HTTP:%{http_code} SIZE:%{size_download} URL:%{url_effective}' https://agentskills.io/client-implementation/adding-skills-support.md -o f_client.md` → exit 0, `HTTP:200 SIZE:20349`; `client_at=2026-10-22T08:17:00Z`.
- `sha256sum f_spec.md f_client.md` → exit 0, `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`, `79489bd252377681a31958e75ee3e6e96f7f791719eaac3b3e870a0d193be172`.
- `diff <(curl -fsSL https://agentskills.io/specification.md) .ufo/waves/round-47/build/KnowDescriptionRule.s001-specification.md` → exit 0, 0 diff lines (spec bytes unchanged since round 47).
- `git ls-files --error-unmatch .ufo/waves/round-47/build/KnowDescriptionRule.s001-specification.md .ufo/waves/round-47/build/KnowDescriptionRule.s002-adding-skills-support.md` → exit 0 (both tracked).
- `grep -c -e 'MUST' -e 'SHOULD' f_spec.md` → `0`, exit 1. `grep -n -E '^\* (Must|Should|Can|We recommend|A space|May only|A map|Clients can)' f_spec.md` → exit 0, 13 lines (63,64,65,66,67,101,102,103,122,134,135,136,160,161,162,176).
- `grep -c -i -e 'angle bracket' -e 'angle-bracket' -e 'XML tag' f_spec.md` → `0`, exit 1. `grep -c -i reserved f_spec.md` → `0`, exit 1. `grep -n -i -e 'unknown field' -e 'other fields' -e 'only these fields' -e 'not recognized' -e 'must not contain any other' f_spec.md` → exit 1 (no match).
- Client sweeps on `f_client.md`: `1024` → 0, `allowed-tools` → 0, `500 lines` → 0, `unicode` → 0, `consecutive` → 0, `hyphen` → 0, `license` → 0 (all exit 1); `compatibility` → 4 (lines 60, 128, 143, 270 — none a validation rule); `metadata` → 2 (lines 36, 107 — generic sense); `64 characters` → 1 (line 135).
- `curl -s -o /dev/null -w '%{http_code}\n'` for `…/specification#name-field`, `#frontmatter`, `#body-content`, `#progressive-disclosure`, `…/adding-skills-support#lenient-validation`, `#handling-malformed-yaml` → `200` each (exit 0).
- Anchor ids extracted from the live HTML: spec `frontmatter`, `name-field`, `description-field`, `compatibility-field`, `metadata-field`, `allowed-tools-field`, `body-content`, `progressive-disclosure`, `validation`; client `frontmatter-extraction`, `handling-malformed-yaml`, `lenient-validation`.
- Recheck command as written in the draft header → exit 0, printed `S001+S002 rule text unchanged` (spec count 7, client count 4).
- Quote lengths: 32 candidate quotes counted; 31 are ≤ 25 words. The one 26-word candidate
  (`client.md:139`, "Record diagnostics so they can be surfaced to the user (in a debug command,
  log file, or UI), but don't block skill loading on cosmetic issues.") was **not used** in the
  draft table; the entry author must not quote it whole.

## Out of scope / not done

- The entry file itself was **not** written (lane read-only except this report; the entry is another seat's).
- No skills-ref, Anthropic, Codex or lane-checker material was opened or asserted here.
- No fetched code was executed; no `git`/`jj` write command was run in the lane, the fleet repo or any sibling lane.

Report: `.ufo/waves/round-48/build/C2SpecScribe.md`
