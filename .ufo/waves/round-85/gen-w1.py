#!/usr/bin/env python3
"""Generate the round-85 wave-1 spec (one v1 wave, 16 seats)."""
import json
import os

REPO = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = "r85-w1"
BASE = "1c8f37edf2e5ac0fb3c2be1c88e32406313fe47b"
FREEZE = "f822dd113fe9f58661dd642dc207669581a4ab57"
RECEIPTS = ".ufo/waves/round-85/receipts"

CONTEXT = f"""## Bounds (read first)
Lane repo: {REPO} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Never write the fleet root, a sibling lane, a file over 50 MB in /tmp, or
considerthese/ (operator-authored, read-only). /home/vgpnk/Projects/shokuknow is read-only: read it,
never write, fetch or run a campaign tool there.
Scratch: create ONE dir /fast/scratch/hyaku/kotoba-r85/<your-seat-name>/ (mkdir -p), pass it
explicitly (TMPDIR=... and any --work), delete it with `trap 'rm -rf -- "$S"' EXIT` (or a finally:)
before you yield; copy receipts first under
{REPO}/.ufo/waves/round-85/w1/<your-seat-name>/.
Never run git/jj writes; read-only git (log, show, diff, status, ls-files, rev-parse, cat-file) is
fine. Never touch /home/vgpnk/Projects/shokunin/.ufo/ (except your own receipts under the lane),
MANIFEST.json, scripts/, templates/, .ufo/state/, .ufo/watchdog.log, or another lane. Never message
agent://all; the only address you may message is agent://KotobaR85.
Security: never write a raw environment dump into the lane (key names and canary presence only).
Tooling authorization (operator 2026-10-19): you may install or upgrade tools that help the task;
read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record
tool/version/channel/reason in your answer). PACMAN IS PAUSED host-wide: no pacman transaction of any
kind; use uv tool / npx / an official binary in ~/.local/bin.
Every `Report:` trailer path the validator renders is relative to {REPO} — write it at
{REPO}/<that path>. Your final answer is a short JSON: files_written, evidence (commands + observed
lines), risks.

## Frozen state (round 85 attempt 1, this host)
Base commit: {BASE}. Freeze commit: {FREEZE} (plan + claims + base receipts, committed before any
after-value). Read {REPO}/plans/round-85.md and {REPO}/.ufo/waves/round-85/claims.json first.
C1 (depth): `python3 -B verifiers/check_description_render.py --rev <rev>` prints
`description render rules met N of 8` and exits 0 iff N == 8. Rules R1-R8 are spelled in the plan
§ C1 with their exact labels (R1 first_sentence_le_99, R2 prefix_carries_triggers, R3
spec_max_1024, R4 imperative_invocation, R5 sibling_clauses, R6 eval_set_shape, R7 no_xml_tag,
R8 sourced_entry). Implement or attack exactly those strings; never add, drop or rename a rule.
C2 (freshness): `python3 -B verifiers/check_substrate_pins.py` exits 0 printing `OK 3/3 pins hold`,
AND `python3 -B verifiers/verify_surfaces.py --json` exits 0 with "pass": 7 and "fail": 0.
File ownership (one writer per production file): ExecC1Counter owns verifiers/check_description_render.py
and verifiers/fixtures/description-render/; ScribeC1Entry owns
corpus/knowledge/description-trigger-discipline-round85.md; ScribeSources owns corpus/SOURCES.md and
corpus/README.md; ScribeLesson owns corpus/lessons/round-85.md, LOG.md and the append-only correction
block in corpus/lessons/round-84.md; ExecC2Pin owns the four omp path constants and its candidate
baseline under its wave dir; ExecC1Eval and ExecC1Desc write only under their own wave dirs. Every
other seat writes only under its own wave dir. SKILL.md itself is integrated by the L1 — never edit it.
Instrument conventions: Python stdlib only, `python3 -B`, honour TMPDIR/--work (no hardcoded /tmp),
`--rev` reads committed bytes through `git show`, exit ladder 0 pass / 1 content fail / 2 environment
error, `--self-test` prints `0 failure(s) over N assertions`.

## Round-85 base facts measured at {BASE} (receipts in {RECEIPTS}/)
- `check_substrate_pins.py` exit 2: `UNREADABLE 2/3 pins failed: omp_binary_sha256,
  omp_binary_mtime` (path /home/vgpnk/.local/bin/omp.real does not exist on this host).
- `verify_surfaces.py --json` exit 2: `omp binary not found: /home/vgpnk/.local/bin/omp.real`;
  with `--omp-binary /home/vgpnk/.local/bin/omp` (omp/18.15.0, sha256 6737ee24...) it reads pass 7,
  fail 0, exit 0.
- The lane's parsed SKILL.md description is 1,021 of 1,024 characters, first sentence 150; the lane's
  own SKILL.md records omp's listing cut at offset 99.
- `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
  /home/vgpnk/Projects/shokunin kotoba` exit 1 with 180 E12 rows: corpus/SOURCES.md is CRLF and the
  census's `## Registry` heading test never enters the section on this host.
- The round-74 sibling census (`corpus/knowledge/sibling-overlap-census-round74.md`) is the current
  base for `verifiers/check_sibling_census.py --province PROVINCE.md` (20 matched 20, exit 0); the
  round-49 census file is stale (matched 4, exit 1) and is not the base.

## YOUR ITEM
"""

