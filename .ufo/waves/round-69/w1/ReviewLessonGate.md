# ReviewLessonGate — round-69 § Gate (kotoba, wave 1)

Seat: `L1Kotoba69-2.ReviewLessonGate` (reviewer, leaf; no subagent dispatch, no lane writes).
Scope: `corpus/lessons/round-69.md` § Gate against the round contract (fleet `CORPUS.md` rule 1,
`SOURCES.md` rules 1–2), the plan (`plans/round-69.md` items 10 and Frontier), and the S203–S208
rows in `corpus/SOURCES.md`. Read-only; every claim below is re-opened from the lane file or a
fresh fetch. No edit was made to any corpus, lesson, verifier or committed file.

## State pinned (the lane was being edited while this review ran)

| artifact | mtime | what I measured |
|---|---|---|
| `corpus/lessons/round-69.md` | 2026-10-25 07:25:59 -0300, 163 lines | the Gate below; it changed at 07:17:50 → 07:25:59 during the review |
| `corpus/SOURCES.md` | 2026-10-25 07:23:49 | first read 07:08: 6 added rows, tiers B, S208 anchor "the tool-approval section"; re-read 07:23: `git diff --numstat a5f7459` = **7 additions / 1 deletion**, tiers A, S206 (11 words), S208 anchor corrected |
| `corpus/knowledge/client-trust-gates-round68.md` | 2026-10-25 07:24:16 | amendment still says "in the tool-approval section" |
| `corpus/knowledge/skill-name-precedence-round69.md` | 2026-10-25 07:28:47 | entry revised during the review (V1-route scope, Roo qualification); cited line numbers are from this read |

I wrote nothing in the lane. The 07:23/07:24/07:25 edits were made by another process after this
seat began; they are evidence in themselves (the Gate at 07:25 absorbed tier A and S206's 11-word
count, but not the S208 bullet, the S201 cell edit, the renumber map, the recheck list or the
validation receipt).

Fetches (all 2026-10-25, `curl -sSL --max-time 40 -A '<Chrome/130 UA>'`, HTTP 200):
`ms.html` 156,814 B sha256 `11a7ab7e01ca39d5b9aff0504f186a0a788c31974fb8b0464a8358d3d60644fe`;
`amp.html` 102,591 B `b49f3c96…`; `junie.html` 38,509 B `b3c67690…`; `roo.html` 71,129 B
`fe801910…`; `oc.html` 71,581 B `06a30dce…`; `dc.html` 163,923 B `af207fac…`; `kilo.html`
138,104 B `894ae031…`; `vibe.md` 74,355 B `e790613a…`. The Microsoft section mapping was read
from the raw HTML heading ids, not from a text scrape.

## Findings

### F1 (high) — S208's § Gate record is incomplete and its location contradicts the row and the page

`corpus/lessons/round-69.md:67-70` admits S208 as "the approval sentence … verbatim on the
Microsoft page (twice), **in the tool-approval sections**", with **no URL** and **no access date in
the § Gate record** (the date appears only in § Status changes, `:155-163`; the URL only in the
S208 row). CORPUS rule 1 requires the Gate to record, for every new row, the URL, the access date
and a ≤25-word quote **with its location**.

The location is wrong against today's served page and against the row the Gate describes:

- the exact string `All three skill tools require approval by default.` occurs **twice**, at HTML
  offsets 34,074 and 35,882, both under `<h2 id="use-agent-skills-with-harness-agent">` — the
  section titled **"Use Agent Skills with Harness Agent"** (the last heading id before each
  occurrence is `use-agent-skills-with-harness-agent`);
- the page's single `<h2 id="tool-approval">Tool approval` section (offset 105,959) does **not**
  contain that sentence; it carries a different one: "All tools exposed by AgentSkillsProvider
  (load_skill, read_skill_resource, run_skill_script) require approval by default.";
- the current S208 row (07:23) is already correct: `the "Use Agent Skills with Harness Agent"
  tool-approval prose (the sentence occurs twice on the page, not in the separate Tool approval
  heading)`. The Gate's "tool-approval sections" therefore contradicts its own row;
