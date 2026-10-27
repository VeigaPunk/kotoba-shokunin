# SC06ReadmeCorpus — corpus/README.md draft (kotoba round 77, w1)

seat: SC06ReadmeCorpus (scribe, leaf)
lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`
base: lane HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e` (freeze); every scratch clone is
`git clone --shared` of that HEAD, and every gate call below names `--repo` / `-C` explicitly.
deliverable: `corpus/README.md` change as a unified patch against lane HEAD.
No tool was installed for this seat (no uv/npx/binary channel used; pacman never invoked).
No git/jj write was made in the lane; the only lane writes are the three paths in the
DELIVERABLES block.

## 1. What was drafted

One patch, one file (`corpus/README.md`), seven inserted lines:

**A. Five `## Coverage map` rows**, inserted after the existing
`| Round-74 verifier spot-check (closure) | ... |` row (patched-file lines 150–154):

1. `knowledge/description-craft-round76.md` — area "Description craft — S213's writing rules, and this
   lane's own `description` measured against them (round-76 data, landed round 77)"; basis: the five
   rule rows, the ≤25-word page-unique quote rule, the self-audit numbers (1022 clip / 1021 stripped /
   first sentence 151), guide-advice tier, `../verifiers/check_desc_craft.py --rev <rev>`
   (`target 6`, `0 of 6` at base `2f675548`), snapshot manifest + fetch record.
2. `lessons/round-76.md` — sections per the round-76 build draft: `## Gate` (S213 re-open, digest in
   four pinned homes), `## Mistakes` (M76-1 plus the slice off-by-one, vacuous red-before, reference-drift,
   scope and seat-arithmetic classes), `## Routed defects` (r75 R1–R4 closure record; carried r74 D1–D5),
   `## Round honesty` (honest stop; withdrawn C1 (a) with its replacement pins).
3. `lessons/round-75-verifier-spotcheck.md` — outside review by the hyaku closure; step-1 conformance,
   the S213/S211 re-opens, the bounded C1 verdict; records that it landed without an index row.
4. `lessons/round-76-verifier-spotcheck.md` — outside review; CD1–CD4 (stray `kotoba-shokukin/` path,
   absent lesson, unrun census, 52-file/64-seat gap), both claims unlanded, per-axis verdicts unchanged.
