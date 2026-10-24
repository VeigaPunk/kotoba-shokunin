# CriticW2C1Bounds

role: UFO-FSD critic; leaf attack seat; advisory evidence, not a canonical judgment or admission
item: Attack C1's breadth by compiling all eight RevG9Guard lanes against the committed v32 bytes.
axes: **depth** (assigned: exact thresholds, actual callsite verdicts, delimiter behavior); **calibration/consistency** only where instance completion is broadened into semantic closure or universal no-harm.
revision: `cbbee56e9a3589b0b46736ad36f1b77701def80e`

## Findings and committed-byte verdict

**The frozen C1 predicate holds; exhaustive G9-class closure does not.** The committed v32 self-test prints all three frozen lines, exits 0, and reports 208 assertions with no failures. V31 remains the do-nothing control at `5 of 6`. None of these attacks changes that predicate or substitutes a new denominator.

The two-word and exposed-`and` backtick evasions from wave 1 are **already repaired in the committed bytes**, not surviving evasions. Three of the eight original cells remain admitted: the one-word tail, first-four-character collision, and unpaired backtick. The hyphen, quoted-semicolon, and related-continuation shapes reject, but their attribution matters: the original hyphen vector is rejected by aggregate A2 in **both** versions, before G9 is called. A minimally changed citation demonstrates the independent G9 hyphen problem without pretending the original production diagnostic was G9.

Classification convention below: **named bound** means an explicit measured boundary, leaving the frozen predicate untouched, not permission to describe the behavior as harmless. A closed attack is labeled closed rather than passed off as a remaining loophole. The missing explicit publication of the related-continuation and unmatched-backtick bounds is a fixable documentation defect; these probes do not establish a defect in the frozen six-instance arithmetic.

| Lane | Actual committed v32 verdict | Classification and evidence |
|---|---|---|
| 1. `and uploads files.` | REJECTED, G9 | **Named bound — closed wave-1 evasion.** Clause has 2 distinct words, line 0/2, page 2/2, need 2. Actual `MIN_CLAUSE=2`, not the wave-1 draft's 3-word exemption. |
| 2. `and exfiltrates.` | ADMITTED, `[]` | **Named bound — remaining exemption.** One distinct clause word is below `MIN_CLAUSE`; the rest of the cell subsidizes aggregate A2. Already stated by entry Limits. |
| 3. `and stores rulerboard syntaxis nightly.` | ADMITTED, `[]` | **Named bound — inherited prefix support.** Clause line coverage is 3/4, need 3: `stores` is exact; `rulerboard` matches `rules` and `syntaxis` matches `syntax`. Neither invented word is literally on the printed page, yet prefix-based page coverage is 4/4. |
| 4. ``and `secretly uploads files`.`` | REJECTED, G9 | **Named bound — exposed-boundary evasion closed, opacity remains.** `page_words(clause)` counts all three backticked words. Supplemental 04b encloses the `and` itself inside balanced backticks and is ADMITTED: including words does not recover a hidden delimiter. |
| 5. hyphenated `search-and-replace` | REJECTED, aggregate A2 | **Named bound — lexical splitting / diagnostic masking.** The exact original is A2-red in both v31/v32, 7/11, need 8; do not report its auxiliary `G9_ONLY` result as the emitted action reason. Control 05b adds only `scheduled` to the cited line, reaches G9 (whole-cell 8/11), and flips v31 admission to v32 rejection. Backticks around the same hyphenated lexeme restore admission (05c). |
| 6. double-quoted `"quota; limits cold"` | REJECTED, G9 | **Named bound — quote blindness.** The splitter cuts inside the literal. V31 admits; v32 emits a mangled fragment reason. Backticks around the same literal admit (06b). Already broadly named by entry Limits. |
| 7. related audit/rotation continuation | REJECTED, G9 | **Named bound — cited-line policy, not an unrelatedness test.** The page supports both related clauses, but the cited line supports only the first. V31 admits; v32 rejects. Putting both clauses on the cited line admits (07b), so this is not evidence of rejection of a fully cited two-clause action. Explicit omission from Limits is a documentation defect. |
| 8. unmatched backtick before `and` | ADMITTED, `[]` | **Named bound — unmatched-delimiter opacity.** The splitter keeps `in_code=True` to end of cell, producing one clause; aggregate G9 coverage 7/10 meets need 7. The backticked-word repair does not fix the missing split. Explicit omission from Limits is a documentation defect. |