- the r68 amendment (`corpus/knowledge/client-trust-gates-round68.md:82-85`) still says "in the
  tool-approval section" — the same wrong location, not updated at 07:24.

This is the R68-6 class the round exists to fix: the correction row's anchor was fixed, the
admission record that describes it was not. Fix (not applied): add the URL and `2026-10-25` to the
S208 bullet; replace "in the tool-approval sections" with "Use Agent Skills with Harness Agent,
the two paragraphs after the file-based-skill `AgentFileSkillScriptRunner` guidance (two
occurrences)"; correct the r68 amendment to the same section.

Corroboration, re-verified by me: `ScribeQuotes.md:62` and `anchor.log:27-33` record the same
section finding; I re-derived it from `ms.html` by heading id.

### F2 (high) — the refusal states no flip condition, and refuses the quote S208 admits

The header at `:72` says "kept as a refusal **with a flip condition**"; the refusal at `:73-80`
ends **"Flip for the old refusal: none — the paragraph is superseded by S208."** That is not a
flip condition; `SOURCES.md` rule 1 and the lane's r68 pattern (`round-68.md:47-58`) require
`flip: <what would change the verdict>`.

The refusal's object is also wrong. It is titled "Refused — the staged S201 quote" while the same
paragraph says the sentence is verbatim and S208 admits it; the only defect it names is the
**anchor**. The refusal should refuse the *staged anchor* (the S201 anchor placed the approval
sentence under `Security best practices`), not the payload, and should record the flip that was
met: the r68 flip was "a fetch that renders the literal phrase 'All three skill tools require
approval by default'", and today's fetch meets it twice. As written a reader cannot tell what is
refused or what would clear it.

### F3 (high) — "as staged … no renumbering was needed" is false, and the plan's renumber map is absent

`corpus/lessons/round-69.md:96-104` says the 128 registry ids and 188 staged ids give 0 collisions
"by construction: `comm -12`", then: "The adopted ids continue the lane's registry **as staged**
(S203–S207); **no renumbering was needed** and no citation was re-pointed by arithmetic."

The campaign package disproves the "as staged" reading:

- `merge/kotoba/SOURCES.append.md` stages S203–S208 as **different documents** (S203 OpenAI Model
  Spec, S204 anthropics/skills, S205–S207 Qwen Code docs EN/ZH/JA, S208 Qwen weekly update);
- the theme's staged ids are S265 (Roo Code), S276 (Amp), S250 (Deep Code English), S252 (Junie),
  and S259 (opencode **Japanese**); S207's English `/docs/skills/` page has **no staged twin**
  (the package stages the JA page as S230/S259);
- the lane's S203–S208 are Roo/Amp/Deep Code EN/Junie/opencode EN/Microsoft — a document-level
  re-pointing, not a copy of the staged ids.

The 0-collision test is true but vacuous for this risk: staged ids start at S203 and the registry
ends at S202, so `comm -12` cannot detect that the adopted ids reuse the campaign's proposed ids
for other documents. `plans/round-69.md` item 10 requires "the renumber map lands in the lesson";
the lesson contains no S265/S276/S250/S252/S259 and no map (`grep -n 'S265\|S276\|S280\|S252\|S259'
corpus/lessons/round-69.md corpus/knowledge/skill-name-precedence-round69.md` returns no line; the
only place those ids appear under `.ufo/waves/round-69/` is the `assimilation/staged-ids` list). Either add the map (S265→S203, S276→S204, S250→S205 — the EN page — S252→S206,
S259→S207, with the page/language changes) or state "0 package rows adopted; the map is empty".
Corroboration: `ExecCollisionGuard.md:5.3` measures the same 16 document twins and reaches the same
conclusion; the S203↔S265, S204↔S276, S205↔S250, S206↔S252, S208↔S274 pairs were re-checked by me
against `SOURCES.append.md`.

### F4 (medium) — the "stripped `recheck` prose" is not the staged prose

`:87-95` claims the list is "from the staged rows, kept here per the contract". The campaign's
staged cells read differently, and in two cases name a different page:

