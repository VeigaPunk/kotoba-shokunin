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
  `w1/ReviewerC1.md`, and the `Sentinel` row of `w1/r87-w1-results.json` — the seat wrote no file of
  its own): survivors are reported, not patched.
- `verify_skill_checklist.py` `governance.citation_resolves` stays red at base and tip (a carried
  red, unchanged by this round).
- `corpus/lessons/round-81.md:8` and the round-86 spot-check line 33 stay red until an operator or a
  closure ruling authorises an edit to a non-author record (an L0 question is filed).

## Attempt 2 — re-verification at the round tip (driver cycle 2, attempt 1)

**Inherited (re-verified, reused).** Attempt 1 landed the round at lane tip
`760e1c5edfdefb4767420f711d08f669952de013` and filed its report at fleet commit
`d752fdbe9cdf82a6faff730d44f44c6fa3e3eb00`; the driver relaunched round 87 after two provider-401
attempts (`grep -n 'kotoba round=87' .ufo/watchdog.log` → two `lane-dead-no-report` lines, then the
23:51 `launch`). The lane worktree was clean and `local == remote == 760e1c5e`; nothing inherited was
discarded, and no uncommitted lane output existed.

**Measured at `760e1c5e`** (receipts `.ufo/waves/round-87/w3/l1/c1-tip.txt`, `q79-control.txt`):

- **C1 re-derives unchanged:** `omp root semantics grounded 12 of 12`, `exit=0`, guards S1–S3 PASS.
- **C2 reads `4 of 5`, `exit=1`:** D1–D4 PASS, D5(i)/(ii)/(iv) PASS, **D5(iii) FAIL** —
  `verifiers/verify_corpus_integrity.py` now prints
  `red set ['corpus.pointers.commit_unresolvable'], want exactly ['corpus.pointers.commit_unresolvable', 'corpus.pointers.report_dead']`.

**Cause (measured, not inferred).** `report_dead` healed: the fleet-root kama report cited at
`corpus/lessons/round-86-verifier-spotcheck.md:33` landed on the fleet repo at 22:47 (fleet commit
`5b052020a13b37340c1054286d65b2514c7133d5`), after the C2 receipt was written. The same committed lane
bytes therefore read 5 of 5 before 22:47 and 4 of 5 after it. A second reading of the same bytes in a
`git clone --shared` checkout gives a third state: `red=['commit_unresolvable','report_dead']` with
the detail at `corpus/lessons/round-81.md:29` (a `../../` pointer), so d5 also refuses on the detail
site. Copying the two fleet reports into the clone's own resolution root reproduces the lane's
reading exactly, which pins the causal variable to the external files and not to the lane's corpus.

