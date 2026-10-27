# R76-D4 baseline + indexing notes — what the L1 must do, and in which order (kotoba, round 77 w1)

Owner: seat `E10GateRepair`. Deliverable 3 of 3 (deliverable 1 = `E10GateRepair.readme-index-rows.patch`,
deliverable 2 = `E10GateRepair.refresh_baseline.sh`). Everything below is measured on scratch
clones of lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`; receipts are named inline and live in
`.ufo/waves/round-77/receipts/`.

## 1. What the two gates actually read

| class | source | mode |
|---|---|---|
| `corpus.index.tracked_files` | `git ls-files corpus/` row count | `equal` vs baseline |
| `corpus.index.unindexed` | tracked corpus files (`corpus/README.md` excepted) that no column-2 token of a `## Coverage map` row denotes | `zero` |
| `corpus.index.stale_patterns` | a corpus-internal column-2 token matching no tracked file | `zero` |
| `corpus.index.missing_paths` | a non-glob column-2 token whose corpus-relative path is not on disk | `zero` |
| `corpus.pointers.report_total` / `report_dead` | `.ufo/reports/round-<n>/…md` tokens in **any** tracked corpus markdown, outside quotes | `equal` / `zero` |
| `corpus.pointers.commit_total` / `commit_unresolvable` / `commit_nonhash` | `commit `<hex>`` tokens in any tracked corpus markdown, outside quotes and code spans | `equal` / `zero` |

Consequences that decide the landing order:

1. **Only tracked files exist for the gate.** `git ls-files` is the universe, and file contents are
   read from the worktree. A file created but not `git add`ed is invisible: an "unindexed" file that
   is untracked does **not** count as unindexed, and a row for it reads STALE. The recipe therefore
   refuses to run on a tree with untracked `corpus/` files (measured, receipt §C of
   `E10GateRepair.recipe.txt`).
2. **A row and its file must travel together.** Apply a row for a file that is neither tracked nor on
   disk and the gate gains two zero-mode failures, not zero: `stale_patterns` +1 *and* `missing_paths`
   +1. Measured on the sibling patch `build/SC06ReadmeCorpus.patch` at the base tree:
   `stale_patterns` 0 → 3 and `missing_paths` 0 → 3, with `unindexed` correctly 0
   (`E10GateRepair.sibling-rows-ordering.txt` §1). Once the three files were present and committed,
   both zero classes returned to 0 and the recipe closed the three `equal` ids (§2 of the same
   receipt).
3. **The description cell is prose but not inert.** It is scanned like the rest of the file for
   `.ufo/reports/…` pointers and `commit `<hex>`` citations. Write "landed at `1e03d19`" or
   "`2f675548`", never `commit `2f675548``, or `commit_total` moves and the baseline drifts for a
   reason nobody intended. (The two rows in this seat's patch were written that way and measured at
   `report_total`/`commit_total` unchanged — `E10GateRepair.gates.txt` stage 2.)

## 2. Files this round adds that MUST also be indexed

| file | status | index row |
|---|---|---|
| `corpus/lessons/round-75-verifier-spotcheck.md` | tracked, **unindexed at base** | in this seat's patch; also in SC06's |
| `corpus/lessons/round-76-verifier-spotcheck.md` | tracked, **unindexed at base** | in this seat's patch; also in SC06's |
| `corpus/lessons/round-76.md` (R76-D2) | not yet written | SC06's patch has it; must land **with** the file |
| `corpus/lessons/round-77.md` | not yet written | SC06's patch has it; must land **with** the file |
| `corpus/knowledge/description-craft-round76.md` (C1) | not yet written | SC06's patch has it; must land **with** the file |

Any further corpus file the round lands (a second knowledge entry, a round-77 verifier spot-check,
another lesson) needs its own row in the same commit, or `unindexed` goes red again — the exact class
R76-D4 exists to close. Rows for a glob already covering the file are unnecessary; check with
`python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json` and read `unindexed_detail`.

## 3. How the counts move when those files land

Each new **tracked** corpus markdown file:

- `tracked_files` **+1** (unconditional);
- `report_total` **+n** where n is the number of unquoted `.ufo/reports/round-<n>/…md` tokens the file
  carries (0 if none);
