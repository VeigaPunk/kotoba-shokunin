source: S112–S115 (per-client scope-key evidence), S117 (writing-time calibration), and S118 (Claude Code memory docs, § Rule frontmatter reference at `memory.md:250`); r61 counter arms/bounds: `corpus/knowledge/scoped-rules-counter-round61.md`
verified-at: 2026-10-23 — `python3 -B verifiers/check_erratum_absorption.py --self-test`; pinned counter sha256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`
recheck: `python3 -B verifiers/check_erratum_absorption.py --self-test`

# Round-62 C1: erratum absorption map

`[]` is ACCEPT; a non-empty reason list is REJECT. Absorbed means both frozen instances reject under the pinned r61 counter and become accepted when only that erratum's guard is disabled. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.

## Matrix

- **E2 — A3(a), `url_key` / `reopen_why`.** Class: these re-open instances target a URL normalizer that must distinguish the base document from an unrelated document. Instances: `e2-url-unrelated-path`, `e2-url-different-document`. Both REJECT; disabling `url_key` changes both to ACCEPT. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.
- **E2b — A3(b), `render_form` / `alias_why`.** Class: these fresh-row instances target locale/version URL renderings that alias an existing same-host document. Instances: `e2b-locale-rendering`, `e2b-version-rendering`. Both REJECT; disabling `render_form` changes both to ACCEPT. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.
- **E2c — A4(iv), `alias_sha_why`.** Class: these snapshot-alias instances target a `supersedes` declaration that must bind its named row to the full SHA and exclude a fresh-fetch claim. Instances: `e2c-wrong-supersedes-target`, `e2c-supersedes-with-fresh-fetch`. Both SURVIVE (`[]`); disabling `alias_sha_why` leaves both accepted. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.
- **E2e — A1, `a1_conjunct` + `scope_conjunct` (`path_site` / `path_value`).** Class: these scope-key instances target negated or commented path-key forms that the guarded key check should reject. Instances: `e2e-negated-path-key`, `e2e-commented-equals-key`. Both SURVIVE (`[]`); the admitting stubs for `a1_conjunct` and `path_value` cause no verdict change. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.
- **E2f — A2, `action_conjunct`.** Class: these action instances target a backticked event claim and a compound-purpose claim outside the cited line. Instances: `e2f-backticked-event-claim`, `e2f-compound-purpose-outside-citation`. Both SURVIVE (`[]`); disabling `action_conjunct` causes no verdict change. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.

Guard flips — `python3 -B verifiers/check_erratum_absorption.py --self-test`:
`guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0`

Aggregate — `python3 -B verifiers/check_erratum_absorption.py --self-test`:
`errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`

Survivors — `python3 -B verifiers/check_erratum_absorption.py --self-test`:
- `survivor E2c e2c-wrong-supersedes-target: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`
- `survivor E2c e2c-supersedes-with-fresh-fetch: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`
- `survivor E2e e2e-negated-path-key: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`
- `survivor E2e e2e-commented-equals-key: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`
- `survivor E2f e2f-backticked-event-claim: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`
- `survivor E2f e2f-compound-purpose-outside-citation: []` — `python3 -B verifiers/check_erratum_absorption.py --self-test`

The matrix's mutation sweeps left off-diagonal class verdicts unchanged. The content-variant arm changed only E2's URL input and changed its verdict. These are results for the frozen matrix, not universal guarantees about other instances. Matrix: `python3 -B verifiers/check_erratum_absorption.py --self-test`.

## E2f gap and successor

The pinned A2 `action_conjunct` checks text-support fractions but has no G7 raw-tokenizer event-claim conjunct; `content_words` strips backticked spans. It also lacks G9's compound-purpose conjunct. The lane's v3.1 successor (`verifiers/check_scoped_rules_v31.py`, sha256 `a07c2269…`; the frozen counter stays byte-identical) adds a G7 raw-evidence check for backticked identifiers and the E2c/E2e guards, and retains G9/F6 as a declared bound. Measured (`python3 -B verifiers/check_scoped_rules_v31.py --self-test`, exit 0, `.ufo/waves/round-62/C1-v31-successor.txt`): `worlds reject 7 of 7; eligible rows pass 4 of 4` unchanged, then five `before accepted; after rejected` survivor lines, `survivors closed 5 of 6`, both must-fail arms (`yes`), `self-test: 0 failure(s) over 201 assertions`. The sixth survivor, `e2f-compound-purpose-outside-citation`, remains a named surviving bound (G9).

## Declared bounds

- **F6 / G9:** compound-purpose claims remain outside the successor's frozen guard; the named E2f compound-purpose instance remains a declared bound.
- **E2:** A3's canonicalization still admits its disclosed canonical-equivalence URL spellings; this arm-level matrix does not remeasure that limit.
- **A4(iii):** earliest-commit versus recorded-opened-date consistency only, not acquisition authentication.

S118's snapshot line `.ufo/waves/round-62/snapshots/S118.page:250` says (raw bytes, link markup included): “Glob patterns that [scope the rule to matching files](#path-specific-rules)”. The bracketed link target is part of the cited line; the quote is not link-stripped. The S118 fetch record lives in `corpus/lessons/round-62.md` § Gate. This source supports the `paths` form used in E2e; it is not a runtime measurement.

## Limits

- The matrix is arm-level; it does not re-run the seven worlds or measure their semantics. The separate r61 world check is `python3 -B verifiers/check_scoped_rules.py --self-test`.
- It does not decide whether source prose entails an Action claim; that remains reviewer judgment per Q31.
- It checks the counter bytes against the embedded SHA-256 pin, but does not independently establish the pin's historical authority.
- It performs no network fetch and does not measure source freshness or current availability.
- The printed headline is not parsed back from the public path by any committed executable; a hardcoded line above the computed survivor rows exits 0 (`FalsifyMatrixMutants`, m3). The receipt's survivor rows are the cross-check.
- The counter pin is hash-then-import, not atomic: a writer racing between the hash and the import can spoof `self_sha()` (`FalsifyPin`, medium).
- The acceptance layer is shape-only: `measured 5 of 5` is the length of the hard-coded erratum table, K/N never gate the exit, and a forged `MatrixRun` reproduces the receipt line; kill-rule (iii)'s own-mutation flip is not asserted (`FalsifyClaimC1`, `FalsifyMatrixAsserted`). The committed datum is unaffected (the public path builds the run with the real scorer).
- The before-state is narrowed: 2 of 5 classes already had one committed synthetic arm-level reject (E2b W2, E2c W1), 0 of 5 had the attack tables re-scored with both directions (`FalsifyBeforeState`).
- The v3.1 successor's closure is bounded: E2c's binding conditions are narrower than the two frozen instances, and G7 both misses one published event form and over-rejects an expanded token (`FalsifyE2cClass`, `FalsifyE2fPair`, `FalsifyV31G7TooStrong`).
