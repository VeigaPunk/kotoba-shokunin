# Kb80Y01Simplify — C1 stack minimization (kotoba round 80, wave w1)

Seat: simplifier (leaf). Scope: the C1 repair stack, E01–E06 (`SKILL.md` registry rows, the LOG symlink, index/baseline,
the E04 `<rev>:` report-pointer fix, the external-commit grammar class, erratum E5). Base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; all work in `/fast/scratch/hyaku/kotoba-r80/Kb80Y01Simplify`
(removed at yield). Deliverable tip `019f27ab199ad79f488fb388a0abe8f7fe1ca0ba` (detached measurement commit).

**Build outputs for E01–E06 did not exist when I started** (`.ufo/waves/round-80/build/` empty of them), so I derived
the whole stack from the r79 drafts and the plan, then minimized it. `Kb80E02Symlink.patch` and `Kb80E04DeadPointer.patch`
landed while I worked; my application of the r79 drafts is byte-identical in effect (E02 is the same patch; E04 produces
the same report_dead=0). Every number below is from a command whose own exit status I captured, never a pipeline's.

## 0. Shipped result (one line)

`.ufo/waves/round-80/build/Kb80Y01-simplified.patch` (sha256 `a601254cc4db8edb4ebd594a8389f1bcf7cc7a4fb1831ec9d04943748cfd73a2`)
applies clean to `398cbe1` and carries the stack at **59 added / 10 deleted instrument lines** (cap 60) with a
**20-line** grammar class (declared budget 21). At `019f27a` the round-80 counter prints
`guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0, in BOTH the `--repo .` and the absolute `--repo <lane>` form
(`Kb80Y01-tipbattery-final-dot.txt`, `Kb80Y01-tipbattery-final-abs.txt`), and at base `398cbe1` the amended counter
prints `guards 5 of 5; tip battery exit 0: 1 of 6`, exit 1 (`Kb80Y01-tipbattery-base-amended.txt`) — the plan's
frozen 1→6 movement, measured on the amended bytes.

## 1. Calibration: the plan's trigger names the wrong tokens

Both corpus gates at `398cbe1` read `commit_unresolvable = 2`, and the two tokens are
**`corpus/SOURCES.md:171` and `:172`, both `7bb48f213ac677f943d5c791199ed3dddf302f00`** (rows S230/S231, pi-mono /
mistral-vibe), not the plan's `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`
(`Kb80Y01-base-integrity.json`, `Kb80Y01-base-independent.json`). The plan-named forms are `commit_quoted` context —
code-span/quoted meta-findings — and are never unresolvable. Two further facts any grammar class must face:

- `commit `owner/repo@<hex>`` is **one token**; neither gate extracts a hex from it, so it lands in `commit_nonhash`
  (a zero-mode check), not `commit_unresolvable`. A class keyed only on the in-token `@` clears nothing at base and
  leaves reviewers' P02/P18-shaped probes red.
- A live `owner/repo@<hex>` with no `commit` keyword is not tokenized at all (measured: `cited at o/r@`deadbee`` →
  `commit_total=0`).

Other base truths I measured (own exits): registry `60 of 62` exit 1; integrity 3/9 checks with six DRIFTs
(`tracked_files` 152≠144, `unindexed` 1, `report_total` 109≠99, `report_dead` 1, `commit_total` 46≠43,
`commit_unresolvable` 2); independent exit 1. The checklist gate is red in a bare clone for a *different* reason
(`../.ufo` is the fleet root, and the r79 spot-check lesson is unindexed); the tip battery's fleet-shaped sandbox is
the measurement that counts, and there the only base reds are the five gates above.

## 2. Candidates: removal diff, re-run receipt, verdict

| # | Candidate | Removal diff | Re-run receipt | Verdict |
|---|---|---|---|---|
| 1 | the two `SKILL.md` withdrawal rows (`check_desc_craft.py`, `check_r75_routed_repairs.py`) | 2 rows deleted (`Kb80Y01-candidate-diffs.txt` exp4) | `check_gate_registry.py --rev HEAD` → `60 of 62`, exit 1 (`Kb80Y01-exp4-no-rows.txt`) | **REQUIRED** |
| 2 | the Q46 parenthetical ` (declared r76, never landed)` in both withdrawal cells | 2 cells shortened, same 8-cell form | registry `62 of 62`, exit 0; `grep -c "claim withdrawn r79 before data; not a claim gate" SKILL.md` → 2 (`Kb80Y01-exp5-short-rows.txt`) | **REMOVABLE** — shipped |
| 3 | the third registry row for `verifiers/check_allowed_tools.py` | 1 row deleted (`Kb80Y01-candidate-diffs.txt` exp6b) | with file+row `63 of 63` exit 0 (`exp6a`); file present, row removed `62 of 63` exit 1 (`exp6b`) | **REQUIRED once the C2 counter lands** (absent in my tree, hence 62/62) |
| 4 | the E04 `<rev>:` hunk in `report_pointer_exists` | 6 lines deleted (`candidate-diffs` exp1) | `report_dead=1` → `DRIFT corpus.pointers.report_dead`, exit 1 (`Kb80Y01-exp1-e04-drop.txt`) | **REQUIRED** |
| 4b | E04's 11-line self-test arm | 11 lines deleted | gate still exit 0 (the arm is verdict-insensitive) | **REQUIRED by plan conjunct** ("with its red-before regression arm"); folding it into the existing citation fixture would rewrite ~6 `eq()` expectations — not smaller |
| 5 | the `corpus/README.md` coverage row for `round-79-verifier-spotcheck.md` | 1 row deleted (`candidate-diffs` exp3) | `unindexed=1` → `DRIFT corpus.index.unindexed`, exit 1 | **REQUIRED** |
| 5b | the baseline refresh | restore the pre-repair baseline | 3 DRIFTs (`tracked_files`, `report_total`, `commit_total`), exit 1 (`Kb80Y01-exp2-baseline-stale.txt`) | **REQUIRED** |
| 6 | the grammar class, 28-line first draft | — | `67` added instrument lines → over cap (numstat) | **REJECTED form** |
| 6b | the class plus the two plain-output detail prints (62-line variant) | — | `62` added → `FAIL guard instrument-size: instruments gain 62 lines > 60` (plus two `instrument-pin` failures, expected for unpinned synthetic bytes), `guards 3 of 5`, exit 1 (`Kb80Y01-tipbattery-62line-dot.txt`) | **REJECTED form** |
| 6c | single-line regex + both class halves + one 2-line arm per gate | — | `59` added → guards 5 of 5, 6 of 6, exit 0 both forms | **SHIPPED form** (grammar 20 ≤ 21) |
| 7 | erratum E5's self-test arm updates ("no other line") | revert arms to hardcoded `41`/`40`/`60`/`40` | `--self-test` → 4 failures: `size world exits 1: exit 0`, its name check, `stub world exits 1: exit 0`, its name check (`Kb80Y01-exp7-bare-cap-selftest.txt`) | **REQUIRED** — the plan's "no other line" is unsatisfiable; arms shipped cap-derived (`range(LINE_CAP + 1)`, `padding=LINE_CAP + 1`, expectations formatted with `LINE_CAP`) |
| 8 | erratum E5's pin additions | drop the two round-80 blobs from the tuples | 2× `FAIL guard instrument-pin` (`Kb80Y01-guard-probes.txt` probe B); with `LINE_CAP=40` also `instruments gain 59 lines > 40` (probe C) | **REQUIRED** |

### The grammar class as shipped (20 added lines, both gates)

Three alternatives, one single-line regex, one routing expression per token class:

- (a) the line is a SOURCES row whose first cell carries `raw.githubusercontent.com/<o>/<r>` or `github.com/<o>/<r>`;
- (b) a backticked `owner/repo` immediately before the `commit` keyword (`` `badlogic/pi-mono` commit `7bb…` ``);
- (c) the token itself is `owner/repo@<hex>`, routed out of `commit_nonhash`.

Red-before retained (`Kb80Y01-discrimination.txt`): a SOURCES row whose URL is a docs host (`agentskills.io/specification.md`),
a bare `commit deadbee`, a reversed `hex@owner/repo`, `HEAD:path`, a 41-hex token — all stay unresolved or nonhash.
Lane/fleet hex tokens keep their exact current resolution. The `owner/repo@<hex>` half cost 2 lines and was funded by
dropping the two **plain-output detail prints**; the INFO count and detail remain in the gates' `--json` observed
(`commit_external`, `commit_external_detail`) and in the `observed` block receipts.

## 3. Shipped patch contents

`.ufo/reports/round-76/kotoba.md` (relative symlink, new), `SKILL.md` (+2 withdrawal rows, Q46-shortened),
`corpus/README.md` (+1 coverage row), `verifiers/verify_corpus_integrity.py` (27+/4−: E04 17, grammar 10),
`verifiers/verify_corpus_independent.py` (10+/3−: grammar 10), `verifiers/check_tip_battery.py` (18+/7−: `LINE_CAP`
40→60, two pins, cap-derived arms), `verifiers/corpus-baseline.json` (refresh at the clean tip:
`tracked_files 144→152`, `report_total 99→109`, `commit_total 43→46`, every zero-mode class 0).
Instrument numstat over the pinned base `072048fa`: `22/3` floors + `27/4` integrity + `10/3` independent =
**59 added / 10 deleted** (`Kb80Y01-instrument-numstat.txt`).
Pins at `019f27a`: integrity `cc182613a4d089c41e44f11b50e03b45ce582dd8`, independent
`89f392daab3e4181db3ded7676ca0879871ef7ff`.

## 4. What the L1 must redo at integration (conditions, not suggestions)

1. **Pins are freeze bytes.** They are valid only for these instrument blobs. Re-derive with
   `git rev-parse <rev>:verifiers/<file>` at the final integration tip if any E-seat edits those files, and append to
   the tuples (two stale-pin runs cost me two battery passes — both exits 1 with `instrument-pin`).
2. **Refresh the baseline last.** `refresh-corpus-baseline.py` refuses (exit 2) on a nonzero zero-mode class; order
   rows → E04 → E05 → refresh → battery, and refresh AFTER every corpus file has landed (the C2 entry/counter change
   `tracked_files`).
3. **The third registry row must land with the counter.** Measured: file+row `63 of 63` exit 0; file without row
   `62 of 63` exit 1. Rows must sit INSIDE the `## Gate registry` table — a row after the table's blank line is
   invisible to the gate.
