verdict: PARTIAL — the sanctioned `<skills>` → `omp skills router` frontmatter edit survives every
attack (byte-identical trigger/anti-trigger blocks, 815/1024 chars, yaml.safe_load-clean, the four
named checks PASS for identical reasons before/after), but the same landing left a stale
self-description of its own instrument in the same file (`SKILL.md:122` says "10 checks"; the
instrument now has 11) and left an append-only lesson row asserting the very token this round
removed.

# W2XmlTriggers — round-47 falsify, wave 2: `SKILL.md` frontmatter / trigger fidelity

- Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`, target `SKILL.md` frontmatter.
- Landed commit under attack: `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`; BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
- Scratch clone (canonical layout, detached at the landing): `/fast/scratch/kotoba-r47/w2/W2XmlTriggers/kotoba-shokunin`
  (`git clone --no-hardlinks` from the lane repo, `checkout --detach 7ad7fad`). Lane repo, its git
  index/refs and jj state were not touched; no `git add/commit/checkout` was run in the lane repo.
- Artifacts: `W2XmlTriggers.diff.txt` (base→tip diff of `SKILL.md` + `verifiers/verify_skill_checklist.py`),
  `W2XmlTriggers.mutation-battery.txt` (24-case tag battery + structural-vs-`yaml.safe_load` divergence scan).
- Tools installed/updated: **none** (no pacman/uv/npm/cargo transaction was needed or performed).

---

## F1 — MEDIUM — `SKILL.md:122` "**10 checks**" is stale at the landing commit; the instrument has 11

`SKILL.md:121-125` (at `7ad7fad`) describes its own gate:

```
121 `python3 verifiers/verify_skill_checklist.py` executes this file's own checklist:
122 **10 checks** (`checklist.box_map_complete` + the eight boxes marked
123 `(executed: …)` below + `governance.citation_resolves` over the two root
124 governance files), each fail-closed on fixtures, `evaluated N` per check,
125 exit 0/1/2/3 (`3` = box map missing, unparseable, or bound elsewhere).
```

Round 47 added `trigger.no_xml_tag` to `CHECK_IDS` (`verifiers/verify_skill_checklist.py:310`).
The count went 10 → 11, and the sentence was **not** updated. The sentence's own formula still
yields 10 (`box_map_complete` 1 + eight executed boxes + `governance.citation_resolves` 1) because
the eleventh check is executed by the default gate yet is **not** one of "the eight boxes marked
`(executed: …)`" — `verifiers/checklist-baseline.json` binds no box to it (41 boxes, 8 executed,
`trigger.01/02/03/04/09/11/14/15`; no `trigger.no_xml_tag` row), so the prose cannot be repaired by
re-counting the map.

This is a self-contradiction inside the landing: the same round's ledger says 11.

```
$ cd /home/vgpnk/Projects/shokunin/kotoba-shokunin
$ git show c61a973:verifiers/verify_skill_checklist.py | sed -n '/^CHECK_IDS = (/,/^)/p' | grep -c '"'
10
$ sed -n '/^CHECK_IDS = (/,/^)/p' verifiers/verify_skill_checklist.py | grep -c '"'
11
$ python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json > /tmp/chk.json; echo exit $?
exit 0
$ python3 -c "import json;d=json.load(open('/tmp/chk.json'));print('checks',len(d['checks']),'pass',d['pass'],'fail',d['fail'])"
checks 11 pass 11 fail 0
$ grep -n "10 checks" SKILL.md
122:**10 checks** (`checklist.box_map_complete` + the eight boxes marked
$ grep -n "11/11" LOG.md SCORECARD.md
LOG.md:2323:… Checklist `--json` exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (C2's check included) …
SCORECARD.md:33:… `python3 -B verifiers/verify_skill_checklist.py --json` exit 1, 9/1 → exit 0, 11/11 (C2's check included) …
```

So `SKILL.md` (10) contradicts `LOG.md:2323` and `SCORECARD.md:33` (11) **inside the same landing
commit**, and the default gate executes the eleventh check unconditionally (the no-`--check`
invocation prints 11 result lines, exit 0).

No instrument catches it: `trigger.citation_resolves` resolves path-shaped tokens, not counts;
`checklist.box_map_complete` maps boxes → dispositions, not prose numbers. The defect is silent.

**Suggested repair (one line, no new content):** `SKILL.md:122-123` → "**11 checks**
(`checklist.box_map_complete` + the eight boxes marked `(executed: …)` below + `trigger.no_xml_tag`
+ `governance.citation_resolves` over the two root governance files)".

Severity: MEDIUM, not HIGH — it is a self-description, not the gate itself; the gate is correct and
runs 11 checks. It is squarely a calibration defect for this lane (the file describes its own
instrument), and it is *new at this landing* (the sentence was accurate at BASE).

**Not checked:** whether `corpus/knowledge/checklist-execution-round1{5,6,7}.md` (historical
round files, which say "8 checks" / "ninth check") were meant to be refreshed; they are
round-scoped records and I did not treat them as in-scope.

---

## F2 — LOW — `corpus/lessons/round-46.md:31` (M13) is false at the landing tree and round 47's erratum row does not say so

`corpus/lessons/round-46.md:31` asserts, in the present tense:

> `SKILL.md:15` description carries the literal `<skills>` token (peer-reported rule, not re-opened here; **presence measured only**)

At `7ad7fad` that is false: the token is gone (this round removed it), and the pointer was already
off by one line at BASE (the token sat on `:14`).

```
$ sed -n '15p' SKILL.md
  router-visible.
$ sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'; echo exit $?
0
exit 1
$ grep -n "SKILL.md:15" corpus/lessons/round-46.md
31:| M13 Structural frontmatter gate mistaken for semantic | … `SKILL.md:15` description carries the literal `<skills>` token (peer-reported rule, not re-opened here; presence measured only) | none → Q08 | …
```

Round 47's own erratum row for exactly this defect class — `corpus/lessons/round-47.md`, row **M22
"A lesson's own evidence pointers stale at landing"** — frames the drift only as a *line-number*
drift:

> M13 cites `SKILL.md:15`, the token sat on `:14` (`.ufo/waves/round-47/build/MistakeSweepOthers.md` N1–N3) | none (`governance.citation_resolves` resolves path tokens in LOG/SCORECARD only, never `file:line` content) | Not fixed by an instrument this round. The round-46 lesson stays append-only; this row is its erratum.

It does not record that **round 47's own C2 repair deleted the token the row asserts is present**,
so a reader who re-runs M13's "presence measured only" command against the landed tree gets zero
matches against a row that says the token is carried. The append-only rule means the false
present-tense claim survives unless the erratum row says so.

**Suggested repair (one clause in the M22 row):** add "and the token itself was removed at this
round's landing (`SKILL.md` frontmatter `<skills>` count 1 → 0), so M13's present-tense
'presence measured only' no longer holds at `7ad7fad`".

Severity: LOW (a historical lesson row, explicitly scoped as a record), but it is in this lane's
own claim surface (the frontmatter description) and it is the exact drift class the round claims
to have catalogued.

---

## F3 — LOW (cross-lane, informational) — `LOG.md:2323` "governance evaluated 804" does not reproduce at the landing commit

The round-47 C3 row reports the checklist's governance arm as "evaluated 804". At `7ad7fad` the
same arm reports 848 — the entry's own append (and the lines after it) changed the token count it
reports, so the cited measurement is not reproducible at the commit that cites it.

```
$ python3 - <<'EOF'
import importlib.util
from pathlib import Path
spec=importlib.util.spec_from_file_location("vsc","verifiers/verify_skill_checklist.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print(m.check_governance_citations(Path(".")))
EOF
('PASS', 848, '848 governance citation token(s) resolve across 2 files; 9 quoted meta-finding(s), 3 schematic token(s) excluded, 1 recorded absence(s) excused')
$ grep -n "governance evaluated 804" LOG.md
2323:… → exit 0, 11/11 (governance evaluated 804, 1 recorded absence excused) …
```

This is C3's lane, not mine; I record it because I ran the check. Also noted from
`.ufo/waves/round-47/after/SUMMARY.md`: the after-battery line `harness claims exit=1` (a red
`verifiers/verify_harness_claims.py`) — the round's own "Not claimed" paragraph in `LOG.md:2326`
declares it out of scope ("21/28 before and after … Q09 debt"), which is consistent, but the red
gate is on the landing tree.

---

## F4 — NIT (pre-existing, surfaced by the round-47 edit of the same sentence) — the `description ≤1024 chars` half of the portability floor has no instrument

`SKILL.md:151` (the sentence round 47 rewrote) states the portability floor:

> Portability floor (spec + vendor + YAML, `corpus/SOURCES.md` S001, S002, S003, S008): `name` ≤64 lowercase-hyphen chars equal to the directory; `description` ≤1024 chars, no XML tags (Anthropic rule), quoted when it holds `: ` or ` #` (illegal in a YAML plain scalar — lenient loaders hide it, strict ones reject). `verifiers/verify_skill_checklist.py` `trigger.no_xml_tag` gates the XML-tag rule on `name` and `description`; Anthropic's reference packager (S012) is stricter and refuses any `<`/`>`.

Round 47 gave the XML half a gate; the length half and the quoting half still have none:

```
$ grep -rn "1024" verifiers/*.py
(no output)
$ grep -c '"description' verifiers/verify_skill_checklist.py   # length/quoting checks
0
```

The value complies today (815 chars, base 815), and `corpus/SOURCES.md:14` (S001) sources the
bound ("description 1-1024 chars"). Not a round-47 regression; recorded because the round edited
this exact sentence and left the sibling rule ungated.

---

## F5 — NIT (pre-existing) — the file's own 600-line box deviates from S001's "under 500 lines", and the file is 528

`trigger.line_budget` PASSes for the **right reason** (verified below), but the threshold it binds
is the file's own box, not the spec bound the file cites 75 lines earlier:

- `SKILL.md:151` cites `corpus/SOURCES.md` S001; `corpus/SOURCES.md:14` (S001) states "SKILL.md **under 500 lines** with detail moved to reference files".
- `SKILL.md:246` is the file's own box: "File ≤ 600 lines; overflow already moved to referenced depth files." — the file is **528** lines.
- The deviation is disclosed at `SKILL.md:176` ("the **~600-line module bound** (round 15 applies it to this file — § Trigger-fidelity checklist, line-budget box)").

Pre-existing (the base file is 525 lines, also over 500). The check binds the box by design
(`verifiers/verify_skill_checklist.py:105-107` docstring: "the box binds the threshold … A box
saying ~450 while the flag says 600 fails at 451 — the file's own text is the contract"), so the
PASS is earned. I record it as a disclosed deviation, not a defect.

---

## Findings that SURVIVED the attack (positive, recorded so the integrator can rely on them)

### S1 — the frontmatter diff is exactly the sanctioned substitution, and nothing else

```
$ git diff c61a973 7ad7fad -- SKILL.md
-  never reach the `<skills>` router — craft here is audit-side, not
+  never reach the omp skills router — craft here is audit-side, not
```

Character-level diff of the *parsed* description (`yaml.safe_load` of the frontmatter block at both
revisions):

```
len B 815 len T 815
replace B[749:759]='`<skills>`' -> T[749:759]='omp skills'
```

Exactly one 10-char → 10-char replacement; the byte count is preserved (815 both sides, 814 after
`.strip()`), i.e. the edit is length-neutral, not a truncation. Raw `cat -A` comparison of
`SKILL.md:1-16` shows only that one line differing; `git diff 7ad7fad -- SKILL.md` is empty, so all
line numbers cited in this report are at the landing commit.

### S2 — every trigger / anti-trigger phrase is byte-identical

```
Triggers     identical=True sha_b=f0c397ccd701e956 sha_t=f0c397ccd701e956
Anti-triggers identical=True sha_b=1818a0dfc9a1da76 sha_t=1818a0dfc9a1da76
Sibling      identical=True sha_b=58791183d82df4bb sha_t=58791183d82df4bb
```

Quoted/backticked span inventory: base 10 spans, tip 9 spans; the **only** removed span is
`` `<skills>` ``; the remaining 9 are byte-identical and in the same order (`removed: ['<skills>']`,
`added: []`). The eight trigger phrases ("skill file", "SKILL.md", "frontmatter description",
"trigger words", "prompt craft", "write a skill", "audit this skill", "skill quality") and the
anti-trigger clause are untouched.

### S3 — length, YAML validity, and the stricter S012 rule all hold

- `description` = **815** chars (814 stripped) ≤ 1024 (S001-sourced).
- `yaml.safe_load` parses the frontmatter block cleanly at both revisions; keys are exactly
  `['name', 'description']`; `name` = `'kotoba-shokunin'` at both.
- **Zero** `<` and zero `>` characters remain in the tip description (base had `<` at offset 750 and
  `>` at 757). So the new description satisfies even the *stricter* S012 rule ("Anthropic's
  packager refuses any `<` or `>` in `description`", `corpus/SOURCES.md:25`), which the instrument
  itself does **not** enforce (it only flags `<`-initiated markup). The repair is therefore
  stronger than the gate that motivated it.

### S4 — the four named checks PASS for the *same* reasons before and after (right-reason test)

Running the **round-47** instrument against the **BASE** file (canonical-layout scratch clone,
`git show c61a973:SKILL.md > SKILL.md`):

```
$ python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md"
PASS checklist.box_map_complete: evaluated 41 — 41 boxes mapped (8 executed, 0 delegated, 33 unexecuted)
PASS trigger.frontmatter_parses: evaluated 4 — frontmatter parses: name='kotoba-shokunin', description 814 chars
PASS trigger.name_directory: evaluated 1 — name 'kotoba-shokunin' == directory 'kotoba-shokunin'
PASS trigger.literal_trigger_string: evaluated 1 — description carries literal 'Triggers:'
PASS trigger.anti_trigger_clause: evaluated 1 — exclusion marker 'Anti-triggers' present (vocabulary test, not semantics: …)
FAIL trigger.no_xml_tag: evaluated 2 — XML tag in description: '<skills>' (S003 Anthropic rule, absent from the open spec (S001); Anthropic's packager bans any '<'/'>' and is stricter)
PASS trigger.line_budget: evaluated 525 — 525 lines within budget 600 (from box at line 246)
PASS trigger.no_placeholder: evaluated 481 — no placeholder markers in 481 scanned lines
PASS trigger.command_binary_resolves: evaluated 13 — 9 segments; 13 command subject(s) resolve
PASS trigger.citation_resolves: evaluated 41 — 41 repo-rooted citation token(s) resolve from the repo root
PASS governance.citation_resolves: evaluated 848 — 848 governance citation token(s) resolve across 2 files; …
=== EXIT 1 ===
```

and against the **TIP** file (scratch clone restored to `7ad7fad`):

```
$ python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md"
… all 11 PASS …
PASS trigger.no_xml_tag: evaluated 2 — no XML tag in name, description (S003 Anthropic rule, …)
PASS trigger.line_budget: evaluated 528 — 528 lines within budget 600 (from box at line 246)
=== EXIT 0 ===
```

Right-reason detail, check by check:

- **`trigger.name_directory`** — PASS on the identity `name == basename(dirname(abspath(skill)))`,
  not on a fallback: the instrument resolves the *invoked* path, so the scratch clone's directory
  name (`kotoba-shokunin`) is what it compares, and it matches. The base file passed the same way
  (the name is not part of the diff).
- **`trigger.literal_trigger_string`** — PASS on the **literal `Triggers:`** branch
  (`verifiers/verify_skill_checklist.py:1262` tests `"Triggers:" in desc` *before* the quoted
  -span fallback), i.e. on the explicit list, not on the accidental quoted spans. Identical reason
  at BASE.
- **`trigger.anti_trigger_clause`** — PASS on the marker **`'Anti-triggers'`**
  (`ANTI_TRIGGER_RE`, `verifiers/verify_skill_checklist.py:390-394`), matched at the earliest
  position in the description; the quoted/backticked spans are stripped first
  (`ALL_QUOTED_SPANS_RE`), so the removal of the `` `<skills>` `` code-span does not change which
  marker fires. Identical reason at BASE. (Note, disclosed by the check itself: the description also
  contains "never", so the check would pass even without the exclusion clause — the instrument names
  this vacuity in its own detail line.)
- **`trigger.line_budget`** — PASS on the **file's own box**, not on the `--max-lines` default:
  `box_line_budget` finds the *first* box matching `LINE_BOUND_BOX_RE`
  (`verifiers/verify_skill_checklist.py:410-411`), and I enumerated every matching box in the file:

  ```
  boxes: 41
  LINE_BOUND_BOX_RE matches: 1
    line 246 limit 600 text: File ≤ 600 lines; overflow already moved to referenced depth files. (executed: `trigger.li…
  ```

  Exactly one match in the whole file (line 246, limit 600); 528 ≤ 600. The count is
  `len(text.splitlines())` = 528 = `wc -l SKILL.md` = 528, so no off-by-one at EOF.

### S5 — the new gate is non-vacuous and discriminating (24-case battery)

Full output: `W2XmlTriggers.mutation-battery.txt`. Selected rows (each is a *mutated copy* of the
description under `/tmp/falsify*/<case>/kotoba-shokunin/SKILL.md`, run through
`verify_skill_checklist.py --check trigger.no_xml_tag`):

| case | exit | verdict |
|---|---|---|
| as landed | 0 | PASS (no XML tag in name, description) |
| `` `<skills>` `` code-span restored | 1 | FAIL — XML tag in description: `'<skills>'` (backticks are **not** exempt) |
| folded-split `</Skills\n  >` | 1 | FAIL — XML tag in description: `'<skills >'` |
| literal block `|` + `<skills>` | 1 | FAIL |
| literal block, tag split across lines | 1 | FAIL |
| double-quoted `\u003cskills\u003e` | 1 | FAIL — YAML angle escape `'\u003c'` |
| single-quoted `<skills>` | 1 | FAIL |
| plain scalar `<skills>` | 1 | FAIL |
| plain multi-line scalar with `<skills>` | 1 | FAIL |
| tag in `name` | 1 | FAIL — XML tag in name |
| HTML comment `<!-- x -->` | 1 | FAIL |
| PI + doctype `<?xml v?> <!DOCTYPE x>` | 1 | FAIL |
| `a < b` (comparison) | 0 | PASS (correct — not a tag) |
| `a -> b` (arrow, no `<`) | 0 | PASS (S012 gap, disclosed in DOCUMENTED LIMITS) |
| `&lt;skills&gt;` (entity) | 0 | PASS (no literal `<`/`>`) |
| `< skills` (space after `<`) | 0 | PASS (not well-formed XML) |
| tag inside `metadata:` | 0 | PASS (out of scope by design; `when_to_use` gap is disclosed) |
| empty `description:` | 1 | FAIL — cannot evaluate: empty description (evaluated 0) |

Two structural-vs-`yaml.safe_load` divergences worth noting, neither of which changes a verdict in
the battery: the instrument's structural parser **folds** a more-indented block-scalar line that
YAML keeps literal (`m21_indent_more`: structural `"para one <skills> para two"` vs YAML
`"para one\n  <skills>\npara two\n"`) — both sides carry the tag, so the check fires either way;
and trailing newlines differ (structural parser strips them). I probed ten such shapes; the tag
verdict agreed in all ten.

### S6 — the frontmatter's own router-visibility claim still holds after the edit

The edited sentence is a factual claim about the loader ("the shokunin files are not in an omp
skill discovery root, so their descriptions never reach the omp skills router"). I verified it
against the live host:

```
$ ls ~/.agents/skills/            # create-toolset godspeed omarchy reverse-engineer-anything shokunin swarm tower ufo unreal-mcp unreal-skill
$ ls ~/.omp/agent/skills/         # No such file or directory
$ ls ~/.claude/skills/            # omarchy, synced
$ find /home/vgpnk/Projects/ompskills -maxdepth 4 -name "kotoba*"
(no output)
$ grep -rl "kotoba-shokunin" ~/.agents/skills ~/.claude/skills /home/vgpnk/Projects/ompskills/.omp/skills
(no output)
$ find /home/vgpnk/Projects/shokunin/.omp -maxdepth 3
/home/vgpnk/Projects/shokunin/.omp
/home/vgpnk/Projects/shokunin/.omp/agents
/home/vgpnk/Projects/shokunin/.omp/agents/executor.md
```

No router-visible copy of `kotoba-shokunin` exists on this host, so the description's
router-visibility claim is true and the edit does not create or destroy a routed surface. The
paraphrase "omp skills router" is faithful to the substrate: the omp 18.12.5 ELF template's
catalogue tag is `<skills>` (`grep -n "<skills>" /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings`
→ line 2423496), which the SKILL.md body still names as such (`SKILL.md:91`) — the frontmatter now
uses prose where the body uses the literal tag, which is the intended asymmetry. (Terminology nit,
not a finding: the body calls the same artefact the "`<skills>` **catalogue**", the frontmatter the
"omp skills **router**"; both terms already appear in the file.)

### S7 — the round's own counting command reproduces

```
$ git show c61a973:SKILL.md | sed -n '/^---$/,/^---$/p' | grep -c '<skills>'; echo exit $?
1
exit 0
$ sed -n '/^---$/,/^---$/p' SKILL.md | grep -c '<skills>'; echo exit $?
0
exit 1
```

matches `SCORECARD.md:31` and `.ufo/waves/round-47/after/SUMMARY.md` ("frontmatter <skills> count: 0
(grep exit 1)"). The sed range is unambiguous — `SKILL.md` has exactly two `^---$` lines (1 and 16).

---

## What I did NOT check

- **C1 lanes** (omp 18.12.5 / opencode 1.19.3 re-derivation and re-pinning, `verifiers/verify_surfaces.py`,
  `verifiers/check_substrate_pins.py`, `verifiers/surfaces-baseline.json`, the § B′ census rows) — out of
  my target; I only confirmed the substrate snapshot exists and that `<skills>` is present in the frozen
  omp strings dump.
- **C3 lane** (`GOVERNANCE_ERRATA` mechanics for `LOG.md:2111`, the corpus index rows, `corpus-baseline.json`
  58→60, the fault-harness planter fix) — out of my target; I observed the `governance.citation_resolves`
  arm's evaluated count only (F3).
- The **corpus gates** (`verify_corpus_integrity.py`, `verify_corpus_independent.py`) and the **fault
  harness** (`verifiers/fault_injection_corpus.sh`): not run. My lane did not mutate committed corpus state.
- The **`--self-test` assertion battery internals**: I ran it whole
  (`python3 -B verifiers/verify_skill_checklist.py --self-test` → `0 failure(s) over 1845 assertions`,
  exit 0, matching `SCORECARD.md:31` and the ratcheted floor in
  `verifiers/check_assertion_floors.py`), but I did not independently re-derive the 1845 count, did not
  verify the floor registry entry `checklist: 1845` against the instrument's own output by mutating it,
  and did not audit the seven "detector mutants killed" claims in
  `.ufo/waves/round-47/build/C2CriticRule.md` (mutation of the detector itself is the
  `W2XmlMutants-2` lane's).
- The four `verifiers/fixtures/checklist/xml-tag-*/` fixtures: I read them and confirmed the self-test
  battery references them, and I re-derived their behaviour independently via my own battery (S5); I did
  not audit the fixtures' `map.json` box hashes against `checklist.box_map_complete` by hand.
- **opencode's** skill-catalogue side (`<available_skills>` full-description rendering) — the description
  edit is byte-visible to opencode's renderer, but kotoba-shokunin is not installed under any opencode
  root either; I did not re-derive opencode 1.19.3's loader.
- The **Anthropic `quick_validate.py`** source itself (S012's rule was taken from the corpus row
  `corpus/SOURCES.md:25`, whose quote is `"Description cannot contain angle brackets (< or >)"` at
  `skills/skill-creator/scripts/quick_validate.py:81`; I did not re-fetch the pinned commit
  `dbd4588f9e1033efb41dad4bef2f7947c8993d44`).
- Whether the **`skokunin` skill symlinked at `~/.agents/skills/shokunin`** (a *different* skill —
  `name: shokunin`, the mint/host-binding skill) should be disambiguated in the description's
  "the shokunin files" phrasing. The description's "shokunin files" could be read as the sibling
  `*-shokunin` domain skills it already enumerates; I did not rule out that a reader could misread it
  as the router-visible `shokunin` skill. Low, ambiguous, not changed by this round.

## Reproduction environment

All commands above ran from `/home/vgpnk/Projects/shokunin/kotoba-shokunin` (read-only) or from
the canonical-layout scratch clone `/fast/scratch/kotoba-r47/w2/W2XmlTriggers/kotoba-shokunin`
(detached at `7ad7fad`; mutated only there, and restored with `git checkout -- SKILL.md` after the
before/after gate run — `git status --short` clean afterwards). Python 3 stdlib only (`yaml`,
`hashlib`, `difflib`, `re`, `importlib`); the repo's own instrument was used unmodified.
