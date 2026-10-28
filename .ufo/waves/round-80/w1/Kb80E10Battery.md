# Seat Kb80E10Battery — C1 battery runner + C1 stack world (kotoba round 80, wave w1)

Item: write the reusable no-harm battery runner at
`.ufo/waves/round-80/build/run-battery.sh`, then build the **full C1 stack world** in
ONE scratch clone (base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`), and measure it with
the amended (E5) counter **and** with the round-72 original counter.

Everything below is measured in my own scratch clone
`/fast/scratch/hyaku/kotoba-r80/Kb80E10Battery/clone` with each command's OWN exit status
captured (`cmd > f 2>&1; rc=$?; printf 'exit=%s\n' "$rc" >> f` — never through a pipeline).
No after-value in this report is scored; the L1 owns the landed tip.

---

## 1. The runner — `.ufo/waves/round-80/build/run-battery.sh`

    run-battery.sh <rev> <repo> <out-dir> [<report-path>]

* `<repo>` is any git repo holding `<rev>` (the real lane **or** a scratch world clone) —
  the runner clones it into a **fleet-shaped** world of its own (`$S/world/<basename>` with
  every other fleet entry symlinked beside it), so a world commit that exists only in a
  clone is measurable and the gates resolve `../.ufo/...` from the repo root as they must.
* `--fleet` is passed **explicitly** to the counter (`HYAKU_FLEET`, default = the repo's
  parent). Without it a scratch world measures a different world: `Path(".").parent == Path(".")`
  (the counter's own comment, `check_tip_battery.py:730-735`).
* Receipt format per command (`<out-dir>/NN-<name>.txt`):
  line 1 `# rev=<full> cmd=<command> utc=<ISO-8601 Z>`, line 2 `# cwd=<dir>`, line 3
  `# timeout=<n>s shell=bash`, optional `# note=<why this shape>`, then the command's
  stdout+stderr byte for byte, then the last line `exit=<rc>`.
* The two `awk | wc` figures are run **without a pipeline** (awk writes a temp file, `wc`
  counts it) so their `exit=` is the command's own status (M80-1 discipline).
* Commands: 01 `--repo .` from the world lane root · 02 absolute `--repo <lane>` · 03
  `check_gate_registry.py --rev` · 04 `check_assertion_floors.py` · 05
  `verify_skill_checklist.py --json` · 06 `verify_corpus_integrity.py --json` · 07
  `verify_corpus_independent.py --json` · 08 `check_correction_sweep.py --root .` · 09 the
  fleet census (live tree, `--note=` says so) · 10-14 the SKILL.md figures · 15 optional
  `check_report_pointers.py`.
* Exit status of the runner: 0 = every command exited 0 · 1 = at least one exited non-zero
  (a red battery is a reading, not a runner failure) · 2 = usage/environment error.
* Scratch: `$HYAKU_SCRATCH/kotoba-r80-battery/run-<pid>-<rand>`, `TMPDIR` exported inside
  it, removed on exit. Read-only on the lane; every git write happens in scratch.
* Stdlib only (bash, git, python3, coreutils). No tool was installed or upgraded by this
  seat (authorised installs unused).

### 1.0 A defect my own runner had, found and fixed (measured)

My first version named the world clone after the **scratch repo's** directory
(`$S/world/clone`). That reddens `verify_skill_checklist.py`'s `trigger.name_directory`
check — the gate reads SKILL.md's `name:` against the repo's own directory and reported
`name 'kotoba-shokunin' != directory 'clone'` — **while the tip battery measured the same
gate green**, because the counter's own sandbox always names its clone `kotoba-shokunin`.
Receipts `05-skill-checklist.txt` of the first two stack runs carry exactly that spurious
FAIL; the tip-battery readings (`01`, `02`) were unaffected, since the counter builds its
own sandbox. The runner now derives the world directory name from the repo's SKILL.md
frontmatter `name:` (falling back to the repo basename), so the world's lane directory is
always the lane's own name. **Both stack runs and the base run were re-executed with the
fixed runner**; the runner's final sha256 is
`cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601`.

This is worth recording as a general hazard for the L1: any measurement harness that
clones the lane under a different directory name will manufacture a red gate that the
frozen predicate never sees.

### 1.1 Base run — the plan's base figure reproduced

    bash .ufo/waves/round-80/build/run-battery.sh \
      398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 \
      /home/vgpnk/Projects/shokunin/kotoba-shokunin \
      .ufo/waves/round-80/build/battery-base

`RUNNER EXIT=1` — 14 receipts, **7 exit 0, 7 non-zero**. Receipts
`.ufo/waves/round-80/build/battery-base/` (14 files + `index.txt`), run log
`battery-base.run.log`.

| receipt | exit | last body line |
|---|---|---|
| 01-tip-battery-dot.txt | 1 | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 1 of 6` |
| 02-tip-battery-abs.txt | 1 | same line |
| 03-gate-registry.txt | 1 | `gate registry rows conformant 60 of 62 lane verifiers; phantom 0` |
| 04-assertion-floors.txt | 1 | `FAIL checklist observed=1863 floor=1863 self_test_failures=1` |
| 05-skill-checklist.txt | 1 | `FAIL governance.citation_resolves: LOG.md:2818 '.ufo/reports/round-76/kotoba.md' does not resolve` |
| 06-corpus-integrity.txt | 1 | 6 DRIFT rows (see §3.2) |
| 07-corpus-independent.txt | 1 | `corpus.index.unindexed` + `commit_unresolvable` DRIFT |
| 08-correction-sweep.txt | 0 | `correction sweep: 0 stale block(s)` |
| 09-census.txt | 0 | `kotoba ok …/corpus/SOURCES.md` |
| 10..14 | 0 | `590 SKILL.md` · `78647 SKILL.md` · `147` · `77` · `longest=1095 line=511` |

This reproduces the plan's base receipt `.ufo/waves/round-80/receipts/tipbattery-base-dot.txt`
exactly (`guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1, both forms).