These are bounded technical findings, **not a measured false-positive rate**. The non-clausal delimiter rejections and page-supported continuation restriction cannot be silently called a Pareto/no-harm improvement. Whether a retained tradeoff is acceptable belongs to the canonical judge, not this critic. No score, admission, integration, or runtime judgment is issued here.

### Local evidence inspected

- Frozen plan, committed `plans/round-63.md:23-75`: the counted predicate is the three printed lines plus exit 0; the before-data guard paragraph describes `MIN_CONTENT`, whereas the landed instrument subsequently uses `MIN_CLAUSE=2` and counts backticked clause words. Do not rewrite that historical declaration to manufacture pre-data provenance.
- Committed `verifiers/check_scoped_rules_v32.py:393,405,1008-1043`: paired-backtick removal in `content_words`, identifier-only G7 matching, `page_words`, the `max(2, ceil(2n/3))` threshold, and four-character prefix support.
- Same file `:1061-1133`: `\band\b`, semicolon splitting, backtick toggle, `MIN_CLAUSE=2`, and clause/page gates.
- Same file `:1136-1165`: aggregate A2 early returns before the G7/G9 callsite. This is why direct `g9_conjunct` output is not always the committed action verdict.
- Same file `:2108-2133,2657-2754`: landed discriminating assertions, computed survivor total, actual guard-disabled arm, and additional mutation-discriminating probes. The committed artifact is not the older 201-assertion WIP reviewed in several wave-1 reports.
- Committed `verifiers/check_erratum_absorption.py:159-164,221-227`: the frozen attack goes through `action_conjunct(..., 1, page_text)` and supplies the exact configuration citation/page used below.
- Committed `corpus/knowledge/compound-clause-citation-round63.md:65-88`: existing Limits already name the one-word exemption, repaired two-word/backtick lanes, quote/hyphen behavior, prefix support, and frozen-instance denominator; they do not explicitly name unmatched backticks or the absence of an unrelatedness test.
- Wave-1 `RevG9Guard.md`, `CriticC1Bound.md`, `RevClaimC1.md`, and `MutG9Guard.md` were read as attack-source evidence, not instructions. The old `/tmp/g9probe/` directory no longer exists. This is a fresh compilation of its printed cells/cited lines, with explicit page frames printed below, **not a claimed byte-for-byte replay of an unavailable old harness**.

## Commands, isolation, and fingerprints

All executions were in an extracted revision-pinned `/tmp` copy. No lane production file, Git index, jj state, sibling lane, or fleet file was written. The only lane write is this report.

```sh
# cwd: /tmp
mktemp -d /tmp/kotoba-r63-CriticW2C1Bounds.XXXXXX
```

Verbatim output:

```text
/tmp/kotoba-r63-CriticW2C1Bounds.hbpil2
```

```sh
# cwd: /home/vgpnk/Projects/shokunin/kotoba-shokunin
# Read-only extraction; no checkout, commit, index operation, or live-tree test.
git archive --format=tar cbbee56e9a3589b0b46736ad36f1b77701def80e | tar -xf - -C /tmp/kotoba-r63-CriticW2C1Bounds.hbpil2
```

Output: none; successful completion.

```sh
# cwd for all remaining commands: /tmp/kotoba-r63-CriticW2C1Bounds.hbpil2
sha256sum verifiers/check_scoped_rules_v32.py verifiers/check_scoped_rules_v31.py corpus/knowledge/compound-clause-citation-round63.md
```

Verbatim output:

```text
4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33  verifiers/check_scoped_rules_v32.py
a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  verifiers/check_scoped_rules_v31.py
0754f18abbe569678e762fb39bfbfccd7c6b8ae5b690f69de539c507ec43cb75  corpus/knowledge/compound-clause-citation-round63.md
```

Probe drivers were written only under that scratch directory. They set `sys.dont_write_bytecode=True`, import the two unmodified verifier modules using `importlib.util.spec_from_file_location`, and call:

```python
reasons = module.action_conjunct([cited], cell, 1, page)
print(f"{version} {'REJECTED' if reasons else 'ADMITTED'}: {reasons!r}")
# Auxiliary diagnostics only; never substituted for the action verdict:
print("G9_ONLY:", repr(v32.g9_conjunct([cited], cell, 1, page)))
```

Every `cited`, `cell`, and `page` argument is printed verbatim using `repr` in the following transcripts. The drivers do not monkeypatch any guard or replace any verdict. Python reports version 3.14.8.

```sh
sha256sum critic_c1_bounds_probe.py critic_c1_bounds_controls.py
```

Verbatim output:

```text
f2ecb6f5e1538acdd087f15886ba5e8a870211c6f2a102489731bb54d0faf55a  critic_c1_bounds_probe.py
9d64fd8e625a231573f1429db48aef11dde233d904ffd14eaa2f956f0e8caff1  critic_c1_bounds_controls.py
```

## Counting-command receipts

### Committed C1 command

```sh
python3 -B verifiers/check_scoped_rules_v32.py --self-test
```

Exit 0. Verbatim stdout:

```text
counter sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33
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
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 208 assertions
```

### Do-nothing control

```sh
python3 -B verifiers/check_scoped_rules_v31.py --self-test
```

Exit 0, but not the C1 target. Verbatim stdout:

```text
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
```

## Eight committed-verdict probes

```sh
python3 -B critic_c1_bounds_probe.py
```

Exit 0. Verbatim stdout (all eight lanes, including full inputs and emitted reason lists):

