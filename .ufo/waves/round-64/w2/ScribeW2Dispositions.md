# ScribeW2Dispositions — round-64 wave 2 (falsify): dispositions

Role: scribe (leaf member, no subagent dispatch). Item: draft the append-ready wave-2
rows for the round-64 lesson's `## Falsify corrections` table plus the Gate
census-after bullet, adjudicating the wave-2 attack themes from this seat's own runs
at the measured tip `c019919c97ab5fe98e87a7754b4449ea4e699c99` and at base
`078eec4a1f6a41c64ff8806f58b46a67cd413bfc`.

Bounds observed: read-only outside this file; no git/jj writes (all rev access via
`git show` / `git cat-file` / `git archive` / `git log`); scratch under `/tmp/sw2`
and the pre-existing `/tmp/mutspan64` (read only). Toolchain as found: `Python 3.14.8`,
`git version 2.56.0`. No tools installed or upgraded (pacman guard respected; none
needed). Worktree at filing: HEAD `b99fb79c27042e0f8a598cbbb4d81479a806b518`,
`git status --porcelain` = 2 lines — ` M .ufo/waves/round-64/receipts/noharm-tip.txt`
and `?? .ufo/waves/round-64/w2/` — neither authored by this seat (my only write is
this file). `verifiers/check_scoped_rules_v32.py` and
`verifiers/check_r64_routed_repairs.py` are byte-identical between `c019919c` and
`b99fb79c` (`git diff --stat` empty), so worktree runs are runs on the measured-tip
bytes.

Wave-2 peer reports were not available to read at drafting time: `ls
.ufo/waves/round-64/w2/` returned only `swarm-registry.json` (no seat reports yet), so
the rows below rest on this seat's measurements and are marked `<PENDING-SEAT …>`
wherever another seat's evidence is required.

## 1. Re-count — the two frozen predicates at tip and at base

### C1 at `c019919c` (tip bytes; worktree-identical)

```
$ python3 -B verifiers/check_scoped_rules_v32.py --self-test
counter sha256 f8f69cada703c8d821690fe01539b433afb7e92e9cdf1752b3365745a7d1113d
world W0: exit=1
worlds reject 7 of 7; eligible rows pass 4 of 4
survivor e2c-wrong-supersedes-target: before accepted; after rejected
survivor e2c-supersedes-with-fresh-fetch: before accepted; after rejected
survivor e2e-negated-path-key: before accepted; after rejected
survivor e2e-commented-equals-key: before accepted; after rejected
survivor e2f-backticked-event-claim: before accepted; after rejected
survivor e2f-compound-purpose-outside-citation: before accepted; after rejected
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 223 assertions
exit=0
```

All four frozen predicate lines are present, byte-for-byte, plus the `(sha256, 223)`
pair the receipt pins (`f8f69cad…`); zero `FAIL` lines. exit 0.

### C1 at base `078eec4`

The base file cannot run alone: `self_test()` imports a sibling
(`check_erratum_absorption.py`) relative to `__file__`. Isolated run observed:

```
$ python3 -B /tmp/sw2/base/verifiers/check_scoped_rules_v32.py --self-test
… FileNotFoundError: [Errno 2] No such file or directory:
  '/tmp/sw2/base/verifiers/check_erratum_absorption.py'
exit=1
```

Re-run with the whole `verifiers/` tree extracted at base
(`git archive 078eec4 verifiers | tar -x -C /tmp/sw2/basefull`), base file sha256
`12d093a1cdbba4e0c57437e79bc1121708f522f84f81d00a4343bbbbf4c70f43`:

```
$ python3 -B /tmp/sw2/basefull/verifiers/check_scoped_rules_v32.py --self-test
worlds reject 7 of 7; eligible rows pass 4 of 4
survivors closed 6 of 6
must-fail E2e guard disabled admits e2e-negated-path-key: yes
must-fail G7 disabled admits e2f-backticked-event-claim: yes
must-fail G9 disabled admits e2f-compound-purpose-outside-citation: yes
self-test: 0 failure(s) over 219 assertions
exit=0
```

Base prints the same four lines with `219` — it cannot reach the `223` predicate. This
is the declared do-nothing control, reproduced.