**Disposition.** C2 is recorded as **4 of 5 at the tip**, not narrowed and not re-worded: the target
`5 of 5` and D5(iii) as frozen by addendum 2 stay exactly as declared, and the round's after-receipt
`receipts/c2-final.txt` (5 of 5 at `35a395a9`) stands as the measurement of its own revision. The
frozen counter is **not** amended — a rule changed after data is not the claim's rule (kumitate r42;
tsukuroi r82 ruling). The repair is routed to r88: D5(iii) becomes monotone (`red ⊆ disclosed set`,
details tested as a subset, the external paths named in the item) and the Q79 control runs over the
lane, a relocated clone and a pinned world. `MutateR87` measured the repair's shape against the
frozen counter: the subset form is a **surviving mutant** because D5(iii)'s tally pin (`7/9 checks
pass`) also refuses the healed corpus (the gate now reads `8/9`), so the r88 recipe must relax the
tally conjunct together with the red-set equality (`w3/MutateR87/base/d5-forms.txt`).

**Wave `r87-w3` findings (12 seats; receipts under `.ufo/waves/round-87/w3/`).**

- **C1 corroborated independently.** `ReviewC1R87` re-implemented the four conjuncts from
  `plans/round-87.md` alone (`w3/ReviewC1R87/reimpl.py`, written before reading the counter) and scored
  `reimpl grounded 12 of 12` with **no per-row disagreement** against the frozen counter
  (`w3/ReviewC1R87/verdicts_diff.txt`); it also confirms the counter is byte-identical between the
  addendum-2 commit and the tip.
- **C1's counter is not discriminating — the question Q71 asks, answered against the claim.**
  `CriticSemanticsR87` first confirmed the honest data byte-wise: all 12 reader quotes sit inside
  executable function bodies (`function`/`const`/`return`/`map(` syntax in the surrounding bytes), and
  for every row the nearest preceding `// packages/<module>` header is the row's own module, so no
  landed attribution is doubtful (`w3/CriticSemanticsR87/attribution.txt`, `elf-bytes.txt`). It then
  built four forgery worlds in a scratch clone and **all four read `12 of 12`, exit 0**
  (`w3/CriticSemanticsR87/forgery-worlds.txt`, `forgery-ledger-diffs.txt`): row 7's quote replaced by
  the codex reader, row 9's by `Zo.join(R.path, "commands")` (the same module's *commands* subdir),
  row 12's by the plugin row's quote from a different module chunk, and row 6's by
  `**Tags:** ${t.tags.join(", ")}` — a markdown template whose `Array#join` satisfies `JOIN_TOKENS`.
  The reason is structural: conjunct 1 never reads the quote and conjuncts 2/3/4 never read the
  pattern, so a quote that names no segment of the row is indistinguishable from one that names it,
  and `JOIN_TOKENS`' `.join(` / `resolve(` also match `Array#join` and `Promise.resolve`. Per Q71/Q74
  the round names that mechanical score beside the target: **the script-only world reaches 12 of 12**,
  so C1 is not admissible on the number; what it rests on is the byte-level attribution, the upstream
  diff (S256's pin is byte-identical to `raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/…`
  `omp-plugins.ts`, `upstream.txt`) and the live probe below. The critic also names a row-level gap
  under the strong reading: row 5's quote builds `{cwd}/.codex` only, with the `skills` segment a
  separate statement 3 098 B later. Routed to r88: bind a row's quote to the row (require the joined
  leaf/literal in the same expression and path-qualified join tokens), and quote row 5's exact
  `skills` join.
- **C1's `{cwd}/` bound observed, not inferred.** `ExecProbeBoundR87` enumerated the installed client
  under a scratch `HOME` with `omp skill list --json`: the cwd-chain skill reads
  `"source":"agents:project"` and the skill directly under the scratch `HOME` reads
  `"source":"agents:user"`; from a cwd outside `$HOME` only the user-scope skill appears; and
  `strace -f -e trace=%file` shows **zero** opens of any `.agents/skills` above `$HOME` and **zero**
  `..`-segment probes (`w3/ExecProbeBoundR87/strace_skilllist.txt`, `skill_list_json.txt`,
  `skill_list_outside.txt`). Conjunct 4's "unless the row is a `~/` row" carve-out is live in the real
  binary at v18.15.0 — the round-86 CF2 hole is now closed by observation, not by a quote. The probe
  is recorded as a capability row in `SCORECARD.md` § Capabilities (first working round 87).
- **Coverage gap measured: the ledger is 12 of 18 roots.** `ScoutPatternsR87` re-derived the skill-root
  set from the ELF before reading either ledger (`w3/ScoutPatternsR87/derived-roots.txt`,
  `three-way-table.md`) and found **six** joins neither ledger carries: `~/.claude/skills`
  (@173840218, `Zte()` → `Fr.join(p, "skills")`), `~/.codex/skills` (@173882129, `mre()` →
  `Xr.join(p, "skills")`), `~/.config/opencode/skills` (@172785499, `V$e()` →
  `d.join(e.home, r.userAgent, n)`), `~/.omp/skillshare/@scope/*/*` (@173923798, `Tie()`/`VH()`), and
  two plugin-marketplace roots (@173851107, @173778070). The L1 re-read those four offsets independently
  (`dd` over the ELF) and they are joins, not doc strings. So C1's `12 of 12` is **12 of a 18-root
  surface** — a coverage hole, not a depth result, and the next round's obvious move: extend the ledger
  to the user-level claude/codex/opencode and skillshare roots, and use the probe capability to
  establish which of them bear `SKILL.md`. The critic's row-5 gap is the same class at a smaller scale.
- **C2 re-derived item by item.** `ReviewD1D5R87` re-checked D1–D5 from committed bytes without
  trusting the counter: D1, D2, D3 (5 reject rows, longest 52 words), D4 (5 verbatim spots) and
  D5(i)/(ii) (`ae3f49a3…`/`315c0ec6…` = base) all PASS; D5(iii) FAIL at the tip for the healed-red
  reason, and the seat classifies the tip reading as `4 of 5`. It also confirms that the round's own
  after-revision `35a395a9` now reads `could-not-evaluate` (the d5(iii) tip pin), so the 5-of-5 row is
  re-derivable only from its committed receipt.
