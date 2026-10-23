Result: DONE — 26 defect candidates and 5 freshly generated equivalents probed; 13 defects killed, 13 survived, all 5 equivalents survived, and every counter mutation was restored exactly.
# MutC1Counter: frozen self-test mutation probe
## Scope, detector, and evidence
- Axes: detector discrimination, measurement-path relevance, isolated single-defect probes, and exact restoration. Leaf seat: no subagent dispatch, integration, runtime/client invocation, or lane code changes.
- Sandbox: `/fast/scratch/hyaku/kotoba-r59/MutC1Counter`. Checkout is frozen commit `4b2125c91ea1868a83b7b28eb4bbbacc35f469fe`, not a build revision. No sandbox commit was created by this probe driver; the frozen self-test creates and removes its own temporary git worlds inside the sandbox.
- Frozen counter: `verifiers/check_hook_files.py`; committed targets read at lines 253–254: `TARGET = 4`, `NEW_TARGET = 5`. All source line references below refer to this frozen file.
- Baseline/restored SHA-256, denoted **B** below: `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71`. Every pristine/restored receipt records this full hash and `matches_frozen_bytes: true`, checked by exact byte comparison against `git show <freeze>:verifiers/check_hook_files.py`, not just by hash.
- Raw evidence: `/fast/scratch/hyaku/kotoba-r59/MutC1Counter/.mutation-receipts/`. For each ID, `<ID>.pristine.json`, `<ID>.mutated.json`, and `<ID>.restored.json` contain UTC start, elapsed time, command, return code, stdout, stderr, byte/hash evidence; the mutated receipt also carries the full unified diff. `manifest.json` records every generated edit. The runner is `/fast/scratch/hyaku/kotoba-r59/MutC1Counter/.mutation-probe.py`.
- Exactly **93** bounded detector invocations: pristine → mutant → restored for each of 31 cases. All 62 pristine/restored runs exited 0 with 323 assertions; none was a failing baseline. All stderr streams were empty; no timeouts, tracebacks, or environmental failures occurred. All 13 kills were explicit assertion failures, not syntax/import failures.
- Detector command, identical for all phases, from the sandbox root:

```sh
timeout 60 python3 -B verifiers/check_hook_files.py --self-test
```
- Each phase was invoked by `timeout 90 python3 -B .mutation-probe.py <pristine|mutated|restored> <ID>` (exit 0 for the recording helper); the detector exit is recorded separately. Runs were sequential because they share one isolated counter file. `TMPDIR`, `TMP`, and `TEMP` were all set to the sandbox `.mutation-tmp` directory; inherited `GIT_DIR`, `GIT_WORK_TREE`, and `GIT_INDEX_FILE` were removed. The helper uses explicit subprocess deadlines as well as `timeout`.
- UTC interval: `2026-10-23T09:37:09.241895+00:00` through `2026-10-23T09:41:18.629182+00:00` (last invocation start).
- Tool versions observed: `Python 3.14.8`; `git version 2.56.0`. No tools installed or upgraded. No web/source fetches, browser use, paid calls, or live C1 predicate runs: the assigned self-test uses its existing fake curl results. These results concern **self-test coverage**, not whether the frozen production counter or the C1 build actually accepts a bad real page.
Pristine/restored stdout, identical in every such receipt (exit 0; stderr empty):

```text
counter sha256 f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71
self-test: 0 failure(s) over 323 assertions
```
## Coverage findings and claim relevance
1. **Live Events wiring survives deletion (M06); snapshot Events deletion does not (M11).** `main` passes events into the live checker at line 2391, but the end-to-end fixtures at 2232–2244 provide either complete pages, a 404, or a curl exception. There is no successful-status live page missing an event. [INFERENCE] M06 could count a live page whose quote/token still match but whose required events disappeared, despite a valid committed snapshot. That matters directly to F and hence G.
2. **Committed-byte hash checks are exercised; revision provenance is not fully exercised.** Bypassing the sha mismatch (M07), trimming bytes before hashing (M08), and reading snapshots at BASE (M10) are killed. Reading from the working tree instead of the measured revision (M09) survives. The fixture writes pages at 2223–2224 and commits them at 2225–2227, but does not diverge those working-tree pages from the measured commit. [INFERENCE] M09 could substitute an uncommitted snapshot and source pin for bytes absent/different at `--rev`; the hash alone would not restore the committed-provenance guarantee.
3. **The real curl argv is bypassed by the main-path fixtures.** At 2246–2250 `run_curl` is replaced by `live_ok`, then by `live_404` and `live_down` at 2264 and 2276. Consequently changed Accept (M15), bot User-Agent (M16), and disabled curl cap (M17) all survive. [INFERENCE] M15/M16 matter to which live representation is measured; they are especially relevant to the frozen header-sensitive contract, but this probe does not claim any particular vendor response. M17 is an operational bound violation, not evidence of a false-positive count.
4. **Fetch policy has untested branches.** Accepting 201 (M12), dropping redirect host pins (M13), dropping redirected-base-URL rejection (M14), making only one attempt (M18), and dropping the 5 MiB bound (M19) all survive. The mocked effective URLs remain the requested URLs, bodies are small, and no transient-then-success sequence is provided (2232–2244). [INFERENCE] M12/M13/M14/M19 can admit out-of-contract responses; M18 can turn a recoverable transient fetch into a false negative. These are measurement-path findings, not equivalent changes.
5. **G over FOUND is genuinely covered.** Counting backed instead of found rows (M20) is killed by two exact summary assertions: on 404/curl failure the mutant prints `new ground 2`, not 0. Ignoring held occurrences (M21) and dropping casefold deduplication (M22) are also killed. This is stronger evidence than merely testing the isolated `new_ground` helper.
6. **Predicate conjunction is covered; frozen numeric pins are not.** `and`→`or` (M23) is killed, but `TARGET = 4`→3 (M24) and `NEW_TARGET = 5`→4 (M25) survive. The self-test overwrites the targets with 5/3 at 1833 and 2/2 at 2248; its own-sha test at 2197–2200 checks consistency with the current file, not equality to the frozen digest. [INFERENCE] M25 is material: a valid world with F≥4 and G=4 could pass the mutant and fail the frozen predicate. **M24 is not a demonstrated pass/fail weakness on valid main-path worlds:** lines 2398–2409 make G≤F, so NEW_TARGET=5 already forces F≥5, making either F≥4 or F≥3 redundant. M24 still exposes absence of a frozen-constant integrity assertion. Do not count it as an independent acceptance-path failure.
7. **The singly-unfrozen sentinel test is mislabeled (M26).** Lines 1838–1840 set both targets to `None` and run the same predicate twice; the second assertion says “with one set” but sets neither. Changing the guard to require both `None` therefore survives. [INFERENCE] a singly-unfrozen configuration could then raise during comparison; it is not reachable under the actual frozen integer targets and is not a C1 measurement-path false positive.
8. **Five equivalents were generated from these expressions during this assignment, not imported from a published list.** E01–E05 all survive, as expected; proofs appear per case. They are sanity controls and are excluded from the 13/26 defect-candidate kill count. These are selected probes, not a population coverage estimate.
No counter, rule, census, or target change is proposed or integrated. Surviving mutants identify missing self-test discrimination; they do not authorize changing the frozen measurement contract. The event-semantic requirement still needs its designated semantic review; this self-test probe does not certify it.
## Per-mutant ledger
`P/M/R` means pristine/mutated/restored detector exit codes. All phases use the command above. The before/after hash column is B/B for every row; full B is printed above and in every phase receipt.

