# C2EntryScaffoldScribe — decision-table draft for `corpus/knowledge/frontmatter-rule-authorities-round48.md`

Seat `KotobaR48.C2EntryScaffoldScribe` (leaf scribe), 2026-10-22. Read-only on the lane; this report
is the only lane write. Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2EntryScaffoldScribe/`
(private clone of the lane at `75f671b109d8eddd0d64c1429bd6379fe577175a` + probe fixtures).
No product file, judge, commit, push or publish was touched. No pacman transaction (host-wide pause).

## Findings (decision-table draft — the deliverable)

Cell discipline: a cell carries a quotable rule or an explicit `not stated (searched: <how>)`
(Q14). Sources, with the bytes I opened (UTC access times and hashes in § Evidence):

- **S001** = `https://agentskills.io/specification.md` (sha256 `9a67de89…`, 260 lines)
- **S-ref** = `agentskills/agentskills` @ `main` `69ef37e9…`, `skills-ref/src/skills_ref/validator.py`
  (sha256 `b5ee3d85…`); PyPI `skills-ref` 0.1.1 installed, validator/parser/prompt/models byte-equal
  to `main` after normalizing `read_text(encoding='utf-8')` → `read_text()` (verified by diff).
- **S003** = `platform.claude.com/…/agent-skills/best-practices.md` (sha256 `f0a5d61b…`, 1191 lines)
  and `…/agent-skills/overview.md` (sha256 `7913d455…`)
- **S012** = `anthropics/skills` @ `dbd4588f…`, `skills/skill-creator/scripts/quick_validate.py`
  (sha256 `67cf5703…`, 102 lines)
- **S013** = `learn.chatgpt.com/docs/build-skills.md` (sha256 `ed6e324f…`, 232 lines)
- **Lane** = `verifiers/verify_skill_checklist.py` (lane base `75f671b`)

### Table

