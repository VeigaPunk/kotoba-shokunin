Result: DONE — opencode documents a user-typed `@skill-id` form for explicitly loading a named skill, and the requested self-test passed.

## Finding and behavior

The V2 skills documentation explicitly says a user can load a skill by mentioning `@skill-id` in their prompt. The same page documents the model-side tool call as `skill` with the skill's exact ID (`services/www/src/docs/content/skills.mdx:186-201`). The proposed decision-table form is `@skill-id`, because it is the direct user-typed prompt form and matches the frozen counter's token rule. The model tool name itself is `skill`; the example tool input uses an `id` field.

The current served V1 `.md` page also documents `opencode/slash: "true"` to expose a skill as a `/name` command in the TUI (`opencode-skills.md:44`), and shows the tool call `skill({ name: "git-release" })` (`:122-126`). Those pages are already represented in SOURCES rows S059 and S064, so the proposed new row uses the uncited, pinned V2 docs source file instead.

V2 also documents a way to keep a skill explicitly loadable while removing it from the model-facing available list. Exact quote (23 words; line 142, retaining inline Markdown code formatting): “`opencode/autoinvoke: false` only hides the skill from the model's available list. The skill remains registered and can still be loaded explicitly by ID.”

## Draft C1 rows

1. Quote for the entry (12 words; source line 201; the inline Markdown code delimiters around the token are stripped, as they are by the counter's page normalization): “To load a skill yourself, mention it in your prompt as @skill-id.” The same sentence is on the fetched live V2 page at HTML line 289 (inline HTML tags stripped).

2. Draft SOURCES row (11 cells):

| S0NN | anomalyco/opencode — V2 Agent skills documentation source, pinned at `3d213123cdf574e55f88711554edfe6fd66a95ad` — https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx | docs | A | opencode V2's documented user-directed explicit skill loading | § Loading (`skills.mdx:201`); § Frontmatter (`:142`); fetched 2026-10-22T23:12:55Z (HTTP 200, 9,187 B, sha256 `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b`) | V2 says users can load a skill by mentioning @skill-id in their prompt | mined | 2026-10-22 | on-release | corpus/knowledge/explicit-invocation-round55.md |

3. Draft entry row (`client | row | quote | location | reading`):

| opencode | S0NN | "To load a skill yourself, mention it in your prompt as @skill-id." | § Loading (`skills.mdx:201`; inline Markdown code delimiters stripped) | User mentions @skill-id in the prompt to load the named skill. |

4. Draft SKILL.md row (`Client | Explicit form | What it does | Action`):

| Client | Explicit form | What it does | Action |
|---|---|---|---|
| opencode | `@skill-id` | The user mentions it in the prompt to load the named skill. | Exclude turns using this explicit form from implicit (description-routed) activation measures. |

## Fetch evidence

The `date -u` line before fetching the current `.md` and V2 page was: `Thu Oct 22 11:12:16 PM UTC 2026`.

Fetch commands and immediate metadata commands:

- `curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-skills.md -w "current HTTP %{http_code} bytes %{size_download} final %{url_effective}\n" https://opencode.ai/docs/skills.md`, then `sha256sum /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-skills.md` and `wc -c /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-skills.md`.
- `curl -L -sS -o /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-v2-skills -w "v2 HTTP %{http_code} bytes %{size_download} final %{url_effective}\n" https://opencode.ai/v2/docs/skills`, then `sha256sum /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-v2-skills` and `wc -c /fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-v2-skills`.

- `https://opencode.ai/docs/skills.md` — HTTP 200, 5,365 bytes, sha256 `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561`; downloaded as `/fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-skills.md`. Invocation-related lines: 44-45, 122-129.
- `https://opencode.ai/v2/docs/skills` — HTTP 200, 32,694 bytes, sha256 `243e88907fcbf35a7ae7dfc99e7c772e1a50fe40632091e4c6b328f1619f1318`; downloaded as `/fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-v2-skills`. The prompt form is at HTML line 289; the model tool call and exact-ID input are at lines 278-281; the opt-out behavior is at line 234.
- `date -u` before fetching the pinned docs source file was: `Thu Oct 22 11:12:55 PM UTC 2026`. URL: `https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx` — HTTP 200, 9,187 bytes, sha256 `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b`; downloaded as `/fast/scratch/hyaku/kotoba-r55/Srcopencode/opencode-skills-v2-source.mdx`. The invocation quote is line 201; the model tool call is at lines 186-192; the opt-out quote is line 142.

The source fetch ran `curl -L -sS -o opencode-skills-v2-source.mdx -w "source HTTP %{http_code} bytes %{size_download} final %{url_effective}\n" https://raw.githubusercontent.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills.mdx`, followed by `sha256sum opencode-skills-v2-source.mdx` and `wc -c opencode-skills-v2-source.mdx` from the sandbox clone directory.
- The raw source URL check against `corpus/SOURCES.md` returned `No matches found`. Existing S059 and S064 cite the served V1 and V2 pages, respectively; this draft row cites the distinct pinned raw source URL.
- `git ls-remote https://github.com/anomalyco/opencode.git HEAD refs/heads/dev refs/heads/main` returned `3d213123cdf574e55f88711554edfe6fd66a95ad` for both `HEAD` and `refs/heads/dev` (no `main` result); the raw source URL is pinned to that observed commit.

Novelty query: `grep -n 'https://raw\.githubusercontent\.com/anomalyco/opencode/3d213123cdf574e55f88711554edfe6fd66a95ad/services/www/src/docs/content/skills\.mdx' /home/vgpnk/Projects/shokunin/kotoba-shokunin/corpus/SOURCES.md` — no matches.

## Gate and limits

Sandbox clone: `/fast/scratch/hyaku/kotoba-r55/Srcopencode`, checked out at plan commit `a10240c0940f770a5f2a5f32a7e3c363dd5d40c`. Command run: `python3 -B /fast/scratch/hyaku/kotoba-r55/Srcopencode/verifiers/check_explicit_invocation.py --self-test` (under a 120-second timeout). Exit code: 0. Output: `self-test: 0 failure(s) over 29 assertions`.

Sandbox setup command: `timeout 120s bash -lc 'unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE; git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/Srcopencode && git -C /fast/scratch/hyaku/kotoba-r55/Srcopencode checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c'`; it returned without output, and the isolated checkout was used for the self-test.

The `--fetch` predicate was not run against this proposed row; it is not yet integrated into the lane's entry, SOURCES, lesson, or SKILL.md. No Q30 silence sweep was needed because an explicit form was found. No lane product files, verifier, or counter were changed; the only lane file written was this report. No tool was installed. C2 work is out of scope for this seat.

Artifact: `.ufo/waves/round-55/build/Srcopencode.md`. Scratch fetches and the isolated checkout are under `/fast/scratch/hyaku/kotoba-r55/Srcopencode/`.