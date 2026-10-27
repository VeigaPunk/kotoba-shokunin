# B24TipBatteryScript — round-76 no-harm battery script + base test-run

Seat: `B24TipBatteryScript` (executor, leaf). Scope: write the round-76 tip-battery
script, test-run it at base, land the base receipt, report only. No claim data was
written; no git/jj mutation was performed anywhere.

**Verdict: the script is in place and runs the full no-harm battery end to end (10
gates, stdout + exit code each, first line `git rev-parse HEAD`). At the base it
reads 8 of 10 green. The 2 reds are the two corpus gates, and they are red at the
base AND at the lane tip identically — the plan's § Base battery line "corpus
integrity exit 0; corpus independent exit 0" does not reproduce (finding
F-B24-1). The script is exit-code-honest by construction: it never pipes a gate
through a truncator, so it cannot repeat the receipt-masking mechanism that
produced the wrong base numbers (finding F-B24-2).**

## Files changed by this seat

| path | kind |
|---|---|
| `.ufo/waves/round-76/receipts/tip-battery.sh` | new — the script (chmod +x) |
| `.ufo/waves/round-76/receipts/tip-battery-base.txt` | new — the base test-run receipt |
| `.ufo/waves/round-76/w1/B24TipBatteryScript.md` | new — this report |

Nothing else in the lane repo was written. No git/jj write, no index change, no
commit, no push.

## What the script is

`.ufo/waves/round-76/receipts/tip-battery.sh` (bash, 755) runs every gate command
of the plan's no-harm battery (`plans/round-76.md` § No-harm battery) and prints
for each: the command line, its stdout, its stderr when non-empty, and its exit
code. First line of the output is `git rev-parse HEAD` of the measured repository;
then a header naming the repo, the repo HEAD, the measured rev and the census root.

```
usage: tip-battery.sh [--repo DIR] [--rev REV] [--census-root DIR] [--census-lane NAME] [--help]
```

Gates, in order (each = one `==` block, one `exit=` line):

| # | gate | note |
|---|---|---|
| 1 | `python3 -B verifiers/verify_corpus_integrity.py --json` | worktree-reading |
| 2 | `python3 -B verifiers/verify_corpus_independent.py --json` | worktree-reading |
| 3 | `python3 -B verifiers/check_gate_registry.py --rev <rev>` | revision-gated |
| 4 | `python3 -B verifiers/check_assertion_floors.py` | worktree-reading, slowest (~95 s) |
| 5 | `python3 -B verifiers/verify_skill_checklist.py --json` | worktree-reading |
| 6 | `python3 -B verifiers/check_spec_craft.py --rev <rev>` | revision-gated |
| 7 | `python3 -B verifiers/check_sibling_reread.py --rev <rev>` | revision-gated |
| 8 | `sources-census.sh validate …` | fleet-root lane run, or `--file` mode off-lane |
| 9 | `wc -l SKILL.md` | the plan's line-budget input |
| 10 | SKILL.md line budget (≤ 600) | the plan's budget check, as its own gate |

The script ends with a `== summary` block (one `command<TAB>exit` row per gate), a
`gates green: N of 10` line and a `battery: PASS|FAIL` line. **Exit status is 0
only when every gate exited 0 and SKILL.md is within budget; 1 otherwise.** It is
read-only: `git rev-parse` only, the census tool in `validate` mode only.

Two design choices worth stating, because they are what make the receipt
trustworthy:

- **No gate is piped.** Every gate's stdout goes to a temp file that is `cat`ed
  back, and the exit code is read from the command itself (`"$@" >"$TMP/out" …;
  rc=$?`). A pipeline would report the *last* stage's status — see F-B24-2.
- **The census shape follows the tree being measured.** When the measured repo IS
  the fleet lane (`<census-root>/kotoba-shokunin`), the census runs in the plan's
  own fleet-root lane form (`validate --root <root> kotoba`, whose last line is
  `kotoba ok <path>`). Off-lane it runs `--file <repo>/corpus/SOURCES.md` against
  the tree under test, so the census always reads the tree being measured rather
  than the live lane's registry.

