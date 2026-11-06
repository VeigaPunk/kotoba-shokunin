# CriticClaimR99 — falsification of C1/C2 against the full round-99 candidate

Seat: CriticClaimR99 (critic, leaf; no subagent dispatch). Status: **COMPLETE** — full candidate built and measured
(`b1e25510`); both READY files present and their patch shas equal the ones I measured
(`bd32f78d…` reds, `94a39dee…` scribe, `9b705bc8…` arms). The reds builder's own full-candidate
receipt (`d0afe6a`, `c2-candidate.txt`) reads the same `green 2 of 3` and the same DRIFT
`tracked_files 204 vs 203`, `report_total 175 vs 174` as my independent build. Every reading below is mine: my own scratch clone
`/fast/scratch/hyaku/kotoba-r99/CriticClaimR99/repo` (clone of the lane at
`b53e209603e7c480cd975ea543e415b66f695438`, `rev-parse --show-toplevel` = the clone), my own
counter invocations, receipts under `.ufo/waves/round-99/w1/CriticClaimR99/receipts/`.

## Mandate

Falsify the two frozen claims against the full candidate (base + ExecRedsR99 + ScribeCorpusR99 +
ExecArmsR99, in that order) and against each single-patch candidate (separability); reproduce the
pre-data do-nothing receipts; attack the four questions: cheaper do-nothing route, §9 axis naming,
are the twelve C1 targets real false greens, is the n12/n18/n19/n20 exclusion honest, does S281
ground t08, does the mined-mistake fix fail on its committed control, is the round-98 routed-defect
list honestly dispositioned.

## Pre-data reproduction (do-nothing controls, my runs)

`python3 -B verifiers/fixtures/round-99/selftest-kills.py c1 52e8e95… "$D"` →
`C1 targets killed 0 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held
12 of 12; code decoys held 12 of 12` / `C1-PREDICATE-UNMET` rc 1. Diff against
`receipts/redbefore-c1-base.txt`: **identical except the scratch path** (receipt
`ctl-donothing-c1-base.txt`).

`python3 -B verifiers/fixtures/round-99/carried-reds.py 52e8e95… "$D"` →
`C2 carried reds green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` /
`C2-PREDICATE-UNMET` rc 1. Diff against `receipts/c2-base.txt`: **identical except the scratch path**
(receipt `ctl-donothing-c2-base.txt`).

## C1 — single-patch candidate (base + ExecArmsR99.patch)

Patch sha256 `9b705bc807855d0149a9eda9e2d45d2f024a34bb71606f99979f158f3f9af924` = the sha in
`ExecArmsR99_READY` = the sha my clone applied. Scratch commit `104dae151c3f351558a94a12f510d59ba2629c0a`.
Note (minor): the patch carries git mnemonic diff prefixes (`c/`…`i/`) instead of `a/`…`b/` (a
builder git-config artifact); `git apply` handles it and the applied bytes equal the READY patch
(MutTesterDispatchR99 independently normalised the same 15124 bytes to the same sha).

Static kill-rule probe (`critic_probe.py`, receipt `probe-arms.txt`):

| kill-rule conjunct | reading |
|---|---|
| every anchor of `CLAIMS[c1]` (13), `[r98c1]` (10), `[r97c1]` (14), `[r96c1]` (12) matches exactly once | 49 of 49 count 1 |
| instrument diff vs `52e8e95` confined to `self_test()` | one hunk `@@ -1514,0 +1515,270 @@ def self_test()`, new span 1515–1784 inside `self_test` 679–1795; 0 deleted lines → production bytes unchanged |
| `--box-proof` | `boxes proven 2`, rc 0 |
| honest `--self-test` | `0 failure(s) over 154 assertions`, rc 0 (128 → 154) |
| counter bytes at REV | both frozen (`aff38953…`, `5f964253…`) |

Counter (`c1`, rules v6) → `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1;
honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12` / `rules v6: honest runs CLEAN
3 of 3; mirror runs reported 13 of 13` / `C1-PREDICATE-MET` rc 0 (receipt `sep-c1-arms-only.txt`).
Per-mutant reported-failure counts (both blind and mirror): t01 3, t02 3, t03 2, t04 2, t05 2, t06 2,
t07 2, t08 2, t09 1, t10 2, t11 1, t12 1; p00 12. Every kill is a REPORTED failure in both runs —
no run errors, no crashes.

### Are the twelve real false greens or contrived?