| ID | Frozen line | Mutation | Verdict | P/M/R | Mutant failures / 323 | Before/after sha256 | Mutated sha256 |
|---|---:|---|---|---|---:|---|---|
| M01 | 718 | Events: allow a single distinct span | KILLED | 0/1/0 | 3 | B / B | `84a6e28a763f92545b1c4a87a74390167c10fe6f3517fca00cb117e64226b7f7` |
| M02 | 710 | Events: count duplicate spans | KILLED | 0/1/0 | 1 | B / B | `1e759ba9baa081bf8bb77d7964fc29ce073e22057a2481b28ae62d7470b3889e` |
| M03 | 722 | Events: bypass identifier validation | KILLED | 0/1/0 | 1 | B / B | `45bd1b2a66a103cd31002725d17b1e3e24391bad100de072bb6bffb531077e67` |
| M04 | 756 | Events: omit the right identifier boundary | KILLED | 0/1/0 | 5 | B / B | `194510f88c8fda608acaffc31e5e9e7d7e9cd89c6da3facea7a8465e7f16ff9d` |
| M05 | 750 | Events: compare names case-insensitively | KILLED | 0/1/0 | 1 | B / B | `78c80acadb9f42e6c94c57835b37bd2b4c3f94bc81ab3ea5539ea12c546d7d05` |
| M06 | 2391 | Events: omit live-page event checking | SURVIVED | 0/0/0 | 0 | B / B | `ecf537ce022dea605125cf2f808dbc086e6c5ed1e992775733a1174d73b84591` |
| M07 | 858 | Snapshot: bypass the sha256 mismatch rejection | KILLED | 0/1/0 | 2 | B / B | `3a99b46eb38826f4b6c5e1ed813cb6d3f83810ae3aa2238160def5e940b39757` |
| M08 | 857 | Snapshot: strip trailing bytes before hashing | KILLED | 0/1/0 | 2 | B / B | `aee20dbe5f326863bc7901cca68cfb0b5dc3ca20eef30a7079f6a920a4c97268` |
| M09 | 2378 | Snapshot: read the working tree rather than measured revision | SURVIVED | 0/0/0 | 0 | B / B | `90df42174e1fa6f563b4c45175bbc06a0a3dabedcef957067d36a3389870d244` |
| M10 | 2379 | Snapshot: read from BASE instead of measured revision | KILLED | 0/1/0 | 11 | B / B | `def130bcf03f0ba55be76088e41ac6a3f2d85fd55298df51d821a745327167ae` |
| M11 | 864 | Snapshot: omit snapshot event checking | KILLED | 0/1/0 | 4 | B / B | `a40e3f1c0c4e87cce9651f52980fb926b13fe2083075a1978e6d05cd6ae49623` |
| M12 | 1096 | Fetch: accept HTTP 201 as well as 200 | SURVIVED | 0/0/0 | 0 | B / B | `88058c04574c8ef094db49979c128f58aecb7a38972fb363331e4912788fdfe1` |
| M13 | 1098 | Fetch: omit the final redirect host pin | SURVIVED | 0/0/0 | 0 | B / B | `0f3ec68648291a705c72ef563a2f4924e7e23ea1faba2441180bcba14a0b55a1` |
| M14 | 1100 | Fetch: omit final-URL base reuse rejection | SURVIVED | 0/0/0 | 0 | B / B | `73c933847d523d4ddc8e7f6921542cec7fb53e66de3d3bccdb125ffd315cd03d` |
| M15 | 1067 | Curl: replace the frozen Accept header | SURVIVED | 0/0/0 | 0 | B / B | `bb45e0c65739ab594c1ffc9b75c6391c344524f9b860c604884b21572ffa08cf` |
| M16 | 1066 | Curl: replace browser User-Agent with bot User-Agent | SURVIVED | 0/0/0 | 0 | B / B | `c8dfbc4542721886fe667492518daee7b1164916955758e7a9ccdd83b206f222` |
| M17 | 1065 | Curl: disable curl max-time | SURVIVED | 0/0/0 | 0 | B / B | `231c1cdafd57efed60522b6ce30965845c45d6b219af7c56344e3a1459973970` |
| M18 | 1093 | Fetch: reduce retries to one attempt | SURVIVED | 0/0/0 | 0 | B / B | `2b84afb13fce4027d0925dcc38442045899d7d46a2b6d106dd93631f4588d2ef` |
| M19 | 1104 | Fetch: omit the five-MiB body limit | SURVIVED | 0/0/0 | 0 | B / B | `8cd5753778b3f8901137c733a4a18ebbd66f5cdef941f5029390464abd2d0a5b` |
| M20 | 2398 | Ground: compute G from backed rather than found rows | KILLED | 0/1/0 | 2 | B / B | `90548354bd0a98789645a14da613204df48cf719f1d9f396e1030bca06e59c04` |
| M21 | 1260 | Ground: ignore held occurrences | KILLED | 0/1/0 | 2 | B / B | `787af1967e255b87aeaad334df20859fff31dd16d6e1ea7301d6bb0e739dde1a` |
| M22 | 1260 | Ground: drop casefold deduplication | KILLED | 0/1/0 | 1 | B / B | `b2fb349084bc1748b3c89776ba6f217d4ebd0752d222565c52c8b1e29454629d` |
| M23 | 1251 | Predicate: replace the F/G conjunction with disjunction | KILLED | 0/1/0 | 2 | B / B | `57ba644cfd1fe1852f1f728af9dbc012f12264ae74a1c92d55cd2fcadfe8e1c5` |
| M24 | 253 | Predicate: lower the frozen F target | SURVIVED | 0/0/0 | 0 | B / B | `44cd50ec859cc72478e9150fc1dd8b8e5772e5193faeca16e7053b69b52b790f` |
| M25 | 254 | Predicate: lower the frozen G target | SURVIVED | 0/0/0 | 0 | B / B | `6eb61db6e362d5772059ffec2e178f9625b6d05f7e3e1cb4bc9997877627070b` |
| M26 | 1249 | Predicate: weaken the unfrozen-target guard to both None | SURVIVED | 0/0/0 | 0 | B / B | `00b24f7222080e63fa863a932ba5c8c73776a776f044c506e04091a9a110b0ee` |
| E01 | 718 | Equivalent: integral event-count boundary spelling | SURVIVED (equivalent) | 0/0/0 | 0 | B / B | `c8dd3c60d7bbad83bed3d34e6c59671ec2df4ddf713508f97a34529c12d93e7f` |
| E02 | 858 | Equivalent: negate digest equality | SURVIVED (equivalent) | 0/0/0 | 0 | B / B | `01258944f635cd40afb1d2b157feed4aca7f398426f3343a2d42ed371ac1b5de` |
| E03 | 1104 | Equivalent: reverse the byte-limit comparison | SURVIVED (equivalent) | 0/0/0 | 0 | B / B | `0ec5e268d1b2b535a2b4ca70a96dd283b6baa221ce32a455ef3a0477e5025671` |
| E04 | 2398 | Equivalent: explicit truth conversion for found-row filtering | SURVIVED (equivalent) | 0/0/0 | 0 | B / B | `f800ac2296bc1ffb3e7a7e10f07152189d539233ed6001d72c05bc58e63d279d` |
| E05 | 1251 | Equivalent: commute the pure integer target conjunction | SURVIVED (equivalent) | 0/0/0 | 0 | B / B | `f7196e270af6f0998fb9fc582fceee89f0afbe6a246ef6fae171188b97fd74ff` |

