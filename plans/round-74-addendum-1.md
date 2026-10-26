# Round 74 — addendum 1 (errata E1, committed before any counter scored any data)

Plan `plans/round-74.md` froze at `329e7d91d7d750031c35d264f0e34af1d0ce8385`. Wave 1 (34 seats; results
`.ufo/waves/round-74/w1-results.json`) attacked the plan and the two counter drafts before any data existed:
no counter has scored a claim row, no entry, no registry row and no snapshot is committed. Every change
below is therefore a pre-data erratum (Q28: a rule changed after any seat has scored data is not the claim's
rule; nothing has been scored). Sources: `w1/ReviewerPlanR74.md` (F1–F11), `w1/CriticClaimsR74.md`
(C1-1…C1-7, C2-1…C2-4), `w1/ScoutSibSoujiTabiR74.md` (Finding 1), `w1/ExecSibCounterR74.md` § Calibration,
`w1/ScoutSibTameshiTsukuroiR74.md`, `w1/ExecSkillGatesR74.md`. The plan's text stays as filed; this addendum
supersedes it where it differs (append-only, Q03).

## E1.1 C1 — relabelled `coverage`; predicate strengthened (ReviewerPlanR74 F3/F4/F5; CriticClaimsR74 C1-1…C1-7)

**Axis.** C1 moves three pages the lane did not hold (0 registry rows, 0 phrase hits at base) from frontier to
Core and carries them into `SKILL.md`'s decision rows. By the sizing list ("name the axis by the surface the
round changes") the counted clauses are new held ground: C1 is a **`coverage`** claim (frontier → core: the
Agent Skills `skill-creation/` authoring guides), with the `SKILL.md` rows (conjunct (e)) as the proof the ground
reaches the guidance, not as a separate depth claim. `depth` is not claimed this round. The lowest-axis
obligation is carried by C2 (`freshness`, 8).

**Headline (unchanged text, re-labelled):** `python3 -B verifiers/check_spec_craft.py --rev <rev>` prints
`spec craft pages backed N of 3`, exit 0 iff N == 3. Conjuncts (a)–(f) stand as filed, with these
tightenings, each measured by a seat on a committed world before data:

- **(a′)** at least one of a row's ≥ 2 tokens is **page-unique**: word-bounded in `P`'s snapshot and in neither
  of the other two pages' snapshots (kills the site-chrome banner and subtitle tokens, C1-2).
- **(b′)** the cited row's URL path ends `/skill-creation/<P>.md` (kills a wrong-id row, C1-3).
- **(c′)** the snapshot's sha256 equals **three** things: the pin in `snapshots/MANIFEST.sha256`, a **constant
  pinned in the counter's source** (Q33 — the measured revision cannot supply its own trust anchor), and the
  64-hex digest carried in the cited registry row's anchor cell; `snapshots/FETCH-LOG.tsv` at the measured
  revision records `page url status bytes sha256 date` with status `200` and bytes/sha equal to the snapshot
  (kills the 404-body snapshot and the self-attested pin, C1-4). Absent entry is `0 of 3`, exit 1 (the
  do-nothing ladder of C1-7); a present-but-tampered snapshot is exit 2.
- **(d′)** the located quote's line lies after the page's first `# ` heading, is not a heading, is not inside the
  blockquote block between that heading and the first `## ` heading, and is not a link to another
  `skill-creation/` page (kills the banner and subtitle quotes).
