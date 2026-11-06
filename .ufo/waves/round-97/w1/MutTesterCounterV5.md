# MutTesterCounterV5 — counter mutants V1–V9 against the v5 kill counter (C2 attack)

Seat: MutTesterCounterV5 (round 97, wave r97-w1). Leaf member; no subagent dispatch.
Lane repo (read-only for this seat): /home/vgpnk/Projects/shokunin/kotoba-shokunin
Scratch clone (the only writable repo): /fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5/repo
(`git rev-parse --show-toplevel` == that dir; base `148395bf42af97436b1b832a97a175515f981939`).
Scratch root: /fast/scratch/hyaku/kotoba-r97/MutTesterCounterV5 (HYAKU_SCRATCH + TMPDIR + HOME),
removed on exit.
Instrument under attack: `verifiers/fixtures/round-97/selftest-kills.py` (v5 counter), sha256
`b4200c5209b1c8a72bf0aaea0a191c1ba26dcf677db59e3b5163ee0ea3744fc7` at the freeze commit (matches
the pre-data receipt header `receipts/c2-v5.txt`). Detector: the committed C2 runner
`verifiers/fixtures/round-97/forgery-controls.py` (v5 mode) and the counter's own
`{c1|r96c1|r95c1}` tables. No lane file was written; no frozen byte was edited.

## Method

Each mutant is one scratch-clone commit (identity `scratch <scratch@invalid>`) whose only change is
`verifiers/fixtures/round-97/selftest-kills.py`; the lane is never touched. The mutant text is
extracted with `git show <rev>:<counter>` exactly as the runner does, compiled before use, and each
replacement anchor is asserted to match exactly once. A mutant is measured with the committed
runner's own `measure` step (build the committed round-96 world bytes, run
`counter r96c1 <world rev> <repo>`, read the predicate) for the g3/g7/g8 worlds and the g2b bound,
plus the honest h1 (801dd9bc instrument bytes) and h2 (r95c1 at the freeze bytes) and the c1 base
control (the redbefore receipt). One counter run at a time.

A control *exposes* a mutant when the mutant changes a reading from the pristine baseline: a verdict
flip (a world the baseline refuses becomes MET, or an honest world becomes UNMET) or a tally
deviation (killed/held/honest counts or the run-class lines differ). A mutant no committed control
exposes is a gap; the minimal new control world is named.

### Measurement substrate (stated, and validated against the committed receipts)

The counter's per-run world is a full-tree clone of the lane (19816 files, ~2.7 s per checkout), so
one committed-runner invocation is ~7 min per world on a host shared with 30+ seats. The instrument's
`--self-test` reads only the repo tree's `verifiers/` files and `SKILL.md` (`_proof_fixture_corpus`
builds its fixture corpus in TMPDIR; `box_proof` reads the proof tree in TMPDIR). The matrix
therefore runs the **same counter bytes** with the **same instrument bytes** against a slim scratch
repo (`slim/`, 532 files per commit: the whole `verifiers/` tree + `SKILL.md`, byte-identical per
rev). Each mutant is still measured by the committed runner's own `measure` step: `counter r96c1
<world rev> <repo>` with the committed round-96 world bytes (g3/g7/g8/g2b patches applied to the
679775ab instrument), the honest h1 bytes (801dd9bc instrument) and h2 (r95c1 at the freeze bytes),
plus the c1 base control at the freeze bytes.

Faithfulness check (before any mutant reading): the slim substrate reproduces the committed receipts
exactly — c1 base `C1 targets killed 0 of 13 ... C1-PREDICATE-UNMET` rc 1 (matches
`receipts/redbefore-c1-base.txt`), r96c1 base `killed 11 of 11 ... MET` rc 0 (matches
`poscontrol-r96c1-base.txt`), r95c1 base `killed 3 of 3 ... MET` rc 0 (matches
`poscontrol-r95c1-base.txt`), and the g3/g7/g8 worlds `killed 0 of 11; comment decoys held 11 of 11;
code decoys held 11 of 11` (matches `c2-v5.txt`), g2b/h1 `killed 11 of 11 ... MET`. A partial
full-tree run of the committed runner was also observed: g3 at the freeze read `killed 0 of 11 ...
UNMET` rc 1, the same line as the committed receipt, before the run was stopped (it would have
serialised ~30 min per mutant).

The first slim cut carried only the instrument + `SKILL.md`; the r95c1 table then read
`honest RUN-ERROR` (`AttributeError: 'NoneType' object has no attribute 'split'`) because
`check_mutation_battery.py` reads its live `verifiers/fixtures/mutation-battery/manifest.tsv` from
the repo. The substrate was widened to the whole `verifiers/` tree + `SKILL.md`, after which r95c1
reads `killed 3 of 3 ... MET`, matching the receipt.

## Mutant implementations (exact edits, each asserted to match exactly once)

| id | edit |
|---|---|
| V1 | removes both mirror job appends; `mirror = rf`; `k = blind == rf`; `pos = 1 if pblind == rf else 0` |
| V2 | `jobs.insert(rng.randrange(1, len(jobs)), honest); jobs = [honest] + jobs + [honest]` → `jobs = [honest] + jobs` (shuffle kept) |
| V3 | `shared = fresh_world("shared") if rules == "v4" else None` → `shared = fresh_world("shared")` |
| V4 | deletes the `if rules == "v5": env.update(HOME=..., XDG_CACHE_HOME=...)` block (TMPDIR stays fresh) |
| V5 | deletes `rng.shuffle(jobs)`; interior honest at fixed `len(jobs) // 2` |
| V6 | `cls_h = "CLEAN" if honest_clean == len(honest_runs) else next(...)` → `"CLEAN" if honest_clean >= 1 else "RUN-ERROR"` |
| V7 | deletes the `try/except UnicodeDecodeError` around `shown.stdout.decode("utf-8")` |
| V8 | both mirror job appends use `original` as the on-disk text (`("mirror", name, mt, original)`, `("pos-mirror", pname, pt, original)`) |
| V9 | `held_comment`/`held_code` count `!= "REPORTED-FAILURE"` instead of `== "CLEAN"` |