Each is a behaviour the base self-test did not observe, and each mutant changes a *verdict* on a
fixture input (MutTesterDispatchR98 § Differential witnesses, re-read; the base counter's own
`redbefore-c1-base.txt` shows all twelve CLEAN at base, i.e. the base self-test passes on each
mutant). I checked the three weakest by hand against the base bytes:

- **t01** (`L1_FILE_RE` not end-anchored): `lane_of("kote-L1.md.bak")` returns a lane under the
  mutant, so `evaluate_dispatch_04` evaluates a backup file as a spawn prompt (honest: 0 evaluated,
  N/A). Verdict-bearing.
- **t02** (`elif rr != round_n:` → `elif rr < round_n:`): a role line stating round 8 for a
  `round-7` file passes under the mutant; honest FAILs `filename_role_round_equal`. Verdict-bearing.
- **t12** (`if fails:` → `if fails and not nas:`): one FAILing round file beside one N/A file reads
  N/A under the mutant, FAIL under the honest code. Verdict-bearing.
- **t09** needs a non-root uid; this host runs the counter as uid 1000 (`id -u` → 1000), and the arm
  is guarded by `os.access` (root would record a pass, not a false failure). Verdict-bearing here.

### Is excluding n12/n18/n19/n20 honest?

Yes, and I verified the sharpest one myself: **n12 is a dead branch** — `report_paths` runs
`stem = m.group(2).rstrip(".,;:")` before `if not stem or stem in (".", "..")`, so a dots-only stem
is already `""` and `if not stem` catches it first (`verify_dispatch_prompts.py:184-186`, read at the
freeze). n18 changes only the `detail` string's PASS/N/A counts (status and exit identical); n19
sends both versions to a non-baseline state (`round_le_latest_dispatched` N/A either way); n20 is
equivalent on the committed nine-box `SKILL.md` (latent only). The round-97 closure's rule (routed
defect 6: no-verdict mutants are not kill targets) is applied consistently; none of the four is
silently dropped from the *record* — they are named, with their equivalence reason, in the counter
header.

### Anti-sniffing / arm discipline

The added 270 lines call only production helpers on fixture inputs (`lane_of`,
`evaluate_dispatch_04/08`, `_verdict_of`, `run_checks`, `main` with explicit argv and in-process
stdout capture, `box_proof` via the existing `run_proof` closure, `EnvError`, `os.access`). No
`__file__`/`inspect`/`ast`/`open`/`read_text`/`subprocess`/`os.environ` in the added lines (grep of
the patch: no matches). Every assertion goes through the existing `rec(...)` tally; the `main()` and
`run_checks` calls are wrapped in try/except so a mutant reads a reported failure, not a crash. The
t04 arm unlinks and restores `SKILL.md` inside the self-test tempdir; `box_proof` returns 1 (never
raises) on a missing skill, so the restore is reached on the honest and mutant paths.

## Independent witness reproduction (C1 target reality)

`witness_r98.py 52e8e95 <lane>` (round-98 harness, my TMPDIR) → `witnesses: 19 DIFFERS`, n12 `SAME`
(receipt `witness-base-rerun.txt`). Every one of the twelve c1 targets (n01–n05, n07–n11, n13, n14)
has a differential witness at the base: honest and mutant disagree on the same fixture input. n12 is
`SAME` by construction (dead branch, verified in the source). n19's witness differs at the
`state_source` level (`stale` vs `none`) but both versions leave `round_le_latest_dispatched` N/A —
the counter header's "verdict-equivalent" is accurate, not a euphemism.

## C2 — forgery controls re-run (my clone)

Both control worlds rebuilt from the committed patches at the round base and measured with the
frozen counter:

| control | my reading | pre-data receipt | verdict |
|---|---|---|---|
| w1 stub the two corpus gates | `green 2 of 3; self-tests held 1 of 3; frozen 2 of 4; guards FAIL` / `C2-PREDICATE-UNMET` rc 1 | same | **reproduces exactly** |
| w4 checklist governance forced PASS + blob pinned | `green 1 of 3; self-tests held 3 of 3; frozen 3 of 4; guards ok` / `C2-PREDICATE-UNMET` rc 1 | same | **reproduces exactly** |

w4 is the load-bearing discrimination: the forced-PASS checklist reads GREEN and its self-test holds,
so only the frozen conjunct (bytes differ outside the corrections data) refuses it. The counter is
not a gate-exit counter that a stubbed or forced gate can satisfy.

## C2 — patch review (ExecRedsR99, final sha `bd32f78d…` = the READY sha)

