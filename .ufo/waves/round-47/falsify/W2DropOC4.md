verdict: BROKEN — OC-4 read-hook gate (`verifiers/verify_surfaces.py:479-483`, rule `OC-4`) mutation-probed on the real opencode-1.19.3 dump at 7ad7fad: 9 of 19 runs correct (control included), 4 false-red on label respellings, 6 presence-only survivors

Lane: KotobaR47-2.W2DropOC4-2. Tip 7ad7fadfc09354b74fb66605dfb0c1182c115a2f, detached in the scratch clone `/fast/scratch/kotoba-r47/w2/W2DropOC4/kotoba-shokunin`. Production is untouched; nothing committed.
Inputs are the frozen dumps, sha256-verified against SHA256SUMS: `opencode-1.19.3.strings` = f4d8f34a…, `omp-18.12.5.strings` = 33df0aef….
Line refs `verify_surfaces.py:N` are at 7ad7fad. `dump:N` is `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` line N.

## Bottom line

OC-4 is three whole-dump substring tests (`verify_surfaces.py:480-481`). It is red when a label is deleted or corrupted, which is correct. It is also red when a label is respelled without changing behaviour, which is a false red. It stays green when the read-tool channel is severed: the call edge is cut, the delivery wrapper is removed, the walk loop is disabled, or a stale copy of a label exists.

Across 19 runs (control plus 18 mutants): 9 correct (control included), 4 false reds, and 6 survivors. Of the 18 mutants, 8 are correct, 4 are false reds, and 6 survive. The survivors are the finding. The gate does not witness the channel it names, and the token it relies on is generic.

## Result matrix (real dump, tip verifier, all checks, `--omp-strings` frozen)

Correct exit is 0 when the mutant preserves behaviour and 1 when it breaks the read-hook channel. Mutant files are in `/fast/scratch/kotoba-r47/w2/W2DropOC4/mut/<name>.strings`.

| name | mutation (dump line / byte) | correct | exit | verdict |
|---|---|---|---|---|
| M00-control | no edits | 0 | 0 | OK |
| M01-instr-delete | delete `fn("Instruction.resolve")` (:443995 / 10895197) | 1 | 1 | OK |
| M02-instr-corrupt | `fn("Instruction.resolv")` | 1 | 1 | OK |
| M03-instr-label-rename | `fn("Instruction.resolveNearest")` | 0 | 1 | FALSE-RED |
| M04-instr-quote-respell | `fn('Instruction.resolve')` | 0 | 1 | FALSE-RED |
| M05-instr-live-gone-stale-copy | live label renamed to `…resolveX`; `fn("Instruction.resolve")` appended at EOF (:750050) | 1 | 0 | SURVIVOR |
| M06-read-delete | delete `fn("ReadTool.execute")` (:444228 / 10946276) | 1 | 1 | OK |
| M07-read-corrupt | `fn("ReadTool.execut")` | 1 | 1 | OK |
| M08-read-label-rename | `fn("ReadTool.run")` | 0 | 1 | FALSE-RED |
| M09-read-quote-respell | `fn('ReadTool.execute')` | 0 | 1 | FALSE-RED |
| M10-read-live-gone-stale-copy | live label renamed to `…executeX`; `fn("ReadTool.execute")` appended at EOF | 1 | 0 | SURVIVOR |
| M11-call-edge-severed | `e.resolve(g.messages` → `e.zzz(g.messages` (:444233 / 10947285) | 1 | 0 | SURVIVOR |
| M12-inhook-token-removed | `<system-reminder>` at :444241 / 10948410, the delivery wrapper → `<system-note>`; 17 hits remain | 1 | 0 | SURVIVOR |
| M13-token-prompt-only | all hits except the 2 prose hits at :443193 → `<system-note>` | 1 | 0 | SURVIVOR |
| M14-token-all | all 18 hits → `<system-note>` | 1 | 1 | OK (also `literal_present` FAIL) |
| M15-both-labels-deleted | both labels deleted | 1 | 1 | OK |
| M16-receiver-rename | `s.fn(` → `r.fn(` on both labels | 0 | 0 | OK |
| M17-callee-receiver-rename | `e.resolve(` → `q.resolve(` at the call site | 0 | 0 | OK |
| M18-walk-loop-disabled | `while(G.startsWith(N)&&G!==N){` (:443995 / 10895347) → `while(false){` | 1 | 0 | SURVIVOR |

