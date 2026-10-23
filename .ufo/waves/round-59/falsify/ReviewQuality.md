Result: HOLDS — Q49–Q51 at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` match the Q45–Q48 format, each criterion is checkable, the M79–M81 lesson pointers resolve, and the able-to-fail evidence for all three is real; no criterion violation found this round so far, with three low-severity notes and two pending items for the L1.

Scope: review of `corpus/QUALITY.md` rows Q49–Q51 (lines 60–62) at `c63ccc68…` (sandbox clone `/fast/scratch/hyaku/kotoba-r59/ReviewQuality` at `c63ccc68…`; lane read-only). No tools installed or updated (python3/git/timeout already present).

# 1. Format matches Q45–Q48 — HOLDS

Q49–Q51 share the Q45–Q48 shape: 5 columns (`id | criterion | applies to | grounded in | supersedes`), one row per criterion, closing `| — |` supersedes cell, inline backtick term references, and evidence pointers in the grounded-in cell (`QUALITY.md:56-62`). Difference is content-only: Q49–Q51 grounded-in cells carry the qualifier "(§ Mistakes, draft)" (see §4, note 2).

# 2. Each criterion is checkable — HOLDS

- Q49 (`QUALITY.md:60`): observables = every seat's declared `Report:` path (dispatch specs + report trailers), the recorded final misroot sweep, seat accounting, and the commit/removal disposition of sweep-found reports. Decidable at round end.
- Q50 (`QUALITY.md:61`): observables = committed receipt naming the exact revision + observed result, per gate result stated for the tip. Decidable.
- Q51 (`QUALITY.md:62`): observables = counter code bytes read at the measured revision vs the credits in the report, and named non-author seats with committed review citations. Decidable.

Soft spots (not failures): Q49 does not enumerate the set of "seat-writable directories" nor define "settles"; the round-58 sweep used `git status --porcelain` and missed an existing fleet-root report, so the round-59 sweep must be specified to cover the fleet-root wave dir explicitly (see §4 note 4).

# 3. Lesson pointers resolve — HOLDS

- Q49 → M79 `misrooted-seat-report-and-premature-sweep`: `corpus/lessons/round-59.md:41` ✓
- Q50 → M80 `tip-receipt-asserted-not-committed`: `corpus/lessons/round-59.md:43` ✓
- Q51 → M81 `counter-blind-fields-and-ua-sensitive-fetch`: `corpus/lessons/round-59.md:45` ✓

Each entry is present at `c63ccc68…` with the exact class name the row cites; each cites the round-58 spot-check evidence, now verified to resolve (`round-58-verifier-spotcheck.md:243-252` R1, `:253-257` R2, `:258-262` R3, `:96-104` field-judgment seats; `ScoutMisroot.md:5-46` and `:3-27` both resolve; `ReviewBudgetMove.provenance.md:3-10`; `noharm-tip.txt:1-8,38-39` at `46b4a706`; `C1-remeasure-tip.txt:1-25` at `6de8e2eb` recording the checklist FAIL at line 24; frozen source `check_command_files.py:762-783` reads `sr[1]` token and `sr[3]` action, never the field cell).

# 4. Able-to-fail evidence is real — HOLDS

- M79: ran `timeout 5 ls /home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` → exit 0, stdout `/home/vgpnk/Projects/shokunin/.ufo/waves/round-58/falsify/ReviewBudgetMove.md` (10,299 B, mtime 05:34). The misroot file exists; the lane copy is committed byte-exact with provenance (`ReviewBudgetMove.provenance.md:3-10`; `cmp` exit 0; sha256 `c288bbd8427b38cda487b6693fe3a3774a674d9dcff944dd7f27fa7d9295cb8d`).
- M80: ran `timeout 10 git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin ls-tree -r --name-only ed44e0c4807b92d99417eaff04a0fd2122f981b4 -- .ufo/waves/round-58 | grep -E 'verify_skill_checklist|checklist.*tip'` → exit 1, no output (no matching committed receipt at `ed44e0c4`).
- M81: the mutant (f) run is recorded at `MutC1Content.md:146-161` (sandbox commit `b8e7d8aa99cb903d1b89d5b82696b2db3a337d9b` at `/fast/scratch/hyaku/kotoba-r58/MutC1Content`, labelled), stdout verbatim `custom command files found on the live page 6 of 6; new ground 4`, exit 0; `ReopenS094.md:46-48` records the urllib 403/curl 200 window and G-floor; `round-58-verifier-spotcheck.md:96-104` names the seats that judged the field cells. ScribeMistakes disclosed honestly which runs it repeated (`ScribeMistakes.md:1-27`: M79 fleet-root sweep count and M81 rerun not run by the scribe; M79 `ls`, M80, M82, M83 run read-only).

# 5. Findings (by severity)

1. LOW — Q50 tip-revision is conditional on the final report's wording. `C1-measure.txt` is committed (present in tree at `d64d945b…`, absent at `c63ccc68…`; `git ls-tree` at `d64d945b…` lists it, at `c63ccc68…` does not) and names exactly `rev: c63ccc6823e1f6a8577acbb43d19551eadbbee9a` with the observed result lines and `exit: 0` + `C1 predicate: --fetch exit 0 (F>=TARGET, G>=NEW_TARGET) — MET` (lines 1-12). This satisfies Q50 for a result stated at `c63ccc68` (the claim's revision). If the round report instead asserts the gate "at the lane tip `d64d945b`", a `d64d945b`-naming committed receipt is required (exactly the R2 shape).
2. LOW — Stale "draft" qualifier in the grounded-in cells of Q49–Q51 ("`corpus/lessons/round-59.md` § Mistakes, draft"): at `c63ccc68…` the lesson is committed and M79–M81 are final (checked by the L1 per `round-59.md:38-39`); the qualifier reflects ScribeQuality's drafting-time state (`ScribeQuality.md:7,23`). Cosmetic; would read better as "(§ Mistakes)".
3. LOW — Supersedes cells dropped vs the draft. `ScribeQuality.md` proposed supersedes Q40/Q36/Q31 (lines 5, 13-14: "| Q36 |", "| Q31 |"); the integrated rows carry `| — |` (`QUALITY.md:60-62`). This is consistent with the table policy (supersedes only records a criterion that failed its own spot-check, `QUALITY.md:64-66`), but Q49≈Q40, Q50≈Q36, Q51≈Q31 are near-duplicates left unlinked — maintainability risk of drift/double standards.
4. PENDING (round-end) — Q49 evidence not yet recorded: no final misroot sweep exists yet (the falsify wave is mid-flight; `git status --porcelain` shows only `?? .ufo/waves/round-59/falsify-taskcall-sent.json` and `?? .ufo/waves/round-59/falsify/`). The L1 must run and commit the sweep after the last seat settles, covering the fleet-root wave dir (the round-58 sweep missed an existing fleet-root file).
5. PENDING (round-end) — Q51 evidence not yet recorded: the plan names the non-author seats (`plans/round-59.md:93-98`: falsify seats `Cells<Client>`, one per client) and the entry's § Not held scope boundary (`hook-files-round59.md:66-71`); their committed reviews must land before the round report so Q51's "committed review cited" holds. No report so far credits the counter with checks its code does not read (checked `w0/ExecC1Counter.md` conjunct table and `C1-measure.txt`).

# 6. Residual risk / verification gaps

- The round-58 misroot sweep's mechanism (`git status --porcelain` on the fleet root) did not enumerate the fleet-root wave dir; whether the round-59 sweep will is unverifiable until it runs (Q49's coverage clause).
- No round-59 tip-named gate receipt exists yet that names `d64d945b`; watch the final report's revision claims (Q50).
- The C1 receipt's count lines (reject opencode alongside "6 of 6 found") were not reconciled here — that is the C1-counter reviewers' domain, not a QUALITY row defect.

Evidence pointers: `corpus/QUALITY.md:56-62`; `corpus/lessons/round-59.md:38-45`; `corpus/lessons/round-58-verifier-spotcheck.md:96-104,243-266`; `.ufo/waves/round-58/falsify/ScoutMisroot.md:3-46`; `.ufo/waves/round-58/falsify/ReviewBudgetMove.provenance.md:3-10`; `.ufo/waves/round-58/falsify/MutC1Content.md:146-161`; `.ufo/waves/round-58/falsify/ReopenS094.md:46-48`; `.ufo/waves/round-58/noharm-tip.txt:1-8,38-39`; `.ufo/waves/round-58/C1-remeasure-tip.txt:1-25`; `.ufo/waves/round-58/w0/check_command_files.py:762-783`; `.ufo/waves/round-59/C1-measure.txt:1-18`; `.ufo/waves/round-59/build/ScribeQuality.md:5-23`; `.ufo/waves/round-59/build/ScribeMistakes.md:1-27`; `.ufo/waves/round-59/bounds.md:3`; `plans/round-59.md:13-17,56-98`.

Report: .ufo/waves/round-59/falsify/ReviewQuality.md
