# F03CheckopenS213 — round-77 w2 source falsification

Axes: depth (source quote and digest), freshness (independent re-open), calibration (claim gate state), consistency (row and artifact landing).

## S213 re-open

- URL: https://agentskills.io/skill-creation/optimizing-descriptions.md
- Accessed: 2026-10-27 via `read` URL fetch; response supplied the markdown page text (HTTP status is not exposed by this reader, so not independently asserted here).
- Exact located quote, from `## Testing whether a description triggers` / `### Running multiple times`: “A should-trigger query passes if its trigger rate is above a threshold (0.5 is a reasonable default).” (17 whitespace words). Present verbatim in fetched text.
- Committed snapshot: `.ufo/waves/round-76/snapshots/optimizing-descriptions.md`; `sha256sum` output `7cc54fbb6abbcf08c33e7b320fd01a1fb9696426270da3b588a398d243bfd837`, matching the pinned digest in `plans/round-77.md` (`7cc54fbb…bd837`). This establishes snapshot digest, not equality of today's fetched bytes: the URL reader did not provide a raw-byte artifact or digest.
- Registry at frozen lane tip `6523aced1ee0ebe07dca996213bdc645a6acbd1e` has S213 using this same URL and quote; `used-by` still points to `corpus/knowledge/skill-eval-artefacts-round70.md`, not the proposed description-craft entry (the entry is not committed at this tip).

## Claim gate and landing

Exact command:
`python3 -B /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_desc_craft.py --rev 6523aced1ee0ebe07dca996213bdc645a6acbd1e`

Observed output ended `description craft backed 0 of 6`; exact exit status captured by shell: `exit=1`. Failing conjuncts were (a) snapshot chain, (b) located quotes, (c) act-on, (d) self-audit, (e) registry, (f) provenance. In particular `corpus/knowledge/description-craft-round76.md` and `corpus/lessons/round-76.md` are not committed at measured revision. Read-only `git show --stat` identifies tip commit `6523ace` as only “round-77: freeze plan, base receipts (counters unchanged from r76 freeze)” (5 files: plan and base receipts). Thus the specified landed claim data is not landed at the inspected HEAD; no S213/C1 success claim is warranted. This is the plan's pre-data frozen base, rather than evidence of a completed w1 integration.

Counter integrity observed: `sha256sum` gives `cf3c45d9e3985f11889816f4bb371dc0d5541c10c09ce2ab3966a4bff4603b9e` for `verifiers/check_desc_craft.py` and `989203c40e1aab55fc14ee1d444dd4fa8b49fe01144b2dcdeaa6a27fa39f4a63` for `verifiers/check_r75_routed_repairs.py`, both matching plan pins. Only C1 was run here; C2 not run, so no verdict on C2.

Minimal repair: integrate the frozen C1 claim artifacts and S213 used-by update at the wave's authorized integration step, then rerun C1 against the resulting landed revision and reopen/capture source raw bytes with digest. This is necessary to test the claim, not an axis-harming change; current evidence does not support assessing effects on other axes.

No lane files or git/jj state modified; no tools installed. No scratch clone used. LSP device was not available in this session; source adjudication is based on the direct page fetch and committed bytes, not a semantic LSP result.

VERDICT: S213’s located quote is present and the committed snapshot digest matches the pinned digest; however, HEAD 6523aced is only the freeze, C1 returns 0 of 6 (exit 1), and claim data is not committed, so landed C1 remains unverified; C2 was not run.
DELIVERABLES: /home/vgpnk/Projects/shokunin/kotoba-shokunin/.ufo/waves/round-77/w2/F03CheckopenS213.md
