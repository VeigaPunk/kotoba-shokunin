# ExecReceiptTemplates — round 64 wave 1

## Deliverable and refresh rule

No receipt/control production file was written; this seat's only write is this report. The four requested receipt bodies below are byte-level templates for L1 integration at these absolute paths:

- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/receipts/C1-span-measure.txt`
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/receipts/C2-r64-measure.txt`
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/controls/C1-before.txt`
- `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/controls/C2-before.txt`

**C1 refresh rule:** do not rewrite, replace, or refresh any round-63 receipt. Those receipts remain true at their named historical revisions. Round 64 adds the new `C1-span-measure.txt` and `controls/C1-before.txt` files; it does not update `.ufo/waves/round-63/receipts/C1-g9-measure.txt` or another r63 receipt. This rule applies even though C1's G7 arms add four assertions in round 64.

Every template retains literal `measured rev: <REV>` and `counter sha256 <SHA256>` placeholders as requested. C1-span's stdout is the frozen 223-assertion signature with unchanged pre-existing output lines; that unchanged-line detail is **[INFERENCE]** from the frozen plan's expected result. C1-before's baseline output is retained below from the existing before-evidence report. C2 bodies include only the exact summary output lines in the frozen predicate; they are templates, not claimed executions.

## Exact receipt bodies

### `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/receipts/C1-span-measure.txt`

```text
# Frozen predicate (verbatim from plans/round-64.md):
# `python3 -B verifiers/check_scoped_rules_v32.py --self-test`
# prints all four lines —
# worlds reject 7 of 7; eligible rows pass 4 of 4
# survivors closed 6 of 6
# must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
# self-test: 0 failure(s) over 223 assertions
# — and exits 0.
command: python3 -B verifiers/check_scoped_rules_v32.py --self-test
measured rev: <REV>
counter sha256 <SHA256>
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
self-test: 0 failure(s) over 223 assertions
exit=0
```

### `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/receipts/C2-r64-measure.txt`

```text
# Frozen predicate (verbatim from plans/round-64.md):
# `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>`
# prints `r63 routed defects closed 4 of 4` and exits 0, AND
# `python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc`
# prints `r63 routed defects closed 0 of 4` and exits nonzero.
command: python3 -B verifiers/check_r64_routed_repairs.py --rev <REV>
measured rev: <REV>
counter sha256 <SHA256>
r63 routed defects closed 4 of 4
exit=0
```

### `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/controls/C1-before.txt`

```text
# Frozen predicate (verbatim from plans/round-64.md):
# `python3 -B verifiers/check_scoped_rules_v32.py --self-test`
# prints all four lines —
# worlds reject 7 of 7; eligible rows pass 4 of 4
# survivors closed 6 of 6
# must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
# self-test: 0 failure(s) over 223 assertions
# — and exits 0.
command: python3 -B verifiers/check_scoped_rules_v32.py --self-test
measured rev: <REV>
counter sha256 <SHA256>
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
self-test: 0 failure(s) over 219 assertions
exit=0
```

### `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-64/controls/C2-before.txt`

```text
# Frozen predicate (verbatim from plans/round-64.md):
# `python3 -B verifiers/check_r64_routed_repairs.py --rev <rev>`
# prints `r63 routed defects closed 4 of 4` and exits 0, AND
# `python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc`
# prints `r63 routed defects closed 0 of 4` and exits nonzero.
command: python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
measured rev: <REV>
counter sha256 <SHA256>
r63 routed defects closed 0 of 4
exit=1
```

## Evidence retained; claims and limits

- **C1 predicate / C1 postcondition (plan §C1):** `plans/round-64.md` lines 44–59 freezes the command, all four predicate output lines, and exit 0. Lines 71–83 declare the expected 223-assertion result and the base control's 219 assertions. ExecSpanArms reports a scratch run of `python3 -B verifiers/check_scoped_rules_v32.py --self-test` from `/tmp/kotoba-r64-c1/work`, with `self-test: 0 failure(s) over 223 assertions`, `EXIT=0`, and no dedicated stdout from the four arms. This is not a measurement at the receipt's future named revision; I did not execute the command.
- **C1 before-state:** read `.ufo/waves/round-64/w1/ExecSpanBefore.md` lines 13–45. That report retains the command and exact output of its base run, including `self-test: 0 failure(s) over 219 assertions` and `EXIT=0`; its reported counter hash is `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`. The C1-before template carries the 219 line and exit 0, while its revision/hash remain placeholders as requested. This seat did not rerun the command.
- **C1 receipt discipline:** read `.ufo/waves/round-63/receipts/C1-g9-measure.txt`; its output order and exact lines were reused, with the frozen assertion tally adjusted only in C1-span's template. The named r63 receipt itself is not to be edited.
- **C2 predicate / C2 control (plan §C2):** `plans/round-64.md` lines 102–118 define both conjuncts; lines 147–151 declare `4 of 4`/exit 0 for the r64 measured tip and `0 of 4`/exit 1 at base. The C2 outputs above are those frozen required signatures, not observed counter runs. `.ufo/waves/round-64/w1/ExecCalibVerify.md` lines 62–80 records only an existing r63 counter self-test, not an r64 predicate run.
- No tool was installed or updated. No build, lint, formatter, test, or counter command was run by this seat. No verification result is claimed.

## Risks / blockers

C1's 223-assertion receipt and C2's two r64-counter receipts remain unmeasured at their named revisions; ExecSpanArms reports a matching scratch C1 self-test, but it does not replace the landed-revision receipt. The C2 counter's detailed per-check stdout was not available in the frozen predicate; these templates therefore retain only the exact required summary line(s) and exit code rather than inventing per-check details. No other blocker.