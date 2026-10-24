# MutW2C2Counter

role: mutation tester (UFO-FSD) — one probe: do the landed C2 counter's *per-check* logic
kill MutCalibInstrument's five mutants, independently of the headline?
item: rebuild MutCalibInstrument's five mutants (M1 worktree read for check 1, M2 literal-token
comparison instead of reading the receipt, M3 hardcoded 64/1044, M4 line-count-only growth check,
M5 grep `36 of 38` anywhere in LOG) against the **committed** counter at `cbbee56e`, run each on
base `35d44b4b` and tip `cbbee56e` with transcripts, report which mutants change any check's
outcome, and propose the minimal per-check kill assertions for the counter's self-test.

Lane read-only: the only lane write is this file. All probes ran in `/tmp/mutw2c2`
(`repo` = a **full** `git clone --no-local` of the lane, no alternates; `mut/` = the mutants;
`patched_counter.py` = the patched copy). Net: lane `git rev-parse HEAD` =
`cbbee56e9a3589b0b46736ad36f1b77701def80e` before and after; lane
`verifiers/check_r63_routed_repairs.py` sha256 `5a15feac…` before and after; lane
`git status --porcelain` unchanged (only the pre-existing untracked r63 dispatch files);
lane `git for-each-ref` = 738 refs, **none** named for a probe/fixture rev.

## 0. The committed bytes under test

`verifiers/check_r63_routed_repairs.py` at `cbbee56e` — sha256
`5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec`, 373 lines. The
worktree copy is byte-identical to the committed blob, so the worktree and the commit agree.

Baseline (lane root, unmodified):

```
$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
exit=1

$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0

$ python3 -B verifiers/check_r63_routed_repairs.py --self-test
self-test: 0 failure(s) over 15 assertions
exit=0
```

The committed counter is materially stronger than the draft MutCalibInstrument probed: it
already reads the receipt's token (`RECEIPT_REV_RE`), computes the entry size from the blob,
keeps the byte-prefix conjunct, reads the count out of the no-harm receipt, and **has four
substitution arms** in its self-test (`:317` entry-size, `:324` short-token, `:330` count-swap,
`:304` rewrite). Those arms were absent from the draft. So the question is not "are the five
mutants killed?" but "which survive the *landed* per-check logic, and at what granularity?"

## 1. The five mutants, rebuilt against the committed bytes

Each mutant replaces exactly one expression in the committed file (anchors verified present
before substitution); all other bytes are identical, so the mutant is the committed counter
minus one check's semantics. Mutant hashes:

```
6d67c13a40521158b4d7c06266d5547bf9ed02fa3da45afbcd5b37d707153956  M1.py   (check 1 reads the WORKTREE)
6d999e7fe669d986ffcfcdad33ec3e5b6fc2065d14340fea3b5a7cb14097303a  M1b.py  (check 1 reads the ABSOLUTE LANE path)
aafee0d7f36dc1cc5f54d1e105216be6144032129cbbaa38ba14d215200f82d0  M2.py   (literal token; receipt-presence guard KEPT)
ee13647dcf30c18a934bf1941117b813d69ffbf187181244f7d0f7cf0bf1d93e  M2s.py  (literal SHORT token "3f911504")
d3217c5510dc80732ff7a065ef41bd8ca00ef779940751c918102976a4651d10  M2b.py  (literal token; receipt NEVER READ)
4b916e1d5421dd967a1071261b7f0fa0cf8d78030c9d40747c9f2e3d06e8c610  M3.py   (hardcoded 64 / 1044)
0c126a1bdfee4261b76ecc4d69afff9fcaa6e26207ebfd3db7eba0049fc0e8e1  M4.py   (line-count-only growth check)
c49303b19f7fa90616df5ad6e0fdc9cac49faa893d3f3664c229f60c0a9fa73b  M5.py   (grep "36 of 38" anywhere in LOG)
2d4d99c8004360440efbfaa61c34c88d54c4a655ec43fa42ca0791e5595ee042  M5b.py  (grep "36 of 38", arm classes still required)
```

