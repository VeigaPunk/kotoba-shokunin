# ExecOC2 — OC-2 re-derived on the opencode v2.1.4 bytes (round 72, wave 1)

**Verdict: OC-2 IS honestly derivable — but only its CONFIG half.** On the v2.1.4 bytes the
round-14 witness (`X.join(<v>.config,"AGENTS.md")` + `X.join(<v>.home,".claude","CLAUDE.md")`)
matches **0x**: the loader moved into the `opencode.config.instruction` plugin and the minifier
aliased `path.join` to a bare callee, so the rule must bind plugin id + join alias + the
`globalSource` arm. A replacement rule that binds those three derives exactly
`opencode:config/AGENTS.md` on the live dump and rejects three decoys that carry the same tokens
without an instruction-loading role. The **home half is gone**: `CLAUDE.md` survives 3x in the dump
in non-loader roles and `.claude` survives only as a config-directory root, so
`opencode:claude-home/CLAUDE.md` must be **removed by the census ledger with a reason**, never
derived by a loosened regex. That removal collides with C2's frozen ledger conjunct
(plan:124-127 keys the ledger on *literal* absence and `CLAUDE.md` is present) — see B1, which the
C2 owner must settle before data.

Nothing committed was modified: deliverables are scratch under
`.ufo/waves/round-72/w1/build/ExecOC2/`.

## Substrate (re-derived here, because the shared dumps were gone)

`/tmp/k72-oc-strings.txt` and `/tmp/k72-omp-strings.txt` were **absent** at 18:39 (`ls` → no such
file). I regenerated the opencode dump in my own scratch and proved it is the same bytes:

```
$ strings -n 4 /home/vgpnk/.opencode/bin/opencode > oc-strings.txt
$ sha256sum oc-strings.txt            # 020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089
$ sha256sum /home/vgpnk/.opencode/bin/opencode
ca9b3ee262e33bb4e7aa0e1230dc61086a474c8c8016b980081d0719712fd2e7  /home/vgpnk/.opencode/bin/opencode
$ wc -l oc-strings.txt
1237844 oc-strings.txt
```

Both shas equal the plan's (`020fb253…` dump, `ca9b3ee2…` binary), and the line count matches what I
read from the shared dump before it vanished (1,237,844 lines, same 28,835,401 bytes), so every
number below is measured on the same bytes the shared dump held.
Tools: GNU strings (GNU Binutils) 2.47, Python 3.14.8. No tool installed or upgraded.

## F1 — the rule as committed matches nothing (step 1)

```
$ cd <lane> && python3 -c "
import sys; sys.path.insert(0,'verifiers'); import verify_surfaces as v
dump=open('<scratch>/oc-strings.txt',encoding='utf-8',errors='replace').read()
print('OC_CONFIG_JOIN_RE hits', [m.group(0) for m in v.OC_CONFIG_JOIN_RE.finditer(dump)][:20])
print('OC_HOME_DIR_JOIN_RE hits', [m.group(0) for m in v.OC_HOME_DIR_JOIN_RE.finditer(dump)][:20])
ids,rep=v.extract_opencode_classes(dump); print('ids',sorted(ids))
for r in rep: print(r['rule_id'], r['matched'], r['missing'])"
OC_CONFIG_JOIN_RE hits []
OC_HOME_DIR_JOIN_RE hits []
ids []
OC-1 False ['["AGENTS.md" … "CONTEXT.md"]', 'disableClaudeCodePrompt']
OC-2 False ['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
OC-3a False ['for(let <v> of <v>.instructions)']
OC-3b False ['.instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://"))', 'Instructions from: ']
OC-4 False ['Instruction.resolve exported as .resolve', 'ReadTool.execute calls .resolve(messages, path, id)', '<system-reminder> wraps the resolved content']
OC-5 False ['OPENCODE_DISABLE_PROJECT_CONFIG', 'globUp(<v>.directory,<v>.worktree)', 'globUp(<v>.config,<v>.config)']
OC-6 False ['core/instructions key + InstructionContext.observe AGENTS.md walk', 'instruction-context layer registered under system-context-builtins']
```

Both OC-2 regexes find nothing and the committed set extracts 0 classes on v2.1.4; every one of the
7 rules reports `matched=False` (see F5). The rule's `owns` fallback in the FAIL message is
`['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md']` (base run, F5).

## F2 — the real v2.1.4 witness: literal, shape, line numbers, quote (step 2)

The loader is the `opencode.config.instruction` plugin. Every slice below is a verbatim byte slice of
dump **line 708687** (that line is 47,694 bytes; each command drops all bytes outside the named
`cut` range), offsets 0-based:

