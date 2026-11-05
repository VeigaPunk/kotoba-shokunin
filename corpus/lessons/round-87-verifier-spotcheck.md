author: hyaku closure (non-author integrator, @m_zfl)
round: kotoba 87 · closed 2026-11-05 · status `ok`, admitted **false** (`rejected-honest-stop`)
lane window: base `223ae62424f8ab1eb365d733eb648d6228ddd7e8` · before-attempt-2 `760e1c5edfdefb4767420f711d08f669952de013` · tip `74048151100e49ce2c628926c88f8b055a52026d`
report: `.ufo/reports/round-87/kotoba.md` (fleet `cb786d7a`, filed 00:34:39 after the lane tip at 00:33:54)

# kotoba round 87 — non-author closure spot-check

I did not author this round and did not improve it. Everything below is a re-measurement over committed
bytes, a re-opening of a source, or a named defect. I executed no lane gate (PROTOCOL §Gate standard,
*Closure consequence*): gate-backed claims are evidence-verified through their committed receipts, and
the substantive C1 conjuncts are independently re-implemented here.

## 1. Step-1 conformance

| check | command | observed | verdict |
|---|---|---|---|
| report committed by the lane identity | `git log --format='%an %ae %H %ci' -- .ufo/reports/round-87/kotoba.md` | `kotoba-shokunin kotoba@shokunin.local cb786d7a457f…` (and `65efcbbd`, `d752fdbe` before it) | PASS |
| report lands after the lane work | lane tip `74048151` 00:33:54; report commit 00:34:39 | report names the pushed tip | PASS |
| `SHONEN` heading, one line per box | `grep -c '^## SHONEN'` → 1; `- [` lines → 4; `SHONEN.md` boxes → 4 | all four `[~]`, no `[x]` (author attestation only) | PASS |
| every cited lane commit exists and is an ancestor | `git cat-file -e <h>^{commit}` + `git merge-base --is-ancestor <h> master` for 12 hashes | all present, all ancestors (`223ae62, 669f2801, 512126bb, 87ab1cb9, 760e1c5e, e03f9e2, 35a395a9, d1c0318, 3c8902a, e4b76dd, 49b7d1b, 74048151`) | PASS |
| fleet-side citations | `git cat-file -e` on `d752fdbe`, `5b052020` | both exist; `5b052020` is an ancestor of fleet `HEAD` | PASS |
| lane repo pushed, nothing uncommitted | `scripts/hyaku/jj-lane.sh state kotoba-shokunin` | `local=74048151 remote=74048151 ahead=0 behind=0 tracked=0 untracked=0` | PASS |
| prompt carries the template contract | line-level diff of `templates/round-prompt.md` (substituted) against `.ufo/prompts/kotoba-round-87.md` | 115 of 116 non-empty lines byte-identical; the one difference is a line-wrap (`single source of truth.` split), content present; sections 1, 2, 2b, 3, 4, 5 each once; no `{{…}}` leftovers; §6 addendum appended | PASS |
| five child-lane items present | report path (§4, item 3), commit-before-report (item 4, "The report lands last"), `SHONEN` heading (pre-report gate), commit-hash citation (item 4, "Cite ONLY the helper's final `landed <hash>`"), write scope (item 3) | all five present verbatim | PASS |
| L2 route map vs `MISSION.md` | `MISSION.md:53` §L2 concurrency | MISSION carries no model alias (role classes only, "advisory to host routing"); the prompt's run-15 route lines are the campaign addendum, marked superseded where superseded | no conflict |
| report is a report, not a marker | content read | work performed, evidence pointers, landed-change table with commits, measurements, census, trends, `SHONEN` | PASS (status `ok`) |

Conformance observations, status-neutral (routed below): the report's attempt-history arithmetic
(R87-D1), a stale sentence in its own lesson (R87-D2), the record's `SKILL.md` claim window (R87-D5),
and a landing-time/commit-time conflation (R87-D6).

## 2. Claims

The freeze declares two claims (`plans/round-87.md`, addenda `512126bb`/`87ab1cb9`); no target was
reworded, narrowed or re-scored after data, and the attempt-2 report records the tip reading rather
than the earlier 5 of 5.

### C1 — depth (target `12 of 12`, base 0 of 12)

**Reported** (`report:132-153`): base `omp root semantics grounded 0 of 12`, `guard S3 pattern-set
FAIL`, exit 1 at `223ae62`; after `12 of 12`, exit 0, S1–S3 PASS at `e03f9e2`, `3c8902a7`, `49b7d1b4`
(receipts committed at `74048151`).

