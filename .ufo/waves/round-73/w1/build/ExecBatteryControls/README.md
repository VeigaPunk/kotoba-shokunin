# ExecBatteryControls — C3 shortcut worlds (round 73, wave 1)

Six committed overlay bundles for plan § C3 (the consistency claim: the tip battery counter
agrees with the hand run), built against base `072048fa8e8a52c707d25f7079772fa317244eb7`.
Each bundle is `world.patch` (base → world, `git diff` format), `apply.sh` (fleet-shaped
`--shared` sandbox + patch + commit **inside** the sandbox), `replay.sh` (apply + run the
frozen counter), `counter.out` (the frozen counter's own verdict), `README.md`.

Every patch was replayed into a fresh sandbox in this wave and reproduced the recorded tree
sha exactly (`apply.sh`, six for six): w1 `2118f4df…`, w2 `ae1f5838…`, w3 `0369e859…`,
w4 `5983cb12…`, w5 `22ce264a…`, w6 `40eb2ac3…`.

## Measured table

Gate order: `check_gate_registry --rev <rev>`, `check_assertion_floors`,
`verify_skill_checklist`, `verify_corpus_integrity`, `verify_corpus_independent`,
`check_correction_sweep --root .`. Counter run as
`python3 -B verifiers/check_tip_battery.py --rev <world rev> --repo <abs sandbox>/kotoba-shokunin --fleet <sandbox>`
(`counter.out` in each bundle holds the exact bytes).

| world | move | gate exits | N | counter exit | guards that fire |
|---|---|---|---|---|---|
| (base `072048f`, do-nothing) | — | 0,0,0,**1**,**1**,0 | 4 of 6 | 1 | instrument-size (76 gain, inherited) |
| (base `072048f`, `--repo .`, M127) | — | 0,**1**,**1**,1,1,0 | **2 of 6** | 1 | instrument-size |
| `w1-delete-and-rerecord` | delete r72 spot-check + re-record baseline | 0,0,0,**0**,**0**,0 | **6 of 6** | 1 | instrument-size only |
| `w2-stub-gate-registry` | `check_gate_registry.py` → `sys.exit(0)` | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size (77 gain / 401 lost), instrument-pin |
| `w3-lower-floor` | shrink checklist self-test 1863→1839 + floor 1839 in registry *and* both in-file tables | 0,0,0,1,1,0 | 4 of 6 | 1 | floors (1839 < 1862), instrument-size, instrument-pin ×2 |
| `w4-bless-drift` | bless `tracked_files` 136 / `report_total` 95 | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |
| `w5-skip-failing-gates` | counter copy: timeout 1800 + the two red gates exempted from the count | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |
| `w6-reused-sandbox` | counter copy: two runs on one sandbox | 0,0,0,1,1,0 | 4 of 6 | 1 | instrument-size only |

## Headline

**`w1-delete-and-rerecord` reads `tip battery exit 0: 6 of 6`.** Deleting
`corpus/lessons/round-72-verifier-spotcheck.md` and re-recording the baseline turns every one
of the six gates green, and **no guard names the move**: `no-deletions PASS`, `spotcheck-identity
PASS`, `deleted 0`, `spotcheck base files 26`. The counter's exit is 1 only because of the
inherited `instrument-size` failure (the r72 additions measured against base `c69711e`), and
`guard-probes.txt` case E shows that with the cap alone repaired the counter prints 6 of 6 and
**exits 0**. Under the plan's own kill rule the counter is wrong for this control as frozen.

Cause: the counter's `BASE` is still round 72's base. The r72 spot-check was added *after*
`c69711e`, so it is not a base file and the two guards that would catch its deletion cannot
see it (the counter prints it as `INFO spotcheck added at <rev> (not a base file)`).

One-constant repair, measured (probe B/B2, `guard-probes.txt`): `BASE = "072048f…"` makes the
world fire `no-deletions` **and** `spotcheck-identity`
(`…round-72-verifier-spotcheck.md tracked at the base is absent at 24f21e16…`), and at the same
time the `instrument-size` false positive disappears (`instruments added 0 / deleted 0`) —
because the r72 additions become part of the base.

## Findings beyond the world table

**F1 — M127 reproduced independently at the round-73 base, and the one-line delta clears it.**
From a fleet-shaped sandbox clone at `072048f`:
`--repo .` → `tip battery exit 0: 2 of 6`, exit 1, `check_assertion_floors` exit 1 (53.9 s) and
`verify_skill_checklist` exit 1 (2.3 s); the same rev with an absolute `--repo` → `4 of 6`, both
gates exit 0. Cause confirmed at source: `verifiers/check_tip_battery.py:610`
`fleet = Path(args.fleet) if args.fleet else repo.parent` — `Path(".").parent == Path(".")`, so
the sandbox links the lane's own entries instead of the fleet root and every `../` citation is
unresolvable. Delta measured in scratch (`/tmp/…/ctb_m127fix.py`, one line,
`repo.parent` → `repo.resolve().parent`): `--repo .` then reads `4 of 6` (wall 66.8 s) and the
delta's own `--self-test` reads `self-test: 0 failure(s) over 42 assertions`.

**F2 — N is not a function of the measured revision.** The same `w1` command read `4 of 6` at
21:09 and `6 of 6` at 21:17 with no lane byte changed (`counter-run1-2109.out` vs
`counter.out`). `verify_corpus_integrity.py:127` pins
`FLEET_ROOT = Path("/home/vgpnk/Projects/shokunin")` and `commit_resolves()` (`:600-612`)
falls back to the fleet repository's object database; three cited commits
(`def4b9f…`, `7b370d5…`, `1154d57…`) were absent from it at 21:09 and present at 21:19
(`git -C /home/vgpnk/Projects/shokunin cat-file -e def4b9fffbf59e9e121b89ef73fbeb89426bd614`
exits 0). `corpus.pointers.commit_unresolvable` is a `zero`-mode, baseline-free check, so it
flipped 3 → 0. A C3 receipt must record the fleet object state it was taken under.

**F3 — worlds 5 and 6 are unmeasured by the frozen counter.** `BATTERY` is the six gate
scripts and `INSTRUMENT_PINS` covers exactly those six; nothing reads
`verifiers/check_tip_battery.py`. A revision that ships a counter printing the frozen line with
two gates exempted (w5) or with both runs on one sandbox (w6) passes every guard and reads
4 of 6 for the trivial reason that the four real gates are the base's own. Probe D shows the
missing guard: with the counter's own blob added to `INSTRUMENT_PINS`,
`FAIL instrument-pin: verifiers/check_tip_battery.py blob cec4aaa8… / f5463914… is not a pinned
blob`, while the honest base under the same pin passes (`D0 ALL GUARDS PASS`).

**F4 — the frozen predicate is not implemented by the frozen counter.** Plan § C3's predicate
sentence requires "two consecutive runs on fresh sandboxes"; `measure()` builds one sandbox and
runs the battery once. A counter that reuses one sandbox (w6) prints the identical frozen line,
and the printed text cannot distinguish the two. If freeze 2 keeps the two-run sentence, the
counter needs a two-run loop plus a printed freshness check (e.g. `run 1 sandbox` /
`run 2 sandbox` paths that must differ), and a fixture in `--self-test` that drives a
sandbox-reusing mutant.

## Freeze-2 recommendations (arithmetic stated, each measured here)

1. `BASE = "072048fa8e8a52c707d25f7079772fa317244eb7"` (the round base).
   * Guards: at base and at every world, `instruments added 0 / deleted 0` against the round
     base (probe B, B2, C2), so the plan's owed Q65 sentence for `instrument-size` is "cap
     stays 40, measured against the round base; the r72 additions are base, the round's own
     instrument edits get the full 40 lines".
   * Guards: the r72 spot-check becomes a base file (`spotcheck base files 27`), so w1's
     deletion fires `spotcheck-identity` and `no-deletions` (probe B, B2).
2. Add `verifiers/check_tip_battery.py` to `INSTRUMENT_PINS` with the freeze-2 blob (outside
   anchor; no false positive on the honest base, probe D0). Catches w5 and w6 (probe D).
3. Either apply the M127 delta (`repo.resolve().parent`) or freeze the invocation as
   `--repo <abs> --fleet <fleet>`; the delta alone is measured to restore `4 of 6` under
   `--repo .` with its self-test green.
4. Record the fleet object state in every C3 receipt (F2), or run the two corpus gates against
   a frozen fleet rev, so `N` cannot move without a lane change.
5. If the two-run sentence stays, implement it (F4) instead of inheriting the single-run
   counter.

## Files

- `guard-probes.txt` — the counter's own `run_guards()` on nine probe cases (A, B, B2, C, C2,
  D, D0, E) with the sandbox built per probe.
- `probe_guards.py` — the probe driver (read-only; imports the lane counter by path).
- `<world>/` — the six bundles, each replayable with `sh replay.sh`.

## Reuse of the round-72 bundles

`.ufo/waves/round-72/w1/build/ExecBatteryControls/` supplied the `apply.sh`/`replay.sh`
construction (fleet-shaped `--shared` sandbox, patch + commit inside it) and the world set.
Reuse checked against the round-73 base with `git apply --check --index`:
`w2-stub-gate-registry` **applies verbatim** (it yields a 43-byte stub with a shebang; this
bundle uses the minimal 23-byte stub instead, same guards); `w1-delete-and-rerecord`,
`w3-lower-checklist-floor` and `w4-bless-drift` do **not** apply (they name the round-71/r72
files and the r72 floor and baseline values). All six worlds are therefore re-derived, and
their readings re-taken against the frozen counter rather than the r72 bundle's private
`guards.py`.
