# ExecRepinCounter — C2 frozen counter `check_substrate_repin_v2.py` (round 72, wave 1)

## Verdict

**Draft delivered; self-test green (`0 failure(s) over 16 assertions`); red on every world that
should be red.** The counter implements the frozen § C2 predicate as three conjuncts — pins
`k/3`, surfaces `p of 7`, removal ledger exact-set — with `BASE_REV`, `3` and `7` pinned in the file
and never read from the measured revision. All six shortcut-control worlds the controls seat built
read exit 1 through this counter, including the composite `w3b` that the frozen predicate alone
would have passed once the surface target is lowered.

Two changes landed after ExecRepinControls measured `w3b` against my first draft, both narrowing
false-green paths and neither adding a fourth conjunct to the frozen line:

1. the counter's own `strings -n 4` pass now reads **the live host opencode**
   (`~/.opencode/bin/opencode`), not the path the measured tree pins — the frozen sentence says the
   ledger answers "the live opencode dump";
2. `k` counts a pin as holding **only against the bytes the counter measured**: an opencode sha256
   row that PASSes because the tree pinned a stub's own sha is not a pin on the host substrate, so a
   stub world reads `pins OK 2/3` instead of `3/3`.

Not claimed: exit 0 on an honest re-pinned revision — none exists yet (the re-pin is ExecPinsRepin's,
the OC-1…OC-6 re-derivation is the OC seats'), so `p == 7` is unmeasured by anyone in this wave. My
green path is evidenced on the self-test fixture only.

## Deliverables

| path (relative to the lane) | what |
|---|---|
| `.ufo/waves/round-72/w1/build/ExecRepinCounter/check_substrate_repin_v2.py` | the counter draft; L1 installs it at `verifiers/check_substrate_repin_v2.py` |
| `.ufo/waves/round-72/w1/build/ExecRepinCounter/base-measurement.txt` | receipt: self-test, base run, all five control worlds, literal census |
| `.ufo/waves/round-72/w1/ExecRepinCounter.md` | this report |

No tracked lane file was touched by this seat: at the tip I measured (`e61fd29`, the L1's wave-1 spec
commit) `git status --porcelain` outside `.ufo/waves/round-72/` was empty, and `c69711e` is still
reachable (`git cat-file -e c69711e^{commit}` exit 0). Later in the wave, sibling seats' in-flight work
appeared in the live tree — `M verifiers/verify_surfaces.py` and other verifier edits plus untracked
`verifiers/census-removals.json` and `verifiers/fixtures/surfaces/strings-opencode-v2.1.4*.txt` and
friends. None of it is mine; I did not read, edit or stage it, and the set kept growing while I
finished, so I record its kind rather than a count. One
consequence worth stating: the untracked `verifiers/census-removals.json` is invisible to this counter,
which reads the `git archive` tree — an uncommitted ledger cannot satisfy the conjunct.

## What the counter does

For `--rev` it `git archive`s that revision's `verifiers` and `corpus` into a temp dir and, from that
tree:

- **P** runs `check_substrate_pins.py --json` with only `--json` — no path flag — so the tree's own
  `BINARIES` (`verifiers/check_substrate_pins.py:64`) and its own `verifiers/baseline.json` decide;
  `k` = rows that hold (a PASS row counts only if its expectation is the live opencode sha256).
- **S** runs `verify_surfaces.py --json` the same way, so `DEFAULT_BINARIES`
  (`verifiers/verify_surfaces.py:163`) and `DEFAULT_INVENTORY` (`:167`) come from the tree; `p` =
  checks with `status == "PASS"` out of `CHECK_IDS` (`:254`).
- **K** recomputes the ledger conjunct: every base opencode class at `c69711e` must be kept (same
  `class_id`, `literal`, `context_kind`, `verdict`) or listed in the rev's
  `verifiers/census-removals.json`; and the ledger must equal **exactly** the base classes whose
  literal the counter's own `strings -n 4` pass finds with count 0 in the live dump.

Output is the frozen line, then the measured substrate (`path`, `sha256`, `bytes`, `strings` lines),
because the counter reads installed binaries and its result must name the bytes it measured. Exit
ladder: 0 all conjuncts hold; 1 a measured conjunct fails (a row was reported and it does not hold);
2 cannot evaluate (extraction, missing instrument, **an empty instrument report**, unreadable ledger,
no readable live dump).

## Evidence 1 — self-test, 16 assertions, exit 0

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecRepinCounter/check_substrate_repin_v2.py --self-test
world 'satisfying': exit 0 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'satisfying, omp class dropped': exit 0 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'stale mtime': exit 1 :: host substrate re-derived: pins OK 2/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'surfaces red': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 1 of 7; removal ledger 1 of 1 verified
world 'present literal ledgered': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 2 verified
world 'absent class unledgered': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 0 of 1 verified
world 're-verdicted base class': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'extra pin row': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'extra check': exit 1 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'bad ledger': exit 2 :: cannot evaluate: verifiers/census-removals.json unreadable/unparseable: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
world 'no surfaces script': exit 2 :: cannot evaluate: gate or pin script missing at the revision
world 'satisfying again': exit 0 :: host substrate re-derived: pins OK 3/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'pinned bytes are not the live bytes': exit 1 :: host substrate re-derived: pins OK 2/3; surfaces pass 7 of 7; removal ledger 1 of 1 verified
world 'empty surfaces report': exit 2 :: cannot evaluate: verify_surfaces.py reported 0 row(s) (exit_code 2: fixture: no opencode dump); pins 3/3 row(s) PASS, surfaces 0/0 check(s) PASS
0 failure(s) over 16 assertions
```

Every world is a commit in one isolated `git init` fixture; `git -C $D rev-parse --show-toplevel` is
asserted equal to the fixture root before the first commit, and each world is rebuilt from the fixture
base commit (`checkout <base> -- .`, `clean -qfd`), so no world inherits another's edits. The fixture's
two instruments derive their verdicts from the fixture tree rather than from knobs: the surfaces stub
runs its own `strings -n 4` on the tree's dump and fails `surfaces.opencode_extract` when a declared
literal is missing; the pin stub hashes the tree's binary and compares the pinned ISO stamp.

Arms, and what each pins down:

- **satisfying** — exit 0 and the exact frozen line: the fixture dump lacks `CONTEXT.md`, the class is
  ledgered and retired, and the tree pins exactly the bytes the counter dumped.
- **one broken world per conjunct** — `stale mtime` (pins), `surfaces red` (six checks red while
  extraction stays green), `present literal ledgered` / `absent class unledgered` (exact set),
  `re-verdicted base class` (kept-identity: the ledger reads `1 of 1` and the exit code is 1 with the
  class named on stderr).
- **the three named must-fail arms** — a ledger that removes a class whose literal is present
  (`1 of 2`, class named), a ledger missing an absent class (`0 of 1`), a pin world with a stale mtime
  (`pins OK 2/3`).
- **the two post-review arms** — `pinned bytes are not the live bytes` (a pin on other bytes is not
  counted: `pins OK 2/3` plus the substrate-identity line) and `empty surfaces report` (an empty
  instrument report is exit 2, and the assertion checks the string `0 of 7` does **not** appear).
- **scope and vacuity** — dropping an `omp` class changes nothing (the conjunct is opencode-only); a
  4th pin row with 3 PASS and an 8th check with 7 PASS both exit 1; an unparseable ledger and a missing
  instrument are exit 2.

Q48: the self-test passes `--opencode-binary <fixture>` for every world, and `main()` short-circuits on
it before the host path is ever touched, so the self-test reads no host binary.

One fixture concession, named so nobody reads it as a host claim: `git archive` cannot carry a
filesystem mtime, so the pin stub compares the pinned stamp against a committed
`verifiers/fixture-omp.mtime` instead of `st_mtime_ns`. The counter never stats mtimes itself — that is
`check_substrate_pins.py`'s job — so nothing in the counter's logic depends on the concession.

## Evidence 2 — the base rev

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecRepinCounter/check_substrate_repin_v2.py --rev c69711ee08279609374d895bb0f3c8c18ccf15c9
cannot evaluate: verify_surfaces.py reported 0 row(s) (exit_code 2: opencode binary not found: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe); pins 0/3 row(s) PASS, surfaces 0/0 check(s) PASS
exit=2
```

The base tree's `verify_surfaces.py` answers `{"checks": [], "exit_code": 2}` because its default
opencode path is the deleted npx `opencode.exe` — the same fact `receipts/base-outputs/verify_surfaces.out`
records (`ERROR opencode binary not found: …opencode.exe`). ExecRepinControls raised this against my
first draft, which printed `surfaces pass 0 of 7` from that empty report; I re-measured, agreed, and
changed the counter: an empty report is not a measurement, so the base is **unevaluable by this
counter** (exit 2) rather than a measured `0 of 7`, and the message still carries the pins reading
(`0/3`) so the base's pin drift stays visible. My first draft read `surfaces pass 0 of 7 … pins OK 0/3`
(exit 1) at the base; that reading is superseded here, and the receipt carries only the current
behaviour.

## Evidence 3 — the five shortcut-control worlds, replayed through this counter

Worlds are ExecRepinControls' committed overlays; the sandboxes and the counter runs are mine (fresh
`--shared` clone of `c69711e` inside a fleet-shaped `/tmp` parent, overlay copied, `__CLONE__`
substituted, one commit inside the clone, sandbox deleted afterwards), so their bundles were not
touched. Replay commands are in the receipt.

