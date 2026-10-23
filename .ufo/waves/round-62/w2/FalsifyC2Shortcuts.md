# FalsifyC2Shortcuts — calibration

## Scoped result

The pathname-only lookup is killed, but the constant-transcript and blob-tree-identity lookups survive the unchanged committed self-test. Both survivors print the frozen signature and return exit 0; their captured stdout and stderr strings also equal the unmodified baseline. This is a fixable anti-shortcut/calibration defect, not an axis tradeoff or an admission judgment.

Target: `e6da78bbe420722dd18a13182a7c4b64ce02f005`. The reproduction loads both Python modules directly from that commit with read-only `git show`, preserving the self-test, CLI, fixture builders, and frozen scorer. It replaces only the in-memory successor `check_repairs`; it does not alter the lane verifier or its fixtures. Module digests and interpreter version appear under the `metadata` command below.

| Candidate | Frozen signature? | Exit | What happened |
|---|---|---|---|
| Unmodified committed evaluator | yes | 0 | Baseline reproduces the receipt. |
| Constants keyed only by sorted `tree_names` | no | 1 | Killed by H1, G-a paired-population, and base CLI arms. |
| Constants keyed by an input blob-tree fingerprint | yes | 0 | No repair predicates execute in the replacement. |
| Constant call-order transcript, inspecting no inputs | yes | 0 | All arms, including the purported constants control, accept it. |

Every measurement in this table comes from the corresponding absolute-path command in **Exact command records**. The fingerprint is a SHA-256 of the serialized evaluator inputs, not a Git tree object ID and not a pathname-only lookup.

## Counterexample and evidence

The strongest survivor is the following replacement. Its scores are literal constants selected by invocation position, not computed from input blobs, pathnames, revision, or census metadata:

```python
scores = iter((5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 0))
def check_repairs(blobs, tree_names, census_is_regular=True):
    return constant_result(next(scores))
```

The tuple follows the unchanged harness's calls: D1–D6; H1; population-29; population-30/stale; population-30/declared; H2 CLI; base CLI. The unreadable-revision CLI arm returns before calling this evaluator. `constant_result` only emits fixed reason labels alongside the selected score. See the full scratch reproduction below.

Relevant committed locations:

- `plans/round-62.md:150-152` requires the D/H arms to be blob-computed, not asserted; the addendum at `:303-306` claims stronger constants/content/population controls.
- `verifiers/check_routed_repairs_v2.py:363-430` constructs the D maps and path lists; `:459-478` constructs H1. D2–D6, H1 and population-29 have identical pathname lists. The stale and corrected population-30 cases also have identical pathname lists. The metadata command additionally observes identical base/H2 pathname lists. A deterministic pathname-only function cannot satisfy these conflicting requirements. The measured pathname lookup fails as expected.
- `:480-512` supplies a real same-repair-blobs/different-population discrimination and a same-population/different-declaration discrimination. This kills the pathname-only lookup but does not challenge a precomputed whole-input lookup or the call-order transcript.
- `:551-559` does **not** substitute a constant evaluator. It compares literal `6`/`0` values against already-required base/H scores. Once those earlier requirements hold, these comparisons cannot distinguish the real evaluator from either survivor. Nevertheless `:571-575` prints `label-only constants fail controls` for both survivors.
- `:594-608` prints the same frozen sentence and returns success for both survivors. The frozen scorer still runs independently inside the unchanged harness, so its expected D/H transcript does not demonstrate successor computation.
- `.ufo/waves/round-62/C2-successor-measure.txt:8-29` contains the baseline diagnostics and frozen signature reproduced by these commands. The surviving replacements produce those same captured stdout/stderr strings, not merely a matching summary assembled outside the harness.

The identity lookup is an independent, stateless shortcut: it prepares a table of literal expected scores for known fixture/revision input fingerprints, then returns a table entry. It reads inputs to form an identity key but never evaluates repair properties. It also passes. This distinguishes resistance to pathname-only names from resistance to memorized fixture identity.

## Impacted axis and smallest safe correction

**Calibration / consistency-calibration:** the diagnostic overstates what the controls discriminate. The baseline measurement itself reproduces; the counterexample concerns its claimed resistance to asserted/labelled scores. No product behavior, other axis, round verdict, or canonical judgment is inferred here.

