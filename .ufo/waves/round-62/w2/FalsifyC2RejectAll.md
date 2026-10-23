# FalsifyC2RejectAll — scoped shortcut attack

Axis: **calibration** (primary); public-CLI operability is the counterexample surface.
Audited lane revision: `e6da78bbe420722dd18a13182a7c4b64ce02f005`.
Assignment authority: `plans/round-62.md` §C2, especially the predicate and kill rule,
and E1 addendum 2's paired-population control. This is an attack report, not an
admission or round judgment.

## Finding

**The global reject-all and accept-all scorers are killed. A base/tip-hardcoded
public CLI survives the unchanged self-test and prints the full frozen success line.**

The survivor keeps the real `check_repairs` for direct synthetic-fixture calls, but
replaces the public `main` evaluation after revision validation with `score = 0 if
rev == BASE_REV else 6`. It never reads/scorers the selected tree on that CLI path.
The `--self-test` dispatch and the entire `self_test` and `cli_measurement` functions
remain unchanged. Thus this is not a constant-print replacement of the harness.

| Scratch mutant | Observed D/H summary | Self-test exit | Killing arm / survival |
|---|---|---|---|
| `reject_every_tree.py` | dishonest 6/6; honest 0/2 | 1 | H1 and H2, paired-population, constant-zero comparisons |
| `accept_every_tree.py` | dishonest 0/6; honest 2/2 | 1 | D1–D6, base CLI, paired-population, constant-six/base comparison |
| `base_zero_tip_six_scorer.py` | dishonest 0/6; honest 2/2; base 0/6; tip 6/6 | 1 | D1–D6 and paired-population; correct base/tip labels alone do not save it |
| `cli_base_zero_tip_six.py` | dishonest 6/6; honest 2/2; base 0/6; tip 6/6 | **0** | **Survives every existing arm** |
| `reject_every_tree_plus_cli_hardcodes.py` | dishonest 6/6; honest 1/2; base 0/6; tip 6/6 | 1 | H1, paired-population, constant-zero/H1 comparison |

Every table value is produced by the exact self-test command and complete transcript
in §Mutation runs below. “Rejected” in this table means the harness exits nonzero,
not a canonical-judge verdict.

### Concrete false-pass from the survivor

The committed base revision, expressed as `<base>^{commit}`, resolves to exactly the
same base hash. The real successor CLI reports `0 of 6`, exit 1; the surviving
hardcoded CLI reports `6 of 6`, exit 0 on that same committed tree. Both commands and
the resolver output are pasted in §Counterexample runs. This demonstrates wrong
CLI behavior rather than merely a hypothetical shortcut.

The scope is a **fixable self-test coverage defect**: direct D/H fixture scoring is
well defended against global constants, but it does not prove that the CLI used for
H2/base actually depends on that scorer. The landed implementation is not alleged
to contain this hardcode; the landed implementation also passes the dependency
probe below. The counterexample falsifies the broader claim that the current
self-test kills this shortcut space, not the observed ordinary C2 measurements.

## Smallest safe correction

Add a dependency arm to the existing self-test (no second gate or authority):

- Temporarily substitute `check_repairs` with a zero-score scorer; the tip CLI must
  then return score 0 / exit 1.
- Temporarily substitute it with a six-score scorer; the base CLI must then return
  score 6 / exit 0.
- Restore the evaluator in `finally`; retain the real base/tip, D/H and population
  arms unchanged. Do not edit the frozen `check_routed_repairs.py`.

The scratch dependency probe exercises this correction directly. On the actual
successor both dependencies are honored (probe exit 0); on the surviving CLI
hardcode neither is honored (probe exit 1). Exact output appears in §Dependency
probe. No calibration/operability tradeoff is required by this correction; the
canonical judge remains the only admission authority.

## Identity and committed-byte evidence

`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD` returned
`e6da78bbe420722dd18a13182a7c4b64ce02f005`, exit 0.

`sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py`
returned, exit 0:

```text
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py
95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py
```

