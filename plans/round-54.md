# Plan — round 54 (hyaku campaign, attempt 1)

Base: branch `master` at `422ffd1082b3f4ae3ebda6060eb1a8d779f6dfd4` (round 53 admitted; spot-check
`corpus/lessons/round-53-verifier-spotcheck.md`). Shape: default, two v1 waves (build, then falsify). The L1
holds the planner seat; a bounded planning data-walk rides one scout item. Every before-value below was
measured by the L1 at round start, 2026-10-22T21:30Z, on the lane checkout at `422ffd10` (Q19). Both counters
are committed in this plan commit, before any content they score (Q28); their clients, tables, rules and
targets are frozen here and never widened this round.

Axis scores at base (`SCORECARD.md` § axes @ `422ffd10`): depth 9, consistency 10, coverage 8.5,
operability 8.5, freshness 8, calibration 8.5, adjacency 8.0. Owned axes: depth + consistency; the lowest
owned axis is depth (9). C1 works depth, so both readings of the lowest-axis duty are not needed: the
owned-only reading is met by C1. (The all-axes reading would point at freshness/adjacency; see below.)

Drift sentinel (closure routed defect 1; orchestrator session note): no freshness claim, nothing on
`verifiers/verify_surfaces.py`, nothing on the executed-checklist/always-on-box Frontier row. C1 works the
Frontier row **Per-render consumption** (`corpus/README.md` § Frontier), untouched since round 46, on its
offer-render half: what each client documents about how much of a skill's `description` reaches the model.
It does not claim the per-session offer→activation join, which stays unheld. Each statement below is the
counter's printed line and nothing more (Q26, Q31).

## Claims (each statement is exactly what its counter prints)

**C1 — depth (lowest owned axis, 9; the learning claim; the sourced claim).**
Statement: `python3 -B verifiers/check_description_thresholds.py --rev <rev>` prints
`description thresholds backed 4 of 7 clients` or more and exits 0.
Before at `422ffd10` (2026-10-22T21:31Z): `description thresholds backed 0 of 7 clients`, exit 1 (no
`### Description thresholds by client` table, no entry `corpus/knowledge/skill-listing-thresholds-round54.md`).
Counter: frozen here; rules in its docstring. A client (Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI,
Cursor, opencode) counts only when the SKILL.md decision table row has a number in its threshold cell and a
non-empty action cell, and the entry's per-client row quotes, in 3–25 words and verbatim as recorded in
`corpus/lessons/round-54.md` § Gate, that same number from a tier-A `mined` `corpus/SOURCES.md` row opened
2026-10-22 on one of the client's pinned hosts. A table with numbers and no sourced quote counts 0.
What the counter does not measure: whether a number is a render cut, a listing budget or an authoring
maximum (entry and reviewer reading, Q31); whether the clients behave as documented; any client outside the
seven. `--fetch` (live-page presence) is a second measurement, reported beside the declared one.

**C2 — consistency (owned; the calibration sub-axis; score 10 held).**
Statement: `python3 -B verifiers/check_gate_registry.py --rev <rev>` prints
`gate registry rows conformant <M> of <M> lane verifiers; phantom 0` and exits 0, where M is the number of
`.py`/`.sh` blobs directly under `verifiers/` at that revision.
Before at `422ffd10` (2026-10-22T21:32Z): `gate registry rows conformant 0 of 21 lane verifiers; phantom 0`,
exit 1 (SKILL.md, the registry home under PROTOCOL.md § Gate standard, has no `## Gate registry`; closure
routed defect 4 names `verify_alwayson.py` and `check_gate_finding_delta.py`).
Counter: frozen here; rules in its docstring. Each mismatch it counts is a disagreement between the lane's
registry (its self-description) and the repository: a verifier with no row, a row naming a file that is not
there, a self-test flag that is not in the file, a pinned path that does not exist, a gate without `0=clean`
and `1=failed`.
What the counter does not measure: whether each declared exit code is really produced, and whether
gate-vs-probe is the right kind. Wave 2 attacks those by running each script; findings are reported, not
counted.

Causal separability: C1 adds the entry, SOURCES rows, the Gate quotes and the SKILL.md
`### Description thresholds by client` table; its counter reads only those four files. C2 adds the SKILL.md
`## Gate registry` table; its counter reads only SKILL.md and `verifiers/`. An enabling, non-claim commit
first moves the verifier-description bullets of SKILL.md § Sources (42 lines, verbatim) to
`verifiers/README.md`, so that either claim lands under the 600-line budget alone (`trigger.line_budget`,
593 of 600 at base).

## Frontier step and routed defects (not claims)

- Sources: rows opened this round for the C1 clients; census before/after.
- Mistake: mined into `corpus/lessons/round-54.md` § Mistakes (candidate: the S050 in-place `anchor` edit,
  an append-only breach not caught by any gate).
