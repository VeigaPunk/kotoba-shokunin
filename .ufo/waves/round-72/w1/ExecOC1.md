# ExecOC1 — OC-1 re-derivation on opencode v2.1.4

**Verdict.** OC-1 as committed cannot be re-derived on the v2.1.4 bytes: the name-priority array it was
written to witness is gone — `CONTEXT.md` occurs **0** times in the dump, `disableClaudeCodePrompt`
occurs **0** times, and `CLAUDE.md` survives only in prompt prose and string tables with no loader role.
What the rule *owned* still exists as a **single-name** target list inside
`ConfigInstructionPlugin.projectSource`, so I re-derived OC-1 to that surviving witness (it derives
`opencode:instructions/AGENTS.md`, rejects three same-token decoys, and still grows when a second name
is planted) and I propose **census removals, not a loosened regex**, for
`opencode:instructions/CONTEXT.md` and `opencode:instructions/CLAUDE.md`. Scratch copy result:
**5 of 7 checks PASS, 2 FAIL** — both FAILs are baseline/ledger work owned by C2, not by OC-1.

Read-only throughout: no committed lane file was touched (`git status --porcelain` shows only the
pre-existing untracked `.ufo/waves/round-72/` entries). Deliverables are drafts under
`.ufo/waves/round-72/w1/build/ExecOC1/`; the L1 is the integration owner.

---

## 1. The rule as committed, run on the v2.1.4 dump — it matches nothing

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B - /tmp/k72-oc-strings.txt <<'PY'
import importlib.util, json
spec = importlib.util.spec_from_file_location("vs", "verifiers/verify_surfaces.py")
vs = importlib.util.module_from_spec(spec); spec.loader.exec_module(vs)
dump = open("/tmp/k72-oc-strings.txt", encoding="utf-8", errors="replace").read()
print("OC_PRIORITY_RE.search ->", vs.OC_PRIORITY_RE.search(dump))
print("OC_GATE count:", dump.count(vs.OC_GATE))
ids, report = vs.extract_opencode_classes(dump)
for r in report: print(" ", r["rule_id"], "matched=%s" % r["matched"], "owns=%s" % r["owns"])
print("ids:", sorted(ids))
PY
```

Observed (dump: 28,835,401 bytes, 1,237,844 lines, sha256 `020fb253…`):

```
dump bytes: 28835401 lines: 1237844
OC_PRIORITY_RE.search -> None
OC_GATE 'disableClaudeCodePrompt' count: 0
OC_MD_NAME_RE literals in whole dump: ['AGENTS.md', 'README-demo.md', 'README.md', 'SKILL.md']
   OC-1 matched=False owns=['opencode:instructions/AGENTS.md', 'opencode:instructions/CLAUDE.md', 'opencode:instructions/CONTEXT.md']
   OC-2 matched=False owns=['opencode:config/AGENTS.md', 'opencode:claude-home/CLAUDE.md']
   OC-3a matched=False owns=['opencode:config/instructions']
   OC-3b matched=False owns=['opencode:config/instructions-remote']
   OC-4 matched=False owns=['opencode:read-hook/instructions']
   OC-5 matched=False owns=[]
   OC-6 matched=False owns=['opencode:instruction-context/AGENTS.md']