```
$ sed -n '708687p' oc-strings.txt | cut -c3233-3279
import td,{dirname as RM,join as j1}from"path";
$ sed -n '708687p' oc-strings.txt | cut -c3287-3345
tt({id:"opencode.config.instruction",effect:c(function*(e){
$ sed -n '708687p' oc-strings.txt | cut -c3647-3689
D=yield*l.resolve(j1(r.config,"AGENTS.md"))
$ sed -n '708687p' oc-strings.txt | cut -c4328-4368
c("ConfigInstructionPlugin.globalSource")
$ sed -n '708687p' oc-strings.txt | cut -c7525-7588
tt({id:"opencode.config.location-watcher",effect:c(function*(e){
```

Quotes (≤25 words each; bytes dropped named above): `import td,{dirname as RM,join as j1}from"path";`
· `tt({id:"opencode.config.instruction",effect:c(function*(e){` ·
`D=yield*l.resolve(j1(r.config,"AGENTS.md"))` · `c("ConfigInstructionPlugin.globalSource")`.

Shape: `join` is imported aliased (`join as j1`), the config candidate is
`j1(<v>.config,"AGENTS.md")` — a **bare callee**, not `.join(` — and it is read by the plugin's
`globalSource` arm (`if(!a.global||!(yield*l.isFile(D)))return[]`, D = the resolved join). The
project half of the same plugin walks `l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})`
(dump line 708687, offset 4574) — that is OC-1/OC-6 ground, not OC-2's class.

## F3 — the home half has no witness on v2.1.4 (sweep, not a loosened regex)

```
$ for a in 'X.join(r.home,".claude","CLAUDE.md")' 'join(A.home,".claude")' 'CLAUDE.md' 'CONTEXT.md'; do
    python3 -c 'import sys;d=open(sys.argv[1],errors="replace").read();print(d.count(sys.argv[2]))' oc-strings.txt "$a"; done
0
1
3
0
$ grep -n 'CLAUDE\.md' oc-strings.txt | cut -c1-160
20946:CLAUDE.md
150271:CLAUDE.md.cursor/rulesbun-blank-templatebun-react-templatebun-react-tailwind-template...
1228295:- existing instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, ...)
```

The three `CLAUDE.md` occurrences are (a) a bare symbol-table entry (line 20946, a lone string with no
caller), (b) a concatenated template/asset blob (line 150271), (c) prompt prose in a doc string
(line 1228295). **None is a loader.** The one surviving `.claude` join takes two arguments and no
`.md`:

```
$ sed -n '708352p' oc-strings.txt | cut -c25970-26030
join(A.home,".claude")),h=[...i?[i]:[],a],S=yield*Q([...h,_,D
```

i.e. `.claude` is a **config-directory scope root** (`a=ke.make(A.config)`,
`_=ke.make(ze.join(A.home,".claude"))`), alongside its compatibility probe at line 708355
(`compatibility:()=>WH({claude:D$(V.claude,e.isDir),agents:D$(V.agents,e.isDir)})`). Neither reads an
instruction file. So the behaviour the round-14 home anchor witnessed (a user-level
`.claude/CLAUDE.md` instruction candidate) is **gone from v2.1.4**, not merely renamed.

## F4 — the replacement rule (step 3)

Deliverables:

| path (under `.ufo/waves/round-72/w1/build/ExecOC2/`) | sha256 | what |
|---|---|---|
| `verify_surfaces.py` | `9944782a…` | base file with ONLY the OC-2 block replaced (94-line diff) |
| `rule.diff` | `3309247e…` | `diff -u verifiers/verify_surfaces.py build/ExecOC2/verify_surfaces.py` |
| `fixtures/oc2-v2.1.4-anchor.txt` | — | 5 verbatim slices of dump line 708687 (offsets in comments) |
| `fixtures/oc2-v2.1.4-decoy-moved.txt` | — | the same slices re-ordered: join inside `location-watcher` |
| `probe_oc2.py` | — | prints the OC-2 report row for base vs scratch on any dump/fixture |
| `make_decoys.py` | — | rebuilds the three decoys from a real dump (each breaks one binding) |

The rule (verbatim from the diff): plugin anchor `id:"opencode.config.instruction"`; window from that
anchor to the next `({id:"opencode.` (or EOF — no arbitrary byte window, so a moved join cannot be
swallowed); inside the window require `c("ConfigInstructionPlugin.globalSource")` and a call
`<join>(<v>.config,"<name>.md")` where `<join>` is an alias declared by
`import …{… join as <join> …} from"path"`. It derives `opencode:config/<name>`; when nothing matches
it falls back to `owns ["opencode:config/AGENTS.md"]` so the FAIL message still names the class.
`OC_HOME_DIR_JOIN_RE` is deleted (`grep -n OC_HOME_DIR_JOIN_RE` on the scratch copy → no reference).

