# Kb81E04Baseline — C1 repairs R3 + R4: the `.ufo/wapes` disposition, the corpus index and the baseline re-record (round 81)

Seat: `Kb81E04Baseline` (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Round base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Plan: `plans/round-81.md` § C1 repairs 3–4
(authoritative; this document is its operational form).

**This document is an ORDERED RECIPE. It is not a patch and must not be applied.** Every number below
is either measured by this seat today (receipts in `.ufo/waves/round-81/build/Kb81E04Baseline/`,
`R01`–`R19`, indexed in § 10) or attributed to the seat that measured it. No claim after-value is
scored here: the L1 measures the after-value.

Relation to the round-80 runbook (`Kb80E15BaselineOrder.md`): **ported** — the dirty-tree
precondition, the exit-code decision tree, the `--carry` tree, "baseline alone in its commit", the
detached-head label, the exit-3 hazard. **Changed** — the group order (the r81 instruments must land
before the baseline), the index rows are owned by `Kb81S08ReadmeRows` (see § 3.2), the measured
tracked-file arithmetic (155 at base, not 154), and the R1 identity finding in § 7, which the r80
runbook has no counterpart for.

---

## 1. Ground truth at `b2842231` (measured today, never piped — each command's own exit captured)

| fact | value | receipt |
|---|---|---|
| `verify_corpus_integrity.py --repo <base> --no-baseline --json` | exit **1**; `tracked_files 155`, `unindexed 1` (`corpus/lessons/round-80-verifier-spotcheck.md`), `stale_patterns 0`, `missing_paths 0`, `report_total 111`, `report_dead 1` (`corpus/lessons/round-77-verifier-spotcheck.md:15: HEAD:.ufo/reports/round-77/kotoba.md`), `commit_total 46`, `commit_unresolvable 2` (`corpus/SOURCES.md:171` and `:172`, both `7bb48f213ac677f943d5c791199ed3dddf302f00`), `commit_nonhash 0`, `commit_truncated 4` | `R01` |
| `verify_corpus_independent.py --repo <base> --json` | exit **1**; same classes, `report_dead **0**` (the known instrument divergence) | `R02` |
| `verifiers/corpus-baseline.json` at base | `tracked_files 154`, `report_total 109`, `commit_total 46`, every zero class `expect 0`; `measured_against.head = 9a16e9d` | lane read |
| lane worktree | **dirty**: 10 untracked entries — `.ufo/wapes`, `plans/round-81.md`, `.ufo/waves/round-81/{build-w1-spec.py,w1-dispatch.json,w1-dispatch-output.json,w1-spec.json,w1.ready,w1.ready.partial,receipts/census-before.txt,receipts/tipbattery-base-dot.txt,w1/swarm-registry.json}` | `git -C <lane> status --porcelain --untracked-files=all` |

Two arithmetic facts the recipe depends on:

* **`tracked_files` is 155 at base, and the baseline says 154.** The +1 is the closure's
  `corpus/lessons/round-80-verifier-spotcheck.md`, landed at `b284223` *after* the baseline was
  recorded at `9a16e9d`. It is already tracked (that is why `tracked_files` counts it) but not yet
  indexed (that is why `unindexed` reads 1). Indexing it does not move `tracked_files`; landing new
  corpus files does.
* **`report_total` is 111 and the baseline says 109.** Both extra pointers are in the closure's
  spot-check; they resolve.

---

## 2. What this seat ships

1. `Kb81E04Baseline.patch` — **self-contained**: the coverage-map row for the round-80 closure
   spot-check **and** `.ufo/waves/round-81/dispositions/wapes.txt`. Applies to a pristine clone of
   the base (`git apply --check` exit 0). Do **not** apply it together with `Kb81S08ReadmeRows.patch`
   (§ 3.2).
2. `Kb81E04Baseline.disposition-only.patch` — the disposition file alone. Applies to a pristine base
   **and** on top of `Kb81S08ReadmeRows.patch` (both `--check` exit 0).
3. `refresh-corpus-baseline.py` — the round-80 script, ported **byte-identical**
   (sha256 `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a`, the same bytes as
   `.ufo/waves/round-79/build/` and `…/round-80/build/`). No fix was needed; § 6 is its re-verified
   behaviour on r81 bytes.
4. This runbook and the receipts `R01`–`R19`.

**Not shipped here** (other seats own them): the two instrument repairs (`Kb81E01Integrity`,
`Kb81E02Independent.patch`), `verifiers/external-commits.json` (`Kb81E03ExtManifest.json` is the
manifest data; it must be committed at `verifiers/external-commits.json`), the erratum-E6 counter
amendment (`Kb81E05Erratum`), the S230 supersede row and S248/S249 rows (`Kb81S05SourcesEdits.patch`,
`Kb81S16CensusLog-SOURCES-rows.patch`), the C2 counter and its registry row, `SKILL.md`/`PROVINCE.md`.

---

## 3. The two repairs, measured

### 3.1 R3 — the `.ufo/wapes` disposition

The stray file is **untracked**, so no commit can move it and no patch can delete it. The disposition
is therefore two steps:

1. its bytes become committed evidence at `.ufo/waves/round-81/dispositions/wapes.txt` — content
   **byte-identical** to the stray (594 B, sha256
   `930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020`, verified with `sha256sum` on
   both paths after the copy). Content is C2 quote-probe output: four `words=N ok=False why='…'`
   lines and a final `exit=0`. Provenance is recorded here, not inside the file, so the digest stays
   the evidence.
2. the L1 deletes the stray from the lane root (`rm .ufo/wapes`). Nothing else removes it; `jj-lane.sh`
   does not block that path.

Measured effect on the corpus gate: **none** (the file is outside `corpus/`), which is why the
disposition can land in its own commit without moving any count.

### 3.2 R4 — the coverage-map row (and the overlap with `Kb81S08ReadmeRows`)

The row this seat's brief asks for is appended after the round-80 allowed-tools row
(`corpus/README.md:159`), in the r77/r78/r79 spot-check row style. Measured effect
(`R03`): `unindexed 1 → 0`, `stale_patterns 0`, `missing_paths 0`; `tracked_files` and `report_total`
**unmoved** by the row itself (the +1 tracked and +2 report pointers are the closure's file, already
observed at base).

**Overlap, measured.** `Kb81S08ReadmeRows.patch` (published in the same wave) carries *three* rows —
the same round-80 spot-check row, plus rows for `lessons/round-81.md` and
`knowledge/allowed-tools-sdk-round81.md` — and the round-81 Frontier note. Its row 1 is worded
differently from mine but covers the same file. Consequences, all `git apply --check`-measured:

| tree state | `Kb81E04Baseline.patch` | `Kb81E04Baseline.disposition-only.patch` |
|---|---|---|
| pristine base | applies (exit 0) | applies (exit 0) |
| after `Kb81S08ReadmeRows.patch` | **fails** (`corpus/README.md:157: patch does not apply`) | applies (exit 0) |

**Decision:** if `Kb81S08ReadmeRows.patch` lands (it indexes all three files and is the superset),
apply the **disposition-only** patch. If it does not, apply the full patch. Never both README hunks —
two rows for one file is index pollution, not coverage.

`Kb81S08ReadmeRows` also measured the other half of the see-saw: its rows **without** the round-81
files read `stale_patterns 2`, `missing_paths 2` (its `stageB` receipt). Rows and their files land in
the same commit.

---

## 4. The ordered recipe

Commit mechanics are the lane's (`scripts/hyaku/jj-lane.sh commit <lane> --as kotoba -m "<msg>" -- <paths>`;
pathspec-limited, fast-forward-only, no amend). Group boundaries are exact.