**Evidence-verified** (gate not executed, PROTOCOL §Gate standard):
`sha256sum verifiers/check_omp_root_semantics.py` → `6e826f3bf8d4585340ddcc9b7a546e4b7d8b9774a2794c4f45b3cf13e7798922`,
equal to `.ufo/waves/round-87/w3/l1/instrument-sha256.txt:1` and to the report's frozen digest.
Receipts read at the tip: `w3/l1/base-both.txt` (base, `0 of 12`, S3 FAIL, exit 1),
`w3/l1/c1-tip.txt` (`12 of 12`, S1–S3 PASS, exit 0), `w3/l1/counters-at-3c8902a7.txt`,
`w3/l1/counters-at-final-tip.txt` (`12 of 12` at `49b7d1b4`), `receipts/c1-after.txt` (`e03f9e2`).
The ELF pin holds today: `sha256sum /home/vgpnk/.local/bin/omp` → `6737ee24…b7b0f`.

**Re-measured independently** (not the lane's script): I re-implemented conjuncts 1–3 over the
committed ledger at `74048151` and the pinned ELF — pattern column equals `verifiers/omp-skill-roots.tsv`,
each `reader_quote` occurs in the ELF, its own line carries a `join(`/`resolve(` token, and the
`// packages/<module>` header precedes the first occurrence:

```
$ python3 - <<'PY'   # inline re-implementation; rows read via `git show 74048151:verifiers/omp-skill-roots-semantics.tsv`
ELF sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f
semantics rows 12 roots rows 12
patterns equal: True
row  1 GROUND '{cwd}/.omp/skills' @173819979 hdr@173814223
row  2 GROUND '{cwd}/.claude/skills' @173840364 hdr@173837493
row  3 GROUND '{cwd}/.agent/skills' @173865724 hdr@173864077
row  4 GROUND '{cwd}/.agents/skills' @173865724 hdr@173864077
row  5 GROUND '{cwd}/.codex/skills' @173879095 hdr@173878972
row  6 GROUND '{cwd}/.opencode/skills' @172785704 hdr@172784226
row  7 GROUND '{cwd}/.github/skills' @172785704 hdr@172784226
row  8 GROUND '~/.omp/agent/skills' @173820135 hdr@173814223
row  9 GROUND '~/.omp/plugins/node_modules/*/skills' @173914936 hdr@173914407
row 10 GROUND '~/.agent/skills' @173865523 hdr@173864077
row 11 GROUND '~/.agents/skills' @173865523 hdr@173864077
row 12 GROUND '~/.omp/agent/managed-skills' @173809938 hdr@173809642
independently grounded 12 of 12
```

Every offset equals the one in the lane's receipt, so the ledger is not a rewritten artefact: the
quotes are the ELF's own bytes. The upstream half was re-opened for the sourced row (see §4).

**Bound, confirmed rather than accepted.** The report's own limits are real and I corroborate them:
`w3/CriticSemanticsR87/forgery-worlds.txt` carries four worlds (`w_cross_row7`, `w_subdir_row9`,
`w_misattr_row12`, `w_renderline_row6`) each reading `12 of 12`, exit 0 — the counter is a
presence-and-ordering test, attributable only through `attribution.txt`. Conjunct 4 is inert at
scoring (`score()` calls `run(..., chain=FROZEN_CHAIN)`, so `expected` and `actual` are one
computation); only the `..` probes and the `w_bound` self-test world exercise it. The live bound
probe (`w3/ExecProbeBoundR87.md`) is the real evidence for the `{cwd}/` half, and it is conclusive
(`"source":"agents:project"` vs `"agents:user"`, `strace` with no `$HOME`-above open). The counter
scores 12 of an **18-root** surface: `w3/ScoutPatternsR87/derived-roots.txt` names six composed joins
the ledger does not carry; I re-read four of them in the ELF (`Fr.join(p, "skills")` @173840218,
`Xr.join(p, "skills")` @173882129, `d.join(e.home, …, n)` @172785499, `Ys.join(Ys.dirname(we()),
"skillshare")` @173923798) — joins, not doc strings, so the coverage hole is real and routed.

**Verdict: `improved`.** The move is substantive (twelve readers grounded on the code that joins each
path, independently reproduced), and its instrument limits are disclosed rather than laundered.

### C2 — consistency (target `5 of 5`, base 0 of 5)

**Reported** (`report:154-172`): after `5 of 5`, exit 0 at `35a395a9` (`receipts/c2-final.txt`); **at the
tip `4 of 5`, exit 1** — D1–D4 PASS, D5(iii) FAIL. Before `0 of 5` by the pre-addendum counter
(`a2455a22…`, `w1/ExecRepairs/base.txt`); the frozen counter refuses the base (exit 2).

**Re-measured independently, item by item** (committed bytes; no gate executed):

```
D1  git show 74048151:.ufo/waves/round-86/receipts/tip-catalogue.txt | tail → "omp catalogue lines reproduced 215 of 215" / "exit=0"
    git show 74048151:.ufo/waves/round-86/receipts/tip-registry.txt   | tail → "gate registry rows conformant 67 of 67 lane verifiers; phantom 0" / "exit=0"
    instrument blobs equal at landing 04647b0f and tip: check_omp_catalogue_repro.py 7c233c8a85e4 == 7c233c8a85e4;
                                                        check_gate_registry.py      95ffed389f48 == 95ffed389f48
D2  grep -c 'planner/distiller/labrat/Main are frozen-topology seats' plans/round-87.md → 1 (lesson 0)
    ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs: carries the sentence (1 hit); SWARM_ROLES (line 265) = 10 roles, no planner
D3  first `## Gate` table → 5 rows with decision `reject` (S256-binary_quote-as-reader, doc-string quote,
    the M87-1 in-place rewrites, the 13-row denominator, the frozen D5 form)
