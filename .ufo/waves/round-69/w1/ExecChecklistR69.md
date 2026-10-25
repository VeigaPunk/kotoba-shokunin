# ExecChecklistR69 — skill-checklist gate + independent corpus gate, round 69 wave 1

Seat: `L1Kotoba69-2.ExecChecklistR69` (leaf, no dispatch). **Verdict: RED.** Neither gate reaches exit
0 at the lane tip, and the L1's draft leaves gate A red for two independent reasons (one of them
pre-existing and owned by no claim) and gate B red until the round's own lesson is indexed. Every
cause is measured and a minimal repair set is proven in a sandbox: gate A `pass=11 fail=0 exit=0`,
gate B `exit 0`, integrity `9/9`, C1 `5 of 5`, C2 `8 of 8`, C3 `2 of 2`.

Two measurement instants, both against the lane's working tree, both in `git clone --shared`
sandboxes with the fleet root's `PROTOCOL.md`/`AXES.md`/`MISSION.md`/`SCORECARD.md`/`shared`/`.ufo`/
`kasegi-shokunin` symlinked beside the clone:

- **S** — snapshot sandbox `/tmp/r69-fleet/kotoba-shokunin` (commit `219b1fb`), taken at wave-1 start.
- **C** — current sandbox `/tmp/r69-fleet2/kotoba-shokunin` (commit `fed4dc9`), re-taken after peers
  changed `corpus/README.md`, `corpus/lessons/round-69.md`,
  `corpus/knowledge/skill-name-precedence-round69.md`, `verifiers/check_r67_routed_repairs.py` and
  `verifiers/check_skill_precedence.py`. **C is authoritative; S is retained because it is where two
  findings were first falsified.**

Lane tip: `a238989a96cb0d2b939679126b832d75b861ca6e` (base `a5f7459f`). The lane repo, index, jj
state and sibling lanes were never written: `HEAD` is still `a238989`, the lane's tracked files hash
identically to the measurement snapshot (except the four peers edited concurrently), and the only
file this seat added to the lane is this one.

## 1. Gate A — `python3 -B verifiers/verify_skill_checklist.py --json`

| state | exit | PASS/FAIL | failing check(s) |
|---|---|---|---|
| tip `a238989` (commit `219b1fb` sandbox) | **1** | 10 / 1 | `governance.citation_resolves` |
| tip, *naive* clone dir `r69-exec-checklist-sb` | 1 | 9 / 2 | `trigger.name_directory` (sandbox artifact) + governance |
| current draft **C** (`fed4dc9`) | **1** | 9 / 2 | `trigger.line_budget` **603 > 600** + governance |
| draft + governance repair (S, `e325dbc`; C, `ddfab41`+errata) | 1 | 10 / 1 | `trigger.line_budget` only |
| `SKILL.md` at 600 lines (tip file) + governance repair | **0** | **11 / 0** | — |
| bound mutation `600`→`700` (box at line 319) | 1 | 1 / 1 | `trigger.line_budget` PASS at 700 **but** `checklist.box_map_complete` FAIL: `map entry trigger.14 has no live box … sha256 b90f6bf1db13…` |
| `--self-test` (with and without the errata patch) | 0 | — | `0 failure(s) over 1862 assertions` |

Tip output, verbatim:

```
pass=10 fail=1 na=0 exit_code=1
FAIL  governance.citation_resolves  LOG.md:2676: '.ufo/waves/round-67/w1/controls/census-validate-append.txt'
      does not resolve; LOG.md:2678: '.ufo/waves/round-67/w1/controls/junk-world/' does not resolve;
      10 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused,
      3 recorded correction(s) excused
```

Current draft output, verbatim (the two reds):

```
FAIL  trigger.line_budget           603 lines exceed budget 600 (from box at line 319)
FAIL  governance.citation_resolves  LOG.md:2676: '…/census-validate-append.txt' does not resolve;
                                    LOG.md:2678: '…/junk-world/' does not resolve
```

`SKILL.md` is **exactly** 600 lines at the tip; the draft's three new gate-registry rows
(`check_skill_precedence`, `check_r68_routed_repairs`, `check_province_core`) take it to 603. The
bound lives in the box at line 319 and is sha256-pinned by `verifiers/checklist-baseline.json`, so
the bound cannot be relaxed silently — measured: raising it to 700 flips `trigger.line_budget` to
PASS and breaks `checklist.box_map_complete` on `trigger.14`.

## 2. Gate B — `python3 -B verifiers/verify_corpus_independent.py --json`