4. **The C2 entry's bare-name citation reds both gates.** `served from commit `7bb48f21…`` on a line whose only repo
   hint is the bare name `mistral-vibe` stays `commit_unresolvable`; write `` `mistralai/mistral-vibe` commit `7bb…` ``
   (backticked owner/repo, form (b)) instead. Do not widen the class to bare names: it is unbounded laundering.
5. **Narrow the plan's grammar prose by erratum.** The `owner/repo@<hex>` shape is not a hex token in either tokenizer,
   so the class is "repo-qualified `commit <hex>` citations (SOURCES row, or a backticked `owner/repo` before the
   keyword) plus `owner/repo@<hex>` tokens". Say it that way, or a reviewer probe (Kb80L01's P02/P18) reads as a
   miss against the current wording.
6. **Measurement hazard (new, beyond M80-1).** `--rev HEAD` in a tree you are still committing to can make the two
   forms read different revs: one command returned dot exit 1 and abs exit 0 against different shas. Measure a fixed
   sha.
7. Q46 remains rule-only: the registry gate is blind to the withdrawal annotation (sibling mutation
   `Kb80M04Registry-mut4-withdrawal-annotation-dropped.patch` survives it). Keep the annotation, but do not claim the
   gate enforces it.

## 5. Limits

I did not measure the integrated tree: my tree has neither `corpus/knowledge/allowed-tools-surfaces-round80.md` nor
`verifiers/check_allowed_tools.py`, so the third-row and entry-citation findings are measured as isolated probes
(exp6a/exp6b, matrix) rather than in the landed tree. The C2 counter's own 0→6 value is out of my scope. No tool
installs or upgrades were needed.