ids: []
```

This is the "expected: nothing" of the item, and it is also the base state C2 must lower or fix: all 7
rules are unmatched and the extraction is 0 classes (the CLI reports it as vacuity, §4).

## 2. The v2.1.4 form of what OC-1 was written to witness

The 1.19.x shape the committed rule encodes (`["AGENTS.md", …!t.disableClaudeCodePrompt?["CLAUDE.md"]:[],
"CONTEXT.md"]`) has no counterpart. The per-directory instruction candidate set of the **same loader**
is now built from one name, and the gate that admitted `CLAUDE.md` is gone. All quotes below are pasted
from `sed -n '<L>p' /tmp/k72-oc-strings.txt | cut -c<a>-<b>`; the bytes dropped are named per quote.

**Q1 — the loader wrapper and its walk-up target list** (dump line 708687, chars 4482–4639; dropped:
the preceding plugin-registration tail `e]:[]}),ze=` and the remainder of the line):

```
c("ConfigInstructionPlugin.projectSource")(function*(){if(!C)return[];let we=yield*Q(yield*l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"}),l.resolve)
```

**Q2 — the global config join** (line 708687, chars 3647–3689; dropped: the two neighbouring
assignments `…V=Ce.contains(O,T)?O:N,` before and `,Y={current:…` after):

```
D=yield*l.resolve(j1(r.config,"AGENTS.md"))
```

**Q3 — the project candidate map** (line 708687, chars 3820–3856; dropped: the enclosing
`ge=[...a.global?[D]:[],...C?` and the trailing `.filter((we)=>a.global||we!==D):[]`):

```
Q1(T,V).map((we)=>j1(we,"AGENTS.md"))
```

That is the whole name set: one name, in one array. The three names the old array derived are disposed
of as follows, each measured on the same dump:

```
$ for t in 'CONTEXT\.md' 'disableClaudeCodePrompt' 'CLAUDE\.md' 'AGENTS\.md'; do
    printf '%-26s %s\n' "$t" "$(grep -c "$t" /tmp/k72-oc-strings.txt)"; done
CONTEXT\.md                0
disableClaudeCodePrompt    0
CLAUDE\.md                 3
AGENTS\.md                 13
```

- `CONTEXT.md` — **0 occurrences**: the literal is absent from the binary, so the class
  `opencode:instructions/CONTEXT.md` has no bytes to witness. `check_literal_present` already says so
  (§4: `literal 'CONTEXT.md' absent from opencode dump`).
- `disableClaudeCodePrompt` — **0 occurrences**: the gate term the rule carried had already reduced to
  `m is not None` (the file's own LIMITS note says this); there is nothing left to gate.
- `CLAUDE.md` — 3 occurrences, **none a loader**:
  - line 20946, a bare string-table entry between `I32And` and `location.heap().kind() != World`
    (a JS engine's string table);
  - line 150271, a concatenated string-table blob `CLAUDE.md.cursor/rulesbun-blank-template…` (template
    names, not paths);
  - line 1228295, init-prompt prose — Q5 (chars 1–140, nothing dropped, 8 words):

    ```
    - existing instruction files (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`)
    ```

  The `.claude` dot-directory still exists in v2.1.4, but as a **skills/agents directory walk**, not as
  OC-2's `.claude/CLAUDE.md` home join — Q6 (line 708352, chars 25983–26130; dropped: the preceding
  `ze.join(A.home,` and the remainder of the line):

  ```
  .claude")),h=[...i?[i]:[],a],S=yield*Q([...h,_,D],(N)=>e.resolve(N)),l=yield*e.resolve(r.directory),F=S.slice(0,h.length).includes(l)||H?.project===
  ```

  (the same walk lists `[".claude",".agents",".opencode",…]` at line 708352 col 26264; `OC_HOME_DIR_JOIN_RE`
  finds 0 matches, i.e. no `.claude/CLAUDE.md` join anywhere.)

**Sweep command for "is the behaviour witnessed in the bytes"** (the honest-derivation test, one line):

```
$ python3 -B - <<'PY'
import re
d=open('/tmp/k72-oc-strings.txt',encoding='utf-8',errors='replace').read()
for pat in (r'\["AGENTS\.md".{0,400}?"CONTEXT\.md"', r'disableClaudeCodePrompt',
            r'j1\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"[A-Za-z0-9_.-]+\.md"\s*\)',
            r'\.up\(\{targets:\[(?:"[A-Za-z0-9_.-]+\.md",?)*\]'):
    print(pat, "->", len(re.findall(pat, d)))
PY
\["AGENTS\.md".{0,400}?"CONTEXT\.md" -> 0
disableClaudeCodePrompt -> 0
j1\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"[A-Za-z0-9_.-]+\.md"\s*\) -> 1
\.up\(\{targets:\[(?:"[A-Za-z0-9_.-]+\.md",?)*\] -> 1
```

So: the *priority list* behaviour is gone; the *per-directory walk of a name set* survives with one
member. That is why the replacement is a re-derivation to the surviving shape plus a removal ledger for
the two names the shape no longer carries — not a regex loosened until it matches.

## 3. The replacement rule and its decoy rejection

Draft: `.ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py` (full copy of the committed verifier,
OC-1 only), diff: `…/ExecOC1/rule.diff` (84 lines, 2 hunks, only the OC-1 comment/limits block and the
OC-1 rule application; `OC_PRIORITY_RE` and `OC_GATE` are deleted, not aliased — clean cutover).

```
$ diff -u --label a/verifiers/verify_surfaces.py \
       --label b/.ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py \
       verifiers/verify_surfaces.py .ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py > rule.diff
$ wc -l rule.diff
84 .ufo/waves/round-72/w1/build/ExecOC1/rule.diff
```

The rule:

```python
OC_LOADER_SOURCE_RE = re.compile(
    r'c\("ConfigInstructionPlugin\.projectSource"\)'
    r'\(function\*\(\)\{[^{}]{0,300}?\.up\(\{targets:\['
    r'(?P<targets>"[A-Za-z0-9_.-]+\.md"(?:,"[A-Za-z0-9_.-]+\.md")*)\]'
)
OC_LOADER_CONFIG_JOIN_RE = re.compile(
    r'j1\(\s*[A-Za-z_$][A-Za-z0-9_$]*\.config\s*,\s*"(?P<file>[A-Za-z0-9_.-]+\.md)"\s*\)'
)
OC_LOADER_REGION = 4000
```

```python
    walk = OC_LOADER_SOURCE_RE.search(dump)
    names = sorted(set(OC_MD_NAME_RE.findall(walk.group("targets")))) if walk else []
    region = (dump[max(0, walk.start() - OC_LOADER_REGION):walk.end()]
              if walk is not None else "")
    joined = set(OC_LOADER_CONFIG_JOIN_RE.findall(region))
    owns = (["opencode:instructions/%s" % n for n in names] if names else
            ["opencode:instructions/AGENTS.md"])
    rule("OC-1", owns,
         walk is not None and bool(names) and bool(joined & set(names)),
         ['ConfigInstructionPlugin.projectSource -> up({targets:["*.md"],…})',
          'j1(<v>.config,"*.md") in the same plugin region'])
```

Derivation is preserved: **every** `*.md` literal inside the target array becomes a class id, so a name
planted into the list still surfaces (the planted-name arm below). The rule is fail-closed: an absent
wrapper or an absent same-name config join leaves OC-1 unmatched and names both anchors as missing. The
gate term is dropped *with the gate it named* (0 occurrences), and that fact is recorded in the rule's
comment rather than silently deleted.

Probe (`.ufo/waves/round-72/w1/build/ExecOC1/oc1_probe.py`, run on the real dump and on decoys):

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecOC1/oc1_probe.py \
      .ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py /tmp/k72-oc-strings.txt
== real dump: /tmp/k72-oc-strings.txt ==
OC_LOADER_SOURCE_RE span: (21499158, 21499276)
config-join names in region: ['AGENTS.md']
derived target names: ['AGENTS.md']
OC-1 row: {'rule_id': 'OC-1', 'owns': ['opencode:instructions/AGENTS.md'], 'matched': True}

== decoy A: ReadTool default name, dump line 708708 (same literal, no loader role) ==
bytes at col 11988: 'path";var OF="read",LF="AGENTS.md",$F=o({path:t.an'
OC-1 row: {'owns': ['opencode:instructions/AGENTS.md'], 'matched': False}

== decoy B: same tokens, bare walk with no loader wrapper ==
bytes: function q(){return l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})};D=l.resolve(j1(r.config,"AGENTS.md"))
OC-1 row: {'owns': ['opencode:instructions/AGENTS.md'], 'matched': False}

== decoy C: same tokens under a different plugin wrapper ==
bytes: c("OtherPlugin.projectSource")(function*(){if(!C)return[];let we=yield*Q(yield*l.up({targets:["AGENTS.md"],start:T,stop:V,type:"file"}),l.resolve)});D=l.resolve(j1(r.config,"AGENTS.md"))
OC-1 row: {'owns': ['opencode:instructions/AGENTS.md'], 'matched': False}

== growth: real loader region with a second name planted ==
OC-1 row: {'owns': ['opencode:instructions/AGENTS.md', 'opencode:instructions/CLAUDE.md'], 'matched': True}
planted name surfaces: True
```

- **Decoy A** is the real decoy the item asks for: `var OF="read",LF="AGENTS.md"` (line 708708, chars
  11975–12008, dropped bytes: the surrounding `import{basename as S0,dirname as rr,join as F0}from"path";`
  and `$F=o({path:t.annotate({…`) — the same literal `AGENTS.md`, the ReadTool's default file name, no
  instruction-loading role. Rejected.
- **Decoy B** carries the *exact* witness tokens (`up({targets:["AGENTS.md"],start:T,stop:V,type:"file"})`
  plus the config join) but outside any loader wrapper. Rejected — so the wrapper is load-bearing, not
  decorative.
- **Decoy C** puts the same tokens under a differently-named plugin. Rejected — the anchor names the
  plugin.
- **Growth** reuses the real 4,000-byte loader region with `targets:["AGENTS.md","CLAUDE.md"]` planted:
  the second name surfaces as a class id, so a future upstream that restores the array cannot slip
  through as a witness-only pass.

## 4. Scratch copy run with the item's flags

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && python3 -B \
    .ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py --repo . \
    --opencode-strings /tmp/k72-oc-strings.txt \
    --omp-binary /home/vgpnk/.local/bin/omp.real
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-2 (owns opencode:config/AGENTS.md, opencode:claude-home/CLAUDE.md; missing X.join(<v>.config,"AGENTS.md") + X.join(<v>.home,".claude","CLAUDE.md")); OC-3a (owns opencode:config/instructions; missing for(let <v> of <v>.instructions)); OC-3b (owns opencode:config/instructions-remote; missing .instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://")) + Instructions from: ); OC-4 (owns opencode:read-hook/instructions; missing Instruction.resolve exported as .resolve + ReadTool.execute calls .resolve(messages, path, id) + <system-reminder> wraps the resolved content); OC-5 (owns no class id (shape witness); missing OPENCODE_DISABLE_PROJECT_CONFIG + globUp(<v>.directory,<v>.worktree) + globUp(<v>.config,<v>.config)); OC-6 (owns opencode:instruction-context/AGENTS.md; missing core/instructions key + InstructionContext.observe AGENTS.md walk + instruction-context layer registered under system-context-builtins)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
exit=1
```

`--repo .` is required only because the draft sits outside `verifiers/` (the script's default repo is its
own grandparent); every other flag is exactly the item's. Per-check reading:

| check | scratch | why |
|---|---|---|
| `literal_present` | FAIL | baseline still declares `opencode:instructions/CONTEXT.md`; the ledger removal is C2's |
| `no_uncovered_class` | PASS | omp half unaffected |
| `opencode_extract` | FAIL | **OC-1 is no longer in the "matched nothing" list and now produces 1 class**; the 8 remaining declared classes belong to OC-2…OC-6, untouched by this seat |
| `table_parity` / `literal_parity` / `kind_parity` / `excluded_reason` | PASS | inventory untouched |

Committed verifier on the same flags for contrast (`python3 -B verifiers/verify_surfaces.py --repo . …`):
same 5 PASS / 2 FAIL, but its `opencode_extract` additionally reports
`vacuity: extraction produced 0 class(es) from 7 rule(s)` and lists `OC-1 (owns …; missing ["AGENTS.md" …
"CONTEXT.md"] + disableClaudeCodePrompt)` among the unmatched rules. The replacement removes the
vacuity for OC-1's half and leaves the honest remainder visible.

## 5. What this does **not** fix (measured, so the L1 is not surprised)

**a) The lane's own self-test.** The OC-1 arms are pinned to the 1.19.x array. Run in a `--shared`
clone with the draft at `verifiers/verify_surfaces.py` (so `FIXTURES` resolves):

```
$ C=$(mktemp -d /tmp/k72oc1clone.XXXX) && git clone --shared -q <lane> "$C/kotoba-shokunin" \
  && cp .ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py "$C/kotoba-shokunin/verifiers/verify_surfaces.py" \
  && cd "$C/kotoba-shokunin" && python3 -B verifiers/verify_surfaces.py --self-test
self-test FAIL: clean: exit 0: got 1
self-test FAIL: clean: PASS surfaces.opencode_extract: got '…FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:instructions/AGENTS.md, …'
self-test FAIL: new-callees: exit 0: got 1
self-test FAIL: oc-1.19.4 anchors: exit 0: got 1
self-test FAIL: oc-1.19.4 anchors: PASS surfaces.opencode_extract: got '…'
self-test FAIL: oc-extra: exit 0: got 1
self-test FAIL: oc-planted-name: names opencode:instructions/GUIDE.md undeclared: got '…'
7 failure(s) over 175 assertions
self-test exit=1 wall_ms=73
```

Consequence for integration: the four fixtures `strings-opencode-clean.txt`,
`strings-opencode-1.19.4-anchors.txt`, `strings-opencode-extra.txt`,
`strings-opencode-planted-name.txt` encode the retired array, and the `strings-opencode-drop-oc1.txt`
arm now passes for the wrong reason (it sees `CONTEXT.md` in the *"produced by no rule"* list, not in
OC-1's missing-anchor list). The lane's own precedent (round 47, `strings-opencode-v2.0.26.txt`) says a
retired generation survives as a **must-fail generation fixture**; the same move applies here: re-pin
`clean`/`extra`/`planted-name` to 2.1.4-shaped bytes, add a `strings-opencode-2.1.4.txt` fixture, keep
the 1.19.x array fixture as a must-fail generation arm, and re-target the `drop-oc1` arm at OC-1's new
anchor pair. That fixture work is integration, not this seat's file scope.

**b) The census disposition for the two lost ids** — proposal, with the exact reasons:

```json
{"class_id": "opencode:instructions/CONTEXT.md", "literal": "CONTEXT.md",
 "reason": "literal absent from the opencode v2.1.4 dump (strings -n 4 count 0); the name-priority array that carried it is gone"}
```

For `opencode:instructions/CLAUDE.md` (and its OC-2 twin `opencode:claude-home/CLAUDE.md`) the removal
ledger **cannot** be used under C2's frozen conjunct: the counter requires the ledger to equal exactly
the set of base classes whose literal it finds **absent**, and `CLAUDE.md` is present 3 times. Present
literal ⇒ cannot be ledgered; no rule produces it ⇒ cannot stay `governed`. The honest third
disposition, and my recommendation: re-kind the two `CLAUDE.md` rows to `prompt-text` with verdict
`excluded` and the reason above ("loader role gone in 2.1.4; the literal survives only in the init
prompt and string tables"). That keeps the literal in the census (a future loader cannot reappear
unnoticed), passes `check_literal_present` (which skips non-loader kinds), and satisfies C2's exact-set
conjunct. **This is a C2 decision, not an OC-1 one; flagging it because my measurement is what exposes
it.**

## 6. Risks / blockers

1. **The shared dumps vanished mid-seat.** At 18:36 `/tmp/k72-oc-strings.txt` (and the omp dump) were
   absent while this seat was running; I regenerated from `/home/vgpnk/.opencode/bin/opencode`
   (sha256 `ca9b3ee2…`, matches the plan) with `strings -n 4` in **904 ms** and got byte-identical bytes
   (sha256 `020fb253…`, 28,835,401 bytes). The shared path was repopulated by another seat before I
   could restore it; my scratch copy is the same sha. Seats that assumed the file was stable should
   re-verify the sha, not the path.
2. **C2's ledger conjunct vs. a present-but-roleless literal** (§5b) — unresolved by OC-1 and needs the
   C2 owner's decision before data.
3. **Self-test re-pin** (§5a) — landing the OC-1 diff without the fixture work turns the lane's own
   self-test red (7 assertions).
4. No blocker on the OC-1 derivation itself: real witness matched, three decoys rejected, growth proven,
   per-check output pasted.

## 7. Files and process

- Drafts (deliverable): `.ufo/waves/round-72/w1/build/ExecOC1/verify_surfaces.py` (scratch copy, OC-1
  only), `.ufo/waves/round-72/w1/build/ExecOC1/rule.diff` (84-line diff vs the committed file),
  `.ufo/waves/round-72/w1/build/ExecOC1/oc1_probe.py` (decoy/growth probe, reusable).
- Scratch `/tmp/k72w1-ExecOC1.QLzj` and the `--shared` clone `/tmp/k72oc1clone.smGe`: deleted before
  returning (see the seat's closing commands). No git write was made anywhere; the clone was read-only
  apart from the copied draft file inside it.
- Tooling: **no install or upgrade**. `strings` (binutils, already present) was the only binary run for
  data; wall times recorded above (dump 904 ms; committed+scratch CLI pair 31.5 s; probe 11.4 s;
  self-test 73 ms).
- No credential, session URL or `op://` reference is reproduced anywhere above.