| state | exit | verdict |
|---|---|---|
| tip `a238989` | **1** | DRIFT `corpus.index.unindexed` 1 = `corpus/lessons/round-68-verifier-spotcheck.md`; tracked 125, report_total 87, commit_total 38 |
| current draft **C**, uncommitted | **1** | DRIFT `corpus.index.stale_patterns` 1 = `corpus/README.md:130: knowledge/skill-name-precedence-round69.md` — the entry exists but is untracked; unindexed 0 |
| current draft **C**, committed (`fed4dc9`) | **1** | DRIFT `corpus.index.unindexed` 1 = `corpus/lessons/round-69.md` (no coverage-map row) |
| + one `lessons/round-69.md` row (`ddfab41`) | **0** | no drift: tracked 127, unindexed 0, stale 0, missing 0, report_dead 0, commit_unresolvable 0 |
| `--self-test` | 0 | `self-test: 103 assertions, 0 failures` |

The tip red is the pre-repair state the plan names as C2's "before" (`unindexed 1`, 125 tracked,
`report_total 87`). The draft repairs the round-68 spot-check row (`corpus/README.md:131`) but leaves
the round's own lesson unindexed. The draft-only STALE is commit-order transient only: the checker
scopes to *tracked* files, so a map row that lands before its entry is committed reads STALE.

## 3. Cross-checks — C1/C2/C3 and the corpus gate

| instrument | current tree `fed4dc9` | green world `ddfab41` | base control `a5f7459` |
|---|---|---|---|
| `check_skill_precedence.py --rev` | exit 0, `skill precedence backed 5 of 5` | 5 of 5 | exit 1, `0 of 5`, `entry missing` |
| `check_r68_routed_repairs.py --rev` | exit **1**, `closed 5 of 8` — open D6, D7, D8 | exit 0, `closed 8 of 8` | — |
| `check_province_core.py --rev` | exit 0, `province core rows 2 of 2` | 2 of 2 | exit 1, both § Core bullets absent |
| `verify_corpus_integrity.py` | exit 1, **5/9** — `tracked 127≠124`, `unindexed 1≠0`, `report_total 87≠85`, `commit_total 39≠38` | exit 0, **9/9** | — |

C2 moved from `4 of 8` (snapshot S) to `5 of 8` (current C) because a peer replaced the r67
verifier's `"checkout"` argv with `reset -q --hard` — i.e. exactly the remedy measured in F5 below,
which confirms F5's analysis: D3 was gated on a token, not on a lane write.

## 4. Findings

**F1 — blocker, pre-existing, unowned by any claim: `governance.citation_resolves` is red at the
tip.** `LOG.md:2676` cites the *wrong* census-receipt path inside the R67-2 erratum (the right path
is on 2677); `LOG.md:2678` cites `…/junk-world/`, a directory R67-3 discloses as removed. Both lines
are past both frozen horizons (`GOVERNANCE_ERRATA_HORIZON` 2315, `GOVERNANCE_CORRECTIONS_HORIZON`
2621). The correction mechanism cannot excuse 2676 even in principle: `correction_problems` requires
the stale and corrected tokens on the *same* row line, and they sit on 2676/2677 — so the round-65
correction class cannot reach a two-line erratum. Measured remedy: `GOVERNANCE_ERRATA_HORIZON =
2678` plus two byte-pinned rows → `PASS … 1244 governance citation token(s) resolve across 2 files …
3 recorded absence(s) excused`, self-test still `0/1862`. Two caveats the Gate note must carry:
(a) the row's `quote` is only substring-checked, and the only phrases available on those physical
lines (`the file that exists is`, `Routed defect R67-3 (disclosure)`) are correction/disclosure
wording, not absence wording — the row is mechanically accepted but semantically off-label; (b) the
only conforming repair is a verifier edit, i.e. the gate excuses its own red. Nothing in C1/C2/C3
covers this, so the "expect exit 0" written into the seat card is unachievable from the frozen plan.