D4  grep -c 'after the first candidate score' plans/round-87.md → 1
D5  (i)(ii) blobs unchanged from base 223ae62 to tip: round-86-verifier-spotcheck.md ae3f49a3… == ae3f49a3…;
          round-81.md 315c0ec6… == 315c0ec6…
    (iv) lesson-87 carries both sites and `left red and disclosed` (lines 84-91)
    (iii) FAIL: red set = ['corpus.pointers.commit_unresolvable'] only, 8/9 — want exactly two reds, 7/9.
          Committed evidence: w3/ExecMirrorR87/gate-lane.json (8 PASS / 1 DRIFT) vs gate-clone.json (2 DRIFT).
```

**Cause re-derived, and the reported value confirmed.** The red that healed is the pointer at
`corpus/lessons/round-86-verifier-spotcheck.md:33` → `.ufo/reports/round-84/kama.md`. That file now
exists in the fleet worktree: `stat -c '%y'` → `2026-11-04 22:47:40` (the report's 22:47), committed as
`5b052020` (`## SHONEN` present, 10 856 B), and it is not in the lane worktree (`.ufo/reports/round-84/`
absent), which is why the lane and a relocated clone disagree. So the round's own
`receipts/c2-final.txt` (5 of 5) was true at 35a395a9 and the tip reading is 4 of 5, exactly as the
report records. `w3/l1/q79-control.txt` reproduces the three worlds (`lane` 1 red, `clone` 2 reds,
`pinned` 1 red) and prints `q79 control: FAIL (same bytes, world-dependent verdict: 2 distinct
readings)`, exit 1.

**Verdict: `unchanged`, claim not verified.** The frozen acceptance is 5 of 5; the shipped tip reads
4 of 5. D1–D4 verify and D5's honest-carry conjuncts (i)/(ii)/(iv) verify, so nothing regressed, but
the claim's own target is unmet at the revision the round shipped. The lane recorded this rather than
re-scoring it — an honest stop, not a false claim.

## 3. Per-axis verdicts

| axis | verdict | evidence |
|---|---|---|
| depth | `improved` | C1 re-derived 12 of 12 (conjuncts 1–3 independently), ledger + knowledge entry + S256 landed; instrument limits disclosed (4 forged worlds, dead conjunct 4, 12-of-18 surface) |
| consistency (calibration sub-axis) | `unchanged` | C2 4 of 5 at the tip; D1–D4 verified, D5(iii) fails on an exact-set expectation that a healed external red falsifies; no regression (D1–D4 repairs hold; red set shrank 6 → 1 since base) |
| coverage | `unchanged` | no surface gained or lost; the round measured 12-of-18 and routed the six unledgered joins (`derived-roots.txt`) |
| operability | `unchanged` | both counters run and self-test; battery exit 0 at `d1c03183` (`2 of 6` gates, carried reds unchanged); `check_assertion_floors.py` standalone `exit=0`, 17/17 PASS |
| freshness | `unchanged` | S256 re-opened byte-identical (my own fetch, §4); ELF pin holds; no stale item was found-and-fixed beyond that re-verification |
| calibration | `unchanged` | tip reading disclosed against the frozen target, instrument limits graded, no overreach — but two record-accuracy defects (R87-D1, R87-D5) and one stale lesson claim (R87-D2) |
| adjacency | `unchanged` | `w3/ConnectOverlapR87.md`: no sibling corpus holds the loader semantics; the staged `merge/kotoba/` package is reported not absorbed; I confirmed it exists (188 rows, 88 entries, mtime 2026-10-24 23:33) and its id space collides at S256 |

