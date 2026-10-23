# ScribeEntry62 — round 62 C1 findings

## Behavior and evidence scope

This seat drafted the full C1 knowledge entry below for `corpus/knowledge/erratum-absorption-round62.md`. It did not write that product file. My only write is this report; no counter, verifier, fixture, source row, fleet, sibling, `.ufo/state`, or jj/Git-index file was changed. I did not run a build, test, lint, formatter, judge, source fetch, Git, or jj command, and installed no tools.

The measured matrix and arm probes below are transcribed from the named wave-one seat reports. The matrix runner itself was a scratch draft; its audited counter input was pinned to the committed r61 bytes. Scratch is not cited as an evidence artifact. The entry marks the unmeasured successor run and the not-yet-integrated S118 registry row explicitly.

## Draft for `corpus/knowledge/erratum-absorption-round62.md`

```markdown
source: S118 (Claude Code Docs, re-opens S103 at the same URL; used here only for `paths` frontmatter at `memory.md:250`) + S112–S115 and `corpus/knowledge/scoped-rules-counter-round61.md` (r61 per-client keys, arms, and declared bounds)
verified-at: 2026-10-23 — arm-level matrix run against `verifiers/check_scoped_rules.py` sha256 `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`; matrix runner was a scratch draft, not yet landed in the lane
recheck: after integration, `python3 -B verifiers/check_erratum_absorption.py --self-test`; separate fix-evidence command, not a C1 predicate: `python3 -B verifiers/check_scoped_rules_v31.py --self-test` (not measured here)

# Erratum absorption against the landed scoped-rules counter

`[]` is ACCEPT; a non-empty reason list is REJECT. Absorbed means both frozen instances reject under the pinned counter and both become accepted with only that erratum's guard disabled.

| r61 erratum | Landed arm | Two fresh instances | Measured counter verdict | Guard-disabled direction | Absorbed? |
|---|---|---|---|---|---|
| E2 | A3(a): `url_key` / `reopen_why` | `e2-url-unrelated-path` (`https://h.example/b` against base `https://h.example/a.md`); `e2-url-different-document` (`https://h.example/c` against the same base) | both REJECT | `url_key = lambda url: "//x" if url else ""`; 2 own-class flips; other erratum-class verdicts unchanged | yes |
| E2b | A3(b): `render_form` / `alias_why` | `e2b-locale-rendering` (`https://h.example/de/a`); `e2b-version-rendering` (`https://h.example/v@1/a`), each against `https://h.example/a` | both REJECT | `render_form = lambda url: ("", "", False)`; 2 own-class flips; other erratum-class verdicts unchanged | yes |
| E2c | A4(iv): `alias_sha_why` | `e2c-wrong-supersedes-target` (the digest maps to S043; teaches names S096); `e2c-supersedes-with-fresh-fetch` (anchored `supersedes S048 —` with a fetched assertion) | both ACCEPT (`[]`); both print as survivors | `alias_sha_why = lambda *args, **kwargs: []`; 0 flips because both already accept | no |
| E2e | A1: `a1_conjunct` + `scope_conjunct` (`path_site` / `path_value`) | `e2e-negated-path-key` (`Do not use paths: src/legacy/**/*.ts`); `e2e-commented-equals-key` (`# paths=src/legacy/**/*.ts`) | both ACCEPT (`[]`); both print as survivors | admitting stubs for `a1_conjunct` and `path_value`; 0 flips because both already accept | no |
| E2f | A2: `action_conjunct` | `e2f-backticked-event-claim` (backticked `InstructionsLoaded` event claim); `e2f-compound-purpose-outside-citation` (adds “secretly uploads files” outside the cited line) | both ACCEPT (`[]`); both print as survivors | `action_conjunct = lambda *args, **kwargs: []`; 0 flips because both already accept | no |

The arm-level matrix printed:

```text
counter sha256 5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91
instances per direction: committed attacks 10; guard-disabled 10 per sweep (50 total); controls 4 committed + 4 disabled; content variant 2
guard flips: E2 2; E2b 2; E2c 0; E2e 0; E2f 0
errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2
survivor E2c e2c-wrong-supersedes-target: []
survivor E2c e2c-supersedes-with-fresh-fetch: []
survivor E2e e2e-negated-path-key: []
survivor E2e e2e-commented-equals-key: []
survivor E2f e2f-backticked-event-claim: []
survivor E2f e2f-compound-purpose-outside-citation: []
EXIT_CODE=0
```

