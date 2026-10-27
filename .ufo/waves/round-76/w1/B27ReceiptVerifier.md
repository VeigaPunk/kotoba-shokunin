# B27ReceiptVerifier — Q36/Q50 receipt revision-naming check (kotoba round 76, wave 1)

Seat: `B27ReceiptVerifier` (executor). Item: write `.ufo/waves/round-76/build/check_receipt_revs.sh`,
run it over the receipts of rounds 73–76, save the run output to
`.ufo/waves/round-76/receipts/receipt-revs.txt`, and list the receipts that fail the check.

**Report only.** No claim data was written, no counter was frozen, no lane git/jj write was made,
no commit was made. Two files exist, both inside the lane repo and both named by this seat's item:
the script (`.ufo/waves/round-76/build/check_receipt_revs.sh`) and the receipt
(`.ufo/waves/round-76/receipts/receipt-revs.txt`).

## The check

Q36 (`corpus/QUALITY.md:47`): *"A no-harm or tip receipt cited in a report names the revision it
measured in the receipt itself (a printed `git rev-parse HEAD` or `--rev`/`--head` value); a report
line citing a revision no committed receipt names is struck, not kept."*

Q50 (`corpus/QUALITY.md:61`): *"Every gate result a report states for the lane tip has a committed
receipt that names that exact tip revision and the observed result; a result asserted only in prose
or a commit message, or covered only by receipts for another revision, is not tip evidence."*

A receipt file **passes** when it names a revision by one of:

- **(A)** a full 40-hex revision token standing alone — implemented as a *maximal* hex run of exactly
  40 characters, so a 64-hex sha256 and a 12-hex abbreviation both do not count; or
- **(B)** an explicitly marked `'<rev>'` placeholder (the literal angle-bracket token).

Verdicts are graded so a reader can see *how* the revision was named, and the grades are reported
separately rather than collapsed into a single pass/fail:

| tier | meaning |
|---|---|
| `MEASURED` | a 40-hex token sits on a line that also names a revision (`measured-rev`, `base`, `rev`, `head`, `tip`, `revision`, `--rev`, `--head`, `rev-parse`, `at …`) |
| `TOKEN` | a 40-hex token is present but no line carrying it names a revision — passes the literal rule, flagged **WEAK** because the 40-hex may be a sha256, a blob id or a sibling-lane head rather than the revision the receipt measured |
| `PLACEHOLDER` | no 40-hex token, but an explicitly marked `'<rev>'` placeholder is present |
| `ABBREV` | a revision-naming line carries an abbreviated hex rev (7–39 chars) but no full 40-hex — names *a* revision, not in the form Q36 asks for; reported separately from `FAIL` because it is a weaker defect |
| `FAIL` | none of the above: the receipt names **no revision at all** |

A runner script (`.sh` / `.py`) filed under `receipts/` is not itself a receipt — the revision
appears in the *output* it writes, not in the script text — so it is listed as `RUNNER-NO-REV` and is
**not** counted as a Q36/Q50 receipt defect.

Each receipt also carries a `committed` / `UNCOMMITTED` marker (`git ls-files --error-unmatch`), a
sha256 of its bytes, and the revision token found.

Exit status: 0 when no receipt FAILs, 1 when at least one receipt FAILs. The script is read-only —
it writes nothing; it only reads the lane tree and prints on stdout.

## Command and exit code

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ SELFTEST=1 .ufo/waves/round-76/build/check_receipt_revs.sh \
    > .ufo/waves/round-76/receipts/receipt-revs.txt 2>&1
