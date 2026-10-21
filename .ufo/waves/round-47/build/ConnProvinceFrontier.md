verdict: C2 moves to Core on landing; C1 does not — its stale record re-pins and the Frontier bullet narrows to the unheld per-release re-derivation. Neither move is true at BASE c61a973; both drafts are gated on observed after-values.

# Connector — PROVINCE / corpus README frontier movement (C1, C2)

Scope: determine whether the two halves of the `Loader-rule freshness` frontier item move
to Core, and draft the append-only PROVINCE/README frontier edits + the LOG.md lines that
would record the move. Production files were not written; every edit below was exercised in
a scratch clone at `/tmp/kotoba-r47-final/kotoba-shokunin` (canonical lane layout plus
symlinks to the fleet `.ufo`, `.md` files and `kasegi-shokunin`).

## 1. Determination

| half | moves to Core? | reason |
|---|---|---|
| **C2** — frontmatter `description` XML-token rule | **Yes, on landing.** | The frontier row's "why not held" is a *gate absence* ("unchecked by the lane's own gate"), not an unexplored surface. The surface (frontmatter description craft) is already listed under Core at `PROVINCE.md:12`; once the rule is executed with a discriminating fixture and the lane's own description is tag-free, the absence is gone. This is ordinary growth: `LEARNING.md:73-80` says moving frontier ground into core is recorded in `LOG.md`. No new surface is absorbed, so Core needs one rule bullet, not a new scope claim. |
| **C1** — omp 18.12.3 substrate drift | **No.** The *record* is re-pinned; the *area* stays Frontier, narrowed. | A pinned version is a maintenance state, not a surface. `PROVINCE.md:8-14` lists surfaces and instruments; putting `omp 18.12.5` there would make Core a status board whose claim decays on the next rebuild. The decay is measured, not hypothetical: round 46 recorded 18.12.3 (`PROVINCE.md:21`, `corpus/README.md:74`), the round-47 before-run is 18.12.5 (`before/SUMMARY.md:10`), and at 18.12.5 the omp extractor yields **0 of 8** declared loader classes (`before/SUMMARY.md:4`). Moving C1 whole would also delete the one frontier item that names the residual: the extractor is a fixed call-shape alternation (`verifiers/verify_surfaces.py:150-163`), so every substrate rebuild is followed by a hand re-derivation. Re-pinning closes the *debt instance*; it does not hold the *capability*. |

The compatible synthesis: **split the bullet's fate, do not add a second frontier bullet.**
Core gains only the C2 rule; the existing Frontier bullet keeps its round-46 text verbatim
as a prefix and appends a round-47 note that (a) records the C2 move, (b) retires the
18.12.3 / `5/7` / `1/3` figures as the round-46 record, (c) points live pins at
`verifiers/baseline.json` `measured_against` instead of repeating versions in prose, and
(d) names the residual. The durable live pin values then have exactly one home (the pin
block), and the live docs cannot drift independently of it.

Neither movement is true at BASE: there is no description-tag check in
`verifiers/verify_skill_checklist.py` (the 10 ids are at `verifiers/verify_skill_checklist.py:282-294`;
the frontmatter check's own limit is "a structural parse, not semantic YAML validation",
`:76`), and the substrate gates are red (`before/SUMMARY.md:3-5`). The drafts below are
therefore **conditional**; §6 names every value that must be observed at landing.

Peer cross-check: `MoriR22R.RevPriorRoundReport-9` independently reproduced the two stale
anchors and the pins drift (their P10), the LOG dead-path class (P7), and the
improved-bounded condition for a 4/3 surfaces landing (P11). No disagreement on the
determination; their requirements are carried in §3 (row before→after), §6 (4/3 rule) and
§7.8 (citation hygiene).

## 2. BASE state — exact anchors

