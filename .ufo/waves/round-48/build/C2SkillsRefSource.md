# C2 source — agentskills reference validator `skills-ref`: pinned validation code, and the angle-bracket question

Seat: `KotobaR48.C2SkillsRefSource` (leaf scout). Date: 2026-10-22. Scope: the `skills-ref`
reference validator at `agentskills/agentskills`. Read-only on the lane; all fetching, cloning and
execution happened in `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2SkillsRefSource/`.

## Findings

**F1 — Pin.** Upstream tip `main` = `69ef37e9424c0a7ea9dd2293b559e43ec8176379` (committer date
`2026-08-09T20:36:04Z`, subject `docs: add OpenClaw to client showcase (#492)`, tree
`65e11c9faad14a022055ce0ff3ebf99f2b55142f`), confirmed twice this session: `git ls-remote` on the
clone's `origin` (HEAD and `refs/heads/main` both that sha) and the GitHub commits API
`/commits/main`. The repo has 145 commits; `skills-ref/` declares version `0.1.0`.

**F2 — Answer to the assigned question: `skills-ref` does NOT ban angle brackets in `description`.**
The whole description rule is non-empty-string plus a 1024-character cap (`validator.py:70-84`);
no character, tag or bracket predicate exists anywhere in the package. Angle brackets are instead
*tolerated and escaped at prompt-render time*: `prompt.py:43,46` wrap name and description in
`html.escape(...)`, and the package's own test asserts it — `tests/test_prompt.py:55-69` feeds
`description: Use <foo> & <bar> tags` and asserts `"&lt;foo&gt;" in result` / `"<foo>" not in result`.
A repo-wide tracked-file search for `angle` returns zero matches (`git grep -c -i angle` exit 1);
`bracket` matches only Apache-2.0 boilerplate (`LICENSE:182,184`). So the round-47 SOURCES S011
adjudication ("credits an angle-bracket ban to the agentskills.io spec which has none") holds for
the spec text **and** for the reference validator; the ban lives only in the *other* authority,
Anthropic's `quick_validate.py` (S012). The spec's rule list for `description`
(`docs/specification.mdx:93-96`) is `Must be 1-1024 characters` plus two `Should` bullets — no
bracket rule, no escaping rule.

**F3 — There is no name regex anywhere in this authority.** The package never imports `re`
(`git grep -n "^import re\|^from re\|re\.compile\|re\.match" -- skills-ref/src/` → no matches), and
no `mdx`/`md` file in the repo contains a character-class pattern
(`git grep -n -E '\[a-z0-9\]|\[0-9a-z\]|\^\[|\$/' -- '*.mdx' '*.md'` → no matches). The spec states
the name rule as prose (`docs/specification.mdx:60-65`); the validator implements it procedurally:

| Rule | file:line (pinned) | Quote (≤25 words) |
|---|---|---|
| non-empty string, length cap 64 | `validator.py:10,33-35,39-43` | `MAX_SKILL_NAME_LENGTH = 64`; `"Field 'name' must be a non-empty string"`; `f"Skill name '{name}' exceeds …"` |
| Unicode normalization, lowercase | `validator.py:37,45-46` | `name = unicodedata.normalize("NFKC", name.strip())`; `f"Skill name '{name}' must be lowercase"` |
| hyphen edges, no `--` | `validator.py:48-52` | `"Skill name cannot start or end with a hyphen"`; `"Skill name cannot contain consecutive hyphens"` |
| character class | `validator.py:54-58` | `if not all(c.isalnum() or c == "-" for c in name):` |
| directory match | `validator.py:60-65` | `dir_name = unicodedata.normalize("NFKC", skill_dir.name)` … `"must match skill name"` |
| description: non-empty, ≤1024 | `validator.py:11,74-83` | `MAX_DESCRIPTION_LENGTH = 1024`; only the empty check and the length check exist |
| compatibility: must be `str`, ≤500 | `validator.py:12,87-101` | `"Field 'compatibility' must be a string"` … `MAX_COMPATIBILITY_LENGTH = 500` |
| allowed fields / unknown fields | `validator.py:14-22,104-113` | `extra_fields = set(metadata.keys()) - ALLOWED_FIELDS`; `"Unexpected fields in frontmatter: …"` |
| required wiring + entry point | `validator.py:118-147,150-176`, `cli.py:27-50` | name, description required, `compatibility` only if present; CLI exits 1 on any error |

