Result: DONE — all 12 pinned cases have an individually isolating delegate defect that made its box fail the frozen counter.

## Method and baseline

The cases and expected statuses are pinned in `verifiers/check_alwayson_boxes.py:64-88`; the runner requires each expected status and exit code (`:28-38,107-119`) and reports each box result (`:139-166`). I cloned the plan commit `3bb0a7a33e6eb585a83a1a55dee30b26079b1e36` to `/fast/scratch/hyaku/kotoba-r53/KotobaR53.MutCounterC2`. Both target entries in `verifiers/checklist-baseline.json` were mapped to `delegated:verifiers/alwayson_probe.py`; each probe commit changes only that delegate's `MODE`, so the other box remains a passing control.

Command for every run:

```text
python3 -B /fast/scratch/hyaku/kotoba-r53/KotobaR53.MutCounterC2/verifiers/check_alwayson_boxes.py --rev HEAD --repo /fast/scratch/hyaku/kotoba-r53/KotobaR53.MutCounterC2
```

On the pristine plan commit, the command printed `always-on boxes executed and discriminating 0 of 8`, both boxes `not counted (disposition unexecuted)`, exit 1. The first correct-delegate draft also failed (commit `9dcfb8adc2ba93c9c48340668134b56af4e265fd`): `1 of 8`; `alwayson.04` had `iso-timestamp expect FAIL, saw exit 0, PASS`; exit 1. This was a baseline defect, not a killed mutant. After correcting the timestamp date boundary, the baseline at `8ce2a1983b42fe72e84b011ab5bd155acf57f144` printed `2 of 8`, both boxes `counted (6 of 6 cases as pinned)`, exit 0.

## Single-case mutants

Each row is one locally committed delegate revision. “Counted?” refers to the mutated box; the other box was counted (6/6) in every run. Each actual output was `always-on boxes executed and discriminating 1 of 8`, the target box `not counted (1 of 6 cases wrong: …)`, the control box `counted (6 of 6 cases as pinned)`, exit 1.

| Case | Naive delegate defect (passes the other 5 cases) | Counted? / exact failing observation | Mutant commit | Mutated delegate SHA-256 |
|---|---|---|---|---|
| alwayson.04 / plain-rules | Treats a rule set with no dated text as invalid unless it also pins a version number. | No — `plain-rules expect PASS, saw exit 1, FAIL` | `6c75465bdeaffbda0f76c8c38bc636032329a0c1` | `4e37e86c3769402f36200601a2816c2ffd84264fa359750ce8de621ffa32fb76` |
| alwayson.04 / version-number | Mistakes a dotted version (`3.12`) for a date. | No — `version-number expect PASS, saw exit 1, FAIL` | `9e7a9c43d026c40984130744148416fe71f85bf7` | `b93c0f1a2dd54627957a3eefa519b6a9798a60f4ffdaa75c3c2ab42dd4f7bc8b` |
| alwayson.04 / iso-date | Misses an ISO date when introduced by `Until`. | No — `iso-date expect FAIL, saw exit 0, PASS` | `ba500af8c5c4fdf004cab7f608552c932d63028f` | `3e552fb53a7389389ff63809db46baea5014db9683a7de3570730c102c4610d1` |
| alwayson.04 / iso-timestamp | Strips ISO timestamps before checking for dates. | No — `iso-timestamp expect FAIL, saw exit 0, PASS` | `ca431afd27a47317082bbe041ada76e7059ab364` | `3bb2c2e807c96555c129cb33e8bad034f44b4a36235ac249ae95480cfb77449c` |
| alwayson.04 / month-day | Recognizes numeric ISO dates but not named month/day dates. | No — `month-day expect FAIL, saw exit 0, PASS` | `645847d70ab016e66d9809359859356bb893f4c2` | `a5e884220a5c83458b209fa08bf5e89140732762c34121eed3625a174ef63f3a` |
| alwayson.04 / dated-claude-md | Scans `AGENTS.md` only, ignoring `CLAUDE.md`. | No — `dated-claude-md expect FAIL, saw exit 0, PASS` | `75584c4216dc5bae23bf01127963a897bd9bd862` | `acd69931f8356601ff48deea605f6bdf8a78aaaae5683be3f7f1b1ca8b332c66` |
| alwayson.07 / agents-only | Rejects an `AGENTS.md`-only repository because it expects `CLAUDE.md`. | No — `agents-only expect PASS, saw exit 1, FAIL` | `9d5435caed87a391edb66e6da7c1cb5fccf2cc45` | `da0759d9d6d5fe231bbaa26b9a6ec38697439596619ace55386fca5a801d1274` |
| alwayson.07 / claude-only | Rejects a `CLAUDE.md`-only repository because it expects `AGENTS.md`. | No — `claude-only expect PASS, saw exit 1, FAIL` | `5c6728eab3043a40996d8c2062586efc8ec94a50` | `b2b5dbe5045d23aed024f04b11de60c19d88eb30ed4decf85dc55c694cd13fdf` |
| alwayson.07 / import-redirect | Recognizes the symlink redirect but not the `@AGENTS.md` import. | No — `import-redirect expect PASS, saw exit 1, FAIL` | `ef49ea4010041011fd583b8fdc074013deafbcca` | `7abad084aa071a6c717bed8cd03271b7c7689771056d46fe3769de5cdd95625b` |
| alwayson.07 / symlink-redirect | Recognizes the `@AGENTS.md` import but not the symlink redirect. | No — `symlink-redirect expect PASS, saw exit 1, FAIL` | `d399f90f01135f49552544cf5e9f0dc0fa16bb8b` | `cda94288d091fe1492f972d412ac95bc9cb19dbeb10397a138d1a641bde4ef8a` |
| alwayson.07 / two-rule-files | Incorrectly accepts two files when `CLAUDE.md` has no `AGENTS.md` reference. | No — `two-rule-files expect FAIL, saw exit 0, PASS` | `53e4f69bc0f9ab9eca926e117229acf48e7155a7` | `eee7143a30f5e76049b25d1b712052803cdc27e504693413af2644a973b41c66` |
| alwayson.07 / prose-mention | Treats any `AGENTS.md` mention as a redirect, including prose. | No — `prose-mention expect FAIL, saw exit 0, PASS` | `f03547d732f7ccb886780a3d3f78aa107d70c42d` | `e2a4feddbb75085cf247898e0ab172befcd2eb807f1b7fa298ce9a111e2e2c1f` |

Result: every case is individually discriminating in this set; no case lacked a simple isolating delegate.

## Restoration evidence

Before every mutant, the delegate SHA-256 was `310ea301c369140fb2e91152d2562fefbe99014d42e531694b7336f91ec1d121`. The table gives each post-mutation hash. After each probe, the delegate was restored and its observed hash returned to that exact baseline value. The mapped baseline JSON stayed unchanged throughout the probes: SHA-256 `bac46845df38527eab96421d151b8865d72ec385871b10c772d36a321bf70203`.

After the final restoration, local commit `7cfc195d4f402428ec3b7fc18d8eb64e7c09178c` was measured with the same command: `always-on boxes executed and discriminating 2 of 8`; both boxes `counted (6 of 6 cases as pinned)`, exit 0. Final `sha256sum` output was the baseline delegate hash above and the unchanged JSON hash above.

Scope note: one initial edit was resolved against the lane-relative JSON path by mistake; I immediately restored the two original `unexecuted:` disposition lines exactly as read, then applied all probe changes only in the scratch clone. No tool installs were needed.
