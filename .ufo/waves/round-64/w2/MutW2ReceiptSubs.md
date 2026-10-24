# MutW2ReceiptSubs — receipt-side substitution attack on the C2 counter (wave 2, falsify)

Date: 2026-10-24. Seat: `kotoba-r64.MutW2ReceiptSubs-2`. Lane repo: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Attacked artifact: `verifiers/check_r64_routed_repairs.py` at the round's measured tip
`c019919c97ab5fe98e87a7754b4449ea4e699c99` (base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`).
Method: scratch clone `/tmp/r64subs` at `c019919c`, one single-sided mutation committed per probe,
counter re-run at the **mutated commit** (all checks read committed bytes via `git show`, so worktree
state cannot mask a mutation). Byte hashes before/after and a restore-to-tip diff are recorded.

Tooling installed/upgraded: none (python3 + git already present; no pacman transaction, no network).

## Baseline (pristine, before any mutation)

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0

$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
EXIT=1

$ python3 -B verifiers/check_r64_routed_repairs.py --self-test
… (process arms) …
self-test: 0 failure(s) over 32 assertions
EXIT=0
```

Pristine file hashes: `LOG.md` = `5aec2cf5788949f265e4168567f46c8dc7affd5cdb46cc4eaba6a3a04880ca3d`;
`ExecW2E2Patch.md` = `a6b196788c1edf9214225032b3dbc6ccbd08ce44d5fcb0cc85e449d4d64fa0a7`;
`MutW2SplitClauses.md` = `e51509ff37b32948005151496a615db3159326056b903b64dc44aaff4336ba3c`.

## Verdict table

| # | Mutation (single-sided, committed) | Mutated rev | Detector output | Verdict |
|---|---|---|---|---|
| 1 | Counted citation line: the two committing revs **swapped** (wrong attribution) | `83b88244` | `4 of 4`, exit 0 | **SURVIVED — CRITICAL** |
| 2 | Counted axis line scores **inverted** (`consistency 9 … depth 10`, `consistency is the lowest`) | `8e325b58` | `4 of 4`, exit 0 | **SURVIVED — CRITICAL** |
| 3 | Seat file grown by 100 marker-free junk lines | `8f7e7196` | `4 of 4`, exit 0, `added-lines=182` | SURVIVED — by design (honest-append allowance) |
| 3b | Seat file: real correction **deleted**, replaced by one marker sentence + 100 filler lines | `e2dbd575` | `4 of 4`, exit 0, `added-lines=101` | **SURVIVED — CRITICAL** |
| 4 | Drift note rewritten to name `23` **without** the word `assertions` | `1618cdac` | `3 of 4`, exit 1 | KILLED |
| 5 | Round-63 LOG line rewritten (non-append) with the right tokens, honest counted line left intact | `929e576b` | `4 of 4`, exit 0 | MASKED / inconclusive as specified |
| 5b | Same r63 rewrite, round-64 counted citation line deleted (tokens exist only non-append) | `d418d2fe` | `3 of 4`, exit 1 | KILLED (suffix gate holds) |
| 5c | Append-only world absent: drift note deleted, dated `15 → 21` cell rewritten to `15 → 23` | `df012a9a` | `4 of 4`, exit 0 | **SURVIVED — CRITICAL** |

Every mutation was made in `/tmp/r64subs` only; each run re-computed the pinned base arm at
`078eec4` and none printed the `base arm failed` refusal, i.e. every mutant world still scored the
do-nothing control `0 of 4`.

## 1 — Swapped committing revs (wrong attribution): SURVIVED, 4 of 4

Changed (in the round-64 counted citation line):

```
-  `C1-do-nothing-v31.txt` committed at `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8` and `C2-before-r62tip.txt` committed at `cbbee56e9a3589b0b46736ad36f1b77701def80e`
+  `C1-do-nothing-v31.txt` committed at `cbbee56e9a3589b0b46736ad36f1b77701def80e` and `C2-before-r62tip.txt` committed at `8c4cefa8e1b751d5f93dbcc65349b8e985b102d8`
```

```
$ git commit -am "M1: swap the two committing revs on the counted citation line"
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 83b88244d0b2ac887a35a95f0d940f7f66e015a2
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

`LOG.md` sha256 at mutated rev: `5fb2c1cf8a6ab8190f96add55c3dc39ae4716176c2e9bc9afdca8472066fe38b`.

**Finding (CRITICAL).** Check 2's matcher is presence-only: it requires each computed rev to appear
somewhere on one suffix line, never that the rev is bound to its own basename. The mutant asserts the
inverse of the measured fact — `C1-do-nothing-v31.txt` committed at `cbbee56e` (false; committed at
`8c4cefa8`), `C2-before-r62tip.txt` committed at `8c4cefa8` (false) — i.e. exactly the M95
mis-citation class the check exists to close, now *inside* the counted line, and it certifies at
`4 of 4`. The PASS detail prints the two computed revs (`8c4cefa8 + cbbee56e`) with no pairing, so
the receipt output cannot reveal the inversion either. The self-test's substitution arms cover
one-sided lines, a wrong revision and a repinned base, but not a **swapped pair**.

## 2 — Inverted axis scores: SURVIVED, 4 of 4, and the PASS message asserts the opposite

```
-  The round-63 report names calibration/consistency (10) the lane's lowest owned axis; the axes table owns depth 9 and consistency 10 — depth is the lowest owned axis, and C1's targeting it satisfies the obligation under both readings.
+  The round-63 report names calibration/consistency (9) the lane's lowest owned axis; the axes table owns consistency 9 and depth 10 — consistency is the lowest owned axis, and C2's targeting it satisfies the obligation under both readings.
```

```
$ git commit -am "M2: invert the counted axis line scores (consistency 9 depth 10)"
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 8e325b581ffdedbda2a8be4f694717b472758fc5
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

`LOG.md` sha256 at mutated rev: `40dbf89152c2e25b08de9857c2d482d7fc1884bf862ce7112695474481425db4`.

**Finding (CRITICAL).** `check_lowest_axis` correctly computes depth 9 < consistency 10 from
SCORECARD, then only requires the suffix line to contain `lowest`, `depth`, `consistency`, `9` and
`10` anywhere. The mutant says consistency is the lowest owned axis at 9 and depth at 10 — the
reverted r63 defect verbatim — and the counter prints the PASS detail *"round-64 LOG suffix names
depth 9 < consistency 10 as lowest"* over bytes that say the exact reverse. The check's own claim
is falsified by its own output line. Plan E3.5 names the discipline the implementation does not
implement ("ordered, content-shaped matchers … token scans green-light inverted statements"): the
matcher is still a token scan.

## 3 — +100 marker-free junk lines in the seat file: SURVIVED (by design)

```
$ for i in $(seq 1 100); do printf 'padding line %03d — no marker token here\n' "$i" >> MutW2SplitClauses.md; done
$ git diff --numstat 38defdc HEAD -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
182     29      .ufo/waves/round-63/w2/MutW2SplitClauses.md
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 8f7e7196811dbf7cfb63161512e857a7455b5c57
PASS seat-edit-committed    marker=True added-marker=True added-lines=182 (need >=60)
… r63 routed defects closed 4 of 4
EXIT=0
```

`MutW2SplitClauses.md` sha256 at mutated rev: `5e77a8272cff5f9752623e7aa8489484e7eced8332cc5d00aad9a96492ee779b`.

Calibration: this probe **cannot** be expected to kill, because plan erratum E2.1 explicitly
rejected a full-blob sha pin to keep the check open to honest later appends. The honest edit is still
present (marker count 1, added-lines 182 ≥ 60), so `4 of 4` is the declared design, not a defect.
The assignment's blanket expectation ("must print <4 of 4") is not met here, and should not be.

## 3b — Real correction deleted, marker sentence + filler substituted: SURVIVED, 4 of 4 (CRITICAL)

World built from the **committed `38defdc` copy** (the un-corrected bytes): replace the whole file
with that copy plus one line containing `temporal mismatch` plus 100 filler lines.

```
$ git show 38defdc:.ufo/waves/round-63/w2/MutW2SplitClauses.md > <seat file>
$ printf 'A **temporal mismatch** note substituted for the seat correction.\n' >> <seat file>
$ for i in $(seq 1 100); do printf 'filler %03d\n' "$i" >> <seat file>; done
$ grep -c "was a \*\*temporal mismatch\*\* on my part" <mutated rev>   # the real correction
0
$ git diff --numstat 38defdc HEAD -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
101     0       .ufo/waves/round-63/w2/MutW2SplitClauses.md
$ python3 -B verifiers/check_r64_routed_repairs.py --rev e2dbd575e72ef57bf8da49ac5cc24b4234312249
PASS seat-edit-committed    marker=True added-marker=True added-lines=101 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

`MutW2SplitClauses.md` sha256 at mutated rev: `70164077c13393036d0e5c2047af5a2f28e229e246153104f14f80bc7d999fd6`.

**Finding (CRITICAL).** Check 1's three conjuncts (marker present, marker line added, ≥60 added
lines) are all satisfiable with the correction absent from the tree: one marker sentence is an
"added marker line", and the 100-line floor is padding-satisfiable. The check therefore does not
pin the routed defect it counts — the seat correction can be *removed* and the counter still
certifies `4 of 4`. Note the trap the plan already identified in E2.1 is real: any blob-hash pin
would freeze honest appends, so the hole needs a content-shaped conjunct (e.g. the correction's own
sentence, or a line-count/ordering relation between the marker region and the removed region), not
a whole-file hash. Reported as a coverage finding only; the contract is not mine to change.

## 4 — Drift note names `23` without `assertions`: KILLED (3 of 4, exit 1)

```
-  …the dated "21 assertions" cells above stand unrewritten): I ran … which printed `self-test: 0 failure(s) over 23 assertions` …
+  …the dated 21-count cells above stand unrewritten): I ran … which printed `self-test: 0 failure(s) over 23 checks` … (no `assertions` token anywhere in the added line)
```

```
$ git commit -am "M4: rewrite drift note to name 23 without the word assertions"
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 1618cdac3c42280170eae6916ecc06b0a5bd63ce
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 3 of 4
EXIT=1
```

`ExecW2E2Patch.md` sha256 at mutated rev: `cdbc3a2047b8ec7ad84e7f24ae0a5d6e8b6454b52cad51c06c147738fdadd52d`.

Check 4's two conjuncts (`23` hash-bounded **and** the word `assertions` on the same added line) are
independently load-bearing; the mutant's runtime tally (23) and static shape still matched, so the
kill is attributable to the receipt-side conjunct alone. Also negative-controlled: `223` cannot
satisfy the token because `_hash_token_re` rejects the leading hex `2` (verified in the pristine run
at base, whose patch file mentions `208`/`15` but no bounded `23`).

## 5 — Non-append rewrite of a round-63 LOG line: masked as specified, KILLED when isolated

As literally specified (rewrite r63 `Defect 2` line to carry both revs, base, both basenames and
`committed`; leave the honest round-64 counted line in place):

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 929e576b77880d997c84018659454eaec80a0585
… r63 routed defects closed 4 of 4
EXIT=0
```

