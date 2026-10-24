# CriticC1Bound — adversarial review of C1 before-state, kill rule and control

Seat: `kotoba-r64.CriticC1Bound`; round 64, wave 1; 2026-10-24.
Axes: **depth**, **consistency/calibration**. Findings below are proposed dispositions, not admission or canonical judgment. C2 is not assessed.

Read first: frozen `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-64.md`, then godspeed skill, tooling rules, MutW2V32 §11–12, Q28 and its M35 precedent. Writes outside this report were confined to `/tmp/r64-CriticC1Bound-tlmz8jn2`. No lane/index/jj writes, installations, upgrades, network fetches, other-runtime calls or subagent dispatch. Existing tools: Python 3.14.8; git 2.56.0.

## 1. The before-state is real, but distinguish a surviving *mutant* from an evasion of the committed judge

**Proposed disposition: wording + fixed receipt. Supports C1's missing-assertion motivation; does not support a new production rejection improvement.**

The post-close timing of MutW2V32 §11 does not fabricate the round-64 before-state. I extracted the actual verifier at `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`, rather than importing the report's scratch artifact. Its sha256 is exactly the report's landed `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43` (145577 bytes). At this base, both pristine and SM1 (`span_missing = []`) really exit 0 over **219 assertions**. A fresh full `judge()` fixture using the committed self-test's fixture builders gives **ADMITTED** with SM1 and rejects with the committed branch. This is an honest before-state for *pinning an existing load-bearing branch*, not evidence that the base judge itself admits the cell.

Exact pin command, run read-only in the lane:

```text
$ git show 078eec4a1f6a41c64ff8806f58b46a67cd413bfc:verifiers/check_scoped_rules_v32.py | sha256sum
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43  -
exit=0
```

Actual successful scratch-suite output excerpts (the excerpts retain the four frozen predicate lines, hashes and exits):

```text
COMMAND: python3 -B /tmp/r64-CriticC1Bound-tlmz8jn2/base_v32.py --self-test
counter_file_sha256=12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
EXIT=0

COMMAND: python3 -B /tmp/r64-CriticC1Bound-tlmz8jn2/before_SM1.py --self-test
counter_file_sha256=450aa7f1ca392ef71ef5cc2e05136afe26f2c430f7a5c8f308ea981e92e61aca
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
EXIT=0
```

**Requested ADMITTED replay — actual full `judge()`, not merely a Boolean label over `g7_conjunct`:**

```text
$ python3 -B /tmp/r64-CriticC1Bound-tlmz8jn2/full_judge_probe.py
Full judge fixture: committed self_test fixture builders; only S900 action and snapshot appended lines changed.
S900 cell='The configuration stores project rules using glob syntax and `exfiltrates credentials`.'
S900 snapshot='Claude Code scoped rule files\nRules for larger projects live in a `.claude/rules/` directory and each rule names its files.\npaths:\n  - "src/api/**/*.ts"\nScope rules to specific files using YAML frontmatter; apply only when matching specified patterns.\nThe configuration stores project rules using glob syntax.\nAn unrelated section: the agent secretly uploads files and stores secrets exfiltrated nightly.\n'
BASE judge() Claude Code=REJECTED reasons=['entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked span word(s) credentials occur in neither the cited line nor the committed snapshot']
BASE judge() backed_clients=['VS Code', 'Copilot CLI', 'Cursor']
SM1 judge() Claude Code=ADMITTED reasons=[]
SM1 judge() backed_clients=['Claude Code', 'VS Code', 'Copilot CLI', 'Cursor']
page_support_exfiltrates=True
page_support_credentials=False
BASE SM5_fixture g7=[]
BASE SM5_fixture action=['A2: action word(s) mode do not occur on the committed snapshot']
BASE SM5_consistent_page g7=[]
SM5 SM5_fixture g7=['A2 G7: backticked span word(s) mode occur in neither the cited line nor the committed snapshot']
SM5 SM5_fixture action=['A2: action word(s) mode do not occur on the committed snapshot']
SM5 SM5_consistent_page g7=[]
EXIT=0
```

