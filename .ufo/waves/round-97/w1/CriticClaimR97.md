# CriticClaimR97 — falsification of C1 and C2 on the full round-97 candidate

Seat: CriticClaimR97 (critic, wave r97-w1; leaf, no subagent dispatch). Scope: attack the two frozen
claims against the candidate `148395bf42af97436b1b832a97a175515f981939` + `ExecArmsR97.patch` +
`ScribeCorpusR97.patch`; re-run the do-nothing controls; answer the attack questions. I do not judge,
admit, edit, integrate or ship. I write only this file and my own receipts under
`.ufo/waves/round-97/w1/CriticClaimR97/`.

## Candidate

Built in my scratch clone `/fast/scratch/hyaku/kotoba-r97/CriticClaimR97/repo` (clone of the lane at
the freeze commit; `git rev-parse --show-toplevel` asserted equal to the clone root before any write):

- `git apply` ExecArmsR97.patch (sha256 `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80`,
  equal to `ExecArmsR97_READY`) and ScribeCorpusR97.patch (sha256
  `3f2712c471c814b31300af5caf7df59a8de8aac8f24cb3a77c184e94681b4902`, equal to
  `ScribeCorpusR97_READY`); both `git apply --check` clean on a fresh clone at the freeze commit.
- Committed under `scratch <scratch@invalid>`: candidate **`962f8c409fe19daa33e91f8ae48ca1e06b39123b`**,
  `git diff --stat 148395bf..HEAD` = 4 files, 413 insertions (instrument +231, lesson +179,
  SOURCES +2, README +1).
- Independent production-identity check on the candidate instrument: base 64051 B, candidate 77704 B,
  common prefix 54060 B, common suffix 9989 B, inserted 13653 B; `base[:p]+ins+base[-s:] == cand`
  **True**; `cand[:p]+cand[-s:] == base` **True**; the insertion lies after `def self_test() -> int:`
  and before the `for f in failures:` tail; **0** inserted lines at column 0. Production code outside
  `self_test()` is byte-identical.

## Verdicts

