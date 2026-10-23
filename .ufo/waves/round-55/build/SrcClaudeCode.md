Result: DONE — Claude Code documents direct `/skill-name` invocation, and the C1 counter self-test passed in the sandbox.

## Finding and draft rows

Fetched quote (19 words, byte-exact): “You can type `/skill-name` to invoke it directly, and Claude can load it automatically when relevant to your conversation.” — `skills.md:547`.

Draft `corpus/SOURCES.md` row (11 cells):

| S0NN | Claude Code — Extend Claude with skills — https://code.claude.com/docs/en/skills.md | docs | A | Claude Code's explicit direct invocation syntax for a named skill | § Control who invokes a skill (`skills.md:547`); fetch details below | Users can type `/skill-name` to invoke a skill directly; Claude can also load it automatically when relevant | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md |

Draft `corpus/knowledge/explicit-invocation-round55.md` row:

| Claude Code | S0NN | "You can type `/skill-name` to invoke it directly, and Claude can load it automatically when relevant to your conversation." | § Control who invokes a skill, `skills.md:547` | Typing `/skill-name` invokes a skill directly; Claude may also load it automatically when relevant. |

Draft `SKILL.md` row:

| Claude Code | `/skill-name` | Typing this slash form invokes a named skill directly. | Set aside turns where the user used this form when measuring implicit (description-routed) activation. |

The page also documents how to block automatic invocation while preserving user invocation. The table header at `skills.md:574` is `| Frontmatter | You can invoke | Claude can invoke | When loaded into context |`.

The data row at `skills.md:577` is quoted verbatim:

```
| `disable-model-invocation: true` | Yes | Not on its own | Description not in context, full skill loads when invoked |
```

The table says the user can still invoke the skill while Claude cannot invoke it on its own.

## Source provenance

`date -u` output, pasted: `Thu 22 Oct 2026 11:12:23 PM UTC`.

Fetch command used the `.md` routes with `curl -L --max-time 60 -sS`, then `wc -c` and `sha256sum`:
Exact first source-fetch command (the `date -u` line above is its output):

```sh
date -u && timeout 70s curl -L --max-time 60 -sS -o /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/skills.md -w 'skills HTTP_STATUS=%{http_code}\n' https://code.claude.com/docs/en/skills.md && wc -c /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/skills.md && sha256sum /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/skills.md && timeout 70s curl -L --max-time 60 -sS -o /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/slash-commands.md -w 'slash-commands HTTP_STATUS=%{http_code}\n' https://code.claude.com/docs/en/slash-commands.md && wc -c /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/slash-commands.md && sha256sum /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/slash-commands.md
```

Commands route fetch:

```sh
date -u && timeout 70s curl -L --max-time 60 -sS -o /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/commands.md -w 'HTTP_STATUS=%{http_code}\n' https://code.claude.com/docs/en/commands.md && wc -c /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/commands.md && sha256sum /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/commands.md
```

Slash-command route follow-up:

```sh
timeout 70s curl -L --max-time 60 -sS -o /dev/null -w 'HTTP_STATUS=%{http_code}\nURL_EFFECTIVE=%{url_effective}\nNUM_REDIRECTS=%{num_redirects}\n' https://code.claude.com/docs/en/slash-commands.md
```


- `https://code.claude.com/docs/en/skills.md` — HTTP 200; 112,748 bytes; SHA-256 `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737`. Quote is at fetched line 547.
- `https://code.claude.com/docs/en/slash-commands.md` — HTTP 200; 112,748 bytes; SHA-256 `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737`; fetched at the same `date -u` time above. A follow-up GET reported `URL_EFFECTIVE=https://code.claude.com/docs/en/slash-commands.md`, `NUM_REDIRECTS=0`; the route returned bytes identical to `skills.md` (the content title is “Extend Claude with skills”), not a distinct source page.
- `https://code.claude.com/docs/en/commands.md` — `date -u`: `Thu 22 Oct 2026 11:13:05 PM UTC`; HTTP 200; 54,225 bytes; SHA-256 `80164a5bc0d09cd44fef9d2d99d152a4fefae04adace1cdfba55d7448db7ed52`. Search for `skill-name|invoke.*skill|skills? directly|invoke it directly|slash command` returned no matches.

Base `corpus/SOURCES.md` search for the Claude skills/slash-command routes found S022 at line 35 and S053 at line 66, both already citing the skills page (S053 uses the `.md` route). The slash-command route served identical bytes, and the separate commands reference search found no explicit skill form; therefore this draft reuses the already-cited skills page under the plan's exception for a form not stated by another page.

## Sandbox check, surfaces, and limits

Sandbox clone command completed with no output:

`timeout 900s mkdir -p /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode && timeout 900s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/repo && timeout 900s env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git -C /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/repo checkout -q a10240c0940f770a5f2a5f32a7e3c363dd5d40c0`

`timeout 900s python3 -B /fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/repo/verifiers/check_explicit_invocation.py --self-test; printf 'EXIT_CODE=%s\n' "$?"` → `self-test: 0 failure(s) over 29 assertions`; `EXIT_CODE=0`.

Only this report was written in the lane: `.ufo/waves/round-55/build/SrcClaudeCode.md`. Documentation fetches and the sandbox clone are under `/fast/scratch/hyaku/kotoba-r55/SrcClaudeCode/`. No product files, knowledge entries, SOURCES rows, or lesson rows were changed. No install was needed.

Limits: the C1 `--rev … --fetch` predicate was not run; these draft rows have not been integrated or checked against the round-55 lesson Gate. The self-test does not establish the C1 predicate or Claude Code runtime behavior. No C2 work was performed.