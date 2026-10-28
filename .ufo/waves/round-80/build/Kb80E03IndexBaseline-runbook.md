# Kb80E03IndexBaseline — C1 repair 3: coverage rows + baseline refresh (runbook-order findings)

Seat: `Kb80E03IndexBaseline` (executor, leaf). Date: 2026-10-27.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E03IndexBaseline` (five clones: `clone`, `wA`, `wA2`, `wB`, `wC`, `verify`, `verify2`, `verify3`), removed after receipts were copied.

Deliverables (all under `.ufo/waves/round-80/build/`):

| file | sha256 | bytes | what it is |
|---|---|---|---|
| `Kb80E03IndexBaseline.patch` | `54e43309e05af3f98d23b030f811d9a729aa865b2dea6a9dc8dc778cf9d796f9` | 4818 | **the three `corpus/README.md` coverage-map rows, README-only** (1 hunk, 3 added rows, 0 deletions) |
| `Kb80E03IndexBaseline.baseline-snapshot.patch` | `ec6c2ea4b3ad0b3d7dad661763bc6ca1f1f3ead7adb14d6350f7706f1a35b3bc` | 5110 | the re-recorded `verifiers/corpus-baseline.json` (probe world C) — **a preview, NOT a landable artifact** (see §4) |
| `refresh-corpus-baseline.py` | `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a` | 20188 | the r79 script copied **byte-for-byte verbatim** from `.ufo/waves/round-79/build/`; unchanged |
| `Kb80E03IndexBaseline/` | — | — | 11 receipts (4 worlds × 2 gates + 3 refresh transcripts), each with its own exit status |

---

## 1. What the two corpus gates actually read (measured, not inferred)

Both gates read the coverage map the same way: **column 2 of every pipe-starting row between `## Coverage map` and the next `## ` heading**, backticked tokens only, fenced regions skipped.

- integrity gate: `file_column_tokens`, `verifiers/verify_corpus_integrity.py:388-421`; section rule `SECTION_HEADING_RE`/`COVERAGE_HEADING_RE` at `:155-157`.
- independent gate: `coverage_cells`, `verifiers/verify_corpus_independent.py:317-346`, independently written.

One backticked corpus-relative path in column 2 is the whole requirement. Measured on the patched README: **column-2 patterns 169 → 172**, and the three new tokens are exactly
`(157, 'lessons/round-79-verifier-spotcheck.md')`, `(158, 'lessons/round-80.md')`, `(159, 'knowledge/allowed-tools-surfaces-round80.md')`.

Column 3 (the basis cell) is prose but **not inert** for the integrity gate — it is scanned for `.ufo/reports/round-<n>/*.md` pointers and `commit `<hex>`` citations. All three rows were checked against the gates' own regexes (`UFO_POINTER_RE`, `COMMIT_RE`): **0 report pointers, 0 commit tokens**. The `..`-hop landmine from the r79 E02 seat (the governance gate caps `..` hops at 3) was checked too: row 3 contains three `../` tokens, **max hop depth 1**.

## 2. The four measured worlds (each command's own exit; no pipelines for verdicts)

Every world is a `--shared` clone at base, `rev-parse --show-toplevel` asserted to be the clone, committed and clean.

| world | contents | integrity | independent |
|---|---|---|---|
| **base** | base `398cbe1` | exit 1 — `tracked 152, unindexed 1, stale 0, missing 0, report_total 109, report_dead 1, commit_total 46, unresolvable 2` | exit 1 — `tracked 152, unindexed 1, report_dead 0, commit_total 46, unresolvable 2` |
| **wA** | rows + the two new corpus files (current bytes), **no instrument repair** | exit 1 — `tracked 154, unindexed 0, stale 0, missing 0, report_dead 1, commit_total 46, unresolvable 2` | exit 1 — `unindexed 0, stale 0, missing 0, report_dead 0, unresolvable 2` |
| **wA2** | **rows only**, the two new corpus files absent | exit 1 — `unindexed 0` but **`stale_patterns 2`, `missing_paths 2`** | exit 1 — same two classes red |
| **wB** | wA + E04 pointer repair | exit 1 — `report_dead 0` (was 1), `unresolvable 2` still red | exit 1 — `unresolvable 2` still red |
| **wC** | wB + a **scratch-only probe** grammar class | exit 1 on the three stale expectations only (`tracked 154`, `report_total 109`, `commit_total 46`); **`unresolvable 0`** | **exit 0**, all checks PASS |