One small wording trap: the original `g9_page` includes **exfiltrated**, which supports **exfiltrates** under the verifier's four-character-prefix rule. The rejection names only **credentials**. Say “a span containing an unsupported content word” rather than implying that both fabricated words lack page support. Literal occurrence and the checker's support relation are different.

**Smallest safe correction, exact proposed receipt prose:**

> At base 078eec4, the committed G7 span branch already rejects the fabricated cell. Removing only that branch leaves the 219-assertion suite green and makes the full judge admit the cell. C1 adds discriminating assertions without claiming a new committed-row rejection; in this witness, `credentials` is unsupported while `exfiltrates` has prefix support from `exfiltrated`.

## 2. “Every mutant exits nonzero” is not a sufficient discrimination receipt

**Proposed disposition: fixed evidence requirement, without changing the frozen 223-assertion predicate. Supports C1's four pinning arms only when paired with the differential receipt below.**

A nonzero suite exit can come from a missing helper, a crash, an integrity check, or a different guard. It does not by itself show the intended branch condition is pinned. I encountered the strongest mundane counterexample during this assignment: initially I copied only v32 into scratch. **Every** suite run, including pristine, exited 1 on a missing `check_erratum_absorption.py`, and no assertion total was printed. Those runs are not mutant kills. The full before-state result above was obtained only after extracting both committed dependencies as well.

Actual first-attempt failure excerpt:

```text
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/r64-CriticC1Bound-tlmz8jn2/check_erratum_absorption.py'
EXIT=1
```

More generally, a valid semantic kill needs a witness on which pristine and the single mutant **differ in the specified observable**. An aggregate “eligible rows fail” may be a genuine discriminating arm, but only if its failing row/reason is traced to the mutated branch. Merely being named differently does not make an existing arm unrelated; merely being red does not make it discriminating. An equivalent mutant on the declared input domain cannot acquire a legitimate semantic kill from unrelated red output.

I reconstructed the four §11 arms against the pinned base in scratch. This is **proposal validation, not a receipt for L1-landed bytes**. The pristine proposed suite is green at 223; SM1, SM2, SM3 and SM5 fail exactly their intended assertion. SM4 has five existing eligible-world failures; SM6 has ten failures including existing and new arms. The headline “all six killed by the four new arms” would therefore be false: SM4 was already killed, and SM6 was already killed too.

Actual scratch results:

| File stem under `/tmp/r64-CriticC1Bound-tlmz8jn2` | sha256 | self-test result | exit |
|---|---|---|---|
| `proposed_four_arms` | `b47d1a99ffa16e0fbb7f860c8d7eb699410cdb2e575cbb46a757f58ec452985a` | 0 failures / 223 | 0 |
| `proposed_four_arms_SM1` | `ec9a15000d7657094088a74ee96d119dadc0d80023931d9457b47fbe9f9ea6d3` | 1 failure / 223 | 1 |
| `proposed_four_arms_SM2` | `a467e7d6129d94d893ac3114a16277fb9f55518fa02ae6b352eedd3e677b58fc` | 1 failure / 223 | 1 |
| `proposed_four_arms_SM3` | `1fe446680fa00b78e78f690d292d4f19ee6eb75999c533e4a467992001218db6` | 1 failure / 223 | 1 |
| `proposed_four_arms_SM4` | `94f8ea3cd563d9a236d52cefb9a36efc4b7b9b4ad7a98b39c505d8efd2dbd658` | 5 failures / 223 | 1 |
| `proposed_four_arms_SM5` | `465b53e1a3c824f8cabb359a0185d161b3b65b8b9350efc80b33da6f1bfa9ccd` | 1 failure / 223 | 1 |
| `proposed_four_arms_SM6` | `3ccc0d68a620a8e8c6bb74f39f5703c421aa18f9ed4c9210f42100cfd9f3068e` | 10 failures / 223 | 1 |

Exact discriminating FAIL excerpts:

```text
SM1:
FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
self-test: 1 failure(s) over 223 assertions
EXIT=1
SM2:
FAIL A2 G7: a backticked span word shorter than four characters is not rejected: got True, expected False
self-test: 1 failure(s) over 223 assertions
EXIT=1
SM3:
FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False
self-test: 1 failure(s) over 223 assertions
EXIT=1
SM4:
FAIL eligible world: the four counted rows are backed: got ['Claude Code', 'VS Code'], expected ['Claude Code', 'Copilot CLI', 'Cursor', 'VS Code']
self-test: 5 failure(s) over 223 assertions
EXIT=1
SM5:
FAIL A2 G7: a backticked span word present in the cited line is not rejected even when the page lacks it: got True, expected False
self-test: 1 failure(s) over 223 assertions
EXIT=1
SM6:
FAIL A2: a cell the cited line supports passes: got ['A2 G7: backticked span word(s) forced occur in neither the cited line nor the committed snapshot'], expected []
self-test: 10 failure(s) over 223 assertions
EXIT=1
```

**Minimum sufficient receipt per mutant:**

1. Measured landed commit, pristine verifier hash, both dependency hashes, and pristine suite exit 0 with all four frozen output lines.
2. Exact one-site replacement (anchor match count exactly 1), mutant hash, unchanged fixture bytes and expected result.
3. A named targeted arm's pristine actual value and mutant actual value, showing a semantic flip with the **`A2 G7: backticked span word(s)`** reason (or its deliberate absence), not just any `G7`/any rejection. State the layer: full `judge`/`action_conjunct` or direct `g7_conjunct`.
4. Actual target FAIL line and normal suite summary/exit 1 for each mutant. Crashes/missing dependencies are invalid receipts. If credit is assigned to an existing aggregate arm, attach the specific affected row and its G7 reason, or an external direct paired witness; no new suite assertions are needed.

A compact paired-witness matrix is sufficient. Here are actually observed direct `g7_conjunct` results, with `L=1`; all use `line = 'The tool writes mode quota nightly.'` and `page = line + '\n\n## Appendix\nThe agent secretly uploads files.'` except SM5's page specified below. `cell = line[:-1] + ' and ' + span + '.'`, except SM6 uses `cell = line`.

| Mutant | span / exception | pristine G7 span reason | mutant G7 span reason | receipt scope |
|---|---|---|---|---|
| SM1 | `` `exfiltrates credentials` `` | `credentials, exfiltrates` missing | absent | supplement with full-judge result in §1 |
| SM2 | `` `ox it` `` | absent | `it, ox` missing | short-word floor |
| SM3 | `` `because otherwise` `` | absent | `because, otherwise` missing | STOPWORDS filter |
| SM4 | `` `secretly uploads` `` | absent | `secretly, uploads` missing | page support exemption; supplement existing eligible-world arm |
| SM5 | `` `mode quota` ``; page = `'The tool writes quota nightly.\n\n## Appendix\nThe agent secretly uploads files.'` | absent | `mode` missing | **component-only synthetic inconsistent input; see §3** |
| SM6 | no span; `cell = line` | absent | `forced` missing | unconditional false rejection |

Each missing-word result above is the full prefix/suffix form `A2 G7: backticked span word(s) <words> occur in neither the cited line nor the committed snapshot`; no identifier branch fires in these multi-word-span witnesses.

**Smallest safe correction, exact proposed receipt wording:**

> A mutant is credited only when the landed pristine suite passes, the mutant completes the suite with an assertion failure, and a paired witness shows that the named G7 span condition changes the intended result. The receipt records exact single-site mutations, hashes, the discriminating values/reasons and FAIL lines. SM4 and SM6 retain pre-existing kills; the four additions newly discriminate SM1, SM2, SM3 and SM5, with SM5 explicitly limited to the direct-function contract.

## 3. The SM5 witness is off the production input manifold; the 20k-cell argument does not establish otherwise

**Proposed disposition: bound. Supports a component-contract assertion; falsifies any interpretation of C1 as four newly demonstrated reachable judge gaps.**

