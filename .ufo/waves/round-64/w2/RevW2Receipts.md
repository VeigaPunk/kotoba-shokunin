# RevW2Receipts — round-64 receipt discipline

- **Author:** `RevW2Receipts` (wave 2, falsify seat). Read-only: no lane file touched (scratch `/tmp/r64rev`).
- **Measured rev:** `c019919c97ab5fe98e87a7754b4449ea4e699c99`; base `078eec4a1f6a41c64ff8806f58b46a67cd413bfc`;
  receipts committed at `b99fb79c27042e0f8a598cbbb4d81479a806b518` (= git HEAD).
- **Method:** every counting command re-run from `git archive` materializations of base and tip
  (`/tmp/r64rev/{base,tip}`) and from the lane; every sha256 recomputed with `git show <rev>:<path> | sha256sum`;
  every cited number compared against my own run.
- **Tooling:** none installed or upgraded.

## Verdict

Item (1) **clean**. Item (2) **one high-severity break**: the no-harm receipt at HEAD records the measured rev as
**FAILED**, and the working tree holds an uncommitted, truncated PASS rerun that replaces it. All numeric and
sha256 content in the five claim/control receipts reproduces exactly. Item (3) **four overreach/attribution
sentences** (two material, two minor).

---

## 1. Round-63 receipts and controls: byte-untouched — PASS

```
$ git log --oneline 078eec4a1f6a41c64ff8806f58b46a67cd413bfc..c019919c97ab5fe98e87a7754b4449ea4e699c99 \
    -- .ufo/waves/round-63/receipts .ufo/waves/round-63/controls
(no output)
EXIT=0

$ git log --oneline 078eec4a1f6a41c64ff8806f58b46a67cd413bfc..HEAD \
    -- .ufo/waves/round-63/receipts .ufo/waves/round-63/controls
(no output)
EXIT=0

$ git diff --stat 078eec4 c019919c -- .ufo/waves/round-63/receipts .ufo/waves/round-63/controls
(no output)
EXIT=0

$ git status --porcelain -- .ufo/waves/round-63/receipts .ufo/waves/round-63/controls
(no output)
EXIT=0
```

Blob-pin proof (stronger than the log filter — every tracked file in both dirs is bit-identical at
base, at `c019919c` and at HEAD):

```
SAME f02b8958… .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
SAME b25a3ed6… .ufo/waves/round-63/controls/C2-before-r62tip.txt
SAME b2d0441a… .ufo/waves/round-63/receipts/C1-g9-interim-cbbee56e.txt
SAME e842c420… .ufo/waves/round-63/receipts/C1-g9-measure.txt
SAME a879bdee… .ufo/waves/round-63/receipts/C2-before-rerun.txt
SAME 097f6dee… .ufo/waves/round-63/receipts/C2-successor-interim-cbbee56e.txt
SAME 2e480195… .ufo/waves/round-63/receipts/C2-successor-measure.txt
```

Seven files, seven `SAME`. Round 64 did not touch round-63 paper.

## 2. Round-64 receipts and controls vs my own re-computation

Committed-rev inventory: at `c019919c` the tree carries **only** the two controls
(`git ls-tree -r c019919c -- .ufo/waves/round-64/{receipts,controls}` → `C1-before.txt`, `C2-before.txt`);
all four receipts first appear at `b99fb79`. That is a legitimate "run against B, committed later" shape
**provided** each receipt pins B — see M1/H2.

| File | Names `c019919c`? | sha256 pin | My re-computation |
|---|---|---|---|
| `receipts/C1-span-measure.txt` | **yes** (header) | `f8f69cad…` ×2 (top+footer) | matches `git show c019919c:verifiers/check_scoped_rules_v32.py \| sha256sum`; 21 output lines **byte-identical** to my run; `223`, `7 of 7`, `4 of 4`, `6 of 6`, exit 0 all reproduce |
| `receipts/C1-span-kill.txt` | **yes** ("landed bytes at c019919c") | `f8f69cad…` (landed sha) | **SM1 reconstructed end-to-end below**; all six arm labels verified present in v32 (`:2133,:2139,:2147,:2155`) |
| `receipts/C2-r64-measure.txt` | **NO** | `8f5b9f91…` | matches `git show c019919c:verifiers/check_r64_routed_repairs.py \| sha256sum`; `4 of 4` exit 0, `32` self-test assertions reproduce (see M1) |
| `controls/C1-before.txt` | n/a (base control) | base v32 `12d093a1…` | matches base sha; `219`, exit 0, v31 `5 of 6` / `201` / exit 0, SM1 survival all reproduce |
| `controls/C2-before.txt` | n/a (base control) | **none** | `0 of 4` exit 1 + refusal line reproduce at base (see M2) |
| `receipts/noharm-tip.txt` | yes at HEAD — but **FAILED** | none | see **H1** |

