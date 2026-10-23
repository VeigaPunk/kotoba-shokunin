# ExecV32SelfTest
role: executor — scoped self-test block proposal
item: ExecV32SelfTest; C1/G9 self-test only

## Findings
1. `Read plans/round-63.md:43-49` freezes the self-test requirement: print `worlds reject 7 of 7; eligible rows pass 4 of 4`, then `survivors closed 6 of 6`, then `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes`, and exit 0.
2. `Read verifiers/check_scoped_rules_v31.py:2577-2615` shows the requested replacement span: five `True` values followed by `False`, computed survivor output/count, E2e and G7 mutation arms, and the old declared-G9-bound output. `sha256sum verifiers/check_scoped_rules_v31.py` returned `a07c2269ea077e4866827e3fae907c45aea7c960bbe5f56b21210a0cecea3858`, matching the frozen source prefix in the plan.
3. `Read verifiers/check_scoped_rules_v32.py:1098-1100,1129-1132,1157-1158` shows `action_conjunct` calls `g9_conjunct`; replacing that module attribute during the attack rescore exercises the G9 guard. At read time, `verifiers/check_scoped_rules_v32.py:2647-2685` still had the five-True/one-False expectation and declared-bound arm.
4. No LSP interface was exposed in this session's tool inventory. The symbol definition and dispatch were checked directly in the source; no empty/cold LSP response was treated as absence.
5. I did not run `--self-test` or another check; wave instructions reserve verification for the parent.

## Artifacts
Replacement for `verifiers/check_scoped_rules_v32.py` lines 2577-2615, copied from the v31 shape with the G9 closure and guard mutation:

```python
        expected_after = (True, True, True, True, True, True)
        check("successor rejects all six frozen survivors",
              tuple(bool(after[ident]) for ident in survivor_ids), expected_after)
        for ident in survivor_ids:
            print("survivor %s: before %s; after %s" %
                  (ident, "rejected" if before[ident] else "accepted",
                   "rejected" if after[ident] else "accepted"))
        survivors_closed = sum(1 for ident in survivor_ids
                               if not before[ident] and after[ident])
        print("survivors closed %d of 6" % survivors_closed)

        negated_id = "e2e-negated-path-key"
        saved_key_guard = current_counter.key_site_guard
        try:
            current_counter.key_site_guard = lambda _line, _position: True
            negated_admitted = not attacks[negated_id].score(current_counter)
        finally:
            current_counter.key_site_guard = saved_key_guard
        check("must-fail E2e guard mutation admits the negated-path survivor",
              negated_admitted, True)
        print("must-fail E2e guard disabled admits %s: %s" %
              (negated_id, "yes" if negated_admitted else "no"))

        backticked_id = "e2f-backticked-event-claim"
        saved_g7 = current_counter.g7_conjunct
        try:
            current_counter.g7_conjunct = lambda *_args: []
            backticked_admitted = not attacks[backticked_id].score(current_counter)
        finally:
            current_counter.g7_conjunct = saved_g7
        check("must-fail G7 mutation admits the backticked-event survivor",
              backticked_admitted, True)
        print("must-fail G7 disabled admits %s: %s" %
              (backticked_id, "yes" if backticked_admitted else "no"))
        g9_id = "e2f-compound-purpose-outside-citation"
        saved_g9 = current_counter.g9_conjunct
        try:
            current_counter.g9_conjunct = lambda *_args: []
            g9_admitted = not attacks[g9_id].score(current_counter)
        finally:
            current_counter.g9_conjunct = saved_g9
        check("must-fail G9 mutation admits the compound-purpose survivor",
              g9_admitted, True)
        print("must-fail G9 disabled admits %s: %s" %
              (g9_id, "yes" if g9_admitted else "no"))
```

Exact replacement boundaries and three lines of unchanged context on each side, from v31:

```text
Before (lines 2574-2576):
                  for ident in survivor_ids}
        check("all six frozen survivors were accepted by the r61 counter",
              tuple(not before[ident] for ident in survivor_ids), (True,) * 6)

Replace lines 2577-2615 with the fenced Python block above.

After (lines 2616-2618):
        # -- the counter's own sha256 (v2) --------------------------------
        own = Path(__file__).read_bytes()
        check("the own sha256 is 64 hex", len(self_sha()), 64)
```

## Verdict
PROPOSES — use this replacement span in v32. I would change my mind if the parent-run self-test fails to compute 6/6 or the G9-disabled rescore does not admit the named survivor; neither result was exercised in this wave.
