Result: DONE — the live host lacks the listed OpenCode agents directory; a dated, line-preserving replacement is drafted for the exact work-revision line.

## Findings

- **Host check (2026-10-23):** ran exactly `ls -la ~/.config/opencode/agents/ 2>&1; ls ~/.config/opencode/ 2>&1`. The first command printed `ls: cannot access '/home/vgpnk/.config/opencode/agents/': No such file or directory`; the second listed `cli.json`, `opencode.json`, and `service.json`. The compound command returned exit 0 (the final `ls` succeeded). Thus the agents directory is absent on this host; the parent config directory exists. This is a host-local observation, not a claim about other machines.
- **Work-revision location:** `01312a77e36317feb6e961aba77841ddab1225ca`. Read-only command `git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin blame -L 515,525 01312a77e36317feb6e961aba77841ddab1225ca -- SKILL.md` exited 0 and locates the target at **SKILL.md:520** (the same historical count is preserved at 520; lines 521–525 continue its details).
- **Old → proposed new text (one source line for one source line):**
  - Old: ``- `~/.config/opencode/agents/*.md` (18 files, 14–197 lines) — agent-definition``
  - New draft: ``- `~/.config/opencode/agents/*.md` (historical: 18 files, 14–197 lines; absent on this host as of 2026-10-23) — agent-definition``

The draft dates the observation, explicitly labels the 18-file count as historical, and preserves it. It is a single-line replacement, so it adds no SKILL.md source lines. It is a proposal only; this seat did not edit SKILL.md.

## Gates and touched surfaces

- Passed the requested read-only host listing and located the target line at the named work revision.
- No build, tests, verifier/counter, or external-source checks were requested or run.
- Only touched surface: this report artifact. No product files, counters, lane Git/jj state, or other artifacts were modified. No tools were installed or updated.

## Out of scope / limits

No claim is made about other hosts or about whether any historical file contents still exist elsewhere. No C1/C2 work or verifier changes were made.

Artifact: `.ufo/waves/round-57/build/ScribeR6StaleLine.md`