| rule | S001 spec | skills-ref validator | Anthropic docs (S003) | Anthropic packager (S012) | Codex (S013) | Lane checker (`verify_skill_checklist.py`) |
|---|---|---|---|---|---|---|
| name length | "Must be 1-64 characters" (`spec.md:63`; table `:30` "Max 64 characters") | `MAX_SKILL_NAME_LENGTH = 64` (`validator.py:10`); observed "exceeds 64 character limit (65 chars)" | "Maximum 64 characters" (`bp.md:153`; restated `bp.md:1133`) | "Name is too long (65 characters). Maximum is 64 characters." (`qv.py:70-71`) | not stated (searched: `grep -niE 'reserved\|third person\|xml\|angle\|500 lines\|1024\|1,024\|64 char\|lowercase\|hyphen\|consecutive' build-skills.md` → 0 hits, exit 1) | no rule — 65-char name passes `trigger.frontmatter_parses` (probe `p_name_65`: PASS) |
| name charset | "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens" (`spec.md:64`) — wording self-conflicting (says unicode, lists ASCII) | `if not all(c.isalnum() or c == "-")` + `NFKC` + lowercase check (`validator.py:37,45-46,54-58`); observed `技能-测试` → "Valid skill" | "Must contain only lowercase letters, numbers, and hyphens" (`bp.md:154`; `ov.md:215`) | `re.match(r'^[a-z0-9-]+$')` (`qv.py:65`); observed `技能-测试` → "should be kebab-case (lowercase letters, digits, and hyphens only)", exit 1 | not stated (same 0-hit sweep as above) | no rule — `Probe-Upper` and `技能-测试` both PASS (`frontmatter_parses`) |
| name = parent directory | "Must match the parent directory name" (`spec.md:67`) | "Directory name '…' must match skill name '…'", both sides NFKC-normalized (`validator.py:60-65`); observed dir `probe－full` + name `probe-full` → "Valid skill" | not stated (searched: `grep -niE 'match the (parent \|skill )?director\|folder name\|directory name'` over `bp.md`+`ov.md` → no rule sentence; `ov.md:208-223` field bullets omit it) | not stated (searched: `grep -n 'dirname\|basename\|parent\|skill_path.name' qv.py` → 0 hits, exit 1) | not stated (0-hit sweep above) | `trigger.name_directory` compares literal strings, no NFKC: dir `probe－full` vs name `probe-full` → FAIL "name 'probe-full' != directory 'probe－full'" |
| consecutive hyphens | "Must not contain consecutive hyphens (`--`)" (`spec.md:66`) | "Skill name cannot contain consecutive hyphens" (`validator.py:52`) | not stated (searched: `grep -niE 'consecutive'` over `bp.md`+`ov.md` → 0 hits, exit 1) | "cannot start/end with hyphen or contain consecutive hyphens" (`qv.py:67`) | not stated (0-hit sweep above) | no rule — `probe--consec` PASSes `frontmatter_parses` |
| description length | "Must be 1-1024 characters" (`spec.md:101`; table `:31`) | `MAX_DESCRIPTION_LENGTH = 1024` (`validator.py:11`); observed 1025-char description → "Description exceeds 1024 character limit (1025 chars)" | "Maximum 1,024 characters" + "Must be non-empty" (`bp.md:160-161`) | "Description is too long (1025 characters). Maximum is 1024 characters." (`qv.py:83-84`); **`description: ""` currently PASSes** ("Skill is valid!", exit 0) — empty-value gate absent | not stated (0-hit sweep above) | min only: empty description FAILs `trigger.frontmatter_parses` ("empty description:"); no max — 1025-char description PASSes |
| description angle brackets / XML tags | not stated (searched: `grep -niE 'angle\|xml' specification.md` → 0 hits, exit 1) | not stated as a validity rule (searched: `grep -niE 'reserved\|person\|angle'` over `validator.py`+`parser.py` → 0 hits); `prompt.py:46` escapes instead (`html.escape(props.description)`); observed `Use <skills> …` → "Valid skill", exit 0 | "Cannot contain XML tags" for `name` and for `description` (`bp.md:155,162`; `ov.md:216,223`) | "Description cannot contain angle brackets (< or >)" — any bracket, not a tag grammar (`qv.py:80`); description only, so `name: probe<angle>` falls out as a kebab-case error | not stated (0-hit sweep above) | `trigger.no_xml_tag` (`verify_skill_checklist.py:1294-1322`; regexes `:404-409`): XML 1.0 markup shapes + YAML `\x3c/\u003c` escapes, applied to the lane's **own structural** `name`/`description` values (not a YAML parse). Observed: `<skills>` → FAIL; `Compare a < b` → PASS; `"… \u003cskills\u003e …"` → FAIL naming `\u003c`. Sibling seat `C2LaneCheckerRun` measured 10 fixtures over the same instrument and the same S012 pin; my figures agree with it case by case |
| third person | not stated (searched: `grep -niE 'third person\|reserved word' specification.md` → 0 hits, exit 1) | not stated (same 0-hit sweep over `validator.py`+`parser.py`) | "Always write in third person" (`bp.md:206`) | not stated (searched: `grep -niE 'reserved\|third person\|500 line' qv.py` → 0 hits, exit 1) | not stated (0-hit sweep above) | no rule — `description: I can help you process Excel files.` PASSes |
| reserved words | not stated (same `reserved word` sweep, 0 hits) | not stated (same sweep); observed `name: claude-tools` → "Valid skill" | "Cannot contain reserved words: \"anthropic\", \"claude\"" (`bp.md:156`; `ov.md:217`); naming list "Reserved words: `anthropic-helper`, `claude-tools`" (`bp.md:191`) | not stated (same 0-hit sweep); observed `claude-tools` → "Skill is valid!", exit 0 | not stated (0-hit sweep above) | no rule — `claude-tools` PASSes `frontmatter_parses` |
| unknown fields | not stated (searched: `grep -niE 'unknown\|unrecognized\|other fields\|additional field' specification.md` → only `:161` "Clients can use this to store additional properties not defined by the Agent Skills spec"; no prohibition on unknown top-level keys) | "Unexpected fields in frontmatter: … Only [...] are allowed." (`validator.py:108-113`); observed `version:` → FAIL, exit 1 | not stated (searched: `grep -niE 'unknown field\|unrecognized\|only these fields'` over `bp.md`+`ov.md` → 0 hits) | "Unexpected key(s) in SKILL.md frontmatter: … Allowed properties are: …" (`qv.py:45-49`); observed `version:` → exit 1 | not stated (0-hit sweep above) | no rule — `version: 1` PASSes `frontmatter_parses` |
| body length | "Keep your main `SKILL.md` under 500 lines." (`spec.md:237`, § Progressive disclosure) | not stated (searched: `grep -niE 'max_lines\|body length\|500 line\|line_count'` over `validator.py`+`parser.py`+`models.py` → 0 hits, exit 1) | "Keep the `SKILL.md` body under 500 lines for optimal performance." (`bp.md:257`; `bp.md:1140`) | not stated (searched: `grep -niE 'body\|lines' qv.py` → 0 hits, exit 1) | not stated (0-hit sweep above) | `trigger.line_budget` (`verify_skill_checklist.py:1327`): threshold taken from the lane's own checklist box "File ≤ 600 lines" (`SKILL.md:246`), `--max-lines` fallback 600. Observed: 505 lines PASS, 605 lines FAIL "605 lines exceed budget 600". **The lane's budget is 600, not the 500 both S001 and S003 state.** |

