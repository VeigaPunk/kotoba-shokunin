#!/usr/bin/env python3
"""Generate the round-86 wave-1 spec (one v1 wave, 13 seats)."""
import json
import os

REPO = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = "r86-w1"
BASE = "e5d966b51494f4177868ad5f46806a204783ef6c"
FREEZE = "ecfad51fe3f24540a6d67d2b54920929c7b83041"
W = f"{REPO}/.ufo/waves/round-86/w1"
COUNTER = "verifiers/check_omp_catalogue_repro.py"

CONTEXT = f"""## Bounds (read first)
Lane repo: {REPO} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{REPO} — write it at {REPO}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only) or /home/vgpnk/Projects/shokuknow (read-only: read it, never write,
fetch or run a campaign tool there).
Scratch: create ONE dir /fast/scratch/hyaku/kotoba-r86/<your-seat-name>/ (mkdir -p), export
TMPDIR to it and pass it to any --work, delete it with `trap 'rm -rf -- "$S"' EXIT` (or finally:)
before you yield; copy receipts first under {W}/<your-seat-name>/. /tmp only for files < 50 MB.
VCS: never run a git/jj write in the lane or the fleet (no add/commit/stash/checkout/reset/jj
mutation); read-only git (log, show, diff, status, ls-files, rev-parse, cat-file, archive) is fine.
A scratch repo is created only as `D=$S/repo && git clone -q --shared {REPO} "$D"` (or `git -C "$D"
init -q`), every later git call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal
$D before your first commit there. Never touch {REPO}/../.ufo, MANIFEST.json, scripts/, templates/,
.ufo/state/, .ufo/watchdog.log or another lane. Message only agent://KotobaR86 (never agent://all).
Never write outside the files your item names; production files have one owner each (below).
Security: never write a raw environment dump, credential or token into the lane.
Tooling authorization (operator 2026-10-19): you may install or upgrade tools that help the task;
read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record
tool/version/channel/reason in your answer). PACMAN IS PAUSED host-wide: no pacman transaction of any
kind (no -S/-Sy/-Syu/-U/-R); use uv tool / npx / an official binary in ~/.local/bin, or report the need.
Your final answer is a short JSON: files_written, evidence (commands + observed lines), findings, risks.

## Frozen state (round 86, Linux host, omp/18.15.0)
Base {BASE}; freeze {FREEZE} (plan + counter + fixture + controls, committed before any candidate
data). Read {REPO}/plans/round-86.md first; it is the claim's single source of truth.
C1 (freshness): `python3 -B {COUNTER} --rev <rev>` prints `omp catalogue lines reproduced N of 215`,
exit 0 iff N >= 205 and guards G1-G4 all PASS. Base: 83 of 215, G4 FAIL (no ledger), exit 1;
132 fixture names are `not-discovered` by the base model (receipts
{REPO}/.ufo/waves/round-86/receipts/c1-K0-base.txt). The counter, its fixture
`verifiers/fixtures/omp-catalogue-r86/catalogue.json` and its pins are FROZEN: nobody edits them;
a counter defect is reported as a finding, never patched.
The surface C1 changes: `verifiers/verify_harness_claims.py` (`WALKUP_REL`, `USER_ROOTS`,
`discover_skills`, `parse_frontmatter`, `omp_key`, `preview`) and the new roots ledger
`verifiers/omp-skill-roots.tsv` (header `root_pattern<TAB>binary_quote`; patterns `~/…`, `{{cwd}}/…`,
absolute, fnmatch globs; each quote >= 12 chars located verbatim in /home/vgpnk/.local/bin/omp).
omp 18.15.0 ships its TypeScript source inside the ELF (bun bundle): e.g. the module
`packages/coding-agent/src/extensibility/skill-descriptions.ts` sits near byte offset 178,7xx,xxx;
settings names `cfgSkillsEnableAgentsUser`, `cfgSkillsEnableClaudeUser`, `cfgSkillsEnableCodexUser`,
`cfgSkillsEnablePiUser`, `cfgSkillsCustomDirectories`, functions `loadSkills`, `loadSkillsFromDir`.
Read it with python mmap + re (the file is 277 MB; never copy it into the lane).
How to score a candidate model without committing in the lane: clone into $S/repo (shared), copy the
candidate files in, `git -C $S/repo -c user.name=seat -c user.email=seat@local commit -qam cand`,
then `TMPDIR=$S python3 -B {REPO}/{COUNTER} --repo $S/repo --rev $(git -C $S/repo rev-parse HEAD)`.
File ownership: ExecModel owns verifiers/verify_harness_claims.py and verifiers/omp-skill-roots.tsv;
ScribeEntry owns corpus/knowledge/omp-catalogue-model-round86.md; ScribeSources owns corpus/SOURCES.md
and corpus/README.md; ScribeLesson owns corpus/lessons/round-86.md, LOG.md and append-only blocks in
corpus/lessons/round-85.md. SKILL.md, SCORECARD.md and everything else are integrated by the L1.
Every other seat writes only under {W}/<its-seat-name>/.
Seats depending on ExecModel: it writes {W}/ExecModel/CANDIDATE_READY (the scratch commit hash and the
counter output) when its candidate scores; do your independent work first, then check for that file
every 2 minutes (sleep 120) for up to 45 minutes; if it never appears, report on the base and say so.
Instrument conventions: Python stdlib only, `python3 -B`, honour TMPDIR, exit ladder 0 pass / 1 content
fail / 2 could-not-evaluate, `--self-test` prints `0 failure(s) over N assertions`.

## YOUR ITEM
"""