Anchor vs decoy fixture, complete output (both modules loaded, OC-2 report row only):

```
$ python3 -B probe_oc2.py fixtures/oc2-v2.1.4-anchor.txt fixtures/oc2-v2.1.4-decoy-moved.txt
oc2-v2.1.4-anchor.txt              base OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
oc2-v2.1.4-anchor.txt              new  OC-2 matched=True owns=['opencode:config/AGENTS.md'] missing=[]
oc2-v2.1.4-decoy-moved.txt         base OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
oc2-v2.1.4-decoy-moved.txt         new  OC-2 matched=False owns=['opencode:config/AGENTS.md'] missing=['id:"opencode.config.instruction"', 'c("ConfigInstructionPlugin.globalSource")', 'X(<v>.config,"AGENTS.md") where X is imported as join from "path"']
```

Decoys on the **live dump bytes** (28 MB copies built by `make_decoys.py` in a scratch dir, mutated
there only), complete output:

```
$ python3 -B make_decoys.py oc-strings.txt .
wrote ./decoy-a-moved.txt 28835408 bytes
wrote ./decoy-b-callee.txt 28835401 bytes
wrote ./decoy-c-method.txt 28835411 bytes
$ python3 -B probe_oc2.py oc-strings.txt decoy-a-moved.txt decoy-b-callee.txt decoy-c-method.txt
oc-strings.txt                     base OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
oc-strings.txt                     new  OC-2 matched=True owns=['opencode:config/AGENTS.md'] missing=[]
decoy-a-moved.txt                  base OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
decoy-a-moved.txt                  new  OC-2 matched=False owns=['opencode:config/AGENTS.md'] missing=['id:"opencode.config.instruction"', 'c("ConfigInstructionPlugin.globalSource")', 'X(<v>.config,"AGENTS.md") where X is imported as join from "path"']
decoy-b-callee.txt                 base OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
decoy-b-callee.txt                 new  OC-2 matched=False owns=['opencode:config/AGENTS.md'] missing=['id:"opencode.config.instruction"', 'c("ConfigInstructionPlugin.globalSource")', 'X(<v>.config,"AGENTS.md") where X is imported as join from "path"']
decoy-c-method.txt                 base OC-2 matched=False owns=['opencode:config/AGENTS.md'] missing=['X.join(<v>.config,"AGENTS.md")', 'X.join(<v>.home,".claude","CLAUDE.md")']
decoy-c-method.txt                 new  OC-2 matched=False owns=['opencode:config/AGENTS.md'] missing=['id:"opencode.config.instruction"', 'c("ConfigInstructionPlugin.globalSource")', 'X(<v>.config,"AGENTS.md") where X is imported as join from "path"']
```

Read the two base rows carefully: the committed rule fails every decoy only because its **home** half
is absent (`bool(cfg) and bool(home)`), not because it is role-aware. On `decoy-c-method.txt` its
`owns` collapses to the single config class — i.e. its cfg half *did* fire — and the direct regex
call proves what it accepted:

```
$ python3 -c "import sys;sys.path.insert(0,'verifiers');import verify_surfaces as v;d=open('<scratch>/decoy-c-method.txt',errors='replace').read();print(v.OC_CONFIG_JOIN_RE.findall(d), v.OC_HOME_DIR_JOIN_RE.findall(d))"
['AGENTS.md'] []
```