All line numbers at `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (`git show`/clone).

| anchor | BASE text / state |
|---|---|
| `PROVINCE.md:21` | `- Loader-rule freshness: the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3) and the frontmatter `description` XML-token rule — …` |
| `PROVINCE.md:10` | `Appended round 46 (LEARNING.md § Province is a frontier); surfaces the lane governs now:` |
| `corpus/README.md:74` | `| Loader-rule freshness | omp 18.12.3 drift leaves surfaces 5/7 and pins 1/3; the frontmatter `description` XML-token rule is unchecked by the lane's own gate | re-derive then re-pin; add the tag rule with a discriminating fixture … |` |
| `SKILL.md:14` | description line `never reach the `<skills>` router — craft here is audit-side, not` (the one frontmatter occurrence) |
| `SKILL.md:151` | `This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47).` |
| `LOG.md:2111` | the pre-existing governance red (`.ufo/round-45/drafts/v10/post-r44-hunt.py` absent) |
| `corpus/SOURCES.md:16` | S003 row: "The description cannot contain XML tags …" (A tier, mined) |
| `verifiers/baseline.json:4-9` | `measured_against` still pins omp `9513ef9f…` / `2026-10-19T12:35:55.628149917-03:00` and opencode `d9123b9b…` |
| `verifiers/floors-registry.json:5-7` | checklist floor `1597`; mirrored at `verifiers/check_assertion_floors.py:121,142` and `:8` |
| `/home/vgpnk/Projects/shokunin/LEARNING.md:73-80` | "Moving frontier ground into core is ordinary growth, recorded in `LOG.md`." |

Measured before-state (round record, `.ufo/waves/round-47/before/SUMMARY.md`):
`surfaces` default exit 2; with the 1.19.3 binary passed explicitly 4 PASS / 3 FAIL
(`literal_present`, `no_uncovered_class` vacuity 0/8, `opencode_extract`); `pins` exit 2,
3/3 failed; checklist exit 1, 9 PASS / 1 FAIL at `LOG.md:2111`; frontmatter `<skills>`
count 1.

## 3. Frontier surfaces — before → after

This is the row movement the round must be able to read off the two live docs.

| surface | BASE (present tense) | After the drafted edit |
|---|---|---|
| `PROVINCE.md:21` | "the omp 18.12.3 substrate drift (surfaces 5/7, pins 1/3) and the frontmatter `description` XML-token rule"; no status | Old text retained as prefix; appended: C2 moved to Core; the 18.12.3/5/7/1/3 figures are the round-46 record; live pins are `verifiers/baseline.json` `measured_against` (omp 18.12.5 / opencode 1.19.3); residual = manual re-derivation after a rebuild (0/8 omp classes at the before-run) |
| `corpus/README.md:74` | "omp 18.12.3 drift leaves surfaces 5/7 and pins 1/3; … unchecked by the lane's own gate"; next probe "re-derive then re-pin; add the tag rule" | Same two cells with an appended round-47 note: C2 moved to Core; C1 figures historical; live pins point at `../verifiers/baseline.json`; still not held = manual re-derivation; next probe extended with "make re-derivation executable / red-gate drill" |
| `PROVINCE.md:12-14` (Core) | surfaces + instruments only | One appended bullet: the C2 rule is executed by `verifiers/verify_skill_checklist.py` `trigger.description_no_xml_tag`, with its re-run command. No substrate-version bullet. |

Deliberate non-edit: **no C1 bullet in Core.** See §1 and counterexample C-1.

## 4. Proposed move (one bounded synthesis)

> Record the C2 capability as held (append one Core bullet, retire the C2 half of the
> frontier item in place), and keep the C1 maintenance area on the Frontier in narrowed
> form — the stale version/counts are replaced by a pointer to the pin block and the
> manual-re-derivation residual, not by a Core status line.

Affected axes:
- **freshness +** — the live docs stop asserting 18.12.3/5/7/1/3; the live pins have one
  authoritative home (`verifiers/baseline.json`), so the docs cannot drift independently.
- **operability +** — the S003 rule becomes an executed check with a re-run command; the
  fixture set pins the predicate's scope (description value, not body).
- **calibration +** — the move is recorded per `LEARNING.md:73-80`; C1's capability gap is
  not overclaimed; the old text is preserved and the durable record is the LOG entry.
- **depth / coverage / adjacency 0** — no new surface, no scope absorption, no sibling.
- No harm observed on the corpus or checklist gates (§9).

## 5. Exact drafts

### 5.1 `PROVINCE.md` — append to Core after line 14 (before the blank line and `## Frontier`)

```text
- Frontmatter `description` XML-tag rule (round 47, moved from Frontier): S003's Anthropic rule (`corpus/SOURCES.md`) is executed by `verifiers/verify_skill_checklist.py` check `trigger.description_no_xml_tag` — opening, closing, attribute-bearing and self-closing tags FAIL; a tag-free description and a body-only-tag control PASS; this file's description is tag-free (the former token survives in body prose only). Re-run: `python3 -B verifiers/verify_skill_checklist.py --json`.
```

