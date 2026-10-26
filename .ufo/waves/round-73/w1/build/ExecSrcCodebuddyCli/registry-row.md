# Draft registry row — CodeBuddy CLI Skills (S217 in the staged package; lane id assigned by the L1)

Fleet 11-column schema, header per `corpus/SOURCES.md:12`. Id placeholder `S<<id>>` until the L1 renumbers
(lane max id today is S216; `assimilation/collisions` records the S203–S216 clash).

| S<<id>> | CodeBuddy Code Skills （技能系统） — Tencent CodeBuddy CLI docs — https://www.codebuddy.ai/docs/zh/cli/skills | docs | B | the CLI skill surface: its two discovery roots, the frontmatter keys the CLI documents, and the project-over-user precedence on a name collision, as one vendor's own page states them | `### 常见问题` at snapshot line 645, its scope-collision answer at lines 659-662, the root list at lines 35-36 and the field table at lines 83-91; quote "- 项目级 Skills 优先级更高 - 使用不同的 name 避免冲突" (8 tokens; the newline between the two adjacent bullets collapsed to one space) | the CLI discovers project skills in `.codebuddy/skills/` and user skills in `~/.codebuddy/skills/`, routes on `description`, and gives a project skill precedence over a user skill of the same name while documenting `disable-model-invocation`, not a bare disable key | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |

Parse check (11 cells → NF 13 under `awk -F'|'`):

$ awk -F'|' '/^\| S<<id>> \|/ {print NF}' registry-row.md
13
