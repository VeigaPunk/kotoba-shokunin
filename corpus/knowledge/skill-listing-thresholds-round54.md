# Skill `description` thresholds by client (round 54)

What seven clients' own documentation says about how much of a skill's `description` reaches the model
or is accepted: an authoring maximum, a per-entry cut in the skill listing, or a listing budget, and what
happens past it. Every row quotes a page opened on 2026-10-22 in round 54 (`../SOURCES.md` S053–S059,
S062–S064; fetch records in `../lessons/round-54.md` § Gate; seat reports
`../../.ufo/waves/round-54/build/Src*.md`). These are documentation statements, not measured client
behaviour, except where a row names shipped source that a seat read.

Frontier row: *Per-render consumption* (`../README.md` § Frontier), offer-render half. The per-session
offer→activation join stays unheld.

## Findings

1. **An authoring maximum is not a render cut.** Four clients document 1,024 characters for `description`
   (VS Code S055, Copilot CLI S056, Cursor S058, opencode S059 as `1-1024`). None of their pages documents a
   cut at that number. Cursor warns and still loads the skill (S058). opencode's shipped trees enforce
   nothing: v1.19.4 `packages/opencode/src/skill/index.ts:39,53-57` accepts any string and `:332,344` print it whole,
   and its V2 page says V2 enforces no maximum description length (S064) — seat `Srcopencode` read both tags.
2. **Two clients cut or budget the listing, and they do it differently.** Claude Code truncates each
   listing entry (`description` + `when_to_use`) at 1,536 characters (S053; the cap was 250 before
   v2.1.105, which added a startup warning, S062) and, past a listing budget of 1% of the context window,
   drops descriptions while keeping every name (S053 `skills.md:1207`). Codex budgets the whole initial list
   at 2% of the context window, or 8,000 characters when the window is unknown, shortens descriptions first
   and may then omit skills with a warning (S054); `skills.max_context_tokens` raises it, capped at 10,000
   tokens (S063).
3. **Gemini CLI gives a size, not a limit:** name plus description are always in context at "~100 words"
   (S057); seat `SrcGeminiCLI` read the loader at `451a02ff` and found no cut. The docs host now carries a
   banner saying Gemini CLI was replaced by Antigravity CLI on 2026-06-18 (seat `ScribeS046Fix`, site chrome
   only), so the recheck cadence for S057 should be short.
4. omp (not one of the seven) cuts at offset 99 unless a cached one-liner exists; opencode renders the full
   description (`../../SKILL.md` § Router model; `render-mechanism-round7.md`). So the tightest documented
   or measured cut on this host's two harnesses is omp's 99 characters, far below any documented maximum.

## Per-client record

| client | row | quote | location | reading |
|---|---|---|---|---|
| Claude Code | S053 | "the combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing" | `skills.md:389`, § Frontmatter reference, `description` row | A per-entry listing cut, not an authoring maximum and not the budget: the page puts the 1,536-character limit inside the skill listing and names no frontmatter limit for `description`, so past it the entry is truncated (the changelog records a startup warning) while the listing still carries every skill name (`:1207`). |
| Codex | S054 | "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" | build-skills.md:38-39 (past-it md:40-41; scope md:46) | A listing budget over the whole initial skills list, not an authoring maximum on one description and not a documented per-entry cut: past it Codex shortens skill descriptions first and, for large skill sets, may omit skills from the initial list with a warning, while the full SKILL.md still loads once the skill is selected. |
| VS Code | S055 | "help Copilot decide when to load the skill. Maximum 1024 characters." | `agent-skills.md:148` | An authoring maximum: the page states a `description` maximum of 1024 characters and no consequence, cut or budget past it. |
| Copilot CLI | S056 | "What the skill does and when to use it. Max 1024 characters." | `cli-command-reference.md:1274` | Authoring maximum: the frontmatter table caps a skill description at 1024 characters, and the page states no behaviour past the cap. |
| Gemini CLI | S057 | "Metadata (name + description): Always in context (~100 words)." | `skills-best-practices.md:24` | A soft per-skill listing budget, not an authoring maximum or a per-entry cut: the metadata is always in context at about 100 words, and past it the client documents nothing — the description reaches the prompt whole (no truncation at `skillLoader.ts:211` or `snippets.ts:320`, commit `451a02ff`), so the cost is context tokens. |
| Cursor | S058 | "Warnings cover a name over 64 characters or not in lowercase-hyphen form, a frontmatter `name` that doesn't match the folder, a description over 1,024 characters" | `release-notes.md:122` | Authoring maximum, not a listing cut: the release notes place it in the `/skills` warning set, so an over-length description still loads and no truncation, shortening, drop or refusal is documented. |
| opencode | S059 | "`description` must be 1-1024 characters." | `skills.md:72` | An authoring maximum, not a listing cut and not a budget: the page states the number under Follow length rules and documents no consequence past it, neither shipped tree enforces it, and V2's own page says V2 enforces no maximum description length, so an over-long description is rendered whole rather than cut, shortened or refused. |

## Relation to what the lane already held

- Claude Code's 1,536-character cut and 1% budget were already recorded in
  `sibling-overlap-census-round49.md:155,221` and `skill-selection-rules-round50.md:48` (from S022); this
  entry re-opens the page, adds the 250 → 1,536 history and the warning (S062), and puts the number into a
  `SKILL.md` decision table. It confirms, and does not replace, those entries.
- The 1,024 maximum was already in `SKILL.md`'s portability floor (S018, S019) and
  `frontmatter-rule-authorities-round48.md`; the new content is which clients restate it and that none of
  them documents a cut at it, with opencode shown not to enforce it.
- Codex's 2% / 8,000 numbers were only in SOURCES rows S013/S021 before; they are held here for the first
  time in an entry.

## Limits

`../../verifiers/check_description_thresholds.py` checks that a `SKILL.md` table row and an entry row exist
per client, that the quote holds the same number token, is recorded in the round-54 Gate, and comes from a
tier-A `mined` SOURCES row dated 2026-10-22 on a pinned host. It does not check that the number is about
`description`, that the page is vendor documentation, or that the row was opened this round (rows from
rounds 48–53 carry the same date); those are reviewer judgment (`../../plans/round-54.md` erratum 3).
No client was run; "nothing is cut" for Gemini CLI and opencode comes from reading source, not from a run.
