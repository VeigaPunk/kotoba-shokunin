# MutateR87 — mutation report: round-87 C1 (depth) and C2 (consistency)

Wave `r87-w3`, seat `MutateR87`. Read-only on the lane: no `verifiers/*`, `plans/round-87*.md`,
`corpus/*`, `LOG.md`, `SCORECARD.md` or `SKILL.md` byte was changed. Every run below is either a
read-only lane invocation or a scratch-clone/scratch-fixture invocation under
`/fast/scratch/hyaku/kotoba-r87/MutateR87/` (deleted before the seat closed; receipts copied to
`.ufo/waves/round-87/w3/MutateR87/`). No tool was installed or upgraded.

## 0. Frozen state as measured, and the tip drift

| item | pinned by the seat | measured |
|---|---|---|
| lane `master` | `760e1c5edfdefb4767420f711d08f669952de013` | **`d1c031833c37af99196f72f84a6643f84eec129a`** — the lane advanced during this wave (commit `d1c0318`, "round-87 attempt 2: the C2 D5(iii) drift …") |
| `verifiers/` at `760e` vs `d1c0318` | — | **byte-identical** (`git -C <clone> diff --stat 760e d1c0318 -- verifiers/` prints nothing), so C1 is measured on the same bytes at either rev |
| omp ELF | sha256 `6737ee24…9ccb7b0f` | same, S2 PASS on every run |
| counters | — | `check_omp_root_semantics.py` `6e826f3b…e7798922`; `check_r86_routed_repairs.py` `26daaa13…61b4ee9a`; `verify_corpus_integrity.py` `a0b52d24…8304b011` (lane = clone = pinned rev) |

Because the brief's rev (`760e`) is no longer the tip, both revs are measured: C1 at `760e` (the
pinned ledger) and at `d1c0318`; C2 at the current lane tip `d1c0318` (D5(iii) requires
`rev-parse master == rev`, so `760e` can only be measured in a clone).

## 1. Pristine baselines (the controls)

```
$ python3 -B verifiers/check_omp_root_semantics.py --rev 760e1c5… --repo <clone@760e>
  … guard S3 pattern-set PASS / omp root semantics grounded 12 of 12 / exit=0     rc=0
$ python3 -B verifiers/check_omp_root_semantics.py --rev d1c03183… --repo <clone@d1c0318>
  … omp root semantics grounded 12 of 12 / exit=0                                  rc=0
$ python3 -B verifiers/check_r86_routed_repairs.py --rev d1c03183… --repo <lane>
  PASS d1 … PASS d2 … PASS d3 … PASS d4
  FAIL d5  … red set ['corpus.pointers.commit_unresolvable'], want exactly
           ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']
  r86 routed defects closed 4 of 5                                                 rc=1
$ python3 -B verifiers/check_omp_root_semantics.py --self-test   -> 0 failure(s) over 35 assertions   rc=0
$ python3 -B verifiers/check_r86_routed_repairs.py --self-test   -> 0 failure(s) over 53 assertions   rc=0
```

The shipped run counts (35 and 53 assertions) are the detectors used for the mutation score.

### The D5 drift, measured (this is the thing the wave asked to measure)

Lane tip, authoritative (`verify_corpus_integrity.py --json`, run in the lane worktree):

```
checks 9  pass 8
red [('corpus.pointers.commit_unresolvable', 1)]          # report_dead is GREEN: healed to 0
dead  0 []
unres 1 ['corpus/lessons/round-81.md:8: 8b1cc1b00a9322cd8e231d87e015e1d75d20adc1']
```

So `report_dead` healed to **0** when the fleet report `../.ufo/reports/round-84/kama.md` landed
(22:47) — the brief's narrative is confirmed **in the lane**. `commit_unresolvable` is still red at
its recorded site, tally `8/9`, D5(iii) dies on its first arm (exact-set equality).

