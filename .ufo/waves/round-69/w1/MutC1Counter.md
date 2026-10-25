# MutC1Counter — mutation test of `verifiers/check_skill_precedence.py` (round 69, wave 1)

Seat: mutation tester (C1, depth axis). Assignment: one plausible-defect battery against the C1
counter in an isolated sandbox; never touch the lane's committed counter.

## Verdict

- **Honest instrument holds.** `--self-test` = 18/18 assertions, 0 failures, exit 0; `--rev
  <content-rev>` = `skill precedence backed 5 of 5`, exit 0; `--fetch` = `live quotes found 5 of 5`,
  exit 0.
- **11 of 13 mutants killed (84.6%).** Each kill is a clean `FAIL` line and nonzero exit, except
  M14, which dies as an uncaught `TypeError` traceback (still exit 1).
- **2 mutants survived**, and both were then shown to *accept real defective revisions* (honest
  counter 0 of 5 → mutant 5 of 5): the self-test does not pin the coverage-map row's **column
  position** (M9) and does not pin the **25-word quote cap** (M10). These are coverage findings
  against the self-test, not mutations of the contract.
- **Kill attribution is not what the world names suggest** for M1 and M4: their dedicated broken
  worlds are rejected by a *different* conjunct, and the honest-world assertion is the actual
  discriminator. Evidence below.
- **Extra, independently reproduced while probing quote mutants:** a heading-only quote
  (`"Skill location"` for S206) passes `5 of 5` and `--fetch 5 of 5` on the honest counter. The
  located-quote conjunct proves "a shared double-quoted span", not "a span stating a precedence
  rule". Confirmed independently of the peer report that raised it (ScoutJunie F2); not my
  mutation, but a false-accept class no self-test world exercises.

## Environment and provenance

| item | value |
|---|---|
| lane | `/home/vgpnk/Projects/shokunin/kotoba-shokunin` |
| lane HEAD at probe start and end | `a238989a96cb0d2b939679126b832d75b861ca6e` (plan + counters commit; branch `master`) |
| sandbox | `/tmp/k69-mut-c1`, `git clone --shared --no-hardlinks`, checked out `a238989` |
| honest content draft | entry untracked, `corpus/SOURCES.md` +5 rows, `corpus/README.md` +2 rows in the lane working tree; copied byte-for-byte into the sandbox and committed **sandbox-only** as `597ba2f1e098fc3d31ff007612b69fc509f73025` ("sandbox: honest C1 content draft") |
| counter under test (pristine) | sha256 `9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48`, byte-identical to `HEAD:verifiers/check_skill_precedence.py` (`c92ab120b741f456bafd9003dc45a064cbf265b4`) |
| mutants | 13 separate copies under `/tmp/k69-mut-c1/verifiers/mutants/`, each one single-statement substitution, all asserts `count(old)==1`; pristine file never edited |
| raw outputs | `/tmp/k69-mut-out/*.txt`, `summary.json`, `bad-revs.json`, `bad-revs2.json`, `false-accept.json`, `survivor-probes.json` |
| installs | none (no pacman, no uv/npx); 1 process at a time, ≤120 s per run |

Why the honest measured rev is not the lane tip: at probe time the lane tip `a238989` carries the
counter but **not** the entry (untracked draft). Measured directly:

```
python3 -B verifiers/check_skill_precedence.py --rev a238989a96cb0d2b939679126b832d75b861ca6e
measured-rev: a238989a96cb0d2b939679126b832d75b861ca6e
skill precedence backed 0 of 5
  - entry missing: corpus/knowledge/skill-name-precedence-round69.md
exit=1
```

So any receipt that says "`--rev <tip>` → 5 of 5" must name the **content** commit, not the plan tip.

## Detector on pristine bytes (baseline)

```
$ python3 -B verifiers/check_skill_precedence.py --repo /tmp/k69-mut-c1 --self-test
PASS honest world: backed 5 of 5
PASS broken world rejected: entry missing
PASS broken world rejected: no source line
... 13 more PASS broken world lines ...
PASS missing-entry classification: backed 0 (content verdict)
self-test: 0 failure(s) over 18 assertions
exit=0
```

```
$ python3 -B verifiers/check_skill_precedence.py --repo /tmp/k69-mut-c1 --rev 597ba2f1e098fc3d31ff007612b69fc509f73025
measured-rev: 597ba2f1e098fc3d31ff007612b69fc509f73025
skill precedence backed 5 of 5
exit=0
```