### G1 — this seat's content (ONE commit)

```
paths: corpus/README.md                                  # only if S08's patch is NOT used
       .ufo/waves/round-81/dispositions/wapes.txt
and:   rm .ufo/wapes                                      # untracked; not part of the commit
```

Gate after G1:

```
python3 -B verifiers/verify_corpus_integrity.py --repo . --no-baseline --json   # unindexed 0, stale 0, missing 0;
                                                                               # report_dead 1, commit_unresolvable 2 → exit 1
```

Exit 1 here is expected: the pointer and commit classes are the instruments' job (G4).

### G2 — the C2 counter file, alone

```
paths: verifiers/check_sdk_allowed_tools.py
```

The registry gate's universe is the **top level** of `verifiers/` (non-recursive, `.py`/`.sh`), so the
counter file grows it by exactly one and needs its row in the next commit. File-before-row reads
`N of M` non-conformant; row-before-file reads `phantom 1`. Both exit 1 — that is the expected
intermediate, and neither may be a measured tip.

### G3 — `SKILL.md`, `PROVINCE.md`, the counter's registry row, the r81 snapshot MANIFEST

```
paths: SKILL.md
       PROVINCE.md
       .ufo/waves/round-81/snapshots/MANIFEST.sha256
```

Merge the registry rows by hand if more than one seat adds one at the same table end (r80 measured
that two patches at the same insertion point fail in both orders and under `--3way`). Check
`wc -l SKILL.md` against the budget box in the same breath.

