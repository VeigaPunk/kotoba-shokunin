---
author: kotoba L1 round 61
date: 2026-10-23
round: 61
lane: kotoba
---

# Round 61 — lesson (kotoba, hyaku run 5, attempt 1)

## Gate

The following source rows were opened on 2026-10-23 by the named seats. Their source snapshots are proposed integration targets, not claimed landed bytes.

- **S112 Claude Code** — https://code.claude.com/docs/en/claude-directory.md — accessed 2026-10-23T19:12:44Z (HTTP 200, 31,144 B, sha256 `1af779e83e62b9017c7966b989e54beb160e9e742d9bf0c45935ad3ae2d82b14`; seat `ScribeS112`; snapshot target `.ufo/waves/round-61/snapshots/S112.page`) — `claude-directory.md:94`: "| `rules/*.md` | `paths` | [Rule frontmatter](https://code.claude.com/docs/en/memory.md#rules-frontmatter-reference) |"
- **S113 VS Code** — https://raw.githubusercontent.com/microsoft/vscode-docs/5f82fce32d763abe6d39d674691f1d2f1b7d5ef9/docs/agent-customization/custom-instructions.md — accessed 2026-10-23T19:13:53Z (HTTP 200, 25,556 B, sha256 `b8f19eab530134e2a1380c365a90a0d1cab2da4e77a9c8663dc5cdd9e95f5fe9`; seat `ScribeS113`; snapshot target `.ufo/waves/round-61/snapshots/S113.page`) — `custom-instructions.md:45`: "Targeted instructions can use `.github/instructions/**/*.instructions.md` or Markdown files in `.claude/rules`."
- **S114 Copilot CLI (re-opens S048)** — https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions.md — accessed 2026-10-23T19:11:44Z (HTTP 200, 8,730 B, sha256 `00e45ea5be05916c1a52092802b84fdb643fc71c46865ccbe09970057bb2c980`; seat `ScribeS114`; snapshot target `.ufo/waves/round-61/snapshots/S114.page`) — `add-custom-instructions.md:32`: "Path-specific instructions are included only when their `applyTo` value matches a file that Copilot CLI is working with."
- **S115 Cursor (re-opens S108)** — https://cursor.com/docs/rules — accessed 2026-10-23T19:09:41Z (HTTP 200, 17,403 B, sha256 `884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8`; seat `ScribeS115`; snapshot target `.ufo/waves/round-61/snapshots/S115.page`) — `rules.md:131`: "Use `globs` to scope a rule to specific files or directories. Separate multiple patterns with commas."
- **S116 — no source row assigned.** The frozen plan assigns S112–S115 to C1 and S117 to C3; the wave census finds no S116 owner. No URL, access, or quote is claimed for S116; no row is invented.
- **S117 kama-shokunin — writing-revision calibration** — `../kama-shokunin/corpus/knowledge/self-assessment-at-writing.md` — opened read-only 2026-10-23 (33 lines, 5,831 B, sha256 `cd6e3730085ed08ca583604390e84c352ea122e4a6386e383d261a0a0b4cf959`; last committed in kama as `6de225c289b7682bf280cffb4a07de3fb7d1275c` at `2026-10-23T16:09:39-03:00`; seats `ScribeC3`, `RevKamaRow`) — `self-assessment-at-writing.md:7`: "a calibration check, not a freshness-only check"

## Mistakes

- **M91 — class: self-assessment overstatement** · The round-60 report's “32 reports, 0 dead” claim conflicts with the closure's count of 29 committed build reports (59/65 seat reports overall); its joint citation also points at `C1-measure.txt` for a base measurement committed in `receipts/freeze2-selftest.txt` (`corpus/lessons/round-60-verifier-spotcheck.md`, §7 defects 2–3). · captured-by: none — no committed-bytes count guarded report claims before this round · fix: the R-a/R-c patterns in `verifiers/check_routed_repairs.py` correct the committed-report count with its counting path and name the precise base-measurement pointer · shown able to fail: the base control reports `routed repairs verified 0 of 6`, exit 1.
- **M92+ — no additional mistake is asserted in this draft.** In-wave reports remain evidence for the L1 to adjudicate; this seat assigns no further lesson class.

## Falsify corrections
- **M92 — class: presence-counter axis claim** · CriticC3Axis exhibited a static counterexample to C3's frozen observables: a tree keeping the S117 row and its index row while replacing the entry with scope-absorbing unsupported claims preserves every named counting observable (`grep -c` 0→1, `test -f`, README row) — the counter cannot measure AXES.md adjacency ("reported, not absorbed"). · captured-by: claim-sizing rule 9 (a target a do-nothing control can reach) · fix: C3 withdrawn as a counted claim before data (plan erratum E1); the curation continues as frontier work; the class is recorded here for future adjacency claims (a presence counter cannot back an adjacency claim — adjacency needs a mismatch/absorption instrument).

## Status changes (contract rule 2, old → new)

- S117 `queued` → `mined` — flipped in the same commit that lands `corpus/knowledge/writing-revision-calibration-round61.md` (its used-by target); no other cell changed.
