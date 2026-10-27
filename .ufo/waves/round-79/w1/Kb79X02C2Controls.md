# Kb79X02C2Controls — C2 control worlds, pre-registered, then run

Seat: Kb79X02C2Controls (executor, leaf). Lane: `/home/vgpnk/Projects/shokunin/kotoba-shokunin`.
Lane base `b10bcbc6b00f8f56b202ccbadca311007b5b463c`; plan commit F1 `2c56622375641193a03bb97c0624e6536f3dffba`.
Written 2026-10-27. Plan text read first: `plans/round-79.md` § C2 (frozen predicate, surface table,
the ten named control worlds, Q71).

---

## 1. Deliverable and the exact invocation the L1 runs after freeze

`/home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/c2_controls.py`
(stdlib only; sha256 `242d970c2f96bbb94cc07d16ec72f16eafa961e963dbbb199473bcaf4c26288e`).

```
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/c2_controls.py \
  --counter /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_allowed_tools.py \
  --base-tree /home/vgpnk/Projects/shokunin/kotoba-shokunin \
  --work /fast/scratch/hyaku/kotoba-r79/<some-dir> \
  --verbose --out /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/c2-controls-run.log
```

* `--counter` is the frozen copy at the lane path (SELF_SHA filled by the L1 at freeze): no
  preparation is needed then. (In this wave I measured a scratch copy of X01's **draft** with
  its `^SELF_SHA = .*$` line filled with the file's own blanked sha; the draft is not frozen and
  changed three times while I worked — see §10.)
* Exit codes: `0` every world matched its pre-registration; `1` at least one world diverged;
  `2` environment (no counter file, base revision not a commit, world build failure,
  fixture self-check failure). The script reports; it never scores the claim.
* Useful flags: `--list` (the pre-registered table), `--only C3,C6`, `--keep`, `--json`.
* Each run also prints the counter's own `script-only world: M of 6`, `held at base`,
  `opened this round`, `province surfaces named`, `skill rule line`, `registry home` lines and
  every finding, so the L1 does not have to re-derive them.

World shape (documented in the module docstring so a reviewer can attack it): each world is
`D=$(mktemp -d -p "$WORK")` + `git -C "$D" init -q`, identity `scratch-r79` /
`scratch@example.invalid`, `git -C "$D" rev-parse --show-toplevel` asserted equal to `$D`.
One line in `$D/.git/objects/info/alternates` shares the base clone's object store **read-only**
(what `git clone --shared` writes), so the frozen `BASE_REV` the counters read resolves inside the
world without copying 190 MB per world; `read-tree <base-rev>` seeds the index with the real base
tree; fixture blobs are written with `hash-object -w --stdin` and `update-index --cacheinfo`; one
`commit-tree -p <base-rev>` produces the measured commit. No worktree is checked out, no world is
larger than its fixtures, and the lane is never written. The counter under test is placed in every
world at `verifiers/check_allowed_tools.py` (its own bytes), because conjunct (g) asks for a
registry row for that path and the lane will hold the counter at the same commit as the data.
C0 is the exception: it measures the base revision itself.

Every page in every world is a fixed synthetic text inside `c2_controls.py`. No network, no
fetched page, nothing that could be confused with the six real snapshots.

---

## 2. Pre-registered expectation table (fixed before the first run)

The table is `EXPECT` in the generator and is printed by `--list`; the receipt
`build/Kb79X02C2Controls.expected.txt` is that output. `N` is the counter's
`allowed-tools surfaces backed N of 6`; `(none)` means no verdict line may be printed.

