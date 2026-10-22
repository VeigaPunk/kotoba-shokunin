Result: DONE — Cursor's current docs, help FAQ, CLI page, CLI changelog and Bugbot page document AGENTS.md at project root plus subdirectories, CLAUDE.md read natively and always applied, legacy `.cursorrules`, no file-inlining import for rule text, no Agent rule size cap (only a 500-line guideline and separate Bugbot character caps), and nothing about dated or transient content; the GEMINI.md and symlink negatives carry the Q30 three-leg sweep.

Seat: `KotobaR53.ScribeCursor` (scribe, leaf). Lane `kotoba-shokunin`, base `e78dff667237fba2e3cf9eccb802eff5bc9ea302`, plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36`. This seat opened sources and wrote this report only. It did not run `verifiers/check_alwayson_boxes.py`, wrote no instrument, edited no lane file, and installed no tool. Scratch fetches live under `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/` (outside the lane).

## What this seat measured

Read-only web fetch with `curl` of Cursor's published documentation, its docs index, its two markdown changelog surfaces, and its old routes. Every admitted page was fetched twice (a first read and a timed gate fetch); the admitted five were byte-identical across the two fetches. No browser, no bot-challenge workaround, no model call.

Retrieved pages total: 281 documentation pages enumerated from `https://cursor.com/llms.txt` (the site's own "Overview of all docs pages" link at `rules.md:399`), all HTTP 200, 279 served as `text/markdown` and 2 as HTML application shells (`changelog.md`, `enterprise/deployment-patterns.md`). The per-page URL/status/sha256 manifest is at `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/pages/manifest.tsv`.

## Answers for Cursor (the five questions)

### 1. Which always-on file names it reads

- `AGENTS.md` — root and any subdirectory. `docs/rules.md:321` "Cursor supports AGENTS.md in the project root and subdirectories." Nested files: `rules.md:357` "Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence."
- `CLAUDE.md` — root. `help/customization/rules.md:97` "Cursor reads `CLAUDE.md` files the same way it reads `AGENTS.md`." and `:99` "`CLAUDE.md` files are always applied to every conversation, regardless of any `alwaysApply` frontmatter setting."
- Both names, CLI form: `docs/cli/using.md:40-41` "The CLI also reads `AGENTS.md` and `CLAUDE.md` at the project root (if present) and applies them as rules alongside `.cursor/rules`."
- `.cursor/rules/*.mdc` — project rules; `rules.md:42` "A plain `.md` file in `.cursor/rules` is ignored by the rules system". `rules.md:32` keeps `.mdc` as the project-rule form.
- Legacy `.cursorrules` — `help/customization/rules.md:88` "The `.cursorrules` file in your project root is legacy and will be deprecated." The page gives a migration that recreates it as an Always Apply rule (`:92` "this matches the old behavior"); it does not state the current precedence of `.cursorrules` against `AGENTS.md`.
- User rules `~/.cursor/rules` and account/team rules (`help:70-71`); these are not project-directory files.
- `GEMINI.md` — not documented anywhere. Sweep in the Q30 section below.

Documentation inconsistency worth recording: the rules reference page lists "four types of rules" (`rules.md:5`) and does not mention `CLAUDE.md` at all, while the help FAQ (`:95-99`) and the CLI page (`:40-41`) document it. A passage that attributes `CLAUDE.md` reading to Cursor must cite the help or CLI page, not the rules reference.

### 2. What happens when two of them exist in one directory

Both are read; no arbitration between `AGENTS.md` and `CLAUDE.md` is documented. The CLI sentence above says it reads `AGENTS.md` and `CLAUDE.md` "and applies them as rules alongside `.cursor/rules`" (`using.md:40-41`), and the help page says `CLAUDE.md` is read "the same way" and "always applied" (`:97`, `:99`). The only precedence statements on these pages are about other axes:

- Rule sources: `rules.md:307` "Rules are applied in this order: **Team Rules → Project Rules → User Rules**" (repeated `help:82`).
- Nesting: `rules.md:357` (quoted above), more specific `AGENTS.md` wins over parent.
- Identical filenames in different folders: `help:103` "There are no conflicts or overrides based on filename." (`:101-103` says rules are identified by full file path and two same-named rules both apply).

So a directory carrying `AGENTS.md` and `CLAUDE.md` is documented as additive, not as a conflict Cursor resolves by picking one. No page states an order between those two names.

### 3. Whether it honours a redirect

