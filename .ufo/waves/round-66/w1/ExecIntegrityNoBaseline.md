# ExecIntegrityNoBaseline — round 66 integrity gate, `--no-baseline` at the observed tip

Seat: read-only measurement (leaf). Assignment: run
`python3 -B <lane>/verifiers/verify_corpus_integrity.py --no-baseline --json` at the observed
tip, recompute the zero-mode findings and the measured count vector, report revision, exact
observed values and exit. No claim, counter, threshold, plan, receipt, source, or Git/jj state
was changed. No tool was installed or upgraded.

## Revisions

| Role | Revision |
|---|---|
| Pinned base (plan freeze, `plans/round-66.md`) | `11385e04e368c1e94ab1a5a89d7439033eb1f855` |
| Baseline re-record point (`round66_rerecord` note) | `daedcdf992c17cbc0b8a6ece204e1c7ce2b45fce` |
| Claim landing tree / declared final tip (`corpus/lessons/round-66-verifier-spotcheck.md:13`) | `9e75e7345574af59d0585429a0f25b6179aa375d` = `HEAD^` |
| **Observed tip (measured)** | **`2a8eba56b3f9321b70c569fa2816d42237ca49a2`** ("round-66 verifier spot-check (integrator, hyaku): non-author admit/reject"), jj change `98c994b017ca50393e0316c8409028f8cdeb4031`, branch `master` |

`11385e04` is an ancestor of HEAD (`git merge-base --is-ancestor` → 0). Corpus worktree was
clean during measurement (`git status --porcelain corpus/` → 0 lines), so the gate read committed
bytes. The only dirty paths are other seats' in-flight output under
`.ufo/waves/round-66/w1/` (one modified `swarm-registry.json`, seven untracked `*.md`), outside
`corpus/` and with no effect on this gate. Gate blob is identical at HEAD and `HEAD^`:
`71cb2730bfe89064567ad429bfd7c2da62aceb45` (sha256 of the file
`febfa57e64896a37cea740ee080ccd1ea0f994980ade0856fc2dc080c1386534`), so the tip delta is corpus
content, not an instrument change.

## Assigned run at the observed tip

```
$ python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json
EXIT=1
```

Plain form of the same command:

```
corpus.index    tracked=119 unindexed=1 stale=0 missing=0  (136 FILE-column patterns over 118 md files)
corpus.pointers report_dead=0/82 commit_total=38 unresolvable=0 nonhash=0 (shapes [relative=1, absolute=44, tilde=1, bare=36], quoted-excluded=6, pointer-excluded=8; sites in --json)
8/9 checks pass; DRIFT: corpus.index.unindexed
EXIT=1
```

The `8/9` text summary counts `OBSERVE` rows as non-failing; the row verdicts below are the
strict accounting (5 PASS, 1 DRIFT, 3 OBSERVE).

### Zero-mode findings (baseline-independent; these decide the exit)

| Check | Mode | Observed | Expected | Verdict |
|---|---|---|---|---|
| `corpus.index.unindexed` | zero | **1** | 0 / empty | **DRIFT** |
| `corpus.index.stale_patterns` | zero | 0 | 0 / empty | PASS |
| `corpus.index.missing_paths` | zero | 0 | 0 / empty | PASS |
| `corpus.pointers.report_dead` | zero | 0 | 0 / empty | PASS |
| `corpus.pointers.commit_unresolvable` | zero | 0 | 0 / empty | PASS |
| `corpus.pointers.commit_nonhash` | zero | 0 | 0 / empty | PASS |

Sole drift detail: `corpus/lessons/round-66-verifier-spotcheck.md`. Independently re-derived:
`git ls-files corpus/ | wc -l` → 119; `grep -c round-66-verifier-spotcheck corpus/README.md` → 0;
of the tracked corpus files, only this one has neither a literal coverage row nor a
brace/glob-row match (`lessons/round-{1,4,5}-aggregator-audit.md`, `corpus/README.md:30`, covers
the three other basename-absent lessons). 119 tracked − 1 `README.md` = 118 need coverage; 117
are covered → unindexed 1. Exit 1 follows from this row alone.

### Measured count vector (equal-mode, reported as OBSERVE under `--no-baseline`)

| Metric | Observed | Frozen C2 pin (plan / counter / baseline `round66_rerecord`) |
|---|---|---|
| `corpus.index.tracked_files` | **119** | 118 |
| `corpus.index.unindexed` | **1** | 0 |
| `corpus.index.stale_patterns` | 0 | 0 |
| `corpus.index.missing_paths` | 0 | 0 |
| `corpus.pointers.report_total` | **82** | 79 |
| `corpus.pointers.report_dead` | 0 | 0 |
| `corpus.pointers.commit_total` | **38** | 37 |
| `corpus.pointers.commit_unresolvable` | 0 | 0 |
| `corpus.pointers.commit_nonhash` | 0 | 0 |