ITEM = {}

ITEM["ScoutSource"] = ("scout", """
Open S213 live this round: `https://agentskills.io/skill-creation/optimizing-descriptions.md`.
Fetch it with `curl -sL -o "$S/page.md" -w 'HTTP %{http_code} size %{size_download}\\n' <url>` plus
`sha256sum` and `wc -c`; record the exact fetch command and output in
`{repo}/.ufo/waves/round-85/w1/ScoutSource/fetch-record.txt`.
Then locate, with page line numbers (`grep -n`), a <=25-word quote for each of:
(a) the sentence that says the description carries the burden of triggering; (b) the imperative
"Use this skill when..." authoring form; (c) the trigger-eval design (about 20 queries, 8-10
should-trigger and 8-10 should-not-trigger, near-miss negatives); (d) the 1024-character description
limit; (e) the caveat that agents consult skills only when the task needs knowledge beyond them.
Write `w1/ScoutSource/source-packet.md`: url, access date 2026-11-04, HTTP status, bytes, sha256, and
one row per quote (page line, quote verbatim, word count <= 25, what it grounds).
Then read, read-only, `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md`
and the round-74 rejection row in `{repo}/corpus/lessons/round-74-verifier-spotcheck.md` (grep
`spec-description-trigger-discipline`). Verdict per staged claim: survives re-grounding on the live
bytes (quote located), or refused (quote not found / page says otherwise) with the reason. Never write
inside shukuknow. Do not add a SOURCES row: S213 already holds this page (a new row would be a W04
duplicate); you are opening S213, not minting a row.
Acceptance: fetch record with HTTP/bytes/sha256; five quotes with page lines and word counts; the
staged-claim verdict table.
""")

ITEM["ScoutSubstrate"] = ("scout", """
Recon the host substrate that C2 re-pins. Record in
`{repo}/.ufo/waves/round-85/w1/ScoutSubstrate/recon.txt`:
1. `file /home/vgpnk/.local/bin/omp`, `ls -l`, `/home/vgpnk/.local/bin/omp --version`,
   `sha256sum /home/vgpnk/.local/bin/omp`, `stat -c '%y' /home/vgpnk/.local/bin/omp`
   (ns-exact stamp; also print the same stamp reformatted as `%Y-%m-%dT%H:%M:%S.%N%:z`).
2. Whether `/home/vgpnk/.local/bin/omp` is the ELF the `omp` command runs (no wrapper hop on this host)
   and whether `/home/vgpnk/.local/bin/omp.real` exists at all.
3. `python3 -B verifiers/verify_surfaces.py --json --omp-binary /home/vgpnk/.local/bin/omp` — paste the
   pass/fail counts and every check id with its verdict. Also run the same with no override and record
   the exit-2 error.
4. Dump `strings -n 4 /home/vgpnk/.local/bin/omp > "$S/omp-1815.strings"` and check which of the 42
   ids in `verifiers/surfaces-baseline.json` still resolve, listing any baseline literal that does not
   occur; then check `verifiers/census-removals.json` for classes declared gone and whether any of
   them occurs again.
5. Whether the description render cut constant still appears: search the dump for `_8n`, `available_skills`,
   `skill-descriptions` and report the located lines (file offset of the first hit).
Report the exact pin values C2 must record (sha256, ns ISO mtime with `-03:00`), and any inventory id
whose class would drift. Read-only: do not edit verifiers/ or SKILL.md.
Acceptance: the recon file with each command and its observed output; an explicit list of ids that
would change and the exact pin triple.
""")

