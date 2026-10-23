Result: MIXED — every Q46–Q48 able-to-fail falsifier reproduces (fails on `3de87aad`, passes on `46b4a706`) and Q47 reflects rather than contradicts the CtlC2SourceGrep finding, but M70's `fix:` sentence — cited in Q46's grounding — still claims a `probe` relabel that never landed, and Q47's remedy clause under-scopes the finding it cites.

# Scope

Attacks Q46–Q48 in `corpus/QUALITY.md:57-59` at `46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`.
Sandbox: `/fast/scratch/hyaku/kotoba-r58/KotobaR58.ReviewQuality`, lane clone checked out at
`46b4a706` (re-checkout `3de87aad` → `46b4a706` during runs; no sandbox commits made).
All lane reads via `git --no-optional-locks show`; all executions in the sandbox only, TMPDIR pinned
under it, every run ≤ 900 s.

# Finding (LOW): M70 `fix:` sentence is stale — cited by Q46's grounded-in cell

`corpus/lessons/round-58.md:49` at `46b4a706` reads:

> fix: round 58 relabels the `SKILL.md` gate-registry row as `probe` and records the withdrawal
> reason (`plans/round-58.md:13`)

The landed `SKILL.md:457` row keeps kind `gate` and appends in-cell
`— claim withdrawn r57; not a claim gate until redesigned and re-controlled`; `SKILL.md:465` carries
the r58 analogue. A `probe` relabel is impossible without script edits: `ExecR1Registry.md:51-55`
measured the plan's `probe` route at 30 of 32 (reasons `probe verdict map declares 1=failed`,
`probe script has an exact --self-test handler`), and my re-run
`TMPDIR=<sandbox>/.tmp timeout 900 python3 -B verifiers/check_gate_registry.py --rev 46b4a7061c688cefd3e3ec9cbb655130ba1aafbe`
→ `gate registry rows conformant 32 of 32 lane verifiers; phantom 0`, exit 0, confirms the annotation
is the conformant state. `ScribeQuality.md:80-88` flagged this reconciliation to the integrator; it
landed unreconciled. M77 correctly records the false premise — M70's fix text remained behind.
The Q46 criterion text itself is accurate and consistent with the landed state; only the cited
lesson sentence is false.

# Verified: Q46 — withdrawal annotation, able to fail

- `git show 3de87aad…:SKILL.md | grep -c 'claim withdrawn r5'` → `0`, exit 1.
- `git show 46b4a706…:SKILL.md | grep -c 'claim withdrawn r5'` → `2`, exit 0 — the r57
  (`check_infoless_fences.py`, :457) and r58 (`check_sweep_mutants.py`, :465) annotations.
- The draft falsifier also verifies: `grep -c 'check_infoless_fences.py.*claim withdrawn.*not a claim gate'`
  → 0 @ `3de87aad` (exit 1), 1 @ `46b4a706` (exit 0). Both annotations match the row's required
  form ("claim withdrawn" + "not a claim gate until redesigned and re-controlled").
- `ExecR1Registry` receipt exists at `46b4a706` (`git cat-file -e`); its 30-of-32 probe-measurement
  matches Q46's "`a probe` relabel scores 30 of 32" and Q46's premise ("`gate` kind alone reads as a
  live claim gate") matches the receipt's own risk note (`ExecR1Registry.md:155-157`).
- M70 and M77 exist in `lessons/round-58.md:49,69` at `46b4a706`. Grounding pointers resolve.

# Verified: Q47 — two-sided measure, non-fixed equivalents; reflects CtlC2SourceGrep

- `verifiers/check_sweep_mutants.py` sha256 `f7664401…` identical at `3de87aad` and `46b4a706`
  (matches the control receipts' recorded counter hash); the catalogue
  `.ufo/waves/round-58/sweep-mutants.json` sha `cf2fa97a…` is identical at both revisions and is a
  published list of 16 entries (11 `mutant` + 5 `equivalent`) — the "fixed published list" Q47
  grounds on is factual.
- Re-ran the counter in sandbox:
  - `TMPDIR=<sandbox>/.tmp/sweep-old timeout 900 python3 -B verifiers/check_sweep_mutants.py --rev 3de87aad…`
    → `sweep mutants killed 4 of 11; equivalents survived 5 of 5`, exit 1 — byte-identical to
    `CtlC2SourceGrep.md:118-135`.
  - `… --rev 46b4a706…` → `sweep mutants killed 11 of 11; equivalents survived 5 of 5`, exit 0 —
    the R3 record, consistent with the row's "stays a record, never a claim" disposition (registry
    row `SKILL.md:465` marks it withdrawn).
- Cited receipts re-read at `46b4a706`: `CtlC2Snapshot.md` Result HOLDS, K=11/E=0 exit 1 (the
  two-sided half rejects a snapshot-only self-test); `CtlC2SourceGrep.md` Result BREAKS, K=11/E=5
  exit 0 (the fixed-list keying beats the predicate). Both match the row's parenthetical numbers.
- **Contradiction check: REFLECTS, does not contradict.** Q47's clause "a fixed list is a label a
  self-test can key on, so the set is generated at measurement time or the measure stays a record,
  never a claim" is exactly the CtlC2SourceGrep mechanism (M75 `fixed-equivalent-set-is-a-label`,
  `lessons/round-58.md:57-63`) and its disposition is the one taken (erratum 1: record-only
  annotation). The row grounds both controls and numbers them accurately.
