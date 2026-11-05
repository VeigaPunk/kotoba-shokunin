# ScribeIndexR87 — round 87 w3 (milestone r87-w3): re-verification, attack, D5 drift, evidence index

Lane `master` at measurement: `d1c031833c37af99196f72f84a6643f84eec129a` (2026-11-05 00:09:30 -0300, "round-87 attempt 2 …").
The brief's tip `760e1c5edfdefb4767420f711d08f669952de013` is an ancestor. Every frozen surface is byte-identical at both
(blob ids at d1c0318: `check_omp_root_semantics.py` 48ec1f2, `omp-skill-roots-semantics.tsv` ae27cb7,
`check_r86_routed_repairs.py` f30e9b3, `verify_corpus_integrity.py` bbee51f, `plans/round-87.md` 9b7e642,
addenda 30eaa26 / 8aa5fbb). Commit d1c0318 changed `LOG.md`, `SCORECARD.md`, `corpus/QUALITY.md`,
`corpus/lessons/round-87.md` and wave-w3 seat files only. The omp ELF sha256 is `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` (matches the pin).

Snapshot caveat: the lane tree is live (peer seats write under `w3/`; the tip moved once during this wave). All numbers are for d1c0318.

## 1. Frozen counters at the tip (lane worktree, read-only runs)

| claim | command | reading | exit |
|---|---|---|---|
| C1 depth | `python3 -B verifiers/check_omp_root_semantics.py --rev d1c0318…` | `omp root semantics grounded 12 of 12`; S1, S2, S3 PASS | 0 |
| C2 consistency | `python3 -B verifiers/check_r86_routed_repairs.py --rev d1c0318…` | D1 PASS, D2 PASS, D3 PASS (5 reject rows, longest 52 words), D4 PASS, **D5 FAIL** (red set `['corpus.pointers.commit_unresolvable']`, want `['…commit_unresolvable', '…report_dead']`); `r86 routed defects closed 4 of 5` | 1 |

- C1 base `223ae62` (scratch clone): `omp root semantics grounded 0 of 12`, exit 1 (S3 FAIL, ledger absent).
- Self-tests (in scratch clone): C1 `0 failure(s) over 35 assertions`, exit 0; C2 `0 failure(s) over 53 assertions`, exit 0.
- At 760e1c5 (observed this wave, no file): C1 12/12 exit 0; C2 4/5 exit 1 with the same D5 failure.
- Receipts: `w3/ScribeIndexR87/receipts/c1-d1c0318.txt`, `c2-d1c0318.txt`, `st-c1.txt`, `st-c2.txt`, `c1-tip-run.txt` (the 760e1c5 C1 run).

Re-verification verdict: **C1 holds at the tip. C2 reads 4 of 5 at the tip, as the lane records.**

## 2. C1 — independent re-implementation and mutant worlds

`w3/ScribeIndexR87/scripts/c1_indep.py` re-derives the four conjuncts from the frozen predicate text (exact newline-delimited ELF lines, header-before-quote ordering, pattern rules, `..` refusal). Its row verdicts match the counter's `row N GROUND/FAIL` lines in every world below (108 row verdicts; the one "difference" is W4's absent row 12, which is not a verdict).

Worlds were committed to a scratch clone branch (`c1-worlds`) and scored with the frozen counter at each world commit.

| world (semantics ledger change only) | counter | independent | reading |
|---|---|---|---|
| W0 honest tip | 12/12 exit 0 | 12/12 | sanity |
| W1 do-nothing: binary quote as reader | 0/12 exit 1 | 0/12 | refused |
| W2 doc quote as row-1 reader | 11/12 exit 1 | 11/12 | refused (`w_docquote` class) |
| W3 row-1 module not in ELF | 11/12 exit 1 | 11/12 | refused |
| W4 eleven rows | 11/12 exit 1 (S3 FAIL) | 11/12 | refused |
| W8 `{cwd}/../` pattern | 11/12 exit 1 (S3 FAIL) | 11/12 | refused |
| **W5 all 12 modules = `coding-agent/src/discovery/helpers.ts`** | **12/12 exit 0** | 12/12 | **accepted** |
| **W6 plugin row's reader = codex join line, module codex.ts** | **12/12 exit 0** | 12/12 | **accepted** |
| **W7 one codex join line serves all 12 roots** | **12/12 exit 0** | 12/12 | **accepted** |

The frozen predicate, as written, accepts W5–W7. The counter does what the predicate says; the predicate is weak:

- **F-C1-1 (predicate gap, module).** Conjunct 3 requires only that *some* `// packages/<m>` header occurs and that the reader's first offset lies after that header's last occurrence. The ELF holds 2,895 distinct package headers; `helpers.ts`'s header precedes every reader, so any module that sits earlier passes. The module cell is not bound to the reader.
- **F-C1-2 (predicate gap, reader↔root).** Nothing binds a row's reader quote to its pattern. W7 grounds all twelve roots from one line; W6 grounds the plugin root from the codex reader. "Grounded per root" is not what is measured.
- **F-C1-3 (predicate gap, join test).** Conjunct 2 requires a join token on the quote's line. All 12 real reader quotes contain `join(` in their own text (`fr.join(`, `Fr.join(`, `Rs.join(`, `Xr.join(`, `d.join(`, `Zo.join(`, `Zm.join(`), so the test is satisfied by the quote itself and cannot separate code from a string literal that contains `join(`.
- **F-C1-4 (implementation defect, latent).** `elf_line()` (`check_omp_root_semantics.py:143-149`) falls back to `blob[0:…]` / `blob[…:size]` when no newline lies within 8 KiB on a side, although its docstring says "bounded". Measured in-process on synthetic blobs through the counter's own `score()` (`scripts/c1_fallback2.py`): a neutral code quote on a 40 KB newline-free line, with `join(` only on an earlier line, reads **row 1 GROUND** (exact line has no join); a doc-string quote in the same setting also reads **GROUND**. The pinned ELF is not affected today: the 12 real quotes' counter line equals the exact line, and the two doc-string occurrences sit on lines of 3,470 and 58 bytes. Latent only, and it cannot be exploited on the pinned binary without changing the binary.
- **F-C1-5 (guard).** `guards = {"S1": True, "S3": True}` is never set False, so S1 cannot fail. The base run prints `guard S1 ledger-from-rev PASS (… rc=absent)`: the PASS line contradicts its own `rc=absent`.
- **F-C1-6 (bound).** Conjunct 4 tests a fixed synthetic chain (`/home/u/proj/sub`), not the session's real cwd. That is what the predicate says; it means conjunct 4 cannot catch a real `{cwd}` expansion problem.

Disposition under the kill rule: these are findings for the next round. Nothing was edited.

## 3. C2 — the D5 drift, measured

D5(iii) is an exact-set predicate over the corpus gate's red checks, with details that must name the two disclosed sites. The fleet pointer `.ufo/reports/round-84/kama.md` is resolved by the gate's bare-path fallback to the fleet root; once it exists with `## SHONEN` (10,856 bytes, present), `report_dead` heals.

To isolate the variable, the lane's own gate source was executed in memory with one line redirected (`target = fleet_root / token` → a fixture report root that is a symlink mirror of the fleet's `.ufo/reports` minus `round-84/kama.md`). Nothing was written into the lane.

| state | bytes | fleet `kama.md` | D5 verdict | tally | red checks / details |
|---|---|---|---|---|---|
| lane, as is (d1c0318) | lane | present | **FAIL** (frozen counter, live) | 8/9 | `commit_unresolvable` only; report_dead detail `[]` |
| lane, same bytes | lane | removed (fixture root) | PASS (replica of frozen `check_d5`) | 7/9 | `report_dead` ×3 (round-86 spotcheck:33, round-87.md:61, :86) + `commit_unresolvable` |
| clone (`git clone --shared`), as is | clone | present | **FAIL** (frozen `check_d5`, in-process) | 7/9 | `report_dead` at `round-81.md:29` (dangling round-76 symlink, relative `../../../../`) + `commit_unresolvable` |
| clone, same bytes | clone | removed | **PASS** (frozen `check_d5`, in-process) | 7/9 | `report_dead` ×4 incl. undisclosed `round-81.md:29`, `round-87.md:61`, `:86` |

Files: `receipts/gate-P.json`, `gate-A.json`, `gate-clone-P.json`, `gate-clone-A.json`, `scripts/d5_inproc.py`, `scripts/gate_runner.py`, `scripts/d5_eval.py`.

Findings:

- **F-C2-1 (the drift).** Identical lane bytes read FAIL with the fleet file present and PASS with it absent. The predicate rewards the state in which a fleet pointer is broken and fails the state in which it is repaired. The lane's own "4 of 5 at the tip" is the honest reading of today's bytes; it is not a lane defect.
- **F-C2-2 (timestamp misattribution in the lesson).** `corpus/lessons/round-87.md` (Attempt 2) says the kama report "landed on the fleet repo at 22:47 (fleet commit `5b052020`)". Measured: commit `5b052020` is authored 12:15:30 and committed 12:16:01 (-0300) and is an ancestor of fleet HEAD `b72ce052`. The 22:47 time is the on-disk file: `round-84/kama.md` mtime 2026-11-04 22:47:40.415 and the directory's mtime is the same instant (a directory entry appeared). The file's content matches the tracked blob. The drift is a working-tree state change with no new commit. The fleet reflog shows `export from jj` entries 23:09–23:51, so the fleet working copy is being rewritten underneath the lane.
- **F-C2-3 (disclosure gap, already in the round's own receipts).** `receipts/after-battery.txt` (measured at ff4bf3f, 21:14) lists `report_dead` three times, all for kama: `corpus/lessons/round-86-verifier-spotcheck.md:33`, `corpus/lessons/round-87.md:61` and `:86`. The lesson's D5 disclosure names only the `:33` site, and `receipts/c2-final.txt` says "red exactly the two disclosed DRIFTs". That sentence is true only because the frozen check is `any(line.startswith(site))`: it never tests that every red detail is disclosed. In state A the round's own lesson lines 61 and 86 remain red and undisclosed.
- **F-C2-4 (any-check).** `check_d5` (`check_r86_routed_repairs.py`, D5(iii)) accepts an unnamed extra red detail as long as the two named sites are present. The clone-A row above passes the frozen check with `round-81.md:29` undisclosed.

Diagnostic only (not the frozen predicate, not a proposal to edit it; the r88 routing belongs to the lane): a monotone check "red ⊆ {report_dead, commit_unresolvable} and every red detail names a disclosed site" passes the lane-as-is state and fails the lane-same-bytes state, because of lesson lines 61/86. So the routed r88 repair (red ⊆ disclosed set) must also disclose or repair those two lesson citations, or the honest carry is still not honest under the detail test.

## 4. Evidence index (`INDEX.md`)

`w3/ScribeIndexR87/INDEX.md` (generated from disk by `scripts/assemble.py`): 129 files in the round-87 tree at the snapshot; section 1 lists each with size, tracked flag, first line, revisions named and commands recorded; section 2 gives heading line numbers for the lesson, the plan and both addenda; section 3 gives the LOG (3298–3372) and SCORECARD (601–648) round-87 blocks and resolves every hash; section 4 is the missing-evidence list.

Closing line: `index: 129 files, 155 resolved pointers, 5 dangling`.

Index findings:

- **F-IDX-1 (false premise, assimilation).** `plans/round-87.md:185–187` says `/home/vgpnk/Projects/shokuknow/merge/kotoba/` is absent on this host ("no such directory") and orders `Assimilation: none`. It exists: `MERGE-REPORT.json`, `MERGE-REPORT.md`, `SOURCES.append.md`, mtime 2026-10-24T23:33 (before round 87 began). The lesson contains no `Assimilation:` line at all.
- **F-IDX-2 (missing promised receipts).** `receipts/q73-sweep.txt` (plan, No-harm battery) does not exist; the sweep is a `q73_sweep` section inside `base-battery.txt`. `w1/Sentinel.md` (lesson:96, routed attack seat) does not exist. `.ufo/waves/round-87/w3/l1/census-now.txt` (LOG.md:3370) does not exist.
- **F-IDX-3 (no command provenance in receipts).** `c1-after.txt`, `c1-after-tip.txt`, `c2-after.txt`, `c2-final.txt`, `census-after.txt` name no command. The C2 PASS lines are transcripts; they are reproducible only through the counters, not from the file. The battery command lines live in `build-base-battery.sh` / `build-after-battery.sh`.
- **F-IDX-4 (historic lane write).** `receipts/d5-after-revert.txt` records `git checkout -- corpus/lessons/round-86-verifier-spotcheck.md corpus/lessons/round-81.md` run in the lane by the L1 during integration. Recorded, not repeated here.
- All LOG and SCORECARD round-87 hashes resolve in the lane or fleet, except `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1`, which is dangling by design and disclosed. Four `7d9f599`-family hashes are blobs, not commits, and resolve in the lane.

## 5. Files written

- `.ufo/waves/round-87/w3/ScribeIndexR87/INDEX.md`
- `.ufo/waves/round-87/w3/ScribeIndexR87/receipts/` (C1 tip and base runs, 9 world receipts + world map, C2 tip run, self-tests, D5 gate states, index scan and inventory JSON)
- `.ufo/waves/round-87/w3/ScribeIndexR87/scripts/` (independent C1 scorer, world builder, fallback fixture test, D5 in-process runner, index assembler and scanner)
- `.ufo/waves/round-87/w3/ScribeIndexR87.md` (this report)

Nothing under `verifiers/`, `plans/`, `corpus/SOURCES.md`, `corpus/QUALITY.md`, `LOG.md`, `SCORECARD.md` or `SKILL.md` was written. Scratch clone, world commits (branch `c1-worlds`, the `c1-worlds-revs.json` commits) and the gate patch exist only in the scratch clone, which is removed before yielding. Those world commits are not in the lane.

## 6. Tooling

No tool was installed or upgraded. `git` and system `python3` were used; no sudo, no pacman. `/home/vgpnk/.omp/agent/RULES.md` was read.

## 7. Risks

- The tip moved (760e1c5 → d1c0318) while this wave ran; any further lane commit changes the C2 reading only through the corpus, and C1 only through the frozen surfaces (which are unchanged).
- The C2 reading depends on a fleet file outside the lane (F-C2-1/2); a fleet jj re-export can flip D5 with no lane change.
- F-C1-1..3 mean C1's 12/12 is a weak signal: W5–W7 pass the frozen predicate. The round's C1 claim is correct as worded and under-powered as a depth measure.
- F-C1-4 is latent; it does not affect the pinned binary.
- F-C2-3/4: the round's D5 disclosure line "red exactly the two disclosed DRIFTs" is accurate only under the any-check.
- At the end of this wave the lane carries uncommitted peer edits: `corpus/lessons/round-87.md` (+34 lines, a "Wave r87-w3 findings" section), `SCORECARD.md` (+2) and `w3/l1/c2-base-clone.txt`. Not written or measured by this seat beyond re-running C2 at d1c0318 with them present: still `4 of 5`, exit 1 (D5 unchanged). The peer section's Assimilation correction agrees with F-IDX-1.
