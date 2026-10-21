verdict: HOLDS — every pointer in `corpus/lessons/round-47.md` M21 (line 20) and M22 (line 21) re-runs to the recorded output at the named commits; the defects found are calibration-grade only (M22's M13 sub-claim is unanchored and is now unreproducible at HEAD, and M22's own row uses the bare line numbers its fix column forbids).

# W2LessonM21M22 — falsify of round-47 lessons M21 + M22

Lane: round-47 falsify, post-crash wave 2. Target commit: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`
("round-47: C1 re-derive+re-pin omp 18.12.5/opencode 1.19.3; C2 trigger.no_xml_tag; C3 governance erratum + corpus index; frontier S012-S015, M20-M22, Q19; wave-1 evidence").
BASE of the round under audit: `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.

## Scope and method

- Read the two target rows at the landed commit: `corpus/lessons/round-47.md:20` (M21) and `corpus/lessons/round-47.md:21` (M22), full raw text (`:19-21:raw`).
- Every pointer was re-run, not read. Environment: canonical-layout scratch clone at
  `/fast/scratch/kotoba-r47/w2/W2LessonM21M22/kotoba-shokunin` (detached at `7ad7fad`), plus four
  detached worktrees of the same clone: `wt-base` (`c61a973`), `wt-parent` (`04192c2`),
  `wt-78ee` (`78ee57e`), `wt-f2f9` (`f2f9ee1`). The production repo
  `/home/vgpnk/Projects/shokunin/kotoba-shokunin` was never written except for this report and one
  artifact under `.ufo/waves/round-47/falsify/`.
- Raw command/exit/output transcript: `.ufo/waves/round-47/falsify/W2LessonM21M22.pointer-runs.txt`.
  The first block of that transcript wraps several commands in `| tail`/`| cut`, so its `EXIT=` is the
  *pipeline's* exit; an appended second block re-runs the gate commands with no pipeline and records
  their direct exit codes (BASE integrity `--json` → **1**, BASE integrity → **1**, BASE independent →
  **1**, parent `04192c2` integrity `--json` → **0**, parent independent → **0**, `7ad7fad` integrity →
  **0**, `7ad7fad` integrity `--self-test` → **0**, `7ad7fad` independent → **0**, `7ad7fad`
  independent `--json` → **0**). The exit codes quoted in this report are the direct ones.
- No tools were installed or upgraded (none needed; git 2.56.0 and the repo's own python3 were
  sufficient). No pacman transaction was attempted, so the host-wide pacman pause was not touched.

---

## Findings (by severity)

### F1 — MINOR / calibration: M22's M13 sub-claim is unanchored and is no longer reproducible at HEAD

`corpus/lessons/round-47.md:21` (M22) asserts three sub-claims. Two of them name the commit where
the measurement was taken; the third does not:

> M5 cites `SCORECARD.md:165`/`:100`, which rotted +8 lines at `f2f9ee1`; **M13 cites `SKILL.md:15`,
> the token sat on `:14`** (`.ufo/waves/round-47/build/MistakeSweepOthers.md` N1–N3)

The M2 sub-claim is anchored ("line 76 at `78ee57e` and at BASE"), and the M5 sub-claim is anchored
("at `f2f9ee1`"). The M13 sub-claim is not anchored to any commit, and round 47's own C2 change
removed the token it describes — so at HEAD the assertion cannot be re-run at all.

Repro (clone at `7ad7fad`):

```
$ grep -n '<skills>' SKILL.md | head -2
22:On **omp** the `<skills>` catalogue (template in the omp ELF, rendered per
91:| omp | `<skills>` (ELF template) | ...
$ sed -n '14p' SKILL.md
  never reach the omp skills router — craft here is audit-side, not
$ sed -n '15p' SKILL.md
  router-visible.
```

versus at BASE `c61a973` (where the token really was on line 14 of the frontmatter description):

```
$ git show c61a973:SKILL.md | grep -n '<skills>' | head -2
14:  never reach the `<skills>` router — craft here is audit-side, not
22:On **omp** the `<skills>` catalogue (template in the omp ELF, rendered per
```