ITEM = {}

ITEM["ScoutRootsSource"] = ("scout", """
Derive, from the omp 18.15.0 source embedded in /home/vgpnk/.local/bin/omp, exactly which directories
omp scans for skills when it builds the `<skills>` catalogue for a session, in which order, and how a
name present in two roots is resolved. Locate the modules (search the ELF bytes for
`// packages/coding-agent/src/` module headers near `loadSkills`, `loadSkillsFromDir`,
`cfgSkillsEnable`, `cfgSkillsCustomDirectories`, `rediscoverSkills`, `.agents/skills`, `.claude`,
`.codex`, `.pi`, `plugins`, `marketplace`). For each root class report: the path expression, the
setting that gates it and its default (find the settings schema default values), whether it recurses
or reads only `<root>/<name>/SKILL.md`, symlink handling, the project walk-up rule (cwd only or every
ancestor; stop at git root or home?), and the dedupe/precedence rule. For EVERY statement give the
byte offset and a verbatim quote (>= 12 chars, <= 25 words) that occurs in the ELF; record how you
located it (command). Also read `~/.omp/agent/config.yml` (read-only; report only skills-related keys,
never secrets) and any omp plugin manifests under ~/.omp that contribute skills.
Write {W}/ScoutRootsSource/source-packet.md (one table: root class | path expression | gate setting +
default | layout | precedence | offset | quote) and {W}/ScoutRootsSource/extract.txt (<= 300 lines of
the located source excerpts with offsets). Read-only everywhere else.
Acceptance: every root class omp 18.15.0 can read is listed with a located quote; unresolved items
are named `unresolved` with what you searched.
""")

ITEM["ScoutRootsHost"] = ("scout", """
Map the 132 fixture names the base model does not discover to host files. Inputs: the fixture
{REPO}/verifiers/fixtures/omp-catalogue-r86/catalogue.json (entries: name, render) and the MISS lines
in {REPO}/.ufo/waves/round-86/receipts/c1-K0-base.txt. For each missing name, list every
`*/<name>/SKILL.md` on this host outside /home/vgpnk/Projects/shokunin (use `fd`/`find` under $HOME
with depth limits; skip node_modules caches only if you also report that you skipped them), and for
each candidate compute the omp preview of its frontmatter description with the lane's own functions
(import {REPO}/verifiers/verify_harness_claims.py read-only and call `parse_frontmatter` and `preview`;
also compute `omp_key(template, name, desc)` with the template from the fixture's `template_hex` and
check it against the fixture's `cache_rows`). Mark which candidates reproduce the fixture render
byte-for-byte (cache hit or preview). Group the reproducing candidates by root directory (SKILL.md's
grandparent) and report each root with its count. Also report the file mtime/ctime of reproducing
files relative to the render time 2026-11-04T21:55:22.890Z.
Write {W}/ScoutRootsHost/host-map.tsv (name, candidate path, render match yes/no, cache hit yes/no,
mtime, ctime) and {W}/ScoutRootsHost/summary.md (roots with counts; names with no reproducing
candidate and why). Read-only outside your wave dir.
Acceptance: all 132 names classified; roots ranked by count; unreproducible names explained.
""")

