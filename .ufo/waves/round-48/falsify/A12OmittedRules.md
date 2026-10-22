# A12OmittedRules — rules the round-48 authority table omits or misstates

Seat `KotobaR48.A12OmittedRules`, leaf, 2026-10-22 UTC. Read-only on the lane; all fixtures and
validator runs in `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A12OmittedRules/`. No installs.

Target: `corpus/knowledge/frontmatter-rule-authorities-round48.md` (C1 at `887b6af`), table
"Rule-by-authority table", whose stated job is "Which authority imposes which SKILL.md frontmatter rule".

## Verdict

**DEFECT (medium). The table omits six rule classes, one of them enforced by both code authorities,
and two cells misstate measured behaviour. No upstream drift: every pin still matches.**
Medium, not high: no lane gate and no declared after-value depends on the missing rows, but a reader
of the table would conclude that no authority imposes the name start/end-hyphen rule.

## Instruments (re-opened by this seat 2026-10-22)

| authority | bytes / sha256 | pin |
|---|---|---|
| S018 spec.md (`agentskills.io/specification.md`, 200, 08:50Z) and spec.mdx at `69ef37e9` | 7,608 B `9a67de89132948b2…`; mdx `b9079c0c10b7930e…` | match; mdx 27, 61-65, 94, 224 exact |
| S017 validator.py / parser.py at `69ef37e9` | `b5ee3d8537c83c95…` / `9a74c9a90eb217b8…` | match |
| S012 qv.py at `dbd4588`; S019 bp.md (`…/best-practices.md`, 08:53Z); S021 codex.md | `67cf570340201393…`; 42,169 B `f0a5d61b67123a31…`; 11,035 B `ed6e324f747d47ad…` | match |

Run forms: `python3 /tmp/qv.py <dir>` (packager, PyYAML 6.0.3), `agentskills validate <dir>` (PyPI
skills-ref 0.1.1), `python3 -B verifiers/verify_skill_checklist.py --repo <lane> --skill <f>/SKILL.md
--check <id> --json`. Dir name equals `name` except where noted, so skills-ref's directory rule stays silent.

## Omitted rules (no row at all)

**O1 — name must not start or end with a hyphen.** Spec table "Must not start or end with a hyphen"
(`spec.md:30`; pinned mdx:27) and name section "Must not start or end with a hyphen (`-`)"
(`spec.md:65`); skills-ref "Skill name cannot start or end with a hyphen" (`validator.py:48-49`);
packager `if name.startswith('-') or name.endswith('-') or '--' in name` (`qv.py:67`). Runs on
dir+name `-lead` and `trail-`: qv exit 1, skills-ref exit 1. Lane `trigger.name_directory` on the
same files: PASS, exit 0 ("name '-lead' == directory '-lead'"). bp.md, codex.md: not stated. The
table spends a row on consecutive hyphens citing `qv.py:67` — the same line rejects the start/end
case the table never names.

**O2 — `compatibility` is 1-500 characters.** Spec table "Max 500 characters" (`spec.md:33`), field
section "Must be 1-500 characters if provided" (`spec.md:134`); skills-ref
`MAX_COMPATIBILITY_LENGTH = 500` (`validator.py:12`, enforced `:88-99`); packager "Maximum is 500
characters" (`qv.py:88-92`). Runs: 501 chars exit 1 both; 499 exit 0 both. The stated lower bound is
enforced by neither: `compatibility: ""` exit 0 both. bp.md, codex.md, lane: no rule (no
compatibility id in `CHECK_IDS`, `verify_skill_checklist.py:305-316`).

**O3 — `metadata` is a string-to-string map.** "a map from string keys to string values"
(`spec.md:34`, `:160`). Neither validator enforces it: skills-ref coerces,
`metadata["metadata"] = {str(k): str(v) …}` (`parser.py:61-62`); the packager's allowed-key check
skips nested keys by construction (`qv.py:41-45`). Run `metadata:` with `version: 1.0` and
`count: 3`: exit 0 both.

**O4 — `allowed-tools` is a space-separated string.** `spec.md:35`; "A space-separated string of
tools that are pre-approved to run" (`spec.md:176`). Both validators only whitelist the key
(`validator.py:15-22`, `qv.py:42`); a YAML list (`- Bash` / `- Read`) exits 0 both.

**O5 — `license`.** `spec.md:32`; section `spec.md:117-127`, "We recommend keeping it short (either
the name of a license or the name of a bundled license file)" (`spec.md:122`). No validator reads it:
a 2,000-character license exits 0 both; the table carries the other advisory rule (third person).