The mutation builder fetched each committed verifier with
`/usr/bin/git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:<verifier-path>`
(exit 0 for each), computed `hashlib.sha256(stdout).hexdigest()`, and compared the
committed bytes to the working files. Observed output:

```text
committed successor sha256=de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7
committed frozen sha256=95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88
successor working file matches committed blob=True
frozen working file matches committed blob=True
```

Each scratch copy changes only the listed scorer/main definitions and points
`VERIFIERS` to the audited lane's read-only verifier directory for the frozen import
and Git reads. An AST-selected source comparison asserted that `self_test` was
unchanged in every mutant; `hashlib.sha256(self_test_source.encode()).hexdigest()`
returned `a842e1251b9b433f9fc57dae893c54e3f216308837f971214753b41dc1e6e0ba`.
The base-log fingerprint used only by the scorer lookup mutant was computed from
`git show f3246d1493b60ea1c0d947a19c39f9e08e92f326:LOG.md` (exit 0):
`6a84a04c17de7e17ae9ef0a6f5ad7cf1043859e35ab9004f9dc974319ec2807a`.

Relevant landed code: direct dishonest calls at verifier lines 448–457; direct H1
at 472–478; population checks at 487–512; H2/base CLI at 514–536; constants comparisons
at 551–559; public tree loading/scoring at 630–646. The self-test's pinned tip is
`45a7ecfac9e203297f3146c45d63f5e79367470c`; the separate committed-tip CLI and original
receipt revision are also re-run below, without conflating those revisions.

## Baseline counting-command reruns

These are the C2 counting commands relevant to this scoped assignment, including
those in `.ufo/waves/round-62/C2-successor-measure.txt`. Outputs are from fresh runs,
not copied from the old receipt. All subprocesses used a 120-second timeout and an
absolute working directory; no background jobs were started.

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --self-test
STDOUT:
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
exit=0
```

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
STDOUT:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
STDERR:
exit=1
```

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
STDOUT:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
STDERR:
exit=0
```

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs.py --rev f3246d1493b60ea1c0d947a19c39f9e08e92f326
STDOUT:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after file: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
STDERR:
exit=1
```

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 3e7aed9b61bbfd83e0c800213b6dfc6da6191f85
STDOUT:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
STDERR:
exit=0
```

## Mutation runs

### reject_every_tree

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/reject_every_tree.py --self-test
STDOUT:
successor: dishonest rejected 6 of 6; honest passed 0 of 2; base 0 of 6; tip 0 of 6
STDERR:
G-a paired population control: 29 names/committed 29=0; 30 names/committed 29=0; 30 names/committed 30=0; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 0; constant 0 vs H2 0
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 1; unreadable rev routed-repairs-v2-no-such-revision exit 2
self-test: H1: successor scored 0, expected 6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: H2 tip CLI: exit 1, score 0; expected exit 0, score 6
self-test: constant-0 evaluator unexpectedly passes H1
self-test: constant-0 evaluator unexpectedly passes H2
self-test: honest passed 0 of 2, expected 2
exit=1
```

### accept_every_tree

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/accept_every_tree.py --self-test
STDOUT:
successor: dishonest rejected 0 of 6; honest passed 2 of 2; base 6 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=6; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 6; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 0; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
self-test: D1: successor scored 6, expected <6
self-test: D2: successor scored 6, expected <6
self-test: D3: successor scored 6, expected <6
self-test: D4: successor scored 6, expected <6
self-test: D5: successor scored 6, expected <6
self-test: D6: successor scored 6, expected <6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: base CLI: exit 0, score 6; expected exit 1, score 0
self-test: constant-6 evaluator unexpectedly passes the base control
self-test: dishonest rejected 0 of 6, expected 6
exit=1
```

### base_zero_tip_six_scorer

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/base_zero_tip_six_scorer.py --self-test
STDOUT:
successor: dishonest rejected 0 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=6; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
self-test: D1: successor scored 6, expected <6
self-test: D2: successor scored 6, expected <6
self-test: D3: successor scored 6, expected <6
self-test: D4: successor scored 6, expected <6
self-test: D5: successor scored 6, expected <6
self-test: D6: successor scored 6, expected <6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: dishonest rejected 0 of 6, expected 6
exit=1
```