Gate after G3: `check_gate_registry.py --rev <tip>` conformant with `phantom 0`, exit 0;
`verify_skill_checklist.py` exit 0.

### G4 — the two corpus-gate repairs + `verifiers/external-commits.json` + the E6 counter amendment (ONE commit)

```
paths: verifiers/verify_corpus_integrity.py
       verifiers/verify_corpus_independent.py
       verifiers/external-commits.json
       verifiers/check_tip_battery.py
```

**The pins are a function of these exact bytes.** `check_tip_battery.py`'s `INSTRUMENT_PINS` must name
the blob of each repaired instrument **at the measured rev**; recompute after the last instrument edit
and before the commit (`Kb81E14PinAudit-recompute.py`). Erratum E6's line set is closed: `LINE_CAP`
40→140, one reviewed pin per instrument, self-test constants re-anchored to derive from `LINE_CAP`,
comment mentions updated. The size arithmetic is `22` lines already spent at the base
(`git diff --numstat 072048fa b2842231 -- <six battery scripts>` → `22 3 check_assertion_floors.py`) plus
the two reviewed repairs, against the amended cap.

Gate after G4 (all four, each own exit):

```
python3 -B verifiers/verify_corpus_integrity.py --self-test      # 0 failures
python3 -B verifiers/verify_corpus_independent.py --self-test    # 0 failures
python3 -B verifiers/check_tip_battery.py --self-test            # 0 failures
python3 -B verifiers/verify_corpus_integrity.py --json           # report_dead 0, commit_unresolvable 0 → exit 0
python3 -B verifiers/verify_corpus_independent.py --json         # exit 0
```