ITEM["ExecModel"] = ("executor", f"""
You are the ONLY writer of {REPO}/verifiers/verify_harness_claims.py and
{REPO}/verifiers/omp-skill-roots.tsv. Make the lane's omp catalogue model match omp 18.15.0.
1. Derive the discovery rule yourself from the ELF source (see context), and use the scouts' packets
   as they land ({W}/ScoutRootsSource/source-packet.md, {W}/ScoutRootsHost/summary.md) — never a root
   you cannot tie to a located omp source quote. Update `USER_ROOTS`, `WALKUP_REL` and
   `discover_skills` (signature unchanged: `discover_skills(roots) -> (offered, dangling)`, first root
   wins unless the source says otherwise; a nested layout, plugin roots or globbed roots are handled
   inside `discover_skills` or by expanding `USER_ROOTS`). Touch `parse_frontmatter` only if a real
   fixture skill needs a frontmatter style it cannot read (show the file); touch `omp_key`/`preview`
   only if the 18.15.0 source differs (it should not: k=100, E=40, T=160, _=12). Keep every other
   behaviour; update the stale comments (the "Verified 2026-09-28 against the 17-name catalogue" line
   becomes a dated round-86 note citing omp 18.15.0).
2. Write {REPO}/verifiers/omp-skill-roots.tsv: header `root_pattern<TAB>binary_quote`, one row per root
   pattern your model reads, each quote the source text that makes omp read that root (>= 12 chars,
   verbatim in the ELF). No row for a root omp does not read.
3. The counter's G1 forbids, inside `discover_skills`/`parse_frontmatter`/`preview`/`omp_key`/
   `USER_ROOTS`/`WALKUP_REL`, any string containing `sessions`, `<skills>`, `.jsonl`, `catalogue.json`,
   `skill-descriptions.db`, and any 40+ char render literal anywhere. Do not read transcripts or the
   fixture from the model; it runs in a bwrap sandbox that hides them anyway.
4. Keep `python3 -B {REPO}/verifiers/verify_harness_claims.py --self-test` at exit 0 (add arms for the
   new roots/layout; report `N failure(s) over M assertions` before and after). Run the main CLI once
   and paste its tail (DRIFT rows vs the round-13 baseline are pre-existing; report any NEW crash).
5. Score the candidate exactly as the context says (scratch clone + commit + counter `--repo`), paste the
   full counter output (MISS lines included) into {W}/ExecModel/score.txt, and write
   {W}/ExecModel/CANDIDATE_READY containing the scratch commit hash, the sha256 of both files and the
   counter's last 6 lines. If N < 205, keep working until it holds or explain each remaining MISS.
Acceptance: counter on your candidate prints `omp catalogue lines reproduced N of 215` with N >= 205
and G1-G4 PASS, exit 0; self-test exit 0; every ledger row cites a located quote.
""")

