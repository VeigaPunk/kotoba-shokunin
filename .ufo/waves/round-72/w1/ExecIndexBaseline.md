# ExecIndexBaseline — round 72, wave 1 (build)

**Verdict.** Three drafts, applied and measured in a fleet-shaped sandbox of base
`c69711ee08279609374d895bb0f3c8c18ccf15c9`: both corpus gates go **1 → 0**.

| gate | base | after (all three drafts) |
|---|---|---|
| `python3 -B verifiers/verify_corpus_integrity.py` | exit **1** (4/9, 5 DRIFT) | exit **0** (9/9) |
| `python3 -B verifiers/verify_corpus_independent.py` | exit **1** (2 DRIFT) | exit **0** |

(a) the `corpus/README.md` row for the non-author r71 spot-check, which the lane never edits
(its sha256 is identical before and after); (b) `verifiers/corpus-baseline.json` re-recorded to
the observed `133 / 0 / 93 / 41` plus a one-command tip re-record that refuses to write while a
zero check is dirty; (c) `commit_nonhash 2` is **not** repairable inside the non-author file — the
two tokens are truncated scratch-repo ids that resolve nowhere — so the smallest honest repair is
instrument-side: a named `commit_truncated` context class, **34 added / 5 removed lines** across
the two corpus instruments, pinned red-before/red-after in both self-tests and in seven control
worlds plus the round-12 fault harness.

Nothing committed was touched. Deliverables:
`.ufo/waves/round-72/w1/build/ExecIndexBaseline/{index-row.diff,corpus-baseline.diff,truncated-id-instrument.diff,rerecord-at-tip.sh,gates.txt,fault-harness.txt,controls.py}`.
All three diffs pass `git apply --check` against the live lane tip `e61fd29` (scratch
`git clone --shared` of the lane, checked in `/tmp`, no lane write).

---

## 0. Base re-measured (not accepted from the plan)

Sandbox: `P=$(mktemp -d /tmp/k72fleet-ExecIndexBaseline.XXXX)`; every entry of
`/home/vgpnk/Projects/shokunin` except `kotoba-shokunin` symlinked in;
`git clone --shared` of the lane then `git reset --hard c69711e`. The gate's `../` fleet-root
reads resolve. From `$P/kotoba-shokunin`:

```
$ python3 -B verifiers/verify_corpus_integrity.py
corpus.index    tracked=133 unindexed=1 stale=0 missing=0  (150 FILE-column patterns over 132 md files)
corpus.pointers report_dead=0/93 commit_total=41 unresolvable=0 nonhash=2 (...)
           unindexed: corpus/lessons/round-71-verifier-spotcheck.md
           commit_nonhash: corpus/lessons/round-71-verifier-spotcheck.md:120: fb6a28ee…
           commit_nonhash: corpus/lessons/round-71-verifier-spotcheck.md:90: 955ffd5d…
DRIFT   corpus.index.tracked_files: observed=133 expected=132
DRIFT   corpus.index.unindexed: observed=1 expected=0 / empty
DRIFT   corpus.pointers.report_total: observed=93 expected=91
DRIFT   corpus.pointers.commit_total: observed=41 expected=40
DRIFT   corpus.pointers.commit_nonhash: observed=2 expected=0 / empty
4/9 checks pass
exit=1
$ python3 -B verifiers/verify_corpus_independent.py
index   tracked_files=133 index_tokens=150 (outside coverage map=18) unindexed=1 ...
commits candidates=49 citations=43 hex=41 quoted=6 nonhash=2 unresolvable=0
exit 1
```

Byte-for-byte the round-start receipt
`.ufo/waves/round-72/receipts/base-outputs/verify_corpus_integrity.out` (I re-ran it rather than
trust it). `git show --stat c69711e` → one file added, `corpus/lessons/round-71-verifier-spotcheck.md`,
185 insertions: the closure landed the file without an index row, which is the whole `unindexed`
cause.

## 1. Cause of `commit_nonhash 2` — file:line, and why the file is the wrong repair site

```
$ sed -n '90p;120p' corpus/lessons/round-71-verifier-spotcheck.md
  committed bundle, the scratch junk commit `955ffd5d…`, the frozen command, and
  `receipts/c2-junk-world.txt` (W12 bundle, scratch junk commit `fb6a28ee…`, `0 of 10`,
```

