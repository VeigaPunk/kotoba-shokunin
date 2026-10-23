# FalsifyE2fPair — computed closure, incomplete G7

Assigned axis: **depth**. Collateral: calibration/provenance (which pair and which guard were actually measured). This is a scoped critic report, not a canonical judgment, admission, integration, or shipping decision.

Reviewed revision: `e6da78bbe420722dd18a13182a7c4b64ce02f005`. Read `plans/round-62.md` first. All executable inputs below were extracted from that commit into `/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox`; no lane product was edited. The preparation command in § Reproduction bound the frozen counter to SHA-256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`, absorption instrument to `afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b`, and successor to `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`.

## Counterexample and answer

**The landed successor computes actual verdicts; it is not the label-only no-op described by the earlier scratch attack. But its G7 is weaker than the frozen claim-span requirement, and the published event attack still survives it.**

Results from **R1**, with each exact function call and reason list retained below:

| Pair / instance | Frozen v3 | Landed v3.1 | v3.1, only G7 disabled |
|---|---|---|---|
| Published `E2f-event-token-backticked`, S103:194 | accepted | **accepted** | accepted |
| Published `E2f-W6-sib-style`, S103:209 | rejected, reverse fraction | rejected, same reason | rejected, same reason |
| Published pair rejected | **1 of 2** | **1 of 2** | **1 of 2** |
| Instrument `e2f-backticked-event-claim`, synthetic line | accepted | rejected, `A2 G7` | accepted |
| Instrument `e2f-compound-purpose-outside-citation`, synthetic page | accepted | accepted | accepted |
| Instrument pair rejected | **0 of 2** | **1 of 2** | **0 of 2** |

The pairs are **not identical inputs under renamed IDs**. `w1/ExecInstancesA2.md:23-34` uses the committed S103 page and its actual citation lines. `check_erratum_absorption.py:215-227` instead uses a synthetic event line whose entire page lacks `InstructionsLoaded`, plus a different compound-purpose/G9 attack. The latter replaces the published W6-sib member; it is intentionally retained as a surviving G9 bound. No observation here establishes post-data selection or dishonest timing. It does establish that the published pair's measured rejection fraction cannot be attributed to the instrument's frozen pair.

### Fixable defect: page presence is not G7 claim-span

The strongest counterexample is already committed: the published event cell, using its original S103 page, returns `[]` under the landed v3.1 (**R1**). `S103.page:194` states path scoping, not the asserted event. The identifier appears elsewhere on that same page (`:427`, `:599`).

The mechanism is exact:

- `check_scoped_rules_v31.py:405` matches only single-backticked identifier-shaped tokens.
- `g7_conjunct`, `:1046-1058`, rejects a token only if it occurs in **neither** the cited line **nor the entire page**. It does not require claim words to co-occur on one line and does not detect raw load/event claims independently of identifier backticks.
- `action_conjunct`, `:1088`, really invokes that guard after the original overlap checks.
- **R1** also appends the synthetic event's missing identifier under an unrelated heading, without changing the action or cited line. That changes its successor result from an `A2 G7` rejection to `[]`. This is a direct page-bag witness, not a claim that the guard was skipped.

The frozen requirement is narrower in applicability but stronger in evidence: `plans/round-61.md:241-254` says a raw load/event claim requires all cell words on one line; it forbids imposing that restriction on non-claim cells and excludes `apply` from the claim-verb set. `plans/round-62.md:73-76` carries G5 plus that G7 form forward; the pre-data amendments at `:265-292` move the successor out of the counted predicate and permit named residuals. They do not turn whole-page identifier occurrence into claim-span checking. The original plan's committed/current identity was checked by **R5**.

This is a **fixable semantic-coverage defect**, not evidence that the matrix's current count was printed from labels. It also is not a reason to implement G9, remove benign positives, change the immutable v3 counter, or credit full G7 closure from the synthetic witness alone. Whether a bounded partial successor warrants the claimed axis move belongs to the canonical judge, not this seat.

### The no-op-label concern does not describe the landed counting path

`CriticC1Hollow.md:14,107-156` explicitly tested a scratch no-op before a final lane successor existed. Its warning was valid for that counterfeit surface. The landed implementation instead:

1. Imports the instrument and calls its pinned-counter loader (`v31:2543-2552`).
2. Calls every selected survivor's `Attack.score` against both the frozen and current modules (`:2571-2574`). The E2f adapter calls `counter.action_conjunct(lines, cell, 1, page_text)` (`absorption:159-164`).
3. Uses the actual lists for the before/after classifications and `survivors_closed = sum(...)` (`v31:2575-2586`). The `expected_after` tuple is an assertion target, not the numerator's source. The fixed survivor-ID set/denominator identifies this catalogue, not universal coverage.
4. Disables only the actual `g7_conjunct`, rescores the same event, restores the function, and asserts admission (`:2600-2610`).

The old `E2f fresh instances reject 2 of 2` label is absent from the landed file (**R1**). Its actual output is `survivors closed 5 of 6` (**R3**). Making G7 a no-op in memory while retaining the public `main(['--self-test'])` route changes that to **`survivors closed 4 of 6`**, produces the actual event's `after accepted` record, and exits **1** with the failure output in **R4**. Thus the landed arm distinguishes this no-op; it is not merely assigning its own expected labels.

## Smallest safe correction

Keep the frozen v3 file, matrix catalogue, existing receipts, and explicit G9 bound unchanged. Add the **published S103 event** as an additional successor regression, not a silent replacement of the frozen matrix pair. Implement G7's raw claim detection and same-line claim-span requirement, without applying it to non-claim action cells; retain the current positive Action controls. Require that published event's real `A2 G7` rejection, and its admission when only G7 is disabled. Do not attribute W6-sib's old reverse-fraction rejection to G7.

If the successor remains only a backticked-identifier presence guard, explicitly name the still-accepted published event as a residual wherever its G7 closure is described. The measured `survivors closed 5 of 6` remains honest **for its catalogue**; it is not proof of full E2f/G7 absorption. Relevant reporting surfaces are `SKILL.md:490`, `LOG.md:2550-2551`, and the knowledge entry's § E2f gap and successor. The entry already describes the implemented check more narrowly as raw evidence for backticked identifiers; the broader G7 attribution needs the residual distinction.

## Scoped ledger, registry, and S118 check

- **R2** reproduces the absorption receipt's complete headline and survivor list. E2f's frozen catalogue has both instances surviving under v3. **R3** reproduces the successor receipt's computed closure output and named G9 bound. `corpus/knowledge/erratum-absorption-round62.md:15,28-39`, the corresponding `SKILL.md:486,488,490` gate rows, and `LOG.md:2548,2550` use those catalogue results rather than the old published-pair fraction. `SCORECARD.md:36` explicitly makes v3.1 separate fix evidence, not C1's counted predicate. These observed correspondences do not certify unrelated C2, census, no-harm, or hollow-auditor claims.
- Reopened [S118's source](https://code.claude.com/docs/en/memory.md) using `read` at URL ranges `:244-252` and then `:256-262`; the live row says: `Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string`. The pinned `.ufo/waves/round-62/snapshots/S118.page:250` carries the same displayed row. Preparation measured that committed snapshot at SHA-256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`. This supports the documented `paths` form, **not** E2f event semantics. This source reopening is a rendered-text observation, not a contemporary HTTP-status, raw-byte-equality, or new acquisition-hash claim.