ITEM["ScribeEntry"] = ("scribe", """
Write {REPO}/corpus/knowledge/omp-catalogue-model-round86.md — the knowledge entry C1 lands. Shape like
the lane's other entries: title; `source:` (the S-id ScribeSources assigns for the omp 18.15.0
embedded source — read {W}/ScribeSources/row.md for the id; until it exists write `S255` and verify
at the end), `verified-at: 2026-11-04`, `recheck: on-release` (omp upgrade), a `ground:` line; then:
1. What omp 18.15.0 renders per skill: `- name: render`, render = cached one-liner (key sha256(prompt ‖
   0 ‖ name ‖ 0 ‖ description), one line <= 160 chars and <= 12 words) else the deterministic preview
   (whitespace collapse; <= 100 chars verbatim; else first sentence within the first 99 chars if >= 40
   chars, no ellipsis; else last-space cut + `…`). Quote the located source lines from
   {W}/ScoutRootsSource/extract.txt (or locate them yourself in the ELF) with offsets.
2. Which roots omp reads, in what order and precedence — from {W}/ScoutRootsSource/source-packet.md
   and the final {REPO}/verifiers/omp-skill-roots.tsv (wait for {W}/ExecModel/CANDIDATE_READY).
3. A "what changed since the lane last looked" table: each earlier lane statement (grep the lane for
   `USER_ROOTS`, `17-name catalogue`, `every line of the newest block must byte-equal a cached`,
   `~/.omp/agent/skill-descriptions.db`, `_8n=100`, `H7s`, `cache.get(key) ?? previewSkillDescription`
   in SKILL.md and corpus/knowledge/*.md) with file:line, its claim, and verdict holds / changed /
   now-wrong with the 18.15.0 evidence. Do not edit those files; the L1 adds errata.
4. The measured before→after: base model 83 of 215, candidate N of 215 (copy from
   {W}/ExecModel/score.txt; never invent a number), and the counter command.
Every quote <= 25 words and present at the cited offset/line. Acceptance: the file; each quote
re-locatable; the errata table with file:line pointers.
""")

ITEM["ScribeSources"] = ("scribe", """
Registry work (sole writer of corpus/SOURCES.md and corpus/README.md).
1. Open the source this round: the omp 18.15.0 TypeScript embedded in /home/vgpnk/.local/bin/omp
   (sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f, `omp --version`). Locate
   the module header `// packages/coding-agent/src/extensibility/skill-descriptions.ts` and the skill
   discovery module(s) (ask nobody; search the bytes). Also check whether the upstream repository for
   omp (search the ELF for a github URL / package name, then `curl -sI` it) publishes the same file at
   a tag for 18.15.0; record the HTTP status. Write {W}/ScribeSources/fetch-record.txt with commands,
   offsets, sha256, HTTP status and a <= 25-word located quote.
2. Append ONE row to the `## Registry` table in {REPO}/corpus/SOURCES.md with the next free id (compute
   it: `grep -oE '^ {{0,3}}\\| S[0-9]{{3}}' corpus/SOURCES.md | sort | tail -1`), 11 cells: id | source
   (name, the ELF path + sha256 prefix, upstream URL if reachable) | `code` | `A` | scope "what this
   host's omp 18.15.0 does when it discovers skills and renders the <skills> catalogue" | anchor
   (module paths + byte offsets) | teaches (one sentence) | `mined` | `2026-11-04` | `on-release` |
   `corpus/knowledge/omp-catalogue-model-round86.md, verifiers/omp-skill-roots.tsv`. No literal `|`
   inside a cell; LF line endings; nothing else in the file changes. Record the id in
   {W}/ScribeSources/row.md.
3. Add rows to {REPO}/corpus/README.md § Coverage map for every new lane file this round lands that
   the corpus index requires (the knowledge entry; the lesson `corpus/lessons/round-86.md`) matching
   the existing row shape, and append one dated note under § Frontier's *Loader-rule freshness* row
   (append-only, below the table like the round-52/53 notes) stating the round-86 move with the counter
   command; never rewrite earlier notes.
4. Validate: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotoba` must exit 0 (no E rows); paste the tail into
   {W}/ScribeSources/census.txt; also `python3 -B {REPO}/verifiers/verify_corpus_integrity.py --json`
   and record corpus.index.* observed values (pre-existing reds recorded as-is).
Acceptance: the fetch record; one new row, census exit 0; README rows; row id recorded.
""")