### Cross-reading the table (the point of the entry)

1. **Only the open spec states the directory-match rule; only Anthropic states reserved words and
   third person.** S001 alone says "Must match the parent directory name"; S003 alone says
   "Cannot contain reserved words" and "Always write in third person"; no other authority mentions
   either (each cell carries its own sweep). This is the per-authority map the entry is for.
2. **Two different angle-bracket rules exist, and the lane is between them.** S003 says "Cannot
   contain XML tags"; S012 bans *any* `<`/`>` (`qv.py:80`); the lane's `trigger.no_xml_tag` bans XML
   1.0 markup shapes plus YAML angle escapes. Measured on the same file `Compare a < b for sorting
   tasks.`: S012 exit 1 ("Description cannot contain angle brackets (< or >)"), lane PASS, skills-ref
   "Valid skill". On `Use <skills> …`: S012 exit 1, lane FAIL, skills-ref "Valid skill".
3. **The lane enforces a body budget of 600 lines where both cited authorities say 500.** The
   lane's number comes from its own checklist box, not from S001/S003 — a lane-local choice, and it
   must not be cited as an S001/S003 rule.
4. **The lane's own frontmatter parse is structural, not YAML**, so it sees different values than
   every YAML client. Measured on `metadata: {note: &d …}` + `description: *d`:
   lane `trigger.frontmatter_parses` reports "description 2 chars" and `trigger.no_xml_tag` PASSes;
   S012 (PyYAML `safe_load`) resolves the alias and reports "Description cannot contain angle
   brackets (< or >)", exit 1; skills-ref (`strictyaml`) rejects the anchor at parse time,
   "Invalid YAML in frontmatter: … Found confusing disallowed anchor token", exit 1. The lane's
   answer is neither authority's answer.
5. **The lane enforces exactly one of the ten rules' authorities** (`trigger.no_xml_tag`, plus the
   name/directory identity check `trigger.name_directory` and a 600-line budget): it has no
   length, charset, hyphen, third-person, reserved-word or unknown-field rule. Each such row is a
   live divergence, not an oversight in the table.

### Routed round-47 counterexamples, re-observed by running the lane checker

| counterexample | lane checker (observed) | S012 `quick_validate.py` | skills-ref |
|---|---|---|---|
| YAML alias hiding `<skills>` in `description` | `frontmatter_parses` PASS "description 2 chars"; `no_xml_tag` PASS | FAIL "Description cannot contain angle brackets (< or >)", exit 1 | FAIL "Invalid YAML in frontmatter: … disallowed anchor token", exit 1 |
| Unicode name `技能-测试` | `frontmatter_parses` PASS, `name_directory` PASS when dir matches | FAIL "should be kebab-case (lowercase letters, digits, and hyphens only)", exit 1 | PASS "Valid skill" (Unicode `isalnum`) |
| escaped value `"… \u003cskills\u003e …"` | `no_xml_tag` FAIL "XML tag in description: '\u003c'" | FAIL "Description cannot contain angle brackets (< or >)", exit 1 | validate PASSes; `read-properties` prints the decoded `<skills>` |

Caveat carried forward: the lane's `no_xml_tag` detail line itself says Anthropic's packager "bans
any '<'/'>' and is stricter". My probes show the packager's rule is indeed broader than the lane's
detector (`Compare a < b` → S012 exit 1, lane PASS), but the detail line asserts the *lane* is
stricter, which the alias probe contradicts (lane PASS, S012 FAIL). Sibling seat `C2LaneCheckerRun`
reached the same conclusion from 10 fixtures and calls the detail string an overclaim (its F5); the
entry should carry the honest wording — *a lexical well-formed-ASCII-tag shape plus a YAML
angle-escape backstop, applied to the lane's unparsed frontmatter text* — and file the detail
string as a text defect.

## Evidence (commands, exit codes, bytes)