## Exact diffs, expected detector, and observed output

All diffs compare each mutant independently against the same pristine frozen file. Every mutant was restored before the next was applied. All mutant stderr was empty. Conditional measurement consequences below are [INFERENCE], not additional executed detectors.

### M01 — Events: allow a single distinct span

- Expected detector/property: `Reject a one-span Events cell`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Cell minimum directly controls backing.
- Receipts: `.mutation-receipts/M01.pristine.json`, `.mutation-receipts/M01.mutated.json`, `.mutation-receipts/M01.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -716,5 +716,5 @@
     """The events-cell rule: >= 2 distinct spans, each a bare identifier."""
     why: list[str] = []
-    if len(events) < 2:
+    if len(events) < 1:
         why.append("SKILL.md Events cell holds %d distinct backticked name(s) (need >= 2)"
                    % len(events))
```

Actual mutant stdout (full):

```text
counter sha256 84a6e28a763f92545b1c4a87a74390167c10fe6f3517fca00cb117e64226b7f7
FAIL one span does not pass the events cell: got [], expected ['SKILL.md Events cell holds 1 distinct backticked name(s) (need >= 2)']
FAIL an Events cell with one span is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL an Events cell with one span is reported as such: got False, expected True
self-test: 3 failure(s) over 323 assertions
```

### M02 — Events: count duplicate spans

- Expected detector/property: `Repeated span must be counted once`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Repeated names could falsely satisfy the two-distinct-events rule.
- Receipts: `.mutation-receipts/M02.pristine.json`, `.mutation-receipts/M02.mutated.json`, `.mutation-receipts/M02.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -708,5 +708,5 @@
     for span in BACKTICK_RE.findall(cell):
         s = span.strip()
-        if s and s not in out:
+        if s:
             out.append(s)
     return out
```

Actual mutant stdout (full):

```text
counter sha256 1e759ba9baa081bf8bb77d7964fc29ce073e22057a2481b28ae62d7470b3889e
FAIL event_spans counts a repeated span once: got ['PreToolUse', 'PreToolUse', 'Stop'], expected ['PreToolUse', 'Stop']
self-test: 1 failure(s) over 323 assertions
```

### M03 — Events: bypass identifier validation

- Expected detector/property: `Reject the non-identifier pre tool`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Invalid event names could back a row.
- Receipts: `.mutation-receipts/M03.pristine.json`, `.mutation-receipts/M03.mutated.json`, `.mutation-receipts/M03.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -720,5 +720,5 @@
                    % len(events))
     for name in events:
-        if not EVENT_RE.match(name):
+        if False:
             why.append("event %r is not an identifier matching "
                        "^[A-Za-z][A-Za-z0-9_.:-]*$" % name)
```

