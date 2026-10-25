# MutC1Counter — C1 counter mutation battery (round-68 wave 1)

Seat: mutation-tester (leaf, no dispatch). Axes named: **depth** (C1 counter conjunct
sensitivity — the assigned attack) and **consistency** (the counter's docstring vs its enforced
surface). Lane tree read-only throughout; every mutant is a /tmp scratch copy.

## Subject history (disclosed — the draft moved twice during this seat)

| state | bytes | status during run |
|---|---|---|
| absent | — | at T0 `.ufo/waves/round-68/w1/drafts/` did not exist |
| landed copy | `verifiers/check_client_trust_gates.py` @ `cafa29d`, sha256 `c68b0311…73483` | battery 1 (bytes pinned via `git show cafa29d:…`) |
| draft, rev 1 | sha256 `9909dc65…88626` | landed mid-run; battery 2 |
| **draft, rev 2 (current)** | sha256 `013b041e…373c2` | replaced mid-run; **battery 3 — primary table below** |

Each battery re-ran pristine baselines first; all were green (`backed 5 of 5`, exit 0, working-tree
and `--rev` arms), so every verdict below is conclusive. Verdict rule: **killed** = exit ≠ 0 with
a message naming the defect.

## Results — current draft bytes (013b041e…), primary

| # | mutant (scratch world) | expected | observed | verdict |
|---|---|---|---|---|
| a | entry's `source:` block moved out of opening (to EOF) | reject (conjunct 2: "opens with") | `backed 5 of 5` **exit 0** | **SURVIVED** — F3 |
| b | S199 `status` mined→queued | reject, message names status | `0 of 5` exit 1 — "S199: status is 'queued', expected 'mined'" | **KILLED — PASS** |
| c | S200 `source` cell altered, entry line no longer matches | reject | `0 of 5` exit 1 — "the row's source cell is not in the entry's source line" | **KILLED — PASS** |
| d | S201 located quote removed from `anchor` cell | reject | `0 of 5` exit 1 — "the per-client table row does not carry the located quote" | **KILLED — PASS** (F4) |
| e | `verified-at:` date changed | reject, 0 of 5 exit 1 | `0 of 5` exit 1 — "no `verified-at: 2026-10-24` line" | **KILLED — PASS** |
| f | coverage-map index row renamed | reject, 0 of 5 exit 1 | `0 of 5` exit 1 — "the entry has no coverage-map index row" | **KILLED — PASS** |
| g | client name changed, no longer matches the source row | reject | `5 of 5` **exit 0** | **SURVIVED** — F2 |
| g1 | client cell **emptied** in the per-client table | reject (conjunct 7: "client cell is filled") | `5 of 5` **exit 0** | **SURVIVED** — F1 |
| h | whole entry deleted (working-tree arm) | `0 of 5` exit 1, NOT exit 2 | `0 of 5` exit 1 — "entry missing: …" | **PASS** (R67-1 guard holds) |
| h′ | entry deleted at a valid `--rev` | same | `0 of 5` exit 1 | **PASS** |
| i | unknown revision `deadbeef×5` | exit 2 | exit 2 — "environment error: cannot read corpus/SOURCES.md at …" | **PASS** |

