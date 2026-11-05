#!/usr/bin/env python3
"""Generate the r87-w3 wave spec (round 87, re-verification attempt, 11 seats).

The round's claims are frozen at plans/round-87.md (freeze 669f2801, addenda
512126bb and 87ab1cb9).  This wave does not re-open them: it re-derives both
counters at the current tip, attacks them, and measures the one drift found
between the round's own after-state and the tip.
"""
from __future__ import annotations

import json
from pathlib import Path

LANE = "/home/vgpnk/Projects/shokunin/kotoba-shokunin"
WAVE = LANE + "/.ufo/waves/round-87/w3"
TIP = "760e1c5edfdefb4767420f711d08f669952de013"
BASE = "223ae62424f8ab1eb365d733eb648d6228ddd7e8"
C2A = "35a395a9aabfe2c849628bb4cfe9b25f176de411"
ELF = "6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f"

CONTEXT = f"""## Bounds (read first)
Lane repo: {LANE} — every path you write is absolute under it. Seat tools start at the fleet root,
so relative paths are wrong. Every `Report:` trailer path the validator renders is relative to
{LANE} — write it at {LANE}/<that path>. Never write the fleet root, a sibling lane, considerthese/
(operator-authored, read-only) or /home/vgpnk/Projects/shokuknow (read-only: read it, never write,
fetch or run a campaign tool there).
Scratch: create ONE dir /fast/scratch/hyaku/kotoba-r87/<your-seat-name>/ (mkdir -p), export TMPDIR to
it and pass it to any --work, delete it with `trap 'rm -rf -- "$S"' EXIT` (or finally:) before you
yield; copy receipts first under {WAVE}/<your-seat-name>/. /tmp only for files < 50 MB.
VCS: never run a git/jj write in the lane or the fleet (no add/commit/stash/checkout/reset/jj
mutation); read-only git (log, show, diff, status, ls-files, rev-parse, cat-file, archive, clone
--shared) is fine. A scratch repo is created only as
`D=$S/repo && git clone -q --shared {LANE} "$D"`, every later git call names `-C "$D"`, and
`git -C "$D" rev-parse --show-toplevel` must equal $D before any commit there.
Never touch {LANE}/../.ufo, MANIFEST.json, scripts/, templates/, .ufo/state/, .ufo/watchdog.log or
another lane. Message only agent://KotobaR87 (never agent://all). Never write outside the files your
item names. Security: never write a raw environment dump, credential or token into the lane.
Tooling authorization (operator 2026-10-19): you may install or upgrade tools that help the task;
read /home/vgpnk/.omp/agent/RULES.md first (official channels, update-safety gate; record
tool/version/channel/reason in your answer). PACMAN IS PAUSED host-wide: no pacman transaction of any
kind (no -S/-Sy/-Syu/-U/-R); use uv tool / npx / an official binary in ~/.local/bin, or report the need.
Your final answer is a short JSON: files_written, evidence (commands + observed lines), findings, risks.

## Frozen state — read it, do not change it
Round 87 already landed its two claims; this wave verifies them, it does not re-open them.
Read {LANE}/plans/round-87.md (freeze `669f2801c31ef27e18cc35a327d2e18f466281c7`), addenda
`512126bbd762ff82b9f330c4afefb29db7cd9f39` and `87ab1cb98b4950f5d7291a4a2ddaab535ca72124`,
`{LANE}/corpus/lessons/round-87.md` and the receipts under
`{LANE}/.ufo/waves/round-87/receipts/`.
Base {BASE}; the round's C2 after-receipt was measured at {C2A}; current lane tip
{TIP} (`git -C {LANE} rev-parse master` must print it; if it does not, say so and measure the tip you
find, naming it). Installed omp ELF: /home/vgpnk/.local/bin/omp, sha256 {ELF}.
The predicates, targets and kill rule are FROZEN. A counter defect is a FINDING for this wave, never
an edit: nobody in this wave changes `verifiers/*.py`, `verifiers/*.tsv`, `plans/round-87*.md`,
`corpus/SOURCES.md`, `corpus/QUALITY.md`, `LOG.md`, `SCORECARD.md` or `SKILL.md`. You write only under
{WAVE}/<your-seat-name>/ and your `Report:` file.

## What the round claims (for context only)
- C1 depth: `python3 -B verifiers/check_omp_root_semantics.py --rev <rev>` -> `omp root semantics
  grounded N of 12`, exit 0 iff N == 12 and guards S1-S3 PASS. Target 12 of 12; base 0 of 12.
- C2 consistency: `python3 -B verifiers/check_r86_routed_repairs.py --rev <rev>` -> `r86 routed
  defects closed N of 5`, exit 0 iff N == 5. Target 5 of 5; base 0 of 5.
Known state at the tip: C1 reads 12 of 12, exit 0. C2 reads 4 of 5, exit 1, because D5(iii) requires
the corpus gate's red set to be exactly `{{report_dead, commit_unresolvable}}` and `report_dead` healed
to 0 when another lane's report `.ufo/reports/round-84/kama.md` landed on the fleet repo at 22:47
(fleet commit `5b052020`). Your job is to measure and attack that, not to repair it.
"""