- `@AGENTS.md` import: not documented, and the documented `@` semantics are the opposite of inlining. `rules.md:127` "A file mention like `@migration-template.sql` tells Agent where to look, and Agent reads the file with its tools" and "The file's contents are not inlined into the prompt". Repeated in the FAQ at `rules.md:375`. The rule body is what reaches the model: `rules.md:127` ends "Put anything that must always be in context directly in the rule body."
- Repository import: `rules.md:313` "Rules aren't imported on their own." The page routes bundling through a plugin marketplace (`:313`).
- Symlink: not documented for rule files or `AGENTS.md`. The nearest statements are elsewhere: `docs/cli/changelog.md:299` "The skills menu follows symlinked directories when discovering skills." and `docs/plugins.md:336` restricts plugin-directory symlinks. Neither covers rule files.
- Config pointing at another name: no such key found. `docs/cli/reference/configuration.md` has no rule-path option; the only alternate-name levers documented are the fixed user/team locations (`help:70-71`) and the self-hosted pool page's `.mdc` under `.cursor/rules` inside `--worker-dir`, where "The filename is arbitrary" (`docs/cloud-agent/self-hosted/pool.md:197`).
- Separate consumer: Bugbot does document linked rule files, but in its own tree and with its own caps, and it excludes project rules — `docs/bugbot.md:457` "(`*.mdc` files in `.cursor/rules/`) do not apply to Bugbot runs", and `:434` counts "Every `.md` or `.mdc` file linked from a `.cursor/BUGBOT.md` file" as its own rule.

### 4. Any documented size limit

- No character or byte cap for Agent rules or `AGENTS.md` is documented. The only size statement is a guideline: `rules.md:155` "Keep rules under 500 lines" and `help:55` "Keep rules under 500 lines. Split large rules into smaller, focused files." The cloud-agent page gives advice, not a bound: `docs/cloud-agent/setup.md:184` "If this section gets large, we recommend including references to other files".
- A real cap exists for Bugbot review rules only: `docs/bugbot.md:434` "Each rule is truncated at 30,000 characters when included in a review." and "The combined rules Bugbot includes for a review are capped at 100,000 characters." Bugbot does not read `.cursor/rules` project rules (`:457`), so this cap does not bound the always-on files the checklist is about.

### 5. Anything about dated or transient content

Nothing directly. The word-level sweep found no rule about dates, expiries or transient facts in the rules reference, the help FAQ, the CLI page, the CLI changelog or the release notes. The nearest prose is a staleness rationale for referencing files instead of copying: `rules.md:160` "This keeps rules short and prevents them from becoming stale as code changes." Rules are framed as durable prompt context (`rules.md:26` "Rules provide persistent, reusable context at the prompt level."), but no page says dated text is forbidden or must move to a status file.

## Q30 sweep record (all three legs run for every negative above)

Leg 1, changelog or release notes (markdown routes, not the rendered HTML shell):
`curl -sS -L -w '%{http_code} %{size_download}' https://cursor.com/docs/release-notes.md` → `200 301193`; `https://cursor.com/docs/cli/changelog.md` → `200 56159`.
Counts: `grep -c 'CLAUDE\.md' release-notes.md` → `0` (exit 1); `grep -c 'GEMINI\.md'` → `0` (exit 1); same two counts on the CLI changelog → `0`, `0` (exit 1). The only `AGENTS.md` entry in the release notes is `:130`; in the CLI changelog it is `:25`.

Leg 2, current docs source tree: all 281 pages listed by `https://cursor.com/llms.txt` (the sitemap link the rules page itself prints at `:399`) were fetched at 2026-10-22T20:05:37Z; all returned 200.
- `grep -rl 'GEMINI\.md' .` → no output, exit 1 (0 of 281 pages).
- `grep -rl 'CLAUDE\.md' .` → `./73732bc0919c` = `docs/cli/using.md`, `./a8dcea1d6d93` = `help/customization/rules.md`, exit 0.
- `grep -rli 'cursorrules' .` → 1 page (`help/customization/rules.md`).
- `grep -rli 'symlink' .` → 5 pages, none about rule files: `cli/changelog.md` (skills), `plugins.md` (plugin dirs), `configuration/worktrees.md` (dependencies), `api/origin/changelog.md` (git symlink mode), `release-notes.md:656` (Bugbot symlink targets).
- `grep -rl '500 lines' .` → 2 pages (`docs/rules.md`, `help/customization/rules.md`).

Leg 3, lane corpus grep, run from `/home/vgpnk/Projects/shokunin/kotoba-shokunin`:
- `grep -rn "GEMINI\.md" corpus/ | wc -l` → `7`; every hit is about omp's own gemini class or opencode's loader, e.g. `corpus/knowledge/instruction-surface-census-round13.md:479`; none is a Cursor vendor statement.
- `grep -rn "CLAUDE\.md" corpus/ | wc -l` → `54`; the same, omp/opencode loader facts.
- `grep -rli "cursor" corpus/` → 3 files only (`instruction-surface-census-round13.md`, `instruction-surface-remeasure-round13.md`, `README.md`); they describe omp's `cursor/rules` loader class, not what Cursor the product reads.