```
$ python3 -B verifiers/check_skill_precedence.py --repo /tmp/k69-mut-c1 --rev 597ba2f… --fetch
skill precedence backed 5 of 5
  fetch S203: found
  fetch S204: found
  fetch S205: found
  fetch S206: found
  fetch S207: found
live quotes found 5 of 5
exit=0        (3.5 s wall)
```

Non-vacuity controls re-run in the sandbox, not taken on trust:

| control | command | result |
|---|---|---|
| base rev | `--rev a5f7459f99bb…` | `0 of 5`, `- entry missing: …`, exit 1 |
| junk world (reconstructed: provenance trio without `source:` lines, one quote, an index row) | `--repo /tmp/k69-junk-world` | `0 of 5`, `- the entry does not open with 'source:' lines naming S### ids`, exit 1 — same verdict as `controls/C1-junk-control.txt` |
| fetch negative — reached page, quote absent | S204 URL → `https://example.com/` | `S204: NOT FOUND`, `live quotes found 4 of 5`, exit 0 |
| fetch negative — unreachable | S204 URL → `http://127.0.0.1:9/skills` | `S204: FETCH FAILED <urlopen error [Errno 111] Connection refused>`, `4 of 5`, exit 0 |

The fetch arm is non-vacuous on both failure modes (never counted as found) — but note it does not
gate the exit code; a page that loses its quote still exits 0 (see F4).

## Mutant battery

Detector for every mutant: the same bounded behavioral detector, `--self-test` with `--repo
/tmp/k69-mut-c1`, pristine working-tree content, exit code and `FAIL` lines recorded. All mutants
are separate files; the pristine counter's sha256 is unchanged before and after (see Restoration).

| # | mutant | before → after (single statement) | detector | kill mode |
|---|---|---|---|---|
| M1 | `M1_status_flip` | `if row[7] != "mined":` → `if row[7] == "mined":` | **KILLED** exit 1, 1 FAIL | honest world (`backed 0 of 5`: every honest row now fails) |
| M2 | `M2_drop_usedby` | `if ENTRY not in [p.strip() … row[10]]:` → `if False and ENTRY not in […]:` | **KILLED** exit 1 | world `used-by omits the entry -> backed 5` |
| M3 | `M3_return_backed` | inserts `return TOTAL, []` before `src, global_findings = _provenance(entry)` | **KILLED** exit 1, 15 FAILs | 15 of 16 broken worlds survive (only `entry missing`, rejected before the insertion point, is caught) |
| M4 | `M4_weaken_quote` | `matched = [_norm(q) for q in quotes if _norm(q) in anchor]` → `matched = [_norm(q) for q in quotes]` | **KILLED** exit 1, 1 FAIL | honest world only; the `quote not in the anchor cell` world is rejected by the *table-carry* conjunct |
| M5 | `M5_drop_distinct_clients` | `if len(set(clients)) != len(clients):` → `if False:` | **KILLED** exit 1 | world `two rows name one client -> backed 5` |
| M6 | `M6_drop_index` | `if not _indexed(readme):` → `if False:` | **KILLED** exit 1 | world `no coverage-map row -> backed 5` |
| M7 | `M7_drop_verifiedat` | `if i >= len(body) or body[i] != f"verified-at: {VERIFIED_AT}":` → `if False:` | **KILLED** exit 1 | world `no verified-at -> backed 5` (the `elif` still checks `recheck:`) |
| M8 | `M8_drop_recheck` | `elif i + 1 >= len(body) or not body[i + 1].startswith("recheck:"):` → `elif False:` | **KILLED** exit 1 | world `no recheck -> backed 5` |
| M9 | `M9_index_any_column` | `if len(cells) >= 2 and cells[1] == needle:` → `if len(cells) >= 1 and needle in " ".join(cells):` | **SURVIVED** exit 0, 0 FAILs | none — see F1, demonstrated false accept |
| M10 | `M10_relax_word_cap` | `… if 0 < len(q.split()) <= 25]` → `… <= 400]` | **SURVIVED** exit 0, 0 FAILs | none — see F2, demonstrated false accept |
| M11 | `M11_drop_global_gate` | `if global_findings or findings:` → `if findings:` | **KILLED** exit 1, 4 FAILs | worlds `no verified-at`, `no recheck`, `two rows name one client`, `no coverage-map row` each `-> backed 5` |
| M12 | `M12_drop_status_conjunct` | `if row[7] != "mined":` → `if False:` | **KILLED** exit 1 | world `row not mined -> backed 5` |
| M14 | `M14_drop_none_guard` | `if row is None:` → `if False:` | **KILLED (unclean)** exit 1 | `TypeError: 'NoneType' object is not subscriptable` at world 5; battery aborts, later worlds unrun |