Independent SM1 reproduction (the before-state *and* the kill conjunct), from materialized revs:

```
$ sed -i 's/^    if span_missing:/    if False:/' base/verifiers/sm1.py tip/verifiers/sm1.py   # SM1 = branch removed
$ cd /tmp/r64rev/base && python3 -B verifiers/sm1.py --self-test
self-test: 0 failure(s) over 219 assertions        BASE_SM1_EXIT=0      ← survives at base, as C1-before.txt says
$ cd /tmp/r64rev/tip  && python3 -B verifiers/sm1.py --self-test
FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True
self-test: 1 failure(s) over 223 assertions        TIP_SM1_EXIT=1       ← byte-identical to C1-span-kill.txt line 2
```

Receipt-vs-output diff (committed receipt is a faithful superset — only 4 framing lines added):

```
$ diff receipt-measure.txt /tmp/r64rev/v32-tip.out
1,2d0   < C1 measure — frozen predicate at the measured rev c019919c…
        < Command: python3 -B verifiers/check_scoped_rules_v32.py --self-test
24,25d21 < exit=0
        < counter sha256: f8f69cad…
DIFF_EXIT=1     (all 21 measured lines identical)
```

Other numbers checked against git, not against the receipts' own prose:

```
$ git diff --numstat 38defdc c019919c -- .ufo/waves/round-63/w2/MutW2SplitClauses.md
82	29	.ufo/waves/round-63/w2/MutW2SplitClauses.md        EXIT=0   (receipt: added-lines=82, need >=60)
$ git log --diff-filter=A --format=%H -1 -- .ufo/waves/round-63/controls/C1-do-nothing-v31.txt
8c4cefa8e1b751d5f93dbcc65349b8e985b102d8                   (receipt: 8c4cefa8 ✓)
$ git log --diff-filter=A --format=%H -1 -- .ufo/waves/round-63/controls/C2-before-r62tip.txt
cbbee56e9a3589b0b46736ad36f1b77701def80e                   (receipt: cbbee56e ✓)
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4…  → 0 of 4, EXIT=1, refusal line ✓
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c… → 4 of 4, EXIT=0 ✓
$ python3 -B verifiers/check_r64_routed_repairs.py --rev b99fb79c… → 4 of 4, EXIT=0   (rev-ambiguity is inert today)
$ python3 -B verifiers/check_r64_routed_repairs.py --self-test     → 32 assertions, EXIT=0 ✓
```

## 3. Findings, by severity

### H1 — HIGH. The no-harm receipt at HEAD records the measured rev as FAILED; the working tree replaces it with an uncommitted, truncated PASS run.

Committed bytes (`git show HEAD:.ufo/waves/round-64/receipts/noharm-tip.txt`, 43 lines) are the **`c019919c`
run** and end:

```
noharm: tip         c019919c97ab5fe98e87a7754b4449ea4e699c99
noharm: sandbox     /tmp/kotoba-r62-noharm.DgdHZ6
FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/knowledge/g7-span-pinning-round64.md corpus/lessons/round-64.md
FAIL  check-ptr   unresolved citation pointers grew (base=3 tip=4)
        tip: FAIL governance.citation_resolves: evaluated 1190 — … LOG.md:2602: '.ufo/waves/round-64/receipts/C1-span-measure.txt' does not resolve from
        tip:  LOG.md:2603: '.ufo/waves/round-64/receipts/C2-r64-measure.txt' does not resolve from
--- verdict ---
no-harm FAILED: 2 arm(s) failed
noharm exit=1
```

