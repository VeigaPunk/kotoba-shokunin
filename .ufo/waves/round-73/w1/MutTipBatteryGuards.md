# MutTipBatteryGuards — C3 counter guard mutation battery (round-73 wave 1)

**Verdict:** baseline `--self-test` of `verifiers/check_tip_battery.py` at base `072048f` **passes** (`self-test: 0 failure(s) over 42 assertions`, exit 0, ~2.0 s). 23 single-point mutants applied to scratch copies: **11 KILLED, 12 SURVIVED**. Every guard's happy path is wired, but the self-test has **no world** for: a gate timeout/absent script (tally channel), an abbreviated pin, git-environment failure inside a guard, a dropped floors row, a deleted/added spotcheck file, a deleted SKILL.md, a binary numstat row, or `main()`'s default fleet root — the exact line where M127 lived (`verifiers/check_tip_battery.py:610`). Those 12 survivors are the weaknesses the C3 redesign must close. Pristine bytes unchanged everywhere (sha256 below); lane tree untouched; scratch deleted.

## Axes
- **guard wiring** — does the mutated point change detector behavior? (killed = wired)
- **detector coverage** — which counter weaknesses the self-test cannot see? (survivor = coverage gap)

## Method (every command verbatim, outputs as observed)

Sandbox + pristine hash (base `072048fa8e8a52c707d25f7079772fa317244eb7`):

```
$ P=$(mktemp -d /tmp/k73fleet-MutTipBatteryGuards.XXXX)   # → /tmp/k73fleet-MutTipBatteryGuards.gPdj
$ for e in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.[!.]*; do
    n=$(basename "$e"); [ "$n" = kotoba-shokunin ] || ln -s "$e" "$P/$n"; done
$ git clone --shared -q --no-checkout /home/vgpnk/Projects/shokunin/kotoba-shokunin "$P/kotoba-shokunin"
$ git -C "$P/kotoba-shokunin" checkout -q 072048fa8e8a52c707d25f7079772fa317244eb7
$ git -C "$P/kotoba-shokunin" rev-parse --show-toplevel   # → .../kotoba-shokunin (equals $P/kotoba-shokunin)
$ git -C "$P/kotoba-shokunin" status --porcelain | wc -l  # → 0
$ sha256sum "$P/kotoba-shokunin/verifiers/check_tip_battery.py"
7e42ab552c6792211662567444fb55ad4ef05d5c3a82bd60aad54a8f03576301
$ git -C "$P/kotoba-shokunin" show 072048f:verifiers/check_tip_battery.py | sha256sum
7e42ab552c6792211662567444fb55ad4ef05d5c3a82bd60aad54a8f03576301   # worktree == base blob
```

Baseline (the one mandated run, in that sandbox):

```
$ cd $P/kotoba-shokunin && python3 -B verifiers/check_tip_battery.py --self-test
self-test: 0 failure(s) over 42 assertions          EXIT=0   (wall ≈ 2.0 s; Python 3.14.8, git 2.56.0)
```

Mutants: driver `w1/build/MutTipBatteryGuards/mutation_driver.py` copies the pristine bytes, applies **one** replacement each (asserted unique — a non-unique old snippet aborts that mutant with an error instead of a verdict), writes `w1/build/MutTipBatteryGuards/mutants/M<NN>.py`, runs `python3 -B mutants/M<NN>.py --self-test` (60 s cap each, 3 concurrent, all runs 1.6–3.5 s), verdict **SURVIVED iff exit 0 and `self-test: 0 failure(s)` in stdout**, else KILLED.

```
$ python3 -B .../build/MutTipBatteryGuards/mutation_driver.py \
    $P/kotoba-shokunin/verifiers/check_tip_battery.py .../build/MutTipBatteryGuards
# 23 rows printed (table below) + "pristine unchanged: True (7e42ab552c679221)"
```

## Result table (23 mutants, detector = self-test)

