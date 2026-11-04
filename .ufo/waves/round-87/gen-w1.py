#!/usr/bin/env python3
"""Generate the round-87 wave-1 spec (14 seats) for the v1 swarm validator.

Every seat prompt is self-contained; the shared context carries the bounds,
the frozen state and the file-ownership map.
"""
import json
from pathlib import Path

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = f"{LANE}/.ufo/waves/round-87/w1"
SCRATCH = "/fast/scratch/hyaku/kotoba-r87"
BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
FREEZE = "669f2801c31ef27e18cc35a327d2e18f466281c7"

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only) or /home/vgpnk/Projects/shokuknow (read-only: read it, never write,
fetch or run a campaign tool there).
Scratch: create ONE dir {SCRATCH}/<your-seat-name>/ (mkdir -p), export TMPDIR to it and pass it to any
--work, delete it with `trap 'rm -rf -- "$S"' EXIT` (or finally:) before you yield; copy receipts first
under {WAVE}/<your-seat-name>/. /tmp only for files < 50 MB.
VCS: never run a git/jj write in the lane or the fleet (no add/commit/stash/checkout/reset/jj
mutation); read-only git (log, show, diff, status, ls-files, rev-parse, cat-file, archive) is fine.
A scratch repo is created only as `D=$S/repo && git clone -q --shared {LANE} "$D"`, every later git
call names `-C "$D"`, and `git -C "$D" rev-parse --show-toplevel` must equal $D before your first
commit there. Never touch {LANE}/../.ufo, MANIFEST.json, scripts/, templates/, .ufo/state/,
.ufo/watchdog.log or another lane. Message only agent://KotobaR87 (never agent://all).
Never write outside the files your item names; production files have one owner each (below).
Security: never write a raw environment dump, credential or token into the lane.
Tooling authorization (operator 2026-10-19): you may install or upgrade tools that help the task;
read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record
tool/version/channel/reason in your answer). PACMAN IS PAUSED host-wide: no pacman transaction of any
kind (no -S/-Sy/-Syu/-U/-R); use uv tool / npx / an official binary in ~/.local/bin, or report the need.
Your final answer is a short JSON: files_written, evidence (commands + observed lines), findings, risks.

## Frozen state (round 87, Linux host, omp/18.15.0)
Base {BASE}; freeze {FREEZE} = `plans/round-87.md` alone, committed before any candidate data.
Read {LANE}/plans/round-87.md first; it is both claims' single source of truth. The predicate
sentences, targets and kill rule are FROZEN: nobody edits them; a counter defect is a finding.
C1 (depth): `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` prints
`omp root semantics grounded N of 13`, exit 0 iff N == 13 and guards S1-S3 PASS. New ledger
`verifiers/omp-skill-roots-semantics.tsv` (header
`root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`), 13 rows whose `root_pattern` equals
the round-86 ledger `verifiers/omp-skill-roots.tsv`'s 13 patterns. Conjuncts per row: pattern
(unchanged, no `..`, no wildcard in the first segment), reader (`reader_quote` >= 12 chars occurs in
the omp ELF on a line carrying a path-join token), module (`// packages/<module>` header occurs in
the ELF before the reader quote), bound (`{{cwd}}/` expansion excludes $HOME unless the row is a
`~/` row; a `..` candidate root never matches).
The round-86 ledger and its counter `verifiers/check_omp_catalogue_repro.py` are OUT OF SCOPE: that
frozen counter requires exactly two tab-separated cells per ledger row, so a third column there
would turn its G4 red. Never edit either file.
C2 (consistency): `python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>` prints
`r86 routed defects closed N of 5`, exit 0 iff N == 5. Items D1-D5 are in plans/round-87.md § C2.
omp 18.15.0 ships its TypeScript source inside the ELF (bun bundle): 277 MB at
/home/vgpnk/.local/bin/omp, sha256 6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f.
Read it with python mmap + re (never copy it into the lane). Round-86 evidence is readable:
{WAVE.replace('/w1','')}/round-86/ (receipts, w1 seat reports, the roots review).
File ownership: ExecSemantics owns verifiers/check_omp_root_semantics.py; ExecLedger owns
verifiers/omp-skill-roots-semantics.tsv; ExecRepairs owns verifiers/check_r86_routed_repairs.py;
ExecD1D5 owns the D1 receipts and the D5 corpus-integrity repair; ScribeEntry owns
corpus/knowledge/omp-root-semantics-round87.md; ScribeSources owns corpus/SOURCES.md and
corpus/README.md; ScribeLesson owns corpus/lessons/round-87.md, corpus/lessons/round-86.md
(append-only block only), corpus/QUALITY.md and LOG.md. SKILL.md, SCORECARD.md, plans/ and
everything else are integrated by the L1.
Every other seat writes only under {WAVE}/<its-seat-name>/.
Handoff files in {WAVE}/: `LEDGER_READY` (ExecLedger), `COUNTERS_READY` (ExecSemantics and
ExecRepairs), `ELF_MAP.tsv` (ScoutElf), `SOURCE_RECORD.txt` (ScoutPlugin). Do your independent work
first, then check for the file you need every 2 minutes (sleep 120) for up to 45 minutes; if it never
appears, report on what exists and say so.
Instrument conventions: Python stdlib only, `python3 -B`, honour TMPDIR and accept a scratch argument,
exit ladder 0 pass / 1 content fail / 2 could-not-evaluate, `--self-test` prints
`0 failure(s) over N assertions`."""

ITEMS = [
    dict(
        role="scout",
        name="ScoutElf",
        prompt=f"""## ScoutElf — the ELF evidence map for the 13 roots (feeds C1 conjuncts 2 and 3)

