# FrontierRows — round-51 drafted append-only updates (report)

Result: drafts delivered for the four still-unlanded append-only surfaces (corpus/README.md § Frontier
row `Loader-rule freshness`, § Known gaps sibling-arbitration paragraph, PROVINCE.md § Core and
§ Frontier); the three requested index rows and the D3 row-72 correction are **already landed** in the
lane and verified here; C1 and C2 both land (measured at HEAD `59903b2`).

## Drafted text (ready to paste; anchors measured at HEAD `59903b2`)

### Block A — corpus/README.md line 88, replace the `Loader-rule freshness` row (3 cells)

Same cell width as the live row; append the round-51 clause inside the "why not held" cell:

```
| Loader-rule freshness | round 51: omp 18.12.6 re-derived and re-pinned — surfaces 7/7 and pins 3/3 at default resolution (`python3 -B verifiers/verify_surfaces.py --json` → `pass 7`, `fail 0`, exit 0; `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3 pins hold`, exit 0; the round-47 "omp 18.12.5 … 7/7 … 3/3" figures are the previous state, `lessons/round-47.md`). The loader-registration callees rotated again to `bq`/`Kl`/`Ho`, and the group-variable leg needed a module-scoped binding rule (the dump-wide first-seen table drops `S$` as a conflicting rebind), so the extraction rule changed with the pin. Not held: the omp extractor is still a callee-name allowlist — the lane's own record names 4 renamed-callee generations (3 at base `43ca0bfb`), counted from the self-test arm comments of `verifiers/verify_surfaces.py` and the `omp_round*_note` keys of `verifiers/baseline.json` — so the next minifier rename is again a red gate plus a hand re-derivation (wider history: 5 omp rebuilds since round 18 renamed the callees, per `.ufo/waves/round-51/build/OmpRenameHistory.md`; the omp 18.12.3 rebuild's callee names were never recorded) | a callee-name-independent omp call-shape rule with a must-fail rename fixture — round 51 made the group leg scope-aware, the callee leg is still a name list; an opencode lineage probe that names which generation a dump carries (`knowledge/instruction-surface-census-round13.md` § B′) |
```

### Block B — corpus/README.md § Known gaps, sibling-arbitration bullet (append after `:132`)

Insert a new paragraph after `  overlapping descriptions (census entry, round-50 section).` (line 132),
two-space indent, before the `- opencode-side offer` bullet:

```
  **Round 51 (append-only):** the overlap-lever knowledge now lives in Core: each of the 7 pinned
  clients documents a lever, other than description wording, that removes one named skill from the
  model's candidates — Copilot SDK `disabledSkills`; Copilot CLI `ignoredSkillsLocations`; VS Code
  `disable-model-invocation`; Claude Code `disable-model-invocation: true`; opencode permission
  `deny`; Gemini CLI `/skills disable <name>`; Codex `allow_implicit_invocation` (entry
  `knowledge/skill-overlap-levers-round51.md`; `python3 -B ../verifiers/check_overlap_levers.py
  --rev <rev>` → `overlap levers backed 7 of 7 clients`). None of these levers decides between two
  skills that both remain candidates — each removes one of them, so the round-50 negative (no client
  documents a rule between two differently named author-written skills whose descriptions both match)
  stands, and whether removing one of an overlapping pair, or naming the neighbour, improves routing is
  still unmeasured on any harness.
```

### Block C — PROVINCE.md § Core, sibling-arbitration bullet (append to line 17)

```
 Round 51: the documented per-client overlap levers join Core — each of the 7 pinned clients documents
 a lever, other than description wording, that removes one named skill from the model's candidates
 (`corpus/knowledge/skill-overlap-levers-round51.md`; `verifiers/check_overlap_levers.py` prints
 `overlap levers backed 7 of 7 clients`), none of them is a tie-break between two skills that both stay
 candidates, and the round-50 finding that no client documents a rule between two differently named
 author-written skills whose descriptions both match stands unrevoked.
```

