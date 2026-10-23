# Round 62 registry-row findings

Seat: `KotobaR62.ExecRegistryRows`. Scope: read-only review of the planned round-62 rows; the only lane write is this report. No source verifier or SKILL.md change was made.

## Decision and exact candidate rows

`corpus/knowledge/anatomy-and-compression.md:110-114` requires a decision table row to contain an action (the entry command supplies it); it does not define a separate verifier-registry schema. The schema and constraints come from `verifiers/check_gate_registry.py:20-43, 68-76, 178-224`: accepted kinds are only `gate`/`probe`; gates require `0=clean`, `1=failed`, a backticked active self-test flag, and pinned values; probes cannot declare `1=failed` and are rejected if their source has an active exact `--self-test` handler. Q35 requires the exact handler on gate rows. Q46 says a withdrawn claim must be marked as such in-cell; it does not call for relabeling a still-operative gate as a probe.

**Intended kind:** both new rows are `gate` if the implementations follow their frozen contracts. The absorption instrument's `--self-test` is not merely a report-only audit: the contract says it returns success only when all five errata are measured and the two controls classify correctly (the measured E2f survivor is an expected finding, not itself an instrument failure). The routed-repairs successor has a verdict-bearing `--rev` command with 0/1/2 outcomes and a computed self-test. If either implementation only prints a finding without gating a verdict, it is a `probe` by the user's rule; the current registry checker cannot accept that probe while an exact `--self-test` handler exists. Do not silently call such a probe conformant.

The proposed pinned-value paths identify the external frozen counter each successor consumes. Both scopes are read-only: the C1 guard substitutions are in-process; C2 reads committed blobs and uses blob-map fixtures. Owner is the lane owner `kotoba`.

The following is the exact **candidate SKILL.md text** to merge after confirming the source files and actual matrix receipt. The r61 row remains a gate and keeps its frozen hash and claim. The r62 clause is marked as the plan's expectation, not a result measured by this seat. No capability row is added.

```markdown
| `verifiers/check_scoped_rules.py` | gate | `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` | 0=clean, 1=failed, 2=could-not-evaluate — r61 frozen v3 sha256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`; frozen claim: `python3 -B verifiers/check_scoped_rules.py --self-test` prints `worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and the same `--rev <rev> --fetch` exits 0 at tip while base `f3246d1493b60ea1c0d947a19c39f9e08e92f326` exits 1; r62 absorption expectation: E2f G7 raw-tokenizer event-claim remains absent, so the event-claim instance survives; G9 compound-purpose remains absent | `--self-test` | in-file | self-test repos under `$TMPDIR` (removed); `--fetch` reads the network | kotoba |
| `verifiers/check_erratum_absorption.py` | gate | `python3 -B verifiers/check_erratum_absorption.py --self-test` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/check_scoped_rules.py` | none (read-only; imports pinned counter, guard mutations are in-process only) | kotoba |
| `verifiers/check_routed_repairs_v2.py` | gate | `python3 -B verifiers/check_routed_repairs_v2.py --rev <rev>` | 0=clean, 1=failed, 2=could-not-evaluate | `--self-test` | `verifiers/check_routed_repairs.py` | none (read-only; reads committed blobs) | kotoba |
```

`check_scoped_rules.py` is not claim-withdrawn: it must remain `gate`; the r62 absorption limitation is an annotation, not a `probe` relabel. The row's pinned-values cell remains `in-file`; its frozen code digest and claim are recorded in the verdict-map cell. The candidate adds no separate capability row.

## Mechanical check and observed conformance failure

The normal checker CLI is revision-only (`--rev`); `Tree` reads `SKILL.md` and verifier blobs from Git (`check_gate_registry.py:108-137, 338-374`). A scratch `SKILL.md` cannot be supplied through that CLI without creating a Git revision, which was prohibited. To check the scratch rows without Git mutation, I invoked the checker's own `judge()` over the scratch `SKILL.md` excerpt and a targeted three-path universe; its `read()` callback read the actual lane files. The exact scratch excerpt is the candidate block above, minus the outer Markdown fence.

Runner used (and its reproducible command):

```python
from pathlib import Path
import importlib.util
import sys

