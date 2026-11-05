source: S262 (PIT (pitest) documentation — "Basic concepts" — https://pitest.org/quickstart/basic_concepts — § Equivalent Mutations, HTML lines 120-146; § Running the tests, HTML lines 154-179; the page's own upstream source file quickstart/basic_concepts.markdown in hcoles/pitest-site (branch gh-pages) at revision e8995cd59e3c, where all three located quotes are quote-equal at markdown lines 59-60, 107 and 109; fetched 2026-11-05) and S261 (own-work — the round-89 mutant matrix `git show 0c20d8ab65587aee0e97b7d14c801ae6dc44c2e5:.ufo/waves/round-89/w1/MutTesterGates/mutants.tsv`, sha256 bba3a5c0506274df8099beed7950af92805e80ac3459d5cd4ac1341de362e1cc)
verified-at: 2026-11-05 @ base 9af1a7af2adf0ab07cfd53f92affc1ed8d992262 (the round-91 freeze commit; at that revision the battery's own self-test reads `0 failure(s) over 19 assertions` and the committed manifest carries 14 kill rows and 6 equivalent rows — `.ufo/waves/round-91/receipts/base-battery-manifest.txt` reads 14 / 6)
recheck: python3 -B verifiers/check_mutation_battery.py --rev <landing-rev> --work <scratch-dir> (expect exactly `mutation battery killed 17 of 17 kill-set; equivalents survived 6 of 6; disclosed survivors 0 of 0`, exit 0, with the G1/G2/G3 guard lines PASS) and python3 -B verifiers/check_mutation_battery.py --self-test (expect `0 failure(s) over N assertions` with N >= 22, exit 0) — the frozen predicate of plans/round-91.md § C1

# Mutation battery (round 91 C1): three new self-test arms guard the battery's own G1/G2 code paths

## What the instrument is at the base

`verifiers/check_mutation_battery.py` reads three committed inputs at `--rev` — the gates it probes
(`verifiers/check_freeze_gate.py`, `verifiers/check_r86_routed_repairs_v3.py`), its manifest
`verifiers/fixtures/mutation-battery/manifest.tsv`, and its own registry row in `SKILL.md` — and
prints

    mutation battery killed K of M kill-set; equivalents survived E of E; disclosed survivors S of S

exiting 0 iff `K == M`, `E == E`, `S == S_declared` and guards G1-G3 pass. The three guards it
protects are the battery's own:

- **G1 revision identity** — `--rev` must be a full 40-hex commit of the lane; the scratch clone is
  checked out detached at that revision; every target and the manifest are read through
  `git show <rev>:<path>`, never the working tree; and the scratch clone must be clean
  (`git status --porcelain` must be empty).
- **G2 copy integrity** — every revision copy and every mutant is written and then read back from
  disk, and the sha256 read back must equal the sha256 recorded from the revision bytes.
- **G3 registry presence** — `git show <rev>:SKILL.md` names `check_mutation_battery.py` on at least
  one line.

The kill rule is a baseline flip, not a verdict: each target's probes run unmodified first, and a
kill-class mutant is killed only when some probe's exit code or result-bearing output differs from
that observed baseline. A probe timeout counts as a flip.

## The three new guard arms (round-91 C1)

At the base the battery's own self-test had no arm for its own guards, and the round-90 mutant
matrix showed why: the three battery-guard mutants `mb-m2` (G1 commit-check skipped), `mb-m15` (G1
clean-tree guard off) and `mb-m16` (revision-copy restore not re-read after each mutant) survived
because no self-test arm exercised those paths. C1 adds one arm per guard path, each of which is
red when its guard is disabled — the arms *are* the kill channel for the three new manifest rows:

1. **G1 commit check.** A full-hex `--rev` that is not a commit of the lane must exit 2 and the
   refusal must say the revision is not a commit. This is the arm that kills `mb-m2`: with the
   commit check disabled, the battery proceeds with a revision that does not exist and the arm's
   world reads a different exit.
2. **G1 clean-tree guard.** A scratch clone whose working tree is dirtied must exit 2 with a
   refusal that says the scratch clone is not clean at `--rev`. This is the arm that kills
   `mb-m15`: with the clean-tree check off, a dirty scratch clone is measured as if it were the
   revision.
3. **G2 restore read-back.** A revision copy that is tampered with on restore after a mutant must
   exit 2, and the refusal must name G2 copy integrity on the restore copy. This is the arm that
   kills `mb-m16`: with the restore not re-read, the next mutant is applied to bytes that are not
   the revision's, and the copy-integrity read-back is what catches it.

To make those arms reachable, the frozen probe set gains a third target: the battery's own
`verifiers/check_mutation_battery.py`, probed with `--self-test` and a declared baseline exit of 0.
The manifest's target set therefore has to equal the probe set's keys, and the three new kill rows
target the battery itself. The three recipes are anchored regex edits against the battery's own
revision bytes, ported from the round-90 harness with the anchors re-verified against the final
bytes.

## The two-sided rule (Q47) and why the equivalents stay generated

The measure is not a kill rate. **Every** declared kill-class row must be killed **and** every
generated equivalent must survive. The equivalent class is *generated at measurement time*: for a
target, the rewrite kinds (`comment-insert`, `docstring-reword`, `trailing-whitespace`) are applied
at every eligible site of the target's revision bytes — the eligible sites come from the AST and
from tokenize over those bytes, not from a published list of sites. A published fixed list would
be a label a self-test could key on, so the set stays generated and the measure stays a claim
rather than a record.

S262 is the external ground for why requiring the equivalents to survive is not charging the test
suite for a defect: the mutation-testing tool's own documentation separates **Killed**,
**Survived** and **No coverage** as three different outcomes and names *equivalence* — a mutant
that behaves exactly as the unmutated class, or differently only outside the scope of testing — as
a reason a mutant survives by construction. A survivor is therefore not automatically a
weakness of the tests, and the two-sided rule can hold both halves without contradiction.

## Bounds (what this measure does not prove)

1. **The equivalence leg is over the three declared rewrite kinds on the two round-89 gate targets
   only.** It is not a general equivalence oracle. In the C1 manifest the battery's own target
   contributes kill rows and no equivalent row, so the battery's own bytes are not
   equivalence-checked by the committed manifest.
2. **The kill rule is a baseline flip.** A mutant is killed when a probe's exit code or
   result-bearing output differs from the observed baseline; that is evidence the mutant changed
   what the probe measures, not a claim that the mutant is semantically wrong.
3. **The minimum pins are floors, not coverage.** `M >= 8` and `E >= 4` stop an empty or trivial
   manifest from satisfying the equalities; they do not establish that the declared rows cover the
   targets, and the kill-set is bounded to the rows the manifest declares.
4. **Anchors are revision-bound.** A recipe whose anchor is absent from the measured bytes is
   could-not-evaluate (exit 2), never skipped.
5. **The d5 baseline is path-dependent (Q79).** The base-receipt probe reads at the round base, so
   a kill there is a flip from the observed value, not from a fixed expectation.
6. **The three new arms are self-test arms and they cover three specific regressions.** They
   exercise the battery's G1 commit check, its G1 clean-tree check and its G2 restore read-back.
   They do not enumerate every way those guards could be weakened; the manifest's rows are the
   bounded set the measure scores.
7. **G3 is registry presence only.** It checks that `SKILL.md` names the battery on at least one
   line; it does not check what that line says.

## Reviewer-judged parts

The manifest's class assignment per row, the sufficiency of the probe set, and the disposition of
the three battery-guard mutants are named non-author seats' calls in the round-91 wave
(`ReviewerBattery`, `MutTesterBattery`); they are not measured here.
