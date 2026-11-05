# ScribeCorpusR93 — SOURCES rows and the round-93 lesson

Seat: ScribeCorpusR93 (scribe). Round 93, wave 1. Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Scratch clone (the only writable repo): `/fast/scratch/hyaku/kotoba-r93/ScribeCorpusR93/repo`, cloned
`git clone -q --shared` from the lane and checked out at the freeze commit
`6d7eee0570912d9f3b9d3e3d0137f3c755451233`; every git command ran with `-C "$D"`, and
`git -C "$D" rev-parse --show-toplevel` printed
`/fast/scratch/hyaku/kotoba-r93/ScribeCorpusR93/repo` before the commit. Scratch identity
`scratch <scratch@invalid>` used inside the clone only. No git or jj write in the lane or the fleet;
the lane's index, jj state and working tree were never touched.

## Behavior

1. **Waited for the scout.** Polled `…/.ufo/waves/round-93/w1/ScoutGitRevs/ScoutGitRevs.md` every
   120 s; it appeared after 720 s (background poll job `bg_8910`, exit 0).
2. **Independently re-fetched both primary pages** rather than trusting the scout's transcript, and
   confirmed byte identity: `curl -sS` of `https://git-scm.com/docs/gitrevisions` → HTTP 200, 74526 B,
   sha256 `60bfaca3907710bdedcfaab0c6d82721b9b317a86ecc11d60d07027bf41a1a54`; of
   `https://git-scm.com/docs/git-cat-file` → HTTP 200, 79360 B, sha256
   `91180e9f7199b73531900776d4d4adc17b5413f26f7c6a7e2420eb34412d8be7`. Both sha256 values equal the
   scout's, so the located quotes and line numbers are confirmed against the same bytes from two
   independent fetches.
3. **Appended two SOURCES rows** (S267, S268) in the exact 11-column schema of S265/S266, status
   `mined`, used-by naming `corpus/lessons/round-93.md` and (for S267 only) `plans/round-93.md`.
4. **Wrote `corpus/lessons/round-93.md`** in the shape of `corpus/lessons/round-92.md`: header
   (author ScribeCorpusR93, scaffold — the L1 completes settlement), `## Gate` (both admits with URL,
   access date, located quote and line, plus the scout's rejected candidate with reason and flip
   condition — the same-round reject the round-92 closure's defect 5 asks for), `## Mistakes` (the
   `receipt-identity` row), `## Status changes`, `## Sources`, `## Considerthese`, `## Settlement`.
5. **Added one `corpus/README.md` index row** for `lessons/round-93.md`, matching the round-92 row's
   form. No existing README row was edited.

## Gates (observed)

| gate | command | observed |
|---|---|---|
| census validate | `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file <clone>/corpus/SOURCES.md --today 2026-11-05` | exit **0**; 33 `W04` (the same pre-existing set as `receipts/census-before.txt`), **no `E`-code**, final line `file ok <clone>/corpus/SOURCES.md` |
| census rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | **192** before → **194** after (base counted in the clone at the freeze commit) |
| next S-id | `grep -oE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md \| grep -oE 'S[0-9]+' \| sort -V \| tail -1` | base `S266` → after `S268` (two new rows, no id reused) |
| row width | `awk -F'|' '/^\| S26[78] /{print NF}' corpus/SOURCES.md` | `13` for both (11 columns + the two edge empties); no literal or escaped `\|` inside a cell |
| SOURCES append-only | `python3 -B verifiers/check_sources_append_only.py --repo . --rev HEAD --base 6d7eee05…` | `sources append-only rows clean: 1 commits scanned, 0 protected-cell changes`, exit 0 (the 19 historical breaches it reports over the whole history are pre-existing at the freeze base) |
| corpus integrity | `python3 -B verifiers/verify_corpus_integrity.py --repo .` | `3/9 checks pass`, DRIFT set identical to base (`tracked_files` 191→192 as the one moved number, `unindexed 2`, `report_total 152`, `report_dead 1`, `commit_total 64`, `commit_unresolvable 1`) — **no new drift class**; the 2 unindexed files are the round-91/round-92 spot-check lessons, not this round's file |
| corpus independent | `python3 -B verifiers/verify_corpus_independent.py --repo .` | exit 1 at base and at the candidate; the diff of the two transcripts is only `tracked_files=191→192` and `index_tokens=207→208`; `unindexed=2 stale=0 missing=0` unchanged |
| gate registry | `python3 -B verifiers/check_gate_registry.py --rev HEAD` | `gate registry rows conformant 74 of 74 lane verifiers; phantom 0`, exit 0 |
| patch applies | `git apply --check` then `git apply` on a **second fresh clone** at `6d7eee05…` | `apply --check rc=0`, `apply rc=0`; the applied tree carries all three files (`corpus/README.md 1+`, `corpus/SOURCES.md 2+`, `corpus/lessons/round-93.md 182+`); the verify clone was removed |
| SKILL.md | `wc -l SKILL.md` / `wc -c SKILL.md` | 600 lines / 92 672 B — untouched, byte-identical |

