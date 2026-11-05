# ExecCtlWorlds — the five declared D5 v3 controls + the v2-blindness receipt (executed before the freeze)

Seat: ExecCtlWorlds (executor, leaf; control author — the gate author is ExecD5Gate, per the
"the gate author must not be the control author" rule). Round 89, wave r89-w1. 2026-11-05.
Everything below was built from committed bytes in seat scratch; the lane was never modified except
this seat's owned paths (`.ufo/waves/round-89/w1/ExecCtlWorlds/`, `w1/CTL_READY`,
`receipts/ctl-*.txt`, `receipts/d5v3-base-receipt-draft.json`) and this report.

## Gate identity

`verifiers/check_r86_routed_repairs_v3.py` sha256 `1c110fb1fd9c7722d40e20d9dbe16b25f4bc1e00cfa41c889fe0a4e8924610f0`
= the `D5_READY` handoff content, byte-verified at run time. All gate runs: `python3 -B`, TMPDIR =
seat scratch, `--work` given implicitly via TMPDIR default `$TMPDIR`, git env sanitized
(`env -u GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES`).

## Base receipt (provisional, draft revision)

Written in a pristine shared clone checked out detached at `43fc7840202d542bcd1f5d7fab6e6f3dbb7f19b3`
(`git rev-parse --show-toplevel` asserted = the clone before anything):

    --write-base-receipt  ->  exit 0
    "base receipt written ... rev 43fc7840202d integrity a0b52d2419e2 baseline 6fdabfac8189; 9 names, 6 DRIFT"

Copied to `.ufo/waves/round-89/receipts/d5v3-base-receipt-draft.json` (sha256
`30ceec37d5fa6f7a16851a6e9df10fbe02173cbc4d7b1806ceb896e9ca3a4c40`). Receipt `root` field is the
bare clone path — location class matters, see F1. The L1 writes the freeze-revision receipt later.

## Worlds (deltas on the draft revision, one shared clone each, committed in scratch)