The check id is this draft's proposal; the bullet must name the **landed** id verbatim. If
the integrator names it differently, regenerate the text rather than leaving a pointer to a
nonexistent check.

### 5.2 `PROVINCE.md` — append to the existing line 21 (old text kept byte-identical as prefix)

Append this clause to the end of the bullet (one space before `**Round 47:**`):

```text
 **Round 47:** the C2 half moved to Core (executed rule, discriminating fixture). The C1 half's round-46 figures — omp 18.12.3, `surfaces 5/7`, `pins 1/3` — are historical: the live pins are the `measured_against` block in `verifiers/baseline.json` (omp 18.12.5, opencode 1.19.3) and both guards are green at default resolution. The area stays here narrowed: re-derivation after a substrate rebuild is manual — at the round-47 before-run omp 18.12.5 yielded 0 extracted omp classes (the extractor is a fixed call-shape alternation in `verifiers/verify_surfaces.py`), so a rebuild is a red gate, never silent drift.
```

### 5.3 `corpus/README.md` — append to the cells of row 74 (old text kept as prefix)

Cell 2, append:

```text
 **Round 47:** C2 moved to Core (the rule is executed with a discriminating fixture); the C1 round-46 figures (omp 18.12.3, surfaces 5/7, pins 1/3) are historical — live pins are `../verifiers/baseline.json` `measured_against` and both guards are green at default resolution. Still not held: re-derivation after a rebuild is manual — 18.12.5 yielded 0 extracted omp classes at the round-47 before-run (fixed call-shape alternation).
```

Cell 3, append:

```text
 **Round 47 next:** make re-derivation executable (a shape-discovery probe that names an unseen call form) or pin a per-release red-gate drill; the tag rule is checked, not probed.
```

Strict diff-append alternative (if "append-only" is meant at the line level, not the content
level): add a new row at the end of the Frontier table instead of touching row 74 —
`| Loader-rule freshness (round 47 status) | C2 moved to Core; C1 re-pinned — live pins in `../verifiers/baseline.json`; residual: manual re-derivation (18.12.5 → 0/8 omp classes) | shape-discovery probe or per-release red-gate drill |`.
Cost: the old row keeps asserting "unchecked by the lane's own gate" and "18.12.3" in the
present tense, so a reader sees two contradictory rows. I recommend the content-preserving
append in the row (old text intact as prefix) and leave the durable history to LOG.md.

### 5.4 `LOG.md` — append at EOF (after the round-46 after-battery entry, LOG.md:2313)

`<CHECKLIST_EXIT>`, `<CHECKLIST_PASS>`, `<CHECKLIST_TOTAL>`, `<PINS_EXIT>`,
`<PINS_PASS>`, `<SURFACES_EXIT>`, `<SURFACES_PASS>` are **must-observe** fields (§6); they
are placeholders, not results.

