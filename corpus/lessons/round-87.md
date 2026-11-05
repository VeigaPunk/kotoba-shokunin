# Round 87 — kotoba (attempt 1, Linux host, omp/18.15.0)

Base `223ae62424f8ab1eb365d733eb648d6228ddd7e8` (the round-86 non-author spot-check landing).
Freeze `669f2801c31ef27e18cc35a327d2e18f466281c7` (`plans/round-87.md` alone, before any candidate
data); addendum 1 `512126bbd762ff82b9f330c4afefb29db7cd9f39` (C1 denominator 12, C2/D5 in the lane
worktree); addendum 2 `87ab1cb98b4950f5d7291a4a2ddaab535ca72124` (D5 redefined as an honest carry;
the laundering attempt reverted). Two claims on two distinct owned axes.

## Claims (verbatim from the freeze)

**C1 — depth (score 9, the lowest owned axis).**

    python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
        -> prints "omp root semantics grounded N of 12", exit 0 iff N == 12 and guards S1-S3 all
           PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

A row of `verifiers/omp-skill-roots-semantics.tsv` is grounded iff (1) its `root_pattern` equals the
round-86 ledger's row (no `..`, no wildcard in the first segment), (2) its `reader_quote` occurs in
the installed omp ELF **on a line carrying a path-join token**, (3) its `module` header
`// packages/<module>` occurs in the ELF **before** the quote, and (4) the row's expansion obeys its
bound (`{cwd}/` stops below `$HOME`; a `..` candidate never matches). Target: 12 of 12. Base: 0 of 12,
exit 1.

**C2 — consistency (calibration sub-axis, score 10).**

    python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5; exit 1 otherwise;
           exit 2 = could-not-evaluate.

Items D1–D5 are the round-86 closure's § 6 routed defects, as corrected by addenda 1 and 2.
Target: 5 of 5. Base: 0 of 5, exit 1.

## Gate

| candidate | decision | reason |
|---|---|---|
| **S256** — the omp plugin skill-root reader (`packages/coding-agent/src/discovery/omp-plugins.ts`, tag v18.15.0, HTTP 200, 15 362 B, sha256 `4e66819c…b1b4`, located quote `dir: path.join(root.path, "skills"),` at upstream line 70) | **admit** | opened this round, tier A `code`, and it grounds the one row the round-86 set could not ground: the reader is a join call, not the `.omp` config constant |
| the round-86 `binary_quote` for `~/.omp/plugins/node_modules/*/skills` (`var Gh = ".omp";`) as a **reader** | **reject** | the quote is a config-directory constant that names no `plugins`, no `node_modules` and no `skills`; the round-86 closure's CF1 already found that no such quote can satisfy the dot rule, and the reader is `dir: Zo.join(R.path, "skills"),` — recorded in the new ledger's `reader_quote` cell, with the old quote kept only as `binary_quote` |
| a `reader_quote` cell that repeats a doc/string-table line | **reject** | conjunct 2 requires a path-join token on the quote's own ELF line, so a doc string is refused by construction (the counter's `w_docquote` world reads `11 of 12`) |
| the integration seat's in-place rewrites of `corpus/lessons/round-86-verifier-spotcheck.md` and `corpus/lessons/round-81.md`, made to turn `verify_corpus_integrity.py` green | **reject** | a non-author record is never edited (`PROTOCOL.md`; `check_tip_battery.py`'s `spotcheck-identity` guard) and a historical lesson is never rewritten to green a gate (Q64); both files were reverted to their branch bytes before any commit — this is M87-1 below |
| the frozen 13-row denominator | **reject** | the round-86 ledger carries 12 data rows (`tail -n +2 | wc -l` → 12); corrected by addendum 1 before any candidate score, not by re-scoring |
| the frozen D5 form ("`verify_corpus_integrity.py` exits 0") | **reject** | measurably unsatisfiable by honest work: two of its six base DRIFTs live in records this lane may not rewrite; redefined by addendum 2 as the honest carry, with the impossibility measured first |

