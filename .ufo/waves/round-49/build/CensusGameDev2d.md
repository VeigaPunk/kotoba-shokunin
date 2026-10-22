# C1 census row — game-dev-2d (kotoba round 49 build)

ROW | game-dev-2d | main (detached HEAD) | 7753d49b16674e122ed134403e7a9b301f2cbf7e | NONE | none | no | no | PROVINCE.md:3 | "Owns: 2D game production verified by executable headless fixtures — loop, input, physics, scenes, camera, UI, levels, juice, export readiness."

## Findings

1. **Pin.** `master` does not exist in this repo (`rc 128`); the default branch is `main`, and the
   checkout is a detached HEAD at the same commit `main` resolves to, so the pin is unambiguous:
   `7753d49b16674e122ed134403e7a9b301f2cbf7e`, branch `main` (detached). Worktree is clean, so the
   absence findings below are not dirty-tree artifacts.
2. **No skill file.** Zero `SKILL.md` at the pinned commit, no `skills/` or `skill/` directory. The
   lane is still in "shonen seed form": `README.md:12-13` says the file is "absent on lanes still in
   shonen seed form", and `SHONEN.md:5` keeps that promotion box unchecked. The frontmatter questions
   are therefore not applicable rather than negative: there is no frontmatter, so no `description`
   can name kotoba and no arbitration clause can live in one. `PROVINCE.md` has no `## Domain`
   heading; its domain statement is the `Owns:` line.
3. **Its own scope** (`PROVINCE.md:3`) is 2D game production under executable headless fixtures on
   Godot 4.7.2 (`Core`, line 14). Its `Refuses` line (line 10) lists: engine/editor source mutation,
   publishing/store submission, asset rights clearance (art-east-asian-design), harness/evidence
   auditing (harness-integrity, gate-evidence, rlm-dispatch), narrative canon. Its `Adjacent` block
   (lines 29-33) routes 3D to game-dev-3d, canon to lore, rights/visual direction to
   art-east-asian-design and generic harness audits to "their owning lanes" — it names **no** prompt
   or skill-craft lane, kotoba included.
4. **Classification: `none`.** Nothing at the pin claims to write or audit `SKILL.md`, prompts,
   `AGENTS.md` or frontmatter for any lane. Sweep over the pinned markdown: 171 matching lines in 115
   files, of which `frontmatter` 0, `kotoba` 3 (all fleet-census or peer-note references), and every
   `SKILL.md` / `AGENTS.md` / `prompt` hit is self-referential, parent-skill consumption, or unrelated
   engine prose (details in §Near touches). No file name in the tree contains `skill`, `prompt` or
   `agents` (0 matches), and no script mentions `SKILL.md`, `AGENTS.md` or `frontmatter` (0 lines
   outside markdown), so the lane has no prompt/skill instrument of its own; its 49 `verify_*` /
   `audit_*` scripts under `corpus/live/rNN-*` check battery rows.
