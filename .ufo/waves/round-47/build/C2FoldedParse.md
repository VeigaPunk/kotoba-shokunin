# C2 folded-frontmatter parse — what the existing parser actually yields

verdict: For `description: >` the existing parser is byte-equivalent to strict YAML on every
fleet file that strict YAML can parse at all (11/21), differing only by YAML's one trailing
newline (814 vs 815 chars for this file); a tag split across a fold is joined with a **space** in
both models, so `<skills>` is visible to a C2 check exactly when it is contiguous in source — and
a naive tag regex over the parsed value has three named false-positive classes a check must close.

All line numbers are at BASE `c61a973b2e02e1ded169703ddcb06466f4edd8bd` (working tree verified
identical: `git rev-parse HEAD` → `c61a973…`; only untracked `.ufo/waves/` and `plans/round-47.md`).

## 1. What `parse_frontmatter` yields for `SKILL.md:3-15`

`verifiers/verify_skill_checklist.py:472` `parse_frontmatter` returns `(fields, problem)`; the
`description` field is a single string:

* **Length / chomping.** `len(fields["description"].strip())` = **814**; the raw value carries no
  trailing newline. `yaml.safe_load` of the same frontmatter (PyYAML 6.0.3) yields the same 814
  characters **plus one `"\n"`** (clip chomping of `>`), i.e. 815. `difflib` shows **zero** changed
  lines — only the final newline. `check_frontmatter` (`:1176`) prints the 814 via `.strip()`
  (`:1189-1191`), as do `check_literal_trigger` (`:1216`) and `check_anti_trigger` (`:1234`), so the
  chomping difference never reaches a verdict. No test or verifier pins `814` (grep: no hits).
* **Folding.** Every continuation line is `line.strip()`ed and appended as `" " + stripped`
  (`:513`). So: exactly one ASCII space per fold, all leading indentation removed (including
  "more-indented" lines that YAML keeps literal), and no newline can ever survive in any value.
* **Blank lines.** `:503` skips them outright. `` `>` `` paragraph breaks are therefore **lost**:
  `alpha beta` / blank / `gamma delta` parses as `alpha beta gamma delta`, where YAML gives
  `alpha beta\ngamma delta\n`.
* **`>` vs `|`.** Identical to this parser: all six indicators are recognized at `:531`, the value
  is reset to `""`, and continuation lines are space-joined. So a literal block's line structure is
  destroyed too (`|-\n alpha\n beta` → `alpha beta`; YAML → `alpha\nbeta`). `>-` is the one
  indicator that matches YAML exactly (no trailing newline).
* **Comments.** `#` has no meaning inside the value (`alpha # see <skills> here` is kept verbatim,
  unlike YAML which yields `alpha`). But a **column-0** `#` comment line inside the frontmatter is
  fatal: `FM_KEY_RE` (`:306`, `^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$`) does not match, `:521`
  records `"unparseable frontmatter line …"`, and `:544` returns `(None, …)` — the whole file
  FAILs `trigger.frontmatter_parses` on legal YAML. Indented `#` inside a block scalar is kept by
  both models (YAML does not treat it as a comment inside a block scalar either).
* **Quotes.** A value whose first and last characters are the same quote has them stripped
  (`:547-549`). A *multi-line* quoted scalar is rejected immediately as
  `"unbalanced quote in scalar …"` (`:535-540`). Side effect measured: a quoted literal `'~'`
  becomes `""` and is then normalized away by `EMPTY_SCALARS` (`:350`) — a description of `~`
  counts as absent, while YAML yields the string `"~"`.
* **Duplicate keys** are a problem (`:528-529`) → whole frontmatter `None`; PyYAML silently takes
  the last value. `tab` indents and stray indents likewise fail (`:506-512`).
* **Nested maps** (`metadata:`) are not parsed: their sub-lines are folded into the parent's string
  value. Irrelevant to a `description`-scoped check.

## 2. Will a tag split across a line fold be seen joined? No.

Measured, parser value vs `yaml.safe_load` value (probe3, exit 0):

