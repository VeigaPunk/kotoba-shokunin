# ReopenS027 — round-50 falsify seat (re-open SOURCES row S027)

**HOLDS** — applies to row S027 in `corpus/SOURCES.md:40`, its Gate line in `corpus/lessons/round-50.md`
(§ Gate, rows table), and the census entry's round-50 bullet for S027
(`corpus/knowledge/sibling-overlap-census-round49.md:214-215`), all as judged at `956ee1676e4c18480bce8ac3993541462be76e11`.
Six of six checks pass; two cosmetic notes, no defect.

## Findings, per check

1. **Bytes and sha256 — PASS (no drift).** The row names the `.md` variant as its fetch route
   ("fetched as .../customize-cloud-agent/add-skills.md"). Re-fetched it 2026-10-22T13:33:23Z:
   HTTP 200, **11,790 B**, sha256 `18c361b5b6536f50947545be92f667864f7c83f7c532c553a70a0c1dc40815b7`
   — byte-identical to the row's record (11,790 B, sha256 `18c361b5…`) and to the seat report's full
   fetch log (`.ufo/waves/round-50/build/SrcCopilotSkills.md`, row `gh-add-skills.md`,
   2026-10-22T12:30:10Z). Same bytes ~1 h after the recorded fetch.

2. **Gate quote verbatim and ≤ 25 words — PASS.** `add-skills.md:33` reads (line 32-33 shown for pin):
   - `:32` `* **name** (required): A unique identifier for the skill. This must be lowercase, using hyphens for spaces. …`
   - `:33` `* **description** (required): A description of what the skill does, and when Copilot should use it.`
   The Gate quote drops only the `* ` list marker; the text is verbatim at the cited location.
   Word count 15 (description, required, A, description, of, what, the, skill, does, and, when,
   Copilot, should, use, it) ≤ 25. Lines 32-33 sit in the "In their simplest form, they include:"
   field list under `## Creating and adding a skill` (header `:10`, next header `:41`), so the
   anchor's section name and `add-skills.md:32-33` pin are correct.

3. **Tier and scope cells honest — PASS.** Tier `A` matches the lane's convention for current vendor
   documentation (S023-S026, all `A`; contrast round-47's "tier B at best" for unversioned opencode
   docs). Scope cell says "How GitHub Copilot decides that a skill applies, and what the page states
   about the `name` and `description` frontmatter fields (vendor documentation for GitHub Copilot, not
   a measurement of omp or opencode)": supported by `## How Copilot uses agent skills` (`:231-233`,
   "based on your prompt and the skill's description") and the frontmatter field list (`:32-33`);
   the no-measurement bound is accurate.

4. **`teaches` cell says no more than the page — PASS.** Every clause verified against my fetched bytes:
   - description role: `:33` quote embedded verbatim; `:233` supports "the field Copilot matches the
     request against" (page: decides "based on your prompt and the skill's description").
   - "`name` must be 'A unique identifier for the skill'": verbatim at `:32`; the page adds
     lowercase/hyphen rules the cell omits — under-claims, not over.
   - "no character cap for the description": `character` → 0, `1024` → 0, `1,024` → 0, `truncat` → 0
     on the whole page. True.
   - "no arbitration rule for skills whose descriptions both apply": the page's only uniqueness
     language is the `name` field's "A unique identifier" (`:32`); adversarial extra sweeps
     `dedup`, `collision`, `duplicate`, `wins`, `first-found`, `first found` → 0 each. True.
   - "(sweeps: the ten terms → 0 each; `description` → 5)": reproduced exactly (check 6).

5. **Census bullet for S027 matches the page — PASS.** Bullet
   (`sibling-overlap-census-round49.md:214-215`): quote "Copilot will decide when to use your skills
   based on your prompt and the skill's description" (`add-skills.md:233`) — a contiguous verbatim
   span of the line's sentence (17 words ≤ 25); "no overlap rule" — supported by the all-zero sweep
   and the absence of any dedup/precedence language (check 4).

6. **Ten-pattern sweep reproduces — PASS.** Command `for t in 'overlap' 'ambigu' 'precedence'
   'tie[- ]?break' 'conflict' 'multiple skills' 'same name' 'prioriti' '1024' 'truncat'; do printf
   '%-16s %s\n' "$t" "$(grep -ciE "$t" add-skills.md)"; done` over the re-fetched 11,790 B:
   all ten → **0**, and `grep -ciE 'description'` → **5**. Matches the row's teaches cell and the
   seat report's sweep table column `gh-add-skills.md (11790 B)` exactly. Loop exit 0.

## Cosmetic notes (not defects)

- The anchor "§ Managing skills with GitHub CLI (`:213` …)" cites the `##` section; `:213` sits in the
  subsection `### Publishing skills` (`:209`). The claim itself ("validation deferred to the Agent
  Skills specification") is verbatim at `:213` ("To validate your skills against the [Agent Skills
  specification](https://agentskills.io/specification) … use `--dry-run`").
- The census bullet quotes `:233` from mid-sentence without an ellipsis (drops "When performing
  tasks,"). The quoted span is contiguous and meaning-preserving; the line pin is exact.

## Evidence (commands and exit codes; fetch landed in my scratch)

- `curl -sSL -o add-skills.md -w 'HTTP %{http_code} %{url_effective}\n'
  https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills.md`
  → `HTTP 200 <same .md URL>`; `wc -c` → 11790; `sha256sum` →
  `18c361b5b6536f50947545be92f667864f7c83f7c532c553a70a0c1dc40815b7`; accessed 2026-10-22T13:33:23Z.
  Located quote: "**description** (required): A description of what the skill does, and when Copilot
  should use it." (line 33 of the fetched markdown).
- `sed -n '32,33p;213p;233p' add-skills.md` → the four pinned lines above; exit 0.
- Ten-term `grep -ciE` sweep + `grep -ciE 'description'` → 0×10 and 5; exit 0. Adversarial terms
  (`1,024`, `character`, `unique`, `dedup`, `collision`, `duplicate`, `wins`, `first-found`,
  `first found`) → 0 except `unique` → 1 (the `name` line `:32`); exit 0.
- `grep -n '^#' add-skills.md` → header map confirming the three anchor sections; exit 0.
- Read-only: `git -C <lane> rev-parse HEAD` → `956ee16…` (judged bytes); row/census/lesson/seat files
  read as committed; exit 0.
- Tooling: **no install or upgrade** — `curl`, `grep`, `sed`, `wc`, `sha256sum`, `find` already on
  host; no pacman/uv/npm channel used. Lane mutation: none except this report file; no git/jj write
  command anywhere; all fetch bytes under `/fast/scratch/hyaku/kotoba-r50/falsify/ReopenS027/fetch/`.

## Residual risk and verification gaps

- Bytes verified at one re-fetch (~63 min after the recorded one); docs.github.com serves stable
  markdown but can change at any later time — the `recheck 90d` cell covers this.
- I did not re-verify the row's sibling claims (S028's `:415` quote lives on a different page) — out
  of this seat's scope; the S027-scoped record is fully reproduced.
- The teaches cell's negative ("no arbitration rule") is sweep-plus-read evidence on one page, the
  same form Q14/Q26 accept; a rule outside these ten patterns and my nine adversarial terms is not
  excluded by construction, but none exists on the page text.
