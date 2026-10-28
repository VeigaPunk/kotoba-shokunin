# Kb81E04Baseline — C1 repairs R3 + R4 (round 81, w1)

Role: executor, leaf. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only except the
wave-81 paths named in the brief). Base: `b284223105f4d106f7e8f56ed4fd296c643cda0e`.
Plan read first: `plans/round-81.md` § C1 repairs 3–4. Nothing here scores a claim after-value.

## 1. Delivered

| artifact | what it is |
|---|---|
| `.ufo/waves/round-81/build/Kb81E04Baseline.patch` | the two content changes, self-contained: coverage-map row for `corpus/lessons/round-80-verifier-spotcheck.md` + `.ufo/waves/round-81/dispositions/wapes.txt` (5445 B; `git apply --check` on a pristine base clone exit 0) |
| `.ufo/waves/round-81/build/Kb81E04Baseline.disposition-only.patch` | the disposition file alone (823 B); applies to a pristine base **and** on top of `Kb81S08ReadmeRows.patch` |
| `.ufo/waves/round-81/build/Kb81E04Baseline.md` | the ordered integration runbook: groups G1–G8, gates after each, the measured expected post-integration baseline diff, the refresh exit 0/2/3 decision tree, the R1 findings, the traps |
| `.ufo/waves/round-81/build/refresh-corpus-baseline.py` | the round-80 script ported **byte-identical** (sha256 `8481be46…`, same bytes as the r79 and r80 copies); no fix was needed |
| `.ufo/waves/round-81/build/Kb81E04Baseline/R01`–`R20` + `MANIFEST.sha256` | every receipt below, with digests |

No instrument patch ships from this seat (E01/E02 own those). No lane file was edited: the row and the
disposition exist only as patches, applied in scratch clones.

## 2. What was measured (own exit captured on every command, never through a pipe)

| # | command | result |
|---|---|---|
| 1 | `verify_corpus_integrity.py --repo <base clone> --no-baseline --json` | exit 1 — `tracked 155, unindexed 1 (round-80 spot-check), stale 0, missing 0, report_total 111, report_dead 1 (HEAD:.ufo/reports/round-77/kotoba.md), commit_total 46, commit_unresolvable 2 (SOURCES.md:171-172), nonhash 0` (`R01`) |
| 2 | `verify_corpus_independent.py --repo <base clone> --json` | exit 1 — same classes, `report_dead 0` (the known divergence) (`R02`) |
| 3 | base + my two changes, committed clean (`4e1979a`), `verify_corpus_integrity.py --json` | exit 1 — `unindexed 0` (was 1), `stale 0`, `missing 0`, `tracked 155`, `report_total 111` unmoved by the row; DRIFT = `tracked_files, report_total, report_dead, commit_unresolvable` (`R03`) |
| 4 | `refresh-corpus-baseline.py --repo <clone>` on that tree | **exit 2, refused**, `zero-mode corpus.pointers.report_dead observed 1, not 0`; baseline untouched, tree clean afterwards (`R04`) — index+baseline repairs alone cannot land the re-record |
| 5 | same tree + measurement-aid instruments (see § 4), both gates | integrity exit 0, independent exit 0; `report_dead 0, commit_unresolvable 0, commit_external 2` (`R05`, `R06`) |
| 6 | `refresh-corpus-baseline.py --repo <clone>` | exit 0 — `tracked_files 154 -> 155`, `report_total 109 -> 111`, `post-refresh: 9/9 checks pass, exit 0`, `independent: exit 0; exit 0` (`R07`), diff in `R08` |
| 7 | post-integration shape: base + `Kb81S08ReadmeRows.patch` + my disposition + `build/allowed-tools-sdk-round81.md` → `corpus/knowledge/…` + `build/Kb81S01Lesson.md` → `corpus/lessons/round-81.md` + aid instruments, clean (`8af6525`) | integrity exit 0: `tracked 157, unindexed 0, stale 0, missing 0, report_total 111, report_dead 0, commit_total 46, commit_unresolvable 0, commit_external 2`; independent exit 0 (`R15`, `R16`) |
| 8 | refresh on that shape: `--dry-run` then real | exit 0 both — `tracked_files 154 -> 157`, `report_total 109 -> 111`, `9/9`, independent exit 0; only two `expect` lines move (`R17`, `R18`) |
| 9 | `--repo .` from a tree root, `--dry-run` | exit 0, same three lines, file untouched (`R19`) — the plan's literal form works |
| 10 | instrument self-tests on the aid tree | integrity `0 failure(s) over 165 assertions` exit 0; independent `105 assertions, 0 failures` exit 0 (`R12`) |
| 11 | the guard's own size computation on the two published repairs | `added 473 / deleted 32` vs `LINE_CAP 140` → `instrument-size` fails by 333 (`R20`) |

## 3. The disposition (R3) — what it actually takes

`.ufo/wapes` is **untracked**, so no commit can move it and no patch can delete it. The committed
evidence is a byte-identical copy at `.ufo/waves/round-81/dispositions/wapes.txt` (594 B, sha256
`930e2bd6b306b973a81144572f0b93a333379e501bffae1a8f8c50ec84dd6020`, verified on both paths after the
copy); its content is C2 quote-probe output (four `words=N ok=False why=…` lines, final `exit=0`).
Provenance lives in the runbook, not in the file, so the digest stays the evidence. The L1 deletes the
stray from the lane root; it is still there now (`ls -l .ufo/wapes` → 594 B, 2026-10-27 20:17) because
that path is outside this seat's write scope.

