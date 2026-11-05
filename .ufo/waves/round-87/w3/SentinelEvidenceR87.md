# SentinelEvidenceR87 — evidence and confinement audit of round 87 (read-only)

Seat `SentinelEvidenceR87`, wave `r87-w3`, 2026-11-05. Scope: the six audit items of the seat
item plus the wave milestone (re-verify C1 and C2 at the tip, attack both with independent
re-implementations and mutants, measure the C2/D5 drift). **No claim was re-opened and no
frozen file was edited**; every artefact below is a measurement or a receipt.

## Tip

| what | value |
|---|---|
| tip named in the seat brief | `760e1c5edfdefb4767420f711d08f669952de013` |
| `git -C <lane> rev-parse master` at 00:16 | **`d1c031833c37af99196f72f84a6643f84eec129a`** |

The tip moved during this audit: `760e1c5` was master when I started, and by 00:09:29 the L1 had
committed `d1c0318` ("round-87 attempt 2: the C2 D5(iii) drift measured at the tip…"). `760e1c5` is
an ancestor of `d1c0318`. **Both revisions were measured**; every number below is identical at both,
so the move changes no verdict. Brief-tip measurements are labelled `@760e1c5`.

## What the round claims, measured

| claim | counter | at `760e1c5` | at `d1c0318` | base `223ae62` |
|---|---|---|---|---|
| C1 depth | `check_omp_root_semantics.py --rev` | `12 of 12`, guards S1–S3 PASS, exit 0 | same | `0 of 12`, S3 FAIL, exit 1 |
| C2 consistency | `check_r86_routed_repairs.py --rev` | `4 of 5`, exit 1 (D5 FAIL) | same | counter absent at base (exit 2 by definition) |

C2 at the tip: D1–D4 PASS, **D5 FAIL** —
`red set ['corpus.pointers.commit_unresolvable'], want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']`.

**D5 drift, measured (the milestone's object).** `report_dead` healed outside the lane: the gate
site `corpus/lessons/round-86-verifier-spotcheck.md:33` cites `.ufo/reports/round-84/kama.md`, and
that file now exists on the fleet root (`10856 B`, mtime `2026-11-04 22:47`, `## SHONEN` present),
added by fleet commit `5b052020`, which `git merge-base --is-ancestor 5b052020 b72ce052` confirms is
an ancestor of fleet HEAD. The lane's bytes did not change: the gate now reads `8/9 checks pass` with
one DRIFT (`commit_unresolvable`), so the second element of D5(iii)'s exact red set is gone and the
item flips PASS→FAIL with no lane commit. The L1's attempt-2 record states this correctly
(`corpus/lessons/round-87.md` § Attempt 2; `SCORECARD.md` attempt-2 block).

## Findings

### F-1 (HIGH) — C1's bound conjunct is inert at scoring time; the counter does not probe the chain the frozen predicate names

**Where.** `verifiers/check_omp_root_semantics.py:90` (`FROZEN_CHAIN`, two elements),
`:91` (`FULL_CHAIN`, the five-element chain named by `plans/round-87.md:64-65`), `:256-257`
(`expected = expansions(pattern, FROZEN_CHAIN)` versus `actual = expansions(pattern, chain)`),
`:380` (`run(..., chain=FROZEN_CHAIN)` — the driver's default), `:587` (the self-test's
`w_bound` world passes `chain=FULL_CHAIN` over **the same 12 rows** and expects refusal).

**Exploit path / measurement.** `bound_grounded()` compares the row's expansion on the *passed*
chain against its expansion on the hard-coded `FROZEN_CHAIN`, and the driver passes exactly
`FROZEN_CHAIN`, so `actual == expected` by construction: the `{cwd}/` "reaches $HOME or above"
branch cannot fire in the scoring path. Measured on the same committed bytes
(`evaluation: .ufo/waves/round-87/w3/SentinelEvidenceR87/c1-probe.txt`):

```
FROZEN_CHAIN: bound fails on 0 of 12 rows   -> score() grounded 12 of 12
FULL_CHAIN:   bound fails on 7 of 12 rows   -> score() grounded  5 of 12
```

The counter's own self-test asserts both halves of this: its `honest` world (`:528`) and its
`w_bound` world (`:587`) are built from `honest_sem`/`honest_roots` — **the same ledger text** — and
differ only in the chain. So the counter simultaneously certifies the 12 rows as honest and requires
the identical 12 rows to be refused, and the released score takes the permissive half.

**Impact.** The recorded number `12 of 12` cannot distinguish a `{cwd}/` row whose expansion is
bounded from one whose expansion is not: every one of the 7 `{cwd}/` rows passes on the scoring
chain and fails on the predicate's chain, and no pattern-preserving mutant can separate them (the
conjunct is a pure function of the pattern, and all 12 frozen patterns pass). A reader of the
receipt is told the bound clause was satisfied when the clause was never exercised. The row-level
half of C1 is sound — my independent re-implementation (no import of the counter,
`.ufo/waves/round-87/w3/SentinelEvidenceR87/indep_c1.py` → `c1-independent.txt`) re-derives
`12 of 12` at `d1c0318` and additionally checks a *stronger* attribution (the nearest preceding
`// packages/` header equals the claimed module for all 12 rows). The defect is confined to
conjunct 4.