| world | what it breaks | expected N | expected exit | defect signature |
|---|---|---|---|---|
| **H** | nothing — honest six-surface world (plumbing oracle, **not** a control) | 6 of 6 | 0 | any divergence = generator/counter plumbing mismatch |
| **C0** | nothing done: the base revision itself | 0 of 6 | 1 | N ≥ 1 or exit 0 |
| **C1** | token dump: every token, label and quote, no snapshot, no manifest | 0 of 6 or no line | 1 or 2 | N ≥ 1 or exit 0 |
| **C2** | wrong-page text: every row quotes another surface's page | 0 of 6 | 1 | N ≥ 1 or exit 0 |
| **C3** | shared banner: one banner line identical in all six snapshots, quoted by every row | 0 of 6 | 1 | N ≥ 1 (banner/subtitle accepted); ≥ 5 is the plan's threshold |
| **C4** | script-only scrape: pins, quotes, tokens, labels generated mechanically from fixed text | 6 of 6 | 0 | **not** a defect: Q71 form-level world; N ≤ 5 = counter rejects mechanical form (a finding) |
| **C5** | label-only: grant labels + page tokens, no quote anywhere | 0 of 6 or no line | 1 or 2 | N ≥ 1 or exit 0 |
| **C6** | sibling host: `…/badlogic/pi-mono-evil/…` and `…/mistralai/mistral-vibe-evil/…` | 4 of 6 | 1 | N ≥ 5 or exit 0 |
| **C7** | tampered snapshot: pi's committed bytes changed after the pin | (none) | 1 or 2 | exit 0, or a full count from bytes that do not hash to their pin |
| **C7a** | wrong sha pin: pi's and vibe's registry anchors carry `000…`, bytes intact | 4 of 6 | 1 | N ≥ 5 or exit 0 |
| **C8** | first answer: 6 of 6 asserted from the census, no snapshot, no row, no pin | 0 of 6 | 1 | N ≥ 1 or exit 0 |
| **C9** | duplicate row: two surface-table rows for `pi` | 5 of 6 | 0 or 1 | N = 6 (duplicate counted twice); N = 5 is the plan's arithmetic (below) |
| **C10** | quote without the token: claude and msaf quote page sentences lacking `allowed-tools` | 4 of 6 | 1 | N ≥ 5 or exit 0 |

Three readings are pre-registered with the table and are the ones a reviewer should attack:

1. **Single-surface controls cannot fall below the target.** C9, C10 and a one-row C6 could each
   only ever remove one surface; 5 of 6 still meets the frozen `N >= 5`, so the world would sit at
   the target and the plan's "any control reaching N ≥ 5 is a counter defect" rule could not bite.
   C6 and C10 therefore break **two** surfaces each (the plan-named probe plus one partner), and
   C9 is left at exactly one surface because the duplicate mechanism *is* single-surface — its
   verdict is read from the N value, not the exit code (see §6.3).
2. **C7 is split.** The plan names one world ("wrong sha pin / tampered snapshot"), but a tampered
   pin is a *could-not-evaluate* in this counter family and aborts before any later surface is
   read, so an anchor-sha probe in the same world would be masked. C7 keeps the tamper (exit 2);
   C7a carries the anchor pin (4 of 6). Both are the plan's named mechanism, measured separately.
3. **C4 is expected to pass.** Q71: what a script-only world reaches is form-level, so C4 belongs
   beside the headline, never in the counter-defect column. Making it fail would require the
   counter to reject mechanically correct form, which is a finding about the predicate, not a
   defect in it.

---

## 3. Observed verdicts (draft counter, `allowed-tools surfaces backed …`, its own exit)

Receipt: `build/Kb79X02C2Controls.run.log` (verbose, every finding and every counter byte).

```
H    N=6/6     exit=0  M=1/6   as-expected
C0   N=0/6     exit=1  M=0/6   as-expected
C1   N=(none)  exit=2  M=-     as-expected
C2   N=0/6     exit=1  M=1/6   as-expected
C3   N=0/6     exit=1  M=1/6   as-expected
C4   N=6/6     exit=0  M=1/6   as-expected
C5   N=0/6     exit=1  M=1/6   as-expected
C6   N=4/6     exit=1  M=0/6   as-expected
C7   N=(none)  exit=2  M=-     as-expected
C7a  N=4/6     exit=1  M=1/6   as-expected
C8   N=0/6     exit=1  M=0/6   as-expected
C9   N=5/6     exit=0  M=1/6   as-expected
C10  N=4/6     exit=1  M=1/6   as-expected
c2_controls: 13 world(s), 0 divergence(s)
```

`M` is the counter's own `script-only world: M of 6` line in that world. The base revision
measured directly with the same draft prints `allowed-tools surfaces backed 0 of 6`, exit 1
(receipt `build/Kb79X02C2Controls.base-draft.txt`) — C0 reproduces the frozen do-nothing.

No control world other than **C4** reached the target with a mechanism the plan calls a defect;
C9 sits at exactly the target for the arithmetic reason named above.

---

## 4. Each world failed for its named mechanism (the counter's own words)

Quoted from `build/Kb79X02C2Controls.run.log`:

* **C0** — `entry corpus/knowledge/allowed-tools-surfaces-round79.md absent at b10bcbc6…`
  and `0 ## Core bullet(s) name the entry (want exactly 1)`.
* **C1** — `environment error: no manifest at .ufo/waves/round-79/snapshots/MANIFEST.sha256 …:
  the snapshots are unpinned, so (c) cannot be evaluated` — exit 2, never a backed surface.
