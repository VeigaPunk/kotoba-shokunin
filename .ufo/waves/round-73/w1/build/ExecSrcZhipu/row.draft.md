# Draft registry row — C1 / Zhipu (id placeholder, L1 renumbers)

Byte-identical row for `corpus/SOURCES.md` (§ Registry, 11 columns). `S<<id>>` is a placeholder:
`scripts/sources-census.sh validate` will report E02 until the L1 substitutes an `S[0-9]{3,}` id.

| S<<id>> | 智谱 AI 开放文档 — Managed Agents — Agent Skills — https://docs.bigmodel.cn/cn/managed-agents/skills.md | docs | B | Zhipu's managed-agents skill surface: how a cloud Skill is packaged, uploaded, versioned and mounted per Agent, and how built-in and custom skills are selected (one vendor's product documentation; no local harness is measured) | `# Agent Skills` (snapshot.md:7), `## 选择内置或自定义 Skill` (snapshot.md:25-28, mount `type` table :79), `## 挂载到 Agent` (runtime dir snapshot.md:83); fetched as https://docs.bigmodel.cn/cn/managed-agents/skills.md (200, 7381 B, sha256 `b20e45c7ff0bb09bd0164e5148162a9cda8e9ccd8f5140c8bb1578fb24961618`, text/markdown, 0 redirects, refetch byte-identical) on 2026-10-25; quote "先读名称与描述，再按任务读取正文和配套资料" (21 chars; dropped: the preceding "Agent " and the trailing "，不必每次把整套方法塞进 system prompt。") | a cloud skill is an uploaded, versioned package of SKILL.md plus templates and scripts whose name and non-empty description are read first while the body loads per task from `/workspace/skills/<目录名>/`; `type:zai` is a built-in skill listed by `GET /v1/skills?source=zai` and `type:custom` an uploaded one; the page names no project or user filesystem root | mined | 2026-10-25 | 90d | corpus/knowledge/chinese-vendor-skill-surfaces-round73.md |

## Schema check (run in this directory)

```
$ awk -F'|' '/^\| S<<id>> \|/{printf "NF=%d cells=%d\n", NF, NF-2}' row.draft.md
NF=13 cells=11
$ grep -c '|' row.draft.md        # the row line has 12 pipes and no pipe inside a cell
```
