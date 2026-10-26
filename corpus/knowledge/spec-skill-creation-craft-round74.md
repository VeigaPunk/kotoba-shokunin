source: S223 — Agent Skills — Best practices for skill creators — https://agentskills.io/skill-creation/best-practices.md — § Calibrating control → § Match specificity to fragility (snapshot `best-practices.md:96`); also § Spending context wisely (`:48`), § Provide defaults, not menus (`:127`), § Favor procedures over declarations (`:145`), § Validation loops (`:229`) — located quote "Match the specificity of your instructions to the fragility of the task."
source: S225 — Agent Skills — Using scripts in skills — https://agentskills.io/skill-creation/using-scripts.md — § One-off commands (snapshot `using-scripts.md:13`); § Referencing scripts from `SKILL.md` (`:94`), § Self-contained scripts (`:127`), § Designing scripts for agentic use (`:231`) — located quote "When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory."
source: S224 — Agent Skills — Quickstart — https://agentskills.io/skill-creation/quickstart.md — § Create the skill (snapshot `quickstart.md:21`); § How it works (`:64`) — located quote "VS Code looks for skills in `.agents/skills/` by default."
verified-at: 2026-10-25
recheck: 30d — from the lane root, `for pair in 'best-practices|references/api-errors.md' 'best-practices|python scripts/migrate.py --verify --backup' 'best-practices|references/schema.yaml' 'using-scripts|uvx ruff@0.8.0 check .' "using-scripts|pipx run 'black==24.10.0' ." 'using-scripts|npx package@version' 'quickstart|.agents/skills/roll-dice/SKILL.md' 'quickstart|/skills'; do p=${pair%%|*}; t=${pair#*|}; printf '%-15s %-44s %s\n' "$p" "$t" "$(grep -c -F -- "$t" .ufo/waves/round-74/snapshots/$p.md)"; done` prints eight per-token counts in that order — `1 1 1 1 1 1 3 4` on 2026-10-25; any 0 means the page moved or the fetch failed, which is a re-open of the page and never a silent pass
ground: the lane held no row for any of the three pages at base `1e03d19` — `grep -nE 'agentskills\.io/skill-creation/(best-practices|using-scripts|quickstart)' corpus/SOURCES.md` printed nothing and `rows=0` (`.ufo/waves/round-74/receipts/base-sweeps.txt`), and the phrase sweep for `calibrating control`, `defaults, not menus`, `favor procedures`, `fragility of the task`, `one-off commands`, `pipx run`, `uvx ruff` over `corpus SKILL.md PROVINCE.md` printed `hits=0` (same receipt).

# The specification's own skill-creation guides: body craft, scripts, and the tutorial's default root

The specification ships three authoring guides beside the format page, and this lane did not hold any of
them: 0 rows and 0 phrase hits at base, above. All three were opened on 2026-10-25 over the `.md` route
(HTTP 200: `best-practices.md` 15 060 B sha256 `ab9f3b60…`, `using-scripts.md` 12 078 B sha256
`2cd77271…`, `quickstart.md` 4 080 B sha256 `7c480b44…`; `wc -lc` over the three gives 277/304/83 lines
and 31 218 B total). Each line number below is a line of the corresponding snapshot, and every quoted
sentence is a literal substring of those fetched bytes (whitespace collapse only, no other shaping).

## The body half — best practices (S223)

The page's organising claim is that prescriptiveness is not one dial for a whole skill: "Not every part of
a skill needs the same level of prescriptiveness. Match the specificity of your instructions to the
fragility of the task." (`best-practices.md:96`). What follows is checkable:

- **Freedom vs. the pinned command.** Give the agent freedom and explain *why* where several approaches
  work (`:96-108`); be prescriptive where the step is fragile, and then write the command and the
  prohibition together — **Be prescriptive** when operations are fragile (`:111`), `python scripts/migrate.py
  --verify --backup` (`:119`), "Do not modify the command or add additional flags." (`:122`).
- **A default, not a menu.** "When multiple tools or approaches could work, pick a default and mention
  alternatives briefly rather than presenting them as equal options." (`:129`).
- **A procedure, not a declaration.** "A skill should teach the agent *how to approach* a class of
  problems, not *what to produce* for a specific instance." (`:147`); the page's own contrast pairs a
  one-off SQL answer with a reusable four-step method (`:149`-`:159`).
