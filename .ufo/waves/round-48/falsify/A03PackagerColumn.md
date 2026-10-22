# A03 Packager column falsify — S012 (`quick_validate.py@dbd4588`), round 48

## Verdict

**CONFIRMED** — every S012 cell in `corpus/knowledge/frontmatter-rule-authorities-round48.md`
reproduces against the pinned upstream file: all quoted line numbers are exact, both claimed
zero-hit greps reproduce (exit 1), and all eight assigned fixtures behave as tabulated
(message, exit code). No defect found in the S012 column.

## Artifact fidelity (fetched 2026-10-22 ~08:50 UTC)

- URL: `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`
  — `curl -fsSL` exit 0, 3,972 bytes.
- sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` — matches the entry's
  `67cf5703…`.
- Freshness claim "this pin is still `main` HEAD on 2026-10-22": `git ls-remote` returns
  `dbd4588f9e1033efb41dad4bef2f7947c8993d44  refs/heads/main` at 2026-10-22T08:50:52Z. Confirmed.

## Line-number audit (all exact)

| cited | actual content | ok |
|---|---|---|
| qv.py:42-49 "allowed set of six" | L42 = `ALLOWED_PROPERTIES = {'name','description','license','allowed-tools','metadata','compatibility'}` (exactly six); L45-49 = unexpected-key diff + `"Unexpected key(s) …"` message | ✔ |
| qv.py:65 | `if not re.match(r'^[a-z0-9-]+$', name):` | ✔ |
| qv.py:67 | `if name.startswith('-') or name.endswith('-') or '--' in name:` | ✔ |
| qv.py:70-71 | `if len(name) > 64:` / `"… Maximum is 64 characters."` (quote verbatim on L71) | ✔ |
| qv.py:78 | `if description:` guard | ✔ |
| qv.py:79-81 | angle-bracket check; `"Description cannot contain angle brackets (< or >)"` verbatim on L81 | ✔ |
| qv.py:83-84 | `if len(description) > 1024:` / `"… Maximum is 1024 characters."` | ✔ |

Not-stated cells reproduce: `grep -n 'dirname\|basename\|parent' quick_validate.py` → exit 1, zero
hits; `grep -niE 'third person' quick_validate.py` → exit 1, zero hits.

## Fixture runs (published file, unmodified; `python3 quick_validate.py <dir>`; PyYAML 6.0.3)

| fixture | result | exit | cell confirmed |
|---|---|---|---|
| name = `a`×65 (exactly 65 chars, verified) | "Name is too long (65 characters). Maximum is 64 characters." | 1 | name length ✔ |
| name = `café-skill` | "Name 'café-skill' should be kebab-case (lowercase letters, digits, and hyphens only)" | 1 | charset `^[a-z0-9-]+$` ✔ |
| name = `probe--x` | "…cannot start/end with hyphen or contain consecutive hyphens" | 1 | consecutive hyphens ✔ |
| description = `x`×1025 (verified 1025) | "Description is too long (1025 characters). Maximum is 1024 characters." | 1 | 1025 fails ✔ |
| description = `''` (empty) | "Skill is valid!" | 0 | empty passes via `if description:` ✔ |
| description = `a < b` | "Description cannot contain angle brackets (< or >)" | 1 | any bracket, not just tags ✔ |
| name = `claude-tools` | "Skill is valid!" | 0 | reserved words not stated ✔ |
| extra key `version: 1` | "Unexpected key(s) in SKILL.md frontmatter: version. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name" | 1 | unknown key, six allowed ✔ |

Counterexample-table S012 rows, re-run as a bonus (same script):

| fixture | result | exit | table row ✔ |
|---|---|---|---|
| name = `技能-测试` | "Name '技能-测试' should be kebab-case …" | 1 | FAIL, kebab-case, exit 1 ✔ |
| `metadata: {anchor: &d "x <b> y"}` + `description: *d` | angle-bracket failure (PyYAML resolves the alias) | 1 | FAIL, angle brackets, exit 1 ✔ — same anchor-under-`metadata` shape as `.ufo/waves/round-48/build/C2EntryScaffoldScribe.md:54` |
| description = `"before \u003cskills\u003e after"` (double-quoted) | angle-bracket failure (decodes to `<skills>`) | 1 | FAIL, exit 1 ✔ |

Process note (honesty): a first generator pass omitted the closing `---` delimiter; the script
correctly rejected all fixtures with "Invalid frontmatter format", exit 1. Fixtures were
regenerated with valid frontmatter and all results above are from the corrected rerun.

## Residual risk and verification gaps

- The `if description:` empty-pass and all messages are pinned to commit `dbd4588`; upstream drift
  invalidates cells without changing the sha256 check unless re-fetched. The entry already scopes
  this ("passes today"). Recheck = re-run this seat's fetch + fixtures.
- Environment variance untested beyond one stack: system `python3` with PyYAML 6.0.3, Linux x64.
  Cells quote code lines, which are environment-independent; behavior cells matched observed runs.
- The alias reproduction anchors under `metadata` (the build wave's documented shape). An alias
  anchored under a *disallowed* top-level key would hit "Unexpected key(s)" first (L45 runs before
  description checks); the entry does not claim otherwise, so no conflict, but that variant was
  not run.
- Out of scope (other seats): skills-ref/docs/lane columns, Claude Code 256-char name claims,
  client runtime behavior.

## Tooling

No installs or upgrades were needed; used preinstalled `curl`, `git`, `grep`, `python3` (with
PyYAML 6.0.3). Lane checkout untouched except this report file.
