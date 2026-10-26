# ReviewerDescFeasibility — Round 73 Wave 1 Report (Attack on Replacement C2)

## Verdict

**REDESIGN BEFORE FREEZE 2 AND RE-CLASSIFY AS EXPLORATORY (OR RE-AXIS TO `calibration` / `consistency` AND DROP AS A `depth` CLAIM); DO NOT FREEZE AS A MEASURED `depth` CLAIM UNDER THE CURRENT ADDENDUM-1 TEXT.**

1. **Technical feasibility in a fleet-shaped sandbox of `072048fa8e8a52c707d25f7079772fa317244eb7` — FEASIBLE (zero new reds):** Applying a trial description rewrite (first sentence 91 characters before `. ` / 92 characters with `.`, containing whole words `skill` and `prompt` and quoted trigger `"SKILL.md"`; folded length `1005 <= 1024`; frontmatter preserved at 19 lines so `git diff --numstat` is `2 2 SKILL.md`, net `0` lines) causes **zero new gate failures**:
   - `verify_skill_checklist.py`: **exit 0** (2.29 s; all 11 checks PASS, 45 boxes, 1005 chars, 568 lines).
   - `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md`: **exit 0** (0.19 s; `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 9 of 9 non-none lanes`, `skill description length 1005 of 1024`).
   - `check_province_core.py --rev <sandbox rev>`: **exit 0** (0.08 s; `province core rows 2 of 2`).
   - `check_assertion_floors.py` (run alone): **exit 0** (83.48 s; all 15 instruments >= floor).
   - `verify_corpus_integrity.py`: **exit 1** (0.37 s; first red line: `unindexed: corpus/lessons/round-72-verifier-spotcheck.md`, summary `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_unresolvable`) — **byte-identical to unmodified base `072048f`** (`verify_corpus_integrity.py:75`: *"SKILL.md is outside corpus/ and is never scanned"*).
2. **Axis honesty (`depth` vs. cosmetics) — FAILS AS A MEASURED `depth` CLAIM:** By `/home/vgpnk/Projects/shokunin/AXES.md:11`, `depth` is *"Verifiable technical detail — decision tables with real thresholds, named error signatures, cited sources | A reader can act on SKILL.md alone; no filler"*, and by `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotoba-round-73.md:435-437` (§9 Claim sizing), *"Name the axis by the surface the round changes, not by the number it produces (kaidoku r29). Re-scoring a rule the lane already holds on new inputs, or counting rows a sourceless fixture also counts, is quality work, never coverage or depth."* Rewriting `SKILL.md`'s own 15-line folded `description` adds zero decision tables, zero thresholds, zero error signatures, and zero cited sources, and `SKILL.md:16-18` + `corpus/knowledge/frontmatter-trigger-surface.md:150-155` explicitly state that `*-shokunin` files sit outside the `omp` discovery roots so `description` craft on this file is *"audit-hygiene, not routing surface"*. Furthermore, the addendum's own shortcut control #6 (`plans/round-73-addendum-1.md:56-58`) delegates hollowness detection of a mid-phrase period to *"the non-author reviewer for hollowness"*, which is the procedural definition of an **exploratory** claim (`AXES.md:46-55`), not a self-contained counter measurement (`QUALITY.md` Q25/Q26).
3. **Rule source & predicate fidelity — 6 MUST-FIX DEFECTS BEFORE FREEZE 2:** While `corpus/knowledge/frontmatter-trigger-surface.md:68` and `:116-120` contain the words the addendum quotes, the addendum's R1/R2 predicate (`plans/round-73-addendum-1.md:39-42`) **diverges from the actual `omp` `H7s` truncator** (`verifiers/verify_harness_claims.py:242-247`; `render-mechanism-round7.md:17-19`) in four ways that either pass broken shortcut worlds (violating the kill rule) or mismeasure the actual `H7s` render.

---

## Task (1): Trial Description Rewrite in a Fleet-Shaped Sandbox of `072048fa8e8a52c707d25f7079772fa317244eb7`

### 1.1 Sandbox Construction and Trial Rewrite

Built a fleet-shaped sandbox at `/tmp/k73fleet-ReviewerDescFeasibility.60p5ayoz` (all `/home/vgpnk/Projects/shokunin` entries except `kotoba-shokunin` symlinked into the parent; `git clone --shared -q --no-checkout` of `/home/vgpnk/Projects/shokunin/kotoba-shokunin` into `/tmp/k73fleet-ReviewerDescFeasibility.60p5ayoz/kotoba-shokunin`; checked out `072048fa8e8a52c707d25f7079772fa317244eb7`; verified `git -C "$D" rev-parse --show-toplevel` equaled the sandbox clone before committing; deleted the sandbox directory before returning).

