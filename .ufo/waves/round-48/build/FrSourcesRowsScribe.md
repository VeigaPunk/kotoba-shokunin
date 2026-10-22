# FrSourcesRowsScribe — round-48 frontier: SOURCES registry rows S016+

Seat: `KotobaR48.FrSourcesRowsScribe` (leaf scribe, no dispatch). Date: 2026-10-22 (UTC, 08:13–08:22Z).
Scope: draft the `corpus/SOURCES.md` rows this round needs, opening every source myself.
Read-only on the lane; the only lane file written is this report. Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/FrSourcesRowsScribe/`.
Contract read first: fleet `CORPUS.md` § "SOURCES.md — where a shokunin learns" (v1, frozen 2026-10-19) and `kotoba-shokunin/corpus/SOURCES.md`.

## Findings

**F1 — S003's teach cell is wrong, and the error is the one the round-47 falsify wave named.**
Its last clause reads "an Anthropic-only rule the open spec lacks", attached to the 500-line body rule
(live cell `corpus/SOURCES.md:16`, verified at base `75f671b`). The open spec states that rule:
`agentskills.io/specification.md:237` "Keep your main `SKILL.md` under 500 lines. Move detailed reference
material to separate files." (fetched today, HTTP 200, 7608 B, sha256 `9a67de89…` — byte-identical to the
round-47 fetch, so this is not drift). S019 supersedes it; S003 stays. This class is mined as M27 by seat
`KotobaR48.FrMistakeScribe` (`.ufo/waves/round-48/build/FrMistakeScribe.md`), whose attribution checker
holds my S019 wording 8/8 (exit 0) against the live cell (exit 1).

**F2 — S001's teach cell is wrong in three ways, and its anchor names a heading that does not exist.**
The live page's headings are `### Frontmatter`, `#### \`name\` field`, `#### \`description\` field`,
`## Progressive disclosure` — there is no "Skill metadata table" (S001's anchor, defect already recorded
in `corpus/lessons/round-47.md` § Gate). S001's teach cell (a) writes the charset as "lowercase-hyphen
chars", dropping the digits the spec allows (`specification.md:27` "Lowercase letters, numbers, and
hyphens only"); (b) drops the consecutive-hyphen rule (`:64` "Must not contain consecutive hyphens
(`--`)"); (c) omits that the spec states the charset twice in two different words — `:62` "May only
contain unicode lowercase alphanumeric characters (`a-z`, `0-9`)" versus `:27` "Lowercase letters,
numbers, and hyphens only". That third fact is the decisive one for C2's Unicode-name counterexample.
The live page and the pinned in-repo `docs/specification.mdx` @ `69ef37e9` carry the same headings and rule
sentences (normalized diff: MDX→markdown rendering only) — answering seat `C2SkillsRefSource`'s question 1.
S018 supersedes S001; S001 stays.

**F3 — Two new authorities, both opened and pinned.** The spec's own reference validator (`skills-ref`,
`agentskills/agentskills` @ `69ef37e9`) and opencode 1.19.3's skill discovery (`anomalyco/opencode` @ tag
`v1.19.3` = `e3c4eb24`). Facts that decide C2 and C1 respectively: `skills-ref` has **no description
character rule at all** (non-empty + 1024 cap) and tests the name charset with Unicode-aware
`str.isalnum()` after NFKC folding; opencode scans **every configured config directory** with the glob
`{skill,skills}/**/SKILL.md`, so `<config-dir>/skill|skills/<name>/SKILL.md` are discovery roots whether
or not the run log names them.

**F4 — Id allocation (no reuse).** `S016` is the opencode row, the id seat
`KotobaR48.C1UpstreamLoaderSource` already proposed for it in
`.ufo/waves/round-48/build/C1UpstreamLoaderSource.md:48`; my draft reproduces that row verbatim so the
integrator lands one row, not two. `S017`–`S019` are mine, unused at the lane base (S001–S015 present,
census `rows=15`); `S017` was unclaimed — seat `C2SkillsRefSource` filed findings but no row id.

