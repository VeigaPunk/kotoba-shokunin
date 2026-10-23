Result: DONE — opencode: NOT ELIGIBLE (nested-directory AGENTS.md; no frontmatter key that scopes a rule to matching files)

opencode's own current docs name `AGENTS.md` and load it by directory, not by a glob of files the agent is working on. The only key that takes a `*` pattern, `instructions`, names extra instruction files to load alongside `AGENTS.md`. No candidate token is well-formed and path-scoped. Not marked experimental, preview, or deprecated on these pages.

## Fetched bytes

Scratch: `/fast/scratch/hyaku/kotoba-r60/Censusopencode/`. No tools installed. User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`.

| page | local date -u | HTTP date | status | bytes | sha256 |
|---|---|---|---|---|---|
| https://opencode.ai/docs/rules.md | Fri 23 Oct 2026 10:29:38 AM UTC (`date-rules.txt`) | Fri, 23 Oct 2026 10:29:38 GMT | 200, `text/plain` | 6684 | `dfb242d9a8c0cfb1c97cee74a895b56ba72cba64b558200f06eede4f5f93cb54` |
| https://opencode.ai/v2/docs/instructions.md | same command, 10:29:53Z (`date-v2.txt`) | (body `Not Found`) | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |
| https://opencode.ai/v2/docs/instructions/ with `Accept: text/markdown` | 10:29:53Z; header is the response clock | Fri, 23 Oct 2026 10:29:57 GMT | 200, `text/markdown` | 5618 | `56162c66b6124de0591d8b902f5e0c9dee3ca03a468985aabb64808630f5c957` |
| https://opencode.ai/llms.txt → final https://opencode.ai/v2/llms.txt | 10:29:38Z | (with the rules fetch) | 200 | 4061 | `79fe81b6d690646e875dbbbc696738286f677a47bd2ea39c4318437ed0dfacd0` |

Saved as `rules.md`, `v2-instructions.md` (the 404), `v2-instructions-accept.md`, `llms.txt`. The V1 `.md` URL is byte-identical to the round-53 S045 record (`dfb242d9…`, 6684 B). `sst/opencode` and `anomalyco/opencode` are the same repo (`gh-sst.json` and `gh-anomalyco.json` share sha256 `8da970d61046f16e…`; default branch `dev`).

Pinned docs tree: `dev` commit `2a3e7c0f349ba0e9454fa0529ec041cf57e53cb8`, committer date 2026-10-23T10:15:01Z, message `sync release versions for v2.1.4 [skip ci]`. Tree API `git/trees/dev?recursive=1` HTTP 200, 2,971,864 B, sha256 `7861c52a34202adb04594293a5de502630b40e1f39d76d81495b79e5f9e9b98a`, `truncated: false`, 9534 entries. English docs downloaded at that pin (57/57 HTTP 200; `docs-src/manifest.txt`):

- V1 `packages/web/src/content/docs/rules.mdx` — 6758 B, sha256 `2d789f8467c7018a07b2307d44beb37ef13b10038aed1124aa20098cb4296fd9`
- V2 `services/www/src/docs/content/instructions.mdx` — 5634 B, sha256 `7c767eb7433054c47549b8e28e1d934aee40e1b36fdf09d777a04062c2958895`

The served V1 markdown is the mdx body with the YAML frontmatter and one leading newline removed (6684 vs 6685). The served V2 markdown drops the mdx frontmatter and prepends `# Instructions`. Line numbers below are the served bytes unless marked `mdx`.

## What the pages document

V2 index (`llms.txt:32`) lists Instructions, not a rules-folder page. Scope is which directory the file sits in:

```
sed -n '17p' v2-instructions-accept.md
Place `AGENTS.md` in the directory where its guidance should apply. OpenCode loads the global file followed by every `AGENTS.md` from the current workspace directory toward the home directory. For workspaces outside the home directory, it stops at the project root.
```

```
sed -n '45p' v2-instructions-accept.md
Instruction files below the workspace are discovered as the agent explores the project. Reading a file or listing a directory loads any `AGENTS.md` files between that target and the workspace.
```