- **(e′)** each counting `SKILL.md` row's action cell carries ≥ 1 **page-unique** token of `P` and ≥ 5 words that
  are neither tokens nor members of a filler list pinned in the counter (a lexical approximation of "says
  something": `use see page guide says the as for this that with and or of to a an it is are be by on in at`
  and the row's own cited id) — kills `Use \`--dry-run\` as the guide says.` (C1-1).
- Word-bounded means ASCII-lookaround `(?<![A-Za-z0-9_])…(?![A-Za-z0-9_])` on the whitespace-collapsed
  snapshot (C1-5), defined in the counter's docstring.
- **Control worlds** (committed before data, each must read < 3): the plan's list plus the critic's W1–W8 (chrome
  banner, subtitle, wrong id, token-stuffed, 404 snapshot, one snapshot for three pages) and the **staged-entry
  copy with fetched snapshots but no lane fetch record** (F3): staged text has no sha256, no status and a
  2026-10-23 date, so (c′) and (b) refuse it.
- **Bound unchanged and now named (Q26/Q51):** form, sources, tokens and pinned bytes are counted; whether a
  rule sentence is true of the page is a reviewer judgement — assigned in wave 2 to named seats whose
  committed reviews are cited.

## E1.2 C2 — headline, (b), (e), (f) and the 9-cell projection (ReviewerPlanR74 F1/F2/F6; CriticClaimsR74 C2-1…C2-4; ScoutSibSoujiTabiR74)

**Headline:** `python3 -B verifiers/check_sibling_reread.py --rev <rev>` prints
`sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads N of 20`, exit 0 iff N == 20. The
words "re-read" leave the headline: the counter measures pin, cells, quote location and a recomputed diff; what
a sibling's boundary sentence means is reviewer judgement (C2-2; Q26).

- **(a)** the counter builds the **9-cell projection** of each 10-cell entry row and runs the pinned base checker
  on the projection; it reads the tenth `delta` cell itself (C2-1: the base checker refuses a tenth cell).
- **(b)** the row's commit cell equals the lane's head in the freeze file **as committed at the measured revision**,
  whose sha256 equals a constant pinned in the counter (Q33, C2-3); that commit must resolve in the lane repo and
  be an ancestor of its branch head (`merge-base --is-ancestor`), failing closed with exit 2 naming the lane when
  the object or branch is missing (C2-4). Live distance (`rev-list --count <frozen>..<branch>`) is printed per
  row and not counted.
- **(e) replaced:** the whole-file `grep -w kotoba` clause is withdrawn. It contradicted conjunct (a) (the base
  checker's `none` rule reads the frontmatter description and `PROVINCE.md` only, `check_sibling_census.py:595-604`)
  and made `tabi`'s honest `none` row unreachable: tabi's `SKILL.md` names kotoba twice inside a code-span roster
  string (`SKILL.md:1313,1450`), which is a citation, not a split. (e) becomes the base rule, already inside (a).
  The lanes whose `SKILL.md` body names kotoba despite a `none` row are **printed** (tabi: 2) and reported beside
  the count, not counted (Q28).
- **(f) added** (C2-2, the strongest mechanical conjunct): each row carries an eleventh `evidence` cell
  `<path>:<line> <changed|unchanged> "<6–25-word quote of the deciding sentence>"`, the path being a file of the
  sibling at the frozen head or, behind the prefix `kotoba/`, a file of this lane at the measured revision (the
  tsukuroi split is stated in kotoba's own corpus). The counter re-checks that the line exists and the quote lies
  within two lines of it, that the quote's line is not a heading, that the path stays inside the repository, and that
  the declared flag equals the recomputation (file text at the frozen head against the round-49 pin, or at the
  measured revision against the base revision). The planned "ownership marker" clause is **dropped before use**: the
  base checker's marker list (`owns/own/owned/route/routes/routing/NOT/see above/…`) is a lexical approximation that
  rejects the honest tsukuroi sentence ("Host package and initramfs hooks are tsukuroi's"), which carries none. For a
  `none` row the absence sweep is the base none rule inside (a).
- **Carry-forward, declared:** a pure mechanical re-pin with recomputed cells is the lowest honest re-verification
  of the mechanical facts and scored 19–20 of 20 on the plan's own controls (`ExecSibCounterR74` § Calibration;
  `CriticClaimsR74` C2-2: all 20 r49 quotes still locate at the same lines, so the plan's claim that "quotes die at
  moved lines" was false). With (f) the do-nothing and bump-only worlds stay below 20; the carry-forward world's
  measured score is reported as the upper bound a mechanical re-pin reaches. The classification judgement is not
  counted: it is assigned to wave-2 reviewers (≥ 10 lanes re-derived independently, disagreements recorded
  verbatim, Q16). One judged change is recorded **before data**: **tsukuroi `none` → `adjacent`** (basis kotoba:
  `corpus/knowledge/hook-files-round59.md:19-20` states "Host package and initramfs hooks are tsukuroi's", a
  committed corpus scope surface under the round-49 rule; `ScoutSibTameshiTsukuroiR74`). That makes
  `check_sibling_census.py --skill SKILL.md` demand that kotoba's description name tsukuroi, so **C2's surface
  list gains the frontmatter `description` of `SKILL.md`** (one ownership clause, net description length ≤ 1,024
  characters, `check_sibling_census.py --skill` exit 0 and the checklist unchanged). The r49 entry is untouched.

## E1.3 No-harm, separability, landing (ReviewerPlanR74 F1/F10/F11; ExecSkillGatesR74)

- The plan's no-harm line "`check_sibling_census.py` on the r49 entry and `--province`" is replaced by: the base
  checker on the **r74** entry with `--province PROVINCE.md` (`rows 20 verified 20`, `province rows 20 matched 20`),
  and on the r49 entry **without** `--province` (row-shape regression only; the r49 pins are historical).
- Each new counter lands with its own `## Gate registry` row, in its own claim's commit; the corpus baseline is
  re-recorded in the commit that adds tracked corpus files (`ExecSkillGatesR74` F2: 139 → 140 with the entry alone).
  The registry universe is 58 → 60. **`ReviewerPlanR74` F10 (a floors row per counter) is not adopted:** the r73
  counters `check_cn_vendor_surfaces.py` and `check_report_pointers.py` carry no row in `verifiers/floors-registry.json`
  (15 rows at base: `python3 -c "import json;print(json.load(open('verifiers/floors-registry.json'))['instrument_total'])"`),
  and a row needs the guard's in-file tables and the tip battery's instrument pins edited together — a change to two
  instruments outside the claims. The two new self-tests are therefore unfloored, recorded as a known gap in the
  lesson, not claimed as guarded.
- **Separability (one-way proof was not enough):** each counter is measured at a **sandbox revision that holds only
  its own claim's files on the base** (labelled `sandbox`, with its clone path, Q41), beside the measurement at the
  lane's landing revision; the receipts name both.
- The SKILL.md budget stays 600 lines (Q65): 570 base + 14 (C1 subsection) + 2 (registry rows) + 4 (routed item
  5) = 590; the frame sentence is net 0 lines; the description edit keeps the 18-line frontmatter.

## E1.4 Corrections of record (append-only)

- **Q55 / ReviewerPlanR74 F8:** `receipts/base-battery-l1.txt` line 2 says "~22:3x -03"; the run (wall 236.6 s) is
  recorded before the plan commit `329e7d9` (22:27:29 -03) and after the round launch (22:05:09 -03); the clock
  label is struck, the wall time and revision stand.
- **ReviewerPlanR74 F9:** the census command in the plan's before-table is the host-absolute
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
- **ReviewerPlanR74 F7 — three id spaces, stated once:** lane registry `S001`–`S222`; the package `S203`–`S390`
  (20 of its ids collide with the lane's, `S203`–`S222`); the campaign's absent-defect register uses **per-round**
  ids, so the register's `S236`/`S237` (round 10: `skills.sh/docs`, `skills.sh/audits`) are NOT the package's
  `S236`/`S237` (agentskills.io using-scripts and quickstart). C1's three pages are in no fetch-failed class; all
  three answered HTTP 200 on 2026-10-25 (`w1/ScoutSpecCensusR74.md`, `w1/ExecQuarR74.md`). The plan's table row
  "staged S236, S237 … quarantined" is a reading of the register by id, struck.
- **Q45 (target reachable):** `ScoutSpecCensusR74` — all three pages carry ≥ 2 usable tokens; the target stays
  `3 of 3`. C2: 20 of 20 lanes have a resolvable freeze head (`ReviewerPlanR74` § 1).
