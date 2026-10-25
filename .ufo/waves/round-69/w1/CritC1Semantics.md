# CritC1Semantics — round 69, wave 1 (C1 depth claim, semantic attack)

Seat: `L1Kotoba69-2.CritC1Semantics`. Read-only: no lane file, index or jj state was written; the
worlds below were built under `/tmp` from copies of the lane's working-tree bytes.

## What was attacked

The C1 claim sentence, as frozen in `plans/round-69.md` § C1 and repeated in `SKILL.md:517`:

```
python3 -B verifiers/check_skill_precedence.py --rev <rev>  ->  "skill precedence backed N of 5"
```

and the entry it certifies, `corpus/knowledge/skill-name-precedence-round69.md`. The question asked
of this seat: **does "backed 5 of 5" mean that the five pages back the entry?** Four sub-questions:
(1) is each `source:` row quote verbatim on its page, (2) is each per-client rule cell a fair reading,
(3) do the two synthesis claims ("four of five resolve by order"; "the orders differ in kind") hold
on the five pages, (4) does anything in the five pages contradict the entry's `## Limits`.

## Method and the exact bytes measured

Five pages re-opened with `curl -sSL -A 'Mozilla/5.0 …'` on 2026-10-25, raw HTML kept, then
tag-stripped and line-numbered (`/tmp/c1sem/raw/<client>.{html,txt}`):

| id | URL as recorded | HTTP | served bytes | served URL / note |
|---|---|---|---|---|
| S203 | https://docs.roocode.com/features/skills | 200 | 71,129 | **301 →** https://roocodeinc.github.io/Roo-Code/features/skills/ |
| S204 | https://ampcode.com/docs/customize/skills | 200 | 102,591 | as recorded |
| S205 | https://deepcode.vegamo.cn/en/docs/configuration/agent-skills | 200 | 163,923 | self-canonical, title "Agent Skills \| Deep Code Docs" |
| S206 | https://junie.jetbrains.com/docs/agent-skills.html | 200 | 38,509 | as recorded |
| S207 | https://opencode.ai/docs/skills/ | 200 | 71,581 | v1 route |
| (V2, prose-cited) | https://opencode.ai/v2/docs/skills | 200 | 34,294 | sha256 `786c87e6…` today (S064 recorded 32,694 B / `243e8890…`, 2026-10-22) |

Lane bytes measured at 2026-10-25T07:23–07:26Z:

```
9d907e3f21d76ed8792ca8487f7a5f2241b38dc0c797c7eb743dabc09bbce657  corpus/knowledge/skill-name-precedence-round69.md
31292a39f112b529e620642c80c92a99b58533adbd037706eabf87a742cd6afb  corpus/SOURCES.md
85dfaf7a2c053387319fdf458621007ef7852642ea521c6ee9e0ab9abaa8f705  corpus/README.md
9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48  verifiers/check_skill_precedence.py  (frozen; = freeze receipt)
dc9f150764431ec612e9632111405f54afb6392759c85af3f55bfd835c5ac246  verifiers/check_skill_precedence.py  (working tree, uncommitted)
```