Both full lines, nothing dropped (each is one physical line; the second is the whole line). The
backticked tokens are `955ffd5d…` and `fb6a28ee…` — 8 hex chars each, closed by U+2026
(`E2 80 A6`, confirmed with `cat -A` as `M-bM-^@M-&`). `COMMIT_RE` (`verifiers/verify_corpus_integrity.py:149`,
base numbering) captures the whole backticked token, `is_hex_object_id` (`:303`) rejects it on the
ellipsis, and the token lands in `commit_nonhash`.

Neither prefix is an object anywhere the gate looks:

```
$ git cat-file -e 955ffd5d^{commit}                                → fatal: Not a valid object name
$ git -C /home/vgpnk/Projects/shokunin cat-file -e 955ffd5d^{commit} → fatal: Not a valid object name
$ git cat-file -e fb6a28ee^{commit}                                → fatal: Not a valid object name
$ git -C /home/vgpnk/Projects/shokunin cat-file -e fb6a28ee^{commit} → fatal: Not a valid object name
```

So the only in-file repair — dropping the ellipsis — would move the red, not clear it:
`commit `955ffd5d`` is 8 hex, becomes a *citation*, and fails `git cat-file -e` → `commit_unresolvable 2`.
The file is also out of bounds three ways: the round contract forbids editing non-author files; the
plan's C3 guard requires `corpus/lessons/*-verifier-spotcheck.md` byte-identical to the base; and
this seat does not edit committed lane files at all. Its sha256 is
`0e64aa1536b5bb38992ca362e877918f1d13245812eafa8d3d49d740fc8decd1` at base `c69711e` and in the
live tree — unchanged by this work.

## 2. (a) `corpus/README.md` index row — `index-row.diff`

One row, same shape as the neighbouring `*-verifier-spotcheck.md` rows (Title | File | Basis), placed
after the r71 lessons row, i.e. the last row of the coverage map:

```diff
@@ -135,6 +135,7 @@
 | Round-70 lessons | `lessons/round-70.md` | ...
 | Round-70 verifier spot-check (closure) | `lessons/round-70-verifier-spotcheck.md` | ...
 | Round-71 lessons | `lessons/round-71.md` | ...
+| Round-71 verifier spot-check (closure) | `lessons/round-71-verifier-spotcheck.md` | written by the hyaku closure, not the lane (outside review; never edited here): round 71's per-claim re-checks of the two successor counters (both `10 of 10` at `bf98d28` with both bases red), the junk-world receipts that predate the real-data receipts, closure-derived trend verdicts, and seven routed defects for round 72; landed at `c69711e` without an index row (which turned `verify_corpus_integrity.py` red at that base: `unindexed 1`), indexed round 72 |
 
 ## Frontier
```

Every clause in the Basis cell is re-derived by me from the file (headings at lines 25, 51, 68, 127,
154, 169; `both 10 of 10` at lines 89 and 119; the seven numbered items at 169-185) and from
`git show --stat c69711e`. The cell carries no `.ufo/reports/…` pointer and no `commit `<token>``
form, so it moves neither `report_total` nor `commit_total`. Measured effect of the row alone
(`--no-baseline --json`): `unindexed 1 → 0`, `index_tokens 150 → 151`, `tracked_files` stays 133,
`commit_nonhash` stays 2.

## 3. (b) `verifiers/corpus-baseline.json` — `corpus-baseline.diff`