One limit of the shipped class, stated so it is not over-read: it is **attribution-blind**. It promises "this token is
a third-repository citation", not "this token belongs to the repository named beside it". A live example is the S230
anchor (`corpus/SOURCES.md:171`), which names pi-mono but carries mistral-vibe's commit `7bb48f21…` (Kb80E08C2Entry,
read from both fetch records). The class files it as `commit_external` INFO and no corpus gate reds on the
mis-attribution; the correction belongs in the round-80 lesson's erratum, not in the gates.

Not mine, and not removed (I did not create it): the lane now carries a stray **file** `.ufo/wapes` (594 B, 20:17) —
an accidental redirect from a seat's probe (`words=11 ok=False why='quote lies in the first-heading block (Q70)'…`),
i.e. the msaf Q70 probe written one directory name off. It is untracked, lives outside `corpus/`, and changes no gate
verdict, but it is debris the owner should delete; a `rm .ufo/wapes` by whoever owns that probe.

VERDICT: The C1 repair stack is minimal at 20 grammar lines / 59 instrument lines (cap 60/21): the two withdrawal rows, the third row, E04 and its arm, the coverage row, the baseline refresh, the E5 pins and cap-derived arms are all REQUIRED; only the Q46 parenthetical is removable; the plan's grammar wording must be narrowed because `owner/repo@<hex>` is not a hex token in either gate.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80Y01Simplify.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-simplified.patch, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-candidate-diffs.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-instrument-numstat.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-discrimination.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-guard-probes.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-tipbattery-final-dot.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-tipbattery-final-abs.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80Y01-tipbattery-base-amended.txt
