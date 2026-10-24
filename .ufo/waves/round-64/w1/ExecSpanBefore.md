# ExecSpanBefore — C1 before-evidence

## Findings

C1's before-state control is evidenced at base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`: the committed verifier's self-test reports 219 assertions and exits 0. The source hash at that full base revision is `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`.

On a scratch extraction of that base under `/tmp/kotoba-r64-c1-before-078eec4a`, I applied the §11 SM1 replacement exactly: replaced the complete `span_missing` branch computation with `span_missing = []`. Its self-test also reports 219 assertions and exits 0, demonstrating that SM1 (branch removed) survives the committed before-state predicate.

**Claim supported:** C1's frozen before-evidence/control at the specified base (219 assertions; SM1 survives). This is not evidence for the post-change 223-assertion predicate or for any landed C1 implementation.

## Exact command outputs

### Base predicate

Command run with the lane as the working directory:

```text
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v32.py --self-test; rc=$?; printf 'EXIT=%s\\n' "$rc"; exit "$rc"
```

Output:

```text
counter sha256 12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
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
self-test: 0 failure(s) over 219 assertions
EXIT=0
```

### SM1 on base scratch copy

Scratch preparation was read-only against the lane repository: `git archive 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` was extracted under `/tmp/kotoba-r64-c1-before-078eec4a`. In `verifiers/check_scoped_rules_v32.py`, the entire `span_missing` comprehension (source lines 1055–1061) was replaced by the SM1 specified in `.ufo/waves/round-63/w2/MutW2V32.md` §11: `span_missing = []`.

Command run from the scratch root:

```text
python3 -B verifiers/check_scoped_rules_v32.py --self-test; rc=$?; printf 'EXIT=%s\\n' "$rc"; exit "$rc"
```

Output:

```text
counter sha256 450aa7f1ca392ef71ef5cc2e05136afe26f2c430f7a5c8f308ea981e92e61aca
world W1: Claude Code reject=True arm=A4 line='entry row S900: A4: snapshot sha256 06277eb1ae94... is already recorded by base row S010 and the teaches cell declares no supersedes'
world W2: Claude Code reject=True arm=A3 line="entry row S900: A3: URL 'https://code.claude.com/docs/de/memory.md' is a rendering alias of the committed row S112 URL 'https://code.claude.com/docs/e"
world W3: Cursor reject=True arm=A1 line="entry row S903: A1: scope key 'rules' is not a canonical key for Cursor (canonical: globs); S903 URL 'https://cursor.com/docs/rules' is already a base"
world W4: Cursor reject=True arm=live line='live page: not found'
world W5: Claude Code reject=True arm=A1 line="entry row S900: scope key 'patterns' is not a canonical key for Claude Code (canonical: paths)"
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
self-test: 0 failure(s) over 219 assertions
EXIT=0
```

### Committed-source hash

Command:

```text
git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 078eec4a1f6a41c64ff8806f58b46a67cd413bfc:verifiers/check_scoped_rules_v32.py | sha256sum
```

Output:

```text
12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43  -
GIT_SHOW_EXIT=0 SHA256SUM_EXIT=0
```

## Commit-ready receipt text

The following is the requested receipt content for `.ufo/waves/round-64/controls/C1-before.txt`. It is included here for the L1 to place; lane production files were not written by this seat.

```text
C1 before-evidence
Predicate: `python3 -B verifiers/check_scoped_rules_v32.py --self-test`
Base rev: `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`
Committed bytes: `self-test: 0 failure(s) over 219 assertions` (exit 0)
SM1 (branch removed) survives: exit 0
```

## Scope and handoff

Files changed in the lane: `.ufo/waves/round-64/w1/ExecSpanBefore.md` only. Scratch mutation files are under `/tmp/kotoba-r64-c1-before-078eec4a`; no lane production file, git index, or jj state was changed. No tools were installed. No blockers. The L1 should add the receipt text above at the requested controls path during integration.