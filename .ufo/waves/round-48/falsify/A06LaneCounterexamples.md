# A06 LaneCounterexamples: round-48 falsify of the counterexample table

Seat: KotobaR48.A06LaneCounterexamples (leaf, no delegation). Date: 2026-10-22 (UTC).
Target: "Round-47 counterexamples, run (routed item 3)", `corpus/knowledge/frontmatter-rule-authorities-round48.md:86-94`, at C1 commit `887b6af54d3f4446f1fe51dc16f26b2e83bc82e1`.
Private clone: `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A06LaneCounterexamples/clone` (HEAD 887b6af). Fixtures: `.../A06LaneCounterexamples/fixtures2/`.

## Verdict

- CONFIRMED, lane column, 3 of 3 rows. Statuses match the table. Observed exit codes 0, 0, 1.
- CONFIRMED, packager column, 3 of 3 rows. Two routes: my PyYAML emulation of the cited S012 lines (validator not executed), and sibling A03PackagerColumn.md, which ran the script itself with the same three verdicts.
- NOT RE-RUN, skills-ref column. Build-wave receipts match the table text. I did not execute the validator, because my named command is the lane checker only.
- DEFECT, MEDIUM, records, verdict-neutral (D1): entry lines 19-20 pair upstream `validator.py` sha256 `b5ee3d85…` with "PyPI skills-ref 0.1.1 run". The 0.1.1 wheel's file is `7b5cb3dc…`.
- DEFECT, LOW, lane false FAIL (D2): the escape backstop fires on single-quoted, plain and block scalars. Its docstring says double-quoted only.
- DEFECT, LOW, lane wording (D3): the PASS detail says "no XML tag" where the lane cannot see one.
- DEFECT, LOW, reproducibility (D4): the alias and Unicode rows have no committed fixture, and the alias row depends on anchor order.
- COSMETIC (D5): stale label "lane tip 75f671b".
- No HIGH finding.

## 1. Required lane runs

Command, from the clone root:
`python3 -B verifiers/verify_skill_checklist.py --skill <fixture>/SKILL.md --check trigger.frontmatter_parses --check trigger.name_directory --check trigger.no_xml_tag --json`

| row | fixture (SKILL.md sha256) | rc | frontmatter_parses | name_directory | no_xml_tag | table lane cell | match |
|---|---|---|---|---|---|---|---|
| YAML alias | f1-alias-hidden-tag (dc7e78ce…) | 0 | PASS "description 2 chars" | PASS | PASS | PASS ("description 2 chars") | yes |
| Unicode name | 技能-测试 (675ab5c0…) | 0 | PASS "description 62 chars" | PASS | PASS | PASS | yes |
| escaped | f3-dq-escaped-skills (1ddd6eb0…) | 1 | PASS | PASS | FAIL "XML tag in description: '\\u003c'" | FAIL, names `\u003c` | yes |

- The JSON `exit_code` field equals rc in every run.
- `--self-test` exit 0, "0 failure(s) over 1845 assertions". Checker sha256 `4ea2100d…`, the same bytes C2 measured at 75f671b.
- Construction note (mine): my first alias build put `description: *d` above its `&d` anchor. PyYAML rejects that as "found undefined alias 'd'", so a packager run would print a YAML error, not angle brackets. The lane still PASSes it (rc 0). The rebuilt fixture defines the anchor under `metadata` first, the same shape as C2's f02 fixture.

## 2. Packager column (S012)

- Emulated by me: PyYAML 6.0.3 `yaml.safe_load` on the frontmatter that the regex at quick_validate.py:27 extracts (line 35), then the rules at lines 44-84.
- Alias, anchor first: description parses to `<b>Use <skills> here…`, so FAIL at line 81. Matches the table.
- Unicode `技能-测试`: FAIL "should be kebab-case" at line 66. Matches.
- Escaped: description parses to `Use <skills> here…`, so FAIL at line 81. Matches.
- Sibling run (A03PackagerColumn.md, same day): same three verdicts, exit 1, same messages.
- Exit path: `sys.exit(0 if valid else 1)` at line 103.

## 3. skills-ref column (receipts and source only)

- Receipts (C2SkillsRefRun.md, C2SkillsRefSource.md F7): alias gives "Found confusing disallowed anchor token", exit 1. `技能-测试` gives "Valid skill". Escaped gives validate exit 0, and `read-properties` decodes it to `<skills>`.
- Source read today: validator.py:37 (NFKC), :54 (`isalnum`), :61-62 (NFKC on the directory name). parser.py:6 imports strictyaml and :53 calls `strictyaml.load`.
- My emulation of the name rules (pure Python, lines above): `技能-测试` gives no errors (valid, matches the table). NFD directory with NFC name gives no errors (valid), while the lane FAILs it (section 4).

## 4. Boundary probes (extra rows; lane run, packager emulated)

| probe | rc | no_xml_tag | packager (emulated) | reading |
|---|---|---|---|---|
| alias, alias before anchor | 0 | PASS | FAIL "Invalid YAML … found undefined alias 'd'" | construction trap (D4) |
| single-quoted `\u003c` | 1 | FAIL | PASS (backslash text kept) | lane false FAIL (D2) |
| plain scalar `\u003c` | 1 | FAIL | PASS | lane false FAIL (D2) |
| block scalar `\u003c` | 1 | FAIL | PASS | lane false FAIL (D2) |
| raw `<技能>` | 0 | PASS | FAIL (any `<`, line 80) | lane false PASS (D3) |
| café, NFD directory, NFC name | 1 | name_directory FAIL | skills-ref: match after NFKC | literal compare, disclosed in entry |
| control, plain | 0 | PASS | PASS | control |
| committed `verifiers/fixtures/checklist/xml-tag-dq-escape` | 1 | FAIL | not run | in-repo escape fixture agrees |

