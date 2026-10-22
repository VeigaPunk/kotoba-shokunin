# A16S020Teach — falsify SOURCES row S020 (own-work, supersedes S010)

Seat: `KotobaR48.A16S020Teach` (leaf critic). Date 2026-10-22 (UTC). Axis judged: freshness.
Scratch area (private clones, fixtures, transcripts): `/fast/scratch/hyaku/kotoba-r48-a2/seats2/A16S020Teach/`.
I installed no tools and ran no pacman transactions. In the lane checkout I wrote only this report and ran no git or jj write commands there.

## Verdict

**CONFIRMED with one LOW defect.**
- Every number in S020's anchor reproduces at `75f671b`: 1845 assertions, `--json` exit 0 with 11 PASS / 0 FAIL, and 41 boxes split 8 executed / 0 delegated / 33 unexecuted. The line anchors 404, 409 and 1294 also match.
- My own fixtures, run through Anthropic's actual packager, support all three parts of the teach clause.
- **D1 (LOW, fixable, a provenance and freshness gap):**
  - The row's `recheck` is `on-commit`. At the very next commit, `84b9c9b`, `--json` already exits 1 (10 PASS / 1 FAIL), because the records commit cites a file that does not exist.
  - The anchor names only `C2LaneCheckerRun.md` as the seat that ran the checks, but that report contains only the self-test count. The `--json` 11/0 result and the box counts appear only in `FrSourceDefects.md`.
  - The numbers are reproducible only when the checkout sits at `<fleet>/kotoba-shokunin`, and the row does not say so.

## Evidence: anchor numbers at 75f671b

Environment: Python 3.14.8 and PyYAML 6.0.3. The verifier `verifiers/verify_skill_checklist.py` has sha256 `4ea2100d…c5e38a`. It is byte-identical at `75f671b` and at `84b9c9b`; between those commits only `SKILL.md` changed (1 line).

| run | layout | exit | result |
|---|---|---|---|
| `--self-test` @75f671b | plain clone | 0 | `0 failure(s) over 1845 assertions` |
| `--json` @75f671b | plain clone at `seats2/A16S020Teach/lane` | **1** | 8 PASS / 3 FAIL: `name_directory` ('lane'), `trigger.citation_resolves` and `governance.citation_resolves` (`../.ufo/...` and `../PROTOCOL.md` do not resolve) |
| `--json` @75f671b | fleet-shaped clone (`fleet/kotoba-shokunin`, siblings symlinked to the fleet root) | **0** | 11 PASS / 0 FAIL / 0 N/A; `checklist.box_map_complete` "41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)"; governance evaluated 872 |
| `--self-test` @7ad7fad~1 (`61610ef`) | fleet-shaped clone | 0 | `0 failure(s) over 1597 assertions`, which is S010's count |
| `--self-test` @84b9c9b (tip) | fleet-shaped clone | 0 | 1845 |
| `--json` @84b9c9b (tip) | fleet-shaped clone | **1** | 10 PASS / 1 FAIL: `governance.citation_resolves` "SCORECARD.md:110: '.ufo/reports/round-48/kotoba.md' does not resolve" (evaluated 901) |
| `--json` on the live lane (read-only, `-B`), HEAD 84b9c9b | the lane itself | **1** | the same single FAIL at `SCORECARD.md:110` |

What the line anchors point to at `75f671b`:
- `:404`: `XML_TAG_RE = re.compile(`
- `:409`: `YAML_ANGLE_ESCAPE_RE = re.compile(r"\\(?:x3[cCeE]|u003[cCeE]|U0000003[cCeE])")`
- `:1294`: `def check_no_xml_tag(...)`
- `:1304`: the search runs on the lane's unparsed frontmatter values.

The claim that S010's counts and its "no XML-tag rule" clause have been stale since round 47 is confirmed:
- At `7ad7fad~1` the file has 0 `def check_no_xml_tag` and the self-test reports 1597 assertions.
- At `7ad7fad` there is 1 definition.

The row is well-formed:
- It has 13 fields (`NF=13`) and status `mined`.
- Its `used-by` file exists and cites S020 3 times.
- Its teaches cell opens with `supersedes S010 —`, as rule 2 of `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` requires.
- S010 is correctly left unchanged, since that rule makes rows append-only.

## Evidence: the teach clause, run independently

