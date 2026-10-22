# BoxProofGate — D2 gate half: the checklist gate runs each delegated instrument's `--box-proof` (round-50 build)

**Result: DELIVERED — `python3 -B verifiers/verify_skill_checklist.py --json` now runs every delegated
instrument's `--box-proof --map <map>` (the map under check) and exits 1 when that proof exits non-zero.
Patch: `/fast/scratch/hyaku/kotoba-r50/build/boxproofgate/patch.diff` (1 file, +212/−12). The L1 must bump the
checklist self-test floor 1845 → 1851 (the guard still passes at 1851 ≥ 1845: `PASS checklist observed=1851
floor=1845`).**

Run: 2026-10-22 (UTC clock as reported by the host). Private clone at
`/fast/scratch/hyaku/kotoba-r50/build/boxproofgate/kotoba-shokunin`, `rev-parse HEAD` =
`f30464660c675d1c1e2851a3bf0366a3aaffe5a8`. The lane checkout was not edited; the only file written there is
this report. No jj command, no git write command in the lane/fleet, no pacman/uv/npm install, no web source
opened, no fetched code executed.

## Where the gate lives, and why not in `check_assertion_floors.py`

The gate is inside the existing `checklist.box_map_complete` check of `verifiers/verify_skill_checklist.py`
(`check_box_map`), because that check is where a `delegated:<instrument>` disposition is already read, validated
and counted. `check_assertion_floors.py` is the wrong home: it re-runs each instrument's `--self-test` and
compares assertion counts; it never reads the box map, never resolves a `delegated:` target, and a floor bump
cannot express "the delegation must be proven". A separate new check id would also have to be registered in
every place that pins the checklist's check-id list; folding the proof into the existing check keeps the
surface, the floor registry and the `--json` schema untouched (11 checks before and after).

## What the gate does (the patch)