- **Spend the context window deliberately.** Add what the agent lacks (`:52`), ask "Would the agent get
  this wrong without this instruction?" of each piece (`:78`), aim for moderate detail (`:84`), and
  structure large skills by progressive disclosure: keep `SKILL.md` under 500 lines and 5,000 tokens and
  move reference material to `references/`, each file attached to the condition that loads it
  (`:90`-`:92`).
- **Patterns that carry the body.** Gotchas as the highest-value content (`:167`-`:183`), templates for
  output format (`:189`), checklists (`:214`), validation loops — "Instruct the agent to validate its own
  work before moving on." (`:231`) — and plan-validate-execute for batch or destructive work (`:247`-`:249`).

## The script half — using scripts (S225)

This is the only one of the three pages about the deterministic half of a skill: commands and bundled
executables (`using-scripts.md:9`). Its first rule is subtraction: "When an existing package already does
what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/`
directory." (`:13`). The page then names a per-ecosystem runner — `uvx ruff@0.8.0 check .` (`:20`), `pipx
run 'black==24.10.0' .` (`:32`), `npx eslint@9 --fix .` (`:44`), `bunx` (`:52`), `deno run` (`:64`),
`go run` (`:76`) — and gives the three tips that turn a one-off into a rule: pin versions (`:50`, `:90`),
state prerequisites in the body rather than assuming the environment (`:91`), and "Move complex commands
into scripts." (`:92`).

- **Reference bundled files by relative path from the skill directory root** (`:96`), listing them so the
  agent knows they exist (`:98`).
- **Self-contained scripts declare their own dependencies inline** (`:127`): PEP 723 `# /// script` blocks
  (`:135`-`:142`) run with `uv run scripts/extract.py` (`:153`), pinned with PEP 508 specifiers and `uv lock --script`
  (`:158`-`:160`); Deno, Bun and Ruby get the same treatment (`:162`-`:229`).
- **Design the interface for an agent caller** (`:231`). The one stated as a hard requirement is
  non-interactivity: "This is a hard requirement of the agent execution environment." (`:237`). Then
  `--help` as the interface an agent reads (`:252`), error messages that say what to try (`:273`),
  structured output (`:284`), data on stdout and diagnostics on stderr (`:295`), and the closing list:
  idempotency, input constraints, `--dry-run`, meaningful exit codes, safe defaults, predictable output
  size (`:299`-`:304`).

## The tutorial's worked instance — quickstart (S224)

The quickstart is the pages' only complete example, and it is small enough to state as a rule. A skill is
a folder with a `SKILL.md` in it, and "VS Code looks for skills in `.agents/skills/` by default."
(`quickstart.md:21`); the worked file sits at `.agents/skills/roll-dice/SKILL.md` (`:23`), carries only
`name` and `description` (`:46`-`:47`), and is "one file, under 20 lines" (`:44`). The description is the
whole trigger surface: "Roll dice using a random number generator. Use when asked to roll a die (d6, d20,
etc.), roll dice, or generate a random dice roll." (`:26`). Verification is explicit — list with `/skills`
and fix the path if the name is missing (`:55`) — and the page explains discovery, activation and
execution as three steps (`:64`-`:74`). It also bounds portability, in its own words: "The same skill
works in any compatible agent, including Claude Code and OpenAI Codex." (`:17`).

Two cautions the page states are worth keeping verbatim in behaviour: "Tool-use reliability varies across
models" (`:62`), so a silent miss is not always a description defect; and the tutorial's own client is VS
Code with GitHub Copilot (`:13`), so `.agents/skills/` there is *this* client's default, not a
client-neutral format rule.

## The three pages as one rule table

One row per page, one rule per page: the page's own advice, with the two tokens an author can grep for and
the action it implies.