## Executed evidence

All shell commands used timeout 120 seconds, no background jobs. Git-writing self-tests ran only in the sandbox clone, with `TMPDIR` inside it. Exit codes below are observed command exits, separated from exact stdout where the command itself did not print an exit marker.

### R1 — both reconstructed pairs, exact calls, controls, and page-bag witness

Command:

```sh
python3 -B /tmp/kotoba-r62-FalsifyE2fPair-20261023/probe_pairs.py
```

Working directory: `/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox`. Observed exit: **0**. Exact stdout:

```text
revision=e6da78bbe420722dd18a13182a7c4b64ce02f005
verifiers/check_scoped_rules.py sha256=5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
verifiers/check_erratum_absorption.py sha256=afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b
verifiers/check_scoped_rules_v31.py sha256=a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
S103_page=Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/.ufo/waves/round-60/snapshots/S103.page').read_text(); S103_lines=S103_page.splitlines(); sha256=82d60341354924ee8658de0fcde297c2ac37b237dcc931aa4a83329b2c7bb6e7
S106_page=Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/.ufo/waves/round-60/snapshots/S106.page').read_text(); S106_lines=S106_page.splitlines(); sha256=00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980
S105_page=Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/.ufo/waves/round-60/snapshots/S105.page').read_text(); S105_lines=S105_page.splitlines(); sha256=a45c9e9f50c62949ea60711c6d657d065752c573a0c945215f32063fa56caa1f
S108_page=Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/.ufo/waves/round-60/snapshots/S108.page').read_text(); S108_lines=S108_page.splitlines(); sha256=884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8
== published_ExecInstancesA2
E2f-event-token-backticked: frozen.action_conjunct(S103_lines, 'The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)', 194, S103_page) -> []; verdict=ACCEPTED
  frozen support: forward=8/10 need=7; reverse=8/15 need=5
E2f-W6-sib-style: frozen.action_conjunct(S103_lines, 'Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)', 209, S103_page) -> ["A2: the cited line's 34 content word(s) are supported 8 time(s) by the action cell at line 209 (need >= 12): the line does not state the claim"]; verdict=REJECTED
  frozen support: forward=6/8 need=6; reverse=8/34 need=12
published_ExecInstancesA2: frozen rejected 1 of 2
E2f-event-token-backticked: v31.action_conjunct(S103_lines, 'The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)', 194, S103_page) -> []; verdict=ACCEPTED
E2f-W6-sib-style: v31.action_conjunct(S103_lines, 'Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)', 209, S103_page) -> ["A2: the cited line's 34 content word(s) are supported 8 time(s) by the action cell at line 209 (need >= 12): the line does not state the claim"]; verdict=REJECTED
published_ExecInstancesA2: v31 rejected 1 of 2
E2f-event-token-backticked: v31_G7_disabled.action_conjunct(S103_lines, 'The `InstructionsLoaded` event loads rules only when Claude works with specific matching files and specified patterns. (S103 :194)', 194, S103_page) -> []; verdict=ACCEPTED
E2f-W6-sib-style: v31_G7_disabled.action_conjunct(S103_lines, 'Create the rule file in the project and add frontmatter so it loads only for the matching files. (S103 :209)', 209, S103_page) -> ["A2: the cited line's 34 content word(s) are supported 8 time(s) by the action cell at line 209 (need >= 12): the line does not state the claim"]; verdict=REJECTED
published_ExecInstancesA2: v31_G7_disabled rejected 1 of 2
== instrument_frozen_E2f
e2f-backticked-event-claim: frozen.action_conjunct(['When agent reads file runtime emits event and loads matching rule files.'], 'When agent reads file runtime emits event and loads matching rule files `InstructionsLoaded`.', 1, 'When agent reads file runtime emits event and loads matching rule files.') -> []; verdict=ACCEPTED
  frozen support: forward=10/10 need=7; reverse=10/10 need=4
e2f-compound-purpose-outside-citation: frozen.action_conjunct(['The configuration stores project rules using glob syntax.'], 'The configuration stores project rules using glob syntax and secretly uploads files.', 1, 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.') -> []; verdict=ACCEPTED
  frozen support: forward=7/10 need=7; reverse=7/7 need=3
instrument_frozen_E2f: frozen rejected 0 of 2
e2f-backticked-event-claim: v31.action_conjunct(['When agent reads file runtime emits event and loads matching rule files.'], 'When agent reads file runtime emits event and loads matching rule files `InstructionsLoaded`.', 1, 'When agent reads file runtime emits event and loads matching rule files.') -> ['A2 G7: backticked identifier(s) InstructionsLoaded occur in neither the cited line nor the committed snapshot']; verdict=REJECTED
e2f-compound-purpose-outside-citation: v31.action_conjunct(['The configuration stores project rules using glob syntax.'], 'The configuration stores project rules using glob syntax and secretly uploads files.', 1, 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.') -> []; verdict=ACCEPTED
instrument_frozen_E2f: v31 rejected 1 of 2
e2f-backticked-event-claim: v31_G7_disabled.action_conjunct(['When agent reads file runtime emits event and loads matching rule files.'], 'When agent reads file runtime emits event and loads matching rule files `InstructionsLoaded`.', 1, 'When agent reads file runtime emits event and loads matching rule files.') -> []; verdict=ACCEPTED
e2f-compound-purpose-outside-citation: v31_G7_disabled.action_conjunct(['The configuration stores project rules using glob syntax.'], 'The configuration stores project rules using glob syntax and secretly uploads files.', 1, 'The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.') -> []; verdict=ACCEPTED
instrument_frozen_E2f: v31_G7_disabled rejected 0 of 2
== published F6 and four eligible Action controls
F6-compound-purpose-bound: frozen.action_conjunct(S106_lines, 'Create instructions files with glob syntax and organize the copies in the project directory. (S106 :60)', 60, S106_page) -> []; verdict=ACCEPTED
F6-compound-purpose-bound: v31.action_conjunct(S106_lines, 'Create instructions files with glob syntax and organize the copies in the project directory. (S106 :60)', 60, S106_page) -> []; verdict=ACCEPTED
eligible-Claude-S103: frozen.action_conjunct(S103_lines, 'Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)', 194, S103_page) -> []; verdict=ACCEPTED
eligible-Claude-S103: v31.action_conjunct(S103_lines, 'Scope rules to specific files using YAML frontmatter; apply only when matching specified patterns. (S103 :194)', 194, S103_page) -> []; verdict=ACCEPTED
eligible-VS-Code-S105: frozen.action_conjunct(S105_lines, 'Use multiple instruction files per topic and apply them selectively (S105 :329)', 329, S105_page) -> []; verdict=ACCEPTED
eligible-VS-Code-S105: v31.action_conjunct(S105_lines, 'Use multiple instruction files per topic and apply them selectively (S105 :329)', 329, S105_page) -> []; verdict=ACCEPTED
eligible-Copilot-S106: frozen.action_conjunct(S106_lines, 'Create a path-specific instruction file with an applyTo glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60)', 60, S106_page) -> []; verdict=ACCEPTED
eligible-Copilot-S106: v31.action_conjunct(S106_lines, 'Create a path-specific instruction file with an applyTo glob; use glob syntax to specify the files or directories the instructions apply to (S106 :60)', 60, S106_page) -> []; verdict=ACCEPTED
eligible-Cursor-S108: frozen.action_conjunct(S108_lines, 'Use globs to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)', 131, S108_page) -> []; verdict=ACCEPTED
eligible-Cursor-S108: v31.action_conjunct(S108_lines, 'Use globs to scope a rule to specific files or directories. Separate multiple patterns with commas. (S108 :131)', 131, S108_page) -> []; verdict=ACCEPTED
== same synthetic event, identifier moved to an unrelated page line
v31.action_conjunct(['When agent reads file runtime emits event and loads matching rule files.'], 'When agent reads file runtime emits event and loads matching rule files `InstructionsLoaded`.', 1, 'When agent reads file runtime emits event and loads matching rule files.\n\n## Unrelated section\n`InstructionsLoaded`') -> []; verdict=ACCEPTED
legacy_E2f_2_of_2_label_in_landed_successor=False
```