Files: `LOG.md` (+21: one correction notice, 16 bullets), `corpus/README.md` (+9 coverage rows:
r91–r98 spot-checks + a round-99 row), `corpus/lessons/round-81.md` (line 8 hash quoted, meaning
unchanged), `verifiers/check_tip_battery.py` (one `INSTRUMENT_PINS` blob `b6280c68…`; I verified
`git rev-parse HEAD:verifiers/verify_skill_checklist.py` = that blob), `verifiers/corpus-baseline.json`
(three `equal` expects 172→203, 127→174, 59→72), `verifiers/verify_skill_checklist.py` (horizon
2723→3601 + 15 appended rows + the round-65 row's subject line 158→161).

Laundering check (Q64/M118): every corrected token names the same artefact the stale token named —
the fleet reports (`../.ufo/reports/...`), the fleet driver log, the L0 questions file, the round-82
receipt renamed `-dot`→plain (the round-83 notice already names the supersession), the `.ufo/wapes`
typo whose own sentence names `.ufo/waves/round-81/dispositions/wapes.txt`, the quarantined
`check_description_render.py` frozen copy, and the `:30,37` citation's bare path. No row points at a
"record of removal" instead of the artefact (the round-70 laundering shape).

Two defects found in the data records (not in the predicate):

- **D4 (baseline provenance, real).** The re-record note says the numbers were taken "over the
  round-99 candidate tree (base b53e209 + candidate patches in order ExecRedsR99, ScribeCorpusR99,
  ExecArmsR99)". The numbers are the **ExecRedsR99-only** tree's: `tracked_files 203` is the freeze
  count, and the full candidate adds `corpus/lessons/round-99.md` → 204. The interim receipt proves
  it: the equal counts pass on the single-patch tree (only `stale_patterns`/`missing_paths` drift),
  which is only possible with 203. The same file keeps `measured_against.head = e03f9e22…`
  (round-87) and the round-87 `head_subject`/`git_status` text under a round-99 note — the metadata
  contradicts the note. Minimal correction: the note names the ExecRedsR99-only tree and says the L1
  re-records at integration; `head`/`head_subject`/`git_status` are updated with the re-record.
- **D5 (notice wording, minor).** The `SCORECARD.md:529` bullet reads `stale "…:30,37" corrected
  …round-80-verifier-spotcheck.md` with no word that the subject is a **gate false red**
  (`strip_token_dressing` lacks the `:N,M` form, ScoutTipReds F5) and not a content error. The plan
  discloses the gate defect; the durable record (the notice) does not. Minimal correction: append
  the parenthetical to that bullet and re-pin its row sha256.

Separability (measured, not inferred): the ExecRedsR99-only candidate reads **green 1 of 3**
(checklist green; integrity 7/9 with `stale_patterns`+`missing_paths`; independent red) — the
round-99 coverage row precedes ScribeCorpusR99's file, so the row is stale/missing by construction.
I ran both corpus gates directly in a fleet-shaped sandbox of the single-patch commit
(`bb827df4…`): the **only** findings are `corpus/README.md:209: lessons/round-99.md` (stale) and
`lessons/round-99.md -> corpus/lessons/round-99.md` (missing); `unindexed 0`, `report_dead 0`,
`commit_unresolvable 0`, `commit_nonhash 0`, and the three equal counts 203/174/72 all pass. So the
content fix is otherwise complete and the single-patch red is exactly the anticipated phantom row
(the seat item says "the row may precede the file in your candidate — say so"). The plan's
separability sentence ("Each is measured at its own candidate") is therefore not met for C2; the
smallest green unit is the landing. This is a construction fact, not a C2 failure, and the L1
should report it as such.

## C2 — single-patch candidate (base + ExecRedsR99.patch, interim sha `bd32f78d…`)

Scratch commit `bb827df49c5cbbd4f9587acf2abe24e555124b64`. My counter run (receipt
`sep-c2-reds-only.txt`):

```
checklist PASS lines 11 (min 11); FAIL/N/A lines 0
red verify_skill_checklist.py exit 0 GREEN: PASS governance.citation_resolves: evaluated 1651 — … 19 recorded correction(s) excused
red verify_corpus_integrity.py exit 1 RED: 7/9 checks pass; DRIFT: corpus.index.stale_patterns, corpus.index.missing_paths
red verify_corpus_independent.py exit 1 RED: exit 1
selftest 3 of 3 HELD; frozen 4 of 4; battery guards 5 of 5
C2 carried reds green 1 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok
C2-PREDICATE-UNMET  rc=1
```

The single red is the round-99 coverage row preceding ScribeCorpusR99's file (measured directly:
`corpus/README.md:209: lessons/round-99.md` stale, `lessons/round-99.md -> corpus/lessons/round-99.md`
missing; every other zero-mode check 0 and the three equal counts 203/174/72 pass). The patch is
otherwise complete; the single-patch reading is red by construction and is **not** a C2 failure.