Full observed block at the tip: `tracked_files=119`, `index_patterns=136`,
`index_tokens_total=136`, `index_tokens_fenced=0`, `index_tokens_excluded=0`,
`index_tokens_classified={directory:2}`, `corpus_md_files=118`, `report_total=82`,
`report_pointers_excluded=8`, `report_pointers_quoted=2`, `report_dead=0`,
`commit_total=38`, `commit_quoted_excluded=6`, `commit_unresolvable=0`, `commit_nonhash=0`,
`report_pointer_shapes={relative:1, absolute:44, tilde:1, bare:36}` (sums to 82). Excluded/quoted
details are the same eight `<lane>`/`<repo>` schematics and two quoted pointers the base control
lists; the six quoted commits are the same set as the base control plus
`corpus/lessons/round-54-verifier-spotcheck.md:147: 451a02ff` (now classified code-span context by
the tip instrument).

## Revision matrix (same tip instrument, `--no-baseline --json`, temp clone of the lane)

The lane repo was cloned read-only to `/tmp/r66-clone` (`git clone --shared` of the lane checkout)
and each revision was checked out detached there; the lane worktree/index were never touched.

| Rev | tracked | unindexed | stale | missing | report_total | report_dead | commit_total | unresolvable | nonhash | exit |
|---|---|---|---|---|---|---|---|---|---|---|
| `11385e04` (pinned base) | 116 | 4 | 0 | 0 | 79 | 0 | 37¹ | 0¹ | 0 | 1 |
| `daedcdf` (re-record point) | 118 | 0 | 0 | 0 | 79 | 0 | 37 | 0 | 0 | 0 |
| `9e75e73` (claim landing tree) | 118 | 0 | 0 | 0 | 79 | 0 | 37 | 0 | 0 | 0 |
| `2a8eba5` (observed tip) | 119 | 1 | 0 | 0 | 82 | 0 | 38 | 0 | 0 | **1** |

¹ Instrument-version effect, not content: the base-era instrument at `11385e04` reads
`commit_total=38`, `commit_unresolvable=3` (details: `round-54-verifier-spotcheck.md:147:
451a02ff`, `round-62-verifier-spotcheck.md:13: def4b9ff…`, `round-65-verifier-spotcheck.md:11:
7b370d54…`) and `4/9 checks pass` with DRIFT `tracked 116/81`, `unindexed 4`, `report_total
79/51`, `commit_total 38/32`, `commit_unresolvable 3` — an exact reproduction of
`controls/C2-before.txt`. The tip instrument's code-span exclusion moves `451a02ff` into quoted
context (38→37) and its lane-first→fleet-root hop resolves the remaining two (3→0). The frozen
before→after `commit_total 38→37` therefore mixes one classification fix with the hop; neither
is a deletion of corpus text.

## Delta attribution for the tip

`2a8eba5` adds exactly one file, `corpus/lessons/round-66-verifier-spotcheck.md` (+83 lines, no
other path). Its own per-file `citation_findings` (instrument functions, resolution stubbed true):
`report_total=3` (all `bare` shape: `:10`, `:22`, `:26` all cite `.ufo/reports/round-66/kotoba.md`),
`commit_total=1` (`:11` `commit \`1154d57a9ebb17faa4c9f8f456a6e53c51c230ae\``, the fleet report
commit, resolvable through the fleet-root hop), excluded/quoted/nonhash 0. That is precisely
+1 tracked, +1 unindexed (no README row), +3 report pointers (79→82), +1 commit (37→38). No other
count moved.

## Second instrument at the tip

`python3 -B verifiers/verify_corpus_independent.py --json` at `2a8eba5`:
`tracked_files=119`, `unindexed=1` (same detail), `report_candidates=92 → report_total=82`
(`excluded=8`, `quoted=2`, shapes `absolute 44 / bare 36 / relative 1 / tilde 1`),
`commit_candidates=44 → commit_total=38` (`quoted=6`, `unresolvable=0`, `nonhash=0`), DRIFT on
`corpus.index.unindexed`, **exit 1**. Both instruments agree value-for-value. A hand re-derivation
reproduced the pointer totals exactly (82 counted, 8 excluded, 2 quoted) and initially over-counted
commits by one (39/5); the discrepant token was
`corpus/lessons/round-54-verifier-spotcheck.md:147`, whose `` commit `451a02ff` `` sits inside a
double-backtick span — the shipped code-span rule excludes it, so 38/6 is the correct count under
the documented rule and the hand-script disagreement was my classifier's bug, not a gate defect.