Actual mutant stdout (full):

```text
counter sha256 45bd1b2a66a103cd31002725d17b1e3e24391bad100de072bb6bffb531077e67
FAIL a non-identifier span does not pass the events cell: got [], expected ["event 'pre tool' is not an identifier matching ^[A-Za-z][A-Za-z0-9_.:-]*$"]
self-test: 1 failure(s) over 323 assertions
```

### M04 — Events: omit the right identifier boundary

- Expected detector/property: `Reject event names inside a longer identifier`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Longer identifiers could be mistaken for real event occurrences.
- Receipts: `.mutation-receipts/M04.pristine.json`, `.mutation-receipts/M04.mutated.json`, `.mutation-receipts/M04.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -754,5 +754,5 @@
         left = i == 0 or text[i - 1] not in EVENT_WORD
         right = j >= len(text) or text[j] not in EVENT_WORD
-        if left and right:
+        if left:
             return i
         start = i + 1
```

Actual mutant stdout (full):

```text
counter sha256 194510f88c8fda608acaffc31e5e9e7d7e9cd89c6da3facea7a8465e7f16ff9d
FAIL event NOT found inside a longer identifier (letter): got True, expected False
FAIL event NOT found inside a longer identifier (digit): got True, expected False
FAIL event NOT found inside a longer identifier (underscore): got True, expected False
FAIL an event found only inside a longer identifier is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL an event inside a longer identifier is reported as not on the page: got False, expected True
self-test: 5 failure(s) over 323 assertions
```

### M05 — Events: compare names case-insensitively

- Expected detector/property: `Reject pretooluse for PreToolUse`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Wrong-case printed names could be accepted.
- Receipts: `.mutation-receipts/M05.pristine.json`, `.mutation-receipts/M05.mutated.json`, `.mutation-receipts/M05.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -748,5 +748,5 @@
     start = 0
     while True:
-        i = text.find(name, start)
+        i = text.casefold().find(name.casefold(), start)
         if i < 0:
             return -1
```

Actual mutant stdout (full):

```text
counter sha256 78c80acadb9f42e6c94c57835b37bd2b4c3f94bc81ab3ea5539ea12c546d7d05
FAIL event matching is case-sensitive: got True, expected False
self-test: 1 failure(s) over 323 assertions
```

### M06 — Events: omit live-page event checking

- Expected detector/property: `A live page missing an event should not be found`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct measurement-path false-positive risk: committed snapshots can pass while the live page omits the events.
- Receipts: `.mutation-receipts/M06.pristine.json`, `.mutation-receipts/M06.mutated.json`, `.mutation-receipts/M06.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -2389,5 +2389,5 @@
             try:
                 page = fetch(r["url"], HOSTS[r["client"]], base_urls)
-                reasons = page_why(page, r["quote"], r["token"], r["events"])
+                reasons = page_why(page, r["quote"], r["token"], [])
                 r["found"] = not reasons
                 r["live_why"] = ["live page: " + x for x in reasons]
```

Actual mutant stdout (full):

```text
counter sha256 ecf537ce022dea605125cf2f808dbc086e6c5ed1e992775733a1174d73b84591
self-test: 0 failure(s) over 323 assertions
```

### M07 — Snapshot: bypass the sha256 mismatch rejection

- Expected detector/property: `Reject a snapshot with different raw bytes`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: A committed snapshot could differ from its source pin.
- Receipts: `.mutation-receipts/M07.pristine.json`, `.mutation-receipts/M07.mutated.json`, `.mutation-receipts/M07.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -856,5 +856,5 @@
                 else:
                     got = hashlib.sha256(data).hexdigest()
-                    if got != sha:
+                    if False:
                         why.append("snapshot %s sha256 %s... does not equal the "
                                    "SOURCES row sha256 %s..."
```

Actual mutant stdout (full):

```text
counter sha256 3a99b46eb38826f4b6c5e1ed813cb6d3f83810ae3aa2238160def5e940b39757
FAIL a snapshot whose sha256 differs from the SOURCES row is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL a snapshot sha mismatch is reported as such: got False, expected True
self-test: 2 failure(s) over 323 assertions
```

### M08 — Snapshot: strip trailing bytes before hashing

- Expected detector/property: `Reject the newline-bumped snapshot`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Pin comparison would no longer hash exact committed bytes.
- Receipts: `.mutation-receipts/M08.pristine.json`, `.mutation-receipts/M08.mutated.json`, `.mutation-receipts/M08.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -855,5 +855,5 @@
                                % snapshot_path(sid))
                 else:
-                    got = hashlib.sha256(data).hexdigest()
+                    got = hashlib.sha256(data.rstrip()).hexdigest()
                     if got != sha:
                         why.append("snapshot %s sha256 %s... does not equal the "
```

Actual mutant stdout (full):

```text
counter sha256 aee20dbe5f326863bc7901cca68cfb0b5dc3ca20eef30a7079f6a920a4c97268
FAIL a snapshot whose sha256 differs from the SOURCES row is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL a snapshot sha mismatch is reported as such: got False, expected True
self-test: 2 failure(s) over 323 assertions
```

### M09 — Snapshot: read the working tree rather than measured revision

- Expected detector/property: `Divergent working-tree and committed snapshots should not substitute`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct measurement-path provenance risk: uncommitted or wrong-revision pages could stand in for the measured snapshot.
- Receipts: `.mutation-receipts/M09.pristine.json`, `.mutation-receipts/M09.mutated.json`, `.mutation-receipts/M09.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -2376,6 +2376,6 @@
         base_sources = git_show(lane, BASE, SOURCES) or ""
         report = judge(skill, entry, sources, lesson, base_sources,
-                       snapshot_of=lambda sid: git_show_bytes(
-                           lane, args.rev, snapshot_path(sid)))
+                       snapshot_of=lambda sid: (
+                           lane / snapshot_path(sid)).read_bytes())
     except (EnvError, UnicodeDecodeError, OSError) as e:
         print("could-not-evaluate: %s" % e, file=sys.stderr)
```

