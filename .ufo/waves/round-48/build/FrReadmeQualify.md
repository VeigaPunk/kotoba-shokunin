# FrReadmeQualify — routed defect 2: README live 24/24 recipe + erratum horizon

Seat: KotobaR48.FrReadmeQualify (leaf, read-only on the lane except this file). Date: 2026-10-22.
Tree measured: lane master `75f671b109d8eddd0d64c1429bd6379fe577175a`, working tree carrying the
in-flight C1 candidate (`M verifiers/verify_harness_independent.py`, sha256 `2d824c0b…` — see F3).
No tools installed this session; pacman untouched.

## Findings

**F1 (HIGH — the routed defect, confirmed). The "live 24/24" promise is stale on two of three
recipe legs at today's substrate.**
- Promise sites: `corpus/README.md:38` — "**live 24/24 over the landed scope, exit 0**" (present
  tense, round-37 row); `corpus/README.md:59` — "a fresh live producer/join **remains** protocol
  24/24 (strict 20/24, 4 adjudicated, 4 scoped out), with zero disagreements" (present tense,
  round-41 row). The top-level `README.md` (16 lines) makes no 24/24 or horizon claim
  (`grep -c 24/24 README.md` → 0; corroborated by FrRoutedDefectPattern).
- Recipe as written: `corpus/knowledge/harness-independent-round37.md` §6 `:492-497` (HAR, IND)
  and `:508-509`/`:512-516` (the join).
- Actual output 2026-10-22 (verbatim heads; full lines in Evidence):
  - HAR `python3 verifiers/verify_harness_claims.py` → `21/28 checks pass; DRIFT: omp.db.rows,
    omp.offered.skills, omp.cache.misses, omp.catalogue.total, omp.catalogue.missing_names,
    omp.cache.verified_skills, oc.roots.names_plus_builtin`, **exit 1** (recipe comment promises
    "28/28, exit 0"). The omp substrate moved again: `omp.db.rows` 17≠14, `omp.offered.skills`
    11≠7, `omp.catalogue.missing_names` observed `['create-toolset','unreal-mcp','unreal-skill']`
    ≠ `[]`; `oc.roots.names_plus_builtin` observed 12 ≠ 7 (log now names 12 roots — the C1 row).
  - CMP `python3 verifiers/compare_harness_independent.py` (live join) →
    `ERROR: false blocker: scoped row omp.catalogue.found declares observable {…5578…} but
    recomputation gives {…5581…}` (same for `omp.catalogue.matched` and `omp.catalogue.missing_names`),
    **exit 2** — not "agreement 24/24 … exit 0". This is exactly the live-carrier race registered
    as HIGH-3 in `SCORECARD.md:33`; `candidate_blocks` moved 5578→5581 between IND's capture and
    CMP's recomputation (new skill files landed in the omp catalogue mid-join).
  - IND `python3 verifiers/verify_harness_independent.py` → `24 derived, 4 scoped out, 0 unlanded
    (of 28 named checks)`, exit 0 — but see F3: these are the C1-candidate bytes, not HEAD's.

**F2 (HIGH — erratum horizon is a debt meter, absent from every README).**
`verifiers/verify_skill_checklist.py:377` pins `GOVERNANCE_ERRATA_HORIZON = 2315`; `:378-384` is
the single row excusing `LOG.md:2111` (line sha256 `7dcbf123…`, token
`.ufo/round-45/drafts/v10/post-r44-hunt.py`, wording "each exited 2 because the referenced runners
are absent"). Per the in-source docstring (`:190-197`) a row applies only to lines **at or below
the horizon**. `LOG.md` is 2343 lines today — 28 lines (2316-2343, the round-47 appends) sit past
the horizon, so any future dead citation there FAILs `governance.citation_resolves` until a
reviewed verifier diff moves the horizon and adds a row (round-47 falsify W2ErrataAppend proved
horizon-only and row-only edits each still FAIL). No README carries this: `corpus/README.md` has
no round-47 checklist row and no horizon mention (grep `horizon` → verifier + `SCORECARD.md:33`
only). The pinned row itself still holds: `sha256(sed -n '2111p' LOG.md, no newline)` =
`7dcbf123…0135` = the row's digest (the with-newline form `d7b4c628…` is the documented
non-matching convention).

