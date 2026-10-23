# FalsifyV31G9 — compound-purpose surviving bound

Axis attacked: **depth**. Secondary exposure: consistency of the counter, ledger and registry. This is scoped critic evidence, not admission, integration or a canonical judgment.

## Finding and smallest safe correction

**The attempted falsification did not reproduce.** The exact frozen `e2f-compound-purpose-outside-citation` input remains ACCEPT under the committed successor. The other survivor verdicts and their actual reason lists are pasted below; no claim of class-wide semantic closure follows from them.

The fresh successor run printed exactly:

```text
survivors closed 5 of 6
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
```

Both lines come from the `--self-test` command, with its exit status, in § Counter runs below. The compound-purpose acceptance is a disclosed limitation, not a contradiction of the bound claim. **Smallest safe correction: none to this scoped claim.** Preserve the named bound; do not promote the measured closure line into complete E2f/G9 closure. No lane product changes were made.

## Frozen evidence and execution boundary

Reviewed committed revision: `e6da78bbe420722dd18a13182a7c4b64ce02f005`. Read `plans/round-62.md` first, including its E1 addenda: the successor is separate fix evidence and anything it cannot close remains a named bound. All counter executions used committed source extracted under `/tmp/kotoba62-FalsifyV31G9-ihmpqbnk`, with `cwd` and `TMPDIR` there and `PYTHONDONTWRITEBYTECODE=1`. Self-test git repositories were therefore outside the lane. Extraction used read-only `git show`; the hashes below were computed using `hashlib.sha256` over each command's returned bytes, not working-tree imports.

```text
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_scoped_rules.py
exit=0
sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91 verifiers/check_scoped_rules.py
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_erratum_absorption.py
exit=0
sha256 afb4ff74c266803f4d6007407775a5c44387c84bf49b9ac1a9059d375178d56b verifiers/check_erratum_absorption.py
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:verifiers/check_scoped_rules_v31.py
exit=0
sha256 a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858 verifiers/check_scoped_rules_v31.py
```

The following claim documents were also extracted from the same revision using `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:<path>` (each exit=0), then inspected under the sandbox's `pinned-docs/` directory: `SKILL.md`, `LOG.md`, `SCORECARD.md`, and `corpus/knowledge/erratum-absorption-round62.md`. This avoids attributing concurrent working-tree prose corrections to the reviewed revision.

## Counter runs — exact stdout and exit status

```text
$ python3 -B /tmp/kotoba62-FalsifyV31G9-ihmpqbnk/verifiers/check_erratum_absorption.py --self-test
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
exit=0

$ python3 -B /tmp/kotoba62-FalsifyV31G9-ihmpqbnk/verifiers/check_scoped_rules_v31.py --self-test
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
exit=0
```

## Strongest counterexample attempted

I did not rely only on the successor's self-test assertions. The scratch probe independently imported the extracted instrument and successor, selected the attacks actually accepted by the frozen counter, and called each attack's `.score(v31)` directly. It separately transcribed the compound-purpose line, cell and page as literals and called `action_conjunct` and `g7_conjunct`.

I then tried the guard-intersection hypothesis: place the unchanged compound-purpose action inside a complete entry-row input with a valid colon-form scope key, a matching repeated-snapshot `supersedes S043` exemption, a located rule-file quote, matching snapshot hash and eligible recorded introduction dates. This makes the new E2c and E2e guards actually execute alongside G7. The trace below records their real return values; the row still accepts. Disabling each combination of the new guards likewise leaves the exact catalogue input accepted.

Contrasts were kept separate from the original attack: negating the scope key, changing the supersedes target, or adding an absent backticked identifier rejects the row for the corresponding newly introduced fault. Removing the unrelated section rejects for the pre-existing whole-page word-support test. None is evidence that the unchanged G9 input is rejected. Backticking the existing side-clause words also does not close the purpose gap because those words already occur elsewhere on the page.

The counting command and exact probe output follow. The script is scratch investigation material, not a lane verifier.

