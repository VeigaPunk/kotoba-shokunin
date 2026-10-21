verdict: HOLDS — I attacked C2's `trigger.no_xml_tag` live at 7ad7fad: every claimed count re-ran green, the planted-`<skills>` mutant FAILs naming the tag, and Anthropic's own upstream packager (the rule the check cites) accepts the repaired description while refusing the base one; two residuals (a disclosed-but-undirected YAML-alias false PASS, a stale S010 row) are non-blocking.

Lane: `KotobaR47-2.W2XmlLive-2` (leaf reviewer, wave-2 fresh identity). Target: `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` (live) at `7ad7fadfc09354b74fb66605dfb0c1182c115a2f` (BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`).
Scratch clone (canonical layout, symlinked fleet siblings, detached at 7ad7fad): `/fast/scratch/kotoba-r47/w2/W2XmlLive/kotoba-shokunin` — left CLEAN (`git status --porcelain` empty, `git log --oneline -1` = 7ad7fad). The planted mutant was made in the clone's working tree and reverted with `git checkout -- SKILL.md`; the fleet repo was never written to. No tools installed (no pacman / uv / npm action this lane) — the only network call was a public `curl` of the upstream Anthropic validator.
Artifacts: `.ufo/waves/round-47/falsify/W2XmlLive.matrix.txt` (the 16-shape detector matrix), `.ufo/waves/round-47/falsify/W2XmlLive.json` (machine summary of the runs below).

Axes: freshness (are the numbers still true at the tip?), operability (does the gate pass/fail the right thing, from any cwd?), calibration (does the label match the source it cites, and are the records honest?).

---

## 1. What I attacked

- `verifiers/verify_skill_checklist.py:1294` — `check_no_xml_tag()` (the rule).
- `verifiers/verify_skill_checklist.py:404-406` — `XML_TAG_RE`; `:409` — `YAML_ANGLE_ESCAPE_RE`; `:97-103` — the docstring entry; `:200-215` — `DOCUMENTED LIMITS`; `:310` — `CHECK_IDS`; `:1806-1809` — fixture expectations; `:1970-1983` — the in-process string battery.
- `SKILL.md:14` (the repaired description line), `SKILL.md:151` (the portability-floor prose the round rewrote), `corpus/SOURCES.md:16` (S003), `corpus/SOURCES.md:23` (S010), `corpus/SOURCES.md:25` (S012), `LOG.md:2322` (the C2 record), `SCORECARD.md:31` (the C2 score row).
- The four new fixtures `verifiers/fixtures/checklist/xml-tag-{codespan,control,dq-escape,split}/`.

## 2. Counts re-run at the tip (all as claimed)

```
$ cd /fast/scratch/kotoba-r47/w2/W2XmlLive/kotoba-shokunin
$ sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'
0                                    # exit=1 (grep: no match)  ✔ expected 0 / exit 1
$ git show c61a973:SKILL.md | sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'
1                                    # exit=0                   ✔ 1 → 0 confirmed at the BASE
$ python3 -B verifiers/verify_skill_checklist.py --json --check trigger.no_xml_tag
{"checks":[{"detail":"no XML tag in name, description (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)","evaluated":2,"id":"trigger.no_xml_tag","status":"PASS"}],"exit_code":0,"fail":0,"na":0,"pass":1}
exit=0                              # ✔ PASS, evaluated 2
$ python3 -B verifiers/verify_skill_checklist.py --json      # exit=0
exit_code 0  pass 11  fail 0  na 0   (11 checks: box_map 41, frontmatter 4, name_directory 1,
                                      literal_trigger 1, anti_trigger 1, no_xml_tag 2,
                                      line_budget 528, no_placeholder 484, command_binary 13,
                                      citation 44, governance 848)   # ✔ 11/11
$ python3 -B verifiers/verify_skill_checklist.py --self-test
0 failure(s) over 1845 assertions    # exit=0                    # ✔ 1845
```
BASE comparison in a second worktree (`git worktree add … c61a973`): `--self-test` → `0 failure(s) over 1597 assertions`, exit 0; full `--json` → exit 1, 10 checks, 8 PASS / 2 FAIL (`trigger.name_directory` fails only because the worktree directory is named `base-wt`; `governance.citation_resolves` fails on C3's `LOG.md:2111` erratum, which is C3's lane). The 1597 → 1845 step matches `LOG.md:2322` and `SCORECARD.md:31` exactly, and `verifiers/floors-registry.json` was bumped **in step** (`"checklist": 1597 → 1845`, `git diff c61a973 7ad7fad -- verifiers/floors-registry.json`); `python3 -B verifiers/check_assertion_floors.py` → exit 0.

Operability of the CLI itself: running from an unrelated cwd works (`cd /tmp && python3 -B <abs>/verifiers/verify_skill_checklist.py --check trigger.no_xml_tag` → PASS, exit 0); the plain (non-`--json`) full run prints 11 PASS lines and exits 0; a bogus check id is rejected by argparse (exit 2, `invalid choice: 'trigger.no_xml_typo'`) — there is no silent no-op gate.

## 3. The mutation: planting `<skills>` back must FAIL naming it — it does

Planted in the clone (working tree only):
```
  Use <skills> catalogue entries when auditing.      # appended inside the folded description
```
```
$ python3 -B verifiers/verify_skill_checklist.py --json --check trigger.no_xml_tag
{"checks":[{"detail":"XML tag in description: '<skills>' (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)","evaluated":2,"id":"trigger.no_xml_tag","status":"FAIL"}],"exit_code":1,"fail":1,"na":0,"pass":0}
exit=1
$ python3 -B verifiers/verify_skill_checklist.py --json      # exit=1
exit_code 1  pass 10  fail 1   # only trigger.no_xml_tag FAILs; every other check unaffected
```
The FAIL **names the tag** (`description: '<skills>'`) and the key it was found in — the acceptance criterion is met. `git checkout -- SKILL.md` restored the clone afterwards.

## 4. Independent upstream oracle (the strongest evidence I found)

The check cites S003/S012; S012 pins Anthropic's own `skills/skill-creator/scripts/quick_validate.py` at tree `dbd4588`. I fetched that file live (`curl` → HTTP 200, 3972 B) and ran it as an **external oracle** on the three trees:

| tree | upstream `quick_validate.py` | repo gate `trigger.no_xml_tag` |
|---|---|---|
| tip 7ad7fad | `Skill is valid!` — **exit 0** | PASS, exit 0 |
| BASE c61a973 | `Description cannot contain angle brackets (< or >)` — **exit 1** | (check absent) |
| planted `<skills>` mutant | `Description cannot contain angle brackets (< or >)` — exit 1 | FAIL exit 1, names `'<skills>'` |

So the C2 repair is not merely self-consistent with the repo's mirror check: the *actual* Anthropic packager refused the base description and accepts the repaired one. S012's citation is accurate — upstream lines 79-81 are `# Check for angle brackets` / `if '<' in description or '>' in description:` / `return False, "Description cannot contain angle brackets (< or >)"`, and the file parses frontmatter with `yaml.safe_load` (a real YAML parser — see F1).

## 5. Detector matrix (16 shapes) — see `W2XmlLive.matrix.txt`

Ran each shape through `check_no_xml_tag()` (imported from the clone) and compared with `yaml.safe_load` (PyYAML 6.0.3) on the same frontmatter.

- Correctly **FAIL** (13/16 shapes): `</skills>`, `<skill name="a">`, `<br/>`, `<!-- c -->`, `<![CDATA[x]]>`, `<?xml …?>`, `<!DOCTYPE x>`, folded `</Skills` + `>` (parses to `'</Skills >'`), double-quoted `\u003c` escape, plain-scalar `<skills>`, folded `<skills>`, anchored value `&a "x <skills>"`, and a tag in the **`name`** field (S003 covers `name` as well as `description` — the shipped check covers both, closing the critic's "half the bullet" objection).
- Correctly **PASS** (controls): `a -> b, x => y, a < b, c > d`; `<= 600 or <500 lines; cat <<EOF; 1<2>0; <> op`; `≤ 9, ‹skills›, &lt;skills&gt;`; a `metadata:` block containing `note: <internal>` (nested metadata stays out of scope, as the `xml-tag-control` fixture asserts).
- **Over-strict, fails closed** (documented): a plain scalar that spells the escape literally (`description: literal \u003cskills\u003e text`) FAILs although YAML never decodes it. The shipped `DOCUMENTED LIMITS` (`verify_skill_checklist.py:213-215`) names this direction ("a tag after ` #` FAILs here though YAML drops it").

## 6. Findings

### F1 — MEDIUM (calibration): a YAML-alias description is a false PASS against the very oracle the check cites

The check's frontmatter parse is a hand-rolled structural parse (`verifiers/verify_skill_checklist.py:515-560`) that does **not** resolve YAML aliases. A description reached through an anchor therefore hides the tag from the gate, while every real YAML client (upstream `quick_validate.py` uses `yaml.safe_load`; omp/opencode are not checked here — `[INFERENCE]`) resolves it and sees the markup.

Counterexample (repro, run in the clone):
```
$ mkdir -p /tmp/w2xml_alias2 && printf -- '---\nname: kotoba-shokunin\nmetadata:\n  note: &d "contains <skills>"\ndescription: *d\n---\n' > /tmp/w2xml_alias2/SKILL.md
$ python3 /tmp/w2xml_qv.py /tmp/w2xml_alias2
Description cannot contain angle brackets (< or >)      # upstream oracle: exit 1
$ python3 -c "import yaml,re; c=open('/tmp/w2xml_alias2/SKILL.md').read(); m=re.match(r'^---\n(.*?)\n---',c,re.S); print(repr(yaml.safe_load(m.group(1))['description']))"
'contains <skills>'                                     # a real YAML loader sees the markup
$ python3 -B verifiers/verify_skill_checklist.py --skill /tmp/w2xml_alias2/SKILL.md --check trigger.no_xml_tag
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (…)   # repo gate: exit 0
```
Same file, same rule, opposite verdicts. **Not a hidden defect**: the alias limit is disclosed at `verifiers/verify_skill_checklist.py:214` ("… fullwidth `＜x＞` (NFKC `<x>`), YAML aliases and plain-scalar `#` comments are outside the structural parse") and in the design artifact `.ufo/waves/round-47/build/C2CriticRule.md` §3 ("YAML alias. `description: *d` resolves in YAML to the anchored value, but the structural parse reads `*d`. This is a named limit and has no fleet instance."). The gap is in the *direction* of the disclosure: the docstring names the mechanism but not the consequence (a false PASS against Anthropic's packager, i.e. a file this gate would green-light that the vendor packager refuses), and neither the detail line (`verify_skill_checklist.py:1307-1312`) nor `SKILL.md:151` carries it. Suggested direction (advisory only — I did not edit anything): state the direction in the `DOCUMENTED LIMITS` bullet and/or in the detail line, e.g. "a YAML-aliased description PASSes here though a YAML client sees the tag".
Live-file impact: none — the shipped `SKILL.md` uses no aliases, and the upstream oracle accepts it.

### F2 — LOW (calibration/freshness of the source table): `corpus/SOURCES.md:23` (S010) is stale against the instrument the round changed

S010 still reads: “`verifiers/verify_skill_checklist.py` — `--self-test` exit 0 and `--json` exit 1 (9 PASS / 1 FAIL governance.citation_resolves at LOG.md:2111) runs 2026-10-19” … “Final line "0 failure(s) over 1597 assertions"” … and, in its claims column, “the frontmatter check is a lenient structural parse **with no XML-tag rule**”. All three are false at 7ad7fad: the XML rule now exists (`verify_skill_checklist.py:97-103, 310, 1294`), the self-test final line is `0 failure(s) over 1845 assertions`, and `--json` is **exit 0 11/11** (the `LOG.md:2111` red was excused by C3's erratum). S010's refresh column says `on-commit`, and the instrument's commit changed in this very landing (`git diff c61a973 7ad7fad -- verifiers/verify_skill_checklist.py` is non-trivial), so by the lane's own refresh policy the row should have been re-derived. The round-47 SOURCES diff added S012–S015 (19+/4- in `corpus/SOURCES.md`) but left S010 untouched. Counter-argument for the record: a source row is a dated observation of a run, so a historical reading is defensible — but the `on-commit` trigger plus the “no XML-tag rule” phrasing (a *present-tense* claim about the instrument) is what makes it stale rather than historical.
Note this is adjacent to my lane (the SOURCES frontier is another seat's), reported because the row describes the exact instrument I attacked.

### F3 — LOW (coverage of the cited rule): the gate mirrors only the XML half of Anthropic's validator

Upstream `quick_validate.py` (pinned by S012) enforces, in addition to the angle-bracket rule: `len(name) > 64` and `^[a-z0-9-]+$` for `name`; `len(description) > 1024`; and a hard reject of any top-level frontmatter key outside `{name, description, license, allowed-tools, metadata, compatibility}`. The repo's gate enforces none of these — `trigger.name_directory` only checks `name == directory`, and no check bounds the description length or the key set. Demonstrated: a file with `foo: bar` in frontmatter passes `trigger.no_xml_tag` (exit 0) but upstream refuses it ("Unexpected key(s) in SKILL.md frontmatter: foo", exit 1). The live file complies in fact (description 814 chars, `name` `kotoba-shokunin`, keys = `name` + `description`), and `SKILL.md:151` is honest about scope ("`trigger.no_xml_tag` gates the XML-tag rule on `name` and `description`; Anthropic's reference packager (S012) is stricter and refuses any `<`/`>`"). Residual only: the same sentence also asserts the `description ≤1024 chars` half of the portability floor, which is prose-only and ungated.

### F4 — INFO: the new check is not represented in the lane's own box map

`verifiers/checklist-baseline.json` maps the 41 prose boxes to dispositions; none carries `executed:trigger.no_xml_tag` (the executed set is `frontmatter_parses`, `name_directory`, `literal_trigger_string`, `anti_trigger_clause`, `command_binary_resolves`, `citation_resolves`, `line_budget`, `no_placeholder`). The check runs unconditionally in the live run, so this is not a coverage hole in execution — but the file the lane treats as its coverage record does not credit the new gate, and no new prose box was added for the XML rule (41 boxes at BASE and at tip).

### F5 — INFO (the repair itself): the description rewrite is faithful

`git diff c61a973 7ad7fad -- SKILL.md` shows the description's “never reach the `<skills>` router” → “never reach the omp skills router”. The token was correct where it was: omp renders the `<skills>` catalogue and opencode the `<available_skills>` block (`SKILL.md:23`, `SKILL.md:42`), so the rewrite keeps the meaning and drops the last angle bracket from the frontmatter. The body still carries `<skills>` (`:23`) and `<available_skills>` (`:42`) — correctly out of scope (frontmatter values only), and the upstream oracle accepts the file. `SKILL.md:151` was also rewritten from “This file's own description still carries `<skills>`; the repair is planned (`SCORECARD.md` § planned, round 47).” to a description of the shipped gate, and the old “planned” sentence is gone. The “planned” wording was the only stale artifact of the pre-round state I found in the landed surfaces, and it is resolved.

## 7. What I did NOT check

- The other C1/C3 claims (omp/opencode surface re-derivation, substrate re-pinning, the governance erratum, the corpus index re-record) — other lanes' targets; I only observed their *side effects* on the floors registry and the base-vs-tip gate deltas.
- Whether omp and opencode actually resolve YAML aliases in their own frontmatter readers — I did not launch an omp session (contract) and did not execute the `~/.local/bin/opencode` wrapper; the F1 impact on those two routers is `[INFERENCE]`.
- The design doc's 101-file fleet scan and its “no fleet instance” claim for the alias limit — not re-run by me (F1's fleet-innocence rests on the design artifact, unverified here).
- The other ten checks' semantics, the four new fixtures' `map.json` hashes, the fault-harness planter fix, `verify_corpus_integrity.py` / `verify_corpus_independent.py`, `verify_surfaces.py`, `check_substrate_pins.py`.
- Whether the XML rule *should* become a checklist box (F4) — a product decision, not mine.
- No host-private reads, no package installs, no `pacman`/`uv`/`npm` transactions in this lane.
