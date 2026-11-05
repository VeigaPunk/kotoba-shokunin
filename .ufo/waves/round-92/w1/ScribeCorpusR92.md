# ScribeCorpusR92 — round 92 w1 (S265, S266; the round-92 lesson; Q83)

Seat: **ScribeCorpusR92** (scribe, leaf member — no subagent dispatch).
Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`. Base (the freeze commit):
`e073723ae667b64e534f8621bddb83ad12ad0e71`.

**The lane was not written.** Every corpus file lives in the seat's own scratch clone
(`/fast/scratch/hyaku/kotoba-r92/ScribeCorpusR92/repo`, a `--shared` clone of the lane at the freeze
base); the patch is the only channel to the lane, and the L1 integrates it. Scratch was removed
before yield. No `git`/`jj` write touched the lane, the fleet root or a sibling lane.

## Files in the patch

| file | change |
|---|---|
| `corpus/SOURCES.md` | **append only** — two rows after S264: S265 (Python `subprocess` docs, the anchor-repair correction row superseding S263, `mined`) and S266 (Python built-in exceptions, the `NotADirectoryError` reference, `mined`). No existing row was touched; the row count went 190 → 192 |
| `corpus/lessons/round-92.md` | **new** — the round lesson: `## Gate`, `## Mistakes`, `## Status changes`, `## Sources`, `## Considerthese`, `## Settlement` (L1 placeholder) |
| `corpus/QUALITY.md` | **append only** — one criterion row, `Q83` |
| `corpus/README.md` | **append/annotate only** — one new index row for `lessons/round-92.md`, plus an append-only note on the existing `QUALITY.md` index row naming Q83. No existing index row was rewritten or removed |

No other corpus file was touched; no `SKILL.md`, no verifier, no plan, no frozen instrument.

## The two SOURCES rows

Ids confirmed before writing: the last id in the registry table is **S264**
(`grep -oE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md | grep -oE 'S[0-9]+' |
sort -V | tail -1` → `S264`), so S265 and S266 are the next two unused ids — exactly what
`plans/round-92.md` § Frontier expects. **No id deviation.**

Both rows carry 11 columns (13 pipe-delimited fields), no `|` inside any cell, and the header shape
the table declares.

**S265 — the S263 anchor repair** (the round-91 spot-check's routed defect 4). `teaches` opens
`supersedes S263 — `, as the SOURCES contract's append-only correction rule requires; the S263 row's
own bytes are **not** rewritten. Same URL, kind `docs`, tier A, and the same scope cell as S263
(verified byte-identical) minus the wrong line anchor, which now reads the corrected anchors from the
scout receipt: the `Popen.communicate` entry `dt` at **HTML line 1051** (signature 1052) and the
contrast quote at **HTML line 1071** (continuing 1072), where S263 cited 1042 — a `versionchanged`
note belonging to the preceding `Popen.wait` entry. The `subprocess.run` entry `dt` (270) and its
timeout paragraph (288–294, quoted sentence 289–291) are unchanged, so the kill-and-wait contract the
cap calibration rests on is untouched. Access 2026-11-05, HTTP 200, 208648 B (byte-identical to the
round-91 reading), footer "Last updated on Nov 05, 2026 (12:47 UTC)." at line 2037, located quote
(25 words) at 289–291. Status `mined`; opened 2026-11-05; recheck `180d`; used-by
`corpus/knowledge/timeout-calibration-round91.md,corpus/lessons/round-92.md`.

**S266 — the environment exception reference.** `https://docs.python.org/3/library/exceptions.html`
answers **301** and lands on `https://docs.python.org/3/builtins/exceptions.html`; the row records
both, as the scout receipt requires, and the anchor cell names the redirect. Final HTTP 200, 145885 B,
title "Built-in Exceptions — Python 3.15.2 documentation". Tier A, kind `docs`, scoped to *which
exception the Python runtime raises when a path component is not a directory — grounding the freeze
gate's fail-closed work-root rung*. The `NotADirectoryError` entry `dt` is at line 1118 (signature
1119, body 1120–1124); the located quote is at 1120–1121 (17 words); the POSIX path-component clause
at 1122–1123 (22 words); `errno.ENOTDIR` at 1124; the exception-hierarchy tree at 1440 (`OSError`)
and 1452 (`NotADirectoryError`) inside the block opening at 1416. The page names exactly one `os`
function for this exception — `os.listdir()` (1120) — and the adjacent `os.remove()` mention (1112)
belongs to `IsADirectoryError` and is **not** attributed to this row. Status `mined`; opened
2026-11-05; recheck `180d`; used-by `corpus/lessons/round-92.md`.

