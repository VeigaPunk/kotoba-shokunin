# ExecC2Tip — kotoba round 61 (attempt 1, hyaku run 5): C2 counter control receipt + gate-registry row audit

Seat: `kotoba-r61-wave-ExecC2Tip` (executor; axis judged: calibration).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated). **Read-only to this seat** — no lane
source, no fleet file, no sibling file, no `.ufo/state`, no git/jj index file was written. The only write
by this seat is this report file.

Base of the assignment: `f3246d1493b60ea1c0d947a19c39f9e08e92f326`. Plan: `plans/round-61.md`.
L1 (sole integrator): `agent://KotobaR61`. No dispatch, no subagent, no ask tool, no jj/git mutation.

---

## 1. Behavior — what this seat did

1. Ran the two commands the assignment named, against the lane's own committed checker, and confirmed both
   against the committed control receipt `.ufo/waves/round-61/controls/C2-base.txt`.
2. Audited `verifiers/check_routed_repairs.py` **against `verifiers/check_gate_registry.py`'s own pinned
   rules** (not by eye): by importing the lane's committed `check_gate_registry.py` and calling its real
   `judge`/`judge_row`/`cells`/`clean`/`has_flag_handler`/`PAIR_RE`/`FLAG_RE`/`Tree` functions on a
   candidate row, and by reading the checker source for every flag the row names.
3. Attacked the C2 counter's six frozen checks for leniency and crash surfaces — the calibration axis
   this round is judged on — and derived the exact token spellings each repair needs so the L1 lands
   C2 on the first try.
4. Confirmed the C2 base control receipt is byte-faithful to a live re-run, and flagged three landing
   hazards that would otherwise surface as a failed C2 measurement or a red adjacent gate.

---

## 2. Measurement 1 — `--self-test`

Command (run from the lane root), `date -u` = `Fri 23 Oct 2026 07:18:21 PM UTC`:

```
$ python3 -B verifiers/check_routed_repairs.py --self-test
self-test all-repairs: 6 of 6 (want 6) ok
self-test base-world: 0 of 6 (want 0) ok
self-test no-log: 3 of 6 (want 3) ok
self-test no-quality: 5 of 6 (want 5) ok
self-test without-round-61.md: 5 of 6 (want 5) ok
self-test without-census-after.txt: 5 of 6 (want 5) ok
self-test without-controls-ancestry.txt: 5 of 6 (want 5) ok
self-test ra-without-command: 5 of 6 (want 5) ok
self-test rb-missing: 5 of 6 (want 5) ok
self-test ra-without-count: 5 of 6 (want 5) ok
self-test rc-without-c1-pointer: 5 of 6 (want 5) ok
self-test ancestry-without-merge-base: 5 of 6 (want 5) ok
self-test: 0 failure(s)
```

**Exit code: 0.** Matches the assignment's expectation (0 failure(s), exit 0).

