# C2 freshness — quick_validate.py at anthropics/skills main HEAD vs S012 pin

Seat: KotobaR48.C2QuickValidateFresh (leaf). Scope: description/name validation drift of
`skills/skill-creator/scripts/quick_validate.py` (S012) between the pinned commit and current
main HEAD. Read-only on the lane; all work in
`/fast/scratch/hyaku/kotoba-r48-a2/seats/KotobaR48.C2QuickValidateFresh/`. No tool installs
(system pyyaml 6.0.3 and uv 0.13.0 already present).

## Verdict

**No drift.** Current main HEAD **is** the S012 pin: `dbd4588f9e1033efb41dad4bef2f7947c8993d44`
(committed 2026-10-09T18:45:49Z, "Update claude-api skill: dynamic workflows and the four
workflow quickstarts (#1995)"). The file is byte-identical at HEAD and at the pin
(git blob `ed8e1dddce77b16af13c6f36b3fe86c4ac7c590c`, 3972 bytes, sha256
`67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`). `diff` between the two
fetches is empty (exit 0). The last upstream commit that touched this file is
`1ed29a03dc85` (2026-02-06T21:19:32Z, "Update skill-creator and make scripts executable
(#350)") — the validation logic has not moved for ~8.5 months.

## Findings

F1. **Pin is current.** S012's tree pin `dbd4588` == `refs/heads/main` == `HEAD` (git
ls-remote), and REST `/repos/anthropics/skills` reports `default_branch main`,
`pushed_at 2026-10-09T18:45:52Z`. A C2 entry may cite `dbd4588` as current HEAD as of
2026-10-22T08:11Z without a superseding row.

F1b. **No alternate pin surface.** Upstream has 0 tags and 0 releases, so main HEAD is the
only pinnable surface for S012; there is no release/tag drift to check.

F2. **Angle brackets: unchanged, any `<`/`>`.** `quick_validate.py:79-81` at both refs:
`# Check for angle brackets` / `if '<' in description or '>' in description:` /
`return False, "Description cannot contain angle brackets (< or >)"`. Substring test, so
well-formed XML tags and plain comparisons (`5 < 6`) are both refused; escaped `&lt;` passes.
S012's citation `:79-81` is still exact — no re-citation needed.

F3. **Lengths: unchanged.** name `if len(name) > 64:` at `:70`, message `:71`; description
`if len(description) > 1024:` at `:83`, message `:84`; compatibility `> 500` at `:91-92`.
Bounds inclusive (64/1024 pass).

F4. **Name regex: unchanged.** `:65` `if not re.match(r'^[a-z0-9-]+$', name):` (message `:66`),
plus `:67-68` start/end hyphen and `--` rule. No `re.UNICODE`/`re.ASCII` flag: `café-skill`
fails, `ProbeSkill` fails.

F5. **Allowed keys: unchanged.** `:42`
`ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata', 'compatibility'}`;
`:45-50` rejects any extra top-level key and prints the allowed set. Non-string
description/name rejected at `:60-61` / `:75-76` (after `yaml.safe_load`, so a YAML alias
resolving to a string passes).

F6. **Live gap (freshness caveat, not a change):** empty `name` or `description` passes today —
the `if name:` (`:63`) / `if description:` (`:78`) guards skip validation. Probes: exit 0,
"Skill is valid!" for both. Four open (unmerged) PRs propose changing this validator:
#1714 "quick_validate: reject empty skill descriptions" (open, updated 2026-09-02),
#1949 "skill-creator: quick_validate rejects empty name/description and checks referenced
files" (open, updated 2026-10-05), #1556 "Declare PyYAML dependency for quick_validate",
#1580 "Fix quick_validate UTF-8 decoding crash on Windows". #1714 deletes the
`if description:` guard and adds `+    if not description:` / `+        return False,
"Description cannot be empty"`; #1949 adds `+    if not name:` / `+        return False,
"Field 'name' in frontmatter must not be empty"` plus a bundled-resource existence check.
Entry must state the empty-value gap as current behavior with fixes pending, not as a rule.

F7. **Authority wiring holds at HEAD.** `skills/skill-creator/scripts/package_skill.py:17`
`from scripts.quick_validate import validate_skill`, called at `:72` — the packager still
gates on this validator, so the S012 "packaging tooling" framing is current.

F8. **Unchanged lines (identical numbering at both refs, proven by blob-sha identity):**
`:23` frontmatter startswith `---`; `:27` `re.match(r'^---\n(.*?)\n---', ...)`; `:35-39`
`safe_load` + dict/YAMLError handling; `:53-56` required name/description; `:59-62` name
extraction + strip; `:74-77` description extraction + strip; `:94` `return True, "Skill is
valid!"`; `:96-103` CLI (`print(message)`, `sys.exit(0 if valid else 1)`).
Changed lines: **none** — the two files' unified diff is empty.

## Behavioral probes (run against the fetched HEAD bytes; exit codes verbatim)

`python3 -B probe.py` (probe_exit=0); each case a temp SKILL.md, validator run per case:

| case | exit | output |
|---|---|---|
| angle_tag (`<tag>`) | 1 | Description cannot contain angle brackets (< or >) |
| angle_math (`5 < 6`) | 1 | Description cannot contain angle brackets (< or >) |
| escaped_entity (`&lt;`) | 0 | Skill is valid! |
| desc_1024 | 0 | Skill is valid! |
| desc_1025 | 1 | Description is too long (1025 characters). Maximum is 1024 characters. |
| name_64 | 0 | Skill is valid! |
| name_65 | 1 | Name is too long (65 characters). Maximum is 64 characters. |
| name_unicode (`café-skill`) | 1 | Name 'café-skill' should be kebab-case (lowercase letters, digits, and hyphens only) |
| name_upper (`ProbeSkill`) | 1 | Name 'ProbeSkill' should be kebab-case (…) |
| name_double_hyphen | 1 | Name 'probe--skill' cannot start/end with hyphen or contain consecutive hyphens |
| desc_alias (YAML `*d`) | 0 | Skill is valid! |
| desc_list | 1 | Description must be a string, got list |
| extra_key (`foo: bar`) | 1 | Unexpected key(s) in SKILL.md frontmatter: foo. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name |
| allowed_keys_all | 0 | Skill is valid! |
| empty_name | 0 | Skill is valid! |
| empty_description | 0 | Skill is valid! |

## Fixture cross-check (peer-supplied paths, run against HEAD bytes)

`python3 -B qv_pinned.py <dir>` over the 18 fleet lane SKILL.md and the 3 vendored unreal-mcp
upstream skills; 21 total, 14 failures:

- 10 lanes fail the **parse** branch with `Invalid YAML in frontmatter: mapping values are not
  allowed here` (game-dev-3d, kagi, kaidoku, kake, kama, kasegi, kumitate, mado, tabi,
  tsukuroi) — plain scalars containing `': '` (e.g. `Rank: shonen.`) under `yaml.safe_load`
  (`:35`). This confirms FrSiblingOverlap's fixture tip: quick_validate's parser is the
  strictest authority for those files.
- 2 more lanes fail a different branch: lore, souji → `Missing 'name' in frontmatter` (`:54`).
- 6 lanes pass: chousa, kengaku, kotoba, kotodama, mori, tameshi.
- Vendored: `create-toolset` → `Description is too long (1054 characters). Maximum is 1024
  characters.` (`:84`); `unreal-skill` → same at 1041; `unreal-mcp` → `Skill is valid!`.
  Both descriptions exceed 1024, exactly as the peer measured.

## Evidence

Source fetches (access 2026-10-22T08:11:20Z UTC):
- `https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/scripts/quick_validate.py`
  → `qv_head.py`, HTTP 200, sha256 `67cf5703…fde365`.
- `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`
  → `qv_pinned.py`, HTTP 200, sha256 `67cf5703…fde365`. Quote (line 79): "Check for angle
  brackets"; quote (line 81): "Description cannot contain angle brackets (< or >)".
- `git ls-remote https://github.com/anthropics/skills HEAD refs/heads/main` → both
  `dbd4588f9e1033efb41dad4bef2f7947c8993d44` (saved `ls-remote.txt`).
- `https://api.github.com/repos/anthropics/skills` → `default_branch main`,
  `pushed_at 2026-10-09T18:45:52Z` (quote: "pushed_at 2026-10-09T18:45:52Z").
- `https://api.github.com/repos/anthropics/skills/contents/skills/skill-creator/scripts/quick_validate.py?ref={main,dbd4588…}`
  → both `sha ed8e1dddce77b16af13c6f36b3fe86c4ac7c590c`, `size 3972`; local
  `git hash-object qv_pinned.py` = `ed8e1dddce77b16af13c6f36b3fe86c4ac7c590c`.
- `https://api.github.com/repos/anthropics/skills/commits?path=skills/skill-creator/scripts/quick_validate.py`
  → newest entry `1ed29a03dc85 2026-02-06T21:19:32Z`.
- PR evidence: `https://api.github.com/repos/anthropics/skills/pulls/1949` (quote: "state:
  open head: f88b129c363c base: 8a1541c4a3ff"), `pulls/1714`, `pulls/1556`, `pulls/1580`;
  patches saved as `pr1949.diff`, `pr1714.diff`.

Command receipts (all in scratch dir unless noted):
- `sha256sum qv_head.py qv_pinned.py` → identical digest, exit 0.
- `diff -u qv_pinned.py qv_head.py` → no output, `diff_exit=0`.
- `python3 -B probe.py` → 16 probe lines above, `probe_exit=0`.
- Read-only lane checks: `corpus/knowledge/frontmatter-rule-authorities-round48.md` ABSENT
  at 2026-10-22T08:12Z; `.ufo/waves/round-48/build/` exists (report written here).

## Remaining unknowns

U1. Whether #1714/#1949 merge before the round-48 landing or a later re-pin — if they land,
S012's row needs a superseding row (empty-value rejection would become a rule).
U2. `skills-ref` and the lane's own lexical checker are outside this seat's scope (other
seats); this seat only certifies the S012 pin and the validator's live behavior.
U3. PyYAML remains undeclared upstream (#1556 open); running the validator requires an
environment that supplies `yaml` (system pyyaml 6.0.3 used here).
