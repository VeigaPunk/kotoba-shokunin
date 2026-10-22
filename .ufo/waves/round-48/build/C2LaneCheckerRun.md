# C2LaneCheckerRun — the lane's own `trigger.no_xml_tag` vs S012 / S003 (routed defect 3)

Seat: `KotobaR48.C2LaneCheckerRun` (leaf executor). Date 2026-10-22 (UTC).
Scope: measure what `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` actually
executes on the routed counterexample classes, and state where that verdict agrees with or
diverges from S012 (Anthropic `quick_validate.py`, parsed description) and S003 (Anthropic
docs, "cannot contain XML tags"). Read-only on the lane checkout except this report; all
code work in `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2LaneCheckerRun/` (private clone of
the lane at `75f671b109d8eddd0d64c1429bd6379fe577175a`). No tool installs (system Python
3.14.8 + PyYAML 6.0.3 already present; no pacman transaction was attempted).

## Findings

**F1 — how to point the script at an arbitrary file (both routes work, and they agree).**
CLI: `python3 -B verifiers/verify_skill_checklist.py --repo <root> --skill <any>/SKILL.md
--check trigger.no_xml_tag --json`. `--skill PATH` is the arbitrary-file flag (default
`<repo>/SKILL.md`); `--repo` sets the command-resolution root; `--check` is repeatable and
restricts the run; `--json` gives machine output; `--map`, `--vocabulary`, `--max-lines`
are the other knobs (`--help`, exit 0). With the default check set (all 11 ids) an
arbitrary file yields `checklist.box_map_complete` N/A and unrelated FAILs
(`trigger.name_directory`, `trigger.literal_trigger_string`, `trigger.anti_trigger_clause`),
so `--check trigger.no_xml_tag` is required for a clean measurement. Exit code: 1 on any
FAIL, 0 when at least one check evaluated and none failed.
Module route: `importlib.util.spec_from_file_location` on the verifier, then
`parse_frontmatter(lines) -> (fields, problem)` (`:515`) and
`check_no_xml_tag(fm) -> (status, evaluated, detail)` (`:1294`); `main(argv)` wraps the CLI.
Both routes returned identical verdicts on all 10 fixtures (`import_matches_cli` true 10/10).

**F2 — what the check actually executes (rule statement).** `check_no_xml_tag` (`:1294`)
takes the values the lane's own lenient structural frontmatter parser produced for `name`
and `description` (`:515-602`), skips a field whose value is empty (`:1298`), and fails when
either value matches `XML_TAG_RE` (`:404-406`: a *well-formed ASCII* XML tag / comment /
CDATA / processing-instruction / declaration shape) **or** `YAML_ANGLE_ESCAPE_RE`
(`:409`: the literal text `\x3c`, `\x3e`, `\u003c`, `\u003e`, `\U0000003C/3E`), searched on
the **unparsed** frontmatter text (`:1304`). It does not resolve YAML aliases, does not
decode YAML double-quoted escapes (the escape backstop is a text match, not a decode), does
not apply plain-scalar typing, and does not NFKC-normalise. The parser folds block scalars
by appending each continuation line with one space (`:556`) — for the folded fixture below
that coincides with YAML's own fold.

**F3 — per-case verdicts.** `lane` = the lane checker; `S012` = S012's *parsed-description*
rule, measured by executing Anthropic's own `quick_validate.py` (sha256 `67cf5703…fde365`,
pin `dbd4588`) on the same fixture; `S003` = the Anthropic-docs rule "Cannot contain XML
tags", operationalised as a well-formed XML tag shape on the YAML-parsed description.

