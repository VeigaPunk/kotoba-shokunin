# Kb81S07Quality — Q76 draft: the stray-artifact mistake criterion

Base `b284223105f4d106f7e8f56ed4fd296c643cda0e`; lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Seat item: Q76 draft (mistake criterion) from `plans/round-81.md` (Frontier step: R80-D2 mined as
the candidate the plan called `M80-new`, landed by the lesson as `M81-1`) and C1 repair 3 (`.ufo/wapes`
disposition).
Scope held: this seat wrote no lane file outside `.ufo/waves/round-81/`; it proposes a row and its
evidence, it does not edit `corpus/QUALITY.md`.

## Delivered

1. `.ufo/waves/round-81/build/Kb81S07Quality.md` — the proposed `corpus/QUALITY.md` Q76 row (one line,
   five cells), its placement (append after Q75), the row-shape check, the able-to-fail receipt excerpt,
   the Q49/Q22 non-overlap reading, and the draft's stated limit.
2. `.ufo/waves/round-81/build/Kb81S07Quality.receipts.txt` — 163 lines, sections W1–W8 including
   W5/W5b–W5d (row shape on the pre-label and final wording), W6 (cited baseline cell), W7 (house row
   widths), W8 (the artifact's duplicate identity);
   every line is a literal command and its output with `rc=` captured from the command itself, never a
   pipeline's last element (r80 M80-1).

## The proposed row (as delivered — paste-ready, no existing row touched)

| Q76 | A seat's probe, debug or command output lands only inside its round's wave directory (`.ufo/waves/round-N/`); a file at the lane root, a swapped or misspelled wave path (`.ufo/wapes`), a stray receipt beside tracked files or a debug dump in a tracked tree is a scope defect even while untracked and read by no gate — it rides `git status`, contradicts the corpus baseline's recorded clean-tree precondition, and an integrator's `git add -A` then tracks it, so a dump under `corpus/` drifts `corpus.index.tracked_files` and reads `unindexed`. Disposition is a move into the wave directory as committed evidence, never a silent delete — extending Q49's sweep-and-disposition to non-report artifacts without superseding it; custody stays Q22. | seat-emitted artifacts (probe output, debug dumps, receipts, scratch files) at write time and their disposition | M81-1 `stray-artifact-outside-wave-dir` (`corpus/lessons/round-81.md` § Mistakes; routed R80-D2 at `corpus/lessons/round-80-verifier-spotcheck.md:66`; `.ufo/wapes` is 594 B of stray probe transcript, sha256 `930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020`, byte-identical (`cmp` rc=0) to the landed wave receipt `.ufo/waves/round-80/build/Kb80C02C2-killproof.txt`, so the disposition move loses no unique bytes). Shown able to fail: `git status --porcelain -- .ufo/wapes` prints `?? .ufo/wapes` at `b2842231` and prints nothing after the move to `.ufo/waves/round-81/dispositions/wapes.txt` (sha256 identical before and after; `.ufo/waves/round-81/build/Kb81S07Quality.receipts.txt` W1/W2/W8). `corpus.index.tracked_files` is the `git ls-files corpus/` count (`verifiers/verify_corpus_integrity.py:6,639,698`; baseline `expect 154`): 155 at `b2842231`, 156 once a `corpus/` dump is staged (receipt W3). | — |

## Shown able to fail — commands, outputs, exit codes

Scratch clone at the base rev (`/fast/scratch/hyaku/kotoba-r81/Kb81S07Quality/clone`, toplevel asserted
`= clone`, `user.name scratch-r81`). Base carries no untracked files, so the 594-byte artifact was
recreated from the lane worktree before the demo (`cp <lane>/.ufo/wapes .ufo/wapes`).

- **Before** — `git -C "$C" status --porcelain -- .ufo/wapes` → `?? .ufo/wapes`, `rc=0`; unfiltered
  `git -C "$C" status --porcelain` → `?? .ufo/wapes`, `rc=0`. Lane worktree, same base rev,
  unfiltered: `?? .ufo/wapes`, `?? .ufo/waves/round-81/`, `?? plans/round-81.md`, `rc=0`
  (`git rev-parse HEAD` = `b2842231…` immediately above it in the receipt).
- **Move** — `sha256sum .ufo/wapes` → `930e2bd6…` (recorded *before* the move);
  `mv .ufo/wapes .ufo/waves/round-81/dispositions/wapes.txt` `rc=0`; `sha256sum` at the destination →
  the same `930e2bd6…`; `test -e .ufo/wapes` → `rc=1` (absent).
- **After** — `git -C "$C" status --porcelain -- .ufo/wapes` prints **nothing**, `rc=0`; unfiltered
  status then reads `?? .ufo/waves/round-81/` (the wave directory itself, as designed).
- **Row shape** (W5, W5b–W5d) — on a scratch copy of `corpus/QUALITY.md` with the final row appended:
  `awk -F'|' '/^\| Q76 /{print NF-2}'` → `5`; `grep -c '^| Q76 '` → `1`;
  `git diff --numstat` → `1	0	corpus/QUALITY.md`; `grep -o '|' | wc -l` → `6`. Row is a pure append and
  closes its last cell with its own pipe; `grep -c 'M81-1'` on the row prints `1` and `grep -c 'M81-2'`
  prints `0`, so the lesson's measurement row is not cited. Row length 224 words; house rows measure
  Q49 105, Q22 64, Q75 132 (`sed -n '/^| Q<n> /p' corpus/QUALITY.md | wc -w`, 2026-10-28) — Q76 is the
  table's longest row, recorded for the L1 rather than trimmed after measurement.

## Wording checked against Q49 and Q22 (no overlap)

- `corpus/QUALITY.md:60` **Q49** owns *declared `Report:` paths*, the final misroot sweep after the last
  seat settles, and the accounting/disposition of reports the sweep finds. Q76's population is different:
  probe/debug/command artifacts and where they are written at all, including a **swapped or misspelled
  wave path** (`.ufo/wapes`) that no report sweep enumerates. The row says in-cell that it *extends*
  Q49's sweep-and-disposition to non-report artifacts and does not supersede it; `supersedes` stays `—`.
- `corpus/QUALITY.md:33` **Q22** owns what a hash match proves (custody, historical objects, original
  mtime, uninterrupted possession) and evidence preservation before targeted cleanup. Q76 asserts no
  custody proposition: it requires the disposition to be a *move into the wave directory as committed
  evidence, never a silent delete*, and names Q22 for the custody wording instead of restating it.
- Checked for a third overlapping row: `:38` Q27 and `:51` Q40 cover the post-settle output window for
  reports; `:22` Q11 sizes evidence bundles without locating them. None binds artifact placement.

## Findings (recorded, not repaired — outside this seat's write scope)

1. **The brief's corpus-index mechanism is one step too strong, and the row states the measured chain.**
   `corpus.index.tracked_files` is `len(tracked_corpus_files(repo))` where that function is
   `git ls-files corpus/` (`verifiers/verify_corpus_integrity.py:6,615-620,639,698`), and
   `corpus.index.unindexed` only walks `corpus/` paths (`:470-471`). So `.ufo/wapes` — outside `corpus/`
   and untracked — does **not** turn that check red while it sits there: W3 measures
   `git ls-files corpus/ | wc -l` = 155 before and after an untracked `corpus/knowledge/debug-dump.txt`,
   and 156 only after `git add -A`. The base's `tracked_files` red (155 vs baseline `expect 154`) comes
   from the round-80 lesson landed tracked-but-unindexed (`corpus.index.unindexed` DRIFT name in the plan),
   not from the stray artifact. Q76 therefore says: the artifact rides `git status`, contradicts the
   baseline's recorded `clean (git status --porcelain empty at the recorded tip)` precondition (receipt
   W6), and an integrator's `git add -A` is what makes a `corpus/` dump drift `tracked_files` and read
   `unindexed`.
