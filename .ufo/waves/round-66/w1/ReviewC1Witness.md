# ReviewC1Witness — round 66 C1 (G9 one-word-tail floor)

Seat: reviewer (read-only). Assignment: adversarially attack the C1 witness — can a
one-content-word clause that is supported elsewhere on the page but absent at its cited line
still pass the landed `action_conjunct`? Recompute with a fresh fixture, report the exact
reason/exit, do not modify the verifier.

- Pinned base: `11385e04e368c1e94ab1a5a89d7439033eb1f855`
- Observed lane tip (git): `2a8eba56b3f9321b70c569fa2816d42237ca49a2` (worktree verifier bytes == HEAD)
- `verifiers/check_scoped_rules_v32.py` sha256 at tip = `97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def`,
  identical at `806b53b`, `9e75e73`, `fc1b71e`, `2a8eba5`; base sha256 = `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d`.
- jj `@` is `98c994b0…` (working-copy commit); all measurements here are on the git revision bytes above.

Method: read-only. Base bytes were extracted with `git archive` into `/tmp/r66c1.B5jpeW/basetree`;
the tip verifier was copied to `/tmp/r66c1.B5jpeW/tip/`. Fixtures were executed by importing the
module by path and calling `g9_conjunct` / `action_conjunct` directly; mutation probes were made only
on copies under `/tmp/r66c1.B5jpeW/mut/`. No lane file, receipt, control, counter, or claim was edited.

## Answer to the assigned question

Yes, in two distinct ways; the exact frozen witness shape itself is closed.

1. **Boundary evasion (outside the witness shape).** The same one-content-word clause with the exact
   word `exfiltrates` present only at page line 5 and absent at the cited line 2 is **admitted**
   (`action_conjunct` → `[]`, exit 0) whenever the tail is attached by anything other than `;` or
   `and`: `. `, `, `, `: `, em dash, `&`, `via`, ` then `, ` with `, ` while `. `split_clauses`
   (verifier `:1078-1120`) only splits at `;` and `\band\b`, so the tail stays inside the parent
   clause, whose 5-of-6 line coverage clears `fwd_need(6)=4`.
2. **Prefix-relation evasion (inside the witness shape).** With the exact `and` split, a one-word
   clause whose token is absent at the cited line but present elsewhere on the page is admitted when
   `supported()` (`:1035`) relates it by its first four characters to a cited-line word: line 2 carries
   `customer`, the tail word is `customs` (only at line 5) → `[]`, exit 0.
3. **The frozen witness shape is closed.** `and exfiltrates.` with no prefix relation → exit 1 with
   exactly `A2 G9: clause "exfiltrates. (S123 :2)" is supported outside the cited line`.

## Recomputed evidence (independent)

| Measurement | Base `11385e04` | Tip `2a8eba56` |
|---|---|---|
| `check_scoped_rules_v32.py --self-test` | `0 failure(s) over 234 assertions`, exit 0 | `0 failure(s) over 240 assertions`, exit 0 |
| Control fixture `g9_line + " and exfiltrates."` | `[]` (admitted) | one G9 reason (rejected) |
| Frozen lines | 7/7 worlds, 4/4 eligible rows, 6/6 survivors | same, plus the three must-fail lines |
| `check_assertion_floors.py` | — | `PASS scoped_rules_v32 observed=240 floor=240`, all 15 PASS, exit 0 |

Assertion delta is accounted for: the base arm `A2 G9: a ONE-word clause is exempt (declared bound)`
(base `:2959`, 0 occurrences at tip) is replaced by 7 new checks (tip `:2963-2997`), net +6 = 234→240.
The receipts' counts, hashes, and frozen lines reproduce exactly.

Fresh production-shaped fixture (5-line page, cited line = 2, citation `(S123 :2)`):

```
1 # Evidence snapshot
2 The archive mirrors customer invoices every night.
3
4 ## Operations
5 The agent secretly exfiltrates telemetry nightly.
```