ITEM["ExecC1Counter"] = ("executor", f"""
Write the C1 counter `{{repo}}/verifiers/check_description_render.py` exactly to the plan
`{{repo}}/plans/round-85.md` § C1: eight rules R1-R8 with the exact labels and conditions, reading
committed bytes of `SKILL.md` and of `verifiers/fixtures/description-eval-round85.tsv` at `--rev`
(default `.`, optional `--repo`), plus `--eval PATH`, `--json`, `--self-test`.
- Parse the frontmatter `description` with the same semantics as
  `verifiers/check_sibling_census.py` `description_of()` (block-scalar indicator dropped, whitespace
  collapsed, value ends at any column-0 line) — reuse that approach, do not import the module's CLI.
- R5 runs `verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md
  --province PROVINCE.md --skill SKILL.md` as a subprocess and requires exit 0 plus the line
  `skill description names 10 of 10 non-none lanes`.
- R6 reads the eval TSV: header exactly `label<TAB>query`; 8-10 rows of each label; >= 5
  should-trigger rows contain none of the description's declared trigger terms (the quoted strings in
  its `Triggers:` clause, case-insensitive); every should-not-trigger row shares >= 1 lowercased
  alphanumeric token of >= 4 characters with the parsed description.
- R8 reads `corpus/knowledge/description-trigger-discipline-round85.md`: `source:` names S213,
  `verified-at: 2026-11-04`, a `recheck:` line, and at least one quote of <= 25 words.
- Print one line per rule (`R1 first_sentence_le_99: ok|fail <detail>`) and the summary
  `description render rules met N of 8`; exit 0 iff N == 8, 1 otherwise, 2 only for an environment
  error (unreadable repo, missing git, bad args).
- `--self-test` builds fixture worlds in a tempdir (honour TMPDIR) under
  `verifiers/fixtures/description-render/` and must include at least: perfect world (8 of 8), naive
  99-char cut, token dump, missing eval set, XML tag, sibling clause lost, first sentence 100 chars,
  and one mutation arm per rule that must turn that rule red. It prints
  `0 failure(s) over N assertions`.
Then measure baseline: run `--rev {BASE}` and paste the per-rule lines and the count into
`w1/ExecC1Counter/base-receipt.txt`; print the sha256 of your own file. Do not edit SKILL.md.
Acceptance: `--self-test` exit 0; the base count is < 8 with the failing rules named; the counter
exits 1 (content) and never 2 on the base rev.
""")

ITEM["ExecC1Eval"] = ("executor", """
Author the C1 trigger eval set candidate at
`{repo}/.ufo/waves/round-85/w1/ExecC1Eval/description-eval-round85.tsv` against the candidate
description bytes frozen in `{repo}/plans/round-85.md` § C1 (copy them exactly; do not paraphrase).
Header line exactly `label<TAB>query` (a real tab). 9 `should-trigger` rows and 9
`should-not-trigger` rows.
- At least 5 should-trigger rows must be indirect: they name none of the trigger terms
  ("skill file", "SKILL.md", "frontmatter description", "trigger words", "prompt craft", "write a
  skill", "audit this skill", "skill quality"), e.g. a user complaining a skill never fires, or
  asking why an agent ignored their prompt file.
- Every should-not-trigger row must be a near miss: it shares at least one lowercased alphanumeric
  token of >= 4 characters with the description but needs a different skill (writing a model-output
  prompt, editing runtime code, writing ficworld lore, publishing a web page, packaging a host
  package). No obviously irrelevant row ("what is the weather" tests nothing).
Write a mirror checker (<= 120 lines, stdlib) at `w1/ExecC1Eval/mirror_check.py` that applies the
R6 conditions from the plan to your TSV and prints the counts, the indirect count and, per negative
row, the shared token. Run it and paste the output in `w1/ExecC1Eval/receipt.txt`.
Acceptance: TSV with 9+9 rows, >= 5 indirect positives, every negative near-miss with a named shared
token, mirror checker exit 0.
""")

