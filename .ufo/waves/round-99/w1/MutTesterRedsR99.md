# MutTesterRedsR99 — C2 counter attack (scratch only)

Seat: `MutTesterRedsR99`. Scope: attack the round-99 C2 counting command
`verifiers/fixtures/round-99/carried-reds.py` (v1) with (a) new forgery worlds on
`b53e209603e7c480cd975ea543e415b66f695438` and (b) counter mutants. No lane file is
written; every edit lives in the scratch clone
`/fast/scratch/hyaku/kotoba-r99/MutTesterRedsR99/repo` (base
`b53e2096`), and the counter is never edited — its mutants are scratch copies.

## Method

1. **Green base W0** (`721fb5af`): the honest route the counter header admits —
   8 coverage-map rows for `corpus/lessons/round-91..98-verifier-spotcheck.md`,
   `corpus/lessons/round-81.md:8` hash quoting, an equal-mode
   `verifiers/corpus-baseline.json` re-record (tracked_files 203, report_total 166,
   commit_total 72), the `SCORECARD.md:158 -> 161` correction-row subject move,
   15 appended `GOVERNANCE_CORRECTIONS` rows for the 15 remaining live dead
   subjects, one appended `LOG.md` notice line (all tokens double-quoted so they
   are not subjects), and one `INSTRUMENT_PINS` admission. W0 is the control: it
   must read `C2-PREDICATE-MET` before any world is believed.
2. **Worlds W1..W10** are single-variation commits on the same base, each aimed at
   one counter conjunct. Every world is measured by the frozen counter with the
   same command and `HYAKU_SCRATCH` root; a world that reads MET without the
   honest content is a counter finding (never a counter edit).
3. **Counter mutants M1..M8** are scratch copies of `carried-reds.py` with one
   minimal edit each (drop a conjunct, weaken `CHECKLIST_PASS_MIN`, accept N/A,
   skip a `literal_eval`). Each is run against the world predicted to isolate the
   mutated conjunct.

Command (all runs):
`HYAKU_SCRATCH=/fast/scratch/hyaku/kotoba-r99/MutTesterRedsR99 python3 -B \
 /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/round-99/carried-reds.py <rev> /fast/scratch/hyaku/kotoba-r99/MutTesterRedsR99/repo`

## W0 control — the honest route reads MET

Receipt `w0-green-base.txt`:

```
checklist PASS lines 11 (min 11); FAIL/N/A lines 0
red ... verify_skill_checklist.py exit 0 GREEN
red ... verify_corpus_integrity.py exit 0 GREEN: 9/9 checks pass
red ... verify_corpus_independent.py exit 0 GREEN: exit 0
selftest ... 1864 / 178 / 109 HELD
frozen ... IDENTICAL / IDENTICAL / IDENTICAL / DATA-ONLY
battery guard ... 5 of 5 PASS
battery fleet root ...; guards 5 of 5; tip battery exit 0: 6 of 6
C2 carried reds green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok
C2-PREDICATE-MET
```

The honest route also heals the battery's own six-gate tally (6 of 6), so W0 is a
valid green base for the isolation worlds.

## Worlds

| world | rev | variation | aim |
|---|---|---|---|
| W0 | `721fb5af` | honest route (control) | MET |
| W1 | `0f27688e` | the two dead receipt subjects are "corrected" to `SKILL.md` (unrelated file) | correction replacement not identity-bound |
| W2 | `9ad51a6a` | corrections block holds a non-literal expression (digest computed at import) + the notice line edited after the fact | `literal_eval` conjunct |
| W3 | `aa4f447b` | horizon 999999 + a correction row citing absent line 4000 | horizon bounded by `len(log_lines)` |
| W4 | `7c13c7e1` | `INSTRUMENT_PINS` entry computed by code (`git hash-object` at import) | pins `literal_eval` conjunct |
| W5 | `1d7d4a1f` | governance check forced PASS in code + pin admission (11 PASS from a forged path, self-test holds) | checklist data-only conjunct |
| W6 | `51c6558a` | one glob row `lessons/round-9*-verifier-spotcheck.md` replaces the 8 index rows | coverage map accepts a wildcard |
| W7 | `0009d013` | the seven earlier `LOG.md` dead citations are rewritten (quoted) instead of corrected by appended notices | governance file not frozen |
| W8 | `7f4cd9cd` | watchdog/l0 rows pinned to pre-existing `LOG.md:2620` / `:779` (no appended notice for them) | "appended notice" not enforced |
| W9 | `ca0bae4a` | W0's changed checklist blob is not pinned | guards conjunct isolation |
| W10 | `e55cf830` | `verifiers/fixtures/checklist/clean/SKILL.md` name altered | selftests conjunct isolation |