Same rev in a `git clone --shared` (`760e`, `.ufo/` not carried): `checks 9 / pass 7`,
`red [(report_dead,1),(commit_unresolvable,1)]`, `report_dead_detail
['corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md']`, tally `7/9`. The clone
reproduces the red **count** but substitutes one dead pointer for another, because
`<lane>/.ufo/reports/round-76/kotoba.md` is a symlink into the fleet root that a clone does not
carry. Consequence: **D5(iii) is only meaningful when run in the lane worktree** (finding F6).

## 2. C1 — five mutants, one per guard

Mutants are copies of the pinned counter with one deleted test each; diffs in
`receipts/mutants/c1_*.diff` (`cp -a` of the lane `verifiers/` into scratch; lane untouched).

| id | mutation | tip run `--rev 760e1c5` | shipped `--self-test` | forged ledger: pristine → mutant |
|---|---|---|---|---|
| **a** | `reader_grounded`: the JOIN_TOKENS scan is dropped, any located quote grounds | `grounded 12 of 12`, S3 PASS, `exit=0`, rc=0 → **survived** | 1 failure: `w_docquote names the join token` (**message-level only**; that world still reads 11 of 12) | `f_a`: 11 of 12 rc=1 → **12 of 12 rc=0** |
| **b** | `module_grounded`: the `first_reader < last` ordering test is deleted | `grounded 12 of 12`, rc=0 → **survived** | 3 failures: `w_offset_order exit 1`, `… 11 of 12`, `… names the order` | `f_b`: 11 of 12 rc=1 → **12 of 12 rc=0** |
| **c** | `pattern_problem`: the `..` segment test is deleted | `grounded 12 of 12`, rc=0 → **survived** | 1 failure: `w_dotdot names the segment` (**message-level only**; that world still reads 11 of 12) | `f_c`: 11 of 12 rc=1 → **12 of 12 rc=0** |
| **d** | `pattern_problem`: the first-segment wildcard test is deleted | `grounded 12 of 12`, rc=0 → **survived** | 3 failures: `w_star exit 1`, `… 11 of 12`, `… names the wildcard` | `f_d`: 11 of 12 rc=1 → **12 of 12 rc=0** |
| **e** | `run`: `grounded == TOTAL` → `grounded >= TOTAL - 1` (an 11-row ledger passes) | `grounded 12 of 12`, rc=0 → **survived** | **6 failures**: `w_docquote/w_nomodule/w_dotdot/w_star/w_quote_miss/w_offset_order exit 1` (each now exits 0 at 11 of 12) | `f_e`: 11 of 12 rc=1 → **11 of 12, `exit=0`, rc=0** |

Every forged world is a *committed* scratch clone revision at the real tip bytes, so the real ELF
and the real round-86 ledger are in play (`receipts/make_worlds.py`, `receipts/forged/worlds/`):

| world | forgery | pristine (control) | intended mutant |
|---|---|---|---|
| `f_a` | row 9 `reader_quote` = `// packages/coding-agent/src/discovery/omp-plugins.ts` (a header line: located, after its own header, **no** path-join token) | 11 of 12, rc=1, "no ELF line carrying a path-join token" | c1_a → 12 of 12, rc=0 |
| `f_b` | row 1 `module` = `…/omp-plugins.ts` (header at 173914407, reader first at 173819979) | 11 of 12, rc=1, "first occurs at 173819979, before the header's last occurrence at 173914407" | c1_b → 12 of 12, rc=0 |
| `f_c` | row 8 `root_pattern` = `~/.omp/../.omp/agent/skills` in **both** ledgers (S3 stays green) | 11 of 12, rc=1, "carries a `..` segment" | c1_c → 12 of 12, rc=0 |
| `f_d` | row 1 `root_pattern` = `*/skills` in both ledgers | 11 of 12, rc=1, "wildcard in its first segment ('*')" | c1_d → 12 of 12, rc=0 |
| `f_e` | both ledgers cut to 11 data rows | 11 of 12, rc=1 (note: "the round-86 ledger carries 11 patterns") | c1_e → 11 of 12, **rc=0** |

Full 6×5 matrix in `receipts/base/world-matrix.txt`. It is **specific**: on each world exactly the
intended mutant flips (11→12 of 12), every other mutant reproduces the pristine failure; `c1_e`
flips every world that reads 11 of 12, as its mutation predicts.