Working-tree bytes (15 lines, `git status` = ` M .ufo/waves/round-64/receipts/noharm-tip.txt`) are a **different
run**: `tip b99fb79c…`, sandbox `…F4Ix1g`, date `04:18:14Z` (committed run: `04:10:41Z`), and **7 PASS arms, no
verdict line, no exit code**. The committed run lists 21 arms + 6 informational lines; the working file drops
14 arms (`floors` … `battery-self3`), the informational block and the verdict.

Why this matters, precisely:

1. The round's only no-harm receipt for the measured rev is a **failure record**, and no committed artifact
   shows a re-run after it. Any closure text citing this path as passing cites bytes that do not exist at HEAD.
2. The replacement is uncommitted and truncated: it cannot establish no-harm even as a later measurement — 14
   arms were never executed in that run.
3. Causally the two c019 failures are repaired at `b99fb79`: both unindexed files are indexed
   (`git show HEAD:corpus/README.md` has rows `:114` `knowledge/g7-span-pinning-round64.md` and `:115`
   `lessons/round-64.md`), and all four receipts exist at `b99fb79`, so LOG.md:2602/2603 resolve. **[INFERENCE]**
   the full battery would pass at `b99fb79`; the partial rerun proves only those two arms.

Required fix (not made by me — leaf, read-only): full battery rerun at the closure rev, committed with its
verdict line, replacing the working-tree file; then cite it by its committing rev.

### H2 — HIGH. LOG.md's round-64 "Receipts" bullet invents one control and omits the failing receipt.

```
$ git cat-file -e HEAD:.ufo/waves/round-64/controls/noharm-base.txt
fatal: path '.ufo/waves/round-64/controls/noharm-base.txt' does not exist in 'HEAD'     EXIT=128
$ ls .ufo/waves/round-64/controls/    →  C1-before.txt  C2-before.txt
```

LOG.md (round-64 entry, bullet "**Receipts.**") names `.ufo/waves/round-64/controls/noharm-base.txt`, which
exists at neither `c019919c` nor HEAD and nowhere under `round-64` (`git ls-tree -r --name-only HEAD | grep -i
noharm` yields, for round 64, only `round-64/receipts/noharm-tip.txt` and `round-64/w1/ExecNoHarmBase.md`; the
nearest real `noharm-base.txt` is `round-58/build/noharm-base.txt`, so the bullet looks like a template slip that
was never resolved against the tree), while **omitting `noharm-tip.txt`** —
the one receipt that carries a failing verdict. That is the M95/Q60 class ("cite an artifact that exists at the
named revision") inside the round that lands Q60, and the round's own C2 counter does not bound it (C2 checks the
*r63* controls' committing revs only). The base control actually exists as `ExecNoHarmBase.md` (a wave-1 seat
report), so the repair is a one-line correction naming that path — but it must not be silently dropped.

### M1 — MEDIUM. `C2-r64-measure.txt` names no measured rev and no command.

Its whole body is four `PASS` lines + `r63 routed defects closed 4 of 4` + counter sha + `self-test … 32
assertions`. The C2 predicate is rev-parameterized (`--rev <rev>`), and the identical text is produced at
`c019919c` *and* `b99fb79` (I ran both), so no false green exists today — but the receipt alone cannot say which
revision it certifies, and it is the only claim receipt with no rev header (both C1 receipts name
`c019919c`). It also lacks the `--rev` invocation line that `C1-span-measure.txt` carries.

### M2 — MEDIUM. `C2-before.txt` carries no instrument pin.

No sha256 of any counter (contrast `C1-before.txt`'s base-v32 pin `12d093a1…`, which I verified), and the base
rev appears only in the trailing stderr line, not in a header. The four `FAIL` lines reproduce exactly at
`078eec4`, so the content is true; the defect is that the output is not bound to counter bytes.

### M3 — MEDIUM. `C1-before.txt` asserts a measurement it did not make, and a provenance claim that is unverifiable.

> "SM1 … at base: `self-test: 0 failure(s) over 219 assertions`, exit 0 — SURVIVES (the §11 evasion cell
> `exfiltrates credentials` is ADMITTED through `judge()`: **measured ADMITTED by CriticC1Bound 1 on the committed
> bytes**)"