| id | point (file:line of pristine anchor) | verdict | exit | detector reading (last line) |
|---|---|---|---|---|
| M01 | `if deleted:` → `if not deleted:` (:246) | KILLED | 1 | `tip battery exit 0: 6 of 6` (deletion world no longer exits 1) |
| M02 | drop `p.startswith(GUARDED_PREFIXES)` (:235 area) | KILLED | 1 | `tip battery exit 0: 6 of 6` (corpus/ deletion undetected → world exits 0) |
| M03 | `LINE_CAP = 40` → `400` (:105) | KILLED | 1 | `tip battery exit 0: 6 of 6` (size+stub worlds stop failing) |
| M04 | drop BATTERY[0] entry (:127 area) | KILLED | 1 | `FAIL gate world verifiers/check_correction_sweep.py reads 5 of 6: tip battery exit 0: 4 …` |
| M05 | tally `if rc == 0:` → `if rc == 0 or rc is None:` (:377) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M06 | absent script recorded `None` → `0` (:334) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M07 | pin `if blob not in allowed:` → prefix match (:301) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M08 | spotcheck `elif rev_spot[path] != sha:` → `elif False:` (:315) | KILLED | 1 | `tip battery exit 0: 6 of 6` (edited spotcheck undetected) |
| M09 | `SPOTCHECK_RE` → `r"-NEVER-MATCH"` (:110) | KILLED | 1 | `tip battery exit 0: 6 of 6` (guard reads zero files) |
| M10 | swallow `git diff` failure (:285) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M11 | floors `new < old` → `new <= old` (:277) | KILLED | 1 | `self-test: 2 failure(s) …` (full run below) |
| M12 | dropped-row check → `if False:` (:270) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M13 | floors file absent → `rev_rows = {}` (:260) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M14 | pin loop `INSTRUMENT_PINS.items()` → `()` (:298) | KILLED | 1 | `tip battery exit 0: 6 of 6` (pin world stops failing) |
| M15 | absent base spotcheck → `pass` (:313-314) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M16 | exit drops `and not failures` (:384) | KILLED | 1 | `FAIL spotcheck world exits 1: exit 0` |
| M17 | `TOTAL = 6` → `5` (:103) | KILLED | 1 | `FAIL gate world … reads 5 of 6: tip battery exit 0: 5 …` (worlds flip to exit 0) |
| M18 | `GATE_TIMEOUT_S = 280` → `0` (:104) | KILLED | 1 | `tip battery exit 0: 0 of 6` (every gate times out → satisfying world fails) |
| M19 | `GUARDED_FILE` → `"Skill.md"` (:107) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M20 | binary numstat fail → `if False:` (:293) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M21 | added-spotcheck INFO → failure (:319) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M22 | absent instrument no longer a size failure (:282-283) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |
| M23 | main fleet default `repo.parent` → `repo.parent.parent` (:610) | **SURVIVED** | 0 | `self-test: 0 failure(s) over 42 assertions` |

Full M11 reading (re-run of `mutants/M11.py`, observed):

```
$ python3 -B .../build/MutTipBatteryGuards/mutants/M11.py --self-test
self-test: 2 failure(s) over 42 assertions
FAIL satisfying world exits 0: exit 1 stderr ''
FAIL pinned world exits 0 when the blob is unchanged: exit 1 ''     EXIT=1
```
The satisfying and pin-ok worlds hold floors **unchanged** (equal), so `<=` over-tightens and is caught — floors comparison strength is wired in both directions on the fixture's single row.

## Survivors — the 12 weaknesses the C3 redesign must close