`--rev` lets the caller pin the revision the three revision-gated gates measure;
when it differs from the repo HEAD the script prints a `NOTE:` line saying so, so a
mismatched run can never be mistaken for a tip measurement. Measured at base the
repo HEAD and the measured rev coincide and no NOTE is printed.

## Base test-run

The receipt is `.ufo/waves/round-76/receipts/tip-battery-base.txt` (545 lines):
the verbatim stdout of the script plus a provenance footer.

```
$ .ufo/waves/round-76/receipts/tip-battery.sh \
    --repo /fast/scratch/hyaku/kotoba-r76/B24TipBatteryScript/base-mirror/kotoba-shokunin
b7f13f4b39cbd43076a85568adca763a6f674e7a          <- line 1: git rev-parse HEAD
TIP BATTERY — kotoba round 76 no-harm battery
repo: /fast/scratch/…/base-mirror/kotoba-shokunin
repo HEAD: b7f13f4b39cbd43076a85568adca763a6f674e7a
measured rev: b7f13f4b39cbd43076a85568adca763a6f674e7a
census root: /home/vgpnk/Projects/shokunin
…
== summary
python3 -B verifiers/verify_corpus_integrity.py --json	1
python3 -B verifiers/verify_corpus_independent.py --json	1
python3 -B verifiers/check_gate_registry.py --rev b7f13f4…	0
python3 -B verifiers/check_assertion_floors.py	0
python3 -B verifiers/verify_skill_checklist.py --json	0
python3 -B verifiers/check_spec_craft.py --rev b7f13f4…	0
python3 -B verifiers/check_sibling_reread.py --rev b7f13f4…	0
sources-census.sh validate --file …/corpus/SOURCES.md	0
wc -l SKILL.md	0
SKILL.md line budget (<= 600)	0
gates green: 8 of 10
battery: FAIL (2 gate(s) red)
script_exit=1
```

### Why the run was made in a mirror, and how the mirror was built

Two of the corpus gates (1, 2) and the checklist/floors gates read the **working
tree**, not a revision. The live lane's worktree had already moved past the base
(its HEAD at the time of the run was `eab64394dba08a47f6797a2e23719be14675b44b`,
the round-76 wave-spec and role-mix commits), so running in the lane would have
measured the tip's corpus and mislabelled it "base". The base therefore ran in a
`git clone --shared` mirror checked out at `b7f13f4…`:

```
$ git clone --shared /home/vgpnk/Projects/shokunin/kotoba-shokunin base-mirror/kotoba-shokunin
$ git -C base-mirror/kotoba-shokunin checkout --quiet b7f13f4b39cbd43076a85568adca763a6f674e7a
$ tar cf - --exclude='waves' .ufo | tar xf - -C base-mirror/kotoba-shokunin/   # untracked reports/ + round-N/ dirs
$ ln -sfn /home/vgpnk/Projects/shokunin/.ufo   base-mirror/.ufo
$ for f in /home/vgpnk/Projects/shokunin/*.md; do ln -sfn "$f" base-mirror/; done
$ for d in /home/vgpnk/Projects/shokunin/*-shokunin; do [ "$d" = …/kotoba-shokunin ] || ln -sfn "$d" base-mirror/; done
```

