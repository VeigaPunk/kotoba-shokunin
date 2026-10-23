# ExecSuccessor31

## Files and hashes

- Created `verifiers/check_scoped_rules_v31.py` by copying the frozen counter, then adding the assigned E2c, E2e, and G7 guards plus self-test cases. The original `verifiers/check_scoped_rules.py` was not edited.
- Original hash observed before the copy, command `sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py && wc -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py`:
  `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`.
- Hashes after the edits, command `sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py`:
  ```
  5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
  a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules_v31.py
  ```
  The baseline copy was made directly from the original before editing; no pre-edit hash of the copy was captured. The original's pinned hash was observed unchanged before and after the edits.

## Verification status

Per the fleet-executor instruction to skip tests while the editing wave is in flight, I did not run either requested Python command. Therefore there is no observed exact self-test stdout/exit, no observed must-fail output, and no measured worlds/eligible line. Parent post-integration verification is required; I have not claimed green.

The implementation's expected (unexecuted, **[INFERENCE]**) worlds/eligible line is `worlds reject 7 of 7; eligible rows pass 4 of 4`. Its self-test loads the six survivor fixtures from `check_erratum_absorption.py` only inside the `--self-test` path and prints the per-id verdicts, computed `survivors closed N of 6`, two guard-mutation lines, and the G9 bound.

Requested fetch command, not run: `python3 -B verifiers/check_scoped_rules_v31.py --rev 43fe0180 --fetch`. **[INFERENCE]** `43fe0180` is not the frozen counter's required 40-hex revision, so this argument is rejected before any network fetch; the requested invocation should be clarified or supplied as a full hash by the parent.

## Six survivor verdicts

The `before` acceptances are from the assignment's supplied round-62 measurements, not a rerun here. `after` outcomes below are **[INFERENCE]** from the implemented guards and still require the parent self-test to measure.

| ID | Before | Successor after (inferred) |
|---|---|---|
| `e2c-wrong-supersedes-target` | accepted (`[]`) | rejected: declared `S096` differs from base owner `S043` |
| `e2c-supersedes-with-fresh-fetch` | accepted (`[]`) | rejected: matching `supersedes` also asserts a fetched ISO timestamp |
| `e2e-negated-path-key` | accepted | rejected: negation before the key occurrence invalidates the key site |
| `e2e-commented-equals-key` | accepted | rejected: comment occurrence is excluded and equals form is not key form |
| `e2f-backticked-event-claim` | accepted (`[]`) | rejected: `InstructionsLoaded` is absent from raw cited line and page |
| `e2f-compound-purpose-outside-citation` | accepted | remains accepted as the declared G9 bound |

Expected but unexecuted self-test lines (**[INFERENCE]**, not observed):

```
survivors closed 5 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
bound: G9 remains unimplemented; e2f-compound-purpose-outside-citation survives per CriticC1Hollow.
```

G9 was intentionally not implemented: `CriticC1Hollow` forbids implementing it contrary to the declared surviving bound. No tools were installed.