**F3 (MEDIUM — custody: my IND leg measured the C1 candidate, not HEAD).**
The lane working tree's `verifiers/verify_harness_independent.py` differs from HEAD by the C1
patch (13 insertions / 8 deletions; working sha256 `2d824c0b…` = the plan's declared C1 consumer
sha; HEAD bytes `872993f8…`). So F1's IND line is "exit 0, 24 derived **on the C1 candidate**";
the committed `872993f8…` bytes were not run this session (HAR + CMP alone already void the clean
recipe, and the round-47 spot-check records the join exiting 2 on committed bytes 2026-10-21).
Any fresh count must be re-run on the landed C1 commit — the C1 union changes
`oc.roots.names_plus_builtin`, one of the compared rows (join compares it `equal`,
`verify_harness_claims.py:544`).

**F4 (LOW — adjacent, out of my routed scope).** `corpus/README.md:37` carries a third "24/24"
(hidden-host hermeticity caveat, round-12 row) already filed stale by round-32 scout M3 (live
32/36); listed so defect 2's repair does not read as covering it.

## Draft qualifying sentences (append-only; dated notes, history untouched)

D1 — append to the `corpus/README.md:38` cell (row convention: bold dated note):
"**2026-10-22 note (append-only):** that headline is the round-37/41 measurement at its pinned
shas, not a standing promise — re-running §6 at master `75f671b` gives HAR `21/28 checks pass`,
exit 1 (`omp.catalogue.missing_names` now create-toolset/unreal-mcp/unreal-skill; substrate
drifted again) and a live join that exits 2 `false blocker` (the scoped `omp.catalogue.*` rows
recompute against a moving carrier — SCORECARD HIGH-3); quote 24/24 only against the measured
tree, and re-measure on the landed C1 commit before quoting any new count."

D2 — append to the `corpus/README.md:59` cell:
"**2026-10-22 note (append-only):** `remains` reads as of `b1be35f`/`1742dccc` (2026-10-19); a
2026-10-22 re-run at `75f671b` exits 2 `false blocker` on the same catalogue race, so the
protocol headline and its strict/adjudicated columns are dated records, not live status."