`LOG.md` sha256 at mutated rev: `ae74fd40da14a2b60cc864715abe4ba8e5b762f8f46a338f09f6bb44fc67ad4a`.
This is **not** a surviving substitution: the honest counted line was never removed, so the check
was still reading true bytes. Inconclusive-by-construction, not a kill or a survival.

Isolated (`5b`): the round-64 counted citation line is deleted; the tokens exist only in the
rewritten pre-header r63 line.

```
$ git show <mutated>:LOG.md | awk '/^## 2026-10-24 — Round 64/{f=1;next} f' | grep -c 8c4cefa8
0
$ python3 -B verifiers/check_r64_routed_repairs.py --rev d418d2feb2b2b554fd4877058e513cc50cf1a09d
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 3 of 4
EXIT=1
```

`LOG.md` sha256 at mutated rev: `b8a8cec13539a5f9958d5724f3c73c7944f3109b4efcb059403e1e59e0471286`.

**Killed.** Erratum E1.1's suffix anchoring does what it claims: a non-append rewrite carrying the
correct token set before the round-64 header does not satisfy check 2 (the base `LOG.md:2576`
co-location leak is closed for this substitution). This is the one substitution probe whose kill
is attributable to a hardening the plan declared pre-data.

## 5c — Check 4's "addition vs BASE_REV" does not mean append-only: SURVIVED, 4 of 4 (CRITICAL)

