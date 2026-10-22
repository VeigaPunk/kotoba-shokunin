Result: HOLDS — the C1 fixture changes are a necessary, honest adaptation to the re-derived OC-4 rule; every pre-existing arm still isolates its rule, and the new decoys keep all bare literals while breaking exactly one call shape each.

# W2ReviewOcFixtures — opencode surface fixtures, C1 (opencode re-pin)

Seat: KotobaR53.W2ReviewOcFixtures. Lane: kotoba-shokunin @ c775d6823bfca8f0de8c0874032a954438b38edc (judged).
Scope: `git diff aeed0890efb7cb62ef1364ce7d7ba5566ef3fed6 6dd311644f987cef62a40f0c028ea2be2fc6ff67 -- verifiers/fixtures/surfaces/`.
All probes ran in the sandbox clone /fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReviewOcFixtures/kotoba-r53 (HEAD = judged rev). No tools installed; no installs performed.

## 0. What the diff actually contains

`git diff aeed0890 6dd3116 -- verifiers/fixtures/surfaces/` → 12 files, 219 insertions / 45 deletions:

- 3 NEW files: `strings-opencode-1.19.4-anchors.txt`, `strings-opencode-1.19.4-decoy-oc4.txt`, `strings-opencode-1.19.4-decoy-oc6.txt`.
- 9 MODIFIED pre-existing files: `strings-opencode-clean.txt`, `strings-opencode-drop-oc1/2/3a/3b/5/6.txt`, `strings-opencode-extra.txt`, `strings-opencode-planted-name.txt`.
- UNCHANGED: `strings-opencode-drop-oc4.txt`, `strings-opencode-v2.0.26.txt`, all baseline/inventory fixtures.

Note: the assignment says "10 pre-existing opencode fixtures C1 modified"; the actual diff modifies 9. `drop-oc4.txt` is untouched (found: informational, severity LOW).

For every one of the 9 modified files the delta is byte-identical in kind (verified per-file, `grep -E '^[+-]'` excluding `---/+++`):

1. Header comment rewrite (5 removed / 4 added lines, wording only): "Every non-comment line is an exact byte substring of … no other binary text is committed" → "Non-comment anchors are exact byte substrings of … Synthetic lines (not dump bytes): … and the round-53 synthetic OC-4 export/call/result bridge lines."
2. The same 8 synthetic OC-4 bridge lines inserted between the OC-4 block and OC-5:

```
# synthetic OC-4 resolver service export bridge (not a raw dump excerpt)
});return O1.of({resolve:b})
# synthetic OC-4 call/result bridge (not a raw dump excerpt)
let y=yield*e.resolve(g.messages,h,w)
y.length>0)_+=`
<system-reminder>
${y.map((B)=>B.content).join(`
</system-reminder>
```

No anchor byte in any rule payload was altered (clean/drop/extra/planted OC-1..OC-6 lines are unchanged vs aeed0890).

## 1. Why was each changed

Root cause is the C1 rule re-derivation in `verify_surfaces.py`. The old OC-4 rule (pre-C1) was a pure presence test: `OC_READ_HOOK_FN in dump and OC_READ_TOOL_FN in dump and OC_READ_HOOK_TOKEN in dump` where `OC_READ_HOOK_FN = 'fn("Instruction.resolve")'` (verify_surfaces.py at aeed0890, ~line 640). On installed 1.19.4 the minifier renamed the registration wrapper `fn` → `l`, so OC-4 matched nothing and the base counter read 6/7. C1 replaced it with a structured witness (`opencode_read_hook_matches`, verify_surfaces.py:673-708): the `Instruction.resolve` entry, an export binding `resolve:<method>` in an `.of({...})` return, the `ReadTool.execute` entry, the call edge `=yield*<v>.resolve(<v>.messages, …)`, and same-result `<system-reminder>` delivery `result.map((B)=>B.content).join(`.

The 9 old fixtures are 1.19.3-generation excerpts; they carry real `fn(...)` shapes but not the new export/call/delivery geometry. Under the new rule they all fail OC-4, which would break every arm that is not about OC-4:

- clean and extra would FAIL (they must exit 0),
- each drop-oc1/2/3a/3b/5/6 would FAIL both its dropped rule AND OC-4, so the arm would no longer isolate,
- planted-name would additionally fail OC-4 (still exit 1, but noisy).

The bridge lines re-satisfy OC-4, restoring each fixture's original semantics. Tag verified: C1 verifier on base-content copies of the 9 files gives exactly this failure picture:

```
strings-opencode-clean.txt (base): rc=1 status=FAIL detail=... OC-4 (owns opencode:read-hook/instructions; missing ...)
strings-opencode-drop-oc1.txt (base): rc=1 status=FAIL detail=... OC-1 (...missing...); OC-4 (...missing...)
strings-opencode-drop-oc2.txt (base): rc=1 FAIL OC-2 + OC-4
strings-opencode-drop-oc3a.txt (base): rc=1 FAIL OC-3a + OC-4
strings-opencode-drop-oc3b.txt (base): rc=1 FAIL OC-3b + OC-4
strings-opencode-drop-oc5.txt (base): rc=1 FAIL OC-4 + OC-5
strings-opencode-drop-oc6.txt (base): rc=1 FAIL OC-4 + OC-6
strings-opencode-extra.txt (base): rc=1 FAIL OC-4
strings-opencode-planted-name.txt (base): rc=1 FAIL OC-4 + GUIDE.md undeclared
```

OC-6 needed no fixture edits: `opencode_context_layer_matches` (verify_surfaces.py:711-755) retains the committed 1.19.3 fixture shape as an explicit fallback (`Key.make("core/instructions")` + observe + targets + `i({name:"system-context-builtins",layer:...})`), so the old fixtures keep passing OC-6 unchanged. This is documented at verify_surfaces.py:748-749.

## 2. Does any change weaken what a 1.19.3-era arm proved?

No. Empirically, with the C1 verifier on the C1 fixtures:

| fixture | exit | opencode_extract detail (observed) |
|---|---|---|
| clean | 0 | PASS 9/9 declared from 7/7 rules |
| drop-oc1 | 1 | FAIL: only OC-1 unmatched; names instructions/AGENTS.md, /CLAUDE.md, /CONTEXT.md |
| drop-oc2 | 1 | FAIL: only OC-2 unmatched; names config/AGENTS.md, claude-home/CLAUDE.md |
| drop-oc3a | 1 | FAIL: only OC-3a unmatched; names config/instructions |
| drop-oc3b | 1 | FAIL: only OC-3b unmatched; names config/instructions-remote |
| drop-oc4 (unchanged) | 1 | FAIL: only OC-4 unmatched; names read-hook/instructions |
| drop-oc5 | 1 | FAIL: only OC-5 unmatched (shape witness) |
| drop-oc6 | 1 | FAIL: only OC-6 unmatched; names instruction-context/AGENTS.md |
| extra | 0 | PASS 9/9 from 7/7 (decoy shapes extract nothing) |
| planted-name | 1 | FAIL: undeclared opencode:instructions/GUIDE.md |
| anchors (new) | 0 | PASS 9/9 from 7/7 |
| decoy-oc4 (new) | 1 | FAIL: only OC-4 unmatched |
| decoy-oc6 (new) | 1 | FAIL: only OC-6 unmatched |
| v2.0.26 | 1 | FAIL: vacuity + all 9 classes named, OC-1 first |

Every drop fixture still isolates exactly its rule; nothing else is reported unmatched. `extra` still proves the rules are not literal-greedy (its `# not anchors` block — `H.up({targets:["RULES.md"]…})`, `X.join(r.config,"opencode.json")`, `projectSource` — extracts nothing). `planted-name` still discriminates a planted array name. The v2.0.26-generation arm still fails (OC-1 unmatched ⇒ the rule set is not OR-ed across generations).

Observation (severity LOW, not a defect): in the 9 adapted fixtures the OC-4 PASS now rests on hand-authored non-dump bytes rather than authentic dump substrings. The headers mark these lines as synthetic (line 7-11 of each fixture), and one OC-4 evidence for the claim is not these fixtures at all: it is the frozen counter measured on the host binary (see §4). The arms prove rule necessity / non-greediness, and still do.

## 3. Decoy fixtures: bare literals kept, call shape broken

Self-test `oc_literals` (verify_surfaces.py:1617-1619) asserts all 7 literals in each decoy: `Instruction.resolve`, `ReadTool.execute`, `<system-reminder>`, `core/instructions`, `targets:["AGENTS.md"]`, `InstructionContext.observe`, `system-context-builtins`. Verified in content and by the self-test:

- decoy-oc4: keeps `l("Instruction.resolve")`, `l("ReadTool.execute")`, export `resolve:k`, `<system-reminder>` delivery block; breaks only the call edge `let y=yield*r.resolve(F.messages,I,F.messageID)` → `let y=yield*r.load(...)` (`OC_READ_CALL_RE` requires `\.resolve\(`, verify_surfaces.py:665-670). Exit 1, only OC-4 unmatched.
- decoy-oc6: keeps `Wr.make("core/instructions")`, observe/targets, and both registrations; breaks only the dependency edge: `sD=Re({name:"system-context-builtins",layer:HD,deps:[Ac,lH,iD,O.node,hs]})` → `deps:[Ac,lH,O.node,hs]` (the `builtins_re` requires `\b<instance>\b` = `iD` inside deps, verify_surfaces.py:739-744). Exit 1, only OC-6 unmatched. The literal `iD` itself remains elsewhere in the file (its own registration line), so no bare literal is lost.

## 4. The claim itself (host binary) at the judged revision

`python3 -B verifiers/check_opencode_repin.py --rev c775d6823bfca8f0de8c0874032a954438b38edc --repo <clone>` → exit 0:

```
opencode re-pin: surfaces pass 7 of 7 (opencode_extract PASS); pins OK 3/3; opencode classes kept 9 of 9; self-test 0 failure(s) over 155 assertions
substrate opencode: /home/vgpnk/.npm/_npx/e2094862b59aac7b/node_modules/opencode-ai/bin/opencode.exe sha256 538fcb1b6408c8d4608822acee19f7ff5b3a3eb3383c0633c4f06170857312a7 bytes 214522032
```

`surfaces-baseline.json` is byte-identical between aeed0890 and 6dd3116 (empty diff), and the counter's kept = 9/9 confirms no literal/kind/verdict changes. `verifiers/baseline.json` changes only the opencode sha (179ca421… → 538fcb1b…) and adds the round-53 note.

`python3 -B verifiers/verify_surfaces.py --self-test` → `0 failure(s) over 155 assertions`, exit 0 (the three `NO-SUCH` ERROR lines are the expected missing-dump arm, which asserts exit 2).

## Findings summary

- F1 (LOW, informational): "10 pre-existing fixtures" vs 9 actually modified; `drop-oc4.txt` unchanged. No effect on arms.
- F2 (no defect): the 9 identical edits are the OC-4 bridge adaptation; without them every non-OC-4 arm would break (probed). All arms hold after it.
- F3 (no defect): decoys keep all 7 bare literals and break one shape each; both exit 1 with only the target unmatched.
- F4 (LOW, observation): OC-4's pass inside the 9 adapted fixtures is now synthetic-content dependent, documented in the fixture headers. It does not weaken what those arms assert; the 1.19.4-matching evidence is the host-binary counter.

## Residual risk / verification gaps

- I did not independently regenerate a `strings -n 4` dump of the host binary (that is erratum guard (b), a separate seat); I cite the counter's own measured substrate line with sha256 and bytes.
- Fixture behavior verified at c775d682 (== C1 for these files; floors commit touched none of them).

Evidence pointers: per-file line dumps in this seat's scratch (`perfile_diffs.txt`), probe driver `probe_fixtures.py`, both in /fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2ReviewOcFixtures/.