The exit 0 is the matrix self-test result for its five measured classes and two seeded controls; it does not mean all five errata were absorbed. The result is computed from the arm calls. The disabled direction is vacuous for E2c, E2e, and E2f because both instances in each class already pass; their zero flips are not mutation kills.

S118 is a same-URL re-open of S103, not a new general rule authority. The only additional proposition used here is the `paths` frontmatter row at `memory.md:250`: “Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string”. This supports the specific `paths` form used in E2e and no broader novelty claim.

## E2f G7/G9 gap and successor

The r61 E2f A2 row requires text support for load/event claims; the measured `action_conjunct` accepts the backticked-event instance because `content_words` strips backticked spans, and it accepts the compound-purpose instance. The landed arm has neither the raw-tokenizer event-claim conjunct (G7) nor the compound-purpose conjunct (G9). The separate r62 v3.1 successor is fix evidence, not a replacement C1 claim predicate. Its planned form adds G5 key-on-line plus G7 and keeps G9/F6 as a declared bound. **Unmeasured:** no `check_scoped_rules_v31.py` file or self-test output was available to this report; the planned `E2f fresh instances reject 2 of 2` line is not claimed.

## Declared bounds

- F6: listed-but-unwired compound-purpose events remain a declared bound; the matrix's compound-purpose instance is accepted.
- E2: 11 canonical-equivalence spellings remain admitted; A3 uses `url_key`, not byte identity.
- A4(iii): committed-byte / recorded-date consistency only, not acquisition-time authentication.

## Limits

- The matrix is arm-level; it does not re-run the seven world-level `--fetch` cases or measure their semantics.
- It does not decide whether a vendor sentence entails an Action claim; that remains reviewer judgment per Q31.
- It compares the loaded counter with the embedded SHA-256 pin; it does not independently establish the historical authority of that pin. The r61 freeze receipt remains the pin provenance.
```

## Measurements, source footing, and gates

### C1 matrix and frozen counter

Transcribed from `.ufo/waves/round-62/w1/ExecAbsorbInstrument.md`; the named lane verifier was not written by that seat. The draft runner and its source are in scratch only.

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ'; sha256sum /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
```

Output at `2026-10-23T21:00:26Z`; exit 0:

```text
2026-10-23T21:00:26Z
5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91  /home/vgpnk/Projects/shokunin/kotoba-shokunin/verifiers/check_scoped_rules.py
```

```sh
date -u '+%Y-%m-%dT%H:%M:%SZ' && python3 -B /fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecAbsorbInstrument/verifiers/check_erratum_absorption.py --self-test
```

Output at `2026-10-23T20:59:31Z`; exit 0. Pasted output is reproduced in the draft block above. The instrument source target `verifiers/check_erratum_absorption.py` was not created in the lane; this is a pre-integration scratch-draft measurement, not a committed verifier run.

The separate frozen no-harm output in `.ufo/waves/round-62/w1/ExecControls.md` records `python3 -B verifiers/check_scoped_rules.py --self-test` at `Fri 23 Oct 2026 08:52:40 PM UTC`: `worlds reject 7 of 7; eligible rows pass 4 of 4`; `self-test: 0 failure(s) over 189 assertions`; `EXIT=0`. This is the unchanged r61 world predicate, not the absorption result.

### Source footing

- `SrcRulesFrontmatter.md` records the first S118 fetch at `2026-10-23T20:49:56Z`, HTTP 200, 55,354 bytes, SHA-256 `02632438e022b5fc70b470b02d59819d9739756c2666b5632734b4564a08a801`; `RevS118.md` records the independent fetch at `2026-10-23T20:54:38Z` with identical bytes and digest. The snapshot `.ufo/waves/round-62/snapshots/S118.page` was read at line 250 and printed exactly:

  ```text
  | `paths` | No | Glob patterns that [scope the rule to matching files](#path-specific-rules). Accepts a YAML list or a comma-separated string |
  ```

- The S118 registry row is still a draft in `ScribeSourcesS118.md`; a scoped search of `corpus/SOURCES.md` found no S118 row at this report's inspection. The draft correctly uses `re-opens S103 —`; do not describe S118 as a new URL or a broader source claim.
- R61 arm and bound references are in `corpus/knowledge/scoped-rules-counter-round61.md` §§ Arms, A4 limit, and Not held, and the corresponding r61 SOURCES rows S112–S115.

### Guard/API probes transcribed from wave reports

