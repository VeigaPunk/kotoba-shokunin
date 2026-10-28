# Kb80S06Shonen — SHONEN box-state re-derivation at base 398cbe1b

Seat: Kb80S06Shonen (leaf, no subagents). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Measured rev: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (lane base; lane HEAD `c2f69d4f7b5887c409d7c3975d6aebc2e312c406`,
`git merge-base --is-ancestor 398cbe1b HEAD` exit 0, and `git diff --stat 398cbe1b HEAD -- SHONEN.md` empty).
`SHONEN.md` sha256 `c42f6bff13563f39bcec3d255b78cb23fbded6bf0446e082179768725838dee8` at both revs — the four box
texts below are the base bytes verbatim, so every drift named here is a drift between the box text and the
tree it is supposed to describe, not a difference between two revisions of the box text.

All verdicts are captured directly (`cmd > f 2>&1; rc=$?`) per M80-1; no gate verdict in this file comes from a
pipeline. Receipts: `Kb80S06Shonen-receipt-*.txt` beside this file. No lane file was edited by this seat.

State summary: **4 of 4 boxes read `[~]`; 0 `[x]`; 0 `[ ]`** (`grep -n '^- \[' SHONEN.md` → lines 5, 7, 9, 11,
all `[~]`; `grep -c '\[x\]' SHONEN.md` → 0). Promotion to shokunin is therefore not claimed at base and this
seat claims no change to that.

---

## Box 1 — "SKILL.md contains real decision tables, error patterns, checklists, cited sources" — `[~]`

Box text at `SHONEN.md:5-6`; evidence pointer `.ufo/round-46/scouts/B2.md:44` (present, quoted below) plus a
recount sentence and a rev-pinned gate-registry run at `80bb89211841289bc802fa7b55057f0ef266d19e`.

Re-derived at `398cbe1b` (receipt `-derivation`):

| Surface | Command | Observed |
|---|---|---|
| SKILL.md identity | `git show 398cbe1b:SKILL.md \| sha256sum` ; `… \| wc -l` | `7b1263b5ccbe2ba8b6ffd5d0f4c87ffc5ab3292c9ce792aeee96de283a06464a`, **590** lines (budget 600; `verify_skill_checklist.py` agrees: `evaluated 590 — 590 lines within budget 600`) |
| Sources entries | `git show 398cbe1b:SKILL.md \| awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' \| wc -l` | **18** — matches the box's "18 at `80bb8921` (re-count this round)" and "18 at `c019919c`" |
| Decision-table rows | `git show 398cbe1b:corpus/knowledge/anatomy-and-compression.md \| sed -n '102,108p'` | header + separator + **5 data rows** ("Intent → command/route mapping", "Request classification…", "Flag → effect reference", "Ordered pipeline", "One conditional") — range resolves |
| Anatomy rows | `… \| grep -n '^\| [0-6] \|'` | **7** data rows at `:130-136` (sections 0 Frontmatter … 6 References) — "seven anatomy-table data rows" resolves |
| Checklist boxes | `git show 398cbe1b:SKILL.md \| grep -c '^- \[ \]'` | **45** — per section 19 Trigger-fidelity / 9 Agent-definition / 9 Dispatch-prompt / 8 Always-on |
| Checklist gate | `python3 -B verifiers/verify_skill_checklist.py` (lane root) | exit **1**; `PASS checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)`; single FAIL `governance.citation_resolves: LOG.md:2818: '.ufo/reports/round-76/kotoba.md' does not resolve` |
| Gate registry at base | `python3 -B verifiers/check_gate_registry.py --rev 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` (run from inside a base clone) | exit **1**; `gate registry rows conformant 60 of 62 lane verifiers; phantom 0` |
| Gate registry at the box's cited rev | `… --rev 80bb89211841289bc802fa7b55057f0ef266d19e` | exit **0**; `gate registry rows conformant 42 of 42 lane verifiers; phantom 0` |
| The two missing rows | `git show 398cbe1b:SKILL.md \| grep -n 'check_desc_craft\|check_r75_routed_repairs'` | no output, exit 1 → both registry rows are absent; the verifier names exactly those two: `verifiers/check_desc_craft.py no registry rows naming it: 0 (need 1)`, `verifiers/check_r75_routed_repairs.py no registry rows naming it: 0 (need 1)` |
| Round-64 row present | `git show 398cbe1b:SKILL.md \| grep -n 'check_r64_routed_repairs'` | `476:` — the box's "SKILL.md carries the round-64 gate-registry row" holds |
| B2 inventory line | `git show 398cbe1b:.ufo/round-46/scouts/B2.md \| sed -n '44p'` | the round-46 inventory quoted in the box: "41 checklist items (15/9/9/8), seven anatomy-table data rows, five decision-table data rows, and 38 Sources entries" |