At `7ad7fad` the frontmatter description no longer contains the literal `<skills>` token at all
(C2's `trigger.no_xml_tag` repair rewrote it to "the omp skills router"), so `SKILL.md:15` at HEAD is
the string `  router-visible.` — a line that has nothing to do with the claim. A reader who tries to
re-run M22's M13 sub-claim at the commit the lesson ships in gets a false negative and no signal
that the pointer is historical.

Severity is calibration, not correctness: the *class* being recorded (a lesson's own `file:line`
pointer is stale) is exactly right, and the row's own fix column names the right remedy ("cite
anchor text with its `grep -n` command"). The defect is that the row does not apply that remedy to
itself. Concrete remediation, consistent with the row's own stated convention: anchor the M13
sub-claim to a commit (e.g. "at `78ee57e` and at BASE") and replace `SKILL.md:15` with the anchor
text + `grep -n '<skills>' SKILL.md` output.

### F2 — MINOR / calibration: M22's row violates the citation convention its own fix column states

Same row, `corpus/lessons/round-47.md:21`. The fix column ends:

> This lesson cites anchor text with its `grep -n` command instead of bare line numbers wherever a
> line can move.

Measured against the file that contains it:

- The row's M2 sub-claim supplies the `grep -n` command and its output. ✔
- The row's M5 sub-claim supplies bare line numbers (`SCORECARD.md:165`/`:100`) with **no** anchor
  text and **no** re-runnable command. The reader has to open
  `.ufo/waves/round-47/build/MistakeSweepOthers.md` N2 to learn which two lines were meant. ✘
- The row's M13 sub-claim supplies a bare line number (`SKILL.md:15`) plus `:14`, again with no
  anchor text and no command. ✘
- The row's own inline citations — `SCORECARD.md:80`, `SCORECARD.md:165`, `:100`, `SKILL.md:15` —
  are bare line numbers into the two most rot-prone files in the repo (an append-in-place scorecard
  and a SKILL.md that this very round rewrote). ✘

Machine check at `7ad7fad` (all backticked path tokens in the file scanned for existence — all
resolve; but the *line*-qualified ones do not carry a command):

```
$ grep -oE '`[^`]*:[0-9]+[^`]*`' corpus/lessons/round-47.md | sort -u
`:100`
`:14`
`LOG.md:2111`
`SCORECARD.md:165`
`SCORECARD.md:80`
`SKILL.md:15`
`skills/skill-creator/scripts/quick_validate.py:81`
```

This is a *self-inconsistency* finding, not a false claim: the row's statement about "this lesson"
is true of the M2 sub-claim and false of the M5/M13 sub-claims. It is the same class the row
itself names (bare line numbers into files that move), landed in the row that names it — which is
what an honest lesson file should be judged against.

Note the two non-defects in that list, for completeness:
- `LOG.md:2111` (header, `corpus/lessons/round-47.md:7`) is a bare line number into an append-only
  LOG, but it is defended by the C3 `GOVERNANCE_ERRATA` pin (line sha256 + horizon), and I measured
  it still resolves: `sed -n '2111p' LOG.md` at `7ad7fad` is byte-identical to BASE, and LOG.md is
  2326 lines (the pinned horizon 2315 is a bound on the *cited* line, not on file length).
- `skills/skill-creator/scripts/quick_validate.py:81` (Gate table, S012) is a citation into an
  external fetched file carried with a sha256 pin (`67cf5703…`), which is the intended discipline.

### F3 — MINOR / calibration: M21's fix cell does not record the value it re-recorded

`corpus/lessons/round-47.md:20` (M21) fix cell:

> Indexed this round (`corpus/README.md` row) with the baseline re-recorded; …

The re-recorded value lives only in `verifiers/corpus-baseline.json` — `expect` 58 → 60 at
`verifiers/corpus-baseline.json:15`, with the justification note at
`verifiers/corpus-baseline.json:58` ("corpus.index.tracked_files 58 -> 60: …"). The lesson row
itself never states the number, so a reader auditing M21's fix must cross-read the baseline to see
that the pin moved and that it moved by two files (the round-46 spot-check *and* round-47.md).
For a row whose whole subject is "a number in one file drifted from the number in another", the
lesson should name the number. Cheap remediation: append "(pin 58 → 60)" to the fix cell.

### F4 — INFO / confirmation: M21's `captured-by` is accurate, and the fix demonstrably can fail

- Both named instruments do catch the class: at BASE `c61a973`,
  `python3 -B verifiers/verify_corpus_integrity.py` exits 1 and
  `python3 -B verifiers/verify_corpus_independent.py` exits 1.
- The fix can fail (mutation, run in the scratch clone at `7ad7fad`, then restored —
  `git diff --stat` empty afterwards): deleting the index row `corpus/README.md:63` from the
  coverage map gives

  ```
  DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
  8/9 checks pass; DRIFT: corpus.index.unindexed
  EXIT=1
  ```

  so the fix is not a no-op and the instrument still binds.
- The round-47 landing does **not** repeat the M21 class: `git show --stat 7ad7fad -- corpus` adds
  `corpus/lessons/round-47.md` (58 lines) and the coverage map has a matching row at
  `corpus/README.md:64`; the pin at `verifiers/corpus-baseline.json:15` is 60; both corpus
  instruments exit 0 at `7ad7fad` (`9/9 checks pass`; independent exit 0).

### F5 — INFO / confirmation: M22's `captured-by: none` is accurate

The row's parenthetical — "`governance.citation_resolves` resolves path tokens in LOG/SCORECARD
only, never `file:line` content" — is correct against the code:
`verifiers/verify_skill_checklist.py:187` documents the check as "the same existence predicate
over repo-root `LOG.md` and `SCORECARD.md`", and the implementation
(`verifiers/verify_skill_checklist.py:1360`, `citation_resolve`) is a pure path-existence test
(`safe_resolve` / bounded `..` hops) with no line-number inspection anywhere in it. A repo-wide
grep for an instrument that would resolve a `:NN` citation found none: `verifiers/verify_corpus_integrity.py`
and `verifiers/verify_corpus_independent.py` check coverage-map paths, `.ufo/reports/round-N/*.md`
report pointers and commit hashes only. So "none" is right, and no gate in the repo would have
flagged M2/M5/M13.

---

## Pointer-by-pointer re-run (commands, exit codes, key output)

### M21 — `corpus/lessons/round-47.md:20`

| # | pointer in the row | command run | exit | key output | verdict |
|---|---|---|---|---|---|
| M21-1 | "`git show --stat c61a973` → adds `corpus/lessons/round-46-verifier-spotcheck.md` only" | `git -C kotoba-shokunin show --stat c61a973` | 0 | `corpus/lessons/round-46-verifier-spotcheck.md \| 17 +++++++++++++++++` / `1 file changed, 17 insertions(+)` — no other file | ✔ holds exactly |
| M21-2 | "at `c61a973` `python3 -B verifiers/verify_corpus_integrity.py --json` → exit 1 (`tracked_files` 59≠58, `unindexed` 1)" | `cd wt-base && python3 -B verifiers/verify_corpus_integrity.py --json` | **1** | `"tracked_files": 59`, `"unindexed": 1`, `"unindexed_detail": ["corpus/lessons/round-46-verifier-spotcheck.md"]`; results: `corpus.index.tracked_files observed=59 expected=58 DRIFT`, `corpus.index.unindexed observed=1 expected=0 / empty DRIFT` | ✔ holds exactly |
| M21-3 | "and at parent `04192c2` → exit 0" | `cd wt-parent && python3 -B verifiers/verify_corpus_integrity.py` | **0** | `tracked=58 unindexed=0 stale=0 missing=0` … `9/9 checks pass`; `git rev-parse c61a973^` = `04192c25268ed8397fd327b865f532b293396bc6` (so `04192c2` really is the parent) | ✔ holds exactly |
| M21-3b | (corroboration, not in the row) | `cd wt-base && python3 -B verifiers/verify_corpus_independent.py` | **1** | `corpus.index.unindexed observed=1 DRIFT` … `exit 1` | ✔ consistent with the row's `captured-by` |
| M21-4 | fix: "Indexed this round (`corpus/README.md` row) with the baseline re-recorded" | `grep -n 'round-46-verifier-spotcheck\|round-47.md' corpus/README.md`; `grep -n 'tracked_files' -A3 verifiers/corpus-baseline.json`; `python3 -B verifiers/verify_corpus_integrity.py` | 0 / 0 / **0** | `corpus/README.md:63` = spot-check row, `corpus/README.md:64` = round-47 lessons row; `verifiers/corpus-baseline.json:15` `"expect": 60`; `9/9 checks pass` | ✔ holds (see F3 for the in-row omission) |
| M21-5 | fix-can-fail (my mutation) | delete `corpus/README.md:63` in the scratch clone, re-run integrity, restore | **1** | `DRIFT corpus.index.unindexed: observed=1 expected=0 / empty` / `8/9 checks pass` | ✔ instrument still binds |
| M21-6 | evidence pointer `.ufo/waves/round-47/build/MistakeUnindexedLanding.md` | `git ls-files .ufo/waves/round-47/build/ \| grep -E 'MistakeUnindexedLanding'` | 0 | `.ufo/waves/round-47/build/MistakeUnindexedLanding.md` (+ `.patch`) — tracked in the landed commit, resolves | ✔ holds |

### M22 — `corpus/lessons/round-47.md:21`

| # | pointer in the row | command run | exit | key output | verdict |
|---|---|---|---|---|---|
| M22-1 | "M2 cites `SCORECARD.md:80` for 'complete-census condition is UNMET', but `grep -n 'complete-census condition is UNMET' SCORECARD.md` → line 76 at `78ee57e`" | `cd wt-78ee && grep -n 'complete-census condition is UNMET' SCORECARD.md` | 0 | `76:**Round 41 completed (loop A position 5 — the 64-seat VERIFICATION round; …` | ✔ holds exactly |
| M22-1b | "… and at BASE (wrong at birth)" | `cd wt-base && grep -n 'complete-census condition is UNMET' SCORECARD.md` | 0 | `76:` (same line) | ✔ holds exactly |
| M22-1c | the cited `SCORECARD.md:80` really is a different quote (counterexample) | `cd wt-base && sed -n '80p' SCORECARD.md`; `sed -n '80p' SCORECARD.md \| grep -c 'complete-census'` | 0 / 1 | `**Round 41 calibration annotation (append-only; round-40 seat denominator).** …`; count `0` | ✔ the pointer is wrong, not the anchor |
| M22-1d | the row's M2 subject exists as quoted | `cd wt-base && grep -n '^| M' corpus/lessons/round-46.md` | 0 | `20:\| M2 Finite census sold as exhaustive \| `SCORECARD.md:80` r41 annotation → "complete-census condition is UNMET"; …` | ✔ the quoted citation is verbatim |
| M22-2 | "M5 cites `SCORECARD.md:165`/`:100`, which rotted +8 lines at `f2f9ee1`" | `cd wt-78ee && grep -n 'fix introduced a None-path crash + malformed-field arm survives' SCORECARD.md`; `grep -n '^\*\*Round 38 completed' SCORECARD.md` | 0 / 0 | `165:\| 38 \| operability \| … None-path crash …` and `100:**Round 38 completed (loop A position 2; REJECTED — …` | ✔ at `78ee57e` both cited lines resolve exactly |
| M22-2b | "+8 at `f2f9ee1`" | `cd wt-f2f9 && grep -n 'fix introduced a None-path crash …' SCORECARD.md`; `grep -n '^\*\*Round 38 completed' SCORECARD.md` | 0 / 0 | `173:` and `108:` — 165+8 and 100+8 | ✔ holds exactly |
| M22-2c | mechanism (my measurement) | `git diff 78ee57e f2f9ee1 -- SCORECARD.md \| grep '^@@'` | 0 | hunks `@@ -25,12 +25,12 @@`, `@@ -95,6 +95,14 @@` (the +8 insert), `@@ -212,6 +220,14 @@`, `@@ -262,3 +278,6 @@`; numstat `22 3` | ✔ the +8 is real and sits above both anchors |
| M22-2d | the rot persists to BASE | `cd wt-base && grep -n '^\*\*Round 38 completed' SCORECARD.md`; `sed -n '165p' SCORECARD.md` | 0 | `108:`; `sed 165p` = `\| 33 \| operability \| 8.5 — box-map parity had no absolute floor; …` (row 33, not row 38) | ✔ |
| M22-3 | "M13 cites `SKILL.md:15`, the token sat on `:14`" | `cd wt-base && grep -n '<skills>' SKILL.md \| head -1`; `sed -n '14p;15p' SKILL.md` | 0 | `14:  never reach the `<skills>` router — craft here is audit-side, not`; line 15 = `  router-visible.` | ✔ holds **at BASE / `78ee57e`** |
| M22-3b | same pointer at the landed commit | `cd kotoba-shokunin && grep -n '<skills>' SKILL.md \| head -1`; `sed -n '14p;15p' SKILL.md` | 0 | first hit is `22:`; line 14 = `  never reach the omp skills router …`, line 15 = `  router-visible.` | ✘ **unreproducible at HEAD** → F1 |
| M22-4 | `captured-by`: "none (`governance.citation_resolves` resolves path tokens in LOG/SCORECARD only, never `file:line` content)" | `sed -n '187,197p' verifiers/verify_skill_checklist.py`; `sed -n '1360,1380p' verifiers/verify_skill_checklist.py`; `grep -rn 'file:line\|line citation\|line pointer' verifiers/` | 0 / 0 / 1 | docstring: "the same existence predicate over repo-root `LOG.md` and `SCORECARD.md`"; impl: `safe_resolve(tok, repo, repo)` / bounded `..` hops, existence only; grep → no hits | ✔ holds exactly ("none" is correct) |
| M22-5 | fix: "The round-46 lesson stays append-only" | `git show --stat 7ad7fad -- corpus` | 0 | corpus files touched: `QUALITY.md`, `README.md`, `SOURCES.md`, `knowledge/instruction-surface-census-round13.md`, `lessons/round-47.md` — `corpus/lessons/round-46.md` **not** touched | ✔ holds |
| M22-6 | fix: "This lesson cites anchor text with its `grep -n` command instead of bare line numbers wherever a line can move" | `grep -oE '`[^`]*:[0-9]+[^`]*`' corpus/lessons/round-47.md \| sort -u` | 0 | `` `:100` ``, `` `:14` ``, `` `LOG.md:2111` ``, `` `SCORECARD.md:165` ``, `` `SCORECARD.md:80` ``, `` `SKILL.md:15` ``, `` `skills/skill-creator/scripts/quick_validate.py:81` `` | ✘ **partly false for its own row** → F2 |
| M22-7 | evidence pointer `.ufo/waves/round-47/build/MistakeSweepOthers.md` | `git ls-files .ufo/waves/round-47/build/ \| grep MistakeSweepOthers` | 0 | `.ufo/waves/round-47/build/MistakeSweepOthers.md` — tracked, resolves | ✔ holds |
| M22-8 | the build report's own N1–N3 (corroboration) | read `.ufo/waves/round-47/build/MistakeSweepOthers.md:11,20,28` | 0 | N1 "`SCORECARD.md:80` vs `:76`"; N2 "`:165`→`:173`, `:100`→`:108`"; N3 "`SKILL.md:15` is off by one; the token is on `:14`" | ✔ consistent with my independent measurements |

### Every path token in the round-47 lesson resolves at `7ad7fad`

```
$ python3 <scan of backticked path tokens in corpus/lessons/round-47.md>
TOKENS: 26
MISSING at 7ad7fad:
(none)
```

Corroborating runs at `7ad7fad`: `verify_corpus_integrity.py` → exit 0 (`9/9 checks pass`);
`verify_corpus_integrity.py --self-test` → exit 0 (`0 failure(s) over 150 assertions`);
`verify_corpus_independent.py` → exit 0; `verify_corpus_independent.py --json` → exit 0
(`"head": "7ad7fad"`). The M21/M22 rows therefore do not break any live gate at the landed commit.

---

## Counterexamples (with repro)

**C1 (F1) — M22's M13 sub-claim cannot be re-run at HEAD.**

```
$ cd <clone at 7ad7fad>
$ grep -n '<skills>' SKILL.md | head -1
22:On **omp** the `<skills>` catalogue (template in the omp ELF, rendered per
$ sed -n '15p' SKILL.md
  router-visible.
# BASE c61a973 for comparison:
$ git show c61a973:SKILL.md | grep -n '<skills>' | head -1
14:  never reach the `<skills>` router — craft here is audit-side, not
```

Impact: the row's M13 assertion is true only for a commit it does not name; at the commit the
lesson ships in, the cited line carries different text and the cited token no longer exists in the
file at all. Severity: calibration (the class claim is right; the pointer is not reproducible).

**C2 (F2) — M22's own row contains the class it names.**

```
$ grep -oE '`[^`]*:[0-9]+[^`]*`' corpus/lessons/round-47.md | sort -u
`:100`  `:14`  `LOG.md:2111`  `SCORECARD.md:165`  `SCORECARD.md:80`  `SKILL.md:15`
`skills/skill-creator/scripts/quick_validate.py:81`
```

Only the M2 sub-claim carries the `grep -n` command its own fix column prescribes; the M5 and M13
sub-claims are bare line numbers, and the M13 one is dead at HEAD (C1).

**C3 (F3) — M21's fix cell omits the number it re-recorded.** `corpus/lessons/round-47.md:20` says
"the baseline re-recorded" without stating 58 → 60; the value is only at
`verifiers/corpus-baseline.json:15` (`:15` → `"expect": 60`) and its rationale at
`verifiers/corpus-baseline.json:58`.

---

## What I did NOT check (residual risk / verification gaps)

- **M20 and the rest of the lesson** (`corpus/lessons/round-47.md:19`, the `## Gate` table S012–S015,
  the C1 class ledger pointer, `corpus/SOURCES.md`, `corpus/QUALITY.md` Q19) — out of scope for this
  lane; a sibling lane owns M20 and others own the Gate rows.
- **C1 freshness, C2 operability, C3 erratum** — not attacked here; the C3 `GOVERNANCE_ERRATA` row
  and `LOG.md:2111` were only checked as far as they appear inside the M22 citation (line identity
  at `7ad7fad` vs BASE, and the fact that the pointer is sha256-pinned). I did **not** re-derive the
  erratum's sha256/horizon arithmetic, and did not run `verify_skill_checklist.py`,
  `verify_surfaces.py` or `check_substrate_pins.py`.
- **The fleet-root identity of `../LOG.md` / `../SCORECARD.md`** — I ran every grep inside the lane
  clone, not against the fleet root; the M22 pointers were reproduced against the lane's own
  `SCORECARD.md` at `78ee57e` / `f2f9ee1` / `c61a973`, which is what the lesson cites.
- **History beyond the four commits named** — I did not re-derive the wave-1 report's wider claims
  (9/30 orphan landings, the per-commit spot-measures of `0f658ff`/`63ceba7`/`683d147`/`b0c7cb2`/
  `911b870`/`cd4798b`, and the "untracked file is invisible" staging probe). I took the M21 row's
  class statement at its single named instance rather than re-measuring the whole history.
- **The `README.md` corpus-index mutation** (F4/M21-5) was run only in the scratch clone, with the
  production tree never modified; the two-artifact requirement (index row **and** pin) was not
  re-tested arm-by-arm (the wave-1 report's §4 items 2/3/5/6).
- **`governance.citation_resolves` behaviour** was read, not executed against a mutated `SKILL.md`;
  I confirmed the code path is an existence test, but I did not run the instrument with a
  `file:line` citation to observe its (non-)behaviour empirically.
- **No live `omp` / `opencode` binary was executed** (out of scope for these two rows); the frozen
  substrate was not touched.