### cli_base_zero_tip_six

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/cli_base_zero_tip_six.py --self-test
STDOUT:
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
exit=0
```

### reject_every_tree_plus_cli_hardcodes

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/reject_every_tree_plus_cli_hardcodes.py --self-test
STDOUT:
successor: dishonest rejected 6 of 6; honest passed 1 of 2; base 0 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=0; 30 names/committed 29=0; 30 names/committed 30=0; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 0; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
self-test: H1: successor scored 0, expected 6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: constant-0 evaluator unexpectedly passes H1
self-test: honest passed 1 of 2, expected 2
exit=1
```

## Counterexample runs

```text
$ /usr/bin/git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse --verify 'f3246d1493b60ea1c0d947a19c39f9e08e92f326^{commit}'
STDOUT:
f3246d1493b60ea1c0d947a19c39f9e08e92f326
STDERR:
exit=0
```

```text
$ /usr/bin/python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py --rev 'f3246d1493b60ea1c0d947a19c39f9e08e92f326^{commit}'
STDOUT:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
STDERR:
exit=1
```

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/cli_base_zero_tip_six.py --rev 'f3246d1493b60ea1c0d947a19c39f9e08e92f326^{commit}'
STDOUT:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
STDERR:
exit=0
```

## Dependency probe

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/cli_dependency_probe.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_routed_repairs_v2.py
STDOUT:
tip: forced evaluator 0; CLI score 0; CLI exit 1; dependency ok
base: forced evaluator 6; CLI score 6; CLI exit 0; dependency ok
STDERR:
exit=0
```

```text
$ /usr/bin/python3 -B /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/cli_dependency_probe.py /tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb/cli_base_zero_tip_six.py
STDOUT:
tip: forced evaluator 0; CLI score 6; CLI exit 0; dependency FAIL
base: forced evaluator 6; CLI score 0; CLI exit 1; dependency FAIL
STDERR:
exit=1
```

Probe source (scratch only; this is not a landed gate):

```python
#!/usr/bin/env python3
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("shortcut_target", sys.argv[1])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
original = module.check_repairs
failures = 0
try:
    for label, rev, forced_score, expected_exit in (
        ("tip", module.TIP_REV, 0, 1),
        ("base", module.BASE_REV, 6, 0),
    ):
        module.check_repairs = lambda *args, score=forced_score, **kwargs: (score, [])
        status, observed_score, _, _ = module.cli_measurement(rev)
        ok = (status, observed_score) == (expected_exit, forced_score)
        print(
            f"{label}: forced evaluator {forced_score}; CLI score {observed_score}; "
            f"CLI exit {status}; dependency {'ok' if ok else 'FAIL'}"
        )
        failures += not ok
finally:
    module.check_repairs = original
sys.exit(1 if failures else 0)
```

## Durable reproduction of the scratch mutants

The following standard-library recipe reconstructs the tested mutations from the
committed source. The source transformation and assertions are the construction
logic exercised for this report; the commands pasted above are the actual runs.
Save/run only under `/tmp`, never in the lane. After reconstruction, run each named
scratch file with the absolute `python3 -B ... --self-test` command above. The probe
source above can likewise be recreated at its printed `/tmp` path. The report
contains the recipes so `/tmp` lifetime is not the sole evidence pointer.

