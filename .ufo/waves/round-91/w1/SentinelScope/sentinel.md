# r91-w1 sentinel verdicts (SentinelScope, scope and safety)

Candidate: `d3f5e1920c315d2ec49faade5b9e6cf6b0f4172a` = base `9af1a7af2adf0ab07cfd53f92affc1ed8d992262`
plus `ExecBatteryArms.patch`, `ExecFloorsCap.patch`, `ExecLadder.patch` (REPAIRABLE), `ScribeCorpus.patch`.
Built in scratch clone `/fast/scratch/hyaku/kotoba-r91/SentinelScope-28/repo` (toplevel verified). No patch changed.

READY inputs: ExecBatteryArms `N=25 rc=0`; ExecFloorsCap `blob=6f2c52fb2e09e817dff3360b97400a5d6e53626c selftest_N=176 rc=0`;
ExecLadder `verdict=REPAIRABLE rc=0`; ScribeCorpus 4 files, census 187 -> 190.

## (1) changed paths within the plan touch list — PASS (file level), FINDING (intra-file)

Command: `git -C "$D" diff --name-only 9af1a7af2adf0ab07cfd53f92affc1ed8d992262`
Observed (10 paths):
```
corpus/SOURCES.md
corpus/knowledge/mutation-battery-arms-round91.md
corpus/knowledge/timeout-calibration-round91.md
corpus/lessons/round-91.md
verifiers/check_assertion_floors.py
verifiers/check_freeze_gate.py
verifiers/check_mutation_battery.py
verifiers/check_tip_battery.py
verifiers/fixtures/mutation-battery/manifest.tsv
verifiers/floors-registry.json
```
Extra paths against the touch list: none.