Smallest safe correction to the demonstrated controls: add a real candidate-evaluator challenge arm that repeats/reorders already-scored fixtures and supplies fresh semantically invariant input changes (for example, an irrelevant newline outside the criterion), plus same-name verdict-flipping changes. Declare expected directions independently from those changes, and exercise pass and fail sides. Repetition/order changes kill this transcript; fresh invariant identities kill this lookup. Actually substitute these shortcut evaluators as negative controls and require their rejection, rather than inferring mutant rejection from literal comparisons. Retain the frozen scorer unchanged. Describe the resulting finite discrimination honestly; no finite known-fixture suite proves immunity to every possible lookup.

This report proposes a correction only; no lane product, verifier, corpus, index, state, or sibling file was edited. No tool was installed or updated. Only the expressly assigned harness runs were exercised.

## Exact command records

All commands run synchronously; scratch runner subprocesses use a timeout and read-only Git commands. `stdout` and `stderr` are recorded separately, followed by the actual process return code.

```text
$ python3 -B /tmp/kotoba62-shortcuts.MuNZ63j9/attack.py metadata
[stdout]
revision=e6da78bbe420722dd18a13182a7c4b64ce02f005
python=3.14.8
verifiers/check_routed_repairs.py sha256=95ade9be1ed1930266bce4b98c8c593fff1feba89e2cf25763f0aa83f206cb88
verifiers/check_routed_repairs_v2.py sha256=de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7
D1: names=35; expected=5; names_key=e748c2dd9f4b76ab15f4686fe7d00d1828db5299f0b349b8b2161e7b1a02734c; blob_tree_key=b24fb3a474a1a589b478906b10183bef52c6603aac7e73b9c51f76b34913a524
D2: names=34; expected=5; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=dd254bcb9770fec77135bdf407eeff0a1ae274a58ebf31370f6c8db872f7cc14
D3: names=34; expected=5; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=3a0140e563f3d59e5c807ef070103434cf42e87e31bc1bb8468a3dc9b1b08ed8
D4: names=34; expected=5; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=ed3127261abb06c00cb192e4fd6a98786212b5d44f3c6981e6ad085d9ed36870
D5: names=34; expected=5; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=3ffcdd3b7826b81ada701436f0cb9c360fb2432571146062be6d9b30c0dcbab8
D6: names=34; expected=5; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=4f5b0038ca1b6a21567b34ef8052940771cfff13a172632b4a066de33d0af334
H1: names=34; expected=6; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=d6b8c62c773b17a1b69c471d8f999bfe059859596b098b99d317326fa0c854d9
population29: names=34; expected=6; names_key=f35576cc49fedd9bf09caa52b9496bddf96d4a9f4f5553a4388475245353ce00; blob_tree_key=29be9601c829a3ab52f947b509478ea620fc9f95540b95d687a3c113db7ceae8
population30-stale: names=35; expected=5; names_key=e748c2dd9f4b76ab15f4686fe7d00d1828db5299f0b349b8b2161e7b1a02734c; blob_tree_key=b24fb3a474a1a589b478906b10183bef52c6603aac7e73b9c51f76b34913a524
population30-declared: names=35; expected=6; names_key=e748c2dd9f4b76ab15f4686fe7d00d1828db5299f0b349b8b2161e7b1a02734c; blob_tree_key=3b5522837b19c66859c03e2d79aacde919c765f29b61013e65c5a2fc43fe38bd
H2: names=33; expected=6; names_key=9b0880cf9aab8db57a4506248eec2ddcb73485f4c5f0b9a031d596e7a0407e51; blob_tree_key=f5eb6b918f82778cf2485c8656bd293977a274cbe3f036837b296bad499b666f
base: names=33; expected=0; names_key=9b0880cf9aab8db57a4506248eec2ddcb73485f4c5f0b9a031d596e7a0407e51; blob_tree_key=cf5973ac8d49511732f11d6a79c0e7dd6d9619a02ffa22260da9480e715b20e0
D2/H1 names identical=True
population30-stale/declared names identical=True
base/H2 names identical=True
[stderr]
[exit=0]
```

```text
$ python3 -B /tmp/kotoba62-shortcuts.MuNZ63j9/attack.py baseline
[stdout]
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
[stderr]
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
[exit=0]
```

