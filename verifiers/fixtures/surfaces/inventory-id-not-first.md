# fixture census — instruction surfaces

Preamble prose.

## Class inventory

| class_id | literal | kind | verdict | evidence |
|----------|---------|------|---------|----------|
| GEMINI.md | `omp:gemini/GEMINI.md` | loader-group | governed | loads on session start |
| CLAUDE.md | `omp:claude-md/CLAUDE.md` | loader-group | excluded | var-bound group (`BWr`), file absent on host |
| rules | `omp:cursor/rules` | loader-literal | governed | directory-of-files registration |
| AGENTS.md | `opencode:instructions/AGENTS.md` | loader-literal | governed | priority list element |
| CLAUDE.md | `opencode:instructions/CLAUDE.md` | loader-literal | governed | gated priority list element |
| CONTEXT.md | `opencode:instructions/CONTEXT.md` | loader-literal | governed | last priority list element |
| AGENTS.md | `opencode:config/AGENTS.md` | loader-config | governed | config join candidate |
| CLAUDE.md | `opencode:claude-home/CLAUDE.md` | loader-config | governed | home join candidate |
| instructions | `opencode:config/instructions` | loader-config | governed | declared list loop |
| https:// | `opencode:config/instructions-remote` | loader-config | governed | remote filter + render |
| <system-reminder> | `opencode:read-hook/instructions` | loader-literal | governed | read-tool channel |
| AGENTS.md | `opencode:instruction-context/AGENTS.md` | loader-literal | governed | second subsystem: ambient all-match walk + ungated config candidate |

## Method notes

Prose mentioning `omp:gemini/GEMINI.md` outside a table row — must NOT count.
