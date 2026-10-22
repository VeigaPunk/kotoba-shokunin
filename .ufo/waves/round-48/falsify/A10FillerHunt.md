# A10FillerHunt — filler and Q12/Q13/Q14 audit of the C1 entry

Target: `corpus/knowledge/frontmatter-rule-authorities-round48.md` (104 lines) at tip `84b9c9ba`. Clone:
`/fast/scratch/hyaku/kotoba-r48-a2/seats2/A10FillerHunt/lane`. No tools installed; `godspeed` has no skill file.

## Verdict

**DEFECT, moderate.** The entry is not filler. About 12 of its 60 table cells restate the base
`SKILL.md:151` (at `75f671b`) or the earlier rows S001, S003 and S012. The rest is new, including at
least six disagreements between authorities that `SKILL.md` never stated. Every re-opened quote and
line number is correct except one (`spec.md:27`). The severity is for freshness, the judged axis:
the one `recheck:` guards one sentence from one of six authorities, only one count (line 3) follows
the Q13 form, and several "not stated" cells carry no sweep, or a sweep that misses the rule's terms.

## Sources re-opened (2026-10-22T08:52:01Z to 08:52:02Z UTC; every hash equals the entry's)

| source | URL | bytes, sha256 prefix | quote (location) |
|---|---|---|---|
| S018 | https://agentskills.io/specification.md | 7608, `9a67de89` | "Must not contain consecutive hyphens (`--`)" (:66) |
| S019 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md | 42169, `f0a5d61b` | "Cannot contain reserved words: \"anthropic\", \"claude\"" (:156) |
| S012 | raw.githubusercontent.com/anthropics/skills/dbd4588f…/skills/skill-creator/scripts/quick_validate.py | 3972, `67cf5703` | "if not re.match(r'^[a-z0-9-]+$', name):" (:65) |
| S017 | raw.githubusercontent.com/agentskills/agentskills/69ef37e9…/skills-ref/src/skills_ref/validator.py | 5154, `b5ee3d85` | "if not all(c.isalnum() or c == \"-\" for c in name):" (:54) |
| S021 | https://learn.chatgpt.com/docs/build-skills.md | 11035, `ed6e324f` | "The `SKILL.md` file must include `name` and `description`." (:48) |

`git ls-remote https://github.com/anthropics/skills HEAD` gave `dbd4588f…` (exit 0); every other cite re-read correctly.

## Filler: duplicates of base `SKILL.md:151` and the existing corpus

`git show 75f671b:SKILL.md | sed -n 151p` and the pre-round S001, S003 and S012 teach cells already state the
spec and docs cells for name length, charset and description length (lines 36, 37, 41), the spec's directory
cell (38), the docs and packager angle cells (42; also `lessons/round-47.md:35`), docs third person (43) and
body length (46). Lines 86-92 rerun the classes from `lessons/round-47-verifier-spotcheck.md:33,72`; only
the runs are new. Commit `887b6af` gives the lane-versus-packager fact three homes (`SKILL.md:151`, S020's
teach cell, lines 63-74), against the M25 fix's "so the fact keeps one home". Line 57 says the spec
contradicts itself; `SKILL.md:151` says ambiguous.

## Genuinely new: disagreements `SKILL.md` never stated

Sweep over `SKILL.md` at base and tip: `grep -ciE` with `skills-ref|S017|isalnum|NFKC`, with
`Unexpected|unknown (top-level )?(field|key)`, with `reserved` and with `third person` printed 0 every time.
1. **Unicode names:** skills-ref applies NFKC then `isalnum` (validator.py:37,54) and accepts `技能-测试`;
   the packager's `^[a-z0-9-]+$` (qv.py:65) rejects it.
2. **Angle brackets:** skills-ref has no description character rule (validator.py:70-84) and escapes at render
   time (prompt.py:46). The packager bans any `<` or `>`; the docs ban XML tags.
3. **Unknown top-level fields:** skills-ref (validator.py:104-113) and the packager (qv.py:42-49) reject them.
   The spec offers only `metadata` for extras (spec.md:161).
4. **Empty description**, by source reading, not run: the packager skips every check (qv.py:77-78);
   skills-ref rejects it (validator.py:74-75); the docs say "Must be non-empty" (bp.md:160).
5. **Consecutive hyphens:** rejected by all but the docs (`grep -niE consecutive bp.md`: 0, exit 1).
6. **Name equals directory:** spec and skills-ref only; the packager never checks it (`grep -cE
   'dirname|basename|parent' qv.py`: 0, exit 1). Base `SKILL.md:151` credited it to spec + vendor.

## Q12 (the source, verified-at and recheck header), cell by cell

- **Line 1, S021:** no URL and no section anchor; its row (`SOURCES.md:34`) is scoped to the skill-list
  budget, yet carries ten "not stated (a)" cells. **Violation.** **S019:** the anchor lists only § Skill
  structure, but cells cite bp.md:206 and :257. **Violation.** **S017:** line 42 cites `prompt.py:46`,
  outside S017's anchor (validator.py, parser.py). **Violation.**
