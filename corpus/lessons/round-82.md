# Round 82 — kotoba (attempt 3, Windows host; attempts 1-2 were the Linux-host dispatches)

Base for this attempt: `cbc72c9f9269f27ea8f3e92eee114e0ff0bac988` (freeze;
parent `ff3b9625` is the attempt-2 wrap-up tip). Two claims on distinct axes:
**C1' freshness** — the host's installed-skill instruction surfaces are
enumerated, hashed and classified by a new read-only instrument (capability
acquisition, sourced to S251); **C2' operability** — the checklist self-test is
hermetic on the current host (`3 failure(s) over 1863` → `0 failure(s) over
1864`, exit 0). The round moved hosts mid-round (Linux → Windows): every
before-value was re-measured at intake (Q19), and one frozen claim was ruled
out because its subject binary does not exist on this host
(`plans/round-82-addendum-2.md` § Ruled out).

## Gate

- **Round-start census** `bash <fleet root>/scripts/sources-census.sh validate
  --root <fleet root> kotoba` → `kotoba ok`, exit 0, 176 data rows, the known
  32 W04 duplicate-URL warnings
  (`.ufo/waves/round-82/receipts/census-round-start-win.txt`, run before any
  lane change). **Round-end census** same command → `kotoba ok`, exit 0, 177
  data rows (receipt `.ufo/waves/round-82/receipts/census-round-end-win.txt`).
  Row-count command: `grep -cE '^ {0,3}\| S[0-9]{3}' corpus/SOURCES.md` → 176
  before, 177 after. Rows added: S251 (own-work, tier B, mined) — the host
  installed-skill instruction surfaces, opened this round; the round-82 plan's
  S251 reservation (loader re-derivation receipt) lapsed unopened when the
  host move removed its subject binary, recorded in the row's anchor cell and
  `plans/round-82-addendum-2.md`. Rows touched old→new: S248 `queued` →
  `mined` (the routed append-only status transition from r81's C2; S248 was
  re-opened this round first: HTTP 200, 28435 B, sha256 `d7419fbd6d6c…`, page
  moved since the r81 pin `ac62c2df…`, both located quotes still present,
  recorded in the row's anchor cell). Frontier rows advanced: 0 (the S251
  surface enters Core by the C1' instrument, not the corpus Frontier list).
- **C1' freshness — capability, verified on this host.** New instrument
  `verifiers/check_host_skill_surfaces.py`: self-test `0 failure(s) over 12
  assertions`, exit 0; live census `host skill surfaces measured 9: identical
  0, drifted 6, lane-absent 3`, exit 0 (ledger
  `.ufo/waves/round-82/receipts/after-host-skill-census-ledger.txt`; before —
  no instrument existed and drift was unknown outside a manual sha table,
  `.ufo/waves/round-82/receipts/before-host-skills-shas.txt`). Registry row
  landed in `SKILL.md` § Gate registry (598/600 line budget);
  `check_gate_registry.py --rev <new rev>` stays green (measured after the
  content commit). Capability row entered `SCORECARD.md` § Capabilities this
  round. Sibling bound: the drifted installed copies are audited read-only and
  reported to their owning lanes; nothing outside this lane was written.
- **C2' operability — verified on this host.** `python -B
  verifiers/verify_skill_checklist.py --self-test` → before `3 failure(s) over
  1863 assertions`, exit 1
  (`.ufo/waves/round-82/receipts/before-checklist-selftest-win.txt`) → after
  `0 failure(s) over 1864 assertions`, exit 0 (receipt
  `.ufo/waves/round-82/receipts/after-checklist-selftest-win.txt`). The two
  live-read governance arms are replaced by isolated fixture arms (fixture
  world: two errata + four corrections land; the second erratum row is
  load-bearing — dropping it or lowering the horizon turns the world red
  naming the row; an unrelated-governance-mutation arm keeps the world green),
  and the delegated-absolute-target assertion compares the `repr()` form the
  gate prints (Windows `repr` doubles backslashes; the rejection semantics
  asserted are unchanged). `check_governance_citations` is untouched: the
  public live gate still flags genuinely dead citations — it is red on this
  host because the lane's parent is no longer the fleet root, so live `../`
  citations do not resolve; that red is named debt, not silently fixed.
  Per `plans/round-82-addendum-1.md`, the postimage blob
  `9be2470bf33921dc5c34d99f8154c105b1aaa695` is appended to
  `check_tip_battery.py` `INSTRUMENT_PINS` for the checklist verifier with an
  inline round-82 reason; existing pins kept; the floors registry is not
  edited (floor 1863 unchanged, observed 1864 ≥ floor).
- **Named debt (pre-existing reds, this host, not claimed as passing):** the
  tip battery at the attempt base reads `2 of 6`, exit 1, absolute `--repo`
  form (receipt `.ufo/waves/round-82/receipts/before-tip-battery-win-abs.txt`):
  registry and sweep green; floors, checklist live gate, corpus integrity and
  independent red — most instruments' self-tests degrade on Windows (floors
  detail in `plans/round-82-addendum-2.md`). New routed defect: the battery's
  `--repo .` relative form reads `1 of 6` with four gates `absent at <rev>`
  (receipt `.ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt`) —
  `build_sandbox` passes the source path to `git clone --shared` as given, so
  a relative path produces a sandbox whose alternates do not resolve. Fix
  routed, not landed: the round's one counter amendment is spent (addendum-1
  pin admission).
- **Assimilation:** `considerthese/` inspected (2026-10-19 … 2026-10-26
  operator digests); no proposal adopted — the two claims were already
  grounded in the round contract's audit-surface ruling and the r81 routed
  duties. Assimilation: none — shokuknow unreachable.
- **Dispatch:** the old host's wave dispatcher does not exist here; the ≥8-L2
  floor was attempted once through this host's batched subagent surface for
  read-only reconnaissance of the landed bytes (result recorded in the round
  report), never padded.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| freeze-ordering (attempt 2, Linux host): the round's no-harm base battery was captured after the plan-only commit, not before it — the freeze protocol names the order but nothing enforced it | `plans/round-82-addendum-1.md` § Ordering correction; `.ufo/waves/round-82/receipts/before-tip-battery.txt` (`2 of 6`, exit 1, taken after `006a834`) | mined this round (the attempt-2 report named it; no lesson file existed until now) | not landed this round; next round: a pre-freeze gate that refuses the plan commit while the base-battery receipt is missing or post-dates the freeze |
| host-bound before-values (this attempt): the frozen plan carried a Linux-host before (`1 failure(s) over 1863`) that did not survive the host move — this host reads `3 failure(s) over 1863` before any edit, and a third arm fails only on Windows path-`repr` | `plans/round-82-addendum-2.md` § Host change; `.ufo/waves/round-82/receipts/before-checklist-selftest-win.txt` vs the attempt-2 receipt | captured by the intake re-measure (Q19) before any after-value | landed this round: every before re-measured at intake and committed before the freeze; the addendum declares the re-measure a round rule for host moves |
| form-dependence found while measuring (this attempt): `check_tip_battery.py --repo .` (relative) breaks its own sandbox clone on this host while the absolute form works — the r81 predicate demanded both forms agree, so the class is a real regression risk on any host where cwd ≠ repo | `.ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt` vs `.ufo/waves/round-82/receipts/before-tip-battery-win-abs.txt` | captured by running both forms at intake (the r81 habit) | routed with both-forms evidence; the one-line resolve inside `build_sandbox` stays unlanded this round (the round's counter-amendment budget is spent) |

## Correction (round 83, append-only; r82 closure D1 — evidence-pointer name drift)
The receipt citations in this lesson's Gate (named-debt bullet) and Mistakes
row 3 that read `.ufo/waves/round-82/receipts/before-tip-battery-win-dot.txt`
are name drift: the dot-form (`--repo .`) receipt was committed as
`.ufo/waves/round-82/receipts/before-tip-battery-win.txt` (same bytes:
`guards 5 of 5; tip battery exit 0: 1 of 6`, four gates
`absent at ff3b962561eaef436c6bf77c8ea9bfdc167f87a1`, measured rev
`ff3b962561eaef436c6bf77c8ea9bfdc167f87a1`). No file named
`before-tip-battery-win-dot.txt` exists at any round-82 rev. Read every
`-dot` citation in this file and in the round-82 fleet report as
`before-tip-battery-win.txt`. Round-83 follow-up: the dot-form failure this
receipt recorded does not reproduce at the r83 tip — both invocation forms
read `2 of 6`, exit 1, gate lines identical modulo wall time — and
`git clone --shared .` writes an absolute alternates entry on this host's
git, so this lesson's Mistakes row 3 root-cause sentence ("build_sandbox
passes the source path to `git clone --shared` as given") does not describe a
reproducible mechanism here; the routed `build_sandbox` resolve stays
unlanded (main() already resolves at line 749 of the r82 base).
