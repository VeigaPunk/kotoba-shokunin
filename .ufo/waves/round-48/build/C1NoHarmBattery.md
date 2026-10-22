# C1NoHarmBattery — round 48 (attempt 2) no-harm gate battery: base `75f671b` vs candidate `26035dc`

Seat `KotobaR48.C1NoHarmBattery` (leaf executor; no delegation, no labrat). Lane read-only except this report; all code
work in my own clones; no lane/fleet/sibling VCS write, no commit, no push. Tooling: none installed or upgraded (stock
`python3`, `git`). Durable scratch `/tmp/kotoba-nh-20261022/` — `base/kotoba-shokunin` = `75f671b…`,
`cand/kotoba-shokunin` = `26035dcec54d8e42f3a8b47ae8ca551c18aec295` (clones of the lane repo; candidate fetched from
`/fast/scratch/hyaku/kotoba-r48-a2/cand`); `landed/kotoba-shokunin` = lane HEAD `84b9c9b` (extra column, F10). Logs
`/tmp/kotoba-nh-20261022/out-{base,cand,landed}/<gate>.log`, copies at
`/fast/scratch/hyaku/kotoba-r48-a2/seats/C1NoHarmBattery/nh-evidence/`.

## Verdict
**No-harm holds: the candidate changes no gate outcome — nine gates, two revisions, same exit code and same headline on every row.** The three gates whose logs differ between revisions differ only in embedded paths/HEAD, never in values. The
landed lane HEAD (F10) shows the same exit codes again.

## Findings
**F1 — Exit codes identical on every gate; no timeouts.** All gates ran under `timeout 900` (durations 0–55 s). Six of
nine outputs are byte-identical between revisions; `compare_harness_live` differs on the one line naming the independent
instrument path, `corpus_independent` only in its `(HEAD …)` label (`75f671b` vs `26035dc`), `skill_checklist_json` only in the path suffix inside two `detail` strings. No check value, count, status or verdict differs.

**F2 — The live-join gate is nondeterministic on this host; the flakiness is not candidate-induced.** Default live join
(from `--help`/docstring): live = `python3 verifiers/verify_harness_claims.py --json`, independent =
`verifiers/verify_harness_independent.py --json`, scope = `verifiers/harness-independent-scope.json`, `--expect-n 28`,
no report/receipt written by default. Three runs per revision: base = exit **2, 2, 1**; candidate = exit **1, 1, 1**.
The exit-2 runs are the driver's own "false blocker" check: scoped rows `omp.catalogue.{found,matched,missing_names}`
declare `candidate_blocks 5723` while the driver's recomputation gives `5724` (later run `5769` vs `5770`) — both sides
re-census the live opencode session carrier, which grows during the run, so the gate races on host state. **When the race
does not fire the revisions are byte-identical** (base run3 vs candidate run3 differ only in the instrument path):
`agreement: 18/24 (mode-aware protocol headline; 28 live checks, 4 scoped out)`, `strict 14/24`, `disagree: 6`,
`scoped-out: 4`, live exit 1 with 21 PASS, independent exit 0 with 28 checks, and the same six disagreements
(`oc.roots.names_plus_builtin` expected 10 vs observed 12; `omp.cache.misses` 3/4; `omp.cache.verified_skills` 7/11;
`omp.descriptions.over_cliff` 10/11; `omp.descriptions.unmodelled` 3/0; `omp.offered.skills` 10/11). The join is **not
clean at either revision**; the `oc.roots.names_plus_builtin` row is the routed production-marker disagreement and stays
routed.

**F3 — The candidate is inert on this host, so the battery cannot detect the fix in either direction.** The fix unions
`<oc-config>/skill` and `<oc-config>/skills`; the instrument's default `--oc-config` is `/home/vgpnk/.config/opencode`,
which has **neither** directory (only `cli.json`, `opencode.json`, `service.json`). Measured: the independent instrument
reports `oc.roots.names_plus_builtin = 10` at base **and** at candidate.

