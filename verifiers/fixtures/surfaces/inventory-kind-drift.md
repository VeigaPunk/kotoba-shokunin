# fixture census — instruction surfaces

Preamble prose.

## Class inventory

| class_id | literal | kind | verdict | evidence |
|----------|---------|------|---------|----------|
| `omp:gemini/GEMINI.md` | GEMINI.md | loader-literal | governed | loads on session start |
| `omp:claude-md/CLAUDE.md` | CLAUDE.md | loader-group | excluded | var-bound group (`BWr`), file absent on host |
| `omp:cursor/rules` | rules | loader-literal | governed | directory-of-files registration |
| `opencode:instructions/AGENTS.md` | AGENTS.md | loader-literal | governed | priority list element |
| `opencode:instructions/CLAUDE.md` | CLAUDE.md | loader-literal | governed | gated priority list element |
| `opencode:instructions/CONTEXT.md` | CONTEXT.md | loader-literal | governed | last priority list element |
| `opencode:config/AGENTS.md` | AGENTS.md | loader-config | governed | config join candidate |
| `opencode:claude-home/CLAUDE.md` | CLAUDE.md | loader-config | governed | home join candidate |
| `opencode:config/instructions` | instructions | loader-config | governed | declared list loop |
| `opencode:config/instructions-remote` | https:// | loader-config | governed | remote filter + render |
| `opencode:read-hook/instructions` | <system-reminder> | loader-literal | governed | read-tool channel |
| `opencode:instruction-context/AGENTS.md` | AGENTS.md | loader-literal | governed | second subsystem: ambient all-match walk + ungated config candidate |

## Method notes

The `omp:gemini/GEMINI.md` row states `loader-literal` where `baseline-clean.json`
declares `loader-group` — a *legitimate* kind value, so only a per-id kind
comparison can catch it. Literal parity, id parity and literal presence all stay
green here.