ITEM["ExecC1Desc"] = ("executor", """
Build the C1 description candidate as a SKILL.md copy at
`{repo}/.ufo/waves/round-85/w1/ExecC1Desc/candidate-SKILL.md`: take `{repo}/SKILL.md`, replace ONLY the
frontmatter `description:` block with the candidate text frozen in `{repo}/plans/round-85.md` § C1,
written as a YAML folded block (`description: >` plus indented lines). Fold at spaces only — never
break a word — and indentation must keep every line column-1 or deeper.
Then prove, with `verifiers/check_sibling_census.py`'s own `description_of()` loaded as a module
(importlib), that the parsed value is byte-equal to the plan's candidate text (report the exact
`parsed == candidate` boolean, both lengths, the first-sentence length, and `repr(parsed[:99])`).
Run the sibling guard against the copy:
`python3 -B verifiers/check_sibling_census.py corpus/knowledge/sibling-overlap-census-round74.md
--province PROVINCE.md --skill <copy>` and paste its last three lines and exit code.
Run `python3 -B verifiers/verify_skill_checklist.py` (it reads the repo SKILL.md; if it cannot target a
copy, say so and instead run its two trigger rules' conditions by hand on the parsed value: literal
`Triggers:`, `Anti-triggers` present, no `<`/`>`).
Produce `w1/ExecC1Desc/frontmatter.diff` — the exact unified diff of the frontmatter block that the L1
will apply to SKILL.md (base lines vs candidate lines). Do not edit SKILL.md itself.
Acceptance: parsed == candidate; 10 of 10 sibling names, exit 0; first sentence <= 99; a diff that
applies cleanly to the base file.
""")

ITEM["ExecC2Pin"] = ("executor", """
C2 payload. (a) Edit the four host-anchored omp path constants to this host's ELF, each with a dated
one-line comment `round 85: this host's omp is the ELF itself (omp/18.15.0); omp.real does not exist`:
`verifiers/check_substrate_pins.py` BINARIES["omp"], `verifiers/verify_surfaces.py`
DEFAULT_BINARIES["omp"], `verifiers/verify_harness_claims.py` OMP_BIN,
`verifiers/verify_harness_independent.py` DEFAULT_OMP_BINARY. Keep every other constant unchanged.
(b) Write `w1/ExecC2Pin/baseline.json.candidate`: a copy of `verifiers/baseline.json` whose
`measured_against.omp_binary_sha256` and `omp_binary_mtime` are re-derived from
`/home/vgpnk/.local/bin/omp` (ns-exact ISO stamp with the `-03:00` offset, the format the checker
parses) and which adds an `omp_round85_note` recording version, sha256, mtime, the re-derivation
commands, and that the 18.12.6 pin is superseded. Do not edit `verifiers/baseline.json` itself.
(c) Controls on the candidate in scratch (each with its exit code recorded):
   1. candidate as-is -> expect exit 1 (DRIFT naming omp_binary_sha256) until the real baseline is
      swapped; that is the instrument-proves-it-reads receipt;
   2. opencode's sha256 placed under omp_binary_sha256 -> exit 1 DRIFT;
   3. the omp pins deleted -> exit 1 (absent pin);
   4. `--omp-binary /home/vgpnk/.opencode/bin/opencode` with the candidate -> exit 1.
(d) Run `python3 -B verifiers/verify_surfaces.py --json` after the path edits (expect exit 0, pass 7,
fail 0) and `python3 -B verifiers/verify_surfaces.py --json` with the base path (expect exit 2) as the
before/after pair. Paste every command and its tail into `w1/ExecC2Pin/receipt.txt`.
Acceptance: the four path edits' diffs; the candidate pin values; four control receipts with exit
codes; surfaces exit 0 pass 7 fail 0 after the edit.
""")