Tally: OK 9, FALSE-RED 4, SURVIVOR 6. The full table with per-mutant edits and the verifier's `opencode_extract` line is in `W2DropOC4.mutants.json`.

Survivor diffs (old → new, at the stated line):
- M11, :444233: `let d=yield*[-e.resolve(g.messages-]{+e.zzz(g.messages+},h,g.messageID)`
- M12, :444241: `R+=\`\n[-<system-reminder>-]{+<system-note>+}\n${d.map((W)=>W.content)…`
- M13, :443280 and others: `may include [-<system-reminder>-]{+<system-note>+} tags` (prose; 16 hits on 14 lines changed, :443193 left alone)
- M18, :443995: `K=X.resolve(d),G=X.dirname(K);[-while(G.startsWith(N)&&G!==N){-]{+while(false){+}let W=yield*h(G);`
- M05, :443995: `b=s.[-fn("Instruction.resolve")-]{+fn("Instruction.resolveX")+}(function*(T,d,w){`, plus `+` line `fn("Instruction.resolve")` at EOF (:750050)
- M10, :444228: `$=s.[-fn("ReadTool.execute")-]{+fn("ReadTool.executeX")+}(function*(a,g){`, plus the same EOF append

## Findings

### F1 (too wide, BROKEN): four survivors show the channel can be severed while OC-4 stays green
- The rule is `read_hook = (OC_READ_HOOK_FN in dump and OC_READ_TOOL_FN in dump and OC_READ_HOOK_TOKEN in dump)` (`verify_surfaces.py:480-481`). That is whole-dump presence. It has no position, adjacency, containment, or call-edge check.
- The header says OC-4 is a WITNESS of a behaviour (`verify_surfaces.py:343-344`). Its documented limit only promises "(c) a rule whose anchor is gone reports itself unmatched" (`:350-352`). The comment at `:421-426` describes a chain: the resolver is called from ReadTool.execute and its output is delivered inside `<system-reminder>`. M11 cuts the call, M12 cuts the delivery wrapper, and M18 cuts the walk. Each one keeps OC-4 green.
- Repro (scratch clone; `echo exit=$?` after each):
  ```
  cd /fast/scratch/kotoba-r47/w2/W2DropOC4/kotoba-shokunin
  python3 verifiers/verify_surfaces.py --opencode-strings /fast/scratch/kotoba-r47/w2/W2DropOC4/mut/M12-inhook-token-removed.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings
  ```
  Output: 7 PASS lines, including `PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`. Exit 0. The same holds for `M11-call-edge-severed.strings` (exit 0) and `M18-walk-loop-disabled.strings` (exit 0).
- Independent corroboration, not novelty: sibling `.ufo/waves/round-47/falsify/W2ReadHook.md:1` (verdict PARTIAL) also reports that the gate passes with the call site deleted and with the read-tool injection deleted. M11 and M12 reproduce that here. M18 is new in this lane.

### F2 (too wide): the token is generic, so the round-47 rationale does not hold
- `<system-reminder>` occurs 18 times on 15 lines. The delivery wrapper is at :444241. Two hits are prose in the read tool description at :443193. The other hits are at :443280 (2), :443597, :443630, :443728, :443868 (2), :443901, :443916, :443921, :444800, :447443, :447466, :447467, :447468.
- The round-47 justification is in `verify_surfaces.py:425-426` and census `corpus/knowledge/instruction-surface-census-round13.md:231-232`. It says the ReadTool.execute label was added because the token alone is generic (18 hits). The added label is also a whole-dump presence test. It does not bind the token to the read path. M12 (wrapper gone, 17 hits remain) and M13 (only prose left) both stay green.
- The class's literal is the same generic token (`verifiers/surfaces-baseline.json:296`; census `:256`). `literal_present`, `literal_parity` and `kind_parity` therefore also pass on M12 and M13, because the full-run exit is 0 and every check passes. No other check catches the wrapper removal.
- The fixture comment cites the token as "injected token (443193)" (`verifiers/fixtures/surfaces/strings-opencode-clean.txt:15`). :443193 is the tool-description prose that describes the injection. The injection itself is at :444241, so the citation points at the wrong line.

