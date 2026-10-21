verdict: The round-47 LOG.md entry can be appended with **zero new dead governance citations** — measured, not asserted — provided (a) it is appended at the **tail** of `LOG.md` (never above `LOG.md:2111`, whose line number and bytes C3's erratum key binds), and (b) the 5–6 not-yet-existing path tokens it names exist at landing; two operational traps remain open for the integrator (the untracked `.ufo/waves/` tree, and the substrate counting command's resolution), and the entry text must be re-checked against the gate after it is pasted because its own tokens change the count.

BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (branch `master`, jj-colocated lane). All
`path:line` references below are at BASE unless stated. Nothing in the lane repo was modified:
this seat wrote only `.ufo/waves/round-47/build/RevLogAppend.md`,
`.ufo/waves/round-47/build/RevLogAppend.proposed-entry.md` and
`.ufo/waves/round-47/build/RevLogAppend.token-inventory.json`; all code drafts live in the
scratch clone `/fast/scratch/kotoba-r47/RevLogAppend/lane` (detached at BASE), scripts
`scratch_r47/check_tokens.py` and `scratch_r47/mirror_build.py`. No git add/commit/stash/checkout
in the lane repo, no jj mutation, no subagent dispatch.

---

## HIGH-1 — the append must be a **tail** append; anything inserted above `LOG.md:2111` breaks C3's erratum key

C3's erratum registry is specified (`.ufo/waves/round-47/build-spec.json`, item `C3ErrataImpl`) as
keying each excused dead citation on **file + line + token + sha256 of the exact line bytes**, with a
stale erratum (line moved, sha changed, token now resolves, line no longer cites the token) failing
loudly. `LOG.md:2111` is the one live dead token:

```
LOG.md:2111  - At `2026-10-19T19:38:15Z`, the census replay command
              `python3 .ufo/round-45/drafts/v10/post-r44-hunt.py` and its two documented R41 draft
              replay commands each exited 2 because the referenced runners are absent. …
```

Measured (`sha256` over the exact line bytes, `LOG.md` ends with a newline, 2315 lines total):

| variant | value |
|---|---|
| sha256 of line 2111 **with** trailing `\n` | `d7b4c6289e30ad0d9c23554c066742802d5c325f9bea9929dce5fa717d981c7a` |
| sha256 of line 2111 **without** trailing `\n` | `7dcbf123313d46c469cab9f5dac2daa7567e54ac1ddf7cffdd1fd38c74200135` |

Counterexample (measured): a **tail** append leaves both the line number (2111) and the line bytes
(`d7b4c628…`) unchanged → the erratum stays valid. Inserting two lines **above** 2111 moves it to
2113 → the file+line key no longer matches even though the bytes are identical → under the C3 design
that is a *stale erratum* → the gate FAILs. The round-47 entry must therefore be written **after
the last line of `LOG.md`**, and must not be inserted by date near the top of the file (round 47 is
dated later than every existing entry, so "chronological insertion" and "tail append" happen to
coincide here — do not rely on that).

This is also the PROTOCOL's own rule, and the entry must not be used to "fix" it:

- `PROTOCOL.md:463` — “`LOG.md` is append-only: entries are never rewritten or deleted; corrections
  land as new entries.”
- `PROTOCOL.md:124` — “append-only files (`LOG.md`) take an appended correction entry pointing at
  the superseded text, never an in-place rewrite.”
- `PROTOCOL.md:135-136` — a correction lands “as an erratum appended after the filed bytes in a new
  commit and naming the text it supersedes — never a rewrite of the filed bytes”.
- `PROTOCOL.md:366-367` — “A falsified claim in an append-only file gets a named correction entry in
  the lane's next round — appended, never rewritten; it stays on the routed-defect queue until it
  lands.”
- `PROTOCOL.md:462` — “Rounds are evidence-driven: every `LOG.md` entry cites the work that
  motivated it.”
- `PROTOCOL.md:431` — the `LOG.md` file row: “Append-only iteration log: round entries, accepted
  changes, falsifiable next-iterations”.

**Consequence for C3:** the erratum registry must record the line number *and* the line-sha **of the
line as it stands after the round-47 append** — which, for a tail append, is identical to BASE
(`d7b4c628…` with `\n`). The C3 executor should also state explicitly whether the registered sha
includes the trailing newline; both values are listed above so the registry cannot silently pick the
wrong one and then "fail closed" against its own row.

## HIGH-2 — 5–6 path tokens in the proposed entry do not exist at BASE; each is a new dead citation if it is still missing at landing

