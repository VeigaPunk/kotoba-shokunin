# A15AppendOnly: round-48 falsify of SOURCES append-only, census, superseding rows

Lane `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. HEAD `84b9c9ba89559b51a72c83c2b9605b184df4ae9e` (records). C1 `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1`. Base `75f671b109d8eddd0d64c1429bd6379fe577175a`. Times are UTC, 2026-10-22. Lane read-only; clone checks under `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A15AppendOnly/`. No tool installed or upgraded.

## Verdicts

| # | Target | Verdict | Severity |
|---|---|---|---|
| 1 | Rule 2: `75f671b..887b6af` adds rows S016-S021 only; no old cell edited | CONFIRMED | none |
| 2 | Each superseding row's teaches opens `supersedes S0NN —` | CONFIRMED: S018→S001, S019→S003, S020→S010, S021→S013 | none |
| 3 | Frozen census (rows, malformed, tiers, statuses) and `validate kotoba` | CONFIRMED clean: 21 rows, 0 malformed, exit 0 | none |
| 4 | used-by backlinks after round 48 | DEFECT: 5 round-48 rows stale or missing a citer | medium |
| 5 | Paths section, SOURCES.md:38-43 | DEFECT: says the spec lacks the 500-line rule; S018 and S019 refute it | low-medium |
| 6 | Search log shape (rule 5) | DEFECT: round-48 search note only in the lesson | low |
| 7 | Superseded rows still in checker output | RESIDUAL, partly disclosed | low |
| 8 | Maintained validator guarantees | RESIDUAL: 4 gaps; append-only not machine-checked | low |
| 9 | Freshness sweep reach | RESIDUAL: 10 of 21 rows can never be overdue | medium (design) |
| 10 | Live pins of S016-S021 | CONFIRMED; S020 `--json` counts not quoted in any Gate | low |

Bottom line: rule 2 holds, and the six new rows are fresh and pinned. The defects are backlinks and prose that round 48 did not update.

## 1. Append-only: CONFIRMED
- `GIT_OPTIONAL_LOCKS=0 git diff --numstat 75f671b 887b6af -- corpus/SOURCES.md` gives `6	0	corpus/SOURCES.md`, exit 0.
- The hunk is `@@ -26,6 +26,12 @@`, adding lines 29-34 (S016-S021). No removed line.
- The 15 base table lines are the first 15 table lines of the 887b6af file, byte-identical (python compare: True).
- `git diff --numstat 887b6af 84b9c9b -- corpus/SOURCES.md` is empty, so the records commit does not touch the registry.
- Blob `8b0993bc654a170af694cc66544e36a10b72061b` is the same at 887b6af and HEAD.
- Rule 2 lets used-by change in place when logged. Nothing changed, so no log entry is owed.

## 2. Superseding rows: CONFIRMED
- Python on the teaches cell, em dash U+2014, pattern `^supersedes (S\d{3}) — `: S018→S001, S019→S003, S020→S010, S021→S013. Four of four.
- Each target exists. Each pair shares one source: the spec URL, the Anthropic best-practices URL, `verifiers/verify_skill_checklist.py`, the Codex build-skills URL.
- S016 and S017 correct no earlier row. [INFERENCE] I read the teaches cells of S001-S015 and found no claim these two contradict.

## 3. Frozen census: CONFIRMED (cwd = lane root)
- Rows `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: 21 (base 15).
- Malformed `awk -F'|' … NF!=13`: 0.
- Tiers: `A=20 C=1` (the C row is S011, rejected).
- Statuses: `mined=12 queued=8 rejected=1`.
- Duplicate ids (`uniq -d`): none. Enum and tier-inflation: none. Mined used-by paths missing: none.
- My first census pass ran from the wrong cwd and had one mistyped status line. Both were rerun; only the rerun numbers stand.
- `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`, exit 0:
  - `kotoba W04 S018 duplicate url agentskills.io/specification across scopes`
  - `kotoba W04 S019 duplicate url platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices across scopes`
  - `kotoba W04 S021 duplicate url learn.chatgpt.com/docs/build-skills across scopes`
  - `kotoba ok .../corpus/SOURCES.md`
  The three warnings are the expected cross-scope reuse of superseded URLs.