**Measured blocker, and it is not this seat's to fix.** The two reviewed repairs as published
(`Kb81E01Integrity.patch` + `Kb81E02Independent.patch`) read, in the guard's own arithmetic
(`git diff --numstat --no-renames 072048fa <rev> -- <six BATTERY scripts>`, summed):
`instruments added 473 / deleted 32 lines (cap 140)` — `instrument-size` fails by **333** added lines
(`R20`; base spend alone is `22/3`, so the repairs are `+451`). Under the plan's own kill rule
("the reviewed instrument patches' combined added lines exceed the declared cap arithmetic … C1 stops
as an honest stop") the claim is alive only if the two instruments shrink to **≤ 118 added lines in
total**. `LINE_CAP` must not be raised after data: E6 froze 140 before any after-value, and raising it
now is the narrowing the kill rule forbids. So: do not read a `6 of 6` in the runbook's group
expectations as an assumption — the battery cannot reach it until that arithmetic closes.

### G5 — the corpus content: the round-81 lesson, the C2 entry, the SOURCES rows (ONE commit)

```
paths: corpus/lessons/round-81.md
       corpus/knowledge/allowed-tools-sdk-round81.md
       corpus/SOURCES.md        # S249, the S230 supersede row, S248 used-by old→new
       corpus/README.md         # if S08's rows are applied here rather than in G1
```

Files without rows → `unindexed`; rows without files → `stale_patterns` + `missing_paths`. Both are
zero-mode classes the refresh refuses on, so they cannot be carried: land the pair.

Gate after G5: both corpus gates exit 0 **with the baseline still at its old expectations**, i.e. the
three `equal` classes read `OBSERVE`/`DRIFT` (the counts moved) and every zero class reads 0. That is
the state G7 records.

### G6 — the wave evidence, and the tree must go clean

```
paths: .ufo/waves/round-81            # build/, w1/, receipts/, snapshots/, dispositions/
and:   rm .ufo/wapes                  # if G1 has not already
```

Gate after G6 — the gate **is** the precondition:

```
git -C <lane> status --porcelain --untracked-files=all     # must print NOTHING
```

### G7 — the baseline: dry-run, then write, then commit the baseline ALONE

From the lane toplevel, clean tree (the plan's literal form):

```
python3 -B .ufo/waves/round-81/build/refresh-corpus-baseline.py --repo . --dry-run
python3 -B .ufo/waves/round-81/build/refresh-corpus-baseline.py --repo .
jj-lane.sh commit <lane> --as kotoba -m "r81: refresh the corpus baseline at the C1/C2 tip" -- verifiers/corpus-baseline.json
```

`--dry-run` is not optional in practice: it prints the three `equal` lines and writes nothing
(`R13`, `R19`), so a surprise in `tracked_files` is caught before the exit-3 hazard (§ 6). **No
`--carry`** at the final tip. Do not amend the content commit afterwards: the baseline records
`measured_against.head`, which an amend moves out from under.

Gate after G7: both corpus gates exit 0 (9/9 and all-PASS), `verifiers/corpus-baseline.json` changed
alone in its commit.

### G8 — the final battery and the report

Both tip-battery forms (`--repo .` from the lane root and the absolute `--repo <lane>`), the rest of
the plan's no-harm battery, then the report. `corpus-baseline.json` is **not** pinned by any battery
guard (checked: `check_tip_battery.py` pins the six `BATTERY` instruments and the spot-check files
only), so G7 cannot break `instrument-pin`; any later corpus edit *does* invalidate the recorded
counts — re-refresh instead of editing after G7.

---

## 5. The expected post-integration baseline diff (measured, then arithmetic)

**Measured anchor — the real post-integration shape** (`R15`–`R18`): base + `Kb81S08ReadmeRows.patch`
+ `Kb81E04Baseline.disposition-only.patch` + the round-81 drafts (`build/allowed-tools-sdk-round81.md`
→ `corpus/knowledge/allowed-tools-sdk-round81.md`, `build/Kb81S01Lesson.md` →
`corpus/lessons/round-81.md`) + the two measurement-aid instruments, clean tree at `8af6525`:

```
corpus.index.tracked_files         154 -> 157
corpus.pointers.report_total       109 -> 111
(commit_total 46 unchanged)
wrote …/corpus-baseline.json (head 8af6525 …)
post-refresh: 9/9 checks pass, exit 0
independent: exit 0; exit 0
```

Baseline `checks` diff on that tree — exactly two expectations move, every zero class stays
`expect: 0`:

```
corpus.index.tracked_files      expect 154 -> 157
corpus.pointers.report_total    expect 109 -> 111
corpus.pointers.commit_total    expect 46 (unchanged)
corpus.index.unindexed / stale_patterns / missing_paths            expect 0
corpus.pointers.report_dead / commit_unresolvable / commit_nonhash expect 0
```

`measured_against.head` / `head_subject` / `note` and one new `notes.round81_rerecord` key change as
the script always changes them; the old `notes.round80_partial` is preserved verbatim (append-only).

**Arithmetic for the L1, so a different final content set is not a surprise:**

```
tracked_files = 155 (base observation, the closure's spot-check included)
              + (each NEW file under corpus/ that is committed, indexed or not)
report_total  = 111 (base observation)
              + (each report-pointer token the new corpus bytes carry)
commit_total  = 46 (base observation)
              + (each new resolvable backticked `commit `<hex>`` token; the two S230/S231 tokens are
                 already counted and classify `commit_external`, not unresolvable)
```

So: two new corpus files and no new report pointer ⇒ **157 / 111 / 46**, which is what the drafts
measure. If the final lesson cites the round-81 report path, `report_total` reads 112 — the script
observes, and the L1 reads it off the `--dry-run` line instead of predicting it.

**Without the instrument repairs the re-record must NOT land** (`R04`, on the tree that holds only
G1's repairs): the script refuses, exit 2, `verifiers/corpus-baseline.json` untouched —

```
gate disagreement (not recorded, expectation stays 0): corpus.pointers.report_dead integrity 1 vs independent 0
refresh-corpus-baseline: refused: zero-mode corpus.pointers.report_dead observed 1, not 0; …
```

That is the plan's W1 world in its true form: index and baseline repairs alone cannot turn the corpus
gates green, which is what makes R1+R2 load-bearing.

---

## 6. The refresh script — exit 0 / 2 / 3, re-verified on r81 bytes

| exit | class | measured words | what the L1 does |
|---|---|---|---|
| **0** | written (or dry-run) | `tracked_files 154 -> 157` … `wrote <path> (head <sha>)`, `post-refresh: 9/9 checks pass, exit 0`, `independent: exit 0; exit 0` | commit the baseline alone (G7) |
| **2** | **refused, baseline untouched** | `dirty tree: … commit or clean these paths first` · `zero-mode <class> observed N, not 0` · `--carry corpus.index.*: an index class is never carried` · `the two gates disagree on <hard class>` · `unexpected tree, missing <file>` · `not a git work tree` / `is not the work-tree toplevel` · `<gate> --self-test exited N` · `a gate exited 2/3` · `baseline is a symlink` / `has no checks object` | fix the named cause, re-run. The script stops at the first nonzero zero-mode class, so a fix advances the refusal to the next one |
| **3** | **internal / post-condition — the baseline HAS already been written** | `post-refresh: … did not emit JSON` · `drift this script does not own: <ids>` · independent exited something other than 0/1 | do **not** commit the file as-is: inspect it, restore it (`git checkout -- verifiers/corpus-baseline.json`), fix the cause, re-run |

Preconditions, all fail-closed and all measured: the tree must be **clean including untracked files**
(a staged file refuses too — the status check is `--untracked-files=all`); the integrity gate's
`--self-test` must pass; both gates must run and agree on every **hard** class
(`tracked_files`, `unindexed`, `stale_patterns`, `missing_paths`, `report_total`, `commit_total`).
On the **soft** zero-mode classes a divergence is printed and stamped into the note, never recorded —
today's is `report_dead` integrity 1 vs independent 0 at base (`R01`/`R02`).

`--carry` decision tree (unchanged from r80, re-read): a `corpus.index.*` id can **never** be carried;
at the final tip nothing is carried (a carried class stays a DRIFT inside the tip battery, so the
battery can never reach `6 of 6`); at an intermediate tip a residual that another seat provably owns
may be carried to unblock a downstream step, and that baseline must be re-recorded at the final tip
anyway because it names the wrong `head`.

`--repo .` and `--repo <abs>` are equivalent: both resolve to the work-tree toplevel
(`open_tree` refuses a subdirectory). Measured `--repo .` from a tree root: `R19`.

---

## 7. Findings for the instrument seats (measured, load-bearing for the kill rule)

### 7.1 Report content identity cannot bind every path target — and must not bind only object targets

Two measurements, both on the r81 corpus:

* **Identity on every resolved target** (the plan's sentence read literally): `report_dead **11**` at
  base — 11 citations of 5 distinct pre-convention reports (rounds 1, 4, 5, 8, 14), listed in `R10`.
  Five of those are the honest record of what those rounds produced; round 8's report *is* a 120 B
  respawn marker and the corpus cites it as one. Identity-for-all therefore makes C1 unreachable.
* **Identity on object-resolved targets only** (the shape the round-81 lesson draft states and the
  shape `Kb81E01Integrity`'s receipts measure, `report_dead 0/111` at base): a marker substituted at a
  post-convention report **path** reads `report_dead **0**` — the round-80 W10 world substituted at
  `.ufo/reports/round-76/kotoba.md`, which the corpus cites by path, so W10 would reach its target and
  the plan's kill rule would fire (`R14`).

**The rule that satisfies both, measured green:** object targets always bind identity; path targets
bind it at round ≥ **19**, the measured convention boundary — `## SHONEN` is uniform from round 19 on
(rounds 19–80 all carry the heading and are ≥ 3166 B), while rounds 1–17 are mixed (`R11`). Under it:
`report_dead 0/111`, `commit_unresolvable 0`, `commit_external 2`, and the W10 marker still reads
dead (`R09`). The floor is a dated convention boundary, declared once, not a fitted denominator.

**Cross-seat status (read, not scored).** `Kb81E01Integrity` adopted this boundary after receiving
`R14` and reports reproducing the 11 sites independently before adopting it — same five reports
(rounds 1/4/5/8/14), same count. Its published instrument applies the rule at **every** path route
(explicit absolute, relative, tilde and the bare fleet fallback), with the pre-convention rounds
exempt, and `<rev>:<path>` objects always bind; its self-test pins the exemption with a round-5,
7-byte body that must stay green. That is the same semantics applied more widely than the arm above,
and it makes the W10 marker die under any citation form.

### 7.2 The R1 repair must re-anchor its own fixture

`verify_corpus_integrity.py`'s self-test `pointer/fleet-root/resolves-existing-report` writes
`"report\n"` at a round-53 fleet path and asserts `report_dead 0` — it encodes the existence rule the
repair exists to replace. With the identity arm on, that assertion fails (`R12`, the pre-anchor run).
Re-anchoring it to a ≥ 400 B `## SHONEN` body **and** adding the marker arm is what this seat measured:
self-test `164 → 165` assertions, 0 failures.

### 7.3 The external manifest must be read by both gates, with its receipt present

`verifiers/external-commits.json` must carry, per id, the repository and a committed receipt path;
a loader that accepts a row without its receipt (or without `repo`) re-creates the laundering hole.
This seat's measurement aid requires `repo` **and** `receipt` present in the tree before an id counts
as external, and checks nothing about the receipt's content — the shipped R2 should also verify the
association the receipt records (`git ls-remote` output naming the hash for that repository), because
the manifest is the new trust root. `Kb81E03ExtManifest.json` is the data (one id:
`7bb48f21…` → `mistralai/mistral-vibe`, evidence
`.ufo/waves/round-79/snapshots/S231.fetch.json`); it needs committing at the manifest path.

### 7.4 What this seat could not verify

`Kb81E01Integrity`'s instrument patch was not published under `build/` when the aid measurements were
taken (only its receipts were), and `Kb81E02Independent.patch` was published after the aid was built.
The aid instruments used here are **this seat's own derivation** (`Kb81E04Baseline` scratch only,
never a lane edit, never a shipped patch); the equal-class counts they produce are the gate's own
definitions (`git ls-files corpus/` row count, token counts) and do not depend on either repair, but
the zero-class readings in `R15`/`R16` are the aid's, not the reviewed instruments'.

### 7.5 The binding constraint on C1 is now line arithmetic, not classification

Measured on the two published repairs (`Kb81E01Integrity.patch` + `Kb81E02Independent.patch`) with the
guard's own computation — `git diff --numstat --no-renames 072048fa <rev> -- <six BATTERY scripts>`,
summed, exactly as `check_tip_battery.py:298-320` does it (`R20`):

```
22   3   verifiers/check_assertion_floors.py      (base spend, 072048fa..b2842231)
247 18   verifiers/verify_corpus_independent.py   (Kb81E02Independent.patch)
204 11   verifiers/verify_corpus_integrity.py     (Kb81E01Integrity.patch)
--- instruments added 473 / deleted 32 lines (cap 140) -> instrument-size FAILS by 333
```

Both repairs are well-designed and both are too large for the cap E6 froze before data. The plan's
kill rule fires on exactly this arithmetic unless the instruments shrink to **≤ 118 added lines in
total** (140 − the 22 already spent). Consequences the L1 must hold:

* **Do not raise `LINE_CAP`.** E6 declared 140 before any after-value; moving it now is the
  post-data narrowing the plan forbids. A raised cap would also make the W4 control world
  (stubbed instrument) easier to launder, which is the load `instrument-size` exists to carry.
* **Do not drop the identity arm to buy lines.** `R14` shows that removing path identity is what
  makes W10 reach its target; shrinking must come out of structure (helpers, comments, shared
  constant tables), not out of classification.
* **A red `instrument-size` is not a corpus-baseline problem.** The refresh script reads only the two
  corpus gates and the baseline; it will happily record a baseline on a tree whose battery still reads
  `5 of 6`. That is precisely why the after-value is measured at the tip and not inferred from a
  green refresh: G7 succeeding says nothing about `instrument-size`.

---

## 8. Traps (ported from r80 where re-verified, new ones marked)

1. **Dirty tree refuses the refresh — untracked files included.** Re-verified today (`R04` was reached
   only after the tree was committed clean). The lane carried 10 untracked entries when this seat
   measured it (§ 1) and the wave's own artifacts grow that list, so G6 is a hard prerequisite, not a
   formality.
2. **`.ufo/wapes` is untracked** — only `rm` removes it; the disposition file is the committed
   evidence, and its digest is the proof of identity (§ 3.1).
3. **NEW — rows and files are a see-saw.** `unindexed` (files without rows) and
   `stale_patterns`+`missing_paths` (rows without files) are both zero-mode and neither is carriable;
   land them together (§ 3.2, `R03`).
4. **NEW — the index rows have two owners this round.** Apply one README hunk, never both (§ 3.2).
5. **A measured tip in a scratch clone records a detached head** —
   `head: "<sha> (detached measurement commit; resolvable in the measuring clone only…)"`. Prefer the
   lane-local G6+G7; the label is a worse record.
6. **Baseline alone in its commit, no amend** — the recorded `head` depends on the content commit
   staying put.
7. **Exit 3 means the file is already on disk** — restore before re-running (§ 6).
8. **Never `--carry` at the final tip**, and never carry a `corpus.index.*` id at all.
9. **`corpus-baseline.json` is not pinned by the battery** (checked), but **any corpus edit after G7
   invalidates the counts** — re-refresh instead.
10. **Do not name the round-76 report symlink's own path to `jj-lane.sh`** (r80 measured the
    `realpath` escape); name the parent directory. Unrelated to this seat's files, but it is the same
    integration pass.

---

## 9. Ordering summary (one line each)

```
G1 disposition + index row      → corpus gates red on pointers only
G2 C2 counter file alone        → registry non-conformant (expected)
G3 SKILL/PROVINCE/row/MANIFEST  → registry 0 phantom, checklist exit 0
G4 instruments + manifest + E6  → both corpus gates exit 0; battery 6 of 6 ONLY if the size
                                  arithmetic closes (measured 473 > 140, § 7.5) — else honest stop
G5 corpus content + SOURCES     → corpus gates exit 0, three equal classes moved
G6 wave evidence; tree clean    → git status empty
G7 refresh (dry-run, write)     → baseline alone, 9/9 + independent 0
G8 battery both forms, report    → claim after-value measured by the L1
```

---

## 10. Evidence index (`.ufo/waves/round-81/build/Kb81E04Baseline/`)

| file | what it proves |
|---|---|
| `R01` / `R02` | the base observation of both corpus gates (`155 / 1 / 111 / 1 / 46 / 2`; the independent's `report_dead 0` divergence) |
| `R03` | after the index row alone: `unindexed 0`, `stale 0`, `missing 0`, pointers still red, `tracked_files`/`report_total` unmoved |
| `R04` | the refresh **refuses** (exit 2) on the index+disposition tree: `report_dead 1` — the re-record must not land without R1/R2 |
| `R05` / `R06` | the aid-instrument tree: `report_dead 0`, `commit_unresolvable 0`, `commit_external 2`; independent exit 0 |
| `R07` | the refresh **writes** on that tree: `154 -> 155`, `109 -> 111`, `9/9`, independent exit 0 |
| `R08` | the full baseline diff on that tree (two `expect` lines, the `measured_against` block, the appended note) |
| `R09` | the W10-class control: marker at a post-convention report path is `report_dead 1`; the real report is 0; the object arm kills a marker blob regardless of round |
| `R10` | identity-for-all costs 11 dead citations (listed), floor 19 costs 0 |
| `R11` | the `## SHONEN` convention sweep over the fleet's round-1…80 reports (the floor's evidence) |
| `R12` | self-tests: the fixture that encodes the old rule fails before re-anchoring; `165 assertions, 0 failures` after |
| `R13` / `R19` | `--dry-run` writes nothing and prints the three equal lines; the plan's `--repo .` form works |
| `R14` | the object-only identity gap: W10 world reads `report_dead 0` with path identity off, `1` at the floor |
| `R15` / `R16` | the post-integration shape (`157 / 0 / 0 / 0 / 111 / 0 / 46 / 0 / 2`) on both gates |
| `R17` / `R18` | the post-integration refresh (`154 -> 157`, `109 -> 111`, `9/9`, independent exit 0) and its `expect`-only diff |
| `R20` | the guard's own line arithmetic on the two published repairs: `added 473 / deleted 32` against `LINE_CAP 140` — `instrument-size` fails by 333 |
| `MANIFEST.sha256` | sha256 of every receipt above |

Scratch (`/fast/scratch/hyaku/kotoba-r81/Kb81E04Baseline/`) was removed before this seat yielded;
the receipts were copied out first. Nothing in the lane tree, the lane git/jj state, the fleet root
or a sibling lane was mutated by this seat: every git mutation happened inside its own clones under
`/fast/scratch`, each asserting `rev-parse --show-toplevel` first.

## 11. Tooling record

Nothing was installed, upgraded or run through a package manager. `pacman` was not invoked (host
pause respected). No network fetch by this seat. Python 3 (system) and git were already present.
