# C2SkillsRefRun — skills-ref capability evidence (claim C2, round 48, attempt 2)
Seat: `KotobaR48.C2SkillsRefRun` (leaf executor, freshness axis). Lane read-only except this report
file. Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2SkillsRefRun/`.

## Findings

F1. **Official source, installed and run.** `skills-ref` **is** published on PyPI, so the PyPI
channel is the official install path the item names. `uv tool install skills-ref==0.1.1` →
`~/.local/bin/agentskills`, `agentskills, version 0.1.1`. Wheel sha256 `d35db5bb…f461b5`, sdist
sha256 `6b400ca6…d2695` (upload 2026-01-10T13:23:40Z; PyPI publishes only 0.1.0 and 0.1.1).

F2. **The installed console-script name differs from the documented one, and the PyPI bytes differ
from the git tree.** The PyPI wheel's entry point is `agentskills`, so `skills-ref validate …` is
**not** on `PATH` after a PyPI install (`command -v skills-ref` → exit 1); the git subdirectory
install does provide `skills-ref`. PyPI 0.1.1 `validator.py` sha256 `7b5cb3dc…906` vs upstream
`b5ee3d85…5f6c5`, differing only in `read_text()` → `read_text(encoding='utf-8')` (same change in
`parser.py`); `cli.py`, `models.py`, `errors.py`, `prompt.py` byte-identical. PyPI 0.1.0 shipped
`agentskills/`; 0.1.1 renamed it `skills_ref/`.

F3. **Both install channels behave identically on every fixture.** PyPI 0.1.1 and the git-pinned
install (upstream `69ef37e9424c0a7ea9dd2293b559e43ec8176379` = current `refs/heads/main` per
`git ls-remote`; also `f130f348…`, the last commit touching `skills-ref/`) gave the same exit code
and message text on all 21 skill directories plus the lane copy. The upstream-pinned executable
reports `skills-ref, version 0.1.0`.

F4. **The routed counterexamples behave as the C2 knowledge entry says, and the divergence is
three-way, not two-way.** YAML alias to an anchored `<b>`: **exit 1** — skills-ref refuses the
*anchor* at parse time (`strictyaml`), so the description is never validated. Escaped `\u003c` in a
double-quoted scalar: **exit 0** — `validate` accepts it; only `read-properties` reveals the
decoded `<skills>`. Literal `<skills>` and `->`: **exit 0** — skills-ref has no description
character rule at all. So the lane's `trigger.no_xml_tag` is not a subset of skills-ref's verdict
set: the two disagree in both directions (lane FAILs on `<skills>`, skills-ref accepts it;
skills-ref FAILs on the alias, the lane checker PASSes it).

F5. **The lane's own SKILL.md passes skills-ref.** Copied to `lane-copy/kotoba-shokunin/` (directory
name matching its `name:`), copy sha256 `1923484600b5879c16d390aff43698f0974616946150c0b20787ed5e65d3ee22`
(equal to the lane file), `validate` exit 0. The lane file changed during this seat's run (a
sibling edited the portability-floor sentence at 05:27); the copy was refreshed and re-validated.

F6. **Supplementary controls** (beyond the assigned 11, to map rules to authorities): name length 64
passes / 65 fails; leading- and trailing-hyphen names fail; uppercase Unicode (`Café-Skill`) fails;
`claude-tools` **passes** (skills-ref enforces no reserved words).

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

Supplementary controls, same tool: `name-64-chars` 0 Valid; `name-65-chars` 1 ("exceeds 64 character limit (65 chars)" + dir-mismatch line); `name-leading-hyphen` / `name-trailing-hyphen` 1 ("Skill name cannot start or end with a hyphen"); `name-uppercase-unicode` 1 ("must be lowercase"); `name-digit-only` 1 (dir-mismatch line); `claude-tools` 0 Valid; `desc-1024-control` 0 Valid.

## Cross-check against the lane's own checker (`trigger.no_xml_tag`)

`python3 -B verifiers/verify_skill_checklist.py --skill <fixture>/SKILL.md --check
trigger.no_xml_tag --json` from the lane root (exit 1 on FAIL). skills-ref exit / lane verdict:
`desc-skills-tag` (`<skills>`) 0 / FAIL (`'<skills>'`); `desc-arrow` (`->`) 0 / PASS;
`desc-escaped-unicode` (`\u003c`) 0 / FAIL (`'\\u003c'`); `desc-alias` (`*desc` → `<b>`) 1 (parse)
/ PASS; `café-skill` 0 / PASS; `Uppercase-Name`, `double--hyphen`, `mismatched-dir`,
`unknown-field`, `desc-1025` 1 / PASS (no such lane rule).

## Evidence — commands, exit codes, hashes

```
uv tool install skills-ref==0.1.1                     exit 0 → ~/.local/bin/agentskills
~/.local/bin/agentskills --version                    exit 0 "agentskills, version 0.1.1"
uv venv --python 3.12 upstream-venv                   exit 0
uv pip install "git+https://github.com/agentskills/agentskills@69ef37e9…#subdirectory=skills-ref"  exit 0
upstream-venv/bin/skills-ref --version               exit 0 "skills-ref, version 0.1.0"
git ls-remote …/agentskills.git HEAD refs/heads/main  exit 0  → 69ef37e9424c0a7ea9dd2293b559e43ec8176379
```

Hashes: PyPI wheel `d35db5bb…f461b5`; PyPI sdist (93,519 B) `6b400ca6…d2695`; upstream
`validator.py` @ `69ef37e9` (= @ `f130f348`, 5,154 B) `b5ee3d85…5f6c5`; upstream `parser.py`
`9a74c9a9…c211`; installed (PyPI 0.1.1) `validator.py` `7b5cb3dc…906` and `parser.py`
`f1599cab…6ffa`; `specification.md` (7,608 B) `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`;
`quick_validate.py` @ `dbd4588` (context only, S012, 3,972 B) `67cf5703…e365`. Scratch transcripts:
`skills-ref-transcript.txt` `dfeb3bf4…cf22`, `skills-ref-upstream-transcript.txt` `f094c8d0…4595`,
`cross-validator-summary.json` `f6c9cf84…8f61`, `pypi-vs-upstream-69ef37e9.txt` `f3abd5ca…387c`
(per-fixture `SKILL.md` hashes are in `cross-validator-summary.json`).

## Sources opened this session (URL, access time UTC, located quote ≤25 words)

1. `https://agentskills.io/specification.md` — 2026-10-22T08:35:54Z, HTTP 200, 7,608 B. § `#### name
   field` :64 "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens
   (`-`)" ; :66 "Must not contain consecutive hyphens (`--`)" ; :67 "Must match the parent
   directory name" ; § `#### description field` :101 "Must be 1-1024 characters" ; § Validation
   :257 "skills-ref validate ./my-skill".