## 2. Transcript: base `35d44b4b` and tip `cbbee56e`

Run with `--root` = the isolated `/tmp/mutw2c2/repo` clone, worktree checked out **at the
revision being measured** (so the worktree carries no extra state):

```
### BASE rev, scratch worktree CHECKED OUT AT BASE (LATE absent on disk)
HONEST: r62 routed defects closed 0 of 5 exit=1
  M1   r62 routed defects closed 0 of 5 | FAIL late-write-tracked   worktree has no .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
  M1b  r62 routed defects closed 1 of 5 | PASS late-write-tracked   lane worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
  M2   r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M2s  r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M2b  r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M3   r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M4   r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M5   r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
  M5b  r62 routed defects closed 0 of 5 | FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05

### TIP rev, scratch worktree CHECKED OUT AT TIP
HONEST: r62 routed defects closed 5 of 5 exit=0
  M1   r62 routed defects closed 5 of 5 | PASS late-write-tracked   worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
  M1b  r62 routed defects closed 5 of 5 | PASS late-write-tracked   lane worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
  M2   r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M2s  r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M2b  r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M3   r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M4   r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M5   r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
  M5b  r62 routed defects closed 5 of 5 | PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
```

Running the same nine against `--root` = the **lane** (dirty worktree, `LATE` present on disk)
reproduces the same picture: at base, M1 and M1b print `1 of 5` (they read the worktree) while
honest prints `0 of 5`; every other mutant prints `0 of 5` at base and `5 of 5` at tip.

**Headline verdict on the two frozen revs:** the two named revisions are a **do-nothing
control pair**. At `35d44b4b` and `cbbee56e` the real measured values coincide with the
mutants' hardcoded values (the receipt's token at base *is* `3f911504…`, the entry at base *is*
64 lines / 1044 words, the no-harm count at base *is* `36 of 38`), so **8 of 9 mutants print a
byte-identical headline to the honest counter at both revs**. The only headline that moves is
M1/M1b's `late-write-tracked` — and it moves for the wrong reason: not because the mutant
knows the tree, but because the worktree happens to hold the file. Nothing about the two frozen
revisions discriminates M2, M2s, M2b, M3, M4, M5 or M5b. This is a **coverage finding**, not a
contract defect: the plan's declared before/after pair is not a mutation-sensitive control.

## 3. Per-check discrimination on substitution fixtures (the real test)

To separate "the mutant is wrong" from "the mutant is indistinguishable at these two revs", I
built six fixtures in the isolated clone, each an **independent branch from `cbbee56e`** (the
first fixture build leaked state between fixtures and was discarded and rebuilt):

| fixture | rev | construction |
|---|---|---|
| `F_TOK` | `9cef4040e5befcef7af1a7292a05e8033fea1bb7` | the receipt's own `receipt_rev=` substituted (`cafebabe…`), LOG still names `3f911504…` |
| `F_NH` | `9247273a5697128a55a00899cd9cbbefe3767954` | the no-harm receipt's `36 of 38` → `37 of 38`, LOG still names `36 of 38` |
| `F_SZ` | `579fe8a25d2eafac2e71f7631d5f7a3a2021bcad` | the entry gains a line (66/1050), LOG still names 64/1044 |
| `F_RW` | `925363bc0387d416fb1984100b1b96f49f2e13d7` | an already-committed r62 LOG bullet rewritten in place (equal line count) |
| `F_EMPTY` | `8f106b456f1e83a27837bfc6810f9f0a057d0980` | the late-write blob truncated to 0 bytes |
| `F_LABEL` | `498bd06f186fd7bb7d57b964913480f8d3b7f486` | 1-byte blob + one appended LOG line carrying every literal |

Result — honest counter per fixture, then each mutant's per-check diff:

```
FIXTURE F_TOK   HONEST 4 of 5 (exit 1)
   FAIL receipt-rev-named    LOG never names cafebabecafebabecafebabecafebabecafebabe
   M2   5 of 5 exit=0  DIFF: ['receipt-rev-named']  honest=FAIL mutant=PASS | LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
   M2s  5 of 5 exit=0  DIFF: ['receipt-rev-named']  honest=FAIL mutant=PASS | LOG names 3f911504 on 1 line(s)
   M2b  5 of 5 exit=0  DIFF: ['receipt-rev-named']  honest=FAIL mutant=PASS | LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
   M1/M1b/M3/M4/M5/M5b:  DIFF: none

FIXTURE F_NH    HONEST 4 of 5 (exit 1)
   FAIL noharm-arms-named    LOG does not name reg_gate 37 of 38 + corpus-idx
   M5   5 of 5 exit=0  DIFF: ['noharm-arms-named']  honest=FAIL mutant=PASS | LOG names reg_gate 37 of 38 + corpus-idx on 1 line(s)
   M5b  5 of 5 exit=0  DIFF: ['noharm-arms-named']  honest=FAIL mutant=PASS | LOG names reg_gate 37 of 38 + corpus-idx on 1 line(s)
   M1/M1b/M2/M2s/M2b/M3/M4: DIFF: none

FIXTURE F_SZ    HONEST 4 of 5 (exit 1)
   FAIL entry-size-named     LOG never states 66 lines / 1050 words for corpus/knowledge/erratum-absorption-round62.md
   M3   5 of 5 exit=0  DIFF: ['entry-size-named']   honest=FAIL mutant=PASS | LOG states 64 lines / 1044 words on 1 line(s)
   all others: DIFF: none

FIXTURE F_RW    HONEST 4 of 5 (exit 1)
   FAIL append-only          prefix=False grew_by=9 line(s)
   M4   5 of 5 exit=0  DIFF: ['append-only']        honest=FAIL mutant=PASS | grew_by=9 line(s)
   all others: DIFF: none

FIXTURE F_EMPTY HONEST 4 of 5 (exit 1)
   FAIL late-write-tracked   tracked blob is empty at 8f106b45… (no evidence)
   M1   5 of 5 exit=0  DIFF: ['late-write-tracked'] honest=FAIL mutant=PASS | worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
   M1b  5 of 5 exit=0  DIFF: ['late-write-tracked'] honest=FAIL mutant=PASS | lane worktree has .ufo/waves/round-62/w2/FalsifyC2HonestH1.md
   all others: DIFF: none

FIXTURE F_LABEL HONEST 5 of 5 (exit 0)   <-- the honest counter accepts the label-only tree
   M1/M1b/M2/M2s/M2b/M3/M4/M5/M5b: DIFF: none
```