Actual mutant stdout (full):

```text
counter sha256 90df42174e1fa6f563b4c45175bbc06a0a3dabedcef957067d36a3389870d244
self-test: 0 failure(s) over 323 assertions
```

### M10 — Snapshot: read from BASE instead of measured revision

- Expected detector/property: `Positive end-to-end world must load its committed snapshots`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Backed rows would disappear when snapshots exist only in the measured commit.
- Receipts: `.mutation-receipts/M10.pristine.json`, `.mutation-receipts/M10.mutated.json`, `.mutation-receipts/M10.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -2377,5 +2377,5 @@
         report = judge(skill, entry, sources, lesson, base_sources,
                        snapshot_of=lambda sid: git_show_bytes(
-                           lane, args.rev, snapshot_path(sid)))
+                           lane, BASE, snapshot_path(sid)))
     except (EnvError, UnicodeDecodeError, OSError) as e:
         print("could-not-evaluate: %s" % e, file=sys.stderr)
```

Actual mutant stdout (full):

```text
counter sha256 def130bcf03f0ba55be76088e41ac6a3f2d85fd55298df51d821a745327167ae
FAIL main: the satisfying world exits 0: got 1, expected 0
FAIL main: the exact summary line is the first line: got 'hook files backed on committed snapshots 0 of 2; found on the live page 0 of 2; new ground 0', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 2 of 2; new ground 2'
FAIL main: no reject line for a found row: got ['reject Claude Code: entry row S900: snapshot .ufo/waves/round-59/snapshots/S900.page is missing at the revision', 'reject Gemini CLI: entry row S901: snapshot .ufo/waves/round-59/snapshots/S901.page is missing at the revision'], expected []
FAIL main: an HTTP 404 keeps S at 2 and F at 0: got 'hook files backed on committed snapshots 0 of 2; found on the live page 0 of 2; new ground 0', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 0'
FAIL main: the 404 is reported on the reject line: got False, expected True
FAIL a curl failure keeps S at 2 and F at 0: got 'hook files backed on committed snapshots 0 of 2; found on the live page 0 of 2; new ground 0', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 0'
FAIL a curl failure names the backed rows: got (False, False), expected (True, True)
FAIL the unfrozen sentinel still prints the summary: got 'hook files backed on committed snapshots 0 of 2; found on the live page 0 of 2; new ground 0', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 2 of 2; new ground 2'
FAIL without --fetch the summary reads 'live not run' and G is 0: got 'hook files backed on committed snapshots 0 of 2; live not run; new ground 0', expected 'hook files backed on committed snapshots 2 of 2; live not run; new ground 0'
FAIL the broken world prints the one-of-two line: got 'hook files backed on committed snapshots 0 of 2; found on the live page 0 of 2; new ground 0', expected 'hook files backed on committed snapshots 1 of 2; found on the live page 1 of 2; new ground 1'
FAIL the broken world names the Gate on the reject line: got False, expected True
self-test: 11 failure(s) over 323 assertions
```

### M11 — Snapshot: omit snapshot event checking

- Expected detector/property: `Reject an event absent from the snapshot`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Snapshot backing would not prove printed events.
- Receipts: `.mutation-receipts/M11.pristine.json`, `.mutation-receipts/M11.mutated.json`, `.mutation-receipts/M11.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -862,5 +862,5 @@
                     else:
                         page = data.decode("utf-8", errors="replace")
-                        for reason in page_why(page, quote, token, events):
+                        for reason in page_why(page, quote, token, []):
                             why.append("snapshot %s: %s" % (snapshot_path(sid), reason))
     return why, sid, url, quote
```

Actual mutant stdout (full):

```text
counter sha256 a40e3f1c0c4e87cce9651f52980fb926b13fe2083075a1978e6d05cd6ae49623
FAIL an event absent from the snapshot is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL an event absent from the snapshot is reported as such: got False, expected True
FAIL an event found only inside a longer identifier is not backed: got ['Claude Code', 'Gemini CLI'], expected ['Gemini CLI']
FAIL an event inside a longer identifier is reported as not on the page: got False, expected True
self-test: 4 failure(s) over 323 assertions
```

### M12 — Fetch: accept HTTP 201 as well as 200

- Expected detector/property: `Reject every HTTP status other than 200`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct fetch-contract risk if a matching body is served with status 201; the frozen detector requires 200.
- Receipts: `.mutation-receipts/M12.pristine.json`, `.mutation-receipts/M12.mutated.json`, `.mutation-receipts/M12.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1094,5 +1094,5 @@
         try:
             status, final, data = run_curl(url)
-            if status != 200:
+            if status not in (200, 201):
                 raise OSError("HTTP %d at %s" % (status, final))
             if pins is not None and not host_ok(final, pins):
```

Actual mutant stdout (full):

```text
counter sha256 88058c04574c8ef094db49979c128f58aecb7a38972fb363331e4912788fdfe1
self-test: 0 failure(s) over 323 assertions
```

### M13 — Fetch: omit the final redirect host pin

- Expected detector/property: `Reject a redirect off the client pinned hosts`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct measurement-path provenance risk: a pinned source could redirect to an off-host matching page.
- Receipts: `.mutation-receipts/M13.pristine.json`, `.mutation-receipts/M13.mutated.json`, `.mutation-receipts/M13.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1096,5 +1096,5 @@
             if status != 200:
                 raise OSError("HTTP %d at %s" % (status, final))
-            if pins is not None and not host_ok(final, pins):
+            if False and pins is not None and not host_ok(final, pins):
                 raise OSError("fetched off the pinned hosts at %s" % final)
             if base_keys is not None and url_key(final) in base_keys:
```

Actual mutant stdout (full):

```text
counter sha256 0f3ec68648291a705c72ef563a2f4924e7e23ea1faba2441180bcba14a0b55a1
self-test: 0 failure(s) over 323 assertions
```