- `census --root … kotoba`: rc 0, same counts. `overdue --today 2026-10-22`: rc 0, no row overdue. `selftest`: rc 0, "selftest ok".

## 4. used-by backlinks: DEFECT (medium)
Citers searched at HEAD in corpus/knowledge, corpus/lessons and SKILL.md:

| row | registry used-by | HEAD tree | problem |
|---|---|---|---|
| S001 | SKILL.md | SKILL.md:151 no longer cites S001 (base did) | stale; `mined` rests on no SKILL.md citer |
| S003 | SKILL.md | SKILL.md:151 no longer cites S003 (base did) | stale; same |
| S012 | SKILL.md | new entry cites S012 at frontmatter-rule-authorities-round48.md:1, :23, :88 | entry missing |
| S018 | entry only | SKILL.md:151 cites S018 | SKILL.md missing |
| S019 | entry only | SKILL.md:151 cites S019 | SKILL.md missing |

- Effect: a recheck of S012 would not reach the new entry. A recheck of S018 or S019 would not reach SKILL.md:151.
- The lesson (corpus/lessons/round-48.md:24-26) says no used-by changed and that S001, S003, S010, S013 "stay as written (contract rule 2)". Rule 2 permits used-by edits when logged. It does not require leaving them false.
- Convention, low: lesson Gate rows S017-S021 (lines 31-35) name the lesson, but used-by names only the entry. S016 is the one row whose used-by lists the lesson.
- Pre-existing, not round 48: S015 is cited by knowledge/opencode-extraction-round14.md:16 but omits it. S010 has used-by "—" while round-46 and round-47 lessons cite it.
- Fix: update used-by old→new for S001, S003, S012, S018, S019; log it in the round lesson; decide the lesson convention.

## 5. Paths section: DEFECT (low-medium)
- SOURCES.md:38-43: "Authoring a SKILL.md that loads everywhere — S001 → S008 → S003 → S002 → S011", with "the vendor-only rules (no XML tags, third person, 500 lines) that the spec does not carry".
- Live https://agentskills.io/specification.md (access 2026-10-22T08:55:46Z) line 237: "Keep your main `SKILL.md` under 500 lines." Pinned docs/specification.mdx at 69ef37e9 (access 08:58:12Z) line 224: same text. S019 supersedes S003 on this exact point.
- The sequence still names two superseded rows, S001 and S003.

## 6. Search log: DEFECT (low)
- SOURCES.md `## Search log` (lines 51-89) holds 2026-10-19 (three notes) and 2026-10-21 notes, and no 2026-10-22 note.
- The round-48 search (identified 11, included 6, excluded 5, stop rationale) sits only in corpus/lessons/round-48.md:44-54. Rounds 46 and 47 put their notes in SOURCES.md.

## 7. Superseded rows in checker output: RESIDUAL
- `verify_skill_checklist.py:1307` builds the `trigger.no_xml_tag` detail "S003 Anthropic rule, absent from the open spec (S001) …". The 2026-10-22 `--json` run emits that text.
- Docstring lines 102-103 and line 210 also cite S003 and S001.
- The entry discloses only 1307-1308 (knowledge file lines 73-74). Fix: cite S019 and S018.

## 8. Validator (maintained script): RESIDUAL, low
- E04 regex `/supersedes S[0-9]{3}/` (sources-census.sh:646-649) accepts the word anywhere in teaches, not opening it. Target existence is not checked.
- `url_of` (:600-605) returns "" for own-work rows, so duplicate checks never run for them. The S010/S020 pair goes unchecked.
- `symbolic()` (:582) accepts any word, so a typo such as "soon" passes E09. No used-by reverse check. No append-only check; only git can show rule 2.
- None of these fails the lane today.

## 9. Freshness sweep reach: RESIDUAL (medium, by design)
- 10 of 21 rows carry a symbolic recheck: on-release ×6 (S001, S005, S006, S008, S015, S016), on-commit ×4 (S009, S010, S017, S020). `overdue` prints them as "cadence" only (:676-682), so they can never be overdue.
- Only the 11 numeric rows (90d, 180d, 365d) get an overdue judgment. Three of six round-48 rows (S016, S017, S020) fall in the unjudged set.