### Block D — PROVINCE.md § Frontier line 23, sibling arbitration clause (append inside the parenthetical)

Replace the `open:` clause tail to:

```
sibling arbitration clauses (round 49: the census moved to Core; round 50: kotoba's own description
names the 9 `adjacent` lanes; round 51: the per-client overlap levers moved to Core — 7 of 7 clients
document a non-wording removal lever, and none of them is a tie-break; open: whether naming a lane, or
removing one of an overlapping pair, improves routing is unmeasured on any harness)
```

### Block E — PROVINCE.md § Frontier line 24, loader-rule freshness bullet (append)

```
 **Round 51:** omp 18.12.6 re-derived and re-pinned — surfaces 7/7, pins 3/3 at default resolution; the
 loader-registration callees rotated again to `bq`/`Kl`/`Ho` and the group-variable leg needed a
 module-scoped binding rule, so the extraction rule changed with the pin. Still not held: re-derivation
 after a rebuild is manual — the omp extractor is still a callee-name allowlist (4 renamed-callee
 generations in the lane's own record, 3 at base), and opencode changed lineage under the same path
 family.
```

## Landed (verified at HEAD `59903b2`; no action needed)

- corpus/README.md:75 — index row for `corpus/knowledge/skill-overlap-levers-round51.md` (File cell
  `knowledge/skill-overlap-levers-round51.md`): present, mentions the counter and removes a skill.
- corpus/README.md:76 — index row for `corpus/lessons/round-51.md` (File cell `lessons/round-51.md`).
- corpus/README.md:74 — index row for `corpus/lessons/round-50-verifier-spotcheck.md` (File cell
  `lessons/round-50-verifier-spotcheck.md`): present; `grep -c round-50-verifier corpus/README.md` →
  1 (was 0), and `corpus.index.unindexed` is now PASS 0.
- corpus/README.md:72 — D3 basis-cell correction landed and matches the withdrawn/corrected scope.

## Evidence

- `python3 -B verifiers/verify_surfaces.py --json` → `pass 7`, `fail 0`, exit 0 (at HEAD).
- `python3 -B verifiers/check_substrate_pins.py` → `OK 3/3 pins hold`, exit 0.
- `git -C /home/vgpnk/Projects/shokunin/kotoba-shokunin show 34cfffbb:verifiers/verify_surfaces.py | grep -n "renamed the callees\|renamed callees again"` → line 877 and 886 at base; same at HEAD.
- Rename count command (scoped to the two prescribed sources: the self-test arm comments + `omp_round*_note` keys):
  `python3 -B /fast/scratch/hyaku/kotoba-r51/build/FrontierRows/count_cmd.sh 43ca0bfb…` → `DISTINCT … 3 ['Co/Dl/Hj','I5/Gl/Mo','lq/Xl/Fo']`, exit 0;
  `… count_cmd.sh 34cfffbb…` → `DISTINCT … 4 ['Co/Dl/Hj','I5/Gl/Mo','bq/Kl/Ho','lq/Xl/Fo']`, exit 0.
- `python3 -B verifiers/check_overlap_levers.py --rev 34cfffbb…` → `overlap levers backed 7 of 7 clients`, exit 0.
- `python3 -B verifiers/verify_corpus_integrity.py --json` at HEAD → 8/9 PASS; the sole DRIFT is the carried `corpus.pointers.report_dead 2` (closure-owned round-48 spot-check, recorded at READINGME:68).

## Findings / notes for the L1

1. The rename count is 3→4 named generations when scoped to the two prescribed sources; the wider
   git-level record (OmpRenameHistory seat) counts 5 rebuilds since round 18 that renamed the callees,
   one of which (omp 18.12.3) had its callee names never recorded — the 4th named generation is the
   bq/Kl/Ho one this round adds.
2. The corpus index rows for the two new files only become live when the files exist and are tracked
   (measured: stale_patterns/missing_paths 1 each before; 0 after) — this landing is already done for
   the first round thus, the lesson row and the spot-check row.
