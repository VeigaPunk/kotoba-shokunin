# ExecOC3a — OC-3a re-derived on the opencode v2.1.4 bytes

**Verdict:** OC-3a **is honestly derivable** on the v2.1.4 bundle — the behaviour did not vanish, its shape
moved. The committed rule (`for(let O of T.instructions)`) matches **0** times on the live dump (its own
committed fixture still matches, so the rule is stale, not broken). The v2.1.4 loader is the
`opencode.config.instruction` plugin: the declared `instructions` list is read out of the config
documents, split by URL-ness with a named predicate, and every non-URL entry is handed to the plugin's
labelled `match` helper, which walks the filesystem (`globUp`). A replacement rule binding those five
conjuncts inside the plugin's own body matches the live bytes and **rejects four decoys**, including one
that keeps every chain token but assigns the loading role to a skills plugin. No census removal is
proposed for this class. The class count moved 0 → 1 for OC-3a; `surfaces.no_uncovered_class` now PASSes
on the live dump.

Base file identity: `verifiers/verify_surfaces.py` is **byte-identical** at the plan base and the current
tip — `git cat-file -p c69711ee…:verifiers/verify_surfaces.py | sha256sum` and `sha256sum
verifiers/verify_surfaces.py` both `4f13e3bd9d7c43b9e9d3b153b02e8f6ebb2ba57fcf66ac8ae82b9a053e809c21`;
`git diff --stat c69711e HEAD -- verifiers/verify_surfaces.py` is empty (HEAD `e61fd29`). The `rule.diff`
therefore applies to both.

## Shared-input note (affects every seat's citations)

The shared dumps named in the wave prompt were **gone mid-wave**. At 18:40 I read them (grep/`sed` over
`/tmp/k72-oc-strings.txt`); at 18:43 `ls -la /tmp/k72-oc-strings.txt /tmp/k72-omp-strings.txt` printed
`ls: cannot access … No such file or directory` for both. I did not delete them; I have no evidence which
process did. I re-derived the opencode dump myself and pinned it by hash:

```
strings -n 4 /home/vgpnk/.opencode/bin/opencode | sha256sum
020fb25393e5ce881ac2da70222acedebc5cef2d3810d07e4625b2cde885b089  -
```
That is the hash the wave prompt states for the shared dump, so my dump is the same bytes;
`wall=1s`, 1,237,844 lines, 28,835,401 bytes (scratch copy `oc-strings.txt`). The omp dump was not
needed: I passed `--omp-binary /home/vgpnk/.local/bin/omp.real` as the item specifies. **The L1 should
assume no `/tmp/k72-*-strings.txt` exists** when it re-runs the battery, and re-dump (the binary at
`~/.opencode/bin/opencode` is still present).

## Step 1 — the rule as committed, on the v2.1.4 bytes: nothing

```
$ python3 -c "import re; dump=open('/tmp/k72-oc-strings.txt',errors='replace').read(); print(len(re.findall(r'for\s*\(\s*let\s+[A-Za-z_$][A-Za-z0-9_$]*\s+of\s+[A-Za-z_$][A-Za-z0-9_$]*\.instructions\s*\)', dump)))"
0
```
(Re-run after re-deriving the dump, through the committed module itself rather than a copied pattern:)

```
$ python3 - <<'EOF'   # imports verifiers/verify_surfaces.py read-only, runs extract_opencode_classes(live)
...
COMMITTED OC-3a: {"rule_id": "OC-3a", "owns": ["opencode:config/instructions"], "matched": false,
 "anchors": ["for(let <v> of <v>.instructions)"], "missing": ["for(let <v> of <v>.instructions)"]}
COMMITTED ids: []
COMMITTED OC_DECLARED_RE.search: None
COMMITTED OC_REMOTE_FILTER_RE hits: 0
COMMITTED OC_REMOTE_RENDER present: True
```
Control that the pattern is live and only stale (not broken): the same committed regex on its committed
fixture matches —
```
$ ... m.OC_DECLARED_RE.search(open('verifiers/fixtures/surfaces/strings-opencode-clean.txt').read())
committed OC_DECLARED_RE on committed fixture: 'for(let O of T.instructions)' line 13
```
So the round-start reading `opencode extraction 0 classes from 7 rules` is confirmed, and OC-3a's arm is
the stale one, not an unreachable pattern.

