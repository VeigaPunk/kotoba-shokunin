# A02AnthropicColumn: S019 column, S019 row, round-48 falsify (attempt 2)

Seat KotobaR48.A02AnthropicColumn, leaf, 2026-10-22. Lane written: this file only. Fetched bytes: /fast/scratch/hyaku/kotoba-r48-a2/seats2/A02AnthropicColumn/. Tools: none installed or upgraded (curl, sha256sum, cmp, diff, grep, and read-only git with --no-optional-locks). This file replaces the first draft committed at eb5a80f, which had three wrong sentences; section 8 corrects them.

## 1. Verdicts (pinned to committed HEAD eb5a80fed97c9ea2c649c6a2e1dc04a0ec80adaa)

- S019 column, every quote and line (bp.md:153-156, 160-162, 206, 257): CONFIRMED.
- "not stated" cells (name equals directory, consecutive hyphens, unknown top-level fields): CONFIRMED.
- S019 row, "supersedes S003", all three reasons: CONFIRMED.
- DEFECT, low, open: "every rule line unchanged" (knowledge entry line 24) and "the rule lines are unchanged" (SOURCES row 32) overstate. Bytes changed at bp.md 257-259, 1131, 1136, 1140, 1150. Content did not change.
- DEFECT, low, resolved at eb5a80f: S019 `used-by` omitted SKILL.md, though SKILL.md:151 cites S019. Present at 84b9c9ba.
- DEFECT, low, resolved at eb5a80f: SOURCES.md:38 said the spec lacks the 500-line rule. spec.md:237 states it. Present at 84b9c9ba.
- DEFECT, low, open: verifiers/verify_skill_checklist.py:102-103 and :210 still name S003 as the source and say "the open spec (S001/S002) lacks" the rule.
- DEFECT, low, open, records: corpus/lessons/round-48.md:25-26 says no existing row's used-by changed and S003 "stays as written". Lines :75-77 record S001 and S003 used-by changed in place.
- S019 page bytes: CURRENT. Same sha256 across three fetches.

## 2. Lane state during this run

- HEAD moved: 84b9c9ba (08:42:44Z), d28b16b (08:56:07Z), 2788704 (08:58:57Z), 48819b9 (09:01:38Z), eb5a80f (09:04:05Z). Times converted from -0300.
- Uncommitted at 09:10Z, not landed, not relied on: knowledge entry (Limits rewritten with per-source rechecks), lesson, QUALITY.md (+Q24), falsify/A11RecheckRuns.md. Untracked: falsify/A29ReadmeQualify.md.
- My first reads (about 08:50Z) saw the 84b9c9ba state. Items that moved are marked with their commit.

## 3. Freshness (re-opened)

| source | fetched (UTC) | bytes | sha256 prefix | result |
|---|---|---|---|---|
| best-practices.md | 08:52:06Z | 42169 | f0a5d61b67123a31 | equals S019 row; curl exit 0 |
| best-practices.md, again | 09:07:24Z | 42169 | f0a5d61b67123a31 | cmp identical, exit 0 |
| overview.md | 08:52:06Z | 21840 | 7913d4556c014c6b | equals C2ClaudeDocs.md table |
| specification.md | same session | 7608 | 9a67de891329 | equals S018 row |
| round-47 copy (in lane) | fetched 2026-10-21T15:54:11Z (SrcS003.md:14) | 42028 | 727f3fa1168eb1c3 | archived under .ufo/waves/round-47/build |

- HTML page, 09:10:16Z, cache-control no-store, no Last-Modified header: tag-stripped text carries the new wording ("from its name" 2 hits, "at a glance" 0). The .md endpoint is a faithful render, so the copy edits are page edits, not renderer artifacts.
- The page changed once, somewhere in (2026-10-21T15:54:11Z, 2026-10-22T08:12:08Z]. No fetch exists inside that window.
- Spec entry recheck `grep -c 'Must match the parent directory name'` on the fetched copy: 1.

## 4. S019 column: quotes and lines (today's bytes)

| cell | cited | observed |
|---|---|---|
| name max 64 | bp.md:153 | exact at 153; overview.md:214 |
| name charset | bp.md:154 | exact at 154; overview.md:215 |
| name no XML tags | bp.md:155 | exact; overview.md:216 |
| name reserved words | bp.md:156 | exact; overview.md:217 |
| description non-empty | bp.md:160 | exact; overview.md:221 |
| description max 1,024 | bp.md:161 | exact; overview.md:222 |
| description no XML tags | bp.md:162 | exact; overview.md:223 |
| third person | bp.md:206 | exact; absent from overview and spec |
| body under 500 lines | bp.md:257 | phrase "under 500 lines for optimal performance" intact; spec.md:237 agrees |

Anchors resolve: `## Skill structure` (bp.md:146), `### Writing effective descriptions` (:201), `### Progressive disclosure patterns` (:251). "Field list" is not a heading; the list is the `<Note>` at bp.md:148-166 inside `## Skill structure`. Nit.

## 5. "Not stated" sweeps: CONFIRMED

