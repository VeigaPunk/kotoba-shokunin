# A04 — skills-ref (S017) column + SOURCES S017 row, round-48 falsify

Seat: `KotobaR48.A04SkillsRefColumn` (leaf reviewer, freshness axis). Date 2026-10-22.
Scope: `corpus/knowledge/frontmatter-rule-authorities-round48.md` S017 column (skills-ref) and
`corpus/SOURCES.md` line 30. Read-only on the lane except this file. Scratch:
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A04SkillsRefColumn/` (clone, fixtures, venvs).

## Verdict

**CONFIRMED** — all ten S017 rule cells, all three counterexample rows, and the SOURCES S017 row.
Zero REFUTED cells, zero defects. One cosmetic citation-hygiene residual (R1).

## Freshness (axis under judgment)

- Upstream tip re-opened 2026-10-22: `git ls-remote` HEAD = `refs/heads/main` =
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`; clone HEAD log: "docs: add OpenClaw to client
  showcase (#492)", committer 2026-08-09T13:36:04-07:00. SOURCES' "main tip, 2026-08-09" still true.
- `validator.py` raw fetch 2026-10-22T08:53:40Z (raw.githubusercontent.com at the pin), 5,154 B,
  sha256 `b5ee3d85…5f6c5` — byte-equal to the clone at the pin and to the hash the entry pins.
  `prompt.py` 1,724 B, sha256 `8ed90a6…cf15`.
- Spec page re-opened 2026-10-22T09:00:49Z: `https://agentskills.io/specification.md`, 200, 7,608 B,
  sha256 `9a67de89…` — byte-identical to the hash in the entry header. :254 "Use the [skills-ref](…)
  reference library to validate your skills:"; :257 "skills-ref validate ./my-skill" — S017's framing
  as "the spec's reference validator" holds.
- Packaged tool: `agentskills, version 0.1.1` (pre-existing uv tool install of PyPI `skills-ref`)
  — matches the entry's "PyPI `skills-ref` 0.1.1 run as `agentskills validate`".
- SOURCES anchors re-checked in the pinned tree: `pyproject.toml:3` `version = "0.1.0"`, `:13`
  `strictyaml>=1.7.3`; `validator.py:10-113` covers every cited rule line; `parser.py:36-73`
  contains the strictyaml load (:53), YAMLError→ParseError (:55-56), metadata coercion (:61-62).

## Cell-by-cell (line numbers read raw at the pin; runs = `agentskills validate`, exit codes verbatim)

| cell | verdict | evidence |
|---|---|---|
| name length: `MAX_SKILL_NAME_LENGTH = 64` (:10); 65 chars fails | CONFIRMED | :10 exact; exact 65-char name exit 1 "exceeds 64 character limit (65 chars)"; 64-char name draws no length error |
| name charset: NFKC then `c.isalnum() or c == "-"` (:37,:54-58); `技能-测试` valid | CONFIRMED | :37 `unicodedata.normalize("NFKC", name.strip())`; :54 `if not all(c.isalnum() or c == "-" ...)`; `技能-测试` exit 0 "Valid skill" |
| name=directory: NFKC both sides (:60-65); dir `probe－full` + name `probe-full` valid | CONFIRMED | :61 NFKC on `skill_dir.name`; U+FF0D-directory fixture exit 0 |
| consecutive hyphens rejected (:51-52) | CONFIRMED | :51 `if "--" in name:`; `double--hyphen` exit 1 "cannot contain consecutive hyphens" |
| description length: `MAX_DESCRIPTION_LENGTH = 1024` (:11) | CONFIRMED | :11 exact; 1024-char desc exit 0, 1025 exit 1 "(1025 chars)" |
| angle brackets not a validity rule; prompt.py:46 escapes; `Use <skills>` valid | CONFIRMED | `_validate_description` (:70-83) is non-empty + cap only; prompt.py:46 `lines.append(html.escape(props.description))`; `Use <skills>` exit 0; `to-prompt` renders `&lt;skills&gt;` |
| third person: not stated | CONFIRMED | grep `person|splitlines|number of lines|500 lines|body` over validator.py → 0 hits |
| reserved words: not stated; `claude-tools` valid | CONFIRMED | grep `claude|anthropic|reserved` → 0 hits; `claude-tools` exit 0 |
| unknown fields: "Unexpected fields in frontmatter" (:104-113) | CONFIRMED | def :104, message f-string :111, close paren :113; top-level `author:` exit 1 with exact message and the six-field allowlist |
| body length: not stated | CONFIRMED | no line-count logic anywhere in validator.py (177 lines; grep 0) |

## Counterexample rows (all reproduce)

- YAML alias `description: *desc` anchored to `<b>`: exit 1, "Found confusing disallowed anchor
  token" — strictyaml refuses the anchor at parse; field rules never run. CONFIRMED.
- Unicode name `技能-测试` (directory matches): exit 0 "Valid skill". CONFIRMED.
- Escaped `"\u003cskills\u003e …"`: validate exit 0; `read-properties` prints the decoded
  "Use <skills> for loading.". CONFIRMED.

## Cross-artifact control

Built the pinned-commit install (`uv venv` + `uv pip install -e repo/skills-ref`, clone at
`69ef37e9`): the imported `validator.py` hashes `b5ee3d85…5f6c5` and returns the same exit code and
message text on all five assigned fixtures (`技能-测试`, `claude-tools`, `desc-skills-tag`,
`unknown-field`, `desc-alias`). The entry's cells hold for the pinned blob, not only the PyPI wheel.

## Residual risk

- **R1 (cosmetic, pre-existing).** The entry header pairs the upstream blob sha `b5ee3d85…` with
  "PyPI 0.1.1 run" in one sentence — different bytes: installed PyPI `validator.py` hashes
  `7b5cb3dc…` (hashed this session; build seat F2 says the only delta is `encoding='utf-8'`).
  Behavioural equality verified on the five assigned fixtures, so no verdict changes; an
  encoding-sensitive fixture could split them. Suggested, not applied: cite the executed artifact.
- **R2 (anchor span).** SOURCES' `parser.py:36-73` omits `parse_frontmatter`'s def (line 30) but
  contains every load-bearing line (53, 55-56, 61-62); no claim rests on the def line.
- README:6 "This library is intended for demonstration purposes only." — a skills-ref verdict is a
  reference-implementation verdict, not a client-loading one; SOURCES' teaches-cell already says so.

## Verification gaps

- Client runtime behavior (what Claude/Codex/omp execute on load) out of scope, as the entry's
  Limits section states.
- The PyPI-vs-upstream byte diff was taken from the build seat (C2SkillsRefRun F2/F8), not re-diffed
  line by line here; the two artifact hashes are first-hand, the diff text is not.

## Tooling

No installs or upgrades (pacman paused; guard not engaged). Used pre-existing `uv` 0.13.0 and PyPI
`skills-ref` 0.1.1 (`~/.local/bin/agentskills`); built one scratch venv from the official GitHub
tree at the pin. All writes confined to the seat scratch directory and this report file.
Fixtures retained for audit under `seats2/A04SkillsRefColumn/fx/`.