| world | `pins OK` | `surfaces pass` | `removal ledger` | exit | conjuncts below target |
|---|---|---|---|---|---|
| `w1-repin-only` | 3/3 | 5 of 7 | 0 of 1 | **1** | surfaces; ledger (CONTEXT.md unledgered) |
| `w2-ledger-all` | 3/3 | 5 of 7 | 1 of 9 | **1** | surfaces; ledger (8 present literals ledgered) |
| `w3-stub-pinned` | **2/3** | 5 of 7 | 0 of 1 | **1** | substrate identity; surfaces; ledger |
| `w3b-stub-full-ledger` | **2/3** | 5 of 7 | 1 of 9 | **1** | substrate identity; surfaces; ledger |
| `w4-omp-mtime-stale` | 2/3 | 5 of 7 | 0 of 1 | **1** | pins (mtime); surfaces; ledger |
| `w5-repin-plus-honest-ledger` | 3/3 | 5 of 7 | 1 of 1 | **1** | surfaces only |

`w5` is the world I asked the controls seat to build after the first review (repin-only plus the
honest one-row ledger); it reads `pins OK 3/3; surfaces pass 5 of 7; removal ledger 1 of 1 verified`,
exit 1 — surfaces only. My sandbox's commit (`18a14dd9…`) differs from theirs (`7527645…`) because the
overlay's `__CLONE__` placeholder carries each sandbox's own path.