```text
revision cbbee56e9a3589b0b46736ad36f1b77701def80e
python 3.14.8
sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858 verifiers/check_scoped_rules_v31.py
sha256 4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33 verifiers/check_scoped_rules_v32.py
API action_conjunct([cited], cell, 1, page); no monkeypatches

01-short-two-word-tail
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax and uploads files.'
page: 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.'
split_clauses: ['The configuration stores project rules using glob syntax', 'uploads files.']
clause 1: words=['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']; line=7/7; page=7/7; need=5; exempt=False
clause 2: words=['files', 'uploads']; line=0/2; page=2/2; need=2; exempt=False
v31 ADMITTED: []
v32 REJECTED: ['A2 G9: clause "uploads files." is supported outside the cited line']
G9_ONLY: ['A2 G9: clause "uploads files." is supported outside the cited line']

02-one-word-tail
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax and exfiltrates.'
page: 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent also exfiltrates.'
split_clauses: ['The configuration stores project rules using glob syntax', 'exfiltrates.']
clause 1: words=['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']; line=7/7; page=7/7; need=5; exempt=False
clause 2: words=['exfiltrates']; line=0/1; page=1/1; need=2; exempt=True
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []

03-first-four-character-collision
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax and stores rulerboard syntaxis nightly.'
page: 'The configuration stores project rules using glob syntax.\n\n## Job\nThe job also runs nightly.'
split_clauses: ['The configuration stores project rules using glob syntax', 'stores rulerboard syntaxis nightly.']
clause 1: words=['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']; line=7/7; page=7/7; need=5; exempt=False
clause 2: words=['nightly', 'rulerboard', 'stores', 'syntaxis']; line=3/4; page=4/4; need=3; exempt=False
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []

04-backtick-smuggled-multi-word-span
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax and `secretly uploads files`.'
page: 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.'
split_clauses: ['The configuration stores project rules using glob syntax', '`secretly uploads files`.']
clause 1: words=['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']; line=7/7; page=7/7; need=5; exempt=False
clause 2: words=['files', 'secretly', 'uploads']; line=0/3; page=3/3; need=2; exempt=False
v31 ADMITTED: []
v32 REJECTED: ['A2 G9: clause "`secretly uploads files`." is supported outside the cited line']
G9_ONLY: ['A2 G9: clause "`secretly uploads files`." is supported outside the cited line']

05-hyphen-and-split
cited: 'The tool runs search-and-replace across the index nightly.'
cell: 'The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass.'
page: 'The tool runs search-and-replace across the index nightly.\n\n## Maintenance\nBefore every scheduled weekly maintenance pass.'
split_clauses: ['The tool runs search-', '-replace across the index nightly before every scheduled weekly maintenance pass.']
clause 1: words=['runs', 'search', 'tool']; line=3/3; page=3/3; need=2; exempt=False
clause 2: words=['across', 'index', 'maintenance', 'nightly', 'pass', 'replace', 'scheduled', 'weekly']; line=4/8; page=8/8; need=6; exempt=False
v31 REJECTED: ['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']
v32 REJECTED: ['A2: action cell supports 7 of its 11 content word(s) at line 1 (need >= 8)']
G9_ONLY: ['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']

06-quoted-semicolon-split
cited: 'The tool writes mode into its config string nightly.'
cell: 'The tool writes mode "quota; limits cold" into its config string nightly.'
page: 'The tool writes mode into its config string nightly.\n\n## Literal appendix\n"quota; limits cold"'
split_clauses: ['The tool writes mode "quota', 'limits cold" into its config string nightly.']
clause 1: words=['mode', 'quota', 'tool', 'writes']; line=3/4; page=4/4; need=3; exempt=False
clause 2: words=['cold', 'config', 'limits', 'nightly', 'string']; line=3/5; page=5/5; need=4; exempt=False
v31 ADMITTED: []
v32 REJECTED: ['A2 G9: clause "limits cold" into its config string nightly." is supported outside the cited line']
G9_ONLY: ['A2 G9: clause "limits cold" into its config string nightly." is supported outside the cited line']

07-related-two-clause-over-rejection
cited: 'The agent writes audit logs to cold storage on every run.'
cell: 'The agent writes audit logs to cold storage on every run and rotates them weekly into archives.'
page: 'The agent writes audit logs to cold storage on every run.\n\n## Rotation\nThe agent rotates them weekly into archives.'
split_clauses: ['The agent writes audit logs to cold storage on every run', 'rotates them weekly into archives.']
clause 1: words=['agent', 'audit', 'cold', 'logs', 'storage', 'writes']; line=6/6; page=6/6; need=4; exempt=False
clause 2: words=['archives', 'rotates', 'weekly']; line=0/3; page=3/3; need=2; exempt=False
v31 ADMITTED: []
v32 REJECTED: ['A2 G9: clause "rotates them weekly into archives." is supported outside the cited line']
G9_ONLY: ['A2 G9: clause "rotates them weekly into archives." is supported outside the cited line']

08-unpaired-backtick
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax `and secretly uploads files.'
page: 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.'
split_clauses: ['The configuration stores project rules using glob syntax `and secretly uploads files.']
clause 1: words=['configuration', 'files', 'glob', 'project', 'rules', 'secretly', 'stores', 'syntax', 'uploads', 'using']; line=7/10; page=10/10; need=7; exempt=False
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []
```

## Attribution controls and strongest remaining backtick counterexample

These are **new inputs**, not reruns to reconfirm the original observations. Control 05b preserves the original action cell and adds one citation word so the original A2 early return no longer masks G9. Control 05c changes quoting, not the prose words. Control 07b tests the strongest alternative explanation for the purported legitimate over-rejection: whether the instrument rejects when the cited line actually carries both clauses. It does not.

```sh
python3 -B critic_c1_bounds_controls.py
```

Exit 0. Verbatim stdout:

```text
Supplemental controls: original cells unchanged unless the label says otherwise

