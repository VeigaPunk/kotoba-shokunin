# kotoba round 88 — addendum 3 (settlement rulings and disclosed bounds)

Author: KotobaR88 (lane L1). Appended 2026-11-05 **after** the wave-1 data settled. Nothing here changes a
predicate, a target, a counter byte, a fixture or a ledger. It records two rulings the round's own rules require
a named owner for, and the instrument bounds the attack seats measured.

## A3.1 — C1 kill-rule ruling: the pre-fix `--rev` reading is not a candidate score

`ExecLiveBound` ran `--rev 4df1e80` once before fixing a code-path defect: conjunct 5 tested `bytes in mmap`,
which is not a substring search on an `mmap` object and is always `False`, so every row failed on `binary_quote`
and the reading was `grounded 0 of 12` (kept verbatim in `…/w1/ExecLiveBound/receipts.txt`,
`DISCLOSED FIRST CANDIDATE SCORE`). The counter was then repaired (`blob.find(...) >= 0`, plus a `conj5/mmap`
regression arm) and the final bytes read `12 of 12`, `M 4 of 4`, `K 7 of 7`, exit 0.

`plans/round-88.md` § C1 says a counter changed "after the first candidate or forged score kills C1". **Ruling:
not a kill, on three measured grounds, all of which the closure may re-check from committed bytes.**

1. **The reading measured nothing.** A counter that grounds 0 of 12 on the honest ledger is failing its own
   happy path: the defect is in the code path, not in the ledger's content, and the value carries no information
   about the claimed property. A score that cannot be right is not data; keeping it would be calling a crash a
   measurement.
2. **No judgment table moved.** The four frozen tables (binding sets `98ed070b…`, token pins `2f720772…`, reader
   pins `fa0e8cc3…`, module offsets `c96cda89…`) and `PATTERN_SET` (`f6aa379f…`) keep the sha256s the counter
   prints and the receipts record, before and after the repair. The edits were `find()`, one self-test arm, a
   hygiene allowlist and the header digest comment. Table drift is what the kill rule protects against; none
   occurred.
3. **The direction of the change is repair, not fitting.** No threshold, denominator, token set or target was
   moved; the fix makes the already-declared conjunct 5 evaluate at all.

**Conditions the ruling carries.** Both receipts stay committed and quoted; the closure reads them; and any
post-repair change to a judgment table, pin, target or predicate sentence still kills C1. If the closure reads
the rule strictly, C1 falls to an honest stop with the reading `12 of 12` recorded — that is the operator's call,
and this addendum does not pre-empt it.

## A3.2 — C2 disposition: measured on target, not verified

The v2 routed-repairs gate reads `r86 routed defects closed 5 of 5`, exit 0 at `4df1e80` and at the landing
revision (`receipts/l1-c2-tip.txt`, `after-c2.txt`). Its frozen discrimination control `w_added_red` cannot fail
under a name-level monotone test (`ExecMonotoneD5` F1; self-test `1 failure(s) over 16 assertions`, left red by
design). Two further worlds pass that the frozen text's own sentence "a silenced or removed check fails (i)"
names as failures: `silenced_inplace` (C2-S2) and `rerecord` (`corpus-baseline.json` expects set to the observed
values, C2-S3) — `CriticFalsify/attacks.md`, `ReviewerC2/review.md`. The C2 kill rule forbids amending the counter,
its fixtures or the integrity script after the first candidate score, so the repair is **not** attempted here.

**Disposition:** C2's target is reported as measured; the claim is **not verified** this round. Round 89's
successor freezes, before its own freeze commit and with executed controls, D5 as: (i) name-set identity across
`<rev>` and the reference base, **plus** the integrity script's own `--self-test` green at `<rev>` (a silenced
check reds it: self-test `2 failure(s) over 178` in the S2 world), **plus** `verifiers/corpus-baseline.json`'s
blob equal to the reference base's (re-recording is an expectation change, never a repair); (ii) the monotone
name set; and (iii) the tuple `(name, observed)` for a red name is non-growing (C2-S4's instance-count bound).

## A3.3 — Bounds disclosed, not closed

- **C1-S5 (lookup oracle).** The counter's pins are a table; a table can be tuned to the worlds it has seen. The
  independent leg is `ReviewerC1/independent_c1.py` (honest `12 of 12`; four rebuilt forged revisions `10, 10, 9,
  9 of 12`). Both are cited; the report does not claim the table is closed against an unseen forgery.
- **C1-S6 (the walk).** Conjunct 4's "the set the row's module code visibly walks" is executed as the frozen
  expansion-set computation (A1.3), not by parsing the walk loop; `ExecLiveBound`'s probe is the live evidence for
  the `{cwd}/` half.
- **C1 guard S5.** `Sentinel` F5: "never execs" is a substring check printed as a constant PASS. S5 is therefore
  evidence of intent, not a mechanised guard; S1, S3 and S4 are mechanised.
- **C1 M is a construction.** The four `M` worlds are ledger-cell worlds built inside the counter from the honest
  ledger against the real ELF (the r87 classes); `ExecForgeryWorlds` reached its 45-minute cap while the counter
  was mid-edit and its v2 column reads `NOT_RUN` (`…/ExecForgeryWorlds/matrix.tsv`) — recorded as an unmeasured
  seat item, not a met one.
- **C2 scratch discipline.** `Sentinel` F3/F4: the C2 gate ignores `--self-test --work` and its default scratch
  falls back to `/tmp` without `TMPDIR`. Both are defects of a frozen gate (kill rule) and are routed to round 89
  with the C2 successor; the wave's own runs passed `--work` and `TMPDIR`.
- **C2 location dependence.** `verify_corpus_integrity.py` reads the worktree and the fleet root, so `report_dead`
  reads green in the lane and DRIFT in a clone at the same revision (C2-S5, `ExecMonotoneD5` F2). D5's subset test
  survives it; a future exact-set test must not.