Recorded only after the row was in the sandbox tree, from

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
tracked_files 133, unindexed 0, stale_patterns 0, missing_paths 0,
report_total 93, report_dead 0, commit_total 41, commit_unresolvable 0, commit_nonhash 2
```

Three `equal` cells re-recorded (`132 → 133`, `91 → 93`, `40 → 41`); all six `zero` cells stay `0`
and are *not* relaxed. `measured_against` re-pointed to `c69711e` with the round-72 build-tree
status, and a `round72_index_rerecord` note added. `report_total`/`commit_total` are the r71
spot-check's own citations, not a fitted denominator.

**Cells that must be re-recorded again at the closing tip.** The round-72 lesson
(`corpus/lessons/round-72.md`) and the C1 entry (`corpus/knowledge/resident-index-and-rungs-round72.md`)
are not tracked yet, and each will also add citations:

- `corpus.index.tracked_files` — `133 → 133 + (new corpus files)`; minimum `135` for those two.
- `corpus.pointers.report_total` — `93 → 93 + (fleet-report pointers the new files carry)`; the r71
  lesson carried two, so expect `+2 … +4`.
- `corpus.pointers.commit_total` — `41 → 41 + (resolvable `commit `<hex>`` citations in the new files)`.
- every `zero` cell must still read `0`; `unindexed` stays `0` **only** if each new corpus file gets
  its coverage-map row in the same landing.

One command, run from the lane root after the last content commit (never typed by hand):

```
$ bash .ufo/waves/round-72/w1/build/ExecIndexBaseline/rerecord-at-tip.sh <rev>
corpus-baseline.json -> 133 / 93 / 41 (tracked_files / report_total / commit_total)
9/9 checks pass
exit 0
```

It reads the three cells back from `--no-baseline --json`, **refuses** to write while any zero
check is non-zero, rewrites `measured_against` and appends a `round72_tip_rerecord` note, then runs
both gates. Both behaviours were exercised: happy path exit 0 and `133 / 93 / 41`; with a planted
`commit `round-99`` corpus file staged, it stopped with
`refusing to re-record: zero-mode checks are not zero: {'unindexed': 1, 'commit_nonhash': 1}` and
wrote nothing. Its metadata rewrite is 4 added / 3 removed lines, confined to `measured_against` and
`notes` (tested by re-running it on the sandbox tree, then `git checkout`).

## 4. (c) `commit_nonhash` stays a `zero` check that can fail — `truncated-id-instrument.diff`

The class is named, counted and documented in both instruments rather than excused silently:

```diff
+# verifiers/verify_corpus_integrity.py (docstring EXCLUDED block, beside the quoted-meta-finding idiom)
+  * truncated commit ids (`commit `955ffd5d…``) — a 7-40 hex prefix closed by a
+    single U+2026 ellipsis is a rendering, not a promise: `commit_truncated_detail`.
+TRUNCATED_COMMIT_RE = re.compile(r"\A[0-9a-fA-F]{7,40}\u2026\Z")
+            if TRUNCATED_COMMIT_RE.match(token):
+                truncated.append(f"{rel}:{line_no}: {token}")
+                continue
+        "commit_truncated": len(truncated),
+        "commit_truncated_detail": sorted(truncated),
```

`verifiers/verify_corpus_independent.py` gets the same rule under its own regex
(`TRUNCATED_RE`), its own branch, `commit_truncated`/`commit_truncated_detail`, and a
`commit_candidates` that still counts the token as a *candidate*. Both are wired into their text
renderers (`commit_truncated:` lines print the two sites) and their self-tests.

**Budget (C3 guard: ≤40 added lines across the six instrument scripts).** Measured:
`git diff --stat c69711e ee2adf4 -- verifiers/verify_corpus_integrity.py verifiers/verify_corpus_independent.py`
→ `2 files changed, 34 insertions(+), 5 deletions(-)`, i.e. 34 added, 39 changed lines total —
6 added lines of headroom for the registry row(s) `check_gate_registry.py` still needs. No new
verifier file, so `check_gate_registry.py` sees no new script. Assertion counts rise and the floors
are minimums: integrity `161 → 164`, independent `103 → 105`, `floors-registry.json` untouched.

**Self-tests** (both green, 0 failures):

```
$ python3 -B verifiers/verify_corpus_integrity.py --self-test
self-test: 0 failure(s) over 164 assertions          exit 0
$ python3 -B verifiers/verify_corpus_independent.py --self-test
self-test: 105 assertions, 0 failures                exit 0
```

New arms: `cites/commit-truncated` = 1, `cites/commit-truncated-detail` =
`["corpus/README.md:8: 955ffd5d…"]`, `truncated/short-prefix` false (6 hex + ellipsis),
`commits: hex+ellipsis is context`, `commits: short prefix stays nonhash`; the fleet fixture's
candidate count moved `8 → 9` because the truncated token is a visible candidate.

**Seven control worlds** (`controls.py`, throwaway repo, both instruments, `--repo`):

| world | token | integrity | independent |
|---|---|---|---|
| A the r71 shape | ``commit `955ffd5d…` `` | exit 0, nonhash 0, truncated 1 | exit 0, nonhash 0, truncated 1 |
| B six hex + ellipsis | ``commit `955ffd…` `` | exit 1, nonhash 1 | exit 1, nonhash 1 |
| C bytes after ellipsis | ``commit `955ffd5d…x` `` | exit 1, nonhash 1 | exit 1, nonhash 1 |
| D word + ellipsis | ``commit `round-99…` `` | exit 1, nonhash 1 | exit 1, nonhash 1 |
| E fault harness `plant_b` | ``commit `round-99` `` | exit 1, nonhash 1 | exit 1, nonhash 1 |
| F eight hex, no ellipsis | ``commit `955ffd5d` `` | exit 1, unresolvable 1 | exit 1, unresolvable 1 |
| G quoted truncated id | ``"commit `955ffd5d…`"`` | exit 0, quoted 1 | exit 0, quoted 1 |

F proves the ellipsis is not a blanket hex escape: an untruncated unknown id still fails
`commit_unresolvable`. E is the exact token `verifiers/fault_injection_corpus.sh:191` plants.

**Round-12 fault harness, whole battery, on the patched instrument** (`--repo` = sandbox, 34 s,
one process, world dirs removed):

```
fault-b | integrity   | 1 | corpus.pointers.commit_nonhash | PASS
fault-b | independent | 1 | corpus.pointers.commit_nonhash | INFO(gating)
verdict: ALL PASS
```

The committed base output before the patch, same command, same tree: the same `commit_nonhash: 2`
line and `4/9 checks pass`.

## 5. No-harm on the neighbouring gates I could disturb

| gate | sandbox result | base |
|---|---|---|
| `check_assertion_floors.py` | exit 1 — `PASS corpus_integrity observed=164 floor=161`, `PASS corpus_independent observed=105 floor=103`, `FAIL checklist observed=1862 floor=1862 self_test_failures=1` | same single inherited checklist failure (`receipts/base-outputs/check_assertion_floors.out`) |
| `verify_skill_checklist.py` | exit 0 | exit 0 |
| `check_correction_sweep.py --root .` | exit 0 — `correction sweep: 0 stale block(s)` | exit 0 |
| `check_gate_registry.py --rev` | exit 1 — `conformant 51 of 53`, no new script | exit 1, same two rows |
| `check_r66_routed_repairs.py --rev` | exit 1 — `D2-corpus-integrity-reconciled: FAIL` | exit 1, **identical** at `--rev c69711e` |

The r66 counter's D2 pins the r66-era counts (`EXPECTED_COUNTS` 118/79/37 at
`verifiers/check_r66_routed_repairs.py:41-49`) against a baseline that rounds 69-72 re-record, so it
is red before and after this work — pre-existing, not a round-72 battery item, and not touched.

## 6. Files written

- `.ufo/waves/round-72/w1/ExecIndexBaseline.md` (this report)
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/index-row.diff`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/corpus-baseline.diff`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/truncated-id-instrument.diff`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/rerecord-at-tip.sh`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/gates.txt`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/fault-harness.txt`
- `.ufo/waves/round-72/w1/build/ExecIndexBaseline/controls.py` (absolute scratch paths inside; re-point to reuse)

No committed lane file modified (`git status --porcelain` shows only untracked `.ufo/waves/round-72/`).
No tool installed or upgraded. Scratch `/tmp/k72w1-ExecIndexBaseline.*`, `/tmp/k72fleet-ExecIndexBaseline.*`
removed before return.

## 7. Risks the L1 should weigh

1. **The truncation exemption is a judgement call.** It is the only repair that leaves the non-author
   file byte-identical, and it keeps both red-before controls (short prefix, word, suffix, plain hex).
   The alternative — leaving the gate red — fails C3's `N == 6`. A falsify-wave critic can re-open it
   by planting `commit `deadbeef…`` and arguing the exemption hides a fabricated id; the answer is
   that the exempt form carries no object-id promise at all, and F shows a *non*-truncated unknown id
   still fails.
2. **The 40-line guard reading.** 34 added / 5 removed satisfies "at most 40 added lines" and also
   added+removed ≤ 40; if C3's counter reads it another way, the numbers are in §4 to check against.
3. **The closing re-record is still owed** (§3). If the L1 lands the lesson and the C1 entry without
   running `rerecord-at-tip.sh`, `verify_corpus_integrity.py` goes red on three `equal` cells —
   which is exactly the C3 predicate's failure mode, not a hidden one.