Conclusion recorded per Q30: Cursor documents nothing about `GEMINI.md` (three legs complete, so "not documented", not "not checked"); it documents nothing about symlink resolution for rule files; it documents no Agent rule size cap and no dated-content rule. The `@`-import negative is stronger than a sweep: the docs affirmatively state mentions are not inlined and rules are not imported (`rules.md:127`, `:313`).

## Gate record

Timed gate fetches, 2026-10-22. `curl -sS -L --max-time 60 -o body -w '%{http_code} %{size_download} %{content_type}'`.

| URL | UTC access | HTTP | bytes | sha256 | quote (≤25 words) | line |
|---|---|---|---|---|---|---|
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca161142c2f3f0e4ef66a732dd48119cb08bd0dc2ff73e693721546bc8 | "Cursor supports AGENTS.md in the project root and subdirectories." | 321 |
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca… | "Instructions from nested `AGENTS.md` files are combined with parent directories, with more specific instructions taking precedence." | 357 |
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca… | "Rules aren't imported on their own." | 313 |
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca… | "A file mention like `@migration-template.sql` tells Agent where to look, and Agent reads the file with its tools" | 127 |
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca… | "Keep rules under 500 lines" | 155 |
| https://cursor.com/docs/rules.md | 2026-10-22T20:09:33Z | 200 | 17,403 | 884c67ca… | "This keeps rules short and prevents them from becoming stale as code changes." | 160 |
| https://cursor.com/help/customization/rules.md | 2026-10-22T20:09:33Z | 200 | 6,285 | c6d2b0697e0b8f51d0d9ad7701a850cd81c389ec075e24b15e24bbd4e5afcdfc | "Cursor reads `CLAUDE.md` files the same way it reads `AGENTS.md`." | 97 |
| https://cursor.com/help/customization/rules.md | 2026-10-22T20:09:33Z | 200 | 6,285 | c6d2b069… | "`CLAUDE.md` files are always applied to every conversation, regardless of any `alwaysApply` frontmatter setting." | 99 |
| https://cursor.com/help/customization/rules.md | 2026-10-22T20:09:33Z | 200 | 6,285 | c6d2b069… | "The `.cursorrules` file in your project root is legacy and will be deprecated." | 88 |
| https://cursor.com/help/customization/rules.md | 2026-10-22T20:09:33Z | 200 | 6,285 | c6d2b069… | "There are no conflicts or overrides based on filename." | 103 |
| https://cursor.com/docs/cli/using.md | 2026-10-22T20:09:33Z | 200 | 5,771 | b070cb1f882dd8e8b9ab7434ff6f96fe1f181c4907ee242773ae6bbbedb47b0b | "The CLI also reads `AGENTS.md` and `CLAUDE.md` at the project root (if present) and applies them as rules alongside `.cursor/rules`." | 40-41 |
| https://cursor.com/docs/cli/changelog.md | 2026-10-22T20:09:33Z | 200 | 56,159 | 70d57616d76ddfa089d42b23a149fad68436ecd8711a94b33c13c3c64795167b | "The skills menu follows symlinked directories when discovering skills." | 299 |
| https://cursor.com/docs/cli/changelog.md | 2026-10-22T20:09:33Z | 200 | 56,159 | 70d57616… | "`.cursor/rules` and `.cursor/skills` in subdirectories are discovered everywhere, matching the IDE." | 366 |
| https://cursor.com/docs/bugbot.md | 2026-10-22T20:11:14Z | 200 | 39,369 | 39fe4c9643ae79b0fbb4f740a82bc2e8756f807b262b71dc1b39302978410106 | "Each rule is truncated at 30,000 characters when included in a review." | 434 |
| https://cursor.com/docs/bugbot.md | 2026-10-22T20:11:14Z | 200 | 39,369 | 39fe4c96… | "The combined rules Bugbot includes for a review are capped at 100,000 characters." | 434 |
| https://cursor.com/docs/bugbot.md | 2026-10-22T20:11:14Z | 200 | 39,369 | 39fe4c96… | "(`*.mdc` files in `.cursor/rules/`) do not apply to Bugbot runs" | 457 |
| https://cursor.com/docs/release-notes.md | 2026-10-22T20:09:33Z | 200 | 301,193 | fd4d830aa5b02cd79d4c3ac485eb01d31ebb7436f152e27496e7cb02a23d82cd | "untracked rules, skills, or `AGENTS.md` files an earlier agent may have left there" | 130 |
| https://cursor.com/llms.txt | 2026-10-22T20:09:33Z | 200 | 24,815 | 38cc4995af1037fea4daa16f4b2ed1062a4c21df63440e5703608eec1017085d | "# Cursor Documentation" (index header; source of the 281-page sweep list) | 1 |

