# swapped-snapshot entry

source: S232/S236/S237
verified-at: 2026-10-25
recheck: 90d

| page | id | rule tokens | quote |
|---|---|---|---|
| best-practices | S232 | "Match the specificity of your instructions to the fragility of the task." `scripts/` | "Match the specificity of your instructions to the fragility of the task." |
| using-scripts | S236 | `uvx ruff@0.8.0 check .` `--dry-run` | "Skills can instruct agents to run shell commands and bundle reusable scripts in a `scripts/` directory." |
| quickstart | S237 | `.agents/skills/` `roll-dice` | "The same skill works in any compatible agent, including Claude Code and OpenAI Codex." |