The located quotes and every line number in both rows are copied from the scout's receipt
(`.ufo/waves/round-92/w1/ScoutPyDocs/ScoutPyDocs.md`); **no URL was re-opened** by this seat. The
`SOURCE_READY` file was polled for and appeared (content `SOURCE-READY`) before the receipt was read.

## Census and validation (measured in the seat's clone)

| measurement | value |
|---|---|
| `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` before | **190** (base clone at `e073723ae…`; the lane's committed receipt `.ufo/waves/round-92/census-before.txt` records 190) |
| same command after | **192** |
| plan § Frontier expectation | 190 → 192 — met, no row dropped |
| `bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --file corpus/SOURCES.md --today 2026-11-05` | **exit 0**, `file ok …/corpus/SOURCES.md`, **33** pre-existing W04 duplicate-URL warnings, **no E-code** |
| the same validator in lane-registry form (`validate --root /home/vgpnk/Projects/shokunin kotoba`) | **exit 0**, `kotoba ok …/kotoba-shokunin/corpus/SOURCES.md` |

The W04 count is unchanged at 33: S265 reuses S263's URL *and* S263's scope, and the census's E04
duplicate-url-within-scope rule is satisfied because the S265 `teaches` cell opens
`supersedes S263 — ` (the `supersedes` escape hatch the validator implements). No new warning class
appears.

## Corpus integrity (before vs after, same instrument, same host)

| counter | base clone `e073723ae…` | after this seat's patch | note |
|---|---|---|---|
| `corpus.index.tracked_files` | 189 | **190** | the new `corpus/lessons/round-92.md`, indexed by the new README row |
| `corpus.index.index_patterns` | 206 | **207** | the new README index row |
| `corpus.index.unindexed` | 1 | 1 | same carried site (`corpus/lessons/round-91-verifier-spotcheck.md`) |
| `corpus.index.stale_patterns` | 0 | 0 | — |
| `corpus.index.missing_paths` | 0 | 0 | — |
| `corpus.pointers.report_total` | 149 | 149 | the lesson cites no report pointer |
| `corpus.pointers.report_dead` | 1 | 1 | same carried site (`corpus/lessons/round-81.md:29`) |
| `corpus.pointers.commit_total` | 64 | 64 | the lesson cites no `commit \`<hash>\`` token |
| `corpus.pointers.commit_unresolvable` | 1 | 1 | same carried site |
| `corpus.pointers.commit_nonhash` | 0 | 0 | — |

The five DRIFTs the gate reports (`tracked_files`, `unindexed`, `report_total`, `commit_total`,
`commit_unresolvable`) are **the same five the base carries**; `verifiers/corpus-baseline.json` is
stale at round-87 and is a frozen instrument this seat may not edit, so the L1 re-records it at
integration. This seat adds one tracked file and one index pattern — the two counters the plan's
landing no-harm line names as the design's growth — and changes nothing else.

`verifiers/check_correction_sweep.py --root .` → `correction sweep: 0 stale block(s)`, exit 0.

The tip battery at the candidate (base + this seat's corpus patch, scratch rev
`0d4f9065d17579ef21e16ba64397490ecd0daeff`) reads **`guards 5 of 5; tip battery exit 0: 3 of 6`** —
identical to the base reading in `.ufo/waves/round-92/receipts/base-tipbattery.txt`: the same three
carried red corpus gates (`verify_skill_checklist`, `verify_corpus_integrity`,
`verify_corpus_independent`), and the `spotcheck-identity` guard PASSes (this seat added no
`corpus/lessons/*-verifier-spotcheck.md` and edited none). No new red, no closed carried red.

**A measurement caveat, recorded so the L1 is not surprised.** `verify_corpus_integrity.py` reads the
index from the working tree but the file population from `git ls-files corpus/`. Applied to a tree
whose new file is *not yet staged*, the README row that indexes it reads as
`stale_patterns=1` (`corpus/README.md:194: lessons/round-92.md`) — an artifact of the file not being
tracked, not a defect in the patch. Once the file is staged (the state the landed commit has), the
same tree reads `stale_patterns=0`. Receipt: `stale-pattern-note.txt`.

## The lesson file

`corpus/lessons/round-92.md` carries the sections the item names: the header (author
**ScribeCorpusR92**, round 92, plan `plans/round-92.md` frozen at `e073723ae667b64e534f8621bddb83ad12ad0e71`,
base `e073723ae667b64e534f8621bddb83ad12ad0e71`, and the pre-data controls receipt); `## Gate` (both
candidates' access records with URL, access date, HTTP status, byte size and located quotes ≤ 25
words with line numbers; the admit decisions with reasons; the census before→after line with the
counting command); `## Mistakes` (the `vacuous` row, marked as **the L1-confirmed row**, with class,
evidence `.ufo/waves/round-91/w1/CriticClaims.md` § Controls + `verifiers/fixtures/round-91/ctl-c2-capline-only.sh`,
captured-by Q37's gap — a control need not refuse its own shortcut — and fix `plans/round-92.md` C1);
`## Status changes` (S263 corrected by S265, anchor-repair only, with the old → new line numbers and
the reason S263's own bytes stand); `## Sources` (both rows as full records); `## Considerthese`
(2026-10-26 re-read, nothing implemented, proposal 3 carried at the 600/600 ceiling, proposals 1/4/5
carried and already mined as Q78/Q80/Q82); and `## Settlement (L1 — placeholder)`, which the L1
completes at settlement.

**No claim verdict is written anywhere in the lesson.** The C1 and C2 verdicts, the seat record, the
wave disposition and the final numbers are the L1's; the placeholder says so explicitly.

## The Q83 criterion

`corpus/QUALITY.md` gains exactly one row, `Q83`: *a §9 shortcut control refuses the shortcut it
names through the public path: on a committed shortcut world missing the claimed conjunct the control
exits non-zero naming that conjunct and its honest world exits zero; a control that reads only a
threshold or an uncommitted tree is a census observable, never the whole evidence.* — grounded in
`corpus/lessons/round-92.md` § Mistakes (the `vacuous` row), supersedes `—`. The criterion text is
the item's text verbatim.

## The README index rows

Two touches, both additive: a new row for `lessons/round-92.md` in the existing
`| Area | File | Basis |` shape, and an append-only note on the existing `QUALITY.md` index row
naming Q83 (the lane's index shape has one QUALITY pointer, the round-46 "Admission bar" row; it is
annotated, not replaced). No existing index row was rewritten or dropped, and nothing else in
`corpus/README.md` was touched.

## Patch and handoff

- Patch: `.ufo/waves/round-92/w1/ScribeCorpusR92/ScribeCorpusR92.patch`
  (`git diff --cached --binary e073723ae667b64e534f8621bddb83ad12ad0e71` over `corpus/`, 28 464 bytes,
  4 files, 135 insertions / 1 deletion).
- Apply proof: a fresh `--shared` clone at `e073723ae667b64e534f8621bddb83ad12ad0e71` passes
  `git apply --check` and then applies; the applied tree reads census **192**, `validate` **exit 0**
  with the same 33 W04 and no E-code, and (staged) corpus integrity `stale_patterns=0`.
- Receipts: `census-after.txt`, `corpus-integrity.txt`, `stale-pattern-note.txt`,
  `tip-battery.txt` in the seat's own directory.
- READY: `.ufo/waves/round-92/w1/ScribeCorpusR92_READY`, content `CORPUS-READY` only, written after
  `validate` exited 0 in the seat's clone.
- The seat's scratch clone also carries a scratch-identity commit `0d4f9065d17579ef21e16ba64397490ecd0daeff`
  so a gate can name the candidate revision; it is inside the scratch clone only and is not part of
  the handoff.

## Out of scope / not done by this seat

- The L1 lands `SCORECARD.md`, `LOG.md`, `PROVINCE.md` and (if needed)
  `plans/round-92-addendum-*.md`, and re-records `verifiers/corpus-baseline.json` at integration. This
  seat edited none of them.
- `corpus/knowledge/timeout-calibration-round91.md` still cites the S263 anchor (line 1042) in its
  own `source:` line. It is **not** this seat's file (the touch list gives this seat SOURCES.md,
  lessons/round-92.md, README.md and QUALITY.md only), and the S265 row is the contract's
  append-only correction. The L1 may want to append a pointer to S265 in that knowledge entry at
  integration; this seat did not touch it.
- The S263 row's own `used-by` still names `corpus/lessons/round-91.md`; the S265 row names the new
  lesson. Both rows stand; the SOURCES contract's rule 2/3 handles the supersede.
- No tool was installed or upgraded this round; nothing was fetched from the network by this seat
  (the scout's receipt is the only access evidence, and it was not re-opened).
