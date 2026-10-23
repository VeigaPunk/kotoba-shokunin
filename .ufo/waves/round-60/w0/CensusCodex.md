Result: DONE — Codex: NOT ELIGIBLE (nested-directory instruction files; no path-pattern frontmatter key)

Codex's own docs name instruction files (AGENTS.md, AGENTS.override.md, fallback filenames) that load by walking directories, and a separate experimental .rules execpolicy that matches command prefixes. Neither is a rule file that applies only when the agent works on matching files, and no page shows a frontmatter key that takes a path pattern.

## Fetches

Browser UA Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36. Bytes under /fast/scratch/hyaku/kotoba-r60/CensusCodex/. No tools installed.

| file | URL (final) | date -u | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| agents-md.body | https://learn.chatgpt.com/docs/agent-configuration/agents-md.md | Fri 23 Oct 2026 10:30:00 AM UTC | 200 text/markdown | 9149 | 9d1f87a2d1cb55b4782b95abe710692b35b9659789c2db31a22c7074a3383e8e |
| rules.body | https://learn.chatgpt.com/docs/agent-configuration/rules.md | same | 200 text/markdown | 6783 | 4ecdfe26ece03895220808a7aa4f05c91d837492300262baf5a5df35c3f44ce7 |
| llms.body | https://learn.chatgpt.com/docs/llms.txt | same | 200 | 33447 | fc7b20eaea56f8fe5dcc0280262009f9546172c521f69cb08b8befc89f03b943 |
| llms-full.body | https://learn.chatgpt.com/docs/llms-full.txt | Fri 23 Oct 2026 10:30:21 AM UTC | 200 | 2550095 | efc3a0f74d5e2b8d86308716b45bb2fd52abb2f1b816d0a1c88031b87f839bff |
| gh-changelog.body | https://raw.githubusercontent.com/openai/codex/main/CHANGELOG.md | same | 200 | 330 | c8458f99de91a4b4b9682ecb72c396f0d08c03c51a657759e1239c3a14c697d5 |
| gh-releases.body | https://api.github.com/repos/openai/codex/releases?per_page=5 | same | 200 | 3353574 | 998220d7015053ed2f5970e0b95cd7570a3adaa864b7be0a685e064329cc67bc |
| gh-docs-tree.body | https://api.github.com/repos/openai/codex/git/trees/main?recursive=1 | Fri 23 Oct 2026 10:30:36 AM UTC | 200 | 3353348 | 9a533a991689e6b48c20432e13317d54d65f6024552f070af094f0b821710959 |
| agents_md.raw.md | https://raw.githubusercontent.com/openai/codex/main/docs/agents_md.md | Fri 23 Oct 2026 10:30:52 AM UTC | 200 | 126 | 56f5b6026b15fad40fe8b1f6f8910b9fccdf66da3b39dd943c91877e2299619e |
| execpolicy.raw.md | https://raw.githubusercontent.com/openai/codex/main/docs/execpolicy.md | same | 200 | 138 | 76b29e8cffcfab00c706e9bbd443e4f4b8c53288968b434e5990af1766132450 |
| config.raw.md | https://raw.githubusercontent.com/openai/codex/main/docs/config.md | same | 200 | 726 | 745768b4da6cd73e414fc49c5c6ef3d6bf8a0c08289fab23a7dd79776ab31d9d |

Redirects (Fri 23 Oct 2026 10:31:19 AM UTC): https://developers.openai.com/codex/guides/agents-md returns 308 to https://learn.chatgpt.com/docs/agent-configuration/agents-md (200 HTML). https://developers.openai.com/codex/exec-policy returns 308 to https://learn.chatgpt.com/docs/agent-configuration/rules (200 HTML). The .md twins above are the pages scored. agents-md.body sha256 matches the S044 pin from 2026-10-22 (9d1f87a2…, 9149 B). GitHub code search returned 401 (120 B); the docs tree was listed from the git trees API instead.

llms.txt Agent Configuration entries (llms.body:19-20): custom instructions = AGENTS.md; Rules = "Control which commands Codex can run outside the sandbox".

## What it documents instead

Directory walk, not file globs. sed -n '12p' agents-md.body:

```
2. **Project scope:** Starting at the project root (typically the Git root), Codex walks down to your current working directory. If Codex cannot find a project root, it only checks the current directory. In each directory along the path, it checks for `AGENTS.override.md`, then `AGENTS.md`, then any fallback names in `project_doc_fallback_filenames`. Codex includes at most one file per directory.
```

sed -n '64p' agents-md.body (11 words; the author action):

```
2. Add overrides in nested directories when specific teams need different rules. For example, inside `services/payments/` create `AGENTS.override.md`:
```

sed -n '83p' agents-md.body:

```
Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible.
```

No frontmatter on this page. Fallback names are a filename list in config.toml (agents-md.body:151-159), not a path-pattern key.

## Rejected candidate A — ~/.codex/rules/ (command execpolicy)

Printed token on rules.body:15 and :46: ~/.codex/rules/default.rules, folder ~/.codex/rules/, project-local repo/.codex/rules/. Marked experimental: sed -n '7p' rules.body is `Rules are experimental and may change.`

Quote (sed -n '5p', 12 words, contains rules, no markdown stripped):