### C1 reading

* Against the **tip ledger alone**: **0/5 killed** — every mutant reproduces `grounded 12 of 12`,
  `guard S3 pattern-set PASS`, `exit=0`, rc 0 exactly. The honest 12-row ledger exercises all four
  conjuncts, so a single genuine input cannot detect a removed guard. This is expected of mutation
  testing (a test *suite* does the killing) and is reported as the headline: **the tip run is not a
  detector for any guard**.
* Against the **shipped `--self-test`** (35 assertions): **5/5 killed**.
* **Verdict-level** kills (a world whose pass/fail the mutant changes) with the shipped suite:
  only b, d, e. For **a** and **c** the shipped worlds stay 11 of 12 under the mutant and only the
  diagnostic-string assertion fails — `w_docquote`'s doc line sits at offset ~114.49M, *before*
  every `// packages/<module>` header (172.78M+), so conjunct 3 masks the missing conjunct 2; and
  `w_dotdot`'s `{cwd}/../…` shape is caught by `bound_grounded`'s "`{cwd}/` rest is not a plain
  relative path" test, so the `pattern_problem` test is masked. The forgeries `f_a` / `f_c` are the
  first inputs that make those two guards load-bearing at verdict level.

## 3. C2 — three mutants (D3, D4, D5(iii))

Diffs in `receipts/mutants/c2_*.diff`.

| id | mutation | lane tip run `--rev d1c0318` | shipped `--self-test` |
|---|---|---|---|
| **d3** | `## Gate` accepted if `\brejected\b` appears anywhere in the prose (before the row path) | `PASS d3 5 reject row(s)…` — *identical to pristine*, rc=1 (only d5 red) → **survived** | **5 failures**: `prose world reads 0 of 5`, `prose world fails every item`, `w_gateprose exits 1`, `w_gateprose reads 4 of 5`, `w_gateprose names d3` → **killed** |
| **d4** | the `KILL_BOUNDARY` membership test is deleted | `PASS d4 plans/round-87.md read; the boundary is not tested` — verdict identical to pristine (d4 passed either way), rc=1 → **survived** | **3 failures**: `prose world reads 0 of 5`, `prose world fails every item`, `the old kill wording reads 4 of 5` → **killed** |
| **d5(iii)** | exact-set equality → `not set(red) <= want` ("no red outside the set") | `FAIL d5 report_dead detail [] does not name corpus/lessons/round-86-verifier-spotcheck.md:33` — **same 4 of 5, same rc=1** as pristine (message differs) → **survived** | **0 failures over 53 assertions** → **survived** |

Note on d3 at the tip: the tip's `## Gate` body carries no `rejected` token
(`grep -c rejected corpus/lessons/round-87.md` → 0), so the mutant falls through to the row path and
passes for the pristine reason; the mutation is invisible at the tip either way. d4's tip verdict is
invisible because the honest plan already carries the boundary.

### D5(iii) — analysis of a proposed repair (not a change made)

The mutation is the repair shape a proposer would reach for after the drift: tolerate a red set that
is a subset of the wanted one. **No lane file was changed**; the mutant is a scratch copy.

*What the frozen exact-set form (`set(red) != want` → FAIL) accepts:* only
`red == {corpus.pointers.report_dead, corpus.pointers.commit_unresolvable}` **and** `report_dead`
detail names `…/round-86-verifier-spotcheck.md:33` **and** `commit_unresolvable` detail names
`…/round-81.md:8` **and** the tally is `7/9 checks pass`.
*It rejects:* a third red; `report_dead` alone; `commit_unresolvable` alone; no red; either detail
site absent; any tally ≠ 7/9.

*What the subset form accepts/rejects:* it accepts **any** `red ⊆ want` at the first arm (so
`{report_dead}`, `{commit_unresolvable}`, `{}`, and the honest pair), rejects any red outside `want`,
and then applies the *same* site and tally arms. On the **healed-drift case** (`red =
{commit_unresolvable}`, `report_dead = 0`) it clears the set arm and dies at the next arm —
`report_dead detail [] does not name …spotcheck.md:33` — which is exactly what the mutant run at the
lane tip prints.