1. **M05 — timeout/`None` exit counted as pass.** No fixture world makes a gate time out or die by signal, so the tally's `rc is None` branch is never exercised; treating a 280 s timeout as a green gate still reads 0 failures. This is precisely the plan's C3 shortcut control "raise the gate timeout / skip the failing gate in the counter" — its kill currently rests on nothing. *Close with:* a fixture gate that sleeps past a small cap, asserting the gate is **not** counted.
2. **M06 — absent battery script recorded as exit 0.** `run_battery`'s absent branch (:333-335) is never taken in any world; recording exit 0 there is invisible. *Close with:* a world that deletes one of the six scripts, asserting N < 6.
3. **M07 — pin compare weakenable to prefix.** Every fixture pin is the full 40-hex base blob, so exact vs `startswith` is indistinguishable on the fixtures. *Close with:* a pin world whose pin is an abbreviated sha that must NOT match the full blob.
4. **M10 — `git diff --numstat` failure swallowed.** The `EnvError` channel (:285-286) is only reachable via a corrupt sandbox; no fixture corrupts git state, so the size guards can silently read added=0/deleted=0. *Close with:* a world where the diff fails (e.g. unreadable object) and the counter must exit 2.
5. **M12 — dropped floors row invisible.** The self-test lowers a floor but never drops a row; the dropped-row branch (:270-272) is unpinned.
6. **M13 — floors file absent treated as empty.** `rev_rows is None` (:260) never fires in any world; a rev without `floors-registry.json` could be read as clean. (Over-tightening *is* caught — see M11.)
7. **M15 — absent base spotcheck treated as pass.** No world deletes a base spotcheck file; the `absent` branch (:313-314) is unpinned (the docstring's fallback to no-deletions is also never demonstrated).
8. **M19 — `GUARDED_FILE` name unpinned.** SKILL.md deletion is guarded by exact string (:107, :235); no world deletes SKILL.md, so the constant can rot silently.
9. **M20 — binary numstat row unpinned.** The "binary diff" failure (:293-294) never fires; a binary instrument would evade the line caps with no detector reading.
10. **M21 — added-spotcheck INFO promise unpinned.** The docstring promises added files are "reported as INFO, never a failure" (:75-78, :318-319); no world adds one, so a mutant inverting this to a *failure* (which would misfire on the round's own spot-check lesson landing at the tip) survives.
11. **M22 — absent instrument not a size failure.** The `absent` loop (:281-283) never fires; deleting an instrument script entirely is invisible to the self-test (distinct from M06: guard-side vs tally-side).
12. **M23 — M127-class: `main()`'s default fleet root untested.** `_drive` always passes `--fleet` (:433-434), so the default `fleet = … else repo.parent` (:610) — the exact line of the L1's M127 finding — is dead code to the self-test; mutating it to `repo.parent.parent` survives. *Close with:* a world that drives `main()` without `--fleet` (or with `--repo .`) and pins the resolved fleet root (e.g. via the sandbox construction it triggers).

**Pattern for the redesign:** the killed set shows every guard fires on its positive case; the survivor set shows the self-test has **no negative fixture for any environment-error channel and none for `main()`'s argument defaults**. The C3 counter rewrite should add, per guard, one "guard input corrupted" world (timeout, absent script, dropped row, missing floors file, deleted/added spotcheck, deleted SKILL.md, binary numstat, failed git call, abbreviated pin) plus one no-`--fleet` world — nine to eleven new worlds, each cheap (~0.2 s, stub gates).

## Restoration evidence

- Pristine sandbox file sha256 before == after the whole battery: `7e42ab552c6792211662567444fb55ad4ef05d5c3a82bd60aad54a8f03576301` (manifest fields `pristine_sha256_before/after`, `pristine_unchanged: true` in `mutation-manifest.json`).
- Live lane untouched: `cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git status --porcelain -- verifiers/check_tip_battery.py` → empty; `sha256sum verifiers/check_tip_battery.py` → `7e42ab55…` (identical at the moved tip `ac8fc595` too — the counter bytes the L1 has not touched).
- Mutants are separate files under `.ufo/waves/round-73/w1/build/MutTipBatteryGuards/mutants/` (23 files, per-file sha256 in the manifest); no committed lane file was written.
- Scratch removed: `rm -rf /tmp/k73w1-MutTipBatteryGuards.JnTm /tmp/k73fleet-MutTipBatteryGuards.gPdj` → both paths subsequently `No such file or directory`.
- Tooling: nothing installed or upgraded (host `python3 3.14.8`, `git 2.56.0` sufficed).

## Artifacts

- Driver: `.ufo/waves/round-73/w1/build/MutTipBatteryGuards/mutation_driver.py`
- Mutants: `.ufo/waves/round-73/w1/build/MutTipBatteryGuards/mutants/M01.py` … `M23.py`
- Manifest (diffs, hashes, exits, readings): `.ufo/waves/round-73/w1/build/MutTipBatteryGuards/mutation-manifest.json`
