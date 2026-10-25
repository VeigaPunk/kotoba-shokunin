# ExecOC3b — OC-3b re-derived on opencode v2.1.4 (round 72, wave 1)

## Verdict

**OC-3b is honestly derivable on the v2.1.4 bytes; the behaviour is not gone.** As committed the rule
matches nothing (0 hits, both constants), and the shape it was written to witness survives in v2.1.4
in a different form: a URL predicate `function E1(e){return URL.canParse(e)&&/^https?:$/.test(new URL(e).protocol)}`
(dump line 708687) decides which entries of the declared `instructions` list are remote, those entries
are fetched into the `{path,content}` object the `Instructions from:` renderer interpolates, and
`configuredSource` resolves them back through `.remote.get`. I wrote a replacement rule that binds
those four roles name-agnostically (predicate by backreference, list by `instructions??[]`, fetch by
`{path,content}` + the `failed to fetch instruction url` label, resolve by `.remote.get`, render by
`${<item>.path}<LF>${<item>.content}`). It matches the live dump, rejects five decoys that keep the
same tokens, and leaves the 175-assertion self-test green. No census removal is warranted.

Deliverables (not committed; L1 lands them):
`.ufo/waves/round-72/w1/build/ExecOC3b/verify_surfaces.py` (sha256 `93cb124d…`) and
`.ufo/waves/round-72/w1/build/ExecOC3b/rule.diff` (120 diff lines, against the committed
`verifiers/verify_surfaces.py`, sha256 `4f13e3bd…`, byte-identical at `c69711e` and at tip `e61fd29`
— `git diff --stat c69711e e61fd29 -- verifiers/ SKILL.md` → empty, exit 0).

## 1. The rule as committed matches nothing on v2.1.4

Rule under test (`verifiers/verify_surfaces.py:624-628` committed):

```
OC_REMOTE_FILTER_RE = re.compile(
    r'\.instructions[^;]{0,20}?\.filter\(\s*\(?\s*([A-Za-z_$][A-Za-z0-9_$]*)\s*\)?\s*=>\s*'
    r'\1\.startsWith\("https://"\)\s*\|\|\s*\1\.startsWith\("http://"\)'
)
OC_REMOTE_RENDER = "Instructions from: "
```

Direct probe (scratch harness, `python3 -B probe_committed.py`, dump `/tmp/k72-oc-strings.txt`,
sha256 `020fb253…`, 28,835,401 bytes, 1,237,844 lines):

```
dump bytes 28835401
OC_DECLARED_RE: 0 match(es)
OC_REMOTE_FILTER_RE: 0 match(es)
OC_REMOTE_RENDER 'Instructions from: ' in dump: 3
```

Full check, committed file, read-only from the lane root:

```
python3 -B verifiers/verify_surfaces.py --repo . --opencode-strings /tmp/k72-oc-strings.txt \
  --omp-binary /home/vgpnk/.local/bin/omp.real        # exit=1
FAIL surfaces.opencode_extract: vacuity: extraction produced 0 class(es) from 7 rule(s); …;
  declared opencode class(es) produced by no rule: …, opencode:config/instructions-remote, …
```

So OC-3b contributes no class id today; `opencode:config/instructions-remote` is named in the
"produced by no rule" list. (The render token alone is still present 3×, so the old conjunct
`OC_REMOTE_RENDER in dump` was already satisfied vacuously — see §5.)

## 2. The v2.1.4 form of what the rule witnessed

All anchors are literal substrings of `/tmp/k72-oc-strings.txt`; each quote below is ≤25 words and
was pasted from the named command's output (dropped bytes are named after each).

| role | literal (quote) | dump line |
|---|---|---|
| URL predicate | `function E1(e){return URL.canParse(e)&&/^https?:$/.test(new URL(e).protocol)}` | 708687 |
| declared list | `Array.from(new Set(we.flatMap((Re)=>Re.type==="document"?Re.info.instructions??[]:[])))` | 708687 |
| filter by it | `Ae.filter(E1)` | 708687 |
| fetch → rendered object | `L((Ve)=>new p2({path:Re,content:Ve}))` | 708687 |
| fetch role label | `failed to fetch instruction url` | 708687 (and 671215, string table) |
| resolve back | `if(E1(ye)){let Re=H.remote.get(ye);if(Re)we.push(Re);continue}` | 708687 |
| render template | `Instructions from: ${e.path}` | 708288 |
| render template | `Instructions from: ${O.path}` | 708687 |

Commands and observed output:

```
grep -o -F 'function E1(e){return URL.canParse(e)&&/^https?:$/.test(new URL(e).protocol)}' /tmp/k72-oc-strings.txt
function E1(e){return URL.canParse(e)&&/^https?:$/.test(new URL(e).protocol)}

grep -o -F 'Ae.filter(E1)' /tmp/k72-oc-strings.txt
Ae.filter(E1)

grep -o -F 'L((Ve)=>new p2({path:Re,content:Ve}))' /tmp/k72-oc-strings.txt
L((Ve)=>new p2({path:Re,content:Ve}))

grep -o -F 'if(E1(ye)){let Re=H.remote.get(ye);if(Re)we.push(Re);continue}' /tmp/k72-oc-strings.txt
if(E1(ye)){let Re=H.remote.get(ye);if(Re)we.push(Re);continue}

sed -n '708687p' /tmp/k72-oc-strings.txt | grep -o -F 'Array.from(new Set(we.flatMap((Re)=>Re.type==="document"?Re.info.instructions??[]:[])))'
Array.from(new Set(we.flatMap((Re)=>Re.type==="document"?Re.info.instructions??[]:[])))

grep -o -F 'Instructions from: ${e.path}' /tmp/k72-oc-strings.txt
Instructions from: ${e.path}
```

The render template is split across dump lines because the JS template literal holds a real LF
(`strings` ends the run there): line 708288 ends at `${e.path}` and line 708289 begins
`${e.content}`).join(` — same at 708687/708688 with `${O.path}`/`${O.content}`.

Anchor distances from the `instructions??[]` read on dump line 708687 (measured, byte offsets
21500538 → 21500575 / 21500656 / 21500699): filter +37, fetch object +118, label +161. The rule's
window is therefore 400 bytes, not a dump-wide co-occurrence.

What changed versus 1.19.x: the two `.startsWith("https://")` / `.startsWith("http://")` literals are
gone from the instruction path (`OC_REMOTE_FILTER_RE` = 0 hits; `https://` survives 827× dump-wide in
unrelated code, e.g. proxy/URL helpers), and the test moved into the `URL.canParse` + `/^https?:$/`
protocol predicate that also gates the remote-vs-path branch in `configuredSource`.

## 3. The replacement rule

Scratch copy: `.ufo/waves/round-72/w1/build/ExecOC3b/verify_surfaces.py`; diff:
`.ufo/waves/round-72/w1/build/ExecOC3b/rule.diff`. Two hunks: the OC-3 block (constants + new
`opencode_remote_instructions_matches()`, `verifiers/verify_surfaces.py:596-679` in the scratch copy)
and the OC-3b dispatch (`:863-871`), which now reads
`remote = opencode_remote_instructions_matches(dump)`.

Constants added: `OC_REMOTE_LIST_RE`, `OC_REMOTE_PRED_CALL_RE`, `OC_REMOTE_URL_PRED_RE` (predicate
name and its argument bound by backreference), `OC_REMOTE_FETCH_RE` (`{path:…,content:` shape),
`OC_REMOTE_FETCH_LABEL`, `OC_REMOTE_RESOLVE_RE` (`if(<pred>(<src>)){let …=.remote.get(<src>)`),
`OC_REMOTE_RENDER_RE` (`` `Instructions from: ${<item>.path<LF>${<item>.content}` `` with the item
name backreferenced), `OC_REMOTE_WINDOW = 400`. No rule is loosened: the render conjunct is
*stronger* than the committed `OC_REMOTE_RENDER in dump` (the bare string-table entry at dump line
607084 no longer satisfies it), and the class id, `literal`, `context_kind` and `verdict` cells are
untouched, so `surfaces-baseline.json` and the census inventory need no edit.

Match counts on the live dump (from the same harness):

```
OC_REMOTE_LIST_RE=1 OC_REMOTE_URL_PRED_RE=1 OC_REMOTE_PRED_CALL_RE=132 OC_REMOTE_RESOLVE_RE=1
OC_REMOTE_RENDER_RE=2 OC_REMOTE_FETCH_LABEL=2 OC_REMOTE_FILTER_RE=0
```

`OC_REMOTE_PRED_CALL_RE` is deliberately generic (132 dump-wide `.filter(<ident>)`); it only counts
inside the 400-byte window that starts at an `instructions??[]` read (1 such read in the dump).

## 4. Decoy rejection (same tokens, no instruction-loading role)

Harness: `python3 -B decoys.py` (scratch dir), which mutates the live dump and calls the scratch
module's `extract_opencode_classes`:

```
live v2.1.4 dump                   OC-3b matched=True  class_present=True
decoy1 list-not-instructions       OC-3b matched=False class_present=False
decoy2 non-url predicate           OC-3b matched=False class_present=False
decoy3 bare render token           OC-3b matched=False class_present=False
decoy4 no .remote.get resolve      OC-3b matched=False class_present=False
decoy5 fetch without {path,content} OC-3b matched=False class_present=False
```

