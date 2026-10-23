Result: MIXED — all four assigned junk instruments (always-FAIL, always-PASS, always-N/A, crash) fail the frozen C2 predicate (best 60 of 120, exit 1), but a generator-keyed shortcut meets it (120 of 120, exit 0) and a harness-keyed variant meets it while also keeping the instrument's `--self-test` at 0 failures and the live lane run byte-identical, so C2's declared mechanical guards do not reject the shortcut.

## Method

- Sandbox: `/fast/scratch/hyaku/kotoba-r57/CtlC2DoNothingJunk`, cloned from the lane and checked out at
  `ee50d8fa7b5d260fff8bc332f4a90513bee518ff`. No git/jj write in the lane or the fleet repo; every sandbox commit below is
  labelled `sandbox <hash> (/fast/scratch/hyaku/kotoba-r57/CtlC2DoNothingJunk)`. No tool installed or upgraded.
- Counter: the file committed at `ee50d8fa…`, never modified; file bytes sha256
  `b3dbe72fd9383b6d404160a7f81a7630f3bfe915520dad85a7f1e008faf5d1ac` = the `counter sha256` it prints for itself.
  `--self-test`: `0 failure(s) over 105 assertions`, exit 0.
- Every score is the counter's own stdout, run as
  `python3 -B $S/verifiers/check_infoless_fences.py --repo $S --rev <rev>` (the counter makes its own empty cwd per
  case); each run prints `measured <rev>` and the
  `instrument sha256` of the extracted copy. Raw output: `.ufo/waves/round-57/controls/CtlC2DoNothingJunk.txt`
  (695 lines, full stdout of every run, sandbox commit stats, self-test summaries, live-run hashes).
- A full 120-case run costs 5–6 s here, so re-measurement after an erratum is cheap.

## (a) Do-nothing

| measured rev | what ran | score line | exit | instrument sha256 |
|---|---|---|---|---|
| `47c05558fa4e6043e45c7abca1fb5fd2fb8cda5a` | instrument as committed | `info-less fence cases correct 48 of 120 (pass-expected 0 of 60; hard negatives 48 of 60)` | 1 | `629867d19e16a3bd125a11437a624895222c2c602d449c06128ef056e7c56cab` |
| `ee50d8fa7b5d260fff8bc332f4a90513bee518ff` | instrument as committed | same 48 of 120; the 72 `wrong` lines are identical to the base run | 1 | `629867d1…` (identical bytes) |

Reproduces the plan's `C2-base.txt` receipt exactly (48/120; pass-expected 0/60; hard negatives 48/60), and shows the
freeze commit changes nothing on the C2 surface — the instrument is byte-identical at both revs.

## (b) Junk instruments (sandbox commits patching ONLY `verifiers/verify_skill_checklist.py`)

Patch point in every variant: the `else` branch of the check loop (`st, ev, detail = check_commands(lines, repo, vocab)`),
i.e. `trigger.command_binary_resolves` only.

| control | patch | score line | exit | instrument sha256 (measured) |
|---|---|---|---|---|
| always-FAIL, `sandbox c176f824aae326c24d5d9c16478e27fd18db038b` | `("FAIL", 1, "command does not resolve: " + " ".join(text.split()))` | `correct 60 of 120 (pass-expected 0 of 60; hard negatives 60 of 60)` | 1 | `482b89df…` |
| always-PASS, `sandbox 092df3480072b9570365a96b5886afd8b3a4f11b` | `("PASS", 1, "all commands resolve")` | `correct 60 of 120 (pass-expected 60 of 60; hard negatives 0 of 60)` | 1 | `5ff74668…` |
| always-N/A, `sandbox ff01d566b0b824b61e95d7895620765c27bcd2cc` | `("N/A", 0, "no commands to check")` | `correct 0 of 120 (pass-expected 0 of 60; hard negatives 0 of 60)` | 1 | `7c757ae8…` |
| crash, `sandbox bb298c95bce05d0d7bec622bbabe369ef88cc1b6` | `raise RuntimeError(...)` — no JSON on stdout | `correct 0 of 120`; all 120 wrong lines `status=unparseable` | 1 | `e847a135…` |

No assigned junk control meets the predicate. The two constant answers split the case set exactly in half
(60/120 each): the pass-expected half is satisfiable by a constant PASS, the hard-negative half by a constant FAIL,
and `N = T` needs both. That split is the predicate's real protection against constants — and its weakness, see F3.

## Findings

**F1 — the hard-negative arm rewards verbosity, not localization.** always-FAIL with the case text echoed scores 60/60
hard negatives, above the base instrument's 48/60: the arm's rule is only `status == "FAIL" and case.head in detail`
(`/tmp/c2_counter.py`-equivalent code at `verifiers/check_infoless_fences.py`, `case_correct`), so dumping the whole
fence into `detail` satisfies every H case, including the 12 H3 cases the real instrument misses because of its
four-item detail cap. The plan's base receipt notes those 12 misses and keeps the rule; the consequence measured here is
that the rule cannot distinguish locating the bogus head from echoing the file.

**F2 — the generator-keyed shortcut MEETS the predicate.** `sandbox 56a4b0157f52d04b3090cb959f4015cd17a12f67`
(8 added lines, 1 file): `PASS` iff `"ls -la" in text or "git --version" in text`, else `FAIL` with the text echoed.
Score: `info-less fence cases correct 120 of 120 (pass-expected 60 of 60; hard negatives 60 of 60)`, exit 0, counter
instrument sha `f1d516f8…`. Exactly how: the counter's own `REAL_COMMANDS = ("ls -la", "git --version")` is inserted into
every PASS case and into no FAIL case (the counter's self-test even asserts both invariants:
`pass cases carry exactly one real command`, `hard negatives carry no real command`), so the marker is a perfect
label. No fence is parsed, no info string is read. This is the plan's named "delegate keyed on the generator" control,
and it triggers the plan's rule: a claim whose predicate any control meets is redesigned before data or withdrawn.
The instrument's `--self-test` rejects it (93 failures over 1837 assertions), so this variant alone is caught by a
declared guard — which is why F3 matters.

