# RevW2SpecPrec

role: reviewer (attack: checks 2/3/5 precision — RevCalibChecks F6a–F6d)
item: (a) does a short-sha `3f911504` line pass check 2; (b) does check 3 match
`64`/`1044` with non-digit/non-hex boundaries on an appended-suffix line only;
(c) are check 2/3/5 matches scoped to appended suffix lines; (d) is `36 of 38`
extracted from the reg_gate diagnostic line of noharm-tip.txt.
Lane tip attacked: `cbbee56e9a3589b0b46736ad36f1b77701def80e` (jj-colocated;
all probes on /tmp copies or synthetic /tmp repos — zero lane writes).

## Baseline receipts (re-run, verbatim)

```
$ python3 -B verifiers/check_r63_routed_repairs.py --rev cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS late-write-tracked   tracked at cbbee56e9a3589b0b46736ad36f1b77701def80e
PASS receipt-rev-named    LOG names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a on 1 line(s)
PASS entry-size-named     LOG states 64 lines / 1044 words on 1 line(s)
PASS append-only          prefix=True grew_by=9 line(s)
PASS noharm-arms-named    LOG names reg_gate 36 of 38 + corpus-idx on 1 line(s)
r62 routed defects closed 5 of 5
exit=0

$ python3 -B verifiers/check_r63_routed_repairs.py --rev 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL late-write-tracked   not a tracked blob at 35d44b4b4dcdda234b5dbff7af37e432fec55f05
FAIL receipt-rev-named    LOG never names 3f911504ce76d9ca186f297d6d4a9cd8ed77508a
FAIL entry-size-named     LOG never states 64 lines / 1044 words for corpus/knowledge/erratum-absorption-round62.md
FAIL append-only          prefix=True grew_by=0 line(s)
FAIL noharm-arms-named    LOG does not name reg_gate 36 of 38 + corpus-idx
r62 routed defects closed 0 of 5
exit=1
```

Landed matcher surface (`verifiers/check_r63_routed_repairs.py`):
check 2 line 105 `token in line and "receipt" in line.lower()`; check 3 line 118
`ENTRY in line and str(lines) in line and str(words) in line`; check 5 lines
154–155 `"reg_gate" in line and "corpus-idx" in line and count_token in line` —
all three iterate `log.splitlines()` over the **whole** rev LOG (lines
104/117/153). No suffix cut, no token boundaries.

Real committed geometry (`wc -c`: base LOG 514498 B / 2566 lines; rev LOG
517352 B / 2575 lines; base ends `.\n`; suffix = 9 appended lines 2567–2575):
matched lines sit at rev lines 2570 (check 2), 2571 (check 3), 2573 (check 5) —
all inside the appended suffix.

## (a) short-sha `3f911504` on a correction line — check 2: **FAIL to pass (correct = PASS verdict)**

Probe (`/tmp/r63w2sp/probe.py`, landed `check_receipt_rev` on a synthetic repo
holding the real base LOG + real receipts + a 2-line appended correction block):

```
-- a-short-sha (rev 0d1fc819)      FAIL receipt-rev-named  LOG never names 3f911504ce76…
-- a-full-token (rev a8f45588)     PASS receipt-rev-named
-- a-embedded-hex (rev 385889be)   PASS receipt-rev-named  (line carries `<token>deadbeef99`, 50-hex)
```

The landed counter enforces the frozen wording "naming **that exact token**":
the 40-hex `receipt_rev=` must appear verbatim; the repo's short-sha convention
does not pass. The honest bytes at cbbee56e name the full token (rev line 2570:
`receipt_rev=3f911504ce76d9ca186f297d6d4a9cd8ed77508a`), and the landed
self-test independently asserts this (`receipt-rev: a short token does not
satisfy check 2`). **Verdict: PASS** — F6a's forced decision landed on the
full-token side, matching the plan. Bound: the test is substring containment,
so a line naming the token only inside a longer hex string (`<token>deadbeef99`)
also passes (probe `a-embedded-hex`).

## (b) boundaries on `64`/`1044` — check 3: **FAIL (defect)**