5. **Near touches, judged not overlap.**
   - `reports/round-104/r104-scr5.md:70` reads a sibling lane's (`game-dev-3d`) `AGENTS.md` for a
     quiet-window check — "`AGENTS.md` there was read, not modified": lifecycle evidence, not
     prompt-craft authoring or auditing.
   - The 11 `SKILL.md` lines in 6 md files are: its own missing file (`README.md:12`, `SHONEN.md:5`),
     the **parent fleet skill** `/home/vgpnk/.kimi-code/skills/shokunin/SKILL.md:167-176` promotion-gate
     text (`reports/round-102/r102-scr5.md:12`, `round-103/r103-scr5.md:95`,
     `round-104/r104-scr5.md:170`), or its own promotion procedure. Consuming the parent skill, not
     owning craft over another lane's.
   - The 13 `prompt` lines are self-task references ("original prompt", "the dispatch prompt's …
     wording", "the census is a prompt, not a defect list") and pipe prose ("with a prompt reader").
6. **kotoba side (for the C1 after-count).** kotoba's `PROVINCE.md` § Adjacent names 10 of the 20
   sibling lanes and names `game-dev-2d` zero times at base `a5adc146`. This row is new material for
   the § Adjacent rewrite; do not present the lane as already listed.

## Evidence (run 2026-10-22; commands with exit codes)

Pin, at `/home/vgpnk/Projects/shokunin/game-dev-2d-shokunin`:

```
git rev-parse master                     -> "fatal: ambiguous argument 'master'"                       rc 128
git symbolic-ref -q HEAD                 -> "fatal: ref HEAD is not a symbolic ref"                    rc 128
git rev-parse HEAD                       -> 7753d49b16674e122ed134403e7a9b301f2cbf7e                    rc 0
git rev-parse main                       -> 7753d49b16674e122ed134403e7a9b301f2cbf7e                    rc 0
git rev-parse --verify '7753d49b…^{commit}' -> 7753d49b16674e122ed134403e7a9b301f2cbf7e                  rc 0
git branch -a                            -> "* (no branch)", main, remotes/origin/HEAD -> origin/main    rc 0
git diff --name-only HEAD | wc -l        -> 0  (clean worktree)
git ls-files -o --exclude-standard | wc -l -> 0 (no untracked file, so no stray SKILL.md)
```

Tree at `<C> = 7753d49b16674e122ed134403e7a9b301f2cbf7e`:

```
git ls-tree --name-only <C>
  -> LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md considerthese corpus reports
git ls-tree -r --name-only <C> | wc -l                                   -> 42568 files
git ls-tree --name-only <C> -- skills skill                              -> (no output)        rc 0
git ls-tree -r --name-only <C> | grep -E '^(skills?/[^/]+/)?SKILL\.md$'  -> (no output)        rc 1
git ls-tree -r --name-only <C> | grep -c 'SKILL\.md'                     -> 0                 rc 1
```

Blob provenance for the files quoted (git object ids, so the quotes can be re-read byte-exact):

```
git rev-parse <C>:PROVINCE.md -> d753cc009ed90658e3bfed65fc80a74931924d6c
git rev-parse <C>:README.md   -> da39e2ac534810bcd210c68c00cf6a6b98b2648e
git rev-parse <C>:SHONEN.md   -> acb96dade8f6f5904d65063e445d05a10eb5917b
git show <C>:PROVINCE.md | sed -n '3p'  -> reproduces the ROW quote verbatim (19 words)
git show <C>:PROVINCE.md | sed -n '10p' -> the Refuses line (harness/evidence auditing named there)
git show <C>:PROVINCE.md | sed -n '29,33p' -> ## Adjacent block: game-dev-3d, lore, art-east-asian-design
git show <C>:README.md   | sed -n '12,13p' -> "absent on lanes still in shonen seed form"
```

Sweep (Q14) over the pinned prose surface, `<C> -- '*.md'`:

```
git grep -l -E 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' <C> -- '*.md' | wc -l -> 115
git grep -h -E 'SKILL\.md|prompt|AGENTS\.md|frontmatter|trigger|description|kotoba' <C> -- '*.md' | wc -l -> 171
per token (files / lines), same invocation per token:
  trigger 72/118 · description 24/25 · prompt 13/13 · SKILL\.md 6/11 · AGENTS\.md 1/1 · frontmatter 0/0 · kotoba 3/3
git ls-tree -r --name-only <C> | grep -Eic '(skill|prompt|agents)'                       -> 0
git grep -h -E 'SKILL\.md|AGENTS\.md|frontmatter' <C> -- ':!*.md' | wc -l                -> 0
git ls-tree -r --name-only <C> | grep -Eic '/(verif|audit|check)[^/]*\.(py|sh)$'         -> 49
```

Counts that decide the two ROW flags (Q13: command + date 2026-10-22):

```
git show <C>:PROVINCE.md   | grep -c -i kotoba -> 0   rc 1
git show <C>:README.md     | grep -c -i kotoba -> 0   rc 1
git show <C>:LOG.md        | grep -c -i kotoba -> 0   rc 1
git show <C>:SHONEN.md     | grep -c -i kotoba -> 0   rc 1
git show <C>:SCORECARD.md  | grep -c -i kotoba -> 0   rc 1
git grep -l -i kotoba <C> | wc -l              -> 3   (tree-wide, every file type)
git grep -h -i kotoba <C> | wc -l              -> 3
```

The three tree-wide `kotoba` lines, all outside the lane's own province:

- `reports/round-102/r102-connector.md:23` — fleet `lane_rounds` census line ("… kotoba 13, kotodama 27 …").
- `reports/round-103/r103-connector.md:34` — fleet staleness table row "kasegi / kagi / kake / kotoba".
- `reports/round-105/r105-R105Reviewer.md:84` — "Peer note from W2RoundProtocol about kotoba blobs is
  outside this assignment and was not acted on."

kotoba-side counts (lane repo, base `a5adc146`):

```
awk '/^## Adjacent/,0' PROVINCE.md | grep -oE '\b(audio|chousa|game-dev-2d|game-dev-3d|kagi|kaidoku|kake|kama|kasegi|kengaku|kotodama|kumitate|lore|mado|mori|revenger|souji|tabi|tameshi|tsukuroi)\b' | sort -u | wc -l -> 10
grep -c 'game-dev-2d' PROVINCE.md -> 0
ls -d /home/vgpnk/Projects/shokunin/*-shokunin | wc -l -> 21  (20 siblings + kotoba)
```

## Method limits

- No `lsp` device in this seat (`read xd://lsp` → "No such tool: xd://lsp. Mounted devices: ast_edit,
  debug"), and the artifacts are blobs in a foreign read-only repo served by `git show`, which no
  language server indexes. Text grep is therefore the only applicable method; every semantic claim
  above rests on a quoted line, not on grep counts alone.
- Sweep scope is markdown for prose (the lane's prose surface) and every file type for `kotoba`. The
  tree's 42,568 files include exported ELF binaries (e.g. `corpus/live/r25-*/…/fixture.x86_64`) whose
  `prompt`/`trigger` byte matches are not prose and are deliberately excluded from the prose counts.
- Unresolved: whether this lane later mints a `SKILL.md` (`SHONEN.md:5` unchecked). At this pin it
  carries none, so a future frontmatter could introduce an arbitration clause that does not exist
  today; the row is exact for `7753d49b`, not a standing claim.