- **Adoption hazard measured (`ConnectOverlapR87`).** The staged `merge/kotoba/` package is real
  (mtime 2026-10-24 23:33, 188 rows, 88 entries, rounds 1–16) but its id space **overlaps** the
  lane's: staged `S256` is the `agentskills.io` row the lane already holds as `S002`, while the lane's
  `S256` is the omp reader row — same id, different source. Adoption therefore needs a renumbering
  map computed in scratch, by document, before any append. Nothing was adopted this round (the freeze
  admits one `SOURCES.md` row); the L0 question records it.
- **Correction to the attempt-1 report.** Its `Assimilation: none` line said
  `/home/vgpnk/Projects/shokuknow/merge/` was absent. The directory exists and has since
  2026-10-24 23:33 (`stat -c '%y %n'`); what is true is narrower — no staged material overlaps this
  round's claims, and the frozen touch list admits one row. The line is corrected in the report, not
  rewritten in place here.

## Record corrections from the attempt-2 audit

- **`w3/l1/c2-base-clone.txt`** carried a false `exit=0` on its first committed version (the `tee`
  pipeline's status, not the counter's) and only the failed command; rewritten to state what the
  frozen instrument can and cannot measure at the base, with both observed exit codes
  (`SentinelEvidenceR87` finding F-2).
- **`census-now.txt`** was cited in `LOG.md` before it existed; written
  (`.ufo/waves/round-87/w3/l1/census-now.txt`, `exit=0`, 33 `W04`, 0 `E`, 182 rows)
  (`ScribeIndexR87`'s dangling list).
- **`w1/Sentinel.md`** was cited but never existed (that seat wrote no file); the record now names the
  seat's row in `w1/r87-w1-results.json`.
- **`receipts/q73-sweep.txt`** is promised by `plans/round-87.md` and does not exist; the sweep is the
  `q73_sweep` section of `receipts/base-battery.txt` (the plan is frozen and is not edited; this line
  is the correction).

## Mistakes — attempt 2

**M87-2 — an exact-set expectation turns another actor's deliverable into a verdict, and punishes a
repaired pointer.** The round's D5(iii) required the corpus gate's red set to equal exactly two
DRIFTs. One of the two was a fleet-root report pointer; when that report landed, the red set shrank
to one and the item flipped from PASS to FAIL with no change to the lane's bytes. Class: a counter
whose expectation is an exact set of *currently broken* things — it reads as "carry the red
honestly" but scores "keep the red". Evidence: `q79-control.txt` (lane / clone / pinned worlds, two
readings at one revision); `receipts/c2-final.txt` against the tip run in `w3/l1/c1-tip.txt` and
`q79-control.txt`. **Captured-by:** Q63 — "a gate whose verdict depends on where the checkout sits …
is never relocated into a temp-dir sandbox" — the lane has held Q63 since r70 and its own new
counter violated the half of it that names the resolution set, because the counter was only ever run
in the lane. **Fix:** Q79 in `corpus/QUALITY.md` plus the control
`.ufo/waves/round-87/w3/l1/q79_location_control.py`, which runs the lane, a relocated clone and a
pinned world and fails when their readings differ. **The fix is shown able to fail:** on this
revision it prints `q79 control: FAIL (same bytes, world-dependent verdict: 2 distinct readings)`,
`exit=1`, while the pinned world it also runs shows the passing world it would need.

## Gate — attempt 2

| candidate | decision | reason |
|---|---|---|
| re-running C2 at a revision or in a checkout where `report_dead` is still red, to restore `5 of 5` | **reject** | the state would be manufactured by copying or withholding another actor's file, so the score would measure the harness rather than the corpus (Q79) |
| amending `verifiers/check_r86_routed_repairs.py`'s d5 to a monotone form after the first candidate score | **reject** | the kill rule freezes the predicate at `plans/round-87.md`; a rule changed after data is not the claim's rule, whatever it later passes (kumitate r42; tsukuroi r82 ruling) |
| editing `corpus/lessons/round-81.md:29` or the round-86 spot-check line to put the red back | **reject** | it is the M87-1 laundering move on a non-author record and a historical lesson, which Q64 and D5(i)/(ii) forbid |
