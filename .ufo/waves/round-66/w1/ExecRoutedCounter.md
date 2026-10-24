# ExecRoutedCounter — r66 C2 routed-repairs counter (calibration)

Seat: ExecRoutedCounter (leaf executor, read-only measurements). Lane: kotoba.
Date: 2026-10-24. No production edit, commit, or change to any claim, counter, threshold, plan,
or receipt. The only file written is this report.

- Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855` (2026-10-24 03:24:36 -0300,
  "round-65 verifier spot-check (integrator, hyaku): non-author admit/reject").
- Observed lane tip (Git HEAD): `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (2026-10-24 04:26:20 -0300,
  "round-66 verifier spot-check (integrator, hyaku): non-author admit/reject"), parent `9e75e73`.
- jj working copy: `@` = `b0939bdc71d34cb7a43befa291ed3f89f98f807c`, parent `2a8eba56`; its changes are
  peer working-copy content only — `M .ufo/waves/round-66/w1/swarm-registry.json` plus untracked
  `w1/*.md` peer reports. The counter reads committed blobs (`git show <rev>:<path>`), so this
  working-copy state cannot influence any result below; worktree and sandbox-clone runs agree.

## Verdict (observations, not a closure ruling)

- **Pinned base is 0 of 2** — `D1-r65-registries-committed: FAIL`, `D2-corpus-integrity-reconciled: FAIL`,
  `r66 routed defects closed 0 of 2`, exit 1.
- **Landed tip is 2 of 2** — both checks PASS, `r66 routed defects closed 2 of 2`, exit 0, at
  `2a8eba56b3f9321b70c569fa2816d42237ca49a2` and at every measured revision from `4119647` through it.
- **Self-test: 0 failure(s) over 14 assertions**, exit 0.
- **Counter bytes are frozen**: sha256 `3129c0d7016467d93a3ea45a626dd1237bc92bd20d79bc09499c53c503293141`
  in the worktree and in the committed blobs at `fc1b71e` and `2a8eba5`; identical to the hash
  recorded in `controls/C2-counter-selftest.txt`.
- Two calibration boundaries are reported below and are **not** predicate failures of the frozen
  counter: (1) the D2 index arm is substring presence, not coverage-map row membership; (2) the
  counter's pins are landing-revision-scoped, so the primary integrity gate is green only at
  revisions before the round-66 spot-check lesson landed (`9e75e73`, `fc1b71e`) and red at the
  observed tip (`2a8eba5`) while the counter stays 2 of 2.

## Exact retained evidence

Command exactly as assigned, at the observed Git tip:

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r66_routed_repairs.py --rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2
control at 11385e04: 0 of 2
D1-r65-registries-committed: PASS
D2-corpus-integrity-reconciled: PASS
r66 routed defects closed 2 of 2
exit=0
```

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r66_routed_repairs.py --self-test
self-test: 0 failure(s) over 14 assertions
exit=0
```

Base control run (same frozen counter, base bytes):

```
$ python3 -B verifiers/check_r66_routed_repairs.py --rev 11385e04e368c1e94ab1a5a89d7439033eb1f855
control at 11385e04: 0 of 2
D1-r65-registries-committed: FAIL
D2-corpus-integrity-reconciled: FAIL
r66 routed defects closed 0 of 2
exit=1
```

Counter provenance: added at `e7d1d8c` ("round-66: freeze claims and controls"); **absent** at the
pinned base (`git cat-file -e 11385e04:verifiers/check_r66_routed_repairs.py` → absent). The before
control is therefore the frozen counter executed against base bytes, which is the counter's own
design (`BASE_REV_LITERAL`, lines 28–29).

## Revision map (counter, `--rev` each; read from committed blobs)

| Rev | Counter | D1 | D2 | Exit |
|---|---|---|---|---|
| `11385e04` pinned base | 0 of 2 | FAIL | FAIL | 1 |
| `e7d1d8c` freeze claims/controls | 0 of 2 | FAIL | FAIL | 1 |
| `806b53b` land G9 coupling + integrity | 1 of 2 | PASS | FAIL | 1 |
| `daedcdf` index lesson evidence | 1 of 2 | PASS | FAIL | 1 |
| `4119647` reconcile corpus baseline | 2 of 2 | PASS | PASS | 0 |
| `fc1b71e` align independent resolver | 2 of 2 | PASS | PASS | 0 |
| `9e75e73` record measurements | 2 of 2 | PASS | PASS | 0 |
| `2a8eba5` integrator spot-check (tip) | 2 of 2 | PASS | PASS | 0 |

D2 flips at `4119647` — the commit that re-records the baseline pins. D1 flips at `806b53b` — the
commit that lands both round-65 registry blobs.

## What the two checks observe at the tip (leaf-level)

**D1** (`check_d1` line 74; `tracked_nonempty_json` line 63): both
`.ufo/waves/round-65/{w1,w2}/swarm-registry.json` are absent at the pinned base and present at the
tip as nonempty JSON dicts — 12,844 B / 11,755 B, sha256 `a40abb1a…` / `d71ffed3…`, 6 keys each,
landed at `806b53b`. Non-vacuous: substituting `{}` for both fails D1 (probe B below).

**D2** (`check_d2` line 78): at the tip,
- `corpus/README.md` contains all four `lessons/round-6{2,3,4,5}-verifier-spotcheck.md` substrings —
  as table rows at lines 118–121; the same paths are absent from the base README (0 hits each).
- `verifiers/corpus-baseline.json` carries exactly the frozen pins — `corpus.index.tracked_files=118`,
  `unindexed=0`, `pointers.report_total=79`, `report_dead=0`, `commit_total=37`,
  `commit_unresolvable=0`, `commit_nonhash=0` — plus note key `round66_rerecord`.