D3 — new coverage-map row (append-only; index-affecting, so integrator's call):
"| Governance erratum horizon (round 47) | `../verifiers/verify_skill_checklist.py`
(`GOVERNANCE_ERRATA`, `:375-384`) + `SCORECARD.md:33` | the governance gate excuses a dead
`LOG.md` citation only via an in-source row pinning the line's sha256, absence wording and a
still-dead path, and only for lines ≤ `GOVERNANCE_ERRATA_HORIZON = 2315`; LOG.md passed 2343
lines on 2026-10-22, so lines 2316+ are un-excusable — each future dead citation needs a reviewed
verifier diff (horizon move + row), which also moves the checklist self-test floor. |"

Minimal alternative if a new row is unwanted: append D3's second half as a dated note to the
round-17 checklist row (`corpus/README.md:45`).

## Evidence (commands with exit codes, verbatim)

```
$ wc -l LOG.md                       → 2343 /home/vgpnk/Projects/shokunin/kotoba-shokunin/LOG.md
$ git rev-parse HEAD                 → 75f671b109d8eddd0d64c1429bd6379fe577175a
$ git status --porcelain (pre and post, identical)
  M verifiers/verify_harness_independent.py
  ?? .ufo/waves/round-48/
  ?? plans/round-48.md
$ sha256sum verifiers/verify_harness_independent.py
  → 2d824c0b3d4954c9a01868ee7c9b44c72b77bb5054419cf0539f6e4082f1b88a
$ git show HEAD:verifiers/verify_harness_independent.py | sha256sum
  → 872993f875338f4f89d5b76178c124313e9fc3368966f8a32583acd0430bdbd1
$ git diff --stat -- verifiers/verify_harness_independent.py
  → 21 lines changed: 13 insertions(+), 8 deletions(-)

$ python3 -B verifiers/verify_harness_claims.py ; echo "HAR exit=$?"      [exit 1, 3.24 s]
  omp      template=c1f03c8e248eb40e… (273 B)  db_rows=17  offered=11  keys_reproduced=7  misses=4
           newest catalogue 2026-10-22T08:14:35.305Z (7/10 lines from cache, 2964 session files scanned)
  opencode init_count_max=0  rescan_skills_max=3  names+builtin=12  <available_skills>=0  skill_perm=0/0
  DRIFT   omp.db.rows: observed=17 expected=14
  DRIFT   omp.offered.skills: observed=11 expected=7
  DRIFT   omp.cache.misses: observed=4 expected=0
  DRIFT   omp.catalogue.total: observed=10 expected=7
  DRIFT   omp.catalogue.missing_names: observed=['create-toolset', 'unreal-mcp', 'unreal-skill'] expected=[]
  DRIFT   omp.cache.verified_skills: observed=11 expected=7
  DRIFT   oc.roots.names_plus_builtin: observed=12 expected=7
  21/28 checks pass; DRIFT: omp.db.rows, omp.offered.skills, omp.cache.misses, omp.catalogue.total,
  omp.catalogue.missing_names, omp.cache.verified_skills, oc.roots.names_plus_builtin
  HAR exit=1

$ python3 -B verifiers/verify_harness_independent.py ; echo "IND exit=$?" [exit 0, 21.47 s]
  DERIVED oc.roots.names_plus_builtin    10        (4 omp.catalogue.* rows SCOPED_OUT)
  24 derived, 4 scoped out, 0 unlanded (of 28 named checks)
  IND exit=0        [on the C1-candidate bytes 2d824c0b…, see F3]

$ python3 -B verifiers/compare_harness_independent.py ; echo "CMP exit=$?" [exit 2, 46.40 s]
  compare_harness_independent: ERROR: false blocker: scoped row omp.catalogue.found declares
  observable {"candidate_blocks": 5578, "distinct_totals": [7, 10], …} but recomputation gives
  {"candidate_blocks": 5581, "distinct_totals": [7, 10], …}; false blocker: … omp.catalogue.matched …;
  false blocker: … omp.catalogue.missing_names …
  CMP exit=2

$ sed -n '2111p' LOG.md | tr -d '\n' | sha256sum
  → 7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135  (matches the GOVERNANCE_ERRATA row)
$ sed -n '2111p' LOG.md | sha256sum
  → d7b4c6289e30ad0d9c23554c066742802d5c325f9bea9929dce5fa717d981c7a  (with-newline; the documented non-matching form)
```

`-B` deviation note: the recipe writes plain `python3`; `-B` (no bytecode writes) was used so the
read-only lane stayed byte-clean — output text is unaffected. `verifiers/__pycache__` holds 3
`.pyc` files all mtime-dated 2026-10-21 (pre-existing, not mine). Recipe arms not run this
session: both `--self-test` legs (~300 s each; not part of the live 24/24 headline), the
`--write-freeze`/receipt legs (their live-mode numbers are contained in the CMP run), and the
mutant/vacuity arms.

## Residual risk and verification gaps

- The committed-bytes (`872993f8…`) IND run is unmeasured this session; the pre-C1 join state
  rests on the round-47 spot-check's 2026-10-21 record (exits 2 at base and landing) plus my
  HAR/CMP runs. No fresh N/24 should be quoted until the join is re-run on the landed C1 commit.
- The join race (HIGH-3) means any single-shot CMP output is a sample of a moving carrier; my
  exit-2 `false blocker` is today's draw, not a stable verdict on the join logic.
- Harness-volatile numbers (omp db_rows/offered/catalogue) will keep moving; D1/D2/D3 are worded
  to name tree + date so they degrade into dated records, not new stale promises.