## Step 2 — the v2.1.4 form of the same behaviour

All five anchors live in **one** dump line, `708687` (chunk line, 47,694 bytes); the plugin starts at dump
byte offset **21,497,967** and its body runs to the next plugin declaration `var VM=tt({id:"opencode.config.location-watcher"…`
at offset 21,502,194 (body 4,227 bytes). Quotes below are slices of that line; the bytes before/after
each slice were dropped.

| role | dump line / offset | located quote (≤25 words) |
|---|---|---|
| plugin id (name-bearing) | 708687 @ 21497967 | `id:"opencode.config.instruction"` |
| declared list read from config documents | 708687 @ 21500495 | `.flatMap((Re)=>Re.type==="document"?Re.info.instructions??[]:[])` |
| URL predicate, defined | 708687 @ 21502117 | `function E1(e){return URL.canParse(e)&&/^https?:$/.test(new URL(e).protocol)}` |
| split applied to the list (remote half) | 708687 @ 21500573 | `Ae.filter(E1)` |
| consumer loop, URLs skipped | 708687 @ 21499944 | `for(let ye of H.sources){if(E1(ye)){` |
| the `match` helper (labelled) | 708687 @ 21499490 | `ee=c("ConfigInstructionPlugin.match")` |
| filesystem walk inside `match` | 708687 @ 21499761 | `globUp(Ae,T,N)` |

Read as a chain (bytes between the slices elided, not paraphrased): `reconfigure` dedupes
`Re.info.instructions??[]` across config documents into `Ae`, fetches `Ae.filter(E1)` as the remote half
and keeps `H.sources=Ae`; `configuredSource` then iterates `H.sources`, skips `E1(ye)` (URL) entries into
the remote map, and passes every remaining entry to `ee` — `ConfigInstructionPlugin.match` — whose body
contains `globUp(Ae,T,N)` (and `scan` for absolute/`~/` paths) before `read` turns each resolved path
into `new p2({path,content})` (`InstructionDiscovery.File`). That is OC-3a's subject exactly: the declared
`instructions` list is consumed, its remote entries are not globbed, its local entries are.

For contrast (not my rule): the render literal of OC-3b survives at dump line 607084, offset 9,087,572,
`Instructions from: `.

## Step 3 — replacement rule, and the decoys it rejects

Deliverables (drafts; the L1 lands them):
- `.ufo/waves/round-72/w1/build/ExecOC3a/verify_surfaces.py` — scratch copy of the verifier with the new
  rule (sha256 differs from base only by the diff below; `rule.diff` is the whole delta).
- `.ufo/waves/round-72/w1/build/ExecOC3a/rule.diff` — 151 lines, `diff -u --label
  a/verifiers/verify_surfaces.py --label b/verifiers/verify_surfaces.py verifiers/verify_surfaces.py
  <scratch>`.
- `.ufo/waves/round-72/w1/build/ExecOC3a/fixtures/strings-opencode-v2.1.4.txt` — the plugin body lifted
  verbatim from dump line 708687 (verified: `fixture is a verbatim dump slice: True`; sha256
  `13899fb6a6520d3ff2f555d4e25841ea44e46231b80dca968e525075239b56c4`).
- `.ufo/waves/round-72/w1/build/ExecOC3a/fixtures/strings-opencode-v2.1.4-decoy.txt` — same-token decoy
  (sha256 `ae025bd1a47ad88dcf44f3ebca8760a0158f4ff7f4e2bfedf261f49785809331`).
- `.ufo/waves/round-72/w1/build/ExecOC3a/decoys/` — the four decoy bodies used below.