- `verifiers/verify_corpus_integrity.py` contains the hop marker and real call sites:
  `inside_code_span` at line 321 (used at 523 in citation collection), `COMMIT_HOP_MARKER` at 588,
  `commit_resolves` at 591 with lane-first then fleet-root bodies, and a live
  `commit_resolves(hex_id` call at 665. The base integrity file contains none of these (no matches).
- The baseline, README, and integrity blobs are byte-identical between `fc1b71e` and the tip
  (`git diff --stat fc1b71e..2a8eba5 -- verifiers/corpus-baseline.json corpus/README.md
  verifiers/verify_corpus_integrity.py` → empty), so the 2-of-2 result at the tip is not a
  post-receipt re-pin.

Companion self-tests re-run for calibration (fresh, read-only): `verify_corpus_integrity.py
--self-test` → `0 failure(s) over 161 assertions`, exit 0; `verify_corpus_independent.py --self-test`
→ `103 assertions, 0 failures`, exit 0.

## Calibration boundary 1 — tip-state vs the plan's "final lane tree"

The plan's C2 after-predicate couples the counter to the primary gate: "Independently,
`python3 -B verifiers/verify_corpus_integrity.py` must exit 0 at the final lane tree." Measured in
pristine `/tmp` clones of each exact revision:

| Rev | `verify_corpus_integrity.py` | `verify_corpus_independent.py` |
|---|---|---|
| `806b53b` | 5/9, exit 1 — tracked 118, **unindexed 1**; DRIFT tracked/report/commit | not measured |
| `daedcdf` | 6/9, exit 1 — tracked 118, unindexed 0; DRIFT tracked 118/81, report 79/51, commit 37/32 | not measured |
| `4119647` | not measured | exit 1 |
| `fc1b71e` | **9/9, exit 0** | exit 0 |
| `9e75e73` | **9/9, exit 0** | exit 0 |
| `2a8eba5` (tip) | **5/9, exit 1** — tracked 119, unindexed 1 = `corpus/lessons/round-66-verifier-spotcheck.md`; report_total 82 vs 79; commit_total 38 vs 37; other zero-modes PASS | **exit 1**, unindexed DRIFT |

Mechanism: `2a8eba5` adds the 83-line closure spot-check lesson as a tracked corpus file and does
not index it or re-record the baseline; the counter still passes because it reads the committed
pins, not the tree. The same convention held at the pinned base, where the four r62–r65 spot-check
lessons were the unindexed set. So at the observed Git tip the counter half of C2 is met and the
plan's independent-gate half is not; at `9e75e73`/`fc1b71e` both are met.

## Calibration boundary 2 — falsification probes (`/tmp` clones of `2a8eba5`, deleted after use)

| Probe | Mutation (temporary commit) | Counter | Exit | Primary gate at mutant tree |
|---|---|---|---|---|
| A | Remove every README line containing `verifier-spotcheck` (rows for r46–r65 included), append one prose line naming the four pinned paths | **2 of 2** (D1 PASS, D2 PASS) | 0 | 5/9, exit 1 — **unindexed 22** |
| B | Both round-65 registries replaced by `{}` | 1 of 2, D1 FAIL | 1 | not measured |
| D | Baseline `corpus.index.tracked_files.expect = 119` (the tip's true observed count) | 1 of 2, D2 FAIL | 1 | not measured |

- A is a survivor of the D2 index arm: the assertion is `path in readme` substring presence
  (`check_d2`, line 78), so prose mentions certify the "indexed" requirement while the coverage map
  is broken for 22 tracked files.
- B and D are rejected as expected: the D1 blob arm requires a nonempty dict, and the pin arm
  rejects any count other than the frozen 118.

## Risks / limits

1. **Textual D2 index arm.** Probe A certifies a tree the primary gate scores 5/9. The frozen
   predicate is explicit about committed-byte pins, and the behavior arm is covered by the
   integrity gate's own 161 assertions and the independent gate's 103, but the counter alone cannot
   distinguish a table row from prose.
2. **Pins are landing-revision-scoped.** Probe D shows the frozen 118/79/37 cannot be re-recorded to
   the tip's observed 119/82/38 without D2 going FAIL. Once the round-66 spot-check lesson is indexed
   and the baseline refreshed, this counter scores 1 of 2 at that later tree. It certifies the
   landing revision, not an evergreen tree.
3. **"Final lane tree" is ambiguous against the observed tip.** Both clauses were observed true only
   at `9e75e73` and `fc1b71e` (lane-authored commits before the integrator spot-check); at
   `2a8eba5` only the counter clause holds. The L1/closure owns which revision the plan's wording
   binds.
4. **Self-test coverage gap.** The 14 assertions cover base 0 of 2, an honest 2 of 2, four kills
   (missing D1 blob, missing D2 index row, drifted baseline, no fleet hop) and two public entry
   points. They do not exercise the exit-2 refusal branches (absent base, absent `--rev`, pinned base
   scoring nonzero); only exit 0/1 paths were observed live.
5. No blocker. No installs or upgrades were needed; nothing was added to the host toolchain.

## Files changed

- `.ufo/waves/round-66/w1/ExecRoutedCounter.md` (this report) — only output.
- No lane commit, no production file, no sandbox retained (all `/tmp` clones removed).

**Confidence:** high on the exact outputs, revision map, byte freeze, and probe results (each
re-run or cloned at the named revision); high on the D1/D2 component observations; the two boundary
readings are measurements plus mechanism, with the closure ruling left to the non-author seat.