**Base frontmatter line-count check (`SKILL.md:1-19`):**
```text
 1: ---
 2: name: kotoba-shokunin
 3: description: >
 4:   Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md /
 5:   dispatch prompts / system prompts for trigger fidelity and decision density.
...
18:   never reaches the omp router — craft here is audit-side.
19: ---
```
*Note (Must-Fix MF-5):* The frontmatter block is **19 lines** (lines `1..19`: opening `---` on line 1, `name:` on line 2, `description: >` on line 3, 15 folded body lines on lines `4..18`, closing `---` on line 19), not 18 lines as written in the wave-1 seat prompts (`w1-spec.json:286,305,314,323`). Replacing lines 4–5 in place with two lines keeps the frontmatter at 19 lines (`git diff --numstat` = `2 2 SKILL.md`, net `0`).

**Trial rewrite applied to `SKILL.md:4-5` (lines 6–568 untouched):**
```yaml
  Prompt & skill craft — audits, writes, and rewrites "SKILL.md", AGENTS.md,
  and prompt files. Tunes trigger fidelity and decision density.
```
- **Folded `D` length:** `1005` characters (`<= 1024`).
- **First sentence (before `. `):** `'Prompt & skill craft — audits, writes, and rewrites "SKILL.md", AGENTS.md, and prompt files'` -> **91 characters** (`92` including `.`, in `[40, 99]`).
- **First 99 characters of `D`:** `'Prompt & skill craft — audits, writes, and rewrites "SKILL.md", AGENTS.md, and prompt files. Tunes '` -> contains whole words `skill` (and `Prompt`), whole word `prompt` (lowercase at offset 79), and double-quoted `"SKILL.md"` (member of `Triggers:`).
- **Actual `omp` `H7s` (`previewSkillDescription`) output on trial `D`:** `'Prompt & skill craft — audits, writes, and rewrites "SKILL.md", AGENTS.md, and prompt files.'` (92 chars, no ellipsis; note `"SKILL.md"` is at offset 53 >= 40 and followed by `,`, so `H7s` does not prematurely split on `.md`).
- **Sandbox commit:** `f077be86ab328f66e8c988c0af3f2a44412be26e` (`git diff --numstat`: `2 2 SKILL.md`).

### 1.2 Gate Runs on Sandbox Revision `f077be86ab328f66e8c988c0af3f2a44412be26e`