ITEM["ScribeLesson"] = ("scribe", f"""
Write the round's lesson and log (sole writer of {REPO}/corpus/lessons/round-86.md, {REPO}/LOG.md and
append-only blocks in {REPO}/corpus/lessons/round-85.md).
1. corpus/lessons/round-86.md: intro (base {BASE}, freeze {FREEZE}, claim C1 verbatim from the plan);
   `## Gate` — the S-row opened this round (copy id, access date 2026-11-04, sha256, offset and the
   located quote from {W}/ScribeSources/fetch-record.txt once it exists), census before (exit 0, 33
   W04: {REPO}/.ufo/waves/round-86/receipts/census-round-start.txt) and after (L1 fills at the end:
   leave the line `census after: <L1>`), rows added/touched; the controls K0/K1/K2 and self-test with
   their receipts.
2. `## Mistakes` — exactly one mined mistake, with class · evidence pointer · captured-by · fix:
   the lane's catalogue check `omp_newest_catalogue` (verifiers/verify_harness_claims.py, the docstring
   at its def) assumed every catalogue line equals a cached description, so 132 lines from unknown
   roots read as a DRIFT count instead of a model failure for ~30 rounds; captured-by: none (no
   criterion required a model to reproduce the observed artefact it describes); fix: a QUALITY.md
   criterion proposal (write its text in the lesson; the L1 appends it) — "a model of an observed
   artefact is scored by reproducing that artefact line for line, and an unmodelled line counts
   against it" — and show it able to fail: the base model fails it (83 of 215).
3. `## Routed defects (r85 spot-check)` — one line per D1-D7 with the disposition the plan names.
   Write the append-only `## Correction, round 86` block in corpus/lessons/round-85.md for D1 (the
   coverage-map rows were 9 at the tip, counting command `git diff 1c8f37e cfcb9a4 --
   corpus/README.md | grep -c '^+| '`), D4 (LOG range is `:3088`–`:3235`, `wc -l` at cfcb9a4) and D5
   (202 884 B final size, `git cat-file -s cfcb9a4:corpus/SOURCES.md`) — run each command yourself and
   paste its output; never rewrite earlier text.
4. Append LOG.md entries (append-only, after the last line): `## Round 86` with the claim (surface,
   command, base 83 of 215, after value left as `<L1 fills>`), the intake (the S-row), the mistake, and
   the routed-defect dispositions.
Acceptance: files exist; every number has its command; LOG diff has zero deletions.
""")

ITEM["Connector"] = ("connector", """
Cross-lane and cross-source scan (read-only). Produce {W}/Connector/overlap.md:
1. Does any sibling lane hold omp skill discovery or catalogue rendering knowledge (read at their
   committed heads under /home/vgpnk/Projects/shokunin/*-shokunin: kumitate, kengaku, tameshi, kagi,
   kama, chousa — grep SKILL.md and corpus/knowledge for `skills>`, `USER_ROOTS`, `.agents/skills`,
   `skill-descriptions`)? For each hit: file:line, collision yes/no with this round's C1.
2. The staged package /home/vgpnk/Projects/shokuknow/merge/kotoba/ (read-only): which staged entries
   bear on omp/client skill discovery roots (e.g. `client-frontmatter-and-discovery-divergence.md`,
   `client-surface-census-extension.md`)? For each: does it assert anything about omp's roots that the
   18.15.0 source contradicts or confirms? Name ONE theme the lane could assimilate next round (not
   this round) and why; or say none fits.
3. considerthese: list proposals in {REPO}/considerthese/2026-10-26.md still unimplemented; this round
   touches none of them — confirm, and note whether C1 changes any of them.
4. One `no-absorb` line: what this lane must not claim because a sibling owns it.
Acceptance: table with file:line evidence; the assimilation candidate; the no-absorb line.
""")

ITEM["ReviewerRoots"] = ("reviewer", """
Independent non-author attack on C1's semantics. First, alone (do not read ExecModel's files yet),
derive from the omp 18.15.0 ELF which roots omp reads for skills, with located quotes (see context).
Then, when {W}/ExecModel/CANDIDATE_READY exists, judge {REPO}/verifiers/omp-skill-roots.tsv row by row:
is each quote the code (or setting default) that makes omp read that root — `sound` / `located but
irrelevant` / `wrong` with your reason and your own located quote. Then judge
{REPO}/verifiers/verify_harness_claims.py's diff against base (`git -C {REPO} diff
e5d966b51494f4177868ad5f46806a204783ef6c -- verifiers/verify_harness_claims.py`): does discovery now
follow omp's order and precedence, or does it reproduce lines by accident (e.g. a root omp does not
read that happens to hold identical copies)? Re-run the counter on the candidate yourself (scratch
clone, see context) and paste the last 6 lines.
Write {W}/ReviewerRoots/review.md with: your independent root table, the per-row verdicts, the
precedence verdict, your counter re-run, and a final line `C1 roots: sound | unsound (<reason>)`.
Acceptance: per-row verdicts with located quotes; the counter re-run; the verdict line.
""")

