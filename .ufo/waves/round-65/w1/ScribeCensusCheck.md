# ScribeCensusCheck — round 65, W1: census receipts (before/after) verification

Seat: scribe, leaf member (no subagent dispatch). Mode: read-only outside this file; no git/jj
writes, no product-code edits, no dispatch. All scratch under `/tmp/censusprobe`. No tool
installed or upgraded (pacman pause respected; nothing was needed). Date 2026-10-24.

Scope (assignment): verify `census-before.txt` and `census-after.txt` are committed, both
exit 0, before = 118 rows / after = 119 rows, W04 = 16 in both, and the census command's
output format matches CORPUS.md's frozen manual census section.

Rev map used: base `c98d1378236b` (r64 close), implementation `80bb89211841`, receipts
`5253b28174a1`, frontier `0e104f498b3d` (round-65 tip), live lane tip `2d2a13cdcd65`
(round-66 commits on top). Lane `corpus/SOURCES.md` sha256: base `4808eb37…`, frontier
`f5f463fa…`, live `02d643da…`.

## Gates

| # | Gate | Result |
|---|---|---|
| G1 | Both receipts committed | **PASS** — before added by `2fdfc1f`, after added by `0e104f4`; both present at `0e104f4` and at the live tip, working-copy blobs == tip blobs |
| G2 | Both exit 0 | **PASS** — reproduced: exact base tree `rc=0`, exact frontier tree `rc=0`, live cited command `rc=0` (byte-identical to the committed after receipt) |
| G3 | before = 118 rows, after = 119 rows | **PASS** — maintained `census` mode: 118 @ `c98d137`, 119 @ `0e104f4` (live tip: 120, round-66) |
| G4 | W04 = 16 in both | **PASS** — 16 W04 lines in each receipt, 16 unique ids, and 16 W04 re-emitted by `validate` at each rev |
| G5 | Output format matches CORPUS.md frozen manual census | **PASS (with F5 nuance)** — frozen manual counts equal the CLI counts at all three revs; receipts are the CLI's documented validate TSV, which CORPUS.md places outside frozen v1 |
| G6 | Instrument itself sane | **PASS** — `sources-census.sh selftest`: 96 `killed`, 0 `SURVIVED`, `selftest ok`, rc 0 |

## 1. Committed (G1)

```
$ git ls-files --error-unmatch .ufo/waves/round-65/census-before.txt .ufo/waves/round-65/census-after.txt
.ufo/waves/round-65/census-after.txt
.ufo/waves/round-65/census-before.txt                      # rc=0

$ git log --diff-filter=A --format='%h %s' -- .ufo/waves/round-65/census-before.txt
2fdfc1f round-65: plan freeze + before-controls + S121 snapshot (...)     # 2026-10-24 02:42:52 -0300
$ git log --diff-filter=A --format='%h %s' -- .ufo/waves/round-65/census-after.txt
0e104f4 round-65: frontier step (S121 row + snapshot, ..., census-after 119 rows exit 0) (...)  # 03:10:39

$ git cat-file -e <rev>:.ufo/waves/round-65/<file>   # presence
2fdfc1fd7bed census-before.txt present_rc=0
2fdfc1fd7bed census-after.txt  present_rc=128     # absent at plan freeze (expected)
c98d1378236b census-before.txt present_rc=128     # absent at base (expected: round artifact)
c98d1378236b census-after.txt  present_rc=128
0e104f498b3d census-after.txt  present_rc=0

$ for r in 2fdfc1fd7bed 0e104f498b3d 2d2a13cdcd65; do ... blob-vs-worktree sha ...; done
2fdfc1fd7bed census-before.txt blob=90b8d516… SAME
0e104f498b3d census-before.txt blob=90b8d516… SAME
0e104f498b3d census-after.txt  blob=90b8d516… SAME
2d2a13cdcd65 census-before.txt blob=90b8d516… SAME
2d2a13cdcd65 census-after.txt  blob=90b8d516… SAME
$ git diff --stat 2d2a13cdcd65 -- .ufo/waves/round-65/census-before.txt .ufo/waves/round-65/census-after.txt
(empty; rc=0)
```

