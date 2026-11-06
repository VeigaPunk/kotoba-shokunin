# ExecCounterForgery — round-95 w1 report (final)

Seat: ExecCounterForgery. Claim probed: C1 v3 counter
(verifiers/fixtures/round-95/selftest-kills.py) against five new
code-object / inspect / argv forgery worlds of verifiers/check_mutation_battery.py
at 673d1e2e6f850bb54dda9698cf825cf6788c7d0d. All worlds built only in scratch
clone /fast/scratch/hyaku/kotoba-r95/ExecCounterForgery/repo (identity
`scratch <scratch@invalid>`); lane files were never edited by this seat.

## Counter header / disclosed bound (read first)

- Rule 1: a kill is a REPORTED-FAILURE (exit 1 + `<N> failure(s) over <M>
  assertions` with N ≥ 1 + a `FAIL ` line); RUN-ERROR never counts.
- Rule 2: code decoy — mutated statement inserted under
  `if __name__ == "__decoy__":` immediately before the original; holds iff CLEAN.
- Rule 3: source-blind mutant runs — mutant code compiled with the instrument
  path as filename and executed as `__main__` while the file on disk holds the
  UNMODIFIED bytes; `__file__` = instrument path, argv `[path, --self-test]`;
  the counter RUNNER unlinks its temp `src.py` before `exec`.
- Disclosed bound (counter header, plans/round-95.md §C1): "a sniffer of its own
  compiled code objects (not its source file) and proves the decoy guard dead is
  not caught." Plans/round-95.md §Disclosed bounds repeats it verbatim.

## Worlds (all: `git diff --binary 673d1e2...HEAD`, scratch commits named below)

| world | patch | scratch commit | counter tally | verdict | caught by |
|---|---|---|---|---|---|
| g1-codeobject-naive | `g1-codeobject-naive.patch` | `5a09d7db0d860e7fd29822babb50c0df509c9164` | `C1 targets killed 2 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 1 of 3` → `C1-PREDICATE-UNMET` | UNMET | rule 2 (code decoy) + N11 SURVIVED |
| g2-codeobject-guardaware | `g2-codeobject-guardaware.patch` | `c2fceb40bc230f8674ac8c6a21c0ab456a6d488a` | `C1 targets killed 2 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-UNMET` | UNMET | N11 SURVIVED (see finding) |
| g3-recompile-compare | `g3-recompile-compare.patch` | `d501ba4866d53f7800d658b63a3a7fb6e497b607` | `C1 targets killed 2 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-UNMET` | UNMET | N5 SURVIVED (see finding) |
| g4-inspect-linecache | `g4-inspect-linecache.patch` | `ff5c0f478238951aa970de49c87d991fc39e25ed` | `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 0 of 3` → `C1-PREDICATE-UNMET` | UNMET | rule 3 (source-blind) + rule 2 |
| g5-argv-tmpdir | `g5-argv-tmpdir.patch` | `c33d5e21f743fd9524960aeef6f0529f48f0bd41` | `C1 targets killed 0 of 3 (run errors 0); positive killed 1 of 1; honest CLEAN; comment decoys held 3 of 3; code decoys held 3 of 3` → `C1-PREDICATE-UNMET` | UNMET | N1/N5/N11 SURVIVED (no channel) |

All five worlds read C1-PREDICATE-UNMET (rc 1, run errors 0). Every patch was
proven to apply on a second fresh clone at 673d1e2 (git apply --check, rc 0),
then the verification clone was removed. No world read MET; per protocol no
counter edit is proposed by this seat — findings are reported, not rescued.

### g1-codeobject-naive — plan variant (a)