---

## 2. The C1 stack world — what it is, and its `git diff --stat`

Built in ONE scratch clone, in the plan's §C1 repair order. Two commits plus the baseline
refresh:

| component | source applied (all from `.ufo/waves/round-80/build/` unless noted) |
|---|---|
| E01 registry rows | the **r79 reviewed draft** `.ufo/waves/round-79/build/Kb79E01Registry.patch` (sha256 `c411106e…`) for the two withdrawn rows (`check_desc_craft.py`, `check_r75_routed_repairs.py`) + `Kb80S09SkillRule.patch`'s third row (`verifiers/check_allowed_tools.py`). E01's own patch was **not published** at assembly time. |
| E02 symlink | `Kb80E02Symlink.patch` (published, sha256 `3fefb536…`) — one path, mode 120000 |
| E03 coverage rows | `Kb80S08ReadmeRows.patch` (published) — 3 rows; **plus** `Kb80E03IndexBaseline.patch`'s 2 rows were compared row-for-row against mine (identical text) |
| E03 baseline refresh | the r79 script `.ufo/waves/round-79/build/refresh-corpus-baseline.py --repo <clone>` — **exit 0**, `tracked_files 144 -> 154`, `report_total 99 -> 109`, `commit_total 43 -> 46`, `post-refresh: 9/9 checks pass, exit 0` |
| E04 report-pointer fix | `Kb80E04DeadPointer.patch` (published, sha256 `d7169dd8…`) |
| E05 grammar class | **Y01's published cap-fitting candidate** `Kb80Y01-simplified.patch` (integrity + independent hunks only) — E05 never published a patch (see §4) |
| E5 amended counter | `check_tip_battery.amended.py` (E06's canonical file, sha256 `15cc1761…`) — swapped in **verbatim** in the second commit |
| C2 files | `allowed-tools-surfaces-round80.md` → `corpus/knowledge/`, `Kb80S01Lesson.md` → `corpus/lessons/round-80.md`, `check_allowed_tools.py` → `verifiers/`, `Kb80N01Sentinel-MANIFEST.proposed` → `.ufo/waves/round-79/snapshots/MANIFEST.sha256`, `Kb80S09SkillRule.patch`'s rule line, `Kb80S10Province.patch`'s `## Core` bullet |

`git diff --stat 398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93 <world tip>`:

```
 .ufo/reports/round-76/kotoba.md                    |    1 +
 .ufo/waves/round-79/snapshots/MANIFEST.sha256      |    7 +
 PROVINCE.md                                        |    1 +
 SKILL.md                                           |    5 +
 corpus/README.md                                   |    5 +
 corpus/knowledge/allowed-tools-surfaces-round80.md |  159 ++
 corpus/lessons/round-80.md                         |   60 +
 verifiers/check_allowed_tools.py                   | 2288 ++++++++++++++++++++
 verifiers/check_tip_battery.py                     |   41 +-
 verifiers/corpus-baseline.json                     |   17 +-
 verifiers/verify_corpus_independent.py             |   13 +-
 verifiers/verify_corpus_integrity.py               |   31 +-
 12 files changed, 2601 insertions(+), 27 deletions(-)
```

World tip: **`c1b007752f17f9602bfea12ec293748644364d67`** (parent `37af095` = the stack
before the counter swap). The patch is delivered as
`.ufo/waves/round-80/build/Kb80E10Battery.stack.patch` (192 520 B, sha256
`3d766ebf54891d5079955af5e6421b9cbbcf26bffb660c241c1e77325cb01330`; re-verified to apply
cleanly — `git apply --check --binary` rc=0 — on a fresh clone at the base `398cbe1…`).

---

## 3. The measurements

### 3.1 The stack world under the E5-amended counter — **6 of 6, exit 0**

World rev `c1b007752f17f9602bfea12ec293748644364d67`, counter = E06's canonical
`check_tip_battery.amended.py` (blob `1f2910078f49cd84cb0191d58ea19359b69044bf`),
verbatim in the world. Receipts:
`.ufo/waves/round-80/build/battery-stack-canonical-counter/`.

    # rev=c1b007752f17f9602bfea12ec293748644364d67 cmd=python3 -B verifiers/check_tip_battery.py --rev c1b007752f17f9602bfea12ec293748644364d67 --repo . --fleet /home/vgpnk/Projects/shokunin
    guard no-deletions PASS
    guard floors PASS
    guard instrument-size PASS
    guard instrument-pin PASS
    guard spotcheck-identity PASS
    gate verifiers/check_gate_registry.py exit 0 wall 0.4s
    gate verifiers/check_assertion_floors.py exit 0 wall 112.3s
    gate verifiers/verify_skill_checklist.py exit 0 wall 1.5s
    gate verifiers/verify_corpus_integrity.py exit 0 wall 0.2s
    gate verifiers/verify_corpus_independent.py exit 0 wall 0.6s
    gate verifiers/check_correction_sweep.py exit 0 wall 0.0s
    wall 115.7s
    fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6
    exit=0

The absolute form (`02-tip-battery-abs.txt`, `--repo <world>`) prints the same frozen line and
exits 0. The intermediate world (rev `7b89d21`, the same stack with Y01's own counter bytes
instead of E06's canonical file) reads identically — receipts
`.ufo/waves/round-80/build/battery-stack-y01-counter/` (see its `NOTE.md`: its receipt 05
carries the runner's directory-naming artifact described in §1.0, not a world defect; the
reading 01/02 is unaffected).

**Full receipt set of the canonical run (all 14 green):**

| receipt | exit | figure |
|---|---|---|
| 01-tip-battery-dot.txt | 0 | `guards 5 of 5; tip battery exit 0: 6 of 6` |
| 02-tip-battery-abs.txt | 0 | `guards 5 of 5; tip battery exit 0: 6 of 6` |
| 03-gate-registry.txt | 0 | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0` |
| 04-assertion-floors.txt | 0 | `PASS corpus_integrity observed=166 floor=164` · `PASS corpus_independent observed=106 floor=105` · 17/17 PASS |
| 05-skill-checklist.txt | 0 | 11/11 PASS (no failing check) |
| 06-corpus-integrity.txt | 0 | 9/9 classes PASS (`tracked_files 154`, `report_total 109`, `commit_total 46`, `report_dead 0`, `commit_unresolvable 0`, `commit_nonhash 0`, `unindexed 0`) |
| 07-corpus-independent.txt | 0 | 9/9 classes PASS |
| 08-correction-sweep.txt | 0 | `correction sweep: 0 stale block(s)` |
| 09-census.txt | 0 | `kotoba ok …/corpus/SOURCES.md` |
| 10..14 | 0 | `595 SKILL.md` · `81783 SKILL.md` · `151` · `81` · `longest=1373 line=517` |

(`index.txt`: `receipts=14 green=14 non-zero=0`.)

### 3.1b The L1's chosen path (option B: standalone E04 + canonical E05) — also **6 of 6, exit 0**, at *exactly* the cap

`Kb80E05GrammarFix` published its canonical class **after** my first stack world was built,
and its composed instrument blobs are **different** from the Y01 candidate's the E06 counter
was pinning:

| instrument | Y01 class (my first world) | E05 canonical (option B) |
|---|---|---|
| `verify_corpus_integrity.py` | `cc182613a4d089c41e44f11b50e03b45ce582dd8` | `68ccce1c152c915e16893a5157c9d5878df779fb` |
| `verify_corpus_independent.py` | `89f392daab3e4181db3ded7676ca0879871ef7ff` | `e887de71892ecfc6be5b3f47e362ce8a766c5c89` |

E06 then republished the amended counter with E05's composed blobs (**file sha256
`20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`** — no longer
`15cc1761…`); the freeze must record the new stream. I built the option-B world
(E01 canonical rows + S09 rule line + S10 + E02 + E03/S08 rows + **E04 + E05** + C2 files +
E06's re-pinned counter, then the baseline refresh, exit 0, `9/9 checks pass`) and measured it:

    rev afbea93b3a408f29b8145f84a3ba6a31aea2496e (parent ccf5e54 = the re-pinned counter commit)
    instruments vs the pinned base 072048fa: 22/3 + 10/3 + 28/2 = 60 added / 8 deleted  (cap 60)
    --repo .  -> fleet root …; guards 5 of 5; tip battery exit 0: 6 of 6   exit=0
    absolute  -> fleet root …; guards 5 of 5; tip battery exit 0: 6 of 6   exit=0
    registry 63 of 63 phantom 0 · floors 17/17 PASS · checklist 11/11 PASS ·
    corpus_integrity 9/9 PASS · corpus_independent 9/9 PASS · correction_sweep 0 stale
    14 receipts, 14 green, 0 non-zero

Receipts: `.ufo/waves/round-80/build/battery-stack-optionB/` (+ `.run.log`); world patch
`.ufo/waves/round-80/build/Kb80E10Battery.stackB.patch` (204 317 B, sha256
`55061e5f67487b0262c7033dc1caa360c5861bf9ebc5718771bd2e1d69b41aeb`, 12 files,
+2877/−25 vs the base).

**The cap has ZERO headroom on this path: 60 of 60 added lines.** One more added line in any
of the three instruments (`check_assertion_floors.py`, `verify_corpus_integrity.py`,
`verify_corpus_independent.py`) trips `instrument-size` by name. Both reviewed classes
therefore fit the plan's declared arithmetic, and the choice between them is a pin/stream
decision, not a cap decision — but the E06 counter's pin table must name **whichever** class
lands, and its sha256 changes when it does.

### 3.2 The stack world under the **round-72 ORIGINAL counter** — the erratum is load-bearing

Command (own exit captured; counter bytes = the lane's
`verifiers/check_tip_battery.py`, sha256 `e33b17d74f5935a43b04272baf2d88d1d4cf4f879ee9cfa48bb25f89e744bc4a`,
identical at base and at lane HEAD `c2f69d4`):

    python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_tip_battery.py \
      --rev c1b007752f17f9602bfea12ec293748644364d67 \
      --repo /fast/scratch/hyaku/kotoba-r80/Kb80E10Battery/clone \
      --fleet /home/vgpnk/Projects/shokunin

Receipt: `.ufo/waves/round-80/build/battery-stack-original-counter/01-original-counter.txt`
(+ `.cmd`). Result **exit 1**:

    measured rev c1b00775… in a fleet-shaped sandbox; base 072048fa…
    instruments added 59 / deleted 10 lines (cap 40)
    FAIL guard instrument-size: instruments gain 59 lines > 40
    FAIL guard instrument-pin: verifiers/verify_corpus_integrity.py blob cc182613a4d089c41e44f11b50e03b45ce582dd8 at c1b00775… is not a pinned blob
    FAIL guard instrument-pin: verifiers/verify_corpus_independent.py blob 89f392daab3e4181db3ded7676ca0879871ef7ff at c1b00775… is not a pinned blob
    guard no-deletions PASS / floors PASS / spotcheck-identity PASS
    gate … all six exit 0
    fleet root /home/vgpnk/Projects/shokunin; guards 3 of 5; tip battery exit 0: 6 of 6
    exit=1

**The six gate verdicts are identical in both runs.** What the erratum changes is the
counter's declared bound and pin table — not the measured gates. The old counter cannot see
the new state, so the world is not reachable under it: that is the erratum's load-bearing
role, measured, not asserted.

### 3.3 Cap arithmetic (the load-bearing constraint on E05)

The size guard diffs the six battery scripts against the counter's **pinned r72 base
`072048fa…`**, not against `398cbe1…`. Measured (`git diff --numstat 072048fa 398cbe1 -- <six scripts>`):
`22 3 verifiers/check_assertion_floors.py` and 0/0 for the other five — i.e. **22 added /
3 deleted already spent at the round-80 base, all of it in `check_assertion_floors.py`**.
E04 adds +17 on `verify_corpus_integrity.py` → 39 spent, **21 added lines left across both
corpus gates** under `LINE_CAP = 60`.

* The published candidate `Kb80S07Quality-world.patch` measures 96 + 75 = **171 added** →
  `22 + 17 + 171 = 210` → **instrument-size FAIL** under the amended cap too (it is not
  rescued by the cap bump).
* The class my world carries (Y01's published candidate) measures **10 added** on
  `verify_corpus_independent.py` and **27 added** (17 of them E04's) on
  `verify_corpus_integrity.py` → total **59 added / 10 deleted** against the pinned base:
  **one line under the cap of 60**. Any single added line in a battery script flips the
  guard by name.

### 3.4 Three facts I measured and broadcast (they re-derive the plan's §C1 text)

1. **The plan's named unresolvable tokens are not the real ones.** At `398cbe1` both corpus
   gates read `commit_unresolvable=2` at `corpus/SOURCES.md:171` and `:172`, both the hash
   `7bb48f213ac677f943d5c791199ed3dddf302f00`; `google-gemini/gemini-cli@451a02ff` and
   `zed-industries/zed@cfb894a5` are `commit_quoted_excluded` context in both gates
   (`commit_quoted_excluded=6`), never unresolvable. The real line shape is
   "resolved to \`badlogic/pi-mono\` commit \`7bb48f21…\`" — a **bare hex** with the third
   repository named as a separate backticked token, so a class keyed on in-token
   `owner/repo@<hex>` clears nothing and the plan's "(or otherwise an explicit
   third-repository citation)" clause is the load-bearing one.
2. **The plan's "the two `commit_unresolvable` tokens are `owner/repo@<hex>`" line is wrong
   in the same way the two named repositories are wrong** — see the provenance note below.
3. **A third blocker existed only in the first draft of the C2 entry** (its Limits bullet
   cited the full hex on a line whose only repo hint was the bare name `mistral-vibe`, with
   no `owner/repo` token and no owner/repo URL). The entry owner has since **rewritten the
   entry**. The copy my world carries is sha256
   `037c3b61774a0eca7fb88b062f095f54ec3ff2645898273f96cd5d24f4823531` and it carries **0**
   commit-shaped citations under the gates' own `COMMIT_RE`
   (`verify_corpus_integrity.py:151`); its only 40-hex token is the in-set lane base
   `398cbe1…`. Measured in the world: `commit_total=46`, `commit_unresolvable=0`,
   `commit_nonhash=0`. **The entry file was rewritten several times during the wave** (the
   build copy was already `caadf57d6ba02de6ffdcd5d2d8bea33f0dbe79dadc85d7d33ef075251ad1df15`
   when this report was written), so the landed bytes must be re-verified before the tip is
   scored — the copy I measured is the one named above, not "whatever is in build/ now".

### 3.5 Ordering constraint (measured, forced by the refresh script's own bytes)

`refresh-corpus-baseline.py --repo <clone>` **refuses with exit 2** while any zero-mode class
is non-zero:

    refresh-corpus-baseline: refused: zero-mode corpus.pointers.commit_unresolvable
    observed 2, not 0; fix the drift (or name the known residual with --carry) -- a
    baseline never records a zero-mode value

So the baseline can only be recorded **after** repairs 4 and 5. The working order is:
coverage rows → E04 → grammar class → refresh → commit → measure. The refresh also refuses
on a dirty tree and writes exactly one path (`verifiers/corpus-baseline.json`).

### 3.6 Two divergences from the published patches that the L1 must not inherit blindly

* **The third coverage row.** `Kb80E03IndexBaseline.patch` (published, sha256 in the build
  dir) carries **two** rows (round-79 spot-check, round-80 lessons). The world also needs a
  third row for the C2 entry (`knowledge/allowed-tools-surfaces-round80.md`), which I took
  from `Kb80S08ReadmeRows.patch`. Measured: with the entry landed and **only** E03's two
  rows present, `verify_corpus_integrity.py --json` exits 1 with
  `corpus.index.unindexed observed 1 DRIFT` and the other eight classes PASS — so E03's
  patch alone does **not** make the corpus gate green once the C2 entry lands.
  (Independently: `Kb80E02Symlink` measured the same point from the other side — S08's rows
  also promise `lessons/round-80.md`, so the rows and the lesson file must land together or
  the index reads `stale_patterns 1` + `missing_paths 1`.)
* **E01's canonical registry patch landed after my world was built.**
  `Kb80E01Registry.patch` (sha256 `263054b531334886e3d58f789bdb1e4b1a6396dc8fff2ca43e99a395dc786cdc`,
  SKILL.md only, 3 rows, 590 → 593 lines) supersedes the r79 draft rows my world used. The
  **only** difference between E01's rows and mine is the third row's pinned-values cell:
  E01's says plain `in-file`; mine (S09's) says
  `in-file SELF_SHA; `.ufo/waves/round-79/snapshots/MANIFEST.sha256``, which is why my world
  must carry that file for the **registry gate** to pass. **Verified in my world with
  E01's canonical rows substituted** (fleet-shaped tree, lane dir named `kotoba-shokunin`):
  `check_gate_registry.py --rev <world>` → `gate registry rows conformant 63 of 63 lane
  verifiers; phantom 0`, exit 0; `verify_skill_checklist.py --json` → exit 0 with **no
  failing check**; SKILL.md 593 lines (7 under the 600-line box). So the L1 may apply E01's
  patch instead of my rows; with E01's row the MANIFEST file is then required only by **C2's**
  counter (conjunct (c)), not by the registry gate. E01's own measurement — rows without the
  counter file read `PHANTOM … conformant 62 of 62; phantom 1` and the checklist's
  `trigger.citation_resolves` FAILs on the same absent file — is why the rows and the
  counter must land in **one** commit; my world does that.
* **The C2 counter bytes.** The file published at
  `.ufo/waves/round-80/build/check_allowed_tools.py` is **byte-identical to the r79 draft**
  (sha256 `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`; `ENTRY =
  "corpus/knowledge/allowed-tools-surfaces-round79.md"`; prints `backed N of 6` /
  `script-only world: M of 6`). I landed it verbatim because the registry row must name a
  file that exists, but **C2 must not be scored on those bytes** — the round-80 counter
  (E07) is not published. This is a C2 finding, not a C1 one: the C1 tip battery does not
  run `check_allowed_tools.py`; it only needs the file to exist so the registry row is not a
  phantom.
* **The MANIFEST.** `.ufo/waves/round-79/snapshots/MANIFEST.sha256` does **not** exist at
  base or at lane HEAD (there are six per-id `.manifest` files instead). I added it, using
  the sentinel's proposed content; all six of its digests were re-verified by me against the
  **committed snapshot bytes** (6/6 MATCH).

---

## 4. What is still missing / what the L1 must decide

1. **Two reviewed grammar classes exist; the L1 picked E05's (option B).** `Kb80E05GrammarFix`
   published its canonical patch *after* my first stack world was built; its composed blobs
   are `68ccce1c…` / `e887de71…`, not the Y01 candidate's `cc182613…` / `89f392da…` that the
   first E06 counter pinned. E06 republished the counter with E05's blobs (**sha256
   `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`**), and I rebuilt the
   world on option B and measured it: **6 of 6, exit 0, both forms, at exactly 60/60 added
   lines** (§3.1b). Both classes fit the plan's arithmetic; only the pin/stream decision
   separates them. If the L1 ever switches back, the pin table must be re-derived
   (`bash .ufo/waves/round-80/build/Kb80E04DeadPointer/compute-combined-blob.sh <grammar-patch>`)
   and the counter's sha256 changes with it.
2. **The freeze receipt now exists and names the exact stream my option-B reading was taken
   on** (corrected from this report's first draft, which said it was absent).
   `.ufo/waves/round-80/receipts/freeze-shas.txt` is present (5 958 B, sha256
   `a71197b5c927afe588483e197fa0e9e38505fef24b9255813d495842dc9f0a7e`), headered
   "FINAL INPUTS, before declared after-value", and it records **line 13 the shipping counter
   sha256 `20e4960126961fe1892cf8647406a4619313db25deb3550a02c0bd41e6445276`** and **lines 20-21
   the pins `68ccce1c…` / `e887de7…`** — i.e. exactly the counter bytes and instrument blobs
   of my option-B world (§3.1b). So that reading is **not** counter-provisional: it was taken
   on the named, frozen stream. (The receipt itself says the declared after-value is still
   the L1's to take; my receipt is a measurement of those frozen bytes, not the claim's
   after-value.) The surviving freeze item is **F23** — the receipt pins `build/` digests
   that are not tracked at the freeze revision, an L1 commit-hygiene item filed by
   `Kb80V01C1`, not something my measurement can discharge.
3. **Zero line headroom on option B.** 60 of 60 added lines against the pinned r72 base. Any
   single added line in `check_assertion_floors.py`, `verify_corpus_integrity.py` or
   `verify_corpus_independent.py` trips `instrument-size` by name at the integrated tip. A
   grammar class that moves its arms into a **new helper module** would escape the size guard
   but is **not** blob-pinned by `INSTRUMENT_PINS` (only the six named scripts are) — an
   unpinned transitive authority. I did not test that shape and do not claim it is safe; the
   plan's kill rule (`22 + 17 + grammar ≤ 21 = 60`) governs.
4. **A provenance residual that no class discharges.** `7bb48f21…` is **mistral-vibe's**
   commit (S231's fetch record), while `corpus/SOURCES.md:171` (the S230/pi-mono row)
   attributes it to `badlogic/pi-mono`, whose recorded fetch head was `bb65e3e4…`. A
   line-scope class labels that line external/INFO and thereby **hides** the wrong anchor
   instead of correcting it. The cell is `corpus/SOURCES.md` (out of the repair seats' write
   scope, and the round's frontier step allows only `used-by` changes in S226–S231), so it
   belongs in the round-80 lesson as an erratum line. **A green C1 must not be read as
   "the SOURCES rows are correct."**
5. **E01's own patch was never published**; I used the r79 reviewed draft for the two
   withdrawn rows. The third row (`check_allowed_tools.py`) is S09's, and its
   pinned-values cell names `.ufo/waves/round-79/snapshots/MANIFEST.sha256`, which the
   registry gate requires to **exist at the measured revision** — hence §3.6's MANIFEST
   item.

---

## 5. Per-repair attribution inside the stack (so the L1 can price each piece)

Measured on the stack (each item's own exit status in the receipts):

| repair | gates it turns green | note |
|---|---|---|
| E02 symlink (one path, mode 120000) | **two** — `verify_skill_checklist` **and** `check_assertion_floors` | one defect (the dead `LOG.md:2818` pointer) measured twice: the floors gate's checklist instrument runs the checklist's live governance arm. A symlink-only world reads **3 of 6** (E02's own receipt). |
| E01 registry rows | `check_gate_registry` | base `60 of 62`; with the three rows and the counter file present, `63 of 63`, exit 0 |
| E04 report-pointer fix | `corpus_integrity` (`report_dead 1 → 0`) | its whole observation diff is two keys; neutral on the commit class |
| E05 grammar class | `corpus_integrity` + `corpus_independent` (`commit_unresolvable 2 → 0`, its own INFO class) | the class carries the two real blockers into an INFO class; see §4.4 |
| E03 rows + baseline refresh | `corpus_integrity` + `corpus_independent` (`tracked_files`, `report_total`, `commit_total` re-recorded; `unindexed → 0`) | refresh exit 0, `9/9 checks pass` |

---

## 6. Files I wrote (all inside my scope)

* `.ufo/waves/round-80/build/run-battery.sh` — the runner (executable; final sha256
  `cddf2dd8852801206a152dec62a62d64409453a280cef82cb3a002d7636d7601`).
* `.ufo/waves/round-80/build/battery-base/` + `battery-base.run.log` — the base world's 14
  receipts + index (7 green / 7 red; both forms `1 of 6`, exit 1).
* `.ufo/waves/round-80/build/battery-stack-canonical-counter/` + `.run.log` — the stack world
  under **E06's canonical E5 counter** (14 receipts + index, **14 green / 0 red**; both forms
  `6 of 6`, exit 0).
* `.ufo/waves/round-80/build/battery-stack-y01-counter/` (+ `NOTE.md`, `run.log`) — the same
  world under Y01's counter bytes; superseded, and its receipt 05 carries the harness
  artifact of §1.0.
* `.ufo/waves/round-80/build/battery-stack-original-counter/` — the **round-72 original
  counter** against the same world (`01-original-counter.txt` with its own `exit=1` line and
  `01-original-counter.cmd`).
* `.ufo/waves/round-80/build/Kb80E10Battery.stack.patch` — the world's diff vs the base
  (12 files, +2601/−27; sha256 `3d766ebf54891d5079955af5e6421b9cbbcf26bffb660c241c1e77325cb01330`).
* `.ufo/waves/round-80/w1/Kb80E10Battery.md` — this report.

Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80E10Battery/` was removed at the end of the seat.

### 6.1 Independent corroboration (not mine, but it is on my bytes)

`Kb80E02Symlink` applied my published stack patch to a clean base-398cbe1 clone (rc=0),
re-derived the six-instrument numstat over the pinned base (22/3 + 27/4 + 10/3 = **59 added /
10 deleted**, inside the cap of 60), and measured **6 of 6 / exit 0 in both forms** with
E06's counter; it also ran the **ablation** of my repair — removing only
`.ufo/reports/round-76/kotoba.md` from my stack drops the world to **`guards 5 of 5; tip
battery exit 0: 4 of 6`, exit 1**, with `check_assertion_floors` and `verify_skill_checklist`
both red — i.e. the symlink is load-bearing for exactly two of the six gates and nothing
else in the stack substitutes for it. Its receipts:
`.ufo/waves/round-80/build/Kb80E02-crosscheck-c1-stack.txt` and the `-crosscheck-stack6of6-*`
/ `-ablation-*` files. `Kb80E14C1Worlds` scored the ten control worlds W0–W7 on the same
E06 counter (none reaches 6 of 6, so the plan's kill rule is not triggered) and its F3/F5
independently re-derive my findings (2) and (3).

VERDICT: The C1 stack reaches the frozen predicate — `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, in BOTH argument forms — on the L1's chosen option B (standalone E04 + canonical E05, world rev `afbea93`, **exactly 60/60 added lines**) measured with the counter stream the freeze receipt names (`20e4960…`, pins `68ccce1c…`/`e887de7…`; a second world on Y01's class, rev `c1b00775` at 59/60, reads the same under its own `15cc1761…` stream), while the round-72 ORIGINAL counter reads the same world as `guards 3 of 5`, exit 1 (instrument-size 59 > 40 and both new blobs unpinned) with the six gate verdicts identical, so the erratum is measurably bounds-only; three warnings for the L1: the real unresolvable pair is the bare-hex `7bb48f21…` at `SOURCES.md:171/:172` (the plan's `owner/repo@<hex>` forms are quoted context, and `:171` is a wrong-repo anchor that no classification discharges), the cap arithmetic runs against the **pinned r72 base** so option B has zero line headroom, and the freeze's `build/` digests are not tracked at the freeze revision (F23, L1 commit hygiene).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/run-battery.sh, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/battery-base/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/battery-stack-canonical-counter/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/battery-stack-optionB/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/battery-stack-y01-counter/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/battery-stack-original-counter/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E10Battery.stack.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E10Battery.stackB.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E10Battery.md
