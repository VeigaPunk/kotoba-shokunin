verdict: HOLDS — mutation-attacked OC-3a (`for(let O of T.instructions)`, verify_surfaces.py:392-395) on the real frozen opencode 1.19.3 dump: all 8 anchor-removal/corruption mutants exit 1 with `FAIL surfaces.opencode_extract` naming `opencode:config/instructions`/`OC-3a`; identifier renames stay green; measured width limits are 3 false-red syntax shapes (too narrow) and 1 surviving same-shape decoy (too wide), both inside the rule set's own DOCUMENTED LIMITS.

## Scope

Target rule: OC-3a in `verifiers/verify_surfaces.py` at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f.
- Rule wiring: `verifiers/verify_surfaces.py:392-395` (`OC_DECLARED_RE = for\s*\(\s*let\s+<id>\s+of\s+<id>\.instructions\s*\)`), consumed at `:470-472` — `rule("OC-3a", ["opencode:config/instructions"], declared, ["for(let <v> of <v>.instructions)"])`.
- Gate: `check_opencode_extract` at `:727-760` (two-way parity + never-vacuous).
- Prior fixture expectation: `:1035-1048`, row `:1039` (`strings-opencode-drop-oc3a.txt` → must name `opencode:config/instructions`).
- Census calibration: `corpus/knowledge/instruction-surface-census-round13.md:254` pins the anchor to "dump 443993" — matches my measurement exactly (single occurrence, line 443993, bytes 10894343–10894371 of the 67839091-byte dump).

## Environment

Scratch clone `/fast/scratch/kotoba-r47/w2/W2DropOC3a-2/kotoba-shokunin` checked out detached at 7ad7fad (verified `git rev-parse HEAD` → `7ad7fadf…`). Frozen substrate digest-verified before probing:
`cd /fast/scratch/kotoba-r47/shared && sha256sum -c SHA256SUMS` → exit 0, `omp-18.12.5.strings: OK`, `opencode-1.19.3.strings: OK`, both binaries OK. The real dump was copied to scratch (`mut/`), never into the lane. No tools installed (none needed). No lane production file touched; artifacts are the two `W2DropOC3a.*` files plus this report.

## Baseline (before)

