# fixture census — instruction surfaces

Preamble prose.

## Class inventory

| class_id | literal | kind | verdict | evidence |
|----------|---------|------|---------|----------|
| GEMINI.md | `omp:gemini/GEMINI.md` | loader-group | governed | loads on session start |
| CLAUDE.md | `omp:claude-md/CLAUDE.md` | loader-group | excluded | var-bound group (`BWr`), file absent on host |
| rules | `omp:cursor/rules` | loader-literal | governed | directory-of-files registration |
| AGENTS.md | `opencode:project/AGENTS.md` | loader-literal | governed | all-match walk-up source |
| AGENTS.md | `opencode:config/AGENTS.md` | loader-config | governed | global config candidate |
| AGENTS.md | `opencode:read-hook/AGENTS.md` | loader-literal | governed | read-tool channel |
| instructions | `opencode:api-entries/instructions` | loader-config | governed | API-managed entries |
| instructions | `opencode:config/instructions` | loader-config | excluded | schema-declared, consumer unproven |

## Method notes

Prose mentioning `omp:gemini/GEMINI.md` outside a table row — must NOT count.
