verdict: PARTIAL — every rule-bearing fixture line is an exact byte substring of the frozen 1.19.3 dump at the claimed dump line and the fixtures extract identically to the real dump, but the fixtures' own header (and LOG.md:2321's "fixtures rebuilt from exact dump substrings") is false for 12 of the 140 non-comment lines in the round-47 set.

# Lane: fixture fidelity — round-47 opencode surfaces fixtures vs the frozen 1.19.3 dump

Target: `verifiers/fixtures/surfaces/strings-opencode-*.txt` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
Substrate (read-only, unmodified): `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings`
sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` (matches
`/fast/scratch/kotoba-r47/shared/SHA256SUMS:4`), 750 049 lines, 67 839 091 bytes.
Scratch clone: `/fast/scratch/kotoba-r47/w2/W2FixtureFidelity/kotoba-shokunin` (detached at `7ad7fad`).
The lane repo was not touched; the only writes are this report and
`.ufo/waves/round-47/falsify/W2FixtureFidelity.lines.json`.
No tool installs were needed (python3 + coreutils sufficed) — no install/upgrade performed.

## Method

For every non-comment line of every `strings-opencode-*.txt` fixture: locate the line in the dump
(a line is a candidate only if it is a substring of a *single* dump line, so cross-line matches are
impossible), and compare the dump line numbers found against the numbers named in the immediately
preceding comment. Claim forms handled: `dump line N`, `dump lines N-M`, and the OC-4 parenthetical
form `resolve entry point (443995), its ReadTool.execute caller (444228), injected token (443193)`.
Per-line machine output: `.ufo/waves/round-47/falsify/W2FixtureFidelity.lines.json`.

Round-47 opencode set = 10 files (`clean`, `drop-oc{1,2,3a,3b,4,5,6}`, `extra`, `planted-name`),
140 non-comment lines. `strings-opencode-v2.0.26.txt` is the retired-generation probe and is
excluded from the substring requirement (all 12 of its non-comment lines are absent from the
1.19.3 dump, which is the point of the probe).

---

## F1 — MEDIUM (calibration, false provenance claim): the fixture header is false for 12 lines

`verifiers/fixtures/surfaces/strings-opencode-clean.txt:3-5` (identical header in all 10 round-47
opencode fixtures) states:

> "Every non-comment line is an exact byte substring of
> `/fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` at the dump line named
> in its comment; **no other binary text is committed**."

That is false for **12** of the 140 non-comment lines:

| file (at `7ad7fad`) | line | content | in dump? |
|---|---|---|---|
| `verifiers/fixtures/surfaces/strings-opencode-clean.txt` | 28 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc1.txt` | 28 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc2.txt` | 28 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc3a.txt` | 28 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc3b.txt` | 27 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc4.txt` | 26 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc5.txt` | 27 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-drop-oc6.txt` | 25 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-extra.txt` | 35 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-planted-name.txt` | 29 | `no-rule-anchor marker line` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-extra.txt` | 30 | `H.up({targets:["RULES.md"],start:S,stop:$})` | **no** |
| `verifiers/fixtures/surfaces/strings-opencode-extra.txt` | 31 | `X.join(r.config,"opencode.json")` | **no** |

Repro (each `grep -c` below exits **1** = no match, count 0):

```
$ grep -c 'no-rule-anchor marker line' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings ; echo "exit=$?"
0
exit=1
$ grep -c 'RULES.md' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings ; echo "exit=$?"
0
exit=1
$ grep -c 'targets:\["RULES.md"\]' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings ; echo "exit=$?"
0
exit=1
$ grep -c 'X.join(r.config,"opencode.json")' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings ; echo "exit=$?"
0
exit=1
$ grep -o '\.join([A-Za-z_$][A-Za-z0-9_$]*\.config,"[^"]*"' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings | sort -u
.join(r.config,"AGENTS.md"
```

So `RULES.md` does not exist anywhere in opencode 1.19.3, and the *only* `<v>.config` `.join` shape
in the whole 67 MB dump is the real OC-2 anchor `X.join(r.config,"AGENTS.md")`. `extra:30` and
`extra:31` are synthetic mutations of real lines (the OC-6 line at dump 445482 with the literal
swapped, and the OC-2 line with the literal swapped), not dump substrings.

The claim is repeated in the landing record:

```
$ sed -n '2321p' LOG.md | fold -w 200 | grep -o 'fixtures rebuilt[^;]*;[^;]*;[^,]*'
fixtures rebuilt from exact dump substrings, the v2.0.26 fixture kept as a must-fail generation probe, a planted-name fixture added
```

`LOG.md:2321` therefore states a false provenance for the round-47 fixture rebuild. The one line
that is *supposed* to be synthetic — `strings-opencode-planted-name.txt:8`
(`…,"CONTEXT.md","GUIDE.md"]`) — is out of scope of the target's plant exception and is correctly
absent from the dump (verified: 0 hits).

Severity note: this is a documentation/provenance defect, not a gate failure. No instrument in the
repo checks fixture provenance (`grep -rn 'substring' verifiers/*.py` returns only unrelated hits in
`compare_harness_independent.py` / `verify_harness_independent.py`), so the overclaim is invisible to
the round's own checks. The round-47 lesson set (`corpus/lessons/round-47.md` M20–M22, read at
`7ad7fad`) does not cover "fixture claims provenance it does not have".

## F2 — LOW (the negative control could have been real, for free): `extra`'s near-misses are synthetic while real ones sit unused in the same binary

`verifiers/fixtures/surfaces/strings-opencode-extra.txt:28-29` labels its added block
"not anchors: a targets array for another file, a config read of a non-.md key, the SDK client stub
for instruction entries, a projectSource token" — i.e. it is presented as the anchor-adjacent
control that proves the rules are anchored rather than literal-greedy
(`verifiers/verify_surfaces.py:1049-1054`, `rec("oc-extra: exit 0", code == 0, code)`).
Two of its four control lines (30, 31) do not exist in the binary, while the binary contains real
counter-shapes of exactly the same families that were not used:

- `r.up({targets:[".opencode"],start:o,stop:t})` — dump line 446403 (real `up({targets:[…]}` array,
  non-`AGENTS.md` literal; OC-6's anchor is the literal `targets:["AGENTS.md"]`)
- `_.up({targets:[".git"],start:V})` — dump line 447174 (same family)
- `XH.Key.make("core/environment")` — dump 445485; `XH.Key.make("core/date")` — dump 445487;
  `XH.Key.make("core/builtins")` — dump 445485-445487 region (real `Key.make("core/…")` shapes next
  to OC-6's `Key.make("core/instructions")`)

I built that all-real replacement and re-ran the gate on the frozen dumps:

```
$ python3 -B verifiers/verify_surfaces.py \
    --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
    --opencode-strings verifiers/fixtures/surfaces/strings-opencode-extra-realnear.txt
PASS surfaces.literal_present: 42 loader-kind entries verified against the dumps
PASS surfaces.no_uncovered_class: all 8 extracted loader class(es) declared
PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)
PASS surfaces.table_parity: inventory id set == baseline id set (42 ids)
PASS surfaces.literal_parity: 42 inventory row literal(s) match the baseline per id
PASS surfaces.kind_parity: 42 inventory row kind(s) match the baseline per id
PASS surfaces.excluded_reason: 8 excluded entries, all reasoned and listed in the inventory
EXIT=0
```
(5 replacement lines, each asserted `in dump` before use; the variant file was deleted afterwards —
`git status --porcelain` empty.)

So the current synthetic near-misses buy nothing: the same control, built from real dump bytes,
keeps the gate green. The fixture is currently weaker than it could be for free.

## F3 — LOW (secondary overclaim): `extra`'s remaining two control lines sit at unnamed dump lines

`verifiers/fixtures/surfaces/strings-opencode-extra.txt:32-33`
(`instructions:{entry:{list:(a,l)=>s({method:"GET",path:…` and `projectSource`) *are* real dump
substrings, but they live at dump lines 606940 and 607465 while their governing comment
(`:28-29`) names no dump line at all — so "at the dump line named in its comment" is unsatisfied
for them too, even though the byte-substring half of the claim holds.

## F4 — INFO (observation): the OC-6 distinguishing shape the census cites is real but absent from the fixtures

`corpus/knowledge/instruction-surface-census-round13.md:257` cites OC-6's *ungated* config candidate
`jX(L.config,"AGENTS.md")`. Verified: exactly 1 occurrence, dump line 445482 — inside the claimed
`dump 445481-445487` range. It is not carried into any fixture, so no fixture exercises the
"ungated vs gated config candidate" distinction the census row asserts. Benign today (no rule keys
on `jX`), but it is the one piece of OC-6 evidence with no fixture coverage.

---

## What survived the attack (re-derived, not taken on trust)

**S1 — every rule-bearing line is an exact byte substring at exactly the claimed dump line.**
Of the 140 non-comment lines: 13 are not exact substrings (F1/F2 + the deliberate plant), 2 are
real control lines at unnamed dump lines (F3), and the remaining **125 rule-bearing lines are all
exact substrings of a single dump line, and the dump line found is the claimed one**:

| fixture group | claimed | found |
|---|---|---|
| OC-1 `y=["AGENTS.md",…` | 443993 | 443993 ✔ |
| OC-2 `n=[X.join(r.config,"AGENTS.md"),…` | 443993 | 443993 ✔ |
| OC-3a `if(T.instructions)for(let O of…` | 443993 | 443993 ✔ |
| OC-3b `w=(T.instructions??[]).filter(…` | 443993 | 443993 ✔ |
| OC-3b render `` [`Instructions from: ${q} `` | 443993 | 443993 (also 443994) ✔ |
| OC-4 `b=s.fn("Instruction.resolve")…` | 443995 | 443995 ✔ |
| OC-4 `$=s.fn("ReadTool.execute")…` | 444228 | 444228 ✔ |
| OC-4 `<system-reminder>` | 443193 | 443193 (also 443280, 443597, 443630, …) ✔ |
| OC-5 `if(!Jr.OPENCODE_DISABLE_PROJECT_CONFIG)…` | 443993 | 443993 ✔ |
| OC-5 `return yield*e.globUp(T,r.config,r.config)` | 443993 | 443993 ✔ |
| OC-6 `A=M.fn("InstructionContext.observe")…` | 445481-445487 | 445482 ✔ (in range) |
| OC-6 `yield*H.up({targets:["AGENTS.md"],start:S,stop:$})` | 445481-445487 | 445482 ✔ (in range) |
| OC-6 `BP=XH.Key.make("core/instructions")` | 445481-445487 | 445481 ✔ |
| OC-6 `kX=i({name:"system-context-builtins",layer:tX,` | 445481-445487 | 445487 ✔ |

The claimed dump lines agree with the census rows
(`corpus/knowledge/instruction-surface-census-round13.md:249-257`, read at `7ad7fad`): OC-1/2/3a/3b/5
→ 443993, OC-4 → 443995 and 444228, OC-6 → 445481-445487.

**S2 — the fixture set extracts identically to the real dump.** Running the shipped rule set over
the real 67 MB dump and over the fixtures (`verifiers/verify_surfaces.py:extract_opencode_classes`):

```
REAL 1.19.3 dump        -> 9 ids; OC-1..OC-6 all matched (OC-5 owns no id)
clean fixture           -> 9 ids; identical set, identical rule report; DIFF extra=[] missing=[]
extra fixture           -> 9 ids; DIFF extra=[] missing=[]
planted-name fixture    -> 10 ids; DIFF extra=['opencode:instructions/GUIDE.md']
v2.0.26 fixture         -> 0 ids; all 7 rules unmatched (must-fail generation probe)
drop-oc1 fixture        -> 6 ids; loses the three opencode:instructions/* ids
drop-oc6 fixture        -> 8 ids; loses opencode:instruction-context/AGENTS.md
```

**S3 — the mandated v2.0.26 equality holds byte-for-byte.**

```
$ git show c61a973b2e02e1ded169703ddcb06466f4edd8bd:verifiers/fixtures/surfaces/strings-opencode-clean.txt | sha256sum
7549bed864cce06b46821a73032dfcffa47173c89744a328641b77f994b371d7  -
$ sha256sum verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt
7549bed864cce06b46821a73032dfcffa47173c89744a328641b77f994b371d7  verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt
$ diff <(git show c61a973b2e02e1ded169703ddcb06466f4edd8bd:verifiers/fixtures/surfaces/strings-opencode-clean.txt) verifiers/fixtures/surfaces/strings-opencode-v2.0.26.txt
(no output; exit 0)
```

**S4 — the gates are green on the frozen substrate** (re-run, not copied):
`python3 -B verifiers/verify_surfaces.py --omp-strings …/omp-18.12.5.strings --opencode-strings
…/opencode-1.19.3.strings` → **7/7 PASS, exit 0**; `--self-test` → **0 failure(s) over 99
assertions, exit 0**. This corroborates C1's "surfaces 7/7 exit 0" for the parts my lane can see.

**S5 — census § B′ anchor counts check out** (adjacent to my lane, cheap to verify, all confirmed):
`<system-reminder>` 18 occurrences (census: "18 hits"); `ConfigInstructionPlugin` 0,
`ReadTool.Plugin` 0, `SessionInstructions` 0, `session.instructions.entry.put` 0,
`j5(r.config,"AGENTS.md")` 0, `InstructionDiscovery` 0; `var n="1.19.3"` 1; `2.0.26` 0.

---

## Calibration read for the integrator

The round-47 C1 claim survives on the substance I could attack: the opencode rule set was genuinely
re-derived against 1.19.3, the fixture corpus is behaviourally faithful to the real binary, and the
mandated v2.0.26 fixture is byte-identical to the base clean fixture. What does not survive is the
**provenance sentence**: the fixtures say "every non-comment line is an exact byte substring … no
other binary text is committed" and the LOG repeats "fixtures rebuilt from exact dump substrings",
while 12 of 140 lines are synthetic (10 shared marker lines + 2 fabricated near-misses). Two
one-line-class repairs make the claim true without touching behaviour:
(a) scope the header sentence to the rule-bearing lines and name the marker line as synthetic
("marker lines are synthetic by design"); (b) replace `extra:30-31` with the real dump bytes
(`r.up({targets:[".opencode"],start:o,stop:t})` @446403, `_.up({targets:[".git"],start:V})` @447174,
`XH.Key.make("core/environment")` @445485) — demonstrated above to keep exit 0. If the header is
not changed, `LOG.md:2321`'s "exact dump substrings" should be softened; the LOG is append-only, so
that is an erratum row, not an edit.

## What I did NOT check

- The omp side of the surfaces fixtures (`strings-omp-*.txt`, `strings-omp-18.12.5.txt`) — other lane.
- `verifiers/surfaces-baseline.json`, `verifiers/baseline.json`, `verifiers/check_substrate_pins.py`
  re-pinning arithmetic (other lanes).
- Whether the frozen `/fast/scratch/kotoba-r47/shared/*.strings` dumps were themselves produced with
  the same `strings -n 4` invocation the verifier would use (I trusted the shared substrate and its
  SHA256SUMS); a mismatch there would not change my per-line results, since substring membership is
  checked against the exact file the verifier was pointed at.
- Runtime behaviour of opencode 1.19.3 (no execution; strings-only evidence, as the census states).
- Whether the wave-1 build reports (`.ufo/waves/round-47/build/`) state the same header claim —
  I read only `LOG.md:2321` and the fixture/census text, not every wave-1 report.
- The `strings-opencode-v2.0.26.txt` generation probe's *content* against the retired v2.0.26 binary
  (that binary was removed from the host; the file was only required to equal the base fixture, which
  it does).