**The load-bearing result — `unindexed` 1 → 0.** At base the single unindexed file is `corpus/lessons/round-79-verifier-spotcheck.md`; row 1 closes it. Rows 2 and 3 close the index gap for the round's two new corpus files.

**The rows do not touch the reds.** wA (rows, no instrument repair) still reads `report_dead 1` and `unresolvable 2`. This is exactly plan **W3**: repairs 4 and 5 are load-bearing, and the rows are not a substitute for them.

**The ordering trap is real and measured (wA2).** A coverage row whose target file is absent is **two** classes red, not one: `stale_patterns` +1 **and** `missing_paths` +1 per row. With both new rows landing before their files, the gate reads `stale 2, missing 2`. **The two corpus files must be tracked before (or with) the rows** — never after.

**The refresh refuses until repairs 4 and 5 land.** Three refusal transcripts, own exit status:

- wA (rows, no repair): exit **2** — `refused: zero-mode corpus.pointers.report_dead observed 1, not 0; fix the drift (or name the known residual with --carry) -- a baseline never records a zero-mode value`
- wB (rows + E04): exit **2** — `refused: zero-mode corpus.pointers.commit_unresolvable observed 2, not 0; …`
- wC (rows + E04 + probe class): exit **0** — wrote the baseline, `post-refresh: 9/9 checks pass, exit 0`, `independent: exit 0`. The three `equal` expectations moved `tracked_files 144 → 154`, `report_total 99 → 109`, `commit_total 43 → 46`; every zero-mode expectation stayed 0.

The refusal order is informative: the script stops at the **first** zero-mode class that is non-zero, so E04 alone unblocks `report_dead` and the run then stops at `commit_unresolvable`. **No `--carry` is needed at the tip** once repairs 4+5 land — the wC run used none, and every zero-mode expectation in the written file is `0`.

## 3. The runbook order the L1 must run (measured, not guessed)

