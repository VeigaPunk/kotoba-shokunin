Result: DONE — The frozen C2 self-test killed 3 of 14 tested mutants; 11 survived, and every restored-byte run passed.

# Scope and frozen bytes

- Redesign input only. C2 remains withdrawn under `plans/round-56.md:108-123`; this is not a claim verdict or permission to change its frozen contract.
- Seat: `KotobaR56.C2RedesignMutants`. Axis under examination: operability (self-test discrimination); evidence axes: behavioral isolation and exact-byte restoration. No subagents or other agent runtime were invoked.
- Sandbox: `/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants`.
- Checkout: `e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8` (observed by `git rev-parse HEAD`, exit 0). No manually authored sandbox commits, pushes, lane Git writes, delegate implementation or map-disposition changes.
- Only this report was written in the lane. All counter mutations, generated fixtures, traces and receipts stayed inside the seat sandbox. No frozen counter was fixed.
- Original/restored counter SHA-256, named **P** below: `8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe`. Original length: 73199 bytes.

Clone command (exit 0):
```sh
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE
 timeout 120s git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants
 timeout 120s git -C /fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants checkout -q e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
```

Identity/time command output (exit 0):
```text
Fri 23 Oct 2026 02:46:48 AM UTC
e02f5f5d2f37427e8a77b1c3efb45f84b78c67c8
8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  verifiers/check_agentdef_boxes.py
```

# Detector and method

The command **D** was identical for the recorded pristine run, each one-at-a-time mutant and each immediately restored run, from the sandbox root:
```sh
TMPDIR=/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants/tmp \
GIT_TRACE_REFS=/fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants/mutation-receipts/<run-label>.git-refs.log \
  timeout --kill-after=5s 300s python3 -B verifiers/check_agentdef_boxes.py --self-test
```

The launcher removed inherited `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE`, captured stdout/stderr/exit code, and imposed a 310-second subprocess deadline outside the 300-second process-group timeout. `GIT_TRACE_REFS` only observed the self-test fixture commits; it did not modify the counter. Every run completed naturally (no timeout or signal exit). Each mutation was restored using the saved original UTF-8 bytes in a `finally` block before D was run again. Hashes were taken immediately before and after each D run.

Pristine D: exit **0**, stdout exactly:
```text
self-test: 0 failure(s) over 109 assertions
```
UTC start `2026-10-23T02:48:36.354461+00:00`; 13.770 s; before/after SHA-256 both P; stderr empty.

An earlier uninstrumented setup run (`timeout 300s env TMPDIR=<sandbox>/tmp python3 -B verifiers/check_agentdef_boxes.py --self-test`) also exited 0 with the same one-line output (16.57 s). Its automatically deleted temporary fixture commit IDs were not retained. It is not the baseline used for the mutation verdicts. Every fixture commit ID captured for the 29 recorded D runs is listed below; no commit IDs are fabricated for the preliminary run.

Classification: **killed** = pristine and restored D exit 0, mutant D exits 1 with failed assertions; **survived** = those controls exit 0 and mutant D also exits 0. A failed pristine/restored control or timeout would be inconclusive. None occurred. Each mutant was run once; the counter self-test generates random nested evaluation seeds and does not expose all successful nested seeds. Survival is the observed draw, not a universal or probabilistic guarantee.

# Findings

| Mutant | Frozen source lines | Defect | Mutant D exit; observed stdout summary | Verdict |
|---|---|---|---|---|
| `01-text-sha` | `939` | Bypass text_sha256 mismatch | 1; `self-test: 2 failure(s) over 109 assertions` | **killed** |
| `02-stdlib-scan` | `854` | Empty stdlib module-name scan | 1; `self-test: 2 failure(s) over 109 assertions` | **killed** |
| `03-isolation` | `775, 785` | Remove both -P and PYTHONSAFEPATH isolation | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `04-exit-code` | `809` | Ignore process exit equality | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `05-status` | `809` | Ignore JSON status equality | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `06-any-case` | `1010` | Count if any case is right | 1; `self-test: 10 failure(s) over 109 assertions` | **killed** |
| `07-one-wrong-allowed` | `1010` | Allow exactly one wrong case | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `08-hardneg-01` | `447-448, 469-471` | Replace named-sibling PASS contexts with unnamed files | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `09-hardneg-02` | `502, 521` | Directly enroll roster-only reachable children | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `10-hardneg-05-version` | `554` | Replace dotted versions with stable | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `11-hardneg-05-body-date` | `555` | Remove body-only date | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `12-hardneg-06` | `654, 666` | Remove benign task wording | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `13-hardneg-07` | `718` | Make repeated short paragraphs distinct | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |
| `14-threshold` | `244` | Lower N threshold from 3 to 2 | 0; `self-test: 0 failure(s) over 109 assertions` | **survived** |

Observed coverage findings:

- **Exit and status checks survive independently.** `run_case` combines both at `verifiers/check_agentdef_boxes.py:808-809`, but the self-test fixtures at `:1530-1543` do not independently perturb the good reference output along these two axes. The exit-remap fixture at `:1356-1366` is constant FAIL with exit 2, so ordinary PASS cases already reject it by status alone. The correct reference keeps both status and exit correct. [INFERENCE] A future self-test needs correct-content/wrong-exit and correct-exit/wrong-status controls to isolate these requirements.
- **Safe-path isolation survives complete removal.** Both redundant mechanisms were disabled together; this is not merely removing one while the other remains active. The extraction stdlib scan and the counter's own import-path scrub were deliberately left intact. The counter-shadow scenario at `:1574-1597` exercises the counter's startup path, not the delegate's safe-path runtime. [INFERENCE] A direct delegate import-path-sensitive assertion is missing from these fixtures.
- **All-cases has a boundary hole.** Changing all-cases to any-correct-case was killed, but allowing one mismatch survived. The former result therefore does not prove the exact universal rule. [INFERENCE] A future independent control should get exactly one case wrong, not broadly fail an input class.
- **Every generated box's deliberate hard negative can disappear while all 109 assertions remain green.** The probes kept the PASS/FAIL labels, counts, twin file names and correct-reference satisfiability. Both independently named agentdef.05 hard negatives were tested separately. The structural checks at `:1469-1496` and positive reference at `:1516-1528` do not assert that these benign-but-easy-to-overflag contexts still exist. No faulty delegate was authored for this assignment.
- **The N>=3 boundary survives lowering to N>=2.** `MIN_COUNT` is read at `:948`, `:965`, `:1023`; the self-test checks 5 counted boxes, reworded 4, and shortcut 0, rather than a 2/3 boundary. [INFERENCE] A later self-test should demonstrate rejection at 2 and acceptance at 3.

