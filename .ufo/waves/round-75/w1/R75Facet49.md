# R75Facet49 — the Gemini CLI threshold row's code-level negative claim

Seat `R75Facet49` (leaf; read-only; no delegation, no edits, no live fetch, no installs, no git/jj mutation).
Measured revision: `65a5c7a663249e0522cc49e4a148424200d9ddfe` (`git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin rev-parse HEAD`).
Named axes: **depth** (a claim asserted beyond its committed evidence base) and **freshness** (a five-day-old
vendor-code reading with no recheck mechanism). No claim about the other axes.

## Facet under audit

`SKILL.md:174` — the **Gemini CLI** row of § Description thresholds by client (heading `SKILL.md:164`), third
cell ("Past the threshold"):

> The loader keeps `frontmatter.description` as-is (`skillLoader.ts:211`) and the prompt template inserts it
> directly (`snippets.ts:320`) at `google-gemini/gemini-cli@451a02ff`; no description cut appears in these
> steps, so longer descriptions spend context.

The same clause is restated in the row's entry, `corpus/knowledge/skill-listing-thresholds-round54.md:44`
("no truncation at `skillLoader.ts:211` or `snippets.ts:320`, google-gemini/gemini-cli@`451a02ff`"). This is the
only row of the seven-client table that asserts a fact about vendor **source code** rather than about a
documented threshold; the other six are page statements.

## Observed (committed bytes)

