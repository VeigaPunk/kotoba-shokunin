# RevNoHarm — kotoba round 65 wave 1

role: reviewer (leaf — no subagent dispatch)
item: re-run the noharm battery at the tip; confirm no prior gate regressed; audit the
SCORECARD/LOG/SHONEN diff for append-only (except the recorded Next-block rename and the
SHONEN evidence refresh)
judged on: calibration
tools installed: none (python3 3.14.8 stdlib present; pacman paused, no install needed)
production edits: none — this file only; all scratch under `/tmp`; no `git`/`jj` write, no
checkout, no lane file touched (lane working copy entered dirty with two peer
`swarm-registry.json` edits and round-66 untracked seat reports; left as found)

Axes named: **calibration** (this seat). The bound below must not move **depth** (C1: v32 234,
floors row) or **consistency** (C2: checklist 1862 / `governance.citation_resolves` /
`GOVERNANCE_CORRECTIONS`).

## 0. The one methodology fact that changes the answer

`0e104f49` is **no longer the lane tip**. Measured state on entry:

```
$ jj log -r @         → 2d2a13cdcd65 (no description set)   # empty working copy
$ jj log -r @-        → 2a8eba56 master | round-66 verifier spot-check (integrator, hyaku)
$ jj log c98d137::@   → 0e104f49 is the round-65 tip, 6 commits behind @
```