### R2 — matrix counting command

```sh
env TMPDIR=/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/tmp python3 -B /tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/verifiers/check_erratum_absorption.py --self-test
```

Observed exit: **0**. Exact stdout:

```text
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
```

### R3 — landed successor public self-test

```sh
env TMPDIR=/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/tmp python3 -B /tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/verifiers/check_scoped_rules_v31.py --self-test
```

Observed exit: **0**. Exact stdout:

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

### R4 — only G7 made a no-op, same public main

```sh
env TMPDIR=/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/tmp python3 -B /tmp/kotoba-r62-FalsifyE2fPair-20261023/noop_g7.py
```

Observed exit: **1**. Exact stdout:

```text
in-memory mutation: g7_conjunct = lambda *_args: []; source file unchanged
counter sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858
FAIL A2 G7: an unsupported backticked identifier is rejected: got False, expected True
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: A1: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
world W6: Claude Code reject=True arm=A2 line='entry row S900: snapshot .ufo/waves/round-60/snapshots/S900.page: A2: action cell supports 5 of its 8 content word(s) at line 6 (need >= 6)'
world W7: all reject=True arm=A1
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
FAIL successor survivor verdicts preserve the declared G9 bound: got (True, True, True, True, False, False), expected (True, True, True, True, True, False)
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after accepted
survivor e2f-compound-purpose-outside-citation: before accepted; after accepted
survivors closed 4 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
self-test: 2 failure(s) over 201 assertions
```

