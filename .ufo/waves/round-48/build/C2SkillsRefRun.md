# C2SkillsRefRun — skills-ref capability evidence (claim C2, round 48, attempt 2)

Seat: `KotobaR48.C2SkillsRefRun` (leaf executor, freshness axis). Lane read-only except this
report file. Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2SkillsRefRun/`.

## Findings

F1. **The validator installs and runs from the official source.** `skills-ref` **is** published on
PyPI, so the PyPI channel is the official install path the item names. `uv tool install
skills-ref==0.1.1` → executable `~/.local/bin/agentskills`, `agentskills, version 0.1.1`. Wheel
sha256 `d35db5bb…f461b5`, sdist sha256 `6b400ca6…d2695` (upload 2026-01-10T13:23:40Z; PyPI
publishes only 0.1.0 and 0.1.1).

F2. **The installed console-script name differs from the documented one, and the PyPI bytes differ
from the git tree.** The PyPI wheel's entry point is `agentskills`, so `skills-ref validate …` is
**not** on `PATH` after a PyPI install (`command -v skills-ref` → exit 1); the git subdirectory
install does provide `skills-ref`. The code bases are not byte-identical: PyPI 0.1.1
`validator.py` sha256 `7b5cb3dc…906` vs upstream `b5ee3d85…5f6c5`; the only difference is one
line, `read_text()` → `read_text(encoding='utf-8')` (same change in `parser.py`); `cli.py`,
`models.py`, `errors.py`, `prompt.py` are byte-identical. PyPI 0.1.0 shipped the module as
`agentskills/`; 0.1.1 renamed it `skills_ref/`.

F3. **Behaviour is identical across both install channels on every fixture.** PyPI 0.1.1 and the
git-pinned install (upstream `69ef37e9424c0a7ea9dd2293b559e43ec8176379` = current `refs/heads/main`
per `git ls-remote`; also `f130f348…`, the last commit touching `skills-ref/`) gave the same exit
code and message text on all 21 skill directories plus the lane copy. The upstream-pinned
executable reports `skills-ref, version 0.1.0` (upstream `pyproject.toml` still says 0.1.0).

F4. **The three routed counterexamples behave as the C2 knowledge entry says, and the divergence is
three-way, not two-way.** YAML alias to an anchored `<b>`: **exit 1** — skills-ref refuses the
*anchor* at parse time (`strictyaml`), so the description is never validated. Escaped `\u003c` in a
double-quoted scalar: **exit 0** — `validate` accepts it; only `read-properties` reveals the
decoded `<skills>`. Literal `<skills>` and `->`: **exit 0** — skills-ref has no description
character rule at all. So the lane's `trigger.no_xml_tag` is not a subset of skills-ref's verdict
set: they disagree in both directions (lane FAILs on `<skills>`, skills-ref accepts it;
skills-ref FAILs on the alias, the lane checker PASSes it).

F5. **The lane's own SKILL.md passes skills-ref.** Copied to `lane-copy/kotoba-shokunin/` (directory
name matching its `name:`), copy sha256 `1923484600b5879c16d390aff43698f0974616946150c0b20787ed5e65d3ee22`
(equal to the lane file), `validate` exit 0. The lane file changed during this seat's run (a
sibling edited the portability-floor sentence at 05:27); the copy was refreshed and re-validated.

F6. **Supplementary controls** (beyond the assigned 11, added to map rules to authorities): name
length 64 passes / 65 fails; leading- and trailing-hyphen names fail; uppercase Unicode
(`Café-Skill`) fails; `claude-tools` **passes** (skills-ref enforces no reserved words); a 64-`b`
name in a matching directory passes.

## Verbatim validator output (exit code + message)

`~/.local/bin/agentskills validate <dir>` (PyPI 0.1.1). Failures print to **stderr**, successes to
**stdout**. Verbatim below; the transcript file carries the absolute paths.

```
=== fixtures/valid-baseline/          exit 0
Valid skill: fixtures/valid-baseline
=== fixtures/Uppercase-Name/          exit 1
Validation failed for fixtures/Uppercase-Name:
  - Skill name 'Uppercase-Name' must be lowercase
=== fixtures/café-skill/              exit 0
Valid skill: fixtures/café-skill
=== fixtures/double--hyphen/          exit 1
Validation failed for fixtures/double--hyphen:
  - Skill name cannot contain consecutive hyphens