So the battery cannot be run in place: the working tree carries round-66 bytes. Verified drift:

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test      # LIVE working tree
self-test: 0 failure(s) over 240 assertions                       # exit 0  (not 234)
$ python3 -B verifiers/verify_skill_checklist.py --json           # LIVE working tree
pass 11 fail 0                                                    # exit 0
```

Every number in this report is measured at **`0e104f498b3df1466284074c5b3a6e5b523420cd`**
(round-65 tip) in scratch trees, base control at
**`c98d1378236bae56d9d2ecacd5db59a4cc142e1e`**:

* tip: `git clone --shared --no-checkout` → `checkout --detach 0e104f49`, parent directory
  exposing the fleet root's entries (`/tmp/r65`), tree content verified equal to `git archive
  0e104f49` (`/tmp/r65rev/tree`, used for the path-independent arms).
* base: same construction at `c98d137` in a fresh unique parent (`/tmp/rb-…`, path in
  `/tmp/rb-path.txt`) after a first mirror was found polluted (`/tmp/r65base/.ufo` was a real
  directory, not the fleet symlink — that run is discarded, not cited).
* clones are read-only consumers of the lane's object store; the lane repo was never checked
  out, written, or `jj`-mutated.

## 1. Battery at the tip — every named arm reproduced

| # | arm | command (cwd = tip tree) | exit | observed |
|---|---|---|---|---|
| 1 | v32 | `python3 -B verifiers/check_scoped_rules_v32.py --self-test` | **0** | `worlds reject 7 of 7; eligible rows pass 4 of 4` / `survivors closed 6 of 6` / `self-test: 0 failure(s) over 234 assertions`; instrument sha256 `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d` (= receipt pin) |
| 2 | checklist | `python3 -B verifiers/verify_skill_checklist.py --json` | **0** | `pass 11 fail 0 na 0`, `"exit_code": 0`; `governance.citation_resolves` PASS, `1197 token(s) … 10 quoted, 3 schematic excluded, 1 recorded absence excused, 3 recorded correction(s) excused` |
| 2b | checklist self-test | `… --self-test` | **0** | `0 failure(s) over 1862 assertions` (= new floor) |
| 3 | r64 counter | `python3 -B verifiers/check_r64_routed_repairs.py --self-test` | **0** | `self-test: 0 failure(s) over 43 assertions`; `--rev 0e104f49` prints `r63 routed defects closed 4 of 4` |
| 4 | r63 counter | `python3 -B verifiers/check_r63_routed_repairs.py --rev 0e104f49 --root <tip>` | **0** | `r62 routed defects closed 5 of 5` (`PASS append-only prefix=True grew_by=56`; `PASS noharm-arms-named LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)`) |
| 4b | r63 self-test | `… --self-test` | **0** | `0 failure(s) over 23 assertions` |
| 5 | gate registry | `python3 -B verifiers/check_gate_registry.py --rev 0e104f49` | **0** | `gate registry rows conformant 42 of 42 lane verifiers; phantom 0` |
| 6 | census | `scripts/sources-census.sh census --root /tmp/r65 kotoba` | **0** | `rows 119`, `tier.A 116 / B 2 / C 1`, `mined 111 / queued 7 / rejected 1`, `missing 0` |
| 6b | census validate | `… validate --root /tmp/r65 kotoba` | **0** | 16 × `W04`, then `ok …/corpus/SOURCES.md` |
| 7 | sources append-only | `python3 -B verifiers/check_sources_append_only.py --rev 0e104f49 --base c98d137 --repo <tip>` | **0** | `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes` |
| 7b | sources self-test | `… --self-test` | **0** | `0 failure(s) over 21 assertions` |
| 8 | floors | `python3 -B verifiers/check_assertion_floors.py` | **0** | 15 rows, `scoped_rules_v32 observed=234 floor=234`, `checklist observed=1862 floor=1862` |

Extra receipts I ran because they are the corpus of "prior gates":

| arm | exit | observed |
|---|---|---|
| `check_scoped_rules_v31.py --self-test` | 0 | `survivors closed 5 of 6`, `201 assertions` (the plan's §9 control text) |
| `verify_corpus_integrity.py --json` | **1** | 9 results; `corpus.index.tracked_files` DRIFT 115/81, `corpus.index.unindexed` DRIFT 3/0, `corpus.pointers.report_total` DRIFT 76/51 |
| `verify_corpus_independent.py` | **1** | same `!` warns as base (`cfb894a5`, `round-N`), `tracked_files=115 unindexed=3` |
| `verify_surfaces.py` | **1** | `FAIL surfaces.literal_present` (31 loader literals), `FAIL surfaces.no_uncovered_class` |
| `check_substrate_pins.py` | **1** | `DRIFT 2/3 pins failed: omp_binary_sha256, omp_binary_mtime` (host binary moved) |

## 2. No prior gate regressed — base `c98d137` → tip `0e104f49`

Floors walk at each rev (same host, same interpreter, same mirror shape):

```
base: exit 0, 14 instruments, checklist 1852/1852, no scoped_rules_v32 row
tip : exit 0, 15 instruments, checklist 1862/1862, scoped_rules_v32 234/234
```

Per-instrument observed counts, base → tip (all from the two floors walks): harness 10→10,
corpus_integrity 152→152, corpus_independent 99→99, surfaces 175→175, pins 62→62,
harness_independent 123→123, compare_harness_independent 330→330, floors_guard 165→165,
dispatch_prompts 56→56, sibling_census 68→68, overlap_levers 55→55, alwayson 89→89,
correction_sweep 25→25, checklist 1852→1862, scoped_rules_v32 absent→234. **No count fell.**

Floors registry is the out-of-file anchor, so I compared it *semantically*, not textually:

```
$ python3 - (json.load of git show <rev>:verifiers/floors-registry.json)
total 14 -> 15
removed []  added ['scoped_rules_v32']
CHANGED checklist {floor 1852} -> {floor 1862}
comment_identical True        extra keys a [] b []
```

Checklist arms, base vs tip, `(status, evaluated)` per id: ten of eleven identical
(41/4/1/1/1/2/599/532/36/161); only `governance.citation_resolves` moved, **FAIL ev=1195 →
PASS ev=1197**. The base failure names exactly the three plan cells:

```
$ … --json   @ c98d137   → exit 1, pass 10 fail 1
governance.citation_resolves FAIL :: LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not
 resolve …; LOG.md:2580: '.ufo/watchdog.log' does not resolve …; SCORECARD.md:158:
 '.ufo/reports/round-60/kotoba.md' does not resolve …