### C2 at `c019919c`

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev c019919c97ab5fe98e87a7754b4449ea4e699c99
PASS seat-edit-committed    marker=True added-marker=True added-lines=82 (need >=60)
PASS control-revs-named     round-64 LOG line names committed controls 8c4cefa8 + cbbee56e and base 35d44b4b
PASS lowest-axis-corrected  round-64 LOG suffix names depth 9 < consistency 10 as lowest
PASS assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; added patch line names 23 assertions
r63 routed defects closed 4 of 4
exit=0
```

### C2 at base `078eec4` (pinned control conjunct)

```
$ python3 -B verifiers/check_r64_routed_repairs.py --rev 078eec4a1f6a41c64ff8806f58b46a67cd413bfc
FAIL seat-edit-committed    marker=False added-marker=False added-lines=0 (need >=60)
FAIL control-revs-named     no round-64 LOG line names both committed control basenames, computed revisions, and computed base
FAIL lowest-axis-corrected  round-64 LOG suffix lacks lowest/depth/consistency and both computed scores
FAIL assertion-count-named  runtime 23 matches static 17 fixed + 2 loop sites x 3 arms = 23; no BASE_REV-added patch line names 23 assertions
r63 routed defects closed 0 of 4
the pinned do-nothing control at 078eec4a1f6a41c64ff8806f58b46a67cd413bfc is never a certification
exit=1
```

`verifiers/check_r64_routed_repairs.py` does not exist at base
(`git show 078eec4:verifiers/check_r64_routed_repairs.py` exit 128), so the base
conjunct is necessarily measured with the tip counter's `--rev` mode — which is what
the frozen sentence specifies. Both conjuncts hold; the refusal message prints.

## 2. Append-ready rows — lesson `## Falsify corrections` (wave 2)

Append below the wave-1 table (lesson lines 87–101) and below the existing note
"(Wave-2 rows append below this table post-wave-2.)". Letters continue the wave-1
sequence; each row names what it attacks.