Read the round-86 ledger {LANE}/verifiers/omp-skill-roots.tsv (13 rows, `root_pattern` +
`binary_quote`) and the round-86 roots review {LANE}/.ufo/waves/round-86/w1/ReviewerRoots/review.md
(it rejects three of the doc quotes and names the real plugin reader).

For EACH of the 13 rows, locate in the installed omp 18.15.0 ELF (/home/vgpnk/.local/bin/omp,
python mmap + re, read-only, never copy the file):
1. the source module the root is read by — the module header comment of the form
   `// packages/<path>.ts` that precedes the code, and its byte offset;
2. the reader code line that BUILDS that root — a line that carries a path-join token
   (`join(`, `.join(`, `resolve(`, `path.join`) AND the root's literal dot-segment token
   (`.agents`, `.omp`, `.claude`, `.codex`, `.opencode`, `.agent`, `.github`, `managed-skills`),
   with its byte offset. Quote >= 12 chars, verbatim, one line, no paraphrase;
3. whether the round-86 `binary_quote` for that row is a doc/string-table line or a code line
   (state which, with the offset you found).

Write {WAVE}/ScoutElf/ELF_MAP.tsv with the header
`root_pattern<TAB>module<TAB>module_offset<TAB>reader_quote<TAB>reader_offset<TAB>binary_quote_class`
and exactly 13 data rows, plus {WAVE}/ScoutElf/receipts.txt holding the mmap commands and their
observed output lines. Where no code line can be found for a root, write `NONE` in the reader cells
and say why in the receipt — an honest `NONE` is worth more than a fabricated quote (the round-86
CF1 finding says the plugin root may have no `.omp/plugins` literal: look for the actual
`join(` call the reviewer named, not for the pattern's own text).

Acceptance: 13 rows present; every non-NONE reader_quote re-finds verbatim in the ELF at the offset
you give (`python3` mmap re-read, pasted); every module header offset precedes its reader offset.
Write ELF_MAP.tsv before your other work is polished — ExecLedger is blocked on it.""",
    ),
    dict(
        role="scout",
        name="ScoutPlugin",
        prompt=f"""## ScoutPlugin — the plugin registry branch and the new SOURCES row's fetch record

Two jobs, both read-only outside your wave dir.

1. **Bind the plugin registry branch (round-86 CF3/P4).** The round-86 closure found that its bwrap
   sandbox hid the plugin registry files, so the scored branch was the model's non-omp fallback.
   Establish, on this host: which files under `~/.omp/plugins/` omp reads to enumerate plugin skills
   (list the directory tree to depth 4, with sizes), which of them the round-86 counter's hide list
   would hide (read the hide list in {LANE}/verifiers/check_omp_catalogue_repro.py), and whether
   `~/.omp/plugins/node_modules/*/skills/*/SKILL.md` still yields the 132 catalogue names the
   round-86 review measured. Commands and observed counts into {WAVE}/ScoutPlugin/registry.txt.

2. **The fetch record for C1's new source row.** C1 is a sourced claim: it needs one
   `corpus/SOURCES.md` row opened THIS round on the omp skill-loader module the ELF embeds.
   - Identify the module from the ELF header (e.g. `// packages/coding-agent/src/skills/...`) that
     builds the roots — coordinate with ScoutElf's `ELF_MAP.tsv` if it exists (poll every 2 min).
   - Re-open it upstream: `https://raw.githubusercontent.com/can1357/oh-my-pi/v18.15.0/<module>`
     (tag v18.15.0 of https://github.com/can1357/oh-my-pi). Record the HTTP status, the byte size,
     the sha256 of the fetched bytes, and a located quote of <= 25 words that names a root the
     ledger carries. If the tag path 404s, try the repo's default branch and say which you read.
   - Write {WAVE}/ScoutPlugin/SOURCE_RECORD.txt: url, access date 2026-11-04, http status, bytes,
     sha256, the located quote, the line number in the fetched text, and the ELF offset of the same
     bytes. ScribeSources turns this into the row; do not edit corpus/SOURCES.md yourself.

Also measure, for the L1's considerthese item, `SKILL.md`: `wc -l`, `wc -c`, the count of lines over
120 chars, over 300 chars, and the longest line length — commands and output into
{WAVE}/ScoutPlugin/skill-size.txt.

Acceptance: registry.txt carries real counts (not estimates); SOURCE_RECORD.txt carries an HTTP
status and a sha256; skill-size.txt carries five numbers with their commands.""",
    ),
    dict(
        role="executor",
        name="ExecSemantics",
        prompt=f"""## ExecSemantics — write the C1 counter `verifiers/check_omp_root_semantics.py`

The only file you own: {LANE}/verifiers/check_omp_root_semantics.py. Never edit the ledger
(ExecLedger owns it), the round-86 ledger, or `check_omp_catalogue_repro.py`.

Frozen predicate (docstring, `--rev` behaviour and every receipt must say the same sentence):
    python3 -B verifiers/check_omp_root_semantics.py --rev <rev>
        -> prints "omp root semantics grounded N of 13", exit 0 iff N == 13 and guards S1-S3 all
           PASS; exit 1 otherwise; exit 2 = could-not-evaluate.

Read {LANE}/plans/round-87.md § C1 for the four conjuncts and the three guards, verbatim.
Implementation notes:
- Read `verifiers/omp-skill-roots-semantics.tsv` and `verifiers/omp-skill-roots.tsv` at `<rev>`
  with `git -C <repo> show <rev>:<path>` (committed bytes only; the worktree is never the source).
- The ELF is /home/vgpnk/.local/bin/omp; sha256 must equal
  `6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f` else exit 2. Read it with
  mmap; never copy it. Locate a quote by finding its line (bounded window, e.g. the enclosing
  newline-delimited slice) and require the line to carry a JOIN_TOKENS member.
- The bound probe (conjunct 4) runs on a frozen synthetic ancestor chain, no host dependency:
  session cwd `/home/u/proj/sub`, HOME `/home/u`, ancestors `/home/u/proj`, `/home/u`, `/home`, `/`.
  A `{{cwd}}/` row's expansion set must be exactly the ancestors strictly below `$HOME` plus the cwd
  itself; a `~/` row expands from `$HOME`. Any candidate root whose normalized form still contains a
  `..` segment must match no row.
- A missing ledger or a missing cell at `<rev>` is a CONTENT verdict (exit 1, N lower), never exit 2
  (round-68 routed defect R67-1).
- `--self-test` builds synthetic worlds under $TMPDIR / --work and must print
  `0 failure(s) over N assertions`. Required arms, each of which must FAIL the way it names:
  `w_noledger`, `w_docquote` (doc line in reader_quote), `w_nomodule`, `w_dotdot`, `w_star`,
  `w_shrink` (12 rows), `w_bound` (a `{{cwd}}/` row reaching $HOME), `w_quote_miss`, `w_offset_order`
  (module header after the quote), plus the honest world (13 grounded rows) passing.
- Honour TMPDIR and a `--work` argument; no hardcoded /tmp; stdlib only; `python3 -B`.
- Also run it against the base {BASE}: it must print `0 of 13` and exit 1 (write that receipt into
  your wave dir as `base.txt`).

Acceptance: `--self-test` exit 0 with the arm count; `--rev {FREEZE}` reads `0 of 13` exit 1; and
once {WAVE}/LEDGER_READY exists (poll every 2 min, up to 45 min) `--rev <worktree state>` on a
scratch clone holding the ledger prints `13 of 13` exit 0 — or you report exactly which rows fail and
why. Write {WAVE}/COUNTERS_READY when the counter is runnable.""",
    ),
    dict(
        role="executor",
        name="ExecLedger",
        prompt=f"""## ExecLedger — write the new semantics ledger `verifiers/omp-skill-roots-semantics.tsv`

The only file you own: {LANE}/verifiers/omp-skill-roots-semantics.tsv. NEVER edit
`verifiers/omp-skill-roots.tsv` or `verifiers/check_omp_catalogue_repro.py` (the round-86 frozen
counter requires exactly two tab cells per row).

Header, exactly: `root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`
13 data rows, one per row of the round-86 ledger, in the same order, with the same `root_pattern` and
`binary_quote` cells copied byte for byte (`git show {BASE}:verifiers/omp-skill-roots.tsv`), plus:
- `module` — the source module path from ScoutElf's `ELF_MAP.tsv` (e.g.
  `coding-agent/src/skills/index.ts`), no leading `packages/`;
- `reader_quote` — the located code line that builds that root (>= 12 chars, one line, verbatim,
  containing a path-join token and the root's dot segment). Never a doc/string-table line: the
  round-86 closure's CF1 finding is exactly that doc quotes cannot ground a root.
Where ScoutElf reports `NONE` for a root, still write the row with `NONE` and say so in your receipt;
do not invent a quote and do not drop the row (guard S3 counts 13).

Verify every reader_quote yourself with a fresh python mmap re-read of the ELF at the offset you
write (do not trust ELF_MAP.tsv blindly); a quote that does not re-find is a `NONE`.
Poll {WAVE}/ScoutElf/ELF_MAP.tsv every 2 minutes (sleep 120) for up to 45 minutes if absent; if it
never appears, derive the map yourself and say so.

Write {WAVE}/ExecLedger/receipts.txt (the re-read commands and their observed offsets) and then
{WAVE}/LEDGER_READY (13 rows, how many grounded, how many `NONE`). ExecSemantics is blocked on it.

Acceptance: 13 rows; every non-NONE quote re-finds verbatim in the ELF; the file's first line is the
exact header; `cut -f1` of your file equals `cut -f1` of the round-86 ledger.""",
    ),
    dict(
        role="executor",
        name="ExecRepairs",
        prompt=f"""## ExecRepairs — write the C2 counter `verifiers/check_r86_routed_repairs.py`

The only file you own: {LANE}/verifiers/check_r86_routed_repairs.py.

Frozen predicate:
    python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>
        -> prints "r86 routed defects closed N of 5", exit 0 iff N == 5;
           exit 1 otherwise; exit 2 = could-not-evaluate.

Read {LANE}/plans/round-87.md § C2 for D1-D5, and
{LANE}/corpus/lessons/round-86-verifier-spotcheck.md § 6 for the defects themselves. Each item is
recomputed from `<rev>`'s committed bytes (git show / git cat-file), never from the worktree:
- D1: `.ufo/waves/round-86/receipts/tip-catalogue.txt` and `tip-registry.txt` exist at `<rev>`; each
  names the measured revision in its own text, carries `exit=0` and the expected line
  (`omp catalogue lines reproduced 215 of 215` / `gate registry rows conformant 67 of 67`); and the
  blobs of `verifiers/check_omp_catalogue_repro.py` and `verifiers/check_gate_registry.py` are equal
  between `04647b0f715ff3c4f314b0d8f03dea28bc453688` and `<rev>` (so the reading carries).
- D2: the lane record (plans/round-87.md or corpus/lessons/round-87.md) carries the sentence
  `planner/distiller/labrat/Main are frozen-topology seats and can never be swarm lanes.` verbatim;
  the counter re-reads /home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs (exit 2 if
  absent), confirms that sentence occurs there, and confirms `planner` is not in `SWARM_ROLES`
  (parse the set literal, do not grep a substring).
- D3: `corpus/lessons/round-87.md` `## Gate` holds >= 1 row whose decision cell is `reject` with a
  reason of >= 8 words.
- D4: `plans/round-87.md` contains `after the first candidate score` verbatim.
- D5: run the revision's `verifiers/verify_corpus_integrity.py` in a scratch shared clone of `<rev>`
  (never in the lane) and require exit 0 with `9/9 checks pass`; a clone that cannot run it is
  exit 2, a red run is a content fail (Q63: never relocate a gate whose `../` tokens die).
`--self-test` prints `0 failure(s) over N assertions` and carries at least: `w_prose` (five items
mentioned in prose only), `w_wrongrev` (a receipt naming another revision), `w_gateprose` (a
"rejected" mention inside a paragraph), `w_norepair` (integrity still red), plus the honest world
passing. Honour TMPDIR and `--work`; stdlib only; `python3 -B`.
Run it against the base {BASE}: it must print `0 of 5` exit 1 (receipt `base.txt` in your wave dir).

Acceptance: self-test exit 0; base reads `0 of 5`; the five items are recomputed, not asserted.
Write {WAVE}/COUNTERS_READY when runnable.""",
    ),
    dict(
        role="executor",
        name="ExecD1D5",
        prompt=f"""## ExecD1D5 — the D1 tip receipts and the D5 corpus-integrity repair

Two jobs, both production work.

1. **D1 tip receipts (round-86 § 6.1).** Run, capturing each command's OWN exit status
   (`cmd >> f 2>&1; rc=$?; printf 'exit=%s\\n' "$rc"`), against the lane tip at the time you run
   (`git -C {LANE} rev-parse master`):
   - `python3 -B verifiers/check_omp_catalogue_repro.py --rev <tip>` →
     {LANE}/.ufo/waves/round-86/receipts/tip-catalogue.txt
   - `python3 -B verifiers/check_gate_registry.py --rev <tip>` →
     {LANE}/.ufo/waves/round-86/receipts/tip-registry.txt
   Each file's first lines must name the measured revision and the instrument's sha256. The
   catalogue counter needs bwrap and takes minutes; give it 1800 s and honour TMPDIR. If it cannot
   run (no bwrap, ENOSPC), write the failure verbatim and say so — do not fabricate a reading.
   Do not edit any file under `.ufo/waves/round-86/` other than adding these two receipts.

2. **D5 the carried base red (round-86 § 6.7).** At base {BASE},
   `python3 -B verifiers/verify_corpus_integrity.py` reads `3/9 checks pass` with six DRIFTs
   (`corpus.index.tracked_files`, `corpus.index.unindexed`, `corpus.pointers.report_total`,
   `corpus.pointers.report_dead`, `corpus.pointers.commit_total`,
   `corpus.pointers.commit_unresolvable`). Clear them the way the gate's own contract allows:
   - an index row for the genuinely new corpus file (the cause, not the symptom);
   - the baseline re-recorded from the gate's own `--no-baseline --json` measurement (the r67
     practice) for counts that grew by intent;
   - a REAL repair for `report_dead` and `commit_unresolvable`: find the dead report pointer and the
     unresolvable commit citation, and fix the citation itself (never re-record a dead pointer green).
   Files you may edit: {LANE}/verifiers/corpus-baseline.json, {LANE}/corpus/README.md's coverage-map
   index rows ONLY (append rows; do not touch § Frontier — ScribeSources owns it), and the single
   offending citation line in whichever lane file the gate names. Name every edit in your receipt.
   Never re-record the baseline to hide a dead pointer (Q64).

Acceptance: `python3 -B verifiers/verify_corpus_integrity.py` exits 0 with `9/9 checks pass` in the
lane worktree, and `--json` shows every check PASS; the receipt lists each DRIFT with its
before→after observed value and the exact edit that moved it. If one DRIFT cannot be cleared without
touching another owner's file, leave it red and report which and why (an honest partial is worth
more than a laundered green).""",
    ),
    dict(
        role="scribe",
        name="ScribeEntry",
        prompt=f"""## ScribeEntry — `corpus/knowledge/omp-root-semantics-round87.md`