**Box state: `[~]` (unchanged).** The surface is real on every axis the box names, and every count the box
asserts about *its own* cited revisions holds. What does not hold at the final-tip tree is the box's live gate:
`check_gate_registry` is red at base (`60 of 62`) and its `42 of 42` figure is only true at the rev it pins.

Drift to carry into the report:

- **S06-F1 (misresolved pointer, box 1).** `SKILL.md:241` is cited as the decision-table pointer. At `c019919c`
  line 241 *is* the decision-table pointer sentence, but at `398cbe1b` line 241 is a mid-sentence fragment of a
  Trigger-fidelity checklist box (`gate: "a marker-bearing but vacuous clause passes unearned…"`); the pointer
  now lives at **`SKILL.md:192`** (**{{TIP}}** re-derive: `git show {{TIP}}:SKILL.md | grep -n 'Decision-table shape'`).
  Cause: SKILL.md grew from 41 to 45 checklist boxes below that pointer, shifting every later line.
- **S06-F2 (stale inventory figure, box 1).** The box's "Recount:" sentence carries the round-46 checklist figure
  (41, split 15/9/9/8) and no current one. At base the count is **45 (19/9/9/8)** — the four new boxes are all in
  § Trigger-fidelity. This does not falsify B2 (which is explicitly the round-46 tree) but it leaves the box's own
  recount stale on the checklist axis while it is fresh on the Sources axis.
