# CritC3Province — C3 (coverage) attack, round 69 wave 1

Lane `kotoba-shokunin`. Claim C3: the r67 and r68 areas enter `PROVINCE.md` § Core.
Base `a5f7459f99bb27bf697e9438362e75ac5833eca8`; measured lane tip `a238989a96cb0d2b939679126b832d75b861ca6e`.
All runs in `/tmp` `git clone --shared` sandboxes (`/tmp/c3prov`, `/tmp/c3merged`); the lane repo was
read only (`log`/`show`/`status`/`diff`). No tool installs were needed.

## Verdict

- **C3 content: PASS as drafted.** With the working-tree `PROVINCE.md` as the measured revision the
  frozen predicate prints `province core rows 2 of 2` and exits 0. I verified this twice: committed
  alone on the lane tip, and committed alone on the pinned base.
- **C3 at the current branch tip: `0 of 2`, exit 1** — because `PROVINCE.md` is uncommitted
  (`git status --porcelain` → ` M PROVINCE.md`; the tip has 0 occurrences of the r67 bullet). This is a
  commit-order fact, not a counter defect. C3 must not be scored pass or fail until the L1 commits the
  draft; then re-run at that rev.
- **No harm holds:** § Frontier and § Adjacent are byte-identical to the base; the whole file delta is
  the two inserted Core lines.
- **No duplicate authority:** neither area is claimed by § Frontier (current or base) or by
  `corpus/README.md` § Frontier, so the Core rows create no second authority and the byte-identity
  conjunct is not in tension with the move.
- Five findings below: F1 (medium, instrument soundness), F2 (low, formatting), F3 (medium, coverage
  legibility), F4 (low, false provenance in the docstring), F5 (low, disclosed design bound).
  None falsifies C3; F1/F3/F4 are corrections the same commit can carry.

## 1. Counter runs (verbatim)

| # | command (in `/tmp/c3prov` unless noted) | output | exit |
|---|---|---|---|
| 1 | `check_province_core.py --rev a238989a96cb0d2b939679126b832d75b861ca6e` | `measured-rev: a238989…` / `province core rows 0 of 2` + one finding per area (no § Core bullet names the entry, counter and round) | **1** |
| 2 | `--rev` on a commit carrying only the draft `PROVINCE.md` on top of `a238989` | `measured-rev: 392736263cd91b2c9acab852dc267bd5073d66e5` / `province core rows 2 of 2` | **0** |
| 3 | `--rev` on the pinned base `a5f7459f…` | `province core rows 0 of 2` | **1** (base control) |
| 4 | base `a5f7459f…` + draft `PROVINCE.md` + the counter, committed | `measured-rev: 3c62a9a09add5d2b11e75958dc88d266aa8b037f` / `province core rows 2 of 2` | **0** |
| 5 | cheap control, reproduced independently: the two bullets replaced by one path-only bullet naming both entries | `province core rows 0 of 2` | **1** |
| 6 | no `--rev` | `environment error: --rev <revision> is required` | **2** |

Run 4 proves **causal separability**: the r67/r68 entries, their counters and their coverage-map rows
all already exist at `a5f7459f`, and nothing from C1 or C2 is needed. The plan's separability
sentence is correct at the bytes.

Run 5 matches the plan's declared cheap control (`0 of 2`, exit 1). Note the declared receipt files
`.ufo/waves/round-69/w1/controls/C3-base.txt` and `C3-cheap-control.txt` **do not exist yet** — the
`controls/` directory is absent (`ls: cannot access … No such file or directory`). Runs 3 and 5 are my
own reproduction, not a re-read of the plan's receipts.

## 2. Self-test

`python3 -B verifiers/check_province_core.py --self-test` → all ten arms pass, exit 0:

```
PASS honest world: 2 of 2
PASS broken world rejected: base province
PASS broken world rejected: row in Frontier, not Core
PASS broken world rejected: row lacks the counter
PASS broken world rejected: row lacks the round
PASS broken world rejected: entry absent
PASS broken world rejected: counter absent
PASS broken world rejected: entry not indexed
PASS broken world rejected: Frontier rewritten
PASS broken world rejected: Adjacent rewritten
self-test: 0 failure(s) over 10 assertions
```