Both files are regular files (not symlinks), 1569 B, 17 lines, trailing newline,
sha256 `90b8d5167b04a35a8dd9a12ea1ff7ce088d6feb6e3ac661bf0dd55d134f698c3` **each**.
Ordering is consistent: freeze 02:42:52 < impl 03:01:30 < receipts 03:03:37 < frontier 03:10:39;
file mtimes 02:38:56 (before) and 03:08:08 (after) bracket the frontier commit.

## 2. Both exit 0 (G2)

The receipts themselves record no exit code and no row count — they are bare stdout bodies.
Exit codes were therefore re-executed, on **exact rev trees** extracted read-only with
`git archive` (no checkout, no jj write):

```
$ git archive c98d1378236b | tar -x -C /tmp/censusprobe/base
$ git archive 0e104f498b3d | tar -x -C /tmp/censusprobe/aftertree
$ sha256sum /tmp/censusprobe/base/corpus/SOURCES.md
4808eb378d8aa5909f2daa376aacf00cbcefdefa9769a507faf74b03889a10f4   # == base rev
$ sha256sum /tmp/censusprobe/aftertree/corpus/SOURCES.md
f5f463face501a9b38904e3d32a2e89667a26e5189e031d16070fb92e336c954   # == frontier rev

$ bash scripts/sources-census.sh validate --today 2026-10-24 --file /tmp/censusprobe/base/corpus/SOURCES.md
rc=0   lines=17   W04=16   stderr=[]
$ bash scripts/sources-census.sh validate --today 2026-10-24 --file /tmp/censusprobe/aftertree/corpus/SOURCES.md
rc=0   lines=17   W04=16   stderr=[]
```

Label-faithful reproduction of the cited command (the plan and the report both cite
`validate --root /home/vgpnk/Projects/shokunin kotoba`, which resolves lane `kotoba` via
`shokunin.conf:50 kotoba|kotoba-shokunin|…`):

```
$ bash scripts/sources-census.sh validate --today 2026-10-24 --root /home/vgpnk/Projects/shokunin kotoba
rc=0
<16 W04 lines, then:>
kotoba	ok	/home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md
$ diff /tmp/censusprobe/live-validate.out .ufo/waves/round-65/census-after.txt
(no output)  → BYTE-IDENTICAL to the committed after receipt
```

Base-state reproduction with the same lane label used a synthetic fleet root
(`/tmp/censusprobe/root-before/shokunin.conf` lane `kotoba|kotoba-shokunin`, lane body a
symlink farm to the live lane, `corpus/SOURCES.md` the exact base bytes): `rc=0`, 16 W04,
and the body equals the committed `census-before.txt` **except** the `ok`-line absolute path
(`/tmp/...` instead of the real lane root). Same result for the after state. The exact-tree
`--file` runs above do not use symlinks at all, so used-by resolution there is the rev's own
tree.

## 3. Row counts 118 → 119 (G3)

`validate` mode does not print row counts; `census` mode does (script header, lines 20–27):

```
$ bash scripts/sources-census.sh census --today 2026-10-24 --file /tmp/censusprobe/base/corpus/SOURCES.md
file	rows	118
file	tier.A	115      file	tier.B	2      file	tier.C	1
file	status.mined	110   file	status.queued	7   file	status.rejected	1
FLEET	rows	118 … FLEET	missing	0
rc=0
$ bash scripts/sources-census.sh census --today 2026-10-24 --file /tmp/censusprobe/aftertree/corpus/SOURCES.md
file	rows	119
file	tier.A	116      file	tier.B	2      file	tier.C	1
file	status.mined	111   file	status.queued	7   file	status.rejected	1
FLEET	rows	119 … FLEET	missing	0
rc=0
$ bash scripts/sources-census.sh census --today 2026-10-24 --file corpus/SOURCES.md   # live tip
file	rows	120   (tier.A 117; status.mined 112; rest unchanged)   rc=0
```

