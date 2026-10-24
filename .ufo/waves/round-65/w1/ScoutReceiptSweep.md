# ScoutReceiptSweep — round-65 W1 receipt sweep at tip

Seat: scout (calibration axis). Task: re-run every command in
`.ufo/waves/round-65/receipts/*.txt` at the tip; each must reproduce its
recorded output; note drift with the exact differing line.

## Headline finding: the tip is NOT the planned rev

```
$ git rev-parse master
2a8eba56b3f9321b70c569fa2816d42237ca49a2
$ git merge-base --is-ancestor 0e104f49 master && echo yes
yes
$ git log --oneline 0e104f49..master | wc -l
10
```

The wave spec says "verify 0e104f49" — **the lane has moved 10 commits past
it** (round-66 landed: `80bb8921`'s surface was edited again, a r66 routed-
repairs counter was added, LOG/SCORECARD/corpus appended). All commands were
re-run at `2a8eba56`. `git status` shows no modifications to `verifiers/`,
`LOG.md`, `SCORECARD.md`, or `corpus/` (only `.ufo/waves/*/swarm-registry.json`
and untracked round-66 w1 reports — sibling seats).

Instrument drift since receipt rev `80bb8921` (`git diff 80bb8921..master
--name-only`): `verifiers/check_scoped_rules_v32.py` (MIN_CLAUSE →
`clause_need`, +6 self-test arms), `verifiers/check_assertion_floors.py`,
`verifiers/floors-registry.json`. `verify_skill_checklist.py`,
`check_r64_routed_repairs.py`, `check_r63_routed_repairs.py`,
`check_gate_registry.py` are byte-identical to the receipt rev, so their
matching outputs are byte-level reproductions.

## Per-receipt results

### C1-close-measure.txt — REPRODUCES with one drifted line

`python3 -B verifiers/check_scoped_rules_v32.py --self-test`, exit=0.
Every frozen predicate line identical (all 7 world lines incl. `worlds reject
7 of 7; eligible rows pass 4 of 4`, all 6 survivor lines, `survivors closed 6
of 6`, all three `must-fail …: yes` lines). Drift:

| recorded | observed |
|---|---|
| `self-test: 0 failure(s) over 234 assertions` | `self-test: 0 failure(s) over 240 assertions` |
| `counter sha256 b6cfc7644b609f120f69b638d45d3253f07758f9dfa02e8252e2aeaad2183e8d` | `counter sha256 97d8971667d5b894bae76c3d811c00d578ee1bf0b4a777b429e04686bed26def` |

Cause: round-66 `clause_need` coupling added 6 self-test arms (`git diff` shows
`one_word_page`/`clause_need` checks). Exit still 0 — the receipt's predicate
shape holds; only the pinned `(sha256, N)` pair moved, as the plan's Q28 freeze
allows at a new rev.

### C1-close-kill.txt — REPRODUCES (battery run at tip bytes)

Rebuilt the harness exactly as the header describes: `git show
master:verifiers/check_scoped_rules_v32.py > /tmp/r65work/tree/
check_scoped_rules_v32.py`, ran the committed `kill_battery.py` against it.
`RESULT: ALL OK`, `harness_exit=0`. All 17 kill lanes exit=1 with their arm
labels; M19/M22 survive; pkg7-control exits 0; the three load-bearing pins
survive the control world; control+M11 dies with no new-arm label. Uniform
drift: `over 240 assertions` where the receipt records `over 234`, and the
control world prints `over 236` where the receipt records `over 230` (the +6
round-66 arms ride along in every mutant, unchanged ratio).

### C2-governance-measure.txt — REPRODUCES (detail counts drift)

`python3 -B verifiers/verify_skill_checklist.py --json` → `"fail": 0`,
`"pass": 11`, `"exit_code": 0`, process exit 0. `governance.citation_resolves`
PASS with `3 recorded correction(s) excused`. Detail-line drift (counts only,
all PASS):
- `trigger.line_budget`: recorded `599 lines within budget 600` → observed
  `600 lines within budget 600` — the budget check is **now at the wall**
  (round-66 appended one line). [INFERENCE] Next skill line added without a
  budget bump fails this check.
- `trigger.no_placeholder`: `532` → `533` scanned lines.
- `trigger.citation_resolves`: `161` → `163` tokens.
- `governance.citation_resolves`: `1193` → `1206` tokens.

`python3 -B verifiers/verify_skill_checklist.py --self-test | tail -1` →
`0 failure(s) over 1862 assertions` — identical.

### noharm-tip.txt — REPRODUCES with three drifted lines

