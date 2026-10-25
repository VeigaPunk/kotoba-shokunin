# RevMistakes — § Mistakes review (round 69, wave 1)

Seat: `L1Kotoba69-2.RevMistakes` (reviewer). Read-only; no lane file edited.
Measured bytes: `corpus/lessons/round-69.md` sha256 `534f73489d837fa864bbb4ccc3198983cb6889e5e87c1b41321ac0f7285c8e06`, 9234 B, mtime 2026-10-25 07:17:50 -0300.
Branch tip at review: `a238989a96cb0d2b939679126b832d75b861ca6e` (plan commit). Base lane tip: `a5f7459f99bb27bf697e9438362e75ac5833eca8`.

Requirement checked per row: class, evidence pointer (resolves at the tip), captured-by (or `none`),
fix **shown able to fail**; M111 names R68-6 and S201; M112 names the clone's disposition.

## Verdict

| Row | class | evidence ptr | captured-by | fix able-to-fail | required names | verdict |
|---|---|---|---|---|---|---|
| M111 (`:112-119`) | yes | resolves | **`none` is wrong** | claimed, **claim false** | R68-6 yes / S201 yes, **not same line** | **defective** |
| M112 (`:120-126`) | yes | **two unresolvable refs** | yes (unpathed) | **absent** | disposition named, **path truncated** | **defective** |

Both rows are present and substantive; neither is missing. Both fail the round's own bar.

## Findings (severity-ordered)

### S1 — M112's disposition line cannot satisfy the frozen D7 conjunct
`corpus/lessons/round-69.md:126` writes the disposition as
`disposition: removed .../c2falsify-clone/` — an **ellipsis**, not the path. `check_r68_routed_repairs.py`
`d7_wave_paths` (`:281-295`) extracts tokens with