2. **A landed QUALITY row is misshapen, which matters for "exact table style".** At base, `Q75`
   (`corpus/QUALITY.md:92`) ends `... exit 0) | —` with **no closing pipe**: `awk -F'|'` reads it as 4
   cells (`sed -n '92p' corpus/QUALITY.md | tail -c 60`, receipt W7). The house distribution is 73 rows at
   5 cells, `Q73` at 6 (its cells contain `\|`, which `awk -F'|'` splits), `Q75` at 4. Q76 is written at
   5 cells with no unescaped pipe. Repairing Q75 would rewrite a landed row in an append-only file, so it
   is reported here and left to the L1.
3. **M-label handoff — settled in-wave.** The plan called the mined mistake `M80-new`; `Kb81S01Lesson`
   landed it as `M81-1` (`| scope (R80-D2 / M81-1) |`, reported to this seat on 2026-10-28), so the Q76
   `grounded in` cell now carries `M81-1 (corpus/lessons/round-81.md § Mistakes; .ufo/wapes stray probe
   transcript)` plus the measured evidence. The lesson's second row, `M81-2` (a base receipt missing the
   counter's own exit status), is deliberately **not** cited: Q76 is the stray-artifact class only.
4. **The artifact's own bytes.** `.ufo/wapes` is 594 B of C2 quote-probe output (`words=11 ok=False
   why='…'` lines from the Q70 probe sweep), sha256 `930e2bd6…`; it is untrusted data, quoted here only
   as a size/hash identity. Its disposition (C1 repair 3) is another seat's move; this seat demonstrated
   the invariant on a scratch copy of those exact bytes and wrote no dispositions file in the lane.

## Not done, and why

- No lane file edited, no commit, no `git add`, no claim after-value scored (claim scoring is forbidden
  to seat seats by the wave spec; control worlds are the only scored ones and Q76 ships none).
- `verify_corpus_integrity.py` was **not** run in the scratch clone: Q63/M116 records that a gate reading
  repo-relative `../` and fleet-root paths read FAIL at every revision when relocated into a `/tmp`
  clone, so its verdicts stay the C1 claim's at the lane. Its check definitions are cited by line
  (`:6`, `:470-471`, `:615-620`, `:639`, `:698`) instead of being re-executed out of place.
- No tool was installed or upgraded (nothing needed); pacman not invoked.

## Scratch

`/fast/scratch/hyaku/kotoba-r81/Kb81S07Quality` removed after the receipts were copied into
`.ufo/waves/round-81/build/`; `TMPDIR` was `$S/tmp` for the whole session. Peers' build outputs were not
needed: this item consumed only lane bytes (`corpus/QUALITY.md`, `verifiers/verify_corpus_integrity.py`,
`verifiers/corpus-baseline.json`, `.ufo/wapes`) and the routed-defect line in
`corpus/lessons/round-80-verifier-spotcheck.md:66`.

Deliverable identity at hand-off (`sha256sum`, 2026-10-28): `Kb81S07Quality.md`
`b661e285f8ea71b5f9ca2cd7163d56cb26d07d6abd444e46ba407a95851b9d49` (101 lines);
`Kb81S07Quality.receipts.txt` `6d735879ebc94d8e583111d704e2fbc6e24fc7e2a12753a4f1c9f93076a8c9d5` (163 lines).
This report's own hash is not recorded: it changes with each edit of this block, so it is self-referential
and would be stale on the next write. Lane HEAD at hand-off stays
`b284223105f4d106f7e8f56ed4fd296c643cda0e`; `git status --porcelain` reads `?? .ufo/wapes`,
`?? .ufo/waves/round-81/`, `?? plans/round-81.md` — unchanged in kind by this seat.

VERDICT: Q76 row drafted and shape-verified (5 cells, pure append); able to fail shown by `?? .ufo/wapes` → nothing after the move; the brief's `tracked_files` link corrected to the measured staging-time mechanism and two landed-row defects recorded unrepaired.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S07Quality.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81S07Quality.receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81S07Quality.md
