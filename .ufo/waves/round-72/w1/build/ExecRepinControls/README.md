# C2 shortcut-control worlds — round 72, wave 1 (seat ExecRepinControls)

Base: lane `kotoba-shokunin`, branch `master`, rev `c69711ee08279609374d895bb0f3c8c18ccf15c9`
(the r71 non-author closure spot-check commit). Plan: `plans/round-72.md` § C2 (frozen at
`7b229a1889bd87d53902150d4f4658dc0c1117b6`).

Every world here is a **bundle**: an `overlay/` tree of complete files to copy onto a fresh clone
of the base, the same change as `world.patch` (verified `git apply --check` clean against the
base), `replay.sh` (the exact replay, sandbox and all), `replay.out` (what the shipped script
printed when it was last run) and `observed-pins.json` / `observed-surfaces.json` (the two
instruments' own `--json` output). Nothing here was run against, or written into, the lane tree;
each world is committed only inside a throwaway `git clone --shared` of the lane that sits in a
fleet-shaped `/tmp` parent.

## The six worlds

| world | plan item | what it does | pins | surfaces | ledger conjunct |
|---|---|---|---|---|---|
| `w1-repin-only` | (1) | baseline sha + both default binary paths only; OC-1…OC-6 and the census untouched | **3/3, exit 0** | **5/7, exit 1** | n/a (no ledger file) |
| `w2-ledger-all` | (2) | w1 + `verifiers/census-removals.json` ledgering **all 9** opencode classes | 3/3, exit 0 | 5/7, exit 1 | **FAILS** (ledgered 9, required 1) |
| `w3-stub-pinned` | (3) | w1 but the pinned opencode path is a **358-byte stub** inside the clone, its sha pinned | **3/3, exit 0** | 5/7, exit 1 | n/a (no ledger file) |
| `w3b-stub-full-ledger` | added | w3 + w2's ledger (stub **and** wholesale ledger) | **3/3, exit 0** | 5/7, exit 1 | **HOLDS** (9 == 9) |
| `w4-omp-mtime-stale` | (4) | pins `omp.real` (correct sha) but `omp_binary_mtime` at the round-47 value | **2/3, exit 1** (mtime DRIFT) | 5/7, exit 1 | n/a (no ledger file) |
| `w5-repin-plus-honest-ledger` | added (counter seat's ask) | w1 + the **honest one-row ledger** (`opencode:instructions/CONTEXT.md`) | **3/3, exit 0** | 5/7, exit 1 | **HOLDS** (1 == 1) |

Measured 2026-10-25 by replaying each shipped `replay.sh`; the `pins`/`surfaces` columns are the
instruments' own `pass`/`pass+fail` and `exit_code` from `observed-*.json`.

Each world reads below the frozen target (`pins OK k/3` with `k == 3`, `surfaces pass p of 7`
with `p == 7`, ledger exact) on at least one conjunct:

* w1 — **surfaces** (`p = 5`, `surfaces.opencode_extract` FAIL on the 2.1.4 bytes: 0 classes from
  7 rules; `surfaces.literal_present` FAIL: `CONTEXT.md` absent from the dump). It defeats the
  pins conjunct outright: a sha + path edit with zero re-derivation reads `pins 3/3, exit 0`.
* w2 — **ledger conjunct** (9 ledgered, 1 required) **and** surfaces.
* w3 — **surfaces** (extraction vacuity, 0 classes from 7 rules). It defeats the pins conjunct
  with a stub.
* w3b — **surfaces only**: every other conjunct holds.
* w4 — **pins** (`omp_binary_mtime` DRIFT, `delta_ns = 173397942086864`).

## Headline: a counter-design finding, measured

On the two instruments the plan's counter runs, **a 358-byte stub and the real 240 MB binary are
indistinguishable at the verdict level**:

1. The 7-check `(id, status)` vector of `verify_surfaces.py --json` is byte-identical for **all
   five worlds**: `jq -c '[.checks[]|{id,status}]' observed-surfaces.json | sha256sum` gives the
   same prefix `93cd5b3e29136d8c` for each. Only the `detail` text differs (w1 names 1
   unverifiable literal, w3 names 9), and nothing in the frozen predicate reads `detail`.
2. `observed-surfaces.json` for w1, w2 and w4 are **byte-identical** (`sha256 2afd5745a13675f3…`):
   the ledger file is read by neither existing instrument, so worlds 1 and 2 are the same
   measurement.
3. w3/w3b pin a 358-byte text stub and still read `pins 3/3, exit 0` — `check_substrate_pins.py`
   compares only the pinned sha and mtime, so it cannot tell a substrate from a stub.
4. On the stub's own dump the plan's ledger rule requires **all 9** base classes (every literal
   counts 0), so w3b's wholesale ledger **HOLDS** (`required 9 == ledgered 9`, exit 0 from
   `ledger-probe.py`).

⇒ **w3b fails the frozen predicate on `p == 7` alone.** The plan allows that target to be lowered
before data (Q45: "the target stays `p == 7` only if that census reaches 7"). If the wave-1 census
lowers it to 5, **w3b reads exit 0 with a 358-byte stub and a wholesale ledger** — a shortcut world
passing the counter, which is exactly what the kill rule forbids. Before any data, the counter
needs a substrate-identity conjunct that neither instrument supplies: for example that the pinned
opencode path's bytes are the live ELF (`~/.opencode/bin/opencode`, sha `ca9b3ee2…`, 240 416 944
bytes), or at minimum a size/ELF-magic floor on the pinned file, plus the dump's own sha recorded
in the receipt. Counting `pass` only is not enough.