=== fixtures/mismatched-dir/          exit 1
Validation failed for fixtures/mismatched-dir:
  - Directory name 'mismatched-dir' must match skill name 'other-name'
=== fixtures/desc-skills-tag/         exit 0
Valid skill: fixtures/desc-skills-tag
=== fixtures/desc-arrow/              exit 0
Valid skill: fixtures/desc-arrow
=== fixtures/desc-1025/               exit 1
Validation failed for fixtures/desc-1025:
  - Description exceeds 1024 character limit (1025 chars)
=== fixtures/desc-alias/              exit 1
Validation failed for fixtures/desc-alias:
  - Invalid YAML in frontmatter: While scanning
  in "<unicode string>", line 3, column 6:
    ref: &desc "Contains <b> bold tag via ...
         ^ (line: 3)
Found confusing disallowed anchor token (surround with ' and ' to make text appear literally)
  in "<unicode string>", line 3, column 11:
    ref: &desc "Contains <b> bold tag via anchor"
              ^ (line: 3)
=== fixtures/desc-escaped-unicode/     exit 0
Valid skill: fixtures/desc-escaped-unicode
=== fixtures/unknown-field/            exit 1
Validation failed for fixtures/unknown-field:
  - Unexpected fields in frontmatter: author. Only ['allowed-tools', 'compatibility', 'description', 'license', 'metadata', 'name'] are allowed.
=== lane-copy/kotoba-shokunin/         exit 0
Valid skill: lane-copy/kotoba-shokunin
```

Supplementary controls, same tool:

```
fixtures/name-64-chars/          exit 0  Valid skill: fixtures/name-64-chars
fixtures/name-65-chars/          exit 1  - Skill name 'aaa…a' exceeds 64 character limit (65 chars)
                                       - Directory name 'name-65-chars' must match skill name 'aaa…a'
fixtures/name-leading-hyphen/     exit 1  - Skill name cannot start or end with a hyphen
fixtures/name-trailing-hyphen/    exit 1  - Skill name cannot start or end with a hyphen
fixtures/name-uppercase-unicode/ exit 1  - Skill name 'Café-Skill' must be lowercase
fixtures/name-digit-only/        exit 1  - Directory name 'name-digit-only' must match skill name '123'
fixtures/claude-tools/            exit 0  Valid skill: fixtures/claude-tools
fixtures/desc-1024-control/       exit 0  Valid skill: fixtures/desc-1024-control
```

The git-pinned upstream install (`upstream-venv/bin/skills-ref`, commit `69ef37e9`) returns the
**same exit code and message text** on every target; transcript sha256 `f3abd5ca…387c`.

## Cross-check against the lane's own checker (`trigger.no_xml_tag`)

`python3 -B verifiers/verify_skill_checklist.py --skill <fixture>/SKILL.md --check
trigger.no_xml_tag --json` from the lane root (exit 1 on FAIL):

| fixture | skills-ref | lane `trigger.no_xml_tag` |
|---|---|---|
| `desc-skills-tag` (`<skills>`) | exit 0 | FAIL (`'<skills>'`) |
| `desc-arrow` (`->`) | exit 0 | PASS |
| `desc-escaped-unicode` (`\u003c`) | exit 0 | FAIL (`'\\u003c'`) |
| `desc-alias` (`*desc` → `<b>`) | exit 1 (parse) | PASS |
| `café-skill` | exit 0 | PASS |
| `Uppercase-Name`, `double--hyphen`, `mismatched-dir`, `unknown-field`, `desc-1025` | exit 1 | PASS (no such lane rule) |

## Evidence — commands, exit codes, hashes

```
uv tool install skills-ref==0.1.1                     exit 0 → ~/.local/bin/agentskills
~/.local/bin/agentskills --version                    exit 0 "agentskills, version 0.1.1"
uv venv --python 3.12 upstream-venv                   exit 0
uv pip install "git+https://github.com/agentskills/agentskills@69ef37e9…#subdirectory=skills-ref"  exit 0
upstream-venv/bin/skills-ref --version               exit 0 "skills-ref, version 0.1.0"
git ls-remote …/agentskills.git HEAD refs/heads/main  exit 0
   69ef37e9424c0a7ea9dd2293b559e43ec8176379  HEAD
   69ef37e9424c0a7ea9dd2293b559e43ec8176379  refs/heads/main
