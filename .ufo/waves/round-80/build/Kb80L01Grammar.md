# Kb80L01Grammar — external-commit grammar probe map (E05 spec input)

Status: EARLY publish for Kb80E05GrammarFix. Probe of BOTH corpus gates' CURRENT
commit-token handling at the round-80 base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`.
23 synthetic shapes appended to a scratch copy of a corpus file; both gates run against
the scratch clone. **The two gates AGREE on all 23 shapes** (0 disagreements).

## How to read this

Each gate's commit classifier pipeline (per line, per `commit `<token>`` match):

1. `COMMIT_RE` must match (the word `commit`, not preceded by `[A-Za-z0-9_-]`, then
   whitespace, then a backticked token). **No match → the gate never sees the shape
   ("INVISIBLE").**
   - integrity `COMMIT_RE = (?<![A-Za-z0-9_-])commit[ \t]+\`([^\`\n]+)\``  (token may contain spaces)
   - independent `COMMIT_RE = (?<![A-Za-z0-9_-])commit\s+\`([^\`\s]+)\`` (token no whitespace)
2. If the citation is inside double quotes OR inside a Markdown code span (backtick run)
   → **quoted** (context; INFO, not a defect).
3. Else if token is 7–40 hex + U+2026 ellipsis → **truncated** (context).
4. Else if token is NOT 7–40 hex → **nonhash** (DEFECT).
5. Else (7–40 hex): `git cat-file -e <tok>^{commit}` against lane repo, then fleet root.
   - resolves in either → **resolved** (counted in `commit_total`, no defect)
   - fails both → **unresolvable** (DEFECT)

The NEW r80 "external commit citation" INFO class (E05, repair 5) does NOT exist yet.
This table records what each shape maps to **today**, so E05 can see exactly what moves.

## Classification table (23 probes; probe file line = P# + 1)

Absent-both hex used as the "third repo" object: `a1b2c3d4e5f60718293a4b5c6d7e8f90a1b2c3d4`.
Fleet-only commit: `33ee79336683f4abf4ae1448b751b17f3b84f7d5` (fleet-present, lane-absent).
Lane commit: `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`; short `398cbe1`.

| P# | Shape (exact bytes, `@`=literal at-sign) | integrity | independent |
|----|--------------------------------------------|-----------|-------------|
| P01 | `third-owner/third-repo@` + `` `a1b2…` `` — prose, `@` OUTSIDE backtick, NO `commit` word (the live S050/S057/S062/S224/S225 form) | INVISIBLE | INVISIBLE |
| P02 | ``commit `third-owner/third-repo@a1b2…``` — owner/repo@<hex> as ONE backticked citation token | nonhash | nonhash |
| P03 | ``…`third-owner/third-repo` commit `a1b2…``` — owner/repo in a SEPARATE backtick, then bare `commit `<hex>`` (the LIVE S230 form) | **unresolvable** | **unresolvable** |
| P04 | ``commit `a1b2…``` — bare <hex> lane-absent (absent both) | **unresolvable** | **unresolvable** |
| P05 | ``commit `33ee7933…``` — bare <hex> fleet-present | resolved (fleet) | resolved (fleet) |
| P06 | ``commit `398cbe1b…``` — bare <hex> lane-present | resolved (lane) | resolved (lane) |
| P07 | ``commit `HEAD:corpus/README.md``` — `HEAD:<path>` | nonhash | nonhash |
| P08 | ``commit `third-owner/third-repo@a1b2c3d``` — owner/repo@<short 7-hex> | nonhash | nonhash |
| P09 | ``commit `a1b2…@third-owner/third-repo``` — <hex>@owner/repo REVERSED | nonhash | nonhash |
| P10 | ``commit `0123…40hex``` — 40-hex sha256-LOOKING, absent both | **unresolvable** | **unresolvable** |
| P11 | ``commit `third-owner@a1b2…``` — owner@<hex>, NO slash | nonhash | nonhash |
| P12 | `` `` commit `a1b2…` `` `` — bare commit `hex` inside DOUBLE-backtick span (round-54 spotcheck exact shape) | quoted | quoted |
| P13 | `"commit `a1b2…`"` — commit `hex` inside double QUOTES | quoted | quoted |
| P14 | ``commit `a1b2c3d…``` — 7-hex + U+2026 | truncated | truncated |
| P15 | ``commit `a1b2c3d``` — bare 7-hex, absent both | **unresolvable** | **unresolvable** |
| P16 | ``commit `398cbe1``` — bare 7-hex, lane-present | resolved (lane) | resolved (lane) |
| P17 | bare `` `a1b2…` `` hex token, NO `commit` word | INVISIBLE | INVISIBLE |
| P18 | ``commit `third-owner/third-repo@33ee7933…``` — owner/repo@<fleet-hex>; note token is non-pure-hex so resolution never runs | nonhash | nonhash |
| P19 | `` `third-owner/third-repo@a1b2…` `` — owner/repo@<hex> fully backticked, NO `commit` word | INVISIBLE | INVISIBLE |
| P20 | `commit` + `` `a1b2…` `` GLUED (no space) | INVISIBLE | INVISIBLE |
| P21 | ``commit `a1b2…e``` — 41-hex (too long) | nonhash | nonhash |
| P22 | ``commit `A1B2…40hex``` — UPPERCASE 40-hex, absent both | **unresolvable** | **unresolvable** |
| P23 | `` `` commit `third-owner/third-repo@a1b2…` `` `` — owner/repo@<hex> inside DOUBLE-backtick span | quoted | quoted |

