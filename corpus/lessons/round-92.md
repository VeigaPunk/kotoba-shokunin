# Round 92 — kotoba (Linux host, omp 18.15.0): lesson

Author: **ScribeCorpusR92** (scribe seat). This file is the round-92 **scaffold**: the Gate record,
the Mistakes row and the Considerthese entry below are written; **the L1 completes the settlement**
(the seat record, the claim verdicts, the wave disposition and the final numbers).
Round: 92, plan `plans/round-92.md` (frozen at `e073723ae667b64e534f8621bddb83ad12ad0e71`), base
`e073723ae667b64e534f8621bddb83ad12ad0e71`.
Pre-data controls: `plans/round-92-controls.md`, executed before any candidate score — receipt
`.ufo/waves/round-92/receipts/freeze-gate-r92.txt` (`freeze gate: 6 control(s) held — freeze may
proceed`, exit 0).

## Gate

Candidates considered, with the decision and the reason:

- **S265** — Python documentation, `subprocess`
  (`https://docs.python.org/3/library/subprocess.html`). **Admitted** as tier A, as a
  *correction row* that supersedes S263: the page is unchanged in substance, and the only defect
  the round-91 spot-check routed (its defect 4) is an anchor line in the S263 row, not a wrong
  claim. Access date 2026-11-05; HTTP 200; 208648 B — byte-identical to the round-91 reading, with
  the same page footer "Last updated on Nov 05, 2026 (12:47 UTC)." at HTML line 2037. Located
  quote (§ `subprocess.run`, HTML lines 289-291, 25 words): "If the timeout expires, the child
  process will be killed and waited for. The TimeoutExpired exception will be re-raised after the
  child process has terminated." Contrast quote (§ `subprocess.Popen.communicate`, HTML line 1071
  continuing to 1072, 10 words): "The child process is not killed if the timeout expires".
  - **Why a new row and not an edit to S263** — the SOURCES contract is append-only: a correction
    lands as a new row whose `teaches` cell opens `supersedes S263 — `, naming the corrected
    anchor; the superseded row keeps its own bytes. The corrected anchors are the `Popen.communicate`
    entry dt at **HTML line 1051** (signature line 1052) and the contrast quote at **HTML line
    1071**; S263's cited line 1042 is a `versionchanged` note belonging to the preceding
    `Popen.wait` entry, not the contrast quote. The `subprocess.run` entry dt (270) and its timeout
    paragraph (288-294, quoted sentence at 289-291) are unchanged. The kill-and-wait contract the
    cap calibration rests on is therefore unaffected — only the anchor line was wrong.
- **S266** — Python documentation, built-in exceptions
  (`https://docs.python.org/3/library/exceptions.html`, requested; the path answers **301** and
  lands on `https://docs.python.org/3/builtins/exceptions.html`). **Admitted** as tier A, scoped to
  *which exception the Python runtime raises when a path component is not a directory* — the
  grounding for the freeze gate's fail-closed work-root rung. Access date 2026-11-05; final HTTP
  200; 145885 B; page title "Built-in Exceptions — Python 3.15.2 documentation". The
  `NotADirectoryError` definition-list entry is at HTML line 1118 (signature line 1119, body
  1120-1124). Located quote (HTML lines 1120-1121, 17 words): "Raised when a directory operation
  (such as os.listdir()) is requested on something which is not a directory." The POSIX
  path-component clause is quotable in the same budget (HTML lines 1122-1123, 22 words): "it may
  also be raised if an operation attempts to open or traverse a non-directory file as if it were a
  directory." The errno correspondence is `ENOTDIR` (line 1124); the exception-hierarchy tree places
  the entry under `OSError` (HTML line 1440) at HTML line 1452, inside the tree block that opens at
  line 1416.
  - **Why the exception class and not a general filesystem row** — the round's C2(b) rung 1 is the
    `--work` argument resolving under a regular file. What the gate must translate is one named
    environment exception, `NotADirectoryError` (an `OSError` subclass), so the row is scoped to
    that class and to the path-component case the POSIX clause states, not to path handling in
    general. The page names exactly one `os` function for this exception — `os.listdir()` (line
    1120); the adjacent `os.remove()` mention at line 1112 belongs to `IsADirectoryError` and is
    **not** attributed here.

