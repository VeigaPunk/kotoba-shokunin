# ExecOC4 — round 72 wave 1: OC-4 re-derived on the opencode v2.1.4 bytes

**Verdict: OC-4 IS honestly derivable on v2.1.4 — the behaviour survived, the delivery
channel changed.** The committed rule matches nothing (all three of its patterns: 0 hits).
The read tool still resolves instructions on a read; it now walks up for `AGENTS.md`,
hands the found paths to `@opencode/SessionInstructions`, and that service **publishes**
`Instructions from: ${path}\n${content}` as a session update instead of appending it to the
tool result's `<system-reminder>`. A replacement rule that binds those five edges inside one
`// @bun` module matches the real dump (`OC-4 matched=True`), rejects all five same-token
decoys, rejects both previous generations (1.19.4 and v2.0.26), and keeps the class id
`opencode:read-hook/instructions` alive. Scratch copy + diff + fixtures + receipts are under
`.ufo/waves/round-72/w1/build/ExecOC4/`. **The baseline `literal` for the class is now
stale** (`<system-reminder>` no longer witnesses it) — disposition proposal in §7.

No committed lane file was modified: `git status --porcelain` shows only untracked paths
(mine under `.ufo/waves/round-72/w1/`, plus other seats' untracked fixtures), and
`git diff --stat c69711ee… -- verifiers/verify_surfaces.py` is empty, so the diff base is the
frozen base file (sha256 `4f13e3bd9d7c43b9e9d3b153b02e8f6ebb2ba57fcf66ac8ae82b9a053e809c21`).

## 0. Substrate: the shared dump was gone; re-derived byte-identically

The shared dump `/tmp/k72-oc-strings.txt` existed when I read it at the start of this seat
(`wc -l` → 1237844 lines, `sha256sum` → `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089`)
and was **absent** a few minutes later (`ls /tmp/k72-*` → no such file). Re-dumped it in my
own scratch:

```
$ S=$(date +%s) && strings -n 4 /home/vgpnk/.opencode/bin/opencode > oc-strings.txt && E=$(date +%s) && echo "wall=$((E-S))s" && sha256sum oc-strings.txt && wc -l oc-strings.txt
wall=1s
020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089  oc-strings.txt
1237844 oc-strings.txt
```

The dump sha256 equals the sha the plan records for the shared dump — the re-dump is the
same bytes, so every line number below is the shared dump's numbering. Binary sha256:
`ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7` (matches the plan's
`ca9b3ee2…`, i.e. v2.1.4). Wall time 1 s, run alone (well under the 300 s bound).

A later check found `/tmp/k72-oc-strings.txt` re-created by another seat at 18:56 (28,835,401
bytes) with sha256 `020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089` — the
same sha as my re-dump, so the three dumps (plan-recorded, re-created shared, my re-dump) are
byte-identical.

## 1. The rule as committed matches nothing (as expected)

Rule read at `verifiers/verify_surfaces.py:650-710` (constants `OC_READ_HOOK_TOKEN`,
`OC_READ_HOOK_ENTRY_RE`, `OC_READ_TOOL_ENTRY_RE`, `OC_READ_CALL_RE`, function
`opencode_read_hook_matches` at `:673`). Ran the committed module itself (not a copy):

```
$ python3 run_committed.py            # imports verifiers/verify_surfaces.py, calls extract_opencode_classes(dump)
OC-1   matched=False owns=['opencode:instructions/AGENTS.md', …] missing=['["AGENTS.md" … "CONTEXT.md"]', 'disableClaudeCodePrompt']
OC-2   matched=False … missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
OC-3a  matched=False … missing=['for(let <v> of <v>.instructions)']
OC-3b  matched=False … missing=['.instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://"))', 'Instructions from: ']
OC-4   matched=False owns=['opencode:read-hook/instructions'] missing=['Instruction.resolve exported as .resolve', 'ReadTool.execute calls .resolve(messages, path, id)', '<system-reminder> wraps the resolved content']
OC-5   matched=False owns=[] missing=['OPENCODE_DISABLE_PROJECT_CONFIG', 'globUp(<v>.directory,<v>.worktree)', 'globUp(<v>.config,<v>.config)']
OC-6   matched=False owns=['opencode:instruction-context/AGENTS.md'] missing=['core/instructions key + InstructionContext.observe AGENTS.md walk', 'instruction-context layer registered under system-context-builtins']
ids: []
OC-4 rule fn opencode_read_hook_matches -> False
OC_READ_TOOL_ENTRY_RE hits: 0
OC_READ_HOOK_ENTRY_RE hits: 0
OC_READ_CALL_RE hits: 0
```

(receipt: `build/ExecOC4/receipt-committed-rule.txt`; wall 30 s, run alone.)

Two extra facts about the committed rule on this dump, measured, because they explain why it
fails silently rather than loudly:

```
$ python3 -c "d=open('oc-strings.txt').read(); print(d.count('\n// @bun\n'), d.count('// @bun @bytecode'))"
0 581
```

The committed OC-4 scopes by the literal separator `"\n// @bun\n"` (`:675`, `:678`). That
literal occurs **0 times** in the v2.1.4 dump (v2.1.4 separators carry `@bytecode`/`@bun-cjs`
suffixes), so its module scope silently degrades to the whole dump — a latent bug that would
have made a whole-dump false positive possible. The replacement uses
`OC_MODULE_SEP_RE = r"\n// @bun[^\n]*"` and a real `opencode_module()` bound.

Anchor sweep on the v2.1.4 dump (`grep -c -F`, receipt `receipt-sweep.txt`):

```
Instruction.resolve              0        InstructionContext               0
ReadTool.execute                 0        system-context-builtins          0
ReadTool.Plugin                  2        core/instructions                2
opencode.tool.read               2        @opencode/SessionInstructions    2
<system-reminder>               14        Instructions from:               3
targets:[LF]                     1        OPENCODE_DISABLE_PROJECT_CONFIG  2
```

## 2. The v2.1.4 form of what OC-4 was written to witness

All five edges live in ONE `// @bun` module, dump lines **708687–708708** (module span
708529–708897; the module also contains the plan-mode reminder strings at 708781/708786,
which is why `<system-reminder>` being present proves nothing about this channel — the read
plugin's own body contains none: `'<system-reminder>' in body` → `False` over the plugin's
first 4000 chars).

Each quote below was verified with `grep -c -F` (every one returns exactly 1 occurrence) and
the dropped bytes are named. Quotes are ≤25 words; the code tokens are single whitespace
words, so word counts are 1–8.

| # | edge | line | located quote (bytes dropped named) |
|---|---|---|---|
| 1 | read-tool plugin registration | 708708 | `{id:"opencode.tool.read",effect:c("ReadTool.Plugin")(function*` — dropped: the effect body that follows the arrow |
| 2 | the plugin binds the instruction service | 708708 | `l=yield*sl` — dropped: the neighbouring bindings `a=yield*TP,i=yield*Pi` |
| 3 | walk-up for the instruction file | 708708 | `.up({targets:[LF],start:O.content.type==="list-page"?C:rr(C),stop:V,type:"file"})` — dropped: the receiver expression before `up(` |
| 4 | the walked target is the AGENTS.md literal | 708708 | `LF="AGENTS.md"` — dropped: the following `,$F=o({…})` tool schema |
| 5 | the read hands the found paths to the service | 708708 | `yield*l.load({sessionID:q.sessionID,paths:Y})` — dropped: the trailing `.pipe(pe(()=>g),Ts(()=>g))` |
| 6 | the service identity | 708687 | `class sl extends U()("@opencode/SessionInstructions"){}` — dropped: the following `var BS=z(sl,…` layer wiring |
| 7 | the service provides `load` | 708689 | `return sl.of({load:_})}));` — dropped: the preceding `load` body |
| 8 | the service **publishes** the rendered instruction text | 708687 | `e.publish(hv,{sessionID:h.sessionID,text:N.map((O)=>` `` `Instructions from: ${O.path}` `` **NL** `` `${O.content}`).join(` `` **NL** `))` — NL = a literal 0x0A byte inside each template (verified: `ord(d[i+28]) == 10` at both render sites), not an escape |

Read path of edges 1–8 in context — line numbers from `grep -n -F`, text is the located
quotes with `…` marking dropped bytes:

```
708687  class sl extends U()("@opencode/SessionInstructions"){}var BS=z(sl,s(function*(){… _=c("SessionInstructions.load")(function*(h){ … readFileStringSafe(O) … e.publish(hv,{sessionID:h.sessionID,text:N.map((O)=>`Instructions from: ${O.path}
708688  ${O.content}`).join(`
708689  `),description:`Loaded ${N.map((O)=>WS(r,O.path)).join(", ")}`,metadata:{instruction:{paths:N.map((O)=>O.path)}}}) … return sl.of({load:_})}));
708708  LF="AGENTS.md",… QF={id:"opencode.tool.read",effect:c("ReadTool.Plugin")(function*(e){let a=yield*TP,i=yield*Pi,l=yield*sl,… execute:(F,q)=>s(function*(){… .up({targets:[LF],…,type:"file"}) … yield*l.load({sessionID:q.sessionID,paths:Y}) …
```

So the old rule's three edges map 1:1 onto the new ones: `Instruction.resolve` service export
→ `@opencode/SessionInstructions` with `load`; `ReadTool.execute` calling `.resolve(messages,
path, id)` → the read plugin calling `<svc>.load({sessionID,paths})` after the walk-up;
"resolved content wrapped in `<system-reminder>`" → the service **publishing** the rendered
text (`session.instructions.updated`, `grep -c` → 5; `instructionUpdate` → 3; the generation
path splices it as a system message). Delivery moved; the role did not.

## 3. The replacement rule (scratch copy) and its decoys

Deliverables: `build/ExecOC4/verify_surfaces.py` (full copy, sha256
`59dee8d3944d556acd262b00f20742083831130e4ce48bbec12535b3c66d2ec8`) and `build/ExecOC4/rule.diff`
(242 lines; 136 lines begin with `+`, including the `+++` header). The diff replaces only the OC-4 block: the three old constants and
`opencode_read_hook_matches`, the rule's anchor strings at the `rule("OC-4", …)` call, an
append-only round-72 GENERATION NOTE paragraph, and the OC-4 self-test arms. No other rule,
check, or parser touched.

The matcher binds, inside one `// @bun` module:

1. `OC_INSTR_SERVICE_RE` — `class <svc> extends U()("@opencode/SessionInstructions")`;
2. `<svc>.of({load:` — the service actually provides `load`;
3. `OC_INSTR_RENDER_RE` — `Instructions from: ${<x>.path}` + (`\n` or 0x0A) + `${<x>.content}`,
   and that render must sit within 300 chars after a `.publish(` (the rendered text is the
   published payload, not a helper used elsewhere);
4. `OC_READ_PLUGIN_RE` — the `opencode.tool.read` / `ReadTool.Plugin` registration;
5. `OC_READ_WALK_RE` — `.up({targets:[<t>],…,type:"file"})` in that plugin body, with
   `<t>="AGENTS.md"` bound in the module;
6. `OC_READ_INSTR_LOAD_RE` — `<callee>.load({sessionID:<v>.sessionID,paths:<v>})` in the same
   plugin body, with `<callee>=yield*<svc>` (the load must target the instruction service).

Fail-closed: no service → no iteration → `False`; each missing edge `continue`s; the rule
reports itself unmatched with the three anchor labels.

**Decoys — same tokens, no instruction-loading role.** The positive fixture is verbatim dump
bytes: slice A = dump bytes 708687–708689 (1,178 bytes), slice B = 708708 (2,010 bytes),
joined by one synthetic `\n// @bun @bytecode\n` separator; proof the fixture is the real
bytes: `A in dump: True | B in dump: True`, `fixture == sep+A+B+newline: True`. Each decoy is
a single-token delta of that fixture (each delta occurs exactly once in the positive):

| decoy | single-token delta | role destroyed | result |
|---|---|---|---|
| `…-decoy-load.txt` | `l=yield*sl,` → `l=yield*sq,` | the load no longer targets the instruction service (all other tokens, incl. `.load({sessionID:q.sessionID,paths:Y})`, intact) | **rejected** |
| `…-decoy-target.txt` | `LF="AGENTS.md"` → `LF="NOTES.md"` | the read no longer walks for an instruction file | rejected |
| `…-decoy-walk.txt` | `stop:V,type:"file"` → `stop:V,type:"dir"` | no file walk (same `up({targets:[LF]` tokens) | rejected |
| `…-decoy-render.txt` | `Instructions from: ${O.path}` → `Sources loaded: ${O.path}` | the service renders no instruction text | rejected |
| `…-decoy-publish.txt` | `e.publish(hv,{sessionID:h.sessionID,text:N.map((O)=>` → `h.sessionID,N.map((O)=>` | render present but never published | rejected |

Probe run (`python3 -B oc4_probe.py <dump> <fixtures>`; receipt `receipt-probe.txt`):

```
edges of the re-derived OC-4 witness in the real dump:
  instruction service class      708687
  render template                708687
  read plugin registration       708708
  read-plugin walk-up            708708
  read-plugin instruction load   708708
  service .of({load:})           708689
  LF="AGENTS.md" binding         708708

opencode_read_hook_matches(real dump) = True

fixture                                              OC-4
… 29 lane + new fixtures …
strings-opencode-1.19.4-anchors.txt                  False      <- previous generation
strings-opencode-v2.0.26.txt                         False      <- retired generation
strings-opencode-clean.txt                           False      <- 1.19.4 shapes
strings-opencode-v2.1.4-oc4-decoy-load.txt           False
strings-opencode-v2.1.4-oc4-decoy-publish.txt        False
strings-opencode-v2.1.4-oc4-decoy-render.txt         False
strings-opencode-v2.1.4-oc4-decoy-target.txt         False
strings-opencode-v2.1.4-oc4-decoy-walk.txt           False
strings-opencode-v2.1.4-oc4.txt                      True
```

30 fixtures: only the v2.1.4 positive matches. No generation is accepted twice (the rule is
not an OR of 1.19.4 and v2.1.4 anchors).

Per-rule report from the scratch copy on the real dump:

```
$ python3 -c "<import build/ExecOC4/verify_surfaces.py>; extract_opencode_classes(dump)"
OC-1 matched=False   OC-2 matched=False   OC-3a matched=False   OC-3b matched=False
OC-4 matched=True owns=['opencode:read-hook/instructions']
OC-5 matched=False   OC-6 matched=False
ids: ['opencode:read-hook/instructions']
```

## 4. Scratch copy run with the required flags

```
$ cd <scratch>/run/verifiers && python3 -B verify_surfaces.py \
    --opencode-strings /tmp/k72w1-ExecOC4/oc-strings.txt \
    --omp-binary /home/vgpnk/.local/bin/omp.real
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md; rule(s) matched nothing: OC-1 (…); OC-2 (…); OC-3a (…); OC-3b (…); OC-5 (…); OC-6 (…)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
```

`--json`: `pass 5 fail 2 exit 1` (receipt `receipt-run.json`; full text
`receipt-percheck.txt`). Two things to read off it precisely:

* `opencode:read-hook/instructions` is **absent** from "produced by no rule", and OC-4 is
  **absent** from "rule(s) matched nothing" — the class is produced by the re-derived rule.
* The remaining opencode_extract failure is the other six rules (their 1.19.x anchors are 0
  hits on v2.1.4); `literal_present` fails only on `CONTEXT.md`. So `surfaces pass 5 of 7` is
  the honest post-OC-4 state; C2's `p == 7` needs the other five re-derivations.

## 5. Self-test state of the scratch copy (measured, not assumed)

```
$ python3 -B verify_surfaces.py --self-test
4 failure(s) over 196 assertions
```

The four red arms are exactly the ones that assert the **1.19.4 fixture** satisfies every
rule, which cannot hold once OC-4 moves generation:

```
self-test FAIL: clean: exit 0: got 1
self-test FAIL: clean: PASS surfaces.opencode_extract: got '… FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:read-hook/instructions; rule(s) matched nothing: OC-4 (…) …'
self-test FAIL: new-callees: exit 0: got 1
self-test FAIL: oc-extra: exit 0: got 1
```

`clean`/`new-callees`/`oc-extra` all default to `strings-opencode-clean.txt` (1.19.4 shapes:
`grep -c -F 'Instruction.resolve'` → 1, `ReadTool.execute` → 2). They go green when the
v2.1.4 fixture set replaces `strings-opencode-clean.txt`, i.e. when OC-1/2/3/5/6 land — that is
wave-2/C2 work, not this seat's. All new OC-4 arms pass, including the generation arms:

```
("strings-opencode-v2.1.4-oc4.txt", True)                     -> OC-4 matches
(the five decoys, False)                                      -> rejected
("strings-opencode-1.19.4-anchors.txt", False)                -> rejected
("strings-opencode-v2.0.26.txt", False)                       -> rejected
("strings-empty.txt", False)                                  -> rejected
```

The `oc-1.19.4 anchors` CLI arm was changed from "exit 0" to "exit 1, only OC-4 unmatched" and
the decoy loop's `other_rule` assertion now tolerates OC-4 (previous generation) — both are
recorded in `rule.diff`; leaving them would have been a stale assertion that only passes on a
false premise.

## 6. What lands where (for the L1)

* `build/ExecOC4/verify_surfaces.py` → `verifiers/verify_surfaces.py` (apply `rule.diff`).
* `build/ExecOC4/fixtures/strings-opencode-v2.1.4-oc4*.txt` (6 files: positive + 5 decoys) →
  `verifiers/fixtures/surfaces/` — the dir `FIXTURES` resolves to
  (`Path(__file__).parent / "fixtures" / "surfaces"`, `:161`). Note other seats are currently
  dropping untracked fixtures at `verifiers/fixtures/` (top level, e.g.
  `oc2-v2.1.4-anchor.txt`), which `FIXTURES` does **not** read — worth a check before the
  integration commit.
* `build/ExecOC4/fixtures/baseline-oc4-only.json` is scratch-only (a one-class baseline used
  to exercise OC-4 alone); it does not need to land.
* `build/ExecOC4/oc4_probe.py` + `run_committed.py` + `receipt-*.txt` are re-runnable receipts.

## 7. Census disposition: the class stays, its baseline `literal` does not

`opencode:read-hook/instructions` is **kept** (the rule produces it from real v2.1.4 bytes).
But its baseline row is now misleading:

```
$ grep -n -A5 '"opencode:read-hook/instructions"' verifiers/surfaces-baseline.json
294:   "class_id": "opencode:read-hook/instructions",
295-   "harness": "opencode",
296-   "literal": "<system-reminder>",
297-   "context_kind": "loader-literal",
298-   "verdict": "governed"
```

`<system-reminder>` occurs 14 times in the v2.1.4 dump (plan-mode prompts at 708781/708786,
the TUI selection reminders at 705219/705220, the harness prompt text at 1204640/1228620/
1228681/1228750), **none of them the read channel** — so `check_literal_present` stays green
on a token that no longer witnesses the class. That is the drift, not a gate failure.

Recommendation (L1 decision, with the C2 consequence spelled out): set the row's `literal` to
`Instructions from: ` (3 occurrences in the dump: 607084 string table, 708288 `Rr` render,
708687 the `SessionInstructions.load` publish — the class's own delivery token). Because C2's
ledger conjunct counts a class "kept" only on the **same** `class_id`, `literal`,
`context_kind`, `verdict`, changing the literal requires a `verifiers/census-removals.json` row
for `opencode:read-hook/instructions` (that file does not exist yet:
`ls verifiers/census-removals.json` → `No such file or directory`; C2's counter creates it).
Suggested row shape, to be filled by the C2 owner:

```json
{"class_id": "opencode:read-hook/instructions", "harness": "opencode",
 "from": {"literal": "<system-reminder>", "context_kind": "loader-literal"},
 "to":   {"literal": "Instructions from: ", "context_kind": "loader-literal"},
 "reason": "round 72: v2.1.4 moved the read channel's delivery from the tool result's <system-reminder> to the SessionInstructions publish (dump 708687/708708); class kept, witness literal re-pointed"}
```

If the L1 prefers to keep the literal (a legal choice: the literal is still present, so no gate
goes red), then the drift must be recorded in the census text instead — the class would then be
"kept" by the ledger but its literal would witness nothing. I do not recommend that; the
literal is the machine-checkable half of the class and should name its witness.

## 8. Risks and limits (recorded, not papered over)

* **Publish-window heuristic.** The render must sit within 300 chars after a `.publish(`. Real
  bytes satisfy it by ~50 chars. A re-minified bundle that hoists the render into a helper
  before the publish call would be **rejected** (fail-closed → OC-4 unmatched, reported by
  name). That is the documented limit of this rule, not a silent pass.
* **Two accepted newline encodings** in the render template (`\n` escape or a literal 0x0A
  byte). This is the same template, not two shapes; the v2.1.4 dump carries the 0x0A byte.
* **Not a completeness claim.** The rule witnesses the channel it names; a third instruction
  subsystem reached by another path is out of the set (same documented limit as the block's
  header, `:557-561`).
* **The other five rules are untouched and still 1.19.x.** `surfaces pass 5 of 7` on the real
  dumps is the post-OC-4 measurement; `p == 7` (C2) needs OC-1/2/3/5/6 re-derived.
* **`oc_clean` fixture is 1.19.4-shaped**, so four self-test arms stay red until the v2.1.4
  fixture set lands (exact arms listed in §5). Nothing else in the self-test regressed: 196
  assertions, 4 failures, all four named.
* No tool installs or upgrades were made; no pacman transaction was run. No network fetch.
* Scratch `/tmp/k72w1-ExecOC4` (dump + run tree) is deleted before return; the dump is
  reproducible with the one-line `strings -n 4` command in §0 and its sha is recorded.

## Files written (all drafts; no committed lane file touched)

```
.ufo/waves/round-72/w1/ExecOC4.md                       (this report)
.ufo/waves/round-72/w1/build/ExecOC4/verify_surfaces.py (scratch copy, sha256 59dee8d3…)
.ufo/waves/round-72/w1/build/ExecOC4/rule.diff          (242 lines vs the base file)
.ufo/waves/round-72/w1/build/ExecOC4/oc4_probe.py
.ufo/waves/round-72/w1/build/ExecOC4/run_committed.py
.ufo/waves/round-72/w1/build/ExecOC4/receipt-committed-rule.txt
.ufo/waves/round-72/w1/build/ExecOC4/receipt-sweep.txt
.ufo/waves/round-72/w1/build/ExecOC4/receipt-probe.txt
.ufo/waves/round-72/w1/build/ExecOC4/receipt-percheck.txt
.ufo/waves/round-72/w1/build/ExecOC4/receipt-run.json
.ufo/waves/round-72/w1/build/ExecOC4/receipt-selftest.txt
.ufo/waves/round-72/w1/build/ExecOC4/fixtures/strings-opencode-v2.1.4-oc4.txt
.ufo/waves/round-72/w1/build/ExecOC4/fixtures/strings-opencode-v2.1.4-oc4-decoy-{load,target,walk,render,publish}.txt
.ufo/waves/round-72/w1/build/ExecOC4/fixtures/baseline-oc4-only.json
```

*The scratch copy is byte-identical to the file `rule.diff` was generated against (same
sha256); `rule.diff` is the authoritative artifact — apply it rather than hand-copying.
Hunk map: `@@ -574` (generation note), `@@ -647` (OC-4 constants + matcher), `@@ -802` (the
`rule("OC-4", …)` anchors), `@@ -1608` and `@@ -1639` (the OC-4 self-test arms).*