Scratch commits (slim substrate revs in `receipts/slim-revs.txt`; full-tree revs in
`receipts/mutant-revs.txt`): V1 `d1f89dad`, V2 `5b9110e7`, V3 `3f5d2f7b`, V4 `324c2ec5`,
V5 `6c92fb2b`, V6 `89c83b3a`, V7 `f9ca1fe6`, V8 `ee78cdd7`, V9 `9c6ef637` (full-tree clone).

## Results (measured; receipts under `receipts/matrix/` and `receipts/probes/`)

Baseline row (pristine counter, slim substrate): g3 `UNMET killed 0 of 11`; g7 `UNMET killed 0 of
11`; g8 `UNMET killed 0 of 11`; g2b `MET killed 11 of 11`; h1 `MET`; h2 `MET killed 3 of 3`; c1 base
`UNMET killed 0 of 13`, `mirror runs reported 1 of 14`, `honest runs CLEAN 3 of 3`; C2-equivalent
`forgeries refused 3 of 3; honest held 2 of 2` — the committed `c2-v5.txt` reading.

| mutant | C2 verdict | g3 world | g7 world | g8 world | g2b | h1 | h2 | c1 base | exposed? |
|---|---|---|---|---|---|---|---|---|---|
| V1-mirror-dropped | **UNMET (refused 2 of 3)** | **MET 11 of 11** | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13; **mirror 14 of 14** | **verdict flip (g3) + tally** |
| V2-bracket-first-only | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13; **honest 1 of 1** | tally only |
| V3-isolation-dropped | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET but **killed 11, honest 1 of 3, comment 0 of 11** | UNMET but **killed 11, honest 1 of 3, comment 0 of 11** | MET | MET | MET | UNMET 0 of 13 | tally only |
| V4-home-not-reset | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13 | **none** |
| V5-no-shuffle | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13 | **none** (run-log order only) |
| V6-honest-any | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13 | **none** |
| V7-unicode-uncaught | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13 | **none** (exit ladder only) |
| V8-mirror-original | **UNMET (refused 2 of 3)** | **MET 11 of 11** | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13; mirror 1 of 14 | **verdict flip (g3)** |
| V9-decoy-runerror-held | MET (3 of 3, 2 of 2) | UNMET 0 of 11 | UNMET 0 of 11 | UNMET 0 of 11 | MET | MET | MET | UNMET 0 of 13 | **none** |

The committed C2 predicate therefore kills **2 of 9** counter mutants (V1, V8, both through the g3
world); seven survive the verdict. The tally deviations expose V2 (honest `1 of 1` vs `3 of 3`) and
V3 (g7/g8: `killed 0 → 11`, `comment 11 → 0`, `honest 3 of 3 → 1 of 3`). V4, V5, V6, V7 and V9 are
invisible to every committed control.

V5's only signal is the run log: the pristine counter shuffles (base-c1 honest at runs 000, 011, 056
with a random job order; seed printed), V5 runs the fixed order (blind t01, mirror t01, blind t02,
mirror t02, …; honest at 000, 028, 056). No committed control checks the order.

## New control worlds (built on the round-96 freeze bytes in the scratch clone; measured)

