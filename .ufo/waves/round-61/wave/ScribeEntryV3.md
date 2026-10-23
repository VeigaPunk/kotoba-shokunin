# ScribeEntryV3 — round 61 findings

## Behavior and evidence scope

This seat produced the C1 knowledge-entry draft below and a read-only attack on the frozen C1 predicate, r60 ground, the C2 routed-repair checker, and the C3 bleed boundary. No lane counter or fixture was run or changed; no current C1 result is claimed.

Inputs read: `plans/round-61.md`; `verifiers/check_scoped_rules.py`; `verifiers/check_routed_repairs.py`; `.ufo/waves/round-61/controls/C2-base.txt`; `.ufo/waves/round-61/census-before.txt`; `corpus/SOURCES.md`; r60 `.ufo/waves/round-60/controls/`, `controls-v2/`, `build/ExecKeyForms.md`, `snapshots/S105.page`, and `corpus/lessons/round-60-verifier-spotcheck.md` §§7–8; and read-only sibling source `kama-shokunin/corpus/knowledge/self-assessment-at-writing.md`.

At inspection, `corpus/SOURCES.md` ended at S111; search found no S112–S115 rows. The round-61 wave directory contained only the dispatch payload/spec, census-before, C2 base receipt, and wave registry; no v3 counter, fixture, S112–S115 source row, or my report existed before this write. The source seats ScribeS112–ScribeS115 were still running when checked. The L1 status read described the freeze handoff, not a C1 integration or measurement. These are point-in-time observations, not a claim that later wave work did not land.

No shell commands, `date -u`, counter runs, self-tests, build, lint, formatter, or judge were run by this scribe. No packages/tools were installed. All reported historical results below are explicitly transcribed from committed r60 receipts; they are not this seat's execution evidence. No fleet, sibling, `.ufo/state`, or jj/git-index files were written.

## Draft for `corpus/knowledge/scoped-rules-counter-round61.md`

The following is a full draft for integration; all W3 v3 results are expected behavior, not observed output. S112–S115 citations are provisional until the running source seats' committed rows and snapshots are available to confirm them.

```markdown
source: S112–S115 (opened this round; canonical per-client scope-key evidence, row/snapshot citations pending integration check) + frozen plan `/home/vgpnk/Projects/shokunin/kotoba-shokunin/plans/round-61.md` § C1
verified-at: 2026-10-23 — draft review of the frozen plan and r60 receipts only; v3 not run
recheck: `python3 -B verifiers/check_scoped_rules.py --self-test`; then `python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` and the same command at base `f3246d14`. Record each command's full stdout, `date -u`, and exit code.

# Scoped-rules counter v3: semantic key, action, URL, and snapshot checks

The round-60 v2 counter could credit real-looking rows with a wrong key, an invented Action, a locale/enterprise URL alias, or reused historical snapshot bytes. This v3 draft records the frozen defenses and the round-60 attack worlds; it does not assert that v3 has passed them.

## What changed from v2 to v3

- **A1 semantic scope-key** — a row's Scope key must be in the canonical per-client key set grounded in S112–S115 (opened this round), and must bind a path-like value on the cited line.
- **A2 semantic action** — every load/event claim in the Action cell must be supported by text on the committed snapshot page (not vocabulary matching alone).
- **A3 URL canonical** — a re-open row's URL must be byte-identical to its base row's URL.
- **A4 snapshot provenance** — the row's recorded sha256 must equal the committed snapshot bytes, the located quote must occur verbatim in them, and the earliest commit introducing those bytes must be no older than the row's recorded open date.

## Seven r60 worlds

The v2 column is transcribed from the named r60 receipt; it is not a v3 run. `Expected reject` describes the intended v3 discriminator, not actual counter stdout.

| World | r60 ground path | Recorded v2 result | Expected v3 reject line (not run) |
|---|---|---|---|
| W1 `CtlReopenForged d` | `.ufo/waves/round-60/controls-v2/CtlReopenForged.md` | S=3/3, F=3/3, `--fetch` exit 0 | `reject <re-open rows>: A4 snapshot bytes were first introduced before the row's opened date` |
| W2 `CtlReopenHeldKey b` | `.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md` | S=3/3, F=3/3, `--fetch` exit 0 | `reject <alias rows>: A3 re-open URL is not byte-identical to the referenced base-row URL` |
| W3 `CtlReopenHeldKey a` | `.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md` | S=2/3, F=2/3, `--fetch` exit 1 | `reject Cursor: A1 scope key 'rules' is not canonical and line 146 does not bind a path-like scope value` |
| W4 `CtlReopenHeldKey c` | `.ufo/waves/round-60/controls-v2/CtlReopenHeldKey.md` | S=3/3, F=2/3, `--fetch` exit 1 | `reject Cursor: A3 requested re-open URL differs from its base row URL` |
| W5 wrong key `sessions` | `.ufo/waves/round-60/build/ExecKeyForms.md` | W-wrong: S=4/4, F=4/4, `--fetch` exit 0 | `reject VS Code: A1 scope key 'sessions' is outside the canonical per-client key set` |
| W6 invented Action | `.ufo/waves/round-60/build/ExecKeyForms.md` | W-invented-best-line: snapshots backed 4/4, no-fetch exit 1; no `--fetch` result is recorded for this row | `reject VS Code: A2 invented load/action claim is unsupported by the cited committed line` |
| W7 v1-hollow `CtlAllFalse` | `.ufo/waves/round-60/controls/CtlAllFalse.md`; rescore `.ufo/waves/round-60/controls-v2/CtlRescoreV2.md` | S=7/7, F=0/7, `--fetch` exit 1 | `reject <fabricated rows>: A1 key 'matchFiles' is outside each client's canonical key set` |

