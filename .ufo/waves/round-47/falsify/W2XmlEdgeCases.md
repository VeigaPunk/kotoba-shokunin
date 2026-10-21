verdict: PARTIAL — C2 no_xml_tag catches the requested ordinary markup, but has undeclared escape false positives and an ASCII-only XML-name false negative.

# Scope and axes

Reviewed `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` in the canonical-layout scratch clone `/fast/scratch/kotoba-r47/w2/W2XmlEdgeCases/kotoba-shokunin`. Axes: **freshness** (source/version identity), **operability** (accept clean descriptions and reject actual markup), **calibration** (PASS/FAIL claims match the implemented and disclosed boundary). This is scoped lane-authored criticism, not admission or canonical judgment. Production files were not changed; this report is the only production-lane write. No tools were installed or updated.

# Commands and evidence

`git rev-parse HEAD` in the scratch clone exited **0**, output `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`.

`python /fast/scratch/kotoba-r47/w2/W2XmlEdgeCases/probe.py` exited **0**. The probe generated 16 frontmatter documents under the scratch clone's `xml-edge-cases/`, launched the verifier CLI concurrently (8 workers), captured each subprocess exit/JSON, and compared structural fields with **PyYAML 6.0.3** `yaml.safe_load`. Python was **3.14.8**. The probe wrapper's exit 0 means successful evidence collection, not that its child checks all passed.

Each table row used the following actual command, with `<case>` replaced by its table ID (absolute paths in the probe):

```sh
cd /fast/scratch/kotoba-r47/w2/W2XmlEdgeCases/kotoba-shokunin
/usr/bin/python verifiers/verify_skill_checklist.py \
  --repo /fast/scratch/kotoba-r47/w2/W2XmlEdgeCases/kotoba-shokunin \
  --skill /fast/scratch/kotoba-r47/w2/W2XmlEdgeCases/kotoba-shokunin/xml-edge-cases/<case>.md \
  --check trigger.no_xml_tag --json
```

All 16 subprocesses had empty stderr and `evaluated: 2`. Each fixture was `---`, the frontmatter shown below, `---`, and `# Edge case`. Unless specified otherwise the other field was `name: edge` or `description: Use for edge.`. `\n` in table cells denotes an actual newline; backslashes in escape cases denote literal source bytes, not table decoding.

| Case ID | Crafted field(s) | CLI exit/status | S003 and stated-limit assessment |
|---|---|---|---|
| `alias` | `metadata:\n  note: &d "Use <skills> here."\ndescription: *d` | **0 PASS** | YAML resolves description to `Use <skills> here.`: violates S003, but aliases are expressly excluded at verifier lines 213–215. Named ceiling, not a newly undisclosed regression. |
| `literal_split_name` | `description: |\n  Use <ski\n  lls> here.` | **1 FAIL**; hit `'<ski lls>'` | No bypass. Structural parser joins lines; actual YAML retains newline. This is a broad tag-shape match, not proof of well-formed XML (the bare `lls` attribute is invalid XML). Matches the detector's broad shape, with the same ambiguity as the comparison row. |
| `literal_split_attributes` | `description: |\n  Use <skills\n  > here.` | **1 FAIL**; hit `'<skills >'` | Correct: newline is legal whitespace before closing `>`; literal scalar does not evade the check. |
| `double_quote_hex` | `description: "Use \x3cskills\x3e here."` | **1 FAIL**; hit `'\\x3c'` | Correct: PyYAML decodes `Use <skills> here.`; meets the documented double-quoted escape rule. |
| `fullwidth` | `description: Use ＜skills＞ here.` | **0 PASS** | Literal fullwidth characters are not XML delimiters. Matches the literal S003 reading and named fullwidth/NFKC ceiling; no normalization claim is proved. |
| `comment` | `description: Use <!-- --> here.` | **1 FAIL**; hit `'<!--'` | Correct under the check's explicit inclusion of XML comments (lines 98–100); S003 itself does not enumerate markup subtypes. |
| `comparison_ambiguous` | `description: a <b and c> d` | **1 FAIL**; hit `'<b and c>'` | Conservative shape rejection, not an intent classifier. Matches its `<` immediately followed by name-character rule, but `and c` are not valid XML attributes. Do not call this a demonstrated S003 parser-equivalence result. |
| `metadata_note` | `metadata:\n  note: <x>` | **0 PASS** | Correct field boundary: S003 constrains name/description, not arbitrary metadata. |
| `when_to_use` | `when_to_use: <x>` | **0 PASS** | Correct to its explicit field boundary and named `when_to_use` ceiling. This does not prove a composed Claude Code listing has no tags. |
| `name` | `name: <x>` | **1 FAIL**; hit `name: '<x>'` | Correct: S003's live field list also prohibits XML tags in name; other name-format rules were not run. |
| `single_quote_escape` | `description: 'Use \x3cskills\x3e here.'` | **1 FAIL**; hit `'\\x3c'` | **False positive:** YAML single quotes do not decode these escapes; no tag or literal angle bracket exists. Not covered by the stated double-quoted escape rule. |
| `double_quote_comparison_escape` | `description: "a \x3c b"` | **1 FAIL**; hit `'\\x3c'` | **False positive:** decoded value is `a < b`, explicitly a permitted comparison, not a tag. This accidentally enforces an angle ban on escaped comparisons while permitting the literal spelling. |
| `double_quote_literal_backslash` | `description: "Use \\x3cskills\\x3e here."` | **1 FAIL**; hit `'\\x3c'` | **False positive:** YAML consumes each escaped backslash, yielding literal `\x3cskills\x3e`, not markup. The regex matches at the second backslash without considering parity. |
| `unicode_xml_name` | `description: Use <技能> here.` | **0 PASS** | **False negative:** a legal Unicode XML start-tag name is excluded by the ASCII first-character class. No ASCII-only ceiling is disclosed. |
| `colon_xml_name` | `description: Use <:skills> here.` | **0 PASS** | Regex excludes initial colon, which XML 1.0 Name permits; XML Namespaces imposes additional QName restrictions. This secondary edge is not needed for the Unicode finding and no namespace-aware acceptance is claimed. |
| `control` | `description: a < b and c > d` | **0 PASS** | Correct: comparison whitespace prevents tag matching, as documented. |