**Cross-version provenance (same mutants, other two byte-states):** intermediate draft
`9909dc65…`: (a) **KILLED** (`ENTRY_WINDOW=10` positional check — "no `source:` line naming an
S### id in the entry's first 10 lines"), (g)(g1) survived, b–f/h/h′/i identical verdicts.
Landed `c68b0311…`: (a)(g)(g1) survived, rest killed. I.e. rev 2 **regressed** rev 1's conjunct-2
enforcement back to the landed semantics.

## Findings — survivors are coverage findings, not contract changes

- **F1 — conjunct 7's "client cell is filled" is vacuous on the current bytes (g1), and the
  draft's own `--self-test` proves it.** Running the current draft's `--self-test`:
  `FAIL client-name-absent/count: got 5 want 0` · `FAIL …/findings-nonempty: got False want
  True` · `FAIL …/main-exit: got 0 want 1` — the self-test arm exits 1 (`5 failure(s) over 48
  assertions`). Mechanism (measured by probe): the emptied first cell is swallowed by row
  splitting. `_split_row(line[1:])` on `|  | gate… | "quote" | S199 |` yields **3 cells** whose
  `cells[0]` is the *gate* text, so `table_row[0].strip()` inspects the wrong cell; the
  intermediate draft's full-line `_split_row(line.strip())` kept 4 cells with `cells[0]==""`,
  defeating its `len(cells) >= 4` structural check the same way. Smallest fix shape (L1's call,
  wave-2 material): after splitting, require the client slot itself to be non-empty, or split
  pipes consistently so the slot index is stable.
- **F2 — client-name cross-match not enforced (g).** Renaming a client cell to a non-matching
  name keeps `5 of 5` exit 0 on all three byte-states. Documented as deliberate in the
  intermediate draft ("the client *name* is prose the counter deliberately does not hardcode");
  the current bytes' docstring instead claims conjunct 7's client cell is "filled" — F1 shows
  even that half is not enforced, so the current docstring overclaims its enforced surface.
- **F3 — conjunct 2 "opens with `source:` lines" is unenforced on the current bytes (a).**
  Mutant (a) moves the block to EOF; current draft and landed copy both still print `5 of 5`
  exit 0. The intermediate draft (`9909dc65…`) killed it — rev 2 dropped the `ENTRY_WINDOW`
  positional check while keeping the docstring claim. Either restore the window check or scope
  the docstring sentence to "carries `source:` lines".
- **F4 — (d) is killed, but at the table conjunct, not the anchor conjunct.** After S201's
  anchor loses its long quote, the only entry quote still inside the anchor is the short
  `"Security best practices"` (quoted in the entry's own `source:` line); no table row carries
  it, so the kill fires one conjunct downstream. Kill confirmed; the anchor conjunct alone is
  loose to short quotes that also appear in `source:` lines.
- **F5 — the current draft's self-test has one non-F1 fixture failure:**
  `FAIL class/unknown-rev/git-init: got False want True`. Host ruled out as the cause: global
  git identity is set and a bare `git init -q && git add && git commit` in /tmp succeeds
  (probe ran clean). Fixture bug in the arm, for the executor's list.

## Process disclosures

1. **False kill, caught.** Battery 2's first run had a path-prefix substitution bug: mutants
   c–g1 ran against nonexistent world dirs, so each printed the missing-entry default
   (`0 of 5` exit 1) — five fake kills. The identical outputs exposed it; worlds were rebuilt
   and the battery re-run. All tables above are from corrected runs.
2. **Moving target.** The draft was absent at T0, landed as rev 1, and was rewritten as rev 2
   during the seat. Each state's bytes were hashed before testing; verdicts attach to the hash
   they name. No verdict in this report spans a hash boundary.

## Restoration evidence

- Lane writes by this seat: this report file only. `git status --porcelain` after the batteries:
  the modified/untracked entries are concurrent-seat churn (sibling log appends, the draft
  revisions themselves, `controls/c2falsify-clone/`) — none authored here; no lane file I read
  was written; no git/jj mutating command was run in the lane.
- `verifiers/check_client_trust_gates.py` sha256 stable across the whole seat:
  `c68b03117f9f0fec1f2e76a91d9679c0c5e7993999bf035e5a58e5e58373e483`; lane-tip pristine run
  after the batteries: `client trust gates backed 5 of 5`, exit 0.
- Pristine bytes pinned per battery via `git show cafa29d:…`: entry `374847e5…0937`, SOURCES
  `3eedcecaa1adea18422e77cd0bc08d4b088596983887af25be10568dcb6a7122`, README
  `09bfd0c1…c2d` (`09bfd0c1e4fc9b16925f24a974f2feab9321619f357d1d9aab4c1d52e8b60c2d`); post-
  battery pristine re-run `5 of 5` exit 0 on every counter state.
- All mutants live only under `/tmp/mutc1/` (`world-*`, `d-world-*`, `d-revworld`, battery
  scripts, counter copies) — disposable scratch.