| Cell tail | `action_conjunct` | Exit |
|---|---|---|
| ` and exfiltrates. (S123 :2)` | `['A2 G9: clause "exfiltrates. (S123 :2)" is supported outside the cited line']` | 1 |
| `; exfiltrates.` | one G9 reason | 1 |
| `. Exfiltrates. (S123 :2)` | `[]` | 0 |
| `, exfiltrates.` | `[]` | 0 |
| ` then exfiltrates.` / ` with ` / ` while ` | `[]` | 0 |
| ` and customs. (S123 :2)` (line 2 has `customer`; `customs` only line 5) | `[]` | 0 |

`plus` behaves differently only because it is a 4-letter non-stopword absent from the page
(`A2: action word(s) plus do not occur on the committed snapshot`); adding `plus` to the page flips
that cell to `[]`, exit 0 — the joiner is attacker-controlled page content.

Note on reading the exit: `action_conjunct` returning `[]` means the cell is admitted by this guard.
Under the suite's check convention (`named(..., "G9")` expected True) a period-joined version of the
frozen witness would fail the assertion (`got False, expected True`) **because the fabrication is
admitted**, not because the guard over-rejects.

## Findings

### F1 (High) — the closure headline claims a class the counter does not measure

`LOG.md:2627` states "The `clause_need(n)=min(fwd_need(n),n)` coupling closes the one-word case";
`corpus/lessons/round-66-verifier-spotcheck.md:38` states "a one-word clause on the page but off the
cited line is now rejected". Both are universal; the counter's witness is `and`-joined only. The
table above falsifies the universal reading with the exact same fabrication word and page.
`corpus/knowledge/compound-clause-citation-round63.md:102-104` already declares `but`, `while`,
commas and participles unmodelled, so the landed code is consistent with the corpus record; the
round-66 prose drops that qualifier. Under Q26 the clause "closes the one-word case" is a claim the
counter's output does not turn on.

Recommendation: bound the headline to `;`/`and`-split clauses (or drop the class-closure wording);
if the wider splitter is wanted it is the v33 contract change the r63 entry describes, not part of
this move.

### F2 (Medium) — the one-word floor of 1 counts a different token as support

Within the exact `and` witness shape, `and customs.` is admitted because `clause_need(1)=1` and
`covered({"customs"}, line_w)=1` via the `cust` prefix of `customer`. The token is absent at the
cited line and occurs only in an unrelated page section, which is the witness's stated condition in
token terms. This is a contract boundary, not a regression: the r63 entry (`:103-104`) documents the
4-character-prefix swap as an unmodelled inherent of A2's `supported()`, and the verifier's own
relation treats the word as line-supported. The defect is that the round-66 prose does not restate
the qualifier while claiming the case closed.

### F3 (Medium) — the r63 knowledge entry is stale and no correction is registered

`corpus/knowledge/compound-clause-citation-round63.md:79` still teaches "Short clauses are exempt";
`:84` still calls the one-word tail a "declared structural bound"; `:87` cites the self-test arm
"a ONE-word clause is exempt", which exists only at base (`:2959`) and has zero occurrences at tip;
`:87-88` predicts closing it would require touching A2's forward-fraction floor — falsified by the
landed clause-local `clause_need`. No correction is registered: `verifiers/check_correction_sweep.py`
has 0 rows mentioning `one-word` and 0 mentioning `clause_need`; the r66 `corpus/QUALITY.md` change
adds only Q61. Q29 requires the stale phrase and declared result in the sweep registry, and Q31
requires prose about what a counter checks to name tests its code reads (the named arm is gone).

Recommendation: append a correction notice (the lane convention, `LOG.md:2618`) and register it; do
not rewrite the r63 row in place.

### F4 (Low) — the g9 docstring's no-double-report justification is wrong for backticked clauses

