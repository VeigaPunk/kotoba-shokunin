# Kb81S06Shonen — SHONEN box-state at base `b2842231` (round 81, w1)

Seat: Kb81S06Shonen (leaf; no subagent dispatch, no background jobs). Lane:
`/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Measured rev: `b284223105f4d106f7e8f56ed4fd296c643cda0e`
(`git rev-parse HEAD`; lane working tree clean for tracked files — `git status --porcelain` shows only
`?? .ufo/wapes`, `?? .ufo/waves/round-81/`, `?? plans/round-81.md`).

`SHONEN.md` sha256 `c42f6bff13563f39bcec3d255b78cb23fbded6bf0446e082179768725838dee8` at base, and
`git show 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93:SHONEN.md | sha256sum` is the same digest — the four box
texts are byte-identical to the r80 base's, so every drift below is **box text vs. the tree it now describes**,
not a difference between two revisions of the box.

State: **4 of 4 boxes read `[~]`; 0 `[x]`; 0 `[ ]`** (`grep -n '^- \[' SHONEN.md` → lines 5, 7, 9, 11, all
`[~]`; `grep -c '\[x\]' SHONEN.md` → 0). Promotion to shokunin is not claimed at base and this seat claims no
change to that.

All verdicts are captured by the command's own exit status (`cmd > f 2>&1; rc=$?`), per M80-1; no gate verdict
below comes from a pipeline. Receipts sit beside this file as `Kb81S06Shonen-receipt-*.txt`. No lane file was
edited; no scratch clone was needed (every read is a lane-tree read at base plus read-only `git show`).

Base identities: `SKILL.md` sha256 `ec92e5d987be10c4b00a66d11e5cf1bfe5d74bfeb675cb3cbdb4b6e21c3eed15`, **596
lines**; `PROVINCE.md` 76 lines, § order `Core` `:8`, `Frontier` `:35`, `Adjacent` `:42`; `LOG.md` 2845 lines;
`corpus/SOURCES.md` rows S230 `:171`, S231 `:172`, S248 `:189`; `verifiers/` has **63** gate-registry
conformant counters (registry receipt) and **no** `verifiers/check_sdk_allowed_tools.py` at base
(`test -e` exit 1 — the C2 counter is round-81 work, not base).

---

## Box 1 — "SKILL.md contains real decision tables, error patterns, checklists, cited sources" — `[~]`

Box text `SHONEN.md:5-6`; pointer `.ufo/round-46/scouts/B2.md:44` plus a recount sentence and a
`check_gate_registry.py --rev 80bb8921…` run.

Re-derived at base (lane root, working tree == base bytes):

| Surface | Command | Observed / exit |
|---|---|---|
| SKILL identity | `sha256sum SKILL.md; wc -l SKILL.md` | `ec92e5d9…`, **596** lines |
| Sources entries | `awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' SKILL.md \| wc -l` | **18** (exit 0) — matches the box's "18 at `c019919c`" and its "re-count this round" |
| § Sources heading | `grep -n '^## Sources' SKILL.md` | `520:` |
| Decision-table rows | `awk 'NR>=102 && NR<=108' corpus/knowledge/anatomy-and-compression.md` | header + separator + **5 data rows** ("Intent → command/route mapping" … "One conditional") — range resolves |
| Decision-table pointer | `grep -n 'Decision-table shape' SKILL.md` | **`195:`** (was `241:` at `c019919c`; `git show c019919c:SKILL.md \| sed -n '241p'` is that same sentence) |
| Anatomy rows | `awk 'NR>=128 && NR<=137' corpus/knowledge/anatomy-and-compression.md \| grep -c '^| [0-6] '` | **7** data rows `:130-136` (sections 0 Frontmatter … 6 References) |
| Checklist boxes | `grep -c '^- \[' SKILL.md` + per-section awk | **45**, split **19** Trigger-fidelity / **9** Agent-definition / **9** Dispatch-prompt / **8** Always-on |
| Checklist gate | `python3 -B verifiers/verify_skill_checklist.py` | **exit 0**, 12 PASS, 0 FAIL: `checklist.box_map_complete: evaluated 45 — 45 boxes mapped (8 executed, 4 delegated, 33 unexecuted)`; `trigger.line_budget: evaluated 596 — 596 lines within budget 600 (from box at line 288)`; `trigger.citation_resolves: evaluated 212 — 212 repo-rooted citation token(s) resolve`; `governance.citation_resolves: evaluated 1324 — … across 2 files` |
| Error-pattern arm | `grep -n -i 'anti-pattern\|error pattern' SKILL.md` | `416:## Anti-patterns`, `419:` pointer to `corpus/knowledge/fail-closed-and-anti-patterns.md` § Anti-pattern table (full), `425:` the round-50 error-pattern sentence |
| Gate registry at base | `python3 -B verifiers/check_gate_registry.py --rev b2842231…` | **exit 0**, `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` |
| Gate registry at the box's rev | `python3 -B verifiers/check_gate_registry.py --rev 80bb8921…` | **exit 0**, `gate registry rows conformant 42 of 42 lane verifiers; phantom 0` |
| Round-64 row present | `grep -n 'check_r64_routed_repairs' SKILL.md` | **`479:`** — the box's "SKILL.md carries the round-64 gate-registry row" holds |
| B2 inventory line | `awk 'NR==44' .ufo/round-46/scouts/B2.md` | the round-46 inventory the box quotes: "41 checklist items (15/9/9/8), seven anatomy-table data rows, five decision-table data rows, and 38 Sources entries"; 521 lines against the 600-line budget |