### F3 (too narrow on labels; not too narrow on identifiers)
- Label text is pinned. M03 renames the Instruction label, M08 renames the ReadTool label, and M04 and M09 respell quotes. All four exit 1 with `FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:read-hook/instructions; rule(s) matched nothing: OC-4 …`. Behaviour preservation of a label rename is an [INFERENCE]: `s.fn(name)` is presumed to be a traced wrapper where `name` is only a span label. Supporting evidence: `s.fnUntraced(function*(c){` takes no name (`dump:444228` region, ReadTool.list), while traced sites pass names (`withSpan("Cli.debug.v2")` at dump byte 10105074; `withSpan("TuiConfig.layer")` at byte 7873960). This was not verified against Effect source. Quote respelling is JS-equivalent, but Bun emits one quote style, so its realism is low [INFERENCE].
- Renaming the minifier receiver is not a false red. M16 (`s.`→`r.`) exits 0. The anchors do not contain minified identifiers. M17 is trivially green, because the rule does not inspect the call site at all.
- The false red is the documented fail-closed trade (`verify_surfaces.py:345-346`). The cost is that any label-only build change needs a human re-census. The churn is real: the generation note at `verify_surfaces.py:354-364` records v2.0.26 anchors at 0 occurrences on 1.19.3.

### F4 (operability): the unmatched message names all three anchors as missing
- `verify_surfaces.py:441` is `missing = [] if matched else list(anchors)`. When OC-4 fails, every anchor is listed as missing, whichever one is absent. The message is built at `:748-754`.
- M01 deletes only `fn("Instruction.resolve")`, yet the output says `missing fn("Instruction.resolve") + fn("ReadTool.execute") + <system-reminder>`. Two of those three are present. M06 shows the same for the other label. The owned class is named correctly, but the reader is pointed at anchors that are not missing.

### F5 (too wide): a stale copy of a label satisfies the gate
- M05 and M10 each rename the live label and append a copy at EOF (line 750050). Both exit 0. The rule cannot tell a stale string from a live label.
- On 1.19.3 each label occurs exactly once (`grep -o` count 1), so this is hypothetical for this build [INFERENCE].

### F6 (calibration of the self-test): fixtures cannot show per-anchor sensitivity
- `--self-test` exits 0 with `0 failure(s) over 99 assertions`. The OC-4 drop case (`verify_surfaces.py:1041`, fixture `verifiers/fixtures/surfaces/strings-opencode-drop-oc4.txt`) contains zero `<system-reminder>` hits (`grep -c -F` prints `0`). It removes all three anchors at once, so it cannot show per-anchor sensitivity. Only this real-dump probe does (M01, M02, M06, M07, M14, M15).
- The clean fixture places the anchors on adjacent lines (`strings-opencode-clean.txt:15-18`). On the real dump the two labels are 51,079 bytes apart (:443995 and :444228), and the token is 2,134 bytes after the ReadTool label (:444241). The fixture shape does not match the real one.

## Held (survives attack)
- Substrate freshness, C1 for OC-4: `fn("Instruction.resolve")` occurs once, at :443995 (byte 10895197). `fn("ReadTool.execute")` occurs once, at :444228 (byte 10946276). The call `e.resolve(g.messages` occurs once, at :444233 (byte 10947285), inside the comment's range 444228-444233. `<system-reminder>` occurs 18 times. The comment's "18 hits" and dump lines match, and census `:231-232`, `:256` and `:320` agree.
- Hashes: `bin/opencode-1.19.3` = 179ca421… (matches SHA256SUMS). `strings -n 4 bin/opencode-1.19.3 | sha256sum` = f4d8f34a…, the dump's own hash. So the frozen dump is exactly the `strings -n 4` output the verifier expects.
- Anchor loss is red and names the class: 6 of 6 mutants (M01, M02, M06, M07, M14, M15) exit 1 with `surfaces.opencode_extract` naming `opencode:read-hook/instructions`.
- Identifier-only renames stay green: 2 of 2 (M16, M17).
- Control (M00) exits 0 with 7 PASS lines, including `opencode extraction 9/9 declared class(es) from 7/7 rules`.