Primary decoy (decoy1) is the one the seat asks for — same tokens, no instruction-loading role: the
dump with `Re.info.instructions??[]` rewritten to `Re.info.allowedHosts??[]` keeps the URL predicate,
its `.filter` call site, the `{path,content}` fetch, the `failed to fetch instruction url` label, the
`.remote.get` resolve and both render templates, and is rejected because no `instructions??[]` read
exists. Secondary decoys pin each remaining conjunct independently (decoy2 keeps `E1` defined and
still used by `configuredSource` but filters the list with `(e)=>e.endsWith(".md")`; decoy3 keeps
the fetch but drops the path/content interpolation; decoy4 keeps the predicate but removes
`.remote.get`; decoy5 keeps the fetch call but drops `path:`).

## 5. Scratch run with the required flags

```
cd .ufo/waves/round-72/w1/build/ExecOC3b
python3 -B verify_surfaces.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --opencode-strings /tmp/k72-oc-strings.txt --omp-binary /home/vgpnk/.local/bin/omp.real
exit=1
FAIL surfaces.literal_present: 1 loader literal(s) not verifiable: opencode:instructions/CONTEXT.md (literal 'CONTEXT.md' absent from opencode dump)
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:claude-home/CLAUDE.md, opencode:config/AGENTS.md, opencode:config/instructions, opencode:instruction-context/AGENTS.md, opencode:instructions/AGENTS.md, opencode:instructions/CLAUDE.md, opencode:instructions/CONTEXT.md, opencode:read-hook/instructions; rule(s) matched nothing: OC-1 (…); OC-2 (…); OC-3a (…); OC-4 (…); OC-5 (…); OC-6 (…)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
```

(The `opencode_extract` line is quoted with its per-rule parenthesis bodies elided as `(…)`; the
decisive part is verbatim: `opencode:config/instructions-remote` is **not** in the "produced by no
rule" list and **OC-3b is not** in "rule(s) matched nothing".) Before my change the same command
reported `0 class(es) from 7 rule(s)` and named `opencode:config/instructions-remote` (artifact
`artifact://44697`). OC-1, OC-2, OC-3a, OC-4, OC-5 and OC-6 still match nothing — those are other
seats' rules, untouched here, and they keep `p < 7` for C2 until re-derived.

Self-test of the scratch copy (fixtures symlinked read-only next to it:
`ln -s <lane>/verifiers/fixtures .ufo/waves/round-72/w1/build/ExecOC3b/fixtures`):

```
python3 -B verify_surfaces.py --self-test
0 failure(s) over 175 assertions      # exit 0
```

This is why the committed 1.19.x shape is retained as a second, explicitly labelled branch
(`OC_REMOTE_FILTER_RE` + bare render token, 0 hits on the v2.1.4 dump): the arms
`strings-opencode-clean.txt`, `strings-opencode-1.19.4-anchors.txt` and
`strings-opencode-drop-oc3b.txt` (which must still fail and name the class) are pinned to it. The
v2.1.4 branch is tried first; the retained branch cannot fire on the live dump.

## 6. Notes, risks, blockers

- **No census removal proposed.** The behaviour is witnessed in the bytes (§2), so the
  "class removed with reason" disposition does not apply; the sweep command that would have justified
  it is the one in §1 (`OC_REMOTE_FILTER_RE: 0 match(es)`), and it is answered by §2's anchors.
- **Baseline `literal` cell is now a weak witness.** `opencode:config/instructions-remote` declares
  `literal: "https://"`; that string occurs 827× in the v2.1.4 dump (`grep -c "https://"`), so
  `surfaces.literal_present` passes it vacuously, while the real witness is `URL.canParse` (22×).
  I did **not** change the cell: C2's ledger conjunct requires a class to be kept with the *same*
  `literal` at `<rev>`, and a present literal cannot be ledgered, so changing it would fail C2.
  Recommend a future round (outside a C2-predicate round) re-point the literal cell to
  `URL.canParse` and record the census row change.
- **Residual of the retained branch:** a dump that still carried the 1.19.x `.startsWith` shape would
  pass OC-3b without the v2.1.4 witness. Measured: 0 such hits on the live dump, so on this host the
  branch contributes nothing; it exists only for the committed fixture generation (precedent: OC-6's
  retained 1.19.3 fixture shape).
- **Not verified by me:** the full lane battery, the C2 counter (`check_substrate_repin_v2.py`), and
  any gate that consumes `p`; the L1 owns those. I ran no lane gate and edited no committed file.
- Tooling: nothing installed or upgraded. No pacman/jj/git write; read-only `git log`/`git diff` only.
  Scratch dir `/tmp/k72w1-ExecOC3b.****` deleted before return.

## Files written

- `.ufo/waves/round-72/w1/build/ExecOC3b/verify_surfaces.py` (scratch copy, sha256 `93cb124d…`)
- `.ufo/waves/round-72/w1/build/ExecOC3b/rule.diff` (unified diff vs `verifiers/verify_surfaces.py`)
- `.ufo/waves/round-72/w1/ExecOC3b.md` (this report)
