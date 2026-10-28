# Kb81S07Quality — proposed `corpus/QUALITY.md` Q76 row (stray-artifact class)

Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Source of the class: routed defect R80-D2 (`corpus/lessons/round-80-verifier-spotcheck.md:66`), mined this
round as `M81-1` per `.ufo/waves/round-81/build/Kb81S01Lesson.md`'s row `| scope (R80-D2 / M81-1) |` (confirmed by
`Kb81S01Lesson` on 2026-10-28; `plans/round-81.md` called the candidate `M80-new`), Frontier step, bridged to C1
repair 3. `M81-2` (base receipt without the counter's own exit status) is a separate measurement row and is not
cited by this criterion.
Receipts: `.ufo/waves/round-81/build/Kb81S07Quality.receipts.txt` (163 lines; W1-W4 run 2026-10-28T02:28:11Z in the
base scratch clone, W5-W8 appended in the same session; units W1-W4 lane/scratch measurements, W5-W5d row shape,
W6 the cited baseline cell, W7 house row widths, W8 the artifact's duplicate identity).
Placement: appended after Q75 (last row, `corpus/QUALITY.md:92`); no existing row edited, no row superseded.

## Proposed row (paste verbatim, one table line)

| Q76 | A seat's probe, debug or command output lands only inside its round's wave directory (`.ufo/waves/round-N/`); a file at the lane root, a swapped or misspelled wave path (`.ufo/wapes`), a stray receipt beside tracked files or a debug dump in a tracked tree is a scope defect even while untracked and read by no gate — it rides `git status`, contradicts the corpus baseline's recorded clean-tree precondition, and an integrator's `git add -A` then tracks it, so a dump under `corpus/` drifts `corpus.index.tracked_files` and reads `unindexed`. Disposition is a move into the wave directory as committed evidence, never a silent delete — extending Q49's sweep-and-disposition to non-report artifacts without superseding it; custody stays Q22. | seat-emitted artifacts (probe output, debug dumps, receipts, scratch files) at write time and their disposition | M81-1 `stray-artifact-outside-wave-dir` (`corpus/lessons/round-81.md` § Mistakes; routed R80-D2 at `corpus/lessons/round-80-verifier-spotcheck.md:66`; `.ufo/wapes` is 594 B of stray probe transcript, sha256 `930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020`, byte-identical (`cmp` rc=0) to the landed wave receipt `.ufo/waves/round-80/build/Kb80C02C2-killproof.txt`, so the disposition move loses no unique bytes). Shown able to fail: `git status --porcelain -- .ufo/wapes` prints `?? .ufo/wapes` at `b2842231` and prints nothing after the move to `.ufo/waves/round-81/dispositions/wapes.txt` (sha256 identical before and after; `.ufo/waves/round-81/build/Kb81S07Quality.receipts.txt` W1/W2/W8). `corpus.index.tracked_files` is the `git ls-files corpus/` count (`verifiers/verify_corpus_integrity.py:6,639,698`; baseline `expect 154`): 155 at `b2842231`, 156 once a `corpus/` dump is staged (receipt W3). | — |

## Cell-level check (5 columns, no unescaped `|` inside a cell) — receipts W5, W5b-W5d

Row appended to a scratch copy of `corpus/QUALITY.md` at `b2842231` (never in the lane), final wording:

```
$ awk -F"|" "/^\\| Q76 /{print NF-2}" corpus/QUALITY.md
5
$ sed -n "/^| Q76 /p" corpus/QUALITY.md | grep -o "|" | wc -l
6
$ git -C "$C" diff --numstat -- corpus/QUALITY.md
1	0	corpus/QUALITY.md
$ sed -n "/^| Q76 /p" corpus/QUALITY.md | grep -c "M81-1"     # lesson label present once
1
$ sed -n "/^| Q76 /p" corpus/QUALITY.md | grep -c "M81-2"     # the measurement row is not cited
0
```

So the row splits into exactly five cells (`id`, `criterion`, `applies to`, `grounded in`,
`supersedes`), closes its last cell with its own pipe, and is a one-line append (`--numstat` `1 0`;
the first W5 append carried a blank separator line, hence its `2 ++`, and no run removed a line —
`grep -c "^-[^-]"` printed `0` with grep rc=1). Row length 224 words; house rows measure Q49 105,
Q22 64, Q75 132 (`sed -n '/^| Q<n> /p' corpus/QUALITY.md | wc -w`, 2026-10-28), so Q76 becomes the
table's longest row — stated for the L1 to weigh, not trimmed after measurement.

House-context measured at `b2842231` (receipt W7): 73 rows split to 5 cells, `Q73` to 6 (`\|` inside two
cells splits under `awk -F'|'`), and `Q75` to 4 — `sed -n '92p' corpus/QUALITY.md | tail -c 60` ends
`... exit 0) | —`, i.e. Q75 has no closing pipe. That is a finding in the seat report, not repaired here:
`corpus/QUALITY.md` is append-only and outside this seat's write scope.

## Able-to-fail receipt (decisive lines excerpted from the receipt file; each block below is one receipt section)

```
## W1 base state: the stray artifact present, untracked
$ git -C "$C" status --porcelain -- .ufo/wapes
?? .ufo/wapes
rc=0

## W2 after the disposition move into the wave dir
$ sha256sum .ufo/wapes    # identity recorded BEFORE the move
930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020  .../clone/.ufo/wapes
rc=0
$ mv .ufo/wapes .ufo/waves/round-81/dispositions/wapes.txt
rc=0
$ test -e .ufo/wapes
rc=1 (1 = absent)
$ git -C "$C" status --porcelain -- .ufo/wapes
rc=0 (no line between the command and this rc = prints nothing)

## W3 the corpus-index mechanism: a dump beside tracked corpus files, before/after staging
$ git -C "$C" ls-files corpus/ | wc -l
155
$ git -C "$C" status --porcelain -- corpus/knowledge/debug-dump.txt
?? corpus/knowledge/debug-dump.txt
$ git -C "$C" ls-files corpus/ | wc -l    # unchanged while the dump stays untracked
155
$ git -C "$C" add -A
rc=0
$ git -C "$C" status --porcelain -- corpus/knowledge/debug-dump.txt
A  corpus/knowledge/debug-dump.txt
$ git -C "$C" ls-files corpus/ | wc -l    # tracked_files observable drifts by 1
156
```

## Non-overlap with Q49 and Q22 (measured against the committed cells)

- `corpus/QUALITY.md:60` (Q49): binds **declared `Report:` paths** to be lane-local, the post-settle misroot
  sweep, and the accounting/disposition of *reports* the sweep finds. Q76 binds a different population —
  probe/debug/command artifacts and where they are written at all — and adds the swapped/misspelled wave
  path (`.ufo/wapes`), which no sweep enumerates because it is not a report and not under a wave round
  directory. Q76 says in-cell that the sweep-and-disposition obligation extends, and names Q49 as not
  superseded; the `supersedes` cell stays `—`.
- `corpus/QUALITY.md:33` (Q22): governs what a hash match proves (custody, historical objects, mtime,
  uninterrupted possession) and that evidence is preserved before targeted cleanup. Q76 restates no
  custody proposition: it requires the disposition to be a move into the wave directory as committed
  evidence and defers identity/custody wording to Q22 by name.
- Not covered elsewhere: `corpus/QUALITY.md:51` Q40 and `:38` Q27 cover the post-settle output window for
  reports, not artifact placement; `:22` Q11 sizes evidence bundles, it does not locate them.

## Limit of this draft

The row states a write-time placement rule and its disposition form; it names no new counter, so its
"shown able to fail" evidence is the `git status` pair plus the `git ls-files corpus/` drift above, not a
gate exit code. The mistake label is settled: the lesson seat landed it as `M81-1` (`| scope (R80-D2 / M81-1) |`),
and the Q76 `grounded in` cell carries that label; `M81-2` is deliberately not cited.