```markdown
| m | **re-count**: both frozen predicates re-run on the landed bytes at `c019919c` and at base | `ScribeW2Dispositions` (w2) | **HELD (measured, this seat)** — C1 at `c019919c`: four frozen lines, `counter sha256 f8f69cad…`, `self-test: 0 failure(s) over 223 assertions`, exit 0; C1 at base `078eec4` (full `verifiers/` tree at the rev): same four lines, `219 assertions`, exit 0 — the control cannot reach 223. C2 at `c019919c`: four `PASS` lines, `r63 routed defects closed 4 of 4`, exit 0; C2 at base: four `FAIL` lines, `0 of 4`, exit 1, with the `never a certification` refusal line. Every frozen line is present verbatim; the tip output additionally carries the pre-existing `E2e`/`G7` must-fail lines, which the frozen block does not forbid. |
| n | **dishonest world**: a print-only substrate satisfies the C1 printed-line conjunct with zero pinning | `ScribeW2Dispositions` (w2); premise from `RevC1Predicate` Q1 | **line conjunct measured non-certifying; certification is composite** — a 4-statement substrate (`/tmp/sw2/printonly.py`, 0 `check(` calls) prints all four frozen lines and exits 0; so the four lines alone certify nothing. What bites is the receipt pin: `receipts/C1-span-measure.txt` names `counter sha256 f8f69cad…` and I recomputed exactly that sha256 from the landed bytes (`sha256sum`), plus E3.1's kill conjunct. Bound: the printed-line conjunct is satisfiable by a fake and must never be cited alone. |
| o | **mutation**: SM1 `span_missing = []` applied to the *landed* bytes (not the wave-1 reconstruction) | `ScribeW2Dispositions` (w2 / SM1); `<PENDING-SEAT R64MutIcon>` for SM2–SM6 + the r64-counter battery | **HELD for SM1 (measured, this seat)** — scratch copy sha256 `acb23eadf5b9a72c4bf1126c59041b1fe9c42be9aa68a8e22a57f1a6b3ccb380`, `python3 -B … --self-test` exit 1, `self-test: 1 failure(s) over 223 assertions`, and the single `FAIL` line is arm 1's own label: `FAIL A2 G7: a backticked span whose words occur in neither the cited line nor the page is rejected: got False, expected True`. The four other predicate lines still print (so the mutation is caught only by the assertion, as intended). SM2–SM6 and the counter mutants are another seat's receipt. |
| p | **substitution**: substituted derivation/receipt on the r64 counter (hard-coded count, look-alike line, repointed base) | `ScribeW2Dispositions` (w2) | **HELD on the counter's own constructed worlds (measured, this seat)** — `python3 -B verifiers/check_r64_routed_repairs.py --self-test` → `self-test: 0 failure(s) over 32 assertions`, exit 0; the substitution arm reports `hardcoded-count: substituted-source rc=0 count=4 want rc!=0 count<4` (i.e. the substituted source would pass, so the arm requires rejection), and the label-only / fingerprint / worktree-read `base`+`look-alike` arms all want `rc!=0 count<4` while `honest/*` target wants `rc=0 count=4`. Bound: this is a constructed-world result; no live look-alike LOG substitution at a real rev was run by this seat. |
| q | **census**: M95 `path@rev` class re-derived; SOURCES census-after re-run; the paper trail checked against the artifacts | `ScribeW2Dispositions` (w2); pair table from `ScoutReceiptSweep`; `<PENDING-SEAT ScoutW2CensusAfter>` for the committed after-census artifact | **class reproduces; paper trail MISMATCH (measured, this seat)** — all 10 unique pairs (15 sites per the wave-1 table) re-checked: every cited `rev:path` exits 128 at its cited rev, and `git log --diff-filter=A --format=%H -1` reproduces the wave-1 committing revs (`8e52f064`, `07c33d73`, `722e474a`, `f2f9ee1d`, `f9ab0812`, `f897d18a`, `d64d945b`, plus the two routed `cbbee56e`/`8c4cefa8`). But the round-64 LOG suffix (12 lines after the header at `LOG.md:2599`) contains **none** of the eight uncovered pairs' committing revs and none of their path basenames (`grep -c` = 0 for each of the 7 distinct revs and for the path-basename pattern), so row (i)'s "the 8 uncovered pairs named with their committing revs in the LOG census line" and lesson line 151's "13 census instances are repaired by the LOG census line" are **unsupported at `c019919c`**. Independently, `.ufo/waves/round-64/census-after.txt` exits 128 at both `c019919c` and `b99fb79c` while the round-64 LOG Frontier line asserts "after 16 W04 exit 0 (`census-before.txt` / `census-after.txt`)" — the named artifact is absent. My own SOURCES census reproduces the claimed numbers (see the Gate bullet below). |
```

## 3. Gate bullet — census (before → after), append-ready

```markdown
- **Census (before → after).** Before: `.ufo/waves/round-64/census-before.txt` —
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba` exit 0,
  16 W04 (117 rows). After (wave-2 re-run by the scribe at `c019919c`, 2026-10-24):
  `rows=118`, `malformed=0`, tier `A=115 B=2 C=1`, status `mined=110 queued=7 rejected=1`,
  no duplicate IDs, no enum/tier-inflation violations, every `mined` used-by path exists,
  `S120` present at `corpus/SOURCES.md:132` (`paper`, tier A), and the maintained gate
  `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
  exit 0 with 16 W04 (before = 16, after = 16; same count, rows 117 → 118).
  `.ufo/waves/round-64/census-after.txt` does not exist at `c019919c` or at `b99fb79c`
  (`git cat-file -e` exit 128), so the LOG Frontier line's parenthetical naming it is
  unsupported until the artifact is committed. `<PENDING-SEAT ScoutW2CensusAfter>` for
  the committed after-census artifact (the numbers above are this seat's substitute
  measurement, not the canonical file).
```

Verbatim supporting run (lane root, all from the frozen CORPUS.md block):

```
rows=118
malformed=0
tier: A=115 B=2 C=1
status: mined=110 queued=7 rejected=1
dups:
enum/tier-inflation violations:
S120 row:
132:| S120 | Practical Mutation Testing at Scale: A view from Google (Petrović, Ivanković, Fraser & Just) — https://arxiv.org/html/2102.11378 | paper | A | Primary peer-reviewed study for the clai
mined used-by paths missing: (empty) exit=0
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba
… kotoba W04 (16 lines) … kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
gate-exit=0
```

## 4. Findings

**F1 (HIGH, consistency — falsifies a landed wave-1 cell).** Row (i) of the lesson's
wave-1 `## Falsify corrections` table and lesson line 151 ("13 census instances are
repaired by the LOG census line + Q60") describe a LOG census line that does not exist
at the measured tip. Evidence: the round-64 LOG suffix is 12 lines (`LOG.md:2599` is the
header); `grep -c` for each of `8e52f064`, `07c33d73`, `722e474a`, `f2f9ee1d`,
`f9ab0812`, `f897d18a`, `d64d945b` in that suffix = 0; `grep -cE
"round-58/C1-measure|round-57/C1-measure|round-56/C1-measure|round-59/C1-measure|round-55/C2-measure|round-62/C1-absorb-measure|round-46/evidence"` in the suffix = 0; a whole-lane
search outside `.ufo`/`.git` finds those revs only in rounds 46–58/63 paperwork, never
in a round-64 census line. The *class* itself I confirmed (F4), so the repair content is
available — only the claimed landing is false.

**F2 (MED, M95-adjacent — named artifact absent).** `census-after.txt` is named by the
round-64 LOG Frontier line as carrying the after-census, but
`git cat-file -e c019919c:.ufo/waves/round-64/census-after.txt` and
`… b99fb79c:…` both exit 128 (`fatal: path … does not exist`). The lesson's Gate bullet
is honest to-do wording ("appended below when run"); the LOG line is not. This is the
same absence-at-rev shape as the M95 class, one round later, in this round's own entry.
My substitute run reproduces the numbers the LOG claims (F3), so the substantive claim
survives; the citation does not.

**F3 (measured, supports the Gate claim).** SOURCES census at `c019919c`: 118 rows,
0 malformed, tier `A=115 B=2 C=1`, status `mined=110 queued=7 rejected=1`, no duplicate
IDs, no enum/tier-inflation violations, every `mined` used-by path exists, S120 present
at line 132, validate gate exit 0 with 16 W04 (identical W04 count to the before run —
same count, one more row).

**F4 (measured, class reproduces).** All 10 unique M95 pairs are absent at their cited
revs and their committing revs reproduce the wave-1 table exactly:

```
78ee57e      .ufo/round-46/evidence/w2/gates/before-78ee57e/summary.txt   cited-exit=128  committing=f2f9ee1d88bc
e966cd59     .ufo/waves/round-55/C2-measure-e966cd59.txt                  cited-exit=128  committing=722e474ad242
ac22ca87     .ufo/waves/round-57/C1-measure.txt                          cited-exit=128  committing=07c33d73ddce
46b4a706     .ufo/waves/round-58/C1-measure.txt                          cited-exit=128  committing=8e52f064f215
46b4a706     .ufo/waves/round-58/noharm-tip.txt                          cited-exit=128  committing=8e52f064f215
3e7aed9b     .ufo/waves/round-62/C1-absorb-measure.txt                   cited-exit=128  committing=f9ab0812a574
35d44b4b     .ufo/waves/round-63/controls/C2-before-r62tip.txt            cited-exit=128  committing=cbbee56e9a35
c22fdd39     .ufo/waves/round-56/C1-measure.txt                          cited-exit=128  committing=f897d18ae9ec
c63ccc68     .ufo/waves/round-59/C1-measure.txt                          cited-exit=128  committing=d64d945b3435
35d44b4b     .ufo/waves/round-63/controls/C1-do-nothing-v31.txt          cited-exit=128  committing=8c4cefa8e1b7
```

The 15-instance-site count is the wave-1 table's; I re-derived the 10 unique pairs, not
the site count.

**F5 (measured, bounds the C1 predicate).** The printed-line conjunct is satisfiable
with zero pinning: `/tmp/sw2/printonly.py` (4 `print` statements, `grep -c "check("` = 0)
emits all four frozen lines and exits 0. Any future audit must cite the `(sha256, 223)`
receipt pair plus the kill conjunct, never the lines alone. [INFERENCE] This is exactly
the E3.1 hazard, still latent in the predicate's phrasing.

**F6 (measured, SM1 only).** SM1 on the landed bytes is killed by arm 1's own label at
223 assertions (see row `o`). I did not run SM2–SM6 or any counter mutant; row `o`
carries `<PENDING-SEAT R64MutIcon>` for the rest of the battery. Note that the SM1
scratch tree at `/tmp/mutspan64` is *not* reusable as-is: it was built on the pre-arm-4
wave-1 bytes (`7791504715f3…`), so I re-applied the mutation to the landed bytes
(sha256 `acb23ead…`).

**F7 (observed, not mine).** Worktree at filing carries a modified
`.ufo/waves/round-64/receipts/noharm-tip.txt` (in-flight sibling edit) and the untracked
`w2/` tree. I did not touch either.

## 5. Pending-seat ledger (what the rows still need)

| Row | Dependency | Needed evidence |
|---|---|---|
| `o` | `R64MutIcon` (or another wave-2 mutation seat) | SM2–SM6 exit codes + own-label FAIL lines on the landed bytes; r64-counter mutant battery |
| `q` | `ScoutW2CensusAfter` | committed `.ufo/waves/round-64/census-after.txt` (or the LOG Frontier parenthetical corrected instead) |
| `n`/`p` | any wave-2 dishonest-counter seat | a live look-alike substitution against a real rev (I ran only the counter's constructed worlds) |
| `m` | none — self-contained | — |

## 6. Scope, out-of-scope, verification

- Touched surfaces: this report only. No lane file, jj/git state, index, or sibling lane
  was written; no commit, push, publish, or deploy. Scratch: `/tmp/sw2/` (base and tip
  materializations, `printonly.py`, SM1 tree, `LOG-tip.md`) and read-only
  `/tmp/mutspan64/`.
- Out of scope (not attempted): re-opening S120's snapshot identity; the r64 counter's
  live-world mutation battery; the source/entry/SCORECARD/LOG edits themselves; any
  judgment or routing change.
- No build, test, lint, or formatter was run. Verification performed is exactly the
  commands pasted above with their exit codes; everything not pasted is marked
  `[INFERENCE]` or `<PENDING-SEAT …>`.

Report: .ufo/waves/round-64/w2/ScribeW2Dispositions.md