These are self-test coverage findings only. They neither repair the counter nor restore C2 as a round-56 claim. No client/source absence claim or external-source fetch was made. Cross-domain evidence: mutation-test method belongs to tameshi; this seat reports the detector gaps without changing that method or claiming ownership.

# Per-mutant evidence

All line numbers refer to pristine `verifiers/check_agentdef_boxes.py` at the frozen checkout. Patches are evidence only; they were not delivered for integration. Complete paired JSON/stdout/stderr/trace artifacts are under `<sandbox>/mutation-receipts/`, with the labels below. The report embeds the actual detector stdout so the findings do not depend on those scratch artifacts surviving.

## 01-text-sha — killed

Disable the map text_sha256 mismatch guard at pristine line 939.

Expected detector: The reworded-box scenario must fail its 4-of-9 and agentdef.01-not-counted assertions.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -936,7 +936,7 @@
             lines.append("  %s: not counted (no pinned base sha for this "
                          "box id)" % box_id)
             continue
-        if box.get("text_sha256") != pinned:
+        if False:
             lines.append("  %s: not counted (box text was reworded at this "
                          "revision)" % box_id)
             continue
```

Command D, mutant: exit **1**, start `2026-10-23T02:49:21.122007+00:00`, elapsed 15.119 s.
Mutant SHA-256 before **and** after D: `66f894e6cff7f788f8e95e78e9e2cdf73d8c7a1a1a12c0f8a8c485a8a63eaec6`.

Actual stdout:
```text
self-test: 2 failure(s) over 109 assertions
FAILED reworded: agentdef.01 not counted: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED reworded: 4 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:49:36.258308+00:00`, elapsed 15.245 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **killed**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 02-stdlib-scan — killed

Replace sys.stdlib_module_names with an empty set of names at line 854.

Expected detector: The stdlib-shadow fixture must be rejected; both stdlib shadow assertions should detect counting it.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -851,7 +851,7 @@
     verifiers = tree / "verifiers"
     if not verifiers.is_dir():
         return found
-    stdlib = getattr(sys, "stdlib_module_names", ())
+    stdlib = ()
     for path in sorted(verifiers.rglob("*.py")):
         stem = path.stem
         if stem in stdlib:
```

Command D, mutant: exit **1**, start `2026-10-23T02:50:08.057627+00:00`, elapsed 16.518 s.
Mutant SHA-256 before **and** after D: `5574b61bf6d8b0d8643d545c7c3d61cd0c51c9c9d534a6b2f3c806d77117105a`.

Actual stdout:
```text
self-test: 2 failure(s) over 109 assertions
FAILED stdlib shadow: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED stdlib shadow: the line says why: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:50:24.582807+00:00`, elapsed 13.795 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **killed**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 03-isolation — survived

Remove both redundant safe-path controls: omit -P at line 785 and explicitly pop PYTHONSAFEPATH at line 775.

Expected detector: An isolation-sensitive fixture should fail when a delegate can import from its own directory; the existing stdlib scan and ordinary reference script may mask the missing runtime isolation.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -772,7 +772,7 @@
     env = dict(os.environ)
     for name in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP"):
         env.pop(name, None)
-    env["PYTHONSAFEPATH"] = "1"
+    env.pop("PYTHONSAFEPATH", None)
     env["GIT_OPTIONAL_LOCKS"] = "0"
     return env
 
@@ -782,7 +782,7 @@
     """Run the delegate over one case.  Returns (as_expected, observed)."""
     try:
         proc = subprocess.run(
-            [sys.executable, "-B", "-P", str(script), "--check", box,
+            [sys.executable, "-B", str(script), "--check", box,
              "--target", str(target), "--json"],
             capture_output=True, text=True, timeout=TIMEOUT, env=delegate_env(),
             cwd=str(cwd))
```

Command D, mutant: exit **0**, start `2026-10-23T02:50:54.597563+00:00`, elapsed 16.006 s.
Mutant SHA-256 before **and** after D: `9b96838e74d60abd32dba9d355642d548565a59139452900b661b18b004b950b`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:51:10.616466+00:00`, elapsed 14.623 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 04-exit-code — survived

Drop the subprocess returncode equality from run_case at line 809; retain expected JSON-status validation.

Expected detector: A correctly discriminating delegate with remapped process exit codes should be rejected; the existing exit-remap fixture is constant FAIL and can be rejected solely by status mismatches.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -806,7 +806,7 @@
     if not statuses:
         return False, "exit %d, no checks entry for %s" % (proc.returncode, box)
     want_rc = 0 if expect == "PASS" else 1
-    ok = proc.returncode == want_rc and all(s == expect for s in statuses)
+    ok = all(s == expect for s in statuses)
     return ok, "exit %d, status %s" % (proc.returncode,
                                        "/".join(map(str, statuses)))
 
```

Command D, mutant: exit **0**, start `2026-10-23T02:51:51.912887+00:00`, elapsed 13.407 s.
Mutant SHA-256 before **and** after D: `534d821c472a4a20522348194d073be616bb0291e2c8cfb8821266f4af9b83a3`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:52:05.327975+00:00`, elapsed 13.287 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 05-status — survived

Drop the expected status equality from run_case at line 809; retain checks-entry presence and exact process exit checking.

Expected detector: A correct-exit but wrong-status delegate should be rejected; existing constant delegates synchronize exit with status and do not isolate this requirement.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -806,7 +806,7 @@
     if not statuses:
         return False, "exit %d, no checks entry for %s" % (proc.returncode, box)
     want_rc = 0 if expect == "PASS" else 1
-    ok = proc.returncode == want_rc and all(s == expect for s in statuses)
+    ok = proc.returncode == want_rc
     return ok, "exit %d, status %s" % (proc.returncode,
                                        "/".join(map(str, statuses)))
 
```

Command D, mutant: exit **0**, start `2026-10-23T02:52:34.314495+00:00`, elapsed 13.175 s.
Mutant SHA-256 before **and** after D: `c095f89e23689b97756df4262961f8b54ec15a2f20105c0f04478d9f066f3ed9`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:52:47.494913+00:00`, elapsed 13.084 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 06-any-case — killed

Change the per-box all-cases policy at line 1010 to reject only when every case is wrong; any one correct case counts the box.

Expected detector: Constant PASS/FAIL, no-reader, id-keyed, exit-remap and name-keyed shortcuts must remain zero boxes; partial accuracy should now break those assertions.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -1007,7 +1007,7 @@
                                    % (case.label, case.expect, observed))
             finally:
                 shutil.rmtree(workdir, ignore_errors=True)
