# ReviewerArmsR97 — C1 patch review (dispatch-prompt self-test arms)

Seat: ReviewerArmsR97 (reviewer, wave r97-w1). Status: **COMPLETE — no blocking finding; C1 patch RECOMMENDED for landing.**

## Verdict

**RECOMMEND LANDING.** The patch (sha256 `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80`,
+231 lines in `verifiers/verify_dispatch_prompts.py`, all inside `self_test()`) meets every reviewed
criterion:

1. **Ownership/byte-identity** — head (module docstring..`run_checks()`) and tail (box-proof section
   ..EOF, `box_proof()`/`main()`) byte-identical to the freeze `148395bf`; the single hunk sits
   between them (nested helper `lane_case` + arms); no production byte changed.
2. **FROZEN ANCHORS** — all 14 c1 anchors counted exactly 1 on the patched file; no new bare
   `if note:` / `if fails:` anywhere; mutated statements keep their line count (production frozen).
   The counter runs themselves prove r96c1/r95c1 anchors too (an anchor miss is exit 2; both MET rc 0).
3. **ANTI-SNIFFING** — every one of the 27 new assertions reads a behaviour result
   (`report_paths`/`role_round`/`has_placeholder`/`lane_kind`/`state_source`/
   `evaluate_dispatch_04`/`evaluate_dispatch_08` on fixture inputs); no source reading, no
   `__file__`/`inspect` in new code. Comment and code decoys held 13/13 under the v5 counter
   (blind AND mirror reported for every kill), so no arm is source-sensitive.
4. **Hand-applied kills** — 14/14 mutants KILLED in my candidate clone, each a REPORTED failure
   (rc 1, `self-test FAIL:` lines, `N failure(s) over 105 assertions`, N ≥ 1, zero RUN-ERRORs);
   per-mutant failing assertions in the table above; each kill reason matches the mutant's stated
   description. Positive p00 killed (8 assertions). Honest run CLEAN 0/105.
5. **Counter readings (my candidate commit `7fbfe2a02305debc97c9c08eda70b091966aae3d`, my clone
   `repo-cand`, lane instrument bytes `94a10217`):**
   - `c1` v5 → `C1 targets killed 13 of 13 (run errors 0); positive killed 1 of 1; honest CLEAN;
     comment decoys held 13 of 13; code decoys held 13 of 13` — **C1-PREDICATE-MET**, rc 0,
     seed 283ef5bceffdd96a (matches the builder's MET at their `ac7a00f5`, seed 35748dccbbc61dd5).
   - `c1 --rules v4` → 13 of 13, **C1-PREDICATE-MET**, rc 0 (separability: C1 stands without v5 rules).
   - `r96c1` → 11 of 11, **R96C1-PREDICATE-MET**, rc 0. `r95c1` → 3 of 3, **R95C1-PREDICATE-MET**, rc 0.
   - `--box-proof` → `boxes proven 2`, rc 0.
6. **Fixture hygiene** — everything under the pre-existing `TemporaryDirectory` (TMPDIR-honouring),
   removed on exit; t10's mode-000 baseline restored to 0600 in a `finally` inside the context
   before cleanup; no absolute /tmp in new code; no crash (verified: t10 kill is a clean REPORTED
   failure with `(Permission denied)` in the detail).

## Findings (non-blocking)

- **N1 (nuance, fails safe):** t10's arm degrades to a recorded-true assertion under a *root* run
  (`os.geteuid() == 0` guard); under root the t10 mutant would survive → counter reads
  `12 of 13 … UNMET` — an honest red, never a false green. The counter's per-run fresh TMPDIR/HOME
  runs as the seat user (non-root), so the real arm executes.
- **N2 (harmless coupling):** t03's and t04's mutants additionally trip t06's recs (all three
  arm groups read the same fleet-root behaviour through `lane_kind`/dispatch.04). Over-determined
  kills; no assertion depends on a mutant.
- **N3 (cosmetic):** the honest `state_source` t02 detail string under the t02 mutant still says
  `"empty …"` while carrying `("baseline", 10**9, …)` — the mismatch is itself the kill witness;
  no action.

## Residual risk / verification gaps

