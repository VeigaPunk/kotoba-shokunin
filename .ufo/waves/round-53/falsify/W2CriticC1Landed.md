Result: MIXED — the landed C1 holds its bounded statement and all three erratum guards at `c775d682`, and its decoy arms now kill route A as written, but a partial weakening of OC-4/OC-6 passes the counter, guards (a)–(c) and the floors guard, deleting the new arms is caught only by the floors guard, and three committed records carry a 63-character "sha256" plus binding claims no arm witnesses.

Seat: KotobaR53.W2CriticC1Landed (critic, wave 2 falsify). Measured 2026-10-22T20:38–20:56Z.
Sandbox: `/fast/scratch/hyaku/kotoba-r53/w2/W2CriticC1Landed` (clone of the lane, checked out at `c775d6823bfca8f0de8c0874032a954438b38edc`). Each probe is a local commit on its own `landed-*` branch. Nothing was pushed. Lane files were only read.
Counter under attack: `verifiers/check_opencode_repin.py`. `git diff --stat 3bb0a7a3 c775d682 -- verifiers/check_opencode_repin.py verifiers/surfaces-baseline.json verifiers/check_substrate_pins.py` printed nothing (exit 0). Its sha256 at `c775d682` is `9abcaa12…ca4fbd`, the same value CriticC1Sizing recorded, so the counter is still frozen.
Substrate at 2026-10-22T20:38:19Z: opencode `/home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe`, 214522032 bytes, mtime 2026-10-22 14:50:30 −0300, sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`, `package.json` `"version": "1.19.4"`. omp `~/.local/bin/omp` sha256 `85d9daf3a05fc76e8cd425ae1904eb576af8d21cc85fcf4690742626e07ccfa4`. Neither binary has been rebuilt since the plan.
No tools were installed or updated. No paid model calls were made, and no client was run.

## 1. Controls: the landed statement and the erratum guards

| Check | Command (sandbox) | Observed | Exit | Verdict |
|---|---|---|---|---|
| Counter at the C2 commit | `python3 -B verifiers/check_opencode_repin.py --rev 55973a20 --repo .` | `surfaces pass 6 of 7 (opencode_extract FAIL); pins OK 2/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 133 assertions` | 1 | matches the brief |
| Counter at the C1 commit | same, `--rev 6dd31164` | `surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 155 assertions` | 0 | matches the brief |
| Counter at the tip | same, `--rev c775d682` | identical to the C1 line; line 2 `… sha256 538fcb1b…312a7 bytes 214522032` | 0 | **HOLDS** (erratum 1 statement) |
| Guard (b): independent dump | `strings -n 4 <binary> > scratch/oc-host.strings` (GNU strings 2.47), then `verify_surfaces.py --json --opencode-strings scratch/oc-host.strings` | dump: 993160 lines, 74137746 bytes, sha256 `2d72d83f8c90b15c4ba12037c305a838fefe03401e0762c90efdfe04f5a4bd98`, the same as the cited dump. Gate: `pass 7 fail 0`, `opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)` | 0 | **HOLDS** |
| Guard (c): rows | `verify_surfaces.py --json` (default binaries) | `exit_code 0`, 7 rows, each of the 7 check ids exactly once, detail `9/9 … from 7/7 rules` | 0 | **HOLDS** |
| Guard (a): scope | `scratch/guard_a.py . c775d682` (top-level AST comparison against `3bb0a7a3`), plus a line-level read of `git diff 3bb0a7a3 c775d682 -- verifiers/verify_surfaces.py verifiers/check_substrate_pins.py` | changed: `extract_opencode_classes`, `self_test`; added: `OC_READ_*_RE`, `OC_V2_*_RE`, the two `opencode_*_matches` helpers; removed: `OC_READ_HOOK_FN`, `OC_READ_TOOL_FN`. Pin script identical. `load_dump`, `DEFAULT_BINARIES`, `substrate_identity`, `check_opencode_extract`, `main` and `emit_json` byte-identical. The only diff lines naming OC-1..OC-3 or OC-5 are comments (`scope.diff` lines 11, 15, 30) | 0 | **HOLDS** |

Every non-comment line of `verifiers/fixtures/surfaces/strings-opencode-1.19.4-anchors.txt` occurs in my dump (`grep -cF`: 1 hit each, except `Instructions from: ${L}` with 2, `<system-reminder>` with 13 and `</system-reminder>` with 8). The fixture's claim that its lines are dump substrings **HOLDS**.

## 2. Routes A–F re-run on the landed rule shape

Each route is the CriticC1Sizing patch, or a stated variant, applied on top of `c775d682`. "Stale" variants keep the landed re-pin and fixtures but restore the pre-C1 rules (`git checkout 55973a20 -- verifiers/verify_surfaces.py`), which is the un-re-derived launder each route was built to hide. The runner is `scratch/run_route.sh`, and the full log is `scratch/routes.log`. Columns: counter line 1 and exit; guard (a) exit (names outside the OC-4/OC-6 allowance); guard (b) gate exit on my dump; guard (c) verdict.

| Route (branch, commit) | Counter | Self-test | (a) | (b) | (c) | Caught by |
|---|---|---|---|---|---|---|
| A: OC-4 is `<system-reminder>` presence, OC-6 is `system-context-builtins` presence (`landed-A-literal` `cfb44e1`) | `pass 7 of 7 … self-test 6 failure(s) over 155`, **exit 1** | 6 failures, all decoy arms (`decoy-oc4/oc6: exit 1`, `FAIL opencode_extract`, `only OC-n unmatched`) | 0 | 0 | PASS | **self-test arms** (through the counter's T term) |
| A2: route A plus the `(oc-1194)` block deleted (`landed-A2-noarms` `b467b86`) | `pass 7 of 7 (opencode_extract PASS); pins OK 3/3; … kept 9 of 9; self-test 0 failure(s) over 133 assertions`, **exit 0** | 0/133 | 0 | 0 | PASS | **nothing in counter or (a)–(c)**. Only the no-harm floors guard catches it: `check_assertion_floors.py --repo .` → `FAIL surfaces observed=133 floor=155`, exit 1 |
| A3: OC-1 is `'"CONTEXT.md"' in dump` (`landed-A3-oc1` `d1fa300`) | target line, 0/155, **exit 0** | 0/155 | 0 at function level; caught at line level | 0 | PASS | **guard (a) only, read line by line**: the diff shows `-    rule("OC-1", owns, m is not None and bool(names) and gated,` / `+    rule("OC-1", owns, '"CONTEXT.md"' in dump,`. A function-level automation misses it, because all seven conditions live in `extract_opencode_classes` |
| A4: partial weakening. OC-4 = `OC_READ_CALL_RE` anywhere; OC-6 = instruction-context instance in the builtins deps, or the 1.19.3 registration regex (`landed-A4-partial` `a44ef5d`, +6/−2) | target line, `0 failure(s) over 155 assertions`, **exit 0** | 0/155 | 0 | 0 | PASS | **nothing**. Floors also pass (`PASS surfaces observed=155 floor=155`, exit 0) |
| B: host-scoped retirement inside the gate (`landed-B-retire` `fbdac67`) | `pass 6 of 7 (opencode_extract FAIL)`, exit 1 | 0/155 | 1 (`check_opencode_extract`, `main`, `HOST_SCOPED_RETIRED`) | 0 | FAIL (`extracted opencode class(es) undeclared in baseline`) | counter, by accident: the honest rules now emit the retired ids |
| B-stale (`landed-B-stale` `d613852`) | target line, 0/133, **exit 0** | 0/133 | 1 | 1 | FAIL (`7/7 declared class(es) from 5/5 rules`) | **guards (a), (b) and (c)** |
| C: `load_dump` returns `strings-opencode-clean.txt` (`landed-C-fixture` `64650ec`) | target line, 0/155, **exit 0**; line 2 is the host binary, byte-identical to the honest line | 0/155 | 1 (`load_dump`) | 0 | PASS | **guard (a) only**. It is harmless here only because the landed rules are honest |
| C-stale (`landed-C-stale` `d84043e`) | target line, 0/133, **exit 0**, line 2 the host binary | 0/133 | 1 | 1 | PASS | **guards (a) and (b)**; (c) misses it |
| D: injected PASS row (`landed-D-row` `6e45294`) | `surfaces pass 8 of 7`, exit 1 | 0/155 | 1 (`main`) | 0 | FAIL | counter, by accident (8 PASS rows) |
| D-stale (`landed-D-stale` `598448a`) | target line, 0/133, **exit 0** | 0/133 | 1 | 1 | FAIL | **guards (a), (b) and (c)** |
| E: OC-4 class re-kinded to `prompt-text` in the baseline (`landed-E-rekind` `638c9ac`) | `pass 6 of 7 … kept 8 of 9`, exit 1 | 0/155 | 0 | 1 | FAIL | counter (K term) |
| F: `DEFAULT_BINARIES["opencode"]` is the clean fixture (`landed-F-defaultpath` `d56c80b`) | target line, 0/155, **exit 0**; line 2 `/tmp/oc-repin-…/strings-opencode-clean.txt sha256 e2a169bf… bytes 2259` | 0/155 | 1 (`DEFAULT_BINARIES`) | 0 | PASS | **guard (a) only**. Line 2 is visible but is not an exit term |
| Control: stale rules, no launder (`landed-S0-stale` `badc989`) | `pass 6 of 7 (opencode_extract FAIL)`, exit 1 | 0/133 | 0 | 1 | FAIL | counter |

Summary of the three buckets the assignment asks for:
- **Caught by the self-test arms:** route A as written, and only A. The decoy arms do what the sizing critic asked for (its correction 4).
- **Caught only by guards (a)–(c):** C and F (guard (a) alone), A3 (guard (a), only when read line by line), B-stale and D-stale (all three guards), and C-stale ((a) and (b)). B, D and E are caught by the counter on the landed tip, but B and D only because the patch collides with honest rules.
- **Caught by nothing:** A4. A2 is caught by nothing in the counter or (a)–(c); only the separate floors no-harm guard catches it, and only since `c775d682` registered surfaces at 155. The counter's own floor is frozen at 129, below the 133 that remains after the 22 new assertions are deleted.

## 3. Findings

### F1. A4: partial weakening of OC-4/OC-6 passes everything (BREAKS the "decoy arms" reading; MEDIUM, calibration)

Each decoy breaks exactly one edge. `decoy-oc4` renames `r.resolve(` to `r.load(` (fixture lines 16–20). `decoy-oc6` drops `iD` from the `system-context-builtins` deps (line 34). The two arms therefore witness one edge per rule. The landed OC-4 code also requires the resolver export (`});return X.of({…resolve:<method>`), the same module, and the same-result `<system-reminder>` delivery (`verifiers/verify_surfaces.py:673-708`). The landed OC-6 code also requires the key, the `ia(m(function*` layer definition, `ki({key:`, `InstructionContext.observe` and the `targets:["AGENTS.md"]` walk (`:711-746`). Removing all of those requirements (A4) leaves the self-test at `0 failure(s) over 155 assertions`, and the counter, guards (a)–(c) and the floors guard all pass. Under A4, OC-6 still owns `opencode:instruction-context/AGENTS.md` without checking for any AGENTS.md text.
- Plan honesty: the counter not seeing this is disclosed (`plans/round-53.md:35-36`; erratum 2). The defect is in the records (F3): they describe bindings that no arm and no guard verifies.
- Smallest safe correction: either add one literal-preserving decoy per unwitnessed edge, each of which must FAIL (OC-4: export renamed off `resolve:`; delivery mapping a different variable. OC-6: `targets:` without `"AGENTS.md"`; key not used before observe; layer defined by a different shape), or bound the census sentence to "the rule code binds …; the self-test witnesses only the call edge (OC-4) and the builtins dependency (OC-6)".

### F2. A2: guard (a) permits deleting the new arms (LOW–MEDIUM)

Erratum guard (a) allows changes to "their comments and self-test arms" (`plans/round-53.md:118`) and does not say "added, none removed". Deleting the 22 `(oc-1194)` assertions passes the counter (133 ≥ 129), guard (a), guard (b) and guard (c). The no-harm floors guard catches it (`FAIL surfaces observed=133 floor=155`, exit 1). That guard is not one of the three C1 guards, and at the C1 commit `6dd31164`, before the floors commit, the registered floor was still 129.
- Smallest safe correction: read guard (a) as "self-test arms added; none removed or weakened", or name `check_assertion_floors.py` with surfaces ≥ 155 as part of the C1 verdict.

### F3. Records state more than the counter and guards verify (BREAKS; calibration)

| Record | Clause | What verifies it | Verdict |
|---|---|---|---|
| `verifiers/baseline.json:11` `opencode_round53_note`; census note `corpus/knowledge/instruction-surface-census-round13.md:550`; anchors fixture header `strings-opencode-1.19.4-anchors.txt:1` | binary "sha256 `538fcb1b6408c8d460882acee19f7ff5b3a3eb3383c0633c4f06170857312a7`" | nothing; no instrument reads notes or comments | **BREAKS (MEDIUM, false provenance)**. The string is 63 hex characters (`rg -o '[0-9a-f]{60,66}' verifiers/baseline.json` → `1 63 538fcb1b6408c8d460882ace…`), with one `2` dropped after `c8d46088`. No file can have this hash. The real hash is `…c8d4608822ace…` (64 characters; `sha256sum` above; the pin field `opencode_binary_sha256` at `:10` is correct, so `pins OK 3/3` is unaffected). The origin is `.ufo/waves/round-53/build/ExecOcRederive.md:28,38,58`, which presents the 63-character value as "printed" `sha256sum` output and as the counter's "exact final output". Both tools print 64 characters, so the seat's quoted output is not verbatim |
| Census note `:551-552` and baseline note | dump `/fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings` | the sha only | **LOW**. The path does not exist (`ls` → `No such file or directory`); ExecOcRederive item 13 deleted it before committing (`ExecOcRederive.md:49`). The dump sha256 is reproducible: my `strings -n 4` (GNU 2.47) gives the same `2d72d83f…bd98` |
| Census note OC-6 bullet | "dump lines 597823 and 597828: `Wr.make("core/instructions")` replaces …"; anchors fixture `:27` "(dump line 597823)" for key, layer and key use | nothing | **LOW**. `Wr.make("core/instructions")`, `eD=ia(m(function*` and `ki({key:UE,` are on dump line **597822**. Observe, targets and the instruction-context registration are on 597823, and builtins is on 597828 (`grep -nF` on my dump). The OC-4 lines (598311-598312, 598484, 598489, 598496-598499) are correct |
| Census note OC-4 bullet | "The 1.19.4 rule now binds the export, caller edge and same-result delivery rather than counting these literals independently." | code reading only; arms witness the caller edge alone (F1) | **states more than verified (MEDIUM)**. True of the code, but no arm, guard or counter term fails when the export or delivery binding is removed |
| Census note OC-6 bullet; baseline note "OC-6 follows Wr.make core/instructions through the instruction-context layer dependency" | key → observe → walk → layer → builtins chain | the arm witnesses only the builtins dependency edge (F1) | **states more than verified (MEDIUM)**, as above |
| Commit `6dd31164` subject | "(alias-agnostic call edge, decoy arms)" | probe: renamed copies of the anchors fixture | **partly true (LOW)**. OC-4 passes with `l(`→`q(`, `O1.of`→`Z9.of`, `r.resolve`→`w.resolve` (`scratch/alias-oc4.txt`, PASS 9/9, exit 0). OC-6 fails closed when any single alias is renamed: `ia(m(`→`xa(n(`, `ki(`→`Pi(`, or `Re(`→`Qe(` (`scratch/alias-oc6*.txt`, each `FAIL … OC-6`, exit 1), because `OC_V2_LAYER_DEF_RE`, the `ki\(\{key:` search and `(?:Re|i)\(` hard-code minifier aliases (`verify_surfaces.py:634-636,724-735`). A minifier rename broke OC-4/OC-6 this round (S051: Bun 1.3.14→1.4.4), and the next one will break OC-6 again. That failure is visible (exit 1), so it is a durability cost to freshness, not a false pass |
| `verify_surfaces.py:572-576` LIMITS comment | "whole-dump anchors remain for OC-1..OC-3 and OC-5 … OC-6 binds its observed layer to the `system-context-builtins` dependency" | code reading | **LOW**. The 1.19.3 fallback (`:748-755`) accepts OC-6 by whole-dump presence of `Key.make("core/instructions")` plus the observe, targets and old-registration regexes, with no window or binding. The comment leaves OC-6 out of the whole-dump list. The 1.19.4 binary cannot take this path (`Key.make("core/instructions")` occurs 0 times in it, per CriticC1Sizing), so this is wording only |
| Census note | "The nine opencode class ids, kinds and verdicts remain unchanged." | counter K (baseline file) and guard (c) (gate enforces 9/9 from 7/7) | **HOLDS** |
| Census note | append-only | `git diff --numstat 55973a20 6dd31164 -- corpus/knowledge/instruction-surface-census-round13.md` → `31 0` | **HOLDS** |
| Baseline note and census note | "opencode-ai 1.19.4" | not printed by the counter or any guard; `package.json` read directly → `"version": "1.19.4"` | context only, consistent with erratum 1 |
| Census S051 provenance paragraph | "rebuild of unchanged source" | outside this seat (W2ReopenS051) | not checked here |

### F4. A3: guard (a) must be applied line by line (LOW, procedure)

All seven rule conditions live in one function, `extract_opencode_classes`. A guard (a) automated at function or definition level passes an OC-1 weakening (`scratch/guard_a.py` exit 0 on `landed-A3-oc1`). The erratum's wording ("changes only the OC-4/OC-6 constants and conditions") is satisfied only by a line-level read, which does catch it. The closure should run guard (a) on diff hunks, not on changed definitions.

### F5. Counter cosmetics (LOW; the counter is frozen)

On route D the counter printed `surfaces pass 8 of 7`. P counts PASS rows without a cap and still exits 1. This is not fixable this round, and is noted for the next counter.

## 4. Impacted axes

- Freshness: the claim holds on the host binary (guard (b) independent), but OC-6 is bound to three minifier aliases, so it will need re-deriving at the next Bun rebuild.
- Calibration: the 63-character hash in three committed records and a seat report, and the binding sentences that state more than any arm verifies (F1, F3).
- Consistency: none found. Guard (a) holds, there is no second authority for the class set, and the pin field is correct.

## 5. Smallest safe corrections, in order

1. Append-only erratum lines in `verifiers/baseline.json` (a new note key) and the census note giving the 64-character sha256 `538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7`. Fix the anchors-fixture header comment, which is not an anchor. Mark the dump path as deleted, reproducible with `strings -n 4` (GNU 2.47) → sha256 `2d72d83f…`. Correct 597823 to 597822 for the key, layer and key-use lines.
2. Bound the census binding sentences to what the arms witness, or add the per-edge decoys listed in F1.
3. In the closure, read guard (a) line by line and with "arms added, none removed", or cite `check_assertion_floors.py` (surfaces 155) alongside guards (a)–(c).
4. In the round record, scope "alias-agnostic" to OC-4.

None of these touches the frozen counter or its cases.

## Commands (all in the sandbox unless a lane path is shown)

- `sha256sum <opencode binary>`; `sha256sum ~/.local/bin/omp`; `strings -n 4 <binary> > scratch/oc-host.strings; sha256sum …; wc -l …; wc -c …` → exit 0 (values above). `ls /fast/scratch/hyaku/kotoba-r53/ExecOcRederive/oc-1.19.4.strings` → exit 2, `No such file or directory`.
- `python3 -B verifiers/check_opencode_repin.py --rev {55973a20,6dd31164,c775d682} --repo .` → exit 1, 0, 0 (lines in § 1).
- `scratch/run_route.sh <branch>` for 14 branches → `scratch/routes.log` (lines quoted in § 2).
- `python3 -B scratch/tree-A/verifiers/verify_surfaces.py --self-test --repo scratch/tree-A` → `6 failure(s) over 155 assertions` (the 6 decoy assertions).
- `python3 -B verifiers/check_assertion_floors.py --repo .` in `scratch/tree-A2` → exit 1 (`FAIL surfaces observed=133 floor=155`); in `scratch/tree-A4` → exit 0 (`PASS surfaces observed=155 floor=155`).
- `python3 -B scratch/tree-c775/verifiers/verify_surfaces.py --repo scratch/tree-c775 --opencode-strings <file> --check surfaces.opencode_extract` on the anchors fixture, `alias-oc4.txt`, `alias-oc6.txt`, `alias-oc6-ki.txt` and `alias-oc6-re.txt` → exit 0, 0, 1, 1, 1.
- `grep -nF` on my dump for each OC-4/OC-6 anchor (line numbers in F3); `grep -cF` for each anchors-fixture line (§ 1).
- Lane, read-only: `git show --stat 6dd31164 c775d682 aeed0890`; `git diff --stat 3bb0a7a3 c775d682 -- <counter, baseline, pin script>` (empty); `git diff --numstat 55973a20 6dd31164 -- <census>` → `31 0`.
