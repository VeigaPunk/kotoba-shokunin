# ExecC1Selftest — round 66, C1 self-test at observed lane tip

Seat: leaf executor (`ExecC1Selftest`), read-only measurement. No claim, counter,
threshold, plan, receipt, lane jj state or Git index was modified. This seat is not a
judge; the numbers below are observations for the L1 planner seat.

## 1. Provenance of the measurement

| Item | Observed value |
|---|---|
| Repo | `/home/vgpnk/Projects/shokunin/kotoba-shokunin` |
| Observed Git tip (`git rev-parse HEAD`) | `2a8eba56b3f9321b70c569fa2816d42237ca49a2` — "round-66 verifier spot-check (integrator, hyaku): non-author admit/reject", 2026-10-24 04:26:20 -0300 |
| jj working copy (observed, moving) | at first read: jj `@` commit `98c994b017ca`; at last read (04:36): change `omvyzpnszwon`, commit `2d2a13cdcd65`, `empty=false`, `conflict=false`. jj moved because read-only jj queries auto-snapshot the working copy and concurrent seats were adding report files; no jj authoring command was issued. The measured revision is keyed to Git HEAD plus the verifier sha256, not to the jj id. |
| Pinned plan base | `11385e04e368c1e94ab1a5a89d7439033eb1f855` |
| C1 landed commit | `806b53b` ("round-66: land G9 coupling and integrity fixes"); `fc1b71e56fda86fefe672f2cae90a62318d34449` is an ancestor of HEAD, and no commit in `fc1b71e..HEAD` touches `verifiers/check_scoped_rules_v32.py` |
| Measured verifier bytes | `sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` (identical before and after every command below; identical to `receipts/C1-measure.txt` and `receipts/C1-landed-measure.txt`) |
| Dirty tracked path at observation | `.ufo/waves/round-66/w1/swarm-registry.json` — already modified before my first command, modified again by concurrent seats during the wave; not touched by this seat and not read for content |

