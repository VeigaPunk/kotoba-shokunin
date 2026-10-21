verdict: PARTIAL — `trigger.no_xml_tag` is registered in every machine surface (CHECK_IDS, docstring, `--check` choices, dispatcher branch, self-test fixture table + string battery) and the floors are consistent, but the SKILL.md that advertises the instrument still says **10 checks** (there are 11) and the new check is bound to no checklist box.

# W2CheckIdsContract — round-47 falsify, post-crash wave 2

Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/verify_skill_checklist.py` CHECK_IDS + docs.
Commit under test: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`).
Scratch clone for every mutation: `/fast/scratch/kotoba-r47/w2/W2CheckIdsContract/kotoba-shokunin` (detached at `7ad7fad`; production tree read-only, no git mutation in production).
Mutation log: `.ufo/waves/round-47/falsify/W2CheckIdsContract.mutants.txt`.
No tools were installed or upgraded (nothing needed beyond `python3` + `git`, both present).

---

## 0. Baseline (production tree, read-only)

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin && git rev-parse HEAD
7ad7fadfc09354b74fb66605dfb0c1182c115a2f

$ PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_skill_checklist.py
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='kotoba-shokunin', description 814 chars
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string: evaluated 1 — description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause: evaluated 1 — exclusion marker 'Anti-triggers' present (...)
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)
PASS trigger.line_budget: evaluated 528 — 528 lines within budget 600 (from box at line 246)
PASS trigger.no_placeholder: evaluated 484 — no placeholder markers in 484 scanned lines
PASS trigger.command_binary_resolves: evaluated 13 — 9 segments; 13 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 44 — 44 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves: evaluated 848 — 848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused
exit 0                                   # 11 PASS lines, 11 checks

$ PYTHONDONTWRITEBYTECODE=1 python3 verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1845 assertions
exit 0