### M14 — Fetch: omit final-URL base reuse rejection

- Expected detector/property: `Reject a redirect to an already-held base source URL`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct new-source provenance risk: a new URL can redirect to a BASE SOURCES URL.
- Receipts: `.mutation-receipts/M14.pristine.json`, `.mutation-receipts/M14.mutated.json`, `.mutation-receipts/M14.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1098,5 +1098,5 @@
             if pins is not None and not host_ok(final, pins):
                 raise OSError("fetched off the pinned hosts at %s" % final)
-            if base_keys is not None and url_key(final) in base_keys:
+            if False and base_keys is not None and url_key(final) in base_keys:
                 raise OSError("reached a base SOURCES URL %s" % final)
             if url_is_change_note(final):
```

Actual mutant stdout (full):

```text
counter sha256 73c933847d523d4ddc8e7f6921542cec7fb53e66de3d3bccdb125ffd315cd03d
self-test: 0 failure(s) over 323 assertions
```

### M15 — Curl: replace the frozen Accept header

- Expected detector/property: `Exercise run_curl and enforce the frozen header`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct transport-path risk: changed content negotiation can select different bytes; no actual server response is asserted here.
- Receipts: `.mutation-receipts/M15.pristine.json`, `.mutation-receipts/M15.mutated.json`, `.mutation-receipts/M15.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1065,5 +1065,5 @@
     argv = ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
             "-A", CURL_UA,
-            "-H", "Accept: " + CURL_ACCEPT,
+            "-H", "Accept: */*",
             "-w", CURL_WRITE_OUT, url]
     try:
```

Actual mutant stdout (full):

```text
counter sha256 bb45e0c65739ab594c1ffc9b75c6391c344524f9b860c604884b21572ffa08cf
self-test: 0 failure(s) over 323 assertions
```

### M16 — Curl: replace browser User-Agent with bot User-Agent

- Expected detector/property: `Exercise run_curl and enforce the frozen User-Agent`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct transport-path risk: servers may serve bots different bytes or deny access; no live fetch was made.
- Receipts: `.mutation-receipts/M16.pristine.json`, `.mutation-receipts/M16.mutated.json`, `.mutation-receipts/M16.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1064,5 +1064,5 @@
     the body."""
     argv = ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
-            "-A", CURL_UA,
+            "-A", "kotoba-check-hook-files",
             "-H", "Accept: " + CURL_ACCEPT,
             "-w", CURL_WRITE_OUT, url]
```

Actual mutant stdout (full):

```text
counter sha256 c8dfbc4542721886fe667492518daee7b1164916955758e7a9ccdd83b206f222
self-test: 0 failure(s) over 323 assertions
```

### M17 — Curl: disable curl max-time

- Expected detector/property: `Exercise run_curl and enforce the 30-second attempt cap`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Measurement operational risk: a real request loses the frozen per-attempt time bound, not an observed false-positive count.
- Receipts: `.mutation-receipts/M17.pristine.json`, `.mutation-receipts/M17.mutated.json`, `.mutation-receipts/M17.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1063,5 +1063,5 @@
     the URL after redirects come from curl's own write-out trailer, never from
     the body."""
-    argv = ["curl", "-sSL", "--max-time", str(FETCH_TIMEOUT),
+    argv = ["curl", "-sSL", "--max-time", "0",
             "-A", CURL_UA,
             "-H", "Accept: " + CURL_ACCEPT,
```

Actual mutant stdout (full):

```text
counter sha256 231c1cdafd57efed60522b6ce30965845c45d6b219af7c56344e3a1459973970
self-test: 0 failure(s) over 323 assertions
```

### M18 — Fetch: reduce retries to one attempt

- Expected detector/property: `Retry a transient failure followed by a valid page`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct measurement availability/false-negative risk: a recoverable transient failure would no longer be retried.
- Receipts: `.mutation-receipts/M18.pristine.json`, `.mutation-receipts/M18.mutated.json`, `.mutation-receipts/M18.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1091,5 +1091,5 @@
     redirects is a base SOURCES URL is not found.  Both only add failures."""
     last: Exception | None = None
-    for _ in range(FETCH_ATTEMPTS):
+    for _ in range(1):
         try:
             status, final, data = run_curl(url)
```

Actual mutant stdout (full):

```text
counter sha256 2b84afb13fce4027d0925dcc38442045899d7d46a2b6d106dd93631f4588d2ef
self-test: 0 failure(s) over 323 assertions
```

### M19 — Fetch: omit the five-MiB body limit

- Expected detector/property: `Reject an oversized matching response body`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct frozen-fetch contract risk: oversized matching pages could be counted.
- Receipts: `.mutation-receipts/M19.pristine.json`, `.mutation-receipts/M19.mutated.json`, `.mutation-receipts/M19.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1102,5 +1102,5 @@
             if url_is_change_note(final):
                 raise OSError("reached a change-note page %s" % final)
-            if len(data) > MAX_BYTES:
+            if False and len(data) > MAX_BYTES:
                 raise OSError("page exceeds 5 MiB")
             return data.decode("utf-8", errors="replace")
```

Actual mutant stdout (full):

```text
counter sha256 8cd5753778b3f8901137c733a4a18ebbd66f5cdef941f5029390464abd2d0a5b
self-test: 0 failure(s) over 323 assertions
```

### M20 — Ground: compute G from backed rather than found rows

- Expected detector/property: `HTTP 404 must leave G at zero despite S=2`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: G could count rows whose live pages failed.
- Receipts: `.mutation-receipts/M20.pristine.json`, `.mutation-receipts/M20.mutated.json`, `.mutation-receipts/M20.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -2396,5 +2396,5 @@
                 r["live_why"] = ["live fetch failed: %s" % e]
             found += 1 if r["found"] else 0
-    counted = [r for r in backed if r.get("found")] if args.fetch else []
+    counted = backed if args.fetch else []
     ground = 0
     if args.fetch:
```