```
re.findall(r"disposition: removed `?([^`\s]+)`?", lesson)   # -> {'.../c2falsify-clone/'}
path = ".ufo/waves/round-68/w1/controls/c2falsify-clone/"   # R68_PATHS, :90
path in removed                                              # -> False
```

Reproduced two ways:
- direct probe on the live bytes: `D7 removed tokens: {'.../c2falsify-clone/'}`, expected path absent;
- end-to-end run on a read-only snapshot (`/tmp/r69rev/clone`, HEAD `0392cce6…`, `git clone --shared` of the
  lane plus the working-tree overlay): `r68 routed defects closed 4 of 8`, with
  `D7: .ufo/waves/round-68/w1/controls/c2falsify-clone/ is neither committed nor dispositioned`.
  (Isolating `d7_wave_paths` yields the same single clone finding; the 23 other paths are the expected
  pre-landing state and are not part of this finding.)

The counter's honest-world fixture (`:375-377`) defines the accepted shape: a column-zero
`disposition: removed `<full path>`` line. The row must spell the full
`.ufo/waves/round-68/w1/controls/c2falsify-clone/` (or drop the backticks/ellipsis consistently) for D7 to clear.
This is the row's own acceptance condition, so the disposition is not merely imprecise — it is inert.

### S1 — M111's "passes at the round-69 tip" is false; the row cannot satisfy D6 as written
`corpus/lessons/round-69.md:119-120` claims the fix "fails … at `a5f7459` (0 of 8) and passes at the
round-69 tip". Both halves do not hold as stated:
- **Base half is true** (credit): the counter at `a5f7459` prints `r68 routed defects closed 0 of 8`, exit 1,
  byte-identical to `.ufo/waves/round-69/controls/C2-base.txt`.
- **Tip half is false.** There is no round-69 tip; the only committed revision is `a238989a`, which predates the
  lesson. On the reviewed bytes the counter prints `4 of 8`, and one of the four is
  `D6: corpus/lessons/round-69.md § Mistakes has no row naming R68-6 and S201`.

Cause: `d6_mistake` (`:267-280`) requires **both tokens on one line**
(`any("R68-6" in l and "S201" in l for l in mistakes.splitlines())`). The row puts `R68-6` on `:112`
and `S201` on `:113`; the 80-column wrap splits them. Direct call on the live bytes returns the D6 finding;
the `Mistakes` section has no line carrying both. The counter's honest-world fixture (`:373`) uses the
same-line shape (`- M111 R68-6: the S201 refusal reason was wrong.`), so the accepted form is same-line.
Minimal remedy: put both ids in the row's first line, e.g.
`**M111 — class: a refusal whose reason is false (R68-6; S201 refusal).**`
No receipt in `.ufo/waves/round-69/` records `r68 routed defects closed 8 of 8` (grep over `controls/`
finds only base/junk/cheap controls), so the "passes" claim has no measurement behind it.

### S2 — M111 `Captured by: none` contradicts the corpus convention and this same file
`:117` says `Captured by: none (the refusal's stated reason was asserted, not observed)`. The parenthetical
restates the *class*, not a capture. The capture exists and is named by the row two entries down: R68-6 in
`corpus/lessons/round-68-verifier-spotcheck.md:179-184` ("The lesson's refusal of the staged S201 quote states
that the page does not carry the staged words … Mine this as a mistake row"). M112 (`:124-125`) uses exactly
that form for its own routed defect ("Captured by: the r68 closure's routed defect R68-7"). The r68 precedent
(`corpus/lessons/round-68.md:139-166`) likewise names the rule/instrument for every row. Either name R68-6 as
the capture or drop the parenthetical — `none` is the one answer that is false.

### S2 — M112 has no fix shown able to fail
`:125-126` opens `**Fix:**` and states intent ("each of the 24 paths is committed … or dispositioned as removed")
with no demonstration. This round's bar requires the fix *shown able to fail*, and M111's row (same section)
carries the `(shown able to fail)` label. The instrument exists: the counter's self-test has
`D7 untracked path left`, `D7 modified log kept its base blob`, `D7 removed path still tracked`
(`verifiers/check_r68_routed_repairs.py:437-439`) and the live run above exhibits the failing state. The row
should cite that pair — and the pair also exposes the S1 disposition defect: with the current lesson the
removed-clone arm's world is the red world, not the green one.

### S3 — M112's evidence/capture references have no resolvable path
`:122` "the r68 report's landed-changes row" and `:124` "the r68 closure's routed defect R68-7" are section
references, not pointers. Verified content, both true:
- the report row is **fleet** `ufo/reports/round-68/kotoba.md:32` (fleet root `/home/vgpnk/Projects/shokunin`),
  which says wave evidence `.ufo/waves/round-68/` landed at `2dd3567a…`; the lane repo carries no round-68 report;
- R68-7 is lane `corpus/lessons/round-68-verifier-spotcheck.md:184-191`.

Under Q58/Q61 (pointer must resolve in a declared resolution set) the row should name the lane path and
declare the fleet root for the report, as M111 does for its `round-68.md § Gate` and `ScoutMsAgentFramework.log:62-64`.

## Verified true (calibration credit)

- M111 class and routed id: `a refusal whose reason is false (R68-6)` matches R68-6's own text (wrong reason
  teaches the wrong lesson) and QUALITY Q62 (`corpus/QUALITY.md:78`, cites `round-69.md` — the counter's D6
  criterion arm is green).
- M111 evidence `corpus/lessons/round-68.md § Gate` supports the quoted ground: the r68 lesson says the page states
  the rule as a tool list "not with the staged words", i.e. a paraphrase — the spotcheck's wording.
- M111 pointer `.ufo/waves/round-68/w1/logs/ScoutMsAgentFramework.log:62-64` resolves at the tip and supports
  the claim: line 62 records the sentence appearing in earlier subsections, not in `Security best practices`;
  line 64 says `This anchor is WRONG`.
- M112's counts are exact: `git status --porcelain` under `.ufo/waves/round-68/w1/` gives 10 modified
  (1 draft + 9 logs) and 14 untracked, = 24; the clone is 269 MB (`du -sh`) and carries its own `.git`.
- M112's drift is confirmed at the **branch tip**, not just the dirty tree: the counter at `a5f7459` lists all 24
  (10 `carries the base blob`, 14 `neither committed nor dispositioned`).
- Q62 exists, is a `| Q62 |` row, and cites `round-69.md`; the counter self-test is green
  (`self-test: 0 failure(s) over 23 assertions`, exit 0), so the able-to-fail instruments for D5/D6/D7 are real
  — the rows cite them inaccurately, the counters are not missing.

## Residual risk / verification gaps

- **Clone still on disk.** The 269 MB tree is present at the moment of review while the row reads
  "dispositioned as removed". D7 accepts an untracked disposition, so the counter can pass with the artefact
  still sitting in the working tree — a reader of M112 would infer removal that has not happened. Not a counter
  breach; an inherited-state honesty gap for the round report (the M109 class it names).
- **No live re-fetch.** I did not re-open the Microsoft page; "verbatim on the page (twice)" is carried from
  S208/R68-6, not independently observed by this seat (out of scope here; `Scout*`/`ExecFetchArm` own it).
- **Snapshot caveat.** The `/tmp` run committed the whole working-tree overlay, so its `D8` (baseline
  `tracked_files 124 vs 127`) and `D3` (r67 counter still carries the literal `"checkout"`, at
  `verifiers/check_r67_routed_repairs.py:101`, inside a `/tmp` clone) are **not** findings of this seat and
  D8's numbers are expected to move at landing. They are cited only because they show the blanket
  "passes at the round-69 tip" claim is unsupported on the current bytes; C2's owners should judge them.
- `D1`/`D2`/`D5` were green on the snapshot (D5 confirms S208's anchor and the r68 entry's naming); their
  receipts are not re-verified here.

## Commands run (all read-only; no lane mutation)

```
git -C kotoba-shokunin status --porcelain; git -C kotoba-shokunin cat-file -e HEAD:<path>
python3 -B <counter> --self-test                      # 23 assertions, exit 0
python3 -B <counter> --rev a5f7459…                   # 0 of 8, exit 1 (matches controls/C2-base.txt)
git clone --shared kotoba-shokunin /tmp/r69rev/clone  # + rsync working-tree overlay, commit 0392cce6
python3 -B <counter> --repo /tmp/r69rev/clone --rev HEAD   # 4 of 8, exit 1 (D3, D6, D7, D8)
```
