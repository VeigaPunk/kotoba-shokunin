Result: HOLDS — S066 (Codex) re-opened to byte-identical bytes; every scoped cell (lesson Gate quote, SOURCES teaches, entry reading, SKILL.md row) is on the page or attributed to held knowledge it names.

Seat: ReopenS066 (FALSIFY wave, axis depth). Revision reviewed: tip `f0e6b695b746775823b65a8c45de7d50ea33e84f`. Read-only; no lane files changed. Sandbox fetches under `/fast/scratch/hyaku/kotoba-r55/ReopenS066/`.

## Re-open receipt

URL (from `corpus/SOURCES.md` row S066, `SOURCES.md:79`): `https://developers.openai.com/blog/eval-skills.md`

- `date -u` before/after: `Fri 23 Oct 2026 12:10:26 AM UTC` / `Fri 23 Oct 2026 12:10:26 AM UTC`
- `curl -sS -o s066_eval-skills.md -w 'HTTP %{http_code} bytes %{size_download}\n' --max-time 60` → `HTTP 200 bytes 19356`
- `sha256sum` → `6cf414bb3e2dddfd940e3ea3293ce588f777e80a7d935cf8a73d9f5cfb94d3a2`; `wc -c` → `19356`
- Matches the recorded fetch in the SOURCES anchor and the Gate row (`corpus/lessons/round-55.md:15`: `19,356 B, sha256 6cf414bb…`, opened `2026-10-22T23:13:16Z`, seat SrcCodex). Byte-identical, not a same-sha claim.
- Host `developers.openai.com` is in the counter's Codex pin set (`verifiers/check_explicit_invocation.py:127`).

## Cell-by-cell verdicts

| cell | verdict | evidence |
|---|---|---|
| Lesson Gate quote (round-55.md:15) | HOLDS | Quote `"Use the $setup-demo-app skill to create the project in this directory."` found byte-exact by `grep -nF` at line 148 of the fetched bytes (exit 0, printed `:148: 'Use the $setup-demo-app skill to create the project in this directory.'`). Stated location `eval-skills.md:148` correct; it sits inside a `codex exec` prompt string (fenced block `:146-149`, prompt single-quoted as the cell says). No normalisation needed: the quote is a substring of raw line 148. 12 words ≤ 25, holds the word `skill`, holds token `$setup-demo-app` verbatim. Entry quote (`explicit-invocation-round55.md:23`) is byte-identical to the Gate quote. |
| SOURCES `teaches` cell (SOURCES.md:79, cell 7) | HOLDS | 17 words: "A Codex prompt names a skill with a `$` prefix, as in `$setup-demo-app`, to invoke it explicitly". Page states the general rule at `:130` — "explicitly activate the skill, either via the `/skills` slash command or by referencing it with the `$` prefix" — and the example at `:148`; `:171-172` names naming-the-skill-directly as the explicit case. Says no more than the page. |
| SOURCES `scope` cell (cell 5) | HOLDS | "Codex explicit named-skill invocation in a user prompt (an example in vendor guidance, not a measurement)" — the page is a vendor evals blog post (`developers.openai.com/blog/eval-skills.md`, title `Testing Agent Skills Systematically with Evals`); §3 `:126-151` is the cited example; §4 `:171-183` backs "explicit vs implicit test prompts". |
| Entry `reading` cell (explicit-invocation-round55.md:23) | HOLDS | "The prompt names the skill with `$`; the page calls this an explicit-invocation prompt (`:171-172`)." `:171-172` labels test-01 (`:163`, a different string also holding `$setup-demo-app`) the "Explicit invocation" prompt that "names the skill directly". The `codex exec` prompt at `:148` is not that identical CSV row, but the page's generalisation at `:130` ("explicitly activate … by referencing it with the `$` prefix") makes the reading supported. |
| SKILL.md `explicit form` cell (`SKILL.md:200`) | HOLDS | `` `$<skill-name>`, e.g. `$setup-demo-app` `` — `$setup-demo-app` is verbatim on the page; the `$`-prefix pattern is stated generally at `:130`. The generalised form is also held knowledge: `skill-overlap-levers-round51.md:26` quotes `explicit $skill invocation still works` (S021), and the entry's Limits (`:67-68`) disclose that the general rule comes from S021, not S066. |
| SKILL.md `what it does` cell | HOLDS | "Names the skill in the prompt so Codex invokes it when asked" — page `:172` ("ensures that Codex can invoke `setup-demo-app` when asked") and `:130`. The tail clause `allow_implicit_invocation: false` keeps this and stops implicit use is attributed in-cell to (S021) and is verbatim-held at `skill-overlap-levers-round51.md:26`; it is not on this page and is not claimed to be — disclosed, not over-wide. |
| SKILL.md `action` cell | HOLDS | "Set the turn aside as explicit when its user text holds `$` plus an installed skill name; only the rest can test description routing" — page `:171-183` is exactly the explicit-vs-implicit-vs-negative split the action encodes; `:172` and `:174-175` carry both sides. "installed skill" is a fair reading of a referenced skill. |

## Row metadata (spot checks)

Row has 11 cells; kind `docs`, tier `A`, status `mined`, opened `2026-10-22`, recheck `90d`, used-by names `corpus/knowledge/explicit-invocation-round55.md` and the lesson — all counter-conformant. Not a row at base: `git show f0e5de82:corpus/SOURCES.md | grep -c S066` → `0`. Token absent at base: `git show f0e5de82:SKILL.md | grep -cF 'setup-demo-app'` → `0`; same fixed-string grep over every `corpus/knowledge/*.md` at `f0e5de82` → `0` matches (new-ground condition for `$setup-demo-app` holds). Quote contains `skill`, satisfies the v2 word-skill rule. Entry `location` cell and front-matter `source:` tag (`:148`) agree with the page.

## Notes (not defects)

1. The page offers two explicit-activation routes (`/skills` slash command or `$` prefix, `:130`). SKILL.md picks `$` — correctly, since `/skills` is a listing/built-in and `$` is the per-skill naming form; no claim of exclusivity is made. Residual blind spot only if a `/skills` turn selects a named skill; the action cell would miss it. Worth a caveat word in a future edit, not a BREAKS.
2. The reading cell's "(`:171-172`)" cite is indirect for the `codex exec` prompt: the page labels test-01, not the line-148 string, the explicit-invocation case. The claim survives on `:130`, but the cite alone would be thinner than stated.
3. `teaches` and `reading` both correctly mark the S066 page as vendor guidance/an example, not a measurement — consistent with S021 being the row for the general rule.

## Commands run (all in sandbox or read-only in lane)

- `curl` receipt above → exit 0, sha256 match.
- `awk`/`grep -nF` line-range reads on fetched bytes → outputs above, quote grep exit 0.
- `git show f0e5de82:…` greps → `0` counts as reported.
- Lane reads: `verifiers/check_explicit_invocation.py`, `corpus/SOURCES.md:79`, `corpus/lessons/round-55.md`, `corpus/knowledge/explicit-invocation-round55.md`, `SKILL.md:193-211`, `plans/round-55.md`, `corpus/knowledge/skill-overlap-levers-round51.md:26`.

No installs needed (curl, git, coreutils already present).