EXIT=1
```

The exit code 1 is the check's own verdict (5 receipts FAIL), not a script error. The script's
`bash -n` parse check passes.

## Result — receipts that fail the check

**5 receipts fail** (name no revision at all):

| receipt | bytes | committed | what it actually contains |
|---|---|---|---|
| `.ufo/waves/round-73/receipts/c3-mutation-rerun.txt` | 4194 | committed | the M01–M15 mutation table (`KILLED` / `SURVIVED`, wall times, exits, sandbox paths). It names **no** revision; the only rev-ish text is prose ("absent at rev treated as empty rows", "base/rev") and the sole 16-hex token `6c87903c9c45f6a0`. |
| `.ufo/waves/round-73/receipts/census-before.txt` | 1940 | committed | only the census duplicate-url warning rows (`kotoba W04 S018 …`). A `grep -aiE 'rev\|commit\|base\|head'` over the file returns **zero** lines: no revision, no timestamp, no command line. |
| `.ufo/waves/round-74/receipts/c1-selftest-freeze.txt` | 5160 | committed | the counter's **sha256** (`bd34ec1b…59679d01`) and the self-test PASS/FAIL lines. The sha256 identifies the *instrument*, not the revision measured; no 40-hex rev and no `'<rev>'` placeholder. |
| `.ufo/waves/round-74/receipts/c2-selftest-freeze.txt` | 239 | committed | the counter's **sha256** (`9eee346e…12e2`) and `self-test: 0 failure(s) over 47 assertions`. Same defect shape as the c1 file above. |
| `.ufo/waves/round-76/receipts/fetch-recheck.txt` | 12926 | **UNCOMMITTED** | the r76 B26 fetch recheck (digest set, HTTP 200s, method). It names **no revision** — its digests are sha256s of page bodies, and it is also not committed at the time of the run. |

**1 receipt is `ABBREV`** (names a revision, but only in shortened form — weaker than Q36's ask):

- `.ufo/waves/round-74/receipts/c2-sandbox-data-2f7c860.txt` — `repo … rev 2f7c860aa83a base
  1e03d1991bc0` (12-hex abbreviations only; 4 abbreviated tokens, no full 40-hex). Its sibling
  `c2-data-559ee76a…txt` in the same directory names the full 40-hex, so the abbreviated form is an
  inconsistency inside one round's receipt set rather than a house style.

**1 file is `TOKEN`/WEAK** (passes the literal rule, but the 40-hex is not on a revision-naming line):

- `.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv` — its 40-hex tokens are the **20 sibling
  lanes'** heads (`7a2fcd4f…`, `00f8c7f5…`, …), not the kotoba lane's own revision. Verified: the
  string `kotoba` appears 0 times in the file and the lane's own r74 base
  `1e03d1991bc02281b00a5b7a5e00c9d5d5d72908` appears 0 times. A reader taking any 40-hex from this
  file as "the revision measured" would take a *sibling's* head. The freeze receipt
  `c2-base-freeze.txt` that consumes it *does* name the lane's revision, so the information is
  present in the round — but not in this file.

**Not counted as failures:** `.ufo/waves/round-76/receipts/tip-battery.sh` (6074 bytes, UNCOMMITTED)
is a *runner* — it prints the measured revision as its output's first line by design, so its own
script text need not carry one. Listed as `RUNNER-NO-REV` for transparency.

**Also flagged (advisory, Q50's "committed receipt" clause):** 4 receipts under
`.ufo/waves/round-76/receipts/` were **uncommitted** at run time — `census-before.txt`,
`d4-selftests.txt`, `fetch-recheck.txt`, `tip-battery.sh`. The first two name their revision
correctly; the third fails the naming check as well. This is expected mid-wave (the L1 lands the
wave), and it is recorded so the L1 can re-run the checker after landing.

## Totals

```
## summary
   receipts scanned: 37
   MEASURED 29 / TOKEN 1 / PLACEHOLDER 0 / ABBREV 1 / FAIL 5
   PASS (full 40-hex or marked <rev>) 30 of 37 ; FAIL 5 of 37
```

Population: round-73 15 files (10 MEASURED, 1 TOKEN/MEASURED, 2 FAIL, 1 code copy, …), round-74 20
files, round-75 **no `receipts/` directory at all** (its artifacts live in `w1/` and `w2/` as seat
*reports*), round-76 5 files at run time.

## Checker self-test (11 arms, all pass)

The check is not vacuous: `SELFTEST=1` drives the same verdict function over synthetic fixtures and
requires each bad shape to be rejected. `self-test failures: 0`.

```
PASS arm full-40-hex-named          expected PASS,   got PASS
PASS arm marked-placeholder         expected PASS,   got PASS
PASS arm no-rev-at-all              expected FAIL,   got FAIL
PASS arm abbrev-rev-only            expected ABBREV, got ABBREV
PASS arm sha256-not-a-rev           expected FAIL,   got FAIL
PASS arm 40-hex-plus-rev-word       expected PASS,   got PASS
PASS arm 40-hex-no-rev-word         expected PASS,   got PASS
PASS arm 39-hex-truncated           expected ABBREV, got ABBREV
PASS arm 41-hex-overlong            expected FAIL,   got FAIL
PASS arm unmarked-placeholder       expected FAIL,   got FAIL
PASS arm sha256-plus-abbrev-rev     expected ABBREV, got ABBREV
```

Note the `sha256-not-a-rev` arm: a bare 64-hex sha256 is rejected, which is the exact shape of the
two r74 self-test freeze receipts that fail. The `41-hex-overlong` arm rejects a 41-char run, so a
truncated or padded token cannot be laundered into a pass.

Determinism: two consecutive runs produce byte-identical output once the `# generated` timestamp and
`# lane HEAD` lines are excluded (verified by sha256 comparison of the two runs:
`c240bb6c548eb4707c7fec3e30df5649bdaadab46f46ee6b0eb19f4fd283f8ee` both times).