$ PYTHONDONTWRITEBYTECODE=1 python3 verifiers/check_assertion_floors.py
PASS checklist observed=1845 floor=1845
... exit 2   # one unrelated row: "harness_independent self-test timed out after 120s (hung?)"
$ python3 verifiers/verify_harness_independent.py --self-test   # standalone
0 failure(s) over 104 assertions   exit 0   (133 s wall)  -> floors row is host-load timeout, not a checklist defect [INFERENCE]
```

---

## Findings

### F1 — HIGH (calibration / live doc): `SKILL.md:122` still advertises **10 checks**; the instrument exposes 11

`SKILL.md:122` at `7ad7fad`:

```
**10 checks** (`checklist.box_map_complete` + the eight boxes marked
(executed: …)` below + `governance.citation_resolves` over the two root
governance files), each fail-closed on fixtures, `evaluated N` per check,
```

The enumeration is exact and it now sums to the wrong number: `CHECK_IDS`
(`verifiers/verify_skill_checklist.py:304-316`) carries **11** ids
(`trigger.no_xml_tag` inserted at `:310`), and the live run prints 11 PASS lines
(§0). `1 + 8 + 1 = 10`; the 11th check (`trigger.no_xml_tag`) cannot be
expressed by that sentence at all, because **no checklist box is bound to it**
(§F2). `SKILL.md:151` names the new check in prose, so the skill is not silent
about it — but the instrument's own self-description in the same file is false
by one, in the present tense, with no time qualifier.

Repro (read-only):

```
$ grep -n "10 checks" SKILL.md
122:**10 checks** (`checklist.box_map_complete` + the eight boxes marked
$ python3 verifiers/verify_skill_checklist.py | grep -c '^PASS'
11
$ python3 -c "import re;print(len(re.findall(r'\"([a-z_.]+)\"', re.search(r'CHECK_IDS = \((.*?)\n\)', open('verifiers/verify_skill_checklist.py').read(), re.S).group(1))))"
11
```

No gate catches it: the checklist verifier exits 0; the floors registry pins an
**assertion** floor (1845), not a check-count floor
(`verifiers/floors-registry.json:5`, `verifiers/check_assertion_floors.py:123`
and `:144`); no verifier greps SKILL.md's count
(`grep -rn "10 checks" verifiers/` → exit 1). This is the same defect class the
repo has already filed errata for — `LOG.md:1310` records
"SHONEN.md:35-37 stale counts (9->10 checks, 67->71 cases, 1283->1504)".

Minimal repair (integrator, not this lane): `SKILL.md:122` → "**11 checks**
(`checklist.box_map_complete` + the eight boxes marked `(executed: …)` below +
`trigger.no_xml_tag` (S003 XML-tag rule on the parsed `name`/`description`) +
`governance.citation_resolves` …)" — or bind a box and keep the arithmetic in
the box map (see F2).

### F2 — MEDIUM (disclosure / box map): the executed check is bound to no checklist box

`verifiers/checklist-baseline.json` at `7ad7fad`: 41 boxes, dispositions
`8 executed / 0 delegated / 33 unexecuted`; the executed ids are
`trigger.frontmatter_parses`, `trigger.name_directory`,
`trigger.literal_trigger_string`, `trigger.anti_trigger_clause`,
`trigger.command_binary_resolves`, `trigger.citation_resolves`,
`trigger.line_budget`, `trigger.no_placeholder` — **no**
`executed:trigger.no_xml_tag` entry. `SKILL.md:185` ("Eight of the fifteen
boxes are **executed, not read**") stays literally true, but the machine
coverage of the skill's own § Trigger-fidelity checklist is now 8 checks while
the instrument runs 11. The XML rule itself is disclosed only in prose at
`SKILL.md:151` (portability floor), never as a `- [ ]` box.

Consequence: a reader who executes "Run before shipping any SKILL.md"
(`SKILL.md:181`) never runs the XML gate as part of the checklist, and the
instrument's own parity check (`checklist.box_map_complete`, which validates
each `executed:<id>` against `CHECK_IDS` at
`verifiers/verify_skill_checklist.py:1127`) cannot see that a machine check
exists for a rule the skill asserts. Nothing fails — this is a coverage/
disclosure gap, not a verifier error: there is no "every CHECK_ID must be
bound to a box" rule in the contract.

Corroborating count claims that are now stale or incomplete:

* `SKILL.md:126-127` — "maps **all 41 boxes** (8 executed, 0 delegated, 33
  unexecuted) … Limits and ceilings: `corpus/knowledge/checklist-execution-round17.md`".
  The box counts hold (41/8/0/33, re-measured above); the cited ceilings doc
  enumerates only the round-17 ten.
* `corpus/knowledge/checklist-execution-round17.md:44` — "At the landed
  round-17 tree, the checklist instrument exposes ten checks." This one is
  honestly time-qualified and is **not** a live false claim; I flag it only
  because `SKILL.md:127` points a reader at it as the live "Limits and ceilings"
  source.
