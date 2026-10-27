# A05RevControls — Q37 control-world adequacy

**Axes:** depth, consistency, calibration, freshness, coverage, operability, adjacency.
**Verdict: FINDING — C2 R2 accepts a valid but stale revision named as “tip” and copied gate-output bytes; the counter's core check scores the shortcut 4/4 (exit 0).** The custom world was scored through the same `check(FakeRepo(...))` path used by the counter's self-test, not through a committed fixture/`--rev` CLI invocation; this limitation is explicit below.

## Controls committed in `plans/round-76.md` § “Controls before data (Q37)”

| Control | World | Expected rejection |
|---|---|---|
| C1-W1 | Fabricated stub entry + empty snapshots | Low count, exit 1 |
| C1-W2 | Real quotes from the held `best-practices` snapshot (wrong page) | Page-unique arm rejects |
| C1-W3 | Token dump naming all six conjuncts, no content | Fails |
| C2-W1 | Token dump: repair files with forged values | Fails |

The plan says receipts are under `receipts/` before data and counter bytes are hashed into the freeze receipt. `plans/round-76-addendum-1.md` corrects C1(a) and the render convention but adds no controls. These committed controls do not exercise C2-R2's valid-stale-revision/copy-transcript shortcut.

## One shortcut built and scored (C2)

The R2 receipt is required to name the “tip revision on its first line” and carry both gates' stdout and exit codes. In `verifiers/check_r75_routed_repairs.py` `r2_receipt` (lines 349–388), the first-line revision is accepted if it is (a) an ancestor of the measured revision and (b) at/after `R75_TIP`; the code does not require it to equal the measured tip. Receipt text is only checked for gate-name substrings, an `exit=0`-shaped token within 800 characters, absence of `DRIFT`, and presence of `PASS`. The actual gate rerun is at the revision the receipt names; its output is not compared with the recorded transcript.

I made one real-input shortcut: starting from the counter's own satisfying `_honest()` self-test world, I changed only the R2 receipt. Its first line names `R75_TIP` (`ac9f29510d3914a6edb97c8dbdb3445cab9141de`), a valid ancestor, while the remaining receipt bytes are copied verbatim from the real base battery after its header (`.ufo/waves/round-76/base-battery/base-battery.txt`), which records the two gate commands and their `exit=0` results at the different base revision `b7f13f4b39cbd43076a85568adca763a6f674e7a`. Thus the receipt calls an older revision “tip” and its transcript is from another revision, while preserving all other honest fixture conjuncts. This is not C2-W1's forged/empty token dump.

### Score evidence

Frozen counter file SHA-256 at scoring: `bdc1e490f751174393d9e1ff69188f8ae7a6a420ae2850a70c66eb6b6a1ceb38`.

Exact scoring command (Python `-B`; exit 0). This imports that counter and calls its own `check()` on the same `FakeRepo` fixture interface its self-test uses; the only mutation to `_honest()` is the R2 receipt text described above. The copied stdout bytes are read from the named base-battery file. The fixture's gate rerun values are the self-test's green values, not a claim that this custom world was committed or exercised by `main --rev`:

```sh
python3 -B - <<'PY'
import importlib.util, sys, pathlib
p='/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py'
b='/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-76/base-battery/base-battery.txt'
spec=importlib.util.spec_from_file_location('c2',p); m=importlib.util.module_from_spec(spec); sys.modules['c2']=m; spec.loader.exec_module(m)
w=m._honest(); source=pathlib.Path(b).read_text().splitlines(keepends=True)
r75=m.R75_TIP
w['files'][m.NOHARM_RECEIPT]=r75+'\\n'+''.join(source[1:])
w['gates']={'integrity_exit':0,'integrity_out':'PASS\\n','independent_exit':0,'independent_out':'PASS\\n'}
w['ancestors'].add(r75)
repo=m.FakeRepo(**w); closed, findings=m.check(repo)
print('r2_receipt findings:',m.r2_receipt(repo))
print('score:',f'r75 routed repairs closed {closed} of {m.TOTAL}')
print('exit=',0 if closed==m.TOTAL else 1)
PY
```

Observed stdout (command exit 0):

```text
r2_receipt findings: []
score: r75 routed repairs closed 4 of 4
exit= 0
```

The R2 result is not dependent on the other arms being absent: the unmodified counter's own `--self-test` passes its honest world and rejects its listed must-fail arms (23 assertions, exit 0), while the custom world changes only the receipt. Exact self-test command:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --self-test
```

Observed tail: `PASS real-git arm: honest fixture closes 4 of 4`; `PASS real-git arm: token-dump fixture rejected (exit 1)`; exit 0.

The counter's specified red-at-base CLI control was also run:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_r75_routed_repairs.py --rev b7f13f4b39cbd43076a85568adca763a6f674e7a
```

Observed `r75 routed repairs closed 0 of 4`, exit 1 (the shell wrapper recorded `exit=1`). This confirms the red control, not the custom shortcut's CLI behavior.

## Limit / interpretation

The result demonstrates that the mechanical R2 predicate does not bind the receipt's claimed tip to the measured tip and does not authenticate recorded stdout against the named revision. It does **not** establish a committed lane revision whose CLI run returns 4/4 on this mutant: seat restrictions prohibit committing or changing the lane index, and I did not perform a git write. The custom score is the counter's exact core check on its documented self-test fixture interface, not a full `main --rev` run. No counter self-test or base result is represented as the custom world's CLI output.

**VERDICT: C2 R2 shortcut ACCEPTED by frozen core check — `r75 routed repairs closed 4 of 4`, exit 0; receipt names valid ancestor R75_TIP but carries base-revision gate stdout.**