`w3`/`w3b` reproduce with the substrate-identity line:

```
FAIL substrate identity: pin(s) opencode_binary_sha256 PASS on bytes that are not the live opencode the counter dumped (sha256 ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7)
```

The controls seat measured `w3b` as holding every conjunct except `p == 7`, so a Q45 lowering of the
surface target would have made a 358-byte stub read exit 0. With the two changes it fails `pins 2/3`
(identity) **and** `removal ledger 1 of 9`, on any target. `w3` plus the honest one-row ledger — the
world nobody built — also fails `pins 2/3` on any target. ExecRepinControls then rebuilt `w1` and `w3b`
in its own sandboxes and ran this draft, reporting the same two readings (`w1` 3/3, 5 of 7, 0 of 1;
`w3b` 2/3 with the substrate-identity line, 5 of 7, 1 of 9), so the numbers above are reproduced by a
second seat from independent sandboxes.

## Evidence 4 — live literal census

```
$ for lit in 'AGENTS.md' 'CLAUDE.md' 'CONTEXT.md' 'instructions' 'https://' '<system-reminder>'; do
    printf '%-20s ' "$lit"; grep -cF -- "$lit" /tmp/k72-oc-strings.txt; done
AGENTS.md            13
CLAUDE.md            3
CONTEXT.md           0
instructions         145
https://             827
<system-reminder>    14
```