## 4. The R1 finding — the strongest thing this seat measured

The plan's R1 sentence ("a resolved report target — path *or* object — must bind report content
identity") is not implementable as written, and the obvious repair is not sufficient:

* **Identity on every resolved target** → `report_dead 11` at base, 11 citations of 5 distinct
  pre-convention reports (rounds 1, 4, 5, 8, 14; the list is in `R10`). Round 8's report *is* a 120 B
  respawn marker and the corpus cites it as one. Identity-for-all makes C1 unreachable.
* **Identity on object-resolved targets only** (the shape the round-81 lesson draft states) → a marker
  substituted at a post-convention report **path** reads `report_dead 0`. The round-80 W10 world
  substituted at `.ufo/reports/round-76/kotoba.md`, which the corpus cites by path, so W10 would reach
  its target and the plan's kill rule would fire (`R14`).
* **The measured boundary that satisfies both**: object targets always bind; path targets bind at
  round ≥ **19**. `## SHONEN` is uniform from round 19 on (rounds 19–80 all carry it and are ≥ 3166 B;
  rounds 1–17 are mixed) — `R11`. Under it: `report_dead 0/111`, `commit_unresolvable 0`,
  `commit_external 2`, W10 marker still dead (`R09`).

`Kb81E01Integrity` adopted the boundary (and reproduced the 11 independently) and applies it at every
path route with `<rev>:<path>` always binding; its published instrument reads the same numbers. The
R1 repair must also **re-anchor its own self-test fixture** `pointer/fleet-root/resolves-existing-report`
(it writes `"report\n"` at round-53 and asserts `report_dead 0`, i.e. it encodes the existence rule):
re-anchoring to a ≥400 B `## SHONEN` body plus a marker arm is what I measured green (`R12`).

## 5. Ported from r80, and what changed

**Ported** (re-verified today): the dirty-tree precondition (untracked files refuse too — `R04` was
only reachable after a clean commit); the exit 0/2/3 decision tree and the "exit 3 has already written
the file" hazard; the `--carry` tree (`corpus.index.*` never carriable; nothing carried at the final
tip); baseline-alone-in-its-commit and no-amend; the detached-head label; the `..`-hop prose trap.
**Changed**: the group order (the instruments and the counter amendment must land before the baseline,
because the pins are a function of those bytes); the tracked-file arithmetic (155 at base, not 154 —
the closure's spot-check landed after the baseline record); the index rows are co-owned by
`Kb81S08ReadmeRows` (§ 6); and § 4 above, which has no r80 counterpart.

## 6. Risks and blockers (honest, not worked around)

1. **Line arithmetic is the binding constraint on C1** (`R20`). The two published repairs sum to
   `added 473 / deleted 32` against the guard's `LINE_CAP 140` (base spend 22 + integrity 204 +
   independent 247), so `instrument-size` fails by 333 before E02's gate even runs. Under the plan's
   kill rule C1 survives only if the instruments shrink to ≤ 118 added lines in total. Do not raise
   `LINE_CAP` after data; do not buy lines by dropping the path identity arm (`R14`). My runbook
   states both, and G4's expectation now reads "6 of 6 only if the arithmetic closes — else honest
   stop" rather than assuming it.
2. **Two owners for one README hunk.** `Kb81S08ReadmeRows.patch` already carries an equivalent
   round-80 spot-check row (plus the two round-81 rows). Applying both patches conflicts
   (`corpus/README.md:157: patch does not apply`, measured). The runbook gives the decision: use S08's
   rows + my disposition-only patch, or mine alone — never both.
3. **The instrument patches were published after my aid was built**, so the zero-class readings in
   `R15`/`R16` come from this seat's own measurement aid (scratch only, never a lane edit, never a
   shipped patch); the equal-class counts are the gate's own definitions and are unaffected. `R20`
   was measured on the real published patches.
4. **The expected post-integration diff is anchored to the current drafts.** `157 / 111 / 46` is what
   the drafts in `build/` produce; if the final lesson cites the round-81 report path, `report_total`
   reads 112. The runbook gives the arithmetic and requires a `--dry-run` read rather than a
   prediction, so a changed final content set is not a surprise.

## 7. Hygiene

Scratch `/fast/scratch/hyaku/kotoba-r81/Kb81E04Baseline/` (five clones: `clone`, `check`, `check2`,
`post`, `cap`) removed before yielding; every receipt copied out first. Every git mutation
happened inside those clones, each after `rev-parse --show-toplevel` asserted the clone as its own
toplevel. No lane commit/add/stash/checkout; lane `git status` still shows only the pre-existing
`.ufo/wapes` and `plans/round-81.md` outside the wave directory. Tooling: nothing installed,
upgraded or run through a package manager; `pacman` not invoked; no network fetch by this seat.

VERDICT: R3+R4 delivered as two verified patches plus the ordered runbook; the refresh mechanism is proven both ways (refuses without R1/R2, writes `154→157 / 109→111 / 9/9` with them), and the measured blocker on C1 is now line arithmetic (473 > 140), with the R1 identity floor of 19 handed to the instrument seats and adopted.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/w1/Kb81E04Baseline.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E04Baseline.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E04Baseline.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E04Baseline.disposition-only.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/refresh-corpus-baseline.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-81/build/Kb81E04Baseline/ (R01-R20 + MANIFEST.sha256)