Second-order finding for calibration: `check_substrate_pins.py` green is **not** evidence of
freshness — 4 of these 5 worlds read `3/3, exit 0`, including both stub worlds.

## Do-nothing control (mine, re-run)

`base-do-nothing/` — the base `c69711e` in the same fleet-shaped sandbox, both instruments at
their own default paths (no flags), which is how the counter runs them:

```
$ cd <sandbox>/kotoba-shokunin
$ python3 -B verifiers/check_substrate_pins.py --json      # exit 2
  {"pass":0,"fail":3,"exit_code":2}   # DRIFT omp sha, DRIFT omp mtime, UNREADABLE opencode
$ python3 -B verifiers/verify_surfaces.py --json           # exit 2
  {"pass":0,"fail":0,"exit_code":2,"error":"opencode binary not found: …/opencode-ai/bin/opencode.exe"}
```

So at the base the two instruments refuse to evaluate (`checks: []` on the surfaces side). The
plan's `DRIFT 3/3` row is the **flag-overridden** run (`--omp-binary omp.real --opencode-binary
~/.opencode/bin/opencode`), which I reproduced at the base too: `pins pass 2 fail 1 exit 1`,
`surfaces pass 5 fail 2 exit 1` — the same surface profile as w1/w2/w4.

## Running the frozen counter on a world

The counter must run while the world's sandbox exists: w3/w3b pin an **absolute** path into that
sandbox, so a deleted sandbox turns those worlds into UNREADABLE (exit 2), not into a verdict.

```
KEEP=1 .ufo/waves/round-72/w1/build/ExecRepinControls/w3b-stub-full-ledger/replay.sh
#   → prints "world commit: <sha>" and "sandbox kept at /tmp/k72fleet-replay-w3b.XXXXXX"
python3 -B verifiers/check_substrate_repin_v2.py \
    --rev <world commit> --repo /tmp/k72fleet-replay-w3b.XXXXXX/kotoba-shokunin
rm -rf /tmp/k72fleet-replay-w3b.XXXXXX
```

`replay.sh` runs that counter step itself whenever `verifiers/check_substrate_repin_v2.py` exists
in the lane (it did not exist while these worlds were built, so each `replay.out` records
`check_substrate_repin_v2.py absent in the lane; counter not run`). `--rev`/`--repo` are the flag
names modelled on `verifiers/check_opencode_repin.py`; if the counter's CLI differs, its own error
is the signal — no world depends on the flags.

Counter scores, measured by me on 2026-10-25 against `ExecRepinCounter`'s draft (each world rebuilt
with `KEEP=1 ./replay.sh`, then the counter run from the lane's `verifiers/`-sibling
`w1/build/ExecRepinCounter/check_substrate_repin_v2.py`):

```
$ python3 -B <build>/ExecRepinCounter/check_substrate_repin_v2.py --rev <world commit> --repo <sandbox>/kotoba-shokunin
w1-repin-only:          exit 1 — pins OK 3/3; surfaces pass 5 of 7; removal ledger 0 of 1 verified
w2-ledger-all:          exit 1 — pins OK 3/3; surfaces pass 5 of 7; removal ledger 1 of 9 verified
w3-stub-pinned:         exit 1 — pins OK 2/3; surfaces pass 5 of 7; removal ledger 0 of 1 verified
                        (FAIL substrate identity: opencode_binary_sha256 PASS on bytes that are
                        not the live opencode the counter dumped)