## ScribeCorpusR99 — S281 row and round-99 lesson (final patch sha `94a39dee…` = the READY sha)

- **S281 row** (line 222): version-pinned URL `https://docs.python.org/release/3.15.2/library/argparse.html`,
  tier A, kind `docs`, `mined`, 2026-11-06, recheck 180d, used-by `corpus/lessons/round-99.md,plans/round-99.md`.
  I re-fetched the pinned URL myself: **327874 B, sha256 `36e8d536…`** — identical to the row; the
  22-word quote is at HTML 989–990, the page's own version pin at 19 and footer at 2709. The row
  names the rolling `/3/` alias, its digest and the 5-byte footer mechanism as superseded, and notes
  the bare marker `'append'` occurs twice (HTML 989 and 1062) so a recheck must match the sentence.
  Census at the full candidate: `file ok`, **207 rows** (206→207), **W04 34** (unchanged).
- **Lesson** `corpus/lessons/round-99.md` (221 lines): `## Gate` (S281 with access record, excerpt,
  quote + `wc -w`, anchor-ambiguity note, the superseded alias, the bound that the page is not the
  authority for the lane's own `args.check` handling); `## Corrections` C99-1 (182 not 183 lines,
  with the two-file numstat), C99-2 (the SCORECARD r98 red-before names `63cd48d9`, the receipt
  measured `a060b450`, bytes equal), C99-3 (S279's quote stops before the `CAP_SYS_PTRACE`
  conjunct; the page digest re-verifies byte-identical — I re-fetched it: 104833 B, `69cd309e…`,
  conjunct at HTML 1519), C99-4 (the S281 rolling-digest drift, with the measured 5-byte field);
  `## Mistakes` (the class row with evidence, captured-by, fix "claim C2 plus … Q89 — the L1 adds
  Q89", shown able to fail `c2-base.txt` 0 of 3); `## Status changes` (none, with the S279/S253/
  S270/S276 re-opens named and deliberately not edited); `## Considerthese` (all five proposals
  still unimplemented, each measured); `## Settlement` (L1 placeholder).
- **Addendum 1** (`plans/round-99-addendum-1.md`, L1, before the landing reading): A1 pins S281 to
  the versioned URL; A2 routes the S253/S270/S276 rolling digests to round 100. It states "No
  predicate, counter, target or kill rule changes" — I read it against the plan and confirm that.

### Full candidate (base + reds + scribe + arms)

Final patch set: reds `bd32f78d…`, scribe `94a39dee…` (the READY sha; the scribe re-cut the patch
at 11:27 to double-quote the Mistakes-row tokens so they are quoted meta-findings, not live report
pointers), arms `9b705bc8…`. Scratch commit **`b1e255104bea2716e59046cc8cdcecd6798f2348`**
(`git add -A` so the new lesson is committed; `git ls-files corpus/` = **204**).

Static probe (`probe-full.txt`): 49 of 49 anchors count 1; one hunk inside `self_test`; `boxes
proven 2`; `0 failure(s) over 154 assertions`; both counters frozen.
`selftest-kills.py c1 b1e25510` → `C1 targets killed 12 of 12 … C1-PREDICATE-MET` rc 0
(`full2-c1.txt`).

Direct gate run in a fleet-shaped sandbox of `b1e25510`:
`tracked=204 unindexed=0 stale=0 missing=0`, `report_dead=0/175 commit_total=72 unresolvable=0
nonhash=0`; **integrity 7/9** with `DRIFT tracked_files 204 vs 203` and `report_total 175 vs 174`;
**independent exit 0**; `check_correction_sweep.py --root .` → `0 stale block(s)`;
`check_gate_registry.py --rev HEAD` → `74 of 74 … phantom 0`. So the only C2 gap at the full
candidate is the two equal-mode counts the scribe's lesson moved (+1 tracked file, +1 report
pointer) — exactly the drift the plan says the L1 re-records at integration; every zero-mode check
is 0 and the independent gate is green.