```text
$ python3 -B /tmp/kotoba62-shortcuts.MuNZ63j9/attack.py tree-names
[stdout]
successor: dishonest rejected 6 of 6; honest passed 1 of 2; base 6 of 6; tip 6 of 6
[stderr]
G-a paired population control: 29 names/committed 29=5; 30 names/committed 29=5; 30 names/committed 30=5; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 6; constant 0 vs H1 5; constant 0 vs H2 6
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
self-test: H1: successor scored 5, expected 6
self-test: G-a paired population control did not score 29/pass, 30/stale/fail, 30/declared/pass
self-test: base CLI: exit 0, score 6; expected exit 1, score 0
self-test: constant-6 evaluator unexpectedly passes the base control
self-test: honest passed 1 of 2, expected 2
[exit=1]
```

```text
$ python3 -B /tmp/kotoba62-shortcuts.MuNZ63j9/attack.py blob-tree-lookup
[stdout]
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
[stderr]
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
[exit=0]
```

```text
$ python3 -B /tmp/kotoba62-shortcuts.MuNZ63j9/attack.py constant-transcript
[stdout]
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
[stderr]
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
[exit=0]
```

### Comparison over the captured results

The following Python comparison was run in the tool session after the process calls above (no harness rerun):

```python
frozen_signature = 'successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6\n'
for mode in ('baseline', 'tree-names', 'blob-tree-lookup', 'constant-transcript'):
    result = attack_results[mode]
    print(f'{mode}: frozen_signature={result.stdout == frozen_signature}; exit={result.returncode}; stdout_equals_baseline={result.stdout == attack_results["baseline"].stdout}; stderr_equals_baseline={result.stderr == attack_results["baseline"].stderr}')
```

```text
baseline: frozen_signature=True; exit=0; stdout_equals_baseline=True; stderr_equals_baseline=True
tree-names: frozen_signature=False; exit=1; stdout_equals_baseline=False; stderr_equals_baseline=False
blob-tree-lookup: frozen_signature=True; exit=0; stdout_equals_baseline=True; stderr_equals_baseline=True
constant-transcript: frozen_signature=True; exit=0; stdout_equals_baseline=True; stderr_equals_baseline=True
```

## Complete scratch reproduction

Saved and executed as `/tmp/kotoba62-shortcuts.MuNZ63j9/attack.py`. This report embeds its source so the evidence does not depend on scratch-file retention. Save this block under an absolute scratch path and run the modes above; all repository access remains read-only and pinned to the stated commit.

```python
#!/usr/bin/env python3
"""Read-only round-62 C2 shortcut attacks against the committed self-test."""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
import types
from pathlib import Path

LANE = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin')
REV = 'e6da78bbe420722dd18a13182a7c4b64ce02f005'
DIGESTS = {}


def load_committed(name, relative):
    result = subprocess.run(
        ['git', '-C', str(LANE), 'show', f'{REV}:{relative}'],
        capture_output=True, check=True, timeout=120,
    )
    DIGESTS[relative] = hashlib.sha256(result.stdout).hexdigest()
    module = types.ModuleType(name)
    module.__file__ = str(LANE / relative)
    sys.modules[name] = module
    exec(compile(result.stdout, module.__file__, 'exec'), module.__dict__)
    return module


frozen = load_committed('check_routed_repairs', 'verifiers/check_routed_repairs.py')
v2 = load_committed('shortcut_target', 'verifiers/check_routed_repairs_v2.py')
REPAIR_NAMES = (
    'R-a count correction', 'R-b landed-scope names', 'R-c base-measure pointer',
    'R-d census-after body', 'R-e byte-exact criterion + M91',
    'R-f controls-ancestry receipt',
)


def constant_result(score):
    return score, [f"{name}: {'ok' if index < score else 'missing'}"
                   for index, name in enumerate(REPAIR_NAMES)]


def names_key(tree_names):
    return tuple(sorted(tree_names))


def blob_tree_key(blobs, tree_names, census_is_regular=True):
    # Identity only: no parsing/scoring of any repair property.
    encoded = json.dumps(
        [sorted(blobs.items()), sorted(tree_names), census_is_regular],
        ensure_ascii=True, separators=(',', ':'),
    ).encode('utf-8')
    return hashlib.sha256(encoded).hexdigest()


def house_style_map():
    h1 = v2.make_fixture_blob_map(29)
    h1['LOG.md'] = (
        '# Iteration log\n\n## 2026-10-23 — Round 61 (house style)\n'
        '- Round-60 build reports: claimed 32, committed 29; counted at `'
        '.ufo/waves/round-60/build`.\n'
        '- R-b landed scope includes `plans/round-60.md` and '
        '`considerthese/2026-10-23.md`.\n'
        '- R-c: the base measurement is receipts/freeze2-selftest.txt;\n'
        '  C1-measure.txt is NOT the base pointer.\n\n## Round 62 — next entry\n'
    )
    h1['.ufo/waves/round-61/receipts/controls-ancestry.txt'] = (
        f'$ git merge-base --is-ancestor {v2.HASH_CTL} {v2.HASH_DATA}\nexit=0\n'
    )
    return h1