The gate's rules were read from the shipped instrument, not guessed:
`verifiers/verify_skill_checklist.py:347` (`CITATION_ROOTS = ("corpus/", "verifiers/", "opencode/",
".ufo/", "../")`), `:348` (`GOVERNANCE_FILES = ("LOG.md", "SCORECARD.md")`), `:349`
(`SCHEMATIC_CITATION_RE`), `:843-862` (`safe_resolve`), `:1295-1315` (`citation_resolve`),
`:1378-1425` (`citation_subjects`), `:1454-1495` (`check_governance_citations`). A token is a
subject when it is a whitespace-separated word of a backticked span, starts with a citation root,
contains a `/`, and carries none of `< > * ? $`; it is excluded when it is double-quoted on its own
line (a “historical/meta finding”) or is schematic (`…`, `...`, or a literal `round-N` path segment).

Proposed entry (full text: `.ufo/waves/round-47/build/RevLogAppend.proposed-entry.md`), 19
evaluated subjects, 0 quoted/schematic exclusions:

| token | at BASE |
|---|---|
| `.ufo/waves/round-47/before/SUMMARY.md` | resolves |
| `verifiers/check_substrate_pins.py` | resolves |
| `verifiers/verify_surfaces.py` | resolves |
| `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json` | resolves (seat landed it 12:58) |
| `.ufo/waves/round-47/build/C1PinsRepin.md` | **absent → must exist at landing** |
| `verifiers/verify_skill_checklist.py` | resolves |
| `verifiers/floors-registry.json` | resolves |
| `.ufo/waves/round-47/build/C2CheckImpl.md` | **absent → must exist at landing** |
| `.ufo/waves/round-47/build/C2SkillRewrite.md` | resolves |
| `verifiers/citation-errata.json` | **absent → must exist at landing (use the landed name)** |
| `corpus/README.md` | resolves |
| `corpus/lessons/round-46-verifier-spotcheck.md` | resolves |
| `verifiers/verify_corpus_integrity.py` | resolves |
| `verifiers/verify_corpus_independent.py` | resolves |
| `verifiers/verify_harness_claims.py` | resolves |
| `.ufo/waves/round-47/build/` | resolves (directory) |

The list is **dynamic**: it was 6 tokens at my first measurement (12:54, before
`C1SurfacesBaselineDiff.json` was written) and is 5 now (13:02). The integrator must re-run the
check after pasting, not trust a list copied from this report. Machine-readable copy:
`.ufo/waves/round-47/build/RevLogAppend.token-inventory.json`.

**`verifiers/citation-errata.json` is a guess.** `build-spec.json` item `C3ErrataImpl` says “e.g.
verifiers/citation-errata.json” — the executor owns the name. If the landed registry is called
something else, the entry must cite the landed name or the citation is dead.

## MED-1 — measured proof that the append adds no new dead citation, and exactly which tokens it adds

The check was run against the **shipped** extraction/resolution functions (not a re-implementation),
on a symlink mirror of the lane repo so the real `LOG.md` was never modified:

```
BEFORE  status=FAIL evaluated=805
        LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve …;
        9 quoted meta-finding(s), 3 schematic token(s) excluded
AFTER   status=FAIL evaluated=824
        LOG.md:2111: '.ufo/round-45/drafts/v10/post-r44-hunt.py' does not resolve …;
        9 quoted meta-finding(s), 3 schematic token(s) excluded
```

The BEFORE line reproduces the live repo's own verdict exactly
(`python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json` →
exit 1, 9 PASS / 1 FAIL / 0 NA, `governance.citation_resolves` detail identical), so the mirror is
faithful. AFTER appending the proposed entry **with the not-yet-existing artifacts present as empty
placeholders**, the dead set is byte-identical to BEFORE: the append introduces **zero** new dead
citations and does not perturb any existing line's verdict (quote state is per-line —
`advance_quote_state` at `:1322-1336` — so an append cannot change another line's evaluation).
With the placeholders removed, the same run reports exactly the 5 (then 6) absent tokens as the new
dead set and nothing else.

## MED-2 — durability: `.ufo/waves/` is **untracked** in kotoba, so a working-tree-resolving citation is dead in any clone

`git ls-files .ufo/waves | wc -l` → **0**; `git status --porcelain` → `?? .ufo/waves/`; the tree is
not gitignored (`git check-ignore .ufo/waves/round-47/build/RevLogAppend.md` → exit 1). Sibling
lanes do track it (`git -C kama-shokunin ls-files .ufo/waves | wc -l` → 5824), and kotoba's own
history uses the older tracked layout (8170 files under `.ufo/round-46/`).

