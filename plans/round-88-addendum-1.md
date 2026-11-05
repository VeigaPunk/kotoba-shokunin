# kotoba round 88 — addendum 1 (pre-score execution rules for C1)

Author: KotobaR88 (lane L1). Appended 2026-11-05, **before any C1 candidate or forged score**.
Base/freeze: `plans/round-88.md` at lane `89579c775731a64a51260af76d7b192d11f719d1`.
Evidence: the wave-1 attack seats `CriticFalsify` (`.ufo/waves/round-88/w1/CriticFalsify/attacks.md`,
receipts under `…/CriticFalsify/receipts/`), `ScoutElfMap` (`.ufo/waves/round-88/w1/ScoutElfMap/ELF_MAP.tsv`)
and the L1's own ELF probes (receipts in `.ufo/waves/round-88/receipts/`).

**What this addendum may not do, and does not do.** It does not change the C1 predicate sentence, the target
(`N == 12` and `M == 4`), the denominator, the kill rule, or the ledger under test. It fixes **how** frozen
conjuncts 1–5 are executed, because the critic measured that the round-87 implementation of three of them is
satisfiable by a forgery the conjunct exists to refuse. No C1 score exists yet: `verifiers/check_omp_root_semantics_v2.py`
is absent at `89579c7` (`ls` → not found), so the pre-score window is open. Different-sized, fully grounded
forgery worlds in three further classes (A1.1, A1.2, A1.3) are added to the M count **as worlds**, not as new
target numbers: M stays 4 (the round-87 critic's four classes), and the three new classes land as `--self-test`
must-fail arms plus a fifth output line `forgery-class worlds rejected K of 7` that the report discloses and the
closure may weigh. `N == 12` is unchanged.

## A1.1 — S3 is anchored to a revision, not to `<rev>` (closes C1-S1)

`CriticFalsify` C1-S1: one scratch commit rewrote **both** ledgers, moving `~/.agents/skills` to
`/tmp/x/skills`, and the r87 counter read `12 of 12`, exit 0 — because S3 compares the semantics ledger's
pattern column with the round-86 ledger *at the same `<rev>`*, which the same commit can rewrite.

**Rule.** Conjunct 1 compares the row's `root_pattern` against **two** anchors:
(a) the row's pattern in `verifiers/omp-skill-roots.tsv` **at the frozen revision**
`223ae62424f8ab1eb365d733eb648d6228ddd7e8` (read with `git show <pin>:…`, never `<rev>`), and
(b) a frozen `PATTERN_SET` tuple in the counter source, whose sha256 the counter prints.
A revision that rewrites both ledgers fails (a) and (b). The counter names the pin in every receipt line.

## A1.2 — module provenance is the NEAREST preceding header (closes C1-S2)

C1-S2: `mod_row2` (`{cwd}/.claude/skills` relabelled `builtin.ts`) and `mod_row12`
(`~/.omp/agent/managed-skills` relabelled `helpers.ts`) both read `12 of 12`; the r87 conjunct accepts 47 of 84
(row, module) pairs because it only asks that *some* header precede the quote.

**Rule.** For the row's reader quote, the counter takes the reader's first occurrence and finds the **nearest**
preceding `// packages/<module>` header; the row's `module` must equal it, and the reader occurrence must lie
before the next header. The critic's `nearest.py` shows all 12 honest rows already agree with the nearest
preceding header, so this costs the honest ledger nothing.

## A1.3 — `$HOME` containment for every row, not only `{cwd}/` and `~/` (closes C1-S4)

C1-S4: `/etc/skills`, `/tmp/x/skills` and `~root/skills` passed conjuncts 1 and 4 (`pattern_problem=None`,
`bound=True`) — an escape with no `..` segment.

**Rule.** A pattern's first segment must be `{cwd}`, `~`, a bare relative name, or one of the ledger's frozen
patterns. Absolute patterns (`/…`) and `~user` patterns are refused outright. For every row, every expanded
candidate root must lie under the session cwd's ancestors strictly below `$HOME` (for `{cwd}/`) or under `$HOME`
(for `~`), after normalization; a candidate at or above `$HOME` is refused unless the row is a `~` row, and a
`~{}`-row candidate above `$HOME` is refused always.

## A1.4 — binding token sets, stated exactly (closes C1-S3's generic-token door)

C1-S3: `cwd` (produced by the `{cwd}` placeholder) and `skills` (a segment of the row's own literal) are legal
under the frozen wording, and both accept a forged world. The rule below keeps the wording ("a token the row's
root literal or its declared reader variable produces") and forbids the generic reading.

**Rule.** Each row carries a **single-token** frozen set. A token binds only if all of:
1. it occurs in the pinned ELF as an exact byte string (quotes included where the literal has them);
2. every occurrence lies inside the row's module chunk — the nearest preceding header (A1.2) through the next
   `// packages/` header;
3. it is absent from **every other row's** reader-quote line;
4. it is not a substring of the row's `binary_quote` line (a doc/string-table line may not bind its own row);
5. it is not in `GENERIC_TOKENS = {cwd, join, skills, path, dir, home, projectDir, userAgent, userBase,
   node_modules, n, p, u, k, e, t, R, x, _}`;
6. within a group of rows sharing one reader quote and one prefix class, the sets differ (rows 3/4, 6/7, 10/11).

**The twelve sets** (measured this round; offsets are the L1's and `ScoutElfMap`'s, both re-findable):

| row | `root_pattern` | binding token | located at |
|---:|---|---|---|
| 1 | `{cwd}/.omp/skills` | `Ou.projectDir` | reader line @173819979 |
| 2 | `{cwd}/.claude/skills` | `eh` | reader line @173840364 |
| 3 | `{cwd}/.agent/skills` | `".agent"` | `var y1 = [".agent", ".agents"];` @173864214 |
| 4 | `{cwd}/.agents/skills` | `".agents"` | same statement @173864221 |
| 5 | `{cwd}/.codex/skills` | `".codex"` | reader line @173879095 |
| 6 | `{cwd}/.opencode/skills` | `".opencode"` | descriptor @172784806 |
| 7 | `{cwd}/.github/skills` | `".github"` | descriptor @172785190 |
| 8 | `~/.omp/agent/skills` | `we()` | reader line @173820135 |
| 9 | `~/.omp/plugins/node_modules/*/skills` | `R.path` | reader line @173914936 |
| 10 | `~/.agent/skills` | `".agent"` | `var y1 = …` @173864214 |
| 11 | `~/.agents/skills` | `".agents"` | same statement @173864221 |
| 12 | `~/.omp/agent/managed-skills` | `"managed-skills"` | reader line @173809938 |

Rows 3/4 and 10/11 share a token across prefix classes but not within one; rows 6/7 and 3/4 differ within their
group; every token is either on its own reader line or a distinct literal inside its own module chunk.
`".agent"` and `".agents"` are distinct byte strings (the closing quote is part of the token), which is what
separates them under an exact-match test.

## A1.5 — per-row ELF offsets are frozen and re-derived (closes C1-S2's sibling class, `w_subdir_row9`)

**Rule.** The counter stores one frozen offset per row — the reader quote's first occurrence — and refuses the
row when the pin does not re-find at that offset. `w_subdir_row9`'s shifted offset then fails instead of passing.
The frozen offsets are the `reader_offset` column of `ScoutElfMap/ELF_MAP.tsv` at sha256
`7ceb720622f2120895b2b93c430d55762ade0570447cdf3ab767287f98f16dd8`.

## A1.6 — controls, stated before the first score

- **must-pass:** the honest ledger at the landing revision → `N == 12`, `M == 4`, guards S1–S5 PASS, exit 0. A
  counter that refuses everything cannot satisfy it (blanket-refusal control).
- **must-fail (M):** `w_cross_row7`, `w_subdir_row9`, `w_misattr_row12`, `w_renderline_row6` (the round-87
  critic's four classes, rebuilt by `ExecForgeryWorlds`).
- **must-fail (K, disclosed):** `w_both_ledgers` (C1-S1), `w_module_mislabel` (C1-S2), `w_home_escape` (C1-S4,
  three patterns `/etc/skills`, `/tmp/x/skills`, `~root/skills`).
- **lookup-oracle bound (C1-S5):** disclosed, not claimed as closed. The counter's honesty rests on the
  independent re-derivation the reviewer seat performs (`ReviewerC1/independent_c1.py`), not on the counter's
  own tables; the report states that in C1's bound paragraph.

## A1.7 — C2 is NOT amended (the kill rule binds)

`verifiers/check_r86_routed_repairs_v2.py` has been scored at the tip (`5 of 5`, exit 0) and against seven
control worlds by an attack seat. Under `plans/round-88.md` § C2's kill rule, a counter or fixture change after
the first candidate score kills C2, so **this addendum amends nothing on the C2 side**. The critic's C2-S2
(in-place silencing passes (i)) and C2-S3 (re-recorded `corpus-baseline.json` passes) are therefore recorded as
**blocking survivors against the frozen text's own "a silenced or removed check fails (i)" clause** — the v2
implementation compares name sets only and does not implement that clause. C2's disposition in this round is an
honest stop with the repair routed to round 89 (v3: (i) additionally requires the integrity script's own
`--self-test` green at `<rev>` and `verifiers/corpus-baseline.json`'s blob equal to the base's); the frozen
target `5 of 5` is reported as measured **and** the claim as not verified, never narrowed.

## A1.8 — erratum (appended after A1.5 was committed; no rule changes)

A1.5's receipt pointer cites `ScoutElfMap/ELF_MAP.tsv` at sha256 `7ceb7206…f16dd8`. That digest is the scout's
mid-flight print, not the table's final bytes. Measured at the commit that lands this addendum:

    $ sha256sum .ufo/waves/round-88/w1/ScoutElfMap/ELF_MAP.tsv
      21e3c518df2eafc17a233ad4232b7b0a852db47f9a9be522acf32ab938444897
    $ git diff f300d895 -- .ufo/waves/round-88/w1/ScoutElfMap/ELF_MAP.tsv   -> (empty)

The frozen `reader_offset` column is read from the table at **`21e3c518…4897`** (marker file `ELF_MAP_READY`
carries the same digest). A1.5's rule stands unchanged; only its pointer is corrected here, append-only.
