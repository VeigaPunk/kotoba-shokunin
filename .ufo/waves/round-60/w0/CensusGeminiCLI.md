Result: DONE — Gemini CLI: NOT ELIGIBLE (nested-directory GEMINI.md / JIT context; no path-pattern frontmatter key)

Gemini CLI's own docs name context files (`GEMINI.md` by default) and scope them by directory: a global file, workspace/ancestor files, and just-in-time files discovered when a tool touches a directory. No page names a rule file whose frontmatter key takes a path pattern (`globs` / `paths` / `applyTo`). Not marked experimental, preview, or deprecated on the context page. No tools installed.

## Pages opened

User-Agent on every fetch: `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36`.

| What | URL | date -u (this seat) | HTTP | bytes | sha256 | saved |
|---|---|---|---|---|---|---|
| Context page (cited) | https://geminicli.com/docs/cli/gemini-md.md | `Fri 23 Oct 2026 10:30:23 AM UTC` (response `date: Fri, 23 Oct 2026 10:30:23 GMT`, `last-modified: Fri, 16 Oct 2026 02:36:07 GMT`, `content-type: text/markdown; charset=utf-8`) | 200 | 3816 | `e5fbfd6d580643a300b5ee0e622d9e2d8f97d4d23460e6b08e1c656251c2f2c2` | `/fast/scratch/hyaku/kotoba-r60/CensusGeminiCLI/gemini-md.md.body` |
| Docs index | https://geminicli.com/docs.md | `Fri 23 Oct 2026 10:29:29 AM UTC` | 200 | 5934 | (not the cited page) | `.../geminicli.com_docs.md` |
| llms export | https://geminicli.com/llms.txt | same batch | 200 | 968590 | (search aid) | `.../geminicli.com_llms.txt` |
| Release notes | https://geminicli.com/docs/changelogs.md | `Fri 23 Oct 2026 10:29:47 AM UTC` | 200 | 69617 | `e8fb2a25f450de8ed4cc1db23c0c48d269853cd05b375399e7a4e47d834f423a` | `.../geminicli.com_docs_changelogs.md` |
| Stable notes | https://geminicli.com/docs/changelogs/latest.md | same batch | 200 | 4140 | `f38215087f7adabbd9d52831ceeb1def13bc98eb4b62181c518f295e399dd68f` | `.../geminicli.com_docs_changelogs_latest.md` |
| Preview notes | https://geminicli.com/docs/changelogs/preview.md | `Fri 23 Oct 2026 10:30:23 AM UTC` | 200 | 6038 | `c186463197c0cb2d65eece11cc0b69a567d7a2b4967443447cf8488b40d06593` | `.../changelogs-preview.md` |

Docs source tree: `git clone --depth 1 --filter=blob:none --sparse` of `https://github.com/google-gemini/gemini-cli.git` into `/fast/scratch/hyaku/kotoba-r60/CensusGeminiCLI/gemini-cli-docs`, then `sparse-checkout set docs`. HEAD `a713410aba5d594594e20d5c822e3aab8f822089` (2026-10-22 22:14:36 +0000). 96 readable `.md`/`.mdx` files. `docs/CONTRIBUTING.md` is a symlink to `../CONTRIBUTING.md` (outside the sparse set); that file was fetched separately at the same commit (below).

Served `gemini-md.md` vs `docs/cli/gemini-md.md` at that commit: not byte-identical (source sha256 `d00eeaef22453de4756a9862d8467750f772e239c4ee9b6f755709429b47c2cf`). `diff -u` shows only link rewriting (`../reference/memport.md` → `/docs/reference/memport`, and three "Next steps" links) plus a missing final newline on the served body. Lines 1–87 and 94–108, including the hierarchy and `fileName` example, are the same text.

## Mechanism the page documents

`sed -n '30,35p' /fast/scratch/hyaku/kotoba-r60/CensusGeminiCLI/gemini-md.md.body`:

```
3.  **Just-in-time (JIT) context files:**
    - **Location:** When a tool accesses a file or directory, the CLI
      automatically scans for `GEMINI.md` files in that directory and its
      ancestors up to a trusted root.
    - **Scope:** Lets the model discover highly specific instructions for
      particular components only when they are needed.
```

That is directory nesting, not a frontmatter glob. The filename printed for the scan is `` `GEMINI.md` `` (one segment, not dot-led). The global file is a different, always-on path. `sed -n '20,21p'` of the same body:

```
    - **Location:** `~/.gemini/GEMINI.md` (in your user home directory).
    - **Scope:** Provides default instructions for all your projects.
```

