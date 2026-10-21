verdict: r47's report is bound by a six-section contract (two sections added in the r47 prompt) and inherits eleven open items from r46 — a pending discernment spot-check, two L0 questions that were never filed to the side channel, seven carried residuals, a dead measurement harness, a stale-frontier row and two unrecorded baseline re-records — while the r46 report itself demonstrates the exact defect r47 must avoid: two of its three printed counting commands cannot be re-run as written (C1 exits 2 on argparse, C2 exits 1 on a traceback).

# RevPriorRoundReport — r46 report shape and the promises r47 must answer

Lane seat: reviewer. BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (lane repo `kotoba-shokunin`,
branch `master`, jj-colocated). All path:line citations below are at BASE unless stated.
Target read: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-46/kotoba.md` (read-only, fleet root).

Scope note: this seat produced no production edit, no patch and no lane-repo mutation. All
measurements ran in two scratch clones under `/fast/scratch/kotoba-r47/RevPriorRoundReport/`
(a plain clone at BASE, and a canonical-layout clone whose parent symlinks the fleet root).
No tool was installed or upgraded this round; no `pacman` transaction was attempted.

---

## 1. The required-sections shape r47's report must have

**Contract source (binding).** `/home/vgpnk/Projects/shokunin/.ufo/prompts/kotoba-round-47.md:99`
("## 4. Report contract"), report path `:101` (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-47/kotoba.md`
on the fleet repo). Required sections **in order**:

| # | Section | Contract line | r46 report line | r46 conform? |
|---|---|---|---|---|
| 1 | **Work performed** — opens by naming the round's declared claims (1–3) and their target axes or capability; one bullet per work item, each with an evidence pointer | `kotoba-round-47.md:104-106` | `.ufo/reports/round-46/kotoba.md:5` (claims named at `:7-10`) | yes |
| 2 | **Landed changes** — every change tied to a LOG.md entry and to the commit hash carrying it | `:107-108` | `:31` (table with LOG entry + commit columns) | yes |
| 3 | **Before → after measurements** — one per claim, each with the counting command and the commit measured against | `:109-110` | `:43` (C1 `:47`, C2 `:56`, C3 `:76`, "no axis harmed" battery `:90-99`) | yes |
| 4 | **Sources & frontier** — SOURCES rows before→after with the counting command, rows added by tier, rows touched old→new, frontier rows advanced | `:111-115` | `:112` | yes (present) |
| 5 | **Trend verdicts** — one verdict each for `expansion`, `quality`, `discernment`; evidence; no scalar | `:116-117` | `:133` | yes (present) |
| 6 | **SHONEN** — one line per box of SHONEN.md; named non-author verifier for `x`, resolvable evidence pointer for the partial mark, blank for untouched | `:118-119` | `:103` (4 lines, 4 boxes) | yes |

**Sections 4 and 5 are new in r47.** `diff` of the r46 and r47 prompt report contracts
(`diff <(sed -n '/^## 4\. Report contract/,/^## 5\./p' …)`, exit 1) shows r47 adds the
**Sources & frontier** and **Trend verdicts** bullets and changes the marker rule
(`kotoba-round-47.md:121-125`): a contentless report fails the round "missing required sections
**other than Sources & frontier and Trend verdicts**" — i.e. those two are conformance items, not
marker predicates. The r46 report already carries both, so the shape is a superset of r46's.

**Shape defect inherited from r46 (ordering).** The contract says "in order"; r46 put SHONEN
at `:103` **before** Sources & frontier (`:112`) and Trend verdicts (`:133`). The marker rule only
tests for missing sections, not order, so this is not a fail — but r47 should emit the six
sections in contract order, since the driver only checks headings. Machine-checked
consequences r47 must satisfy:

- **Sources & frontier heading** — `scripts/shokunin-watchdog.sh:302-316` greps
  `^#{1,6}[[:space:]]+Sources[[:space:]]*&[[:space:]]*frontier` case-insensitively; a missing
  heading logs `sources-conformance-defect` (never a relaunch, per the comment at `:302-304`).
- **SHONEN marker + size floor** — `scripts/shokunin-watchdog.sh:140-163` (`report_of`) requires a
  line matching `^#+[[:space:]]*SHONEN` or `^[[:space:]]*-[[:space:]]+\*\*SHONEN\*\*`, and
  `wc -c >= MIN_REPORT_BYTES` (default 400, `:54`). r47's report is well over 400 bytes.
- **Census gate** — `scripts/sokunin-watchdog.sh:318+` runs `sources-census.sh validate`; the
  prompt requires exit 0 at round end (`kotoba-round-47.md` §2b.2).
- **Report path** — fleet root, not the lane repo (`kotoba-round-47.md:101`). r47 must also
  commit it in the fleet repo and state the push disposition (see promise P9).