**F4 — Committed ruler reproduces the claim's before/after in my clones.** `python3 -B .ufo/round-48/tools/config-root-ruler.py`
(oracle `1d09a38c…`, before receipt `8bec447a…`): base `75f671b` → exit **1**, `verdict failed`, `target_failures
[singular-unlogged, plural-unlogged, both-distinct-unlogged, same-name-both-config-roots, configured-plus-other-log-root]`,
`behavioral_mismatches []`; candidate `26035dc` → exit **0**, `verdict clean`, `target_failures []`,
`behavioral_mismatches []`; 13/13 cases settled at both revisions. Recomputed from the receipts: all **27 non-target
check values and all 28 statuses (24 DERIVED / 4 SCOPED_OUT)** equal the same-run `control-agents-only` case and the
committed before receipt in **13/13 cases at both revisions**; only the target row moves (`singular-unlogged` 2→3,
`plural-unlogged` 2→3, `both-distinct-unlogged` 2→4, `same-name-both-config-roots` 2→3, `configured-plus-other-log-root`
3→4); the 8 controls are unchanged. Receipts
`/fast/scratch/hyaku/kotoba-r48-a2/seats/nh-ruler-{base,cand}-2/receipt.json` (copies in `nh-evidence/`).

**F5 — Q05 unmet at the candidate commit, measured by mutation: the consumer's `--self-test` was blind to the fix.**
The candidate diff is 21 lines in one file, touching only `derive()`; the `--self-test` region is unchanged and prints
`0 failure(s) over 104 assertions` at both revisions. Mutating the candidate back to the base line
(`sorted(sources | configured):` → `sorted(sources):`) still prints `0 failure(s) over 104 assertions`, **exit 0** —
identical to the unmutated candidate. No self-test fixture creates `<oc-config>/skill` or `<oc-config>/skills`
(`build_fixture` writes only `<config>/opencode.json`; the mutant fixtures write only `opencode.json` plus one JSON
mutation), so the new path was never exercised — a green `verify_harness_independent.py --self-test` row therefore
carried **zero** coverage of the change (closed at the landed revision, see F10).

**F6 — Pre-existing lane failures, identical at both revisions (not candidate-induced).** `verify_skill_checklist.py
--json`: 9 PASS / 2 FAIL — `trigger.citation_resolves` (`../.ufo/reports/round-7/kotoba.md`) and
`governance.citation_resolves` (`../.ufo/reports/round-9/kotoba.md`, `../.ufo/reports/round-11/kotoba.md`,
`../PROTOCOL.md`, `../.ufo/l0-questions.md`); those targets are **not committed** in the lane (`git ls-files .ufo` starts
at `round-20`; `PROTOCOL.md` and `.ufo/l0-questions.md` absent), so the failure is real lane state.
`verify_surfaces.py --json`: 5 PASS / 2 FAIL — `surfaces.literal_present` (8 loader literals not verifiable from the omp
dump) and `surfaces.no_uncovered_class` (0 of 8 declared loader classes extracted; extractor blind on 33 declared
literals). `check_substrate_pins.py`: `DRIFT 2/3` — `omp_binary_sha256` expected `fdbc8136…`, got `85d9daf3…`;
`omp_binary_mtime` drift; `opencode_binary_sha256` PASS. **F7 — Checkout-directory artifact removed.** In a tree whose
final directory is not `kotoba-shokunin`, `verify_skill_checklist.py --json` adds a third failure (`name 'kotoba-shokunin'
!= directory 'base'`; 8 PASS / 3 FAIL instead of 9 PASS / 2 FAIL). This report's numbers come from clones whose final
directory **is** `kotoba-shokunin`; the artifact is identical on both revisions and changes no exit code.

**F8 — Unmeasured, bounded no-harm risk in the candidate's shape (one-directional delta, unbounded magnitude).** The
candidate enumerates the **singular** configured root `<oc-config>/skill`; the live producer enumerates only the plural
`~/.config/opencode/skills` (`verifiers/verify_harness_claims.py:472`). Where the singular directory exists and is
populated, the independent row rises **above** the live value and the `mode=equal` row `oc.roots.names_plus_builtin`
becomes a new disagreement the pre-fix instrument did not have; the candidate bounds no delta. Neither directory exists
here, so this is a risk, not a measurement.