| claim | verdict | basis |
|---|---|---|
| C1 | **MET** | candidate c1 v5: `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13` / `C1-PREDICATE-MET`, rc 0; candidate c1 v4 also MET; r96c1 and r95c1 MET; box proof 2 |
| C2 | **MET (predicate), bounded** | C2 v5 at the freeze commit (counter bytes identical to the candidate's) reads `forgeries refused 3 of 3; honest held 2 of 2`, `C2-PREDICATE-MET`, rc 0; the cause control v5-as-v4 reads 0 of 3; **but** two new no-arm worlds (g10, g11-seeded) read MET — disclosed findings D1/D2, not rescues |

## Do-nothing controls (re-run; pre-data receipts reproduce)

| control | command | observed | receipt |
|---|---|---|---|
| C1 at base | `selftest-kills.py c1 fa1bebae…` | `C1 targets killed 0 of 13 (run errors 0); … C1-PREDICATE-UNMET`, rc 1 | `do-nothing-c1-base.txt` |
| C2 v4 | `forgery-controls.py v4 148395bf…` | `C2 v4: forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-UNMET`, rc 1 | `do-nothing-c2-v4.txt` |
| C2 v5-as-v4 | `forgery-controls.py v5-as-v4 148395bf…` | `C2 v5-as-v4: forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-UNMET`, rc 1 | `do-nothing-c2-v5-as-v4.txt` |

All three reproduce the frozen pre-data receipts in their decisive lines (`redbefore-c1-base.txt`,
`c2-before-v4.txt`, `c2-v5-as-v4.txt`).

## Candidate readings (my own runs, one counter at a time)

| reading | command | observed | receipt |
|---|---|---|---|
| C1 v5 | `selftest-kills.py c1 962f8c40… "$D"` | `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13` / `C1-PREDICATE-MET`, rc 0; `honest runs CLEAN 3 of 3; mirror runs reported 14 of 14` | `candidate-c1-v5.txt` |
| C1 v4 | `… c1 962f8c40… "$D" --rules v4` | `C1 targets killed 13 of 13 … C1-PREDICATE-MET`, rc 0; `honest runs CLEAN 1 of 1` | `candidate-c1-v4.txt` |
| r96c1 | `… r96c1 962f8c40… "$D"` | `R96C1 targets killed 11 of 11 … R96C1-PREDICATE-MET`, rc 0 | `candidate-r96c1.txt` |
| r95c1 | `… r95c1 962f8c40… "$D"` | `R95C1 targets killed 3 of 3 … R95C1-PREDICATE-MET`, rc 0 | `candidate-r95c1.txt` |
| box proof | `verify_dispatch_prompts.py --box-proof` | `boxes proven 2`, rc 0 | inline |
| honest self-test | `verify_dispatch_prompts.py --self-test` | `0 failure(s) over 105 assertions`, rc 0 | inline |
| C2 v5 | `forgery-controls.py v5 148395bf…` | `C2 v5: forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET`, `C2-PREDICATE-MET`, rc 0 | `candidate-c2-v5.txt` |

The C2 runner's `LANE` is the lane repo, so it cannot read a scratch candidate rev; the assignment
names the freeze commit for this reading, and the counter bytes at the freeze commit are the
candidate's counter bytes (`b4200c52…`, unchanged by either patch).

## Attack answers

### 1. Does a do-nothing or cheaper change meet either target?

**C1: no.** The do-nothing base reads 0 of 13 (reproduced). The candidate adds 27 behavioural
assertions (78 → 105); the counter reads 13 of 13 in my independent run. A source-reading arm cannot
substitute: under v5 the mirror run puts the mutant on disk, so a source reader is CLEAN in the
mirror run and is not KILLED (rule 5). The arms call only production helpers on fixtures (reviewed
statically by ReviewerArmsR97 and by me), so the kill is behavioural.

**C2: no for the committed worlds.** The v4 counter reads 0 of 3; the v5 counter reads 3 of 3
(pre-data `c2-v5.txt`, reproduced at the freeze commit by my `candidate-c2-v5.txt`). The refusal is
not a table/path change: `v5-as-v4` (same file, v4 rules, v4 decoy marker) reads 0 of 3. **But** two
new no-arm worlds (g10, g11-seeded) still read MET under v5, so the v5 fix is not a general no-arm
refusal (D1, D2).

### 2. Is C2 work of this round or a re-labelled instrument (§9)?

The surface moved is the kill-counter instrument itself (v4 → v5), not a product behaviour. §9
(fleet `scripts/hyaku/lane-addendum.md`) says to name the axis by the surface the round changes. The
plan names it `consistency (calibration sub-axis, score 10)`: the instrument's calibration is the
surface, and the v5 rules 4–6 are a real rule change with a cause control, not a relabel. It is
legitimate instrument work, but it is **pre-freeze work**: the counter bytes at the freeze commit
(`b4200c52…`) are the instrument commit's bytes, and the C2 reading is already MET at the freeze
(`receipts/c2-v5.txt`). The wave's C2 seat (ExecForgeryV5) is attack-only; it cannot move the C2
predicate. That is consistent with the plan's disclosure, but it means C2's "landing" reading is a
re-read, not a wave outcome.

### 3. Are C1 and C2 causally separable?

Yes for the C1 predicate: my candidate `--rules v4` run reads 13 of 13 (the round-96 rules, no mirror,
one honest run), and the base v4 receipt reads 0 of 13. The new arms are behavioural, so they kill in
the blind run without the mirror rule. C1's landing reading is under v5, which is *stricter* (mirror +
honest bracket), so C2's hardening cannot manufacture a C1 kill. Conversely, C2's reading does not
depend on the C1 patch: the counter is unchanged by ExecArmsR97, and the C2 runner reads the counter
bytes at the freeze commit. **Caveat:** C1's v4 reading alone would not distinguish a behavioural arm
from a source reader (v4 has no mirror); the v5 reading is the one that carries the anti-sniffing
guarantee. The plan records both; the v5 reading is the load-bearing one.

### 4. Are the thirteen targets real false greens / false reds, or contrived?

Twelve are real verdict errors; one is cosmetic:

| target | class | real? |
|---|---|---|
| t01-rstrip-dot | sentence-final `.` kept in the stem → a valid prose path reads FAIL | real false red |
| t02-empty-baseline | empty baseline → `10**9` bound → any round PASS | real false green |
| t03-fleetroot-stem-pass | fleet-root stem reads PASS instead of N/A → file/check PASS | real false green |
| t04-fleetroot-no-baseline | `.report-baseline` dropped from `lane_kind` → fleet-root role unknown → FAIL | real false red |
| t05-placeholder-empty-angle | `<>` no longer a placeholder → a non-literal path reads PASS | real, low severity (degenerate placeholder) |
| t06-sibling-file-as-lane | a plain FILE `<lane>-shokunin` counts as a repo → sibling-lane | real false green |
| t07-report-regex-noprefix | `.ufo/reports/7/` accepted as a report dir | real false green |
| t08-role-regex-nospace | `round7` read as the role round | real false green, low severity |
| t09-file-note-dropped | per-file `note` never attached | **cosmetic**: the note is written but consumed by no verifier (`grep` over `verifiers/*.py` finds only the writer); no verdict changes |
| t10-unreadable-as-baseline | unreadable baseline → `10**9` bound | real false green |
| t11-lane-kind-legacy-dropped | legacy `.round` dropped → state-stale lane reads unknown → FAIL | real false red |
| t12-finish-single-fail-na | one failing file reads N/A instead of FAIL | real false green (headline) |
| t13-noreport-08-pass | no report path → dir conjunct PASS instead of N/A | real false green |

t09 is the one target that is not a false green/red of the box: it guards an output field with no
consumer. It is a real behavioural difference (the round-96 survivor is non-equivalent), but the
plan's phrase "false greens / false reds" overstates it. This does not affect the predicate (the
mutant is killed behaviourally), only the claim's severity framing.

### 5. Does S273 actually ground C2's rule 4?

S273 (Bazel Test Encyclopedia, HTTP 200, 223640 B, sha256 `6b07e08f…5346`, HTML line 656 heading,
lines 659–661 quote, 21 words) states the test-runner contract: "Tests should create files only
within the directories specified by $TEST_TMPDIR and $TEST_UNDECLARED_OUTPUTS_DIR (if set). These
directories will be initially empty." **I re-opened the page myself** (2026-11-06,
`curl -sS -L -o bazel-test.html` → `http 200 bytes 223640`, sha256
`6b07e08f0f4bae537544eac1afc64d98f0b19a9ae7408b8e6482f56e134d5346` equal; heading line 656; quote
lines 659–661; 21 words). I also re-opened the scout's S274 page
(`https://google.github.io/googletest/advanced.html` → `http 200 bytes 214623`, sha256
`7317f5e7d59afb22c2bd9550122f55b38c60d28865d7522664972769b2fd16c5`; heading line 2110; quote lines
2112–2113; 25 words). Rule 4 gives every counter run a fresh clone, TMPDIR, HOME and
XDG_CACHE_HOME. The quote grounds the *initially empty, per-run private directory* half directly;
the HOME = TEST_TMPDIR half is grounded by the page's env table (line 559, recommended), and the
"no constant path is exclusive" bound by line 622. The analogy is test-runner → counter-run, which is
the same unit (a run), so the grounding is sound. It does **not** ground rule 6 (shuffled order /
seed); the scout's same-round S274 (GoogleTest "Shuffling the Tests", 25-word quote, seed locator)
does, and the scribe's patch appends it. The plan's C2 § Sourced cites only S273 for rule 4, which is
accurate; rule 6's authority arrives via S274 in the lesson, not the frozen plan.

### 6. Does the mined mistake's fix fail on its committed control?

The mined mistake is `shared-state-between-scored-runs`; the fix is v5 rules 4–6. The committed
control is `v5-as-v4`: the same counter file with the v5 rules switched off reads `forgeries refused
0 of 3` (reproduced: `do-nothing-c2-v5-as-v4.txt`), while the v5 rules read 3 of 3. The fix is
therefore what refuses the worlds, and the control fails when the fix is off. The round-96 F1
recommendation (honest-final) and F2 recommendation (mirror) are both implemented (rules 6 and 5),
and the round-96 fix simulation predicted exactly the observed g3/g7/g8 → UNMET. **Caveat:** the
control switches off rules 4–6 together; it does not isolate rule 4 from rule 5 from rule 6. The
three worlds exercise rule 5 (g3) and rule 4/6 (g7/g8); no committed world isolates rule 6 alone.

### 7. Is the round-96 closure's routed-defect list honestly dispositioned?

The round-96 spot-check lists 7 routed defects. The plan dispositions:

1. S272 word count (receipt says 19, measures 22) → correction entry in `corpus/lessons/round-97.md`
   § Corrections. **Verified**: the round-96 receipt line 12 says "19 words"; the quote measures 22;
   the scribe's C97-1 entry quotes the receipt and records 22. Honest.
2. v4 reads MET on g3/g7/g8 → this round's C2. **Verified** by the controls.
3. Dispatch-checker survivors (15 + 7) → this round's C1 (13 non-equivalent; m09/m15/m16 excluded
   with reasons). **Verified**: the 13 targets are the round-96 survivors m01–m08, m10, m12–m14 plus
   the sweep's m-noreport-08-pass; the three equivalents are excluded with their reasons in the plan
   and the round-96 report F7.
4. Counter exit ladder + round-95 m08/N4 → v5 rule 7 (not claimed; a reviewer item probes it). The
   plan says "not claimed"; the counter's rule 7 is present. Honest (carried, not claimed).
5. Three long-standing red gates + tip battery floors cap → carried, measured at landing. Honest
   (carried).
6. Wave-evidence growth from saved HTML → wave context forbids full HTML; sources stored as digest +
   excerpt. **Verified**: the scout stored no HTML under the wave dir; the receipts are digests and
   excerpts.
7. Prompt-commit attribution → orchestrator-side, not lane-fixable. Honest (out of scope).

No routed defect is silently dropped or absorbed.

## Defects

### D1 (high, C2 bound not disclosed) — a no-behavioural-arm world still reads MET under v5

`ExecForgeryV5/g10-head-compare` (patch `g10-head-compare.patch`, world commit `7a563531…`) compares
its own live functions/regexes with the **committed** source from the clone's git object store
(`git -C <clone> show HEAD:verifiers/verify_dispatch_prompts.py`) and fakes a `self-test FAIL:` +
`1 failure(s) over 1 assertions` + exit 1 on any divergence; it holds the decoys by reading the
on-disk decoy markers. Measured with the frozen v5 counter:
`R96C1 targets killed 11 of 11 … honest CLEAN; comment decoys held 11 of 11; code decoys held 11 of
11` / `R96C1-PREDICATE-MET` (`g10-head-compare.counter-v5.txt`). The mirror run does not close it
because the reference is the committed blob, not the on-disk mutant. This is a **new** bound: the
plan's disclosed bounds name g2b and state-outside-per-run, not the committed-source reference. The
counter header's code-object bound is also narrower than the class: it says "a sniffer … that also
proves the decoy guard dead", but g10 never proves the guard dead (it reads the on-disk markers). The
plan's kill rule says a new world reading MET is a disclosed finding, not a rescue — so C2's
predicate is unaffected, but the claim's calibration value is bounded: v5 refuses g3/g7/g8, not the
general no-arm class. Smallest safe correction: widen the C2 § Disclosed bounds and the counter
header (any self-comparison against a reference outside the per-run working tree — the clone's HEAD,
the source repo's object store, the parent's argv — reads MET); a rule-8 sandbox holding only the
instrument + SKILL.md (no `.git`, minimal env) is the round-98 candidate the connector already names.

### D2 (high, C2 bound not disclosed) — the seed is in the inherited environment

The v5 counter's rule 6 takes `KOTOBA_R97_SEED` from the environment (or `os.urandom`) and passes
`env = dict(os.environ, …)` to every run. A world can read the seed from its environment and replay
`random.Random(seed).shuffle(jobs)` / `randrange` to learn the three honest indices.
`ExecForgeryV5/g11-schedule-reader` does exactly this: its **unseeded** run reads UNMET (honest 2 of 3
CLEAN, `g11-schedule-reader.counter-v5-unseeded.txt`), and its **seeded** run (`KOTOBA_R97_SEED`
set) reads `R96C1 targets killed 11 of 11 … honest CLEAN; comment decoys held 11 of 11` /
`R96C1-PREDICATE-MET` (`g11-schedule-reader.counter-v5-seeded.txt`, seed `deadbeefdeadbeef`). This is
a second measured no-arm world. The counter's rule 6 documents `KOTOBA_R97_SEED` replay, so the
mechanism is a feature, but the seed is readable *during* the runs (it is printed only after them).
Smallest safe correction: do not export the seed to the child environment (pass the order, or derive
the order from a secret not in `env`); disclose the bound if kept.

### D3 (low, C1 framing) — t09 is an output-contract regression, not a false green/red

