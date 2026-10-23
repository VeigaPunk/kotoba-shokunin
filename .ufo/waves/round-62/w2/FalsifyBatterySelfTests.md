# FalsifyBatterySelfTests — round-62 wave 2 (falsify)

Seat `L1kotoba62.FalsifyBatterySelfTests`, 2026-10-23. Lane read-only; every mutation ran on
`/tmp` copies. Scope: attack the two new gates **as tests** — delete one assertion/arm each in
a copy and measure whether the gate's own `--self-test` or `verifiers/check_assertion_floors.py`
notices. One deletion per gate, plus the same deletion on the hardened working-tree bytes.

## Bytes measured

| gate | committed blob | working tree | note |
|---|---|---|---|
| `verifiers/check_erratum_absorption.py` | `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b` | same | identical at `e6da78b` and `3f911504` |
| `verifiers/check_routed_repairs_v2.py` | `de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7` | `604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d` | working tree carries an **uncommitted** wave-2 hardening (`git status` = ` M`); its receipt copy is modified too |

```
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
3f911504ce76d9ca186f297d6d4a9cd8ed77508a
$ git -C … show e6da78b:verifiers/check_routed_repairs_v2.py | sha256sum
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  -
$ git -C … show 3f911504:verifiers/check_erratum_absorption.py | sha256sum
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  -
$ sha256sum verifiers/check_erratum_absorption.py verifiers/check_routed_repairs_v2.py
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  verifiers/check_erratum_absorption.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  verifiers/check_routed_repairs_v2.py
$ git -C … status --porcelain -- verifiers/
 M verifiers/check_routed_repairs_v2.py
```

The seat was tasked against `de5e3471…` (the committed blob at both lane tips); both v2 byte
versions were attacked because the working tree is what will be integrated.

## Method

Sandbox: `git clone --shared <lane> /tmp/kotoba62-selftest-probe/lane` (HEAD `3f911504`, clean
checkout), pristine copies kept beside it. For each gate: hash -> delete one arm -> run
`--self-test` -> `diff` the full stdout+stderr against the pristine run -> in-process
differential probe -> restore -> re-hash -> re-run.

Baselines (a baseline failure would have been inconclusive; none occurred):

- absorption: exit 0, frozen C1 line + six survivor lines (pasted below).
- v2 committed: exit 0, `successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6`.
- v2 hardened: exit 0, same headline plus `CLI scorer-dependency` and `invariance controls`.

## Mutant A — `check_erratum_absorption.py`: isolation arm deleted