## Coverage appendix — reported, not counted

Q36/Q50 govern *receipts*, not seat reports. Round-75 has no `receipts/` directory; its round
artifacts are 128 seat reports under `w1/` and `w2/`. The same rule applied to those reports (for
context only; **not** added to the PASS/FAIL totals):

```
## .ufo/waves/round-75/w1 : files 64 | MEASURED 28 | TOKEN 1 | PLACEHOLDER 2 | ABBREV 4 | no-rev 29
## .ufo/waves/round-75/w2 : files 64 | MEASURED 55 | TOKEN 2 | PLACEHOLDER 0 | ABBREV 4 | no-rev 3
```

32 of 128 round-75 seat reports name no revision in any form. Most are prose-and-pointer facets
whose subject is historical evidence rather than a measurement, so the number is a coverage signal,
not a defect count. It is noted because the *r75 closure's* own R1 defect was a revision-bound
measurement (`corpus/lessons/round-75.md` correction, per the r76 plan § C2) — the population worth
watching is reports that assert a *measured* result, not reports that quote history.

## Caveats and limits (stated, not hedged)

- The check is **lexical**: it asks whether the revision is *named*, not whether the named revision
  is the one the receipt actually measured. A receipt naming a wrong-but-full 40-hex rev passes. The
  `MEASURED` / `TOKEN` / `ABBREV` grading exists to let a reviewer see the token in context.
- The `TOKEN`/WEAK tier is deliberately *not* a failure: the literal rule (a 40-hex rev is present)
  is satisfied, but the token may be a sha256 or a sibling head. `sibling-heads-freeze.tsv` is the
  concrete instance.
- The check reads the **working tree**, not a git object, so a receipt modified after its commit is
  graded on the bytes on disk. Every verdict line carries the file's sha256 so the graded bytes are
  pinned, and the header carries the lane HEAD observed at run time.
- Round-76's receipt population grew during the wave (`census-before.txt`, `d4-selftests.txt`,
  `fetch-recheck.txt`, `tip-battery.sh` appeared between runs; `fetch-recheck.txt` grew from 10068
  to 12926 bytes as its seat kept writing). The receipt records the population at its run time.
  **The L1 should re-run the script after landing the wave**; the numbers above are a mid-wave
  snapshot, not a final census.
- `round-75` has no `receipts/` directory. That is reported as an absence, not as a pass.

## Files written by this seat

| path | bytes | note |
|---|---|---|
| `.ufo/waves/round-76/build/check_receipt_revs.sh` | 14231 | the checker; read-only; `bash -n` clean; executable |
| `.ufo/waves/round-76/receipts/receipt-revs.txt` | 15575 | the run output (exit 1 = 5 receipt FAILs) |

Nothing else in the lane repo was created, edited or deleted. No git or jj command that mutates
state was run (read-only `rev-parse`, `ls-files`, `status`, `reflog` only). No tool was installed.
No scratch directory was created, so none needs removing.

## What the L1 should do

1. Re-run `SELFTEST=1 .ufo/waves/round-76/build/check_receipt_revs.sh` after the wave lands and
   after the round-76 receipts are committed, to get the final population and the final
   committed/uncommitted split.
2. Decide the disposition of the 5 failing receipts. The two r74 self-test freeze receipts and the
   two r73 receipts are historical (r73/r74) — the r76 plan's touch list does not include them, so
   they are most likely a recorded observation rather than a repair item. The r76 one,
   `fetch-recheck.txt`, is in-wave: its seat can append the measured revision, or the L1 can record
   it as a known exception.
3. Note the `sibling-heads-freeze.tsv` WEAK finding for the sibling-census area if a future round
   re-pins those heads.

**VERDICT: 5 receipts FAIL the Q36/Q50 revision-naming check
(`.ufo/waves/round-73/receipts/c3-mutation-rerun.txt`, `.ufo/waves/round-73/receipts/census-before.txt`,
`.ufo/waves/round-74/receipts/c1-selftest-freeze.txt`, `.ufo/waves/round-74/receipts/c2-selftest-freeze.txt`,
`.ufo/waves/round-76/receipts/fetch-recheck.txt`); 1 further receipt is ABBREV
(`.ufo/waves/round-74/receipts/c2-sandbox-data-2f7c860.txt`); 1 is rule-pass but WEAK
(`.ufo/waves/round-74/receipts/sibling-heads-freeze.tsv`); totals MEASURED 29 / TOKEN 1 / PLACEHOLDER 0 /
ABBREV 1 / FAIL 5 of 37 receipts scanned; checker self-test 11 of 11 arms pass.**
