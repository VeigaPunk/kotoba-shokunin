verdict: PARTIAL — C1/C2/C3 gate values reproduce at 7ad7fad, but the landing's own records carry a dead forward citation (SCORECARD.md:32), a stale after-count (LOG.md:2323 "governance evaluated 804" vs 848), and an index row that overstates source re-open coverage (corpus/README.md:64 vs corpus/lessons/round-47.md:50); the first and third are classes M20–M22 do not name.

# Target and method

Landed tree `7ad7fadfc09354b74fb66605dfb0c1182c115a2f`, BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd`.
All runs were in canonical-layout clones (sibling symlinks to `/home/vgpnk/Projects/shokunin/*`,
lane repo cloned `--no-hardlinks`), because the gate suite resolves `../PROTOCOL.md` and the
governance check counts fleet-root citations:

- landing clone: `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2MistakeSweep-2/kotoba-shokunin` (detached 7ad7fad)
- BASE clone: `/fast/scratch/kotoba-r47/w2/KotobaR47-2.W2MistakeSweep-2/basecanon/kotoba-shokunin` (detached c61a973)
- hybrid/BASE-record clones and mutation copies under the same parent (`hybrid/`, `hybrid2/`, `preappend/`, `discrim/`, `errata/`, `errata2/`, `mut/`, `xmlmut/`)

The fleet root was read-only throughout; no `git add/commit/checkout` in it. Python 3.14.8.
Host was heavily loaded (254 live peer agents), so wall times are upper bounds.

Swept text: every changed line of `LOG.md` (2317–2326), `SCORECARD.md` (31, 32, 33, 106, 108),
`PROVINCE.md` (15, 22), `plans/round-47.md` (all), `corpus/lessons/round-47.md` (all),
`corpus/QUALITY.md` (30), `corpus/README.md` (63–64, 73), `corpus/SOURCES.md` (7–8, 25–28, 69–88),
the touched verifiers/baselines/fixtures, `before/SUMMARY.md`, `after/SUMMARY.md`.

Class axes scanned: (a) stale `path:line` citations in new LOG/SCORECARD text, (b) claims printed
without exit codes, (c) counting commands that cannot be re-run as written, (d) inherited-artifact
reuse without verification.

# Findings

## F1 — MEDIUM, new class (anticipatory citation): SCORECARD.md:32 cites a LOG entry that does not exist at the landing commit

`SCORECARD.md:32` (freshness row, new this round) ends its round-47 segment with:

> `... Measured on the round-47 landing tree (hash in the LOG.md round-47 landing-pin entry).`

At 7ad7fad there is no round-47 landing-pin entry. The round-47 entry itself defers it:

```
$ grep -n 'landing-pin\|landing pin' LOG.md
2312:## 2026-10-19 — Round 46 landing pin and after-battery      ← round 46 only
$ sed -n '2326p' LOG.md
- Not claimed: ... Falsification wave and landing pin follow in the next entry.
```

So the row's only pointer to the tree hash it claims to have been measured on is a prose
reference to an entry that is not in the record. `SCORECARD.md:106` compounds it: "verdict
detail in the LOG.md round-47 **entries**" — at 7ad7fad there is exactly one round-47 entry
(`LOG.md:2317`).

Why no gate catches it: `verifiers/verify_skill_checklist.py` `governance.citation_resolves`
resolves only path tokens (and only `LOG.md`/`SCORECARD.md` → repo paths); it never checks a
prose reference to a section title (documented limit, `verifiers/verify_skill_checklist.py:234-237`
"never ... content support, commit pins or line anchors"). This is an append-only record, so a
later "landing pin" entry may cure the pointer — at the attacked commit it is dead.

Repro:
```
$ cd <canonical clone at 7ad7fad>
$ grep -n 'round-47 landing-pin' SCORECARD.md   # 32
$ grep -c '^## .*Round 47' LOG.md               # 1 (the landing entry)
$ tail -2 LOG.md                                # "landing pin follow in the next entry"
```

## F2 — MEDIUM, M22 recurrence: LOG.md:2323 prints "governance evaluated 804"; the landing tree reports 848

`LOG.md:2323`:

> `Checklist --json exit 1, 9 PASS / 1 FAIL → exit 0, 11/11 (governance evaluated 804, 1 recorded absence excused); ...`

The same command at 7ad7fad:

```
$ python3 -B verifiers/verify_skill_checklist.py --json | jq -r '.checks[]|select(.id=="governance.citation_resolves")|"\(.status) \(.evaluated)"'
PASS 848
$ ... | jq '.pass,.fail'    # 11, 0 ; exit 0
```

804 is reproducible only with the **BASE records** under the **landing code**:

| tree (landing code = 7ad7fad verifiers) | governance `evaluated` | status |
|---|---|---|
| BASE `LOG.md` + BASE `SCORECARD.md` (`hybrid/`) | **804** | PASS |
| landing `LOG.md` + BASE `SCORECARD.md` (`hybrid2/`) | 837 | PASS |
| landing `LOG.md` + landing `SCORECARD.md` (7ad7fad) | **848** | PASS |
| BASE tree, BASE code (failing subject counted) | 805 | FAIL (LOG.md:2111) |

The value's likely origin is the C3 critic probe, which prints the same number against the BASE
gate: `.ufo/waves/round-47/build/C3CriticDesign.md:42` "Each of these single-line edits to
`LOG.md:2111` gives `PASS 804` under the BASE gate". The landing entry prints a pre-landing
experiment value as the after-run result, and the count necessarily grows when the entry itself
is appended (it adds 33 subjects; the new SCORECARD rows add 11).

This is the M22 class ("a lesson's own evidence pointers stale at landing") applied to a numeric
after-value, in the round that recorded M22 — and `corpus/lessons/round-47.md:53` claims the
wave-1 sweep "found no further class in this round's own work". The sweep was run at BASE; the
integrated text was never re-swept. Exact repro:
```
$ python3 -B verifiers/verify_skill_checklist.py --json  # at 7ad7fad: PASS 848
$ # in a throwaway clone: restore the BASE records under the same code
$ git show c61a973b:LOG.md > LOG.md && git show c61a973b:SCORECARD.md > SCORECARD.md
$ python3 -B verifiers/verify_skill_checklist.py --json  # (same code): PASS 804
```

## F3 — MEDIUM-LOW, new class (index row inflates re-open coverage): corpus/README.md:64

`corpus/README.md:64` (new index row):

> `... ## Gate (source rows S012–S015 with access records, S001–S008 re-opened, the C1 class ledger pointer)`

`corpus/lessons/round-47.md:49-50` says the opposite for two of those rows:

> `S002, S003, S004, S005, S008 still hold (SrcS002.md … SrcS008.md). S006, S007 not re-opened.`

S001 was re-opened (lesson § Gate), so the Gate's population is S001–S005 + S008 = 6 rows; the
index row claims 8. `ls .ufo/waves/round-47/build/SrcS006* SrcS007*` → no such files; the build
report list has `SrcS001,S002,S003,S004,S005,S008` only. The parenthetical `(SrcS002.md … SrcS008.md)`
is itself a range notation over non-contiguous files, which is what the index row appears to
have flattened. No gate compares an index row's prose against the lesson it summarizes.

Repro:
```
$ grep -n 'S001–S008' corpus/README.md                 # 64
$ grep -n 'S006, S007 not re-opened' corpus/lessons/round-47.md   # 50
$ ls .ufo/waves/round-47/build/SrcS00{6,7}* 2>&1       # no such file
```

## F4 — LOW, new minor class: the opencode fixture headers' provenance claim is false in every fixture

Every round-47 opencode fixture header says (e.g. `verifiers/fixtures/surfaces/strings-opencode-clean.txt:2-5`):

> `... Every non-comment line is an exact byte substring of /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings at the dump line named in its comment; no other binary text is committed.`

Measured against the frozen dump:
```
$ grep -c 'no-rule-anchor marker line' /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings
0   (exit 1)
$ grep -n 'no-rule-anchor marker line' verifiers/fixtures/surfaces/strings-opencode-clean.txt
28:no-rule-anchor marker line
$ grep -n 'H.up({targets:\["RULES.md"\]\|X.join(r.config,"opencode.json")' verifiers/fixtures/surfaces/strings-opencode-extra.txt
30:H.up({targets:["RULES.md"],start:S,stop:$})
31:X.join(r.config,"opencode.json")
```
All ten `strings-opencode-*.txt` fixtures carry the synthetic marker line; `extra.txt` adds two
more synthetic anchor-adjacent shapes, and `strings-opencode-planted-name.txt:9` plants a synthetic
`"GUIDE.md"` into the priority array. These controls are legitimate fixture design, but the header
says "no other binary text is committed", which a reader can only disprove by grepping the dump.
The omp 18.12.5 fixture has no such header; its synthetic decoy line
(`const q = Xl; var decoy = q(u, "evil", "EVIL.md");`) is disclosed in `verifiers/verify_surfaces.py:881`.
`strings-opencode-v2.0.26.txt:2-4` is honest ("No real binary excerpt is committed").

## F5 — MEDIUM, reproducibility: the printed `floors exit=0` is a timeout-margin flake

`after/SUMMARY.md:10` says `floors exit=0`; `LOG.md:2324` says "all 9 instruments at floor". One
default re-run at the landing tree did not reproduce it:

```
$ python3 -B verifiers/check_assertion_floors.py
PASS harness observed=10 floor=10
...
PASS pins observed=62 floor=62
FAIL harness_independent self-test timed out after 120s (hung?)
PASS compare_harness_independent observed=330 floor=330
PASS floors_guard observed=150 floor=150
exit=2      (wall 126.64 s)
$ python3 -B verifiers/verify_harness_independent.py --self-test
0 failure(s) over 104 assertions
exit=0      (wall 2 m 9.6 s = 129.6 s)
$ python3 -B verifiers/check_assertion_floors.py --self-test-timeout 300
... all nine PASS ... exit=0   (wall 109.17 s)
$ python3 -B verifiers/check_assertion_floors.py   # second default run
... all nine PASS ... exit=0   (wall 100.94 s)
```
The guard's timeout is 120 s (`verifiers/check_assertion_floors.py:129`, `SELF_TEST_TIMEOUT_S = 120`)
and the instrument alone measured 129.6 s under this host's load. The failure is intermittent
(1 of 2 default runs here), so the claim is true but not stably re-runnable as written; the guard
also reports "hung?" for what is a slow self-test. [INFERENCE] cause is host contention (254 live
agents), not a code regression: the relaxed-timeout run and the direct self-test both pass, and
the after-battery output (13:46–13:48, `.ufo/waves/round-47/after/check_assertion_floors.out`)
shows the same nine PASS lines.

## F6 — LOW, record-hygiene cluster

1. **Unpinned measurement note.** `verifiers/corpus-baseline.json:58` (`round47`) says
   "Measured ... on the round-47 integration tree" but names no commit/tree hash, unlike the
   `round46_landing` note that names the overlay clone. The values themselves reproduce at
   7ad7fad (`tracked_files` 60, `report_total` 40, `commit_total` 29, all defect counters 0,
   integrity 9/9 exit 0), so this is a re-anchoring gap, not a wrong number. The round's own
   Q19 (`corpus/QUALITY.md:30`) asks a recorded value to carry "its command and commit".
2. **Placeholder command in the before artifact.** `.ufo/waves/round-47/before/SUMMARY.md:4`
   prints `surfaces --opencode-binary <npx 1.19.3>: 4 PASS / 3 FAIL`; `<npx 1.19.3>` is not a
   runnable path. The actual invocation is only in `before/verify_surfaces.override-oc.json` and
   `before/exits.txt` (`surfaces-override exit=1`). The value itself reproduces (4 pass / 3 fail).
3. **Newline-less line hash.** The C3 erratum pins `LOG.md:2111` by
   `sha256("...line text...")` with no trailing newline (`verifiers/verify_skill_checklist.py:1519-1541`,
   `text.encode("utf-8")` on a `splitlines()` element). The natural verification
   `sed -n '2111p' LOG.md | sha256sum` returns `d7b4c628…`, not the pinned `7dcbf123…`; only
   `python3 -c '...splitlines()[2110]...'` reproduces it. The gate is internally consistent
   (I confirmed the pinned digest equals the newline-less hash), but the record does not print
   the command that yields it.
4. **Claims without exit codes** (all verified green by me, listed for the b-class sweep):
   `LOG.md:2322` "live check PASS 2 evaluated" and "`--self-test` 1597 → 1845 assertions, 0
   failures" (exit codes absent); `SCORECARD.md:31` same self-test claim; `SCORECARD.md:32`
   "self-test 87 → 99 assertions, 0 failures"; `SCORECARD.md:33` "in-place launderings, a restored
   runner, an appended copy and past-horizon rows all FAIL" (no per-arm exit codes). Exit codes
   are present for the gate-level claims in the same rows (checklist, integrity, independent,
   fault harness).

# What survived the attack (re-run, no defect found)

All commands at 7ad7fad in the canonical landing clone unless marked BASE.

| claim (source) | re-run | result |
|---|---|---|
| surfaces 7/7, exit 0 (`SCORECARD.md:32`, `LOG.md:2321`) | `python3 -B verifiers/verify_surfaces.py --json` | exit 0, pass 7 fail 0 |
| pins 3/3, exit 0 | `python3 -B verifiers/check_substrate_pins.py` | exit 0, `OK 3/3 pins hold`, sha `fdbc8136…`/`179ca421…` |
| checklist 11/11, exit 0 (`LOG.md:2323`) | `python3 -B verifiers/verify_skill_checklist.py --json` | exit 0, pass 11 fail 0 |
| corpus integrity 9/9 | `python3 -B verifiers/verify_corpus_integrity.py --json` | exit 0, tracked 60/report 40/commit 29, all defect counters 0 |
| corpus independent exit 0 | `python3 -B verifiers/verify_corpus_independent.py --json` | exit 0 |
| fault harness exit 0 ALL PASS | `bash verifiers/fault_injection_corpus.sh` | exit 0, `verdict: ALL PASS` (faults a,b,c,d1,d2,e fire; f blind-spot; g,h controls) |
| BASE checklist 9/1 exit 1 | BASE canonical clone | exit 1, pass 9 fail 1, governance FAIL 805 at `LOG.md:2111` |
| BASE surfaces exit 2 / pins exit 2 DRIFT 3/3 | BASE canonical clone | exit 2 / exit 2 `DRIFT 3/3 pins failed` |
| BASE corpus integrity 2 DRIFT / independent 1 DRIFT | BASE canonical clone | exit 1 (`tracked_files 59!=58`, `unindexed 1`) / exit 1 (`unindexed 1`) |
| discriminating cell: AFTER code × BASE baseline+census → exit 1 (`SCORECARD.md:32`) | landing clone with BASE `surfaces-baseline.json` + BASE census | exit 1, pass 6 fail 1 (`surfaces.opencode_extract` names `api-entries`, `project`, `read-hook`) |
| self-test 1597 → 1845 (`LOG.md:2322`) | `python3 -B verifiers/verify_skill_checklist.py --self-test` | exit 0, `0 failure(s) over 1845 assertions` |
| self-test 87 → 99 | `python3 -B verifiers/verify_surfaces.py --self-test` | exit 0, `0 failure(s) over 99 assertions` |
| floors surfaces 99 / checklist 1845, 9 instruments | `check_assertion_floors.py --self-test-timeout 300` | exit 0, nine exact-floor PASS lines |
| C2 `<skills>` 1 → 0 (`SCORECARD.md:31`) | `sed -n '/^---$/,/^---$/p' SKILL.md \| grep -c '<skills>'` at BASE / 7ad7fad | 1 (exit 0) / 0 (exit 1) |
| C2 live check PASS 2 evaluated | checklist JSON | `trigger.no_xml_tag PASS 2 no XML tag in name, description` |
| C2 planted tag fails | live edit `omp skills router` → `omp <skills> router` | checklist exit 1, `trigger.no_xml_tag FAIL 2 XML tag in description: '<skills>'` (10 pass/1 fail) |
| C2 arrow control passes | live edit → `omp -> skills router` | exit 0, 11 pass |
| seven detector mutants killed (`.ufo/waves/round-47/build/C2CriticRule.md:90`) | re-ran `mutate.sh` on a copy in my scratch | 7/7 exit 1, 1837-assertion prototype |
| mutant still killed on landed bytes | M1 (`ALL_QUOTED_SPANS_RE.sub`) applied to 7ad7fad `verify_skill_checklist.py` in `verifiers/` | exit 1, 4 failures over 1845 assertions |
| errata excuses 2111 | checklist at 7ad7fad | `1 recorded absence(s) excused`, line sha `7dcbf123…` matches |
| errata fails on restored runner | created `.ufo/round-45/drafts/v10/post-r44-hunt.py` | checklist exit 1, `stale, the path now resolves` |
| errata fails on appended copy | appended LOG line citing the token | checklist exit 1, `LOG.md:2327 ... does not resolve` |
| errata fails on in-place laundering | rewrote line 2111 wording | checklist exit 1, `line text drifted` |
| four XML fixtures exist and discriminate | direct reads + self-test | codespan/split/dq-escape must-fail, control (arrows/comparisons) passes |
| S015 frozen substrate | `sha256sum -c SHA256SUMS` in `/fast/scratch/kotoba-r47/shared` | exit 0, 4/4 OK; omp `fdbc8136…`, opencode `179ca421…` |
| census ledger anchors (12 rows) | `python3 -c '...count...'` on the frozen 1.19.3 dump | every count matches: `ConfigInstructionPlugin*` 0, `ReadTool.Plugin` 0, `SessionInstructions*` 0, `session.instructions.entry.put` 0, `j5(r.config,"AGENTS.md")` 0, `InstructionDiscovery` 0, `var n="1.19.3"` 1, `2.0.26` 0, `X.join(r.config,"AGENTS.md")` 1, `for(let O of T.instructions)` 1, `CONTEXT.md` 1, `X.join(r.home,".claude","CLAUDE.md")` 1, `Instructions from: ` 4, `fn("Instruction.resolve")` 1, `fn("ReadTool.execute")` 1, `disableClaudeCodePrompt` 3, `.filter((q)=>q.startsWith("https://")` 1, `instructions:{entry:{list:` 1 |
| dump-line citations in census § B′ | located anchors in the dump | cited "dump 443993/443995/444228/445481-445487" are **line numbers** and match: globUp 443993, Instruction.resolve 443995, ReadTool.execute 444228, InstructionContext.observe 445482, system-context-builtins 445487; `<system-reminder>` 18 hits as claimed |
| 92 seats / role split / 72 reported / 20 dead (`LOG.md:2319-2320`) | `build-spec.json` vs `build/*.md` | 92 items, roles 39/17/10/8/6/5/2/2/2/1; 76 md − 4 non-seat artifacts (`KnowDescriptionRule.s001-s003`, `RevLogAppend.proposed-entry`) = 72 reports; spec-minus-reports = exactly the 20 names printed at `LOG.md:2320`, same order |
| 8 job-cap refusals, try 9 (`LOG.md:2319`) | `build-refusals.json` | 9 attempts; refused=92 on 1–8, refused=0 on 9; `build-task-result.txt`: "Spawned 92 background agents" |
| SOURCES 11 → 15 rows | `grep -cE '^\| S0[0-9][0-9] ' corpus/SOURCES.md` | 15; census `scripts/sources-census.sh validate --root ... kotoba` exit 0 |
| S012 quote/location (`corpus/SOURCES.md:25`, lesson Gate) | `curl` raw `quick_validate.py` at `dbd4588…` | line 79 `# Check for angle brackets`, line 81 `return False, "Description cannot contain angle brackets (< or >)"`; sha256 `67cf570340…` matches the row; commit date 2026-10-09 |
| S013 308 + Last-Modified + quote | `curl -I` / `curl -L` | `HTTP/2 308` → `learn.chatgpt.com/docs/build-skills`; `last-modified: Wed, 21 Oct 2026 15:05:00 GMT`; sentence present |
| S014 dates + quote | `curl -L` research page | `datePublished 2025-10-16`, `dateModified 2026-10-18`; "At startup, the agent pre-loads the name and description of every installed skill into its system prompt." present |
| S003 re-open byte identity | `sha256sum .ufo/waves/round-47/build/KnowDescriptionRule.s003-best-practices.md` | `727f3fa116…` matches the lesson's `727f3fa1…` |
| S001 anchor-label defect (`corpus/lessons/round-47.md` § Gate) | `curl -L https://agentskills.io/specification`, extracted headings | no heading matches "Skill metadata table" (0 occurrences); headings are `Frontmatter`, `metadata field`, `Progressive disclosure` — the recorded defect holds |
| M20 evidence command | `git show c61a973:SCORECARD.md \| grep -c 'installed omp 18.12.3'` | 1 |
| M21 evidence | `git show --stat c61a973` / corpus integrity at c61a973 / at 04192c2 | adds only `corpus/lessons/round-46-verifier-spotcheck.md`; exit 1 (59≠58, unindexed 1) / exit 0 (58 tracked, 9/9) |
| M22 evidence | `grep -n 'complete-census condition is UNMET'` at 78ee57e and BASE; f2f9ee1 row shift; SKILL token line | line 76 both; row 38 at 173 (+8) and round-38 entry at 108 (+8); `<skills>` on SKILL.md line 14 at f2f9ee1 |
| corpus tracked_files 58 → 60 | `git ls-files corpus \| wc -l` | 60 |
| opencode package identity | `package.json` in the npx cache | version 1.19.3, `bin.opencode: ./bin/opencode.exe`; wrapper (read, not executed) resolves `opencode-ai` through npx |

# Counterexamples / negative results

- No stale `file:line` citation was found in the **new round-47** LOG/SCORECARD text. The 11
  `file:line`-shaped tokens in changed record lines break down as: (i) repo-rooted and resolving —
  `LOG.md:2111` (new, the erratum subject), `corpus/knowledge/fail-closed-and-anti-patterns.md:58`
  (carried, `LOG.md:1272`), `verifiers/baseline.json:7` (carried, `LOG.md:1252`); (ii) quoted
  wrong-at-birth pointers that the lesson M22 is *about*, not claims —
  `SCORECARD.md:80/165`, `SKILL.md:15`; (iii) bare legacy prose in rewritten SCORECARD rows, not
  repo-rooted subjects (`PROTOCOL.md:34-39`, `baseline.json:7's`, `SKILL.md:456/465` — the checker's
  `citation_resolve('PROTOCOL.md')` is False from the repo root, `'../PROTOCOL.md'` True); (iv) the
  upstream path `skills/skill-creator/scripts/quick_validate.py:79/81` in S012/the lesson, outside
  the governance gate's file set, matching the fetched file. None of (i)–(iv) is a stale round-47
  claim. The dead references found are prose pointers to a missing LOG section (F1), not
  `file:line` tokens.
- The `SCORECARD.md:31` C2 counting command is re-runnable as printed at both trees; the only
  non-runnable printed form is the before-artifact placeholder (F6.2).
- The `verify_surfaces.py --self-test` output prints two `ERROR ... NO-SUCH.md/.json` lines as
  negative controls and still exits 0; this is expected and not a claim defect.
- The after-battery directory `.ufo/waves/round-47/after/` is **untracked** at 7ad7fad and its
  files are timestamped 13:46–13:48, after the commit's committer time 13:46:13 (author time
  12:05:28). I reproduced every value it records; the untracked state is a durability note, not
  a false claim.

# What I did NOT check

- The 20 dead seats' reports (they do not exist by definition); their partial artifacts were not
  audited beyond the two named in the landing text.
- The full contents of all 72 wave-1 build reports; I read only those the landing text cites
  (`C1OmpCallShapes`, `KnowSubstrateRecensus`, `C1CriticRepin`, `C2CriticRule`, `C3CriticDesign`,
  `C3SentinelErrata`, `ExecFaultBaseline`, `Mistake*`, `Src*`, `RevLogAppend`, `RevScorecardRows`).
- S013/S014 beyond the quoted sentences and metadata; S012 beyond `quick_validate.py:70-90`.
- Whether a later appends cure F1 (the landing-pin entry may be written in a subsequent commit).
- Semantic adequacy of the C1 re-derivation (that the 9 ids are the *right* classes, not just
  that the anchors count): that is the C1 lanes' question, not the mistake sweep.
- The host-skill root cause behind `verify_harness_claims.py` 21/28; I only reproduced the count
  and the seven DRIFT ids (`omp.db.rows`, `omp.offered.skills`, `omp.cache.misses`,
  `omp.catalogue.total`, `omp.catalogue.missing_names`, `omp.cache.verified_skills`,
  `oc.roots.names_and_builtin`).
- No installs or upgrades were needed; no pacman transaction was run.
