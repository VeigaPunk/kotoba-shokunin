# Round 49 seat report — SrcSpecDescriptionField (C1 source check, row S018 re-open)

Scope: re-open `https://agentskills.io/specification.md` myself, compare bytes/sha256 to the S018 row
in `corpus/SOURCES.md`, locate what the spec says the `description` field must describe (what the
skill does and when to use it) with a ≤25-word verbatim quote and a line number, sweep the same
document for any statement about overlapping or conflicting skills (recording the grep command and
count), draft the `corpus/lessons/round-49.md` `## Gate` re-open line, and rule on whether the C1
entry may cite S018 for the description-role sentence. Lane base
`a5adc146a2995dcc5a95a6d8db6e5674f75191ac`. Lane read-only: this report file is the only file
written in the lane.

## Findings

**F1 — S018 re-opens byte-identically; the row needs no status or recheck change.**
This round's fetch: HTTP 200, 7,608 B, sha256
`9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`, at 2026-10-22T09:38:59Z. The
S018 row's anchor cell already records "200, 7608 B, sha256 `9a67de89…`" and calls it
"byte-identical to the round-47 fetch". A second, independent fetch, timestamped 2026-10-22T10:00:12Z,
returned the same size and hash (`cmp` → identical), so the source did not move during the
measurement (Q10). The
row's cells are `status=mined`, `opened=2026-10-22`, `recheck=90d`. Both stay **unchanged**: the
content still teaches what the row says it teaches, and contract rule 2 forbids editing anything but
`status`/`recheck`/`used-by` in place. **No new row is written** — S018 already covers this URL, and
the plan's frontier step already says "New rows only for sources opened this round" while the census
start lists S018 among the three W04 duplicate-URL warnings.

**F2 — The description-role sentence, located and quoted.**
Two places in the live page carry it, both inside S018's own anchor list (§ Frontmatter table,
§ `description` field):

- `specification.md:102`, under the heading `#### \`description\` field` (line 97):
  `* Should describe both what the skill does and when to use it` — 12 words.
- `specification.md:31`, the `description` row of the Frontmatter table:
  `| \`description\` | Yes | Max 1024 characters. Non-empty. Describes what the skill does and when to use it. |`
  — 20 words.

Both are ≤25 words and verbatim. Note the normative strength differs between them: the field
section uses **Should** (line 102), while the table states it as the row's constraint description
(line 31). The same section's hard rule is only the length bound, `* Must be 1-1024 characters`
(line 101). The pinned upstream source `docs/specification.mdx` at commit `69ef37e9` carries the same
two lines at :95 and :28 (verified this round, fetch below), so the sentence is not a rendering
artifact of the live `.md` route.

**F3 — The spec states no rule about overlapping or conflicting skills (negative finding, with its
sweep).**
Canonical sweep over the fetched file, `grep -cinE
'overlap|ambiguit|compete|competition|precedence|disambiguat|tie[- ]?break|arbitrat|mutually
exclusive|multiple skills|more than one skill' specification.md` → **0** (exit 1). Adding `conflict`
to the same alternation → **1** (exit 0), and that one hit is not about skills: line 162, under
§ `metadata` field, reads "We recommend making your key names reasonably unique to avoid accidental
conflicts" — a warning about duplicate *metadata key names*, not about two skills competing. A
whole-word sweep of the same family (`overlap`, `overlaps`, `overlapping`, `conflict`, `conflicts`,
`conflicting`, `ambiguous`, `ambiguity`, `compete`, `competing`, `precedence`, `disambiguate`,
`disambiguation`) gives 0 for every token except `conflicts` = 1 (line 162). A
selection-vocabulary sweep (`pick|select|choos|which skill|most relevant|similar skills|multiple
skills|several skills`) hits only the three description-role lines (31, 42, 102) and one unrelated
"or similar products" line (141, the `compatibility` example). **Consequence for C1: S018 cannot
ground an arbitration or tie-break rule.** The census must not cite it for one.

**F4 — What the spec does offer the census, and where its limit is.**
Three located statements bound what S018 may be cited for, all inside S018's anchor list:

- `specification.md:233` (§ Progressive disclosure): "The `name` and `description` fields are loaded
  at startup for all skills" — i.e. every installed skill's description is preloaded at once, so
  descriptions do compete for the same context. This is a *load* fact, not a *selection* rule.
