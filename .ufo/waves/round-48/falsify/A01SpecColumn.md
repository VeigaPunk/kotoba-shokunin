# Round-48 falsify, A01SpecColumn (spec S018 column, point 2, point 7)

Seat: KotobaR48.A01SpecColumn (leaf). Target: spec column of
`corpus/knowledge/frontmatter-rule-authorities-round48.md`, plus points 2 and 7. Judged on freshness.
Lane read only; this file is the only write.

## Verdict

DEFECT, medium. No spec quote is wrong. Seven spec line citations are right (63, 64, 66, 67, 101,
161, 237), and all ten claims hold against today's spec. The defects are in evidence and wording:

- Three negative cells lack a working search: angle brackets (printed search cannot find "angle" or
  "xml", medium); reserved words (no file operand, low); unknown fields (no search named, low).
- Point 2 cites the table row at spec.md:27; it is at spec.md:30. It also says that row contradicts
  line 64. It does not; the inconsistency is inside line 64 alone (medium).
- Point 7's conclusion holds, but its printed sweep covers 2 of 10 keywords, "gives maxima only" is
  false, and the cited heading is mis-cited (low).
- Teaching point 1 ("Only the spec states the name-equals-directory rule") is contradicted in code by
  the entry's own skills-ref row (low).
- Freshness: today's spec bytes match the round-47 pin. The round-46 to round-47 byte change is not
  recorded in the entry (residual, medium).

## Fetch record (UTC; sha256; run = executed, read = source read only)

- https://agentskills.io/specification.md: 2026-10-22T08:50:40Z; HTTP 200; 7,608 B; 260 lines;
  sha256 9a67de89132948b2300b8dc87b93817971d47f9be89b644444965881a8dfde16. Matches the entry and
  round-47 record (`.ufo/waves/round-47/build/SrcS001.json:23-24`). Run.
- skills-ref `validator.py` at 69ef37e9: 2026-10-22T08:54:06Z; sha256 b5ee3d85... (matches). Read only.
- Packager `quick_validate.py` at dbd4588f: 2026-10-22T08:55:21Z; sha256 67cf5703... (matches). Read only.
- RFC 2119, https://www.rfc-editor.org/rfc/rfc2119.txt: 2026-10-22T08:54:06Z; sha256 3c2ceb7b...
  Quote, lines 24-25: "These words are often capitalized."
- Tools: none installed or updated.

## Spec column, cell by cell (spec.md lines from the fetched `.md`)

1. name length, "Must be 1-64 characters", :63. CONFIRMED.
2. charset, "May only contain unicode lowercase alphanumeric characters ... and hyphens", :64. CONFIRMED.
3. directory match, "Must match the parent directory name", :67. CONFIRMED.
4. consecutive hyphens, "Must not contain consecutive hyphens", :66. CONFIRMED.
5. description length, "Must be 1-1024 characters", :101. CONFIRMED.
6. angle brackets "not stated". Claim holds (command C). DEFECT (evidence, medium): in grep -E, backslash-pipe
   is a literal pipe, so the printed search looks for "angle|xml" and exits 1 on any text (command B).
7. third person "not stated". Claim holds (command D). CONFIRMED.
8. reserved words "not stated". Claim holds (only :141, an example "Designed for Claude Code").
   DEFECT (evidence, low): the printed search has no file operand, so it reads stdin (command E).
9. unknown fields, "no ban; metadata holds extra properties", :161. The paraphrase holds, and no
   top-level ban exists (command F). DEFECT (evidence, low): no search is named; Q14
   (corpus/QUALITY.md:25) requires one.
10. body length, "Keep your main `SKILL.md` under 500 lines", :237. CONFIRMED.

Totals: 7 CONFIRMED, 3 DEFECT (evidence only; all three claims are true).

## Commands (exit codes)

- A. `grep -niE 'angle\|xml' specification.md`: exit 1 (printed form).
- B. Control: `printf 'an angle bracket\nxml tag\nangle|xml\n' | grep -niE 'angle\|xml'` prints only
  `3:angle|xml`, exit 0.
- C. `grep -niE 'angle|xml' specification.md`: exit 1. `grep -n '[<>]'` finds only Markdown quote
  markers and :234 "(\< 5000 tokens recommended)", a token budget.