### R5 — original G7 contract binding

```sh
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:plans/round-61.md | sha256sum && sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-61.md
```

Observed exit: **0**. Exact stdout:

```text
a9603b282b56ee49d48e02c0884524f9cd5db2e320c124094b7781a411455866  -
a9603b282b56ee49d48e02c0884524f9cd5db2e320c124094b7781a411455866  /home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-61.md
```

## Reproduction sources

Scratch is not durable evidence. The complete preparation, pair probe, and no-op driver sources are retained here so the committed report plus pinned lane objects suffice to reconstruct the experiments. Save them to the absolute command paths used above; run preparation in a fresh sandbox location if the existing scratch is absent. No checkout, add, commit, reset, or index operation is needed in the lane.

Preparation command (observed exit **0**, Python version output `python=3.14.8`, clone output `clone_exit=0`):

```sh
python3 -B /tmp/kotoba-r62-FalsifyE2fPair-20261023/prepare.py
```

`prepare.py`:

```python
from pathlib import Path
import hashlib
import subprocess
import sys

LANE = Path('/home/vgpnk/Projects/shokunin/kotoba-shokunin')
REV = 'e6da78bbe420722dd18a13182a7c4b64ce02f005'
ROOT = Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023')
SANDBOX = ROOT / 'sandbox'
FILES = [
    'plans/round-62.md',
    'verifiers/check_scoped_rules.py',
    'verifiers/check_scoped_rules_v31.py',
    'verifiers/check_erratum_absorption.py',
    '.ufo/waves/round-62/w1/ExecInstancesA2.md',
    '.ufo/waves/round-62/w1/CriticC1Hollow.md',
    '.ufo/waves/round-62/C1-absorb-measure.txt',
    '.ufo/waves/round-62/C1-v31-successor.txt',
    '.ufo/waves/round-60/snapshots/S103.page',
    '.ufo/waves/round-60/snapshots/S105.page',
    '.ufo/waves/round-60/snapshots/S106.page',
    '.ufo/waves/round-60/snapshots/S108.page',
    '.ufo/waves/round-62/snapshots/S118.page',
    'corpus/SOURCES.md',
    'corpus/knowledge/erratum-absorption-round62.md',
    'corpus/lessons/round-62.md',
    'corpus/QUALITY.md',
    'SKILL.md',
    'LOG.md',
    'SCORECARD.md',
]
print('python=' + sys.version.split()[0], flush=True)
print('pinned_revision=' + REV, flush=True)
cmd = ['git', 'clone', '--no-checkout', '--local', '--no-hardlinks', '--quiet', str(LANE), str(SANDBOX)]
print('$ ' + ' '.join(cmd), flush=True)
result = subprocess.run(cmd, text=True, capture_output=True, timeout=110)
print(result.stdout, end='')
print(result.stderr, end='', file=sys.stderr)
print('clone_exit=' + str(result.returncode), flush=True)
result.check_returncode()
for name in FILES:
    command = ['git', '-C', str(LANE), 'show', f'{REV}:{name}']
    result = subprocess.run(command, capture_output=True, timeout=15)
    result.check_returncode()
    dest = SANDBOX / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(result.stdout)
    digest = hashlib.sha256(result.stdout).hexdigest()
    current = LANE / name
    matches = current.read_bytes() == result.stdout
    print(f'git show {REV}:{name}: exit={result.returncode}; bytes={len(result.stdout)}; sha256={digest}; working_tree_equals_committed={matches}', flush=True)
(SANDBOX / 'tmp').mkdir()
print('sandbox=' + str(SANDBOX), flush=True)
```