Dump sha256 `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089`, 28,835,401 bytes. Exactly
one base opencode class is absent, so `required` is exactly `{opencode:instructions/CONTEXT.md}`; the
counter's own pass on `~/.opencode/bin/opencode` (sha256 `ca9b3ee2…`, 240,416,944 bytes, 1,237,844
strings lines) agrees — `w1`/`w2`/`w3`/`w4` all report `1 absent class(es) not ledgered:
opencode:instructions/CONTEXT.md`.

## Decisions a wave-2 reviewer must judge

1. **The ledger's referent is the live host binary, not the tree's pinned path.** The frozen sentence
   names "the live opencode dump"; letting a tree choose the bytes its ledger is judged against is what
   made `w3b` pass. The substrate line names the path, sha256 and size actually dumped.
2. **`k` counts only pins that hold against those bytes.** `check_substrate_pins.py` compares a pin
   with whatever sits at the tree's path, so it cannot tell the host binary from a stub whose own sha
   was pinned (the controls seat measured `pins 3/3` for a 358-byte stub). A PASS row whose expectation
   is not the measured sha is not counted, and stderr names it. This refines `k` rather than adding a
   fourth conjunct to the frozen line.
3. **`<total>` in the frozen line is |ledger ∪ required|**, so an exactly-right ledger reads `l of l`
   and a defect shows in the line itself (`1 of 2` for a ledgered-but-present literal, `0 of 1` for an
   unledgered-but-absent class). The other readings each hide one defect (`|required|` hides the
   superset, `|ledger|` hides the gap).
4. **Two row-count guards**: the pin script must report exactly 3 rows and the surfaces script exactly
   7 checks, else exit 1 even if `k == 3` / `p == 7`. Self-tested (`extra pin row`, `extra check`).
   Stricter than the frozen iff in one direction only; deletable by removing two `len(...) ==` terms.
5. **An empty instrument report is exit 2**, not `0 of 7` / `0/3` (see Evidence 2).
6. **The ledger schema is mine to define** (no fleet precedent: `grep -rln census-removals` hits only
   `plans/round-72.md`, `w1-spec.json`, `w1-dispatch.json`). The counter reads only
   `removals[].class_id`; a missing file is an empty ledger; unparseable JSON or a row without a string
   `class_id` is exit 2. ExecRepinControls confirmed its files match this shape.
7. **Committed bytes only**: the ledger is read from the `git archive` tree, so an untracked
   `verifiers/census-removals.json` is invisible.
8. **"An absent class cannot stay declared `governed`" is not a separate conjunct.** The frozen
   sentence says kept-*or*-listed, and the consequence is enforced by `surfaces.opencode_extract`'s
   two-way parity — which is why `p` must be 7. I did not add a stricter clause.

## Integration requirements for the L1

- Install at `verifiers/check_substrate_repin_v2.py`. `default_repo()` walks up to the nearest ancestor
  holding `verifiers/surfaces-baseline.json`; verified at both locations by loading the module and
  pointing `__file__` at each (build dir → lane root; `…/verifiers/check_substrate_repin_v2.py` → same
  root).
- `verifiers/census-removals.json` must be **committed** with exactly one row at the live substrate:
  `opencode:instructions/CONTEXT.md` (extra fields such as `literal`, `reason`, `evidence`, `rev` are
  ignored). Any additional row is a superset and fails the exact-set conjunct.
- Keep exactly three pin rows, and make the opencode sha256 pin the live binary's sha — a pin on any
  other bytes is no longer counted as holding. Do not name re-pin notes `opencode_binary_<word>`:
  `DISCOVER_RE` (`verifiers/check_substrate_pins.py:80`) discovers such keys as pins.