The gate resolves against the **working tree**, not the index, so an untracked artifact passes the
local gate and still fails in a fresh clone (which is how round 46 measured its battery — a
“canonical-layout shared clone”). **The landing commit must add the round-47 wave artifacts that
the entry cites.** If the integrator does not want to commit the wave tree, the entry must cite
only paths that are already tracked in the repo (e.g. `corpus/lessons/round-46-verifier-spotcheck.md`,
`verifiers/…`), or the citation is a local-only green.

## MED-3 — calibration: the entry must not hardcode the governance token count, and must name the substrate resolution

- The governance count is a function of the entry itself: measured **805 → 824** for this entry.
  A number written into the entry is stale the moment the entry is pasted (or a word is reworded).
  The entry should state the *check id* and the *pass/fail*, not the token count.
- `python3 -B verifiers/verify_surfaces.py --json` currently exits **2** with
  `{"error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode"}` — the default
  resolution is a path that no longer exists (`verifiers/verify_surfaces.py:128-131`,
  `verifiers/check_substrate_pins.py:61-64`). The recorded before-value with the 1.19.3 ELF passed
  explicitly is exit **1**, 4 PASS / 3 FAIL
  (`.ufo/waves/round-47/before/verify_surfaces.override-oc.json`, `exits.txt`:
  `surfaces-override exit=1`). Therefore an after-value of “exit 0 / 7-of-7” is only re-derivable
  if the entry says **which resolution** produced it (re-pinned default vs an explicit
  `--opencode-binary` path). Print the resolution next to the count.
- `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` prints **1** and exits **0**; the
  count is on stdout and the exit code carries no information. The entry must say “printed 1”,
  never “exit 1”.

## LOW-1 — path-token shapes the entry must avoid (each one hides a dead citation from the gate)

1. **A literal `round-N` path segment** (`corpus/lessons/round-N.md`) — auto-excluded as
   “schematic” (`verify_skill_checklist.py:349`, `:1422-1426`). A dead path written that way is
   invisible to the gate: a green that means nothing.
2. **Ellipsis** (`…`, `...`) inside a token — same exclusion. Use it only for genuinely
   non-literal prose, never for an artifact path.
3. **A token carrying `?`, `*`, `$`, `<`, `>`** — skipped entirely (`:1402-1403`). `<skills>` and
   `grep -c '<skills>'` are safe for exactly this reason; a real artifact path is not.
4. **A same-line double-quoted token** — excluded as a “historical/meta finding” (`:1400-1421`).
   Round 46 P4 had to reword its own correction note twice because it repeated a brace-form
   citation as a live link (`LOG.md:2273-2284`). Do not rely on the quoted exclusion to smuggle a
   dead path into the entry.
5. **`../`-prefixed tokens** — resolved against the repo's ancestors (up to 3 hops,
   `:1295-1315`), i.e. the **fleet root**, not the lane repo. `LOG.md` + `SCORECARD.md` already
   carry **23** such tokens (`../PROTOCOL.md`, `../AXES.md`, `../.ufo/l0-questions.md`,
   `../kasegi-shokunin/corpus/instruments/…`, …). They resolve on this host and are dead in a lane
   clone. Do not add new ones; the round-47 entry contains none.
6. **Absolute host paths** (`/home/vgpnk/.npm/_npx/…/opencode`, `/fast/scratch/kotoba-r47/shared/…`)
   — not citation roots, therefore **never checked** by the gate. Fine as prose; not acceptable as
   the *only* evidence pointer, and they are host-coupled.
7. **Pruned draft paths** under `.ufo/round-45/drafts/` — the pre-existing dead token
   `.ufo/round-45/drafts/v10/post-r44-hunt.py` (`LOG.md:2111`) is exactly such a path: the line
   records that the runner is absent. Never cite it, or any sibling path, in the new entry.
8. **A path in the old layout** — the round-47 artifacts live under `.ufo/waves/round-47/`, not
   `.ufo/round-47/`; the latter does not exist and would be a dead citation.
9. **`corpus/lessons/round-47.md`** — does not exist at BASE (the newest lesson is
   `corpus/lessons/round-46.md`, plus `corpus/lessons/round-46-verifier-spotcheck.md`). Cite it
   only if the round actually lands that lesson file.

## LOW-2 — the entry's structure must match the recent-round convention