Note for the L1 — the checker was hardened *during* this wave, after the freeze commit. The freeze commit
`7827628` carried a 9-arm self-test; the current `HEAD` (`eb5e149`, "round-61: C2 checker self-test
hardened pre-data (MutC2: 12 arms, kills m1/m2/m5/m7; two-point residual disclosed; frozen six checks
untouched)") carries 12 arms. The three new arms are `ra-without-count`, `rc-without-c1-pointer`,
`ancestry-without-merge-base`, plus an arm-count guard (`arms != 12` → failure). **The six scoring
checks in `check_repairs()` are byte-identical between the two revisions** — I verified this by
re-reading the function at both revisions and by re-running every attack probe below against the current
file. All findings in §5 were re-confirmed against `eb5e149` and still hold.

---

## 3. Measurement 2 — `--rev <base>`

Command, `date -u` = `Fri 23 Oct 2026 07:18:21 PM UTC`:

```
$ python3 -B verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
```

**Exit code: 1.** Matches the assignment's expectation (`routed repairs verified 0 of 6`, exit 1).

---

## 4. Confirmation against the committed control receipt

`.ufo/waves/round-61/controls/C2-base.txt` (committed at freeze `7827628`, unchanged at `eb5e149` —
`git diff 7827628 eb5e149 -- .ufo/waves/round-61/controls/C2-base.txt` is empty):

```
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
base-exit=1
```

Byte-diff of the receipt (minus its trailing `base-exit=1` annotation line) against the live re-run of
§3, `date -u` = `Fri 23 Oct 2026 07:18:21 PM UTC`:

```
$ diff <(grep -v '^base-exit=' .ufo/waves/round-61/controls/C2-base.txt) /tmp/c2_actual.txt && echo IDENTICAL
IDENTICAL
```

**Both required measurements are confirmed against the control receipt.** The receipt is faithful: same
six per-repair verdicts, same `routed repairs verified 0 of 6` line, same exit 1. The receipt's
`base-exit=1` line is an annotation, not counter output.

Independent corroboration that the base is a genuine do-nothing world: at base `f3246d14` the six repair
substrings are absent from the measured blobs — `git show f3246d14:LOG.md` contains 0 occurrences each of
`plans/round-60.md`, `considerthese/2026-10-23.md`, `build reports`, `claimed 32`, `committed 29`,
`.ufo/waves/round-60/build`; `git show f3246d14:corpus/QUALITY.md` contains 0 occurrences of `Q56` and 0
of `byte-exact`; `corpus/lessons/round-61.md`, `.ufo/waves/round-61/census-after.txt` and
`.ufo/waves/round-61/receipts/controls-ancestry.txt` do not exist at base. The counter's 0-of-6 is a
true absence count, not a read failure.

---

## 5. Audit of `verifiers/check_routed_repairs.py` against `check_gate_registry.py`'s pinned rules

### 5.1 The rules that bind this row (all from the lane's committed `check_gate_registry.py`)

- **Universe** = blobs *directly* under `verifiers/` at the measured revision ending `.py`/`.sh`
  (`Tree.universe()`, `git ls-tree`, no recursion). Universe is **35 at tip**, **34 at base** — the
  counter is the 35th.
- **Exactly one row** must name the verifier; name cell compared lower-cased with backticks/asterisks
  stripped (`clean()`).
- **kind** ∈ {`gate`, `probe`}. A `gate` must declare `0=clean` and `1=failed`, and may not have
  self-test `none` nor pinned-values `none`.
- **Verdict map** pairs parse as `\d+\s*(=|->|→)\s*(clean|failed|could-not-evaluate)` (`PAIR_RE`); no
  code twice.
- **Self-test cell** = `none` or ≥1 backticked `` `--flag` ``; each named flag must be an **exact active
  handler** — a Python `add_argument` call whose **exact string argument** is that flag (AST), or a shell
  `case` arm whose exact pattern is that flag. Comments and longer lookalikes do not count.
- **Pinned values** = `none` | `in-file` | backticked repo-relative paths existing at the measured
  revision (no absolute, no `..`).
- **Write scope** non-empty and not `-`/`–`/`—`. **Owner** must be `kotoba`.
- **Parser end rules** (silent failure modes): only the *first* table under `## Gate registry` is read; a
  blank line after rows sets `done`; a heading of level ≤2 ends the section — **a row appended after a
  blank line is silently unread**; a literal `|` inside a cell shifts every later column.
- **Phantom**: any row naming a `verifiers/...` path outside the universe.

### 5.2 The checker file's own facts (the row must not over-claim these)

From `verifiers/check_routed_repairs.py` at `eb5e149`:

- `add_argument("--rev", default=None, …)` and `add_argument("--self-test", action="store_true")` — two
  exact flag handlers, and **only** these two. `--selftest` and `--fetch` are *not* handlers (measured:
  `has_flag_handler` → `False` for both). A row naming `--fetch` would be non-conformant.
- Exit codes: `0` iff K == 6, `1` otherwise, `2` = could-not-evaluate (unreadable rev / missing
  `LOG.md` or `corpus/QUALITY.md`). Measured end-to-end: nonexistent rev → stderr
  `routed repairs verified could-not-evaluate: unreadable rev`, exit **2**.
- The six repair patterns are frozen in `check_repairs()` (in-file); the counter reads committed blobs
  only (`git show <rev>:<path>`), writes nothing, uses no network, and its self-test fixtures are pure
  in-memory dicts. Pinned values are therefore genuinely **`in-file`**, and write scope is genuinely
  **`none`**.

### 5.3 The exact registry row text (copy-ready, one line, no wrapping)

Target path: `SKILL.md`, `## Gate registry` table. Insert **inside** the table, in the alphabetical slot
immediately after the `verifiers/check_plugin_manifests.py` row (`check_routed_repairs` < `check_scoped_rules`
sorts correctly there). **No blank line may separate the new row from the table above it**, and no `|` may
appear inside any cell.

```
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only; `git show` of committed blobs only) | kotoba |
```

### 5.4 Verification of that row by the lane's own judge (not by eye)

Harness: `verifiers/check_gate_registry.py` imported from the lane and its real `judge()` /
`judge_row()` / `cells()` / `clean()` / `has_flag_handler()` / `PAIR_RE` / `FLAG_RE` / `Tree` applied to the
committed tip tree. `date -u` = `Fri 23 Oct 2026 07:13:54 PM UTC` (row-validation run) and
`Fri 23 Oct 2026 07:16:05 PM UTC` (final, re-run at the moved HEAD).

```
== FINAL: row inserted at SKILL.md line 492 (alphabetical slot) ==
  verifiers/check_routed_repairs.py conformant=True why=[]
  => 35 of 35 conformant; phantom=[]
  (current committed SKILL.md, without the row: 34 of 35)

== cell-by-cell rule trace ==
  cells parsed: 8 (header width 8)
  name cell   clean='verifiers/check_routed_repairs.py' -> == path.lower()? True
  kind cell   clean='gate' in KINDS? True
  entry cell  contains path? True
  verdict map pairs=[('0', 'clean'), ('1', 'failed'), ('2', 'could-not-evaluate')] codes=['0', '1', '2'] dup=False
  gate needs 0=clean & 1=failed? True
  self-test cell flags=['--self-test'] handlers={'--self-test': True}
  pinned cell clean='in-file' (gate may not be 'none': True)
  write scope clean='none (read-only; git show of committed blobs only)' (empty/dash? False)
  owner cell  clean='kotoba' == OWNER? True
```

Flag truth table measured from the committed source (not inferred):

```
== has_flag_handler truth table ==
  --self-test  handler=True
  --rev        handler=True
  --selftest   handler=False
  --fetch      handler=False
```

Registry counter state, measured (`date -u` = `Fri 23 Oct 2026 07:18:21 PM UTC`):

```
$ python3 -B verifiers/check_gate_registry.py --self-test
self-test: 0 failure(s) over 28 assertions
exit=0

$ python3 -B verifiers/check_gate_registry.py --rev eb5e149
gate registry rows conformant 34 of 35 lane verifiers; phantom 0
```

The single nonconformance is exactly the missing row:

```
verifiers/check_routed_repairs.py            no registry rows naming it: 0 (need 1)
```

**With the §5.3 row inserted, the counter goes to 35 of 35, phantom 0** — verified by running the lane's
own `judge()` over the tip tree with the row spliced into the committed `SKILL.md` text at the stated slot.
The registry gate is therefore **red between freeze and integration**, and stays red until the L1 lands
the row. Any C2 report phrased "registry clean at tip" before that commit lands would be false.

### 5.5 Two row-shape cautions for the L1

1. **Phantom risk by measured revision.** The row names `verifiers/check_routed_repairs.py`, which does
   not exist at base `f3246d14`. Measured: at base the universe is 34 and the verifier is absent, so a
   row naming it there would be **PHANTOM**; at tip the universe is 35 and it is conformant. Land the
   row in the same integration commit that carries the repairs, and **measure the registry at a revision
   where the counter exists**.
2. **Parser end rule.** `registry_rows()` stops at the first blank line after the header row. If the row
   is appended at the *end of the file* or after a blank line following the table, it is silently not
   read and the counter still reports 34 of 35. Insert inside the table.

---

## 6. Attack on the C2 counter — what the six checks actually measure (calibration axis)

All probes below call the **committed** `check_repairs()` from the lane, with in-memory blob maps.
Re-confirmed against the hardened `eb5e149` file (`date -u` = `Fri 23 Oct 2026 07:14:16 PM UTC`):

| # | Probe | Result | Reading |
|---|---|---|---|
| A | `census-after.txt` present but **empty** | **raises `IndexError`** | see §6.1 — a crash, not a verdict |
| A | `census-after.txt` present but whitespace-only | **raises `IndexError`** | same |
| A | `exit=0` with no trailing newline / trailing blank lines | 6 of 6 | fine |
| A | `exit=0` followed by a later text line | 5 of 6 | last non-empty line is what counts |
| B | R-a tokens **scattered over 4 lines** + R-b/R-c on their own lines | **6 of 6** | the docstring's "on one line" is **not enforced** for R-a |
| C | R-a with the counting path as **prose**, no command | **6 of 6** | no counting command is required |
| D | R-a satisfied by `claimed 3200` / `committed 29x` | **6 of 6** | bare-substring false positive |
| E | R-c's two pointers on **two different lines** | 5 of 6 | R-c *does* enforce one line (correct) |
| F | R-f: `merge-base --is-ancestor` mentioned + an **unrelated** `exit 0` | **6 of 6** | R-f does not require the two on one line, nor that the run is the ancestry run |
| F | R-f: a real ancestry run that **failed** (`exit 1`) | 5 of 6 | a failing run is correctly rejected |
| G | lesson mentions `M91` only in prose, not as a Mistakes entry | **6 of 6** | R-e does not require M91 to be under `## Mistakes` |
| G | `Q56` present but `byte-exact` absent | 5 of 6 | both tokens required (correct) |
| H | LOG.md alone carries R-a, R-b, R-c | 3 of 6 from one file | one file can satisfy three of six |

**Independent corroboration.** Sibling seat `CriticHollowC2` (report
`.ufo/waves/round-61/wave/CriticHollowC2.md`, read after my probes were run) independently reproduced
the same `IndexError` on empty/whitespace census input, and extends the same class to three dishonest
worlds that score 6 of 6 — cosmetic LOG material, body-empty census receipts ending `exit=0`, and
self-asserted ancestry. Its finding and mine are the same finding from two directions: **the counter
scores lexical presence, not substantive repair.** Its specific contribution beyond mine is the
reflexive-ancestry counterexample (`git merge-base --is-ancestor BASE BASE` → exit 0), recorded in
§7 item 5. I re-verified that claim myself rather than relaying it.

The counter discloses this boundary in its own header ("it does not judge whether a repair text is
substantively honest — reviewers remain responsible for that (Q31)"), so the finding is **not** a claim
that the counter is misdesigned — it is a calibration statement about what `6 of 6` may be cited as
evidence of. The L1 should treat `routed repairs verified 6 of 6` as **necessary but not sufficient**
for C2, and cite the repair texts and their receipts alongside it.

### 6.1 The one crash surface — `R-d` on an empty census-after file (needs L1 attention)

`check_repairs()` builds R-d as:

```python
rd = (
    census is not None
    and [ln for ln in census.splitlines() if ln.strip()][-1].strip() == "exit=0"
    if census is not None
    else False
)
```

When `census-after.txt` **exists but has no non-empty line**, the list comprehension is empty and
`[-1]` raises `IndexError`. Reproduced end-to-end through `main()` in a scratch clone (not the lane):
exit code **1** with an `IndexError` traceback on stderr and **no** `routed repairs verified K of 6`
line at all.

Consequence for the L1: the counter's declared contract is "exit 2 = could not evaluate". An empty
census-after file instead produces a **traceback with exit 1** — an exit-1 that reads exactly like
"the six repairs did not land" but is actually a crash in the instrument. Since the L1 lands
`.ufo/waves/round-61/census-after.txt` this round, this is reachable. Two mitigations, either is
sufficient: (a) ensure the committed census-after file is never empty (it ends `exit=0` by the R-d rule
anyway, so an empty file means the census command produced nothing — check its exit code before
committing), and (b) when reading the C2 measurement, **require the `routed repairs verified K of 6` line
to be present**; a missing line with exit 1 is a crash, not a verdict.

Note this is a defect in the *frozen* checker, so this seat did **not** and must not patch it — the
counter is frozen at the plan commit and a later change is a second measurement (Q28). It is reported as
a landing hazard for the L1, and as a candidate for a future round's erratum.

### 6.2 The token spellings each repair needs (derived from the committed source, exact)

| Repair | Where | Required tokens, exactly | Enforced shape |
|---|---|---|---|
| R-a | `LOG.md` | `build reports`, `claimed 32`, `committed 29`, `.ufo/waves/round-60/build` | anywhere in the file (**not** one line, despite the docstring) |
| R-b | `LOG.md` | `plans/round-60.md`, `considerthese/2026-10-23.md` | anywhere in the file, any lines |
| R-c | `LOG.md` | `receipts/freeze2-selftest.txt` **and** `C1-measure.txt` | **on one line** (any single line) |
| R-d | `.ufo/waves/round-61/census-after.txt` | last non-empty line is exactly `exit=0` | equals sign, lowercase, alone on the line |
| R-e | `corpus/QUALITY.md` + `corpus/lessons/round-61.md` | `Q56` **and** `byte-exact` in QUALITY.md; `M91` anywhere in the lesson file | tokens may sit on different lines |
| R-f | `.ufo/waves/round-61/receipts/controls-ancestry.txt` | `merge-base --is-ancestor` **and** `exit 0` | anywhere in the file; **`exit 0` with a space, not `exit=0`** |

**The `exit 0` vs `exit=0` asymmetry is the highest-risk token.** Measured: R-f with `exit 0` (space)
→ 6 of 6; R-f with `exit=0` (equals) → **5 of 6**. R-d is the opposite: `exit=0` (equals) is required
and `Exit=0` or `exit=0 (ok)` → 5 of 6. The two receipts use different conventions and the counter
distinguishes them.

**The R-a counting command must be the one that actually yields 29.** The committed fixture in the
counter's own self-test uses `` (`ls .ufo/waves/round-60/build | wc -l`) `` — but that command yields
**33** at tip, not 29. Measured at tip:

```
all entries:         33
*.md:                30
*.md minus fixture:  29
```

The 33 entries are 30 `.md` files (of which `check_word_counts.fixture.md` is a fixture, not a seat
report) plus 3 non-`.md` files (`ExecIndexCorpus.patch`, `check_word_counts.py`, `swarm-registry.json`).
The r60 lesson's "29 build reports" excludes the fixture and the 3 non-report files, and names the three
absent seat reports — all three verified absent at tip: `ExecBudgetMove.md`, `ExecGateRegistry.md`,
`ExecShonenPointer.md`. So the honest counting command is:

```
ls .ufo/waves/round-60/build/*.md | grep -v check_word_counts.fixture.md | wc -l    -> 29
```

Since R-a does not evaluate any command (§6 probe C), a LOG.md line citing the 33-yielding command next
to the words "committed 29" would still score R-a as landed. **This is precisely the class of defect R-a
exists to repair** (a count overstated against committed bytes), so the L1 should cite the
29-yielding command. A reviewer can check this by running the command; the counter cannot.

---

## 7. Landing hazards the L1 should know about (each measured, none speculative)

1. **`corpus/lessons/round-61.md` (R-e) needs a `corpus/README.md` coverage-map row**, or the corpus
   gate goes further red. Measured with the lane's own `verify_corpus_integrity.index_findings()` over
   the committed README and the tip tree: with the lesson file tracked but **no** README row →
   `unindexed=2` (adding `corpus/lessons/round-61.md` to the pre-existing `corpus/lessons/round-60-verifier-spotcheck.md`).
   With a coverage-map row whose column-2 token is `` `lessons/round-61.md` `` → `unindexed=1`, back to
   the pre-existing value. The token harvests cleanly: `exclusion_reason=None`, `corpus_internal=True`,
   `expand_pattern` hits `['lessons/round-61.md']`. The row must go **inside the `## Coverage map`
   section** and carry the file token in **column 2** (the `File` column) — the harvest reads column-2
   backticked tokens only. Note `corpus/lessons/round-60-verifier-spotcheck.md` is **already** unindexed
   at tip (a pre-existing debt, not this round's): `verify_corpus_integrity.py` reports
   `corpus.index tracked=100 unindexed=1` and exits **1** at tip. That redness is pre-existing and
   out of C2's six repairs; R-e must not make it worse.
2. **`SKILL.md` line budget has 9 lines of headroom.** The trigger-fidelity box states "File ≤ 600 lines";
   `SKILL.md` is **591 lines** at tip. The registry row costs 1 line (→ 592). The r61 plan's other
   SKILL.md edits (the v3 rows and S112–S115 entries) must fit in the same 9-line budget.
3. **`.ufo/waves/...` is committable; only `.ufo`, `.ufo/state` and `.ufo/watchdog.log` are barred.**
   `scripts/hyaku/jj-lane.sh`'s `repo_path_allowed()` rejects exactly `.ufo|.ufo/state|.ufo/state/*|.ufo/watchdog.log`,
   so the R-d and R-f receipt paths under `.ufo/waves/round-61/` are landable by the L1 through
   `jj-lane.sh commit`. The freeze commit itself proves it: `git ls-tree 7827628 .ufo/waves/round-61/`
   lists `census-before.txt` and `controls/C2-base.txt`.
4. **R-c's two pointers must share one LOG.md line.** Put the erratum on a single line, e.g. naming
   `receipts/freeze2-selftest.txt` and `C1-measure.txt` together — verified that splitting them across
   two lines drops R-c to 5 of 6.
5. **R-f needs the real ancestry run, with `exit 0` on a space — and it must be NON-reflexive.** The
   receipt should contain the literal command `git merge-base --is-ancestor` and a line `exit 0`.
   Measured at the current HEAD:
   `git merge-base --is-ancestor 7827628a939b0333c89892dfcedc72e390ccfb60 master` → **exit 0**, so the
   freeze commit (which carries the C2 control receipt) does precede the branch tip. The L1 must re-run
   this against the *actual* control-receipts commit and the *actual* C1 data commit at integration time
   and record that run's own exit code — not a re-derivation of mine.
   **Hazard (measured, and independently reported by sibling `CriticHollowC2`):** R-f checks only that
   the receipt *text* contains `merge-base --is-ancestor` and `exit 0`. It performs no graph or object
   verification, so a **reflexive** relation satisfies it. I measured
   `git merge-base --is-ancestor 7827628… 7827628…` → **exit 0** — a truthful but vacuous
   "is-ancestor" of a commit against *itself*, which would let a receipt assert ancestry that was never
   actually tested between two distinct commits. The receipt must therefore name **two distinct
   commits** (control-receipts commit and C1 data commit) and the L1 must run the relation between
   those two distinct commits; a receipt that reuses one hash on both sides is a hollow pass.
6. **R-d's census-after file must end `exit=0` on its own line**, and must not be empty (§6.1). The
   committed `census-before.txt` ends with the census output line then `exit=0` (bytes verified:
   `… SOURCES.md\nexit=0\n`), which is the shape to copy. Note the r60 predecessor
   `.ufo/waves/round-60/census-start.txt` ends `exit 0` (space) — a different convention, and the wrong
   one for R-d.
7. **C3 was withdrawn before data** by erratum E1 (`c630c4c`): the C3 counter could not measure the axis
   property, so C3 is retired unmeasured and the round's claims are C1 and C2 only. This does not change
   C2's six repairs or the counter; it does mean any C2 report that cites a C3 count would be stale.
8. **The counter's default `--rev` is `master`** (`git rev-parse --verify master`). The C2 measurement
   must pass an explicit `--rev <tip>`; the plan's predicate does so, and the base control receipt used
   an explicit hash.

---

## 8. Scope and honesty statement

- **Verified by execution**: every command output pasted above was run by this seat, with its
  `date -u` and exit code. The registry row's conformance was decided by the lane's own
  `check_gate_registry.py` functions, not by reading.
- **Not verified / could not verify**: I did **not** run the C2 measurement at a revision where the six
  repairs have landed — that revision does not exist yet; the L1 creates it. Consequently the
  `routed repairs verified 6 of 6` / exit 0 half of the C2 predicate is **untested by this seat** and
  remains the L1's measurement. I also did not run `verify_skill_checklist.py` or the C1 counter, which
  are outside this seat's assignment. The `corpus/README.md` coverage-map conclusion in §7.1 is a
  computation over the lane's committed `index_findings()`, not a run of the full corpus verifier against
  a tree carrying the new lesson file.
- **Scratch is untrusted and is not cited as evidence.** The harnesses under
  `/fast/scratch/hyaku/kotoba-r61/ExecC2Tip/` (`validate_row.py`, `attack_counter.py`, `token_probe.py`,
  `final_validate.py`, `corpus_index_probe.py`) exist only to import the lane's committed functions; every
  number in this report is traceable to a lane artifact or a lane-command output.
- **No lane, fleet, sibling, `.ufo/state`, or git/jj index file was written.** The only write by this
  seat is this report file.

---

## 9. Files changed

- `.ufo/waves/round-61/wave/ExecC2Tip.md` — this report (the seat's only write).
- No other file, in any repo, was created, edited, deleted, committed, or staged by this seat.

## 10. Drafts — copy-ready text for the L1

### 10.1 The gate-registry row (target: `SKILL.md`, `## Gate registry` table, after the `check_plugin_manifests.py` row)

```
| `verifiers/check_routed_repairs.py` | gate | `python3 -B verifiers/check_routed_repairs.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | in-file | none (read-only; `git show` of committed blobs only) | kotoba |
```

### 10.2 A `corpus/README.md` coverage-map row for the R-e lesson file (target: `corpus/README.md`, inside `## Coverage map`)

```
| Round-61 lessons | `lessons/round-61.md` | LOG.md round-61 entry; `## Mistakes` M91, M92; `## Gate` S112–S115 |
```

(The `File` column carries the backticked token `` `lessons/round-61.md` ``; the `Basis` column is the
L1's to write. This row is **not** part of the six C2 repairs — it is the adjacent-gate condition that
keeps R-e from deepening the corpus gate's redness.)

### 10.3 R-a's counting command, verified against committed bytes (target: the `LOG.md` line carrying R-a)

```
ls .ufo/waves/round-60/build/*.md | grep -v check_word_counts.fixture.md | wc -l    -> 29
```

---

## 11. Installs

**No installs.** The task required only `python3 -B` runs of the lane's committed checkers plus `git`,
`diff`, `od`, `grep`, `sed` — all preinstalled. No pacman transaction was attempted (pacman is PAUSED
host-wide per the orchestrator ruling). No `uv tool`/`npx`/binary install was needed.

## 12. Blockers

**None.** (One coordination note, not a blocker: the C2 counter's self-test was hardened by the L1 during
this wave — freeze `7827628` carried 9 arms, current `HEAD` `eb5e149` carries 12 — and I re-verified every
finding in §5 and §6 against the current file; the six frozen scoring checks are unchanged.)

## 13. One line

I attacked the committed C2 counter's six frozen checks and the r60 evidentiary ground behind them
(exposing one `IndexError` crash surface on an empty census-after file, four leniency gaps that the
counter cannot see, the `exit 0`/`exit=0` token asymmetry, and a 33-vs-29 counting-command trap in R-a's
own fixture), confirmed the C2 base control receipt byte-for-byte against live re-runs of both required
commands, and produced the exact, judge-verified gate-registry row text that takes the registry counter
from 34 of 35 to 35 of 35 with zero phantom rows on the L1's first try.