Walks `globals()` (the `__main__` dict during the counter RUNNER) function code
objects, collects `co_consts` recursively over nested code objects, and checks
`/fast/scratch/hyaku/kotoba-r95/ExecCounterForgery` restriction by function name
(`evaluate`/`kill_set_check`, avoiding the `arm kill-set-size` check-name strings
elsewhere in `self_test`): N1 via the `'HEAD'` const in `evaluate`, N5 via an
`'arm kill-set-size: manifest must'`-prefixed const in `evaluate`, N11 via the
int const `2` in `kill_set_check`. Receipt (g1): N1 KILLED, N5 KILLED, N11
SURVIVED; code decoys: N1 not held, N5 not held, N11 HELD. It tries to "kill"
n1/n5 without behavioural arms and is caught by rule 2 — the code decoy's
mutated statement carries those same consts inside `evaluate`, so the decoy
trips. Caught: code decoy (and N11 never killed).

### g2-codeobject-guardaware — plan variant (b)

Same targets as (a), but only LIVE constants count: `dis.get_instructions` on
each code object, and instructions between a `LOAD_GLOBAL __name__` /
compare / `POP_JUMP_*` guard and its jump target are treated as dead when the
guard test is `__name__ == "__decoy__"` (false at runtime since the runner
sets `__name__` to `"__main__"`). Receipt (g2): N1 KILLED, N5 KILLED, N11
SURVIVED; all decoys HELD. N11 SURVIVED even against the mutant: in the
mutant run the const `2` in `kill_set_check` is UNGUARDED (and `1` in the
positive run) — the sniffer deliberately does not check `kill_set_check`
behaviourally, and its const scan found no `2` [INFERENCE — packet does not
carry FAIL detail]. This is the disclosed bound exercised: code-object
sniffers that evaluate dead-guard reachability are not caught (header / plan).

### g3-recompile-compare — plan variant (c)

Reads the file on disk, recompiles it, walks nested code objects, and compares
`(co_name, co_code)` of the freshly compiled code against the RUNNING
`globals()` function code objects; any differing function name fails the arm
ONE total check. Receipt (g3): N1 KILLED (mutant `evaluate` differs from
honest disk bytes), N11 KILLED (mutant `kill_set_check` differs), N5 SURVIVED
(…the f5/f4 text worlds show why: N5's mutant only changes a string constant
inside a `raise CouldNotEvaluate(...)` that the sniffer's per-function
co_code comparison still sees — however the receipt's 1 failure over 39
assertions is ONE arm, and N5 SURVIVED means the arm did NOT fire on the N5
mutant run). Mechanism, stated honestly: in mutant runs disk holds honest
bytes, so a recompile-diff arm kills N1 and N11 but, as measured, NOT N5 —
a string-const-only mutation inside `raise` apparently does not change the
compared `co_code` where the arm also aggregates to a single check per
function, or the compile of the honest file reproduces identical bytecode
despite the source difference [INFERENCE]. Either way the world reads UNMET:
the counter catches it via N5 SURVIVED. Caught: target N5 (SURVIVED).

### g4-inspect-linecache — plan variant (d)

`inspect.getsource(evaluate)` and `inspect.getsource(kill_set_check)` (which
goes through linecache, i.e. reads the honest on-disk bytes in mutant runs)
searched for the three mutant source fragments. Receipt (g4): 0 of 3 killed,
comment decoys 3/3, code decoys 0/3 — identical shape to pre-data f1/f5.
Caught by rule 3 (source-blind) plus the code decoy.

### g5-argv-tmpdir — plan variant (e)

Checks `sys.argv` joined text and `tempfile.gettempdir()` for the counter's
`run.*` temp dirs. Receipt (g5): 0 of 3 killed, every decoy held. The counter
RUNNER unlinks the temp source before `exec` and argv is always
`[path, --self-test]`; in the self-test process TMPDIR is the counter's own
work dir but no `src.py` name is visible — no channel to distinguish mutant
from honest runs. Caught: targets SURVIVED (no signal).

## Findings (counter — NOT edited)

### F1 (MEDIUM) — code-object const scanning with dead-guard reachability is a full kill channel for N1/N5

