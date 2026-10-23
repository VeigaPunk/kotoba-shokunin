Result: HOLDS — at `a975cbbf` none of the six landed hook tokens has a case-insensitive segment-boundary hit outside `.ufo/`, so `new ground 6` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` matches an independent recount. They do not occur only in files added after the base.

Attacked: C1 `new ground 6` (the base-tree half). Not re-fetched; the live `found 6 of 6` half is the receipt's, not this seat's.

## Tokens

First backtick of each Hook config cell in `SKILL.md` at `c63ccc6823e1f6a8577acbb43d19551eadbbee9a` (heading line 121, rows 127–132). `normalise` strips one leading `~/`. opencode's cell has no backtick, so it is not one of the six. The six casefolds are distinct (6/6).

| Client | raw cell token | form searched |
|---|---|---|
| Claude Code | `.claude/settings.json` | `.claude/settings.json` |
| Codex | `~/.codex/hooks.json` | `.codex/hooks.json` |
| VS Code | `.github/hooks/*.json` | `.github/hooks/*.json` |
| Copilot CLI | `~/.copilot/hooks/*.json` | `.copilot/hooks/*.json` |
| Gemini CLI | `.gemini/settings.json` | `.gemini/settings.json` |
| Cursor | `.cursor/hooks.json` | `.cursor/hooks.json` |

Counter blob `c63ccc68:verifiers/check_hook_files.py` sha256 `f695d59e109c20a80c1874298f580aadf1cfec0b353a8576ac3e238fb50dbe71` (matches the receipt). Empty diff of that path against HEAD `3f15f844` (work tree was past the measure commit; every search below names the revision). `new_ground` (`verifiers/check_hook_files.py:1254-1260`) counts distinct `casefold(norm)` of **found** rows whose norm is not held. `held_in_base` (`:1211-1227`, skip at `:1131-1133`) ignores a path equal to `.ufo` or starting with `.ufo/`. Without `--fetch`, `main` forces ground 0 (`:2398-2399`); the receipt line `live not run; new ground 0` is that branch, not a second base scan.

## Method

Own scan, lane code not executed. For each normalised token, fixed-string case-insensitive git grep, then a segment-boundary check on every hit with the same predicate as `held_in_text` / `held_right_ok` (`:1170-1201`), reimplemented in scratch and not imported: casefold, per line; left edge is start-of-line, whitespace, or one of `` `"'([</~= ``; right edge rejects an ASCII letter/digit/`_`/`-`, and also `.` followed by an ASCII letter or digit. `*` is literal (`-F`). NUL blobs skipped, as the counter skips them.

Census command shape (plan `plans/round-59.md:75`), run 2026-10-23T09:55:36Z:

```
git --no-optional-locks grep -q -i -l -F -e <token> a975cbbf00534443c49bf02e29c813a3db0bf0f8 -- . ':!.ufo'
```

Exit 1 (no match) for all six. Same six commands with `-a` (binary as text) also exit 1. Whole-tree grep (no pathspec) exits 1 for `.codex/hooks.json`, `.github/hooks/*.json`, and `.copilot/hooks/*.json` (nowhere in the base tree, including `.ufo/`). It exits 0 for the other three, and every hit path is under `.ufo/`. The `:!.ufo` pathspec leaked no `.ufo` path and missed no outside path (outside list empty).

Boundary check on those `.ufo` hits: all of them are real boundary hits, not substring false positives. They stay out of G because of the `.ufo` exclusion, which is the frozen rule. The 47,815,579-byte `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` was over a 5 MiB cap on the first pass; the tip pass read that same unchanged blob and counted boundary hits (Claude line 557534, `Load settings from .claude/settings.json)`; Gemini 8 hits on the same file). Still under `.ufo/`.

Base boundary hits **outside** `.ufo/`: 0, 0, 0, 0, 0, 0. Unheld distinct tokens = 6. With the receipt's found = 6, G = 6. Any found subset of these six is also unheld, so this scan cannot inflate G above the found count, and it cannot be the reason G would fall short of 6.

No tool installed.

## Where each token is at `c63ccc68`

Not only new files. Three paths already existed at `a975cbbf` and were modified (`M`); at the base each had boundary count 0, so the token was added in the round-59 diff. Unchanged files that already held a token are all under `.ufo/` (excluded from G). Classification is `git diff --name-status a975cbbf c63ccc68` joined to `git grep -ilF` at the tip. `A` = added path, `M` = pre-existing, `UNCHANGED` = in both trees and not in that diff.

Tracked paths (outside `.ufo/`):

| token | M (pre-existing) | A (new path) |
|---|---|---|
| `.claude/settings.json` | `SKILL.md:127`, `corpus/README.md:99` | `corpus/knowledge/hook-files-round59.md`, `corpus/lessons/round-59.md`, `plans/round-59.md`, `verifiers/check_hook_files.py` |
| `.codex/hooks.json` | `SKILL.md:128`, `corpus/README.md:99` | `corpus/knowledge/hook-files-round59.md`, `corpus/lessons/round-59.md`, `plans/round-59.md` |
| `.github/hooks/*.json` | `SKILL.md:129`, `corpus/README.md:99`, `corpus/SOURCES.md:110` and `:111` | same four new paths as Claude |
| `.copilot/hooks/*.json` | `SKILL.md:130`, `corpus/README.md:99`, `corpus/SOURCES.md:111` | entry, lesson, plan (not the verifier) |
| `.gemini/settings.json` | `SKILL.md:131`, `corpus/README.md:99`, `corpus/SOURCES.md:112` | entry, lesson, plan (not the verifier) |
| `.cursor/hooks.json` | `SKILL.md:132`, `corpus/README.md:99`, `corpus/SOURCES.md:113` | same four new paths as Claude |

`corpus/SOURCES.md` S096 (`:108`) and S097 (`:109`) paraphrase the locations and do not contain `.claude/settings.json` or `.codex/hooks.json`. S099's row contains both `.github/hooks/*.json` and `~/.copilot/hooks/*.json`. `verifiers/check_hook_files.py` literals cover Claude, the VS Code glob, and Cursor only (Codex / Copilot / Gemini norms are absent there). `corpus/README.md:99` is one index sentence that contains all six.

Unchanged `.ufo/` paths that already held the token at the base (boundary hits, not new):

- `.claude/settings.json` (7): `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`; `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json`; `.ufo/waves/round-53/build-dispatch.json`; `.ufo/waves/round-53/build-spec.json`; `.ufo/waves/round-53/build-taskcall-sent.json`; `.ufo/waves/round-53/build/ScoutClaudeBehaviour.md`; `.ufo/waves/round-57/build/SrcClaudeCode.md`
- `.gemini/settings.json` (6): the strings file; `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json`; `.ufo/waves/round-51/build/SrcGemini.md`; `.ufo/waves/round-53/build/ScribeAgentsMdSpec.md`; `.ufo/waves/round-58/controls-call.json`; `.ufo/waves/round-58/controls/CtlC1OffTopic.md`
- `.cursor/hooks.json` (2): `.ufo/waves/round-56/controls/CtlC1RealNoForm-v12.md`; `.ufo/waves/round-56/controls/CtlC1RealNoForm-v12.txt`

`.codex/hooks.json`, `.github/hooks/*.json`, and `.copilot/hooks/*.json` have no unchanged path. Every other tip hit is an added `.ufo/waves/round-59/` file (build reports, controls, w0 census, snapshots). Snapshot hits: S096 and S098 carry `.claude/settings.json`; S097 carries `.codex/hooks.json`; S098 and S099 carry `.github/hooks/*.json`; S099 carries `.copilot/hooks/*.json`; S100 carries `.gemini/settings.json`; S101 carries `.cursor/hooks.json`.

Tip file counts from `git grep -ilF`: Claude 38, Codex 24, VS Code 29, Copilot 24, Gemini 30, Cursor 29. Full `status / ufo|tracked / path` list: scratch `/fast/scratch/hyaku/kotoba-r59/ScoutHeldGroundTip/tip-files.txt` (not a lane file). Probe: `/fast/scratch/hyaku/kotoba-r59/ScoutHeldGroundTip/recount.py`.

## Confidence

High on the base-tree count and on the tip path list. Not checked: the live fetch that marks a row found (sibling work). No remaining gap on whether these six are held outside `.ufo/` at `a975cbbf`.