Rule design (`OC_DECLARED_PLUGIN_ID`, `OC_DECLARED_LIST_RE`, `OC_DECLARED_URL_PRED_RE`,
`OC_DECLARED_SPLIT_RE`, `OC_DECLARED_MATCH_LABEL`, `OC_DECLARED_GLOB_RE`, `OC_DECLARED_WINDOW`, and
`opencode_declared_list_matches(dump)`; OC-3a is now
`OC_DECLARED_RE.search(dump) is not None or opencode_declared_list_matches(dump)`). The v2.1.4 arm finds
the plugin id, bounds the window at the next `var X=tt({id:"…"` declaration (6,000-byte fallback), and
requires **all** of: the declared-list read; a `function` whose body is
`URL.canParse(v)&&/^https?:$/.test(new URL(v).protocol)`; that same captured name applied as
`.filter(NAME)`; a `.sources` loop whose `if(NAME(entry))` guard is followed (within 240 bytes) by
`for(let … of (yield*HELPER(entry))`; `HELPER=c("ConfigInstructionPlugin.match")`; and a three-argument
`globUp(...)`. Fail-closed: any missing conjunct returns False and the existing `rule()` reporting names
both arms as missing anchors.

The 1.19.x arm is **retained unchanged** on purpose: `fixtures/surfaces/strings-opencode-clean.txt:13`
carries it and both `verify_surfaces.py --self-test` and `check_opencode_repin.py`'s S/T arms run against
that fixture — the same generation-arm pattern OC-6 already uses for its committed 1.19.3 shape. This is
not a loosening of the v2.1.4 arm: the new arm is strictly additive, and the decoy below shows it is not
satisfied by tokens.

Decoy rejection (each decoy is a file; the probe imports the scratch module and calls
`extract_opencode_classes(<decoy text>)`):

| decoy | what it carries | OC-3a |
|---|---|---|
| `d1-token-soup.txt` | real dump regions: tree-sitter `DownloadUtils.downloadOrLoad` (`startsWith("http://")`/`("https://")`, `readFile`), the `McpInstructions` module, and the `FileSystem.globUp` symbol rows | **False** |
| `d2-skills-plugin.txt` | the real plugin body with `id:"opencode.config.instruction"` renamed to `opencode.config.skills` | **False** |
| `d3-no-glob.txt` | the real plugin body with `globUp(Ae,T,N)` → `walkUp(Ae,T,N)` | **False** |
| `d4-same-tokens-skills.txt` (primary) | **every** chain token (`info.instructions??[]`, `URL.canParse`, `.filter(`, `.sources`, `ConfigInstructionPlugin.match`, `globUp(`, and the literal `id:"opencode.config.instruction"`) — but the chain belongs to a skills plugin and the instruction id is a `yield*e.noop()` stub | **False** |