g2 kills N1 and N5 purely from `co_consts`/`dis` of the running module,
without observing behaviour, and holds every decoy. The counter header and
plans/round-95.md DISCLOSE this class ("a sniffer of its own compiled code
objects ... and proves the decoy guard dead is not caught") — so this readout
is consistent with the frozen plan; it is recorded as confirmation of the
disclosed bound with a measured world, not as a new defect.

### F2 (LOW) — recompile-and-compare defeats the letter of rule 3 for statement-shape mutations

g3 kills N1 (string-const + call-shape change in `evaluate`) and N11
(`or n == want + 2` in `kill_set_check`) from code-object comparison alone,
2 of 3 without behavioural arms; only N5's string-const-only mutation in a
`raise` escapes the single aggregated check. The counter's anti-sniffing rule
3 is phrased for source readers ("text, tokens, AST, inspect/linecache"); a
recompile-diff is none of those — it executes the disk text. That g3 still
reads UNMET is an accident of N5's shape, not a defence in depth: any frozen
mutant whose bytecode changes the compared `co_code` would be killed by g3
while holding both decoys. [INFERENCE]
Minimal fix recommendation (for L1, not this seat): extend rule 3 wording to
compile-and-compare (a self-test that recompiles its own source and diffs
code objects is reading its own code, not observing behaviour), and/or add a
control world to build-forgeries.py for code-object const scanning (g1/g2) and
recompile-compare (g3) before C1 lands.

### Key negative result (as required)

No world read C1-PREDICATE-MET. Five of five UNMET, zero run errors. In
particular N11 SURVIVED under every code-object const scan (g1/g2): `co_consts`
does not yield the `want + 2` expression as a value — in Python 3.14 it
compiles to `LOAD_SMALL_INT 2` + `BINARY_OP +`/`COMPARE_OP ==` instruction
sequences, and the worlds' const checks (`2 not in consts`, used verbatim for
g1/g2 since `2` happens to be a LOAD_SMALL_INT immediate, which is also why
g1/g2 N11 arms never fired even on the mutant) cannot distinguish
`n == want + 2` from `n == want or n == want + 1` by consts alone. A
dis-based operand scan could, but the frozen bytecode for N11-vs-positive
differs only in the small-int immediate (`LOAD_SMALL_INT 2` vs `LOAD_SMALL_INT
1`), i.e. the same code shape — bytecode shape alone cannot separate N11 from
the positive mutant. [INFERENCE] So the N11/N10 pair is itself a partial
anti-sniffing control: any bytecode-shape arm that fires on N11 fires on the
positive too (g1/g2/g3 receipts all show `positive n10-accept-plus-one
KILLED` only where the behavioural base arms already kill it).

## Risks / blockers

- None blocking. Counter, builder, patches and frozen predicates were never
  edited (no seat may). Scratch clone left at 673d1e2 (reset --hard, clean).
- One counter run at a time respected; each ~50 s.
- Tooling installs: none. No pacman used (paused host-wide; rules file read
  first). Scratch dirs to be removed by the final cleanup pass of this seat.
- Receipts kept in scratch during the wave and copied? No — per bounds the
  patches live under `.ufo/waves/round-95/w1/ExecCounterForgery/`; counter
  receipt text is inline above and the tally lines are exact.

Report: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-95/w1/ExecCounterForgery.md
Patches:
Report: .ufo/waves/round-95/w1/ExecCounterForgery/g1-codeobject-naive.patch
Report: .ufo/waves/round-95/w1/ExecCounterForgery/g2-codeobject-guardaware.patch
Report: .ufo/waves/round-95/w1/ExecCounterForgery/g3-recompile-compare.patch
Report: .ufo/waves/round-95/w1/ExecCounterForgery/g4-inspect-linecache.patch
Report: .ufo/waves/round-95/w1/ExecCounterForgery/g5-argv-tmpdir.patch