Actual mutant stdout (full):

```text
counter sha256 90548354bd0a98789645a14da613204df48cf719f1d9f396e1030bca06e59c04
FAIL main: an HTTP 404 keeps S at 2 and F at 0: got 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 2', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 0'
FAIL a curl failure keeps S at 2 and F at 0: got 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 2', expected 'hook files backed on committed snapshots 2 of 2; found on the live page 0 of 2; new ground 0'
self-test: 2 failure(s) over 323 assertions
```

### M21 — Ground: ignore held occurrences

- Expected detector/property: `A held token contributes no new ground`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Previously held tokens could inflate G.
- Receipts: `.mutation-receipts/M21.pristine.json`, `.mutation-receipts/M21.mutated.json`, `.mutation-receipts/M21.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1258,5 +1258,5 @@
     itself is case-insensitive, so both spellings of one token get the same
     answer, and two clients whose tokens differ in case alone count once."""
-    return len({t.casefold() for t in norms if t and not held.get(t)})
+    return len({t.casefold() for t in norms if t})
 
 
```

Actual mutant stdout (full):

```text
counter sha256 787af1967e255b87aeaad334df20859fff31dd16d6e1ea7301d6bb0e739dde1a
FAIL ground: a held spelling drops its own key: got 1, expected 0
FAIL ground: a held token is not new ground: got 1, expected 0
self-test: 2 failure(s) over 323 assertions
```

### M22 — Ground: drop casefold deduplication

- Expected detector/property: `Two case-only spellings contribute one distinct token`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Case variants could inflate G.
- Receipts: `.mutation-receipts/M22.pristine.json`, `.mutation-receipts/M22.mutated.json`, `.mutation-receipts/M22.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1258,5 +1258,5 @@
     itself is case-insensitive, so both spellings of one token get the same
     answer, and two clients whose tokens differ in case alone count once."""
-    return len({t.casefold() for t in norms if t and not held.get(t)})
+    return len({t for t in norms if t and not held.get(t)})
 
 
```

Actual mutant stdout (full):

```text
counter sha256 b2fb349084bc1748b3c89776ba6f217d4ebd0752d222565c52c8b1e29454629d
FAIL ground: two spellings of one token count once: got 2, expected 1
self-test: 1 failure(s) over 323 assertions
```

### M23 — Predicate: replace the F/G conjunction with disjunction

- Expected detector/property: `Fail when either F or G misses its target`.
- Observed verdict: **KILLED**; mutant detector exit `1`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: C1 could pass with only one target met.
- Receipts: `.mutation-receipts/M23.pristine.json`, `.mutation-receipts/M23.mutated.json`, `.mutation-receipts/M23.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1249,5 +1249,5 @@
     if TARGET is None or NEW_TARGET is None:
         return 1
-    return 0 if found >= TARGET and ground >= NEW_TARGET else 1
+    return 0 if found >= TARGET or ground >= NEW_TARGET else 1
 
 
```

Actual mutant stdout (full):

```text
counter sha256 57ba644cfd1fe1852f1f728af9dbc012f12264ae74a1c92d55cd2fcadfe8e1c5
FAIL predicate: fetch, 4 of 7, ground 3, fails: got 0, expected 1
FAIL predicate: fetch, 5 of 7, ground 2, fails: got 0, expected 1
self-test: 2 failure(s) over 323 assertions
```

### M24 — Predicate: lower the frozen F target

- Expected detector/property: `Detect drift from the frozen TARGET=4`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct frozen-counter integrity risk; F boundary weakens. With G<=F and NEW_TARGET=5, lowering F alone is pass/fail-redundant on valid worlds, but changes frozen bytes and declared target.
- Receipts: `.mutation-receipts/M24.pristine.json`, `.mutation-receipts/M24.mutated.json`, `.mutation-receipts/M24.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -251,5 +251,5 @@
 LESSON = "corpus/lessons/round-59.md"
 SNAPSHOT_DIR = ".ufo/waves/round-59/snapshots"
-TARGET = 4
+TARGET = 3
 NEW_TARGET = 5
 MIN_WORDS = 6
```

Actual mutant stdout (full):

```text
counter sha256 44cd50ec859cc72478e9150fc1dd8b8e5772e5193faeca16e7053b69b52b790f
self-test: 0 failure(s) over 323 assertions
```

### M25 — Predicate: lower the frozen G target

- Expected detector/property: `Detect drift from the frozen NEW_TARGET=5`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Direct measurement pass/fail risk: F>=4 and G=4 could now pass, whereas the frozen predicate requires G>=5.
- Receipts: `.mutation-receipts/M25.pristine.json`, `.mutation-receipts/M25.mutated.json`, `.mutation-receipts/M25.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -252,5 +252,5 @@
 SNAPSHOT_DIR = ".ufo/waves/round-59/snapshots"
 TARGET = 4
-NEW_TARGET = 5
+NEW_TARGET = 4
 MIN_WORDS = 6
 MAX_WORDS = 25
```

Actual mutant stdout (full):

```text
counter sha256 6eb61db6e362d5772059ffec2e178f9625b6d05f7e3e1cb4bc9997877627070b
self-test: 0 failure(s) over 323 assertions
```

### M26 — Predicate: weaken the unfrozen-target guard to both None

- Expected detector/property: `Reject either singly-unfrozen target without an exception`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Measurement-path relevance [INFERENCE]: Not exercised by the frozen measurement path, whose targets are both integers; relevant to the documented guard. The self-test label claiming one set does not actually set one.
- Receipts: `.mutation-receipts/M26.pristine.json`, `.mutation-receipts/M26.mutated.json`, `.mutation-receipts/M26.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1247,5 +1247,5 @@
     if not fetching:
         return 1
-    if TARGET is None or NEW_TARGET is None:
+    if TARGET is None and NEW_TARGET is None:
         return 1
     return 0 if found >= TARGET and ground >= NEW_TARGET else 1
```

