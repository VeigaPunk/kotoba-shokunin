# S255 — located quotes, for the round-72 Gate block

Source: https://agentskills.io/skill.md (host `agentskills.io`, path `/skill.md`).
Snapshot: `.ufo/waves/round-72/snapshots/S255-agent-skills-skill-md.md`, 16 035 B, 234 lines,
sha256 `624f1c7f14a89481823f156aad5b665064a3c595cd9682e73c26f48db88994fc`, opened 2026-10-25
(HTTP 200, `content-type: text/markdown; charset=utf-8`, `last-modified: Sun, 25 Oct 2026 07:31:25 GMT`).

| # | quote (verbatim, ≤25 words) | w | located | section in source | snapshot line | dropped bytes |
|---|---|---|---|---|---|---|
| Q1 | at startup they load only the name and description of each skill (~50-100 tokens per skill) | 16 | yes, byte-exact substring | `## Product summary` | 15 | prefix `Agents load skills through **progressive disclosure**: `; suffix `; when a task matches a skill's description, they load the full \`SKILL.md\` body into context; if the instructions reference supporting files, those load individually as needed.` |
| Q2 | Discovery paths: `.agents/skills/` (cross-client standard), `.<client>/skills/` (client-specific) | 7 | yes, byte-exact substring | `## Product summary` → bold label `**Key files and paths:**` (line 17) | 22 | prefix `- `; suffix `.` |
| Q3 | `name`, `description`, optional `license`, `compatibility`, `metadata`, `allowed-tools` | 7 | yes, byte-exact substring | `## Product summary` → `**Key files and paths:**` | 18 | prefix `- \`SKILL.md\` — Required. Contains YAML frontmatter (`; suffix `) followed by markdown instructions.` |
| Q4 | 1-64 chars, lowercase + numbers + hyphens, no leading/trailing/consecutive hyphens, must match parent directory | 14 | yes, byte-exact substring | `### SKILL.md frontmatter fields` (table row `name`) | 43 | prefix `| \`name\` | Yes | `; suffix ` | Unique skill identifier |` |
| Q5 | Tells agents when to use the skill. Carries the entire burden of triggering. | 13 | yes, byte-exact substring | `### SKILL.md frontmatter fields` (table row `description`) | 44 | prefix `| \`description\` | Yes | 1-1024 chars, non-empty | `; suffix ` |` |
| Q6 | Project-level \| `.agents/skills/` \| Highest (overrides user-level) | 7 | yes (table row, verbatim cells) | `### Skill activation paths (discovery)` | 80 | none within the row; the row is the whole line |

Note for any counter that checks these word-bounded: Q1 ends with `)`, so a `\b…\b` test
returns 0 matches; `(?<!\w)…(?!\w)` returns 1. Q6 is a table row, not a sentence.