- **S06-F3 (rev-pinned gate, box 1).** The evidence is a `--rev 80bb8921…` run. That run still reproduces
  (`42 of 42`, exit 0), so the box is not false — but at the base tip the same command is `60 of 62`, exit 1,
  missing exactly `check_desc_craft.py` and `check_r75_routed_repairs.py`, i.e. two of the three SKILL.md rows the
  round-80 C1 stack adds. Post-integration the figure to assert is **63 of 63** (62 today + `check_allowed_tools.py`
  once C2's counter lands in `verifiers/`), not `62 of 62` — the box text and the report's after-value must both
  move to the new verifier count, or the "phantom 0 / all conformant" claim will be re-falsified the moment the
  new counter exists.
- **S06-F4 (cross-cut, box 1's checklist arm).** The checklist gate's single base FAIL is the missing
  `.ufo/reports/round-76/kotoba.md`: `ls -la .ufo/reports/round-76/kotoba.md` → *No such file or directory*
  (exit 2), `test -e` exit 1, while the fleet file exists
  (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-76/kotoba.md`, 8128 B, exit 0). This is the C1 symlink repair
  (`Kb79E02LogCitation.patch` line of the stack) and it is the only thing keeping this arm red — it is not a
  SKILL.md defect.

---

## Box 2 — "At least one end-to-end domain task executed and logged in LOG.md" — `[~]`

Box text at `SHONEN.md:7-8`; evidence `corpus/knowledge/cold-run-round11.md` + `LOG.md:287,294,342` at `078eec4`.

Re-derived at `398cbe1b` (receipt `-derivation`):

| Claim | Command | Observed |
|---|---|---|
| Cold-run record exists | `git ls-tree -r --name-only 398cbe1b corpus/knowledge/ \| grep -i cold-run` | `corpus/knowledge/cold-run-round11.md` — 1 file |
| LOG.md pointers resolve | `git show 398cbe1b:LOG.md \| grep -n 'cold-run-round11'` | `287:`, `294:`, `342:` — all three cited lines still carry the citation (LOG.md is 2833 lines at base) |
| The task's verifier, at base | `python3 -B verifiers/verify_corpus_integrity.py` (lane root) | exit **1**; `3/9 checks pass` |

So the box's criterion — a domain task executed end-to-end and logged — **holds**, and its pointers resolve at
the base tip, not only at the commit they pin.

Drift to carry into the report:

- **S06-F5 (freshness, box 2).** The task's own verifier is red at the base tree, so "red-before → green-after"
  describes round 11, not the tip. Six DRIFTs, each with a named site:
  `corpus.index.tracked_files` 152 vs 144; `corpus.index.unindexed` 1 (`corpus/lessons/round-79-verifier-spotcheck.md`);
  `corpus.pointers.report_total` 109 vs 99; `corpus.pointers.report_dead` 1
  (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md` — the `<rev>:` shape
  `Kb79E04DeadPointer.patch` addresses); `corpus.pointers.commit_total` 46 vs 43; `corpus.pointers.commit_unresolvable` 2
  (`corpus/SOURCES.md:171` and `:172`, both `7bb48f213ac677f943d5c791199ed3dddf302f00`).
  Any report sentence of the form "the box-2 domain task is green" is false at base; the defensible sentence is
  "the task is on record and logged; its verifier is red at base and the C1 stack is the repair".
- **S06-F6 (corpus quality, found while classifying the two unresolvable commits — see also box 4).** The two
  unresolvable commits are *external* repo pins in SOURCES.md rows S230/S231, so the new external-commit grammar
  class (C1 repair 6, Q61) will classify them **INFO** and stop counting them as unresolvable. But S231
  (`mistralai/mistral-vibe`) states "served commit `7bb48f213ac677f943d5c791199ed3dddf302f00`" — the **same hash**
  quoted verbatim for S230 (`badlogic/pi-mono`). The round-79 fetch receipt
  (`Kb79A01SkillRule-fetch-receipt.txt:18`) records for S231 only URL / HTTP 200 / bytes 77634 / sha256
  `fc48a5db…` / occurrences 1 — **no commit column**, so nothing in the receipt supports the S231 commit cell and
  the identical hash across two different repos is not credibly both. The INFO class will launder this cell. If
  the grammar repair lands without a per-row external-repo check, record the S231 commit cell as an open corpus
  defect rather than as a resolved citation.

---

## Box 3 — "Instructions executable by an agent without oral context" — `[~]`

Box text at `SHONEN.md:9-10`; evidence `corpus/lessons/round-8-aggregator-box3-coldrun.md` with line pins
`:36`, `:37`, `:78`, `:100`.

Re-derived at `398cbe1b` (receipt `-derivation`):

| Pin | Observed at base |
|---|---|
| `:36` | `| B1 | :168-170 | "read … the newest <skills> block …" — … the recipe names no selection rule (the verifier brute-scans all) | not-found |` → exact |
| `:37` | `| B2 | :618-620 | fault_injection_corpus.sh … no mutating-gate warning … | ambiguous |` → exact |
| `:78` | ends `… the refusal is credited, the recipe gap stands.` → exact; it is also the sentence that keeps the verdict `[~]` with the gate counted |
| `:100` | `## kotoba reconciliation (round 13, 2026-09-28)` — the **section heading**, not the quoted sentence |
| cold-run sweep | `git ls-tree -r --name-only 398cbe1b corpus/knowledge/ \| grep -ci cold-run` → **1** — "corpus/knowledge/ holds one cold-run record" holds (the only other cold-run-named file in the tree is `corpus/lessons/round-8-aggregator-box3-coldrun.md`, the record itself) |

**Box state: `[~]` (unchanged).** No fresh non-author cold run exists, so the box's own corrected reading —
B1 stands, B2's executability confusion survives the gate count — is still the true reading. Nothing this seat
measured closes it.

Drift to carry into the report:

- **S06-F7 (off-by-two pin, box 3).** The box says the round-13 pass `:100` was "presentational only — no
  verdict, count, or quotation above was changed". The quoted sentence is at **`:102`**; `:100` is the section
  heading. A reader following `:100` lands in the right section but not on the quotation, so the citation is
  near-miss rather than false. Fix the pin to `:102` (**{{TIP}}**: `git show {{TIP}}:corpus/lessons/round-8-aggregator-box3-coldrun.md | grep -n 'Presentational only'`).

---

## Box 4 — "No cross-domain bleed (PROVINCE.md still accurate)" — `[~]`

Box text at `SHONEN.md:11-12`; evidence `PROVINCE.md` § Adjacent with the line pins `35:` (heading) and `37:`
(round-49 rewrite sentence), the guard
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`,
and the round-64 STRICT_HITS 0 claim.

Re-derived at `398cbe1b`:

| Check | Command (cwd = base clone unless noted) | Observed |
|---|---|---|
| Heading pin | `git show 398cbe1b:PROVINCE.md \| grep -n '^## Adjacent'` | **`41:`** (was `35:` at `c019919c` — verified) |
| Rewrite sentence pin | `git show 398cbe1b:PROVINCE.md \| sed -n '43,44p'` | "Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census / `corpus/knowledge/sibling-overlap-census-round49.md` …" → the sentence is at **`:43-44`** (was `:37`) |
| Box's cited guard | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | **exit 1**; `rows 20 verified 20` / `province rows 20 matched 4`; 16 FAILs — rows 2,5,6,7,8,9,10,11,12,14,15,16,17,18,19 commit mismatches ("lane X commit A does not match the census B") and row 20 `tsukuroi classification 'adjacent' does not match the census 'none'` |
| Current-census guard | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md` | **exit 0**; `rows 20 verified 20` / `province rows 20 matched 20` |
| Re-pin gate | `check_sibling_reread.py --rev 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` | **exit 0**; `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`; freeze `sibling-heads-freeze.tsv` sha256 `6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d`; INFO (not counted): `none-row SKILL.md/PROVINCE.md body names kotoba: tabi (SKILL.md at 856fa9e12021)` |
| Description guard | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --skill SKILL.md` | **exit 0**; `skill description names 10 of 10 non-none lanes`; `skill description length 1021 of 1024` |
| Round-64 scan rows | (historical claim; no live gate re-runs it) | not re-run — reported as history, not as verified-at-base |

**Box state: `[~]` (unchanged)**, and on the substantive question the box asks — is `PROVINCE.md` still
accurate? — the answer at base is **yes for lane set, classification and commit** (round-74 census + reread,
both exit 0, 20 of 20). What is wrong is the box's *evidence command*.

Drift to carry into the report:

- **S06-F8 (stale guard argument, box 4 — the load-bearing one).** The box's guard explicitly takes the round-49
  census. That census was superseded at round 74 (`PROVINCE.md:52` append-only note: the 20 rows below are
  re-pinned at the round-74 frozen heads; "The earlier rows are in `git show 1e03d19:PROVINCE.md`"), so the cited
  command is red *by construction* — it compares round-74-pinned rows against round-49 pins. It reads
  `province rows 20 matched 4`, exit 1, not `matched 20`, exit 0. The resolvable pointer is the round-74 census
  (`corpus/knowledge/sibling-overlap-census-round74.md`) or, better, the re-pin gate
  `check_sibling_reread.py --rev <rev>`; both are green at base. This is a box-text repair (one argument), not a
  counter defect, and it must not be mistaken for lane drift.
- **S06-F9 (stale count, box 4).** "the 9 lanes classed `adjacent`" → at base the description names
  **10 of 10** non-`none` lanes: the round-74 re-read moved `tsukuroi` `none` → `adjacent` (basis kotoba). The
  description is 1021 of 1024 chars, i.e. 3 chars of headroom — any further lane-name addition breaks the
  frontmatter budget, which is worth knowing before someone appends a name.
- **S06-F10 (line pins, box 4).** Heading `35:` → `41:`, rewrite sentence `37:` → `43-44:` (both re-derived
  above). Any report that repeats the box's `:35` / `:37` pins is quoting a stale tree.

---

## Cross-cutting observations for the report's SHONEN section

1. **Two of the four boxes have a live red gate at base, and both are already in the round-80 C1 stack** —
   box 1 via `check_gate_registry` (two missing SKILL.md rows) + the checklist arm (missing round-76 symlink);
   box 4 via a stale census argument in its evidence command (green once re-pointed, no code change).
   Boxes 2 and 3 stay `[~]` on their own grounds and are not touched by C1/C2: box 2's record stands but its
   verifier is red at base; box 3 has no fresh non-author cold run.
2. **`{{TIP}}` discipline for the after-value.** Every line pin above was verified at `398cbe1b`. Round-80's own
   commits land SKILL.md § Gate registry rows (below line 192 and above § Sources), append LOG.md entries at the
   end, and may append PROVINCE.md § Adjacent; the pins that survive untouched are
   `corpus/knowledge/anatomy-and-compression.md:104-108` (decision rows), `:130-136` (anatomy rows),
   `corpus/lessons/round-8-aggregator-box3-coldrun.md:36,37,78`, and `LOG.md:287,294,342`. Re-derive, do not
   copy: `git show {{TIP}}:SKILL.md | grep -n 'Decision-table shape'`; `git show {{TIP}}:PROVINCE.md | grep -n '^## Adjacent'`;
   `git show {{TIP}}:LOG.md | grep -n 'cold-run-round11'`.
3. **Sandbox shape changes gate verdicts — do not cite a clone run for a path-sensitive arm.** Run from a
   scratch clone at `/fast/scratch/hyaku/kotoba-r80/Kb80S06Shonen/clone`, `verify_skill_checklist.py` exits 1 with
   **two** FAILs (`trigger.name_directory: name 'kotoba-shokunin' != directory 'clone'`;
   `trigger.citation_resolves: line 580: '../.ufo/reports/round-7/kotoba.md' does not resolve`). From the lane
   root it exits 1 with **one** FAIL (`governance.citation_resolves` on `LOG.md:2818`). The clone's two extra
   FAILs are artifacts of the clone's basename and non-fleet parent, not lane drift. Both runs are kept as
   receipts (`-receipt-skillchk.txt` = clone, `-receipt-skillchk-lane.txt` = lane root) so the difference is
   auditable.
4. **Not measured here, by design:** no after-value for C1/C2, no scoring of any claim, no tip-battery run (the
   base receipt `.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` is the L1's and I only read it:
   `guards 5 of 5`, `tip battery exit 0: 1 of 6`, exit 1; `check_assertion_floors` 101.0 s is the 104 s pass, and
   `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` showed `/fast/scratch/hyaku` at 27 % used /
   592.3 G free, so no heavy pass was needed by this seat).