**Box state: `[~]` (unchanged).** Every surface the box names exists at base, its cited revisions still reproduce
(`80bb8921` → 42 of 42; `c019919c:SKILL.md:241` → the decision sentence), and — unlike at the r80 base — **both
live gates behind this box are green at base** (`check_gate_registry` exit 0, `verify_skill_checklist` exit 0).
What is stale is the box's own arithmetic and pointer.

**`{{TIP}}` evidence pointer (re-derive, do not copy):**
`git show {{TIP}}:SKILL.md | grep -n 'Decision-table shape'` and
`python3 -B verifiers/check_gate_registry.py --rev {{TIP}}` — the latter must print
`gate registry rows conformant N of N lane verifiers; phantom 0`, exit 0, where N is the lane's verifier count at
the tip (63 at base; 64 once the plan's C2 counter lands). Sources recount and box count:
`git show {{TIP}}:SKILL.md | awk '/^## Sources/{p=1;next} /^## /{p=0} p && /^- /' | wc -l` (18 at base) and
`git show {{TIP}}:SKILL.md | grep -c '^- \['` (45 at base).

---

## Box 2 — "At least one end-to-end domain task executed and logged in LOG.md" — `[~]`

Box text `SHONEN.md:7-8`; evidence `corpus/knowledge/cold-run-round11.md` + `LOG.md:287,294,342` at `078eec4`.

| Claim | Command | Observed / exit |
|---|---|---|
| Cold-run record | `git ls-tree -r --name-only b2842231… corpus/knowledge/ \| grep -ci cold-run` | **1** — `corpus/knowledge/cold-run-round11.md` (21056 B) |
| Non-author marker | `head -12 corpus/knowledge/cold-run-round11.md` | `**NON-AUTHOR cold run.** The runner (lane ColdRunRecord) did **not** author …`; § 4 heading `:170`, `**none found**` `:172` |
| LOG pointers at base | `grep -n 'cold-run-round11' LOG.md` | `287:`, `294:`, `342:` — all three cited lines carry the citation (LOG.md 2845 lines) |
| Commit pin | `git cat-file -e 078eec4^{commit}`; `git log -1 --format='%H %s' 078eec4` | exit 0 — `078eec4a1f6a41c64ff8806f58b46a67cd413bfc round-63 verifier spot-check (integrator, hyaku): non-author admit/reject` |
| Same lines at that rev | `git show 078eec4:LOG.md \| sed -n '287p;294p;342p'` | the same three cold-run citations, verbatim |
| Task's verifier at base | `python3 -B verifiers/verify_corpus_integrity.py` | **exit 1**; `4/9 checks pass`; DRIFTs `tracked_files 155≠154`, `unindexed 1` (`corpus/lessons/round-80-verifier-spotcheck.md`), `report_total 111≠109`, `report_dead 1` (`corpus/lessons/round-77-verifier-spotcheck.md:15` → `HEAD:.ufo/reports/round-77/kotoba.md`), `commit_unresolvable 2` (`corpus/SOURCES.md:171`, `:172`, `7bb48f213ac677f943d5c791199ed3dddf302f00`) |
| Round-76 report site (r80's cited FAIL) | `ls -la .ufo/reports/round-76/`; `test -e .ufo/reports/round-76/kotoba.md`; `grep -c '^## SHONEN'` on the target | `kotoba.md -> ../../../../.ufo/reports/round-76/kotoba.md`; `test -e` **exit 0**; target 8128 B with **1** `## SHONEN` heading — this arm is no longer red |
| Round-77 report site | `git cat-file -e HEAD:.ufo/reports/round-77/kotoba.md` (lane) | **exit 128** ("does not exist in 'HEAD'") — the lane has no `.ufo/reports/round-77/`; the fleet does: `/home/vgpnk/Projects/shokunin/.ufo/reports/round-77/kotoba.md`, 8547 B, and `git -C <fleet> cat-file -e HEAD:.ufo/reports/round-77/kotoba.md` → exit 0 |

**Box state: `[~]` (unchanged).** The criterion — a domain task executed end-to-end and logged — holds, and its
pointers resolve at base, not only at the commit they pin.

**`{{TIP}}` evidence pointer:** `git show {{TIP}}:LOG.md | grep -n 'cold-run-round11'` (287/294/342; LOG grows only
at the tail, so these pins are stable) and `git show {{TIP}}:corpus/knowledge/cold-run-round11.md | sed -n '1,6p'`
(NON-AUTHOR marker) plus `:172` (`**none found**`).

---

## Box 3 — "Instructions executable by an agent without oral context" — `[~]`

Box text `SHONEN.md:9-10`; evidence `corpus/lessons/round-8-aggregator-box3-coldrun.md` with pins `:36`, `:37`,
`:78`, `:100`.

| Pin | Observed at base |
|---|---|
| `:36` | `\| B1 \| :168-170 \| "read … the newest \`<skills>\` block …" — … the recipe names no selection rule (the verifier brute-scans all) \| not-found \|` → exact |
| `:37` | `\| B2 \| :618-620 \| \`fault_injection_corpus.sh\` sits in the runnable-verifier list with no mutating-gate warning … \| ambiguous \|` → exact |
| `:78` | `Grade impact: **none.** The verdict stays \`[~\`] on B1 + B2 — … the refusal is credited, the recipe gap stands.` → exact (this sentence is what keeps the box `[~]` with the gate counted) |
| `:100` | `## kotoba reconciliation (round 13, 2026-09-28)` — the **section heading**; the quoted "Presentational only — no verdict, count, or quotation above was changed" is at **`:102`** |
| Cold-run sweep | `git ls-tree -r --name-only b2842231… corpus/knowledge/ \| grep -i cold-run` → **only** `corpus/knowledge/cold-run-round11.md`; `wc -l` on the lesson 121 → "corpus/knowledge/ holds one cold-run record" holds |

**Box state: `[~]` (unchanged).** No fresh non-author cold run exists at base, so the box's corrected reading
(B1 stands; B2's executability confusion survives the gate count) is still the true reading.

**`{{TIP}}` evidence pointer:** `git show {{TIP}}:corpus/lessons/round-8-aggregator-box3-coldrun.md | sed -n '36p;37p;78p'`
and the quotation at `:102` (`git show {{TIP}}:… | grep -n 'Presentational only'`), plus
`git ls-tree -r --name-only {{TIP}} corpus/knowledge/ | grep -ci cold-run` (1).

---

## Box 4 — "No cross-domain bleed (PROVINCE.md still accurate)" — `[~]`

Box text `SHONEN.md:11-12`; evidence `PROVINCE.md` § Adjacent (`35:` heading, `37:` round-49 rewrite sentence at
`c019919c`), the guard
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md`,
and the round-64 STRICT_HITS 0 claim.

| Check | Command | Observed / exit |
|---|---|---|
| Heading pin | `grep -n '^## Adjacent' PROVINCE.md` | **`42:`** (box pins `35:` at `c019919c`) |
| Rewrite sentence | `grep -n 'Rewritten round 49' PROVINCE.md` | **`44:`** `. Sibling-owned ground (report, don't absorb). Rewritten round 49 from the fleet census …` |
| Superseding note | `grep -n 'Round 74 (append-only)' PROVINCE.md` | **`53:`** — the 20 rows are re-pinned at the round-74 frozen heads from `corpus/knowledge/sibling-overlap-census-round74.md`; "The earlier rows are in `git show 1e03d19:PROVINCE.md`" |
| Box's guard (round-49 census) | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round49.md --province PROVINCE.md` | **exit 1**; `rows 20 verified 20` / `province rows 20 matched 4`; 16 FAILs (rows 2,5,6,7,8,9,10,11,12,14,15,16,17,18,19 commit mismatch; row 20 `lane tsukuroi classification 'adjacent' does not match the census 'none'`) |
| Seat form (+`--skill`) | same + `--skill SKILL.md` | **exit 1**; same `matched 4`; `skill description names 9 of 9 non-none lanes`; `skill description length 1021 of 1024` |
| Current-census guard | `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md` | **exit 0**; `rows 20 verified 20` / `province rows 20 matched 20` / `skill description names 10 of 10 non-none lanes` / `length 1021 of 1024` |
| Re-pin gate at base | `check_sibling_reread.py --rev b2842231…` | **exit 0**; `sibling rows re-pinned, re-located and re-diffed at the frozen fleet heads 20 of 20`; freeze `sibling-heads-freeze.tsv` sha256 `6e6012fc800d0f8da9666a2c1ad42934c6de4c0225d97391ae72c97ecdee195d`; INFO (not counted): `none-row SKILL.md/PROVINCE.md body names kotoba … tabi (SKILL.md at 856fa9e12021)` |
| Round-64 STRICT_HITS | historical claim; no live gate re-runs it | artifacts present: `.ufo/waves/round-64/w1/ScoutSiblingOverlap.md:77` "**STRICT_HITS = 0.**"; `.ufo/waves/round-64/w2/ScoutW2SiblingVerify.md:7` agrees for all three artifacts and separately qualifies ConnSibling's literal `M95` zero-hit control. Reported as history, not as verified-at-base |

**Box state: `[~]` (unchanged).** On the substantive question — is `PROVINCE.md` still accurate? — the answer at
base is **yes for lane set, classification and commit**: the round-74 census guard and the re-pin gate are both
exit 0 at 20 of 20. What is wrong is the box's *evidence command* and its line pins.

**`{{TIP}}` evidence pointer:**
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill SKILL.md`
must print `rows 20 verified 20`, `province rows 20 matched 20`, `skill description names 10 of 10 non-none lanes`,
exit 0; and `python3 -B verifiers/check_sibling_reread.py --rev {{TIP}}` must print `… 20 of 20`, exit 0. Line
pins are not durable: § `Frontier` (`:35`) precedes § `Adjacent` (`:42`), so any PROVINCE § Frontier append shifts
the heading — re-grep, never copy.

---

## Drift register (box text vs. observed state at base)

Status is relative to the round-80 SHONEN check (`Kb80S06Shonen.md`, base `398cbe1b`).

| # | Box | Drift | Status |
|---|---|---|---|
| **R81-S06-F1** | 1 | Decision-table pointer pinned at `SKILL.md:241`; at base the sentence is at **`:195`** (was `:192` at the r80 base — the file grew 3 lines above it). `:241` is now mid-box text (“`Triggers:` list. (executed: `trigger.literal_trigger_string`)”). Re-derive after integration: the plan's C2 lands an SDK-channel sentence near `SKILL.md:164`, i.e. **above** `:195`, which pushes the pin by at least one line. | persists (moved 192→195) |
| **R81-S06-F2** | 1 | "Recount:" carries the round-46 inventory **41 checklist items (15/9/9/8)** and no current figure; base is **45 (19/9/9/8)** — the four extra boxes are all § Trigger-fidelity. Fresh on the Sources axis (18), stale on the checklist axis. | persists |
| **R81-S06-F3** | 1 | The gate evidence is a `--rev 80bb8921` run (**42 of 42**, exit 0, reproduces). At base the same command is **63 of 63, exit 0** — the r80 “60 of 62, two missing rows” red arm is gone, and the r80 checklist arm (`governance.citation_resolves` on the round-76 report) is also green (exit 0). Post-C2 the tip figure is **64 of 64** (one new counter, one new registry row), never 63 and never 62. Any r80 text saying “two missing rows / red at base” is now false. | changed → green |
| **R81-S06-F4** | 1 | **New pressure:** `SKILL.md` is **596 of 600** lines (`trigger.line_budget: evaluated 596 — 596 lines within budget 600 (from box at line 288)`). The plan's C2 adds an SDK-channel sentence plus a gate-registry row; two added physical lines leave **2** lines of headroom, and any wrapped line in either addition trips the box (`>600` fails). The description budget is separate and tighter: **1021 of 1024** chars — the SDK sentence must not touch the frontmatter description. | new |
| **R81-S06-F5** | 2 | The task's verifier is red at base: `verify_corpus_integrity.py` exit 1, `4/9 checks pass`, five DRIFT classes (`tracked 155≠154`; `unindexed 1` = `corpus/lessons/round-80-verifier-spotcheck.md`; `report_total 111≠109`; `report_dead 1`; `commit_unresolvable 2`). “Red-before → green-after” describes round 11, not the tip; the defensible sentence is “the task is on record and logged; its verifier is red at base and the C1 stack is the repair.” | persists (sites moved) |
| **R81-S06-F6** | 2 | **New:** `report_dead 1` now sits at `corpus/lessons/round-77-verifier-spotcheck.md:15` (`HEAD:.ufo/reports/round-77/kotoba.md`); the lane has no such object (`git cat-file -e` exit 128) while the **fleet** carries it (8547 B, fleet `cat-file -e HEAD:.ufo/reports/round-77/kotoba.md` exit 0). C1 R1's lane-then-fleet resolution order therefore has a real target; if R1 resolves only lane objects the class stays red. (Observation only — R1 is not this seat's claim.) | new |
| **R81-S06-F7** | 3 | The box cites the round-13 pass at `:100`; `:100` is the section heading and the quoted “Presentational only — no verdict, count, or quotation above was changed” is at **`:102`**. Near-miss, not false. | persists |
| **R81-S06-F8** | 4 | **Load-bearing:** the box's guard takes the round-49 census against a `PROVINCE.md` whose § Adjacent rows were re-pinned at round 74 (`PROVINCE.md:53`). It is red by construction: exit 1, `province rows 20 matched 4`, 16 FAILs. Adding `--skill` does not change it, and it adds a second red arm (`skill description names 9 of 9 non-none lanes`) because the round-49 census classes `tsukuroi` `none`. The resolvable pointer is the round-74 census (exit 0, 20/20, 10/10) or `check_sibling_reread.py --rev <rev>` (exit 0 at base). | persists |
| **R81-S06-F9** | 4 | The “9 lanes classed `adjacent`” reading is stale: the description names **10 of 10** non-`none` lanes (round 74 moved `tsukuroi` `none` → `adjacent`), at **1021 of 1024** chars — 3 chars of headroom, so no lane name can be appended to the description without breaking the frontmatter budget. | persists |
| **R81-S06-F10** | 4 | Line pins `35:` / `37:` → **`42:`** / **`44:`** at base. § `Frontier` (`:35`) precedes § `Adjacent` (`:42`), so a § Frontier append moves the heading; the guard, not the pin, is the durable pointer. | persists |

## Cross-cutting notes

1. **Box text is stable; the tree moved.** `SHONEN.md` is byte-identical to the r80 base's, so none of the ten
   findings is a box-text edit — they are all box text vs. current tree.
2. **Two of the four boxes carry a red *evidence command* at base, neither of them a lane defect:** box 4's guard
   argument (round-49 census) is stale by construction, and box 2's verifier is red for reasons the round-81 C1
   repair set names (`report_dead`, `commit_unresolvable`, index/baseline). Boxes 1 and 3 have no red live gate.
3. **Round-80's S06-F6 (identical hash across S230/S231) is still live at base**: `commit_unresolvable 2` at
   `corpus/SOURCES.md:171` and `:172`, both `7bb48f213ac677f943d5c791199ed3dddf302f00`. The r81 C1 R2 replaces
   the marker grammar with `verifiers/external-commits.json`; box 2's verifier arm only turns green if that
   binding resolves *both* tokens to a real third repository. Not scored here.
4. **No after-value was scored, and no C1/C2 counter was run.** The C2 counter does not exist at base
   (`test -e verifiers/check_sdk_allowed_tools.py` exit 1), and the tip battery was not run by this seat
   (~105 s heavy pass; `/home/vgpnk/Projects/shokunin/scripts/hyaku/disk-guard.sh status` showed
   `/fast/scratch/hyaku` at 27 % used / 592.2 G free).
5. **`{{TIP}}` discipline:** every pin above was verified at `b2842231`. Pins that survive r81 integration
   untouched are `corpus/knowledge/anatomy-and-compression.md:102-108` (decision rows), `:130-136` (anatomy rows),
   `corpus/lessons/round-8-aggregator-box3-coldrun.md:36,37,78` and the quotation at `:102`, and
   `LOG.md:287,294,342`. Pins that move are every `SKILL.md` line above § Gate registry (C2 inserts at ~`:164`),
   the `PROVINCE.md` § Adjacent heading if § Frontier grows, and every figure that counts verifiers/boxes/sources.
   Re-derive at the tip; do not copy.