1. **Land the two new corpus files** (`corpus/lessons/round-80.md` from `Kb80S01Lesson.md`; `corpus/knowledge/allowed-tools-surfaces-round80.md` from E08's file) **and commit them.** If the rows land first, the gate reads `stale 2 / missing 2` (wA2).
2. **Apply `Kb80E03IndexBaseline.patch`** (README rows only, 1 hunk, +3 lines) **and commit.**
3. **Apply E04** (`Kb80E04DeadPointer.patch`, published) and E05 (both corpus gates) and commit. Until E05 lands, `commit_unresolvable` is 2 and the refresh refuses.
4. **Run the refresh** from the lane toplevel with a clean tree:
   `python3 -B .ufo/waves/round-80/build/refresh-corpus-baseline.py --repo .`
   → exit 0, writes `verifiers/corpus-baseline.json`, prints `post-refresh: 9/9 checks pass, exit 0` and `independent: exit 0`. **No `--carry`.**
5. **Commit `verifiers/corpus-baseline.json` alone** (path group 2). The recorded `head` is step 3's commit, so the label names a real lane object.
6. **Re-run both corpus gates** (`verify_corpus_integrity.py --repo .` → exit 0, `verify_corpus_independent.py --repo .` → exit 0) and then the tip battery in both `--repo .` and absolute forms.

The script's own preconditions, all verified in the worlds above: `--repo` must be the toplevel of a git work tree; `git status --porcelain --untracked-files=all` must be **empty** (the gate reads worktree bytes while the baseline records HEAD); `verify_corpus_integrity.py --self-test` must exit 0 (measured at base: `self-test: 0 failure(s) over 164 assertions`); the two gates must agree on the six `equal` classes or the script refuses.

## 4. `Kb80E03IndexBaseline.baseline-snapshot.patch` is a PREVIEW, not a landable artifact

It was produced in wC, whose tree carries a **scratch-only probe** grammar class that is not E05's. Two fields inside it are probe-labelled: `measured_against.head_subject` is `PROBE external class` and `head` carries the script's detached-measurement-commit label. **The L1 must not apply it.** Step 4 above re-derives the file at the real tip with the real E05 bytes. The preview's value is the three moved expectations (`154 / 109 / 46`) — the numbers the L1 should see — and its `notes` key `round79_rerecord` shows the note-key to pass (`--note-key`) for round 80.

## 5. Findings the L1 and the other repair seats need

### F1 — the plan names the wrong failing tokens, and the grammar class must reach a bare-hex token
The plan's Trigger names the two `commit_unresolvable` tokens as `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`. **Measured, both are wrong** — at base the two unresolvable subjects are `corpus/SOURCES.md:171` and `corpus/SOURCES.md:172`, and **both are the same hash** `7bb48f213ac677f943d5c791199ed3dddf302f00`. `451a02ff` and `cfb894a5` are in the gates' `commit_quoted` class (6 entries) — already excluded, never unresolvable. A sweep of every `commit `<token>`` in the base corpus (55 harvested) finds **zero** tokens in the `owner/repo@<hex>` grammar; the `owner/repo@<hex>` strings that exist in the corpus sit in SOURCES.md anchor cells **without** the word `commit` before them, so `COMMIT_RE` never harvests them.

The real line shape is `… resolved to `badlogic/pi-mono` commit `7bb48f21…`` — the third-repo name is a **separate backticked token on the same line**, and the second row names the repo only in the row title/URL. **A class keyed on the in-token grammar clears nothing.** The plan's own clause "*(or otherwise an explicit third-repository citation)*" is the load-bearing one; it must operate at **line scope**. (Independently confirmed by `Kb80L01Grammar` and `Kb80V03Instruments`; messaged to `Kb80E10Battery` and `Kb80E14C1Worlds`.)

### F2 — the entry file no longer adds a third unresolvable (hazard closed mid-wave)
An earlier build of `allowed-tools-surfaces-round80.md` carried a full-hex `commit `7bb48f21…`` citation, which **would** have made `commit_unresolvable` 3 the moment the entry landed (measured in my first wA build: `unresolvable 3`, detail `corpus/knowledge/allowed-tools-surfaces-round80.md:95`). E08 has since revised the file: the current bytes (sha256 `037c3b61…`, 24,726 B) carry **0 commit-shaped tokens and 0 report pointers**, and the file no longer contains `7bb48f` or `bb65e3e4`. My published receipts were all re-measured against the current bytes. **The third instance is gone** — but the hazard is real for any future entry revision: a documentary entry that cites a third-repo digest in the `commit `<hex>`` form adds a corpus-gate red the moment it lands.

### F3 — the instrument-size cap arithmetic is tighter than the plan's words
The counter's `instrument-size` guard diffs the six battery scripts against its **pinned r72 base `072048fa`**, not against `398cbe1`. Measured at base: `check_assertion_floors.py` **+22 / −3**, all other five **+0** → **22 added** at base. E04 adds **+17** on `verify_corpus_integrity.py` → **39**. Under the plan's amended `LINE_CAP` 60, the grammar class has **60 − 39 = 21 added lines to spend across BOTH gates**. A grammar class whose self-test arms live in the two gates' own bytes cannot fit 21 lines across both files. The cap arithmetic in the plan (§C1, "22 already spent at base + 17 E04 + grammar ≤ 21 = 60") is *arithmetically* right but **practically infeasible as scoped**; E06's `LINE_CAP` amendment and E05's class shape must be reconciled, and the reconciliation declared. The E04 blob id that must be pinned is `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` (measured from the applied world B; matches the published `Kb80E04DeadPointer.blob`).

### F3b — the counter's pin table must gain the round-80 blobs (owned by E06, closed there)
`build/Kb80E06CounterErratum.cap60-provisional.py` is the **cap-only provisional** and its `INSTRUMENT_PINS` table still carries only the two old `verify_corpus_integrity.py` pins (`71cb2730…`, `e470eaae…`) — the E04 blob `051b8c5f…` and E05's two blobs are absent, so that table as-is cannot read `guards 5 of 5` on an E04 stack. E06 confirms the final patch will carry the pins: the `verify_corpus_integrity.py` row gains **both** `051b8c5f…` (E04-only) and the E04∘E05 composed blob (the guard's test is `blob not in allowed` over a tuple, so one row may hold several allowed blobs — the pin set then holds for either stack and the integration-order hazard disappears), the `verify_corpus_independent.py` row gains E05's blob, and the other four instruments are already pinned and unchanged by every published r80 artifact. Composition order stated as **E04 first, then E05** (the plan's repair numbering), with the reverse order measured.