5. `lessons/round-77.md` — `## Gate` (S213 re-open rows + the two frozen counters' base receipts),
   the round's mistakes and routed-defect record, and the C1/C2 re-land record.

Rows 3 and 4 repair the measured base defect directly: at base the gate read
`unindexed 2` naming exactly those two files.

**B. One `## Frontier` note**, appended after the Round-74 note (patched-file line 239), in the
established append-only style — the Round-74 note is not rewritten. It records that the
description-writing guidance now sits in Core at the **guide-advice tier** (documentary evidence, no
client run, page statements recorded as the page states them) and names the frontier that does not
move: **eval fidelity** — whether following the guidance changes what a client routes to; the
trigger-eval protocol stays the round-70 reading and the round-74 note's
`optimizing-descriptions` trigger-eval design beyond S213 stays open.

Both paragraphs state the counter by its predicate (`description craft backed K of 6`, target 6,
`0 of 6` at base `2f675548`) rather than asserting a post-landing result — the landing seat measures it.

## 2. The index form, as the gates actually match it

Read from the instruments, not assumed:

- `verifiers/verify_corpus_integrity.py`: `file_column_tokens()` harvests **only** rows whose line
  starts with `|`, only inside the section opened by the exact heading `## Coverage map` and closed by
  the next `## ` heading; it takes `cells[2]` and every backticked token in it. Tokens are brace-expanded,
  glob-expanded against `git ls-files corpus/`, and — for non-glob variants — checked with
  `Path.exists`; `unindexed` counts tracked corpus files **not** covered by any token's expansion
  (`README.md` itself excluded).
- `verifiers/verify_corpus_independent.py`: same section rule (`stripped == "## Coverage map"`), same
  column, but it skips rows whose split has fewer than five fields — i.e. a row must be a complete
  `| area | file | basis |` row. Rows inside fenced regions are opaque in both.
- Consequence applied in the draft: every row is a full three-cell row, every column-2 token is the
  exact corpus-relative path (`knowledge/...`, `lessons/...`), no glob, no trailing slash, no
  placeholder mark; `../verifiers/...` pointers were kept in column 3 (unharvested) so the index
  population grows by exactly five checked tokens and nothing else.

## 3. Measurements (all from the receipts; own exit statuses, no pipelines)

| state | command (`$S` = scratch) | exit | observation |
|---|---|---|---|
| lane base `6523ace` | `python3 -B verifiers/verify_corpus_integrity.py --json` | **1** | `tracked_files 146` (baseline 144), `unindexed 2` (r75+r76 spot-checks), `report_total 102` (99), `commit_total 44` (43) |
| patch alone, no data files | integrity `--no-baseline --json --repo $S/applytest` | **1** | `unindexed 0`, `stale_patterns 0`, `missing_paths 3` (README:150/151/154), `report_total 102`, `commit_total 44` |
| patch alone, no data files | independent `--json --repo $S/applytest` | **1** | `unindexed 0`, `stale_tokens 3`, `missing_paths 3`, `index_tokens 167` |
| patch + data files (`entry-draft.md`, `lesson-draft.md`, labelled placeholder `round-77.md`) | integrity `--no-baseline --json --repo $S/final` | **0** | `tracked_files 149`, `index_patterns 167`, `unindexed 0`, `stale 0`, `missing 0`, `report_total 102`, `report_dead 0`, `commit_total 44`, `commit_unresolvable 0`, `commit_nonhash 0` |
| same | independent `--json --repo $S/final` | **0** | `tracked_files 149`, `index_tokens 167`, `unindexed 0`, `stale 0`, `missing 0`, `report 102/0`, `commits 44/0/0` |
| same, **unmodified** baseline | integrity `--json --repo $S/final` | **1** | DRIFT only on the three `equal` checks: `tracked_files 149`, `report_total 102`, `commit_total 44` |
| same, baseline expect = 149/102/44 (scratch only) | integrity `--json --repo $S/applytest2` | **0** | all nine checks PASS |

The apply check is `git -C $S/final apply --check <patch>` → exit 0 from lane HEAD, and
`git apply` → exit 0. Patch sha256
`9f7fe56dd11aafe8be8a6cbe5d0af8f4bfc5a01aa73f32d0491bbfc981c4781a`.

The data-file fixtures above are the **round-76 build drafts**, not new claims: entry-draft.md as the
knowledge entry's content, lesson-draft.md as the round-76 lesson. The round-77 lesson file in the
fixture is a one-line placeholder, used only to satisfy the existence test; nothing in this report
claims content for it.

## 4. Landing-order constraint (integration note for L1)

The README rows index files that do not exist at lane HEAD. Applying the patch **before** those files
land turns both corpus gates red with `missing_paths 3` — measured, not inferred. It must be applied
in the same commit as (or after) `corpus/knowledge/description-craft-round76.md`,
`corpus/lessons/round-76.md` and `corpus/lessons/round-77.md`. The two spot-check rows carry no such
constraint; the patch-alone run shows `unindexed 0`, i.e. they can land as soon as the README does.

## 5. Baseline deltas the L1 must pin (outside this seat's write scope)

The patch adds **no** report pointers and **no** `commit `<hex>`` citations — the measured
`report_total` stays 102 and `commit_total` stays 44 in the patch-alone and with-data runs. What moves
is the file population and the two counts that were already drifted at base:

- `corpus.index.tracked_files`: 144 → **149** (146 at base + the three data files)
- `corpus.pointers.report_total`: 99 → **102** (102 already at base; this patch contributes 0)
- `corpus.pointers.commit_total`: 43 → **44** (44 already at base; this patch contributes 0)
- observation only, not a check: `index_patterns` 162 → **167** (+5 rows)

With those three expectations the integrity gate reads 9/9 PASS, exit 0 (measured in a scratch clone).

## 6. Findings routed to other owners (not fixed here)

1. **The round-76 lesson draft carries a foreign commit citation.** `build/lesson-draft.md:183` reads
   `commit `69ef37e`` (an agentskills-repository object). Landed verbatim it makes the corpus gate
   `commit_unresolvable 1` / `commit_total 45` and the independent gate exit 1 — measured in a scratch
   clone. With the fixture-only wording change `commit ` → `revision ` (same hex), both gates return to
   exit 0 with `commit_unresolvable 0`. The lesson scribe / L1 should not land the `commit `<hex>``
   shape for a foreign object (the round-66 fleet-hop only covers the fleet root, and this object is in
   neither repository).
2. **`verifiers/corpus-baseline.json` is a separate edit** (§5). It is not part of this patch and I did
   not touch it.
3. The C1/C2 counters are untouched by this patch; the README is not read by either counter (the six
   conjuncts read the snapshots, the entry, `SKILL.md`, `SOURCES.md` and `corpus/lessons/round-76.md`).
   I did not run them: they are other seats' evidence.

## 7. Limits of this report

- The green runs in §3 use draft data files. They establish that the README rows are the form both
  gates accept and that the patch introduces no pointer/commit drift; they are not evidence that
  C1 or C2 is satisfied.
- The round-77 lesson row's section names follow the plan and the lane's lesson convention; the row is
  descriptive and can be adjusted by the L1 if the landed lesson's headings differ.
- The frontier note states the audit numbers the entry carries (1022 clip / 1021 stripped / 151 first
  sentence); it does not re-measure them — `check_desc_craft.py` conjunct (d) recomputes them at the
  measured revision, and that is the authority.

## 8. Artifacts

- patch: `.ufo/waves/round-77/build/SC06ReadmeCorpus.patch` (sha256 above; applies from lane root)
- receipts: `.ufo/waves/round-77/build/SC06ReadmeCorpus.receipts.txt`
- this report: `.ufo/waves/round-77/w1/SC06ReadmeCorpus.md`

Scratch (`/fast/scratch/hyaku/kotoba-r77/SC06ReadmeCorpus/`) was removed before yield.

VERDICT: README draft delivered and form-verified — five coverage rows plus a round-77 Frontier note apply cleanly at lane HEAD, both corpus instruments exit 0 once the indexed files exist, and the patch adds zero report/commit tokens; the baseline refresh (149/102/44) and the draft lesson's foreign `commit `69ef37e`` shape are routed to their owners.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC06ReadmeCorpus.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/build/SC06ReadmeCorpus.receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w1/SC06ReadmeCorpus.md
