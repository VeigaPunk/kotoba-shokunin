# ReviewD7Carry — round-51 falsify: the D7 carry paragraph

Verdict: FAILS (narrow). Every round-50 D7 item is named and every open-status reason reproduces at HEAD 59903b26, except one stated fact: "the patch still applies cleanly" is false at HEAD (`git apply --check` exit 1). The paragraph also presents its crash-path count as complete and drops a fourth, unrun path. No D7 item is claimed fixed. A one-line correction to the lesson closes the false fact.

Scope: `corpus/lessons/round-51.md` § Routed defects, D7 (lines 130-138), checked against `.ufo/waves/round-51/build/CarryD7.md` and the round-50 spot-check D7 (`corpus/lessons/round-50-verifier-spotcheck.md` lines 270-274). Clone: `/fast/scratch/hyaku/kotoba-r51/falsify/ReviewD7Carry/lane` at 59903b26 (base 43ca0bfb is an ancestor; status clean). Probes ran on private commits in scratch clones, never in the lane.

## Findings (by severity)

### F1 (Medium) — "the patch still applies cleanly" is false at HEAD
- Lesson line 135. `git apply --check /fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/patch.diff` in the HEAD clone: exit 1, `error: verifiers/check_assertion_floors.py: patch does not apply` (hunk at line 6). The same check on the base `verifiers/` tree (`git archive 43ca0bfb... verifiers | tar -x`): exit 0.
- Cause: the landed C1/C2 edits to `check_assertion_floors.py` move the patch's context. `git diff 43ca0bfb HEAD -- verifiers/check_assertion_floors.py` hunks: `@@ -5,9` (docstring, surfaces 99->115, overlap_levers), `@@ -127,7` (EXPECTED_INSTRUMENTS), `@@ -149,7` (INSTRUMENTS), `@@ -610,8` (self-test anchors), `@@ -701,9` (F6 total 11->12).
- The "unapplied" half holds: `grep -c F30 verifiers/check_assertion_floors.py` -> 0 (exit 1); `check_assertion_floors.py --self-test` -> `0 failure(s) over 150 assertions` (exit 0; the patch's 169 is not in the tree); no `sibling_census` arm exists.
- Effect: CarryD7 "Findings for the integrator" item 3 says D7.7 is "the cheapest item to close — the patch applies cleanly at base". That was true at base. The lesson copied it to HEAD. Fixing D7.7 now needs a rebase first.
- The patch exists only outside the lane, at `/fast/scratch/hyaku/kotoba-r50/build/FloorsRegister/patch.diff`. The only lane reference is `.ufo/waves/round-50/build/FloorsRegister.md:10`. The paragraph names no path.
- Fix: replace the parenthetical with "(the patch no longer applies at HEAD and needs a rebase; it lives outside the lane)".

### F2 (Low) — crash-path count stated as complete; unlabelled-twin laundering is mode-bound
- Lesson lines 131-132: "three crash paths ..., not two". The three are confirmed (R3a-c below). The seat's D7.3 and its Finding 1 also carry a fourth candidate. `run_box_proof` calls `subprocess.run(..., timeout=600)` (driver lines 186-187) and has no `TimeoutExpired` or `OSError` handler (grep: no `TimeoutExpired` in the driver). `ReviewDriver.md` F5 marks it "[INFERENCE from reading the code]" and "Not run". The paragraph drops it, so "three" reads as the full count.
- Reason 1 ("launders through ... unlabelled twins") holds only with `--in-place` (R2). The default mode crashes instead (R2 default, exit 1, FileExistsError). The paragraph does not say so.
- Crash (c) mechanism (code read; the traceback confirms the id): the duplicate work directory is `fixtures-d08-missing-state`, the N/A case. The six-conjunct loop picks that case through the `or holders` fallback (driver line 308), and the N/A loop (lines 331-335) attempts it again. So the D7.1 fix (drop the fallback) also removes this crash trigger. The carry should say so.
- Fix: write "three confirmed (unknown rev, malformed manifest, existing work directory); a fourth, subprocess timeout/OSError at driver lines 186-187, is unrun", and "unlabelled twins launder under --in-place; the default mode crashes".

### F3 (Low) — "the 'counter not registered' class does not repeat" reads as closing the class
- Lesson lines 136-138. True for the new counter. `floors-registry.json` line 3 (`instrument_total` 12) and lines 37-40 (`overlap_levers`, floor 22, path `verifiers/check_overlap_levers.py`). Both in-file tables hold it (guard diff hunks `@@ -127,7`, `@@ -149,7`). `check_overlap_levers.py --self-test` -> `0 failures` / `22 assertions`, exit 0, which matches the INSTRUMENTS regex.
- The same paragraph (lines 133-134) says the C2 driver, the round-50 instance of the class, has no row and cannot get one yet. Scope the sentence to "the new counter is registered; the C2 driver stays unregistered (D7.6)".

### F4 (Low, record) — the paragraph's only source is not committed at HEAD
- The paragraph cites `CarryD7.md`. At 59903b26: `git ls-files .ufo/waves/round-51 | wc -l` -> 0, and `git ls-files .ufo/waves/round-51/build/CarryD7.md | wc -l` -> 0. `.ufo/waves/round-50` has 79 tracked files. The seat report exists only in the lane working tree, where I read it. A checkout of HEAD cannot reproduce the D7 source. The L1 should commit the round-51 wave evidence or record that it stays uncommitted.

### F5 (Info) — what holds
- All seven round-50 D7 items are named (table below). The seat's D7.1-D7.7 are all in the paragraph. The fourth crash path is the only seat item missing (F2).
- No D7 item is claimed fixed. Every item is carried ("Reason for carrying"). The one closed thing is the new counter (F3).

## Per-item check

| # | round-50 D7 item | round-51 paragraph (lesson lines) | HEAD rerun, clone 59903b26 | verdict |
|---|---|---|---|---|
| 1 | driver launders via duplicate-id twins | named (131) | R1 `killed 6 of 6`, exit 0; falsifier `boxes proven 2`, exit 0 | true |
| 2 | driver launders via unlabelled twins | named (131) | R2 `--in-place` `killed 6 of 6`, exit 0; default mode exit 1 (FileExistsError) | true only under --in-place (F2) |
| 3 | kill test is a stderr substring | named (131) | R4 generic failure -> `killed 6 of 6`, exit 0; driver line 205 | true |
| 4 | "two crash paths" | "three, not two" (131-132) | R3a/b/c each exit 1; fourth (timeout/OSError) unrun | three true; count incomplete (F2) |
| 5 | 7 of 17 instrument mutants survive | named (132) | driver bytes unchanged 956ee->HEAD; MutBoxProofCode.md line 3 "10 of 17" break, so 7 survive; NOT rerun | true (cited) |
| 6 | 11 of 28 census-guard mutants survive | named (133) | guard bytes unchanged; self-test `68 assertions`, exit 0; MutGuardCode.md line 46 "17 killed, 11 survived of 28"; NOT rerun | true (cited) |
| 7 | driver not in floors-registry.json | named, reason "no --self-test" (133-134) | registry grep -> 0, exit 1; driver argparse has only `--rev`, `--repo`, `--in-place` (lines 215-220) | true |
| 8 | FloorsRegister F30-F33 unapplied | named, "(the patch still applies cleanly)" (134-135) | F30 grep -> 0; floors self-test `150 assertions`, exit 0; `git apply --check` exit 1 | status true; parenthetical false (F1) |
| + | fourth crash path (seat D7.3, F5) | absent | code only, driver lines 186-187 | omitted (F2) |

## Reruns (commands and exit codes)

- `git clone -q <lane> <scratch>/lane && git -C <scratch>/lane checkout -q 59903b26...` -> exit 0; HEAD `59903b2637689739a5b9901956301da72d0effe1`; `merge-base --is-ancestor 43ca0bfb... HEAD` -> exit 0; `status --porcelain | wc -l` -> 0.
- `git diff --stat 43ca0bfb... HEAD -- verifiers/` -> 7 files, 1261+ / 30-, exit 0. Driver, dispatch and census guard are not in the list.
- `git diff --quiet 43ca0bfb... HEAD -- <driver> <dispatch> <guard>` -> exit 0. `git diff --stat 956ee167... HEAD -- <same 3>` -> empty, exit 0.
- `sha256sum` (first 16 hex): driver `e09a402fd16c9311`, dispatch `de9602710a67a3a5`, guard `2f9d8a88b1d3dd85`; all match the seat's digests.
- Driver grep: `get("id") == cid` line 285; `must_fail or holders` line 308; `name in stderr` line 205; `return 0 if killed == 6 else 1` line 344; `timeout=600` line 187; `--self-test` -> no match (exit 1).
- HEAD control (`python3 -B <clone>/verifiers/box_proof_case_deletion.py --rev HEAD --repo <clone>`): `controls killed 2 of 2`, `na killed 1 of 1`, `killed 6 of 6`, exit 0.
- R1 probe-dup (commit 6974e09; second `d04-stem` entry): `killed 6 of 6`, exit 0. Falsifier (fixtures with one `d04-stem`, equal to the HEAD manifest; `verify_dispatch_prompts.py --box-proof --map ... --fixtures <copy>`): `boxes proven 2`, exit 0.
- R2 probe-twin (commit 764f331; `d08-above-state` labels stripped, unlabelled `d08-above-twin` added). Default: exit 1, `FileExistsError` at `shutil.copytree` for `fixtures-d08-missing-state`. `--in-place`: `case d08-missing-state (round_le_latest_dispatched): exit 1 killed`, `killed 6 of 6`, exit 0.
- R3a unknown rev `0000...0`: exit 1, `tarfile.ReadError: empty file`.
- R3b probe-malformed (commit 1bb363c; manifest `{"cases": [`): exit 1, `DriverError: cannot parse ... (Expecting value: line 2 column 1 (char 12))`, raised from `main` line 254.
- R3c = R2 default: exit 1, existing work directory.
- R4 probe-generic (commit 07764df; instrument wrapper prints six conjunct names and exits 1 below nine cases; the original runs otherwise): `killed 6 of 6`, exit 0; `na killed 1 of 1`; `controls killed 0 of 2` (my wrapper omits the control ids; the seat recorded 2 of 2; the headline is unchanged).
- `grep -c box_proof_case_deletion verifiers/floors-registry.json` -> 0, exit 1.
- `python3 -B verifiers/check_sibling_census.py --self-test` -> `self-test: 0 failure(s) over 68 assertions`, exit 0.
- `python3 -B verifiers/check_assertion_floors.py --self-test` -> `0 failure(s) over 150 assertions`, exit 0.
- `python3 -B verifiers/check_overlap_levers.py --self-test` -> `0 failures`, `22 assertions`, exit 0.
- `grep -c F30 verifiers/check_assertion_floors.py` -> 0, exit 1.
- `git apply --check <patch>`: base tree -> exit 0; HEAD clone -> exit 1 (`patch does not apply`).
- `git ls-files .ufo/waves/round-51 | wc -l` -> 0; `git ls-files .ufo/waves/round-50 | wc -l` -> 79.

## Residual risk and verification gaps

- The 17 driver mutants and 28 guard mutants were not rerun. Both claims rest on the committed round-50 tables plus byte identity since 956ee167 (verified above).
- The subprocess timeout path (600 s) and the `survived (absent)` branch were not run.
- The seat's twin falsifier (fixtures minus `d08-above-state`, twin kept, `boxes proven 2`) was not rerun; R2 reproduces the laundering without it.
- The patch was checked only for `git apply --check`. Whether a rebase is trivial is not measured.

## Tools

None installed or updated. python3 3.14.8 and git 2.x were already present.
