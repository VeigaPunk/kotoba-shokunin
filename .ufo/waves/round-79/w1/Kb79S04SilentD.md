# C2 negative-sweep results — Junie, Hermes, Goose

All page captures below were fetched directly on 2026-10-27 using `curl -sSL -A 'Mozilla/5.0'`; page SHA-256 is over the exact response body including the appended HTTP marker only where noted. Direct page fetch summaries:

| client | page SHA-256 | sweep 1 | sweep 2 | sweep 3 | sweep 4 | verdict |
|---|---|---|---|---|---|---|
| JetBrains Junie | `7ee69d5edf2e41b0b4f277489035a511ba854143269c9752462fcda2c4713808` | HTTP 200, 38,524 B; `allowed[-_ ]tools`/`allowedTools` absent raw and tag-stripped | JetBrains IDEA releases category page searched (2026-10-27 fetch; no hit); Junie page itself inspected; no date-bounded per-client changelog located | Docs/source probes: `.md` variant HTTP 404; `https://github.com/JetBrains/junie` (337,623 B) no hit; GitHub code-search API for `allowed-tools repo:JetBrains/junie` HTTP 401 (auth required) | Required corpus/SKILL grep below; no Junie hit | not checked (sweep 3 incomplete: authenticated code search unavailable and source tree not established) |
| Hermes Agent | `d9f3364a1bb3510736ed585606783ed67bb55b00f2627193b668fc0ae0d5b123` | HTTP 200, 206,646 B; both spellings absent raw and tag-stripped | GitHub releases API `https://api.github.com/repos/NousResearch/hermes-agent/releases?per_page=20` fetched 2026-10-27 (398,923 B), 0 `allowed-tools` hits; covers latest 20 releases, dates not fully validated | `.md` URL HTTP 404; `https://github.com/NousResearch/hermes-agent/tree/main/docs` (232,488 B) no hit; code-search API `allowed-tools repo:NousResearch/hermes-agent` HTTP 401 | Required corpus/SKILL grep below; no Hermes hit | not checked (sweep 3 incomplete: code search auth-blocked, docs tree listing page alone does not establish source-tree-wide absence) |
| Goose | `0059621f1125c8418f65ec0aec7327add1657f4581b68805c0a9717464d38c7c` | Current page `https://goose-docs.ai/docs/guides/context-engineering/using-skills/`: HTTP 200, 87,438 B; both spellings absent raw and tag-stripped. Former guessed `block.github.io/goose/docs/guides/skills/` was HTTP 404. | GitHub releases API `https://api.github.com/repos/block/goose/releases?per_page=20` fetched 2026-10-27 (1,388,400 B), zero `allowed-tools` hits; latest 20 releases, date range not individually validated | Markdown/raw source `https://goose-docs.ai/docs/guides/context-engineering/using-skills.md` HTTP 200, 8,955 B, no hits; repo source `https://raw.githubusercontent.com/block/goose/main/documentation/docs/guides/context-engineering/using-skills.md` HTTP 200, 9,197 B, no hits; docs source-tree listing `https://github.com/block/goose/tree/main/documentation/docs/guides/context-engineering` fetched (246,901 B), no hit | Required corpus/SKILL grep below; no Goose hit | not checked (sweep 3 incomplete: fetched source file and listing, not a recursive source-tree search) |

Sweep 4 command, exactly as required:

```sh
grep -rniE 'allowed-tools|allowed_tools' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus /home/vgpnk/Projects/shokunin/kotoba-shokunin/SKILL.md | head
```

Exit status: 0. Output contained existing `frontmatter-rule-authorities-round48.md`, `chinese-vendor-skill-surfaces-round73.md`, round-73 lesson, and `SOURCES.md` references; none named Junie, Hermes, or Goose. Thus no claim of `silent (sweeps 1-4 all empty)` is made: each remains `not checked` because sweep 3 could not establish comprehensive source-tree absence. No page states the field; no S232+ row recommended.

VERDICT: No `allowed-tools` evidence found in the fetched pages; all three clients remain not checked because source-tree sweeps were incomplete.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79S04SilentD.md