## Touched surfaces

Three production files, all inside this seat's ownership, and nothing else:

- `corpus/SOURCES.md` — two appended registry rows (S267, S268); every pre-existing row byte-identical.
- `corpus/lessons/round-93.md` — new file (191 lines).
- `corpus/README.md` — one appended index row for `lessons/round-93.md`; no existing row edited.

Wave artifacts written (allowed paths): `.ufo/waves/round-93/w1/ScribeCorpusR93/ScribeCorpusR93.patch`
(sha256 `35ace44e034fbfea3a9b1b755c0478dad7f032c84fcffcbbcc32f885f85de228`),
`.ufo/waves/round-93/w1/ScribeCorpusR93_READY`, and this report at
`.ufo/waves/round-93/w1/ScribeCorpusR93.md`.

## Out of scope (deliberately not done)

- No SOURCES row for the rejected Stack Overflow candidate: the item admits rows with status
  `mined` only, so the reject is recorded in the lesson's `## Gate` prose (as round-92's `## Gate`
  records rejects) and not as a registry row.
- No edit to `verifiers/check_mutation_battery.py`, `verifiers/check_tip_battery.py` or
  `verifiers/fixtures/round-93/check-receipt-revs.sh` — other seats' ownership.
- No edit to `SKILL.md`, `corpus/QUALITY.md`, `corpus/lessons/round-92.md`,
  `corpus/lessons/round-92-verifier-spotcheck.md`, the plan, the frozen counters, or any
  `*-verifier-spotcheck.md` file.
- No commit, push, publish or deploy in the lane; no `scripts/` tool run from the read-only
  `/home/vgpnk/Projects/shokuknow`.

## Findings

1. **The plan's Frontier step says "One SOURCES row opened this round grounds C1"** and this round
   landed **two** rows (S267 grounds C1; S268 grounds the receipt-revision check the mined mistake
   names). The plan's § C1 "Sourced" clause names only the gitrevisions row, so S267 satisfies it
   literally; S268 is an additional tier-A row the item's "git-cat-file if admitted" clause admits.
   Flagged so the L1 can decide whether the count needs an addendum note; **no plan edit was made**.
2. **`corpus.index.tracked_files` moves 191 → 192** with the new lesson file. The baseline expects
   172 and already reads `DRIFT` at the freeze base, and the check's `equal` mode means the count
   was already outside its expectation, so the change is one more file on an already-red count, not
   a new drift class. The same red count (`3/9 checks pass`) is read at base and at the candidate.
3. **The round-92 spot-check defect 1 evidence is now reproducible by a machine**: the fix script
   `verifiers/fixtures/round-93/check-receipt-revs.sh` (ExecReceiptRevs' file, not this seat's)
   reads the round-92 landing receipts as `receipt revisions: 1 resolved, 4 unresolved over 18 files`,
   exit 1 — the four `cd355c4796fa…` occurrences named in the spot-check's defect 1, plus the
   scratch-declared world revisions. The lesson's `## Mistakes` row names this script as the fix and
   leaves the observed line to the L1, per the item.
4. **The `git cat-file -e` exit code 128 is not a documentation fact.** Both admitted pages state
   only the zero/non-zero contract; the numeric 128 is an observed behaviour of git 2.56.0 already
   recorded in `corpus/QUALITY.md` Q60. S268's `teaches` cell says so explicitly, so a later claim
   about "exits 128" cannot cite the doc row.
5. **The `revisions` alias page is a live trap for anchors.** `https://git-scm.com/docs/revisions`
   answers 200 with 70426 B (≠ `gitrevisions.html`'s 74526 B) and carries the same sentence at its
   own line 2338; an anchor line or sha256 taken from one page must not be mixed with the other's.
   Recorded in the lesson's `## Gate`.

## Artifact paths

- Patch: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ScribeCorpusR93/ScribeCorpusR93.patch`
  (sha256 `35ace44e034fbfea3a9b1b755c0478dad7f032c84fcffcbbcc32f885f85de228`)
- READY: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ScribeCorpusR93_READY`
- This report: `/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-93/w1/ScribeCorpusR93.md`
- Scratch clone (deleted on exit): `/fast/scratch/hyaku/kotoba-r93/ScribeCorpusR93/`