Deleted span (plan §C1 kill rule (iii), "each guard mutation must be shown to change exactly its
erratum's verdicts and no other class's (isolation arm)"):

```python
    for target in ERRATA:
        changed = run.mutations[target.name]
        for other in ERRATA:
            if other.name != target.name:
                require(verdicts(changed[other.name]) == verdicts(run.baseline[other.name]),
                        "%s guard mutation changed %s verdicts" % (target.name, other.name))
```

Before `afb4ff74…` -> after `6b8ec921cd1690c0f23eba86fd727a8dcd07b3dad520418ea20b588e835f150d`.

```
$ python3 -B verifiers/check_erratum_absorption.py --self-test   # mutant
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
mutant_exit=0
$ diff -u A-pristine.out A-mutant.out > A.diff; echo "diff_exit=$?"; wc -l A.diff
diff_exit=0
0 A.diff
```

The mutant's stdout+stderr is **identical** to the pristine run (0 diff lines) — the C1 receipt
line is reproducible from a gate with its plan-required isolation arm removed.

Isolation probe (`probe_isolation.py`; doctors exactly one off-diagonal observation — E2 under
the E2f mutation, both instances REJECT -> ACCEPT — and calls `summarize`):

```
pristine: REJECTED doctored run: E2f guard mutation changed E2 verdicts   (exit 3)
mutant:   ACCEPTED doctored run: measured=5 absorbed=2 surviving=6        (exit 0)
```

Lane-byte invocation for the pristine leg: `python3 -B probe_isolation.py
/home/…/kotoba-shokunin/verifiers/check_erratum_absorption.py` (read-only import of the pinned
counter beside it).

## Mutant B — `check_routed_repairs_v2.py`: base-world CLI assertion deleted

Deleted span (plan §C2 kill rule, "the self-test's base-world arm must print 0 of 6"):

```python
    if base_status != 1 or base_score != 0:
        failures.append(
            f"base CLI: exit {base_status}, score {base_score}; expected exit 1, score 0"
        )
```

| version | before | after | mutant `--self-test` | full-stream diff |
|---|---|---|---|---|
| committed | `de5e3471…` | `1de190cb878c71989ee2878c2c6ee186f0546d859687b31a3c9e96eddb51d719` | exit 0 | 0 lines (`v2-committed.diff`) |
| hardened (worktree) | `604ae4fb…` | `b8986da1b40aa2c6208b68c169512f01fbd5bda64a6d0187af6cbf0ad72a3b4f` | exit 0 | 0 lines (`v2-hardened.diff`) |

Headline after deletion, unchanged in both versions:

```
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
```

Base-regression probe (`probe_base.py`; the **first** `cli_measurement(BASE_REV)` returns a
3-of-6 base world, later calls real — the hardened gate also measures BASE_REV in its
scorer-dependency arm, so the fake is call-selective):

```
committed pristine: status=1 failures=['self-test: base CLI: exit 0, score 3; expected exit 1, score 0'] REJECTED (exit 3)
committed mutant:   status=0 failures=[] ACCEPTED (exit 0)
hardened pristine:  status=1 failures=['self-test: base CLI: exit 0, score 3; expected exit 1, score 0'] REJECTED (exit 3)
hardened mutant:    status=0 failures=[] ACCEPTED (exit 0)
```

In both mutant legs the printed headline is `base 3 of 6` **and the process exits 0** — the
printed line and the exit code disagree and nothing in the gate notices.

## Detector 2 — `verifiers/check_assertion_floors.py`: not registered (named bound)

```
$ python3 -B -c 'import json;d=json.load(open("verifiers/floors-registry.json"));names={v["path"].rsplit("/",1)[-1] for v in d["instruments"].values()};print("instrument_total",d["instrument_total"],"entries",len(d["instruments"]));[print(name,"in floors-registry.json =",name in names) for name in ("check_erratum_absorption.py","check_routed_repairs_v2.py","check_scoped_rules_v31.py")]'
instrument_total 14 entries 14
check_erratum_absorption.py in floors-registry.json = False
check_routed_repairs_v2.py in floors-registry.json = False
check_scoped_rules_v31.py in floors-registry.json = False
$ for g in check_erratum_absorption check_routed_repairs_v2; do printf "guard source mentions %s = %s\n" "$g" "$(grep -c $g verifiers/check_assertion_floors.py || true)"; done
guard source mentions check_erratum_absorption = 0
guard source mentions check_routed_repairs_v2 = 0
```

Full guard run **while both mutants were in place** (the tree that self-tested green above):

```
$ timeout 118 python3 -B verifiers/check_assertion_floors.py --repo . --load 1
PASS harness observed=10 floor=10
PASS corpus_integrity observed=152 floor=152
PASS corpus_independent observed=99 floor=93
PASS surfaces observed=175 floor=175
PASS checklist observed=1852 floor=1852
PASS pins observed=62 floor=62
PASS harness_independent observed=123 floor=123
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=165 floor=150
PASS dispatch_prompts observed=56 floor=56
PASS sibling_census observed=68 floor=68
PASS overlap_levers observed=55 floor=51
PASS alwayson observed=89 floor=89
PASS correction_sweep observed=25 floor=25
Wall time: 111.80 seconds
floors_exit=0
```

The two weakened gate files were never executed: the guard runs only its 14 registry rows, and
the registry contains neither gate. **No assertion-count guard covers these files.**

Registration is also blocked as written — the guard extracts a count with one of four patterns
and neither gate prints any:

```
$ python3 -B - <<'PY'   # load guard.INSTRUMENTS; re.search each pattern over each gate's --self-test stdout
import importlib.util, re, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("g", "verifiers/check_assertion_floors.py")
g = importlib.util.module_from_spec(spec); sys.modules[spec.name] = g; spec.loader.exec_module(g)
patterns = sorted({row[2] for row in g.INSTRUMENTS.values()})
print("guard ships %d distinct count patterns:" % len(patterns))
for p in patterns: print("  %r" % p)
for gate in ("verifiers/check_erratum_absorption.py", "verifiers/check_routed_repairs_v2.py",
             "verifiers/v2_committed_tmp.py"):
    r = subprocess.run([sys.executable, "-B", gate, "--self-test"], capture_output=True, text=True)
    print(gate, "exit=%d" % r.returncode, "hits=", [p for p in patterns if re.search(p, r.stdout)])
PY
guard ships 4 distinct count patterns:
  '(?m)^(\d+) failure\(s\) over (\d+) assertions$'
  '(?m)^(\d+) failures\n(\d+) assertions$'
  'self-test:\s*(\d+) assertions,\s*(\d+) failures'
  'self-test:\s*(\d+) failure\(s\) over (\d+) assertions'
verifiers/check_erratum_absorption.py    exit=0 count-pattern-hits=[]
verifiers/check_routed_repairs_v2.py     exit=0 count-pattern-hits=[]
verifiers/v2_committed_tmp.py            exit=0 count-pattern-hits=[]
$ grep -c 'assertion' verifiers/check_erratum_absorption.py verifiers/check_routed_repairs_v2.py
verifiers/check_erratum_absorption.py:0
verifiers/check_routed_repairs_v2.py:0
```

A row added without a count line would fail closed (`observed=0`). For contrast,
`check_scoped_rules_v31.py` already prints `self-test: 0 failure(s) over 201 assertions`, so it
is floor-ready — but it too is outside the registry.

## The planned v2 arm-count guard is absent

`.ufo/waves/round-62/w1-spec.json:325` asked for "(e) a `--self-test` arm-count guard" for
`check_routed_repairs_v2.py`. Both gates measure 0 for `arm.count|arm_count` and 0 for
`assertion`; the deletable assertion sites are: absorption `require(` x16, v2
`failures.append(` x17 (committed) / x22 (hardened).

```
$ for f in verifiers/check_erratum_absorption.py verifiers/check_routed_repairs_v2.py; do
>   printf "%-38s assertions=%s arm_count=%s\n" "$f" "$(grep -c 'assertion' $f)" "$(grep -ci 'arm.count\|arm_count' $f)"
> done
verifiers/check_erratum_absorption.py  assertions=0 arm_count=0
verifiers/check_routed_repairs_v2.py   assertions=0 arm_count=0
$ grep -c 'require(' verifiers/check_erratum_absorption.py
16
$ grep -c 'failures.append(' verifiers/check_routed_repairs_v2.py
22
$ git show HEAD:verifiers/check_routed_repairs_v2.py | grep -c 'failures.append('
17
```

Nothing pins those counts anywhere, so a deletion is invisible to the gate, to the floor guard,
and to any wrapper that reads exit codes.

## Verdicts

| probe | gate self-test | floor guard | verdict |
|---|---|---|---|
| A: isolation arm deleted | **not caught** (exit 0; byte-identical streams) | not registered | **survived** |
| B: base arm deleted (committed `de5e3471`) | **not caught** (exit 0; byte-identical streams) | not registered | **survived** |
| B: base arm deleted (worktree `604ae4fb`) | **not caught** (exit 0; byte-identical streams) | not registered | **survived** |

A surviving mutant is a coverage finding; the frozen predicates are not changed here.

## Findings for the L1

1. **HIGH — the two new gates are not self-verifying at the assertion level.** Removing a
   plan-mandated arm leaves stdout+stderr byte-identical and exit 0, so both receipts' headline
   lines (`errata measured 5 of 5; …` and `successor: … base 0 of 6; tip 6 of 6`) are label-
   reproducible from a weakened gate. The differential probes show the deleted arms are not
   redundant detectors: off-diagonal guard flips and a 3-of-6 base world are accepted only after
   deletion.
2. **HIGH — neither gate is in `verifiers/floors-registry.json`** (14/14 rows, 0 guard mentions).
   The floor detector passed a tree containing both mutants (exit 0, 111.80 s). This is the
   named bound the task allows; it is not a pass for assertion coverage.
3. **MEDIUM — registration cannot work until each gate prints an assertion count.** None of the
   guard's four count patterns matches either gate's output; a row added as-is would fail closed
   at `observed=0`. Adding the line + row (and the arm-count guard of w1-spec item (e)) is the
   smallest fix; v31 already prints `self-test: 0 failure(s) over 201 assertions`.
4. **NOTE — byte state moved under the seat.** The seat's first hash of the working tree showed
   `de5e3471` (matching the committed blob and the committed receipt `receipt_rev=3e7aed9b…`);
   a later hash showed `604ae4fb` plus a modified receipt, i.e. an uncommitted wave-2 hardening
   landed while this seat ran. Both versions were attacked; all share the same weakness for the
   base arm. Integration should keep the gate and its receipt on the same version.
5. **NOTE — downstream reruns inherit this blindness.** The wave-1 no-harm arm as specified
   (`ExecNoHarm62.md`: "If present, nonzero exit fails its arm") reads only the exit code, and
   the measured mutant exit is 0. [INFERENCE — the battery itself was not run by this seat.]

## Restoration evidence

All mutations were confined to `/tmp/kotoba62-selftest-probe`; nothing under the lane was
written except this report.

```
$ sha256sum lane/verifiers/check_erratum_absorption.py lane/verifiers/check_routed_repairs_v2.py
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  lane/verifiers/check_erratum_absorption.py
604ae4fb41779874eb420e8a904cb2ebdd953fa41dfc5f270ece53562b5c414d  lane/verifiers/check_routed_repairs_v2.py
$ python3 -B lane/verifiers/check_erratum_absorption.py --self-test | tail -1; echo "exit=${PIPESTATUS[0]}"
survivor E2f e2f-compound-purpose-outside-citation: []
exit=0
$ python3 -B lane/verifiers/check_routed_repairs_v2.py --self-test >/dev/null 2>&1; echo "exit=$?"
exit=0
$ sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_erratum_absorption.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py
afb4ff74…  …/verifiers/check_erratum_absorption.py
604ae4fb…  …/verifiers/check_routed_repairs_v2.py
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin status --porcelain -- verifiers/
 M verifiers/check_routed_repairs_v2.py
```

The sandbox's final state is the working-tree bytes of both gates (`afb4ff74…`, `604ae4fb…`),
each re-hashed and re-run green; the committed `de5e3471…` copy was separately restored and
re-run green before that step. The lane's ` M` entry is the mid-seat uncommitted hardening, not
a write by this seat: every mutation ran under `/tmp/kotoba62-selftest-probe`, and this report
is the seat's only lane write.

No tool installs or updates; commands used `python3` (system), `git` (system) and `diff`.
```