So `decoy-c-method.txt` is a shape the committed rule accepts on a plugin with no instruction-loading
role; the replacement rejects all three decoys (`decoy-a-moved.txt` is the "same tokens, no
instruction-loading role" case, also shipped as `fixtures/oc2-v2.1.4-decoy-moved.txt`).

## F5 — the scratch copy run (step 4)

The shared dump path is gone, so I passed the regenerated dump (same sha256) instead of
`/tmp/k72-oc-strings.txt`. The literal command from the ticket exits 3 because the scratch copy's
`DEFAULT_REPO` is its grandparent:

```
$ cd .ufo/waves/round-72/w1/build/ExecOC2
$ python3 -B verify_surfaces.py --opencode-strings <scratch>/oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
ERROR baseline not found: .../w1/build/verifiers/surfaces-baseline.json
exit=3
```

With `--repo` naming the lane root (the same run, 14.6 s wall):

```
$ python3 -B verify_surfaces.py --repo <lane> --opencode-strings <scratch>/oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/instructions, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-1 (owns opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md; missing ["AGENTS.md" … "CONTEXT.md"] + disableClaudeCodePrompt); OC-3a (owns opencode:config/instructions; missing for(let <v> of <v>.instructions)); OC-3b (owns opencode:config/instructions-remote; missing .instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://")) + Instructions from: ); OC-4 (owns opencode:read-hook/instructions; missing Instruction.resolve exported as .resolve + ReadTool.execute calls .resolve(messages, path, id) + <system-reminder> wraps the resolved content); OC-5 (owns no class id (shape witness); missing OPENCODE_DISABLE_PROJECT_CONFIG + globUp(<v>.directory,<v>.worktree) + globUp(<v>.config,<v>.config)); OC-6 (owns opencode:instruction-context/AGENTS.md; missing core/instructions key + InstructionContext.observe AGENTS.md walk + instruction-context layer registered under system-context-builtins)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
exit=1
```

Read it exactly: **OC-2 is absent from both the "produced by no rule" and "matched nothing" lists**,
`opencode:config/AGENTS.md` is no longer a missing class, and the vacuity sentence is gone
(extraction is now 8 classes from 7 rules, 6 of them unmatched — OC-1/3a/3b/4/5/6, other seats'
ground). `opencode:claude-home/CLAUDE.md` is the single OC-2-owned class still named — the ledger
candidate of F8.

The committed script on the same bytes, same flags, for the before column:

```
$ python3 -B verifiers/verify_surfaces.py --repo <lane> --opencode-strings <scratch>/oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s); … 0 extracted classes with 9 declared …; … OC-2 (owns opencode:config/AGENTS.md, opencode:claude-home/CLAUDE.md; missing X.join(<v>.config,"AGENTS.md") + X.join(<v>.home,".claude","CLAUDE.md")); …
```

## F6 — self-test consequence the integration owner must absorb

`--self-test` on the scratch copy (fixtures resolved through a symlink to the committed
`verifiers/fixtures`, read-only) vs the base file:

```
$ python3 -B verifiers/verify_surfaces.py --self-test   # base, run from the lane root
0 failure(s) over 175 assertions                  # exit 0
$ python3 -B verify_surfaces.py --self-test      # scratch copy
self-test FAIL: clean: exit 0: got 1
self-test FAIL: clean: PASS surfaces.opencode_extract: got '…FAIL surfaces.opencode_extract: … OC-2 (owns opencode:config/AGENTS.md; missing id:"opencode.config.instruction" + …)…'
self-test FAIL: new-callees: exit 0: got 1
self-test FAIL: oc-1.19.4 anchors: exit 0: got 1
self-test FAIL: oc-1.19.4 anchors: PASS opencode_extract: got '…'
self-test FAIL: oc-extra: exit 0: got 1
6 failure(s) over 175 assertions                  # exit 1
```

The `got '…'` payloads are the subprocess 7-line check tables; the bytes dropped from those two
assertion lines are exactly the table reproduced in F5 (the `clean` / `oc-1.19.4 anchors` runs differ
only in the omp dump and the OC-2 `owns` line). One cause, not six: **every** opencode fixture still carries the round-14 pair on one line
(`grep -n 'join(.*\.config,"AGENTS.md"' verifiers/fixtures/surfaces/*.txt` → 14 files, e.g.
`strings-opencode-clean.txt:11: n=[X.join(r.config,"AGENTS.md"),...!t.disableClaudeCodePrompt?[X.join(r.home,".claude","CLAUDE.md")]:[]]`).
Two omp arms (`clean`, `new-callees`) fail only because they reuse that opencode dump. This is the
generation rule the self-test already enforces for v2.0.26 (`oc-gen`): once the rule set is
re-derived on v2.1.4, the 1.19.x fixtures become old-generation must-fail fixtures and the matrix
needs v2.1.4-shaped replacements for **all** rules — a single integration task, not an OC-2 edit. My
two fixtures are the OC-2-shaped starting points. `strings-opencode-drop-oc2.txt` still passes (its
arm asserts exit 1 + FAIL + a named class, and the parity FAIL names the declared classes).

## F7 — census disposition (proposal, not a loosened rule)

`opencode:claude-home/CLAUDE.md` is **removed with reason** on v2.1.4:

- census ledger row (append-only table at `corpus/knowledge/instruction-surface-census-round13.md:313-324`,
  the row today reads `| opencode:claude-home/CLAUDE.md | historical | resurrected | X.join(r.home,".claude","CLAUDE.md") 1 |`, line 318):
  new round-72 row → `retired (v2.1.4)`, anchor `X.join(r.home,".claude","CLAUDE.md")` **0**,
  `CLAUDE.md` 3 (symbol table 20946, template blob 150271, prompt prose 1228295 — none a loader),
  `.claude` 1 (config-scope root, two-arg join at 708352).
- `verifiers/census-removals.json` entry recording `class_id`, `literal: "CLAUDE.md"`, `context_kind:
  "loader-config"`, the base `verdict: "governed"`, `removed_at`, `reason` naming the two surviving
  non-loader roles and the absent three-arg join, and `evidence` the counts above (do not invent a
  `verdict: "removed"` value — the baseline's verdict domain is `governed`/`excluded`).
- `opencode:config/AGENTS.md` is `retained, re-anchored`: `X.join(r.config,"AGENTS.md")` **0** →
  `id:"opencode.config.instruction"` **1** + `j1(r.config,"AGENTS.md")` **1** (same shape as the
  existing line 311 row).

## Before → after (same bytes, same flags)

| measurement | base `c69711e` script | scratch copy |
|---|---|---|
| OC-2 rule matched | False | True |
| classes derived by OC-2 | 0 | 1 (`opencode:config/AGENTS.md`) |
| opencode extraction | 0 classes / 7 rules (vacuity) | 8 classes / 7 rules, 6 unmatched |
| `surfaces.opencode_extract` reason | vacuity + all 9 declared missing | 8 declared missing, OC-2 not named as unmatched |
| surfaces checks | 5 PASS / 2 FAIL | 5 PASS / 2 FAIL (same two checks; opencode_extract composition changed) |
| self-test | 0 failures / 175 | 6 failures / 175 (F6, one generation cause) |
| decoys rejected (3 live-dump decoys) | 0 / 3 as a whole rule (its home half is absent, but it accepts decoy-c's config half) | 3 / 3 |

## Risks / blockers

- **B1 (C2 owner, before data).** Plan:124-127 freezes the ledger conjunct as *literal* absence:
  "the ledger must equal **exactly** the set of base classes whose literal the counter finds absent …
  a present literal cannot be ledgered". `CLAUDE.md` is present 3x (F3), so ledgering
  `opencode:claude-home/CLAUDE.md` under that wording **fails the conjunct by construction**, and
  leaving it declared `governed` fails `surfaces.opencode_extract` (F5). The conjunct needs a
  witness-absence key (the class's *loader shape* absent — three-arg `.home,.claude,<file>.md` 0,
  and the two surviving `.claude` sites are non-loaders), decided before any seat scores C2.
- **B2 (integration).** The fixture matrix is single-generation; it must be re-derived wholesale on
  v2.1.4 when OC-1/3/4/5/6 land (F6). Landing OC-2 alone leaves `--self-test` red at 6/175.
- **B3.** The scratch copy cannot pass `opencode_extract` alone: 6 other rules are unmatched on
  v2.1.4 by their own seats' accounts. C2's `p == 7` target therefore depends on all seven, and the
  Q45 census must count OC-2 as **passable** (it is) — I did not lower anything.

## Hygiene record

- Committed lane files untouched (`git -C <lane> status --porcelain` shows only `.ufo/waves/…`).
  `git diff --stat c69711e -- verifiers/verify_surfaces.py verifiers/surfaces-baseline.json` → empty,
  so the base file I diffed against is the frozen base; lane tip while working was `e61fd29` (wave-1
  spec commit).
- Two self-corrected slips, both reverted inside the same minute and verified gone:
  (a) three decoy dumps were written to the **fleet root** by a `python3 decoys.py` with no `cwd`
  (`/home/vgpnk/Projects/shokunin/decoy-{a-moved,b-callee,c-method}.txt`) → `mv` into the scratch
  dir; (b) the two fixtures were first written through a `fixtures → verifiers/fixtures` symlink and
  landed in the committed `verifiers/fixtures/` → symlink removed, files moved to
  `build/ExecOC2/fixtures/`, `git status` shows no `verifiers/` entry. No tracked byte was modified
  at any point.
- Three scratch dirs under `/tmp/k72w1-ExecOC2*` (28 MB dumps, the decoy copies, probe runs, run
  logs) were deleted before this report was filed; the shipped `probe_oc2.py` + `make_decoys.py` +
  two fixtures reproduce every measurement without them.
- `verifiers/__pycache__/` (git-ignored, `__pycache__/` at `.gitignore:2`) is refreshed by importing
  `verifiers/verify_surfaces.py` in-process; it carries no tracked byte and I left it in place rather
  than race the seats importing the same module.