F6b recommended "the two numbers on a single appended-suffix line with
non-hex/non-digit boundaries." Landed code has neither clause: `str(lines) in
line and str(words) in line` is bare substring. Probe: appended line
`- Correction: corpus/knowledge/erratum-absorption-round62.md blob
ed41044b64dead.` — `1044` inside `ed41044b`, `64` inside `b64d` — states
**neither number**:

```
-- b-hex-boundary (rev 465dc493)   PASS entry-size-named  LOG states 64 lines / 1044 words on 1 line(s)
```

The base-LOG loci F6b named are real: base line 1793 carries `1044` inside
SHA `…ed41044b7a97ef19f2`; base line 1229 carries `64` as prose ("the full
64-lane dispatch", "64 items", "64 completed"). Neither also carries the entry
path, so they don't fire — the boundary hole is exploitable only on lines that
contain `corpus/knowledge/erratum-absorption-round62.md` (which today means
base line 2557 + appended lines). Same defect class, one line down the file:
check 5's `count_token in line` passes `136 of 381` (probe `d-count-boundary`:
line `… reg_gate corpus-idx re-run 136 of 381 arms.` → `PASS
noharm-arms-named`), and check 2's token passes inside a 50-hex string (above).

## (c) appended-suffix scoping — **FAIL (defect)**

Checks 2/3/5 iterate `log.splitlines()` over the entire rev LOG; nothing
intersects matches with the appended suffix that check 4 proves. Demonstrated,
all with real committed base bytes:

1. `c-base-line-credit` — appended suffix carries only `- bookkeeping only.`;
   ENTRY rewritten to 62 lines/62 words. Pre-existing **base** line 2557
   (`**R-b landed scope …**` — the only base line containing the entry path)
   carries `62` inside `round-62`: landed `check_entry_size` → `PASS … 62 lines
   / 62 words on 1 line(s)`. A check-3 pass credited to a line committed at the
   r62 tip, while `append-only` is honest (`prefix=True grew_by=1`).
2. `c-mid-insert` — a `64 lines / 1044 words` line inserted mid-file:
   `check_entry_size` → `PASS`, `append-only` → `FAIL`. Per-check credit never
   requires the match to be appended.
3. Check 2 vector exists in base: **59 base-LOG lines** contain `receipt` plus
   a 40-hex (lines 1437, 1464, 1485, …, 2538, 2552 — anchor scan in
   `/tmp/r63w2sp/probe2.py`). `C2-successor-measure.txt` is not
   append/invariant-guarded, so a rev rewriting `receipt_rev=` to any anchored
   token passes check 2 without an appended line naming it.
4. Check 5 vector is latent only: zero base-LOG lines contain `reg_gate` and
   `corpus-idx` together.

At cbbee56e the credit lands honestly — all three matched lines are in the
suffix (2570/2571/2573), so `5 of 5` stands on these bytes. The defect is
contract-level: per-check semantics are "any LOG line names the token," not the
plan's "appended correction line"; check 3's pass is demonstrably creditable
without any correction existing.

## (d) `36 of 38` extraction locus — **PASS**

Instrumented the landed regexes against `noharm-tip.txt` at cbbee56e:

```
reg_gate verdict line  : 'FAIL  reg_gate    expected exit 0 in both columns, got base=0 tip=1'
corpus-idx verdict line: 'FAIL  corpus-idx  tip leaves new corpus file(s) unindexed: corpus/lessons/round-61-verifier-spotcheck.md '
first `N of M` in block: '36 of 38' -> count_token='36 of 38'
verdict line `N of M`  : None
count lives on line    : '        tip: gate registry rows conformant 36 of 38 lane verifiers; phantom 0'
```

Exactly as F6d required: the count is pulled from the indented `tip:` diagnostic
line (receipt line 15) inside the block between the `FAIL reg_gate` (line 12)
and `FAIL corpus-idx` (line 17) verdicts; the verdict line itself carries no
`N of M` (`REG_COUNT_RE.search(reg.group(0))` → `None`). Bound: the extraction
is the *first* `\d+ of \d+` in the inter-verdict block — receipt-layout
dependent; fine for the frozen receipt bytes, brittle if the battery format
drifts.

## Smallest safe correction (verified against real + adversarial bytes)

One helper, one boundary regex, and suffix-scoping the three line scans —
fail-closed and exactly the F6b/F6c fix. Insert after `check_append_only`
(line 135):

```python
NUM_BOUND_RE = "0-9a-fA-F"


def _suffix_lines(root: Path, rev: str) -> list[str]:
    base = show(root, R62_TIP, LOG)
    log = show(root, rev, LOG)
    if base is None or log is None or not log.startswith(base):
        return []
    return log[len(base):].splitlines()


