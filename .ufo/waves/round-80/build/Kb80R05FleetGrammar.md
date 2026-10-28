# Kb80R05FleetGrammar — fleet grammar precedent for the r80 external-commit class

Seat: Kb80R05FleetGrammar (scout, leaf). Date: 2026-10-27.
Question: does ANY gate under `/home/vgpnk/Projects/shokunin/*/verifiers/` already classify
`owner/repo@<hex>` (or third-repository) commit citations? Is the r80 grammar-class fix novel
ground or a re-derivation of an existing class?

## Verdict (short)

**Re-derivation of a recorded class, novel as a gate mechanism.** No gate anywhere in the
fleet classifies `owner/repo@<hex>` third-repository commit citations by token grammar, and no
gate has a named INFO class for them (no `commit_external` symbol exists in any fleet `.py`).
The CLASS itself — "foreign/external-repository commit citation must not read as
unresolvable-defect" — was named in this lane at round 66 (M102) and was explicitly proposed
for instrument implementation at round 53 (D2, W2CriticDrift.md:117); it was never implemented
in either corpus gate. The nearest fleet mechanisms (kake keyword-line suppression, kama
frozen upstream pin, revenger lane-only resolution) are different mechanisms on different
grammars. E05's fix is the first token-grammar, named-INFO classification.

## Method (all read-only)

1. Lane inventory: `for d in /home/vgpnk/Projects/shokunin/*/; do [ -d "$d/verifiers" ] …` →
   exactly one lane has `verifiers/`: kotoba-shokunin (61 top-level `.py`, `ls verifiers/*.py | wc -l`).
   The seat-prompt's glob grep over `{FLEET}/*/verifiers/*.py` silently matched nothing on the
   first pass (tool glob issue); I redid the sweep directory-scoped — results below stand on the
   directory-scoped greps, not the empty first glob.
2. Grammar sweep, kotoba's 61 verifiers: pattern
   `owner/repo|@<hex>|commit_external|foreign|@hex|third.?repo|external.?commit`
   → hits for "foreign" are all the SKILL.md client-marker guard (`foreign_marker`) and unrelated
   foreign-file/path prose; ZERO hits for `owner/repo`, `@<hex>`, `commit_external`,
   `external commit`, or any third-repository grammar.