```text
$ python3 -B /tmp/kotoba62-FalsifyV31G9-ihmpqbnk/g9-probe.py
== Six survivor inputs, scored directly ==
e2c-wrong-supersedes-target: REJECT ['A4: supersedes target S096 differs from base row S043 that owns the snapshot sha256']
e2c-supersedes-with-fresh-fetch: REJECT ['A4: supersedes S048 declares byte identity but the teaches cell also asserts a fetched ISO timestamp']
e2e-negated-path-key: REJECT ["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
e2e-commented-equals-key: REJECT ["A1: scope key 'paths' is not in key form with a path-like glob at line 1"]
e2f-backticked-event-claim: REJECT ['A2 G7: backticked identifier(s) InstructionsLoaded occur in neither the cited line nor the committed snapshot']
e2f-compound-purpose-outside-citation: ACCEPT []
== Independently transcribed G9 input ==
line='The configuration stores project rules using glob syntax.'
cell='The configuration stores project rules using glob syntax and secretly uploads files.'
page='The configuration stores project rules using glob syntax.\n\n## Unrelated section\nThe agent secretly uploads files.'
literal action_conjunct: []
cell words: ['configuration', 'files', 'glob', 'project', 'rules', 'secretly', 'stores', 'syntax', 'uploads', 'using']
cited-line words: ['configuration', 'glob', 'project', 'rules', 'stores', 'syntax', 'using']
forward: 7 of 10; need 7
reverse: 7 of 7; need 3
page words missing: []
G7 raw identifier matches: []
G7 direct verdict: []
== Cross-guard disable grid on unchanged G9 input ==
disabled E2e=0 E2c=0 G7=0: ACCEPT []
disabled E2e=0 E2c=0 G7=1: ACCEPT []
disabled E2e=0 E2c=1 G7=0: ACCEPT []
disabled E2e=0 E2c=1 G7=1: ACCEPT []
disabled E2e=1 E2c=0 G7=0: ACCEPT []
disabled E2e=1 E2c=0 G7=1: ACCEPT []
disabled E2e=1 E2c=1 G7=0: ACCEPT []
disabled E2e=1 E2c=1 G7=1: ACCEPT []
== Full entry-row guard intersection, unchanged G9 action ==
full row with valid key + valid repeated-sha exemption: []
alias_sha_why: input='supersedes S043 — byte identity'; result=[]
key_site_guard: input='paths: src/api/**/*.ts'; result=True
g7_conjunct: input=[]; result=[]
full row with negated scope key: ["snapshot .ufo/waves/round-60/snapshots/S900.page: A1: scope key 'paths' is not in key form with a path-like glob at line 6"]
full row with wrong supersedes target: ['A4: supersedes target S096 differs from base row S043 that owns the snapshot sha256']
full row with added missing identifier: ['snapshot .ufo/waves/round-60/snapshots/S900.page: A2 G7: backticked identifier(s) InventedEvent occur in neither the cited line nor the committed snapshot']
== Input-change contrasts, not the original survivor ==
remove unrelated page section: ['A2: action word(s) files, secretly, uploads do not occur on the committed snapshot']
backtick existing side-clause words: []
unchanged original after all probes: []
exit=0
```

### Why the new guards do not close this input

- `verifiers/check_scoped_rules_v31.py:1061-1088`: the action retains fraction-based support and whole-page presence checks, then calls G7. The support counts printed by the probe satisfy both thresholds; the unsupported-at-citation side-clause words are present in the unrelated page section.
- `:1046-1058`: G7 only enumerates `BACKTICKED_IDENTIFIER_RE` matches. The original action has none, as independently printed by the probe. Its direct G7 result is empty; it has no compound-purpose entailment test.
- `:975-996,1101-1115`: E2e guards key occurrences, not the action's purpose. The full-row trace demonstrates that a valid scope key does not reject the compound action.
- `:1236-1254`: E2c binds the supersedes target to the full-hash owner and rejects a fresh-fetch assertion. A correctly bound exemption returns no reason even when the separate action contains the G9 side clause.
- `:2571-2586,2611-2615`: the successor computes its closure count from actual reason lists and separately asserts that this named G9 reason list remains empty. The direct probe agrees, rather than merely trusting those expectations.

## Claims, ledger and registry

At the reviewed revision, `corpus/knowledge/erratum-absorption-round62.md:39` states:

> **F6 / G9:** compound-purpose claims remain outside the successor's frozen guard; the named E2f compound-purpose instance remains a declared bound.

The entry's successor paragraph (`:35`), `LOG.md:2550-2551`, `SKILL.md:486,490`, and `SCORECARD.md:36,371` retain this residual rather than claiming compound-purpose closure. The successor's registry row is explicitly a **gate**, separate from the frozen counter; there is no capability promotion in that row. The direct run supports this scoped disclosure. It does not establish that all other shapes of E2c/E2e/G7 are closed, that purpose entailment is measured, or that any score band should move.

## S118 reopened

Opened https://code.claude.com/docs/en/memory.md independently. Its Rule frontmatter reference still describes `paths` with the located text `Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string`. The committed snapshot locator is `.ufo/waves/round-62/snapshots/S118.page:250`; `corpus/SOURCES.md:129` labels this vendor documentation, not a runtime test. It supports the E2e form and supplies no basis to reclassify the G9 action as rejected.

The following summaries were computed from the respective commands' raw stdout bytes; the curl write-out suffix was separated before hashing its body. The literal fetched body was also compared with the committed snapshot.

```text
$ git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show e6da78bbe420722dd18a13182a7c4b64ce02f005:.ufo/waves/round-62/snapshots/S118.page
exit=0
bytes=55354
sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
$ curl -sSL --max-time 60 --connect-timeout 15 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -H 'Accept: text/markdown, text/plain;q=0.9, */*;q=0.8' -w '
%{http_code} %{url_effective}' https://code.claude.com/docs/en/memory.md
200 https://code.claude.com/docs/en/memory.md
exit=0
bytes=55354
sha256=02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801
matches committed snapshot=True
```

## Scope and tooling

No subagents, background jobs, model calls, runtime judgments, package transactions, installs or updates were used. Only this report was written inside the lane; scratch extraction and probes stayed under `/tmp`. This seat exercised the absorption self-test, successor self-test, direct survivor/guard-intersection probes and S118 fetch shown above. It did not rerun the routed-repairs successor, census, live-row CLI fetches or general no-harm battery, and does not claim they passed.