- S265 (Roo): `90d — re-fetch and confirm the "higher priority" labels and the scope ordering are
  unchanged (ran 2026-10-23)` — the Gate's wording ("Override Control bullet and the native-root
  priority label") is a rewrite;
- S276 (Amp): `… confirm the eight-source order and the masking sentence … (ran 2026-10-24)` — the
  Gate drops the eight-source order;
- S250 (Deep Code EN): `… confirm the five-rank scan table and the metadata.allow-implicit-invocation
  field … (ran 2026-10-23)`; S280 (the Chinese page the staged entry cites): `… the four-root list
  and the same-name rule … (ran 2026-10-24)` — the Gate says "re-fetch **the English page** and
  confirm the highest-priority-kept sentence", matching neither staged cell exactly;
- S252 (Junie): `… the five location categories, the --skill-default-locations lever and the
  frontmatter requirements … (ran 2026-10-23)` — the Gate substitutes "the project-level-precedence
  sentence";
- S259 (opencode JA): `… the six roots, the walk-up rule and the recognised-field list … (ran
  2026-10-23)` — the Gate says "the page … the uniqueness check", i.e. the English V1 page, not the
  staged page.

No artifact under `.ufo/waves/round-69/` carries the Gate's prose (the append block has bare `90d`).
Quote the staged cells verbatim with their dates, or drop the "from the staged rows" claim and
explain the page substitutions.

### F5 (medium) — the census validation receipt does not cover the landed file

`:105-111` cites `assimilation/validate/corpus/SOURCES.md` → exit 0, "re-run after this round's
append". That mirror has **5 rows, S203–S207, strength cell A, anchors ending "page as served
2026-10-25", 17 W04**; the landed file has **6 rows, S203–S208, now strength A, 18 W04**. S208 was
never in the append block or the mirror (`grep -c S208` → 0 in both). The live census additions are
`S207 duplicate url opencode.ai/docs/skills` (against S024/S039) and `S208 duplicate url
learn.microsoft.com/…` (against S201): 16 W04 at base → 18 now (`controls/census-before.txt` 16;
I re-ran `scripts/sources-census.sh validate --file` on a `/tmp` copy of the current file and
counted 18 W04 — the copy also raises E11 `missing used-by` lines because its corpus tree is absent,
an artefact of the copy, not the lane; the Gate's mirror had the tree and exit 0). "exit 0 (file
ok, warnings only)" is true of the exit code; "census unchanged" would be false. Run the validator on the
landed bytes (or a mirror of them) after the last append and commit that receipt; disclose the
W04 delta. Corroboration: `ScribeFactsAudit.md:51-56,160-166` (same mismatch, measured at the 07:08
B-state) — the 07:23 edit fixed the A/note half, not the S208/W04 half.

### F6 (medium) — S201's anchor cell was edited in place after the Gate, and the Gate does not log it