FINDING F1 (scope, ownership): `verifiers/floors-registry.json` changes TWO values, not one.
Plan touch list: "`verifiers/floors-registry.json` — `floors_guard` floor value only." ExecFloorsCap ownership: "floors-registry.json (the floors_guard row ONLY)."
Observed in `git diff -- verifiers/floors-registry.json`:
```
-      "floor": 150,      (floors_guard)
+      "floor": 176,
-      "floor": 30,       (freeze_gate)
+      "floor": 31,
```
The `freeze_gate` 30→31 bump is outside the named edit. The candidate is not blocked by it (the bump is consistent with ExecLadder's new arm), but the L1 must either record it as an amendment before scoring or revert that one line. Not repaired here (no patch changes).

## (2) no hardcoded /tmp; new code honours TMPDIR or --work — PASS

Command: `git -C "$D" diff 9af1a7a... | grep -n '^+.*/tmp'` → `(none)`.
Command: `git diff -- '*.py' | grep -nE '^\+.*(tempfile\.|mkdtemp|TemporaryDirectory|gettempdir)'` → `(none)` (no added tempdir call sites).
Observed TMPDIR/--work honouring in candidate scripts:
- `verifiers/check_mutation_battery.py:426 ap.add_argument("--work", help="scratch directory (clone, probe TMPDIR, record)")`
- `verifiers/check_mutation_battery.py:296 env=clean_env(TMPDIR=str(tmp))`
- `verifiers/check_freeze_gate.py:222 env["TMPDIR"] = tmpdir`; `:254 work_root = os.environ.get("TMPDIR") or tempfile.gettempdir()` (pre-existing line).

## (3) no sysctl, /proc/sys, network call, credential or token in added code — PASS

Command: `git diff -- '*.py' '*.json' '*.tsv' | grep -nE '^\+' | grep -iE 'sysctl|/proc/sys|urllib|urlopen|socket|requests\.|http\.client|curl|wget|token|secret|password|passwd|api[_-]?key|credential|environ'` → `(none)`.
Also `added .py lines with a URL` → `(none)`; `os.environ|getenv|sysctl` in added .py → `(none)`.
Note (not a violation): the unfiltered grep hit prose only: `tokenize` in `corpus/knowledge/mutation-battery-arms-round91.md`, and source-citation URLs (`pitest.org`, `docs.python.org`, `en.wikipedia.org`) inside `corpus/SOURCES.md` and knowledge/lesson prose. No counter performs a network call.

## (4) INSTRUMENT_PINS blob = hash-object of check_assertion_floors.py — PASS

Command: `git -C "$D" hash-object verifiers/check_assertion_floors.py` → `6f2c52fb2e09e817dff3360b97400a5d6e53626c`.
Pin in candidate `verifiers/check_tip_battery.py` (line 134–141):
```
"verifiers/check_assertion_floors.py": (
    "780f6fe5184ecb94e70f0f79446ae4339d1aec27",
    "50348420260ab41a916ef1ab19d27966565de5af",
    "9cb860bda21ef8d24fcb0603aa85372b96f3ac41",
    # round-91 claim C2 leg A(d) admission ...
    "6f2c52fb2e09e817dff3360b97400a5d6e53626c"),
```
`grep -c 6f2c52fb… verifiers/check_tip_battery.py` → `1`. Equal; the three earlier blobs are kept.

## (5) no edit to a frozen file — PASS

`git diff 9af1a7a -- verifiers/check_r86_routed_repairs_v3.py` → 0 lines; same for `verifiers/verify_corpus_integrity.py`, `verifiers/corpus-baseline.json`, `SKILL.md` (all 0 diff-lines). Spotcheck files changed: `0` (`grep -c verifier-spotcheck` over the changed-name list).

## (6) SOURCES patch appends only — PASS

Command: `git -C "$D" diff 9af1a7af… -- corpus/SOURCES.md | grep '^-' | grep -v '^---'` → `(none — append only)`.
Added rows: S262 (PIT, tier A), S263 (Python subprocess docs, tier A), S264 (Wikipedia, REJECTED per its own row text).
Census: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` base 187, candidate 190.

FINDING F2 (plan arithmetic, not a candidate defect): the frozen plan expects "Census before→after: 187 → 189 expected" (plans/round-91.md Frontier step). The owned item appends S262, S263 AND one rejection row, which is three rows → 190. The candidate's 190 matches the item; the plan's 189 expectation is internally inconsistent. Route to the L1 as a recorded note; do not edit the plan.

## Extra scope checks (beyond the six, from the touch list)

- `verifiers/fixtures/mutation-battery/manifest.tsv`: `grep -cP '\tkill\t'` 14 → 17; removed lines: none; +3 rows naming `check_mutation_battery.py` (mb-m2, mb-m15, mb-m16). Matches "exactly +3 kill rows".
- `verifiers/check_tip_battery.py`: one removed line (the closing `)` of the tuple, re-emitted with a trailing comma); the rest is the appended pin. Append-only in substance.
- `verifiers/check_freeze_gate.py`: one existing `except OSError` line widened to `(OSError, UnicodeError)` plus one new self-test arm `arm_plan_not_utf8`. In scope for ExecLadder leg B.
- `verifiers/check_mutation_battery.py`: not in the tip battery `BATTERY` list (no instrument-pin required).

## Residuals for the L1 (not sentinel failures)

- `corpus/README.md` index rows for the three new corpus files, `LOG.md`, `SCORECARD.md`, `PROVINCE.md` § Core are touch-list items outside every builder's ownership. Absent from the candidate; L1 integration must add them.
- The candidate has no `plans/round-91-addendum-*.md`; none is needed unless F1 is amended.

## Verdict summary

| check | verdict |
|---|---|
| 1 touch list | PASS at file level; F1 (floors-registry freeze_gate 30→31 outside "floors_guard row ONLY") |
| 2 /tmp and TMPDIR | PASS |
| 3 sysctl/network/credential | PASS |
| 4 INSTRUMENT_PINS blob | PASS (6f2c52fb…) |
| 5 frozen files | PASS |
| 6 SOURCES append-only | PASS; F2 plan arithmetic 189 vs 190 |

The candidate is safe to hand to the attack seats. F1 needs an L1 decision (amend or revert one line) before scoring.
