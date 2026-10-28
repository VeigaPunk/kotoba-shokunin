# Kb80L01Grammar — external-commit grammar probe (scout, leaf)

## Assignment
Probe the grammar class that feeds E05 (repair 5 of claim C1). Run a bounded probe of BOTH
corpus gates' CURRENT commit-token handling at the round-80 base
`398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93` with ~20 synthetic shapes appended to a scratch
copy of a corpus file; for each shape, record which class each gate assigns. Publish the map
EARLY for Kb80E05GrammarFix.

## Method
- Scratch clone of the lane at base (`--shared`), toplevel asserted = the clone. Probe file
  `corpus/knowledge/z-grammar-probe.md` (24 lines, P01–P23) appended and `git add`ed (both
  gates enumerate corpus via `git ls-files corpus/`).
- Three resolution classes verified up front with `git cat-file -e <tok>^{commit}`:
  lane-present `398cbe1…` (in clone), fleet-present/lane-absent `33ee7933…` (in fleet root
  only), absent-both `a1b2c3d4…` / `0123…40` / `A1B2…40` / `a1b2c3d` / 41-hex.
- Both gates run from the LANE's verifiers/ against the clone; each command's OWN exit status
  captured (no pipeline — round-80 lesson M80-1). Both exit 1 on the probe (intentional defects).

## Result — the two gates AGREE on all 23 shapes (0 disagreements)

Delivered as a full table in `.ufo/waves/round-80/build/Kb80L01Grammar.md` (E05's spec input).
Headline mappings (integrity == independent in every row):

- `owner/repo@<hex>` prose with `@` OUTSIDE the backtick, no `commit` word (the live
  S050/S057/S062/S224/S225 form) → INVISIBLE (COMMIT_RE never fires).
- `commit `owner/repo@<hex>`` single backticked token (plus `@short`, reversed `<hex>@owner/repo`,
  `owner@<hex>` no-slash, `owner/repo@<fleet-hex>`) → **nonhash** (token not 7–40 hex).
- bare `commit `<hex>`` absent both → **unresolvable**; fleet-present → resolved; lane-present → resolved.
- `commit `HEAD:<path>`` → nonhash.  41-hex → nonhash.  7-hex + `…` → truncated.
- `commit `<hex>`` inside double quotes OR inside a double-backtick code span (the round-54
  spotcheck exact shape, bare-hex AND owner/repo@hex forms) → **quoted**.
- bare `<hex>`/owner-repo@hex fully backticked with no `commit` word, and `commit`+backtick
  glued with no space → INVISIBLE.
- 40-hex sha256-looking token (and its uppercase twin) → **unresolvable** (misread as a commit).

## Findings that matter to E05 / C1
1. The single-token `owner/repo@<hex>` grammar is `nonhash`, not `unresolvable` — it does not
   feed the red count today; E05's class for it is preventive and must also decide the
   `commit_nonhash` interaction.
2. The LIVE red at base is bare `commit `<hex>`` third-repo citations: SOURCES.md:171 and
   :172, both `7bb48f…` (S230 pi-mono, S231 mistral-vibe), absent from lane AND fleet.
3. **S231 is a bare `commit `7bb48f…`` with the repo named only in the row title/URL — no
   in-line owner/repo.** A grammar rule keyed on the token or same-line context cannot catch
   it. E05 must define how a bare unresolved `commit `<hex>`` is classified external vs broken.
4. 40-hex sha256-lookups are misclassified as commits (false-positive risk for digests).
5. Calibration discrepancy: the plan names `451a02ff`/`cfb894a5` as the unresolvable pair, but
   measured at base those are QUOTED (round-53/54 lessons); the red pair is `7bb48f` (S230/S231).
   Same class, different instances — flagged for the battery/claim of record.
6. Lane/fleet resolution behaves per plan (fleet fallback works); E05 must preserve it.

## Evidence (all under .ufo/waves/round-80/build/)
- `Kb80L01Grammar.md` — EARLY spec map / full 23-row table (E05 input).
- `Kb80L01Grammar-probe-lines.md` — the 24 probe lines (P01–P23).
- `Kb80L01Grammar-integrity-receipt.txt`, `Kb80L01Grammar-independent-receipt.txt` — human
  output + own exit status (both exit 1).
- `Kb80L01Grammar-integrity-probe.json`, `Kb80L01Grammar-independent-probe.json` — full observations.

## Commands
- `python3 -B verifiers/verify_corpus_integrity.py --repo <clone> --no-baseline --json` → exit 1
- `python3 -B verifiers/verify_corpus_independent.py --repo <clone> --json` → exit 1
- Verification facts: `git -C <clone> cat-file -e 398cbe1…^{commit}` present;
  `33ee7933…` absent in clone / present in fleet; `a1b2c3d4…`, `0123…40`, `A1B2…40`, `a1b2c3d`,
  41-hex absent in both; `451a02ff`, `cfb894a5`, `7bb48f…` absent in both.

No tools installed/upgraded (none needed). No host mutations. Scratch dir removed after
receipts copied. Coordination: replied to Kb80E10Battery (map is a spec, not a patch; E05 owns
patches) and Kb80E14C1Worlds (map published; key W5 facts).

VERDICT: Both corpus gates classify all 23 synthetic commit-token shapes IDENTICALLY; map published for E05, with the live-red form (bare commit `<hex>`, S231 lacking in-line owner/repo) and the nonhash-not-unresolvable owner/repo@<hex> single-token grammar flagged as the load-bearing facts.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar-probe-lines.md; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar-integrity-receipt.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar-independent-receipt.txt; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar-integrity-probe.json; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80L01Grammar-independent-probe.json