```

Other prior gates, base vs tip:

| gate | base `c98d137` | tip `0e104f49` |
|---|---|---|
| v32 self-test | 223, exit 0, sha `f8f69cad…` | 234, exit 0, sha `b6cfc764…` |
| gate registry | 42 of 42, exit 0 | 42 of 42, exit 0 |
| r64 counter self-test | 43 assertions, exit 0 | 43 assertions, exit 0 |
| r63 counter `--rev` | n/a (rev-specific) | 5 of 5, exit 0 |
| census rows | 118 (A115/B2/C1), 16 W04, exit 0 | 119 (A116/B2/C1), 16 W04, exit 0 |
| `verify_surfaces.py` | exit 1 | exit 1 — output **byte-identical** after path normalization |
| `check_substrate_pins.py` | exit 1 | exit 1 — output **byte-identical** |
| `verify_corpus_integrity.py` | exit 1, same 3 DRIFT rows | exit 1, same 3 DRIFT rows; only observation `tracked_files 113→115` |
| `verify_corpus_independent.py` | exit 1, same warns | exit 1, same warns; `tracked_files 113→115` |

Conclusion: **no prior gate regressed.** The four reds at the tip are pre-existing at the base
with identical verdicts (two of them byte-identical) and are environment/baseline debt, not
round-65 movement. Read with §5 F5: *floors green ≠ every gate green*.

## 3. Write-scope audit — append-only, with the two recorded exceptions

```
$ git diff --numstat c98d137..0e104f49      # 25 files, +4311 / −74
deletions exist in 5 files only:
3 1   SCORECARD.md
1 1   SHONEN.md
19 6  verifiers/check_assertion_floors.py
63 59 verifiers/floors-registry.json
156 7 verifiers/verify_skill_checklist.py
```

* `LOG.md` **8 insertions, 0 deletions**, hunk `@@ -2613,2 +2613,10 @@`, file 2614 → 2622
  lines: appended at EOF under `## 2026-10-24 — Round 65`. Nothing above line 2615 changed.
* `SCORECARD.md` **3 insertions, 1 deletion**: the single deletion is line 371,
  `**Next: round 65** …` → `**Next: round 66** …` (the recorded rename), plus two appended
  annotation lines. I checked the rename is *content-preserving item by item*, not just
  "not a deletion": A2's F6 compound-purpose bound carried; v33 candidates (MIN_SHARED,
  `-and-`/quote/relatedness) carried verbatim; the r64 C2 bound (4 routed instances of the M95
  class) carried; the full carry-forward quality-debt tail (SentBounds, helper-invocation
  receipts, r62 dispositions remainder incl. `LOG.md:2549`, r61 R-b corpus-idx, the S120
  sources-gate breach + the supersede-row alternative) carried; and the three consumed items
  are each *named as consumed* (W8 escape class, M7–M22 judge lanes, v32 floors row at 234,
  the governance red) — no debt item vanished silently.
* `SHONEN.md` **1 insertion, 1 deletion**: the evidence line only, and the diff is exactly the
  recorded refresh — `; 18 at \`80bb8921\` (re-count this round)` inserted and the registry rev
  `c019919c…` → `80bb8921…`. `gate registry … 42 of 42` is true at both revs (§2).
* `verifiers/verify_skill_checklist.py` 7 deletions are signature/docstring/format
  adaptations (`horizon:` default, context string, one call site gaining
  `corrections=GOVERNANCE_CORRECTIONS`); **no check arm is removed**.
* `verifiers/check_assertion_floors.py` 6 deletions are the old `1852` values, the old
  `instrument_total: 14` swap string, and docstring numbers.
* `verifiers/floors-registry.json` 59 deletions are a **whole-file re-indent** (1-space →
  2-space); the parsed diff is exactly §2's two changes. Benign, but it makes a 2-line bump
  a 122-line diff.

## 4. Is C2's pass load-bearing? (do-nothing control, tip tree, corrections disabled)

```
check_governance_citations(<tip>, corrections=())   # default ()
→ FAIL evaluated 1200
  LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve …
  LOG.md:2580: '.ufo/watchdog.log' does not resolve …
  SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve …
  0 recorded correction(s) excused
```

So the 11/11 is produced by the excusal mechanism, not by any unrelated change that made the
old cells resolve (LOG is append-only; the stale cells are still there). Independent guard
battery on the real code, my own synthetic worlds (`/tmp/probe_corrections*.py`, `errata=()`,
`horizon=0` to keep the live errata row out):

```
A no corrections (control red)                FAIL ev=3   both red tokens named
B good correction, second red token same line FAIL ev=2   also-missing.md still red  ← never-masks holds
C drifted pinned line sha                     FAIL      "line text drifted"
D dead corrected token, wording on the line   FAIL      "corrected token '../dead.md' does not resolve"
E subject not on the named line               FAIL      "names no live red subject"
F correction aimed at the *other* red token   FAIL      "correction wording not on the line" + other red
G row past horizon                            FAIL      "past horizon 1 or absent"
H stale token restored (now resolves)         FAIL      "stale, the old token now resolves"
I wording absent from the pinned line         FAIL      "past horizon 2 or absent" (row aimed at line 3)
```