## Results (frozen counter, one run per world)

| world | tally line | verdict | caught by |
|---|---|---|---|
| W0 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | **MET** | control |
| W1 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | **MET** | nothing — **F2** |
| W2 | `green 3 of 3; self-tests held 3 of 3; frozen 3 of 4; guards ok` | UNMET | frozen (4): `corrections block not literal data … Call(...)` |
| W3 | `green 2 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | UNMET | reds: `correction LOG.md:4000 … is past horizon 999999 or absent` |
| W4 | `green 3 of 3; self-tests held 3 of 3; frozen 3 of 4; guards ok` | UNMET | frozen (3): `check_tip_battery.py outside INSTRUMENT_PINS CHANGED` (pins `literal_eval`) |
| W5 | `green 3 of 3; self-tests held 3 of 3; frozen 3 of 4; guards ok` | UNMET | frozen (4): `bytes differ outside the corrections data` |
| W6 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | **MET** | nothing — **F4** |
| W7 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | **MET** | nothing — **F1** |
| W8 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards ok` | **MET** | nothing — **F3** |
| W9 | `green 3 of 3; self-tests held 3 of 3; frozen 4 of 4; guards FAIL` | UNMET | guards: `guards 4 of 5` (instrument-pin) |
| W10 | `green 3 of 3; self-tests held 2 of 3; frozen 4 of 4; guards ok` | UNMET | selftests: checklist `--self-test` exit 1, `assertions -1` |

Receipts: `run-W0.txt` … `run-W10.txt` (verbatim counter output). The four MET
worlds (W1, W6, W7, W8) are the counter findings; W9/W10 are isolation controls
that prove the guards and self-test conjuncts are independently falsifiable.

## Counter mutants

Scratch copies at `fakelane/verifiers/fixtures/round-99/` (a clone of the lane at
`b53e2096` so the counter's `parents[3]` lane lookup still reads the frozen base
battery; `--fleet /home/vgpnk/Projects/shokunin` passed explicitly). Each mutant
is one minimal edit; the counter is never edited in the lane.

| mutant | edit | world | pristine | mutant | verdict |
|---|---|---|---|---|---|
| M1-drop-reds | `met` loses `green == 3` | W3 | UNMET (`green 2 of 3`) | **MET** | killed |
| M2-drop-selftests | `met` loses `held == 3` | W10 | UNMET (`self-tests held 2 of 3`) | **MET** | killed |
| M3-drop-frozen | `met` loses `frozen == 4` | W5 | UNMET (`frozen 3 of 4`) | **MET** | killed |
| M4-pass-min-10 | `CHECKLIST_PASS_MIN = 10` | W3C | UNMET (`green 0 of 3`) | UNMET (`green 0 of 3`) | **survives** |
| M5-accept-na | N/A lines no longer counted | W3C | UNMET (`green 0 of 3`) | UNMET (`green 0 of 3`) | **survives alone** |
| M4+M5 | both edits | W3C | UNMET (`green 0 of 3`) | UNMET (`green 1 of 3; frozen 3 of 4`) | survives (frozen still catches) |
| M6-skip-checklist-literal | a non-literal corrections block is accepted | W2 | UNMET (`frozen 3 of 4`) | **MET** | killed |
| M7-skip-pins-literal | a dict-shaped pins block is accepted without `literal_eval` | W4 | UNMET (`frozen 3 of 4`) | **MET** | killed |
| M8-drop-guards | `met` loses `guards_ok` | W9 | UNMET (`guards FAIL`) | **MET** | killed |

