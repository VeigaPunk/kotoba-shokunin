# fixture census — instruction surfaces

Preamble prose.

## Class inventory

| literal | class_id | kind | verdict | evidence |
|---------|----------|------|---------|----------|
| GEMINI.md | `omp:gemini/GEMINI.md` | loader-group | governed | loads on session start |
| rules | `omp:cursor/rules` | loader-literal | governed | directory-of-files registration |
| CLAUDE.md | `omp:claude-md/CLAUDE.md` | loader-group | excluded | var-bound group (`BWr`), file absent on host |
| AGENTS.md | `opencode:instructions/AGENTS.md` | loader-literal | governed | priority list element |
| CLAUDE.md | `opencode:instructions/CLAUDE.md` | loader-literal | governed | gated priority list element |
| CONTEXT.md | `opencode:instructions/CONTEXT.md` | loader-literal | governed | last priority list element |
| AGENTS.md | `opencode:config/AGENTS.md` | loader-config | governed | config join candidate |
| CLAUDE.md | `opencode:claude-home/CLAUDE.md` | loader-config | governed | home join candidate |
| instructions | `opencode:config/instructions` | loader-config | governed | declared list loop |
| https:// | `opencode:config/instructions-remote` | loader-config | governed | remote filter + render |
| <system-reminder> | `opencode:read-hook/instructions` | loader-literal | governed | read-tool channel |
| AGENTS.md | `opencode:instruction-context/AGENTS.md` | loader-literal | governed | second subsystem: ambient all-match walk |

## Method notes

The class id sits in the SECOND cell here. Id-level parity still passes (it
collects backticked ids anywhere in a row), and no other check reads the second
cell — which is exactly the hole this fixture pins: a census may not carry a
declared class id outside the first cell, because then no per-id literal or kind
comparison can be anchored to it.