Actual mutant stdout (full):

```text
counter sha256 00b24f7222080e63fa863a932ba5c8c73776a776f044c506e04091a9a110b0ee
self-test: 0 failure(s) over 323 assertions
```

### E01 — Equivalent: integral event-count boundary spelling

- Expected detector/property: `Remain green under the same detector`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Equivalence proof: Equivalent because len(events) is an integer; <2 iff <=1.
- Receipts: `.mutation-receipts/E01.pristine.json`, `.mutation-receipts/E01.mutated.json`, `.mutation-receipts/E01.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -716,5 +716,5 @@
     """The events-cell rule: >= 2 distinct spans, each a bare identifier."""
     why: list[str] = []
-    if len(events) < 2:
+    if len(events) <= 1:
         why.append("SKILL.md Events cell holds %d distinct backticked name(s) (need >= 2)"
                    % len(events))
```

Actual mutant stdout (full):

```text
counter sha256 c8dd3c60d7bbad83bed3d34e6c59671ec2df4ddf713508f97a34529c12d93e7f
self-test: 0 failure(s) over 323 assertions
```

### E02 — Equivalent: negate digest equality

- Expected detector/property: `Remain green under the same detector`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Equivalence proof: Equivalent because got and sha are ordinary strings, so != is not ==.
- Receipts: `.mutation-receipts/E02.pristine.json`, `.mutation-receipts/E02.mutated.json`, `.mutation-receipts/E02.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -856,5 +856,5 @@
                 else:
                     got = hashlib.sha256(data).hexdigest()
-                    if got != sha:
+                    if not (got == sha):
                         why.append("snapshot %s sha256 %s... does not equal the "
                                    "SOURCES row sha256 %s..."
```

Actual mutant stdout (full):

```text
counter sha256 01258944f635cd40afb1d2b157feed4aca7f398426f3343a2d42ed371ac1b5de
self-test: 0 failure(s) over 323 assertions
```

### E03 — Equivalent: reverse the byte-limit comparison

- Expected detector/property: `Remain green under the same detector`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Equivalence proof: Equivalent because both operands are integers and evaluate without side effects.
- Receipts: `.mutation-receipts/E03.pristine.json`, `.mutation-receipts/E03.mutated.json`, `.mutation-receipts/E03.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1102,5 +1102,5 @@
             if url_is_change_note(final):
                 raise OSError("reached a change-note page %s" % final)
-            if len(data) > MAX_BYTES:
+            if MAX_BYTES < len(data):
                 raise OSError("page exceeds 5 MiB")
             return data.decode("utf-8", errors="replace")
```

Actual mutant stdout (full):

```text
counter sha256 0ec5e268d1b2b535a2b4ca70a96dd283b6baa221ce32a455ef3a0477e5025671
self-test: 0 failure(s) over 323 assertions
```

### E04 — Equivalent: explicit truth conversion for found-row filtering

- Expected detector/property: `Remain green under the same detector`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Equivalence proof: Equivalent because an if-filter already applies the same truth conversion.
- Receipts: `.mutation-receipts/E04.pristine.json`, `.mutation-receipts/E04.mutated.json`, `.mutation-receipts/E04.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -2396,5 +2396,5 @@
                 r["live_why"] = ["live fetch failed: %s" % e]
             found += 1 if r["found"] else 0
-    counted = [r for r in backed if r.get("found")] if args.fetch else []
+    counted = [r for r in backed if bool(r.get("found"))] if args.fetch else []
     ground = 0
     if args.fetch:
```

Actual mutant stdout (full):

```text
counter sha256 f800ac2296bc1ffb3e7a7e10f07152189d539233ed6001d72c05bc58e63d279d
self-test: 0 failure(s) over 323 assertions
```

### E05 — Equivalent: commute the pure integer target conjunction

- Expected detector/property: `Remain green under the same detector`.
- Observed verdict: **SURVIVED**; mutant detector exit `0`; pristine/restored exits `0/0`; restoration is byte-exact (B).
- Equivalence proof: Equivalent on the counter domain after the None guard: both comparisons are pure integer comparisons with the same conjunction.
- Receipts: `.mutation-receipts/E05.pristine.json`, `.mutation-receipts/E05.mutated.json`, `.mutation-receipts/E05.restored.json` under the sandbox above.

```diff
--- a/verifiers/check_hook_files.py
+++ b/verifiers/check_hook_files.py
@@ -1249,5 +1249,5 @@
     if TARGET is None or NEW_TARGET is None:
         return 1
-    return 0 if found >= TARGET and ground >= NEW_TARGET else 1
+    return 0 if ground >= NEW_TARGET and found >= TARGET else 1
 
 
```

Actual mutant stdout (full):

```text
counter sha256 f7196e270af6f0998fb9fc582fceee89f0afbe6a246ef6fae171188b97fd74ff
self-test: 0 failure(s) over 323 assertions
```

## Final restoration and containment

After E05 restoration, these commands ran in the sandbox, each exit 0:

```text
$ timeout 30 sha256sum verifiers/check_hook_files.py
f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71  verifiers/check_hook_files.py
$ timeout 30 git --no-optional-locks rev-parse HEAD
4b2125c91ea1868a83b7b28eb4bbbacc35f469fe
$ timeout 30 python3 --version
Python 3.14.8
$ timeout 30 git --version
git version 2.56.0
$ timeout 30 date -u
Fri 23 Oct 2026 09:41:42 AM UTC
```

Every restoration was also followed by the same bounded self-test, not merely a hash check. No mutation remains applied; the counter is back to its frozen bytes. The only lane file written by this seat is this report. Runner/manifest/raw receipts are retained solely under this seat’s scratch clone as reproducibility evidence, not production scaffolding. No lane Git/jj write, fleet-root write, sibling-source write, push, or tool installation occurred.

Report: .ufo/waves/round-59/build/MutC1Counter.md