**Landing simulation** (`a211ddf0`, my clone only): the same tree with the baseline re-recorded to
the gate's own observed 204/175/72 — the act the plan assigns to the L1 — then the frozen counter:
`C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` / **C2-PREDICATE-MET**
rc 0 (receipt `full2-rerecord-c2.txt`). The full candidate without the re-record reads
`green 2 of 3` / UNMET rc 1 (`full2-c2.txt`). So C2 is reachable at the landing exactly by the
disclosed integration act, and the gap is the two equal-mode counts, not a content defect.

## Verdicts

| claim | candidate | verdict |
|---|---|---|
| C1 | base + ExecArmsR99 (`104dae15`) | **MET** — `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12` / `C1-PREDICATE-MET` rc 0; `--rules v5` same tally MET; `r98c1` 9 of 9 MET; `r97c1` 13 of 13 MET; `r96c1` 11 of 11 MET |
| C1 | full candidate (`b1e25510`) | **MET** — 12 of 12, rc 0; instrument bytes identical to the arms-only candidate (one hunk inside `self_test`) |
| C2 | base + ExecRedsR99 (`bb827df4`) | **UNMET by construction** (green 1 of 3; the phantom round-99 row) — not a claim failure |
| C2 | full candidate (`b1e25510`) | **UNMET** — `green 2 of 3` rc 1; the only reds are `tracked_files 204 vs 203` and `report_total 175 vs 174` (the scribe's lesson), i.e. the disclosed baseline drift |
| C2 | full candidate + L1 baseline re-record (`a211ddf0`, simulation) | **MET** — `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` rc 0; battery `guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0 |
| C1/C2 | do-nothing at `52e8e95` | both UNMET, receipts reproduce exactly |
| C2 | forgery controls w1/w4 | both UNMET, receipts reproduce exactly |

## Findings

- **F1 (C1 is real and separable).** The twelve frozen survivors are genuine false greens of the base
  self-test (all CLEAN at base; every one has a differential witness; I reproduced 19 DIFFERS / 1
  SAME with the round-98 harness and hand-applied six mutants to name the exact failing assertion).
  The arms kill each mutant in both the source-blind and mirror runs, with 1–3 reported failures and
  no run errors; the positive control kills with 12. Production bytes are unchanged (one hunk inside
  `self_test`), all 49 frozen anchors still match exactly once, `--box-proof` stays `boxes proven 2`,
  and the three predecessor tables stay MET. The claim is met at the arms-only candidate and at the
  full candidate.
- **F2 (C2 is real but its measurable unit is the landing).** The content fixes are complete: at the
  full candidate every zero-mode corpus check is 0, the independent gate is green, the checklist is
  green (11 PASS, 19 corrections excused) and the correction rows are mechanically sound (I verified
  all 20 rows' line sha256, both tokens on each notice line, and every stale token on its subject
  line). The only gap is the two equal-mode counts the scribe's lesson moved; re-recording them to
  the gate's own observed 204/175/72 — the act the plan assigns to the L1 — turns the counter MET and
  the whole battery 6 of 6. The single-patch candidate reads 1 of 3 by construction (the round-99
  coverage row precedes the file), so the plan's "each is measured at its own candidate" sentence is
  over-stated for C2.
- **F3 (the counter's discrimination is load-bearing).** w4 (a checklist forced to PASS with its blob
  pinned) reads GREEN and its self-test holds; only the frozen-bytes conjunct refuses it. w1 (stubs)
  reads 2 of 3 with guards FAIL. Both reproduce the pre-data receipts exactly, as do the do-nothing
  controls. A gate-exit-only counter would pass w4; this one does not.
- **F4 (S281 grounds t08; the access record was repaired before data).** The pinned page verifies
  byte-for-byte (327874 B, `36e8d536…`), the 22-word quote is at HTML 989–990 and the sentence is
  unique; the rolling `/3/` alias is disclosed as superseded with the measured 5-byte footer
  mechanism. The L1's pre-data receipt digest is not re-fetchable, and addendum 1 (before the landing
  reading) plus the row handle it honestly.
- **F5 (the mined-mistake fix is half-landed by the wave).** The lesson records the class, the
  captured-by (the gate fired; the no-harm rule accepted the red set) and the fix "claim C2 plus a
  QUALITY criterion — the L1 adds Q89", with `c2-base.txt` (0 of 3) as the shown-able-to-fail
  control. Q89 is an L1 act at integration and is not in the wave's file ownership; verify it lands.
- **F6 (round-98 routed defects are honestly dispositioned, with one disclosed narrowing).** 2, 3 and
  5 land as C99-1/C99-2/C99-3 in the lesson; 4 is confirmed (two `/dev/shm` markers remain, listed
  not deleted); 6 is C2. Defect 1 (the non-reproducible v6 refusal) is carried to round 100 — a
  disclosed narrowing of the calibration sub-axis's own prior miss, which this round's C2 does not
  retest.

## Defects

- **D1 (S281 access record — resolved before data).** The L1's pre-data receipt digest `bcd717f2…`
  does not reproduce (the `/3/` page was rebuilt at 13:47 UTC, 6 min after the 13:41:12Z fetch; the
  two streams differ in exactly 5 bytes, the Sphinx footer). The L1's addendum 1 (before the landing
  reading) pins S281 to `https://docs.python.org/release/3.15.2/library/argparse.html`, and the
  scribe's row cites that URL with a digest I reproduced exactly (327874 B, `36e8d536…`) and names
  the rolling alias as superseded. **No open defect in the landed row**; the residual is that the
  frozen pre-data receipt's digest is a build stamp, which the row and C99-4 disclose.
- **D2 (QUALITY criterion, landing dependency).** The mined-mistake fix's second half ("a QUALITY
  criterion that a landing's no-harm reading requires the carried-reds counter MET") is assigned to
  the L1 ("L1 adds Q89" in the scribe's item) and is not in the wave's file-ownership list. If the
  L1 does not add Q89 at integration, the recurrence guard is missing and the fix is only the C2
  data repair. Verify at the landing.
- **D3 (separability over-stated, disclosure).** The plan says each claim is measured at its own
  candidate; C2's own candidate reads 1 of 3 by construction (the row precedes the file). The seat
  item anticipates the row ("the row may precede the file … say so"), the plan does not. Report the
  reading with its cause; do not treat it as a C2 failure.
- **D4 (baseline provenance, real, quantified).** `verifiers/corpus-baseline.json`'s new note claims
  the numbers were taken "over the round-99 candidate tree (base b53e209 + candidate patches in order
  ExecRedsR99, ScribeCorpusR99, ExecArmsR99)". They are the **ExecRedsR99-only** tree's: 203/174/72.
  The final full candidate measures **204 tracked / 175 report pointers / 72 commit citations** (my
  direct gate run at `b1e25510`), and the single-patch tree is 203/174/72 (my direct run at
  `bb827df4`). The same file keeps `measured_against.head = e03f9e22…` (round-87) and the round-87
  `head_subject`/`git_status` under a round-99 note. Minimal correction: name the ExecRedsR99-only
  tree, state that the L1 re-records at integration, and update the metadata fields with that
  re-record (204/175/72). The builder's own report corroborates the numbers and says "the L1's
  re-record must happen after all three patches" — i.e. the note's provenance sentence contradicts
  the builder's own reading, not just mine.
- **D5 (notice wording, minor).** The `SCORECARD.md:529` bullet reads `stale "…:30,37" corrected
  …round-80-verifier-spotcheck.md` without saying the subject is a **gate false red**
  (`strip_token_dressing` lacks the `:N,M` form, ScoutTipReds F5), not a content error. The plan
  discloses the gate defect; the durable notice does not. Minimal correction: append the
  parenthetical and re-pin that row's sha256.

## Tradeoffs (named, not defects)

- **T1 (equal-mode re-record).** At the landing, 3 of the 9 corpus checks are equal-mode counts that
  the landing's own baseline re-record sets; the substance is the 6 zero-mode checks (all 0 after
  the content fix) plus the checklist's 11 PASS and the independent gate. The gate bytes are frozen
  and the zero-mode checks are baseline-free, so "without weakening a gate" holds; the equal-mode
  conjunct is bookkeeping, not independent evidence.
