# ExecAnchorR100 — C2 build (round 100, w1)

Seat: `ExecAnchorR100`. Claim: C2 — `verifiers/verify_skill_checklist.py` reads
comma-list line anchors (`file.md:30,37`) as line anchors on both public
citation checks. Scratch clone at `03a98eb78b63bf9895cbe00ba0f3c8b0e53aa687`,
commit `6a59d80755d8f50c3d2cf67cbafdac60dc5e9e0c`.

## Changes (owned files only)

- `verifiers/verify_skill_checklist.py`
  - `strip_token_dressing`: the frozen fix line, byte for byte
    (`re.match(r"^(.+\.\w+):\d+(-\d+)?(,\d+(-\d+)?)*$", tok)`).
  - `self_test()`: 22 new `r100-comma-anchor` arms. Each arm calls
    `strip_token_dressing` via `check_citation_resolves(["- \`TOKEN\`"], world)`
    and `check_governance_citations(world, errata=(), corrections=())` on a
    fixture governance world under `TMPDIR` (`corpus/lessons/x.md`, 40 lines).
    Positives: `:30,37`, `:3,7-9`, `:30,37,` (trailing comma stripped as
    `TRAILING_PUNCT`), `:10,18,34,40-42`, `:42`, `:1-2`, bare. Negatives
    (must stay red on both paths): missing file `:30,37`, `:30,abc`,
    `:30,,37`, `:,30`. All arms are exception-caught `rec(...)` tallies —
    behaviour observers, never source readers.
  - `GOVERNANCE_CORRECTIONS`: removed exactly the one row whose stale token
    is `corpus/lessons/round-80-verifier-spotcheck.md:30,37` (LOG.md:3598 /
    SCORECARD.md:529). Horizon line unchanged; no other row changed.
- `verifiers/check_tip_battery.py`
  - `INSTRUMENT_PINS`: admitted the new checklist blob
    `94d11c7a103590bfeea93910da6710bd8a64f0c6` with a round-100 comment;
    every earlier pin kept. Nothing outside the `INSTRUMENT_PINS` block
    changed.

## Evidence

- Self-test (in scratch clone): `0 failure(s) over 1886 assertions`, exit 0
  (floor 1864). Receipt: `ExecAnchorR100/self-test.txt`.
- Revert-mutant kill is covered by the counter below (old regex restored on
  disk): `8 failure(s) over 1886 assertions`, exit 1.
- C2 counter
  (`anchor-lists.py 6a59d80755d8f50c3d2cf67cbafdac60dc5e9e0c "$D"`):
  see `ExecAnchorR100/anchor-lists.txt` — all 28 truth-table rows OK,
  gate GREEN (11 PASS lines), self-test HELD, revert mutant KILLED,
  frozen 3 of 3, tip battery guards 5 of 5 with checklist gate exit 0.

## Patch

`ExecAnchorR100/ExecAnchorR100.patch` (sha256
`f2d1efee8815ef635859fdb2b805e09973ceb6c70a34b447d0005b92c87d9c92`),
`git apply --check` clean on a fresh clone at the freeze commit.

## Findings / risks

- The counter discloses that its kill conjunct runs the mutant on disk only,
  so a source-sniffing arm would also read KILLED; these arms observe
  behaviour (function calls on fixture inputs), not source.
- Battery corpus gates remain red at this candidate (unindexed round-99
  spot-check lesson) — landing no-harm work for the L1, not a C2 failure;
  the C2 counter does not read the corpus gates.
- No tools installed; no kernel/host settings needed; no counter defects found.