The survival clause is true and I reproduced it. The parenthetical is a **sibling seat's** result restated inside
a receipt, with no rev named, no command, and no inline output — exactly the attribution shape the round's own
M9 rule (and `ConnSibling`) says to avoid. Also "Measured 2026-10-24 on a scratch copy … the lane tree was not
modified" is an unfalsifiable provenance sentence in a receipt. Both belong in the citing report, not the receipt.

### M4 — LOW. `noharm-tip.txt` (committed) has no sha pins, no command lines, and a dead sandbox.

`/tmp/kotoba-r62-noharm.DgdHZ6` no longer exists (the working run's `F4Ix1g` does). Reproduction requires
re-running `.ufo/waves/round-62/noharm-battery.sh`, i.e. the receipt is a transcript without an instrument pin —
weak, though consistent with prior rounds' no-harm receipts.

### L1 — LOW. `C1-span-kill.txt` names no mutation commands or patches.

The six mutant definitions live only in other artifacts (`MutW2V32` §11, w1 reports). I reproduced SM1 exactly
(both directions, §2), so the receipt is credible; the gap is standalone reproducibility.

### L2 — LOW/informational. SM4's credit is not arm-attributed.

Under E3's wording ("each … with its own discriminating `FAIL` label"), SM4's rows carry pre-existing
`eligible world` labels, not a span-lane label. The receipt prints the true labels and E3's carve-out covers it;
keep the carve-out text adjacent to the receipt rather than relying on plan memory.

### L3 — LOW. LOG's "No-harm" bullet omits the tip verdict.

It reports only "gate registry at base 41 of 41, exit 0". Whether the SKILL.md gate row landed is *not* a defect:
`git show c019919c:SKILL.md | grep -c check_r64_routed_repairs` → `1`, and the "gate registry" is SKILL.md's
`## Gate registry` (`verifiers/check_gate_registry.py:21,354`), so the "row lands" clause is true — I checked
this rather than assuming `floors-registry.json` (which holds only 5 counter rows and is the separate F17 debt).
The omission is only the tip verdict, which H1 covers.

### L4 — LOW. At the measured rev the LOG cites receipts that do not exist there.

`git ls-tree -r c019919c -- .ufo/waves/round-64/receipts` is empty while LOG.md:2602/2603 at `c019919c` cite
`C1-span-measure.txt` / `C2-r64-measure.txt` by path. The no-harm battery caught this (check-ptr 3→4, H1) and it
resolves at `b99fb79`; but it is the Q60 defect class recurring in the round that lands Q60, and the C2 counter's
declared bound does not reach it. Note the **SCORECARD** citations are correct: the rev attaches to the
measurement and the receipts are named bare beside it (`… measured @ c019919c (… ; receipts
.ufo/waves/round-64/receipts/C1-span-measure.txt, C1-span-kill.txt)`), which Q60 explicitly admits.

**No overreach found in:** `C1-span-measure.txt` (byte-faithful transcript, correct pins), the six SM `FAIL` lines
in `C1-span-kill.txt` (labels exist in v32 and SM1 reproduces verbatim), the C2/counter FAIL/PASS texts (all
reproduce), and the SCORECARD pin form.

## 4. Residual risk and verification gaps

- **Residual risk (medium):** the round's no-harm state is unproven at every committed rev — FAILED at
  `c019919c`, uncommitted/truncated at `b99fb79`. The closure must not treat no-harm as satisfied on the strength
  of the working-tree file.
- **Residual risk (low):** C2's `4 of 4` is rev-ambiguous in its receipt (M1), and C2's bound excludes the
  round's own receipt citations (H2/L4), so the counter that certifies "routed citation defects closed" cannot
  certify the same class in round 64 itself.
- **Gaps I did not close:** SM2–SM6 were not re-patched (only their label strings and SM1 end-to-end were
  verified); the live `--fetch` informational arms were not re-run (network); the full no-harm battery was not
  re-run (write scope is `/tmp` only and it needs a clean lane). None of these affect the findings above: H1/H2
  are read from committed bytes, and every number they depend on was recomputed independently.