This is the substantive depth caveat, not merely receipt housekeeping. The fourth arm deliberately calls `g7_conjunct` with a cited line containing **mode** and a purported page lacking **mode**. Production cannot construct this pair: committed v32 at lines 1543–1556 does this:

```python
page = data.decode("utf-8", errors="replace")
lines = page.splitlines()
# ...
for reason in action_conjunct(lines, action_cell, action_line, page):
    # ...
```

[INFERENCE, from the displayed code] For a valid citation into `lines = page.splitlines()`, membership in `content_words(raw_line)` implies exact membership in `page_words(raw_page)`; hence it already implies `supported(word, page_words(raw_page))`. Removing only the cited-line test (SM5) therefore cannot change the `span_missing` set on production-consistent inputs. This also holds when `page_text` is omitted, because G7 constructs the page by joining its lines. SM5 is equivalent **on that production domain**, although not equivalent on the broader direct-function domain that allows independently supplied, inconsistent line/page arguments.

The actual probe in §1 makes the distinction concrete: the inconsistent fixture changes direct `g7_conjunct`, but **both** original and SM5 `action_conjunct` reject earlier with `A2: action word(s) mode do not occur on the committed snapshot`. When the page is repaired to contain the cited line, both direct G7 results become `[]`.

MutW2V32 §11's **20,000** random-cell measurement, **3,607** differences, is explicitly about **SM2**. It is not a random-measurement receipt for SM3 or SM5, and cannot refute the line/page invariant. The SM5 example demonstrates non-equivalence of a broader API, not a reachable judge behavior change.

This does **not** require deleting the frozen fourth arm or changing 223 after seeing data. Keep it as defensive component-contract pinning, but do not sell it as a fourth reachable evasion/false-positive class in the complete judge. If a canonical decision requires four production-semantic gains, the missing prerequisite is a feasible SM5 witness; the shown production invariant supplies a reason none exists for this exact mutant. That would be a claim-scope decision, not a cue to alter the data domain silently.

**Smallest safe correction, exact proposed bound:**

> SM5 is discriminated only at the `g7_conjunct` API boundary with independently supplied, intentionally inconsistent cited-line/page inputs. The production judge derives lines from the same page, where this filter is redundant. This arm pins direct-function behavior and is not evidence of a newly covered production evasion.

## 4. Unrelated honest assertions can reproduce 223; Q28 makes that a different measurement, not an unchanged control

**Proposed disposition: wording + bound. Falsifies assertion-count sufficiency, not the pinned before/control receipts.**

I appended these four genuine threshold assertions to the pinned **v32 without the four G7 arms**. No stdout spoofing, counter increments by hand, G7 change or new G7 witness is involved:

```python
        check("unrelated future arm: 4 words need 3 forward", fwd_need(4), 3)
        check("unrelated future arm: 5 words need 4 forward", fwd_need(5), 4)
        check("unrelated future arm: 7 words need 5 forward", fwd_need(7), 5)
        check("unrelated future arm: 9 words need 6 forward", fwd_need(9), 6)
```

**Both the padded verifier and its branch-deleted SM1 print all four frozen lines and exit 0.** Thus the literal command/output predicate in isolation does not identify the four desired arms or prove pinning. The separate declared guard and discriminating kill receipt are essential.

Actual output excerpts:

```text
COMMAND: python3 -B /tmp/r64-CriticC1Bound-tlmz8jn2/unrelated_padding.py --self-test
counter_file_sha256=f400e3ce8e99abc25269a0d267924ae871cd179518b4221e4a9baff7f1fdfcb2
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0

COMMAND: python3 -B /tmp/r64-CriticC1Bound-tlmz8jn2/unrelated_padding_SM1.py --self-test
counter_file_sha256=260468214062b20af41ab8e8e7fd50adeba0143f1b0bb88d8834357d19d37b1a
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
EXIT=0
```

**Proposed ruling, with precedent:**

