# D2Bound — round 51 routed defect D2: bound the checklist-gate sentence

Seat: KotobaR51.D2Bound (scribe, round 51 build, 2026-10-22). Read-only on the lane except this
report; all probes ran in scratch clones at `43ca0bfb74372f2a67a48e0aeb2e35d0d98b1d10`. The gate
file at HEAD is byte-identical to the round-50 reviewed bytes (`sha256sum verifiers/verify_skill_checklist.py`
= `325d22efdf26d8a99bf5f2f395bd10ae1bc6322737859b539c80af9689d51eae`, equal to 956ee167), so the
round-50 falsify line numbers carry over.

**DRAFTED, BOUNDED** — both routed sentences now carry a fail-open bound. The gate's fail-open arms
reproduce at HEAD; the F3–F5 false-red/crash paths reproduce at HEAD; the drafts pass the lane gates
(checklist gate 11/11, exit 0; corpus-integrity identical to baseline).

## Findings (D2 sentence = calibration defect; the code is the documented behaviour)

- **F1 fail-open at the probe, fail-closed at the proof.** `delegated_box_proof`
  (verifiers/verify_skill_checklist.py:985-1027) returns a note with `problem=None` when
  `instrument_command` returns None (`:995-998`, “not runnable (no interpreter, not executable), not
  run”) or when `supports_box_proof` returns False (`:999-1002`, “no --box-proof support (%s), not
  run”). `supports_box_proof` (`:960-973`) probes `--help` with `timeout=BOX_PROOF_TIMEOUT` (120 s,
  `:312`), and returns False on `TimeoutExpired` (`:967-968`), on `OSError` (`:969-970`), and when the
  flag token is absent from stdout+stderr (`:971-973`). The note is appended to the PASS detail
  (`:1334-1336`); the check returns PASS because `proof_problems` is empty (`:1322-1326`). The proof
  run itself is fail-closed: a 120 s proof timeout (`:1009-1012`), an exec failure (`:1013-1017`) or a
  non-zero exit (`:1019-1024`) set a problem → FAIL. Reproduced at HEAD: `--help` timeout (real 120 s,
  wall 120.0 s) → exit 0 PASS “the --help probe timed out”; no-interpreter/exec-failure probe → exit 0
  PASS “the --help probe failed ([Errno 2] …)”; non-runnable target → exit 0 PASS “not runnable (no
  interpreter, not executable), not run”; hidden flag (argparse SUPPRESS) → exit 0 PASS “the --help
  probe does not advertise --box-proof”.
- **F3 false red on a relative `--map`.** `main` keeps `map_path = Path(args.map)` unresolved
  (`:2534`) while `base = map_repo or repo or Path(".")` (`:1242`) and the child runs with
  `cwd=str(base)` (`:1008`), so a relative `--map` given from another directory is passed verbatim
  (`:1004-1005`) and the child cannot read it → exit 2 → FAIL. Reproduced: control with absolute map
  from the same cwd → exit 0 PASS “--box-proof exit 0: boxes proven 2”; relative map from the parent
  dir → exit 1 FAIL “failed its --box-proof (exit 2)”.
- **F4 the red detail drops the instrument's stderr reason.** `summary = first_line(proc.stdout)`
  (`:1018`); stderr is never shown. Reproduced: a stub exiting 1 with its reason on stderr → FAIL
  detail contains no stderr line.
- **F5 non-UTF-8 `--help` output crashes the gate.** `text=True` in the probe subprocess (`:965-966`,
  same exposure at `:1007`) raises an uncaught `UnicodeDecodeError`; only `TimeoutExpired`/`OSError`
  are caught (`:967`, `:969`). Reproduced: exit 1, traceback, no JSON, no check row.
- **Detector gap.** The gate's own `--self-test` has no arm for F1–F5 (ReviewBoxProofGate.md F6),
  and 4 of 12 single-point gate mutants survive it (MutBoxProofGate.md M3, M7, M11, M12). The
  round-50 build note “A timeout or an unrunnable instrument is also a FAIL (fail-closed)”
  (.ufo/waves/round-50/build/BoxProofGate.md:33) does not match the code.
- **Live tree unaffected.** The lane's one delegated instrument runs and is green:
  `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete --json` → exit 0,
  PASS, “delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2”; full
  `--json` → exit 0, 11/11.

## Draft (a) — SKILL.md:135 replacement clause

Replace the clause `the checklist gate runs `--box-proof`` (SKILL.md:135) with:

