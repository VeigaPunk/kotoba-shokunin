# ExecC1Eval — round-85 w1 report (C1 trigger eval set candidate)

Item: author the C1 trigger eval set candidate + R6 mirror checker under
`.ufo/waves/round-85/w1/ExecC1Eval/`, against the candidate description bytes frozen in
`plans/round-85.md` § C1. Status: **done, mirror checker exit 0, non-vacuity control exit 1 as
designed.**

## Files written (all under my wave dir)
- `description-eval-round85.tsv` — header `label<TAB>query`; 9 `should-trigger` + 9
  `should-not-trigger` rows, LF, no trailing blanks.
- `mirror_check.py` — R6 mirror checker, stdlib only, 105 lines, exit ladder 0/1/2, honours
  `TMPDIR` implicitly (no writes; reads only its two inputs), `--tsv`/`--description` overridable.
- `candidate-description.txt` — the exact frozen payload bytes (see provenance below); the checker
  reads the declared trigger terms and token field from this file instead of hardcoding them.
- `receipt.txt` — pasted pass-run output, negative control, provenance.

## Method
- Description bytes extracted programmatically via `git show
  f822dd113fe9f58661dd642dc207669581a4ab57:plans/round-85.md` line 77 (§ C1 payload) — never
  retyped. Verified: 876 parsed chars (matches the plan's stated 876), sha256
  `824cbacc8ad5f1e494c1ee262818dd8954eeba432e02135a9da27d2a76b981a3`, no `<`/`>`; plan unchanged
  freeze..HEAD and the worktree line is byte-identical to the freeze line.
- Positives (9): 4 direct rows carry declared terms (`audit this skill`; `SKILL.md` +
  `frontmatter description`; `skill file`; `write a skill` + `trigger words`); 5 indirect rows
  contain **none** of the 8 declared phrases — agent-ignores-packaged-instructions complaints,
  a "my skill never fires unless verbatim" complaint, a steering-doc wording mismatch, an
  assistant-ignores-my-steering-file question (floor is ≥ 5).
- Negatives (9): every row shares ≥ 1 lowercased alphanumeric token of ≥ 4 chars with the parsed
  description and needs a *different* skill — model-output prompt polish (prompt/model/outputs),
  runtime code refactor (runtime/code), fictional-worlds lore (fictional/worlds/language/naming),
  web page content + publish (content), host package + initramfs hook (host/package/initramfs),
  mutation fixture repair (fixture/mutation → tameshi), endpoint verification (endpoint/verification
  → kama), research method design (research/method → chousa), kagi source collection (kagi).
  No throwaway rows ("weather" class) included.
- Mirror checker applies exactly the plan's R6 conditions: exact header; 8–10 per label; ≥ 5
  indirect positives (case-insensitive phrase containment of the declared terms); every negative
  shares ≥ 1 `[a-z0-9]{4,}` token with the parsed description; prints counts, indirect count and
  per-negative shared tokens.

## Evidence (observed, full text in receipt.txt)
- `python3 -B …/mirror_check.py` → `rows: should-trigger=9 should-not-trigger=9`,
  `indirect positives …: 5 (need >= 5)`, `near-miss negatives …: 9/9`,
  `OK R6 eval_set_shape: header exact, row counts in range, indirect floor met, all negatives
  near-miss`, exit 0.
- Negative control (scratch copy, lane TSV untouched): a negative row rewritten to share no ≥4-char
  token → `FAIL R6 eval_set_shape / line 15: negative row shares no token >= 4 chars`, exit 1 —
  the checker is not vacuous.
- No tools installed or upgraded (none needed); no pacman use; scratch
  `/fast/scratch/hyaku/kotoba-r85/ExecC1Eval/` created, used as TMPDIR, removed before this report.

## Risks / handoff notes
- The frozen counter's R6 reads `verifiers/fixtures/description-eval-round85.tsv` (ExecC1Counter's
  file). My candidate lives in my wave dir; the counter owner or the L1 must copy it there
  (byte-identical) for the after-value measurement. Copying is out of my ownership.
- R6's indirect test is phrase containment of the declared terms, as the plan words it. A stricter
  future wording (banning standalone tokens `skill`/`trigger`/`prompt` in indirect rows) would
  still leave lines 6, 7, 9, 10 indirect (they contain none of those tokens); only line 8
  ("My skill never fires…") carries the standalone token `skill`. Flagging so the counter owner
  picks the containment level deliberately.
- Negative line 11 additionally shares the generic token `this` (len 4); its meaningful shares are
  `prompt`/`model`/`outputs`. Mechanical condition holds regardless.
- The candidate set is authored against the payload's declared terms; if the L1 changes the payload
  bytes before integration, rerun the checker (`--description` override) — terms and token field
  re-derive automatically; only a term-list change could flip direct/indirect classification.