- `check_box_map` collects each distinct `delegated:` target that already passed the existing guards (target
  exists, is an instrument, stays inside the map's repo). It then runs the delegated instrument's own proof
  **against the map under check**: `<instrument> --box-proof --map <map-path>`, cwd = the map's repo, 120 s
  timeout, stderr/stdout captured.
- **Non-zero exit ⇒ the check is FAIL** and the detail names the instrument and its exit code, e.g.
  `delegated instrument 'verifiers/verify_dispatch_prompts.py' failed its --box-proof (exit 1): boxes proven 1`.
  A timeout or an unrunnable instrument is also a FAIL (fail-closed).
- **Support probe**: the instrument's `--help` output is probed for `--box-proof`. An instrument that does not
  advertise the flag is **not run** — today's behaviour is kept — and the detail says so:
  `delegated <target>: no --box-proof support (the --help probe does not advertise --box-proof), not run`.
  A delegated instrument that is not runnable at all (no interpreter for its suffix, no execute bit) is likewise
  not run, and the detail says `not runnable (no interpreter, not executable), not run`.
- `.py` instruments run under this interpreter with `-B` (no `__pycache__` written into the tree — verified:
  `git status --porcelain` shows only the patched file after the runs); `.sh`/`.bash` run under `bash`; anything
  else runs directly when it has the execute bit.
- The PASS detail keeps its old text and appends the proof outcomes, e.g.
  `41 boxes mapped (8 executed, 2 delegated, 31 unexecuted); delegated verifiers/verify_dispatch_prompts.py:
  --box-proof exit 0: boxes proven 2`.
- The map path reaches the check as a new `map_path` parameter (`main` passes the resolved `--map`), so the
  delegated instrument proves **the map this run is checking**, not a default of its own.

## Self-test arms (6 new assertions; the red arm is shown failing on the unpatched code)

New arms in `self_test()` build a temporary tree (`SKILL.md` + `verifiers/checklist-baseline.json` +
`verifiers/probe.py`), map one box `executed:` and one `delegated:verifiers/probe.py`, and run the CLI with
`--check checklist.box_map_complete`:

1. a stub that exits 1 under `--box-proof` ⇒ the check is **red** (exit 1, `FAIL checklist.box_map_complete:`);
2. the failing instrument, the flag and its exit code are **named** in the detail;
3. the same stub exiting 0 ⇒ the check stays **green**;
4. the proof run is stated in the detail (`delegated verifiers/probe.py`, `exit 0`);
5. an instrument without `--box-proof` support keeps **today's behaviour** (still green);
6. the skipped instrument is stated in the detail (`no --box-proof support`).

**Red before** (same file, the gate disabled — `delegated_box_proof` returning `("", None)`, i.e. exactly the
unpatched behaviour):
`python3 -B verifiers/verify_skill_checklist.py --self-test` → **exit 1**, `4 failure(s) over 1851 assertions`,
the four failures being arms 1, 2, 4 and 6 (arm 3 and 5 are green on the unpatched code because the check was
green anyway).

**Green after** (gate enabled): `--self-test` → **exit 0**, `0 failure(s) over 1851 assertions`.

## Evidence (commands with exit codes; cwd = the fleet-shaped clone root)

| command | exit | result |
|---|---|---|
| `python3 -B verifiers/verify_skill_checklist.py --json` (base `f3046466`) | 0 | `pass 11 fail 0 na 0` |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` (base) | 0 | `0 failure(s) over 1845 assertions` |
| `python3 -B verifiers/verify_skill_checklist.py --json` (patched) | 0 | `pass 11 fail 0 na 0`; `checklist.box_map_complete` detail now ends `…; delegated verifiers/verify_dispatch_prompts.py: --box-proof exit 0: boxes proven 2` |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` (patched) | 0 | `0 failure(s) over 1851 assertions` (+6 arms) |
| `python3 -B verifiers/verify_skill_checklist.py --self-test` (gate disabled = unpatched behaviour) | 1 | `4 failure(s) over 1851 assertions` (arms 1, 2, 4, 6) |
| `python3 -B verifiers/check_assertion_floors.py` (patched) | 0 | `PASS checklist observed=1851 floor=1845` (floor bump owed: 1845 → 1851) |
| `python3 -B verifiers/verify_dispatch_prompts.py --box-proof --map verifiers/checklist-baseline.json` | 0 | `boxes proven 2` (the instrument the gate now runs) |
| end-to-end red demo: a map whose `dispatch.04` disposition is mutated to `unexecuted:…` → `python3 -B verifiers/verify_skill_checklist.py --check checklist.box_map_complete --map verifiers/mutated-baseline.json` | 1 | `FAIL checklist.box_map_complete: evaluated 41 — delegated instrument 'verifiers/verify_dispatch_prompts.py' failed its --box-proof (exit 1): boxes proven 1` |
| `git apply --check -v patch.diff` on a fresh base clone, then apply and re-run `--self-test` | 0 / 0 | applies cleanly; `0 failure(s) over 1851 assertions` |

Base vs patched PASS/FAIL counts are identical (11 PASS / 0 FAIL / 0 N/A, exit 0) — the only change on the
live map is the appended proof outcome in the `checklist.box_map_complete` detail. The self-test assertion count
moves 1845 → 1851.

**Clone shape (a location artifact, not lane state):** a bare `git clone` of the lane is red for two reasons that
have nothing to do with this patch — the clone directory must be named `kotoba-shokunin`
(`trigger.name_directory`) and the fleet-root siblings `../.ufo`, `../PROTOCOL.md`, `../<lane>-shokunin` must
resolve (`trigger.citation_resolves`, `governance.citation_resolves`). I therefore cloned into
`…/boxproofgate/kotoba-shokunin` and symlinked every entry of `/home/vgpnk/Projects/shokunin` (including the
dotfile `.ufo`) into `…/boxproofgate/`. With that shape the base is 11 PASS / 0 FAIL and the patched tree is
11 PASS / 0 FAIL. (Same trap as the baseline seat's finding.)

## Risks and dependencies

1. **The gate inherits the instrument's pins.** `verify_dispatch_prompts.box_proof` requires the map entry's
   `disposition` to be exactly `delegated:verifiers/verify_dispatch_prompts.py` and its `text_sha256` to match
   `PINNED_BOX_SHA` and the live `SKILL.md` box hash. If any round-50 seat rewords the `dispatch.04`/`dispatch.08`
   checklist boxes, or edits the map's disposition, without re-pinning in the same step, this gate goes **red** —
   by design (a reworded box must be re-pinned), but the L1 must land the pin/map update with it.
2. **C2 interaction (different file, same round).** The C2 seat changes `verify_dispatch_prompts.box_proof` so
   that deleting a must-fail case makes it exit 1. No file conflict (I edited only
   `verifiers/verify_skill_checklist.py`), but once C2 lands this gate inherits the stricter contract: the proof
   must exit 0 on the intact tree and must fail when a case is missing. If C2 lands with a proof that is red on the
   intact tree, the checklist gate goes red with it — the L1 should land them in that order (C2 first, then this
   patch, or together with a green `--box-proof`).
   Measured by the C2 mutation seat (and confirmed by my own run of the instrument): at base the proof does **not**
   check fixture coverage — deleting any one of the 6 must-fail cases, or all 6 at once, still gives
   `boxes proven 2`, exit 0. So the gate I land makes the C2 contract *enforceable* but does not by itself enforce
   it: until the coverage-strict proof lands, my gate proves the map/pin half only. The two must land in the same
   step (instrument + manifest + this patch), because the stricter proof and the manifest are one change.
   Robustness of my side against a crashing proof: the gate reads the **exit code** as the contract; stdout is
   used only for a human-readable summary and its absence is harmless (an instrument that dies before printing
   `boxes proven N` exits non-zero, which my gate reports as a FAIL naming the instrument and the exit code — no
   parse failure, no traceback in the gate's own output).
3. **Subprocess cost.** Two extra subprocesses per delegated instrument (the `--help` probe and the proof); the
   live instrument's proof evaluates the 6 fixture cases (~1 s). Timeout 120 s, fail-closed on timeout.
4. **Stated ceiling of the support probe.** An instrument that accepts `--box-proof` but hides the flag from its
   help output would be skipped, not gated. The skip is stated in the detail string, never a silent pass.
5. The gate runs only when `checklist.box_map_complete` is selected (default: yes) and only when a map is loaded
   (a foreign target with no pinned map stays `N/A`); the delegated instrument receives the map under check, so a
   red-before run against a snapshot map proves against that snapshot's repo, not the live one.

## Not established / out of scope

- I did not touch `verifiers/checklist-baseline.json`, `verifiers/verify_dispatch_prompts.py`,
  `verifiers/check_assertion_floors.py` or `verifiers/floors-registry.json`: the floor bump (1845 → 1851, in the
  registry and in the guard's two in-file tables) is the L1's in-step step, and my seat owns one file.
- I did not run the other nine floored instruments against the patched tree beyond `check_assertion_floors.py`
  (which re-runs all ten self-tests and reported 10/10 PASS, `checklist observed=1851 floor=1845`).
- The C2 counter (6 of 6 must-fail cases killed) is not my claim; the round-49 spot-check records it at 0 of 6.

**Patch:** `/fast/scratch/hyaku/kotoba-r50/build/boxproofgate/patch.diff`
(`git -C …/kotoba-shokunin diff f30464660c675d1c1e2851a3bf0366a3aaffe5a8`; one file, no new files).
