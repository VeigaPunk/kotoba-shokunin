verdict: PARTIAL — OC-3b's filter anchor survives attack (site-unique, killed all 8 kill-mutants), but its render anchor is TOO WIDE: 2 surviving mutants delete Instruction.system's entire render block and the full 7-check battery stays green, because the dump-wide `Instructions from: ` check is satisfied by the OC-6/v2 subsystem's own two copies.

# W2DropOC3b — mutation probe of OC-3b (remote `.filter(` + `Instructions from: `)

Target at 7ad7fadfc09354b74fb66605dfb0c1182c115a2f: `verifiers/verify_surfaces.py:396-400` (anchors `OC_REMOTE_FILTER_RE`, `OC_REMOTE_RENDER = "Instructions from: "`), conjunction at `:473-474` (`OC_REMOTE_FILTER_RE.search(dump) is not None and OC_REMOTE_RENDER in dump`), rule declaration at `:475-477` (owns `opencode:config/instructions-remote`), consumer `check_opencode_extract` at `:727-761`.

## Method

- Scratch clone at 7ad7fad: `/fast/scratch/kotoba-r47/w2/W2DropOC3b/kotoba-shokunin` (detached HEAD verified: `7ad7fad round-47: C1 re-derive+re-pin …`).
- Source dump copied-by-derivation from the frozen substrate (mutant dumps written to `/fast/scratch/kotoba-r47/w2/W2DropOC3b/mutants/`, NOT into the lane): src sha256 `f4d8f34ae02a2411eb5e30203421b6fcdfa81b83e96b768bbcf404504a297bc3` — matches `SHA256SUMS` beside the frozen dump.
- All surgery offset/exact-string based with `count==1` assertions; per-mutant sha256 in `W2DropOC3b.mutants.json`.
- Runner (exit codes inline below):
  `python3 verifiers/verify_surfaces.py --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings --opencode-strings <mutant> --check surfaces.opencode_extract`

## Baseline (real dump)

Full battery: exit 0, all 7 checks PASS (`W2DropOC3b.baseline-full.txt`), incl.
`PASS surfaces.opencode_extract: opencode extraction 9/9 declared class(es) from 7/7 rules (OC-1, OC-2, OC-3a, OC-3b, OC-4, OC-5, OC-6)`.

Dump anatomy on the real 1.19.3 dump:
- Filter regex: exactly **1 match** (offset 10894741, var `q`, gap `??[])` = 4 chars), inside `Instruction.system` (its `fn("Instruction.system")` registers @10894668). The round-47 tightening did de-mask the a-loop: the old 2-hit problem is gone.
- Render literal `Instructions from: `: **4 occurrences in 2 subsystems** — @10894959 (`Instruction.system` local render `O[R]`), @10895024 (`Instruction.system` remote render `U[R]`), @10895604 (v2 `instruction-context` claims-walk), @12867004 (v2 `XP()` joiner). The last two belong to the OC-6 subsystem, not OC-3b's.

## Surviving mutants (render anchor too wide) — repro included

Repro for both (also runs the FULL battery for R2):

```
cd /fast/scratch/kotoba-r47/w2/W2DropOC3b/kotoba-shokunin
python3 verifiers/verify_surfaces.py \
  --omp-strings /fast/scratch/kotoba-r47/shared/omp-18.12.5.strings \
  --opencode-strings /fast/scratch/kotoba-r47/w2/W2DropOC3b/mutants/R2_del_both_system_renders.strings
# exit 0; all 7 checks PASS  (saved: W2DropOC3b.R2_full_battery.txt)
```

- **R1** `R1_del_remote_render_only.strings` — deletes ONLY the remote render anchor @10895024, i.e. exactly the render OC-3b's comment claims to witness ("Instruction.system fetches the remote entries and renders them", `verify_surfaces.py:388-390`). Deleted span: ``[`Instructions from: ${q}<LF>${U[R]}`]:[]``. → **exit 0**, `PASS … 9/9 from 7/7 (… OC-3b …)`.
- **R2** `R2_del_both_system_renders.strings` — deletes BOTH `Instruction.system` render spans (@10894959 ``[`Instructions from: ${q}<LF>${O[R]}`]:[]`` and @10895024 remote). The entire render block of the witnessed function is gone; `<LF>` is a real 0x0A byte in the dump. → **exit 0** on the scoped check AND **exit 0 on the full 7-check battery** (`W2DropOC3b.R2_full_battery.txt`: literal_present, no_uncovered_class, opencode_extract, table_parity, literal_parity, kind_parity, excluded_reason all PASS).