`probe_pairs.py`:

```python
from pathlib import Path
import ast
import hashlib
import importlib.util
import sys

ROOT = Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023')
SANDBOX = ROOT / 'sandbox'
REV = 'e6da78bbe420722dd18a13182a7c4b64ce02f005'
PIN = '5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91'

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

absorption = load('review_absorption', SANDBOX / 'verifiers/check_erratum_absorption.py')
frozen = absorption.load_counter(SANDBOX / 'verifiers/check_scoped_rules.py')
successor = load('review_successor', SANDBOX / 'verifiers/check_scoped_rules_v31.py')
assert frozen.self_sha() == PIN
print('revision=' + REV)
for path in ('verifiers/check_scoped_rules.py', 'verifiers/check_erratum_absorption.py', 'verifiers/check_scoped_rules_v31.py'):
    print(path + ' sha256=' + hashlib.sha256((SANDBOX / path).read_bytes()).hexdigest())

report = (SANDBOX / '.ufo/waves/round-62/w1/ExecInstancesA2.md').read_text()
source = report.split('```python\n', 1)[1].split('```', 1)[0]
assignment = ast.parse(source).body[0]
assert isinstance(assignment, ast.Assign)
assert assignment.targets[0].id == 'CASES'
published = ast.literal_eval(assignment.value)
case_calls = []
page_names = {}
for ident, path, line, cell in published:
    page = (SANDBOX / path).read_text()
    name = Path(path).stem
    if name not in page_names:
        page_names[name] = page
        print(f'{name}_page=Path({str(SANDBOX / path)!r}).read_text(); {name}_lines={name}_page.splitlines(); sha256={hashlib.sha256(page.encode()).hexdigest()}')
    case_calls.append((ident, (page.splitlines(), cell, line, page), f'{name}_lines, {cell!r}, {line}, {name}_page'))

class Capture:
    def __init__(self):
        self.calls = []
    def action_conjunct(self, *args):
        self.calls.append(args)
        return frozen.action_conjunct(*args)

captured = Capture()
frozen_calls = []
for erratum in absorption.ERRATA:
    if erratum.name == 'E2f':
        for attack in erratum.attacks:
            start = len(captured.calls)
            attack.score(captured)
            assert len(captured.calls) == start + 1
            args = captured.calls[-1]
            frozen_calls.append((attack.ident, args, ', '.join(repr(arg) for arg in args)))

for pair_name, cases in [('published_ExecInstancesA2', case_calls[:2]), ('instrument_frozen_E2f', frozen_calls)]:
    print('== ' + pair_name)
    for mode in ('frozen', 'v31', 'v31_G7_disabled'):
        module = frozen if mode == 'frozen' else successor
        saved_g7 = successor.g7_conjunct
        if mode == 'v31_G7_disabled':
            successor.g7_conjunct = lambda *_args: []
        try:
            rejected = 0
            for ident, args, expression in cases:
                reasons = module.action_conjunct(*args)
                rejected += bool(reasons)
                print(f'{ident}: {mode}.action_conjunct({expression}) -> {reasons!r}; verdict={"REJECTED" if reasons else "ACCEPTED"}')
                if mode == 'frozen':
                    lines, cell, line, page = args
                    cell_words = frozen.content_words(cell)
                    line_words = frozen.content_words(lines[line - 1])
                    print(f'  frozen support: forward={frozen.covered(cell_words, line_words)}/{len(cell_words)} need={frozen.fwd_need(len(cell_words))}; reverse={frozen.covered(line_words, cell_words)}/{len(line_words)} need={frozen.rev_need(len(line_words))}')
            print(f'{pair_name}: {mode} rejected {rejected} of {len(cases)}')
        finally:
            successor.g7_conjunct = saved_g7

print('== published F6 and four eligible Action controls')
for ident, args, expression in case_calls[2:]:
    for mode, module in [('frozen', frozen), ('v31', successor)]:
        reasons = module.action_conjunct(*args)
        print(f'{ident}: {mode}.action_conjunct({expression}) -> {reasons!r}; verdict={"REJECTED" if reasons else "ACCEPTED"}')

print('== same synthetic event, identifier moved to an unrelated page line')
ident, (lines, cell, line, page), _ = frozen_calls[0]
page = page + '\n\n## Unrelated section\n`InstructionsLoaded`'
reasons = successor.action_conjunct(lines, cell, line, page)
print(f'v31.action_conjunct({lines!r}, {cell!r}, {line!r}, {page!r}) -> {reasons!r}; verdict={"REJECTED" if reasons else "ACCEPTED"}')
print('legacy_E2f_2_of_2_label_in_landed_successor=' + str('E2f fresh instances reject' in (SANDBOX / 'verifiers/check_scoped_rules_v31.py').read_text()))
```

`noop_g7.py`:

```python
from pathlib import Path
import importlib.util
import sys

path = Path('/tmp/kotoba-r62-FalsifyE2fPair-20261023/sandbox/verifiers/check_scoped_rules_v31.py')
spec = importlib.util.spec_from_file_location('review_noop_g7', path)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
module.g7_conjunct = lambda *_args: []
print('in-memory mutation: g7_conjunct = lambda *_args: []; source file unchanged', flush=True)
raise SystemExit(module.main(['--self-test']))
```

## Bounds

Only this report was written in the lane. Scratch files and clone stayed under the named `/tmp` root; the frozen/product files were not changed. No subagents, background jobs, alternate orchestration/judging runtime, package transaction, installation, or update was used. Existing Python was used by the expressly assigned experiments. No C2 gate, full live-row `--fetch`, census, no-harm battery, or CriticC1Hollow catalogue-hollow laboratory was rerun here; none is claimed passed by this report. No blocker remains for the assigned review.