**F9 — Custody.** My first scratch tree under `/fast/scratch/hyaku/kotoba-r48-a2/seats/C1NoHarmBattery/` was partially removed mid-run by an unidentified cleaner (ruler scratch, runner script and two worktrees gone; `out-base/`,
`out-cand/`, `ind-*.json` survived). I rebuilt both revisions as fresh clones in `/tmp/kotoba-nh-20261022/` and re-ran
every gate there; all numbers here come from that durable run (both worktrees `git status --short` clean after the battery).

**F10 — The lane advanced during this run; the landed C1 revision closes F5 and the battery still holds there.** Lane
HEAD is now `84b9c9b`, containing `d1ae458` ("independent instrument enumerates --oc-config/skill and skills direct
children … with self-test arm incl. nested discriminator; harness_independent floor 104->115"). Measured at that HEAD:
consumer sha256 `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`, `--self-test` =
`0 failure(s) over 115 assertions` exit 0 (arm present — F5 closed there); the nine gates give the same exit codes as base
and candidate (last table column), floors now read `harness_independent 115/115`, `corpus_integrity 150/150`,
`corpus_independent 91/91`, `surfaces 99/99`, `checklist 1845/1845`, `pins 62/62`, `compare_harness_independent 330/330`,
`floors_guard 150/150`; the live join is byte-identical to the candidate's (`18/24`, `disagree 6`) apart from the
instrument path. **Action for the L1:** the ruler is pinned to consumer sha256 `2d824c0b…` (candidate) but the landed
consumer is `d67b1b6e…`, so `--consumer-sha256` must be re-pinned and the ruler re-run against the landed revision before
the C1 receipt is frozen.

## Gate battery table (each cell: exit — headline; no gate timed out)
| Gate | base `75f671b` | candidate `26035dc` | landed `84b9c9b` | changed? |
|---|---|---|---|---|
| `verify_harness_independent.py --self-test` | 0 — `0 failure(s) over 104 assertions` | 0 — `0 failure(s) over 104 assertions` | 0 — `0 failure(s) over 115 assertions` | no (arm added at landing) |
| `check_assertion_floors.py` | 0 — 6 floors PASS (surfaces 99, checklist 1845, pins 62, harness_independent 104, compare_harness_independent 330, floors_guard 150) | 0 — same 6 floors PASS | 0 — 8 floors PASS (harness_independent 115, corpus_integrity 150, corpus_independent 91 added) | no |
| `verify_skill_checklist.py --json` | 1 — `pass 9 / fail 2` (citation_resolves ×2) | 1 — `pass 9 / fail 2` (same 2 ids) | 1 — `pass 9 / fail 2` (same 2 ids) | no |
| `verify_skill_checklist.py --self-test` | 0 — `0 failure(s) over 1845 assertions` | 0 — `0 failure(s) over 1845 assertions` | 0 — `0 failure(s) over 1845 assertions` | no |
| `verify_corpus_integrity.py --json` | 0 — all rows PASS, `exit_code 0` | 0 — all rows PASS, `exit_code 0` | 0 — all rows PASS, `exit_code 0` | no |
| `verify_corpus_independent.py` | 0 — `exit 0` (5 `!` notes, identical) | 0 — `exit 0` (identical notes) | 0 — `exit 0` | no |
| `check_substrate_pins.py` | 1 — `DRIFT 2/3` (omp sha + mtime; opencode sha PASS) | 1 — same DRIFT 2/3, same hashes | 1 — same DRIFT 2/3 | no |
| `verify_surfaces.py --json` | 1 — `pass 5 / fail 2` (literal_present, no_uncovered_class) | 1 — `pass 5 / fail 2` (same 2 ids) | 1 — `pass 5 / fail 2` (same 2 ids) | no |
| `compare_harness_independent.py` (default live join) | 2, 2, 1 — `false blocker` (carrier census race) ×2, then `18/24`, `disagree 6` | 1, 1, 1 — `18/24`, `disagree 6` every run | 1 — `18/24`, `disagree 6` | values identical when the race does not fire; exit code is host-race dependent (F2) |

## Evidence (commands, exit codes, hashes)
```
# trees: git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/kotoba-nh-20261022/{base,cand,landed}/kotoba-shokunin
#   base -> checkout 75f671b109d8eddd0d64c1429bd6379fe577175a ; cand -> fetch /fast/scratch/hyaku/kotoba-r48-a2/cand
#   26035dcec54d8e42f3a8b47ae8ca551c18aec295 and checkout it ; landed -> lane HEAD 84b9c9b
# battery: per gate, cd <tree> && timeout 900 python3 -B <verifier> <flags>   (runner /tmp/kotoba-nh-20261022/run_battery.sh)
bash /tmp/kotoba-nh-20261022/run_battery.sh /tmp/kotoba-nh-20261022/base/kotoba-shokunin base
bash /tmp/kotoba-nh-20261022/run_battery.sh /tmp/kotoba-nh-20261022/cand/kotoba-shokunin cand
bash /tmp/kotoba-nh-20261022/run_battery.sh /tmp/kotoba-nh-20261022/landed/kotoba-shokunin landed
# live-join repeats: cd <tree> && timeout 900 python3 -B verifiers/compare_harness_independent.py
#   base EXIT=2,2,1   candidate EXIT=1,1,1
# mutation test (Q05 blindness)
cp -a /tmp/kotoba-nh-20261022/cand/kotoba-shokunin /tmp/kotoba-nh-20261022/mutant-no-union   # line 609 -> sorted(sources)
cd /tmp/kotoba-nh-20261022/mutant-no-union && timeout 900 python3 -B verifiers/verify_harness_independent.py --self-test
#   -> "0 failure(s) over 104 assertions"  EXIT=0   (identical to unmutated candidate)
# ruler A/B (committed ruler/oracle/receipt; --repo /tmp/kotoba-nh-20261022/cand/kotoba-shokunin), run twice:
#   base      --revision 75f671b109d8eddd0d64c1429bd6379fe577175a --consumer-sha256 872993f8...
#              --scratch /fast/scratch/hyaku/kotoba-r48-a2/seats/nh-ruler-base-2   -> EXIT=1 verdict failed
#   candidate --revision 26035dcec54d8e42f3a8b47ae8ca551c18aec295 --consumer-sha256 2d824c0b...
#              --scratch /fast/scratch/hyaku/kotoba-r48-a2/seats/nh-ruler-cand-2   -> EXIT=0 verdict clean
#   both add: --oracle .ufo/round-48/oracle/config-root-cases.json --oracle-sha256 1d09a38c...
#             --baseline-receipt .ufo/round-48/verification/before-configured-root.json --baseline-sha256 8bec447a...
```

Digests: base consumer `872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1`; candidate consumer
`2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a`; landed consumer `d67b1b6e9ba0e614f643adda2686c9db8d57c31741de01780be3fcb06c4f7937`;
oracle `1d09a38ce04d6c0ab9a1c4edd7f4255978a0c2b8d44ce037d10fcd37d756b883`; before receipt
`8bec447aa538446e84b7cb87b902c5f1021c42bd7a01f81ea14313262f7e2312`; ruler `01af33a6724cb91ddcfd09b690fa7ba68114d799cc4552fa65d6519c3f78bd45`.

## Risks / blockers
- **R1** — No-harm for the candidate is measured and holds across the battery and the ruler matrix; nothing in the
  battery blocks the change, and the landed revision (F10) holds too.
- **R2** — The battery is a no-harm instrument, not a sensitivity instrument: the fix is inert here (F3) and the
  candidate's `--self-test` was blind to it (F5). A green `--self-test` must not be cited as evidence that the fix works
  or is protected; only the ruler's synthetic matrix measures the change.
- **R3** — The live-join gate's exit code is a host race (F2); quoting one exit code for it is unsafe. The stable content
  is `18/24`, `disagree 6`, identical at all three revisions, with the routed built-in-marker row still open.
- **R4** — The ruler measurement is pinned to candidate consumer sha256 `2d824c0b…`; the landed consumer is `d67b1b6e…`
  (F10), so `--consumer-sha256` must be re-pinned and the ruler re-run against the landed revision before the C1 receipt
  is frozen.
- **R5** — F8's singular-root overshoot is unmeasured on this host; exercise it with a populated `<oc-config>/skill` and no `<oc-config>/skills` before calling the change harmless in general.