| # | Command (run from `$P/kotoba-shokunin`) | Exit | Wall | Observed Output / First Red Line |
|---|---|---|---|---|
| 1 | `python3 -B verifiers/verify_skill_checklist.py` | **0** | 2.29 s | **0 reds.** All 11 checks PASS (`checklist.box_map_complete` 45 boxes; `trigger.frontmatter_parses` 1005 chars; `trigger.name_directory`; `trigger.literal_trigger_string`; `trigger.anti_trigger_clause`; `trigger.no_xml_tag`; `trigger.line_budget` 568/600; `trigger.no_placeholder` 506 lines; `trigger.command_binary_resolves` 29 subjects; `trigger.citation_resolves` 187 tokens; `governance.citation_resolves` 1280 tokens). |
| 2 | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md --skill SKILL.md` | **0** | 0.19 s | **0 reds.** `rows 20 verified 20` / `province rows 20 matched 20` / `skill description names 9 of 9 non-none lanes` / `skill description length 1005 of 1024`. |
| 3 | `python3 -B verifiers/check_province_core.py --rev f077be86ab328f66e8c988c0af3f2a44412be26e` | **0** | 0.08 s | **0 reds.** `measured-rev: f077be86ab328f66e8c988c0af3f2a44412be26e` / `province core rows 2 of 2`. |
| 4 | `python3 -B verifiers/check_assertion_floors.py` *(run alone)* | **0** | 83.48 s | **0 reds.** All 15 floored self-tests PASS (`harness` 10/10, `corpus_integrity` 164/164, `corpus_independent` 105/105, `surfaces` 218/218, `checklist` 1863/1863, `pins` 62/62, `harness_independent` 123/123, `compare_harness_independent` 330/330, `floors_guard` 165/150, `dispatch_prompts` 56/56, `sibling_census` 68/68, `overlap_levers` 55/51, `alwayson` 89/89, `correction_sweep` 25/25, `scoped_rules_v32` 240/240). |
| 5 | `python3 -B verifiers/verify_corpus_integrity.py` | **1** | 0.37 s | **Pre-existing base reds only (byte-identical to `072048f`; `SKILL.md` is not scanned):**<br>- First detail red: `unindexed: corpus/lessons/round-72-verifier-spotcheck.md`<br>- First `DRIFT` line: `DRIFT   corpus.index.tracked_files: observed=136 expected=135`<br>- Other `DRIFT` lines: `corpus.index.unindexed: observed=1 expected=0 / empty`; `corpus.pointers.report_total: observed=95 expected=93`; `corpus.pointers.commit_unresolvable: observed=3 expected=0 / empty` *(note: in a sandbox clone, `commit_resolves` falls back to `FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` where those 3 commits are not objects)*<br>- Summary line: `5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_unresolvable`. |

**Exact stdout of `verify_skill_checklist.py` on `f077be86ab328f66e8c988c0af3f2a44412be26e`:**
```text
PASS checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted); delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2; delegated verifiers/verify_alwayson.py: --box-proof exit 0: boxes proven 2
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='kotoba-shokunin', description 1005 chars
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string: evaluated 1 — description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause: evaluated 1 — exclusion marker 'Anti-triggers' present (vocabulary test, not semantics: a vacuous 'Never use this skill.' passes and an unlisted real exclusion fails)
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (S019 Anthropic rule, absent from the open spec (S018), approximated lexically on the unparsed text; Anthropic's packager (S012) bans any '<'/'>' in the parsed value, and the two disagree in both directions (corpus/knowledge/frontmatter-rule-authorities-round48.md))
PASS trigger.line_budget: evaluated 568 — 568 lines within budget 600 (from box at line 267)
PASS trigger.no_placeholder: evaluated 506 — no placeholder markers in 506 scanned lines
PASS trigger.command_binary_resolves: evaluated 29 — 16 segments; 29 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 187 — 187 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves: evaluated 1280 — 1280 governance citation token(s) resolve across 2 files; 10 quoted meta-finding(s), 3 schematic token(s) excluded, 2 recorded absence(s) excused, 4 recorded correction(s) excused
```

**Exact stdout of `verify_corpus_integrity.py` on `f077be86ab328f66e8c988c0af3f2a44412be26e` (verified `p_base.stdout == p_trial.stdout -> True`):**
```text
corpus.index    tracked=136 unindexed=1 stale=0 missing=0  (153 FILE-column patterns over 135 md files)
corpus.pointers report_dead=0/95 commit_total=41 unresolvable=3 nonhash=0 (shapes [relative=1, absolute=44, tilde=1, bare=49], quoted-excluded=6, pointer-excluded=8; sites in --json)
           unindexed: corpus/lessons/round-72-verifier-spotcheck.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:100: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:142: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:148: <repo>/.ufo/reports/round-11/kotoba.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:280: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/cold-run-round11.md:66: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/corpus-integrity-round11.md:116: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/corpus-integrity-round11.md:218: .ufo/reports/round-1/<lane>.md
           report_pointers_excluded: corpus/knowledge/dispatch-prompt-audit-round7.md:42: .ufo/reports/round-1/<lane>.md
           report_pointers_quoted: corpus/README.md:68: .ufo/reports/round-48/kotoba.md
           report_pointers_quoted: corpus/lessons/round-57.md:86: /home/vgpnk/Projects/shokunin/.ufo/reports/round-56/kotoba.md
           commit_unresolvable: corpus/lessons/round-62-verifier-spotcheck.md:13: def4b9fffbf59e9e121b89ef73fbeb89426bd614
           commit_unresolvable: corpus/lessons/round-65-verifier-spotcheck.md:11: 7b370d54bd0e74eef4aa90b2e8b2fc9736b3d39f
           commit_unresolvable: corpus/lessons/round-66-verifier-spotcheck.md:11: 1154d57a9ebb17faa4c9f8f456a6e53c51c230ae
           commit_truncated: corpus/lessons/round-71-verifier-spotcheck.md:120: fb6a28ee…
           commit_truncated: corpus/lessons/round-71-verifier-spotcheck.md:90: 955ffd5d…
           commit_quoted: corpus/knowledge/claim-census-round12.md:95: 4dd7753 (quoted meta-finding)
           commit_quoted: corpus/lessons/round-53.md:44: cfb894a5 (quoted meta-finding)
           commit_quoted: corpus/lessons/round-53.md:45: <hex> (quoted meta-finding)
           commit_quoted: corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff (quoted meta-finding)
           commit_quoted: corpus/lessons/round-54.md:13: cfb894a5 (quoted meta-finding)
           commit_quoted: corpus/lessons/round-6-aggregator-audit.md:45: round-N (quoted meta-finding)
DRIFT   corpus.index.tracked_files: observed=136 expected=135
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=95 expected=93
DRIFT   corpus.pointers.commit_unresolvable: observed=3 expected=0 / empty
5/9 checks pass; DRIFT: corpus.index.tracked_files, corpus.index.unindexed, corpus.pointers.report_total, corpus.pointers.commit_unresolvable
```

---

## Task (2): Is the Claim `depth` (`AXES.md`: a reader can act on `SKILL.md` alone; no filler) or Cosmetics?

### 2.1 Argument FOR `depth` (from `frontmatter-trigger-surface.md` and `skill-listing-thresholds-round54.md`)

1. **`omp`'s 99-char truncator is the tightest cut across all surveyed harnesses (`skill-listing-thresholds-round54.md:32-34`):**
   - `sed -n '32,34p' corpus/knowledge/skill-listing-thresholds-round54.md`:
     ```text
     4. omp (not one of the seven) cuts at offset 99 unless a cached one-liner exists; opencode renders the full
        description (`../../SKILL.md` § Router model; `render-mechanism-round7.md`). So the tightest documented
        or measured cut on this host's two harnesses is omp's 99 characters, far below any documented maximum.
     ```
   - `skill-listing-thresholds-round54.md:20-27` also documents that Codex shortens descriptions first when the initial list exceeds its budget (`2%` of context window or `8,000` characters, S054) and Claude Code truncates at `1,536` characters and drops descriptions past `1%` of context window (S053), so `SKILL.md:166` advises: *"Front-load the use case and trigger words in `description` so matching survives shortening; do not rely on a long tail."*
2. **`SKILL.md`'s own `description` is the first example a reader sees (`frontmatter-trigger-surface.md:116-136`):**
   - `frontmatter-trigger-surface.md:116-120` states Rule 8 (*"On omp the 99-char cliff is absolute — write for the truncator, not the compressor … Put the capability clause + the most match-critical WHEN material in the first <=99 chars"*), and `:131-136` states Rule 9 (*"Exploit the omp first-sentence branch. If the first `.`/`!`/`?` sentence is >=40 chars it renders whole with NO ellipsis … Put trigger material inside sentence 1 or accept the loss"*).
   - At base `072048f`, `SKILL.md`'s own first sentence is 150 chars (151 with `.`), so under `H7s` it falls into the last-space ellipsis branch (`Prompt & skill craft — audits, writes, and rewrites SKILL.md / AGENTS.md / dispatch prompts /…`, 94 chars, `render-mechanism-round7.md:22-23`, `sibling-description-rewrites-round8.md:51`) and loses every quoted trigger string.
   - A reader using `SKILL.md` as a reference template for writing their own skill (`AXES.md:11`: *"A reader can act on SKILL.md alone"*) currently sees a frontmatter `description` that violates the skill's own Rule 8 and Rule 9 (`considerthese/2026-10-25.md:23` item 5). Making the exemplar obey the rule removes an exemplar-vs-rule contradiction.

### 2.2 Argument AGAINST `depth` — Why This Is Audit-Hygiene / Calibration / Exploratory Craft, NOT Measured `depth`

1. **`frontmatter-trigger-surface.md:150-155` (Rule 12) and `SKILL.md:16-18` explicitly classify `*-shokunin` description edits as "audit-hygiene", not routing:**
   - `sed -n '150,155p' corpus/knowledge/frontmatter-trigger-surface.md`:
     ```text
     12. **Skill files outside a discovery root never route.** omp loads
         `.agent/skills` + `.agents/skills` (project walk-up + user home),
         `.claude/skills`, marketplace cache. A SKILL.md at a bare repo root (the
         six `*-shokunin` files) is never offered — for those, `description` craft
         is audit-hygiene, not routing surface; check the discovery root before
         predicting router behavior.
     ```
   - `SKILL.md:16-18`: *"Note: shokunin files sit outside the omp skill discovery roots, so this text never reaches the omp router — craft here is audit-side."*
   - Even if `SKILL.md` were offered on `opencode`, `skill-listing-thresholds-round54.md:18-19,32,46` proves that `opencode` has no 99-char cliff and renders the full `description` byte-for-byte.
2. **It fails the `AXES.md:11` definition of `depth` and the prompt §9 axis-naming rule (`kotoba-round-73.md:435-437`):**
   - `AXES.md:11` defines `depth` as: *"Verifiable technical detail — decision tables with real thresholds, named error signatures, cited sources | A reader can act on SKILL.md alone; no filler."*
   - Rewording lines 4–5 of `SKILL.md`'s frontmatter adds **zero** decision tables, **zero** thresholds, **zero** error signatures, and **zero** cited sources. Worse, to squeeze a quoted trigger and a period into the first 99 characters while keeping `len(D) <= 1024`, a rewrite must **drop or compress** existing domain words from sentence 1 (e.g., `ScribeDescription.md:177-180` notes its picked candidate B moves `SKILL.md, AGENTS.md, dispatch and system prompts` out of sentence 1 into sentence 2 — where `omp`'s truncator discards it! — and drops `trigger fidelity` from sentence 2).
   - `.ufo/prompts/kotoba-round-73.md:435-437`: *"Name the axis by the surface the round changes, not by the number it produces (kaidoku r29). Re-scoring a rule the lane already holds on new inputs, or counting rows a sourceless fixture also counts, is quality work, never coverage or depth."* Applying a round-7/round-15 rule (`frontmatter-trigger-surface.md:68,116-120`) to `SKILL.md`'s own frontmatter is **re-scoring a rule the lane already holds on an existing file** (`calibration` / `consistency`: self-audit of `SKILL.md` against its own rule), not `depth`. (And in round 73, `consistency` is already claimed by C3, so two claims on `consistency` would count as one claim under `AXES.md:32-33`.)
   - Precedent in this lane: in round 50, when C1 edited `SKILL.md`'s own `description` to name the 9 adjacent siblings, the non-author spot-check (`corpus/lessons/round-50-verifier-spotcheck.md:105-108`) explicitly ruled: *"The description says it never reaches the omp router (`SKILL.md:16-17`). The claim moves wording only. Because the guard checks wording only, the learning-claim label rests on separate evidence: the new entry `corpus/knowledge/skill-selection-rules-round50.md`, the `SKILL.md` § Anti-patterns error pattern (`SKILL.md:373-379`) and the 'sibling-description check' capability row."* Replacement C2 has **no** new knowledge entry, **no** new `SKILL.md` body rule/table, and **no** new SOURCES row.
3. **The addendum's own shortcut control #6 admits the counter cannot distinguish craft from a 1-byte punctuation hack (`plans/round-73-addendum-1.md:56-58`):**
   - `sed -n '56,58p' plans/round-73-addendum-1.md`:
     ```text
     description over 1,024 characters; the first sentence made short by inserting a period mid-phrase while the old
     151-character sentence continues after it (R1 reads the new first sentence only — judged by the non-author
     reviewer for hollowness; the counter prints the first sentence). **Kill rule:** any shortcut world scoring 3 means
     ```
   - This is an explicit self-contradiction in `plans/round-73-addendum-1.md:56-58`: the next sentence says *"Kill rule: any shortcut world scoring 3 means the counter is wrong; fixed before data"*, yet the mid-phrase period world **is listed among the "Shortcut controls (committed worlds, each must read below 3)"** while parenthetically admitting that the counter scores it `3 of 3` (`R1 reads the new first sentence only — judged by the non-author reviewer for hollowness`)!
   - Under `AXES.md:43-55`, a claim whose quality/non-hollowness cannot be decided by its counting command and requires a named non-author reviewer's judgment is, by definition, **exploratory** (`unprovable-but-better`).

### 2.3 Which Sentence(s) of `plans/round-73-addendum-1.md` Must Change So a Non-Author Reviewer Can Honestly Judge

1. **`plans/round-73-addendum-1.md:26-28`** currently reads:
   > `The description's own Note: says the file sits outside the omp discovery roots, so this is audit-side craft, not router behaviour — the claim is that the lane practises the rule it teaches, and it says nothing about any router.`
   - **Why it misleads / is insufficient:** Calling a self-consistency wording edit on an unrouted frontmatter field a measured `depth` claim contradicts `AXES.md:11` (which requires verifiable technical detail so a reader can act on `SKILL.md` alone) and `kotoba-round-73.md:435-437` (re-scoring a held rule on a file is quality/calibration work, not `depth`), while hiding the trade-off that shortening sentence 1 to `<= 99` chars evicts the four-surface capability list (`SKILL.md / AGENTS.md / dispatch prompts / system prompts`) into sentence 2 where `omp`'s truncator discards it (`frontmatter-trigger-surface.md:134`).
   - **Required replacement for `plans/round-73-addendum-1.md:26-28`:**
     > `Because SKILL.md sits outside the omp discovery roots (frontmatter-trigger-surface.md:150-155, rule 12) and opencode renders the full description without a 99-char cut (skill-listing-thresholds-round54.md:32-34,46), this edit is audit-hygiene exemplar alignment, not router behaviour and not new technical detail; C2 is therefore declared EXPLORATORY on depth (AXES.md:43-55; check_own_description.py is supporting form evidence only), and the non-author reviewer judges whether the rewritten first sentence is a net improvement in exemplar clarity despite moving part of the base capability clause past sentence 1.`
2. **`plans/round-73-addendum-1.md:53-58`** currently reads:
   > `**Shortcut controls (committed worlds, each must read below 3):** … the first sentence made short by inserting a period mid-phrase while the old 151-character sentence continues after it (R1 reads the new first sentence only — judged by the non-author reviewer for hollowness; the counter prints the first sentence). **Kill rule:** any shortcut world scoring 3 means the counter is wrong; fixed before data; nothing changes after a seat has scored data (Q28).`
   - **Why it must change:** Listing a world under *"Shortcut controls (committed worlds, each must read below 3)"* followed by *"Kill rule: any shortcut world scoring 3 means the counter is wrong"*, while that world **scores 3 of 3** on the counter and relies on reviewer judgment, breaks the kill rule on arrival.
   - **Required replacement for `plans/round-73-addendum-1.md:56-58`:** Move the mid-phrase period world (and the quote-list-only / domain-evicted worlds) out of the machine-killed shortcut list into an explicit **Counter-bound / non-author reviewer judgment** paragraph (matching `round-60-verifier-spotcheck.md:68-73` and `round-72-verifier-spotcheck.md:62`).

---

## Task (3): Rule Source Verification (`corpus/knowledge/frontmatter-trigger-surface.md` Lines 68 and 116–120)

### 3.1 Exact Printed Lines (`sed -n '68p;116,120p' corpus/knowledge/frontmatter-trigger-surface.md`)

**Command:**
```sh
sed -n '68p;116,120p' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/knowledge/frontmatter-trigger-surface.md
```

**Observed output (with surrounding lines 67–69 and 116–121 from `nl -ba`):**
```text
    67	the render is that LLM one-liner (≤160 chars, ≤12 words); otherwise a
    68	deterministic truncator keeps at most 99 chars — first sentence wins if ≥40
    69	chars, else last-space cut + `…`. Measured over the live 17-skill omp
   116	8. **On omp the 99-char cliff is absolute — write for the truncator, not the
   117	   compressor.** Anything past ws-collapsed offset 99 is invisible whenever the
   118	   cache misses: 0 chars survive in all 14 measured truncations; effective keep
   119	   is 55–96 (last-space back-off). Put the capability clause + the most
   120	   match-critical WHEN material in the first ≤99 chars; everything later is
   121	   only reachable if the async LLM cache has landed *for this session's
```

### 3.2 Comparison Against `plans/round-73-addendum-1.md:21-23` and `:39-42`

1. **Do lines 68 and 116–120 say what `plans/round-73-addendum-1.md:21-23` quotes?**
   - **Yes on the words quoted (quote-equal after documented shaping):**
     - `plans/round-73-addendum-1.md:21-22` quotes `corpus/knowledge/frontmatter-trigger-surface.md:116-120` as `"write for the truncator … match-critical WHEN material in the first ≤99 chars"`. In lines 116–120, `write for the truncator` sits on line 116 and `match-critical WHEN material in the first ≤99 chars` sits on line 120 (with 35 words on lines 116–119 replaced by `…` and `**` stripped).
     - `plans/round-73-addendum-1.md:22-23` paraphrases `:68` (plus the first word `chars` of `:69`) as `(the deterministic truncator keeps at most 99 characters, the first sentence wins if ≥ 40)`. Line 68–69 literally reads `deterministic truncator keeps at most 99 chars — first sentence wins if ≥40 / chars, else last-space cut + …`.
2. **Does the addendum's R1/R2 predicate (`plans/round-73-addendum-1.md:39-42`) match the mechanism in `frontmatter-trigger-surface.md:68,116-120,131-136` and `render-mechanism-round7.md:17-19`? NO — 4 concrete mismatches:**
   - **Mismatch 3A (R1 fallback lets a period-less run-on sentence pass R1 with length 99):**
     - `plans/round-73-addendum-1.md:39-40` defines R1's first sentence as *"the text before the first `. ` or `: ` followed by an uppercase letter, else the first 99 characters"* and requires it to be *"between 40 and 99 characters long"*.
     - If `D` has **no** `. ` or `: ` followed by an uppercase letter (e.g., clauses joined by `;` or periods followed by lowercase words), the `else` branch returns `D[:99]`, whose length is `99`, which satisfies `40 <= 99 <= 99`! Under the real `omp` truncator (`frontmatter-trigger-surface.md:68-69`), a string with no sentence end in `D[:99]` falls into the **last-space cut + `…` branch**, NOT the first-sentence branch. Both `ScribeDescription` (F2) and `CriticC2Counter` (`W6_FALLBACK_VACUOUS`) independently confirmed this hole: a run-on description with no uppercase sentence boundary scores `3 of 3`.
   - **Mismatch 3B (R1 delimiter `[.:] (?=[A-Z])` disagrees with `omp` `H7s`'s `^.*?[.!?](?=\s|$)` inside `D[:99]`):**
     - Actual `H7s` (`verifiers/verify_harness_claims.py:242-245`; `render-mechanism-round7.md:17-18`; `frontmatter-trigger-surface.md:129,131`):
       ```python
       s = t[:99]
       m = re.match(r"^.*?[.!?](?=\s|$)", s)
       if m and len(m.group(0)) >= 40:
           return m.group(0)
       ```
     - First, `H7s` does **not** split on `: ` (`frontmatter-trigger-surface.md:129`: *"the sentence regex knows only `[.!?]`"*). Treating `: ` + uppercase as a sentence end in R1 is fabricated and absent from `frontmatter-trigger-surface.md:68,129,131`.
     - Second, `H7s` matches `.`, `!`, or `?` followed by **any whitespace** (not only whitespace + uppercase), and it matches **non-greedily from offset 0**. Thus, if a rewrite puts unquoted `SKILL.md ` (followed by a space) after offset 40, or puts `. chousa` (period + lowercase), `H7s` cuts there while R1's `. (?=[A-Z])` does not!
     - Third, `H7s` includes the sentence-ending punctuation character in `m.group(0)` (`len(m.group(0)) >= 40` inside `t[:99]`, so the text before `.` is `39..98` chars and the sentence with `.` is `40..99` chars). In `plans/round-73-addendum-1.md`, lines 24 and 52 say the base first sentence is **151** characters (which includes the `.`), while line 39 says *"the text before the first `. `"* (which is **150** characters at base, and in `ExecDescCounter/check_own_description.py:153` `description[:match.start()]` prints `150 chars`, contradicting the addendum's `151`).
   - **Mismatch 3C (R2 checks `D[:99]` instead of the first sentence, violating `frontmatter-trigger-surface.md:134-135`):**
     - `frontmatter-trigger-surface.md:131-135` (Rule 9) states: *"If the first `.`/`!`/`?` sentence is ≥40 chars it renders whole with NO ellipsis … **But the same branch discards sentence 2+: godspeed's own trigger list sits in its second sentence and is gone. Put trigger material inside sentence 1 or accept the loss.**"*
     - Yet `plans/round-73-addendum-1.md:41-42` (R2) checks whether **"the first 99 characters of `D`"** contain `skill`, `prompt`, and a quoted trigger — **not** whether **the first sentence** contains them!
     - Consequence: If sentence 1 is 45 characters with no quoted trigger (e.g., `Prompt & skill craft — audits SKILL.md files.`) and sentence 2 starts at offset 46 with `Triggers: "skill file", …`, then R1 passes (sentence 1 is 45 chars), R2 passes (`"skill file"` is at offset 56 inside `D[:99]`), and R3 passes — scoring **`3 of 3`** even though `H7s`'s first-sentence branch **discards sentence 2+ at offset 45**, so the rendered preview contains **zero** quoted triggers!
   - **Mismatch 3D (`frontmatter-trigger-surface.md:119-120` requires "the capability clause + the most match-critical WHEN material", which R1+R2 do not check):**
     - `frontmatter-trigger-surface.md:119-120` says: *"Put the capability clause + the most match-critical WHEN material in the first ≤99 chars"*.
     - R2 only checks for the words `skill` and `prompt` and one quoted trigger string. A first sentence that is just a list of triggers (`"skill file", "prompt craft" are skill prompt triggers.`) or that drops all verbs (`audits`, `writes`, `rewrites`) and artefact names (`SKILL.md`, `AGENTS.md`) passes R1 and R2 while evicting the capability clause past sentence 1.

---

## Summary Must-Fix List (Before Freeze 2) and Verdict on C2

### Must-Fix List

1. **[MF-1 / R1 period-less fallback bug — KILL-RULE VIOLATION]:** Remove `else the first 99 characters` from R1 (`plans/round-73-addendum-1.md:39-40` and `ExecDescCounter/check_own_description.py:148-153`). If no sentence end occurs within the first 99 characters of `D`, R1 must **FAIL** (currently `len(D[:99]) == 99` passes `40 <= len <= 99` on any run-on description with no uppercase sentence boundary).
2. **[MF-2 / R1 `150` vs. `151` off-by-one and `H7s` regex alignment]:** `plans/round-73-addendum-1.md:24,52` states the base first sentence is `151` characters (which includes the trailing `.`), whereas `:39` says *"the text before the first `. ` or `: `"* (`150` characters at base; `ExecDescCounter/check_own_description.py` prints `150 chars`). Also `: ` is not a sentence terminator in `omp`'s `H7s` (`frontmatter-trigger-surface.md:129`: *"the sentence regex knows only `[.!?]`"*). Align R1 with `H7s` (`re.match(r"^.*?[.!?](?=\s|$)", D[:99])` has length in `40..99`, or include the trailing `.` in the first-sentence slice so base is `151` in both the addendum prose and the counter output).
3. **[MF-3 / R2 window bug — checks `D[:99]` instead of the first sentence]:** In `plans/round-73-addendum-1.md:41-42` and `check_own_description.py:192-195`, require the whole words `skill` and `prompt` and the quoted `Triggers:` member to appear **inside the first sentence** (not merely anywhere in `D[:99]`), because under `frontmatter-trigger-surface.md:134-135` (Rule 9) the `>= 40`-char first-sentence branch **discards sentence 2+**, so a trigger at offset 55 after a 45-char first sentence is dropped by `H7s`.
4. **[MF-4 / R2 capability-clause floor]:** To match `frontmatter-trigger-surface.md:119-120` (*"Put the capability clause + the most match-critical WHEN material in the first ≤99 chars"*) and block trigger-list-only / mid-phrase-period shortcuts mechanically, require the first sentence to also carry at least one capability verb (`audit`/`audits`, `write`/`writes`, `rewrite`/`rewrites`) and at least two governed surface names (`SKILL.md`, `AGENTS.md`, `dispatch`, `system`), and require `Triggers:` to hold at least the base count of 8 quoted trigger strings (blocking `W5_TRIGGERS_SHRUNK`).
5. **[MF-5 / Frontmatter line count is 19, not 18]:** Correct any seat/plan reference from `18 lines` to `19 lines` (lines `1..19` of `SKILL.md` at `072048f`), and make the net-zero frontmatter line-diff guard (`inserted == deleted` inside the frontmatter block, `base_lines == rev_lines == 19`) a **counted conjunct** of `check_own_description.py` rather than an uncounted print line (`plans/round-73-addendum-1.md:47-49`), so a rewrite that shifts `SKILL.md:<line>` body citations cannot exit 0.
6. **[MF-6 / Axis & claim-type honesty in `plans/round-73-addendum-1.md:26-28,56-58`]:** Rewrite lines 26–28 and 56–58 as specified in §2.3 above so the addendum does not claim a machine-measured `depth` move on an unrouted file whose hollowness check is explicitly delegated to a non-author reviewer.

### Final Verdict on C2

- **Should C2 stay a measured `depth` claim?** **NO.** Even with MF-1..MF-5 fixed in `check_own_description.py`, editing 2 lines of `SKILL.md`'s own unrouted frontmatter `description` to obey a rule the lane already holds (`frontmatter-trigger-surface.md:68,116-120`) is self-audit hygiene (`calibration`/`consistency`), adds zero new technical detail or decision tables to `SKILL.md` (`AXES.md:11`, `kotoba-round-73.md:435-437`), and relies on non-author reviewer judgment for non-hollowness (`plans/round-73-addendum-1.md:57-58`).
- **Recommended disposition (pick one before Freeze 2):**
  1. **Declare C2 `exploratory` on `depth` before data** (per `AXES.md:43-55`, as round 60 did in Erratum E2), fixing MF-1..MF-6 so `check_own_description.py` (`1 of 3` -> `3 of 3`) serves as honest supporting form evidence while the non-author closure judges whether the rewrite is `unprovable-but-better`; **OR**
  2. **Drop C2 as a separate claim** (fold the description self-audit into round 73 as an unclaimed `considerthese` item-5 hygiene fix or part of C3 `consistency`), leaving the round with two clean measured claims (**C1 `coverage`** and **C3 `consistency`**) per `kotoba-round-73.md:424` (*"Prefer 2 claims. Add a 3rd only if it is independent and cheap to verify."* — note that if C2 is dropped, `depth` is the lowest owned axis at 9 vs `consistency` 10, so **Option 1 (exploratory C2 on `depth`)** satisfies the lowest-owned-axis obligation of `AXES.md:33` while remaining 100% honest).

### Tool Installs / Environment Note
- No tools were installed or upgraded (`pacman` untouched; stdlib `python3` and `git` sufficed).
- All temporary sandbox directories (`/tmp/k73fleet-ReviewerDescFeasibility.60p5ayoz`) were removed before returning; `git status --porcelain` in `/home/vgpnk/Projects/shokunin/kotoba-shokunin` is clean of any tracked modifications.