- **Gate registry cost.** `check_gate_registry.py` counts lane verifier files against the
  `## Gate registry` table in `SKILL.md` (base `conformant 51 of 53`). Installing this counter makes 54
  verifiers; the table has 51 rows (`awk` pipe-line count under `## Gate registry` = 53, header +
  separator + 51 rows), so a row must be added — and `wc -l SKILL.md` is **600**, the checklist
  ceiling, so the row needs a freed line first. The C3 counter carries the same cost: budget two freed
  lines.

## Risks / blockers

1. **The green path is unproven on real bytes** — the honest re-pinned rev does not exist yet. Its first
   honest run is the receipt that matters, and it must be run before the claim is scored (Q19).
2. **A lowered surface target is narrower than it looked, and the row-count guard is what narrows it.**
   I measured (my own sandboxes, `verify_surfaces.py --json` at default paths) that `w1` (real 240 MB
   binary) and `w3` (358-byte stub) produce an identical 7-row `(id, status)` vector — my serialization
   hashes both at `82b34d71fb720fce`, failing exactly `surfaces.literal_present` and
   `surfaces.opencode_extract` — so pass-count and verdict vector cannot tell real bytes from a stub;
   only `detail` differs, and the frozen predicate does not read `detail`. ExecRepinControls built that
   world as `w5` (repin-only + the honest one-row ledger); at the frozen target it reads
   `pins OK 3/3; surfaces pass 5 of 7; removal ledger 1 of 1 verified`, exit 1 — surfaces only.
   I then tested the lowering directly on a throwaway copy of this counter with `CHECKS_TOTAL = 5`
   (lane file untouched) against the same world:
   `surfaces pass 5 of 5; removal ledger 1 of 1 verified` plus
   `FAIL surfaces: 5 of 7 check(s) PASS, 7 check(s) reported, 5 expected` — **exit 1**. Editing the
   target alone does not turn `w5` green: the guard requiring the instrument to report exactly
   `CHECKS_TOTAL` checks catches it. ExecRepinControls then reproduced the lowering independently on a
   fresh w5 rebuild (its commit `97352e69…`, sandbox deleted) and reported the same two lines and
   exit 1, and corrected its own earlier "exit 0 at target 5" inference. So the hazard requires
   **retiring two checks from `verify_surfaces.py`'s `CHECK_IDS` as well** (a visible instrument edit
   that also moves that verifier's self-test assertion count, i.e. its `floors-registry.json` floor),
   not a bookkeeping change to this counter. That is the shape any Q45 lowering must take, and it
   should be reviewed as an instrument retirement, not as a target change.
3. **My two refinements are supersets of the frozen iff** (points 2 and 4 above); wave 2 should accept
   them or have the L1 delete them.
4. **Ledger superset/gap visibility depends on the union denominator**; with `|required|` the line
   would read `1 of 1` on a superset ledger and only the exit code would carry the defect.

## Not observed

- No exit 0 on a real revision; `p == 7` on v2.1.4 is unmeasured. The Q45 population census belongs to
  another seat and I did not attempt it.
- I ran no lane gate, no battery item, no fleet-shaped gate, and did not re-run the r53
  `check_opencode_repin.py`. The L1 owns post-integration gate execution.
- Host binaries were not re-dumped; the census uses the shared `/tmp/k72-oc-strings.txt` (the counter's
  own pass agreed on `CONTEXT.md` = 0).

## Hygiene

No tool installed or upgraded (`strings` GNU binutils 2.47 and python 3.14 were already present); no
pacman transaction; no jj command; no git write outside throwaway `/tmp` clones (all deleted —
`ls -d /tmp/k72w1-ExecRepinCounter.*` → none); no credential, session or `op://` material read or
written.

## Files changed

- `.ufo/waves/round-72/w1/build/ExecRepinCounter/check_substrate_repin_v2.py` (new draft)
- `.ufo/waves/round-72/w1/build/ExecRepinCounter/base-measurement.txt` (new receipt)
- `.ufo/waves/round-72/w1/ExecRepinCounter.md` (this report)