## 2. Required measurement

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
...
self-test: 0 failure(s) over 240 assertions
EXIT=0
```

Revision: `2a8eba56b3f9321b70c569fa2816d42237ca49a2`. Exit: **0**. Assertions: **240**.
Failures: **0**. Predicate line confirmed at the observed tip, not only at the two
revisions named in `C1-landed-measure.txt`.

## 3. Frozen headline lines (verbatim from the run)

| Frozen line (plan §C1 / receipts) | Observed | Status |
|---|---|---|
| `worlds reject 7 of 7; eligible rows pass 4 of 4` | present, verbatim | match |
| `survivors closed 6 of 6` | present, verbatim (six `survivor …: before accepted; after rejected` lines) | match |
| `must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes` | present, verbatim | match |
| `must-fail E2e guard disabled admits e2e-negated-path-key: yes` | present | match |
| `must-fail G7 disabled admits e2f-backticked-event-claim: yes` | present | match |
| `self-test: 0 failure(s) over 240 assertions` | present, verbatim | match |
| `counter sha256 97d897…bed26def` | present, first output line; equals `sha256sum` of the file | match |

Full observed block (abridged only in the per-world reason strings, which are unchanged
from `receipts/C1-measure.txt`):

```
counter sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def
world W1 … W7: reject=True (arms A4, A3, A1, live, A1, A2, A1)
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target … e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 240 assertions
```

## 4. Pinned base, measured separately (temporary sandbox)

Exported with `git archive 11385e04… | tar -x -C /tmp/r66base.85KkXe` (no worktree, no
index write), then run there:

```
$ cd /tmp/r66base.85KkXe && python3 -B verifiers/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 234 assertions   (exit 0)
```

Base verifier sha256 `b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d`
(≠ measured tip). Base `g9_conjunct` still carries `MIN_CLAUSE = 2` and uses
`fwd_need(len(w))` for both comparisons; there is no `clause_need` symbol at base.

Control replay, base sandbox, command from `controls/C1-one-word-control.txt`, verbatim:

```
$ python3 -B -c '…; line="The index stores project rules."; page=line+"\n\n## Schedule\nThe agent secretly exfiltrates telemetry."; cell=line[:-1]+" and exfiltrates."; print("one-word-tail reasons:", m.g9_conjunct([line], cell, 1, page))'
one-word-tail reasons: []
```

Same command at the measured tip (`2a8eba56`):

```
one-word-tail reasons: ['A2 G9: clause "exfiltrates." is supported outside the cited line']
```

So the do-nothing control is real at the base (admits the witness, 234 assertions) and the
witness is closed at the tip (rejects, 240 assertions). Pinned base and measured tip are
kept distinct: 234/base-sha-`b6cfc76` vs 240/tip-sha-`97d8971`.

## 5. Independent cross-check of the counted value

```
$ python3 -B verifiers/check_assertion_floors.py    # reruns every registered self-test
PASS scoped_rules_v32 observed=240 floor=240
EXIT=0
```

`verifiers/check_assertion_floors.py:176` registers `"scoped_rules_v32": 240`, so the
committed floor and the observed count agree at the observed tip.

## 6. 234 → 240 arithmetic (why the count is exactly +6)

`git diff 11385e04..HEAD -- verifiers/check_scoped_rules_v32.py` (49 insertions, 16
deletions) touches `check(` lines thus:

- removed: `check("A2 G9: a ONE-word clause is exempt (declared bound)", …)` (1)
- added:
  1. `A2 G9: a ONE-word off-citation clause is rejected`
  2. `A2 G9: a ONE-word clause supported by the cited line passes`
  3. `A2 G9: clause need couples the one-word floor` (`clause_need(1) == 1`)
  4. `A2 G9: clause need retains the two-word floor` (`clause_need(2) == fwd_need(2)`)
  5. `A2 G9: clause need retains the three-word fraction` (`clause_need(3) == fwd_need(3)`)
  6. `must-fail G9 uncoupled MIN_SHARED admits one-word fabrication`
  7. `must-fail G9 zero clause floor admits one-word fabrication`

234 + 7 − 1 = 240, matching both runs. `MIN_CLAUSE` is gone at the tip (no dead constant;
`grep -n MIN_CLAUSE` → none); `clause_need` has exactly one production call site
(`check_scoped_rules_v32.py:1145`, inside `g9_conjunct`) plus the three pins.

## 7. Mutation battery re-run (`receipts/C1-kill.txt`) — observed vs receipt

Method: full `verifiers/` directory copied to `/tmp/r66mut2.7t3Y46/K<n>/` (the self-test
imports a sibling `check_erratum_absorption.py`, so single-file copies raise
`FileNotFoundError` and never reach the C1 arms), one `sed -E` mutation per copy, run as
`python3 -B <mutant>/check_scoped_rules_v32.py --self-test` from the lane root. Lane bytes
untouched. Mutations were diff-verified before running (my first K2 attempt was a silent
no-op; its re-applied form is the one reported).

| Mutant | Exit | Failures | First FAIL observed | Receipt's attributed line |
|---|---:|---:|---|---|
| K1 `clause_need → fwd_need` | 1 | 2 | `FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True` | same (1st) ✓ |
| K2 skip clauses with `< 2` content words | 1 | 1 | `FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True` | same ✓ |
| K3 page comparison uses `fwd_need(len(w))` | 1 | 1 | `FAIL A2 G9: a ONE-word off-citation clause is rejected: got False, expected True` | same ✓ |
| K4 line comparison uses `fwd_need(len(w))` | 1 | 2 | `FAIL A2 G9: a ONE-word clause supported by the cited line passes: got True, expected False` | same (1st) ✓ |
| K5 `clause_need → 0` | 1 | 20 | FAIL A2 G9: an 'and'-joined purpose clause off the cited line is rejected: got False, expected True | names the ONE-word line, which is the **14th** FAIL |

All five receipts' claims "exit 1 and the named witness line appears" reproduce. K2's
receipt line reproduces exactly (1 failure). K1 and K4 also trip one secondary arm
(`clause need couples the one-word floor`; `must-fail G9 zero clause floor admits …`),
which the receipt's "also trip secondary arms" note covers; K5 trips 20 arms and its
attributed line is not the first FAIL, so the receipt's "first load-bearing C1
witness/control" phrasing overstates the ordering for K5.

## 8. Coupling behaviour, probed directly

`clause_need(n) = min(fwd_need(n), n)`; `fwd_need(n) = max(2, ceil(2n/3))`.

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `fwd_need` | 2 | 2 | 2 | 2 | 3 | 4 | 4 | 5 | 6 | 6 | 7 | 8 | 8 |
| `clause_need` | 0 | 1 | 2 | 2 | 3 | 4 | 4 | 5 | 6 | 6 | 7 | 8 | 8 |

The coupling differs from the old flat floor **only at n = 1** (2 → 1); n = 0 is
unreachable because `g9_conjunct` does `if not w: continue` before the call. So the pins
at lengths 2 and 3 are retention pins (they prove the change stayed surgical), and the
length-1 pin is the discriminating one. Replays at the tip:

- `and exfiltrates.` where *exfiltrates* occurs only elsewhere on the page → rejected,
  `A2 G9: clause "exfiltrates." is supported outside the cited line`.
- `and glob.` where *glob* is in the cited line → accepted (`[]`), as the plan requires.
- `and stores.` where *stores* is a cited-line word → accepted (`[]`), and the full
  `action_conjunct` path also returns `[]`. This is the declared lexical semantics ("a
  one-word tail supported by the cited line remains accepted"), not a defect, but it is
  the acceptance boundary: one shared word out of one word is 100 % support.
- `and stored.` against a line word *stores* → accepted via the documented four-character
  prefix rule (`supported()`: same word or shared 4-char prefix). Inherited from A2,
  unchanged by C1.
- `and now.` (3 letters) → no G9 reason, and the full `action_conjunct` path also returns
  `[]`: `CONTENT_RE` is `[a-z]{4,}`, so sub-4-char tails are dropped by `content_words`
  and `page_words` alike and are invisible to A2 and G9. Pre-existing declared vocabulary
  bound; C1's one-word tail means a one-**content**-word tail.

## 9. Residual pinning gap found by an extra mutant

Extra mutant K7 (not in the receipt): `need = 2 if len(w) == 4 else clause_need(len(w))`
— honest everywhere except a 4-content-word clause, whose floor drops 3 → 2.

```
$ python3 -B /tmp/r66mut2.7t3Y46/K7/check_scoped_rules_v32.py --self-test
self-test: 0 failure(s) over 240 assertions
exit=0
```

K7 is **green**. The plan pins lengths 1, 2 and 3 only, so this is not a contradiction of
the frozen claim; it is the boundary of the pinned set. Why no fixture sees it: the
shortest clause that exercises a floor above 2 is the 5-word backticked clause in
`A2 G9: a clause absent from the page is NOT reported by G9`, which has page coverage
3-of-5 and honest need 4 (`fwd_need(5)`); K6 (`min(fwd_need(n-1), n)`, which lowers need
to 3 for n = 5) is caught by that fixture, while n = 4 has no comparable fixture.

Related observation on that same fixture: its name says "absent from the page", but the
clause is *present* 3-of-5 on the page (`secretly`, `exfiltrates`≈`exfiltrated` by prefix,
`nightly`); `telemetry` and `beacons` are absent. The assertion is really a below-floor
page test (3 < need 4) and is the only pin above 3. The name predates round 66 (round-63
`MutW2GuardEvasion`); flagged because it is the arm that caught K6 and a maintainer
reading the name would mis-model what it protects.

## 10. Side effects / cleanliness

- No tracked file changed by this seat: `git status --porcelain` before and after every
  command shows only `.ufo/waves/round-66/w1/swarm-registry.json` (already dirty at my
  first command, moved again by concurrent seats) and other seats' new `w1/*.md` files,
  plus this report. No worktree, branch, bookmark, commit, stage or index operation was
  performed; mutations lived only under `/tmp/r66mut.DkH8cB`, `/tmp/r66mut2.7t3Y46` and
  `/tmp/r66base.85KkXe`. Two read-only `jj log -r @` calls auto-snapshotted the working
  copy (jj's default), which moved jj `@` from `98c994b017ca` to `2d2a13cdcd65` as peer
  report files landed; no jj authoring command was issued.
- Every Python invocation I issued used `python3 -B`. A gitignored
  `verifiers/__pycache__/check_scoped_rules_v32.cpython-314.pyc` exists with mtime
  04:33:32; the floors gate does not import that module, and a `-B` process writes no
  bytecode, so it is attributable to concurrent seat activity rather than to this seat.
  It does not affect tracked bytes or the measured sha256.

## 11. Mismatches and risks (none blocking the frozen predicate)

1. K5 attribution ordering in `receipts/C1-kill.txt` (§7): cited line is the 14th FAIL, not
   the first. Exit 1 and the named line both hold; presentation only.
2. K1 and K4 produce one extra FAIL each beyond the single line the table lists; the
   receipt's caveat acknowledges secondary arms.
3. `receipts/C1-landed-measure.txt` names `806b53b4…` and `fc1b71e5…` as its revisions;
   the observed tip is one commit later (`2a8eba56…`). The verifier bytes are unchanged
   across that span (no commits touch the file in `fc1b71e..HEAD`, sha identical), so the
   receipt's value carries forward to the measured tip — recorded here explicitly so the
   pinned/measured distinction stays visible.
4. Residual pin gap at a 4-content-word clause (§9) and the misnamed "absent from the
   page" fixture (§9). Neither changes the 240 count or any frozen line; both are
   future-round pin candidates if the coupling is tightened again.

## 12. Observed status for the planner seat

At `2a8eba56b3f9321b70c569fa2816d42237ca49a2`, `python3 -B
verifiers/check_scoped_rules_v32.py --self-test` exits 0 and prints `self-test: 0
failure(s) over 240 assertions` with `worlds reject 7 of 7; eligible rows pass 4 of 4`,
`survivors closed 6 of 6` and all three `must-fail … : yes` lines, at verifier sha256
`97d897…bed26def`. The same command at pinned base `11385e04…` (sandbox) prints 234
assertions and the one-word control returns `[]`. No score is asserted by this seat.