> observed statuses; the checklist gate runs each delegated instrument's `--box-proof` against the map
> under check and FAILs the check on a non-zero exit, a 120 s proof timeout or a proof that cannot
> exec, naming the instrument and its exit code (gate `verifiers/verify_skill_checklist.py` lines
> 1006-1024, 1267-1272) - but it fails open before that run, so a delegate whose `--help` probe times
> out at 120 s, cannot be executed, carries no interpreter and no execute bit, or does not advertise
> `--box-proof` is reported PASS with the note `not run` and is left unproven (lines 945-957,
> 960-973, 996-1002; `.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1-F2) - and the same path
> false-reds on a relative `--map` run from another directory (lines 1004-1008, 2534; F3), drops the
> instrument's stderr reason from the FAIL detail (line 1018; F4), and crashes on non-UTF-8 `--help`
> output with a `UnicodeDecodeError` traceback instead of a check row (lines 965-966; F5); the

(The trailing “; the” continues the original sentence into “unsubstituted-variable clause, …”.)

## Draft (b) — SCORECARD.md operability cell, appended qualifier (append-only)

Insert immediately before the closing ` | advisory | 16 |` of line 31 (i.e. after the existing
Round-50 qualifier), starting exactly with:

> Round 51 qualifier (routed D2): the sentence above is bounded by the gate's own code, and the bound
> is fail-open on a delegate the gate cannot probe. The delegated proof does run: a non-zero exit, a
> 120 s proof timeout or a proof that cannot exec turn `checklist.box_map_complete` red, naming the
> instrument and its exit code (gate `verifiers/verify_skill_checklist.py` lines 1006-1024,
> 1267-1272). But an instrument whose `--help` probe times out, cannot be executed, or does not
> advertise `--box-proof` is reported PASS with the note `not run` and is never proven (lines
> 960-973, 996-1002; `.ufo/waves/round-50/falsify/ReviewBoxProofGate.md` F1-F2), and the detail's
> `no --box-proof support` states a fact the probe never measured (F1, Q26). The same path false-reds
> on a relative `--map` run from another directory (lines 1004-1008, 2534; F3), drops the instrument's
> stderr reason from the FAIL detail (line 1018; F4), and crashes on non-UTF-8 `--help` output with a
> `UnicodeDecodeError` traceback and no check row (lines 965-966; F5). The gate's own `--self-test`
> has no arm for any of these five paths, and 4 of its 12 single-point mutants survive it
> (`.ufo/waves/round-50/falsify/MutBoxProofGate.md` M3, M7, M11, M12). The round-50 build note that a
> timeout or an unrunnable instrument is also a FAIL (`.ufo/waves/round-50/build/BoxProofGate.md` line
> 33) does not match the code; the bound itself is already disclosed in
> `corpus/lessons/round-50.md:193` and `LOG.md:2407`. Live tree unchanged: the one live delegate runs
> and is green (`verifiers/verify_skill_checklist.py --check checklist.box_map_complete --json` exit
> 0, `boxes proven 2`).

## Gate validation of the drafts (scratch, faithful fleet layout)

- `git apply --check` of `patch.diff` onto a pristine clone at 43ca0bfb → OK. Applied; SKILL.md
  549 → 561 lines (line budget 600 unchanged, PASS).
- `python3 -B verifiers/verify_skill_checklist.py --json` on the patched faithful clone → exit 0,
  11/11 PASS (trigger.citation_resolves evaluated 51, governance.citation_resolves evaluated 967; all
  new tokens resolve).
- `python3 -B verifiers/verify_corpus_integrity.py --json` on the patched clone → identical DRIFT set
  to the unpatched baseline (tracked_files 70 vs 69, unindexed 1, report_total 45 vs 44, report_dead
  2) — pre-existing at HEAD, unchanged by the drafts.
- Append-only check: SCORECARD.md line 31's original text is preserved byte-for-byte up to the
  insertion point and the closing cells ` | advisory | 16 |` are preserved after the inserted 1648
  bytes.

## Evidence commands (all exit codes as reported)

- `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete --json` (lane,
  read-only) → exit 0, PASS, “…delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0:
  boxes proven 2”.
- `python3 -B verifiers/verify_skill_checklist.py --json` (lane, read-only) → exit 0, pass 11 fail 0.
- Probe suite in `/fast/scratch/hyaku/kotoba-r51/build/D2Bound/` (probe.py, probe2.py, probe3.py):
  P1 hidden flag exit 0 PASS; Q2 exec-failure probe exit 0 PASS; P3 not-runnable exit 0 PASS; Q1 real
  120 s timeout exit 0 PASS (wall 120.0 s); P4a absolute-map control exit 0 PASS; P4b relative-map
  false red exit 1 FAIL (exit 2); P5 stderr-dropped FAIL detail; P6 non-UTF-8 crash exit 1
  UnicodeDecodeError, no JSON.

## Out of scope / notes

- No code changes proposed (fail-closed fix list already exists in ReviewBoxProofGate.md “Fix list”);
  this item bounds the two sentences.
- Lane writes: none besides this report; the stray `kotoba-shokunin-d2trial` copy I accidentally
  created via a symlinked `cp` was removed (lane `git status` now shows only other seats' edits).
- No tools installed or updated (Python 3.14.8 present).

Report: .ufo/waves/round-51/build/D2Bound.md
Patch artifact (scratch, for the L1): /fast/scratch/hyaku/kotoba-r51/build/D2Bound/patch.diff (unified diff vs 43ca0bfb; SKILL.md +14/-1, SCORECARD.md +1/-1).