## C2 calibration read (pinned base vs claim tree vs measured tip)

- At the claim landing tree `9e75e73` (= `HEAD^`), the gate is **exit 0**, 6 PASS / 3 OBSERVE,
  vector `118 / 0 / 0 / 0 / 79 / 0 / 37 / 0 / 0` — byte-for-byte the frozen C2 after-predicate, and
  matching `daedcdf` (the baseline re-record point).
- At the observed tip `2a8eba5` the same command is **exit 1** with the vector `119 / 1 / 82 / 38`.
  The plan's separate clause "`verify_corpus_integrity.py` must exit 0 at the final lane tree"
  holds at `9e75e73` and fails one commit later.
- The frozen counter `check_r66_routed_repairs.py --rev <rev>` reads `2 of 2`, exit 0 at **both**
  `9e75e73` and `2a8eba5` (and `0 of 2` at the pinned base). Its D2 predicate inspects committed
  blobs at `rev` — README contains the four r62–r65 spot-check rows (1 each),
  `verifiers/corpus-baseline.json` carries note `round66_rerecord` and expects
  `118/0/79/0/37/0/0`, and `verifiers/verify_corpus_integrity.py` carries `COMMIT_HOP_MARKER`,
  `def commit_resolves(`, `inside_code_span`, `commit_resolves(hex_id` — it does not re-measure
  live counts at an arbitrary later revision. So D1/D2 are not reopened by the tip; the tip red is
  a new, baseline-independent zero-mode violation.
- Baseline mode at the tip (informational): `python3 -B verifiers/verify_corpus_integrity.py --json`
  → exit 1, 4 DRIFT (`tracked 119≠118`, `unindexed 1`, `report_total 82≠79`, `commit_total 38≠37`),
  5 PASS. The pins are a stale as-of record, not fitted.

## Findings (observed, not adjudicated)

1. The tip's sole integrity defect is the closure-owned
   `corpus/lessons/round-66-verifier-spotcheck.md` being committed without a coverage-map row —
   the same M21/M47 class the README records for rounds 58–61 (`corpus/README.md:98,101,104,108`),
   each later "indexed round N". It is not a lane-authored artifact and not a C1/C2 content revert.
2. The frozen C2 count pins (118/0/79/37) are exact for the landing tree and stale by exactly one
   post-claim closure file at the observed tip; only `unindexed` is a zero-mode failure, the other
   three are equal-mode drift against an as-of baseline.
3. The C2 counter's committed-byte predicate cannot see this class of later drift; a judge reading
   "2 of 2" at the tip must not read it as "gate green at the tip". Both facts were measured
   (counter exit 0, gate exit 1 at the same revision).
4. Environment mode: the same gate on non-git `git archive` trees (`/tmp/r66-base`,
   `/tmp/r66-daedcdf`) exits **2** (documented: not a git repo), confirming `tracked_files` is
   derived from `git ls-files`, not a filesystem walk.

## Risks / residual

- Scoring the C2 claim against the observed tip rather than the declared landing tree would read
  as a reopened D2; scoring against `9e75e73` reads as closed. This report keeps the two distinct.
- Closing the tip red requires a lane `corpus/README.md` coverage row for a closure-owned file;
  that edit is outside this read-only seat and was not made.
- Measurement is bound to `2a8eba5`; later landings (including the in-flight w1 sibling files) can
  move the vector again, but nothing under `corpus/` was dirty at measurement time.

## Evidence commands (reproducible)

```
git rev-parse HEAD                                        # 2a8eba56b3f9321b70c569fa2816d42237ca49a2
python3 -B verifiers/verify_corpus_integrity.py --no-baseline --json   # exit 1 (values above)
python3 -B verifiers/verify_corpus_integrity.py --no-baseline          # 8/9 pass, DRIFT unindexed, exit 1
python3 -B verifiers/verify_corpus_integrity.py --json                 # baseline mode: 4 DRIFT, exit 1
python3 -B verifiers/verify_corpus_independent.py --json               # same vector, exit 1
python3 -B verifiers/check_r66_routed_repairs.py --rev 2a8eba5…        # 2 of 2, exit 0
# sandbox: git clone --shared <lane> /tmp/r66-clone; detached checkouts of 11385e04 / daedcdf / 9e75e73
```