*Why it can never be more than a message change:* the tally arm is computed from the same `results`
(`passed = #{verdict == "PASS"}`, `len = 9`) and pinned to `7/9`, so it forces `|red| = 2`; with
`|red| = 2`, `red ⊆ want` ⟺ `red == want`. Empirically (`receipts/base/d5-forms.txt`, six fixture
worlds, pristine vs mutant):

| world | red set | pristine | subset mutant |
|---|---|---|---|
| honest | 2 wanted, both details, 7/9 | PASS d5 | **PASS d5 (identical text)** |
| healed | `{commit_unresolvable}`, 8/9 | FAIL (red set) | FAIL (report_dead detail []) |
| only_dead | `{report_dead}`, 8/9 | FAIL (red set) | FAIL (commit_unresolvable detail []) |
| empty | `{}`, 9/9 | FAIL (red set) | FAIL (report_dead detail []) |
| extra | 3 reds | FAIL (red set) | FAIL (red set) |
| healed_detail | `{commit_unresolvable}` but the dead site present, 8/9 | FAIL (red set) | FAIL (`tally 8/9 checks pass, want 7/9 checks pass`) |

Verdict, score and exit code are identical in all six worlds and in all 53 shipped assertions; only
the diagnostic string differs. So the proposed repair is **an equivalent mutant**: it does not
repair the drift (D5(iii) still fails at the next pin) and it cannot be distinguished by any input
the counter accepts. D5(iii) is bound to the pre-drift snapshot by **three** independent pins — both
reds must be red, `report_dead` must name `spotcheck:33`, and the tally must be 7/9 — so the healed
state cannot be absorbed by relaxing one of them, and the "monotone form" the attempt-2 lesson
rejects by policy would in any case have to relax the site and tally pins as well.

## 4. Scores

* C1, tip ledger only: 0/5. C1, shipped `--self-test`: **5/5**. C1, verdict-level with the five
  forgeries: 5/5. Surviving mutant: none; two guards (a, c) have only message-level coverage in the
  shipped suite.
* C2, tip only: 0/3. C2, shipped `--self-test`: **2/3**. Surviving mutant: **d5(iii) subset**, which
  no input can kill (section 3).
* Strongest surviving mutant: **C2 d5(iii) `set(red) <= want`** — it survives the tip run *and* all
  53 shipped assertions and is unkillable by construction; second, **C1 e** (an 11-row ledger exits
  0 while printing `grounded 11 of 12`), the only survivor shape that changes a real verdict, and
  the one whose kill in the shipped suite is incidental (six wild worlds, not `w_shrink`).

## 5. Findings

1. **F1 — C1 e: exit code decoupled from the frozen target.** `grounded >= TOTAL - 1` prints
   `omp root semantics grounded 11 of 12` and exits 0 on a genuinely 11-row, S3-green ledger
   (`f_e`). Any consumer keying on exit 0 accepts a ledger one row short of the frozen denominator.
   `w_shrink` does not test this (its roots ledger stays at 12 rows, so S3 goes red first).
2. **F2 — C1 a: the join-token guard has message-only coverage.** `w_docquote` fails the row for
   two reasons at once (no join token *and* the doc line precedes every module header), so deleting
   the join-token test keeps `11 of 12`. Forged world `f_a` moves the same quote onto a header line
   and the mutant reaches `12 of 12`, exit 0.
3. **F3 — C1 c: the `..` test in `pattern_problem` is masked for the shape the suite tests.**
   `w_dotdot` uses `{cwd}/../…`, which `bound_grounded` independently refuses; only a `~/…/../…`
   row (`f_c`) makes the deleted test load-bearing.
4. **F4 — C2 d3/d4 mutants are invisible at the tip**: both keep the pristine verdict and change
   only a detail string (`PASS d3 …` / `PASS d4 … read; the boundary is not tested`); the shipped
   self-test kills them, so this is coverage that exists but that the frozen claim run does not
   exercise.
