# CritSourcesRecheck — round 67 wave 2

## Scope and measured identity

- **Attack:** the S123/S124/S129 `recheck` transforms: bare cadence in the adopted registry, presence of each stripped condition in the lesson Gate, and substantive identity between that Gate condition and the corresponding staged row.
- **Measured revision:** `da86c03e482a6aef433c34d733726b37c7cf6607`. `git rev-parse HEAD` returned that revision, and the scoped registry/lesson paths had no working-tree diff. The staged comparison source was the read-only `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md`.
- **Axis:** calibration, specifically consistency and provenance of the assimilation record. This is a scoped attack result, not a verdict on the frozen C1/C2 counters.

## Verdict

**Counterexample found: S129 fails condition preservation.** All three adopted cells are bare cadences; S123 and S124 also preserve their staged conditions in the Gate. S129 does not.

### F1 — S129's Gate condition is substituted, not stripped from its staged row

- **Staged condition:** `/home/vgpnk/Projects/shokuknow/merge/kotoba/SOURCES.append.md:13` says:
  > `180d — re-fetch the arXiv abstract and confirm the 853-task, 12-level and ~40% figures (ran 2026-10-23)`
- **Recorded condition:** `corpus/lessons/round-67.md:58-62` claims that the stripped prose from each row is recorded there, but `:61` instead gives S129 as:
  > `re-check arXiv:2604.09443 for a v2`
- **Adopted cell:** `corpus/SOURCES.md:136` contains the bare cadence `90d`, so the defect is not prose left in the registry.

This both **drops** the staged abstract/853-task/12-level/~40% checks and **invents a row condition** about v2 that the staged S129 row does not contain. The v2 wording does occur in the separate staged entry at `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/instruction-authority-ladder.md:8`; that different artifact is not evidence that it was stripped from S129's registry cell. It is also stale beside the adopted row's own `record v4` pin (`corpus/SOURCES.md:136`) and leaves the row's numerical claims without their staged recheck condition.

**Impacted axis:** calibration — the Gate gives false provenance for the preserved condition and no longer faithfully records what the adopted cadence is meant to recheck.

**Smallest safe correction:** in `corpus/lessons/round-67.md:61`, replace only S129's quoted condition with:
> `re-fetch the arXiv abstract and confirm the 853-task, 12-level and ~40% figures`

No registry-cell change is needed for this defect.

## Checks without a mismatch

| row | adopted cadence | staged versus Gate condition |
|---|---|---|
| S123 | `corpus/SOURCES.md:134` = bare `90d` | Matches: staged `:7` versus `corpus/lessons/round-67.md:58-60` (five levels plus override sentence). |
| S124 | `corpus/SOURCES.md:135` = bare `90d` | Matches: staged `:8` versus `corpus/lessons/round-67.md:60-61` (20-query, 60/40, 3-run, 5-iteration). |
| S129 | `corpus/SOURCES.md:136` = bare `90d` | Cadence passes; condition fails as F1. |

The omitted parenthetical `(ran 2026-10-23)` is run metadata, not part of the forward recheck condition, so its omission is not counted as a dropped condition. S129's cadence changed from staged `180d` to adopted `90d`; both are bare cadences, and the assigned checks do not require cadence preservation, so that change is not counted as an additional mismatch.

Report: .ufo/waves/round-67/w2/CritSourcesRecheck.md
