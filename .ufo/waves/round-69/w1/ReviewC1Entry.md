# ReviewC1Entry — C1 depth, skill name-collision precedence

Seat: `L1Kotoba69-2.ReviewC1Entry` (read-only leaf; no lane mutation).
Claim reviewed: C1 (`plans/round-69.md:20-52`), content draft
`corpus/knowledge/skill-name-precedence-round69.md` plus its registry rows S203–S207 and its
`corpus/README.md` index row. Base lane tip `a5f7459f`; branch tip measured `a238989a`.
Bar: QUALITY Q12, Q25, Q26 (and the plan's frozen counter semantics).

## Verdict

**Content passes Q12's shape and the frozen counter — but only from the uncommitted working
tree. At the branch tip the counter is `0 of 5`.** Independently re-opened, all five quotes are
verbatim and the five paraphrases are supported by their pages. Three defects must be repaired
before admission; the counter cannot see any of them:

1. **HIGH — the novelty premise is false.** `skill-selection-rules-round50.md` already holds
   same-name collision rules for five pinned clients, including opencode's *identical* sentence
   (`skills.md:229`). The entry's intro and the plan's "the lane holds no such ground" are
   contradicted by lane bytes; the opencode row adds no ground and S207 duplicates S024.
2. **HIGH — a false Limits clause.** "Five clients, none of them the lane's pinned seven" is
   wrong: opencode *is* one of the pinned seven.
3. **MEDIUM — the H1 asserts a winner the entry itself denies** for opencode, and the counter
   never measures a winner.

Recommendation: revise (F1–F4), commit the entry + rows, and re-capture the self-test receipt
(F5) before C1 is scored as backed at a tip.

## What I ran (all in `/tmp/r69c1-review`, never in the lane)

```
# worktree measurement, verifier + the three corpus files copied to a scratch root
python3 -B verifiers/check_skill_precedence.py            -> "skill precedence backed 5 of 5", exit 0
python3 -B verifiers/check_skill_precedence.py --fetch    -> "live quotes found 5 of 5", exit 0
python3 -B verifiers/check_skill_precedence.py --self-test-> 0 failure(s) over 18 assertions, exit 0
# git clone --shared of the lane
python3 -B verifiers/check_skill_precedence.py --rev HEAD -> "backed 0 of 5 / entry missing", exit 1
python3 -B verifiers/check_skill_precedence.py --rev a5f7459 -> "backed 0 of 5 / entry missing", exit 1
# partial world: entry present, S203–S207 rows stripped from SOURCES.md
plain run        -> "backed 0 of 5" + five "no 11-cell row" findings, exit 1
--self-test      -> Traceback KeyError: 'S203' at check_skill_precedence.py:315, exit 1
```

Independent page re-open (2026-10-25, five URLs fetched with curl, tags stripped) confirmed each
quote in context; `--fetch` and my own fetches agree.

## Findings

### F0 — HIGH (evidence, blocking): the claim is not measurable at the branch tip

`--rev a238989a` prints `skill precedence backed 0 of 5` / `entry missing`, exit 1. `git ls-tree`
at the tip has no `corpus/knowledge/skill-name-precedence-round69.md`, and `git show
a238989:corpus/SOURCES.md` has no S203–S207 rows (the entry is `??` and both registries are `M`
in `git status`). The 5-of-5 result exists only as a working-tree measurement, which the plan's
C1 bound (Q33: "the counter reads the measured revision's own bytes") and its own predicate
`--rev <rev>` exclude. Fix: commit the entry, the five rows and the README row, then record
`--rev <new-tip>` (and `--self-test`) receipts.

### F1 — HIGH (Q26 + depth): the "no such ground" premise is false; opencode restates r50

- Entry `:13-15`: "the round-50 entry `skill-selection-rules-round50.md` only covers how clients
  choose between *differently named* skills."
- `corpus/knowledge/skill-selection-rules-round50.md:16` has column
  `| "which one wins" rule documented |`; `:18` (opencode) quotes **the same sentence the new
  entry uses**: "Ensure skill names are unique across all locations" (`skills.md:229`); `:19`
  VS Code ("the primary root takes precedence"), `:22` Copilot CLI ("first-found-wins
  precedence"), `:23` Gemini CLI ("the version from the higher-precedence location is used"),
  `:24` Claude Code skills (name clash by origin; nested by working directory). `r51:47` and
  `r51:138-139` add Claude Code nested-skill and Copilot SDK same-name rules.
- `corpus/README.md:72` is a Coverage-map row for that ground ("the documented rules decide
  between copies of one name"), contradicting `plans/round-69.md:24-26` ("the coverage map has no
  row for it").
- `corpus/SOURCES.md:37` (S024, tier A) already anchors opencode's
  "§ Troubleshoot loading `skills.md:223-231`" — the exact section S207 re-opens at tier B for
  the same quote.

So the genuinely new ground is **four non-pinned clients (Roo, Amp, Deep Code, Junie) plus a
cross-client synthesis**; the opencode row is a restatement. Fix: say so in the intro/Scope (and
drop or explicitly mark the opencode row as repeating r50/S024). The counter never reads r50, so
it cannot fail on this — the Q26 clause is currently unsupported.

### F2 — HIGH (factual, Q26): "none of them the lane's pinned seven" is false

Entry `:45-46`: "Five clients, none of them the lane's pinned seven; a pinned client's collision
rule is not claimed here." The pinned seven are enumerated lane-side in
`corpus/knowledge/client-trust-gates-round68.md:56`:
`Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI, opencode, Cursor`. **opencode is pinned**,
and the entry's own `:25` row claims its rule. The counter passes because it never reads the
pinned list (Q26: a clause no guard turns on). Fix: state the true boundary ("four clients
outside the pinned seven; the opencode row restates r50").

### F3 — MEDIUM (Q26): the H1 asserts a winner the entry denies

Entry `:9` — "# Skill name-collision precedence by client — **which same-named skill wins**" —
while `:25` records "no precedence stated" for opencode and `:33` says "One client states no
order at all." Four of five have a winner; the title claims five. The counter measures
provenance, never a winner. Fix: title to "what each client documents about two same-named
skills" (the intro at `:11-12` already says this).

### F4 — MEDIUM (depth/precision): "The orders differ in kind" misclassifies Roo and Deep Code

Entry `:30-32` labels Roo Code "scope", Deep Code "root", Amp "source". The pages:

- Roo `Override Priority`: "When skills with the same name exist in multiple locations, this
  priority applies (highest to lowest)" — an 8-row list ordered project→global, then `.roo/`
  before `.agents/`, then mode-specific before generic.
- Deep Code `Scan Locations`: 1 Project `./.deepcode/skills/`, 2 Project `./.agents/skills/`,
  3 User `~/.deepcode/skills/`, 4 User `~/.agents/skills/`, 5 Global built-in.

Both are the **same lexicographic family** (scope, then native root, then specificity for Roo);
they are not different "kinds". Only Amp ranks a flat *source* list (":5" order, first skill with
a given name wins); Junie is single-key scope. Not measured by the counter. Fix: re-ground the
classification or bound it ("three of the four rank locations; Amp ranks sources").

### F5 — MEDIUM (Q25): the committed self-test receipt is red; no post-entry receipt exists

`.ufo/waves/round-69/controls/freeze-receipt.txt` records

```
== check_skill_precedence --self-test
selftest setup failed: the entry is not present in the working tree
exit=2
```

i.e. the frozen non-vacuity evidence on file is pre-entry and failing. `.ufo/waves/round-69/recapture/`
holds only `check_client_trust_gates.py` receipts (`C1-*.txt` names collide with this claim but
measure the r68 counter), so no green C1 self-test receipt is committed. Current worktree is green
(I ran 18/18). Fix: capture `--self-test` (and `--rev <tip> --fetch`) receipts post-entry.

### F6 — MEDIUM (Q25/counter robustness): `--self-test` crashes on the partial state

With the entry present and S203–S207 absent, the plain run classifies cleanly (`0 of 5`, five
"no 11-cell row" findings, exit 1), but `--self-test` raises an uncaught
`KeyError: 'S203'` at `verifiers/check_skill_precedence.py:315` (`row = rows[first]`) after the
honest-world assertion prints. The frozen semantics name a content verdict (exit 1) and an
unreadable environment (exit 2); a partial state is neither, and entry-before-rows is a plausible
commit order. Fix: `row = rows.get(first)` and let that conjunction fail cleanly.

### F7 — LOW (Q25 evidence): the junk control is not reproducible from lane bytes

`controls/C1-junk-control.txt` cites "sandbox commit 95651d4d6a465d7986f993cfe9c47b394fd53ea0";
in a lane clone `git cat-file -t` reports "could not get object info" and no ref contains it. The
conjunct is independently covered by the self-test's "no source line" world (I ran it: rejected,
`0 of 5`), so impact is receipt hygiene (the M107 class: a line asserted that the lane cannot
re-derive). Fix: re-run the junk world from a committed rev, or cite the self-test world only.

### F8 — LOW (Q12): `recheck:` is prose, not a command

`:7` — "90d — re-fetch all five pages and confirm each located quote and the rule it carries are
unchanged". Q12 asks for "a `recheck:` that runs"; the entries of r50/r51 carry a runnable loop
plus the verifier. r67/r68 use prose too, so this is a lane-wide soft gap rather than a C1
regression; the cheap fix is to name the instrument the README row already cites:
`python3 -B verifiers/check_skill_precedence.py --rev <rev> --fetch`.

### F9 — LOW (precision): the Roo Limits sentence names "heading lines"

`:44-47` says the root label rests on "the unshaped 'Roo-specific (higher priority)' heading
lines". On the fetched page those are `#` comments **inside a fenced code block** under "Choose a
location", not headings; and the root rule also has a marked-up statement ("`.roo/` paths always
take precedence over `.agents/` paths at the same project level", `<code>`). The Limits' account
of where the rule lives is imprecise, though the chosen located quote is admissible under Q42.

### F10 — LOW (precision; from ScoutAmp, verified here): Amp "a fixed ordered list"

Amp's order item 8 is "Directories in `amp.skills.path`, in the order they are configured", so the
membership/order within that item is configuration-dependent; the list positions are fixed.
"Fixed ordered list" is defensible, but "fixed" invites the over-read. Not a defect; scope it if
the cell is edited. (ScoutAmp's second point — personal > workspace repository only, project
`.agents/` still outranks the personal repo — does not bite: the entry does not quote the second
sentence.)

## What checked clean (verified, not assumed)

- **Q12 shape (counter-green and hand-checked):** five `source:` lines open the file, each naming
  the S-id, the registry `source` cell verbatim (so `row[1] in tail`), a section anchor and a
  ≤25-word located quote; then `verified-at: 2026-10-25`; then `recheck:`. `_provenance` green.
- **Quotes are real and in context** (my own fetches): Roo "Override Control" bullet in "What
  Skills Let You Do"; Amp under "Skill Sources and Precedence" after the ordered list; Deep Code
  under "Scan Locations" before the priority table; Junie's skill-location sentence (repeated in
  its conflict checklist); opencode "Troubleshoot loading" third check. opencode's three
  "override" hits are nav and permissions, not skill precedence — the negative "no precedence
  stated" survives a read.
- **Per-client map:** five rows, five distinct clients, each naming exactly one S-id and carrying
  that id's located quote plus a non-empty rule cell (`check()` counts 5).
- **Registry rows:** S203–S207 are 11-cell `mined` rows, `opened 2026-10-25`, `recheck 90d`,
  `used-by corpus/knowledge/skill-name-precedence-round69.md`; appended (diff is insertions only).
- **Index:** `corpus/README.md:130` under `## Coverage map`, path cell exactly
  `` `knowledge/skill-name-precedence-round69.md` ``; `_indexed` green.
- **Counter non-vacuity:** self-test kills all 18 worlds (entry missing, no source line,
  provenance not at the opening, four ids, unresolvable id, not mined, wrong opened, used-by,
  source cell absent, verified-at, recheck, quote not in anchor, table row loses quote, row
  duplicated, shared client, no index row, missing-entry classification); base `a5f7459` is
  `0 of 5` exit 1.

## Residual risk / gaps

- The claim is documentary only; no client was run and no rule was observed, as the entry's
  Limits state. Fine for this surface.
- S203–S207 do not pin fetch bytes (no sha256/size), matching the r68 rows but not r50/r51; drift
  is detectable only by prose re-read or `--fetch`, which proves quote presence, not rule
  fidelity.
- The paraphrase of each rule is unmeasured by the counter (only the quote's presence is): a
  wrong rule cell passes. F3/F4 are exactly that class and need human repair.
- I did not judge C2/C3 or the plan's band move; not in this seat's scope.
