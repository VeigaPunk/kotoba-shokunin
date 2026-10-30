# Kb82E04Governance — round-82 routed live-citation repair (governance corrections)

Seat: Kb82E04Governance (leaf, no dispatch). Base: `47dbe8781657de563ff867caca6244d28e3db504`.
Scope: the four dead SCORECARD tokens named by the base live gate
(`.ufo/waves/round-82/receipts/before-checklist.txt`, `governance.citation_resolves`
FAIL, exit 1). C2 self-test fixture work belongs to Kb82E03Checklist; this seat
touches live governance only and no self-test arm.

## The four tokens and their repairs

| subject | stale token (live, red at base) | corrected token (resolves) |
|---|---|---|
| SCORECARD.md:480 | `.ufo/wapes` | `.ufo/waves/round-81/dispositions/wapes.txt` |
| SCORECARD.md:482 | `corpus/lessons/round-80-verifier-spotcheck.md:30,37` | `corpus/lessons/round-80-verifier-spotcheck.md` |
| SCORECARD.md:484 (×2, one row) | `.ufo/reports/round-81/kotoba.md` | `../.ufo/reports/round-81/kotoba.md` |

- **Displaced wapes artifact:** the round-81 G1 landing ledger (SCORECARD.md:478)
  names `dispositions/wapes.txt`, and the routed-repairs sentence on :480 itself
  states R3's replacement `.ufo/waves/round-81/dispositions/wapes.txt`; the bare
  `.ufo/wapes` was never a repo path. Corrected token verified tracked at base
  (`git ls-tree -r HEAD`); stale token verified absent (count 0).
- **Comma line selector:** the `:30,37` suffix is a line selector, not path
  bytes; the bare lesson path is tracked at base (round-81 R4 landed the index
  row). The stale form stays red because no file carries the suffix.
- **Fleet report path:** the round-81 fleet report lives in the fleet repo
  (`/home/vgpnk/Projects/shokunin/.ufo/reports/round-81/kotoba.md`, 26036 bytes,
  present); the `../`-hop form is the round-60/round-65 precedent. One row
  excuses both :484 occurrences (subjects are keyed by (file, line, token)).

No old SCORECARD/LOG line is modified; the repair is three appended LOG.md
notice lines (LOG.md:2867-2869 at base) plus three
`GOVERNANCE_CORRECTIONS` rows and the horizon bump 2723→2869 in
`verifiers/verify_skill_checklist.py`. Genuine absent pointers are not
suppressed (M5 below); old SCORECARD lines are untouched.

## Deliverable patch

`build/Kb82E04Governance.corrections.patch` — sha256
`b7d08b94cea1c4ceffd78e8b6a90b4e9f3dda7ad3b486647bd90689173e63277`.
Two files: `LOG.md` (+3 appended notice lines) and
`verifiers/verify_skill_checklist.py` (horizon + 3 rows + comment).
`git apply --check` verified against a pristine base clone. Byte-frozen
notice texts + digests: `build/Kb82E04Governance.notices.txt`. If other LOG
appends land first, `build/Kb82E04Governance.rebase.py <lane-repo>` regenerates
line numbers/digests (wording must not change — E03's fixture replays it).

## Evidence (all commands' own exit status; no pipes on the measured command)

World: scratch clones under `/fast/scratch/hyaku/kotoba-r82/Kb82E04Governance/`
(deleted on exit), in a synthetic fleet layout — symlinks to the real fleet
root make the lane's `..`-hop citations resolve exactly as they do at the
production lane root; nothing was written outside the seat's scratch and the
named build/report paths. Fixture-only commit `9047d2b` (scratch identity)
held the patch during mutation runs.

- **RED (base)**: `python3 -B verifiers/verify_skill_checklist.py --json`
  → exit 1, 10 pass / 1 fail; the fail is `governance.citation_resolves`
  naming exactly the four tokens, `evaluated 1363`, `4 recorded correction(s)
  excused` — byte-shape identical to the production before receipt.
  (`build/Kb82E04Governance.evidence.red-full.json`)
- **GREEN (base+patch)**: same command → exit 0, 11 pass / 0 fail;
  `governance.citation_resolves` PASS, `evaluated 1359` (1363−4 excused),
  `7 recorded correction(s) excused`. (`...evidence.green-full.json`,
  `...green-final.json`)
- **Mutation reds** (each restored; `...evidence.mut-M*.txt`):
  - M1 stale restored (`.ufo/wapes` created) → FAIL `stale, the old token now resolves`, exit 1.
  - M2 corrected dead (wapes disposition removed) → FAIL `corrected token ... does not resolve`, exit 1 (also shows LOG.md:2858's pre-existing live citation of the same path goes red — genuine).
  - M3 notice drift (1 byte on LOG.md:2867) → FAIL `line text drifted`, exit 1.
  - M4 horizon 2869→2868 → FAIL `past horizon 2868 or absent` for all three rows, exit 1.
  - M5/M5b unrelated dead subject appended → FAIL naming `corpus/knowledge/kb82e04-probe-gone.md` (+1 problem), exit 1 — genuine absent pointers stay flagged.
- **Driver reproduces all of the above from the patch alone**:
  `build/Kb82E04Governance.redgreen.sh` (`...evidence.driver-run.txt`,
  `...evidence.driver-run.txt` rerun exit 0; RED exit 1, GREEN exit 0, M1/M5 exit 1).

## C2 coupling (coordinated with Kb82E03Checklist)

- With only this patch, `--self-test` reads `1 failure(s) over 1863
  assertions` — the live arm at :2521-2527 still expects `4 recorded
  correction(s)` while the live gate now reports 7. E03's patch deletes that
  live-reading arm (replaced by hermetic fixture replay); per coordination,
  **this patch deliberately does not touch any self-test arm** (the `:2526`
  hunk was dropped). (`...evidence.selftest-patched-only.txt`)
- Integration preview (scratch-only, one-line expectation 4→7, discarded
  after the run): `--self-test` → `0 failure(s) over 1863 assertions`, exit 0
  — assertion count unchanged, so `verifiers/floors-registry.json`'s 1863
  floor stays satisfied. (`...evidence.selftest-integration-preview.txt`)
- E03's fixture pins the row set equal to `GOVERNANCE_ERRATA`/`GOVERNANCE_CORRECTIONS`
  with per-row literal line texts; landing both patches in one revision needs
  E03's fixture table to gain these 3 (row, literal-line) entries — exact
  texts shipped in `build/Kb82E04Governance.notices.txt`. Alternative
  sequencing (E03 first, then this patch) works without touching E03's file.

## Boundaries and non-claims

- Production files untouched; nothing scored after production data; no
  fleet-root or lane-path writes outside the named build/report artifacts.
- No tools installed; no pacman; scratch deleted on exit after copying
  receipts. No subagents dispatched (one coordination message to the owning
  sibling only). Judged axes: freshness (live pins stay fresh/honest),
  operability (live gate green again without suppressing real dead citations).

VERDICT: routed live-citation repair complete — narrowly scoped append-only
patch (3 LOG notices + 3 correction rows + horizon), RED→GREEN reproduced
from base 47dbe878, five fail-closed mutation arms red, C2 self-test
integration path evidenced and sequenced with Kb82E03Checklist; no production
after-value claimed.

DELIVERABLES:
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.corrections.patch
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.notices.txt
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.rebase.py
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.redgreen.sh
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.patch.sha256
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/build/Kb82E04Governance.evidence.*
- /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-82/w1/Kb82E04Governance.md
