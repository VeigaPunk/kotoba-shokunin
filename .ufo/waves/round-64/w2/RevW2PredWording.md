# RevW2PredWording — round 64 wave 2: predicate wording across plan / receipt / SCORECARD

Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Data/integration tip `c019919c97ab5fe98e87a7754b4449ea4e699c99`
(base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`), HEAD `b99fb79c27042e0f8a598cbbb4d81479a806b518`.
Measured 2026-10-24. Read-only: no lane file, index, or jj state touched; scratch only in `/tmp`. I wrote only this report.
No tools installed. `git status` showed `M .ufo/waves/round-64/receipts/noharm-tip.txt` before I started — not mine,
not touched.

**Topology correction to the assignment premise (verified).** The C1/C2 receipts and the round-64 SCORECARD
annotation are **not** at `c019919c`; they land at `b99fb79`.
`git ls-tree -r --name-only c019919c -- .ufo/waves/round-64/receipts` → empty (only `controls/C1-before.txt`,
`controls/C2-before.txt` exist there); `git show c019919c:SCORECARD.md | grep -c 'Round 64'` → 0. So "receipts at
c019919c" means *measured against* that rev, committed one commit later.

**Method note.** This seat's tool inventory has no `lsp` device, so no server-backed `references`/`definition`/
`diagnostics` pass was possible; the sites are Markdown prose plus two Python counters, compared with `grep`,
`read` line ranges, `git show`, and live re-runs. Counter semantics were checked in code, not inferred from prose.

## Verdict

Both counted predicates **hold** at the measured rev, but the claim that they are "the same sentence" in all
sites is **false for both C1 and C2**. Six material drifts plus two low-severity traceability/naming defects.
No score inflation found; the largest defect is a false exemption clause inside the C1 kill conjunct.

## Findings

### F1 — HIGH — C1 kill conjunct: the SM6 exemption is false, and the credit rule is paraphrased away
Plan `plans/round-64.md:313-316` (E3.1):

> kill conjunct holds: each of SM1–SM6 scores exit 1 on the landed bytes with its own discriminating FAIL label —
> an arm is credited only when its own `check()` label is the FAIL line (the kotodama R64-M9 lesson via
> `ConnSibling`: SM4/SM6 are red on pre-existing `eligible world` arms and are not new-arm pins).

SCORECARD.md:375:

> AND the kill conjunct holds (SM1–SM6 each exit 1 on the landed bytes with arm-attributed FAIL lines; SM4/SM6 via
> the pre-existing `eligible world` arms — the kotodama R64-M9 attribution rule)

LOG.md:2602 repeats "arm-attributed FAIL lines (SM4/SM6 by the pre-existing `eligible world` arms; attribution per
the kotodama R64-M9 rule via `ConnSibling`)".

Two independent defects:

1. **Drift:** "with its own discriminating FAIL label" ≠ "with arm-attributed FAIL lines". The plan's operative
   rule — *an arm is credited only when its own `check()` label is the FAIL line* — is present in no other site.
   "arm-attributed" is weaker and admits exactly the pre-existing-arm kills the plan's rule excludes.
2. **Falsity:** SM6 is a new-arm pin on the landed bytes. `C1-span-kill.txt` already shows two FAIL lines for
   SM6, the second being arm 2's own label:
   `SM6_branch_always_fires: exit=1 | FAIL A2: ... ; FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False`.
   The receipt quotes no `eligible world` line for SM6. My independent reproduction on the landed file
   (HEAD tree, `check_scoped_rules_v32.py` unchanged since `c019919c`, sha `f8f69cad…`), mutation
   `if span_missing:` → `if True:` at line 1065:

   ```
   $ cd /tmp/r64head && python3 -B verifiers/check_scoped_rules_v32.py --self-test
   SM6_EXIT=1
   self-test: 10 failure(s) over 223 assertions
   FAIL A2 G7: a backticked span made only of stopwords is not rejected: got True, expected False     (arm 2)
   FAIL A2 G7: a backticked span word shorter than four characters is not rejected: ...              (arm 3)
   FAIL A2 G7: a backticked span word present in the cited line is not rejected ...                  (arm 4)
   FAIL eligible world: ... (5 lines)
   FAIL must-fail G9 mutation admits the compound-purpose survivor: got False, expected True
   ```

   That is arms 2, 3 and 4 failing with their own labels — under the plan's own credit rule SM6 **is** a
   new-arm pin. Both the plan's "SM4/SM6 … are not new-arm pins" and the SCORECARD's "SM4/SM6 via the
   pre-existing `eligible world` arms" are wrong for SM6 (SM4 is correct: its five FAIL lines are all
   pre-existing `eligible world`/predicate-line arms, per `MutSpanArms.md:185-192`).
   This matches wave-1 `MutSpanArms.md:131` ("SM6 … 10 failures / 223 … worlds + arms 2,3,4") and its
   attribution map `:308-309` ("SM6←world lines + arms 2–4") — the contradiction is in wave-1's own artifacts,
   not new data. The kill receipt truncates SM6 to two lines, which is why the receipt alone does not show it.

### F2 — MEDIUM — C2 refuse rule: the plan's frozen sentence states the rule its own erratum withdraws
Plan `plans/round-64.md:115-118`:

> and the counter refuses to certify any revision while the control is green (the E2 discipline of
> `check_r63_routed_repairs.py`).

Plan E2.5 (`:283-289`) names that exact r63 rule as insufficient — a vacuous counter "prints `1 of 4` at base
… and `4 of 4` at target, passing both conjuncts" — and replaces it with "refuses to certify any revision
unless the pinned base scores exactly `0 of 4`". SCORECARD.md:375 uses "the refuse-unless-`base_closed == 0`
rule"; LOG.md:2603 uses "unless the control scores exactly `0 of 4` (erratum E2.5)". Implemented rule verified
in `verifiers/check_r64_routed_repairs.py:386-397` (`if base_closed != 0: … return 1`).
So plan 115 states the **weaker, withdrawn** rule as part of the frozen predicate; SCORECARD and LOG state the
hardened one. Three sites, three different sentences; only two carry the rule the code enforces.

### F3 — MEDIUM — C2 pinned-base clause is self-contradictory in the plan and absent from SCORECARD
Plan `:110-116` makes the control conjunct literally
`python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc`, then says:

> The second conjunct is the do-nothing control; its revision is pinned in code as BASE_REV, never a
> command-line argument …

The base revision *is* a command-line argument in that very conjunct. SCORECARD restates only
"`--rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc` → `0 of 4`, exit nonzero" and drops the pinned-in-code clause
entirely; LOG.md:2603 patches the gap with a clause found in neither site — "(argparse rejects `--base` rc 2)".
Verified: `BASE_REV_LITERAL`/`BASE_REV` at counter lines 35-36; argparse accepts only `--rev/--root/--self-test`;
`--base 078eec4` → rc 2; `--rev <BASE_REV>` prints `0 of 4` then refuses via the `rev.lower() == BASE_REV`
branch (lines 404-407, exit 1). Semantics are sound; the plan's sentence as worded is false and the
SCORECARD/LOG do not state the same clause.

### F4 — MEDIUM — C2 receipt site records neither exit clause; the receipt is an unattributed splice
The frozen predicate's two conjuncts both include exit status ("and exits 0", "and exits nonzero"). The receipt
site carries neither:

```
$ for f in .ufo/waves/round-64/receipts/C2-r64-measure.txt .ufo/waves/round-64/controls/C2-before.txt; do
    printf "%s: " "$f"; grep -ci 'exit\|Command:' "$f"; done
.ufo/waves/round-64/receipts/C2-r64-measure.txt: 0
.ufo/waves/round-64/controls/C2-before.txt: 0
```

`C2-r64-measure.txt` is 7 lines: 4 `PASS` lines, `r63 routed defects closed 4 of 4`, `counter sha256: 8f5b9f91…`,
`self-test: 0 failure(s) over 32 assertions`. A `--rev` run prints **only** the 4 PASS lines + summary
(my run: 5 lines, no sha line, no self-test line), so the receipt splices at least two runs and records neither
command. The SCORECARD's "exit 0"/"exit nonzero" clauses therefore have no receipt backing — the C1 receipt by
contrast is verbatim (see Verified below). I independently confirm both exit statuses are true
(`EXIT=0` at `c019919c`; `EXIT=1` at `078eec4`), so this is an evidence-chain defect, not a false claim — and it
is the lane's own M95 citation class, one site outside the four counted checks.

### F5 — MEDIUM — C1 "same wording in … counter label" names a label that does not exist
Plan `:44` says "same wording in plan, counter label and receipt"; E3.1 `:307-308` says "same in plan, receipt and
SCORECARD" for the same sentence. No counter label carries the round-64 predicate:
`grep -c 223 verifiers/check_scoped_rules_v32.py` → 0, and the only literal is the round-60 v2 sentence —
`PREDICATE_LINE = "worlds reject 7 of 7; eligible rows pass 4 of 4"` (line 321) plus `RECEIPT` (322-324) naming
`check_scoped_rules.py`, `BASE61`, `--fetch`; the docstring "THE FROZEN PREDICATE" (lines 49-58) is that same v2
sentence. So the plan names two different triples, and the named counter label is a *different predicate*. If
"counter label" means the printed lines, the four lines do match byte-exactly (verified) — but neither added
conjunct (sha pair, kill) is printed by the counter, so the identity claim still cannot cover the counted
sentence.

### F6 — LOW — receipts absent at the claimed measurement rev; LOG forward-references them
`git ls-tree -r --name-only c019919c -- .ufo/waves/round-64/receipts` → empty. LOG.md:2610, committed **at**
`c019919c`, lists `C1-span-measure.txt`, `C1-span-kill.txt`, `C2-r64-measure.txt`; those paths are dead at that
rev and appear at `b99fb79`. SCORECARD:375 cites them while claiming "measured @ `c019919c…`". Honest as a
later-recorded measurement of that rev, but the citations do not resolve at the rev they annotate (the M95
citation class again).

### F7 — LOW — C2 heading inverts the axis names
`plans/round-64.md:89` — "### C2 — calibration (consistency sub-axis)" — while the plan's own opening says
"depth + consistency (calibration sub-axis)" and SCORECARD:29/375 name the owned 10-scored axis
"consistency (calibration sub-axis)". SCORECARD also carries a separate advisory axis
"calibration (advisory) | 8.5". The C2 heading therefore names the advisory 8.5 axis as the claim's axis. The
counter's check 3 (which passes) requires depth 9 < consistency 10; naming the axis "calibration" in the claim
heading can misroute a closure judgment on which axis holds 10.

## Verified true (re-run, not cited)

- C1 predicate at the landed bytes: `python3 -B verifiers/check_scoped_rules_v32.py --self-test` → `C1_EXIT=0`,
  `self-test: 0 failure(s) over 223 assertions`; `sha256sum` = `f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d`,
  equal to `git show c019919c:verifiers/check_scoped_rules_v32.py | sha256sum` and to both receipt lines.
- The four frozen lines are **byte-identical** in `plans/round-64.md` (one occurrence each), `C1-span-measure.txt`
  (one each) and live output (one each). The receipt is a verbatim transcript: `diff` of receipt[2:] vs live output
  adds only `exit=0` and the repeated `counter sha256:` line.
- Base control: `git archive 078eec4` → run → `self-test: 0 failure(s) over 219 assertions`, exit 0, v32 sha
  `12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43` (matches `C1-before.txt`).
- C2 predicate: `--rev c019919c…` → `r63 routed defects closed 4 of 4`, `EXIT=0`; `--rev 078eec4…` →
  `0 of 4` + refusal line, `EXIT=1`; `--self-test` → `0 failure(s) over 32 assertions`, `ST_EXIT=0`;
  counter sha `8f5b9f91…` = receipt = `git show c019919c:…`. `--base` → rc 2.
- SM6 mutant: exit 1, 10 failures, arms 2/3/4 labels (F1).

## Residual risk / verification gaps

- SM1–SM5 were not re-run in this seat (time-box). Their exit-1 statuses are receipt- and `MutSpanArms`-cited;
  only SM6 was independently reproduced (it is the one the exemption clause is wrong about).
- The base "§11 evasion cell ADMITTED through `judge()`" claim was not re-measured; it is cited from
  `C1-before.txt`/`CriticC1Bound`.
- The C2 predicate's *behavioral* content (the four checks) was exercised only through the counter's own
  `--rev` arms at the two declared revs; I did not construct dishonest revs beyond the two predicate commands.
- No LSP server queries (no device in this seat's inventory); prose sites were compared textually, code sites by
  reading the exact line ranges cited.