World: restore the patch receipt to its exact `078eec4` bytes (drift note gone), then rewrite the
pre-existing dated line `the assertion count moves 15 → 21` to `15 → 23`. The correct tally text now
exists **only as a replacement of dated bytes**.

```
$ git diff --unified=0 078eec4 <mutated> -- .ufo/waves/round-63/w2/ExecW2E2Patch.md
+++ b/.ufo/waves/round-63/w2/ExecW2E2Patch.md
+no-rewrite invariant; the assertion count moves 15 → 23 and every citation of `15 assertions` must
--- a/.ufo/waves/round-63/w2/ExecW2E2Patch.md
-no-rewrite invariant; the assertion count moves 15 → 21 and every citation of `15 assertions` must
$ python3 -B verifiers/check_r64_routed_repairs.py --rev df012a9a61331d3334e4029510dea819a0248a45
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
EXIT=0
```

`ExecW2E2Patch.md` sha256 at mutated rev: `5dcc621e6e780cc59386b5c958cbc0591eade4bc7d5014600b91d2214276698e`.

**Finding (CRITICAL, against the probe's stated expectation).** `_added_lines()` collects every
`+` line of `git diff --unified=0 BASE_REV <rev>`, and a replacement hunk's new line is a `+` line.
So "be an addition vs `BASE_REV`" is satisfied by rewriting a dated cell; the check cannot
distinguish append from rewrite. Consequence: the E3.6 remedy rationale ("append the drift note
(M95 discipline: never rewrite a dated seat cell)") is **not machine-enforced** for this receipt —
the exact non-append edit the discipline forbids passes at `4 of 4`. The probe's predicted
"append-only world must fail check 4's addition-vs-BASE requirement" is not the observed behavior:
the append-only *absence* (rewrite-only) world is certified.

## Findings (calibration summary)

1. **CRITICAL — check 2 is presence-only (M1).** Rev↔basename attribution is unbound; swapping the
   two committing revs on the counted line prints `4 of 4`. The M95 class survives inside the
   counter's own evidence line, and the PASS detail echoes only the computed values.
2. **CRITICAL — check 3 is presence-only on digits (M2).** Score↔axis attribution is unbound;
   `consistency 9 … depth 10 … consistency is the lowest` prints `4 of 4` with a PASS detail that
   states the opposite of the bytes. Plan E3.5's "ordered, content-shaped matchers" discipline is
   declared but not implemented for this check.
3. **CRITICAL — check 1's floor is padding-satisfiable (M3b).** Deleting the real 82-line seat
   correction and substituting one marker sentence + 100 filler lines prints `4 of 4` with
   `added-lines=101`. M3 (honest +100 junk) surviving is expected by design (E2.1 rejected blob
   pinning); M3b is the substitution that design leaves open.
4. **CRITICAL — check 4's addition test is diff-based, not append-based (M5c).** A rewrite of the
   dated `15 → 21` cell to `15 → 23`, with the drift note deleted, prints `4 of 4`. The no-rewrite
   discipline for this receipt is enforced by etiquette, not by the counter.
5. **Killed, attributable:** check 4's `assertions` conjunct (M4: 3 of 4, exit 1); check 2's
   suffix anchoring against a non-append rewrite (M5b: 3 of 4, exit 1).
6. **Self-test coverage gap (calibration, not a contract change):** `--self-test` (32 assertions,
   exit 0) carries one-sided citation, wrong-rev, repinned-base, reordered-axes and stale-tally arms,
   but no **swapped-pair** arm (revs or axis scores) and no **marker-plus-filler** arm — the four
   surviving substitution classes above are all outside it. [INFERENCE] A swapped-pair arm and a
   pad-without-correction arm would each fail the current implementation, so they are honest
   additions to the suite, not redefinitions of the predicate.

None of this changes the frozen predicate's wording, the verdict, or the claim's disposition in this
seat's gift; it is a coverage record for the L1. Mutant survival here is a finding about the
counter's discriminating power, not a licence to relax or restate C2.

## Restoration evidence

Scratch clone returned to the measured tip after every probe; the final state:

```
$ git reset --hard c019919c97ab5fe98e87a7754b4449ea4e699c99
HEAD=c019919c97ab5fe98e87a7754b4449ea4e699c99
status-lines=0
5aec2cf5788949f265e4168567f46c8dc7affd5cdb46cc4eaba6a3a04880ca3d  LOG.md
a6b196788c1edf9214225032b3dbc6ccbd08ce44d5fcb0cc85e449d4d64fa0a7  .ufo/waves/round-63/w2/ExecW2E2Patch.md
e51509ff37b32948005151496a615db3159326056b903b64dc44aaff4336ba3c  .ufo/waves/round-63/w2/MutW2SplitClauses.md
$ git diff --stat c019919c   → (empty)
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c…   → r63 routed defects closed 4 of 4, EXIT=0
```

All three hashes equal the pristine values recorded before mutation 1. Lane repo
`/home/vgpnk/Projects/shokunin/kotoba-shokunin` untouched by this seat (its pre-existing state at
dispatch — `M .ufo/waves/round-64/receipts/noharm-tip.txt`, `?? .ufo/waves/round-64/w2/` — is
unchanged; no git/jj writes run there). No file outside `/tmp/r64subs` and this report was written.

Report: .ufo/waves/round-64/w2/MutW2ReceiptSubs.md
