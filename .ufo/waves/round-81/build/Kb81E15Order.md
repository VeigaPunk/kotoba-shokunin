# Kb81E15Order — the L1 integration-order runbook (round 81: C1 consistency + C2 depth)

Seat: `Kb81E15Order` (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Round base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Written while the w1 wave was still landing;
every number below is either measured first-hand by this seat (receipts in
`.ufo/waves/round-81/build/Kb81E15Order/`) or attributed by file to the seat that measured it.

**This document is an ORDER, not a patch. Do not apply it.** `plans/round-81.md` is authoritative;
where this runbook and the plan disagree, the plan wins and the disagreement is a routed defect
against this seat.

Contents: § 1 ground truth · § 2 pre-flight · § 3 the ordered recipe G0–G7 · § 4 the refresh script's
exit codes · § 5 failure modes · § 6 the final battery · § 7 traps measured here · § 8 what changed
from the r80 runbook · § 9 evidence index · § 10 what must not be done.

---

## 1. Ground truth this recipe depends on (measured by this seat at `b2842231`)

| fact | value | how it was read |
|---|---|---|
| lane git HEAD | `b284223105f4d106f7e8f56ed4fd296c643cda0e`, **detached** | `git rev-parse HEAD`; `.git/HEAD` holds the raw sha |
| lane bookmark | `master` → `b2842231`, `ahead=0 behind=0` vs `origin/master` | `git for-each-ref`; `git rev-list --count` both ways; `jj bookmark list` |
| lane working tree at wave start | 11 untracked entries, 0 modified | `git status --porcelain --untracked-files=all` |
| the untracked classes | `plans/round-81.md`; `.ufo/wapes`; `.ufo/waves/round-81/**` | same command |
| verifiers registry universe | **63** top-level `.py`/`.sh` under `verifiers/` | `git ls-tree -z --name-only <base> verifiers/` filtered |
| base registry gate | `gate registry rows conformant 63 of 63 lane verifiers; phantom 0`, **exit 0** | `verifiers/check_gate_registry.py --rev <base>`, receipt `base-registry.txt` |
| base tip battery | `guards 5 of 5; tip battery exit 0: 4 of 6`, exit 1; `instruments added 22 / deleted 3 lines (cap 40)` | `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt` |
| base corpus classes (integrity) | `tracked_files 155≠154`, `unindexed 1`, `report_total 111≠109`, `report_dead 1`, `commit_unresolvable 2` | `verify_corpus_integrity.py --repo <base clone> --json`, receipt `base-integrity.json` |
| base corpus classes (independent) | `unindexed 1`, `commit_unresolvable 2` (`report_dead` reads 0 — soft-class disagreement) | `verify_corpus_independent.py --json`, receipt `base-independent.json` |
| base self-tests | tip battery `0 failure(s) over 69 assertions`; integrity `164 assertions`; independent `105 assertions` — all exit 0 | receipts `base-*-selftest.txt` |
| `verifiers/verify_corpus_integrity.py` base blob | `e470eaaea5ef11c582b8353c9344ddf730c1a57a` — **already one of its two `INSTRUMENT_PINS` members** | `git rev-parse <base>:<path>`; `check_tip_battery.py:125-140` |
| `verifiers/verify_corpus_independent.py` base blob | `edac0df79324ba62ee25ff10a6a4d422ef59da61` — **already a pinned member** | same |
| `verifiers/check_tip_battery.py` base blob | `a356e9d101f3021687a80e73fca284e7436976d2`, 743 lines, sha256 `e33b17d7…bc4a` | `git rev-parse`; `sha256sum` |
| instrument-size reference base | `072048fa8e8a52c707d25f7079772fa317244eb7`; spend already 22 added / 3 deleted → the repairs' headroom is `900 − 22 = 878` added lines under the frozen E6 cap (402 used today, § 2.4) | base battery summary line; `.ufo/waves/round-81/build/Kb81E05Erratum.hunk-inventory.txt` |
| `SKILL.md` | 596 lines, budget 600 (`trigger.line_budget` box at `SKILL.md:288-290`); registry table rows end at **line 518**, blank line 519, `## Sources` at **520** | `wc -l SKILL.md`; `grep -n '^## Gate registry\|^## Sources' SKILL.md` |
| `PROVINCE.md` `## Core` round-80 bullet | line 34 | `sed -n '31,36p' PROVINCE.md` |
| `corpus/README.md` coverage rows | last row (round-80 allowed-tools entry) at line 159; `## Frontier` note area ~243 | `sed -n '155,160p'`; S08 patch hunks `@@ -157,6` and `@@ -243,6` |
| `corpus/SOURCES.md` rows | S248 at 189; S249/S250 append after S250's neighbours (S05's hunk base `@@ -186,7`); S230/S231 tokens at 171-172 | `grep -n`; `sed -n '168,175p'` |
| `HEAD:.ufo/reports/round-77/kotoba.md` | **resolves in the FLEET root** (`git -C /home/vgpnk/Projects/shokunin cat-file -e` exit 0; 8547 B; carries `## SHONEN`), **does not resolve in the lane** (exit 128) | both `cat-file -e` calls, copied into § 7.3 |
| **composed instrument spend on the current patches** | **402 added / 29 deleted** (22/3 floors spend at the base + E01 210/10 + E02 170/16) against the frozen `LINE_CAP = 900`; the superseded cuts measured 269/21 and 472/31 and are kept only as history | `git apply` into base clones + `git diff --numstat 072048fa <rev> -- <six battery scripts>`, receipts `Kb81E15Order/Kb81E15Order-instrument-cap.txt`, `composed-numstat-v2.txt` |
| **the E6 pin check at a composed tip** | with the `c66103f3…` erratum: `FAIL guard instrument-pin: verifiers/verify_corpus_independent.py blob 59602942… is not a pinned blob`, `guards 4 of 5` (exact string in § 2.5); the republished `c15680f8…` pins `59602942…` | counter run at scratch commit `d3f29d59`, receipt `Kb81E15Order/composed-prestale-pin-tipbattery.txt` |
| **the G1 content group at the r81 bytes** | `tracked_files 157`, `unindexed 0`, `stale 0`, `missing 0`, `report_total 111`, `report_dead 1` (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`), `commit_unresolvable 2` (**both** `corpus/SOURCES.md:171-172`) → both corpus gates exit 1; registry 63 of 63 exit 0; correction sweep 0 exit 0 | receipts `Kb81E15Order/G1-integrity.json`, `G1-independent.json`, `G1-registry.txt`, `G1-sweep.txt` |
| **the battery at a G1-only tip** | `fleet root …; guards 5 of 5; tip battery exit 0: 4 of 6`, **exit 1 in both forms**; the six gates registry 0 / floors 0 / checklist 0 / integrity 1 / independent 1 / sweep 0; 14 receipts, 10 green, 4 non-zero, 335 s wall | `.ufo/waves/round-81/build/Kb81E15Order/battery-content-group/` |
| the refresh script r81 copy | `.ufo/waves/round-81/build/refresh-corpus-baseline.py`, sha256 `8481be46…b470a` — **byte-identical to the r80 copy tracked at base** | `sha256sum` both |
| the r81 battery runner | `.ufo/waves/round-81/build/run-battery.sh`, sha256 `19b878a1…c76a`, usage `<rev> <repo> <out-dir> [<report-path>]`, 15 receipts (01–15), exit 0 all-green / 1 a red reading / 2 environment | read of the script header |
| disk | `/fast/scratch/hyaku` 27 % used, 588 G free | `scripts/hyaku/disk-guard.sh status` |
| lane governance files | `LOG.md` (569 755 B) and `SCORECARD.md` (206 990 B) live **in the lane**, clean at the base | `ls -la LOG.md SCORECARD.md`; `git status` |

Two facts to keep in front of you while reading § 3:

1. **The registry gate's universe is the top level of `verifiers/` only** (`.py`/`.sh`), and it is
   **63 → 64** this round, not 62 → 63 (r80's number).
2. **The E6 pin table is a function of the landed instrument bytes.** The base blobs are already
   pinned, so an amended counter with pins that do not yet match a *repaired* instrument fails
   `instrument-pin` **by name** — the pin is the anti-laundering guard, not the size cap.

---

## 2. Pre-flight (run before G0; every step here can refuse a later one)

### 2.1 Lane state

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD         # b2842231… before G0
    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin for-each-ref refs/heads/master
    jj -R /home/vgpnk/Projects/shokunin/kotoba-shokunin bookmark list           # master → b2842231 (read-only)

`jj-lane.sh state kotoba` could **not** read this lane from the fleet root in this seat's run
(`jj-lane: not a real clone (missing .git directory): kotoba`, exit 1) — it resolved the id to a path
without `.git`. Read the state with the three plain git/jj commands above instead; that is what the
recipe's commits need (branch name `master`, already-known tip).

### 2.2 Dirty-tree inventory — every entry must be classified before G6

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain --untracked-files=all

| class | paths at wave start | disposition |
|---|---|---|
| the pre-data plan (L1-frozen) | `plans/round-81.md` | commit in **G0** |
| the stray probe file (R80-D2 class) | `.ufo/wapes` (594 B, content = a C2 quote probe, `words=11 ok=False why='quote lies in the first-heading block (Q70)'`) | **delete from the root**; its bytes go to `.ufo/waves/round-81/dispositions/wapes.txt`, committed (E04's patch adds exactly that file) |
| wave evidence | `.ufo/waves/round-81/**` (build, w1, receipts, snapshots, dispositions, `w1-spec.json`, `w1.ready*`, `build-w1-spec.py`) | commit in **G5**; `snapshots/` + `dispositions/` commit earlier in **G1** because claims read them |
| scribe drafts applied into lane files | `LOG.md`, `SCORECARD.md` (drafts in `build/Kb81S02Log.md`, `Kb81S03Scorecard.md`) | commit in **G4** |
| lane-tree patch targets | `SKILL.md`, `PROVINCE.md`, `corpus/**`, `verifiers/**`, `verifiers/corpus-baseline.json` | G1–G3, G6 |

The refresh refuses on **any** leftover, tracked or untracked (§ 4). The wave build dir itself is the
largest leftover: until G5 the tree can never be clean.

### 2.3 The freeze receipt exists before any after-value

    test -f .ufo/waves/round-81/receipts/freeze-shas.txt && grep -c '{{' .ufo/waves/round-81/receipts/freeze-shas.txt

`Kb81S15FreezeShas` publishes the format with `{{…}}` markers where seat bytes were still pending. The
L1 fills every marker from the **landed** bytes (`sha256sum`, `git hash-object`), re-writes the file,
and commits it with G0 or G1 — **before** the G7 measurement. A freeze receipt with live `{{…}}`
markers at the final tip is an unverified freeze and voids C1's calibration sub-axis.

### 2.4 Pre-flight the E6 cap arithmetic — **read this before G2**

**The erratum was revised pre-freeze, and the plan now says 900 with tight tuples.** `plans/round-81.md`
line 15 (verbatim): "`INSTRUMENT_PINS` for the two corpus gates reset to TIGHT tuples `(<r72 base blob>,
<reviewed r81 blob>)` admitting exactly the round-81 post-image, `LINE_CAP` 40→900 as the outer
no-laundering bound (justification below)"; line 28's kill rule reads "base-spent + measured added > 900".
The earlier 140 version of E6 is superseded, and so is every 140-era measurement (including this seat's
`269/21` and `472/31` figures — they measured the superseded patch cuts and are kept only as history).

The guard does not measure the patches; it measures the composed tree:

    git diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 <rev> \
      -- verifiers/check_gate_registry.py verifiers/check_assertion_floors.py \
         verifiers/verify_skill_checklist.py verifiers/verify_corpus_integrity.py \
         verifiers/verify_corpus_independent.py verifiers/check_correction_sweep.py

Measured on the **current** patch bytes (E01 `6bbb304b…` 210/10, E02 `d8bf88c8…` 170/16, E05
`c66103f3…` 24/16; three `git apply` exit 0 into a base clone, scratch commit `d3f29d59`):

    22  3  verifiers/check_assertion_floors.py     (spent at the r81 base)
    210 10 verifiers/verify_corpus_integrity.py
    170 16 verifiers/verify_corpus_independent.py
    totals: added=402 deleted=29   cap=900   headroom=498

So the size guard passes on the current stack. Two caveats the integrator must carry:

* the plan's own justification still cites the superseded cuts ("+203/-10 and +247/-18 … +472/-31"); the
  freeze receipt must record the **measured** numstat of the frozen blobs, so the parenthetical and the
  receipt will disagree until one of them is corrected;
* if the L1 re-cuts the erratum back to 140 (the orchestrator's stated preference — "900 must not land"),
  the repairs must shrink to **≤ 118 added combined** (284 lines out of E01+E02) before the guard can pass.

Receipts: `Kb81E15Order/Kb81E15Order-instrument-cap.txt` (three compositions, each with its command).

### 2.5 The erratum itself: the checks that decide whether it may land

E6 is a frozen line set, so the amended counter is measured against the plan — and, decisively, **the
pins are measured against the blobs the repair patches actually produce**. This checker was run by this
seat on the composed scratch tree (base + current E01 + E02 + E05); it prints both answers:

    cd <tree with the amended counter>
    python3 - <<'PY'
    import ast, subprocess
    def consts(text):
        out = {}
        for node in ast.parse(text).body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                try: out[node.targets[0].id] = ast.literal_eval(node.value)
                except Exception: pass
        return out
    base_text = subprocess.run(["git", "show",
        "b284223105f4d106f7e8f56ed4fd296c643cda0e:verifiers/check_tip_battery.py"],
        capture_output=True, text=True).stdout
    base, tip = consts(base_text), consts(open("verifiers/check_tip_battery.py").read())
    print("LINE_CAP tip:", tip.get("LINE_CAP"), " base:", base.get("LINE_CAP"))   # plan v2: 900 / 40
    for row in ("verifiers/verify_corpus_integrity.py", "verifiers/verify_corpus_independent.py"):
        print(row, "pinned:", tip["INSTRUMENT_PINS"][row])
    PY
    for p in verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py; do
      echo "$p $(git rev-parse HEAD:$p)"; done

Measured on the current stack (scratch commit `d3f29d59`):

    LINE_CAP tip: 900  base: 40
    integrity   pinned ('e470eaea…', 'bbee51f2…')   actual blob bbee51f2…   MATCH
    independent pinned ('edac0df7…', '7b37461a…')   actual blob 59602942…   **MISMATCH**

**One stale pin, and it blocks G2.** `7b37461a…` was the earlier 247/18 cut of E02; when E02 was revised
to 170/16 the blob moved to `59602942075d8fe77061876fb52eb32a44313697`, and the erratum still pinned the old
value. Measured in the counter's own words at that composed tip (base + E01 + E02 + the `c66103f3…`
erratum, scratch commit `d3f29d59`; receipt `Kb81E15Order/composed-prestale-pin-tipbattery.txt`):

    guarded paths 586, deleted 0; floors 15 rows; instruments added 402 / deleted 29 lines (cap 900)
    guard no-deletions PASS
    guard floors PASS
    guard instrument-size PASS
    FAIL guard instrument-pin: verifiers/verify_corpus_independent.py blob
      59602942075d8fe77061876fb52eb32a44313697 at d3f29d59… is not a pinned blob
    guard spotcheck-identity PASS
    fleet root /home/vgpnk/Projects/shokunin; guards 4 of 5; tip battery exit 0: 4 of 6

`Kb81E05Erratum` republished the patch (`c15680f8…`) with the independent pin set to `59602942…` and the
integrity pin to `bbee51f2…`; the pins then match the blobs the current E01/E02 produce. The general rule
stands for the integrator: **the pin hexes are a function of the repair bytes, so any re-cut of E01 or E02
re-opens this check.**

The integrity row matches, and the other four pin rows are byte-identical to the base (verified). The fix
is one hex inside E6 line set (b) — the declared pin member — plus a re-issued patch sha256 in the freeze
receipt. It is **not** a cap change and it is **not** a reason to touch the guard logic.

Ordering rules that follow:

* run § 2.4 and § 2.5 on a **scratch clone of the composed stack** before committing G2; a pin hex or a
  `LINE_CAP` value that does not match the frozen plan is a mechanical fix in the erratum patch, never an
  edit to the gate at integration time;
* the erratum patch and the instrument patches must land in the **same commit** (§ 3 G2), because the
  pins are a function of exactly those bytes;
* the two control surfaces stay open regardless: a tight tuple still admits a base-bytes tip, so the base
  reading (`guards 5 of 5; 4 of 6`) remains measurable after the amendment.

### 2.6 Artifact reconciliation against the wave spec

    ls -1 .ufo/waves/round-81/build/

The w1 spec (`w1-spec.json`, 64 seats) names the expected artifacts. Reconcile the landed set against
`§ 3`'s path list; where a seat's artifact is missing, **derive it yourself from the same inputs and
record that you did** (the plan's rule for a consumed build output). The recipes in § 3 that matter
are the gate readings — they are cheap to re-measure, so a missing draft never blocks the order.

---

## 3. The ordered recipe

Commit mechanics (unchanged from r80, re-read from `scripts/hyaku/jj-lane.sh`):

    /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit kotoba --as kotoba -m "<msg>" -- <path>...

* Commits are **pathspec-limited**: `validate_change_scope` refuses any changed path outside the
  named request (`commit changed a path outside the request: <path>`), and refuses repo internals and
  `.ufo`, `.ufo/state`, `.ufo/state/*`, `.ufo/watchdog.log`. `.ufo/waves/**` and `.ufo/waves/round-81/**`
  are **allowed**; the lone `.ufo/wapes` was never blocked, only disowned.
* `exit 0` landed and pushed · `exit 1` refused · **`exit 3` committed but the push failed** — the
  commit is kept; run `jj-lane.sh push kotoba`, never re-run the commit blindly.
* No amend: the baseline records `measured_against.head`, so the content commit must stay put.
* A named path is canonicalised with `realpath -m --relative-to=.`; naming a **symlink** resolves its
  target and can escape the lane root (`path escapes the lane root`). Name the parent directory
  instead (r80 R13/R14). This round the trap is latent only — see § 7.3 for why no symlink commit is
  in the recipe.

### The staged readings — what the battery says after each group (all measured this seat)

| tip | registry | integrity | independent | battery | why |
|---|---|---|---|---|---|
| r81 base `b2842231` | 63 of 63, 0 | red: 5 classes | red: 2 classes | **`guards 5 of 5; 4 of 6`**, exit 1 | the receipted base |
| + G1 (content, rows, snapshot, disposition) | 63 of 63, 0 | red: `report_dead 1`, `commit_unresolvable 2` (+ two equal-mode) | red: `commit_unresolvable 2` | **`guards 5 of 5; 4 of 6`**, exit 1 | R1/R2 not landed — the load-bearing intermediate |
| + G2 (repairs, manifest, erratum) + G3 (C2 counter, SKILL, PROVINCE) | **64 of 64**, 0 | red **only** on the two equal-mode baseline classes (`tracked_files 157≠154`, `report_total 111≠109`); `report_dead 0`, `commit_unresolvable 0` | **exit 0** | **`guards 5 of 5; 5 of 6`**, exit 1 — integrity the one red (receipt `Kb81E15Order/composed-full-tipbattery.txt`) | the repairs work; the baseline still records round 80 |
| + G5 (clean tree) + G6 (refresh + baseline committed) | 64 of 64, 0 | **9/9, exit 0** (expected — the refresh re-records the two equal-mode counts) | exit 0 (expected) | **`guards 5 of 5; 6 of 6`**, exit 0 — **expected, not measured by this seat** | the after-value; the L1 measures it, this runbook only predicts it |

Two consequences the integrator must not miss:

* **`6 of 6` is unreachable before G6.** `tracked_files` and `report_total` are *equal-mode* classes
  compared against `verifiers/corpus-baseline.json`; until the refresh re-records them, integrity stays
  red by design. A red integrity at the G3 tip is the expected state, not a stalled repair — the measured
  proof is that `report_dead` and `commit_unresolvable` are already 0 there.
* **The C2 claim is measurable from G3** (`sdk allowed-tools surface documented 1 of 1`, exit 0 at the
  G1+G2+G3 tip, conjuncts a–g ok; receipt `Kb81E15Order/C2-after.txt`). It does not depend on G6, so a
  round that stops C1 (§ 3.9) still scores C2.

### G0 — the frozen plan, alone

    paths: plans/round-81.md
    msg:   "round-81: freeze the plan and the w1 wave spec before claim data"

Why first: the plan is the freeze artifact and the only untracked file outside the wave dir whose
presence is a *precondition* of the claims (the erratum E6 line set, the C2 conjuncts). Land it before
any measured repair so history shows the declaration precedes the data.

Gate after G0: nothing to run — a plan commit moves no gate. (If you also commit
`.ufo/waves/round-81/receipts/` here, `check_correction_sweep.py --root .` must still print
`correction sweep: 0 stale block(s)`.)

### G1 — corpus content + index rows + source rows + the claim's snapshot + the wapes disposition

    paths: corpus/lessons/round-81.md
           corpus/knowledge/allowed-tools-sdk-round81.md
           corpus/README.md
           corpus/SOURCES.md
           .ufo/waves/round-81/snapshots
           .ufo/waves/round-81/dispositions

Inputs (landed by the wave): `build/Kb81S01Lesson.md` (lesson body), `build/allowed-tools-sdk-round81.md`
(the C2 entry), `build/Kb81S08ReadmeRows.patch` (three coverage rows + the Frontier note;
`git apply --check -p1` **passes at the base** — measured), `build/Kb81S05SourcesEdits.patch`
(S249 `mined` row, S250 supersede row, S248 `used-by` old→new), `snapshots/S249.md` +
`S249.fetch.json` + `S249.manifest` (28395 B, sha256 `ac62c2df…e5a2` — the manifest row and the fetch
record agree, measured), `build/Kb81E04Baseline.patch`'s first hunk (the `dispositions/wapes.txt` file).

Why all in one commit — the index see-saw, **measured at the r81 bytes this seat**: a tree with the
S08 rows applied and the two new corpus files present reads `unindexed 0, stale_patterns 0,
missing_paths 0`, and `tracked_files 157`; rows without files or files without rows red the opposite
class (r80 E03 measured `stale_patterns 2 + missing_paths 2` / `unindexed 2`; the refresh's own base
refusal at r81 is `corpus.index.unindexed observed 1` — receipt `refresh-base.txt`).

Why the snapshot is *here* and not with the rest of the wave evidence: the C2 counter's conjunct (c)
reads `.ufo/waves/round-81/snapshots/S249.md` **from the measured revision**. If the snapshot only
lands with G5's bulk `.ufo/waves/round-81` commit, every earlier tip reads `0 of 1` for a reason that
has nothing to do with the entry. Naming the directory early also keeps the dispositions file tracked
before the clean-tree check.

Expected readings after G1 — **measured on the real-bytes G1 tree this seat** (clone at
`1d70af0d…` = base + S08 patch + S05 patch + S01 lesson + E08 entry + the snapshots), and the four
corpus classes are the expected intermediate, **not** regressions:

    python3 -B verifiers/verify_corpus_integrity.py --json     # exit 1
    #   unindexed 0 / stale 0 / missing 0        (the new pair is closed — measured)
    #   tracked_files 157 vs 154                 (equal-mode; G6 re-records)
    #   report_total 111 vs 109                  (equal-mode; G6 re-records)
    #   report_dead 1   detail: corpus/lessons/round-77-verifier-spotcheck.md:15 HEAD:.ufo/reports/round-77/kotoba.md
    #   commit_unresolvable 2  detail: corpus/SOURCES.md:171 and :172 (the one S230/S231 hash, twice)
    python3 -B verifiers/verify_corpus_independent.py --json   # exit 1, commit_unresolvable 2 only
    python3 -B verifiers/check_gate_registry.py --rev <tip>    # 63 of 63, phantom 0, exit 0
    python3 -B verifiers/check_correction_sweep.py --root .    # 0 stale block(s), exit 0
    /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
                                                               # `kotoba ok …/corpus/SOURCES.md`, exit 0
    # and the whole battery at this tip: guards 5 of 5; tip battery exit 0: 4 of 6, exit 1 (both forms)

Two details worth knowing: the lesson's other hex tokens (`fc48a5db`, `bb65e3e4`, `a9228305`, `5afe1810`,
`0141c203`) did **not** add an `commit_unresolvable` entry — only the S230/S231 hash did, twice, which is
the base's own count; and `verify_skill_checklist.py` must be judged in a fleet-shaped world (§ 7.8) —
in a clone named `clone6` it reds `trigger.name_directory` and the `../.ufo/...` citations for reasons
unrelated to this round.

If `sources-census.sh validate` turns red on the two new rows, the cause is row *shape* (a cell count
≠ 11, or a `|` inside a cell) — fix the row, never the census.

### G2 — the two corpus-gate repairs + the external-commit manifest + the E6-amended counter (ONE commit)

    paths: verifiers/verify_corpus_integrity.py     # R1: <rev>:<path> object resolution + content identity
           verifiers/verify_corpus_independent.py   # R2, independent implementation of the same binding
           verifiers/external-commits.json          # the reviewed evidence manifest (E03)
           verifiers/check_tip_battery.py            # erratum E6: LINE_CAP 900 + two TIGHT pins + derived constants

Inputs: `build/Kb81E01Integrity.patch`, `build/Kb81E02Independent.patch`,
`build/Kb81E05Erratum.patch`, `build/Kb81E03ExtManifest.json` (the manifest body; one entry:
`7bb48f213ac677f943d5c791199ed3dddf302f00` → `mistralai/mistral-vibe`, evidence
`.ufo/waves/round-79/snapshots/S231.fetch.json` — **tracked at the base, measured**, and the hash occurs
in that receipt).

**Why these four files in one commit — this is the single most important ordering constraint.**
`instrument-pin` allows each instrument's blob to be the **base blob or a pinned blob**. Two shapes are
therefore possible:

* counter first, repairs second → the amended pins name blobs that do not exist yet, but the files are
  still the base blobs (already pinned) → the guard *passes*; the repairs then land and the pins are
  already correct. Legal but two chances to get the blob wrong.
* repairs first, counter second → `instrument-pin` fails by name at the intermediate tip.
* **same commit** → no tip exists in either bad shape. Do this.

`verifiers/external-commits.json` belongs in the same commit for a mechanical reason, not a stylistic one:
the repaired gate reads it **from the measured revision** —
`entries = json.loads(git_blob_bytes(repo, f"HEAD:{EXTERNAL_MANIFEST}"))["commits"]` (E01 patch, the
`EXTERNAL_MANIFEST` reader) — and then verifies that the named receipt's committed bytes hash to
`receipt_sha256`. Landing it a commit later leaves `commit_unresolvable 2` red at a tip whose instruments
already claim the binding, a shape that reads like a broken repair.

Pre-flight the manifest against the committed receipt (measured this seat: both digests agree):

    sha256sum .ufo/waves/round-79/snapshots/S231.fetch.json
    # e75f057a8e8f8319df227a254a42526ed096c7d0dc5364307365729a08ae738f  == the manifest's receipt_sha256
    grep -c '7bb48f213ac677f943d5c791199ed3dddf302f00' .ufo/waves/round-79/snapshots/S231.fetch.json   # 1

Use the manifest **as embedded in the E01 patch** (schema `{note, commits:[{hash, repository, receipt,
receipt_sha256}]}`); `build/Kb81E03ExtManifest.json` is the seat's evidence draft and uses different keys
(`hash/repo/evidence/pinned_at`), so pasting it in place of the patch's file would leave the gate unable to
find its fields.

Expected readings after G2:

    python3 -B verifiers/verify_corpus_integrity.py --self-test    # 0 failures (≥164 assertions)
    python3 -B verifiers/verify_corpus_independent.py --self-test  # 0 failures (≥105)
    python3 -B verifiers/check_tip_battery.py --self-test          # 0 failure(s) over 69 assertions (measured)
    python3 -B verifiers/verify_corpus_integrity.py --json         # still 2 equal-mode DRIFTs here; see below
    python3 -B verifiers/verify_corpus_independent.py --json       # all PASS, exit 0 (measured)
    python3 -B verifiers/check_tip_battery.py --rev <tip> --repo . # guards 5 of 5 (measured); 5 of 6 until G6

Note the intermediate that matters for the plan's own control worlds: **with G1 landed and G2 not, the
battery still reads `4 of 6`, correctly** — integrity/independent red on `report_dead` +
`commit_unresolvable`, registry/floors/checklist/sweep green. `Kb81E04Baseline`'s R04 receipt is the
same state seen from the refresh side: `refused: zero-mode corpus.pointers.report_dead observed 1`,
exit 2. So a red battery at that boundary is evidence the repairs are load-bearing, not a stalled wave.

**The after-value is not reachable at the G2 tip, and that is correct.** Measured at a composed
G1+G2+G3 tree (scratch commit `84f6c5a6`, receipt `Kb81E15Order/composed-integrity.json`): `report_dead 0`
and `commit_unresolvable 0` — both repairs work on the real corpus bytes — while `tracked_files 157≠154`
and `report_total 111≠109` remain, because those are **equal-mode** classes recorded in
`verifiers/corpus-baseline.json` at the round-80 tip. Integrity therefore still exits 1 and the battery
reads `5 of 6` until G6 re-records the counts. A `6 of 6` seen before G6 means a baseline was hand-edited
or carried — inspect it, do not celebrate it.

### G3 — the C2 counter + its SKILL row + the SKILL SDK line + the PROVINCE cell (ONE commit)

    paths: verifiers/check_sdk_allowed_tools.py   # the new counter (E09)
           SKILL.md                               # the SDK-channel line + the registry row (S09)
           PROVINCE.md                            # the ## Core bullet extension (S10)

Inputs: `build/check_sdk_allowed_tools.py`, `build/Kb81S09SkillRule-SKILL.patch` (rewrites the
`allowed-tools` rule paragraph at `SKILL.md:163` — **no added line** — and appends one registry row
after the `check_allowed_tools.py` row), `build/Kb81S10Province.patch` (`git apply --check -p1`
**passes at the base** — measured).

**Merge the SKILL edits into one application; never apply two patches to the same table.** The r80
runbook's § 7.2 trap returns in a different form: S09's registry row must be **contiguous with the
table block**. Measured this seat on the r81 bytes:

| probe | reading | exit |
|---|---|---|
| counter present, no SKILL row | `conformant 63 of 64 lane verifiers; phantom 0` | 1 |
| counter present, row inserted **after the blank line** before `## Sources` | `63 of 64` (the row is invisible: the parser stops at the first non-cell line after the header) | 1 |
| counter present, row appended **immediately after** the last table row (line 518) | `conformant 64 of 64 lane verifiers; phantom 0` | 0 |
| row present, counter file removed | `conformant 63 of 63 lane verifiers; phantom 1` | 1 |

So: file + contiguous row in the same commit, and the file must exist when the row is measured.
`verifiers/check_sdk_allowed_tools.py` is also a *gate* in the registry sense — its row needs
`0=clean, 1=failed`, a backticked `--self-test` flag that has an **exact handler** in the script, a
non-empty write scope and owner `kotoba`.

Expected readings after G3:

    python3 -B verifiers/check_gate_registry.py --rev <tip>          # 64 of 64; phantom 0, exit 0   (measured)
    python3 -B verifiers/verify_skill_checklist.py                   # exit 0                        (measured in a fleet-shaped world)
    wc -l SKILL.md                                                   # 597 (measured) ≤ 600 budget
    python3 -B verifiers/check_sdk_allowed_tools.py --rev <tip>      # `sdk allowed-tools surface documented 1 of 1`, exit 0 (measured)
    python3 -B verifiers/check_sdk_allowed_tools.py --self-test      # 0 failure(s) over 138 assertions in 47 world(s) (measured)
    python3 -B verifiers/check_province_core.py --rev <tip> --repo .  # `province core rows 2 of 2`, exit 0 (measured;
                                                                     #   not one of the six battery gates, but PROVINCE.md moved)

If `wc -l SKILL.md` exceeds 600, the budget is not raised: compress the SDK sentence into the existing
paragraph (it is one line already) or drop a redundant row — the checklist's `trigger.line_budget`
reads the number in the box.

### G4 — the lane governance files (LOG.md, SCORECARD.md)

    paths: LOG.md
           SCORECARD.md

Inputs: `build/Kb81S02Log.md`, `build/Kb81S03Scorecard.md`. These are the lane's two largest prose
surfaces and the ones `verify_skill_checklist`'s `governance.citation_resolves` walks. Apply the drafts
verbatim, then:

    python3 -B verifiers/verify_skill_checklist.py            # exit 0 (fail 0)
    python3 -B verifiers/check_assertion_floors.py            # 17 PASS rows, exit 0
    python3 -B verifiers/check_correction_sweep.py --root .   # 0 stale block(s), exit 0

Trap (r80 § 7.8, still live): the `..`-hop cap is 3 in **prose**. Never backtick a four-hop relative
path in `LOG.md`/`SCORECARD.md`/`SKILL.md`; the citation gate reads it as a token to resolve.

### G5 — the wave evidence (this is what makes the tree clean)

    paths: .ufo/waves/round-81

    rm -f .ufo/wapes        # if it is still at the root; its bytes are already committed under dispositions/

Gate after G5 — for this group the gate **is** the precondition:

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain --untracked-files=all
    # must print NOTHING

Note what this commits: every seat report under `w1/`, every build receipt, the freeze receipt, the
snapshots and `w1-spec.json`/`w1-dispatch*.json`/`w1.ready*`/`build-w1-spec.py`. The 127 KB dispatch
JSON is orchestration metadata; r80's precedent committed it in the wave dir, so keep it — the
alternative is an untracked file that blocks the refresh forever.

### G6 — the corpus baseline: refresh at the clean tip, then commit the baseline ALONE

From the lane root, clean tree:

    python3 -B .ufo/waves/round-81/build/refresh-corpus-baseline.py --repo .

Expected (measured by `Kb81E04Baseline` R07 on a repaired world, and shaped by this seat's G1 probe):

    corpus.index.tracked_files         155 -> 157      # 155 base + the new lesson + the new entry
    corpus.pointers.report_total       111 -> (observed) # the script prints what it records
    wrote <lane>/verifiers/corpus-baseline.json (head <G5 tip>)
    post-refresh: 9/9 checks pass, exit 0
    independent: exit 0; exit 0
    exit=0

Then:

    /home/vgpnk/Projects/shokunin/scripts/hyaku/jj-lane.sh commit kotoba --as kotoba \
      -m "r81: refresh the corpus baseline at the C1/C2 tip" -- verifiers/corpus-baseline.json

**No `--carry`** (§ 4). Commit the baseline **alone** and never amend the content commit: the baseline
records `measured_against.head` = the G5 tip.

### G7 — the final measurement, then the report

Run § 6 at the G6 tip (both tip-battery forms first, then the gates, then the C2 counter), then write
`.ufo/reports/round-81/kotoba.md` into the **fleet** root
(`/home/vgpnk/Projects/shokunin/.ufo/reports/round-81/kotoba.md`; r79/r80 reports live in the fleet
repo, not the lane), and only then run the report-pointer gate:

    python3 -B verifiers/check_report_pointers.py \
      --report /home/vgpnk/Projects/shokunin/.ufo/reports/round-81/kotoba.md \
      --repo . --rev <G6 tip> --round 81       # `report pointers resolved N of M; unresolved 0`, exit 0

Every backticked lane pointer in the report must resolve at that tip; `--round` names
`.ufo/waves/round-81/` for the wave-dir pointers.

### 3.9 Path B — the ordering when C1 stops (re-cut to 140, an unfixable pin, or a control world reaching 6 of 6)

If the L1 re-cuts E6 back to `LINE_CAP = 140` (the repairs must then shed 284 lines), or a pin cannot be
made to match the repair bytes, or a control world reaches `6 of 6`, **C1 stops and G2 does not land**,
and no counter goes in whose pins name blobs the tree does not carry. The stop is recorded, not
engineered around: the `instrument-size` guard measures from the frozen r73 base forever, so an over-cap
landing leaves every later round's battery at `guards 4 of 5` — and no amend is allowed to take it back.

The order that still ships the independent claim:

    G0  plans/round-81.md
    G1  corpus content + rows + snapshots + dispositions        (unchanged; C2 needs it)
    —   no G2: verifiers/**, except the new counter, stay at their base bytes
    G3  verifiers/check_sdk_allowed_tools.py + SKILL.md + PROVINCE.md   (registry 63 → 64, 64 of 64)
    G4  LOG.md + SCORECARD.md
    G5  .ufo/waves/round-81  + rm -f .ufo/wapes                  (tree clean)
    —   no G6: the refresh cannot write while report_dead/commit_unresolvable are nonzero,
        and carrying them would record a fabricated green. verifiers/corpus-baseline.json
        keeps its round-80 record; the tip's corpus drift is *reported*, never baselined.
    G7  the final battery + the C2 counter + the report

The final readings in that shape, measured at the r81 bytes: tip battery `guards 5 of 5; tip battery
exit 0: 4 of 6`, exit 1 (integrity/independent red on the two base classes — nothing new); registry
`64 of 64; phantom 0`, exit 0; floors/checklist/sweep green; the C2 counter `sdk allowed-tools surface
documented 1 of 1`, exit 0. C1 is written as an honest stop with the composed numstat as its receipt
(`402 added / 29 deleted vs cap 900`, or the re-cut figure if E6 goes back to 140), C2 is scored on its own axis, and the corpus gates stay red with
the two named causes — which is the honest state, not a defect to be repaired after data.

The `## Gate` section of the lesson and the report must both carry that stop in words, and the
scorecard row for C1 must read the stop with its receipt, not a narrowed restatement of the predicate.

---

## 4. The refresh script — exit 0 / 2 / 3, measured at the r81 bytes

Source: `.ufo/waves/round-81/build/refresh-corpus-baseline.py`, sha256 `8481be46…b470a`, **byte-identical
to the r80 copy tracked in the lane at the base** (so the r80 measurements R1–R5 apply unchanged; the
script's own header: `Exit: 0 written (or dry-run), 2 refused, 3 internal or post-condition failure.`).

| exit | class | this seat's / the baseline seat's own words | what the L1 does |
|---|---|---|---|
| **0** | written | `wrote <path> (head <sha>)` + `post-refresh: 9/9 checks pass, exit 0` + `independent: exit 0; exit 0` | commit `verifiers/corpus-baseline.json` alone (G6) |
| **2** | refused, **baseline untouched** | `dirty tree: … commit or clean these paths first` · `zero-mode corpus.index.unindexed observed 1, not 0` (this seat, at the r81 base — receipt `refresh-base.txt`) · `zero-mode corpus.pointers.report_dead observed 1, not 0` (Kb81E04Baseline R04, the content-only world) · `--carry corpus.index.unindexed: an index class is never carried` · `the two gates disagree on <hard class>` · `not a git work tree` / `is not the work-tree toplevel` · `a gate exited 2/3 (environment answer, not a measurement)` | fix the **named** cause and re-run. It stops at the first nonzero zero-mode class, so fixing one advances to the next |
| **3** | internal / post-condition failure — **and the baseline has already been written** (write at `:356`, post-conditions at `:369/:380/:387`) | `post-refresh: … did not emit JSON` · `drift this script does not own: <ids>` · the independent gate exited something other than 0/1 | do **not** commit the file as-is: inspect, restore it to HEAD (`jj restore` / `git checkout --`), fix the cause, re-run. A committed exit-3 baseline is a fabricated green |

Two behaviours to expect rather than fix:

* **`report_dead` is a soft class across the two gates** (`integrity 1 vs independent 0`): the script
  prints `gate disagreement (not recorded, expectation stays 0)` and continues to the next class. Both
  gates must still exit 0 at the final tip.
* **`corpus.index.*` is never carried.** `--carry` is a diagnostic, not a repair: it writes the
  baseline while the expectation stays 0 **and the gate stays red**, so a carried class can never reach
  `6 of 6` (r80 R5: `post-refresh: 7/9 checks pass, exit 1`).

The `--carry` decision tree, for the final tip only: a nonzero class names an unfinished repair —
`report_dead` → G2's R1, `commit_unresolvable` → G2's manifest/R2, `unindexed/stale/missing` → G1.
There is no legitimately carried class at the final tip.

---

## 5. Failure modes, in the order they will bite

### 5.1 Refresh exit 2 — dirty tree

The check is `git status --porcelain --untracked-files=all` **including staged files**. The usual
leftovers are the wave build dir (G5 not run), `plans/round-81.md` (G0 not run), `.ufo/wapes` (not
deleted), and any receipt a seat wrote after G5. Re-run G5's status command, then G6.

### 5.2 Refresh exit 2 — a zero-mode corpus class

`corpus.index.unindexed 1` → the coverage-map row for a new corpus file is missing (this is exactly the
r81 base state: `corpus/lessons/round-80-verifier-spotcheck.md` landed at `b284223` without a row).
`corpus.pointers.report_dead 1` → R1 (G2) is not landed or its object resolution misses the fleet root
(§ 7.3). `corpus.pointers.commit_unresolvable 2` → the manifest is absent at the measured rev or the two
S230/S231 tokens are not bound by it.

### 5.3 Refresh exit 3 — a half-verified baseline on disk

Restore `verifiers/corpus-baseline.json` to HEAD, fix the cause, re-run. Never commit it (see § 4).

### 5.4 Blob-sha mismatch on the E6 pin (`instrument-pin`)

Symptom: at the G2 tip the battery prints `guards 4 of 5` and a guard line naming
`verifiers/verify_corpus_integrity.py blob <sha> at <rev> is not a pinned blob` (or the independent
row). Cause: the pin hex was taken from a draft blob, or an instrument was edited after the pin was
computed, or a second instrument (not the one you pinned) was touched.

Fix path — recompute, never widen:

    python3 .ufo/waves/round-81/build/Kb81E14PinAudit-recompute.py --repo <scratch clone> \
        --patch Kb81E01Integrity.patch --patch Kb81E02Independent.patch --patch Kb81E05Erratum.patch

(Harness published by `Kb81E14PinAudit`; it recomputes base blobs, per-row membership, each patch's
sha256, the blobs a patch stack produces in a throwaway clone, and the E6 cap arithmetic. Checklist:
`build/Kb81E14PinAudit-base.txt` and `build/Kb81E14PinAudit.md`.) Then change **only** the pin hex string
(E6 line set (b)) and re-run `check_tip_battery.py --self-test` plus one battery pass.

The instrument-size arithmetic, measured on the **current** patches: base spend **22 added / 3 deleted**
against `072048fa`, E01 **210/10**, E02 **170/16** → composed **402 added / 29 deleted** against the
frozen `LINE_CAP = 900` (498 lines of headroom, § 2.4). The superseded cuts (269/21 and 472/31) are
history. If the L1 re-cuts the erratum to the earlier 140 the repairs must shed 284 lines first — the
guard is measured, never widened:

* under 900 with the current repairs → G2 lands once the pins match (§ 2.5);
* re-cut to 140, or pins that cannot be made to match → **C1 stops as an honest stop**; record the stop
  with the composed numstat as its receipt.

Note the two red-herring classes this section has already produced in round 81, both measured:
(a) a pin taken from an earlier cut of the repair patch (`7b37461a…` pin against `59602942…` blob —
the counter names the blob, read the name); (b) a cap value quoted from a superseded erratum draft
(140) against the plan's frozen 900. Both are checked mechanically by § 2.4–§ 2.5, which is why those two
commands run before G2 rather than after.

### 5.5 Census findings — duplicate ids and duplicate URLs

`Kb81S12AssimDisp`/`Kb81E12Census` publish the before/after census and the id-collision checks. At the
base the census prints 32 `W04 duplicate url … across scopes` lines and still ends `kotoba ok …`
(exit 0 — receipt `.ufo/waves/round-81/receipts/census-before.txt` and the runner's receipt `09-census`).
So: **a duplicate-URL warning is not the failure; a duplicated row id is.** A new row that reuses an
existing `S###` id, or a supersede row that rewrites S230 instead of appending S250, turns the census
red (`duplicate id`) after G1 — fix in G1, not in the census.

### 5.6 Registry shapes (G3)

`63 of 64` → the row is missing or invisible (blank line before it). `phantom 1` → the row precedes the
counter file. A stub script without a real `--self-test` handler reads as `self-test flag --self-test
lacks an exact handler`. Each of these is a one-line fix in the same commit.

### 5.7 SKILL.md line budget (G3)

Base 596, one row `+1` → 597; the SDK sentence replaces an existing line. Budget 600. If a draft adds
a second line elsewhere, compress; do not raise `trigger.line_budget`.

### 5.8 Pathspec refusals (any group)

`commit changed a path outside the request: <path>` → the group's `--` list is short by that path (the
usual case: a scribe also touched `corpus/README.md`, which belongs to G1).
`path escapes the lane root: ../…` → a named path is a symlink whose target leaves the lane; name the
parent directory instead.

### 5.9 The report-pointer gate (G7)

`check_report_pointers.py` fails on any backticked lane pointer in the report that does not resolve at
`--rev`. Two recurring causes: a pointer to a build file the L1 did not commit (it lives only in
scratch), and a pointer to the fleet-root report path written as if it were lane-relative. The report
itself stays in the fleet repo; only its *pointers into the lane* are checked.

---

## 6. The final-tip battery — exact commands and expected greens

Run one command at a time from the lane root and capture **the command's own exit**
(`cmd > f 2>&1; rc=$?; echo "exit=$rc" >> f`) — never through a pipe (round-80 lesson M80-1: a pipeline
reports its last element). The runner
`.ufo/waves/round-81/build/run-battery.sh <rev> <repo> <out-dir> [<report>]` does exactly this and
writes 15 receipts with `exit=` as the last line; use it, then run rows 1–2 and 12 below **literally**
because they are the frozen predicate's own forms.

| # | command | expected reading | exit |
|---|---|---|---|
| 1 | `python3 -B verifiers/check_tip_battery.py --rev <tip> --repo .` (from the lane root) | `fleet root /home/vgpnk/Projects/shokunin; guards 5 of 5; tip battery exit 0: 6 of 6` | 0 |
| 2 | `python3 -B verifiers/check_tip_battery.py --rev <tip> --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin` | same line as 1 | 0 |
| 3 | `python3 -B verifiers/check_gate_registry.py --rev <tip>` | `gate registry rows conformant 64 of 64 lane verifiers; phantom 0` | 0 |
| 4 | `python3 -B verifiers/check_assertion_floors.py` | 17 `PASS` rows, none `FAIL` | 0 |
| 5 | `python3 -B verifiers/verify_skill_checklist.py` | `"fail": 0` | 0 |
| 6 | `python3 -B verifiers/verify_corpus_integrity.py --json` | `9/9 checks pass` | 0 |
| 7 | `python3 -B verifiers/verify_corpus_independent.py --json` | all `PASS` | 0 |
| 8 | `python3 -B verifiers/check_correction_sweep.py --root .` | `correction sweep: 0 stale block(s)` | 0 |
| 9 | `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` | one `kotoba ok …/corpus/SOURCES.md` line (W04 duplicate-URL warnings still allowed) | 0 |
| 10 | `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --skill SKILL.md` | `rows 20 verified 20` · `skill description names 10 of 10 non-none lanes` · `skill description length ≤1024` | 0 |
| 11 | `python3 -B verifiers/check_report_pointers.py --report /home/vgpnk/Projects/shokunin/.ufo/reports/round-81/kotoba.md --repo . --rev <tip> --round 81` | `report pointers resolved N of M; unresolved 0` | 0 |
| 12 | `python3 -B verifiers/check_sdk_allowed_tools.py --rev <tip>` | `sdk allowed-tools surface documented 1 of 1` + the conjunct diagnostics | 0 |
| 13 | `python3 -B verifiers/check_province_core.py --rev <tip> --repo .` | `province core rows 2 of 2` (outside the plan's list; run because G3 edits `PROVINCE.md`) | 0 |

Two corrections inherited from r80 and re-checked here:

* **#10's plan-literal form is not runnable.** `check_sibling_census.py --skill SKILL.md` with no
  positional argument exits 2 with its `usage:` line (r80 R16). The census file positional is required;
  the form in the table is the working one.
* **#12 is a claim counter, not a battery gate.** It is not one of the six frozen gates and the battery
  runner does not run it — measure it separately, on the same tip, with its own exit captured.

Base truth for calibration (both forms read the same world — the counter builds a fleet-shaped sandbox
of `<rev>`): at `b2842231` the dot form is `.ufo/waves/round-81/receipts/tipbattery-base-dot.txt`
(`4 of 6`, exit 1) and the C2 counter reads `0 of 1`, exit 1.

---

## 7. Traps measured by this seat

### 7.1 The registry row must be contiguous with the table

Measured four ways (§ 3 G3's table). A row after the blank line before `## Sources` is silently
invisible: the parser ends the section at the first line that yields no cells after the header was seen.
This is the r81 form of r80's "two patches, one insertion point" trap.

### 7.2 The base blobs are already pinned — do not "fix" them

`verify_corpus_integrity.py` at the base is `e470eaea…`, which is its **second** pin tuple member;
`verify_corpus_independent.py` is `edac0df7…`, also already a member. E6 adds **one** member per row
(the reviewed r81 repair blob). If you see a pin failure naming a *base* blob, the pin table was
rewritten, not extended.

### 7.3 `report_dead` this round is the round-77 `HEAD:` object token — and it resolves in the fleet

    git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md'
    # fatal: path '.ufo/reports/round-77/kotoba.md' does not exist in 'HEAD'   (exit 128)
    git -C /home/vgpnk/Projects/shokunin cat-file -e 'HEAD:.ufo/reports/round-77/kotoba.md'
    # exit 0 — 8547 B, carries `## SHONEN` (grep -c '^## SHONEN' = 1)

Consequences: (a) R1's resolution order **must** be lane-then-fleet, or the token stays dead; (b) no
round-77 symlink commit is needed; (c) the content-identity arm (≥400 B + `## SHONEN`) is satisfied by
the fleet's own bytes — a seven-byte marker file at that path would fail it (the W8/W10 class).
Fallback only if R1 still dead-ends: the r80 G5 mechanism (commit the **parent directory**
`.ufo/reports/round-77`, mode `120000`, never the symlink path).

### 7.4 The snapshot is a claim input, so it must be committed early

Measured: `snapshots/S249.md` is 28395 B, sha256 `ac62c2dff61ef07bb778e5d115060e22f3f061fa3eca402be9b886946f01e5a2`,
identical to `S249.fetch.json`'s record and to `S249.manifest`'s single line. Because conjunct (c) reads
it at the measured rev, it belongs to G1 (§ 3).

### 7.5 `run-battery.sh` differs from the r80 copy

r80 `cddf2dd8…`, r81 `19b878a1…`. The r81 runner passes `--fleet` explicitly in receipts 01–02 so a
scratch world stays fleet-shaped; the frozen predicate's literal forms (rows 1–2 of § 6) are therefore
still measured by hand at the final tip.

### 7.6 `.ufo/wapes` is not a lane artifact and nothing else will remove it

`jj-lane.sh`'s path guard blocks only `.ufo`, `.ufo/state`, `.ufo/state/*`, `.ufo/watchdog.log`. The
file survives any number of commits; it blocks the refresh forever. Its bytes are now committed as
`.ufo/waves/round-81/dispositions/wapes.txt` (E04's patch), so `rm .ufo/wapes` is safe and final.

### 7.7 `jj-lane.sh state kotoba` did not read this lane in this seat's run

`jj-lane: not a real clone (missing .git directory): kotoba`, exit 1. Use `git rev-parse` /
`for-each-ref` / `jj bookmark list` (§ 2.1) — and do not read that failure as a lane defect.

### 7.8 Read the checklist and citation gates in a fleet-shaped world, never in a differently named clone

Measured: the same G1 tree, cloned as `…/Kb81E15Order/clone6`, reds two checks that have nothing to do
with round-81 content:

    FAIL trigger.name_directory: name 'kotoba-shokunin' != directory 'clone6'
    FAIL trigger.citation_resolves / governance.citation_resolves: '../.ufo/reports/round-7/kotoba.md'
      does not resolve from /fast/scratch/hyaku/kotoba-r81/Kb81E15Order/clone6   (+31 more)

Both are directory-shape artefacts: the skill name must equal its directory, and `../.ufo/...` pointers
must resolve from the lane's position inside the fleet. `run-battery.sh` builds exactly such a world
(`…/battery/run-*/world/kotoba-shokunin`) and there the same tree reads checklist exit 0 (receipt 05).
So: judge those two checks from the runner's world or from the lane itself; a clone named anything else
will lie to you in the red direction, exactly as a lane-adjacent clone can lie in the green direction.

---

## 8. What changed from the r80 runbook (`Kb80E15BaselineOrder.md`), and what still holds

| r80 item | status in r81 |
|---|---|
| G1 corpus content+rows in one commit (the index see-saw) | **holds**, re-measured at the r81 bytes with the new pair in the tree (`unindexed/stale/missing` all 0) |
| G2 counter file, then G3 rows (two commits) | **changed**: file + contiguous row + SDK line + PROVINCE in **one** commit (G3). r80 split because two seats' patches collided in one table end; here one seat (S09) produces both the sentence and the row, and the split's intermediate tips are red for no gain |
| G4 instrument repairs + amended counter in one commit | **holds** — and now also carries the new manifest, because both repaired gates read it at the measured rev |
| G5 round-76 report symlink | **not needed this round** (§ 7.3): the dead token is the round-77 `HEAD:` object, resolvable in the fleet root |
| G6 wave evidence, then G7 refresh + baseline alone | **holds** — plus the snapshot and dispositions moving forward into G1 as claim inputs |
| r80 E04 patch (report-pointer `<rev>:<path>`) | **read, ported in spirit, superseded**: R1 adds content identity (≥400 B + `## SHONEN`) so a marker file cannot pass |
| r80 E05 grammar patch (marker-based external class) | **read, superseded**: `verifiers/external-commits.json` binds hash→repo→committed receipt; a line marker alone never exempts |
| r80 E5 erratum (`LINE_CAP` 60, two composed pins) | **superseded by E6** (revised pre-freeze): `LINE_CAP` 900, base spend 22, composed 402/29 today, two TIGHT pin tuples `(base blob, reviewed r81 blob)` |
| r80 `--carry` tree and refresh exit 2/3 semantics | **holds**, script byte-identical (`8481be46…`) |
| r80 § 7.2 SKILL merge trap | **holds in a new form** (§ 7.1: contiguity, not patch order) |
| r80 § 7.9 clean-tree-with-untracked | **holds**, and is the reason G5 exists |

---

## 9. Evidence index (this seat's receipts, in `.ufo/waves/round-81/build/Kb81E15Order/`)

| file | what it proves |
|---|---|
| `base-registry.txt` | base registry `63 of 63; phantom 0`, exit 0 |
| `base-integrity.json` | the base integrity document: the five classes and their observed values |
| `base-independent.json` | the base independent document (`report_dead` 0, `commit_unresolvable` 2) |
| `base-tipbattery-selftest.txt` | `0 failure(s) over 69 assertions`, exit 0 |
| `base-integrity-selftest.txt` | `164 assertions`, exit 0 |
| `base-independent-selftest.txt` | `105 assertions`, exit 0 |
| `registry-counter-no-row.txt` | counter file without a row → `63 of 64`, exit 1 |
| `registry-counter-with-row.txt` | counter + contiguous row → `64 of 64; phantom 0`, exit 0 |
| `registry-row-no-file.txt` | row without the counter → `63 of 63; phantom 1`, exit 1 |
| `refresh-base.txt` | the refresh at the r81 base: `refused: zero-mode corpus.index.unindexed observed 1`, exit 2, baseline untouched |
| `content-group-integrity.json` / `content-group-independent.json` | the stub-body G1 probe: `unindexed/stale/missing` 0, `tracked_files 157` |
| `G1-integrity.json` / `G1-independent.json` | the **real-bytes** G1 tip: the exact class set and the two detail tokens (`HEAD:.ufo/reports/round-77/kotoba.md`, both `SOURCES.md:171-172`) |
| `G1-registry.txt` / `G1-sweep.txt` | registry `63 of 63` exit 0 and `correction sweep: 0 stale block(s)` exit 0 on the real G1 tree |
| `battery-content-group/` (01–14 + index) | `run-battery.sh` on the G1-only world: `guards 5 of 5; tip battery exit 0: 4 of 6` in **both** forms, 14 receipts, 10 green, 335 s wall |
| `Kb81E15Order-instrument-cap.txt` | the cap arithmetic, four compositions (base spend, E02-only, E01+E02 superseded, current 402/29), each with the guard's own `git diff --numstat` command |
| `composed-numstat-v2.txt` | the current composed numstat: 22/3 + 170/16 + 210/10 = 402/29 against `LINE_CAP` 900 |
| `composed-v2-tipbattery.txt` | the composed G2 tip with the republished erratum: `guards 5 of 5` — every guard PASS, corpus gates red only because G1 was not in that world |
| `composed-integrity.json` / `composed-independent.json` | the composed G1+G2+G3 tip: `report_dead 0`, `commit_unresolvable 0`, equal-mode DRIFTs only; independent exit 0 |
| `composed-full-tipbattery.txt` | the composed G1+G2+G3 tip: `guards 5 of 5; tip battery exit 0: 5 of 6`, exit 1 — the single red is integrity's equal-mode pair |
| `C2-after.txt` | the C2 counter at the composed tip: `sdk allowed-tools surface documented 1 of 1`, exit 0, conjuncts a–g ok |
| `composed-province-core.txt` | `province core rows 2 of 2`, exit 0 at the composed tip |
| `composed-prestale-pin-tipbattery.txt` | the stale-pin defect in the counter's own words (`guard instrument-pin` FAIL naming blob `59602942…`) |

Commands that produced them are the ones quoted in § 1 and § 3; each was run in
`/fast/scratch/hyaku/kotoba-r81/Kb81E15Order/clone{,2,3}` at the base or at a probe commit, with
`-C` naming the clone for every git call. Nothing outside this seat's scratch and
`.ufo/waves/round-81/build/` was written; the lane tree, its git/jj state and the fleet root were only
read.

---

## 10. What must not be done

* **No amend, no history rewrite**: the baseline's `measured_against.head` names the G5 tip.
* **No `--carry` at the final tip** (§ 4).
* **No `LINE_CAP` widening** beyond the frozen 900 as written in `plans/round-81.md`; if a re-cut sets it
  to 140 the repairs must fit under 140, and if the measured delta exceeds whatever bound is frozen, C1
  stops as an honest stop.
* **No edits to the six pinned instruments** other than the reviewed repair blobs; a 30-line edit inside
  the cap still fails `instrument-pin` by name.
* **No edit to the corpus gates after G6** — re-refresh instead.
* **No `.ufo/state/`, `.ufo/watchdog.log`, `.git/`, `.jj/` commits** (the helper refuses them).
* **No scoring by the integrator**: control/shortcut worlds are the critics' to score; a world that
  reaches a target is reported as a counter defect and is never repaired by narrowing.
* **No duplicate row ids**: S250 appends the S230 supersede; S230 stays as the audit trail.

VERDICT: ordered integration recipe delivered from first-hand r81-byte measurements — registry 63→64 arms, G1 class set, refresh refusal, staged battery readings (4/6 and 5/6 measured; the post-G6 6/6 predicted only), composed cap 402/29, the counter's own stale-pin FAIL, C2 1 of 1 — with a full-landing and a C1-stop ordering; no lane file mutated.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E15Order.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E15Order.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E15Order/
