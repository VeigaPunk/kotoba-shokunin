verdict: PARTIAL — the four `xml-tag-*` fixtures each kill the detector they claim to and the control stays green, but the control fixture lost the `c > d` half of its own design case (two over-eager detectors survive the fixture set) and three of the six markup shapes the docstring claims (CDATA, PI, declaration) have **zero** assertions — mutants that delete them leave the whole 1845-assertion self-test green.

Lane: `KotobaR47-2.W2XmlFixtures-2` (leaf reviewer, no subagents).
Target: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/fixtures/checklist/xml-tag-*` at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.
Scratch clone (canonical layout, detached at 7ad7fad): `/fast/scratch/kotoba-r47/w2/W2XmlFixtures/kotoba-shokunin`.
Artifacts: `.ufo/waves/round-47/falsify/W2XmlFixtures.mutants.txt`, `.ufo/waves/round-47/falsify/W2XmlFixtures.mutants.json`.
Tooling: nothing installed, upgraded, or downgraded (no pacman transaction; the stdlib-only verifier was sufficient).

---

## 0. The three questions, answered

| question | answer | evidence |
|---|---|---|
| Does each fixture kill the wrong implementation it claims to? | **Mostly yes.** codespan→span-stripping; split→lowercase-naive **and** no-whitespace-before-`>` (and start-tag-only); dq-escape→escape-blind; control→any-bracket, all-fields scan, name-only/desc-only, entity-decode. **Two exceptions**, both on the control (F1 below). | mutation matrix, §3 |
| Does the control fixture stay green on every check? | **Yes.** `xml-tag-control` exits 0; every non-N/A check is `PASS` with `evaluated > 0` (box-map 2, frontmatter 4, name 1, literal-trigger 1, anti-trigger 1, no_xml_tag 2, line-budget 29, placeholder 21, command 2). | §2 |
| Do the 7 frontmatter-broken fixtures list `trigger.no_xml_tag` under FAIL with `evaluated 0`? | **Yes, 7/7** — in the `CASES` table *and* at runtime. | §4 |

---

## 1. Baseline re-measure (all commands from the scratch clone at 7ad7fad)

```
$ python3 -B verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1845 assertions
exit=0

$ python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" \
      --skill verifiers/fixtures/checklist/<case>/SKILL.md \
      --map  verifiers/fixtures/checklist/<case>/map.json
xml-tag-codespan exit=1  FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '<skills>' (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)
xml-tag-split    exit=1  FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '</Skills >' (…)
xml-tag-dq-escape exit=1 FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '\\u003c' (…)
xml-tag-control  exit=0  PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (…)
```

`verifiers/floors-registry.json` floor for `checklist` = 1845; the guard prints `PASS checklist observed=1845 floor=1845` (guard's own exit was 2 in my clone for an unrelated reason — see F6).

Live file: `sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'` → **0** (grep exit 1); the live check passes (`PASS trigger.no_xml_tag: evaluated 2`). Before-value at BASE was 1 (`.ufo/waves/round-47/before/SUMMARY.md`, "frontmatter <skills> count: 1"). C2's "1→0" holds.

---

## 2. Findings

### F1 — MEDIUM — the control fixture no longer kills the two over-eager detectors its design record claims it kills

`verifiers/fixtures/checklist/xml-tag-control/SKILL.md:3-7` (parsed description):

> `Fixture skill … Triggers: "fixture run", \`a -> b\`, \`x => y\`. Anti-triggers: never use when a < b, for files <= 600 lines or <500 lines, cat <<EOF, ≤ 9, or the escaped &lt;skills&gt; router entity.`

The design record `.ufo/waves/round-47/build/C2CriticRule.md` §5 claims the control *"kills … any-bracket (M3), all-fields scan, space-after-`<` (M7)"*, and its battery `C2CriticRule.battery.json` carries the case `ctl-cmp` = `'Fires when a < b and c > d'`. **The landed control kept `a < b` and dropped the `c > d` half.** Consequence: the control's description contains no `<`…`>` pair that a loose matcher can reach (the only `>` characters are in `->`, `=>` and the entity `&gt;`, and every `<` is followed by a space, `=`, a digit or `<`).

Two wrong implementations therefore **pass the control fixture**:

* **space-after-`<` allowed** — `XML_TAG_RE` → `r"</?\s*[A-Za-z_][\w.:-]*(?:\s[^<>]*)?/?>"`
* **loose angle** — `XML_TAG_RE` → `r"<[^<>]*>"`