**O6 — frontmatter delimiter and placement rules.** Spec states only "The `SKILL.md` file must
contain YAML frontmatter followed by Markdown content." (`spec.md:24`), no delimiter text.
skills-ref needs byte 0 to be `---` and a later closing `---` (`parser.py:41-49`); the packager needs
`startswith('---')` plus `^---\n(.*?)\n---` (`qv.py:23-29`); the lane tolerates the rest — "blank
lines / BOM before the opening ``---`` are tolerated; delimiters compare after .strip()", `...`
closes (`verify_skill_checklist.py:515-528`). Measured:

| fixture | lane `trigger.frontmatter_parses` | packager | skills-ref |
|---|---|---|---|
| BOM before `---` | PASS 0 | 1 "No YAML frontmatter found" | 1 "must start with YAML frontmatter (---)" |
| blank lines before `---` | PASS 0 | 1 | 1 |
| `...` closer | PASS 0 | 1 "Invalid frontmatter format" | 1 "not properly closed with ---" |
| `  ---  ` delimiters | PASS 0 | 1 | 1 |
| CRLF throughout | PASS 0 | 0 | 0 (both use `read_text()`, universal newlines) |
| lowercase `skill.md` | n/a | 1 "SKILL.md not found" | 0 (`parser.py:14-21` accepts it) |

The lane is more permissive than both code authorities on every delimiter variant and disagrees on
the file name. bp.md, codex.md: not stated (their only `---` are examples).

## Misstated or incomplete cells

**M1 — description length (row 5).** "1025 fails (qv.py:83-84)" for the packager and "no maximum:
1025 characters pass" for the lane. The packager strips before counting (`qv.py:77`); skills-ref
does not (`validator.py:78` counts raw, `:74` guards only emptiness). A 1,024-character description
plus two spaces (`descpad`) → qv exit 0, skills-ref exit 1 "exceeds 1024 character limit (1026
chars)": "1025 fails" is false for a padded value, and the two authorities the row compares
disagree. The same guard passes whitespace-only `description: "   "` on the packager (exit 0) and
fails it on skills-ref and the lane (exit 1 each); the table records only the empty-string case.

**M2 — skills-ref name length (row 1).** "MAX_SKILL_NAME_LENGTH = 64 (validator.py:10); 65 chars
fails" is measured after `strip()` and `normalize("NFKC", …)` (`validator.py:37`), and NFKC can
lengthen: 63 `a` plus U+33CF (raw 64, NFKC image 65) → exit 1 "exceeds 64 character limit (65
chars)", while the spec's "Must be 1-64 characters" over the literal value would pass. Raw 63 →
NFKC 64 → exit 0. The packager rejects that character on charset (`qv.py:65`, exit 1), so the two
cells are not comparable.

**M3 — citation drift.** "What the table teaches" item 2 puts the frontmatter table at
"spec.md:27"; the rendered `spec.md` has the `name` row at line 30 (27 is blank) — 27 is the mdx
line. Every other spec.md citation (63, 64, 66, 67, 101, 161, 237) and bp.md citation (153, 154,
155, 156, 160-161, 162, 206, 257) is exact.

## Upstream drift since the pins: none

`git ls-remote` 08:51Z: `agentskills/agentskills` HEAD+main `69ef37e9…` (S017 pin), `anthropics/skills` HEAD+main `dbd4588…` (S012 pin); all hashes above equal the entry's.

- `specification.md` sends `last-modified` equal to its own `date` (08:53:57Z), so that header is
  per-request and cannot evidence drift. The entry's body-grep recheck is the right instrument but
  greps one sentence ("Must match the parent directory name"); a removed start/end-hyphen bullet or
  a changed compatibility clause would pass it. Greps on "Must not start or end with a hyphen" and
  "Must be 1-500 characters" would cover O1 and O2.
- Provenance: installed PyPI `skills-ref` 0.1.1 `validator.py` hashes `7b5cb3dc…`, not the pin's
  `b5ee3d85…`. `diff --strip-trailing-cr` shows the only delta is `read_text(encoding='utf-8')`
  (`validator.py:172`, `parser.py:89`) plus CRLF — behaviourally identical on a UTF-8 locale, so
  the cells stand, but the run cells come from bytes whose hash the entry does not state.

## Unresolved

- bp.md delegates structure to the overview page ("For complete Skill structure details, see …",
  `bp.md:165`), which may state compatibility/metadata rules; it is not one of the six authorities.
- Client-side enforcement of O1-O6 is unmeasured, the same limit the entry already declares.