```
Use rules to control which commands Codex can run outside the sandbox.
```

That quote does not contain the path token. Token-bearing line (sed -n '15p', 17 words) is about command allowlisting, and every rules on it sits inside a path span (.rules, rules/, or ~/.codex/rules/default.rules):

```
1. Create a `.rules` file under a `rules/` folder next to an active config layer (for example, `~/.codex/rules/default.rules`).
```

sed -n '22,25p' rules.body (the only pattern assignment):

```
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",
```

sed -n '61p' rules.body:

```
- `pattern` **(required)**: A non-empty list that defines the command prefix to match. Each element is either:
```

Conjuncts for ~/.codex/rules/:

- own docs, pinned host: yes (learn.chatgpt.com, 200)
- file/folder for a rule (instruction) file that applies only when the agent works on matching files: no. Execpolicy for commands outside the sandbox (rules.body:5). Line 13 says ".rules instructions apply to Codex" meaning the product, not file-scoped guidance. Match target is a command prefix (rules.body:61).
- path token at least 2 segments, first starts with `.`: yes (.codex / rules after stripping ~/)
- no banned segment word: yes (C1 allows rules; codex is this client's own marker)
- E7: yes (no extra dot in a non-final segment)
- no other client's marker: yes
- key K takes a path pattern on one line L: no (below)
- 6-25 word quote with the token and rule/instruction outside the token: no (line 5 has rules but not the token; line 15 has the token but every rules is inside a path span)
- Action line a cell could cite for file scope: no (line 15 says create a command rule; line 44 says Restart Codex.)

Scope-key on L=22, K=pattern: pattern is followed by ` =`, so the key shape is present, but the value ["gh", "pr", "view"] has no star run, the block exception wants a colon not `=`, and the only word pattern on the line is K itself. Lines 23-25 have no glob. L=61 is a backticked name, not a backticked table cell, and after the closing backtick comes space and bold markers, not a colon or equals.

Wrong key decision (sed -n '25p'): `       decision = "prompt",` — equals is present, the value has no star, and the line has neither glob/globs nor pattern/patterns. Fails the Scope-key rule.

## Rejected candidate B — AGENTS.md / AGENTS.override.md

- names an instruction file: yes (agents-md.body:5, :12)
- applies only for matching files: no. One file per directory on the walk from the project root to the cwd (:12, :83)
- path token grammar: no. AGENTS.md is one segment and does not start with a dot. ~/.codex/AGENTS.md and AGENTS.override.md split to the banned word agents
- frontmatter key K with a path pattern: no frontmatter on the page
- experimental/preview/deprecated: not marked

## Not instruction-file scope (seen, not scored as candidates)

- Skills: SKILL.md frontmatter is name and description (llms-full.body:7816, :7852-7856); implicit invoke matches description (:7827-7828). Paths .agents/skills and /etc/codex/skills (:7867, :7875) contain the banned word skills. No globs / applyTo.
- Sandbox deny-read globs (permissions filesystem glob_scan_max_depth, llms-full.body:14518-14533 and :38053) gate filesystem reads, not which instruction file loads.
- Full-docs search of llms-full.body for applyTo, apply_to, frontmatter, and "globs:" returned no instruction-file hit. glob hits are network wildcards, deny-read globs, or the substring of global.

## Q30 sweep (all three legs)

1. Changelog / release notes. CHANGELOG.md on main is a pointer to the releases page plus one unreleased exec fix (gh-changelog.body, 3 lines). Latest release rust-v0.164.0 published 2026-10-23T04:48:10Z, body 27771 B saved as release-v0.164.0.body. Counts: AGENTS 3, applyTo 0, frontmatter 0, .rules 0, execpolicy 0. The one glob hit is the substring of global. No path-scoped instruction file.
2. Current docs source tree. openai/codex docs/*.md is 15 files (docs/agents_md.md, docs/execpolicy.md, docs/config.md, docs/skills.md, and the rest listed from gh-docs-tree.body). The three fetched stubs only redirect to developers.openai.com/codex/..., which 308 to the learn.chatgpt.com pages scored above. The live docs export is llms-full.body.
3. Lane corpus. Command grep -ril -E 'codex.*(glob|applyTo|rules/)|AGENTS\.override|\.codex/rules' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus exit 0, five files, all prior always-on AGENTS.md census (S044 / round 53), not a glob key. grep -rilF '.codex/rules' on that corpus exit 1 (no hits). grep -rilF applyTo hits only corpus/knowledge/instruction-surface-remeasure-round13.md (VS Code / Copilot instructions files, not Codex).

## Base counts (step 4, nearest strings)

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.codex/rules' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

git grep exit 1, wc printed 0.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'pattern'
```

printed 5 (lines 130, 272, 418, 421, 427: hook-folder wording, bailian-cli, anti-patterns — not a Codex scope key). grep -cF applyTo printed 0. grep -cF globs printed 0. grep -cF '.codex/rules' printed 0. grep -cF 'AGENTS.md' printed 11.

[INFERENCE] Codex has no C1-eligible client: the instruction mechanism is nested directory files, which the census item names as the not-eligible case, and the only pattern key on the rules page matches command argv prefixes.