```text
## 2026-10-21 — Round 47 BUILD — C2 moves to Core; C1 re-pinned, area stays Frontier narrowed

- Base `c61a973b2e02e1ded169703ddcb06466f4edd8bd`. This entry records a frontier move only; it asserts no axis score.
- C2 (operability) — **moved to Core.** The `SKILL.md` frontmatter `description` no longer carries an XML tag (the former token survives in body prose only): `sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'` 1 → 0; description 814 → 820 chars. S003's rule is executed by `verifiers/verify_skill_checklist.py` check `trigger.description_no_xml_tag`: opening, closing, attribute-bearing and self-closing fixtures FAIL; a tag-free description and a body-only-tag control PASS. `python3 -B verifiers/verify_skill_checklist.py --json` exit <CHECKLIST_EXIT>, <CHECKLIST_PASS>/<CHECKLIST_TOTAL> (before 9 PASS / 1 FAIL at `LOG.md:2111`; the remaining red is C3's erratum-registry target in the same wave). The `--self-test` floor is re-recorded in step (registry, both in-file tables, docstring). The stale sentence at `SKILL.md:151` now states the rule is executed.
- C1 (freshness) — **not moved; the debt closes.** Re-derived and re-pinned: omp 18.12.5 sha256 `fdbc8136…`, ns-exact mtime `2026-10-21T03:30:38.135013187-03:00`; opencode 1.19.3 sha256 `179ca421…` at the npx-cache ELF (the pinned `~/.opencode/bin/opencode` path is gone; no gate executes the `~/.local/bin/opencode` wrapper). `python3 -B verifiers/check_substrate_pins.py --json` exit <PINS_EXIT>, <PINS_PASS>/3 PASS (before exit 2, 3/3 failed). `python3 -B verifiers/verify_surfaces.py --json` exit <SURFACES_EXIT>, <SURFACES_PASS>/7 (before exit 2 at default; 4 PASS / 3 FAIL with the 1.19.3 binary passed explicitly); the extraction rules were re-derived, not copied, and every class that no longer exists is re-verdicted with its sweep — no silent drop (Q09, Q14).
- Why C1 stays (`LEARNING.md` § Province is a frontier): a pinned version is a maintenance state, not a surface — Core lists surfaces and instruments, not measurements that decay. The area is not held because the extractor is a fixed call-shape alternation in `verifiers/verify_surfaces.py`, and omp 18.12.5 yielded 0 extracted omp classes before the re-derivation; a rebuild is a red gate followed by a hand re-derivation. `PROVINCE.md` Core takes only the C2 bullet; `corpus/README.md` § Frontier keeps the row with the stale figures corrected and the residual named.
- No Git add, commit or ref operation.
```

### 5.5 C2 prerequisite — `SKILL.md` edits (not frontier text; needed for the move to be true)

`SKILL.md:12-15` (description), old → new:

```text
-  shokunin files are not in an omp skill discovery root, so their descriptions
-  never reach the `<skills>` router — craft here is audit-side, not
-  router-visible.
+  shokunin files are not in an omp skill discovery root, so their descriptions
+  never reach a router's skills catalogue — craft here is audit-side, not
+  router-visible.
```

`SKILL.md:151`, old → new (the current sentence would be false after the move):

```text
-This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47).
+This file's own description carries no XML tag; the rule is executed by `verifiers/verify_skill_checklist.py` (`trigger.description_no_xml_tag`), with a body-only-tag control so body prose is not a false red.
```

Measured effect (production parser, in the canonical scratch layout): description
814 → 820 chars (limit 1024); frontmatter `<skills>` count 1 → 0; body prose keeps the
literal at lines 22, 91, 96, 99, 111 and 430, so the router-model documentation is intact.
The existing trigger checks stay green (`literal_trigger_string`, `anti_trigger_clause`);
the whole checklist stays at 9 PASS / 1 FAIL (only `LOG.md:2111`) after the edit.

### 5.6 If the L1 overrides and moves C1 anyway (not recommended)

The only defensible Core text is a state line, not an area line:

```text
- Substrate pin, round 47 (state, not surface): omp 18.12.5 sha256 `fdbc8136…` with ns-exact mtime `2026-10-21T03:30:38.135013187-03:00`; opencode 1.19.3 sha256 `179ca421…` at the npx-cache ELF; `verifiers/check_substrate_pins.py` exit 0, 3/3. The authoritative values live in `verifiers/baseline.json` `measured_against`; this line must be re-derived on every rebuild.
```

Risk: duplicates the pin block and decays (18.12.3 → 18.12.5 happened inside one round
boundary); if the frontier row is deleted at the same time, the next rebuild has no named
exploration item. I recommend the §1 split instead.

### 5.7 Fallback — if the after-state is not reached

If the description check does not land, C2 does not move; if `verify_surfaces.py` is not
7/7, C1's 7/7 must not be written (my prototype reached only 4/7 after the pin fix). Record
that state instead of a move:

```text
## 2026-10-21 — Round 47 BUILD — C2 <moved|not moved>; C1 stays Frontier (gate red)

- Base `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
- C2: <the check did not land / landed as `trigger.description_no_xml_tag` and the live file passes>; the frontier row keeps the C2 half.
- C1: re-pin attempted; `verifiers/check_substrate_pins.py` exit <E> (<k>/3), `verifiers/verify_surfaces.py` exit <E> (<k>/7, failing <ids>). The Frontier row is corrected to the live substrate and keeps the residual; no Core move. Class: round-46 M9 (a rebuild makes freshness red until the extraction is re-derived); no claim closure.
- No Git add, commit or ref operation.
```

