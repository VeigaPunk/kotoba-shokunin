Result: BREAKS — the frozen C1 counter prints the exact target line and exits 0 on four laundering patches (rule weakened to a generic token, a class retired inside the gate, the gate reading a 1.19.3-shaped fixture, and an injected PASS row); the plan's "does not measure" sentence covers only the first, and two statement clauses (omp, version) map to nothing printed.

Seat: KotobaR53.CriticC1Sizing (critic, wave 1 build). Measured 2026-10-22T20:00–20:11Z.
Sandbox: `/fast/scratch/hyaku/kotoba-r53/CriticC1Sizing` (clone of the lane, checked out at plan commit
`3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`; every probe is a local commit on its own branch; nothing pushed).
Lane files read only. Counter under attack: `verifiers/check_opencode_repin.py`, sha256
`9abcaa12fb41563a44517fdbcac773fb54aebb79f4334d317277b6e783ca4fbd` in the lane working tree and at
`3bb0a7a3` (identical, so frozen). Plan read: `plans/round-53.md` sha256 `40534b3d…d980c8`.
Substrate observed: opencode `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`,
sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, 214522032 bytes, mtime
2026-10-22T17:50:30Z, `package.json` `"version": "1.19.4"`; omp `~/.local/bin/omp --version` → `omp/18.12.6`,
sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`.
No tools installed or updated. No paid model call; no client run beyond `omp --version`.

## Control runs (the counter works as written)

Every run below is `python3 -B verifiers/check_opencode_repin.py --rev <rev> --repo .` inside the clone.

| Revision | Change | Line 1 | Exit |
|---|---|---|---|
| `3bb0a7a3` (plan) | none | `surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions` | 1 |
| `737dd7d` pin-only | `verifiers/baseline.json` `opencode_binary_sha256` → `538fcb1b…` | `surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 3/3; … kept 9 of 9; self-test 0 failure(s) over 129 assertions` | 1 |

The plan-commit run reproduces the plan's before line byte for byte. Both runs print substrate line 2 as the host
binary above.

The 1.19.4 anchors only changed callee names: `l("Instruction.resolve")(function*(C,y,b){…` (dump line 598311),
`A=l("ReadTool.execute")(function*(T,F){…` (598484), `UE=Wr.make("core/instructions")` (597822). The
1.19.3 constants are `fn("Instruction.resolve")`, `fn("ReadTool.execute")` and `Key.make("core/instructions")`
(`verifiers/verify_surfaces.py:628,640-641`), and each occurs 0 times in `strings -n 4` of the 1.19.4 binary.
The bare literals `Instruction.resolve`, `ReadTool.execute` and `core/instructions` occur once each;
`<system-reminder>` occurs 13 times; `targets:["AGENTS.md"]`, `InstructionContext.observe` and
`system-context-builtins` once each. So an honest re-derivation and a weakening both reach PASS, and the
printed line is the same for both.

## Laundering routes, each run on the frozen counter

All four patches sit on top of the pin-only commit `737dd7d`. Line 2 is the substrate line.

### A — rules weakened to literal presence (branch `launder-A-literal`, commit `5be6434`, 6-line diff)

`verify_surfaces.py`: `read_hook = OC_READ_HOOK_TOKEN in dump` (OC-4 becomes the generic `<system-reminder>`
token, which has 13 hits); `v2 = OC_V2_REGISTRATION in dump` (OC-6 becomes the string `system-context-builtins`,
the name of a different layer).
Counter output: `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`, line 2 the host binary `538fcb1b…`, **exit 0**.
- Caught by the counter: no. The self-test stays at 0 failures over 129 assertions. The drop fixtures
  `fixtures/surfaces/strings-opencode-drop-oc4.txt` and `-drop-oc6.txt` delete every anchor of their rule:
  `<system-reminder>`, `Instruction.resolve` and `fn("ReadTool.execute")` occur 0 times in drop-oc4, and
  `system-context-builtins` occurs 0 times in drop-oc6. So the arms at `verify_surfaces.py:1452-1464` kill
  "every anchor gone" but not "rule reduced to one generic token".
- Plan honesty: covered. The "does not measure" sentence at `plans/round-53.md:35-36` excludes whether OC-4/OC-6
  match "the loader code they name rather than an unrelated string". That sentence names only OC-4 and OC-6,
  though. The counter has no per-rule term, so a weakening of OC-1, OC-2, OC-3a, OC-3b or OC-5 in the same change
  is equally invisible to it [INFERENCE from the code read; not run].
- Severity: MEDIUM. This is a disclosed tradeoff. The residual defect is that the exclusion is scoped to two rules
  when the counter cannot see any of the seven.

### B — class retired inside the gate, baseline untouched (branch `launder-B-shadow-retire`, commit `6ca013a`, +16/−3)

This patch copies the file's own "host-scoped retirement" idiom (`verify_surfaces.py:571`). It adds
`HOST_SCOPED_RETIRED = {"538fcb1b…": ("opencode:read-hook/instructions", "opencode:instruction-context/AGENTS.md")}`.
`check_opencode_extract` then drops those ids from `declared` and drops their rules from `report`, but only when
`main` hashes the default binary to that sha. `verifiers/surfaces-baseline.json` is byte-identical to base.
Counter output: `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`, line 2 the host binary, **exit 0**.
The gate's own detail line gives it away, but the counter never prints that line:
`PASS surfaces.opencode_extract: opencode extraction 7/7 declared class(es) from 5/5 rules (OC-1, OC-2, OC-3a, OC-3b, OC-5)` (gate exit 0).
- Caught by the counter: no. Term K reads only `surfaces-baseline.json` (`check_opencode_repin.py:110-111`), not
  the set the gate actually enforces. The self-test arms pass because they feed dumps through `--opencode-strings`,
  which leaves no host sha to match.
- Plan honesty: contradicted. `plans/round-53.md:31-32` says "retiring or re-kinding a class to clear the gate is
  not kept". That holds only when the retirement is written into the baseline file. Probe E below shows a
  retirement in the baseline is caught; a retirement in the gate is not. This is a Q31 defect (counter prose names
  a check the code does not run) and a Q26 defect (`kept 9 of 9` reads as "no class retired"). A variant of the
  same route (a second authority: the gate's default `--baseline` path pointed at a shadow baseline file) is
  [INFERENCE] equally uncaught, by the same code read.
- Severity: HIGH. It is a hidden regression (two governed classes stop being enforced) with a false `kept 9 of 9`.

### C — gate reads a committed fixture but reports the host binary (branch `launder-C-fixture`, commit `e834bd5`, +3)

`load_dump`: when no `--opencode-strings` is given and the harness is opencode, it returns
`fixtures/surfaces/strings-opencode-clean.txt` (1.19.3-shaped, 1957 bytes). `substrate_identity` is
untouched, so it still hashes the host binary. No rule is changed.
Counter output: `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`
and `substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032`, **exit 0**.
Both lines are byte-identical to what an honest re-derivation would print, and no 1.19.4 byte is matched by any rule.
- Caught by the counter: no. The substrate line is whatever the revision's gate writes into `sj["substrate"]`
  (`check_opencode_repin.py:122,130`). The counter never hashes a binary itself, and never checks that the gate
  read the binary it reports.
- Plan honesty: contradicted. `plans/round-53.md:29-30` says the counter runs the gate "against the installed
  binaries", and `:33-34` says "The second output line names the measured opencode binary". The counter
  docstring (`check_opencode_repin.py:9`) says the extraction is "re-derived from the 1.19.4 bytes". The code
  checks none of the three. Both Q31 and Q26 apply: the clause "measured on the host opencode 1.19.4
  (sha256 538fcb1b…)" rests on the measured revision's own report.
- Severity: HIGH. This is false provenance with no visible trace in the output.

### D — injected PASS row (branch `launder-D-row`, commit `dbf51fe`, +2)

In `--json` mode, `main` prepends `{"id": "surfaces.opencode_extract", "status": "PASS"}` to the results. The real
FAIL row stays.
Counter output: `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 129 assertions`, line 2 the host binary, **exit 0**.
The gate's own JSON for the same revision: `rows 8 pass 7 fail 1 gate exit_code 1`.
- Caught by the counter: no. P is a count of PASS rows (`check_opencode_repin.py:101`) and `oc` is the first
  matching id (`:102`). The counter never checks the row count, id uniqueness, the gate's `fail` field or its
  `exit_code`. The same family applies to T: F and A are parsed from whatever text the revision's
  `--self-test` prints (`:113-121`), so a self-test that prints `0 failure(s) over 129 assertions` would pass
  [INFERENCE from the code read; not run].
- Plan honesty: not covered. "Each statement is exactly what its counter prints" holds, but `7 of 7` here means
  "7 PASS rows", not "the 7 checks pass".
- Severity: HIGH as a counter defect. A one-glance diff review catches it, so it is less dangerous than B or C.

### Routes that are caught or visible

- **E — class moved out of the opencode harness label** (branch `launder-E-relabel`, commit `08d8344`, on top of A):
  the OC-4 row is relabelled `omp:read-hook/instructions` with harness `omp`. Output:
  `surfaces pass 5 of 7 (opencode_extract FAIL); pins OK 3/3; opencode classes kept 8 of 9; …`, exit 1.
  **Caught** by K. Re-kinding or re-verdicting in the baseline is caught by the same tuple comparison
  (`check_opencode_repin.py:76-77,111`) [INFERENCE from the code read; not run].
- **F — the gate's default opencode path pointed at a fixture** (branch `launder-F-defaultpath`, commit `7a0adf9`):
  `DEFAULT_BINARIES["opencode"] = str(FIXTURES / "strings-opencode-clean.txt")`. Line 1 is the target line,
  **exit 0**. Line 2 gives it away:
  `substrate opencode: /tmp/oc-repin-s3ymwfgu/verifiers/fixtures/surfaces/strings-opencode-clean.txt sha256 b6e87960… bytes 1957`.
  The counter does not catch it, but a reader comparing line 2 with the statement's sha would. The pin script
  still hashed the host binary (its own `DEFAULT_BINARIES`, `check_substrate_pins.py:65-66`), so `pins OK 3/3`
  cannot tell what the gate read. Severity: MEDIUM. The trace is visible, but it is not an exit term; route C is
  the same attack without the trace.
- **G — gate cannot find its binary** (branch `probe-G-missing`, commit `3d23f27`, simulating an npx cache move): output
  `surfaces pass 0 of 7 (opencode_extract ABSENT); pins OK 3/3; …` and `substrate opencode: None sha256 None bytes None`, **exit 1**.
  The docstring reserves exit 2 for "could not evaluate" (`check_opencode_repin.py:36`). The gate emitted
  `exit_code` 2 with empty checks, and the counter scored that as a claim failure. Severity: LOW.

## Q26 clause map for the C1 statement (`plans/round-53.md:22-26`)

| Clause | Turned on by | Holds? |
|---|---|---|
| `surfaces pass 7 of 7 (opencode_extract PASS)` | line 1 and the exit term | counts PASS rows, not distinct checks (route D) |
| `pins OK 3/3` | line 1 and the exit term | pins and pin script are both the revision's; a true host-hash check only while `check_substrate_pins.py` is unmodified |
| `opencode classes kept 9 of 9` | line 1 and the exit term | reads the baseline file, not the gate's enforced set (route B) |
| `self-test 0 failure(s)` | line 1 and the exit term | the statement drops `over <A> assertions`, yet `A >= 129` is an exit term; text is self-reported (route D family) |
| measured on host opencode **1.19.4** | nothing | the version is printed nowhere; only the sha is |
| (sha256 `538fcb1b…`) | line 2, which is not an exit term | self-reported by the measured revision (route C); a mismatch still exits 0 (route F) |
| and omp 18.12.6 (sha256 `85d9daf3…`) | nothing | the counter prints no omp line. `pins OK 3/3` only says the host omp matches whatever the revision pins, and the change may re-pin omp |

Two clauses are turned on by nothing the counter prints (the omp clause and the 1.19.4 version), and one is
printed but self-reported. Under Q26 they must be dropped or bounded. The plan's line-20 assertion "each
statement is exactly what its counter prints" is also loose: the statement omits the `opencode re-pin: ` prefix
and the `over <A> assertions` tail (LOW).

## Is the substrate line enough for a closure to tell a host rebuild from a regression?

Partly, for opencode only, and only if the revision's gate is honest.
- For opencode: a changed sha on line 2 together with `pins OK 2/3` reads as a rebuild, and the same sha with a
  FAIL reads as a regression. This holds only while the gate and pin script are base-equivalent. Route C forges
  line 2 and route F breaks the link between line 2 and what the gate read.
- For omp: nothing. P includes `surfaces.literal_present` and `surfaces.no_uncovered_class`, which read the omp
  dump (`verify_surfaces.py:1654-1657`), but the counter prints no omp substrate. `pins OK k/3` does not say which
  pin drifted. An omp rebuild that flips an omp check is indistinguishable from a regression on the printed lines.
- Version: the version is not printed, so the 1.19.4↔`538fcb1b…` link lives only in plan prose.
- Rebuild exposure is high. `~/.local/bin/opencode` runs `npx --yes --prefer-online --package opencode-ai -- true`
  before every launch, and the cache `package.json` reads `"opencode-ai":"^1.19.4"`. Any operator `opencode`
  invocation can replace the binary in place at the same path [INFERENCE from the wrapper text; not exercised].
  A cache-directory move instead yields route G's `None` plus exit 1, which is conflated with failure.
- Severity: MEDIUM.

## Impacted axes

- Freshness: the claimed axis. Routes B, C and D let `7 of 7` stand with no 1.19.4 re-derivation.
- Calibration: the statement and the counter prose say more than the code measures (Q26, Q31).
- Consistency: route B creates a second authority for the declared class set.

## Smallest safe corrections (the counter is frozen, so these are statement and closure-side fixes)

1. Bound the statement (Q26). Drop "and omp 18.12.6 (sha256 85d9daf3…)", or move it to a cited guard that prints
   the omp sha. Replace "measured on the host opencode 1.19.4" with "line 2 prints the sha256 the revision's gate
   reports". Fix the counter prose (Q31): strike "against the installed binaries", "names the measured opencode
   binary" and "retiring … is not kept" as counter properties. Say instead that K compares
   `surfaces-baseline.json` only.
2. Extend the "does not measure" sentence: the counter trusts the measured revision's gate for which dump it
   reads, which classes it enforces, which rows it emits and what its self-test prints. It covers no rule
   besides OC-4/OC-6 either.
3. Add a cited closure guard whose exit code flips on B, C, D and F. It has three parts, all mechanical and all
   killing the four patches above:
   - **Diff gate.** `git diff e78dff66 <rev> -- verifiers/verify_surfaces.py verifiers/check_substrate_pins.py`
     may touch only the OC-4/OC-6 anchor constants and conditions (lines 622-642, 692-711), their GENERATION
     NOTE comment, and self-test arms. `load_dump`, `dump_via_strings`, `DEFAULT_BINARIES`, `substrate_identity`,
     `check_opencode_extract`, `main` and `emit_json` must stay byte-identical to base, and the pin script too.
     This kills B, C, D and F.
   - **Independent dump.** Re-run the revision's gate with `--opencode-strings` set to the closure's own
     `strings -n 4` of the host binary, after an independent `sha256sum` equal to `538fcb1b…`. This kills C.
   - **Detail and row check.** Require gate JSON `exit_code == 0`, exactly the 7 `CHECK_IDS` once each, and the
     opencode_extract detail `9/9 declared class(es) from 7/7 rules`. This kills B and D.
4. For the executor (route A, which the plan routes to wave 2): add one decoy arm per re-derived rule. Each
   fixture keeps the bare literals (`Instruction.resolve`, `ReadTool.execute`, `<system-reminder>`,
   `core/instructions`, `system-context-builtins`) but breaks the call shape (`<callee>("…")(function*` or
   `<callee>.make("core/instructions")`), and the arm must FAIL. The current all-anchors-deleted drop
   fixtures cannot tell the shape-bound rule from patch A.

Defect versus tradeoff: route A is a disclosed tradeoff, acceptable as worded once item 2 widens it beyond
OC-4/OC-6. Routes B, C and D are fixable defects in the claim text and the closure, not in the frozen counter. A
judge should not read `exit 0` alone as C1 closed: without the item-3 guard, the printed line cannot tell an
honest re-derivation from B, C or D.