- v32: `0 failure(s) over 240 assertions` (recorded `… 234`).
- checklist: `exit 0 pass 11 fail 0` — identical.
- r64 counter: `self-test: 0 failure(s) over 43 assertions` — identical.
- r63 counter: `r62 routed defects closed 5 of 5` — identical
  (`--rev 2a8eba56…`, the noharm run's own rev-pinning form).
- gate registry: `gate registry rows conformant 43 of 43 lane verifiers;
  phantom 0`, exit 0 (recorded `42 of 42`). +1 row = new
  `verifiers/check_r66_routed_repairs.py`, itself listed `OK`. Invocation
  caveat: the counter requires `--rev` (`exit=2` bare); ran
  `--rev 2a8eba56b3f9321b70c569fa2816d42237ca49a2`.

### FLOORS-noharm.txt / FLOORS-after.txt — exit 0 REPRODUCES, four drifted rows

`python3 -B verifiers/check_assertion_floors.py` exit=0, every row PASS
(observed ≥ floor everywhere; no hidden red row). Differing lines:

| receipt | observed |
|---|---|
| `PASS corpus_integrity observed=152 floor=152` | `observed=161 floor=161` |
| `PASS corpus_independent observed=99 floor=93` | `observed=103 floor=103` |
| `PASS scoped_rules_v32 observed=234 floor=234` | `observed=240 floor=240` |
| (FLOORS-after only) `PASS checklist observed=1852 floor=1852` | `observed=1862 floor=1862` |

Note: FLOORS-after's own `checklist observed=1852` line already disagreed
with the same round's noharm walk (`1862`) — the receipt appears to be a
mid-bump capture; the current registry is self-consistent at 1862.
`corpus_independent` floor was raised 93→103 by round-66 (now at its own
ceiling); `corpus_integrity` floor tracks the new observed 161.

### REGRESSION-probes.txt — REPRODUCES, including the oddity

- r64: `self-test: 0 failure(s) over 43 assertions` — identical.
- r63 (`--rev <tip>`): `r62 routed defects closed 5 of 5` — identical.
- `python3 -B verifiers/verify_corpus_integrity.py --json` → **process exit
  1**, JSON `{"observed": …, "results": [...]}` — the object has NO
  `pass`/`fail`/`exit_code` keys, so a `.get()`-style probe prints literally
  `corpus_integrity exit None fail None`. The receipt's odd line is thus
  accurate. Live non-PASS rows (4, all `DRIFT`): `corpus.index.tracked_files
  119 vs 118`, `corpus.index.unindexed 1` (`corpus/lessons/round-66-verifier-
  spotcheck.md`), `corpus.pointers.report_total 82 vs 79`,
  `commit_total 38 vs 37`. The receipts commit (`5253b281`) already records
  this check as "red pre-existing identical at base c98d137" — the red
  persists at tip, now against round-66 additions. Not a round-65
  falsification; a live, attributed, pre-existing red.

### Census — REPRODUCES (exit 0)

`scripts/sources-census.sh` is NOT in the lane tree; the plan's command means
the fleet script `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`.
`validate --root /home/vgpnk/Projects/shokunin kotoba` → exit=0, 16 `W04`
lines + `kotoba ok …/corpus/SOURCES.md` (17 output lines). Matches
`census-after.txt`'s shape (16 W04); corpus-integrity reports
`tracked_files: 119`, consistent with the round's "118 → 119 rows" claim.

### C2-selfreference-redbefore.txt — REPRODUCES byte-exactly (reconstruction)

The receipt records output only (no command line); it is a sandbox probe
against `check_governance_citations`. I rebuilt the fixture worlds with the
verifier's own functions (probe at `/tmp/r65work/c2_selfref_probe.py`,
[INFERENCE]: original script not committed). Observed:

```
BACKTICKED notice: status=FAIL
detail: LOG.md:2: 'corpus/gone.md' does not resolve from
/tmp/kotoba-redbefore-chmmxnzb; 0 quoted meta-finding(s), 0 schematic
token(s) excluded, 0 recorded absence(s) excused, 1 recorded correction(s)
excused
QUOTED     notice: status=PASS  (evaluated=1)
```

Byte-identical to the receipt modulo the tmpdir name. The self-reference
class is real and the landed double-quote fix holds.

### M99-fixture-leak.txt — REPRODUCES (reconstruction, one cosmetic clause)

Same caveat: output-only receipt. Probe `/tmp/r65work/m99_probe.py`:

```
bug A (errata default leaks into fixture): status=FAIL
   ["erratum LOG.md:2111 '.ufo/round-45/drafts/v10/post-r44-hunt.py' is past
     horizon 2315 or absent"]
bug B (subject line mismatch): status=FAIL
   ["correction LOG.md:2 SCORECARD.md:8 'corpus/gone.md': names no live red
     subject; SCORECARD.md:2: 'corpus/gone.md' does not resolve from
     /tmp/kotoba-m99b-…"]
```

Bug A line is byte-identical to the receipt. Bug B carries the named
`names no live red subject` clause byte-identically plus one extra clause
(`'corpus/gone.md' does not resolve`) — [INFERENCE] my fixture's subject sits
on line 2 vs the receipt's line-9-named SCORECARD; the bug class (mismatched
subject line → fail-closed) reproduces. The M99 record stands.

## Claim impact

- **C1** (frozen predicate: 5 lines + kill conjunct + floors row): every
  counted line reproduces verbatim at tip except the pinned `(sha, N)` —
  expected drift since round-66 edited the instrument. Kill conjunct intact
  at the new byte surface (ALL OK). → **supports C1**; the pinned pair is
  now stale, superseded by `(97d89716…, 240)`.
- **C2** (11/11, `citation_resolves` PASS, 1862, 3 corrections excused):
  reproduces fully. → **supports C2.** Flag: `trigger.line_budget` is at
  600/600 — zero headroom left.
- **Noharm/regression**: all green except pre-existing attributed
  corpus-integrity DRIFT (recorded in the receipts commit itself).

## Environment / tooling

No installs needed or made (pacman pause respected; `python3 3.14`, `git`,
`tar`, `sha256sum` all present). Scratch only under `/tmp/r65work/`. Lane
tree untouched; no git/jj writes. Peer processes spawned: none.