**Smallest remediation (r88, not this wave).** Pass `FULL_CHAIN` into `run()` (or make `expected`
and `actual` use one chain and add the predicate's chain as the second probe), then re-state the
target before new data: on the predicate's chain the honest score is `5 of 12`.

### F-2 (HIGH) — a committed receipt records `exit=0` for a command that never ran, and was then rewritten in the worktree

**Where.** `.ufo/waves/round-87/w3/l1/c2-base-clone.txt:3` (blob at `d1c0318`):
`git show d1c0318:.ufo/waves/round-87/w3/l1/c2-base-clone.txt` prints

```
$ python3 -B verifiers/check_r86_routed_repairs.py --rev 223ae62424f8ab1eb365d733eb648d6228ddd7e8   # in a clone pinned to base
python3: can't open file '/fast/scratch/hyaku/kotoba-r87/l1-base/repo/verifiers/check_r86_routed_repairs.py': [Errno 2] No such file or directory
exit=0
```

**Impact.** The third line asserts a pass for a run that produced `Errno 2`; that is fabricated
provenance, the exact class this round's own D1 polices in the r86 receipts. The worktree version of
the same path (`git status` → ` M .ufo/waves/round-87/w3/l1/c2-base-clone.txt`) is a 35-line
replacement that states the opposite, correct conclusion ("the counter does not exist at the base,
so the base cannot be scored by it"). So the committed record and the honest one disagree, and the
committed one is what a later reader of `d1c0318` sees.

**Smallest remediation.** Commit the honest version (delete the `exit=0` line; record the run as
"not scored — counter absent at base"), and treat an echoed `exit=` in any receipt as needing its
command line adjacent in the same block.

### F-3 (MEDIUM) — C2's D5(iii) is a function of the worktree and of the fleet root, not of `<rev>`

**Where.** `verifiers/check_r86_routed_repairs.py:12` (docstring: "recomputed from `<rev>`'s
committed bytes … and never from the worktree"), `:435` (pins only `git rev-parse master`), `:444-445`
(runs the gate with `cwd=repo`, so the gate reads worktree files), `:462` (exact red-set literal).

**Evidence, three readings at one revision.** At `35a395a9` — the revision the 5-of-5 receipt
`receipts/c2-final.txt` names — the frozen counter now reads:

```
could-not-evaluate: worktree tip d1c031833c37 != measured revision 35a395a9aabf (plans/round-87-addendum-1.md A1.2)
exit=2
```

so the round's own `5 of 5` receipt cannot be re-derived at its own revision by its own instrument.
At the tip the lane reads `8/9` (one red); the same revision in a relocated checkout reads `7/9`
with `report_dead_detail = ['corpus/lessons/round-81.md:29: ../../.ufo/reports/round-76/kotoba.md']`
— a different site from the one D5(iii) requires
(`.ufo/waves/round-87/w3/SentinelEvidenceR87/clone-gate.json`). And the pin does not constrain
dirtiness: one uncommitted line appended to `corpus/lessons/round-87.md` in a clean checkout moves
the gate `7/9 → 6/9` with `HEAD` unchanged
(`.ufo/waves/round-87/w3/SentinelEvidenceR87/d5-worktree-sensitivity.txt`). The same mechanism was
live earlier in this audit: C2 evaluated at `760e1c5` while the lane worktree carried four
modified tracked files (`LOG.md`, `SCORECARD.md`, `corpus/QUALITY.md`, `corpus/lessons/round-87.md`)
and the tip pin still passed.

**Impact.** "C2 = 5 of 5" is an archive of a checkout-state, not of a revision: it is false today
in the lane (4 of 5), unreachable by re-run (exit 2), and false in a clone (wrong detail site).
The Q79 the L1 landed names this class; the measurement above adds the worktree half, which Q79
does not cover.

**Smallest remediation.** Break the pin into its parts: read the measured corpus through
`git ls-tree`/`git show <rev>:<path>` (or refuse a dirty worktree), name the external resolution
root in the item, and test the red set as a subset of the disclosed set with a monotone direction
(they already routed this).

### F-4 (MEDIUM) — the C2 receipts carry neither the measured revision nor an exit code

**Where.** `receipts/c2-final.txt:1-6` and `receipts/c2-after.txt:1-6` (the revision appears only
inside D1's `instruments equal 04647b0f..35a395a9` string; no `exit=`); `receipts/d5-after-revert.txt`
(no revision line); `receipts/census-after.txt` (neither); `receipts/province-core-tip.txt:1` (revision
`fcdaba57`, no exit). `check_r86_routed_repairs.py`'s `main()` never prints `rev` or `exit=`, while
the C1 counter prints both (`:385`, `:395`) — the receipts cannot carry the fields by construction.

**Impact.** The round's own D1 criterion requires an r86 receipt to name its measured revision and
carry `exit=0`; four of its own ten receipts would fail that criterion. An auditor cannot tie
`c2-final.txt` to a revision without reading a parenthesised instrument list.

**Smallest remediation.** Print `rev <rev>` and `exit=N` from `main()` (C1 already does) and re-emit
the receipts; for `census-after.txt` record the frozen census command and its exit code.

### F-5 (LOW) — the S1 guard always passes, including when the ledger is absent

**Where.** `verifiers/check_omp_root_semantics.py:306` (`guards = {"S1": True, "S3": True}`; `S1` is
never set `False`), `:386` (prints `PASS` unconditionally), `:394` (the exit condition includes
`guards["S1"]`, which is the constant `True`).

**Evidence.** Base run: `guard S1 ledger-from-rev PASS (git show 223ae62…:verifiers/omp-skill-roots-semantics.tsv rc=absent, …)`.

**Impact.** The frozen predicate reads "exit 0 iff N == 12 and guards S1–S3 all PASS"; S1 cannot
fail, so it is a label rather than a conjunct. The underlying mechanism (ledgers read via
`git show`, never the worktree) is correct — the label overstates it.

**Smallest remediation.** Set `guards["S1"] = False` when either ledger is absent at `<rev>`;
otherwise drop S1 from the predicate sentence.

### F-6 (INFO) — `/tmp` citations exist in the corpus, none in round-87's own evidence

`grep -rnE '(^|[^a-z])/tmp/' <lane>/corpus <lane>/.ufo/waves/round-87 --include='*.md' --include='*.txt' --include='*.json' --include='*.tsv'`
→ 57 lines in `corpus/`, 2 in `.ufo/waves/round-87/`. Both round-87 hits are prompt text
(`r87-w3-spec.json:55`, `r87-w3-dispatch.json:171`) carrying this audit's own grep pattern — command
artefacts, allowed. In the corpus, 30 lines are command/`$`-block artefacts and **27 are prose
citations** to `/tmp` directories, all from rounds 7–54 (`corpus/knowledge/harness-independent-round37.md`,
`corpus/lessons/round-10.md:132`, `corpus/lessons/round-12.md:44,84`, …). None is round-87 evidence
and none is used by either claim; listed in `item2-tmp-hits.txt` for the record. Rated INFO, not a
finding for this wave.

### INFO — the plan's frozen sentence says `N of 13`

`plans/round-87.md:45` still reads `grounded N of 13` while the counter, SKILL.md and every receipt
read `12`; addendum 1 (`plans/round-87-addendum-1.md:10,25`) corrects it before any candidate score
and the round-86 ledger carries 12 data rows (verified). Disclosed and admissible under the closure
ruling; noted so a later reader of the plan alone is not misled.

## The six audit items

### 1. Non-author records — identical

`git rev-parse 223ae62:<path>` vs `760e1c5:<path>` vs `d1c0318:<path>`:

```
corpus/lessons/round-86-verifier-spotcheck.md
  base 223ae62 ae3f49a3685e796ae5154cf9a4b055132a8c25b0
  tip  760e1c5 ae3f49a3685e796ae5154cf9a4b055132a8c25b0
  tip  d1c0318 ae3f49a3685e796ae5154cf9a4b055132a8c25b0
corpus/lessons/round-81.md
  base 223ae62 315c0ec68075e9c7c4037b8f42617e3eee0a434b
  tip  760e1c5 315c0ec68075e9c7c4037b8f42617e3eee0a434b
  tip  d1c0318 315c0ec68075e9c7c4037b8f42617e3eee0a434b
```

**Identical** in both pairs. The A2.2 laundering was reverted and stayed reverted.

### 2. `/tmp` evidence — 0 citations in round-87

Counts and classification in § F-6; full list in `item2-tmp-hits.txt`. Round-87 artefacts: 2 hits,
both command artefacts (prompt text). Corpus: 57 hits, 30 command artefacts, 27 prose citations,
all pre-round-87.

### 3. Receipts name their revision — 5 of 10 do

`item1-item3.txt`. **Do not:** `c2-after.txt`, `c2-final.txt` (revision only implied by D1's
instrument string; no exit code), `census-after.txt` (neither), `d5-after-revert.txt` (no revision),
`province-core-tip.txt` (revision `fcdaba57`, no exit). **Do:** `after-battery.txt`,
`base-battery.txt`, `c1-after.txt`, `c1-after-tip.txt`, `c1-instrument-freeze.txt` — these carry a
revision line and exit codes. The gap is structural (§ F-4): the C2 counter prints neither field.

### 4. Credentials — clean

`item4-credentials.txt`. No `op://`, `ghp_`, `TOKEN=`, `PASSWORD=` or `-----BEGIN` value exists in
the wave tree: the 7 hits for each of `op://`/`ghp_`/`TOKEN=`/`PASSWORD=` (and the 1 for `sk-`) are
the audit pattern itself quoted in `gen-w1.py`,
`gen-w3.py`, `r87-w1-dispatch.json`/`spec.json`, `r87-w3-dispatch.json`/`spec.json` (and, after
this run, in my own `item4-credentials.txt`). 132 long base64-shaped runs, **all hex** (commit ids,
sha256 digests, mmap offsets); 0 non-hex runs; 0 PEM blocks.

### 5. Ready-file discipline — both taken, no rewrite

`item5-ready.txt`. Round-87 holds 4 ready-related files: `r87-w1.ready` (20:10) +
`r87-w1.ready.dispatched` (20:11:31) and `r87-w3.ready` (23:58) + `r87-w3.ready.dispatched`
(00:08:39). Each `ready` is committed exactly once (`git log -- <ready>` → one commit each), no
duplicate and no re-write; both waves' ready files were taken. Other round-8x waves hold 2 each
(83/84 hold 0). Transient only: at 00:08 the w3 marker existed as `r87-w3.ready.partial` (404 B) and
by 00:09 as `r87-w3.ready.dispatched` (467 B) — one dispatch, marker finalised.

### 6. Write confinement — no misroot, no out-of-tree lane change

`item6-confinement.txt`. Lane porcelain: only `.ufo/waves/round-87/w3/**` (this wave's seats) plus
one modified tracked file inside the wave tree (F-2). Lane files changed **outside** the wave tree:
none. Fleet porcelain: ` M .scratch/run15-state.json`, ` M .ufo/l0-questions.md`,
`?? .ufo/reports/round-86/kama.md`, `?? .ufo/reports/round-90/kotodama.md`, `?? mo.tip` — grep for
`kotoba|round-87|r87` → **(none)**: no fleet-root entry names this lane or this round.

## Attack set (independent re-implementations and mutants)

- **C1 independent re-derivation** (`indep_c1.py`, no import of the counter): ledgers via
  `git show`, ELF mmapped, own header scan. `12 of 12` at `d1c0318`; every row's reader quote sits
  on a true newline-delimited line carrying a join token 7–45 bytes away, and the nearest preceding
  `// packages/` header equals the claimed module for all 12.
- **C1 mutants** (`c1-mutants.txt`, cumulative commits in the scratch clone,
  `git rev-parse --show-toplevel` = the clone): doc-quote in `reader_quote` → `11 of 12`; module
  swap rows 3↔5 → `10 of 12`; ledger shrunk to 11 rows → `9 of 12` + S3 FAIL; pattern mutated →
  `9 of 12` + S3 FAIL. All refused, exit 1. The pristine rev in the same clone still reads
  `12 of 12` (the counter is git-only and path-independent — the contrast with C2's D5).
- **C1 bound probe** (`probe_c1.py`, `c1-probe.txt`) → F-1.
- **C2 independent re-derivation** (`indep_c2.py`, `c2-independent-tip.txt`): D1 PASS
  (receipts at the rev, two named revisions `04647b0f`/`9b040edb` whose instrument blobs equal the
  measured rev's), D2 PASS (sentence present in `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`
  after comment-marker stripping, `SWARM_ROLES` = 10 roles, no `planner`), D3 PASS (5 reject rows
  with ≥8-word reasons), D4 PASS, D5(i)(ii) PASS, D5(iv) PASS. Only D5(iii) fails — the drift.
- **C2 location control** (`clone-gate.json`, `d5-worktree-sensitivity.txt`) → F-3.
- **C2 re-run at the receipt revision** → exit 2 (F-3).

## Receipts

`.ufo/waves/round-87/w3/SentinelEvidenceR87/`: `measurements-C1-C2.txt`, `c1-probe.txt`,
`c1-independent.txt`, `c1-mutants.txt`, `c2-independent-tip.txt`, `clone-gate.json`,
`d5-worktree-sensitivity.txt`, `item1-item3.txt`, `item2-tmp-hits.txt`, `item4-credentials.txt`,
`item5-ready.txt`, `item6-confinement.txt`, `non-author-blobs.txt`, and the three scripts
(`indep_c1.py`, `indep_c2.py`, `probe_c1.py`). Scratch `/fast/scratch/hyaku/kotoba-r87/SentinelEvidenceR87/`
deleted at exit; no tool was installed (none was needed).

## Verdict

The two claims stand or fall as the round states them: C1 is `12 of 12` at both tips with the
base at `0 of 12`, and C2 is **`4 of 5`**, not 5 of 5, because D5(iii)'s exact red set lost
`report_dead` to a fleet commit at 22:47 with no lane change. Beyond the round's own record:
C1's bound conjunct is dead code at scoring (F-1), one committed base-row receipt carries a false
`exit=0` (F-2), and D5(iii) cannot be re-derived at its own revision and moves with uncommitted
bytes (F-3). The `/tmp`, credential, ready-file and confinement axes are clean.

`audit: 5 findings (2 high, 2 medium, 1 low), 1 informational (F-6)` — F-1
`verifiers/check_omp_root_semantics.py:90,91,256,257,380,587`; F-2
`.ufo/waves/round-87/w3/l1/c2-base-clone.txt:3`; F-3 `verifiers/check_r86_routed_repairs.py:12,435,444-445,462`;
F-4 `.ufo/waves/round-87/receipts/c2-final.txt:1-6`; F-5 `verifiers/check_omp_root_semantics.py:306,386,394`.