- Round-53 spot-check routed defects: (2) S046 "replaces" correction row; (3) S050 in-place edit recorded as a
  correction row; (4) is C2; (5) tip runs committed with revisions (corpus integrity, independent, finding
  delta against a pinned revision, floors guard), `LOG.md` gains `e5355a62`; (6) `baseline.json`
  `opencode_round53_note` cites the regeneration command, not the deleted scratch path — a pointer fix with
  no change to any pin value; (1) carried into lesson text; (7) carried.

## Erratum (append-only; landed before any C1 or C2 content)

- The before-value times above (`21:30Z`, `21:31Z`, `21:32Z`) are wrong: the L1 wrote them ahead of the clock.
  The plan commit `e33715486a45a4a857b64c30e6b695f7995858b8` has committer time 2026-10-22T21:12:08Z, and both
  base runs (`check_description_thresholds.py --rev 422ffd10` → `backed 0 of 7`; `check_gate_registry.py
  --rev 422ffd10` → `conformant 0 of 21 … phantom 0`, exit 1) ran between 21:08Z and 21:11Z. The values are
  unchanged; only the times were misstated (lesson round 54, mistake candidate).
- The enabling move is 43 lines (`SKILL.md` 532–574 at `422ffd10`), not 42; it landed as
  `7ad05d342d7505ab674a5ebcf5ac1106b2f45c39` (593 → 552 lines; `diff` of the two ranges is empty).

## Erratum 2 (append-only; on wave-1 critic `CriticC2Sizing`, before any C2 content)

- The C2 sentence "Each mismatch it counts is a disagreement between the lane's registry … and the repository"
  is wider than the counter (Q31). Four of its checks read the repository — a row exists for each verifier blob,
  phantom rows, the self-test flag text occurs in the file, a pinned path exists. The other four (kind, verdict
  pairs, write scope, owner) read only the row's own cells. The flag check is a substring test, so a flag in a
  comment, a borrowed flag or a fragment passes it (`.ufo/waves/round-54/build/CriticC2Sizing.md`).
- Guard outside the counter, declared now and judged with the claim: four verifiers are gates without a
  self-test at `7ad05d34` (`box_proof_case_deletion.py`, `check_alwayson_boxes.py`, `check_callee_rename.py`,
  `check_opencode_repin.py`; each exits 2 on `--self-test`). C2 is not claimed unless each of their rows says
  `gate` and its declared flag, run in a sandbox clone at the measured revision, exits 0. A `probe` label or a
  borrowed flag on any of the four fails the claim even if the counter prints `M of M`. The honest registry
  at `7ad05d34` would print 19 of 23.
- The counter is not changed (Q28). Exact flag matching is a later-round item.

## Erratum 3 (append-only; on wave-1 critic `CriticC1Sizing`, before any C1 content)

- What the C1 counter does not check, named here (Q31): that a row was opened in round 54 — it checks only the
  date `2026-10-22`, which rows S016–S052 from rounds 48–53 also carry; that the number is about the
  `description` (Claude Code's 64-character name cap or a "500 lines" rule would count); that the page is
  vendor documentation (any subdomain of a pinned host passes, e.g. a forum; any `docs.github.com` page counts
  for Copilot CLI); that the quote is on the live page (only `--fetch` checks, and it follows redirects without
  re-checking the host). Its `--json` output is followed by the summary line, so it is not one JSON document.
- Prior holds, measured at the plan commit: Claude Code's 1,536-character listing cut and 1% listing budget are
  already in `corpus/knowledge/sibling-overlap-census-round49.md:155,221` and
  `corpus/knowledge/skill-selection-rules-round50.md:48`; the 1,024 maximum (VS Code, opencode) is already in
  `SKILL.md` (portability floor). Codex's 2% / 8,000 numbers are only in SOURCES rows S013/S021, not in an entry.
  So C1's learning form is the third one the round allows: a `SKILL.md` decision table grounded in admitted
  entries, plus the Codex and any Copilot CLI, Gemini CLI or Cursor numbers as new entry content.
- Guards outside the counter, declared now and judged with the claim: (a) each backed client's `S###` is absent
  from `corpus/SOURCES.md` at `e33715486a45a4a857b64c30e6b695f7995858b8` (opened this round, not only dated
  today); (b) new ground in `SKILL.md`: at least 2 backed clients carry a threshold number that
  `git show e33715486a45a4a857b64c30e6b695f7995858b8:SKILL.md | grep -c -F -- '<number>'` counts 0 times
  (at the plan commit `1,536`, `2%`, `8,000` and `1%` count 0; `1024`/`1,024` count 1); (c) each backed quote is
  found by `--fetch`. C1 is not claimed if any guard fails, whatever the counter prints.