The `g9_conjunct` docstring (`:~1132-1135`) says a clause absent from the page too "is already
reported by A2's page-containment check". For a backticked clause that is false: A2's
`content_words` strips backticked spans, `g9_conjunct` returns `[]`, and the actual rejector is G7.
Fixture `and \`zephyrizes\`.` → `action_conjunct` returns
`['A2 G7: backticked identifier(s) zephyrizes occur in neither the cited line nor the committed snapshot']`,
exit 1. Behaviour is safe; the prose names the wrong arm (Q31).

### F5 (Low, informational) — the coupling widens rejection of irregular-morphology continuations

Cited line "The system writes records nightly." with tail `and wrote.` returns
`['A2 G9: clause "wrote." is supported outside the cited line']` at tip and `[]` at base, because
`wrote`/`writes` share no 4-character prefix. This is consistent with A2's support relation and sits
inside the r63 "legitimate continuation rejected" bound, but it is a new false-positive class for
prose. No live cell is affected on the corpus at either revision: the offline gate output is
identical at `--rev 11385e04` and `--rev 2a8eba56` after the revision line
(`scoped rule files backed on committed snapshots 4 of 4; live not run`; the same three pre-existing
client rejects; exit 1 at both). The shared exit 1 is pre-existing, not a C1 regression.

### Mutation probes (independently executed in temp copies)

| Probe | Result |
|---|---|
| cited-line arm uses `fwd_need(len(w))` (K4 shape) | exit 1; first FAIL `A2 G9: a ONE-word clause supported by the cited line passes: got True, expected False` — matches `C1-kill.txt` K4; a second failure lands on the zero-floor must-fail arm because that arm's admission also routes through `clause_need` |
| `clause_need` capped at 2 for all n | exit 1, 3 failures (includes the `clause_need(1)=1` pin) |
| `clause_need` capped at 2 only for n≥4 | exit 1, 1 failure (`a clause absent from the page is NOT reported by G9`): the 5-word clause is 3/5 page-supported by prefix, so `fwd_need(5)=4` vs 2 flips it. n≥4 **is** pinned indirectly; the plan's "pinned at lengths 1, 2, and 3" understates coverage (harmless) |

K1/K2/K3/K5 were not individually reconstructed. K1's admission is printed by the suite itself
(`must-fail G9 uncoupled MIN_SHARED admits one-word fabrication: yes`); K2/K3/K5 follow from the same
`covered >= need` arithmetic (skip, page-floor, and zero-floor respectively). The receipt's
"first load-bearing FAIL" convention is accurate.

## Residual risk

- The one-word class remains open at any non-`;`/non-`and` boundary and for prefix-related tokens.
  Both are pre-existing, documented r63 bounds, not introduced by this diff; the risk is to the
  depth claim, not to the code's regression surface.
- A future period/comma-aware splitter will reject legitimate multi-sentence cells (the r63 C10
  bound predicts this); it should land as a declared contract change with its own controls.
- The offline gate is not a fully green baseline (three pre-existing client rejects at both revs),
  so "no live regression" is inferred from output identity, not from a green gate.

## Verification gaps

- No `lsp` device is available in this seat's toolset (`read`, `bash`, `edit`, `eval`, `glob`,
  `grep`, `task`, `wait`, `web_search`, `write`, plus `xd://ast_edit` / `xd://debug`). Caller
  inventory was therefore taken by text search (`action_conjunct` definition `:1155`, sole production
  caller `:1559`, self-test arms `:2098-2275`, `:2884-3022`) and then proven by executing the module;
  the text search is recorded as the fallback, not as semantic proof. No language server answered or
  was configured for this single-file Python instrument.
- Live (`--fetch`) path not run; only the offline `--rev` gate at the two revisions.
- K2/K3/K5 mutants not individually reconstructed (K4, all-n cap-2, and n≥4 cap-2 were).
- C2 and every non-C1 item were not reviewed (out of this seat's scope).

Temp sandboxes retained at `/tmp/r66c1.B5jpeW/` (base tree, tip copy, three mutant dirs, gate
outputs) for reproduction. Only this report was written into the lane.
