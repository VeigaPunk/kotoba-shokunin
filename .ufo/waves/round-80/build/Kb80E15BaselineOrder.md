# Kb80E15BaselineOrder — the L1 integration-order runbook (round 80: C1 consistency + C2 depth)

Seat: `Kb80E15BaselineOrder` (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
(the LANE repo). Round base: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`. Lane tip at the time of
writing: `a481913bafeb1ec5c231fd581f13da6ae5a306dc` (`398cbe1` + `308bff9` Addendum 1 + `a481913b`
Addendum 2; only `plans/round-80.md` moved).

This document is the ORDERED recipe the L1 runs after the wave. It is not a patch and must not be
applied. Every claim below is either first-hand measured by this seat (receipts in
`.ufo/waves/round-80/build/Kb80E15BaselineOrder/`, `R1`–`R16`) or attributed to the seat that
measured it (E02, E03, E04, E06, E10, E14). Nothing here is scored: the L1 measures the after-value.

---

## 1. Ground truth the recipe depends on

| fact | value | how it was read |
|---|---|---|
| lane branch / bookmark | `master` | `jj-lane.sh state <lane>`: `branch=master local=a481913b… remote=a481913b… ahead=0 behind=0` |
| lane working copy `@` | empty, parent = the branch tip | `jj status` in the lane: `Working copy (@) : … (empty)`, `Parent commit (@-): … a481913b master` |
| lane git HEAD | detached at the branch tip | `cat .git/HEAD` = the raw sha `a481913b…` |
| lane tree | **DIRTY for the refresh script** (639 untracked entries, § 2) | `git status --porcelain --untracked-files=all` |
| the six battery instruments' guard BASE | `072048fa8e8a52c707d25f7079772fa317244eb7` (round-73 base, pinned **inside** the counter) | `verifiers/check_tip_battery.py:108` |
| the counter's own status | the lane's `verifiers/check_tip_battery.py` is still the round-72/73 bytes (`LINE_CAP = 40`, no E04/E05 pins) — **the E5 erratum is not landed yet** | read of the lane file |
| `SKILL.md` | 590 lines, budget 600 (`trigger.line_budget` box) | `wc -l SKILL.md`; `verify_skill_checklist.py` box text |
| the registry universe | `git ls-tree -z <rev> verifiers/` — **non-recursive, top level only**, `.py`/`.sh` | `verifiers/check_gate_registry.py:119-129`; 62 entries at base (R10) |

**The single most important number in this runbook:** the tip battery's `instrument-size` guard
diffs the six battery scripts against `072048fa`, **not** against `398cbe1`. Measured:
`git diff --numstat 072048fa 398cbe1 -- <six scripts>` → `22 3 verifiers/check_assertion_floors.py`,
nothing else. So the round-80 base has already spent **22 added lines** of the budget:

    22 (already spent at the base) + 17 (E04) + grammar class (≤ 21) = 60  == the amended LINE_CAP

The composed stack this seat re-ran lands at **59 added / 10 deleted** (measured, R6):
`22/3 check_assertion_floors.py + 10/3 verify_corpus_independent.py + 27/4 verify_corpus_integrity.py`.
**One line of headroom.** If the L1 lands a grammar class larger than the reviewed one, C1 stops as
an honest stop under the plan's own arithmetic — do not widen `LINE_CAP` to absorb it.

---

## 2. Pre-flight — the dirty-tree precondition (run this FIRST, it can refuse every later step)

The refresh script (§ 4) requires `git status --porcelain --untracked-files=all` to be **empty** in
the repo it is pointed at. It refuses on untracked files just as on modified ones — measured twice:

    R1: "refused: dirty tree: … commit or clean these paths first:  ?? untracked-probe.txt"  exit 2
    (the same refusal fires for a STAGED file)

Exact check the L1 runs from the lane root:

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain --untracked-files=all

**It is NOT empty today** (639 entries). Two distinct classes, both must be gone before step 7:

1. **The wave's own artifacts** — `.ufo/waves/round-80/build/`, `.ufo/waves/round-80/w1/`,
   `.ufo/waves/round-80/receipts/`, `.ufo/waves/round-80/assimilation/`, `w1.ready`,
   `w1.ready.dispatched`. The r79 precedent is that the L1 **commits** the wave evidence into the
   lane (`.ufo/waves/round-79/build/…`, `…/w1/…`, `…/receipts/…` are tracked) — so group **G6**
   commits them and that is what makes the tree clean.
2. **A stray file at the lane root: `.ufo/wapes`** (594 B, mtime 2026-10-27 20:17; content is a C2
   quote-probe transcript — "quote lies in the first-heading block (Q70)" — i.e. another seat's
   probe output written to the wrong path). It is **not** a lane artifact and should not be
   committed. `jj-lane.sh`'s path guard does not block it (only `.ufo`, `.ufo/state`,
   `.ufo/state/*`, `.ufo/watchdog.log` are blocked), so nothing else will remove it for you: the
   L1 must delete it (or move it under `round-80/build/`) before G7, or the refresh refuses forever.
   *Reported by E06 too (§ 8.5); neither seat may delete another seat's file, the L1 may.*

---

## 3. The ordered recipe — path groups and the gate after each

Commit mechanics, measured from `scripts/hyaku/jj-lane.sh` and exercised in a scratch lane:

    /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit <lane> --as kotoba -m "<msg>" -- <path>...

* lane id is `kotoba` (from jj `user.name = kotoba-shokunin`); `--as protocol` also works.
* commits are **pathspec-limited**: every changed path must sit under one of the named paths, or
  `validate_change_scope` refuses. Groups below are therefore exact.
* each commit is pushed before the helper returns; `landed <hash>` is the only citable line.
  Exit 0 = ok · 1 = failure · **3 = committed but push failed** (the commit is kept — do not re-run
  blindly, run `jj-lane.sh push <lane>`).
* the helper never rewrites history: **there is no amend anywhere in this recipe** and the push is
  fast-forward-only. The baseline's recorded `head` also names the content commit (step G7), which
  an amend would invalidate.

### G1 — corpus content, rows and sources (ONE commit)

    paths: corpus/knowledge/allowed-tools-surfaces-round80.md
           corpus/lessons/round-80.md
           corpus/README.md          # the three coverage-map rows + the § Frontier note
           corpus/SOURCES.md         # S226–S231 used-by moves + the S232+ rejection rows

**Why one commit:** the two classes are a see-saw, both zero-mode, and the refresh refuses on
either. Measured by E03 (§ wA2): rows committed without their files → `stale_patterns 2` +
`missing_paths 2`. Files tracked without rows → `unindexed 2` (E03 § wA). Only the pair is clean.
The lesson body and the entry body must be **final** here: they are corpus files, so they move
`tracked_files` / `report_total` / `commit_total`, and the baseline is recorded after them (G7).

Gate after G1 — expect the corpus gates *still red on the pointer/commit classes*, and green on the
index classes:

    python3 -B verifiers/verify_corpus_integrity.py --json      # unindexed 0, stale 0, missing 0;
                                                                # report_dead 1, commit_unresolvable 2 → exit 1
    python3 -B verifiers/verify_corpus_independent.py --json    # same shape → exit 1

Do not read that exit 1 as a regression: see § 7.1 for why the base reads 1 of 6 at all.

### G2 — the C2 counter file, alone

    paths: verifiers/check_allowed_tools.py

**Why before G3:** the registry gate's universe grows by exactly this one file (62 → 63). A SKILL.md
row naming a verifier that is not in the tree is a **PHANTOM** row, and a verifier in the tree
without a row is simply non-conformant — measured both ways:

    R11: counter file present, no row  → "conformant 60 of 63; phantom 0"   exit 1
    S09 row applied, file absent      → "conformant 60 of 62; phantom 1"   exit 1

Gate after G2: `python3 -B verifiers/check_gate_registry.py --rev <tip>` → still `60 of 63`, exit 1.
That is the expected intermediate; the next group closes it.

### G3 — SKILL.md (ONE MERGED EDIT), PROVINCE.md, and the snapshot MANIFEST

    paths: SKILL.md
           PROVINCE.md
           .ufo/waves/round-79/snapshots/MANIFEST.sha256

**Merge the registry rows by hand — do not apply two patches.** `Kb79E01Registry.patch` (the two
withdrawn rows: `check_desc_craft.py`, `check_r75_routed_repairs.py`) and `Kb80S09SkillRule.patch`
(the `check_allowed_tools.py` row + the `allowed-tools` rule line) both insert at the **same place**
(the end of the `## Gate registry` table, just before `## Sources`). Measured: either order fails —
E01-then-S09 and S09-then-E01 both `patch does not apply`, and `git apply --3way` fails too
(`SKILL.md: does not match index`). The verified merge is: apply S09, then insert E01's two row
lines verbatim before the blank line above `## Sources`. Result: **595 lines** (≤ 600 budget) and
`63 of 63; phantom 0` once G2 and MANIFEST are present (R6).

**MANIFEST.sha256 is load-bearing.** The `check_allowed_tools.py` registry row's pinned-values cell
names `.ufo/waves/round-79/snapshots/MANIFEST.sha256`. The directory holds six snapshots, six
`.fetch.json` and six per-page `.manifest` fragments — **there is no `MANIFEST.sha256`** (E03 F4,
confirmed by this seat). Measured: with the row present and that path absent the row is
non-conformant (`no pinned path … does not exist`) → `62 of 63`, exit 1. Write it from the committed
snapshot bytes (`<sha256>  <basename>` per line, six rows; E06's recipe verifies each digest against
the file before writing — reuse that block rather than re-deriving it).

Gate after G3:

    python3 -B verifiers/check_gate_registry.py --rev <tip>    # "63 of 63 lane verifiers; phantom 0"  exit 0  (R6)
    python3 -B verifiers/verify_skill_checklist.py            # exit 0
    wc -l SKILL.md                                            # ≤ 600  (measured 595)

### G4 — the two corpus-gate repairs and the E5-amended counter (ONE commit)

    paths: verifiers/verify_corpus_integrity.py     # E04's <rev>: resolver + the grammar class
           verifiers/verify_corpus_independent.py   # the grammar class
           verifiers/check_tip_battery.py           # erratum E5 (LINE_CAP 60 + the two composed pins)

**The pins are a function of these exact bytes.** The amended counter's `INSTRUMENT_PINS` must name
the blob **at the measured rev**:

    verifiers/verify_corpus_integrity.py    cc182613a4d089c41e44f11b50e03b45ce582dd8
    verifiers/verify_corpus_independent.py  89f392daab3e4181db3ded7676ca0879871ef7ff

Both were re-derived by this seat from the base bytes (R6) and match E06's published pin table. The
E04-only blob `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` is **not** the tip blob — it is E04 on the
bare base, before the grammar class — so pinning it alone fails `instrument-pin` by name (E14's W4).
The blob is order-independent (E06 measured E04-then-class and class-then-E04 → identical blob), so
the L1 may land E04 first if it prefers; the pin still holds.

Gate after G4:

    python3 -B verifiers/verify_corpus_integrity.py --self-test     # 0 failures, assertions ≥ 164
    python3 -B verifiers/verify_corpus_independent.py --self-test   # 0 failures
    python3 -B verifiers/check_tip_battery.py --self-test           # "0 failure(s) over 69 assertions"  exit 0
    python3 -B verifiers/verify_corpus_integrity.py --json          # report_dead 0, commit_unresolvable 0 → exit 0
    python3 -B verifiers/verify_corpus_independent.py --json        # exit 0

### G5 — the round-76 report symlink (name the PARENT DIRECTORY, never the symlink path)

    path: .ufo/reports/round-76        # ← the directory, not .ufo/reports/round-76/kotoba.md

**Measured trap.** `jj-lane.sh` canonicalises every named path with `realpath -m --relative-to=.`,
which **resolves the symlink**; the target is the fleet's file, so the canonical path becomes
`../.ufo/reports/round-76/kotoba.md` and the guard refuses it as an escape:

    R13: jj-lane.sh commit … -- .ufo/reports/round-76/kotoba.md
         "jj-lane: path escapes the lane root: ../.ufo/reports/round-76/kotoba.md"   exit 1

Naming the parent directory canonicalises to itself (a real directory) and works; jj records the
symlink with mode 120000:

    R14: jj-lane.sh commit … -- .ufo/reports/round-76
         tree: "120000 blob bf7c7e0c0c39a57c49224c87348afc74dca14db4  .ufo/reports/round-76/kotoba.md"

(The `exit=3` line in R14 is the *push* of a scratch fixture whose bare remote does not track the
bookmark; the commit itself landed — that is what the tree line proves. In the lane the push is
fast-forward on `master`.)

The symlink's target is the four-hop relative path recorded in `Kb80E02Symlink.patch`; **do not paste
that string backticked into tracked prose** — the governance gate caps `..` hops at 3, so a
backticked four-hop token in `LOG.md`/`SCORECARD.md`/`SKILL.md` reds `governance.citation_resolves`.
The symlink blob itself is not prose and is fine.

Gate after G5:

    python3 -B verifiers/verify_skill_checklist.py     # exit 0 — governance.citation_resolves now PASSes
    python3 -B verifiers/check_assertion_floors.py     # exit 0 — the checklist self-test's last failure is gone

### G6 — the wave evidence (this is what makes the tree clean)

    paths: .ufo/waves/round-80            # build/, w1/, receipts/, assimilation/ …
    and:   rm .ufo/wapes                  # the stray probe file, if it is still there (§ 2)

Gate after G6 — for this group the gate *is* the precondition:

    git -C <lane> status --porcelain --untracked-files=all    # must print NOTHING

### G7 — the corpus baseline: refresh, then commit the baseline ALONE

From the lane toplevel, clean tree:

    python3 -B .ufo/waves/round-79/build/refresh-corpus-baseline.py --repo .

Expected (measured, R6; and E06's recipe receipt):

    corpus.index.tracked_files    152 → 153 (the E06 recipe tree; 154 if the lesson is in)
    corpus.pointers.report_total  … → …    (whatever the final corpus bytes say — the script observes)
    corpus.pointers.commit_total  … → …
    post-refresh: 9/9 checks pass, exit 0
    independent: exit 0; exit 0
    exit=0

**No `--carry`** (§ 5). Then:

    jj-lane.sh commit <lane> --as kotoba -m "r80: refresh the corpus baseline at the C1/C2 tip" -- verifiers/corpus-baseline.json

Commit the baseline **alone** and **do not amend the content commit**: the baseline records
`measured_against.head` = the commit it was refreshed at (the G6 tip), and an amend would move that
commit out from under the recorded label. `verifiers/corpus-baseline.json` is not a corpus file, so
this commit moves none of the counts it records.

Gate after G7: both corpus gates exit 0 (9/9 and all-PASS).

### G8 — final measurement, then the report

Run § 6 at the tip. Then write `.ufo/reports/round-80/kotoba.md` into the **fleet** root
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-80/kotoba.md`; r79's report was committed in the
fleet repo as `b6f918b0`, not in the lane) and run the report-pointer gate at that report commit.

---

## 4. The refresh script — exit 0 / 2 / 3 and what the L1 does on each

Source: `.ufo/waves/round-79/build/refresh-corpus-baseline.py` (tracked in the lane; sha256
`8481be46…`, byte-identical to the r79 original — reuse it, do not edit it).

| exit | class | the script's own words (measured) | what the L1 does |
|---|---|---|---|
| **0** | written | `wrote <path> (head <sha>)` then `post-refresh: 9/9 checks pass, exit 0` + `independent: exit 0; exit 0` | commit `verifiers/corpus-baseline.json` alone (G7) |
| **2** | **refused, baseline untouched** | `dirty tree: … commit or clean these paths first` (R1) · `zero-mode corpus.index.unindexed observed 1, not 0` (R3) · `--carry corpus.index.unindexed: an index class is never carried` (R2) · `zero-mode corpus.pointers.commit_unresolvable observed 2, not 0` (R4) · `the two gates disagree on <hard class>` · `unexpected tree, missing <file>` · `not a git work tree` / `is not the work-tree toplevel` · `integrity --self-test exited N` · `a gate exited 2/3 (environment answer, not a measurement)` · `baseline is a symlink` / `has no checks object` | **fix the named cause and re-run.** The script stops at the *first* nonzero zero-mode class, so a fix unblocks the next one (R4 shows the run advancing from `report_dead` to `commit_unresolvable`). Do **not** reach for `--carry` (§ 5). |
| **3** | **internal / post-condition failure — AND THE BASELINE HAS ALREADY BEEN WRITTEN** (the write is at `:356`, the post-conditions at `:369`, `:380`, `:387` of the script) | `post-refresh: … did not emit JSON` · `drift this script does not own: <ids>` · the independent gate exited something other than 0/1 | **do not commit the file as-is.** The write precedes the post-condition, so `verifiers/corpus-baseline.json` on disk is a half-verified record: inspect it, restore it to HEAD (`jj restore` / `git checkout --`), fix the cause, re-run. A committed exit-3 baseline is a fabricated green. |

Two behaviours worth knowing before you read a refusal as a failure:

* **The two gates may disagree on a soft class and still write.** `report_dead` is soft: the r80
  base prints `gate disagreement (not recorded, expectation stays 0): corpus.pointers.report_dead
  integrity 1 vs independent 0` and continues (R3/R5). A **hard** class (`tracked_files`,
  `unindexed`, `stale_patterns`, `missing_paths`, `report_total`, `commit_total`) refuses instead.
* **`unindexed` is the one class that must be fixed, never carried.** `corpus.index.*` is refused by
  `--carry` outright (R2).

---

## 5. The `--carry` decision tree — none at the final tip

`--carry <check-id>` is a **diagnostic**, not a fix: it lets the write proceed while the expectation
**stays 0**, the residual is stamped into `measured_against.note`, and **the gate stays red**.
Measured end-to-end (R5):

    --carry report_dead --carry commit_unresolvable
      → wrote the baseline, but: "post-refresh: 7/9 checks pass, exit 1,
         drift: corpus.pointers.report_dead, corpus.pointers.commit_unresolvable"
         "independent: red (exit 1)"                                     exit=0

So a carried baseline can never reach `6 of 6` — the carried class is still a DRIFT inside the tip
battery. The tree:

    is the nonzero class a corpus.index.* id?
      YES → it can NEVER be carried (script refuses, exit 2). Write the coverage row / remove the
            stale token, commit, re-run.
      NO  → is this the FINAL pre-report tip?
              YES → do NOT carry (plan § C1 repair 3: "--carry none — every zero class must read 0
                    after repairs 4+5"). The nonzero class names a repair that has not landed:
                      report_dead            → E04 (G4)
                      commit_unresolvable    → the grammar class (G4)
                      unindexed/stale/missing→ G1 (files + rows)
                    Land the repair, re-run.
              NO  → an intermediate tip MAY carry a residual that another seat provably owns, purely
                    to unblock a downstream step — and that baseline must be re-recorded at the
                    final tip anyway (it records the wrong `head` otherwise).

---

## 6. The final-tip no-harm battery — exact commands and expected greens

Run from the lane root at the G7 tip, **one command at a time, capturing each command's own exit**
(`cmd > f 2>&1; rc=$?; echo "exit=$rc" >> f`) — never through a pipe (round-80 lesson M80-1: a
pipeline reports its last element's status; that mistake is what made every base gate read "green").

| # | command | expected reading | exit |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_tip_battery.py --rev <tip> --repo .` | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6` | 0 |
| 2 | `python3 -B verifiers/check_tip_battery.py --rev <tip> --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin` | same line as 1 | 0 |
| 3 | `python3 -B verifiers/check_gate_registry.py --rev <tip>` | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` | 0 |
| 4 | `python3 -B verifiers/check_assertion_floors.py` | 17 `PASS` rows (the checklist row included) | 0 |
| 5 | `python3 -B verifiers/verify_skill_checklist.py` | `"fail": 0` | 0 |
| 6 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 9/9 checks pass | 0 |
| 7 | `python3 -B verifiers/verify_corpus_independent.py --json` | all PASS | 0 |
| 8 | `python3 -B verifiers/check_correction_sweep.py --root .` | `correction sweep: 0 stale block(s)` | 0 |
| 9 | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | one `kotoba ok …/corpus/SOURCES.md` line | 0 (R15) |
| 10 | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --skill SKILL.md` | `rows 20 verified 20` / `skill description names 10 of 10 non-none lanes` / `skill description length 1021 of 1024` | 0 (R16) |
| 11 | `python3 -B verifiers/check_report_pointers.py --report /home/vgpnk/Projects/shokunin/.ufo/reports/round-80/kotoba.md --repo . --rev <tip> --round 80` | `report pointers resolved N of M; unresolved 0` | 0 |
| 12 | C2: `python3 -B verifiers/check_allowed_tools.py --rev <tip>` | the plan § C2 headline (`allowed-tools surfaces documented N of 6` + `generator world: M of 6`) and the tree conjuncts | 0 iff N == 6 |

**Two corrections to the plan's literal battery list, both measured:**

* **#10 — the plan's form is not runnable.** `check_sibling_census.py --skill SKILL.md` with no
  positional argument exits **2** with `usage: check_sibling_census.py CENSUS.md [--fleet DIR]
  [--province PROVINCE.md] [--skill SKILL.md]` (R16). The census file positional is required; the
  working form is the one in the table and it reads exit 0 with the three lines above.
* **#12 — verify the counter's printed headline before trusting it.** The `check_allowed_tools.py`
  in `.ufo/waves/round-80/build/` today prints `allowed-tools surfaces backed N of 6` and
  `script-only world: M of 6`, and its `ENTRY` constant is still
  `corpus/knowledge/allowed-tools-surfaces-round79.md`; its `SELF_SHA` does not match its own bytes,
  so it exits 2 with `environment error: counter drifted` (measured). Only its docstring carries the
  plan's strings. **The counter the L1 lands must (a) have `ENTRY` naming the round-80 entry,
  (b) print the plan's headline sentence, and (c) have `SELF_SHA` refilled after the last edit
  (`--print-self-sha`).** That is E07's deliverable; the L1 should verify it, not assume it.

The battery's two invocation forms are equivalent: the counter builds its own fleet-shaped sandbox,
so `--repo .` from the lane root and the absolute `--repo <lane>` measure the same world. Measured at
the round-80 base, both read `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 — the dot form is
`.ufo/waves/round-80/receipts/tipbattery-base-dot.txt` (the plan's own receipt) and this seat measured
the absolute form at the base (`R17`).

---

## 7. Traps measured this seat — do not rediscover them the hard way

**7.1 The base reads 1 of 6, not 2, and every group boundary is red on purpose.**
At `398cbe1` the six battery gates read: registry 1, floors 1, checklist 1, integrity 1,
independent 1, correction-sweep **0** → `1 of 6`. The floors gate is red because the checklist
**self-test** fails once on the live `LOG.md:2818` governance citation (this seat re-read the base
integrity/independent JSON: R8, R9). So expect intermediate groups to keep several gates red. Only
the G7 tip is judged.

**7.2 `SKILL.md` is a merge, not two patches.** E01 and S09 insert at the same table end; either
order fails. Verified merge: 595 lines, registry 63 of 63 (R6).

**7.3 The registry gate's universe is the *top level* of `verifiers/` only.** A new helper under
`verifiers/fixtures/` is not in the universe; a new file directly under `verifiers/` **is**, and it
needs its row in the same commit (R11).

**7.4 Row before file = PHANTOM; file before row = non-conformant.** Both read exit 1. Land the
counter file and its row in adjacent commits (G2 then G3) so no measured tip has either shape.

**7.5 The counter's pins name composed blobs.** Pin `cc182613…` / `89f392da…`, not `051b8c5f…`.
A `instrument-pin` failure names the blob — read the name, recompute with the published
`Kb80E04DeadPointer/compute-combined-blob.sh` (or, on the bundle that already embeds E04, apply
`Kb80Y01-simplified.patch` alone and `git hash-object` the two files). If a *different* grammar
class lands, one hex string per pin row changes and nothing else does.

**7.6 Do not edit the six pinned instruments beyond the reviewed bytes.** The anti-laundering load is
`instrument-pin`: a 30-line edit inside the 60-line cap still fails it by name (E06's W30 receipt).
A stubbed instrument fails both `instrument-size` (loses ~1473 lines) and `instrument-pin`.

**7.7 Adding a verifier does not need a floors row.** Measured (R12): with
`verifiers/check_allowed_tools.py` present the floors gate still walks its 17 registered
instruments and reports `PASS` for each. **Do not touch `verifiers/floors-registry.json` or
`verifiers/check_assertion_floors.py`** — the latter is pinned, and a registry-only floor edit makes
the gate exit 2 with `registry floor drift` (E04's B2).

**7.8 The `..`-hop cap is prose-only, but it bites.** Never backtick a four-hop path in
`LOG.md` / `SCORECARD.md` / `SKILL.md` (cap 3). The symlink's own target text is a blob, not prose.

**7.9 The worktree must be clean before G7 — including untracked files.** Measured twice (R1). If the
L1 prefers not to commit the wave evidence, run the refresh in a scratch clone at the tip and copy
`verifiers/corpus-baseline.json` back — but then the baseline's `head` label becomes
"detached measurement commit; resolvable in the measuring clone only", which is a worse record than
the lane-local one. Prefer G6 + G7 in the lane.

---

## 8. What must NOT be done

* **No amend, no history rewrite** (jj-lane.sh is fast-forward-only; the baseline's label depends on
  the content commit staying put).
* **No `--carry` at the final tip** (§ 5).
* **No narrowing after data**: if the C1 stack cannot reach 6 of 6 because a class costs more than
  the 21-line budget, C1 stops as an honest stop — do not raise `LINE_CAP` beyond the frozen 60.
* **No edits to the six pinned instruments** other than the reviewed E04/grammar/E5 bytes.
* **No edit to the corpus gate blobs after G7** — any later corpus change invalidates the recorded
  counts; re-refresh instead.
* **No `.ufo/state/`, `.ufo/watchdog.log`, `.git/`, `.jj/` commits** (jj-lane refuses them).

---

## 9. Evidence index (this seat's own receipts, in `.ufo/waves/round-80/build/Kb80E15BaselineOrder/`)

| file | what it proves |
|---|---|
| `R1-dirty-untracked.txt` | the refresh refuses on an untracked file, exit 2 |
| `R2-carry-index-class.txt` | `--carry corpus.index.*` is refused, exit 2 |
| `R3-zero-mode-unindexed.txt` | clean tree, unfixed instruments → `unindexed 1` refusal, exit 2 |
| `R4-carry-report-dead-only.txt` | carrying one class advances the refusal to the next, exit 2 |
| `R5-carry-both-zero-classes.txt` | carrying both writes the file but the gate stays red: `7/9`, exit 1 |
| `R6-landing-recipe-transcript.txt` | the composed stack: rev, counter sha256, the two blobs, `22/3+10/3+27/4`, `63 of 63` |
| `R7-tipbattery-on-recipe-tree.txt` | **`guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0** on that stack, own exit captured |
| `R8` / `R9` | the base integrity / independent `--json` documents (the 1-of-6 shape) |
| `R10-registry-base.txt` | base registry `60 of 62`, exit 1 — the two withdrawn rows are the gap |
| `R11-registry-counter-without-row.txt` | counter file without its row → `60 of 63`, exit 1 |
| `R12-floors-with-new-verifier-bareclone.txt` | a new verifier needs no floors row (checklist row is a bare-clone artefact) |
| `R13-jjlane-symlink-file-path-refused.txt` | naming the symlink path is refused: `path escapes the lane root` |
| `R14-jjlane-symlink-parent-dir-accepted.txt` | naming the parent directory lands mode `120000` |
| `R15-census-validate.txt` | the census gate form used in § 6 exits 0 |
| `R16-sibling-census-forms.txt` | the plan's literal form exits 2 (usage); the working form exits 0 |
| `R17-tipbattery-base-absolute-form.txt` | the absolute `--repo <lane>` form at the round-80 base: `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 |

Scratch (`/fast/scratch/hyaku/kotoba-r80/Kb80E15BaselineOrder`) is removed before this seat yields;
the receipts above were copied out first. Nothing in the lane tree, the lane git/jj state, the fleet
root or a sibling lane was mutated by this seat.