* **C2** — every row: `located quote not found in its pinned snapshot after the text view:
  '<the other surface's sentence>'` (e.g. claude's row carries factory's sentence).
* **C3** — `spec: S226-spec.md: quote lies in the first-heading block (Q70)` for five surfaces and
  `msaf: S229-msaf.html: the located quote is a shared banner line (it also occurs in
  S226-spec.md, a different page): Q70` for the sixth. The banner was written to carry every
  frozen page token, so only Q70 can reject it — and it does.
* **C5** — `located quote is 2 words (want 5-25)` for all six (labels and tokens right, no quote).
* **C6** — `pi: S230: no URL on pi's pinned host(s) ['raw.githubusercontent.com/badlogic/pi-mono']:
  ['https://raw.githubusercontent.com/badlogic/pi-mono-evil/main/…']`, same for
  `mistral-vibe-evil`. Q32's whole-segment prefix is enforced, not a string prefix.
* **C7** — `environment error: snapshot_tampered: .ufo/waves/round-79/snapshots/S230-pi.md`, exit 2.
* **C7a** — `pi: S230: anchor sha256 000000000000… is not the snapshot's pin 66a709117830…`
  (same for vibe).
* **C8** — `spec: row carries 1 backticked token(s) (want >= 3): ['allowed-tools']` — the
  first-answer entry earns nothing.
* **C9** — `pi: 2 surface-table row(s) name pi (want exactly 1)`; `opened this round 5 of 6`.
* **C10** — `claude: located quote does not contain the token \`allowed-tools\`:
  'Tools Claude can use during the turn that invokes the skill'` (same for msaf).
* **H** — exit 0, no findings.

---

## 5. What this proves, and what it does not

Proves (on the draft bytes named in §10):

* The counter separates all ten plan-named shortcut mechanisms from an honest world: none of
  C1, C2, C3, C5, C6, C7, C7a, C8, C9, C10 reaches the target by its mechanism, and each fails
  with the finding that names the mechanism.
* The predicate is satisfiable at all: a well-formed world reaches `6 of 6`, exit 0, including
  all tree conjuncts (`province surfaces named 6 of 6`, `skill rule line ok`, `registry home ok`,
  `opened this round 6 of 6`) — the claim is not a predicate that nothing can pass.
* The base is a genuine do-nothing: `0 of 6`, exit 1, while `held at base: 5` (see §6.4).

Does **not** prove, and the L1 must not read it as claim evidence:

* anything about the six real pages: the fixtures are synthetic, so no quote, pin, token or label
  here is evidence about what any vendor states;
* that the frozen C2 counter behaves this way — I measured X01's draft, which changed three times
  during this seat (§10). The table in §2 is the pre-registration to re-run against the frozen
  bytes; the generator prints `DIVERGES` per world if the frozen counter disagrees;
* the real snapshot bytes, the real entry's cell arity, or the real registry rows.

---

## 6. Findings handed to the L1

**6.1 A script-only world reaches 6 of 6, not merely "high on form".** C4 builds snapshots from
fixed text, derives each quote as the shortest 5-25-word window holding `allowed-tools` and the
label's ground token, takes the three page tokens and the grant label from the frozen table,
computes the pins from the bytes, and assembles the entry — no sentence read, no page judged. The
counter backs all six and exits 0. The derived quotes are printed in the receipt, e.g.

```
derived S226: Experimental: support for allowed-tools may vary between agent implementations.
derived S227: The allowed-tools field grants the listed tools for the turn that invokes the skill, so Claude can use them without prompting you for approval.
derived S228: The allowed-tools field is metadata for review and packaging, and it does not add tools to the agent.
derived S229: allowed-tools Space-delimited list of pre-approved tools. Experimental, support may vary between agent implementations.
derived S230: The allowed-tools field is an Experimental list of pre-approved tools for the skill.
derived S231: markdown --- name: commit-helper description: Draft commit messages from the staged diff allowed-tools:
```

Consequence for the claim wording (Q71): the headline may assert only what C4 does not reach —
i.e. nothing about form, pins, quotes or tokens; what remains is that every grant label is true
of its page, which is reviewer judgement (RV/CR seats) and not measurable by this counter.