Repro (mutant tree = repo-root symlinks + patched copy of `verifiers/`, `--self-test` in the mutant):

```
M27-space-after-lt  selftest=1  flips=[]      # control still exits 0
M19-loose-angle     selftest=1  flips=[]      # control still exits 0
```

i.e. the *fixture* does not discriminate them; only the in-source string battery row `'Map a -> b, x => y, a < b and c > d.'` (`verifiers/verify_skill_checklist.py:1978`) catches them — so the on-disk evidence for C2 is narrower than the claim.

Constructive confirmation (scratch copy of the control only): restoring the design battery's `c > d` half at `xml-tag-control/SKILL.md:6`

```
description line 6: "a < b, for files <= 600 lines"  ->  "a < b and c > d, for files <= 600 lines"
M19-loose-angle    control exit=1  FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '< b an'
M27-space-after-lt control exit=1  FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '< b an'
```

Both over-eager detectors die with that one edit. **Fix is one clause in `xml-tag-control/SKILL.md:6`** (the control's own needles and the map hashes do not change: the box text is untouched). Severity: MEDIUM — the control's job is to kill over-eager detectors, and two of the three plausible over-eager shapes it was designed against now escape it.

### F2 — MEDIUM — CDATA, processing-instruction and declaration branches are unasserted; deleting them leaves the gate green

`verifiers/verify_skill_checklist.py:404-406`:

```python
XML_TAG_RE = re.compile(
    r"</?[A-Za-z_][\w.:-]*(?:\s[^<>]*)?/?>"
    r"|<!--|<!\[CDATA\[|<\?[A-Za-z_]|<![A-Za-z]")
```

The module docstring (`verifiers/verify_skill_checklist.py:97-104`) promises *"a start/end/empty-element tag …, comment, CDATA, processing instruction or declaration"*. Mutation (delete one alternation, change nothing else):

```
M21-no-CDATA-branch   selftest=0   # 0 failure(s) over 1845 assertions
M22-no-PI-branch      selftest=0
M23-no-declaration    selftest=0
```

**Three of the six documented shapes have no assertion anywhere** — neither in the four fixtures (no fixture description contains `<!--`, `<![CDATA[`, `<?` or `<!`) nor in the in-source string battery (`verifiers/verify_skill_checklist.py:1970-1983` has `<!-- c -->` only). The design battery has the same hole: `C2CriticRule.battery.json` has `plant-comment` but no `plant-CDATA` / `plant-PI` / `plant-declaration` case, even though `C2CriticRule.md` §3 names them ("`<!-- -->`, `<![CDATA[`, `<?x`, `<!X` all need explicit alternations").

Consequence: a future refactor can silently drop the CDATA / PI / declaration branches and every gate stays green, while the docstring still claims them. Severity: MEDIUM (prose contract > assertion coverage). Cheap fix: three rows in the string battery, e.g. `("x", "Use <![CDATA[x]]> here.", "FAIL")`, `("x", "Use <?xml v?> here.", "FAIL")`, `("x", "Use <!DOCTYPE x> here.", "FAIL")`.

### F3 — LOW — an NFKC-normalising implementation survives the whole gate (the "literal, not NFKC" decision is unpinned)

Mutant: `val = unicodedata.normalize("NFKC", fields[key])` (`:1303`).

```
M11-nfkc  selftest=0  flips=[]
```

No fixture and no battery row distinguishes "literal matching" from "NFKC-folded matching". The landed rule is literal, which is what `C2CriticRule.md` §3 recommends ("Fullwidth `＜skills＞` is not an XML tag, but NFKC maps it to `<skills>` … Record them as limits rather than adding rules"), so this is not a wrong behaviour — it is an unpinned decision. A control row such as `("x", "Use ＜skills＞ router.", "PASS")` would close it (the battery has `plant-fullwidth` with `intent_fail=None`, i.e. left undecided).

### F4 — LOW — the YAML-escape branch ignores quote context; the docstring overstates it

`verifiers/verify_skill_checklist.py:409` + `:1304` apply `YAML_ANGLE_ESCAPE_RE` to the parsed value regardless of how the scalar was quoted. The docstring (`:100-101`) says *"a YAML **double-quoted** `\x3c`/`\u003c` escape that decodes to one"*, but in a single-quoted or plain scalar YAML does **not** decode the escape — the value holds literal `\u003c` text, which no client sees as `<`. Observed:

```
parse_frontmatter(['---','name: x','description: \'Use the \u003cskills\u003e router.\'','---',''])
  -> {'name':'x','description':'Use the \\u003cskills\\u003e router.'}
  -> FAIL trigger.no_xml_tag: XML tag in description: '\\u003c'
```

So the implementation is broader than its own prose. It fails closed (harmless), but the prose over-claims specificity. `C2CriticRule.md` §3 does record this ("a theoretical FP only for a plain scalar that spells the escape literally"), so the behaviour is known — only the docstring wording is off.

### F5 — LOW — the split fixture kills only *per-line* raw scanners, not a whole-file raw scanner

`C2CriticRule.md` §5 credits `xml-tag-split` with killing "raw-line scanners". Measured against the raw fixture text with the shipped `XML_TAG_RE`:

| fixture | per-line raw hit | whole-file raw hit |
|---|---|---|
| xml-tag-codespan | true | true |
| xml-tag-split | **false** | **true** |
| xml-tag-dq-escape | false | false |

A per-line raw scanner is killed by `xml-tag-split` ✓ (its `</Skills` / `>` split is invisible per line). A whole-file raw scanner is **not** killed by it: `\s` in the regex matches the newline, so `</Skills\n>` matches on the raw text too. (`xml-tag-dq-escape` does kill both raw scanner kinds.) The claim is right for one reading of "raw-line scanner" and wrong for the other — worth one word of clarification, not a code change.

### F6 — LOW (adjacent, outside the fixture scope) — the floors gate is host-load-fragile

`python3 -B verifiers/check_assertion_floors.py` in my scratch clone exits **2**, with `FAIL harness_independent self-test timed out after 120s (hung?)`; `python3 -B verifiers/verify_harness_independent.py --self-test` alone takes **113 s** (`real 1m53.512s`, `0 failure(s) over 104 assertions`, exit 0) against the guard's 120 s cap — a ~7 % margin. The round's after-summary claims `floors exit=0` (`.ufo/waves/round-47/after/SUMMARY.md`). The same timeout was already observed at BASE by the wave-1 critic (`C2CriticRule.md`, "Commands run": *"The same run printed `FAIL harness_independent self-test timed out after 120s`, which is unrelated to C2 and probably host load"*). Not reproduced in the lane repo — I may not write there and could only run read-only — so lane-repo reproduction is **unobserved**; the defect is the missing head-room on a gate the round reports as green.

---

## 3. Mutation matrix (the core of the attack)

Method: for each mutant, a tree of symlinks to the repo root + a patched copy of `verifiers/` (so `DEFAULT_REPO` still resolves), then `--self-test` plus the four fixtures and the seven broken-frontmatter cases. `flips` = fixture whose verdict changed; `selftest=0` with `flips=[]` = **survives**.

```
 id                        selftest  flips                            killed by
 M1 strip-quoted-spans     1         xml-tag-codespan                  codespan needle '<skills>'
 M2 strict tag             1         xml-tag-split                     split needle '</Skills >'
 M3 drop YAML-escape       1         xml-tag-dq-escape                 dq needle '\\u003c'
 M4 any-angle '[<>'        1         xml-tag-control                  control exit 0->1
 M5 name-only              1         xml-tag-control                  control exit 0->1 + needles
 M6 start-tag-only         1         xml-tag-split                     split needle
 M7 lowercase-naive        1         xml-tag-split                     split needle
 M9 drop comment branch    1         (none)                            string battery only
 M10 entity-decode         1         xml-tag-control                  control exit 0->1
 M11 NFKC-normalise        0 SURV    (none)                            NOTHING            (F3)
 M12 description-only      1         (none)                            control needle
 M13 strict + no comment   1         xml-tag-split                     split needle
 M17 fail-open guard       1         (none)                            7 broken-frontmatter cases
 M19 loose angle           1         (none)                            string battery only  (F1)
 M20 scan first 80 chars   1         codespan,split,dq-escape          the three needles
 M21 drop CDATA branch     0 SURV    (none)                            NOTHING            (F2)
 M22 drop PI branch        0 SURV    (none)                            NOTHING            (F2)
 M23 drop declaration      0 SURV    (none)                            NOTHING            (F2)
 M24 drop comment only     1         (none)                            string battery only
 M26 scan EVERY field      1         xml-tag-control                  control exit 0->1 (metadata '<internal>')
 M27 space after '<'       1         (none)                            string battery only  (F1)
```

Reads:
* **Each of the four fixtures kills the class it is named for**: codespan→span-stripping (the defect `C2CriticRule.md` §3 calls "the most likely build defect", because `ALL_QUOTED_SPANS_RE` already exists at `:398`); split→lowercase-naive *and* no-whitespace-before-`>` *and* start-tag-only; dq-escape→escape-blind; control→any-bracket, all-fields scan, name-only, description-only, entity-decode.
* The tag grammar is **XML-1.0-accurate**: `</Skills >` is a well-formed end tag (XML 1.0 `End-tag ::= '</' Name S? '>'` allows the space), so the "folded split" fixture is well-founded, and `a < b` is correctly not a tag (XML requires a name character right after `<`).
* The dq-escape fixture is faithful to the structural parser (`parse_frontmatter` at `:515` decodes nothing), so the escape branch is load-bearing: dropping it turns the fixture green.

---

## 4. The seven frontmatter-broken fixtures — 7/7 confirmed

`verifiers/verify_skill_checklist.py` `CASES` table: `no-frontmatter` :1781-1785, `fm-null` :1786-1789, `fm-malformed` :1790-1794, `fm-dup-key` :1795-1799, `fm-body-yaml` :1800-1804, `fm-stray-indent` :1810-1814, `empty-file` :1869-1873 — each lists `"trigger.no_xml_tag"` in its `fails` list (and `trigger.no_xml_tag` is in `CHECK_IDS` at `:310`).

Runtime (exit code 1 each, one line each):

```
no-frontmatter  FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: no leading ---
fm-null         FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: empty description:
fm-malformed    FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: unbalanced quote in scalar '"unclosed scalar'
fm-dup-key      FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: duplicate key 'name'
fm-body-yaml    FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: no leading ---
fm-stray-indent FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: stray indented line 'orphan indented line with no field above'
empty-file      FAIL trigger.no_xml_tag: evaluated 0 — cannot evaluate: no leading ---
```

The fail-closed contract is load-bearing: the mutant `M17-fail-open-guard` (`fields is None → "PASS", 0`) is caught **only** by these seven cases (`self-test FAIL: no-frontmatter: FAIL trigger.no_xml_tag: got 'PASS …'` and `… 'evaluated 0' line is not a PASS …`). No xml-tag-* fixture covers it.

---

## 5. `map.json` review

* All four `map.json` files are **byte-identical** (`md5 ca96663c23f6dadc7b5bc8f69cdbbfee`), and the four `SKILL.md` bodies are byte-identical from `# clean` onward; only the frontmatter differs. Deliberate isolation of one variable per fixture — acceptable, but note the map's `text_sha256` cannot distinguish the four fixtures (a body swap between them is invisible to the map; a frontmatter swap is caught by `trigger.name_directory`).
* The pinned hashes **recompute correctly** under the documented normalisation rule (`verifiers/verify_skill_checklist.py:18-22`): "First box text for this fixture. (executed: \`trigger.line_budget\`)" → `d87e45246965533d71b96c11525a4f6b1f0ce5b94e08c0f5aeb1977b1a82c052`; "Second box text for this fixture, with a continuation line to exercise multi-line box extraction." → `7b66c0712ce44dddb17bed02e46423a68c86d1656774204dd096a40353748fb6` — matching `map.json:8` and `map.json:14` in all four files.
* `file: "SKILL.md"` matches the target basename; `fixture.01` disposition `executed:trigger.line_budget` names a live check id; `fixture.02` is `unexecuted:fixture review`; `checklist.box_map_complete` PASSes with `evaluated 2` in all four.
* No `box_total` key — optional per `load_map` (`:480-487`).

---

## 6. Adjacent observations (not fixture defects, recorded for the integrator)

* The rule's **own design record is not in `corpus/`**: the 35-case battery lives only at `.ufo/waves/round-47/build/C2CriticRule.battery.json`; `corpus/knowledge/description-xml-tag-rule-round47.md` was proposed by the wave-1 lane (`KnowDescriptionRule.md` §5: *"NOT in corpus/; L1 admits"*) and does **not** exist at 7ad7fad. `corpus/README.md` has no row for the new rule; the only mention is a parenthetical inside the *loader-freshness* row (`corpus/README.md:76`, "the XML-token rule moved to Core (`trigger.no_xml_tag`)"). Since F2 shows the durable assertions are thinner than the rule's prose, the corpus index would be the natural home for the battery.
* `corpus/SOURCES.md:25` (S012) records that Anthropic's packager *"refuses any `<` or `>` in `description`"* — a **stricter** rule than the one implemented. The check's own `limit` string discloses this (`verifiers/verify_skill_checklist.py:1307-1308`), and `C2CriticRule.md` §1 records it as a deliberate tradeoff ("keep the tag grammar under the S003 label, and record the stricter packager rule as a named limit"). Not a defect — but note that adopting S012 later would make `xml-tag-control` fail by design, so the dependency is worth writing down next to the fixture.

---

## 7. What I did NOT check

* **C1 (freshness)** — the omp 18.12.5 / opencode 1.19.3 re-derivation and re-pin: not re-run (out of scope). I did not open the frozen strings dumps or the substrate binaries.
* **C3 (calibration)** — the governance erratum (`LOG.md:2111`), the corpus index row, `corpus-baseline.json` 58→60, and the fault-harness planter fix: not re-run. I only read `corpus/lessons/round-47.md`, `corpus/SOURCES.md:25-28`, `corpus/QUALITY.md:30` and `corpus/README.md` in passing. The fault harness (`verifiers/fault_injection_corpus.sh`) contains **no** reference to the xml fixtures or `trigger.no_xml_tag` (grep: 0 hits) — I did not determine whether it should.
* The `--self-test` assertion-count delta 1597 → 1845: I confirmed 1845 at 7ad7fad and the floor value 1845 in `verifiers/floors-registry.json`, but did not re-measure the BASE count or attribute the +248 to individual arms.
* **A real YAML parser** (PyYAML) was not run against the four fixtures; the folding/escape reasoning is from the verifier's own structural parser plus the YAML spec. I did not test CRLF files, YAML anchors/aliases (`*d`), `!!str` tags, multi-document frontmatter, or a `name` field with a tag other than `<x>`.
* The live Anthropic packager (`quick_validate.py`), the Skills API and claude.ai upload enforcement: not run, no upload attempted.
* I did not run any verifier inside `/home/vgpnk/Projects/shokunin/kotoba-shokunin` other than read-only greps and the read-only frontmatter count; all execution happened in the scratch clone. Consequently F6's lane-repo reproduction is unobserved.
* I did not evaluate whether the four fixtures should also live under `verifiers/fixtures/` for a different harness, nor whether a fixture-level inventory/baseline should list them (I found no such inventory).

---

## 8. Appendix — repro harness (self-contained)

```bash
# in a clone of the repo at 7ad7fad (my scratch: /fast/scratch/kotoba-r47/w2/W2XmlFixtures/kotoba-shokunin)
REPO=$PWD
D=/fast/scratch/kotoba-r47/w2/W2XmlFixtures/mut3/M27-space-after-lt
rm -rf "$D"; mkdir -p "$D"
for e in "$REPO"/*; do ln -sfn "$e" "$D/$(basename "$e")"; done   # repo root as symlinks
cp -r "$REPO/verifiers" "$D/verifiers"                            # patched copy below

# 1) the mutation (anchors: W2XmlFixtures.mutants.txt)
python3 - "$D" <<'PY'
import sys, pathlib
d = pathlib.Path(sys.argv[1])
f = d / "verifiers" / "verify_skill_checklist.py"
s = f.read_text()
old = r'r"</?[A-Za-z_][\w.:-]*(?:\s[^<>]*)?/?>"'
new = r'r"</?\s*[A-Za-z_][\w.:-]*(?:\s[^<>]*)?/?>"'
assert s.count(old) == 1
f.write_text(s.replace(old, new))
PY

# 2) the gate and the fixtures
python3 -B "$D/verifiers/verify_skill_checklist.py" --self-test      # -> exit 1
python3 -B "$D/verifiers/verify_skill_checklist.py" --repo "$REPO" \
  --skill "$D/verifiers/fixtures/checklist/xml-tag-control/SKILL.md" \
  --map  "$D/verifiers/fixtures/checklist/xml-tag-control/map.json"  # -> exit 0  (F1: not killed)
```

Mutation anchors used (all at 7ad7fad):
`verifiers/verify_skill_checklist.py:404-406` (`XML_TAG_RE`), `:409` (`YAML_ANGLE_ESCAPE_RE`), `:1298` (`present` list), `:1303-1304` (`val`/`search`).