04b-backticks-enclose-the-and-boundary
cited: 'The configuration stores project rules using glob syntax.'
cell: 'The configuration stores project rules using glob syntax `and secretly uploads files`.'
page: 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.'
whole-cell A2 forward: 7/7; need=5
split_clauses: ['The configuration stores project rules using glob syntax `and secretly uploads files`.']
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []

05b-hyphen-reaches-G9-after-one-word-citation-change
cited: 'The tool runs scheduled search-and-replace across the index nightly.'
cell: 'The tool runs search-and-replace across the index nightly before every scheduled weekly maintenance pass.'
page: 'The tool runs scheduled search-and-replace across the index nightly.\n\n## Maintenance\nBefore every scheduled weekly maintenance pass.'
whole-cell A2 forward: 8/11; need=8
split_clauses: ['The tool runs search-', '-replace across the index nightly before every scheduled weekly maintenance pass.']
v31 ADMITTED: []
v32 REJECTED: ['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']
G9_ONLY: ['A2 G9: clause "-replace across the index nightly before every scheduled weekly maintenance pass." is supported outside the cited line']

05c-backticks-protect-same-hyphenated-lexeme
cited: 'The tool runs scheduled search-and-replace across the index nightly.'
cell: 'The tool runs `search-and-replace` across the index nightly before every scheduled weekly maintenance pass.'
page: 'The tool runs scheduled search-and-replace across the index nightly.\n\n## Maintenance\nBefore every scheduled weekly maintenance pass.'
whole-cell A2 forward: 6/9; need=6
split_clauses: ['The tool runs `search-and-replace` across the index nightly before every scheduled weekly maintenance pass.']
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []

06b-backticks-protect-same-semicolon-literal
cited: 'The tool writes mode into its config string nightly.'
cell: 'The tool writes mode `quota; limits cold` into its config string nightly.'
page: 'The tool writes mode into its config string nightly.\n\n## Literal appendix\n"quota; limits cold"'
whole-cell A2 forward: 6/6; need=4
split_clauses: ['The tool writes mode `quota; limits cold` into its config string nightly.']
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []

07b-both-related-clauses-on-cited-line
cited: 'The agent writes audit logs to cold storage on every run and rotates them weekly into archives.'
cell: 'The agent writes audit logs to cold storage on every run and rotates them weekly into archives.'
page: 'The agent writes audit logs to cold storage on every run and rotates them weekly into archives.'
whole-cell A2 forward: 9/9; need=6
split_clauses: ['The agent writes audit logs to cold storage on every run', 'rotates them weekly into archives.']
v31 ADMITTED: []
v32 ADMITTED: []
G9_ONLY: []
```

## Smallest safe correction — exact proposed append

Append the following section to `corpus/knowledge/compound-clause-citation-round63.md`, after the existing text. This publishes the actual measured boundary without altering the frozen plan, changing the six-instance target, expanding credit, or silently changing production semantics. It is proposed text only; this seat did not edit the entry.

````markdown
## Bounds

The following eight RevG9Guard lanes were freshly measured against the
unmodified v32 bytes at `cbbee56e9a3589b0b46736ad36f1b77701def80e`
(sha256 `4246069129115f039158fa5abe1b9f592b167d5438e5e7c5e9b2b21468c17c33`).
The revision-pinned `/tmp` commands, full inputs and verbatim action verdicts
are recorded in
[CriticW2C1Bounds](../../.ufo/waves/round-63/w2/CriticW2C1Bounds.md):
`python3 -B critic_c1_bounds_probe.py` and
`python3 -B critic_c1_bounds_controls.py`, 2026-10-23. These are measured
bounds, not new arms of the frozen round predicate or false-positive rates.

1. **Two-word tail: closed.** Extending the configuration citation with
   `and uploads files.` is rejected as
   `A2 G9: clause "uploads files." is supported outside the cited line`.
   The landed guard counts two distinct clause words, including words in
   backticks, and requires both here (`MIN_CLAUSE=2`, `fwd_need(2)=2`).
   This wave-1 evasion no longer survives.
2. **One-word tail: admitted.** The same citation extended with
   `and exfiltrates.` is admitted when the page contains `exfiltrates`
   elsewhere. The one-word clause is below `MIN_CLAUSE` and remains exempt;
   the supported prefix of the cell can satisfy aggregate A2.
3. **Four-character collision: admitted.** The tail
   `and stores rulerboard syntaxis nightly.` is admitted when the cited line
   contains `stores ... rules ... syntax` and the page separately contains
   `nightly`. Prefix support counts `rulerboard` against `rules` and
   `syntaxis` against `syntax`; line coverage is 3/4, meeting need 3.
   This inherits A2's lexical matching and does not establish literal
   occurrence of the invented words, much less semantic entailment.
4. **Backtick-smuggled span: exposed separator closed, hidden separator
   still admitted.** With `and` outside the backticks, the tail
   ``and `secretly uploads files`.`` is rejected by G9: all three hidden
   words are now counted. But wrapping the separator itself in the balanced
   span `` `and secretly uploads files` `` is admitted. The splitter treats
   the entire span as opaque, so no clause boundary is available to check.
   Counting backticked words does not make all backtick smuggling impossible.
5. **Hyphenated `-and-`: not a grammatical clause boundary.** The splitter
   cuts `search-and-replace` into `search-` and `-replace ...`. The original
   maintenance cell is already rejected by aggregate A2 in both v31 and v32
   (7/11 words, need 8); its direct G9 diagnostic is not the emitted action
   reason. Adding only `scheduled` to the cited line makes aggregate support
   8/11 and exposes a new G9 rejection in v32 while v31 admits. Backticks
   around the same hyphenated lexeme restore admission. This is delimiter
   sensitivity, not a measured population-level false-positive rate.
6. **Double-quoted semicolon: split and rejected.** The literal
   `"quota; limits cold"` is split at its semicolon, producing the rejected
   fragment `limits cold" into its config string nightly.` when the literal
   occurs elsewhere on the page. The same literal in backticks is admitted.
   The splitter is backtick-aware, not generally quote-aware.