- **T2 (correction rows vs in-place fixes).** 16 dead citations are excused by appended notices, not
  fixed at their sites (LOG.md/SCORECARD.md are append-only). The gate's PASS line self-describes
  the green (`19 recorded correction(s) excused`), and every corrected token resolves to the same
  artefact (Q64/M118 checked row by row). The residual is that a reader following a citation from
  its original site still needs the notice.
- **T3 (`:30,37` gate defect papered over by data).** The regex fix is routed to round 100; the
  correction row is the data workaround the plan authorizes.
- **T4 (round-98 C2 miss carried, not retried).** The plan carries the non-reproducible v6 refusal
  and the g16 hole to round 100 and spends this round's C2 on a different surface of the same
  sub-axis. Disclosed narrowing; the prior miss stays open.

## Risks (landing-level)

- **R1.** The L1's own round-99 `LOG.md`/`SCORECARD.md` append is inside C2's landing reading; one
  repo-rooted dead `.ufo/...` token there re-reds the checklist.
- **R2.** `check_assertion_floors.py` measured 202–279 s against the battery's 280 s cap under this
  wave's load; the landing's `tip battery exit 0: N of 6` row can read red with no gate wrong. C2's
  predicate reads only `guards 5 of 5`, so this is a landing no-harm risk, not a C2 predicate risk.
