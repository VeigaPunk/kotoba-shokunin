verdict: PARTIAL — every numeric before→after claim in the three round-47 axis segments (SCORECARD.md:31/32/33) re-measures EXACTLY at BASE c61a973 and at the landing 7ad7fad, but four statement-level defects survive the attack: a dangling pointer to a nonexistent "LOG.md round-47 landing-pin entry" (:32), a rubric rationale that contradicts the file's own rubric (:32), a "falsification wave and verdict detail in the LOG.md round-47 entries" claim that is false at 7ad7fad (:106), and three wave-1-reviewer mandates that were not honoured (no round-47 Move-log rows, stale `Last change` cells, the unadopted S003 body-length clause unnamed).

# W2ScorecardRows — round-47 SCORECARD segments, falsified

Lane: reviewer (leaf, wave 2, post-crash). Target: `SCORECARD.md` round-47 axis segments + the
`Round 47 completed` / `Next: round 48` paragraphs at landing `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
Scratch clone (canonical layout, detached at 7ad7fad): `/fast/scratch/kotoba-r47/w2/W2ScorecardRows/kotoba-shokunin`.
Production repo read-only; no production file was written except this report. No tools were installed or
upgraded (none needed).

---

## 0. What I attacked, and how

Method: every counting command named in the three segments and in the two paragraphs was re-run **twice** —
once on BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (detached in the scratch clone) and once at the
landing `7ad7fad` — then each prose claim in the segments was re-derived from the artefacts it cites.
Cross-check sources: `corpus/knowledge/instruction-surface-census-round13.md` (§ B′ + round-47 ledger),
`verifiers/*.py`, `verifiers/*.json`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-47.md`,
`corpus/QUALITY.md`, `LOG.md`, and the wave-1 reviewer spec `.ufo/waves/round-47/build/RevScorecardRows.md`
(tracked, 216 tracked files under `.ufo/waves/round-47`).

Layout caveat (F7 of the wave-1 review): the checklist gate is layout-sensitive. All my checklist numbers
are from the canonical-layout clone `…/w2/W2ScorecardRows/kotoba-shokunin` (same directory name as the repo
root, so `trigger.name_directory` holds).

### 0.1 Re-measurement ledger (every command in the segments)

| Command (at the stated tree) | Claimed | Measured | Exit |
|---|---|---|---|
| `python3 -B verifiers/verify_skill_checklist.py --json` @ landing | exit 0, 11/11 | `pass 11 fail 0 na 0`, 11 check ids incl. `trigger.no_xml_tag` | **0** |
| same @ BASE | exit 1, 9 PASS / 1 FAIL | `pass 9 fail 1`; sole FAIL `governance.citation_resolves :: LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve` | **1** |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` @ landing | 1845 assertions, 0 failures | `0 failure(s) over 1845 assertions` | **0** |
| same @ BASE | 1597 assertions | `0 failure(s) over 1597 assertions` | **0** |
| `python3 -B verifiers/verify_surfaces.py --json` @ landing, **default resolution** | exit 0, 7/7 | `pass 7 fail 0`; 42 loader-kind entries; 8/8 loader classes; opencode 9/9 classes from 7/7 rules | **0** |
| same @ BASE | exit 2 | `{"checks": [], "error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode", "exit_code": 2}` | **2** |
| `python3 -B verifiers/verify_surfaces.py --self-test` @ landing | 99 assertions, 0 failures | `0 failure(s) over 99 assertions` | **0** |
| same @ BASE | 87 assertions | `0 failure(s) over 87 assertions` | **0** |
| `python3 -B verifiers/check_substrate_pins.py` @ landing, **default resolution** | exit 0, 3/3 | `OK 3/3 pins hold`; omp sha `fdbc8136…`=expect, mtime delta 0 ns, opencode sha `179ca421…`=expect | **0** |
| same @ BASE | exit 2, DRIFT 3/3 | `FAIL omp_binary_sha256: sha256 drift: expect=9513ef9f… got=fdbc8136…`; `FAIL omp_binary_mtime … delta_ns=140082506863270`; opencode path unreadable → `DRIFT 3/3` | **2** |
| `python3 -B verifiers/verify_corpus_integrity.py --json` @ landing | exit 0, 9/9 | 9 results, all `verdict PASS`; `corpus.index.tracked_files observed 60 expected 60` | **0** |
| same @ BASE | exit 1, 2 DRIFT | `tracked_files 59≠58` + `unindexed 1` (`corpus/lessons/round-46-verifier-spotcheck.md`) | **1** |
| `python3 -B verifiers/verify_corpus_independent.py --json` @ landing | exit 0 | exit 0 | **0** |
| same @ BASE | exit 1 | exit 1 | **1** |
| `bash verifiers/fault_injection_corpus.sh` @ landing | exit 0, ALL PASS | `verdict: ALL PASS` | **0** |
| same @ BASE | exit 1 | exit 1 | **1** |
| `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` @ landing | 1 → 0, exit 1 | `0` (grep exit 1) | **1** |
| discriminating cell: landing code × BASE baseline+census | exit 1 | `FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:api-entries/instructions, opencode:project/AGENTS.md, opencode:read-hook/AGENTS.md` | **1** |

Every number in the three segments is **true**. No fabricated count found.

---

## 1. Findings (severity-ordered)

### F1 — MED/HIGH — `SCORECARD.md:32` cites a LOG entry that does not exist at 7ad7fad (dangling pointer)

Freshness row, last sentence: *"Measured on the round-47 landing tree (hash in the LOG.md round-47
landing-pin entry)."*

`LOG.md` at 7ad7fad has **2326 lines and one** round-47 entry: the landing entry header at `LOG.md:2317`,
bullets `:2319`–`:2326`. There is no "landing pin" entry. The landing entry's own last bullet
(`LOG.md:2326`) ends: *"Falsification wave and landing pin follow in the next entry."* — and no next entry
exists at the landing commit.

Repro:

```
$ git -C kotoba-shokunin show 7ad7fad:LOG.md | grep -n "landing pin\|Round 47"
2317:## 2026-10-21 — Round 47 landing (hyaku campaign, steered round 47): …
2326:- Not claimed: … Falsification wave and landing pin follow in the next entry.
$ git -C kotoba-shokunin show 7ad7fad:LOG.md | wc -l
2326
```

The only "landing pin" heading in the file is the round-46 one (`LOG.md:2312`). The measurement itself is
true (I re-measured at `7ad7fad`, and the hash does appear in the **untracked** `.ufo/waves/round-47/after/SUMMARY.md`
— `git ls-files .ufo/waves/round-47 | wc -l` = 216, none of them under `after/`), but the pointer the row
gives a reader does not resolve. This is the same class the round-47 C3 erratum was built to excuse
(`LOG.md:2111` = a recorded absence whose evidence path is missing) — the scorecard row now carries the
mirror-image defect: a present-tense claim about a record that is not yet written.

Note the governance gate cannot catch this: the phrase is prose, not a backticked path token, so
`governance.citation_resolves` (11/11 PASS) stays green.

**Recommendation (integrator, not me):** append the promised landing-pin entry to `LOG.md` (append-only) and
let the row point at it, or reword the row to name the measured commit it was measured at (`7ad7fad`) instead
of a non-existent entry.

### F2 — MED — `SCORECARD.md:106` claims the falsification wave and verdict are already in `LOG.md`

`Round 47 completed` paragraph: *"…scores held (bands need the non-author closure); **falsification wave and
verdict detail in the LOG.md round-47 entries**."*

At 7ad7fad the falsification wave is **in flight** (this lane is part of it) and the verdict is **not
recorded**. The only round-47 `LOG.md` entry is the landing entry (`LOG.md:2317`), which explicitly defers
both: *"Falsification wave and landing pin follow in the next entry."* (`LOG.md:2326`).

Repro: see F1's grep. `grep -c "Round 47" LOG.md` → 1 entry.

So the sentence is a present-tense claim about a record that does not exist yet — the same defect class as
the round-41 calibration annotation (`SCORECARD.md:80`) was created to fix, and the same class the round-47
`Q19` rule (`corpus/QUALITY.md:30`) exists to catch: *"a value copied from an earlier record is struck, never
scored against."*

**Recommendation:** reword to "falsification wave and verdict to follow in the next `LOG.md` entry", or land
that entry before the row is read as settled.

### F3 — MED — `SCORECARD.md:32`'s stated band rationale contradicts the file's own rubric

Freshness row parenthetical: *"score held 8, **band 8.5 needs the non-author re-measure**"*, and
`SCORECARD.md:106`: *"scores held (bands need the non-author closure)"*.

Rubric (`SCORECARD.md:16-19`, verbatim): *"0–3 absent/wrong · 4–5 exists, claims uncited · 6 cited but dead
pointers or unre-verified this round · 7 all pointers resolve and carry their command, lane-measured · 8 +
independently re-measured by another lane · 9 + machine-checked or externally audited · 10 + repeated
non-author verification in the opposite direction. `0.5` = one of the two criteria of the next band met."*

Under that text, **8.5 = one of band 9's two criteria met** — i.e. *machine-checked* or *externally audited* —
whereas "independently re-measured by another lane" is **band 8's** criterion, which the row already carries
(it sits at 8). The row therefore names the wrong criterion as the blocker for the half-step. (The lane's own
round-17 calibration annotation reads the same way: *"8.5 lands; 9 is withheld because … all review lanes
remain lane-authored"* — i.e. 8.5 = machine-checked, 9 = also externally audited.)

This is not a cosmetic wording nit, because it decides the score. Measured against the rubric as written,
the round-47 C1 evidence **does** meet band 9's first criterion: it is machine-checked end-to-end
(`verify_surfaces.py` 7/7, `check_substrate_pins.py` 3/3, `verify_surfaces.py --self-test` 87→99 with two
new must-fail fixtures) and, since this wave, **independently re-measured by a non-author lane** (this
report). The lane's own wave-1 spec reaches the same place from the other direction
(`.ufo/waves/round-47/build/RevScorecardRows.md` §2.1: *"Conditional 9.0 only if BOTH conditions below are
met and recorded: (a) the opencode half of the loader surface is machine-covered and **non-vacuous** …
(b) a **named non-author lane** in wave 2 independently re-measures the re-derivation"*).

I checked condition (a) rather than assuming it:
* the opencode half is machine-covered and **non-vacuous**: `surfaces.opencode_extract` extracts **9/9**
  declared classes from 7/7 rules on the frozen 1.19.3 dump, and the retired v2.0.26 rule-set fixture is a
  must-fail generation guard (exit 1, `vacuity: extraction produced 0 class(es) from 7 rule(s)`), while the
  planted-name fixture must fail (exit 1, `extracted opencode class(es) undeclared in baseline:
  opencode:instructions/GUIDE.md`);
* the omp half is non-vacuous: `surfaces.no_uncovered_class` reports *"all 8 extracted loader class(es)
  declared"* and the vacuity arm fires when the shapes vanish (see §2, F6).

Repro for the two must-fail fixtures (real baseline + real census):

```
$ python3 -B verifiers/verify_surfaces.py --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s); …   → exit 1
$ … --opencode-strings verifiers/fixtures/surfaces/strings-opencode-planted-name.txt
FAIL surfaces.opencode_extract: extracted opencode class(es) undeclared in baseline: opencode:instructions/GUIDE.md  → exit 1
```

**Recommendation:** the *number* 8 is defensible as a conservative lane choice, but the stated reason is
false against the lane's own rubric, and the rubric (plus the lane's own wave-1 conditions (a)+(b), now
satisfied) supports **8.5, and 9 under the wave-1 spec's conditions**. At minimum the parenthetical must be
rewritten to the rubric's own terms; the score decision is the integrator's, and the axes are advisory.

### F4 — MED — `SCORECARD.md:31` names S003 as a source without naming the clause it does not adopt

Operability row: *"…lands with four fixtures … sourced on S003 + S012."*

`corpus/SOURCES.md:16` (S003) states, in the same cell, *"The description cannot contain XML tags, must be
third person, and states what the skill does and when; **body under 500 lines**"*. This lane's `SKILL.md` is
**528 lines** (`wc -l SKILL.md` = 528; the live gate prints *"528 lines within budget 600"*). The rule as
landed enforces **only** the XML-tag clause; the body-length clause is not adopted, and the row does not say
so, so a reader can read "sourced on S003" as an S003 conformance claim the lane does not make.

The wave-1 review called this out as a **mandatory** note: *"CE6 (F8) — the rule is adopted from S003's
XML-tag clause only. The same S003 row also states 'body under 500 lines'; this lane's `SKILL.md` is 525
lines … The row must name the body-length clause as **not adopted** (named residual) or it overclaims S003
conformance"* (`.ufo/waves/round-47/build/RevScorecardRows.md` §6 F8). The landed row carries no such note.

The row is otherwise honest about the *other* divergence — *"no code-span exemption; YAML escapes caught;
arrows/comparisons pass"* states that S012's stricter "any `<`/`>`" clause is **not** enforced (the live
detail string says so: *"Anthropic's packager bans any '<'/'>' and is stricter"*). The 500-line clause is the
one omission.

Also unlanded from the wave-1 spec (same section): the mandated cross-claim note that the description edit
changes the omp description-cache key (`(name, description-as-loaded)`).

**Recommendation:** add one clause — *"S003's body-under-500-lines clause is not adopted (SKILL.md is 528
lines)"* — and, if "sourced on S003 + S012" is kept, say that only S003's XML-tag clause is enforced.

### F5 — MED — no round-47 rows in the Move log (the round's before→after is not recorded where rounds 43–46 record theirs)

`SCORECARD.md:129` `## Move log`; the round-43/44/45 tables at `:188`–`:196`, the round-46 table at
`:227`–`:233`. There is **no round-47 table**: `grep -n "^| 4[3-9] |" SCORECARD.md` returns rows for 43, 44,
45, 46 only.

The wave-1 spec wrote the three rows verbatim (`RevScorecardRows.md` §3), including the measured before
columns (`surfaces exit 2 … pins exit 2 DRIFT 3/3 … checklist 9 PASS / 1 FAIL`) and the `held` reasons.
`AXES.md` § Working the axes: *"measure it … record before→after in `SCORECARD.md`"*. The before→after
survives only inside the axes rows and the `## planned` prose; the table the lane uses for exactly this
purpose is silent for round 47.

**Recommendation:** append the three round-47 Move-log rows (append-only, after `:233`).

### F6 — LOW/MED — the `Last change` cells are stale for the three rows round 47 touched

Axes table header at `SCORECARD.md:26` ("| Axis | Score | Evidence … | Owned? | Last change |"); the three
touched rows still read `16` (operability, `:31`), `21` (freshness, `:32`), `17` (calibration, `:33`) —
while each row's own evidence text is headed *"round 47 (C2/C1/C3 …)"*.

The wave-1 spec (§6 F5) called the column a status field and required re-stamping the three touched rows to
`47`; the landed edit did not. `AXES.md` § SCORECARD.md contract requires a last-change round per row, so
`16`/`21`/`17` is now a false present-tense claim on three rows the round itself rewrote. (Depth 15 /
consistency 15 / coverage 15 / adjacency 21 are untouched by round 47 — pre-existing staleness, not this
round's.)

### F7 — LOW — `SCORECARD.md:108`'s round-48 parenthetical is accurate but reads as a silent-green risk that does not exist

*"a rename-robust omp call-shape rule with a must-fail rename fixture (the allowlist still goes vacuous on
the next minifier rename)"*.

Measured (fixture `verifiers/fixtures/surfaces/strings-omp-18.12.5.txt`, callees renamed):

```
# total rename (lq|Xl|Fo → Zq):
FAIL surfaces.literal_present: 8 loader literal(s) not verifiable …
FAIL surfaces.no_uncovered_class: vacuity: 0 loader class(es) extracted from the omp dump while the
     baseline declares 8 loader-group class(es) for it — a moved or renamed substrate must FAIL, never pass
     silently; extractor blind: 8 declared literal(s) present in the omp dump but no registration shape extracts
→ exit 1

# partial rename (Fo → Fw only):
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: omp:github/copilot-instructions.md …
PASS surfaces.no_uncovered_class: all 7 extracted loader class(es) declared
→ exit 1
```

So the allowlist does go vacuous (0 extracted) on a total rename — the parenthetical is literally true — but
the gate **fails closed** in both the total and the partial case (round-21 vacuity guard + round-31
extractor-blindness arm + `literal_present`). The residual risk is *re-derivation effort*, not a silent
green. As written the parenthetical can be read as "the next rebuild reads green"; it does not. Cheap
reword; no substantive defect.

### F8 — LOW — `SCORECARD.md:287`'s "round 47's C1 satisfies both readings" is unsupported under the owned-axis reading

The running-window paragraph (round-46 refresh, `SCORECARD.md:287`) closes: *"round 47's C1 satisfies both
readings."* The all-axes reading holds (freshness 8.0 is the lowest non-retired axis). The **owned** reading
does not: the lane owns depth (9) + the consistency sub-axis (10) (`SCORECARD.md:3-4`, `:28-29`), so the
lowest-scoring owned non-retired axis is **depth**, and round 47 carries no depth or consistency claim
(C1 freshness, C2 operability, C3 calibration — all advisory). The wave-1 review flagged exactly this
(§6 F6: *"The **owned** reading is not: … the lowest-scoring owned non-retired axis is depth (9), and round 47
carries no depth claim"*) and proposed a round-48 depth claim as the discharge. The landed `Next: round 48`
block (`:108`) lists three candidates and **none is a depth claim**, so the owned-axis obligation stays
undischarged and `:287`'s "both readings" is not supported.

Adjacent to my three segments (it is the saturation paragraph), reported because it is the sentence that
justifies round 47's admissibility.

### F9 — INFO/ADJACENT — the floors vector is load-conditional; `LOG.md:2324`'s "all 9 instruments at floor" does not reproduce right now

`LOG.md:2324`: *"Floors ratcheted in step (`verifiers/floors-registry.json`, `verifiers/check_assertion_floors.py`):
surfaces 87 → 99, checklist 1597 → 1845; **all 9 instruments at floor**."*

At the landing tree, right now, under wave load:

```
$ python3 -B verifiers/check_assertion_floors.py
PASS harness observed=10 floor=10
PASS corpus_integrity observed=150 floor=150
PASS corpus_independent observed=91 floor=91
PASS surfaces observed=99 floor=99
PASS checklist observed=1845 floor=1845
PASS pins observed=62 floor=62
FAIL harness_independent self-test timed out after 120s (hung?)
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=150 floor=150
→ exit 2
```

Standalone, the same self-test passes but takes longer than the guard's budget:

```
$ time python3 -B verifiers/verify_harness_independent.py --self-test
real 2m16.734s   → 0 failure(s) over 104 assertions   (exit 0)
```

The vector itself is right (all nine floors are exactly met: 10/150/91/99/1845/62/104/330/150) and this is the
known standing debt ("IND self-test >120s under wave load"). But the landing record states it unconditionally,
so the reader is told a gate is green that is currently red under load. The three SCORECARD segments do not
themselves cite the floors vector, so no SCORECARD sentence is false on this point — recorded because the
paragraph at `:32` and `:31` cite self-test counts that the same guard measures.

---

## 2. Claims that survived the attack (findings too)

* **Every numeric before→after in all three segments reproduces exactly** (§0.1): 11/11 and 9/1 checklist,
  1845 and 1597 assertions, 7/7 and exit-2 surfaces, 3/3 and exit-2 DRIFT 3/3 pins, 99 and 87 surfaces
  self-test assertions, 9/9 and 2-DRIFT corpus integrity, corpus independent exit 1→0, fault harness
  exit 1→0 ALL PASS, frontmatter `<skills>` 1→0 (grep exit 1).
* **The "7/7 at default resolution" claim is real, not an artifact of my flags**: the opencode default moved
  to the npm `opencode-ai` ELF in both instruments (`verifiers/verify_surfaces.py:128-131`,
  `verifiers/check_substrate_pins.py:64-67`), so the bare commands work for a reader who has no flags.
  Base default path `/home/vgpnk/.opencode/bin/opencode` is gone from the host — that is *why* BASE exits 2.
* **The discriminating cell is real and points the right way**: landing code × BASE baseline+census → exit 1,
  naming exactly the three retired v2.0.26 ids (`opencode:api-entries/instructions`,
  `opencode:project/AGENTS.md`, `opencode:read-hook/AGENTS.md`) — i.e. the re-derivation is not a copy of the
  old pins.
* **The C1 census claim is true as stated**: `corpus/knowledge/instruction-surface-census-round13.md:212`
  (§ B′) carries exactly **9** re-instated opencode ids; the ledger at `:287`/`:308-319` marks exactly **3**
  v2.0.26 ids retired and re-verdicts `opencode:config/instructions` **governed**; `config/instructions` now
  has a proven consumer (`for(let O of T.instructions)`).
* **The C2 fixtures are live discriminators — I re-ran the wave-1 mutation battery myself** (7 mutants, same
  replacements as `.ufo/waves/round-47/build/C2CriticRule.md`'s design): every one turns the self-test red
  (M1 4 failures, M2 7, M3 7, M4 3, M5 1, M6 5, M7 2 — all exit 1 over 1845 assertions), and the unmutated
  detector keeps the "arrows/comparisons pass" control green. The four fixtures
  (`verifiers/fixtures/checklist/xml-tag-{codespan,control,dq-escape,split}`) are tracked.
* **The C3 erratum mechanism is fail-closed on all four classes the row claims** — I ran each class against
  the landing tree in the scratch clone and restored after each:
  * in-place laundering of `LOG.md:2111` → `FAIL … erratum LOG.md:2111 '…post-r44-hunt.py': line text drifted` (exit 1);
  * restored runner (created `.ufo/round-45/drafts/v10/post-r44-hunt.py`) → `FAIL … stale, the path now resolves` (exit 1);
  * appended copy (same line appended to `LOG.md`) → `FAIL LOG.md:2327: '…post-r44-hunt.py' does not resolve` (exit 1);
  * past-horizon row (`errata_problems` called with line 2400, horizon 2315) → `erratum LOG.md:2400 … is past horizon 2315 or absent`.
  The in-source design deviates from the wave-1 spec's "digest-pinned external registry"
  (`RevScorecardRows.md` §6 F2), but the deviation is **sound on the evidence**: the line-sha256 + quote +
  token + horizon pins close all four laundering doors I could construct, and the row says "in-source" plainly.
* **The C3 corpus claims are true**: `corpus/README.md:63-64` indexes `lessons/round-46-verifier-spotcheck.md`
  and `lessons/round-47.md`; `verifiers/corpus-baseline.json` `corpus.index.tracked_files expect 60` (the
  58→60 move) with an appended `round47` note that names both indexed files, and the historical
  `measured_against` block is explicitly retained as history (as the `round46_landing` note already did);
  `verifiers/fault_injection_corpus.sh:117` anchors the planters inside `## Coverage map`.
* **The `Round 47 completed` paragraph's Q19 correction is true**: `SCORECARD.md:101` still carries the stale
  "installed omp 18.12.3" / "Before: surfaces 5/7, pins 1/3" text, `corpus/lessons/round-47.md:19` (M20)
  records it as the stale-premise class, and the measured before-values I re-measured (omp 18.12.5 via
  `omp --version` → `omp/18.12.5`, sha `fdbc8136…`; surfaces exit 2; pins exit 2 DRIFT 3/3) match the
  paragraph. The planned C3 capability was indeed replaced by the calibration claim, and the SOURCES frontier
  step did run as S012–S015 (`corpus/SOURCES.md:25` onward) — no capability row entered (capability table
  still two rows, first-working rounds 23 and 29), which is what `AXES.md` § Capabilities requires.
* **The `Next: round 48` block's harness figure is true**: `python3 -B verifiers/verify_harness_claims.py --json`
  → exit 1, verdicts **21 PASS / 7 DRIFT of 28**, the seven DRIFT ids being `omp.db.rows`, `omp.offered.skills`,
  `omp.cache.misses`, `omp.catalogue.total`, `omp.catalogue.missing_names`, `omp.cache.verified_skills`,
  `oc.roots.names_plus_builtin`, with `catalogue_total 10 / catalogue_matched 7 /
  catalogue_missing_names ["create-toolset","unreal-mcp","unreal-skill"]` — i.e. exactly the "three new host
  skills" the block names. The round-46 residuals it lists are carried honestly (not re-verified by me; see §4).
* **The three rows' scores holding is the right call on the numbers** — every claim behind them verifies.

---

## 3. Score decisions (recommendation only — the lanes are advisory; the integrator rules)

| Axis | Landed | My finding | Recommendation |
|---|---|---|---|
| freshness | 8 (held) | numbers true; the *stated* blocker misquotes the rubric (F3) | Keep or move to 8.5 — but fix the rationale. Under the rubric as written, 8.5 = one of band 9's {machine-checked, externally audited}; the C1 evidence is machine-checked and (as of this wave) non-author re-measured. Under the lane's own wave-1 conditions (a)+(b) (machine-covered **non-vacuous** opencode half + named non-author re-measure) both are now met, so 9 is supportable if the lane wants it — with the reviewer seat named. If the score holds at 8, the parenthetical must change to the rubric's terms. |
| operability | 8.5 (held) | numbers true; F4 (S003 clause scope) and F6 (last-change cell) | Score hold is right (r46 residuals survive; band 9 needs the checklist surface machine-covered). Fix F4 (one clause) and F6. |
| calibration | 8.5 (held) | numbers true; F6 | Hold. The erratum registry's own fail-closed behaviour is now independently re-measured by this lane (F-a…F-d above) — that is the round-48 C3 the `Next: round 48` block should have named, and it does not. |
| depth / consistency / coverage / adjacency | unchanged | not touched by round 47 | No move. Note F8 (owned-axis obligation). |

---

## 4. What I did NOT check

* I did **not** re-run the comparator residual arms named in the segments (mirror opt-out, missing verdict,
  `NaN`/case-variant shadow keys, record-level `kind` drift, payload-selectable committed scope-outs) — they
  live in `.ufo/round-46/evidence/w2/l1-matrix/` and are not SCORECARD-row claims; I took them on the row's
  word and did not attack them.
* I did **not** independently re-derive the opencode loader anchors from the 1.19.3 dump by hand. I verified
  the *machine* outcome (9/9 classes from 7/7 rules, the two must-fail fixtures, the retired-id discriminating
  cell) and the census's prose, not each anchor string against the binary.
* I did **not** verify `PROVINCE.md`, `plans/round-47.md`, `corpus/lessons/round-47.md` M21/M22, or
  `corpus/QUALITY.md` Q19 beyond the single cited lines (M20, Q19) that the segments quote.
* I did **not** re-measure `verify_harness_claims.py` at BASE (only at the landing tree); the "21/28 before
  and after" identity rests on `.ufo/waves/round-47/before/SUMMARY.md` (tracked) plus my landing-tree run.
* I did **not** determine whether the `harness_independent` self-test's 136.7 s runtime is load-dependent or a
  genuine hang (F9); I measured it standalone once and through the guard once.
* I did **not** run the SOURCES contract census commands (`scripts/sources-census.sh validate`) beyond
  confirming the S012–S015 rows exist in `corpus/SOURCES.md`; the frontier step's own verification belongs to
  the wave-1 lanes that wrote it.
* I did **not** execute the `opencode` wrapper or any omp session; `omp --version` (→ `omp/18.12.5`) and the
  frozen dumps under `/fast/scratch/kotoba-r47/shared/` were the only substrate reads. Frozen bytes match the
  pins: `omp-18.12.5` sha256 `fdbc8136…` = `verifiers/baseline.json` pin, `opencode-1.19.3` sha256
  `179ca421…` = pin.
* I did **not** re-run the wave-2 peer batteries (mutation / errata / census lanes); my §0.1 and §2 numbers
  are my own, and peers' findings were in flight.
* I did **not** check the fleet-root `PROTOCOL.md` / sibling lanes' conventions beyond `AXES.md`, `MISSION.md`
  and kotoba's own file.

---

## 5. One-paragraph summary

The round-47 SCORECARD segments are **numerically clean**: every counting command in `SCORECARD.md:31/32/33`
re-measures exactly at BASE `c61a973` and at the landing `7ad7fad` (11/11 and 9/1; 1845 and 1597; 7/7 and
exit 2; 3/3 and exit 2 DRIFT 3/3; 99 and 87; 9/9 and 2 DRIFT; corpus independent 1→0; fault harness 1→0 ALL
PASS; frontmatter `<skills>` 1→0), the C2 detector's seven mutants all die in my own re-run, the C3 erratum
fails closed on all four laundering classes I could construct, and the "Round 47 completed" Q19 correction and
the round-48 harness figure (21/28, three host skills) are true. What does **not** hold: `:32` points at a
"LOG.md round-47 landing-pin entry" that does not exist at the landing commit (`LOG.md:2326` defers it to a
next entry that is not there); `:106` claims the falsification wave and verdict are already in the LOG's
round-47 entries (they are not — that entry is in flight); `:32`'s "band 8.5 needs the non-author re-measure"
misquotes the lane's own rubric (`SCORECARD.md:16-19`), where the non-author re-measure is band 8's criterion
and 8.5 needs band 9's machine-checked/externally-audited criterion — which the round-47 evidence now meets;
`:31` says "sourced on S003 + S012" without naming that S003's body-under-500-lines clause is **not** adopted
(`SKILL.md` is 528 lines), a note the wave-1 review mandated; the Move log has no round-47 rows; and the
`Last change` cells of the three touched rows still read 16/21/17. Scores: nothing false in the cells, so no
score is *wrong*, but freshness's held-at-8 rationale is wrong and the held-at-8.5 pair needs the S003 scope
note before the row is honest.

---

## 6. Coordination note — an in-flight sibling edit touches the file my freshness numbers depend on

While I ran, the **production working tree** (not my scratch clone) carried an uncommitted sibling edit to
`verifiers/verify_surfaces.py` (`git status` → ` M verifiers/verify_surfaces.py`; mtime 14:05:21; header
comment *"Round-47 falsify candidate (W2DropOC2, not landed)"*). It tightens **OC-2**: it adds
`OC_CANDIDATE_ARRAY_RE` (both anchors must sit in one array expression carrying the `disableClaudeCodePrompt`
gate), changes OC-1's gate test from `OC_GATE not in m.group(0) or OC_GATE in dump` to `OC_GATE in m.group(0)`,
and makes OC-2 require the new array regex.

This is **not** mine (my scratch clone is clean: `git status --short` empty, `git diff --stat` empty at
`/fast/scratch/kotoba-r47/w2/W2ScorecardRows/kotoba-shokunin`), and I did not touch production. Every number in
this report is from **committed bytes** at `7ad7fad` in the scratch clone, so nothing here is invalidated.

Forward-looking, for the integrator: if that OC-2 candidate is landed, the freshness row's
*"opencode extraction 9/9 declared class(es) from 7/7 rules"* and my §0.1 rows change, and `SCORECARD.md:32`
plus `corpus/knowledge/instruction-surface-census-round13.md` § B′/ledger must be re-measured (and the census's
`opencode:config/AGENTS.md` / `opencode:claude-home/CLAUDE.md` anchors re-derived) before the segment is read
as settled.