**No candidate was rejected this round.** Both candidates are tier-A official documentation whose
located quotes were re-verified against the bytes the scout fetched; no row carries a `rejected`
status, and no flip condition is open.

**Census before → after.** Rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **190** before this round (receipt `.ufo/waves/round-92/census-before.txt`,
validate rc 0 with the 33 pre-existing W04 duplicate-URL warnings) and **192** after — the two
rows appended above (S265, S266), no row dropped, consistent with the plan's § Frontier
expectation of 190 → 192. Validation:
`bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md
--today 2026-11-05` → exit 0, the same 33 pre-existing W04 warnings and no E-code.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| `vacuous` (**the L1-confirmed row**) — a frozen pre-data control reads MET on the shortcut it names: `ctl-c2-capline-only` (cap raised to 360, no `INSTRUMENT_PINS` admission) prints `C2-PREDICATE-MET`, exit 0; the control reads only the working-tree cap, so it never refuses the shortcut world it declares | `.ufo/waves/round-91/w1/CriticClaims.md` § Controls (the shortcut-check table names the same control as a **control defect**: it reports MET for the shortcut it is declared to refuse) and `verifiers/fixtures/round-91/ctl-c2-capline-only.sh`; the round-92 red-before receipt `.ufo/waves/round-92/receipts/redbefore-ctl-c2.txt` re-observes the defect at this round's base bytes | Q37's gap: a control need not refuse its own shortcut — Q37 requires the cheapest real-input shortcut to be built and run under the frozen predicate, but not that the control *refuses* the failing conjunct of that shortcut, so the control was satisfied in form while reading MET on the shortcut it names | `plans/round-92.md` C1 — the shortcut world is committed and the public gates read it, so the control refuses its own shortcut instead of restating a threshold; the row is confirmed by the L1 in the round-92 plan (the same routed defect the plan carries as C1's red-before) |
| `landing`: a candidate patch rewrote a source line that a frozen battery manifest row anchors on, and the patch's owner did not own the manifest row; the candidate's battery aborted with rc 2 (`anchor miss: fg-x1-parse-drop-exit-clause`), so the frozen C1 honest world read UNMET on the candidate | `.ufo/waves/round-92/w1/CriticClaimsR92/CriticClaimsR92.md` § Defects D1 (anchor replay: base 19 edits 0 mismatches, candidate 1); `.ufo/waves/round-92/w1/MutTesterBattery/MutTesterBattery.md` F-1; repaired and re-measured `.ufo/waves/round-92/receipts/landing/bat-rev.txt` (`killed 17 of 17`, rc 0) | none — the plan's no-harm battery ran at base only (Q65), and Q72's post-state run needs the candidate, which did not exist at freeze; no builder ran the frozen battery manifest against its own patch | `plans/round-92-addendum-1.md` A1: the rung-3 check moved above the anchored two-line sequence, which is restored byte-identical; the frozen manifest row is untouched; `INSTRUMENT_PINS` admits the repaired blob. The able-to-fail reading is the pre-repair candidate's `ctl-c1-honest.sh` → rc 2 (critic receipt) |
| `plan-text`: the frozen plan's own sentences were wrong in three places — `verifiers/fixtures/freeze-gate/r88-controls.md` named as the honest world that "still exits 0" (it is the refusal fixture), the landing conjunct "corpus integrity rc 0" (base reads rc 1, 4 of 9), and the floors drift arm named in `--self-test` (it fires in the guard run) | `.ufo/waves/round-92/w1/ReviewerFloors/ReviewerFloors.md` R1; `.ufo/waves/round-92/w1/MutTesterBattery/MutTesterBattery.md` F-2, F-3; `.ufo/waves/round-92/w1/CriticClaimsR92/CriticClaimsR92.md` D4, D5; `.ufo/waves/round-92/receipts/base-corpus-integrity.txt` | none — Q19 re-measures before-values, but no criterion re-reads a plan's own honest-world and landing sentences against the bytes they name before the freeze | `plans/round-92-addendum-1.md` A2 (errata; no predicate, counter, control or manifest byte changed); the honest world and the landing DRIFT conjunct are restated in the addendum from the measured bytes |
| `receipt-pointer`: the frozen plan cited three receipts that were never produced at the cited paths (`receipts/nowork-c1-controls.txt`, `receipts/q73-sweep.txt`, `receipts/census-before.txt`) | `.ufo/waves/round-92/w1/ReviewerCtl/ReviewerCtl.md` R12; `plans/round-92-addendum-1.md` A2(iv) | Q68 (a report is opened by a command before it is filed) covers reports, not a plan's own pointers | `plans/round-92-addendum-1.md` A2(iv) maps each to the produced receipt (`redbefore-ctl-c1/c2.txt`, `q73-sweep-raw.txt`, `.ufo/waves/round-92/census-before.txt`) |
| `late-write`: the round-91 `ReviewerRepairs` seat wrote its output after the round-91 lesson recorded "no late files" (mtime 14:49, after the settlement), and the files sat untracked in the lane | `.ufo/waves/round-91/w1/ReviewerRepairs.md` and `ReviewerRepairs/review.md` (mtime 14:49:34 and 14:49:57); `git status --porcelain` at round-92 start | Q40 and Q49 require a final sweep after the last seat write; the round-91 closure ran its sweep before this write | committed as round-92 wave evidence for round 91 with disclosure, not deleted (`plans/round-92-addendum-1.md` A6); the round-91 "no late files" line is corrected there |
| `scope-drift`: the scribe's README edit rewrote an existing index row's cell instead of appending only new index rows (the `Admission bar (round 46)` row) | `git diff -- corpus/README.md` at the scratch integration commit (scribe patch hunk `@@ -57`); reviewed by `.ufo/waves/round-92/w1/CriticClaimsR92/CriticClaimsR92.md` D6 | none — the scribe's ownership text allowed "index rows" and the sentinel's byte scope check named files, not cells | reverted at integration to the base row text; `corpus/README.md` keeps only the new round-92 lesson row |

## Status changes

- **S263 — corrected by S265** (new row, `mined`, opened 2026-11-05, recheck `180d`). The
  correction is the anchor line only: S263 cites the `Popen.communicate` contrast quote at HTML
  line 1042; on today's byte-identical page (HTTP 200, 208648 B, same footer timestamp at line
  2037) that line is a `versionchanged` note of the preceding `Popen.wait` entry, while the
  `Popen.communicate` entry dt is at line 1051 and the contrast quote at line 1071. The quote text,
  its section, and the teach are unchanged, so the kill-and-wait contract the cap calibration
  rests on stands; only the anchor line was wrong (the round-91 spot-check's routed defect 4).
  S263's own row bytes are **not** rewritten — the correction lands as the appended row, per the
  SOURCES contract's append-only rule for a cited token.
- **S266 — new row**, `mined` at opening (2026-11-05), tier A, kind `docs`, recheck `180d`, used-by
  `corpus/lessons/round-92.md`. No other row's `status`, `recheck` or `used-by` cell changed.

## Sources

- **S265** — Python documentation, `subprocess`; URL
  `https://docs.python.org/3/library/subprocess.html`; access 2026-11-05; HTTP 200; 208648 B
  (byte-identical to the round-91 reading); page footer "Last updated on Nov 05, 2026 (12:47 UTC)."
  at HTML line 2037; located quote at HTML lines 289-291 (25 words) and the contrast quote at HTML
  line 1071 (10 words), the `Popen.communicate` entry dt at HTML line 1051, the `subprocess.run`
  entry dt at HTML line 270 and its timeout paragraph at HTML lines 288-294. Tier A scoped; a
  correction row superseding S263 (anchor repair only). Status `mined`; used-by
  `corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md`.
- **S266** — Python documentation, built-in exceptions; URL requested
  `https://docs.python.org/3/library/exceptions.html` (HTTP 301), effective
  `https://docs.python.org/3/builtins/exceptions.html`; access 2026-11-05; final HTTP 200; 145885 B;
  page title "Built-in Exceptions — Python 3.15.2 documentation"; located quote at HTML lines
  1120-1121 (17 words) and the POSIX path-component clause at HTML lines 1122-1123 (22 words), the
  `NotADirectoryError` entry dt at HTML line 1118, the exception-hierarchy tree at HTML lines 1440
  and 1452, and the `errno.ENOTDIR` correspondence at HTML line 1124. Tier A scoped to the
  non-directory path-component exception class. Status `mined`; used-by
  `corpus/lessons/round-92.md`.

## Considerthese

`considerthese/2026-10-26.md` was re-read (proposals only; nothing implemented).

- **No proposal implemented this round.** Both claims are instrument-deepening with frozen
  predicates, so no proposal of this file is inside either claim's scope, and no proposal is
  implemented outside them.
- **Proposal 3** (land the page round 74 rejected and use it on the skill's own description) stays
  carried: it needs a SKILL.md description rewrite, and the 600-line budget cannot absorb one —
  `SKILL.md` is already 600 lines / 92 672 B at the freeze (receipt
  `.ufo/waves/round-92/receipts/base-skill-size.txt`), so a rewrite of the frontmatter description
  has to be paid for by lines saved elsewhere, which is a claim-adjacent edit this round's frozen
  predicates do not admit.
- **Proposals 1, 4 and 5** (a byte/line ceiling; "do not close a round before its falsify wave
  runs"; a per-round evidence budget) are carried unchanged from the previous rounds; proposals 1
  and 5 are already mined as criteria Q78 and Q82 and are not re-mined here.

## Settlement (L1, KotobaR92)

**Seat record — wave `r92-w1` (one v1 wave, band 8–16, policy `scripts/hyaku/ufo-wave-policy.json`).**
Dispatch `.ufo/waves/round-92/r92-w1-dispatch.json` (12 spawn members, 0 resumes; ready file taken
and marker `.ready.dispatched` present). WAVE-DONE received: all 12 seats settled. The orchestrator
kernel restarted mid-wave, so `r92-w1-results.json` carries no per-seat output (its `note` says so);
the seat outputs are the files each seat wrote on disk, and every seat wrote its report: 12 of 12
(`ConnectorOverlapR92.md`, `CriticClaimsR92.md`, `ExecCtlWorlds.md`, `ExecKillPin.md`,
`ExecLadderR92.md`, `MutTesterBattery.md`, `MutTesterCtl.md`, `ReviewerCtl.md`, `ReviewerFloors.md`,
`ScoutPyDocs.md`, `ScribeCorpusR92.md`, `SentinelScopeR92.md`). Dead seats: none. Roles: executor 3,
scout 1, scribe 1, connector 1, reviewer 2, critic 1, mutation-tester 2, sentinel 1; attack seats
6 of 12 (50 %, ≥ 25 %); connector 1 (≤ 2); the L1 holds the § 3 planner seat (validator rejects it).
Round total 12; no residual call; no second wave.

**Integration (what the seats produced and what the landing kept).** The four builder patches
applied cleanly to the freeze base. The critic (CriticClaimsR92 D1) and the mutation-tester (F-1)
found one blocker: ExecLadderR92's rung-3 rewrite broke the frozen battery anchor
`fg-x1-parse-drop-exit-clause`, which made C1's honest world read rc 2. The L1 repaired it by moving
the rung-3 check above the anchored line (`plans/round-92-addendum-1.md` A1). Patches kept as
produced: ExecCtlWorlds (C1 worlds), ExecKillPin (C2a arm), ExecLadderR92 (C2b rungs, coupling),
ScribeCorpusR92 (S265, S266, Q83, lesson scaffold). L1 integration edits: the A1 repair, the
`INSTRUMENT_PINS` admission, the README row revert (D6), this settlement.

**Claim verdicts (measured at the landing revision `c679a631b3cc7f048a3627e2f79b0486190d45a4`; receipts `.ufo/waves/round-92/receipts/landing/`).**

- **C1 — consistency (calibration sub-axis), controls refuse their named shortcuts: MET.**
  `controls-run.stdout`: `round-92 controls: shortcuts refused 2 of 2; honest held 2 of 2`, rc 0.
  Stages (`controls-run.stderr`): C2-shortcut rc 1 met; C2-honest rc 0 met; C1-shortcut rc 1 met;
  C1-honest rc 0 met (`killed 17 of 17`, `C1-PREDICATE-MET`). Before (red, base receipts):
  `redbefore-ctl-c2.txt` `C2-PREDICATE-MET` rc 0 on the cap-only shortcut; `redbefore-ctl-c1.txt`
  `C1-PREDICATE-UNMET` rc 1 with the appended rows never read. Do-nothing control: the round-91 pair
  refuses 0 of 2 (the same two receipts; the 2-of-2 target is unreachable without the redesign).
  Score held at 10 (rubric maximum); the SCORECARD row carries the measured verdict.
  Carried: `F1` (MutTesterCtl) — the frozen counting does not pin a refused world's own exit code;
  a mutant that accepts rc 0 for a refused world survives the real-world counting.

- **C2 — depth (kill-set pin and the three freeze-gate rungs): MET, with one disclosed naming gap.**
  (a) Battery kill-set size pin. Landing: `bat-selftest.txt` `0 failure(s) over 28 assertions` rc 0
  (was 25); `landing-m6-dropped-row.txt`: one kill row dropped → `FAIL arm kill-set-size: … observed
  16 kill rows, pinned 17`, `1 failure(s) over 28 assertions`, rc 1 (before: `redbefore-m6-dropped-row.txt`,
  `0 failure(s) over 25 assertions`, rc 0). Disclosed (A3): the constant is a literal and the arm reads the
  working-tree manifest; a committed-revision dropped row is refused with rc 2 by the baseline check
  and does not name the arm (CriticClaimsR92 D2, routed to round 93).
  (b) Three fail-closed rungs. Landing (`landing-rungs.txt`): work root under a regular file → rc 2
  `COULD-NOT-EVALUATE --work …: not a directory` (before: uncaught `NotADirectoryError`, rc 1);
  `--work` naming a regular file → rc 2 (before: uncaught `FileExistsError`, rc 1); duplicate control
  name → rc 3 `INVALID SPEC: duplicate control dup (line 9)` (before: both pass, `freeze gate: 2 control(s)
  held`, rc 0); declared `exit 127` → rc 3 `INVALID SPEC … unobservable` (before: rc 2
  `COULD-NOT-EVALUATE … command not found (rc=127)`, the declaration never compared). Self-test
  `fg-selftest.txt` `0 failure(s) over 34 assertions` rc 0 (was 31); floors `floors-selftest.txt`
  `0 failure(s) over 176 assertions` rc 0; coupling 34 == 34 == 34 (registry, two in-file cells);
  honest worlds `fg-honest-fp-minimal.txt` rc 0 (`1 control(s) held`), `fg-honest-r88fixed.txt` rc 0 (`4
  control(s) held`). The refusal fixture `fg-r88-refusal-fixture.txt` still refuses (rc 1, `w_added_red`).
  The `rp-*.sh` probes exit 1 on the fixed candidate by construction (their pass condition is the
  defect); the readings above are the gate's printed lines, not the probe exit codes.
  Carried: `F-4` (MutTesterBattery) — removing a whole `INSTRUMENT_PINS` key is silent in the tip
  battery; `R1` — the probe's BASE constant is `5031a782` (pre-freeze tip, checker bytes equal).

**No axis harmed.** Measured no-harm at landing: gate registry `74 of 74 … phantom 0` rc 0
(`gate-registry.txt`); tip battery `guards 5 of 5; tip battery exit 0: 3 of 6` rc 1, the same three
carried red corpus gates as base (`tip-battery.txt`, `base-tipbattery.txt`); corpus integrity at the
lane root `4/9 checks pass`, DRIFT set identical to base (`corpus-integrity-laneroot.txt`,
`base-corpus-integrity.txt`); census `grep -cE … corpus/SOURCES.md` 190 → 192, validate rc 0
(`census-validate-file.txt`); SKILL.md byte-identical (600 lines); no `/tmp` literal in added lines.
Carried red, unchanged: sibling census (`province rows 20 matched 4`, rc 1), province core (`0 of 2`,
rc 1), checklist `governance.citation_resolves` (rc 1).

**Frontier step (§ 2b).** Census 190 → 192 (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`,
base `census-before.txt`, landing `census-validate-file.txt`). Sourced claims: C2(b) cites S266;
C1's calibration conjunct cites S265 (the correction row, superseding S263). Mistake mined: the
`vacuous` row and the five L1 rows above (`landing`, `plan-text`, `receipt-pointer`, `late-write`,
`scope-drift`), each with its captured-by and fix. Assimilation: none — the shokuknow package stays
unadopted (L0 `kotoba | round-88` open). Considerthese: no proposal implemented; proposal 3 carried.

**Non-author spot-check:** pending — the closure samples one admit and one reject from the Gate above.
The gate has two admits (S265, S266) and no reject this round; the closure's reject sample is the
S264 reject from round 91 if it wants a cross-round pair.