Whitespace-separated words across those two lines: 17 (`-` `**Location:**` `` `~/.gemini/GEMINI.md` `` `(in` `your` `user` `home` `directory).` `-` `**Scope:**` `Provides` `default` `instructions` `for` `all` `your` `projects.`). The token and `instructions` are both present, and 17 is inside 6–25, but the sentence is "for all your projects", not "only when the agent works on matching files". No bytes were stripped.

Feature status on this page: `experimental` 0, `preview` 0, `deprecated` 0.

## Nearest path, scored against every C1 conjunct

Token as printed: `` `~/.gemini/GEMINI.md` `` (line 20). Normalised after one `~/`: `.gemini/GEMINI.md`. There is no eligible token. The JIT name `` `GEMINI.md` `` is scored in the same table.

| Conjunct | `~/.gemini/GEMINI.md` | bare `GEMINI.md` (JIT / project) |
|---|---|---|
| Own documentation | yes — title "Provide context with GEMINI.md files" | yes — same page, lines 31–33 |
| Pinned host, not changelog/release/news/blog/tracker | yes — `geminicli.com` | yes |
| Instruction file | yes — "default instructions" (line 21) | yes — "specific instructions" (line 34) |
| Applies only when the agent works on matching files | no — "for all your projects" (line 21) | no as a path-pattern rule — the page scans a directory and its ancestors when a tool accesses that directory (lines 31–33). No glob, no frontmatter |
| `TOKEN_RE` `^(~/|\./)?[A-Za-z0-9_.-]+(/[A-Za-z0-9_.*-]+)*/?$` | yes | yes (one segment) |
| After one leading `~/` or `./`, ≥ 2 segments | yes — `.gemini`, `GEMINI.md` | no — one segment |
| First segment starts with `.` | yes — `.gemini` | no — `GEMINI.md` |
| No segment word in {skill(s), agent(s), command(s), prompt(s), plugin(s), extension(s), hook(s)} (`rule(s)` / `instructions` allowed) | yes — words `gemini`; `GEMINI`, `md` | yes — `GEMINI`, `md` |
| E7 (dot in a non-final segment only as its first character) | yes | yes (single segment) |
| No other client's marker | yes — contains `gemini`, this client's own marker | yes |
| Scope key K on one line L: K then `:`/`=` (optional closing quote) or a backticked table cell, AND a `*` path-pattern on L or the next 3 lines when the value is only spaces/`[`/`|`, OR `glob`/`globs`/`pattern`/`patterns` on L outside K | no — see below | no |
| 6–25-word verbatim quote with the token and `rule(s)`/`instruction(s)` outside the token | the two-line span above is 17 words and has both, but it does not say the file is path-scoped | lines 34–35 have `instructions` and no path token; lines 31–33 have `` `GEMINI.md` `` and no `rule`/`instruction` word |
| Not experimental/preview/deprecated | yes (those words are absent) | yes |

Scope-key failure on this page. `sed -n '98p;105,108p'` of the fetched body:

```
`context.fileName` property.
    "fileName": ["AGENTS.md", "CONTEXT.md", "GEMINI.md"]
  }
}
```

- Line 98's backticked span is `context.fileName`, which fails `^[A-Za-z][A-Za-z0-9_-]*$` (embedded `.`). The line has no `*`.
- Line 105: `fileName` is at an identifier boundary, then `":` (closing `"` then `:`). The value `["AGENTS.md", "CONTEXT.md", "GEMINI.md"]` has no `*`. The next 3 lines are `  }`, `}`, and the closing fence — no `*`. Line 105 has no word `glob`/`globs`/`pattern`/`patterns` outside `fileName`.
- `description` does not occur on this page. The careless key here is `fileName` (the settings key that names the context filename, not the paths a rule applies to).

No Action line tells a rule author to attach a path pattern. The nearest author instruction is lines 8–9: "Instead of repeating instructions in every prompt, you can define them once in a context file." That is "write a context file", not "scope it to matching files".

## Other printed keys that are not this row