ITEM["ReviewerCounter"] = ("reviewer", f"""
Independent attack on the frozen instrument {REPO}/{COUNTER} (read-only; never edit it).
1. Predicate identity: compare the plan's predicate sentence ({REPO}/plans/round-86.md § C1) with the
   counter's code line by line (the printed headline, the 205 threshold, the guard set, exit ladder).
   Report every divergence.
2. Sandbox: from inside the same bwrap invocation the counter builds (read `run_module`/`default_hide`),
   test whether a module can still read any copy of the rendered catalogue: other session stores
   (~/.omp/agent/*.db not hidden, ~/.omp/agent/blobs, ~/.omp/agent/cache, ~/.cache, ~/.local/share,
   other agents' transcript dirs), the counter's own process via /proc, or network. Build each probe
   as a scratch module and score it with the counter (`--repo` scratch clone). Report each escape with
   the N it reaches.
3. Guards: try to reach N >= 205 with each guard satisfied by a world that skips the claimed work
   (G1 obfuscation, G2 a real old SKILL.md whose description happens to equal a render, G4 a quote that
   is located but irrelevant). Report the cheapest passing forgery, if any.
4. Fixture: confirm the fixture's 215 entries equal the `<skills>` block at line 7 of
   /home/vgpnk/.omp/agent/sessions/-Projects-shokunin/2026-11-03T17-37-19-922Z_01a1a27c-a432-71e1-944b-0900e4e7a66b/KakeR90.jsonl
   (decode the JSON line; compare) and that its cache rows were captured after the render (say whether
   a row added after 21:55:22Z could change a reproduced/missed verdict, and for which names).
Write {W}/ReviewerCounter/review.md + per-probe receipts. Acceptance: identity table; escape list with
N; fixture verdict.
""")

ITEM["Critic"] = ("critic", f"""
Falsify C1 with shortcut worlds scored on the frozen counter (scratch clones only; see context).
W-brute: a model whose USER_ROOTS are every host directory that holds a same-named SKILL.md for a
fixture name (computed by a script: find under $HOME, outside /home/vgpnk/Projects/shokunin), first match
wins — score it (a) with no ledger, (b) with a ledger citing, for each root, ANY >= 12-char ELF string
that merely contains a path fragment (e.g. `.agents/skills` or `SKILL.md`). Report N and exit for both.
W-alpha: the same roots sorted alphabetically. W-base+1: the base model plus only the single largest
missing root. W-candidate: ExecModel's candidate when {W}/ExecModel/CANDIDATE_READY exists.
Answer: (a) does any world that never read omp's discovery source reach the target, and with which
ledger? (b) what is the cheapest world that reaches it? (c) does the candidate name any root the
brute world needs but omp does not read (compare with {W}/ScoutRootsSource/source-packet.md)?
These numbers are the plan's Q71 disclosure: report them exactly, whatever they are.
Write {W}/Critic/worlds.md + per-world receipts. Do not edit production files.
""")

