source: S112–S115 (opened round 61; canonical per-client scope-key evidence) + frozen plan `plans/round-61.md` § C1 with errata E2, E2b, E2c (+binding conditions), E2d, E2e, E2f + receipt `.ufo/waves/round-61/receipts/C1-worlds.txt`
verified-at: 2026-10-23 — `python3 -B verifiers/check_scoped_rules.py --self-test` exit 0 (counter sha256 `5a5adc94…`, frozen at `6a7f722e`); world receipt committed at `b4a8d2ee` before any `--fetch` (M90)
recheck: `python3 -B verifiers/check_scoped_rules.py --self-test`; then `python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` and the same command at base `f3246d14`. Record each command's full stdout, `date -u`, and exit code.

# Scoped-rules counter v3: provenance-authenticating arms

The round-60 v2 counter crediting real-looking rows with a wrong key, an invented Action, a
locale/enterprise URL alias, or reused historical snapshot bytes is the recorded ground
(`.ufo/waves/round-60/controls-v2/SUMMARY.md`, `build/ExecKeyForms.md`). Counter v3 replaces
the weakest conjuncts with four arms; every other v2 rule is kept (erratum E1's five re-open
sub-rules included — MutV2Regress).

## Arms (final wording per errata E2–E2f)

- **A1 semantic scope-key (guarded, E2e)** — the row's Scope key must be the one canonical
  key for its client, read from the committed S112–S115 row texts AT THE MEASURED REVISION
  (pinned marker `scope-key[<client>]=<key>`; empty set at base — the predicate's base
  clause, E2d). Guards (MutA1): one key per cell, exact-case membership, path-like value on
  the cited line or its immediate block (quote-aware lookahead — the real Claude row binds
  `paths:` at `memory.md:198` with the glob example at :199), no commented/negated/equals-form
  keys, no example-cell keys. Per client: Claude Code `paths`, VS Code `applyTo`,
  Copilot CLI `applyTo`, Cursor `globs`; no cross-client union.
- **A2 semantic action (guarded, E2f)** — load/event claims must be supported by the committed
  snapshot: every content word on the page, ≥ ceil(2|W|/3) at the cited line, with a RAW
  tokenizer (`content_words` strips backticked spans) and `apply` excluded from the claim
  verbs (MutA2's measured guards G5+G7+G9). Bound, declared before data: listed-but-unwired
  compound-purpose events (MutA2 F6) survive even the full guard.
- **A3 URL canonical (E2 + E2b)** — (a) a declared re-open's URL must have the same `url_key`
  as its base row (the counter's canonicalization: host lowercased, scheme/default-port/www
  normalized, one trailing `.md` dropped — byte-identity was unsatisfiable: r60's own S108
  records `/docs/rules` against S049's `/docs/rules.md`, MutA3); all five E1 sub-rules kept.
  (b) a fresh row whose URL diverges from an existing same-host row only by a locale segment
  or `@version`/`enterprise` suffix is a rendering alias and rejects (MutFixtures seam S1:
  the recorded W2 worlds are fresh rows, so a re-open-only A3 never evaluates them).
  Disclosed limit: 11 canonical-equivalence spellings of the same document remain admitted.
- **A4 snapshot provenance (E2c, six binding conditions)** — (i) recorded sha256 equals the
  committed snapshot bytes; (ii) the located quote occurs (normalised — entity escapes and
  whitespace shaping are documented per Q56, not byte-exact); (iii) the earliest commit
  introducing the blob is no older than the row's opened date — CONSISTENCY ONLY, not
  acquisition authentication (CriticA4Limit demonstrated backdated commits pass); (iv) the
  row's full 64-hex snapshot sha must not already be recorded in the base (`31092dc6`) or
  measured SOURCES table, excluding self, unless the teaches cell declares byte identity via
  an anchored `supersedes S### —` whose named row records that full sha and whose row carries
  no fresh-fetch claim (MutA4's alias matrix and three seams; full-64-hex comparison only —
  8-hex prefixes are never alias evidence). W1's forged row pins `971d75bf…` in full, also
  recorded by base row S043 → A4(iv) rejects; the four eligible rows alias their bases only
  by 8-hex prefix → pass.

## Seven r60 worlds — measured under v3 (`.ufo/waves/round-61/receipts/C1-worlds.txt`)

| World | r60 ground | v2 recorded | v3 measured (arm) |
|---|---|---|---|
| W1 `CtlReopenForged d` | `controls-v2/CtlReopenForged.md` | `--fetch` exit 0 (MET) | reject, arm A4 (sha alias of S043's full pin) |
| W2 `CtlReopenHeldKey b` | `controls-v2/CtlReopenHeldKey.md` | `--fetch` exit 0 (MET) | reject, arm A3 (rendering alias) |
| W3 `CtlReopenHeldKey a` | `controls-v2/CtlReopenHeldKey.md` | exit 1 | reject, arm A1 (not canonical for Cursor) |
| W4 `CtlReopenHeldKey c` | `controls-v2/CtlReopenHeldKey.md` | exit 1 | reject, arm live (redirect guard; E1 sub-rules) |
| W5 wrong scope key | `build/ExecKeyForms.md` | backed end-to-end exit 0 | reject, arm A1 (`patterns` not canonical) |
| W6 invented Action | `build/ExecKeyForms.md` | backed (A2 gap) | reject, arm A2 (claim unsupported at cited line) |
| W7 v1-hollow rescore | `controls/CtlRescoreV2.md` | exit 1 | reject, arm A1 (retained base-URL conjunct family) |

W0 do-nothing rejects with exit 1 (extra arm, not counted). Independent rebuilds by
MutWorldW1/MutWorldW24/MutWorldW5W6 reproduced the v2 recorded results before v3 was
measured; RevControlsV2 reproduced every committed r60 receipt byte-for-byte.

## Entry bound (MutFixtureEscape)

The four arms authenticate cell provenance, NOT row truth: A1 checks key-form occurrence,
A2 support-by-text not entailment, A3 URL identity, A4 sha/quote/first-commit consistency —
no arm tests same-mechanism applicability, own-rule-class truth, current-version behaviour
(MutFixtureEscape's W8 semantic substitution survives all four), or wall-clock fetch time.

## Frozen predicate

`python3 -B verifiers/check_scoped_rules.py --self-test` prints
`worlds reject 7 of 7; eligible rows pass 4 of 4` and exits 0, and
`python3 -B verifiers/check_scoped_rules.py --rev <tip> --fetch` exits 0 while the same
command at base `f3246d14` exits 1.

## Not held

- The counter does not prove the semantic truth of rows; reviewers re-read the cells (W8 class).
- A4(iii) is committed-byte + recorded-date consistency; author-forged commit dates pass it.
- A2's F6 bound and A3's 11 admitted spellings are disclosed limits, not oversights.
- The v2 exploratory ruling (r60 erratum E2) is unchanged: this is the redesign, not a
  re-measurement of r60's exploratory claim (RevE2Boundary).
