Result: DONE — VS Code’s official documentation gives a named skill slash-command example and documents a manual-only setting.

## Behavior and evidence

Fetched the served Markdown page from the client's pinned host:

- URL: `https://code.visualstudio.com/docs/agent-customization/agent-skills.md`
- `date -u` output: `2026-10-22T23:13:16Z`
- HTTP status: `200`
- Bytes: `23082`
- SHA-256: `26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a`
- Fetched bytes: `/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcVSCode/agent-skills.md`
The fetch command was `timeout 900 bash -c 'url=https://code.visualstudio.com/docs/agent-customization/agent-skills.md; file=/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcVSCode/agent-skills.md; date -u +%Y-%m-%dT%H:%M:%SZ; status=$(curl -L -sS -o "$file" -w "%{http_code}" "$url"); printf "HTTP_STATUS=%s\n" "$status"; printf "FINAL_URL="; curl -L -sS -o /dev/null -w "%{url_effective}\n" "$url"; printf "BYTES="; wc -c < "$file"; printf "SHA256="; sha256sum "$file"'`. Output: `2026-10-22T23:13:16Z`, `HTTP_STATUS=200`, `FINAL_URL=https://code.visualstudio.com/docs/agent-customization/agent-skills.md`, `BYTES=23082`, `SHA256=26973567be23eb5756eb6db62afacf055455fbe6f427d40b45659aacb44d361a`.

Under `## Use skills as slash commands`, the page says that selecting a skill invokes it (`agent-skills.md:285`) and gives this byte-exact example (`agent-skills.md:287`, 20 whitespace-separated words):

> You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`.

Form token for the proposed VS Code row: `` `/webapp-testing` ``. It explicitly identifies a named skill slash command; the example also shows that a user can supply task context after it. Reading for the entry: typing this command invokes that named skill, with optional extra context after the command.

The page also documents a way to block automatic invocation and keep manual invocation. Exact quote from the `disable-model-invocation` field at `agent-skills.md:151`:

> Set to `true` to require manual invocation through the `/` slash command only.

Thus `disable-model-invocation: true` requires manual slash-command invocation, rather than automatic loading based on relevance. This statement is directly quoted from the page.

## Drafts for integration

Draft SOURCES row (11 cells; `S0NN` is intentionally a placeholder):

| S0NN | Visual Studio Code — Use Agent Skills in VS Code — https://code.visualstudio.com/docs/agent-customization/agent-skills.md | docs | A | What VS Code documents about invoking named skills with chat slash commands and the manual-only `disable-model-invocation` setting (not a test of editor behavior) | § Use skills as slash commands (`agent-skills.md:283-287`); `disable-model-invocation` field (`agent-skills.md:151`) | VS Code gives `/webapp-testing` as a slash-command example and says extra context may follow. | mined | 2026-10-22 | 90d | corpus/knowledge/explicit-invocation-round55.md |

Draft `corpus/knowledge/explicit-invocation-round55.md` entry row (quote cell preserves the fetched Markdown bytes):

| VS Code | S0NN | "You can add extra context after the slash command. For example, `/webapp-testing for the login page` or `/github-actions-debugging PR #42`." | `agent-skills.md:287` | Typing a skill's slash command invokes it; the page says extra context may follow. |

Draft `SKILL.md` decision row:

| VS Code | `/webapp-testing` | Invokes the named skill; extra context may follow. | Set aside turns using this explicit command when measuring implicit (description-routed) activation. |

The proposed `teaches` cell is 14 words and stays within the explicit example quote. The entry quote is byte-exact, 20 words, and contains the token. Its token is absent from the frozen base inputs checked below, so it qualifies as new ground for this token.

## Gates, provenance, and limits

- Read the frozen plan first: `plans/round-55.md:18-34` pins C1 and requires a new source row, an entry quote, and the SKILL decision table. The counter docstring (`verifiers/check_explicit_invocation.py:20-61, 97-121`) pins the host `code.visualstudio.com`, 3–25 quote words, and the base new-ground rule.
- The page is already cited in base source rows S025 and S055 (`corpus/SOURCES.md:38,68`) for other claims. The targeted official-site search `site:code.visualstudio.com/docs/agent-customization "webapp-testing" OR "Use skills as slash commands"` returned this same page as its only source. The lane corpus search also located the existing citations but no prior `/webapp-testing` form. No alternate official page stating this form appeared in that targeted search; this is not an exhaustive claim about every page on the site.
- In the isolated plan-commit clone, `timeout 900 bash -c 'base=/fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcVSCode/base-f0e5de; mkdir -p "$base"; git -C /fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcVSCode archive f0e5de820a60ec44ff7e5b7c88ac8c8d463dde0c SKILL.md corpus/knowledge | tar -x -C "$base"; printf "ARCHIVE_EXIT=%s\n" "$?"'` produced `ARCHIVE_EXIT=0`. The `grep` tool searched `/webapp-testing` in the extracted `SKILL.md` and `corpus/knowledge/` and returned `No matches found`.
- Required sandbox check: `timeout 900 python3 -B /fast/scratch/hyaku/kotoba-r55/KotobaR55.SrcVSCode/verifiers/check_explicit_invocation.py --self-test` — exit 0; output: `self-test: 0 failure(s) over 29 assertions`.
- The full C1 `--fetch` predicate was not run: the report provides drafts only, and the final source/entry/Gate/SKILL table integration is outside this source seat. The exact quote must also be recorded in `corpus/lessons/round-55.md` § Gate before the full predicate can count it. No client behavior was run or independently measured.
- No product, verifier, source, entry, lesson, or SKILL files were edited. No tools were installed. This report is the only lane file written; fetched bytes and base extraction are in the assigned scratch clone.

Report: .ufo/waves/round-55/build/SrcVSCode.md