- `specification.md:103`: "Should include specific keywords that help agents identify relevant tasks"
  — the spec's only guidance aimed at making a description selectable.
- F2's description-role sentence.

So the honest citation shape for the C1 census is: **S018 grounds the description-role sentence
(what a description must say) and the all-preloaded-at-startup fact; it says nothing about how a
harness resolves two matching descriptions.** The arbitration half of the C1 claim needs a different
authority — the sibling seats' drafts (S022 Claude Code skills docs, S023 Anthropic overview) are
the candidates for that half.

**F5 — Yes, the C1 entry may cite S018 for the description-role sentence, with three conditions.**
(a) *Scope fits.* S018's `scope` cell is "SKILL.md frontmatter field rules, with the page's own
headings and the pinned file that renders them", and its `anchor` cell already names "§ Frontmatter
table, § `description` field" — the description-role sentence is inside the row's stated scope and
anchor, so no new row and no anchor edit (rule 2) is needed. (b) *The re-open must be logged this
round.* Rule 1 requires the source to be opened in the round that writes the claim; this seat's
re-open (F1) plus the `## Gate` line drafted below is that record. (c) *`used-by` must be updated
old→new.* S018's `used-by` is currently `SKILL.md,
corpus/knowledge/frontmatter-rule-authorities-round48.md`; because the census entry cites S018, it
becomes `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md,
corpus/knowledge/sibling-overlap-census-round49.md`. The census validator's E11 check tests every
`used-by` path of a `mined` row against the disk: `corpus/knowledge/sibling-overlap-census-round49.md`
landed in the lane during this seat's run (it was absent at my first check and present at my last),
so the E11 precondition is now satisfied and the `used-by` edit can be made; it had **not** been
made at my last read of `corpus/SOURCES.md`, and `scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kotoba` still exits 0 with the same three W04 warnings.

**F5b — The entry's `source:` line cites S018, but no body sentence is grounded on it.**
`corpus/knowledge/sibling-overlap-census-round49.md:1` lists `S018 (https://agentskills.io/specification,
§ \`description\` field)` in its `source:` header, and the string `S018` appears nowhere else in the
entry — the only other mention of the spec is in that same header line. The entry's body sentence
that carries the description role is grounded on S022 instead (line 16: "The description is the
matching input. Claude Code: \"What the skill does and when to use it. Claude uses this to decide
when to apply the skill.\" (S022, `skills.md:389`)"). So the entry currently has a header-level
citation to S018 with no located quote behind it. Two ways to close that, both within the rules:
(i) ground one body sentence on S018 with the located quote from F2 — "Should describe both what the
skill does and when to use it" (§ `description` field, `specification.md:102`) — which is the
normative *format* requirement, alongside S022/S023's *runtime* statements; or (ii) drop S018 from
the `source:` header if the entry makes no claim the spec grounds. Option (i) is the one this seat's
evidence supports; option (ii) is also legitimate, since the entry's arbitration claim does not rest
on the spec (F3). Either way the `used-by` old→new in F5(c) must match what the entry actually
cites.

**F6 — One anchor-precision note for the L1 (not a change I can make).**
S018's anchor cites the pinned source at "lines 27, 61-65, 94, 224". I checked all of them against
the pinned file this round: 27 = the `name` table row, 61-65 = the five `name` field bullets, 94 =
`- Must be 1-1024 characters` (the description *length* rule), 224 = the 500-line body rule. The
description-role sentence itself is at pinned line **95**, and its Frontmatter-table row at pinned
line **28** — neither is in the cited list. This does not impair the C1 citation (the live-page
section anchors cover it, and rule 2 forbids an in-place anchor edit anyway), but if the L1 wants a
pinned-source locator for the description-role sentence it should cite `docs/specification.mdx:95`
and `:28` in the entry's own `source:` line rather than leaning on S018's anchor cell.

**F7 — The re-open adds no new census warning.** `bash scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin kotoba` on the current tree: three W04 duplicate-URL warnings (S018,
S019, S021) and `kotoba ok`, exit 0 — matching the plan's frontier step. A *new* row on the
agentskills.io URL would have added a fourth W04; the re-open adds none.

## Draft deliverables

### D1 — `corpus/lessons/round-49.md` `## Gate` re-open line

Prose form, following round 47's `## Gate` precedent for re-opened rows (round 48's `## Gate`
instead logs new rows in a table; the re-open line sits after that table):