The only production file you own: {LANE}/corpus/knowledge/omp-root-semantics-round87.md.
Write the domain knowledge C1 lands: **which code reads each omp skill root, and what bounds that
reading** — not a log of the round.

Required shape (CORPUS.md + QUALITY Q12: the `source:` block is the entry's opening):
- `source:` (the new SOURCES row id from ScoutPlugin's record — poll {WAVE}/ScoutPlugin/SOURCE_RECORD.txt
  every 2 min up to 30 min; if absent, write the entry citing S255 plus the ELF offsets and say the
  new row is pending), `verified-at:` the ELF sha256 and host, `recheck:` cadence.
- A 13-row table: `root_pattern | module | reader_quote (<= 25 words, verbatim) | bound`. Every
  reader_quote comes from ExecLedger's ledger (poll {WAVE}/LEDGER_READY) and must re-find in the ELF;
  rows ExecLedger marks `NONE` are stated as `no code quote located` with the reason, never filled
  with a doc string.
- Three rule rows a skill author can act on: (a) a root claim is grounded by the code that joins the
  path, not by a doc string that mentions the directory; (b) `{{cwd}}/` walk-up stops below `$HOME`,
  so a project-scoped root is not a home root; (c) a `..` segment never matches a root pattern.
- A `## Bound` line: what this entry does not claim (no client run beyond the round-86 catalogue
  capture; the plugin registry branch is documented from files, not observed).
Cite with located quotes and offsets; no paraphrase presented as a quote. Append-only rules apply.

Acceptance: provenance trio; 13 rows; >= 3 rule rows; every quote re-finds at the offset the entry
gives (paste the re-find commands in your answer).""",
    ),
    dict(
        role="scribe",
        name="ScribeSources",
        prompt=f"""## ScribeSources — the `corpus/SOURCES.md` row and the `corpus/README.md` frontier note

Files you own: {LANE}/corpus/SOURCES.md (append one row) and {LANE}/corpus/README.md (one
append-only note under § Frontier; never rewrite an existing row).

1. Read {LANE}/CORPUS.md § SOURCES.md contract v1 and the registry's existing rows
   (`grep -n '^| S' {LANE}/corpus/SOURCES.md | tail -3`) for the exact 11-column shape. The next free
   id is S256 unless the tail says otherwise; check with
   `grep -oE '^ {{0,3}}\\| S[0-9]{{3}}' {LANE}/corpus/SOURCES.md | sort | tail -1`.
2. Build the row from {WAVE}/ScoutPlugin/SOURCE_RECORD.txt (poll every 2 min up to 40 min): the omp
   skill-loader module re-opened upstream at tag v18.15.0, tier A, `kind: code`, status `mined`,
   opened 2026-11-04, recheck `on-release`, `used-by` naming
   `corpus/knowledge/omp-root-semantics-round87.md` and `verifiers/omp-skill-roots-semantics.tsv`.
   The anchor cell carries the fetched bytes' sha256 and the located quote (<= 25 words) — one cell,
   no literal or escaped `|` anywhere in the row (the census parses 11 columns).
3. Append-only: one `+| ` line, nothing else moved. Then run
   `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`
   and paste its exit code and last line; `W04` warnings are allowed, an `E` row is not.
4. `corpus/README.md`: append one note under § Frontier advancing the loader-rule row with this
   round's per-root code grounding (entry path, counter command, the 13-row count) — append only, no
   row rewrite, and do not touch § Adjacent.
If the SOURCE_RECORD never appears, do not invent a row: report `row not appended` with the reason.

Acceptance: exactly one new row with a resolvable id, census exit 0, one appended frontier note,
`git diff --numstat` for both files showing insertions only.""",
    ),
    dict(
        role="scribe",
        name="ScribeLesson",
        prompt=f"""## ScribeLesson — `corpus/lessons/round-87.md`, the r86 correction block, `QUALITY.md` and `LOG.md`

Files you own: {LANE}/corpus/lessons/round-87.md (new), {LANE}/corpus/lessons/round-86.md
(one APPEND-ONLY block; never rewrite a committed line), {LANE}/corpus/QUALITY.md (append one
criterion row), {LANE}/LOG.md (append the round-87 entry).

1. `corpus/lessons/round-87.md` must carry:
   - the round's claims verbatim from {LANE}/plans/round-87.md (predicate sentence, target, base);
   - `## Gate` — candidates, admitted, **and at least one REJECTED row with a reason of >= 8 words**
     (the round-86 closure's § 6.3 defect: a Gate with no reject row hides the round's taste). A
     real rejection from this round is required — mine the wave seats' findings
     ({WAVE}/*/ and the seat reports) for a candidate claim, quote or source that was refused, and
     record it with its reason. If the round truly has no rejection, record the closest gate
     decision (e.g. a `NONE` reader row refused as a grounding) and say so — never invent one;
   - the census before and after lines with exit codes;
   - `## Mistakes` — ONE mined mistake: class · evidence pointer · captured-by (the criterion or rule
     that should have caught it, or `none`) · fix, and the fix shown able to fail (a command whose
     output is pasted). Candidates: the r86 ledger's doc quotes that could not ground the plugin root
     (CF1) surviving a round; the base corpus-integrity drift growing from 8/9 to 3/9 while round 86
     reported it as carried; the round-86 tip after-values cited without receipts (r85 D2 recurrence).
     Pick one, measure it, and paste the sweep that found it.
2. `corpus/lessons/round-86.md` append-only block: the r86 § 6.5 correction — the r74 precedent cited
   for the r86 addendum amended the PLAN, not the counter (the round-74 counter sha256 is identical
   in both freeze receipts), so the r86 addendum's real precedent is the "amended before any data"
   principle, and this round's kill rule states the boundary as `after the first candidate score`.
   Append; never edit the committed sentence.
3. `corpus/QUALITY.md`: append ONE criterion row (Q78) from `considerthese/2026-10-26.md` proposal 1
   (a size ceiling on `SKILL.md`), grounded in your own measurement of
   {WAVE}/ScoutPlugin/skill-size.txt (poll every 2 min up to 30 min; measure `wc -l`, `wc -c`,
   lines > 120 chars, longest line yourself if the file is absent): a ceiling is a RATCHET measured
   at the freeze and never a promise, and a floor that is red at base cannot land. Cite
   `considerthese/2026-10-26.md` + the date in the evidence cell.
4. `LOG.md`: append the round-87 entry in the file's existing shape (round header, claims, measured
   values, landed commits, routed defects) — read the last 60 lines for the shape first.
Never edit SCORECARD.md (the L1 integrates it) and never touch another lane's lesson.

Acceptance: the four files carry insertions only (`git diff --numstat`), the Gate has a reject row,
Mistakes has one row with a failing-fix command, and the Q78 row cites considerthese + date.""",
    ),
    dict(
        role="connector",
        name="Connector",
        prompt=f"""## Connector — sibling-overlap scan and the planning data-walk

Two jobs, both read-only in production.

1. **Sibling-overlap scan (mandatory).** The round's new ground is "which code reads an agent client's
   skill roots and what bounds that reading". Read the neighbouring lanes' `PROVINCE.md` descriptions
   at their current tips (fleet root /home/vgpnk/Projects/shokunin/<lane>-shokunin/, lanes: kumitate
   (orchestration/tooling), kagi (secrets/vault ops), kama (local model serving), kengaku (LLM eval),
   chousa (research), tsukoroi/tsukuroi if present) and decide for each whether this round's ground
   is contested, adjacent or none. Use the lane's own guard:
   `python3 -B {LANE}/verifiers/check_sibling_census.py {LANE}/corpus/knowledge/sibling-overlap-census-round49.md --province {LANE}/PROVINCE.md`
   and report its output. Do NOT absorb another lane's evidence: name it and route it.
   Write {WAVE}/Connector/overlap.md with a 6-row table (lane | class | basis | routing).

2. **Planning data-walk (the L1's planner duty rides here).** Walk the two claims' data paths and
   report where the plan is under-determined:
   - does `~/.omp/plugins/node_modules/*/skills` really yield the 132 names the round-86 review
     measured (count them yourself; the round-86 review's number is a pointer, not evidence)?
   - are the 13 ledger patterns actually the roots omp walks, or does the list miss a root the ELF
     reads (sweep the ELF for `skills` joins and compare against the 13)?
   - does the C2 item set D1-D5 each name one recomputable fact, or does any item assert a prose
     property (that is the class the r86 closure refused)?
   Write {WAVE}/Connector/plan-walk.md with the three answers, each carrying its command and output.

Acceptance: overlap.md has the 6 rows and the census command's output; plan-walk.md answers all
three with measured values (a count, a diff, a per-item verdict).""",
    ),
    dict(
        role="reviewer",
        name="ReviewerC1",
        prompt=f"""## ReviewerC1 — attack C1's four conjuncts

Target: {LANE}/verifiers/check_omp_root_semantics.py and
{LANE}/verifiers/omp-skill-roots-semantics.tsv (poll {WAVE}/COUNTERS_READY and {WAVE}/LEDGER_READY
every 2 min, up to 45 min; if a file never appears, review what exists and say so).

Build an INDEPENDENT implementation of the four conjuncts (your own code, in your wave dir, reading
the same committed bytes and the same ELF) and compare its per-row verdict with the counter's. Then
attack, each world built in your scratch dir and scored on the FROZEN counter (never edit it):
1. a `reader_quote` that is a doc/string-table line but whose surrounding 200 bytes happen to
   contain a join token — does conjunct 2 admit it? (the round-86 CF1 class);
2. a `reader_quote` from the wrong module (header precedes it, but the code belongs to another
   reader) — does conjunct 3 catch it?
3. a `{{cwd}}/` row whose expansion set reaches `$HOME` — does conjunct 4 refuse it?
4. a `..` candidate root that normalizes onto a legitimate row — does the matcher refuse it?
5. a 13-row ledger where one `NONE` row is replaced by a plausible fabricated quote that is not in
   the ELF — refused?
Report each attack as `world | conjunct | observed (N of 13, exit) | verdict: refused/admitted`.
An admitted world is a finding that bounds the claim: say so plainly, name the conjunct, and do not
propose a post-data patch (the predicate is frozen; the finding is the deliverable).
Also verify the counter's own base reading: `--rev {BASE}` must print `0 of 13` exit 1.

Acceptance: your independent per-row table (13 rows, grounded yes/no) beside the counter's, the five
attack rows with observed values, and a one-line verdict `C1 conjuncts: sound / bounded by X`.""",
    ),
    dict(
        role="critic",
        name="Critic",
        prompt=f"""## Critic — falsify both claims' predicates (do-nothing and script-only worlds)

Targets: {LANE}/verifiers/check_omp_root_semantics.py (C1) and
{LANE}/verifiers/check_r86_routed_repairs.py (C2) — poll {WAVE}/COUNTERS_READY every 2 min, up to
45 min; if it never appears, critique {LANE}/plans/round-87.md's frozen predicates instead and say so.

The question is not "do the counters run" but "can a world that does no claimed work reach the
target?" Build, in your scratch dir, and score on the FROZEN counters:
1. **Do-nothing world for C1**: keep the round-86 ledger as-is, add a `reader_quote` column filled
   with the existing `binary_quote` doc lines. Expected: < 13. Observed?
2. **Script-only generator world for C1 (Q71/Q74)**: a script that mechanically picks, for each row,
   any ELF line containing a join token and the dot segment — no judgement about which reader it is.
   If this reaches 13 of 13, the counter measures form, not root semantics, and the claim's headline
   must say so. Score it and report the number.
3. **Do-nothing world for C2**: a commit that mentions D1-D5 in prose, adds a `## Gate` paragraph
   containing the word "rejected", keeps the old kill-rule wording and leaves integrity red.
   Expected: 0 of 5. Observed?
4. **Target-width check**: does either counter's target equal what the base can already reach
   (`--rev {BASE}`)? C1 must read 0 of 13, C2 0 of 5. If not, the claim is dead before data.
5. **Q76 count discipline**: does either predicate quote a count from another artifact without its
   row-selection rule? Name it.

Report as a table `world | counter | observed | target | verdict`, and one line per claim:
`C1: discriminating / form-only (generator reaches N)` and `C2: discriminating / hollow`.
A hollow verdict is a finding, not a failure of your seat: the lane reports it honestly.""",
    ),
    dict(
        role="mutation-tester",
        name="MutTester",
        prompt=f"""## MutTester — mutate the two new counters and count survivors

Targets (poll {WAVE}/COUNTERS_READY every 2 min, up to 45 min; if absent, report what exists):
{LANE}/verifiers/check_omp_root_semantics.py and {LANE}/verifiers/check_r86_routed_repairs.py.

Method: copy each counter into your scratch dir, apply ONE mutation at a time to the copy (never to
the lane file), run its `--self-test` and the counter's base/honest invocation, and record whether
the self-test goes red. Mutations to try, at least eight per counter, each named:
- flip a conjunct's comparison (`>=` -> `>`, `==` -> `!=`, `in` -> `not in`);
- drop the module-offset-order check; drop the `..` rejection; widen the walk-up to `$HOME`;
- weaken the join-token set to empty; accept a quote that occurs only in the ledger;
- for C2: accept a receipt naming any revision; accept a `## Gate` paragraph instead of a row;
  accept a missing blob-identity check; let D5 pass without running the gate;
- hardcode `N = 13` / `N = 5` (a constant that ignores the rows) — does the self-test kill it?
Report `mutant | counter | self-test rc | killed/survived | which arm killed it (or none)`.
Survivors are the deliverable: the round needs the exact list of self-test gaps (the round-86
closure counted 15 of 26 survivors and routed them). Also state the assertion counts
(`0 failure(s) over N assertions`) you observed for each counter's honest run.

Acceptance: >= 16 mutants attempted, a killed/survived table, the survivor list named by mutation,
and the two assertion counts. Do not patch the counters: report, do not fix.""",
    ),
    dict(
        role="sentinel",
        name="Sentinel",
        prompt=f"""## Sentinel — isolation and security review of the new instruments and this round's evidence

Targets (poll {WAVE}/COUNTERS_READY every 2 min, up to 45 min; if absent, review what exists):
{LANE}/verifiers/check_omp_root_semantics.py, {LANE}/verifiers/check_r86_routed_repairs.py, the new
ledger {LANE}/verifiers/omp-skill-roots-semantics.tsv, and this round's wave evidence under
{WAVE}/.

Check, each with a command and its observed output:
1. **No network**: neither counter opens a socket (read the source for urllib/http/socket; and run
   each under `unshare -n` or bwrap `--unshare-net` if available, pasting the rc).
2. **Sandbox flags are self-tested**: the round-86 closure's S4 finding was `/run/docker.sock`
   reachable inside the bwrap sandbox. Does either new counter build a sandbox? If yes, list every
   bind/mount and say whether the socket, the omp logs, `~/.omp` databases and the fleet tree are
   hidden, and whether a self-test arm asserts it.
3. **TMPDIR honoured**: `grep -n 'mkdtemp\\|/tmp' <counter>` — a hardcoded `/tmp` root is a routed
   defect (scratch discipline § 4); report each hit and whether `--work`/`TMPDIR` overrides it.
4. **No credential or environment material** in any file under {WAVE}/: sweep for `op://`, `ghp_`,
   `sk-`, `TOKEN=`, `PASSWORD=`, long base64-looking runs, and the literal `$HOME` dumps of `env`;
   paste the sweep command and its (empty or non-empty) result.
5. **Write confinement**: do the counters write only under TMPDIR/--work (and never into the lane,
   the fleet root, a sibling lane, or `~/.omp`)? Check for absolute write paths in the source.
6. **ELF read-only discipline**: no copy of the 277 MB ELF into the lane or the wave dir
   (`du -sh {WAVE}` and a find for files > 5 MB under {LANE} that are not tracked at base).

Report `check | command | observed | verdict (pass/finding)` and a closing line
`instruments: clean / N findings`, naming each finding's file:line. Do not patch anything.""",
    ),
]


def main() -> None:
    for item in ITEMS:
        item["prompt"] = CONTEXT + "\n\n" + item["prompt"]
    spec = {
        "wave": "r87-w1",
        "milestone": (
            "r87-w1: C1 depth — omp root semantics grounded per root (13 rows: code reader quote, "
            "module offset, walk-up bound, `..` refusal); C2 consistency — the five r86 routed "
            "defects closed. 4 attack seats falsify both."
        ),
        "reportDir": ".ufo/waves/round-87/w1",
        "context": CONTEXT,
        "items": ITEMS,
    }
    out = Path(__file__).resolve().parent / "r87-w1-spec.json"
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out} items={len(ITEMS)}")


if __name__ == "__main__":
    main()
