# RevReceiptRevs — round 65, wave 1: do the receipts name the rev they measured (Q36), and do the SCORECARD citations match?

Seat: reviewer, leaf member (no dispatch). Reviewed 2026-10-24 07:41 UTC, Python 3.14.8,
`python3 -B`. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (jj-colocated).

Attack surface: the landed round-65 bytes. At review time the lane had already moved on —
round 65 was closed by the non-author spot-check at `11385e0` and round 66 landed on top
(`HEAD = 2a8eba56b3f9321b70c569fa2816d42237ca49a2`). Every byte below is committed and
immutable from this seat's point of view; I read only, ran nothing in the lane, and created
no git/jj state. All executions were in `/tmp` extractions (`git archive <rev>`), 1 process
at a time, each under 120 s.

Q36 as written (`corpus/QUALITY.md:47`): *"A no-harm or tip receipt cited in a report names
the revision it measured in the receipt itself (a printed `git rev-parse HEAD` or
`--rev`/`--head` value); a report line citing a revision no committed receipt names is
struck, not kept."*

## 0. Receipt byte identities (so a later seat can prove it attacked the same bytes)

```
$ sha256sum .ufo/waves/round-65/receipts/*.txt
4de3aef034287587d8d1abb1a032e8f85351ec0ffc7ec40585e89b2d241f770a  C1-close-kill.txt
039047782adbe2152c3e9fc94f13929224ac0cf464e548edda07e484a321fc3a  C1-close-measure.txt
9684746037df00b9324a19e0bd18aecdb1eabddbaf726e397c4fb6a080dce810  C2-governance-measure.txt
6c81348992659966796d6aabd29d0359644e10ffc7afb54d12c08b7bc2316503  C2-selfreference-redbefore.txt
bd19cf9ef5c5b88a902b3020900ddcacf8d0b7e22500cc2dcb1131d545542f9e  FLOORS-after.txt
364d593deaa68230fd13b33d9dc8eeb194a45ac663584db7411ad04b6f86e919  FLOORS-noharm.txt
ee740da79fe52eca127ea2b8424c73e45b576945d7a72ebf6e2d8ff59d03a810  M99-fixture-leak.txt
bd0dce8a1c9438335fc19d973a0b7f4f9cb56d2a6e657948061e4658fee56a8b  REGRESSION-probes.txt
ee31aa39332231a9c9b4059ab99679ba02c7e8c6898278413263c7d7bafe6d28  noharm-tip.txt
```
Working tree == HEAD for the whole receipts dir (`git status --porcelain .ufo/waves/round-65/receipts/`
→ empty), so every receipt cited below is committed, not a working-copy artifact (Q50 shape OK).

All four cited revisions resolve uniquely at this tip:

```
80bb8921   disambiguate=1 -> 80bb89211841289bc802fa7b55057f0ef266d19e
0e104f49   disambiguate=1 -> 0e104f498b3df1466284074c5b3a6e5b523420cd
c98d137    disambiguate=1 -> c98d1378236bae56d9d2ecacd5db59a4cc142e1e
5253b281   disambiguate=1 -> 5253b28174a17dccba8db391b2a5b9bc6470472a
```
So the short-sha headers are unambiguous *at this tip*; the "disambiguate=1" check is what a
reader must redo after any history rewrite, which is a residual risk, not a defect (see R3).

## 1. Q36 test: one row per receipt file