## 6. Must-observe fill table (do not copy values)

| field | how to observe | my prototype (scratch, not landing) | may the draft be applied? |
|---|---|---|---|
| `<CHECKLIST_EXIT>`, `<CHECKLIST_PASS>/<CHECKLIST_TOTAL>` | `python3 -B verifiers/verify_skill_checklist.py --json` after the new check lands | pre-check edit: exit 1, 9/10, only `LOG.md:2111` | Only if the new check PASSes and the total is the landed count (11 with C3; 10 + the C3 red otherwise) |
| `<PINS_EXIT>`, `<PINS_PASS>` | `python3 -B verifiers/check_substrate_pins.py --json` with default paths | **exit 0, 3/3** after pointing the opencode default at the npx ELF and re-pinning values | Yes, if the landing run reproduces 0/3 |
| `<SURFACES_EXIT>`, `<SURFACES_PASS>` | `python3 -B verifiers/verify_surfaces.py --json` with default paths | **exit 1, 4/7** after the pin fix; `literal_present` (8 omp literals unverifiable), `no_uncovered_class` (vacuity 0/8), `opencode_extract` still fail | **No** until the extraction re-derivation lands; the plan's 7/7 is a target, not a result. If the re-derivation lands 4/3, C1 is `improved-bounded`, not improved: keep the row, name the three failing classes and their per-class sweep (Q09/Q14), and record no move. |
| description chars | `verify_skill_checklist.py --json`, `trigger.frontmatter_parses` detail | 814 → 820 | Yes |
| `<skills>` count | `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` | 1 → 0 | Yes |
| new self-test floor | run `--self-test`, count assertions; bump registry + both tables + docstring | not implemented here; current registry 1597 | Only after the observed count |
| check id | the landed `CHECK_IDS` entry | proposed `trigger.description_no_xml_tag` | Only the landed id |

## 7. Second-order effects / landing checklist

1. **`CHECK_IDS` ripples through every self-test fixture.** The self-test derives expected
   PASSes as `passes = [c for c in CHECK_IDS if c not in fails and c not in nas]`
   (`verifiers/verify_skill_checklist.py:1839`). Adding an 11th id makes every existing
   `CASES` entry expect a PASS for it. Malformed-frontmatter fixtures must list the new id
   under `fails` (a missing description cannot satisfy the tag rule → FAIL, fail-closed).
   Do **not** add it to `NA_ALLOWED` (`:1830`) instead: that set makes N/A acceptable
   globally and would let malformed frontmatter read as N/A — the M13 structural/semantic
   confusion returning through the fixture matrix.