The `isalnum()` predicate is Unicode-aware, so the code is **looser than an ASCII regex**: `技能`,
`мой-навык` and even Arabic-Indic digit `٣` and fullwidth `ｆｕｌｌ` (NFKC-folded) validate (observed
below). The spec's wording is ambiguous — `docs/specification.mdx:62` says `May only contain unicode
lowercase alphanumeric characters (a-z, 0-9) and hyphens (-)` — but the shipped tests
(`tests/test_validator.py:165-219`) lock in the Unicode reading.

**F4 — `license` is whitelisted but never validated** (`validator.py:14-22` lists it;
`validate_metadata` at `validator.py:131-147` checks only name/description/compatibility). An
integer `license` validates (observed). `metadata` is coerced to `str`→`str` in the parser
(`parser.py:61-62`), stringifying nested maps — `metadata: {outer: {inner: 1}}` returns
`"outer": "{'inner': '1'}"`. Unknown *top-level* keys are hard errors, while
`docs/specification.mdx:151` points authors at `metadata` as the escape hatch (`Clients can use this
to store additional properties not defined by the Agent Skills spec`).

**F5 — Discovery and encoding.** `find_skill_md` accepts `SKILL.md` or lowercase `skill.md`
(`parser.py:23`); `validate()` (`validator.py:172`) and `read_properties()` (`parser.py:89`) call
`read_text()` with no explicit encoding, so decoding follows the platform default.

**F6 — YAML strictness beats the field rules.** The parser uses `strictyaml` (`parser.py:11,55-59`),
which rejects anchors/aliases outright, so the round-47 "YAML alias" counterexample never reaches the
field validators here: fixtures with `&d`/`*d` in description or `metadata` exit 1 with `Invalid YAML
in frontmatter: … Found confusing disallowed anchor token`. Alias handling differs per authority —
this one fails closed at parse time.

**F7 — Raw text vs parsed value (double-escape trap).** `\u003c` inside a double-quoted YAML scalar
parses to `<` (so `read-properties` prints `Use <foo> escaped form`) and is re-escaped to `&lt;` by
`to_prompt`. A literal entity `&lt;` stays literal in the parsed value and is escaped *again* to
`&amp;lt;` — a lexical checker reading raw bytes and this validator reading parsed values disagree on
the same file, and neither is "the" answer.

**F8 — Freshness trap: the newest PyPI artifact is older than the pinned main tree.** PyPI has
`skills-ref` 0.1.0 and 0.1.1, both uploaded `2026-01-10`; the GitHub pin is `2026-08-09`. The 0.1.1
sdist ships an **older** `docs/specification.mdx` (its name bullet reads `May only contain unicode
lowercase alphanumeric characters and hyphens (a-z and -)`), CRLF endings, and
`read_text(encoding='utf-8')` at `validator.py:172` / `parser.py:89`, where main has plain
`read_text()` (the only semantic difference in the Python sources; normalized diffs of `prompt.py`,
`models.py`, `cli.py` are empty). Pinning "the reference validator" by version number alone pins an
older authority than main; pin the commit.

**F9 — Rule-surface stability.** `validator.py` and `prompt.py` each have exactly one commit of
history (`547831f`, `2025-12-18`, `Add skills-ref library (#2)`); the *spec* document has moved since
(last change `217be54`, `2026-08-04`), so the executable rule surface predates the current spec prose
by ~8 months — relevant to any row treating spec text and validator behavior as one authority.

**F10 — Real-fixture census (sibling-supplied inputs, independently run).** Pinned
`skills-ref validate` over the 18 fleet lane `SKILL.md` files: 12 fail, 6 pass (`chousa`, `kengaku`,
`kotoba`, `kotodama`, `mori`, `tameshi`). Ten fail with `Invalid YAML in frontmatter: mapping values
are not allowed here` at line 3 — the same byte class PyYAML 6.0.3 `safe_load` rejects (plain scalar
containing `: `), now reproduced by a second, independent YAML implementation (`strictyaml`), so that
divergence is not PyYAML-specific. Two fail for a reason the sibling did not report: `lore-shokunin`
and `souji-shokunin` have **no `name` field at all** (frontmatter top-level keys = `['description']`),
a required-field violation (`docs/specification.mdx:60`, `validator.py:134-135`), not a YAML issue.
The two vendored upstream skills fail solely on the length cap with the sibling's numbers reproduced
exactly: `create-toolset` 1054 chars, `unreal-skill` 1041 chars (both parse cleanly).
`kotoba-shokunin`'s own `SKILL.md` passes the reference validator.

## Evidence

Clone: `git clone -q https://github.com/agentskills/agentskills.git repo` in `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2SkillsRefSource/` → exit 0.
`git ls-remote origin HEAD refs/heads/main` → `69ef37e9…` for both; GitHub API `/commits/main` →
`api_sha=69ef37e9…`, `api_date=2026-08-09T20:36:04Z` (accessed 2026-10-22T08:11Z).

File sha256 at the pin: `validator.py b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5`,
`prompt.py 8ed90a61685b84050a8fde32e63d5f3f04c205b05bfc5f8ef4bb2f101cc9cf15`,
`parser.py 9a74c9a90eb217b82bec27570332eab74547acfbee2973c0a8bcd23f6c7bc211`,
`docs/specification.mdx b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220`.

Execution: the pinned package was installed into a scratch venv (`uv venv`;
`uv pip install -e repo/skills-ref`, resolving `strictyaml 1.7.3`, `click 8.5.0`; dist version
`skills-ref 0.1.0`) — the named validator from the item, not arbitrary fetched code.
`skills-ref validate` / `read-properties` / `to-prompt` results (exit codes verbatim):

| Fixture | Command | Exit | Observed |
|---|---|---|---|
| `description: Use <foo> & <bar> tags…` | validate | 0 | `Valid skill` — no bracket complaint |
| same fixture | to-prompt | 0 | `Use &lt;foo&gt; &amp; &lt;bar&gt; tags when the user asks` |
| `description: Compare a < b for sorting tasks` | validate | 0 | `Valid skill` |
| `description: Use &lt;foo&gt; entity form` | to-prompt | 0 | `Use &amp;lt;foo&amp;gt; entity form` (double escape) |
| `name: 技能` in `技能/`; `name: ٣` in `٣/`; `name: ｆｕｌｌ` in `ｆｕｌｌ/` | validate | 0 | `Valid skill` (NFKC + Unicode `isalnum`; non-ASCII digit, fullwidth) |
| `x-custom:` top-level key | validate | 1 | `Unexpected fields in frontmatter: x-custom. Only ['allowed-tools', 'compatibility', 'description', 'license', 'metadata', 'name'] are allowed.` |
| `compatibility:` as a list / as a string | validate | 1 / 0 | `Field 'compatibility' must be a string` / `Valid skill` |
| `license: 42` | validate | 0 | `Valid skill` (license unvalidated) |
| `metadata: {outer: {inner: 1}}` | read-properties | 0 | `"outer": "{'inner': '1'}"` |
| `description:` as a YAML list | validate | 1 | `Field 'description' must be a non-empty string` |
| `x: &d` anchor + `description: *d`; `&x`/`*x` in `metadata` | validate | 1 | `Invalid YAML in frontmatter: … Found confusing disallowed anchor token` |
| only `skill.md` (lowercase) present | validate | 0 | `Valid skill` |
| 10 fleet lane `SKILL.md` (sibling list) | validate | 1 | `Invalid YAML in frontmatter: mapping values are not allowed here` (line 3) |
| `lore-shokunin`, `souji-shokunin` | validate | 1 | `Missing required field in frontmatter: name` |
| vendored `create-toolset` / `unreal-skill` | validate | 1 | `Description exceeds 1024 character limit (1054 chars)` / `(1041 chars)` |
| `kotoba-shokunin` (this lane) | validate | 0 | `Valid skill` |

Full `mado-shokunin` error text: `Invalid YAML in frontmatter: mapping values are not allowed here in "<unicode string>", line 3, column 66: … desktop & compositor craft. Rank: shonen (probation).`

Scratch tooling recorded: `uv 0.13.0` (already on PATH, no host install), venv inside the seat scratch only; **no pacman/npm/cargo installs, no host service restarts, no lane writes except this report file**.

## Remaining unknowns (not this seat's scope)

1. Whether the live `agentskills.io/specification` page (S001) matches the pinned in-repo
   `docs/specification.mdx` byte-for-byte — the spec page is S001's row, not opened here.
2. Which of `skills-ref`/PyPI 0.1.1/`quick_validate.py` a given client (opencode, omp, Codex)
   actually executes — S012/S013 territory.
3. The lane's own `trigger.frontmatter_parses` / `trigger.no_xml_tag` behavior on these fixtures, and
   whether upstream adds a description character rule after this pin (none at `69ef37e9`).
