Result: DONE — drafted both requested insertion-ready texts; no product files or C1 evidence were changed or claimed.

# Round 60 Frontier documentation drafts

## Behavior
The drafts describe the four matching-path clients (Claude Code, VS Code, Copilot CLI and Cursor) and distinguish the directory-scoped Codex, Gemini CLI and opencode cases. They state the evidence is documentary and leave runtime loading, precedence between scoped and always-on files beyond what pages state, and directory-scoped clients unheld.

## (a) `PROVINCE.md` § Core

**Insertion point:** immediately after the current `Hook files by client` bullet (`PROVINCE.md:24`), before the blank line and `## Frontier` (`PROVINCE.md:26`). This follows the round-58/59 Core bullet style (`PROVINCE.md:23-24`).

```md
- Scoped rule files by client (round 60, new ground beside the round-56 agent-definition, round-58 custom-command and round-59 hook-file maps): where Claude Code, VS Code, Copilot CLI and Cursor document rule files scoped to matching paths, each client's scope key, and the authoring action the page names for scoping a rule to the files it is about instead of loading it every turn; Codex, Gemini CLI and opencode are directory-scoped rather than qualifying for this matching-path map (S103–S109) — `corpus/knowledge/scoped-rules-round60.md`, acted on in `SKILL.md` § Scoped rule files by client and counted by `verifiers/check_scoped_rules.py --rev <rev> --fetch`. This is documentary evidence, not observed runtime behaviour; runtime loading, precedence between scoped and always-on files beyond what a page states, and directory-scoped clients stay unheld.
```

## (b) `corpus/README.md` § Frontier

**Insertion point:** append after the existing Round-59 note (`corpus/README.md:177`) and before `## Known gaps` (`corpus/README.md:179`). The Round-59 note was read first and used as the style anchor.

```md
**Round 60 (append-only note; new area *Scoped rule files by client*):** the seven-client documentation census (S103–S109) records Claude Code, VS Code, Copilot CLI and Cursor on rule files scoped to matching paths, their scope keys and authoring actions, and Codex, Gemini CLI and opencode as directory-scoped rather than matching-path clients, in `knowledge/scoped-rules-round60.md`; the matching-path guidance is acted on in `../SKILL.md` § Scoped rule files by client. The counter `../verifiers/check_scoped_rules.py --rev <rev> --fetch` checks row tokens, cited source/quote, snapshot hashes, and Scope key/Action evidence on committed snapshots; `--fetch` additionally requires the quote and scope-key site on the live page. Still not held: runtime loading; precedence between scoped and always-on files beyond what a page states; directory-scoped clients.
```

## Gates and evidence
- The round-60 plan describes the section/entry surface and semantic evidence requirements (`plans/round-60.md:21-44`), the v2 census and frozen counter identity (`plans/round-60.md:141-153`). The final eligible-client set is Claude Code, VS Code, Copilot CLI and Cursor (`plans/round-60.md:145-148`).
- No source pages, SOURCES rows, snapshots, knowledge entry or SKILL section were independently checked for this drafting assignment. These texts are proposals, not evidence that those surfaces landed.
- `python3 -B verifiers/check_scoped_rules.py --rev <rev> --fetch` was not run by this seat. No counter result, target pass, snapshot/hash verification, or control receipt is claimed.
- No tools were installed or updated.

## Touched surfaces and limits
- Written artifact: `.ufo/waves/round-60/build/ScribeFrontier.md` only. `PROVINCE.md` and `corpus/README.md` were read for insertion points and style but not edited; the proposed insertion text above is for the L1 to integrate.
- Out of scope: implementing the entry or SKILL section, creating sources/snapshots, editing lane product files, running C1 checks, and asserting runtime behavior or precedence not stated by a page.
- Provenance: current Core/frontier anchors and round-59 style are `PROVINCE.md:22-26` and `corpus/README.md:177-179`; claim semantics and counter description are the frozen round-60 plan. Source-page content and current build completion remain unverified here.