ITEM["ScribeC1Entry"] = ("scribe", """
Write `{repo}/corpus/knowledge/description-trigger-discipline-round85.md` (C1's sourced knowledge
entry). Structure like the lane's other entries: a title, then `source:` naming S213
(`https://agentskills.io/skill-creation/optimizing-descriptions.md`), `verified-at: 2026-11-04`,
`recheck:`, a `ground:` line, findings, and a closing pointer to the counter.
Content, all of it grounded on quotes that exist in `w1/ScoutSource/source-packet.md` (read it; invent
nothing, and do not quote a sentence the packet does not carry):
1. The page's own problem statement: an under-specified description does not trigger, an over-broad
   one triggers wrongly; the description carries the triggering burden.
2. The authoring rules: frame it as an instruction to the agent ("Use this skill when..."), describe
   the user's goal rather than the mechanics, be pushy about contexts including ones that never name
   the domain, and stay inside 1,024 characters.
3. The eval design: about 20 labelled queries, 8-10 each way, near-miss negatives, indirect positives
   are the valuable ones; the caveat that a task the agent can handle alone may not trigger the skill
   even with a good description.
4. The three-way tension on negative conditions, stated as three distinct things and not averaged: a
   negative *scope* in the description (TRAE's position, already held at `corpus/knowledge/
   chinese-vendor-skill-surfaces-round73.md`), the *eval set* as the test (the specification), and a
   negative *directive* in the body (Chiba's warning, round 73). State the lane's reading: this lane
   keeps an `Anti-triggers:` scope clause and puts near-miss negatives in the eval set.
5. This lane's own before -> after: the parsed description was 1,021 characters with a 150-character
   first sentence, past omp's offset-99 listing cut; the round-85 candidate is 876 characters with a
   64-character first sentence and ten sibling clauses, and R6 requires a 9+9 eval set.
End with the exact counter command `python3 -B verifiers/check_description_render.py --rev <rev>`.
Acceptance: the file; every quote traceable to the packet with <= 25 words; `source:` names S213;
`verified-at` and `recheck:` present; no claim the packet cannot ground.
""")

ITEM["ScribeSources"] = ("scribe", """
Four record repairs, one writer for both files.
1. `corpus/SOURCES.md` is CRLF and the census cannot see its `## Registry` heading on this host
   (180 E12 rows, receipt .ufo/waves/round-85/receipts/census-round-start.txt). Normalize the file to
   LF: `python3` read bytes, replace `\\r\\n` with `\\n` (and any lone `\\r` with `\\n`), write back.
   Prove no cell changed: `diff <(git show {BASE}:corpus/SOURCES.md | tr -d '\\r') <(tr -d '\\r' <
   corpus/SOURCES.md)` prints nothing; record byte counts before/after and that proof in
   `w1/ScribeSources/crlf-proof.txt`. Do not touch any other file's line endings.
2. Update S213's `used-by` cell (last cell) to add `corpus/knowledge/description-trigger-discipline-round85.md`,
   keeping the row at 13 pipe-separated fields and no literal `|` inside a cell. Record old -> new in
   `w1/ScribeSources/s213-usedby.txt`.
3. Add 7 rows to `corpus/README.md` § Coverage map for the unindexed files named in
   .ufo/waves/round-85/receipts/before-gates.txt: corpus/lessons/round-81-verifier-spotcheck.md,
   round-82.md, round-82-verifier-spotcheck.md, round-83.md, round-83-verifier-spotcheck.md, round-84.md,
   round-84-verifier-spotcheck.md. Match the existing row shape; describe each file in one clause from
   its own head (never invent content). These are closure/lane records: indexed, never edited.
4. Validate: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file
   corpus/SOURCES.md` must exit 0 (receipt `w1/ScribeSources/census-lane-file.txt`); and
   `python3 -B verifiers/verify_corpus_integrity.py --json` must show `corpus.index.unindexed`
   observed 0 (other DRIFT classes are refreshed by the L1 at round end — record them as-is).
   Also run `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotoba` and record its exit code and tail.
Acceptance: census `--file` exit 0; the tr-diff empty proof; S213 old->new; 7 index rows; unindexed 0.
""")