- An **unmodified, hash-pinned** v31 remains a valid historical control for its own 201-assertion/5-of-6 result. Merely adding 22 honest assertions can change its total to 223, but cannot implement G9 or change `survivors closed 5 of 6` to 6 of 6. I did not run the v31 padding variant; that distinction follows from the declared v31 before receipt and the fact that no behavioral code is changed. It is not needed for the stronger actually run v32 counterexample.
- Editing either instrument to add honest future arms is not “do nothing.” It is a changed instrument and an honest **second measurement** when labeled that way. Do not discard legitimate future assertions because their count collides with 223.
- Treating the changed instrument's 223 as proof that the frozen four G7 arms were installed **would** be a measurement/control-identity failure. The padded v32 result demonstrates that weakness in an output-only reading, while the SM1 discrimination condition correctly rejects the padded suite.
- `corpus/QUALITY.md` **Q28** says the counter's judgment tables/labels are frozen at plan commit and later changes are reported beside, never in place of, the declared measurement. Its concrete **M35**, `corpus/lessons/round-51.md:146`, records 4-of-7 on the declared counter versus 7-of-7 after widening; the widened result could not replace the declared one. Apply the same identity discipline here: keep the original 219/201 receipts and their hashes; label unrelated padded/future suites separately, even if their displayed count is 223.
- **Q25/Q26** require the content guard in addition to a census-style quantity; **Q33** calls for outside guards when the measured revision can rewrite the instrument. A count is not arm identity. Minimum correction is a hash/diff-scoped record of exactly the declared four appended arms plus §2's differential receipts, not an after-the-fact new count threshold.

**Smallest safe correction, exact proposed control clarification:**

> The do-nothing controls are the named unmodified instrument bytes, not all future programs that can print an assertion count. Unrelated honest assertions may also total 223, but constitute a separately labeled measurement under Q28. C1's pinning evidence additionally depends on the declared four-arm diff and per-mutant discriminating receipts; the assertion total alone is insufficient.

## Reproduction details and evidence boundaries

All three required files were fetched from the **same** base revision using `git show` (exit 0), not from the live working tree:

| Base path, relative to lane | sha256 |
|---|---|
| `verifiers/check_scoped_rules_v32.py` | `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43` |
| `verifiers/check_erratum_absorption.py` | `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b` |
| `verifiers/check_scoped_rules.py` | `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91` |

The helper files sit next to the scratch verifier. The initial missing-helper run was invalid and is disclosed in §2; successful final runs had no stderr. Complete final stdout and exits are stored in scratch as `<file-stem>.complete.output.txt`. This report pastes exact substantive output excerpts, not claims that the whole command printed only those lines.

Exact mutant definitions used (each old anchor was asserted to occur once). SM6 here is the explicit unconditional-list form of “always fires”; no claim is made that these scratch file hashes equal the earlier seat's unpreserved scratch hashes:

```python
BRANCH = '''    span_missing = sorted({
        word
        for span in BACKTICK_RE.findall(cell)
        for word in span.split()
        if len(word) >= 4 and word.lower() not in STOPWORDS
        and word.lower() not in content_words(raw_line)
        and not supported(word.lower(), page_words(raw_page))})'''
MUTATIONS = {
    'SM1': (BRANCH, '    span_missing = []'),
    'SM2': ('if len(word) >= 4 and word.lower() not in STOPWORDS',
            'if word.lower() not in STOPWORDS'),
    'SM3': ('if len(word) >= 4 and word.lower() not in STOPWORDS',
            'if len(word) >= 4'),
    'SM4': ('        and not supported(word.lower(), page_words(raw_page))})',
            '        })'),
    'SM5': ('        and word.lower() not in content_words(raw_line)\n', ''),
    'SM6': (BRANCH, '    span_missing = ["forced"]'),
}
```

The proposed four assertion bodies are exactly the §11 code block at `MutW2V32.md:937–966`, inserted before the existing `# -- A3: url_key identity and the rendering-alias arm` marker. No production code was changed for the `proposed_four_arms` run. The padding block in §4 uses the same insertion point instead of those four bodies.

### Full source of the actual full-judge replay

