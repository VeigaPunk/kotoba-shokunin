Result: HOLDS — S065 (Claude Code) re-opens clean: my fetch is byte-identical to the recorded one, the Gate quote is byte-exact at `skills.md:547`, and the teaches/entry-reading/SKILL.md cells each say no more than the page. One non-blocking note: the row's URL is already cited at base by S022/S053, so it cannot count as v2 new ground (and does not need to — G comes from the other rows).

# Fetch evidence (my own, this seat)

```
$ cd /fast/scratch/hyaku/kotoba-r55/ReopenS065
$ date -u
Fri 23 Oct 2026 12:10:59 AM UTC
$ curl -sS -o skills-now.md -w 'HTTP %{http_code} bytes %{size_download} url %{url_effective}\n' --max-time 60 https://code.claude.com/docs/en/skills.md
HTTP 200 bytes 112748 url https://code.claude.com/docs/en/skills.md
curl_exit=0
$ wc -c < skills-now.md
112748
$ sha256sum skills-now.md
909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737  skills-now.md
```

Secondary anchor-cell claim re-verified (`slash-commands.md` serves the same bytes):

```
$ date -u
Fri 23 Oct 2026 12:15:27 AM UTC
$ curl -sS -o slash-commands-now.md -w ... https://code.claude.com/docs/en/slash-commands.md
HTTP 200 bytes 112748 url https://code.claude.com/docs/en/slash-commands.md
curl_exit=0
$ sha256sum slash-commands-now.md
909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737  slash-commands-now.md
$ cmp -s skills-now.md slash-commands-now.md && echo IDENTICAL
IDENTICAL
```

Bytes are identical to the seat's recorded fetch (S065 anchor cell: 112,748 B, sha256 `909dd50ab595e5511d0c24e00527ec4f5ad9acc90e308f7df992c071b1ddc737`; `SrcClaudeCode.md:53`), so no page drift since 2026-10-22T23:12:23Z.

# Per-cell verdicts

| cell | verdict | evidence |
|---|---|---|
| Gate quote `lessons/round-55.md:14` (19 words ≤25) | HOLDS | byte-exact at fetched line 547: `sed -n '547p' skills-now.md` → `By default, both you and Claude can invoke any skill. You can type \`/skill-name\` to invoke it directly, and Claude can load it automatically when relevant to your conversation. Two frontmatter fields let you restrict this:` — the quoted 19-word substring is verbatim, no normalisation needed |
| Gate location `skills.md:547` | HOLDS | the quote sits on fetched line 547; the `§ Control who invokes a skill` heading named in the anchor cell is fetched line 545 |
| Gate fetch record (opened `2026-10-22T23:12:23Z`, 112,748 B, `909dd50a…`) | HOLDS | my fetch reproduces identical bytes and hash |
| SOURCES row `corpus/SOURCES.md:78` | HOLDS | 11 cells against header `id\|source\|kind\|tier\|scope\|anchor\|teaches\|status\|opened\|recheck\|used-by` (`SOURCES.md:11`); `docs \| A \| mined \| 2026-10-22 \| 90d`; used-by names `corpus/knowledge/explicit-invocation-round55.md, corpus/lessons/round-55.md`; first URL on pinned host `code.claude.com` (counter HOSTS at `verifiers/check_explicit_invocation.py:124`) |
| SOURCES `teaches` cell (19 words ≤25) | HOLDS | "A user can type `/skill-name` to invoke a skill directly, and Claude can also load it automatically when relevant" — a verbatim-faithful paraphrase of `:547`; adds nothing the page does not say; the `(user-typed)` qualifier in scope is borne by `:25` ("typing `/` followed by the skill name") and `:394` ("you type `/name`") |
| SOURCES `anchor` cell — `disable-model-invocation: true` row `:577`; `slash-commands.md` same-bytes | HOLDS | fetched line 577 is the `disable-model-invocation: true` table row (`Yes \| Not on its own \| Description not in context, full skill loads when invoked`); the slash-commands route re-served identical bytes today (evidence above) |
| Entry row `explicit-invocation-round55.md:22` — quote | HOLDS | identical double-quoted string to the Gate cell; byte-exact on the page (see line 547 above); 19 words |
| Entry row — location `skills.md:547` | HOLDS | correct |
| Entry row — reading cell | HOLDS | "Typing the slash form invokes the named skill directly; the same sentence says Claude may also load it automatically." — both clauses are in the cited sentence at `:547`; says no more |
| SKILL.md row `SKILL.md:199` — form `` `/skill-name` `` | HOLDS | page documents it verbatim (`:547`, also `:9`, `:25`, `:1187`); token matches v2 TOKEN_RE (`/skill-name`, `check_explicit_invocation.py:145`); sigil-stripped `skill-name` is not in BUILTINS (`:146-153`); not a listing or built-in command — the page calls it the user's way to "invoke it directly" (`:547`) and excludes built-ins from the skill path only on the model side (`:851`) |
| SKILL.md row — what-it-does | HOLDS | "Invokes the named skill directly" = `:547`; "automatic loading stays possible unless `disable-model-invocation: true` (`skills.md:577`)" = the `:577` row (you: Yes, Claude: Not on its own), corroborated by `:549` |
| SKILL.md row — action | HOLDS | "starts with the skill's `/name`" is the page's form (command entered at the prompt; `:145` example block puts `/summarize-changes` alone; `:81` shows `/claude-api migrate` with a subcommand after the name); the page documents no mid-text invocation, so "starts with" is the page's own usage and the conservative reading; "count only the other activations as implicit" is the table's declared purpose (`SKILL.md:195`), not a page claim |

