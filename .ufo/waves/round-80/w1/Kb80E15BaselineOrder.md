# Kb80E15BaselineOrder — integration-order runbook (round 80 w1)

Seat: executor (leaf, no spawns). Date 2026-10-27. Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Round base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; lane tip at read time
`a481913bafeb1ec5c231fd581f13da6ae5a306dc` (base + Addendum 1 + Addendum 2, `plans/` only).
Scratch `/fast/scratch/hyaku/kotoba-r80/Kb80E15BaselineOrder` (removed before yield; receipts copied out first).

Item: from the E03/E04/E05/E10 outputs, write the ordered integration recipe the L1 runs — path
groups, the gate after each, the dirty-tree precondition, the `--carry` decision tree, the final-tip
no-harm battery with expected greens, and the refresh script's exit-2/exit-3 semantics.

## Deliverable

`.ufo/waves/round-80/build/Kb80E15BaselineOrder.md` (28 292 B) — the runbook: pre-flight, groups
G1–G8 with the exact `jj-lane.sh` path groups and the gate reading after each, the refresh exit
0/2/3 table, the `--carry` tree, the 12-command final battery, and the traps. Receipts in
`.ufo/waves/round-80/build/Kb80E15BaselineOrder/` (`R1`–`R16`).

## What I measured first-hand (own exit captured, no pipelines)

1. **I re-ran the composed stack end to end in my own scratch** by executing E06's published
   `Kb80E06CounterErratum.landing-recipe.sh`: rev `40ac8b7188621febb8d7a56559ba20c73fdfca52`,
   counter sha256 `15cc17614e61bdc47122bf501da951de3dbde6444b1ed4a98ca8192c2329ddba`, instrument
   blobs `cc182613a4d089c41e44f11b50e03b45ce582dd8` / `89f392daab3e4181db3ded7676ca0879871ef7ff`
   (**exactly** the two pins E06's counter names), six-instrument numstat vs the pinned guard base
   `072048fa` = `22/3 + 10/3 + 27/4` = **59 added / 10 deleted (cap 60, one line of headroom)**,
   registry `63 of 63; phantom 0`, refresh `9/9` exit 0, and the amended counter on that tree:
   **`guards 5 of 5; tip battery exit 0: 6 of 6`, exit 0** (`R6`, `R7`). The C1 recipe is therefore
   measured reachable by me, not only by the seat that built it. It is **not** scored here.
2. **The refresh script's refusal surface** (`R1`–`R5`): dirty tree incl. untracked → exit 2;
   `--carry corpus.index.*` → exit 2; clean tree with unfixed instruments → `unindexed 1` exit 2;
   carrying only `report_dead` advances the refusal to `commit_unresolvable` (the script stops at the
   *first* nonzero zero-mode class) exit 2; carrying **both** writes the file but leaves the gate
   RED — `post-refresh: 7/9 checks pass, exit 1, drift: report_dead, commit_unresolvable`,
   `independent: red (exit 1)`, exit 0. So `--carry` can never buy a green tip: the runbook's tree
   says carry nothing at the final tip.
3. **`jj-lane.sh commit` refuses the round-76 symlink when named as a file.** Its canonicalisation
   (`realpath -m --relative-to=.`) resolves the symlink out of the lane root →
   `jj-lane: path escapes the lane root: ../.ufo/reports/round-76/kotoba.md`, exit 1 (`R13`).
   Naming the **parent directory** works and records mode `120000` with blob
   `bf7c7e0c0c39a57c49224c87348afc74dca14db4` (`R14`). This is the one integration step that would
   silently fail if run the obvious way.
4. **Registry/order arithmetic** (`R10`, `R11`, `R12`): base `60 of 62` exit 1 (the two withdrawn
   rows); counter file present without its row → `60 of 63` exit 1; SKILL.md row before the counter
   file → `phantom 1` exit 1 (E14/E06 measured the same shape); a new verifier needs **no** floors
   row, and touching `floors-registry.json` alone makes the floors gate exit 2.
5. **`SKILL.md` must be ONE merged edit**: `Kb79E01Registry.patch` and `Kb80S09SkillRule.patch`
   insert at the same table end; either application order fails, `--3way` fails. The verified merge
   is 595 lines (≤ 600) with `63 of 63` (`R6`).
6. **MANIFEST.sha256 is absent** from `.ufo/waves/round-79/snapshots/` and the C2 counter's registry
   row pins that path, so the row is non-conformant until it exists (E03 F4, confirmed by me:
   `no pinned path … does not exist`).
7. **The plan's `check_sibling_census.py --skill SKILL.md` is not runnable** — the CLI requires a
   `CENSUS.md` positional, so the literal command exits **2** (usage). Working form:
   `check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --skill SKILL.md` →
   exit 0, `rows 20 verified 20` / `skill description names 10 of 10` / `length 1021 of 1024` (`R16`).
8. **The C2 counter published in `build/` is not yet the round-80 counter**: `ENTRY` still names
   `…round79.md`, the print lines are `allowed-tools surfaces backed N of 6` / `script-only world:
   M of 6` (the plan's frozen sentence is only in its docstring), and its `SELF_SHA`
   (`1f9744c8…`) does not match its own blanked sha (`f6569f6b…`), so it exits 2 with
   `environment error: counter drifted`. Refilled in scratch it runs and reports
   `allowed-tools surfaces backed 0 of 6`. E07 owns this; the runbook tells the L1 to verify the
   landed counter's headline and `ENTRY` instead of assuming them.

## Blockers / risks named for the L1 (not repaired by me)

* **`.ufo/wapes`** — a stray 594 B probe transcript at the lane's `.ufo/` root (another seat's
  output). It is untracked, `jj-lane.sh`'s path guard does not block it, and it keeps
  `git status --porcelain --untracked-files=all` non-empty, which makes the refresh refuse. The L1
  must delete or relocate it; no seat may.
* **The lane tree is dirty with 639 untracked wave entries**; the refresh needs a clean tree, so the
  wave evidence must be committed first (group G6) — r79 tracked its wave dir, so this is precedent,
  not invention.
* **E05 published no patch and no `.blobs` file**; the grammar class exists only inside Y01's bundle.
  The practical route is E06's landing recipe (bundle-minus-counter + E06's counter), which I
  re-ran green. If a different grammar class lands, the two pins move by one hex string each.
* **C2 counter state** (point 8) — a C1-green tip does not imply a C2-green counter.
* The composed stack leaves **one line** under the 60-line cap; a larger grammar class is an honest
  stop under the plan's arithmetic, not a reason to widen the cap.

## Limits

I did not score any claim after-value, did not edit the lane tree or its git/jj state, and did not
run the pinned instruments beyond reading them. The battery value in `R7` was measured on **E06's
recipe stack in scratch**, not on the lane tip — the tip does not exist yet. No tool was installed or
upgraded; pacman was not invoked; no host service was restarted; scratch was removed.

VERDICT: The ordered recipe is written and every load-bearing step is measured — the composed stack reads `guards 5 of 5; tip battery exit 0: 6 of 6` (exit 0) with pins `cc182613…`/`89f392da…` and 59/60 lines, the refresh refuses on a dirty tree or a nonzero zero-mode class (exit 2) and leaves a written file on exit 3, `--carry` can never produce a green tip (7/9, exit 1), and `jj-lane.sh` must be given the symlink's parent directory because the symlink path is refused as a lane-root escape.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E15BaselineOrder.md, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E15BaselineOrder/, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E15BaselineOrder.md