`solutionSpace` note: the mutants were not guessed from a fixed list — the 8 record/provenance
conjuncts, the global gate, the index helper and the quote helper were each mutated at their
decision point, then survivors were converted into defective revisions to see whether they matter.

### Kill attribution — two worlds do not discriminate the conjunct they are named for

Verified by importing the honest module and the mutant and calling `check()` on the same worlds the
self-test builds:

```
honest.check(row not mined)        -> backed 0  ["S203: status is 'queued', expected 'mined'",
                                               'S204: the per-client table row does not carry the located quote']
M1.check(row not mined)            -> backed 0  ["S204: status is 'mined', expected 'mined'", … x4]
honest.check(quote not in anchor)  -> backed 0  ["S203: no located quote of the entry occurs in the row's anchor cell",
                                               'S204: the per-client table row does not carry the located quote']
M4.check(quote not in anchor)      -> backed 0  ['S203: the per-client table row does not carry the located quote', …]
```

So: under the `!=`→`==` flip, the "row not mined" world is rejected because the *other four* rows
now fail the flipped predicate; under the anchor-blind `_row_quote`, the anchor world is rejected
because the globally-chosen quote is not carried by the row. Both mutants are still killed, but by
the honest-world assertion, not by the dedicated world. A future self-test edit that drops the
honest assertion would silently lose these two kills.

## Survivors are real defects, not equivalent mutants

Each survivor was given a defective revision that the honest counter rejects and the mutant accepts
(commits in the sandbox only):

| rev | defect | honest counter | mutant |
|---|---|---|---|
| `dc70184b38a58de95a788a5b2282940047664f61` | coverage-map row has the entry path in **column 3**, not column 2 (row still names the entry) | `0 of 5`, `- the entry has no coverage-map index row in corpus/README.md`, exit 1 | **M9: `5 of 5`, exit 0** |
| `c32db2c881f8c5749e3804674c6cb77b7be26e71` | S204's located quote is 28 words (> the frozen 25-word cap) in all three carriers (source line, anchor, table row) | `0 of 5`, `- S204: the per-client table row does not carry the located quote`, exit 1 | **M10: `5 of 5`, exit 0** |

