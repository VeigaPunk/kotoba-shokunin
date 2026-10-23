# FalsifyE2eClass — scoped class/provenance review

Audited revision: `e6da78bbe420722dd18a13182a7c4b64ce02f005`. Axis under attack: **depth**; related risk: consistency/calibration. This is a critic's evidence report, not an admission, axis verdict, integration, or canonical judgment.

## Result and counterexample

**The named E2e instances are not a smuggled class.** They belong to the explicitly amended **guarded A1** class, not merely the original lexical key-form/path-value predicate. Rejecting them as positive evidence of an active scope-key binding follows the pinned E2e amendment. It does **not** follow from the isolated vendor statement “Accepts a YAML list or a comma-separated string” alone.

**The stronger counterexample is a surviving member of the original class:**

```text
Do not set paths: src/legacy/**/*.ts in a rule that should load for every file.
```

This is the original MutA1 V10 literal, not a newly invented semantic demand (`.ufo/waves/round-61/wave/MutA1.md:368-380`). The probe below observed `key_site=True`, `path_site=True`, and `a1_conjunct + scope_conjunct == []` under both the frozen counter and v3.1. The amended A1's required rejection therefore **fails for this original class member in the successor**, even though the successor's own finite-fixture self-test exits successfully. The original G6 `//` and `<!--` commented-key forms likewise remain accepted in that probe.

The measured survivor-closure headline is not itself falsified: the successor rejects the particular matrix literals, including `Do not use paths: ...`. The problem is treating that finite closure as the whole E2e guarded-form repair.

## Exact class evidence

All line references below are relative to the lane at the audited revision; a sandbox clone preserved those committed bytes while the live lane continued changing.

- `plans/round-61.md:27-29` originally required canonical per-client membership and a path-like value. That wording alone did not exclude comments, negation, or equals forms.
- **The decisive amendment is `plans/round-61.md:196-205`:**

  ```text
  201: ... A1's letter is amended to the GUARDED form
  202: (MutA1 §5 validated code): one key per cell; exact-case membership in the per-client set;
  203: path-like value bound on the cited line OR its immediate block (quote-aware lookahead —
  204: this is what keeps the real S103:198/:199 row passing); no commented keys; no negation
  205: within 60 chars; colon form; no equals-form keys; no example/unchecked-cell keys. ...
  ```