The `../` symlink shim matters and was necessary: without it the fleet-relative
citations in `LOG.md` (`../PROTOCOL.md`, `../AXES.md`,
`../kasegi-shokunin/corpus/instruments/resolve.py`) do not resolve from the
mirror, and `verify_skill_checklist.py` reports a spurious
`governance.citation_resolves` FAIL. With the shim the mirror reproduces the live
lane exactly — the checklist reads `pass 11, fail 0, exit 0` in the mirror and in
the live lane alike. This is the same trick peer `B10RepairD2D3` used ("fleet-layout
parent shim"), independently arrived at.

**Fidelity check (mirror vs live lane, same battery, same script):** the mirror at
base and the live lane at HEAD produce the *same* gate verdicts — greens at 3, 4, 5,
6, 7, 8, 9, 10 and reds at 1 and 2 in both. The only difference between the two runs
is the census block, which switches from `--file` form (mirror) to the fleet-root
`kotoba` form (lane) by design, and the measured rev.

## Findings

### F-B24-1 (calibration, blocks C2's R2 as literally specified) — the plan's base-battery corpus numbers do not reproduce

`plans/round-76.md` § Base battery states:

> "corpus integrity exit 0; corpus independent exit 0"

Measured at the declared base `b7f13f4b39cbd43076a85568adca763a6f674e7a` (clean
mirror, base checkout) **and** at the live lane, both verifiers are **exit 1**:

```
$ python3 -B verifiers/verify_corpus_integrity.py --json
DRIFT corpus.index.tracked_files   145 != 144
DRIFT corpus.index.unindexed       1 != 0/empty   (corpus/lessons/round-75-verifier-spotcheck.md)
DRIFT corpus.pointers.report_total  101 != 99
DRIFT corpus.pointers.commit_total  44 != 43
exit=1
$ python3 -B verifiers/verify_corpus_independent.py --json
DRIFT corpus.index.unindexed       1 != 0/empty
exit=1
```

The base commit `b7f13f4` ("round-75 verifier spot-check (integrator, hyaku)")
landed the closure-owned `corpus/lessons/round-75-verifier-spotcheck.md` **without**
a `corpus/README.md` coverage-map index row (`grep -c round-75-verifier-spotcheck
corpus/README.md` → 0) and **without** re-recording `verifiers/corpus-baseline.json`
(whose `measured_against` still reads base `65a5c7a`, `tracked_files 144 /
report_total 99 / commit_total 43`). This is the exact recurring pattern the lane
has already recorded three times in `corpus/README.md` (rows for rounds 49, 50,
53, 54: "landed without an index row (which turned `verify_corpus_integrity.py` red
at that base: `unindexed 1`), indexed round N").

This is **not** a round-76 regression and **not** caused by the wave: the two gates
read identically at the base and at the lane tip (`eab6439…`), and the drift was
introduced by the r75 closure commit itself.

**Consequence for C2's R2.** R2 requires a receipt
(`.ufo/waves/round-76/receipts/noharm-at-tip.txt`) carrying "stdout + exit codes of
`verify_corpus_integrity.py --json` and `verify_corpus_independent.py --json`
reading green". As committed bytes stand, that receipt cannot exist truthfully:
both gates are red and the reds are structural (an unindexed corpus file and a
stale baseline), not transient.

**Measured path to green** (in a scratch clone at `b7f13f4`, three edits, then the
two gates re-run):

```
(i)  add corpus/README.md coverage-map index rows for
       lessons/round-75-verifier-spotcheck.md, knowledge/description-craft-round76.md,
       lessons/round-76.md                       (rows must sit inside the "## Coverage map"
                                                  section, before "## Frontier" — a row appended
                                                  after "## Frontier" is NOT harvested and changes nothing)
     -> verify_corpus_integrity.py --no-baseline --json : unindexed 0, exit 0
     -> verify_corpus_independent.py --json             : exit 0
     -> verify_corpus_integrity.py --json                : still exit 1
        (tracked_files 147 != 144, report_total 101 != 99, commit_total 44 != 43)

(ii) re-record verifiers/corpus-baseline.json to the new measured values
     -> verify_corpus_integrity.py --json   : exit 0, zero red rows
     -> verify_corpus_independent.py --json : exit 0
```

So both R2 legs go green only with **(a)** the README index rows *and* **(b)** a
baseline re-record — the same two-part repair the lane performed at round 74
(commit `1cf5afa` "round-74: corpus baseline re-record (commit_total 43)"). Note
that the r74 precedent receipt (`.ufo/waves/round-74/receipts/base-battery-l1.txt`)
recorded exactly this shape honestly, including a red pair and the reason:

> "gate verifiers/verify_corpus_integrity.py exit 1 … gate
> verifiers/verify_corpus_independent.py exit 1 … Reading: the two reds are the
> unindexed r73 closure file …"

**Recommendation for the L1 (decision, not mine to take):** land the README index
row for `lessons/round-75-verifier-spotcheck.md` and re-record
`verifiers/corpus-baseline.json` in the same commit as the round-76 data (the
baseline is a measurement of the tree, so it must be re-recorded *after* the new
corpus files land, not before). Until then, an R2 receipt claiming the two corpus
gates "read green" would be a fabricated verdict, and the tip battery will report
`battery: FAIL (2 gate(s) red)` for the same reason the base does.

Note the tip-state numbers the baseline will have to carry: with the round-76
corpus files present, `tracked_files` is 147 (145 + `knowledge/description-craft-round76.md`
+ `lessons/round-76.md`), and `report_total`/`commit_total` shift with whatever
those files cite. The exact values must be measured at the tip, not predicted.

### F-B24-2 (calibration / operability) — the committed base receipt's exit codes are a truncator's, not the gates'

`.ufo/waves/round-76/base-battery/base-battery.txt` records, for gates 1 and 2:

```
== python3 -B verifiers/verify_corpus_integrity.py --json
    }
  ]
}
exit=0
```

The block is the **last three lines** of the JSON followed by `exit=0`. Reproduced:

```
$ python3 -B verifiers/verify_corpus_integrity.py --json | tail -3
    }
  ]
}
$ python3 -B verifiers/verify_corpus_integrity.py --json | tail -3 >/dev/null; echo $?
0                      # <- tail's status
$ python3 -B verifiers/verify_corpus_integrity.py --json >/dev/null 2>&1; echo $?
1                      # <- the gate's status
```

The receipt captured `$?` of a pipeline, so the exit code recorded is `tail`'s
(always 0), not the verifier's (1). The same shape appears in the sibling round-74
receipt `.ufo/waves/round-74/receipts/base-battery-l1.txt`, which is candid about
it — "`battery exit` is `${PIPESTATUS[0]}`" — but the round-76 base receipt applies
`tail -3` to gates whose exit codes then get recorded from the wrong command. The
plan's base-battery prose was written from that receipt and therefore inherits the
error.

This is why `tip-battery.sh` never pipes: it redirects each gate to a temp file
and reads the gate's own status. A battery that can report `exit=0` for a red gate
is worse than no battery, because it launders a red into a green.

### F-B24-3 (operability, informational) — the battery's slowest gate

`check_assertion_floors.py` takes ~95 s wall (it re-runs the whole floors registry,
several instrument self-tests inside). The full battery is ~100 s. A tip re-run
should budget for that rather than assume a quick loop; `verify_skill_checklist.py`
is ~3 s, the corpus gates <1 s each.

### F-B24-4 (freshness, informational) — the plan's SKILL.md line figure is right

`wc -l SKILL.md` → 590 at the base and at the lane tip, budget 600 (from the box
at SKILL.md line 285). The plan's "SKILL.md 590 lines (budget 600)" reproduces. The
budget gate is implemented as its own gate so the tip run carries the number
forward in its own output rather than needing a second command.

## Consistency with the plan and with the other no-harm consumers

- The plan's § No-harm battery lists exactly these gates ("re-run the same battery
  plus `check_gate_registry.py`, `check_assertion_floors.py`,
  `verify_skill_checklist.py --json`, census, and the SKILL.md line-budget check on
  a scratch tree holding the claim files before the report"). The script covers
  all of them; the plan's "on a scratch tree holding the claim files" is exactly
  the mode the script supports via `--repo`.
- The plan's base-battery census line (`exit 0`, `kotoba ok`, 151 rows, W04 set as
  at r75) reproduces: the script's census gate is exit 0 at base and at the lane
  tip, with the same 20 W04 duplicate-URL warnings and no E-codes (cross-checked
  against peer `B25Census`'s receipt).
- `check_spec_craft` and `check_sibling_reread` are green at base (3 of 3; 20 of
  20) from the script, so the round-76 counters' revision-gated siblings are sound
  at the point the wave starts.

### Coverage delta vs the committed base receipt

The committed `.ufo/waves/round-76/base-battery/base-battery.txt` covers 7 commands.
The script covers 10: it adds the census, `wc -l SKILL.md` and the line-budget
check (the plan's § Base battery prose lists all three, but the receipt file
omits them), and it prints full stdout for every gate instead of a 3-line tail.
That is the difference between "the battery was run" and "the battery can be
re-run".

### Pointer-gate self-check (read-only)

```
$ python3 -B verifiers/check_report_pointers.py --report .ufo/waves/round-76/w1/B24TipBatteryScript.md \
    --repo . --rev eab64394dba08a47f6797a2e23719be14675b44b --round 76
report pointers resolved 16 of 23; unresolved 7
exit=1
```

All 7 unresolved tokens are paths this round has not committed yet — this seat's
own three artifacts (`tip-battery.sh`, `tip-battery-base.txt`, this report) and
`.ufo/waves/round-76/receipts/noharm-at-tip.txt` (R2's receipt, not yet written).
The counter reads committed bytes only, so the pre-landing state is expected;
peer `B25Census`'s report shows the same shape (3 distinct unresolved tokens, all
not-yet-committed). Nothing here is a broken pointer.

Incidentally, the pointer gate's "nearest" hint for `noharm-at-tip.txt` is
`.ufo/waves/round-70/receipts/noharm-at-tip.txt` — an existing file in an earlier
round, confirming the R2 receipt's name and shape are the lane's own convention
rather than a new one.

## Risks / blockers

- **None blocking for this seat.** The script and the base receipt are landed; the
  battery runs.
- **R2 as literally specified cannot yet be satisfied truthfully** (F-B24-1): the
  two corpus gates are structurally red at base and tip. The integrator must land
  the README index row(s) and the baseline re-record before a "reading green"
  no-harm receipt can exist. Until then the tip battery will report
  `battery: FAIL (2 gate(s) red)` — which is the correct, honest reading, and the
  same reading the base gives.
- **The tip re-run must be made on a tree holding the round-76 claim files**, per
  the plan. Run against the live lane *before* the data lands, it measures the
  pre-data tree; run after, it measures the tip. Either way the receipt's first
  line (`git rev-parse HEAD`) and the `measured rev:` line must agree with the
  revision the receipt claims to cover — the script prints a `NOTE:` when they
  differ.
- **Do not rebuild the mirror from the receipt's paths alone** — the receipt's
  provenance footer records the `../` symlink shim, which is required for the
  checklist's fleet-relative citations to resolve. A mirror without the shim
  produces a spurious `governance.citation_resolves` FAIL (measured: 10 pass / 1
  fail) that the live lane does not have.

## Tooling

No tool was installed or upgraded by this seat. `git`, `python3`, `bash`,
`gawk` (used by the census script) were already present and were used from their
existing locations.

## Scratch

All temporary work lived in `/fast/scratch/hyaku/kotoba-r76/B24TipBatteryScript/`
(the base mirror, the probe clone used for the F-B24-1 green-path measurement, and
the captured run outputs). The directory was removed at the end of the seat.

VERDICT: B24TipBatteryScript complete — tip-battery.sh landed (chmod +x) and base-tested; base receipt tip-battery-base.txt landed; base battery reads 8 of 10 gates green, the 2 reds being the pre-existing r75-closure corpus drift (F-B24-1: the plan's "corpus integrity exit 0" base claim is not reproducible — the committed base receipt recorded tail's exit code, F-B24-2); no claim data written, no git/jj mutation, scratch removed.