Two further mutants were validated the same way (not survivors — killed by the self-test — but this
proves the mutants are genuine defects and the self-test's kill is the right kill):

| rev | defect | honest counter | mutant |
|---|---|---|---|
| `00a664b2f81f9d1df9725ab88e5f34a284ef9650` | S204 anchor cell replaced | `0 of 5`, `- S204: no located quote of the entry occurs in the row's anchor cell`, exit 1 | **M3: `5 of 5`, exit 0** |
| `63cb8c481cd23a66461d4ff4c145a206b448f476` | S204 `used-by` cell cleared | `0 of 5`, `- S204: used-by does not name …`, exit 1 | **M2: `5 of 5`, exit 0** |
| `1758670bd31266bc3f7124405adc857433043e28` | S204 table row renamed to `Roo Code` (duplicate client) | `0 of 5`, `- two table rows name the same client`, exit 1 | **M11: `5 of 5`, exit 0** |

## Restoration evidence

The pristine counter was never edited; mutants live in sibling files. Measured after the whole
battery and all rev probes:

```
sandbox sha256  9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48
lane    sha256  9c796574c2d588f27869e0e14289c1be8f0b3f3e56f785d68eb64ee5e756da48   identical: True
restored --self-test            exit 0  self-test: 0 failure(s) over 18 assertions
restored --rev 597ba2f1…        exit 0  skill precedence backed 5 of 5
lane HEAD                       a238989a96cb0d2b939679126b832d75b861ca6e  (unchanged)
lane `git diff HEAD -- verifiers/check_skill_precedence.py`   (empty)
```

The sandbox's HEAD is left at the last defective probe commit; its *working tree* corpus was
restored from the honest commit before the final detector run (`git diff 597ba2f -- corpus` empty at
that point). Sandbox is disposable; the lane was read-only throughout.

## Findings handed to the L1 (falsifier inputs; contract unchanged)

- **F1 — self-test gap, index column.** `_indexed()` requires the entry path in cell 1; no world
  moves it. M9 survives and accepts BAD4. A world with the needle in cell 3 would kill M9. Severity:
  low content risk (a row that names the entry elsewhere), but it is the only unpinned positional
  rule in `check()`.
- **F2 — self-test gap, quote word cap.** No world carries a >25-word quote; M10 survives and
  accepts BAD5. A world with a 28-word located quote would kill M10. Severity: medium — the cap is
  an explicit frozen conjunct ("≤25-word located quote") and is currently unasserted.
- **F3 — quote substance, honest-world false accept (independently reproduced).** With S206's
  `source:` line quoting only the section name and the Junie table-row quote cell set to
  `"Skill location"`, the honest counter prints `skill precedence backed 5 of 5`, exit 0, and
  `--fetch` prints `S206: found` / `5 of 5`. `_quoted()` accepts any 1–25-word double-quoted span
  and `_row_quote()` takes the longest span present in the anchor — and the entry legitimately
  double-quotes the section name. The 18 worlds vary structure, never quote substance. The draft
  entry is unaffected (it carries the substantive sentence), but the counter's sentence, "the entry
  carries a located quote … that the row's anchor carries", is weaker than the claim it is used to
  support.
- **F4 — `--fetch` does not gate the exit code.** With S204 pointed at `https://example.com/`, the
  run prints `S204: NOT FOUND`, `live quotes found 4 of 5`, and still exits 0 (returns on `n ==
  TOTAL` only). This matches the docstring's exit table, but the frozen predicate's "sourced" half
  is then only visible in stdout; a receipt that records only `exit=0` would hide a lost live quote.
  Record the printed `live quotes found N of 5` line in the receipt.
- **F5 — "the tip" must be a content commit.** `--rev a238989` (the plan commit, i.e. the lane tip
  while the entry is untracked) prints `0 of 5`, exit 1. The `5 of 5` measurement is only
  reproducible at a revision that contains the entry, `SOURCES.md` and `README.md` together: my
  sandbox commit `597ba2f1…` does. The C1 receipt must name that class of revision.
- **F6 — a crashing mutant aborts the battery.** M14 (dropped `row is None` guard) produces a
  traceback at world 5 and the remaining 13 assertions never run; the self-test still exits 1, so it
  is "killed", but the failure is not a reported `FAIL` and later worlds are unexercised. If the
  self-test is ever expected to be complete-run evidence, the worlds need per-world exception
  capture; if not, this is only a note on its failure mode.
- **F7 — kill attribution.** As shown above, M1 and M4 are killed by the honest assertion; their
  dedicated worlds discriminate a different conjunct. Not a defect, but do not cite those world
  lines as evidence that the `status`/`anchor` conjuncts are individually pinned.

Mutation score: **11 killed / 13 = 84.6%** (M14 counted killed, unclean), **2 survivors, both
demonstrated non-equivalent** (each has a revision the honest counter rejects and the mutant
accepts). Effective gap: the self-test pins 5 of the 7 record-level content conjuncts independently
and leaves the index-column and quote-cap rules to the honest world.

## Reproduce

```bash
git clone --shared --no-hardlinks /home/vgpnk/Projects/shokunin/kotoba-shokunin /tmp/k69-mut-c1
cd /tmp/k69-mut-c1 && git checkout --detach a238989a96cb0d2b939679126b832d75b861ca6e
# overlay the lane's honest working-tree draft (entry + corpus/SOURCES.md + corpus/README.md),
# commit sandbox-only as 597ba2f1…
python3 -B verifiers/check_skill_precedence.py --repo /tmp/k69-mut-c1 --self-test
python3 -B verifiers/mutants/M9_index_any_column.py --repo /tmp/k69-mut-c1 --self-test   # survives
python3 -B verifiers/check_skill_precedence.py --rev dc70184b38a58de95a788a5b2282940047664f61
python3 -B verifiers/mutants/M9_index_any_column.py --repo /tmp/k69-mut-c1 --rev dc70184b38a5…
```