W3C is a rebuild of the committed w3 control
(`receipts/ctl-worlds/w3-checklist-gov-na-pinned.patch`) in this scratch clone,
rev `32921fde`; its pristine reading is the committed
`receipts/c2-ctl-w3-checklist-gov-na-pinned.txt` (`green 0 of 3; self-tests held
3 of 3; frozen 3 of 4; guards ok`, `checklist PASS lines 10 (min 11); FAIL/N/A
lines 1`). Receipts: `mut-M1-on-W3.txt` … `mut-M45-on-W3C.txt`.

Kill rule used: a mutant is killed iff the pristine counter reads UNMET on the
world and the mutant counter reads MET on the same world with the same command.
Six of the eight mutants are killed; M4 and M5 survive (see F6).

## Findings

**F1 (high) — the counter does not freeze `LOG.md`/`SCORECARD.md`, so an in-place
rewrite of a governance record reads MET.** World W7 quotes the seven earlier
`LOG.md` dead citations (backticks → double quotes) instead of correcting them
with appended notices; `citation_subjects(exclude_quoted=True)` stops seeing
them, the checklist prints `PASS … 12 recorded correction(s) excused`, and the
counter prints `C2-PREDICATE-MET`. The plan's honest route allows only "one
appended LOG.md correction notice"; the counter freezes the checklist (data-only),
the battery (outside `INSTRUMENT_PINS`) and the two corpus gates, but no conjunct
reads the governance files' bytes. The battery's guards guard `corpus/`,
`verifiers/` and `SKILL.md` (no-deletions) and the six battery scripts
(instrument-size); `LOG.md` is outside every guard. Minimal fix (a predicate
change, an L1 act — not applied): add a fifth frozen conjunct requiring the base
`LOG.md` and `SCORECARD.md` bytes to be a prefix of the REV bytes (append-only),
or require every correction row's notice line to be greater than the base
`LOG.md` length. Evidence: `run-W7-clean.txt` (clean quote form; the first build used a doubled quote pair and was rebuilt).

**F2 (medium-high) — a correction's replacement token is not identity-bound.**
World W1 "corrects" the two dead receipt subjects to `SKILL.md` (an unrelated
file); `correction_problems` only requires `citation_resolve(corrected)`, so the
checklist prints PASS and the counter prints MET while the citation remains
wrong. This is a gap in the checklist gate's own spec ("the replacement must
resolve"), inherited by the counter. Minimal fix: require the corrected token's
basename to equal the stale token's basename, or require the corrected token to
be the `../`-rooted form of the same path (all four round-base rows are of that
form), or require the notice to bind the replacement by path identity. Evidence:
`run-W1.txt`.

**F3 (medium) — the "appended notice" property is not enforced; the wording check
is a substring test.** World W8 pins the `LOG.md:3353`/`:3561` rows to the
pre-existing line 2620 (the round-65 notice) and the `LOG.md:3512` row to line
779; no appended notice names those subjects. Because the corrected token
`../.ufo/watchdog.log` contains the stale token `.ufo/watchdog.log` as a
substring, `stale in text` and `corrected in text` are both satisfied by the old
line, and the horizon 2723 already covers line 2620. The counter prints MET.
Minimal fix: require the notice line to be greater than the subject line (or
greater than the base `LOG.md` length), and require the stale token to occur as
a distinct occurrence, not as a suffix of the corrected token. Evidence:
`run-W8.txt`.

**F4 (low-medium) — one glob coverage row satisfies the corpus index.** World W6
replaces the eight per-file rows with `lessons/round-9*-verifier-spotcheck.md`;
the integrity gate reads `9/9 checks pass`, the independent gate exit 0, and the
counter prints MET. The gate's documented spec allows globs (`expand_pattern`
uses `fnmatch`), so this is a gate-design weakness, not a counter bug: the
counter's "content fix" route cannot distinguish a per-file index from a
wildcard. Minimal fix (gate, not counter): require at least one exact-path row
per tracked corpus file, or cap a glob row's fan-out, or record the fan-out in
the baseline. Evidence: `run-W6.txt`.