| receipt | rev named in the file? | form | independent byte binding printed? | verdict |
|---|---|---|---|---|
| `C1-close-measure.txt` | **yes**, full sha | header `# C1 measure @ 80bb89211841289bc802fa7b55057f0ef266d19e (committed bytes via git archive)` | **yes** — `counter sha256 b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d` + `sha256sum` of the file | **PASS** |
| `C1-close-kill.txt` | **yes**, 7-hex short | header `# C1 kill battery @ 80bb8921 (committed bytes; each lane one exact-string replacement)` | no — no candidate sha256; only `234 assertions` links it to a rev | **PASS (weak)** → F5 |
| `C2-governance-measure.txt` | **yes**, full sha | header `# C2 measure @ 80bb89211841289bc802fa7b55057f0ef266d19e` | partial — assertion count 1862 is rev-bound; the green result is also location-bound (F4) | **PASS (weak)** → F4 |
| `C2-selfreference-redbefore.txt` | **no** | body only (`BACKTICKED notice: status=FAIL`) | no | **FAIL (Q36)** → F2 |
| `FLOORS-after.txt` | **no** | body only (`$ python3 -B verifiers/check_assertion_floors.py   # after, with scoped_rules_v32 row`) | no | **FAIL (Q36)** → F1 |
| `FLOORS-noharm.txt` | **yes**, 7-hex short | `# noharm full walk @ 0e104f49` | no (no instrument shas) | PASS |
| `M99-fixture-leak.txt` | **no** | two lines, no command, no fixture path, no exit codes | no | **FAIL (Q36)** → F3 |
| `REGRESSION-probes.txt` | **yes**, 7-hex short | `# regression probes @ 80bb8921` | no; and one probe line records `exit None fail None` | PASS (weak) → F6 |
| `noharm-tip.txt` | **yes**, 7-hex short + base | `# noharm battery @ 0e104f49 (base c98d137)` | no | PASS |

Score: **6 of 9 receipts name a revision; 3 do not** (`C2-selfreference-redbefore.txt`,
`FLOORS-after.txt`, `M99-fixture-leak.txt`). `kill_battery.py` is a harness, not a receipt,
and carries no rev either (by design — see F5).

## 2. SCORECARD citation match (round-65 block, `SCORECARD.md:381`)

| SCORECARD claim | receipt(s) cited | rev each cited receipt names | match |
|---|---|---|---|
| C1 counted predicate, `234 assertions`, `measured @ 80bb89211841289bc802fa7b55057f0ef266d19e`, `committed v32 sha256 b6cfc764…` | `receipts/C1-close-measure.txt`, `C1-close-kill.txt` | full `80bb8921…` + `b6cfc764…` (measure); short `80bb8921` (kill) | **match** (reproduced, §4) |
| kill conjunct: `SM1–SM6, M7, M8, M9, M10, M12, M14, M17, SPAN_FIRST, SPAN_LAST, M20, M11-upper exits 1`, attribution SM4/SM6/M11 | `C1-close-kill.txt` | `80bb8921` | **match on 17 lanes + attribution**, one id mismatch → F7 |
| C2 `"fail": 0`, 11/11, `governance.citation_resolves` PASS, `3 recorded correction(s) excused`, self-test `1852 → 1862`, `measured @ 80bb8921`, receipts `C2-governance-measure.txt`, `C2-selfreference-redbefore.txt`, `M99-fixture-leak.txt` | the three named files | only `C2-governance-measure.txt` names `80bb8921…`; the other two name **no rev** | **partial mismatch** → F2, F3 (and F4 for rev-sufficiency) |
| before-state `"fail": 1`, exit 1 `@ c98d137` (10/1) | `controls/C2-before.txt` | full `c98d1378236bae56d9d2ecacd5db59a4cc142e1e` | **match** |
| `Floors: scoped_rules_v32 registered at 234` | none named in the SCORECARD; the closure lesson cites the pair `FLOORS-after.txt` / `FLOORS-noharm.txt` (`corpus/lessons/round-65-verifier-spotcheck.md:38`) | `FLOORS-noharm`: `0e104f49`; `FLOORS-after`: none | **backed by the pair's rev-named half**, the unreved half carries numbers no commit produces → F1 |
| `v31 prints survivors closed 5 of 6 over 201` / `pkg7 control world … 230 assertions` | none in the SCORECARD (`C1-close-kill.txt` carries the 230-assertion control lanes; the 201 figure is round-64 material) | kill: `80bb8921`; the 201 line names no rev and no receipt | **match for 230**; the 201 line is a prose control with no receipt and no rev (not a Q36 measurement claim, flagged for the plan-length seat) |