- **Line 1, S012:** its used-by reads `SKILL.md` only, and the lesson says "No other row moved". **Violation.**
- **Lines 20 and 90-92:** the skills-ref runs used PyPI 0.1.1. Its `validator.py` is sha256 `7b5cb3dc`, not the
  pin's `b5ee3d85`: CRLF line endings and `read_text(encoding='utf-8')` at validator.py:172 and parser.py:89
  (`diff --strip-trailing-cr`, exit 1). The entry does not disclose this. **Violation (provenance; low).**
- **Line 2:** `verified-at` is present. **Pass.**
- **Line 3:** the recheck printed 1, exit 0, at 08:53:58Z; a dead-URL control printed 0, exit status `22 1`.
  **Pass in form, weak for freshness:** it guards one spec sentence. Lines 98-99 hand the rest to
  `C2RecheckCommand.md`, outside the corpus (5 strings, not 10 rule rows); its R2 pins skills-ref at `547831f3`,
  not `69ef37e9`. The validator bytes match at both commits (`b5ee3d85`), so only the label is wrong.

## Q13 (each count written as number, command, date)

Only line 3 ("1 on 2026-10-22") meets the form in full. **No command:** line 14 "7,608 B"; line 21
"42,169 B" and "42,028 B"; line 29 "24"; line 30 "10"; line 45 "six"; line 47 "64-character", "1,024";
lines 63-64 "6 of 10", "3 of 10" (they reproduce from `C2LaneCheckerRun.md:59-61`); line 78 "ten";
line 98 "Five of the six"; line 103 "256-character". **Command but no date:** lines 39-44, 47, 81.
**Command naming no file:** lines 40 (`consecutive`), 43 (`reserved word`), 44 (`unknown field`).

## Q14 (each negative claim carries its sweep)

- **No sweep:** third person for skills-ref and the lane (line 43; the lane cell has no run either), body
  length for skills-ref and the packager (line 46), and the spec's "no ban" on unknown fields (line 44).
  Reserved words for skills-ref and the packager (line 44) rest on one `claude-tools` run, not a search.
- **Line 47, Codex sweep (a):** it never searches for directory, match, unknown or empty, so the Codex cells
  on lines 38, 41 and 45 carry no sweep. My broader sweep holds them: `empty` 0 hits; `unknown|unexpected|…`
  1 hit (`md:39`, context window); the `director|folder` hits are install locations (md:138-157).
- **Line 48:** sweep (b) covers an "overview page" with no S### row and gives no count (my bp.md rerun: 0, exit 1).
- **Lines 52-56** inherit these gaps. **Lines 83-84** delegate their sweep to `C2SpecScribe.md`; the claim is
  true (I read spec.md:28-35).

## Content defects beyond Q12, Q13 and Q14

- **Line 58:** `spec.md:27` is blank; the quoted row is at spec.md:30 (`grep -n`). 27 is the mdx line.
- **Line 83:** "gives maxima only" is false; spec.md:30-31 also says "Non-empty" and bans a leading or trailing hyphen.
- **Line 64:** the docs verdicts use the seat's own rule ("operationalised as a well-formed XML tag shape",
  `C2LaneCheckerRun.md:43-44`), not a vendor run. Undisclosed.
- **Line 78:** "one of the ten rules' content checks" is contradicted by line 41, where the lane enforces a
  non-empty description. My `empty-desc` run also gave `no_xml_tag` FAIL ("cannot evaluate: empty description:").
- **Lines 73-74:** only the FAIL detail string is called stale, but the PASS string still says "S003 Anthropic
  rule, absent from the open spec (S001); … is stricter" (seen on the `trail-` fixture).
- **For A12 (omitted rules):** the start-or-end-hyphen rule (spec.md:65, validator.py:48, qv.py:67) and the
  500-character `compatibility` cap are absent. The lane passes `name: trail-` (rc 0).

## Lane checker runs

Command: `python3 -B verifiers/verify_skill_checklist.py --skill <fixture>/SKILL.md --json`, with
`--check` for `frontmatter_parses`, `name_directory` and `no_xml_tag` (in that order below).
- `empty-desc` (`description: ""`): FAIL, PASS, FAIL; rc 1. `empty-name`: FAIL, FAIL, PASS; rc 1.
- `tag-desc` (`<skills>`): PASS, PASS, FAIL; rc 1.
- `技能-测试`, `angle-ab` (`a < b`), `first-person` and `trail-`: PASS, PASS, PASS; rc 0.

Knowledge Markdown count: 34 at base and 35 at tip (`git ls-tree --name-only <rev> corpus/knowledge/ | grep -c '\.md$'`),
matching C1. I did not run the packager or skills-ref, because my item names no packaged validator.

## Smallest safe correction

Change `spec.md:27` to `:30` and delete "gives maxima only" (lines 58, 83). Say the line-64 docs verdicts come
from an operationalised rule. Give S021 a URL and anchor, widen S019's anchor, and fix S017's (`prompt.py`).
Add the entry to S012's used-by, logged in the lesson. Disclose the PyPI 0.1.1 bytes (`7b5cb3dc`) on lines 20
and 90-92. Carry one recheck per authority, or name the unguarded rows. Add the command, date and sweep to
every Q13 and Q14 item above. Cut `SKILL.md:151`'s restated disagreement down to the pointer.