**6.2 The counter's own `script-only world` line cannot reach the target at measurement.** In the
draft (sha `74e067cc…`) the mechanical world writes `SCRIPT_LABEL = "unstated"` into *every*
surface row (constant at line 1164, row writer at line 1322), while (f) requires each surface's
frozen label — and only `vibe` is `unstated`. So `M ∈ {0, 1}` by construction: every world above
shows `M = 0` or `M = 1`, never 5. The `m < TARGET` conjunct therefore cannot fire in a
measurement (only its self-test, which rebinds SURFACES, exercises the ≥ target branch). Q71's
protection is nominal; C4 is the probe that actually shows a no-judgement entry passing. If the L1
wants (i) to mean something, the mechanical world must be scored against labels it *derived* from
each page, which is a counter change before freeze, not a data change.

**6.3 C9 at 5 of 6 exits 0 — record it as the plan's arithmetic, not as a pass.** The duplicate
row is correctly refused (`2 surface-table row(s) name pi`) and the surface is lost, but 5 still
meets `N >= 5`, so a malformed entry exits 0. Two things follow: the defect test for C9 is the N
value (6 = duplicate counted, a counter defect; 5 = refused), and the frozen target alone cannot
distinguish "one surface lost to a duplicate" from "one surface moved on the web". Suggested
report wording: `C9 duplicate row: 5 of 6, exit 0, pi disqualified; the target is met by the
frozen rule — no inflation observed`.

**6.4 `held at base: 5`, not 0: five of the six surfaces are already cited in the base registry.**
At `b10bcbc` the registry holds 151 rows; the frozen host+path pins already appear for
`agentskills.io/specification`, `code.claude.com/docs/en/skills`,
`learn.microsoft.com/en-us/agent-framework/agents/skills`,
`raw.githubusercontent.com/badlogic/pi-mono/main/...` and
`raw.githubusercontent.com/mistralai/mistral-vibe/main/README.md`; only `factory` is new (its host
moved to `docs.factory.com/harness/skills` before data). So the *population* is not the claim — the
per-client reading of the field is — and C0 (`0 of 6`, `held at base: 5`) shows the counter keeps
"host present" separate from "surface backed". The lesson/SCORECARD wording should not imply six
newly discovered sources.

**6.5 Q32 holds, including the `.md` route.** C6's two `-evil` siblings are rejected by
whole-segment prefix, and the draft's `same_page()` additionally accepts a bare `.md` suffix on one
side for the factory snapshot route. That exception is the only place two URLs are the same page;
C6 shows it does not become a prefix loophole.

---

## 7. Plumbing validation against the template counter

`verifiers/check_cn_vendor_surfaces.py` (round 73) was run over the same 13 worlds:

```
python3 -B c2_controls.py --counter …/verifiers/check_cn_vendor_surfaces.py \
  --base-rev 072048fa8e8a52c707d25f7079772fa317244eb7 --base-tree <lane> --work <scratch>
-> 13 worlds built and measured, every world exit 1, generator exit 1 (all DIVERGE by construction)
```

What that run validates: world construction (init, toplevel assertion, index from the base tree,
blob writes, commit-tree), resolution of the *template's* own frozen `BASE_REV` through the
alternates line (`held at base: 0` printed, so its `held_at_base()` did not raise), counter
invocation with `--repo <abs> --rev <commit>`, and line capture. It does **not** validate
discrimination: the template counts `vendor skill surfaces backed 0 of 4` because its frozen entry
path (`chinese-vendor-skill-surfaces-round73.md`) is absent from every world. Receipt:
`build/Kb79X02C2Controls.plumbing.log`.

The template run also forced one design decision that the r79 counter inherits: a world must have
the frozen `BASE_REV` in its object store, or the counter exits 2 before printing a verdict. That
is why the worlds share the base object store instead of being self-contained fixtures.

---

## 8. Readings a reviewer can attack (named, not hidden)

* **Synthetic text, not the real pages.** Deliberate: a control world must not be able to supply
  claim data. The cost is that the fixture must satisfy the counter's *frozen table* (page tokens,
  factory's moved host, the markdown text view that deletes backticks and list markers, the
  entry line naming the shaping, row arity 5, registry arity 11, `fetched … sha256` anchor). If
  the certain-claim seat's real rows use a different shape, the counter's findings on the real
  entry are the authority; my worlds only prove the mechanisms are refused.
* **World = base tree + fixtures.** Tree conjuncts (g)(h) are therefore exercised on a real
  `SKILL.md`/`PROVINCE.md` *replacement*, not on the lane's files: an honest world's tree
  conjuncts are my fixtures, so a `skill rule line ok` here says the counter's parser accepts a
  canonical rule line, not that the lane's landed line does.
* **The counter is injected into every world at its lane path.** A registry home row naming
  `verifiers/check_allowed_tools.py` is therefore always resolvable in a world; the counter is
  never *executed* from the measured tree (the run uses `--counter <path>`), so no instrument of
  the measured revision runs.