5. **F5 — C2 D5(iii) is triple-pinned to the pre-drift snapshot** (both reds, `report_dead` at
   `spotcheck:33`, tally 7/9). The healed state (`report_dead 0`, tally 8/9) cannot pass by
   relaxing set equality alone, and the subset form is an equivalent mutant. A repair, if any, is a
   predicate amendment (frozen here), not a counter edit.
6. **F6 — D5(iii) reads the worktree, not `<rev>`.** It runs `repo/verifiers/verify_corpus_integrity.py`
   with `cwd=repo` and a hard-coded `FLEET_ROOT`, so the same `--rev` yields different red details
   depending on where the worktree lives and on lane-local `.ufo/` state (clone at `760e`:
   `report_dead` at `round-81.md:29`, tally 7/9; lane at `d1c0318`: `report_dead` 0, tally 8/9).
   The verdict coincided at 4 of 5 by different arms. Unlike C1's S1, this arm is not rev-bound.
7. **F7 — the tip is not a mutation detector.** All eight mutants reproduce the pristine output at
   the tip (12/12 rc=0; 4 of 5 rc=1); only the counters' own self-tests discriminate. Any future
   wave that measures these claims should run `--self-test` alongside `--rev`.

## 6. Risks

* The lane advanced under this seat (`760e` → `d1c0318`); the C2 numbers belong to `d1c0318` and to
  the fleet state at 22:47. A new fleet or lane commit can move `report_dead` again, changing
  D5(iii)'s *failing arm* (never its verdict) — re-measure in the lane, not in a clone.
* Forged worlds are scratch-clone commits (`760e` + one ledger edit); they are reproduced from the
  copied ledgers in `receipts/forged/worlds/`, not from the deleted clone.
* No claim was re-scored and no counter was repaired; every "defect" above is a finding.

## 7. Receipts

```
.ufo/waves/round-87/w3/MutateR87/
  MutateR87.md                 this report
  mutants/c1_{a..e}.py + .diff  the five C1 mutants and their diffs
  mutants/c2_{d3,d4,d5iii}.py + .diff
  base/c1-tip.txt               pristine 12/12 at 760e and d1c0318
  base/c1-mutants-tip.txt       the five tip runs (all 12/12, rc=0)
  base/c1-self-test.txt         pristine 0/35 + per-mutant failure lists
  base/c1_e-selftest.txt        mutant e: 6 failures over 35
  base/c2-tip.txt               pristine C2 in both clones (4 of 5)
  base/c2-lane-tip.txt          pristine C2 in the lane (D5 red-set arm)
  base/c2-mutants-tip.txt       the three C2 tip runs
  base/c2-self-test.txt         pristine 0/53, d3 5 failures, d4 3 failures, d5iii 0
  base/d5-forms.txt             six D5(iii) fixture worlds, pristine vs subset
  base/world-matrix.txt         6×5 C1 world matrix
  base/worlds.json              the five forged revisions
  base/gate-lane-tip.json       lane gate: 8/9, report_dead 0, red {commit_unresolvable}
  base/gate-tip.json            clone@760e gate: 7/9, report_dead at round-81.md:29
  base/gate-base.json           clone@223ae62 gate: 3/9
  base/offset-probe.txt         ELF offsets: every doc quote precedes every module header
  base/instrument-sha256.txt    instrument hashes
  forged/worlds/f_*/            the two ledgers as committed in each forged world
  probe_offsets.py make_worlds.py d5_worlds.py   the drivers
```

Scale for the closing line: killers are counted against the counters' own shipped self-tests
(C1 35 assertions, C2 53). Against the single frozen tip ledger the score is C1 0/5 and C2 0/3 by
construction (the tip is one honest input); each C1 mutant's verdict-level kill is demonstrated by
the forged ledger named in section 2.

`C1 killers: 5/5; C2 killers: 2/3; survivors=[c2_d5iii (set(red) <= want — equivalent mutant, masked by the tally pin); c1_e iff the score is taken at the tip only]`