Every fail-closed arm fires; the duplicate-row case dedups to one excusal; and the anti-vacuity
guard (`evaluated == 0` → FAIL) bites when a correction would excuse the last subject.

## 5. Findings (severity ordered)

**F1 — LOW/MED (calibration) — the census "after" receipt cannot distinguish before from
after; the claim itself is true.** `census-before.txt` and `census-after.txt` are byte
identical (`md5 4712924ae2a105333d479906cfab9fd0`, both 1569 B), and `validate` output carries
no row count, so the committed after-receipt is satisfied by a do-nothing round. The lesson
defers the after-measurement to "the report" (`corpus/lessons/round-65.md` §Gate, "After: run
at round end (appended below when run; the report carries it)"), but no `.ufo/reports/round-65/`
directory exists anywhere in the lane history (`git log --all -- .ufo/reports/round-65/` → no
commits) and no after-line was appended to the lesson. The underlying claim is nevertheless
**verified independently**: rows 118 → 119, tier.A 115 → 116, 16 W04 both sides, exit 0 both
sides (§1, §2). Fix is a one-line append: the `census`-mode before/after row counts, rev-named.
Corroborates `ScribeCensusCheck.md`; I claim only the extra fact that the lesson's deferral
target does not exist.

**F2 — LOW (calibration) — the committed noharm receipt names 5 of the 9 arms the wave spec
requires.** `receipts/noharm-tip.txt` records v32, checklist, r64, r63, gate registry. The
spec item (`.ufo/waves/round-65/w1-spec.json`, item `RevNoHarm`) also names **census** and
**sources append-only over c98d137..tip**; floors lives in a separate file
(`FLOORS-noharm.txt`). Both missing arms are green when run (§1 rows 6/7), and no harness is
committed (`find . -maxdepth 4 -name 'noharm*'` → nothing; the LOG's earlier rounds cite a
`noharm-battery.sh` that is not in this repo), so the battery is not one reproducible command.

**F3 — LOW (calibration) — `REGRESSION-probes.txt` records a non-result.**
`corpus_integrity exit None fail None`: the instrument's JSON has keys
`observed`/`results` only, so the probe read absent keys and printed `None` twice. I re-derived
the state it was meant to capture: exit **1** at *both* revs, with the identical three DRIFT
rows (only the `tracked_files` observation moves, 113 → 115). The commit message's
"corpus_integrity red pre-existing identical at base c98d137" is therefore *true* but is not
what the receipt shows. (Same defect class as `RevReceiptRevs.md` F6; independent repro here.)

**F4 — INFO — the 11/11 is conditional on the lane's *parent contents*, not on the lane
alone.** Isolated `git archive` export → `pass 8 fail 3`
(`trigger.name_directory` "directory 'tree'", `trigger.citation_resolves` on
`../.ufo/reports/round-7/kotoba.md`, `governance.citation_resolves` on the three corrected
tokens and 9 more `../` tokens). With a parent exposing the fleet root's entries (symlinks to
`.ufo`, `PROTOCOL.md`, `AXES.md`, `kasegi-shokunin/…`, siblings) and the directory named
`kotoba-shokunin` → 11/11. Refinement of `RevReceiptRevs.md`'s note: the precondition is the
fleet root's **contents** as the lane's parent, *not* the literal `/home/vgpnk/…` path — a
content-complete mirror reproduces `fail: 0`, so a CI shape is possible; round 65 adds three
new fleet-ancestor dependencies through the corrections and no receipt states the condition.

**F5 — INFO — "floors exit 0" must not be read as "all gates green".**
`check_assertion_floors.py` grades assertion **counts**; at the tip three instruments are red
by verdict while their counts pass: `verify_corpus_integrity` (exit 1, tracked_files/unindexed/
report_total DRIFT), `verify_corpus_independent` (exit 1, two `!` warns), `verify_surfaces`
(exit 1, 2 FAILs), `check_substrate_pins` (exit 1, host omp binary sha+mtime). All four are
identical at the base (§2), so no regression — but the two-receipt "no-harm" story is only
about floors + the five named arms.

