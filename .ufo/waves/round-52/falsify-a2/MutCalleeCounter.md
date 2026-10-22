Result: BREAKS — the C1 counter `check_callee_rename.py` kills 3 of the 4 named wrong implementations but survives the fourth (widened lookbehind) and one more I added; the survived mutants are caught by other gates (M4) or by NOTHING at all (M5).

# MutCalleeCounter — mutation testing of the round-52 C1 counter

Seat: `KotobaR52a2.MutCalleeCounter` (mutation-tester, leaf).
Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_callee_rename.py` (the frozen C1 counter) and the gate it measures, `verifiers/verify_surfaces.py`.
Judged revision: `c8407a453788df964df5a7b835dd0ce1360de882`.
Sandbox (mine, sole writer): `/fast/scratch/hyaku/kotoba-r52a2/MutCalleeCounter`, cloned from the lane and checked out at `c8407a4`. **No lane file was written by me.** The lane working tree still shows only the pre-existing attempt-1 `SCORECARD.md` diff plus sibling seats' in-flight edits (`verifiers/verify_surfaces.py` is dirty from `ReviewC1Diff`/`CriticC1Escape P4`, not from me).

Tooling: no install was needed or performed. Python 3.14 (system), `git` (system). No pacman transaction, no `uv tool install`, no network fetch.

## Method

For each mutation I edited **only** `verifiers/verify_surfaces.py` in the sandbox, committed it on a `mutants/*` branch, ran the frozen counter against that commit, and restored the bytes afterwards.

- Mutation point: `verifiers/verify_surfaces.py:512` (`admitted = ...` admission rule) and `:234-239` (`OMP_GENERIC_CALL_RE` / `OMP_CALLEE_MODE`).
- Detector: `python3 -B verifiers/check_callee_rename.py --rev <sandbox commit>`.
- Baseline (no mutation), to prove the detector is live and discriminating, and that a red baseline is not being read as a kill:

| revision | last line | exit |
|---|---|---|
| `c8579a4c5b48789e56fb9060ddd48f33569e1215` (round-51 base) | `callee-rename robust 0 of 4 fixtures` | 1 |
| `c8407a453788df964df5a7b835dd0ce1360de882` (judged head) | `callee-rename robust 4 of 4 fixtures` | 0 |

The head is 4 of 4 with exit 0 at seeds 52, 7 and 1234. The counter is a working detector; every kill below is a real kill, and every survival below is a real survival.

## The four named mutations

### M1 — revert to the round-51 callee allowlist — KILLED

`OMP_CALLEE_MODE = "declared"` → `"allowlist"` (line 239), i.e. extraction goes back to the round-51 per-harness callee list instead of the declared-pair admission rule.

```
rev: ad874758f4712a1c7e8360fe0be31fe5fdbb04ed
gate sha256: 07173a528678492be3d1a51f4653e134345937e9a1b1e540f90efc2f8f7b9550
strings-omp-clean.txt        control=[0, True] renamed=[1, False] planted=[1, False] robust=False map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[0, True] renamed=[1, False] planted=[1, False] robust=False map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[0, True] renamed=[1, False] planted=[1, False] robust=False map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[1, False] planted=[1, False] robust=False map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 0 of 4 fixtures
LAST: callee-rename robust 0 of 4 fixtures
EXIT: 1
```

Killed at every seed: seed 52 / 7 / 1234 → `0 of 4`, exit 1 each. The renamed arm fails because the renamed callees are no longer in the allowlist, so nothing extracts and the vacuity guard fires. **Holds.**

### M2 — admit every generic callee without declared pairs — KILLED

`admitted = {c for c, g, f in calls if (g, f) in declared}` → `admitted = {c for c, g, f in calls}` (line 512). Every callee of the generic shape is admitted, so the alias decoy `q(u, "evil", "EVIL.md")` now extracts.

```
rev: 0d360aa5ac9394b8fd2d37a9b3c4a6a8c27209b8
gate sha256: 81fc4848e7c208fc1374313bc3dd19ad5e9f49cd29c9626085be5374b6e9f91e
strings-omp-clean.txt        control=[1, False] renamed=[1, False] planted=[1, True] robust=False map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[1, False] renamed=[1, False] planted=[1, True] robust=False map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[1, False] renamed=[1, False] planted=[1, True] robust=False map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 1 of 4 fixtures
LAST: callee-rename robust 1 of 4 fixtures
EXIT: 1
```

Killed (exit 1) at every seed: 52 / 7 / 1234 → `1 of 4`, exit 1 each. The three fixtures carrying the `evil`/`EVIL.md` decoy go red; the 18.12.6 fixture has no decoy and stays green, which is why the score is 1 of 4 rather than 0. **Holds.**

### M3 — keep only declared pairs and drop new pairs — KILLED

`return {(g, f) for c, g, f in calls if c in admitted}` → `... if c in admitted and (g, f) in declared` (line 514). Declared pairs survive; a newly registered pair is silently dropped.

```
rev: 4eb02503b62b618bcdd6948223e348894ba7eea6
gate sha256: eca4c07bd9f01cfc3b2aabebb4112a877f527ab902afdac6596fcc7c18916cf9
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[0, False] robust=False map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[0, False] robust=False map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[0, False] robust=False map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[0, False] robust=False map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 0 of 4 fixtures
LAST: callee-rename robust 0 of 4 fixtures
EXIT: 1
```

Killed at every seed: 52 / 7 / 1234 → `0 of 4`, exit 1 each. The planted arm exits 0 (the planted pair is dropped, so nothing is uncovered) instead of the required exit 1 naming `omp:rnplant/RNPLANT.md`. **Holds.** This is the arm the plan names as the reason a declared-pairs-only rule cannot pass, and it works.

### M4 — widen the lookbehind to allow `.` — SURVIVED (BREAK)

`OMP_GENERIC_CALL_RE` lookbehind `(?<![A-Za-z0-9_$.])` → `(?<![A-Za-z0-9_$])` (line 235), i.e. a member call `this.foo(u, "grp", "FILE.md")` now matches the registration shape.

```
rev: a0ddb05f7b10a4324f003a72fda2f70dcd085523
gate sha256: b9a9bf618aaf51783976f41d17dd27565983a7109516360ee6731b4c081001ba
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'jDe': 'L6', 'Id': 'Ev'}
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'Dl': 'L6', 'I5': 'Ev', 'Co': 'U4', 'Gl': 'Wk', 'Mo': 'Gn'}
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'lq': 'L6', 'Xl': 'Ev', 'Fo': 'U4'}
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True map={'bq': 'L6', 'Kl': 'Ev', 'Ho': 'U4'}
callee-rename robust 4 of 4 fixtures
LAST: callee-rename robust 4 of 4 fixtures
EXIT: 0
```

Survived at seed 52, seed 7 and seed 1234 — all three print `4 of 4`, exit 0. The counter does not catch this mutation at all. **BREAKS.**

**Why the counter cannot see it (root cause, not a flake).** The counter's three arms are: control (fixture as committed), renamed (all 19 historical callees renamed), planted (renamed + one new pair by a renamed real callee). None of the three ever puts a **member call** in the fixture. The counter's own rename rule (`GENERIC_CALL_RE`, `check_callee_rename.py:79-82`) has the *same* tightened lookbehind `(?<![A-Za-z0-9_$])` and renames only bare callees, so no member-call site is ever produced. The 4 pinned fixtures contain **zero** member-call registration shapes — I scanned every `verifiers/fixtures/surfaces/*.txt` and found none. The counter therefore has no arm that can observe the difference between "the lookbehind forbids `.`" and "the lookbehind allows `.`".

**The mutation is a real defect, not a no-op.** With the widened lookbehind, the gate extracts a member call that the pristine gate does not:

```
member call 'o.x(u, "agents-md", "AGENTS.md");'
  pristine extract_classes -> []
  M4      extract_classes -> [('agents-md', 'AGENTS.md')]
```

And on an admitted callee it produces a **false red** on the live substrate's shape — injecting `this.<renamed admitted callee>(u, "evilgroup", "EVILFILE.md")` into the renamed fixture:

```
PRISTINE gate, member call on the RENAMED admitted callee:
  strings-omp-clean.txt    callee=L6   exit=0 ['PASS surfaces.no_uncovered_class: all 2 extracted loader class(es) declared']
M4 gate,      member call on the RENAMED admitted callee:
  strings-omp-clean.txt    callee=L6   exit=1 ['FAIL surfaces.no_uncovered_class: 1 loader class(es) undeclared in baseline: omp:evilgroup/EVILFILE.md']
```

So M4 turns a member call into a spurious "undeclared loader class" — the gate would go red on a real rebuild that used a method call. On today's omp 18.12.6 the harm is latent (0 member-call `.md` shapes in the 42 MB dump; 11 generic sites under both regexes; extraction identical at 8 pairs), which is exactly why a counter that never plants one cannot see it.

**Severity: MEDIUM, and the defect is caught elsewhere — but the C1 counter specifically does not catch it.** The gate's own self-test fails under M4, and the floors guard propagates that:

```
M4 self-test:            self-test FAIL: admission: member call not matched: got [('agents-md', 'AGENTS.md')]
                          1 failure(s) over 129 assertions          EXIT: 1
M4 assertion floors:     FAIL surfaces observed=129 floor=129 self_test_failures=1     EXIT: 1
```

The Q18 control arm (`admission: member call not matched`, `verifiers/verify_surfaces.py:1209-1210`) exists and fires. So the lane as a whole would not ship M4 silently — but the **C1 counter's own verdict is wrong**: it prints `4 of 4` for a gate that its own sibling self-test calls broken. A reader who trusts only `check_callee_rename.py` would believe M4 is a correct C1 implementation.

### M5 — admission keyed on the group only (added by me) — SURVIVED, CAUGHT BY NOTHING

Not on the assigned list; I added it because M4 exposed that the counter's fixture set has no *group-level* decoy either. `admitted = {c for c, g, f in calls if g in _dg}` where `_dg` is the set of declared groups — the file half of the pair is dropped from the admission test (line 512).

```
rev: 2109d54...
strings-omp-clean.txt        control=[0, True] renamed=[0, True] planted=[1, True] robust=True
strings-omp-newcallees.txt   control=[0, True] renamed=[0, True] planted=[1, True] robust=True
strings-omp-18.12.5.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True
strings-omp-18.12.6.txt      control=[0, True] renamed=[0, True] planted=[1, True] robust=True
callee-rename robust 4 of 4 fixtures
LAST: callee-rename robust 4 of 4 fixtures
EXIT: 0
```

Survived at seeds 52, 7, 1234. **Severity: HIGH — this one is caught by no gate in the repo.** Full battery, pristine vs M5:

| gate | pristine | M4 | M5 |
|---|---|---|---|
| `verify_surfaces.py --self-test` | exit 0, 0 failures / 129 | **exit 1**, 1 failure | exit 0, 0 failures |
| `verify_surfaces.py --json` (live) | exit 1 (pre-existing opencode drift) | exit 1 (same) | exit 1 (same) |
| `check_callee_rename.py` (seed 52) | exit 0, 4 of 4 | **exit 0, 4 of 4** | **exit 0, 4 of 4** |
| `check_callee_rename.py` (seed 7 / 1234) | exit 0, 4 of 4 | **exit 0, 4 of 4** | **exit 0, 4 of 4** |
| `check_assertion_floors.py` | exit 0 | **exit 1** | exit 0 |
| `check_substrate_pins.py` | exit 1 (pre-existing opencode drift) | exit 1 (same) | exit 1 (same) |
| `check_correction_sweep.py --rev HEAD` | exit 0 | exit 0 | exit 0 |
| `check_mcp_instructions.py --rev HEAD` | exit 0, 5 of 7 | exit 0, 5 of 7 | exit 0, 5 of 7 |

M5 passes the self-test (129/129), passes the floors guard, passes the counter at every seed, and produces a byte-identical live gate result to pristine. Yet it is a wrong implementation: it admits a callee whose pair is `(declared group, undeclared file)`, which the pristine rule rejects:

```
decoy 'q(u, "agents-md", "UNDECLARED.md");'
  pristine extract_classes -> []
  M5      extract_classes -> [('agents-md', 'UNDECLARED.md')]
```

and on the pinned fixtures it produces a **false red** on the 18.12.5 and 18.12.6 baselines:

```
PRISTINE gate, decoy (declared group, undeclared file):
  strings-omp-18.12.5.txt    exit=0 ['PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared']
M5 gate,      decoy (declared group, undeclared file):
  strings-omp-18.12.5.txt    exit=1 ['FAIL surfaces.no_uncovered_class: 2 loader class(es) undeclared in baseline: omp:agents-md/UNDECLARED.md, omp:evil/EVIL.md']
```

M5's harm on a live substrate: a benign helper that reuses a declared group with a new file would be reported as an undeclared loader class — a false red on a real rebuild. Today it is latent (no such site in the omp 18.12.6 dump; extraction identical at 8 pairs), and the counter, the self-test, the floors guard and the live gate all stay green. **This is the one finding here that no guard in the lane would catch.**

### M6 — hand re-pin the allowlist with the round-52 fresh names (added by me) — SURVIVES AT THE DEFAULT SEED, killed by the other two

The historical failure mode the C1 work exists to end: "each rename turned the freshness gate red until a round re-pinned a callee allowlist by hand" (`check_callee_rename.py:5-8`). I re-pinned `OMP_CALL_RE` by hand with the seed-52 fresh names `L6|Ev|U4|Wk|Gn` and set `OMP_CALLEE_MODE = "allowlist"`.

```
M6c seed=52    callee-rename robust 4 of 4 fixtures (exit 0)
M6c seed=7     callee-rename robust 0 of 4 fixtures (exit 1)
M6c seed=1234  callee-rename robust 0 of 4 fixtures (exit 1)
```

At the **default seed 52** this mutant is indistinguishable from a correct implementation: the counter prints `4 of 4`, exit 0, with every fixture `robust=True`. Only the two non-default seeds kill it, because the hand-pinned list happens to contain the seed-52 names. This is exactly the "no implementation hardcodes them" property the counter's docstring claims for `--seed`, and it is real — but it means **the counter's default invocation alone does not certify the C1 claim**; the claim needs the seed sweep to be meaningful. The plan's "After" text does say `4 of 4` also at `--seed 7` and `--seed 1234`, so the landed claim is stated correctly and the landed implementation does survive all three seeds. Severity: LOW as a defect of the landed work; MEDIUM as a statement about the counter's default run.

Note for honesty: my first two M6 attempts were **broken mutants** (a double-escaped `\\(` in the regex, which matched nothing and made the control arm red for the wrong reason). I caught that by checking *why* the mutant failed, rebuilt the mutation from the pristine pattern by patching one anchor inside it, verified the regex matches the clean fixture, and re-ran. The numbers above are from the corrected mutant. I am recording this because a mutant that fails for a spurious reason is not a kill.

## The sibling's in-flight repair does not close the gap

The lane's working-tree `verifiers/verify_surfaces.py` (sha256 `31c23d83e2d44cce4762eee6c0b64e4ce057c7b0685b73ce24a107cc93bcf560`, from `ReviewC1Diff` and `CriticC1Escape P4`) adds an empty-`declared` fallback and an unresolved-group admission arm. I stacked M4 and M5 on top of it (read-only on the lane; the mutation was written only to `/tmp`):

```
sibling pristine   member=[]                          groupdecoy=[]                         alias=[]
sibling+M4         member=[('agents-md', 'AGENTS.md')] groupdecoy=[]                         alias=[]
sibling+M5         member=[]                          groupdecoy=[('gemini', 'EVIL.md')]     alias=[]
```

and against the counter via `--root`:

```
sib      callee-rename robust 4 of 4 fixtures (exit 0)
sibm4    callee-rename robust 4 of 4 fixtures (exit 0)
sibm5    callee-rename robust 4 of 4 fixtures (exit 0)
```

So the repair neither closes the M4 nor the M5 gap, and the counter still passes both. **The L1's fix must not read the counter's `4 of 4` as evidence that the member-call and group-level decoy properties hold.**

## Pre-existing conditions on this host (not caused by any mutation here)

Two gates are red on the **pristine** judged revision, before any mutation:

1. `verify_surfaces.py --json` → exit 1, `surfaces.opencode_extract` FAIL: `opencode:instruction-context/AGENTS.md, opencode:read-hook/instructions` produced by no rule (OC-4, OC-6 unmatched). The **omp half of the same run is green**: `PASS surfaces.literal_present | 42 loader-kind entries verified`, `PASS surfaces.no_uncovered_class | all 8 extracted loader class(es) declared`. I confirmed this red is pre-existing by running the round-51 base gate (`c8579a4c`) — it fails identically (pass 6 / fail 1 / exit 1). So it is host drift, not a C1 regression.
2. `check_substrate_pins.py` → exit 1, `DRIFT 1/3 pins failed: opencode_binary_sha256`, expect `179ca421…` got `538fcb1b…`. Cause: the host's opencode moved from the pinned `opencode-ai` 1.19.3 to **1.19.4** (`/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/package.json` → `1.19.4`), and the npx cache now holds only that one version. The omp substrate is pinned and clean (`sha256 85d9daf3a05fc76e…` = the expected `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`).

The plan's no-harm guard says the live gate "stays `pass 7`, exit 0". On this host it is `pass 6, fail 1, exit 1` — for the opencode half only, caused by the 1.19.3 → 1.19.4 substrate drift, and identical at the round-51 base. The C1 (omp) half of that guard holds: both omp checks PASS. **The L1 should record this as a substrate drift against the "live gate pass 7" no-harm guard, not as a C1 failure** — the counter's own no-harm arms (`--self-test` 129/129, `check_substrate_pins.py`) are separately red for the same opencode reason.

## Restoration evidence

Sandbox restored to the judged revision, byte-identical:

```
$ git -C /fast/scratch/hyaku/kotoba-r52a2/MutCalleeCounter rev-parse HEAD
c8407a453788df964df5a7b835dd0ce1360de882
$ git -C ... status --porcelain          # (no output)
$ sha256sum verifiers/verify_surfaces.py
296aba902a4b8ec4a761b70f4fcff831c70e7d26b7e42d70324f80286c7d5476
$ git show c8407a45...:verifiers/verify_surfaces.py | sha256sum
296aba902a4b8ec4a761b70f4fcff831c70e7d26b7e42d70324f80286c7d5476  -
$ git diff c8407a45... -- verifiers/verify_surfaces.py --stat    # (empty)
```

Hash ledger for `verifiers/verify_surfaces.py` across the run:

| state | sha256 |
|---|---|
| pristine (`c8407a4`) | `296aba902a4b8ec4a761b70f4fcff831c70e7d26b7e42d70324f80286c7d5476` |
| M1 (allowlist mode) | `07173a528678492be3d1a51f4653e134345937e9a1b1e540f90efc2f8f7b9550` |
| M2 (admit all callees) | `81fc4848e7c208fc1374313bc3dd19ad5e9f49cd29c9626085be5374b6e9f91e` |
| M3 (declared pairs only) | `eca4c07bd9f01cfc3b2aabebb4112a877f527ab902afdac6596fcc7c18916cf9` |
| M4 (lookbehind allows `.`) | `b9a9bf618aaf51783976f41d17dd27565983a7109516360ee6731b4c081001ba` |
| M5 (group-only admission) | (mutant branch `mutants/M5`, commit `2109d54`) |
| M6c (hand re-pin) | (mutant branch `mutants/M6`, corrected) |
| restored pristine | `296aba902a4b8ec4a761b70f4fcff831c70e7d26b7e42d70324f80286c7d5476` ✓ |

Mutant commits are parked on sandbox branches `mutants/M1` … `mutants/M6` (never pushed, never in the lane). The lane repo and the lane `jj` state were never written by me; no `git add/commit/stash/checkout/switch/reset/pull/push/worktree` ran in the lane, and no `jj` command ran anywhere.

## Findings, with severity

| # | Finding | Severity | Where |
|---|---|---|---|
| F1 | The C1 counter does not detect a widened lookbehind (member calls now match). It prints `4 of 4`, exit 0, at all three seeds, for a gate that extracts member calls and can false-red on a real rebuild. | **MEDIUM** (defect caught by the gate's own Q18 self-test and the floors guard; the counter's verdict alone is wrong) | `verifiers/verify_surfaces.py:235` vs `verifiers/check_callee_rename.py` (no member-call arm, no fixture with one) |
| F2 | The C1 counter does not detect group-keyed admission (the file half of the pair dropped). Survives the counter at all seeds, the self-test (129/129), the floors guard, and the live gate. **No gate in the lane catches it.** | **HIGH** | `verifiers/verify_surfaces.py:512` |
| F3 | The counter's default seed alone does not certify the claim: a hand re-pinned allowlist containing the seed-52 fresh names passes `4 of 4` exit 0 at seed 52 and dies only at seeds 7 / 1234. The landed claim states all three seeds, so the landed work is fine; the counter's default invocation is not self-certifying. | **MEDIUM** (counter design), **LOW** (landed work) | `verifiers/check_callee_rename.py` `--seed` |
| F4 | The counter's fixture set carries no member-call shape and no group-level decoy, so two whole classes of wrong admission rule are unobservable to it. Root cause of F1 and F2. | **MEDIUM** | `verifiers/fixtures/surfaces/*.txt` (0 member-call `.md` shapes) |
| F5 | The sibling's in-flight repair (`ReviewC1Diff` / `CriticC1Escape P4`, lane working tree sha `31c23d83…`) closes neither F1 nor F2, and the counter still prints `4 of 4` for both. | **MEDIUM** | lane working tree `verifiers/verify_surfaces.py` |
| F6 | Pre-existing host drift: opencode moved 1.19.3 → 1.19.4 (sha `179ca421…` → `538fcb1b…`), so `surfaces.opencode_extract` fails and `check_substrate_pins.py` reports `DRIFT 1/3` on the pristine judged revision. The live gate is `pass 6, fail 1, exit 1`, not the plan's `pass 7, exit 0`. The **omp** half of the live gate is green (both checks PASS) and the failure is identical at the round-51 base, so it is not a C1 regression — but the plan's "live gate pass 7" no-harm guard cannot be reproduced on this host today. | **MEDIUM** (a guard the plan names is unreproducible on this host) | `verifiers/baseline.json:10`, `verifiers/check_substrate_pins.py` |

**Recommendation to the L1 (I do not edit lane files):** the C1 counter needs one more arm — a fixture or an injected member-call / group-level-decoy site — before its `4 of 4` can be read as evidence that the admission rule is the declared-pair rule and not a weaker approximation of it. Adding a member-call decoy to the pinned fixtures would make F1 observable by the counter directly, and a decoy that reuses a declared group with an undeclared file would make F2 observable. F3 argues the counter's certificate should always be read across all three seeds, never from the default run alone.

**Verdict on the judged work:** the C1 *implementation* landed at `c8407a4` is correct — it is the only one of the seven variants I built that passes the counter at all three seeds **and** the self-test **and** the floors guard **and** the live gate. The C1 *counter* is weaker than the C1 claim needs: of the four named wrong implementations, it kills three and misses one (F1), and I found a fifth it misses along with every other gate (F2). The claim as stated ("the extractor survives a pure callee rename") is true and demonstrated; the counter does not by itself establish that the *rule* is the declared-pair rule rather than a near-miss of it.