- `.geminiignore` (`docs/cli/gemini-ignore.md` line 23 at `a713410`: "Standard glob patterns are supported (such as `*`, `?`, and `[]`)."). An ignore file, not an instruction file. Token `.geminiignore` is one segment.
- Policy `argsPattern` (`docs/reference/policy-engine.md` line 310: `argsPattern = '"command":"(git|npm)'`). A regex over tool-call arguments, not a path glob on an instruction file. Line 310 has no `*`. The word `pattern` sits inside `argsPattern`, so it is not outside K. The key fails the Scope-key rule on that line.
- Skill frontmatter (`docs/cli/creating-skills.md` lines 151–154) is `name` and `description` only ("This is how Gemini decides when to use the skill"). `description` is not a path pattern. The folder `.gemini/skills/` also contains the banned segment word `skills`.
- Subagent frontmatter (`docs/core/subagents.md` lines 334–343) keys are `name`, `description`, `kind`, `tools`, `model`, `temperature`, `max_turns`. `tools` allows a tool-name wildcard `*` on the schema line (line 367), not a file-path pattern for when a rule loads. The path `.gemini/agents/*.md` (line 323) contains the banned segment word `agents`.

Docs-tree search at `a713410` (96 readable markdown files): `.gemini/rules` 0, `applyTo` 0, `globs:` 0. `CONTRIBUTING.md` at the same commit (HTTP 200, 20400 bytes, sha256 `b9cd98e07df3d36b…`, saved `.../CONTRIBUTING.md`) has the same three counts at 0. Its only `GEMINI.md` hit is lines 352–353: "typically found in the project root" for project conventions — still the one-segment name.

## Q30 sweep (no path-scoped rule file is documented)

1. Changelog / release notes. Served `https://geminicli.com/docs/changelogs.md` (69617 bytes, sha above) counts: `applyTo` 0, `glob` 0, `frontmatter` 0, `rule` 0, `.gemini/rules` 0. The only context-scoping announcements are directory discovery, not a frontmatter key. Lines from that body:

```
361:- **Subagent Context and Feedback:** Enhanced subagents with JIT context
385:- **JIT Context Discovery:** Implemented Just-In-Time context discovery for file
```

(line 385 continues "system tools…" on the next line; v0.35.0, 2026-03-24). Source `docs/changelogs/index.md` at `a713410` (70570 bytes, sha256 `cdc7744aec682e441d8ffb55e71eb49067060d7d9fc799370f3d79f123ec6b32`) counts: `.gemini/rules` 0, `applyTo` 0, `globs` 0, `frontmatter` 0, `path-scoped` 0, `GEMINI.md` 0. Preview and stable notes were fetched (sizes above) and are the short channel pages the index links. The index points at `https://github.com/google-gemini/gemini-cli/releases` for the full changelog; those release pages were not fetched one by one. The in-repo announcement log is the changelog this seat opened.

2. Current docs source tree. The clone above. Negative counts in the previous paragraph. `docs/cli/` has `gemini-md.md` and no `rules.md`. GitHub code search (`api.github.com/search/code`) returned HTTP 401 "Requires authentication", so the implementation tree was not grepped. [INFERENCE] an undocumented loader would still not be a documented C1 candidate. The published docs and the docs tree do not name one.

3. Lane corpus. `grep -ril -- '.gemini/rules' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus` → exit 1, no file. `grep -ril 'applyTo' .../corpus` → exit 0, one file: `corpus/knowledge/instruction-surface-remeasure-round13.md` line 48, about `*.instructions.md` `applyTo` (the github/instructions class), not a Gemini CLI key.

All three legs ran. Verdict stands: NOT ELIGIBLE.

## Base pre-count (the printed global path, not an eligible row)

Token with no leading `~/` or `./` and no trailing `/`: `.gemini/GEMINI.md`. Key that fails the Scope-key rule: `fileName`.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin grep -ilF '.gemini/GEMINI.md' 31092dc6f875370bddd6eb1e4da4ca0d210c56af -- . ':!.ufo' | wc -l
```

Output: `1` (pipeline exit 0). The one file, from the unpiped `git grep -nF` (exit 0):

```
31092dc6f875370bddd6eb1e4da4ca0d210c56af:corpus/knowledge/instruction-surface-census-round13.md:147:  `cwd/.gemini/GEMINI.md` only, with no walk-up.
```

That is a substring hit on `cwd/.gemini/GEMINI.md` in an old census note, not a SKILL.md row.

```
git --no-optional-locks -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 31092dc6f875370bddd6eb1e4da4ca0d210c56af:SKILL.md | grep -cF 'fileName'
```

Output: `0` (grep exit 1, no match). `--no-optional-locks` is the only addition to the assigned commands.

## Fetch notes

Markdown variants were used (`text/markdown`). No headless browser. No lane git or jj writes. Scratch clone of the upstream docs repo is under `/fast/scratch/hyaku/kotoba-r60/CensusGeminiCLI/` only. No sandbox commit.