**F6 — INFO — SCORECARD/SHONEN are undeclared surfaces.** `plans/round-65.md` declares the
verifier/registry/LOG surfaces and the frontier files; it does not declare the SCORECARD
Next-block rename/annotation or the SHONEN refresh, and the LOG's round-65 entry records only
the citation corrections. The "recorded" record for those two is the `0e104f49` commit
message. Content-wise I found nothing to object to (§3); this is a traceability note, and the
plan-vs-landing surface delta is exactly the two files.

## 6. Claims supported / falsified

* **C1 counted predicate (arms 1–3 of the sentence)** — SUPPORTED at `0e104f49`: the three
  predicate lines print, `N = 234`, exit 0; the floors row registers v32 at floor 234. The
  kill conjunct (each SM/M lane exits 1 with arm attribution) was **not** run by me — C1
  owners hold it.
* **C2 counted predicate** — SUPPORTED: `"fail": 0`, exit 0 (11/11) at the tip, `fail: 1` /
  exit 1 at the base, `governance.citation_resolves` PASS; floor 1852 → 1862 bumped in the
  registry, both guard tables and the docstring in the same change (§2, semantic diff).
* **"No prior gate regressed"** — SUPPORTED (§2), with the red-set caveat F5.
* **"SCORECARD/LOG append-only except the recorded Next-block rename and the SHONEN evidence
  refresh"** — SUPPORTED structurally (0 deletions in LOG; exactly 1 in SCORECARD at the Next
  line; exactly 1 in SHONEN at the evidence line) and content-wise (no debt item lost in the
  rename; the SHONEN delta is exactly the two recorded refreshes).
* **Census 118 → 119, exit 0** — SUPPORTED as a measurement, NOT evidenced by the committed
  after-receipt (F1).
* **S121 row integrity (spot check, as the receipt's frontier claim touches the battery's
  census arm)** — SUPPORTED: snapshot `S121.pdf` sha256
  `bad1b681b1d6d6cea09f0c1e4701618b88dc175b713689c2a6ac43aba07418a3`, 1,126,684 B; gate quote
  occurs **once** whitespace-normalized, 16 words (extract lines 64–65); support quote occurs
  once, 24 words, at extract lines **1174–1176** (the row's anchor is correct); DOI
  `10.1109/TSE.2013.44` at extract line 90; the row's six columns parse as one 11-cell row and
  census E11 passes.
* Nothing falsified. Two claims are *true but under-receipted* (F1, F3).

## 7. Residual risk / verification gaps

1. **Existence-only corrected token** (corroborates `RevC2Mechanism.md` F6). Demonstrated on
   the real code: a correction whose corrected token is an unrelated *existing* file yields
   `PASS` (`/tmp/probe_equiv.py`: "SEMANTIC-MISMATCH correction … PASS evaluated 1"). The
   three landed corrections are substantively right (I checked the corrected paths are the
   documents named: the fleet round-60 report and the fleet watchdog log), so this is a
   future-use hazard, not a defect in this landing.
2. **Corrections shrink the checked universe by 3** (evaluated 1200 raw → 1197). Each excused
   cell's replacement is separately resolved, and the anti-vacuity arm prevents excusing
   everything, but a long series of corrections monotonically reduces what the gate checks.
   No cap exists; only the `evaluated == 0` floor.
3. **Backtick hazard is real, not retired** (`M100`, `receipts/C2-selfreference-redbefore.txt`):
   a *future* notice that quotes the stale token in backticks re-imports it as a red subject
   and fails the gate. Fail-closed (safe) but it will look like a regression to the next seat.
4. **I measured mirrors, not the live lane.** Tree content is verified identical at the rev,
   and `repo.resolve()` was mirrored (the clone path is a real directory under a real parent),
   but the fleet parent is symlinked, not native. The in-lane numbers I *did* take (live
   working tree) are round-66's: v32 240, checklist 11/11.
5. **Kill conjunct not run** (C1 SM1–SM6/M7–M22 attribution) and **the C2 self-test's internal
   arm list not re-derived** — both out of this lane's scope and owned by C1/C2 reviewers.
6. `md5` identity of the two census files is a hash of the committed bytes at the tip; the
   base-side file was never re-run by me (it is a 118-row tree and would produce the same
   bytes by construction, which is the point of F1).
