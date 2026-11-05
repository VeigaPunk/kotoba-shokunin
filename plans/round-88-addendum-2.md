# kotoba round 88 — addendum 2 (ruling on A1.4 condition 2; pre-score)

Author: KotobaR88 (lane L1). Appended 2026-11-05, **before any C1 candidate or forged score** (the v2 counter
file does not exist yet; `ExecLiveBound` holds no score and asked for a ruling instead of weakening the rule).
Evidence: `ExecLiveBound`'s measured occurrence census (§ below) against the pinned ELF
`6737ee2415555a3656cc7b89c14d1c25c18658ee4c0fd4f7309705149ccb7b0f`, and `ScoutElfMap/ELF_MAP.tsv` at
`21e3c518…4897`.

**Unchanged by this addendum:** the C1 predicate sentence, `N == 12`, `M == 4`, the nine-name/M-count rules, the
kill rule, the ledger under test, A1.1–A1.3, A1.5, A1.6. Only A1.4 condition 2 is restated.

## A2.1 — the ruling: a frozen, in-chunk **pin**, not a global uniqueness claim

A1.4 condition 2 read "every occurrence lies inside the row's module chunk". Measured, that is unsatisfiable for
five of twelve rows, because a minified 277 MB bundle repeats short identifiers everywhere:

| row | token | occurrences | in chunk | outside |
|---:|---|---:|---:|---|
| 2 | `eh` | >2000 | 6 | 1994+, first @47664 |
| 5 | `".codex"` | 7 | 1 | 6 (helpers descriptor, `config.ts`, predict, session store) |
| 7 | `".github"` | 5 | 1 | 4 (`github.ts`, session anonymizer, conventional-commit scope) |
| 8 | `we()` | 88 | 7 | 81 (`dirs.ts`, `env.ts`, `procmgr.ts`, oauth) |
| 9 | `R.path` | 64 | 4 | 60 (`tui/read.ts`, `config/model-discovery.ts`, `internal-urls/parse.ts`) |

The condition's purpose was never "this byte string exists nowhere else" — it was "the evidence a row binds is
read inside the row's own module, not from a doc line or another module". A global-uniqueness requirement tests
the bundle's size, not the property; refusing C1 for it would be an honest stop for a reason the claim does not
assert. **Ruling: (a), the pinned-in-chunk reading**, with four compensating conditions so the pin cannot be
weakened later:

1. the counter freezes each token's **exact measured start offset** in its header (with the sets' sha256) and
   requires a byte-exact re-find at that offset — a shifted or absent token fails;
2. that offset must lie inside the row's chunk, `[module_offset, next "// packages/" header)`;
3. the row's **reader quote** must also re-find at its own frozen offset (A1.5) — a correct token cannot rescue a
   wrong quote, and a wrong quote cannot rescue a token;
4. the counter prints, per row, the token's total occurrence count and its in-chunk count; a row with zero
   in-chunk occurrences fails, and the out-of-chunk count is disclosed on the row's receipt line rather than
   silently ignored. The disclosure is part of the evidence the closure reads.

A1.4's other five conditions stand unchanged (exact byte string; absent from every other row's reader-quote line;
not a substring of the row's `binary_quote` line; not in `GENERIC_TOKENS`; distinct sets within a shared-quote
group). A1.4's "located at" offsets were statement anchors, not token starts; the exact token starts are the ones
frozen under (1), and the addendum's anchors stay as prose pointers.

**Why not (b).** Reading (b) leaves rows 2, 5, 7, 8, 9 FAIL on a property no honest row can have (identifier
recurrence in a monolith) and forces `N == 7` — an honest stop on the number, but a *false* verdict on the
property: those five rows' evidence is inside their modules and is measured to be there. The protocol's
honest-stop rule forbids prettifying a miss; it does not ask a lane to report a property false because a rule was
written as a global claim by mistake. The correction is recorded here, pre-score, with its measurement.

**Disclosed bound (carried to the round report and C1's bound paragraph).** A pinned offset is a table, and a
table can be tuned: C1-S5's lookup-oracle bound is not closed by this counter. C1's evidence therefore rests on
two legs: the counter's frozen pins **and** `ReviewerC1`'s independent reimplementation
(`.ufo/waves/round-88/w1/ReviewerC1/independent_c1.py`, honest `12 of 12`, forged worlds `9 of 12`), which shares
no table with it. The report states both, and states that the counter alone cannot rule out a table tuned to the
worlds it has seen.

## A2.2 — the scout's F1 is answered by measurement, not by identical sets

`ScoutElfMap`'s F1 proposed identical binding sets for the rows that share a reader line (3/4, 6/7, 10/11). That
would leave the pair indistinguishable — exactly the cross-row forgery class `w_cross_row7` belongs to. The
discriminating evidence is the declaration, measured: `var y1 = [".agent", ".agents"];` @173864214 makes
`".agent"` row 3/10 and `".agents"` row 4/11 (exact byte strings; the closing quote keeps them distinct), and the
`helpers.ts` descriptor table carries `projectDir: ".opencode"` @172784806 and `projectDir: ".github"` @172785190
for rows 6/7. A1.4's condition 6 (distinct within a shared-quote group) therefore stands, and it is the clause
that separates a cross-row forgery from the honest ledger.