-            if bad:
+            if len(bad) == total_cases:
                 lines.append("  %s: not counted (%d of %d cases wrong: %s)"
                              % (box_id, len(bad), total_cases,
                                 "; ".join(bad[:4])))
```

Command D, mutant: exit **1**, start `2026-10-23T02:53:11.936906+00:00`, elapsed 14.433 s.
Mutant SHA-256 before **and** after D: `362cb6d96d02ed4fa95e9c4e003e9c717a8e7a04af7ac69f20e9deefc6837aab`.

Actual stdout:
```text
self-test: 10 failure(s) over 109 assertions
FAILED constant-pass: exit 1: exit 0 
FAILED constant-pass: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED constant-fail: exit 1: exit 0 
FAILED constant-fail: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED no-reader: exit 1: exit 0 
FAILED no-reader: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED id-keyed: exit 1: exit 0 
FAILED id-keyed: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
FAILED name-keyed: exit 1: exit 0 
FAILED name-keyed: 0 of 9: agent-definition boxes executed and discriminating 5 of 9
  agentdef.03: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.04: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.08: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.09: not counted (no case generator for this box: this counter generates cases for agentdef.01, agentdef.02, agentdef.05, agentdef.06, agentdef.07)
  agentdef.01: counted (8 of 8 cases)
  agentdef.02: counted (10 of 10 cases)
  agentdef.05: counted (10 of 10
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:53:26.375901+00:00`, elapsed 15.544 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **killed**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 07-one-wrong-allowed — survived

Change line 1010 from rejecting any wrong case to rejecting only two or more wrong cases.

Expected detector: A delegate that gets exactly one generated case wrong must disqualify its box; the existing broad shortcuts get multiple cases wrong and may not detect this boundary.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -1007,7 +1007,7 @@
                                    % (case.label, case.expect, observed))
             finally:
                 shutil.rmtree(workdir, ignore_errors=True)
-            if bad:
+            if len(bad) > 1:
                 lines.append("  %s: not counted (%d of %d cases wrong: %s)"
                              % (box_id, len(bad), total_cases,
                                 "; ".join(bad[:4])))
```

Command D, mutant: exit **0**, start `2026-10-23T02:53:54.747265+00:00`, elapsed 13.978 s.
Mutant SHA-256 before **and** after D: `fe40274c82aeefd6f2b001cd056c8d37314f0712dc60680e9ac714e012ec1872`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:54:08.730824+00:00`, elapsed 13.944 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 08-hardneg-01 — survived

In the agentdef.01 generator, change the five declared names in multi-file PASS groups g2/g4 to None at lines 447-448 and 469-471. The hard-negative situation of matching names with all named siblings disappears, but labels, twin names, PASS/FAIL counts and FAIL members remain.

Expected detector: A semantic hard-negative assertion should notice that the named-sibling PASS scenario disappeared; generic size/name/cardinality checks and the correct reference may still pass.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -444,8 +444,8 @@
     t = stems.next()
     g = stems.next()
     out.append(Case("agentdef.01", "f2-sibling-roster-consistent", "g2",
-                    {"agents/%s.md" % t: agent_doc(t, t, desc, body),
-                     "agents/%s.md" % g: agent_doc(g, g, desc, body)}, "PASS"))
+                    {"agents/%s.md" % t: agent_doc(t, None, desc, body),
+                     "agents/%s.md" % g: agent_doc(g, None, desc, body)}, "PASS"))
     out.append(Case("agentdef.01", "f2-absent-name-with-declaring-sibling", "g2",
                     {"agents/%s.md" % t: agent_doc(t, None, desc, body),
                      "agents/%s.md" % g: agent_doc(g, g, desc, body)}, "FAIL"))
@@ -466,9 +466,9 @@
     g1 = stems.next()
     g2 = stems.next()
     out.append(Case("agentdef.01", "f4-three-consistent-names", "g4",
-                    {"agents/%s.md" % t: agent_doc(t, t, desc, body),
-                     "agents/%s.md" % g1: agent_doc(g1, g1, desc, body),
-                     "agents/%s.md" % g2: agent_doc(g2, g2, desc, body)}, "PASS"))
+                    {"agents/%s.md" % t: agent_doc(t, None, desc, body),
+                     "agents/%s.md" % g1: agent_doc(g1, None, desc, body),
+                     "agents/%s.md" % g2: agent_doc(g2, None, desc, body)}, "PASS"))
     out.append(Case("agentdef.01", "f4-one-mismatched-name", "g4",
                     {"agents/%s.md" % t: agent_doc(t, t, desc, body),
                      "agents/%s.md" % g1: agent_doc(g1, g1, desc, body),
```

Command D, mutant: exit **0**, start `2026-10-23T02:54:43.456132+00:00`, elapsed 12.930 s.
Mutant SHA-256 before **and** after D: `66f7cfe5dd95d8883f15c71d33f67dae2cb24978c7a2386f76283d5a3edd2f32`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:54:56.391927+00:00`, elapsed 13.692 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 09-hardneg-02 — survived

Directly enroll both parent and child in PASS groups g2/g3 at lines 502/521 instead of enrolling only the parent. No PASS case now requires reachability solely through subagents.

Expected detector: A semantic hard-negative assertion should require a roster-only reachable child; the reference still succeeds because direct enrollment is also valid.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -499,7 +499,7 @@
                     {"agents/%s.md" % p: agent_doc(p, p, desc, body,
                                                    subagents=[c]),
                      "agents/%s.md" % c: agent_doc(c, c, desc, body),
-                     "opencode.json": roster_json([p])}, "PASS"))
+                     "opencode.json": roster_json([p, c])}, "PASS"))
     out.append(Case("agentdef.02", "f2-parent-names-no-subagent", "g2",
                     {"agents/%s.md" % p: agent_doc(p, p, desc, body),
                      "agents/%s.md" % c: agent_doc(c, c, desc, body),
@@ -518,7 +518,7 @@
                     {"agents/%s.md" % p: agent_doc(p, p, desc, body,
                                                    subagents=[c]),
                      "agents/%s.md" % c: agent_doc(c, c, desc, body),
-                     "opencode.json": roster_json([p])}, "PASS"))
+                     "opencode.json": roster_json([p, c])}, "PASS"))
 
     # F4: two agents, both enrolled (PASS) / one of them not (FAIL).
     a = stems.next()
```

Command D, mutant: exit **0**, start `2026-10-23T02:55:26.615916+00:00`, elapsed 13.829 s.
Mutant SHA-256 before **and** after D: `35caa029eed785f020b15375474c41f8aabdcbea377ace53b4110dee314662d2`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:55:40.452619+00:00`, elapsed 14.488 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 10-hardneg-05-version — survived

Replace generated dotted version with the word stable at line 554, removing numeric-version hard negatives in groups g2/g5 without changing the dated-body hard negative.

Expected detector: A semantic hard-negative assertion should require a non-date dotted version in frontmatter; the correct reference should still accept the easier neutral word.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -551,7 +551,7 @@
     body = standard_body(rng)
     date_a = pick_date(rng)
     date_b = pick_date(rng)
-    version = pick_version(rng)
+    version = "stable"
     dated_body = body + "\n\nThe lane shipped a fix on %s." % date_a
 
     # F1: a date in the description (FAIL) / no date (PASS).
```

Command D, mutant: exit **0**, start `2026-10-23T02:56:06.024626+00:00`, elapsed 13.137 s.
Mutant SHA-256 before **and** after D: `15fb85596e9fd643a737bf44793d78b1ec3df2cdb99f47edf829604df5e78331`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:56:19.168764+00:00`, elapsed 13.398 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 11-hardneg-05-body-date — survived

Set dated_body to the ordinary undated body at line 555, removing the body-only date hard negative while leaving dotted-version hard negatives intact.

Expected detector: A semantic hard-negative assertion should require a body date with date-free frontmatter; the correct reference and structural checks may accept its removal.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -552,7 +552,7 @@
     date_a = pick_date(rng)
     date_b = pick_date(rng)
     version = pick_version(rng)
-    dated_body = body + "\n\nThe lane shipped a fix on %s." % date_a
+    dated_body = body
 
     # F1: a date in the description (FAIL) / no date (PASS).
     s = stems.next()
```

Command D, mutant: exit **0**, start `2026-10-23T02:56:38.759390+00:00`, elapsed 13.603 s.
Mutant SHA-256 before **and** after D: `a5b22f93d7fa44a4d8051a5046f33adce62d8a31305c424e0e5c9785185f5803`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:56:54.300265+00:00`, elapsed 13.249 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 12-hardneg-06 — survived

Replace task with duty in the g3 standing-body PASS at line 654 and with change in the g4 stable sentence at line 666. Both deliberate benign-task PASS contexts disappear.

Expected detector: A semantic hard-negative assertion should require the bare word task without a forbidden current-task phrase; generic reference correctness is not enough.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -651,7 +651,7 @@
     out.append(Case("agentdef.06", "f3-standing-task", "g3",
                     {"agents/%s.md" % s: agent_doc(
                         s, s, desc,
-                        body + "\n\nThis is a standing task: sweep the %s queue each cycle."
+                        body + "\n\nThis is a standing duty: sweep the %s queue each cycle."
                         % surface)}, "PASS"))
     out.append(Case("agentdef.06", "f3-one-shot-instruction", "g3",
                     {"agents/%s.md" % s: agent_doc(
@@ -663,7 +663,7 @@
     # sentence plus a current-task line (FAIL).  The hard negative of this
     # box: only the phrase `your current task` is a defect, not `task`.
     s = stems.next()
-    stable = body + "\n- Keep one task per commit."
+    stable = body + "\n- Keep one change per commit."
     out.append(Case("agentdef.06", "f4-bare-word-task", "g4",
                     {"agents/%s.md" % s: agent_doc(s, s, desc, stable)}, "PASS"))
     out.append(Case("agentdef.06", "f4-task-word-plus-current-task", "g4",
```

Command D, mutant: exit **0**, start `2026-10-23T02:57:17.857016+00:00`, elapsed 13.717 s.
Mutant SHA-256 before **and** after D: `c5e36e4b8bde4cc220eb96c2b0401b43651f27e5d5d79f58e20ec91101a92761`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:57:31.578855+00:00`, elapsed 52.013 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 13-hardneg-07 — survived

Change the second short - yes paragraph to - no at line 718, removing repeated short content from the g3 PASS while retaining the long-duplicate FAIL twin.

Expected detector: A semantic hard-negative assertion should require an actual repeated paragraph shorter than 40 characters; structural checks and the correct reference can accept the easier distinct lines.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -715,7 +715,7 @@
     # body plus a repeated long paragraph is (FAIL).
     s = stems.next()
     short_repeat = ("You are the keeper for the lineage surface.\n\n"
-                    "## Loop\n\n- yes\n\n## Ledger\n\n%s\n\n- yes\n\n"
+                    "## Loop\n\n- yes\n\n## Ledger\n\n%s\n\n- no\n\n"
                     "## Close\n\n%s" % (LEDGER_PARAGRAPH, CLOSE_PARAGRAPH))
     out.append(Case("agentdef.07", "f3-repeated-short-line", "g3",
                     {"agents/%s.md" % s: agent_doc(s, s, desc, short_repeat)},
```

Command D, mutant: exit **0**, start `2026-10-23T02:58:35.876130+00:00`, elapsed 69.169 s.
Mutant SHA-256 before **and** after D: `8abc82a3665c4ceb50fc1ce2d4437b70ae5979490ab05e03c74acf6a0eac1160`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T02:59:45.067626+00:00`, elapsed 59.416 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

## 14-threshold — survived

Lower MIN_COUNT from 3 to 2 at line 244.

Expected detector: A 2-of-9 fixture must still exit 1; the existing self-test references 5, 4 and 0 counted boxes and may have no threshold boundary fixture.

Mutation patch:
```diff
--- a/verifiers/check_agentdef_boxes.py
+++ b/verifiers/check_agentdef_boxes.py
@@ -241,7 +241,7 @@
 BASE_REV = "b0b7140b5a7cf8a50f13989ee6285fc8ee245c41"
 SECTION = "Agent-definition fidelity checklist"
 TIMEOUT = 20
-MIN_COUNT = 3
+MIN_COUNT = 2
 TOTAL_BUDGET = 240.0
 
 # The boxes this counter generates cases for.  The other four boxes of the
```

Command D, mutant: exit **0**, start `2026-10-23T03:00:55.104295+00:00`, elapsed 63.394 s.
Mutant SHA-256 before **and** after D: `42729158146616b37441b18d13128be72dedf13974fd2bddf62e7856e04255e3`.

Actual stdout:
```text
self-test: 0 failure(s) over 109 assertions
```
Actual stderr: `` (empty).

Restored command D: exit **0**, start `2026-10-23T03:01:58.541663+00:00`, elapsed 45.050 s; SHA-256 before **and** after D = P.
Restored stdout exactly: `self-test: 0 failure(s) over 109 assertions`; stderr empty.
Verdict: **survived**. Exact restoration and passing baseline/restored controls prevent classifying a baseline failure as a killed mutant.

# Restoration and bounds evidence

- 29 recorded D runs: one pristine, fourteen mutant, fourteen restored. Every run's counter hash was unchanged from its own before to after. Every restored hash equals P and every restored detector exited 0 with 109 assertions. Three mutant runs exited 1, all eleven other mutant runs exited 0; all stderr streams were empty.
- Maximum recorded D wall time: 69.169 s; no recorded D reached its cap. All launched subprocesses returned before this report; no long-lived service or asynchronous job was started.
- Final saved-byte equality check: `counter.read_bytes() == pristine_bytes` returned `True`. This establishes byte identity, not inode/mtime history or custody (Q22).
- Final independent hash/time command: `timeout 20s date -u && timeout 20s sha256sum <lane>/verifiers/check_agentdef_boxes.py <sandbox>/verifiers/check_agentdef_boxes.py`, exit 0:
```text
Fri 23 Oct 2026 03:03:15 AM UTC
8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_agentdef_boxes.py
8aeb9bcf611decdba9e1027c435c3f268e5c51112706f43d76f284ae05aeb8fe  /fast/scratch/hyaku/kotoba-r56/KotobaR56.C2RedesignMutants/verifiers/check_agentdef_boxes.py
```
- No tools were installed or upgraded; no paid model/client calls, browser, network fetches, lane tests or unrelated verifiers were run.

# Automatically created sandbox fixture commits

These are the 12 unique nonzero commit IDs observed by Git ref tracing during each recorded D invocation. All temporary fixture repositories were under the sandbox TMPDIR and were removed by the counter's own self-test cleanup. They are recorded IDs, not promises of retained Git objects. No Git commit was made in the lane by this seat. The uninstrumented preliminary run's IDs are unavailable as disclosed above.

## 00-pristine
```text
2eb228c48c3ed9066c4ee5ff52f7f65fcb0ce92e
380b634005edf505742234ab97eb1df1e11e8095
661f64461123113b590b50ffe0b1bd071a2b9573
6922c399f4b6759177b3a65d7fcae42774e4c25b
84952fb4cc5ec021ca297e54b7dc80175af2b775
92664e5f94d7fc90fa22cc350230b1b8d2051412
9b38701dff858f2df24c29d47d89ced24e9bab7d
9bff8e41f3ffc836bda636dc578b8da1bba4e089
bc0a187738eca073320732a9c58d7e839c2a7d18
e01315c611f55275c8782a23a45a4eb1baf5cd74
fa2cbacaeda0191cb46cc41148327e9004603cf4
ff3c56d6f141a29366ec3b3cb9b1af11de3b9c58
```

## 01-text-sha-mutant
```text
22ea9d4f31fa980a27ed82018722e71dc2b29d6d
3d0d0819e0ae93d96258121161335064cdd548c0
48ecb07d84a98f2c85e227f494bd62a9bd85d8cb
52592ee6245f5e735be419215c84e6f3819c6ef6
542c2239f6a1419eb4a90411c6175895d702072c
5ef7783a2d75f2a32b5048171674de638a777d66
6c217d9edf672ca723b135e33953733b751d48e3
962fafbc17b8543539006a61b1b433e62ef64535
d40c1d678e42c94a7c305456c7b0bc1bac877284
edf53e1a74c6953cc413cf14c072cc0a5b3bb9c6
f52284ac943dfe76e6cbb435fe091b1c04d29632
fea8be177eb8b2f12d44ef4dcd07f4beb3a072d3
```

## 01-text-sha-restored
```text
17eb160639c5c7b7e33b18b6f912b8c88cb4020d
325040b74824902f0b569ac07a97dc3854f33ba9
331d81c53ab61670c4a8a35a2e7094fd7ccd5c9b
4f42fd72f052b3df93a5b83882832811d92209d4
5ecbb179a4bd20fcd5756334e72377dff3560c0e
6bd663e64b6d727a823e6fd945190bb9abdad809
b28ec5d37ad349661f5705276cbe58a855592fd7
d1d73429cc52a93d083adef719edc4a1bcb4a9ae
dc409bc4e95505dd96e25c6547be8cedff90b878
e00600ca95a340e6b0015dfeb9aa98f7b7f99520
e8f234f7296fc9c4b532b8c60bef8979fade1d4d
eac871efd793d50a82cd0ce022495611a116692d
```

## 02-stdlib-scan-mutant
```text
04c46daf9725984a5ac4a8654789de3c196a53e2
22bd35d6cfe0473a235bc20a015ac4b4b0582b3c
3f55f1fbc08db20709b4636042850ce7f7268006
4fd8d9071dda98cc7a1ddd2ad6c8ee96d92403aa
88030c505742218e57fc3d6b9d5e97252917eca0
9add0c6ef221903a6bcadbc6b4500d90862bb9e6
aa8c17c5b1583f414b26929858ce1bb664f0f53f
afefa61a67c2ae565d621ed7fe4083037fad1140
bc471a5022d9704f4339e0c55055cbc2e9edc24b
ce5e570b9925dc24fb8a301372ab9e8622b38c25
dc398c2d99d6d92034635ebc62d1192fcaf8d42d
e0722ab15442885e91dd575e40fbab31c5467e00
```

## 02-stdlib-scan-restored
```text
112ad0e7d676070a35addec8ff033b47e1e80c90
2a86df6bbd7bcf634d19b9f1401ef02077c60ae1
41b5365aa32f7385c04186ed65d2d9ff5ed6ad50
7823a62898db9ea61f79b90a4427296668769ff7
85a81da6957be443b8c8c420c487f7afbacd832b
aa52e2c7e3f4bc09280070367fb9d7d6b3a1c2d3
afdb9df7ab3046658aed3c26bee9e34fb62bae40
c495e4f8746b9519668c1a9d62cf571fdabd04b5
e3aab829efd4ff5baa017c9fc3b89e12908ed214
f0bf16e8a7ff2878b456ec00a0b0c3852dc148bb
f931ad3ffbc1def86b44746ab24e4bd9f3d57d18
fe872fdc2bd44aa4296a2f30ce058e67480fbb7e
```

## 03-isolation-mutant
```text
09d8d5dcfe627f5079e65b7d2f0d423af0bc65e6
3f6d85c01dfbcb6c8a9801aa85e4e0b26d62e669
59044be5faa2e6f76efb011a8331640653bcad5a
68fc2e64e4b583a04aefa89332478ace4a52dabf
6f6849b1cf9fbcc0a6313eee57e13924573e0ec8
7760f2f3d441d0c3e4d0ed2703816ac797543827
7fe03774f9c7ac719c8828de8a0dab21f3100678
95ad2857d9b22f4693b1be24c38e643cad7c1e88
e0ea025e93fcb9b582794185aeebd1c803a28956
e1444982b22add01713670655598efc64839ae9e
e55817331475274d69d8fa30bf05209e074d4a89
f9fcdbda6d6918960594444055566f4e95d9d502
```

## 03-isolation-restored
```text
285c651929fde104322efac2d9125cd196fc47db
2bb9674db63db0c2bf8efed463872d7da2b20f17
7aed0247dd3f0b9948143b24eb2d9d10e34ecdc3
9275a7a8054739376aaaed66ede8fb3c626bb166
ab46371e053f6aa256abbb168479ad3e61b07514
ab9f99f17c23769914d4153d66e02261d93dc15e
ac5a2d2fb2414d93f0afd84376c9ea6b39080284
b7e9dda611efc1ed0e17d174960b0352d36a6693
c020bb7e669b6b65a6790d67ae7ea97b1df810ce
d794af41c0486334928056e6fe4d94fea4da6260
f6cbcac671614926f75f5f425bdbc4f76278a885
f981d1661723ecb35970bbbee818679faa7b19ba
```

## 04-exit-code-mutant
```text
0d7f52665fea8d6a48ef7286067c7a250f074067
171ca3c769c6e66864013d0930ed0331e1194599
18a175aeee75a4f89957d11f06667d300c322e15
23dd429c14c2320dd9b8c6451da982a2ada919d5
2722053ad5772735781c09a8962af51bf612d604
6d77ab9589065f54e45ec281f75cdf47a282c8f0
8fe48859f5262d473b0d26fa6eb8a6b6eb72678b
9706f8c23225f2c6ec953232edb16141d9c557e9
a5c7563be13bf32a8634013b182fca5e38bf608a
ad6f3490e953efe4127e3b43d1d46f731c3f1e2a
d306f7d324ffa9847ef993d52e10528546fff2c3
e56b0b80797e16888094c8781d10b072506d7a81
```

## 04-exit-code-restored
```text
0029bc5711e71645d5371bdaaff1e4193e3d9a8a
122c7be5a6a338b5cce0250f479b0f573e682378
3ffb24437bb6a2030bcdd3f2f52852fa31f88d72
4be453d72a1afeea6856a60178aa59a9d34e6c72
5038f991ff6793467a8d6e319808558a63477bc7
5bf75d5976bb52fa51287c8517bfe6cccd7c4fb8
73dc9a01bf50d3cb09bd18f314c5875b6dd2954a
7e767f479f91b35bd60d5e3c1e030e1e3ed55db6
847930bb660c5704058ec9c5e7f0c2542f05484d
a5ce1b7ff925b3e9b67c17b2a63d71192db61f6b
bf73b7537083f879d70615ade91e1bafd13d4144
da1618ded7634fccdbbdb9b56b7d46c3213022f4
```

## 05-status-mutant
```text
04d7c128f0cc33712085851a0c83015b0bdd648c
2136c5db908ecff65a305a995344919031f9cd8c
3b7694b09891313fa8984a22e158e0da93c42701
3c68d60b93248af84e4611dfa818a6c5a355b68e
44aa30604849021bcb2d76d53f08a10cae784f93
4ff7be67aa8bc9d2d9bbbf8957c293c9eed525db
5af0c0d31c1baf7b3f0ee57d519596cb6d7da247
600a4a3e1b36808485da1d823871e49c1e22d217
6eba391a6686b0e0982403f6d6076d5dc2915252
916f426bd545a94a320bd746ed47435802ee0c4a
af814fd2be7d247641dcb89097e2754d7e99f8d4
b18d0d6b1d8ffdcf3ed9bd7b36f258b10b2de098
```

## 05-status-restored
```text
0864d4259c91e0b36eb3d3ab21f478ed6e09fb4e
15d21e12ff6b6f87acd03ce96a0f68bd59e0aa33
1613baa7a3e98147478b773ec602b55269bb8818
3aa2e9607dc5e6780d4ecc2caf52350d2a061808
5f64bc494e31270ddcdd053e2ea627c3ccc401a6
8440b7c33c4a2beb7058eda7ef4443445e85ad9c
c06a29d5f16a5ede3c6d726828be06fa5d1f9d23
d1a1a351335eb91f3213346e3939d9ea6f0f5ef0
df668912ca2af01b1d8891ca4ec6db2ffb44d4db
ee8255908ee8bc0dd512508c5b4977756cdfb011
f2cb6ff9d4b2d79506e7f965e2baee4d90ac2959
fe267d212e316f0c8b8a3bd88ce2605ea329fd87
```

## 06-any-case-mutant
```text
09582098a7aac97e05df3a5fcac62ec3b4aa8ac8
0fd60407aa7430f26cb8c9cd4ce5969a5030bdcb
1eb82971fc5db0c5182f760765a717ac4d3b9cd4
55f23fc8f684b3db83040647d5b30f6c68fc0804
91ee42ec3d6127b900a0fc1afbdb2ae47d31ee84
943bb139b03302009d7f9229ab429fce7c5d21f3
98eaf8a2b4465692e0d022e8f145d853d0f74737
a341bc662aaf6e8539ae707775cc338b36631471
caf0cc7e8f055b2ffb345a0839f8255532060f8a
ccd94dc470b7c29883d74f4f8ec4ea60b6f0865d
d5380f1c031b99e9afefef11a95135056de4da5a
f8e6955242322bcc1e22bc53e27ba6fc203cb7fb
```

## 06-any-case-restored
```text
18c6c7b7fab95a8b216d384a35c4636f1e5f6d45
1b43773b2134ac7659222a80f6bdb191fbc11f4f
302cf00e7f2d8bd563c68fef3b98563fea8babba
32cc6d21039c393fd8a2fb0b7e711a9b47eb2187
3c7c27a98dae1efc55750e6750cbe7111ee04663
422f7a7ed522285c8fb71657b77ef725c3a64a49
43b2b08558daf30f0ba61cdf4db1ba8cd278022b
a160ad0fd4e3acce70fcd530e984de3da00e5aa2
b84502d01dbcb69956e776b5368ecd4d6ca86445
baa61a7013e0d0922aac358fa1afbc5f1ecdc13f
f00b10a926b79e5ed12abbb2071de5c342fec342
fbfc4dcf2ee1bde7fba95b6a69b38ab19d16660b
```

## 07-one-wrong-allowed-mutant
```text
12251a867f8a1a59c9328de4f58967538d64bfd0
19af469142aae351813e79783685679b808f2c3f
27ddd6093069ff4bbd292d67967dfa0c3e92bac7
7691cd5441780ca51e52c45b6964fa2eb4b95968
9debd11d2f671a404bd302f66fa8b3cf3907f724
a6d8fde184a07a0f9a03473eab622635c0e29275
a9cef68a20ecd492fad71886a5b5b9cc930f1db8
bf5746a96ae4803bf8f66302e46d17abfae5b0bc
d1e6858c0f69ae57bc78ba057f380af594b58632
e62ac0471be28bf0cd0f6cfc08ad7be09b8a895d
f2af0e714110703904b831b22fa610a420e5ff91
f9456d8b18fe7cf346345e4f6aa0733e8e421453
```

## 07-one-wrong-allowed-restored
```text
12573002db377f6dc9512756fe1faccf784b0834
199c77529b3b5cf6bb7632c38cfc88674128c085
4578e35e2d2efdaa3875ba366f4f9ca2849d0db3
5235f912f930c10b53ebd2be0891d7cbf8bca177
6d87c891c68804f5c67fba8f163c8e7efa2e5c7d
7a3460f611f8ba2d70cdb587ecd7f278c2636b81
9381f619761934a42db8cceeac0b14b0bdb2ea7d
aa456cd6ba6f5cf62c858d5c0962e8e46a35ca30
aa5e9e6b15c6edf3734e85fa2b909ab7d536f9c8
b47beafb0cdf839948570ed3fad2cb56bb866405
b96c07b105cc97c0462e576eb1e32d6b095a8660
f9d8b2c39874fc7f5a9613f22f7458ecbabbf2db
```

## 08-hardneg-01-mutant
```text
185587aff2e1d5dfa1b1b36e61b6b71e205fa5f4
329f6920ca924339a051f841e29870521dddcc9d
32bf60d02b0d71cc6c85fc11e9b2e33ed560d546
402664d116f9161921dc336274462c96815e0b46
5b8f45d550a3cce05c410c3dbe2ee2eee5d22755
7245be07a71e083ad2136e0b25e471b342e7d0a1
9fe42e485a923afddd0f6eb9ef3e863ba899e78c
abfa65656fb8e115f59f4a168a16bebd63e0d6aa
af1c9842950f2f891ff57cbfa3214902fab95c8f
c0dde615619527aa599060dd11a16bc9f2a58fd3
c89aa0a180fd2edfc870f868aea268179b2823a6
e2e1fb83a6f3f80c88bbcd88f90a8c1c16993bed
```

## 08-hardneg-01-restored
```text
3545a4dee29c38d20a025953e394c2f3f5f4462f
3be7b06d0b1367a7ade7b0a448b06766d0a01842
4ee82ee251d1e0c4ebac30f00f17e6b9434354a0
5060a31340afd1fec355314a3912971294d16de6
5e325f61d2e2f74f989ac2c97cda63123806fe7d
87d43ad09557239ec29a01f930c5463c18e48c50
88ffdf522eb15159b97b26f0945f5a8569ce1c9f
8d816562338582ad38e7a404614f0cc876970df8
9e097292b51d13b7a0a430a4f30bd82eef88f0ee
ec68b5cede8d04287814b2ad0e350ba4fe2676c8
ed74748e6ed18a180400f98a4197bee6ad448fe8
ff2edd022acd40514ce4ce8ef389a37f87cb400c
```

## 09-hardneg-02-mutant
```text
020a49d71accc887f354e59788f9bf5f1117f7b9
0f6594248025b42047ea095e7718a0cc99766dba
116c4de26c26722b655743f792b22cf53415530d
36cdc56c4fea3bb29fc03039484ae6fb5a6ea9eb
52749f6ce8b17b4e6d425e2986746fd9ec7e51a6
89b8cfeeb64d21835c59d9e7f72564f843859727
901b15de68bc5ce3a811d56c10339604f45b719d
94c5efdeacae723db7078939ca4354b171c22381
94d3fb9f11d2f9ba68db488522305c196eba17f1
a98de44adaafaea6f1caa52a4f8d687030058c16
ea8cb90e93d8b1cc45456d8bd461df55119f069b
ead84fda89154683467ae07db8ed78eeddf3a083
```

## 09-hardneg-02-restored
```text
1a91cd2788e52a8d7d1cf63a1810b32735d75358
30b7936d8d0e90a0f1e8626f0406e06c96344dc0
4b05ae2c4cccef81026763c2d07fff15c6ec5605
53335978d9775ae124c6ebbde9557c8177c1b931
7e95e76baf6e2a9cdb15371cebf79417a15151b6
7f37efee50f1875bdc5b3e3a10651e21edbf8ca1
ad7e36cd11ddef3d6a32bdf957240512db60ae46
b73e80cc422011996b14331396d28e0ab846fdae
d28735328c55165d821d20974eb512badad61658
d728de68c4b102a924e9281faa16f08c19111221
ea01eb43afd87cf181ef400a846a60e398f527f6
fbb5f94303b74abb8b21e97acbc06b6f00de1581
```

## 10-hardneg-05-version-mutant
```text
125a8eb073939a8054156a73d28ec2117a4db3e2
139add4de8128ad98208ebc106ae1df2f53a48e0
2d7a4f70e960e2bf681f5955b18f07ef1391a1b3
2dbc40b146e23b863ac13573d68b0bf938ee993d
2f6f5da1a79d35b38a8941b47d72ccdbfb558006
4527ff0ca9827c4d11679c3de48c285e369c328c
7c6977ef9c22917b8946be5c3aeb84d1307ac347
b5935cf813bef90017ea16b7f73843c6f4f60c61
e8c993d3c267109221052f728a0b36929363b2ab
ea438965550ac64113962fb81976462acea55175
efcd193815a756b0069fbddba252a0a2ba351af0
f4da634254a6f543e22098d9a36d6c3c54d0e747
```

## 10-hardneg-05-version-restored
```text
3ac8b2eefa270933ca6a25a278f9aaa897e3b372
4ee2416229b1783ea437f4efe4ab104e9b502de1
570dc6907707f28a65e873497b7e0cc46556a424
660327ef341080470795630a880890e716be7a77
772d4504847d2aad38921b42478414d9060057aa
9007e388a5689e6e8b04df1c3bf701b7f8f3e296
951cf9b748dd69107dc8e4940f6218dbc5e5c34f
d7d39891d9e9b0587cf522e88f3df068b63ae06c
e31c233e74e3a6ea3676187ec0eace7416e5ff66
e6ecaac6719e697755f75b13911a8c96c0b28645
f947072ae795bbc279c56cc8ab685d94b17a0ee9
fca1829b3e445cb89065e72c589a2744e75830dc
```

## 11-hardneg-05-body-date-mutant
```text
05924979e87c938e2357b672a40b091b9b5282f9
39550add2744c7338c131bb9375a84938b172bdc
47f9d2d308e6cbe0dc8ba003a6a4c4df2527e291
48e71100c2fa66a29de14ec9c2a6a006f492f5b6
4c45d56cf74350e308d2bb81a0e4611f29814f94
68cf3e05bab1b040a36df8e2f1467aed28d54860
6cea9940fb7b1f69b8c0a755832e148dfdf341d1
87fd41e7a1abf894d2d45585450e41bd46987e94
9a1f69bbacd8765727bfa9c4334e0757e84dc7af
9d1b88d87e647c864022e31b2e51c55eddbe93ec
c98c84f1540cf753df300dea56fcd9f8bbc0cf42
de799c82c713b29148f0bbdcf4f267a9fc93bee2
```

## 11-hardneg-05-body-date-restored
```text
0d32d0d18f7c43df2171c949ecd9d9afc5f156c9
1a338a014c339fa8da8c07d7dda6b3ab104fc084
74ad3764c70dc95000c506a1f110435f5871b76f
88f351c15ea718243a7380bc72ff7d9a6fc9a932
9dbbd8e7efcf45c3ed75223bfc048c0591088416
bf07cd0279f0945c6017250176719ad2a4d925e6
c06ea2e5cef6b0e94c5923294ccd333bd303da55
c8f95dfda03a0f93764e3789240503c1070a0f19
e1be707b930b55b4a058da8cd69e32fc7dc47b1b
ea8a4eddc127af6197049caae917db1d4923ca37
f411cd2f9279cc26013333000cad948fd293b6d7
fd56f4b8ce69127993a51d704c362951870d0631
```

## 12-hardneg-06-mutant
```text
0d243ed1dae06e178872c14f0fc8b304be4f0c83
5d0c3ddca63f514fec183180c6a23907c50bda2e
66dd34bf13a774d8e3265c526a6d4eca59037f12
6825c16d73a66e5c45c1a654ade461fb4d8b7b5c
6f9ba682e3917d3b2d437b8e3ddf0456f237745d
83466e1815ca8078d2c20adf3b2e3e1c84b5045b
b81f5de885a9958d71b37990d1d8a5766798ac26
ddab8785e1e2e956399afed870a4a8e04976bb11
ee316fa835a7445df03c5b07358980fa0f0f5e5d
f0890227e223d6c89305af7d95e90af2311a3b2b
f7788607cccebe88040facda034fd931c48b31d5
fe9fabc3fc1cf5b1b843ce8ac0d8b9ad0c420d0b
```

## 12-hardneg-06-restored
```text
03ae858df05b95a26e78bba8f3f1bc647e93e6b0
17a56582a9943217750218468db325743d194516
22ade4c3eb0192cadd2f1105d675d9ee3106c209
2f5baf570e6855562432b4fe4d982e073548b2b8
432ffec21db7833df02478c20a3f616c5d2ab21c
44bb1e023b5b5689404b5f9c423f07385a74e8e8
4c0b7eb432897307b9f84f64c821e0607e575955
7974559e82e25b9f5b2be3cd1bbf7cc4017e7609
90c5d5e9a5630f287e44a8a6b668d59bd38f3350
bf82deff1879032ba1cc33ab2281f9b8fcf215ac
cd4d65b999631ed0665643b74eccc0ee0bb99a8d
f6efc425d15e024b9086f1501616be438557ccd8
```

## 13-hardneg-07-mutant
```text
06bb4f18a2f97971e97d935f46dee8d0b6701ddf
13ef467e352b7d9b3423d6319402b2572a3977db
14c7f62c4254c09d4946b61c9152120fb1e34a53
27fd666b366e320919bee0cf58f182a3205fd883
2f4ce846505b58fde837c6c6cdb23db0fc794e72
5c58a40fa76e1cdf5a202c3463e026bb5f01b8dc
8186709ae996e9f00a442ffac1754c7d2d18d759
82fa297d76309caea3523b2eccd85c8118cb9b64
8ac703d6cd7d48689c1dc239f859a622f266f167
8d5d796c3c763ff259acca5acd426842b89ae529
d85d04da4b8157e780bd3c55c2a85ffa1e1ec313
d948935e732da141e8aa8125874ead3ef0a755c2
```

## 13-hardneg-07-restored
```text
017fed01761daefa130fa0f17a86bfb17b29b91a
2a000b4685d1a495cdce1961be2bc6ae7b71b073
35fd3f91ab7d74e2389ffb2c1a4f82e525855d42
3e2a14e43fb286676dbfba9fa4781a2c112a895b
465a9d5907bcc51edfab2c2a181f457eaab8169b
63a0863ce4b3ed0443f93f42f48a2fa90b0cedaf
6533f7c9590b3d8ced335ea2365780c1a75c6ad7
7afad1fac418281f05ce23cb5e15419d1a69c7ae
8d9e8b87d80e118bcb711b709f468a3faeb72984
90e8ecfced9a67e24ccb5c187d9a1afc91857d92
d8e819c1e107de3be1d4adcdaf7bd8962ab46cac
e2ca82ccf8f7a178196b5fa47609f4f2e3fdf2c5
```

## 14-threshold-mutant
```text
02019aa249087d595957395f6211147a24ff78e9
21b89185be8dba6b11d7496265c2c8548dd6cab7
5406f23e3f11c92ba7d0cedf2e527ffdaa6716e7
7371618d6314b349f6a2a8fcaf78287a0b0299de
7c54564ab2f313e1d69f0dd0a77ff255613f32ae
7d24d59baef67e13b20293f2061d57f109726411
8b2ff61250d72621770e055705e3fe3bbd97c6ce
8db6f84191c60b156f3b6946852a24e0a56456f3
b18102edb08b1a456716bd6a6b8ebcbb0112ca4d
c28252db4082f8215d1b64fdf8e3c73607026e9b
db7e312a0fdab4bf0f36ae3a2a2dc74012622b65
e4a1d36ba4f7a6ad223646c9dc39c6cd414e96b4
```

## 14-threshold-restored
```text
01c339e13ae3d4318808275473f7b35279ada30e
14dcfdcc75bc4d9114c34cd3eeb111cbb48a9ff2
1a81882f25bc6c90f93754f9f6910e90438e631d
51c8e0d1e721079e32b3d12570b3ad7352100094
51e509bf0b6844f4dfd1e4336a130d08ae53a519
9645b999d310c2d3c807f3cca7a66619d531fa8f
997f63268543fad6f1cb4a2806bb7e920df6dc84
9b592201c47fc2ae0f83f3a583d46ed1fc164bbb
a3b6790b4282538252a5a8381cfbccd05cb11664
d8aa3555ec9e7d45c5042e0ebf3587aa6c28eae0
eef8f5b11296aa7608fb08bdf8aa3d44ba525f3e
f2d0f2e217e056ebe120668abef6491c8804c7e2
```