ITEMS = [
    {
        "role": "scout",
        "name": "ScoutSourceS256R87",
        "prompt": f"""
## Item — re-open S256 and re-verify its bytes (read-only on the lane)
`{LANE}/corpus/SOURCES.md` row `S256` grounds C1's plugin root. Re-open it this round:
1. Print the S256 row (`grep -n '^| S256' {LANE}/corpus/SOURCES.md`) and extract the URL, the access
   date, the status/recheck cells and the located quote from it. Do not trust this item's summary.
2. Fetch the URL yourself (`curl -sS -o "$S/body" -w '%{{http_code}} %{{size_download}}' <url>`;
   a 404/403 is a finding, not a licence to substitute a different page). Record HTTP code, bytes,
   `sha256sum "$S/body"`, and locate the quoted text's line number in the fetched body.
3. Decide: does the fetched body contain the row's quote verbatim, at the line the row names, and does
   its sha256 equal the row's pin? Does the page's own text make the quote a **reader** (code that
   builds the root) rather than a doc/string-table line? Quote the fetched lines around it.
4. Run the census for this lane and paste its exit code and the last line:
   `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotoba`.
Report a table `check | command | observed | verdict`, every command verbatim, and a closing line
`S256: admit-as-grounded | finding`. Write receipts under {WAVE}/ScoutSourceS256R87/.
""",
    },
    {
        "role": "scout",
        "name": "ScoutPatternsR87",
        "prompt": f"""
## Item — re-derive the skill-root pattern set from the installed binary (read-only)
The round's C1 ledger is `{LANE}/verifiers/omp-skill-roots-semantics.tsv` (header
`root_pattern<TAB>binary_quote<TAB>module<TAB>reader_quote`); the round-86 ledger is
`{LANE}/verifiers/omp-skill-roots.tsv`.
1. Derive the set yourself from `/home/vgpnk/.local/bin/omp` (sha256 {ELF}): extract the literal
   skill-root path segments the binary carries (e.g. `strings -a -n 6` piped through a pattern for
   `.omp/skills`, `.claude/skills`, `.agents/skills`, `plugins`, `managed-skills`, then `objdump -s`
   or `grep -aob` to confirm the bytes and their file offsets). Do not read the ledgers first; write
   your derived list down, then compare.
2. Compare three ways: your list vs the round-86 ledger's 13 `root_pattern` cells vs the round-87
   ledger's 12. Name every pattern one set has and another lacks, with the offset where you found it
   (or the command that found nothing).
3. State whether any derived root is a *skill* root the round's model still does not carry (a coverage
   hole for a later round), and whether any carried row is not a skill root (a false row).
Report `derived | r86 | r87` as a table with offsets, and a closing line
`coverage: N derived, N matched, holes=[...], false=[...]`. Receipts under {WAVE}/ScoutPatternsR87/.
""",
    },
    {
        "role": "executor",
        "name": "ExecTipR87",
        "prompt": f"""
## Item — measure both frozen counters and the lane battery at the tip (receipts only)
Write nothing in the lane except under {WAVE}/ExecTipR87/.
1. `git -C {LANE} rev-parse master` and `git -C {LANE} status --porcelain` (paste both).
2. `cd {LANE} && python3 -B verifiers/check_omp_root_semantics.py --rev <tip>` — paste the full
   output and `echo exit=$?`.
3. `cd {LANE} && python3 -B verifiers/check_r86_routed_repairs.py --rev <tip>` — full output and exit.
4. `cd {LANE} && python3 -B verifiers/check_tip_battery.py --rev <tip>` — full output and exit.
5. `cd {LANE} && python3 -B verifiers/verify_corpus_integrity.py --json` piped to a one-line summary
   of every non-PASS check and its detail — paste it and the exit code.
6. `cd {LANE} && python3 -B verifiers/check_gate_registry.py --rev <tip>` and
   `python3 -B verifiers/check_province_core.py --rev <tip>` — outputs and exits.
7. Census: `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
   /home/vgpnk/Projects/shokunin kotoba` — exit code, the count of `W04` lines and of `E` lines
   (`... | grep -c 'W04'`, `... | grep -c '^E'`), and the last line. Also
   `grep -cE '^ {{0,3}}\\| S[0-9]{{3}}' {LANE}/corpus/SOURCES.md` and the same for
   `corpus/knowledge/` entries and `corpus/lessons/` files (three counts, each with its command).
8. `sha256sum` every `verifiers/check_*.py` and `verifiers/omp-skill-roots-semantics.tsv` you ran, so
   the reading is bound to bytes.
Deliver one receipt file per numbered step under {WAVE}/ExecTipR87/ (verbatim command, verbatim
output, exit code), plus `SUMMARY.json` with every value as a field. Close with
`tip battery: <C1> / <C2> / <battery> / <census>` using the observed strings.
""",
    },
    {
        "role": "executor",
        "name": "ExecMirrorR87",
        "prompt": f"""
## Item — the same-bytes, different-path world for C2's D5(iii)
Hypothesis to test: C2's D5(iii) verdict depends on a file **outside** the lane (the fleet report
`.ufo/reports/round-84/kama.md`), so identical lane bytes score differently by checkout location.
1. `D=$S/repo && git clone -q --shared {LANE} "$D"` and verify
   `git -C "$D" rev-parse --show-toplevel` equals $D. Check out the tip ({TIP}) as `master` in the
   clone (`git -C "$D" checkout -q -B master <tip>` — this is the one permitted write, inside the
   clone only).
2. Run the frozen counter in the clone: `cd "$D" && python3 -B verifiers/check_r86_routed_repairs.py
   --rev <tip>` — paste the output and exit. Then run the same command in the real lane and paste it.
3. Run `python3 -B verifiers/verify_corpus_integrity.py --json` in the clone and in the lane; diff
   the `observed.corpus.report_dead` / `report_dead_detail` / `commit_unresolvable` fields and paste
   both. Say exactly which path resolved in which location and why (read the gate's resolution rule
   in `verifiers/verify_corpus_integrity.py` and quote the code lines that implement it).
4. Re-create the drift **inside the clone only** in a way you can show: make the citing line's target
   not resolve in the clone's own resolution set (do not edit `corpus/lessons/round-86-verifier-spotcheck.md`;
   instead, if the gate resolves a bare `.ufo/reports/...` from a fleet root, demonstrate the
   resolution by placing/removing the target under the clone's parent — or prove with the gate's own
   `--json` fields that the resolution set is the deciding variable and say so plainly if a live
   re-creation is impossible without editing a non-author record).
5. Verdict: is D5(iii)'s exact-set conjunct monotone (fails only when a red is **added**) or not
   (fails when a red is **healed**)? Give the observed pair of readings as the proof.
Write receipts under {WAVE}/ExecMirrorR87/ and a short `WORLD.md` with the command list and the two
readings. Close with `same bytes, two paths: lane=<...> clone=<...>; conjunct=non-monotone|monotone`.
""",
    },
    {
        "role": "executor",
        "name": "ExecProbeBoundR87",
        "prompt": f"""
## Item — one bounded read-only probe of C1's `{{cwd}}/` bound, under a scratch HOME
C1's conjunct 4 says a `{{cwd}}/` row's expansion (cwd and its ancestors) **excludes** `$HOME` and
above. Probe it empirically without touching the real HOME:
1. `S=/fast/scratch/hyaku/kotoba-r87/ExecProbeBoundR87; mkdir -p "$S/home/u/proj/sub" "$S/home/.agents/skills/probe-skill" "$S/home/u/proj/sub/.agents/skills/local-skill"`.
   Put a minimal `SKILL.md` (name + description + one line) in each skills dir.
2. With `HOME=$S/home` and cwd `$S/home/u/proj/sub`, run the installed omp in a non-interactive mode
   that lists or loads skills if it has one (`omp --help | head -40`, then the closest verb;
   `timeout 60` every run). Record exactly what you ran.
3. Report which of the two skills omp sees: the one under the cwd chain (`$S/home/u/proj/sub`) and/or
   the one directly under the scratch HOME. If neither mode can enumerate skills, say so, paste the
   `--help` lines you checked and the exit codes, and mark the probe **inconclusive** — an
   inconclusive probe is a valid result and never a pass.
4. Delete the scratch tree at exit.
You may spawn at most ONE read-only `labrat` child for a second probe attempt; no other seats.
Write receipts under {WAVE}/ExecProbeBoundR87/. Close with
`bound probe: <home-visible|home-hidden|inconclusive>` and the command that decided it.
""",
    },
    {
        "role": "reviewer",
        "name": "ReviewC1R87",
        "prompt": f"""
## Item — independently re-implement C1's four conjuncts (read-only; do not import the counter)
Target revision: the lane tip ({TIP}). Ledger: `verifiers/omp-skill-roots-semantics.tsv` (12 rows).
Write your own Python under {WAVE}/ReviewC1R87/reimpl.py — never import
`verifiers/check_omp_root_semantics.py` and never read its source before your first scored run; write
your four conjuncts from `plans/round-87.md` § C1 only.
1. Conjunct 1: each `root_pattern` equals the round-86 ledger row at the same index and contains no
   `..` and no wildcard in its first segment (`verifiers/omp-skill-roots.tsv`, read from committed
   bytes with `git -C {LANE} show {TIP}:<path>`).
2. Conjunct 2: the `reader_quote` (>= 12 chars) occurs in `/home/vgpnk/.local/bin/omp` on a line that
   also carries a path-join token (`join(`, `.join(`, `resolve(`, `path.join`).
3. Conjunct 3: `// packages/<module>` occurs in the ELF and the quote's first occurrence lies after
   that header's last occurrence.
4. Conjunct 4: for `{{cwd}}/` rows the expansion set excludes `$HOME` and above; a `..` candidate never
   matches.
Score all 12 rows, print `reimpl grounded N of 12`, and diff your per-row verdicts against the frozen
counter's `row NN GROUND` lines (run it after yours: `python3 -B verifiers/check_omp_root_semantics.py
--rev {TIP}`). Every disagreement is a finding with the row, the conjunct and both observed values.
Also state the limits of your re-implementation (what you share with the counter — the ELF, the same
plan text — and what that means for independence).
Receipts under {WAVE}/ReviewC1R87/. Close with `reimpl: N of 12; disagreements=[...]`.
""",
    },
    {
        "role": "reviewer",
        "name": "ReviewD1D5R87",
        "prompt": f"""
## Item — independently check C2's five items at the tip (read-only)
Read `plans/round-87.md` § C2 and `plans/round-87-addendum-2.md` § A2.1, then check each item by hand
against committed bytes at {TIP} (`git -C {LANE} show {TIP}:<path>`), not by trusting the counter:
- D1: `.ufo/waves/round-86/receipts/tip-catalogue.txt` and `tip-registry.txt` exist at {TIP}, name
  their measured revision, carry `exit=0` and the two required lines; the two instruments are
  byte-identical between `04647b0f715ff3c4f314b0d8f03dea28bc453688` and {TIP}
  (`git -C {LANE} rev-parse {TIP}:verifiers/<file>` vs the same at `04647b0f`).
- D2: the validator sentence occurs verbatim in the lane's record AND in
  `~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs`; `SWARM_ROLES` has no `planner`. Quote the
  lines and the array.
- D3: `corpus/lessons/round-87.md` `## Gate` has >= 1 row whose decision cell is `reject` with >= 8
  words of reason; count them and quote the longest.
- D4: `plans/round-87.md` states `after the first candidate score` verbatim; quote the sentence.
- D5(i)/(ii): the blobs of `corpus/lessons/round-86-verifier-spotcheck.md` and
  `corpus/lessons/round-81.md` at {TIP} equal their blobs at {BASE} (`git -C {LANE} rev-parse`).
- D5(iii): run `cd {LANE} && python3 -B verifiers/verify_corpus_integrity.py --json` and state the
  red set; run the frozen counter and paste its d5 line. Then run the counter at {C2A} and paste the
  exact refusal it prints. Explain, from the code (`verifiers/check_r86_routed_repairs.py`'s
  `check_d5`), which conjunct produces each reading, and whether the difference is an improvement or
  a regression **in the corpus** (not in the instrument).
Deliver a table `item | verdict at tip | evidence | delta vs the round's after-receipt` and a closing
line `C2 at tip: N of 5; defect class: <none|instrument-staleness|work-regression>`. Receipts under
{WAVE}/ReviewD1D5R87/.
""",
    },
    {
        "role": "critic",
        "name": "CriticSemanticsR87",
        "prompt": f"""
## Item — falsify C1's semantics (read-only; be adversarial)
C1's claim is that each ledger row's `reader_quote` is the code that **builds** the root, not a doc or
string-table line that merely mentions it. Attack it on at least four rows, including the plugin root
(`~/.omp/plugins/node_modules/*/skills`) and one `{{cwd}}/` row:
1. For each row, locate the quote in `/home/vgpnk/.local/bin/omp` (`grep -aob` for the offset,
   `od`/`objdump -s` around it) and show the surrounding bytes. Does the surrounding context read as
   executable code (a property assignment, a join call, a function body) or as a literal table? State
   which, with the bytes.
2. Check the module attribution: is `// packages/<module>` really the header of the code that contains
   the quote, or merely the nearest header by file offset (the ELF is a bundle; a misattributed module
   would satisfy conjunct 3 without being true)? Name any row where attribution is doubtful.
3. Ask the strongest falsification the claim invites: could a row pass all four conjuncts while the
   quoted call constructs a **different** path than the `root_pattern` names (e.g. quote joins a
   subdirectory of another root)? Build that world on paper against one row and say whether the
   counter would pass it.
4. State what would settle the question mechanically (a probe that loads a real skill from the root,
   a decompiler pass, an upstream source diff) and whether it is available this round.
Receipts under {WAVE}/CriticSemanticsR87/. Close with
`semantics: grounded | partially-grounded | unproven` plus the rows that carry the doubt.
""",
    },
    {
        "role": "mutation-tester",
        "name": "MutateR87",
        "prompt": f"""
## Item — mutate both counters in a scratch copy; report every surviving mutant (read-only on the lane)
Copy the lane's `verifiers/` into your scratch (`cp -a`), never edit the lane copies.
1. C1 (`check_omp_root_semantics.py`): produce one mutant per guard and run each against the tip
   ledger at {TIP}, in a scratch repo clone so `git show <tip>:<path>` resolves. Mutants: (a) drop the
   path-join-token requirement from conjunct 2; (b) drop the module-ordering test (quote after header);
   (c) accept a `..` segment; (d) accept a wildcard first segment; (e) accept an 11-row ledger.
   For each: command, printed N, exit code, and killed/survived. A survivor is a finding — name the
   forged ledger that would pass.
2. C2 (`check_r86_routed_repairs.py`): mutants of D3 (accept `rejected` anywhere in the prose, not a
   row) and D4 (drop the verbatim boundary sentence), plus one mutant of D5(iii) (replace exact-set
   equality with "no red outside the set") — for D5(iii) say explicitly what each form accepts and
   rejects, including the healed-drift case, and label it **analysis of a proposed repair**, not a
   change you made.
3. Report the mutation score per counter and the strongest surviving mutant.
Receipts under {WAVE}/MutateR87/ (`mutants/` with the diff of each mutant). Close with
`C1 killers: k/5; C2 killers: k/3; survivors=[...]`.
""",
    },
    {
        "role": "sentinel",
        "name": "SentinelEvidenceR87",
        "prompt": f"""
## Item — evidence and confinement audit of the round (read-only)
1. **Non-author records**: `git -C {LANE} rev-parse {BASE}:corpus/lessons/round-86-verifier-spotcheck.md`
   vs `{TIP}:...` and the same for `corpus/lessons/round-81.md` — paste both pairs and state identical
   or not.
2. **No `/tmp` evidence**: grep the lane's round-87 artifacts and the whole `corpus/` for citable
   `/tmp` paths (`grep -rnE '(^|[^a-z])/tmp/' {LANE}/corpus {LANE}/.ufo/waves/round-87 --include='*.md'
   --include='*.txt' --include='*.json' --include='*.tsv'`); classify each hit as a citation (defect) or
   a command artifact (allowed). Paste the counts.
3. **Receipts name their revision**: for every file under {LANE}/.ufo/waves/round-87/receipts/, state
   whether it names the revision it was measured at and an exit code; list the ones that do not.
4. **Credentials**: sweep the round-87 wave tree and the receipts for `op://`, `ghp_`, `sk-`,
   `TOKEN=`, `PASSWORD=`, `-----BEGIN`, and long base64 runs; paste the command and result.
5. **Ready-file discipline**: list `{LANE}/.ufo/waves/round-87/*.ready*`, state how many `ready` files
   exist per wave and whether each was taken (a `.dispatched` marker) — a re-written or duplicated
   ready is a finding.
6. **Write confinement**: `git -C {LANE} status --porcelain` and `git -C /home/vgpnk/Projects/shokunin
   status --porcelain` — list any untracked file that names this lane or round under the fleet root
   (a misroot), and any lane file changed outside the wave tree.
Receipts under {WAVE}/SentinelEvidenceR87/. Close with `audit: clean / N findings`, each with file:line.
""",
    },
    {
        "role": "scribe",
        "name": "ScribeIndexR87",
        "prompt": f"""
## Item — build the round's evidence index from what is actually on disk (draft only)
Produce {WAVE}/ScribeIndexR87/INDEX.md, a factual table of the round's evidence as it exists:
1. Every file under `{LANE}/.ufo/waves/round-87/` (spec, dispatch, results, receipts, seat dirs) with
   its size, first line and — where the file is a receipt — the command it records and the revision it
   names. Read the files; do not assume.
2. For `{LANE}/corpus/lessons/round-87.md`, `plans/round-87.md`, `plans/round-87-addendum-1.md`,
   `plans/round-87-addendum-2.md`: the section headings, in order, with line numbers.
3. For `{LANE}/LOG.md` and `{LANE}/SCORECARD.md`: the line range of the round-87 entry
   (`grep -n 'Round 87' …`) and whether it names commit hashes that resolve
   (`git -C {LANE} cat-file -e <hash>^{{commit}}` for each, paste the results).
4. A "missing evidence" list: every claim in the lesson/report whose pointer you could not resolve on
   disk, with the pointer text.
No production file is written by this item. Close with `index: N files, N resolved pointers, N dangling`.
""",
    },
    {
        "role": "connector",
        "name": "ConnectOverlapR87",
        "prompt": f"""
## Item — sibling overlap and staged-package overlap (read-only everywhere)
1. **Staged package**: read `/home/vgpnk/Projects/shokuknow/merge/kotoba/MERGE-REPORT.md` (and grep
   its `SOURCES.append.md` / `knowledge/` tree read-only). Report: does stage contain the omp skill
   -root loader semantics this round grounds (search for `skill`, `discovery`, `plugin`, `root`,
   `omp`, `loader`)? Quote the rows/entries that overlap and say which are duplicates of S256 or of
   the round-87 knowledge entry. Then state the package's staged date and the lane's current tip —
   the round-87 report recorded the package as absent; is that still true, and if not, when did it
   appear (`stat`/git log on the fleet repo is not available for that tree — use its mtimes and say
   they are mtimes).
2. **Sibling lanes**: `grep -rl 'omp-skill-roots\|reader_quote\|discovery/omp-plugins' {LANE}/../*/\\.ufo
   {LANE}/../*/corpus 2>/dev/null` (read-only) and name any sibling lane that already holds the same
   loader semantics or contradicts ours. Do not write in any sibling.
3. State the cross-lane consequence: duplication to avoid, a contested scope to report, or nothing.
Receipts under {WAVE}/ConnectOverlapR87/. Close with
`overlap: package=<none|rows N|entries M>, siblings=[...], consequence=<...>`.
""",
    },
]


def main() -> None:
    for item in ITEMS:
        item["prompt"] = CONTEXT + "\n" + item["prompt"].strip() + "\n"
    spec = {
        "wave": "r87-w3",
        "milestone": (
            "r87-w3: re-verify frozen C1 (depth 12/12) and C2 (consistency 5/5) at the tip, attack "
            "both with independent re-implementations and mutants, and measure the C2 D5 drift."
        ),
        "reportDir": ".ufo/waves/round-87/w3",
        "context": CONTEXT,
        "items": ITEMS,
    }
    out = Path(__file__).resolve().parent / "r87-w3-spec.json"
    out.write_text(json.dumps(spec, indent=1, ensure_ascii=False) + "\n")
    print(f"wrote {out} items={len(ITEMS)} roles={[i['role'] for i in ITEMS]}")


if __name__ == "__main__":
    main()
