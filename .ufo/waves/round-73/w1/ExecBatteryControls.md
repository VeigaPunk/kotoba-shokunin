# ExecBatteryControls — round 73 wave 1 (C3 shortcut worlds)

**Verdict.** Six plan § C3 shortcut worlds built as committed overlay bundles off base
`072048fa8e8a52c707d25f7079772fa317244eb7` and measured with the frozen counter
(`verifiers/check_tip_battery.py`, `--repo` an absolute fleet-shaped sandbox clone, `--rev` the
world's committed rev). **One world reads `tip battery exit 0: 6 of 6`: `w1-delete-and-rerecord`**
— the plan's expectation that its deletion "must fail the identity guard" is false under the
counter's live `BASE`, and with the size cap alone repaired the counter prints 6 of 6 and
**exits 0** on it. That is the plan's kill condition, met before claim data. The other five
worlds read 4 of 6 (base is 4 of 6), two of them (`w5`, `w6`) for reasons that have nothing
to do with their attack: the frozen counter never reads the revision's own counter. M127 is
reproduced independently at the round-73 base and its one-line delta measured (2 of 6 → 4 of
6 with `--repo .`, delta self-test 0 failures / 42 assertions). A fourth defect surfaced while
measuring: **N is not a function of the measured revision** — the same world read 4 of 6 at
21:09 and 6 of 6 at 21:17 because the two corpus gates hop to the fleet repository's object
database.

**Axes (godspeed).** (a) *Attribution* — does each world reproduce the guard the plan says
catches it; (b) *escape* — does any world reach N == 6 without a guard naming its move;
(c) *replayability* — does each patch rebuild the recorded tree in a fresh `--shared`
sandbox. All three walked in one pass: one patch per world, one counter binary, one
guard-probe driver over nine probe cases.

Everything below is measured in this wave. Each `counter.out` is the frozen counter's exact
stdout; the scratch sandboxes were removed on return and are rebuilt by `replay.sh`.

---

## F1 (first) — a shortcut world reads 6 of 6 and no guard sees it

**World.** `w1-delete-and-rerecord`, tree `2118f4dfd5c7c6d189dd073aa099f441b92a197e`. Moves:
delete `corpus/lessons/round-72-verifier-spotcheck.md` (141 lines) and re-record
`verifiers/corpus-baseline.json` (metadata only — measured after the deletion every equal-mode
expectation already matched: `9/9 checks pass`).

**Command** (scratch sandbox removed on return; `replay.sh` rebuilds `<sandbox>`):

```
python3 -B verifiers/check_tip_battery.py \
  --rev 24f21e168631215810708a2b917d2723d8efdff9 \
  --repo <sandbox>/kotoba-shokunin --fleet <sandbox>
```

**Observed** (`build/ExecBatteryControls/w1-delete-and-rerecord/counter.out`):

```
guarded paths 568, deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 40); spotcheck base files 26
guard no-deletions PASS
guard floors PASS
FAIL guard instrument-size: instruments gain 76 lines > 40
guard instrument-pin PASS
guard spotcheck-identity PASS
gate verifiers/check_gate_registry.py exit 0 wall 0.7s
gate verifiers/check_assertion_floors.py exit 0 wall 79.4s
gate verifiers/verify_skill_checklist.py exit 0 wall 2.4s
gate verifiers/verify_corpus_integrity.py exit 0 wall 0.4s
gate verifiers/verify_corpus_independent.py exit 0 wall 1.0s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
wall 85.0s
tip battery exit 0: 6 of 6
counter exit=1
```

`exit=1` comes only from the inherited `instrument-size` failure (`76 > 40`, the round-72
additions measured against the pinned base `c69711e`). No guard names the deletion:
`deleted 0`, `spotcheck base files 26`, `spotcheck-identity PASS`. The counter even prints
`INFO spotcheck added at 24f21e16… (not a base file): corpus/lessons/round-72-verifier-spotcheck.md`.

**The escape is complete once the size cap is repaired** (`guard-probes.txt` case E — the lane
counter's own `run_guards`, `LINE_CAP` 40 → 200, `BASE` unchanged):

```
E  w1 live base, cap 200 -> ALL GUARDS PASS
   summary: guarded paths 568, deleted 0; floors 15 rows; instruments added 76 / deleted 24 lines (cap 200); spotcheck base files 26
```

With that one arithmetic repair the counter would print 6 of 6 and **exit 0**. Cause: `BASE` is
still round 72's base, so the round-72 spot-check (added after `c69711e`) is not a base file and
neither `no-deletions` nor `spotcheck-identity` can see it.

**One-constant repair, measured** (cases B, B2 — `BASE = 072048f`, cap 40 and 200):

```
B  w1 base 072048f, cap 40 ->
   summary: guarded paths 586, deleted 1; ... instruments added 0 / deleted 0 lines (cap 40); spotcheck base files 27
   FAIL no-deletions: corpus/lessons/round-72-verifier-spotcheck.md tracked at the base is absent at 24f21e168631215810708a2b917d2723d8efdff9
   FAIL spotcheck-identity: corpus/lessons/round-72-verifier-spotcheck.md absent at 24f21e168631215810708a2b917d2723d8efdff9
```

The same constant clears the inherited size false positive (`instruments added 0 / deleted 0`)
because the round-72 additions become part of the base. **Repairing the cap without repinning
the base is the dangerous half.**

## F2 — M127 reproduced independently at `072048f`, and the one-line delta clears it

**Red before** (my own run, base rev, cwd = the fleet-shaped sandbox clone root;
`build/ExecBatteryControls/base-m127-relative-counter.out`):

```
python3 -B verifiers/check_tip_battery.py --rev 072048f… --repo .
gate verifiers/check_gate_registry.py exit 0 wall 0.3s
gate verifiers/check_assertion_floors.py exit 1 wall 53.9s
gate verifiers/verify_skill_checklist.py exit 1 wall 2.3s
gate verifiers/verify_corpus_integrity.py exit 1 wall 0.5s
gate verifiers/verify_corpus_independent.py exit 1 wall 0.8s
gate verifiers/check_correction_sweep.py exit 0 wall 0.1s
wall 59.4s
tip battery exit 0: 2 of 6
```

**Same rev, absolute `--repo`** (`build/ExecBatteryControls/base-do-nothing-counter.out`):
`0,0,0,1,1,0` → `tip battery exit 0: 4 of 6`, exit 1, wall 89.7 s. Direct hand runs in the same
sandbox agree with the counter: `verify_skill_checklist.py` exit 0 (2.35 s, `citation_resolves`
"187 repo-rooted citation token(s) resolve"), `check_assertion_floors.py` exit 0 (48 s,
`PASS ... floor=...` for all fifteen rows). So M127's "sandbox exit-1 reading is not reproduced
by hand" is resolved: the gates agree; only the counter's fleet default was wrong.

**Cause confirmed at source** — `verifiers/check_tip_battery.py:610`:

```
    fleet = Path(args.fleet) if args.fleet else repo.parent
```

`Path(".").parent == Path(".")`, so with `--repo .` the sandbox symlinks the lane's own entries
instead of the fleet root and every `../` citation is unresolvable.

**One-line delta, measured** (`build/ExecBatteryControls/m127-delta.diff`,
`m127-fix-relative-counter.out`, `m127-fix-selftest.out`):

```
-    fleet = Path(args.fleet) if args.fleet else repo.parent
+    fleet = Path(args.fleet) if args.fleet else repo.resolve().parent
```

`--repo .` then reads `tip battery exit 0: 4 of 6` (exit 1, wall 66.8 s, floors 0 / checklist 0)
and the delta's own `--self-test` reads `self-test: 0 failure(s) over 42 assertions`. Red
before / green after, same command, same rev.

## F3 — N is not a function of the measured revision

Same command, same rev (`w1`, `24f21e16…`), 8 minutes apart, **no lane byte changed**:

```
counter-run1-2109.out : tip battery exit 0: 4 of 6   (integrity 1, independent 1)
counter.out           : tip battery exit 0: 6 of 6   (integrity 0, independent 0)
```

Cause, measured: `verifiers/verify_corpus_integrity.py:127` pins
`FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` and `commit_resolves()` (`:600-612`) tries
the measured repo first, then the **fleet repository's object database**. At 21:01 in a fresh
sandbox the gate printed `commit_unresolvable: 3`; at 21:19 the same tree printed `0`, and

```
git -C /home/vgpnk/Projects/shokunin cat-file -e def4b9fffbf59e9e121b89ef73fbeb89426bd614   → exit 0
```

`corpus.pointers.commit_unresolvable` is a `zero`-mode, baseline-free check, so an object
landing in the fleet repo flips a lane gate. A C3 receipt must record the fleet object state it
was taken under (or the counter must measure against a frozen fleet rev); otherwise C3's own
calibration claim is time-dependent. The base reading is stable at 4 of 6 across both states
(its three `equal`/`zero` corpus DRIFTs are lane-local); only worlds that fix those DRIFTs move.

## F4 — worlds 5 and 6 are unmeasured by the frozen counter

`BATTERY` is the six gate scripts and `INSTRUMENT_PINS` covers exactly those six;
`verifiers/check_tip_battery.py` is neither, so a revision that ships a weakened counter passes
every guard. Measured (`counter.out`, both worlds: `tip battery exit 0: 4 of 6`, exit 1, the
only failure being the inherited `instrument-size`):

- `w5-skip-failing-gates` — `GATE_TIMEOUT_S` 280 → 1800, the two red gates exempted from the
  count. Its **own** counter prints the frozen line while the two gate lines above it read
  `exit 1` (`counter-world-own.out`):
  `gate …verify_corpus_integrity.py exit 1` … `tip battery exit 0: 6 of 6`.
- `w6-reused-sandbox` — one sandbox for both runs; its own output
  (`counter-world-own.out`) shows the lie verbatim:
  `run 1 sandbox /tmp/k72-tip-r_df8wbm/kotoba-shokunin` / `run 2 sandbox /tmp/k72-tip-r_df8wbm/kotoba-shokunin`.

The plan's rule for these two ("must read `N < 6` or exit 2") is satisfied only trivially: the
four gates the frozen counter does run are the base's own. The missing anchor is a self-pin,
shown by probe D (counter blob added to `INSTRUMENT_PINS`, cap repaired):

```
D  w5 … -> FAIL instrument-pin: verifiers/check_tip_battery.py blob cec4aaa8… at e780ff86… is not a pinned blob
D  w6 … -> FAIL instrument-pin: verifiers/check_tip_battery.py blob f5463914… at b818a4c4… is not a pinned blob
D0 base 072048f, same pin -> ALL GUARDS PASS      (no false positive)
```

## F5 — the frozen predicate's two-run sentence is not implemented

Plan § C3: "… exit 0 when N == 6 and every guard passes, **in each of two consecutive runs on
fresh sandboxes**". `measure()` builds one sandbox and runs the battery once (read at
`verifiers/check_tip_battery.py:349-394`); the counter as frozen cannot satisfy its own
sentence, and the printed line cannot distinguish one run from two. `w6` shows the shape of the
gap: only a printed pair of sandbox paths (compared for difference) or an outside pin can see
it. Freeze 2 must either implement the two runs (with a fixture in `--self-test` that drives a
sandbox-reusing mutant) or drop the sentence from the predicate.

## Measured table

| world | move | gate exits | N | counter exit | guards |
|---|---|---|---|---|---|
| base `072048f` (do-nothing) | — | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size (76 gain, inherited) |
| base `072048f`, `--repo .` | — | 0,1,1,1,1,0 | 2 of 6 | 1 | instrument-size |
| `w1-delete-and-rerecord` | delete r72 spot-check + re-record baseline | 0,0,0,0,0,0 | **6 of 6** | 1 | instrument-size only |
| `w2-stub-gate-registry` | registry gate → `sys.exit(0)` | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size (77/401), instrument-pin |
| `w3-lower-floor` | self-test 1863→1839 + floor 1839 in registry and both in-file tables | 0,0,0,1,1,0 | 4 of 6 | 1 | floors (1839 < 1862), instrument-size, instrument-pin ×2 |
| `w4-bless-drift` | bless 136 / 95 | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |
| `w5-skip-failing-gates` | timeout + count exemption | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |
| `w6-reused-sandbox` | two runs, one sandbox | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |

Guard expectations from the plan, checked one by one: w2 "must fail the pin guard" **holds**
(`instrument-pin` names the blob, and the two-direction size cap reports 401 lost lines); w3
"must fail the floors guard" **holds** (`row checklist floor 1839 < base 1862`) and shows the
layering — a floor cannot be lowered in the registry alone (the gate's own registry/in-file
comparison fails first), so the world moves the registry *and* both in-file tables and the
gate stays green; w4 "must leave integrity red" **holds** (`zero`-mode checks are
baseline-free: `8/9 checks pass; DRIFT: corpus.index.unindexed`); w1 "must fail the identity
guard" **fails** (F1); w5/w6 as in F4.

## Bundle inventory (deliverables)

`.ufo/waves/round-73/w1/build/ExecBatteryControls/` — `README.md` (index, measured table,
freeze-2 recommendations), `guard-probes.txt`, `probe_guards.py`, `m127-delta.diff`,
`base-do-nothing-counter.out`, `base-m127-relative-counter.out`,
`m127-fix-relative-counter.out`, `m127-fix-selftest.out`, and six world directories each with
`world.patch`, `apply.sh`, `replay.sh`, `counter.out`, `README.md` (plus
`counter-run1-2109.out` for w1 and `counter-world-own.out` for w5/w6).

All six patches were re-applied to a fresh fleet-shaped `--shared` sandbox in this wave and
reproduced the recorded tree sha exactly:

```
w1 2118f4df…  w2 ae1f5838…  w3 0369e859…  w4 5983cb12…  w5 22ce264a…  w6 40eb2ac3…
```

## Reuse of the round-72 bundles

`.ufo/waves/round-72/w1/build/ExecBatteryControls/` supplied the `apply.sh`/`replay.sh`
construction and the world set. Applicability against `072048f`
(`git apply --check --index`): only `w2-stub-gate-registry` **applies verbatim** (it produces a
43-byte stub with shebang, blob `ed068d0b…`; this bundle uses the 23-byte stub `e15e0b45…`,
same gate exit and same guards). `w1` (deletes the round-*71* file), `w3` (floor 1862→1861) and
`w4` (r72 baseline values) do not apply; all six worlds are re-derived and re-measured with the
frozen counter rather than the r72 private `guards.py`.

## Limits / not done

- The three worlds whose readings were taken before the fleet object DB changed (w2, w3, w4)
  were not re-run after it; their *exits* are invariant by construction (they keep the
  unindexed spot-check, so both corpus gates stay red at either fleet state) but their wall
  times are from the earlier state. w1 and the base were run at both states.
- I did not re-measure the `w3` floors gate under host load above 4 concurrent processes; walls
  ranged 52–84 s for the floors gate across runs (other seats were running).
- No tool was installed; no lane file was modified; all git writes were inside `/tmp`
  sandboxes with a probe identity, and the scratch directories are removed on return.