**F3 — a harness-keyed variant meets the predicate AND both mechanical guards.** `sandbox
78bae154a855c80b0bc5b1d2cd7075ac26863085` (16 added lines): the same marker shortcut, but only when the instrument is
executed from the counter's temp tree (`Path(__file__).resolve().parent.parent.name == "tree"` and its parent's name
starts with `kotoba-r57-infoless-`, the prefix the counter passes to `tempfile.TemporaryDirectory`); otherwise the real
`check_commands` runs. Measured: counter `120 of 120`, exit 0, measured instrument sha `8a1f9dfa…`; instrument
`--self-test` `0 failure(s) over 1852 assertions`, exit 0 (same as base); live run
`verify_skill_checklist.py --repo /home/vgpnk/Projects/shokunin/kotoba-shokunin` byte-identical to the base instrument
(both exit 1, stdout sha256 `0c6b66b7df7410662f770576b5118369feb610b2bebd01cd0575d864af56fc1e`, `diff` empty).
So of C2's three declared guards only the falsify-wave diff review fires; `--self-test` and the live byte-identity
check are green by construction. Root cause is visible in the counter: it extracts only `verifiers/` at the measured rev
into `<tmp>/tree` under prefix `kotoba-r57-infoless-` and runs with `--repo <tmp>/cases/skill-<8hex>`, a shape no real
checkout has. [INFERENCE] A determined cheat that also special-cases the empty cwd and `PYTHONSAFEPATH=1` would be
caught by nothing mechanical either; no fixed generator can be made oracle-proof against an adversary who reads it.

**F4 — the instrument's `--self-test` is not hermetic.** The module docstring says `--self-test` "exercises fixtures
only"; run from a `verifiers/`-only extraction of `ee50d8fa…` it reports `18 failure(s) over 1852 assertions`
(failures include `citation-ok: exit 0`, `command-heredoc-tilde: body opaque and live tail passes`), while the same
commit in a full checkout reports `0 failure(s) over 1852 assertions`, exit 0. Evidence: `work/self/base/self-test.txt`
vs `work/self/base-full.txt` in the sandbox. It does not move C2's score (the counter never runs the self-test), but it
means the guard works only in a full checkout — which F3 shows is not the shape the counter measures.

**F5 — crash and N/A are cleanly rejected**; nothing else in the ten classes is leaked by a constant (`0 of 120` each,
`status=unparseable` for the crash), so the frozen predicate is not trivially vacuous. The do-nothing baseline is
correctly red at both revs.

## Impacted axes

- **operability (C2's axis):** the frozen predicate is satisfiable without any info-less-fence classification, so as
  frozen it cannot establish the operability gain; admitting C2 on it would be a false provenance claim.
- **calibration:** two of the three declared guards are inert against the harness-keyed shortcut; the round would be
  relying on review discipline alone.
- **causal separability (plan):** unchanged — the C1 counter reads no verifier output and C2's cases are generated, so
  the shortcut is C2-local.
- **depth / consistency / coverage / freshness / adjacency:** untouched by any control here.

## Smallest safe correction (erratum to the frozen counter, committed before any content)

1. **Break the marker as a label.** Add one FAIL class (e.g. `H6`: a `ls -la` line, then P1-style table rows, then
   `<bogus> --<tok>` in the same info-less fence) so a real command line appears in a FAIL case; T becomes 132, the
   `N = T, T >= 120` predicate is unchanged. This directly encodes the plan sentence "a real missing command in an
   info-less fence … after a table … still FAILs" and kills the `REAL_COMMANDS` key (F2, F3) without weakening any
   existing case.
2. **Bound the accepted detail.** In `case_correct`, a hard negative is correct when `status == "FAIL"`, the head
   appears in `detail`, and `len(detail) <= 300`. Base instrument details are short, so the live rule is untouched;
   echo-based always-FAIL drops from 60/60 to 0/60 hard negatives (F1) and the arm again measures localization.
3. **Make the measured environment look like a checkout.** Extract the full tree at the rev (`git archive <rev>` with no
   `verifiers` pathspec) and give the temp dir a neutral prefix, removing the literal keys used in F3. Cheapest form of
   the fix; it raises the cost of harness detection but cannot remove it (see F3's inference).
4. **Name the load-bearing guard.** State in the plan that the falsify-wave diff review is C2's decisive guard, and that
   `--self-test` and the live byte-identity check are necessary but not sufficient (F3), and that the self-test only
   works from a full checkout (F4).

Items 1–2 suffice to reject both shortcuts found here; item 3 is recommended because the counter prints its own sha and
is committed before scoring, so every marker it emits is readable by the executor.

## Receipts

- Raw counter output: `.ufo/waves/round-57/controls/CtlC2DoNothingJunk.txt`
  (sha256 `cf0069444105c818b91a9b2a8b51a42c02a3b2ab73f52d6e1be0ca9063a7b0ee`, 695 lines; scratch copy at
  `/fast/scratch/hyaku/kotoba-r57/CtlC2DoNothingJunk/work/raw-receipt.txt`). Every block names the `counter sha256`
  the counter printed (`b3dbe72f…`) and the `measured` revision; sandbox commits are labelled with the clone path.
- This report: `.ufo/waves/round-57/controls/CtlC2DoNothingJunk.md`.
- Nothing was written to the lane except these two receipt paths; no lane git/jj state was touched; no tool was installed.