## 3. `## Frontier` / `## Adjacent` diff against the base

`git show a5f7459f…:PROVINCE.md > /tmp/base-pv.md`, then heading-delimited section comparison with the
counter's own boundary regex (`^## <name>` … next `^## `):

| section | base | current | identical | sha256 (first 16) |
|---|---|---|---|---|
| preamble (before `## Core`) | 323 ch | 323 ch | **yes** | — |
| Core | 8903 ch | 9339 ch | no (+436 ch / +440 B) | `a490c2534caf87d7` |
| Frontier | 2125 ch | 2125 ch | **yes** | `fa763651cc9166bc` |
| Adjacent | 8321 ch | 8321 ch | **yes** | `d4e9b92d43bbb3cd` |

Independent byte check: bytes from `## Frontier` to EOF are identical in both files (10466 B each),
headings sit at the same relative offsets, and the only hunk in `diff -u` is
`@@ -25,6 +25,8 @@` with two `+` lines and **no** deletions. Section diff: **none**. The byte delta is
+440 bytes (436 characters — the file is UTF-8 with `—`/`§`).

## 4. Bullet audit — entry, counter, round

Both bullets, verbatim from the draft:

```
- Instruction-authority ladder (round 67): what a skill body may assert and at whose authority level — `corpus/knowledge/instruction-authority-ladder-round67.md`, counted by `verifiers/check_instruction_authority.py --rev <rev>`.
- Client trust gates (round 68): what five clients document about an untrusted skill body — `corpus/knowledge/client-trust-gates-round68.md`, counted by `verifiers/check_client_trust_gates.py --rev <rev>`.
```

Each names its entry path, its counter path and its round, inside `## Core` (Core bullet count
14 → 16). Both entries and both counters exist at the tip, and both coverage-map rows
(`corpus/README.md:125`, `:128`) exist at the base — otherwise run 4 could not pass.

**Do they belong in Core?** Yes, on the lane's own definition:

- § Core preamble: *"Appended round 46 (LEARNING.md § Province is a frontier); surfaces the lane
  governs now"* — Core holds surfaces plus their instruments.
- Both areas are *held*, not exploratory: their own counters pass at the measured tip —
  `check_instruction_authority.py --rev a238989…` → `authority ladder grounded 1 of 1`, exit 0;
  `check_client_trust_gates.py --rev a238989…` → `client trust gates backed 5 of 5`, exit 0.
- Neither row is a decaying measurement: r67 is a documented authority ordering, r68 a per-client
  documentary map — the same class as the r48 authority map and the r52–r60 per-client maps already
  in Core. The round-47 rule recorded in `.ufo/waves/round-47/build/ConnProvinceFrontier.md:143`
  ("Core lists surfaces and instruments, not measurements that decay") admits both.
- The r68 closure recorded the move as deferred, not refused: "`PROVINCE.md` § Core is untouched this
  round (carried to 69, as disclosed)" and "§ Core is not yet moved"
  (`corpus/lessons/round-68-verifier-spotcheck.md:101,135`).

## 5. Completeness — is "the r67 and r68 areas" the whole set?