ITEM["MutTester"] = ("mutation-tester", f"""
Mutation battery, read-only on production files (work on copies in scratch).
A. The frozen counter {REPO}/{COUNTER}: apply at least 12 single-point mutants to a scratch copy (each
   guard disabled, the 205 threshold, the TOTAL check, the hide list emptied, the scratch list emptied,
   the ctime check dropped, G4 quote-location check dropped, G4 pattern match always-true, the cache
   precedence swapped (preview before cache), render comparison loosened to strip()). For each mutant
   run the copy's `--self-test`: killed (self-test fails) or survived. A survivor is a counter defect —
   name it; for each survivor also show whether a real forgery world exploits it.
B. The candidate model (when {W}/ExecModel/CANDIDATE_READY exists): mutate it (drop each added root,
   reorder roots, break the nested-layout handling, preview cut 99->100, sentence floor 40->39) and
   score each mutant with the real counter (scratch clone). Each must drop N or flip a guard; a mutant
   that keeps N >= 205 shows a part of the model the measure does not test — name it.
Write {W}/MutTester/mutants.md (table: mutant, expected, observed, killed/survived) + receipts.
""")

ITEM["Sentinel"] = ("sentinel", f"""
Security review (read-only on production files).
1. {REPO}/{COUNTER}: it executes revision-selected code. Verify the bwrap invocation (`run_module`):
   read-only root bind, which paths are hidden, whether the module can write anywhere persistent
   (home, the lane, /dev/shm, the box dir), network access, and whether `--die-with-parent` plus the
   600 s timeout bound it. Name file:line for each finding; propose (do not apply) fixes.
2. {REPO}/verifiers/fixtures/omp-catalogue-r86/catalogue.json (committed): grep it for credential
   shapes (api keys, `sk-`, `ghp_`, `AKIA`, bearer tokens, emails, private paths beyond $HOME skill
   paths) and for any third-party content whose redistribution is a concern (skill descriptions are
   short public strings — say if any is not).
3. ExecModel's changes (when CANDIDATE_READY exists): does the model now read new paths at import
   time, follow symlinks out of a root, or execute anything? Any path traversal from a malformed
   SKILL.md name?
4. Confirm no seat wrote outside its own wave dir: `git -C {REPO} status --porcelain` and
   `git -C /home/vgpnk/Projects/shokunin status --porcelain` (report only paths naming kotoba/round-86).
Write {W}/Sentinel/audit.md (id, file:line, severity, verdict) ending with `no new fail-open` or the
defect.
""")

ITEM["RevengerPrecedence"] = ("revenger", """
One falsifiable hypothesis: when the same skill name exists under two roots omp reads, omp 18.15.0
renders the copy from the root it scans first, and the fixture shows it. Test it: from the fixture
{REPO}/verifiers/fixtures/omp-catalogue-r86/catalogue.json pick every name whose SKILL.md exists in
two or more host roots with DIFFERENT descriptions (find them; compute previews with the lane's
`preview`), and for each say which copy the rendered line matches. Then locate in the ELF source the
code that decides (dedupe key, first-wins or last-wins, provider priority numbers) with offsets and
quotes. Verdict: `first-scanned wins` / `other rule: <rule>` / `unresolved`, with the evidence table.
Write {W}/RevengerPrecedence/probe.md. Read-only.
""")

ORDER = ["ScoutRootsSource", "ScoutRootsHost", "ExecModel", "ScribeEntry", "ScribeSources",
         "ScribeLesson", "Connector", "ReviewerRoots", "ReviewerCounter", "Critic", "MutTester",
         "Sentinel", "RevengerPrecedence"]


def main():
    items = []
    for name in ORDER:
        role, body = ITEM[name]
        body = body.replace("{REPO}", REPO).replace("{W}", W).replace("{{", "{").replace("}}", "}")
        prompt = "/skill:godspeed\n\n" + CONTEXT + body
        items.append({"name": name, "role": role, "prompt": prompt})
    spec = {
        "wave": WAVE,
        "milestone": "r86-w1: C1 freshness — the lane's omp catalogue model re-derived against omp 18.15.0 "
                     "(83 of 215 -> target >= 205 under the frozen sandboxed counter), sourced on the ELF's "
                     "embedded source; 4 strict attack seats + sentinel + revenger falsify it.",
        "reportDir": ".ufo/waves/round-86/w1",
        "context": CONTEXT,
        "items": items,
    }
    out = os.path.join(REPO, ".ufo/waves/round-86", WAVE + "-spec.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, indent=1, ensure_ascii=False)
    print(out, len(items), "items", sorted({i["role"] for i in items}))


if __name__ == "__main__":
    main()