**Per-check verdicts (the item's actual question).** Every one of the five mutants is killed
by the landed counter's *per-check* logic — each is caught by a distinct check, on a fixture
where the mutant flips exactly one PASS to a FAIL and every other check is unchanged:

| mutant | killed by | check that flips | verdict |
|---|---|---|---|
| M1 (worktree read) | `F_EMPTY` (and the self-test's worktree + zero-byte arms) | `late-write-tracked` | **KILLED** |
| M1b (absolute lane path) | same | `late-write-tracked` | **KILLED** |
| M2 (literal token) | `F_TOK` | `receipt-rev-named` | **KILLED** |
| M2s (short literal) | `F_TOK` | `receipt-rev-named` | **KILLED** |
| M2b (receipt never read) | `F_TOK` | `receipt-rev-named` | **KILLED** |
| M3 (hardcoded 64/1044) | `F_SZ` | `entry-size-named` | **KILLED** |
| M4 (line-count only) | `F_RW` | `append-only` | **KILLED** |
| M5 (grep literal) | `F_NH` | `noharm-arms-named` | **KILLED** |
| M5b (grep literal + arm classes) | `F_NH` | `noharm-arms-named` | **KILLED** |

So the landed counter's check bodies are **sound** for all five mutants: each reads the
authoritative bytes at `<rev>` rather than a literal. That is a real improvement over the
draft MutCalibInstrument probed.

## 4. But the landed **self-test** does not kill all of them

The mutants also carry the counter's own self-test, so running `--self-test` on each mutant
asks whether the committed test suite catches the defect:

```
### HONEST committed counter --self-test
self-test: 0 failure(s) over 15 assertions
exit=0

M1   exit=1  KILLED    | FAIL worktree: an untracked copy on disk leaves check 1 red: got True, expected False; FAIL late-write: a zero-byte tracked blob fails check 1: got True, expected False
M1b  exit=1  KILLED    | FAIL worktree…; FAIL base: late write is not tracked; FAIL base: the do-nothing control scores 0 of 5: got 1, expected 0; FAIL late-write…
M2   exit=0  SURVIVED  | self-test: 0 failure(s) over 15 assertions
M2s  exit=1  KILLED    | FAIL receipt-rev: a short token does not satisfy check 2: got True, expected False
M2b  exit=1  KILLED    | FAIL shortcut: a LOG naming a constant fails without the receipt: got True, expected False
M3   exit=1  KILLED    | FAIL repaired: all five checks pass: got {… 'entry-size-named': False …}; FAIL repaired: the counter scores 5 of 5: got 4, expected 5
M4   exit=1  KILLED    | FAIL rewrite: a rewritten LOG fails the prefix conjunct: got True, expected False
M5   exit=0  SURVIVED  | self-test: 0 failure(s) over 15 assertions
M5b  exit=0  SURVIVED  | self-test: 0 failure(s) over 15 assertions
```

**M2 and M5 (and M5b) survive the committed self-test.** The reason is precise and is a
*coverage* gap, not a broken check body:

- The self-test's check-2 arm (`:324`) substitutes the **LOG's** token (`3f911504…` → `3f911504`),
  so it proves the check rejects a *short* token. It never substitutes the **receipt's** token,
  so it never proves the check *read* the receipt. M2 hardcodes the receipt's own value
  (`3f911504ce76…`), so it satisfies every arm the self-test poses.
- The self-test's check-5 arm (`:328`) substitutes the count in the **LOG** (`36 of 38` →
  `37 of 38`), so it proves the check rejects a *mismatched* count. It never substitutes the
  **no-harm receipt's** count, so M5's hardcoded `36 of 38` satisfies it. M5b likewise.

In both cases the substitution is applied to the wrong side of the relation. The committed
self-test verifies the LOG side and leaves the receipt side unverified — which is exactly the
side the check is supposed to read.

## 5. Minimal per-check kill assertions (proposed)

Two additional arms close the gap, and only two. Proposed text, to be inserted in
`self_test()` between the existing count-swap arm (`:330`) and the zero-byte arm (`:333`):

```python
            # M2 arm: the receipt's OWN token is substituted at the rev while
            # the LOG still names the original token.  The counter must read the
            # token out of the receipt at <rev>; a hardcoded literal must fail.
            _write(base, C2_RECEIPT, "measured\nreceipt_rev=%s\n" % ("cafebabe" * 5))
            _write(base, LOG, base_log + extra)
            token_swap_rev = _commit(base, "receipt-token-swap")
            check("receipt-rev: a substituted receipt token fails check 2",
                  check_receipt_rev(base, token_swap_rev)[0], False)

            # M5 arm: the no-harm receipt's reg_gate count is substituted at the
            # rev while the LOG still names the measured count.  The counter must
            # read the count out of the receipt at <rev>; a literal must fail.
            _write(base, NOHARM, (base / NOHARM).read_text().replace("36 of 38", "37 of 38"))
            _write(base, LOG, base_log + extra)
            count_swap_rev = _commit(base, "noharm-count-swap")
            check("noharm: a substituted receipt count fails check 5",
                  check_noharm(base, count_swap_rev)[0], False)
```

Verified against the patched copy (`/tmp/mutw2c2/patched_counter.py`, sha256
`82e1f5977e6d91656217bec46c1898dd7ea394c033452f0046f5be387930e0ad`):

```
### PATCHED honest --self-test
self-test: 0 failure(s) over 17 assertions
exit=0

M1   -> exit=1  KILLED    | FAIL worktree: an untracked copy on disk leaves check 1 red…
M1b  -> exit=1  KILLED    | FAIL worktree…; FAIL base: late write is not tracked; FAIL base: the do-nothing control scores 0 of 5…
M2   -> exit=1  KILLED    | FAIL receipt-rev: a substituted receipt token fails check 2: got True, expected False
M2s  -> exit=1  KILLED    | FAIL receipt-rev: a short token does not satisfy check 2…; FAIL receipt-rev: a substituted receipt token fails check 2…
M2b  -> exit=1  KILLED    | FAIL shortcut: a LOG naming a constant fails without the receipt…; FAIL receipt-rev: a substituted receipt token fails check 2…
M3   -> exit=1  KILLED    | FAIL repaired: all five checks pass…; FAIL repaired: the counter scores 5 of 5…
M4   -> exit=1  KILLED    | FAIL rewrite: a rewritten LOG fails the prefix conjunct…
M5   -> exit=1  KILLED    | FAIL noharm: a substituted receipt count fails check 5: got True, expected False
M5b  -> exit=1  KILLED    | FAIL noharm: a substituted receipt count fails check 5: got True, expected False
```

**All nine mutants killed; the honest patched counter still passes 17/17.** The patch touches
`self_test()` only — no check body, no frozen predicate, no headline. The patched counter
still measures the frozen revs identically:

```
### PATCHED counter at 35d44b4b
FAIL … (all five) / r62 routed defects closed 0 of 5   exit=1
### PATCHED counter at cbbee56e
PASS … (all five) / r62 routed defects closed 5 of 5   exit=0
```

## 6. Two further gaps the fixtures expose (coverage findings, not contract changes)

**(a) The counter accepts a label-only tree.** `F_LABEL` — a 1-byte blob plus one appended LOG
line naming every literal — scores **5 of 5** on the honest committed counter. Built from the
**base** instead of the tip (`F_LABEL2`, rev `2c1eb932a58098c4619d75da6dd2484f643daa1b`), a
tree whose LOG carries one line naming `receipt_rev=3f911504ce76…`, `64 lines / 1044 words`
and `reg_gate 36 of 38 … corpus-idx` also scores **5 of 5**:

```
### HONEST at F_LABEL2 (label-only tree from base)
PASS late-write-tracked   tracked at 2c1eb932a58098c4619d75da6dd2484f643daa1b
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=4 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0
```

The committed counter's check 1 has a **substance floor of "> 0 bytes"** (`:96-99` rejects a
zero-byte blob) but no floor on the *finding* the file is supposed to carry. The real H1
evidence at the tip is **10,224 bytes**, sha256 `6ccdc25b287840705bd5ca50856bb2d59d26d661855f4d3dad88b7944f91a4f2`,
and it contains `R-c` (14 hits) and `ancestry` (7 hits). `F_TINY` — that 10,224-byte finding
replaced by a 1-byte placeholder at the tip — still scores **5 of 5**:

```
### HONEST at F_TINY (1-byte placeholder for the H1 finding)
PASS late-write-tracked   tracked at 749bc1269b702dd9ee7c8b2d5797e79fba12ba47
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0
```

This is the same bound MutCalibInstrument reported, still open in the landed bytes. It is
arguably **outside** the counter's declared bound ("the counter binds these five named defects
and the two receipts it reads"; checks 2/3/5 are token linkage, per the docstring) — so the
honest reading is that this is a **bound to record, not a defect to fix**, unless the L1 wants
check 1 to require substance. A minimal, in-contract option that closes it without changing
the predicate's meaning: require the tracked blob to be non-empty **and** to carry the
evidence markers, e.g. `b"R-c" in blob and b"ancestry" in blob` — but that widens the counter
past its declared bound and is the L1's call, not this seat's.

**(b) Spot-check defect 2c is counted by no check.** `grep -n child verifiers/check_r63_routed_repairs.py`
→ `271: "- No post-report child commit exists.\n"`. The sentence exists only in the self-test
fixture text; no assertion consumes it, and `F_LABEL2` (which omits it entirely) still scores
5 of 5. The counter can print `r62 routed defects closed 5 of 5` with the child-commit claim
uncorrected. Same disposition as (a): a **recorded bound** (defects 1, 2a, 2b and 4 are
counted; 2c is not).