### F4 — `MANIFEST.sha256` does not exist where the rows and the counter's conjunct (c) look for it
`.ufo/waves/round-79/snapshots/` holds six per-page snapshots, six `.fetch.json` and six per-page `.manifest` fragments — **no `MANIFEST.sha256`** (measured absent; the round-80 snapshots directory does not exist either). The sibling `Kb80S08ReadmeRows` rows and the C2 counter's snapshot-pin conjunct both name that path. The L1 must publish the assembled manifest at the path the counter reads (or the counter's conjunct (c) must name the six per-page fragments). **Not this seat's to repair** — corpus/ is out of my write scope, and the counter is E07's.

### F5 — the sibling's rows and mine are the same three rows; apply ONE, not both
`Kb80S08ReadmeRows.patch` (published by the scribe seat) adds **the same three rows** plus a `## Frontier` note hunk. The three row lines are **byte-identical** to mine (measured: each of my three `+|` lines is a substring of S08's `+|` lines; the patched coverage-map sections are **identical**, 152 rows each). Applying S08's patch and then mine **fails**: `error: corpus/README.md: patch does not apply` (exit 1) — the second patch's context is gone. The README sha256 after S08's patch is `9db6cc91a6942679c45d118896ee4780563da859b43defcac65b6935355d75a1`; after my rows-only patch it is `6d898bcc710993253529477cd88df1ca09dc2eaeefd3c4f8306bc61a5fed0d3b` (they differ only by S08's extra Frontier note). **The L1 must apply exactly one rows patch.** S08's is the superset (rows + Frontier note) and is already published and reviewed — **S08's patch is the one to apply**; mine is the same rows without the note, published as the repair-3 executor's own artifact and as the byte-level proof of the index delta.

### F6 — the coverage-map rows' `..` hops are within the governance bound
Row 3 cites `../.ufo/waves/round-79/snapshots/MANIFEST.sha256` and `../verifiers/check_allowed_tools.py --rev <rev>` — three `../` tokens, **max hop depth 1**, inside the governance gate's 3-hop cap. The four-hop string from the r79 E02 landmine is **not** written backticked anywhere in the rows.

## 6. What this seat did NOT do

- Did **not** edit any lane file: the lane's `corpus/README.md` is unchanged on disk (the rows exist only as a patch under `.ufo/waves/round-80/build/`). No git mutation in the lane — read-only `git log/ls-tree/rev-parse/cat-file/show` only. No `jj` command.
- Did **not** write to `corpus/`, `verifiers/`, `SKILL.md`, `PROVINCE.md`, `MANIFEST.json`, `SCORECARD.md`, `LOG.md`, `templates/`, `scripts/`, `.ufo/state/`, `plans/`.
- Did **not** score any claim after-value: no tip-battery run, no `check_allowed_tools.py` run, no SCORECARD row. The tip battery is the L1's post-integration measurement.
- Did **not** author the grammar class (E05), the counter erratum (E06), the pointer fix (E04), the symlink (E02), the registry rows (E01) or the C2 entry (E08). The scratch grammar class in wC is a **probe**, exists only in the scratch clone, and is **not** published as a patch.
- Did **not** modify `refresh-corpus-baseline.py`; the published copy is byte-identical to the r79 original (sha256 `8481be46…`).
- No tool install or upgrade (none needed); **pacman untouched**; no host service restarted.

## 7. Limits

- The refreshed baseline in §4 was measured under a probe grammar class, not E05's bytes. The three moved expectations (`154 / 109 / 46`) should reproduce at the real tip, but the file must be re-derived (step 4) — the `measured_against` block would otherwise name a scratch commit.
- wA's two corpus files are the sibling drafts copied into the scratch clone as fixtures; the L1 lands the real bodies (and the real bodies' bytes may move `report_total` / `commit_total` by a line or two — re-derive).
- The `unindexed 1 → 0` result is measured against the gates' own `--json` observations on committed bytes, not inferred from the row text.
- Scratch removed after receipts were copied (checked by absence, not asserted).

VERDICT: The three coverage rows land cleanly on base `398cbe1` (README-only patch, `git apply --check` exit 0, README sha256 `6d898bcc…` identical in the generating and a fresh clone, column-2 patterns 169→172); the rows move `unindexed` 1→0 and touch no other class, and the measured order is content files → rows → E04+E05 → refresh (no `--carry`, exit 0, 9/9) → commit baseline → gates — with four load-bearing findings for the L1 (the plan's wrong token names, the instrument-cap arithmetic, the missing `MANIFEST.sha256`, and the one-rows-patch-only rule).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline.baseline-snapshot.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/refresh-corpus-baseline.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline-runbook.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline/
