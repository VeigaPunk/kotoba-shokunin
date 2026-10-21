verdict: BROKEN — `verify_surfaces.py --self-test` survives five of six assigned single-site regressions; only the priority-array span mutant is killed.

# Scope and axes

Target: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. All source references below are repository-relative `path:line` at that commit, not line numbers after mutation. This is a lane-authored mutation finding, not round admission or non-author closure.

Axes: **freshness** (sensitivity to reverted opencode loader patterns/default), **operability** (read-tool caller and default CLI argument), **calibration** (what the claimed 99-assertion self-test actually detects). I tested the five requested mutation categories. The plural fallback category was split into two independent mutations so that only one behavior-bearing site was changed at a time.

Canonical-layout scratch repo:

```
/fast/scratch/kotoba-r47/w2/W2SurfSelfTestMut-2/kotoba-shokunin
```

Production source was read-only. No siblings, lane Git/jj state, fleet records, or runtime state were changed. Only this report and the two uniquely named evidence artifacts were written in the lane. No subagents, other orchestration runtimes, omp sessions, opencode executables, package managers, or tool installs were invoked.

## Actual detector and controls

The bounded assigned detector was always:

```sh
python3 verifiers/verify_surfaces.py --self-test
```

It ran from the scratch repo with a 60-second subprocess timeout. The initial pristine run exited **0**, stdout exactly `0 failure(s) over 99 assertions`. I then ran it once on each single-site mutant and once after each exact restoration: **13 invocations total**. Each previous restoration is the next mutant's pristine byte state; no additional pristine invocations are implied. Every restored invocation exited **0**, stdout exactly `0 failure(s) over 99 assertions`.

All invocations also emitted the same three expected stderr errors for the deliberately nonexistent `NO-SUCH.txt`, `NO-SUCH.md`, and `NO-SUCH.json` negative fixtures. Those are part of the passing self-test, not baseline failures. No run timed out or crashed. Full unabridged stdout/stderr and commands are in `W2SurfSelfTestMut.results.json`.

# Results

| ID | Single changed site | Mutant `--self-test` exit / stdout summary | Assigned-detector verdict | Restored exit |
|---|---|---|---|---|
| M1 | `verifiers/verify_surfaces.py:396-399`: restore the authentic round-14 `OC_REMOTE_FILTER_RE` | 0 / `0 failure(s) over 99 assertions` | **SURVIVED** | 0 |
| M2 | `verifiers/verify_surfaces.py:480`: remove `and OC_READ_TOOL_FN in dump` from OC-4's predicate | 0 / `0 failure(s) over 99 assertions` | **SURVIVED** | 0 |
| M3 | `verifiers/verify_surfaces.py:370`: remove trailing `[^\]]{0,200}` from `OC_PRIORITY_RE` | 1 / `1 failure(s) over 99 assertions` | **KILLED** | 0 |
| M4a | `verifiers/verify_surfaces.py:451-453`: remove OC-1's fallback `owns` list | 0 / `0 failure(s) over 99 assertions` | **SURVIVED — diagnostic metadata** | 0 |
| M4b | `verifiers/verify_surfaces.py:464`: remove OC-2's fallback `owns` list | 0 / `0 failure(s) over 99 assertions` | **SURVIVED — diagnostic metadata** | 0 |
| M5 | `verifiers/verify_surfaces.py:130`: revert opencode's default binary to `/home/vgpnk/.opencode/bin/opencode` | 0 / `0 failure(s) over 99 assertions` | **SURVIVED** | 0 |

Thus the assigned suite kills **1/6** independently tested sites. Two survivors concern diagnostic ownership only; they are not evidence of a pass/fail bypass. The other three concern the remote-loader predicate, read-tool predicate, and CLI default. Supplemental arms below actually distinguish all five survivors, but were **not integrated into the suite** and do not change their SURVIVED verdicts.

## M1 — round-14 remote matcher survives despite recreating the known false positive