Stability (Q10): each URL above was fetched once during the sweep and once in the gate run; `sha256sum` of both copies matched for every one. The two fetch times are 2026-10-22T20:05:37Z (sweep) and 2026-10-22T20:09:33Z (gate), so no admitted page moved during the measurement.

## SOURCES rows to append (exact column shape; `S0xx` left for the next free number)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S0xx | Cursor Docs — Rules — https://cursor.com/docs/rules.md | docs | A | Which always-on rule files Cursor Agent reads, how nested files combine, and what an `@`-mention in a rule does | § Project rules (`rules.md:32,42`), § Importing rules from a repository (`:311-313`), § Referencing files from a rule (`:127`), § Best practices (`:155,160`), § Team Rules precedence (`:307`), § AGENTS.md (`:317,321,342,357`), § FAQ (`:375`); markdown route fetched 2026-10-22T20:09:33Z (17,403 B, sha256 `884c67ca…`) | AGENTS.md is read from the project root and any subdirectory with the more specific file winning, project rules must be `.mdc`, and an `@file` mention is a lazy tool read whose contents are not inlined, so a rule body cannot inline another file's text | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Cursor Docs — Rules help and FAQ — https://cursor.com/help/customization/rules.md | docs | A | Cursor's documented handling of CLAUDE.md, legacy `.cursorrules`, same-named rules in different folders, and rule length guidance | § What are good practices for writing rules? (`rules.md:53-58`), § How do I migrate from .cursorrules? (`:86-93`), § How does CLAUDE.md work in Cursor? (`:95-99`), § How do rules with the same name in different folders work? (`:101-103`); fetched 2026-10-22T20:09:33Z (6,285 B, sha256 `c6d2b069…`) | Cursor reads `CLAUDE.md` the same way as `AGENTS.md` and always applies it regardless of frontmatter, `.cursorrules` is legacy and slated for deprecation, and rules are keyed by full path so no filename override exists | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Cursor Docs — Use Agent in CLI — https://cursor.com/docs/cli/using.md | docs | A | What the Cursor CLI reads at the project root alongside `.cursor/rules` | § Rules (`using.md:36-41`); fetched 2026-10-22T20:09:33Z (5,771 B, sha256 `b070cb1f…`) | The CLI reads both `AGENTS.md` and `CLAUDE.md` at the project root when present and applies them as rules alongside `.cursor/rules`, stating no order between the two names | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Cursor Docs — Cursor CLI changelog — https://cursor.com/docs/cli/changelog.md | docs | A | Release-note history for Cursor's rule and skill discovery, including nested directories and symlinks | § May 14, 2026 (`changelog.md:366`), § Skills found through symlinks (`:299`), § Self-hosted workers (`:25`); fetched 2026-10-22T20:09:33Z (56,159 B, sha256 `70d57616…`) | Cursor discovers `.cursor/rules` and `.cursor/skills` in subdirectories everywhere, and follows symlinked directories for skills only; no entry documents a rule-file symlink or a rule import | mined | 2026-10-22 | on-release | corpus/knowledge/alwayson-rule-files-round53.md |
| S0xx | Cursor Docs — Bugbot rules — https://cursor.com/docs/bugbot.md | docs | A | The one documented rule-size cap in Cursor's documentation, and which rule surfaces Bugbot does not read | § Rules → § Rule limits (`bugbot.md:432-434`), § Repository rules → § Project rules (`:457`); fetched 2026-10-22T20:11:14Z (39,369 B, sha256 `39fe4c96…`) | Bugbot truncates each review rule at 30,000 characters and caps a review's combined rules at 100,000 characters, and it does not read `.cursor/rules` project rules at all | mined | 2026-10-22 | 90d | corpus/knowledge/alwayson-rule-files-round53.md |

Precondition on the status cell: `mined` requires a citing path in `used-by`. `corpus/knowledge/alwayson-rule-files-round53.md` is absent at this seat's read time (`test -f` → exit 1), so the L1 must land that entry citing these rows, or drop the rows to `queued`; leaving `mined` with an uncited path would violate SOURCES rule 1 and Q12.

## Rejected and screened candidates

