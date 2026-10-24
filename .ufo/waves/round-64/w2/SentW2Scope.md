# Round 64 W2 — verifier security/scope review

Measured comparison: `078eec4` → `c019919c97ab5fe98e87a7754b4449ea4e699c99`. Read-only review; no verifier or tests executed, no repo changes except this report, and no tools installed.

## Per-item verdicts

### R64 counter — arbitrary revision code execution / root escape: HIGH

**Exploit path.** Invoke `check_r64_routed_repairs.py --root <any-git-checkout> --rev <commit-with-crafted-R63-counter>`. `--root` is resolved but not checked against `LANE`; `rev-parse --show-toplevel` only confirms the supplied path is a Git checkout. The counter then retrieves `verifiers/check_r63_routed_repairs.py` from that revision, writes it into a temporary directory, and runs it as Python with `--self-test`.

**Evidence.** `check_r64_routed_repairs.py:948-957` accepts arbitrary `--root`, calls `Path(args.root).resolve()`, then only checks `git rev-parse --show-toplevel`. `:321-337` gets the candidate blob using `show_bytes(root, rev, R63_COUNTER)`, writes it at `temp_root/verifiers/check_r63_routed_repairs.py`, and runs `[sys.executable, "-B", str(script), "--self-test"]`. That subprocess has no `env=` restriction or OS sandbox. The target `--rev` is only syntax-checked as 40 hex at `:954-955`; it is not trusted/pinned.

**Impact.** The executable source can perform arbitrary local actions as the caller, including reading environment secrets, writing outside the temporary directory, or accessing the network. The 90-second timeout bounds the direct Python process, not its descendants. `[INFERENCE]` A malicious candidate revision in the lane (or a repo supplied via `--root`) can use this path while the counter evaluates it. The code does not itself contain a direct network client, but it executes the candidate's code without a network restriction.

**Smallest remediation.** Do not execute a blob selected by untrusted `--rev`; if runtime execution is essential, run it in an OS sandbox with network disabled, sanitized environment, read-only host filesystem, bounded resources, and process-group cleanup. Separately constrain `--root` to an explicitly permitted checkout (while preserving a deliberate test-only path for constructed worlds).

### R64 subprocess argv/time bounds: PARTIAL PASS; self-test has unbounded Git calls

**Evidence.** Production Git calls go through `git()` at `:59-61` with a 20-second default; `show_bytes()` at `:69-73` has a 20-second timeout. Materialized Python has a 90-second timeout at `:335-337`; mutant/candidate processes have 120 seconds at `:649-656` and argparse probe 30 seconds at `:677-683`. Commands are argument arrays (no shell); the normal `rev` is full-hex validated (`:954-955`) and Git paths are fixed constants, so shell/option injection is not evident.

The self-test Git operations are not bounded: `_commit()` runs `git add`, `git commit`, and `git rev-parse` without `timeout` at `:484-490`; `_new_world()` runs `git init` and `update-ref` without `timeout` at `:543-557`; additional `update-ref` calls at `:845-852` are also unbounded. `FINGERPRINT_SOURCE` contains another `git show` subprocess without a timeout at `:431-435` (invoked under the outer candidate timeout).

**Exploit path / impact.** `[INFERENCE]` In `--self-test`, a hanging Git operation (including a configured user/global Git hook run by `git commit`) can hang the verifier indefinitely; a hook can also execute with the caller's privileges. A child spawned by a timed-out candidate can outlive the direct process because no process-group cleanup is used.

**Smallest remediation.** Add explicit timeouts to every self-test Git subprocess; disable hooks via a temporary `core.hooksPath` and avoid inheriting user Git configuration where feasible. Run timed candidate processes in a new process group and terminate the group on timeout.

### R64 direct writes and embedded secrets: PASS with the execution caveat above

**Evidence.** `_materialized_tally()` writes only inside its `TemporaryDirectory` (`:329-335`). `self_test()` creates a temporary directory and its constructed Git world below it (`:697-700`); `_write()` writes under the supplied fixture root (`:468-471`), and candidate files use paths below that temp root (`:644-646`). I found no embedded credential assignment in either verifier (`grep` for common API-key/token/password/secret/private-key assignment forms returned no matches).

**Impact.** No direct production write outside temp directories or hard-coded secret was found. This does not mitigate arbitrary writes or secret reads by the executed revision blob (HIGH finding above), nor possible Git-hook side effects during self-test.

**Smallest remediation.** Address the untrusted-code and hook execution paths above; no separate literal-secret cleanup indicated.

### V32 diff/network: changed hunk PASS; whole verifier uses network