Additional executed control:

```sh
python verifiers/verify_skill_checklist.py --check trigger.no_xml_tag --json
```

In the clone this exited **0**, `PASS`, `evaluated: 2`, `no XML tag in name, description`. The actual landed description survives this isolated check.

# Finding 1 — escape handling violates its own narrower contract

**Evidence at landed revision:** `verifiers/verify_skill_checklist.py:97–104` promises double-quoted YAML escapes that decode to markup; `:407–409` defines a raw backslash/hex regex; `:588–592` strips quote style from field values; `:1302–1304` applies that regex to every present field regardless of original scalar style or decoded tag shape. `:210–216` names several ceilings, but not this false-positive class.

**Smallest counterexample / repro:** create `xml-edge-cases/single_quote_escape.md` in the scratch clone:

```yaml
---
name: edge
description: 'Use \x3cskills\x3e here.'
---
```

Run the per-row command: exit **1**, JSON reports `XML tag in description: '\\x3c'`. `yaml.safe_load` instead yields the literal string `Use \\x3cskills\\x3e here.` in Python repr, containing neither `<` nor `>`. Even S012's stricter *decoded* angle-bracket predicate would not reject this text on angle brackets; the reference packager was read, not executed.

The decoded-comparison and escaped-backslash rows independently demonstrate that simply restricting this regex to double-quoted scalars does **not** finish the correction.

**Impacted axes:** operability (clean descriptions rejected); calibration (reported “XML tag” is absent, even under the declared source distinction). No freshness regression established.

**Smallest safe correction:** retain scalar-style information, decode YAML double-quoted escapes with their actual backslash semantics, and apply the same markup predicate to the decoded value. Do not apply the angle-escape regex to single-quoted/plain/block scalar text; do not reject a decoded angle unless it forms the prohibited markup shape. Add the three negative controls plus the existing positive hex-tag case. This is a fixable implementation defect, not a request to replace S003 with S012's stricter rule. Adopting an unconditional encoded-angle ban instead would be a contract tradeoff, not a no-harm fix.

# Finding 2 — “XML 1.0 markup shapes” silently means ASCII-start names

**Evidence at landed revision:** `verifiers/verify_skill_checklist.py:401–406` labels the regex XML 1.0 but uses `</?[A-Za-z_]` for start/end names and `[A-Za-z_]` for processing instructions. `:97–104` says “a name character,” not “ASCII name character”; `:210–216` does not disclose this restriction. The Unicode description row exits **0** while containing `<技能>`.

Additional parser probe exited **0** (exact command):

```sh
python -c 'import xml.etree.ElementTree as E; samples=["<技能/>", "<b and c/>", "<skills\n/>"]; [(print(repr(s), "ACCEPT", E.fromstring(s).tag) if s != "<b and c/>" else None) for s in samples]; print("literal single-quoted YAML has no markup:"); import yaml; print(repr(yaml.safe_load("description: '\''Use \\x3cskills\\x3e here.'\''")["description"]))'
```

Output included `'<技能/>' ACCEPT 技能` and `'<skills\n/>' ACCEPT skills`. This establishes a real XML name, not fullwidth-delimiter normalization. The actual detector CLI was exercised on the start tag `<技能>`, not on a complete XML document; S003 bans tags, not only well-formed documents. The command intentionally skipped parsing the ambiguous `<b and c/>` sample, so it supplies no parser verdict on that sample.

**Impacted axes:** operability (real tags accepted); calibration (unqualified “no XML tag” claim exceeds implemented coverage). No freshness regression established.

**Smallest safe correction:** extend markup-name recognition to XML 1.0 NameStartChar/NameChar (including applicable Unicode ranges) and add positive fixtures for non-ASCII start/end/empty-element tags. Keep the comparison controls. Merely documenting ASCII-only coverage is a calibration-only alternative that does not close the S003 detector defect; the canonical judge must distinguish that tradeoff from an implementation fix.

# Source reopening and limits

Opened S003's actual URL, `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices` (served as its Markdown alternate). Its **Skill structure** field list says both name and description “Cannot contain XML tags.” This confirms `corpus/SOURCES.md:16` and that name scanning is intentional, not field-scope creep.

Opened S012's pinned source, `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`. It calls `yaml.safe_load` and then checks `if '<' in description or '>' in description`; this supports `corpus/SOURCES.md:25` and the deliberately stricter packager distinction. It was **not executed**. Its ban must not silently replace S003's tag predicate.

Opened `https://www.w3.org/TR/xml/#NT-NameStartChar`; the reader returned W3C recommendation metadata rather than the grammar body, so no fetched grammar-body quotation is claimed. The executed ElementTree Unicode example supplies the local parser evidence.

# Not checked

No full checklist/self-test, corpus gates, fault harness, C1 surface census, pin gates, C3 errata, fleet sweep, or host-substrate execution was performed in this scoped review. No omp session or opencode wrapper was launched. No mutations were committed: this checker reads the supplied files directly, so committed-state harness behavior was not under test. No alternative YAML implementation or live Claude Code description composition was exercised. Ambiguous comparison/attribute-shaped strings are reported as heuristic tradeoffs, not padded as additional proven defects. None of the findings claims the landed real SKILL.md itself currently contains an XML tag.