The following corroborating outputs are from `ScoutCounterApi.md`, `ExecInstancesA1.md`, `ExecInstancesA2.md`, and `ExecInstancesA4.md`; they are peer-run probes, not commands run by this scribe.

`ScoutCounterApi.md` reports `date -u` `Fri 23 Oct 2026 08:52:10 PM UTC`; probe exit 0; counter file/self hash matched `5a5adc945e58ec18ba48a4929af9a1475eb7c186a757ee1a10008ca3c1b52b91`. Its E2e outputs include:

```text
path_site(["globs=a/*/b"], 1, "globs") | True
path_site(["# globs: a/*/b"], 1, "globs") | True
```

Thus the reported path-site helper also accepts equals-form and commented-key probes. These are supplemental API probes, not additional members of the matrix's ten frozen instances.

`ExecInstancesA4.md` records `date -u` `Fri 23 Oct 2026 08:52:06 PM UTC`; `python3 -B /fast/scratch/hyaku/kotoba-r62/KotobaR62.ExecInstancesA4/a4_instances.py` exit 0. The relevant output is:

```text
alias_sha_why=['A4: snapshot sha256 971d75bfce7a... is already recorded by base row S043 and the teaches cell declares no supersedes']
reject_condition5_wrong_named_prefix_row:
  alias_sha_why=[]
condition6_expected = REJECT; reason contains 'fresh-fetch claim'
condition6_alias_sha_why (teaches-only API) = []
```

This matches the matrix's E2c survivors: the anchored `supersedes` prefix does not bind the named row to its full SHA (condition 5) or inspect the other row cells for a fresh-fetch claim (condition 6).

`ExecInstancesA2.md` records `date -u` `Fri 23 Oct 2026 08:53:38 PM UTC`; probe exit 0. The backticked-event case printed `content_words=['claude', 'event', 'files', 'loads', 'matching', 'patterns', 'rules', 'specific', 'specified', 'works']`, `forward=8/10 need=7; reverse=8/15 need=5`, `verdict=ACCEPTED; reasons=[]`; `InstructionsLoaded` is absent from the content-word list. Its `F6-compound-purpose-bound` case printed `forward=6/9 need=6; reverse=7/14 need=5`, `verdict=ACCEPTED; reasons=[]`.

`ExecInstancesA1.md` separately records the `Do not use paths: src/legacy/**/*.ts` probe as `combined_reasons=[]`, `actual_verdict=ACCEPT`, `python_exit=0` at `2026-10-23T20:52:03Z`. The matrix uses its own frozen E2e instances named in the table above.

## Plan conflict for the canonical judge

The frozen plan contains both of these incompatible expected-result strings; they are transcribed verbatim:

- `errata measured 5 of 5; absorbed 4 of 5; surviving 2; controls 2 of 2`
- `E2f unabsorbed with its event-claim instance surviving: absorbed 4 of 5; surviving 1`

The measured matrix output is `errata measured 5 of 5; absorbed 2 of 5; surviving 6; controls 2 of 2`. Do not substitute either frozen expectation for the computed output.

## Touched surfaces, out-of-scope items, and status

- **Touched:** only `.ufo/waves/round-62/w1/ScribeEntry62.md`; the full product-entry draft is fenced above at its exact target path.
- **Out of scope:** writing/integrating the knowledge entry, source row, C1 verifier, or successor; C2 routed-repairs; Git/jj mutation; wave-two falsification; builds/tests/linters/formatters; canonical judge.
- **Findings:** E2 and E2b are absorbed; E2c, E2e, and E2f are not. The computed matrix output has six accepted instances. The S118 line grounds only the narrow `paths` proposition. The successor self-test remains unmeasured here.
- **Artifacts:** `.ufo/waves/round-62/w1/ExecAbsorbInstrument.md`; `ExecInstancesA1.md`–`ExecInstancesA4.md`; `ScoutCounterApi.md`; `SrcRulesFrontmatter.md`; `ScribeSourcesS118.md`; `RevS118.md`; `corpus/knowledge/scoped-rules-counter-round61.md`; `.ufo/waves/round-62/snapshots/S118.page:250`.

Installs: no installs.
Blockers: none to this scoped report; the successor self-test and committed S118 registry row are explicitly unclaimed.
Produced: the full C1 erratum-absorption entry draft with the measured two-absorbed/six-surviving matrix and its limits.
Report: .ufo/waves/round-62/w1/ScribeEntry62.md