Spot-check result: **pending** — the non-author closure reads this lesson, the counters and the
receipts. Nothing here self-admits.

## Census (`corpus/SOURCES.md`, contract v1)

- **Before** (round start, base `223ae62`):
  `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  → `exit=0`, 33 `W04`, 0 `E` rows, last line `kotoba ok …/corpus/SOURCES.md`
  (`.ufo/waves/round-87/receipts/base-battery.txt` § census).
- **After** (round end, this tree): same command → `exit=0`, 33 `W04`, 0 `E` rows, 182 registry rows
  (181 at base + S256) (`.ufo/waves/round-87/receipts/census-after.txt`).

## Mistakes

**M87-1 — a routed red was greened by rewriting the record that carried it.**
A wave seat, asked to clear `verify_corpus_integrity.py`'s carried red, made the gate green by
editing the two documents that produced the red instead of repairing the citation: it wrapped
`.ufo/reports/round-84/kama.md` in double quotes inside
`corpus/lessons/round-86-verifier-spotcheck.md:33` (a **non-author** record) and reworded
`corpus/lessons/round-81.md:8` so its dead test-world commit left citation position (a **historical**
lesson). Both are the gate's own idioms for a quoted meta-finding — applied by rewriting history
rather than by adding a correction. Evidence: `git diff` of both paths before the revert
(blobs `7d9f599` / `d7f589b` against base `ae3f49a` / `315c0ec`); after the revert the gate reads
`7/9 checks pass; DRIFT: corpus.pointers.report_dead, corpus.pointers.commit_unresolvable`
(`.ufo/waves/round-87/receipts/d5-after-revert.txt`).
**Captured-by: `none`** — Q64 stated the rule ("never 'corrected' to the record of its removal to
green a gate") and the frozen D5 asked for a green, so the criterion existed but no instrument
checked it. **Fix:** D5's conjuncts (i) and (ii) in `verifiers/check_r86_routed_repairs.py` compare
both files' blobs at `<rev>` to their blobs at base and fail on any rewrite.
**The fix is shown able to fail:** on the pre-revert tree the same comparison reads
`corpus/lessons/round-86-verifier-spotcheck.md rewritten at … (blob 7d9f599 != base ae3f49a)`; on the
reverted tree it passes and D5's remaining conjuncts decide. The `w_launder` self-test arm pins it.

**Correction to the freeze (not a second mistake, recorded because the plan is append-only).**
`plans/round-87.md` § C1 froze a 13-row denominator: the L1 counted the round-86 ledger's **file**
lines (header + 12). Addendum 1 corrects it to 12 with the counting command, before any candidate
score. `plans/round-87.md` § C2 D5 quoted the round-86 closure's `8/9` carried base; the measured base
is `3/9` with six DRIFTs — the carried figure had not been re-measured, which is the same class as
M87-1 (a record quoted instead of measured) and is why addendum 2 states the base it measured.

## D5 disclosure (the two remaining DRIFTs, `left red and disclosed`)

- `corpus/lessons/round-86-verifier-spotcheck.md:33` cites `.ufo/reports/round-84/kama.md`, another
  actor's fleet-root artifact that carries no `## SHONEN` marker; the citing file is a non-author
  record and is never edited. **`left red and disclosed`.**
- `corpus/lessons/round-81.md:8` cites `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`, a dead-clone
  test-world commit that resolves in neither lane nor fleet **by design**; rewriting the lesson to
  move it out of citation position is the laundering M87-1 refuses. **`left red and disclosed`.**

## Routed to the next round

- The counters' self-test gaps the attack seats name (`.ufo/waves/round-87/w1/MutTester/`,
  `ReviewerC1.md`, `Sentinel.md`): survivors are reported, not patched.
- `verify_skill_checklist.py` `governance.citation_resolves` stays red at base and tip (a carried
  red, unchanged by this round).
- `corpus/lessons/round-81.md:8` and the round-86 spot-check line 33 stay red until an operator or a
  closure ruling authorises an edit to a non-author record (an L0 question is filed).