ITEM["ScribeLesson"] = ("scribe", """
Write the round-85 lesson and the round's log entries.
1. `corpus/lessons/round-85.md` with: an intro (base {BASE}, freeze {FREEZE}, the two claims); `## Gate`
   with the sourced rows actually opened this round (S213: url, access date 2026-11-04, HTTP status,
   bytes, sha256 and the located <=25-word quote from `w1/ScoutSource/source-packet.md`), the census
   before/after commands and exit codes, rows added 0, rows touched S213 (used-by old->new), frontier
   rows advanced; the C1 and C2 predicates verbatim from the plan with their base readings; and the
   records this round touched (S213, the CRLF normalization, the 7 index rows).
2. `## Mistakes` — exactly two, each with class - evidence pointer - captured-by - fix:
   (a) r84-D1: a numeric wording claim ("10 FAIL instruments") carried without a counting command, so
   the reader could not re-derive it; evidence `corpus/lessons/round-84-verifier-spotcheck.md` § defects;
   captured-by: the lane's counting-command rule, which needs a QUALITY.md criterion; fix: add the
   criterion (Q-number appended to `corpus/QUALITY.md`, appended, never renumbered) and append a
   correction block to `corpus/lessons/round-84.md` naming the measured count and the command.
   (b) the CRLF registry defect: a committed registry that parsed on one host and read as 180 E12 rows
   on another because the census heading test is byte-exact; evidence
   `.ufo/waves/round-85/receipts/census-round-start.txt`; captured-by: the census E12 class, which did
   catch it once run on this host; fix: LF normalization plus the lesson rule "a registry change is
   validated with the census on the host that will read it, and the census is run before the report".
3. `## Ruled out` (with reasons): the byte ceiling and the Gate-registry move (considerthese proposals 1
   and 2) sized out; a new S-row for the description page (W04 duplicate); the round-49 census as the
   guard's base (stale pins; round-74 census is current).
4. Append the append-only correction block to `corpus/lessons/round-84.md` (## Correction, round 85)
   naming the measured FAIL count with its counting command; never rewrite the r84 text.
5. Append `LOG.md` entries: one per claim (surface changed, command, before->after, commit to be named
   as "round-85 landing" without inventing a hash), one intake entry (S213 re-open + merge/kotoba
   adoption through this lane's gate + considerthese proposal 3), and one routed-defect entry (the
   pre-existing reds: checklist citation tokens, round-49 census pins). LOG.md is append-only.
Acceptance: files exist; the lesson's Gate quotes match the scout packet; no invented hash; LOG diff
has zero deletions.
""")

ITEM["Connector"] = ("connector", """
Sibling/cross-source scan (read-only). Produce `w1/Connector/overlap.md`:
1. Does any sibling lane already hold (a) the description render cut / trigger-eval discipline, or
   (b) host substrate pinning of an installed harness? Read at their committed heads: kengaku
   (measured capability effects of prompt format), kumitate (dispatch/orchestration tooling),
   tameshi (fixture/mutation method). For each, name the file:line you read and whether it collides
   with this round's C1 or C2.
2. Read the staged package entry
   `/home/vgpnk/Projects/shokuknow/merge/kotoba/knowledge/corpus/knowledge/spec-description-trigger-discipline.md`
   and `corpus/lessons/round-74-verifier-spotcheck.md`'s rejection row. Is the round-74 flip condition
   (cite the already-held row instead of minting a duplicate) satisfied by this round's plan? Answer
   yes/no with the exact lines.
3. List any other merge/kotoba staged entry whose ground now overlaps C1 or C2 (name + why), and any
   `considerthese` proposal still unimplemented that this round does not touch (name it, do not
   implement it).
4. One `no-absorb` line: what this lane must not claim because a sibling owns it.
Acceptance: the table with file:line evidence; the flip answer; the no-absorb line. Write only under
your wave dir.
""")

