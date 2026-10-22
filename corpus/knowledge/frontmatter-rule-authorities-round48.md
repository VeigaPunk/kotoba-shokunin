source: S018 (https://agentskills.io/specification, § Frontmatter, § `name` field, § `description` field, § Progressive disclosure), S017 (https://github.com/agentskills/agentskills/tree/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref, `validator.py`, and `prompt.py:46` in the same tree), S019 (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices, § Skill structure, § Writing effective descriptions, § Progressive disclosure patterns), S012 (`quick_validate.py:42-92` at `dbd4588`), S021 (https://learn.chatgpt.com/docs/build-skills, page intro and § How ChatGPT and Codex use skills; cited only for what the Codex page does not state), S020 (lane `verify_skill_checklist.py`)
verified-at: 2026-10-22
recheck: curl -fsSL https://agentskills.io/specification.md | grep -c 'Must match the parent directory name'  # 1 on 2026-10-22; 0 means the spec's rule text moved

# Which authority imposes which SKILL.md frontmatter rule (round 48)

Round 47's outside spot-check routed one defect this entry repairs: the lane described its
`trigger.no_xml_tag` check as if it executed a vendor rule, while it is a lexical approximation
of a parsed-value rule, and the YAML-alias, Unicode-name and escaped-value counterexamples were
argued, not run (`corpus/lessons/round-47-verifier-spotcheck.md`, routed item 3). Here every
authority is opened on 2026-10-22, every lane cell is a run of the lane checker, and every
"not stated" cell names the search that found nothing (Q14).

Authorities and the bytes read (2026-10-22, UTC):

- **Spec** — S018, `https://agentskills.io/specification.md`, 7,608 B, sha256 `9a67de89…`, byte-identical
  to the round-47 fetch.
- **skills-ref** — S017, the spec's reference validator, `agentskills/agentskills` commit
  `69ef37e9424c0a7ea9dd2293b559e43ec8176379`, `skills-ref/src/skills_ref/validator.py` sha256
  `b5ee3d85…`; PyPI `skills-ref` 0.1.1 run as `agentskills validate`. The PyPI file is not byte-identical
  to the pinned tree (its `validator.py` hashes `7b5cb3dc…`: CRLF line endings and `read_text(encoding='utf-8')`);
  a pinned-commit install gave the same exit codes and messages on 21 fixtures (`C2SkillsRefRun.md`).
- **Anthropic docs** — S019, best-practices page `.md`, 42,169 B, sha256 `f0a5d61b…` (round 47 read
  42,028 B `727f3fa1…`; copy edits only, every rule line unchanged).
- **Anthropic packager** — S012, `quick_validate.py` at `dbd4588f…`, sha256 `67cf5703…`; this pin is
  still `main` HEAD on 2026-10-22 (`git ls-remote`).
- **Codex docs** — S021, `learn.chatgpt.com/docs/build-skills.md`, sha256 `ed6e324f…`.
- **Lane checker** — S020, `verifiers/verify_skill_checklist.py` at lane tip `75f671b` (its rule code is
  unchanged through round 48; only the FAIL detail string changed later), run as
  `python3 -B verifiers/verify_skill_checklist.py --skill <fixture> --check <id> --json`.

Seat evidence: `.ufo/waves/round-48/build/C2EntryScaffoldScribe.md` (24 probe fixtures, the
table's source), `C2LaneCheckerRun.md` (10 fixtures, three-way comparison), `C2SkillsRefSource.md`,
`C2QuickValidateFresh.md`, `C2ClaudeDocs.md`, `C2CodexOpencodeDocs.md`, `C2RecheckCommand.md`.

## Rule-by-authority table

| rule | spec (S018) | skills-ref (S017) | Anthropic docs (S019) | Anthropic packager (S012) | Codex docs (S021) | lane checker (S020), observed |
|---|---|---|---|---|---|---|
| name length | "Must be 1-64 characters" (spec.md:63) | `MAX_SKILL_NAME_LENGTH = 64` (validator.py:10); 65 chars fails | "Maximum 64 characters" (bp.md:153) | 65 chars: "Maximum is 64 characters" (qv.py:70-71) | not stated (a) | no rule: a 65-character name passes |
| name charset | "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens" (spec.md:64) | NFKC, then `c.isalnum() or c == "-"` (validator.py:37,54-58): `技能-测试` valid | "Must contain only lowercase letters, numbers, and hyphens" (bp.md:154) | `^[a-z0-9-]+$` (qv.py:65): `技能-测试` and `café-skill` fail | not stated (a) | no rule: `Probe-Upper`, `技能-测试` pass |
| name equals directory | "Must match the parent directory name" (spec.md:67) | NFKC on both sides (validator.py:60-65): dir `probe－full` + name `probe-full` valid | not stated (b) | not stated (d) | not stated (a) | `trigger.name_directory`, literal compare: dir `probe－full` vs `probe-full` FAIL |
| consecutive hyphens | "Must not contain consecutive hyphens" (spec.md:66) | rejected (validator.py:51-52) | not stated (e) | rejected (qv.py:67) | not stated (a) | no rule: `probe--consec` passes |
| description length | "Must be 1-1024 characters" (spec.md:101) | `MAX_DESCRIPTION_LENGTH = 1024` (validator.py:11) | "Maximum 1,024 characters", "Must be non-empty" (bp.md:160-161) | 1025 fails (qv.py:83-84), counted after stripping whitespace (qv.py:77), so a padded 1,024-character value passes; an empty description passes today (`if description:` guard, qv.py:78) | not stated (a) | empty fails `trigger.frontmatter_parses`; no maximum: 1025 characters pass |
| description angle brackets or XML tags | not stated (c) | not a validity rule; `prompt.py:46` HTML-escapes the description instead; `Use <skills>` valid | "Cannot contain XML tags" for name and description (bp.md:155,162) | any `<` or `>` in the parsed value: "Description cannot contain angle brackets (< or >)" (qv.py:79-81) | not stated (a) | `trigger.no_xml_tag`: an ASCII XML-tag shape or a YAML angle-escape token in the unparsed scalar text (verify_skill_checklist.py:404,409,1294) |
| third person | not stated (c) | not stated (f) | "Always write in third person" (bp.md:206) | not stated (d) | not stated (a) | no rule |
| reserved words | not stated (c) | not stated (f); `claude-tools` valid | "Cannot contain reserved words: \"anthropic\", \"claude\"" (bp.md:156) | not stated (d); `claude-tools` valid | not stated (a) | no rule: `claude-tools` passes |
| unknown top-level fields | no ban stated (c); `metadata` holds extra properties (spec.md:161) | "Unexpected fields in frontmatter" (validator.py:104-113) | not stated (e) | "Unexpected key(s)"; allowed set of six (qv.py:42-49) | not stated (a) | no rule: `version: 1` passes |
| body length | "Keep your main `SKILL.md` under 500 lines" (spec.md:237) | not stated (f) | "under 500 lines for optimal performance" (bp.md:257) | not stated (d) | not stated (a) | `trigger.line_budget` 600, from the lane's own box (SKILL.md:246): 605 lines FAIL, 505 PASS |

(a) `grep -niE 'reserved|third person|xml|angle|500 lines|1024|1,024|64 char|lowercase|hyphen|consecutive' build-skills.md` → 0 hits, exit 1; widened on 2026-10-22 with `director|unknown|unexpected|additional field` → 5 hits, none a frontmatter rule (md:11 plugin directory, md:39 "context window is unknown", md:48 "must include `name` and `description`", md:138 and md:142 skill locations). The Codex page documents only that `name` and `description` are required; Codex CLI 0.163.0's shipped parser has its own limits (64-character name, catalog descriptions truncated at 1,024), recorded in `C2CodexOpencodeDocs.md` and not tabled here because no source row pins that code.
(b) `grep -niE 'match the (parent |skill )?director|folder name|directory name' best-practices.md overview.md` → no rule sentence (2026-10-22, `C2EntryScaffoldScribe.md`).
(c) Spec sweeps over `specification.md` (sha256 `9a67de89…`), 2026-10-22: `grep -ciE 'angle|xml|[<>]'` finds no rule line (the only `<`/`>` hits are the `\< 5000 tokens` note and Markdown markup); `grep -ciE 'third person'` → 0; `grep -ciE 'reserved'` → 0; `grep -niE 'unknown|unrecognized|additional (field|propert)'` → only spec.md:161 (the `metadata` sentence), no ban (`.ufo/waves/round-48/falsify/A01SpecColumn.md`).
(d) Packager sweeps over `quick_validate.py` at `dbd4588`: `grep -nE 'dirname|basename|parent'` → 0; `grep -niE 'third person|reserved|lines'` → 0 rule lines; behaviour run on `claude-tools` → "Skill is valid!" (`.ufo/waves/round-48/falsify/A03PackagerColumn.md`).
(e) Anthropic sweeps over `best-practices.md` (sha256 `f0a5d61b…`) and `overview.md`: `grep -ciE 'consecutive'` → 0; `grep -niE 'unknown field|unrecognized|only these fields'` → 0 (2026-10-22, `C2EntryScaffoldScribe.md`).
(f) skills-ref sweeps over `validator.py`, `parser.py`, `models.py` at upstream commit 69ef37e9: `grep -niE 'third person|reserved|max_lines|line_count|500'` → 0 (2026-10-22, `C2EntryScaffoldScribe.md`, `C2SkillsRefSource.md`).

## What the table teaches

1. **Each rule has its own owner.** Among the documents, only the spec states the name-equals-directory
   rule; skills-ref enforces it in code and the packager never checks it. Only Anthropic's docs state
   reserved words and third person. Only the packager bans every angle
   bracket. Only skills-ref and the packager reject unknown top-level fields. "Spec rule" and
   "Anthropic rule" are not interchangeable labels.
2. **The spec is ambiguous on the name charset.** spec.md:64 says "unicode lowercase alphanumeric
   characters" and then lists only `a-z`, `0-9`; the frontmatter table (spec.md:30, "Lowercase letters,
   numbers, and hyphens only") does not settle it. Its own validator takes the Unicode reading (NFKC
   plus `isalnum`), the packager takes the ASCII reading. A Unicode name is valid to one and invalid to the other.
3. **Three different angle-bracket rules exist.** Anthropic's docs ban XML tags; the packager bans
   any `<` or `>` in the parsed value; skills-ref allows both and escapes at render time.
4. **The lane checker is lexical, and it diverges from the packager in both directions**
   (`C2LaneCheckerRun.md`, 10 fixtures run 2026-10-22 with its `runner.py`; 6 of 10 verdicts differ from
   the packager, 3 of 10 from the docs' tag rule):
   - an alias `description: *d` whose anchor holds `<b>`: lane PASS, packager FAIL (the lane reads
     the two characters `*d`; it does not resolve aliases);
   - non-tag brackets (`a < b`, `->`, a folded block splitting `<` and `b>`): lane PASS, packager FAIL;
   - a single-quoted `'\u003cb\u003e'` (literal backslash text in YAML): lane FAIL, packager PASS; the
     same escape text in a plain or block scalar also FAILs the lane (`.ufo/waves/round-48/falsify/A06LaneCounterexamples.md`);
   - a double-quoted `"\u003cb\u003e"` (decodes to `<b>`): both FAIL, by different mechanisms.
   So the lane check is neither the packager's rule nor a superset of it. `SKILL.md`'s portability
   floor called the packager simply "stricter"; round 48 corrects that sentence and points it here.
   The check's FAIL detail string (`verify_skill_checklist.py:1307-1311`) and `PROVINCE.md` carried the
   same wording; both were corrected later in round 48 after the falsify wave flagged them
   (`.ufo/waves/round-48/falsify/A28QualityRows.md`).
5. **The lane's parse is not YAML.** On the alias fixture the lane reports "description 2 chars",
   the packager (PyYAML) resolves the alias and fails it, and skills-ref (strictyaml) refuses the
   anchor at parse time. Three tools, three answers to "what is the description".
6. **The lane executes one of the ten rules' content checks** (`trigger.no_xml_tag`) plus a literal
   name-directory compare and a 600-line budget. The 600 is a lane-local choice; both the spec and
   Anthropic's docs say 500. It must not be cited as an S018 or S019 rule.
7. **The spec carries no uppercase RFC 2119 keywords** (`grep -cwE 'MUST|MUST NOT|REQUIRED|SHALL|SHALL NOT|SHOULD|SHOULD NOT|RECOMMENDED|MAY|OPTIONAL' specification.md`
   → 0, exit 1, 2026-10-22); its strength lives in prose verbs ("Must", "Should", "We recommend"). Its frontmatter
   table is a lossy summary: it omits the consecutive-hyphen and
   directory-match rules that the `#### `name` field` section (spec.md:59) states (`C2SpecScribe.md`).

## Rules not tabled (found by the falsify wave)

`.ufo/waves/round-48/falsify/A12OmittedRules.md` found six rule classes the table above does not carry,
each with runs: name start or end hyphen (spec.md:30 and :65; skills-ref validator.py:48-49; packager
qv.py:67; the lane passes `-lead` and `trail-`), `compatibility` 1-500 (spec.md:33, :134; 501 fails
both validators, an empty value passes both), `metadata` string-to-string (spec.md:34, :160; neither
validator enforces it), `allowed-tools` as a space-separated string (spec.md:35, :176; a YAML list
passes both), `license` (spec.md:32, :122; unvalidated), and frontmatter delimiters (spec.md:24; the
lane tolerates a BOM, leading blank lines and a `...` closer that both validators reject). skills-ref
also measures name length after NFKC folding. The table is therefore a map of ten rules, not of
every frontmatter rule.

## Round-47 counterexamples, run (routed item 3)

| counterexample | lane checker | packager (S012) | skills-ref (S017) |
|---|---|---|---|
| YAML alias hiding a tag in `description` | PASS ("description 2 chars") | FAIL, angle brackets, exit 1 | FAIL, "disallowed anchor token", exit 1 |
| Unicode name `技能-测试` (directory matches) | PASS | FAIL, kebab-case, exit 1 | PASS, "Valid skill" |
| escaped `"… \u003cskills\u003e …"` | FAIL, names `\u003c` | FAIL, exit 1 | validate PASS; `read-properties` prints the decoded `<skills>` |

These stay as counterexamples. No universal frontmatter-validator claim is made for the lane check.

## Limits

- Five of the six sources are read live; the recheck line and the commands in
  `C2RecheckCommand.md` fail closed (count 0, exit 1) when the rule text moves or the URL dies.
  The packager and skills-ref rows are pinned to commits; the docs pages carry only a content hash.
- Client runtime behaviour (what Claude, Codex, opencode or omp do on load) is not measured here;
  this entry maps stated and executed validation rules only. Claude Code's skills page and the
  Anthropic Skills API guide state further rules (a 256-character name refusal; upload-time
  rejection) recorded in `C2ClaudeDocs.md` and not yet opened into source rows.