## Findings that drive E05

1. **The single-token `owner/repo@<hex>` grammar is `nonhash`, NOT `unresolvable`.**
   P02/P08/P09/P11/P18 (any `commit `owner/repo@<hex>`` / `@`-variants with the `commit`
   trigger) land in `commit_nonhash` because the token is not 7–40 hex. So this grammar
   does NOT feed the red `commit_unresolvable` count today — the E05 class for it is
   preventive, and must ALSO keep it from inflating `commit_nonhash` if that is the intent.

2. **The LIVE red at base is bare `commit `<hex>`` third-repo citations (P03/P04 form),**
   currently `corpus/SOURCES.md:171` and `:172`, both token `7bb48f213ac677f943d5c791199ed3dddf302f00`
   (pi-mono S230, mistral-vibe S231). Both absent from lane AND fleet (verified `cat-file`).

3. **CRITICAL context asymmetry between the two live tokens:**
   - S230 (`:171`) HAS the owner/repo in-line: `` `badlogic/pi-mono` commit `7bb48f…` `` (P03 form).
   - S231 (`:172`) is a BARE ``commit `7bb48f…` `` with the repo named ONLY in the row
     title/URL (`mistralai/mistral-vibe`), NOT on the citation line.
   A grammar class keyed only on the citation token, or only on same-line `owner/repo`
   context, CANNOT catch S231. E05 must decide how a bare `commit `<hex>`` with neither
   lane nor fleet resolution is distinguished as "external" (Q61: absent from both *by
   construction* for a third-repo object) vs a genuinely broken lane/fleet citation.

4. **sha256-looking 40-hex is mistaken for a commit (P10, P22 → unresolvable).** Any
   40-hex token (a truncated sha256, a digest) in a `commit `<token>`` citation is tested
   by `cat-file` and, if absent, reported `unresolvable`. Integrity lowercases before
   resolve (`token.lower()`); git hex is case-insensitive, so P22 (uppercase) is also
   unresolvable. E05's red-before arms should note this is reachable.

5. **Plan-vs-measured naming discrepancy (calibration note for the battery/claim).** The
   plan §Trigger names the two `commit_unresolvable` tokens as
   `google-gemini/gemini-cli@451a02ff` and `zed-industries/zed@cfb894a5`. Measured at base
   those two are in the **quoted** class (round-53/54 lessons, quoted meta-findings); the
   two LIVE `commit_unresolvable` tokens are `7bb48f…` (S230/S231). All three objects
   (451a02ff, cfb894a5, 7bb48f) are absent from lane and fleet (verified). The class is the
   same; the instances named in the plan are not the currently-red ones.

6. **`owner/repo@<hex>` with `@` outside the backtick (P01) — the dominant live form — is
   INVISIBLE** to both gates (no `commit` trigger word). The round-53 lesson (M45) records
   that rewriting a bare `commit `<hex>`` citation into this `@`-outside form clears the
   gate. E05 should be aware this form is the corpus's chosen way to cite third-repo
   commits inertly; whether it should now be *classified* (INFO) rather than invisible is
   a design choice for the plan's "or otherwise an explicit third-repository citation".

7. **Resolved set behaves per plan (P05/P06/P16):** lane-present and fleet-present hex
   resolve; the fleet fallback works. E05 must not disturb these (repair 5: "lane and
   fleet hex tokens keep the exact current resolution behavior").

## Reproduce

- Scratch clone at base; probe file `corpus/knowledge/z-grammar-probe.md` (24 lines,
  P01–P23) `git add`ed. Run from LANE verifiers/:
  - `python3 -B verifiers/verify_corpus_integrity.py --repo <clone> --no-baseline --json`
  - `python3 -B verifiers/verify_corpus_independent.py --repo <clone> --json`
- Receipts: `Kb80L01Grammar-integrity-receipt.txt`, `Kb80L01Grammar-independent-receipt.txt`
  (own exit status captured, no pipeline). Full JSON: `Kb80L01Grammar-{integrity,independent}-probe.json`.
  Probe lines: `Kb80L01Grammar-probe-lines.md`. Both gates exit 1 on the probe (intentional defects).

Seat: Kb80L01Grammar (scout). Leaf seat; no subagents.