W0 do-nothing is the separate control; the seven rows above are W1–W7 from the frozen plan.

## A4 limit

The check authenticates internal provenance consistency of committed snapshot bytes: the recorded SHA-256 and quote must match the committed bytes, and the earliest commit introducing those bytes must not predate the row's recorded open date. It does not authenticate wall-clock fetch time and cannot defeat author-forged commit dates.

## Frozen predicate

`python3 -B verifiers/check_scoped_rules.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
`python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0 while the same
command at base `f3246d14` exits 1.

## Not held

- The counter does not prove the semantic truth of rows or that the cited page entails every Action-cell statement; reviewers re-read the cells.
- A passing snapshot check is not wall-clock authentication of when a fetch happened.
- The r60 world scores are historical v2 evidence, not a current v3 measurement.
```

## Attacks and findings

### C1 — depth / v3 gate

- The frozen predicate is clear about separate self-test, tip `--fetch`, and base `--fetch` gates. None was run here; there is no result to promote to a pass.
- **A1 discriminator is well-motivated:** r60's `ExecKeyForms.md` reports a live-pass wrong `sessions` key, and `CtlReopenHeldKey.md` reports a held `rules` key that is a prose colon/bold construct rather than Cursor's cited `globs` key. A1 must check both canonical membership and a path-like value on the cited line; syntax-only key-form tests were already defeated.
- **A2 remains a semantic boundary:** the r60 invented action “Put the guidance in an instructions file and add frontmatter so it attaches only to the files you name.” is associated with VS Code snapshot line 105, whose text says file-based instructions can attach by matching `applyTo` and also load on demand. Token overlap does not prove the whole Action-cell claim, and the counter must not be reported as semantic proof. `ExecKeyForms.md` only records W-invented-best-line's offline `4 of 4`; it does not record a `--fetch` result for that world.
- **A3 needs row identity as well as equality:** compare the raw URL on the re-open row with the raw URL in the particular base row named by its `re-opens` cell. The r60 alias world reached 3/3 live with locale/enterprise URLs; the redirect world separately demonstrates that a requested URL can redirect to a different held base key.
- **A4 is bounded by the frozen plan's explicit limit.** Implementation evidence must identify the exact commit-time field and search domain used to find the earliest introducing bytes; a consistency check over Git metadata is not proof that the fetch happened then. The r60 W1 receipt proves v2's gap (old S043/S048/S049 bytes copied under fresh rows scored 3/3 and exit 0), not that v3 closes it.
- **A4 attack on W1 fixture provenance [INFERENCE]:** `CtlReopenForged.md` says the d-world bytes came from `/fast/scratch/hyaku/kotoba-r53/...`; the receipt does not establish that those exact bytes had a pre-open *committed* occurrence. If their first lane commit is the new snapshot commit after the row's open date, the earliest-commit check can accept recycled scratch bytes. The W1 fixture must demonstrate an actual pre-open committed occurrence (not merely old scratch provenance or fabricated commit dates), or it does not test the promised reject.
- The v2 historical command/output/date detail exists for W1–W4 in `controls-v2/CtlReopenForged.md:305-339` and `controls-v2/CtlReopenHeldKey.md:268-328,394-452,456-515`. Example W1: recorded `date -u` `Fri Oct 23 12:08:42 PM UTC 2026`; `timeout 900 python3 -B verifiers/check_scoped_rules.py --rev 7f05968a085ddf9fb9155b0a1047808d616b7b1b --fetch` printed `scoped rule files backed on committed snapshots 3 of 3; found on the live page 3 of 3` (plus the counter/reject lines in that receipt); exit 0. These are receipt transcriptions, not reruns.
- The r60 `ExecKeyForms.md` has sandbox commit ids and table outputs for W5/W6, but the inspected table does not print per-run `date -u` or the exact scoring command. Do not dress those historical rows up as complete timestamped measurement receipts. The W7 v2 score is recorded in `controls-v2/CtlRescoreV2.md:174-189` as `S 7 of 7; F 0 of 7`, seven HTTP 404 reject lines and exit 1; the inspected section does not show a per-run `date -u` or exact command. W7's primary v1 receipt `controls/CtlAllFalse.md:13-19` explicitly says the v2-style offline success is not an authentic source and calls the mutation inconclusive against a pristine v1 world.

### C2 — routed-repair gate attack

The committed base receipt `.ufo/waves/round-61/controls/C2-base.txt` literally records six `missing` lines, `routed repairs verified 0 of 6`, and `base-exit=1`. It contains no command or `date -u` transcript, so I did not claim an independently reproduced measurement. The plan's checker command is `python3 -B verifiers/check_routed_repairs.py --rev <rev>`.

Static attack on `verifiers/check_routed_repairs.py` (no execution):

- R-a's frozen plan requires a corrected count on one line with its counting command. The implementation at lines 69–75 only checks four substrings anywhere in `LOG.md`; it does not require one line or a command, so a fabricated count can score.
- R-b checks both path substrings anywhere in `LOG.md`, not that the report accurately names landed scope.
- R-c does require both pointer strings on one line, but not that the line correctly characterizes which file contains the base measurement.
- R-d checks only that the final non-empty census-after line is literal `exit=0`; it does not bind it to a census command/output/date.
- R-e checks `Q56` and `byte-exact` substrings in QUALITY plus `M91` in the lesson; it does not validate the substantive correction.
- R-f checks for the literal `merge-base --is-ancestor` and `exit 0` strings; it does not execute or bind them to commit ids.

The checker docstring itself says it does not judge whether repair text is substantively honest. Thus `0 of 6` at base is a useful negative control, not a proof that `6 of 6` means the report is honest. This does not alter the frozen C2 contract; it is an attack finding for the L1's interpretation.

### C3 — adjacency / bleed boundary

The sibling entry `kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` identifies its source as the round-29 counter, preregistration, baseline receipt, and Git manual rows S174–S177. It states that the check covers six recognized patterns in SCORECARD.md and SHONEN.md at a frozen writing revision, and explicitly says it is a bounded extractor, not a semantic proofreader; its own `verified-at` says no fresh counter run was performed. This is relevant as a tier-B own-work example of writing-revision calibration for prompt-craft self-assessment only. It does not support scoped-rule vendor claims, prove round-61 A1–A4, or establish a fresh execution result; importing it for those would cross the planned C3 boundary.

## Gates, touched surfaces, limits

- **Gates:** no C1 self-test, no C1 tip/base measurement, no C2 checker rerun, and no C3 integration count were performed by this seat. The only observed C2 base status is the committed output-only receipt above. No v3 pass is asserted.
- **Touched surface:** only this report file is written. Read-only surfaces are enumerated above. No product source, fixtures, SOURCES rows, knowledge files, sibling files, fleet files, `.ufo/state`, or jj/git-index files were changed.
- **Out of scope:** integrating peer source rows or v3 code, fetching source pages, creating fixtures, running gates, assigning C1 verdict, and writing the C3 entry/README/S117 row. Those remain with their assigned seats and L1.
- **Known limits:** S112–S115 source evidence and v3 artifacts were not visible at this inspection; the exact expected reject strings are suggested labels, not observed output. W5/W6/W7 r60 measurement receipts lack some per-run timestamp/command detail as noted above. No installs.

Installs: no installs.
Blockers: none to this report; current C1 artifacts were not available to measure and are explicitly left unclaimed.
Produced: C1 v3 knowledge-entry draft, plus static attacks on C1/C2 and a C3 scope-boundary finding.
Report: .ufo/waves/round-61/wave/ScribeEntryV3.md