- **Residual (below):** the criterion's remedy names only the *equivalent* list; the actual
  shortcut keyed on the eleven published *mutant* `old` texts, canonicalising the two equivalent
  regex spellings for the survive side (`CtlC2SourceGrep.md:9-13`). See residual risk.

# Verified: Q48 — successful `main()` path, able to fail

- `verifiers/check_plugin_manifests.py` sha `bf11a4ef…` @ `3de87aad` → `7cefb997…` @ `46b4a706`;
  both match `ExecR4PluginMain.md:11-14` byte-for-byte.
- Old state: at `3de87aad`, the only `main(` call sites are `:1126` `main(["--rev","not-a-hash"])`
  (invalid rev, returns before measurement) and the `sys.exit(main())` tail — "no exit-0 `main()`
  call" is literal. `TMPDIR=<sandbox>/.tmp timeout 900 python3 -B verifiers/check_plugin_manifests.py
  --self-test` @ `3de87aad` → `0 failure(s) over 235 assertions`, exit 0 — the defect is invisible
  to the old self-test (criterion fails on the old state: satisfied).
- New state: @ `46b4a706`, `--self-test` → `0 failure(s) over 239 assertions`, exit 0; arm at
  `verifiers/check_plugin_manifests.py:1771-1854` asserts exit 0 + exact line
  `plugin manifests found on the live page 2 of 2; new ground 2` and a broken-conjunct exit 1 +
  `1 of 2; new ground 1` — both conjuncts of the criterion present.
- Mutant repro (arm target `2 → 3` at `:1826`, applied in my sandbox worktree only, reverted):
  `--self-test` → `FAIL R4: the satisfying world exits 0: got 1, expected 0`,
  `self-test: 1 failure(s) over 239 assertions`, exit 1 — byte-matches `ExecR4PluginMain.md:75-76`
  ("raising the fixture target 2→3 fails the exit-0 arm").
- `verifiers/check_command_files.py` sha `aae12d36…` identical at both revisions; arm present at
  `:1805-1863` (`main(["--rev", measured, "--fetch"])`, exit-0 + exact-line + broken-world arms);
  `--self-test` → `0 failure(s) over 244 assertions`, exit 0 (244 = the ScribeQuality run's base).
  File is absent at base `f56f6e19` (`git cat-file -e` → "exists on disk, but not in f56f6e19…")
  and first appears at `3de87aad` — "carries the arm from birth" is accurate.
- QUALITY itself: Q45 is the last row at `3de87aad` (`git show …:corpus/QUALITY.md | grep -n Q4[5-8]`
  → only line 56) — Q46–Q48 are new at `46b4a706`, `supersedes` `—` correct.

# Residual risk

- **Q47 scope gap (informational, not a defect of the row's evidence):** CtlC2SourceGrep's shortcut
  keys on the published *mutant* texts and merely tolerates the two equivalent rewrites; a
  measurement-time-generated equivalent set that preserves the eleven mutant `old` substrings would
  still leave that shortcut open. "Generated at measurement time" is a necessary but not sufficient
  condition for killing the named shortcut class. The row's own grounding (M75 + redesign pointer
  `build/CriticC2Redesign.md`, which specifies generated equivalents and parent-owned counts) is
  where sufficiency must live; the criterion text alone does not guarantee it.
- The Q46 evidence line says "2 after the round-58 fix" without naming the second annotated row;
  verified the second hit is the `check_sweep_mutants.py` row, not an accidental match.

# Verification gaps / bounds

- I did not re-run `check_plugin_manifests.py --rev … --fetch` (network; receipt #4 of
  `ExecR4PluginMain.md` already records it unchanged) and did not rebuild the CtlC2 worlds — both
  controls' committed receipts were re-read, and the counter's pristine/base runs were re-executed
  byte-identically.
- No tools installed or upgraded; no sandbox commits; no lane writes besides this report.