## 7. Verdict on the committed bytes

**The five mutants are all killed by the landed counter's per-check logic**, each by a
distinct check on a substitution fixture where it flips exactly one outcome and changes
nothing else (§3). The landed counter is materially stronger than the draft MutCalibInstrument
probed, and its check bodies do compute from committed bytes at `<rev>` rather than from
literals.

**Two gaps remain, both in the self-test, not in the checks:**

1. **M2 and M5 (M5b) survive the committed self-test** (§4). The check-2 and check-5 arms
   substitute the **LOG** side of the relation and never the **receipt** side, so a mutant
   that hardcodes the receipt's own value passes. The two-arm patch in §5 is minimal, verified
   to kill all nine mutants, and leaves the honest counter at 17/17 and the frozen revs at
   0 of 5 / 5 of 5. **This is the smallest safe correction** and is the one thing this seat
   would have the L1 apply.
2. **The two frozen revs are a non-discriminating control pair** (§2). 8 of 9 mutants print a
   byte-identical headline to the honest counter at both `35d44b4b` and `cbbee56e`, because the
   measured values at base coincide with the mutants' hardcoded constants. A reviewer who
   compares only the two headlines will conclude "all mutants pass"; only the substitution
   fixtures separate them. The self-test arms in §5 are what make the instrument
   mutation-sensitive without adding a third revision.

Two bounds should be **recorded rather than fixed** (they are outside the counter's declared
scope and fixing them would change the frozen predicate): the label-only tree scoring 5 of 5
(§6a) and spot-check defect 2c being counted by no check (§6b).

## 8. Restoration and isolation

- The lane's `verifiers/check_r63_routed_repairs.py` is byte-identical before and after:
  sha256 `5a15feac0358fd537ad3a54cad589fa5f41743971e02f9d3e742fa4c3528c6ec` (worktree and
  `git show cbbee56e:…` agree). No production file was edited.
- Lane `git rev-parse HEAD` = `cbbee56e9a3589b0b46736ad36f1b77701def80e` before and after;
  lane `git status --porcelain` unchanged (only the pre-existing untracked r63 dispatch files:
  `.ufo/waves/round-63/w2-dispatch.{err,json}`, `.ufo/waves/round-63/w2-spec.json`,
  `.ufo/waves/round-63/w2/`, `receipts.new-C1.txt`, `receipts.new-C2-interim.txt`); lane
  `git diff --stat HEAD` empty. The lane Git index and jj state were not touched.
- All mutants and fixtures live in `/tmp/mutw2c2` (mutants `mut/M*.py`, fixtures on branches
  `probe/fixtures`, `F_TOK`, `F_NH`, `F_SZ`, `F_RW`, `F_EMPTY`, `F_LABEL`, `F_TINY`,
  `F_LABEL2` inside `/tmp/mutw2c2/repo`). The clone is `git clone --no-local` — no alternates
  file, so no probe object is reachable from the lane's object store. The lane's 738 refs
  contain no probe/fixture rev (`git for-each-ref | grep -i "probe\|fixture"` → no match).
- No tools installed. `pacman`, `uv`, `npx`, `cargo` all untouched (the pacman pause honoured;
  no install was needed — `git`, `python3`, `grep`, `sha256sum` suffice).

## 9. Artifacts

- `/tmp/c2_committed.py` — the committed counter, sha256 `5a15feac…`, 373 lines.
- `/tmp/mutw2c2/mut/M{1,1b,2,2s,2b,3,4,5,5b}.py` — the nine mutants (hashes in §1).
- `/tmp/mutw2c2/patched_counter.py` — the §5 patch, sha256 `82e1f597…`.
- `/tmp/mutw2c2/repo` — the isolated clone holding the six substitution fixtures and the two
  label-only fixtures.
- `/tmp/mutw2c2/fixture_revs.txt`, `/tmp/mutw2c2/matrix.json` — fixture revs and the per-check diff matrix.