## Measured fix direction (proxy only; not landed; production read-only)
- I evaluated body-scoped predicates in Python on the same mutant bytes. (a) The ReadTool body runs from `fn("ReadTool.execute")` to the next `fn("` label: dump:444228 to 444263, 10,414 bytes. It must contain `.resolve(g.messages` and `<system-reminder>`. (b) The Instruction body runs from `fn("Instruction.resolve")` to the next `fn("` label: dump:443995 to 443996, 1,013 bytes. It must contain `while(G.startsWith(N)&&G!==N){`.
- Proxy outcome: all 6 survivors go red (M05, M10, M11, M12, M13, M18). M00, M16 and M17 stay green. M03, M04, M08 and M09 remain false reds, because the label pinning is untouched.
- This assumes the next-label boundary holds in other builds [INFERENCE]; one build was measured.
- Smaller fix: compute `missing` per anchor at `verify_surfaces.py:441`.

## Commands run and exit codes
- Clone and checkout in scratch: `git clone … && git -C kotoba-shokunin checkout -q --detach 7ad7fad…` → exit 0. `rev-parse HEAD` = 7ad7fadfc09354b74fb66605dfb0c1182c115a2f.
- `sha256sum` of the copied dump and the frozen dumps → matches SHA256SUMS. `df` shows 727 GB free on /fast.
- Control: `python3 verifiers/verify_surfaces.py --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings` → exit 0, 3.3 s, 7 PASS.
- `--check surfaces.opencode_extract` on the unmutated dump → exit 0.
- `grep -o -b -F` / `grep -c -F` counts for all anchors → 1, 1, 1, and 18 occurrences on 15 lines. Byte offsets are as cited above.
- `python3 verifiers/verify_surfaces.py --self-test` → exit 0, `0 failure(s) over 99 assertions`.
- `sha256sum bin/opencode-1.19.3` → 179ca421… (exit 0). `strings -n 4 bin/opencode-1.19.3 | sha256sum` → f4d8f34a… (exit 0).
- Harness: `python3 .ufo/waves/round-47/falsify/W2DropOC4.harness.txt` → exit 0, tally `OK 9, FALSE-RED 4, SURVIVOR 6`. The final run is the 19-entry version including M18. Runtime about 78 s.
- Repro exits, after the harness: M12 exit 0; M11 exit 0; M05 exit 0; M03 exit 1; M01 exit 1.
- `grep -c -F '<system-reminder>' verifiers/fixtures/surfaces/strings-opencode-drop-oc4.txt` → `0` (grep exit 1).
- JSON check of `W2DropOC4.mutants.json` → 19 mutants, base sha f4d8f34a…, exit 0.
- Sibling read: `W2ReadHook.md:1`, read only, not modified.

## Not checked
- Runtime behaviour of opencode 1.19.3. Nothing was executed, and whether the read hook fires was not checked. The `e` binding (`Wo.Service`) and the `read` registration were not traced here. The sibling covers the source reasoning.
- Effect `fn(name)` semantics from source. Label-equivalence is an [INFERENCE] from the `fnUntraced` and `withSpan` evidence in F3.
- Other build lineages. Only 1.19.3 and the frozen omp dump were used. The default-resolution run from host binary paths was not run.
- Other rules. OC-1 through OC-3, OC-5 and OC-6, and all omp-side rules, were not mutated. Baseline-side and inventory-side mutations (the two-way parity from the baseline side) were not run.
- The C2 and C3 gates: the corpus integrity and independence gates, the fault harness, and the checklist were not run. They are not in this assignment.
- Decoding edges. `errors="replace"` (`verify_surfaces.py:203`) can split an anchor with invalid UTF-8. Not probed.
- The body-scoped proxy was not implemented in the verifier and was not run against the fixtures or the full suite.
- The labrat allowance was not used.
- No SHONEN marks, no LOG.md or lesson writes.

## Tooling
No tools installed or upgraded. I used the host's python3 (3.14.8), `/usr/bin/strings`, `sha256sum`, `grep`, and the Python stdlib.

## Artifacts (all under `.ufo/waves/round-47/falsify/`)
- `W2DropOC4.md`: this report.
- `W2DropOC4.harness.txt`: the consolidated probe. It reproduces M00–M18 and writes the JSON. The mutant dumps stay in scratch, not in the repo.
- `W2DropOC4.mutants.json`: 24 KB. Per mutant: edits with offsets and lines, correct and actual exit, verdict, `opencode_extract` line, other FAILs, and diff samples.