The lane was **live** while this audit ran: the entry and `corpus/SOURCES.md` were rewritten at
07:23:11Z and 07:23:49Z (r50 prior-ground disclosure, B→A tier, S207 retitled "served V1 docs
page"). Findings below are stated against the hashes above; anything the revision already fixed is
marked *fixed in flight*, so the L1 does not re-litigate it.

---

## P1 — the claim's own predicate is red right now (counterexample)

`skill precedence backed 5 of 5` **does not hold on the measured working tree**. Both the frozen and
the working-tree counter print, verbatim, on a refreshed `/tmp` shared clone:

```
measured-rev: working-tree
skill precedence backed 0 of 5
  - S207: the row's source cell is not in the entry's source line
exit=1
```

Cause: `SOURCES.md:148` now titles the row `opencode — Agent skills (served V1 docs page)`, the
entry's `source:` line (`:5`) still says `opencode — Agent skills (served docs page)`, and the
counter requires `row[1] in tail` (`check_skill_precedence.py:214-216` frozen; `:223-225` live).
The retitle landed 38 s after the entry edit and the two are not atomic.

Evidence that this is a one-string propagation miss, not a deeper break: replacing only
`(served docs page)` → `(served V1 docs page)` in the entry returns `(5, [])` under **both** counter
versions. So the claim's headline number is, at this instant, false while every structural conjunct
is satisfiable.

## P2 — "backed 5 of 5" is citation plumbing, not entailment (counterexample battery)

What the counter actually reads: five `source:` ids → 11-cell `mined` rows opened 2026-10-25 whose
`used-by` names the entry; `row[1]` occurs in the entry's source-line tail; one ≤25-word double
quoted span occurs in `row[5]`; exactly one entry table row contains the S-id, has a client cell and
a (live: ≥6-word) rule cell and carries the quote; five distinct clients; an index row exists. It
**never reads the rule cell's meaning, and never reads the prose at all** (`check()` at
`:184-240` frozen, `:193-256` live; the invariants pass through `cells[0]`/`cells[1]` only as
non-empty/word-count tests at `:226`/`:238-241`).

Six worlds plus four quote/plumbing worlds, each one declared substitution, run through both counter
versions (`/tmp/c1sem/controls/snapshot_matrix.py` and the consolidated run that produced this
table). Base = the measured entry with the one-string S207 title fix, so P1 does not mask the
semantic conjuncts:

| world (one substitution) | frozen `9c796574` | live `dc9f1507` |
|---|---|---|
| honest base | 5 | 5 |
| Roo rule cell inverted ("a global skill beats a project one") | **5** | **5** |
| Amp rule cell invents a first-wins scope rule | **5** | **5** |
| Junie rule cell claims a general project-over-user rule | **5** | **5** |
| synthesis bullet inverted ("All five cited routes merge a collision") | **5** | **5** |
| Limits pinned line inverted ("all five are non-pinned … every pinned client is out of scope") | **5** | **5** |
| SOURCES anchor sentence contradicts its own rule cell | **5** | **5** |
| located quote replaced everywhere by a 5-word heading ("What Skills Let You Do") | 0 | **5** |
| located quote replaced everywhere by a 2-word heading ("What Skills") | 0 | 0 |
| located quote changed only in the `source:` line (table keeps the real one) | 5 | 5 |

So: a counter-green entry can state the opposite of the pages on all five rows, can negate its own
Limits, and (live version) can carry a five-word section heading as its "located quote". The number
certifies that citations are *plumbed*, not that the map is *true*. **This is the semantic gap the
claim sentence hides.**

Why the heading world passes the live counter but not the frozen one — mechanism, measured: the
candidate pool is `_quoted(_norm(entry))`, i.e. **every** 5–25-word double-quoted span in the whole
entry, including `source:` lines, the `## Limits` prose and the synthesis; `_row_quote` then picks
the longest pool member that is a substring of the SOURCES anchor (`:178-181`). With the real
sentence removed, the live counter's longest surviving match is the source line's section name
"`What Skills Let You Do`", which the table row carries → 5. The frozen counter has no word floor,
so a 3-word Limits label ("`Roo-specific (higher priority)`", `:45`) wins the longest match and the
row does not carry it → 0. Neither outcome is a designed guarantee.

Correction to a peer claim: `MutC1Counter`'s F3 (a 2-word section title passes) is **true of the
frozen bytes**, reproducible with S206 ("Skill location": no competing short label in that anchor),
and **false of the working-tree bytes**, whose five-word floor rejects it — my S206 reproduction
against the live file returns `0 of 5` with `S206: no located quote of the entry occurs in the
row's anchor cell`. The live counter re-opens the same class at five words, as the table shows.

