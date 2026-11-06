# ReviewerCounterV5 — review of the frozen v5 counter, C2 runner, pre-data receipts (read-only)

Seat: ReviewerCounterV5. Scope: review `verifiers/fixtures/round-97/selftest-kills.py` (v5 counter)
and `verifiers/fixtures/round-97/forgery-controls.py` (C2 runner) at
`148395bf42af97436b1b832a97a175515f981939` against `plans/round-97.md`; diff the v5 counter against
the v4 counter (`verifiers/fixtures/round-96/selftest-kills.py`); re-run redbefore-c1-base,
poscontrol-r96c1-base and c2-v5 in my own scratch and compare with
`.ufo/waves/round-97/receipts/`. I wrote nothing in any repo except this file and my receipts under
`.ufo/waves/round-97/w1/ReviewerCounterV5/`; no lsp server is mounted — all checks are text +
execution evidence. No tools were installed.

Method: full raw read of both round-97 instruments and the v4 counter; programmatic AST comparison;
live runs, one counter run at a time, in scratch clone
`/fast/scratch/hyaku/kotoba-r97/ReviewerCounterV5/repo` (cloned at `148395bf`,
`rev-parse --show-toplevel` = the clone; HYAKU_SCRATCH/TMPDIR pointed at the seat scratch; scratch
removed at seat end).

## Verdict: no blocking finding. The instruments match their headers and the plan; every re-run
## reproduces its receipt. Two latent, fail-closed exit-ladder notes (F1/F2) — nothing to rescue.

## Confirmed items

1. **Rules 1–3 unchanged in meaning (v5 vs v4).** `classify`, `code_decoy`, `last_line` and `RUNNER`
   are AST-identical between the two files (programmatic `ast.dump` equality, all True); the
   `SUMMARY` regex line is byte-identical; outcome classes identical (REPORTED-FAILURE = rc 1 ∧ last
   summary N≥1 ∧ ≥1 `fail_prefix` line; CLEAN = rc 0 ∧ N=0; RUN-ERROR otherwise; RUN-ERROR never a
   kill). The only rule-1..3 surface difference is the decoy marker constant, which the header
   documents (`# r97-decoy ` default, `# r96-decoy ` under `--rules v4`).
2. **r96c1 / r95c1 anchors byte-equal to v4's c1 / r95c1.** Programmatic table equality:
   `CLAIMS["r96c1"] == v4 CLAIMS["c1"]` True; `CLAIMS["r95c1"] == v4 CLAIMS["r95c1"]` True;
   `P00 == v4 c1 positive` True. Runtime anchor-uniqueness exercised: every mutant is constructed
   with `original.count(anchor) == 1` before run 000; both live runs and all receipt runs reached
   the run phase, so all c1/r96c1/r95c1 anchors matched exactly once at this rev.
3. **`--rules v4` reproduces v4 exactly (mechanics).** Code: one shared world
   (`fresh_world("shared")` once), env carries only `TMPDIR` (`HOME`/`XDG_CACHE_HOME` guarded by
   `if rules == "v5"`), instrument restored on disk after each run, honest first and only once, no
   mirror (`mirror -`), fixed order, `DECOY_MARK_V4`. Observed order in
   `receipts/redbefore-c1-base-rulesv4.txt` (honest → blind t01..t13 → positive → per-target
   comment+code interleaved) is exactly the actual v4 counter's order, which I re-ran live at the
   freeze rev (`w1/ReviewerCounterV5/rerun-v4-counter-c1-base.txt`): v4 reads
   `C1 targets killed 11 of 11 … C1-PREDICATE-MET`, rc 0 — also confirming the round-96 no-harm
   control holds at `148395bf`.
4. **Rules 4–7 do what the header says.**
   - Rule 4 (isolation): per-run `fresh_world` = fresh `--shared --no-checkout` clone of REV +
     detach, fresh `tmp/home/cache`, `TMPDIR/HOME/XDG_CACHE_HOME` set (v5), world `rmtree`'d in the
     run loop's `finally`; the shared world exists only in v4 mode.
   - Rule 5 (mirror): mirror jobs execute the mutant AND hold it on disk; KILLED iff blind AND
     mirror both REPORTED-FAILURE. Observed live: at base every target reads `blind CLEAN mirror
     CLEAN: not killed`; at r96c1 all 11 read `blind REPORTED-FAILURE mirror REPORTED-FAILURE:
     KILLED` (`mirror runs reported 12 of 12` incl. positive).
   - Rule 6 (honest bracket): `seed = KOTOBA_R97_SEED or os.urandom(8).hex()`, printed;
     `shuffle(jobs)`, honest inserted at `rng.randrange(1, len(jobs))`, then `[honest]+jobs+[honest]`.
     Two independent live runs with different seeds/orders reproduced the same tally lines.
   - Rule 7 (exit ladder): absent instrument (git show rc≠0), non-UTF-8, failed clone/checkout,
     anchor miss, non-compiling job text (every job compiled before ANY run), timeout all raise
     `NotEvaluated` → `<C>-NOT-EVALUATED`, exit 2. **Exercised:** a scratch-clone commit
     (`fb562bae…`, identity `scratch <scratch@invalid>`) replacing the instrument with bytes
     containing `0xff` gives `C1-NOT-EVALUATED: instrument … is not valid UTF-8 at fb562bae…
     ('utf-8' codec can't decode byte 0xff in position 21)`, rc 2, no runs attempted
     (`w1/ReviewerCounterV5/rerun-exit2-nonutf8.txt`).