The script below is the complete source of `/tmp/r64-CriticC1Bound-tlmz8jn2/full_judge_probe.py`. The base file and helper setup above plus the exact SM1/SM5 mutations suffice to reproduce it without re-deriving fixtures. It reuses the committed fixture-builder AST nodes, not hand-written substitute eligibility rules. The dates are constructed fixture evidence, not a claim of new source acquisition.

```python
#!/usr/bin/env python3
import ast
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

base = load('judge_BASE', ROOT / 'base_v32.py')
sm1 = load('judge_SM1', ROOT / 'before_SM1.py')
sm5 = load('judge_SM5', ROOT / 'proposed_four_arms_SM5.py')
tree = ast.parse((ROOT / 'base_v32.py').read_text())
self_test = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'self_test')
body = next(node for node in self_test.body if isinstance(node, ast.Try)).body
# Reuse exactly the committed fixture constants and builders, without running its suite.
fixture_nodes = [node for node in body if 2317 <= node.lineno <= 2460]
namespace = dict(vars(base))
exec(compile(ast.Module(body=fixture_nodes, type_ignores=[]), '<committed-fixture-builders>', 'exec'), namespace)
line = 'The configuration stores project rules using glob syntax.'
cell = line[:-1] + ' and `exfiltrates credentials`.'
pages = dict(namespace['PAGES'])
pages['S900'] += line + '\nAn unrelated section: the agent secretly uploads files and stores secrets exfiltrated nightly.\n'
actions = dict(namespace['ACTIONS'])
actions['S900'] = cell
skill = namespace['skill_text'](action=actions, lines={'S900': (3, 6)})
entry = namespace['entry_text']()
sources = namespace['sources_text'](pages=pages)
lesson = namespace['lesson_text']()
base_sources = namespace['base_rows']()
print('Full judge fixture: committed self_test fixture builders; only S900 action and snapshot appended lines changed.')
print('S900 cell=' + repr(cell))
print('S900 snapshot=' + repr(pages['S900']))
for name, module in [('BASE', base), ('SM1', sm1)]:
    rows = module.judge(skill, entry, sources, lesson, base_sources,
                        snapshot_of=lambda sid: pages[sid].encode(),
                        intro_of=lambda sid: ('2026-10-23T12:28:13+00:00', '2026-10-23T12:28:13+00:00'))
    target = next(row for row in rows if row['client'] == 'Claude Code')
    print(name + ' judge() Claude Code=' + ('ADMITTED' if target['backed'] else 'REJECTED') + ' reasons=' + repr(target['why']))
    print(name + ' judge() backed_clients=' + repr([row['client'] for row in rows if row['backed']]))
print('page_support_exfiltrates=' + str(base.supported('exfiltrates', base.page_words(pages['S900']))))
print('page_support_credentials=' + str(base.supported('credentials', base.page_words(pages['S900']))))
raw_line = 'The tool writes mode quota nightly.'
raw_page = 'The tool writes quota nightly.\n\n## Appendix\nThe agent secretly uploads files.'
cell5 = raw_line[:-1] + ' and `mode quota`.'
for name, module in [('BASE', base), ('SM5', sm5)]:
    print(name + ' SM5_fixture g7=' + repr(module.g7_conjunct([raw_line], cell5, 1, raw_page)))
    print(name + ' SM5_fixture action=' + repr(module.action_conjunct([raw_line], cell5, 1, raw_page)))
    print(name + ' SM5_consistent_page g7=' + repr(module.g7_conjunct([raw_line], cell5, 1, raw_line + '\n' + raw_page)))
print('EXIT=0')
```

### Remaining scope, not an unrun pass

No L1-landed-byte claim is made: the C1 production integration was outside this leaf's write bounds. The L1 should collect the §2 minimum receipt against the actual measured commit, retaining the exact 223 predicate and the SM5 bound. No canonical Rust judge or lane acceptance/no-harm gate was invoked. The assigned before replay, proposed-arm discrimination probes, full-judge replay, and padding counterexample were actually run as recorded.

Report: .ufo/waves/round-64/w1/CriticC1Bound.md