```
**Existing row re-opened (no status change):** S018 (Agent Skills — Specification) re-opened this
round by seat `.ufo/waves/round-49/build/SrcSpecDescriptionField.md`: `https://agentskills.io/specification.md`,
fetched 2026-10-22T09:38:59Z, 200, 7,608 B, sha256 `9a67de89…` — byte-identical to the round-47 and
round-48 fetches and to the bytes the row's anchor cell already records; a second fetch at
2026-10-22T10:00:12Z returned the same size and hash. The `description`-role rule holds and is
located: "Should describe both what the skill does and when to use it" (§ `description` field,
`specification.md:102`; the same sentence as the Frontmatter-table row at `specification.md:31`).
Status `mined` → `mined` (unchanged); recheck `90d` → `90d` (unchanged). `used-by` old→new:
`SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md` → `SKILL.md,
corpus/knowledge/frontmatter-rule-authorities-round48.md,
corpus/knowledge/sibling-overlap-census-round49.md` (the census entry must exist on disk first —
E11 checks every `used-by` path of a `mined` row).
```

Table-form alternative, if the L1 keeps round 48's per-row table for re-opens too (add after the
new-row table; `accessed` = 2026-10-22T09:38:59Z):

```
| S018 | https://agentskills.io/specification | 2026-10-22T09:38:59Z | "Should describe both what the skill does and when to use it" (§ `description` field, `specification.md:102`) — seat `.ufo/waves/round-49/build/SrcSpecDescriptionField.md` |
```

### D2 — the negative claim's sweep, for the lesson's sweep sentence

```
S018's spec states no rule about overlapping or conflicting skills: `grep -cinE
'overlap|ambiguit|compete|competition|precedence|disambiguat|tie[- ]?break|arbitrat|mutually
exclusive|multiple skills|more than one skill' specification.md` → 0 (exit 1) over the 2026-10-22
fetch (7,608 B, sha256 `9a67de89…`); widened with `conflict` → 1 (exit 0), the sole hit being
`specification.md:162` "We recommend making your key names reasonably unique to avoid accidental
conflicts", which is about `metadata` key names, not skills.
```

### D3 — the C1 citation sentence (for the census entry's `source:` line)

S018 may be cited for the description-role sentence, and only for that. It may **not** be cited for
arbitration, tie-breaking, or how a harness picks one skill among overlapping descriptions — the
spec states no such rule (F3). If the entry keeps S018 in its `source:` header, one body sentence
should carry the located quote so the citation is grounded (F5b):

> The description states what the skill does and when to use it (§ `description` field,
> `specification.md:102`, S018).

and the matching `used-by` old→new on S018 is D1's last clause.

## Evidence

Fetch and hash (scratch `/fast/scratch/hyaku/kotoba-r49/seats/srcspecdescriptionfield/`):

- `curl -sS -L -o specification.md -w 'http_code=%{http_code} size_download=%{size_download} …' https://agentskills.io/specification.md`
  → exit 0; `http_code=200`, `size_download=7608`, `url_effective=https://agentskills.io/specification.md`;
  `date -u` → `2026-10-22T09:38:59Z`.
- `sha256sum specification.md` → `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`;
  `wc -c specification.md` → `7608`.
- Second fetch (`specification.fetch2`) at 2026-10-22T10:00:12Z: same size, same sha256; `cmp` → identical.
- Pinned upstream source: `curl -sS -L -o spec-mdx-69ef37e9.md https://raw.githubusercontent.com/agentskills/agentskills/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx`
  → exit 0, `http_code=200`, `size=7166`; `sha256sum` → `b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220`.
  Pinned lines 28, 95 carry the same description-role sentence as live lines 31, 102; pinned 27, 61-65,
  94, 224 match S018's cited list (F6).
- No fetched code was executed; both fetches are read-only document reads.

Sweeps on the fetched spec (all commands in scratch, exit codes verbatim):

