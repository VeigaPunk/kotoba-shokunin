# R75Attack29 — falsification of R75Facet29 (skill-eval threshold mismatch)

Seat: `R75Attack29` (leaf, read-only, no delegation). Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git rev-parse HEAD`). Target: `.ufo/waves/round-75/w1/R75Facet29.md`. No lane source edited; only this report and my scratch (`/fast/scratch/hyaku/kotoba-r75/R75Attack29/`, emptied) written.

## Verdict

**Does not survive as an actionable finding.** The central factual claim is TRUE — I byte-verified what the facet admitted it never opened — but the finding is a **duplicate** (settled inside the cited artifact itself and by sibling facet `R75Facet02` at the same revision), its **control-weakness premise is false** (the round-70 entry's action already specifies exactly the control facet29 proposes), and its headline **boundary fixture is unconstructible at reference defaults as written**.

## Facet's central factual claim

`corpus/knowledge/skill-eval-artefacts-round70.md:33-34` records a prose/code mismatch: the guide's trigger rule is "above the threshold" (F7, S213) while the cited `run_eval.py` passes at `>=` (F8, S211) — implementation accepts equality, prose says strictly-above. Facet presents this as "a specific, independently falsifiable description-audit candidate" and flags "control weakness: existing round-70 recommendation leaves boundary semantics under-specified."

## Findings by severity

### F-MAJOR-1 — Duplicate: the claim is already settled three times over

- **In the cited artifact itself (committed at 65a5c7a):** F7 (`:33`) and F8 (`:34`) state the mismatch with located quotes, and § "The one disagreement, and the action it implies" (`:56-72`) carries the full boundary analysis facet29 gestures at — default 3 runs cannot reach 0.5, even run counts open the gap, per-query-string division (`:213-229` of the snapshot) widens it, non-default thresholds make it hit whenever threshold × runs is integral, disagreement runs one way only, and an explicit action at `:70-72`. Facet29 adds no fact the artifact does not already state.
- **Sibling facet, same revision:** `R75Facet02.md` is a dedicated byte-level audit of this exact disagreement (its target table: paragraph `:56-72`, snapshots sha256 `7cc54fbb…`/`43e3b8f8…`, comparator branches `:232`/`:234`, its own enumeration). Facet29's factual content is a strict subset.
- **Post-wave-1 remediation already issues facet29's remedy:** the entry's "Round 75 correction — equality wording" (working tree `:86-88`, appended after 65a5c7a; uncommitted delta confirmed via `git diff`, committed blob is 85 lines) cites `R75Facet02.md:28-36` and instructs "tell a reader to name the comparator used by the implementation under evaluation" — precisely facet29's "Record threshold, numerator/denominator, and comparison operator."

### F-MAJOR-2 — Incorrect inference: "boundary semantics under-specified" is contradicted by the cited bytes

Facet's axis table claims the round-70 recommendation leaves boundary semantics under-specified. Entry `:70-72` (committed at 65a5c7a): "**Action:** keep threshold × runs non-integral (an odd run count at 0.5), de-duplicate query strings, **or state which rule the report applies**." The third disjunct *is* naming the comparator — the control facet29 proposes. Its "Concrete control" is therefore vacuous as a delta: it prescribes what the artifact it critiques already prescribes, twice (committed action + working-tree correction).

### F-MODERATE-1 — Proposed boundary fixture is unconstructible at reference defaults as written

Facet: "include a deterministic boundary fixture with trigger rate exactly equal to threshold." At the reference defaults (3 runs, threshold 0.5) the reachable rates are {0, 1/3, 2/3, 1} — exactly 0.5 is unreachable. My enumeration (pure arithmetic, run in scratch): disagreement-at-equality occurs only at even run counts (n=2:k=1, n=4:k=2, n=6:k=3). A fixture built per facet29's text under defaults would silently exercise no boundary case. The entry states this (`:60-64`) and facet02 enumerated it; facet29 acknowledges neither, so its control needs an even run count, a duplicated query string, or a non-default threshold — none stated.

### F-MINOR-1 — Cross-facet pin discrepancy (context; facet02 is not my seat)

Facet02 cites the fact rows at `:24-25` and "source line 4"; the committed blob at 65a5c7a has F7/F8 at `:33-34` (`git show 65a5c7a:corpus/knowledge/skill-eval-artefacts-round70.md | grep -n '^| F7\|^| F8'`) and S211 at `:3`. Facet29's pins are the accurate ones.

## What survives the attack

- **The mismatch is real.** Byte-verified by me: `.ufo/waves/round-70/snapshots/S210-optimizing-descriptions.md:92` — "A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default)"; `.ufo/waves/round-70/snapshots/S211-run_eval.py.txt:232` — `did_pass = trigger_rate >= trigger_threshold`, `:234` — `did_pass = trigger_rate < trigger_threshold`. Snapshot sha256 and byte sizes match the entry's own claims (`43e3b8f8…`, 11 464 B; `7cc54fbb…`, 13 403 B).
- **Every facet29 line pin is exact at 65a5c7a:** `:3` (S211, tree `dbd4588f…`, lines 230–234), `:6` (S213, upstream rev `69ef37e…`), `:33-34` (F7/F8), `:48` (labelled/repeated/split block 48–51), `:54` ("twice, not independent corroboration"), `:76` (scope refusal block 76–80). Working tree vs committed blob differ only by the appended correction (`:86-88`), which touches none of facet29's cited lines.
- **Secondary citations exact:** `corpus/lessons/round-74-verifier-spotcheck.md:102` (depth unchanged, no declared claim) and `:104` (consistency/calibration sub-axis unchanged); `plans/round-74.md:47-51` (C1 declared as a depth claim on the sibling body-craft guides).
- **Scope:** in scope — documentary guidance plus one implementation discrepancy; no performance claim, no client-native-execution claim. Facet's honesty disclosures (bytes not opened, nothing executed) are accurate.
- **Stated control not executed, safely decided part run:** running the fixture requires `run_eval.py`, which shells out to `claude -p` — model experiments out of bounds this wave (facet02 reached the same conclusion). I ran the decidable arithmetic (rate reachability / disagreement sets) locally; no files written outside scratch.

## Residual risk and verification gaps

- Live pages not fetched (documented): an upstream change to the guide wording would be caught by the entry's designated recheck (`python3 -B verifiers/check_skill_evals.py --rev <rev> --fetch`); not run — live fetch out of bounds for this seat.
- The working tree at attack time differs from 65a5c7a only by that uncommitted correction; all verdicts above are pinned to the committed blob except where explicitly labeled working-tree.
- `run_eval.py` behavior is code-reading plus arithmetic, not a measured run — same limitation facet29 and facet02 disclose; it does not affect the duplicate/incorrect-inference verdicts.

## Commands/evidence used

`git rev-parse HEAD`; `git show 65a5c7a:<entry> | grep -n` + `sed -n` window reads; `git status --porcelain` and `git diff` on the entry (uncommitted `:86-88` delta identified); `sha256sum` + `wc -c` on both snapshots; `grep -n` line maps on entry, snapshots, spotcheck lesson, round-74 plan; `read` windows on facet02, spotcheck `:97-111`, plan `:43-57`; `python3 -c` enumeration of reachable rates and disagreement sets at t=1/2 for n=1..6 (scratch cwd, no writes). No git/jj mutation, no pacman, no installs, no live fetch, no lane edits.