The single-row delta 118→119 is S121 (`corpus/SOURCES.md:132` at the frontier rev), status
`mined`, matching the lesson's Status-changes line.

## 4. W04 = 16 in both (G4)

```
$ grep -c $'\tW04\t' census-before.txt census-after.txt
census-before.txt:16
census-after.txt:16
$ grep $'\tW04\t' census-after.txt | cut -f3 | awk '{print $1}' | sort -u | wc -l
16
```

Ids: S018 S019 S021 S054 S055 S056 S065 S086 S103 S104 S106 S110 S111 S114 S115 S118.
No `E`-coded finding appears in either receipt (`grep -cE $'\tE[0-9]+\t'` → 0 and 0), which is
why W-only `validate` exits 0 (header: "W-codes … never change status").
Both receipts are byte-identical, which is **expected**: S121's URL is unique, so the W04 set
is unchanged by the row addition. Consequence recorded as F2.

## 5. Format conformance to CORPUS.md's frozen manual census (G5)

The frozen manual census section is `/home/vgpnk/Projects/shokunin/CORPUS.md:131-148`
(heading + fenced `sh` block: rows / malformed / tier histogram / status histogram / duplicate
ids / enum violations / missing used-by, "run from the lane root"). The maintained CLI is
explicitly placed outside that frozen text by `CORPUS.md:150-154` ("Maintained parser note
(outside frozen v1) … the frozen manual census examples above assume column-zero input and
remain unchanged"). CORPUS.md is unmodified since 2026-10-19 (single fleet commit `6a1dd8c`,
sha256 `88556402…`), so this is the same frozen text the round measured against.

Conformance therefore means: the maintained CLI's census output must agree, row for row, with
what the frozen manual commands compute on the same file. It does, at all three revs:

```
frozen manual (run per file, cwd = rev tree for used-by):
                          base(c98d137)   frontier(0e104f4)   live tip
rows (grep -cE)                118              119              120
malformed (NF!=13)               0                0                0
duplicate ids               (none)           (none)           (none)
tier histogram          A=115 B=2 C=1    A=116 B=2 C=1    A=117 B=2 C=1
status histogram    mined=110 queued=7   mined=111 queued=7   mined=112 queued=7
                       rejected=1        rejected=1        rejected=1
enum violations             (none)           (none)           (none)
missing used-by             (none)           (none)           (none)
S-rows outside ## Registry       0                0                0
```

The last row matters: the manual `grep` counts every `S###` row in the file, while the CLI
counts only inside `## Registry` (rows elsewhere would be `E12`); with 0 rows outside the
section at every rev, the two definitions coincide and the equal counts are not a coincidence.
Missing-used-by was additionally checked with the frozen pipeline inside the exact archives
(`cwd=/tmp/censusprobe/{base,aftertree}`) — no output, i.e. no missing path.

The receipt lines themselves are the CLI's documented validate shape
(`lane<TAB>code<TAB>value`, script header lines 20–27): `kotoba<TAB>W04<TAB>S0NN duplicate url
<host/path> across scopes` and the clean-lane line `kotoba<TAB>ok<TAB><abs>/corpus/SOURCES.md`,
which is exactly `emit "$lane\tok\t$f"` for a W-only lane. The frozen manual section prescribes
no TSV shape, so literal output-format identity with it is not a meaningful test; semantic and
count identity is, and it holds. See F5.

## 6. Instrument identity (G6)

```
$ sha256sum scripts/sources-census.sh
3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30
GNU Awk 5.4.1, API 4.1 …   /   GNU bash, version 5.3.20(1)-release
$ bash scripts/sources-census.sh selftest
96 lines "killed", 0 "SURVIVED", "selftest ok"   rc=0   (1.34 s wall)
```

