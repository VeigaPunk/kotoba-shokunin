verdict: PARTIAL — attacked trigger.no_xml_tag self-test sensitivity; 7/9 single-defect mutants killed, CDATA and PI deletions survived.

# W2 XML detector mutation probe

Target revision: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`. All source line references below are at that revision, not at a mutant. Author: `KotobaR47-2.W2XmlMutants-2`; lane-authored falsification evidence only, not non-author closure or integration.

## Axes and boundary

- **Freshness:** cloned and detached the exact landed revision; all nine pristine verifier SHA-256 values were identical (H0 below). No live substrate version claim was re-verified.
- **Operability:** ran the identical bounded `--self-test` on pristine, mutated, and exactly restored bytes in every isolated clone. Each invocation had a 90-second timeout; none timed out.
- **Calibration:** separate self-test kills from survivors and from the supplemental targeted oracle. A green pristine/restored run is required before counting a kill. No baseline failure or inconclusive mutant occurred.

The seven requested mutation categories became **nine independent one-defect probes**: the last category was split into comment, CDATA, and PI arm deletions. Removing all three together would let the existing comment case mask missing coverage for the other two. `M7NoSpecialMarkup` is the scratch directory name for the **comment-only** deletion; it does not remove all three arms. No contract, production source, fixtures, or production Git/jj state was changed.

## Findings

### F1 — deleting the CDATA arm survives the committed self-test

- Behavior-bearing point: `verifiers/verify_skill_checklist.py:406`, remove only `|<!\[CDATA\[`; keep regular element, comment, PI, and declaration matching intact.
- Contract: `verifiers/verify_skill_checklist.py:97-104` explicitly forbids CDATA. The regex implements that at `:404-406`.
- Actual `--self-test` output, pristine → mutant → restored: **exit 0 / 0 / 0**, each printing `0 failure(s) over 1845 assertions`.
- Non-equivalence counterexample: fields `{"name":"x","description":"Use <![CDATA[x]]> here."}`. The same targeted oracle on pristine → mutant → restored returns **FAIL → PASS → FAIL**. Its aggregate assertion exit codes are **0 → 1 → 0**. The mutated check reports `no XML tag in name, description` despite that CDATA text.
- Coverage anchor: `verifiers/verify_skill_checklist.py:1971-1980` tests comments (`:1975`) but carries no CDATA row. The observed survival is a self-test coverage finding, **not a claim that the landed detector currently accepts CDATA**; the pristine detector rejected this example.

### F2 — deleting the PI arm independently survives the committed self-test

- Behavior-bearing point: `verifiers/verify_skill_checklist.py:406`, remove only `|<\?[A-Za-z_]`; keep the other arms.
- Actual `--self-test` output, pristine → mutant → restored: **exit 0 / 0 / 0**, each printing `0 failure(s) over 1845 assertions`.
- Non-equivalence counterexample: fields `{"name":"x","description":"Use <?xml version=\"1.0\"?> here."}`. Targeted oracle statuses: **FAIL → PASS → FAIL**; aggregate assertion exit codes: **0 → 1 → 0**.
- Coverage/contract anchors: processing instructions are named at `verifiers/verify_skill_checklist.py:100` and implemented at `:406`, but not represented in the string battery at `:1971-1980`. Again this demonstrates a regression can escape `--self-test`, not a present production acceptance defect.

## Kill matrix

Command in each clone: `python3 -B verifiers/verify_skill_checklist.py --self-test`.

P / M / R = pristine / mutated / restored exit codes. All runs evaluated **1845 assertions**. Verdicts in this table use **only the committed self-test**. The supplemental oracle was not added to that self-test and does not turn a survivor into a self-test kill.

| Mutant | Smallest change | Source line(s) | P / M / R | Mutant self-test output | Verdict | Targeted expected → actual on mutant |
|---|---|---|---|---|---|---|---|
| M1Backticks | Strip backtick spans before scanning | `1303` | 0 / 1 / 0 | 3 failure(s) | **KILLED** | `FAIL → PASS` |
| M2Description | Scan description only | `1302` | 0 / 1 / 0 | 1 failure(s) | **KILLED** | `FAIL → PASS` |
| M3Lowercase | Lowercase-only element-name regex | `405` | 0 / 1 / 0 | 3 failure(s) | **KILLED** | `FAIL → PASS` |
| M4NoYamlEscape | Drop YAML-escape scan arm | `1304` | 0 / 1 / 0 | 3 failure(s) | **KILLED** | `FAIL → PASS` |
| M5Whitespace | Allow whitespace immediately after < | `405` | 0 / 1 / 0 | 1 failure(s) | **KILLED** | `PASS → FAIL` |
| M6AnyBracket | Ban any ASCII angle bracket | `404–406` | 0 / 1 / 0 | 7 failure(s) | **KILLED** | `PASS → FAIL` |
| M7NoSpecialMarkup | Drop comment alternation only | `406` | 0 / 1 / 0 | 1 failure(s) | **KILLED** | `FAIL → PASS` |
| M8NoCdata | Drop CDATA alternation only | `406` | 0 / 0 / 0 | 0 failure(s) | **SURVIVED** | `FAIL → PASS` |
| M9NoPi | Drop processing-instruction alternation only | `406` | 0 / 0 / 0 | 0 failure(s) | **SURVIVED** | `FAIL → PASS` |

Counting method over the recorded subprocess results: `sum(mutant_exit == 1) = 7`, `sum(mutant_exit == 0) = 2`, baseline/restoration failures `= 0`. See `matrix` and `counts` in the evidence artifact. The last column uses the explicit contract oracle, not the self-test exit code; `FAIL → PASS` is a false negative, `PASS → FAIL` a false positive.

### Expected detector anchors

- M1: `verifiers/verify_skill_checklist.py:1806`; `verifiers/fixtures/checklist/xml-tag-codespan/SKILL.md:6` carries backticked `<skills>`. Mutation changes only `val = fields[key]` at `:1303` to `BACKTICK_SPAN_RE.sub("", fields[key])`.
- M2: `verifiers/verify_skill_checklist.py:1977` supplies a tag in `name` alone. The scan list is defined at `:1298`; the mutant changes only the loop at `:1302` to `for key in ("description",):`.
- M3: `verifiers/verify_skill_checklist.py:1807`; `verifiers/fixtures/checklist/xml-tag-split/SKILL.md:6-7` folds to `</Skills >`. At `:405`, the mutant uses `[a-z_][a-z0-9_.:-]*` instead of `[A-Za-z_][\w.:-]*` for ordinary element names; special-markup arms are unchanged.
- M4: `verifiers/verify_skill_checklist.py:1808`; `verifiers/fixtures/checklist/xml-tag-dq-escape/SKILL.md:3`. The mutation removes only `or YAML_ANGLE_ESCAPE_RE.search(val)` at `:1304`; the escape regex at `:409` remains present but unused by this check.
- M5: `verifiers/verify_skill_checklist.py:1978` pins the legal comparison control. Adding `\s*` immediately after `<` at `:405` falsely matches `< b and c >` within `a < b and c > d`.
- M6: `verifiers/verify_skill_checklist.py:1809,1978-1979`; `verifiers/fixtures/checklist/xml-tag-control/SKILL.md:5-7`. Replacing the regex expression at `:404-406` with `re.compile(r"[<>]")` overrejects comparisons and arrows, contradicting the named packager-vs-rule distinction at `:210-216`.
- M7: `verifiers/verify_skill_checklist.py:1975` supplies `Use <!-- c --> here.` and kills removal of only the comment arm at `:406`.
- M8/M9: expected CDATA/PI rejection follows the documented contract at `:97-104`, but the committed detector has no sensitive assertion for these isolated deletions in this run.

### Actual key stdout (mutated runs)

Full unabridged stdout/stderr are stored in the JSON artifact; these are literal short failure lines and summaries extracted from those results:

```text
M1Backticks
self-test FAIL: xml-tag-codespan: exit 1: got 0
3 failure(s) over 1845 assertions
M2Description
self-test FAIL: no_xml_tag['<x>'/'Use for x.']: FAIL: got 'PASS'
1 failure(s) over 1845 assertions
M3Lowercase
self-test FAIL: xml-tag-split: exit 1: got 0
3 failure(s) over 1845 assertions
M4NoYamlEscape
self-test FAIL: xml-tag-dq-escape: exit 1: got 0
3 failure(s) over 1845 assertions
M5Whitespace
self-test FAIL: no_xml_tag['x'/'Map a -> b, x => y, a < b and c > d.']: PASS: got 'FAIL'
1 failure(s) over 1845 assertions
M6AnyBracket
self-test FAIL: xml-tag-control: exit 0: got 1
self-test FAIL: no_xml_tag['x'/'Map a -> b, x => y, a < b and c > d.']: PASS: got 'FAIL'
self-test FAIL: no_xml_tag['x'/'Keep <= 600 or <500 lines; cat <<EOF; 1<2>0; <> op.']: PASS: got 'FAIL'
7 failure(s) over 1845 assertions
M7NoSpecialMarkup
self-test FAIL: no_xml_tag['x'/'Use <!-- c --> here.']: FAIL: got 'PASS'
1 failure(s) over 1845 assertions
M8NoCdata
(no failure lines)
0 failure(s) over 1845 assertions
M9NoPi
(no failure lines)
0 failure(s) over 1845 assertions
```

## Commands, environment, and evidence

- Initial canonical-layout clone: `git clone -q --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/kotoba-r47/w2/W2XmlMutants/kotoba-shokunin` followed by `git -C <clone> checkout -q --detach 7ad7fadfc09354b74fb66605dfb0c1182c115a2f`; successful, no stdout/stderr. Nested canonical-layout clones were created from that isolated reference clone. Sibling entries and `.ufo` were symlinked by the assigned recipe; no symlink target was written.
- Nine nested `git clone` and detached-checkout commands, plus layout setup: **all exit 0**; exact argv/cwd/output appear in `setup`/`base_layout` in the artifact.
- `python3 --version`: **exit 0**, `Python 3.14.8`. No tool install/update was needed or performed.
- For each of nine clones, three phases ran `sha256sum verifiers/verify_skill_checklist.py` and `git rev-parse HEAD`: **all exit 0**.
- Mutations and restorations were committed **only in isolated scratch clones**, pathspec-limited to the verifier, using `git -c user.name=kotoba-shokunin -c user.email=kotoba@shokunin.local -c commit.gpgsign=false -c core.hooksPath=/dev/null commit -m <message> -- verifiers/verify_skill_checklist.py`: **all 18 commits exit 0**.
- All **27** `--self-test` invocations and their exit codes are recorded in the matrix/evidence. No timeout, exception, or missing output was treated as a kill.
- The supplemental command was `python3 -B -c <targeted_oracle.code> <JSON-encoded targeted_oracle.cases>`; its **exact executable argv** and full output are recorded as `phases.<phase>.<mutant>.targeted`. It loads the same verifier with `runpy.run_path`, calls `check_no_xml_tag` on eight fixed name/description pairs, prints every result, and exits 1 on any mismatch. All nine pristine runs exited **0**, all nine mutated runs **1**, and all nine restored runs **0**. It is deliberately reported separately from the committed self-test.

Evidence artifact (repo-relative): `.ufo/waves/round-47/falsify/W2XmlMutants.evidence.json` (181412 bytes, SHA-256 `da14bb9ba8a3ebebe577ef6c3ef6774755ba875ac354926986b5aaae69532062`). It contains exact before/after snippets, source locations, commands, raw outputs, Git commit IDs, hashes, and restoration results; no binaries or strings dumps.

## Restoration evidence

**H0**, the full verifier SHA-256 on all nine pristine and all nine restored copies:

```text
4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a
```

Every mutant hash differs from H0; every restored file returned exactly to H0. The same `--self-test` then returned exit 0 / `0 failure(s) over 1845 assertions` on each restored copy, and all supplemental controls returned to their pristine outcomes.

| Mutant | Mutated verifier SHA-256 | Before → mutated → restored |
|---|---|---|
| M1Backticks | `9410524d63019b68d4f5fbf920233c7c2b22d2693d64623ffcb3179e2249cc36` | H0 → mutant → H0 |
| M2Description | `8d8c13967a2f3e3c2d90b39c462f9c820becc3af0d413cc2fc16aee4787f3e9b` | H0 → mutant → H0 |
| M3Lowercase | `2b8d8746ba778ae6f71b71d46fba925a3de8273ea8dfecf8168aed51036e0daa` | H0 → mutant → H0 |
| M4NoYamlEscape | `f7893a0817f778fc3319d5881f273d007e4baa34095506a987fac4d655030fa6` | H0 → mutant → H0 |
| M5Whitespace | `01fd4ddfb72c16154baf20c1463b469d7e4db37ef216ceaed1df694b6a3b3a35` | H0 → mutant → H0 |
| M6AnyBracket | `d9b7909305ca407d6423541de5ddeeeaddb5e37ec40db511a08d692085f71369` | H0 → mutant → H0 |
| M7NoSpecialMarkup | `82721fa1d5cd6c82384ce9277aeb5655512698c23afcadd0aa1084b17101e35b` | H0 → mutant → H0 |
| M8NoCdata | `8a62d8880352ed4a2ceed52f025eedb73340dcca690547b4ab841b7d44bb8242` | H0 → mutant → H0 |
| M9NoPi | `6cd7994cb254de9a92cc2f26143f0b4d63216a8c821fca233125b2c78ec4853a` | H0 → mutant → H0 |

Scratch root: `/fast/scratch/kotoba-r47/w2/W2XmlMutants/<mutant>/kotoba-shokunin` (one clone per table row).

| Mutant | Mutation commit | Exact-byte restoration commit |
|---|---|---|
| M1Backticks | `75195b67c80ab7b7a7926dd25c5d64b35d914ab9` | `bf41ab013c8c7569dd55a62f701a89948fda6b2d` |
| M2Description | `7cf5d1e73c20a9437e6d9dd5ae5ed72c99caf2c7` | `d7dac74986966fac01c999e09836436a47718023` |
| M3Lowercase | `5944ffc226309d6da6479d4cf423e7278e3c0033` | `8788afc960e334c4d0414288d07c51cc670b148e` |
| M4NoYamlEscape | `49858784c2fe79161a8dd720df321857cfb8f1be` | `eddef5b2611012d33409c5ffd8f9419ae36dc54e` |
| M5Whitespace | `0fda24d745d3260ceda3a239a88a1ee7f52b1a38` | `6f487407e9386014e5f3a79ba9b267ec92e6860e` |
| M6AnyBracket | `ace7b0561887955d678e1189874ad40b8281fe4b` | `db99ce9e8a8626e050674362c1b33474b34a2eb5` |
| M7NoSpecialMarkup | `3625e1c80e6fade00be31bcdbf11b62eadf1c302` | `44c5d3d99b632030072b54c9a6b25d56ae4a640a` |
| M8NoCdata | `1adc5d8e2312ff928fe9698a528085d9267d6edd` | `ba589d7507b1d00c4e867af77f774eb9fae13dd1` |
| M9NoPi | `fc9e23d31b3216e3d8b2f1c3ac1cc06de5fab3bd` | `63497b44673033de3bec9e8a1d35ad55ea788d2b` |

## Reproduction of surviving mutants

This is a replay recipe, **not an additional verification claimed to have run**. It checks out only the named isolated scratch clone, runs the exact recorded self-test and targeted argv, and returns the clone to its recorded restored commit even if a detector fails. Set `E` to the evidence artifact's absolute path. Use `M9NoPi` instead of `M8NoCdata` to reproduce the PI survivor. Expected from the exercised records: `detector` exit 0; `targeted` exit 1 with only the selected CDATA or PI case flipping to PASS.

```sh
E=/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-47/falsify/W2XmlMutants.evidence.json
python3 -B - "$E" M8NoCdata <<'PY'
import json, subprocess, sys
from pathlib import Path
e = json.loads(Path(sys.argv[1]).read_text())
m = sys.argv[2]  # choose M8NoCdata or M9NoPi
mut = e["phases"]["mutated"][m]
rest = e["phases"]["restored"][m]
repo = mut["detector"]["cwd"]  # always isolated scratch; never production
subprocess.run(["git", "checkout", "--detach", mut["head"]["stdout"].strip()], cwd=repo, check=True)
try:
    for kind in ("detector", "targeted"):
        p = subprocess.run(mut[kind]["argv"], cwd=repo, text=True, capture_output=True)
        print(kind, "exit", p.returncode, p.stdout, p.stderr, sep="\n")
finally:
    subprocess.run(["git", "checkout", "--detach", rest["head"]["stdout"].strip()], cwd=repo, check=True)
PY
```

For a fresh clone instead of the retained scratch histories, `mutations.<id>` in the artifact specifies the exact single source replacement to apply to `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`; the mutated hash above identifies the resulting bytes.

## Not checked

- C1 substrate freshness, `verify_surfaces.py`, `check_substrate_pins.py`, omp/opencode binaries or wrappers, and live model/runtime sessions were not exercised.
- C3 corpus integrity, independent corpus verification, fault harness, governance errata, new source rows, and frontier/ledger claims were not re-audited in this leaf assignment.
- No full live checklist run, external YAML parser, Anthropic packager, or browser/client behavior was tested. The supplemental battery calls the checker on supplied parsed-field-shaped dictionaries; it does not claim YAML-parser or client equivalence.
- No combined comment+CDATA+PI deletion was counted as a separate mutant: independent arm deletions were used so comment coverage could not hide the two survivors. No production fixes, test additions, shipping, admission, or closure judgments were performed.