- Name equals directory: `grep -niE 'match the (parent |skill )?director|folder name|directory name|parent director' bp.md overview.md` gives exit 1. Broader "match" hits are bp.md:63 and :627 ("Match the level of ..."), not rules.
- Consecutive hyphens: `grep -niE consecutive bp.md` gives exit 1; overview combined sweep has no hit.
- Unknown top-level fields: `grep -niE 'unknown field|unrecognized' bp.md` gives exit 1. Broader `additional|extra|custom|other field|propert|allowed|top-level|frontmatter field|metadata` hits are prose only (bp.md:19, 22, 269, 1151; overview.md:59, 96). No field rule.
- Omitted SHOULD: bp.md:163 "Should describe what the Skill does and when to use it" is not in the S019 column. Not a MUST. Gap, nit.

## 6. Drift claim: DEFECT, low

`diff` of the round-47 copy against bp.md gives exit 1. Both files are 1,191 lines. There are 62 change records, all in place, 79 lines per side.

- Changed bytes: 257-259 ("* Keep SKILL.md body ..." becomes "* Keep the `SKILL.md` body ...."), 1131 and 1136 (backticks, link text), 1140 (same class as 257), 1150 (backticks).
- Unchanged bytes: bullets 153-156, 160-162 and 1133-1134, and the sentence at 206.
- No cell misquotes. The phrase in the 500-line cell survives.
- C2ClaudeDocs.md F2 says the 500-line sentence is "byte-identical at both shas". Its diffs covered only 145-170 and 1100-1191, never 257. Its own 1100-1191 evidence lists 5 changed lines, including 1140. So F2 is unverified for 257 and contradicted for 1140.
- Repair wording: "no rule's content changed; copy edits (backticks, article, period) touched bp.md 257, 1140 and 1150; the rule bullets 153-162 and 1133-1134 are byte-identical."

## 7. S019 row, "supersedes S003": CONFIRMED

1. "The 500-line body rule is not Anthropic-only": spec.md:237 "Keep your main `SKILL.md` under 500 lines.", under `## Progressive disclosure` (spec.md:229). Confirmed.
2. "No-XML-tags rule on name and description is Anthropic-only": `grep -niEc 'angle|xml' spec.md` gives 0 (exit 1). Confirmed.
3. "Reserved words and third person are Anthropic-only": spec `grep -ciF 'third person'` gives 0 and `grep -ciF 'reserved'` gives 0. Confirmed.

## 8. Corrections to my first draft

- I wrote that reserved words and third person were "the only statements among the opened sources". Wrong for reserved words: overview.md:217 states them too. Third person is only bp.md:206 among the two Anthropic pages. The row's Anthropic-only conclusion still stands.
- I wrote that the 90d recheck "matches every other docs-tier row". Wrong: S007 (docs) is 365d. The 90d docs rows are S002, S003, S013, S014, S019 and S021.
- I wrote that a hash recheck "will false-alarm roughly daily". Unsupported. The only evidence is one change inside a 16-hour window.
- Spec fetch timing was recorded as "same run". It was a separate command in the same session.

## 9. Records and convention, checked at both commits

- S019 used-by (row 32): 84b9c9ba lists the knowledge entry only; eb5a80f lists SKILL.md and the knowledge entry. Fixed.
- SOURCES.md:38 Paths line: 84b9c9ba reads "S001 → S008 → S003 → S002 → S011" and "vendor-only rules (… 500 lines) that the spec does not carry". eb5a80f reads "S018 → S017 → S008 → S019 → S012 → S002 → S011", with the 500-line rule shared with the spec. Fixed.
- S003 row (row 16): used-by at eb5a80f is lessons round-46 and round-47; SKILL.md removed. Teaches cell still says "an Anthropic-only rule the open spec lacks". Left as written, the same convention as S001, S010 and S013.
- Lesson gate contradiction: round-48.md:25-26 against :75-77. Open.
- Contract rule 2 text: `_glob` for SOURCES-CONTRACT* under the fleet root found no file. The convention above is taken from the lesson's own text.

## 10. Adjacent S019 citations

- FAIL detail string: 75f671b and 84b9c9ba carry "S003 Anthropic rule ... is stricter" at 1307-1308; the file is identical at both commits. eb5a80f carries "S019 ... (S018) ... two disagree in both directions" at 1307-1310. Fixed by d28b16b.
- Knowledge entry point 4 at eb5a80f cites "verify_skill_checklist.py:1307-1311"; the string ends at 1310. Nit.
- PROVINCE.md:15 at eb5a80f says "superseded as a row by S019 in round 48". Consistent.
- SKILL.md:151 at eb5a80f cites S019 and does not cite S003. Consistent.

## 11. Recheck and cadence

- S019 recheck is "90d". The page changed once inside a window of about 16 hours, so 90d is not a freshness control here.
- Uncommitted worktree recheck: `curl -fsSL …best-practices.md | grep -c 'Cannot contain XML tags'` gives 2, exit 0. It covers two cells. It does not check 257, 206 or the reserved-word cell.

## 12. Residual risk and gaps

- Skills API guide and Claude Code page: not re-opened here (see C2ClaudeDocs.md).
- Spec side only was checked. Packager, skills-ref and Codex columns belong to other seats.
- Uncommitted worktree edits are not landed. Re-verify after commit.
- The lane may move again during the wave. All verdicts above are pinned to eb5a80f.