`python3 verifiers/verify_surfaces.py --repo . --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings /fast/scratch/kotoba-r47/shared/opencode-1.19.3.strings` → **exit 0**, 7/7 PASS, key line:
`PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.

Anchor census on the pristine dump: `grep -c 'for(let <id> of <id>.instructions)'` → **1** hit, line 443993 (corroborates census § row at `corpus/knowledge/instruction-surface-census-round13.md:254`).

## Battery

Driver: `mut/run_probes.py` (scratch). Each mutant applies exactly one edit at the single anchor span, runs the verifier with `--omp-strings <frozen omp> --opencode-strings <mutant> --json`. Full machine table: `W2DropOC3a.probes.json`. Result: **16 probes, 0 unexpected** per classification.

Kill mutants (each must exit 1 naming owner/rule) — **8/8 KILLED**, and in every case `surfaces.opencode_extract` is the *only* failing check, so exit 1 is attributable to OC-3a's own gate:

| mutant | edit at line 443993 | exit | verdict |
|---|---|---|---|
| kill-drop-whole | anchor deleted | 1 | KILLED |
| kill-no-r-in-for | `fo(let O of T.instructions)` | 1 | KILLED |
| kill-no-open-paren | `forlet O of T.instructions)` | 1 | KILLED |
| kill-drop-let | `for(O of T.instructions)` | 1 | KILLED |
| kill-drop-of | `for(let O T.instructions)` | 1 | KILLED |
| kill-member-corrupt | `for(let O of T.instrutions)` | 1 | KILLED |
| kill-no-close-paren | `for(let O of T.instructions` | 1 | KILLED |
| kill-of-to-in | `for(let O in T.instructions)` | 1 | KILLED |

Canonical repro (`kill-drop-whole`), human output, exit 1:
```
FAIL surfaces.opencode_extract: declared opencode class(es) produced by no rule: opencode:config/instructions; rule(s) matched nothing: OC-3a (owns opencode:config/instructions; missing for(let <v> of <v>.instructions))
```

Equivalent-but-renamed anchors (same JS semantics):

| mutant | text | exit | verdict |
|---|---|---|---|
| eq-rename-loop-var | `for(let Qz9 of T.instructions)` | 0 | matched (robust to minifier identifier renames) |
| eq-rename-object | `for(let O of Vv.instructions)` | 0 | matched (object rename robust) |
| eq-spaced | `for ( let O of T.instructions )` | 0 | matched (`\s*` tolerance) |
| eq-multiline-wrap | `of\nT.instructions` | 0 | matched (`\s+` covers wrapped chunks) |
| eq-const-decl | `for(const O of T.instructions)` | 1 | **FALSE-RED** (too narrow to `let`) |
| eq-optional-chain | `for(let O of T?.instructions)` | 1 | **FALSE-RED** (no `?\.` in pattern) |
| eq-for-await | `for await(let O of T.instructions)` | 1 | **FALSE-RED** (`for\s*\(` rejects `await`) |

Surviving mutant (exit 0) — **decoy-elsewhere**: real anchor deleted at line 443993 AND `for(let X of Y.instructions)` appended in an unrelated chunk at EOF → verifier exit 0, 7/7 PASS, `opencode_extract PASS 9/9`. Byte-exact diff: `W2DropOC3a.decoy-diff.txt` (pristine sha256 `f4d8f34a…`, mutant sha256 `dbd866e7…`, −28/+30 bytes, both edits asserted against the frozen original).

## Too narrow or too wide?

Both, in measured, bounded ways — neither breaks the round's claim:
- **Too narrow (false reds, fail-closed):** `const`-declared, optional-chained, and `for await` forms of the same loop are real JS equivalents the regex rejects. If upstream ever minifies to those shapes on a healthy binary, OC-3a flags drift (exit 1) — a false alarm, never a silent pass. This is exactly the header's DOCUMENTED LIMITS at `verify_surfaces.py:33-46` ("a loader shape minified differently … is out of the set"; the check "proves set parity over this documented extraction, never existential completeness").
- **Too wide (surviving decoy, fail-open):** OC-3a is a text-shape witness owning a fixed class id — any `for(let <v> of <v>.instructions)` anywhere in the dump satisfies it, so the real consumer can be deleted while a same-shape string survives elsewhere. Also within the documented limit ("a compiled-in call shape proves the loader path exists in the binary, not that it fires at runtime or reaches a prompt", `:43-45`). Round 47's tightening of OC-3b to require `.filter(` (`:390-391`) shows the authors reason in exactly these terms; OC-3a carries the same inherent witness limitation, now measured rather than assumed.

The claim under attack (C1 freshness arm for opencode 1.19.3: OC-3a re-derived on the frozen dump and killing dropped/corrupted anchors of the real loop) **holds**: 8/8 destructive mutants die loudly and correctly attributed; the census's dump-line citation (443993) is byte-accurate; the existing self-test fixture row (`:1039`) matches real-dump behavior.

## What I did NOT check

- Runtime firing of the loop in the actual binary (witness rule is static by design; excluded by `:43-45`).
- OC-1/OC-2/OC-3b/OC-4/OC-5/OC-6 mutation behavior on the real dump (other seats' scope; OC-3b only touched where stated).
- omp-side rules and `check_substrate_pins.py`/checklist gates (other seats).
- Whether the 1.19.3 bundle can legitimately contain `const`/`?.`/`for await` shapes at this site (probed as hypothetical equivalents, not observed upstream forms).
- Self-test regeneration or fixture edits (production files read-only to this seat).
