| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S198 | VT Code — SKILLS_GUIDE.md — https://raw.githubusercontent.com/vinhnx/vtcode/main/docs/skills/SKILLS_GUIDE.md | docs | B | VT Code's own documented activation envelope and its untrusted-content posture; one client's implementation, no claim about any other client | the "Activation Context" section; quote "Skill content is untrusted resource data; host tool and sandbox policy remains authoritative." (13 words) | a client that renders an activated skill as bounded untrusted data and subordinates it to the host's own tool and sandbox policy | mined | 2026-10-24 | 90d | corpus/knowledge/client-trust-gates-round68.md |
| S199 | Parallel Works — pw code skills — https://parallelworks.com/docs/ai/code/skills | docs | B | Parallel Works' own two-gate trust model for project skills; one client's implementation, no claim about any other client | the "Trust" section; quote "Project skills are repository-controlled instructions, so they clear two independent gates." (12 words) | a project skill clears a workspace-level grant and a separate per-skill execution grant, and a model invocation can never grant either | mined | 2026-10-24 | 90d | corpus/knowledge/client-trust-gates-round68.md |
| S200 | Kilo Code — Skills — https://kilo.ai/docs/customize/skills | docs | B | Kilo Code's own trusted-location rule for skill-embedded commands; one client's implementation, no claim about any other client | the "Shell commands in skills" section; quote "Project skills (.kilo/skills/ in a repository) and skills fetched from remote URLs never execute commands" (16 words) | commands embedded in a skill body execute only from trusted locations, and a project or remote-URL skill never executes them | mined | 2026-10-24 | 90d | corpus/knowledge/client-trust-gates-round68.md |
| S201 | Microsoft Agent Framework — Agent Skills — https://learn.microsoft.com/en-us/agent-framework/agents/skills | docs | B | Microsoft's own approval default and review guidance for Agent Framework skills; one implementation, and the English upstream of the page the lane holds in Japanese | the "Security best practices" subsection; quote "Agent Skills should be treated like any third-party code you bring into your project." (13 words) | the skill tools require approval by default, and a skill is to be reviewed with the discipline of a third-party dependency | mined | 2026-10-24 | 90d | corpus/knowledge/client-trust-gates-round68.md |
| S202 | Mistral AI Vibe — README — https://raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md | docs | B | Mistral AI Vibe's own skill discovery and trusted-folder model; one client's implementation, no claim about any other client | the "Skill Discovery" section; quote "Standard Agent Skills path (project root, trusted folders only)" (9 words) | a project skill is discovered only inside a trusted folder, so the install path is part of what the skill can do | mined | 2026-10-24 | 90d | corpus/knowledge/client-trust-gates-round68.md |

## Stripped recheck prose (from the staged campaign rows)

- S198 — "re-fetch the raw file and confirm the four-root list and the untrusted-resource-data
  sentence are unchanged (ran 2026-10-24)"
- S199 — "re-fetch the page and confirm the two-gate description and the `/skills trust <name>`
  command are unchanged (ran 2026-10-24)"
- S200 — "re-fetch the page and confirm the trusted-skills-only rule and the approval-prompt
  wording are unchanged (ran 2026-10-24)"
- S201 — "re-fetch the English page and confirm the approval-by-default sentence and the
  untrusted-input instruction are unchanged (ran 2026-10-24)"
- S202 — "re-fetch the raw README and confirm the discovery list and the trusted-folders-only
  annotation are unchanged (ran 2026-10-24)"