`git diff a5f7459 -- corpus/SOURCES.md` now has **7 additions / 1 deletion**; the deletion/addition
is the S201 anchor cell `(13 words)` → `(14 words)`. The corrected count is the true `wc -w` (14),
but `SOURCES.md` rule 2 permits only `status`, `recheck` and `used-by` to change in place, and each
change must be logged old→new in the round lesson. `:155-162` says only "No prior row's `status`,
`recheck` or `used-by` was changed: … gained six rows and lost none" — the anchor-cell edit is
neither logged nor reverted. (At my first 07:08 read the diff was 6/0, so this edit postdates the
initial Gate.) Log `S201 anchor word-count cell 13→14 (base count was wrong)` and note that the
append-only gate will flag it, or revert the cell and carry the correction as a new row. The edit
is a correction of a real defect (`ScribeQuotes.md:45` measured 14 vs the row's 13), not a
falsification; the defect is the unlogged protected-cell rewrite.

### F7 (low) — count evidence: Q13 and Q54

The Gate states `(8 words)`, `(9)`, `(6)`, `(11)`, `(8)`, `128`, `188`, `13`, `7`, `6`, `1,020`,
`1,024` without the `<command> <date>` form Q13 requires for corpus counts or the `wc -w` command
Q54 requires on the line (or next two) for word counts. The five counts are otherwise correct
(S203 8, S204 9, S205 6, S206 11, S207 8 by `wc -w`; S206 was 12 in the 07:17 Gate and is now
fixed), and `128`/`188`/`0` are backed by `assimilation/reg-ids`, `staged-ids`, `collisions` —
cite the commands and the date. The `1,020 parsed` is consistent with the lane's convention
(`yaml.safe_load` gives 1,019 space-joined; 1,020 parsed with the YAML `>` trailing newline, as the
r67 spot-check records), so the number itself is not a defect.

### F8 (low) — `considerthese` attribution and section pointer

`:124-129` calls `considerthese/2026-10-24.md` "operator-authored"; its own header says "Daily
reflection by the kotoba-shokunin Grok Bot (read-only reviewer; this file is its one authorized
write)". It also says "the C1 entry's `## Scope` and the round's claim declarations cite the same
bar": the entry's `## Scope` (currently `:52-57` after the 07:28 revision) does not cite the
documentary bar; the `## Limits` section (`:41-46`) does ("Documentary evidence only"), and the
plan's C1 bound does. Point at `## Limits`.

### F9 (low) — S172's register span does not truncate mid-word

`:117-121` says S172's register span "truncates mid-word". The cell is exactly
`` `If a project-level and a `` — it ends after the word "a", mid-sentence, not mid-word; it elides
the two `<code>` parentheticals. The substantive point (a folded anchor copy, not a missing
payload) stands; the wording overclaims.

### F10 (low) — S207's negative and the duplicate-page row

The S207 row's `teaches` ("opencode states no precedence … its only guidance is a uniqueness
rule") is a negative with no recorded sweep (Q14/Q30). My sweep of the served V1 page supports it:
`precedence` 0, `same name` 0, `conflict` 0, `duplicate` 0; only the quoted `unique` line and
"Override per agent" (a permissions mechanism, not name precedence). The new "Delta against round
50" paragraph (`:37-44`) is a genuine improvement — it acknowledges the round-50 entry already
carries opencode's exact sentence from S024, scopes opencode to the V1 route, and records that
`/v2/docs/skills/` (S064's page) has a § Precedence ladder; I verified the V1 page has no
"precedence" hit, the V2 page has the ladder ("Skills are selected by ID … the source registered
later supplies the skill"), and the entry now says "opencode (V1 route) … does not claim the V2
ladder". The remaining row-level gap is that S207 duplicates S024's page and quote (the W04 above)
without the row naming the duplicate; the delta discloses the re-carry, so this is disclosure
quality, not a false claim.

### F11 (low) — one stale S201 pointer remains in the r68 entry

The body's section header now reads "**Approval and review (S208, superseding S201's anchor)**"
(`client-trust-gates-round68.md:37`), but the amendment's last parenthetical still says "(section
'Approval and review', **S201**)" (`:85`), and the body's table row 26 still cites S201 for the
*security* quote (correct for that quote). The Gate's sentence "The r68 entry names S208 in an
appended amendment" is true; the leftover `S201` in the amendment's section pointer is a small
custody drift, not a false Gate claim. (RevSourcesRows F3 raised the earlier, larger form of this
finding; the 07:24 edit fixed the header, not the parenthetical.)

## Verified rows (admission record)

`wc -w` run on the quoted strings; verbatim checked against the fetched pages; sections from the
HTML heading ids or the page's own heading text.

| id | URL in § Gate | date in § Gate | quote | wc -w | verbatim | location |
|---|---|---|---|---|---|---|
| S203 | ✓ | ✓ 2026-10-25 | "Project skills override global skills, mode-specific override generic" | 8 ✓ | ✓ 1×, under "What Skills Let You Do" → "Override Control" | ✓; "Roo-specific (higher priority)" under "1. Choose a location" |
| S204 | ✓ | ✓ | "Local skills mask repository skills with the same name." | 9 ✓ | ✓ 1×, under "Skill Sources and Precedence" | ✓ |
| S205 | ✓ | ✓ | "only the highest-priority one is kept" | 6 ✓ | ✓ 1×, under "Scan Locations", sentence before the priority table | ✓ |
| S206 | ✓ | ✓ | "the project-level skill takes precedence and the user-level skill is ignored." | 11 ✓ | ✓ 1×, under "Skill location" | ✓ |
| S207 | ✓ | ✓ | "Ensure skill names are unique across all locations" | 8 ✓ | ✓ 1×, under "Troubleshoot loading", third check | ✓ |
| S208 | ✗ (no URL; "the Microsoft page") | ✗ in § Gate (date only in § Status changes) | "All three skill tools require approval by default." | 8 ✓ | ✓ 2× | ✗ "tool-approval sections"; the page has both under "Use Agent Skills with Harness Agent", and the `Tool approval` h2 carries a different sentence |

S206's 12 was corrected to 11 in the 07:25 Gate — verified; the current row also says 11. S201's
carried anchor is 14 words (current row 14; base row said 13 — see F6). S202's shaping note's quote
is 9 words and matches the raw README line after the `**` removal.

## Verified positives

- **S203–S207 admission records**: URL, `2026-10-25`, ≤25-word located quote and section all
  present; all five quotes verbatim on today's pages; counts now correct.
- **Shaping notes (R68-4)**: the Gate names exactly the removed bytes — S200's `<code>` around
  `.kilo/skills/` (raw `Project skills (<code>.kilo/skills/</code> in a repository) …`) and S202's
  `**` around "Standard Agent Skills path" (raw README line 755: `2. **Standard Agent Skills path**
  (project root, trusted folders only): …`). Q53's literal `sed -n '<L>p'` paste is still absent;
  the byte claims themselves are right.
- **The ledger's rows**: `git diff a5f7459` shows six added rows and no row deleted; the current
  rows are tier A, which the Gate's new "Tier" paragraph explains (official client docs → A) and
  the Status changes now matches.
- **Quarantine slice**: 13 rows = 7 `payload-absent` (S151, S167, S168, S172, S176, S180, S185) +
  6 `unreachable` (S169, S236, S237, S238, S239, S243); S185 is Roo Code and S172 Junie in the
  register. I re-opened two: S185's "Skill locations" has 0 occurrences on the Roo page, and S172's
  span is broken by the Junie `<code>` parentheticals; both verdicts hold.
- **Guard proof**: `assimilation/guard-proof/collisions` contains `S203`, `collisions-col0` is
  empty — the 0–3-space pattern catches the indented row and the column-zero pattern misses it.
- **Index and amendment**: `corpus/README.md:130` indexes the entry; the r68 entry carries the
  amendment; the watchdog line (`.ufo/watchdog.log:1309`) confirms attempt 1 died 13 minutes in on
  a Cursor `PROVIDER_ERROR`.
- **Delta against round 50** (`:37-44`): accurate — the round-50 entry's "which one wins" column
  has same-name rules for six client pages (opencode, VS Code, Claude Code subagents, Copilot CLI,
  Gemini CLI, Claude Code skills), opencode's exact sentence is there from S024, and the four new
  clients + synthesis are the new ground. The V1/V2 route facts are verified above.

## Residual risk / verification gaps

1. **The lane is moving.** The Gate changed at 07:17:50 and 07:25:59, SOURCES at 07:23:49, the r68
   entry at 07:24:16. The findings above are against the 07:25:59 Gate and the 07:23:49 registry;
   a further edit invalidates the stale sentences (S208 bullet, S201 log line) and must be
   re-checked. The lane's seats are bound not to write `corpus/`; whoever wrote the 07:23/07:24
   edits should be recorded (and the S201 protected-cell edit reconciled with Q34).
2. **Five of the seven `payload-absent` rows** (S151, S167, S168, S176, S180) were not re-opened by
   this seat; the Gate's "every payload-absent row refused" is a 7-row universal evidenced only by
   the slice's labels plus my two spot-checks.
3. **The Microsoft page has no snapshot/sha in the Gate.** My fetch is today's en-us HTML; if the
   L1's fetch differed, the S208 section finding needs the L1's bytes. A committed snapshot (or the
   printed sha256) would settle it.
4. **C1/C2/C3 counters were not run by this seat** (other seats own them); this report is the
   source-record review only. The S208 anchor/W04/append-only findings are conditions those
   counters do not check.