def _tok_re(token: str) -> "re.Pattern[str]":
    return re.compile(r"(?<![%s])%s(?![%s])"
                      % (NUM_BOUND_RE, re.escape(token), NUM_BOUND_RE))
```

Then replace the three scan bodies:

- check 2, lines 104–105 →
  `named = [line for line in _suffix_lines(root, rev)
           if _tok_re(token).search(line) and "receipt" in line.lower()]`
- check 3, lines 117–118 →
  `hits = [line for line in _suffix_lines(root, rev)
          if ENTRY in line and _tok_re(str(lines)).search(line)
          and _tok_re(str(words)).search(line)]`
- check 5, lines 153–155 →
  `named = [line for line in _suffix_lines(root, rev)
           if "reg_gate" in line and "corpus-idx" in line
           and _tok_re(count_token).search(line)]`

Verification of the proposed text (`/tmp/r63w2sp/probe2.py`, suffix computed
against the real base-LOG bytes — what check 4 guarantees):

```
== landed vs tightened (scope=base-suffix + hex boundaries) ==
real rev cbbee56e (honest bytes)       landed c2=True  c3=True  c5=True  | tightened c2=True  c3=True  c5=True
a-short-sha                            landed c2=False c3=False c5=False | tightened c2=False c3=False c5=False
a-full-token                           landed c2=True  c3=False c5=False | tightened c2=True  c3=False c5=False
a-embedded-hex                         landed c2=True  c3=False c5=False | tightened c2=False c3=False c5=False
b-hex-boundary                         landed c2=False c3=True  c5=False | tightened c2=False c3=False c5=False
c-base-line-credit (entry 62/62)       landed c2=False c3=True  c5=False | tightened c2=False c3=False c5=False
c-mid-insert (entry 64/1044)           landed c2=False c3=True  c5=False | tightened c2=False c3=False c5=False
d-count-boundary                       landed c2=False c3=False c5=True  | tightened c2=False c3=False c5=False
```

All honest suffix lines survive boundary tightening (rev line 2570 token
bounded by `=`…`)`, line 2571 `64 lines / 1044 words` and line 2573 `` `36 of
38` `` are non-hex-bounded), and the self-test's base/repaired/short-token/
count-swap arms are unaffected in direction: scoping only removes
non-suffix matches, and every self-test LOG edit re-appends the suffix. If the
L1 lands this, the docstring lines for checks 2/3 (lines 21/25, "an appended
line" / "one LOG.md line") should read consistently — e.g. check 3: "one line
of the appended LOG.md suffix must carry both numbers with non-hex boundaries
and the entry path." Scope bound stays: a correction naming the right tokens
with wrong prose still passes — the counter measures token linkage, not truth
of surrounding prose (docstring's declared bound), and the unguarded
C2-successor-measure.txt mutability (anchor-rewrite attack on check 2's token
*source*) is a separate residual: pin the receipt's `receipt_rev` to the r62-tip
value or hash-pin the receipt file if invariance beyond LOG is wanted.

## Verdict

ATTACKS on (b) and (c) landed: check 3's match is boundary-free and all three
token checks scan the whole LOG — a check-3 PASS is creditable to a
pre-existing base line with no correction written (probes above). (a) and (d)
PASS as committed. None of the findings flip the committed-bytes verdict —
`5 of 5` at cbbee56e is honest, and the do-nothing control `0 of 5` holds — but
the per-check contract is weaker than the plan's "appended correction line"
wording; the verified patch above tightens it without moving either measured
output.

## Method notes / tooling

Lane files accessed read-only via `git show <rev>:<path>` into `/tmp/r63w2sp/`;
synthetic repos built with `git init`/`commit` in `/tmp` (wave-1's receipt-free
method; `R62_TIP` absent there is expected — `append-only` FAILs in synths are
environment, not signal, and the tightened-eval suffix used real base bytes).
Probes: `/tmp/r63w2sp/probe.py`, `/tmp/r63w2sp/probe2.py`,
`counter.py` = byte-copy of the landed script. lsp device unavailable in this
lane toolchain — citations are line-numbered `grep`/`read` output on committed
bytes. No tools installed or upgraded this run (system `python3`, `git`,
coreutils); nothing needed beyond the authorized channels.