3. Fleet-wide `.py` sweep for commit-resolution and external-grammar:
   `grep -rln 'cat-file' {FLEET} --include='*.py'` and
   `grep -rn 'owner/repo|@<hex>|commit_external|third.repo|external.commit|external.repo' …`
   → the only gate-like files outside kotoba are revenger-shokunin/corpus/*.py (12 files),
   kake-shokunin/scripts/citation_lint.py, and kama-shokunin/tools/round54-cited-path-check.py;
   each inspected below.
4. Lane history: M102/M103 (corpus/lessons/round-66.md), Q61 (corpus/QUALITY.md:76),
   round-53 D2 (.ufo/waves/round-53/falsify/W2CriticDrift.md), M45 (corpus/lessons/round-54.md:13,
   round-53.md:43-47), round-54 spot-check and round-55 carried row.

## Evidence — kotoba's own corpus gates (base 398cbe1)

- `verifiers/verify_corpus_integrity.py:23-28` — the published rule: ``commit `<token>```
  citations must be "7-40 hex characters"; `commit_unresolvable` = those where
  `git cat-file -e <hex>^{commit}` fails. No external/third-repository clause.
- `verifiers/verify_corpus_integrity.py:151-153` — token model:
  `COMMIT_RE = (?<![A-Za-z0-9_-])commit[ \t]+`([^`\n]+)`` ; `HEX_RE = \A[0-9a-fA-F]{7,40}\Z`.
  A token `owner/repo@<hex>` cannot match `HEX_RE`, so a backticked `owner/repo@<hex>` token in
  `commit `…`` clothing lands in `commit_nonhash` (line 533-535), not a resolution class; the
  base-`commit_unresolvable=2` arises from the hex portion extracted where the corpus text says
  `commit `<hex>`` and the owner/repo qualifier sits outside the backticks (the r53 lesson's
  exact shape, "at zed-industries/zed@`cfb894a5`" — corpus/lessons/round-53.md:44).
- `verifiers/verify_corpus_integrity.py:600-612` — `commit_resolves`: lane repo first, then
  fleet root. This is the ENTIRE resolution set. A third-repository object is absent from both
  by construction → `commit_unresolvable`. No `owner/repo@` branch exists.
- `verifiers/verify_corpus_independent.py:25-30` — same rule text ("lane repo or declared
  parent fleet root"); `:493-499` same lane→fleet fallback; no external class.
- Zero matches for `commit_external`, `owner/repo`, `third` in either gate — the symbol does
  not exist in any of the 61 verifier files.

## Evidence — the class was named before, and the fix was proposed before

- `corpus/lessons/round-66.md:18` — **M102**: "class: foreign-repository commit misclassified
  as unresolved." Fix taken then: lane-first/fleet-root resolution (the r66 repairs). That fix
  covers bare-hex citations of FLEET objects only; it cannot see a third repository.
- `corpus/lessons/round-66.md:32` — M103: the independent gate's resolver diverged on the same
  repository-context question (Q61 made the resolution-set declaration binding,
  corpus/QUALITY.md:76: "keep an object absent from both unresolved").
- `.ufo/waves/round-53/falsify/W2CriticDrift.md:117` — the round-53 D2 routed defect's
  "smallest safe correction" already read: "classify `cfb894a5` as an external-repository
  commit in the instrument, with a self-test arm, or quote it". The instrument route was NOT
  taken; the lane instead took the "or quote it" evasions:
  - r53: in-place SOURCES edit (M45, corpus/lessons/round-54.md:13;
    corpus/lessons/round-53.md:43-47) rewriting "at commit `cfb894a5`" → "at
    zed-industries/zed@`cfb894a5`" — an append-only breach that only moved the token;
  - r54: `cae8f2ea` reworded the new entry's `` commit `451a02ff` `` to
    `google-gemini/gemini-cli@451a02ff` (corpus/lessons/round-54-verifier-spotcheck.md:146-148);
  - r55: the closure-authored spotcheck token "stays a routed red gate" because the lane never
    edits that file (corpus/lessons/round-55.md:57); the round-54 spot-check's verdict on
    `451a02ff` ("not a defect") was a HUMAN reviewer ruling, not a gate class
    (corpus/lessons/round-54-verifier-spotcheck.md:37).
- `plans/round-80.md:11` and `:24` — the two tokens now block both corpus gates at base
  (`google-gemini/gemini-cli@451a02ff`, `zed-industries/zed@cfb894a5`); repair 5 is the
  external-commit grammar class, counted INFO, per Q61's resolution-set declaration.

## Evidence — nearest fleet neighbors (all different mechanisms)

- `kake-shokunin/scripts/citation_lint.py:45-47,167-168` — the closest existing mechanism:
  `EXTERNAL_RE` suppresses dead-citation violations for tokens on lines naming a FIXED keyword
  list of external repos (`ufo-fsd-alpha|ds4cc-marketplace|plazir|webzites|charter|lucario|…|
  marketplace|upstream|sandbox|fleet repo|spotcheck|render.yaml`), plus a manual adjudication
  ledger (`citation-adjudications.md`, `:48,102-183`). Differences: (a) keyword-on-line
  suppression, not token-grammar detection — a line containing `owner/repo@<hex>` without a
  listed keyword is still flagged; (b) exclusion, not a named INFO classification (suppressed
  tokens vanish from the report; no `commit_external`-style count); (c) no `@`-grammar anywhere.
- `kama-shokunin/tools/round54-cited-path-check.py:529-556` — an "upstream" evidence class that
  REQUIRES raw.githubusercontent URL evidence to equal one frozen `UPSTREAM_OWNER_REPO` +
  `UPSTREAM_COMMIT` pin. Pin-equality for a single known upstream, on URL form, not
  `owner/repo@<hex>` citation tokens; fails closed on any other owner/repo.
- `revenger-shokunin/corpus/self_assessment_check.py` (SM5) and `lint_entry.py:18,93` —
  commit citations must resolve `git cat-file -e <h>^{commit}` in the LANE repo only (no fleet
  fallback); SM5's only escape is an appended erratum line. No external/third-repo class.

## Classification of the r80 fix

- The CLASS (external-repository commit citation ≠ unresolvable defect): **not novel** —
  recorded at M102 (2026-10-24) and proposed as an instrument fix at round 53 (D2). Rounds
  53–55 evaded it by rewording; round 66 fixed only the fleet-object half of it.
- The MECHANISM (token grammar `owner/repo@<hex>` → named INFO class `commit_external`, in
  both corpus gates, with red-before arms): **novel ground** — no gate under the fleet root has
  it, and no fleet gate classifies any third-repository commit citation by token grammar.

## Confidence and remaining unknowns

- Confidence: high for "no existing fleet gate implements the grammar class" (three
  independent sweeps: lane verifiers dir-scoped grep, fleet-wide cat-file py inventory,
  fleet-wide external-grammar grep). Moderate for history completeness — I read the lesson
  rows the seat named plus the r53/r54/r55 chain they cite; deeper .ufo wave archaeology was
  capped per the seat spec.
- Unknown: whether a NON-py gate (shell/awk in scripts/) anywhere implements an equivalent
  class — the sweeps covered `.py` gates and the hyaku scripts dir listing showed no
  citation-classification script; a full shell-grep of every scripts/ dir was out of the
  seat's read cap. Signal: the only commit-citation gates found are the py files above.
- Unknown: whether hyaku `closure-check.py` waves (.ufo/waves/round-12..15) classify third-repo
  commits — they are per-round closure checkers, not standing gates; not read (cap).

Report: .ufo/waves/round-80/w1/Kb80R05FleetGrammar.md