| case | description shape | lane | lane exit | S012 | S003 | divergence |
|---|---|---|---|---|---|---|
| f01-raw-tag | `<skills>` raw | FAIL | 1 | FAIL (exit 1, "Description cannot contain angle brackets (< or >)") | FAIL | none |
| f02-alias-anchor | YAML alias `*d` → anchored `"<b>"` (anchor inside `metadata`) | **PASS** | 0 | **FAIL** (exit 1, angle-bracket message) | **FAIL** | lane misses a real XML tag behind an alias |
| f02b-alias-topkey | same alias, anchor on a top-level key | **PASS** | 0 | exit 1 but on the *unexpected-key* branch (fixture artifact); description branch also fails | **FAIL** | lane misses the tag |
| f03-escaped-unicode | `"\u003cb\u003e"` (double-quoted) | FAIL | 1 | FAIL (exit 1, angle brackets) | FAIL | none — but by a different mechanism (text match, not decode) |
| f04-unicode-name | `name: café-skill`, plain description | PASS | 0 | exit 1 on the **name** rule ("should be kebab-case"), not the angle rule | PASS on angle; **FAIL on S003's name charset** ("only lowercase letters, numbers, and hyphens") | angle rules agree; the Unicode *name* gap is uncovered by any lane check |
| f05-arrow | `Converts input -> output …` | **PASS** | 0 | **FAIL** (exit 1, angle brackets — `>` present) | PASS | lane laxer than S012 only |
| f06-comparison | `Compares a < b and reports …` | **PASS** | 0 | **FAIL** (exit 1, angle brackets) | PASS | lane laxer than S012 only |
| f07-folded-split | folded block, `<` end of one line / `b>` start of next | **PASS** | 0 | **FAIL** (exit 1, angle brackets) | PASS | lane laxer than S012 only |
| f08-single-quoted-escape | `'\u003cb\u003e'` (single-quoted → literal backslash text) | **FAIL** | 1 | PASS (exit 0, "Skill is valid!") | PASS | lane **stricter** than both (false positive) |
| f09-fullwidth-desc | `Uses ＜skills＞ tags …` | PASS | 0 | PASS (exit 0) | PASS | none (NFKC would map `＜skills＞`→`<skills>`; not checked by anyone) |

Counts: lane FAIL 3 / PASS 7. Divergence from S012's parsed-description rule: **6/10**
(f02, f02b, f05, f06, f07, f08). Divergence from S003's XML-tag rule: **3/10** (f02, f02b,
f08). The lane's parsed description equals the YAML-parsed description on every fixture
except f02/f02b (lane `*d` vs YAML `<b>`) — the alias is the only place where the lane's
frontmatter parse and a real YAML parse disagree.

**F4 — the five divergence classes (routed defect 3, now measured).**
A. *Alias-hidden tag* (f02, f02b): the lane parser keeps the literal `*d`; S012's
`yaml.safe_load` resolves it to `<b>`. Lane PASS, S012 FAIL, S003 FAIL. The lane's
frontmatter parse is not a YAML parse.
B. *Non-tag angle brackets* (f05 `->`, f06 `a < b`, f07 folded `< b>`): lane PASS, S012 FAIL,
S003 PASS — exactly the "stricter than S003" gap the check's own detail line claims to
close but does not.
C. *Escape-text false positive* (f08): the lane's `YAML_ANGLE_ESCAPE_RE` fires on the
literal `\u003c` inside a single-quoted scalar, where YAML keeps the backslash text;
S012 accepts the file. The lane is stricter than both authorities here.
D. *Escape-text true positive* (f03): same backstop, but the decoded value really is `<b>`,
so the FAIL agrees with S012/S003 by a different mechanism (text match, not decode).
E. *Unicode name* (f04): outside the angle rule entirely — S012 and S003 reject
`café-skill` on their *name* rules, and the lane has no name-charset check at all
(`trigger.name_directory` only compares name to the directory name).

**F5 — the check's detail line overclaims.** `check_no_xml_tag` emits the fixed string
"…Anthropic's packager bans any '<'/'>' and is stricter" (`:1307-1308`). Measured: the
implemented rule is **not** stricter than S012 (classes A and B are missed) and is **not**
S003 either (class A misses a real tag; class C fails where both pass). The honest label
is: *a lexical well-formed-ASCII-tag shape plus a YAML angle-escape backstop, applied to
the unparsed frontmatter text of `name`/`description`*. Recommend the C2 entry carry this
wording, and the defect list carry the detail-string overclaim as a fixable text defect.

**F6 — freshness of the two authorities, re-opened today.** S012: `quick_validate.py` at
pin `dbd4588` fetched today, sha256 `67cf5703402013936c8fb75ad6a1afecd8841d45cc5e606b634eb05825fde365`,
identical to the round-47 receipt and to the sibling seat's HEAD fetch. S003: the Anthropic
best-practices page re-fetched today, sha256
`f0a5d61b67123a31527e64aae7c5cfc05c4c7e27fff16f5b35ea14b135423960` — **not** the
round-46 recorded `727f3fa1…`, i.e. the page bytes changed since round 46, while the rule
text "Cannot contain XML tags" is still present at lines 155 (description) and 162 (name).
A superseding source row is warranted for S003 on the byte change alone.