- I reviewed C1 only; C2 (v5 forgery refusal) and the corpus/lesson seats are out of my scope.
- The v5 counter's disclosed bounds (g2b source-sniffer; state outside per-run dirs) remain as
  stated in the plan — unchanged by this patch.
- My runs used my scratch clone commit `7fbfe2a0…`; the L1 landing should re-run the same five
  readings at the landing revision (the plan's no-harm battery already requires it).

## Evidence files (this dir)

`README.txt` (provenance), `hand-mutants-candidate.txt` (per-mutant kill log),
`c1-v5.txt`, `c1-v4.txt`, `r96c1.txt`, `r95c1.txt`, `boxproof.txt`. Scratch
`/fast/scratch/hyaku/kotoba-r97/ReviewerArmsR97/` deleted after this report was written.

## Verification log

Scope reviewed: `.ufo/waves/round-97/w1/ExecArmsR97/ExecArmsR97.patch` against `plans/round-97.md`
§ C1, the ANTI-SNIFFING rule and the FROZEN ANCHORS rule; per-mutant hand-applied kills (t01..t13)
with the failing assertion named; v5 counter readings c1 / r96c1 / r95c1 / c1 `--rules v4` /
`--box-proof` on the candidate; fixture hygiene under TMPDIR.

- Plan read in full; counter header + `CLAIMS["c1"]` (13 targets + p00) and runner header read.
- Scratch set up at `/fast/scratch/hyaku/kotoba-r97/ReviewerArmsR97/` (TMPDIR/HYAKU_SCRATCH exported
  per command; single scratch dir holding the candidate clone, harness scripts and run logs).
- Freeze base `148395bf42af97436b1b832a97a175515f981939` staged to
  `dp_freeze.py`; all 14 frozen anchors counted == 1 at base (including `if note:` and the two-line
  `    if fails:` / `        status = "FAIL"` pair, `stem = stem[:-3]`).
- Candidate base clone `/fast/scratch/hyaku/kotoba-r97/ReviewerArmsR97/repo-cand` at 148395bf;
  `git rev-parse --show-toplevel` == the clone dir.
- Hand-mutant harness `hand_mutants.py` (scratch-only) validated on the untouched base: **all 13
  targets CLEAN (0 failures over 78 assertions), positive p00-md-not-stripped KILLED**
  (5 failures: control dispatch.04 verdict, `report_paths keeps an absolute report path`, three
  box-proof recs) — this independently reproduces the pre-data red receipt
  `redbefore-c1-base.txt` (`C1 targets killed 0 of 13 … C1-PREDICATE-UNMET`).
- Static reviewer `review_static.py` ready: head region (docstring..run_checks) and tail region
  (`# box proof`..EOF, i.e. box_proof()+main()) byte-identity, difflib locality of every changed
  line inside the owned region (`def _write_case` .. before the box-proof section comment), and the
  14-anchor uniqueness check on the patched file.
- `ExecArmsR97_READY` present after 360 s; patch sha256 verified
  `22638a4e8a81cc8fabf1760660d5908ed40d8a0a5e4b9d09212d7c87d8973c80` (matches READY).
- Patch applied to `repo-cand` cleanly; **STATIC-REVIEW OK** (`review_static.py`): head region
  (docstring..run_checks) and tail region (`# box proof`..EOF) byte-identical to the freeze base;
  every changed line (one hunk, +237/−0) inside the owned region (one nested helper `lane_case` +
  13 arm groups, all inside `self_test()`); all 14 frozen anchors counted == 1 on the patched file
  (so no second `if note:` / `if fails:` was introduced). `import os` present (module line 85), so
  the `os.geteuid()` root guard compiles.
- Candidate committed in my clone as `7fbfe2a02305debc97c9c08eda70b091966aae3d`
  (identity `scratch <scratch@invalid>`; tree = 148395bf + patch only;
  `git rev-parse --show-toplevel` == the clone). Builder's own candidate commit was `ac7a00f5c5…`
  in the builder's clone — same patch, so same tree content (byte counts cross-checked: candidate
  file 77704 B in the builder's `production-identity.txt`).

## Hand-applied kills (t01..t13 + positive, candidate `7fbfe2a0`)

`hand_mutants.py` applies each frozen anchor→replacement (count-asserted == 1) and runs
`python3 -B verifiers/verify_dispatch_prompts.py --self-test` in a fresh TMPDIR. Self-test grew
78 → 105 assertions (+27, matching the READY claim). **14 of 14 KILLED, zero RUN-ERRORs**
(full log: `hand-mutants-candidate.txt` in my scratch; table below: failing assertions under the
mutant, all REPORTED `self-test FAIL:` lines, rc 1):

| mutant | fails | discriminating assertion(s) — observed got |
|---|---|---|
| t01-rstrip-dot | 3 | `report_paths reads the stem 'kote'`: got `[(7, 'kote.md.')]`; stem conjunct + file verdict FAIL (`kote.md. != lane id 'kote'`) |
| t02-empty-baseline | 3 | `state == 'none'`: got `('baseline', 1000000000, 'empty …')`; conjunct N/A rec got PASS `round 7 <= latest dispatched 1000000000`; file verdict PASS |
| t03-fleetroot-stem-pass | 3 | fleet-root stem conjunct got PASS; file verdict got PASS (also trips t06's not-PASS rec) |
| t04-fleetroot-no-baseline | 3 | `lane_kind == 'fleet-root-role'`: got `'unknown'`; `lane_identity_known` got FAIL `names no known lane` (also trips t06's lane_kind rec) |
| t05-placeholder-empty-angle | 2 | `has_placeholder('kote<>')`: got `False`; `report_path_literal` got PASS while stem conjunct still FAILs (isolates the placeholder conjunct) |
| t06-sibling-file-as-lane | 2 | `lane_kind`: got `'sibling-lane'` for a plain FILE; file verdict got PASS |
| t07-report-regex-noprefix | 2 | `report_paths('.ufo/reports/7/kote.md')`: got `[(7, 'kote')]`; file verdict got PASS on the prefix-less prompt |
| t08-role-regex-nospace | 2 | `role_round('…, round7 …')`: got `7` (honest `None`); conjunct got PASS `role line round 7` |
| t09-file-note-dropped | 1 | `f.get('note') == 'no report path found'`: got no `note` key |
| t10-unreadable-as-baseline | 2 | `state == 'none'`: got `('baseline', 1000000000, 'unreadable … (Permission denied)')`; conjunct got PASS. Non-root run; mode-000 file chmod-restored to 0600 in `finally` before the TemporaryDirectory context exits; no crash, cleanup clean |
| t11-lane-kind-legacy-dropped | 2 | `lane_kind`: got `'unknown'` for legacy-only lane; `lane_identity_known` got FAIL |
| t12-finish-single-fail-na | 1 | check status got `PASS` with detail `1 PASS, 1 FAIL` (one failing file `kote-round-8.md` beside one passing file) — the check-level FAIL headline |
| t13-noreport-08-pass | 2 | dispatch.08 file verdict got PASS; conjunct `filename_report_dir_round_equal` got PASS `no report path found in the file` |
| p00-md-not-stripped (positive) | 8 | control verdict, `report_paths keeps an absolute report path`, three box-proof recs, t01 report_paths rec, +2 more |

Each kill reason matches the mutant's stated description; the honest run on the same candidate is
CLEAN (0 failures over 105 assertions).

### Anti-sniffing check (patch reading)

Every new rec observes a behaviour: a call result of `report_paths` / `role_round` /
`has_placeholder` / `lane_kind` / `state_source` / `evaluate_dispatch_04` / `evaluate_dispatch_08`
on fixture inputs, or the resulting file/check dicts. No rec reads this file's source, no
`__file__`/`inspect`/frame access in the new code (the only `__file__` use is the frozen box-proof
skill copy, unchanged). The root guard on t10 records an environment-conditional arm (a root run
cannot exercise mode-000); the counter runs non-root, so the real arm executes.

### Fixture hygiene

All fixtures live under the pre-existing `tempfile.TemporaryDirectory(prefix="dispatch-selftest-")`
(`root`), so they honour TMPDIR and are removed on context exit. `lane_case` writes only under
`root/<name>`. t10's mode-000 baseline is chmod-restored to 0600 in a `finally` that runs inside
the context, before cleanup. No absolute /tmp path anywhere in the new code.