I ran 14 fixtures of my own design; I did not reuse the C2LaneCheckerRun fixtures. Each one went through two paths:
- the lane checker at `75f671b`: `--check trigger.no_xml_tag --json`;
- Anthropic's real packaging path: `python3 -m scripts.package_skill <dir> <out>`.

`package_skill.py:71-76` calls `validate_skill` and returns None when validation fails, so a refused case means the packager produced no `.skill` file.

| class | fixtures (YAML-parsed description) | lane | packager |
|---|---|---|---|
| alias-hidden tag | `a1` alias to `"<b> bold"` anchored in `metadata`; `a2` alias to plain `Use <skills> tags` | PASS, exit 0 | exit 1, "Description cannot contain angle brackets (< or >)", no file |
| non-tag brackets | `b1` `->`, `b2` `a < b`, `b3` `>= 3`, `b4` `<3`, `b5` `<user@example.com>` | PASS, exit 0 | exit 1, same message, no file |
| escape text outside a double-quoted decode | `c1` single-quoted `'\u003cb\u003e'`, `c2` plain `\x3c`, `c3` literal block `\u003e`, `c4` double-quoted `"\\u003c"` (decodes to backslash text) | **FAIL, exit 1** | exit 0, "Successfully packaged", `.skill` written |
| controls | `d1` double-quoted `"\u003cb\u003e"`, `d2` raw `<skills>` | FAIL, exit 1 | exit 1, no file |
| control | `d3` clean | PASS, exit 0 | exit 0, file written |

All three teach parts hold: the alias miss (2 of 2), the non-tag bracket miss (5 of 5), and the single-quoted false positive (c1).

Strongest counterexample to the clause's scope, which is not a falsification: the false-positive class is wider than "a single-quoted escape text". Plain (c2), block (c3) and double-quoted escaped-backslash (c4) text also fail in the lane and pass the packager. The root cause is that `:1304` matches escape text and never decodes it. The knowledge entry (`frontmatter-rule-authorities-round48.md:69`) names only the single-quoted instance. The clause is true but undersized; widening it is optional.

## Sources re-opened this session

The GitHub commits API returned 403 (`curl` exit 22). This is not needed, because the bytes at `main` and at the pin are identical.

1. `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`
   - Accessed 2026-10-22T08:51:27Z.
   - sha256 `67cf5703…fde365`, identical to `main` and to the round-47 receipt.
   - Quote (`:81`): "Description cannot contain angle brackets (< or >)".
2. `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/package_skill.py`
   - Accessed 2026-10-22T08:51:27Z.
   - sha256 `1a33059b…8d1c0f`, identical to `main`.
   - Quote (`:74-75`): "Validation failed: {message}" … "Please fix the validation errors before packaging."

## Impacted axes

- Freshness: S020 is an `on-commit` row, and its `--json` fact does not survive commit `84b9c9b`.
- Provenance: the anchor's single seat citation does not ground the `--json` numbers.
- Depth and operability: not affected, because the checker bytes did not change.

## Smallest safe corrections

1. Fix the root cause of the tip FAIL in the records commit. `SCORECARD.md:110` should cite `../.ufo/reports/round-48/kotoba.md`, the fleet-root form other rounds use. That file does not exist yet either: `../.ufo/reports/round-48/` is empty. Write the report, or drop the citation until it exists.
2. In S020's anchor, add `.ufo/waves/round-48/build/FrSourceDefects.md` as the seat for the `--json` 11/0 result and the box counts. Also note "run from `<fleet>/kotoba-shokunin` (`governance.citation_resolves` resolves `../` paths; `name_directory` needs the directory name)".
3. Optionally widen the teach clause to "fails escape text the packager accepts when it is not decoded by a double-quoted scalar (single-quoted, plain, block, escaped backslash)".

## Receipts (sha256)

- `results.json`: `3199867d…308fcf1`
- `runner.py`: `5637d7c6…96573d`
- `json-75f-fleet.json`: `cca486c0…a242`
- `json-tip-fleet.json`: `ce6b0750…11fbc`
- `selftest-75f.txt`: `67dcfe2f…7f37`
- Transcript: `run-transcript.txt`. Packaged `.skill` outputs are in `dist/`.

Report: .ufo/waves/round-48/falsify/A16S020Teach.md
