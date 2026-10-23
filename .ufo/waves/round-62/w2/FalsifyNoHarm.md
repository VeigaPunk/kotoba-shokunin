# FalsifyNoHarm — scoped no-harm evidence review

## Counterexample and disposition

**No complete no-harm pass was measured by this seat.** The serial battery run against assigned tip `e6da78bbe420722dd18a13182a7c4b64ce02f005` exited **124** at the permitted deadline, during `floors`. It did not reach `no-harm OK` or the battery's final failure summary. The completed arm output includes a `check-ptr` failure; later arms are **unmeasured**, not passing.

The historical receipt `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-tip.txt` measures `3e7aed9b61bbfd83e0c800213b6dfc6da6191f85`, not the assigned tip. Its registry/unindexed-file failures cannot serve as current failures: both corresponding arms passed in this seat's later run. Conversely, neither incomplete receipt establishes full no-harm.

**Impacted axes:** operability (the battery did not finish within this seat's allowed command deadline) and calibration (a partial receipt cannot support a full-pass statement). This is a fixable measurement/reporting gap, not evidence authorizing an axis trade. No admission, score change, or canonical judgment is made here.

## Exact battery invocation and output

Executed as one foreground battery invocation, without subagents or background jobs, from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`:

```sh
timeout --signal=TERM --kill-after=2s 117s bash /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-battery.sh --base a745411c66d4765e9ac0ce48f1d96c34f425dab4 --tip e6da78bbe420722dd18a13182a7c4b64ce02f005 --sandbox /tmp/kotoba-r62-FalsifyNoHarm-e6da78bb --keep
```

Exact stdout before termination:

```text
noharm: lane        /home/vgpnk/Projects/shokunin/kotoba-shokunin
noharm: base        a745411c66d4765e9ac0ce48f1d96c34f425dab4
noharm: tip         e6da78bbe420722dd18a13182a7c4b64ce02f005
noharm: sandbox     /tmp/kotoba-r62-FalsifyNoHarm-e6da78bb
noharm: date -u     2026-10-23T21:33:25Z
noharm: column base ready (a745411c66d4765e9ac0ce48f1d96c34f425dab4)
noharm: column tip ready (e6da78bbe420722dd18a13182a7c4b64ce02f005)
--- arms ---
PASS  reg_gate    exit 0 in both columns (base=0 tip=0)
PASS  corpus      tip introduces no new DRIFT kind (base set: corpus.index.tracked_files: corpus.index.unindexed: corpus.pointers.commit_total: corpus.pointers.commit_unresolvable: corpus.pointers.report_total: )
PASS  corpus-idx  no new unindexed corpus file at tip (base set: corpus/lessons/round-60-verifier-spotcheck.md )
PASS  sources     exit 0 in both columns (base=0 tip=0)
PASS  checklist   tip introduces no new failing check id (base set: governance.citation_resolves: )
FAIL  check-ptr   unresolved citation pointers grew (base=2 tip=4)
        tip: FAIL governance.citation_resolves: evaluated 1155 — LOG.md:2533: '.ufo/reports/round-60/kotoba.md' does not resolve from
        tip:  LOG.md:2558: '.ufo/waves/round-62/census-after.txt' does not resolve from
        tip:  SCORECARD.md:158: '.ufo/reports/round-60/kotoba.md' does not resolve from
        tip:  SCORECARD.md:369: '.ufo/reports/round-62/kotoba.md' does not resolve from
PASS  boxproof    exit 0 in both columns (base=0 tip=0)
```

Tool result: `Wall time: 117.00 seconds`; `Command exited with code 124`. A terminal was requested but unavailable; the tool explicitly reported running without one. No extra deadline or background continuation was used.

### Bound on `floors` and subsequent arms

The retained base `floors.txt`, read at `/tmp/kotoba-r62-FalsifyNoHarm-e6da78bb/logs/base/floors.txt`, contained:

```text
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
```

The retained tip `floors.txt`, read at `/tmp/kotoba-r62-FalsifyNoHarm-e6da78bb/logs/tip/floors.txt`, contained only:

```text
PASS harness observed=10 floor=10
PASS corpus_integrity observed=152 floor=152
PASS corpus_independent observed=99 floor=93
PASS surfaces observed=175 floor=175
PASS checklist observed=1852 floor=1852
PASS pins observed=62 floor=62
```

These are child observations from the interrupted command, **not** a paired `floors` verdict; no paired exit receipt was produced. `agentdefs`, `explicit`, `desc`, `mcp`, `plugin`, `hooks`, `scoped`, `absorption`, `repairs-v2`, `scoped-v31`, and `battery-self*` were not reached by this run. Neither were the informational live-fetch commands. Their current results are not asserted.

## Distinguishing the pointer findings from final-tip state

The parent subsequently instructed this seat to retain the command bound, not rerun the entire battery, and distinguish the following:

- **Census pointer:** missing in the measured `e6da78bb` checkout; subsequently committed at `3f911504ce76d9ca186f297d6d4a9cd8ed77508a`. I opened that committed file with the command below, which exited `0` and printed its validator body plus recorded `exit=0`. This establishes that the file now exists at that revision; it is not a new census execution by this seat.
- **Round report pointer:** the parent corrected the current working-tree SCORECARD pointer to `../.ufo/reports/round-62/kotoba.md` and explained that the fleet report lands after lane work. I read the current literal line and observed `Report \`../.ufo/reports/round-62/kotoba.md\` (fleet repo, sibling of this lane).` This is **expected-if-unlanded**, not a lane-product defect. The committed SCORECARD at `3f911504…`, separately opened below, still printed the older lane-local spelling; do not attribute the working-tree spelling to that commit.
- The round-60 report pointers already appear in the base failure set; the run does not establish them as new round-62 harm.

Commands exercised for committed pointer context, each with exit `0`:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 3f911504ce76d9ca186f297d6d4a9cd8ed77508a:.ufo/waves/round-62/census-after.txt
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 3f911504ce76d9ca186f297d6d4a9cd8ed77508a:SCORECARD.md
```

The completed-arm transcript above remains the exact result for its named measured revision. **No newer full-battery result is inferred from pointer repairs.**

## Committed arm inventory

Commands used to identify the script:

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
# e6da78bbe420722dd18a13182a7c4b64ce02f005; exit 0
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:.ufo/waves/round-62/noharm-battery.sh | sha256sum
# 21b6075bc830e23bbcfa8476907a72b01460ef51f81d1bb6cbe9d494196f8309  -; exit 0
sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-battery.sh /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-tip.txt
# 21b6075bc830e23bbcfa8476907a72b01460ef51f81d1bb6cbe9d494196f8309  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-battery.sh
# 2bbef4e9b009d6f94e86d94b8070213186ab6e8120392f93ce78feaf77806b6a  /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-62/noharm-tip.txt
# exit 0
```

The following is a self-contained rendering of the executed Python evaluation cells (setup inlined and variable names shortened), not a separately rerun command. Each `git show` subprocess exited `0`. The code counts verdict-arm call sites, deduplicating the mutually exclusive success/failure branches of each battery self-check. It does **not** count explanatory comments, INFO echoes, helper definitions, or verifier child assertions. The first attempt tokenized unrelated continued shell lines and raised `ValueError: No escaped character` (tool exit `1`); the corrected counting cell succeeded (tool exit `0`).

```python
import hashlib, shlex, subprocess
lane = '/home/vgpnk/Projects/shokunin/kotoba-shokunin'
path = '.ufo/waves/round-62/noharm-battery.sh'
revisions = (
    'e6da78bbe420722dd18a13182a7c4b64ce02f005',
    '3f911504ce76d9ca186f297d6d4a9cd8ed77508a',
)
scripts = []
for rev in revisions:
    result = subprocess.run(
        ['git', '-C', lane, 'show', f'{rev}:{path}'],
        capture_output=True, timeout=20)
    result.check_returncode()
    scripts.append(result.stdout.decode())
    print('sha256=' + hashlib.sha256(result.stdout).hexdigest())
print('battery bytes identical across reviewed tips=' + str(scripts[0] == scripts[1]))
script = scripts[0]
lines = script.splitlines()
start = next(i for i, line in enumerate(lines)
             if line.startswith('# ============================ ARMS'))
names, locations, optional_calls = [], [], []
commands = {'cmp_exit0', 'cmp_unchanged', 'cmp_no_new_kind',
            'cmp_no_new_unindexed', 'cmp_no_new_pointer',
            'tip_self_test_optional', 'tip_self_test_required', 'report'}
for number, line in enumerate(lines[start:], start=start + 1):
    first = line.strip().split(maxsplit=1)
    if not first or first[0] not in commands:
        continue
    tokens = shlex.split(line, comments=True)
    name = None
    if tokens[0] in ('cmp_exit0', 'cmp_unchanged', 'cmp_no_new_kind'):
        name = tokens[1]
    elif tokens[0] == 'cmp_no_new_unindexed':
        name = 'corpus-idx'
    elif tokens[0] == 'cmp_no_new_pointer':
        name = 'check-ptr'
    elif tokens[0] in ('tip_self_test_optional', 'tip_self_test_required'):
        name = tokens[1]
        if tokens[0] == 'tip_self_test_optional':
            optional_calls.append(line)
    elif tokens[0] == 'report' and tokens[1].startswith('battery-self'):
        name = tokens[1]
    if name and name not in names:
        names.append(name)
        locations.append((number, name))
print('gating report arms=' + str(len(names)))
print('inherited comparison arms=' + str(len(names[:names.index('absorption')])))
print('successor arms=' + str(sum(n in ('absorption', 'repairs-v2', 'scoped-v31') for n in names)))
print('battery self-verification arms=' + str(sum(n.startswith('battery-self') for n in names)))
print('optional successors=' + str(len(optional_calls)))
for number, name in locations:
    print(f'L{number}: {name}')
```

Observed hash and successful count lines, collated from the setup and corrected counting cells:

```text
sha256=21b6075bc830e23bbcfa8476907a72b01460ef51f81d1bb6cbe9d494196f8309
sha256=21b6075bc830e23bbcfa8476907a72b01460ef51f81d1bb6cbe9d494196f8309
battery bytes identical across reviewed tips=True
gating report arms=21
inherited comparison arms=15
successor arms=3
battery self-verification arms=3
optional successors=2
L332: reg_gate
L335: corpus
L336: corpus-idx
L339: sources
L342: checklist
L343: check-ptr
L346: boxproof
L349: floors
L352: agentdefs
L355: explicit
L358: desc
L361: mcp
L364: plugin
L367: hooks
L373: scoped
L377: absorption
L378: repairs-v2
L379: scoped-v31
L394: battery-self
L408: battery-self2
L423: battery-self3
```

Thus the committed script has **21 potential verdict arms: 15 inherited comparisons + 3 successor self-tests + 3 battery self-checks**. Optional absence substitutes a SKIP for its successor verdict. This is an inventory, **not** a claim that the interrupted run exercised those arms.

## Absent-optional behavior exercised

The normal battery invocation did not reach its optional arms. To test absence without altering any lane or verifier file, I separately executed the exact committed `tip_self_test_optional` helper and its exact committed call sites against an empty temporary `TIP_TREE`. No verifier stub or substitute counter was used. The executed Python probe is rendered below with variable names aligned to the self-contained counting code above:

```python
import tempfile
helper = script[script.index('tip_self_test_optional() {'):
                script.index('\ntip_self_test_required() {')]
with tempfile.TemporaryDirectory(prefix='kotoba-r62-FalsifyNoHarm-absent-') as tip:
    probe = ('set -u -o pipefail\nTIP_TREE=' + shlex.quote(tip) +
             '\nFAILURES=0\n' + helper + '\n' +
             '\n'.join(optional_calls) +
             '\nprintf "FAILURES=%s\\n" "$FAILURES"\n')
    result = subprocess.run(['bash', '-c', probe],
                            capture_output=True, text=True, timeout=20)
    print(result.stdout, end='')
    print(result.stderr, end='')
    print(f'absent-optional probe exit={result.returncode}')
```

Exact output:

```text
SKIP check_erratum_absorption.py (not landed)
SKIP check_routed_repairs_v2.py (not landed)
FAILURES=0
absent-optional probe exit=0
```

The absent-optional arms therefore visibly print `SKIP`, not `PASS`, and do not increment `FAILURES`. The required `scoped-v31` helper is separate; no absence-pass behavior for it is claimed.

## Smallest safe correction and evidence limits

Keep the old and this new bounded receipt revision-qualified. Describe no-harm as **not fully measured**, not passed. Carry the corrected census pointer and the fleet-relative report pointer into the final committed records, with the latter expected to resolve only after the fleet report lands. The L1's final evidence must name any completed-arm outputs and any unfinished arms; this seat's deadline does not justify extending process bounds or replacing the real floor/fetch arms with faster substitutes.

No product, verifier, frozen counter, corpus, fleet file, state file, index, or routing change was made. Only this scoped report was written in the lane. No tool was installed or updated. Scratch clone/log paths in the transcript are historical measurement locations; their relevant output is copied above and the seat-owned sandbox is removed after report creation. No full battery, source census, successor self-test, live fetch, or canonical judge is claimed beyond the explicit executions above.