## Findings

- **F1 — evidence strength (low, not a falsification).** `validate` mode emits no row count and
  no `exit=` line, so neither receipt file can evidence "118 rows" / "119 rows" or its own exit
  code. The row figures are reproducible only with `census` mode. `plans/round-65.md:20-21` and
  `.ufo/reports/round-65/kotoba.md:30` cite the `validate` command and attach the row counts to
  it; the numbers are **correct** (I reproduced 118/119), but the cited command alone cannot
  show them. Round-62's receipt carried an `exit=` line (LOG.md:2559); round-65's do not.
- **F2 — evidence strength (low).** `census-before.txt` and `census-after.txt` are the same blob
  (`90b8d516…`). Expected (S121's URL is unique; the W04 set is unchanged), but it means the
  after receipt carries no observable delta from the before receipt, and cannot by itself prove
  it was produced after the S121 row landed. Ordering evidence is the commit that adds it
  (`0e104f4`, 03:10:39, after impl `80bb892`, 03:01:30) plus the row-count re-measurement above.
- **F3 — record location (informational).** The lane's round-65 LOG entry (`LOG.md:2616-2622`)
  contains only the C2 citation-correction bullet — no Frontier/census bullet. The SCORECARD
  round-65 annotation (`SCORECARD.md:381`) is depth/consistency only; the "Census: 16 W04
  before/after, both exit 0" sentence at `SCORECARD.md:387` belongs to **round-66**. The
  round-65 after-census claim is carried by the fleet report line 30 and the commit message of
  `0e104f4`. No contradiction, but the lane-local trail is thinner than the claim's reach.
- **F4 — rev scoping (informational, freshness).** At the live tip `SOURCES.md` is 120 rows
  (round-66 added S122, sha `02d643da…`). Round-65's 119 is rev-scoped to `0e104f4`; a reader
  running the cited command today sees 120. Both receipts are unmodified at the tip (blob
  equality), so the round-65 evidence itself has not drifted.
- **F5 — format (confirmed, with the nuance above).** Receipts are maintained-CLI validate TSV,
  not literal frozen-manual output; CORPUS.md:150-154 makes that the intended relationship.
  Frozen-manual and CLI counts agree exactly at base, frontier and live tip. No conflict found.

Nothing here falsifies the round's census claims; the two evidence-strength findings concern
what the artifacts alone can prove, not what is true.

## Claims supported / not touched

Supported: `plans/round-65.md:20-21` (before: exit 0, 16 W04, 118 rows); commit `0e104f4`
message ("census-after 119 rows exit 0"); `.ufo/reports/round-65/kotoba.md:30` (before exit 0 /
16 W04 / 118 rows; after exit 0 / 16 W04 / 119 rows; re-run exit 0); `corpus/lessons/round-65.md:44-46`
(before-state only; the lesson defers the after-state to the report, which carries it).

Not touched by this seat: C1 closing-package predicate, arms, floors registration; C2
`GOVERNANCE_CORRECTIONS` and the 1852→1862 checklist; S121's content/quote; sibling lanes; wave
dispatch; jj state.

## Out of scope

C1 kill battery, C2 11/11 checklist, assertion floors, no-harm battery, S121 re-open, wave
specs/payloads, any write outside this file.

## Artifacts

- This report: `.ufo/waves/round-65/w1/ScribeCensusCheck.md`
- Scratch (not committed): `/tmp/censusprobe/` — `SOURCES-before.md`, `SOURCES-after-0e104f49.md`,
  `base/` and `aftertree/` (exact `git archive` trees), `root-before/`, `root-after/` (roster
  reconstructions), `{base,aftertree,before,after}-validate.out`, `live-validate.out`,
  `selftest.out`, `*.cv` comparisons.

## Tooling

None installed or upgraded. Instrument used as found: `scripts/sources-census.sh`
(sha256 `3fb72615…`), GNU Awk 5.4.1, GNU bash 5.3.20.
