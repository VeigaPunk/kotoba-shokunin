# Adjudication ledger — round-37 C1 (template)

Fill one block per row. A row without a probe command + raw output is not a
ruling (protocol §5). Never edit a settled row: supersede with a numbered erratum
row. `pin` is ledger-only — builders must not be shown this file (protocol §6).

```yaml
- row: adj-r37-01
  checks: [omp.offered.skills]          # one or more ids; or "mutant:<name>"; or "class-level"
  class: D1|D2|D3|D4|D5|D6|D7|U
  readings: {ind: <value>, har: <value>, pin: <value>, hand: <value>}
  probe: "command → raw output (saved at drafts/<seat>/probe-01.txt)"
  ruling: defect(author)|defect(independent)|definitional|bookkeeping|cosmetic|
          shared-property|correction|unresolved
  authority: hand-substrate|spec-sentence|observed-behaviour
  action: "code fix path | baseline/doc note path | fixture path | none"
  blind: outputs-only|source-read(author)|source-read(builder)|none
  status: settled|superseded-by:adj-r37-NN|unresolved
```

Required fields per class:

| class | additionally required |
|---|---|
| D1 | losing side + exact line; red-before fixture path; live delta |
| D2 | both scopes' probe blocks; exact scope wording landed where the number is compared |
| D3 | the claim sentence vs the behaviour; fixture (carries proof when delta 0) |
| D4 | the population and its measured delta (0 must be stated); why naming beats silence |
| D5 | the sum/identity that proves the two readings are the same population |
| D6 | the detector that does notice; the safe invocation adopted |
| D7 | the false premise; the predecessor sentence's status (complete/incomplete) |
| U | both readings; the discriminator that would settle it; probes attempted (≤2) |

Agreement line (report §1, not smoothed):
`IND agrees N/28 (equal a/17, zero b/10, positive c/1); adjudicated rows: k
(definitional d, bookkeeping e, cosmetic f, defects g, shared-property h,
correction i, unresolved j).`