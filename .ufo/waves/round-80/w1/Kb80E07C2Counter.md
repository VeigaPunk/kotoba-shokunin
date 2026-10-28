# Kb80E07C2Counter — C2 counter (port + redesign), round 80 w1

Seat: leaf, no subagents. Deliverable: `.ufo/waves/round-80/build/check_allowed_tools.py` (lands at
`verifiers/check_allowed_tools.py`; the L1 integrates — I did not touch `verifiers/`, `corpus/`, `SKILL.md`,
`PROVINCE.md`, the lane index or any lane file outside `.ufo/waves/round-80/`).

## 1. What was built

The round-80 C2 counter, ported from the reviewed r79 draft
(`.ufo/waves/round-79/build/check_allowed_tools.py`, sha256 `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`)
and redesigned on the six deltas my item names, plus three counter-side defects that the wave measured
under the draft and that made the plain frozen target unreachable on the committed bytes.

Frozen printed predicate (exactly three claim lines, in this order, then the diagnostics):

```
allowed-tools surfaces documented N of 6
generator world: M of 6
semantic rider: exploratory — reviewers of record: round-80 non-author closure spot-check
```

Exit 0 iff `N == 6` **and** the tree conjuncts hold: (g) `SKILL.md` carries one rule line naming ≥3 surfaces
and citing the entry, plus a conformant 8-cell `gate` registry row for `verifiers/check_allowed_tools.py`;
(h) `PROVINCE.md` `## Core` has exactly one bullet naming the entry. The generator world's `M` is printed
beside the headline and **never gates** (delta 4). Exit 1 = content verdict; exit 2 = could not evaluate.

Deltas implemented: (1) headline `documented`, not `backed`; (2) `TARGET = 6`, exit iff `N == 6`; (3) the
semantic-rider line always printed; (4) the exit predicate no longer conditions on the generator world
`< target` — `M` is printed; (5) entry path `corpus/knowledge/allowed-tools-surfaces-round80.md`, counter
names itself `check_allowed_tools.py`; (6) self-test worlds re-baselined to `N == 6` (every 5-of-6 arm now
exits 1) plus a world asserting the exit predicate is `N == 6` and worlds asserting the `generator world:`
and rider lines are present. The six per-surface conjuncts (a)–(f) and the frozen surface table / grant
labels stay exactly as the r79 plan § C2 (no new conjunct, none dropped).

## 2. The three counter-side fixes (each with a red-before self-test arm)

**F1 — Q70 heading detection is per snapshot shape.** The r79 reading took "the page's first heading" as
the first text-view line starting with `#`. On an HTML snapshot the view has no `#` headings at all (tags
are stripped), so that scan lands on a code comment. Measured on the committed
`.ufo/waves/round-79/snapshots/S229-msaf.html`: the field is named once (text-view line 95) and the first
`#`-line is `# Auto-approve load_skill and read_skill_resource, not run_skill_script.` (a Python comment,
line 168), while the real `<h1 id="agent-skills">Agent Skills</h1>` is at raw line 676. The r79 rule
therefore rejected every admissible msaf quote (`idx <= first_head + 1`) and the six-surface target was
unreachable. Fix: `view_with_headings()` reads headings per shape — Markdown: `#` lines outside fenced
blocks; HTML: the view line carrying a `<h1>`..`<h6>` element of the raw bytes, marked before the same
pipeline runs so line indices stay aligned and no quote ever sees the marker. The rule itself
("not on a heading, not in the first-heading block, not a shared banner") is unchanged; **no source quote
was narrowed** — the entry owner's msaf quote is used as written.

**F2 — the anchor fetch-record grammar.** The committed `corpus/SOURCES.md` rows write
``fetched 2026-10-27, HTTP 200, 7608 B, sha256 `9a67…` `` — a date with no time and a **backticked**
digest. The r79 regex demanded `fetched <ISO8601>T..Z, … sha256 <hex>` and rejected all six committed rows
so `(c)` could not pass on the real corpus. `FETCHED_RE` now accepts a date or a date-time with `Z` and an
optional backtick pair; `HTTP 200`, the byte count and the 64-hex digest stay required, and the digest must
equal the manifest pin and the committed snapshot's own sha256. Red-before arm: the committed form is
accepted (6 of 6) while a wrong status is not.

**F3 — the pin source.** `MANIFEST.sha256` is absent from the lane tree (checked at base 398cbe1 and in
git history); the round-79 wave committed six per-page `<id>.manifest` files in the same directory, each
`<sha256>  <basename>`. `Repo.manifest()` now reads the aggregate when committed and the per-page files
otherwise, and requires them to agree basename by basename when both exist (disagreement = exit 2). The
pin load is unchanged: the committed snapshot bytes must hash to the pin and the row's anchor record must
carry the same digest. `snapshot_name()` also binds a cited id by the pin's own id prefix
(`S226` → `S226-spec.md`), which is deterministic and immune to entry prose that names several snapshots on
one line (the r79 version raised exit 2 there); a genuine ambiguity (two pins with one prefix) still exits 2.

## 3. The generator world (Q71/Q74 disclosure)

