Result: DONE — S068 re-opened byte-identical; quote and teaches cell hold; one over-wide phrase found in the knowledge entry's reading cell.

# ReopenS068 — Copilot CLI row re-check

Tip checked: `f0e6b695b746775823b65a8c45de7d50ea33e84f`. Lane read-only; fetch in `/fast/scratch/hyaku/kotoba-r55/ReopenS068/`.

## Re-open receipt

```
$ date -u
Fri 23 Oct 2026 12:09:28 AM UTC
$ curl -sS -o s068.md -w 'HTTP %{http_code} %{size_download} B\n' \
    'https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills.md'
HTTP 200 10057 B
$ wc -c s068.md
10057 s068.md
$ sha256sum s068.md
989af4981773349a74feaebfe98cdac9895b394707d201545ba55c8f9f4131a0  s068.md
$ date -u
Fri 23 Oct 2026 12:09:28 AM UTC
```

Byte-for-byte identical to the row's recorded receipt (10,057 B, same sha256, same second-scale clock). Host `docs.github.com` is in the counter's Copilot CLI pin set (`verifiers/check_explicit_invocation.py:132`, `HOSTS["Copilot CLI"]`). S068 does not appear in `corpus/SOURCES.md` at base `f0e5de82` (`git show f0e5de82:corpus/SOURCES.md | grep -c S068` → 0), tier `A`, kind `mined`, opened 2026-10-22 — all predicate fields satisfied.

## Cell verdicts

| Cell | Verdict | Evidence |
|---|---|---|
| Lesson Gate quote (`corpus/lessons/round-55.md:17`) | **HOLDS** | Quote "Use the /frontend-design skill to create a responsive navigation bar in React." is byte-exact on the fetched page at `add-skills.md:128`, the body of a fenced `copilot` block; the direction sentence sits at `:125` as stated. 14 words, ≤25. |
| SOURCES `teaches` cell (`corpus/SOURCES.md:81`) | **HOLDS** | "A Copilot CLI prompt asks for one named skill by its name after a forward slash, as in `/frontend-design`" — 19 words, ≤25; `:125` states include-the-name-preceded-by-a-forward-slash, `:128` shows `/frontend-design`. Says no more than the page. |
| Knowledge `reading` cell (`corpus/knowledge/explicit-invocation-round55.md:25`) | **BREAKS** | First half holds: `:125` does say the slash-prefixed name tells Copilot to use that skill. Second half over-wide: the cell reads "otherwise Copilot decides from the description (`:121`)", but `:121` says Copilot decides "based on **your prompt and** the skill's description". The prompt factor is dropped, so the cell asserts description-only routing the page does not state. Skill name "frontend-design" is itself inside the example prompt — exactly the signal the cell omits. |
| SKILL.md form cell (`SKILL.md:202`, `### Explicit invocation by client` at `:193`) | **HOLDS** | Form `` `/<skill-name>`, e.g. `/frontend-design` `` — backticked token starts `/` + letter, matching the counter's token rule and the page's `/frontend-design`. |
| SKILL.md "What it does" cell (`SKILL.md:202`) | **HOLDS** | "Asks Copilot to use the named skill; without it Copilot picks skills from the prompt and each description (`add-skills.md:121`)" — keeps both routing inputs the page names; accurate where the knowledge cell is not. |
| SKILL.md Action cell (`SKILL.md:202`) | **HOLDS** | "Set the turn aside as explicit when its prompt holds `/` plus a skill name" restates the page's explicit form only. Minor caveat, not a break: a prompt holding the built-in `/skills` command could match a skill literally named `skills`; no such skill is named anywhere, so the pattern does not over-fire on the documented surface. |

## Findings (by severity)

1. **Over-wide record (minor)** — `corpus/knowledge/explicit-invocation-round55.md:25`, reading cell for S068: "otherwise Copilot decides from the description" omits the prompt input from `add-skills.md:121` ("based on your prompt and the skill's description"). The SKILL.md row in the same lane states it correctly, so this is a single-cell inconsistency, not a systemic misread. The dropped phrase is the recurring over-wide-record defect class (rounds 50–54): the statement says the description is the routing input; the page says prompt plus description.

## Residual risk / verification gaps

- Counter not re-run here (out of scope for this seat); the C1 predicate's other arms (form-token syntax, Gate-table placement, host pins) were checked by reading, not execution.
- `/skills` builtin-vs-skill-name edge noted above; unreachable on the documented surface.
- No installs or tool changes performed. No lane files modified; all fetching/hashing done under `/fast/scratch/hyaku/kotoba-r55/ReopenS068/`.