## P3 — the frozen predicate has changed identity since the freeze (false provenance)

`controls/freeze-receipt.txt` records `9c796574…  verifiers/check_skill_precedence.py`. That is the
committed blob (`git show HEAD:…`, base commit `a238989`) — and the working tree is `dc9f1507…`,
uncommitted (`git status` → ` M`), mtime 07:21:28Z, **47 insertions / 12 deletions**. No wave-1
report or receipt names the change (`grep -rln '5 <= len|dc9f1507|quote floor' .ufo/waves/round-69/`
→ empty).

Semantic content of the drift:

1. quote floor `0 <` → `5 <=` words, docstring: "a shorter span of five words or more is never
   satisfied by a section title";
2. rule cell must be "a sentence of at least six words" and the client cell must not be an S-id;
3. the quote must occur in the table row's **quote cell** (`cells[2]`), not anywhere in the row;
4. the coverage-map row must sit under a `## Coverage map` heading;
5. the source-line tail must be ≥20 chars;
6. `_source_rows` keeps the first duplicate row;
7. self-test gains five broken worlds, temp cleanup, `--repo` directory check.

Consequences for the claim's meaning:

- `plans/round-69.md` ("each row's anchor carries a ≤25-word located quote"), `SKILL.md:517`
  ("located quotes (≤25 words)") and the freeze receipt all describe version A; the file that
  produces today's headline is version B. A reviewer who re-runs the frozen artifact (as
  `MutC1Counter` did from `/tmp/k69-mut-c1`) and a reviewer who runs the lane get different verdicts
  on the same content.
- **No recorded control discriminates A from B.** `controls/C1-base.txt` ("entry missing") and
  `controls/C1-junk-control.txt` ("no `source:` lines") are version-insensitive; the honest world is
  5/5 under both. The drift is invisible to every receipt the round holds.
- SKILL.md's gate row states the weaker predicate, so the lane's own gate registry now under-describes
  the gate that ran.

## P4 — the four page-level questions

### (1) verbatim quote — 5 of 5 pass

Each located quote occurs exactly once in its page's raw HTML (one additional occurrence of S205's
sentence on the Deep Code page):

| id | found at (extracted text line) | page section |
|---|---|---|
| S203 | `roo.txt:82` | `What Skills Let You Do` (`:65`), bullet `Override Control` (`:81`) |
| S204 | `amp.txt:121` | `Skill Sources and Precedence` (`:102`) |
| S205 | `deepcode.txt:36` | `Scan Locations` (`:33`) |
| S206 | `junie.txt:132` | `Skill location` (`:83`) |
| S207 | `opencode.txt:366` | `Troubleshoot loading` (`:357`), 3rd of 4 checks |

Every `source:` line's section claim is accurate. S206's `SOURCES.md` word-count annotation is wrong
(`(12 words)`; the quote is 11), and nothing checks it.

Provenance note: S203's recorded URL is a 301 to a GitHub Pages host; the `--fetch` arm follows
redirects and prints only `found`, so the receipt cannot say which host served the quote. Two further
leniences, both measured: `fetch()` (`:269-273`) tests quote *presence* only, so the entry's own
`recheck: 90d — … confirm each located quote **and the rule it carries** are unchanged` (`:7`) has no
implementation anywhere (a page that kept the sentence and reversed the rule still passes); and the
`source:` line's "located quote" clause is never compared with the table's quote cell — changing only
the source line leaves the counter at 5 of 5 (last row of the P2 table).

### (2) fair reading of the rule cells — 3 clean, 1 partly, 1 with an uncounted citation