2. **Floor bump in four sites** (the guard's own BUMP-IN-STEP rule): `verifiers/floors-registry.json:5-7`,
   `verifiers/check_assertion_floors.py:121`, `:142`, and the docstring at `:8`. A half-bump
   fails loudly, not silently.
3. **No new checklist box.** The rule is executed at instrument level; adding a box changes
   the 41-box denominator and the "33 of 41" counts repeated in `PROVINCE.md:20`,
   `corpus/README.md` § Known gaps and elsewhere. The instrument-level check keeps the
   coverage map honest.
4. **No new knowledge file is required for this move.** The rule's source is S003
   (`corpus/SOURCES.md:16`); the executable is the checklist. If a knowledge entry is added
   anyway, its index row is a separate C3-path edit.
5. **`verify_harness_claims.py:55` carries the same stale `OC_BIN` default**
   (`~/.opencode/bin/opencode`) as the two verifiers named in C1. C1's path change should
   include it for consistency; that verifier is already red at BASE (21/28) and was not run
   here. Not changing it leaves one instrument resolving a missing path.
6. **Corpus baseline must move twice, not once** (reviewer P10): 58→59 for
   `corpus/lessons/round-46-verifier-spotcheck.md`, then again for the round-47 lesson.
   This belongs to the C3/index path. My Frontier edit is outside the coverage map
   (`verifiers/verify_corpus_integrity.py:33-34` reads only column 2 of coverage-map rows),
   so it does not alter `tracked_files`/`unindexed` — measured unchanged 59/1 before→after.
7. **npx-path fragility:** the opencode default becomes the npx-cache ELF
   (`/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-linux-x64/bin/opencode`).
   A cache prune makes the pin guard exit 2 UNREADABLE (fail-closed, but a red gate for
   an unchanged substrate). Do **not** point the default at `~/.local/bin/opencode`: that is
   a 1460-byte bash wrapper which runs `npx --prefer-online` (a network fetch the contract
   forbids), and `verify_surfaces.py` would `strings` a shell script — a new vacuity.
8. **LOG citation safety:** the appended section cites only `verifiers/…`, `corpus/…`,
   `SKILL.md` (bare, skipped) and `LOG.md:2111` (bare, skipped); it contains no `.ufo` token
   at all. In a lane-faithful scratch layout the checklist's `governance.citation_resolves`
   failure set is unchanged: only the pre-existing `LOG.md:2111`. Reviewer P7 independently
   reproduced the dead class: a backticked `.ufo/reports/round-46/kotoba.md` appended to
   LOG.md creates a second failure because fleet report paths do not live in the lane repo.
   `.ufo/waves/…` resolves today (the directory exists in the lane) but is untracked and
   prunable, so it is not used here either; a host-absolute path is the safe form if a
   report must be cited (r46 lesson's convention).

### 7.9 Merged-LOG invariant (the gate reads the union, not my section)

`governance.citation_resolves` collects subjects across the whole `LOG.md`/`SCORECARD.md`
(gate prose `verifiers/verify_skill_checklist.py:179-180`; roots `:347`; scan `:1454-1500`),
so the property below must be checked on the **merged** lane LOG after every r47 seat's
append, not on this section alone:

- **Invariant:** the unquoted, non-schematic repo-rooted backtick subjects in the merged
  `LOG.md` have exactly one dead token, `LOG.md:2111` (the recorded absence C3 pins).
- **Command:** `python3 -B verifiers/verify_skill_checklist.py --repo . --skill ./SKILL.md --json`,
  then read `governance.citation_resolves` (FAIL expected at BASE; the detail must name only
  `LOG.md:2111`). This also catches a sibling seat's `.ufo/waves/…` or `.ufo/reports/…`
  append, which the per-section check cannot see.
- **Control arm (executed):** appending `- control: \`.ufo/reports/round-46/kotoba.md\`` to the
  merged scratch LOG produced a second failure at the appended line
  (`LOG.md:2325: '.ufo/reports/round-46/kotoba.md' does not resolve`); restoring the file
  returned the set to exactly `{LOG.md:2111}`. The check is not vacuous under a registry that
  pins one absence.
- **C3 coupling:** if any new dead subject is merged before C3 lands, C3's before-value moves
  and its planned `10/10` after-value is measured against a different set. Run this check
  immediately before C3's re-measurement. A registry key must carry **file + line + token**
  as measured at the pinning commit, with the token's recorded absence attached — not a bare
  line number (append-only LOG shifts lines) and not a bare path (it stops being an absence
  the moment the path exists again). A different dead citation must still FAIL (the control
  above is that arm).

## 8. Counterexamples and risks

- **C-1 (full C1 move).** A Core bullet carrying `omp 18.12.5` is false the next time omp is
  rebuilt; the measured interval here is short (18.12.3 at round 46 → 18.12.5 two days
  later) and the rebuild already deleted the extractor's omp call shapes (0/8). A status in
  Core would also displace the only frontier item that names the manual re-derivation.
- **C-2 (early C2 move).** Writing the Core bullet before the check exists makes PROVINCE
  assert an instrument that is not there; the bullet is not validated by any gate, so the
  falsehood would be silent. Gate on the check PASS and the live-file tag count 0.
- **C-3 (`NA_ALLOWED` shortcut).** Adding the new id to the global N/A set instead of
  per-case `fails` would convert the no-frontmatter fixtures from FAIL to N/A and hollow
  out the fail-closed property. The per-case route is the discriminating one.
- **C-4 (adding a checklist box).** Cascades into the 41-box denominator and three
  documents' counts; unnecessary for an instrument-level rule.
- **C-5 (pure line-level append).** Leaves the old row's present-tense "unchecked" and
  "18.12.3" claims in a live doc. Content-preserving append + LOG is the calibrated form;
  the old text survives either way.
- **C-6 (pinning the wrapper).** See §7.7 — a shell script has no loader strings; the
  surfaces check would fail for the wrong reason and the pin would not describe the
  substrate.
- **Risk — predicate boundary.** The proposed tag regex `</?[A-Za-z][A-Za-z0-9._:-]*(\s[^<>]*)?/?>`
  fails a description containing an unspaced comparison such as `a<b and c>d`. That is a
  fail-closed direction and should be named in the check's detail line; the body-only
  control pins the scope (description value, not the whole file).
- **Risk — trigger surface.** The reworded final sentence removes the literal `<skills>`
  term from the description (it remains in body prose). The description's trigger strings
  are unchanged; the lane's skill is not in an omp discovery root (`SKILL.md:12-14`), so no
  omp cache key is created. Opencode-side render/activation was not measured [INFERENCE].

## 9. Verification performed

All in `/tmp`; the lane repo was only read. Canonical-layout scratch:
`/tmp/kotoba-r47-final/kotoba-shokunin` (clone at BASE, parent symlinks to the fleet `.ufo`,
`.md` files and `kasegi-shokunin`).

| command | exit | key output |
|---|---:|---|
| `python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` (BASE, canonical layout) | 1 | 9 PASS / 1 FAIL, only `governance.citation_resolves` at `LOG.md:2111` |
| same after the C2 description + line-151 edits | 1 | identical set; `trigger.frontmatter_parses` detail `description 814 → 820 chars` |
| `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` | 0 (grep count 0) | 1 → 0 |
| tag probe (scratch Python, saved JSON) | — | base description FAIL `<skills>`; after PASS; `<skills>`, `</available_skills>`, `<tool name="x">`, `<br/>` FAIL; math and body-only controls PASS |
| pins prototype: patch both default paths to the npx ELF + update `measured_against` to omp 18.12.5 / opencode 1.19.3 | 0 | `pass: 3, fail: 0`; omp mtime `delta_ns 0`; opencode sha `179ca421…` |
| `verify_surfaces.py --json` after the same pin fix | 1 | 4 PASS / 3 FAIL; `literal_present` (8 omp literals), `no_uncovered_class` (vacuity 0/8), `opencode_extract` |
| `verify_corpus_integrity.py --json` after the README frontier edit | 1 | `tracked_files 59`, `unindexed 1`, `stale 0`, `missing 0`, `report_dead 0`, `commit_nonhash 0` — unchanged from BASE |
| `verify_corpus_independent.py --json` after the README frontier edit | 1 | `unindexed 1`, `stale 0`, `report_dead 0`, `commit_nonhash 0` — unchanged |
| `git apply --check ConnProvinceFrontier.patch` in a fresh BASE clone | 0 | applies cleanly |

Artifacts: `.ufo/waves/round-47/build/ConnProvinceFrontier.patch` (3 files, 11 insertions /
2 deletions: PROVINCE, corpus README, LOG; the old frontier text is retained as a prefix),
`.ufo/waves/round-47/build/ConnProvinceFrontier.desc-tag-probe.json`,
`.ufo/waves/round-47/build/ConnProvinceFrontier.probe-results.json`.

## 10. What I did NOT check

- I did not implement the C2 check, its fixtures, or its floor bump; the `CHECK_IDS` /
  `passes` / `NA_ALLOWED` ripple is read from source (`verifiers/verify_skill_checklist.py:282-294,1830,1839`),
  not executed. The post-C2 aggregate checklist count is therefore unobserved.
- I did not re-derive the 18.12.5 extraction rules. `verify_surfaces.py` 7/7 is the plan's
  target; my best measured state after the pin fix is 4/7. The C1 `7/7` in the LOG draft
  must not be written until observed.
- I did not run the C3 erratum registry or the corpus index row; `0 DRIFT` and `11/11`
  are unverified. The reviewer's double-baseline move (58→59→60) is recorded as C3-path,
  not measured here.
- I did not run `verify_harness_claims.py` after the `OC_BIN` path question, the floors
  guard, or the lane-wide battery in the lane repo (contract restricted my runs to the
  named read-only verifiers, and I kept them in scratch).
- I did not test npx cache eviction, the wrapper's network behavior, or opencode's
  render/activation after the description change.
- I did not verify that the integrator will use `trigger.description_no_xml_tag` as the
  check id; the drafts assume it and must be regenerated if the landed id differs.
- I did not render the edited Markdown (a long appended table cell) or check line-length
  conventions; the README row was already a single long line.
- All line numbers are at BASE; the lane worktree may have moved after my last read.