**Extra shape obligations the r47 prompt adds beyond §4** (they belong inside "Work performed"
and "Landed changes"): wave seat counts, role mix, dead seats, round total, and the
planner-seat mapping note (`kotoba-round-47.md` §6 swarm paragraph). r46 discharged this at
`.ufo/reports/round-46/kotoba.md:27-29` (L2 swarm, 10 seats, provider exhaustion, seat reports).

---

## 2. Promises r46 left that r47's report must answer

### P1 — the pending discernment verdict (r46's own conditional promise)

`/home/vgpnk/Projects/shokunin/.ufo/reports/round-46/kotoba.md:137`:

> **Discernment: `unchanged`, pending.** A bar now exists (Q01–Q18), but no non-author
> spot-check has run. If the orchestrator's spot-check of ≥1 admit (S003) and ≥1 reject (S011)
> agrees, this becomes `improved`.

The condition has since been met on record. `corpus/lessons/round-46-verifier-spotcheck.md:8-13`
(integrator/kaika, not the lane — "Written by the integrator, not the lane", `:3-5`) records the
admit sample (S003/S006, "agree", W3ReviewKotoba) and the reject sample (S011, "agree"), and
`:17` adjudicates "Trends: … **discernment improved (narrow, 3/3 spot-check agree)**". The file is
committed at BASE (`c61a973` "round-46 verifier spot-check (integrator, kaika)"), and the fleet
verifier reports are at `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika-w3/kotoba-review.md` and
`kotoba-critic.md` (both exist).

**r47 must do one of two things and say which:** (a) report `discernment: improved` (narrow) with
the spot-check pointer, closing r46's condition; or (b) report `unchanged` with an explicit
"pending" that names what is still missing. Leaving the trend verdict silent or re-asserting
"pending" without acknowledging the 3/3 agreement would contradict an on-record promise.

**But do not over-claim.** `LEARNING.md:44-47` requires the spot-check to sample **that round's**
gate decisions — "Each round a non-author … spot-checks a sample of that round's gate decisions,
**at least one admit and one reject**, and records `agree`/`disagree` with a reason in the round's
lesson" — and "A subagent the lane dispatched is still the lane." The r46 spot-check discharges
*r46's* condition; it does **not** automatically discharge r47's own round requirement. If r47 has
no fresh non-author spot-check of its own gate decisions recorded in `corpus/lessons/round-47.md`,
the honest r47 verdict is `unchanged` (pending) — while still recording that r46's condition is now
met. Both statements can and must coexist in the report.

**Trend-vocabulary check for the other two verdicts** (`LEARNING.md:33-35`, the table):
- `expansion` improves on "net new admitted entries on uncovered ground", "frontier areas entered",
  "new kinds of source", **or "a capability admitted to `SCORECARD.md`"**; r46 read a registry row
  as *not* expansion under contract rule 4 (`.ufo/reports/round-46/kotoba.md:135`). If r47 adds a
  capability row to the SCORECARD capabilities table, `expansion: improved` is then the correct
  verdict by the letter of `LEARNING.md:33` — and the report must say so explicitly rather than
  repeating r46's "registry rows are not expansion" reflex.