**F5 — Superseding rows necessarily re-use the superseded row's URL.** The maintained census emits
`W04 duplicate url … across scopes` for S018 and S019 (warning, not error; exit 0) — fleet practice, not a
defect: the fleet-wide run shows 143 such warnings and 0 E-codes. `E04` (duplicate URL *within* a scope) is
exempted for rows whose teaches cell contains `supersedes S0NN`, which both rows do.

**F6 — Rows are drafted `queued` / used-by `—`, and that is deliberate.** At draft time no corpus file
cites them; the census check "mined rows whose used-by paths do not exist — must print nothing" would
fail if a row were marked `mined` before its citing file exists. When the C2 knowledge entry lands, flip
in the same commit and log old→new in the round lesson (contract rule 2): `S017/S018/S019: queued→mined,
used-by —→corpus/knowledge/frontmatter-rule-authorities-round48.md` (add `corpus/lessons/round-48.md` if
the lesson cites them in its Gate table). Without that flip the rows stay `queued` and rule 4's expansion
trend does not count them.

**F7 — Landing state observed in the working tree (read-only check, no edit by me).** S016–S019 are landed
in `corpus/SOURCES.md` with the promotion applied (S017–S019 `mined`, used-by `corpus/knowledge/frontmatter-rule-authorities-round48.md`;
S016 `mined`, used-by `corpus/lessons/round-48.md`). The lesson file landed at `887b6af` (HEAD `84b9c9ba`),
so the earlier E11 is closed: `scripts/sources-census.sh validate --file kotoba-shokunin/corpus/SOURCES.md
--today 2026-10-22` → exit 0, no E-codes; W04 same-URL warnings remain for S018/S019/S021 (expected cost of
rule 2 superseding + S021, fleet-significant). The landed S016 cell is more honest than the one I drafted —
the verifier reads no upstream discovery fact, so naming it as a consumer asserts a dependency the code lacks
(row author's position). If the lesson had slipped, the only alternative would be status `queued` + used-by
`—` (the S004–S007 / S010 shape); `mined` + `—` would trip the CLI's W03 "mined but unused". Any such move
is logged old→new in the round lesson (rule 2).

## Draft rows (paste-ready; 11 columns, census-clean)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S016 | anomalyco/opencode — skill discovery, tag v1.19.3 — https://github.com/anomalyco/opencode/blob/v1.19.3/packages/opencode/src/skill/index.ts#L24 | code | A | Which directories under an opencode config directory are scanned for SKILL.md, and at what depth | `packages/opencode/src/skill/index.ts:24` `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"`; `:205-207`; `config/paths.ts:23-40`; tag v1.19.3 = commit `e3c4eb242585dcd77be1a867391b7c25fd47ce52`; opened 2026-10-22 | Both `skill/` and `skills/` under every configured directory are scanned recursively, and `**` also matches zero segments, so a `SKILL.md` directly in either dir loads; identity is the frontmatter name, not the directory name | mined | 2026-10-22 | on-release | verifiers/verify_harness_independent.py |
| S017 | agentskills/agentskills — skills-ref reference validator v0.1.0 — https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref | code | A | What the open spec's own reference validator enforces for SKILL.md frontmatter (name, description, compatibility, unknown fields) | `skills-ref/src/skills_ref/validator.py:10-113` and `parser.py:36-73` at commit `69ef37e9424c0a7ea9dd2293b559e43ec8176379` (main tip, 2026-08-09); `pyproject.toml` version 0.1.0, `strictyaml>=1.7.3`; opened 2026-10-22 | The spec's own validator has no description character rule at all (non-empty plus a 1024-character cap) and tests the name charset with the Unicode-aware `str.isalnum()` after NFKC folding, so it accepts what an ASCII-only regex rejects; its README marks the library demonstration-only | queued | 2026-10-22 | on-commit | — |
| S018 | Agent Skills — Specification — https://agentskills.io/specification | spec | A | SKILL.md frontmatter field rules, with the page's own headings and the pinned file that renders them | § Frontmatter table, § `name` field, § `description` field, § Progressive disclosure; live page fetched as https://agentskills.io/specification.md (200, 7608 B, sha256 `9a67de89…`) on 2026-10-22, byte-identical to the round-47 fetch; the same rule text in the pinned source `docs/specification.mdx` at commit `69ef37e9` (lines 27, 61-65, 94, 224) | supersedes S001 — the page has no "Skill metadata table" heading, so S001's anchor named a heading that does not exist; the name rule is stated twice in different words ("unicode lowercase alphanumeric" in § `name` field versus "Lowercase letters, numbers, and hyphens only" in the Frontmatter table) and S001's teach cell drops the consecutive-hyphen rule | queued | 2026-10-22 | 90d | — |
| S019 | Claude Docs — Agent Skills best practices — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | docs | A | Anthropic's authoring rules for name and description | § Skill structure field list, § Writing effective descriptions, § Progressive disclosure patterns; fetched as .../best-practices.md (200, 42169 B, sha256 `f0a5d61b…`) on 2026-10-22; the round-47 fetch was 42028 B, sha256 `727f3fa1…` — editorial drift only, the rule lines are unchanged | supersedes S003 — the 500-line body rule is not Anthropic-only: the open spec states it too (S018 § Progressive disclosure); Anthropic-only are the no-XML-tags rule on both `name` and `description`, the reserved words "anthropic" and "claude", and the third-person description rule | queued | 2026-10-22 | 90d | — |

## Lesson Gate lines (paste into `corpus/lessons/round-48.md` § Gate)

| row | URL | accessed | ≤25-word quote (location) |
|---|---|---|---|
| S016 | https://github.com/anomalyco/opencode/blob/v1.19.3/packages/opencode/src/skill/index.ts (tag v1.19.3 = `e3c4eb24`) | 2026-10-22T08:13:22Z | `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` (`packages/opencode/src/skill/index.ts:24`) |
| S017 | https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref/src/skills_ref/validator.py | 2026-10-22T08:16Z | `if not all(c.isalnum() or c == "-" for c in name):` (`skills-ref/src/skills_ref/validator.py:54`) |
| S018 | https://agentskills.io/specification | 2026-10-22T08:14:16Z (HTTP `date:` header) | "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)" (§ `name` field, `specification.md:64`) |
| S019 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices | 2026-10-22T08:16Z | "Cannot contain XML tags" (§ Skill structure, `best-practices.md:155` and `:162`) |

Sweeps that ground the negative claims (contract rule 5 — a negative claim carries its sweep):
- S017 has no angle-bracket rule: `grep -c '<' skills-ref/src/skills_ref/validator.py` → **0** (exit 1);
  `git -C as-repo grep -c -i angle` → **0** (exit 1); the only `xml`/`bracket` hits in the package are the
  `<available_skills>` prompt wrapper (`prompt.py:1,10,12,20`, `cli.py:81`), and `prompt.py:43,46`
  `html.escape` the name and description rather than rejecting them.
- The open spec carries no XML rule and no third-person rule: `grep -ci 'xml' specification.md` → **0**
  (exit 1); `grep -ci 'third person'` → **0** (exit 1); `grep -n '500 lines'` → 1 hit (`:237`, exit 0) — so
  the XML-tag, reserved-word and third-person rules are Anthropic-only and the 500-line rule is shared: the
  exact inverse of what S003's teach cell claims.

## Evidence (commands run this session, exit codes verbatim)

```
$ curl -fsSL -o /tmp/spec_now.md -w 'http=%{http_code} size=%{size_download}\n' https://agentskills.io/specification.md → http=200 size=7608 (exit 0); sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16
$ grep -ci 'xml' specification.md      → 0  (exit 1) ; grep -ci 'third person' …  → 0  (exit 1)
$ grep -n '500 lines' specification.md → 237:Keep your main `SKILL.md` under 500 lines. …  (exit 0)
$ curl -fsSL …/agent-skills/best-practices.md → http=200 size=42169 (exit 0); sha256 f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960 ; diff vs round-47 copy → editorial only, rule lines identical
$ git clone --depth 1 --branch v1.19.3 https://github.com/anomalyco/opencode.git oc-1.19.3   (exit 0)
$ git -C oc-1.19.3 rev-parse HEAD → e3c4eb242585dcd77be1a867391b7c25fd47ce52 ; git describe --tags → v1.19.3
$ sha256sum oc-1.19.3/packages/opencode/src/skill/index.ts → 91dce57f590e1ad3… ; config/paths.ts → cd86a34461b27caf… ; core/global.ts → 37c9aae045e01cd2… (identical to the raw fetches; `global.ts:64` `config: Flag.OPENCODE_CONFIG_DIR ?? Path.config`)
$ grep -n 'state.skills\[md.data.name\] = {' oc-1.19.3/packages/opencode/src/skill/index.ts → 134 (identity is the frontmatter name); scan site :205-207, pattern :24
$ git clone --depth 1 https://github.com/agentskills/agentskills.git as-repo (exit 0) → HEAD 69ef37e9424c0a7ea9dd2293b559e43ec8176379 ; validator.py sha256 b5ee3d8537c83c95… (identical to the raw fetch)
$ curl -sSL https://pypi.org/pypi/skills-ref/json → http 200; latest 0.1.1 (uploaded 2026-01-10); pinned pyproject says 0.1.0
$ opencode --version → 1.19.3 (exit 0); live ~/.local/bin/opencode
```

Census, frozen contract commands, lane base vs. candidate (`SOURCES_candidate.md` = base + the four rows):
```
base:    rows=15  malformed=0  tier A=14 C=1  status mined=6 queued=8 rejected=1  dup-ids=none  enum-violations=none
candidate: rows=19  malformed=0  tier A=18 C=1  status mined=7 queued=11 rejected=1  dup-ids=none  enum-violations=none
$ bash scripts/sources-census.sh validate --file <candidate> --today 2026-10-22   → exit 0
  W04 S018 duplicate url agentskills.io/specification across scopes ; W04 S019 duplicate url …/agent-skills/best-practices across scopes
$ bash scripts/sources-census.sh validate --file kotoba-shokunin/corpus/SOURCES.md --today 2026-10-22 → exit 0, no findings (base)
$ bash scripts/sources-census.sh validate --today 2026-10-22 (fleet)  → exit 0; 143 W04 fleet-wide, 0 E-codes
```
(The candidate was validated from a scratch mirror symlinking the lane's `SKILL.md`, `verifiers/` and `corpus/knowledge/`.)

## Touched surfaces

- Written in the lane: this report only — `.ufo/waves/round-48/build/FrSourcesRowsScribe.md`; not written: `corpus/SOURCES.md`, `corpus/lessons/round-48.md`, `corpus/knowledge/*` (drafting only).
- No git/jj write command was run in the lane, the fleet repo, or any sibling lane. Scratch clones
  (`oc-1.19.3`, `as-repo`) live only under this seat's scratch directory. Tooling: no install, no upgrade,
  no host service touched; `git`, `curl`, `grep`, `awk`, `sha256sum`, `python3` only.

## Out of scope / not claimed

- **S010** (`verifiers/verify_skill_checklist.py` own-work row) and **S013** (Codex skills doc) also carry
  routed defects per `corpus/lessons/round-47.md` § Gate (S010's teach cell is stale since
  `trigger.no_xml_tag` landed; S013 needs version-pinned semantics). No row is drafted here — id
  allocation for those belongs to whoever drafts them; S018/S019 do not depend on them.
- I did not re-open S002, S004–S008, S011, S014, S015 (no status change needed; S011's rejection still
  holds: the spec has 0 `xml` hits, confirmed today), and I make no claim about what any specific client
  (opencode, omp, Codex) executes at runtime; the rows speak only to the sources' own text.
- The W04 warnings from F5 are the accepted cost of rule 2's superseding mechanism; a lane wanting zero
  warnings could anchor S018 to the pinned `docs/specification.mdx` URL (different URL, same text) instead.

## Artifacts

- Report: `.ufo/waves/round-48/build/FrSourcesRowsScribe.md`; draft rows and census candidate:
  `/fast/scratch/hyaku/kotoba-r48-a2/seats/FrSourcesRowsScribe/{draft_rows.md,SOURCES_candidate.md}`
  (mirror `cand-lane/corpus/SOURCES.md`); fetched sources: `agentskills_spec.md`,
  `claude_bp_5d0c1222.md`, `sr_skills-ref_src_skills_ref_{validator,parser}.py`,
  `oc_packages_opencode_src_skill_index.ts`, `oc_paths.ts`, `oc_flag.ts` (same directory).