# Q31 / Q26 (is it really explicit invocation; does anything say more than the page?)

- The form is a genuine user-typed invocation, not a listing or management command: page `:547` ("type `/skill-name` to invoke it directly"), `:25` ("invoke a bundled skill the same way as any other skill, by typing `/` followed by the skill name"), `:394` (`user-invocable: false` → "doesn't run it when you type `/name`"). Q31: HOLDS.
- No over-wide sentence found in the teaches, anchor, entry-reading, or SKILL.md cells. The one narrowness choice worth recording — the Action cell's "starts with" rather than "holds" — is conservative (the page shows the command at prompt start only) and cannot misclassify an implicit turn as explicit.
- Not found on the page, and nowhere claimed: nothing in S065's cells asserts a client-side listing command, a mid-text invocation form, or measured client behaviour — the entry's own framing states these are "documentation statements, not measured client behaviour" (`explicit-invocation-round55.md:11-12`).

# Notes (not defects)

- **URL reuse.** S065's URL `https://code.claude.com/docs/en/skills.md` is the same page already cited at base by S022 and S053 (`SOURCES.md` base rows; seat report `SrcClaudeCode.md:57` acknowledges this and invoked a plan exception for forms no other page states). The v2 counter's new-ground rule requires the row's URL to not be a base row URL, so Claude Code cannot contribute to `new ground G`; it still backs and finds. This is consistent with the landed outcome (`found 5 of 5; new ground 4` per `SCORECARD.md:140`) and is the counter's own discount working, not a misrecorded cell.
- The row's `anchor` also cites `:577`, which I verified byte-exact; the Gate lesson keeps a normalisation note only for S067/S069/S071 (`lessons/round-55.md:23-25`) — S065 needed none and none was applied.

# Scope and hygiene

- Read-only on the lane; no lane file edited. Fetched bytes stored at `/fast/scratch/hyaku/kotoba-r55/ReopenS065/{skills-now.md,slash-commands-now.md}` only.
- No headless browser, no bot challenge (plain `curl -sS`, HTTP 200), no paid model call, no `model` parameter, no lane code executed (no clone needed — checks are fetch + text).
- No tools installed or updated (none needed).