ITEM["ReviewerC1"] = ("reviewer", """
Independent attack on C1. Build your own oracle from `{repo}/plans/round-85.md` § C1 (do not read
the counter's code first): implement the eight rules in a scratch script and score, at the base rev
(`--rev {BASE}` semantics: `git show {BASE}:SKILL.md` etc.) and at the current working tree (the
candidate description may be applied by the L1 later; if SKILL.md still holds the base text, say so).
Paste per-rule verdicts for: base bytes; the plan's candidate text; a naive cut of the base to 99
characters; a token dump (trigger list + ten lane names, no clauses); an eval set of 9 identical
should-trigger rows; an eval set whose negatives are obviously irrelevant; a description whose first
"sentence" is short only because of "e.g.".
Then, if `verifiers/check_description_render.py` exists, compare its per-rule output with your oracle
line by line and report every disagreement (this is the predicate-identity check: the counter's
condition must be the plan's sentence).
State the largest false-green door you found and whether it reaches 8 of 8.
Write `w1/ReviewerC1/review.md` + receipts. Do not edit production files.
Acceptance: oracle vs counter table; the seven world scores; a yes/no on whether any world other than
the candidate reaches 8 of 8.
""")

ITEM["ReviewerC2"] = ("reviewer", """
Independent attack on C2. (1) Re-derive the pin values yourself: `sha256sum
/home/vgpnk/.local/bin/omp`, `stat -c '%y'` (and the `%Y-%m-%dT%H:%M:%S.%N%:z` form), `file`,
`--version`; state whether the candidate baseline in `w1/ExecC2Pin/baseline.json.candidate` matches
them exactly. (2) Build control baselines in scratch and score each with
`python3 -B verifiers/check_substrate_pins.py --baseline <file>`: wrong sha (opencode's), deleted omp
pins, wrong path, and a pin value in a non-ns format — record exit codes and the exact lines. (3)
`grep -rn 'omp\\.real' verifiers/ SKILL.md` and list every remaining constant/path that still names the
missing path, marking each as live code, comment, or documentation. (4) Verify
`verify_surfaces.py --json` reads the same ELF (no override) and that its class inventory is unchanged
(42 ids). (5) Verdict: is the guard non-vacuous (a wrong binary cannot pass), and does any control
exit 0 when it must not?
Write `w1/ReviewerC2/review.md` + receipts. Do not edit production files.
Acceptance: control table with exit codes; the omp.real grep table; the vacuity verdict.
""")

ITEM["Critic"] = ("critic", """
Falsify both claim targets with do-nothing and shortcut worlds, scored on the frozen predicates.
Build worlds under your scratch dir:
W0 base tree at `{BASE}` (git worktree/clone-free: `git -C {repo} archive {BASE} | tar -x -C "$S/W0"`);
W1 W0 plus the plan's candidate description only (no eval set, no entry);
W2 W0 plus the candidate description and a token-dump eval set;
W3 W0 plus the eval set and entry but the base description;
W4 W0 plus the four omp path constants only (no pin values);
W5 W0 plus the candidate pin values but the base path constants.
For each world run the C1 counter (if it exists; else the ReviewerC1-style independent oracle you
build from the plan) and `check_substrate_pins.py` / `verify_surfaces.py --json` with `--repo`/`--repo`
or `--baseline` as each tool allows, and record the score and exit code.
Answer: (a) can any world that skips the claimed work reach the C1 target? (b) can W4/W5 reach the C2
target? (c) what is the cheapest world that reaches each target, and does it contain the claimed work?
Write `w1/Critic/worlds.md` + per-world receipts. Do not edit production files.
Acceptance: the six-world table with commands, scores and exit codes; the three answers.
""")

ITEM["MutTester"] = ("mutation-tester", """
Mutation battery for both counters (or for the frozen spec if a counter is missing at your start).
C1: for each rule R1-R8, construct a world that satisfies all other rules but violates exactly that
one (description-only mutants and eval-set mutants), score it, and show that rule alone goes red and
the count falls below 8 — i.e. the rule is load-bearing, not decorative. Also try two "laundering"
mutants: a description whose trigger terms appear only after offset 99 (R2 must still pass but R1 must
fail if the first sentence is long), and an eval set whose negatives are near-misses of each other but
not of the description (R6 must fail).
C2: mutate the pin (wrong sha), the path (missing file), and the mtime format (non-ns) and show each
is rejected.
Write `w1/MutTester/mutants.md` + one receipt per mutant with the exact command and observed line.
Acceptance: 8 C1 mutants + 2 laundering mutants + 3 C2 mutants, each with the expected-vs-observed
verdict; any mutant that survives is named as a counter defect.
""")