2. `…/agentskills/agentskills/69ef37e9…/skills-ref/src/skills_ref/validator.py` — 2026-10-22T08:35:55Z,
   HTTP 200, 5,154 B; `_validate_name` :54 `if not all(c.isalnum() or c == "-" for c in name):`;
   :46 "must be lowercase"; :52 "no consecutive hyphens"; :111 "Unexpected fields in frontmatter".
3. `…/agentskills/agentskills/69ef37e9…/skills-ref/README.md` — 2026-10-22T08:35:54Z, HTTP 200,
   2,166 B. :52 "the `skills-ref` executable will be available on your `PATH`" ; :6 "This library is
   intended for demonstration purposes only." (README documents the name the PyPI wheel does not install — F2.)
4. `https://pypi.org/pypi/skills-ref/json` — 2026-10-22T08:35:55Z, HTTP 200, 8,277 B.
   summary "Reference library for Agent Skills"; versions `["0.1.0","0.1.1"]`; project URL
   `https://github.com/anthropics/agentskills` (**404 today**) while the code lives at
   `https://github.com/agentskills/agentskills` (HTTP 200) — dead repo.
## Risks / blockers

- **SOURCES citation hazard for the C2 entry.** A row citing "skills-ref `validator.py` sha256
  `b5ee3d85…`" while the run used the PyPI wheel describes different bytes (`7b5cb3dc…`). The C2
  entry as drafted pairs the git blob hash with "PyPI `skills-ref` 0.1.1 run as `agentskills
  validate`" in one sentence; the two identifiers are not the same artefact. Behavioural equality
  (F3) means no verdict changes, but the citation should name which artefact was executed. Noted,
  not edited — the entry belongs to the scribe seat.
- Upstream `pyproject.toml` version `0.1.0` while PyPI publishes `0.1.1`; the utf-8 read fix is PyPI-only.
- The upstream README marks the library "intended for demonstration purposes only", so a skills-ref
  verdict is a reference-implementation verdict, not a client-loading verdict.
- Tooling: `uv tool install` (PyPI) and `uv venv` + `uv pip install` from the official GitHub
  repository. No pacman transaction, no host service restart; the pacman guard was not engaged.
