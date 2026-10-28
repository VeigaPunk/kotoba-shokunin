# Kb80E03IndexBaseline — C1 repair 3: coverage rows + baseline refresh

Seat: `Kb80E03IndexBaseline` (executor, leaf). Date: 2026-10-27.
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`; base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
Scratch: `/fast/scratch/hyaku/kotoba-r80/Kb80E03IndexBaseline` (eight clones), removed after receipts were copied.

Item: the coverage-map rows that close the corpus index gap and the re-recordable corpus baseline — plan §C1 repair 3.

## Deliverables (all under `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/`)

| file | sha256 | bytes | what it is |
|---|---|---|---|
| `Kb80E03IndexBaseline.patch` | `54e43309e05af3f98d23b030f811d9a729aa865b2dea6a9dc8dc778cf9d796f9` | 4818 | **the three `corpus/README.md` coverage-map rows** — README-only, 1 hunk, +3 lines, 0 deletions |
| `Kb80E03IndexBaseline.baseline-snapshot.patch` | `ec6c2ea4b3ad0b3d7dad661763bc6ca1f1f3ead7adb14d6350f7706f1a35b3bc` | 5110 | the re-recorded `verifiers/corpus-baseline.json` — **a PREVIEW under a scratch probe class, not landable** (see §4) |
| `refresh-corpus-baseline.py` | `8481be46ab6b74656fe7fa68c53300a5e490ee23265e69768d4dfeed770b470a` | 20188 | the r79 script copied **byte-for-byte verbatim** (unchanged) |
| `Kb80E03IndexBaseline-runbook.md` | — | 16.7 KB | the full runbook-order findings, world-by-world measurements, and F1–F6 |
| `Kb80E03IndexBaseline/` | — | 11 files | receipts: 4 worlds × 2 gates (JSON, own exit) + 3 refresh transcripts (own exit) |

## What the two corpus gates read (measured)

Both read **column 2 of every pipe-starting row between `## Coverage map` and the next `## ` heading**, backticked tokens only, fenced regions skipped — integrity `file_column_tokens` (`verifiers/verify_corpus_integrity.py:388-421`), independent `coverage_cells` (`verifiers/verify_corpus_independent.py:317-346`, independently written). One backticked corpus-relative path per row is the whole requirement. Measured on the patched README: **column-2 patterns 169 → 172**, new tokens exactly `(157, lessons/round-79-verifier-spotcheck.md)`, `(158, lessons/round-80.md)`, `(159, knowledge/allowed-tools-surfaces-round80.md)`.