**Evidence.** The complete V32 diff at `c019919c` adds only four `check(...)` self-test assertions (lines `2129-2162`); those added lines make no subprocess/network calls and write nothing. However, the existing V32 verifier has a network fetch path: `curl_argv()` builds `curl -sSL --max-time 30 ... <url>` at `:1643-1650`, and `run_curl()` invokes it at `:1653-1660`. This was not added by the round's V32 hunk. `run_curl()` has no Python-level subprocess timeout, although curl receives its own `--max-time 30` argument.

**Verdict.** PASS for network access introduced by the changed hunk; FAIL if “network access must be none” applies to the complete V32 verifier at runtime. The existing `--fetch`/curl path is outside this diff, so this is not a round-64-introduced regression.

**Smallest remediation.** If the requirement is strict for the whole verifier, remove/disable the live-fetch path for this verification route and use the frozen page snapshots; otherwise keep this finding scoped as pre-existing behavior. Add a subprocess timeout to `run_curl()` if retaining it.

### Whole-round write-scope discipline: PASS

Command and result (complete output; all paths are repository-relative):

```text
$ git diff --name-only 078eec4 c019919c
.ufo/waves/round-63/w2/ExecW2E2Patch.md
.ufo/waves/round-63/w2/MutW2SplitClauses.md
.ufo/waves/round-64/census-before.txt
.ufo/waves/round-64/controls/C1-before.txt
.ufo/waves/round-64/controls/C2-before.txt
.ufo/waves/round-64/snapshots/S120.page
.ufo/waves/round-64/w1-dispatch.err
.ufo/waves/round-64/w1-dispatch.json
.ufo/waves/round-64/w1-spec.json
.ufo/waves/round-64/w1/ConnSibling.md
.ufo/waves/round-64/w1/CriticC1Bound.md
.ufo/waves/round-64/w1/CriticC2Bound.md
.ufo/waves/round-64/w1/ExecCalibVerify.md
.ufo/waves/round-64/w1/ExecCensusAfter.md
.ufo/waves/round-64/w1/ExecGateRow.md
.ufo/waves/round-64/w1/ExecNoHarmBase.md
.ufo/waves/round-64/w1/ExecR64Counter.md
.ufo/waves/round-64/w1/ExecReceiptTemplates.md
.ufo/waves/round-64/w1/ExecSeatDriftFix.md
.ufo/waves/round-64/w1/ExecSpanArms.md
.ufo/waves/round-64/w1/ExecSpanBefore.md
.ufo/waves/round-64/w1/MutR64Counter.md
.ufo/waves/round-64/w1/MutSpanArms.md
.ufo/waves/round-64/w1/RevC1Predicate.md
.ufo/waves/round-64/w1/RevC2Checks.md
.ufo/waves/round-64/w1/RevSourcesGate.md
.ufo/waves/round-64/w1/RevSpotcheckCrosswalk.md
.ufo/waves/round-64/w1/ScoutQualityDebt.md
.ufo/waves/round-64/w1/ScoutReceiptSweep.md
.ufo/waves/round-64/w1/ScoutS049.md
.ufo/waves/round-64/w1/ScoutS120.md
.ufo/waves/round-64/w1/ScoutS120Alt.md
.ufo/waves/round-64/w1/ScoutSiblingOverlap.md
.ufo/waves/round-64/w1/ScribeEntry.md
.ufo/waves/round-64/w1/ScribeLOGCorr.md
.ufo/waves/round-64/w1/ScribeLesson.md
.ufo/waves/round-64/w1/ScribeQ60.md
.ufo/waves/round-64/w1/ScribeReportSkeleton.md
.ufo/waves/round-64/w1/ScribeSCORECARD.md
.ufo/waves/round-64/w1/ScribeSHONEN.md
.ufo/waves/round-64/w1/ScribeSOURCESRow.md
.ufo/waves/round-64/w1/swarm-registry.json
LOG.md
SKILL.md
corpus/QUALITY.md
corpus/README.md
corpus/SOURCES.md
corpus/knowledge/compound-clause-citation-round63.md
corpus/knowledge/g7-span-pinning-round64.md
corpus/lessons/round-64.md
plans/round-64.md
verifiers/check_r64_routed_repairs.py
verifiers/check_scoped_rules_v32.py
EXIT:0
```

The observed diff has 53 paths, all relative to the lane checkout; no fleet or sibling-lane path appears.

V32 changed-hunk command evidence:

```text
$ git diff --unified=0 078eec4 c019919c -- verifiers/check_scoped_rules_v32.py
@@ -2128,0 +2129,34 @@ def self_test() -> int:
[34 added lines: four self-test check(...) assertions]
EXIT:0
```

No tests/builds/linters were run; this was a source/scope review only.