| page | S id | rule | quote | tokens | action |
|---|---|---|---|---|---|
| best-practices | S223 | Prescriptiveness is per part: grade each instruction by how fragile its step is, not by taste; name a default rather than a menu | "Match the specificity of your instructions to the fragility of the task." | `references/api-errors.md`; `python scripts/migrate.py --verify --backup`; `references/schema.yaml` | give the agent freedom and say why where several approaches work, and pin the exact command plus its prohibition where the step is fragile |
| using-scripts | S225 | Reference an existing package before bundling a script, pin the version, and write the script's interface for an agent caller | "When an existing package already does what you need, you can reference it directly in your `SKILL.md` instructions without a `scripts/` directory." | `uvx ruff@0.8.0 check .`; `pipx run 'black==24.10.0' .`; `npx package@version` | reach for the tool with an explicit version first, state the prerequisite in the body, and move a command into a tested script only once it is too complex to get right first try |
| quickstart | S224 | The tutorial's minimal shape: one `SKILL.md` in the project's `.agents/skills/` tree, name plus description only, under twenty lines | "VS Code looks for skills in `.agents/skills/` by default." | `.agents/skills/roll-dice/SKILL.md`; `.agents/skills/`; `/skills` | place the first skill in that tree, keep it under twenty lines, and confirm the name with `/skills` before trusting the path |

## What a skill author does with this

- **Calibrate per section, not per skill.** Write the fragile steps as a pinned command plus the
  prohibition; write the flexible ones as an approach with the reason attached (S223, `:96`-`:122`).
- **Subtract before you bundle.** Name the existing tool with an explicit version before writing a script,
  and state the prerequisite the agent's environment must already meet (S225, `:13`, `:90`-`:92`).
- **Write the script for a machine caller.** No prompts, `--help`, structured data on stdout, diagnostics
  on stderr, distinct exit codes (S225, `:237`-`:304`).
- **Start from the tutorial's shape.** One `SKILL.md` under the project's `.agents/skills/` tree, name plus a
  capability-then-contexts description, under twenty lines, confirmed by listing the skills (S224,
  `:21`-`:55`).

## Limits

- **Documentary evidence only.** Three pages were fetched and read; no client was installed, loaded or run,
  and no claim here is about observed harness behaviour.
- **A rule is the page's advice, not a Must, unless the page says Must.** From the lane root,
  `for p in best-practices using-scripts quickstart; do printf '%s must=%s hard=%s\n' $p "$(grep -c -iE '\bmust\b' .ufo/waves/round-74/snapshots/$p.md)" "$(grep -c -F 'hard requirement' .ufo/waves/round-74/snapshots/$p.md)"; done`
  prints `best-practices must=2 hard=0`, `using-scripts must=1 hard=1`, `quickstart must=1 hard=0` (run
  2026-10-25). The only hard requirement any of the three states is using-scripts' non-interactivity rule
  (`using-scripts.md:237`); two of the four `must` hits sit inside examples (a SQL convention at
  `best-practices.md:174`, an error string at `using-scripts.md:278`) and the other two are guidance
  sentences (`best-practices.md:111`, `quickstart.md:46`), not format rules.
- **Not checked:** the other client pages (the lane's pinned seven, and the sibling specification pages
  `evaluating-skills` S212 and `optimizing-descriptions` S213), the specification page itself, and whether
  any client actually applies these rules. This entry stops at what the three pages say.
- **The tutorial's root is one client's default.** `.agents/skills/` is stated for VS Code with GitHub
  Copilot (`quickstart.md:13`, `:21`); the portability sentence (`:17`) says other compatible agents read
  the same folder, so the root is treated here as the tutorial's taught default, not as a format rule.
- **Quotes are literal substrings of the fetched `.md` bytes** (the snapshot sha256s above match this
  seat's own fetches), compared after whitespace collapse only; nothing here is `byte-exact` against the
  rendered HTML page, which was not fetched as HTML.
- **Line numbers drift.** Every citation is to the 2026-10-25 snapshot, not to a current URL: the page can
  change without the URL changing, which is why the recheck line counts tokens instead of trusting the URL.

## Scope

Prompt-and-skill craft: how a skill body is written — detail, prescriptiveness, scripts, and the minimal
working shape a specification tutorial demonstrates. Not: a client's discovery or trust behaviour
(`corpus/knowledge/client-trust-gates-round68.md`, `corpus/knowledge/skill-name-precedence-round69.md`),
the description-writing and trigger-eval rules the specification states on its own `optimizing-descriptions`
page (S213), or an evaluation of any skill's output quality (S212, and kengaku's ground).

## Related

- `corpus/knowledge/skill-listing-thresholds-round54.md` — what each client keeps in context before the
  body loads; this entry starts where that threshold ends.
- `corpus/knowledge/client-trust-gates-round68.md` — what a client does with a body it did not place.
- `corpus/knowledge/skill-eval-artefacts-round70.md` — the specification's evaluation and description
  pages (S209, S212, S213), the siblings this entry does not re-open.