The generator is a **form builder**: from the measured revision's own committed bytes (registry rows +
pinned snapshots) plus the plan's frozen surface table it writes the complete proposed evidence shape — the
source lines, the five-cell rows, the tokens, the mechanically located quote, the frozen grant cell — then
scores that world with the same `check()`. It performs no judgement about what a page means; the frozen
grant label is a form cell (public in the plan), and whether a label is **true** of its page is not decided
by the counter at all. `M` is measured, printed and never gated. Measured: `M = 6` at the tip **and at
base** — i.e. the form backbone is mechanically reachable from base bytes; what the base lacks is the
entry. That is the plan's declared split (form backbone measured, grant-semantics rider exploratory with
named non-author reviewers), and the third printed line states it. A reviewer should read the headline as
a form-level number only; that is what it says.

## 4. Verification (each command's own exit status; receipts in `build/`)

- `python3 -B check_allowed_tools.py --self-test` → `self-test: 0 failure(s) over 255 assertions in 89
  world(s)`, **exit 0** (`Kb80E07C2Counter-selftest.txt`). 89 worlds: the honest world (6 of 6, exit 0,
  both `--repo` forms, tree conjuncts green), one broken world per conjunct (a)…(h), the plan's shortcut
  controls (C1 token dump without snapshots → exit 2, C5 label-only, closed-shell rows), the
  cannot-evaluate arms (unknown rev, no registry, tampered pin, no pin source, aggregate/per-page
  disagreement, counter drift), and the red-before arms for F1–F3.
- base `398cbe1bb67f8d9dcf5d25d5ecf1b26a7c6f7e93`: `allowed-tools surfaces documented 0 of 6`,
  `generator world: 6 of 6`, rider line printed, **exit 1** (`Kb80E07C2Counter-base.txt`) — the plan's
  frozen base figure.
- scratch **operability** world (base + `Kb80S05SourcesEdits.patch` + `Kb80S09SkillRule.patch` +
  `Kb80S10Province.patch` + the published entry + `.ufo/waves/round-79/snapshots/MANIFEST.sha256` built
  from the six per-page pins): `documented 6 of 6`, `generator world: 6 of 6`, **exit 0**, in the
  absolute `--repo <clone>` form **and** the `--repo .` form run from the clone root, and again with the
  aggregate manifest removed (per-page pins only) (`Kb80E07C2Counter-tip-scratch.txt`). This is a
  counter-operability measurement in scratch, **not** the claim's after-value — scoring the lane tip is
  the L1's.
- freeze receipt: full sha256 `a12921bee0433e88b04dd0ff5779cb0cd2bbdd3671d5faa574bfd5928e19f08e`,
  118313 B, 2563 lines; blanked `SELF_SHA` `434fd6f9646bbc56948eb5c4603c7a1f2d815fc11b3741cb25ef052720111742`
  (agrees with `--print-self-sha`, so the drift guard passes) (`Kb80E07C2Counter-freeze-shas.txt`).

## 5. Dependencies and risks (not my write scope)

- `corpus/SOURCES.md`: the six rows' `used-by` must name `corpus/knowledge/allowed-tools-surfaces-round80.md`
  (S05's patch does) or conjunct (b) fails for all six.
- `SKILL.md`: the rule line citing the entry + the 8-cell `gate` row for `verifiers/check_allowed_tools.py`
  (S09's patch does). `PROVINCE.md`: the one `## Core` bullet (S10's patch does).
- **Pin trap:** the S229 row's anchor must keep the **pinned** digest `34016233…`, not the live re-open
  digest; the counter compares the anchor's digest to the pin *and* re-hashes the committed snapshot.
- The aggregate `MANIFEST.sha256` is optional (F3). If it is landed, it must agree with the six committed
  per-page pins; the sentinel's `Kb80N01Sentinel-MANIFEST.proposed` does.
- Inherited row defect (reported, not repaired, per the plan's frontier rule): `corpus/SOURCES.md` S230's
  anchor cites `7bb48f21…`, which is the Mistral-Vibe head, not pi-mono's (`S230.fetch.json` records
  `bb65e3e4…`). It belongs in the round-80 lesson as an erratum line.
- Calibration note for the L1/reviewers: `M = 6` also at base means the measured number is a form number;
  the claim's content lives in the entry's quotes/labels and in the rider, not in beating a generator.

Tooling: nothing installed or upgraded (no pacman; no PATH changes). Scratch clone and temp dirs under
`/fast/scratch/hyaku/kotoba-r80/Kb80E07C2Counter/` were removed after the receipts were copied; nothing was
written at the fleet root, in `verifiers/`, or in any lane file outside `.ufo/waves/round-80/`.

VERDICT: C2 counter ported and redesigned to the frozen round-80 predicate (documented/generator-world/rider, exit iff N == 6 + tree conjuncts), with the HTML-heading, fetch-record and pin-source defects fixed; self-test 0 failures/255 assertions/89 worlds exit 0; base=0 of 6 exit 1; scratch operability tip=6 of 6 exit 0 both repo forms; frozen sha256 a12921be….
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/check_allowed_tools.py ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E07C2Counter-selftest.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E07C2Counter-base.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E07C2Counter-tip-scratch.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/build/Kb80E07C2Counter-freeze-shas.txt ; /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-80/w1/Kb80E07C2Counter.md