- `https://cursor.com/changelog` — 200, 204,106 B, `text/html`, sha256 `ccadc4b6…`. Rejected: the page is an application shell with navigation only; `grep -o -i -E ".{80}(AGENTS\.md|CLAUDE\.md|GEMINI\.md|cursorrules).{120}"` returned nothing, and no changelog entry text is server-rendered. Flip: a markdown or JSON route that exposes the entries.
- `https://cursor.com/changelog.md` — 200, 189,133 B, served as `text/html` (not markdown), same shell. Rejected for the same reason; it also moved one byte between the sweep fetch (189,132 B, sha256 `a9a14144…`) and the gate fetch (189,133 B, sha256 `eb9bc09a…`), so it is not a stable citation.
- `https://cursor.com/docs/context/rules.md` — 404, 389 B, sha256 `4f98eb06…`. Old docs path; the live route is `https://cursor.com/docs/rules.md`. Rejected as a dead route (it must not be cited as the source).
- `https://cursor.com/docs/rules.mdx` — 404, 24,190 B HTML error shell. Rejected: no markdown source route exists at that name.
- `https://github.com/getcursor/docs` — 404, 265,673 B GitHub "Page not found". The once-public docs repository no longer exists, so it cannot serve as Q30's source tree; the tree leg used the published 281-page index instead.
- `https://cursor.com/docs/release-notes.md` — 200, 301,193 B, sha256 `fd4d830a…`. Screened, not admitted as a row: it carries exactly one `AGENTS.md` mention (`:130`, cloud-worker checkout reuse) and no rule-file rule; it is quoted in the Gate and used as the Q30 changelog leg, but it teaches no fact the five rows do not carry, and SOURCES rule 1 requires a quote that grounds `teaches`.
- `https://cursor.com/docs/cloud-agent/setup.md` — 200, 11,310 B. Has "Cloud agents read `AGENTS.md` files." (`:182`) and the size advice at `:184`; redundant with `rules.md` for the always-on question and its advice is not a rule. Screened out.
- `https://cursor.com/docs/customize-cursor.md` — 200, 5,200 B. Lists `AGENTS.md` as one rules mechanism (`:27`); repeats `rules.md` without new behaviour. Screened out.
- `https://cursor.com/docs.md` and `https://cursor.com/llms.txt` — index pages. `llms.txt` is the sweep manifest (Gate row above), not a source row: it carries no rule prose.

## Operability consequences for C2's boxes 04 and 07

- Box 04 (dated or transient text): Cursor supplies no vendor rule to cite. The only related sentence is a staleness rationale for referencing files (`rules.md:160`), not a prohibition on dates. An instrument or knowledge entry that attributes a dated-text ban to Cursor would be a Q23 misattribution; the authority for box 04 remains the lane's own checklist item (AC-4, `corpus/knowledge/alwayson-checklist-round7.md:16`).
- Box 07 (one canonical rule-file name or an explicit redirect): for this client the documented behaviour is multi-name native reading — `AGENTS.md` and `CLAUDE.md` are both read (`using.md:40-41`, `help:97`), a directory holding both is additive, and no import or symlink redirect is documented (`rules.md:313`, `:127`). A repository that keeps `AGENTS.md` as its single owner needs no `@AGENTS.md` line for Cursor; the box's "explicit redirect" branch has no Cursor-documented form. The only documented file-linking form belongs to a different consumer (Bugbot's `.cursor/BUGBOT.md`, `bugbot.md:434`).
- A C2 knowledge entry citing Cursor should cite `help/customization/rules.md` and `docs/cli/using.md` for `CLAUDE.md`, not `docs/rules.md`, which omits it from its four-type list.

## Limits and out-of-scope

- Measured surfaces only: Cursor's published markdown docs and its markdown changelog routes. The product binaries were not inspected; no statement here is a measurement of what a Cursor build actually loads.
- The rendered `cursor.com/changelog` page is client-rendered and could not be read as text; the markdown release notes were used in its place and that substitution is recorded above.
- Not done by this seat, by bounds: the Claude Code memory documentation (another seat), the always-on instrument, the `verifiers/check_alwayson_boxes.py` counter, any SOURCES or knowledge edit, any other client.
- No tool was installed or upgraded, so the tooling directive has no entry to record.

## Artifact paths

- This report: `.ufo/waves/round-53/build/ScribeCursor.md`
- Fetched bytes and manifests (scratch, not committed): `/fast/scratch/hyaku/kotoba-r53/ScribeCursor/fetch/gate.tsv`, `.../fetch/pages/manifest.tsv`, `.../fetch/pages/urlmap.tsv`, `.../fetch/urls-docs.txt`