- D. `grep -niE 'third|person|voice|pronoun|imperative' specification.md`: exit 1.
- E. `grep -niE 'reserved|anthropic|claude' specification.md` finds only :141. Control:
  `printf 'reserved word\n' | grep -niE 'reserved word'` exits 0, so the printed form reads stdin.
- F. `grep -niE 'unknown|unexpected|extra|not allowed|disallow|forbid|reject|only (the )?(following|these)|other (fields|keys)'`
  exits 0 with false positives only (:51 "Extract", :86 and :94 name examples, :108, :246-247).
- G. `grep -c -e 'MUST' -e 'SHOULD' specification.md`: count 0, exit 1 (printed form, 2 of 10 words).
  `grep -nwE 'MUST|REQUIRED|SHALL|SHOULD|RECOMMENDED|MAY|OPTIONAL' specification.md`: exit 1.
- H. `grep -n '^#' specification.md`: `59:#### \`name\` field`, `229:## Progressive disclosure`.
  `grep -n '#### name field'` finds nothing.
- I. `curl -fsSL https://agentskills.io/specification.md | grep -c 'Must match the parent directory name'`:
  count 1, exit 0.

## Point 2 (charset "self-contradiction"): DEFECT (medium)

- CONFIRMED: line 64 pairs "unicode lowercase alphanumeric characters" with a parenthetical listing only
  `a-z` and `0-9`. Read as exhaustive, "unicode" is wrong; read as examples, the list is incomplete.
- REFUTED as stated: the "Lowercase letters, numbers, and hyphens only" sentence is at :30 (`grep -n
  'Lowercase'` gives `30:`), not :27 (blank). It does not contradict line 64 on either reading, since
  "lowercase letters" includes Unicode letters. Cite line 64 alone, or call the spec ambiguous.
- Read from source, not run: skills-ref takes the Unicode reading (validator.py:37 NFKC; :54
  `c.isalnum() or c == "-"`). The packager takes the ASCII reading (quick_validate.py:65
  `re.match(r'^[a-z0-9-]+$', name)`).

## Point 7 ("no RFC 2119 keywords"): claim CONFIRMED; evidence and wording DEFECT (low)

- Full uppercase sweep (command G) finds no keyword. The printed command covers only MUST and SHOULD.
- RFC 2119 says the words "are often capitalized" (:24-25) and lists them in capitals (:29-31). A
  search for an explicit all-caps mandate exits 1. My reading, not a quote: title-case "Must",
  "Should", "May" and "We recommend" are not the RFC's keywords, and the spec never invokes RFC 2119.
- DEFECT (low), "gives maxima only": the table also states "Must not start or end with a hyphen"
  (:30) and "Non-empty." (:31). The claim that it omits the consecutive-hyphen and directory rules is
  CONFIRMED (:30 has neither).
- DEFECT (low): "`#### name field` section" does not exist. The heading is "#### `name` field" at :59.

## Teaching point 1 ("Only the spec states the name-equals-directory rule"): DEFECT (low)

The entry's own skills-ref row cites validator.py:60-65, which enforces the match in code (read, not
run). The unqualified "only" is wrong; the prose-only version is what the table supports.

## Freshness

- Spec today: 7,608 B, sha256 9a67de89..., identical to the round-47 record (SrcS001.json:23-24;
  SrcS001.md:13). "Byte-identical to the round-47 fetch" is CONFIRMED at hash level.
- Drift not recorded (residual, medium): the round-47 record says the `.md` was 4c649bdf... at round 46
  (fetched 2026-10-19T18:40:53Z) and 9a67de89... at round 47 (2026-10-21T15:54:19Z). The old bytes were
  not kept, and ten normalizations did not reproduce the old hash (SrcS001.md:28). The entry should
  record this and say the lane cannot tell whether any rule row moved.
- The recheck guards one sentence (:67). Its comment "0 means the spec's rule text moved" overclaims;
  a count of 1 does not confirm the other cells. The `.md` sha256 is the better detector (low).
- Header nit (low): the S018 header (entry and `corpus/SOURCES.md:31`) cites the HTML page
  (459,866 B, per SrcS001.md:12); every line number refers to the `.md`.

## Residual risk and verification gaps

- The validator and packager were read, not executed; their behavior claims rest on pinned source.
- The lane checker (S020), the skills-ref run and fleet files were not run or written.
- Round-46 bytes are not in the lane, so rule-level drift between 2026-10-19 and 2026-10-21 is unknown.