**F2 — blocker, draft-introduced: `SKILL.md` 603 > 600.** The three new registry rows cost exactly
the 3 lines the file does not have. The bound is pinned (F above), so the draft must free 3 lines
elsewhere (the box's own remedy: "overflow already moved to referenced depth files") or relocate the
three rows.

**F3 — blocker, draft: `corpus/lessons/round-69.md` has no coverage-map row.** `corpus/README.md`
gains rows for the precedence entry (130) and the r68 spot-check (131), not for the round's own
lesson. One row flips gate B to exit 0 (measured at `ddfab41`).

**F4 — methodology, affects every seat this wave.** A `git clone --shared` into a differently-named
directory yields two *false* FAILs in gate A: `trigger.name_directory` (the frontmatter name must
equal the directory, so the clone must be `…/kotoba-shokunin`) and `governance.citation_resolves`
(`../PROTOCOL.md`-style tokens need fleet-root siblings present). Seats that skip this will report
phantom reds; the first run of this seat did exactly that (9 PASS / 2 FAIL).

**F5 — falsified and now confirmed by the lane: D3 was a token ban, not a lane-write test.** At
snapshot S the draft's `check_r67_routed_repairs.py` materialized the measured rev in a
`tempfile.TemporaryDirectory` clone — never the lane — yet the counter's predicate is
`re.search(r"[\"']checkout[\"']", src)`. Replacing that argv with
`["git","-C",str(clone),"reset","--hard","-q",rev]` (same target, same behaviour, no lane write)
moved the counter from **4 of 8 to 5 of 8**. The lane now carries `reset -q --hard` and C2 reads
`5 of 8`, which is D3 closed. Consequence for the registry row: D3's stated rule ("runs no
`git checkout` (a git write in the lane)") is enforced as a literal-token ban; a future verifier that
legitimately needs the word in a sandbox path will be failed for it.

**F6 — D6/D7/D8 are narrower than their prose.** D6 requires `R68-6` **and** `S201` on one line of
§ Mistakes; M111 carries `R68-6` on its head line and `S201` two lines later, so it fails even though
the row is correct — adding `, S201` to the head line closes it. D7 reduces to a single literal line,
`disposition: removed .ufo/waves/round-68/w1/controls/c2falsify-clone/`; the current prose
(`dispositioned as removed (the clone: \`disposition: removed .../c2falsify-clone/\`)`) captures
`.../c2falsify-clone/`, which is not the path in `R68_PATHS`, so it does not count. D8 needs the
re-record to the gate's own `--no-baseline --json` measurement: `tracked_files 124→127`,
`report_total 85→87`, `commit_total 38→39` (`unindexed` is 0 once F3 lands). With D6+D7+D8 landed:
C2 `8 of 8`, integrity `9/9`, gate B `exit 0` — measured at `ddfab41`.

## 5. Measured repair set (lane untouched; applied only in `/tmp`)

1. `SKILL.md` ≤ 600 lines (free 3 lines or relocate the three new rows).
2. `GOVERNANCE_ERRATA_HORIZON` ≥ 2678 + two byte-pinned rows for `LOG.md:2676` and `LOG.md:2678`.
3. `corpus/README.md` coverage-map row for `lessons/round-69.md`.
4. `corpus/lessons/round-69.md` § Mistakes: `S201` on the M111 head line; plus the literal
   `disposition: removed .ufo/waves/round-68/w1/controls/c2falsify-clone/` line.
5. `verifiers/corpus-baseline.json` re-record `124→127`, `85→87`, `38→39`, taken **after** the final
   corpus edits.

Item 6 of an earlier draft of this list (drop the `"checkout"` token) is already landed by a peer.
With 1–5: gate A `pass=11 fail=0 exit=0`, gate B exit 0, integrity 9/9, C1 5/5, C2 8/8, C3 2/2.

## 6. Bounds, risks, artifacts

Bounds: read-only git in the lane only; every execution under `/tmp`; one process at a time; no
`git checkout`/`git write` in the lane; no installs were needed, so none are recorded; seat writes
limited to this file. The 269 MB `c2falsify-clone` was excluded from both sandboxes and is not needed
to reproduce any number here.

Risks for the L1: (a) D8's expected counts move with any later corpus edit — `commit_total` is 39 only
because `round-69.md` cites `a238989a`; re-record last. (b) The governance red is invisible to all
three r69 counters, so a round can close C1/C2/C3 and still ship a red primary gate — and F4 means a
seat's sandbox layout can also manufacture a phantom version of it. (c) r69's `11/11` after the
errata extension is **not** independent evidence that `LOG.md`'s citations are live; the Gate note
must say the extension excuses two named absent paths. (d) `governance.citation_resolves` counts 1244
tokens across two files, so a green run says nothing about the 11 unscanned correctness surfaces.

Raw JSON/exit-code artifacts for every row above: `/tmp/r69-*.json`, `/tmp/r69-*.out`,
`/tmp/r69-*.txt`, produced during this seat. Each row is reproducible by re-running the stated
command in a fleet-shaped sandbox at the stated commit.