`git log --diff-filter=A --name-only` over the r67/r68 commits shows exactly one knowledge entry and
one counter per round: `da86c03` adds `corpus/knowledge/instruction-authority-ladder-round67.md` +
`verifiers/check_instruction_authority.py`; `605b84b` adds
`corpus/knowledge/client-trust-gates-round68.md` + `verifiers/check_client_trust_gates.py`. The other
r67/r68 artefacts are closure spot-check lessons written by the hyaku closure ("outside review; never
edited here", `corpus/README.md:124,127,131`) — records, not Core ground. No admitted r67/r68 area is
omitted by the two rows.

## 6. Findings

### F1 — the counter counts areas, not rows; one merged bullet passes (medium)
Counterexample, run in `/tmp/c3merged` at `1c0b0d6978b1d0d834d53a75cc142fd7cc49f199`: the two honest
bullets replaced by **one** bullet (plus one continuation line) naming both entries, both counters and
both rounds →

```
province core rows 2 of 2
exit=0
```

with 15 Core bullets instead of 16. `check()` loops the areas independently and never consumes a
matched bullet; `bullets()` also folds any indented continuation line into the previous bullet, so an
area can be satisfied from inside another row's continuation. The label "rows 2 of 2" therefore
overstates granularity. Impact on the shipped draft: none (16 bullets, one per area). Fixable defect,
not a tradeoff: have each area take a distinct bullet (track consumed indices) and add a must-fail arm
"one bullet for two areas"; rename the printed noun to `areas` if row granularity is not intended.

### F2 — the Core list runs into `## Frontier` with no blank line (low)
The diff hunk is `"…--rev <rev>`.\n+bullet 67\n+bullet 68\n ## Frontier"`: the existing separator blank
line moved above the bullets and the heading now follows the list immediately. Every other `##`
heading in the file is preceded by a blank line. Verified safe: adding the blank line back keeps
`province core rows 2 of 2`, exit 0 (sandbox commit `76572cde560d82fc72c168f0db4cbe31aaec871c`), and
`section("Frontier")` begins at the heading, so no-harm is unaffected. Smallest safe correction: add
the blank line.

### F3 — the bullets name no clients or authorities, unlike every comparable Core row (medium)
The r68 bullet says "five clients" and names none; those five (VT Code, Parallel Works, Kilo Code,
Microsoft Agent Framework, Mistral AI Vibe) are explicitly **not** the lane's pinned seven
(`corpus/knowledge/client-trust-gates-round68.md:56`; `corpus/lessons/round-68-verifier-spotcheck.md:101`
flags the gap). Read from `PROVINCE.md` alone, the row looks like ground over the pinned client set.
The r67 bullet names no source at all, while the r48 Core row names all five authorities. Core
convention is to name them: r52 names six clients, r53 nine, r56 seven, r58 seven, r59 six, r60 four
plus three. Smallest safe correction: add the five client names (and state "none of the pinned
seven") and the three r67 sources. No counter or Frontier byte impact.

### F4 — counter docstring misstates the "before" state (low)
`verifiers/check_province_core.py:13-15` says the areas were "left on the frontier side of
`PROVINCE.md`". They were on neither side: base § Frontier is 7 lines and names only executed-checklist
coverage and loader-rule freshness, and `corpus/README.md` § Frontier carries no r67/r68 row. The
accurate state is "admitted into `corpus/knowledge/` and indexed in the coverage map, but unnamed in
the province". This also means the precedent label "moved from Frontier" (used in the r47/r49/r52/r53
rows) would be false here — the draft's plain "(round 67)"/"(round 68)" is the correct wording; do not
change it. Smallest safe correction: reword the docstring only.

### F5 — the byte-identity conjunct is permanently base-locked (low; disclose, do not change)
Because § Frontier and § Adjacent must stay byte-identical to `a5f7459f` at every measured rev, any
future round that legitimately edits either section cannot also run C3. That is the declared no-harm
tradeoff, and it is the right one for this round; record it as the instrument's bound rather than
loosening it now.

## 7. Impacted axes

- `coverage` (C3's own axis): claim holds on content; predicate observable only post-commit.
- `consistency`: F2 (heading separator), F3 (Core naming convention), F4 (docstring provenance).
- `depth`, `calibration`: untouched by C3 (documentary naming move, no new source work).

## 8. Smallest safe corrections (ordered, all in one commit)

1. Commit the draft `PROVINCE.md` (only then is `2 of 2` measurable); re-run the counter at that rev.
2. F2: blank line before `## Frontier`.
3. F3: name the five r68 clients (+ "none of the pinned seven") and the three r67 sources.
4. F4: reword the counter docstring's "frontier side" clause.
5. F1 (optional, instrument): distinct-bullet consumption + a "one bullet for two areas" must-fail arm,
   or record the area-vs-row bound in the plan's counter semantics.