| # | observation | evidence |
|---|---|---|
| O1 | The row landed in `ed3e899` (2026-10-22 20:17:25 -0300); it is five days old at today's date and unchanged since. | `git blame -L 170,176 --date=short -- SKILL.md` → line 174 prefixed `ed3e899 (kotoba-shokunin 2026-10-22 …)`; `git log -1 --format='%h %ci' ed3e899` → `ed3e899 2026-10-22 20:17:25 -0300` |
| O2 | The commit pin is an **8-hex abbreviation**. The full 40-char hash of that commit exists in this repo only inside two URL cells for a different artefact (`docs/cli/gemini-md.md`), not for the two skill files this row cites. | `grep -rnoE 'gemini-cli@`?[0-9a-f]{7,12}`?|`451a02ff`' SKILL.md corpus/knowledge/*.md` → `SKILL.md:174`, `corpus/knowledge/alwayson-rule-files-round53.md:1`, `corpus/knowledge/skill-listing-thresholds-round54.md:29`, `:44` — all short form; `grep -rno '451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1' corpus/SOURCES.md SKILL.md corpus/knowledge/skill-listing-thresholds-round54.md` → `corpus/SOURCES.md:59`, `corpus/SOURCES.md:73` only (rows S046, S060, gemini-md.md) |
| O3 | **No committed snapshot of either cited file exists.** The only committed record of the fetch is seat prose. | `git ls-files \| grep -iE 'gemini\|skillLoader\|snippets'` → seat reports only (`.ufo/waves/round-54/build/SrcGeminiCLI.md`, `.ufo/waves/round-54/falsify/W2SrcGeminiCLI.md`, `.ufo/waves/round-55/build/ScribeC1Cells.md`, …); `git ls-files '.ufo/waves/*/snapshots/*' \| wc -l` → 149 files across rounds 59–74 (S096–S101, S103–S109, S112–S115, S118–S120, S209–S211, the r73 Chinese-vendor pages with `MANIFEST.sha256`, and r74's `best-practices/quickstart/using-scripts.md` + `MANIFEST.sha256`); none for the Gemini TS files |
| O4 | The fetch record is complete but unrepeatable from the repo: URL, HTTP 200, byte counts and sha256 are in a seat report; the fetched bytes went to **scratch**, not a commit. | `.ufo/waves/round-55/build/ScribeC1Cells.md:67-70` — `skillLoader.ts` 6,560 B sha256 `8bce3215263e9ec06f32a865715c04af6deb4b6299db1490665f53972d4326f9`, quote at `:211` `description: frontmatter.description,`; `snippets.ts` 70,505 B sha256 `b2cccbd0cf68e33d057f33938e457fe3c781cc7e65c593f7a3974d70c5c68fe7e`, quote at `:320` `<description>${skill.description}</description>`; both written under `/fast/scratch/hyaku/kotoba-r55/ScribeC1Cells/sources/` |
| O5 | The frozen counter for this table **does not read the code clause**. It reads: one SKILL row per client; ≥1 number token in the *threshold* cell; a non-empty action cell; the entry's single `S###` row, tier `A`, kind docs/spec/code, status `mined`, `opened == 2026-10-22`, `used-by` naming the entry, host allowlist; and the entry quote (3–25 words, holding one of the threshold-cell numbers, recorded in the round-54 Gate). With `--fetch` it fetches the **first URL of the S057 source cell** — the served docs page — never the two `raw.githubusercontent.com` code URLs. | `verifiers/check_description_thresholds.py:281-283` (`tokens = NUM_RE.findall(sr[1])`), `:286-330` (entry/registry/quote), `:496` (`found = norm(r["quote"]) in page`); `grep -rln 'skillLoader\|snippets\.ts' verifiers/` → **no output** |
| O6 | The entry's own § Limits discloses the docs-half boundary ("nothing is cut" is a source reading, not a run) but not the code-half evidence gap. | `corpus/knowledge/skill-listing-thresholds-round54.md:60-67`, closing line 67: "No client was run; \"nothing is cut\" for Gemini CLI and opencode comes from reading source, not from a run." |
| O7 | The entry records that the vendor documents a **replacement for a user segment** and asks for a short recheck cadence; `SKILL.md:174` carries neither the qualifier nor the replacement. | `corpus/knowledge/skill-listing-thresholds-round54.md:29-31`: "…replaced by Antigravity CLI on 2026-06-18 … so the recheck cadence for S057 should be short"; `SKILL.md:174` threshold cell reads flatly "No threshold" |
| O8 | The entry carries **no `source:` / `verified-at:` / `recheck:` header block**; `grep -n 'recheck\|verified-at\|^source:'` returns only the prose sentence at line 31. | command as written; file head `:1-9` is a title plus prose with a `../SOURCES.md` pointer |
| O9 | The lane's own rule for this class of citation is in the same file. | `SKILL.md:54-56`: "Cited line numbers are points-in-time. Verify before trusting: if a cited line has drifted, re-read the file and update the citation — do not propagate a claim whose source moved." |

The docs half of the row **is** backed in committed bytes: S057 (`corpus/SOURCES.md:70`) is a tier-A `mined`
row with a served-page URL, byte count 3,257 B, sha256 `612c3b83…`, and the quote is recorded at
`corpus/lessons/round-54.md:27`. Only the code half lacks committed evidence.

## Assessment

**Factual support.** Split. The threshold cell ("No threshold", ~100 words as a size estimate) is supported by
S057 and re-checkable by the counter's `--fetch` arm. The "past the threshold" cell asserts three code facts —
`description` is copied as-is at `skillLoader.ts:211`; it is interpolated whole at `snippets.ts:320`; no cut
appears in those steps — and its evidence is two lane seats' readings of a fetch taken on 2026-10-22/23, with
no committed bytes (`O3`, `O4`). Two seats agreeing (`round-54/falsify/W2SrcGeminiCLI.md:37` re-read the same
lines) is corroboration of a reading, not a committed artefact.

**Falsifiability.** The negative is falsifiable in principle: a `description.slice(…)`, `substring`, or a
length guard in either file at the pinned commit would refute it, and a later vendor change would too. But
nothing in the repository can decide it today without the network, and nothing turns red if the vendor adds a
cut — the counter never opens those files (`O5`). So the row's most load-bearing clause is the one the audit
surface cannot measure.

**Scope.** Two gaps beyond the (correctly narrow) "in these steps" hedge. (a) The row states a product-level
"No threshold" while the entry records a documented replacement for unpaid-tier and Google One users and a
requested short cadence (`O7`); an auditor reading `SKILL.md` alone gets a currency the source does not carry.
(b) The pin is an 8-char abbreviation at the citation site (`O2`), weaker than the registry's own full-hash
form for the same commit, and weaker than `SKILL.md:54-56` asks (`O9`).

**Control weakness.** The table presents seven rows in one shape; six rest on a documented page, one on a code
reading. The counter's PASS for the Gemini row therefore certifies the docs quote and the registry row only
(`O5`) — the Q31/Q51 boundary, which the entry's § Limits half-states (`O6`) but which `SKILL.md:174` does not
mark at all. An r75 audit that counts "§ Description thresholds by client backed 7 of 7" or "tokens 7 of 7"
as sourced depth inherits that gap: the one clause that distinguishes this row from the page-only rows is
exactly the clause no conjunct reads.

## Concrete check / control (design; nothing executed here)

**(C1) Pin-form check — runnable today, committed bytes only.**

```
grep -nE 'gemini-cli@`?[0-9a-f]{7,12}`?' SKILL.md corpus/knowledge/*.md
```

Criterion: every hit must carry the 40-char commit (or the words `point-in-time`) in the same cell/line.
Measured now: four hits, zero with the full hash → the two rows that assert the code fact (`SKILL.md:174`,
`corpus/knowledge/skill-listing-thresholds-round54.md:44`) fail; `alwayson-rule-files-round53.md:1` fails the
form but its S046 URL carries the full hash, so it is a mechanical hit, not a defect. The check is cheap,
mechanical, and fails on exactly the audited rows.

**(C2) Negative-claim falsifier — snapshot arm, no fetch in this round.**

Capture `packages/core/src/skills/skillLoader.ts` and `packages/core/src/prompts/snippets.ts` at
`451a02ff03f1d2a8fe870c120fd5342cfd6f9fd1` into a wave snapshot dir with `MANIFEST.sha256`, then a counter arm
that asserts all of: (a) line 211 holds `description: frontmatter.description,` and line 320 holds
`<description>${skill.description}</description>`; (b) `grep -cE 'description\.(slice|substring|substr)|\.slice\(0, *[0-9]+\)'`
over both files is 0; (c) the snapshot sha256 equals the manifest pin.

- Red-before: today no snapshot exists, so the arm reads **could-not-evaluate (2)** — the honest measurement of
  the gap, not a pass. The row itself is unchanged either way.
- Do-nothing control: deleting the snapshot must yield 2, not 0.
- Shortcut worlds (real-input, per Q37), each must score below clean: (i) a snapshot of **current `main`** where
  both lines still read identically — passes (a) and (b) and is killed only by (c); this is why the counter must
  bind the sha, not the line location; (ii) a snapshot with `description.slice(0, 1024)` injected — killed by
  (b); (iii) a snapshot with the lines shifted by one — killed by (a); (iv) the docs snapshot
  (`skills-best-practices.md`) submitted in the code snapshot's place — killed by (a)+(c), and the counter must
  refuse a `.md` page for a `.ts` path.

**(C3) Freshness mechanism for this row.**

Add `recheck: 30d — <command>` beside the code claim (entry header or a pointer from `SKILL.md:174`), where the
command re-fetches the two files at the pinned commit and diffs against the snapshot; a changed page is a
re-open, not a silent swap. Audit criterion: a row asserting a vendor-code negative with no snapshot and no
recheck is `improved-bounded`/"reviewer reading", never `sourced`; and a row whose own entry documents a vendor
replacement (O7) must carry the qualifier or lose its "current" reading.

## Risks and limits

- No live fetch was made (lane bound). I have not re-confirmed that the two lines still read as quoted at
  `451a02ff` today, nor that upstream has not moved; O4 is the r55 seat's recorded fetch, not mine.
- I did not run `check_description_thresholds.py`. O5 is a reading of its committed source at `65a5c7a`; a gate
  run is the parent's, not this seat's.
- The two code URLs may be rate-limited or 404 on a re-fetch; C2's red-before (2) covers that as
  could-not-evaluate rather than a false red.
- "No description cut appears in these steps" is a statement about two functions, not about the CLI at runtime
  (a plugin, a later pipeline stage, or the `/skills` UI could cut). C2 must not be widened into a runtime
  claim.
- O8 (no provenance trio in the r54 entry) is stated as an observation; whether `corpus/QUALITY.md` Q12 admits
  that entry's prose form is a bar-reading question I did not adjudicate, and it is not required for this facet.

## Axes

- **depth** — candidate: one row claims a code fact with lane prose as its only evidence (0 committed bytes for
  the two files), and the table's counter certifies the page half only. A "backed N of 7" headline would
  over-credit it.
- **freshness** — candidate: a five-day-old vendor-code reading with no `recheck`, pinned by an 8-char
  abbreviation, while the same entry records a vendor replacement for a user segment that the SKILL row drops.
- No harm claimed to consistency, calibration, operability or adjacency; nothing was edited.

Report path (relative to `kotoba-shokunin`): `.ufo/waves/round-75/w1/R75Facet49.md`
