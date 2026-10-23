Result: DONE — drafted the Round 58 C1 Frontier note and Core line without stating a counter result.

## Verbatim draft — `corpus/README.md` § Frontier, after the Round 57 note

**Round 58 (append-only note on the custom-command row above):** *Custom command files by client* — the seven-client map of documented reusable command/prompt file surfaces, what a file sets, and the authoring action is held in `knowledge/command-files-round58.md` and acted on in `../SKILL.md` § Custom command files by client. Six clients have a documented client-owned folder in the new source rows S089–S091 and S093–S095; Copilot CLI's existing command-reference source (S031) points to Claude Code's `.claude/commands/`, not a separate eligible client-owned folder (S092 is reserved only if a new non-base Copilot CLI source is needed). Still not held: any client run, observed runtime argument-substitution behaviour, or precedence when a skill and a custom command share a name.

## Verbatim draft — `PROVINCE.md` § Core, appended after the existing client-file entry

- Custom command files by client (round 58): the seven-client map of documented reusable command/prompt folders, what a file sets, and the authoring action — six client-owned folders in S089–S091 and S093–S095; Copilot CLI's existing command-reference source S031 points to Claude Code's `.claude/commands/`, not a separate eligible folder — is in `corpus/knowledge/command-files-round58.md` and `SKILL.md` § Custom command files by client. Still not held: client runs, runtime argument substitution, or precedence against a same-named skill.

## Evidence and scope

- The frozen C1 plan names all seven client rows, identifies Copilot CLI as NOT ELIGIBLE because its command reference reads `.claude/commands/`, and lists the six eligible folders and census source locations: `plans/round-58.md:52-68`. It records the new source assignments and the conditional S092 slot in the task context; the proposed wording keeps that distinction rather than claiming seven independent client-owned folders.
- The frozen counter contract describes the C1 claim as a per-client table for command/prompt file location, what the file sets, and author action, backed by new 2026-10-23 SOURCES rows and a lesson Gate quote: `verifiers/check_command_files.py:24-31,75-88`. I read the contract only; I did not run it or state its result.
- Round 56/57 note style and placement: `corpus/README.md:142-159`; existing Core entry style: `PROVINCE.md:21-24`.
- Drafted surfaces: only this report file. I did not edit `corpus/README.md`, `PROVINCE.md`, or product code.
- Gates/out-of-scope: this scribe did not fetch sources, run clients/verifiers/counters, build, test, or lint. Client execution, runtime argument substitution, and same-name skill/command precedence remain unheld.
- Draft limitation: at writing time, `corpus/knowledge/command-files-round58.md` and `corpus/lessons/round-58.md` returned not found, and `build/SrcCodex.md` was the only direct `build/Src*.md` report visible. These blocks are proposed copy, not evidence that entry/SKILL/SOURCES/Gate integration is complete.
- Artifact: `.ufo/waves/round-58/build/ScribeFrontier.md`.