- **Roo Code** — fair, and the in-flight revision fixed the defect I had drafted. The page's
  `Override Priority` ladder (`roo.txt:226-280`) is scope → root → mode
  (project/`.roo`/generic at #2 beats project/`.agents`/mode-specific at #3), so the old cell's
  unqualified "mode-specific beats generic" ranked the keys wrongly. The current cell says "the
  page's own precedence ladder orders locations before it orders mode-specific against generic —
  the quote's two clauses are therefore not independent" (`:22`): **page-supported, no defect left**.
- **Deep Code** — fair. `deepcode.txt:34-36` is explicit ("If multiple skills resolve to the same
  name, only the highest-priority one is kept") and the table (`:37-60`) is Priority 1 Project
  `.deepcode`, 2 Project `.agents`, 3 User `.deepcode`, 4 User `.agents`, 5 Global built-in. The
  cell's "(project roots before user roots)" is exactly that.
- **Amp** — the cell is a fair reading of the sentence it quotes, but it omits the one direction the
  page states and the claim's readers need. `amp.txt:103-105`: "Amp uses the first skill with a
  given frontmatter name. The order is:" then items 1–11 (`:106-120`). Item **2** is
  `~/.agents/skills/` and item **4** is `.agents/skills/` in the project → **a home-level
  `.agents/skills/<name>` masks a project-level `.agents/skills/<name>`**. Item **5** (project
  `.claude/skills/`) precedes item **6** (`~/.claude/skills/`) → for the `.claude` pair the
  direction reverses *inside the same client*. The entry never states either. "Fixed ordered source
  list" (`:23`) also over-reads item 8, "Directories in `amp.skills.path`, in the order they are
  configured" (`:115-117`).
- **Junie** — partly unfair. The page's rule is scoped to one pair of roots: "If a project-level
  (`<projectRoot>/.junie/skills/<skill-name>/`) and a user-level (`~/.junie/skills/<skill-name>/`)
  skills share the same name, the project-level skill takes precedence and the user-level skill is
  ignored." (`junie.txt:128-132`, restated at `:366`). But the same page loads `.agents/skills/` in
  the project and in `~`, extension skills, `--skill-location` folders and built-ins (`:97-127`) and
  states **no** collision rule for any of them. The cell's unqualified "scope order: project-level
  beats user-level" (`:25`) and the Limits (which discloses Roo's shaping and opencode's pinning but
  not this) let a reader infer a general Junie order the page does not give.
- **opencode (V1 route)** — fair on the V1 page: six locations are listed (`opencode.txt:112-124`),
  no `precedence`/`priority`/`first`/`wins` statement exists on it, and the uniqueness check is the
  3rd of 4 under `Troubleshoot loading` (`:366`). The in-flight revision correctly narrowed the row
  to "V1 route" and named the V2 ladder. **But the citation that carries the narrowing is false
  provenance**: `:26` says "(registry row S064, § Precedence)", while S064's anchor cell is
  "§ IDs … § Frontmatter `:140` … § Loading `:184`" — no § Precedence — and S064 was mined on
  2026-10-22 at 32,694 B / `243e8890…`, whereas the V2 page today is 34,294 B / `786c87e6…`. The row
  neither anchors nor covers the section it is cited for, and `:47-48` of the entry half-admits this
  ("mined in round 54 for a different question"). The five `source:` ids do not include S064, so the
  counter cannot see the citation at all.

### (3) the two synthesis claims

- **"Four of the five cited routes resolve a collision by order, not by merging."** Supported:
  Roo "override" (`roo.txt:81-82`, ladder `:228`), Amp "uses the first skill" (`:103`), Deep Code
  "only the highest-priority one is kept" (`deepcode.txt:36`), Junie "takes precedence … is ignored"
  (`junie.txt:132`); opencode V1 states only uniqueness. No page documents merging. **Holds.**
- **"The orders differ in kind"** — the version I was assigned to attack is gone; the current bullet
  is the corrected one ("The orders are not three different kinds. Roo Code and Deep Code both order
  scope first … and the native root before the shared one; Junie states only the project/user pair;
  Amp is the one flat source list"). That is page-accurate. **But the same bullet still ends on
  "The same pair of skills can still resolve differently on two clients, because the orders name
  different keys" without naming the one page-backed case that would demonstrate it** — the Amp
  `.agents` inversion in (2). The claim a skill author can act on is missing precisely where the
  pages supply it, and Amp's internal `.agents`/`.claude` reversal makes it sharper than a generic
  "different keys" sentence.

### (4) do the five pages contradict the Limits?

- "Documentary evidence only…" — no contradiction.
- Roo bullet (`:44-46`): `<strong>` around project/global, `<code>` around `.roo/`/`.agents/` — I
  verified the raw HTML: `<p>A <strong>project</strong> skill always overrides a
  <strong>global</strong> skill of the same name. Within the same project level, <code>.roo/</code>
  overrides <code>.agents/</code>.</p>`; and the "Roo-specific (higher priority)" labels are inside
  code fences (`roo.html` lines 40/42, `token plain` spans). **Accurate.** One residual: the
  Limits presents the root order as markup-bearing only, but the same section's lead sentence is
  **plain** and states the collision surface directly — "When skills with the same name exist in
  multiple locations, this priority applies (highest to lowest)." (`roo.txt:228`, HTML `<p>` with no
  inline tag, 16 words ≤ the 25-word ceiling). Under QUALITY Q42's "an unshaped quote from the same
  page when one exists", that is the better located quote, and the chosen bullet never says *same
  name*. So the entry's only Roo quote is off the claim's own surface while an on-surface, unshaped,
  ≤25-word sentence sits on the page.
- Pinned-client bullet (`:47`): "opencode is one of the lane's pinned clients" — **now true**; the
  earlier "none of them the lane's pinned seven" was false (pinned set: Claude Code, Codex, VS Code,
  Copilot CLI, Gemini CLI, opencode, Cursor — `client-trust-gates-round68.md:56-57`,
  `PROVINCE.md:22`). This is the one Limits line I would have called decisive; it is fixed.
- "Five clients, all English pages, read 2026-10-25" — the pages are English; S204/S205's hosts are
  third-party/self-published docs (Amp's own site; a `*.vegamo.cn` host that self-canonicalises), and
  no page contradicts the Limits. The clause is accurate but silent on the V2 route that the cell
  now leans on.

**Net answer to (4): no page contradicts the current Limits; one Limits omission (Junie's
`.junie/skills`-only rule) and one inaccurate justification (the Roo collision sentence is unshaped
and quotable) remain.**

## Prior ground and a duplicate registry row

The in-flight revision now discloses that `skill-selection-rules-round50.md` holds a "which one
wins" column with same-name rules for six client pages (`:13-16`), which is correct
(`skill-selection-rules-round50.md:16` header; `:18` opencode, `:19` VS Code, `:22` Copilot CLI,
`:23` Gemini, `:24` Claude Code; `README.md:72` "the documented rules decide between copies of one
name"). Good — that closes the false-novelty finding.

What the revision did **not** close: **S207 duplicates S024.** Same URL, same section, one fact, two
`mined` rows: S024 (`SOURCES.md:37`, opened 2026-10-22) anchors "§ Troubleshoot loading
`skills.md:223-231`" and its rule cell already records "its only collision controls are name
uniqueness across locations and `opencode/autoinvoke: \"false\"`"; round-50's entry quotes the
sentence verbatim at `skill-selection-rules-round50.md:18` (`skills.md:229`). S207 (`:148`) is the
second registry row for that source. The counter's five-distinct-clients test cannot see it (it
compares client cells, not sources), so `5 of 5` is reachable with one authority counted twice inside
the five.

## Impacted axes

- **depth (C1, owned, 9)** — the number is a plumbing measure; at the measured instant it is 0 of 5,
  and the entry's remaining prose gaps (Amp direction, Junie scope) are exactly the depth the round
  promised.
- **consistency (C2, owned, 10)** — the gate now has two identities and three stale descriptions:
  `plans/round-69.md`, `SKILL.md:517` and `controls/freeze-receipt.txt` all describe/record version A
  (≤25 words, entry `9c796574`), while the file that runs is version B (`dc9f1507`, uncommitted,
  5–25 words + ≥6-word rule cell + quote-cell-only + `## Coverage map` heading + first-row dedupe).
  `README.md:130` also still carries the retracted synthesis ("Deep Code by root, Amp by source, and
  opencode states only a uniqueness rule") and the "five clients" framing that the entry's own body
  now contradicts.
- **sourcing/provenance** — S064 cited for a section its anchor does not hold and whose bytes have
  changed since it was mined; S207 a duplicate of S024.

## Smallest safe correction

Ordered, each independently verifiable:

1. **Make the S207 title atomic** (one string, entry `:5`): `opencode — Agent skills (served docs
   page)` → `opencode — Agent skills (served V1 docs page)`. Verified: restores `(5, [])` under both
   counter versions. Do it in the same commit as the `SOURCES.md` retitle, or neither.
2. **Resolve the freeze drift explicitly**, do not bury it: either revert the counter to `9c796574…`
   (then the 5-word/6-word/quote-cell hardening is a new round's proposal), or land the working tree
   as the measured predicate and re-issue `controls/freeze-receipt.txt` + `SKILL.md:517` + the plan's
   "Counter semantics" sentence with the new sha256 and the new conjunct text. A control that
   distinguishes A from B (a 2-word heading world) belongs in `--self-test` either way.
3. **Fix the V2 citation** in `:26`/`:47-48`: cite the fact to the page read today
   (`https://opencode.ai/v2/docs/skills`, § Precedence, "the source registered later supplies the
   skill that OpenCode loads", 34,294 B / `786c87e6…`) and either append a new registry row for
   § Precedence or drop the S064 parenthetical. S064's bytes no longer match the page it names.
4. **Amp cell**: add the two directions — "`~/.agents/skills/<name>` masks the project's
   `.agents/skills/<name>` (order items 2 before 4), while the project's `.claude/skills/<name>`
   masks `~/.claude/skills/<name>` (items 5 before 6)" — and drop "fixed" or say "the
   `amp.skills.path` entries follow their configured order". Then name that pair in the synthesis
   bullet as the concrete case of "resolve differently on two clients".
5. **Junie cell**: append "on the `.junie/skills/` pair only; the page states no rule for its
   `.agents/skills/`, extension, custom-folder or built-in skills (`junie.txt:97-127`)". Add the
   same to Limits.
6. **Roo quote** (optional but cheap): replace the bullet with the page's unshaped lead sentence
   "When skills with the same name exist in multiple locations, this priority applies (highest to
   lowest)." (16 words, no inline markup) and keep the ladder in the cell. That puts the quote on the
   claim's own surface and retires the "markup-bearing" justification.
7. **README.md:130**: rewrite the row to the entry's current synthesis (four new clients + the
   V1-only opencode route + "orders agree on scope/root except Amp's flat list") — the index row is
   what the next round's readers and `SKILL.md` will copy.
8. **Duplicate row**: supersede S207 with a pointer to S024 (or vice versa) rather than keeping two
   `mined` rows for one URL/section/quote; otherwise every later `5 of 5` can be reached with one
   authority counted twice.

## Scope of this seat's claims

I re-opened the five pages myself; I did not accept any peer's page reading without reproducing it
(`ScoutOpencode`'s V2 ladder: reproduced and confirmed; `MutC1Counter`'s 2-word-heading world:
reproduced and **refuted on the working-tree bytes**, true only on the frozen ones; `ScoutAmp`'s
"personal masks workspace is repository-internal": consistent with items 9/10 of the list, and the
`~/.agents` inversion I report is independent of that sentence). I did not run any client, did not
measure behaviour, and wrote nothing outside `/tmp` and this report.