## 5. Findings

D1, MEDIUM, records, verdict-neutral. Entry lines 19-20 name upstream `validator.py` sha256 `b5ee3d85…` in the same sentence as the PyPI 0.1.1 run. I fetched the 0.1.1 wheel (https://pypi.org/pypi/skills-ref/0.1.1/json, accessed 2026-10-22T08:57:27Z). Its `skills_ref/validator.py` is 5,347 B, sha256 `7b5cb3dc…`. Upstream is 5,154 B, `b5ee3d85…`. C2SkillsRefRun.md F2 records the same difference, and its Risks section flags this exact sentence; the committed entry still carries it. SOURCES.md:30 labels S017 "v0.1.0", while the entry says 0.1.1 ran. C2SkillsRefRun F3 reports identical behavior across channels, so the verdicts stand. Fix: name the executed wheel (`7b5cb3dc…`) and the upstream blob (`b5ee3d85…`) separately, and align the version label.

D2, LOW, lane false FAIL, docs wrong. The docstring at verify_skill_checklist.py:100-101 says the check covers "a YAML double-quoted `\x3c`/`\u003c` escape that decodes to one". The regex at :409 runs on the value after parse_frontmatter (515-602) strips matching quotes, and it runs in every scalar style. The single-quoted, plain and block probes all FAIL here, while the packager's rule (emulated) passes them. Entry line 69 names only the single-quoted false positive; plain and block scalars are not named (the double-quoted case at line 70 is a true positive). Fix: restrict the check to double-quoted scalars (the parser must keep the quoting style), or correct the docstring and the entry list.

D3, LOW, wording. The PASS detail "no XML tag in name, description" is printed for (a) the alias row, where the YAML-resolved description is `<b>Use <skills> …`. The docstring at :213-216 excludes aliases, but the detail text does not. And for (b) `<技能>`, the regex at :405 admits ASCII start characters only, while the docstring at :98-99 says "a name character". The entry says "ASCII" at line 42; the detail string does not. Cosmetic: the FAIL detail prints the match through %r, so the text shows `'\\u003c'` and the table shows `\u003c`.

D4, LOW, reproducibility. Repo grep found no committed alias or Unicode fixture (patterns `description: \*[A-Za-z]`, `&d "<b>`, `技能-测试` under verifiers/ and corpus/). Alias bytes appear only in round-47 prose. The escape row has a committed fixture. The alias row depends on anchor order, since alias-first is invalid YAML. The entry carries no fixture bytes, so "every lane cell is a run" cannot be re-run from the repo. Fix: commit the three fixtures with sha256 values and note the anchor-first requirement.

D5, COSMETIC. Entry line 26 and SOURCES.md:33 say "lane tip 75f671b". The checker is byte-identical at 887b6af (`git diff --stat 75f671b -- verifiers/verify_skill_checklist.py` is empty; sha256 `4ea2100d…`). The content pin holds; only the label is stale.

## 6. Freshness (fetched or queried 2026-10-22, UTC)

| source | access (UTC) | bytes | sha256 | result |
|---|---|---|---|---|
| S018 agentskills spec | 08:53:50Z | 7,608 | 9a67de89… | match; recheck grep count 1 |
| S012 quick_validate @dbd4588 | 08:53:56Z | 3,972 | 67cf5703… | match |
| S017 validator @69ef37e9 | 08:53:56Z | 5,154 | b5ee3d85… | match |
| S017 parser @69ef37e9 | 08:55:49Z | n/a | 9a74c9a9… | strictyaml at lines 6, 53 |
| S019 best-practices .md | 08:53:56Z | 42,169 | f0a5d61b… | match; rule lines 153-162 |
| anthropics/skills main (ls-remote) | 08:56:29Z | n/a | dbd4588f… | pin still HEAD |
| agentskills/agentskills main (ls-remote) | 08:56:29Z | n/a | 69ef37e9… | pin still HEAD |
| PyPI skills-ref 0.1.1 wheel | 08:57:27Z | 12,918 | d35db5bb… | matches PyPI digest; validator.py 7b5cb3dc… (D1) |

Located quotes (25 words or fewer): spec.md:67 "Must match the parent directory name"; quick_validate.py:81 "Description cannot contain angle brackets (< or >)"; best-practices.md:155 "Cannot contain XML tags".

## 7. Commands and exit codes

- `git clone -q` of the lane into the scratch clone: 0. `git checkout -q 887b6af…`: 0.
- Required lane runs: 0, 0, 1. Extra probes in section 4 order: 0, 1, 1, 1, 0, 1, 0, 1, then the committed fixture: 1.
- `python3 -B verifiers/verify_skill_checklist.py --self-test`: 0.
- `curl -fsSL` fetches (spec, quick_validate, validator, parser, best-practices, PyPI JSON, PyPI wheel): 0 each. `git ls-remote` ×2: 0.
- Emulations and parses (`python3`, PyYAML 6.0.3): 0.

## 8. Verification gaps

- skills-ref: not executed. Its cells rest on receipts, source reads and my name-rule emulation.
- Packager: emulated here, executed by sibling A03 (not repeated).
- Not checked: the "byte-identical to round 47" claims for S018 and S019, because I hold no round-47 bytes; records other than the entry and SOURCES rows.
- Lane default run (all 11 checks) not run. The table cells cover only the named checks.
- Sibling A08LaneRuleColumn.md mutation-tested the other lane cells. It agrees with my literal name-directory result.
- Installs: none. Tools used: system python3 3.14.8 with PyYAML 6.0.3, curl, git.
- Lane checkout: no writes except this report. Scratch fixtures, sources and clone are under /fast/scratch/hyaku/kotoba-r48-a2/seats2/A06LaneCounterexamples/.