5. **Fail-open scan: none fail-open.** RUN-ERROR never kills; honest RUN-ERROR → UNMET; decoy
   non-CLEAN → held < N → UNMET; a crash can never produce MET or rc 0. No silent-skip path:
   decoys are appended unconditionally per target and `code_decoy`/`mutant_text` raise
   `NotEvaluated`; the results-dict lookups cannot KeyError with the unconditional job
   construction; tables are frozen non-empty. See F1 for the one ladder caveat.
6. **C2 runner matches its header.** Counter bytes measured with `git -C LANE show REV:<counter>`
   written into scratch and executed from there (printed `22741 bytes`; sha256 `b4200c52…` identical
   at `94a10217` and `148395bf`, matching every receipt header). Worlds are built only under
   `${HYAKU_SCRATCH}/kotoba-r97/forgery-controls/run.*`: clone of the lane at round-96 freeze
   `679775ab`, toplevel asserted equal to the scratch repo, patched from
   `REV:.ufo/waves/round-96/w1/ExecCounterForgeryR96/<world>.patch`, committed under
   `forgery <forgery@invalid>`, removed with the work dir. Scoring: a world is MET iff counter rc 0
   AND the last predicate line ends `-PREDICATE-MET`; REFUSED = not MET; HELD = MET;
   `met = refused == 3 and held == 2`; g2b reported, not scored; h1 = r96c1 at landing `801dd9bc`,
   h2 = r95c1 at REV.
7. **Predicate sentences identical (plan ↔ instrument headers, modulo line wrap).**
   - C1: plan § C1 and the v5 header both read "`<C>-PREDICATE-MET` iff (honest) every honest run is
     CLEAN; (targets) every target mutant applies and is KILLED; (positive) the positive mutant
     applies and is KILLED; (guard) every target's comment decoy and code decoy HOLDS."
   - C2: plan § C2 and the runner header both read "`C2-PREDICATE-MET` iff forgeries refused 3 of 3
     AND honest held 2 of 2" (h1/h2 spelled out in both).
8. **Re-runs reproduce the receipts** (same-bytes comparability verified first:
   `verify_dispatch_prompts.py` cf363a5c… and `check_mutation_battery.py` f102b419… identical at
   fa1bebae / 94a10217 / 148395bf; counter b4200c52… and runner 28fbdb9f… match the receipt-header
   sha256s):
   - `redbefore-c1-base` at `148395bf`: `C1 targets killed 0 of 13 (run errors 0); positive killed
     1 of 1; honest CLEAN; comment decoys held 13 of 13; code decoys held 13 of 13` / `rules v5:
     honest runs CLEAN 3 of 3; mirror runs reported 1 of 14; seed 6d84877cf8c02dd1` /
     `C1-PREDICATE-UNMET`, rc 1 — tally-identical to the receipt (order/seed differ by design).
   - `poscontrol-r96c1-base` at `148395bf`: `R96C1 targets killed 11 of 11 …; honest CLEAN; …
     11 of 11; code decoys held 11 of 11` / `R96C1-PREDICATE-MET`, rc 0 — matches the receipt
     (honest CLEAN 3 of 3, mirror reported 12 of 12).
   - `c2-v5` at `148395bf`: `C2 v5: forgeries refused 3 of 3; honest held 2 of 2; bound g2b MET` /
     `C2-PREDICATE-MET`, rc 0 — matches `receipts/c2-v5.txt` exactly; the honest h2 leg also proves
     `r95c1` reads MET at `148395bf`. World commit hashes differ from the receipt (583bd507… vs
     883bae2b… etc.) only because commit timestamps differ; content is the same committed patch on
     the same `679775ab` base.
   - Cause control read from `receipts/c2-v5-as-v4.txt`: v5 with `--rules v4` reads refused 0 of 3
     (all three worlds MET), honest held 2 of 2 — consistent with the code (v4 marker + v4 rules)
     and with the plan's amendment note; the refusal therefore comes from rules 4–6.
   - `poscontrol-r95c1-base.txt` (MET 3 of 3 at fa1bebae) consistent; re-proven at `148395bf` via
     the c2 h2 leg.