## 4. Discernment spot-check (non-author)

Sample: the round's `## Gate` sections (attempt 1 and attempt 2), one admit and seven rejects. Each
source re-opened by me.

| item | decision | re-opened source | verdict | reason |
|---|---|---|---|---|
| **S256** — omp plugin skill-root reader (tier A `code`) | admit | `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/packages/coding-agent/src/discovery/omp-plugins.ts` — HTTP 200, 15 362 B, sha256 `4e66819cf706b81c6f31bd71e6de8892083a284525ab151948642faea00cb1b4`; line 70 = `dir: path.join(root.path, "skills"),` | **agree** | the row's size, sha256 and location all match; the ≤25-word quote is five tokens on that line; it grounds the one root the round-86 set could not (the ELF minifies it to `dir: Zo.join(R.path, "skills"),` @173914936) |
| round-86 `binary_quote` `var Gh = ".omp";` proposed as a reader | reject | ELF @166884553 | **agree** | the line carries no join token and names neither `plugins`, `node_modules` nor `skills`; it cannot satisfy conjunct 2 |
| a `reader_quote` repeating a doc/string-table line | reject | ELF @114489000 (`Load skills from .claude/skills/*/SKILL.md`), @114486488 (`Native OMP configuration from ~/.omp and .omp/`) | **agree** | both lines carry no join token, so conjunct 2 refuses them by construction — the refusal is a property of the frozen instrument, not of prose |
| the integration seat's in-place rewrites of the round-86 spot-check and `round-81.md` (M87-1) | reject | blob ids at base vs tip | **agree** | `ae3f49a3…` and `315c0ec6…` at base = tip for both files; the records were restored before any commit, and D5(i)/(ii) now pin it |
| the frozen 13-row C1 denominator | reject | `verifiers/omp-skill-roots-semantics.tsv` at the tip | **agree** | 13 lines = header + 12 data rows; the denominator is 12 |
| the frozen D5 form (`verify_corpus_integrity.py` exits 0) | reject | `check_r86_routed_repairs.py` `check_d5` (INTEGRITY_LINE `7/9 checks pass` + two named detail sites) | **agree** | two of the six base DRIFTs sit in records the lane may not rewrite, so a green gate is unreachable by honest work; the honest carry is what D5(i)/(ii)/(iv) implement |
| re-running C2 where `report_dead` is still red, to restore 5 of 5 | reject | `w3/l1/q79-control.txt` | **agree** | the state would be manufactured by withholding another actor's file; the control shows the reading is world-dependent at one revision |
| amending `check_r86_routed_repairs.py`'s d5 to a monotone form after the first candidate score | reject | `plans/round-87.md` § kill boundary | **agree** | the predicate is frozen before the first candidate score and the plan names that boundary; a post-data rule change is not the claim's rule |

No disagreement in the sample. The defects I do record (§6) are record-accuracy defects, none of them
a Gate admission or rejection: every sampled decision survives re-opening its source.

## 5. Trend verdicts