def known_cases():
    for label, blobs in v2.dishonest_fixture_maps().items():
        yield label, blobs, v2.fixture_tree_names(blobs), True, 5
    h1 = house_style_map()
    yield 'H1', h1, v2.fixture_tree_names(h1), True, 6
    pop29 = v2.make_fixture_blob_map(29)
    yield 'population29', pop29, v2.fixture_tree_names(pop29), True, 6
    pop30 = dict(pop29)
    pop30[f'{v2.BUILD_DIR}/ExecSynthetic30.md'] = 'synthetic build report 30\n'
    yield 'population30-stale', pop30, v2.fixture_tree_names(pop30), True, 5
    declared = dict(pop30)
    declared['LOG.md'] = str(declared['LOG.md']).replace('committed 29', 'committed 30', 1)
    yield 'population30-declared', declared, v2.fixture_tree_names(declared), True, 6
    for label, rev, score in [('H2', v2.TIP_REV, 6), ('base', v2.BASE_REV, 0)]:
        blobs = {path: v2.git_show(LANE, rev, path) for path in v2.INPUT_PATHS}
        names = v2.git_tree_names(LANE, rev)
        assert names is not None
        regular = v2.git_regular_blob(LANE, rev, '.ufo/waves/round-61/census-after.txt')
        yield label, blobs, names, regular, score


mode = sys.argv[1]
if mode == 'metadata':
    print(f'revision={REV}')
    print(f'python={platform.python_version()}')
    for path, digest in DIGESTS.items():
        print(f'{path} sha256={digest}')
    cases = list(known_cases())
    for label, blobs, names, regular, expected in cases:
        print(f'{label}: names={len(names)}; expected={expected}; '
              f'names_key={hashlib.sha256(repr(names_key(names)).encode()).hexdigest()}; '
              f'blob_tree_key={blob_tree_key(blobs, names, regular)}')
    print('D2/H1 names identical=' + str(names_key(cases[1][2]) == names_key(cases[6][2])))
    print('population30-stale/declared names identical=' + str(
        names_key(cases[8][2]) == names_key(cases[9][2])))
    print('base/H2 names identical=' + str(names_key(cases[11][2]) == names_key(cases[10][2])))
    raise SystemExit(0)

if mode == 'tree-names':
    # The table uses path names only. Conflicting verdicts cannot all be represented.
    table = {}
    for label, blobs, names, regular, score in known_cases():
        table.setdefault(names_key(names), score)

    def check_repairs(blobs, tree_names, census_is_regular=True):
        return constant_result(table.get(names_key(tree_names), 0))

    v2.check_repairs = check_repairs
elif mode == 'blob-tree-lookup':
    # Expected scores are literals above, never derived by either repair scorer.
    table = {}
    for label, blobs, names, regular, score in known_cases():
        key = blob_tree_key(blobs, names, regular)
        if key in table:
            assert table[key] == score
        table[key] = score

    def check_repairs(blobs, tree_names, census_is_regular=True):
        return constant_result(table.get(blob_tree_key(blobs, tree_names, census_is_regular), 0))

    v2.check_repairs = check_repairs
elif mode == 'constant-transcript':
    # D1..D6, H1, population29, population30-stale, population30-declared, H2, base.
    scores = iter((5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 0))

    def check_repairs(blobs, tree_names, census_is_regular=True):
        # Deliberately inspect no input, label, call stack, revision, or metadata.
        return constant_result(next(scores))

    v2.check_repairs = check_repairs
elif mode != 'baseline':
    raise SystemExit(f'unknown mode: {mode}')

# Everything except the evaluator is the unchanged source from the committed revision.
raise SystemExit(v2.main(['--self-test']))
```