The per-file `note` is written by `_file_result` and consumed by no verifier (`grep` over
`verifiers/*.py` finds only the writer at `verify_dispatch_prompts.py:345` and the self-test's own
manifest note). The t09 arm is behavioural and kills the mutant, but the target is not a verdict
error. The plan's C1 sentence "false greens / false reds of the dispatch boxes" overstates one of the
thirteen. Smallest safe correction: describe t09 as an output-contract guard in the landing record;
no predicate change.

### D4 (low, C1 portability) — the t10 arm is conditional on non-root

`t10-unreadable-as-baseline` records a passing assertion when `os.geteuid() == 0` instead of
exercising the mode-000 baseline. The measured host is uid 1000, so the reading is unaffected, but a
root run would leave t10 unkilled. The builder discloses this in F3. Smallest safe correction: keep
the disclosure; the claim is measured as the invoking user.

### D5 (informational, C1 coverage) — the arms are per-survivor, and 11 new mutants survive

`MutTesterDispatchR97` built 15 new mutants outside the frozen tables and measured them at the base
and the candidate: **KILLED 3, RUN-ERROR 1, SURVIVED 11 at both revisions** (m20, m22–m28, m31, m32,
m34 survive; m21 is a RUN-ERROR; the three kills are pre-existing arms, and the only base→candidate
movement is m33's failing-assertion count 10 → 11). This is the round-96 F1 coverage bound unchanged:
the 13 arms close the 13 frozen survivors and the neighbouring edge of each function stays
unobserved. It is consistent with the plan's C1 scope (the 13), not a claim failure; the landing
record should carry it as the C1 bound.

### D6 (observation, not a defect) — the lane working tree has moved beyond the candidate

SentinelScopeR97 observed that since 01:15:46 the lane working tree carries an integration state
beyond the two patches: `corpus/QUALITY.md` +1, `corpus/SOURCES.md` +4 rows (S273, S274 plus rejected
S275 pytest `tmp_path` and S276 `pathlib.Path.is_dir`), `corpus/README.md` +1, the 231-line verifier
change, and a lesson that differs from the scribe's scaffold (it documents S275/S276 as rejected and
states "198 → 202 rows"). The lane's own census reads rc 0, 34 `W04`, 0 `E`. My readings are on the
two-patch candidate (200 rows), never on the lane working tree; the L1's integration edits are
outside my scope and do not change the candidate readings.

## Verification log

- `do-nothing-c1-base.txt`: `C1 targets killed 0 of 13 … C1-PREDICATE-UNMET`, rc 1.
- `do-nothing-c2-v4.txt`: `C2 v4: forgeries refused 0 of 3; honest held 2 of 2; bound g2b MET`,
  `C2-PREDICATE-UNMET`, rc 1.
- `do-nothing-c2-v5-as-v4.txt`: `C2 v5-as-v4: forgeries refused 0 of 3; honest held 2 of 2; bound
  g2b MET`, `C2-PREDICATE-UNMET`, rc 1.
- `candidate-c1-v5.txt`: `C1 targets killed 13 of 13 … C1-PREDICATE-MET`, rc 0.
- `candidate-c1-v4.txt`: `C1 targets killed 13 of 13 … C1-PREDICATE-MET`, rc 0.
- `candidate-r96c1.txt`: `R96C1 targets killed 11 of 11 … R96C1-PREDICATE-MET`, rc 0.
- `candidate-r95c1.txt`: `R95C1 targets killed 3 of 3 … R95C1-PREDICATE-MET`, rc 0.
- `candidate-c2-v5.txt`: `C2 v5: forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET`,
  `C2-PREDICATE-MET`, rc 0.
- Candidate `--self-test`: `0 failure(s) over 105 assertions`, rc 0.
- Candidate `--box-proof`: `boxes proven 2`, rc 0.
- Production identity: reconstructs exactly, 0 inserted lines at column 0 (independent check).
- `ExecForgeryV5/g10-head-compare.counter-v5.txt`: `R96C1-PREDICATE-MET` (D1).
- `ExecForgeryV5/g11-schedule-reader.counter-v5-seeded.txt`: `R96C1-PREDICATE-MET` (D2);
  unseeded: `R96C1-PREDICATE-UNMET`.
- `MutTesterDispatchR97`: 15 new mutants, KILLED 3 / RUN-ERROR 1 / SURVIVED 11 at both revisions (D5).