* `corpus/knowledge/checklist-execution-round16.md:23` ("As of round 16 the
  checklist instrument has **nine** checks") — historical, correct, no action.

### F3 — MEDIUM (latent, registration is not fail-closed): `CHECK_IDS` → dispatcher parity is not enforced

`verifiers/verify_skill_checklist.py:2406-2407` — the dispatch chain ends in an
unconditional `else:` that maps **any** unrecognised cid to
`check_commands(...)`:

```
2406:        else:
2407:            st, ev, detail = check_commands(lines, repo, vocab)
```

`--check`'s `choices=CHECK_IDS` (`:2288`) derives from `CHECK_IDS`, so adding an
id to `CHECK_IDS` is enough to make `--check <new-id>` accepted — with no
dispatch branch it silently reports the *command* check's verdict.

Repro (scratch clone, M6):

```
$ python3 verifiers/verify_skill_checklist.py --check trigger.bogus_probe
N/A trigger.bogus_probe: evaluated 0 — 0 segments: no shell-fenced block lines and no inline spans headed by a declared vocabulary word
$ python3 verifiers/verify_skill_checklist.py        # full run
PASS trigger.bogus_probe: evaluated 13 — 9 segments; 13 command subject(s) resolve
exit 0
```

Worse, the self-test does **not** guarantee the parity: deleting the branch of
the landed check (M3) leaves **43 of the 75 fixture cases silent** — including
the positive control `clean`, because in that fixture the command check PASSes
with `evaluated 2`, so every implicit-PASS assertion still holds:

```
$ # M3: delete `elif cid == "trigger.no_xml_tag":` block
$ python3 verifiers/verify_skill_checklist.py --self-test
52 failure(s) over 1853 assertions     exit 1
# failing fixture cases: 32 of 75; silent: clean, fm-nested-metadata, name-mismatch,
# name-quoted, no-literal-trigger, trigger-key, no-anti-trigger, anti-quoted-negation,
# over-line-budget, line-budget-box-binding, placeholder-*, negation-respected,
# command-skip-list, command-fence-filter, command-heredoc-*, map-*, no-checklist-section,
# missing-map, map-malformed, commands-*, citation-dead, citation-base-named, ...
```

Today the landed change is correct (`verifiers/verify_skill_checklist.py:2391-2392`
has its own branch, not the `else`), so this does not break C2 — it is the
residual risk for the *next* check and the reason "registered in `CHECK_IDS`" is
not sufficient evidence of registration. A one-line `else: raise` (or an
exhaustive `assert cid == "trigger.command_binary_resolves"` in the tail) would
close it; a self-test assertion "every CHECK_ID has a dispatch branch" would
close it locally.

### F4 — LOW/MED (doc surface): the docstring is not gated, and its YAML-escape clause over-states the rule

**(a) The docstring surface is unverified.** `CHECK_IDS` ↔ module docstring
parity is asserted by nothing. Deleting the 8-line
`trigger.no_xml_tag` bullet (`verifiers/verify_skill_checklist.py:97-104`)
leaves the instrument green (M4):

```
$ # M4: delete lines 97-104 (the trigger.no_xml_tag docstring bullet)
$ python3 verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1845 assertions     exit 0
$ python3 verifiers/verify_skill_checklist.py     exit 0
```

The floors floor stays satisfied because deleting prose changes no assertion
count. A future check can therefore land in `CHECK_IDS` with no contract text
and no gate will notice.

**(b) The docstring's YAML-escape clause is narrower than the implementation.**
`verifiers/verify_skill_checklist.py:97-104` says the check fails on "a YAML
double-quoted ``\x3c``/``\u003c`` escape **that decodes to one**". The
implementation (`YAML_ANGLE_ESCAPE_RE` at `:409`, used by
`check_no_xml_tag` at `:1294-1317`) matches the literal backslash text in
**any** scalar style, and a plain (unquoted) YAML scalar does not decode
`\u003c` to `<`. Measured (M7, direct calls, no file mutation):

```
plain-scalar-literal-uescape  -> FAIL, 2, "XML tag in description: '\\u003c'"
double-quoted-uescape        -> FAIL, 2, "XML tag in description: '\\u003c'"
plain-scalar-literal-x3c     -> FAIL, 2, "XML tag in description: '\\x3c'"
backtick-escape              -> FAIL, 2, "XML tag in description: '\\u003c'"
```

i.e. a description that *talks about* the YAML escape sequence fails the gate
for a reason the docstring says it should not. False-negative direction: I
found none (tags, comments, CDATA, PIs, declarations, namespaced names and
attribute-bearing tags all hit — `XML_TAG_RE` at `:404-407`, plus the direct
string battery at `:1970-1983`). This is over-strictness vs the stated rule, a
calibration nit, not a false-negative hole.

### F5 — What SURVIVES the attack (findings in the positive direction)

Every registration surface the assignment asked about is present and correct at
`7ad7fad`:

| surface | evidence at `7ad7fad` | verdict |
|---|---|---|
| `CHECK_IDS` | `verifiers/verify_skill_checklist.py:304-316`, `trigger.no_xml_tag` at `:310`; 11 ids | registered |
| module docstring | `verifiers/verify_skill_checklist.py:97-104`; all 11 ids appear exactly once in the docstring (script-checked) | registered |
| `--check` choices | `verifiers/verify_skill_checklist.py:2288` `choices=CHECK_IDS` (derives automatically); `--check trigger.no_xml_tag` → `PASS … evaluated 2`, exit 0 | registered |
| dispatcher | `verifiers/verify_skill_checklist.py:2391-2392` — own branch, not the `else` tail (`:2406`) | registered (but see F3 for the parity hole) |
| self-test fixture table (implicit-PASS rule) | `:1778` comment, entries `:1784,1788,1793,1798,1803,1806,1807,1808,1813,1872` list it in `fails`; control `xml-tag-control` at `:1809`; the rule itself at `:1950` (`passes = [c for c in CHECK_IDS if c not in fails and c not in nas]`) | registered; rule is exception-based and load-bearing |
| string battery | `:1970-1983`, 9 cases incl. `<x>` name hit, `a < b` / `<=` / `<<EOF` / `&lt;skills&gt;` controls | registered |
| floors / calibration | `verifiers/floors-registry.json:5` "checklist": 1845; `verifiers/check_assertion_floors.py:123` and `:144` both 1845; observed 1845 → `PASS` | consistent |
| box map | `verifiers/checklist-baseline.json` — 41 boxes, 8 executed / 0 delegated / 33 unexecuted; `executed:` ids validated against `CHECK_IDS` at `:1127` | consistent, but no box for the new check (F2) |
| gate bites on the real file | M1: plant `<skills>` in the live description → `FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '<skills>'`, exit 1 | operability confirmed |
| fixture battery discriminates | M5: plant `<skills>` in `verifiers/fixtures/checklist/xml-tag-control/SKILL.md` → self-test 3 failures, exit 1 | confirmed |
| registration is enforced on removal | M2: drop the id from `CHECK_IDS` → self-test 17 failures / 1712 assertions, exit 1 | confirmed |
| C2 side-claim | `SKILL.md` frontmatter now carries 0 `<skills>` and 0 `<`/`>` in the parsed `description` (814 chars) — `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` → 0 | confirmed |

---

## What I did NOT check

* **C1 (substrate freshness)** — I did not re-derive omp 18.12.5 / opencode 1.19.3, did not touch `verifiers/verify_surfaces.py`, `verifiers/surfaces-baseline.json`, `verifiers/check_substrate_pins.py`, `verifiers/baseline.json`, or the frozen strings dumps. Other lanes own that.
* **C3 (governance erratum / corpus index)** — I did not audit `GOVERNANCE_ERRATA` (`:378`, horizon `:377`), the LOG.md:2111 pinning, `corpus/README.md` index rows, `corpus-baseline.json` tracked_files 58→60, or the corpus integrity / independent / fault-harness gates. I only read `corpus/SOURCES.md` S003 (`:16`) and S012 (`:25`) to judge the rule the new check states.
* I did **not** audit `verifiers/fault_injection_corpus.sh` (it targets the corpus instruments, not the checklist instrument — `grep -in "skill|checklist" verifiers/fault_injection_corpus.sh` → no match), and I did not run the fault harness.
* I did not verify whether a `corpus/knowledge/` doc is *required* for a new check (C2 landed without one; `corpus/README.md` has no round-47 checklist row) — that convention call belongs to the integrator.
* I did not check the six **body** occurrences of `<skills>` in `SKILL.md` (lines 22, 91, 96, 99, 111, 430) against S012; S012 and S003 are description-scoped, and the check scans `name`+`description` only, so body compliance is out of the check's contract — but it is unverified by me.
* I did not re-measure every fixture's `evaluated` count for `trigger.no_xml_tag` (the docstring promises 1-2); I checked the `clean` and control fixtures (2) and the frontmatter-broken family (0, FAIL).
* I did not chase the `harness_independent` floors-row timeout beyond one standalone re-run (passes in 133 s > the guard's 120 s budget) — cause is host load [INFERENCE].
* I made no production edits, no git/jj mutations in `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, and did not write outside `.ufo/waves/round-47/falsify/`. This report and `W2CheckIdsContract.mutants.txt` are the only lane writes. (`git status --porcelain` in the production repo shows `M verifiers/verify_surfaces.py` and new `.ufo/waves/round-47/after/` at report time — an in-flight change by another lane/integrator, not mine; every mutation of this lane lives in the scratch clone, which is clean.)
* I did not re-run the whole fleet battery (harness/corpus/surfaces/pins) beyond the checklist verifier, its self-test, and the floors guard.