Why it survives: `OC_REMOTE_RENDER in dump` (`verify_surfaces.py:474`) is a whole-dump substring test. The v2 `instruction-context` subsystem legitimately contains the same literal twice (@10895604, @12867004), so on any 1.19.3-lineage dump that keeps OC-6 alive, OC-3b's render half can never fail — its failure signal is coupled to OC-6's survival, not to the site it owns. Consequence: the render half of the conjunction is vacuous for detecting loss of the remote render; only the filter half actually bites.

- R3 `R3_del_v2_claims_render.strings` (delete the v2-side anchor @10895604) → exit 0, as expected — recorded to show the anchor is not site-scoped in either direction.

## Killed mutants (all exit 1, `FAIL surfaces.opencode_extract` naming `opencode:config/instructions-remote` AND rule `OC-3b`)

Every kill produces: `declared opencode class(es) produced by no rule: opencode:config/instructions-remote; rule(s) matched nothing: OC-3b (owns opencode:config/instructions-remote; missing .instructions….filter((q)=>q.startsWith("https://")||q.startsWith("http://")) + Instructions from: )` — the harness requirement (exit 1 naming owned class(es) or the rule) holds for all 8.

| id | mutation at the unique site | exit |
|---|---|---|
| F1 | `.filter(` → `.f1lter(` | 1 |
| F2 | `q.startsWith("https://")` → `q.startsWith("https:")` | 1 |
| F3 | rename first body var `q`→`z` (unbound; breaks regex backreference) | 1 |
| F4 | insert `.map(x=>x.trim())` before `.filter(` — gap 4→21 chars, exceeds `[^;]{0,20}?` | 1 |
| F5 | arrow `.filter(…)` rewritten as strictly equivalent `for…of`+`if` push loop | 1 |
| R4 | delete all 4 render anchors | 1 |
| R5 | `Instructions from: ` → `Instructions from :` (all 4) | 1 |
| R6 | `Instructions from: ` → `Instructions from ` (all 4; drop colon) | 1 |

Robustness probe E1: minifier-style rename of the arrow var `q`→`zz` in BOTH positions → **exit 0** (the `\1` backreference handles it). The filter anchor is robust to identifier renames.

## Narrow or wide?

- **Filter half: too narrow, but narrow-by-design.** F4 and F5 are renamed-but-equivalent anchors (same semantics, different syntax: pipeline insertion; arrow→loop) and both false-red → exit 1 forces re-derivation. That is the intended C1 drift-tripwire behavior, not a silent-pass risk; it only fires if upstream/minified output changes shape. F1–F3 corruption is correctly killed. Site-uniqueness on 1.19.3 (1 regex match) means no cross-site masking today.
- **Render half: too wide — the real defect.** R1/R2 surviving (R2 at full-battery level) shows the anchor passes while the behavior it documents is deleted. Minimal fix [INFERENCE]: scope the literal to the filter site — require ≥1 `Instructions from: ` within ~400 bytes AFTER the `OC_REMOTE_FILTER_RE` match (owned renders sit at +138/+203; foreign v2 renders at +783 and +1,972,183), or require both renders in-window; v2's renders stay OC-6's business.

## Verdict on the claim

C1's OC-3b portion as landed at 7ad7fad: the round-47 `.filter(` tightening is real and effective (a-loop de-masked; 5/5 filter mutants die; var-rename robust), but OC-3b still cannot detect loss of the remote render on any dump where OC-6 lives. Claim C1 "operability of the OC-3b gate" is therefore PARTIAL at the rule level: exit-1-on-corruption holds; exit-1-on-behavior-loss does not for the render half.

## What I did NOT check

- omp-side rules (OC lane only); behavior of the other 6 surfaces checks under filter-side mutants (only R2 was run against the full battery).
- Whether a future opencode release could gain a second `.instructions….filter(https||http)` site (would re-open cross-site masking of the filter half); static count on 1.19.3 only.
- Semantic equivalence of F4 beyond local reasoning: `.map(x=>x.trim())` alters values if URLs carry whitespace — F4 is a near-equivalent shape probe, not a value-preserving rewrite (F5 is strictly equivalent).
- Byte-level identity of my mutant surgery against a fresh `strings` re-dump of the binary; surgery was anchored on the provided frozen dump (sha verified against SHA256SUMS).
- No tools were installed or upgraded for this probe (stock `python3`; pacman untouched per the host-wide pause).

## Artifacts (this directory)

`W2DropOC3b.md` (this report), `W2DropOC3b.mutants.json` (full manifest: shas, expect/exit/verdict per mutant), `W2DropOC3b.baseline-full.txt`, `W2DropOC3b.R2_full_battery.txt`, `W2DropOC3b.<mutant-id>.txt` ×12 (raw verifier output per mutant). Mutant dumps (~68 MB each) retained only under `/fast/scratch/kotoba-r47/w2/W2DropOC3b/mutants/`, never in the lane.