LANE = Path("/home/vgpnk/Projects/shokunin/kotoba-shokunin")
SKILL_COPY = Path("/fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecRegistryRows/SKILL.md")
CHECKER = LANE / "verifiers/check_gate_registry.py"
spec = importlib.util.spec_from_file_location("check_gate_registry", CHECKER)
checker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)
universe = [
    "verifiers/check_scoped_rules.py",
    "verifiers/check_erratum_absorption.py",
    "verifiers/check_routed_repairs_v2.py",
]
def read(path):
    try:
        return (LANE / path).read_bytes()
    except FileNotFoundError:
        return None
def exists(path):
    return (LANE / path).exists()
report, phantom = checker.judge(SKILL_COPY.read_text(encoding="utf-8"), universe, read, exists)
for row in report:
    print("%-44s %s %s" % (row["verifier"], "OK" if row["conformant"] else "no", "; ".join(row["why"])))
for path in phantom:
    print("PHANTOM %s" % path)
conformant = sum(1 for row in report if row["conformant"])
print("gate registry rows conformant %d of %d lane verifiers; phantom %d" % (conformant, len(universe), len(phantom)))
sys.exit(0 if conformant == len(universe) and not phantom else 1)
```

Command, pasted output, UTC date, and exit:

```text
$ date -u '+%Y-%m-%dT%H:%M:%SZ'; python3 -B /fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecRegistryRows/check_rows.py; rc=$?; printf 'exit=%s\n' "$rc"; exit "$rc"
2026-10-23T20:53:55Z
verifiers/check_scoped_rules.py              OK 
verifiers/check_erratum_absorption.py        no self-test flag --self-test lacks an exact handler
verifiers/check_routed_repairs_v2.py         no self-test flag --self-test lacks an exact handler
gate registry rows conformant 1 of 3 lane verifiers; phantom 0
exit=1
```

This is a targeted scratch mechanics check, **not** a full lane-inventory result or evidence that either not-yet-present source conforms. Direct reads of both new source paths returned `Path ... not found`; consequently the checker sees no exact self-test handlers for them and the candidate rows fail. The r61 row passes the targeted check, including its exact `--self-test` handler.

Frozen digest check (read-only):

```text
$ date -u '+%Y-%m-%dT%H:%M:%SZ' && sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
2026-10-23T20:52:16Z
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
exit=0
```

## Risks and blockers

- The source files `verifiers/check_erratum_absorption.py` and `verifiers/check_routed_repairs_v2.py` are not present in the lane at this check. Thus their actual `--self-test` handlers, verdict gating, pinned-value behavior, CLI mappings, and write scopes remain unverified. The table text above is a candidate derived from the frozen contracts, not a source-confirmed conformance pass.
- The frozen plan is internally inconsistent on the absorption survivor count: `plans/round-62.md:35` says the predicate prints `surviving 2`, while `:69-71` and `:91-92` expect `surviving 1`. I therefore did not encode a survivor count in the v3 row annotation. Reconcile against the computed matrix output before finalizing any count-bearing annotation.
- Q46's `claim withdrawn` annotation is not appropriate for the v3 row as currently framed: retain `gate` and the frozen r61 claim, and annotate the measured E2f limitation without treating it as a withdrawal. No capability row was created.
- No builds, tests, linters, or formatters were run. I read the registry checker's self-test implementation (`check_gate_registry.py:245-336`) but did not run its separate `--self-test`; the requested scratch-row check used `judge()` directly.

Installs: no installs.
Blockers: the two new verifier sources are absent, and the plan's absorption survivor count conflicts.
Produced: candidate registry rows, a scratch `judge()` check, and the r61 v3 registry honesty review.