- **R3.** The C1 counter's rule 8 does not confine absolute paths: a mutant that drops `argv` falls
  through to the live fleet defaults and reads the host's 1219-file prompt directory during a
  scored run (MutTesterDispatchR99 F4, read-only). A counter bound, not a claim defect.
- **R4.** The full candidate's C2 MET depends on the L1's post-wave baseline re-record; the candidate
  I can name is not the landing the predicate scores.

## Evidence (commands and observed lines)

All commands from my scratch clone `$D=/fast/scratch/hyaku/kotoba-r99/CriticClaimR99/repo`
(`git -C "$D" rev-parse --show-toplevel` = `$D`), `HYAKU_SCRATCH`/`TMPDIR` under
`/fast/scratch/hyaku/kotoba-r99/CriticClaimR99`, counters invoked by absolute path from the lane.

| command | observed |
|---|---|
| `selftest-kills.py c1 52e8e95 "$D"` | `C1 targets killed 0 of 12 … C1-PREDICATE-UNMET` rc 1 — receipt identical to `redbefore-c1-base.txt` |
| `carried-reds.py 52e8e95 "$D"` | `C2 carried reds green 0 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` / UNMET rc 1 — identical to `c2-base.txt` |
| `carried-reds.py e8f2907c "$D"` (w1) | `green 2 of 3; self-tests held 1 of 3; frozen 2 of 4; guards FAIL` / UNMET rc 1 — identical to `c2-ctl-w1-stub-gates.txt` |
| `carried-reds.py 05f7bc9d "$D"` (w4) | `green 1 of 3; self-tests held 3 of 3; frozen 3 of 4; guards ok` / UNMET rc 1 — identical to `c2-ctl-w4-…txt` |
| `selftest-kills.py c1 104dae15 "$D"` (arms) | `C1 targets killed 12 of 12 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 12 of 12; code decoys held 12 of 12` / MET rc 0 |
| `selftest-kills.py c1 104dae15 "$D" --rules v5` | same tally / MET rc 0 |
| `selftest-kills.py r98c1|r97c1|r96c1 104dae15 "$D"` | 9 of 9, 13 of 13, 11 of 11 — all MET rc 0 |
| `critic_probe.py "$D" 104dae15` | 49 of 49 anchors count 1; one hunk inside `self_test`; `boxes proven 2`; `0 failure(s) over 154 assertions`; both counters frozen |
| `selftest-kills.py c1 a9e940c0 "$D"` (reds+arms) | 12 of 12 MET rc 0 |
| `carried-reds.py bb827df4 "$D"` (reds only) | `green 1 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` / UNMET rc 1 — the phantom round-99 row |
| `witness_r98.py 52e8e95 <lane>` | `witnesses: 19 DIFFERS`, n12 `SAME` — every c1 target has a differential witness |
| `curl -sS -L https://docs.python.org/3/library/argparse.html` | 200, 334994 B, sha256 `906919fd…` (twice identical); quote at HTML 992–993, 22 words; footer `Last updated on Nov 06, 2026 (13:47 UTC)`, `last-modified 13:49:15 GMT` |

## Bounds of this review

- I did not run the C2 forgery controls w2, w3, w5 (the pre-data receipts stand; w1 and w4, the two
  most discriminating, reproduce exactly).
- I did not re-run the round-98 witnesses for all 20 mutants; the harness reproduces 19 DIFFERS / 1
  SAME, which covers every c1 target.
- The full-candidate C2 reading depends on ScribeCorpusR99's patch; if it does not land before my
  poll window closes I report the single-patch readings and say so.
- No lane write, no fleet write, no git/jj mutation outside my scratch clone; the only commits are
  scratch-identity commits inside `$D`.

## S281 — does it ground t08? (page re-opened)