Mutation at `verifiers/verify_surfaces.py:396-399`:

```python
OC_REMOTE_FILTER_RE = re.compile(
    r'\.instructions.{0,40}?startsWith\("https://"\).{0,40}?startsWith\("http://"\)'
)
```

This is the actual round-14 expression, extracted with `git show 29c17be:verifiers/verify_surfaces.py` and AST source selection, not a guessed approximation.

The current code explicitly documents this regression at `verifiers/verify_surfaces.py:390-391`: the old pattern also matches the declared-list loop. OC-3b's final predicate still separately requires the render marker at `verifiers/verify_surfaces.py:473-477`.

**Why the existing arm misses it:** `verifiers/fixtures/surfaces/strings-opencode-drop-oc3b.txt:12-14` retains the local `for ... instructions` loop but drops **both** the remote filter and the renderer. Even the overbroad matcher fails OC-3b when the renderer is absent. The drop-rule assertions at `verifiers/verify_surfaces.py:1035-1048` therefore remain green without exercising the filter's independent necessity.

**Concrete counterexample / killing arm:** start from `strings-opencode-clean.txt` and remove only its line 13:

```javascript
w=(T.instructions??[]).filter((q)=>q.startsWith("https://")||q.startsWith("http://"))
```

Keep the local loop at line 11 and `Instructions from: ` at line 14. Run `check_opencode_extract` against `baseline-clean.json`, asserting rejection and OC-3b's missing class. The supplied supplemental `remote-filter-only` arm does this.

Observed pristine → mutated → restored:

- Arm process exit **0 → 1 → 0**.
- Gate boolean **false → true → false**.
- Mutated detail: `opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.
- Pristine/restored reject with `opencode:config/instructions-remote` and unmatched `OC-3b`.

This is an exercised false-positive regression hidden by the 99-assertion suite, not a claim that the landed strict matcher itself is broken.

## M2 — ReadTool.execute necessity is not independently tested

Only the behavior-bearing term at `verifiers/verify_surfaces.py:480` was removed. `OC_READ_TOOL_FN`'s definition and the diagnostic anchor list at lines 428 and 483 remained unchanged. The resulting predicate requires only `Instruction.resolve` and `<system-reminder>`.

**Why the existing arm misses it:** `verifiers/fixtures/surfaces/strings-opencode-drop-oc4.txt:16-17` removes the entire OC-4 group: resolver, caller, and injected token. The suite's `strings-opencode-drop-oc4.txt` case at `verifiers/verify_surfaces.py:1041-1048` therefore cannot establish that the new caller requirement matters independently.

**Concrete counterexample / killing arm:** remove only `strings-opencode-clean.txt:17`:

```javascript
$=s.fn("ReadTool.execute")(function*(a,g){
```

Retain `Instruction.resolve` and `<system-reminder>` at lines 16 and 18. The supplemental `read-tool-only` arm asserts `check_opencode_extract` rejects this dump.

Observed pristine → mutated → restored:

- Arm process exit **0 → 1 → 0**.
- Gate boolean **false → true → false**.
- Mutant again reports all **9/9 classes, 7/7 rules** extracted.
- Pristine/restored reject with `opencode:read-hook/instructions` and unmatched `OC-4`.

The new anchor's rationale is documented at `verifiers/verify_surfaces.py:421-426`, but its necessity is not protected by the assigned suite.

## M3 — priority-array trailing-span regression is killed by the right assertion

At `verifiers/verify_surfaces.py:370`, replace the expression with:

```python
OC_PRIORITY_RE = re.compile(r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"\]')
```

The planted fixture appends `GUIDE.md` **after** `CONTEXT.md` at `verifiers/fixtures/surfaces/strings-opencode-planted-name.txt:8`.

Actual output identifies exactly one failing assertion:

```
self-test FAIL: oc-planted-name: names opencode:instructions/GUIDE.md undeclared
1 failure(s) over 99 assertions
```

The existing arm is `verifiers/verify_surfaces.py:1065-1070`. This is a sound kill: the mutant still produces gate exit 1, but loses the entire OC-1 match and does **not** name `GUIDE.md` as undeclared. Therefore the exit-only assertion at line 1068 still passes; the class-specific assertion at lines 1069-1070 kills it. Pristine and exact-restored runs both pass.

## M4a / M4b — fallback ownership metadata is not asserted

These were separate probes, never simultaneous.

- M4a replaces the conditional assignment at `verifiers/verify_surfaces.py:451-453` with `owns = ["opencode:instructions/%s" % n for n in names]`.
- M4b changes only the first argument line of the OC-2 rule call at `verifiers/verify_surfaces.py:464` to `rule("OC-2", owns2,`.

The rule report contract is stated at `verifiers/verify_surfaces.py:435-436`; the helper records `owns` even when unmatched at lines 440-445. Fallbacks do not add extracted IDs on a missing match. Their removal degrades **per-rule attribution**, not the boolean rejection result.

**Why the existing arm misses them:** `check_opencode_extract` independently prints `declared - extracted` at `verifiers/verify_surfaces.py:740-743`. The drop-fixture assertions at lines 1045-1048 only require exit 1, a failing check, and a class name somewhere in the complete output. The class therefore still appears even when the unmatched rule's `owns` is empty. Unmatched empty ownership is rendered as `no class id (shape witness)` at lines 748-752.

**Concrete counterexamples / killing arms:** call `extract_opencode_classes("")`, select each rule report, and assert both `matched is False` and its exact `owns` list:

- OC-1: `opencode:instructions/AGENTS.md`, `opencode:instructions/CLAUDE.md`, `opencode:instructions/CONTEXT.md`.
- OC-2: `opencode:config/AGENTS.md`, `opencode:claude-home/CLAUDE.md`.

The supplemental `fallback-oc1` and `fallback-oc2` arms were each run on pristine, its own mutant, and restored source. Each produced process exits **0 → 1 → 0**. In each mutant the selected report still has `matched: false` but `owns: []`; pristine/restored retain the expected lists. These are exercised diagnostic-coverage findings, not gate-pass escapes.

## M5 — default-binary reversion is invisible to fixture-only self-testing

At `verifiers/verify_surfaces.py:130`, replace the new npm-cache path with:

```python
"opencode": "/home/vgpnk/.opencode/bin/opencode",
```

The CLI uses this default at `verifiers/verify_surfaces.py:1125-1127`. However, the self-test helper always supplies `--opencode-strings` at lines 850-855, bypassing the binary default through `load_dump` at lines 230-234. Its other explicit fixture invocations do the same. Consequently, all 99 assertions still pass.

**Concrete counterexample / killing arm:** the supplemental `default-opencode` arm checks `build_parser().parse_args([]).opencode_binary` against the tip's declared npm-cache path, without opening or executing either binary.

Observed pristine → mutated → restored arm exits are **0 → 1 → 0**. The mutant's actual parsed default is `/home/vgpnk/.opencode/bin/opencode`; pristine/restored parse `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`.

This demonstrates a missing default-wiring assertion. It does not independently establish either path's current existence, binary digest, or live default-resolution outcome; those were outside this probe.

# Reproduction and commands

The clone setup ran successfully, exit **0**, with empty stdout/stderr:

```sh
# cwd: /fast/scratch/kotoba-r47/w2/W2SurfSelfTestMut-2
for p in /home/vgpnk/Projects/shokunin/* /home/vgpnk/Projects/shokunin/.ufo; do
  n=$(basename "$p")
  [ "$n" = kotoba-shokunin ] || ln -sfn "$p" "$n"
done &&
git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin kotoba-shokunin &&
git -C kotoba-shokunin checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f
```

Read-only history commands from the scratch repo all exited **0**:

```sh
git diff c61a973b2e02e1ded169703ddcb06466f4edd8bd 7ad7fadfc09354b74fb66605dfb0c1182c115a2f -- verifiers/verify_surfaces.py
git log --oneline --all -- verifiers/verify_surfaces.py
git show 29c17be:verifiers/verify_surfaces.py
```

For each mutation, apply only its replacement above to a fresh canonical-layout tip clone, run the bounded assigned command, then restore exact bytes and run the same command again. Mutation and restoration edits used the surgical edit tool, not a source-rewriting script. No commit was necessary because this self-test executes the working-tree verifier and committed fixtures; no corpus gate or fault harness was run.

The five supplemental arms actually ran as `python3 -c SCRIPT CASE` with 30-second subprocess deadlines. Their exact script, full shell-quoted commands, exit codes, and outputs are in `W2SurfSelfTestMut.results.json`; the identical script is also retained as `W2SurfSelfTestMut.arm.txt`. A convenient equivalent reproduction command is:

```sh
# cwd: a canonical-layout scratch clone; apply only the selected mutant first
ARM=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2SurfSelfTestMut.arm.txt
python3 "$ARM" remote-filter-only  # M1
python3 "$ARM" read-tool-only      # M2
python3 "$ARM" fallback-oc1        # M4a
python3 "$ARM" fallback-oc2        # M4b
python3 "$ARM" default-opencode   # M5
```

Each applicable arm exits 0 on pristine/restored source and 1 on its respective mutant. The displayed file-form commands are reproduction equivalents; the actual executions used `-c`, as recorded in the JSON. The arms are evidence artifacts only, not a change to the production suite.

# Hashes and exact restoration

`sha256sum verifiers/verify_surfaces.py` was run before and after every assigned-detector and supplemental-arm execution; every checksum command exited **0**. Detector execution itself never changed the source hash.

Pristine SHA-256, also obtained before and after **all six** restored detector runs:

```
e44bf34b1a52c0e5e4cd320b8f90a20c10c0a997bc225e9b36bf90ccf173be4e
```

| Mutant | SHA-256 before and after its detector run | SHA-256 after restoration |
|---|---|---|
| M1 | `2ffb2b9f0af2cbe81c9d8533c63eea76b10a9363694615e324f6b01f6d7675fa` | pristine hash above |
| M2 | `e95dacbeafa649524979f2a88ef593e4996f4f7c0c4adf5e3eb0643cfc481724` | pristine hash above |
| M3 | `7547a31bdbd2cd2b8212c3a57107213ed33c67b80993d07092f82a4a8701a036` | pristine hash above |
| M4a | `067e17abc5e1be87830dd6db80ea06c790b8f7ea05fc4fa4e4e848e687ee71e2` | pristine hash above |
| M4b | `ccf661d0ba60b4fbdb7e1a85970a913c67bc77dd7fcd0192fe10f412c9c4d2cd` | pristine hash above |
| M5 | `0a618549bad585176382a41ed22e8215051a87be55110bc1af606848cf944570` | pristine hash above |

Final scratch source is exactly restored, with the final detector again reporting 0 failures over 99 assertions. There were no surviving source edits to integrate.

# Not checked

- No live-binary census, default-resolution full verifier, frozen-binary strings counts, substrate-pin gate, or binary execution. In particular, the old/new default paths were tested as parsed values only.
- No C2 checklist/XML trigger check, C3 governance erratum/corpus integrity/fault harness, SOURCE registry rows, ledger counts, append-only history audit, or frontier-admission review.
- No OMP callee mutations; those are outside this assigned opencode/self-test slice.
- No assertion that the five supplemental arms are comprehensive; they are narrow counterexamples that kill these exact mutants. No production tests or contracts were changed.
- No packages were installed or updated.

Evidence artifacts: `W2SurfSelfTestMut.results.json` (complete machine-readable receipts) and `W2SurfSelfTestMut.arm.txt` (supplemental detector source), beside this report. The invariant falsified here is **self-test sensitivity to every assigned mutation**, not the correctness of the landed strict OC-3b/OC-4 logic on pristine bytes.