- `grep -cinE 'overlap|ambiguit|compete|competition|precedence|disambiguat|tie[- ]?break|arbitrat|mutually exclusive|multiple skills|more than one skill' specification.md` → `0`, exit 1.
- `grep -cinE '…|conflict' specification.md` → `1`, exit 0 (line 162, `metadata` key names).
- Whole-word loop over `overlap overlaps overlapping conflict conflicts conflicting ambiguous ambiguity compete competing precedence disambiguate disambiguation` → all 0 except `conflicts` = 1.
- `grep -inE 'pick|select|choos|which skill|most relevant|similar skills|multiple skills|several skills' specification.md` → lines 31, 42, 102, 141 (141 = `compatibility` example), exit 0.
- `grep -inE 'activat|trigger|relevant|identify|decide|match|load' specification.md` → lines 67, 103, 195, 219, 231, 233, 234, 235, exit 0.
- `grep -n 'what the skill does and when to use it' specification.md` → lines 31 and 102, exit 0.
- `grep -n 'specific keywords that help agents identify relevant tasks' specification.md` → line 103, exit 0.
- `grep -nE '^#{1,4} ' specification.md` → 18 headings; `§ \`description\` field` at 97, `§ Frontmatter` at 26,
  `§ Progressive disclosure` at 229, `§ \`metadata\` field` at 156, `§ Validation` at 252.

Lane checks (read-only, in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`):

- `git rev-parse HEAD` → `a5adc146a2995dcc5a95a6d8db6e5674f75191ac`.
- `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` → three W04 lines
  (S018, S019, S021) plus `kotoba ok`, exit 0.
- `awk -F'|' '/^\| S018 /{print NF}' corpus/SOURCES.md` → 13 (11 columns, well-formed row);
  `status` = `mined`, `opened` = `2026-10-22`, `recheck` = `90d`,
  `used-by` = `SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md`.
- `ls corpus/knowledge/ | grep -i 'sibling-overlap'` → exit 1 (no match) at 09:52Z; by 10:0xZ the
  same path listed `sibling-overlap-census-round49.md` (13,720 B, mtime 06:53) — the C1 entry landed
  in the lane during this seat's run, which is what satisfies the E11 precondition in F5(c).
- `grep -n 'S018\|specification' corpus/knowledge/sibling-overlap-census-round49.md` → only line 1
  (the `source:` header); `grep -n 'does and when to use it\|describ'` → only line 16, which grounds
  the description role on S022 (`skills.md:389`), not S018 (F5b).
- `awk -F'|' '/^\| S018 /{print $12}' corpus/SOURCES.md` at 10:0xZ → still
  ` SKILL.md, corpus/knowledge/frontmatter-rule-authorities-round48.md ` — the `used-by` old→new edit
  has **not** been made yet.
- `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` re-run after
  the entry landed → three W04 lines (S018, S019, S021) plus `kotoba ok`, exit 0.
- `grep -rn 'S018' --include='*.md' .` (excluding `.ufo`) → the round-48 authorities entry, the round-48
  lesson, the round-48 spot-check, `corpus/README.md`, `SKILL.md` (1 hit), `corpus/SOURCES.md`, and
  the new census entry.
- `ls corpus/lessons/round-49.md` → exit 1 (file absent): the `## Gate` line in D1 is a draft for the
  L1 to insert when the lesson file is created.

## Not done / limits

- No edit to `corpus/SOURCES.md`, `corpus/lessons/round-49.md`, or any lane file except this report;
  the lane is read-only for this seat. D1–D3 are drafts for the L1.
- The C1 census entry landed in the lane during this seat's run (F5c). The `used-by` old→new edit on
  S018 has not been made, and the entry's body still grounds the description role on S022 rather than
  S018 (F5b). Both are the L1's to land; this seat did not touch either file.
- This seat did not open Anthropic's, OpenAI's, or Claude Code's documentation, so it makes no claim
  about what those authorities say about arbitration — only about the open spec (S018's URL).
- The spec is a *specification of the format*, not a measurement of any harness. Whether a real host
  (omp, opencode, Claude Code) loads descriptions as the spec describes is outside this seat's scope.
- No tool was installed or upgraded this session; the fetch used the pre-existing `curl`, `sha256sum`,
  `grep`, `awk`, `wc`, `cmp`, `date` and `git` (read-only commands only). No `jj` command was run, and
  no `pacman`/`uv tool`/`cargo`/`npm -g` transaction was made.

Report: .ufo/waves/round-49/build/SrcSpecDescriptionField.md