Re-opened `https://docs.python.org/3/library/argparse.html` with `curl -sS -L` on 2026-11-06:
HTTP 200, **334994 B**, sha256 `906919fda1b652a56d07a61823ce6e169ae6acfd2afa3233a56d3c26bf4e732e`
(two fetches identical). The quoted sentence is present at HTML line 992: `'append' - This appends
each argument value to a list.` + `It is useful for allowing an option to be specified multiple
times.` The instrument declares `--check` with `action="append"` (`verify_dispatch_prompts.py:527`,
read at the freeze), so `--check dispatch.04` appends exactly one value and selects exactly that
check — the t08 arm's expectation is grounded.

**But the recorded digest is not reproducible**: `receipts/sources-opened.txt` records
`bcd717f244b432fbee39f45742910347599f5f8b9f1dc6d4377a23c5c8faac16` at the same 334994 B, fetched
2026-11-06T13:41:12Z. The served page carries a volatile footer — `Last updated on Nov 06, 2026
(13:47 UTC)` — and `last-modified: Fri, 06 Nov 2026 13:49:15 GMT`: the page was rebuilt 6 minutes
after the L1's fetch, and the equal byte count is the equal-length date/time substitution in that
one line. So the row pins a build that no longer exists; a round-98-style discernment re-open
(digest equality) will read a mismatch and may be mistaken for a false access record. Minimal safe
correction: record the digest with its fetch time and state that docs.python.org rewrites the
"Last updated" footer (the quote line is stable), or re-open at landing and record the then-current
digest. The grounding of the arm is unaffected.

## Routed defects (round-98 closure) — disposition check

| # | routed defect | plan's disposition | my check |
|---|---|---|---|
| 1 | C2 non-reproducible refusal (v6 g11 rests on a `/dev/shm` marker) | **carried to round 100** with the g16 pristine-export hole; "a v7 counter is a rules change whose own controls need a full round" | disclosed narrowing: the calibration sub-axis's *own* failed claim is not retried; round-99 C2 is a different surface on the same sub-axis. Honest as disclosure, but the axis's prior miss stays open and the new C2 does not test it. |
| 2 | report line count +183 vs 182 | "correction in this round's report and LOG.md § Round 99" | **landed in the lesson as C99-1** (182 lines, `@@ -1333,0 +1334,182 @@`, with the two-file numstat); the L1's report still owes the same correction. |
| 3 | SCORECARD r98 C1 annotation names `63cd48d9` where the receipt measured `a060b450` | "appended correction in SCORECARD.md (append-only)" | **landed in the lesson as C99-2** (the named revision corrected, the value stands on byte-identical instrument bytes). The SCORECARD append itself is still an L1 act — verify at integration. |
| 4 | `/dev/shm/.r97-g11-run.*` leftovers | "no v6/v7 g11 world runs this round; the L1 lists any remaining markers" | confirmed: two markers remain (`/dev/shm/.r97-g11-run.5eifdezx` 10:19, `.r97-g11-run.6m2gtc69` 10:28); not attributable to this wave, not deleted. Honest. |
| 5 | S279 conditional denial (`CAP_SYS_PTRACE`) | "the round-99 lesson records the conjunct as a correction note" | **landed as C99-3** with the 16-word conjunct quote at HTML 1518–1520; I re-fetched ptrace(2) (104833 B, `69cd309e…`, identical to S279's digest) and the conjunct is real. |
| 6 | carried tip-battery reds | **this round's C2** | landed as the claim. |

## Risks (claim-level)

R1. The full candidate's C2 reading can drift from ExecRedsR99's baseline by ScribeCorpusR99's
`corpus/lessons/round-99.md` (+1 tracked file, +1 coverage row) and the S281 row; the L1 re-records
at integration, so the *candidate* I can name is not the *landing* the predicate scores. Observed
drift will be reported, not treated as an ExecRedsR99-only failure.
R2. The L1's own round-99 `LOG.md`/`SCORECARD.md` append is inside C2's reading
(`governance.citation_resolves` scans every line); one repo-rooted dead `.ufo/...` token there
re-reds the checklist at the landing (ConnectorOverlapR99 § 1.4).
R3. `check_assertion_floors.py` measured 193.8–204.0 s in my runs (226–278 s in the pre-data
controls) against the battery's 280 s cap under this wave's load; the landing's `tip battery exit 0:
N of 6` row can read red with no gate wrong. C2's predicate reads only `guards 5 of 5`, so this is a
landing no-harm risk, not a C2 predicate risk.
