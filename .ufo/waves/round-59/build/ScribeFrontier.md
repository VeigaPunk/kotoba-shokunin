Result: DONE — Drafted both append-only texts and their insertion points; no product files changed.

## (a) `PROVINCE.md` § Core

**Insertion point:** after the current round-58 “Custom command files by client” bullet at `PROVINCE.md:23`, before `## Frontier` at line 25.

**Exact text:**

```markdown
- Hook files by client (round 59, new ground beside the round-56 agent-definition and round-58 custom-command maps): where Claude Code, Codex, VS Code, Copilot CLI, Gemini CLI and Cursor document hook-configuration locations and lifecycle events, and the authoring action for rules that must hold every time (S096–S101) — `corpus/knowledge/hook-files-round59.md`, acted on in `SKILL.md` § Hook files by client and counted by `verifiers/check_hook_files.py --rev <rev> --fetch`. This is documentary evidence, not observed runtime behaviour; opencode hook code is a plugin surface, not a hook-file row.
```

## (b) `corpus/README.md` § Frontier

**Insertion point:** after the Round-58 append-only note ending at `corpus/README.md:172`, before `## Known gaps` at line 174.

**Exact text:**

```markdown
**Round 59 (append-only note; new area *Hook files by client*):** six clients' own docs (S096–S101) on where hook configuration lives and which lifecycle events the pages name are recorded in `knowledge/hook-files-round59.md` and acted on in `../SKILL.md` § Hook files by client; the table gives the rule-author action for guidance that must hold every time. The counter `../verifiers/check_hook_files.py --rev <rev> --fetch` checks the cited event identifiers on committed snapshots and live pages, not observed execution. Still not held: client runtime behaviour. opencode hooks are code in plugin folders, so they remain a plugin surface outside this hook-file move.
```

## Evidence and limits

- Read the style exemplars at `PROVINCE.md:22–23`, the Frontier table at `corpus/README.md:99–110`, and the Round-58 note at `corpus/README.md:163–172` before drafting. The proposed insertion points are between the existing Core bullets and Frontier heading, and after the Round-58 note before Known gaps.
- Read the frozen counter specification at `verifiers/check_hook_files.py:2–230`, including the page-printed event-name rule and the frozen predicate; `TARGET = 4` and `NEW_TARGET = 5` are at lines 253–254. The proposed wording does not claim a real-build counter result.
- Read `.ufo/waves/round-59/controls/CtlFabEvents.md:28–56,128–143` and `CtlFabSnapshot.md:5–15`. These are control receipts, not a real-build verdict; the snapshot control explicitly limits its event check to printed identifier presence, not semantics. I ran neither control nor the C1 counter.
- At read time, `corpus/knowledge/hook-files-round59.md` and `corpus/lessons/round-59.md` were absent (`read` returned “Path … not found”). Thus this deliverable is draft text only; source rows, entry, lesson, snapshots, skill section, and a real-data counter result are not asserted as landed here.
- **Commands/outcomes:** `timeout 60 ls -l /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ScribeFrontier.md` → `-rw-r--r-- 1 vgpnk vgpnk 3651 Oct 23 06:36 /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-59/build/ScribeFrontier.md` (exit 0; this was the required pre-correction artifact check). No build, tests, lint, source fetches, or counter execution by this seat. No tools installed or updated. No Git/jj writes. The only file written is this report.
- **Touched surfaces:** only `.ufo/waves/round-59/build/ScribeFrontier.md`. `PROVINCE.md` and `corpus/README.md` are proposed surfaces and were not edited.
- **Out of scope:** applying either draft, making a C1 admission judgment, or asserting measured runtime behaviour. The documented event identifiers and configuration locations are not evidence that clients execute hooks.

Artifact: `.ufo/waves/round-59/build/ScribeFrontier.md`