## 10. Live pins: CONFIRMED (non-author sample)
- S018 spec .md, 2026-10-22T08:55:46Z: 7608 B, sha256 9a67de89… matches. "Skill metadata table": 0 hits, so the S001 anchor defect is real. Line 30 "Lowercase letters, numbers, and hyphens only". Line 64 "May only contain unicode lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)" (14 words). Headings `#### name field` (:59) and `#### description field` (:97) exist.
- S018 pin docs/specification.mdx at 69ef37e9, 2026-10-22T08:58:12Z: 7166 B. Lines 27, 62-65, 94 ("- Must be 1-1024 characters") and 224 match the row's cited lines.
- S019 best-practices.md, 2026-10-22T08:55:46Z: 42169 B, sha256 f0a5d61b… matches. "Cannot contain XML tags" at :155 and :162; "Always write in third person" :206; "under 500 lines" :257; headings :146, :201, :251 exist.
- S021 build-skills.md, 2026-10-22T08:55:46Z: 11035 B, 232 lines, sha256 ed6e324f… matches (also in round-47 SrcNewCodexSkills.md). md:38-39 "this list uses at most 2% of the model's context window, or 8,000 characters when the context window is unknown" (21 words). md:43-44 "up to 10,000 tokens". Heading md:91. Implicit invocation md:98-99.
- S016 raw index.ts at v1.19.3, 2026-10-22T09:00:12Z: line 24 `const OPENCODE_SKILL_PATTERN = "{skill,skills}/**/SKILL.md"` matches. `git ls-remote` tag v1.19.3 gives e3c4eb242585dcd77be1a867391b7c25fd47ce52.
- S017 raw validator.py at 69ef37e9, 2026-10-22T09:00:12Z: 5154 B. Line 10 `MAX_SKILL_NAME_LENGTH = 64`, line 11 `MAX_DESCRIPTION_LENGTH = 1024`, line 54 `c.isalnum()` match.
- S020 reproduction: private clone `…/A15AppendOnly/fleet/kotoba-shokunin` at 75f671b, fleet siblings linked read-only beside it.
  - `python3 -B verifiers/verify_skill_checklist.py --self-test`: rc 0, "0 failure(s) over 1845 assertions". Matches.
  - `python3 -B verifiers/verify_skill_checklist.py --json`: rc 0, pass 11, fail 0, na 0, "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)". Matches.
  - Lines 404 (XML_TAG_RE), 409 (YAML_ANGLE_ESCAPE_RE), 1294 (def check_no_xml_tag) match. verify_skill_checklist.py has no diff from 75f671b to HEAD.
  - Two earlier `--json` runs returned rc 1, from the clone directory name and missing sibling repos. Environment, not lane.
  - Provenance gap, low: `git grep -E '11 PASS|41 boxes'` over `.ufo/waves/round-48` at 887b6af gives no hits. The S020 Gate quotes only the self-test line.
- S001 anchor defect was recorded in round 47 (corpus/lessons/round-47.md:46-50) and deferred to a superseding row. S018 is that row. CONFIRMED.

## Not verified by this seat
- Live re-opens of S001-S015, and the knowledge entry's numeric claims (other seats). S016 and S017 Gate context beyond the pinned lines (A14S016Row, A17GateLines).
- Lane working copy has uncommitted changes from other seats (verifiers/verify_harness_independent.py, check_assertion_floors.py, floors-registry.json, corpus/knowledge/frontmatter-rule-authorities-round48.md with +28/-21, several round-48 build reports). My committed-tree checks are unaffected. The knowledge-entry edit keeps the same S-id citers (S012, S017-S021), and SKILL.md:151 is unchanged, so the used-by findings hold on both trees. The census and validate read working-copy corpus/SOURCES.md, which matches HEAD.

## Fix directions (not applied; lane read-only)
1. used-by: S001 and S003 drop SKILL.md; S012 add the entry; S018 and S019 add SKILL.md; log old→new in corpus/lessons/round-48.md.
2. Paths: rewrite SOURCES.md:38-43 onto S018 and S019; remove "the spec does not carry" for 500 lines.
3. Move the round-48 search note into SOURCES.md `## Search log`.
4. Checker detail string and docstrings: cite S019 and S018.
5. Validator: opens-with check; supersedes target check; own-work duplicate key; cadence whitelist; used-by reverse check.
