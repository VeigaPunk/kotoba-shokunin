Result: MIXED — S059/S064 and their entry/Gate evidence hold, but the landed SKILL.md action cell overstates an opencode benefit and cites superseded S001.

## Findings (severity order)

- **Low — BREAKS, `SKILL.md:191`, Action cell (as committed at `5a097e12`).** “Front-load it, because opencode shows all of it” gives a reason the evidence does not establish. The docs and both source trees establish full rendering, not a front-loading advantage; the earlier lane record explicitly says on opencode front-loading is “style, not survival” (`corpus/knowledge/frontmatter-trigger-surface.md:79-83`). The same action cites S001 even though SOURCES S018 says it supersedes S001 (`corpus/SOURCES.md:31`); the portability-floor paragraph already cites S018 (`SKILL.md:177`).

  **Corrected text:** `Keep the description within 1-1024 characters for portability (S018); opencode renders it whole, so the documented maximum is not an opencode listing cut.` This retains the supported advice and removes the unsupported causal implication and stale citation.

  Scope note: the checked-in workspace now has a different action phrase (“front-load it for the clients that cut or shorten; opencode itself shows all of it”), but `git show 5a097e12:SKILL.md` and `git show 58db81c:SKILL.md` both contain the quoted landed wording. I did not edit either version or the lane.

## Cell verdicts

- **SOURCES S059 — HOLDS** (`corpus/SOURCES.md:72`). The quote is verbatim and names the skill frontmatter `description`, not `name`: the served page introduces `name` and `description` as Agent Skills fields, then states at `skills.md:72`: “`description` must be 1-1024 characters.” Its scope explicitly limits the claim to what the v1 page states, not enforcement. The row’s anchor, opened date, status, recheck and used-by destination agree with the material checked here.
- **SOURCES S064 — HOLDS** (`corpus/SOURCES.md:77`). The row’s source is the V2 docs page and the cited source location is the V2 MDX source. That source has the exact quote at `services/www/src/docs/content/skills.mdx:160`; the rendered page contains the same prose with Markdown code delimiters rendered as `<code>` tags. “V2 does not enforce a maximum description length” is a bounded summary of that current-page statement, not a claim about v1 or every future V2 release.
- **Entry row — HOLDS** (`corpus/knowledge/skill-listing-thresholds-round54.md:46`). The S059 quote is identical to the page and Gate quote, five words, and includes the same `1-1024` token as the SKILL threshold cell. The threshold describes a `description` authoring maximum. The reading correctly distinguishes it from a render cut/budget and limits “no consequence” to what the page documents; its added runtime statement is supported by the source inspection below.
- **Entry Findings — HOLDS for the opencode statements** (`.../skill-listing-thresholds-round54.md:15-19, 21-23`). The statements that the v1 docs do not document a cut at 1,024, neither checked tree enforces that maximum, and the V2 page says V2 does not enforce one are supported. The opencode clause that its full description is rendered is also consistent with older lane evidence. The unrelated other-client claims in those Findings were not reviewed in this scoped assignment.
- **Gate S059 and S064 — HOLDS** (`corpus/lessons/round-54.md:29,34`). Both quotes match their respective source locations; the recorded original fetch metadata matches the corresponding source rows. S064’s source-file location is not a claim that its Markdown punctuation survives HTML rendering verbatim; the raw MDX location is verbatim.
- **SKILL.md threshold cell — HOLDS** (`SKILL.md:191` at the target commit). `1-1024 characters` matches S059, and the parenthetical accurately distinguishes the V1 rule from the V2 no-maximum statement.
- **SKILL.md past-the-threshold cell — HOLDS** (`SKILL.md:191` at the target commit). It does not claim the 1,024 maximum is enforced. V1.19.4 accepts any string description and interpolates it whole in the verbose `<available_skills>` renderer (`skill/index.ts:39,53-57,332`, with the compact renderer also interpolating the whole value at `:344`). V2.1.3 has no maximum in its optional string schema (`skill.ts:30`) and interpolates the whole description in its available-skills renderer (`instructions.ts:21`); availability filters only undefined descriptions and `autoinvoke === false` (`instructions.ts:82-84`).
- **SKILL.md Action cell — BREAKS** as above. The numeric portability advice is supported; the asserted opencode-specific reason for front-loading is not.