No SCORECARD line in the round-65 block cites a revision that *no* committed receipt names
except the two dropped seat-quoted pins (`f3c82574…`, `b614e8b1…`) — F8.

## 3. Findings, by severity

### F1 — MEDIUM — `FLOORS-after.txt` names no revision and its recorded state exists at **no commit**

`receipts/FLOORS-after.txt` (committed in `5253b281`, whose subject says *"measurement receipts
**at 80bb8921**"*) prints:

```
PASS checklist observed=1852 floor=1852
PASS scoped_rules_v32 observed=234 floor=234
exit=0
```

There is no rev in the file and no state that can produce those two lines together:

```
$ git show c98d137:verifiers/floors-registry.json   -> checklist floor 1852 ; scoped_rules_v32 absent (grep -c = 0)
$ git show 80bb8921:verifiers/floors-registry.json  -> checklist floor 1862 ; scoped_rules_v32 floor 234
$ git show 80bb8921 -- verifiers/floors-registry.json
-  "instrument_total": 14,          +  "instrument_total": 15,
-  "checklist": {                  +    "checklist": {                 (floor 1852 -> 1862, parsed both revs)
                                    +    "scoped_rules_v32": {          (new row, floor 234)
```

Both rows moved in **one** commit (`80bb8921`), so `v32 = 234` with `checklist = 1852` is not
any commit's state: it is the author's uncommitted working tree between the C1 edit and the C2
edit. The file therefore is not Q36 evidence for anything, and the commit that carries it
attributes it to a rev that would print `checklist observed=1862`.

It has already reached the closure record. `SCORECARD.md:381` does not cite it, but
`corpus/lessons/round-65-verifier-spotcheck.md:38` does:

```
guard self-test 165 ≥ floor 150 in `receipts/FLOORS-after.txt` / `FLOORS-noharm.txt`
```

The claim survives because the *pair* is cited and `FLOORS-noharm.txt` (`@ 0e104f49`) prints
the same `floors_guard observed=165 floor=150` line with a rev in the file; the harm is that
an unreved file whose other rows (`checklist 1852`, `v32 234`) describe no commit now sits in
the closure's evidence chain, so a reader who takes it alone gets numbers the measured rev
falsifies. The round-66 receipts dir *does* head its same-named file with the rev
(`Round 66 assertion floors at fc1b71e5…`) — this is a round-65 omission, not house style.

Fix shape: head it `# pre-C2 intermediate working tree (no commit; v32 234, checklist 1852)`
or delete it and cite `FLOORS-noharm.txt` (which is rev-named).

### F2 — MEDIUM — `C2-selfreference-redbefore.txt` names no rev, no command, and its fixture is gone

```
BACKTICKED notice: status=FAIL
detail: LOG.md:2: 'corpus/gone.md' does not resolve from /tmp/kotoba-redbefore-nkodw7fe; … 1 recorded correction(s) excused
QUOTED notice:     status=PASS (evaluated=1)
```

No revision, no command line, and the fixture root `/tmp/kotoba-redbefore-nkodw7fe` **no
longer exists** (`ls -d /tmp/kotoba-redbefore-*` → "No such file or directory"), so the
probe cannot be rerun at all. `SCORECARD.md:381` nonetheless lists this file among the
receipts of the C2 measurement *"@ 80bb8921"* — an attribution the file does not make. The
lesson row (`corpus/lessons/round-65.md` M100) cites it the same way. It is a fixture probe,
so the honest header is *"checker bytes at 80bb8921 (sha256 …), sandbox `<path>`"*; without
it a reader cannot tell whether the probe ran against landed or pre-landing bytes — exactly
the harm Q36 exists to prevent.

### F3 — MEDIUM — `M99-fixture-leak.txt` names no rev, no command, no fixture, no exit code

```
bug A (errata default leaks into fixture): status=FAIL
   ["erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py' is past horizon 2315 or absent"]
bug B (subject line mismatch): status=FAIL
   ["correction LOG.md:2 SCORECARD.md:8 'corpus/gone.md': names no live red subject"]
```

`corpus/lessons/round-65.md` M99 says this file "regenerates both bug shapes … in a sandbox
world". The file shows no sandbox, no command, no checker sha, no rev, and no exit codes;
`status=FAIL` is a fixture-expected verdict, not a process exit. Cited in `SCORECARD.md:381`
as @ `80bb8921` evidence and in the lesson. Q36 failure: nothing in it is revision-bound, so
it cannot be re-derived at any rev.

### F4 — MEDIUM — the C2 receipt is rev-bound but **not rev-sufficient**: the green does not reproduce at the named rev outside the fleet layout

Frozen predicate (plan / `SCORECARD.md:381`): *"`verify_skill_checklist.py --json` prints
`\"fail\": 0`, exit 0 (11/11) **at the measured rev**, with `governance.citation_resolves`
PASS"*. At the measured rev in a clean extraction:

```
$ git archive 80bb8921 | tar -x -C /tmp/r65q36 && cd /tmp/r65q36
$ python3 -B verifiers/verify_skill_checklist.py --json      # fail 3, pass 8, exit 1
  trigger.name_directory      -> FAIL | name 'kotoba-shokunin' != directory 'r65q36'      # my extraction dir, not a lane defect
  trigger.citation_resolves   -> FAIL | line 589: '../.ufo/reports/round-7/kotoba.md' does not resolve from /tmp/r65q36
  governance.citation_resolves-> FAIL | correction LOG.md:2619 … corrected token '../.ufo/reports/round-60/kotoba.md' does not resolve
$ python3 -B verifiers/verify_skill_checklist.py --self-test # 1 failure(s) over 1862 assertions ; exit 1
  self-test FAIL: governance: live round-65 corrections land, check PASS … 0 recorded correction(s) excused
$ python3 -B verifiers/check_assertion_floors.py             # exit 1
  FAIL checklist observed=1862 floor=1862 self_test_failures=1
  FAIL correction_sweep observed=25 floor=25 self_test_failures=1
```

Repeated under a fleet-like parent (`/tmp/fleetq36/.ufo/…` populated, lane at
`/tmp/fleetq36/lane`): still `1 failure(s) over 1862 assertions`, this time on the other `../`
tokens (`../PROTOCOL.md`, `../.ufo/reports/round-11/kotoba.md`, `../kasegi-shokunin/…`). The
assertion **count** 1862 *is* rev-bound (it matches at the rev); the **`0 failures` / `fail:0`**
needs the exact fleet root — the lane must sit at `/home/vgpnk/Projects/shokunin/…` with the
sibling repos and `.ufo` tree present. The base control has the same property
(`controls/C2-before.txt` shows `trigger.citation_resolves` PASS at `c98d137`, i.e. it was also
run in-lane), so the *comparison* is fair; what is missing is the precondition. Round 55's
receipts stated it explicitly (`.ufo/waves/round-55/falsify/NoHarmGates.md` F2, "verifier at
plan commit, `--skill` = the lane working copy"); round 65's do not.

Mitigation, verified: the red is **loud**, never silently green — the floors guard itself
flips to `FAIL checklist … self_test_failures=1` in a clean checkout. So this is a
reproducibility/disclosure defect, not a hidden false green. Fix shape: header the receipt
`# run from the lane path under the fleet root (<path>); ../ citations resolve there`, and/or
add the same sentence to the SCORECARD line.

### F5 — LOW — `C1-close-kill.txt`'s rev binding is a hand-written short sha with no byte pin

Header names `80bb8921`; the harness (`receipts/kill_battery.py`) hardcodes
`TREE = Path('/tmp/r65work/tree')`, takes no `--rev`, prints no `sha256sum`, and never checks
that the extracted tree is the named revision. The only in-receipt link from the output to a
rev is the count `234`. Corroboration available *today* (ephemeral, not evidence a receipt
can carry):

```
$ git show 80bb8921:verifiers/check_scoped_rules_v32.py | sha256sum
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d
$ sha256sum /tmp/r65work/tree/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d      # == the named rev's bytes
$ for f in verifiers/verify_skill_checklist.py verifiers/floors-registry.json; do
    git show 80bb8921:$f | sha256sum ; sha256sum /tmp/r65work/tree/$f ; done
86d8b1584242ccaa096ac9a17e83be28c49e88a21c90bfb7b7ffddfa94bb25f1 == 86d8b158…   (checklist)
3b53d9087cfc483dca1edcfeeeb64559312b1db6bad41069b740a43bafc89077 == 3b53d908…   (registry)
```

So the claim "committed bytes" holds today; the receipt just doesn't prove it. Fix shape:
`print("candidate sha256", hashlib.sha256(BASE.encode()).hexdigest())` as the baseline line,
and `git rev-parse <rev>` before extraction.

### F6 — LOW — `REGRESSION-probes.txt` records a non-result as a probe

```
# regression probes @ 80bb8921
…
$ python3 -B verifiers/verify_corpus_integrity.py --json
corpus_integrity exit None fail None
```

`exit None` is the wrapper's own missing return, not an observed exit code; a receipt must
record what it observed. The `5253b281` subject claims the red was "pre-existing identical at
base c98d137", but no receipt in the round-65 set prints that base run, so the claim rests on
the commit message prose. Q36-wise the file is compliant (it names `80bb8921`); it is flagged
because an unrun/non-observing line inside a rev-named receipt is the classic way a red gets
laundered.

### F7 — LOW — the kill-conjunct enumeration names `M11-upper`; no receipt lane has that label

`SCORECARD.md:381` (and the plan) require *"M11-upper exits 1"*. The receipt's lane is
`== M11-page-no-lower: exit=1  self-test: 7 failure(s) over 234 assertions`; the string
`M11-upper` appears on no receipt line. The attribution sentence does match the receipt
exactly (`first via pre-existing A2 cell arm`/main-world collateral; new arm as named
witness), and the mechanism is the case-sensitivity mutant. Recommend renaming the lane or
the citation so the frozen predicate's identifiers are greppable in the receipt.

### F8 — LOW — the SCORECARD copies two shas its own upstream seat told it not to copy

`SCORECARD.md:381` prints `f3c82574…`/`b614e8b1…`. Their source is
`.ufo/waves/round-64/w2/MutW2M7M22.md:162-163` (full values) and the same file at line 185:
*"it means the L1 must not copy `f3c82574…`/`b614e8b1…` into a receipt."* No committed receipt
names them, and Q36's second clause says such a report line is *struck, not kept*. The
SCORECARD does mark them as non-reproducing and dropped, so the intent is honest; the tokens
are still unattested. Cheapest repair: keep only the report anchor (`MutW2M7M22` §4, seat-quoted
pins, not reproduced) and drop the hex.

## 4. What reproduces (positive verification, exit codes as observed)

C1 counted predicate at the named full sha — re-derived from `git archive`, not from the lane:

```
$ cd /tmp/r65q36 && python3 -B verifiers/check_scoped_rules_v32.py --self-test
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 234 assertions
exit=0
$ sha256sum verifiers/check_scoped_rules_v32.py
b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d
```

Matches `C1-close-measure.txt` line-for-line on the predicate, the pin and the counter sha
(`b6cfc764…` = `git show 80bb8921:verifiers/check_scoped_rules_v32.py`, also = the round-65
spot-check's recomputation at `corpus/lessons/round-65-verifier-spotcheck.md:35`). Kill-receipt
structure reconciled: **17** `exit=1` kill lanes + **1** `exit=1` control lane +
**7** `exit=0` lanes (baseline, `M19`, `M22`, `pkg7-control`, `control+SPAN_FIRST`,
`control+SPAN_LAST`, `control+M20`); `RESULT: ALL OK`, `harness_exit=0` — arithmetically
consistent with the SCORECARD's conjunct and with `MutW2M7M22` F7 (M11 killed by pre-existing
collateral in every world).

C2 at the named rev: assertion count `1862` reproduced (green only in-lane, F4); the receipt's
`"3 recorded correction(s) excused"` matches the three appended notices at
`LOG.md:2619-2621` in the same commit; `checklist` floor 1852 → 1862 in
`verifiers/floors-registry.json` (parsed at both revs) matches the bump-in-step claim, and
`scoped_rules_v32` row = 234 with `instrument_total` 15 (14 at base).

`FLOORS-noharm.txt` (`@ 0e104f49`) and `noharm-tip.txt` (`@ 0e104f49`, base `c98d137`) are the
receipts that actually carry the round's floors/no-harm numbers with a rev named in the file;
their printed `checklist 1862/1862`, `scoped_rules_v32 234/234`, `r64 43 assertions`,
`r63 5 of 5` are consistent with the same rev's bytes (v32 unchanged between `80bb8921` and
`0e104f49`).

## 5. Residual risk and verification gaps

- **R1 — Could not re-run the C2 `--json` (11/11) inside the lane at `80bb8921`**: doing so
  requires mutating the lane's working tree, which this seat's write bounds forbid. I verified
  the rev's bytes, the assertion count and the three-correction detail instead, and proved the
  out-of-lane run fails (F4). A falsifier with a sanctioned sandbox at the lane path should
  close this.
- **R2 — Could not re-run `kill_battery.py`** (it mutates its own tree; it also writes to a
  hardcoded `/tmp/r65work/tree`). Corroborated by tree-identity hashes (§F5) + the 234 count.
- **R3 — short-sha headers** (`80bb8921`, `0e104f49`, `c98d137`) resolve uniquely *at this tip*
  only. Any history rewrite (jj rebase/describe) invalidates them silently; the full shas in
  `C1-close-measure`/`C2-governance-measure` are the durable pair. Suggest full shas in every
  receipt header.
- **R4 — the 201-assertion / `survivors closed 5 of 6` do-nothing control** is asserted in the
  plan and cited to round-64 material; no round-65 receipt names it. Not a Q36 measurement
  claim (no revision is cited), but a falsifier should confirm the figure before the closure
  leans on it.
- **R5 — `/tmp/r65work/tree` is live and mutable** (`kill_battery.py` rewrites the candidate in
  place). It happens to hold the named rev's bytes now; it is not evidence.
- The round-65 non-author spot-check (`11385e0`) verified the two *measured* receipts' pins but
  did not audit the receipts dir for Q36 identity — F1/F2/F3 survived that closure (it cites
  `FLOORS-after.txt` at line 38 only as the rev-named file's partner). That is the calibration
  headline: Q36 was applied to the claim receipts, not to the receipt *set*.

## 6. Claims this seat's findings support or falsify

- **C1 (depth, 223 → 234 + floors registration):** *supported* in its counted predicate, pin
  and floor row (reproduced, §4). *Weakened in evidence completion*, not in value: the floors
  receipt that sits in the receipts dir (`FLOORS-after.txt`) is unreved and describes no commit
  (F1); the kill receipt's rev binding is a header with no byte pin (F5); one enumeration id
  does not exist on the receipt (F7). No C1 number is falsified.
- **C2 (consistency / governance corrections, checklist 1852 → 1862):** *supported* in the
  number, the pin and the three-excused-cells detail; the frozen predicate's "`fail: 0` …
  **at the measured rev**" is *falsified as stated* — it holds only in the fleet layout (F4).
  Two of the three receipts the SCORECARD cites for the C2 measurement name no rev at all
  (F2, F3), so the C2 receipt set does not satisfy Q36 as cited.
- **Q36 itself:** holds for 6 of 9 round-65 receipts; fails for 3. The SCORECARD's revision
  citations match the receipts except for the two fixture receipts (F2/F3) and the two
  disowned shas (F8).

## 7. Tooling / environment

No installs, no upgrades, no pacman transaction (host-wide pause honored; nothing was needed).
Scratch used: `/tmp/r65q36`, `/tmp/r65base`, `/tmp/fleetq36` (all created by `git archive`;
read-only against the lane). Lane jj state, lane Git index and every file outside this report
are untouched.