9. **Anchor contexts sanity-checked in the instrument** (lane working-tree sha = rev bytes):
   t01→L186 `stem = m.group(2).rstrip(".,;:")`, t05→L145 `PLACEHOLDER_RE`, t07→L142
   `REPORT_PATH_RE`, t08→L144 `ROLE_ROUND_RE`, t09→L344 `if note:`, t11/t04→L219-220 `.round` /
   `.report-baseline` is_file, t06→L217 `-shokunin" % lane`).is_dir(), t12→L496-497
   `    if fails:` / `        status = "FAIL"`, p00→L190 `stem = stem[:-3]` — each sits on the
   production statement its mutant description claims, in `verify_dispatch_prompts.py`
   (dispatch.04/08 extraction, lane identity, baseline reading, `_file_result` note, `_finish`).
10. **c1 table = plan.** The 13 frozen target names and the positive in `CLAIMS["c1"]` match plan
    § C1 one-for-one; m09/m15/m16 are absent (excluded as equivalent), m17 absent (RUN-ERROR class).

## Findings (blocking first)

None blocking.

- **F1 (LOW, latent, fail-closed): exit-ladder gap for uncaught non-`NotEvaluated` exceptions.**
  Any other exception escapes `main()` as a traceback with Python exit 1 and no
  `<C>-PREDICATE-*`/`-NOT-EVALUATED` line, so the printed ladder ("Exit 0 met, 1 unmet, 2
  could-not-evaluate") is violated on that path — a crash is printed as neither UNMET nor
  NOT-EVALUATED. Never fail-open (no MET, no rc 0; any consumer keying on `-PREDICATE-MET` or rc 0
  still refuses). Reachable instances are latent with frozen tables: (a) `code_decoy` runs
  `ast.parse(mutated)` during job construction, before the compile-all-jobs guard — a non-parsing
  table replacement would raise bare SyntaxError; (b) OSError from mkdtemp/write under disk
  exhaustion. In the C2 runner, `measure()`'s `timeout=3600` `TimeoutExpired` is uncaught (the
  counter's own 600 s should fire first) and an honest world would then read not-held —
  fail-closed. Recommendation for a future instrument round (L1 act, not a rescue): wrap the
  `main()` bodies with `except Exception → NOT-EVALUATED, exit 2`. Do not amend the frozen bytes
  this round.
- **F2 (INFO, inherited v4 bound, already routed):** the v4 counter (round-96 file) has the crash
  path genuinely reachable — a non-UTF-8 instrument at REV raises UnicodeDecodeError from
  `read_text()` uncaught → traceback exit 1 instead of NOT-EVALUATED exit 2. v5 fixes this via
  `git show` + explicit UTF-8 decode (rule 7; exercised above). No action for round 97.
- **F3 (INFO, non-issue on inspection):** `results[("honest","honest")]` / `results[("mirror",
  name)]` lookups cannot KeyError — every job kind is appended unconditionally per target and the
  honest triple is always inserted; an empty-table MET is unreachable (frozen non-empty tables; the
  positive still gates).

## Residual risks / verification gaps

- Mirror-run semantics were verified by code reading plus observed blind/mirror asymmetry at base
  vs r96c1; I did not build a source-reading attack arm against the v5 counter (that is the attack
  seats' job; my item is read-only review of the frozen instruments).
- Rule-6 order-independence was observed across two seeds for c1 and one seed each for r96c1/c2
  legs; exhaustive order coverage is not claimed.
- C2 world content depends on the committed round-96 patch files at REV; I verified the mechanism
  (git show at REV, apply on `679775ab`, toplevel assert, forgery identity) and the refusal
  readings, not each patch's internal forgery logic (frozen round-96 artifacts, out of scope).

## Files written by this seat

- `.ufo/waves/round-97/w1/ReviewerCounterV5.md` (this report)
- `.ufo/waves/round-97/w1/ReviewerCounterV5/rerun-redbefore-c1-base.txt`
- `.ufo/waves/round-97/w1/ReviewerCounterV5/rerun-poscontrol-r96c1-base.txt`
- `.ufo/waves/round-97/w1/ReviewerCounterV5/rerun-c2-v5.txt`
- `.ufo/waves/round-97/w1/ReviewerCounterV5/rerun-exit2-nonutf8.txt`
- `.ufo/waves/round-97/w1/ReviewerCounterV5/rerun-v4-counter-c1-base.txt`

Scratch `/fast/scratch/hyaku/kotoba-r97/ReviewerCounterV5/` (incl. the clone and the `fb562bae`
probe commit) is removed at seat end.