- `commit_total` **+m** where m is the number of unquoted, non-code-span `commit `<hex>`` citations
  that resolve in the lane or the fleet root (0 if none; an unresolvable or non-hex token instead
  raises a zero-mode failure).

Measured demonstration, three scratch files each carrying exactly one host-absolute report pointer and
one resolvable `commit` token, each with an index row (`E10GateRepair.recipe.txt` §F):

```
tracked_files   146 -> 149     (+3, one per file)
report_total    102 -> 105     (+3, one per file)
commit_total     44 ->  47     (+3, one per file)
unindexed 0, stale_patterns 0, missing_paths 0, report_dead 0, commit_unresolvable 0
```

With the three real files still empty, the observed counts were `149 / 0 / 102 / 44`
(`E10GateRepair.sibling-rows-ordering.txt` §2) — i.e. +3 tracked and nothing else. **Do not carry
either number forward as a prediction**: the real files are prose and will move `report_total` and
`commit_total` by whatever they cite. That is why the baseline is computed, not typed.

## 4. The landing order the L1 must follow (baseline LAST)

1. Land the data commit(s) as usual: entry, SKILL.md row, SOURCES row, lessons, R1–R4 repairs, and the
   README index rows **for exactly the files that exist in that commit**. For the two closure
   spot-checks that is this seat's patch; for the three new r77 files it is SC06's rows, in the same
   commit as those files. Do not apply both patches — they collide at the same anchor and
   `git apply --check` exits 1 in either order (`E10GateRepair.patch-conflict.txt`).
2. Clone the lane to scratch (`git clone --shared`), check out the **final** tree, and make sure
   nothing under `corpus/` is untracked there. If the pristine tree is what you want to measure,
   commit it in the clone first; the recipe refuses otherwise.
3. Run `E10GateRepair.refresh_baseline.sh <clone> round77_rerecord`. It re-runs both gates, refuses
   on any red (zero-mode drift, untracked corpus file, non-toplevel path), copies every `equal`
   expectation from the integrity gate's own `--no-baseline --json`, asserts every `zero` expectation
   is 0, prints `old -> new` for each moved id, writes `verifiers/corpus-baseline.json`
   (`json.dump(indent=1)` + trailing newline, i.e. the file's existing shape), then re-runs both gates
   and fails if either is non-zero afterwards.
4. Commit that baseline as its own commit (it is a measurement, not data), then run the no-harm
   battery at that tip and capture each gate's own exit status.
5. If anything lands afterwards that touches `corpus/` (a w2 correction, a spot-check, a new lesson),
   repeat 2–4. The recipe is idempotent — a re-run with no change prints `no expectation moved` and
   exits 0 (`E10GateRepair.recipe.txt` §B) — and it preserves the baseline's `repo` identity
   (`kotoba-shokunin`) instead of recording the scratch directory's name.

## 5. Base -> repaired numbers, for the report and SCORECARD row

Baseline at base: `tracked_files 144`, `report_total 99`, `commit_total 43`. Observed at lane HEAD
`6523aced` with the index rows in place: `146 / 102 / 44` — the +2 tracked files are the two closure
spot-checks themselves, and their citations are the whole of the +3 report pointers and +1 commit
token (per-file measurement: `round-75-verifier-spotcheck.md` +2 reports +1 commit,
`round-76-verifier-spotcheck.md` +1 report, every other corpus file unchanged between `65a5c7a` and
`6523aced`). Re-recorded baseline after the recipe: `146 / 102 / 44`, both gates exit 0, 9 PASS and
`INFO`-only observations (`E10GateRepair.gates.txt` stages 2 and 3).

## 6. Residual risks this seat cannot close

- **The rows are prose.** A later round may edit a description cell and add a pointer or a
  `commit `<hex>`` by accident; only the baseline refresh catches that, and only as a red `equal`
  drift.
- **Two patches, one anchor.** Until the L1 picks one, `build/SC06ReadmeCorpus.patch` and this seat's
  patch both sit in `build/` and cannot both apply.
- **Tracked-set blindness is structural.** A file the integrator forgets to `git add` is invisible to
  both gates, so `unindexed` stays 0 while the file is absent from the corpus's own index. The recipe's
  untracked-corpus guard closes this only for whoever runs the recipe.