| source shape | parser value | YAML value |
|---|---|---|
| `` `<skills>` `` contiguous | `` …`<skills>`… `` | identical + `\n` |
| `<ski` ⏎ `lls>` (folded) | `<ski lls>` | `<ski lls>` |
| `<ski` ⏎ blank ⏎ `lls>` | `<ski lls>` | `<ski\nlls>` |
| `<ski` ⏎ `lls>` inside `\|` | `<ski lls>` | `<ski\nlls>` |
| `<skills` ⏎ `    >` (more-indented) | `<skills >` | `<skills\n  >` |
| `"<ski\` ⏎ `lls>"` (YAML escaped newline) | **parser rejects file** | `<skills>` (contiguous!) |
| `\<` ⏎ `skills>` | `< skills>` | `< skills>` |

Consequence: the fold always inserts a space, so **no fold can synthesize character contiguity**
and a check over the parsed value cannot invent a tag from a line-broken one. The two exceptions
are both named: (a) the parser *does* synthesize a syntactically valid `<skills >` from
`<skills` + a more-indented `>` — conservative, and arguably correct to flag, but it means a
"contiguous in source" claim cannot be made from the parsed value; (b) YAML's escaped-newline
double-quoted scalar creates a real contiguous `<skills>` that this parser can never see — but that
file is already a hard FAIL (`unbalanced quote`), so the two verdicts agree.

## 3. Divergences a C2 check must account for

1. **Never use PyYAML as the oracle in the instrument** (`:251` pins "stdlib only"). Measured on the
   fleet: **10 of 21** `SKILL.md` frontmatters raise `ScannerError: mapping values are not allowed
   here` under PyYAML 6.0.3 — each at a `: ` inside a plain-scalar description (8× `Rank: shonen`,
   plus `Trigger strings:` in `game-dev-3d-shokunin` and `Anti-trigger:` in `kaidoku-shokunin`;
   e.g. `kagi-shokunin/SKILL.md:3` errors at column 125). The structural
   parser accepts all of them (`problem: ''`). A YAML-based tag check would silently skip ~half the
   fleet; S008 names exactly this hazard.
2. **Scan the folded value, do not strip backticks.** The live `<skills>` sits inside a backtick
   span. Reusing `ALL_QUOTED_SPANS_RE`/`BACKTICK_SPAN_RE` (as `check_anti_trigger` does at `:1237`)
   before matching tags makes the check **vacuous on the very defect it exists to catch**.
3. **Trailing comments** are part of the parser's value: `alpha # see <skills> here` would be
   flagged where YAML sees `alpha`. No fleet file has one; name it as a ceiling rather than handle it.
4. **Column-0 YAML comments** make `fields is None`; the check must return `FAIL, 0, "cannot
   evaluate: …"` (consistent with `check_literal_trigger:1216`), never `N/A` — the module docstring
   (`:43-46`) makes description a must-exist subject.
5. **Loss of paragraph/line structure** (`>` and `|` collapse) means the check cannot report a
   line/column of the raw file — only an offset into the folded value (`<skills>` at offset 750 in
   the current description). Do not print a raw line number; it would be wrong.
6. **Duplicate keys / tabs / multi-line quotes** already short-circuit at `fields is None`, so the
   tag rule inherits those verdicts; do not re-parse with YAML to "recover" them.

## 4. Recommended check shape (measured)

Name-anchored and attribute-`=`-strict, over `fields["description"]`, nothing stripped:

```
DESCRIPTION_TAG_RE = re.compile(
    r"</?[A-Za-z_][-A-Za-z0-9_.:]*"
    r"(?:\s+[A-Za-z_:][-A-Za-z0-9_:.]*\s*=\s*"
    r"(?:\"[^\"]*\"|'[^']*'|[^\s\"'=<>`]+))*\s*/?>")