Column 3 is scanned by the integrity gate for `.ufo/reports/round-<n>/*.md` pointers and `commit `<hex>`` citations: **all three rows carry 0 of each** (checked with the gates' own `UFO_POINTER_RE`/`COMMIT_RE`). The r79 E02 `..`-hop landmine was checked too: max hop depth **1** (cap 3).

## Measured worlds (each command's own exit status; no pipeline verdicts)

| world | contents | integrity | independent |
|---|---|---|---|
| base | base `398cbe1` | exit 1 — `tracked 152, unindexed 1, stale 0, missing 0, report_dead 1, commit_total 46, unresolvable 2` | exit 1 — `unindexed 1, report_dead 0, unresolvable 2` |
| **wA** | rows + the two new corpus files (current bytes), no instrument repair | exit 1 — `tracked 154, **unindexed 0**, stale 0, missing 0, report_dead 1, unresolvable 2` | exit 1 — `unindexed 0, stale 0, missing 0, report_dead 0, unresolvable 2` |
| **wA2** | **rows only**, corpus files absent | exit 1 — `unindexed 0` but **`stale 2`, `missing 2`** | exit 1 — same two classes red |
| **wB** | wA + E04 | exit 1 — `report_dead 0` (was 1), `unresolvable 2` still red | exit 1 — `unresolvable 2` still red |
| **wC** | wB + scratch-only probe grammar class | exit 1 on the three stale expectations only; **`unresolvable 0`** | **exit 0**, all PASS |

**`unindexed` 1 → 0.** The single unindexed file at base is `corpus/lessons/round-79-verifier-spotcheck.md`; row 1 closes it, rows 2–3 close the index gap for the round's two new files.

**The rows move no other class** (wA): `report_dead 1` and `unresolvable 2` stay red. Plan W3 confirmed — repairs 4 and 5 are load-bearing; the rows are not a substitute.

**The refresh refuses until repairs 4+5 land** (own exit status):
- wA: exit **2** — `refused: zero-mode corpus.pointers.report_dead observed 1, not 0; …`
- wB: exit **2** — `refused: zero-mode corpus.pointers.commit_unresolvable observed 2, not 0; …`
- wC: exit **0** — wrote the baseline; `post-refresh: 9/9 checks pass, exit 0`; `independent: exit 0`; `equal` expectations moved `tracked_files 144 → 154`, `report_total 99 → 109`, `commit_total 43 → 46`; **every zero-mode expectation stayed 0 and no `--carry` was used.**

## The order the L1 must run

1. Land the two new corpus files (`corpus/lessons/round-80.md` from `Kb80S01Lesson.md`; `corpus/knowledge/allowed-tools-surfaces-round80.md` from E08's file) and commit. **Rows before files = `stale 2` + `missing 2`** (wA2).
2. Apply **one** rows patch and commit.
3. Apply E04 and E05 and commit. Until E05 lands, `commit_unresolvable` is 2 and the refresh refuses.
4. `python3 -B .ufo/waves/round-80/build/refresh-corpus-baseline.py --repo .` from the lane toplevel, clean tree → exit 0, no `--carry`.
5. Commit `verifiers/corpus-baseline.json` alone.
6. Re-run both corpus gates (exit 0 each) and the tip battery in both `--repo .` and absolute forms.

Full detail, including the script's own preconditions (all verified), is in `Kb80E03IndexBaseline-runbook.md`.

## Findings for the L1

**F1 — the plan names the wrong failing tokens.** The plan's Trigger names `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`; **measured**, the two `commit_unresolvable` subjects are `corpus/SOURCES.md:171` and `:172` and **both are the same hash** `7bb48f213ac677f943d5c791199ed3dddf302f00`. The plan's two hexes are in the gates' `commit_quoted` class (6 entries) — already excluded. A sweep of every `commit `<token>`` in the base corpus (55 harvested) finds **zero** `owner/repo@<hex>` tokens; the third-repo NAME is a *separate backticked token on the same line*, and the second row names the repo only in the row title/URL. **A class keyed on the in-token grammar clears nothing**; the plan's "*(or otherwise an explicit third-repository citation)*" clause must work at **line scope**. (Independently confirmed by `Kb80L01Grammar` and `Kb80V03Instruments`; messaged to `Kb80E14C1Worlds`, `Kb80E04DeadPointer`.)

**F2 — a third instance appeared mid-wave and was closed.** An earlier build of E08's entry carried a full-hex `commit `7bb48f21…`` citation, which **would** have made `commit_unresolvable` **3** the moment it landed (measured in my first wA build: detail `corpus/knowledge/allowed-tools-surfaces-round80.md:95`). E08 has since revised the file — current bytes (sha256 `037c3b61…`, 24,726 B) carry **0 commit-shaped tokens and 0 report pointers**, and no `7bb48f`/`bb65e3e4`. All my published receipts were re-measured against the current bytes. The hazard is real for any future revision: a documentary entry citing a third-repo digest in the `commit `<hex>`` form adds a corpus-gate red the moment it lands.

**F3 — the instrument-size cap arithmetic is tighter than the plan's words.** The counter's `instrument-size` guard diffs the six battery scripts against its **pinned r72 base `072048fa`**, not `398cbe1`. At base: `check_assertion_floors.py` **+22/−3**, the other five **+0** → 22 added. E04 adds **+17** → 39. Under the amended `LINE_CAP` 60, the grammar class has **21 added lines to spend across BOTH gates** — very tight for a class whose self-test arms live in the two gates' own bytes. The plan's arithmetic (22 + 17 + ≤21 = 60) is right but infeasible as scoped; E06's `LINE_CAP` amendment and E05's class shape must be reconciled and the reconciliation declared. The E04 blob id to pin: `051b8c5f8676cba5c8d6047c8c9f7fcb56cd8f9f` (measured; matches the published `Kb80E04DeadPointer.blob`).

**F3b — E06's provisional counter does not yet pin the E04 blob (so it would fail `instrument-pin` at the tip).** `build/Kb80E06CounterErratum.cap60-provisional.py` still carries only the two old `verify_corpus_integrity.py` pins (`71cb2730…`, `e470eaae…`); the E04 blob `051b8c5f…` is absent, and E05's two blobs are not yet published. The `instrument-pin` guard requires every one of the six scripts at the measured rev to be byte-identical to the base blob or to a pin, so with E04 landed and that table as-is the guard fails. **Owned and closed by E06** (confirmed): the provisional file is explicitly cap-only, and the final `Kb80E06CounterErratum.patch` will carry the pins — the `verify_corpus_integrity.py` row gains **both** `051b8c5f…` (E04-only) **and** the E04∘E05 composed blob (the guard's test is `blob not in allowed` over a tuple, so a row may hold several allowed blobs — this makes the pin set hold for either stack and removes the integration-order hazard), and the `verify_corpus_independent.py` row gains E05's blob. Composition order stated as **E04 first, then E05** (the plan's repair numbering), with the reverse order measured. The other four instruments are unchanged by every published r80 artifact and are already pinned. Messaged E06 and Main.

**F4 — `MANIFEST.sha256` is absent where the rows and the counter look for it.** `.ufo/waves/round-79/snapshots/` holds six snapshots, six `.fetch.json` and six per-page `.manifest` fragments — **no `MANIFEST.sha256`** (measured absent; the round-80 snapshots dir does not exist). S08's row 3 and the C2 counter's snapshot-pin conjunct (c) both name that path. **Not mine to repair** (corpus/ is out of my write scope; the counter is E07's) — but the L1 must close it or the C2 counter's conjunct (c) fails at the tip.

**F5 — apply ONE rows patch, not two.** `Kb80S08ReadmeRows.patch` (sibling) adds **the same three rows** plus a `## Frontier` note hunk; the three row lines are **byte-identical** to mine (the patched coverage-map sections are identical, 152 rows each). Applying S08's and then mine **fails**: `error: corpus/README.md: patch does not apply`, exit 1. README sha256 after S08's patch `9db6cc91a6942679c45d118896ee4780563da859b43defcac65b6935355d75a1`; after my rows-only patch `6d898bcc710993253529477cd88df1ca09dc2eaeefd3c4f8306bc61a5fed0d3b` (they differ only by S08's Frontier note). **S08's patch is the superset and is the one to apply**; mine is the repair-3 executor's own artifact and the byte-level proof of the index delta. My patch applies clean on base (`git apply --check` exit 0) and produces a README byte-identical to the generating clone (sha256 `6d898bcc…`).

**F6 — the rows' `..` hops are inside the governance bound** (max depth 1, cap 3); the four-hop r79 landmine string appears nowhere in the rows.

## What I did NOT do

- **No lane file edited.** The lane's `corpus/README.md` is unchanged on disk; the rows exist only as a patch. No git mutation in the lane (read-only `git log/ls-tree/rev-parse/cat-file/show` only), no `jj` command.
- Nothing written to `corpus/`, `verifiers/`, `SKILL.md`, `PROVINCE.md`, `MANIFEST.json`, `SCORECARD.md`, `LOG.md`, `templates/`, `scripts/`, `.ufo/state/`, `plans/`.
- **No claim after-value scored**: no tip-battery run, no `check_allowed_tools.py` run, no SCORECARD row. The tip battery is the L1's post-integration measurement.
- Did not author E01–E06 or the C2 entry. The grammar class in wC is a **scratch-only probe** — it lives only in the scratch clone and is **not** published as a patch; wC is cited as evidence that the refresh is *reachable*, not as a proposal.
- `refresh-corpus-baseline.py` is unmodified (published copy byte-identical to the r79 original).
- No tool install or upgrade (none needed); **pacman untouched**; no host service restarted; ≤4 concurrent processes; scratch removed after receipts were copied (checked by absence).

## Limits

- The §4 baseline preview was measured under the probe class, not E05's bytes: `measured_against.head_subject` is `PROBE external class` and `head` carries the detached-measurement-commit label. **The L1 must re-derive it** at the real tip (runbook step 4); the three moved expectations (`154 / 109 / 46`) are the numbers to expect.
- wA's two corpus files are the sibling drafts copied into the scratch clone as fixtures; the real bodies may move `report_total`/`commit_total` slightly — re-derive.
- `unindexed 1 → 0` is measured from the gates' own `--json` observations on committed bytes, not inferred from the row text.

VERDICT: The three coverage rows land cleanly on base `398cbe1` (README-only patch, `git apply --check` exit 0, README sha256 `6d898bcc…` reproduced in a fresh clone, column-2 patterns 169→172); they move `unindexed` 1→0 and touch no other class, and the measured integration order is content files → rows → E04+E05 → refresh (no `--carry`, exit 0, 9/9) → commit baseline → gates — with four load-bearing findings for the L1 (the plan's wrong token names, the instrument-cap arithmetic, the missing `MANIFEST.sha256`, and the one-rows-patch-only rule).
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline.baseline-snapshot.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/refresh-corpus-baseline.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline-runbook.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E03IndexBaseline/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E03IndexBaseline.md