V1 still says the same thing as directory scope, and says the global file is not conditional (`rules.md`):

```
sed -n '64p' rules.md
Place an `AGENTS.md` in your project root for project-specific rules. These only apply when you are working in this directory or its sub-directories.
```

```
sed -n '68p' rules.md
You can also have global rules in a `~/.config/opencode/AGENTS.md` file. This gets applied across all opencode sessions.
```

Quote for that global path (10 whitespace-separated words; backticks kept; no bytes stripped). Token and the word `rules` outside the token:

`You can also have global rules in a `~/.config/opencode/AGENTS.md` file.`

Quote for the project file (10 words), from the first sentence of `rules.md:64`:

`Place an `AGENTS.md` in your project root for project-specific rules.`

Action line a cell could cite, and what it actually tells the author to do (put the file in a directory):

```
sed -n '17p' v2-instructions-accept.md
Place `AGENTS.md` in the directory where its guidance should apply. ...
```

```
sed -n '35p' v2-instructions-accept.md
Keep guidance that applies everywhere in the global file. Put repository-wide guidance at the project root and more specific guidance closer to the code it covers. OpenCode combines the files and does not resolve conflicts between them.
```

Migrate page, same pin, `docs-src/v2/migrate-v1.mdx:549-550`: `Existing `AGENTS.md` files stay in place. V2 discovers the global `~/.config/opencode/AGENTS.md` and ambient `AGENTS.md` files from the current directory up to home.`

## Near-miss key `instructions` (not a scope key)

V2 served lines 101 and 106–108 (`sed -n '101p;106,108p'`):

```
Use the `instructions` array to add files, glob patterns, or HTTP(S) URLs alongside discovered `AGENTS.md` files:
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines/*.md",
```

Line 115: `Configured instructions load after `AGENTS.md` files, in the order they are listed.`

Syntactic Scope-key pattern: on line 106, `instructions` is followed by `": [` (quoted key, then `:` then `[`), and line 108 (within the next 3 lines) contains `*`. That pattern matches. The semantic conjunct does not: the globs choose instruction files to load with `AGENTS.md`, not paths of files the agent is working on. None of those entries is a well-formed opencode rule-file token (`CONTRIBUTING.md` is one segment; `docs/guidelines/*.md` is not dot-led; `~/rules/opencode.md` strips to a first segment `rules` that does not start with `.`).

V1 puts another client's folder in the same array (`sed -n '111p' rules.md`):

```
  "instructions": ["CONTRIBUTING.md", "docs/guidelines.md", ".cursor/rules/*.md"]
```

`.cursor/rules/*.md` fails the foreign-name guard (`cursor`). `rules` as a segment word is allowed by this round's rule; the marker is what rejects it. Line 126: `All instruction files are combined with your `AGENTS.md` files.`

## Wrong keys that fail the Scope-key rule

`description` does not occur in served `rules.md` or served V2 instructions. It is only the V1 mdx frontmatter, which the served `.md` drops.

`docs-src/v1/rules.mdx:3` (`sed -n '3p'`):

```
description: Set custom instructions for opencode.
```

Fail: after `:` the value is not a `[`/`|` block, the line has no `*` run, and it has no word `glob`/`globs`/`pattern`/`patterns`.

`docs-src/v2/instructions.mdx:2`:

```
title: "Instructions"
```

Same failure (no `*`, no glob/pattern word).

Served V2 line 105 (`sed -n '105,108p'`):

```
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "CONTRIBUTING.md",
    "docs/guidelines/*.md",
```

`$schema` fails: the value is a quoted URL with no `*`, the next character after `:` is not a block `[` or `|` (it is `"`), and line 105 has no glob/pattern word. `$schema` also fails `^[A-Za-z][A-Za-z0-9_-]*$`.

## Conjuncts (C1 row rule)

Scored on the served bytes. E5 is dropped by the plan; one client, so not tested.