```

Measured accepts: `<skills>`, `</skills>`, `<skills/>`, `<skills >`, `<skills a="b">`,
`<skills limit=3>`, `<SKILLS>`, `<skills\n  >`. Measured rejects: `<ski lls>`, `<b and y >`,
`<5 and profit >`, `< skills>`, `<!-- c -->`, `<?xml v?>`. The obvious looser variant
`<[^<>]{1,60}>` **fails** on prose: `cost < 5 and profit > 3` matches `< 5 and profit >`; a
valueless-attribute variant matched `<b and y >`. Both rejections matter because descriptions
are prose.

## 5. Two integration routes, both measured

* **A — separate check id** (`trigger.description_no_xml_tag`, inserted in `CHECK_IDS:282`).
  Self-test `CASES:1676` asserts `PASS <cid>` for every id not listed in `fails` (`:1839`) and
  rejects `evaluated 0` on a PASS line (`:1856`); the id is `FAIL, 0` whenever `fields is None`,
  so it must be added to the `fails` list of **7** rows — `no-frontmatter`, `fm-null`,
  `fm-malformed`, `fm-dup-key`, `fm-body-yaml`, `fm-stray-indent`, `empty-file`. With those edits
  plus 3 fixtures: `--self-test` → `0 failure(s) over 1735 assertions`, exit 0 (baseline 1597).
  Live file: `FAIL … description carries XML tag '<skills>' at offset 750`, exit 1.
* **B — fold into `check_frontmatter`**: `evaluated = 4` (`:1178`) → 5, docstring pins at `:75`
  and `:44`; no case-table edit needed, `--self-test` stays `0 failure(s) over 1597 assertions`,
  exit 0; live `FAIL trigger.frontmatter_parses: evaluated 5 — description carries XML tag
  '<skills>'`. Cost: the detail line loses `name=…, description N chars` and the offset.
  Recommend A (legible, offset-bearing, and usable as a map `executed:` target — `box_map_complete`
  validates that every `executed:<id>` names a check at `:1084`).

Prototype (route A, tightened regex, 3 fixtures) saved as
`.ufo/waves/round-47/build/C2FoldedParse.prototype.patch` — advisory draft, not a production edit.
Fixture discrimination: `description-xml-tag` FAIL (offset 47), `description-tag-split` PASS
(folded `<ski`/`lls>`), `description-angle-prose` PASS (`cost < 5 … > 3`).

## 6. Live-defect surface the C2 edit must also touch

* `SKILL.md:14` — the `<skills>` token, offset 750 in the folded value.
* `SKILL.md:151` — the portability paragraph says *"This file's own description still carries
  `<skills>`; the repair is planned"*. After the edit this sentence becomes false; it must be
  updated in the same change or the file asserts a stale fact.
* `.tower/jj-probe/kotoba-shokunin/SKILL.md` carries the identical 814-char description; it is not
  the lane's gate target, but any future sweep of `.tower/` would flag it.

## 7. Fleet calibration (21 `SKILL.md` under the fleet root)

Only `kotoba-shokunin/SKILL.md` and its `.tower` copy carry a tag (`<skills>`); the other 19 have
no `<`/`>`-shaped tag in `description`. 11 files parse under strict YAML and are identical to the
parser's value modulo the trailing newline (0 differ in content); 10 raise `ScannerError` yet the
parser accepts them. All 21 frontmatters are simple — no column-0 comments, no blank lines, no
more-indented continuations, no tabs — so on today's corpus the trailing-newline chomping is the
only live divergence.

## 8. Commands run (exit codes)

* `git rev-parse HEAD` → `c61a973…`, exit 0.
* `python3 probe.py` (scratch) — SKILL.md parser vs YAML: 814/815, diff empty, exit 0.
* `python3 probe2.py` — 27-case divergence matrix, exit 0.
* `python3 probe3.py` — 13-case tag-formation matrix, exit 0.
* `python3 verifiers/verify_skill_checklist.py --self-test` (scratch clone) → `0 failure(s) over
  1597 assertions`, exit 0 (baseline, before any edit).
* Prototype route A → `0 failure(s) over 1735 assertions`, exit 0; route B → `0 failure(s) over
  1597 assertions`, exit 0; both live-file probes exit 1 naming the tag.
* `git apply --check` of `C2FoldedParse.prototype.patch` on a pristine clone at BASE → "apply-check
  OK", and after applying, `--self-test` → `0 failure(s) over 1735 assertions`.
* Fleet scan scripts (parser + PyYAML over 21 files) exit 0; YAML errors caught per file.

## 9. What I did NOT check

* Did not run the lane's real gate on the unmodified lane repo (`--self-test` ran in the scratch
  clone; a full live run there reports clone-layout artifacts — `name_directory` FAIL because the
  clone directory is named `lane`, and citation FAILs because `../.ufo`/`../PROTOCOL.md` escape the
  clone).
* Did not verify what an Anthropic/omp loader does with a `<skills>`-bearing description (S003 is
  taken as the rule; no live router was exercised).
* Did not test CRLF beyond `splitlines()` (parser and YAML agree on the fixture I ran).
* Did not measure aliases/anchors, flow-style mappings, or multi-document frontmatter; no fleet file
  uses them.
* No tools installed (PyYAML 6.0.3 was already present and used only as an oracle).
