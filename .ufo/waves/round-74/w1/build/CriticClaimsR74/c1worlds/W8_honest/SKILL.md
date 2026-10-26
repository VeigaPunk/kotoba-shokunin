# world SKILL

### Body craft — the specification's skill-creation guides

| page | id | action |
|---|---|---|
| best-practices | S232 | Fragile steps get the exact verbatim command; every other step gets the goal and the reason: "Match the specificity of your instructions to the fragility of the task." |
| using-scripts | S236 | Run a packaged linter with `uvx ruff@0.8.0 check .` when the repository already has one instead of bundling a second copy. |
| quickstart | S237 | Put the skill under `.agents/skills/` so a VS Code session discovers it without configuration. |
| best-practices | S232 | Offer one default and one named escape hatch; a menu of equal options is a decision the author never made: "Match the specificity of your instructions to the fragility of the task." |
| using-scripts | S236 | Give destructive scripts a `--dry-run` flag so the agent can preview the change before it runs. |
| quickstart | S237 | Name the example directory `roll-dice` and copy its shape for your first skill before adding rules. |
