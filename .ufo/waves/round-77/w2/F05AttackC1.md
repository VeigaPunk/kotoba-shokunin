# F05AttackC1 — C1 semantic/counter boundary attack

Axes: depth, consistency, calibration, freshness, operability.

## Counterexample and evidence

The exact frozen C1 counter (`verifiers/check_desc_craft.py`, SHA-256 `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e`) was run against the only current landed revision, freeze HEAD `6523aced1ee0ebe07dca996213bdc645a6acbd1e`:

```sh
python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e
```

Output ended `description craft backed 0 of 6`; own process exit status was 1. All six conjuncts fail because the entry, lesson, Skill row, and SOURCES used-by update are not committed at that revision. This matches the plan's designated pre-data freeze state, not a green C1 claim. The lane HEAD is still the freeze commit; no w2 claim-data tip is present to attack. Thus C1 is not verified as landed, and should not be scored as a successful depth move.

The strongest semantic boundary counterexample available is documented in the landed executor report `.ufo/waves/round-77/w1/E06EntryVerify.md`, lines 101–108, and its named mutant receipts. Counter (b) counts located quotes across the *whole entry*, including provenance `recheck:` tokens. The report states a mutant with wrong-page rule-table quotes still scores `6 of 6` if those recheck tokens remain; only after de-quoting the recheck tokens as well does the wrong-page mutant fail (b). This means (b) does not establish the intended semantic proposition that the admitted guidance/rule table is supported by page-unique quotes; it establishes that the entry somewhere contains enough qualifying quotes. The actual entry draft is said to contain eight body quotes, so this is a counter-boundary defect/hollow-world survivor, not evidence the current draft itself is hollow.

This boundary is already consistent with round-76 frozen counter docstring lines 31–36 and its explicit warning at lines 34 (the page's judgement is delegated to non-author seats). It does not invalidate the narrower literal predicate, but it limits the broader semantic claim; do not describe counter success alone as semantic validation of the advice.

## Smallest safe correction and axis impact

Keep the frozen counter and claim contract unchanged for this round. At the next pre-data contract revision, constrain counted quotes to the entry's rule/evidence table rather than provenance/recheck text, and include a must-fail mutant with wrong-page rule quotes plus valid page quotes only in `recheck:`. This improves calibration and depth claim fidelity; no identified harm to consistency, freshness, or operability, though it is a future predicate change and must not be silently applied to the frozen r77 counter.

Current precise disposition: C1 counter was run, exit 1 at the freeze revision; no landed C1 claim exists at HEAD. No gate was run against a post-data revision. No quote was independently reopened in this seat, so S213 freshness remains unassessed here. No tool installs.

VERDICT: C1 is not landed at HEAD (frozen counter returns 0 of 6, exit 1); counter boundary allows wrong-page rule evidence to be masked by page quotes in recheck provenance, so semantic backing is not established by that predicate alone.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F05AttackC1.md