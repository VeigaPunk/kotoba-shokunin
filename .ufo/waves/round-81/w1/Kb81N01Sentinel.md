# Kb81N01Sentinel — adversarial no-harm sweep, round 81 w1

Seat: sentinel (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` @ `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Surface: the five assigned items (a)–(e) — substrate pins, wave-dir uncommitted work, base-claim truth,
`.ufo/wapes` content, post-base writers — plus anything else this round could harm outside C1/C2.
Every count below carries the command that produced it; every verdict is an observed exit status, never a
pipeline's (`M80-1` discipline). Nothing here scores a claim after-value.

Receipts: `.ufo/waves/round-81/build/Kb81N01Sentinel-*.txt` (16 files, listed in DELIVERABLES).

---

## 0. Headline

Five findings, three of them actionable before the L1 commits:

| # | Finding | Severity | Who must act |
|---|---|---|---|
| A | Host substrate **did** drift and the pinned *path* vanished: `~/.local/bin/omp.real` is gone, so `check_substrate_pins.py`, `verify_harness_claims.py` and `check_substrate_repin_v2.py` all exit **2** at base. No r81 gate covers them. | medium (pre-existing, not r81-caused; coverage gap) | L1: declare, do not claim substrate green; re-pin in a later round |
| B | The published repair blob **exceeds E6's cap**: the chain adds **269** lines across the six instruments vs `LINE_CAP = 140`, so `instrument-size` fails and `guards 5 of 5` is unattainable. The plan's own kill rule fires. | **high — decides C1** | L1 + E01/E02 owners |
| C | Integration collisions: three mutually exclusive `corpus/SOURCES.md` patches (S05 / S16 / E12), three on `corpus/README.md` (E04Baseline / S08 / S08.stageA), two on `dispositions/wapes.txt`. A measured compatible chain exists. | **high (operability)** | L1 (integration order) |
| D | `.ufo/wapes` is a real quote-probe transcript but **2 of its 4 verdicts cannot be reproduced** from any committed snapshot; every shipped disposition patch commits it verbatim, `exit=0` included. | medium (provenance) | L1 (R3) |
| E | Every SOURCES draft rewrites `S248` to `queued` **with** a `used-by`, and adds `S249` as a duplicate URL of `S248`. Base invariant `queued ⇔ used-by —` (8/8, 0/149) has no gate; the duplicate adds a new `W04`. | medium | L1 + S05/S16 owners |

---

## 1. (a) Host substrate pins at base — **drifted, and the pinned path is gone**

Commands, in the lane root, verbatim:

```
$ python3 -B verifiers/check_substrate_pins.py
FAIL omp_binary_sha256: UNREADABLE: [Errno 2] No such file or directory: '/home/vgpnk/.local/bin/omp.real'
FAIL omp_binary_mtime: UNREADABLE: [Errno 2] No such file or directory: '/home/vgpnk/.local/bin/omp.real'
PASS opencode_binary_sha256: ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7
UNREADABLE 2/3 pins failed: omp_binary_sha256, omp_binary_mtime
exit=2

$ python3 -B verifiers/verify_harness_claims.py
INCONCLUSIVE: omp binary not found: /home/vgpnk/.local/bin/omp.real
exit=2

$ python3 -B verifiers/check_substrate_repin_v2.py --rev b284223105f4d106f7e8f56ed4fd296c643cda0e
cannot evaluate: verify_surfaces.py reported 0 row(s) (exit_code 2: omp binary not found: /home/vgpnk/.local/bin/omp.real);
pins 1/3 row(s) PASS, surfaces 0/0 check(s) PASS
exit=2
```

The drift is real, not merely a missing file:

| | pinned (`verifiers/baseline.json` `measured_against`) | live |
|---|---|---|
| path | `/home/vgpnk/.local/bin/omp.real` | `/home/vgpnk/.local/bin/omp` (`omp.real` absent, ENOENT) |
| sha256 | `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4` (r51 note: omp 18.12.6) | `ee2961c7da02e514a2475ee958c2fd85dbabf4d0907949ba5022edb2951f84b5` |
| mtime | `2026-10-21T20:37:24.615549837-03:00` | `2026-10-27 00:02:23.855671804 -0300` |
| shape | 1,680-byte launcher wrapper + real binary (r72 lineage) | 275,986,608 B ELF, `omp --version` → `omp/18.13.1` |

Attribution and blast radius:

- The binary landed at `2026-10-27T00:02:23`, i.e. **~23 h before** the r81 base commit (`23:05:39`) and
  inside r80's window. It is host-side; nothing in the lane can produce it, and this seat made no install.
- Because the *path* moved as well as the bytes, the guard reports tier 2 (`UNREADABLE`, "cannot read the
  pinned binary") rather than tier 1 (`DRIFT`). A reader skimming the ladder sees an environmental error, not
  a moved substrate — the r21/r23 "an unenforced pin is the defect" class, now unenforced *and* drifted.
- **No gate in this round covers it.** The r81 no-harm battery (`plans/round-81.md` § No-harm battery) lists
  the tip battery, gate registry, floors, checklist, both corpus gates, correction sweep, sources census,
  sibling census, report pointers — no substrate instrument. The tip battery's own six gates
  (`check_gate_registry`, `check_assertion_floors`, `verify_skill_checklist`, `verify_corpus_integrity`,
  `verify_corpus_independent`, `check_correction_sweep`) do not include them either, which is why the base
  receipt can honestly read `guards 5 of 5; tip battery exit 0: 4 of 6` while three substrate instruments
  are red.
- Lane text that this now leaves unbacked (read-only finding, no edit made):
  `PROVINCE.md:30` (round-72 Core: "omp.real and opencode v2.1.4 re-derived and re-pinned … counted by
  `verifiers/check_substrate_repin_v2.py`") — its counter exits 2; `corpus/README.md:171` (round-51
  "pins 3/3 … exit 0" — a dated record, keep as history, but nothing current reproduces it);
  `SKILL.md:559` ("`~/.local/bin/omp` embedded JS (`strings -n 6` …)") — that path is an ELF today.

Smallest remediation (not this seat's write scope): re-pin `measured_against.omp_binary_sha256`/`_mtime` to
the live path+bytes in one declarable r51-style re-pin step (or restore the wrapper/`omp.real` layout), add
`check_substrate_pins.py` to the no-harm battery so the next drift is caught where it happens, and correct
`SKILL.md:559`'s path description in whichever round touches that area.

**Consequence for r81:** none of C1's or C2's conjuncts read these instruments, so the two claims are not
affected — but no r81 text may assert the substrate is verified, and the round's own "no-harm" statement
should name this as an inherited red.

---

## 2. (b) Uncommitted seat work in `.ufo/waves/round-8*/` — round 80 is clean, round 81 collides with itself

Round-80 is fully settled, so it cannot collide with r81:

```
$ git ls-files .ufo/waves/round-80 | wc -l                         -> 805
$ git status --porcelain=v1 -uall -- .ufo/waves/round-80 | wc -l    -> 0
$ git status --ignored --porcelain=v1 -- .ufo/waves/round-80
!! .ufo/waves/round-80/build/__pycache__/                          (build-tool cache only)
```

Every r80 prerequisite the r81 seats consume is present: `Kb80E04DeadPointer.patch` (2,274 B) + its report
(24,902 B), `Kb80E05GrammarFix.patch` (7,341 B) + report (7,470 B), `refresh-corpus-baseline.py` (20,188 B),
`run-battery.sh` (12,199 B), `Kb80E15BaselineOrder.md` (7,388 B), `S230.fetch.json` (2,091 B),
`S231.fetch.json` (866 B), plus **30** `Kb80C01C1-canonical-*` control receipts.

Round-81 in flight (untracked, expected) — and it collides with itself. Measured in a base clone
(`/fast/scratch/.../clone` at `b2842231`, toplevel asserted); every patch applies alone with exit 0:

| pair | result |
|---|---|
| `Kb81S05SourcesEdits.patch` → check `Kb81S16CensusLog-SOURCES-rows.patch` | **exit 1** (`patch failed: corpus/SOURCES.md:186`) |
| `Kb81S16…` → check `Kb81S05…` | **exit 1** |
| `Kb81E12Census-derived-alternative.patch` → check `Kb81S05…` / `Kb81S16…` | **exit 1** / **exit 1** |
| `Kb81S08ReadmeRows.patch` → check `Kb81E04Baseline.patch` | **exit 1** |
| `Kb81E04Baseline.patch` → check `Kb81S08ReadmeRows.patch` | **exit 1** |
| `Kb81S08ReadmeRows.stageA.patch` → check `Kb81S08ReadmeRows.patch` | **exit 1** |
| `Kb81E04Baseline.patch` → check `Kb81E04Baseline.disposition-only.patch` | **exit 1** (both create `dispositions/wapes.txt`) |

So there are three rival `corpus/SOURCES.md` patches (S05, S16, E12 — E12 additionally ships the entry, the
lesson and `verifiers/external-commits.json`), three rival `corpus/README.md` patches
(E04Baseline, S08, S08.stageA — stageA and its final are one seat's two stages) and two rival
`dispositions/wapes.txt` creators. Exactly one of each may land.

A measured compatible chain exists — these six apply in order, all exit 0 (`chain_ok=1`):

```
Kb81E12Census-derived-alternative.patch
Kb81E02Independent.patch          (+247/-18 lines in verifiers/verify_corpus_independent.py)
Kb81S09SkillRule-SKILL.patch
Kb81S10Province.patch
Kb81S08ReadmeRows.patch
Kb81E04Baseline.disposition-only.patch
```

`Kb81E01Integrity.patch` was **absent** at sweep time (23:29–23:40). Consequence: (i) E6's
`INSTRUMENT_PINS` list cannot be finalised, since the second reviewed blob does not exist yet; (ii) if E01
also adds `verifiers/external-commits.json`, it collides with E12, which already creates that file — the L1
must re-run `git apply --check` after E01 lands and take one creator.

Divergence inside the duplicated rows (all census-clean individually, so the census will not arbitrate):
`S249` tier **A** (S05) vs **B** (S16) for the same page; `S250` kind **`own-work`** with source "kotoba own
work — git ls-remote …" (S05) vs **`code`** with source "mistralai/mistral-vibe — repository …" (S16). Both
S250 drafts do carry `supersedes S230` in `teaches`, so the census's E04 exemption holds.

---

## 3. (c) Base claim vs git — **true**, with one committed-state hazard

```
$ git rev-parse HEAD master origin/master
b284223105f4d106f7e8f56ed4fd296c643cda0e   (×3)
$ git rev-list --left-right --count origin/master...HEAD
0	0
$ git log --oneline -10
b284223 round-80 verifier spot-check (integrator, hyaku): non-author admit/reject
… (matches the plan's base claim)
$ git status --porcelain=v1 -uall | grep -v '^?? .ufo/waves/round-81/'
?? .ufo/wapes
?? plans/round-81.md
```

`b2842231` really is the tip, ahead/behind 0, and the plan's "one untracked file `.ufo/wapes`" was true at
freeze time (the plan and the round-81 tree are untracked because the L1 has not committed them yet).

Hazard: **HEAD is detached.** `git symbolic-ref -q HEAD` exits 1 and `.git/HEAD` holds the raw sha, while
`master` points at the same commit. A commit made from this state lands off-branch and the next round's base
claim (which reads `origin/master`) would not see it. The r80 integrator evidently lands on `master`
explicitly; the L1 must do the same and verify `git rev-parse master` after landing.

Independent base-truth reproduction (not a re-read of the L1 receipt): scratch clone of the lane at base,
the lane's frozen counter, `--fleet /home/vgpnk/Projects/shokunin`:

```
guards 5 of 5; tip battery exit 0: 4 of 6
exit=1, wall 112.2s
gate verifiers/verify_corpus_integrity.py exit 1
gate verifiers/verify_corpus_independent.py exit 1
(all other four gates exit 0)
```

That is exactly the plan's declared base state, and it confirms the two corpus gates are the only reds —
i.e. C1's do-nothing starting point (`4 of 6`) is real, and the reds are the ones R1/R2 target.

---

## 4. (d) `.ufo/wapes` — probe output, but two of its verdicts are not reproducible

Byte facts: 594 B, ASCII, 5 lines, mtime `2026-10-27T20:17:03-03:00`, owner `vgpnk`, untracked and **not
gitignored** (`git check-ignore -v .ufo/wapes` prints nothing).

```
words=11 ok=False why='quote lies in the first-heading block (Q70)'  quote='allowed-tools No Space-delimited list of pre-approved tools the skill may use.'
words=12 ok=False why='quote lies in the first-heading block (Q70)'  quote='… the skill may use. Experimental'
words=11 ok=False why='quote not found in the text view'  quote='No Space-delimited … allowed-tools'
words=7  ok=False why='quote not found in the text view'  quote='the skill may use. allowed-tools No Space-delimited'
exit=0
```

Classification: the stdout of `verifiers/check_allowed_tools.py`'s `quote_location()` over four candidate
quotes. The message strings are verbatim from that file (lines 1056–1078), the word counts match the quotes
(11/12/11/7), and `S229`'s Microsoft wording ("Space-delimited list of pre-approved tools") identifies the
target page. r80 seats independently recorded it the same way (S06, S17, S11, S02, E02, Y01 all call it a
sibling's typo'd redirect of a Q70 quote probe). Note one inconsistency across those r80 observations: S10,
S08 and S15 describe `.ufo/wapes` as an *empty directory*, others as this 594 B file — unexplained, and not
reproducible now (it is a regular file).

Reproduction (the committed locator on every committed snapshot):

```
$ python3 -B -   # import verifiers/check_allowed_tools.py; view_with_headings + quote_location on each snapshot
snapshots scanned: 87
S229-msaf.html q1: words=11 ok=True  why=None  first_heading_line=38
S229-msaf.html q2: words=12 ok=True  why=None  first_heading_line=38
occurrences in committed snapshots: 2
S229: quote view line 95, first heading line 38 -> Q70 first-heading-block requires line <= 39; observed ok=True
```

So: the two `first-heading block` verdicts **cannot be produced** by the committed instrument on committed
bytes — 0 of 87 snapshots yield them, and the only snapshot containing the quote accepts it (view line 95,
first heading line 38). The two `quote not found` verdicts reproduce exactly (those candidates reorder
fragments and genuinely are absent). The trailing `exit=0` is the probe *driver's* exit and contradicts its
own four `ok=False` lines — the `M80-1` class (a verdict read from the loop, not from the check).

This matters because the disposition is already drafted: `Kb81E04Baseline.patch` and
`Kb81E04Baseline.disposition-only.patch` both create `.ufo/waves/round-81/dispositions/wapes.txt` with those
five lines **verbatim**. Committed as-is, the round would enshrine (i) a verdict the committed instrument
cannot produce and (ii) an `exit=0` that reads as a passing quote check, under a plan sentence that calls the
file "committed evidence of the disposition". The disposition itself is right; the evidence framing is not.

Smallest remediation: keep the bytes, and ship an adjacent note with the sha256, the mtime, the reproduction
result above and the sentence "`exit=0` is the probe driver's exit, not a quote-check verdict" — or
disposition as deletion with that note. Never cite the file as evidence that a quote passed.

---

## 5. (e) Any lane file touched after base by a non-r81 process — **no**

```
$ find . -path ./.git -prune -o -path ./.jj -prune -o -path ./.ufo/waves/round-81 -prune \
       -o -type f -newermt "2026-10-27T23:05:39-03:00" -print      # base commit time
./verifiers/__pycache__/check_allowed_tools.cpython-314.pyc   2026-10-27 23:32:02
./plans/round-81.md                                           2026-10-27 23:18:19
```

Exactly two files, both attributable:

1. `plans/round-81.md` — the L1's own plan (r81 process), untracked by design.
2. `verifiers/__pycache__/check_allowed_tools.cpython-314.pyc` — **written by this seat** (see § 7). It is
   inside a gitignored directory (`!! verifiers/__pycache__/`, `git ls-files verifiers/__pycache__` → 0), so
   no tracked byte changed.

`.jj` churn is the base commit itself, not concurrent activity: 29 files newer than base, all stamped
`23:05:39.x`, and **0** newer than `23:10`. Conclusion: no non-r81 writer touched the lane after base.

---

## 6. Cross-cutting harm found outside the assigned list

### 6.1 E6's cap is already exceeded — this decides C1 (high)

`check_tip_battery.py`'s `instrument-size` guard sums added lines over the six `BATTERY` scripts between the
pinned r73 base `072048fa` and the measured rev (code at lines 304–320). `BATTERY` (lines 145–152) includes
`verify_corpus_integrity.py` and `verify_corpus_independent.py` — the two files R1/R2 repair. Measured with
the guard's own command on a committed scratch chain (`E12 + E02`):

```
$ git -C <clone> diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 <chain> -- <six scripts>
22	3	verifiers/check_assertion_floors.py        # the pre-existing base delta, matches the base receipt
247	18	verifiers/verify_corpus_independent.py      # Kb81E02Independent.patch
=> added 269, deleted 21
```

E6 raises `LINE_CAP` 40 → **140**; the base already spends 22, so a new repair has 118 lines of headroom.
The published E02 blob alone spends 247 (129 over headroom, 2.1× the whole cap), and `verify_corpus_integrity.py`
has not been patched yet (E01 absent), so the real total is ≥ 269. Under E6 the guard prints
`instruments gain 269 lines > 140`, i.e. **`guards 5 of 5` is unattainable** and the frozen C1 predicate
(`guards 5 of 5` **and** `tip battery exit 0: 6 of 6`, exit 0, both forms) cannot be met with this blob.

The plan's own kill rule reads: C1 stops as an honest stop if "the reviewed instrument patches' combined
added lines exceed the declared cap arithmetic (40 base-spent + measured added ≤ 140)". By the published
numbers it does. Two honest exits: shrink the repair to ≤ 118 added lines total, or (if the round wants the
larger blob) record the cap arithmetic as broken and stop C1 as declared — a post-data cap raise would be the
narrowing the plan forbids. This receives a reviewer seat's attention too (`Kb81V01C1`), but it is arithmetic,
not judgement: it should not wait for the review.

Re-measure after any revision:

```
git -C <clone> diff --numstat 072048fa8e8a52c707d25f7079772fa317244eb7 <tip> -- \
  verifiers/check_gate_registry.py verifiers/check_assertion_floors.py verifiers/verify_skill_checklist.py \
  verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py verifiers/check_correction_sweep.py \
  | awk -F'\t' '{a+=$1;d+=$2} END{print "added",a,"deleted",d}'
```

### 6.2 C2's S249 duplicates S248's URL — a frozen predicate that mandates a duplicate (medium)

`S248` (line 189, status `queued`, `used-by —`) already is the Agent SDK skills page, with the same fetch
record the plan hands to `S249` (28395 B, sha256 `ac62c2df…`, lines 348/389). C2's conjunct (b) requires a
*new* row S249 carrying that same URL, and conjunct (e) requires S248's `used-by` to name the new entry.
Census decision table, measured on a fixture that reproduces the lane exactly (base corpus + one synthetic
row inserted inside the registry table):

| variant | census |
|---|---|
| base (no row) | exit 0, `ok`, **31** `W04` duplicate-url warnings |
| S249, URL + **S248's scope cell verbatim**, `teaches` without `supersedes S248` | **exit 1, `E04 duplicate url … within scope`** |
| S249, same URL, **distinct** scope | exit 0, **+1** `W04` (31 → 32) |
| S249, same URL + same scope + `teaches` begins `supersedes S248 —` | exit 0, **no new line** |
| S250 (R5), S230's URL + scope + `teaches` begins `supersedes S230 —` | exit 0, **no new line** |

Rule source: `scripts/sources-census.sh:646-651` — same URL **and** same scope, both non-rejected, `teaches`
lacking `supersedes S<nnn>` ⇒ `E04` (error); differing scope ⇒ `W04` (warning). So an author who reuses
S248's scope text — the natural way to describe the same page's teaching — turns the plan's own no-harm
battery red. Both shipped drafts chose distinct scopes and each adds exactly one new `W04`
(`S249 duplicate url code.claude.com/docs/en/agent-sdk/skills.md across scopes`), so R5 (`S250`) is clean and
C2 is viable, but the duplicate row is real and the lesson should declare the new warning.

### 6.3 The corpus status invariant is broken by every SOURCES draft (medium)

Measured over all 174 registry rows at base: 8 `queued`, 149 `mined`; **every** queued row carries
`used-by —` (8/8) and **no** mined row does (0/149). Both drafts rewrite S248 to `status queued` **with**
`used-by corpus/knowledge/allowed-tools-sdk-round81.md` (S16 adds `corpus/lessons/round-81.md`). That is the
corpus's first "queued but used" row — a row whose status contradicts its own citation — and no census rule
(E01–E12, W01–W04) catches it. Smallest fix: mine S248 (`queued→mined`, `used-by` = entry) and let S249 own
the SDK channel; or leave S248 `queued` with `used-by —` and accept that conjunct (e) cannot be satisfied as
written (which is itself a plan-level decision for the L1, not a seat's).

---

## 7. Own defects and corrections

- **I wrote a lane byte.** Importing `verifiers/check_allowed_tools.py` with `importlib` (no `-B`) refreshed
  `verifiers/__pycache__/check_allowed_tools.cpython-314.pyc` at `23:32:02`. The directory is gitignored and
  has 0 tracked files, so no committed byte changed; I left it rather than delete a cache other gate runs may
  have shared. It is visible in § 5's sweep and is named here rather than hidden.
- **First mtime sweep was wrong.** `find -newermt "2026-10-27 23:05:39 -0300"` is unparseable by this
  `find`; it printed an error to stderr and 0 lines on stdout, and my first read reported "0 files". The
  ISO form `2026-10-27T23:05:39-03:00` returns **2**. The receipt keeps the corrected command and both values
  are reconciled in § 5.
- **One receipt was damaged by a heredoc.** An unquoted heredoc interpreted two backticked words as command
  substitution (`error: command not found: code`). The file was rewritten with a quoted heredoc; the current
  `Kb81N01Sentinel-patch-composition.txt` is the clean version.
- **Fixture false positive, fixed before use.** The first census fixture lacked `SKILL.md`, which produced
  two `E11` errors that looked like lane findings. After copying `SKILL.md`/`PROVINCE.md`/`README.md` the
  fixture reproduces the lane exactly (exit 0, 31 `W04`, `ok`), and only then were the variants scored.
- Scratch: `/fast/scratch/hyaku/kotoba-r81/Kb81N01Sentinel/` — removed at the end of this seat; all receipts
  were copied into the build dir first.
- Tooling: **nothing installed or upgraded**; `pacman` untouched (host-wide pause). No background job beyond
  the one 112 s tip-battery run, which I started and completed.

---

## 8. Commands (as run, condensed)

```
cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
python3 -B verifiers/check_substrate_pins.py                              # exit 2
python3 -B verifiers/verify_harness_claims.py                             # exit 2
python3 -B verifiers/check_substrate_repin_v2.py --rev b2842231…          # exit 2
sha256sum /home/vgpnk/.local/bin/omp; stat -c '%n %s %y' …; …/omp --version   # ee2961c7…, 18.13.1
git rev-parse HEAD master origin/master; git symbolic-ref -q HEAD; cat .git/HEAD
git rev-list --left-right --count origin/master...HEAD                    # 0 0
/tmp-free scratch: git clone --shared … && git checkout b2842231… && toplevel assert
python3 -B <lane>/verifiers/check_tip_battery.py --repo <clone> --rev b2842231… --fleet …   # 4 of 6, exit 1
./scripts/sources-census.sh validate --root <fixture> kotoba               # base 0 / A1 1 (E04) / A2,A3,D 0
git -C <clone> apply --check <each patch>; apply <a>; apply --check <b>     # collision matrix
git -C <clone> diff --numstat 072048fa… <chain> -- <six instruments>       # 22+247 = 269 added
python3 -B -  # quote_location over 87 committed snapshots                 # 0/87 first-heading-block
```

---

## 9. What the L1 should do with this, in order

1. **Before claiming C1**: run the § 6.1 re-measure on the final tip. If added > 140 the claim stops by its
   own kill rule — record that, do not raise the cap.
2. **Integration**: pick one of {S05, S16, E12} for SOURCES, one of {E04Baseline, S08, S08.stageA} for
   README, one of {E04Baseline, E04Baseline.disposition-only} for `wapes.txt`; the § 2 chain is a measured
   compatible set. Re-check composition once `Kb81E01Integrity.patch` lands.
3. **R3**: commit the wapes bytes only with the reproduction note; it is not evidence of a passing quote.
4. **S248/S249**: decide `queued→mined` on S248 rather than shipping a queued row with a `used-by`; declare
   the new `W04` in the census-after receipt and the lesson.
5. **Commit on `master`**, not the detached HEAD, then verify `git rev-parse master`.
6. **Say out loud** in the round record: the host substrate drifted at `2026-10-27T00:02` (omp 18.12.6 →
   18.13.1, `omp.real` gone), three substrate instruments are red at base, and no r81 gate covers them.

VERDICT: No r81-caused lane mutation found (round-80 fully settled; only two post-base files, both attributable), and the plan's base claim reproduces exactly (`4 of 6`, exit 1) — but four live hazards stand: the published C1 repair adds 269 instrument lines against E6's cap of 140, three SOURCES and three README patches are mutually exclusive, the wapes transcript ships two verdicts no committed byte supports, and the host omp pin drifted to a path that no longer exists with no gate covering it.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81N01Sentinel.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-substrate-pins-base.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-gitstate.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-tipbase.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-wapes-repro.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-collisions.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-patch-composition.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-e6-cap-arithmetic.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-sources-invariant.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-decision-table.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-base2.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-A1_samescope.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-A2_newscope.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-A3_supersedes.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-D_s250_supersedes230.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-patchS05.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81N01Sentinel-census-patchS16.txt