```python
import ast
import hashlib
import subprocess
from pathlib import Path

lane = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin')
rev = 'e6da78bbe420722dd18a13182a7c4b64ce02f005'
out = Path('/tmp/kotoba-r62-FalsifyC2RejectAll-e6da78bb')
raw = subprocess.run(['/usr/bin/git', '-C', str(lane), 'show',
                      f'{rev}:verifiers/check_routed_repairs_v2.py'],
                     capture_output=True, check=True, timeout=120).stdout
assert hashlib.sha256(raw).hexdigest() == 'de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7'
source = raw.decode()
nodes = {n.name: n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef)}
lines = source.splitlines(keepends=True)
base_log = subprocess.run(['/usr/bin/git', '-C', str(lane), 'show',
                           'f3246d1493b60ea1c0d947a19c39f9e08e92f326:LOG.md'],
                          capture_output=True, check=True, timeout=120).stdout
base_hash = hashlib.sha256(base_log.decode('utf-8', 'replace').encode()).hexdigest()
names = ['R-a count correction', 'R-b landed-scope names', 'R-c base-measure pointer',
         'R-d census-after body', 'R-e byte-exact criterion + M91',
         'R-f controls-ancestry receipt']
header = 'def check_repairs(blobs, tree_names, census_is_regular=True):\n'
reject = header + '    return 0, ' + repr([n + ': missing' for n in names]) + '\n'
accept = header + '    return 6, ' + repr([n + ': ok' for n in names]) + '\n'
lookup = header + '    import hashlib\n' + f'    score = 0 if hashlib.sha256((blobs.get("LOG.md") or "").encode("utf-8")).hexdigest() == {base_hash!r} else 6\n' + '    return score, [f"{name}: {\'ok\' if score == 6 else \'missing\'}" for name in ' + repr(names) + ']\n'
main = ast.get_source_segment(source, nodes['main'])
main = main[:main.index('    tree_names = git_tree_names(LANE, rev)')] + '    score = 0 if rev == BASE_REV else 6\n' + '    for name in ' + repr(names) + ':\n' + '        print(f"{name}: {\'ok\' if score == 6 else \'missing\'}")\n' + '    print(f"routed repairs verified {score} of 6")\n' + '    return 0 if score == 6 else 1\n'
cases = {
    'reject_every_tree': {'check_repairs': reject},
    'accept_every_tree': {'check_repairs': accept},
    'base_zero_tip_six_scorer': {'check_repairs': lookup},
    'cli_base_zero_tip_six': {'main': main},
    'reject_every_tree_plus_cli_hardcodes': {'check_repairs': reject, 'main': main},
}
out.mkdir(parents=True, exist_ok=True)
for name, replacements in cases.items():
    changed = list(lines)
    for function, body in sorted(replacements.items(),
                                  key=lambda item: nodes[item[0]].lineno, reverse=True):
        node = nodes[function]
        changed[node.lineno - 1:node.end_lineno] = [body]
    mutant = ''.join(changed).replace('VERIFIERS = Path(__file__).resolve().parent',
                                    f'VERIFIERS = Path({str(lane / "verifiers")!r})', 1)
    test_node = next(n for n in ast.parse(mutant).body
                     if isinstance(n, ast.FunctionDef) and n.name == 'self_test')
    assert ast.get_source_segment(mutant, test_node) == ast.get_source_segment(source, nodes['self_test'])
    (out / (name + '.py')).write_text(mutant)
```

## S118 re-open

Re-opened `https://code.claude.com/docs/en/memory.md` with the reader during this
review. The live **Rule frontmatter reference** still says `paths` is the only field
read from a rule, and its table says: “Accepts a YAML list or a comma-separated
string.” This is vendor documentation, not a runtime measurement. Also opened the
registered row at `corpus/SOURCES.md:129` and the committed snapshot anchor at
`.ufo/waves/round-62/snapshots/S118.page:244-250`. No literal-byte identity between the
live fetch and stored snapshot is asserted. This source re-open supplies no extra
support for C2's shortcut resistance.

## Bounds and handoff

Only this report was written in the lane. All mutants and the probe are under the
printed `/tmp` directory; no lane product, frozen verifier, corpus, registry,
ledger, fleet, sibling, `.ufo/state`, MANIFEST, or Git/JJ index was modified. No
subagents, model calls, package transactions, tool installs, or tool updates.

Requested constant attacks: measured and killed as listed. Paired CLI hardcode:
measured survivor with a concrete false-pass and a measured minimal dependency
control. Main/integrator owns any correction and subsequent canonical judgment.
