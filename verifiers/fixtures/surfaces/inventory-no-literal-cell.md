# fixture census — instruction surfaces

Preamble prose.

## Class inventory

| class id | kind | verdict | evidence |
|----------|------|---------|----------|
| `omp:gemini/GEMINI.md` | loader-group | governed | loads on session start |
| `omp:cursor/rules` |
| `omp:claude-md/CLAUDE.md` | CLAUDE.md | loader-group | var-bound group (`BWr`), file absent on host |
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

Two distinct `surfaces.literal_parity` failures, both on rows the other checks
accept:

- the `omp:gemini/GEMINI.md` row keeps the pre-round-14 4-column shape, so its
  second cell is `loader-group` where the baseline literal is `GEMINI.md`;
- the `omp:cursor/rules` row carries the id and nothing else — no literal cell at
  all.

Id-level parity, kind parity, literal presence and excluded-reason all stay
green: the ids are present, the literals exist in the dump, and the one excluded
id is listed. (`surfaces.kind_parity` also reads the third cell, so the first row
fails it too — the two failures are named per check, not merged.)