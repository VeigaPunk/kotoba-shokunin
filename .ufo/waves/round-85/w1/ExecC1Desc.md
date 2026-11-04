# ExecC1Desc — C1 description candidate (round 85, attempt 1)

Base: 1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b. Lane HEAD at run time: aaa3978753a409b63b5feca48c923ee9948f1539
(descendant of base; `plans/round-85.md` +145 lines since base, `SKILL.md`, `verifiers/check_sibling_census.py`,
`corpus/knowledge/sibling-overlap-census-round74.md`, `PROVINCE.md` unchanged).

## Files written

- `.ufo/waves/round-85/w1/ExecC1Desc/candidate-SKILL.md` — SKILL.md copy; only the frontmatter description block replaced (folded `description: >`, 13 lines, max width 72, CRLF kept). Body bytes identical to base.
- `.ufo/waves/round-85/w1/ExecC1Desc/frontmatter.diff` — CRLF-exact unified diff of the frontmatter (base lines 1–21 vs candidate lines 1–19, three context lines after the terminator). Applies to `SKILL.md` with no fuzz.
- `.ufo/waves/round-85/w1/ExecC1Desc/proof-parsed-equality.json` — parse proof.
- `.ufo/waves/round-85/w1/ExecC1Desc/sibling-guard-candidate.out` — sibling guard receipt.
- `.ufo/waves/round-85/w1/ExecC1Desc/checklist-trigger-rules.out` — checklist receipt.
- `.ufo/waves/round-85/w1/ExecC1Desc/build_candidate.py` — the builder (reads the frozen candidate from the plan's § C1 fence).
- `.ufo/waves/round-85/w1/ExecC1Desc.md` — this report.

SKILL.md itself was not edited.

## Parse proof (`description_of()` loaded via importlib from `verifiers/check_sibling_census.py`)

- `parsed == candidate`: **true**
- `len(parsed)` = 876, `len(candidate)` = 876 (plan says 876)
- first sentence length = 65 (≤ 99)
- `repr(parsed[:99])` = `'Use this skill when auditing or rewriting a skill file or prompt. Triggers: "skill file", "SKILL.md'`
- Probes on the parsed value: `skill` in first 99 chars: true; `prompt` or `skill.md` in first 99: true; `use this skill when`: true; literal `Triggers:`: true; `Anti-triggers`: true; no `<` or `>`: true.
- Base SKILL.md parses to 1021 characters (measured by the same function), matching the plan's base fact.

## Sibling guard on the copy

Command: `python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md --province PROVINCE.md --skill <candidate-SKILL.md>`
Last three lines, exit 0:
```
province rows 20 matched 20
skill description names 10 of 10 non-none lanes
skill description length 876 of 1024
```

## verify_skill_checklist on the copy

`verify_skill_checklist.py --skill <copy>` accepts a copy. Run with the four trigger checks plus name_directory, exit 1:
- PASS `trigger.literal_trigger_string` (literal `Triggers:`)
- PASS `trigger.anti_trigger_clause` (`Anti-triggers` present)
- PASS `trigger.no_xml_tag`
- PASS `trigger.frontmatter_parses` (name `kotoba-shokunin`, description 876 chars)
- FAIL `trigger.name_directory`: name `kotoba-shokunin` != directory `ExecC1Desc`. This is an artifact of targeting a copy inside a wave dir, not a candidate defect; the repo SKILL.md satisfies it at its own directory.

## Frontmatter diff

`frontmatter.diff` applies to the base with `patch -p1 --dry-run --batch --forward` → exit 0, `Hunk #1` clean (no fuzz line). Applied to a scratch copy, the result is byte-equal to `candidate-SKILL.md` (`cmp` silent). The L1 applies it with `patch -p1` against `SKILL.md`.

## Issues found during the build (for the L1)

1. **SKILL.md is CRLF** (599 of 599 terminated lines carry `\r`). A text-mode read normalises CRLF to LF, so a naive rebuild differs from the base in every line ending. The builder reads and writes with `newline=""` and preserves CRLF. Any seat that rewrites SKILL.md in text mode will silently change line endings.
2. The base frontmatter terminator is line 19 (index 18); the candidate's is line 17 (index 16), because the candidate's folded block is 13 lines against the base's 15. Diffs must anchor on the `---` terminator, not a fixed line number.
3. A first diff generated with no trailing context applied only with `fuzz 2`. The regenerated diff carries three context lines after the terminator and applies clean.

## Tooling

No tools installed or upgraded. Only Python stdlib (`difflib`, `importlib`), `patch`, `cmp`, `grep`, `diff` were used.

## Risks

- The candidate's `description` is a hand-authored payload; the plan froze its text and I reproduced it verbatim (876 chars, equal). The semantic quality of the trigger clauses is not evaluated here (that is the eval set / R6 seat's concern).
- `verify_skill_checklist.py` cannot target a copy without a name/directory mismatch; the name_directory result is reported as an artifact, not a pass. The L1 should run the checklist against the real SKILL.md after applying the diff.
- The L1 must apply the diff in CRLF-preserving mode; a text-mode editor would flip line endings for the whole file.
- The lane's HEAD (`aaa3978`) is ahead of base; the plan file grew by 145 lines in that range. My parse proof does not depend on it, but it is recorded.