**F5 (informational) — the self-test fixtures are outside every frozen set;
conjunct (2) is their only detector.** World W10 alters
`verifiers/fixtures/checklist/clean/SKILL.md` (`name: clean` → `not-clean`); the
checklist self-test exits 1 and the counter reads `self-tests held 2 of 3` →
UNMET. The fixture edit passes frozen (4 of 4) and guards (5 of 5): the fixtures
are not in `FROZEN`, not in `INSTRUMENT_PINS`, and not in the guards'
spotcheck set. The arm works, but a fixture the self-test does not read would be
invisible; no such fixture was found (the self-test cases exercise the committed
fixtures). Evidence: `run-W10.txt`.

**F6 (informational) — `CHECKLIST_PASS_MIN` and the N/A rejection are not
independently falsifiable by any admitted world.** M4 alone leaves the N/A world
red (the N/A line still counts); M5 alone leaves it red (10 PASS < 11); the pair
turns the checklist green (`green 1 of 3`) but the world still fails frozen
(`3 of 4`, a code change), so the verdict stays UNMET. A data-only world cannot
produce an N/A line (the governance check returns N/A only when
`governance_enabled` is false, an environment condition) and cannot reduce the
11-check count. The two arms are defense-in-depth against code changes already
caught by conjunct (4). Evidence: `mut-M4-on-W3C.txt`, `mut-M5-on-W3C.txt`,
`mut-M45-on-W3C.txt`.

**F7 (informational) — the `reds` conjunct is load-bearing and independently
falsifiable.** W3's horizon/absent-line row makes the checklist red while the
corpus gates stay green (`green 2 of 3`); M1 flips it to MET. The horizon is
correctly bounded by `min(horizon, len(log_lines))`, so a row citing a line that
does not exist is refused.

**F8 (informational) — reporting truncation.** The counter's `last()` truncates
each gate's final line to 300 chars, so the `red …` receipt line shows only the
first two governance problems (the base tree has 17 dead subjects + 1 correction
problem). The tally is unaffected; a reader must run the gate itself to see the
full list. `probe_gov.py` in this directory enumerates them.

**F9 (medium) — the committed forgery controls are not conjunct-isolating, and
the counter has no self-test of its own.** The counter exposes no `--self-test`
(the "selftests" conjunct runs the three gates' self-tests); its conjuncts are
controlled only by the worlds. Of the five committed controls, only w2 isolates
a conjunct (`green 0 of 3`, everything else green → kills M1). w1 fails four
conjuncts at once (`green 2 of 3; self-tests 1 of 3; frozen 2 of 4; guards
FAIL`), w3 fails two (`green 0 of 3; frozen 3 of 4`), w4 fails two (`green 1 of
3; frozen 3 of 4`), w5 fails two (`green 0 of 3; frozen 3 of 4`) — so under any
single conjunct-drop mutant they still read UNMET. M2, M3, M6, M7 and M8 are
killed only by the purpose-built isolation worlds W10, W5, W2, W4 and W9. This
is a control-design gap, not a predicate hole: the counter's verdict is correct
on every world measured, but the pre-data set does not demonstrate that each
conjunct is load-bearing. Minimal fix: add the isolation worlds (or a
`--self-test` that runs the counter against them) to the frozen control set.

## Restoration / bounds

- The lane was never written: all worlds are commits in the scratch clone; the
  base commit `b53e2096` is byte-identical and every counter run read the frozen
  lane instrument (`carried-reds.py` sha256
  `5f964253755e0d69f7651a0be43288aaad60fec3ba6c5a25328f5619972bf358`).
- The counter was never edited: the mutants are scratch copies under
  `fakelane/verifiers/fixtures/round-99/`; the lane copy is untouched.
- Scratch dir `/fast/scratch/hyaku/kotoba-r99/MutTesterRedsR99` is removed before
  the final answer; receipts are copied under this directory first.