| world | head | delta |
|---|---|---|
| w_added_instance | `a6077cfad0badb37f8503ec77a59c45094e21b92` | one line appended to `corpus/lessons/round-88-verifier-spotcheck.md` citing 40-hex unresolvable `0123456789abcdef0123456789abcdef01234567` |
| w_silenced | `f3827eb836feb39fe074a87e3ee1c11edd1afaa7` | `CHECKS` drops `corpus.pointers.commit_nonhash` (integrity script edited in the world only; its `--self-test` still exits 0: `0 failure(s) over 178 assertions`) |
| w_rerecorded | `2b1d7821deb10a5e6f3d5846f59d1ad75eb27bf4` | `corpus-baseline.json` equal-mode expectations re-recorded to drifted live counts 172→177, 127→141, 59→61 (zero expectations untouched, per the baseline's own recorded practice) |
| w_healed | `bbae42fcd55307173a49ec418f0cf140888a44ce` | `corpus/lessons/round-81.md:8` dead citation `8b1cc1b00a9322cd8e231d87e015e1d75d20adc1` re-pointed at the resolvable round base commit `b284223105f4d106f7e8f56ed4fd296c643cda0e` (annotated in place; `cat-file -e <hash>^{commit}` rc 0 in the world) |
| w_tip | (no delta) | the pristine clone itself |

## Observed polarities (all five match the plan's declared expectations)

| world | exit | first failing leg | key detail |
|---|---|---|---|
| w_added_instance | 1 | **d5iii** | `instance growth under: ['corpus.pointers.commit_total 62>61', 'corpus.pointers.commit_unresolvable 2>1']`; instance drift 2; d5i/d5ii/snapshot PASS |
| w_silenced | 1 | **d5i** | `check names differ: missing ['corpus.pointers.commit_nonhash'], extra []`; snapshot_tampered also failing (`a0b52d2419e2` vs `a056345b485e`) — declared "d5i and/or snapshot_tampered" |
| w_rerecorded | 1 | **snapshot_tampered** | baseline digest `6fdabfac8189` vs `3e405f997313`; the re-record legitimately greens the three equal-count names (d5ii narrows 6→3) but cannot green the pinned snapshot |
| w_healed | 0 | — | `5 of 5`, instance drift 0; the healed red passes (d5ii narrows 6→5), no blanket refusal |
| w_tip | 0 | — | `5 of 5`, instance drift 0 |

Full outputs: `receipts/ctl-w_tip.txt`, `ctl-w_added_instance.txt`, `ctl-w_silenced.txt`,
`ctl-w_rerecorded.txt`, `ctl-w_healed.txt`. Equivalence: `receipts/ctl-equivalence.txt`.
v2 blindness: `receipts/ctl-v2-blindness.txt`. Raw probes: `w1/ExecCtlWorlds/evidence/`.

## v2-blindness receipt (the discrimination control)

- Frozen v2 `--self-test` (committed bytes): `1 failure(s) over 16 assertions`; the failing arm is
  `arm w_added_red (frozen control): an added unresolvable commit citation expects D5 FAIL via (ii);
  the names-set reads it as PASS (counter defect, see ExecMonotoneD5.md)`.
- Direct v2 run on the real w_added_instance world: readable (D1-D4 pass in the world), honest, and
  blind — `r86 routed defects closed 5 of 5`, exit 0. v2 sha256
  `10bd5508a7e5f8c18e994cf179274469bc6d9c4d28f6134b99b71e7998e58b82` (untouched).
- Same world on v3: exit 1 naming d5iii. The pair is the C2 discrimination evidence.

## Findings

**F1 — location flip confirmed and enlarged (Q79): exactly one name flips, and the gate cannot
express "could-not-evaluate" for it.** At identical draft bytes, `corpus.pointers.report_dead` reads
1 (DRIFT) in any bare clone and 0 (PASS) in a lane-shaped tree — the tracked symlink
`<root>/.ufo/reports/round-76/kotoba.md` escapes to the parent directory, so it dangles off the lane
(r88 ExecMonotoneD5 F2, re-measured at the draft revision; site `corpus/lessons/round-81.md:29`).
Everything else is location-stable (commit fleet hop is path-constant; the four `<rev>:<path>`
report sites resolve via the fleet repo). The plan's honest-bound red list (5 names) is the
LANE-shaped reading; a bare clone reads 6. Consequences for the freeze: (a) my provisional receipt
and all five worlds are bare-clone-measured — internally consistent, polarities clean; (b) the L1's
freeze receipt will be lane-measured (`report_dead 0`), and the landing tip measured in the lane
stays consistent — but any future BARE-CLONE world against that receipt reads `report_dead 1 > 0`
and v3 `compare()` will exit 1 naming d5iii, a false refusal, instead of the plan's
could-not-evaluate: the gate has no flip detector (receipt `root` field vs measured root path is the
reviewer hook, or worlds must be measured in a lane-shaped scaffold like the one I built at
`<scratch>/lane-shape/`).

**F2 — receipt-writer environment hazard (measured).** One probe of the same pristine bytes read
`commit_unresolvable 10 / report_dead 5` where the clean reading is `1 / 1` (both JSONs kept in
`evidence/`: `obs-pristine-draft.envpolluted.json` vs `obs-pristine-draft.json`). Direct git probes +
code read leave one mechanism class: a subprocess git-env override (GIT_DIR-class) in the probe
shell makes `git -C <fleet-root> cat-file` read the shell's own store instead of the fleet's — 9
fleet-resident citations and 4 `<rev>:<path>` sites silently misread. Every gate/receipt run after
the first used explicit `env -u` of the five GIT_* vars. Any receipt written under a polluted env
skews every d5 leg; the integrity/gate contract should state the env-sanitization requirement.

**F3 — assignment-vs-plan shape note on w_added_instance.** My dispatch said "a 41-hex garbage
hash"; the FROZEN plan's polarity is "added finding under already-red `commit_unresolvable` and
`commit_total` → exit 1 naming d5iii". A 41-hex token is not 7-40 hex, so it would land under
`commit_nonhash` (a NEW red name) and d5ii would fire before d5iii — contradicting the frozen
polarity. I used the 40-hex unresolvable shape (the r88 `w_added_red` fixture token), which is the
only reading consistent with the frozen predicate. Recorded, not resolved beyond that.

**F4 — equivalence HOLDS clone-vs-clone.** The two pristine clones produced byte-identical
observation dicts (doc digest `570f90ab16c188c291858161d2c79ea693857becbe612465780676971fb4903e`
both; zero key/value/result diffs) and clone2's gate verdict is `5 of 5, instance drift 0, exit 0`.
The Q79 discipline is satisfiable as specified within one location class; the open risk is only the
cross-class case in F1.

## Files written (lane)

- `.ufo/waves/round-89/receipts/`: `ctl-w_tip.txt`, `ctl-w_added_instance.txt`, `ctl-w_silenced.txt`,
  `ctl-w_rerecorded.txt`, `ctl-w_healed.txt`, `ctl-equivalence.txt`, `ctl-v2-blindness.txt`,
  `d5v3-base-receipt-draft.json`.
- `.ufo/waves/round-89/w1/CTL_READY` (the five observed polarities).
- `.ufo/waves/round-89/w1/ExecCtlWorlds/evidence/`: 10 probe artifacts (raw observations incl. the
  polluted/unpolluted pair, lane-shape observation, v2 outputs, silenced-world self-test, the
  equivalence output, base receipt copy).
- This report.

## Checks the main agent should run (not run by this seat)

- `sha256sum verifiers/check_r86_routed_repairs_v3.py` = `1c110fb1…` (= D5_READY) — gate unchanged
  since my runs; if the L1 amends the gate pre-freeze, my receipts must be re-run.
- `cat .ufo/waves/round-89/w1/CTL_READY` — the five polarities.
- Spot-check any polarity: clone the lane shared, checkout `43fc784`, copy the gate in, run
  `--write-base-receipt` then the world deltas above (recipes in receipts).
- Decide the F1 freeze shape: freeze receipt location class vs world measurement location class
  (lane-shaped scaffold vs bare clone), and whether v3 needs a flip-detection amendment routed
  through the kill rule BEFORE any candidate score.

Tooling: nothing installed or updated (no pacman, no uv, no binaries). Scratch
`/fast/scratch/hyaku/kotoba-r89/ExecCtlWorlds/` deleted before yield; receipts copied out first.

— ExecCtlWorlds