| control | pristine counter | target mutant | reading |
|---|---|---|---|
| **g10-workdir-marker** — marker in the counter's per-invocation work dir (`Path(__file__).resolve().parents[4]`), outside the per-run dirs, r97-decoy aware | UNMET (killed 11, honest 1 of 3) | **V2** | **MET** (honest 1 of 1) — verdict flip |
| g10-workdir-marker | UNMET (honest 1 of 3) | **V6** | **MET** (honest 1 of 3, `any` holds) — verdict flip |
| **g9-home-marker** — marker in `$HOME`, r97-decoy aware | UNMET (killed 0, honest 3 of 3) | **V4** | UNMET (killed 11, honest 1 of 3) — tally deviation |
| **g7p-tmpdir-marker** — the committed g7 with `# r97-decoy` recognition | UNMET (killed 0, honest 3 of 3, comment 11) | **V3** | UNMET (killed 11, honest 1 of 3, comment 11) — tally deviation |
| **g11-blob-crash** — committed-blob compare, exits 3 on decoy texts | UNMET (killed 0, comment 0, code 0) | **V9** | UNMET (killed 0, comment 11, code 11) — tally deviation |
| **badutf8** — instrument with invalid UTF-8 at a rev | `C1-NOT-EVALUATED` rc 2 | **V7** | `UnicodeDecodeError` traceback rc 1 — exit-ladder exposure |
| **g12-blob-committed** — committed-blob compare, decoys held clean | UNMET (killed 0, comment 11, code 11) | — | negative: no verdict flip (see F3) |

## Exposure matrix (committed controls only)

| mutant | committed control | kind of exposure |
|---|---|---|
| V1 | g3 world; c1 base | verdict flip (g3 MET); tally (mirror 1 of 14 → 14 of 14) |
| V2 | c1 base (every run) | tally only (honest 1 of 1 vs 3 of 3) |
| V3 | g7 and g8 worlds | tally only (killed 0→11, comment 11→0, honest 3 of 3→1 of 3) |
| V4 | none | **gap** |
| V5 | none | **gap** (run-log order is not a control) |
| V6 | none | **gap** |
| V7 | none | **gap** (C2 worlds are valid UTF-8; the runner maps rc 1 and rc 2 alike) |
| V8 | g3 world | verdict flip (g3 MET); no tally change (mirror 1 of 14 both) |
| V9 | none | **gap** (no committed world produces a RUN-ERROR decoy) |

## Gaps and minimal new controls

- **V4 (HOME/XDG not reset)** — no committed control keys on HOME or XDG_CACHE_HOME (g7 keys on
  TMPDIR, g8 on the clone, both still fresh under V4). Minimal control: **g9-home-marker** (built):
  under v5 it is refused (killed 0, honest 3 of 3); under V4 the honest run writes the marker, the
  mutants fake-fail (killed 11) and the honest runs 2/3 fail (honest 1 of 3) — a tally deviation.
  A *verdict* flip additionally needs a blind-mutant detector (see F2), i.e. the disclosed g2b
  code-object sniffer with a HOME marker.
- **V5 (no shuffle)** — no committed control keys on run order. Minimal control: an **order-keyed
  forgery**: count runs in the shared work dir, read `verifiers/fixtures/round-97/selftest-kills.py`
  from the clone, reconstruct the fixed job list, and fake-fail exactly on the mutant/positive
  positions while staying CLEAN on honest/decoy positions. Under v5's shuffle the map is wrong and
  honest/decoy runs fake-fail (refused); under V5 the map is exact and it reads MET. (Described, not
  built — the only gap without a built control.)
- **V6 (honest `any`)** — every honest run is CLEAN in every committed world, so `any` and `all`
  agree. Minimal control: **g10-workdir-marker** (built): under v5 honest runs 2/3 fail (refused);
  under V6 `honest_clean >= 1` holds and it reads MET (verdict flip).
- **V7 (uncaught UnicodeDecodeError)** — the committed worlds are valid UTF-8 and the C2 runner maps
  rc 1 and rc 2 both to "not MET", so the exit ladder is invisible to C2. Minimal detector:
  **badutf8** (built): the pristine counter prints `C1-NOT-EVALUATED` rc 2; V7 raises an uncaught
  `UnicodeDecodeError` rc 1. This is a direct exit-ladder check, not a C2 world.
- **V9 (decoy RUN-ERROR held)** — no committed world produces a RUN-ERROR decoy. Minimal control:
  **g11-blob-crash** (built): under v5 the decoys are RUN-ERROR → `held 0 of 11` → refused; under V9
  `held 11 of 11` (tally deviation). A verdict flip additionally needs a mutant killer that survives
  v5 (the disclosed g2b sniffer) plus the decoy crash.
- **V2 (bracket first only)** — exposed by the c1 base as a tally only; **g10** (built) flips it.
- **V3 (isolation dropped)** — exposed by g7/g8 as a tally only; the r97-marker-aware **g7p**
  (built) still does not flip the verdict because the honest bracket catches the stateful marker
  (honest 1 of 3). A verdict flip needs the g2b bound.