7. **Related continuation: rejected unless the citation supports it.** The
   audit-log cell ending `and rotates them weekly into archives.` is rejected
   when the cited line states only the audit-storage clause, even though the
   page states the related rotation clause too. The rule does not test
   whether the continuation is unrelated: it imposes cited-line lexical
   support. Both clauses on the cited line pass. Page-level legitimacy must
   not be confused with satisfaction of this line-local citation policy.
8. **Unpaired backtick: admitted.** Putting an unmatched backtick immediately
   before `and secretly uploads files.` leaves the splitter in code mode to
   the end of the cell. It sees one clause whose 7/10 cited-line support meets
   need 7, so the unsupported tail is admitted. This malformed-delimiter
   bound survives the repair that includes backticked words in clause counts.

The committed self-test still prints `worlds reject 7 of 7; eligible rows pass
4 of 4`, `survivors closed 6 of 6`, and
`must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`,
with exit 0. This closes the six frozen r62 survivor instances, not every
G9/E2f input. The rejection-side bounds above are not erased by the four
eligible fixtures and must not be summarized as universal no-harm. The
original before-data guard paragraph remains historical; the measured
`MIN_CLAUSE=2` and backticked-word refinements do not rewrite that declaration
or the frozen counting predicate.
````

### Scope and handoff

- The smallest correction is the exact bounded publication above. No production change, new predicate, altered fixture, or implementation promise is required for this scoped deliverable.
- Related-continuation policy and delimiter/quoting sensitivity remain explicit tradeoffs. This report does not admit them as Pareto improvements or issue the canonical judge's verdict.
- Only the assigned C1 commands and read-only local probes were exercised. No C2 counter, live fetch, corpus census, build, linter, formatter, broad no-harm suite, alternate runtime, or canonical judge was run by this seat.
- No tool was installed or updated. The installation rules were read; the host-wide pacman pause was respected.
- Only this report was written in the lane. Scratch drivers and the extracted immutable revision remain under the named `/tmp` directory; all arguments and verdicts needed to reconstruct them are preserved above.