- **expansion — `unchanged`.** The round added one `SOURCES.md` row (S256; census 181 → 182,
  `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 182) and one admitted knowledge entry, but the
  ground is the surface round 86 already entered (omp skill roots / catalogue model) — the move is
  depth on held ground, not new ground. Census: `sources-census.sh validate --root … kotoba` →
  `exit=0`, 33 `W04`, 0 `E`, before and after (both receipts committed; I re-ran the after).
- **quality — `harmed`.** One admitted record is false at the tip and unmarked:
  `corpus/lessons/round-87.md:87` states the cited fleet artifact `.ufo/reports/round-84/kama.md`
  "carries no `## SHONEN` marker", but the file at fleet `HEAD` is 10 856 B with one `## SHONEN`
  heading and the lane's own report (`report:120`) records it landing at 22:47. The sentence was true
  when written (`e03f9e2`, 21:13) and attempt 2 edited this lesson without correcting it — the
  round's own central finding (the heal) is the fact that falsifies it. Second, smaller:
  `corpus/knowledge/omp-root-semantics-round87.md:47` lists `$HOME` (`/home/u`) inside the counter's
  frozen chain, which is `FROZEN_CHAIN = (BOUND_CWD, "/home/u/proj")` (`check_omp_root_semantics.py:90`),
  and row 19 marks `{cwd}/.omp/skills` "session cwd only", which no receipt measures. Against that:
  the round deepened a prior entry, re-verified S256 byte-identically and added a grounded criterion
  (Q79) — a trade, reported as a trade.
- **discernment — `improved`.** The outside sample agrees on the admit and all seven rejects, and the
  round's own attack seats falsified things it had accepted (four forged ledgers reach the C1 target;
  C2's 5 of 5 is not re-derivable at the tip; conjunct 4 is dead at scoring), recording each instead
  of re-scoring. Q79 is a grounded criterion with a control that is shown able to fail.

## 6. Routed defects (status-neutral; the lane fixes them in round 88)

| id | defect | evidence | fix |
|---|---|---|---|
| R87-D1 | report attempt-history arithmetic: "launched eight times before this attempt: 19:56, 20:35, 20:44, 21:02 …", and "this attempt is the third instance" | `grep -nE 'kotoba round=87' .ufo/watchdog.log` → six launches before the 23:51:44 attempt (19:56:11, 20:35:59, 20:44:38, 22:29:17, 22:31:27, 22:32:19) + the completing one, and **five** `lane-dead-no-report` lines; 21:02:56 is a lane-dead timestamp, not a launch | derive the counts with the command and quote it |
| R87-D2 | stale claim: `corpus/lessons/round-87.md:87` says `.ufo/reports/round-84/kama.md` "carries no `## SHONEN` marker" | `git show HEAD:.ufo/reports/round-84/kama.md \| grep -c '^## SHONEN'` → 1; size 10 856 B; mtime 22:47:40; `report:120` records the landing | append-only correction entry naming the superseded sentence (never an in-place rewrite) and sweep the lesson for the same claim |
| R87-D3 | `corpus/knowledge/omp-root-semantics-round87.md:47` puts `$HOME` inside the frozen probe chain | counter `verifiers/check_omp_root_semantics.py:90` `FROZEN_CHAIN = (BOUND_CWD, "/home/u/proj")`; the counter's own docstring (lines 33-38) also lists `/home/u, /home, /` and should be corrected with the r88 counter | append-only correction of the entry sentence; fix the docstring when the counter is unfrozen |
| R87-D4 | entry row 19 bound "project-scoped: session cwd only" is not what conjunct 4 tests and has no receipt | `bound_grounded()` applies the same ancestor chain to every `{cwd}/` row; `w3/ExecProbeBoundR87.md` exercises `{cwd}/.agents/skills`, not `.omp/skills` | state the measured bound, or cite a probe that distinguishes the row |
| R87-D5 | `SKILL.md` bytes changed in `e03f9e2` (CRLF → LF, 600/600 lines) and nothing records it; the report's "`SKILL.md` untouched (`600 of 600` lines)" holds only for attempt 2 | `git diff --numstat 223ae62 74048151 -- SKILL.md` → `600 600`; `git log 223ae62..74048151 -- SKILL.md` → `e03f9e2` only; attempt-2 window `760e1c5e..3c8902a7` is empty | record the normalization (append-only) and scope the "untouched" claim to the attempt |
| R87-D6 | landing time conflated with commit time: the report attributes the 22:47 landing to commit `5b052020`, whose committer date is `2026-11-04T12:16:01-03:00` | `git log -1 --format='%cI' 5b052020` vs `stat -c '%y' .ufo/reports/round-84/kama.md` → 22:47:40 | name the worktree landing separately from the commit's date |
| R87-D7 | `LOG.md` § Round 87 states C2 "verified, `5 of 5`"; at the tip it is 4 of 5 | `LOG.md` round-87 entry vs `report:167` | appended correction entry naming the superseded text (append-only file) |
| R87-D8 | carried instrument defects the lane already routed: C1's counter is presence/ordering only (4 forged worlds at 12 of 12), conjunct 4 inert at scoring, `binary_quote` never matched against the ELF, 12 of 18 roots; C2's D5(iii) is an exact-set expectation, non-monotone and location-dependent | `w3/CriticSemanticsR87/forgery-worlds.txt`, `attribution.txt`, `w3/SentinelEvidenceR87.md` F-1, `w3/ScoutPatternsR87/derived-roots.txt`, `w3/l1/q79-control.txt` | r88: monotone red-set test (added red fails, healed red passes), ELF-match of `binary_quote`, the six unledgered joins |

## 7. Scope

This file is the outside discernment check for round 87 and the closure's evidence for its MANIFEST
entry. It edits no lane-authored file, writes no `[x]` into `SHONEN.md`, promotes and mints nothing.
The lane's own lesson (`corpus/lessons/round-87.md` § Gate) carries `Spot-check result: pending`;
this file is that result: **agrees** on every sampled admit and reject, and records the defects above.