Observed probe output (live dump plus the four decoys, scratch module):
```
LIVE OC-3a: {"rule_id": "OC-3a", "owns": ["opencode:config/instructions"], "matched": true, ...}
LIVE all rules: [('OC-1', False), ('OC-2', False), ('OC-3a', True), ('OC-3b', False), ('OC-4', False), ('OC-5', False), ('OC-6', False)]
LIVE ids: ['opencode:config/instructions']
d1-token-soup.txt OC-3a matched: False | ids: []
d2-skills-plugin.txt OC-3a matched: False | ids: []
d3-no-glob.txt OC-3a matched: False | ids: []
fixtures/strings-opencode-v2.1.4.txt -> OC-3a matched: True ids: ['opencode:config/instructions']
decoys/d4-same-tokens-skills.txt -> OC-3a matched: False ids: []
```
(The six other rules reading False is the rest of the re-derivation — OC-1, OC-2, OC-3b, OC-4, OC-5, OC-6
are other seats' items; I did not touch them.)

Durable form of the decoy: the scratch copy also adds a self-test arm `(oc-214)` that reads both fixture
files, asserts the decoy still contains the six tokens, asserts the fixture matches, and asserts the decoy
does not — so the rule cannot silently rot into a token test.

## Step 4 — scratch copy run, per-check result

```
$ python3 -B .ufo/waves/round-72/w1/build/ExecOC3a/verify_surfaces.py \
    --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin \
    --opencode-strings /tmp/k72w1-ExecOC3a.9Dov/oc-strings.txt \
    --omp-binary /home/vgpnk/.local/bin/omp.real
exit=1 wall=17s
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions-remote, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-1 (…); OC-2 (…); OC-3b (…); OC-4 (…); OC-5 (…); OC-6 (…)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
```
`--json` on the same run: `exit_code: 1 pass: 5 fail: 2`; the `opencode_extract` detail's
"rule(s) matched nothing" list **does not contain OC-3a** (it contains OC-1, OC-2, OC-3b, OC-4, OC-5,
OC-6), and `no_uncovered_class` PASSes because `opencode:config/instructions` is now produced. The two
remaining FAILs are the other six rules' unmatched anchors plus the absent `CONTEXT.md` literal — not
OC-3a, and not fixed here.

`--repo` had to be passed explicitly: `DEFAULT_REPO` is `Path(__file__).parent.parent`, and the scratch
copy lives under `.ufo/waves/round-72/w1/build/ExecOC3a/`, so without it the baseline/inventory resolve
under the build directory.

## No-regression: the committed self-test

```
$ python3 -B verifiers/verify_surfaces.py --self-test            # lane, base bytes
0 failure(s) over 175 assertions          exit=0
$ python3 -B <scratch>/verifiers/verify_surfaces.py --self-test   # scratch + two fixtures
0 failure(s) over 183 assertions          exit=0
```
The base/scratch diff of the outputs is only the fixture-path prefix in the three expected-error arms.
183 > the recorded floor 175 for `surfaces` in `check_assertion_floors.py:209`, and the floors guard
fails only when the observed count is *below* the floor (`check_assertion_floors.py:6-7`), so no floor
re-record is needed. The existing arms `strings-opencode-drop-oc3a.txt` (must still FAIL and name
`opencode:config/instructions`) and `strings-opencode-1.19.4-anchors.txt` (must still PASS) both hold
inside that 183/0 run.

## Landing notes for the L1 (single integration owner)

1. Apply `build/ExecOC3a/rule.diff` to `verifiers/verify_surfaces.py`.
2. Copy the two `build/ExecOC3a/fixtures/*.txt` into `verifiers/fixtures/surfaces/`.
3. After landing, `verify_surfaces.py --opencode-strings <fresh dump> --omp-binary ~/.local/bin/omp.real`
   still reads `pass 5 fail 2` with only OC-3a landed: `opencode_extract` keeps FAILing while six rules
   produce nothing, and `literal_present` keeps FAILing on the absent `CONTEXT.md` literal (that absence
   is OC-1's and the C2 removal-ledger's item, not OC-3a's). `p == 7` arrives only when every seat's rule
   lands and the literal question is settled.
4. Do **not** re-pin the baseline: the class id, literal (`instructions`), kind (`loader-config`) and
   verdict (`governed`) are unchanged — only the witness shape moved, so `census-removals.json` gains no
   row for `opencode:config/instructions`.

## Risks and limits (stated, not papered over)

- The v2.1.4 arm's window boundary (`var X=tt({id:"`) and the `.sources` field name are bundle-shape
  facts, not language facts; the next opencode bump re-derives them, exactly as OC-4's call edge is
  re-derived per generation. If the plugin id or boundary disappears, the arm is False and the existing
  reporting names it (fail-closed) — verified by `d2`/`d4`.
- The arm proves *this* plugin consumes the declared list into the file walk; it does not prove the list
  is the only instruction channel (OC-1/OC-2/OC-4/OC-6 cover the others). That is the rule set's declared
  scope, unchanged.
- `OC_DECLARED_RE`'s 1.19.x arm still matches any `for(let x of y.instructions)` in any bundle — the
  pre-existing witness weakness, carried unchanged and reported as such.
- No census disposition (removal) is proposed: the behaviour is witnessed in the bytes, so a "class
  removed with reason" entry would be false.

## Evidence hygiene

- No committed lane file was modified: `git status --porcelain` shows only the four untracked wave paths
  (`snapshots/`, `w1.ready`, `w1.ready.dispatched`, `w1/`); `verifiers/verify_surfaces.py` sha equals
  `HEAD:verifiers/verify_surfaces.py`.
- Writes went only to `.ufo/waves/round-72/w1/build/ExecOC3a/` (drafts), this report, and a scratch
  directory `/tmp/k72w1-ExecOC3a.9Dov` (deleted before return).
- No tool install or upgrade was needed; no pacman transaction, no jj mutation, no fleet/sibling-lane
  write, no credential material read or copied.
- Process bounds: the largest single command was the verifier run at 17 s (limit 120 s); the `strings`
  dump took 1 s; nothing ran in the background; no other seat's process was signalled.