## Commands and exit codes (all run in the seat scratch dir)

- `git clone -q /home/vgpnk/Projects/shokunin/kotoba-shokunin lane` → exit 0; `git -C lane
  rev-parse HEAD` → `75f671b109d8eddd0d64c1429bd6379fe577175a`.
- `sha256sum lane/verifiers/verify_skill_checklist.py <lane>/verifiers/verify_skill_checklist.py`
  → both `4ea2100dee220077eead8ed8cfc2c5acb311ffff8746451bb5fd12b202c5e38a` (the measured
  instrument is byte-identical to the lane file).
- `python3 -B lane/verifiers/verify_skill_checklist.py --self-test` → exit 0,
  "0 failure(s) over 1845 assertions".
- `python3 -B runner.py` → exit 0; writes `results.json` and `run-transcript.txt`
  (one CLI run + one quick_validate run + one module-import run per fixture).
- Per-fixture lane run: `python3 -B lane/verifiers/verify_skill_checklist.py --repo fixtures
  --skill fixtures/<case>/SKILL.md --check trigger.no_xml_tag --json` → exit 1 for
  f01/f03/f08, exit 0 for the other seven (`cli-transcript.txt`).
- Per-fixture S012 run: `python3 -B qv.py fixtures/<case>` → exit 1 for
  f01/f02/f02b/f03/f04/f05/f06/f07 and exit 0 for f08/f09 (f02b's exit 1 is the
  unexpected-key branch and f04's is the name-kebab-case branch, not the angle rule).
- `python3 -B lane/verifiers/verify_skill_checklist.py --help` → exit 0 (flag inventory).
- `curl -fsSL https://raw.githubusercontent.com/anthropics/skills/dbd4588…/quick_validate.py`
  → exit 0; `curl -fsSL https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`
  → exit 0.

## Sources opened this session

- `https://raw.githubusercontent.com/anthropics/skills/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/quick_validate.py`
  — accessed 2026-10-22T08:14:16Z, sha256 `67cf5703…fde365`. Quote (`:81`): "Description
  cannot contain angle brackets (< or >)". Location: `quick_validate.py:79-81`, inside
  `if '<' in description or '>' in description:` on the `yaml.safe_load` result (`:35`).
- `https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices.md`
  — accessed 2026-10-22T08:18:04Z, sha256 `f0a5d61b…3423960` (round-46 fetch was
  `727f3fa1…`; bytes changed). Quote (`:155`): "Cannot contain XML tags". Location:
  § Skill structure → `description` field rules (`:155`); the same rule repeats for `name`
  at `:162`, which also states "Must contain only lowercase letters, numbers, and hyphens".

## Receipts and limits

- Scratch (private clone, fixtures, runner, transcripts, `results.json`, fetched sources):
  `/fast/scratch/hyaku/kotoba-r48-a2/seats/C2LaneCheckerRun/`.
- Fixtures are synthetic and purpose-built; their bodies are one line, so unrelated checks
  (`trigger.literal_trigger_string`, `trigger.anti_trigger_clause`) fail by design and were
  excluded from the measurement via `--check trigger.no_xml_tag`.
- S003's prose rule has no machine form; "cannot contain XML tags" was operationalised as
  the well-formed XML tag/comment/CDATA/PI/declaration shapes (`XML_TAG_RE`), which is the
  same shape set the lane encodes. A stricter reading of "XML tags" is possible.
- S012's verdict column is the executed validator, not an emulation; the emulation
  (`'<' in parsed or '>' in parsed` on `yaml.safe_load`) agreed with the validator on all
  10 fixtures.
- The lane's `description` value equals the YAML-parsed value on every fixture except the
  alias cases — the frontmatter parser is only divergent where YAML aliasing is involved.
- Nothing in the lane checkout was edited, and no git/jj write command was run there.

Report: .ufo/waves/round-48/build/C2LaneCheckerRun.md