```

| artefact | sha256 | note |
|---|---|---|
| PyPI wheel `skills_ref-0.1.1-py3-none-any.whl` | `d35db5bb…f461b5` | PyPI JSON `digests.sha256` |
| PyPI sdist `skills_ref-0.1.1.tar.gz` | `6b400ca6…d2695` | downloaded, 93,519 B |
| upstream `validator.py` @ `69ef37e9` | `b5ee3d85…5f6c5` | = @ `f130f348`; 5,154 B |
| upstream `parser.py` @ `69ef37e9` | `9a74c9a9…c211` | = @ `f130f348` |
| installed (PyPI 0.1.1) `validator.py` | `7b5cb3dc…906` | differs from upstream by the `encoding='utf-8'` line only |
| installed (PyPI 0.1.1) `parser.py` | `f1599cab…6ffa` | same one-line difference |
| `https://agentskills.io/specification.md` | `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16` | 7,608 B |
| `quick_validate.py` @ `dbd4588` (context only, S012) | `67cf5703…e365` | 3,972 B |

Scratch transcripts: `skills-ref-transcript.txt` (`dfeb3bf4…cf22`),
`skills-ref-upstream-transcript.txt` (`f094c8d0…4595`), `cross-validator-summary.json`
(`f6c9cf84…8f61`), `pypi-vs-upstream-69ef37e9.txt` (`f3abd5ca…387c`). Fixture `SKILL.md`
sha256 (the 11 assigned) are in `cross-validator-summary.json` and in the transcript dir; the
lane copy is `1923484600b5879c16d390aff43698f0974616946150c0b20787ed5e65d3ee22`.

## Sources opened this session (URL, access time UTC, located quote ≤25 words)

1. `https://agentskills.io/specification.md` — 2026-10-22T08:35:54Z, HTTP 200, 7,608 B.
   § `#### name field` :64 "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)";
   :66 "Must not contain consecutive hyphens (`--`)"; :67 "Must match the parent directory name";
   § `#### description field` :101 "Must be 1-1024 characters"; § Validation :257 "skills-ref validate ./my-skill".
2. `…/agentskills/agentskills/69ef37e9…/skills-ref/src/skills_ref/validator.py` — 2026-10-22T08:35:55Z,
   HTTP 200, 5,154 B. `_validate_name` :54 `if not all(c.isalnum() or c == "-" for c in name):`;
   :46 "must be lowercase"; :52 "Skill name cannot contain consecutive hyphens";
   :111 "Unexpected fields in frontmatter".
3. `…/agentskills/agentskills/69ef37e9…/skills-ref/README.md` — 2026-10-22T08:35:54Z, HTTP 200,
   2,166 B. :52 "the `skills-ref` executable will be available on your `PATH`"; :6 "This library is
   intended for demonstration purposes only." (The README documents the name the PyPI wheel does
   not install — F2.)
4. `https://pypi.org/pypi/skills-ref/json` — 2026-10-22T08:35:55Z, HTTP 200, 8,277 B. summary
   "Reference library for Agent Skills"; versions `["0.1.0","0.1.1"]`; project URL
   `https://github.com/anthropics/agentskills` (**404 today**) while the code lives at
   `https://github.com/agentskills/agentskills` (HTTP 200) — the PyPI metadata points at a dead repo.

## Risks / blockers

- **SOURCES citation hazard for the C2 entry.** A row citing "skills-ref `validator.py` sha256
  `b5ee3d85…`" while the run used the PyPI wheel describes different bytes (`7b5cb3dc…`). The C2
  entry as drafted pairs the git blob hash with "PyPI `skills-ref` 0.1.1 run as `agentskills
  validate`" in one sentence; the two identifiers are not the same artefact. Behavioural equality
  (F3) means no verdict changes, but the citation should name which artefact was executed. Noted,
  not edited — the entry belongs to the scribe seat.
- Upstream `skills-ref` version in `pyproject.toml` is still `0.1.0` while PyPI publishes `0.1.1`;
  upstream `main` does not carry the `encoding='utf-8'` change. "0.1.1" is a PyPI-only build.
- The upstream README marks the library "intended for demonstration purposes only", so a skills-ref
  verdict is a reference-implementation verdict, not a client-loading verdict.
- Tooling: `uv tool install` (PyPI) and `uv venv` + `uv pip install` from the official GitHub
  repository. No pacman transaction, no host service restart; the host-wide pacman guard was not
  engaged.