- Original class examples and mechanisms are already committed in `.ufo/waves/round-61/wave/MutA1.md`: commented `# paths:` at `:356-366`; negated `Do not set paths:` at `:368-382`; equals form at `:384-398`. The guard implementation uses a colon at `:503`, the preceding-window slice at `:506`, and `not|never|avoid|instead|n't` at `:507`. G6 explicitly includes `#`, `//`, and `<!--` at `:498` and `:538`; G7/G8 are restated at `:539-540`.
- `plans/round-62.md:40-45` identifies the measured class as E2e/**A1 guarded key form** and names `a1_conjunct + scope_conjunct / path_site`. Its pre-data addenda explicitly name the absent colon/comment clauses at `:245-247` and the negated-key observation at `:285-292`.
- `verifiers/check_erratum_absorption.py:147-156` passes a canonical Claude `paths` key and the synthetic line to those actual arm functions. The exact literals are at `:200-205`. Thus neither instance relies on a wrong client/key or an invalid glob. `# paths=...` combines the already-pinned G6 and G8 subconditions; it is in-class but cannot by itself attribute rejection to either subcondition independently.

## What the frozen functions actually recognize

- `verifiers/check_scoped_rules.py:397` uses `KEY_SUFFIX_RE = re.compile(r"""["'`]?[ \t]*[:=]""")`, explicitly allowing either delimiter.
- `:944-959` (`key_site`) scans identifier-boundary occurrences of the key and checks suffix/value, not comment status or assertion direction. Its own docstring at `:947-949` says `K:` / `K=`.
- `:1043-1050` (`path_value`) requires `*`, `/`, and the token character grammar. Both matrix inputs retain the same genuine `src/legacy/**/*.ts` value, so this conjunct is satisfied rather than bypassed with markdown bold.
- `:1053-1064` (`path_site`) repeats the occurrence/suffix/value procedure with `path_value`, without a comment or negation guard. `:1103-1112` (`scope_conjunct`) rejects only when that path site is absent; `:1089-1100` (`a1_conjunct`) performs canonical membership.

Consequently, the frozen accepts are expected **evidence of non-absorption**, not evidence that rejecting the amended class would overreach. The direct probe also preserves acceptance for a plain colon binding, S118's block-list shape, and a comma-separated string; its exact code/output is in the transcript appendix.

## S118 re-open and source boundary

Re-opened the vendor URL with the static reader during this review: <https://code.claude.com/docs/en/memory.md>. The rule-frontmatter reference still states the YAML-list/comma-string fact. This review does not assert literal equality of the live response with the stored snapshot; the snapshot fingerprint is separately measured below.

Exact committed snapshot evidence (`.ufo/waves/round-62/snapshots/S118.page`):

```text
194: Rules can be scoped to specific files using YAML frontmatter with the `paths` field. These conditional rules only apply when Claude is working with files matching the specified patterns.
198: paths:
199:   - "src/api/**/*.ts"
246: Configure a rule with YAML [frontmatter](https://code.claude.com/docs/en/glossary.md#frontmatter) between `---` markers at the top of the file. `paths` is the only field Claude Code reads from a rule; any other field is ignored without an error. Claude Code removes the frontmatter before loading the rule into context.
250: | `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
252: If the YAML between the markers doesn't parse, Claude Code ignores the frontmatter and loads the rule as if it had no `paths`. Run `claude --debug` to see the parse error.
```

`corpus/SOURCES.md:129` scopes S118 to vendor documentation of `paths` frontmatter matching syntax, explicitly **not a runtime test**. That is an appropriate source boundary. The list/string alternative concerns the **value of the actual `paths` YAML field**; it does not make a `# paths=...` comment an active field, make equals syntax a YAML mapping separator, or make a prose prescription naming `paths` an affirmative configuration binding. The explicit negative/comment policies and their context window derive from the pinned A1 amendment, not from an invented vendor prohibition.

Conversely, do not infer that Claude rejects an entire rule file merely because this evidence guard rejects a cited line: `S118.page:209` says rules without `paths` are unconditional, and `:252` gives the invalid-frontmatter fallback. Nor does S118's general syntax establish the counter's narrower `*`/`/` requirement for every possible vendor-valid pattern. This review tested the documented list/string shapes with path-like globs; it did not execute Claude Code.

## Successor defect and boundary mismatch

The direct probe is the counterexample experiment; its process exit merely indicates successful probe execution, not satisfaction of the guarded A1 requirement.

- `verifiers/check_scoped_rules_v31.py:401` correctly changes the delimiter to colon-only.
- `:402-404` recognizes only `do not use`, `don't use`, `never use`, or `avoid`, not the original V10's **`Do not set`** or the original generic G7 token set. Hence the concrete V10 rejection fails.
- `:952-972` recognizes YAML `#` comments outside quoted scalars, but does not implement the original G6 leading `//`/`<!--` alternatives; the probe observes both accepted.
- `:975-979` searches the **entire** preceding line rather than `max(0, position-60):position`. The probe's `outside-pinned-60-char-window` witness has no negator in that pinned window but is rejected by v3.1. This is a specification-boundary counterexample, **not** a claim that the synthetic line is a vendor-valid positive fixture or that a production runtime regression has been demonstrated.
- `:2554-2586` measures only the named frozen survivor catalogue; `:2588-2598` disables the key-site guard only for the new `Do not use` instance. Those checks do not exercise original V10 or the G6 alternatives.

## Claims, ledger, and registry impact

- `corpus/knowledge/erratum-absorption-round62.md:14` correctly describes the matrix E2e accepts and unchanged admitting-stub direction. `:31` correctly disclaims universal guarantees. The broader wording “the E2c/E2e guards” at `:35` needs the residual boundary above if it is intended as class-wide closure; the declared bounds at `:37-41` currently omit it. `:43` must keep S118's role limited to form/source evidence, not the authority for the negation policy.
- `LOG.md:2548` records the matrix survivors; `:2550` and `SKILL.md:490` bound successor closure to **measured survivor instances**. The executed commands below reproduce those finite outputs, so this attack does not relabel their measured values as failures.
- `SKILL.md:486` keeps the frozen counter and successor distinct, and `:488-490` registers the new tools as gates. No identity replacement or new capability admission is needed to explain these E2e inputs.
- `SCORECARD.md:36` holds the depth score and names the matrix as arm-level, not whole-class semantic completeness. Its broader “No axis harmed” sentence is not established by the frozen-fixture self-tests alone; this seat supplies the concrete residuals rather than issuing an axis judgment.

**Impacted axes:** depth (the promised guarded-A1 decision boundary remains incompletely implemented); calibration/consistency if finite-fixture closure is promoted to full E2e absorption or source-derived runtime behavior. There is no demonstrated loss on the existing documented benign list/string examples: their outcomes are in the probe and the real-revision live counting runs below.

## Smallest safe correction

1. Preserve the frozen counter, original matrix pair/denominator, and honest finite receipts. Do not replace E2e with a bold-marker-only class merely to recover absorption credit.
2. In the **successor only**, implement the already-pinned preceding-window/negator rule from MutA1 `:506-507` and the already-pinned G6 leading comment forms, retaining quote-aware YAML comment handling. Add the literal original V10 and isolated comment/equals controls beside the existing fixtures, paired with the documented block-list and comma-string positives. This fixes a defect rather than renegotiating the class.
3. Until that change has its own measurement/hash, explicitly declare the original V10/G6 cases and the context-window mismatch as successor bounds. Keep S118's attribution as vendor form evidence, and class-rejection authority as the r61 E2e amendment. No claim of whole-class absorption or universal no-harm follows from the current finite green lines.

No product files, verifier files, corpus files, fleet files, sibling files, state files, or lane git/jj index were written by this seat. Sandbox-only git writes were used for the self-tests. Installs/updates: none. No canonical judge or another orchestration/model runtime was invoked.

## Exact command/output transcript

Commands were executed sequentially, with a per-command timeout and `PYTHONDONTWRITEBYTECODE=1`, `TMPDIR=/tmp`; no background work or subagent dispatch. Self-test programs were loaded from the pinned sandbox clone, and their fixture git writes were under `/tmp`. `STDERR:` below separates captured stderr from stdout; every process exit is recorded. The `-c` probe source is the literal argument in its displayed command. Hash outputs below are actual `sha256sum` command output, not a reconstructed pipeline.

```text
$ /usr/bin/git -C /tmp/FalsifyE2eClass-cl63f12n/lane rev-parse HEAD
e6da78bbe420722dd18a13182a7c4b64ce02f005
EXIT_CODE=0
```
```text
$ /usr/bin/git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD
e6da78bbe420722dd18a13182a7c4b64ce02f005
EXIT_CODE=0
```

```text
$ /usr/bin/git clone --quiet --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/FalsifyE2eClass-cl63f12n/lane
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_erratum_absorption.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules.py --self-test
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
self-test: 0 failure(s) over 189 assertions
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules_v31.py --self-test
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 0 failure(s) over 201 assertions
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_routed_repairs_v2.py --self-test
successor: dishonest rejected 6 of 6; honest passed 2 of 2; base 0 of 6; tip 6 of 6
STDERR:
G-a paired population control: 29 names/committed 29=6; 30 names/committed 29=5; 30 names/committed 30=6; frozen=6/6/5
label-only constants fail controls: constant 6 vs base 0; constant 0 vs H1 6; constant 0 vs H2 6
frozen counter before: D1 6 of 6; D2 6 of 6; D3 6 of 6; D4 6 of 6; D5 6 of 6; D6 6 of 6; H1 4 of 6; H2 tip 6 of 6
self-test base CLI output:
R-a count correction: missing
R-b landed-scope names: missing
R-c base-measure pointer: missing
R-d census-after body: missing
R-e byte-exact criterion + M91: missing
R-f controls-ancestry receipt: missing
routed repairs verified 0 of 6
self-test tip CLI output:
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
self-test CLI exits: base rev f3246d1493b60ea1c0d947a19c39f9e08e92f326 exit 1; tip rev 45a7ecfac9e203297f3146c45d63f5e79367470c exit 0; unreadable rev routed-repairs-v2-no-such-revision exit 2
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B -c 'import importlib.util
import sys
from pathlib import Path
sys.dont_write_bytecode = True
root = Path('"'"'/tmp/FalsifyE2eClass-cl63f12n/lane'"'"')
def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, root / '"'"'verifiers'"'"' / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module
frozen = load('"'"'e2e_frozen_probe'"'"', '"'"'check_scoped_rules.py'"'"')
successor = load('"'"'e2e_successor_probe'"'"', '"'"'check_scoped_rules_v31.py'"'"')
keys = {'"'"'Claude Code'"'"': frozenset({'"'"'paths'"'"'})}
cases = [
    ('"'"'e2e-negated-path-key'"'"', ['"'"'Do not use paths: src/legacy/**/*.ts'"'"']),
    ('"'"'e2e-commented-equals-key'"'"', ['"'"'# paths=src/legacy/**/*.ts'"'"']),
    ('"'"'comment-only'"'"', ['"'"'# paths: src/legacy/**/*.ts'"'"']),
    ('"'"'equals-only'"'"', ['"'"'paths=src/legacy/**/*.ts'"'"']),
    ('"'"'benign-inline-colon'"'"', ['"'"'paths: src/legacy/**/*.ts'"'"']),
    ('"'"'benign-S118-YAML-list'"'"', ['"'"'paths:'"'"', '"'"'  - "src/api/**/*.ts"'"'"']),
    ('"'"'benign-comma-string'"'"', ['"'"'paths: "src/api/**/*.ts, tests/**/*.ts"'"'"']),
    ('"'"'original-MutA1-V10'"'"', ['"'"'Do not set paths: src/legacy/**/*.ts in a rule that should load for every file.'"'"']),
    ('"'"'original-G6-slash-comment'"'"', ['"'"'// paths: src/legacy/**/*.ts'"'"']),
    ('"'"'original-G6-HTML-comment'"'"', ['"'"'<!-- paths: src/legacy/**/*.ts -->'"'"']),
    ('"'"'outside-pinned-60-char-window'"'"', ['"'"'Do not use '"'"' + '"'"'x'"'"' * 61 + '"'"' paths: src/legacy/**/*.ts'"'"']),
]
for ident, lines in cases:
    print(ident + '"'"': '"'"' + repr(lines))
    for label, module in [('"'"'frozen'"'"', frozen), ('"'"'v31'"'"', successor)]:
        reasons = module.a1_conjunct('"'"'Claude Code'"'"', '"'"'paths'"'"', keys)
        reasons += module.scope_conjunct(lines, '"'"'paths'"'"', 1)
        print('"'"'  %s key_site=%r path_site=%r path_value=%r reasons=%r'"'"' % (
            label, module.key_site(lines, 1, '"'"'paths'"'"'),
            module.path_site(lines, 1, '"'"'paths'"'"'),
            module.path_value('"'"'src/legacy/**/*.ts'"'"'), reasons))
    if ident == '"'"'outside-pinned-60-char-window'"'"':
        position = lines[0].index('"'"'paths'"'"')
        print('"'"'  pinned_pre60='"'"' + repr(lines[0][max(0, position - 60):position]))
'
e2e-negated-path-key: ['Do not use paths: src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=False path_site=False path_value=True reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
e2e-commented-equals-key: ['# paths=src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=False path_site=False path_value=True reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
comment-only: ['# paths: src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=False path_site=False path_value=True reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
equals-only: ['paths=src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=False path_site=False path_value=True reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
benign-inline-colon: ['paths: src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
benign-S118-YAML-list: ['paths:', '  - "src/api/**/*.ts"']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
benign-comma-string: ['paths: "src/api/**/*.ts, tests/**/*.ts"']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
original-MutA1-V10: ['Do not set paths: src/legacy/**/*.ts in a rule that should load for every file.']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
original-G6-slash-comment: ['// paths: src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
original-G6-HTML-comment: ['<!-- paths: src/legacy/**/*.ts -->']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=True path_site=True path_value=True reasons=[]
outside-pinned-60-char-window: ['Do not use xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx paths: src/legacy/**/*.ts']
  frozen key_site=True path_site=True path_value=True reasons=[]
  v31 key_site=False path_site=False path_value=True reasons=["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
  pinned_pre60='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx '
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91; rev e6da78bbe420722dd18a13182a7c4b64ce02f005
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules_v31.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005 --fetch
scoped rule files backed on committed snapshots 4 of 4; found on the live page 4 of 4
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858; rev e6da78bbe420722dd18a13182a7c4b64ce02f005
canonical scope keys (S112/S113/S114/S115): Claude Code=paths; VS Code=applyTo; Copilot CLI=applyTo; Cursor=globs
reject Codex: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject Gemini CLI: SKILL.md rule-files cell holds no backticked token; no entry row names the client
reject opencode: SKILL.md rule-files cell holds no backticked token; no entry row names the client
EXIT_CODE=0
```

```text
$ /usr/bin/python3 -B /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_routed_repairs_v2.py --rev e6da78bbe420722dd18a13182a7c4b64ce02f005
R-a count correction: ok
R-b landed-scope names: ok
R-c base-measure pointer: ok
R-d census-after body: ok
R-e byte-exact criterion + M91: ok
R-f controls-ancestry receipt: ok
routed repairs verified 6 of 6
EXIT_CODE=0
```

```text
$ /usr/bin/sha256sum /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules.py /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_erratum_absorption.py /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules_v31.py /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_routed_repairs_v2.py /tmp/FalsifyE2eClass-cl63f12n/lane/.ufo/waves/round-62/snapshots/S118.page
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules.py
afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b  /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_erratum_absorption.py
a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_scoped_rules_v31.py
de5e347170e05738e030d681f4e2023eb3d3faec81ce352ae06924904273e7b7  /tmp/FalsifyE2eClass-cl63f12n/lane/verifiers/check_routed_repairs_v2.py
02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801  /tmp/FalsifyE2eClass-cl63f12n/lane/.ufo/waves/round-62/snapshots/S118.page
EXIT_CODE=0
```