ITEM["RevengerRender"] = ("revenger", """
Reverse-engineer the installed harness's description renderer, one hypothesis: does omp 18.15.0 still
cut the skill listing at offset 99 (`_8n=100`), the figure this lane's SKILL.md pins at line 30 and
587?
Dump `strings -n 4 /home/vgpnk/.local/bin/omp` into scratch, locate the description-rendering chunk
(search `available_skills`, `skill-descriptions`, `_8n`, `SKILL.md` near the listing code), and report
the located bytes (string index/offset, the surrounding 1-2 lines). If the code is minified or the
literal is renamed, report what you did find (the render call shape and any numeric constant adjacent
to it) and say `unresolved` rather than guessing.
Also check the sibling claim used by C1's R1: whether the cut is at 99 characters or at 100 bytes, and
whether a cached one-liner changes it (the lane's r54 entry says so). Quote the bytes you rely on.
Write `w1/RevengerRender/probe.md` + the dump excerpt file (<= 200 lines).
Acceptance: located evidence with offsets; verdict `cut-at-99 preserved` / `changed` / `unresolved`,
each with the bytes that justify it.
""")

ITEM["Sentinel"] = ("sentinel", """
Security review of this round's instruments and payloads (read-only; no production edits).
1. `verifiers/check_description_render.py` (if present) and the four omp path constants: does any guard
   newly execute the pinned binary, write outside `--work`/TMPDIR, follow a symlink out of the repo,
   or fail open on a missing input? Name file:line.
2. The CRLF normalization in `corpus/SOURCES.md`: verify with an independent content diff
   (`git show {BASE}:corpus/SOURCES.md | tr -d '\\r'` vs `tr -d '\\r' < corpus/SOURCES.md`) that no
   cell changed, and that no other file's line endings moved.
3. The new eval TSV, knowledge entry and lesson: confirm no environment dump, credential shape, token
   or absolute home path leaks into committed content (grep for `HOME=`, `TOKEN`, `KEY=`, `/home/`
   outside the documented lane paths).
4. The scout's fetch: confirm it is a read-only curl of a public URL with the bytes recorded, and that
   nothing was written under shukuknow.
Write `w1/Sentinel/audit.md` with a findings table (id, file:line, severity, verdict) and an explicit
"no new fail-open" or the defect.
Acceptance: the findings table; the content-diff proof; the leak grep output.
""")

ROLE_ORDER = [
    ("ScoutSource", None), ("ScoutSubstrate", None), ("ExecC1Counter", None), ("ExecC1Eval", None),
    ("ExecC1Desc", None), ("ExecC2Pin", None), ("ScribeC1Entry", None), ("ScribeSources", None),
    ("ScribeLesson", None), ("Connector", None), ("ReviewerC1", None), ("ReviewerC2", None),
    ("Critic", None), ("MutTester", None), ("RevengerRender", None), ("Sentinel", None),
]


def main():
    items = []
    for name, _ in ROLE_ORDER:
        role, body = ITEM[name]
        prompt = "/skill:godspeed\n\n" + CONTEXT.replace("{repo}", REPO) + body.replace("{repo}", REPO).replace("{BASE}", BASE)
        prompt = prompt.replace("{{repo}}", REPO).replace("{{BASE}}", BASE)
        items.append({"name": name, "role": role, "prompt": prompt})
    spec = {
        "wave": WAVE,
        "milestone": "r85-w1: C1 description render discipline + trigger eval set (sourced S213) and C2 host "
                     "substrate re-pin verified and attacked; registry CRLF repair; 8 rules and 4 controls "
                     "attacked by 6 attack seats.",
        "reportDir": ".ufo/waves/round-85/w1",
        "context": CONTEXT.replace("{repo}", REPO),
        "items": items,
    }
    out = os.path.join(REPO, ".ufo/waves/round-85", WAVE + "-spec.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, indent=1, ensure_ascii=False)
    print(out, len(items), "items")
    print(sorted({i["role"] for i in items}))


if __name__ == "__main__":
    main()