w3b-stub-full-ledger:   exit 1 — pins OK 2/3; surfaces pass 5 of 7; removal ledger 1 of 9 verified
                        (FAIL substrate identity, same text)
w4-omp-mtime-stale:     exit 1 — pins OK 2/3 (mtime); surfaces pass 5 of 7; removal ledger 0 of 1 verified
```

w2/w3/w4's exit lines are the counter seat's own re-measurement (relayed, not re-run by me); w1
and w3b are my own runs (their full output is in each world's `observed-counter.txt`). All exit 1.
The counter dumps the **live** `~/.opencode/bin/opencode`, never the tree's pinned path, so w3's
stub is caught by the identity fold. Residual risk, measured: a lowering of the target to 5
**alone** cannot green w1/w5 (the counter's row-count guard still sees 7 reported checks —
`FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 5 expected`, exit 1, run by me with a
throwaway `CHECKS_TOTAL = 5` copy). The reachable green-reading shortcut is the lowering **plus**
retiring the two failing checks (`surfaces.literal_present`, `surfaces.opencode_extract`) from
`CHECK_IDS` — a visible instrument change the floors gate can see (self-test assertion count), but
which the verdict vector cannot distinguish from honest work (w1/w5's 7-check `(id, status)`
vector is byte-identical, `sha256 93cd5b3e29136d8c…`); only `detail` differs. A lowering below 7
therefore still needs the detail-reading floor.

## `ledger-probe.py`

A standalone probe of **only** the plan's ledger conjunct (not the counter, which owns the frozen
predicate). It counts each base opencode class literal as a plain substring of a `strings -n 4`
dump and compares that exact set with `removals[].class_id` of a world's
`verifiers/census-removals.json`. Observed:

```
$ python3 -B ledger-probe.py --dump /tmp/k72-oc-strings.txt \
      --ledger w2-ledger-all/overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 1
… opencode:instructions/CONTEXT.md  literal CONTEXT.md  count 0  absent
FAIL ledgered but literal present: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, …
ledger conjunct FAILS                                   # exit 1

$ python3 -B ledger-probe.py --dump <stub strings dump> \
      --ledger w2-ledger-all/overlay/verifiers/census-removals.json
base opencode classes 9; ledgered 9; required 9
ledger conjunct HOLDS                                   # exit 0
```

and the honest minimal ledger holds on the live dump: a one-row ledger naming
`opencode:instructions/CONTEXT.md` alone gives `required 1`, `HOLDS`, exit 0. The live dump
(`/tmp/k72-oc-strings.txt`, sha256 `020fb253…`) counts `CONTEXT.md` 0, `AGENTS.md` 15,
`CLAUDE.md` 3, `instructions` 281, `https://` 1282, `<system-reminder>` 15 (substring counts;
the `grep -c -F` line counts are 0/13/3/145/827/14 — presence/absence agrees).

## Caveats

* Host-anchored: every reading names the substrate it measured (path, sha256, bytes, mtime). The
  omp pins are the r51 pins and still hold for `~/.local/bin/omp.real` (`85d9daf3…`, mtime
  `2026-10-21T20:37:24.615549837-03:00`); `~/.local/bin/omp` is now a 1 680-byte wrapper
  (`ed62a41e…`), which is the path drift the base pins catch as DRIFT.
* A rebuilt host binary is a different measurement, not a failure of these worlds: re-run
  `replay.sh`, which overwrites `observed-*.json` in place.
* Sandbox hygiene: `replay.sh` deletes its `/tmp/k72fleet-replay-*` parent on exit unless
  `KEEP=1`; all git writes are inside `$P/kotoba-shokunin`, whose `rev-parse --show-toplevel` is
  checked against `$P/kotoba-shokunin` before the first commit.