Every recent entry uses `## <date> — Round <N> <label>` followed by `- ` bullets, one per claim,
each carrying the command, its exit code, and the evidence pointer
(`LOG.md:2052-2315`; the round-46 landing entry is `LOG.md:2300-2311`, the landing pin
`LOG.md:2312-2315`). The draft follows it: one header, one bullet for the steer/base, one bullet
per claim C1/C2/C3, one “not claimed” bullet, one durability bullet. `AGENTS.md:4` requires the
same (“Every change appends a LOG.md entry with the evidence that motivated it”).

## The exact proposed entry

Full text with the `[fill: …]` markers: `.ufo/waves/round-47/build/RevLogAppend.proposed-entry.md`.
Markers sit outside backticks, so they are never citation tokens.

```
## 2026-10-21 — Round 47 landing (MoriR22R steered round 47): C1 freshness re-pin; C2 operability description-tag rule; C3 calibration erratum registry + corpus index

- Steer and base: the round plan is `plans/round-47.md`; BASE commit `c61a973b2e02e1ded169703ddcb06466f4edd8bd`; the before-measurement summary and its raw outputs are `.ufo/waves/round-47/before/SUMMARY.md` and the sibling files beside it.
- C1 (freshness, lowest non-retired axis): the omp 18.12.5 and opencode 1.19.3 instruction surfaces were re-derived from the frozen dumps and the substrate pins re-cut; before `python3 -B verifiers/check_substrate_pins.py` exited 2 (DRIFT 3/3 — omp sha256 drift, omp mtime drift, opencode binary unreadable) and `python3 -B verifiers/verify_surfaces.py --json` exited 2 (opencode binary not found); after, the same two commands exit 0 at 3/3 pins and 7/7 surface classes. Evidence: `.ufo/waves/round-47/build/C1SurfacesBaselineDiff.json`, `.ufo/waves/round-47/build/C1PinsRepin.md`.
- C2 (operability): `verifiers/verify_skill_checklist.py` gained the `frontmatter.description_no_xml_tag` check and this lane's own description lost its `<skills>` token; before, the frontmatter carried one `<skills>` occurrence and no check existed; after, zero occurrences and the live check passes. The self-test count moved with the new arms and the floor in `verifiers/floors-registry.json` was bumped in the same change [fill: assertion count before -> after]. Evidence: `.ufo/waves/round-47/build/C2CheckImpl.md`, `.ufo/waves/round-47/build/C2SkillRewrite.md`.
- C3 (calibration): `verifiers/citation-errata.json` pins the recorded absence at `LOG.md:2111` by file, line, token and line sha256, and `corpus/README.md` indexes `corpus/lessons/round-46-verifier-spotcheck.md`; before `python3 -B verifiers/verify_skill_checklist.py --json` exited 1 at 9 PASS / 1 FAIL (`governance.citation_resolves`), `python3 -B verifiers/verify_corpus_integrity.py --json` exited 1 (tracked_files 59 != 58, unindexed 1) and `python3 -B verifiers/verify_corpus_independent.py --json` exited 1 (unindexed 1); after, all three exit 0 [fill: checklist 10/10 or 11/11; corpus integrity 0 DRIFT; corpus independent 0 DRIFT]. Evidence: `.ufo/waves/round-47/build/C3ErrataImpl.md`, `.ufo/waves/round-47/build/C3CorpusIndex.md`.
- Not claimed: `verifiers/verify_harness_claims.py` 21/28 at BASE (three host skills without cache rows) stays Q09 debt; the round-46 spot-check residuals (mirror opt-out, missing verdict, NaN/case-variant keys, row `kind`, payload-selectable committed scope-outs, the printed C1 counting command's exit 2) are carried with why-not lines in the wave reports under `.ufo/waves/round-47/build/`.
- Every path token this entry cites resolves at the landing tree, and the entry is appended at the tail of `LOG.md`, so no line above `LOG.md:2111` moves and the erratum entry keyed on that line stays valid.
```

### Counting commands per claim — measured at BASE (exit codes)