## Re-opened source records

Fetched directly by plain HTTP GET; UTC timestamps were recorded immediately after each request. SHA-256 is over the saved response bytes.

| URL | UTC | HTTP | bytes | SHA-256 |
|---|---|---:|---:|---|
| `https://opencode.ai/docs/skills.md` | 2026-10-22T22:03:15Z | 200 | 5,365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| `https://opencode.ai/v2/docs/skills` | 2026-10-22T22:03:16Z | 200 | 32,694 | `243e88907fcbf35a7ae7dfc99e7c772e1a50fe40632091e4c6b328f1619f1318` |
| `https://opencode.ai/v2/docs/skills.md` | 2026-10-22T22:03:16Z | 404 | 9 | `e3ebaa16dd9d9b9fc107c42183fb6cf9d22927e1af03dbbdfa0ccc38e4e4ac31` |
| `https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/web/src/content/docs/skills.mdx` | 2026-10-22T22:03:17Z | 200 | 5,462 | `39548bda09fc936c42cabf232472a4d92b5ed7133ed7762db19cef970df7dd4a` |
| `https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/services/www/src/docs/content/skills.mdx` | 2026-10-22T22:03:17Z | 200 | 9,187 | `931b5425fffc7339913327fbd5f54416397d664311407eeaaae9e349300da27b` |
| `https://raw.githubusercontent.com/anomalyco/opencode/v1.19.4/packages/opencode/src/skill/index.ts` | 2026-10-22T22:03:17Z | 200 | 11,843 | `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6` |
| `https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/core/src/skill/instructions.ts` | 2026-10-22T22:03:17Z | 200 | 4,089 | `ee6b644ca849292f68fdfae7c6ab1d3f02b46e9050757ff4a7cb976199ccc60e` |
| `https://raw.githubusercontent.com/anomalyco/opencode/v2.1.3/packages/schema/src/skill.ts` | 2026-10-22T22:03:18Z | 200 | 2,476 | `da003f8a6fd607569adb11e789c08eede92b044faa87648c422e69b47e281b4c` |

The v1 served text and V1 MDX body match on all nonblank lines after stripping MDX frontmatter and substituting `${name}` with `name`; the quoted rule is at served line 72 and MDX line 77. For S064, the quote is exact in the fetched MDX at line 160 and its prose appears in the fetched HTML at line 261 after code-markup rendering.

## Commands and cross-checks

- Exact landed-revision counter, in the sandbox clone only: `python3 -B verifiers/check_description_thresholds.py --rev 5a097e12b9409a1f425fbc76334f36f1402eb4cc --fetch` → `opencode BACKED found=True`; `description thresholds backed 7 of 7 clients`; `description thresholds found on the live page 7 of 7`; exit 0.
- Frozen-plan guard (a): `git show e33715486a45a4a857b64c30e6b695f7995858b8:corpus/SOURCES.md | grep -cE '^\| S0(59|64) '` → `0`, grep exit 1 (neither ID existed at the plan commit).
- Number novelty: `git show e33715486a45a4a857b64c30e6b695f7995858b8:SKILL.md | grep -c -F -- '1024'` → 1; the comma-form `1,024` also → 1. So opencode’s 1,024 is prior portability ground, not one of the plan’s required two new threshold numbers.
- Older consistency: S024 and S039 describe the same V1 docs (`corpus/SOURCES.md:37,52`); older render evidence says opencode passes the full description and front-loading is not survival-critical (`corpus/knowledge/frontmatter-trigger-surface.md:79-83`, `corpus/knowledge/harness-router-models-round9.md:175-176`). Round-53’s caution about treating docs as proof of enforcement is not a contradiction: S059 explicitly scopes itself to documentation, while the entry separately cites code evidence.

## Residual risk and verification gaps

The C1 counter is structural and its 7/7 result does not validate the learning/action prose; the action-cell issue above is outside its rules. This seat checked only opencode’s rows and did not assess whether other clients satisfy the plan’s two-new-number guard. No lane files were edited, no lane code was executed, and no tools were installed.