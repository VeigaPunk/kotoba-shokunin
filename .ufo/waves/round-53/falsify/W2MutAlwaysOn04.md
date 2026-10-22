Result: MIXED — the frozen counter killed four mutants; a fenced-date exemption survived the counter but was killed by the detector self-test.

## Scope and baseline

Target: `alwayson.04` in `verifiers/verify_alwayson.py` at `c775d6823bfca8f0de8c0874032a954438b38edc`. The instrument documents that it scans selected files including code blocks (`verifiers/verify_alwayson.py:24-29`); date patterns and the scan loop are at `:76-98,265-289`. The pinned counter's six `alwayson.04` cases are at `verifiers/check_alwayson_boxes.py:65-75`; the additional fenced-date and version cases are self-test cases at `verify_alwayson.py:402-415`.

All source mutations and Git writes/commits were confined to `/fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2MutAlwaysOn04`; the only lane write was this assigned report. Each mutant was one committed change to `verifiers/verify_alwayson.py`. For each, the two commands were:

- `python3 -B /fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2MutAlwaysOn04/verifiers/verify_alwayson.py --self-test`
- `python3 -B /fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2MutAlwaysOn04/verifiers/check_alwayson_boxes.py --rev <mutant-or-restoration-rev> --repo /fast/scratch/hyaku/kotoba-r53/w2/KotobaR53.W2MutAlwaysOn04`

Pristine baseline at `c775d6823bfca8f0de8c0874032a954438b38edc`, detector SHA-256 `e4a8b3f230bb5c467798b6cb8bf31b420069d972844315dc4a85f243d9adc890`: self-test exit 0, `0 failure(s) over 89 assertions`; counter exit 0, `always-on boxes executed and discriminating 2 of 8`, with both always-on boxes counted (6/6 each).

## Attack results

1. **Drop ISO-date pattern — HOLDS.** Expected: ISO date fixtures fail. Mutant revision `5e60bab5cfd9cc4c5ade11a5b300624a7779e8f9`; SHA-256 `9d034f983f4c047c1192d977fb130d416fc993c64cdddff739a4a97c960ceea6`. Self-test exit 1: `8 failure(s) over 89 assertions`, including `iso-date`, `iso-timestamp`, `dated-claude-md`, and `fenced-date` (all incorrectly PASS). Counter exit 1: `1 of 8`; `.04` not counted, 3/6 wrong (`iso-date`, `iso-timestamp`, `dated-claude-md`); `.07` counted. Killed by both detectors.

2. **Drop timestamp recognition while retaining bare ISO dates — HOLDS.** Expected: timestamp fixture fails. Mutant revision `c1538f8a7c8ca3d5e6e931a8099f1398a3b452b6`; SHA-256 `2ae18632f49c3b48cd06cd9fd8ee2886897cd74e133a64eeeb4f71abdab449ba`. Self-test exit 1: `4 failure(s) over 89 assertions`, including `iso-timestamp` and `fenced-date` (incorrectly PASS). Counter exit 1: `1 of 8`; `.04` not counted, 1/6 wrong (`iso-timestamp`); `.07` counted. Killed by both.

3. **Drop month-day pattern — HOLDS.** Expected: month-name date fixtures fail. Mutant revision `9952e97b8ce9fdf22740f9d0d559d1a245cea288`; SHA-256 `2c79910a7b178de0b1ba87b1a0f0e21bdf8d6b3307c5016dbca77f933a246fb9`. Self-test exit 1: `4 failure(s) over 89 assertions`, including `month-day` and `abbreviated-month-day` (incorrectly PASS). Counter exit 1: `1 of 8`; `.04` not counted, 1/6 wrong (`month-day`); `.07` counted. Killed by both.

4. **Fenced-code exemption — BREAKS for frozen-counter coverage (low severity).** The baseline date scanner has no fence exemption; its documented behavior scans code blocks. To probe the plausible regression, the mutant skipped fenced blocks in `_dated_hits`. Expected: the fenced-date self-test case fails. Mutant revision `7185b0650084e3851b1694186ed353c2b75d81d5`; SHA-256 `afc2a1525cadf1c96cf872f322d4269a7defd61be793ade648e144bd9adcc231`. Self-test exit 1: `2 failure(s) over 89 assertions`; `fenced-date` incorrectly PASS. Frozen counter exit 0: `2 of 8`, both boxes counted 6/6. Thus the counter survives this mutant; the self-test kills it. Severity: low coverage finding limited to the frozen counter's pinned cases, not a surviving behavior defect in the instrument when its self-test is run.

5. **Treat dotted versions as dates — HOLDS.** Expected: version-number PASS control fails. Mutant revision `0c2daa4534be821e564d9e1a91577f495029fd0a`; SHA-256 `74dc9324bb4bb5675cdaa236aca8fae7ee3bb34fe94e7a53e331429b7b321299`. Self-test exit 1: `4 failure(s) over 89 assertions`, including `version-number` and `dotted-version` (incorrectly FAIL). Counter exit 1: `1 of 8`; `.04` not counted, 1/6 wrong (`version-number`); `.07` counted. Killed by both.

## Restoration evidence

After every mutant, restored `verifiers/verify_alwayson.py` from the exact base revision and tested the restored, locally committed revision. Every restoration had the base SHA-256 `e4a8b3f230bb5c467798b6cb8bf31b420069d972844315dc4a85f243d9adc890`, self-test exit 0 (`0 failure(s) over 89 assertions`), and counter exit 0 (`2 of 8`; both boxes counted 6/6):

- After ISO omission: restoration `b2afd38f090c785b167573c5cd590fcb6630bfee`.
- After timestamp omission: restoration `7f3f484b02222456ba1a1af33b5735de89618049`.
- After month-day omission: restoration `1a82b4b6c7a5eab8686780c44866a3a8f862d62f`.
- After fence-exemption mutant: restoration `c57919e963f8b2306f414ba3e1de56121dd4047e`.
- After version false-positive mutant: restoration `2da299aef65a26564213e115083e04dc23be5146`.

No tools were installed or updated.