| claim | command | exit | observed |
|---|---|---|---|
| C1 | `python3 -B verifiers/check_substrate_pins.py` | 2 | `DRIFT 3/3 pins failed: omp_binary_sha256, omp_binary_mtime, opencode_binary_sha256` (omp sha256 `fdbc8136…` vs pinned `9513ef9f…`; mtime delta 140082506863270 ns; opencode binary unreadable) |
| C1 | `python3 -B verifiers/verify_surfaces.py --json` | 2 | `{"error": "opencode binary not found: /home/vgpnk/.opencode/bin/opencode", "checks": []}` |
| C1 | same, with the 1.19.3 ELF passed explicitly | 1 | 4 PASS / 3 FAIL — `surfaces.literal_present`, `surfaces.no_uncovered_class` (0/8 loader classes vs baseline 8), `surfaces.opencode_extract` (OC-1/OC-4/OC-6) |
| C2 | `grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)` | 0 | prints `1` |
| C2 | `python3 -B verifiers/verify_skill_checklist.py --self-test` | 0 | `0 failure(s) over 1597 assertions` (floor `verifiers/floors-registry.json` → `checklist: 1597`; C2's new arms move it, and the registry + both in-file tables + the guard docstring must move in the same change) |
| C3 | `python3 -B verifiers/verify_skill_checklist.py --json` | 1 | 9 PASS / 1 FAIL / 0 NA; only `governance.citation_resolves` FAILs, on `LOG.md:2111` |
| C3 | `python3 -B verifiers/verify_corpus_integrity.py --json` | 1 | `tracked_files 59` vs baseline `58`; `unindexed 1` = `corpus/lessons/round-46-verifier-spotcheck.md` |
| C3 | `python3 -B verifiers/verify_corpus_independent.py --json` | 1 | `unindexed 1`, same file |

### Commands run (all read-only, in the lane repo, no mutation)

```
python3 -B verifiers/verify_skill_checklist.py --repo "$PWD" --skill "$PWD/SKILL.md" --json   → exit 1
python3 -B verifiers/verify_skill_checklist.py --self-test                                    → exit 0 (1597 assertions)
python3 -B verifiers/check_substrate_pins.py                                                   → exit 2
python3 -B verifiers/verify_surfaces.py --json                                                → exit 2
python3 -B verifiers/verify_corpus_integrity.py --json                                         → exit 1
python3 -B verifiers/verify_corpus_independent.py --json                                       → exit 1
grep -c '<skills>' <(sed -n '/^---$/,/^---$/p' SKILL.md)                                       → exit 0, prints 1
python3 scratch_r47/check_tokens.py --repo <repo> --entry entry_only.md                       → exit 1 (5 new dead tokens, as expected pre-landing)
python3 scratch_r47/mirror_build.py && <gate on mirror>                                       → BEFORE 805/1 dead, AFTER 824/1 dead
git ls-files .ufo/waves | wc -l                                                               → 0
git status --porcelain                                                                         → "?? .ufo/waves/", "?? plans/round-47.md" (unchanged by this seat)
```

`git status --porcelain LOG.md` is empty and `wc -l LOG.md` is still 2315: this seat did not touch
`LOG.md`. (The mirror build first tried `cp -al` into `/tmp`, which failed — cross-device hardlink —
and then `cp` onto a symlinked `LOG.md`; `cp` refused with “are the same file” and the repo's
`LOG.md` was verified byte-unchanged afterwards.)

## What I did NOT check

- I did **not** run the wave-1 falsification battery or the C1/C2/C3 implementations; the after-values
  in the draft are markers, and every number I state for “after” is a target, not a measurement.
- I did **not** verify the erratum registry's own design (key format, stale-erratum semantics) — that
  is `C3ErrataImpl`'s lane; I only derived the constraint it places on the LOG append (HIGH-1) and
  the line hashes it must bind.
- I did **not** check whether `verifiers/citation-errata.json` is the name the C3 seat will land, nor
  whether `C1PinsRepin.md`, `C2CheckImpl.md`, `C3ErrataImpl.md`, `C3CorpusIndex.md` will be written
  under those exact names; the must-exist list must be recomputed at landing.
- I did **not** run the `SCORECARD.md` update for round 47 (out of this lane's scope) and did not
  check the `SCORECARD.md` planned block (`SCORECARD.md:101-102`) for token validity — note that
  `SCORECARD.md` is governed by the **same** gate, so any round-47 SCORECARD edit carries the same
  token rules and the same `../` caveat (13 `../` tokens live in `SCORECARD.md`).
- I did **not** evaluate `verify_harness_claims.py` (21/28, not claimed this round) and did not
  audit the r46 spot-check residuals; they are named in the entry's “not claimed” bullet only.
- I did **not** verify the round-47 lesson file (`corpus/lessons/round-47.md` does not exist at BASE)
  nor whether one will be written; the entry does not cite it.
- I did **not** execute `~/.local/bin/opencode` or the npx wrapper (forbidden); the opencode
  before-values are read from the frozen snapshot record
  (`.ufo/waves/round-47/before/verify_surfaces.override-oc.json`, `exits.txt`), not re-run.
- I did **not** check the C1 seat's re-pin of `verifiers/baseline.json` (omp mtime pin semantics) —
  only that the entry's counting command and its resolution are named together (MED-3).
