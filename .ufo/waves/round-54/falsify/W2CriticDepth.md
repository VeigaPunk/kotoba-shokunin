Result: MIXED — C1 is real learning and the table is a rule-conformant decision surface (counter 7 of 7, guards a/b/c pass), but the intro sentence's framing omits an admitted, still-live counterexample (Codex's shipped parser cuts every catalog description at 1,024), and three cells say more than their sources (Cursor "not cut", Codex "raises the default", opencode's front-load reason).

Seat: `KotobaR54.W2CriticDepth` (critic, falsify wave). Read at `5a097e12` (C1) and tip `58db81c4`. Sandbox clone
`/fast/scratch/hyaku/kotoba-r54/W2CriticDepth` at `58db81c4`; fetched bytes under `.scratch/fetch/` there. No lane
file written except this report. No installs, no paid model calls, no counter edits.

## Verdicts

| # | Question | Verdict | Impacted axes |
|---|---|---|---|
| 1 | Is the table a decision surface with an action per row (SKILL.md § Decision tables, table rule)? | HOLDS (weak as a surface) | depth |
| 2 | Does the intro sentence hold against the quotes? | MIXED: every clause holds literally; the framing BREAKS on Codex | depth, calibration |
| 3 | Is any action or past-threshold cell advice the sources do not support? | BREAKS on 3 cells; 3 more minor | calibration, depth |
| 4 | Is the learning real, or re-stated held numbers (erratum 3 guard b)? | HOLDS; guard (b) is weaker than it reads | depth, calibration |
| 5 | Does the claim harm any axis (599 of 600 lines, long rows)? | HOLDS (no harm today); 1-line headroom is a tradeoff | operability (future) |

## Re-runs (sandbox, 2026-10-22T21:54:07Z)

```
python3 -B verifiers/check_description_thresholds.py --rev 5a097e12   → "description thresholds backed 7 of 7 clients"
python3 -B verifiers/check_description_thresholds.py --rev 58db81c4   → "description thresholds backed 7 of 7 clients", exit 0
python3 -B verifiers/check_description_thresholds.py --rev 58db81c4 --fetch
  → all seven "BACKED found=True"; "description thresholds found on the live page 7 of 7", exit 0      (guard c)
guard a: for S053..S059: git show e3371548:corpus/SOURCES.md | grep -c "^| S0NN |"  → 0 for all seven
guard b: git show e3371548:SKILL.md | grep -c -F: 1,536→0  1%→0  2%→0  8,000→0  10,000→0  100 words→0  1024→1  1,024→1
git diff --stat e3371548 58db81c4 -- verifiers/check_description_thresholds.py verifiers/verify_surfaces.py → empty, exit 0
python3 -B verifiers/verify_skill_checklist.py → "PASS trigger.line_budget: evaluated 599 — 599 lines within budget 600"
  (overall exit 1 in the sandbox only from path artifacts: name_directory 'W2CriticDepth', cross-lane citations)
```

## Fetch records (opened by this seat; curl -L, plain GET)

Every page the Gate names re-opened byte-identical to the Gate's recorded byte count and digest.

| file | URL | UTC | HTTP | bytes | sha256 |
|---|---|---|---|---|---|
| cc-skills.md | https://code.claude.com/docs/en/skills.md | 21:52:36Z | 200 | 111,928 | `d1359f0c64371b3f2e267069d9f752418466abadb2765eca2929ecbee4ce0b2b` |
| cc-settings.md | https://code.claude.com/docs/en/settings-reference.md | 21:52:36Z | 200 | 413,033 | `022e35adb2721a940aff2eb1f2aab9a3aabbf4171b46c01e103aaf2dcd1c143d` |
| cc-changelog.md | raw.githubusercontent.com/anthropics/claude-code/5ed799e5…/CHANGELOG.md | 21:52:37Z | 200 | 1,070,244 | `121129bcb4d33f3bafe4ea5bc30b4f6d5ec057e886030f84b62648c3115c2c49` |
| codex-build.md | https://learn.chatgpt.com/docs/build-skills.md | 21:52:37Z | 200 | 11,035 | `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5` |
| codex-config.md | https://learn.chatgpt.com/docs/config-file/config-reference.md | 21:52:37Z | 200 | 136,297 | `fe48af085a53345cf171cf492f3147eb2bb297b8ab28f83e67b8e9e62f715a21` |
| vscode.md | https://code.visualstudio.com/docs/agent-customization/agent-skills.md | 21:52:38Z | 200 | 22,871 | `de5ba34f0c2306af7d1b792581d01f53b4ddd6a912699a19f3a2c958efda3ab5` |
| copilot.md | https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference.md | 21:52:38Z | 200 | 461,944 | `c61997efd7c939324e1f1b846fcb9ed420e5bbfd5eb5319531c6e6210025b5c9` |
| gemini-bp.md | https://geminicli.com/docs/cli/skills-best-practices.md | 21:52:38Z | 200 | 3,257 | `612c3b8396fdc6669702127975c5d4ec5ce59bd8355fdbfb837fdd83d3d524c3` |
| cursor-rn.md | https://cursor.com/docs/release-notes.md | 21:52:38Z | 200 | 301,193 | `fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd` |
| oc-v1.md | https://opencode.ai/docs/skills.md | 21:52:38Z | 200 | 5,365 | `f10ced73971ce83b85f41395e2e15a683fe5a874e9057fc9d13da5f5a1bf8561` |
| oc-v2.html | https://opencode.ai/v2/docs/skills | 21:52:39Z | 200 | 32,694 | `243e88907fcbf35a7ae7dfc99e7c772e1a50fe40632091e4c6b328f1619f1318` |
| cursor-skills.md | https://cursor.com/docs/skills.md | 21:53:42Z | 200 | 18,477 | `a642fa96776c247dba126a325e1dd73dac3f532a70060e745fb9bbd5b377602d` |
| oc-v1-index.ts | raw…/anomalyco/opencode/v1.19.4/packages/opencode/src/skill/index.ts | 21:53:42Z | 200 | 11,843 | `91dce57f590e1ad3103e0555b893500e098a95cde2739422b699233889b205e6` |
| oc-v2-instr.ts | raw…/anomalyco/opencode/v2.1.3/packages/core/src/skill/instructions.ts | 21:53:56Z | 200 | 4,089 | `ee6b644ca849292f68fdfae7c6ab1d3f02b46e9050757ff4a7cb976199ccc60e` |
| codex-render.rs | https://raw.githubusercontent.com/openai/codex/main/codex-rs/ext/skills/src/render.rs | 21:55:12Z | 200 | 37,304 | `1abc9f7fe7b0d261c36adbd3611125ca74dcc01fec69bb68e8915565264a4ecb` |
| gem-skillLoader.ts | raw…/google-gemini/gemini-cli/451a02ff…/packages/core/src/skills/skillLoader.ts | 21:55:43Z | 200 | 6,560 | `8bce3215263e9ec06f32a865715c04af6deb4b6299db1490665f53972d4326f9` |
| gem-snippets.ts | raw…/google-gemini/gemini-cli/451a02ff…/packages/core/src/prompts/snippets.ts | 21:55:43Z | 200 | 70,505 | `b2cccbd0cf68e33d057f33938e457fe3c781cc7e65c593f7a3974d70c5c68fe7` |

`codex-render.rs` is at branch `main`, not a pinned commit: `api.github.com/repos/openai/codex/commits/main` answered
403 at 21:55:19Z, so the commit is unresolved; the digest above identifies the bytes. A first try at
`v2.1.3/packages/opencode/src/skill/instructions.ts` answered 404 (wrong package; the seat's path is `packages/core`).
Read only, not fetched: `/fast/scratch/hyaku/kotoba-r54/SrcCopilotCLI/_scratch/fetch2/changelog.md` (289,859 B,
sha256 `c4b793bd6555bf699c1f6ef61fb9052e6400df8f475c97fdae25ba5084531dfb`, the seat's pinned `github/copilot-cli@7ea98dfc` copy).

## 1. Decision surface — HOLDS (weak)

The rule (`SKILL.md:203-207` at tip): every row must carry an action cell (command, route, named fallback or
verdict); a table with no action column is documentation. All seven rows (`SKILL.md:185-191`) have a non-empty
imperative `Action` cell, and Claude Code's names concrete settings (`skillListingMaxDescChars`,
`skillListingBudgetFraction`, `"name-only"`), each present in the source (`cc-settings.md:2455`, `:2471`, `:3709`;
`cc-skills.md:1213`). So the rule holds.

Weaknesses (not breaks):
- Four of seven actions are one sentence: VS Code, Copilot CLI, Cursor and opencode all say "keep ≤1024, lead
  with what and when" (`SKILL.md:187,188,190,191`). The table keys on client, but for those four the decision does
  not depend on the client.
- No row gives the cross-client answer a portable author needs (the binding constraint across all seven plus omp).
  The reader has to combine the floor (`SKILL.md:177`, ≤1024), omp's 99 (`:161`) and Gemini's ~100 words.
- Two actions address the person who configures the client, not the skill author (Claude Code's settings). That is
  allowed, but it mixes audiences in one cell.

Smallest safe correction (text, optional): one closing sentence under the table, e.g. "Portable: `description`
≤1,024 characters, the capability and trigger inside the first 99 (omp), and near ~100 words of name plus
description if Gemini CLI is a target." That collapses the four identical rows' meaning without adding a row.

## 2. Intro sentence — MIXED

Sentence (`SKILL.md:181`): "A documented maximum is not a render cut: four clients state 1,024 and none documents a
cut there, Claude Code and Codex cut or budget the listing, omp cuts at 99 (§ Router model)."

Clause by clause against the bytes:
- "four clients state 1,024": HOLDS. VS Code "Maximum 1024 characters." (`vscode.md:148`); Copilot CLI "Max 1024
  characters." (`copilot.md:1274`); Cursor "a description over 1,024 characters" (`cursor-rn.md:122`); opencode
  "`description` must be 1-1024 characters." (`oc-v1.md:72`).
- "none documents a cut there": HOLDS for the four. `grep -n -i -E 'truncat|budget|warn|shorten|cut' vscode.md` finds
  no description consequence (only `:173` forked context, `:326` terminal approvals). The Copilot table row states
  only the cap; Cursor's release note says "Skills that load but exceed the spec's limits now show a yellow warning
  count" (`cursor-rn.md:122`); opencode v1 prints the string whole (`oc-v1-index.ts:332`, `` `<description>${skill.description}</description>` ``),
  v2.1.3 likewise (`oc-v2-instr.ts:21`), and the V2 page says V2 "does not enforce … a maximum description length".
- "Claude Code and Codex cut or budget the listing": HOLDS for those two (`cc-skills.md:389`, `:1207`;
  `codex-build.md:37-41`).
- "omp cuts at 99 (§ Router model)": HOLDS (`SKILL.md:97` heading; `:161` "a miss keeps at most 99 chars").

The framing BREAKS — strongest counterexample: **Codex cuts each description at 1,024 in shipped code, and the lane
already admitted it.** `corpus/knowledge/frontmatter-rule-authorities-round48.md:51`, note (a): "Codex CLI 0.163.0's
shipped parser has its own limits (64-character name, catalog descriptions truncated at 1,024) … not tabled here
because no source row pins that code." It is still live today on `main`:
`codex-render.rs:24` `const MAX_CATALOG_SKILL_DESCRIPTION_CHARS: usize = 1_024;`, applied to every catalog entry at
`:220` (`description: truncate_catalog_skill_description(description)`), which keeps 1,021 characters plus `"..."`
(`:1118-1134`, `:25`). So a fifth client does cut at exactly 1,024. The sentence's lesson ("a documented maximum is
not a render cut") is literally about *documented* maxima, but a reader acting on SKILL.md alone takes "1,024 is not
where text gets cut", and the Codex row (`SKILL.md:186`) gives no per-entry cut at all. The entry's "Relation to what
the lane already held" (`skill-listing-thresholds-round54.md:49-57`) also omits this admitted measurement, although
`ScoutPriorHolds.md` row 23 and § C item 8 flagged it before landing.

Second omission: Copilot CLI's own changelog documents a listing limit: "Skills that exceed the token limit are still
discoverable and invocable by name" (`github/copilot-cli@7ea98dfc changelog.md:1993`, § 1.0.32, 14 words), found and
recorded by seat `SrcCopilotCLI` (`.ufo/waves/round-54/build/SrcCopilotCLI.md:97`). It has no number, so it cannot back
the counter, but "Claude Code and Codex cut or budget the listing" leaves a reader thinking only two do. The lane held
nothing about it before (`git grep -i 'token limit' e3371548 -- corpus/knowledge SKILL.md` → no match).

Smallest safe correction: open a SOURCES row pinning `openai/codex` `codex-rs/ext/skills/src/render.rs` at a commit,
then append to the Codex "Past the threshold" cell: "shipped code also cuts every catalog description at 1,024
characters (1,021 + `...`)". Append to the intro: "Codex's shipped parser also cuts at 1,024 (code, not docs)". For
Copilot CLI, append "the changelog (1.0.32) says skills over an unnumbered token limit stay listed by name" with its
own row. Without new rows, at least name both in the entry's "Relation to what the lane already held" and Limits.

## 3. Advice the sources do not support — BREAKS on three cells

BREAKS:
- **Cursor, "Warned, not cut"** (`SKILL.md:190`). The source says only that skills that load and exceed the limits
  show a warning (`cursor-rn.md:122`); Cursor's skills page states no length rule
  (`grep -n -i -E '1,024|1024|5,000|warn' cursor-skills.md` → no match; `:173` describes the field only). Cursor is
  closed source and no seat read its code. The entry itself says "no truncation, shortening, drop or refusal is
  documented" (`skill-listing-thresholds-round54.md:44`); the SKILL cell drops "documented" and asserts a fact no one
  observed (the over-wide-record defect). Fix: "Warned; no cut documented: the skill still loads and `/skills` shows …".
- **Codex, "`skills.max_context_tokens` raises the default, capped at 10,000 tokens"** (`SKILL.md:186`). The docs say
  "set a different budget, up to 10,000 tokens" (`codex-build.md:43-44`) and "Explicit values are capped at `10000`
  tokens" (`codex-config.md:378`). The code sets an explicit value to `min(value, 10_000)` (`codex-render.rs:128-137`)
  while the default is 2% of the window with no cap (`:140-149`). So for any context window over 500,000 tokens an
  explicit value can only lower the budget. Fix: "`skills.max_context_tokens` sets a different budget; explicit
  values are capped at 10,000 tokens".
- **opencode, "front-load it, because opencode shows all of it"** (`SKILL.md:191`). The reason does not support the
  action: if the whole description reaches the model, opencode gives no reason to front-load. The supported reason is
  the clients that cut (omp at 99, Codex at 1,024 in code). Fix: "… and front-load it for clients that cut (omp at 99);
  opencode itself shows all of it".

Minor (fixable, not breaks):
- **Gemini CLI, "Keep name + description near 100 words"** (`SKILL.md:189`). `gemini-bp.md:24` is a size estimate
  inside a three-level progressive-disclosure list ("Always in context (~100 words)"), not an instruction. The cell
  turns an estimate into a rule. "Past the threshold: Nothing is cut" is a code reading (`gem-skillLoader.ts:211`
  `description: frontmatter.description,`; `gem-snippets.ts:320`; no slice on the description in either file), which
  holds, but the cell does not say it is code in a column headed by a documented threshold. Fix: "The page sizes
  metadata at ~100 words (an estimate, not a limit); the loader passes the description whole (code at `451a02ff`)".
- **Claude Code, "keep the entry under 1,536 characters"** (`SKILL.md:185`). Supported by `cc-skills.md:389,1213`, but
  under-qualified: the same vendor's best practices say "Maximum 1,024 characters" (S019, `best-practices.md:160`,
  recorded at `frontmatter-rule-authorities-round48.md:44`), its packager refuses 1,025 (same row), and Codex cuts at
  1,024. A 1,025–1,536-character description passes this row and fails those. The floor two paragraphs above
  (`SKILL.md:177`) softens this. Fix: "keep `description` ≤1,024 (floor) and `description` + `when_to_use` under 1,536".
- **Cursor, "move detail into `references/` rather than the body"**. Supported by `cursor-skills.md:269` ("Keep your
  main `SKILL.md` focused and move detailed reference material to separate files"), but no SOURCES row cites that page
  (`grep -n 'cursor.com/docs/skills' corpus/SOURCES.md` → no match) and the table's basis line names only S053–S059,
  S062–S064. A provenance gap, not a wrong statement.

Cells checked and holding: Claude Code past-threshold (`cc-skills.md:1207` "drops descriptions starting with the
skills you invoke least"; `:1213` "regardless of budget"; changelog `:6409` "raised the listing cap from 250 to 1,536
characters and added a startup warning"; default `0.01` at `cc-settings.md:2461`); Codex past-threshold and action
(`codex-build.md:40-41`, `:46`, `:101-103` "Front-load the key use case and trigger words"); VS Code and Copilot CLI
rows (page-scoped negatives; both seats ran the three Q30 legs, `SrcVSCode.md:76-114`, `SrcCopilotCLI.md:91-102`);
opencode past-threshold (both trees, above).

## 4. Learning real versus re-stated — HOLDS (guard b is weaker than it reads)

Guards (a), (b), (c) pass (re-runs above). But guard (b) greps only `SKILL.md`. Claude Code's `1,536` and `1%` were
already in admitted entries (`git grep -F` at `e3371548` over `corpus/knowledge` and `SKILL.md`: `1,536` → 2 hits,
`sibling-overlap-census-round49.md:221`, `skill-selection-rules-round50.md:48`; `1%` → 1 hit), so guard (b) counts a
re-statement as new ground. The `2%` hits there are unrelated (`99.92%`, `~72%`).

Stricter measure (a number absent from both `corpus/knowledge` and `SKILL.md` at the plan commit), per client:

| client | counted number | in knowledge + SKILL.md at `e3371548` | new to admitted knowledge? |
|---|---|---|---|
| Claude Code | 1,536 / 1% | 2 / 1 | no (re-stated; adds S062 history and the two settings, `skillListingMaxDescChars` 0 hits) |
| Codex | 2% / 8,000; 10,000 | 0 (unrelated `2%` only) / 0; 0 | yes (before: SOURCES and lesson Gates only) |
| VS Code | 1024 | in the floor (`SKILL.md:177`) | no |
| Copilot CLI | 1024 on the skill frontmatter row | `Max 1024` 0 | yes (the lane held only a plugin-manifest cap, S028) |
| Gemini CLI | ~100 words | `100 words` 0 (SOURCES S029 only) | yes |
| Cursor | 1,024 `/skills` warning | `yellow warning` 0; no prior hold (`ScoutPriorHolds.md` B) | yes |
| opencode | 1-1024 | in the floor | no (adds V2 non-enforcement, S064) |

Four clients are new on both counts (Codex, Copilot CLI, Gemini CLI, Cursor), so the learning is real at the
claimed size, not saturated by prior holds. The learning the round found and then dropped is the Copilot CLI
changelog limit and the Codex code cut (§ 2).

## 5. Harm — HOLDS; headroom is a tradeoff

- Line budget: `SKILL.md` 593 (`e3371548`) → 552 (`7ad05d34`) → 585 (`bf65974c`) → 599 (`5a097e12`, tip); the executed
  box passes at 599 of 600. Nothing fails today. The cost moves to the next round: any added `SKILL.md` line must
  first remove one, or `trigger.line_budget` fails. A tradeoff for the judge, not a defect.
- Row length: rows are 241–578 characters (`awk` over `SKILL.md:185-191`: 578, 494, 287, 241, 371, 310, 412). The
  file already carries longer lines (`:177` 763, `:106` 599), so this is house style. Part of the length is
  provenance and history that the entry already holds — `v2.1.105 raised the cap from 250`, `(v1.19.4
  skill/index.ts:332, v2.1.3 skill/instructions.ts:21)`, `(skills-best-practices.md:24-25)` — against the compression
  rule "one authoritative home per fact" (`SKILL.md:213`). Trimming those would shorten rows with no line cost.
- No other axis falls: the counter and `verify_surfaces.py` are unchanged (`git diff --stat` empty, exit 0); the
  table agrees with the measured opencode render (`SKILL.md:106`, `:164-165`) and does not revive omp truncation-era
  figures.

## What the judge should weigh

- C1 meets its counter and all three erratum-3 guards, and the learning is real (four clients new on the stricter
  measure). Depth credit stands.
- Before admission, fix the three over-wide cells (Cursor "not cut", Codex "raises", opencode's reason). Each is a
  wording change inside an existing row (0 lines).
- The Codex 1,024 code cut is an admitted, still-live counterexample to the table's framing. At minimum the entry's
  "Relation to what the lane already held" and the Codex row should name it; tabling it needs a pinned SOURCES row.