* **`--base-rev` is a knob.** It defaults to the plan's base `b10bcbc…`; the template run had to
  pass its own `072048fa…`. A world measured with the wrong base revision would exit 2, not
  silently pass, because the counter reads `BASE_REV` from the repo.
* **C0 is the base revision itself** (no world commit), which is exactly the do-nothing world of
  record; it is the only world whose measured tree is not "base + fixtures".
* **Expectations live in the file.** `EXPECT` is data in the generator, fixed before the first
  run and printed by `--list` into `build/Kb79X02C2Controls.expected.txt`. The generator's exit
  code means "matched pre-registration", never "claim holds".

---

## 9. Evidence

* Generator: `.ufo/waves/round-79/build/c2_controls.py`,
  sha256 `242d970c2f96bbb94cc07d16ec72f16eafa961e963dbbb199473bcaf4c26288e`.
* Pre-registration: `.ufo/waves/round-79/build/Kb79X02C2Controls.expected.txt` (`--list`, rc=0).
* World run: `.ufo/waves/round-79/build/Kb79X02C2Controls.run.log` (13 worlds, 0 divergences,
  generator rc=0; every finding and every counter line in full).
* Base measurement with the same draft: `.ufo/waves/round-79/build/Kb79X02C2Controls.base-draft.txt`
  (`allowed-tools surfaces backed 0 of 6`, rc=1).
* Plumbing validation: `.ufo/waves/round-79/build/Kb79X02C2Controls.plumbing.log`.
* Hashes, exact commands and their own exit codes:
  `.ufo/waves/round-79/build/Kb79X02C2Controls.receipts.txt`.
* Draft counter measured: source `.ufo/waves/round-79/build/check_allowed_tools.py`
  sha256 `74e067ccad7813d91826ee503c8ee93ba47d3a4a05b12ec67a82791d93f722a6`
  (filled copy `ae1cb406…`, blanked sha `50c0e10b…`). **Not frozen.**
* Tooling: nothing installed, no pacman, no host service touched (operator 2026-10-19 authority
  unused). `disk-guard.sh status` read before the run (idle=27, largest scratch 587.6M); a full
  13-world pass costs ~4 MB and ~2 s because worlds are plumbing commits over the shared object
  store.
* Scratch `/fast/scratch/hyaku/kotoba-r79/Kb79X02C2Controls` removed before delivery.

---

## 10. Risks, freshness, blockers

* **The counter is a moving draft.** X01 was still editing while I worked; three different drafts
  were measured (blanked shas `b15a6139…`, `3aa7f2f6…`, `50c0e10b…`; the file grew from 91 834 B
  to 100 224 B to its current size). Verdicts were 13/13 as pre-registered on the last two. The
  L1 must re-run the invocation in §1 against the **frozen** counter; if the freeze changes the
  entry's shaping line, row/registry arity, a page token, factory's host, `SCRIPT_LABEL`, or the
  exit rule, expect `DIVERGES` per affected world — that divergence is the signal this generator
  exists to give, and it is why the pre-registration table is fixed before the run.
* **C9 will read `5 of 6`, exit 0** on a counter that enforces "exactly one row per surface". That
  is the frozen rule, not a defect; report the mechanism, not the exit code (§6.3).
* **C4 will read `6 of 6`, exit 0** on any counter that reads cells, tokens, pins and quotes.
  Report it beside the headline per Q71 (§6.1), and state that grant-label truth is not measured.
* **The (i) conjunct is nominal at measurement** while `SCRIPT_LABEL = "unstated"` is written for
  every surface (§6.2). If the L1 wants (i) to protect the claim, that is a pre-freeze counter
  change, not something this seat may do.
* No blockers. No work was left unfinished; nothing was written outside
  `.ufo/waves/round-79/` (generator, four receipts) and this report, and no lane git state was
  touched (read-only `git -C <lane> show/rev-parse/archive` only).

VERDICT: C2 control suite built and pre-registered before data; 13/13 worlds match expectation on the draft counter — all ten plan shortcut worlds are refused by their named mechanism, an honest world reaches 6 of 6, and a script-only world also reaches 6 of 6 (form-level per Q71) while the counter's own script-only conjunct is structurally capped at 1; re-run required on the frozen counter.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/c2_controls.py, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79X02C2Controls.expected.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79X02C2Controls.run.log, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79X02C2Controls.plumbing.log, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79X02C2Controls.base-draft.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/build/Kb79X02C2Controls.receipts.txt, /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-79/w1/Kb79X02C2Controls.md
