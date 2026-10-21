verdict: PARTIAL — XML-tag Frontier→Core claim has a reproducible Unicode-tag hole; the narrowed loader-freshness residual is honestly named and reproduced.

## Scope and axes

Reviewed commit `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` in canonical-layout scratch clone `/fast/scratch/kotoba-r47/w2/W2ProvinceMove/kotoba-shokunin` (`git rev-parse HEAD`, exit 0, exact hash above). Axes: freshness (loader re-derivation and remaining rename fragility), operability (executed XML rejection), calibration (Core wording versus demonstrated boundary). No production edits, integration, judgment-runtime invocation, subagents, installs, or upgrades.

## F1 — Core promotion overstates the XML-tag boundary

**Counterexample:** a description containing `<技/>` or `<é/>` is accepted as containing no XML tag. Both are actual XML elements according to Python's XML parser. This is not the consciously excluded arrow/comparison case and is not merely the stricter S012 ban on arbitrary angle brackets.

**Evidence at 7ad7fad:**

- `PROVINCE.md:15` moves the frontmatter XML-tag rule into Core and claims execution on name/description, with four discriminating fixtures.
- `corpus/README.md:76` repeats that the XML-token rule moved to Core.
- `corpus/SOURCES.md:16` gives S003's unqualified description XML-tag prohibition; `corpus/SOURCES.md:25` separately and honestly distinguishes the stricter S012 angle-bracket rule.
- `verifiers/verify_skill_checklist.py:401-406` labels the matcher “XML 1.0 markup shapes” but restricts the first element-name character to `[A-Za-z_]`. XML names are not restricted to that ASCII initial set.
- `verifiers/verify_skill_checklist.py:1302-1313` uses that matcher and then returns `PASS ... no XML tag in name, description`.

**Commands and observed results:**

1. `python verifiers/verify_skill_checklist.py --self-test` — exit 0, `0 failure(s) over 1845 assertions` (run before the scratch mutation).
2. Direct checker/parser probe — exit 0:

```sh
python -c 'import importlib.util; p="verifiers/verify_skill_checklist.py"; s=importlib.util.spec_from_file_location("probe",p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); import xml.etree.ElementTree as E; cases=["<skills/>","<技/>","<é/>","<skills\u00a0/>","a < b"]; [(print(repr(x), "xml="+str(E.fromstring(x).tag) if x.startswith("<") and "\u00a0" not in x else "control", m.check_no_xml_tag(({"name":"kotoba-shokunin","description":"Use for audit. "+x},"")))) for x in cases]'
```

Key output: `<skills/>` → XML parser `skills`, checker FAIL; `<技/>` → XML parser `技`, checker PASS; `<é/>` → XML parser `é`, checker PASS; `a < b` → checker PASS.

3. End-to-end fixture mutation in scratch only: append ` Also <技/>.` to `verifiers/fixtures/checklist/xml-tag-control/SKILL.md:7`, leaving its map and all other bytes unchanged. Then:

```sh
python verifiers/verify_skill_checklist.py \
  --skill verifiers/fixtures/checklist/xml-tag-control/SKILL.md \
  --map verifiers/fixtures/checklist/xml-tag-control/map.json
```

Exit 0. Key output:

```text
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='xml-tag-control', description 236 chars
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)
```

All other applicable fixture checks also PASS; citation/governance checks are N/A for this fixture. Thus the counterexample crosses the real frontmatter parser and CLI, not only an isolated regex.

**Impacted axes:** operability (false green on the named rule), calibration (unqualified Core boundary despite surviving legal XML tags). No inference of harm to loader freshness from this defect.

**Smallest safe correction:** implement the XML NameStartChar/NameChar boundary, including non-ASCII legal XML initial characters, and add an end-to-end Unicode element fixture plus a comparison control. Keep S012's stricter all-angle prohibition distinct; changing to that stronger prohibition would introduce a different policy and break deliberate comparison controls. Until repaired, narrow the Core bullet to the executed subset and retain Unicode-tag coverage as a named Frontier residual. This is a fixable detector defect, not a tradeoff requiring abandonment of the task.

The four existing fixture families and the self-test are real executed evidence; this report does not deny that bounded gain. The unqualified claim is what the counterexample falsifies. A reviewer can reproduce it without trusting lane-authored receipts, so the move is externally verifiable—but the verification finds a missing boundary, not full closure. `LEARNING.md:75-78` permits ordinary frontier growth; it does not make a declaration of Core proof of coverage. This lane-authored review is not the outside spot-check required by `LEARNING.md:42-48`.

## F2 — Narrowed loader-freshness residual survives the attack

`PROVINCE.md:22` explicitly marks old 5/7 and 1/3 figures historical, records 18.12.5/1.19.3 re-pinning, and retains manual re-derivation after rebuild as not held. `corpus/README.md:76` names the callee allowlist, next-rename failure, manual correction, and an opencode generation probe as the next work. This is a bounded residual, not a claim of rename robustness.

Re-ran in the same pinned scratch tree:

- `python verifiers/verify_surfaces.py` — exit 0, seven PASS rows; 42 loader-kind entries; all 8 extracted omp classes declared; opencode 9/9 classes from 7/7 rules; table/literal/kind parity and excluded reasons hold.
- `python verifiers/check_substrate_pins.py` — exit 0, `OK 3/3 pins hold`; omp SHA-256 `fdbc8136084c9a10439569157b2af62312e2b0d801cab54c73e89476da798e7e`, mtime delta 0 ns, opencode SHA-256 `179ca421d61eefeadfa0c50e084a6e79c1623734732f0f4593f81ccfd3ab7ee9`.

These commands use the verifier's default resolved ELF targets; they do not execute the opencode wrapper or launch omp sessions.

Cheap rename mutation, exit 0:

```sh
python -c 'import importlib.util,pathlib; s=importlib.util.spec_from_file_location("surfaces","verifiers/verify_surfaces.py"); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); d=pathlib.Path("verifiers/fixtures/surfaces/strings-omp-18.12.5.txt").read_text(); before=m.extract_classes(d,"omp"); after=m.extract_classes(d.replace("lq(","zz(").replace("Xl(","yy(").replace("Fo(","xx("),"omp"); print("before",len(before),sorted(before)); print("after",len(after),sorted(after)); print("lost",len(before-after)); assert len(before)==8 and len(after)==0'
```

Observed `before 8`, `after 0`, `lost 8`. This directly reproduces the named extractor dependence. Source anchors: `verifiers/verify_surfaces.py:156-159` (callee allowlist), `:316-333` (extraction), `:348-352` (explicit non-exhaustiveness), and `:354-364` (generation note). The full renamed-dump gate was not run; the extraction loss, not a fresh full-gate exit code, is the observation here.

**Impacted axes:** freshness/calibration. The current 7/7 and 3/3 results hold in this run; the manually maintained residual remains real and named. **Smallest safe correction:** none to the residual wording on this evidence. Do not treat the current green battery as proof of future-generation loader completeness. The XML exception in F1 must be restored/narrowed independently.

## What I did not check

Did not independently reopen upstream S003/S012 web content, re-derive opencode lineage from all binary anchors, rerun the before tree, mutation-test every loader rule, run corpus integrity/independent/fault-harness/C3 erratum gates, inspect all 1845 assertion implementations, test the entire XML character repertoire, or provide a non-author admit/reject spot-check. Those are outside this scoped Province/Frontier attack. The observed Unicode counterexample needs none of those assumptions. Scratch fixture mutation is uncommitted; no gate that reads committed corpus state was used for that mutation. No production files except this report were written.