| step | command | exit | result |
|---|---|---|---|
| fetch S001 | `curl -sS -o s001.md https://agentskills.io/specification.md` | 0 | 7,608 B, sha256 `9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16`, 260 lines; re-fetch 08:21:04Z identical |
| fetch S003 | `curl -sS -o s003.md …/best-practices.md` (+ `s003_ov.md` overview) | 0 | `f0a5d61b…` 42,169 B 1191 lines; `7913d455…` |
| fetch S013 | `curl -sS -o s013.md https://learn.chatgpt.com/docs/build-skills.md` | 0 | 11,035 B, sha256 `ed6e324f747d47adf6f60ee1fca13ba469b3671f55f58c3a78f35947af6919d5`, 232 lines; `Last-Modified: Thu, 22 Oct 2026 04:05:41 GMT` |
| fetch S012 | `curl -sS -o qv.py https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py` | 0 | 3,972 B, sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365` |
| fetch skills-ref | `curl -sS` `raw.githubusercontent.com/agentskills/agentskills/main/skills-ref/src/skills_ref/{validator,parser,prompt,models}.py` | 0 | `validator.py` sha256 `b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5`; pin `main` = `69ef37e9424c0a7ea9dd2293b559e43ec8176379` (committer date 2026-08-09T20:36:04Z) |
| install validator | `uv tool install skills-ref` | 0 | `skills-ref 0.1.1` → `~/.local/bin/agentskills`; installed `validator.py`/`parser.py`/`prompt.py`/`models.py` normalized-diff equal to `main` (quote style + `read_text(encoding=…)` only) |
| lane clone | `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin lane` | 0 | HEAD `75f671b109d8eddd0d64c1429bd6379fe577175a` |
| lane probes | `python3 -B verifiers/verify_skill_checklist.py --skill <probe> --check trigger.frontmatter_parses --check trigger.name_directory --check trigger.no_xml_tag --check trigger.line_budget --json` | 0 | 24 probe fixtures; per-row statuses quoted in the table |
| S012 probes | `python3 -B /tmp/qv.py <probe>` | 0/1 | messages quoted in the table |
| skills-ref probes | `~/.local/bin/agentskills validate <probe>` | 0/1 | messages quoted in the table |
| absence sweeps | the seven `grep -niE …` sweeps quoted inline in the table cells | 1 (0 hits) | each `not stated` cell names its sweep |
| corpus sweep | `grep -rln "skills-ref\|agentskills" corpus/knowledge/` | 1 | 0 hits — no existing entry covers per-authority frontmatter validity; `git ls-tree -r --name-only HEAD corpus/knowledge \| grep -c '\.md$'` = 34 |

Tooling recorded: `skills-ref` 0.1.1, channel `uv tool install` (PyPI), reason — run the named
reference validator against probe fixtures. `uv 0.13.0` was already on PATH. No pacman, npm or cargo
install; no service restart; no lane file written except this report.

## Gates

- No product gate was run or required by this item (drafting a knowledge-entry table).
- Read-only on the lane confirmed: the only lane write is this file; scratch clone and probes live
  under `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2EntryScaffoldScribe/`.
- Sweep for the entry's claimed novelty re-run here: 0 hits for `skills-ref|agentskills` under
  `corpus/knowledge/`, so no existing entry covers this ground.

## Touched surfaces

- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-48/build/C2EntryScaffoldScribe.md`
  (this report). Nothing else in the lane; no git/jj write command issued.
- Scratch: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2EntryScaffoldScribe/` — clone `lane/`, probes
  `lane/probes{,2..14}/` (24 fixtures), fetched sources in `/tmp`.

## Out of scope (named, not silently dropped)

- Writing `corpus/knowledge/frontmatter-rule-authorities-round48.md` itself — the integrator owns
  the landed entry; this report supplies its decision-table half.
- New `SOURCES.md` rows (S001/S003/S012/S013 supersessions, a `skills-ref` row) — planner/integrator
  scope. This report supplies the bytes and quotes a row would need.
- `code.claude.com/docs/en/skills` and the Anthropic Skills API upload guide (separate Anthropic
  authorities with their own rules: 256-char name refusal, unknown-field hard error on packaging) —
  covered by sibling seat `C2ClaudeDocs`, not re-opened here.
- Codex CLI implementation rules (`MAX_NAME_LEN = 64`, optional name, 1024-char catalog truncation) —
  covered by sibling seat `C2CodexOpencodeDocs`; the S013 *doc* column above stays "not stated".
- opencode's docs/implementation pair — sibling seat, same reason.
- Lane gate re-runs and the C1 arm — other seats.

## Artifacts

- This report: `.ufo/waves/round-48/build/C2EntryScaffoldScribe.md`
- Sibling receipts this table leans on (not re-derived here):
  `.ufo/waves/round-48/build/C2ClaudeDocs.md`, `C2SkillsRefSource.md`, `C2QuickValidateFresh.md`,
  `C2CodexOpencodeDocs.md`
- Round-47 routed defects this table re-measures:
  `corpus/lessons/round-47-verifier-spotcheck.md` (items 2 and 3), `.ufo/waves/round-47/build/C2CriticRule.md`
- Scratch probes and fetched sources: `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2EntryScaffoldScribe/`

Report: .ufo/waves/round-48/build/C2EntryScaffoldScribe.md