| conjunct | yes/no |
|---|---|
| Own docs on a pinned host (opencode.ai; raw.githubusercontent.com/anomalyco/opencode) | yes |
| Names a rule/instruction file or folder | yes: `AGENTS.md`, `~/.config/opencode/AGENTS.md` |
| Applies only when the agent works on matching files (glob / frontmatter), not merely by sitting in a directory | no |
| Token has ≥ 2 segments after one leading `~/` or `./` | `~/.config/opencode/AGENTS.md` yes (3); bare `AGENTS.md` no |
| First segment starts with `.` | `~/.config/opencode/AGENTS.md` yes (`.config`); `AGENTS.md` no |
| No segment word skill/agent/command/prompt/plugin/extension/hook (`rules` allowed) | no: `AGENTS` equals `agents` |
| E7: no non-final segment has a dot except as its first character | yes for `~/.config/opencode/AGENTS.md` |
| No other client's marker | yes for the AGENTS.md paths; no for the example `.cursor/rules/*.md` |
| Frontmatter key K that names the matching work paths, as a key that takes a path pattern, on one line L | no. `instructions` matches the colon-plus-`*` shape and fails the meaning |
| 6–25 word verbatim quote with the token and rule/instruction outside it | a 10-word quote exists (`rules.md:68`) for a token that is not well-formed |
| A line an Action cell can cite | yes (`v2-instructions-accept.md:17`); it says where to put the file, not how to glob it |
| experimental / preview / deprecated on this feature | no |

## Base counts (item 4)

Commands use `git --no-optional-locks` (read-only). Base `31092dc6f875370bddd6eb1e4da4ca0d210c56af`.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.config/opencode/AGENTS.md' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

`wc -l` = 0. `git grep` itself exited 1 (no file).

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF 'AGENTS.md' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

`wc -l` = 97, git exit 0.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'instructions'
```

12 (exit 0). There is no eligible K. Same command for the failing keys: `description` → 56; `$schema` → 0.

## Q30 sweep (no eligible candidate)

1. Changelog. `https://raw.githubusercontent.com/anomalyco/opencode/2a3e7c0f349ba0e9454fa0529ec041cf57e53cb8/CHANGELOG.md`, command date Fri 23 Oct 2026 10:30:40 AM UTC (`date-docs-tree.txt`), HTTP 200, 55190 B, sha256 `1d7914fd62cb1f12806a2397700a7beebab4575b88d80b41478da3f22dd0ba2a`. Grep for `applyTo`, `globs`, `.opencode/rules`, `frontmatter`: no matches. Closest release note is v2.0.30 (2026-10-15), line 371: `Load local glob patterns and remote URLs configured through `instructions`, and refresh them when configuration changes.` That is the instruction-file list, not a match-the-open-file rule.
2. Current English docs source at the pin above (33 V1 mdx + 24 V2 mdx, all HTTP 200). Grep of `docs-src/` for `applyTo`, `globs:`, and `.opencode/rules`: no hits. `paths:` matched only the prose `OpenCode checks these paths:` in `config.mdx:174`. Permission pages use globs as tool-approval patterns (`v1/permissions.mdx`, `v2/permissions.mdx`), not as rule-file frontmatter. Agent files (`.opencode/agents/`) are a different surface and the segment word `agents` would fail this row.
3. Corpus. `grep -ril -e 'applyTo' -e '.opencode/rules' -e 'path-scoped' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` (10:32:41Z) printed one file: `corpus/knowledge/instruction-surface-remeasure-round13.md`. Its `applyTo` sentence is the github/instructions class (`:47-49`), not opencode. The same file's opencode row (`:25`) is `path/glob/https://` on the `instructions` config. `grep -ril opencode` over that corpus is 79 files; among those, files that also mention `globs` or `applyTo` are the round-13 instruction notes, the round-50/51 skill notes, and `SOURCES.md`. None states an opencode frontmatter key that scopes a rule to matching files. S045 is the always-on rules page already in the corpus.

Confidence: high. Unresolved: non-English copies of the same two pages were not fetched; runtime source outside the docs tree was not audited, and an undocumented code path would not satisfy C1.