## Findings

- **F1 — the committed C2 predicate is not mutation-adequate for its own rules.** It kills 2 of 9
  rule mutants (V1, V8, both via g3). Rules 5 (mirror) and 6 (honest bracket) are load-bearing, but
  no committed world exercises a non-CLEAN honest run, a RUN-ERROR decoy, an order-keyed forgery or
  the exit ladder, so V2/V4/V5/V6/V7/V9 survive the verdict. Next round should add g10 (V2/V6) and
  the order-keyed world (V5), and either add a decoy-crash world (V9) or state the decoy-held rule's
  bound.
- **F2 — the honest bracket is the decisive defense against state-based forgeries.** Every stateful
  marker (g7p, g9, g10-baseline) is caught by honest runs 2/3; a stateful forgery cannot flip the
  verdict under v5 unless it can distinguish a blind mutant from the honest run, and in both the
  on-disk text is the original. The only known blind-mutant detector is the disclosed g2b
  code-object sniffer, so the V4/V9 verdict flips require that bound. V2 and V6 are exactly the
  mutants that remove this defense (g10 reads MET under both).
- **F3 — the mirror rule is robust against static self-comparison, including the committed blob.**
  g3 (on-disk recompile) and g12 (`git show HEAD:` compare) both read `killed 0 of 11` under v5: in
  the blind run the on-disk text is the original, so the compare reads "equal" and the kill needs
  both runs. My prior hypothesis that the committed blob would beat the mirror was wrong — a useful
  negative result. No forgery that reads MET under v5 was found beyond the disclosed g2b bound.
- **F4 — the exit ladder is invisible to the C2 runner.** `measure` treats rc 1 and rc 2 alike; V7
  survives C2 and is only caught by a direct rc check (badutf8: rc 2 `C1-NOT-EVALUATED` vs rc 1
  traceback). If rule 7 is to be claimed, the runner must distinguish rc 2 from rc 1.
- **F5 — V3's refusal under v5 is overdetermined.** Under V3 the g7/g8 worlds move to `killed 11,
  comment 0, honest 1 of 3` but stay UNMET: the honest bracket and the decoy guard both catch the
  forgery. The plan's statement that the v5 refusal "does not depend on the marker" holds for the
  verdict; the *tally* does depend on the marker (comment held 11 under v5, 0 under V3).
- **F6 — V5 is unobservable by any committed control.** The only signal is the run-log order (fixed
  order and fixed honest positions 000/028/056 vs the pristine shuffle). The seed is printed but
  unused, so a reviewer can detect it by replaying two seeds and seeing the same order; no control
  asserts it.

## Evidence (commands and observed lines)

- `git clone -q --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin $D && git -C $D checkout -q
  148395bf…` → `git -C $D rev-parse --show-toplevel` = `$D`.
- `python3 -B build_mutants.py` → nine texts, each anchor asserted once, all compile.
- `python3 -B build_slim.py` → 532-file slim commits; `receipts/slim-revs.txt`.
- Validation: `counter c1 base97 $SLIM` → `C1 targets killed 0 of 13 ... C1-PREDICATE-UNMET` rc 1;
  `counter r96c1 base97 $SLIM` → `killed 11 of 11 ... MET` rc 0; `counter r95c1 base97 $SLIM` →
  `killed 3 of 3 ... MET` rc 0; g3/g7/g8 → `killed 0 of 11; comment 11; code 11` (all in
  `receipts/validate/`).
- Matrix: `bash run_all.sh` → `receipts/matrix/summary.txt` (the table above); per-mutant receipts
  under `receipts/matrix/<mutant>/`.
- Probes: `receipts/probes/` — g7p-baseline/V3, g9-baseline/V4, g10-baseline/V2/V6,
  g11-baseline/V9, g12-baseline/V1/V8/V3, badutf8-baseline/V7.
- Full-tree baseline partial: `receipts/c2-baseline-v5.txt` — `forgery g3-recompile-compare … rc 1
  R96C1-PREDICATE-UNMET | killed 0 of 11 …` (same line as the committed receipt).

## Risks / bounds

- The matrix ran on the slim substrate (same counter/instrument bytes, validated against every
  committed receipt). The full-tree committed runner was run end to end only for the g3 world before
  being stopped for time; the per-world readings are byte-for-byte the committed ones.
- The counter's mutant set is frozen, so killing it is not killing every mutant; the V4/V9 verdict
  flips are reachable only through the disclosed g2b bound, and V5's control is described, not
  built.
- The host is shared with 30+ seats; timings varied (r95c1 ~113 s, r96c1 ~4–13 s), but every reading
  is a verdict, not a timing.
- No tool installs were needed (stdlib + git + coreutils only). No lane file, frozen byte, or
  sibling seat's file was written.