- `quality` improves when "a weaker entry is superseded by a stronger one, **or stale entries
  re-verify**". r47's C1 re-derives and re-pins the substrate — if that re-derivation is recorded
  as a re-verified `corpus/knowledge/` entry (with `verified-at`/`recheck` updated and logged
  old→new, per `CORPUS.md` §SOURCES rule 2), `quality: improved` is defensible; if r47 only
  re-pins a verifier constant with no knowledge entry touched, r46's precedent
  (`.ufo/reports/round-46/kotoba.md:136`: "not re-derived, so it is no longer left stale but it is
  not stronger either") makes `unchanged` the honest verdict. The report must pick one and cite the
  entry it refers to.

### P2 — L0 question 1 (AXES.md "lowest non-retired axis") was never filed

`.ufo/reports/round-46/kotoba.md:141` asks whether the "lowest non-retired axis" range covers
advisory axes, and states the r47 consequence: "r47's C1 is freshness, so it meets both readings."

**Finding (operability): the question was never routed.** `grep -c 'round-46' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`
→ `0`, exit 1. The file holds kotoba entries for rounds 1, 6, 9, 10, 13, 16 and 22 only. So the
r46 report's "## L0 questions" section (`:139-142`) is the *only* copy of both questions; the
prompt's side channel (`kotoba-round-47.md` §5) was not exercised.

**r47 must** (a) state the disposition of each r46 question in the report, and (b) either file the
still-open one to `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` in the
`<lane> | round-<N> | <question>` form, or say in the report why it does not need an answer.
Question 1 is materially answered by construction — r47's C1 is freshness (8.0), which is the
lowest under both readings, and the r47 plan (`plans/round-47.md`, "C1 — freshness (lowest
non-retired axis, 8.0; tie with adjacency)") matches. The report should say that the r46 question
is discharged *by construction*, not left silently open.

### P3 — L0 question 2 (append-only LOG citation going dead) is answered by C3

`.ufo/reports/round-46/kotoba.md:142` asks: "Can a lane amend an append-only LOG citation that later
goes dead (`LOG.md:2111` → never-committed runner)? The checklist gate stays red on it forever.
Options: a gate erratum ledger, or accepting it as permanent." The r47 plan's C3 takes the
"gate erratum ledger" option ("pinned, fail-closed erratum registry for recorded absences").

**Verified at BASE (the exact failure r47 must key on):** in the canonical-layout clone,
`python3 -B verifiers/verify_skill_checklist.py --json` → **exit 1, 9 PASS / 1 FAIL**, the single
failure being

```
governance.citation_resolves FAIL | LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py'
does not resolve from <repo>; 9 quoted meta-finding(s), 3 schematic token(s) excluded
```

and `LOG.md:2111` itself records the absence ("…each exited 2 because the referenced runners are
absent. The prefixed V10 evidence scripts and R45 result JSON exist; the R41/R45 draft paths listed
in U1.md do not."). The plan's framing is therefore exact.

**r47 must** (a) report the disposition ("option chosen: pinned fail-closed erratum ledger"),
(b) show the registry is *pinned* (a fixed file:line → recorded-absence pair, not a pattern), and
(c) show it is *fail-closed* with a control arm: a **different** dead governance citation must
still FAIL after the registry lands. Without the control arm the change is a blanket exemption
and violates the lane's own Q05/Q18 (a fix ships a control arm from every input class the
instrument promises to tolerate) and re-opens r46's M17 class ("a fix silently narrows accepted
input"). This is the single highest-value check r47 can put on its own C3.

*(Cross-check, peer-reported, not independently reproduced by me: seat
`MoriR22R.ConnProvinceFrontier-9` states it executed the control arm in a lane-faithful scratch —
appending a line carrying `` `.ufo/reports/round-46/kotoba.md` `` produced a second failure at the
appended line, and restoring returned exactly `{LOG.md:2111}` — and records the merged-LOG
invariant: the gate's subject set is collected across the whole file, so the check must be run on
the merged LOG.md with the failure set pinned to exactly `{LOG.md:2111}`, immediately before C3's
re-measurement. The integrator must re-run that check on the merged bytes.)*

### P4 — seven carried residuals, each needs a why-not line

The r47 plan's "Not claimed (named)" list carries six r46 residuals. **The source list has seven.**
`corpus/lessons/round-46-verifier-spotcheck.md:17` ends with:

> Open residuals (carried): mirror-map-removed input passes; row with no verdict, NaN and
> case-variant keys pass; mismatched row-level `kind` passes; payload can mark committed rows out
> of scope; the printed C1 counting command exits 2 as written; **SKILL.md's own description carries
> `<skills>` (its new Q08 forbids it)**.

The seventh (the `<skills>` token) is exactly r47's C2 subject, so it is **closed by C2, not
omitted**. The r47 report's why-not/why-closed list must therefore account for **seven** items,
with the seventh marked closed-by-C2:

1. mirror-map-removed input passes (r46 report `:72`, reviewer HIGH-1);
2. a row with no `verdict` reads PASS (`:73`, MED-1);
3. `NaN` passes (`:74`, critic P2);
4. case-variant shadow keys pass (`:74`, critic P3);
5. mismatched row-level `kind` passes (`:89`, critic P5);
6. payload can mark committed rows out of scope (`:89`, reviewer HIGH-2, r39 design);
7. the printed C1 counting command exits 2 as written (`:48`, see D1 below) — and the
   `<skills>`/Q08 item, which C2 closes.

**Recommendation for the report shape:** give each item a one-line "why-not / why-closed" with a
pointer, as the r47 plan already promises ("each gets a why-not line in the report"). r46's own
report did this well at `:83-95` — that part of the shape is worth copying verbatim in style.

### P5 — evidence bloat (M15/Q11) is carried and still open

`.ufo/reports/round-46/kotoba.md:149`: "**Evidence bloat** (M15/Q11) carried: `.ufo/round-46/`
stays 52 MB / 8050+ tracked files. This round added 1.4 MB. Pruning was not done (never delete
knowledge without an operator ruling)."

`corpus/QUALITY.md:22` (Q11): "An evidence bundle is sized to the claims it serves; only cited
inputs and counting bundles land." r47 adds a new wave tree under `.ufo/waves/round-47/`. The r47
report must state the new evidence size/footprint and either justify it against Q11 or record the
Q11 debt as carried. The r46 report's "Landed changes" table already carries a per-change evidence
pointer, which is the right place. (This seat's own lane bound — "never copy strings dumps or
binaries into the repo (Q11 evidence bloat)" — is the same rule; the frozen substrate snapshot at
`/fast/scratch/kotoba-r47/shared/` must stay there.)

### P6 — the r46 measurement harness is dead as written

`.ufo/reports/round-46/kotoba.md:150`: "**Harness.** The tower worktree location breaks `../`
citations; measure in a canonical-layout clone (`meas-tree.sh`)."

That harness is `.ufo/round-46/evidence/w2/gates/meas-tree.sh`, and it is **hard-wired to r46's
paths**:

- `:7` `FLEET=/home/vgpnk/Projects/shokunin`
- `:8` `WT=$FLEET/.tower/worktrees/kaika/kotoba-shokunin` → **does not exist** at BASE
  (`ls -d …` → exit 2, "No such file or directory")
- `:10` `D=/tmp/kotoba-r46-meas/$C` → r46-namespaced output path.

**Measured consequence (the number r47 must not misquote).** The checklist gate's `../` citations
resolve only from a canonical layout, so the same BASE commit yields different gate counts
depending on where it is run:

| Layout | Command | Result |
|---|---|---|
| scratch clone at `/fast/scratch/kotoba-r47/RevPriorRoundReport/lane` | `python3 -B verifiers/verify_skill_checklist.py --json` | exit 1, **7 PASS / 3 FAIL** — `trigger.name_directory` FAIL ("name 'kotoba-shokunin' != directory 'lane'"), `trigger.citation_resolves` FAIL (`../.ufo/reports/round-7/kotoba.md` does not resolve), `governance.citation_resolves` FAIL |
| canonical-layout clone (parent symlinks the fleet root) | same command | exit 1, **9 PASS / 1 FAIL** — only `governance.citation_resolves` (LOG.md:2111) |

The r47 "before" figures in `.ufo/waves/round-47/before/SUMMARY.md` ("checklist --json: exit=1
9 PASS/1 FAIL governance.citation_resolves LOG.md:2111") are the **canonical-layout** numbers, and
I reproduced them exactly. **r47's report must state the layout its numbers were measured in**,
or a reader who re-runs in a plain clone will see 3 failures and call the after-state a
regression. r47 either re-points `meas-tree.sh` at the jj-colocated lane
(`/home/vgpnk/Projects/shokunin/kotoba-shokunin`) or ships its own canonical-layout harness, and
says so with the path.

### P7 — report location: the lane copy convention and a live governance-gate trap

`.ufo/reports/round-46/kotoba.md:148`: "**Report location.** Lane reports for rounds 20–45 live
only in the lane repo. Bare `.ufo/reports/round-45/kotoba.md` pointers resolve against the fleet
root and read dead; the lesson now uses host-absolute paths."

Verified: the lane repo has `.ufo/reports/` for rounds 20–45 (`ls .ufo/reports/ | tail` →
`round-20 … round-45`; **no `round-46`**), and `git ls-files .ufo/reports/` is tracked.

**Trap I reproduced (this one can make C3's green gate red again).** `GOVERNANCE_FILES` is
`("LOG.md", "SCORECARD.md")` (`verifiers/verify_skill_checklist.py:348`) and `CITATION_ROOTS`
includes `.ufo/` (`:347`); a backticked repo-rooted token in either file is a governance subject
(`:1454-1500`, resolution predicate `:1295-1318`). I appended one probe line to the scratch
clone's LOG.md:

```
- probe: round-47 report path token `.ufo/reports/round-46/kotoba.md` cited for the test.
```

Result — a **second** governance failure appeared:

```
governance.citation_resolves FAIL | LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does
not resolve …; LOG.md:2317: '.ufo/reports/round-46/kotoba.md' does not resolve …
```

(probe reverted afterwards with `git checkout -- LOG.md` in the scratch clone only.)

**r47 must** either (a) copy the round-47 report into the lane repo at
`.ufo/reports/round-47/kotoba.md` — restoring the rounds-20–45 lane convention — before writing
any backticked report pointer, or (b) use a host-absolute path (as the r46 lesson now does) and
write no repo-rooted report token into lane LOG.md/SCORECARD.md. What r47 must **not** do is
widen the C3 erratum registry to cover report paths: that would be a blanket exemption and would
break the fail-closed property P3 demands.

*(Cross-check, peer-reported, not independently reproduced by me: seat
`MoriR22R.ConnProvinceFrontier-9` states that its appended LOG section contains no `.ufo` token
at all — checked with the verifier's own `citation_subjects` — so the failure set stays exactly
`LOG.md:2111`, and that it adopted the P7 repro and the host-absolute rule in its §7.8. It also
states its prototype after the pin-path fix measured exit 1, 4 PASS / 3 FAIL on surfaces, so
`7/7` is written nowhere as observed. Both claims are the seat's own; the integrator must still
check the merged bytes.)*

### P8 — fleet-root ledger clobber and fleet-root strays are carried

`.ufo/reports/round-46/kotoba.md:146-147`:
- "**Fleet-root strays.** Through the broken-`cd` hazard, the reviewer seat
  `W2RoundKotoba.R46Reviewer-2` wrote 28 files into the fleet root … reported to Main and the lane
  did not touch them; at L1 check time they appeared to be already cleaned."
- "**Root ledger clobber.** The fleet-root `LOG.md`/`SCORECARD.md` still hold kotoba bytes.
  W2RoundProtocol attributes them to kotoba commit `b7470d7`, not `c8e233d`."

`corpus/QUALITY.md:28` (Q17): "Fleet-root LOG/SCORECARD identity names the fleet/protocol lane,
not a child lane; report it, never edit it from here." r47 must re-check both at round end and
report the state; the wave seats in r47 are dispatched from the fleet root, so the same broken-`cd`
hazard applies to r47's seats. The r47 prompt (§6) already insists on absolute seat paths; the
report should state whether any strays appeared.

### P9 — push disposition must be stated

r46's report opening paragraph (`:3`) records the precedence it applied: "the standing operator
rule 'No push' and PROTOCOL.md § Invariants (operator-gated artifacts are committed, not pushed)
override MISSION.md § Round end's commit-then-push, so nothing was pushed." The r47 prompt §5 says
"commit (`round-47`) inside your lane repo, then push. Also commit and push the report on the
fleet repo." r47's report must state which rule it applied and why — the same precedence sentence
is the precedent — rather than silently pushing or silently not pushing.

### P10 — the r47 plan's own "Before" values are reproducible; two plan gaps are not covered

Reproduced at BASE in the canonical-layout clone (all commands listed in §4):
`verify_surfaces.py --json` → exit 2 (opencode binary not found);
`check_substrate_pins.py` → exit 2, DRIFT 3/3;
`verify_skill_checklist.py --json` → exit 1, 9 PASS / 1 FAIL;
`verify_corpus_integrity.py --json` → exit 1, DRIFT `corpus.index.tracked_files` 59 ≠ 58 and
`corpus.index.unindexed` = 1, `unindexed_detail: ["corpus/lessons/round-46-verifier-spotcheck.md"]`;
`verify_corpus_independent.py --json` → exit 1, DRIFT unindexed.

**Gap 1 (the plan does not name it): the corpus baseline re-record.** The "0 DRIFT" after-target
is unreachable without re-recording `verifiers/corpus-baseline.json` — and r47 adds
`corpus/lessons/round-47.md` (prompt §2b.3), so `tracked_files` moves **twice** (59 → 60 for
`round-46-verifier-spotcheck.md` being indexed, and again for the new `round-47.md`), with
`expect: 58` today (`verifiers/corpus-baseline.json`, `checks.corpus.index.tracked_files.expect`).
r46 did exactly this and logged it (`r46 report:37` — "corpus-baseline.json re-record 55→58 /
38→40 / 27→29 (`notes.round46_landing`)"). r47's report must list the re-record as a landed
change tied to a LOG entry, and must state that a baseline re-record is a **measurement-baseline
change, not a score move** (Q03/Q13) — otherwise a reader sees a "green" drift gate and assumes
a real improvement.

**Gap 2 (the plan does not name it): the stale frontier rows still read "omp 18.12.3".** The two
frontier surfaces the r47 C1 advances still name the pre-drift substrate:
- `PROVINCE.md:21` — "Loader-rule freshness: the omp **18.12.3** substrate drift (surfaces 5/7, pins 1/3) …"
- `corpus/README.md:74` — "Loader-rule freshness | omp **18.12.3** drift leaves surfaces 5/7 and pins 1/3; the frontmatter `description` XML-token rule is unchecked by the lane's own gate | re-derive then re-pin; add the tag rule with a discriminating fixture"

The omp binary is now **18.12.5** (sha256 `fdbc8136…`, per `.ufo/waves/round-47/before/SUMMARY.md`
and `check_substrate_pins.py` output: "expect=9513ef9f… got=fdbc8136…"). After r47 lands, the
frontier row still claiming 18.12.3 is a **stale record of the very drift r47 closed**, and the
prompt §4 requires the "Sources & frontier" section to report "frontier rows advanced". r47 must
update both rows (or state why not) and report the row's before→after text.

### P11 — C1's after-value must be the observed value, not the plan's target

The r47 plan states C1's after-target as "surfaces 7/7 exit 0 and pins 3/3 exit 0 at the default
resolution". The before-summary records the surfaces half as **4 PASS / 3 FAIL** against the
opencode 1.19.3 binary (`literal_present`, `no_uncovered_class` vacuity 0/8, `opencode_extract`
OC-1/OC-4/OC-6), i.e. the three failing checks are the re-derivation work itself, not a defect
someone else can close. Peer seat `MoriR22R.ConnProvinceFrontier-9` reports (in-session, not
independently reproduced by me): pins **3/3 PASS at default resolution** with the npx-cache
1.19.3 ELF, surfaces still **4 PASS / 3 FAIL**, and it deliberately writes `<PINS_EXIT>` /
`<SURFACES_EXIT>` placeholders in its LOG lines so the 7/7 value is not written before it is
observed.

**r47 must** report the measured exit codes, not the planned ones. If the re-derivation lands
only 4 PASS / 3 FAIL on surfaces, the honest C1 verdict is `improved-bounded` (pins closed,
surfaces classes not yet re-derived) and the report must say so with the per-class sweep — the
plan's own words: "every class that no longer exists re-verdicted with its sweep, never silently
dropped (Q09, Q14)". Writing "7/7" from the plan is the r46 M18 class ("a seat reports a run
result it did not observe").

### P12 — `verifiers/baseline.json` is a shared file: the C1 re-pin must not disturb the harness-claims gate

The substrate pins and the harness-claims expectations live in **one** file. `verifiers/baseline.json`
has three top-level keys (`as_of`, `host`, `measured_against`, `checks`, `notes`):

- `measured_against` — the pins: `omp_binary_sha256`, `omp_binary_mtime`, `opencode_binary_sha256`,
  plus the documentary lineage keys `omp_round21_note`, `omp_round44_note`, `command`, `round18_move`;
- `checks` — **12 expected-value rows** (`omp.elf.template_sha256`, `omp.elf.template_bytes`,
  `omp.db.rows`, `omp.db.rows_wellformed`, `omp.offered.skills`, `omp.offered.dangling`,
  `omp.cache.keys_reproduced`, `omp.cache.misses`, `omp.descriptions.over_cliff`,
  `omp.names.mismatches`, `omp.descriptions.missing`, `omp.descriptions.unmodelled`);
- `notes` — per-check documentary notes.

`verifiers/verify_harness_claims.py:57` loads that file and `:569` reads
`baseline["checks"].get(cid, {}).get("expect")` — so the `checks` block *is* the harness-claims
gate's expected value. That gate is the one the r47 plan lists as **not claimed**: "verify_harness_claims.py
21/28 at BASE: three host skills appeared (create-toolset, unreal-mcp, unreal-skill); cache rows absent
for them." I reproduced it at BASE in the canonical-layout clone: `python3 -B verifiers/verify_harness_claims.py --json`
→ **exit 1**, with `catalogue_missing_names: ['create-toolset','unreal-mcp','unreal-skill']`,
`keys_reproduced: 7`, `cache_misses: 3`, `offered_skills: 10`, `db_rows: 17`.

**r47 must** treat the re-pin as a surgical edit to `measured_against` only, and must say so in the
report:
1. update the pin values only (omp → 18.12.5 sha `fdbc8136…` + the observed mtime ns; opencode →
   1.19.3 sha `179ca421…`; and the new `opencode_launcher_binary_sha256` that
   `.ufo/waves/round-47/build/RevPinsContract.patch` adds to the guard);
2. **append** a new note key (e.g. `omp_round47_note`) and keep `omp_round21_note`,
   `omp_round44_note`, `round18_move` — the lineage notes are the documentary record of the
   previous re-pins, and the r44 note already carries that lineage ("Re-pinned at 2026-10-19T18:09:38Z …");
3. **not touch `checks`** — a whole-file rewrite that re-serializes `checks` would silently move the
   harness-claims expectations and change the out-of-scope 21/28 gate (r46's M17 class, and a harm
   under the round's "no axis harmed" battery);
4. refresh `as_of`.

**No-harm arm for the report:** after the re-pin, `verify_harness_claims.py` must still read the
same 21/28 with the same three named misses (not 28/28 and not a different count), and
`check_substrate_pins.py` must report 4/4 (the added launcher pin) rather than 3/3. Note that
`RevPinsContract.patch` itself touches only `verifiers/check_substrate_pins.py` — the value re-pin in
`verifiers/baseline.json` is a separate edit by a separate seat, which is exactly why the two-writer
bound matters here.

---

## 3. Defects found in the r46 report itself (the pattern r47 must not repeat)

### D1 — the r46 C1 counting command exits 2 as written (no measurement at all)

`.ufo/reports/round-46/kotoba.md:48` prints:

```
Counting command: `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py`
```

Run verbatim at BASE in the scratch clone:

```
$ PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py
usage: runner.py [-h] --worktree WORKTREE [--scratch SCRATCH]
                 --comparator COMPARATOR --source {frozen,committed,worktree}
                 --arm {planted-relative,absolute-control}
                 [--committed-source COMMITTED_SOURCE]
runner.py: error: the following arguments are required: --worktree, --comparator, --source, --arm
EXIT=2     (stdout 0 bytes)
```

`runner.py:104-110` makes all four arguments required. The exit-2 the r46 report attributes to the
planted arm (`:51`) is thus **indistinguishable from the exit-2 of the printed command itself** —
and the report's own numbers (`:50-53`) came from a fuller invocation that is not printed. This is
exactly the residual the non-author spot-check named ("the printed C1 counting command exits 2 as
written", `corpus/lessons/round-46-verifier-spotcheck.md:17`).

### D2 — the r46 C2 counting command exits 1 with a traceback as written

`.ufo/reports/round-46/kotoba.md:57` prints
`HOME=<snapshot> PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/l1-matrix/r46_l1_matrix.py`.
The `<snapshot>` placeholder is not a command, and the snapshot the report describes (`:15`,
"frozen `cp -a` snapshot of the carrier … deleted after measurement") is gone. Run with a fresh
empty HOME in the canonical-layout clone:

```
compare_refresh.CompareError: probe target carries no candidate block: /tmp/fakehome/.omp/agent/sessions
EXIT=1     (stdout 0 bytes, stderr 1308 bytes, unhandled traceback)
```

**Two of r46's three printed counting commands are therefore not re-runnable as printed.** r47's
printed commands must be copy-pasteable and must exit as the report claims at the commit named —
this is the same obligation `corpus/QUALITY.md:25` (Q14, a negative claim carries its sweep) and
`:24` (Q13, a count carries its command) impose, and the r47 plan already names the risk for C1
("with extraction rules re-derived (not copied) and every class that no longer exists re-verdicted
with its sweep, never silently dropped (Q09, Q14)").

### D3 — the r46 report's C2/C3 verdicts are honest about surviving doors, and r47 must keep that

`.ufo/reports/round-46/kotoba.md:71-75` and `:89` list the surviving same-class doors, and `:101`
states the admission honestly ("C2 and C3 verify their registered arms, but each has surviving
same-class doors … that is `improved-bounded`, not a full verify"). r47's report should use the
same vocabulary discipline: `improved` vs `improved-bounded` vs `unchanged` must match what the
arms show, and the "No axis harmed" battery (r46 `:90-99`) is the shape to copy for r47's gate
battery.

### D4 — the S003 caveat must travel with C2 (calibration)

`corpus/lessons/round-46-verifier-spotcheck.md:12` records, in the admit sample, "the 'cannot
contain XML tags' rule is **vendor-specific**, recorded as such"; `corpus/SOURCES.md:16` (S003)
says "an Anthropic-only rule the open spec lacks"; and S011 (`:24`) records that the
agentskills.io spec "has none". r47's C2 lands a lane-local gate on that rule. **r47's report must
say the gate is a lane-local convention, not a spec requirement** — otherwise r47 has turned a
vendor-specific authoring rule into a universal one and over-claimed its scope. Note the sibling
draft in this wave already moves in that direction (`.ufo/waves/round-47/build/C2SkillRewrite.md`,
patch `C2SkillRewrite.patch`: `<skills>` router → "omp skill catalogue router"), so the caveat is
cheap to state.

---

## 4. Commands run (all read-only; exit codes as observed)

| # | Command | Where | Exit | Key output |
|---|---|---|---|---|
| 1 | `git clone -q --no-hardlinks … && git -C … checkout -q --detach c61a973b2e02e1ded169703ddcb06466f4edd8bd` | `/fast/scratch/kotoba-r47/RevPriorRoundReport/lane` | 0 | HEAD `c61a973` |
| 2 | `PYTHONDONTWRITEBYTECODE=1 python3 -B .ufo/round-46/evidence/w2/c1/runner.py` | scratch clone @BASE | **2** | argparse usage error, "the following arguments are required: --worktree, --comparator, --source, --arm"; stdout 0 bytes (D1) |
| 3 | `HOME=/tmp/fakehome … python3 -B .ufo/round-46/evidence/w2/l1-matrix/r46_l1_matrix.py` | canonical-layout clone @BASE | **1** | `CompareError: probe target carries no candidate block: /tmp/fakehome/.omp/agent/sessions` (D2) |
| 4 | `python3 -B verifiers/verify_surfaces.py --json` | scratch clone @BASE | 2 | `"error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode"`, pass 0 / fail 0 |
| 5 | `python3 -B verifiers/check_substrate_pins.py` | scratch clone @BASE | 2 | `DRIFT 3/3`: omp sha expect `9513ef9f…` got `fdbc8136…`; omp mtime drift; opencode sha UNREADABLE |
| 6 | `python3 -B verifiers/verify_skill_checklist.py --json` | scratch clone (non-canonical path) @BASE | 1 | 7 PASS / 3 FAIL — `trigger.name_directory`, `trigger.citation_resolves`, `governance.citation_resolves` (path artifacts) |
| 7 | same | canonical-layout clone @BASE | 1 | **9 PASS / 1 FAIL** — only `governance.citation_resolves` LOG.md:2111 → `.ufo/round-45/drafts/v10/post-r44-hunt.py` (P6) |
| 8 | `python3 -B verifiers/verify_corpus_integrity.py --json` | canonical-layout clone @BASE | 1 | `corpus.index.tracked_files` 59 ≠ 58 DRIFT; `corpus.index.unindexed` 1 → `corpus/lessons/round-46-verifier-spotcheck.md` (P10 gap 1) |
| 9 | `python3 -B verifiers/verify_corpus_independent.py --json` | scratch clone @BASE | 1 | exit 1, DRIFT unindexed |
| 10 | probe line with backticked `.ufo/reports/round-46/kotoba.md` appended to scratch LOG.md, then checklist | canonical-layout clone | 1 | new failure `LOG.md:2317: '.ufo/reports/round-46/kotoba.md' does not resolve` (P7); reverted with `git checkout -- LOG.md` in the scratch clone only |
| 11 | `grep -c 'round-46' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` | fleet root | 1 (0 matches) | r46's two L0 questions were never filed (P2) |
| 12 | `ls -d /home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotoba-shokunin` | fleet root | 2 | path absent → `meas-tree.sh` dead as written (P6) |
| 13 | `diff <(sed -n '/^## 4\. Report contract/,/^## 5\./p' kotoba-round-4{6,7}.md)` | fleet `.ufo/prompts/` | 1 | r47 adds the Sources & frontier + Trend verdicts bullets and relaxes the marker rule for exactly those two |
| 14 | `git log --oneline -3 -- .ufo/reports/round-46/kotoba.md` | fleet root | 0 | `a746314 round-46 report (kotoba) — lane-authored, committed by integrator` |
| 15 | `for p in .ufo/round-46/scouts/B2.md corpus/knowledge/cold-run-round11.md corpus/lessons/round-8-aggregator-box3-coldrun.md PROVINCE.md .ufo/round-46/scouts/w2-connector.md; do [ -e "$p" ] …` | lane repo @BASE | 0 | all five r46 SHONEN evidence pointers resolve — r47 may carry them |
| 16 | `grep -n 'S003\|S011' corpus/SOURCES.md` | lane repo @BASE | 0 | S003 `mined`, recheck `90d`, used-by `SKILL.md`, "an Anthropic-only rule the open spec lacks"; S011 `rejected` (D4) |

No tool was installed, upgraded or removed. No `pacman` transaction was attempted (host-wide
pacman pause observed). No lane-repo file was created, modified or deleted; the only writes this
seat made are this report and its scratch clones under `/fast/scratch/kotoba-r47/RevPriorRoundReport/`.

---

## 5. What I did NOT check

- **I did not run the r47 wave, the r47 gates, or any lane-wide gate in
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.** All gate runs were in my two scratch clones;
  the lane repo was read only.
- **I did not evaluate r47's in-flight work.** I read the r47 plan (`plans/round-47.md`) and the
  before-summary (`.ufo/waves/round-47/before/SUMMARY.md`), and glanced at two sibling wave
  artifacts (`C2SkillRewrite.md`, `C2SkillRewrite.patch`) only to check the S003 vendor-specific
  caveat. I did not audit the other seats' drafts, patches or claims.
- **I did not open the S003 source.** I did not fetch `platform.claude.com/docs/...`; the
  "cannot contain XML tags" claim is reported here as the lane's recorded row text
  (`corpus/SOURCES.md:16`) and the integrator's spot-check note
  (`corpus/lessons/round-46-verifier-spotcheck.md:12`), not as a re-verified fact. r47's C2 is
  sourced on a row that must be re-opened this round (prompt §2b.1/§2b.4) — I did not perform
  that re-open.
- **I did not run the census** (`scripts/sources-census.sh validate`) — the before-summary records
  `kotoba ok exit=0` and I did not re-derive it; r47 must paste its own before/after pair.
- **I did not verify the substrate snapshot** at `/fast/scratch/kotoba-r47/shared/` (sha256
  `fdbc8136…` for omp 18.12.5, `179ca421…` for opencode 1.19.3). I read the *pinned* values from
  `check_substrate_pins.py` output and the before-summary only, and did not re-derive the omp
  loader classes or the opencode extraction rules. My P10/§1 findings concern the report shape and
  the promises, not the re-derivation itself.
- **I did not re-run `verify_surfaces.py` with the explicit opencode 1.19.3 binary** (the override
  path), so the "4 PASS / 3 FAIL" figure I cite is the before-summary's number and the peer seat's
  report (P11), not my own re-measurement. My own surface run used the default resolution and
  exited 2 on the missing binary.
- **I did not verify the fleet-root ledger-clobber attribution** (r46 `:147`, "W2RoundProtocol
  attributes them to kotoba commit `b7470d7`, not `c8e233d`"); I only confirmed that
  `grep -n 'round-46' /home/vgpnk/Projects/shokunin/LOG.md` returns nothing, which is consistent
  with the fleet-root LOG not carrying the r46 entries.
- **I did not check whether an r47 non-author spot-check already exists** beyond the BASE
  tree; the wave is live and may produce one after my read.
- **I did not verify the SHONEN marks of any round** (this seat does not write marks) and I made
  no judgement about r47's own SHONEN lines beyond the shape requirement in §1.
- **I did not check r45 and earlier rounds** for further carried promises; my scope was the r46
  report only, as assigned.
